import sys, textwrap
f,a,b=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
s=open(f,encoding='utf-8').read()
sys.stdout.reconfigure(encoding='utf-8')
print(textwrap.fill(s[a:b],220))
