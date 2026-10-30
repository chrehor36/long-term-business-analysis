p = '../../Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
b = open(p, 'rb').read()
note = open('fold_note.md', encoding='utf-8').read()
note = note.replace('\n', '\r\n').encode('utf-8')
assert b.endswith(b'\r\n')
open(p, 'wb').write(b + note)
d = '../../Screens/_daily/_wave7_done.txt'
t = open(d, 'rb').read()
nl = b'\r\n' if b'\r\n' in t else b'\n'
if not t.endswith(nl):
    t += nl
open(d, 'wb').write(t + b'IPAR' + nl)
lines = open(d, encoding='utf-8').read().splitlines()
print('done lines', len(lines), 'last', lines[-1], 'IPAR count', lines.count('IPAR'))
