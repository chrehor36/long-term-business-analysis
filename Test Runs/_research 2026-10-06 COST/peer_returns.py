import json
from datetime import date
def series(f, tags, form=("10-K",), dur=True, ns="us-gaap"):
    out={}
    for tag in tags:
        try: d=f[ns][tag]
        except KeyError: continue
        for unit,vals in d["units"].items():
            for v in vals:
                if v.get("form") not in form: continue
                if dur:
                    if "start" not in v: continue
                    s=date.fromisoformat(v["start"]); e=date.fromisoformat(v["end"])
                    if not (340<=(e-s).days<=380): continue
                key=v["end"][:4] if int(v["end"][5:7])>=6 else str(int(v["end"][:4])-1)  # fiscal year label
                if key not in out: out[key]=(v["val"],tag,v["end"])
        if out: break
    return out
REV=["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"]
OI=["OperatingIncomeLoss"]
PT=["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest","IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]
NI=["NetIncomeLoss","ProfitLoss"]
TA=["Assets"]
EQ=["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]
GW=["Goodwill"]
INT=["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"]
CASH=["CashAndCashEquivalentsAtCarryingValue"]
LTD=["LongTermDebtNoncurrent","LongTermDebtAndCapitalLeaseObligations"]
OCF=["NetCashProvidedByUsedInOperatingActivities"]
CAPEX=["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"]
SBC=["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"]
DA=["DepreciationDepletionAndAmortization","DepreciationAndAmortization","DepreciationAmortizationAndAccretionNet"]
for t in ["COST","WMT","BJ","TGT","KR","AMZN","PSMT"]:
    f=json.load(open(f"edgar/{t}_facts.json"))["facts"]
    rev=series(f,REV); oi=series(f,OI); pt=series(f,PT); ni=series(f,NI)
    ta=series(f,TA,dur=False); eq=series(f,EQ,dur=False); gw=series(f,GW,dur=False); it=series(f,INT,dur=False); cash=series(f,CASH,dur=False)
    ocf=series(f,OCF); cx=series(f,CAPEX); sbc=series(f,SBC); da=series(f,DA)
    print(f"\n==== {t}  (rev tag {next(iter(rev.values()))[1] if rev else '-'}; OI tag; eq tag {next(iter(eq.values()))[1] if eq else '-'})")
    print(" FY    revenue   op.inc  OI/rev  pretax   netinc   assets   equity  goodwill  tang.eq  OI/TA  PT/tangEq  OCF    capex   SBC    D&A  (OCF-SBC-capex)")
    for y in sorted(set(rev)|set(oi)):
        if y<"2015" or y>"2026": continue
        r=rev.get(y,(None,))[0]; o=oi.get(y,(None,))[0]; p=pt.get(y,(None,))[0]; n=ni.get(y,(None,))[0]
        a=ta.get(y,(None,))[0]; e=eq.get(y,(None,))[0]; g=(gw.get(y,(0,))[0] or 0)+(it.get(y,(0,))[0] or 0)
        te=(e-g) if e is not None else None
        oc=ocf.get(y,(None,))[0]; c=cx.get(y,(None,))[0]; s=sbc.get(y,(None,))[0]; d=da.get(y,(None,))[0]
        oe=(oc-(s or 0)-c) if (oc is not None and c is not None) else None
        fm=lambda x: f"{x/1e6:9,.0f}" if x is not None else "        -"
        pc=lambda x,y: f"{100*x/y:5.1f}%" if (x is not None and y) else "    -"
        print(f" {y} {fm(r)} {fm(o)} {pc(o,r)} {fm(p)} {fm(n)} {fm(a)} {fm(e)} {fm(g)} {fm(te)} {pc(o,a)} {pc(p,te)} {fm(oc)} {fm(c)} {fm(s)} {fm(d)} {fm(oe)}")
