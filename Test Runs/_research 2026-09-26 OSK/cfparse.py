import re,json
t=open('cf_text.txt',encoding='utf-8').read()
num=r'\(?\s*-?[\d,]+\.\d\s*\)?|�|--|—'
def val(s):
    s=s.strip()
    if s in ('�','--','—'): return 0.0
    neg=s.startswith('(')
    v=float(re.sub(r'[^\d.]','',s)); return -v if neg else v
labels={
 'ocf':r'Net cash provided by (?:\(used (?:in|by)\) )?operating activities',
 'sbc':r'Stock-based (?:incentive )?compensation(?: expense)?(?! \w)',
 'da':r'Depreciation and amortization',
 'capex':r'Additions to property, plant and equipment',
 'rental':r'Additions to equipment held for rental',
 'rental_sale':r'Proceeds from sale of equipment held for rental',
 'ppe_sale':r'Proceeds from sale of property, plant and equipment',
 'acq':r'Acquisitions? of (?:a )?business(?:es)?, net of cash acquired',
 'int':r'Cash paid for interest\s*\$?',
 'adv':r'Customer advances',
 'buyback':r'(?:Repurchases|Purchase) of [Cc]ommon [Ss]tock',
 'div':r'Dividends paid',
 'ni':r'Net (?:\(loss\) )?income(?: \(loss\))?\s*\$?',
}
res={}
for blk in t.split('===== ')[1:]:
    fn=blk.split('\n')[0].strip(); body=blk[:9000]
    # stop at notes
    body=re.split(r'accompanying notes',body)[0]
    r={}
    for k,p in labels.items():
        m=re.search(p+r'\s*\$?\s*('+num+r')\s*\$?\s*('+num+r')?\s*\$?\s*('+num+r')?',body)
        r[k]=[val(x) for x in m.groups() if x] if m else None
    res[fn]=r
    print(fn, {k:(v[0] if v else None) for k,v in r.items()})
json.dump(res,open('cf_parsed.json','w'),indent=1)
