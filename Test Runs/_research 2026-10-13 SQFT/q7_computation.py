# COMPUTATION, NOT A CLEARANCE. Figures from the filed cash flow statements (10-K FY2021 0001437749-22-007590,
# FY2023 0001437749-24-012113, FY2025 0001437749-26-010114) and the 10-Q for 2026-06-30 (0001437749-26-027591).
yrs=[2021,2022,2023,2024,2025]
ocf={2021:2374943,2022:928817,2023:1489839,2024:-728060,2025:417870}
capex={2021:1597186+117062,2022:2107505+70889,2023:6663116-7744,2024:2273726,2025:2703012}  # buildings and TI, plus deferred leasing costs where in investing
interest={2021:4320174+103861,2022:4110288,2023:4962458,2024:5371017,2025:5906234}  # interest paid, supplemental
nci={2021:7588197,2022:4412046,2023:1676639,2024:3629964,2025:1277913}  # distributions to noncontrolling interests, net
eq={y:ocf[y]-capex[y] for y in yrs}            # equity-only owner cash (after interest), before NCI distributions
ae={y:eq[y]+interest[y] for y in yrs}          # all-equity owner cash (before interest); REIT: company tax ~nil (income tax paid 2025 $78,848)
for y in yrs: print(y, f"eq {eq[y]:>12,.0f}  all-equity {ae[y]:>12,.0f}  after NCI dist {eq[y]-nci[y]:>12,.0f}")
avg_ae=sum(ae.values())/5; avg_eq=sum(eq.values())/5
print(f"avg all-equity {avg_ae:,.0f}  avg equity-only {avg_eq:,.0f}")
# growth: series has a negative year (2023), so (b): first half (2021-22) vs second half (2024-25), three years apart
h1=(ae[2021]+ae[2022])/2; h2=(ae[2024]+ae[2025])/2
g=(h2/h1)**(1/3)-1
print(f"half averages {h1:,.0f} -> {h2:,.0f}, g={g:.4%}")
r=0.056
def value(c,g,r):
    v=0; cf=c
    for t in range(1,11):
        cf=cf*(1+g); v+=cf/(1+r)**t
    v+=cf/r/(1+r)**10   # zero nominal growth after year ten
    return v
top=value(avg_ae,0.0,r); bot=value(avg_ae,g,r)
print(f"EV no-growth {top:,.0f}; EV decline {bot:,.0f}")
# claims ahead of the common, latest filed date 2026-06-30 with the subsequent events the filings state
debt=80858050; cash=5902592
shea=16353296; shea_cash=2400000   # foreclosure 2026-07-01 extinguishes the loan; lender keeps ~$2.4M restricted cash
netdebt=debt-cash-shea+shea_cash
pref_sh=973736-149773; pref=pref_sh*25.0
arrears=pref_sh*(1331263/973736 + 2*0.19531)   # arrears to 2026-07-31 per share, plus Aug and Sep accruals
nci_book=7570650
shares=1434432+823753
print(f"net debt {netdebt:,.0f}; preferred liq {pref:,.0f} + arrears {arrears:,.0f}; NCI book {nci_book:,.0f}; shares {shares:,}")
for name,ev in (('no-growth',top),('decline',bot)):
    a=(ev-netdebt)/shares; b=(ev-netdebt-pref-arrears-nci_book)/shares
    print(f"{name}: per share less net debt only {a:,.2f}; less net debt, preferred and NCI {b:,.2f}")
# fair price: each end valued at 10%
ft=value(avg_ae,0.0,0.10); fb=value(avg_ae,g,0.10)
fp=((ft+fb)/2-netdebt)/shares; fp2=((ft+fb)/2-netdebt-pref-arrears-nci_book)/shares
print(f"fair (all-equity, at 10%): EV ends {ft:,.0f} / {fb:,.0f}; per share less net debt {fp:,.2f}; less all senior claims {fp2:,.2f}")
print("equity-only: average owner cash after interest is negative, so every case values the common below zero")
price=0.859
print(f"market value of common at ${price}: {price*shares:,.0f}")
