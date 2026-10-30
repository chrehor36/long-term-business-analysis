import json, urllib.request, time, re, html
UA={"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
sub=json.loads(get("https://data.sec.gov/submissions/CIK0001395942.json")); r=sub["filings"]["recent"]
q=[x for x in zip(r["form"],r["accessionNumber"],r["primaryDocument"],r["reportDate"],r["filingDate"]) if x[0]=="10-Q"][0]; print(q)
b=get(f"https://www.sec.gov/Archives/edgar/data/1395942/{q[1].replace('-','')}/{q[2]}").decode("utf-8","ignore")
t=re.sub(r"<[^>]+>"," ",b); t=html.unescape(t); t=re.sub(r"[ \t\xa0]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
open("peer_OPLN_10Q_latest.txt","w",encoding="utf-8").write(t)
