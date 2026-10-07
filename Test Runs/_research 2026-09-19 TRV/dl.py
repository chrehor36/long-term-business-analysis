import json, sys, time, urllib.request, re, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u):
    time.sleep(0.2)
    return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
def idx(acc):
    a=acc.replace('-','')
    return json.loads(get(f"https://www.sec.gov/Archives/edgar/data/86312/{a}/index.json"))['directory']['item']
def totext(b):
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    return t
if __name__=='__main__':
    acc,name=sys.argv[1],sys.argv[2]
    want=sys.argv[3] if len(sys.argv)>3 else None
    items=idx(acc)
    for it in items:
        n=it['name']
        if want and not re.search(want,n,re.I): continue
        if not want: print(n, it.get('size')); continue
        b=get(f"https://www.sec.gov/Archives/edgar/data/86312/{acc.replace('-','')}/{n}")
        open(f"{name}.txt","w",encoding="utf-8").write(totext(b))
        print("wrote",name,n,len(b))
        break
