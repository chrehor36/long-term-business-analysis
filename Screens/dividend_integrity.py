#!/usr/bin/env python3
"""DIVIDEND INTEGRITY CHECK â€” the fix forced by the COLM run, 2026-08-31.

The dividend lens computed COLM at "~9% 5-year CAGR, no cuts." The filings say the
dividend was SUSPENDED in March 2020 and has been FROZEN at $0.30 for nineteen
consecutive quarterly declarations: post-restoration growth 0.0%. Two defects, both
mine:
  1. a 5-year lookback that ANCHORS ON A SUSPENSION YEAR manufactures growth out of a
     recovery;
  2. the cut test compared trailing-12M sums, so a suspension followed by restoration
     nets out and reads as "no cut."

This runs BEFORE any name from the shortlist gets a full run. It reports, per ticker:
the payment history by year, any missed/zero quarters, whether the current rate is
FROZEN and for how long, raw 5y CAGR, and the CAGR measured from the pre-2020 rate.
A name whose growth exists only in the suspension-anchored window is recorded as
GROWTH ARTIFACT and drops down the queue.
"""
import json, os, sys, time
from collections import defaultdict
from datetime import date

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
_ARGV = sys.argv[1:]   # captured BEFORE the reset below - the reset was eating --all
sys.argv = [sys.argv[0]]
import bt17_microcap as M  # noqa: E402

SHORTLIST = ["COLM", "HOG", "LEVI", "LOW", "ITW", "RPM", "MTDR", "UNH"]

# --all scans every READ name in the prepped list and ranks the genuinely clean growers.
# Added 2026-08-31: the first eight were chosen by a lens that manufactured growth from
# suspension years, so the whole list deserves the corrected test.


def divs(ticker):
    for tk in (ticker, ticker.replace(".", "-")):
        for suffix in ("", "_20y", "_10y"):
            p = os.path.join(M.CACHE, f"chart_{tk}{suffix}.json")
            if os.path.exists(p):
                try:
                    d = json.load(open(p, encoding="utf-8"))
                    ev = (d["chart"]["result"][0].get("events", {}) or {}).get("dividends", {}) or {}
                    out = sorted((e["date"], e["amount"]) for e in ev.values()
                                 if isinstance(e.get("date"), (int, float))
                                 and 0 < e["date"] < 4e9 and e.get("amount"))
                    if out:
                        return out
                except Exception:
                    pass
    return []


def scan_all():
    """Rank every READ name by CLEAN dividend growth: no suspension, no frozen rate,
    and growth that survives measurement from a pre-2020 base."""
    import csv
    src = os.path.join(HERE, f"{date.today()} PREPPED LIST.csv")
    rows = [r for r in csv.DictReader(open(src, encoding="utf-8")) if r["status"] == "READ"]
    out = []
    for r in rows:
        t = r["ticker"]
        d = divs(t)
        if not d:
            continue
        by_year = defaultdict(list)
        for ts, amt in d:
            by_year[time.gmtime(ts).tm_year].append(amt)
        now = time.time()

        def ttm(off):
            return sum(a for ts, a in d
                       if now - (off + 1) * 365 * 86400 < ts <= now - off * 365 * 86400)
        d0 = ttm(0)
        if d0 <= 0:
            continue
        last_rate = round(d[-1][1], 4)
        streak = 0
        for ts, amt in reversed(d):
            if round(amt, 4) == last_rate:
                streak += 1
            else:
                break
        recent = [y for y in sorted(by_year) if y >= date.today().year - 6]
        skipped = [y for y in recent[:-1] if len(by_year[y]) < 4]
        pre = sum(by_year.get(2019, [])) or sum(by_year.get(2018, []))
        yrs = date.today().year - (2019 if by_year.get(2019) else 2018)
        cagr_pre = (d0 / pre) ** (1 / yrs) - 1 if pre else None
        if cagr_pre is None or skipped or streak >= 8:
            continue                      # suspension, freeze, or too short a record
        px_cap = r["cap_m"]
        out.append((cagr_pre, t, r["name"][:32], r["div_yield"], px_cap,
                    r["statute_yield"], r["payout_worst5"]))
    out.sort(reverse=True)
    print(f"CLEAN DIVIDEND GROWERS â€” {date.today()}")
    print("(no suspension, no frozen rate, growth measured from a PRE-2020 base)\n")
    print(f"{'tick':6s} {'growth':>7s} {'divY':>6s} {'statute':>8s} {'capM':>8s} "
          f"{'payout':>7s}  name")
    for cagr, t, name, dy, cap, sy, po in out[:30]:
        dyf = f"{float(dy):.1%}" if dy else "   -  "
        syf = f"{float(sy):.1%}" if sy else "    -  "
        pof = f"{po:>7}" if po else "      -"
        print(f"{t:6s} {cagr:+7.1%} {dyf:>6s} {syf:>8s} {cap:>8} {pof}  {name}")
    print(f"\n{len(out)} names pass the integrity test out of {len(rows)} READ names.")


def main():
    if "--all" in _ARGV:
        scan_all()
        return
    names = [a for a in _ARGV if not a.startswith("--")] or SHORTLIST
    print(f"DIVIDEND INTEGRITY â€” {date.today()}\n")
    for t in names:
        d = divs(t)
        if not d:
            print(f"{t}: no cached dividend history\n")
            continue
        by_year = defaultdict(list)
        for ts, amt in d:
            by_year[time.gmtime(ts).tm_year].append(amt)
        years = sorted(by_year)[-8:]
        print(f"== {t} ==")
        for y in years:
            pays = by_year[y]
            print(f"   {y}: {len(pays)} payments, total {sum(pays):.2f}, "
                  f"rates {sorted(set(round(a, 4) for a in pays))}")
        # frozen-rate streak on the most recent rate
        last_rate = round(d[-1][1], 4)
        streak = 0
        for ts, amt in reversed(d):
            if round(amt, 4) == last_rate:
                streak += 1
            else:
                break
        # suspension / skipped quarters inside the last 6 years
        recent_years = [y for y in sorted(by_year) if y >= date.today().year - 6]
        skipped = [y for y in recent_years[:-1] if len(by_year[y]) < 4]
        now = time.time()

        def ttm(off):
            return sum(a for ts, a in d if now - (off + 1) * 365 * 86400 < ts <= now - off * 365 * 86400)
        d0, d5 = ttm(0), ttm(5)
        cagr5 = (d0 / d5) ** 0.2 - 1 if d5 > 0 else None
        pre = sum(by_year.get(2019, [])) or sum(by_year.get(2018, []))
        yrs_since = date.today().year - (2019 if by_year.get(2019) else 2018)
        cagr_pre = (d0 / pre) ** (1 / yrs_since) - 1 if pre else None
        flags = []
        if skipped:
            flags.append(f"SUSPENSION/SKIPPED QUARTERS in {skipped}")
        if streak >= 8:
            flags.append(f"FROZEN at {last_rate} for {streak} consecutive payments")
        if cagr5 and cagr_pre is not None and cagr5 - cagr_pre > 0.04:
            flags.append("GROWTH ARTIFACT: 5y CAGR far exceeds the pre-2020-anchored rate")
        print(f"   raw 5y CAGR {cagr5:+.1%}" if cagr5 is not None else "   raw 5y CAGR n/a", end="")
        print(f" | from pre-2020 base {cagr_pre:+.1%}" if cagr_pre is not None else " | pre-2020 base n/a")
        print("   VERDICT: " + ("; ".join(flags) if flags else "clean - real, unbroken growth"))
        print()


if __name__ == "__main__":
    main()


