import json, io, os, collections
D = os.path.dirname(os.path.abspath(__file__))
cf = json.load(io.open(os.path.join(D,'companyfacts.json'), encoding='utf-8'))
us = cf['facts']['us-gaap']
def annual(tag, vintage='newest'):
    """FY figures: frames with ~365 day duration, keyed by fy end, newest accession wins."""
    if tag not in us: return {}
    out = {}
    for unit, arr in us[tag]['units'].items():
        if unit != 'USD': continue
        for f in arr:
            if 'start' not in f: 
                continue
            import datetime
            s = datetime.date(*map(int, f['start'].split('-')))
            e = datetime.date(*map(int, f['end'].split('-')))
            days = (e-s).days
            if not (340 <= days <= 400): continue
            key = f['end']
            prev = out.get(key)
            if prev is None or f.get('accn','') > prev[1]:
                out[key] = (f['val'], f.get('accn',''), f.get('form',''), f.get('fy'), f.get('fp'))
    return dict(sorted(out.items()))
def instant(tag):
    if tag not in us: return {}
    out={}
    for unit, arr in us[tag]['units'].items():
        if unit != 'USD': continue
        for f in arr:
            if 'start' in f: continue
            key=f['end']
            prev=out.get(key)
            if prev is None or f.get('accn','')>prev[1]:
                out[key]=(f['val'],f.get('accn',''))
    return dict(sorted(out.items()))
tags = ['NetCashProvidedByUsedInOperatingActivities',
        'NetCashProvidedByUsedInOperatingActivitiesContinuingOperations',
        'PaymentsToAcquirePropertyPlantAndEquipment',
        'PaymentsForSoftware','PaymentsToDevelopSoftware','PaymentsToAcquireSoftware',
        'Depreciation','DepreciationDepletionAndAmortization',
        'AmortizationOfIntangibleAssets',
        'ShareBasedCompensation',
        'NetIncomeLoss','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax',
        'PaymentsOfDividendsCommonStock','PaymentsForRepurchaseOfCommonStock',
        'ProceedsFromIssuanceOfCommonStock','IncomeTaxesPaidNet','InterestPaidNet',
        'StockRepurchasedDuringPeriodValue','PaymentsToAcquireBusinessesNetOfCashAcquired']
for t in tags:
    a = annual(t)
    if not a: 
        print(t, 'ABSENT'); continue
    print('==', t)
    for k,v in a.items():
        print('   ', k, '%14s'%('{:,}'.format(v[0])), v[1], v[2], v[3], v[4])
