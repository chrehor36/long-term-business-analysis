"""Owner cash for SSAB, SEK m, from the filed consolidated cash flow statements (annual reports 2016-2025).
Equity-only = CFO (after interest and tax, includes working capital) - (investments in intangible+tangible
fixed assets - sales of same; this nets emission-allowance purchases and sales, which the filer runs through
these lines) - (acquisitions - divestments) - lease principal (total lease cash outflow less lease interest;
IFRS 16 from 2019; before 2019 operating leases were already inside CFO).
All-equity = equity-only + (interest paid less lease interest - interest received) x (1 - 20.6%).
Maintenance case adds back the filer's 'strategic expenditures in plant and machinery'."""
T=0.206
d={ # yr: CFO, int_recv, int_paid, capex_gross, capex_sales, acq, divest, lease_total, lease_int, strategic, revenue
2016:(3297,28,1022,1326,45,46,0,0,0,273,55354),
2017:(6650,311,1254,1603,51,11,1,0,0,237,66059),
2018:(6750,237,778,2451,142,11,76,0,0,397,74941),
2019:(5341,239,694,2939,15,1140,118,818,128,1035,76485),
2020:(4366,111,655,2204,114,233,143,744,130,582,65396),
2021:(14873,139,512,3382,1235,130,0,742,127,835,95891),
2022:(18156,457,474,4948,1537,433,0,806,127,1952,128745),
2023:(21473,1213,776,6567,1264,52,61,865,204,1889,119489),
2024:(11896,1315,854,8215,1646,38,0,910,197,2601,103418),
2025:(10079,278,420,13532,2720,139,144,961,185,7215,96220)}
rows={}
for y,(cfo,ir,ip,cg,cs,aq,dv,lt,li,st,rev) in d.items():
    lp=lt-li
    eq=cfo-(cg-cs)-(aq-dv)-lp
    ae=eq+(ip-li-ir)*(1-T)
    rows[y]=dict(eq=eq,ae=ae,eqm=eq+st,aem=ae+st,rev=rev,acq=aq-dv)
    print(y, f"equity-only {eq:7.0f}  all-equity {ae:7.0f}  maint eq {eq+st:7.0f}  maint ae {ae+st:7.0f}  rev {rev}  net acq {aq-dv}")
def avg(k,ys): return sum(rows[y][k] for y in ys)/len(ys)
A=range(2016,2021); B=range(2021,2026); C=range(2016,2026)
for k in ('eq','ae','eqm','aem','rev'):
    print(k, 'avg16-20 %.0f  avg21-25 %.0f  avg16-25 %.0f' % (avg(k,A),avg(k,B),avg(k,C)))
print('net acquisitions 2021-25', sum(rows[y]['acq'] for y in B), ' 2016-25', sum(rows[y]['acq'] for y in C))
