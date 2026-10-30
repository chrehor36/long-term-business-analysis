import sys, time, json, urllib.parse, urllib.request
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
sys.stdout.reconfigure(encoding="utf-8")
# who names UiPath in a 10-K, since 2024
q = {"q": '"UiPath"', "forms": "10-K", "dateRange": "custom", "startdt": "2024-01-01", "enddt": "2026-09-18"}
url = sources.FTS_URL + "?" + urllib.parse.urlencode(q)
r = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com"}), timeout=60))
seen = {}
for h in r["hits"]["hits"]:
    s = h["_source"]; nm = s["display_names"][0]
    seen.setdefault(nm, []).append((s["file_date"], h["_id"]))
print("total", r["hits"]["total"])
for k, v in sorted(seen.items()): print(k, v[:3])
for nm, cik in [("Appian","0001441683"),("Pegasystems","0001013857"),("ServiceNow","0001373715"),("Microsoft","0000789019"),("SS&C","0001402436"),("Salesforce","0001108524")]:
    try: print(nm, sources.fts_count("UiPath", cik=cik, forms="10-K"))
    except Exception as e: print(nm, "ERR", e)
    time.sleep(0.5)
