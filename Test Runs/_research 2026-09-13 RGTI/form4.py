import sys, os, json, re, time, urllib.request
sys.path.insert(0, "tools"); import sources
OUT="Test Runs/_research 2026-09-13 RGTI"
d=json.load(open(os.path.join(OUT,"submissions_RGTI.json")))
r=d["filings"]["recent"]
rows=[]
for i in range(len(r["form"])):
    if r["form"][i]=="4" and r["filingDate"][i]>="2025-01-01":
        rows.append((r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]))
print(len(rows),"form 4s since 2025")
agg={}
lines=[]
for fd,acc,doc in rows:
    a=acc.replace("-","")
    xmlname=doc.split("/")[-1]
    url=f"https://www.sec.gov/Archives/edgar/data/1838359/{a}/{xmlname}"
    try:
        x=urllib.request.urlopen(urllib.request.Request(url,headers=sources.SEC_UA),timeout=60).read().decode("utf-8","replace")
    except Exception as e:
        print("fail",acc,e); continue
    name=re.search(r"<rptOwnerName>(.*?)</rptOwnerName>",x)
    name=name.group(1) if name else "?"
    for t in re.findall(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>",x,re.S):
        code=re.search(r"<transactionCode>(.*?)</transactionCode>",t)
        sh=re.search(r"<transactionShares>\s*<value>(.*?)</value>",t,re.S)
        px=re.search(r"<transactionPricePerShare>\s*<value>(.*?)</value>",t,re.S)
        dt=re.search(r"<transactionDate>\s*<value>(.*?)</value>",t,re.S)
        c=code.group(1) if code else "?"; s=float(sh.group(1)) if sh else 0; p=float(px.group(1)) if px else 0
        k=(name,c); v=agg.get(k,[0,0]); v[0]+=s; v[1]+=s*p; agg[k]=v
        lines.append(f"{fd} {name} {c} {s:,.0f} @ {p} {dt.group(1) if dt else ''}")
    time.sleep(0.15)
open(os.path.join(OUT,"form4_2025-2026.txt"),"w").write("\n".join(lines))
for k,v in sorted(agg.items()): print(k, f"{v[0]:,.0f} shares ${v[1]/1e6:,.2f}M")
