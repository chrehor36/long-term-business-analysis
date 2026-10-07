"""List the documents in EDGAR filings. usage: python -I idx.py accession [...]"""
import sys, time, json, urllib.request

UA = "LongTermBusinessAnalysis research chrehor36@gmail.com"
for acc in sys.argv[1:]:
    url = f"https://www.sec.gov/Archives/edgar/data/1018724/{acc.replace('-', '')}/index.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    d = json.load(urllib.request.urlopen(req, timeout=60))
    print(acc, [i["name"] for i in d["directory"]["item"]])
    time.sleep(0.4)
