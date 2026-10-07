# Parse the filed Consolidated Statements of Cash Flows, each 10-K's three columns, for the owner-earnings lines.
import re, json
NUM = r'\(?\s*-?[0-9][0-9,]*\s*\)?'
LINES = {
    'ocf': r'Net cash provided by (?:\(used in\) )?operating activities',
    'sbc': r'Stock-based compensation(?: expense)?',
    'da': r'Depreciation and amortization',
    'capex': r'Purchases? of property and equipment',
    'ni': r'Net earnings',
    'acq': r'Acquisition of [^|]{0,60}',
}
def val(t):
    t = t.replace(' ', '').replace(',', '')
    neg = t.startswith('(')
    t = t.strip('()')
    return -float(t) if neg else float(t)
def parse(fy):
    fn = f'tenk_FY{fy}.txt' if fy != 2025 else 'tenk_FY2025_wsm-20260201.htm.txt'
    t = open(fn, encoding='utf-8').read()
    # the statement itself: the occurrence of the heading followed within 400 chars by "operating activities"
    starts = [m.start() for m in re.finditer(r'(?i)CONSOLIDATED STATEMENTS OF CASH FLOWS', t)]
    seg = None
    for s in starts:
        if re.search(r'(?i)Cash flows from operating activities', t[s:s + 1500]):
            seg = t[s:s + 12000]; break
    flat = re.sub(r'[|$\s]+', ' ', seg)
    out = {}
    for k, pat in LINES.items():
        m = re.search(pat + r'[^0-9(]{0,40}((?:' + NUM + r' ){3})', flat + ' ')
        out[k] = [val(x) for x in re.findall(NUM, m.group(1))] if m else None
    unit = 'thousands'
    return out, unit
if __name__ == '__main__':
    res = {}
    for fy in range(2006, 2026):
        try:
            o, u = parse(fy); res[fy] = o
            print(fy, {k: v for k, v in o.items()})
        except Exception as e:
            print(fy, 'ERR', e)
    json.dump(res, open('cf_parsed.json', 'w'), indent=0)
