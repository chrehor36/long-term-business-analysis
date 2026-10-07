p = '../2026-09-27 Run - IPAR Interparfums.md'
s = open(p, encoding='utf-8').read()
i = s.index('## SELF-AUDIT')
b = open('body_audit.md', encoding='utf-8').read()
open(p, 'w', encoding='utf-8').write(s[:i] + b)
print('spliced', len(s[:i] + b))
