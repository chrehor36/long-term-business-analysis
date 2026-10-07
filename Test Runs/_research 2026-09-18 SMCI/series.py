import json, sys
sys.path.insert(0, r"C:/Users/chreh/OneDrive/Documents/BRK/Screens")
import floor_screen as N
f = json.load(open("companyfacts.json"))
def A(tags, v="newest"):
    try: return N.annual(f, tags, vintage=v)
    except TypeError: return N.annual(f, tags)
rev = A(["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueNet"])
gp = A(["GrossProfit"]); oi = A(["OperatingIncomeLoss"]); ni = A(["NetIncomeLoss"])
eq = {}
g = f["facts"]["us-gaap"]
def inst(tag):
    d = {}
    for x in g.get(tag, {}).get("units", {}).get("USD", []):
        if x.get("form","").startswith("10-K") and x["end"][5:] == "06-30":
            d[x["end"]] = x["val"]  # later filings overwrite
    return d
E = inst("StockholdersEquity"); C = inst("CashAndCashEquivalentsAtCarryingValue"); INV = inst("InventoryNet"); AR = inst("AccountsReceivableNetCurrent"); TA = inst("Assets")
print("FY rev gp gm% oi om% ni")
for k in sorted(rev):
    r = rev[k]; p = gp.get(k); o = oi.get(k); n = ni.get(k)
    print(k, round(r/1e6,1), p and round(p/1e6,1), p and round(100*p/r,2), o and round(o/1e6,1), o and round(100*o/r,2), n and round(n/1e6,1))
print("balance: end equity cash inventory AR assets")
for k in sorted(E):
    print(k, *(round(d.get(k,0)/1e6,1) for d in (E,C,INV,AR,TA)))
