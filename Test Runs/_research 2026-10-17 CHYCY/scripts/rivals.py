# Annual (10-K, FY, 12-month) values of a few tags from SEC companyfacts; earliest-filed vintage per period end.
import json, sys
names = {"0001124198": "Fluor", "0001357615": "KBR", "0000708819": "McDermott"}
tags = ["NetIncomeLoss", "ProfitLoss", "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
        "StockholdersEquity", "OperatingIncomeLoss"]
from datetime import date
for cik, nm in names.items():
    f = json.load(open(f"cache/sec/facts_{cik}.json"))["facts"]["us-gaap"]
    print("=====", nm, cik)
    for t in tags:
        if t not in f: continue
        units = f[t]["units"].get("USD", [])
        best = {}
        for u in units:
            if u.get("form") != "10-K": continue
            end = u["end"]
            if "start" in u:
                d = (date.fromisoformat(end) - date.fromisoformat(u["start"])).days
                if not 350 <= d <= 380: continue
            if end not in best or u["filed"] < best[end][1]:
                best[end] = (u["val"], u["filed"], u["accn"])
        rows = sorted((e, v) for e, v in best.items() if e >= "2014-12-01")
        print(t, "; ".join(f"{e[:7]} {v[0]/1e6:,.0f} [{v[2]}]" for e, v in rows))
