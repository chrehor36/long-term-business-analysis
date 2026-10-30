import json,sys,urllib.request
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def facts(cik):
    r=urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json',headers=UA)
    return json.load(urllib.request.urlopen(r,timeout=120))
def series(d,tags,inst=False):
    for t in tags:
        if t in d['facts']['us-gaap']:
            out={}
            for f in d['facts']['us-gaap'][t]['units'].get('USD',[]):
                fr=f.get('frame','')
                if f.get('form','').startswith('10-K') and ((inst and fr.endswith('Q4I')) or (not inst and len(fr)==6)):
                    out[fr[2:6]]=f['val'];
            if out: return t,out
    return None,{}
for name,cik in [('SO',92122),('DUK',1326160),('ETR',65984),('D',715957)]:
    d=facts(cik)
    tn,ni=series(d,['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss'])
    te,eq=series(d,['StockholdersEquity'],inst=True)
    line=[]
    for y in range(2021,2026):
        y=str(y);py=str(int(y)-1)
        if y in ni and y in eq and py in eq:
            line.append(f"{y}:{ni[y]/1e6:,.0f}/{(eq[y]+eq[py])/2e6:,.0f}={ni[y]/((eq[y]+eq[py])/2)*100:.1f}%")
        else: line.append(f"{y}:NA")
    tot=sum(ni.get(str(y),0) for y in range(2021,2026)); ae=sum((eq.get(str(y),0)+eq.get(str(y-1),0))/2 for y in range(2021,2026))
    print(name,tn,'|',' '.join(line),f'| 5y {tot/ae*100:.1f}%')
