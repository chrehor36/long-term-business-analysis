import sys
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-25 Run - WS Worthington Steel.md"
src = sys.argv[1]
t = open(p, encoding='utf-8').read()
add = open(src, encoding='utf-8').read()
open(p, 'w', encoding='utf-8').write(t.rstrip('\n') + '\n' + add.rstrip('\n') + '\n')
print(len(t), '->', len(t) + len(add))
