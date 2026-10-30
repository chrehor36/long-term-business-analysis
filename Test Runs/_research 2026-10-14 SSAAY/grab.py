import re,sys
s=open(sys.argv[1],encoding='utf-8').read().replace('|',' ')
s=re.sub(r'\s+',' ',s).replace('$ ','$')
for pat in sys.argv[2:]:
    for m in list(re.finditer(pat,s))[:3]: print('>>',m.group(0)[:260])
