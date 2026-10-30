import re, json, sys, io, glob
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
NUM=r'(\(\s*[\d,]+\s*\)|[\d,]+|—)'
LAB={'cash':r'Cash and cash equivalents','ltd':r'Long-term debt','cur_ltd':r'Current portion of long-term debt','gw':r'Goodwill',
'intang':r'Other intangible assets, net(?: of accumulated amortization of [\d,]+ million as of 20\d\d and [\d,]+ million as of 20\d\d)?',
'pen_asset':r'Pension plan assets','pen_liab':r'Pension plan liabilities','opeb':r'Other postretirement plan liabilities','cur_post':r'Current portion of postretirement plan liabilities',
'contract_liab':r'Contract liabilities','advances':r'Advances on contracts','billings':r'Billings in excess of costs(?: and estimated earnings)?','equity':r'Total stockholders. equity',
'assets':r'Total assets','contract_assets':r'Contract assets','ar':r'Accounts receivable, net(?: of allowance[^0-9]*?[\d,]+ million as of 20\d\d and \$?\s?[\d,]+ million as of 20\d\d)?',
'ppe':r'Property, plant, and equipment, net(?: of accumulated depreciation of \$?\s?[\d,]+ million as of 20\d\d and \$?\s?[\d,]+ million as of 20\d\d)?','tap':r'Trade accounts payable','dtl':r'Deferred tax liabilities','dta':r'Deferred tax assets'}
def val(s):
    s=s.replace(' ','')
    if s=='—': return 0.0
    neg=s.startswith('(')
    v=float(s.strip('()').replace(',',''))
    return -v if neg else v
res={}
for fn in sorted(glob.glob('tenk_FY20??.txt'))+['tenk25_hii-20251231.htm.txt']:
    t=open(fn,encoding='utf-8').read()
    seg=None
    for m in re.finditer(r'(?<!CONDENSED )CONSOLIDATED STATEMENTS OF FINANCIAL POSITION',t):
        s=t[m.start():m.start()+40000]
        if 'Current Assets' in s[:4000] or 'Current assets' in s[:4000]: seg=s
    if not seg: print(fn,'none'); continue
    i=seg.find('Total liabilities and'); seg=seg[:i+400] if i>0 else seg
    flat=re.sub(r'[|$\n]',' ',seg); flat=re.sub(r'\s+',' ',flat); flat=re.sub(r'\(\s+','(',flat); flat=re.sub(r'\s+\)',')',flat)
    flat=re.sub(r'\$\s','',flat)
    out={}
    for k,l in LAB.items():
        m=re.search(l+r' '+NUM+' '+NUM+r'(?![\d,])',flat)
        if m: out[k]=[val(x) for x in m.groups()[-2:]]
    res[fn]=out
    print(fn, out)
json.dump(res,open('bs_parsed.json','w'),indent=1)
