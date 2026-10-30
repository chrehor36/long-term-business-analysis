import re
R = r'C:/Users/chreh/OneDrive/Documents/BRK/'
M = R + 'Test Runs/_research 2026-09-26 WSM/'

def append(path, addition):
    raw = open(path, 'rb').read()
    crlf = b'\r\n' in raw
    nl = '\r\n' if crlf else '\n'
    t = raw.decode('utf-8')
    if not t.endswith(nl):
        t += nl
    add = addition.replace('\r\n', '\n').rstrip('\n').replace('\n', nl) + nl
    open(path, 'wb').write((t + add).encode('utf-8'))
    print(path.split('/')[-1], 'crlf', crlf)

# shape index: count rows first
sp = R + 'Screens/SURVIVAL SHAPES - index.md'
st = open(sp, encoding='utf-8').read()
rows = re.findall(r'^\| (\d+) \|', st, re.M)
print('shape rows', len(rows), 'max', max(int(x) for x in rows))
assert len(rows) == 30 and max(int(x) for x in rows) == 30
assert 'the WSM fold' not in st
append(sp, '\n' + open(M + '_shape_note.md', encoding='utf-8').read())

fp = R + 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
ft = open(fp, encoding='utf-8').read()
assert 'UPDATE 2026-09-26 - WSM' not in ft
append(fp, open(M + '_fold.md', encoding='utf-8').read())
