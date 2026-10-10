# Competitor operating margins and returns from their own XBRL filings (SEC companyfacts, 10-K annual facts,
# newest vintage). Transcription only; the run reads the filed statements for the figures it leans on.
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import sources
NAMES = ["ITW", "LECO", "DOV", "MIDD", "PH", "EMR", "ESAB"]
REV = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet",
       "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueGoodsNet"]
OI = ["OperatingIncomeLoss"]
PRETAX = ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
          "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]
INT = ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"]
OCF = ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]
CAPEX = ["PaymentsToAcquirePropertyPlantAndEquipment"]
ACQ = ["PaymentsToAcquireBusinessesNetOfCashAcquired"]
SBC = ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"]
out = {}
for t in NAMES:
    cik, title = sources.cik_for(t)
    if not cik:
        print(t, "no CIK"); continue
    f = sources.sec_facts(cik)
    row = {"title": title, "cik": cik}
    for k, tags in (("rev", REV), ("oi", OI), ("pretax", PRETAX), ("int", INT), ("ocf", OCF), ("capex", CAPEX), ("acq", ACQ), ("sbc", SBC)):
        d, used, unit = sources.annual(f, tags, vintage="newest")
        row[k] = {e[:4]: round(v, 1) for e, v in d.items()}
        row[k + "_tag"] = used
    out[t] = row
json.dump(out, open(os.path.join(os.path.dirname(__file__), "cache", "peers.json"), "w"), indent=1)
for t, r in out.items():
    print("=====", t, r["title"], r["cik"], "| rev tag:", r["rev_tag"], "| oi tag:", r["oi_tag"])
    yrs = sorted(set(r["rev"]) | set(r["oi"]) | set(r["pretax"]))
    yrs = [y for y in yrs if "2011" <= y <= "2026"]
    for y in yrs:
        rv, oi, pt, it = r["rev"].get(y), r["oi"].get(y), r["pretax"].get(y), r["int"].get(y)
        m = f"{100*oi/rv:5.1f}%" if rv and oi is not None else "   - "
        m2 = f"{100*(pt+(it or 0))/rv:5.1f}%" if rv and pt is not None else "   - "
        print(f"  {y} rev {rv!s:>9} oi {oi!s:>8} margin {m}  (pretax+interest)/rev {m2}  ocf {r['ocf'].get(y)!s:>7} capex {r['capex'].get(y)!s:>6} acq {r['acq'].get(y)!s:>7} sbc {r['sbc'].get(y)}")
