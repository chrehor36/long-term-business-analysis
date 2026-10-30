"""JKHY fold: register entry (line-exact heading, counted before and after), reading-list fold, survival-shape #11
instance, alert bands, PORTFOLIO row, wave 7 done file. Run from the repository root."""
import re, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
R = 'Test Runs/_research 2026-09-27 JKHY/'

# 1. register
P = 'Screens/WATCHLIST RUN QUEUE.md'
raw = open(P, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl)
H = [i for i, x in enumerate(L) if x == '## COMPLETED FROM THE QUEUE']
W = [i for i, x in enumerate(L) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(H) == 1 and len(W) == 1 and H[0] < W[0], (H, W)
def count(lines, h, w):
    ent = [x for x in lines[h + 1:w] if re.match(r'^- \*\*', x)]
    return len(ent), len([x for x in ent if x.startswith('- **JKHY (')]), ent[0][:40] if ent else None
before = count(L, H[0], W[0]); print('register before', before)
assert before[1] == 0, 'JKHY already entered'
entry = open(R + 'register_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
entry = [e.replace('@@N@@', str(before[0] + 1)).replace('@@B@@', str(before[0])) for e in entry]
L2 = L[:H[0] + 1] + entry + L[H[0] + 1:]
H2 = [i for i, x in enumerate(L2) if x == '## COMPLETED FROM THE QUEUE']
W2 = [i for i, x in enumerate(L2) if x.startswith('## THE WRITE-EARLY PROTOCOL')]
after = count(L2, H2[0], W2[0]); print('register after', after)
assert after[0] == before[0] + 1 and after[1] == 1 and after[2].startswith('- **JKHY (')
open(P, 'w', encoding='utf-8', newline='').write(nl.join(L2))
N = after[0]

# 2. reading list
P = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
raw = open(P, encoding='utf-8', newline='').read()
nl2 = '\r\n' if '\r\n' in raw else '\n'
assert raw.rstrip().endswith('**Next in the order file: JKHY.**'), raw[-80:]
note = open(R + 'fold_note.md', encoding='utf-8').read().replace('@@N@@', str(N)).rstrip('\n')
raw = raw.rstrip('\r\n') + nl2 + nl2 + note.replace('\n', nl2) + nl2
open(P, 'w', encoding='utf-8', newline='').write(raw)
print('reading list folded')

# 3. survival shapes #11 instance
P = 'Screens/SURVIVAL SHAPES - index.md'
raw = open(P, encoding='utf-8', newline='').read()
nl3 = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl3)
k = [i for i, x in enumerate(L) if x.startswith('| 11 | **The pass-through**')]
assert len(k) == 1
assert 'JKHY (2026-09-27' not in L[k[0]]
inst = (", **JKHY (2026-09-27, the mechanism at an OPENED Q4, all four business gates IN and Q5 quit on at price: a switching-cost "
        "moat without demonstrated pricing power, where the renewal of a six-year core contract, a client's acquisition by a bank on "
        "another core, or the company's own move to a public-cloud core is the moment the client re-chooses; the filer's own "
        "\"Certain of our renewals have resulted in price compression\" (first in FY2025) and \"upfront incentive payments or credits\" "
        "($108.3M FY2023 to $178.5M FY2026, +65% against revenue +22%), while owner earnings grew 3.2% a year five-year to five-year "
        "against revenue at 7.5%; the re-platforming recorded as an exposure inside #11, not a new shape; a real possibility for the "
        "return, a low-level possibility for the company, debt $40M and interest covered about 94x)**")
row = L[k[0]].rstrip()
assert row.endswith('|')
L[k[0]] = row[:-1].rstrip() + inst + ' |'
open(P, 'w', encoding='utf-8', newline='').write(nl3.join(L))
print('survival shape #11 instance added')

# 4. alerts
P = 'tools/alerts.json'
d = json.load(open(P, encoding='utf-8'))
ids = {a['id'] for a in d['alerts']}
assert 'JKHY-floor-band' not in ids
d['alerts'].append({"id": "JKHY-floor-band", "ticker": "JKHY", "currency": "USD", "op": "<=", "threshold": 81.30, "active": True,
  "label": "JKHY at/below $81.30: the E4-28 floor is met at g = 3.2% (five-year owner earnings 2016-20 to 2021-25, capex end; revenue 7.5% a year FY2009-2026 but owner earnings slower) on the three-year capex-end owner earnings of $387.6M and 70,112,608 cover shares. Q1-Q4 all IN on 2026-09-27 (Q2 NARROW, flat to narrowing); Q5 quit on at $147.79 (yield 3.74-4.21% against a 5.49% sovereign, expectancy 6.9-9.2%). Prompt for a FULL v4.1 re-run, not a purchase, sized DOWN if it clears (capital-allocation flag live: FY2026 buybacks at an average $152, above the run's $80-$125 range). VOID if any Q2 falsifier has fired: contract assets (client incentives) above 8% of revenue or growing faster than revenue in both FY2027 and FY2028; core banks below 20% or core credit unions below 15% of the filer's market count, or both shares falling two 10-Ks running; pre-tax return on operating capital ex goodwill below 30% for two years; GAAP operating margin below 21%. Source: Test Runs/2026-09-27 Run - JKHY Jack Henry.md."})
d['alerts'].append({"id": "JKHY-rerun-band", "ticker": "JKHY", "currency": "USD", "op": "<=", "threshold": 124.43, "active": True,
  "label": "JKHY at/below $124.43: the E4-28 floor is met only if E4-44's 5% ceiling on perpetual growth is granted on the three-year D&A-end owner earnings ($436.2M), above the latest five-year owner-earnings rate (3.2%). Prompt for a FULL v4.1 re-run in which the growth and the (c) end are re-tested before either is spent; re-derive both JKHY bands on the FY2027 10-K (about late August 2027). VOID if any Q2 falsifier in JKHY-floor-band has fired."})
raw = json.dumps(d, indent=1, ensure_ascii=False)
open(P, 'w', encoding='utf-8', newline='\n').write(raw + '\n')
print('alerts added', len(d['alerts']))

# 5. PORTFOLIO row after UNP
P = 'PORTFOLIO.md'
raw = open(P, encoding='utf-8', newline='').read()
nl5 = '\r\n' if '\r\n' in raw else '\n'
L = raw.split(nl5)
u = [i for i, x in enumerate(L) if x.startswith('| — | UNP |')]
assert len(u) == 1 and not any(x.startswith('| - | JKHY |') or x.startswith('| — | JKHY |') for x in L)
prow = open(R + 'portfolio_row.md', encoding='utf-8').read().strip()
L.insert(u[0] + 1, prow)
open(P, 'w', encoding='utf-8', newline='').write(nl5.join(L))
print('PORTFOLIO row added after line', u[0] + 1)

# 6. done file
P = 'Screens/_daily/_wave7_done.txt'
raw = open(P, encoding='utf-8', newline='').read()
lines = [x for x in raw.splitlines() if x.strip()]
assert 'JKHY' not in lines
nl6 = '\r\n' if '\r\n' in raw else '\n'
raw = raw if raw.endswith(('\n', '\r\n')) else raw + nl6
open(P, 'w', encoding='utf-8', newline='').write(raw + 'JKHY' + nl6)
print('done file now', len(lines) + 1, 'lines')
