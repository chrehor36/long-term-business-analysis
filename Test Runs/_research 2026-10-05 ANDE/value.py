# COMPUTATION - NOT A CLEARANCE. Q7 convention arithmetic for ANDE.
exec(open('owner_cash.py').read().split("import statistics")[0].replace('print(','(lambda *a,**k:None)('))
r=0.0563; shares=33.975570; price=66.84
fin=425*r          # pre-tax carrying cost of the $425M TAMH buyout at the sovereign (CONVENTION of this run)
fin_at=fin*(1-0.21)
def pv(c,g,yrs=10):
    v=0; x=c
    for t in range(1,yrs+1):
        x=x*(1+g); v+=x/(1+r)**t
    term=x/r            # no nominal growth after year ten
    return v+term/(1+r)**yrs
import statistics as st
def base(lo,hi,idx):
    return st.mean(rows[str(y)][idx] for y in range(lo,hi+1))
out=[]
for name,lo,hi in [('5yr 2021-2025',2021,2025),('whole-cycle 2019-2025',2019,2025),('10yr 2016-2025 (rail in 2016-18)',2016,2025)]:
    oc_cx=base(lo,hi,4)-fin_at; oc_da=base(lo,hi,5)-fin_at
    # pre-tax owner cash: pretax + impairment + D&A - capex - financing cost
    ptoc=st.mean(rows[str(y)][8]+rows[str(y)][2]+rows[str(y)][1]-rows[str(y)][3] for y in range(lo,hi+1))-fin
    print(f"== {name}: after-tax OC capex basis {oc_cx:.1f}M  D&A basis {oc_da:.1f}M  pre-tax OC {ptoc:.1f}M  per share AT {oc_cx/shares:.2f}  PT {ptoc/shares:.2f}")
    for g in [-0.006,0.0,0.021]:
        v=pv(oc_cx,g)/shares; v2=pv(oc_da,g)/shares
        print(f"   g={g*100:5.1f}%  value/share capex basis ${v:6.2f}   D&A basis ${v2:6.2f}")
    print(f"   pre-tax yield at ${price}: {ptoc/shares/price*100:.1f}%   after-tax yield {oc_cx/shares/price*100:.1f}%")
    print(f"   fair price (pre-tax OC / 10%, no growth): ${ptoc/shares/0.10:.2f}")
print('financing cost pre-tax %.1fM after-tax %.1fM'%(fin,fin_at))
