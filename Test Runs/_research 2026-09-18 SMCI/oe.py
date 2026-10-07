# Owner earnings, SMCI, from the filed cash-flow statements (FY2021-26 faces read; FY2016-20 companyfacts values cross-checked
# to the FY2019/FY2020 faces for OCF, SBC, D&A). Construction per v4 section VI CONVENTION: OCF - SBC - (c).
import json
f = json.load(open("companyfacts.json")); g = f["facts"]["us-gaap"]
def ann(tag):
    d = {}
    for x in g.get(tag, {}).get("units", {}).get("USD", []):
        if x.get("form","").startswith("10-K") and x.get("start") and x["end"][5:] == "06-30":
            y = int(x["end"][:4]); 
            if int(x["start"][:4]) == y - 1: d[y] = x["val"] / 1e6   # newest filing wins (list is in filing order)
    return d
OCF = ann("NetCashProvidedByUsedInOperatingActivities"); SBC = ann("ShareBasedCompensation"); CAPEX = ann("PaymentsToAcquirePropertyPlantAndEquipment")
DA = ann("DepreciationDepletionAndAmortization"); DA.update({2026: 53.673, 2025: 41.298, 2024: 29.617, 2023: 34.904, 2022: 32.471, 2021: 28.185})
ASSET = ["IncreaseDecreaseInAccountsReceivable","IncreaseDecreaseInInventories","IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets","IncreaseDecreaseInOtherOperatingAssets"]
LIAB = ["IncreaseDecreaseInAccountsPayable","IncreaseDecreaseInAccruedLiabilities","IncreaseDecreaseInAccruedIncomeTaxesPayable","IncreaseDecreaseInContractWithCustomerLiability","IncreaseDecreaseInDeferredRevenue","IncreaseDecreaseInOtherNoncurrentLiabilities","IncreaseDecreaseInIncomeTaxesPayableNetOfIncomeTaxesReceivable","IncreaseDecreaseInOtherOperatingLiabilities"]
A = {t: ann(t) for t in ASSET}; L = {t: ann(t) for t in LIAB}
years = list(range(2016, 2027)); rows = {}
print("FY   OCF      SBC    capex   D&A    WCcash   OCFpreWC  OE_capex  OE_da   OEpreWC_capex")
for y in years:
    wc = -sum(A[t].get(y, 0) for t in ASSET) + sum(L[t].get(y, 0) for t in LIAB)
    o, s, c, d = OCF[y], SBC[y], CAPEX[y], DA[y]
    r = dict(ocf=o, sbc=s, capex=c, da=d, wc=wc, pre=o-wc, oe_c=o-s-c, oe_d=o-s-d, pre_c=o-wc-s-c)
    rows[y] = r
    print(y, *("%8.1f" % r[k] for k in ("ocf","sbc","capex","da","wc","pre","oe_c","oe_d","pre_c")))
def mean(ys, k): return sum(rows[y][k] for y in ys)/len(ys)
for name, ys in [("3y FY2024-26", range(2024,2027)), ("5y FY2022-26 (default)", range(2022,2027)), ("10y FY2017-26", range(2017,2027)), ("FY2026", [2026])]:
    print(name, "OE capex-end %.1f  D&A-end %.1f  | pre-WC capex-end %.1f  D&A-end %.1f | WC mean %.1f" % (mean(ys,"oe_c"), mean(ys,"oe_d"), mean(ys,"pre_c"), mean(ys,"pre")-mean(ys,"sbc")-mean(ys,"da"), mean(ys,"wc")))
json.dump(rows, open("oe_rows.json","w"), indent=1)
# Display: operating cash before the working-capital lines, LESS inventory write-downs added back on the face
# (FY2016-22 "Provision for excess and obsolete inventories", FY2024-26 "Inventory valuation adjustment write-down";
# FY2023's face carries no such line, so 0), less SBC, less (c). The write-downs are a real cost of the product cycle.
WD = {2016:9.4,2017:15.7,2018:9.6,2019:32.9,2020:18.4,2021:6.8,2022:15.1,2023:0.0,2024:83.0,2025:232.1,2026:188.1}
print("\nFY  preWC-less-WD-SBC-capex   preWC-less-WD-SBC-D&A")
for y in years:
    rows[y]["pw_c"] = rows[y]["pre"] - WD[y] - rows[y]["sbc"] - rows[y]["capex"]
    rows[y]["pw_d"] = rows[y]["pre"] - WD[y] - rows[y]["sbc"] - rows[y]["da"]
    print(y, "%8.1f %8.1f" % (rows[y]["pw_c"], rows[y]["pw_d"]))
for name, ys in [("3y FY2024-26", range(2024,2027)), ("5y FY2022-26", range(2022,2027)), ("10y FY2017-26", range(2017,2027)), ("FY2026", [2026])]:
    print(name, "display capex-end %.1f D&A-end %.1f" % (mean(ys,"pw_c"), mean(ys,"pw_d")))
json.dump(rows, open("oe_rows.json","w"), indent=1)
