# AIG fold, 2026-09-19. Re-reads every target file from disk at the moment of editing (other sessions
# write to the same files), makes surgical edits, and asserts the register gained exactly one entry.
import re, sys, os

Q = 'Screens/WATCHLIST RUN QUEUE.md'
RL = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
OL = 'Screens/_daily/OVERNIGHT LOG.md'
HERE = os.path.dirname(os.path.abspath(__file__))

def count_entries(text):
    m1 = re.search(r'(?m)^## COMPLETED FROM THE QUEUE\s*$', text)
    m2 = re.search(r'(?m)^## THE WRITE-EARLY PROTOCOL', text)
    assert m1 and m2 and m1.start() < m2.start(), 'register anchors not found'
    body = text[m1.end():m2.start()]
    lines = [l for l in body.split('\n') if l.startswith('- **')]
    aig = [l for l in lines if l.startswith('- **AIG')]
    return len(lines), len(aig)

ENTRY = open(os.path.join(HERE, 'fold_entry.md'), encoding='utf-8').read().rstrip('\n')
ROSTER = open(os.path.join(HERE, 'fold_roster.md'), encoding='utf-8').read().strip()
WAVE6 = open(os.path.join(HERE, 'fold_wave6.md'), encoding='utf-8').read().strip()
NARR = open(os.path.join(HERE, 'fold_narrative.md'), encoding='utf-8').read()
OLINE = open(os.path.join(HERE, 'fold_overnight.md'), encoding='utf-8').read().strip()

t = open(Q, encoding='utf-8').read()
before, aig_before = count_entries(t)
assert aig_before == 0, 'an AIG register entry already exists'
# 1. register entry, directly under the heading
m1 = re.search(r'(?m)^## COMPLETED FROM THE QUEUE\s*\n', t)
t = t[:m1.end()] + ENTRY + '\n' + t[m1.end():]
# 2a. strike in the WAVE 6 table (exactly one unstruck AIG row)
old_row = '| AIG | American International Group | insurer | **RUN on the Mini Berk track** |'
assert t.count(old_row) == 1, 'WAVE 6 AIG row not found exactly once'
t = t.replace(old_row, WAVE6)
# 2b. MINI BERK roster line: insert immediately before the CB item, as TRV and CB were recorded
anchor = ', **~~CB~~** *(Chubb Limited, added to this track from WAVE 6'
assert t.count(anchor) == 1, 'roster anchor not found exactly once'
assert '~~AIG~~ *(' not in t.split('### MINI BERK')[1].split('**UNBLOCKED')[0], 'AIG already on roster'
t = t.replace(anchor, ', ' + ROSTER + anchor)
after, aig_after = count_entries(t)
print('register entries before %d, after %d; AIG entries after %d' % (before, after, aig_after))
assert after == before + 1 and aig_after == 1
open(Q, 'w', encoding='utf-8', newline='').write(t)
# re-read from disk and recount
t2 = open(Q, encoding='utf-8').read()
print('recount from disk:', count_entries(t2))
# 3. narrative fold: append to the reading list
r = open(RL, encoding='utf-8').read()
assert '## AIG (American International Group' not in r, 'AIG narrative already present'
if not r.endswith('\n'): r += '\n'
open(RL, 'w', encoding='utf-8', newline='').write(r + '\n' + NARR)
# overnight log line
o = open(OL, encoding='utf-8').read()
assert '| AIG |' not in o
if not o.endswith('\n'): o += '\n'
open(OL, 'w', encoding='utf-8', newline='').write(o + OLINE + '\n')
print('fold written')
