import re,glob,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def norm(t):
    t=t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('\xa0',' ')
    t=re.sub(r'\s*\|\s*',' ',t)
    t=re.sub(r'\s+',' ',t)
    return t.lower()
srcs=glob.glob('*.txt')+glob.glob('peers/*.txt')+glob.glob('jnj/*.txt')+[r'../../principle_ledger.csv',r'../../Framework/THE FRAMEWORK v4.md',r'../2026-09-12 Run - ROKU Roku.md',r'../../Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv']
big=' '.join(norm(open(f,encoding='utf-8',errors='ignore').read()) for f in srcs)
big2=re.sub(r'\s','',big)
run=open(sys.argv[1],encoding='utf-8').read()
frags=re.findall(r'\*"(.+?)"\*',run,flags=re.S)
bad=0
for q in frags:
    n=norm(q).strip()
    parts=[p.strip() for p in re.split(r'\s*(?:\.\.\.|\[\.\.\.\]|…)\s*',n) if p.strip()]
    ok=all((p in big) or (re.sub(r'\s','',p) in big2) for p in parts)
    if not ok:
        bad+=1; print('UNMATCHED:',q[:200])
print(len(frags),'fragments,',bad,'unmatched')
