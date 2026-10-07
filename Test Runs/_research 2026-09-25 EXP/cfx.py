import re,sys
labels=['Net Earnings','Net Earnings from Continuing Operations','Depreciation, Depletion, and Amortization','Depreciation, Depletion and Amortization','Stock Compensation Expense','Equity in Earnings of Unconsolidated Joint Venture','Distributions from Joint Venture','Net Cash Provided by Operating Activities','Additions to Property, Plant, and Equipment','Additions to Property, Plant and Equipment','Acquisition Spending','Minority Investment','Purchase and Retirement of Common Stock','Dividends Paid to Stockholders','Impairment Losses','Proceeds from Sale of Businesses','Net Cash Provided by Operating Activities from Continuing Operations']
for f in sys.argv[1:]:
    L=open(f,encoding='utf-8').read().split('\n')
    # find cash flow statement
    st=[i for i,l in enumerate(L) if 'Consolidated Statements of Cash Flows' in l and 'Subsidiaries' in l]
    if not st: st=[i for i,l in enumerate(L) if 'STATEMENTS OF CASH FLOWS' in l.upper()]
    i0=st[0]; seg=L[i0:i0+260]
    print('==',f,i0, seg[1:5])
    for j,l in enumerate(seg):
        if '|' in l:
            cells=[c.strip() for c in l.split('|')]
            if cells[0] in labels: print('  ',cells[:4])
        elif l.strip() in labels:
            vals=[]
            k=j+1
            while k<len(seg) and len(vals)<3:
                s=seg[k].strip()
                if re.match(r'^\(?[\d,]+\)?$|^—$',s): vals.append(s)
                elif s: break
                k+=1
            print('  ',l.strip(),vals)
