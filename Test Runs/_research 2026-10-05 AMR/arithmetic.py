# Owner cash = OCF - SBC (cash-flow line) - capex - capital contributions to equity affiliates (DTA). USD M, from filed cash-flow statements.
oc={2017:(314.260,20.372,83.121,5.691),2018:(158.381,13.354,81.881,5.253),2019:(131.880,12.397,192.411,10.051),
    2020:(129.236,4.896,153.990,3.443),2021:(174.943,5.315,83.300,6.677),2022:(1484.005,7.484,164.309,19.556),
    2023:(851.159,19.017,245.373,30.812),2024:(579.919,12.318,198.848,32.504),2025:(144.926,13.598,127.153,38.146)}
o={y:a-b-c-d for y,(a,b,c,d) in oc.items()}
for y in o: print(y, round(o[y],1))
h1=68.910-7.972-85.816-23.325; print('H1 2026',round(h1,1))
tax={2019:3.039-72.236,2020:0.005-68.801,2021:0.176-64.498,2022:139.663-0.006,2023:79.191,2024:8.379,2025:2.118}
m=lambda ys: sum(o[y] for y in ys)/len(ys)
five=m(range(2021,2026)); seven=m(range(2019,2026)); exs=m([2019,2020,2021,2024,2025]); nine=m(range(2017,2026))
r=0.0563; sh=12.679045
netcash=307.595+30.887-8.202-3.199  # 10-Q 0001704715-26-000031 balance sheet
print('netcash',round(netcash,1))
for n,v in [('five 2021-25',five),('seven 2019-25',seven),('ex-spike',exs),('nine 2017-25',nine)]:
    print(n, round(v,1), 'value/sh at sovereign no growth', round((v/r+netcash)/sh,2))
pretax7=seven+sum(tax.values())/7
print('pretax central',round(pretax7,1),'fair price', round((pretax7/0.10+netcash)/sh,2))
print('cheap (ex-spike after tax at 10%)', round((exs/0.10+netcash)/sh,2))
print('netcash/sh',round(netcash/sh,2))
# buybacks under program
for y,(s,c) in {2022:(3544413,516.845),2023:(6475271-3544413,1039.934-516.845),2024:(6630535-6475271,1098.717-1039.934),
              2025:(6878449-6630535,1138.709-1098.717),'H1-2026':(7035097-6878449,1169.704-1138.709),'all':(7035097,1169.704)}.items():
    print('buyback',y,s,round(c,1),'avg',round(c*1e6/s,2))
# margins per short ton; HCC per metric ton converted
hcc={2017:(189.94,99.86),2018:(193.72,103.35),2019:(170.72,99.15),2020:(113.12,92.31),2021:(180.43,96.43),2022:(334.89,138.35),2023:(241.64,132.60),2024:(207.32,138.10),2025:(146.20,111.66)}
amr={2019:25.85,2020:10.71,2021:37.47,2022:117.22,2023:67.73,2024:30.64,2025:14.85}
metc={2019:35,2020:14,2021:39,2022:99,2023:59,2024:35,2025:22}
h={y:(p-c)/1.10231 for y,(p,c) in hcc.items()}
print({y:round(v,1) for y,v in h.items()})
ys=range(2019,2026)
print('2019-25 mean margin/st AMR',round(sum(amr[y] for y in ys)/7,1),'HCC',round(sum(h[y] for y in ys)/7,1),'METC',round(sum(metc[y] for y in ys)/7,1))
print('price/cap', 175.05*sh)
