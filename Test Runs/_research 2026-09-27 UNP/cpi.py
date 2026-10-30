import json,urllib.request
out={}
for a,b in ((1996,2005),(2006,2015),(2016,2025)):
    body=json.dumps({'seriesid':['CUUR0000SA0'],'startyear':str(a),'endyear':str(b)}).encode()
    req=urllib.request.Request('https://api.bls.gov/publicAPI/v1/timeseries/data/',data=body,headers={'Content-Type':'application/json','User-Agent':'Mozilla/5.0'})
    d=json.loads(urllib.request.urlopen(req,timeout=60).read())
    for s in d['Results']['series'][0]['data']:
        if s['period'].startswith('M') and s['period']!='M13' and s['value'].replace('.','').isdigit():
            out.setdefault(s['year'],[]).append(float(s['value']))
json.dump(out,open('cpi_bls.json','w'))
for y in sorted(out): print(y,len(out[y]),round(sum(out[y])/len(out[y]),3))
