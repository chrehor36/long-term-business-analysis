# Probe by the overnight cycle (brief prep): what the CURRENT screen returns for BX,
# and what the 2026-09-01 triage code (a8bc84f) returned on facts filed by then.
# Fresh companyfacts pull; no number here is a clearance.
import sys, os, json, copy, urllib.request
from datetime import date
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
sys.path.insert(0, os.path.join(here, "..", "..", "Screens"))
sys.path.insert(0, os.path.join(here, "..", "..", "Backtests", "scripts"))
import floor_screen as F
import floor_screen_a8bc84f as O
url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0001393818.json"
req = urllib.request.Request(url, headers={"User-Agent": "BRK research chrehor36@gmail.com", "Accept-Encoding": "identity"})
facts = json.load(urllib.request.urlopen(req, timeout=60))
json.dump(facts, open(os.path.join(here, "companyfacts.json"), "w"))
print("entity", facts.get("entityName"))
print("== CURRENT screen ==")
print("owner_earnings:", F.owner_earnings(facts))
for name in ["restatement_shift", "scale_shift", "acquisition_flag", "working_capital_flag", "da_discontinuity_flag", "capex_funding_flag", "stale_filer", "lease_capex_flag"]:
    try:
        print(name, ":", getattr(F, name)(facts))
    except Exception as e:
        print(name, ": ERR", repr(e))
print("share_count_shift WITH ticker:", F.share_count_shift(facts, "BX"))
print("share_count_shift no ticker:", F.share_count_shift(facts))
print("sbc_annual:", F.sbc_annual(facts))
print("da_annual:", F.da_annual(facts))
print("ocf:", F.ocf_continuing(facts))
print("capex annual:", F.annual(facts, F.CAPX_TAGS))
print("capital_acquired:", F.capital_acquired(facts))
print("rev:", F.annual(facts, F.REV_TAGS))
print("shares:", F.shares_outstanding(facts))
def cut(facts, before):
    g = copy.deepcopy(facts)
    for ns in g["facts"].values():
        for t in ns.values():
            for u, L in t["units"].items():
                t["units"][u] = [x for x in L if x.get("filed", "9999") <= before]
    return g
f0 = cut(facts, "2026-09-01")
O.TODAY = date(2026, 9, 1)
print("== a8bc84f on facts filed by 2026-09-01 ==")
for name in ["share_count_shift", "scale_shift", "restatement_shift", "owner_earnings"]:
    try:
        print(name, ":", getattr(O, name)(f0))
    except Exception as e:
        print(name, ": ERR", repr(e))
print("dei elements:", list(facts["facts"].get("dei", {}).keys()))
for k, t in facts["facts"].get("dei", {}).items():
    for u, L in t["units"].items():
        for x in L[-6:]: print("dei", k, x.get("end"), x["val"], x["form"], x["filed"], x.get("frame",""))
