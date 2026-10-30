# all $M, from the filed cash-flow statements (FY2016, FY2019, FY2021, FY2023, FY2025 10-Ks; 10-Q Q2 2026)
Y=list(range(2014,2026))
ocf=[198.288,141.047,384.857,196.5,270.0,370.9,805.4,1259.6,585.9,190.2,586.3,694.5]
sbc=[16.012,18.851,21.073,18.9,18.7,18.8,32.3,28.3,27.0,20.1,25.2,29.0]
capex=[150.392,120.252,156.521,215.8,141.0,191.8,103.2,143.6,155.5,185.4,245.1,270.0]
da=[42.344,47.239,51.234,57.9,67.1,71.6,75.8,78.9,89.3,92.0,113.1,121.1]
fp=[7832.014-7802.719,7557.237-7504.516,6597.406-6676.161,7019.1-6957.9,6954.3-6870.1,7304.6-7423.2,9998.1-10374.0,8333.2-8801.8,10236.1-9766.5,11366.2-10940.4,12593.0-12490.9,15893.7-16081.4]
acq=[336.551,212.252,57.327,109.1,135.3,143.2,1.3,1099.6,528.7,366.1,1276.8,546.8]
disp=[144.597,41.581,36.843,10.7,107.9,43.4,29.8,24.8,141.4,193.8,229.7,145.5]
bb=[36.802,97.473,127.606,40.1,183.9,1.4,80.2,210.6,521.2,172.8,161.6,554.8]
div=[17.097,19.942,19.987,20.5,20.9,20.3,11.0,23.9,23.7,25.2,25.2,25.6]
rows=[]
print('year ocf fp ocf_adj  oe_capex oe_da  oeadj_capex oeadj_da  capex/da')
for i,y in enumerate(Y):
    a=ocf[i]+fp[i]
    r=(y,ocf[i],fp[i],a,ocf[i]-sbc[i]-capex[i],ocf[i]-sbc[i]-da[i],a-sbc[i]-capex[i],a-sbc[i]-da[i],capex[i]/da[i])
    rows.append(r); print(' '.join(f'{v:.1f}' if isinstance(v,float) else str(v) for v in r))
def mean(k,lo,hi): 
    v=[r[k] for r in rows if lo<=r[0]<=hi]; return sum(v)/len(v)
for lo,hi in [(2014,2025),(2021,2025),(2016,2020),(2014,2019),(2019,2025)]:
    print(lo,hi,'GAAP capex-end %.0f D&A-end %.0f | fp-neutral capex-end %.0f D&A-end %.0f | acq %.0f disp %.0f'%(mean(4,lo,hi),mean(5,lo,hi),mean(6,lo,hi),mean(7,lo,hi),sum(acq[Y.index(lo):Y.index(hi)+1])/(hi-lo+1),sum(disp[Y.index(lo):Y.index(hi)+1])/(hi-lo+1)))
print('sum fp 12y',sum(fp),'5y',sum(fp[7:]))
print('sum acq 12y',sum(acq),'disp',sum(disp),'bb',sum(bb),'div',sum(div),'ocf',sum(ocf),'capex',sum(capex))
print('5y acq',sum(acq[7:]),'disp',sum(disp[7:]),'bb',sum(bb[7:]),'ocf',sum(ocf[7:]),'capex',sum(capex[7:]))
# TTM to 2026-06-30
t_ocf=694.5-410.3+155.0; t_cap=270.0-123.9+126.8; t_sbc=29.0-15.8+18.8; t_da=121.1-58.0+62.1; t_fp=-187.7-(7050.3-7134.4)+(8675.7-8352.4)
print('TTM ocf',t_ocf,'capex',t_cap,'sbc',t_sbc,'da',t_da,'fp',t_fp,'OE capex',t_ocf-t_sbc-t_cap,'D&A',t_ocf-t_sbc-t_da,'fpadj capex',t_ocf+t_fp-t_sbc-t_cap,'D&A',t_ocf+t_fp-t_sbc-t_da)
