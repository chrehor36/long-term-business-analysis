import urllib.request, json, sys
UA = {"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read()
# find CIK
tk = json.loads(get("https://www.sec.gov/files/company_tickers.json").decode())
cik = None
for v in tk.values():
    if v["ticker"].upper() == "ALKT":
        cik = str(v["cik_str"]).zfill(10); name = v["title"]
print("CIK", cik, name)
sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json").decode())
open("Test Runs/_research 2026-09-12 ALKT/submissions.json","wb").write(json.dumps(sub).encode())
r = sub["filings"]["recent"]
rows = list(zip(r["form"], r["filingDate"], r["reportDate"], r["accessionNumber"], r["primaryDocument"]))
keep = [x for x in rows if x[0] in ("10-K","10-Q","DEF 14A","8-K","10-K/A","S-1","20-F")]
for x in keep[:90]:
    print(" | ".join(str(y) for y in x))
print("--- total recent:", len(rows), " older files:", sub["filings"].get("files"))
