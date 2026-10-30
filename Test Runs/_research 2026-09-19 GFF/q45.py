# GFF Q4/Q5 arithmetic. Inputs hand-transcribed from filed statements (thousands USD):
# recast FY2025 annual report, 8-K 0001628280-26-054906 (continuing cash-flow statement, FY2023-25)
# Q3 FY2026 10-Q 0001628280-26-053536 (nine months to 2026-06-30 and 2025-06-30)
# Arithmetic only. It concludes nothing.
ocf  = {2023: 332826, 2024: 307370, 2025: 307794}
sbc  = {2023: 39178,  2024: 25570,  2025: 24191}
capx = {2023: 31445,  2024: 50279,  2025: 41692}
dep  = {2023: 20925,  2024: 21607,  2025: 23892}   # depreciation only (recast Note: "Depreciation expense")
int_paid = {2023: 99833, 2024: 100676, 2025: 92887}
m9 = dict(ocf26=217944, ocf25=234516, sbc26=20652, sbc25=16898, cap26=23736, cap25=32498)

print("OE by year (OCF - SBC - c)")
lo, hi = [], []
for y in (2023, 2024, 2025):
    a = ocf[y] - sbc[y] - capx[y]; b = ocf[y] - sbc[y] - dep[y]
    lo.append(a); hi.append(b)
    print(y, "capex end", a, "| depreciation end", b, "| capex/dep", round(capx[y]/dep[y], 2))
m_lo, m_hi = sum(lo)/3, sum(hi)/3
print("3-yr mean capex end", round(m_lo), "depreciation end", round(m_hi))
ttm_ocf = ocf[2025] + m9['ocf26'] - m9['ocf25']
ttm_sbc = sbc[2025] + m9['sbc26'] - m9['sbc25']
ttm_cap = capx[2025] + m9['cap26'] - m9['cap25']
ttm = ttm_ocf - ttm_sbc - ttm_cap
print("TTM to 2026-06-30: OCF", ttm_ocf, "SBC", ttm_sbc, "capex", ttm_cap, "OE", ttm)

# Pro forma interest (disclosed judgment): AMES cash applied to debt, $100,000 (June) + $180,910 (July)
# at the Term Loan B rate 5.66%; refinancing $974,775 @5.75% -> $800,000 @6.25% + remainder on revolver @5.51%
tax = 0.28  # the company's guided normalized rate
save_ames = 280910 * 0.0566
refi = (800000*0.0625 + (974775-792000)*0.0551) - 974775*0.0575
adj3 = (save_ames - refi) * (1 - tax)
adj_ttm = (180910*0.0566 - refi) * (1 - tax)
print("pro forma interest adj: 3-yr", round(adj3), "TTM", round(adj_ttm), "(refi cost pre-tax", round(refi), ")")

price, shares = 93.22, 45294716
cap = price * shares / 1000
nonop = 118600 + 20896 + 161100 + 48593   # equity-method carrying values + PIK principal
print("cap $k", round(cap), "non-operating carrying", nonop)
cons = [("conservative: TTM, capex end, JV/PIK at 50%", ttm + adj_ttm, 0.5),
        ("default: 3-yr mean, capex end, JV/PIK at 75%", m_lo + adj3, 0.75),
        ("generous: 3-yr mean, depreciation end, JV/PIK at 100%", m_hi + adj3, 1.0)]
for name, oe, h in cons:
    opcap = cap - nonop*h
    y = oe/opcap
    g_floor = (0.10 - y)/(1 + y)
    g_bond = (0.0534 - y)/(1 + y)
    print(f"{name}: OE {oe:,.0f}  op-cap {opcap:,.0f}  yield {y:.2%}  vs bond {y-0.0534:+.2%}  g for 10% floor {g_floor:.2%}  g for bond {g_bond:.2%}")
    for g in (0.0, 0.025, 0.035):
        v = oe*(1+g)/(0.10-g) + nonop*h
        print(f"   value at the 10% floor, g={g:.1%}: ${v/1000:,.0f}M  ${v/shares*1000:,.0f}/share")

# Q4: coverage [E2-54]
for y in (2023, 2024, 2025):
    print(y, "cash for interest after capex / interest paid", round((ocf[y] + int_paid[y] - capx[y]) / int_paid[y], 2))
# Named death, margin reversion: HBP FY2025 revenue 1,584,182; FY2025 margin 30.1% vs FY2021 15.7%
full = 1584182 * (0.301 - 0.157); half = full/2
print("reversion pre-tax: full", round(full), "half", round(half), "after tax full", round(full*(1-tax)), "half", round(half*(1-tax)))
ebit = 173866 + 243612
print("continuing EBIT FY2025 pre-impairment", ebit, "after full reversion", round(ebit-full), "after half", round(ebit-half))
# Named death, housing depression: revenue -25%, decremental at FY2025 continuing gross margin 47.2%
dd = 1795384 * 0.25 * 0.472
print("depression: EBIT falls", round(dd), "to", round(ebit-dd))
