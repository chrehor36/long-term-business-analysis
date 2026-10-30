import sys, time, urllib.request, re, html, os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
CIK="1720990"
def get(accn, doc, out):
    url=f"https://www.sec.gov/Archives/edgar/data/{CIK}/{accn.replace('-','')}/{doc}"
    p=os.path.join("cache",out)
    if not os.path.exists(p):
        b=urllib.request.urlopen(urllib.request.Request(url,headers=UA)).read()
        open(p,"wb").write(b); time.sleep(0.3)
    t=open(p,"rb").read().decode("utf-8","replace")
    t=re.sub(r"(?is)<(script|style).*?</\1>"," ",t)
    t=re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>","\n",t)
    t=re.sub(r"(?i)</td>"," | ",t)
    t=re.sub(r"<[^>]+>"," ",t); t=html.unescape(t)
    t=re.sub(r"[ \t\xa0]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
    open(os.path.join("cache",out+".txt"),"w",encoding="utf-8").write(t)
    print(out, len(t))
for line in sys.argv[1:]:
    accn,doc,out=line.split(",")
    get(accn,doc,out)
