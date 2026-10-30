import sys, os, re, time, urllib.request, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(url):
    for i in range(5):
        try:
            req=urllib.request.Request(url,headers=UA)
            return urllib.request.urlopen(req,timeout=60).read()
        except Exception as e:
            print("retry",e); time.sleep(2)
    raise SystemExit("fail "+url)
def strip(b):
    t=b.decode("utf-8","replace")
    t=re.sub(r"(?is)<(script|style).*?</\1>"," ",t)
    t=re.sub(r"(?i)<br\s*/?>","\n",t)
    t=re.sub(r"(?i)</(p|div|tr|li|h\d|table)>","\n",t)
    t=re.sub(r"(?i)</t[dh]>"," | ",t)
    t=re.sub(r"<[^>]+>"," ",t)
    t=html.unescape(t)
    t=re.sub(r"[ \t\xa0]+"," ",t)
    t=re.sub(r"\n\s*\n+","\n",t)
    return t
cik=sys.argv[1]; acc=sys.argv[2]; doc=sys.argv[3]; out=sys.argv[4]
url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
b=get(url)
open(os.path.join("cache",out+".htm"),"wb").write(b)
open(os.path.join("cache",out+".txt"),"w",encoding="utf-8").write(strip(b))
print(out, len(b))
time.sleep(0.3)
