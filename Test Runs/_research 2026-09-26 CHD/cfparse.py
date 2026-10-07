import re,json
blocks={}
cur=None
for line in open('cf_blocks.txt',encoding='utf-8'):
    if line.startswith('#### '): cur=line.split()[1][5:9]; continue
    if cur: blocks[cur]=line
NUM=r'\(?-?[\d,]+(?:\.\d+)?\)?|—|-(?=\s)'
def first(txt,pat):
    m=re.search(pat+r'\s*(?:\(\d\)\s*)?\$?\s*('+NUM+')',txt)
    if not m: return None
    v=m.group(1)
    if v in ('—','-'): return 0.0
    neg=v.startswith('(')
    v=float(v.strip('()').replace(',',''))
    return -v if neg else v
out={}
for fy,t in sorted(blocks.items()):
    scale=1/1000 if 'thousands' in t[:300] else 1.0
    r={}
    pats={
     'ocf':r'Net Cash Provided [Bb]y Operating Activities',
     'sbc':r'Non[- ]cash compensation expense',
     'dep':r'Depreciation expense',
     'da':r'Depreciation(?:, depletion)? and amortization',
     'amort':r'Amortization expense',
     'capex':r'Additions to property, plant and equipment',
     'acq':r'(?:Acquisitions?(?: \(net of cash acquired\)|, net of cash acquired)?|Purchase of new businesses \(net of cash acquired[^)]*\))',
     'contingent':r'Contingent acquisition payments',
     'fvacq':r'Change in fair value of business acquisition liabilities',
     'payacq':r'Payment of business acquisition liabilit(?:y|ies)',
     'sale_assets':r'Proceeds from (?:the )?sale of assets',
     'sale_fixed':r'Proceeds from sale of fixed assets',
     'sale_vit':r'Proceeds from Sale of Vitamin Business',
     'sale_passport':r'Proceeds from Sale of Passport',
     'held_for_sale':r'Net proceeds from assets held for sale',
     'buyback':r'Purchase of treasury stock',
     'div':r'Payment of cash dividends',
     'interest':r'Interest \(net of amounts capitalized\)',
     'excess_tax':r'Excess tax benefit on stock options exercised',
    }
    for k,p in pats.items():
        v=first(t,p)
        if v is not None: r[k]=round(v*scale,3)
    out[fy]=r
    print(fy, r)
json.dump(out,open('cf_parsed.json','w'),indent=1)
