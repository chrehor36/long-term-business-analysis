# Q2 competitor row: same metrics from each company's own filings (USD or CAD millions).
# FIX: XBRL company facts (CIK 1035983), first-filed annual values; accessions printed by facts.py.
fix = {  # year: (revenue, gross profit, operating income, amortization of intangibles, goodwill impairment, net income incl NCI, equity)
2009:(1128.9,225.6,56.6,3.5,0.0,34.2,None),2010:(1108.3,188.7,20.0,6.2,5.7,14.7,312.8),2011:(1240.0,181.5,-49.4,7.5,58.9,-36.5,264.6),
2012:(1331.2,207.6,22.3,8.8,0.0,11.8,270.4),2013:(1357.3,239.9,46.3,7.1,0.0,28.6,295.8),2014:(1410.8,249.8,42.2,7.7,0.7,28.6,306.3),
2015:(1580.5,318.1,90.0,7.5,0.0,57.4,346.7),2016:(1634.3,344.0,101.6,8.2,0.0,64.9,376.6),2017:(1787.9,366.3,99.3,17.4,1.1,55.3,417.9),
2018:(2182.9,446.3,150.2,20.1,0.0,112.9,498.0),2019:(2615.3,501.9,163.6,27.1,0.0,114.3,585.3),2020:(2856.7,547.0,190.7,32.7,0.0,150.1,696.4),
2021:(3073.6,563.2,188.4,40.5,0.0,143.3,805.7),2022:(4140.4,741.6,253.8,47.8,0.0,245.9,999.9),2023:(5206.8,990.5,418.4,43.4,0.0,323.4,1277.8),
2024:(7027.5,1476.4,749.4,97.3,0.0,522.4,1704.7),2025:(9101.6,2195.9,1314.6,79.6,0.0,1022.6,2448.8)}
# LGN: 10-K FY2025 (2023-2025), IPO 424B4 (2022); amortization of intangibles from the cash-flow statements; impairments incl long-lived.
lgn = {2022:(1246.5,233.7,-24.2,76.5,23.4,-82.3,540.6),2023:(1615.1,315.1,10.3,70.1,5.1,-46.0,522.9),
       2024:(2098.6,430.8,70.4,81.0,17.8,-27.6,203.6),2025:(2550.5,535.9,61.6,82.3,27.4,-77.3,788.8)}
lgn_im_gm = {2023:167.254/1188.816, 2024:225.682/1497.000, 2025:297.056/1824.198}
# Stantec (CAD): XBRL company facts (CIK 1131383), revenue (gross), profit, equity attributable to owners
stn = {2016:(4300.1,130.5,1975.7),2017:(5140.1,97.0,1896.3),2018:(4283.8,47.4,1906.9),2019:(4827.3,194.4,1875.5),
       2020:(4730.1,171.1,1928.5),2021:(4576.8,200.7,2001.7),2022:(5677.2,247.0,2286.0),2023:(6479.6,331.2,2756.6),
       2024:(7500.0,361.5,2945.1),2025:(8144.2,479.4,3240.4)}
print("FIX  year  gross%  EBITA%  ROE(avg eq)")
prev=None
for y,(r,g,o,a,i,n,e) in sorted(fix.items()):
    roe = (n/((e+prev)/2)) if (e and prev) else None
    print(y, f"{g/r:6.1%} {(o+a+i)/r:6.1%}", f"{roe:6.1%}" if roe is not None else "   n/a")
    prev=e
print("LGN  year  gross%  EBITA%  I&M gross%  net margin")
for y,(r,g,o,a,i,n,e) in sorted(lgn.items()):
    print(y, f"{g/r:6.1%} {(o+a+i)/r:6.1%}", f"{lgn_im_gm[y]:6.1%}" if y in lgn_im_gm else "   n/a", f"{n/r:6.1%}")
print("STN  year  net margin  ROE(avg eq)")
prev=None
for y,(r,n,e) in sorted(stn.items()):
    roe = n/((e+prev)/2) if prev else None
    print(y, f"{n/r:6.1%}", f"{roe:6.1%}" if roe else "   n/a"); prev=e
