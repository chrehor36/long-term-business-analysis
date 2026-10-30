import json, sys, os, re, time, urllib.request, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
here=os.path.dirname(os.path.abspath(__file__)); cache=os.path.join(here,"cache")
d=json.load(open(os.path.join(cache,"sub.json")))
r=d['filings']['recent']
want=set(sys.argv[1:])
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
    h=re.sub(r'(?i)<br\s*/?>','\n',h)
    h=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h); h=re.sub(r'\n\s*\n+','\n',h)
    return h
for i in range(len(r['form'])):
    acc=r['accessionNumber'][i]
    if acc not in want: continue
    doc=r['primaryDocument'][i]
    url=f"https://www.sec.gov/Archives/edgar/data/2031009/{acc.replace('-','')}/{doc}"
    out=os.path.join(cache,f"{r['filingDate'][i]}_{r['form'][i].replace('/','-')}_{acc}.txt")
    if os.path.exists(out): print('have',out); continue
    req=urllib.request.Request(url,headers=UA)
    h=urllib.request.urlopen(req,timeout=60).read().decode('utf-8','replace')
    open(out,'w',encoding='utf-8').write(totext(h)); print('wrote',out,len(h)); time.sleep(0.3)
