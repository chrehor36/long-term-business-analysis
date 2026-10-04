#!/usr/bin/env python3
"""BT-17 Universe A: the S&P 500 replication.

Re-scores the 13 committed corrected point-in-time screens (2013..2025 anchors)
with today's price data: 1y (context) / 3y / 5y forward windows, passed vs the
rejected names of the SAME screen at the SAME anchor, SPY beside for the return
leg. Pre-registration b853dcf governs. Reuses bt17_microcap's cache and chart
conventions (monthly adjclose ratios only; a series starting after the anchor
is a recycled ticker, refused; series ending early = no-data class).
"""
import csv, glob, os, sys
from datetime import date

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
BT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from bt17_microcap import chart, shift_month  # noqa: E402

TODAY_M = "2026-08"


def main():
    screens = {}
    for p in sorted(glob.glob(os.path.join(BT, "2026-07-25 CORRECTED Screen *.csv"))):
        anchor = os.path.basename(p).split("Screen ")[1][:10]
        rows = list(csv.DictReader(open(p, encoding="utf-8")))
        screens[anchor] = [(r["ticker"], r["passed"] == "True") for r in rows
                           if r["passed"] in ("True", "False")]
    tickers = sorted({t for rows in screens.values() for t, _ in rows} | {"SPY"})
    print(f"anchors={len(screens)} union tickers={len(tickers)}")

    series, failed = {}, []
    for i, t in enumerate(tickers):
        try:
            _closes, adjs, _sp = chart(t, i)
            series[t] = adjs
        except Exception:
            failed.append(t)
        if (i + 1) % 50 == 0:
            print(f"  charts {i+1}/{len(tickers)} ({len(failed)} failed)")
    print(f"charts done, failed={len(failed)}: {failed[:12]}")

    out = os.path.join(BT, "2026-08-28 BT-17 SP500 rescore.csv")
    w = csv.writer(open(out, "w", newline="", encoding="utf-8"))
    w.writerow(["anchor", "ticker", "passed", "r1", "r3", "r5", "note"])

    pooled = {"r1": {}, "r3": {}, "r5": {}}
    spy = {}
    for anchor, rows in sorted(screens.items()):
        am = anchor[:7]
        for lbl, k in (("r1", 12), ("r3", 36), ("r5", 60)):
            exit_m = shift_month(am, k)
            if exit_m > TODAY_M:
                continue
            s = series.get("SPY", {})
            if am in s and exit_m in s:
                spy.setdefault(lbl, {})[anchor] = s[exit_m] / s[am] - 1.0
            for t, passed in rows:
                adjs = series.get(t)
                note, r = "", None
                if not adjs:
                    note = "no_chart"
                elif am not in adjs:
                    first = min(adjs) if adjs else None
                    note = "recycled" if (first and first > am) else "no_entry"
                elif exit_m not in adjs:
                    note = "no_data"
                else:
                    r = adjs[exit_m] / adjs[am] - 1.0
                if lbl == "r1":
                    w.writerow([anchor, t, passed, r, "", "", note])
                key = (anchor, passed)
                pooled[lbl].setdefault(key, []).append(r)

    print("\n== POOLED (per window, passed vs rejected; no-data shown both ways) ==")
    for lbl in ("r1", "r3", "r5"):
        for passed in (True, False):
            vals, nod, n = [], 0, 0
            for (anchor, p), lst in pooled[lbl].items():
                if p != passed:
                    continue
                for r in lst:
                    n += 1
                    if r is None:
                        nod += 1
                    else:
                        vals.append(r)
            if not vals:
                continue
            losses = [v for v in vals if v < 0]
            print(f"{lbl} {'PASS' if passed else 'REJ '}: slots={n} scored={len(vals)} "
                  f"nodata={nod} mean={sum(vals)/len(vals):+.1%} "
                  f"lossfreq_ex={len(losses)/len(vals):.1%} "
                  f"lossfreq_incl={(len(losses)+nod)/n:.1%} "
                  f"depth={(sum(losses)/len(losses)) if losses else 0:+.1%}")
        if lbl in spy:
            m = sum(spy[lbl].values()) / len(spy[lbl])
            print(f"{lbl} SPY : anchors={len(spy[lbl])} mean={m:+.1%}")

    print("\n== RETURN LEG per anchor (equal-weight passed basket minus SPY, r1) ==")
    for anchor in sorted(screens):
        key = (anchor, True)
        vals = [r for r in pooled["r1"].get(key, []) if r is not None]
        if vals and anchor in spy.get("r1", {}):
            print(f"  {anchor}: basket {sum(vals)/len(vals):+.1%}  SPY {spy['r1'][anchor]:+.1%}  "
                  f"delta {sum(vals)/len(vals)-spy['r1'][anchor]:+.1%}  n={len(vals)}")
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
