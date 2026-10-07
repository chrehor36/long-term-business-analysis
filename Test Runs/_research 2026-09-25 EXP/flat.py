import re,sys
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\s*\n\s*',' ',s); s=re.sub(r' +',' ',s)
    s=re.sub(r'(\. )(?=[A-Z])',r'.\n',s)  # sentence-ish breaks
    open(f.replace('.txt','_flat.txt'),'w',encoding='utf-8').write(s)
