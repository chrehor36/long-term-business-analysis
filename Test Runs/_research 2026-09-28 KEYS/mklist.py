import json
rows=[]
for p in ('cache/sub_0001601046.json','cache/sub_001.json'):
    d=json.load(open(p)); r=d['filings']['recent'] if 'filings' in d else d
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-K/A'):
            rows.append((r['reportDate'][i], r['form'][i], r['filingDate'][i], r['accessionNumber'][i], r['primaryDocument'][i], '0001601046'))
rows.sort()
open('annual_list.txt','w').write(''.join(' '.join(x)+'\n' for x in rows))
print(open('annual_list.txt').read())
