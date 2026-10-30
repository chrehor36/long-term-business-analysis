import re, sys, io, glob, json
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from cfdump import section
NUM=r'(\([\d,.]+\)|[\d,]+\.\d|—|-)'
LAB={'ni':r'Net income(?: attributable to [A-Za-z ,.]+)?','da':r'Depreciation and amortization','dep':r'Depreciation',
 'amort':r'Amortization(?: of intangible assets| of intangibles)?',
 'sbc':r'(?:Share-based payment expense|Stock-based compensation expense|Share-based compensation expense)',
 'ocf':r'Net cash provided by operating activities(?: of continuing operations)?',
 'capex':r'Purchases of property, plant,? and equipment','ppe_sale':r'Proceeds from sale of property, plant,? and equipment',
 'acq':r'Acquisitions? of businesses(?:, net of cash acquired)?','buyback':r'Repurchases of common stock','div':r'Dividends paid',
 'tax_paid':r'Income taxes paid(?:, net of refunds)?','int_paid':r'Interest paid','imp':r'Asset impairments?',
 'pension_settle':r'Pension settlement loss','ar':r'Accounts receivable','inv':r'Inventories','prep':r'Prepayments and other current assets',
 'ap':r'Accounts payable','ocl':r'Other current liabilities','other_op':r'Other operating activities','dtax':r'Deferred income taxes',
 'ocf_total':r'Net cash provided by operating activities'}
def val(s):
    if s in('—','-'): return 0.0
    neg=s.startswith('('); v=float(s.strip('()').replace(',',''))
    return -v if neg else v
def parse(fn):
    s=section(fn)
    if not s: return None
    flat=re.sub(r'[|$\n]',' ',s); flat=re.sub(r'\s+',' ',flat)
    flat=re.sub(r'\(\s+','(',flat); flat=re.sub(r'\s+\)',')',flat)
    yrs=re.search(r'(20\d\d) (20\d\d) (20\d\d)',flat)
    out={'years':[int(x) for x in yrs.groups()]}
    for k,l in LAB.items():
        m=re.search(r'(?<![A-Za-z])'+l+r' '+NUM+' '+NUM+' '+NUM+r'(?![\d,])',flat)
        if m: out[k]=[val(x) for x in m.groups()[-3:]]
    return out
if __name__=='__main__':
    res={}
    for fn in sorted(glob.glob('tenk_FY20??.txt'))+['tenk25_ayi-20250831.htm.txt']:
        r=parse(fn); res[fn]=r
        print(fn, r and r['years'])
        if r:
            for k,v in r.items():
                if k!='years': print('   ',k,v)
    json.dump(res,open('cf_parsed.json','w'),indent=1)
