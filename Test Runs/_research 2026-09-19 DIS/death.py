# Q4: the named way this business dies, quantified from filed figures. [E2-27, E3-24, E4-40]
# All figures FY2025 10-K accession 0001744489-25-000155 unless marked.

# --- strength 3: near-term cash requirements, FY2026 ---
debt_mat_26, interest_26 = 6751, 1559          # Note 8 scheduled maturity table
commit_26 = 17007                              # Note 14: sports 9,894 + other prog 2,951 + other 4,162
capex_26  = 9000                               # MD&A guidance "approximately $9 billion"
div_26    = 2400                               # $1.50/share annualised x ~1.73bn shares, approx
buyback_26= 9000                               # FY2026 Q3 EX-99.1: "at least $9 billion"
ocf_26    = 19000                              # MD&A/8-K guidance "at least $19 billion"
print('FY2026 intended and contracted outflow vs guided operating cash flow, $M')
print(f'  debt maturities                 {debt_mat_26:>7,}')
print(f'  interest on borrowings          {interest_26:>7,}')
print(f'  programming + other commitments {commit_26:>7,}   (Note 14, FY2026 column)')
print(f'  capital expenditure (guided)    {capex_26:>7,}')
print(f'  dividends (approx)              {div_26:>7,}')
print(f'  buyback target                  {buyback_26:>7,}   ("at least $9 billion")')
print(f'  TOTAL                           {debt_mat_26+interest_26+commit_26+capex_26+div_26+buyback_26:>7,}')
print(f'  guided operating cash flow      {ocf_26:>7,}   ("at least $19 billion")')
print()
noncancel = debt_mat_26 + interest_26 + capex_26
print(f'  of which NON-CANCELLABLE and non-operating (debt service + capex): {noncancel:,}')
print(f'  discretionary (dividends + buyback):                              {div_26+buyback_26:,}')
print('  (the programming commitments are the operating cost base and already sit inside OCF)')
print()
# --- [E2-54] coverage test: interest out of cash flow NET OF AMPLE CAPEX ---
for lab, ocf, capex, interest in [('FY2025 actual', 18101, 8024, 2050),
                                  ('FY2024 actual', 13971, 5412, 2134),
                                  ('FY2026 guided', 19000, 9000, 2050)]:
    print(f'[E2-54] {lab}: (OCF {ocf:,} - capex {capex:,}) / interest paid {interest:,} = '
          f'{(ocf-capex)/interest:.1f}x')
print()
# --- the death, quantified ---
espn_dom_rev, espn_dom_oi = 16085, 2801
affil = 11944                       # ESPN affiliate and subscription fees, total (dom 11,913 + Star 31)
linear_oi = 2955
seg_oi_total = 17551
rights_26 = 9894                    # contracted sports rights due FY2026
rights_total = 84076
print('THE DEATH: the contracted cost stays and the fee-paying base leaves.')
print(f'  ESPN domestic operating income {espn_dom_oi:,} on revenue {espn_dom_rev:,}; '
      f'costs therefore {espn_dom_rev-espn_dom_oi:,}, of which contracted programming 12,492')
for pct in (5, 10, 15, 23.5):
    hit = affil*pct/100
    print(f'  a {pct:>4}% fall in ESPN affiliate and subscription fees = {hit:7,.0f} '
          f'-> ESPN domestic OI {espn_dom_oi-hit:7,.0f} ({(espn_dom_oi-hit)/espn_dom_oi-1:+.0%})')
print(f'  wipe-out point: {espn_dom_oi/affil*100:.1f}% fall in affiliate and subscription fees')
import math
print(f'  at the filed 7% annual unit decline with rate rises no longer offsetting, '
      f'{espn_dom_oi/affil*100:.1f}% arrives in {math.log(1-espn_dom_oi/affil)/math.log(0.93):.1f} years')
print()
exposed = espn_dom_oi + linear_oi
print(f'  combined exposure: ESPN domestic OI {espn_dom_oi:,} + Linear Networks OI {linear_oi:,} '
      f'= {exposed:,} = {exposed/seg_oi_total:.1%} of segment operating income')
print(f'  against contracted sports rights of {rights_26:,} due FY2026 and {rights_total:,} signed, '
      f'which do not fall with it')
print(f'  signed commitments 104,088 vs market cap 177,279 = {104088/177279:.0%} of the cap')
