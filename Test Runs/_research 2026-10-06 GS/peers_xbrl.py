import json, urllib.request, time, sys
UA = "Long-Term Business Analysis research chrehor36@gmail.com"
peers = {"GS": 886982, "MS": 895421, "JPM": 19617}
tags = ["Assets", "Deposits", "StockholdersEquity", "InterestExpenseDeposits", "InterestExpenseDeposit"]
for t, cik in peers.items():
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120))
    g = d["facts"]["us-gaap"]
    for tag in tags:
        if tag not in g:
            continue
        for u in g[tag]["units"].get("USD", []):
            if u.get("form") == "10-K" and u.get("fy") == 2025 and (u.get("fp") == "FY"):
                end = u["end"]
                if end.startswith("2025-12") or end.startswith("2024-12"):
                    dur = "" if "start" not in u else u["start"] + ".."
                    print(t, tag, dur + end, u["val"], u["accn"])
    time.sleep(0.5)
