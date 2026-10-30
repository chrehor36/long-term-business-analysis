import re, sys, urllib.request
UA = {'User-Agent': 'Chris Hrehor chrehor36@gmail.com'}
for acc in sys.argv[1:]:
    a = acc.replace('-', '')
    u = f'https://www.sec.gov/Archives/edgar/data/898173/{a}/'
    d = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read().decode('utf-8', 'replace')
    print(acc, sorted(set(re.findall(r'([A-Za-z0-9_\-\.]+\.htm)', d))))
