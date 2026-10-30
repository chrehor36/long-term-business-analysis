"""JKHY Q5 arithmetic (after Q1-Q4 all IN). Yield, expectancy, growth needed, floor values, two-stage engine. $M."""
CAP=147.79*70112608/1e6; SH=70.112608; BOND=0.0549; FLOOR=0.10
OE={'3y capex end':387.6,'3y D&A end':436.2,'3y capex end, catch-up removed':345.6,'3y D&A end, catch-up removed':394.2,'5y capex end':319.4,'5y D&A end':362.8,'4y capex end (tax-neutral)':327.2,'4y D&A end (tax-neutral)':372.4}
print(f'cap {CAP:,.1f}')
for k,v in OE.items():
    y=v/CAP
    print(f'{k:34s} OE {v:7.1f} yield {y:.2%} | vs bond {y-BOND:+.2%} | g needed floor {FLOOR-y:.2%} bond {BOND-y:.2%} | exp g0 {y:.2%} g3.2 {y+.032:.2%} g5 {y+.05:.2%} g6.2 {y+.062:.2%} | floor value g3.2 ${v/(FLOOR-.032)/SH:.2f} g5 ${v/(FLOOR-.05)/SH:.2f} g0 ${v/FLOOR/SH:.2f}')
def two(oe,g1,n=10,g2=0.03,r=FLOOR):
    v=0;x=oe
    for t in range(1,n+1): x*=1+g1; v+=x/(1+r)**t
    return (v+x*(1+g2)/(r-g2)/(1+r)**n)/SH
for k in ('3y capex end','3y D&A end'):
    print('two-stage engine (10y then 3%, at 10%):',k, ', '.join(f'g1 {g:.1%}: ${two(OE[k],g):.2f}' for g in (0.032,0.05,0.062,0.075)))
print('bands: floor at g3.2 capex end', round(387.6/0.068/SH,2), '| 5% ceiling D&A end', round(436.2/0.05/SH,2))
