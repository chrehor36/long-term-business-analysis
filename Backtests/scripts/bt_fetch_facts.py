import json, time, urllib.request, os, sys

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
UA = "BRK-Framework research chrehor36@gmail.com"

UNIVERSE = ["HPQ","LEN","CTSH","DHI","PHM","IT","UHS","NVR","HON","APA","ZTS","VZ",
"HCA","CMCSA","EOG","TROW","TSCO","LULU","ELV","COP","PYPL","UPS","REGN","GEHC",
"LOW","DVN","ADBE","BLDR","BBY","FDX","CDW","CHTR","SWKS","HD","MU","TXN","SPY"]

tickers_map = json.load(open(os.path.join(SCRATCH, "company_tickers.json")))
tk2cik = {}
for v in tickers_map.values():
    tk2cik[v["ticker"].upper()] = v["cik_str"]

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

missing = []
for t in UNIVERSE:
    if t == "SPY":
        continue
    cik = tk2cik.get(t)
    if not cik:
        missing.append(t)
        continue
    fn = os.path.join(CACHE, f"facts_{t}.json")
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        continue
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    try:
        data = fetch(url)
        open(fn, "wb").write(data)
        print(t, cik, len(data), "OK")
    except Exception as e:
        print(t, cik, "FAIL", e)
    time.sleep(0.25)

print("MISSING CIK:", missing)
