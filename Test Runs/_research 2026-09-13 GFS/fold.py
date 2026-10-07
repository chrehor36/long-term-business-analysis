import re
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
Q = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
RL = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
HERE = ROOT + r"\Test Runs\_research 2026-09-13 GFS"
pat = re.compile(r'^- \*\*([A-Z][A-Z.\-]*) \(')
def count(lines):
    last = max(i for i, l in enumerate(lines) if l.startswith('## COMPLETED FROM THE QUEUE'))
    ents = [l for l in lines[last+1:] if pat.match(l)]
    return last, len(ents), ents
# ONE read-modify-write of the queue file, immediately before the commit
q = open(Q, encoding='utf-8').read()
lines = q.split('\n')
last, before, entries_before = count(lines)
assert not any(l.startswith('- **GFS (') for l in entries_before), 'GFS already in register'
entry = open(HERE + r"\fold_entry.md", encoding='utf-8').read().replace('@@COMMITS@@', 'Step 0 `d2c6ae3`, Q1 `c7eee7e`, Q2 `a29fd2d`, Q3-Q6 and audit `07597ba`').rstrip('\n').split('\n')
assert not any('@@' in l for l in entry)
lines[last+1:last+1] = entry
wi = [i for i, l in enumerate(lines) if l.startswith('| foreign 20-F filers, short XBRL history |')]
assert len(wi) == 1, wi
row = lines[wi[0]]
assert ', GFS,' in row, row
lines[wi[0]] = row.replace(', GFS,', ', ~~GFS~~,')
open(Q, 'w', encoding='utf-8').write('\n'.join(lines))
chk = open(Q, encoding='utf-8').read().split('\n')
_, after, entries_after = count(chk)
lost = set(entries_before) - set(entries_after)
print('register before', before, 'after', after, 'lost', len(lost))
assert after == before + 1 and not lost
print('wave5 row:', [l for l in chk if l.startswith('| foreign 20-F filers')][0])
ticks = [pat.match(l).group(1) for l in entries_after]
print('top entries:', ticks[:6])
others = ticks[:ticks.index('GFS')]
cnt = (f"**Register count at the fold, read from the register: {after} runs** (GFS adds one Q2 OUT"
       + (f"; entries above it folded concurrently: {', '.join(others)}" if others else "") + ").")
narr = open(HERE + r"\fold_narrative.md", encoding='utf-8').read().replace('@@COUNT@@', cnt)
assert '@@' not in narr
rl = open(RL, encoding='utf-8').read()
assert 'UPDATE 2026-09-13 - GFS' not in rl
if not rl.endswith('\n'): rl += '\n'
open(RL, 'w', encoding='utf-8').write(rl + narr)
print('reading list appended;', cnt)
