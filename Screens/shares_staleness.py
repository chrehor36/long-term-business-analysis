#!/usr/bin/env python3
"""SHARES STALENESS AUDIT — forced by the LEVI run, 2026-08-31.

LEVI's screen entry was wrong by 10.23x. Mechanism, new and systematic:
`dei:EntityCommonStockSharesOutstanding` in SEC companyfacts goes DIMENSIONAL
(Class A / Class B) once a company has two classes, and companyfacts DROPS
dimensioned facts. So the last usable value can be the pre-IPO, pre-split,
single-class cover count - LEVI's was dated 2019-01-30, before both its March 2019
ten-for-one split and its IPO. The split guard does not save it either: a PRE-IPO
split has no market split event, so the factor is 1.0.

This audits every READ name for the same defect: how old is the share count our
tools actually used? Anything over ~18 months is SUSPECT and its cap, statute
yield and payout figures cannot be trusted without a filed-cover check.
"""
import csv, os, sys
from datetime import date

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
sys.argv = [sys.argv[0]]
import bt17_microcap as M  # noqa: E402

TODAY = date.today()
STALE_MONTHS = 18


def main():
    src = os.path.join(HERE, f"{TODAY} PREPPED LIST.csv")
    rows = [r for r in csv.DictReader(open(src, encoding="utf-8")) if r["status"] == "READ"]
    print(f"auditing {len(rows)} READ names for stale share counts "
          f"(threshold {STALE_MONTHS} months)\n")
    suspect, ok, nofacts = [], 0, 0
    for r in rows:
        t = r["ticker"]
        cik = None
        for f in os.listdir(M.CACHE):
            pass
        # cheaper: re-derive cik from the ticker map
        break
    tick = M.cached_json("company_tickers.json", "https://www.sec.gov/files/company_tickers.json")
    sec = {str(v["ticker"]).upper(): int(v["cik_str"]) for v in tick.values()}
    for r in rows:
        t = r["ticker"]
        key = next((k for k in (t, t.replace(".", "-")) if k in sec), None)
        if key is None:
            continue
        p = os.path.join(M.CACHE, f"facts_{sec[key]}.json")
        if not os.path.exists(p):
            nofacts += 1
            continue
        import json
        facts = json.load(open(p, encoding="utf-8"))
        sh = M.shares_asof(facts, TODAY)
        if not sh:
            nofacts += 1
            continue
        meas, shares = sh
        months = (TODAY.year - meas.year) * 12 + (TODAY.month - meas.month)
        if months > STALE_MONTHS:
            suspect.append((months, t, meas.isoformat(), int(shares), r["cap_m"],
                            r["statute_yield"], r["name"][:34]))
        else:
            ok += 1
    suspect.sort(reverse=True)
    print(f"clean: {ok}   no usable facts: {nofacts}   SUSPECT: {len(suspect)}\n")
    if suspect:
        print(f"{'age':>4s} {'tick':6s} {'measured':10s} {'shares':>14s} {'capM':>8s} "
              f"{'statute':>8s}  name")
        for months, t, meas, shares, cap, sy in [(s[0], s[1], s[2], s[3], s[4], s[5]) for s in suspect]:
            name = next(s[6] for s in suspect if s[1] == t)
            syf = f"{float(sy):.1%}" if sy not in ("", None) else "   n/a"
            print(f"{months:4d} {t:6s} {meas:10s} {shares:14,d} {cap:>8} {syf:>8s}  {name}")
    print("\nEvery SUSPECT row needs its share count read off the latest filed cover "
          "before its cap, statute yield or payout figure is used for anything.")


if __name__ == "__main__":
    main()
