import csv, sys, collections
k = sys.argv[1]; codes = sys.argv[2].split(',')
rs = list(csv.DictReader(open(f'data/usim_{k}.csv', encoding='utf-8')))
tab = collections.defaultdict(dict); names = {}
for r in rs:
    key = r['DT_FIM_EXERC'] + ('' if r['SRC']=='dfp' else ' '+r['DT_INI_EXERC'][5:7])
    if r['SRC']=='dfp' and r['DT_FIM_EXERC'][:4]!=r['DT_REFER'][:4]: continue
    tab[key][r['CD_CONTA']] = float(r['VL_CONTA'])/1000.0
    names.setdefault(r['CD_CONTA'], set()).add(r['DS_CONTA'][:38])
keys = sorted(tab)
print('code'.ljust(14), ' '.join(x[:10].rjust(9) for x in keys))
for c in codes:
    print(c.ljust(14), ' '.join(f"{tab[x].get(c,float('nan')):9.0f}" for x in keys), '|', '/'.join(sorted(names.get(c,['?'])))[:60])
