"""COMPUTATION, NOT A CLEARANCE. SUNB reporting figures under Q7's range convention (file closed at Q2).
All $M. Sources noted per line; see the run file."""
R = 0.056          # UST 30y par, 10/09/2026
FLOOR = 0.10
SH = 409.764897    # M shares, 10-Q cover
PRICE = 75.17
years = ['FY2022','FY2023','FY2024','FY2025','FY2026']
# --- Series A: all spending (OCF-based), equity-only before acquisitions
# FY2022 IFRS: FCF 1,125.4 (AR2022 cash flow table) - lease principal 107.6 (IFRS 16, financing) - SBC 48.1
# FY2023-26 US GAAP: FCF (10-K def: OCF - rental & non-rental capex + disposal proceeds) - SBC (cash-flow add-back) - finance-lease principal - intangibles - other investing
fcf      = [1125.4, 441.0, 126.0, 1675.0, 2055.0]
lease_pr = [107.6, 0, 0, 0, 0]
sbc      = [48.1, 53.0, 92.0, -9.0, 80.0]
fl_pr    = [0, 8.0, 12.0, 18.0, 18.0]
intang   = [0, 10.0, 29.0, 15.0, 6.0]
other    = [0, 42.0, 15.0, 0, 0]
acq      = [1277.4, 1061.0+22.0, 846.0+30.0, 134.0+13.0, 206.0-16.0]   # acquisitions + contingent consideration paid, net of disposals
int_paid_debt = [231.1-80.7+36.0, 245.0, 392.0, 416.0, 368.0]       # FY2022: financing costs paid less lease interest, plus exceptional redemption premium
tax      = [417.0/1668.1, 547/2152, 522/2094, 517/2070, 476/1801]
eqA_pre = [fcf[i]-lease_pr[i]-sbc[i]-fl_pr[i]-intang[i]-other[i] for i in range(5)]
eqA = [eqA_pre[i]-acq[i] for i in range(5)]
atint = [int_paid_debt[i]*(1-tax[i]) for i in range(5)]
allA = [eqA[i]+atint[i] for i in range(5)]
allA_pre = [eqA_pre[i]+atint[i] for i in range(5)]
# --- Series B: maintenance-only (depreciation as the maintenance proxy), all-equity
# operating income US-GAAP basis + amortization of acquired intangibles, after the company's own tax
opinc = [1947.8-80.7, 2446.0, 2511.0, 2499.0, 2181.0]   # FY2022 IFRS operating profit less lease interest (US-GAAP-like)
amort = [108.6, 118.0, 121.0, 114.0, 113.0]
M = [(opinc[i]+amort[i])*(1-tax[i]) for i in range(5)]
# growth spending = net capex above depreciation (ex amortization, ex IFRS16 ROU) + acquisitions (net) + working-capital increase
netcapex = [1765.4+398.4-343.8-24.8, 3020+500-574-41+10+42, 3759+659-832-48+29+15, 2251+441-462-61+15, 1842+352-424-41+6]
dep      = [1553.0-154.1, 1727-118, 2047-121, 2251-114, 2309-113]
wc_incr  = [3609.4-3406.5, -(-172-5-103-34+83), -(-184+21-89-24+120), -(22+15-74+2+59), -(-206-30+15+57+111)]  # FY2022: EBITDA less cash from operations before rental changes (IFRS); US GAAP: sign-flipped working-capital lines
G = [netcapex[i]-dep[i]+acq[i]+wc_incr[i] for i in range(5)]
avg = lambda v: sum(v)/len(v)
def pv_growth(c0, g, G0, gG, r, yrs=10):
    """years 1..10: c0*(1+g)^t - G0*(1+gG)^t ; after 10: c0*(1+g)^10 flat forever (growth spending stops)"""
    v=0
    for t in range(1,yrs+1):
        v += (c0*(1+g)**t - G0*(1+gG)**t)/(1+r)**t
    v += (c0*(1+g)**yrs)/r/(1+r)**yrs
    return v
def pv_flat(c0, r): return c0/r
def cagr(a,b,n): return (b/a)**(1/n)-1
ND = 8556 + 171 - 32 + 56 + 123   # debt 7/31/26 + finance leases (4/30/26, latest stated) - cash + subsequent acquisitions + dividend declared 9/9/26 (0.30 x 409.76M)
out=[]
P=lambda *a: out.append(' '.join(str(x) for x in a))
P('years', years)
P('A eq-only owner cash before acquisitions', [round(x) for x in eqA_pre], 'avg', round(avg(eqA_pre)))
P('A eq-only owner cash, acquisitions deducted', [round(x) for x in eqA], 'avg', round(avg(eqA)))
P('after-tax debt interest', [round(x) for x in atint], 'avg', round(avg(atint)))
P('A all-equity, acquisitions deducted', [round(x) for x in allA], 'avg', round(avg(allA)))
P('A all-equity, before acquisitions', [round(x) for x in allA_pre], 'avg', round(avg(allA_pre)))
P('B maintenance-only all-equity (M)', [round(x) for x in M], 'avg', round(avg(M)))
P('B equity-only M less after-tax interest', [round(M[i]-atint[i]) for i in range(5)], 'avg', round(avg(M)-avg(atint)))
P('growth spending G (net capex - dep + acq + WC)', [round(x) for x in G], 'avg', round(avg(G)))
P('net capex', [round(x) for x in netcapex], 'dep', [round(x) for x in dep], 'wc incr', [round(x) for x in wc_incr])
gM = cagr(M[0], M[-1], 4)
gM_half = (avg(M[3:]) / avg(M[:2]))**(1/3)-1
P('shown growth of M: end-to-end CAGR FY22-26', round(100*gM,2), '% ; halves (FY22-23 avg to FY25-26 avg, 3 yrs)', round(100*gM_half,2), '%')
rev = [7962.3, 9667.3, 10859, 10791, 11154]
P('revenue CAGR FY22-26', round(100*cagr(rev[0],rev[-1],4),2), '%')
Mbar, Gbar = avg(M), avg(G)
for label, r in [('sovereign 5.60%', R), ('floor 10%', FLOOR)]:
    ng = pv_flat(Mbar, r)
    gr = pv_growth(Mbar, gM, Gbar, gM, r)
    P(f'[{label}] maintenance-only, no growth: EV', round(ng), ' per share', round((ng-ND)/SH,2))
    P(f'[{label}] growth case (M grown at {100*gM:.2f}%, growth spending G charged, stops after yr10): EV', round(gr), ' per share', round((gr-ND)/SH,2))
    # equity-only beside
    Me = Mbar-avg(atint)
    P(f'[{label}] equity-only no growth: equity', round(pv_flat(Me,r)), ' per share', round(pv_flat(Me,r)/SH,2))
    P(f'[{label}] equity-only growth: equity', round(pv_growth(Me,gM,Gbar,gM,r)), ' per share', round(pv_growth(Me,gM,Gbar,gM,r)/SH,2))
# all-spending literal series A: sign change -> no-growth case alone
for label, r in [('sovereign', R), ('floor', FLOOR)]:
    v = avg(allA)/r
    P(f'[{label}] series A (acq deducted) no-growth alone: EV', round(v), ' per share', round((v-ND)/SH,2))
    v2 = avg(allA_pre)/r
    P(f'[{label}] series A before acquisitions (organic beside) no-growth: EV', round(v2), ' per share', round((v2-ND)/SH,2))
P('net debt used', ND, ' market cap', round(SH*PRICE), ' EV at price', round(SH*PRICE+ND))
# expected return at price: maintenance-only no growth yield, and growth case IRR
EV = SH*PRICE+ND
P('owner cash yield at price (all-equity, M avg / EV)', round(100*Mbar/EV,2), '%')
def irr(f, lo=-0.5, hi=0.5):
    for _ in range(200):
        mid=(lo+hi)/2
        (lo,hi) = (mid,hi) if f(mid)>EV else (lo,mid)
    return mid
P('expected return at price, no-growth case', round(100*Mbar/EV,2), '%')
P('expected return at price, growth case (IRR)', round(100*irr(lambda r: pv_growth(Mbar,gM,Gbar,gM,r) if r>gM+0.001 else 1e12, lo=gM+0.002),2), '%')
P('expected return at price, growth case without charging growth spending (M grown, nothing charged)', round(100*irr(lambda r: pv_growth(Mbar,gM,0,gM,r) if r>0.001 else 1e12, lo=0.002),2), '%')
print('\n'.join(out))
