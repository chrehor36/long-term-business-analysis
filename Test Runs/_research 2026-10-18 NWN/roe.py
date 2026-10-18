import json,sys
def series(f,tag):
    out={}
    for ns in ('us-gaap',):
        if tag not in f[ns]: return out
        for r in f[ns][tag]['units']['USD']:
            if r['form'].startswith('10-K') and r.get('fp')=='FY':
                if 'start' in r:
                    if r['start'][5:]=='01-01' and r['end'][5:]=='12-31' and r['start'][:4]==r['end'][:4]:
                        out.setdefault(r['end'][:4],r['val'])
                elif r['end'][5:]=='12-31': out.setdefault(r['end'][:4],r['val'])
    return out
for name in sys.argv[1:]:
    f=json.load(open(f'cache/facts_{name}.json'))['facts']
    ni=series(f,'NetIncomeLoss') if name!='por' else series(f,'ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest')
    ni2=series(f,'NetIncomeLossAvailableToCommonStockholdersBasic')
    eq={**series(f,'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'),**series(f,'StockholdersEquity')}
    print(name)
    for y in range(2016,2026):
        y=str(y);p=str(int(y)-1)
        n=ni.get(y) or ni2.get(y)
        if n and eq.get(y) and eq.get(p):
            print(' ',y,f"NI {n/1e6:.1f} eq {eq[y]/1e6:.0f} ROE {n/((eq[y]+eq[p])/2)*100:.1f}%")
        else: print(' ',y,n,eq.get(y))
