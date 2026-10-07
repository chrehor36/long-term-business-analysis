import sys, re, json
from fetch_core import *
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for acc in sys.argv[1:]:
    names = exhibits(acc)
    x = [n for n in names if n.endswith(".xml")][0]
    raw = get(f"https://www.sec.gov/Archives/edgar/data/1849635/{acc.replace('-','')}/{x}")
    open(os.path.join(HERE, "form4_"+acc+".xml"), "w", encoding="utf-8").write(raw)
    nm = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", raw); tt = re.search(r"<officerTitle>(.*?)</officerTitle>", raw)
    print(acc, nm and nm.group(1), tt and tt.group(1))
    for t in re.findall(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>", raw, re.S):
        g = lambda k: (re.search(r"<"+k+r">\s*(?:<value>)?([^<]*)", t) or [None,None])[1]
        print("  ", g("transactionDate"), g("transactionCode"), g("transactionShares"), g("transactionPricePerShare"), g("transactionAcquiredDisposedCode"))
    fn = re.findall(r"<footnote id=\"(F\d)\">(.*?)</footnote>", raw, re.S)
    for f in fn: print("   ", f[0], f[1][:300])
