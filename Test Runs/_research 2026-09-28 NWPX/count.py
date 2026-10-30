import re
L=open('../../Screens/WATCHLIST RUN QUEUE.md',encoding='utf-8').read().split('\n')
h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']
w=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(h)==1 and len(w)==1, (h,w)
sl=L[h[0]+1:w[0]]
ent=[l for l in sl if l.startswith('- **')]
print('heading line', h[0]+1, 'write-early line', w[0]+1, 'entries', len(ent))
print('first', ent[0][:60]); print('second', ent[1][:60])
print('NWPX entries', sum(1 for l in ent if l.startswith('- **NWPX')))
print('unstruck NWPX lines in whole file:', [ (i+1, l[:120]) for i,l in enumerate(L) if re.search(r'(?<!~)\bNWPX\b(?!~)', l)])
d=open('../../Screens/_daily/_wave7_done.txt').read().split(); o=open('../../Screens/_daily/_wave7_order.txt').read().split()
print('done', len(d), d[-1], 'equal to order prefix', d==o[:len(d)], 'order[109]', o[109], 'order[110]', o[110])
