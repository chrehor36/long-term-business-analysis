from fetch_core import *
j = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
for v in j.values():
    if v["ticker"] in ("BIRD",) or "allbirds" in v["title"].lower():
        print(v)
