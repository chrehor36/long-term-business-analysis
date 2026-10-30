"""List the documents behind an fts_count screen hit (so they can be opened). Uses the same
endpoint and User-Agent as tools/sources.py:fts_count; the count itself came from fts_count."""
import json, sys, urllib.parse, urllib.request
FTS = "https://efts.sec.gov/LATEST/search-index"
def hits(phrase, cik, forms):
    q = urllib.parse.urlencode({"q": '"%s"' % phrase, "forms": forms, "ciks": cik})
    r = urllib.request.urlopen(urllib.request.Request(FTS + "?" + q, headers={
        "User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept": "application/json"}), timeout=60)
    for h in json.loads(r.read())["hits"]["hits"]:
        s = h["_source"]
        print(phrase, "|", s.get("form"), s.get("file_date"), s.get("period_ending"), h["_id"])
for ph, f in [("price of consoles", "10-Q"), ("price of consoles", "10-K"), ("price increase", "10-Q"), ("price increase", "10-K")]:
    hits(ph, "0000789019", f)
