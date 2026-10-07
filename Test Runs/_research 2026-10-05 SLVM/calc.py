# COMPUTATION - NOT A CLEARANCE. Inputs from the filed cash-flow statements (continuing operations).
r=0.0563; sh=39.760243; price=33.31
ocf ={2021:423,2022:418,2023:504,2024:469,2025:268}
sbc ={2021:14,2022:20,2023:23,2024:23,2025:18}
cap ={2021:69,2022:149,2023:210,2024:221,2025:224}
da  ={2021:126,2022:125,2023:143,2024:159,2025:179}
oc ={y:ocf[y]-sbc[y]-cap[y] for y in ocf}
ocd={y:ocf[y]-sbc[y]-da[y] for y in ocf}
print("owner cash capex basis",oc, "mean5",sum(oc.values())/5)
print("owner cash D&A basis",ocd,"mean5",sum(ocd.values())/5)
def val(base,g,yrs=10):
    pv=0;c=base
    for t in range(1,yrs+1):
        c*=1+g; pv+=c/(1+r)**t
    term=c/r/(1+r)**yrs   # zero nominal growth after year 10
    return pv+term
def show(lbl,base,g):
    v=val(base,g); print(f"{lbl}: base {base:.1f} g {g*100:.1f}% value {v:,.0f}M  ${v/sh:.2f}/sh")
    return v/sh
m5=sum(oc.values())/5
g5=(oc[2025]/oc[2021])**(1/4)-1
hi=show("5yr no-growth",m5,0.0); lo=show("5yr shown-growth",m5,g5); print("ratio",hi/lo)
wc=sum(oc[y] for y in (2022,2023,2024,2025))/4
gwc=(oc[2025]/oc[2022])**(1/3)-1
hi2=show("whole-cycle 2022-25 no-growth",wc,0.0); lo2=show("whole-cycle shown-growth",wc,gwc); print("ratio",hi2/lo2)
md=sum(ocd.values())/5; gd=(ocd[2025]/ocd[2021])**(1/4)-1
show("D&A var no-growth",md,0); show("D&A var shown",md,gd)
# fair price: central case = whole-cycle owner cash, declining at the filer's stated UFS demand CAGR, clears 10% pre-tax
tax=(116+103+67)/(369+405+199)
hurdle=0.10*(1-tax); print("tax",tax,"after-tax hurdle",hurdle)
for g in (-0.021,-0.011,0.0):
    P=wc/(hurdle-g); print(f"fair (wc, g {g*100:.1f}%): {P:,.0f}M ${P/sh:.2f}")
    P=m5/(hurdle-g); print(f"fair (5yr, g {g*100:.1f}%): {P:,.0f}M ${P/sh:.2f}")
# cheap: trough year 2025 alone at no growth clears the floor
P=oc[2025]/hurdle; print(f"cheap (2025 trough, no growth): {P:,.0f}M ${P/sh:.2f}")
print("half of fair (wc,-2.1%):", wc/(hurdle+0.021)/sh/2)
print("mktcap",price*sh,"yield wc",wc/(price*sh),"yield 5yr",m5/(price*sh))
# TTM to June 2026
ttm_ocf=268-87+28; ttm_cap=224-114+110; ttm_sbc=18-13+6
print("TTM owner cash",ttm_ocf-ttm_sbc-ttm_cap, ttm_ocf,ttm_cap,ttm_sbc)
