from fetch_core import *
import re
for acc in ["0001437749-26-029607", "0001437749-26-029604", "0001437749-26-029103"]:
    names = [n for n in exhibits(acc) if n.endswith(".xml") and "rdgdoc" in n or n.endswith(".xml") and "form4" in n.lower()]
    for n in exhibits(acc):
        if n.endswith(".xml") and not n.startswith("Financial") and "Filing" not in n:
            a = acc.replace("-", "")
            t = get(f"https://www.sec.gov/Archives/edgar/data/1653909/{a}/{n}")
            owner = re.findall(r"<rptOwnerName>(.*?)</rptOwnerName>", t)
            rel = re.findall(r"<officerTitle>(.*?)</officerTitle>", t)
            rows = re.findall(r"<nonDerivativeTransaction>.*?</nonDerivativeTransaction>", t, re.S)
            print(acc, n, owner, rel)
            for r in rows:
                g = lambda k: (re.search(rf"<{k}>\s*(?:<value>)?(.*?)(?:</value>)?\s*</{k}>", r, re.S) or [None, ""])[1]
                print("   ", g("transactionDate"), "code", g("transactionCode"), "shares", g("transactionShares"), "price", g("transactionPricePerShare"), "A/D", g("transactionAcquiredDisposedCode"), "after", g("sharesOwnedFollowingTransaction"))
            time.sleep(0.3)
