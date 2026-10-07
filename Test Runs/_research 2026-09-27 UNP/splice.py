import sys,re,io
run='Test Runs/2026-09-27 Run - UNP Union Pacific.md'
s=io.open(run,encoding='utf-8').read()
start_marker,end_marker,body=sys.argv[1],sys.argv[2],sys.argv[3]
b=io.open(body,encoding='utf-8').read().rstrip('\n')+'\n'
i=s.index(start_marker); j=s.index(end_marker,i)
# end marker is the heading of the next section; keep it
s=s[:i]+b+'\n'+s[j:]
s=s.replace('# Company Run — [COMPANY] ([TICKER]) — [DATE]','# Company Run — Union Pacific Corporation (UNP) — 2026-09-27')
io.open(run,'w',encoding='utf-8',newline='\n').write(s)
print('ok',len(s))
