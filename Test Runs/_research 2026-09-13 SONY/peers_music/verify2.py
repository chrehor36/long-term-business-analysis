import re, glob
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('​','')
    s=re.sub(r'-\s+(?=[a-z])','-',s)
    return re.sub(r'\s+',' ',s).strip()
src={f:norm(open(f,encoding='utf-8').read()) for f in glob.glob('*.txt')}
md=open('../peers_music.md',encoding='utf-8').read()
bad=0;n=0
for line in md.splitlines():
    if not line.startswith('> "'): continue
    for q in re.findall(r'"(.+?)"(?=\s*(?:\(|$|>))', line[2:]):
        n+=1; nq=norm(q)
        parts=[p.strip() for p in re.split(r'\[.*?\]',nq) if len(p.strip())>15]
        if not all(any(p in t for t in src.values()) for p in parts):
            bad+=1; print("NOT FOUND:", q[:200])
print(n,"blockquotes checked,",bad,"not found")
