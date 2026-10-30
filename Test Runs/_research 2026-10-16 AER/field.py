import json,subprocess,sys
sys.argv=['x','AER']
exec(open('facts.py').read().split("t=sys.argv[1]")[0])
def series(t):
    d=json.load(open(f'cache/facts_{t}.json'))
    return {k:annual(d,v,'inst' if k in('eq','assets') else 'dur') for k,v in T.items()}
for t in ['AER','AL','AYR','WLFC']:
    r=series(t); ys=sorted(r['pti'])
    print('==',t,' year  EBIT/avgAssets  NI/avgEq  pti/avgEq  Assets/Eq')
    tot=[0,0,0,0];n=0
    for i,y in enumerate(ys):
        if y<'2011': continue
        prev=[p for p in sorted(r['assets']) if p<y]
        if not prev or y not in r['assets'] or y not in r['int']: continue
        p=prev[-1]
        aa=(r['assets'][y][0]+r['assets'][p][0])/2; ae=(r['eq'][y][0]+r['eq'][p][0])/2
        ebit=r['pti'][y][0]+r['int'][y][0]
        ni=r['ni'][y][0] if y in r['ni'] else float('nan')
        print(t,y,f"{ebit/aa*100:6.2f}% {ni/ae*100:7.2f}% {r['pti'][y][0]/ae*100:7.2f}% {r['assets'][y][0]/r['eq'][y][0]:5.2f}")
