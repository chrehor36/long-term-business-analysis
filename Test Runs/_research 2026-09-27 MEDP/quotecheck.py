import re, glob, sys
def norm(s): 
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('–','-').replace('—','-')
    return re.sub(r'\s+',' ',s).strip()
corpus={}
for f in glob.glob('filings/*.txt')+glob.glob('peers/*.txt'):
    corpus[f]=norm(open(f,encoding='utf-8').read())
body=open(sys.argv[1],encoding='utf-8').read()
qs=re.findall(r'\*"(.+?)"\*',body)
bad=0
for q in qs:
    parts=[norm(p) for p in re.split(r'\s*(?:\.\.\.|\[\.\.\.\]|…)\s*',q) if p.strip()]
    ok=all(any(p in t for t in corpus.values()) for p in parts)
    if not ok:
        bad+=1; print('MISSING:',q[:200])
print(len(qs),'quotes,',bad,'missing')
