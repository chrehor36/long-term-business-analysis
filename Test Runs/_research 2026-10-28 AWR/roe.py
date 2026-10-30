import json,sys
sys.stdout.reconfigure(encoding="utf-8")
def annual(cf,tags,unit='USD'):
    for t in tags:
        d=cf['facts'].get('us-gaap',{}).get(t)
        if not d: continue
        out={}
        for f in d['units'].get(unit,[]):
            if f.get('form')=='10-K' and f.get('fp')=='FY':
                if 'start' in f:
                    # duration: need ~1 year
                    from datetime import date
                    s=date.fromisoformat(f['start']);e=date.fromisoformat(f['end'])
                    if not 350<(e-s).days<380: continue
                y=int(f['end'][:4])
                if f['end'][5:]!='12-31': continue
                out.setdefault(y,(f['val'],f['accn'],f['filed']))
                # keep first-filed
                if f['filed']<out[y][2]: out[y]=(f['val'],f['accn'],f['filed'])
        if out: return out,t
    return {},None
for n in ['awr','cwt','sjw','wtrg']:
    cf=json.load(open(f'cache/cf_{n}.json'))
    ni,t1=annual(cf,(['NetIncomeLoss'] if n=='cwt' else ['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss']))
    eq,t2=annual(cf,['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'] if n=='cwt' else ['StockholdersEquity'])
    rev,t3=annual(cf,(['RegulatedAndUnregulatedOperatingRevenue','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'] if n=='cwt' else ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RegulatedAndUnregulatedOperatingRevenue']))
    oi,t4=annual(cf,['OperatingIncomeLoss'])
    print('==',n,cf['entityName'],t1,t2,t3,t4)
    for y in range(2016,2026):
        if y in ni and y in eq and y-1 in eq:
            roe=ni[y][0]/((eq[y][0]+eq[y-1][0])/2)
            m = oi[y][0]/rev[y][0] if (y in oi and y in rev) else float('nan')
            print(y, f"NI {ni[y][0]/1e6:8.1f}  avgEq {(eq[y][0]+eq[y-1][0])/2e6:8.1f}  ROE {roe*100:5.1f}%  opmargin {m*100:5.1f}%  accn {ni[y][1]}")
