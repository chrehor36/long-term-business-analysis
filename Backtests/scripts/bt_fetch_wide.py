import json, time, urllib.request, os

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
UA = "BRK-Framework research chrehor36@gmail.com"

wide = json.load(open(os.path.join(SCRATCH, "wide_universe.json")))
tickers = wide["tickers"]
ciks = wide["ciks"]

def fetch(url, ua=UA):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

fail_log = []
for i, t in enumerate(tickers):
    cik = ciks[t]
    fn = os.path.join(CACHE, f"facts_{t}.json")
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        print(t, "cached")
        continue
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    try:
        data = fetch(url)
        open(fn, "wb").write(data)
        print(i, t, cik, len(data), "OK")
    except Exception as e:
        print(i, t, cik, "FAIL", e)
        fail_log.append((t, str(e)))
    time.sleep(0.2)

print("FAILS:", fail_log)

p1 = 1293840000
p2 = 1800000000
for t in tickers:
    fn = os.path.join(CACHE, f"px_{t}.json")
    if os.path.exists(fn) and os.path.getsize(fn) > 500:
        continue
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1={p1}&period2={p2}&interval=1d&events=div,split"
    try:
        data = fetch(url, ua="Mozilla/5.0")
        open(fn, "wb").write(data)
        d = json.loads(data)
        n = len(d["chart"]["result"][0]["timestamp"])
        print(t, "PX OK", n)
    except Exception as e:
        print(t, "PX FAIL", e)
    time.sleep(0.25)
