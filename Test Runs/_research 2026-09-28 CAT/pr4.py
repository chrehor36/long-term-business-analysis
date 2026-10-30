import re,sys
sys.stdout.reconfigure(encoding='utf-8')
def doc(y):
    f=f'cache/x13_{y}.txt' if y<=2014 else f'cache/k_{y}.txt'
    return open(f,encoding='utf-8').read()
P=[r'(?:favorable|unfavorable|improved|higher|lower|better|weaker)?\s*price realization (?:of |was |were )?(?:favorable |unfavorable |improved |lower |higher )?(?:by )?\$\s?[\d.,]+ (?:million|billion)',
   r'\$\s?[\d.,]+ (?:million|billion) (?:of|in|from) (?:improved |favorable |unfavorable |higher |lower |better )?price realization',
   r'[Pp]rice realization (?:improved|increased|declined|decreased|was unfavorable|was favorable|was)\s*\$\s?[\d.,]+ (?:million|billion)']
for y in range(2001,2026):
    t=re.sub(r'\s+',' ',doc(y))
    print('=====',y)
    seen=0
    for p in P:
        for m in re.finditer(p,t):
            ctx=t[max(0,m.start()-260):m.end()+40]
            if re.search(r'quarter',ctx[-300:],re.I): continue
            print('  *',ctx.replace('|',' ')); seen+=1
            if seen>7: break
