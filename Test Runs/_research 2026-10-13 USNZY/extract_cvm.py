import zipfile, csv, io, sys, os
base = sys.argv[1]
out = sys.argv[2]
CNPJ = '60.894.730/0001-05'
kinds = ['BPA_con','BPP_con','DRE_con','DFC_MI_con','DVA_con']
rows = {k: [] for k in kinds}
docs = []; cap = []
def read(z, name):
    with z.open(name) as f:
        return list(csv.DictReader(io.TextIOWrapper(f, encoding='latin1'), delimiter=';'))
files = sorted(os.listdir(base))
for fn in files:
    if not fn.endswith('.zip'): continue
    z = zipfile.ZipFile(os.path.join(base, fn))
    pref = fn.replace('.zip','')
    typ, year = pref.split('_')[0], pref.split('_')[-1]
    for n in z.namelist():
        for k in kinds:
            if n.endswith(f'_{k}_{year}.csv'):
                for r in read(z, n):
                    if r['CNPJ_CIA'] == CNPJ and r.get('ORDEM_EXERC','').startswith('ÚLT'):
                        r['SRC'] = typ; rows[k].append(r)
        if n == f'{pref}.csv':
            docs += [dict(r, SRC=typ) for r in read(z, n) if r['CNPJ_CIA'] == CNPJ]
        if 'composicao_capital' in n:
            cap += [dict(r, SRC=typ) for r in read(z, n) if r['CNPJ_CIA'] == CNPJ]
os.makedirs(out, exist_ok=True)
for k, rs in rows.items():
    if not rs: continue
    keys = ['SRC','DT_REFER','VERSAO','DT_INI_EXERC','DT_FIM_EXERC','CD_CONTA','DS_CONTA','ESCALA_MOEDA','VL_CONTA']
    with open(os.path.join(out, f'usim_{k}.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction='ignore'); w.writeheader(); w.writerows(rs)
for name, rs in [('docs', docs), ('capital', cap)]:
    if rs:
        with open(os.path.join(out, f'usim_{name}.csv'), 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(rs[0].keys())); w.writeheader(); w.writerows(rs)
print({k: len(v) for k, v in rows.items()}, len(docs), len(cap))
