# fetch helper for the LOW run: EDGAR only, raw files into cache/ (gitignored)
import sys, os, json, time, urllib.request, re, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
HERE=os.path.dirname(os.path.abspath(__file__)); C=os.path.join(HERE,"cache")
def get(url,dest=None):
    p=os.path.join(C,dest) if dest else None
    if p and os.path.exists(p): return open(p,"rb").read()
    for i in range(4):
        try:
            b=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read(); break
        except Exception as e:
            err=e; time.sleep(2*(i+1))
    else: raise err
    if p: open(p,"wb").write(b)
    time.sleep(0.25); return b
def text(b):
    s=b.decode("utf-8","replace")
    s=re.sub(r"(?is)<(script|style).*?</\1>"," ",s)
    s=re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>","\n",s)
    s=re.sub(r"(?i)</td>|</th>"," | ",s)
    s=re.sub(r"<[^>]+>"," ",s); s=html.unescape(s)
    s=re.sub(r"[ \t\xa0]+"," ",s); s=re.sub(r"\n\s*\n+","\n",s)
    return s
def subs(cik):
    j=json.loads(get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json",f"sub_{cik}.json"))
    rows=[]
    r=j["filings"]["recent"]
    for i in range(len(r["form"])): rows.append((r["form"][i],r["filingDate"][i],r["accessionNumber"][i],r["primaryDocument"][i],r["reportDate"][i]))
    for f in j["filings"].get("files",[]):
        jj=json.loads(get("https://data.sec.gov/submissions/"+f["name"],f["name"]))
        for i in range(len(jj["form"])): rows.append((jj["form"][i],jj["filingDate"][i],jj["accessionNumber"][i],jj["primaryDocument"][i],jj["reportDate"][i]))
    return rows
def doc(cik,acc,prim,name):
    url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{prim}"
    b=get(url,name+".htm"); t=text(b)
    open(os.path.join(C,name+".txt"),"w",encoding="utf-8").write(t); return t
if __name__=="__main__":
    cik=sys.argv[1]; forms=sys.argv[2].split(",")
    for row in subs(cik):
        if row[0] in forms: print(*row,sep=" | ")
