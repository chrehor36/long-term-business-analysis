# Owner cash, all-equity basis, from the filed cash-flow statements (USD M). Sources: 10-K FY2016/FY2019/FY2022/FY2025 cash-flow
# statements and XBRL company facts (ATR_facts.json, first-filed values). Tax rate for the interest add-back = the company's own
# five-year effective rate FY2021-25: total tax / total pre-tax income.
tax = {2021:78.0,2022:95.1,2023:90.6,2024:95.6,2025:98.9}; pti={2021:321.7,2022:334.7,2023:374.8,2024:469.8,2025:491.4}
t = sum(tax.values())/sum(pti.values())
Y = {  # ocf, interest paid, sbc, capex, depreciation, intangibles bought, ppe sale proceeds, grants, acquisitions+equity stakes net
2015:(323.8,31.7,20.6,149.3,134.6,0.0,0.8,0.0,None),
2016:(325.3,36.3,19.8,129.0,145.5,2.5,1.7,0.0,203.0),
2017:(324.7,38.8,18.9,156.6,142.8,0.0,2.0,0.0,5.0),
2018:(313.6,32.0,19.6,211.3,156.3,0.6,4.5,0.0,537.9),
2019:(514.5,34.4,23.9,242.3,166.9,4.8,4.3,0.0,109.8),
2020:(570.2,33.3,34.1,246.0,180.5,6.1,5.3,0.0,203.8),
2021:(363.4,29.1,38.9,307.9,193.8,0.0,5.2,2.0,152.9),
2022:(478.6,35.5,40.9,310.4,190.1,5.2,0.1,27.8,2.5),
2023:(575.2,39.6,41.3,312.3,203.9,6.1,5.3,0.0,33.8),
2024:(643.4,43.5,47.6,276.5,219.7,17.7,1.5,0.0,99.1),
2025:(570.0,50.0,43.9,270.4,242.3,5.0,3.5,3.3,66.5)}
print('tax rate used %.1f%%'%(100*t))
M={};A={}
print('year  maint-basis  all-capex  acquisitions  all-capex-after-acq   (equity-only maint: less after-tax interest)')
for y,(o,i,s,c,d,ib,pp,g,aq) in Y.items():
    m=o+i*(1-t)-s-d-ib+pp
    a=o+i*(1-t)-s-c-ib+pp+g
    M[y]=m;A[y]=a
    print(y,'%8.1f %9.1f %9s %9s  eq-only %7.1f'%(m,a,'%.1f'%aq if aq is not None else '-', '%.1f'%(a-aq) if aq is not None else '-', m-i*(1-t)))
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
w5=range(2021,2026); cyc=range(2019,2026); prev=range(2015,2019)
acq5=sum(Y[y][8] for y in w5)/5; acqc=sum(Y[y][8] for y in cyc)/7
gs5=avg(A,w5); gsc=avg(A,cyc)
print('5yr window 2021-25: maint %.1f  all-capex %.1f  acq %.1f  all-after-acq %.1f'%(avg(M,w5),gs5,acq5,gs5-acq5))
print('cycle 2019-25:      maint %.1f  all-capex %.1f  acq %.1f  all-after-acq %.1f'%(avg(M,cyc),gsc,acqc,gsc-acqc))
print('prior span 2015-18: maint %.1f'%avg(M,prev))
g_cyc=(avg(M,cyc)/avg(M,prev))**(1/5.5)-1
print('growth, maint-basis, 2015-18 avg -> 2019-25 avg (midpoints 2016.5 -> 2022): %.1f%%/yr'%(100*g_cyc))
print('growth, window halves 2021-22 -> 2024-25 (3 yrs): %.1f%%/yr'%(100*((avg(M,[2024,2025])/avg(M,[2021,2022]))**(1/3)-1)))
# operating income growth, as filed
oi={2015:324.1,2016:310.5,2017:321.5,2018:286.3,2019:371.7,2020:339.5,2021:347.3,2022:379.3,2023:404.0,2024:496.5,2025:501.0}
print('operating income growth 2015-18 avg -> 2019-25 avg: %.1f%%/yr'%(100*((avg(oi,cyc)/avg(oi,prev))**(1/5.5)-1)))
