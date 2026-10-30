# LGN run 2026-10-17: arithmetic only. Every input is a filed figure (USD millions) with its source in comments.
# Sources: 10-K FY2025 acc 0002052568-26-000008 (2023-2025); IPO 424B4 acc 0001193125-25-202469 (2022);
# 10-Q Q2 2026 acc 0002052568-26-000026 (net debt, shares); 8-K/A acc 0001193125-26-114802 ex 99.1 (Bowers).
years = [2022, 2023, 2024, 2025]
ocf   = [26.996, 33.917, 29.268, 256.873]
sbc   = [5.185, 10.051, 5.411, 67.550]          # cash-flow statement add-back, all stock pay
sbc_co= [5.185, 10.051, 5.411, 3.192]           # 2025: RSUs and options only (statement of equity); earlier years as filed
capex = [26.312, 17.073, 19.008, 37.940]
finl  = [1.221, 1.937, 2.460, 3.843]            # finance lease principal (financing section)
acq   = [134.151, 119.882, 225.246, 16.497]     # consideration paid for acquisitions, net of cash acquired
cont  = [1.900, 5.520, 32.504, 0.0]             # contingent consideration paid (financing section)
intx  = [50.836, 68.196, 91.609, 101.778]       # interest expense, net of capitalized interest
dfa   = [5.535, 5.035, 5.052, 3.480]            # amortization of debt issuance costs (non-cash)
TAX = 0.2673   # CONVENTION of the run: the filer's own stated combined federal and state rate (10-K, TRA estimate)
rev   = [1246.501, 1615.062, 2098.602, 2550.491]
R = 0.0543     # 30-year Treasury par yield 2026-10-16, US Treasury
FLOOR = 0.10

def mean(x): return sum(x)/len(x)
eq_only = [o-s-c-f for o,s,c,f in zip(ocf,sbc,capex,finl)]
all_eq  = [e+(i-d)*(1-TAX) for e,i,d in zip(eq_only,intx,dfa)]
eq_only_co = [o-s-c-f for o,s,c,f in zip(ocf,sbc_co,capex,finl)]
all_eq_co  = [e+(i-d)*(1-TAX) for e,i,d in zip(eq_only_co,intx,dfa)]
purch = [a+c for a,c in zip(acq,cont)]
print("year  OCF   eq-only  all-equity  purchases  all-eq after purchases  OCF-share-of-sales")
for k,y in enumerate(years):
    print(y, round(ocf[k],1), round(eq_only[k],1), round(all_eq[k],1), round(purch[k],1), round(all_eq[k]-purch[k],1), f"{all_eq[k]/rev[k]:.1%}")
print("means: eq-only", round(mean(eq_only),1), " all-equity", round(mean(all_eq),1),
      " all-eq after purchases", round(mean([a-p for a,p in zip(all_eq,purch)]),1))
print("variant, company-funded stock pay only: eq-only", round(mean(eq_only_co),1), " all-equity", round(mean(all_eq_co),1))
print("serial-acquirer test: purchases", round(sum(purch),1), "vs half of owner cash before purchases", round(sum(all_eq)/2,1))
# Organic revenue growth, derived from the filer's MD&A attributions (10-K FY2025, IPO 424B4 for 2023):
# 2025: E&C +124.7 of which ~80% acquisitions -> organic 24.9; I&M +327.2, no acquisition named -> organic 327.2
# 2024: E&D +123.8 (85% acq) -> 18.6; PPM +51.6 (30% acq) -> 36.1; I&F +240.9 (60% acq) -> 96.4; M&S +67.3 (80% acq) -> 13.5
org25 = (124.691*0.20 + 327.198)/2098.602
org24 = (123.779*0.15 + 51.577*0.70 + 240.909*0.40 + 67.275*0.20)/1615.062
print(f"organic growth derived: 2024 {org24:.1%}, 2025 {org25:.1%}, mean {(org24+org25)/2:.1%}")
sales_cagr = (rev[-1]/rev[0])**(1/3)-1
print(f"total sales growth 2022-2025 {sales_cagr:.1%}")

def pv(base, g, r, n=10):
    v=0; c=base
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+r)**t
    return v + (c/r)/(1+r)**n      # zero nominal growth after year ten
def irr(price, base, g, n=10):
    lo,hi=0.0001,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(base,g,m,n)>price: lo=m
        else: hi=m
    return m

# Bowers on its own filed record (closed 2026-01-02, after the window): FY Sept 2024 and 2025 audited
bow_ocf=[81.912804,46.196030]; bow_capex=[3.074522,2.127334]
bow_pre = mean([o-c for o,c in zip(bow_ocf,bow_capex)])   # S-corporation: almost no entity tax, interest negligible
bow = bow_pre*(1-TAX)
print("Bowers owner cash, mean FY2024-25, before tax", round(bow_pre,1), "after the run's tax rate", round(bow,1))

# Net debt at 2026-06-30 (10-Q): debt current 26.201 + long-term 1,008.336 (net of issuance costs), cash 291.980;
# Bowers deferred consideration $50M due 2026-12-31 (8-K 2026-01-02) added as a stated obligation.
debt = 26.201 + 1008.336; cash = 291.980; deferred = 50.0
nd = debt - cash + deferred
tra = 342.729
shares = 108.075480   # cover of the 10-Q: Class A 76,904,346 + Class B 31,171,134 (exchangeable one for one)
price = 43.53
mcap = price*shares
ev = mcap + nd
print(f"net debt {nd:.1f}  (TRA liability {tra:.1f} shown beside)  market cap {mcap:.1f}  EV {ev:.1f}")

def report(label, base, g):
    lo = pv(base, 0.0, R); hi = pv(base, g, R)
    lo10 = pv(base,0.0,FLOOR); hi10 = pv(base,g,FLOOR)
    ps = lambda v: (v-nd)/shares
    print(f"\n{label}: base {base:.1f}, growth {g:.1%}")
    print(f"  value at {R:.2%}: no-growth EV {lo:.0f} -> ${ps(lo):.2f}/sh ; growth EV {hi:.0f} -> ${ps(hi):.2f}/sh ; width {hi/lo if lo>0 else float('nan'):.2f}x (EV), per share {ps(hi)/ps(lo) if ps(lo)>0 else float('nan'):.2f}x")
    print(f"  expected return at price (EV {ev:.0f}): no-growth {base/ev:.2%} ; growth case IRR {irr(ev,base,g):.2%}")
    print(f"  fair price (each end at 10%, averaged): EV {(lo10+hi10)/2:.0f} -> ${ps((lo10+hi10)/2):.2f}/sh")
    return ps((lo10+hi10)/2)

g_org = (org24+org25)/2
# central: organic pair (serial acquirer), all-equity, window mean plus Bowers on its own record
f_c = report("CENTRAL all-equity organic pair, window 2022-25 + Bowers", mean(all_eq)+bow, g_org)
report("cap check: growth cut to discount rate", mean(all_eq)+bow, R)
report("literal window, all-equity, no Bowers", mean(all_eq), g_org)
report("variant: company-funded stock pay only, + Bowers", mean(all_eq_co)+bow, g_org)
# equity-only beside: owner cash after interest against market value; current interest on today's debt
cur_int = 33.911*2 - 0.859*2      # H1 2026 interest expense annualized, less non-cash amortization
eqo_base = mean(all_eq)+bow - cur_int*(1-TAX)
lo = pv(eqo_base,0,R); hi = pv(eqo_base,g_org,R)
lo10 = pv(eqo_base,0,FLOOR); hi10=pv(eqo_base,g_org,FLOOR)
print(f"\nEQUITY-ONLY beside: base {eqo_base:.1f} (after current interest {cur_int:.1f} taxed at {TAX:.2%})")
print(f"  value {lo/shares:.2f} to {hi/shares:.2f} per share; return at price: no-growth {eqo_base/mcap:.2%}, growth IRR {irr(mcap,eqo_base,g_org):.2%}")
print(f"  fair price equity-only ${(lo10+hi10)/2/shares:.2f}")
# default pair beside: purchases deducted, total growth credited (window mean negative -> no-growth case alone, said so)
dp = mean([a-p for a,p in zip(all_eq,purch)])
print(f"\nDEFAULT pair beside: mean owner cash after purchases {dp:.1f} (negative: no positive value on this pair)")
