import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_core import *
cache = os.path.join(sources.CACHE, "sov_USD_treasury.csv")
if os.path.exists(cache): os.remove(cache)
print("SOV", sources.sovereign("USD"))
print("CIK", sources.cik_for("EQIX"))
for name, url in [("submissions.json", "https://data.sec.gov/submissions/CIK0001101239.json"),
                  ("companyfacts.json", "https://data.sec.gov/api/xbrl/companyfacts/CIK0001101239.json")]:
    open(os.path.join(HERE, name), "w", encoding="utf-8").write(get(url)); print("got", name)
print("PRICE", sources.price("EQIX"))
print("DEALS", sources.deal_filings("0001101239"))
