import json, os
f = json.load(open('BE_companyfacts.json'))
facts = f['facts']['us-gaap']
def ann(tag, fp_only=True):
    out={}
    if tag not in facts: return out
    for u,rows in facts[tag]['units'].items():
        for r in rows:
            if r.get('form') not in ('10-K','10-K/A'): continue
            if 'start' in r:
                # annual duration only
                from datetime import date
                s=date.fromisoformat(r['start']); e=date.fromisoformat(r['end'])
                if (e-s).days < 350 or (e-s).days>380: continue
            key=r['end']
            out.setdefault(key,[]).append((r.get('fy'),r.get('fp'),r['val'],r.get('accn')))
    return out
tags=['NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation',
 'PaymentsToAcquirePropertyPlantAndEquipment','DepreciationDepletionAndAmortization',
 'DepreciationAmortizationAndAccretionNet','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax',
 'NetIncomeLoss','ContractWithCustomerLiability','ContractWithCustomerLiabilityCurrent',
 'ContractWithCustomerLiabilityNoncurrent','IncreaseDecreaseInContractWithCustomerLiability',
 'CostOfRevenue','GrossProfit']
for t in tags:
    d=ann(t)
    if not d: print(t,'MISSING'); continue
    print('===',t)
    for k in sorted(d):
        vals=sorted(set(v[2] for v in d[k]))
        print('  ',k, [round(v/1e6,1) for v in vals])
