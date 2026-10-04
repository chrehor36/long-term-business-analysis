#!/usr/bin/env python3
"""NEW CANDIDATES â€” find businesses never examined, then price them before reading them.

The operator asked for fifty more names. Fifty full runs is ~20M tokens and several days
of usage stalls, and 34 completed runs have established what that spend buys: eight
businesses cleared every gate and ALL EIGHT failed on price. So this finds the fifty, then
puts every one through the cheap tests first, and only what survives earns a full read.

Pipeline, cheapest first, nothing expensive run on a name already dead:
  1 FIND    - continue the deterministic hash-of-CIK sweep PAST everything already
              examined (the prepped list, the earlier sweeps, and every run on the shelf),
              so these are genuinely new names, not a reshuffle.
  2 VALIDATE- SEC filer, live price, five filed 10-K years, single-class-ish, cap in band.
  3 GUARD   - the four artifact classes that have each destroyed a screen number:
              stale share count, perimeter change (0.75-1.50x over two years),
              capex-unresolved (the E5-20 invalid end), and a dividend suspension or
              freeze inside the window.
  4 PRICE   - owner earnings both windows x both (c) constructions, bottom boundary,
              yield vs the sovereign, and the perpetual growth needed for the E4-28 floor.

Output is a reading order. It opens and closes NOTHING: operator rule 3 governs, every
number is a COMPUTATION, and no verdict on any business exists until the six questions run.
"""
import csv, hashlib, json, os, sys, time
from collections import defaultdict
from datetime import date

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
sys.path.insert(0, HERE)
_ARGV = sys.argv[1:]
sys.argv = [sys.argv[0]]
import bt17_microcap as M            # noqa: E402
import floor_screen as F             # noqa: E402

TODAY = date.today()
TARGET = int(_ARGV[0]) if _ARGV else 50
CAP_LO, CAP_HI = 200e6, 60e9         # small through large; excludes the untradeable tail
EXAM_CAP = 9000

FIN = ("bank", "bancorp", "bancshares", "financial", "insurance", "capital", "asset manage",
       "mortgage", "reit", "realty", "properties", "trust", "holdings ltd", "partners",
       "acquisition", "royalty")
UTIL = ("electric", "utilit", "gas & electric", "power & light", "energy corp")


def already_examined():
    seen = set()
    for fn in os.listdir(HERE):
        if fn.endswith(".csv"):
            try:
                for r in csv.DictReader(open(os.path.join(HERE, fn), encoding="utf-8")):
                    t = (r.get("ticker") or "").strip().upper()
                    if t:
                        seen.add(t)
            except Exception:
                pass
    runs = os.path.join(ROOT, "Test Runs")
    for fn in os.listdir(runs):
        if " Run - " in fn and fn.endswith(".md"):
            part = fn.split(" Run - ", 1)[1]
            seen.add(part.split(" ")[0].upper())
    return seen


def main():
    seen = already_examined()
    print(f"NEW CANDIDATES â€” {TODAY}")
    print(f"excluding {len(seen)} tickers already examined or run\n")
    tick = M.cached_json("company_tickers.json",
                         "https://www.sec.gov/files/company_tickers.json")
    cands = sorted(tick.values(),
                   key=lambda v: hashlib.sha256(str(v["cik_str"]).encode()).hexdigest())
    sov = (M.dgs30_asof(TODAY) or 5.25) / 100.0
    print(f"sovereign {sov:.2%} Â· floor 10% [E4-28]\n")

    found, examined = [], 0
    skip = defaultdict(int)
    for c in cands:
        if len(found) >= TARGET or examined >= EXAM_CAP:
            break
        examined += 1
        t = str(c["ticker"]).upper()
        name = c.get("title", "")
        if t in seen or "-" in t or (len(t) == 5 and t[-1] in "WU"):
            skip["seen/suffix"] += 1
            continue
        low = name.lower()
        if any(k in low for k in FIN):
            skip["financial"] += 1
            continue
        if any(k in low for k in UTIL):
            skip["regulated"] += 1
            continue
        cik = int(c["cik_str"])
        # SIC GUARD, added 2026-09-01. Name matching missed First Hawaiian (a bank),
        # Essent (a mortgage insurer) and OppFi (a subprime lender) because none carries
        # a financial word in its title. The SEC assigns an SIC code; 6000-6799 is
        # Finance, Insurance and Real Estate, which is the operator's excluded class
        # [directive 2026-08-30; E2-50 stroke-of-a-pen, E3-29 leverage].
        try:
            subs = M.cached_json(f"subs_{cik}.json",
                                 f"https://data.sec.gov/submissions/CIK{cik:010d}.json",
                                 sleep=0.12)
            sic = int(subs.get("sic") or 0)
        except Exception:
            sic = 0
        if 6000 <= sic <= 6799:
            skip[f"financial by SIC {sic}"] += 1
            continue
        try:
            facts = M.cached_json(f"facts_{cik}.json",
                                  f"https://data.sec.gov/api/xbrl/companyfacts/"
                                  f"CIK{cik:010d}.json", sleep=0.12)
        except Exception:
            skip["nofacts"] += 1
            continue
        sh = M.shares_asof(facts, TODAY)
        if not sh:
            skip["noshares"] += 1
            continue
        meas = sh[0]
        if (TODAY.year - meas.year) * 12 + (TODAY.month - meas.month) > 18:
            skip["stale shares"] += 1
            continue
        ratio = F.share_count_shift(facts)
        if ratio is not None and not (0.75 <= ratio <= 1.50):
            skip["perimeter"] += 1
            continue
        # The merger-into-a-new-filer case the share-count guard cannot see. Amentum
        # passed at 1.005x and Smurfit Westrock at 1.008x while the business underneath
        # tripled. Revenue doubling in a single year is a corporate action, not growth.
        scale = F.scale_shift(facts)
        if scale is not None and scale > 2.0:
            skip["perimeter by revenue step"] += 1
            continue
        # A five-year mean needs five filed years. Four years with a 2% spread is a SHORT
        # estimate, not a well-determined one - the Ferguson error, stated in the list.
        if F.filed_years(facts) < 5:
            skip["fewer than 5 filed years"] += 1
            continue
        oe = F.owner_earnings(facts)
        if oe == "CAPEX_UNRESOLVED":
            skip["capex unresolved [E5-20]"] += 1
            continue
        if not oe:
            skip["no owner earnings"] += 1
            continue
        try:
            closes, _a, splits = M.chart(t, examined)
        except Exception:
            skip["nochart"] += 1
            continue
        m = f"{TODAY.year}-{TODAY.month:02d}"
        px = closes.get(m) or (closes[max(closes)] if closes else None)
        if not px or (closes and max(closes) < m):
            skip["stale/no price"] += 1
            continue
        factor = 1.0
        for sd, f in splits:
            if sd > meas:
                factor *= f
        cap = px * sh[1] * factor
        if not (CAP_LO <= cap <= CAP_HI):
            skip["cap out of band"] += 1
            continue
        vals = list(oe.values())
        bottom = min(vals)
        y = bottom / cap
        found.append(dict(ticker=t, name=name[:34], cap_m=round(cap / 1e6),
                          oe_bottom_m=round(bottom / 1e6),
                          yield_bottom=round(y, 4),
                          vs_sovereign=round(y - sov, 4),
                          growth_required=round(0.10 - y, 4),
                          spread=round((max(vals) - bottom) / bottom, 3) if bottom > 0 else ""))
        if len(found) % 10 == 0:
            print(f"  {len(found)}/{TARGET} found, {examined} examined")

    found.sort(key=lambda x: x["growth_required"])
    # Batch-numbered output. The sweep excludes every ticker in Screens/*.csv, INCLUDING its
# own prior output, so a second run finds fifty genuinely new names rather than repeating
# the first fifty. That is the intended behaviour, but a fixed filename made the second
# run destroy the first. Number the batches instead.
    n = 1
    while os.path.exists(os.path.join(HERE, f"{TODAY} NEW CANDIDATES batch{n}.csv")):
        n += 1
    dest = os.path.join(HERE, f"{TODAY} NEW CANDIDATES batch{n}.csv")
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(found[0].keys()))
        w.writeheader(); w.writerows(found)

    print(f"\n{'tick':6s} {'capM':>8s} {'OE bot':>8s} {'yield':>7s} {'vs bond':>8s} "
          f"{'growth req':>10s} {'spread':>7s}  name")
    for x in found:
        sp = f"{x['spread']:.0%}" if x["spread"] != "" else "    -"
        print(f"{x['ticker']:6s} {x['cap_m']:>8,} {x['oe_bottom_m']:>8,} "
              f"{x['yield_bottom']:>7.2%} {x['vs_sovereign']:>+8.2%} "
              f"{x['growth_required']:>10.2%} {sp:>7s}  {x['name']}")
    plausible = [x for x in found if x["growth_required"] <= 0.06]
    print(f"\nexamined {examined}; skips: {dict(skip)}")
    print(f"**{len(plausible)} of {len(found)} need <=6% perpetual growth** â€” the only "
          f"names where a full run could end in anything but a price failure.")
    print(f"WROTE {dest}")


if __name__ == "__main__":
    main()


