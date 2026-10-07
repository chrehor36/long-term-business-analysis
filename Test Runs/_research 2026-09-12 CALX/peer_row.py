"""Peer row arithmetic from competitor_xbrl.json. Same metric, same window. Transcription only."""
import json
d = json.load(open("competitor_xbrl.json"))
def pick(f, tags):
    for t in tags:
        if t in f and f[t]: return f[t]
    return {}
def yr(rows, y):
    for k, v in rows.items():
        if k.startswith(str(y)) or (k[:4] == str(y+1) and k[5:7] in ("01",)): return v["val"]
    return None
for t, e in d.items():
    f = e["facts"]
    rev = pick(f, ["us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax","us-gaap:Revenues","us-gaap:SalesRevenueNet","ifrs-full:Revenue"])
    gp = pick(f, ["us-gaap:GrossProfit","ifrs-full:GrossProfit"])
    cogs = pick(f, ["us-gaap:CostOfRevenue","us-gaap:CostOfGoodsAndServicesSold"])
    op = pick(f, ["us-gaap:OperatingIncomeLoss","ifrs-full:ProfitLossFromOperatingActivities"])
    rd = pick(f, ["us-gaap:ResearchAndDevelopmentExpense"])
    sbc = pick(f, ["us-gaap:ShareBasedCompensation"])
    ocf = pick(f, ["us-gaap:NetCashProvidedByUsedInOperatingActivities"])
    eq = pick(f, ["us-gaap:StockholdersEquity"])
    print(f"\n{t} {e['name']} cik {e['cik']}")
    print(" yr    rev     GM%    opm%    R&D%   SBC%rev  SBC/OCF")
    for y in range(2019, 2026):
        r = yr(rev, y); g = yr(gp, y); c = yr(cogs, y); o = yr(op, y); rdv = yr(rd, y); s = yr(sbc, y); oc = yr(ocf, y)
        if r is None: continue
        if g is None and c is not None: g = r - c
        gm = f"{100*g/r:6.1f}" if g is not None else "   n/a"
        om = f"{100*o/r:6.1f}" if o is not None else "   n/a"
        rdp = f"{100*rdv/r:6.1f}" if rdv is not None else "   n/a"
        sp = f"{100*s/r:6.1f}" if s is not None else "   n/a"
        so = f"{100*s/oc:6.1f}" if (s is not None and oc) else "   n/a"
        print(f" {y}  {r/1e6:8.0f}  {gm}  {om}  {rdp}  {sp}  {so}")
