import sys,re,html,urllib.request,time,os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=120).read()
def totext(b):
    s=b.decode('utf-8',errors='replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</li>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>|</th>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
cik='1267565'
for spec in sys.argv[1:]:
    acc,doc,name=spec.split(',')
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    if os.path.exists(name): print('have',name); continue
    t=totext(get(url)); open(name,'w',encoding='utf-8').write(t); print(name,len(t)); time.sleep(0.3)
