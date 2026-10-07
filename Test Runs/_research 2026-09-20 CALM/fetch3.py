import os, json, urllib.request
R = "Test Runs/_research 2026-09-20 CALM"
UA = {"User-Agent": "BRK research chrehor36@gmail.com"}
p = R + "/companyfacts.json"
if not os.path.exists(p):
    req = urllib.request.Request("https://data.sec.gov/api/xbrl/companyfacts/CIK0000016160.json", headers=UA)
    open(p,'wb').write(urllib.request.urlopen(req, timeout=180).read())
cf = json.load(open(p))
us = cf["facts"]["us-gaap"]
print("n tags:", len(us))
import re
for k in sorted(us):
    if re.search(r'ShareBased|StockBased|Compensation', k):
        print("SBC-ish:", k, list(us[k]["units"]))
