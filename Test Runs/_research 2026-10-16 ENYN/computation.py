# ENYN COMPUTATION, NOT A CLEARANCE. Figures in CDN$ from the FY2006 20-F (acc 0001049021-06-000046),
# Item 3.A selected data (Canadian GAAP, audited), and the Q2 FY2007 interim statements
# (6-K acc 0001049021-07-000009, unaudited, not reviewed).
yrs=[2002,2003,2004,2005,2006]
ocf=[-2020541,621878,-3052995,4625926,-789226]          # cash from operating activities (incl. discontinued M&M to FY2005)
capex=[2759206,354625,1740154,1001743,6535176]          # purchase of oil and gas properties for cash
cap_assets_2002=163000                                    # FY2002 20-F: purchase of capital assets $163K (000s table)
interest=[4925,5215,4812,2020,6968]
oc=[o-c for o,c in zip(ocf,capex)]; oc[0]-=cap_assets_2002
for y,v in zip(yrs,oc): print(y,'owner cash after all capital spending',v)
avg=sum(oc)/5; avg_pre_int=avg+sum(interest)/5
print('5y avg owner cash (equity-only)',round(avg)); print('5y avg before interest (all-equity)',round(avg_pre_int))
# operating cash proxy for continuing oil & gas alone, before capex: net revenue - operating - admin - interest (Item 3.A)
netrev=[448463,579749,659456,745483,980268]; opx=[260599,279189,292275,399795,394863]; adm=[1627838,2023237,1921385,2221343,2198024]
cont=[n-o-a-i for n,o,a,i in zip(netrev,opx,adm,interest)]
print('continuing O&G before depletion, capex and tax, by year',cont,'avg',round(sum(cont)/5))
r=0.0419; shares=4293000
# net debt at 2006-12-31 (borrowings less cash and securities) plus the stated subsequent event (SCC leave denied 2007-01-18)
borrow=225834+654105+15152+143151+71722
cash_sec=38160+784487
oakwell_net=7825946-1500000
nd_borrow=borrow-cash_sec; nd=nd_borrow+oakwell_net
print('borrowings',borrow,'cash+securities',cash_sec,'net borrowings',nd_borrow,'Oakwell claim less security posted',oakwell_net,'net debt incl judgment',nd)
# range: series changes sign (2003, 2005 positive); halves: first (2002-03) vs second (2005-06)
h1=(oc[0]+oc[1])/2; h2=(oc[3]+oc[4])/2; print('halves',round(h1),round(h2),'-> growth of a negative series is meaningless: no-growth case alone')
v_ae=avg_pre_int/r-nd; v_eq=avg/r
print('VALUE no-growth all-equity /sh',round(v_ae/shares,2),' equity-only /sh',round(v_eq/shares,2))
print('  all-equity excluding the judgment /sh',round((avg_pre_int/r-nd_borrow)/shares,2))
f_ae=avg_pre_int/0.10-nd; f_eq=avg/0.10
print('FAIR all-equity /sh',round(f_ae/shares,2),' equity-only /sh',round(f_eq/shares,2))
# continuing-ops variant (ex discontinued M&M cash), before any capex: still negative
c=sum(cont)/5; print('continuing-only variant, no capex charged, all-equity value /sh',round((c+sum(interest)/5)/r/shares - nd/shares,2))
