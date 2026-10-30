from fetch_core import *
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
out = open("form4_table.txt","w",encoding="utf-8")
for acc in ["0002127293-26-000008","0001855778-26-000007","0001855767-26-000018","0002127293-26-000006","0001855778-26-000006","0001855764-26-000010","0002143377-26-000003","0001543401-26-000006"]:
    a = acc.replace("-","")
    try:
        x = get(f"https://www.sec.gov/Archives/edgar/data/1734722/{a}/primarydocument.xml")
    except Exception as e:
        print("ERR", acc, e); continue
    name = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", x).group(1)
    for t in re.findall(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>", x, re.S):
        d = re.search(r"<transactionDate>\s*<value>(.*?)</value>", t, re.S).group(1)
        c = re.search(r"<transactionCode>(.*?)</transactionCode>", t).group(1)
        sh = re.search(r"<transactionShares>\s*<value>(.*?)</value>", t, re.S).group(1)
        p = re.search(r"<transactionPricePerShare>\s*(?:<value>(.*?)</value>)?", t, re.S)
        fn = re.findall(r"<footnote id=\"(F\d)\">(.*?)</footnote>", x, re.S)
        line = f"{acc} {name} {d} {c} {sh} {p.group(1) if p else None}"
        print(line); out.write(line+"\n")
    for fid, ftxt in re.findall(r"<footnote id=\"(F\d+)\">(.*?)</footnote>", x, re.S):
        if "range" in ftxt or "weighted" in ftxt.lower():
            s = f"   {fid}: {re.sub(chr(10),' ',ftxt)[:300]}"; print(s); out.write(s+"\n")
    time.sleep(0.3)
