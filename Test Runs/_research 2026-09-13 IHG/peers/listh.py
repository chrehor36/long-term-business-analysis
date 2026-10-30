import sys, json
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 IHG')
import edgar
s = edgar.submissions(1468174)
for f in s['filings']['files']:
    d = json.loads(edgar.get('https://data.sec.gov/submissions/'+f['name']))
    for i in range(len(d['form'])):
        if d['form'][i] in ('10-K','10-K/A'):
            print(d['form'][i], d['reportDate'][i], d['filingDate'][i], d['accessionNumber'][i], d['primaryDocument'][i])
