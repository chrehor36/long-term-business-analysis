import sys,re,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
f,pat=sys.argv[1],sys.argv[2]
w=int(sys.argv[3]) if len(sys.argv)>3 else 700
for i,l in enumerate(open(f,encoding='utf-8',errors='ignore')):
    if len(l)>20000: continue
    if re.search(pat,l,re.I): print(i+1,':',l.strip()[:w])
