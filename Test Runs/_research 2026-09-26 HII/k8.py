import json
n=0
for fn in ['submissions.json','sub001.json']:
    d=json.load(open(fn)); r=d['filings']['recent'] if 'filings' in d else d
    for i in range(len(r['form'])):
        if r['form'][i].startswith('8-K'):
            n+=1
            it=r['items'][i]
            if any(x in it for x in ('1.01','2.01','4.02','1.02','2.06','4.01')):
                print(r['filingDate'][i], r['form'][i], r['accessionNumber'][i], it)
        if r['form'][i].startswith('10-12') or r['form'][i] in ('10-K/A','10-Q/A'):
            print('   ',r['filingDate'][i], r['form'][i], r['accessionNumber'][i])
print('8-K count',n)
