import json,sys
d=json.load(open(sys.argv[1]))
r=d['filings']['recent']
for i in range(len(r['form'])):
    if r['form'][i] in ('10-K','10-Q','8-K','DEF 14A','424B5','424B2','S-3ASR','8-K/A') and r['filingDate'][i]>='2021-01-01':
        print(r['filingDate'][i],r['form'][i],r['accessionNumber'][i],r['primaryDocument'][i],r.get('items',['']*9999)[i])
