import json,io,sys
from datetime import date
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
f=json.load(open('facts.json'))['facts']['us-gaap']
def s(t,dur=True):
    out={}
    for u,vals in f.get(t,{}).get('units',{}).items():
        for v in vals:
            if v.get('form') not in ('10-K','10-K/A'): continue
            if dur:
                if 'start' not in v or (date.fromisoformat(v['end'])-date.fromisoformat(v['start'])).days<350: continue
            k=int(v['end'][:4])
            if k not in out or v['filed']>out[k][1]: out[k]=(v['val']/1e6,v['filed'])
    return {k:x[0] for k,x in out.items()}
rev=s('Revenues'); gp=s('GrossProfit'); cogs=s('CostOfGoodsSold'); cogs.update(s('CostOfGoodsAndServicesSold'))
oi=s('OperatingIncomeLoss'); pt=s('IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'); pt.update(s('IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'))
ie=s('InterestExpense'); ie.update(s('InterestExpenseNonoperating'))
ar=s('AccountsReceivableNetCurrent',False); inv=s('InventoryNet',False); ppe=s('PropertyPlantAndEquipmentNet',False); ap=s('AccountsPayableCurrent',False)
adj={2020:243.320,2021:240.577,2022:290.387,2023:397.716,2024:414.272,2025:414.598}
print('FY | sales | gross margin | EBIT (op income or pretax+interest) | EBIT margin | NTOA | EBIT/NTOA | adjusted OI/NTOA')
for y in range(2009,2026):
    g=gp.get(y, rev[y]-cogs[y] if y in cogs else None)
    e=oi.get(y, pt.get(y,0)+ie.get(y,0))
    nt=ar[y]+inv[y]+ppe[y]-ap[y]
    a=adj.get(y)
    print(y,f"{rev[y]:.1f} | {g/rev[y]*100:.1f}% | {e:.1f} | {e/rev[y]*100:.1f}% | {nt:.1f} | {e/nt*100:.1f}% |", f"{a/nt*100:.1f}%" if a else '')
