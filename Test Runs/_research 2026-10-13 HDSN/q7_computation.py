# COMPUTATION, NOT A CLEARANCE (the file closed at Q2). Q7's range convention and Part VII's fair price, USD millions.
r_sov = 0.056          # UST 30y par, 2026-10-09
r_floor = 0.10         # the floor convention, about ten percent
shares = 42.088547     # 10-Q cover, 2026-07-27
price = 5.12
net_debt = -25.6       # 2026-06-30: no borrowings, cash $25.6M (10-Q); operating leases left out
allq = {2021:4.37,2022:67.47,2023:56.19,2024:64.62,2025:-13.55}   # all-equity owner cash, acquisitions deducted (owner_cash.py)
eqo  = {2021:-3.66,2022:58.23,2023:52.66,2024:65.00,2025:-11.55}  # equity-only, after interest, acquisitions deducted
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
def value(c, g, r, years=10):
    v=0; x=c
    for t in range(1,years+1):
        x*= (1+g); v+= x/(1+r)**t
    return v + x/r/(1+r)**years      # zero nominal growth after year ten
def irr(c,g,cost):
    lo,hi=0.001,2.0
    for _ in range(200):
        m=(lo+hi)/2
        if value(c,g,m)>cost: lo=m
        else: hi=m
    return m
def growth_halves(d):
    a=(d[2021]+d[2022])/2; b=(d[2024]+d[2025])/2
    return (b/a)**(1/3)-1, a, b
for label,d,nd,mv_adj in (('ALL-EQUITY (central)',allq,net_debt,True),('EQUITY-ONLY (beside)',eqo,0.0,False)):
    print('==',label)
    g,a,b=growth_halves(d); print('  growth between window halves FY2021-22 avg %.2f -> FY2024-25 avg %.2f: %.1f%%/yr'%(a,b,100*g))
    for base_label,ys in (('cycle base FY2022-25',range(2022,2026)),('literal window FY2021-25',range(2021,2026))):
        C=avg(d,ys)
        top=value(C,0.0,r_sov); bot=value(C,g,r_sov)
        ps=lambda v:(v-nd)/shares
        print('  %s: C=%.2f  bottom(g=%.1f%%) %.1f  top(no growth) %.1f  -> per share $%.2f to $%.2f ; width %.2fx'%(base_label,C,100*g,bot,top,ps(bot),ps(top),top/bot))
        cost = price*shares + nd
        print('     at $%.2f (cost %.1f): expected return no-growth %.1f%%, decline case %.1f%%'%(price,cost,100*irr(C,0.0,cost),100*irr(C,g,cost)))
        ftop=value(C,0.0,r_floor); fbot=value(C,g,r_floor)
        print('     fair price (ends at 10%%, averaged): $%.2f  [ends $%.2f and $%.2f]'%(((ftop+fbot)/2-nd)/shares,(fbot-nd)/shares,(ftop-nd)/shares))
# ten-year record with the 2017 acquisition deducted, beside
ten = 10.94
print('ten-year all-equity average after acquisitions %.2f: no-growth value %.1f -> $%.2f/share; at 10%% $%.2f; return at price %.1f%%'%(ten,ten/r_sov,(ten/r_sov+25.6)/shares,(ten/0.10+25.6)/shares,100*ten/(price*shares-25.6)))
