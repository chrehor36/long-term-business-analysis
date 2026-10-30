# COMPUTATION, NOT A CLEARANCE. SHOP owner cash and the Q7 range convention, FY2021-FY2025.
# Inputs: filed statements (10-K FY2025 0001594805-26-000007 for 2023-2025; XBRL first-filed vintage for 2021-2022,
# 40-F FY2022 0001594805-23-000011 and FY2021 0001594805-22-000011), USD millions.
yrs  = [2021, 2022, 2023, 2024, 2025]
ocf  = [504.4, -136.4, 944, 1616, 2033]
sbc  = [330.8, 549.1, 615, 430, 449]
capx = [50.8, 50.0, 39, 19, 26]
loan_out = [198.5, 525.5, 1861, 3006, 4014]
loan_in  = [167.2, 366.9, 1338, 2542, 3435]
acq  = [59.6, 1753.7, 31, 30, 56]
intinc = [15.4, 79.1, 241, 308, 331]
rev  = [4611.9, 5599.9, 7060, 8880, 11556]
T = 278/1509   # 2025 effective tax rate, used to take interest income out after tax (CONVENTION of this run)
net_loans = [a-b for a, b in zip(loan_out, loan_in)]
int_at = [i*(1-T) for i in intinc]
def series(loans=True, acqs=True, interest_out=True):
    out = []
    for k in range(5):
        v = ocf[k] - sbc[k] - capx[k]
        if loans: v -= net_loans[k]
        if acqs: v -= acq[k]
        if interest_out: v -= int_at[k]
        out.append(v)
    return out
R = 0.056; F = 0.10
def pv(base, g, r):
    tot = 0; cf = base
    for t in range(1, 11):
        cf = cf*(1+g); tot += cf/(1+r)**t
    tot += (cf/r)/(1+r)**10   # zero nominal growth after year ten
    return tot
def nogrowth(base, r): return base/r
shares = 1208.570347 + 78.073584   # millions, cover of 10-Q 0001594805-26-000047 as of 2026-07-31
netcash = 1656 + 3291 + 525        # 2026-06-30: cash, marketable securities, long-term investments; no borrowings
eqinv_fv = 3299                    # equity and other investments carried at fair value, shown beside
price = 170.85
print("effective tax rate used for interest", round(T,4))
print("net loan originations", [round(x,1) for x in net_loans])
for name, kw in [("A central: acquisitions and net loans deducted, interest out", dict()),
                 ("B organic pair: acquisitions left out", dict(acqs=False)),
                 ("C as-filed investing: loans not deducted, acquisitions left out", dict(acqs=False, loans=False)),
                 ("D equity-only: interest kept, acquisitions and loans deducted", dict(interest_out=False))]:
    s = series(**kw); m = sum(s)/5
    print(name, [round(x,1) for x in s], "mean", round(m,1), "first half", round((s[0]+s[1])/2,1), "second half", round((s[3]+s[4])/2,1))
    print("   share of sales", [round(x/r*100,2) for x, r in zip(s, rev)])
    v = nogrowth(m, R); print("   no-growth value $M", round(v), "per share all-equity", round((v+netcash)/shares,2))
print("revenue CAGR 2021-2025", round((rev[-1]/rev[0])**0.25-1,4))
# Beside cases, generous to the business, NOT the convention's central figure:
g = (rev[-1]/rev[0])**0.25-1
for label, base in [("E 2025 year alone, central definition", series()[-1]), ("F 2025 year alone, loans not deducted, acq out", series(acqs=False, loans=False)[-1])]:
    lo = nogrowth(base, R); hi = pv(base, g, R)
    lo10 = nogrowth(base, F); hi10 = pv(base, g, F)
    print(label, "base", round(base,1))
    print("   range at 5.6%: $M", round(lo), round(hi), " per share", round((lo+netcash)/shares,2), round((hi+netcash)/shares,2))
    print("   at 10%: $M", round(lo10), round(hi10), " fair per share", round(((lo10+hi10)/2+netcash)/shares,2))
    print("   year-10 owner cash share of 2025 sales grown at same rate", round(base/rev[-1]*100,2), "%")
print("market cap $M", round(price*shares), "EV $M", round(price*shares-netcash))
print("net cash per share", round(netcash/shares,2), "with fair-value equity investments", round((netcash+eqinv_fv)/shares,2))
