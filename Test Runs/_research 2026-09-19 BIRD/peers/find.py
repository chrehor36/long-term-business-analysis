import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from fetch_core import get
j = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
for v in j.values():
    if v["ticker"] in ("CRWV", "APLD", "NBIS", "IREN", "WULF", "CIFR", "GLXY", "HUT", "QMLS", "NVDA") or "qumulus" in v["title"].lower() or "lambda" in v["title"].lower():
        print(v)
