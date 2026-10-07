import sys,re,urllib.request,html,time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    req=urllib.request.Request(url,headers=UA); return urllib.request.urlopen(req).read().decode('utf-8','replace')
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
    h=re.sub(r'(?i)<ix:header>.*?</ix:header>','',h,flags=re.S)
    h=re.sub(r'(?i)</(p|div|tr|br|h\d|li)>','\n',h); h=re.sub(r'(?i)<br\s*/?>','\n',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'<[^>]+>','',h); h=html.unescape(h)
    h=re.sub(r'[ \t\xa0]+',' ',h); h=re.sub(r'\n\s*\n+','\n',h)
    return h
for arg in sys.argv[1:]:
    acc,doc,out,cik=(arg.split(",")+["890564"])[:4]
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    t=totext(get(url)); open(out,'w',encoding='utf-8').write(t); print(out,len(t)); time.sleep(0.3)
