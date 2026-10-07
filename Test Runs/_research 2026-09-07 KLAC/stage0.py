"""KLAC Stage 0: margins, windows, yields, split guard. Arithmetic only."""
import json, os, collections
from datetime import date

OUT = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(os.path.join(OUT, "companyfacts_KLAC.json"), encoding="utf-8"))["facts"]
US = F["us-gaap"]

def series(tag, ns=US):
    if tag not in ns: return {}
    by_end = collections.defaultdict(list)
    for unit, rows in ns[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K", "10-K/A") or r.get("fp") != "FY": continue
            if "start" in r:
                s = date.fromisoformat(r["start"]); e = date.fromisoformat(r["end"])
                if not (330 <= (e - s).days <= 400): continue
            by_end[r["end"]].append((r["filed"], r["val"]))
    return {e: sorted(v)[0][1] for e, v in by_end.items()}

rev = {}
for t in ("SalesRevenueNet", "SalesRevenueGoodsNet", "Revenues",
          "RevenueFromContractWithCustomerExcludingAssessedTax"):
    for e, v in series(t).items():
        rev.setdefault(e, v)
cogs  = series("CostOfRevenue")
rd    = series("ResearchAndDevelopmentExpense")
sga   = series("SellingGeneralAndAdministrativeExpense")
ocf   = series("NetCashProvidedByUsedInOperatingActivities")
sbc   = series("ShareBasedCompensation")
da    = series("DepreciationDepletionAndAmortization")
amort = series("AmortizationOfIntangibleAssets")
cap   = series("PaymentsToAcquirePropertyPlantAndEquipment")
ni    = series("NetIncomeLoss")
assets= series("Assets"); gw = series("Goodwill")
intan = series("IntangibleAssetsNetExcludingGoodwill")
cl    = series("LiabilitiesCurrent"); cd = series("LongTermDebtCurrent")
eq    = series("StockholdersEquity")

M = 1e6
ends = sorted(e for e in ocf if e >= "2009-06-01")
print("FY      rev     GM%    opinc   opm%   R&D%    OCF    SBC   D&A  amort  tangD&A  capex  cap/tD&A   OE(capex)  OE(D&A)   NI   ROE%   opinc/NTOA%")
rows = []
for e in ends:
    R = rev.get(e); C = cogs.get(e); D = rd.get(e); S = sga.get(e)
    o = ocf[e]; b = sbc.get(e, 0); dd = da.get(e, 0); am = amort.get(e, 0); cx = cap.get(e, 0)
    oi = (R - C - D - S) if None not in (R, C, D, S) else None
    gm = (R - C) / R * 100 if R and C else None
    tang = dd - am
    oe_c = o - b - cx
    oe_d = o - b - dd
    ntoa = None
    if e in assets:
        nibcl = cl.get(e, 0) - cd.get(e, 0)
        ntoa = assets[e] - gw.get(e, 0) - intan.get(e, 0) - nibcl
    roe = ni.get(e, 0) / eq[e] * 100 if e in eq and eq[e] else None
    rows.append((e, oe_c, oe_d))
    def f(x, n=1): return f"{x/M:8.1f}" if x is not None else "     n/a"
    def p(x, n=1): return f"{x:6.1f}" if x is not None else "   n/a"
    print(f"{e[:7]} {f(R)} {p(gm)} {f(oi)} {p(oi/R*100 if oi and R else None)} "
          f"{p(D/R*100 if D and R else None)} {f(o)} {f(b)} {f(dd)} {f(am)} {f(tang)} {f(cx)} "
          f"{p(cx/tang if tang else None,2)}   {f(oe_c)} {f(oe_d)} {f(ni.get(e))} {p(roe)} "
          f"{p(oi/ntoa*100 if oi and ntoa else None)}")

print("\n=== WINDOWS, capex end (mean $M) and the yield at cap ===")
CAP_M = 1306.546783 * 185.60          # cover count x price, $M
print(f"market cap = 1,306,546,783 sh x $185.60 = ${CAP_M:,.0f}M")
SOV = 5.24
def mean(n, idx=1):
    v = [r[idx] for r in rows[-n:]]; return sum(v)/len(v)/M
labels = [("3-yr FY2024-26", 3), ("5-yr FY2022-26", 5), ("8-yr FY2019-26", 8),
          ("10-yr FY2017-26", 10), ("15-yr FY2012-26", 15), ("18-yr FY2009-26", 18)]
print(f"{'window':18s} {'capex end':>10s} {'yield%':>8s} | {'D&A end':>10s} {'yield%':>8s}  growth-to-floor%")
for lab, n in labels:
    a = mean(n, 1); d = mean(n, 2)
    ya = a/CAP_M*100; yd = d/CAP_M*100
    print(f"{lab:18s} {a:10.1f} {ya:8.3f} | {d:10.1f} {yd:8.3f}      {10-ya:6.2f}")
# leave-two-out
for n in (5, 10):
    v = sorted(r[1] for r in rows[-n:])[:-2]
    a = sum(v)/len(v)/M
    print(f"{n}-yr leave-two-out  {a:10.1f} {a/CAP_M*100:8.3f}")
best = max(r[1] for r in rows)/M
print(f"BEST YEAR EVER (capex end) {best:10.1f} {best/CAP_M*100:8.3f}")

print("\n=== THE SPREAD, REBUILT [E4-25] ===")
allc = [mean(n,1) for _, n in labels] + [mean(n,2) for _, n in labels]
print(f"  narrowest construction {max(allc):,.1f}  widest-conservative {min(allc):,.1f}")
print(f"  TRUE WIDTH = {max(allc)/min(allc):.2f}x  =  {(max(allc)/min(allc)-1)*100:.1f}%")
print(f"  screen row claimed:  oe_bottom 3,092  oe_top 3,252  spread 5.2%")

print("\n=== [E4-41] LEVEL SHIFT, by hand ===")
pre = [r[1] for r in rows if "2015-06" <= r[0] <= "2019-06"]
post = [r[1] for r in rows if r[0] >= "2022-06"]
print(f"  pre-wave 5-yr mean FY2015-19: {sum(pre)/len(pre)/M:,.1f}")
print(f"  wave     5-yr mean FY2022-26: {sum(post)/len(post)/M:,.1f}")
print(f"  step = {(sum(post)/len(post))/(sum(pre)/len(pre)):.2f}x   (screen level_shift 1.73)")

print("\n=== VALUE, zero growth at the sovereign and at the [E4-28] floor ===")
SH = 1306.546783
for lab, oe in (("18-yr", mean(18,1)), ("10-yr", mean(10,1)), ("5-yr LTO", sum(sorted(r[1] for r in rows[-5:])[:-2])/3/M),
                ("5-yr", mean(5,1)), ("3-yr", mean(3,1)), ("best yr", best)):
    print(f"  {lab:9s} OE {oe:8.1f}M -> at 5.24%: ${oe/0.0524/SH:7.2f}/sh   at 10%: ${oe/0.10/SH:7.2f}/sh")
print(f"  price $185.60")
