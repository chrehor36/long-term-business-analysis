import json, time, urllib.request, os

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
UA = "BRK-Framework research chrehor36@gmail.com"

resolved = json.load(open(os.path.join(SCRATCH, "sp500_2013_resolved_ciks.json")))

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

ok, fail = 0, 0
fails = []
for i, (t, cik) in enumerate(resolved.items()):
    fn = os.path.join(CACHE, f"facts_{t}.json")
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        ok += 1
        continue
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json"
    try:
        data = fetch(url)
        open(fn, "wb").write(data)
        ok += 1
        if i % 25 == 0:
            print(f"[{i}/{len(resolved)}] {t} OK")
    except Exception as e:
        fail += 1
        fails.append((t, str(e)))
    time.sleep(0.15)

print(f"DONE: ok={ok} fail={fail}")
print("failures:", fails)
json.dump(fails, open(os.path.join(SCRATCH, "sp500_2013_fetch_fails.json"), "w"))
