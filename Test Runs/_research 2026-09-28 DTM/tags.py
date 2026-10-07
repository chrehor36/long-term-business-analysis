import json
f=json.load(open('cache/facts.json'))['facts']['us-gaap']
tags=['NetCashProvidedByUsedInOperatingActivities','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','ShareBasedCompensation','DepreciationDepletionAndAmortization','DepreciationAndAmortization','PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireBusinessesGross','ProceedsFromEquityMethodInvestmentDividendsOrDistributionsReturnOfCapital','IncomeLossFromEquityMethodInvestments','OperatingIncomeLoss','NetIncomeLoss','Revenues','ProceedsFromEquityMethodInvestmentDividendsOrDistributions','PaymentsToAcquireEquityMethodInvestments','AmortizationOfIntangibleAssets','InterestPaidNet','IncomeTaxesPaidNet','PaymentsOfDividendsCommonStock','LongTermDebt','LongTermDebtNoncurrent']
for t in tags:
    if t not in f: print(t,'--absent'); continue
    u=f[t]['units'].get('USD',[])
    d={}
    for it in u:
        if it.get('form')!='10-K': continue
        s=it.get('start'); e=it['end']
        if s and not (s[5:]=='01-01' and e[5:]=='12-31'): continue
        key=e[:4]
        if key not in d or it['fy']>d[key][1]: d[key]=(it['val'],it['fy'],it['accn'])
    print(t, {k:(round(v[0]/1e6),v[1]) for k,v in sorted(d.items())})
