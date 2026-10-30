p = r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-09-26 Run - MLI Mueller Industries.md'
L = open(p, encoding='utf-8').read().split('\n')
s = [i for i, l in enumerate(L) if l == '## SELF-AUDIT']
assert len(s) == 1
new = open(r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/_research 2026-09-26 MLI/_audit.md', encoding='utf-8').read().rstrip('\n').split('\n')
L = L[:s[0]] + new + ['']
old = '**WAVE 7 name 48 of 218. Claimed at dispatch 2026-09-26 by an unattended run agent. RESULT: in progress.**'
assert L[1] == old, L[1]
L[1] = '**WAVE 7 name 48 of 218. Claimed at dispatch 2026-09-26 by an unattended run agent (claim commit `7fd48dab`). RESULT: Q1 IN, Q2 OUT (on the business); the file closed at Q2.**'
open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
print('ok', len(L))
