import sys
t=open(sys.argv[1],encoding='utf-8').read()
i=t.find(sys.argv[2])
if len(sys.argv)>4: i=t.find(sys.argv[2], i+1) if sys.argv[4]=='2' else i
n=int(sys.argv[3])
s=t[i:i+n]
s='\n'.join(l for l in s.split('\n') if 'TABLE OF CONTENTS' not in l and 'COPEL and Subsidiaries' not in l and 'COMPANHIA PARANAENSE' not in l and l.strip(' |'))
sys.stdout.reconfigure(encoding='utf-8')
print(s)
