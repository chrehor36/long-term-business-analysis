import urllib.request, re, html, os, sys, time
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def totext(h):
    h=re.sub(r'(?is)<(script|style).*?</\1>','',h)
    h=re.sub(r'(?is)<ix:header>.*?</ix:header>','',h)
    h=re.sub(r'(?i)</(p|div|tr|br|li|h\d|table)>','\n',h)
    h=re.sub(r'(?i)<br\s*/?>','\n',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h).replace('\xa0',' ')
    h=re.sub(r'[ \t]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
for line in sys.argv[1:]:
    cik,acc,doc,name=line.split(",")
    out=name+".txt"
    if os.path.exists(out): print("have",out); continue
    url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    h=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read().decode("utf-8","replace")
    open(out,"w",encoding="utf-8").write(f"SOURCE {url}\nACCESSION {acc}\n"+totext(h))
    print("wrote",out,len(h)); time.sleep(0.5)
