# replace the block from heading A (inclusive) to heading B (exclusive) with the contents of a file
import sys
run = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - HMC Honda Motor.md"
a, b, src = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(run, encoding='utf-8').read()
i = t.index(a); j = t.index(b, i + len(a))
new = open(src, encoding='utf-8').read().rstrip('\n') + '\n\n'
t = t[:i] + new + t[j:]
open(run, 'w', encoding='utf-8').write(t)
print('replaced', j - i, 'chars with', len(new))
