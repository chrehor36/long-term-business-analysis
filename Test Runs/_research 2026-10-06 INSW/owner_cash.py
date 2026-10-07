# All USD millions, from INSW 10-K cash flow statements (accessions in run file). Owner cash = OCF (after drydock) - SBC - vessel exp + vessel sale proceeds - noncash debt-financed vessel purchases.
Y=list(range(2014,2026))
ocf ={2014:-223.3,2015:260.2,2016:129.0,2017:17.4,2018:-12.5,2019:87.5,2020:216.1,2021:-76.2,2022:287.8,2023:688.4,2024:547.1,2025:380.1}
oneoff={2014:285.3}  # OSG bankruptcy claim payments inside 2014 OCF, added back
dry ={2014:12.1,2015:20.7,2016:9.3,2017:21.4,2018:4.5,2019:19.5,2020:25.6,2021:42.4,2022:43.3,2023:34.5,2024:58.6,2025:84.2}
sbc ={2014:0.6,2015:2.8,2016:2.8,2017:3.8,2018:3.2,2019:4.3,2020:5.6,2021:10.5,2022:6.7,2023:8.5,2024:9.0,2025:8.7}
da  ={2014:84.9,2015:81.7,2016:79.9,2017:78.9,2018:72.4,2019:75.7,2020:74.3,2021:86.7,2022:110.4,2023:129.0,2024:149.4,2025:163.6}
vexp={2014:21.5,2015:1.0,2016:2.9,2017:173.9,2018:150.0,2019:37.2,2020:50.6,2021:79.0,2022:116.7,2023:206.7,2024:280.2,2025:341.9}  # vessels + other property
proc={2014:78.4,2015:17.1,2016:0.0,2017:18.3,2018:169.3,2019:15.8,2020:73.1,2021:165.8,2022:99.2,2023:66.0,2024:71.9,2025:246.3}
ncv ={2018:311.0}  # debt assumed on six VLCCs, non-cash investing (FY2018 10-K)
sh  ={2014:29.2,2015:29.2,2016:29.2,2017:29.2,2018:29.1,2019:29.2,2020:28.5,2021:39.5,2022:49.4,2023:49.0,2024:49.3,2025:49.3}  # weighted basic, millions (2014-15 = 2016 spin count)
ni  ={2014:-119.1,2015:173.2,2016:-18.2,2017:-106.1,2018:-88.9,2019:-0.8,2020:-5.5,2021:-134.7,2022:387.9,2023:556.4,2024:416.7,2025:309.3}
rows=[]
for y in Y:
    o=ocf[y]+oneoff.get(y,0)
    capex_basis=o-sbc[y]-vexp[y]+proc[y]-ncv.get(y,0)
    da_basis=o+dry[y]-sbc[y]-da[y]
    rows.append((y,o,capex_basis,da_basis,capex_basis/sh[y],da_basis/sh[y]))
    print(f"{y} OCFadj {o:7.1f} capex-basis {capex_basis:7.1f} DA-basis {da_basis:7.1f}  /sh {capex_basis/sh[y]:6.2f} {da_basis/sh[y]:6.2f}  NI {ni[y]:7.1f}")
def avg(a,b,i): s=[r for r in rows if a<=r[0]<=b]; return sum(r[i] for r in s)/len(s)
for a,b in [(2021,2025),(2016,2025),(2014,2025),(2016,2020)]:
    print(a,b,'mean $M capex %.1f DA %.1f ; per share capex %.2f DA %.2f'%(avg(a,b,2),avg(a,b,3),avg(a,b,4),avg(a,b,5)))
