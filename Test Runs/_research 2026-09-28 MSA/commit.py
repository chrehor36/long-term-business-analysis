import subprocess,sys
R='Test Runs/_research 2026-09-28 MSA'
extra=sys.argv[2:]
staged=subprocess.run(['git','diff','--cached','--name-only','--',R],capture_output=True,text=True).stdout.split('\n')
paths=[p for p in staged if p]+extra
r=subprocess.run(['git','commit','-q','-F',sys.argv[1],'--']+paths,capture_output=True,text=True)
print(r.stdout,r.stderr)
print(subprocess.run(['git','log','--oneline','-1'],capture_output=True,text=True).stdout)
print(subprocess.run(['git','show','--stat','--format=','HEAD'],capture_output=True,text=True).stdout)
