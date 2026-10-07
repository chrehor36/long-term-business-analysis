"""List TRV's 10-K, 10-Q, DEF 14A and 8-K filings from the cached EDGAR submissions file."""
import json
import sys

d = json.load(open(sys.argv[1]))
since = sys.argv[2] if len(sys.argv) > 2 else "2024-01-01"
forms = set((sys.argv[3] if len(sys.argv) > 3 else "10-K,10-Q,DEF 14A,8-K").split(","))
r = d["filings"]["recent"]
for i in range(len(r["form"])):
    if r["form"][i] in forms and r["filingDate"][i] >= since:
        print(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i],
              r.get("items", [""] * len(r["form"]))[i])
