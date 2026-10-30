import re,sys
sys.stdout.reconfigure(encoding='utf-8')
def doc(y):
    f=f'cache/x13_{y}.txt' if y<=2014 else f'cache/k_{y}.txt'
    return open(f,encoding='utf-8').read()
for y in range(2004,2026):
    t=re.sub(r'[\s|$]+',' ',doc(y))
    i=[m.start() for m in re.finditer(r'Supplemental [Dd]ata for (?:Statement of )?[Cc]ash [Ff]low',t)][0]
    blk=t[i:i+20000]
    m=re.search(r'Capital expenditures\s*[–-]+\s*excluding equipment leased to others',blk)
    print(y, blk[m.end():m.end()+110] if m else 'NONE')
    m=re.search(r'[Ss]tock-based compensation expense|[Ss]hare-based compensation expense|[Ss]tock-based compensation',blk)
    if m: print('   SBC', blk[m.end():m.end()+90])
