import sys, urllib.request, gzip, json, re, html, os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"gzip"}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    b=r.read()
    if r.headers.get("Content-Encoding")=="gzip": b=gzip.decompress(b)
    return b
def text(url,out):
    b=get(url).decode("utf-8","replace")
    t=re.sub(r"(?is)<(script|style).*?</\1>","",b)
    t=re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>","\n",t)
    t=re.sub(r"(?i)</td>"," | ",t)
    t=re.sub(r"<[^>]+>","",t)
    t=html.unescape(t).replace("\xa0"," ")
    t=re.sub(r"[ \t]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
    open(out,"w",encoding="utf-8").write(t); print(out,len(t))
if __name__=="__main__":
    if sys.argv[1]=="json":
        open(sys.argv[3],"wb").write(get(sys.argv[2])); print("ok")
    else: text(sys.argv[2],sys.argv[3])
