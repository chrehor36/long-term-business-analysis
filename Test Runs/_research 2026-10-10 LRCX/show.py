import csv,collections,sys
for t in sys.argv[1:]:
    d=collections.defaultdict(dict)
    for r in csv.DictReader(open(f'series_{t}.csv')):
        d[r['fiscal_end']][r['metric']]=float(r['value_millions'])
    ms=['revenue','gross_profit','op_income','rnd','ocf','capex','sbc','buyback','dividends','acq_paid','diluted_shares','net_income']
    print(t); print('end        '+' '.join(f'{m[:8]:>9}' for m in ms))
    for e in sorted(d):
        print(e, ' '.join(f'{d[e].get(m,float("nan")):9.0f}' for m in ms))
