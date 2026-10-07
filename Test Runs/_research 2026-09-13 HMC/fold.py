import re
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
Q = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
RL = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
HERE = ROOT + r"\Test Runs\_research 2026-09-13 HMC"
pat = re.compile(r'^- \*\*([A-Z][A-Z.\-]*) \(')
def count(lines):
    last = max(i for i, l in enumerate(lines) if l.startswith('## COMPLETED FROM THE QUEUE'))
    ents = [l for l in lines[last+1:] if pat.match(l)]
    return last, len(ents), ents
q = open(Q, encoding='utf-8').read()
lines = q.split('\n')
last, before, entries_before = count(lines)
assert not any(l.startswith('- **HMC (') for l in entries_before), 'HMC already in register'
entry = open(HERE + r"\fold_entry.md", encoding='utf-8').read().rstrip('\n').split('\n')
lines[last+1:last+1] = entry
wi = [i for i, l in enumerate(lines) if l.startswith('| foreign 20-F filers, short XBRL history |')]
assert len(wi) == 1, wi
row = lines[wi[0]]
assert ', HMC,' in row, row
lines[wi[0]] = row.replace(', HMC,', ', ~~HMC~~,')
open(Q, 'w', encoding='utf-8').write('\n'.join(lines))
chk = open(Q, encoding='utf-8').read().split('\n')
_, after, entries_after = count(chk)
lost = set(entries_before) - set(entries_after)
print('register before', before, 'after', after, 'lost', len(lost))
assert after == before + 1 and not lost
print('wave5 row:', chk[[i for i, l in enumerate(chk) if l.startswith('| foreign 20-F filers')][0]])
tick = [pat.match(l).group(1) for l in entries_after]
# categories from the register's own headline lines
cats = {'Q5': 0, 'Q2': 0, 'Q4': 0, 'Q1': 0, '?': 0}
text = '\n'.join(chk[max(i for i, l in enumerate(chk) if l.startswith('## COMPLETED FROM THE QUEUE'))+1:])
blocks = re.split(r'\n(?=- \*\*[A-Z][A-Z.\-]* \()', '\n' + text)
new_since_tm = []
for b in blocks:
    m = pat.match(b.strip('\n'))
    if not m: continue
    if m.group(1) in ('HMC',): continue
for t_ in tick:
    pass
others = [t_ for t_ in tick[:tick.index('HMC')]] if 'HMC' in tick else []
print('entries above HMC (newer):', others)
if after == 85:
    cnt = ("85 runs** - gate-clearers 26, **Q2 OUT 55**, Q4 OUT 2, Q1 UNKNOWABLE 2 (HHH, RGTI). *(Counted from the register at the fold: "
           "84 after TM, plus HMC.)*")
else:
    cnt = (f"{after} runs by the register at the fold** (84 after TM, plus HMC and {after-85} other WAVE 5 entr{'y' if after-85==1 else 'ies'} "
           "folded concurrently, whose categories stand as their own folds state; HMC adds one Q2 OUT).")
narr = open(HERE + r"\fold_narrative.md", encoding='utf-8').read().replace('@@COUNT@@', cnt)
rl = open(RL, encoding='utf-8').read()
assert 'UPDATE 2026-09-13 - HMC' not in rl
if not rl.endswith('\n'): rl += '\n'
open(RL, 'w', encoding='utf-8').write(rl + narr)
print('reading list appended; count:', cnt[:90])
