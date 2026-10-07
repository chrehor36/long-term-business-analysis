import json, os, re, time, urllib.request

UA = "BRK-research chrehor36@gmail.com"
D = os.path.dirname(os.path.abspath(__file__))

def get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding":"identity"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

# earnings 8-Ks: item 2.02
subs=[]
for f in ['submissions.json','submissions-001.json']:
    d=json.load(open(os.path.join(D,f)))
    r=d.get('filings',{}).get('recent') if 'filings' in d else d
    for i,fm in enumerate(r['form']):
        if fm=='8-K' and '2.02' in (r['items'][i] or ''):
            subs.append((r['filingDate'][i], r['accessionNumber'][i]))
subs=sorted(set(subs), reverse=True)
subs=[s for s in subs if s[0] >= '2012-01-01']
print(len(subs),"earnings 8-Ks since 2018")

manifest={}
for date, acc in subs:
    nod = acc.replace('-','')
    idx_url = f"https://www.sec.gov/Archives/edgar/data/104169/{nod}/{acc}-index.htm"
    ip = os.path.join(D, f"idx-{date}.html")
    if not os.path.exists(ip):
        try:
            open(ip,'wb').write(get(idx_url)); time.sleep(0.25)
        except Exception as e:
            print("IDXFAIL", date, acc, e); continue
    html = open(ip, encoding='utf-8', errors='replace').read()
    # rows: <tr>...<td>seq</td><td>desc</td><td><a href=doc></td><td>TYPE</td>
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.S|re.I)
    cand=[]
    for row in rows:
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S|re.I)
        if len(cells) < 4: continue
        txt = [re.sub(r'<[^>]+>','',c).strip() for c in cells]
        href = re.search(r'href="([^"]+)"', row)
        if not href: continue
        typ = txt[3] if len(txt)>3 else ''
        desc = txt[1] if len(txt)>1 else ''
        cand.append((typ, desc, href.group(1)))
    pick=None
    for typ,desc,h in cand:
        if typ.upper().startswith('EX-99.1'): pick=(typ,desc,h); break
    if not pick:
        for typ,desc,h in cand:
            if 'EX-99' in typ.upper(): pick=(typ,desc,h); break
    manifest[date]={'acc':acc,'cands':cand,'pick':pick}
    print(date, acc, pick[0] if pick else 'NONE', pick[2].split('/')[-1] if pick else '')

json.dump(manifest, open(os.path.join(D,'manifest2.json'),'w'), indent=1)
