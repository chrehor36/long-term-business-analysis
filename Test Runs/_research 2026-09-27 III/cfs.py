import re, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
keys = [r'^ *Net (income|loss|\(loss\) income|income \(loss\))\|', r'Depreciation', r'Amortization of intangible', r'mpairment', r'(Stock|Share)-based compensation\|',
        r'Net cash (provided by|used in|\(used in\) provided by|provided by \(used in\)) operating', r'Purchase[s]? of (furniture|property)', r'[Cc]apitaliz', r'[Aa]cquisition', r'[Ss]oftware',
        r'Accounts payable\|', r'Accrued expenses', r'Accounts receivable', r'Contract liabilities\|', r'[Dd]ivestiture', r'[Cc]ontingent consideration', r'[Ff]inance lease', r'[Cc]apital lease', r'Treasury shares|repurchase', r'[Dd]ividends paid', r'Proceeds from issuance', r'tax withholding', r'Taxes, net|Income taxes paid|Cash paid for taxes|Taxes\|']
out = open('cfs_blocks.txt', 'w', encoding='utf-8')
for f in sorted(glob.glob('flat/*_10-K_*.txt')):
    s = open(f, encoding='utf-8').read().split('\n')
    # locate the cash-flow statement: the line 'Cash flows from operating activities' nearest after a CASH FLOWS heading
    idx = [i for i, l in enumerate(s) if re.search(r'Cash flows from operating activities', l, re.I)]
    if not idx:
        out.write(f'== {f} NO CFS FOUND\n'); continue
    # pick the one whose block contains 'Net cash' within 60 lines and appears after 'CONSOLIDATED STATEMENT'
    best = None
    for i in idx:
        blk = s[max(0, i - 6):i + 90]
        if any(re.search(r'Net cash', l) for l in blk) and any(re.search(r'CASH FLOWS', l, re.I) for l in s[max(0, i - 8):i + 1]):
            best = i; break
    if best is None: best = idx[-1]
    out.write(f'== {f}\n')
    for l in s[max(0, best - 4):best + 95]:
        if any(re.search(k, l) for k in keys) or re.search(r'Years? Ended|20\d\d\| *20\d\d', l):
            out.write('   ' + l.strip()[:260] + '\n')
out.close()
print(open('cfs_blocks.txt', encoding='utf-8').read()[:200])
