import re,sys
pats = ['Net loss','Depreciation and amortization','Stock-based compensation','Deferred revenue and customer deposits',
        'Net cash provided by (used in) operating activities','Net cash used in operating activities',
        'Purchase of property, plant and equipment','Impairment']
for fn in sys.argv[1:]:
    txt=open(fn,encoding='utf-8',errors='replace').read().split('\n')
    # find the cash flow statement start
    idx=[i for i,l in enumerate(txt) if 'Consolidated Statements of Cash Flows' in l]
    print('='*20, fn, 'CF headers at', idx)
    if not idx: continue
    start=idx[-1]
    for i in range(start, min(start+130, len(txt))):
        l=txt[i].strip()
        if any(p.lower() in l.lower() for p in pats) or 'Years Ended' in l or re.match(r'^\|?\s*\d{4}\s*\|',l):
            print(i, l[:180])
            if not re.search(r'\d',l) and i+1<len(txt): print('   ->',txt[i+1].strip()[:180])
