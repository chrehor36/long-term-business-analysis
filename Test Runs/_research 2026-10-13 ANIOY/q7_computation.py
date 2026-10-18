# COMPUTATION, NOT A CLEARANCE (the file closed OUT at Q2). Q7's range convention applied in full, arithmetic only.
import figures as F

r = 0.0376          # ECB euro AAA 30y spot, 2026-10-12
floor = 0.10
shares = 249.158749 # millions outstanding at 2026-06-30
price = 16.77
lease = 23.5        # right-of-use assets at 2026-06-30 as the stand-in for lease liabilities (not separated in the condensed statements)
nd_h1 = 1361.0 + lease   # company NFD at 2026-06-30 (bank borrowings less cash) plus leases

def value(base, g, rate, years=10):
    """PV of owner cash growing at g for ten years, then flat (zero nominal growth) forever."""
    pv = 0.0; c = base
    for t in range(1, years+1):
        c = c*(1+g); pv += c/(1+rate)**t
    pv += (c/rate)/(1+rate)**years
    return pv

def per_share(ev): return (ev - nd_h1)/shares
def per_share_eq(v): return v/shares

cyc = [2020,2021,2022,2023,2024,2025]   # last full cycle, trough (2020) to trough (2025): see the run file, specific (a)
prev = [2016,2017,2018,2019]           # previous cycle, trough (2016) to trough (2019)
lit = [2021,2022,2023,2024,2025]       # the literal five-year window
avg = lambda f, ys: sum(f(y) for y in ys)/len(ys)

base_all = avg(F.oc_allequity, cyc); base_eq = avg(F.oc_equity, cyc)
prev_all = avg(F.oc_allequity, prev); prev_eq = avg(F.oc_equity, prev)
acq_cyc = sum(F.acq[y]-F.divest[y] for y in cyc)/len(cyc)
acq_prev = sum(F.acq[y]-F.divest[y] for y in prev)/len(prev)
sum_oc_cyc = sum(F.oc_equity(y) for y in cyc)
gap = (sum(cyc)/len(cyc)) - (sum(prev)/len(prev))
print(f"cycle base all-equity {base_all:.1f}, equity {base_eq:.1f}; previous cycle {prev_all:.1f} / {prev_eq:.1f}; years between midpoints {gap}")
print(f"net purchases over the cycle window {sum(F.acq[y]-F.divest[y] for y in cyc):.1f} vs half of owner cash before purchases {sum_oc_cyc/2:.1f}")
lit_oc = sum(F.oc_equity(y) for y in lit); lit_acq = sum(F.acq[y]-F.divest[y] for y in lit)
print(f"literal window: net purchases {lit_acq:.1f} vs half owner cash {lit_oc/2:.1f}")

# organic growth: the filer reports no organic growth figure; the stainless business's own sales growth 2016 (whole group
# was stainless) to 2025 (stainless segment revenue 4,143.8) is the run's stand-in, said so in the run file
g_org = (4143.8/3968.1)**(1/9)-1
# total growth between cycle averages, purchases in (for the default pair the purchases are deducted)
g_tot_all = (base_all/prev_all)**(1/gap)-1
def_base_all = base_all - acq_cyc; def_prev_all = prev_all - acq_prev
g_def_all = (def_base_all/def_prev_all)**(1/gap)-1
print(f"g organic (stainless sales) {g_org*100:.2f}%  g total purchases-in {g_tot_all*100:.2f}%  default pair base {def_base_all:.1f} g {g_def_all*100:.2f}%")

def show(label, base, gs, nd=True):
    vals=[]
    for g in gs:
        ev = value(base, g, r)
        ps = per_share(ev) if nd else per_share_eq(ev)
        vals.append((g, ev, ps))
    print(label, " | ".join(f"g={g*100:.2f}% EV {ev:.0f} -> {ps:.2f}/sh" for g,ev,ps in vals))
    return vals

print("\nCENTRAL (serial-acquirer rule -> organic pair): all-equity, purchases left out, organic growth credited")
org = show("organic all-equity", base_all, [0.0, g_org])
print("equity-only beside:")
org_eq = show("organic equity-only", base_eq, [0.0, g_org], nd=False)
print("\nDEFAULT PAIR beside (purchases deducted, total growth credited; a decline is the bottom, no-growth the top)")
dft = show("default all-equity", def_base_all, [g_def_all, 0.0])
print("\nLITERAL window 2021-2025 beside (all-equity, purchases left out)")
litb = avg(F.oc_allequity, lit)
show("literal", litb, [0.0, g_org])
print("\nDEPRECIATION variant beside (D&A in place of capex over the cycle)")
dep_adj = avg(lambda y: F.capex[y]-F.da[y]-F.dispo[y], cyc)
show("D&A variant all-equity", base_all+dep_adj, [0.0, g_org])

# floor test at the price: expected return at the price for each case = owner cash yield (no growth after the ten years)
ev_price = price*shares + nd_h1
print(f"\nEV at price {ev_price:.0f}; mkt cap {price*shares:.0f}")
def irr(base, g, cost):
    lo, hi = 0.001, 1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if value(base,g,mid) > cost: lo=mid
        else: hi=mid
    return mid
for lab, b, g in [("organic no-growth", base_all, 0.0), ("organic growth", base_all, g_org),
                  ("default no-growth", def_base_all, 0.0), ("literal no-growth", litb, 0.0), ("literal growth", litb, g_org)]:
    print(f"floor test {lab}: expected return at price {irr(b,g,ev_price)*100:.2f}%")
print(f"equity-only floor test organic growth: {irr(base_eq,g_org,price*shares)*100:.2f}%")

# fair price: each end case valued at 10%, averaged (Part VII)
ends = [value(base_all,0.0,floor), value(base_all,g_org,floor)]
fair = (sum(ends)/2 - nd_h1)/shares
ends_eq = [value(base_eq,0.0,floor), value(base_eq,g_org,floor)]
fair_eq = (sum(ends_eq)/2)/shares
print(f"\nFAIR PRICE central (all-equity, organic pair) {fair:.2f}; equity-only {fair_eq:.2f}")
ends_d = [value(def_base_all,g_def_all,floor), value(def_base_all,0.0,floor)]
print(f"fair price default pair beside {(sum(ends_d)/2 - nd_h1)/shares:.2f}")
print(f"per ADR (one-half share): range {org[0][2]/2:.2f}-{org[1][2]/2:.2f}, fair {fair/2:.2f}")
