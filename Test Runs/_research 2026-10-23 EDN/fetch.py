import sys, urllib.request, re, html, os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(acc, doc, out):
    cik="1395213"; a=acc.replace("-","")
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}"
    raw=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read().decode("utf-8","replace")
    t=re.sub(r"(?is)<(script|style).*?</\1>","",raw); t=re.sub(r"\s+"," ",t)
    t=re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>","\n",t)
    t=re.sub(r"(?i)</td>|</th>"," | ",t); t=re.sub(r"\|(\s*\|)+","|",t)
    t=re.sub(r"<[^>]+>","",t); t=html.unescape(t).replace("\xa0"," ")
    t=re.sub(r"[ \t]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
    open(out,"w",encoding="utf-8").write(t); print(out,len(t))
for arg in sys.argv[1:]:
    acc,doc,out=arg.split(",")
    get(acc,doc,os.path.join("cache",out))
