import urllib.request, re, sys, html, os
UA={"User-Agent":"BRK research chrehor36@gmail.com"}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
def totext(b):
    s=b.decode("utf-8","ignore")
    s=re.sub(r"(?is)<(script|style|ix:header)[^>]*>.*?</\1>"," ",s)
    s=re.sub(r"(?i)<br[^>]*>","\n",s)
    s=re.sub(r"(?i)</(p|div|tr|h[1-6]|li)>","\n",s)
    s=re.sub(r"(?i)</t[dh]>"," | ",s)
    s=re.sub(r"<[^>]+>"," ",s)
    s=html.unescape(s)
    s=re.sub(r"[ \t\u00a0]+"," ",s)
    s=re.sub(r"\n\s*\n+","\n",s)
    return s
if __name__=="__main__":
    url, out = sys.argv[1], sys.argv[2]
    b=get(url)
    open(out+".raw","wb").write(b)
    t=totext(b)
    open(out,"w",encoding="utf-8").write(t)
    print(out, len(b), len(t))
