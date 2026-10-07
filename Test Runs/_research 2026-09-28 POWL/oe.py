# Owner earnings [E2-23]: OCF - SBC - (c). No net-income proxy. $M. FY to Oct 31 until FY2005; FY2006 = 11 months to Sep 30; FY to Sep 30 after.
Y=list(range(2001,2026))
OCF=[-2.057,31.666,36.705,24.908,-21.189,-4.655,12.160,-5.188]+[126.98,64.13,15.49,-5.96,91.42,9.13,12.92,74.91,36.81,-28.54,68.76,72.39,-30.46,-3.58,182.55,108.66,167.94]
SBC=[0.0,0.0,0.119,0.064,0.159,2.229,0.947,2.167]+[2.26,1.93,0.10,1.72,4.46,3.38,3.17,4.88,2.72,3.15,3.84,3.47,2.58,4.09,4.60,4.75,4.63]
CAPEX=[10.291,13.872,4.541,6.472,6.108,8.435,14.338,3.428]+[8.08,4.42,7.35,29.06,74.37,16.50,34.72,3.04,3.62,4.42,4.25,5.16,2.93,2.45,7.82,11.98,13.15]
DEP=[4.381,4.898,5.155,4.469,4.623,5.188,7.688,8.133]+[7.49,9.15,10.60,10.46,8.52,11.39,13.12,12.98,12.40,12.70,11.90,10.40,10.20,9.36,8.60,6.90,7.20]
# operating working-capital block as filed (sum of the lines under 'changes in operating assets and liabilities'), FY2009-FY2025, from wc_out.txt
WC={2009:74.3,2010:15.8,2011:-2.7,2012:-49.1,2013:42.4,2014:-22.7,2015:-24.2,2016:38.0,2017:30.6,2018:-34.6,2019:41.9,2020:40.5,2021:-43.1,2022:-24.1,2023:122.7,2024:-45.3,2025:-19.6}
CL={2023:227.6,2024:-34.7,2025:-23.5}  # contract assets and liabilities, net (cash-flow face)
REV={2001:271.2,2002:306.4,2003:253.4,2004:206.1,2005:256.6,2006:374.5,2007:564.3,2008:638.7,2009:665.9,2010:550.7,2011:562.4,2012:690.7,2013:640.9,2014:647.8,2015:661.9,2016:565.2,2017:395.9,2018:448.7,2019:517.2,2020:518.5,2021:470.6,2022:532.6,2023:699.3,2024:1012.4,2025:1104.3}
SH=[11.0]*0
PRICE=187.23; SHARES=36.432564; CAP=PRICE*SHARES
cx=[o-s-c for o,s,c in zip(OCF,SBC,CAPEX)]
dp=[o-s-d for o,s,d in zip(OCF,SBC,DEP)]
print('cap $M', round(CAP,1))
print('FY    OCF    SBC  capex   dep |  OE capex end | OE dep end | WC block | SBC/OCF | capex/dep')
for i,y in enumerate(Y):
    print(y, f'{OCF[i]:7.1f} {SBC[i]:5.2f} {CAPEX[i]:6.1f} {DEP[i]:5.1f} | {cx[i]:8.1f} | {dp[i]:8.1f} | {WC.get(y,""):>6} | {"" if OCF[i]<=0 else round(SBC[i]/OCF[i]*100,1)} | {round(CAPEX[i]/DEP[i],2)}')
print('\nTRAILING windows ending FY2025 (capex end / dep end), yield on cap')
for n in range(1,len(Y)+1):
    a=sum(cx[-n:])/n; b=sum(dp[-n:])/n
    print(f'{n:2d}y FY{Y[-n]}-25  {a:7.1f} {b:7.1f}   {a/CAP*100:5.2f}% {b/CAP*100:5.2f}%')
print('\nROLLING 5y windows (capex end / dep end)')
for i in range(0,len(Y)-4):
    print(f'FY{Y[i]}-{Y[i+4]}  {sum(cx[i:i+5])/5:7.1f} {sum(dp[i:i+5])/5:7.1f}')
lo=min(sum(cx[i:i+n])/n for n in range(3,len(Y)+1) for i in range(0,len(Y)-n+1))
hi=max(sum(dp[i:i+n])/n for n in range(3,len(Y)+1) for i in range(0,len(Y)-n+1))
print('\nevery window of 3+ years: low (capex end)', round(lo,1), ' high (dep end)', round(hi,1))
s5c=sum(cx[-5:]); s5d=sum(dp[-5:])
print('share of 5y sum by year FY2021-25, capex end:', [round(v/s5c*100,1) for v in cx[-5:]], ' dep end:', [round(v/s5d*100,1) for v in dp[-5:]])
print('FY2023+FY2025 share of 5y sum, capex end:', round((cx[-3]+cx[-1])/s5c*100,1), ' FY2023+FY2024:', round((cx[-3]+cx[-2])/s5c*100,1))
# WC stripped for FY2009-2025
st={y:cx[Y.index(y)]-WC[y] for y in WC}
for n in (3,5,10,17):
    ys=list(range(2025-n+1,2026)); print(f'{n}y WC-stripped capex end {sum(st[y] for y in ys)/n:.1f}')
print('sum WC FY2021-25', round(sum(WC[y] for y in range(2021,2026)),1), ' FY2009-25', round(sum(WC.values()),1))
# mean |OCF| check for the screen wc_note
for a,b in ((2017,2025),(2016,2025),(2014,2022),(2013,2022),(2009,2025)):
    v=[abs(OCF[Y.index(y)]) for y in range(a,b+1)]; print('mean |OCF|',a,b, round(sum(v)/len(v),1))
# TTM to 2026-06-30: FY2025 + 9M FY2026 - 9M FY2025
ttm_ocf=167.94+195.038-106.862; ttm_sbc=4.63+4.280-3.675; ttm_cx=13.15+10.386-11.380; ttm_dep=7.2+6.496-5.215
print('\nTTM June 2026: OCF',round(ttm_ocf,1),'SBC',round(ttm_sbc,1),'capex',round(ttm_cx,1),'D&A',round(ttm_dep,1),'OE capex end',round(ttm_ocf-ttm_sbc-ttm_cx,1),'dep end',round(ttm_ocf-ttm_sbc-ttm_dep,1))
# owner earnings as % of revenue, 5y
print('OE capex end / revenue by year:', {y:round(cx[i]/REV[y]*100,1) for i,y in enumerate(Y)})
