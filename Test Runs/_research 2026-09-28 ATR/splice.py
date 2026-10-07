import sys
p='Test Runs/2026-09-28 Run - ATR AptarGroup.md'
start_marker, end_marker, body = sys.argv[1], sys.argv[2], sys.argv[3]
s=open(p,encoding='utf-8').read()
a=s.index(start_marker)
b=s.index(end_marker,a+1) if end_marker!='EOF' else len(s)
assert s.count(start_marker)==1, 'start not unique'
new=open(body,encoding='utf-8').read()
s=s[:a]+new+s[b:]
open(p,'w',encoding='utf-8').write(s)
print('spliced',a,b)
