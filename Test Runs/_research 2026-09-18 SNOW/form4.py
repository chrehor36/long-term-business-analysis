import re, os
from fetch_core import *
for acc, doc in [("0001821737-26-000014","wk-form4_1789605493.xml"),("0002127025-26-000007","wk-form4_1789605465.xml"),("0001979088-26-000019","wk-form4_1789429822.xml"),("0001640147-26-000038","wk-form4_1789086839.xml")]:
    a = acc.replace("-", "")
    x = get(f"https://www.sec.gov/Archives/edgar/data/1640147/{a}/{doc}")
    open(f"form4_{acc}.xml","w",encoding="utf-8").write(x)
    name = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", x)
    print(acc, name.group(1) if name else "")
    for t in re.findall(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>", x, re.S):
        d = re.search(r"<transactionDate>\s*<value>(.*?)</value>", t, re.S)
        c = re.search(r"<transactionCode>(.*?)</transactionCode>", t)
        s = re.search(r"<transactionShares>\s*<value>(.*?)</value>", t, re.S)
        p = re.search(r"<transactionPricePerShare>\s*<value>(.*?)</value>", t, re.S)
        print("  ", d and d.group(1), c and c.group(1), s and s.group(1), p and p.group(1))
    fn = re.findall(r'<footnote id="(F\d+)">(.*?)</footnote>', x, re.S)
    for i, f in fn[:4]: print("   ", i, f[:300].replace("\n"," "))
