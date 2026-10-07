# BIRD run 2026-09-19. Arithmetic only (operator rule 8): owner earnings by window and (c) end, the lease's implicit
# rate, the notes' all-in cost, and the equity series. Annual inputs from companyfacts (single vintage for every
# cash-flow fact, vintage_probe_out.txt), FY2025 and FY2024 cross-checked to the FY2025 10-K cash-flow face; H1
# figures from the Q2 2026 10-Q face (0001437749-26-028446) and the Q2 2025 10-Q (0001653909-25-000051).
import json, os
here = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(here, "companyfacts.json")))["facts"]["us-gaap"]
def fy(tag):
    out = {}
    for x in f.get(tag, {}).get("units", {}).get("USD", []):
        if x.get("fp") == "FY" and x["form"].startswith("10-K") and x.get("start"):
            s, e = x["start"], x["end"]
            if int(e[:4]) - int(s[:4]) == 1 or s[5:] == "01-01":
                out.setdefault(e[:4], x["val"])
    return out
ocf = fy("NetCashProvidedByUsedInOperatingActivities"); sbc = fy("ShareBasedCompensation")
cap = fy("PaymentsToAcquirePropertyPlantAndEquipment"); da = fy("DepreciationDepletionAndAmortization")
rev = fy("RevenueFromContractWithCustomerExcludingAssessedTax") or {}
M = 1e6
print("year   OCF     SBC    capex    D&A    OE(D&A end)  OE(capex end)")
rows = {}
for y in ["2021", "2022", "2023", "2024", "2025"]:
    a, b, c, d = ocf[y]/M, sbc[y]/M, cap[y]/M, da[y]/M
    rows[y] = (a - b - d, a - b - c)
    print(y, f"{a:8.1f} {b:7.1f} {c:7.1f} {d:7.1f} {a-b-d:11.1f} {a-b-c:13.1f}")
def mean(ys, k): return sum(rows[y][k] for y in ys) / len(ys)
for lbl, ys in (("five-year FY2021-25", ["2021","2022","2023","2024","2025"]), ("three-year FY2023-25", ["2023","2024","2025"])):
    print(lbl, f"D&A end {mean(ys,0):.1f}  capex end {mean(ys,1):.1f}")
# TTM to 2026-06-30, whole company (continuing + discontinued), from the faces
fy25 = dict(ocf=-55.083, sbc=7.763, capex=3.145, da=8.019)
h125 = dict(ocf=-13.529 - 23.046, sbc=0.753, capex=1.371)   # Q2 2026 10-Q recast; SBC continuing only on the face
h126 = dict(ocf=-7.304 - 15.884, sbc=2.395, capex=2.758)
print("H1 2025 total OCF", round(h125["ocf"], 3), "; H1 2026 total OCF", round(h126["ocf"], 3))
ttm_ocf = fy25["ocf"] - h125["ocf"] + h126["ocf"]
print("TTM OCF (whole company) to 2026-06-30:", round(ttm_ocf, 3))
# continuing operations only, H1 2026, before the working-capital release
nl_c = -18.869; noncash = 2.395 + 0.412 + 0.229
print("H1 2026 continuing: OCF -7.304 = net loss", nl_c, "+ non-cash", noncash, "+ working capital", round(-7.304 - nl_c - noncash, 3))
print("H1 2026 continuing, before working capital, less SBC:", round(nl_c + noncash - 2.395, 3), "; annualised x2:", round(2 * (nl_c + noncash - 2.395), 1))
# the one lease: paid 2,758 on 2026-04-19; 30 monthly payments then 6 larger, plus a purchase option; schedule from Note 11
pay = [86.67] * 30 + [155.5] * 6
pay[-1] += 140.0   # end-of-term option, 'approximately $0.1 million'; total then ~3,671 against the note's ~$3.7M
def npv(r, cf0, cfs): return -cf0 + sum(c / (1 + r) ** (i + 1) for i, c in enumerate(cfs))
lo, hi = 0.0, 0.1
for _ in range(200):
    mid = (lo + hi) / 2
    if npv(mid, 2758, pay) > 0: lo = mid
    else: hi = mid
print("lease: total receipts", round(sum(pay)), "k; implicit monthly rate", round(mid, 5), "-> annual", round((1 + mid) ** 12 - 1, 4))
# the notes: 12% coupon on face, 5% OID, ~$0.5M of issuance cost on $8.25M face, two-year term
face, net = 8.25, 2.8 + 4.5
print("notes: net cash", net, "on face", face, "-> upfront cost", round(1 - net / face, 4))
lo, hi = 0.0, 1.0
cf = [face * 0.12] + [face * 1.12]
for _ in range(200):
    mid = (lo + hi) / 2
    v = -net + cf[0] / (1 + mid) + cf[1] / (1 + mid) ** 2
    if v > 0: lo = mid
    else: hi = mid
print("notes: all-in annual cost if held to maturity and paid in cash", round(mid, 4))
eq = {}
for x in f.get("StockholdersEquity", {}).get("units", {}).get("USD", []):
    if x["end"].endswith("12-31") and x["form"].startswith("10-K"): eq.setdefault(x["end"][:4], x["val"] / M)
print("equity at year ends", {k: round(v, 1) for k, v in sorted(eq.items())})
nl = fy("NetIncomeLoss")
for y in ["2021","2022","2023","2024","2025"]:
    avg = (eq.get(str(int(y)-1), float("nan")) + eq[y]) / 2
    print(y, "net loss", round(nl[y]/M, 1), "return on average equity", round(nl[y]/M/avg, 3))
