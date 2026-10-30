C=497801.4; SH=876.00994
bases={'5y capex 11,501':11501,'FY2025 normalized 15,100':15100,'TTM 15,360':15360,'FY2025 15,836':15836}
print('PERPETUAL: expectancy at g, and g needed for 10%')
for k,oe in bases.items():
    y=oe/C
    row=[f"g={g*100:.0f}%: {(y*(1+g)+g)*100:.2f}%" for g in (0.0,0.03,0.05)]
    greq=(0.10*C-oe)/(C+oe)
    print(f"{k}: yield {y*100:.2f}% | "+' | '.join(row)+f" | g needed {greq*100:.2f}% | g for bond {((0.0549*C-oe)/(C+oe))*100:.2f}%")
def pv(oe,g1,n,g2,r):
    v=0; x=oe
    for t in range(1,n+1):
        x*=1+g1; v+=x/(1+r)**t
    tv=x*(1+g2)/(r-g2); return v+tv/(1+r)**n
def irr(oe,g1,n,g2):
    lo,hi=g2+0.0005,0.40
    for _ in range(200):
        m=(lo+hi)/2
        if pv(oe,g1,n,g2,m)>C: lo=m
        else: hi=m
    return m
print('\nTWO-STAGE ENGINE (casts no vote): IRR at the price, 10 years at g1 then g2 forever')
for k,oe in bases.items():
    for g2 in (0.04,0.05):
        print(k,f"g2={g2*100:.0f}%",' | '.join(f"g1 {g1*100:.0f}%: {irr(oe,g1,10,g2)*100:.2f}%" for g1 in (0.06,0.08,0.10,0.12,0.14,0.16)))
print('\ng1 (10 yrs) needed for 10% IRR:')
for k,oe in bases.items():
    for g2 in (0.04,0.05):
        lo,hi=-0.05,0.40
        for _ in range(200):
            m=(lo+hi)/2
            if pv(oe,m,10,g2,0.10)<C: lo=m
            else: hi=m
        print(k, f"g2 {g2*100:.0f}% -> g1 {m*100:.2f}%", f"(OE year 10 = {oe*(1+m)**10:,.0f}; revenue at 48% margin {oe*(1+m)**10/0.483:,.0f})")
print('\nVALUE per share at the ~10% floor (price at which IRR = 10%):')
for k,oe in bases.items():
    out=[]
    for g1,g2 in ((0,0),(0.03,0.03),(0.05,0.05),(0.08,0.05),(0.10,0.05),(0.12,0.05),(0.08,0.04),(0.10,0.04)):
        v=pv(oe,g1,10,g2,0.10) if g1!=g2 else oe*(1+g1)/(0.10-g1)
        out.append(f"{g1*100:.0f}/{g2*100:.0f}: ${v/SH:,.0f}")
    print(k,' | '.join(out))
print('\nat the bond 5.49%, no growth: ', {k:round(oe/0.0549/SH) for k,oe in bases.items()})
print('five-year-out bottom boundary: 15,100 x 1.06^5 =', round(15100*1.06**5), 'cap / that =', round(C/(15100*1.06**5),1), '| top 15,836 x 1.14^5 =', round(15836*1.14**5), 'cap/that', round(C/(15836*1.14**5),1))
