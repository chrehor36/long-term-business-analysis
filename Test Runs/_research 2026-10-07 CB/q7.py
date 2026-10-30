# Q7 arithmetic for the CB run of 2026-10-07 (sector method v5). All $M unless stated. Sources: see run file.
rf=0.0564          # UST 30y par yield 10/06/2026 (tools/sources.py)
floor=0.10         # Q7 floor CONVENTION
N=385.799859       # shares, cover of 10-Q filed 2026-07-28 (as of 2026-07-20), millions
price=334.21
# --- balance sheet 2026-06-30 (10-Q 0000896159-26-000017)
inv=172649; cash=2753
unpaid=89669; rr_loss=20284; unearned=28511; prepaid_re=4683
prem_recv=19068; dac=10744
fpb=20159; mrb=505; pab=9102; rr_pb=333
ins_pay=9345; repo=3368; nci=5473; dtl_net=1870-1237
debt=663+17452+427
float_A2=(unpaid-rr_loss)+(unearned-prepaid_re)
float_C1=float_A2-prem_recv-dac
life_liab=fpb+mrb+pab-rr_pb
def c1(fl): return inv+cash-fl-life_liab-ins_pay-repo-nci-dtl_net
C1_central=c1(float_C1); C1_A2=c1(float_A2); C1_gross=c1(0)
print(f"float A2 {float_A2:,.0f}  float with receivables and DAC deducted {float_C1:,.0f}  life liabilities {life_liab:,.0f}  debt {debt:,.0f}")
print(f"C1 net (central, C1 deductions) {C1_central:,.0f}; C1 net (A2 strict) {C1_A2:,.0f}; C1 gross {C1_gross:,.0f}")
# --- component 2
ay={2016:2063,2017:650,2018:927,2019:1623,2020:2998,2021:3257,2022:3626,2023:5075,2024:5169,2025:5395}
win=[ay[y] for y in range(2021,2026)]; avg5=sum(win)/5; avg10=sum(ay.values())/10
g_lit=(ay[2025]/ay[2021])**(1/4)-1
g_npe=(45790/33890)**(1/4)-1     # P&C NPE 2021->2025
g_npe10=(45790/26694)**(1/9)-1   # P&C NPE 2016->2025
tax=0.186; tax_a4=0.144
life=168; integ=-60; runoff=-300   # life segment income less NII (2023-25 avg); integration and severance (recurring); corporate run-off adverse development (2024-25)
nogrowth_share=0.11
def pv(base,g,r,years=10):
    v=0;c=base
    for t in range(1,years+1):
        c=c*(1+g); v+=c/(1+r)**t
    v+= c/r/(1+r)**years   # zero nominal growth after year ten
    return v
def c2(base_uw_pre,g,r,t=tax):
    b=base_uw_pre*(1-t)
    uw=pv(b*(1-nogrowth_share),g,r)+b*nogrowth_share/r
    other=(life+integ+runoff)*(1-t)/r
    return uw+other, uw, other
print(f"AY avg 5y {avg5:,.0f}  AY avg 10y {avg10:,.0f}  growth literal {g_lit:.3%}  NPE growth 21-25 {g_npe:.3%}  NPE growth 16-25 {g_npe10:.3%}")
def rng(C1,base,g,t=tax,label=''):
    lo_c2,_,oth=c2(0,0,rf,t)
    hi_c2,uw,_=c2(base,g,rf,t)
    lo=C1+lo_c2-debt; hi=C1+hi_c2-debt
    print(f"{label:52s} low {lo:9,.0f} (${lo/N:7.1f})  high {hi:9,.0f} (${hi/N:7.1f})  ratio {hi/lo:5.2f}  mid ${ (lo+hi)/2/N:7.1f}")
    return lo,hi
print('--- value ranges at the sovereign, all-equity (whole business less debt), per share on',N,'M shares; price',price)
cen=rng(C1_central,avg5,g_lit,label='CENTRAL: net (C1 deductions), 5y window, literal g')
rng(C1_central,avg5,g_npe,label='net (C1 ded.), 5y window, g cut to NPE growth')
rng(C1_central,avg10,g_npe10,label='net (C1 ded.), whole-cycle 10 AY, g=NPE 16-25')
rng(C1_central,avg5,g_lit,t=tax_a4,label='net (C1 ded.), 5y, literal g, A4 window tax 14.4%')
rng(C1_A2,avg5,g_lit,label='net (A2 strict float), 5y, literal g')
rng(C1_gross,avg5,g_lit,label='GROSS (float counted as equity), 5y, literal g')
rng(C1_gross,avg5,g_npe,label='GROSS, 5y, g cut to NPE growth')
# immaturity load sensitivity
load=float(open('immaturity_load.txt').read()) if __import__('os').path.exists('immaturity_load.txt') else 0
if load:
    rng(C1_central,avg5-load,g_lit,label=f'net, 5y less immaturity load {load:,.0f}/yr')
# --- fair price: midpoint stream earns the floor (CONVENTION of this run for a two-component value)
nii=6465; avg_inv=(150650+168720)/2; y_at=nii/avg_inv*(1-tax)
c1_income=C1_central*y_at
mid_uw_base=avg5/2
v10_c2,_,_=c2(mid_uw_base,g_lit,floor)
ev_central=c1_income/floor+v10_c2
fair_ae=(ev_central-debt)/N
interest_at=764*(1-tax)
fair_eq=(ev_central-interest_at/floor)/N
fair_ae_face=(C1_central+v10_c2-debt)/N
print(f"after-tax portfolio yield {y_at:.3%}; C1 income {c1_income:,.0f}")
print(f"FAIR PRICE all-equity (C1 at its earnings) ${fair_ae:.1f}; equity-only ${fair_eq:.1f}; all-equity with C1 at face ${fair_ae_face:.1f}")
# gross variant fair price
c1g_income=C1_gross*y_at
ev_g=c1g_income/floor+v10_c2
print(f"FAIR PRICE gross variant all-equity ${(ev_g-debt)/N:.1f}; equity-only ${(ev_g-interest_at/floor)/N:.1f}")
# expected return at price on central midpoint stream (perpetuity approx, year-one)
print(f"market cap {price*N:,.0f}  EV {price*N+debt:,.0f}")
# whole-cycle variant fair price and expected return at the price (central midpoint stream, all-equity)
v10_cyc,_,_=c2(avg10/2,g_npe10,floor)
print(f"FAIR PRICE whole-cycle variant all-equity ${(c1_income/floor+v10_cyc-debt)/N:.1f}; equity-only ${(c1_income/floor+v10_cyc-interest_at/floor)/N:.1f}")
def ev_at(r,base,g): 
    v,_,_=c2(base,g,r); return c1_income/r+v
ev=price*N+debt
lo,hi=0.001,0.5
for _ in range(100):
    mid=(lo+hi)/2
    if ev_at(mid,avg5/2,g_lit)>ev: lo=mid
    else: hi=mid
print(f"expected return at ${price} on the central midpoint stream, all-equity basis: {lo:.2%}")
lo,hi=0.001,0.5
for _ in range(100):
    mid=(lo+hi)/2
    if ev_at(mid,avg5,g_lit)>ev: lo=mid
    else: hi=mid
print(f"expected return at ${price} on the HIGH-END stream (full AY average, literal growth), all-equity: {lo:.2%}")
def irr(c1inc,base,g):
    lo,hi=0.001,0.5
    for _ in range(100):
        mid=(lo+hi)/2
        v,_,_=c2(base,g,mid)
        if c1inc/mid+v>ev: lo=mid
        else: hi=mid
    return lo
print(f"expected return at price, GROSS high-end stream (float as equity, full AY average, literal growth): {irr(c1g_income,avg5,g_lit):.2%}")
print(f"expected return at price, GROSS midpoint stream: {irr(c1g_income,avg5/2,g_lit):.2%}")
print(f"expected return at price, net, high-end stream with g cut to NPE growth: {irr(c1_income,avg5,g_npe):.2%}")
print(f"expected return at price, net, whole-cycle high-end stream: {irr(c1_income,avg10,g_npe10):.2%}")
print(f"C1 counted at face instead of at its earnings, net, high-end stream: value at 10% = {(C1_central+c2(avg5,g_lit,floor)[0]-debt)/N:.1f}/share")
