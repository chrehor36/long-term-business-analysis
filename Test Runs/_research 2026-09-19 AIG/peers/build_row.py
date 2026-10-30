# Competitor row for AIG: the CB run's row (Test Runs/_research 2026-09-19 CB/peers/row_out.txt), every accession
# re-resolved here (resolve_out.txt: 15 of 15 MATCH), EXTENDED with AIG, TRV (consolidated) and HIG (Business Insurance segment).
# Basis 1 = reported combined ratio; Basis 2 = current accident year incl. catastrophes = reported + favourable PYD points.
rows = {
 # name: (reported 2021..2025, PYD points favourable-positive 2021..2025, source)
 'KNSL': ((77.1,78.5,75.4,76.4,75.9),(5.5,4.4,3.2,2.7,3.9),'CB row'),
 'ACGL': ((85.2,81.6,79.3,82.5,82.8),(4.39,7.95,4.32,3.36,3.52),'CB row'),
 'CB':   ((89.1,87.6,86.5,86.6,85.7),(2.8,2.8,1.9,2.0,2.5),'CB row'),
 'WRB':  ((89.6,89.3,89.7,90.3,90.7),(0.08,-0.38,-0.18,0.04,0.03),'CB row'),
 'RLI':  ((86.8,84.4,86.6,86.2,83.6),(None,10.75,8.42,6.22,6.13),'CB row'),
 'AXS':  ((97.5,95.8,99.9,92.3,89.8),(0.7,0.5,-8.1,0.5,1.6),'CB row'),
 'MKL':  ((90.0,92.0,98.8,95.5,94.6),(None,None,0.5,5.6,5.8),'CB row'),
 'FFH':  ((95.0,94.7,93.2,92.7,93.0),(None,)*5,'CB row; IFRS, not comparable on basis 2'),
 'TRV':  ((94.5,95.6,97.0,92.5,89.9),(1.8,1.9,0.4,1.7,2.4),'FY2025 10-K 0000086312-26-000065 lines 1338,1449; FY2023 10-K 0000086312-24-000012 lines 1370,1481; FY2022 10-K 0000086312-23-000011 line 1753; CONSOLIDATED incl. Personal'),
 'HIG-BI':((95.8,90.2,89.6,89.9,88.3),(-1.5,2.2,1.9,1.8,3.2),'Business Insurance SEGMENT: FY2025 10-K 0000874766-26-000012 lines 2311-2319; FY2023 10-K 0000874766-24-000016 lines 2473-2481'),
 'AIG':  ((95.8,91.9,90.6,91.8,90.1),(0.6,1.8,1.4,1.4,2.1),'General Insurance: FY2025 10-K 0000005272-26-000023 p44; FY2023 10-K 0000005272-24-000023; FY2021 10-K 0001104659-22-024701; excludes ADC-ceded PYD and reserve discount'),
}
def mean(v):
    v=[x for x in v if x is not None]; return sum(v)/len(v) if v else None
print('BASIS 1 reported, 2021-2025')
b1=sorted(((mean(r[0]),k) for k,r in rows.items()))
for m,k in b1: print('| %-6s | %s | **%.2f** |' % (k,' | '.join('%.1f'%x for x in rows[k][0]),m))
print('\nBASIS 2 current accident year incl. catastrophes')
b2=[]
for k,(rep,ppd,src) in rows.items():
    cay=[(r+p) if p is not None else None for r,p in zip(rep,ppd)]
    if all(c is None for c in cay): continue
    b2.append((mean(cay),k,cay,sum(c is not None for c in cay)))
for m,k,cay,n in sorted(b2): print('| %-6s | %s | **%.2f** | %d |' % (k,' | '.join('%.1f'%c if c is not None else 'n/a' for c in cay),m,n))
print('\nrank basis1:', ' > '.join(k for _,k in b1))
print('rank basis2:', ' > '.join(k for _,k,_,_ in sorted(b2)))
for k,r in rows.items(): print(k,'|',r[2])
