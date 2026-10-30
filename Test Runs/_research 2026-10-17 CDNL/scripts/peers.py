# pull annual (10-K, FY) revenue, operating income, net income and equity for the comparison set from SEC companyfacts
import json, urllib.request, sys, time
sys.stdout.reconfigure(encoding="utf-8")
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
peers = {"STRL": 874238, "ROAD": 1718227, "GVA": 861459}
tags = {"rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "ContractsRevenue"],
        "opinc": ["OperatingIncomeLoss"], "ni": ["NetIncomeLoss", "ProfitLoss"],
        "eq": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]}
for t, cik in peers.items():
    d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", headers=UA)))
    g = d["facts"]["us-gaap"]
    out = {}
    for k, names in tags.items():
        for n in names:
            if n not in g: continue
            for u in g[n]["units"].get("USD", []):
                if u.get("form") != "10-K": continue
                if k == "eq":
                    y = int(u["end"][:4]); mo = u["end"][5:7]
                else:
                    if "start" not in u: continue
                    days = (int(u["end"][:4]) - int(u["start"][:4])) * 365 + (int(u["end"][5:7]) - int(u["start"][5:7])) * 30
                    if days < 330 or days > 400: continue
                    y = int(u["end"][:4])
                key = (y, k)
                if key not in out: out[key] = u["val"]
    print(t, d["entityName"], "accession sample:", g["OperatingIncomeLoss"]["units"]["USD"][-1]["accn"])
    print(" year   rev(M)  opinc(M)  opm%   ni(M)   eq(M)  ROE%")
    for y in range(2008, 2026):
        r, o, n, e = (out.get((y, x)) for x in ("rev", "opinc", "ni", "eq"))
        f = lambda v: f"{v/1e6:8.1f}" if v is not None else "       -"
        opm = f"{100*o/r:5.1f}" if r and o is not None else "    -"
        roe = f"{100*n/e:5.1f}" if n is not None and e else "    -"
        print(f" {y} {f(r)} {f(o)} {opm} {f(n)} {f(e)} {roe}")
    time.sleep(0.5)
