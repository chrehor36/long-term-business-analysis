import json, os, re, time, urllib.request
import xml.etree.ElementTree as ET
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
sub = json.load(open(os.path.join(HERE, "submissions.json")))
r = sub["filings"]["recent"]
out = []
for i in range(len(r["form"])):
    if r["form"][i] not in ("4", "4/A") or r["filingDate"][i] < "2025-06-01":
        continue
    acc = r["accessionNumber"][i]
    doc = r["primaryDocument"][i].split("/")[-1]
    url = f"https://www.sec.gov/Archives/edgar/data/1474627/{acc.replace('-', '')}/{doc}"
    try:
        x = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
    except Exception as e:
        print("fail", url, e); continue
    time.sleep(0.25)
    try:
        root = ET.fromstring(x)
    except Exception as e:
        print("parse fail", acc, e); continue
    owner = root.findtext(".//reportingOwnerId/rptOwnerName")
    rel = root.findtext(".//reportingOwnerRelationship/officerTitle") or ""
    for t in root.findall(".//nonDerivativeTransaction"):
        code = t.findtext(".//transactionCoding/transactionCode")
        sh = t.findtext(".//transactionAmounts/transactionShares/value")
        px = t.findtext(".//transactionAmounts/transactionPricePerShare/value")
        ad = t.findtext(".//transactionAmounts/transactionAcquiredDisposedCode/value")
        dt = t.findtext(".//transactionDate/value")
        post = t.findtext(".//postTransactionAmounts/sharesOwnedFollowingTransaction/value")
        line = f"{r['filingDate'][i]} {acc} | {owner} {rel} | {dt} code {code} {ad} {sh} @ {px} -> post {post}"
        out.append(line); print(line)
    for t in root.findall(".//derivativeTransaction"):
        code = t.findtext(".//transactionCoding/transactionCode")
        sh = t.findtext(".//transactionAmounts/transactionShares/value")
        dt = t.findtext(".//transactionDate/value")
        line = f"{r['filingDate'][i]} {acc} | {owner} | {dt} DERIV code {code} {sh}"
        out.append(line); print(line)
open(os.path.join(HERE, "form4_2025-2026.txt"), "w", encoding="utf-8").write("\n".join(out))
