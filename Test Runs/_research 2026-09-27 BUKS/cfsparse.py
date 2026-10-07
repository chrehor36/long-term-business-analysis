import re,json
NUM=r'\(?-?[\d,]+\)?|-(?=\s)'
def val(tok):
    tok=tok.strip()
    if tok in ('-',''): return 0.0
    neg=tok.startswith('(')
    v=float(tok.strip('()').replace(',',''))
    return -v if neg else v
LAB={'ocf':r'(?:Net cash provided by operating activities|Cash flows from operating activities|Net cash provided by \(used in\) operating activities|Cash provided by \(used in\) operating activities)',
 'capex':r'Capital expenditures',
 'da':r'Depreciation and amortization',
 'stc_amort':r'Amortization \(Supplemental Type Certificates\)',
 'stock_401k':r'Stock issued for benefit plan',
 'stock_opt':r'Stock options issued to employees and directors',
 'stock_serv':r'Stock issued for services',
 'stock_dir':r'Stock (?:awarded|issued) to directors?',
 'rsu':r'Deferred compensation, restricted stock',
 'air_proc':r'Proceeds from sale of (?:airplanes?|land/other assets)',
 'nci_dist':r'Distribution to noncontrolling member',
 'forgive':r'Forgiveness of debt'}
out={}
for y in range(2011,2027):
    s=open(f'cfs_{y}.txt',encoding='utf-8').read().replace('|',' ')
    s=re.sub(r'\s+',' ',s)
    s=s[s.find('OPERATING ACTIVITIES'):]
    d={}
    for k,lab in LAB.items():
        m=re.search(lab+r'\s*\$?\s*('+NUM+')',s)
        d[k]=val(m.group(1)) if m else None
    # 2011 file in dollars
    if y<=2011:
        d={k:(v/1000 if v is not None else None) for k,v in d.items()}
    out[y]=d
json.dump(out,open('cfs_parsed.json','w'),indent=1)
for y,d in out.items(): print(y,{k:v for k,v in d.items() if v not in (None,0.0)})
