# COMPUTATION - NOT A CLEARANCE. Arithmetic by parts for INVA, valuation date 2026-06-30 balance sheet,
# price 2026-10-05. All $ millions unless stated. Sources in the run file.
SOV=0.0566; FLOOR=0.10; SH=72.245485; PRICE=20.63
# royalty cases: gross royalties by period, (years from 2026-06-30 to mid-period, amount)
cases={
 'low':    [(0.25,118),(1.0,155),(2.0,100),(3.0,40)],
 'central':[(0.25,119),(1.0,200),(2.0,165),(3.0,120),(3.75,20)],
 'high':   [(0.25,120),(1.0,240),(2.0,233),(3.0,227)],
}
def pv(flows,r): return sum(a/(1+r)**t for t,a in flows)
# non-royalty operations (IST + corporate): low = cash burn 40/yr to end-2029 then nil; central = 0; high = carrying value of IST net assets
ist_low=[(0.25,-20),(1.0,-40),(2.0,-40),(3.0,-40)]
ist_high_carry=169.0+17.9+39.0+50.8-61.6   # intangibles+goodwill+inventory+receivables-HCR obligation (10-Q 6/30/26)
cash=570.4-10.0            # less July buybacks
roy_recv=59.8
invest=669.5; level3=315.96
debt=261.0; hcr=61.6; tax_ut=59.9; dtl=36.7; lease=0.7+10.5
def total(case,r,ist,l3_zero=False,hcr_sep=True,after_tax=False):
    roy=pv(cases[case],r)*(0.79 if after_tax else 1)
    i=invest-(level3 if l3_zero else 0)
    v=roy+ist+cash+roy_recv+i-debt-tax_ut-dtl-lease-(hcr if hcr_sep else 0)
    return roy,v,v/SH
for r,lab in [(SOV,'sovereign 5.66%'),(FLOOR,'floor 10%')]:
    print('==',lab)
    for c in cases:
        ist = pv(ist_low,r) if c=='low' else (0.0 if c=='central' else ist_high_carry)
        hs = c!='high'
        roy,v,ps=total(c,r,ist,hcr_sep=hs)
        roy2,v2,ps2=total(c,r,ist,hcr_sep=hs,after_tax=True)
        roy3,v3,ps3=total(c,r,ist,l3_zero=True,hcr_sep=hs)
        print(f'{c:8s} royaltyPV {roy:7.1f}  IST {ist:7.1f}  total {v:7.1f}  /sh {ps:6.2f} | royalty after 21% tax /sh {ps2:6.2f} | Level3 at zero /sh {ps3:6.2f}')
print('nominal royalty sums', {c:sum(a for t,a in f) for c,f in cases.items()})
print('cash+recv+invest-debt-tax-dtl-lease-hcr per share', (cash+roy_recv+invest-debt-tax_ut-dtl-lease-hcr)/SH)
print('ist_high_carry',ist_high_carry, 'per share', ist_high_carry/SH)
print('market cap', PRICE*SH)
