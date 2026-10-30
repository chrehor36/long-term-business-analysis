import sys,re,html,urllib.request,time,os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(acc,doc,out):
    cikacc=acc.replace('-','')
    url=f"https://www.sec.gov/Archives/edgar/data/1243429/{cikacc}/{doc}"
    p='cache/'+out
    if not os.path.exists(p+'.htm'):
        raw=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read()
        open(p+'.htm','wb').write(raw); time.sleep(0.3)
    raw=open(p+'.htm','rb').read()
    try: t=raw.decode('utf-8')
    except: t=raw.decode('cp1252',errors='replace')
    t=re.sub(r'(?is)<ix:header>.*?</ix:header>','',t)
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(p+'.txt','w',encoding='utf-8').write(t); print(out,len(t))
for a in sys.argv[1:]:
    acc,doc,out=a.split(',')
    get(acc,doc,out)
