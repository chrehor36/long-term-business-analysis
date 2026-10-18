import sys,re
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8').read()
    for _ in range(3):
        t=re.sub(r'\n\s*\|',' |',t)
        t=re.sub(r'\|\s*\n\s*(?=[\d\(\)%\$—\-,\.]+\s*(\||\n))','| ',t)
        t=re.sub(r'\n\s*(%|\)|\)%)\s*(?=\|)',r' \1',t)
    t=re.sub(r'(\|\s*){2,}','| ',t)
    t=re.sub(r'[ \t]+',' ',t)
    open(f.replace('.txt','.c.txt'),'w',encoding='utf-8').write(t)
