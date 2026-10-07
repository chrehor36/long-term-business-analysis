import re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
# From every 10-K, read the filed statements (current-year column = first number on the line).
LABELS = {
 'net_sales': r'^\s*Net Sales\s*\|',
 'op_income': r'^\s*Operating Income\s*\|',
 'net_income': r'^\s*Net income\s*\|',
 'depreciation': r'^\s*Depreciation\s*\|',
 'amortization': r'^\s*Amortization\s*\|',
 'dep_amort': r'^\s*Depreciation and amortization\s*\|',
 'sbc': r'^\s*(Stock-based compensation|Stock based compensation|Stock option based compensation|Share-based compensation)\s*\|',
 'ocf': r'^\s*Net Cash Provided by Operations\s*\|',
 'capex': r'^\s*Capital expenditures\s*\|',
 'acq': r'^\s*(Acquisition of business|Acquisition of businesses|Acquisitions? of business).*\|',
 'buyback': r'^\s*Purchase of treasury stock\s*\|',
 'dividends': r'^\s*Dividends paid\s*\|',
 'options': r'^\s*Proceeds from stock option exercises\s*\|',
}
def num(s):
    s = s.replace(',', '').replace('$', '').strip()
    m = re.match(r'^\(?\s*(-?[\d.]+)\s*\)?$', s)
    if not m: return None
    v = float(m.group(1));
    return -v if '(' in s else v
def first_nums(line):
    cells = [c.strip() for c in line.split('|')[1:]]
    out = []
    for c in cells:
        if c in ('', '$', '—', '-'):
            if c in ('—', '-'): out.append(0.0)
            continue
        v = num(c)
        if v is not None: out.append(v)
    return out
res = {}
for p in sorted(glob.glob('cache/k_*.txt')):
    yr = p.split('_')[1][:4]
    L = open(p, encoding='utf-8').read().split('\n')
    # join label line with following numbers when the label wrapped
    L2 = []
    for i, l in enumerate(L):
        L2.append(l)
    row = {}
    # cash-flow statement region: after the LAST heading
    cfi = [i for i, l in enumerate(L2) if re.search(r'STATEMENTS? OF CASH FLOWS', l)]
    isi = [i for i, l in enumerate(L2) if re.search(r'STATEMENTS? OF INCOME', l)]
    for k, pat in LABELS.items():
        rx = re.compile(pat, re.I)
        region = range(cfi[-1], min(cfi[-1] + 120, len(L2))) if k not in ('net_sales', 'op_income') else range(isi[-1] if isi else 0, len(L2))
        for i in region:
            if rx.search(L2[i]):
                n = first_nums(L2[i])
                if n:
                    row[k] = n[:3]; break
    res[yr] = row
    print(yr, {k: v for k, v in row.items()})
