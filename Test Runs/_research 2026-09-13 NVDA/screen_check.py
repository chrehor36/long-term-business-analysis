import sys, os, json
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "Screens"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
os.chdir(os.path.join(ROOT, "Screens"))
import floor_screen as F
HERE = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 NVDA"
facts = json.load(open(os.path.join(HERE, "companyfacts.json")))
print("owner_earnings():", F.owner_earnings(facts))
ocf, note = F.ocf_continuing(facts)
sbc = F.sbc_annual(facts)
capx, lease = F.capital_acquired(facts)
da = F.da_annual(facts)
print("disc note:", note)
for e in sorted(ocf):
    print(e, "OCF", round(ocf[e], 1), "SBC", sbc.get(e), "CAPEX", capx.get(e), "DA", da.get(e))
print("lease flag:", lease)
try:
    print("wc flag:", F.working_capital_flag(facts))
except Exception as ex:
    print("wc flag err", ex)
for fn in ("acquisition_flag", "restatement_shift", "scale_shift", "da_discontinuity_flag", "capex_funding_flag", "lease_capex_flag", "share_count_shift"):
    try:
        print(fn, getattr(F, fn)(facts))
    except Exception as ex:
        print(fn, "ERR", type(ex).__name__, ex)
