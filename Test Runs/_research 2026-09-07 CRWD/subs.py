import json, urllib.request, sys
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read()
ciks={'CRWD':1535527,'PANW':1327567,'S':1583708,'FTNT':1262039,'MSFT':789019}
for t,c in ciks.items():
    d=json.loads(get(f"https://data.sec.gov/submissions/CIK{c:010d}.json"))
    r=d['filings']['recent']
    print(f"=== {t} {d['name']} CIK {c} FYE={d.get('fiscalYearEnd')} ===")
    n=0
    for i,f in enumerate(r['form']):
        if f=='10-K':
            print(f"  {r['accessionNumber'][i]} | filed {r['filingDate'][i]} | period {r['reportDate'][i]} | {r['primaryDocument'][i]}")
            n+=1
            if n>=8: break
