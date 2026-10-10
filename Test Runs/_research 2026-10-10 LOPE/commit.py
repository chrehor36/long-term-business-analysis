import subprocess,sys,time
msg=sys.argv[1]+"\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
paths=["Test Runs/2026-10-10 Run - LOPE Grand Canyon Education.md","Test Runs/_research 2026-10-10 LOPE"]
for i in range(10):
    a=subprocess.run(["git","add","--"]+paths,capture_output=True,text=True)
    if a.returncode==0:
        c=subprocess.run(["git","commit","-q","-m",msg,"--"]+paths,capture_output=True,text=True)
        if c.returncode==0:
            print(subprocess.run(["git","log","--oneline","-1"],capture_output=True,text=True).stdout); sys.exit(0)
        err=c.stderr
    else: err=a.stderr
    print("attempt",i,"failed:",err.strip()[:200]); time.sleep(30)
sys.exit(1)
