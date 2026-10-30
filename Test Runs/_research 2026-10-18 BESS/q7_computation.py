# COMPUTATION, NOT A CLEARANCE (the file closed at Q1). Q7's range convention and Part VII's fair price, arithmetic only.
oc = {2021: -298853, 2022: -789344, 2023: -894586, 2024: -1675224, 2025: -3252489}   # owner cash, all spending
growth_spend = {2021: 25000, 2025: 1678320}                                         # project rights bought (investing)
sov, floor = 0.0543, 0.10
net_cash = 9377141            # 10-Q 2026-06-30: cash 9,377,141; borrowings 0; operating lease left out
sh, sh_cover = 7397573, 7097573
def case(base_all, base_maint, label):
    print(f"--- {label}: base all-spending {base_all:,.0f}  maintenance-only {base_maint:,.0f}")
    for name, b in (("bottom (all spending, no growth)", base_all), ("top (maintenance only, no growth)", base_maint)):
        v = b / sov
        print(f"{name}: PV at {sov:.2%} {v:,.0f}; all-equity {v+net_cash:,.0f} = {(v+net_cash)/sh:.2f}/sh ({(v+net_cash)/sh_cover:.2f} cover); equity-only {v/sh:.2f}/sh")
    ends10 = [base_all / floor, base_maint / floor]
    fair_all = (sum(ends10) / 2 + net_cash)
    print(f"fair price (ends at 10%, averaged): all-equity {fair_all:,.0f} = {fair_all/sh:.2f}/sh ({fair_all/sh_cover:.2f} cover); equity-only {sum(ends10)/2/sh:.2f}/sh")
yrs = sorted(oc)
mean_all = sum(oc.values()) / 5
mean_maint = sum(oc[y] + growth_spend.get(y, 0) for y in yrs) / 5
case(mean_all, mean_maint, "five-year window 2021-2025 (literal)")
b_all = (oc[2024] + oc[2025]) / 2
b_maint = (oc[2024] + oc[2025] + growth_spend[2025]) / 2
case(b_all, b_maint, "BESS era 2024-2025 (beside)")
print("halves:", (oc[2021]+oc[2022])/2, (oc[2024]+oc[2025])/2)
print("market cap cover", sh_cover*2.21, "with pre-funded", sh*2.21)
