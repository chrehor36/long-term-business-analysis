import sys,io
F='Test Runs/2026-09-27 Run - NGVC Natural Grocers.md'
start_marker, end_marker, body = sys.argv[1], sys.argv[2], sys.argv[3]
t=open(F,encoding='utf-8').read()
a=t.index(start_marker); b=t.index(end_marker) if end_marker!='EOF' else len(t)
assert t.count(start_marker)==1, 'start not unique'
new=t[:a]+open(body,encoding='utf-8').read().rstrip('\n')+'\n\n'+t[b:]
open(F,'w',encoding='utf-8',newline='\n').write(new)
print('ok', len(t), '->', len(new))
