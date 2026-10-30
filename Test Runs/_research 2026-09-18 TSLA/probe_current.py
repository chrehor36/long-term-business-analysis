# What the CURRENT screen returns for TSLA (tagged data, a prompt only). Uses companyfacts.json on disk.
import sys, os, json
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "..", "Screens")); sys.path.insert(0, os.path.join(here, "..", "..", "Backtests", "scripts"))
import floor_screen as F
facts = json.load(open(os.path.join(here, "companyfacts.json")))
print("owner_earnings:", F.owner_earnings(facts))
for name in ["restatement_shift", "scale_shift", "acquisition_flag", "working_capital_flag", "da_discontinuity_flag", "capex_funding_flag", "stale_filer", "lease_capex_flag"]:
    try: print(name, ":", getattr(F, name)(facts))
    except Exception as e: print(name, ": ERR", repr(e))
print("share_count_shift WITH ticker:", F.share_count_shift(facts, "TSLA"))
for n in ["sbc_annual","da_annual","ocf_continuing","capital_acquired"]:
    try: print(n, {str(k):round(v/1e6,1) for k,v in sorted(getattr(F,n)(facts).items())})
    except Exception as e: print(n, "ERR", e)
print("rev:", {str(k):round(v/1e6,1) for k,v in sorted(F.annual(facts, F.REV_TAGS).items())})
print("capex annual:", {str(k):round(v/1e6,1) for k,v in sorted(F.annual(facts, F.CAPX_TAGS).items())})
