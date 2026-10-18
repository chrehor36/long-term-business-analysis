"""Annual revenue, operating income, OCF, assets, equity per ticker; latest-filed value for each FY (restated where restated). Usage: peers.py TICKER [first|last]"""
import json, sys
from datetime import date
t = sys.argv[1]; mode = sys.argv[2] if len(sys.argv) > 2 else "last"
g = json.load(open(f"cache/facts_{t}.json"))["facts"]["us-gaap"]
def series(tags, instant=False):
    out = {}
    for tag in tags:
        if tag not in g: continue
        for unit, vals in g[tag]["units"].items():
            if unit != "USD": continue
            for v in vals:
                if v.get("form") not in ("10-K", "10-K/A", "10-KT"): continue
                if not instant:
                    if "start" not in v: continue
                    dd = (date.fromisoformat(v["end"]) - date.fromisoformat(v["start"])).days
                    if not 330 < dd < 400: continue
                y = v["end"][:7]
                better = (y not in out) or ((v["filed"] > out[y][1]) if mode == "last" else (v["filed"] < out[y][1]))
                if better and (y not in out or out[y][2] == tag or True):
                    if y in out and out[y][2] != tag and out[y][3] < tags.index(tag): continue
                    out[y] = (v["val"], v["filed"], tag, tags.index(tag))
    return out
rev = series(["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "OilAndGasRevenue", "OilAndGasSalesRevenue", "RevenueFromContractWithCustomerIncludingAssessedTax"])
oi = series(["OperatingIncomeLoss"])
ocf = series(["NetCashProvidedByUsedInOperatingActivities"])
ast = series(["Assets"], instant=True)
eq = series(["StockholdersEquity"], instant=True)
dda = series(["DepreciationDepletionAndAmortization", "DepreciationAndAmortization", "DepreciationDepletionAndAmortizationIncludingAccretion"])
print(f"{t} ({mode}-filed) USD millions")
print("FY       revenue  op.inc  margin    OCF   assets  equity   DD&A")
for y in sorted(set(rev) | set(oi)):
    if y < "2013": continue
    r = rev.get(y, (float('nan'),))[0]/1e6; o = oi.get(y, (float('nan'),))[0]/1e6
    print(f"{y}  {r:8.1f} {o:7.1f} {o/r*100 if r==r and r else float('nan'):6.1f}% {ocf.get(y,(float('nan'),))[0]/1e6:7.1f} {ast.get(y,(float('nan'),))[0]/1e6:8.1f} {eq.get(y,(float('nan'),))[0]/1e6:7.1f} {dda.get(y,(float('nan'),))[0]/1e6:6.1f}")
