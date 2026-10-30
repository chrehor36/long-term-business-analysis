# check every > "..." quote and inline "..." quote of 60+ chars in peers_music.md exists verbatim in some source txt
import re, glob
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).strip()
src={f:norm(open(f,encoding='utf-8').read()) for f in glob.glob('*.txt')}
md=open('../peers_music.md',encoding='utf-8').read()
qs=re.findall(r'"([^"]{60,}?)"', md.replace('“','"').replace('”','"')) + re.findall(r'“([^”]{60,}?)”', md)
bad=0
for q in qs:
    nq=norm(q).replace('[s]','')
    parts=[p for p in re.split(r'\.\.\.|\[.*?\]', nq) if len(p.strip())>20]
    ok=all(any(p.strip() in t for t in src.values()) for p in parts)
    if not ok:
        bad+=1; print("NOT FOUND:", q[:150])
print(len(qs),"quotes checked,",bad,"not found")
