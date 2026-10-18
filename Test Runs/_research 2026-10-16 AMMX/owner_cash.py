# Owner cash by year, typed from the filed (2017-2021, audited) and company-published (2022-2025, unaudited) statements.
# Sources and accessions are in figures.md. Signs as printed; 2025 investing lines are printed positive (inflows).
T=0.2815  # FY2021 tax note: 21.00% federal + 7.15% state
Y={ # cfo, ppe, rental, proceeds, caplease(noncash capex), finlease principal, stock pay, interest paid, revenue, op income
2017:(1975547,-159735,-1709379,134194,0,0,0,542638,8709514,1514298),
2018:(1420165,-473757,-1936628,131165,1411604,0,0,799831,9797854,1951437),
2019:(-1525908,-419293,-375912,0,812099,0,0,747855,12655238,933701),
2020:(-256068,-141998,-611830,0,225859,0,25660,907534,12279120,-58609),
2021:(5783721,-513798,-724070,0,168061,0,46400,774074,24721838,3163966),
2022:(1906657,-67699,-1890017,0,0,0,71000,652607,19222509,1762519),
2023:(-2405549,-725941,-364804,0,0,292158,0,532297,13383499,-852010),
2024:(3743605,-252785,-6024673,0,0,346356,0,1202977,14736842,437844),
2025:(-791671,642919,4484392,0,0,292158,0,1354386,14034542,926517),
}
oc={};ae={}
for y,(c,p,r,pr,cl,fl,sp,i,rev,op) in Y.items():
    oc[y]=c+p+r+pr-cl-fl-sp
    ae[y]=oc[y]+i*(1-T)
    print(y,f"owner cash {oc[y]:>12,.0f}  all-equity {ae[y]:>12,.0f}  rev {rev:>12,.0f}  op margin {op/rev*100:5.1f}%")
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
w=range(2021,2026); full=range(2017,2026)
print('5y 2021-25 avg owner cash',f"{avg(oc,w):,.0f}",'all-equity',f"{avg(ae,w):,.0f}")
print('9y 2017-25 avg owner cash',f"{avg(oc,full):,.0f}",'all-equity',f"{avg(ae,full):,.0f}")
print('2021-25 excl. 2025 investing inflow (2025 inv set 0):', f"{(sum(oc[y] for y in w)-642919-4484392)/5:,.0f}")
