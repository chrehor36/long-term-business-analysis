import sys, json
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 IHG')
import edgar
P = {'MAR':1048286,'HLT':1585689,'H':1468174,'WH':1722684,'CHH':1046311}
out = {}
for t,c in P.items():
    s = edgar.submissions(c)
    r = s['filings']['recent']
    rows=[]
    for i in range(len(r['form'])):
        if r['form'][i] in ('10-K','10-K/A'):
            rows.append((r['form'][i], r['reportDate'][i], r['filingDate'][i], r['accessionNumber'][i], r['primaryDocument'][i]))
    print(t, s['name'], len(s['filings'].get('files',[])))
    for x in rows: print('  ', x)
    out[t]=rows
json.dump(out, open('tenk_list.json','w'), indent=1)
