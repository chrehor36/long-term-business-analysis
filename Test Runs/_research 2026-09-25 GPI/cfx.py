import re,sys
f=sys.argv[1]
s=open(f,encoding='utf-8',errors='ignore').read()
for m in re.finditer('CONSOLIDATED STATEMENTS OF CASH FLOWS',s):
    c=s[m.start():m.start()+20000]
    if re.search('OPERATING ACTIVITIES',c[:3000]): break
t=re.sub(r'[|$\n]',' ',c)
t=re.sub(r'\(\s*([\d,\.]+)\s*\)',r'-\1',t)
t=re.sub(r'\s+',' ',t)
t=t[:t.find('SUPPLEMENTAL')] if 'SUPPLEMENTAL' in t else t[:12000]
print(t)
