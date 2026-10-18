# Owner cash for CLNE from the filed cash-flow statements (USD millions). Sources:
# FY2025 10-K 0001104659-26-019215 (2023-2025); FY2023 10-K 0001558370-24-002174 (2021-2023);
# FY2020 10-K 0001558370-21-002638 (2018-2020). Arithmetic only.
Y=[2018,2019,2020,2021,2022,2023,2024,2025]
OCF=[38.0,12.3,61.0,41.3,66.7,43.8,64.6,85.5]
SBC=[5.3,3.9,3.0,15.0,26.5,23.3,10.8,8.9]
AMZ=[0,0,0,83.6,24.3,60.6,60.8,66.1]          # stock-based sales incentive (Amazon warrant) added back in OCF
CAPEX=[25.3,27.1,13.3,23.1,44.5,100.9,65.0,25.7]
ADG=[0,0,0,5.8,9.0,20.3,15.0,34.2]             # equipment and manure rights for ADG RNG projects
JV=[0,0,0.65,78.9,89.7,73.5,32.9,16.5]         # investments in other entities
OTH=[1.9,16.0,10.6,0.3,3.1,4.7,-1.2,8.0]       # other investing, net (loans, grants, JD proceeds, disposals, asset sales)
DA=[51.9,49.6,47.7,45.2,54.7,45.7,44.7,44.2]   # 2025 excludes 54.4 Pilot accelerated depreciation and ARO (10-K MD&A)
INTP=[16.8,6.8,5.6,3.9,1.9,16.4,27.4,15.0]     # cash interest paid
INTI=[2.9,2.4,1.3,1.1,3.4,11.1,14.0,11.4]      # interest income
PIK=[0,0,0,0,0,0,0,15.0]                       # paid-in-kind interest, non-cash inside OCF
AFTC=[26.7,47.1,19.8,20.7,21.8,20.9,23.8,0.2]  # expired 2024-12-31 (10-K)
REV=[346.4,344.1,291.7,255.6,420.2,425.2,415.9,424.8]
rows={}
for i,y in enumerate(Y):
    eq_m = OCF[i]-SBC[i]-DA[i]-PIK[i]                  # equity-only, maintenance proxy = D&A
    ae_m = OCF[i]-SBC[i]-DA[i]+INTP[i]-INTI[i]         # all-equity (before net interest), maintenance proxy
    spend = CAPEX[i]+ADG[i]+JV[i]-OTH[i]
    eq_a = OCF[i]-SBC[i]-spend-PIK[i]
    ae_a = OCF[i]-SBC[i]-spend+INTP[i]-INTI[i]
    rows[y]=dict(eq_m=eq_m,ae_m=ae_m,eq_a=eq_a,ae_a=ae_a,
                 eq_m_amz=eq_m-AMZ[i],ae_m_amz=ae_m-AMZ[i],eq_a_amz=eq_a-AMZ[i],ae_a_amz=ae_a-AMZ[i],
                 ae_m_xa=ae_m-AFTC[i],eq_m_xa=eq_m-AFTC[i],spend=spend)
keys=['ae_m','eq_m','ae_m_xa','eq_m_xa','ae_a','eq_a','ae_m_amz','eq_m_amz','ae_a_amz','eq_a_amz','spend']
print('year  '+' '.join('%9s'%k for k in keys))
for y in Y: print(y,' '.join('%9.1f'%rows[y][k] for k in keys))
W=[2021,2022,2023,2024,2025]
avg={k:sum(rows[y][k] for y in W)/5 for k in keys}
print('avg21-25',' '.join('%9.1f'%avg[k] for k in keys))
W8=Y
print('avg18-25',' '.join('%9.1f'%(sum(rows[y][k] for y in W8)/8) for k in keys))
r=0.0543; floor=0.10
price=1.50; sh=220.445015
debt=250.0+0.158+1.192+1.849   # Stonepeak principal + other debt + finance leases, 2026-06-30 10-Q
cash=59.153+80.997             # cash (incl. restricted) + short-term investments, 2026-06-30
nd=debt-cash
mcap=price*sh; ev=mcap+nd
print('net debt %.1f  mcap %.1f  EV %.1f'%(nd,mcap,ev))
for k in ['ae_m','ae_m_xa','ae_a','ae_m_amz']:
    v=avg[k]/r; vf=avg[k]/floor
    print('%-9s value@sov %.1f per share %.2f | fair(10%%) %.1f per share %.2f | yield on EV %.2f%%'%(k,v,(v-nd)/sh,vf,(vf-nd)/sh,100*avg[k]/ev))
for k in ['eq_m','eq_m_xa','eq_a','eq_m_amz']:
    v=avg[k]/r; vf=avg[k]/floor
    print('%-9s value@sov %.1f per share %.2f | fair(10%%) %.1f per share %.2f | yield on mcap %.2f%%'%(k,v,v/sh,vf,vf/sh,100*avg[k]/mcap))
best=max(rows[y]['ae_m'] for y in Y)
print('best single year all-equity maintenance-only: %.1f -> %.2f%% of EV; needed for floor %.1f'%(best,100*best/ev,floor*ev))
import math
print('revenue CAGR 2018-2025 %.2f%%  2021-2025 %.2f%%'%(100*((REV[-1]/REV[0])**(1/7)-1),100*((REV[-1]/REV[3])**(1/4)-1)))
