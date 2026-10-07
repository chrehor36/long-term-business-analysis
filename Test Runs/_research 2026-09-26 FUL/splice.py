import sys
f='../2026-09-26 Run - FUL H.B. Fuller.md'
s=open(f,encoding='utf-8').read()
start,end,src=sys.argv[1],sys.argv[2],sys.argv[3]
a=s.index(start); b=s.index(end) if end!='EOF' else len(s)
new=open(src,encoding='utf-8').read()
s=s[:a]+new+('\n' if not new.endswith('\n') else '')+s[b:]
open(f,'w',encoding='utf-8').write(s); print('spliced',src,len(s))
