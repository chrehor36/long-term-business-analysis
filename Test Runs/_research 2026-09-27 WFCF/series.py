import re,glob,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
files=sorted(glob.glob('filings/*_10-K_*.txt'))
pats={'ver_rev':r'Verification and certification (?:service )?revenue','prod_rev':r'Product sales','ps_rev':r'(?:Professional services|Consulting) (?:revenue)?','tot_rev':r'Total revenues?','ver_cost':r'Costs? of verification and certification(?: services)?','prod_cost':r'Costs? of products','ps_cost':r'Costs? of (?:professional services|consulting)','gp':r'Gross profit','sga':r'Selling, general and administrative expenses','opinc':r'(?:Income|Earnings) \(?(?:loss)?\)? ?from operations|Operating income','ocf':r'Net cash provided by (?:\(used in\) )?operating activities','capex':r'Purchases? of property(?:,| and) equipment[^|]*','sbc':r'Stock[- ]based compensation(?: expense)?','da':r'Depreciation and amortization','buy':r'(?:Stock repurchase|Repurchase of common)[^|]*','ni':r'Net income(?: \(loss\))?(?: attributable to [^|]*)?'}
num=r'\|\s*\$?\s*\|?\s*(\(?\s*[\d,]+\s*\)?|—|-)'
for f in files:
    s=open(f,encoding='utf-8').read(); s=re.sub(r'\s*\n\s*',' ',s)
    i=s.find('Statements of Cash Flows', s.find('Report of Independent'))
    print('=====',f)
    for k,p in pats.items():
        m=re.search('('+p+r')\s*((?:\|\s*[\$]?\s*)+)(\(?\s*[\d,]+\s*\)?)\s*((?:\|\s*[\$]?\s*)+)(\(?\s*[\d,]+\s*\)?)', s[s.find('Report of Independent'):])
        if m: print(k, '|', m.group(1)[:50], '|', m.group(3).replace(' ',''), '|', m.group(5).replace(' ',''))
