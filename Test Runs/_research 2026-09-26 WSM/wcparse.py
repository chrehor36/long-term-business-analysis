# Sum the working-capital lines of the filed cash-flow statements (the "Changes in" block), excluding the
# operating-lease-liability line (rent paid, paired with the non-cash lease expense add-back; not working capital).
import re, json
NUM = r'\(?\s*-?[0-9][0-9,]*\s*\)?'
def val(t):
    t = t.replace(' ', '').replace(',', ''); neg = t.startswith('(')
    t = t.strip('()'); return -float(t) if neg else float(t)
WC = [r'Accounts receivable', r'Merchandise inventories', r'Prepaid (?:catalog expenses|expenses)(?: and other assets)?',
      r'Other (?:current )?assets', r'Accounts payable', r'Accrued (?:salaries, benefits and other|expenses and other liabilities)',
      r'Customer deposits', r'Gift card and other deferred revenue', r'Deferred rent and lease incentives',
      r'Income taxes payable', r'Other (?:long-term )?liabilities']
def parse(fy):
    fn = f'tenk_FY{fy}.txt' if fy != 2025 else 'tenk_FY2025_wsm-20260201.htm.txt'
    t = open(fn, encoding='utf-8').read()
    for m in re.finditer(r'(?i)CONSOLIDATED STATEMENTS OF CASH FLOWS', t):
        if re.search(r'(?i)Cash flows from operating activities', t[m.start():m.start() + 1500]):
            seg = t[m.start():m.start() + 12000]; break
    flat = re.sub(r'[|$\s]+', ' ', seg)
    a = flat.index('Changes in'); b = flat.index('Net cash provided by', a)
    block = flat[a:b]
    found = {}
    for pat in WC:
        for mm in re.finditer('(' + pat + r')[^0-9(]{0,30}((?:' + NUM + r' ){3})', block + ' '):
            found[mm.group(1)] = [val(x) for x in re.findall(NUM, mm.group(2))]
    tot = [sum(v[i] for v in found.values()) for i in range(3)]
    return found, tot
if __name__ == '__main__':
    res = {}
    for fy in range(2008, 2026):
        f, tot = parse(fy); res[fy] = tot
        print(fy, [round(x / 1e3, 1) for x in tot], sorted(f))
    json.dump(res, open('wc_parsed.json', 'w'))
