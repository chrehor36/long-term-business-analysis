import json, urllib.request, sys, os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
for cik in sys.argv[1:]:
    p=f"subs_{cik}.json"
    if not os.path.exists(p):
        d=urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/submissions/CIK{cik}.json",headers=UA),timeout=60).read()
        open(p,"wb").write(d)
    j=json.load(open(p))
    print(j["name"])
    r=j["filings"]["recent"]
    forms=set()
    for i,f in enumerate(r["form"]):
        forms.add(f)
        if f in ("10-K","20-F","40-F","6-K","F-6","15F","10-K/A") :
            print(f, r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i])
    print(sorted(forms))
