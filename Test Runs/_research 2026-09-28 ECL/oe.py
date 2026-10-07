# Owner earnings, priced perimeter (continuing operations, post-ChampionX), from the filed cash-flow statements.
# OCF - SBC - (c); (c) at three ends: capex (gross), depreciation (PP&E incl. capitalized software), depreciation + acquired-intangible amortization.
import sys; sys.stdout.reconfigure(encoding='utf-8')
cap=78349.0; bond=5.49; sh=280.328603
R={ # FY: OCF, SBC, capex, dep, amort   (FY2018-2020: FY2020 10-K continuing; 2021-22: FY2022 10-K; 2023-25: FY2025 10-K)
2018:(2006.9,88.0,778.7,535.9,194.5),
2019:(2046.7,84.0,731.3,569.1,206.2),
2020:(1741.8,82.1,489.0,594.3,218.4),
2021:(2061.9,89.5,643.0,604.4,238.7),
2022:(1788.4,87.8,712.8,618.5,320.2),
2023:(2411.8,95.1,774.8,616.7,306.9),
2024:(2813.9,134.8,994.5,634.9,300.5),
2025:(2952.6,136.6,1048.3,672.6,303.8)}
H1_26=(1175.4,75.1,588.6,364.3,167.7); H1_25=(1071.2,75.9,454.6,327.9,149.9)
TTM=tuple(a+b-c for a,b,c in zip(R[2025],H1_26,H1_25))
def oe(r): o,s,c,d,a=r; return o-s-c, o-s-d, o-s-d-a
print('FY   OCF   SBC  capex  dep  amort | OE capex end | OE dep end | OE dep+amort end | capex/dep')
for y,r in list(R.items())+[('TTM',TTM)]:
    e=oe(r); print(y, ' '.join(f'{v:.1f}' for v in r), '|', ' | '.join(f'{v:.1f}' for v in e), f'| {r[2]/r[3]:.2f}')
ys=sorted(R)
def win(yy):
    rows=[R[y] for y in yy]; m=tuple(sum(c)/len(rows) for c in zip(*rows)); return oe(m)
print('\nTrailing windows ending FY2025 (mean $M, yield on cap %.1f):'%cap)
for n in range(1,9):
    yy=ys[-n:]; e=win(yy)
    print(f'{n}y FY{yy[0]}-{yy[-1]}: capex end {e[0]:.1f} ({100*e[0]/cap:.2f}%) | dep end {e[1]:.1f} ({100*e[1]/cap:.2f}%) | dep+amort end {e[2]:.1f} ({100*e[2]/cap:.2f}%)')
e=oe(TTM); print(f'TTM to 2026-06-30: capex end {e[0]:.1f} ({100*e[0]/cap:.2f}%) | dep end {e[1]:.1f} ({100*e[1]/cap:.2f}%) | dep+amort end {e[2]:.1f} ({100*e[2]/cap:.2f}%)')
print('\nRolling five-year windows:')
for i in range(len(ys)-4):
    yy=ys[i:i+5]; e=win(yy); print(f'FY{yy[0]}-{yy[-1]}: capex {e[0]:.1f} ({100*e[0]/cap:.2f}%) dep {e[1]:.1f} ({100*e[1]/cap:.2f}%) dep+amort {e[2]:.1f} ({100*e[2]/cap:.2f}%)')
# screen reproduction
e5=win(ys[-5:]); e3=win(ys[-3:])
print('\nscreen oe_bottom 1373 vs 5y dep+amort end %.1f ; oe_top 1665 vs 3y capex end %.1f'%(e5[2],e3[0]))
# CoolIT financing: coupons on the May 2026 notes
notes=[(1200,4.600),(900,4.800),(1500,5.150),(1400,5.350)]
intr=sum(p*c/100 for p,c in notes); print('\nAnnual coupon on the $5.0bn May 2026 notes: %.1f pre-tax; after 21%% tax %.1f'%(intr,intr*0.79))
print('CoolIT NTM EBITDA implied by 29x on $4,750M: %.1f'%(4750/29))
# per-share, no growth, at floor and at bond
print('\nPer share, no growth (value = OE / rate):')
for lab,val in [('5y capex',e5[0]),('5y dep',e5[1]),('3y capex',e3[0]),('3y dep',e3[1]),('1y capex',oe(R[2025])[0]),('1y dep',oe(R[2025])[1]),('TTM capex',oe(TTM)[0]),('TTM dep',oe(TTM)[1])]:
    print(f'{lab}: {val:.1f} -> ${val/0.10/sh:.0f} at 10%, ${val/(bond/100)/sh:.0f} at {bond}%; growth to reach 10%% floor g=(0.10-y)/(1+y) = {100*(0.10-val/cap)/(1+val/cap):.2f}%')
