"""R2 arithmetic, analyst B. All figures $ thousands, from the segment notes of the 10-Ks named in the output file.
Every input is typed from the filed segment table; the source line is in the comment."""
def pct(a,b): return 100.0*a/b
print("BASIS A: each company's segment Adjusted EBITDA as its CODM measures it (both exclude D&A, stock pay, impairment, deal costs)")
# Malibu: 10-K FY2026 note 20 (FY2024-26); 10-K FY2025 note 19 (FY2023)
mb={2023:(186873,636247),2024:(42579,279131),2025:(60611,312698),2026:(50674,312907)}
# MasterCraft: 10-K FY2026 note 16 (FY2024-26, Performance and Wake = former MasterCraft segment); 10-K FY2025 note (FY2023)
mc={2023:(110292,468656),2024:(38862,262736),2025:(29771,240763),2026:(45855,271177)}
for y in sorted(mb):
    a,b=mb[y]; c,d=mc[y]; print(f" FY{y}: Malibu {a:,}/{b:,} = {pct(a,b):.2f}%   MasterCraft {c:,}/{d:,} = {pct(c,d):.2f}%   gap {pct(a,b)-pct(c,d):+.2f} pts")
print()
print("BASIS B: segment profit fully loaded as each filed it, plus segment D&A (Malibu: pre-tax income before FY2025 basis change; MasterCraft: operating income)")
# Malibu segment pre-tax + D&A: 10-K FY2021 note 19 (FY2019-21), FY2023 note 19 (FY2022-23), FY2024 note 19 (FY2024)
mbB={2019:(54160,7674,374611),2020:(55567,8809,354769),2021:(88511,9397,483525),2022:(137133,8398,607543),2023:(40157,8974,636247),2024:(-11589,9714,279131)}
# MasterCraft segment operating income + D&A: FY2019 from 10-K FY2021 (includes Aviara); FY2020-21 from 10-K FY2022 (Aviara split out);
# FY2022-23 10-K FY2023; FY2024 10-K FY2024; FY2025-26 computed from 10-K FY2026 note 16 (net sales - cost of sales - operating expenses)
mcB={2019:(53989,3481,311830),2020:(35833,4078,236856),2021:(73354,4479,350812),2022:(105341,4968,466027),2023:(101324,5555,468656),
     2024:(29573,5109,262736),2025:(240763-183180-36925,5888,240763),2026:(271177-194514-55125,5837,271177)}
for y in sorted(mcB):
    c,dd,d=mcB[y]; s=f" FY{y}: MasterCraft OI {c:,} + D&A {dd:,} = {c+dd:,} on {d:,} = {pct(c+dd,d):.2f}%"
    if y in mbB:
        a,da,b=mbB[y]; s+=f"   Malibu pre-tax {a:,} + D&A {da:,} = {a+da:,} on {b:,} = {pct(a+da,b):.2f}%"
    else: s+="   Malibu: not filed on this basis after FY2024"
    print(s)
print()
print("FY2026 RECONCILIATIONS (the OUT fact year)")
mal_ebitda, mal_sales = 50674, 312907
corp, interest, acq = 51030, 3559, 14773       # Malibu 10-K FY2026: corporate expenses and other; interest expense; acquisition and integration
corp_ex_int = corp-interest
legacy_sales = 312907+284006+233374            # segments that receive corporate allocations (Saxdor not yet allocated, note 20 fn 4)
tot_sales = 914590
mc_oi, mc_da, mc_sales, mc_adj = 21538, 5837, 271177, 45855
mc_deal = 15249                                 # MasterCraft 10-K FY2026 note 16: Marine Products Transaction costs (in G&A)
print(f" MasterCraft P&W operating income + D&A = {mc_oi+mc_da:,} / {mc_sales:,} = {pct(mc_oi+mc_da,mc_sales):.2f}%  (the run's pre-registered MasterCraft measure)")
print(f" MasterCraft P&W adjusted EBITDA = {mc_adj:,} / {mc_sales:,} = {pct(mc_adj,mc_sales):.2f}%")
print(f" MasterCraft P&W adjusted EBITDA less all of ERP ($999K) and leadership transition ($196K), worst case for MasterCraft = {mc_adj-999-196:,} = {pct(mc_adj-999-196,mc_sales):.2f}%")
print(f" Malibu segment adjusted EBITDA = {pct(mal_ebitda,mal_sales):.2f}%  (the run's pre-registered Malibu measure)")
print(f" Malibu corporate expenses and other ex interest = {corp_ex_int:,}")
for lab,share in [("share of total net sales",mal_sales/tot_sales),("share of allocated (legacy) net sales",mal_sales/legacy_sales),("all of it, MasterCraft's practice",1.0)]:
    x=mal_ebitda-share*corp_ex_int
    print(f"   Malibu, OI+D&A basis, corporate charged by {lab} ({share:.4f}): {x:,.0f} = {pct(x,mal_sales):.2f}%")
for lab,share in [("share of total net sales",mal_sales/tot_sales),("share of allocated (legacy) net sales",mal_sales/legacy_sales)]:
    x=mal_ebitda-share*(corp_ex_int-acq); y=mc_oi+mc_da+mc_deal
    print(f"   Deal costs out of both: Malibu {pct(x,mal_sales):.2f}% ({lab})  vs MasterCraft OI+D&A+deal costs {y:,} = {pct(y,mc_sales):.2f}%")
