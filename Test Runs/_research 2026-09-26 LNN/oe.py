# owner earnings the framework's way: OCF as filed (latest 10-K showing each year) - SBC - (c); (c) = total capex (capex end) or D&A less acquired-intangible amortisation (D&A end)
Y=list(range(2010,2026))
OCF=dict(zip(Y,[23.833,43.055,52.439,57.505,91.798,49.293,33.125,39.449,33.934,3.797,46.034,43.968,3.048,119.707,95.761,132.910]))
CAPEX=dict(zip(Y,[5.784,8.405,9.890,11.136,17.715,15.244,11.496,8.863,11.054,23.211,21.445,26.511,15.595,18.775,28.979,42.496]))
SBC=dict(zip(Y,[2.206,3.474,3.939,4.573,4.207,3.332,3.060,3.598,3.891,4.195,5.616,6.186,5.458,6.529,6.392,8.059]))
DA=dict(zip(Y,[10.710,11.734,12.468,12.600,14.793,16.412,16.881,16.678,16.514,14.018,19.396,19.177,20.178,19.282,21.200,20.896]))
AMORT=dict(zip(Y,[2.6,2.8,2.9,2.8,4.0,4.7,4.7,4.4,4.0,2.9,2.5,2.2,2.0,2.0,2.9,2.2]))
ACQ=dict(zip(Y,[6.4,6.2,0,29.0,0,69.5,0,0,0,0,3.0,0,0,30.8,0,5.8]))  # 2025 = equity-method investment
CAP=1161.8
print('year OCF SBC D&A amort capex OE_DAend OE_capexend')
oe_c={};oe_d={}
for y in Y:
    oe_c[y]=OCF[y]-SBC[y]-CAPEX[y]; oe_d[y]=OCF[y]-SBC[y]-(DA[y]-AMORT[y])
    print(y,OCF[y],SBC[y],DA[y],AMORT[y],CAPEX[y],round(oe_d[y],1),round(oe_c[y],1))
# TTM to 2026-05-31
ttm=dict(OCF=132.910-68.874+30.626,CAPEX=42.496-28.251+35.514,SBC=8.059-5.971+4.890,DA=20.896-15.707+17.047)
print('TTM',{k:round(v,1) for k,v in ttm.items()},'OE capex end',round(ttm['OCF']-ttm['SBC']-ttm['CAPEX'],1),'OE D&A end (amort 2.2 assumed as FY2025)',round(ttm['OCF']-ttm['SBC']-(ttm['DA']-2.2),1))
print()
print('window  capex_end  DA_end  yield_c  yield_d  acq_incl')
rows=[]
for n in range(3,17):
    ys=Y[-n:]
    c=sum(oe_c[y] for y in ys)/n; d=sum(oe_d[y] for y in ys)/n; a=c-sum(ACQ[y] for y in ys)/n
    rows.append((n,c,d)); print(f'{n}y {ys[0]}-{ys[-1]}  {c:.1f}  {d:.1f}  {c/CAP*100:.2f}%  {d/CAP*100:.2f}%  {a:.1f}')
lo=min(min(r[1],r[2]) for r in rows); hi=max(max(r[1],r[2]) for r in rows)
print('range all windows both ends',round(lo,1),round(hi,1),f'{lo/CAP*100:.2f}% {hi/CAP*100:.2f}%')
tot=sum(oe_c.values()); print('16y capex-end total',round(tot,1),'share of 2023+2025',round((oe_c[2023]+oe_c[2025])/tot*100,1),'share 2014+2023',round((oe_c[2014]+oe_c[2023])/tot*100,1))
for drop in [(2023,2025),(2023,2024,2025)]:
    ys=[y for y in Y if y not in drop]; print('16y without',drop, round(sum(oe_c[y] for y in ys)/len(ys),1))
ys=range(2015,2022); print('lean 2015-2021', round(sum(oe_c[y] for y in ys)/7,1), round(sum(oe_d[y] for y in ys)/7,1))
print('SBC/OCF 16y',round(sum(SBC.values())/sum(OCF.values())*100,1))
print('capex/DA-amort ratio by year',{y:round(CAPEX[y]/(DA[y]-AMORT[y]),2) for y in Y})
