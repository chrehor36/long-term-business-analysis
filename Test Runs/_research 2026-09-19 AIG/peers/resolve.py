# Re-resolve every competitor-row accession from each registrant's own submissions JSON (not from the CB file).
import sys, os, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
CLAIMED = {  # accessions cited in the CB/MKL row, plus the two added here
 'CB':  ['0000896159-26-000005','0000896159-24-000003','0000896159-22-000005'],
 'WRB': ['0000011544-26-000005','0000011544-24-000005'],
 'ACGL':['0000947484-26-000017','0000947484-24-000020'],
 'RLI': ['0001104659-26-018013','0001558370-24-001599'],
 'KNSL':['0001669162-26-000015','0001669162-24-000006','0001669162-23-000009'],
 'AXS': ['0001214816-26-000097','0001214816-24-000024'],
 'MKL': ['0001096343-26-000020'],
 'TRV': [], 'HIG': [],
}
res = {}
for t, accs in CLAIMED.items():
    cik, name = sources.cik_for(t)
    raw = sources._get('https://data.sec.gov/submissions/CIK%s.json' % cik, headers=sources.SEC_UA, cache_name='aigpeer_sub_'+t, max_age_h=24)
    if not isinstance(raw, str): raw = raw.decode()
    r = json.loads(raw)['filings']['recent']
    tenks = [(r['filingDate'][i], r['reportDate'][i], r['accessionNumber'][i], r['primaryDocument'][i]) for i in range(len(r['form'])) if r['form'][i] == '10-K']
    have = {a for _, _, a, _ in tenks}
    for a in accs:
        print('%-5s %-10s %s  %s' % (t, cik, a, 'MATCH (10-K in own submissions)' if a in have else 'NOT FOUND'))
    res[t] = tenks[:5]
    if not accs:
        for x in tenks[:5]: print('%-5s %-10s %s' % (t, cik, x))
json.dump(res, open(os.path.join('Test Runs/_research 2026-09-19 AIG/peers', 'resolved.json'), 'w'), indent=1)
