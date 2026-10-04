import json, re
from datetime import date, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"

TARGET = date(2008, 1, 1)  # the honest ceiling -- change log is too sparse before this

current = json.load(open(f"{SCRATCH}\\sp500_constituents.json"))
current_tickers = {r["symbol"]: r for r in current}
changes = json.load(open(f"{SCRATCH}\\sp500_changes.json"))

def parse_date(s):
    s = s.strip()
    for fmt in ("%B %d, %Y", "%B %d %Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None

parsed = []
for c in changes:
    d = parse_date(c["date"])
    if d:
        parsed.append((d, c))
parsed.sort(key=lambda x: x[0], reverse=True)  # most recent first

working = set(current_tickers.keys())
undone = []
for d, c in parsed:
    if d <= TARGET:
        break  # everything from here back is before our target; stop reversing
    added = c["added_ticker"].strip()
    removed = c["removed_ticker"].strip()
    if added and added in working:
        working.discard(added)
    if removed:
        working.add(removed)
    undone.append((d.isoformat(), added, c["added_name"], removed, c["removed_name"], c["reason"]))

print(f"Reconstructed universe as of {TARGET.isoformat()}: {len(working)} tickers")
print(f"Changes reversed: {len(undone)}")

# classify each ticker: still in today's S&P 500 (survivor) vs not (needs fate lookup)
still_in_index = sorted(t for t in working if t in current_tickers)
not_in_index = sorted(t for t in working if t not in current_tickers)
print(f"Still in today's S&P 500: {len(still_in_index)}")
print(f"No longer in the index (fate unknown, needs lookup): {len(not_in_index)}")
print()
print("Names no longer in the index (need fate classification):")
for t in not_in_index:
    print(" ", t)

json.dump({
    "target_date": TARGET.isoformat(),
    "reconstructed_tickers": sorted(working),
    "still_in_index_today": still_in_index,
    "left_index_since": not_in_index,
    "reversed_changes": undone,
}, open(f"{SCRATCH}\\sp500_2008_reconstruction.json", "w"), indent=1)
