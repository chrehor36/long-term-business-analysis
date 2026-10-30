import subprocess, time, sys
P=["Test Runs/2026-10-10 Run - LSTR Landstar.md","Test Runs/_research 2026-10-10 LSTR"]
msg=open(sys.argv[1],encoding="utf-8").read()
for i in range(10):
    a=subprocess.run(["git","add","--"]+P,capture_output=True,text=True)
    if a.returncode==0:
        c=subprocess.run(["git","commit","-q","-F",sys.argv[1],"--"]+P,capture_output=True,text=True)
        if c.returncode==0: print("OK try",i+1); break
        print("commit fail",c.stderr[:120])
    else: print("add fail try",i+1,a.stderr[:60])
    time.sleep(30)
print(subprocess.run(["git","log","--oneline","-1","--",P[0]],capture_output=True,text=True).stdout)
