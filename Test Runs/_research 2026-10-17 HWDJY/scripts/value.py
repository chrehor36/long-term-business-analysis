# Q7 arithmetic for HWDJY. GBP m unless stated.
import csv
rows = {int(r['year']): r for r in csv.DictReader(open('data_filed.csv'))}
F = lambda y,k: float(rows[y][k])
rate = {y: (0.19 if y <= 2022 else (0.235 if y == 2023 else 0.25)) for y in rows}
rate[2015] = 0.2025; rate[2016] = 0.20; rate[2017] = 0.1925
def oc(y, basis='charge', pension_addback=True):
    a = F(y,'cfo') - F(y,'capex') + F(y,'disposals') - F(y,'lease_principal') - F(y,'interest_paid') - F(y,'sbc')
    if basis == 'charge': a += F(y,'tax_paid') - F(y,'tax_cy_basis')
    pe = F(y,'pension_cash_excess')
    if pension_addback and pe > 0: a += pe * (1 - rate[y])
    return a
def value(base, g, d, years=10):
    v = 0.0; c = base
    for t in range(1, years+1):
        c *= (1+g); v += c / (1+d)**t
    return v + c / d / (1+d)**years      # zero nominal growth after year ten
S = {y: oc(y) for y in rows}
print("Series S (tax-charge basis, pension deficit repair added back after tax):")
for y in sorted(S): print(y, round(S[y],1), f"{100*S[y]/F(y,'revenue'):.1f}% of sales", " | as filed", round(oc(y,'cash',False),1))
acq_w = sum(F(y,'acq') for y in range(2021,2026))/5
lit = sum(S[y] for y in range(2021,2026))/5
cyc_years = range(2018, 2024)   # trough 2018 to the year before trough 2024
cyc = sum(S[y] for y in cyc_years)/len(cyc_years)
acq_c = sum(F(y,'acq') for y in cyc_years)/len(cyc_years)
h1 = sum(S[y] for y in range(2015,2020))/5; h2 = lit
g = (h2/h1)**(1/6) - 1
rv1 = sum(F(y,'revenue') for y in range(2015,2020))/5; rv2 = sum(F(y,'revenue') for y in range(2021,2026))/5
gs = (rv2/rv1)**(1/6) - 1
lit_g = (S[2025]/S[2021])**(1/4) - 1
print(f"\nliteral window 2021-25 avg {lit:.1f}, acquisitions/yr {acq_w:.1f} -> {lit-acq_w:.1f}; literal end-to-end growth {100*lit_g:.1f}%")
print(f"cycle base 2018-2023 avg {cyc:.1f}, acquisitions/yr {acq_c:.1f} -> {cyc-acq_c:.1f}")
print(f"halves: 2015-19 avg {h1:.1f}, 2021-25 avg {h2:.1f}, growth {100*g:.2f}%/yr; sales halves {rv1:.0f}->{rv2:.0f} {100*gs:.2f}%/yr")
sov = 0.057225; FLOOR = 0.10
base = cyc - acq_c
# DIY Kitchens: closed 23 Jun 2026, valued on its own filed record (2025 revenue 136, EBIT 37, five-year revenue growth 17%).
diy_base = 37 * (1 - 0.25)     # disclosed guess: capex = depreciation, no working-capital draw (customer prepayment), UK 25% tax
diy_g = 0.17
# Net debt: 13 Jun 2026 cash 332.8; DIY cash out c.300; term loan 240 drawn; buyback after 13 Jun est. 8.65m shares x ~765p
buyback_after = 8.65 * 7.65
cash = 332.8 - 300 + 240 - buyback_after
net_debt = 240 - cash
pension = 16.9
nd_all = net_debt + pension
shares = 541.95
fx = 1.3253
def ps(whole): return 100 * (whole - nd_all) / shares   # pence per share
out = {}
for lab, d in [('sovereign', sov), ('ten percent', FLOOR)]:
    lo_h = value(base, 0.0, d); hi_h = value(base, g, d)
    lo_d = value(diy_base, 0.0, d); hi_d = value(diy_base, diy_g, d)
    out[lab] = (lo_h, hi_h, lo_d, hi_d)
    print(f"\n[{lab} {100*d:.3f}%] Howden no-growth {lo_h:.0f}, shown growth {hi_h:.0f}; DIY no-growth {lo_d:.0f}, 17% {hi_d:.0f}")
    print(f"   whole-business ends {lo_h+lo_d:.0f} to {hi_h+hi_d:.0f}; per share {ps(lo_h+lo_d):.0f}p to {ps(hi_h+hi_d):.0f}p; ex-DIY-growth top {ps(hi_h+lo_d):.0f}p")
lo, hi = ps(out['sovereign'][0]+out['sovereign'][2]), ps(out['sovereign'][1]+out['sovereign'][3])
flo, fhi = ps(out['ten percent'][0]+out['ten percent'][2]), ps(out['ten percent'][1]+out['ten percent'][3])
fair = (flo+fhi)/2
print(f"\nnet debt {net_debt:.1f} (cash {cash:.1f}), pension deficit {pension}, total {nd_all:.1f}; shares {shares}m")
print(f"RANGE {lo:.0f}p to {hi:.0f}p (width {hi/lo:.2f}x); per ADS US${4*lo/100*fx:.2f} to US${4*hi/100*fx:.2f}")
print(f"FAIR (all-equity) {fair:.0f}p = US${4*fair/100*fx:.2f} per ADS; ends at 10%: {flo:.0f}p / {fhi:.0f}p")
# equity-only: owner cash after interest (add interest received on cash ~ net of term loan interest)
# equity-only adds net interest to owner cash and ignores net debt
ni = 13.2*0.75 - 0   # 2025 interest received after tax as the window's latest; term loan interest c.9/yr guided
eq_base = base + (sum(F(y,'interest_recd') for y in range(2021,2026))/5)*0.75 - 9*0.75
lo_e = value(eq_base,0,FLOOR)+out['ten percent'][2]; hi_e = value(eq_base,g,FLOOR)+out['ten percent'][3]
print(f"equity-only fair {100*(lo_e+hi_e)/2/shares:.0f}p (base {eq_base:.1f})")
# sensitivities at 10% (floor test): which case earns the floor at 788p?
print("\nfloor-test sensitivities (top case value at 10%, pence):")
for name, b, gg in [('central', base, g), ('literal window base, halves growth', lit-acq_w, g),
                    ('as-filed cash tax, cycle base', sum(oc(y,'cash',False) for y in cyc_years)/6 - acq_c, g),
                    ('cycle base, sales growth 8.5%', base, gs)]:
    print(f"  {name}: base {b:.1f}, g {100*gg:.2f}% -> {ps(value(b,gg,FLOOR)+out['ten percent'][3]):.0f}p")

# (e) maintenance case: owned depreciation as the maintenance guess over the cycle years
capx = sum(F(y,'capex') for y in cyc_years)/6; dep = sum(F(y,'da_owned') for y in cyc_years)/6
M = base + (capx - dep)
print(f"\n(e) cycle-years capex avg {capx:.1f}, owned D&A avg {dep:.1f}; maintenance-only base {M:.1f}")
for lab, d in [('sovereign', sov), ('ten percent', FLOOR)]:
    mng = value(M, 0, d); agr = value(base, g, d); ang = value(base, 0, d)
    lo_d = value(diy_base, 0, d); hi_d = value(diy_base, diy_g, d)
    bot = min(mng, agr) + lo_d; top = max(mng, agr) + hi_d
    print(f"[{lab}] maint no-growth {mng:.0f} | all-spend shown growth {agr:.0f} | all-spend no growth {ang:.0f}")
    print(f"   RANGE (e) whole {bot:.0f} to {top:.0f}; per share {ps(bot):.0f}p to {ps(top):.0f}p; per ADS US${4*ps(bot)/100*fx:.2f} to US${4*ps(top)/100*fx:.2f}; width {ps(top)/ps(bot):.2f}x")
    if lab == 'ten percent':
        fair_e = (ps(bot)+ps(top))/2
        print(f"   FAIR (e, all-equity) {fair_e:.0f}p, US${4*fair_e/100*fx:.2f} per ADS")
        Me = M + (sum(F(y,'interest_recd') for y in range(2021,2026))/5)*0.75 - 9*0.75
        be = Me - M + base
        botq = min(value(Me,0,d), value(be,g,d)) + lo_d; topq = max(value(Me,0,d), value(be,g,d)) + hi_d
        fe = 100*((botq+topq)/2)/shares
        print(f"   equity-only fair {fe:.0f}p, US${4*fe/100*fx:.2f} per ADS (no net debt deducted; net interest added)")
# literal window beside
print(f"\nliteral window: base {lit-acq_w:.1f}, end-to-end growth {100*lit_g:.1f}% (decline carried as bottom per (b))")
for lab, d in [('sovereign', sov), ('ten percent', FLOOR)]:
    print(f"  [{lab}] no growth {ps(value(lit-acq_w,0,d)+value(diy_base,0,d)):.0f}p ; decline {ps(value(lit-acq_w,lit_g,d)+value(diy_base,0,d)):.0f}p")
