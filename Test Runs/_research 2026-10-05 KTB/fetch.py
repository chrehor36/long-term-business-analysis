import sys, urllib.request, gzip, json, re, html, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
def get(url):
    for i in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
            b=r.read()
            if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
            return b
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(2)
    raise SystemExit('fail '+url)
def text(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style|ix:header).*?</\1>','',s)
    s=re.sub(r'(?i)</t[dh]>','\x01',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>','\n',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ').replace('​','')
    out=[]
    for line in s.split('\n'):
        if '\x01' in line:
            cells=[c.strip() for c in line.split('\x01')]
            cells=[c for c in cells if c and c not in ('$','%',')')]
            line=' | '.join(cells)
        line=re.sub(r'[ \t]+',' ',line).strip()
        if line: out.append(line)
    return '\n'.join(out)
if __name__=='__main__':
    url,out=sys.argv[1],sys.argv[2]
    b=get(url)
    raw=out+'.raw.html'
    if out.endswith('.json'): open(out,'wb').write(b)
    else:
        open(raw,'wb').write(b)
        open(out,'w',encoding='utf-8').write(text(b))
    print(out, os.path.getsize(out))
