import io, sys
p = 'Test Runs/2026-09-19 Run - DIS Walt Disney.md'
src, start_marker, end_marker = sys.argv[1], sys.argv[2], sys.argv[3]
t = io.open(p, encoding='utf-8').read()
a = t.index(start_marker)
b = t.index(end_marker)
new = io.open(src, encoding='utf-8').read()
io.open(p, 'w', encoding='utf-8').write(t[:a] + new + t[b:])
print('replaced', start_marker[:40], '->', end_marker[:40], len(new))
