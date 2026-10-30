import json,glob,os
for f in sorted(glob.glob("sub_*.json")):
    d=json.load(open(f))
    r=d["filings"]["recent"]
    print("=== ",d.get("name"),d.get("cik"))
    for i in range(len(r["form"])):
        if r["form"][i] in ("10-K","10-K/A"):
            print("  ",r["form"][i], r["accessionNumber"][i], "filed",r["filingDate"][i], "period",r["reportDate"][i], r["primaryDocument"][i])
