# Owner cash by fiscal year (US$000), all-equity basis, from the filed cash-flow statements.
# FY2023: 424B4 (0001213900-25-042797) predecessor FY; FY2024: predecessor stub + successor period (20-F 0001193125-26-282941);
# FY2025, FY2026: 20-F 0001193125-26-282941.
yrs={
 'FY2023':dict(ocf=29030,int_rec=235,refund=0,capex=1066,intang=69,ppe_sale=18,lease=1731,lease_int=184,nci=775,rev=97462,dep=910),
 'FY2024':dict(ocf=-2890+24045,int_rec=74+55,refund=0,capex=1200+3238,intang=11,ppe_sale=698,lease=197+824,lease_int=38+915,nci=508+1208,rev=18182+163267,dep=251+3800),
 'FY2025':dict(ocf=40502,int_rec=339,refund=0,capex=2863,intang=0,ppe_sale=0,lease=1302,lease_int=253,nci=2161,rev=203607,dep=2711),
 'FY2026':dict(ocf=54118,int_rec=3593,refund=2398,capex=1114,intang=523,ppe_sale=2,lease=1468,lease_int=404,nci=1670,rev=155910,dep=4679),
}
oc={}
for y,d in yrs.items():
    v=d['ocf']-d['int_rec']-d['refund']-d['capex']-d['intang']+d['ppe_sale']-d['lease']-d['lease_int']-d['nci']
    dv=v+d['capex']+d['intang']-d['ppe_sale']-d['dep']   # depreciation variant: PP&E depreciation in place of capex
    oc[y]=v
    print(y,'owner cash',v,'dep-variant',dv,'share of sales %.1f%%'%(v/d['rev']*100))
avg=sum(oc.values())/4; print('4-yr avg',round(avg))
g=(oc['FY2026']/oc['FY2023'])**(1/3)-1; print('end-year CAGR %.1f%%'%(g*100))
h1=(oc['FY2023']+oc['FY2024'])/2; h2=(oc['FY2025']+oc['FY2026'])/2; print('halves',h1,h2,'rate %.1f%%'%(((h2/h1)**0.5-1)*100))
rv=[yrs[y]['rev'] for y in yrs]; print('sales CAGR FY23-26 %.1f%%'%(((rv[-1]/rv[0])**(1/3)-1)*100))
def value(c0,g,r,yrs=10):
    pv=0;c=c0
    for t in range(1,yrs+1):
        c*=1+g; pv+=c/(1+r)**t
    return pv + (c/r)/(1+r)**yrs
r=0.0543; netcash=151985; sh=42448704; price=3.91
for lab,gg in [('no growth',0.0),('shown growth',g)]:
    ev=value(avg,gg,r); ev10=value(avg,gg,0.10)
    print(lab,'EV@5.43 %.0f'%ev,'per share %.2f'%((ev+netcash)*1000/sh),' EV@10 %.0f'%ev10,'per share %.2f'%((ev10+netcash)*1000/sh))
mc=price*sh/1000; print('mkt cap',round(mc),'EV',round(mc-netcash),'yield on EV %.0f%%'%(avg/(mc-netcash)*100))
# equity-only: owner cash after interest = add back interest received (cash earns it), against market cap alone
eo=avg+sum(yrs[y]['int_rec'] for y in yrs)/4
print('equity-only owner cash',round(eo),'no-growth @10 per share %.2f'%(eo/0.10*1000/sh), 'growth @10 per share %.2f'%(value(eo,g,0.10)*1000/sh))
print('fair all-equity (avg of ends @10) %.2f'%(((value(avg,0,0.10)+value(avg,g,0.10))/2+netcash)*1000/sh))
print('fair equity-only %.2f'%((value(eo,0,0.10)+value(eo,g,0.10))/2*1000/sh))
print('no-growth-alone fair all-equity %.2f, equity-only %.2f'%((value(avg,0,0.10)+netcash)*1000/sh, value(eo,0,0.10)*1000/sh))
