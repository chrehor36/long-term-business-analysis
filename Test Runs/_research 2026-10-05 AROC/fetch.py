import sys, re, urllib.request, html, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=60).read()
def clean(s):
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s).replace('\xa0',' ').replace('​','')
    return re.sub(r'\s+',' ',s).strip()
def row(m):
    cells=re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',m.group(0))
    cells=[clean(c) for c in cells]; cells=[c for c in cells if c not in ('','$','%',')')]
    return "\n"+" | ".join(cells)+"\n"
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>','',s)
    s=re.sub(r'(?is)<tr[^>]*>.*?</tr>',row,s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>',"\n",s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ').replace('​','')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
cik=sys.argv[1]; acc=sys.argv[2]; doc=sys.argv[3]; out=sys.argv[4]
url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
cache=os.path.join(os.path.dirname(out),'raw_'+os.path.basename(out).replace('.txt','.htm'))
if os.path.exists(cache): b=open(cache,'rb').read()
else:
    b=get(url); open(cache,'wb').write(b)
t=totext(b)
open(out,'w',encoding='utf-8').write(f"SOURCE: {url}\nACCESSION: {acc}\n\n"+t)
print(out,len(t))
