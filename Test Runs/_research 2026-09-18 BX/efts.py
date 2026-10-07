import json, sys, urllib.parse
from fetch_core import *
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
q = sys.argv[1]; forms = sys.argv[2] if len(sys.argv)>2 else ""
url = "https://efts.sec.gov/LATEST/search-index?q=" + urllib.parse.quote(q) + ("&forms="+forms if forms else "") + "&dateRange=custom&startdt=2025-01-01&enddt=2026-09-18"
d = json.loads(get(url))
print(d["hits"]["total"])
for h in d["hits"]["hits"][:40]:
    s = h["_source"]; print(s.get("file_date"), s.get("form"), s.get("display_names"), h["_id"])
