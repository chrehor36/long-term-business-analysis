import sys, json
sys.path.insert(0, "tools")
import sources as s
print("SOV", s.sovereign("USD"))
print("PRICE BAM", s.price("BAM"))
print("PRICE BN", s.price("BN"))
print("SPLIT", s.split_factor_after("BAM", "2026-07-01"))
print("DEAL", s.deal_note(1937926))
print("NAME", s.name_change_note(1937926))
import urllib.request
r = urllib.request.urlopen(urllib.request.Request("https://data.sec.gov/submissions/CIK0001937926.json", headers=s.SEC_UA)).read()
open("Test Runs/_research 2026-09-13 BAM/submissions.json","wb").write(r)
d = json.loads(r)
print(d["name"], d.get("formerNames"), d.get("sicDescription"), d.get("stateOfIncorporation"), d.get("fiscalYearEnd"))
rec = d["filings"]["recent"]
for i in range(len(rec["form"])):
    print(rec["filingDate"][i], rec["form"][i], rec["accessionNumber"][i], rec["primaryDocument"][i], rec.get("items",[""]*999)[i], rec["primaryDocDescription"][i])
print("files", d["filings"].get("files"))
