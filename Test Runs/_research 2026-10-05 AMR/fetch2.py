import sys, urllib.request, re, html, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    for k in range(4):
        try: return urllib.request.urlopen(req,timeout=90).read()
        except Exception as e: print('retry',e); time.sleep(3)
    raise SystemExit('fail '+url)
def cell(s):
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s).replace('\xa0',' ')
    return re.sub(r'\s+',' ',s).strip()
def totext(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>','',s)
    def tab(m):
        out=[]
        for tr in re.findall(r'(?is)<tr.*?</tr>',m.group(0)):
            cells=[cell(c) for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',tr)]
            cells=[c for c in cells if c not in ('','$',')','%',')%')]
            if cells: out.append(' | '.join(cells))
        return '\n[TABLE]\n'+'\n'.join(out)+'\n[/TABLE]\n'
    s=re.sub(r'(?is)<table.*?</table>',tab,s)
    s=re.sub(r'(?i)</(p|div|br|h\d|li)>','\n',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    return s
cik=os.environ.get('CIK','1704715')
for arg in sys.argv[1:]:
    name,acc,doc=arg.split(',')
    if os.path.exists(name): print('have',name); continue
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    t=totext(get(url))
    open(name,'w',encoding='utf-8').write(f'SOURCE {url}\nACCESSION {acc}\n'+t)
    print(name,len(t)); time.sleep(0.3)
