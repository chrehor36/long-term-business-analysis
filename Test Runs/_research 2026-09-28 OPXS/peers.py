import json, sys, os, time
from datetime import date
sys.path.insert(0,'../../tools')
sys.stdout.reconfigure(encoding='utf-8')
import sources as S
from fetch import get
PEERS=['OPXS','LPTH','POCI','KOPN','ESP','CVU','AIRI','FEIM','ULBI','ISSC','SYPR','SVT']
def ann(g,tags,inst=False):
    tags=list(tags)
    out={}
    for t in tags:
        if t not in g: continue
        for k,u in g[t]['units'].items():
            if k!='USD': continue
            for f in u:
                if f.get('form') not in ('10-K','10-K/A'): continue
                e=f['end']
                if not inst:
                    s=f.get('start')
                    if not s: continue
                    dd=(date.fromisoformat(e)-date.fromisoformat(s)).days
                    if dd<340 or dd>380: continue
                fy=int(e[:4]) if e[5:7]>='06' else int(e[:4])-1
                if inst or 'rev' not in tags[0].lower(): out.setdefault(fy,f['val'])
                else: out[fy]=max(out.get(fy,f['val']),f['val'])
    return out
res={}
for t in PEERS:
    try:
        cik,name=S.cik_for(t)
    except Exception as e:
        print(t,'no cik',e); continue
    if not cik: print(t,'no cik'); continue
    p=f'cache/peers/{t}_facts.json'
    if not os.path.exists(p):
        open(p,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')); time.sleep(0.3)
    g=json.load(open(p))['facts'].get('us-gaap',{})
    rev=ann(g,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    oi=ann(g,['OperatingIncomeLoss']); gp=ann(g,['GrossProfit'])
    ca=ann(g,['AssetsCurrent'],1); cl=ann(g,['LiabilitiesCurrent'],1)
    cash=ann(g,['CashAndCashEquivalentsAtCarryingValue','Cash','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],1)
    sti=ann(g,['ShortTermInvestments','MarketableSecuritiesCurrent','AvailableForSaleSecuritiesDebtSecuritiesCurrent','HeldToMaturitySecuritiesCurrent'],1)
    ppe=ann(g,['PropertyPlantAndEquipmentNet'],1)
    debt=ann(g,['LinesOfCreditCurrent','LineOfCredit','ShortTermBorrowings','LongTermDebtCurrent','NotesPayableCurrent','DebtCurrent'],1)
    yrs=[y for y in range(2021,2026) if y in rev and y in oi and y in ca and y in cl]
    R=sum(rev[y] for y in yrs); O=sum(oi[y] for y in yrs)
    C=sum(ca[y]-cash.get(y,0)-sti.get(y,0)-(cl[y]-debt.get(y,0))+ppe.get(y,0) for y in yrs)
    G=sum(gp.get(y,0) for y in yrs)
    per={y:(round(rev[y]/1e6,1), f"{oi[y]/rev[y]:.1%}") for y in yrs}
    res[t]=dict(name=name,yrs=yrs,rev=R,op=O,cap=C,opm=O/R if R else None,roc=O/C if C else None,gm=G/R if R else None,per=per)
    print(f"{t:5} {name[:38]:38} yrs {yrs[0] if yrs else '-'}-{yrs[-1] if yrs else '-'} n={len(yrs)} rev5 {R/1e6:7.1f}M opm {O/R if R else 0:6.1%} gm {G/R if R else 0:6.1%} ROC {O/C if C else 0:7.1%}  {per}")
json.dump(res,open('peers_out.json','w'),indent=1,default=str)
