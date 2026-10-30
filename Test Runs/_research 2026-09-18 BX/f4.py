import sys, re, json
from fetch_core import *
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for acc in sys.argv[1:]:
    a = acc.replace("-", "")
    idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json"))
    xs = [i["name"] for i in idx["directory"]["item"] if i["name"].endswith(".xml")]
    for x in xs:
        t = get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{x}")
        open(f"form4_{acc}.xml","w",encoding="utf-8").write(t)
        iss = re.findall(r"<issuerName>(.*?)</issuerName>", t); own = re.findall(r"<rptOwnerName>(.*?)</rptOwnerName>", t)
        print(acc, iss, own)
        for m in re.finditer(r"<nonDerivativeTransaction>.*?</nonDerivativeTransaction>", t, re.S):
            b = m.group(0)
            g = lambda k: (re.search(rf"<{k}>\s*(?:<value>)?\s*([^<]*)", b) or [None,None])[1]
            print("  ", g("transactionDate"), g("transactionCode"), g("transactionShares"), g("transactionPricePerShare"), g("transactionAcquiredDisposedCode"))
            fn = re.findall(r"<footnote id=\"(F\d)\">(.*?)</footnote>", t, re.S)
        for f in re.findall(r"<footnote id=\"(F\d+)\">(.*?)</footnote>", t, re.S)[:4]: print("   FN", f[0], f[1][:300])
