P = r'C:\Users\chreh\OneDrive\Documents\BRK\Screens\2026-08-31 PREPPED READING LIST (operator lists).md'
N = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-27 AIT\fold_note.md'
b = open(P, 'rb').read()
assert b.endswith(b'\r\n')
assert b'UPDATE 2026-09-27 - AIT' not in b
note = open(N, encoding='utf-8').read().rstrip('\n')
add = note.replace('\n', '\r\n') + '\r\n'
open(P, 'ab').write(add.encode('utf-8'))
b2 = open(P, 'rb').read()
print('lines', b2.count(b'\r\n'), 'LF', b2.count(b'\n'), 'last', b2.decode('utf-8').rstrip().split('\r\n')[-1])
