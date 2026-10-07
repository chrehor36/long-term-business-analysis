import json,datetime as dt
def series(t, tags, unit='USD'):
    d=json.load(open(f'peers/{t}_facts.json' if t!='BCC' else 'BCC_facts.json'))['facts']['us-gaap']
    out={}
    for tag in tags:
        if tag not in d: continue
        for x in d[tag]['units'].get(unit,[]):
            if not x['form'].startswith('10-K') or not x.get('start'): continue
            a=dt.date.fromisoformat(x['start']); b=dt.date.fromisoformat(x['end'])
            if 350<=(b-a).days<=380:
                y=b.year if b.month>6 else b.year-1
                out.setdefault(y,(x['val'],x['accn']))
    return out
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
