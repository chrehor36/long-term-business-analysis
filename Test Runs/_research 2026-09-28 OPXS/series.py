import json, sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('cache/facts.json'))
g=d['facts']['us-gaap']
def ann(tags, inst=False):
    out={}
    for t in tags:
        if t not in g: continue
        for k,u in g[t]['units'].items():
            for f in u:
                if f.get('form') not in ('10-K','10-K/A'): continue
                e=f['end']
                if not inst:
                    s=f.get('start')
                    if not s: continue
                    dd=(date.fromisoformat(e)-date.fromisoformat(s)).days
                    if dd<340 or dd>380: continue
                fy=int(e[:4]) if e[5:7]>='06' else int(e[:4])-1
                out.setdefault(fy,f['val'])
    return out
rev=ann(['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
gp=ann(['GrossProfit']); oi=ann(['OperatingIncomeLoss'])
ca=ann(['AssetsCurrent'],1); cl=ann(['LiabilitiesCurrent'],1); cash=ann(['CashAndCashEquivalentsAtCarryingValue'],1)
ppe=ann(['PropertyPlantAndEquipmentNet'],1); eq=ann(['StockholdersEquity'],1); assets=ann(['Assets'],1)
debt=ann(['LinesOfCreditCurrent','LineOfCredit','ShortTermBorrowings','NotesPayableCurrent'],1)
inv=ann(['InventoryNet'],1)
print('FY  rev  gp%  opm%  op  cap(NWCexcash+debt,+PPE)  ROC  equity')
rows=[]
for y in range(2009,2026):
    r=rev.get(y); o=oi.get(y)
    if y in ca and y in cl:
        nwc=ca[y]-cash.get(y,0)-(cl[y]-debt.get(y,0))
        cap=nwc+ppe.get(y,0)
    else: cap=None
    print(y, r and round(r/1e3), r and gp.get(y) and f"{gp[y]/r:.1%}", r and o is not None and f"{o/r:.1%}", o and round(o/1e3), cap and round(cap/1e3), cap and o is not None and f"{o/cap:.1%}", eq.get(y) and round(eq[y]/1e3), 'debt',debt.get(y), 'inv',inv.get(y) and round(inv[y]/1e3))
