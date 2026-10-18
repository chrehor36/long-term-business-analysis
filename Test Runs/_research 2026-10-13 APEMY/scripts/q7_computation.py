"""COMPUTATION, NOT A CLEARANCE (Q2 closed the file OUT). APEMY / Aperam, EUR millions.
Inputs transcribed from the consolidated statements of cash flows in the annual reports (2018-2025)
and the Q2 2026 release (net financial debt at 30 June 2026). Arithmetic only."""
r = 0.0376          # ECB euro area AAA 30y spot, 2026-10-12
FLOOR = 0.10
SH = 72.467683      # million shares outstanding, company share-capital page, 30 Sep 2026
PRICE = 38.50       # APAM Euronext Amsterdam, 2026-10-13 (aggregator quote, flagged)
NFD = 993.0         # net financial debt 30 Jun 2026 (borrowings incl. leases, less cash)
FX = 1.1188         # ECB USD per EUR, 2026-10-13
#        OCF   capex  bio  lease  acq   net_int_paid  sales
d = {2018:(295,192,0,1,0,5,4677), 2019:(400,151,0,8,0,5,4240), 2020:(303,109,0,9,0,7,3624),
     2021:(550,152,0,9,31,4,5102), 2022:(642,285,11,14,0,-3,8156), 2023:(471,250,51,15,0,5,6592),
     2024:(280,139,26,19,0,26,6255), 2025:(422,137,37,25,415,40,6080)}
def oc(y, allequity=True, preacq=True):
    o,c,b,l,a,i,s = d[y]
    v = o-c-b-l
    if not preacq: v -= a
    if allequity: v += i
    return v
for y in d: print(y, 'eq-only pre-acq', oc(y,False), ' all-eq pre-acq', oc(y), ' all-eq after acq', oc(y,True,False), ' share of sales %.1f%%' % (100*oc(y)/d[y][6]))
def pv(base, g, rate, after_base):
    # ten years of 'base' growing at g (first year = base*(1+g)), then zero nominal growth on after_base grown the same
    v=0; x=base; z=after_base
    for t in range(1,11):
        x*=(1+g); z*=(1+g); v+=x/(1+rate)**t
    return v + (z/rate)/(1+rate)**10
def show(label, base_after_acq, base_pre, g, basis_debt=NFD, sh=SH):
    out=[]
    for rate in (r, FLOOR):
        ev = pv(base_after_acq, g, rate, base_pre)
        out.append((ev, (ev-basis_debt)/sh))
    print(f"{label}: g={g:+.2%}  at {r:.2%}: EV {out[0][0]:,.0f} -> {out[0][1]:.2f}/sh | at 10%: EV {out[1][0]:,.0f} -> {out[1][1]:.2f}/sh")
    return out
yrs5=[2021,2022,2023,2024,2025]; cyc=[2020,2021,2022,2023,2024,2025]; prev=[2018,2019]
avg=lambda ys,**k: sum(oc(y,**k) for y in ys)/len(ys)
acq5=sum(d[y][4] for y in yrs5); pre5=sum(oc(y) for y in yrs5)
print('net purchases / owner cash before purchases, window: %.1f%%' % (100*acq5/pre5))
B_pre=avg(cyc); B_aft=avg(cyc,preacq=False); P_pre=avg(prev)
print(f'cycle base 2020-25 all-eq pre-acq {B_pre:.1f}, after acq {B_aft:.1f}; prior-cycle end 2018-19 {P_pre:.1f}')
g_cyc=(B_pre/P_pre)**(1/4.5)-1
s_cyc=(sum(d[y][6] for y in cyc)/6)/(sum(d[y][6] for y in prev)/2); g_sales=s_cyc**(1/4.5)-1
print(f'growth between cycle averages {g_cyc:.2%}; sales growth same span {g_sales:.2%}')
# cap test (f): owner cash in year 10 vs highest share of sales earned
hi=max(oc(y)/d[y][6] for y in d); last_sales=d[2025][6]
print(f'highest owner-cash share of sales {hi:.1%}; yr10 owner cash at shown g {B_pre*(1+g_cyc)**10:.0f} = {B_pre*(1+g_cyc)**10/last_sales:.1%} of 2025 sales; at sales g {B_pre*(1+g_sales)**10/last_sales:.1%}')
g_top = g_cyc if B_pre*(1+g_cyc)**10/last_sales <= hi else g_sales
print('== ALL-EQUITY (central) ==')
lo=show('no-growth case (bottom)', B_aft, B_pre, 0.0)
hi_=show('growth case (top)', B_aft, B_pre, g_top)
fair=(lo[1][1]+hi_[1][1])/2
print(f'RANGE {lo[0][1]:.2f} to {hi_[0][1]:.2f} per share; width {hi_[0][1]/lo[0][1]:.2f}x; FAIR (avg of ends at 10%) {fair:.2f} EUR = {fair*FX:.2f} USD per ADR (1:1)')
ev_price = PRICE*SH + NFD
print(f'EV at price {ev_price:,.0f}; ends at 10% EV {lo[1][0]:,.0f} / {hi_[1][0]:,.0f} -> floor earned by some case? {max(lo[1][0],hi_[1][0])>=ev_price}')
# literal window beside
L_pre=avg(yrs5); L_aft=avg(yrs5,preacq=False)
h1=(oc(2021)+oc(2022))/2; h2=(oc(2024)+oc(2025))/2; g_lit=(h2/h1)**(1/3)-1
print(f'LITERAL window 2021-25: base pre {L_pre:.1f} after acq {L_aft:.1f}; halves {h1:.0f}->{h2:.0f} g={g_lit:.2%}')
show('literal no-growth', L_aft, L_pre, 0.0); show('literal decline (bottom)', L_aft, L_pre, g_lit)
print('== EQUITY-ONLY (beside) ==')
E_pre=sum(oc(y,False) for y in cyc)/6; E_aft=sum(oc(y,False,False) for y in cyc)/6
elo=show('eq no-growth', E_aft, E_pre, 0.0, basis_debt=0)
ehi=show('eq growth', E_aft, E_pre, g_top, basis_debt=0)
print('note: equity-only per-share values are owner cash after interest capitalised against the shares alone (no net debt deducted)')
ef=(elo[1][1]+ehi[1][1])/2
print(f'EQUITY-ONLY range {elo[0][1]:.2f} to {ehi[0][1]:.2f}; fair {ef:.2f} EUR = {ef*FX:.2f} USD')
print(f'market cap at price {PRICE*SH:,.0f}')
