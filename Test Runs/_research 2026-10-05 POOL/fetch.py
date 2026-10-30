import sys, re, html, urllib.request, time, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=60).read()
def totext(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
# args: cik accession(with dashes) doc outname
cik,acc,doc,out=sys.argv[1:5]
url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
b=get(url)
open(out,'w',encoding='utf-8').write(totext(b))
print(out, len(b))
