import urllib.request, json, urllib.parse, time, os
UA = {'User-Agent': 'Chris Hrehor chrehor36@gmail.com'}

def q(path, **kw):
    url = 'https://banks.data.fdic.gov/api/' + path + '?' + urllib.parse.urlencode(kw)
    for _ in range(3):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read())
        except Exception as e:
            print('retry', e); time.sleep(3)
    raise SystemExit('failed ' + url)

PA = ['Adams', 'Berks', 'Cumberland', 'Franklin', 'Lancaster', 'York']
MD = ['Baltimore', 'Carroll', 'Frederick']

# 1. all branches in ACNB's nine counties -> CERT set with office counts
certs = {}
for st, counties in (('PA', PA), ('MD', MD)):
    for c in counties:
        off = 0
        page = 0
        while True:
            r = q('locations',
                  filters=f'STALP:{st} AND COUNTY:"{c}"',
                  fields='CERT,NAME,COUNTY,STALP,OFFNAME',
                  limit='1000', offset=str(page * 1000))
            rows = r['data']
            if not rows:
                break
            for x in rows:
                d = x['data']
                key = d['CERT']
                certs.setdefault(key, {'NAME': d.get('NAME', ''), 'offices': 0, 'counties': set()})
                certs[key]['offices'] += 1
                certs[key]['counties'].add(f"{c},{st}")
            off += len(rows)
            if len(rows) < 1000:
                break
            page += 1
        print(st, c, off)
print('distinct certs with an office in the nine counties:', len(certs))

# 2. financials at 2025-12-31 for each
out = []
cl = list(certs)
for i in range(0, len(cl), 1):
    chunk = cl[i:i + 1]
    r = q('financials', filters='REPDTE:20251231', search='CERT:'+str(chunk[0]),
          fields='CERT,NAME,ASSET,DEP,DEPUNINS,DEPNIDOM,COREDEP,NIMY,INTEXPY,EEFFR,ROE,ROA,ROAPTX,EQ,LNLSDEPR',
          limit='5')
    for x in r['data']:
        d = x['data']
        if str(d['CERT']) not in certs:
            continue
        d['offices'] = certs[str(d['CERT'])]['offices']
        d['counties'] = sorted(certs[str(d['CERT'])]['counties'])
        out.append(d)
print('financials rows', len(out))
json.dump(out, open('fdic_footprint_2025.json', 'w'), indent=1)

out.sort(key=lambda d: -(d.get('ASSET') or 0))
print(f"{'CERT':>6} {'NAME':44} {'offices':>7} {'assets$m':>9} {'NIMY':>6} {'INTEXPY':>7} {'EEFFR':>6} {'ROE':>6} {'ROA':>5} {'uninsD%':>7} {'NIB%':>5}")
for d in out:
    a = d.get('ASSET') or 0
    dep = d.get('DEP') or 1
    print(f"{d['CERT']:>6} {(d.get('NAME') or '')[:44]:44} {d['offices']:>7} {a/1000:9.0f} "
          f"{(d.get('NIMY') or 0):6.2f} {(d.get('INTEXPY') or 0):7.2f} {(d.get('EEFFR') or 0):6.1f} "
          f"{(d.get('ROE') or 0):6.2f} {(d.get('ROA') or 0):5.2f} {100*(d.get('DEPUNINS') or 0)/dep:7.1f} "
          f"{100*(d.get('DEPNIDOM') or 0)/dep:5.1f}")
