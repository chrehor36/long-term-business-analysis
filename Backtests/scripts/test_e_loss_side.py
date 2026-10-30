#!/usr/bin/env python3
"""TEST E — the loss leg of Ground Rule 7 [E1-17].

Pre-registration: Framework/v4/TEST E - PREREGISTRATION - the loss leg.md,
committed 49be7b4 BEFORE this script produced a number. The criteria there
govern; nothing here re-decides them.

Panel: the eight corrected point-in-time screens (2013-2020 anchors), every name
carrying the screen's own passed flag. Control = the rejected names of the SAME
screen at the SAME anchor. Windows: 3y and 5y (Ground Rule 5). Returns: monthly
adjclose RATIOS only (the house rule -- adjclose is never a price).

Guards, per the pre-registration:
  - a series starting after the anchor is a RECYCLED TICKER -> refused
  - a series ending before the window closes is a DELISTING -> counted separately,
    never silently dropped; the loss rates are therefore UNDERSTATEMENTS
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import csv, glob, json, os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
BT = os.path.dirname(HERE)
ROOT = os.path.dirname(BT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources as S

ANCHORS = [f"{y}-06-30" for y in range(2013, 2021)]


def monthly(ticker):
    """Monthly adjclose series {YYYY-MM: adj} from one fetch, cached a month."""
    import urllib.error
    try:
        txt = S._get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
                     f"?range=max&interval=1mo",
                     S.WEB_UA, f"px1mo_{ticker}.json", max_age_h=24 * 30)
        r = json.loads(txt)["chart"]["result"][0]
    except Exception:
        return None
    ts = r.get("timestamp") or []
    adj = (r.get("indicators", {}).get("adjclose") or [{}])[0].get("adjclose") or []
    out = {}
    from datetime import datetime
    for t, a in zip(ts, adj):
        if a is None:
            continue
        try:
            out[datetime.utcfromtimestamp(t).strftime("%Y-%m")] = a
        except (OSError, OverflowError, ValueError):
            continue
    return out or None


def at_or_before(series, ym):
    ks = [k for k in series if k <= ym]
    return (max(ks), series[max(ks)]) if ks else (None, None)


def month_add(ym, n):
    y, m = int(ym[:4]), int(ym[5:7])
    m += n
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    return f"{y}-{m:02d}"


def window_return(series, anchor_ym, months):
    """(status, ret). status: OK | RECYCLED | DELISTED | NO_ENTRY."""
    if min(series) > anchor_ym:
        return "RECYCLED", None          # series starts after the anchor
    ek, ev = at_or_before(series, anchor_ym)
    if not ek or ek < month_add(anchor_ym, -3):
        return "NO_ENTRY", None          # no price within a quarter of the anchor
    target = month_add(anchor_ym, months)
    xk, xv = at_or_before(series, target)
    if not xk or xk < month_add(target, -3):
        return "DELISTED", None          # series ends before the window closes
    return "OK", xv / ev - 1.0


def main():
    panel = []
    for p in sorted(glob.glob(os.path.join(BT, "2026-07-25 CORRECTED Screen 20*.csv"))):
        anchor = os.path.basename(p).split()[-1][:10]
        if anchor not in ANCHORS:
            continue
        for r in csv.DictReader(open(p, encoding="utf-8-sig")):
            panel.append((anchor, r["ticker"], r["passed"] == "True"))
    tickers = sorted({t for _, t, _ in panel})
    print(f"panel: {len(panel)} name-anchor slots, {len(tickers)} tickers, "
          f"{len(ANCHORS)} anchors", flush=True)

    series, dead = {}, []
    for i, t in enumerate(tickers, 1):
        s = monthly(t)
        if s:
            series[t] = s
        else:
            dead.append(t)
        if i % 50 == 0:
            print(f"  ...{i}/{len(tickers)} fetched ({len(dead)} no-data)", flush=True)
    spy = monthly("SPY")
    print(f"fetched {len(series)}/{len(tickers)}; NO DATA: {len(dead)}", flush=True)

    rows = []
    for anchor, t, passed in panel:
        ym = anchor[:7]
        if t not in series:
            rows.append(dict(anchor=anchor, ticker=t, passed=passed,
                             w3="NO_DATA", r3=None, w5="NO_DATA", r5=None))
            continue
        s3, r3 = window_return(series[t], ym, 36)
        s5, r5 = window_return(series[t], ym, 60)
        rows.append(dict(anchor=anchor, ticker=t, passed=passed,
                         w3=s3, r3=r3, w5=s5, r5=r5))

    out_csv = os.path.join(BT, "2026-08-28 TEST-E Loss Panel.csv")
    with open(out_csv, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    def side(rows_, flag, wk, rk):
        grp = [r for r in rows_ if r["passed"] == flag]
        ok = [r for r in grp if r[wk] == "OK"]
        losses = [r for r in ok if r[rk] < 0]
        depth = (sum(r[rk] for r in losses) / len(losses)) if losses else 0.0
        return dict(slots=len(grp), scored=len(ok),
                    delisted=sum(1 for r in grp if r[wk] == "DELISTED"),
                    recycled=sum(1 for r in grp if r[wk] == "RECYCLED"),
                    no_data=sum(1 for r in grp if r[wk] in ("NO_DATA", "NO_ENTRY")),
                    loss_n=len(losses),
                    loss_rate=len(losses) / len(ok) * 100 if ok else None,
                    mean_depth=depth * 100,
                    median_ret=sorted(r[rk] for r in ok)[len(ok) // 2] * 100 if ok else None)

    summary = {}
    for wk, rk, label, months in (("w3", "r3", "3y", 36), ("w5", "r5", "5y", 60)):
        p = side(rows, True, wk, rk)
        f_ = side(rows, False, wk, rk)
        spy_rets = {}
        for anchor in ANCHORS:
            st, rr = window_return(spy, anchor[:7], months)
            spy_rets[anchor[:4]] = round(rr * 100, 1) if st == "OK" else st
        summary[label] = dict(passed=p, rejected=f_, spy_window_returns_pct=spy_rets)

    # per-anchor loss rates, both windows -- pooling can hide an anchor-level flip
    per_anchor = {}
    for anchor in ANCHORS:
        ar = [r for r in rows if r["anchor"] == anchor]
        per_anchor[anchor[:4]] = {
            lab: {grp: (lambda g: (sum(1 for x in g if x[rk] < 0) / len(g) * 100)
                        if g else None)(
                      [r[rk] for r in ar if r["passed"] == fl and r[wk] == "OK"
                       and r[rk] is not None] and
                      [r for r in ar if r["passed"] == fl and r[wk] == "OK"])
                  for grp, fl in (("passed", True), ("rejected", False))}
            for lab, wk, rk in (("3y", "w3", "r3"), ("5y", "w5", "r5"))}

    out_json = os.path.join(BT, "2026-08-28 TEST-E Summary.json")
    json.dump(dict(summary=summary, per_anchor=per_anchor, no_data_tickers=dead),
              open(out_json, "w", encoding="utf-8"), indent=1)

    print(json.dumps(summary, indent=1))
    print(f"\nwrote {os.path.basename(out_csv)} and {os.path.basename(out_json)}")
    print("\nPer the pre-registration: PASS requires passed-group loss frequency "
          "STRICTLY below rejected at BOTH windows, and mean depth no worse.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
