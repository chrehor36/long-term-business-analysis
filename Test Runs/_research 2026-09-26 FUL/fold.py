import re
ROOT = r'C:/Users/chreh/OneDrive/Documents/BRK/'
Q = ROOT + 'Screens/WATCHLIST RUN QUEUE.md'
D = ROOT + 'Screens/_daily/_wave7_done.txt'
R = ROOT + 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
S = ROOT + 'Screens/SURVIVAL SHAPES - index.md'
H = ROOT + 'Test Runs/_research 2026-09-26 FUL/'
def count(lines):
    h = [i for i, l in enumerate(lines) if l == '## COMPLETED FROM THE QUEUE']
    w = [i for i, l in enumerate(lines) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(h) == 1 and len(w) == 1, (h, w)
    sl = lines[h[0] + 1:w[0]]
    return h[0], [l for l in sl if re.match(r'^- \*\*[A-Z0-9.\-]+ \(', l)]
txt = open(Q, encoding='utf-8').read(); L = txt.split('\n')
hi, before = count(L)
assert not any(l.startswith('- **FUL ') for l in before)
B = len(before); N = B + 1
entry = open(H + '_reg_entry.md', encoding='utf-8').read().rstrip('\n').replace('__N__', str(N)).replace('__B__', str(B)).split('\n')
L = L[:hi + 1] + entry + L[hi + 1:]
_, after = count(L)
assert len(after) == N and after[0].startswith('- **FUL ') and sum(1 for l in after if l.startswith('- **FUL ')) == 1
open(Q, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
print('register: before', B, 'after', len(after), 'first', after[0][:40], 'heading line', hi + 1)
d = open(D, encoding='utf-8').read()
assert 'FUL' not in d.split()
if not d.endswith('\n'): d += '\n'
d += 'FUL\n'; open(D, 'w', encoding='utf-8', newline='\n').write(d)
print('done file lines', len(d.strip().split('\n')), 'last', d.strip().split('\n')[-1])
r = open(R, encoding='utf-8').read()
if not r.endswith('\n'): r += '\n'
r += '\n' + open(H + '_fold.md', encoding='utf-8').read().rstrip('\n').replace('__N__', str(N)) + '\n'
open(R, 'w', encoding='utf-8', newline='\n').write(r)
s = open(S, encoding='utf-8').read()
rows = [l for l in s.split('\n') if re.match(r'^\| \d+ \|', l)]
nums = [int(re.match(r'^\| (\d+) \|', l).group(1)) for l in rows]
print('shapes rows', len(rows), 'max', max(nums))
if not s.endswith('\n'): s += '\n'
s += '\n' + open(H + '_shape.md', encoding='utf-8').read().rstrip('\n').replace('__ROWS__', str(len(rows))).replace('__MAX__', str(max(nums))) + '\n'
open(S, 'w', encoding='utf-8', newline='\n').write(s)
