import sys,re,html,urllib.request,time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(acc,doc,out):
    cik='1624794'
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    if acc.startswith('http'): url=acc
    t=urllib.request.urlopen(urllib.request.Request(url,headers=UA)).read().decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>','\n',t)
    t=re.sub(r'(?i)</td>',' | ',t)
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(out,'w',encoding='utf-8').write(f'SOURCE {url}\n'+t); print(out,len(t)); time.sleep(0.3)
for a in sys.argv[1:]:
    acc,doc,out=a.split(',')
    get(acc,doc,out)
