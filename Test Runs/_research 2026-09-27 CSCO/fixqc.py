L=open('quotecheck.py',encoding='utf-8').read().split('\n')
for i,l in enumerate(L):
    if l.startswith('for f in [') and 'principle_ledger' in l:
        L[i]="for f in ['../../principle_ledger.csv','../../Framework/THE FRAMEWORK v4.md','../../Screens/SURVIVAL SHAPES - index.md','../../Test Runs/_TEMPLATE - Company Run.md']+glob.glob('../../Framework/v4/RULING CASE 2026-09-20*'):"
open('quotecheck.py','w',encoding='utf-8').write('\n'.join(L))
