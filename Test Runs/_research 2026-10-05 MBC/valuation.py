# COMPUTATION - NOT A CLEARANCE. Arithmetic for the MBC run of 2026-10-05; inputs from filings cited in the run file.
r=0.0563; t=0.24; shares=203.490; net_debt=1390.3-241.6; px=6.99
# MBC (CY) owner cash, capex basis = OCF - SBC - capex ; net interest (expense +) for unlevering
mbc={2021:(148.2,9.3,51.6,-4.6),2022:(235.6,10.9,55.9,2.2-12.9),2023:(405.6,17.8,57.3,65.2),2024:(292.0,21.9,80.9,74.0),2025:(195.7,16.1,78.2,74.1)}
amwd={2021:(151.8,4.6,35.7,23.1),2022:(24.4,4.7,44.1,10.2),2023:(198.8,7.4,42.6,16.0),2024:(230.8,10.7,91.0,8.2),2025:(108.4,8.0,39.7,10.3)}
def un(d): return {y:o-s-c+i*(1-t) for y,(o,s,c,i) in d.items()}
um,ua=un(mbc),un(amwd); comb={y:um[y]+ua[y] for y in um}
for y in comb: print(y, round(um[y],1), round(ua[y],1), round(comb[y],1))
avg=sum(comb.values())/5; print('5yr avg unlevered combined',round(avg,1))
g=(comb[2025]/comb[2021])**0.25-1; print('shown growth endpoints',round(g*100,2),'%')
int_at=91.1*(1-t); print('after-tax interest pro forma FY2025',round(int_at,1))
def pv(c,g):
    v=sum(c*(1+g)**k/(1+r)**k for k in range(1,11)); return v+c*(1+g)**10/r/(1+r)**10
def eq(c_unlev,g): return (pv(c_unlev,g)-net_debt)/shares
print('CONVENTION range: no-growth $%.2f  shown-growth $%.2f'%(eq(avg,0),eq(avg,g)))
# whole-cycle variant: Fortune Cabinets segment margin 2008-2021 avg, less standalone corporate cost, plus amortization add-back
seg=[7.36,-2.23,2.37,0.45,1.55,5.91,7.71,8.85,10.75,10.83,5.93,7.46,9.55,9.78]
wc_margin=sum(seg)/len(seg); print('segment margin avg',round(wc_margin,2))
ebit=(wc_margin-1.6)/100; amort=0.007; sales=4330.4
wc_un=sales*(ebit*(1-t)+amort); print('whole-cycle unlevered owner cash',round(wc_un,1))
print('WHOLE-CYCLE no-growth $%.2f  shown-growth $%.2f'%(eq(wc_un,0),eq(wc_un,g)))
lev=wc_un-int_at; pretax=lev/(1-t)
fair=pretax/0.10/shares; print('levered equity owner cash',round(lev,1),'pre-tax',round(pretax,1),'FAIR $%.2f'%fair,'CHEAP $%.2f'%(fair/2))
lev5=avg-int_at; print('5yr-basis fair $%.2f'%((lev5/(1-t))/0.10/shares))
print('market cap',round(px*shares,1),'EV',round(px*shares+net_debt,1))
# MBC standalone at the merger (L2009-019 note): end-2025 net debt
nd25=974.5-183.3; mb_avg=sum(um.values())/5
for lbl,c in (('5yr',mb_avg),('whole-cycle',2734.7*(ebit*(1-t)+amort))):
    print('MBC alone',lbl,'no-growth $%.2f'%((pv(c,0)-nd25)/127.2))
