import json, re, time, urllib.request, sys
sys.stdout.reconfigure(encoding="utf-8")
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
d = json.load(open("cache/sub.json")); r = d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] != "4" or r["filingDate"][i] < "2026-05-01": continue
    acc = r["accessionNumber"][i].replace("-", ""); doc = r["primaryDocument"][i].split("/")[-1]
    t = urllib.request.urlopen(urllib.request.Request(f"https://www.sec.gov/Archives/edgar/data/1693736/{acc}/{doc}", headers=UA)).read().decode("utf-8", "ignore")
    name = re.search(r"<rptOwnerName>(.*?)</rptOwnerName>", t, re.S)
    title = re.search(r"<officerTitle>(.*?)</officerTitle>", t, re.S)
    txs = re.findall(r"<nonDerivativeTransaction>(.*?)</nonDerivativeTransaction>", t, re.S)
    out = []
    for x in txs:
        code = re.search(r"<transactionCode>(.*?)</transactionCode>", x); sh = re.search(r"<transactionShares>\s*<value>(.*?)</value>", x, re.S)
        px = re.search(r"<transactionPricePerShare>\s*<value>(.*?)</value>", x, re.S); ad = re.search(r"<transactionAcquiredDisposedCode>\s*<value>(.*?)</value>", x, re.S)
        out.append((code.group(1) if code else "", sh.group(1) if sh else "", px.group(1) if px else "", ad.group(1) if ad else ""))
    print(r["filingDate"][i], r["accessionNumber"][i], name.group(1).strip() if name else "?", (title.group(1).strip() if title else ""), out[:5])
    time.sleep(0.25)
