"""Re-fetch full price history WITH split/dividend events for the whole universe.

Why: the existing `pxlong_*.json` files (334 tickers with no `px_` twin) were
fetched without `events=div,split`, so they carry no split data. The market-cap
fix needs the post-anchor split factor for every ticker; without events it
silently defaults to 1.0 and the look-ahead bug survives untouched for most of
the universe. Writes pxfix_{ticker}.json.
"""
import json, os, time, urllib.request, urllib.error

SCRATCH = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SCRATCH, "bt_cache")

recon = json.load(open(os.path.join(SCRATCH, "sp500_2013_reconstruction.json")))
universe = sorted(set(recon["reconstructed_tickers"]) | {"SPY"})

P1 = 662688000    # 1991-01-01, comfortably before every anchor we test
P2 = 1800000000

done, failed, skipped = [], [], []
for i, t in enumerate(universe, 1):
    out = os.path.join(CACHE, f"pxfix_{t}.json")
    if os.path.exists(out) and os.path.getsize(out) > 500:
        skipped.append(t)
        continue
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{t}"
           f"?period1={P1}&period2={P2}&interval=1d&events=div,split")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        d = json.loads(data)
        res = d["chart"]["result"][0]
        if "timestamp" not in res:
            failed.append((t, "no timestamps"))
        else:
            open(out, "wb").write(data)
            nsp = len(res.get("events", {}).get("splits", {}))
            done.append((t, len(res["timestamp"]), nsp))
    except Exception as e:
        failed.append((t, str(e)[:60]))
    time.sleep(0.25)
    if i % 50 == 0:
        print(f"  ...{i}/{len(universe)} (ok={len(done)} fail={len(failed)})",
              flush=True)

print(f"\nDONE fetched={len(done)} skipped={len(skipped)} failed={len(failed)}")
with_splits = [d for d in done if d[2] > 0]
print(f"of fetched, {len(with_splits)} have >=1 split event")
json.dump({"fetched": done, "failed": failed},
          open(os.path.join(SCRATCH, "refetch_events_log.json"), "w"), indent=1)
if failed:
    print("failures:", failed[:25])
