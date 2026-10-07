# Filed cash-flow statements: FY2014 10-K (2012-14), FY2017 (2015-17), FY2020 (2018-20), FY2023 (2021-22), FY2025 (2023-25).
Y=list(range(2012,2026))
OCF=[94.0,195.7,165.7,245.3,157.8,224.9,305.0,248.8,429.8,984.1,1271.9,510.5,767.8,547.1]
SBC=[4.0,5.9,8.7,12.2,11.2,11.1,12.1,11.3,18.8,19.3,18.3,23.8,26.5,22.7]
DA =[72.5,69.7,69.7,83.4,97.1,101.2,94.4,100.4,114.9,135.9,141.3,142.2,153.1,166.9]
CAP=[38.1,35.2,27.9,67.8,179.4,307.0,401.2,310.3,192.3,325.3,209.3,248.4,310.1,393.4]
R=dict(zip(Y,zip(OCF,SBC,DA,CAP)))
print('year   OCF   SBC    D&A  capex   OE(D&A end)  OE(capex end)')
for y in Y:
    o,s,d,c=R[y]; print(y,f'{o:7.1f}{s:6.1f}{d:7.1f}{c:7.1f}   {o-s-d:9.1f}   {o-s-c:9.1f}')
def win(ys):
    n=len(ys); hi=sum(R[y][0]-R[y][1]-R[y][2] for y in ys)/n; lo=sum(R[y][0]-R[y][1]-R[y][3] for y in ys)/n
    return lo,hi
cap=6718.1
print('\nwindows ending 2025 (mean OE, capex end .. D&A end; yield on cap $6,718.1M)')
for n in range(3,15):
    ys=Y[-n:]; lo,hi=win(ys); print(f'{n:2d}y {ys[0]}-2025: {lo:7.1f} .. {hi:7.1f}   {lo/cap*100:5.2f}% .. {hi/cap*100:5.2f}%')
print('\nother windows')
for name,ys in [('pre-boom 2012-2019',list(range(2012,2020))),('2016-2019 renewal',list(range(2016,2020))),('14y without 2021-2022',[y for y in Y if y not in(2021,2022)]),('3y 2023-25 less the 118.6 refund',None),('5y 2021-25',list(range(2021,2026))),('10y without 2021-22',[y for y in range(2016,2026) if y not in (2021,2022)])]:
    if ys is None:
        lo,hi=win([2023,2024,2025]); lo-=118.6/3; hi-=118.6/3
    else: lo,hi=win(ys)
    print(f'{name}: {lo:7.1f} .. {hi:7.1f}   {lo/cap*100:5.2f}% .. {hi/cap*100:5.2f}%')
tot_ocf=sum(OCF); tot_sbc=sum(SBC)
print('\nSBC / OCF 2012-2025', round(tot_sbc/tot_ocf*100,1),'%')
print('share of 14y OCF-SBC-capex from 2021-22:', round(sum(R[y][0]-R[y][1]-R[y][3] for y in (2021,2022))/sum(R[y][0]-R[y][1]-R[y][3] for y in Y)*100,1),'%')
