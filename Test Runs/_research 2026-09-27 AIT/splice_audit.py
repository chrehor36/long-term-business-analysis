run = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-27 Run - AIT Applied Industrial Technologies.md'
body = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-27 AIT\body_audit.md'
L = open(run, encoding='utf-8').read().split('\n')
si = [i for i, l in enumerate(L) if l.startswith('## SELF-AUDIT')]
assert len(si) == 1, si
new = open(body, encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:si[0]] + new
open(run, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('ok', len(L))
