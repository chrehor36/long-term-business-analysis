# THE FOLD, as ONE read-modify-write because concurrent runs share this tree.
# Counts the register entries between the last '## COMPLETED FROM THE QUEUE' heading line and
# '## THE WRITE-EARLY PROTOCOL' before and after, and refuses to write unless it is exactly one more.
import io, re, sys, shutil

Q   = 'Screens/WATCHLIST RUN QUEUE.md'
RL  = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
LOG = 'Screens/_daily/OVERNIGHT LOG.md'
D   = 'Test Runs/_research 2026-09-19 DIS/'

def count(text):
    lines = text.split('\n')
    hi = [i for i, l in enumerate(lines) if l.strip() == '## COMPLETED FROM THE QUEUE']
    pi = [i for i, l in enumerate(lines) if l.strip().startswith('## THE WRITE-EARLY PROTOCOL')]
    assert hi and pi, 'headings not found'
    seg = lines[hi[-1] + 1: pi[0]]
    return len([l for l in seg if re.match(r'^- \*\*', l)]), hi[-1], pi[0]

q = io.open(Q, encoding='utf-8').read()
before, hidx, pidx = count(q)
print('register entries BEFORE:', before)

assert 'DIS (The Walt Disney Company), 2026-09-19' not in q, 'DIS already entered - ABORT'

entry = io.open(D + 'fold_register.txt', encoding='utf-8').read().rstrip('\n')
lines = q.split('\n')
# newest entry goes immediately after the heading line, as KO/IBM/BIRD did
lines = lines[:hidx + 1] + [entry] + lines[hidx + 1:]
q2 = '\n'.join(lines)

# FOLD step 2: strike DIS in the WAVE 6 table
old_row = '| DIS | The Walt Disney Company | ordinary | **RUN** |'
assert q2.count(old_row) == 1, 'WAVE 6 DIS row not found exactly once'
q2 = q2.replace(old_row, '| ~~DIS~~ | The Walt Disney Company | ordinary | **RUN** |')

after, _, _ = count(q2)
print('register entries AFTER :', after)
assert after == before + 1, 'COUNT CHECK FAILED (%d -> %d) - ABORT, nothing written' % (before, after)

# FOLD step 3: the narrative fold
rl = io.open(RL, encoding='utf-8').read()
assert 'DIS (The Walt Disney Company) - run 2026-09-19' not in rl, 'narrative fold already present - ABORT'
narr = io.open(D + 'fold_narrative.md', encoding='utf-8').read()
rl2 = rl.rstrip('\n') + '\n\n' + narr.lstrip('\n')

# the overnight log line, with a clock time
log = io.open(LOG, encoding='utf-8').read()
line = io.open(D + 'fold_logline.txt', encoding='utf-8').read().strip()
assert '| DIS |' not in log, 'DIS already in the overnight log - ABORT'
log2 = log.rstrip('\n') + '\n' + line + '\n'

for p in (Q, RL, LOG):
    shutil.copy(p, D + 'backup_' + p.replace('/', '_'))
io.open(Q, 'w', encoding='utf-8', newline='').write(q2)
io.open(RL, 'w', encoding='utf-8', newline='').write(rl2)
io.open(LOG, 'w', encoding='utf-8', newline='').write(log2)
print('WROTE all three. Register entry number:', after)
print('WAVE 6 DIS struck:', '| ~~DIS~~ |' in q2)
