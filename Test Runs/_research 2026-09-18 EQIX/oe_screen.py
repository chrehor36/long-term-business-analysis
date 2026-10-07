import sys, os, json
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "Screens"))
import floor_screen as fs
f = json.load(open("companyfacts.json", encoding="utf-8"))
print("OE", fs.owner_earnings(f))
for nm, tags in [("OCF", fs.OCF_TAGS), ("CAPX", fs.CAPX_TAGS), ("FINLEASE", fs.FINLEASE_TAGS), ("SOFT", fs.SOFTWARE_CAPX_TAGS), ("FLFLAG", fs.FINLEASE_FLAG_TAGS), ("ACQ", fs.ACQ_TAGS)]:
    print(nm, {k: round(v/1e6,1) for k, v in sorted(fs.annual(f, tags).items())})
print("CAPACQ", [{k: round(v/1e6,1) for k, v in sorted(d.items())} for d in fs.capital_acquired(f)])
print("SBC", {k: round(v/1e6,1) for k, v in sorted(fs.sbc_annual(f).items())})
print("DA", {k: round(v/1e6,1) for k, v in sorted(fs.da_annual(f).items())})
print("DAflag", fs.da_discontinuity_flag(f))
print("WC", fs.working_capital_flag(f))
print("leaseflag", fs.lease_capex_flag(f))
print("OEcapex", {k: round(v/1e6,1) for k, v in sorted(fs.oe_annual(f,"capex").items())} if isinstance(fs.oe_annual(f,"capex"), dict) else fs.oe_annual(f,"capex"))
print("acqflag", fs.acquisition_flag(f))
print("capexfund", fs.capex_funding_flag(f))
# raw tags per year for capex-like elements
g = f["facts"]["us-gaap"]
for tag in fs.CAPX_TAGS + fs.DA_TOTAL_TAGS + fs.DA_COMPONENT_TAGS + ["DepreciationAndAmortization","PaymentsToAcquireRealEstate","PaymentsForCapitalImprovements","PaymentsToDevelopRealEstateAssets"]:
    if tag in g:
        d = {}
        for x in g[tag]["units"].get("USD", []):
            if x.get("form") == "10-K" and x.get("fp") == "FY" and "start" in x:
                from datetime import date
                s, e = date.fromisoformat(x["start"]), date.fromisoformat(x["end"])
                if 340 < (e - s).days < 380: d.setdefault(x["end"][:4], set()).add(round(x["val"]/1e6, 1))
        print("RAW", tag, dict(sorted(d.items())))
