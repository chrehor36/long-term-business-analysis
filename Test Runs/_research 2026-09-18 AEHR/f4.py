import sys, re, json
from fetch_core import *
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
rows = [l.split(" | ") for l in open("filings_list.txt", encoding="utf-8")]
out = open("form4_table.txt", "w", encoding="utf-8")
for r in rows:
    if r[1] != "4" or r[0] < "2025-06-01": continue
    acc = r[2]; a = acc.replace("-", "")
    try:
        names = exhibits(acc)
        x = [n for n in names if n.endswith(".xml")][0]
        raw = get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{x}")
    except Exception as e:
        print("FAIL", acc, e); continue
    own = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", raw).group(1)
    title = (re.search(r"<officerTitle>(.*?)</officerTitle>", raw) or re.search(r"<isDirector>(.*?)</isDirector>", raw)).group(1)
    for t in re.findall(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>", raw, re.S):
        g = lambda k: (re.search(r"<%s>.*?<value>(.*?)</value>" % k, t, re.S) or [None, ""])[1] if re.search(r"<%s>.*?<value>(.*?)</value>" % k, t, re.S) else ""
        d = re.search(r"<transactionDate>\s*<value>(.*?)</value>", t, re.S).group(1)
        code = re.search(r"<transactionCode>(.*?)</transactionCode>", t).group(1)
        sh = g("transactionShares"); px = g("transactionPricePerShare"); ad = g("transactionAcquiredDisposedCode"); post = g("sharesOwnedFollowingTransaction")
        line = f"{r[0]} {acc} {own} [{title}] {d} {code} {ad} {sh} @ {px} -> {post}"
        print(line); out.write(line + "\n")
    time.sleep(0.2)
