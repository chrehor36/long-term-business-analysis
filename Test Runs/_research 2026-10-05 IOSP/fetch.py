import sys, re, html, urllib.request, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=60).read()
def totext(b):
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>','\n',t)
    t=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',t)
    t=re.sub(r'(?i)</t[dh]>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t
if __name__=='__main__':
  for arg in sys.argv[1:]:
    acc,doc,out=arg.split(',')
    url=f"https://www.sec.gov/Archives/edgar/data/1054905/{acc.replace('-','')}/{doc}"
    b=get(url); open(out,'w',encoding='utf-8').write(totext(b)); print(out,len(b)); time.sleep(0.3)
