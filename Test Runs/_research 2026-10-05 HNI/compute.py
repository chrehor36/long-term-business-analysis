# COMPUTATION - NOT A CLEARANCE. Owner cash = OCF - all capex (incl. capitalized software) - stock pay; USD millions.
hni={2016:(223.4,119.6,8.1),2017:(133.1,127.4,7.8),2018:(186.4,63.7,7.3),2019:(219.4,66.9,6.8),2020:(214.5,41.8,7.8),
     2021:(131.6,66.5,12.9),2022:(81.2,68.4,9.0),2023:(267.5,79.1,16.5),2024:(226.7,52.9,17.4),2025:(276.3,67.8,24.7)}
# Steelcase fiscal years end late Feb of the following calendar year; FY ending Feb 2017 labelled 2016, etc.
scs={2015:(186.4,93.4,21.0),2016:(170.7,61.1,19.8),2017:(227.0,87.9,19.1),2018:(131.2,81.4,17.7),2019:(360.8,73.4,16.7),
     2020:(64.8,41.3,20.9),2021:(-102.6,60.5,16.1),2022:(89.4,59.1,21.8),2023:(308.7,47.1,26.0),2024:(148.5,47.1,24.5)}
oc=lambda t:t[0]-t[1]-t[2]
print("HNI owner cash by year:",{y:round(oc(v),1) for y,v in hni.items()})
print("SCS owner cash by FY (label = calendar year in which FY began):",{y:round(oc(v),1) for y,v in scs.items()})
h5=sum(oc(hni[y]) for y in range(2021,2026))/5; h5p=sum(oc(hni[y]) for y in range(2016,2021))/5
s5=sum(oc(scs[y]) for y in range(2020,2025))/5; s5p=sum(oc(scs[y]) for y in range(2015,2020))/5
print(f"HNI 5yr avg 2021-25 {h5:.1f}  prior 2016-20 {h5p:.1f}")
print(f"SCS 5yr avg FY21-FY25 {s5:.1f}  prior FY16-FY20 {s5p:.1f}")
inc_int_after_tax=38.0   # disclosed guess: H1-2026 net interest 44.4 annualised ~89 less pre-deal ~38 net, at ~25% tax
base=h5+s5-inc_int_after_tax
prior=h5p+s5p-inc_int_after_tax
print(f"combined base (after added interest) {base:.1f}; same construction for prior window {prior:.1f}")
g=( (h5+s5)/(h5p+s5p) )**(1/5)-1
print(f"growth shown, aggregate, between the two five-year averages: {g*100:.2f}%/yr")
sh=72.1818; r=0.0563; price=47.65
def pv(c0,g,r,yrs=10):
    v=0;c=c0
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    return v + (c/r)/(1+r)**yrs   # then zero nominal growth
lo=pv(base,g,r); hi=pv(base,0,r)
print(f"range: shown-growth {lo:.0f}M = ${lo/sh:.2f}/sh ; no-growth {hi:.0f}M = ${hi/sh:.2f}/sh ; ratio {hi/lo:.2f} ; price ${price}")
print(f"owner cash yield at price: {base/(sh*price)*100:.2f}%")
# fair price: expected return on central case (no growth) clears 10% pre-tax floor
for f in (0.10,0.07):
    print(f"price at which central (no-growth) case yields {f*100:.0f}%: ${base/f/sh:.2f}")
# cheap price: the pessimistic (shown-growth) case discounted at 10% (needs no pencil if even the worst case clears the floor)
cheap=pv(base,g,0.10)
print(f"cheap: shown-growth case at 10%: ${cheap/sh:.2f}")
# management case sensitivity: add 120 run-rate synergies pre-tax, 25% tax, no growth
syn=120*0.75
print(f"sensitivity, synergies counted in full: no-growth value ${(base+syn)/r/sh:.2f}/sh; 10% price ${(base+syn)/0.10/sh:.2f}")
print("--- floor applied as 7% after corporate tax (L2002-020's translation of 10% pre-tax) ---")
print(f"fair (central = no-growth case at 7%): ${base/0.07/sh:.2f}")
print(f"cheap (bottom = shown-growth case discounted at 7%): ${pv(base,g,0.07)/sh:.2f}")
print(f"sensitivity with synergies in full, no growth, at 7%: ${(base+syn)/0.07/sh:.2f}")
# implied: owner cash the price needs at 7%, no growth
print(f"owner cash the price needs at 7%, no growth: {price*sh*0.07:.0f}M vs base {base:.1f}M")
