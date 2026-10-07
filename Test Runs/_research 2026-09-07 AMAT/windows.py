"""AMAT windows, yields, level shift, value. Arithmetic only."""
import json, os, collections
from datetime import date
OUT = os.path.dirname(os.path.abspath(__file__))
US = json.load(open(os.path.join(OUT, "companyfacts_AMAT.json"), encoding="utf-8"))["facts"]["us-gaap"]

def series(tag):
    if tag not in US: return {}
    by = collections.defaultdict(list)
    for u, rows in US[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A") or r.get("fp") != "FY": continue
            if "start" in r:
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (330 <= (e - s).days <= 400): continue
            by[r["end"]].append((r["filed"], r["val"]))
    return {e: sorted(v)[0][1] for e, v in by.items()}

ocf = series("NetCashProvidedByUsedInOperatingActivities")
sbc = series("ShareBasedCompensation")
da = {}
for t in ("DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet", "DepreciationAndAmortization"):
    for e, v in series(t).items():
        if e not in da or abs(v) > abs(da[e]): da[e] = v
cap = series("PaymentsToAcquirePropertyPlantAndEquipment")

M = 1e6
ends = sorted(e for e in ocf if e >= "2007-01-01")
oe_c = {e: (ocf[e] - sbc.get(e, 0) - cap.get(e, 0)) / M for e in ends}
oe_d = {e: (ocf[e] - sbc.get(e, 0) - da.get(e, 0)) / M for e in ends}

SH = 793597443
PX = 454.71
CAP_M = SH * PX / 1e6
SOV = 5.24
print(f"shares {SH:,}  price ${PX}  market cap ${CAP_M:,.0f}M   sovereign {SOV}%")
print(f"screen row: cap 368,001  oe_bottom 5,512  oe_top 7,419  spread 0.346  growth_req 0.085  level_shift 2.0")

labels = [("3-yr FY2023-25", 3), ("5-yr FY2021-25", 5), ("8-yr FY2018-25", 8),
          ("10-yr FY2016-25", 10), ("15-yr FY2011-25", 15), ("19-yr FY2007-25", 19)]
print(f"\n{'window':18s} {'capex end':>10s} {'yield%':>8s} | {'D&A end':>10s} {'yield%':>8s}   g-to-floor%  g-to-sov%")
allv = []
for lab, n in labels:
    w = ends[-n:]
    a = sum(oe_c[e] for e in w) / n
    d = sum(oe_d[e] for e in w) / n
    ya, yd = a / CAP_M * 100, d / CAP_M * 100
    allv += [a, d]
    print(f"{lab:18s} {a:10.1f} {ya:8.3f} | {d:10.1f} {yd:8.3f}      {10-ya:6.2f}     {SOV-ya:6.2f}")
for n in (5, 10):
    v = sorted(oe_c[e] for e in ends[-n:])[:-2]
    a = sum(v) / len(v); allv.append(a)
    print(f"{n}-yr leave-two-out  {a:10.1f} {a/CAP_M*100:8.3f}")
best = max(oe_c.values()); allv.append(best)
print(f"BEST YEAR EVER (capex end) {best:10.1f} {best/CAP_M*100:8.3f}    g-to-floor {10-best/CAP_M*100:.2f}")
bestd = max(oe_d.values())
print(f"BEST YEAR EVER (D&A end)   {bestd:10.1f} {bestd/CAP_M*100:8.3f}    g-to-floor {10-bestd/CAP_M*100:.2f}")

print("\n=== TRUE WIDTH [E4-25] ===")
print(f"  widest {max(allv+[bestd]):,.1f}   narrowest {min(allv):,.1f}   ratio {max(allv+[bestd])/min(allv):.2f}x = {(max(allv+[bestd])/min(allv)-1)*100:.1f}%")
print(f"  screen claimed 5,512 to 7,419 = 34.6%")

print("\n=== [E4-41] LEVEL SHIFT, by hand ===")
pre = [oe_c[e] for e in ends if "2014-10" <= e <= "2018-11"]
post = [oe_c[e] for e in ends if e >= "2021-10"]
print(f"  pre-wave 5-yr FY2014-18: {sum(pre)/len(pre):,.1f}   wave 5-yr FY2021-25: {sum(post)/len(post):,.1f}")
print(f"  step = {(sum(post)/len(post))/(sum(pre)/len(pre)):.2f}x  (screen level_shift 2.0)")
pre2 = [oe_c[e] for e in ends if "2015-10" <= e <= "2019-11"]
print(f"  alt pre-wave FY2015-19: {sum(pre2)/len(pre2):,.1f}  step {(sum(post)/len(post))/(sum(pre2)/len(pre2)):.2f}x")

print("\n=== VALUE per share, zero growth ===")
for lab, n in labels:
    w = ends[-n:]
    a = sum(oe_c[e] for e in w) / n
    print(f"  {lab:18s} OE {a:8.1f}M -> at {SOV}%: ${a*1e6/(SOV/100)/SH:8.2f}/sh   at 10%: ${a*1e6/0.10/SH:8.2f}/sh")
print(f"  best year          OE {best:8.1f}M -> at {SOV}%: ${best*1e6/(SOV/100)/SH:8.2f}/sh   at 10%: ${best*1e6/0.10/SH:8.2f}/sh")
print(f"  price ${PX}")

print("\n=== OE by year, both ends ===")
for e in ends:
    print(f"  {e}  capex-end {oe_c[e]:8.1f}   D&A-end {oe_d[e]:8.1f}")

print("\n=== OE CAGR, every window [E4-38] ===")
for n in (8, 10, 15, 19):
    a, b = oe_c[ends[-n]], oe_c[ends[-1]]
    if a > 0:
        print(f"  {n-1}-yr FY{ends[-n][:4]}->FY{ends[-1][:4]}: {((b/a)**(1/(n-1))-1)*100:6.2f}%/yr   ({a:,.0f} -> {b:,.0f})")
