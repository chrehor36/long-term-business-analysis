import re, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
txt = open('cfs_blocks.txt', encoding='utf-8').read()
blocks = re.split(r'\n== ', '\n' + txt)
PAT = {
 'ni': r'^Net income',
 'dep': r'^Depreciation',
 'amort_int': r'^Amortization of intangibles',
 'amort_mixed': r'^Amortization of restricted common stock|^Stock-based compensation and amortization',
 'sbc_opt': r'^Amortization of stock (options|appreciation)|^Stock-based compensation\b|^Share-based compensation\b',
 'sbc_other': r'^Other share-based compensation',
 'sbc_treas': r'^Treasury shares contributed',
 'gw_imp': r'^Goodwill impairment|^Impairment',
 'ocf': r'^(NET CASH PROVIDED BY OPERATING|Net Cash provided by Operating|Cash provided by Operating)',
 'capex': r'^(Property purchases|Capital expenditures)',
 'prop_sales': r'^Proceeds from property sales',
 'acq': r'^Net cash paid for acquisition|^Cash paid for acquisition',
 'buyback': r'^Purchases of treasury shares',
 'div': r'^Dividends paid',
 'withheld': r'^Taxes paid for shares withheld',
 'ar': r'^Accounts receivable',
 'inv': r'^Inventories',
 'ap': r'^Accounts payable',
 'taxpaid': r'^Income taxes\b',
 'interest': r'^Interest\b',
}
def nums(s):
    s = s.replace('|', ' ')
    s = re.sub(r'\(\s*([\d,\.]+)\s*\)?', r'(\1)', s)
    s = s.replace('—', ' 0 ')
    toks = re.findall(r'\(?\$?\s?[\d][\d,]*\)?', s)
    out = []
    for t in toks:
        neg = t.startswith('(')
        v = re.sub(r'[^\d]', '', t)
        if v == '': continue
        out.append(-int(v) if neg else int(v))
    return out
res = {}
for b in blocks[1:]:
    lines = b.split('\n')
    name = lines[0].strip()
    if 'NO CFS' in name: continue
    fdate = name.replace(chr(92), '/').split('/')[-1][:10]
    years = None
    for l in lines[1:12]:
        m = re.findall(r'\b(19\d\d|20\d\d)\b', l)
        if len(m) >= 3: years = [int(x) for x in m[:3]]; break
    if not years: print('noyears', name); continue
    # join continuation label lines: if a line has no numbers and the next has numbers, merge
    merged = []
    buf = ''
    for l in lines[1:]:
        l = l.strip()
        if not l or not l.strip('-=| '): continue
        if l.rstrip('| ').endswith(':'): buf = ''; continue
        lab = re.sub(r'\|', '', l)
        has = len(nums(re.sub(r'\$\d[\d,]*', '', lab))) > 0
        if not has and not re.search(r'Cash Flows|CASH FLOWS', l):
            buf = (buf + ' ' + lab).strip(); continue
        merged.append((buf + ' ' + lab).strip() if buf else lab); buf = ''
    rec = {}
    for l in merged:
        label = re.split(r'[\(\$\d]', l, 1)[0].strip()
        for k, p in PAT.items():
            if re.search(p, l, re.I) and k not in rec:
                body = re.sub(r'acquired of \$[\d,]+( and \$[\d,]+)?( in \d{4}( and \d{4})?)?(, respectively)?', '', l)
                body = re.sub(r'of \$[\d,]+ (and \$[\d,]+ )?in \d{4}', '', body)
                v = nums(body)
                rec[k] = v
                break
    res[name] = {'fdate': fdate, 'years': years, 'rec': rec}
json.dump(res, open('cfs_parsed.json', 'w'), indent=0)
for n, r in res.items():
    print(r['fdate'], r['years'], {k: v for k, v in r['rec'].items() if len(v) != 3})
