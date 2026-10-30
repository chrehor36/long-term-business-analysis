import json, glob, os, sys
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
            out[e]=u['val']
        if out: return t,dict(sorted(out.items()))
    return None,{}
def near(d, y):
    # pick the value whose end-date year matches calendar-year label y (fiscal year ending in y)
    best=None
    for k,v in d.items():
        if int(k[:4])==y or (int(k[:4])==y+1 and int(k[5:7])<=2):
            if best is None or k>best[0]: best=(k,v)
    return best
def report(name, path):
    G=json.load(open(path))['facts']['us-gaap']
    to,op=ann(G,['OperatingIncomeLoss'])
    tr,rev=ann(G,['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet'])
    ta,at=ann(G,['Assets'],dur=False)
    tl,cl=ann(G,['LiabilitiesCurrent'],dur=False)
    rows=[]
    for y in range(2016,2027):
        o=near(op,y); r=near(rev,y); a=near(at,y); c=near(cl,y)
        if not(o and r and a and c): rows.append((y,None,None,None)); continue
        ce=a[1]-c[1]
        rows.append((y, o[1]/r[1]*100 if r[1] else None, o[1]/ce*100 if ce else None, r[1]/1e6))
    print(f'--- {name}  (op tag {to}, rev tag {tr})')
    for y,m,rc,rv in rows:
        if m is None: print(f'  FY{y}   n/a'); continue
        print(f'  FY{y}  op margin {m:6.2f}%   EBIT/cap-employed {rc:6.2f}%   rev ${rv:8.1f}M')
    vals=[rc for y,m,rc,rv in rows if rc is not None]
    if vals: print(f'  MEAN EBIT/capital-employed over {len(vals)}y: {sum(vals)/len(vals):.2f}%')
    m2=[m for y,m,rc,rv in rows if m is not None]
    if m2: print(f'  MEAN operating margin over {len(m2)}y: {sum(m2)/len(m2):.2f}%')
for t in ['TGLS','ROCK','NX','JELD','AWI','AAON','GFF','CSTE','BLDR']:
    report(t, f'{t}_companyfacts.json')
report('APOG','../companyfacts.json')
