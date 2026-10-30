import json, urllib.request, time, sys
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60); time.sleep(0.15); return r.read()
for name,cik in [('MBUU',1590976),('MCFT',1638290)]:
    d=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik:010d}.json'))
    json.dump(d,open(f'raw/{name}_sub.json','w'))
    r=d['filings']['recent']
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-K/A') or (name=='MBUU' and r['form'][i]=='8-K' and r['filingDate'][i]>='2024-07-01'):
            print(name,r['form'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i],r.get('items',['']*99)[i])
    print(name,'files',d['filings'].get('files'))
