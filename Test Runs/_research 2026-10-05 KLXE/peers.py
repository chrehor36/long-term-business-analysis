import json,sys
from datetime import date
def series(g,tags,annual=True):
    out={}
    for t in tags:
        if t not in g: continue
        for unit,u in g[t]['units'].items():
            for x in u:
                if not x['form'].startswith('10-K'): continue
                if annual:
                    if 'start' not in x: continue
                    if (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<300: continue
                y=x['end'][:4] if x['end'][5:7]!='01' else str(int(x['end'][:4])-1)  # KLXE Jan FY -> prior year
                # prefer latest filing (restated) -> keep last by filed date
                k=y
                if k not in out or x['filed']>out[k][1]: out[k]=(x['val'],x['filed'],x['accn'],x['end'])
        if out: pass
    return out
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet','SalesRevenueServicesNet']
OPI=['OperatingIncomeLoss']
OCF=['NetCashProvidedByUsedInOperatingActivities']
CAP=['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets']
NI=['NetIncomeLoss']
SBC=['ShareBasedCompensation','AllocatedShareBasedCompensationExpense']
PROC=['ProceedsFromSaleOfPropertyPlantAndEquipment','ProceedsFromSaleOfProductiveAssets']
ASSETS=['Assets']; EQ=['StockholdersEquity']
def merged(g,tags):
    res={}
    for t in tags:
        s=series(g,[t])
        for k,v in s.items():
            res.setdefault(k,v)
    return res
for f in sys.argv[1:]:
    d=json.load(open(f)); g=d['facts']['us-gaap']
    R=merged(g,REV);O=merged(g,OPI);C=merged(g,OCF);K=merged(g,CAP);N=merged(g,NI);S=merged(g,SBC);P=merged(g,PROC)
    print('==',d['entityName'])
    print(' yr     rev    opinc  opm%   OCF   capex  procAS  SBC   OC=OCF-SBC-capex+proc   NI')
    tot={'r':0,'o':0,'oc':0,'n':0}
    for y in [str(i) for i in range(2017,2026)]:
        if y not in R: continue
        r=R[y][0]/1e6; o=O.get(y,(0,))[0]/1e6; c=C.get(y,(0,))[0]/1e6; k=K.get(y,(0,))[0]/1e6; n=N.get(y,(0,))[0]/1e6; s=S.get(y,(0,))[0]/1e6; p=P.get(y,(0,))[0]/1e6
        oc=c-s-k+p
        if int(y)>=2018: tot['r']+=r;tot['o']+=o;tot['oc']+=oc;tot['n']+=n
        print(f" {y} {r:8.1f} {o:8.1f} {100*o/r:6.1f} {c:7.1f} {k:7.1f} {p:6.1f} {s:5.1f} {oc:8.1f} {n:8.1f}  {R[y][3]} {R[y][2]}")
    print(f" 2018-2025 sums: rev {tot['r']:.1f} opinc {tot['o']:.1f} op margin {100*tot['o']/tot['r']:.1f}% owner cash {tot['oc']:.1f} NI {tot['n']:.1f}")
