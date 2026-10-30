import json, sys
sys.path.insert(0, '.')
from fetch import get
for name, cik in [('Avista', '0000104918'), ('NorthWestern Energy Group', '0001993004'), ('NorthWestern Corp', '0000073088')]:
    j = json.loads(get("https://data.sec.gov/submissions/CIK%s.json" % cik))
    r = j['filings']['recent']
    ks = [(r['filingDate'][i], r['accessionNumber'][i]) for i in range(len(r['form'])) if r['form'][i] == '10-K'][:3]
    print(name, ks)
NI = {'IDA': [198.3,212.4,226.8,232.9,237.4,245.6,259.0,261.2,289.2,323.5],
      'AVA': [137.2,115.9,136.4,197.0,129.5,147.3,155.0,171.0,180.0,193.0],
      'NWE': [164.2,162.7,197.0,202.1,155.2,186.8,183.0,194.1,224.1,181.1]}
EQ = {'IDA': [2057.9,2153.9,2251.4,2370.4,2464.6,2560.0,2668.4,2807.2,2907.6,3331.0,3571.9],
      'AVA': [1528.6,1648.7,1729.8,1773.2,1939.3,2029.7,2154.7,2335.0,2485.0,2591.0,None],
      'NWE': [1600.2,1676.2,1798.9,1942.4,2039.1,2079.1,2339.7,2665.2,2785.3,None,None]}
yrs = list(range(2016, 2026))
for k in NI:
    roes = []
    for i, y in enumerate(yrs):
        a, b = EQ[k][i], EQ[k][i+1]
        roes.append(NI[k][i]/((a+b)/2)*100 if (a and b) else None)
    s = ' '.join(('%5.1f' % x) if x else '    -' for x in roes)
    v = [x for x in roes if x]
    print(k, s, ' mean %.1f over %d yrs' % (sum(v)/len(v), len(v)))
print('    ', ' '.join(str(y) for y in yrs))
