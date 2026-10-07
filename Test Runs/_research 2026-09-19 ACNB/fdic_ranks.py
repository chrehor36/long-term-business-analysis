import urllib.request, json, urllib.parse, time, os
UA = {'User-Agent': 'Chris Hrehor chrehor36@gmail.com'}

def q(path, **kw):
    url = 'https://banks.data.fdic.gov/api/' + path + '?' + urllib.parse.urlencode(kw)
    for _ in range(4):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read())
        except Exception as e:
            print('retry', e); time.sleep(3)
    raise SystemExit('failed ' + url)

base = json.load(open('fdic_footprint_2025.json'))
certs = {str(d['CERT']): d for d in base}

FIELDS = ('CERT,NAME,ASSET,DEP,DEPUNINS,DEPNIDOM,COREDEP,NIMY,INTEXPY,EEFFR,ROE,ROA,ROAPTX,EQ,'
          'LNLSDEPR,NTLNLSQ,NTLNLSR,LNATRES,LNLSNTV,IDT1RWAJR,RBCT1J,RBC1RWAJ,RBCRWAJ')

for rep in ('20260630', '20251231', '20241231', '20231231', '20221231', '20211231'):
    p = f'fdic_footprint_{rep}.json'
    if os.path.exists(p):
        print('have', p); continue
    out = []
    for c in certs:
        r = q('financials', filters=f'REPDTE:{rep}', search='CERT:' + c, fields=FIELDS, limit='5')
        for x in r['data']:
            d = x['data']
            if str(d['CERT']) != c:
                continue
            d['offices'] = certs[c]['offices']
            out.append(d)
    json.dump(out, open(p, 'w'), indent=1)
    print(rep, len(out))
