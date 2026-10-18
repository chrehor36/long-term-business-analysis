import csv, sys, os, collections
base = os.path.dirname(os.path.abspath(__file__))
s = sys.argv[1]; maxlev = int(sys.argv[2]) if len(sys.argv)>2 else 9
rows = list(csv.DictReader(open((os.path.join(base,'cache',f'cvm_lzr_{s}.csv') if s in ('DMPL_con','BPP_con') else os.path.join(base, f'cvm_lzr_{s}.csv')), encoding='utf-8')))
tab = collections.OrderedDict(); years=set()
for r in rows:
    y = r['DT_FIM_EXERC'][:4] if 'DT_FIM_EXERC' in r else r['DT_REFER'][:4]
    code = r['CD_CONTA']
    if code.count('.')+1 > maxlev: continue
    key=(code, r['DS_CONTA'][:55])
    tab.setdefault(key, {})[y] = float(r['VL_CONTA'])/ (1 if r.get('ESCALA_MOEDA','MIL')=='MIL' else 1000)
    years.add(y)
years = sorted(years)
print('code'.ljust(14), 'account'.ljust(56), ' '.join(y.rjust(9) for y in years))
for (c,d),v in sorted(tab.items(), key=lambda kv: [int(x) for x in kv[0][0].split('.')]):
    print(c.ljust(14), d.ljust(56), ' '.join((f"{v[y]/1000:9.0f}" if y in v else ' '*9) for y in years))
