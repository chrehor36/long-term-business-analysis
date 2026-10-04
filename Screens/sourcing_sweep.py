#!/usr/bin/env python3
"""SOURCING SWEEP — the program's reading-list generator, parameterized.

Extends bt17_microcap's machinery (same hash-of-CIK order, same frozen statute
gate, same house-rule cap) to a wider cap band and deeper examination, and tags
each name's listing venue from the chart metadata (NYSE / Nasdaq / OTC...).
Output is A READING LIST, NEVER A BUY LIST [E5-36]. SEC-reporting names only by
construction: no filing, no run [E3-27] - dark/Pink no-information names cannot
enter.

Usage: python sourcing_sweep.py [cap_lo_M] [cap_hi_M] [target] [exam_cap]
Default: 50 2000 300 8000
"""
import csv, os, sys, time
from datetime import date

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
_argv = sys.argv[1:]
sys.argv = [sys.argv[0]]  # keep bt17_microcap's import-time argv parse inert
import bt17_microcap as M  # noqa: E402
import hashlib, json  # noqa: E402

CAP_LO = float(_argv[0]) * 1e6 if len(_argv) > 0 else 50e6
CAP_HI = float(_argv[1]) * 1e6 if len(_argv) > 1 else 2000e6
TARGET = int(_argv[2]) if len(_argv) > 2 else 300
EXAM_CAP = int(_argv[3]) if len(_argv) > 3 else 8000
ANCHOR = date.today()
AMONTH = f"{ANCHOR.year}-{ANCHOR.month:02d}"


def venue(ticker):
    p = os.path.join(M.CACHE, f"chart_{ticker}.json")
    try:
        d = json.load(open(p, encoding="utf-8"))
        meta = d["chart"]["result"][0].get("meta", {})
        return meta.get("fullExchangeName") or meta.get("exchangeName") or "?"
    except Exception:
        return "?"


def main():
    hurdle = max((M.dgs30_asof(ANCHOR) or 4.0) / 100.0, 0.04)
    print(f"SOURCING SWEEP anchor={ANCHOR} band=[{CAP_LO/1e6:.0f}M,{CAP_HI/1e6:.0f}M] "
          f"target={TARGET} exam_cap={EXAM_CAP} hurdle={hurdle:.4f}")
    tick = M.cached_json("company_tickers.json", "https://www.sec.gov/files/company_tickers.json")
    cands = sorted(tick.values(), key=lambda v: hashlib.sha256(str(v["cik_str"]).encode()).hexdigest())

    rows, examined, skip = [], 0, {}
    for c in cands:
        if len(rows) >= TARGET or examined >= EXAM_CAP:
            break
        examined += 1
        t = str(c["ticker"]).upper()
        if "-" in t or (len(t) == 5 and t[-1] in "WU"):
            skip["suffix"] = skip.get("suffix", 0) + 1
            continue
        cik = int(c["cik_str"])
        try:
            facts = M.cached_json(f"facts_{cik}.json",
                                  f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",
                                  sleep=0.12)
        except Exception:
            skip["nofacts"] = skip.get("nofacts", 0) + 1
            continue
        ni = M.ni_series(facts, ANCHOR)
        ends = sorted(ni)[-5:]
        if len(ends) < 5:
            skip["ni5"] = skip.get("ni5", 0) + 1
            continue
        sh = M.shares_asof(facts, ANCHOR)
        if not sh:
            skip["noshares"] = skip.get("noshares", 0) + 1
            continue
        try:
            closes, adjs, splits = M.chart(t, examined)
        except Exception:
            skip["nochart"] = skip.get("nochart", 0) + 1
            continue
        if AMONTH not in closes:
            skip["stale"] = skip.get("stale", 0) + 1
            continue
        meas, shares = sh
        factor = 1.0
        for sd, f in splits:
            if sd > meas:
                factor *= f
        cap = closes[AMONTH] * shares * factor
        if not (CAP_LO <= cap <= CAP_HI):
            skip["capout"] = skip.get("capout", 0) + 1
            continue
        worst5 = min(ni[e] for e in ends)
        yld = worst5 / cap
        rows.append(dict(ticker=t, cik=cik, name=c.get("title", "")[:40],
                         venue=venue(t), cap_m=round(cap / 1e6),
                         band=("micro" if cap <= 300e6 else "smallmid"),
                         worst5_ni_m=round(worst5 / 1e6, 1),
                         yld=round(yld, 5),
                         passed=(worst5 > 0 and yld >= hurdle)))
        if len(rows) % 25 == 0:
            print(f"  {len(rows)} found / {examined} examined "
                  f"({sum(1 for r in rows if r['passed'])} pass)")

    rows.sort(key=lambda r: -r["yld"])
    out = os.path.join(HERE, f"{ANCHOR} SOURCING SWEEP {CAP_LO/1e6:.0f}M-{CAP_HI/1e6:.0f}M.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    passes = [r for r in rows if r["passed"]]
    print(f"\nuniverse={len(rows)} examined={examined} passes={len(passes)} skips={skip}")
    by_v = {}
    for r in passes:
        by_v.setdefault((r["venue"], r["band"]), []).append(r)
    for (v, b), lst in sorted(by_v.items()):
        print(f"  {v:22s} {b:8s}: {len(lst)}  e.g. " +
              ", ".join(f"{r['ticker']}({r['yld']:.0%})" for r in lst[:5]))
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
