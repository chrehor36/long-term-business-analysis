import urllib.request, json, os, time, csv

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
UA = "Mozilla/5.0"

rows = list(csv.DictReader(open(os.path.join(SCRATCH, "sfd_master.csv"))))
tickers = sorted(set(r["ticker"] for r in rows if r["fiscal_year"] and r["fiscal_year"] != "UNKNOWN"))
print(f"{len(tickers)} tickers to refetch")

ok, fail = 0, 0
for i, t in enumerate(tickers):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=0&period2=9999999999&interval=1d&events=splits,div"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            data = r.read()
        d = json.loads(data)
        if d["chart"]["result"]:
            open(os.path.join(CACHE, f"pxfull_{t}.json"), "wb").write(data)
            ok += 1
        else:
            fail += 1
    except Exception as e:
        fail += 1
    time.sleep(0.3)
    if i % 20 == 0:
        print(f"[{i}/{len(tickers)}] {t}")

print(f"\nDone: {ok} ok, {fail} failed")
