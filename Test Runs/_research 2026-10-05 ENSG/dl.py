import sys, urllib.request, re, html, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(acc,doc,out,cik="1125376"):
    url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    raw=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=90).read().decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',raw)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>|</th>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(out,'w',encoding='utf-8').write(f"SOURCE {url}\nACCESSION {acc}\n"+t)
    print(out,len(t)); time.sleep(0.3)
for a in sys.argv[1:]:
    p=a.split(","); acc,doc,out=p[:3]; cik=p[3] if len(p)>3 else "1125376"
    get(acc,doc,out,cik)
