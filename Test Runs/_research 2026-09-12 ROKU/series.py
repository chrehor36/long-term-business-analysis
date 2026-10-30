import sys, os, json
sys.path.insert(0,os.path.join("C:/Users/chreh/OneDrive/Documents/BRK","tools"))
import sources
f=sources.sec_facts('0001428439')
us=f['facts']['us-gaap']

def ann(tag, lo=340, hi=380):
    if tag not in us: return {}
    out={}
    for unit,rows in us[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A'): continue
            if 'start' not in r: continue
            from datetime import date
            s=date.fromisoformat(r['start']); e=date.fromisoformat(r['end'])
            d=(e-s).days
            if not (lo<=d<=hi): continue
            fy=e.year if e.month>=6 else e.year-1
            key=r['end']
            # keep latest-filed (restated) value
            prev=out.get(key)
            if prev is None or r['filed']>prev[1]:
                out[key]=(r['val'],r['filed'])
    return {k:v[0] for k,v in sorted(out.items())}

def inst(tag):
    if tag not in us: return {}
    out={}
    for unit,rows in us[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A'): continue
            if 'start' in r: continue
            key=r['end']
            prev=out.get(key)
            if prev is None or r['filed']>prev[1]:
                out[key]=(r['val'],r['filed'])
    return {k:v[0] for k,v in sorted(out.items())}

tags={
 'OCF':'NetCashProvidedByUsedInOperatingActivities',
 'SBC':'ShareBasedCompensation',
 'DA':'DepreciationDepletionAndAmortization',
 'DA2':'DepreciationAndAmortization',
 'CAPEX':'PaymentsToAcquirePropertyPlantAndEquipment',
 'REV':'Revenues',
 'GP':'GrossProfit',
 'NI':'NetIncomeLoss',
 'dCL':'IncreaseDecreaseInContractWithCustomerLiability',
 'dDR':'IncreaseDecreaseInDeferredRevenue',
 'AMORT':'AmortizationOfIntangibleAssets',
}
res={}
for k,t in tags.items():
    res[k]=ann(t)
inst_tags={'CL_cur':'ContractWithCustomerLiabilityCurrent','CL_nc':'ContractWithCustomerLiabilityNoncurrent','DR_cur':'DeferredRevenueCurrent','DR_nc':'DeferredRevenueNoncurrent','CL':'ContractWithCustomerLiability','DR':'DeferredRevenue'}
for k,t in inst_tags.items():
    res[k]=inst(t)
print(json.dumps(res,indent=1,default=str))
