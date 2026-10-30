import re,json,glob
out={}
def num(s): 
    s=s.replace(',','').strip(); return float(s)
files=sorted(glob.glob('cache/k_*.txt'))+['cache/form10a_2019-05-30.txt']
for f in files:
    t=re.sub(r'\s+',' ',open(f,encoding='utf-8').read()); t=re.sub(r'(\| )+','| ',t)
    i=t.find('Statements of Income'); 
    # find the income statement with 'Product revenue |'
    for m in re.finditer(r'Product revenue \| \$? ?\|? ?([\d,]+) \| \$? ?\|? ?([\d,]+) \|',t):
        seg=t[m.start()-400:m.start()+2500]
        if 'Cost of product sales' not in seg: continue
        hdr=re.findall(r'(20\d\d) \|',t[m.start()-400:m.start()])
        yrs=[int(y) for y in hdr[-3:]] if len(hdr)>=2 else []
        def row(lbl):
            mm=re.search(re.escape(lbl)+r' \| \$? ?\|? ?([\d,]+) \| \$? ?\|? ?([\d,]+)(?: \| \$? ?\|? ?([\d,]+))?',seg)
            return [num(x) for x in mm.groups() if x] if mm else None
        rows={k:row(k) for k in ['Product revenue','Service revenue','Cost of product sales','Cost of service','Sales and marketing','General and administrative','Operating Income']}
        scale=1e3 if rows['Product revenue'][0]<1e7 else 1
        print(f, yrs, {k:v for k,v in rows.items()})
        break
