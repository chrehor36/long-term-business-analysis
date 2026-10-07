import sys, os
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources, urllib.request, datetime
url = sources.USD_TREASURY.format(yr=2026)
print(datetime.datetime.now().isoformat(), url)
req = urllib.request.Request(url, headers=sources.WEB_UA)
t = urllib.request.urlopen(req, timeout=60).read().decode()
rows = t.strip().split("\n")
print(rows[0]); print(rows[1]); print(rows[2])
