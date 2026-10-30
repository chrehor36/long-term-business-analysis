import json,sys
sys.stdout.reconfigure(encoding='utf-8')
def series(path,tags,fy_end='12-31',duration=True):
    d=json.load(open(path))['facts']['us-gaap']
    out={}
    for tag in tags:
        if tag not in d: continue
        u=d[tag]['units']['USD']
        for f in u:
            if f['form'] not in ('10-K',) or f.get('fp')!='FY': continue
            if duration:
                if 'start' not in f: continue
                from datetime import date
                s=date.fromisoformat(f['start']); e=date.fromisoformat(f['end'])
                if not (350<(e-s).days<380): continue
            y=int(f['end'][:4]) if f['end'][5:7]>='07' else int(f['end'][:4])-1
            if f['end'][5:7]>='07': y=int(f['end'][:4])
            # first filed value
            if y not in out or f['filed']<out[y][1]: out[y]=(f['val'],f['filed'],tag)
    return out
peers={'NI':'cache/companyfacts.json','ATO':'cache/peer_0000731802_companyfacts.json','CNP':'cache/peer_0001130310_companyfacts.json','OGS':'cache/peer_0001587732_companyfacts.json'}
for n,p in peers.items():
    ni=series(p,['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss'])
    eq=series(p,['StockholdersEquity'],duration=False)
    # for ATO fiscal year ends Sept
    print(n)
    rows=[]
    for y in range(2015,2026):
        if y in ni and y in eq and (y-1) in eq:
            avg=(eq[y][0]+eq[y-1][0])/2
            rows.append((y,ni[y][0]/1e6,eq[y][0]/1e6,ni[y][0]/avg*100))
    for r in rows: print('  %d NI %.1f Eq %.1f ROE %.1f%%'%r)
    if rows:
        import statistics
        print('  mean ROE %d-%d: %.1f%%'%(rows[0][0],rows[-1][0],statistics.mean(r[3] for r in rows)))
        r5=[r for r in rows if r[0]>=2021]; print('  mean ROE 2021-2025: %.1f%%'%statistics.mean(r[3] for r in r5))
