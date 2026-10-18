# Print PDF pages whose text contains all given needles, with lines rebuilt by y coordinate.
# usage: python -P -E pg.py file.pdf "needle1" ["needle2" ...] [--max N]
import sys
import fitz
sys.stdout.reconfigure(encoding='utf-8')
args=sys.argv[1:]
mx=1
if '--max' in args:
    k=args.index('--max'); mx=int(args[k+1]); del args[k:k+2]
pages=None
if '--pages' in args:
    k=args.index('--pages'); a,b=args[k+1].split('-'); pages=range(int(a),int(b)+1); del args[k:k+2]
f=args[0]; needles=args[1:]
d=fitz.open(f)
n=0
for i,p in enumerate(d):
    if pages is not None and i not in pages: continue
    t=p.get_text()
    if all(x in t for x in needles):
        print('=== page',i)
        words=p.get_text('words')
        rows=[]
        for w in sorted(words,key=lambda w:(w[1]+w[3])/2):
            yc=(w[1]+w[3])/2
            if rows and abs(rows[-1][0]-yc)<3.0:
                rows[-1][1].append(w)
            else:
                rows.append([yc,[w]])
        for yc,ws in rows:
            print(' '.join(w[4] for w in sorted(ws,key=lambda w:w[0])))
        n+=1
        if n>=mx: break
