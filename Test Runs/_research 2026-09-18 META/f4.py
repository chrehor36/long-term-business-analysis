from fetch_core import *
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
out = open("form4_table.txt","w",encoding="utf-8")
for acc in ["0000950103-26-014140","0000950103-26-014061","0000950103-26-013860","0000950103-26-013794","0000950103-26-013672"]:
    names = exhibits(acc)
    xml = [n for n in names if n.endswith(".xml") and "index" not in n][0]
    raw = get(f"https://www.sec.gov/Archives/edgar/data/1326801/{acc.replace('-','')}/{xml}")
    who = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", raw).group(1)
    for tx in re.findall(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>", raw, re.S):
        d = re.search(r"<transactionDate>\s*<value>(.*?)</value>", tx, re.S).group(1)
        code = re.search(r"<transactionCode>(.*?)</transactionCode>", tx).group(1)
        sh = re.search(r"<transactionShares>\s*<value>(.*?)</value>", tx, re.S).group(1)
        p = re.search(r"<transactionPricePerShare>\s*(?:<value>(.*?)</value>)?", tx, re.S)
        line = f"{acc} | {who} | {d} | {code} | {sh} | {p.group(1) if p else None}"
        print(line); out.write(line+"\n")
