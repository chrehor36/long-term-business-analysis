import json, time, urllib.request, os

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")

UNIVERSE = ["HPQ","LEN","CTSH","DHI","PHM","IT","UHS","NVR","HON","APA","ZTS","VZ",
"HCA","CMCSA","EOG","TROW","TSCO","LULU","ELV","COP","PYPL","UPS","REGN","GEHC",
"LOW","DVN","ADBE","BLDR","BBY","FDX","CDW","CHTR","SWKS","HD","MU","TXN","SPY"]

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

# period1 = 2011-01-01, period2 = now
p1 = 1293840000
p2 = 1800000000

for t in UNIVERSE:
    fn = os.path.join(CACHE, f"px_{t}.json")
    if os.path.exists(fn) and os.path.getsize(fn) > 500:
        continue
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1={p1}&period2={p2}&interval=1d&events=div,split"
    try:
        data = fetch(url)
        open(fn, "wb").write(data)
        d = json.loads(data)
        n = len(d["chart"]["result"][0]["timestamp"])
        print(t, "OK", n, "bars")
    except Exception as e:
        print(t, "FAIL", e)
    time.sleep(0.3)
