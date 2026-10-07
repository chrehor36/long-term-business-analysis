"""Q2 competitor arithmetic on filed figures (HD 10-K 0001628280-26-019436; LOW 10-K 0000060667-26-000029)."""
hd_primary_sales, hd_primary_oi, hd_stores, hd_avg_sqft = 151966, 20574, 2359, 104000
low_sales, low_oi, low_acq_costs, low_sqft_m, low_stores = 86286, 10153, 321, 196, 1759
hd_sqft_m = hd_stores * hd_avg_sqft / 1e6
print(f"HD store sq ft (approx, stores x average) {hd_sqft_m:.1f}M")
print(f"HD Primary sales per sq ft ${hd_primary_sales/hd_sqft_m:,.0f}; LOW ${low_sales/low_sqft_m:,.0f}")
print(f"HD Primary sales per store ${hd_primary_sales/hd_stores:,.1f}M; LOW ${low_sales/low_stores:,.1f}M")
print(f"HD Primary op margin {100*hd_primary_oi/hd_primary_sales:.1f}%; LOW {100*low_oi/low_sales:.1f}%, "
      f"ex acquisition costs {100*(low_oi+low_acq_costs)/low_sales:.1f}%")
for y, (hs, ho), (ls, lo) in [("FY2023", (152669, 21689), (86377, 11557)), ("FY2024", (153108, 21313), (83674, 10466))]:
    print(y, f"HD Primary {100*ho/hs:.1f}%  LOW {100*lo/ls:.1f}%")
print(f"HD total FY2021 op margin {100*23040/151157:.1f}% vs LOW FY2021 {100*12093/96250:.1f}%")
print(f"Other segment: OI 316 + amortization 398 = {316+398} on sales 12717 = {100*(316+398)/12717:.1f}%; "
      f"on 23054 acquisition cash (FY2024 17644 + FY2025 5410) = {100*(316+398)/23054:.1f}% pre-tax")
