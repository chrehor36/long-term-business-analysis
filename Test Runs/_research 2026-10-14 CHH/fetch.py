import sys, os, re, time, urllib.request, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    for i in range(5):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e:
            print('retry',e); time.sleep(3)
    raise SystemExit('fail '+url)
def strip(b):
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t)
    t=re.sub(r'(?i)<ix:header>.*?</ix:header>',' ',t,flags=re.S)
    t=re.sub(r'(?i)</(p|div|tr|br|h\d|li|table)>','\n',t)
    t=re.sub(r'(?i)<br\s*/?>','\n',t)
    t=re.sub(r'(?i)</t[dh]>',' | ',t)
    t=re.sub(r'<[^>]+>',' ',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t
cik='1046311'
for arg in sys.argv[1:]:
    name,acc,doc=arg.split(',')
    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
    out=f'cache/{name}.txt'
    if os.path.exists(out): continue
    b=get(url); open(out,'w',encoding='utf-8').write(strip(b)); print(name,len(b)); time.sleep(0.3)
