import json, urllib.request
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=120).read()
d=json.loads(get("https://data.sec.gov/submissions/CIK0001327567.json"))
r=d['filings']['recent']
print("PANW most recent 20 filings of any form:")
for i in range(20):
    print(f"  {r['filingDate'][i]} {r['form'][i]:12s} {r['accessionNumber'][i]} period={r['reportDate'][i]}")
