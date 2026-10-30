"""Print annual (10-K, ~12-month duration or instant) values of chosen XBRL tags from a cached companyfacts file.
Arithmetic transcription only; first-filed value for each fiscal period end is kept, later restatements shown in brackets."""
import json, sys
from datetime import date
t = sys.argv[1]; tags = sys.argv[2].split(","); start = sys.argv[3] if len(sys.argv) > 3 else "2015-01-01"
f = json.load(open(f"cache/facts_{t}.json"))["facts"]
def d(s): return date.fromisoformat(s)
for tag in tags:
    ns = "us-gaap" if tag in f.get("us-gaap", {}) else ("dei" if tag in f.get("dei", {}) else None)
    if not ns: print(f"{tag}: not found"); continue
    units = f[ns][tag]["units"]; u = list(units)[0]
    rows = {}
    for r in units[u]:
        if r.get("form") not in ("10-K", "10-K/A"): continue
        if r["end"] < start: continue
        if "start" in r:
            days = (d(r["end"]) - d(r["start"])).days
            if not 350 <= days <= 380: continue
        key = r["end"]
        rows.setdefault(key, []).append((r["filed"], r["val"], r["accn"]))
    out = []
    for k in sorted(rows):
        v = sorted(rows[k])
        first = v[0]; last = v[-1]
        s = f"{k}:{first[1]/1e6:,.1f}"
        if last[1] != first[1]: s += f"[{last[1]/1e6:,.1f}]"
        out.append(s)
    print(f"{tag} ({u}): " + "  ".join(out))
