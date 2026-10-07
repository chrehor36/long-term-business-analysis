import json, os
from fetch_core import *
p = os.path.join(HERE, "submissions_001.json")
if not os.path.exists(p):
    open(p, "w").write(get("https://data.sec.gov/submissions/CIK0001640147-submissions-001.json"))
s = json.load(open(p))
out = []
for i in range(len(s["form"])):
    out.append(f'{s["filingDate"][i]} {s["form"][i]:10s} {s["accessionNumber"][i]} {s["primaryDocument"][i]} {s["items"][i]} {s["reportDate"][i]}')
open(os.path.join(HERE, "filings_list_old.txt"), "w").write("\n".join(out))
docs = [
 ("0001640147-26-000037", "snow-20260731.htm", "10Q_2026-07-31"),
 ("0001640147-26-000030", "snow-20260430.htm", "10Q_2026-04-30"),
 ("0001640147-26-000008", "snow-20260131.htm", "10K_FY2026"),
 ("0001640147-25-000052", "snow-20250131.htm", "10K_FY2025"),
 ("0001640147-24-000101", "snow-20240131.htm", "10K_FY2024"),
 ("0001640147-23-000030", "snow-20230131.htm", "10K_FY2023"),
 ("0001640147-26-000019", "snow-20260518.htm", "DEF14A_2026"),
]
for acc, doc, name in docs:
    grab(acc, doc, name)
for acc, doc, name in [("0001640147-22-000023","snow-20220131.htm","10K_FY2022"),("0001640147-21-000073","snow-20210131.htm","10K_FY2021")]:
    grab(acc, doc, name)
