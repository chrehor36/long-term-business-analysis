"""The skip reason, tested in two parts. (a) floor_screen.py as it stood at a8bc84f, on today's companyfacts;
(b) the current floor_screen.owner_earnings() and its inputs. Nothing under Screens/ or tools/ is edited."""
import sys, os, json, importlib.util, urllib.request
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "Screens"))
sys.path.insert(0, os.path.join(ROOT, "Backtests", "scripts"))
import sources as S

cf = os.path.join(HERE, "companyfacts.json")
if not os.path.exists(cf):
    raw = urllib.request.urlopen(urllib.request.Request(
        "https://data.sec.gov/api/xbrl/companyfacts/CIK0000021665.json", headers=S.SEC_UA), timeout=120).read()
    open(cf, "wb").write(raw)
facts = json.load(open(cf, encoding="utf-8"))

out = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

os.chdir(os.path.join(ROOT, "Screens"))
spec = importlib.util.spec_from_file_location("fs_old", os.path.join(HERE, "floor_screen_a8bc84f.py"))
m = importlib.util.module_from_spec(spec)
_argv = sys.argv; sys.argv = [sys.argv[0]]
spec.loader.exec_module(m)
sys.argv = _argv
p("== (a) a8bc84f owner_earnings():", m.owner_earnings(facts))
p("a8bc84f CAPX_TAGS", m.CAPX_TAGS)
p("a8bc84f annual(OCF):", {k: round(v, 1) for k, v in sorted(m.annual(facts, m.OCF_TAGS).items())[-8:]})
p("a8bc84f annual(SBC):", {k: round(v, 1) for k, v in sorted(m.annual(facts, m.SBC_TAGS).items())[-8:]})
capx_old, _ = m.capital_acquired(facts)
p("a8bc84f capital_acquired cash capex:", {k: round(v, 1) for k, v in sorted(capx_old.items())[-8:]})
for t in m.CAPX_TAGS:
    p("  a8bc84f annual([", t, "]):", {k: round(v, 1) for k, v in sorted(m.annual(facts, [t]).items())[-12:]})
p("a8bc84f da_annual:", {k: round(v, 1) for k, v in sorted(m.da_annual(facts).items())[-8:]})

import floor_screen as F
p("\n== (b) current owner_earnings():", F.owner_earnings(facts))
ocf, note = F.ocf_continuing(facts)
sbc = F.sbc_annual(facts)
capx, lease = F.capital_acquired(facts)
da = F.da_annual(facts)
p("disc note:", note)
for e in sorted(ocf)[-12:]:
    p(e, "OCF", round(ocf[e], 1), "SBC", sbc.get(e), "CAPEX", capx.get(e), "DA", da.get(e))
for fn in ("working_capital_flag", "acquisition_flag", "restatement_shift", "scale_shift", "da_discontinuity_flag",
           "capex_funding_flag", "lease_capex_flag", "share_count_shift"):
    try:
        p(fn, getattr(F, fn)(facts))
    except Exception as ex:
        p(fn, "ERR", type(ex).__name__, ex)

# which us-gaap capex-like tags exist, by year
g = facts["facts"]["us-gaap"]
for t in sorted(g):
    if any(k in t for k in ("PaymentsToAcquire", "CapitalExpend", "ShareBasedComp", "EmployeeStockOwnership", "Depreciation")):
        vals = [(x["end"], x["val"], x.get("fp"), x.get("form")) for u in g[t]["units"].values() for x in u if x.get("form") == "10-K" and x.get("fp") == "FY"]
        yrs = sorted({v[0] for v in vals})
        p("TAG", t, len(yrs), yrs[:1], yrs[-1:])
open(os.path.join(HERE, "skip_test_out.txt"), "w", encoding="utf-8").write("\n".join(out))
