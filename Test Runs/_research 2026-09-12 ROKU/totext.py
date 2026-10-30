import re,sys,html,os
for src in sys.argv[1:]:
    b=open(src,'rb').read().decode('utf-8','replace')
    b=re.sub(r'(?is)<(script|style).*?</\1>',' ',b)
    b=re.sub(r'(?is)</t[dh]>','\t',b)
    b=re.sub(r'(?is)</tr>','\n',b)
    b=re.sub(r'(?is)<(p|div|br|tr|h[1-6])[^>]*>','\n',b)
    b=re.sub(r'(?s)<[^>]+>',' ',b)
    b=html.unescape(b)
    b=re.sub(r'[ \u00a0]+',' ',b)
    b=re.sub(r'\n[ \t]*\n+','\n',b)
    lines=[l.strip() for l in b.split('\n')]
    out=src.rsplit('.',1)[0]+'.txt'
    open(out,'w',encoding='utf-8').write('\n'.join(l for l in lines if l))
    print(out, os.path.getsize(out))
