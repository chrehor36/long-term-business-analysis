import json,urllib.request,time,sys
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
peers={'OGS':'0001587732','ATO':'0000731802','SR':'0001126956','NWN':'0001733998'}
out={}
for t,c in peers.items():
    if t=='OGS': d=json.load(open('cache/facts.json'))
    else:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json',headers=UA)).read()); time.sleep(0.5)
    def ser(tags,dur):
        for tag in tags:
            try: arr=d['facts']['us-gaap'][tag]['units']['USD']
            except KeyError: continue
            r={}
            for f in arr:
                if f['form']!='10-K' or f.get('fp')!='FY': continue
                if dur:
                    if 'start' not in f: continue
                    import datetime as D
                    if not (350<=(D.date.fromisoformat(f['end'])-D.date.fromisoformat(f['start'])).days<=380): continue
                r.setdefault(f['end'][:7],(f['val'],f['accn']))
            if r: return tag,r
        return None,{}
    ni_t,ni=ser(['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss'],True)
    eq_t,eq=ser(['StockholdersEquity'],False)
    print(t,ni_t,eq_t)
    ks=sorted(ni)
    for k in ks:
        if k[:4]<'2015': continue
        prev=[e for e in eq if e<k]
        pe=eq[max(prev)][0] if prev else None
        ce=eq.get(k,(None,))[0]
        roe= ni[k][0]/((pe+ce)/2) if pe and ce else None
        print(f"  {k} NI {ni[k][0]/1e6:8.1f} Eq {ce/1e6 if ce else 0:8.1f} ROE(avg eq) {roe*100 if roe else 0:5.1f}%  accn {ni[k][1]}")
