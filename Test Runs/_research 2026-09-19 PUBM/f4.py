from fetch_core import *
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
out = open("form4_table.txt","w",encoding="utf-8")
L=[l.split() for l in open("filings_list.txt")]
for x in L:
    if x[1] != "4" or x[0] < "2026-08-01": continue
    acc, doc = x[2], x[3].split("/")[-1]
    a = acc.replace("-","")
    try:
        xx = get(f"https://www.sec.gov/Archives/edgar/data/1422930/{a}/{doc}")
    except Exception as e:
        print("ERR", acc, e); continue
    name = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", xx).group(1)
    for t in re.findall(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>", xx, re.S):
        d = re.search(r"<transactionDate>\s*<value>(.*?)</value>", t, re.S).group(1)
        c = re.search(r"<transactionCode>(.*?)</transactionCode>", t).group(1)
        sh = re.search(r"<transactionShares>\s*<value>(.*?)</value>", t, re.S).group(1)
        p = re.search(r"<transactionPricePerShare>\s*(?:<value>(.*?)</value>)?", t, re.S)
        line = f"{x[0]} {acc} {name} {d} {c} {sh} {p.group(1) if p else None}"
        print(line); out.write(line+"\n")
    for fid, ftxt in re.findall(r"<footnote id=\"(F\d+)\">(.*?)</footnote>", xx, re.S):
        if "range" in ftxt or "weighted" in ftxt.lower():
            s = f"   {fid}: {re.sub(chr(10),' ',ftxt)[:300]}"; print(s); out.write(s+"\n")
    time.sleep(0.3)
