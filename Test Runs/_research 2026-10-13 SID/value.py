SH=1326.093947  # million shares
P=6.45
MC=SH*P
# 30 June 2026 ITR (6-K 0001292814-26-004375): borrowings 8,326.693+45,038.867; leases 241.881+798.787; cash 13,630.963; fin. inv. 654.791+26.232
ND=8326.693+45038.867+241.881+798.787-13630.963-654.791-26.232
ADVS=4352.609+8748.729   # contract liabilities (customer advances), 30 June 2026
FORF=1504.134
def pv(c0,g,r,n=10):
    v=0;c=c0
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+r)**t
    v+= c/r/(1+r)**n
    return v
def case(label,c0,g,r,debt):
    ev=pv(c0,g,r); eq=ev-debt
    return eq/SH
S=0.1257
print(f"market cap R${MC:,.0f}m  net debt R${ND:,.0f}m  EV R${MC+ND:,.0f}m  advances {ADVS:,.0f}  forfaiting {FORF:,.0f}")
# halves
ae_h1, ae_h2 = 3071, 1560          # all-equity recast, organic (purchases left out), all spending
m_h1, m_h2 = 3071-35, 1560+1128    # maintenance case (capex above D&A added back)
eq_h1, eq_h2 = 1515-35, -579+1128  # equity-only, maintenance case
import math
g_ae=(ae_h2/ae_h1)**(1/5)-1; g_m=(m_h2/m_h1)**(1/5)-1; g_eq=(eq_h2/eq_h1)**(1/5)-1
print(f"growth halves: all-spending {g_ae:.1%}, maintenance {g_m:.1%}, equity-only maint {g_eq:.1%}")
base_m=2316+546; base_ae=2316; base_eq=468+546
for lab,c0,g in (("all-equity maintenance (central)",base_m,g_m),("all-equity all spending",base_ae,g_ae)):
    for r in (S,0.10):
        top=case(lab,c0,0,r,ND); bot=case(lab,c0,g,r,ND)
        print(f"{lab} @{r:.2%}: top(no growth) R${top:.2f}/sh  bottom({g:.1%}) R${bot:.2f}/sh  avg {((top+bot)/2):.2f}")
    print(f"   with advances as debt @12.57%: top R${case(lab,c0,0,S,ND+ADVS):.2f}  @10% top R${case(lab,c0,0,0.10,ND+ADVS):.2f}")
    print(f"   yield at price: {c0/(MC+ND):.1%} of EV")
for r in (S,0.10):
    top=case("eq",base_eq,0,r,0); bot=case("eq",base_eq,g_eq,r,0)
    print(f"equity-only maintenance @{r:.2%}: top R${top:.2f} bottom({g_eq:.1%}) R${bot:.2f} avg {(top+bot)/2:.2f}; yield at price {base_eq/MC:.1%}")
# as-filed sensitivities (advances counted as owner cash)
asf_ae=1934+27991*0.66/10+546
print(f"as-filed all-equity incl. advances, maintenance: {asf_ae:,.0f}/yr = {asf_ae/(MC+ND):.1%} of EV")
