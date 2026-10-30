# COMPUTATION, NOT A CLEARANCE (the file closed at Q2). Figures in C$ millions from the filed cash-flow statements
# (40-F exhibits FY2017, FY2019, FY2021, FY2023, FY2025; accessions in the run file). Arithmetic only.
years = list(range(2016, 2026))
ocf   = [744, 626, 820, 849, 702, 1001, 877, 1464, 796, 646]
capex = [358, 338, 277, 417, 486, 480, 918, 875, 311, 249]
intan = [21, 51, 20, 14, 14, 9, 31, 13, 10, 11]
sust  = [254, 218, 150, 141, 157, 199, 142, 174, 142, 162]   # filer's sustaining capital, finance leases excluded
lease = [16, 17, 18, 21, 25, 8, 9, 10, 6, 4]
nci   = [151, 172, 165, 106, 97, 156, 187, 223, 40, 11]
pref  = [42, 40, 40, 40, 39, 39, 43, 51, 52, 52]
sbc   = [0, 1, 1, 33, 0, 13, 3, 11, 22, 10]                  # equity-settled share pay added back in OCF; 2020 shown -7, taken as 0
intp  = [235, 230, 188, 185, 201, 220, 229, 277, 269, 282]   # cash interest paid, inside OCF
acq   = [0, 0, 30, 117, 32, 120, 10, 811, 217, 0]            # acquisitions net of cash, incl. TransAlta Renewables minority buyout 2023 (cash part)
disp  = [0, 0, 0, 0, 0, 128, 0, 0, 0, 0]                     # Pioneer Pipeline sale 2021
TAX = 0.233                                                   # applicable (statutory) rate, FY2025 tax note
def eq_all(i):   return ocf[i]-capex[i]-intan[i]-lease[i]-nci[i]-pref[i]-sbc[i]
def eq_mnt(i):   return ocf[i]-sust[i]-intan[i]-lease[i]-nci[i]-pref[i]-sbc[i]
def ae(f, i):    return f(i) + pref[i] + intp[i]*(1-TAX)       # all-equity: before interest after tax shield, before pref dividends
print('year  eq_allspend eq_maint  ae_allspend ae_maint  acq-disp')
for i, y in enumerate(years):
    print(y, eq_all(i), eq_mnt(i), round(ae(eq_all, i)), round(ae(eq_mnt, i)), acq[i]-disp[i])
def avg(f, idx): return sum(f(i) for i in idx)/len(idx)
W = range(5, 10); C = range(0, 10); H1 = range(0, 5)
for name, f in [('eq_all', eq_all), ('eq_mnt', eq_mnt), ('ae_all', lambda i: ae(eq_all, i)), ('ae_mnt', lambda i: ae(eq_mnt, i))]:
    print(name, 'window21-25 avg %.0f' % avg(f, W), 'cycle16-25 avg %.0f' % avg(f, C), 'half1 %.0f half2 %.0f' % (avg(f, H1), avg(f, W)))
acq_net = [acq[i]-disp[i] for i in range(10)]
print('acq net avg window %.0f cycle %.0f' % (sum(acq_net[5:])/5, sum(acq_net)/10))

def value(c0, g, r, yrs=10):
    pv = 0; c = c0
    for t in range(1, yrs+1):
        c = c*(1+g); pv += c/(1+r)**t
    pv += (c/r)/(1+r)**yrs           # zero nominal growth after year ten
    return pv
SHARES = 316.0; PRICE = 17.14; FX = 1.3993
nd_june = 3489 + 750 - 302          # borrowings incl. leases + exchangeable securities - cash, June 30 2026
prefs = 942
subs = FX*750 + FX*250 - FX*305     # Colorado debt assumed + cash paid, less Oklahoma wind 49% sale proceeds (closed 2026-10-22)
nd_ae = nd_june + prefs + subs
nd_eq_debt_only = nd_june + subs     # for reference
print('net debt all-equity (incl prefs) %.0f' % nd_ae)
lost = FX*29                        # share of Oklahoma wind sold, the release's own 2026 adjusted EBITDA figure, deducted from owner cash
print('lost owner cash from the wind sale %.0f' % lost)
import itertools
R = 0.0412
for label, base_ae, base_eq, g in [
    ('window, maintenance, acquisitions deducted', avg(lambda i: ae(eq_mnt, i), W) - sum(acq_net[5:])/5, avg(eq_mnt, W) - sum(acq_net[5:])/5, None),
    ('cycle, maintenance, acquisitions deducted', avg(lambda i: ae(eq_mnt, i), C) - sum(acq_net)/10, avg(eq_mnt, C) - sum(acq_net)/10, None),
    ('cycle, all spending, acquisitions deducted', avg(lambda i: ae(eq_all, i), C) - sum(acq_net)/10, avg(eq_all, C) - sum(acq_net)/10, None),
    ('window, all spending, acquisitions deducted', avg(lambda i: ae(eq_all, i), W) - sum(acq_net[5:])/5, avg(eq_all, W) - sum(acq_net[5:])/5, None)]:
    ae0 = base_ae - lost; eq0 = base_eq - lost
    print('--', label, 'ae0 %.0f eq0 %.0f' % (ae0, eq0))
    for gg in [0.0, -0.02, 0.02, 0.05]:
        v_ae = value(ae0, gg, R) - nd_ae; v_eq = value(eq0, gg, R) - subs  # equity-only: owner cash to common; the subsequent net financing (Colorado debt and cash, less the wind proceeds) charged against the equity
        f_ae = value(ae0, gg, 0.10) - nd_ae
        print('  g %+.2f  all-equity per share %.2f  (at 10%%: %.2f)  equity-only per share %.2f (at 10%%: %.2f)' % (gg, v_ae/SHARES, f_ae/SHARES, v_eq/SHARES, (value(eq0, gg, 0.10) - subs)/SHARES))
print('market value %.0f' % (SHARES*PRICE))

# floor test at the price: return on the price, no growth (the growth case is cut to sales growth, about zero)
for label, ae0, eq0 in [('cycle maint', 522.4, 300.0), ('window maint', 585.0, 342.0)]:
    print(label, 'all-equity yield on EV %.1f%%' % (100*ae0/(SHARES*PRICE+nd_ae)), 'equity-only yield %.1f%%' % (100*eq0/(SHARES*PRICE+subs)))
import statistics
dep = [601,635,574,590,654,529,599,621,531,579]
print('avg D&A %.1f avg sustaining %.1f gap %.1f' % (sum(dep)/10, sum(sust)/10, sum(dep)/10-sum(sust)/10))
print('sales 2016 2397 2025 2405 cagr %.2f%%' % (100*((2405/2397)**(1/9)-1)))
