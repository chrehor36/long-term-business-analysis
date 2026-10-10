import sys, subprocess
jobs=[l.split() for l in open(sys.argv[1]) if l.strip()]
for cik,acc,doc,out in jobs:
    try:
        r=subprocess.run([sys.executable,'fetch.py','doc',cik,acc,doc,out],capture_output=True,text=True,timeout=150)
        print(out, r.stdout.strip()[-80:], r.stderr.strip()[-200:], flush=True)
    except Exception as e: print(out,'FAIL',e, flush=True)
