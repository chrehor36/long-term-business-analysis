import re,sys,glob,os
sys.stdout.reconfigure(encoding='utf-8')
files=['cache/ex03_d13042exv13.txt.txt','cache/ex05_d33393exv13.htm.txt']+sorted(glob.glob('cache/tenk_20*.txt'))
for f in files:
    s=open(f,encoding='utf-8').read().replace('​',' ')
    s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\s+',' ',s)
    p=re.search(r'Pounds per day ([\d,]{6,}) ([\d,]{6,})',s)
    t=re.search(r'Tonnage per day ([\d,]{4,}) ([\d,]{4,})',s) or re.search(r'[Tt]onnage \(tons\) per day[^\d]{0,20}([\d,]{4,}) ([\d,]{4,})',s)
    y=re.search(r'hundredweight(?:, including fuel surcharges)?(?: \(\d\))? \$ ?([\d.]+) \$ ?([\d.]+)',s)
    tot=re.search(r'Tonnage \(tons\)[^\d]{0,30}([\d,]{6,}) ([\d,]{6,})',s)
    print(os.path.basename(f),'lbs/day',p and p.groups(),'tons/day',t and t.groups(),'tons',tot and tot.groups(),'yield',y and y.groups())
