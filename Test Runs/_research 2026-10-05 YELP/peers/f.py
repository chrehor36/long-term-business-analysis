import sys,urllib.request,re,html,time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def totext(b):
    s=b.decode('utf-8','ignore');s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s);s=re.sub(r'(?i)</td>',' | ',s)
    s=re.sub(r'<[^>]+>','',s);s=html.unescape(s);s=re.sub(r'[ \t\xa0]+',' ',s);return re.sub(r'\n\s*\n+','\n',s)
for a in sys.argv[1:]:
    cik,acc,doc,name=a.split(',')
    u=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
    t=totext(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read());open(name,'w',encoding='utf-8').write(t);print(name,len(t));time.sleep(0.3)
