# Pre-tax return on capital employed net of cash, LCID FY2022-25 (tags transcribed; FY2025 cross-checked to the 10-K face)
import json
f = json.load(open("companyfacts.json"))["facts"]["us-gaap"]
def v(tag, end):
    for x in f.get(tag, {}).get("units", {}).get("USD", []):
        if x.get("end") == end and x.get("form") in ("10-K",): return x["val"]
    return None
opl = {"2022-12-31": -2593991e3, "2023-12-31": -3099588e3, "2024-12-31": -3020820e3, "2025-12-31": -3501753e3}
for e in ["2022-12-31", "2023-12-31", "2024-12-31", "2025-12-31"]:
    A = v("Assets", e); c = v("CashAndCashEquivalentsAtCarryingValue", e) or 0
    st = v("ShortTermInvestments", e) or v("AvailableForSaleSecuritiesDebtSecuritiesCurrent", e) or 0
    lt = v("LongTermInvestments", e) or v("AvailableForSaleSecuritiesDebtSecuritiesNoncurrent", e) or 0
    ap = v("AccountsPayableCurrent", e) or 0; ocl = v("OtherLiabilitiesCurrent", e) or 0
    ce = A - c - st - lt - ap - ocl
    print(e, "assets", A/1e6, "cash+inv", (c+st+lt)/1e6, "AP+OCL", (ap+ocl)/1e6, "CE", round(ce/1e6,1), "op loss", opl[e]/1e6, "ROCE", f"{opl[e]/ce:.0%}")
