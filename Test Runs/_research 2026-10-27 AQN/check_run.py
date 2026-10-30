# Citation check for the AQN run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment attached to an id is a substring of that row's quote (whitespace-normalised, [...] splits).
# A quote is attached to an id when it opens within 4 characters after the id inside "(" (the id ("...") form),
# otherwise to the first id that follows it within 45 characters (the "..." **[id]** form).
import csv, re, sys
LED = 'C:/Projects/BRK/principle_ledger_v5.csv'
RUN = 'C:/Projects/BRK/Test Runs/2026-10-27 Run - AQN Algonquin Power & Utilities.md'
rows = {x[0].lstrip('\ufeff'): ' '.join(x[2].split()) for x in csv.reader(open(LED, encoding='utf-8'))}
t = open(RUN, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', t)
if eids: print('E-ids found:', eids); bad += 1
idre = re.compile(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
ids = idre.findall(t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
quotes = [(q.start(), q.end(), q.group(1)) for q in re.finditer(r'"([^"\n]{6,}(?:\n[^"\n]*){0,3})"', t)]
idpos = [(m.start(), m.end(), m.group(1)) for m in idre.finditer(t)]
pairs = []
for qs, qe, qt in quotes:
    after = [i for i in idpos if 0 <= qs - i[1] <= 4 and t[i[1]:qs].strip() in ('(', '')]
    if after:
        # chained ("..."; "...") after one id
        pairs.append((after[-1][2], qt)); continue
    nxt = [i for i in idpos if 0 <= i[0] - qe <= 45]
    if nxt: pairs.append((nxt[0][2], qt))
for i, qt in pairs:
    row = rows.get(i, '')
    for p in qt.split('[...]'):
        p = ' '.join(p.split()).strip(' .,;:')
        if p and p not in row:
            print(f'FRAGMENT NOT IN ROW {i}: "{p}"'); bad += 1
# chained second quotes inside one parenthesis after an id: ("a"; "b")
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\* \(("[^)]*")\)', t):
    for q in re.findall(r'"([^"]+)"', m.group(2))[1:]:
        p = ' '.join(q.split()).strip(' .,;:')
        if p not in rows.get(m.group(1), ''):
            print(f'CHAINED FRAGMENT NOT IN ROW {m.group(1)}: "{p}"'); bad += 1
print('ids cited:', len(set(ids)), 'quote-id pairs checked:', len(pairs), 'checks failed:', bad)
sys.exit(1 if bad else 0)
