# owner earnings from filed cash-flow statements; (c) both ends; no net-income proxy
Y=['FY2008','FY2009','FY2010','FY2011','FY2012','FY2013','FY2014','FY2015','FY2016','FY2017','FY2018','FY2019','FY2020','FY2021','2022','2023','2024','2025']
#        OCF    SBC  capex rental rsale  D&A  amort finlease adv   dcc
D={'FY2008':(390.4,15.0,75.8,42.5,13.0,152.9,68.7,0,-41.3,0),
'FY2009':(898.9,10.9,46.2,15.4,6.1,152.0,62.3,0,435.6,0),
'FY2010':(619.7,14.7,83.2,6.3,10.3,172.9,60.5,0,-356.4,0),
'FY2011':(387.7,15.5,82.3,3.9,20.2,144.4,59.3,0,95.4,0),
'FY2012':(268.3,18.5,55.9,8.4,3.7,130.9,57.7,0,44.2,0),
'FY2013':(438.0,24.4,46.0,13.9,7.5,126.8,56.6,0,-216.0,0),
'FY2014':(170.4,25.0,92.2,32.7,12.8,126.8,55.3,0,15.8,0),
'FY2015':(82.5,21.4,131.7,26.3,26.8,124.5,53.2,0,130.1,0),
'FY2016':(577.7,18.7,92.5,34.8,40.2,128.8,52.5,0,31.6,0),
'FY2017':(246.5,22.4,85.8,27.4,49.5,130.3,45.8,0,41.5,0),
'FY2018':(436.3,26.7,95.3,4.8,5.8,120.5,38.3,0,-68.4,0),
'FY2019':(568.3,29.0,147.6,26.6,12.0,115.2,36.9,0,-90.2,0),
'FY2020':(327.3,29.3,112.3,17.9,38.8,104.2,11.0,0,112.3,0),
'FY2021':(1221.6,27.2,104.4,10.4,16.3,104.0,9.6,5.5,162.6,0),
'2022':(601.3,28.6,269.5,10.2,13.0,107.6,11.6,10.3,819.3,-342.6),
'2023':(599.6,31.9,325.3,4.6,0.0,159.9,41.7,14.6,157.0,-294.8),
'2024':(550.1,38.1,281.0,7.3,0.0,200.1,64.9,20.8,-94.1,-131.9),
'2025':(783.4,38.0,165.4,46.4,0.0,224.1,59.7,40.3,155.9,17.1)}
TQ=(-163.1,4.2,39.4,3.8,14.9,27.0,None,2.1,124.9,None)
cap=8195.96
rows={}
out=open('oe_out.txt','w',encoding='utf-8')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
P('year | OCF | SBC | capex+rental-rsale | dep(D&A-amort) | finlease | OE capex end | OE D&A end | adv | dcc | OE capex end ex adv/dcc | capex/dep')
for y in Y:
    ocf,sbc,cx,rn,rs,da,am,fl,adv,dcc=D[y]
    c=cx+rn-rs; dep=da-am
    a=ocf-sbc-c-fl; b=ocf-sbc-dep-fl
    x=a-adv-dcc
    rows[y]=(a,b,x,c,dep)
    P(y,'|',ocf,'|',sbc,'|',round(c,1),'|',round(dep,1),'|',fl,'|',round(a,1),'|',round(b,1),'|',adv,'|',dcc,'|',round(x,1),'|',round(c/dep,2))
P('')
P('window | capex end | D&A end | yld capex | yld D&A | capex/dep | capex end ex advances and deferred contract costs')
for n in range(3,19):
    w=Y[-n:]
    a=sum(rows[y][0] for y in w)/n; b=sum(rows[y][1] for y in w)/n; x=sum(rows[y][2] for y in w)/n
    r=sum(rows[y][3] for y in w)/sum(rows[y][4] for y in w)
    P(f'{n}y {w[0]}-{w[-1]} | {a:.1f} | {b:.1f} | {a/cap*100:.2f}% | {b/cap*100:.2f}% | {r:.2f} | {x:.1f}')
# CY2021 composite sensitivity: FY2021 - Q1FY21 (Oct-Dec 2020) + TQ
ocf=1221.6-368.1-163.1; sbc=27.2-6.6+4.2; cx=104.4-21.6+39.4; rn=10.4-1.9+3.8; rs=16.3-2.7+14.9; da=104.0-26.6+27.0
P('')
P(f'CY2021 composite (FY2021 - Oct-Dec 2020 + transition quarter): OCF {ocf:.1f} SBC {sbc:.1f} net capex {cx+rn-rs:.1f} D&A {da:.1f} -> OE capex end (no finlease) {ocf-sbc-(cx+rn-rs):.1f}')
tq=TQ; P(f'Transition quarter Oct-Dec 2021: OCF {tq[0]} SBC {tq[1]} net capex {tq[2]+tq[3]-tq[4]:.1f} D&A {tq[5]} finlease {tq[7]} -> OE capex end {tq[0]-tq[1]-(tq[2]+tq[3]-tq[4])-tq[7]:.1f}; customer advances +{tq[8]}')
# TTM to 2026-06-30
ocf=783.4+213.3-(-305.7); sbc=38.0+21.4-19.1; cx=165.4+54.8-80.9; rn=46.4+11.2-18.1; rs=0+22.9-1.7; da=224.1+122.8-109.5
P(f'TTM to 2026-06-30: OCF {ocf:.1f} SBC {sbc:.1f} net capex {cx+rn-rs:.1f} D&A {da:.1f} -> OE capex end (finlease 2025 {40.3} as proxy) {ocf-sbc-(cx+rn-rs)-40.3:.1f}; D&A end (amort 2025 59.7 as proxy) {ocf-sbc-(da-59.7)-40.3:.1f}')
