# Arithmetic only. Inputs from the filed statements (see run file for accessions).
ocf  ={2020:242.0,2021:283.9,2022:83.6,2023:356.5,2024:368.2,2025:455.8}
sbc  ={2020:15.9,2021:38.5,2022:21.9,2023:16.7,2024:26.6,2025:39.1}
capex={2020:18.2+44.2,2021:10.6+26.3,2022:18.4+10.0,2023:27.4+10.0,2024:18.8+3.3,2025:21.0+4.1}
da   ={2020:34.5,2021:36.6,2022:37.1,2023:38.0,2024:42.6,2025:47.8}
sold ={2019:188.1,2020:127.1,2021:170.6,2022:246.0,2023:197.7,2024:178.2,2025:261.4}  # sold receivables outstanding
oe={y:ocf[y]-sbc[y]-capex[y] for y in ocf}
oed={y:ocf[y]-sbc[y]-da[y] for y in ocf}
oef={y:oe[y]-(sold[y]-sold[y-1]) for y in ocf}
for y in ocf: print(y, round(oe[y],1), round(oed[y],1), 'factoring-adj', round(oef[y],1), 'chg sold', round(sold[y]-sold[y-1],1))
m=lambda d,ys: sum(d[y] for y in ys)/len(ys)
f5=range(2021,2026); w6=range(2020,2026)
v={'capex 5y':m(oe,f5),'D&A 5y':m(oed,f5),'factoring-adj 5y':m(oef,f5),'capex 6y':m(oe,w6),'factoring-adj 6y':m(oef,w6)}
for k,x in v.items(): print(k, round(x,1))
r=0.0566; sh=54.653620; price=64.19; t=0.243
def pv(c,g,n=10):
    s=0;cf=c
    for i in range(1,n+1):
        cf*=1+g; s+=cf/(1+r)**i
    return s+cf/r/(1+r)**n   # then zero nominal growth
print('mktcap',round(sh*price,1))
for k,x in v.items():
    lo=x/r; hi=pv(x,0.02)
    print(f'{k}: no-growth {lo:,.0f}M ${lo/sh:.2f}  2%-growth {hi:,.0f}M ${hi/sh:.2f}')
# fair price: pre-tax owner-cash yield + g = 10% (equity basis; owner cash is after interest)
for k in ['capex 5y','factoring-adj 5y','D&A 5y']:
    for g in (0.0,0.01,0.02):
        pre=v[k]/(1-t); P=pre/(0.10-g)
        print(f'fair {k} g={g}: {P:,.0f}M ${P/sh:.2f}  exp pre-tax return at price {(pre/(sh*price)+g)*100:.2f}%')
