import io
p = 'Test Runs/2026-09-19 Run - DIS Walt Disney.md'
t = io.open(p, encoding='utf-8').read()
start = t.index('## STEP 0 - THE RATE, AND THE FILING'.replace(' - ', ' — '))
end = t.index('## Q2 — IS IT A FRANCHISE?')
new = io.open('Test Runs/_research 2026-09-19 DIS/q1.md', encoding='utf-8').read()
io.open(p, 'w', encoding='utf-8').write(t[:start] + new + t[end:])
print('written', len(new))
