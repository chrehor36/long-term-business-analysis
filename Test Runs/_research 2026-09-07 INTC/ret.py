import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# [E2-43] return on UNLEVERAGED NET TANGIBLE OPERATING ASSETS
# = pre-tax operating income / (total assets - goodwill - intangibles - cash&STI - non-debt current liabs)
rows = {
# yr: assets, goodwill, intang, cash, sti, current_liabs, short_debt, equity, op_income
2019: (136524, 26276, 10827,  4194, 1082, 22310, 3693,  77504, 22035),
2020: (153091, 26971,  9026,  5865,2292+0, 24754, 2504,  81038, 23678),
2021: (168406, 26963,  7270,  4827,26193, 27462, 4591,  95391, 19456),
2022: (182103, 27591,  6018, 11144,17194, 32155,  423, 101423,  2334),
2023: (191572, 27591,  4589,  7079,17955, 28053, 2288, 105590,    93),
2024: (196485, 24693,  3691,  8249,13813, 35666, 3729,  99270,-11678),
2025: (211429, 23912,  2772, 14265,23151, 31575, 2499, 114281, -2214),
}
print(f"{'yr':>5} {'op inc':>8} {'unlev NTOA':>11} {'return %':>9}")
for y,(A,G,I,C,S,CL,SD,E,OI) in rows.items():
    ntoa = A - G - I - C - S - (CL - SD)
    print(f"{y:>5} {OI:8,} {ntoa:11,} {OI/ntoa*100:9.1f}")

print()
print('=== [E2-56] INCREMENTAL, never the blended ===')
capex = {2021:18733,2022:24844,2023:25750,2024:25122,2025:17672}
print('  capex FY2021-25 total:', f"{sum(capex.values()):,}")
print('  + Ireland SCIP buy-back Apr-2026 (cash, real):', '14,200')
print('  operating income FY2020 23,678 -> FY2025 (2,214):  delta (25,892)')
print('  operating income FY2020 23,678 -> TTM:')
# TTM operating income: FY2025 -2214 ; H1-2025 -3477 ; H1-2026 -1340 -> TTM = -2214 +3477 -1340
print('     TTM op income =', -2214 + 3477 - 1340)
print('  gross profit  FY2020 43,612 -> FY2025 18,375: delta (25,237)')
# TTM gross profit
print('     TTM gross profit =', 18375 - 8214 + 11856)
print()
print('=== [E2-54] with GROSS interest (capitalised interest counts: "both payable and accrued") ===')
gross_int = {2023: 878+1500, 2024: 1034+1500, 2025: 1091+1200}
for y,gi in gross_int.items():
    pass
print('  interest incurred: 2023', 878+1500, '| 2024', 1034+1500, '| 2025', 1091+1200)
ttm_ocf, ttm_cap = 14936, 14592
print(f"  TTM: OCF {ttm_ocf:,} - capex {ttm_cap:,} = {ttm_ocf-ttm_cap:,}")
for lbl, gi in [('net (P&L) interest ~1,100', 1100), ('GROSS interest incurred ~2,300', 2300)]:
    print(f"    vs {lbl}: coverage {(ttm_ocf-ttm_cap)/gi:.2f}x")
print()
print('=== twelve-month claims from the Jun-27-2026 balance sheet ===')
claims = {
 'short-term debt (balance sheet)': 1988,
 'interest incurred (TTM run-rate, gross)': 2300,
 'capital expenditure (TTM actual; FY26 commitment was 9,100)': 14592,
 'other purchase obligations committed for 2026 (FY25 10-K)': 2200,
 'Mentee Robotics (Mobileye, signed Jan-2026)': 900,
}
print('  CONTRACTUAL / RUN-RATE SUBTOTAL:', f"{sum(claims.values()):,}")
for k,v in claims.items(): print(f"    {k:<62} {v:8,}")
print(f"  + Arizona SCIP NCI at the Ireland precedent (carrying {13428:,}, Ireland paid 14,200 on a 112 carrying value)  ~14,000")
res = 29727 + 14936
print(f"  RESOURCES: cash+STI 29,727 + TTM OCF 14,936 = {res:,}")
print(f"  cover WITHOUT an Arizona buy-out: {res/sum(claims.values()):.2f}x")
print(f"  cover WITH    an Arizona buy-out: {res/(sum(claims.values())+14000):.2f}x")
print()
print('=== yields at the price ===')
CAP = 5115*95.80
for lbl, oe in [('TTM capex end', -2049), ('TTM D&A end', 1108), ('5-yr capex end', -10403),
                ('5-yr D&A end', 2094), ('10-yr capex end', 1538), ('10-yr D&A end', 10470),
                ('pre-collapse FY2016-20 capex end', 13479), ('FY2020 alone, D&A end (best year ever)', 23528),
                ('Intel Products segment op income FY2025, taxed at 21%', int(12739*0.79))]:
    print(f"  {lbl:<50} {oe:9,}  yield {oe/CAP*100:6.2f}%")
print(f"  market cap used: {CAP:,.0f}")
