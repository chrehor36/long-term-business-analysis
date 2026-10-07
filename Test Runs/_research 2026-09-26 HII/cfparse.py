import re, json, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
NUM=r'(\(\s*[\d,]+\s*\)|[\d,]+|—|-)'
LAB={'ocf':r'Net cash (?:provided by|used in|provided by \(used in\)) operating activities',
 'ni':r'Net earnings(?: \(loss\))?','dep':r'Depreciation','amort':r'Amortization of purchased intangibles?(?: assets)?',
 'sbc':r'Stock-based compensation','capex':r'Capital expenditure additions','grant':r'Grant proceeds for capital expenditures',
 'capex_old':r'Additions to property, plant, and equipment','acq':r'Acquisitions? of businesses(?:, net of cash (?:received|acquired))?',
 'ap':r'Accounts payable and accruals','retiree':r'Retiree benefits','ar':r'Accounts receivable','ca':r'Contract assets',
 'inv':r'Inventoried costs','prep':r'Prepaid expenses and other assets','buyback':r'Repurchases of common stock','div':r'Dividends paid',
 'int_paid':r'Cash paid for interest','tax_paid':r'Cash paid for income taxes(?: \(net of refunds\))?','goodwill_imp':r'Goodwill impairment',
 'dtax':r'Deferred income taxes'}
def val(s):
    s=s.replace(' ','')
    if s in('—','-'): return 0.0
    neg=s.startswith('(')
    v=float(s.strip('()').replace(',',''))
    return -v if neg else v
def parse(fn):
    t=open(fn,encoding='utf-8').read()
    best=None
    for m in re.finditer(r'(?<!CONDENSED )CONSOLIDATED STATEMENTS OF CASH FLOWS',t):
        seg=t[m.start():m.start()+30000]
        if 'Operating Activities' in seg[:3000] and 'Net earnings' in seg[:6000]:
            best=seg; 
    if not best: return None
    end=best.find('Non-Cash Investing')
    if end<0: end=best.find('The accompanying notes')
    seg=best[:end+600]
    flat=re.sub(r'[|$\n]',' ',seg); flat=re.sub(r'\s+',' ',flat)
    flat=re.sub(r'\(\s+','(',flat); flat=re.sub(r'\s+\)',')',flat)
    yrs=re.search(r'(20\d\d) (20\d\d) (20\d\d)',flat)
    ys=[int(x) for x in yrs.groups()]
    out={'years':ys}
    for k,l in LAB.items():
        m=re.search(l+r' '+NUM+' '+NUM+' '+NUM+r'(?![\d,])',flat)
        if m: out[k]=[val(x) for x in m.groups()[-3:]]
    return out
res={}
import glob
for fn in sorted(glob.glob('tenk_FY20??.txt'))+['tenk25_hii-20251231.htm.txt']:
    r=parse(fn)
    print(fn, r and r['years']); 
    if r:
        for k,v in r.items():
            if k!='years': print('   ',k,v)
    res[fn]=r
json.dump(res,open('cf_parsed.json','w'),indent=1)
