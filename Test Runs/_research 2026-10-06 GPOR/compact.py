# Collapse one-cell-per-line tables into one line per row label. Text transformation only.
import sys,re
ZW='​‌‍﻿'
for fn in sys.argv[1:]:
    out=[];cur=''
    for ln in open(fn,encoding='utf-8'):
        s=ln
        for z in ZW: s=s.replace(z,'')
        s=s.strip()
        if not s or s in ('|','$','| $','|  |'): continue
        t=s.strip('| ').strip()
        if re.fullmatch(r'[\$\(\)\d,\.\-—–%\s|]+',s) or t in (')','%',')%'):
            cur+=' '+t
        else:
            if cur: out.append(cur)
            cur=t
    out.append(cur)
    open(fn.replace('.txt','.compact.txt'),'w',encoding='utf-8').write('\n'.join(out))
