# Q7 computation for the ELPC run, 2026-10-18. R$ millions. Figures from the filed cash-flow statements
# (continuing operations): FY2021-2022 from 20-F FY2023 (0001292814-24-001329), FY2023-2025 from 20-F FY2025
# (0002070979-26-000155); FY2024 grant bonus from 20-F FY2024 (0001628280-25-018102).
Y=[2021,2022,2023,2024,2025]
ocf   =[2858.937,3724.822,3393.002,3389.916,3028.446]   # net cash from operating activities, continuing (after interest and tax paid)
crc   =[1646.614,0,0,0,0]                               # CRC transferred to the State of Parana (one-off inside 2021 OCF)
ca    =[1468.516,1909.603,1973.215,2174.902,2903.661]   # additions to contract assets
ppe   =[338.129,381.938,204.805,137.635,162.100]
intg  =[4.546,8.319,13.388,4098.286,43.788]             # additions to intangibles (2024 includes grant bonus 4,073.915)
bonus =[0,0,0,4073.915,0]
lease =[48.785,57.212,69.293,70.949,69.583]             # principal of lease liabilities
da    =[1017.293,1233.097,1382.040,1465.478,1481.886]   # depreciation and amortization
intpd =[193.421+343.524+5.135, 337.455+890.123+19.531, 521.134+1127.607+24.284, 471.276+1089.013+33.292, 425.192+1549.452+32.013]
# deals, continuing investing: acquisitions (-), disposals (+), additions in investments (-), capital reductions (+), PP&E disposals (+)
deals =[-501.886-30.970, -18.031-4.829+61.536, -911.450+58.132-10.780, 47.066+37.129+11.440, -190.433+2536.421-1060.804+0.294]
rev   =[20976.216,20535.341,21479.468,22651.036,26116.856]
debt_iss=[3000+134.313,1500+1891.954,2900+45.325,3920+5.051,5000]
debt_rep=[202.577+1831.809,1000.319+2051.481,260.971+1193.910,261.753+1079.912,1254.405+3317.499]
BONUS_YR=4073.915/30   # CONVENTION of this run: the bonus spread over the 30-year term
T=0.34
shares=2970.070324; price=17.70; netdebt=19651.2   # net debt 2026-06-30, 2Q26 release
rf=0.1287; floor=0.10
def avg(x): return sum(x)/len(x)
oc_ocf=[o-c for o,c in zip(ocf,crc)]
capex=[c+p+(i-b) for c,p,i,b in zip(ca,ppe,intg,bonus)]
allsp=[o-cx-l-BONUS_YR for o,cx,l in zip(oc_ocf,capex,lease)]
allsp_lit=[o-c-p-i-l for o,c,p,i,l in zip(oc_ocf,ca,ppe,intg,lease)]
maint=[o-d-l-(BONUS_YR if y<2025 else 0) for o,d,l,y in zip(oc_ocf,da,lease,Y)]   # D&A from 2025 already amortizes the bonus
ae_add=[x*(1-T) for x in intpd]
print('year  OCFadj  capex  allspend  allspend_literal  maint  interest  maint_AE  allsp_AE  share_of_sales(maint_AE)')
for k in range(5):
    print(Y[k], round(oc_ocf[k]), round(capex[k]), round(allsp[k]), round(allsp_lit[k]), round(maint[k]), round(intpd[k]), round(maint[k]+ae_add[k]), round(allsp[k]+ae_add[k]), f"{(maint[k]+ae_add[k])/rev[k]:.3f} {maint[k]/rev[k]:.3f}")
print('avg', round(avg(oc_ocf)), round(avg(capex)), round(avg(allsp)), round(avg(allsp_lit)), round(avg(maint)), round(avg(intpd)), round(avg(maint)+avg(ae_add)), round(avg(allsp)+avg(ae_add)))
print('deals by year', [round(d) for d in deals], 'avg', round(avg(deals)), 'net purchases > half of owner cash?')
netnew=[i-r for i,r in zip(debt_iss,debt_rep)]
print('net new debt', [round(x) for x in netnew], 'avg', round(avg(netnew)), 'capex avg', round(avg(capex)))
sg=(rev[-1]/rev[0])**(1/4)-1
print('sales growth 2021-2025 CAGR', round(sg,4))
def halves(s):
    a=(s[0]+s[1])/2; b=(s[3]+s[4])/2
    return (b/a)**(1/3)-1 if a>0 and b>0 else None
def pv(cf0,g,r,n=10):
    s=0; cf=cf0
    for t in range(1,n+1):
        cf*=1+g; s+=cf/(1+r)**t
    return s+cf/r/(1+r)**n
def case(name, series, base, adddebt):
    g=halves(series); gs=g
    cap=None
    if g is not None:
        maxshare=max(x/rv for x,rv in zip(series,rev))
        cf10=base*(1+g)**10; rev10=rev[-1]*(1+sg)**10
        if cf10/rev10>maxshare: g=sg; cap=f'cut: {cf10/rev10:.3f} of sales in yr10 > max share {maxshare:.3f}'
        if g>rf: g=sg; cap=(cap or '')+' cut: above discount rate'
    lo_r=pv(base,0,rf) - adddebt; hi_r=pv(base,g,rf)-adddebt if g is not None else lo_r
    lo_f=pv(base,0,floor)-adddebt; hi_f=pv(base,g,floor)-adddebt if g is not None else lo_f
    fair=(lo_f+hi_f)/2/shares
    # expected return at price, high case: solve r
    def irr(gg):
        lo,hi=0.0005,1.0
        if pv(base,gg,lo)-adddebt<price*shares: return float('nan')
        for _ in range(200):
            m=(lo+hi)/2
            v=pv(base,gg,m)-adddebt
            if v>price*shares: lo=m
            else: hi=m
        return m
    print(f"{name}: base {base:,.0f}; growth shown {gs if gs is None else round(gs,4)} carried {None if g is None else round(g,4)} {cap or ''}")
    print(f"   range at {rf:.4f}: R$ {lo_r/shares:.2f} to R$ {hi_r/shares:.2f} a share (top/bottom {hi_r/lo_r if lo_r>0 else float('nan'):.2f}); at 10%: {lo_f/shares:.2f} to {hi_f/shares:.2f}; FAIR {fair:.2f}; per ADS {fair*4:.2f}")
    print(f"   expected return at R$ {price}: no-growth {irr(0):.4f}, growth {irr(g if g is not None else 0):.4f}")
    return fair
bm=avg(maint); ba=avg(allsp)
f_eq_m=case('EQUITY-ONLY maintenance-only (e)', maint, bm, 0)
f_eq_a=case('EQUITY-ONLY all spending', allsp, ba, 0)
f_ae_m=case('ALL-EQUITY maintenance-only', [m+a for m,a in zip(maint,ae_add)], bm+avg(ae_add), netdebt)
f_ae_a=case('ALL-EQUITY all spending', [m+a for m,a in zip(allsp,ae_add)], ba+avg(ae_add), netdebt)
# regulated-utility variant: credit net new LT debt against capex up to debt share of capital
debtshare=23484.2/(23484.2+23092)   # debt 2026-06-30 against equity 2025-12-31 (latest filed)
credit=[min(n, debtshare*c) if n>0 else 0 for n,c in zip(netnew,capex)]
reg=[a+c for a,c in zip(allsp,credit)]
print('debt share', round(debtshare,3), 'credit by year', [round(c) for c in credit], 'avg', round(avg(credit)))
f_reg=case('EQUITY-ONLY all spending + regulated debt credit', reg, avg(reg), 0)
# literal window (bonus charged in full)
f_lit=case('EQUITY-ONLY all spending, LITERAL (bonus in full)', allsp_lit, avg(allsp_lit), 0)

# beside: the 2022-2025 decline of maintenance-only owner cash, carried as the bottom by (b)
gd=(maint[4]/maint[1])**(1/3)-1
print('maint 2022->2025 rate', round(gd,4), 'equity-only bottom at rf', round(pv(bm,gd,rf)/shares,2), 'at 10%', round(pv(bm,gd,floor)/shares,2))
ae=[m+a for m,a in zip(maint,ae_add)]; gda=(ae[4]/ae[1])**(1/3)-1
print('AE maint 2022->2025 rate', round(gda,4), 'all-equity bottom at rf', round((pv(bm+avg(ae_add),gda,rf)-netdebt)/shares,2), 'at 10%', round((pv(bm+avg(ae_add),gda,floor)-netdebt)/shares,2))
print('market cap', round(price*shares), 'EV', round(price*shares+netdebt))
print('owner cash yields: eq maint', round(bm/(price*shares),4), 'eq allsp', round(ba/(price*shares),4), 'AE maint', round((bm+avg(ae_add))/(price*shares+netdebt),4))
