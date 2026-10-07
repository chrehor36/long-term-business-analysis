import json,urllib.request,gzip,sys,os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(cik,tk):
    fn=f'{tk}_facts.json'
    if not os.path.exists(fn):
        r=urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json',headers=UA)).read()
        try: r=gzip.decompress(r)
        except: pass
        open(fn,'wb').write(r)
    return json.load(open(fn))
def annual(d,tags):
    out={}
    for t in tags:
        for unit in ('USD',):
            try: arr=d['facts']['us-gaap'][t]['units'][unit]
            except KeyError: continue
            for x in arr:
                if x.get('form','').startswith('10-K') and 'frame' in x and len(x['frame'])==6:
                    # duration ~1 yr
                    out.setdefault(x['frame'],(x['val'],x['accn'],t))
    return out
peers={'SCVL':895447,'DBI':1319947,'CAL':14707,'FL':850209,'ASO':1817358}
for tk,cik in peers.items():
    d=get(cik,tk)
    rev=annual(d,['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueGoodsNet'])
    oi=annual(d,['OperatingIncomeLoss'])
    gp=annual(d,['GrossProfit'])
    print('==',tk,d['entityName'])
    for fr in sorted(set(rev)|set(oi)):
        r=rev.get(fr,(None,))[0]; o=oi.get(fr,(None,))[0]; g=gp.get(fr,(None,))[0]
        m=f'{o/r*100:6.1f}%' if r and o is not None else '   n/a'
        gm=f'{g/r*100:6.1f}%' if r and g else '   n/a'
        print(fr, f'{(r or 0)/1e6:9.0f}', f'{(o or 0)/1e6:8.0f}', m, gm, oi.get(fr,(0,''))[1] if fr in oi else rev.get(fr)[1])
