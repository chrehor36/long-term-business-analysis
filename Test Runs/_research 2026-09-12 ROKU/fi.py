import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
for name, cik in [("SAMSUNG ELECTRONICS CO LTD /FI","0000879316"),
                  ("SAMSUNG DISPLAY CO LTD","0001843625"),
                  ("LG ELECTRONICS INC","0000948343"),
                  ("LG ELECTRONICS INC /FI","0000930445"),
                  ("LG DISPLAY CO LTD","0001290109"),
                  ("TCL ELECTRONICS HOLDINGS/ADR","0002073804")]:
    try:
        raw = sources._get("https://data.sec.gov/submissions/CIK%s.json" % cik,
                           headers=sources.SEC_UA, cache_name="sub_fi_%s.json" % cik, max_age_h=240)
        d = json.loads(raw)
        r = d["filings"]["recent"]
        forms = {}
        for i, f in enumerate(r["form"]):
            forms.setdefault(f, []).append(r["filingDate"][i])
        print("=== %s  CIK %s" % (d["name"], cik))
        print("    tickers:", d.get("tickers"), "exchanges:", d.get("exchanges"),
              "category:", repr(d.get("category")), "SIC:", d.get("sicDescription"))
        print("    total recent filings:", len(r["form"]))
        for f in sorted(forms):
            ds = sorted(forms[f])
            print("      %-12s n=%-4d first=%s last=%s" % (f, len(ds), ds[0], ds[-1]))
        print("    older archive files:", len(d["filings"].get("files", [])))
    except Exception as e:
        print(name, cik, "ERR", repr(e))
    print()
