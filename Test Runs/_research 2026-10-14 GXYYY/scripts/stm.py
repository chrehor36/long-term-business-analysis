import sys, fitz, re
sys.stdout.reconfigure(encoding='utf-8')
def lines(p):
    words=p.get_text('words'); rows=[]
    for w in sorted(words,key=lambda w:(w[1]+w[3])/2):
        yc=(w[1]+w[3])/2
        if rows and abs(rows[-1][0]-yc)<3.0: rows[-1][1].append(w)
        else: rows.append([yc,[w]])
    return [' '.join(w[4] for w in sorted(ws,key=lambda w:w[0])) for yc,ws in rows]
f=sys.argv[1]; d=fitz.open(f)
cf=[i for i,p in enumerate(d) if re.search(r'Cash (generated from|used in|\(used in\)/generated from|generated from/\(used in\)) operations',p.get_text()) and 'investing activities' in p.get_text()]
rec=[i for i,p in enumerate(d) if ('Reconciliation of profit' in p.get_text() or 'reconciliation of profit' in p.get_text().lower()) and 'operations' in p.get_text()]
i=cf[0]
for j in list(range(i-4,i+1))+rec[:1]:
    print('=== page',j); print('\n'.join(lines(d[j])))
