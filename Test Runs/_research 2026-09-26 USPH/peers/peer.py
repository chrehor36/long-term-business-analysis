import re,sys
pat=re.compile(r'(?i)(revenue per visit|net rate per patient visit|patient visits|number of visits|Adjusted EBITDA margin)')
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8').read(); t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t)
    print('==',f); n=0
    for m in pat.finditer(t):
        s=t[max(0,m.start()-150):m.start()+300]
        if re.search(r'\$ ?\d{2,3}(\.\d\d)?|\d{1,2},\d{3}',s):
            print('  ',s); n+=1
        if n>=7: break
