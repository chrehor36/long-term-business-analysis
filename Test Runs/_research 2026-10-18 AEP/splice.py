"""Replace the run-file text from a start heading up to (not including) an end heading with the content of a file.
python -I splice.py START_PREFIX END_PREFIX contentfile"""
import sys,os
run=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','2026-10-18 Run - AEP American Electric Power.md')
s=open(run,encoding='utf-8').read()
a=s.index(sys.argv[1]); b=s.index(sys.argv[2],a+1)
new=open(sys.argv[3],encoding='utf-8').read()
s=s[:a]+new.rstrip('\n')+'\n\n'+s[b:]
open(run,'w',encoding='utf-8').write(s)
print('ok',a,b)
