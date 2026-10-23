# Q7 arithmetic for the DUK run. Inputs: filed cash-flow statements (10-K FY2021 0001326160-22-000072, FY2023 0001326160-24-000037,
# FY2025 0001326160-26-000014) via the companyfacts first-filed values, checked against the FY2025 filed statement for 2023-2025.
# USD millions. Arithmetic only; every choice is stated in the run file.
import sys
sys.stdout.reconfigure(encoding='utf-8')
Y   = [2021, 2022, 2023, 2024, 2025]
OCF = [8290, 5927, 9878, 12328, 12330]
SBC = [88, 100, 97, 96, 102]
LEA = [219, 151, 160, 113, 64]          # finance-lease principal (financing section)
PRF = [106, 106, 106, 106, 56]          # preferred dividends
NCD = [66, 140, 59, 32, 31]             # distributions to noncontrolling interests
CAP = [9715, 11367, 12604, 12280, 14024]
OTH = [333, 644, 799, 1009, 1079]       # "Other" investing outflow (not explained in MD&A)
DA  = [5663, 5843, 6084, 6419, 7704]    # cash-flow line: depreciation, amortization and accretion incl. nuclear fuel
ISS = [9052, 11874, 10028, 8956, 11891] # long-term debt issued
RED = [5294, 4396, 4737, 3357, 5652]    # long-term debt redeemed
INT = [2248, 2361, 2883, 3284, 3590]    # cash interest paid, net of capitalized
REV = [24703, 28675, 28674, 30050, 31741]
DEBT_SHARE = 0.47                        # allowed debt share: 53% equity in the NC cases (10-K Item 1 table)
SH = 779.702; MCAP = SH*121.47
NETDEBT = 2330 + 6666 + 82242 - 673 + 2000   # 10-Q 2026-06-30 borrowings less cash, plus the $2,000M equity-unit notes (8-K 2026-08-13)
SOV = 0.0543; FLOOR = 0.10
mean = lambda s: sum(s)/len(s)
netdebt = [i-r for i,r in zip(ISS,RED)]
def V(c0,g,r):
    pv=0; c=c0
    for t in range(1,11):
        c=c*(1+g); pv+=c/(1+r)**t
    return pv + c/r/(1+r)**10
def irr(c0,g,target):
    lo,hi=0.0001,0.5
    for _ in range(100):
        m=(lo+hi)/2
        if V(c0,g,m)>target: lo=m
        else: hi=m
    return m
def growth(series):
    a,b=series[0],series[-1]
    if a>0 and b>0: return (b/a)**(1/4)-1, 'end years'
    h1=mean(series[:2]); h2=mean(series[-2:])
    if h1>0 and h2>0: return (h2/h1)**(1/3)-1, 'halves (sign change or non-positive end year)'
    return None, 'meaningless'
sales_g=(REV[-1]/REV[0])**(1/4)-1
print('sales growth 2021-2025 %.2f%%' % (sales_g*100))
cases={}
M  =[o-s-l-p-n-d for o,s,l,p,n,d in zip(OCF,SBC,LEA,PRF,NCD,DA)]
Mc =[m+min(nd,DEBT_SHARE*d) for m,nd,d in zip(M,netdebt,DA)]
A  =[o-s-l-p-n-c+min(nd,DEBT_SHARE*c) for o,s,l,p,n,c,nd in zip(OCF,SBC,LEA,PRF,NCD,CAP,netdebt)]
Ao =[a-x for a,x in zip(A,OTH)]
A0 =[o-s-l-p-n-c for o,s,l,p,n,c in zip(OCF,SBC,LEA,PRF,NCD,CAP)]
for name,s in [('M maintenance-only, no debt credit (central)',M),('M+credit maintenance-only, debt credit to 47% of maintenance',Mc),
               ('A all spending, net LT debt credited to 47% of capex',A),('A-oth same, less Other investing',Ao),('A0 all spending, no credit (literal)',A0)]:
    print('\n==',name); print('  by year', [round(x) for x in s], 'mean', round(mean(s)))
    print('  debt credit by year', [round(min(nd,DEBT_SHARE*c)) for nd,c in zip(netdebt,CAP)] if name.startswith('A') else '')
    g,how=growth(s); c0=mean(s)
    if c0<=0: print('  mean not positive: no value'); continue
    shares=[x/r for x,r in zip(s,REV)]; mx=max(shares)
    gc=g
    if g is not None:
        y10=c0*(1+g)**10; s10=REV[-1]*(1+sales_g)**8  # sales in year 10 from the 2023 midpoint base, carried at sales growth
        cut = g>SOV or (y10/s10>mx)
        print('  shown growth %.2f%% (%s); owner cash at yr10 / sales at yr10 = %.1f%% vs highest share in window %.1f%%' % (g*100,how,100*y10/s10,100*mx))
        if cut: gc=min(sales_g,SOV); print('  cut (f): carried at sales growth, not above the discount rate: %.2f%%' % (gc*100))
    else: gc=0; print('  growth meaningless: no-growth case alone')
    lo=V(c0,0,SOV); hi=V(c0,gc,SOV)
    lo10=V(c0,0,FLOOR); hi10=V(c0,gc,FLOOR)
    print('  range at sovereign: $%.2f to $%.2f a share (width %.2fx); vs price $121.47' % (lo/SH, hi/SH, hi/lo))
    print('  return at the price: no-growth case %.2f%%, growth case %.2f%%' % (100*irr(c0,0,MCAP),100*irr(c0,gc,MCAP)))
    print('  fair price (each end at 10%%, averaged): $%.2f' % ((lo10+hi10)/2/SH))
    cases[name]=(c0,gc)
# all-equity beside: owner cash before interest (interest paid less a 21% shield), no debt credit, less net debt
print('\n== ALL-EQUITY BESIDE, net debt %d' % NETDEBT)
for name,s in [('maintenance-only',M),('all spending',A0)]:
    u=[x+i*0.79 for x,i in zip(s,INT)]; c0=mean(u)
    print(name,'unlevered by year',[round(x) for x in u],'mean',round(c0))
    if c0<=0: print('  not positive'); continue
    g,how=growth(u); gc = min(sales_g,SOV) if (g is None or g>SOV) else g
    lo=V(c0,0,SOV)-NETDEBT; hi=V(c0,gc,SOV)-NETDEBT; lo10=V(c0,0,FLOOR)-NETDEBT; hi10=V(c0,gc,FLOOR)-NETDEBT
    print('  growth shown %s (%s), carried %.2f%%; range $%.2f to $%.2f; fair $%.2f' % (g and round(g*100,2),how,gc*100,lo/SH,hi/SH,(lo10+hi10)/2/SH))
print('\nmarket cap', round(MCAP), 'net LT debt raised by year', netdebt)

# BESIDE: Q7 "Whose tax" carryforward clause, applied as far as the filing allows.
# (i) transferable-credit receipts in OCF (723, 558, 28 in 2025, 2024, 2023; 10-K cash-flow statement) are owed back to customers
#     (Note 4, "Deferred nuclear PTC"); removed from owner cash.  (ii) carryforward shelter: NOL and credit carryforwards utilized,
#     $523M (FY2024 tax note, the one year stated), taken as the annual shelter until "around 2030" (Item 7): owner cash lowered by it
#     every year, and its present value for four years (2026-2029) added back.
CR = [0, 0, 28, 558, 723]
SHELTER = 523
Mt = [m - c - SHELTER for m, c in zip(M, CR)]
c0 = mean(Mt); g, how = growth(Mt)
gc = min(sales_g, SOV)
ann = lambda r: sum(1/(1+r)**t for t in range(1,5))
lo = V(c0,0,SOV)+SHELTER*ann(SOV); hi = V(c0,gc,SOV)+SHELTER*ann(SOV)
lo10 = V(c0,0,FLOOR)+SHELTER*ann(FLOOR); hi10 = V(c0,gc,FLOOR)+SHELTER*ann(FLOOR)
print('\n== M tax-adjusted beside: by year', [round(x) for x in Mt], 'mean', round(c0), 'shown growth', g and round(g*100,2), how, 'carried %.2f%%' % (gc*100))
print('  range $%.2f to $%.2f; returns at price %.2f%% / %.2f%%; fair $%.2f' % (lo/SH, hi/SH, 100*irr(c0,0,MCAP-SHELTER*ann(0.05)), 100*irr(c0,gc,MCAP-SHELTER*ann(0.05)), (lo10+hi10)/2/SH))
