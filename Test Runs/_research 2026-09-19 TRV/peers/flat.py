import sys,re
for fn in sys.argv[1:]:
    t=open(fn,encoding='utf-8').read()
    t=re.sub(r'\n(?=\s*\|)',' ',t)
    t=re.sub(r'\n(?=\s*\)\s*%)',' ',t)
    t=re.sub(r'(\|\s*)+\|',' | ',t)
    t=re.sub(r'[ \t]+',' ',t)
    open(fn.replace('raw/','flat/'),'w',encoding='utf-8').write(t)
