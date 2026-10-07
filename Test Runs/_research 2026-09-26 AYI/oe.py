import json
# FY: (OCF as filed latest vintage, excess tax benefit line (negative in OCF, pre-FY2016 basis), SBC per note, capex gross, PP&E sale proceeds, D&A, acquired-intangible amortisation)
D={2006:(124.512,-17.282,11.4,23.443,4.717,30.688,3.2),
 2007:(208.705,-15.360,11.1,31.457,1.618,31.348,3.2),
 2008:(221.8,-5.0,12.0,27.2,0.2,33.8,3.7),
 2009:(92.7,-0.4,13.6,21.2,0.2,35.7,5.4),
 2010:(160.5,-2.8,12.5,21.9,0.2,36.5,7.1),
 2011:(161.1,-5.3,14.2,23.3,1.2,40.1,10.2),
 2012:(172.2,-4.9,15.9,31.4,0.1,39.8,11.2),
 2013:(132.3,-8.6,16.5,40.6,7.6,40.8,10.9),
 2014:(233.1,-10.4,17.7,35.3,1.0,43.4,11.2),
 2015:(288.9,-17.6,18.2,56.5,1.3,45.8,11.0),
 2016:(387.9,0,27.7,83.7,2.2,62.6,21.4),
 2017:(336.6,0,32.0,67.3,5.5,74.6,28.0),
 2018:(351.5,0,32.3,43.6,0.0,80.3,28.5),
 2019:(494.7,0,29.2,53.0,0.0,88.3,30.8),
 2020:(504.8,0,38.2,54.9,0.2,101.1,41.7),
 2021:(408.7,0,32.5,43.8,4.7,100.1,40.7),
 2022:(316.3,0,37.4,56.5,8.9,94.8,41.0),
 2023:(578.1,0,42.0,66.7,0.0,93.2,42.1),
 2024:(619.2,0,46.6,64.0,0.0,91.1,39.7),
 2025:(601.4,0,45.1,68.4,0.0,133.1,76.5)}
CAP=319.42*29935547/1e6
rows={}
print('FY   OCFadj   SBC  capex  D&A-amort  OE_capex  OE_DA  OE_DA_amortIn')
for y,(ocf,etb,sbc,cx,px,da,am) in sorted(D.items()):
    o=ocf-etb  # add back the excess tax benefit subtracted on the old basis
    dep=da-am
    rows[y]=dict(ocf=o,sbc=sbc,capex=cx,dep=dep,da=da,oe_cx=o-sbc-cx,oe_da=o-sbc-dep,oe_da_in=o-sbc-da)
    r=rows[y]; print(y,f"{o:7.1f} {sbc:5.1f} {cx:6.1f} {dep:8.1f} {r['oe_cx']:8.1f} {r['oe_da']:7.1f} {r['oe_da_in']:7.1f}")
ttm=dict(ocf=601.4+520.2-398.9,sbc=45.1+39.2-34.0,capex=68.4+58.5-43.6,da=133.1+117.8-86.7,am=76.5+70.4-45.5)
ttm['oe_cx']=ttm['ocf']-ttm['sbc']-ttm['capex']; ttm['oe_da']=ttm['ocf']-ttm['sbc']-(ttm['da']-ttm['am'])
print('TTM',{k:round(v,1) for k,v in ttm.items()})
print(f'cap {CAP:.1f}')
print('window      capex_end   DA_end   y_cx   y_da  capex/dep  DA_end_amortIn')
W={}
lo,hi=1e9,-1e9
for n in range(3,21):
    ys=list(range(2026-n,2026))
    m=lambda k: sum(rows[y][k] for y in ys)/n
    a,b=m('oe_cx'),m('oe_da'); c=m('oe_da_in')
    ratio=sum(rows[y]['capex'] for y in ys)/sum(rows[y]['dep'] for y in ys)
    W[n]=(a,b,c,ratio); lo=min(lo,a,b); hi=max(hi,a,b)
    print(f'{n:2}y FY{ys[0]}-25  {a:8.1f} {b:8.1f} {a/CAP*100:6.2f} {b/CAP*100:6.2f} {ratio:6.2f} {c:8.1f}')
print(f'range {lo:.1f} to {hi:.1f}  yields {lo/CAP*100:.2f}% to {hi/CAP*100:.2f}%')
# screen reproduction: 3y and 5y, capex end and D&A end with amort in, using as-filed OCF and tag SBC
json.dump(dict(rows=rows,ttm=ttm,windows=W,cap=CAP),open('oe_series.json','w'),indent=1)
