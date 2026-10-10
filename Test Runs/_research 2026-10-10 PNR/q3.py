"""Q3/Q4 arithmetic from the filed statements (values in $M as filed; sources in the run file)."""
yrs=[2018,2019,2020,2021,2022,2023,2024,2025]
equity=dict(zip(yrs,[1836,1954,2106,2422,2708,3217,3563,3869.2]))
debt  =dict(zip(yrs,[788,1029,840,894,2317,1988,1648,1638.6]))
cash  =dict(zip(yrs,[74,82,82,94,109,170,119,101.6]))
gw    =dict(zip(yrs,[2073,2258,2392,2504,3253,3275,3287,3538.1]))
intg  =dict(zip(yrs,[276,339,326,428,1095,1042,1034,1073.3]))
opinc =dict(zip(yrs,[437,432,461,637,595,739.2,803.8,857.5]))
amort =dict(zip(yrs,[None,31.7,28.4,26.3,52.5,55.3,54.3,58.1]))
sales =dict(zip(yrs,[2965,2957,3018,3765,4122,4104.5,4082.8,4176.0]))
ar    ={2019:502.9,2020:367.5,2021:534.3,2022:531.5,2023:561.7,2024:565.2,2025:673.2}
inv   ={2018:387.5,2019:377.4,2020:420.0,2021:562.9,2022:790.0,2023:677.7,2024:610.9,2025:632.6}
for y in yrs:
    ce=equity[y]+debt[y]-cash[y]; tc=ce-gw[y]-intg[y]
    s=f"{y} capital employed {ce:7.0f}  pretax return {opinc[y]/ce*100:5.1f}%  tangible capital {tc:6.0f}"
    if amort[y]: s+=f"  (opinc+amort)/tangible {(opinc[y]+amort[y])/tc*100:6.0f}%"
    if y in ar: s+=f"  AR/sales {ar[y]/sales[y]*100:4.1f}%"
    s+=f"  inv/sales {inv[y]/sales[y]*100:4.1f}%"
    print(s)
ce18=equity[2018]+debt[2018]-cash[2018]; ce25=equity[2025]+debt[2025]-cash[2025]
print(f"incremental 2018->2025: capital +{ce25-ce18:.0f}, operating income +{opinc[2025]-opinc[2018]:.0f}, pretax {((opinc[2025]-opinc[2018])/(ce25-ce18))*100:.1f}%")
acq=287.8+58.0+338.5+1580.9+0.6+108.0+292.1-1.4-15.3
print(f"acquisitions net of business sales 2019-2025: {acq:.0f}")
