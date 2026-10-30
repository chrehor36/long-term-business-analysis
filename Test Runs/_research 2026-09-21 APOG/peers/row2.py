import json
# CALENDAR ALIGNMENT, stated: Apogee's fiscal year ending late Feb of year Y runs
# Mar(Y-1)..Feb(Y), so it maps to CALENDAR YEAR Y-1. Peers with Dec year-ends map to
# their own end year. Quanex (Oct 31) maps to its end year. This is the "same window".
def ann(G,tags,unit='USD',dur=True):
    for t in tags:
        if t not in G: continue
        out={}
        for u in G[t]['units'].get(unit,[]):
            if u.get('form') not in ('10-K','10-K/A'): continue
            s,e=u.get('start'),u['end']
            if dur:
                if not s: continue
                d=(int(e[:4])-int(s[:4]))*12+(int(e[5:7])-int(s[5:7]))
                if d<11 or d>13: continue
            else:
                if s: continue
            y,m=int(e[:4]),int(e[5:7])
            cal = y-1 if m<=6 else y          # Feb/Jan/Apr enders -> prior calendar year
            if cal in out and e < out[cal][0]: continue
            out[cal]=(e,u['val'])
        if out: return t,out
    return None,{}
YRS=list(range(2015,2026))
def series(path):
    G=json.load(open(path))['facts']['us-gaap']
    _,op=ann(G,['OperatingIncomeLoss'])
    _,rev=ann(G,['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet'])
    _,at=ann(G,['Assets'],dur=False)
    _,cl=ann(G,['LiabilitiesCurrent'],dur=False)
    out={}
    for y in YRS:
        if y in op and y in rev and y in at and y in cl:
            ce=at[y][1]-cl[y][1]
            out[y]=(op[y][1]/rev[y][1]*100, op[y][1]/ce*100 if ce else None, rev[y][1]/1e6, op[y][0])
    return out
names={'APOG':'../companyfacts.json','TGLS':'TGLS_companyfacts.json','ROCK':'ROCK_companyfacts.json',
       'JELD':'JELD_companyfacts.json','AWI':'AWI_companyfacts.json','GFF':'GFF_companyfacts.json',
       'NX':'NX_companyfacts.json','BLDR':'BLDR_companyfacts.json'}
S={k:series(v) for k,v in names.items()}
print('EBIT / CAPITAL EMPLOYED (operating income / (total assets - current liabilities)), by CALENDAR year')
hdr='cal '+' '.join(f'{k:>7}' for k in names)
print(hdr)
for y in YRS:
    print(f'{y} '+' '.join((f'{S[k][y][1]:7.1f}' if y in S[k] and S[k][y][1] is not None else '    n/a') for k in names))
print()
print('OPERATING MARGIN %')
print(hdr)
for y in YRS:
    print(f'{y} '+' '.join((f'{S[k][y][0]:7.1f}' if y in S[k] else '    n/a') for k in names))
print()
for k in names:
    v=[S[k][y][1] for y in YRS if y in S[k] and S[k][y][1] is not None]
    m=[S[k][y][0] for y in YRS if y in S[k]]
    yy=[y for y in YRS if y in S[k]]
    if v: print(f'{k:>5}: {len(v)}y  mean EBIT/CE {sum(v)/len(v):6.2f}%  min {min(v):6.2f}%  mean op margin {sum(m)/len(m):6.2f}%  years {min(yy)}-{max(yy)}')
print()
print('APOG source end-dates:', {y:S['APOG'][y][3] for y in sorted(S['APOG'])})
print('APOG revenue $M:', {y:round(S['APOG'][y][2],1) for y in sorted(S['APOG'])})
