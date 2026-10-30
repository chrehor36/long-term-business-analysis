# COMPUTATION - NOT A CLEARANCE (Q2 closed OUT). Arithmetic only; every input from the filed cash-flow statements.
ys=[2020,2021,2022,2023,2024,2025]
ocf={2020:3397,2021:334,2022:2525,2023:3168,2024:1769,2025:2197}
sbc={2020:115,2021:141,2022:137,2023:188,2024:254,2025:136}
capex={2020:229,2021:295,2022:375,2023:469,2024:434,2025:475}
finlease={2024:109,2025:9}
dep={2020:746-415,2021:317,2022:296,2023:305,2024:353,2025:300}
talc={2021:3200}           # US talc payments, retained by J&J under the Separation Agreement (424B4 MD&A)
intr={2020:440,2021:440,2022:440,2023:440-224}  # standalone cash interest not borne in carve-out years; 2023 bore 224
TAX=0.21                   # disclosed judgment: US statutory rate on the interest charge
cap=17.80*1920773467/1e6
rows={}
for y in ys:
    c=capex[y]+finlease.get(y,0)
    a=ocf[y]-sbc[y]-c; b=ocf[y]-sbc[y]-dep[y]
    adj=talc.get(y,0)-intr.get(y,0)*(1-TAX)
    rows[y]=(a,b,a+adj,b+adj,c,dep[y])
    print(y,'capex(c)',c,'dep',dep[y],'OE capex end',a,'OE dep end',b,'| perimeter-adjusted',round(a+adj),round(b+adj))
print('cap $M',round(cap,1))
for n in (3,4,5,6):
    w=ys[-n:]
    f=lambda i: sum(rows[y][i] for y in w)/n
    print(f'{n}y {w[0]}-{w[-1]}: as filed {f(0):,.1f} to {f(1):,.1f} ({f(0)/cap:.2%} to {f(1)/cap:.2%}); adjusted {f(2):,.1f} to {f(3):,.1f} ({f(2)/cap:.2%} to {f(3)/cap:.2%})')
