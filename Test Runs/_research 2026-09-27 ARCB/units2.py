import re,sys,glob,os
sys.stdout.reconfigure(encoding='utf-8')
files=sorted(glob.glob('cache/tenk_20*.txt'))+['cache/ex05_d33393exv13.htm.txt','cache/ex03_d13042exv13.txt.txt']
for f in files:
    s=open(f,encoding='utf-8').read().replace('​',' ')
    s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\s+',' ',s)
    a=re.findall(r'[Tt]onnage per day(?: \(tons\))?(?: \([^)]*\))? ([\d,]{4,}(?: \$? ?[\d,.]+){1,4})',s)
    b=re.findall(r'[Bb]illed revenue per hundredweight(?:, including fuel surcharges)? \$ ([\d.]+(?: \$? ?[\d.,()%]+){1,4})',s)
    c=re.findall(r'[Rr]evenue per hundredweight(?:, including fuel surcharges)? \$ ([\d.]+(?: \$? ?[\d.,()%]+){1,4})',s)
    print(os.path.basename(f),'TPD',a[:2],'YLD',(b or c)[:2])
