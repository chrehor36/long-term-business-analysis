import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
want = {"AMZN":"0001018724-26-000004","NFLX":"0001065280-26-000034","TTD":"0001671933-26-000014",
        "CMCSA":"0001628280-26-004994","CHTR":"0001091667-26-000017","WMT":"0000104169-26-000055",
        "AAPL":"0000320193-25-000079","GOOGL":"0001652044-26-000018"}
for t, accn in want.items():
    cik = sources.cik_for(t)[0]
    raw = sources._get("https://data.sec.gov/submissions/CIK%s.json" % cik,
                       headers=sources.SEC_UA, cache_name="sub_%s.json" % t, max_age_h=240)
    d = json.loads(raw); r = d["filings"]["recent"]
    for i, a in enumerate(r["accessionNumber"]):
        if a == accn:
            print(t, cik, a, r["form"][i], r["filingDate"][i], r["primaryDocument"][i],
                  "https://www.sec.gov/Archives/edgar/data/%d/%s/%s" % (int(cik), a.replace("-",""), r["primaryDocument"][i]))
            break
    else:
        print(t, cik, accn, "NOT FOUND in recent")
