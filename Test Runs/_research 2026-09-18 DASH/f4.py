from fetch_core import *
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
L=[l.split() for l in open("filings_list.txt") if l.split()[1]=="4"][:6]
out=[]
for x in L:
    a=x[2].replace("-","")
    doc=x[3].split("/")[-1]
    raw=get(f"https://www.sec.gov/Archives/edgar/data/1792789/{a}/{doc}")
    name=re.search(r"<rptOwnerName>(.*?)</rptOwnerName>",raw).group(1)
    for t in re.findall(r"<nonDerivativeTransaction>.*?</nonDerivativeTransaction>",raw,re.S):
        d=re.search(r"<transactionDate>\s*<value>(.*?)</value>",t,re.S).group(1)
        c=re.search(r"<transactionCode>(.*?)</transactionCode>",t).group(1)
        sh=re.search(r"<transactionShares>\s*<value>(.*?)</value>",t,re.S).group(1)
        p=re.search(r"<transactionPricePerShare>\s*(?:<value>(.*?)</value>)?",t,re.S)
        out.append(f"{x[2]} {name} {d} code={c} shares={sh} price={p.group(1) if p else None}")
    time.sleep(0.3)
open("form4_table.txt","w").write("\n".join(out)); print("\n".join(out))
