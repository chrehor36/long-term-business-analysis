# COMPUTATION, NOT A CLEARANCE. Q7 range and fair price, per Q7's range convention and Part VII.
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from owner_cash import oc
SOV = 0.0543; FLOOR = 0.10
SH = 30.939686            # cover count, millions
DEBT = 1805.6; CASH = 273.7   # 10-Q 2026-05-31, debt net (recourse 733.3 + non-recourse 1,072.3); cash and equivalents
NETDEBT = DEBT - CASH
PRICE = 39.11
def pv(base, g, r, years=10):
    v=0; c=base
    for t in range(1,years+1):
        c = c*(1+g); v += c/(1+r)**t
    v += c/r/(1+r)**years      # zero nominal growth after year ten
    return v
def avg(ys, basis, capex): return sum(oc(y,basis,capex) for y in ys)/len(ys)
cyc = range(2016,2026); win = range(2021,2026)
rows=[]
def case(label, base, g, basis):
    out=[]
    for r in (SOV, FLOOR):
        ev = pv(base,g,r)
        ps = (ev - NETDEBT)/SH if basis=='all' else ev/SH
        out.append(ps)
    print('%-62s base %7.1f g %6.1f%%  value/sh @5.43%% %8.2f  @10%% %8.2f' % (label, base, 100*g, out[0], out[1]))
    return out
print('net debt', round(NETDEBT,1), 'market cap', round(PRICE*SH,1), 'EV', round(PRICE*SH+NETDEBT,1))
# all-equity, maintenance-only (central where the filing allows the guess), cycle base FY2016-FY2025
b = avg(cyc,'all','maint')
h1 = avg(range(2016,2021),'all','maint'); h2 = avg(range(2021,2026),'all','maint')
g = (h2/h1)**(1/5)-1
print('halves all-equity maint', round(h1,1), round(h2,1), 'rate %.1f%%'%(100*g))
top = case('AE maintenance-only, cycle base, no growth (TOP)', b, 0.0, 'all')
bot = case('AE maintenance-only, cycle base, halves decline (BOTTOM)', b, g, 'all')
print('FAIR (all-equity) = avg of ends at 10%%: %.2f' % ((top[1]+bot[1])/2))
# beside: all spending (acquisitions deducted), cycle base
case('AE all spending, cycle base, no growth (beside)', avg(cyc,'all','all'), 0.0, 'all')
case('AE organic (no acquisitions), cycle base, no growth (beside)', avg(cyc,'all','noacq'), 0.0, 'all')
# literal window beside
case('AE maintenance-only, literal window FY21-25, no growth', avg(win,'all','maint'), 0.0, 'all')
case('AE all spending, literal window FY21-25, no growth', avg(win,'all','all'), 0.0, 'all')
case('AE maintenance-only, FY2014-FY2025 base, no growth (robustness)', avg(range(2014,2026),'all','maint'), 0.0, 'all')
# equity-only beside
be = avg(cyc,'eq','maint'); e1=avg(range(2016,2021),'eq','maint'); e2=avg(range(2021,2026),'eq','maint')
print('halves equity maint', round(e1,1), round(e2,1), '(sign change: range is the no-growth case alone)')
eq = case('EQUITY-ONLY maintenance-only, cycle base, no growth', be, 0.0, 'eq')
print('FAIR (equity-only) = %.2f (no-growth case alone)' % eq[1])
case('EQUITY-ONLY all spending, cycle base, no growth', avg(cyc,'eq','all'), 0.0, 'eq')
# what owner cash would the price need at the floor (all-equity, no growth)
print('owner cash before interest needed for 10%% at the price, all-equity: %.1f' % (FLOOR*(PRICE*SH+NETDEBT)))
