import csv,collections
out=open('competitor_table.csv','w',newline='',encoding='utf-8'); w=csv.writer(out)
w.writerow(['ticker','fiscal_end','revenue_m','gross_margin_pct','op_margin_pct','rnd_pct','owner_cash_m(ocf-sbc-capex)','owner_cash_pct_rev','unit'])
for t in ['LRCX','AMAT','KLAC','ASML']:
    d=collections.defaultdict(dict); unit={}
    for r in csv.DictReader(open(f'series_{t}.csv')):
        d[r['fiscal_end']][r['metric']]=float(r['value_millions']); unit[r['fiscal_end']]=r['unit']
    print(t)
    for e in sorted(d):
        x=d[e]; rev=x.get('revenue')
        if not rev: continue
        gp=x.get('gross_profit', rev-x['cost_of_rev'] if 'cost_of_rev' in x else None)
        oi=x.get('op_income')
        if oi is None and gp is not None and 'rnd' in x and 'sga' in x: oi=gp-x['rnd']-x['sga']
        oc=(x['ocf']-x.get('sbc',0)-x['capex']) if 'ocf' in x and 'capex' in x else None
        f=lambda v:'' if v is None else round(v,1)
        row=[t,e,round(rev),f(gp/rev*100 if gp is not None else None),f(oi/rev*100 if oi is not None else None),f(x.get('rnd',0)/rev*100),f(oc),f(oc/rev*100 if oc is not None else None),unit[e]]
        w.writerow(row); print('  ',row[1:])
