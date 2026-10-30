import sys
run='2026-09-27 Run - WFCF Where Food Comes From.md'
start_marker, end_marker, body = sys.argv[1], sys.argv[2], sys.argv[3]
s=open(run,encoding='utf-8').read()
a=s.index(start_marker); b=s.index(end_marker,a)
assert s.count(start_marker)==1, 'start not unique'
new=open(body,encoding='utf-8').read()
if not new.endswith('\n'): new+='\n'
s=s[:a]+new+'\n'+s[b:]
open(run,'w',encoding='utf-8').write(s)
print('ok', a, b)
