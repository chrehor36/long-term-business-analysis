# Probe by the overnight cycle (brief prep): what the CURRENT screen returns for SMCI.
# Fresh companyfacts pull; no number here is a clearance.
import sys, os, json, urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "Screens"))
import floor_screen as F
url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0001375365.json"
req = urllib.request.Request(url, headers={"User-Agent": "BRK research chrehor36@gmail.com", "Accept-Encoding": "identity"})
facts = json.load(urllib.request.urlopen(req, timeout=60))
out = os.path.join(os.path.dirname(__file__), "companyfacts.json")
json.dump(facts, open(out, "w"))
print("entity", facts.get("entityName"))
print("owner_earnings:", F.owner_earnings(facts))
for name in ["restatement_shift", "scale_shift", "share_count_shift", "acquisition_flag", "working_capital_flag", "da_discontinuity_flag", "capex_funding_flag", "stale_filer"]:
    try:
        print(name, ":", getattr(F, name)(facts))
    except Exception as e:
        print(name, ": ERR", repr(e))
print("sbc_annual:", F.sbc_annual(facts))
print("da_annual:", F.da_annual(facts))
print("ocf:", F.ocf_continuing(facts))
print("capex annual:", F.annual(facts, F.CAPX_TAGS))
print("shares:", F.shares_outstanding(facts))
