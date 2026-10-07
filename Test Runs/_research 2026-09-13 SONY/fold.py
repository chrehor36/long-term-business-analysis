import re, subprocess, sys
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
Q = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
RL = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
HERE = ROOT + r"\Test Runs\_research 2026-09-13 SONY"
pat = re.compile(r'^- \*\*[A-Z][A-Z.\-]* \(')
def count(lines):
    last = max(i for i, l in enumerate(lines) if l.startswith('## COMPLETED FROM THE QUEUE'))
    return last, sum(1 for l in lines[last+1:] if pat.match(l)), [l for l in lines[last+1:] if pat.match(l)]
q = open(Q, encoding='utf-8').read()
lines = q.split('\n')
last, before, entries_before = count(lines)
assert not any(l.startswith('- **SONY (') for l in entries_before), 'SONY already in register'
entry = open(HERE + r"\fold_entry.md", encoding='utf-8').read().rstrip('\n').split('\n')
lines[last+1:last+1] = entry
# strike SONY in WAVE 5 table row
wi = [i for i, l in enumerate(lines) if l.startswith('| foreign 20-F filers, short XBRL history |')]
assert len(wi) == 1, wi
row = lines[wi[0]]
assert ', SONY,' in row or '~~SONY~~' in row, row
lines[wi[0]] = row.replace(', SONY,', ', ~~SONY~~,')
new = '\n'.join(lines)
open(Q, 'w', encoding='utf-8').write(new)
chk = open(Q, encoding='utf-8').read().split('\n')
_, after, entries_after = count(chk)
lost = set(entries_before) - set(entries_after)
print('register before', before, 'after', after, 'lost', len(lost))
assert after == before + 1 and not lost
print('wave5 row:', chk[[i for i,l in enumerate(chk) if l.startswith('| foreign 20-F filers')][0]])
# narrative
tickers = [re.match(r'^- \*\*([A-Z][A-Z.\-]*) \(', l).group(1) for l in entries_after]
if after == 83:
    cnt = ("83 runs** - gate-clearers 26, **Q2 OUT 53**, Q4 OUT 2, Q1 UNKNOWABLE 2 (HHH, RGTI). *(Counted from the register at the fold: "
           "82 before this wave plus SONY.)*")
else:
    cnt = (f"{after} runs by the register at the fold** (82 before WAVE 5, plus SONY and {after-83} other WAVE 5 entr{'y' if after-83==1 else 'ies'} "
           "folded concurrently, whose categories stand as their own folds state).")
narr = open(HERE + r"\fold_narrative.md", encoding='utf-8').read().replace('@@COUNT@@', cnt)
rl = open(RL, encoding='utf-8').read()
assert 'UPDATE 2026-09-13 - SONY' not in rl
if not rl.endswith('\n'): rl += '\n'
open(RL, 'w', encoding='utf-8').write(rl + narr)
print('reading list appended; count line:', cnt[:80])
