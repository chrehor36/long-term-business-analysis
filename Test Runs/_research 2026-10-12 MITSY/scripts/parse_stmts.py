"""Parse the page-row extracts of Mitsui's consolidated statements into a year-by-line table (Mn JPY).
Each extract holds two fiscal years (t, t-1); the first two numbers on a labelled line are taken."""
import re, csv, glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
LINES = {  # key: regex on the line start (case-insensitive)
 'cash': r'cash and cash equivalents \(', 'recv_cur': r'trade and other receivables \(notes? 2, 7, 8, 9, ?16 and 21\)|trade and other receivables \(notes? 2, 7, 8, 9, 16, and 21\)',
 'inventories': r'inventories', 'total_current_assets': r'total current assets',
 'equity_method_inv': r'investments accounted for using the equity method \(', 'other_investments': r'other investments \(',
 'ppe': r'property, plant and equipment \(', 'inv_property': r'investment property \(', 'intangibles': r'intangible assets \(',
 'total_assets': r'total assets', 'st_debt': r'short-term debt \(', 'cur_ltd': r'current portion of long-term debt',
 'payables': r'trade and other payables \(', 'ltd': r'long-term debt, less current portion', 'total_liabilities': r'total liabilities \s|total liabilities$',
 'retained': r'retained earnings', 'treasury': r'treasury stock \s|treasury stock$', 'equity_parent': r'total equity attributable to owners of the parent',
 'nci': r'non-controlling interests \(', 'revenue': r'revenue \(', 'gross_profit': r'gross profit',
 'sga': r'selling, general and administrative', 'interest_expense': r'interest expense', 'dividend_income': r'dividend income \s|dividend income$',
 'equity_share': r'^\d[\d,]* \d[\d,]* \d[\d,]*$', 'pbt': r'^\d', 'income_tax': r'^\(', 'net_income': r'owners of the parent \(note',
 'da': r'depreciation and amortization', 'impairment': r'impairment (reversal )?(\(reversal\) )?loss of fixed assets|impairment reversal \(loss\)',
 'chg_recv': r'change in trade and other receivables', 'chg_inv': r'change in inventories', 'chg_pay': r'change in trade and other payables',
 'interest_received': r'interest received', 'interest_paid': r'interest paid', 'dividends_received': r'dividends received',
 'taxes_paid': r'income taxes paid', 'taxes_refunded': r'income taxes refunded', 'cfo': r'cash flows from operating activities',
 'inv_eq_investees': r'investments in equity (accounted|method) investees', 'sale_eq_investees': r'proceeds from sales of investments in equity',
 'purch_other_inv': r'purchases of other investments', 'sale_other_inv': r'proceeds from sales and maturities of other investments',
 'loans_out': r'increases in loan receivables', 'loans_in': r'collections of loan receivables',
 'capex_ppe': r'purchases of property, plant and equipment', 'sale_ppe': r'proceeds from sales of property, plant and equipment',
 'capex_invprop': r'purchases of investment property', 'sale_invprop': r'proceeds from sales of investment property',
 'acq_subs': r'acquisition of subsidiaries', 'sale_subs': r'proceeds from sales of subsidiaries', 'time_dep': r'change in time deposits',
 'cfi': r'cash flows from investing activities', 'lease_repay': r'repayments of lease liabilities', 'buyback': r'purchases and sales of treasury stock',
 'dividends_paid': r'dividends paid', 'nci_tx': r'transactions with non-controlling', 'cff': r'cash flows from financing activities',
}
NUM = re.compile(r'\(?-?[\d,]+\)?')
def nums(s):
    out = []
    for t in NUM.findall(s):
        if not re.search(r'\d', t) or t in (',',): continue
        neg = t.startswith('(') or t.startswith('-')
        v = t.strip('()-').replace(',', '')
        if not v.isdigit(): continue
        out.append(-int(v) if neg else int(v))
    return out
def parse(path):
    lines = [l.strip() for l in open(path, encoding='utf-8', errors='replace')]
    m = re.search(r'fy(\d{4})', path); fy = int(m.group(1))
    res = {fy: {}, fy - 1: {}}
    for i, l in enumerate(lines):
        low = l.lower()
        for k, rx in LINES.items():
            if k in ('equity_share', 'pbt', 'income_tax'): continue
            if k in res[fy]: continue
            if re.match(rx, low):
                n = [x for x in nums(re.sub(r'\((notes?|note) [^)]*\)', '', l)) if abs(x) >= 100 or x == 0]
                if len(n) < 2 and i + 1 < len(lines):  # numbers on the next row
                    n = [x for x in nums(lines[i + 1]) if abs(x) >= 100]
                if len(n) >= 2:
                    res[fy][k], res[fy - 1][k] = n[0], n[1]
        # equity-method share, profit before tax, taxes, profit for year: label row followed by numbers row
        if low.startswith('share of profit (loss) of investments accounted for using') or low.startswith('share of profit (loss) of investments accounted for using the equity method'):
            for j in (i + 1, i + 2):
                n = [x for x in nums(lines[j]) if abs(x) >= 100]
                if len(n) >= 2: res[fy]['equity_share'], res[fy - 1]['equity_share'] = n[0], n[1]; break
        for lab, key in (('profit before income taxes', 'pbt'), ('income taxes (note', 'income_tax'), ('profit for the year', 'profit_year')):
            if low.startswith(lab) and key not in res[fy]:
                n = [x for x in nums(re.sub(r'\((notes?|note) [^)]*\)', '', l)) if abs(x) >= 100]
                if len(n) < 2: n = [x for x in nums(lines[i + 1]) if abs(x) >= 100]
                if len(n) >= 2: res[fy][key], res[fy - 1][key] = n[0], n[1]
    return res
data = {}
for p in sorted(glob.glob(os.path.join(HERE, '..', 'extracts', 'fy*_stmts.txt'))):
    for fy, d in parse(p).items():
        if fy not in data: data[fy] = d
        else:
            for k, v in d.items(): data[fy].setdefault(k, v)
keys = list(LINES) + ['profit_year']
with open(os.path.join(HERE, '..', 'extracts', 'statements_10y.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['line'] + sorted(data))
    for k in keys:
        if k in ('pbt', 'income_tax'): pass
        w.writerow([k] + [data[y].get(k, '') for y in sorted(data)])
print(open(os.path.join(HERE, '..', 'extracts', 'statements_10y.csv')).read())
