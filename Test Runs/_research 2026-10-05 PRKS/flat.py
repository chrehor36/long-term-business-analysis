import re,sys,glob
for f in sorted(glob.glob('10K_FY*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t)
    open(f.replace('10K_','flat_'),'w',encoding='utf-8').write(t)
    ms=[m.group(0) for m in re.finditer(r'Attendance \(?[^A-Za-z]{0,10}[0-9,]{5,}[^A-Za-z]{0,120}',t)]
    print('==',f); [print('  ',x[:200]) for x in ms[:4]]
