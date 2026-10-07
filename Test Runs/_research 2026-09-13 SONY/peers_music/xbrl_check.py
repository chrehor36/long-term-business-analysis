import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
f=sources.sec_facts("0001319161")
g=f["facts"]["us-gaap"]
for tag in ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","OperatingIncomeLoss","PaymentsToAcquirePropertyPlantAndEquipment"]:
    if tag in g:
        for u in g[tag]["units"]["USD"]:
            if u.get("form")=="10-K" and u.get("fp")=="FY" and u["end"] in("2025-09-30","2024-09-30","2023-09-30") and u.get("accn","").startswith("0001319161-25") and "frame" in u or (u.get("form")=="10-K" and u["end"]=="2025-09-30" and u.get("start","").startswith("2024-10")):
                print(tag,u["start"],u["end"],u["val"],u["accn"],u.get("segment",""))
