# Q4/Q5 arithmetic, both perimeters. Inputs are filed figures; see run file for sources.
price=273.79; sh=594.075498; cap=price*sh; sov=5.49
print(f'cap ${cap:,.1f}M')
# standalone constructions ($M): 3y capex end, 3y filer-split middle, 3y D&A end, 5y, 10y, 23y, TTM
mid=[8379-107-(3606-664-57), 9346-118-(3452-500-143), 9290-142-(3791-617-311)]
S={'3y capex end':5266.3,'3y filer split (capex less capacity/commercial and lease buyouts)':sum(mid)/3,'3y D&A end':6489.0,
   '5y capex end':5490.0,'5y D&A end':6644.0,'10y capex end':5103.3,'10y D&A end':6260.3,'23y capex end':3086.9,'23y D&A end':4384.3,
   'TTM to 2026-06-30 capex end':10263-131-3759,'TTM D&A end':10263-131-2513}
print('filer-split by year',mid)
for k,v in S.items():
    y=v/cap*100
    print(f'STANDALONE {k:70s} ${v:,.1f}M  {y:.2f}%  per share ${v/sh:.2f}  g to reach 10%: {10-y:.2f}%  vs bond {y-sov:+.2f}')
# combined perimeter
nsc={'capex':(812+1631+2094)/3,'da':(1841+2659+2905)/3,'capex_acq':(812-12+2094)/3}
print('NSC 3y', {k:round(v,1) for k,v in nsc.items()})
newsh=225.0; tsh=sh+newsh
for rate in (5.10,5.35,5.60):
    at=20000*rate/100*(1-0.22)
    for lab,u,n in (('capex end',5266.3,nsc['capex']),('D&A end',6489.0,nsc['da']),('capex end, NSC CSR purchase counted',5266.3,nsc['capex_acq'])):
        base=u+n-at
        for syn,sl in ((0,'no synergies'),(2750*(1-0.22),'full claimed $2.75bn pre-tax synergies')):
            oe=base+syn; ccap=price*tsh
            print(f'COMBINED rate {rate}% {lab:40s} {sl:40s} OE ${oe:,.1f}M per share ${oe/tsh:.2f} yield {oe/ccap*100:.2f}%  g to 10%: {10-oe/ccap*100:.2f}%')
print('combined cap at $273.79:', round(price*tsh,1))
# value range: price at which OE/P + g = 10%
def val(oe,g,shares): return oe/((10-g)/100)/shares
print('\nVALUE (floor price) standalone:')
for lab,oe in (('3y capex end',5266.3),('filer split',sum(mid)/3),('3y D&A end',6489.0)):
    for g in (0,3.1,4.0,5.0):
        print(f'  {lab:14s} g={g}%  ${val(oe,g,sh):,.2f}')
print('VALUE combined (5.35% new debt), per UNP share after close:')
at=20000*0.0535*0.78
for lab,oe in (('capex end no syn',5266.3+nsc['capex']-at),('capex end full syn',5266.3+nsc['capex']-at+2145),('D&A end full syn',6489+nsc['da']-at+2145)):
    for g in (3.1,5.0):
        print(f'  {lab:22s} g={g}%  ${val(oe,g,tsh):,.2f}')
# price paid for NSC at today's UNP price
paid=225*price+20000
print(f'\nconsideration at $273.79: ${paid:,.0f}M; NSC OE yield on it: capex3y {nsc["capex"]/paid*100:.2f}%  2025 capex {2094/paid*100:.2f}%  D&A3y {nsc["da"]/paid*100:.2f}%  with full synergies after tax (2025 capex) {(2094+2145)/paid*100:.2f}%  (3y D&A) {(nsc["da"]+2145)/paid*100:.2f}%')
# coverage [E2-54]
unp_before_int=9290+1311-3791
print(f'\nUNP 2025: OCF+interest paid-capex = {unp_before_int}; interest expense 1,309 -> cover {unp_before_int/1309:.1f}x')
nsc_before=4361+765-2204
comb_int=1309+792+20000*0.0535
print(f'combined: ({unp_before_int}+{nsc_before}) / {comb_int:.0f} = {(unp_before_int+nsc_before)/comb_int:.1f}x')
