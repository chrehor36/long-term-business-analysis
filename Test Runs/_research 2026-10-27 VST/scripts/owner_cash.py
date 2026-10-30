# COMPUTATION from the filed cash-flow statements (10-K FY2020, FY2023, FY2025; accessions in the run file).
# USD millions. All items as filed; sign: + inflow.
Y=[2018,2019,2020,2021,2022,2023,2024,2025]
OCF   =[1471,2736,3337,-206, 485,5453,4563,4070]
SBC   =[  73,  47,  65,  47,  63,  77, 100, 113]
CAPEX =[ 530, 713,1259,1033,1301,1676,2078,2752]   # incl nuclear fuel, LTSA prepayments, growth
GROWTH_MDA=[None,None,None,440,475,698,800,None]   # MD&A "Growth and development expenditures"
MAINT_NEW=[None,None,None,None,None,1471,1727,2104] # FY2025 10-K Note 21, "including nuclear fuel and excluding growth expenditures"
ALLOW_NET=[-4,-125,-339,-213,-28,-571,-453,-914]   # sales less purchases of environmental allowances
NDT_NET =[-22,-22,-22,-22,-23,-23,-23,-24]
PPE_PROC=[7,6,24,30,78,115,196,119]
INS_PROC=[0,0,0,89,39,15,3,325]
ITC_PROC=[0,0,0,0,0,0,150,0]
OTHER_INV=[3,17,24,-4,-4,-5,-6,-10]
ACQ     =[-445,880,0,0,0,0,3065,1140]  # 2018 cash acquired in Dynegy merger (inflow, shown negative); Ambit+Crius 2019; Energy Harbor; Lotus
NCI_PAY =[0,0,0,0,0,0,1748+180,703]   # Vistra Vision noncontrolling interest purchase + NCI dividends
INT_PAID=[639,513,482,456,552,599,910,1040]  # net of capitalized interest
TAX_PAID=[67,-76,-140,None,None,31,55,97]
PRETAX  =[-101,1216,890,-1722,-1560,2000,3467,1123]
INTEXP  =[572,797,630,384,368,740,900,1179]
MTM_COM =[380,-696,-231,759,2510,-490,-1155,808]  # unrealized commodity MTM loss (+) / gain (-) in net income
PTC_REV =[0,0,0,0,0,0,545,220]  # transferable nuclear PTC revenue (45U, 2024-2032)
PREF_DIV=[0,0,0,0,151,150,173,192]
T=0.23  # CONVENTION of this run: 21% federal + about 2% state (filer's reconciliation shows 2.0%-3.6% state)
rows=[]
for i,y in enumerate(Y):
    pre_int_pre_tax = OCF[i] + INT_PAID[i] + (TAX_PAID[i] or 0)
    allspend = CAPEX[i] - ALLOW_NET[i] - NDT_NET[i] - PPE_PROC[i] - INS_PROC[i] - ITC_PROC[i] - OTHER_INV[i]
    ebitx = PRETAX[i] + INTEXP[i] + MTM_COM[i]
    tax = T*ebitx
    oc_ae_all = pre_int_pre_tax - SBC[i] - allspend - tax          # all spending charged, before interest, after statutory tax
    oc_ae_all_xptc = oc_ae_all - PTC_REV[i]*(1)                     # PTC removed from base (priced separately)
    oc_eq_all = oc_ae_all - INT_PAID[i]*(1-T) - PREF_DIV[i]
    rows.append((y,pre_int_pre_tax,allspend,ebitx,tax,oc_ae_all,oc_ae_all_xptc,oc_eq_all))
print(" year  preInt/preTax  allspend   EBITx    tax@23%   OC_ae_all  OC_ae_xPTC  OC_eq_all")
for r in rows: print(f" {r[0]}  {r[1]:9.0f}  {r[2]:9.0f}  {r[3]:7.0f}  {r[4]:8.0f}  {r[5]:9.0f}  {r[6]:9.0f}  {r[7]:9.0f}")
import statistics as st
def avg(a,b,k): return st.mean([r[k] for r in rows if a<=r[0]<=b])
for a,b in [(2021,2025),(2019,2025),(2018,2025),(2020,2024),(2023,2025)]:
    print(f" avg {a}-{b}: OC_ae_all {avg(a,b,5):7.0f}  OC_ae_xPTC {avg(a,b,6):7.0f}  OC_eq_all {avg(a,b,7):7.0f}")
print(" purchases 2021-2025 (acq + NCI):", sum(ACQ[3:])+sum(NCI_PAY[3:]))
