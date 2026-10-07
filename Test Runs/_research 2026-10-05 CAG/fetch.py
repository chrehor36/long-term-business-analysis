import sys, urllib.request, re, html, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(cik, acc, doc, out):
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    raw=urllib.request.urlopen(urllib.request.Request(url,headers=UA)).read().decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',raw)
    t=re.sub(r'(?i)<br\s*/?>','\n',t)
    t=re.sub(r'(?i)</(p|div|tr|h\d|li|table)>','\n',t)
    t=re.sub(r'(?i)</t[dh]>',' | ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    open(out,'w',encoding='utf-8').write(t)
    print(out,len(t))
    time.sleep(0.3)
if __name__=='__main__':
    cik=sys.argv[1]
    for a in sys.argv[2:]:
        acc,doc,out=a.split(',')
        get(cik,acc,doc,out)
