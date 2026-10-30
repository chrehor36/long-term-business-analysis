import re, json
ROOT = '../../'
# 1. register entry, by line, line-exact heading asserted unique
p = ROOT + 'Screens/WATCHLIST RUN QUEUE.md'
b = open(p, 'rb').read(); assert b.count(b'\r\n') == b.count(b'\n')
L = b.decode('utf-8').split('\r\n')
def count(L):
    h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
    w = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(h) == 1 and len(w) == 1, (h, w)
    ent = [l for l in L[h[0]+1:w[0]] if re.match(r'^- \*\*[A-Z0-9]', l)]
    return h[0], w[0], ent
h, w, ent = count(L)
print('before: heading line', h+1, 'write-early line', w+1, 'entries', len(ent), 'first', ent[0][:12], 'NDSN', sum(1 for l in ent if l.startswith('- **NDSN')))
assert L[h+1].startswith('- **JJSF') and len(ent) == 217
entry = open('register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h+1] + entry + L[h+1:]
open(p, 'wb').write('\r\n'.join(L).encode('utf-8'))
L = open(p, 'rb').read().decode('utf-8').split('\r\n')
h, w, ent = count(L)
print('after: heading line', h+1, 'write-early line', w+1, 'entries', len(ent), 'first', ent[0][:12], 'second', ent[1][:12], 'NDSN', sum(1 for l in ent if l.startswith('- **NDSN')))
assert len(ent) == 218 and ent[0].startswith('- **NDSN')
# 2. done file
d = ROOT + 'Screens/_daily/_wave7_done.txt'
t = open(d, 'rb').read(); nl = b'\r\n' if b'\r\n' in t else b'\n'
if not t.endswith(nl): t += nl
assert b'NDSN' not in t.split()
open(d, 'wb').write(t + b'NDSN' + nl)
lines = open(d, encoding='utf-8').read().splitlines()
o = open(ROOT + 'Screens/_daily/_wave7_order.txt', encoding='utf-8').read().split()
rem = [x for x in o if x not in set(lines)]
print('done lines', len(lines), 'last', lines[-1], 'NDSN count', lines.count('NDSN'), 'remaining', len(rem), 'next', rem[0])
# 3. reading list, append-only
p2 = ROOT + 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
b = open(p2, 'rb').read(); assert b.endswith(b'\r\n')
note = open('fold_note.md', encoding='utf-8').read().replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8')
open(p2, 'wb').write(b + note)
# 4a. alerts (gate-clearer)
pa = ROOT + 'tools/alerts.json'
a = json.loads(open(pa, 'rb').read())
assert not any(x['ticker'] == 'NDSN' for x in a['alerts'])
a['alerts'].append({"id": "NDSN-floor-band", "ticker": "NDSN", "currency": "USD", "op": "<=", "threshold": 125.02, "active": True,
 "label": "NDSN at/below $125.02: the E4-28 floor is met at g = 2.6% (organic sales FY2016-FY2025; about 3.5% FY2003-FY2025) on the five-year depreciation-end owner earnings of $515.3M and 55,699,366 cover shares. Q1-Q4 all IN on 2026-09-27 (Q2 NARROW); Q5 quit on at $325.77 (yield 2.84-2.88% five-year against a 5.49% sovereign, expectancy 5.4-7.7%). Prompt for a FULL v4.1 re-run, not a purchase, sized DOWN if it clears (capital-allocation flag live: buybacks at $224.80 and $287.34 against the run's values; 82% of 26 years' owner earnings spent on purchases). VOID if any Q2 falsifier has fired: gross margin below 52% two consecutive fiscal years without a quantified one-time cause; the filer reporting price given back two consecutive years; FY2026 organic sales negative (a fourth year running); a further write-down of a purchased business of $100M or more or a purchase exited at a loss; pre-tax return on all operating capital, goodwill and intangibles included, below 12% two consecutive years. Source: Test Runs/2026-09-27 Run - NDSN Nordson.md."})
a['alerts'].append({"id": "NDSN-rerun-band", "ticker": "NDSN", "currency": "USD", "op": "<=", "threshold": 202.93, "active": True,
 "label": "NDSN at/below $202.93: the E4-28 floor is met only if 3.8%/yr (organic FY2003-FY2025 plus the FY2016-FY2025 share-count decline) is granted in perpetuity on the TTM capex-end owner earnings ($700.8M to 2026-07-31). Prompt for a FULL v4.1 re-run in which that rate is re-tested against the then-current organic series before it is spent. Re-derive both NDSN bands on the FY2026 10-K (about mid-December 2026); VOID if any falsifier in NDSN-floor-band has fired."})
open(pa, 'wb').write((json.dumps(a, indent=1, ensure_ascii=False) + '\n').encode('utf-8'))
json.loads(open(pa, 'rb').read()); print('alerts', len(a['alerts']))
# 4b. PORTFOLIO row after JKHY
pp = ROOT + 'PORTFOLIO.md'
b = open(pp, 'rb').read(); assert b.count(b'\r\n') == b.count(b'\n')
P = b.decode('utf-8').split('\r\n')
j = [i for i, l in enumerate(P) if l.startswith('| - | JKHY |')]; assert len(j) == 1
assert not any('| NDSN |' in l for l in P)
row = open('portfolio_row.md', encoding='utf-8').read().strip()
P = P[:j[0]+1] + [row] + P[j[0]+1:]
open(pp, 'wb').write('\r\n'.join(P).encode('utf-8'))
print('portfolio row at line', j[0]+2)
# 4c. survival-shapes index: NDSN into #10's instances column, and a dated note
ps = ROOT + 'Screens/SURVIVAL SHAPES - index.md'
b = open(ps, 'rb').read(); crlf = b'\r\n' in b
sep = '\r\n' if crlf else '\n'
S = b.decode('utf-8').split(sep)
rows = [l for l in S if re.match(r'^\| \d+ \|', l)]
nums = [int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows]
print('shape rows', len(rows), 'max', max(nums))
k = [i for i, l in enumerate(S) if l.startswith('| 10 | **The camouflage**')]; assert len(k) == 1
add = open('index_add.txt', encoding='utf-8').read().strip()
assert S[k[0]].rstrip().endswith('|')
line = S[k[0]].rstrip()
S[k[0]] = line[:-1].rstrip() + ', ' + add + ' |'
note = open('index_note.txt', encoding='utf-8').read().strip() % (len(rows), max(nums))
while S and S[-1] == '': S.pop()
S = S + ['', note, '']
open(ps, 'wb').write(sep.join(S).encode('utf-8'))
print('index updated')
