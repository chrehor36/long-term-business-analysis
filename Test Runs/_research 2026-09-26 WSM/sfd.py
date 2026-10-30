import re, sys
NUM = r'\(?-?[0-9][0-9,]*\.?[0-9]*\)?%?'
def rows(fy, labels, n=5, occurrence=2):
    t = open(f'tenk_FY{fy}.txt', encoding='utf-8').read()
    ms = [m.start() for m in re.finditer(r'(?i)SELECTED (CONSOLIDATED )?FINANCIAL DATA', t)]
    s = t[ms[occurrence-1]:ms[occurrence-1]+25000]
    flat = re.sub(r'[|$\s]+', ' ', s)
    out = {}
    for lab in labels:
        pat = re.escape(lab) + r'[^0-9(]*((?:' + NUM + r' ){' + str(n) + r'})'
        m = re.search(pat, flat)
        out[lab] = m.group(1).split() if m else None
    return out
if __name__ == '__main__':
    labs = ['Net revenues', 'Gross margin', 'Gross profit', 'Operating income', 'Earnings before income taxes',
            'Net earnings', 'Operating margin', 'Shareholders’ equity', 'Stockholders’ equity',
            'Comparable brand revenue', 'Comparable store sales', 'Number of stores at year-end', 'Store count',
            'Leased square footage', 'Gross leasable area', 'Direct-to-customer', 'E-commerce', 'Selling, general']
    for fy in [int(a) for a in sys.argv[1:]]:
        r = rows(fy, labs)
        print('FY', fy)
        for k, v in r.items():
            if v: print('   ', k, v)
