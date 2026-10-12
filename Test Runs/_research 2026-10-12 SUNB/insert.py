import sys
p="Test Runs/2026-10-12 Run - SUNB Sunbelt Rentals Holdings.md"
start_marker, end_marker, draft = sys.argv[1], sys.argv[2], sys.argv[3]
s=open(p,encoding='utf-8').read()
a=s.index(start_marker); b=s.index(end_marker, a)
new=open(draft,encoding='utf-8').read()
s=s[:a]+new+s[b:]
open(p,'w',encoding='utf-8').write(s)
print('ok', a, b)
