# HTCMY after-tax operating return on capital employed, and on tangible capital, from the filed statements (millions of yen).
# capital = total equity + bonds and borrowings - cash, at March 31 (leases left out: their cost is inside operating income).
# Sources: statements of financial position, 53rd to 62nd Annual Securities Reports (latest filed figure for each date).
cap = {2016:(456816,111888+106007,79110,8694+9611), 2017:(450430,153883+94818,65455,36640+40088), 2018:(505030,69892+160773,81929,35016+37748),
       2019:(542661,185641+119167,67347,34564+42092), 2020:(525111,160447+178496,62165,30538+37883), 2021:(569245,150262+179226,80330,35406+41576),
       2022:(667931,174337+178770,94257,39071+42008), 2023:(701040,310944+196523,111992,40421+39704), 2024:(814413,396302+179280,143530,58271+43630),
       2025:(857952,326693+211165,147136,58540+46703), 2026:(955670,316159+181407,141456,63809+49050)}   # key = March 31 of that year
opinc = {2016:23622,2017:95737,2018:102296,2019:72849,2020:28235,2021:106590,2022:135665,2023:162690,2024:154730,2025:130144}  # FY starting April of key
T=0.306; tot=[];totT=[]
for fy,oi in opinc.items():
    a=cap[fy]; b=cap[fy+1]
    ce=lambda x: x[0]+x[1]-x[2]
    avg=(ce(a)+ce(b))/2; avgT=avg-(a[3]+b[3])/2
    r=oi*(1-T)/avg; rT=oi*(1-T)/avgT; tot.append(r); totT.append(rT)
    print(f"FY{fy}: op inc {oi:,}  avg capital {avg:,.0f}  after-tax return {r:.1%}  on tangible {rT:.1%}")
print(f"ten-year average {sum(tot)/10:.1%}; tangible {sum(totT)/10:.1%}")
