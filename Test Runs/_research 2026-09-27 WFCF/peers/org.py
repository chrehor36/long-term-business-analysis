import urllib.request, json, sys
UA={'User-Agent':'Mozilla/5.0 research'}
for ein in sys.argv[1:]:
    u=f'https://projects.propublica.org/nonprofits/api/v2/organizations/{ein}.json'
    b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
    open(f'pp_{ein}.json','wb').write(b)
    d=json.loads(b); o=d['organization']
    print('==',ein,o['name'],o.get('ntee_code'))
    for f in sorted(d['filings_with_data'],key=lambda x:x['tax_prd'])[-12:]:
        r=f.get('totrevenue'); e=f.get('totfuncexpns'); 
        print(' ',f['tax_prd'],'rev',r,'exp',e,'surplus',(r-e) if r is not None and e is not None else None,'margin',round((r-e)/r*100,1) if r else None,'assets',f.get('totassetsend'),'progrev',f.get('totprgmrevnue'), 'pdf',bool(f.get('pdf_url')))
