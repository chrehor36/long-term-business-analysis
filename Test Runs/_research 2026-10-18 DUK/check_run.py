# Checks for the DUK run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment in the span before an id (since the previous id) appears verbatim in one of the ids cited there.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = r'C:/Users/chreh/OneDrive/Documents/BRK/'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ROOT+'principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open(ROOT+'Test Runs/2026-10-18 Run - DUK Duke Energy.md', encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
problems = 0
for e in re.findall(r'\[E\d+-\d+\]', t):
    print('E-id found', e); problems += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); problems += 1
# fragment check: group consecutive ids (separated only by commas/spaces) and check the quote just before the group
pat = re.compile(r'((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:\s*,\s*)?)+)')
last = 0; checked = 0
for m in pat.finditer(t):
    group = re.findall(r'[MLR]\d{4}-\d{3}', m.group(1))
    span = t[last:m.start()]; last = m.end()
    # the quote directly before the id group: from the first '"' after the last sentence break that opens a quote
    q = span.rstrip()
    if not q.endswith('"') and not q.endswith('"' + ','):
        # only check when the text right before the ids closes a quote
        if not re.search(r'"\s*[\.\,;:]?\s*$', q): continue
    k = q.rfind('"'); start = q.rfind(' "', 0, k)
    if start < 0: start = q.rfind('"', 0, k)
    # walk back to the opening quote: allow inner quotes by taking from the earliest ' "' after the previous id in the span
    opens = [mm.start() for mm in re.finditer(r'(^|[\s\(:;])"', q)]
    opens = [o for o in opens if o < k]
    if not opens: continue
    frag = q[opens[-1]:k+1]
    # if the fragment looks too short and there is an earlier opener, the inner quote split it: extend
    for o in reversed(opens[:-1]):
        cand = q[o:k+1]
        if any(norm(p.strip(' "')) in norm(rows.get(g,'')) for g in group for p in [cand]) : frag = cand; break
    pieces = [norm(p.strip(' "“”')) for p in re.split(r'\[\.\.\.\]', frag.strip().strip('"'))]
    pieces = [p for p in pieces if len(p) > 8]
    ok = all(any(p in norm(rows.get(g,'')) for g in group) for p in pieces)
    checked += 1
    if not ok:
        bad = [p for p in pieces if not any(p in norm(rows.get(g,'')) for g in group)]
        print('FRAGMENT not in row', group, '|', bad[:2]); problems += 1
print('ids cited:', len(ids), 'distinct:', len(set(ids)), 'quote groups checked:', checked, 'problems:', problems)
