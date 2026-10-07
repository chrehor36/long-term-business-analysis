import json
sub=json.load(open("Test Runs/_research 2026-09-12 ALKT/submissions.json"))
r=sub["filings"]["recent"]
for f,d,rd,a,p,it in zip(r["form"],r["filingDate"],r["reportDate"],r["accessionNumber"],r["primaryDocument"],r["items"]):
    if d>="2021-01-01" and f not in ("4","3","144","S-8","S-8 POS"):
        print(f,d,rd,a,p,"items:",it)
print(sub.get("sicDescription"), sub.get("fiscalYearEnd"), sub.get("stateOfIncorporation"))
