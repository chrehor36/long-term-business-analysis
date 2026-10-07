import re,sys
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    lines=[l for l in s.split('\n') if len(l)<3000 and not re.fullmatch(r'[\s|​$]*',l)]
    t=' '.join(lines)
    t=re.sub(r' \| ',' ',t); t=re.sub(r'\s+',' ',t)
    open(f.replace('.txt','.flat'),'w',encoding='utf-8').write(t)
