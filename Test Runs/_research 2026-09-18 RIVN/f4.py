from fetch_core import *
import re
for acc, doc in [("0001262742-26-000014","wk-form4_1789552810.xml"),("0001890925-26-000025","wk-form4_1787361845.xml")]:
    a = acc.replace("-","")
    t = get(f"https://www.sec.gov/Archives/edgar/data/1874178/{a}/{doc}")
    open(os.path.join(HERE, f"form4_{acc}.xml"),"w",encoding="utf-8").write(t)
    name = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", t)
    print(acc, name.group(1) if name else "")
    for m in re.finditer(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>", t, re.S):
        b = m.group(1)
        g = lambda k: (re.search(rf"<{k}>\s*(?:<value>)?(.*?)(?:</value>)?\s*</{k}>", b, re.S) or [None,""])[1]
        print("  ", g("transactionDate"), g("transactionCode"), g("transactionShares"), g("transactionPricePerShare"), g("sharesOwnedFollowingTransaction"))
    fn = re.findall(r'<footnote id="(F\d)">(.*?)</footnote>', t, re.S)
    for f in fn: print("   ", f[0], f[1][:300])
