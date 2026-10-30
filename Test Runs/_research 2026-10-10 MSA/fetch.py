import sys, os, time, urllib.request, gzip, json, re, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"gzip"}
def get(url):
    for i in range(5):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
            b=r.read()
            if r.headers.get("Content-Encoding")=="gzip": b=gzip.decompress(b)
            time.sleep(0.15); return b
        except Exception as e:
            print("retry",url,e,file=sys.stderr); time.sleep(2)
    raise SystemExit("fail "+url)
def text(b):
    s=b.decode("utf-8","ignore")
    s=re.sub(r"(?is)<(script|style).*?</\1>"," ",s)
    s=re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>","\n",s)
    s=re.sub(r"(?i)</td>|</th>"," | ",s)
    s=re.sub(r"<[^>]+>"," ",s); s=html.unescape(s)
    s=re.sub(r"[ \t\xa0]+"," ",s); s=re.sub(r"\n\s*\n+","\n",s)
    return s
if __name__=="__main__":
    url,out=sys.argv[1],sys.argv[2]
    b=get(url)
    if out.endswith(".txt"): open(out,"w",encoding="utf-8").write(text(b))
    else: open(out,"wb").write(b)
    print(out, len(b))
