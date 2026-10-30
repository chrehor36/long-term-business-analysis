import json, os, sys
OUT = os.path.dirname(os.path.abspath(__file__))
s = json.load(open(os.path.join(OUT, "submissions.json")))
r = s["filings"]["recent"]
want = sys.argv[1] if len(sys.argv) > 1 else None
n = int(sys.argv[2]) if len(sys.argv) > 2 else 40
c = 0
for i in range(len(r["form"])):
    f = r["form"][i]
    if want and f != want: continue
    print(f, r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i], r["items"][i][:60] if r.get("items") else "")
    c += 1
    if c >= n: break
print("--- older files:", [x["name"] for x in s["filings"].get("files", [])])
