"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
directly before an id (within the same sentence, "..." **[ID]**) appears in that row's verbatim quote."""
import csv, re, sys, os
root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
run = os.path.join(root, 'Test Runs', '2026-10-16 Run - LZRFY Localiza Rent a Car.md')
led = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(root, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}
text = open(run, encoding='utf-8').read()
flat = re.sub(r'\s*\n\s*', ' ', text)
bad = 0
for e in re.findall(r'\[(E\d+-\d+)\]', flat):
    print('E-id found:', e); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat)
for i in sorted(set(ids)):
    if i not in led: print('MISSING id', i); bad += 1
norm = lambda s: re.sub(r'\s+', ' ', s.replace('""', '"')).strip()
# quoted fragment immediately followed (allowing punctuation/space) by an id
for m in re.finditer(r'"([^"]{6,400}?)"[\s.,;:)]*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2)
    if i in led and norm(frag) not in norm(led[i]):
        print('FRAGMENT NOT IN ROW', i, '::', frag[:120]); bad += 1
print('ids:', len(set(ids)), 'checked; problems:', bad)
sys.exit(1 if bad else 0)
