"""Q7 arithmetic for the D run of 2026-10-18. Every input is typed from the filed statements
named in the run file; nothing is fetched here. Arithmetic only, no verdict."""
import sys
sys.stdout.reconfigure(encoding="utf-8")

R = 0.0543          # 30-year Treasury par yield, 2026-10-16
FLOOR = 0.10        # Q7 floor CONVENTION
SH = 879.525949     # millions of shares, 10-Q cover, 2026-07-24
PX = 63.56
CAP = SH * PX
Y = [2022, 2023, 2024, 2025]

ocf = {2022: 3700, 2023: 6572, 2024: 5018, 2025: 5361}            # consolidated, as filed
disc_ocf = {2022: 1029, 2023: 663, 2024: 215, 2025: 0}           # chained from MD&A; 2025 = 0 is a stated guess
sbc = {2022: 36, 2023: 44, 2024: 53, 2025: 46}                   # Note 20
pref = {2022: 93, 2023: 81, 2024: 78, 2025: 44}                  # equity statements
da_seg = {2022: 2442, 2023: 2580, 2024: 2345, 2025: 2387}        # segment tables (continuing, income statement)
nucfuel = {2022: 295, 2023: 295, 2024: 2639 - 2345, 2025: 2684 - 2387}  # 2022-23 = guess, mean of 2024-25
capex_seg = {2022: 7758, 2023: 10235, 2024: 12427, 2025: 12653}  # segment table totals (= CF capex + solar acquisitions)
corp_capex = {2022: 1180, 2023: 1342, 2024: 582, 2025: 101}
CORP_OWN = 100                                                   # guess: corporate's own capex, the 2025 level
stonepeak_contrib = {2022: 0, 2023: 0, 2024: 377, 2025: 1569}
nci_sale = {2022: 0, 2023: 0, 2024: 2558, 2025: -88}
dist_stonepeak = {2022: 0, 2023: 0, 2024: 0, 2025: 241}
ltd_iss = {2022: 4965, 2023: 3310, 2024: 5993, 2025: 8897}
ltd_rep = {2022: 1388, 2023: 5673, 2024: 2740, 2025: 1722}
interest = {2022: 1002, 2023: 1679, 2024: 1893, 2025: 2022}      # segment tables, consolidated
rev = {2022: 13938, 2023: 14393, 2024: 14459, 2025: 16506}
TAX = 0.21                                                       # CONVENTION: federal statutory rate for the interest add-back
DEBT_SHARE = 24059 / (24059 + 27205)                             # Virginia Power 2025-12-31, ex securitization

def mean(d): return sum(d[y] for y in Y) / len(Y)

ocf_c = {y: ocf[y] - disc_ocf[y] for y in Y}
da_c = {y: da_seg[y] + nucfuel[y] for y in Y}
capex_c = {y: capex_seg[y] - max(corp_capex[y] - CORP_OWN, 0) for y in Y}
capex_a = {y: capex_c[y] - stonepeak_contrib[y] - nci_sale[y] + dist_stonepeak[y] for y in Y}
net_ltd = {y: ltd_iss[y] - ltd_rep[y] for y in Y}
oe_m = {y: ocf_c[y] - sbc[y] - pref[y] - da_c[y] for y in Y}           # maintenance-only, equity-only
oe_all_nocredit = {y: ocf_c[y] - sbc[y] - pref[y] - capex_a[y] for y in Y}

print("year  OCFcont  D&Acont  capexAttr  netLTD  OE_maint  OE_all(no credit)")
for y in Y:
    print(y, ocf_c[y], da_c[y], capex_a[y], net_ltd[y], oe_m[y], oe_all_nocredit[y])
sum_capex_a = sum(capex_a.values()); sum_ltd = sum(net_ltd.values())
cap_credit = DEBT_SHARE * sum_capex_a
credit = min(sum_ltd, cap_credit)
print(f"debt share {DEBT_SHARE:.4f}; capex attributable sum {sum_capex_a}; net LTD sum {sum_ltd}; cap {cap_credit:.0f}; credit {credit:.0f}")
OEM = mean(oe_m)
OEALL = mean(oe_all_nocredit) + credit / 4
OEALL_CAP = mean(oe_all_nocredit) + cap_credit / 4
GROWTH_SPEND = mean(capex_a) - mean(da_c)
EQ_GROWTH_SPEND = GROWTH_SPEND - credit / 4
EQ_GROWTH_SPEND_CAP = GROWTH_SPEND - cap_credit / 4
print(f"mean OE maintenance-only {OEM:.0f}; mean OE all-spending with credit {OEALL:.0f} (credit at cap {OEALL_CAP:.0f})")
print(f"growth spending {GROWTH_SPEND:.0f}; equity-funded {EQ_GROWTH_SPEND:.0f} (at cap {EQ_GROWTH_SPEND_CAP:.0f})")

# growth shown: series changes sign -> halves
h1 = (oe_m[2022] + oe_m[2023]) / 2; h2 = (oe_m[2024] + oe_m[2025]) / 2
g_shown = (h2 / h1) ** 0.5 - 1
rh1 = (rev[2022] + rev[2023]) / 2; rh2 = (rev[2024] + rev[2025]) / 2
g_sales_halves = (rh2 / rh1) ** 0.5 - 1
g_sales_end = (rev[2025] / rev[2022]) ** (1 / 3) - 1
max_share = max(oe_m[y] / rev[y] for y in Y)
print(f"halves OE {h1:.0f} -> {h2:.0f}: shown growth {g_shown*100:.1f}%; sales growth halves {g_sales_halves*100:.2f}%, end-to-end {g_sales_end*100:.2f}%; max OE/sales {max_share*100:.1f}%")
oe10 = OEM * (1 + g_shown) ** 10; s10 = rev[2025] * (1 + g_sales_halves) ** 10
print(f"cap test: OE year 10 at shown growth {oe10:.0f} vs sales year 10 {s10:.0f}: share {oe10/s10*100:.0f}% > {max_share*100:.1f}% -> cut")
G = min(g_sales_halves, R)

def growth_case(base, g, spend, r):
    pv = sum((base * (1 + g) ** t - spend) / (1 + r) ** t for t in range(1, 11))
    tv = base * (1 + g) ** 10 / r / (1 + r) ** 10      # growth and growth spending stop after year ten
    return pv + tv

def nogrowth(base, r): return base / r

res = {}
for lab, r in (("long rate", R), ("ten percent", FLOOR)):
    ng = nogrowth(OEM, r); gc = growth_case(OEM, G, EQ_GROWTH_SPEND, r); gcc = growth_case(OEM, G, EQ_GROWTH_SPEND_CAP, r)
    res[lab] = (ng, gc, gcc)
    print(f"{lab}: no-growth maintenance {ng:.0f} = ${ng/SH:.2f}; growth case {gc:.0f} = ${gc/SH:.2f}; growth case, credit at cap {gcc:.0f} = ${gcc/SH:.2f}")
ng, gc, _ = res["ten percent"]
print(f"FAIR (equity-only, central) = ${(ng/SH + gc/SH)/2:.2f}")
print(f"yield at price, maintenance no-growth: {OEM/CAP*100:.2f}%  (market cap {CAP:.0f})")
# growth case IRR at the price
def irr():
    lo, hi = -0.5, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        v = growth_case(OEM, G, EQ_GROWTH_SPEND, mid) if mid > 0.001 else 1e18
        if v > CAP: lo = mid
        else: hi = mid
    return mid
print(f"growth case expected return at the price: {irr()*100:.2f}%")
print(f"all-spending equity-only owner cash at no growth (central credit): {OEALL:.0f}; at cap {OEALL_CAP:.0f}")

# all-equity beside
ati = mean(interest) * (1 - TAX)
NETDEBT = 4043 + 200 + 2462 + 46719 - 296; PREF = 991
base_ae = OEM + ati
for lab, r in (("long rate", R), ("ten percent", FLOOR)):
    ng = nogrowth(base_ae, r) - NETDEBT - PREF
    gc = growth_case(base_ae, G, GROWTH_SPEND, r) - NETDEBT - PREF
    print(f"ALL-EQUITY {lab}: no-growth ${ng/SH:.2f}; growth ${gc/SH:.2f}; (pre-interest base {base_ae:.0f}, after-tax interest {ati:.0f}, net debt {NETDEBT}, pref {PREF})")

# literal five-year consolidated window 2021-2025, as filed, no sale proceeds
L = dict(ocf=[4037, 3700, 6572, 5018, 5361], da=[2781, 3113, 3128, 2639, 2684], sbc=[42, 36, 44, 53, 46],
         pref=[68, 93, 81, 78, 44], capex=[5960 + 101, 7758, 10235, 12427 - 377 - 2558, 12653 - 1569 + 88 + 241],
         ltd=[6400 - 3750, 3577, -2363, 3253, 7175])
lm = sum(L["ocf"][i] - L["sbc"][i] - L["pref"][i] - L["da"][i] for i in range(5)) / 5
la = sum(L["ocf"][i] - L["sbc"][i] - L["pref"][i] - L["capex"][i] for i in range(5)) / 5 + min(sum(L["ltd"]), DEBT_SHARE * sum(L["capex"])) / 5
print(f"LITERAL 2021-25: OE maintenance {lm:.0f} (no-growth ${lm/R/SH:.2f}); OE all-spending with credit {la:.0f}")

# signed deal beside: 0.8138 NEE + $0.41, combined maintenance-only owner cash, no growth
nee_ocf = [7553, 8262, 11301, 13260, 12485]; nee_da = [3924, 4503, 5879, 5462, 6580]; nee_sbc = [119, 142, 139, 138, 185]
nee_m = sum(nee_ocf[i] - nee_sbc[i] - nee_da[i] for i in range(5)) / 5
comb_sh = 2085.803189 + 0.8138 * SH
per_d = (OEM + nee_m) / comb_sh * 0.8138
print(f"DEAL: NEE maintenance-only OE {nee_m:.0f}; combined shares {comb_sh:.1f}M; per D share OE {per_d:.3f}; no-growth at long rate ${per_d/R+0.41:.2f}; at ten percent ${per_d/FLOOR+0.41:.2f}; market value 0.8138 x 79.80 + 0.41 = ${0.8138*79.80+0.41:.2f}")
