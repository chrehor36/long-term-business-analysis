"""AMBQ owner cash and the Q7 reporting computation (COMPUTATION, NOT A CLEARANCE). $ thousands, from the filed statements."""
# year: (operating cash, stock pay, capex, intangible purchases (IP licences), interest/other income net)
F = {
 2020: (-34639, 702, 2630, 1962, None),   # DRS/A 0000950123-22-012507
 2021: (-52881, 1290, 4623, 0, 43),       # DRS/A 0000950123-22-012507 (interest income 43; other expense 259 not interest)
 2023: (-26958, 2623, 459, 2562, 1020),   # DRS/A 0000950123-25-001897; other income 2023 from 424B4 0001193125-25-169401
 2024: (-21428, 5174, 658, 3073, 980),    # 10-K 0001193125-26-094004
 2025: (-19690, 6835, 1344, 6099, 3122),  # 10-K 0001193125-26-094004
}
H1_2026 = (-20678, 6919, 781, 5120)       # 10-Q 0001193125-26-344145
oc = {}
for y, (ocf, sbc, capex, ip, oth) in F.items():
    eq = ocf - sbc - capex - ip
    ae = eq - (oth or 0)
    oc[y] = (eq, ae)
    print(f"FY{y}: OCF {ocf:,} SBC {sbc:,} capex {capex:,} IP {ip:,} -> owner cash (equity-only) {eq:,}; all-equity (less interest/other income) {ae:,}")
print("H1 2026 owner cash:", H1_2026[0]-H1_2026[1]-H1_2026[2]-H1_2026[3])
win = [2021, 2023, 2024, 2025]   # literal window FY2021-FY2025; FY2022 statements never filed
eq_avg = sum(oc[y][0] for y in win)/len(win)
ae_avg = sum(oc[y][1] for y in win)/len(win)
print(f"window average, four filed years: equity-only {eq_avg:,.0f}; all-equity {ae_avg:,.0f}")
SOV = 0.056
SH = 24184536/1000         # thousands of shares, cover of 10-Q, as of 2026-08-07
NET_CASH = 366774          # cash and equivalents 2026-06-30; no borrowings; no finance leases; operating leases left out
PRICE = 58.56
for lab, avg, add in (("all-equity", ae_avg, NET_CASH), ("equity-only", eq_avg, 0)):
    v_sov = avg/SOV + add
    v_10 = avg/0.10 + add
    print(f"{lab}: no-growth value at {SOV:.1%}: {v_sov:,.0f}K = ${v_sov/SH:,.2f}/share; at 10%: {v_10:,.0f}K = ${v_10/SH:,.2f}/share")
print(f"market cap at ${PRICE}: {PRICE*SH:,.0f}K")

# Beside it: the window without FY2021 (the shortage year), FY2023-FY2025, to show that no base drawn from the filed
# years turns the sign of owner cash. Shown, not the central figure.
alt = [2023, 2024, 2025]
eq3 = sum(oc[y][0] for y in alt)/3
ae3 = sum(oc[y][1] for y in alt)/3
print(f"FY2023-FY2025 average: equity-only {eq3:,.0f}; all-equity {ae3:,.0f}")
for lab, avg, add in (("all-equity", ae3, NET_CASH), ("equity-only", eq3, 0)):
    v_sov = avg/SOV + add
    v_10 = avg/0.10 + add
    print(f"  {lab}: at {SOV:.1%}: ${v_sov/SH:,.2f}/share; at 10%: ${v_10/SH:,.2f}/share")
# margins
S = {2020: (50974, 21574, -20215), 2021: (91008, 30766, -25101), 2023: (65537, 19441, -51322),
     2024: (76067, 24291, -40613), 2025: (72514, 32095, -39543), 'H1 2026': (58961, 26158, -20416)}
for y, (r, g, o) in S.items():
    print(f"{y}: gross {g/r:.1%} operating {o/r:.1%}")
