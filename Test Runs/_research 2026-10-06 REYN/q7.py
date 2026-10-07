# Q7 arithmetic for REYN run 2026-10-06. Convention of v5 Part VI: five-year mean owner cash, shown growth capped by Q3,
# ten years then zero nominal growth, discounted at the sovereign. Fair/cheap at the ~10% pre-tax floor (owner's request).
S=210.790982; P=22.23; r=0.0566
def pv(c,g,rate,yrs=10):
    v=0; x=c
    for t in range(1,yrs+1):
        x*= (1+g); v+= x/(1+rate)**t
    return v + (x/rate)/(1+rate)**yrs
oc={2020:171,2021:165,2022:86,2023:526,2024:350,2025:295}
ocd={2020:215,2021:197,2022:97,2023:506,2024:341,2025:321}
base=sum(oc[y] for y in range(2021,2026))/5; based=sum(ocd[y] for y in range(2021,2026))/5
wc_adj=279  # 2020 one-time rebuild of receivables sold to the parent SPE before the IPO (13 -> 292)
whole=(sum(oc.values())+wc_adj)/6; whole_raw=sum(oc.values())/6
print('base capex %.1f  D&A %.1f  whole-cycle adj %.1f raw %.1f'%(base,based,whole,whole_raw))
print('market cap %.0f'%(P*S))
for name,c in (('5yr capex',base),('5yr D&A',based),('whole-cycle',whole),('whole raw',whole_raw)):
    lo=pv(c,0,r); hi=pv(c,0.02,r)
    print('%-12s no-growth %6.0f ($%.2f)   2%%x10 %6.0f ($%.2f)  width %.2f'%(name,lo,lo/S,hi,hi/S,hi/lo))
taxes=(91+64+90+125+67)/5; interest=(41+68+114+98+82)/5; netdebt=1586-147
pre_eq=base+taxes; pre_ev=pre_eq+interest
print('cash tax %.1f cash interest %.1f  pretax owner cash to equity %.1f  pre-interest %.1f'%(taxes,interest,pre_eq,pre_ev))
print('pretax yield at price: equity %.2f%%  EV %.2f%% (EV %.0f)'%(100*pre_eq/(P*S),100*pre_ev/(P*S+netdebt),P*S+netdebt))
# expected pre-tax return at price: IRR of buying at P*S the pre-tax stream, growth g 10y then 0
def irr(price,c,g):
    lo,hi=0.0,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c,g,m)>price: lo=m
        else: hi=m
    return m
for g in (0,0.01,0.02):
    print('IRR pre-tax equity g=%d%%: %.2f%%   EV basis: %.2f%%'%(g*100,100*irr(P*S,pre_eq,g),100*irr(P*S+netdebt,pre_ev,g)))
# FAIR: central case g=1% clears 10% pre-tax
fe=pv(pre_eq,0.01,0.10); fv=pv(pre_ev,0.01,0.10)-netdebt
print('FAIR equity basis %.0f -> $%.2f ; EV basis %.0f -> $%.2f'%(fe,fe/S,fv,fv/S))
# CHEAP: lower of no-growth case at 10% pre-tax, and two-thirds of bottom of value range
c1=pv(pre_eq,0,0.10)/S; c2=(2/3)*pv(base,0,r)/S
print('CHEAP candidates: no-growth at 10%% pre-tax $%.2f ; two-thirds of range bottom $%.2f'%(c1,c2))
# whole-cycle fair
we=pv(whole+taxes,0.01,0.10)
print('FAIR whole-cycle equity $%.2f'%(we/S))
