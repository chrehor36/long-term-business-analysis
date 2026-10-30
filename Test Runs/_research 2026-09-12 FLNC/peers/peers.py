import sys, os, json, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
out = {}
for t in ["TSLA","STEM","EOSE","GWH","GNRC","AES","FLNC"]:
    cik, name = sources.cik_for(t)
    print(t, cik, name)
    if not cik: continue
    txt = sources._get(f"https://data.sec.gov/submissions/CIK{cik}.json", sources.SEC_UA, f"sub_{cik}.json", max_age_h=24)
    r = json.loads(txt)["filings"]["recent"]
    ks = [(r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]) for i in range(len(r["form"])) if r["form"][i]=="10-K"][:2]
    qs = [(r["filingDate"][i], r["reportDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]) for i in range(len(r["form"])) if r["form"][i]=="10-Q"][:1]
    print("   10-K:", ks); print("   10-Q:", qs)
    time.sleep(0.3)
print()
for phrase in ["Fluence"]:
    for t,c in [("TSLA","0001318605"),("STEM","0001758766"),("EOSE","0001805077"),("GWH","0001819438"),("GNRC","0001474735"),("AES","0000874761")]:
        try:
            n,u = sources.fts_count(phrase, cik=c, forms="10-K")
            print(phrase, t, n)
        except Exception as e: print(phrase, t, "ERR", e)
        time.sleep(0.5)
for phrase in ["Tesla","Powin","Wartsila","Wärtsilä","Sungrow","CATL","Stem, Inc"]:
    n,u = sources.fts_count(phrase, cik="0001868941", forms="10-K"); print("FLNC 10-K names", phrase, n); time.sleep(0.5)
