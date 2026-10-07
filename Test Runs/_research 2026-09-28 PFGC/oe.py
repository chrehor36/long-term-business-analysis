# Owner earnings [E2-23], OCF - SBC - (c). No net-income proxy. $M.
Y=list(range(2013,2027))
OCF=[140.7,119.7,127.4,228.5,201.7,367.0,317.4,623.6,64.6,276.5,832.1,1163.0,1210.1,1413.7]
SBC=[1.1,0.7,1.2,17.2,17.3,21.6,15.7,17.9,25.4,44.0,43.4,41.9,47.8,51.5]
CAPEX=[66.5,90.6,98.6,119.7,140.2,140.1,139.1,158.0,188.8,215.5,269.7,395.6,506.0,384.1]
FLA=[5.7,8.1,3.0,0.1,23.4,18.2,98.1,93.0,125.6,109.4,191.8,412.4,842.0,441.1]   # finance-lease (capital-lease) additions, non-cash
DEP=[58.7,73.5,76.3,80.5,91.5,100.3,116.2,178.5,213.9,279.7,315.7,355.2,455.3,541.9]
AMORT=[61.3,59.2,45.0,38.1,34.6,29.8,38.8,97.8,125.0,183.1,181.0,201.5,262.6,272.0]
SH=[86.9,86.9,86.9,96.4,100.2,102.0,103.8,113.0,132.1,149.8,154.2,154.4,154.8,155.9]  # basic weighted shares, M (companyfacts WeightedAverageNumberOfSharesOutstandingBasic; FY2013 from the IPO prospectus)
CAP=91.97*157.533032
cx=[o-s-(c+f) for o,s,c,f in zip(OCF,SBC,CAPEX,FLA)]
dp=[o-s-d for o,s,d in zip(OCF,SBC,DEP)]
dpa=[o-s-d-a for o,s,d,a in zip(OCF,SBC,DEP,AMORT)]
print('FY   OCF   SBC  capex  FLA  dep  amort | OE capex+FLA end | OE dep end | (run.py D&A incl amort) | SBC/OCF')
for i,y in enumerate(Y): print(y, OCF[i],SBC[i],CAPEX[i],FLA[i],DEP[i],AMORT[i],'|',round(cx[i],1),'|',round(dp[i],1),'|',round(dpa[i],1),'|',round(SBC[i]/OCF[i]*100,1))
print('\nTRAILING windows ending FY2026 (capex+FLA end / dep end), yield on cap',round(CAP,1))
for n in range(1,15):
    a=sum(cx[-n:])/n; b=sum(dp[-n:])/n
    print(f'{n:2d}y FY{Y[-n]}-26  {a:8.1f} {b:8.1f}   {a/CAP*100:5.2f}% {b/CAP*100:5.2f}%')
print('\nROLLING 5y windows (capex+FLA end / dep end)')
for i in range(0,len(Y)-4):
    print(f'FY{Y[i]}-{Y[i+4]}  {sum(cx[i:i+5])/5:8.1f} {sum(dp[i:i+5])/5:8.1f}')
print('\nper share (capex end / dep end), basic weighted')
for i,y in enumerate(Y): print(y, round(cx[i]/SH[i],2), round(dp[i]/SH[i],2))
s5c=sum(cx[-5:]); s5d=sum(dp[-5:])
print('\nshare of 5y sum by year, capex end:', [round(v/s5c*100,1) for v in cx[-5:]], ' dep end:', [round(v/s5d*100,1) for v in dp[-5:]])
print('SBC/OCF 5y', round(sum(SBC[-5:])/sum(OCF[-5:])*100,1))
# six working-capital lines as filed (AR, inventories, income-tax receivable, prepaid, payables and outstanding checks, accrued), $M, sign as in the statement
WC=[-0.9,-48.1,-63.3,-1.3,-52.0,-9.8,-47.5,208.9,-390.6,-488.1,-208.7,30.8,-20.7,-41.8]
st=[c-w for c,w in zip(cx,WC)]
print('\nWC lines by year:', dict(zip(Y,WC)))
print('capex end, WC stripped by year:', {y:round(v,1) for y,v in zip(Y,st)})
for n in (3,5,10,14): print(f'{n}y stripped {sum(st[-n:])/n:.1f}  dep-end stripped {sum([d-w for d,w in zip(dp,WC)][-n:])/n:.1f}')
print('sum WC FY2013-26', round(sum(WC),1), ' FY2022-26', round(sum(WC[-5:]),1))
