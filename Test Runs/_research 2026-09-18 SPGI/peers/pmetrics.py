import sys,os,json,datetime as dt
sys.path.insert(0,r'C:\Users\chreh\OneDrive\Documents\BRK\Screens')
sys.path.insert(0,r'C:\Users\chreh\OneDrive\Documents\BRK\tools')
import floor_screen as fs
HERE=os.path.dirname(os.path.abspath(__file__))
SPGI=r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-18 SPGI\companyfacts.json'
TAGS={
 "revenue":["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","RevenueFromContractWithCustomerIncludingAssessedTax"],
 "opinc":["OperatingIncomeLoss"],
 "ocf":["NetCashProvidedByUsedInOperatingActivities"],
 "capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets","PaymentsForCapitalImprovements"],
 "sbc":["ShareBasedCompensation"],
 "da":["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet"],
}
INST={
 "assets":["Assets"],"goodwill":["Goodwill"],
 "intang":["FiniteLivedIntangibleAssetsNet","IntangibleAssetsNetExcludingGoodwill"],
 "cash":["CashAndCashEquivalentsAtCarryingValue"],
 "curliab":["LiabilitiesCurrent"],
 "stdebt":["ShortTermBorrowings","OtherShortTermBorrowings","LongTermDebtCurrent","CommercialPaper"],
 "ltdebt":["LongTermDebtNoncurrent","LongTermDebt"],
 "equity":["StockholdersEquity"],
}
def series(facts,tags,instant=False):
    fn = fs.annual_instant if instant else fs.annual
    out={}
    for t in tags:
        try: d=fn(facts,[t])
        except TypeError: d=fn(facts,t)
        for k,v in (d or {}).items():
            out.setdefault(k,v)
    return out
rows={}
names={"SPGI":SPGI}
for f in sorted(os.listdir(HERE)):
    if f.endswith("_companyfacts.json"): names[f.split("_")[0]]=os.path.join(HERE,f)
for tk,path in names.items():
    facts=json.load(open(path,encoding="utf-8"))
    r={}
    for k,tags in TAGS.items(): r[k]=series(facts,tags)
    for k,tags in INST.items(): r[k]=series(facts,tags,instant=True)
    rows[tk]=r
def g(r,k,y):
    for d,v in r.get(k,{}).items():
        if d.year==y: return v/1e6
    return None
print(f"{'tk':6s} {'yr':5s} {'rev':>9s} {'opinc':>9s} {'opmar%':>7s} {'assets':>9s} {'gw':>9s} {'intang':>9s} {'cash':>8s} {'curliab':>8s} {'NTOA':>9s} {'pretaxROA%':>10s} {'capex':>7s} {'D&A':>8s} {'ocf':>9s} {'sbc':>7s}")
for tk in sorted(rows):
    for y in (2023,2024,2025):
        r=rows[tk]
        rev,op=g(r,"revenue",y),g(r,"opinc",y)
        a,gw,it,ca,cl=g(r,"assets",y),g(r,"goodwill",y),g(r,"intang",y),g(r,"cash",y),g(r,"curliab",y)
        ntoa=None
        if None not in (a,gw,ca,cl): ntoa=a-gw-(it or 0)-ca-cl
        roa=(op/ntoa*100) if (op and ntoa and ntoa>0) else None
        f=lambda x,d=1: ("%.*f"%(d,x)) if x is not None else "-"
        print(f"{tk:6s} {y:<5d} {f(rev,0):>9s} {f(op,0):>9s} {f(op/rev*100 if rev and op else None):>7s} {f(a,0):>9s} {f(gw,0):>9s} {f(it,0):>9s} {f(ca,0):>8s} {f(cl,0):>8s} {f(ntoa,0):>9s} {f(roa):>10s} {f(g(r,'capex',y),0):>7s} {f(g(r,'da',y),0):>8s} {f(g(r,'ocf',y),0):>9s} {f(g(r,'sbc',y),0):>7s}")
