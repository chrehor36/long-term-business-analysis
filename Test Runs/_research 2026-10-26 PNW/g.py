import sys,re
import sys; sys.stdout.reconfigure(encoding="utf-8")
f,pat=sys.argv[1],sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 400; mx=int(sys.argv[4]) if len(sys.argv)>4 else 8
t=open('cache/'+f+'.txt',encoding='utf-8').read()
n=0
for m in re.finditer(pat,t,re.I):
    s=t[max(0,m.start()-w):m.end()+w].replace('\n',' ')
    print('@',m.start(),':',re.sub(r'\s+',' ',s));print('---');n+=1
    if n>=mx: break
