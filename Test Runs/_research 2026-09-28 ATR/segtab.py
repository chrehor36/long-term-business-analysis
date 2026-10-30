import re, sys
sys.stdout.reconfigure(encoding='utf-8')
# From segx_out.txt, pull the three-year rows as filed for each segment under each block heading.
txt = open('segx_out.txt', encoding='utf-8').read()
blocks = re.split(r'===== (\d{4}) line \d+\n', txt)[1:]
NUM = r'\(?\$?\s?-?[\d,]+\s?\)?|—'
def rows(block, head, seg):
    i = block.find(head)
    if i < 0: return None
    j = block.find(seg, i)
    if j < 0 or j - i > 900: return None
    m = re.match(r'\s*\$?\s*(' + NUM + r')\s+\$?\s*(' + NUM + r')\s+\$?\s*(' + NUM + r')', block[j + len(seg):])
    if not m: return None
    def v(x):
        x = x.replace('$', '').replace(',', '').replace(' ', '')
        if x == '—': return 0.0
        neg = x.startswith('(')
        x = x.strip('()')
        return -float(x) if neg else float(x)
    return [v(m.group(k)) for k in (1, 2, 3)]
out = {}
for k in range(0, len(blocks), 2):
    yr, b = blocks[k], blocks[k + 1]
    segs = ['Pharma', 'Beauty + Home', 'Beauty & Home', 'Beauty', 'Closures', 'Food + Beverage']
    for head in ['Net Sales:', 'Segment Income:', 'Adjusted EBITDA', 'Depreciation and Amortization:', 'Total Assets:', 'Capital Expenditures:']:
        for sg in segs:
            r = rows(b, head, sg + ' ')
            if r: print(yr, head, sg, r)
    print()
