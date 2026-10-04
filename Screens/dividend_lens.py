#!/usr/bin/env python3
"""DIVIDEND LENS - re-rank the sweep universe for the dividend-compounder profile.

Operator steer 2026-08-30: "a dividend payer that also compounds over time."
Reads the committed sweep CSV plus the CACHED charts (events.dividends fetched
2026-08-30) - zero network calls. For each name: trailing-12M dividend/share,
yield on last monthly close, 5-year dividend CAGR, cut-in-last-5y flag, and
payout vs worst-5y EPS (coverage). A LENS over a reading list - still never a
buy list [E5-36]; banks/BDCs stay excluded per the 2026-08-30 directive.
"""
import csv, json, os, sys, time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(ROOT, "Backtests", "bt17_cache")
SWEEP = os.path.join(HERE, "2026-08-30 SOURCING SWEEP 50M-2000M.csv")

EXCL_BANKS_BDC = {"CUBB","MBINN","MBINL","MBINM","BCSF","NEWT","CGBD","TSLX","SCM","CPSS",
                  "CASH","UBCP","SNFCA","SBSI","PCB","FINW","PEBK","HBCP","UVSP","UNTY",
                  "OVLY","FCAP","PROV","MCB"}
ARTIFACTS = {"LADR","HOVVB","SITC","HOV","EMBC"}


def divs_and_close(ticker):
    p = os.path.join(CACHE, f"chart_{ticker}.json")
    if not os.path.exists(p):
        return None
    d = json.load(open(p, encoding="utf-8"))
    r = d["chart"]["result"][0]
    events = (r.get("events", {}) or {}).get("dividends", {}) or {}
    divs = sorted((ev["date"], ev["amount"]) for ev in events.values())
    ts = r.get("timestamp") or []
    q = r["indicators"]["quote"][0].get("close") or []
    last_close = next((c for c in reversed(q) if c is not None), None)
    return divs, last_close


def ttm(divs, asof_ts):
    return sum(a for t, a in divs if asof_ts - 365 * 86400 < t <= asof_ts)


def main():
    now = time.time()
    rows = list(csv.DictReader(open(SWEEP, encoding="utf-8")))
    out = []
    for r in rows:
        t = r["ticker"]
        if t in ARTIFACTS or t in EXCL_BANKS_BDC:
            continue
        dc = divs_and_close(t)
        if not dc:
            continue
        divs, close = dc
        if not divs or not close:
            continue
        d_now = ttm(divs, now)
        d_5y = ttm(divs, now - 5 * 365 * 86400)
        if d_now <= 0:
            continue
        yld = d_now / close
        cagr = (d_now / d_5y) ** 0.2 - 1 if d_5y > 0 else None
        cut = any(ttm(divs, now - k * 365 * 86400) < 0.95 * ttm(divs, now - (k + 1) * 365 * 86400)
                  for k in range(0, 5))
        cap = float(r["cap_m"]) * 1e6
        worst5 = float(r["worst5_ni_m"]) * 1e6
        shares_est = cap / close
        eps_worst = worst5 / shares_est if shares_est else None
        payout = d_now / eps_worst if eps_worst and eps_worst > 0 else None
        out.append(dict(ticker=t, name=r["name"][:36], venue=r["venue"], cap_m=r["cap_m"],
                        passed=r["passed"], div_ttm=round(d_now, 2), div_yield=round(yld, 4),
                        div_cagr_5y=(round(cagr, 4) if cagr is not None else ""),
                        cut_last5y=cut,
                        payout_vs_worst5=(round(payout, 2) if payout else "")))
    out.sort(key=lambda x: (-(x["div_cagr_5y"] or -1), -x["div_yield"]))
    dest = os.path.join(HERE, "2026-08-30 DIVIDEND LENS.csv")
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    print(f"names with dividends (ex banks/BDCs/artifacts): {len(out)}")
    print(f"{'tick':6s} {'yield':>6s} {'5yCAGR':>7s} {'cut?':>5s} {'payout':>7s}  gate  name")
    for x in out[:20]:
        print(f"{x['ticker']:6s} {x['div_yield']:6.1%} "
              f"{(format(x['div_cagr_5y'], '7.1%') if x['div_cagr_5y'] != '' else '     - ')} "
              f"{str(x['cut_last5y']):>5s} "
              f"{(format(x['payout_vs_worst5'], '7.2f') if x['payout_vs_worst5'] != '' else '      -')}  "
              f"{'PASS' if x['passed'] == 'True' else 'rej '}  {x['name']}")
    print(f"WROTE {dest}")


if __name__ == "__main__":
    main()
