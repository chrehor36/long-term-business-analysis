# Q7 arithmetic for SR (USD millions). Every input is a filed figure; see the run file for accessions.
yrs=[2021,2022,2023,2024,2025]
ocf={2021:249.8,2022:55.0,2023:440.2,2024:912.4,2025:578.0}
sbc={2021:13.9,2022:6.4,2023:9.8,2024:5.8,2025:6.7}       # stock pay recognized in net income
da ={2021:213.1,2022:237.3,2023:254.8,2024:278.4,2025:298.2}
cap={2021:624.8,2022:552.2,2023:662.5,2024:861.3,2025:922.4}
acq={2021:0.0,2022:0.0,2023:37.0,2024:175.9,2025:0.0}
pref={y:14.8 for y in yrs}
dtax={2021:67.0,2022:57.9,2023:36.9,2024:57.0,2025:57.3}
wc={2021:-319.3,2022:-469.8,2023:-82.0,2024:317.8,2025:-62.3}   # sum of 'changes in assets and liabilities'
intr={2021:106.6,2022:119.8,2023:185.7,2024:201.1,2025:204.1}
tax={2021:68.5,2022:58.9,2023:38.8,2024:58.7,2025:59.7}
ni={2021:271.7,2022:220.8,2023:217.5,2024:250.9,2025:271.7}
avg=lambda d: sum(d[y] for y in yrs)/5
maint={y:ocf[y]-sbc[y]-pref[y]-da[y] for y in yrs}
allsp={y:ocf[y]-sbc[y]-pref[y]-cap[y]-acq[y] for y in yrs}
prewc={y:maint[y]-wc[y] for y in yrs}
print('owner cash after maintenance (equity-only, after pref):',{y:round(maint[y],1) for y in yrs},'avg',round(avg(maint),1))
print('owner cash after ALL spending:',{y:round(allsp[y],1) for y in yrs},'avg',round(avg(allsp),1))
print('before working capital (beside):',{y:round(prewc[y],1) for y in yrs},'avg',round(avg(prewc),1))
print('book-tax variant (deferred tax not added back): avg',round(avg(maint)-avg(dtax),1))
h1=(maint[2021]+maint[2022])/2; h2=(maint[2024]+maint[2025])/2
print('halves of window (maint):',round(h1,1),round(h2,1),'-> sign change, growth meaningless')
print('pre-WC end-year growth:', round(((prewc[2025]/prewc[2021])**0.25-1)*100,2),'%')
gs=avg(cap)-avg(da)+avg(acq); print('growth spending avg (capex-D&A + acquisitions):',round(gs,1))
ltd0=2423.7+60.4; ltd1=3369.4+487.5; credit=(ltd1-ltd0)/5
capsh=(5758.0+238.1)/(5758.0+238.1+3583.0)
print('LTD FY2020',ltd0,'FY2025',ltd1,'increase/yr',round(credit,1),'cap share',round(capsh*100,1),'% -> cap',round(capsh*gs,1))
cr=min(credit,capsh*gs)
# post-window adjustments (equity-only owner cash, after company tax)
t=sum(tax.values())/(sum(ni.values())+sum(tax.values())); print('five-year effective tax rate',round(t*100,1))
tn_pretax=121.605; deal_debt=2500.8-819.9-30.0; r=(900*0.0635+825*0.05)/1725
tn=tn_pretax*(1-t)-deal_debt*r*(1-t)
removed=185.9/5+23.1*12/9   # Marketing five-year GAAP net income average; Storage nine months to sale (10-Q) annualized
pref_eff=14.8-(200*0.06375)*(1-t)-(50*r)*(1-t)
adj=tn-removed+pref_eff
print('TN after tax',round(tn_pretax*(1-t),1),'deal debt',round(deal_debt,1),'rate',round(r*100,2),'TN net',round(tn,1),'removed',round(removed,1),'pref',round(pref_eff,1),'net adj',round(adj,1))
base_lit=avg(maint); base=base_lit+adj
S=59.112807; P=85.37; R=0.0531
mc=S*P; print('market cap',round(mc,1))
def pv_flat(c,r): return c/r
def pv_growth(c0,g,spend0,credit0,r):
    v=0
    for k in range(1,11):
        c=c0*(1+g)**k; s=(spend0-credit0)*(1+g)**k
        v+=(c-s)/(1+r)**k
    term=c0*(1+g)**10/r/(1+r)**10
    return v+term
for lab,b in (('central (adjusted for closed deals)',base),('literal window',base_lit)):
    ng=pv_flat(b,R); ng10=pv_flat(b,0.10)
    gc=pv_growth(b,0.0,gs,cr,R); gc10=pv_growth(b,0.0,gs,cr,0.10)
    print(f'{lab}: base {b:.1f}; no-growth at sovereign {ng:.0f} = ${ng/S:.2f}/sh; at 10% ${ng10/S:.2f}')
    print(f'   growth case beside (g=0 shown, growth spending net of debt credit charged ten years): at sovereign ${gc/S:.2f}; at 10% ${gc10/S:.2f}; average of ends at 10% ${(ng10+gc10)/2/S:.2f}')
    print(f'   yield at price on base: {b/mc*100:.2f}%')
# all-equity beside
ia=avg(intr)*(1-t)
unlev=base+ia+14.8*0  # pref treated as a claim below
debt_june=5758.0+238.1+1263.5; cash_june=None
print('after-tax interest avg',round(ia,1),'unlevered maintenance owner cash',round(base+ia,1))

# appended to q7.py: the variants shown beside the central figure
m2020=469.9-8.8-14.8-197.3   # FY2020: OCF, stock pay, preferred dividend, D&A (10-K FY2021/FY2022 cash-flow statements)
cyc=(m2020+sum(maint.values()))/6
print('FY2020 maint owner cash',round(m2020,1),'six-year cycle average',round(cyc,1),'-> no-growth $%.2f at sovereign, $%.2f at 10%%'%(cyc/R/S,cyc/0.10/S))
bt=avg(maint)-avg(dtax)+adj
print('book-tax variant central',round(bt,1),'-> $%.2f at sovereign, $%.2f at 10%%, yield %.2f%%'%(bt/R/S,bt/0.10/S,bt/mc*100))
pw=avg(prewc)+adj
print('pre-WC variant central',round(pw,1),'-> $%.2f at sovereign, yield %.2f%%'%(pw/R/S,pw/mc*100),' literal pre-WC yield %.2f%%'%(avg(prewc)/mc*100))
unlev=avg(maint)+ia+14.8+tn_pretax*(1-t)-removed
nd=5758.0+238.1+1263.5-20.7
print('all-equity: unlevered owner cash',round(unlev,1),'net debt 2026-06-30',round(nd,1),'-> at sovereign $%.2f, at 10%% $%.2f'%((unlev/R-nd)/S,(unlev/0.10-nd)/S))
