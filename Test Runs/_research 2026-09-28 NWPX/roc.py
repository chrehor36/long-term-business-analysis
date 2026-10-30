import json
from datetime import date
F=json.load(open('cache/facts.json'))['facts']['us-gaap']
print([k for k in F if 'Receivable' in k and 'Current' in k][:20])
def inst(tag):
    if tag not in F: return {}
    out={}
    for u,rows in F[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A'): continue
            if r['end'][5:7]!='12': continue
            out.setdefault(r['end'],{})[r['filed']]=r['val']
    return {e[:4]:v[max(v)]/1e6 for e,v in out.items()}
rec=inst('AccountsReceivableNetCurrent') or {}
for t in ['ReceivablesNetCurrent','AccountsAndOtherReceivablesNetCurrent','AccountsNotesAndLoansReceivableNetCurrent']:
    for k,v in inst(t).items(): rec.setdefault(k,v)
ca=inst('ContractWithCustomerAssetNetCurrent'); inv=inst('InventoryNet'); ap=inst('AccountsPayableCurrent'); cl=inst('ContractWithCustomerLiabilityCurrent'); ppe=inst('PropertyPlantAndEquipmentNet')
eq=inst('StockholdersEquity'); gw=inst('Goodwill'); ia=inst('IntangibleAssetsNetExcludingGoodwill') or inst('FiniteLivedIntangibleAssetsNet')
S=json.load(open('series.json'))
oi={k[:4]:v/1e6 for k,v in S['OperatingIncomeLoss'].items()}; am={k[:4]:v/1e6 for k,v in S['AmortizationOfIntangibleAssets'].items()}
pt={k[:4]:v/1e6 for k,v in S.get('IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',{}).items()}
for y in [str(x) for x in range(2017,2026)]:
    try:
        toc=rec[y]+ca.get(y,0)+inv[y]-ap[y]-cl.get(y,0)+ppe[y]
        print(y,'rec',round(rec[y],1),'ca',round(ca.get(y,0),1),'inv',round(inv[y],1),'ap',round(ap[y],1),'cl',round(cl.get(y,0),1),'ppe',round(ppe[y],1),'TOC',round(toc,1),'OI+am',round(oi[y]+am.get(y,0),1),'ROTOC%',round(100*(oi[y]+am.get(y,0))/toc,1),'eq',round(eq[y],1),'gw',gw.get(y),'ia',ia.get(y))
    except KeyError as e: print(y,'missing',e)
