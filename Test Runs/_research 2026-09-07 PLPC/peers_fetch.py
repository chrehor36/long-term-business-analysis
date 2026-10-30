import json, urllib.request, time, os, sys
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
D=os.path.dirname(os.path.abspath(__file__))
def get(u, tries=4):
    import gzip, io
    for i in range(tries):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=120)
            b=r.read()
            if r.headers.get('Content-Encoding')=='gzip':
                b=gzip.decompress(b)
            return b
        except Exception as e:
            print('retry',u,repr(e)); time.sleep(3)
    raise SystemExit('FAIL '+u)

tk=json.loads(get('https://www.sec.gov/files/company_tickers.json'))
open(os.path.join(D,'company_tickers.json'),'wb').write(json.dumps(tk).encode())
want={'HUBB','VMI','NVT','AZZ','ATKR','THR','WIRE','PLPC'}
m={}
for k,v in tk.items():
    if v['ticker'] in want:
        m[v['ticker']]=(v['cik_str'], v['title'])
for t in sorted(want):
    print(t, m.get(t))
json.dump(m, open(os.path.join(D,'peer_ciks.json'),'w'), indent=1)

for t,(cik,name) in sorted(m.items()):
    if t=='PLPC': continue
    out=os.path.join(D,f'companyfacts_{t}.json')
    if os.path.exists(out) and os.path.getsize(out)>10000:
        print('have',t); continue
    u=f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json'
    b=get(u)
    open(out,'wb').write(b)
    print('saved',t,cik,len(b))
    time.sleep(0.5)
