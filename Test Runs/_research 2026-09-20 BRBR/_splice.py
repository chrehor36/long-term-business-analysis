import sys, io, os
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-20 Run - BRBR BellRing Brands.md"
sec_path = sys.argv[1]
start_marker = sys.argv[2]
end_marker = sys.argv[3]
t = io.open(p, encoding='utf-8').read()
new = io.open(sec_path, encoding='utf-8').read()
a = t.index(start_marker)
b = t.index(end_marker)
t = t[:a] + new + t[b:]
io.open(p, 'w', encoding='utf-8', newline='\n').write(t)
print("written", len(t))
