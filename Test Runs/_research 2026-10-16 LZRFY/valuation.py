"""Q7 COMPUTATION, NOT A CLEARANCE (file closed OUT at Q2). BRL millions unless stated.
Range by Q7's convention: base = five-year (FY2021-FY2025, combined basis) average owner cash after maintenance only
(spec e), shown growth carried ten years then zero nominal growth, discounted at the long government rate; growth case
charges the growth spending the growth requires (k = incremental tangible capital per BRL of added owner cash)."""
r_gov = 0.1287          # Tesouro Prefixado com Juros Semestrais 01/01/2037, buy rate, 15/10/2026 (Tesouro Nacional)
B = 4186.0               # owner_cash.py: average 2021-2025, maintenance only, all-equity, tax 34% x (EBIT - IOC)
g = 0.083                # shown growth, between the halves of the window (2021-22 avg to 2024-25 avg)
g_lit = 0.129            # literal end-to-end growth 2021->2025, shown beside
# incremental tangible capital 2021->2025 (combined): end-2021 Localiza 15,041 less intangibles 143 + Locamerica 12,221
# less intangibles 1,217 = 25,902; less carve-out proceeds 3,879 returned = 22,023; end-2025 58,542 less 8,874 = 49,668
dK = 49668.0 - 22023.0
dOC = 5482.0 - 3371.0
k = dK/dOC
net_debt = 32352.0       # company-defined net debt at 06/30/2026 (2Q26 release; ITR balance sheet), subsequent events: debt exchange only
shares = 1104.614922     # million, 06/30/2026: 1,124,259,345 issued less 19,644,423 treasury (ITR 2Q26)
price = 49.69
mcap = 1064.036631*49.69 + 40.578291*48.20
ev = mcap + net_debt
def no_growth(B, r): return B/r
def growth_case(B, g, r, k, years=10):
    pv=0; oc_prev=B
    for t in range(1,years+1):
        oc = B*(1+g)**t
        net = oc - k*(oc-oc_prev)
        pv += net/(1+r)**t; oc_prev=oc
    pv += (oc_prev/r)/(1+r)**years
    return pv
def plain_growth(B,g,r,years=10):   # all spending NOT charged: shown only to bound the arithmetic
    pv=sum(B*(1+g)**t/(1+r)**t for t in range(1,years+1)); return pv + (B*(1+g)**years/r)/(1+r)**years
out=[]
def line(lbl, ev_val):
    eq = ev_val-net_debt; out.append(f'{lbl:70s} EV {ev_val:9.0f}  equity {eq:9.0f}  per share BRL {eq/shares:7.2f}')
line('No-growth case (maintenance owner cash), at gov rate 12.87%', no_growth(B,r_gov))
line('Growth case 8.3pct, growth spending charged (k=%.1f), at 12.87pct' % k, growth_case(B,g,r_gov,k))
line('Literal growth 12.9%, growth spending charged, at 12.87%', growth_case(B,g_lit,r_gov,k))
line('[bound only] Growth 8.3% with NO growth spending charged, at 12.87%', plain_growth(B,g,r_gov))
line('FAIR: no-growth case at 10%', no_growth(B,0.10))
line('FAIR: growth case at 10%', growth_case(B,g,0.10,k))
fair_ev = (no_growth(B,0.10)+growth_case(B,g,0.10,k))/2
line('FAIR PRICE (average of the two ends at 10%), all-equity basis', fair_ev)
# equity-only: owner cash after after-tax interest. Net financial expense avg 2023-2025 = (4024.3+3938.7+4613.8)/3
nfe = (4024.3+3938.7+4613.8)/3; Beq = B - nfe*(1-0.34)
eq_ng = Beq/0.10
k_eq = k  # same capital need, but financed as the business is (shown on equity only for reference)
eq_g = growth_case(Beq, g, 0.10, k)
out.append(f'Equity-only owner cash = {B:.0f} - {nfe:.0f} x 0.66 = {Beq:.0f}; no-growth at 10% {eq_ng:.0f}, growth at 10% {eq_g:.0f}; fair equity-only per share BRL {(eq_ng+eq_g)/2/shares:.2f}')
out.append(f'Market cap {mcap:.0f}; EV {ev:.0f}; owner cash yield on EV (no-growth) {B/ev:.3%}; k = {k:.2f}; incremental after-tax return on capital 2021->2025 = {dOC/dK:.3%}')
# sensitivity: 1H26 run rate, cash-tax basis (contrary evidence)
ebit_1h26 = 5057.4-282.4; run = 2*ebit_1h26
out.append(f'Sensitivity (not the base): 1H26 EBIT ex Voll gain annualized {run:.0f}; at 34% tax less 2025 IOC shield NOPAT {run - 0.34*(run-1755.6):.0f} = {(run - 0.34*(run-1755.6))/ev:.2%} of EV; at the 2025 cash tax (477) {(run-477)/ev:.2%} of EV')
print('\n'.join(out))
open('valuation_out.txt','w').write('\n'.join(out)+'\n')
