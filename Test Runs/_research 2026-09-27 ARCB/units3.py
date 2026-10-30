import re,sys,glob,os
sys.stdout.reconfigure(encoding='utf-8')
files=['cache/ex03_d13042exv13.txt.txt','cache/ex05_d33393exv13.htm.txt']+sorted(glob.glob('cache/tenk_20*.txt'))
for f in files:
    s=open(f,encoding='utf-8').read().replace('​',' ')
    s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\s+',' ',s)
    for m in re.finditer(r'Tonnage[^.]{0,40}?(\(tons\)|per day)[ A-Za-z()]{0,30}([\d,]{5,}) ([\d,]{5,})',s):
        print(os.path.basename(f), m.group(0)[:160]); break
