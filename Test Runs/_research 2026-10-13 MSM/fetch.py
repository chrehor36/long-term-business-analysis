import sys, re, html, urllib.request, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e:
            print('retry',e); time.sleep(3)
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<ix:header>.*?</ix:header>','',s,flags=re.S)
    s=re.sub(r'(?i)</(p|div|tr|br|h\d|li)>','\n',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</td>','\t',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
cik=sys.argv[1]; acc=sys.argv[2]; doc=sys.argv[3]; out=sys.argv[4]
url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
b=get(url)
open('cache/'+out+'.txt','w',encoding='utf-8').write(totext(b))
print(out, len(b))
