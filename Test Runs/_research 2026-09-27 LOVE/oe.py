# Owner earnings per [E2-23] from the filed cash-flow statements (thousands), latest vintage.
# OE = OCF - SBC - (c); (c) shown at two ends: full capex (PP&E + patents/trademarks) and D&A (PP&E + intangibles).
# OCF here is already after operating-lease payments (the statement deducts "Operating lease liabilities").
import json
x=json.load(open('xb_rows.json'))
k=lambda t,y: x[t][str(y)]/1000
S={
2017:dict(ocf=-6476.9,sbc=25.7,capex=3680.6+304.8,da=1828.9+281.2,src='424B1 2018-10-30'),
2018:dict(ocf=-2740.3,sbc=950.6,capex=6636.5+172.9,da=1996.2+218.3,src='424B1 2018-10-30'),
}
for y in range(2019,2027):
    S[y]=dict(ocf=k('OCF',y),sbc=k('SBC',y),capex=k('Capex',y)+k('IntangBuy',y),da=k('DA',y),src='companyfacts, checked to the filed statement')
# filed-statement overrides where read directly
S[2020].update(ocf=-11194,sbc=5246,capex=10277+674,da=4894+264)
S[2021].update(ocf=40521,sbc=4681,capex=8374+678,da=6100+513)
S[2022].update(ocf=32648,sbc=5859,capex=14615+503)   # FY2024 10-K revised column
S[2023].update(ocf=-21375,sbc=10450,capex=25242+307)  # restated
S[2024].update(ocf=76441,sbc=4216,capex=28736+475,da=12174+429)
S[2025].update(ocf=38977,sbc=7945,capex=21026+491,da=14292+418)
S[2026].update(ocf=49328,sbc=5510,capex=23135+885,da=14887+319)
TTM=dict(ocf=49328-11429+29212,sbc=5510+4362-5767,capex=24020+12204-13196,da=15206+8390-7449)
cap=219092
print('FY    OCF      SBC    capex    D&A   OE@capex  OE@D&A')
for y in sorted(S):
    s=S[y]; a=s['ocf']-s['sbc']-s['capex']; b=s['ocf']-s['sbc']-s['da']; s['a']=a; s['b']=b
    print('%d %8.1f %7.1f %7.1f %7.1f %8.1f %8.1f'%(y,s['ocf']/1e3,s['sbc']/1e3,s['capex']/1e3,s['da']/1e3,a/1e3,b/1e3))
a=TTM['ocf']-TTM['sbc']-TTM['capex']; b=TTM['ocf']-TTM['sbc']-TTM['da']
print('TTM  %8.1f %7.1f %7.1f %7.1f %8.1f %8.1f   (incl. $20.0M IEEPA tariff refund in cost of goods, $21.0M cash)'%(TTM['ocf']/1e3,TTM['sbc']/1e3,TTM['capex']/1e3,TTM['da']/1e3,a/1e3,b/1e3))
print('TTM ex-refund OE: %.1f to %.1f'%((a-21000)/1e3,(b-21000)/1e3))
print('\nWindows ending FY2026 (mean OE $M, yield on cap $219.1M):')
ys=sorted(S)
for n in range(1,len(ys)+1):
    w=ys[-n:]; ma=sum(S[y]['a'] for y in w)/n; mb=sum(S[y]['b'] for y in w)/n
    print('  %2d-yr FY%d-FY2026: %7.1f to %7.1f   yield %5.2f%% to %5.2f%%'%(n,w[0],min(ma,mb)/1e3,max(ma,mb)/1e3,100*min(ma,mb)/cap,100*max(ma,mb)/cap))
cumocf=sum(S[y]['ocf'] for y in ys); cumsbc=sum(S[y]['sbc'] for y in ys)
print('\nCumulative FY2017-FY2026: OCF %.1f, SBC %.1f (%.1f%% of OCF), capex %.1f, OE@capex %.1f, OE@D&A %.1f'%(cumocf/1e3,cumsbc/1e3,100*cumsbc/cumocf,sum(S[y]['capex'] for y in ys)/1e3,sum(S[y]['a'] for y in ys)/1e3,sum(S[y]['b'] for y in ys)/1e3))
json.dump({str(y):S[y] for y in S},open('oe_rows.json','w'),indent=0)
