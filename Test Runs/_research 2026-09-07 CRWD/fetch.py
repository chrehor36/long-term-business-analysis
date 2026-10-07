import sys, os, re, json, urllib.request, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
OUT=os.path.dirname(os.path.abspath(__file__))
def get(url, binary=False):
    return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read()
def strip(h):
    h=h.decode('utf-8','replace')
    h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h)
    h=re.sub(r'(?is)<br\s*/?>','\n',h)
    h=re.sub(r'(?is)</(p|div|tr|h1|h2|h3|h4|li|table)>','\n',h)
    h=re.sub(r'(?is)</t[dh]>','\t',h)
    h=re.sub(r'(?is)<[^>]+>',' ',h)
    h=html.unescape(h)
    h=re.sub(r'[ \u00a0]+',' ',h)
    h=re.sub(r'\n[ \t]+','\n',h)
    h=re.sub(r'\n{3,}','\n\n',h)
    return h
if __name__=='__main__':
    cik, acc, doc, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    a=acc.replace('-','')
    url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    raw=get(url)
    p=os.path.join(OUT,name)
    open(p,'w',encoding='utf-8').write(strip(raw))
    print(p, os.path.getsize(p))
