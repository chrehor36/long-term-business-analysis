"""Extract Localiza Rent a Car (CD_CVM 019739) consolidated DFP rows from CVM open-data zips.
Writes cvm_lzr_<stmt>.csv (all years, last-exercise rows only) into this folder."""
import zipfile, csv, io, sys, os
base = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(base, 'cache', 'cvm')
stmts = ['BPA_con','BPP_con','DRE_con','DFC_MI_con','DMPL_con','DVA_con','composicao_capital']
out = {s: [] for s in stmts}
for y in range(2015, 2026):
    z = zipfile.ZipFile(os.path.join(cache, f'dfp_cia_aberta_{y}.zip'))
    for s in stmts:
        name = f'dfp_cia_aberta_{s}_{y}.csv'
        if name not in z.namelist():
            continue
        with z.open(name) as f:
            r = csv.reader(io.TextIOWrapper(f, encoding='latin1'), delimiter=';')
            hdr = next(r)
            for row in r:
                d = dict(zip(hdr, row))
                if d.get('CD_CVM','').lstrip('0') != '19739':
                    continue
                if 'ORDEM_EXERC' in d and d['ORDEM_EXERC'] != 'ÚLTIMO':
                    continue
                out[s].append(d)
for s, rows in out.items():
    if not rows: continue
    keys = list(rows[0].keys())
    with open((os.path.join(base,'cache',f'cvm_lzr_{s}.csv') if s in ('DMPL_con','BPP_con') else os.path.join(base, f'cvm_lzr_{s}.csv')), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, keys, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
    print(s, len(rows))
