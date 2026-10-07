import re, sys
sys.stdout.reconfigure(encoding='utf-8')
R = 'Test Runs/_research 2026-09-28 TXRH/'
def entries(L):
    h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
    assert len(h) == 1, h
    w = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(w) == 1, w
    sl = L[h[0] + 1:w[0]]
    return h[0], [l for l in sl if re.match(r'^- \*\*[A-Z0-9.\-]+ \(', l)]
# 1. register entry, by line, heading matched line-exactly and asserted unique
P = 'Screens/WATCHLIST RUN QUEUE.md'
raw = open(P, 'rb').read(); crlf = b'\r\n' in raw; sep = '\r\n' if crlf else '\n'
L = raw.decode('utf-8').split(sep)
h, e = entries(L)
before = len(e)
assert e[0].startswith('- **OPXS '), e[0][:40]
assert not any(x.startswith('- **TXRH ') for x in e)
N = before + 1
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n')
entry = entry.replace('__N__', str(N)).replace('__B__', str(before)).replace('__H__', str(h + 1))
L = L[:h + 1] + entry.split('\n') + L[h + 1:]
out = sep.join(L); open(P, 'wb').write(out.encode('utf-8'))
L2 = out.split(sep); h2, e2 = entries(L2)
print('register crlf', crlf, 'heading line', h2 + 1, 'before', before, 'after', len(e2), 'first', e2[0][:30], 'second', e2[1][:30],
      'TXRH count', sum(1 for x in e2 if x.startswith('- **TXRH ')))
def append(path, text):
    raw = open(path, 'rb').read(); crlf = b'\r\n' in raw
    t = text.replace('\r\n', '\n')
    if crlf: t = t.replace('\n', '\r\n')
    nl = b'\r\n' if crlf else b'\n'
    if not raw.endswith(nl): raw += nl
    open(path, 'wb').write(raw + t.encode('utf-8'))
    return crlf
# 3. narrative fold
rl = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
print('reading list crlf', append(rl, open(R + 'fold_note.md', encoding='utf-8').read().replace('__N__', str(N))))
# survival shapes: count the table first
sp = 'Screens/SURVIVAL SHAPES - index.md'
s = open(sp, encoding='utf-8').read()
rows = re.findall(r'(?m)^\| (\d+) \|', s); n = len(rows); mx = max(map(int, rows))
note = f"""
*Dated note, 2026-09-28 (the TXRH fold, wave 7 name 93): **no row was added, no number moved, and the count of distinct shapes is unchanged at 25.** The table was counted with a line-start regex immediately before writing: **{n} rows, maximum number {mx}**. Texas Roadhouse closed at **Q2 OUT**, so Q4 was never opened and this business has no named death. The run file names **#11 THE PASS-THROUGH** as a signature WITHOUT a verdict: the company survives and grows, and the gain of its execution goes to the guest as a per person check that rose less than the category's prices (FY2014-19 and FY2022-25), while beef, bought from four packers, sets half of food cost; the owner's operating margin has sat at 7.6-9.6% since 2009. **It is not entered in #11's instances column**, for the reason the PAGP and CALM folds gave: a Q2 observation is not a Q4 instance.*
"""
print('shapes crlf', append(sp, note), n, mx)
# done file
df = 'Screens/_daily/_wave7_done.txt'
raw = open(df, 'rb').read(); crlf = b'\r\n' in raw; nl = b'\r\n' if crlf else b'\n'
if not raw.endswith(nl): raw += nl
open(df, 'wb').write(raw + b'TXRH' + nl)
D = [l for l in open(df, encoding='utf-8').read().splitlines() if l.strip()]
O = [l for l in open('Screens/_daily/_wave7_order.txt', encoding='utf-8').read().splitlines() if l.strip()]
print('done lines', len(D), 'last', D[-1], 'dupes', len(D) - len(set(D)), 'order', len(O), 'done == order prefix', D == O[:len(D)], 'next', O[len(D)])
