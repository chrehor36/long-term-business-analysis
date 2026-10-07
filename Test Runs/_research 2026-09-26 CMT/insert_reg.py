p = r'C:/Users/chreh/OneDrive/Documents/BRK/Screens/WATCHLIST RUN QUEUE.md'
raw = open(p, 'rb').read()
crlf = b'\r\n' in raw
t = raw.decode('utf-8')
nl = '\r\n' if crlf else '\n'
L = t.split(nl)
h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE']
assert len(h) == 1, h
def count(L):
    h = [i for i, l in enumerate(L) if l == '## COMPLETED FROM THE QUEUE'][0]
    e = [i for i, l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
    assert len(e) == 1
    return [l for l in L[h + 1:e[0]] if l.startswith('- **')]
before = count(L)
assert not any(l.startswith('- **CMT ') for l in before)
new = open(r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/_research 2026-09-26 CMT/_reg_entry.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:h[0] + 1] + new + L[h[0] + 1:]
after = count(L)
print('crlf', crlf, 'heading line', h[0] + 1, 'before', len(before), 'after', len(after), 'first', after[0][:40])
assert len(after) == len(before) + 1 and after[0].startswith('- **CMT ')
open(p, 'wb').write(nl.join(L).encode('utf-8'))
