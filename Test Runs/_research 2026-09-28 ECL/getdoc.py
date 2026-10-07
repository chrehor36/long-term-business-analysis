import sys, os, json
from fetch import get, strip
CIK='31462'
def idx(acc):
    a=acc.replace('-','')
    d=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
    return [(it['name'],it.get('size')) for it in d['directory']['item']]
def doc(acc, name, out):
    out='cache/'+out
    if os.path.exists(out): return out
    a=acc.replace('-','')
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{name}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); return out
if __name__=='__main__':
    if sys.argv[1]=='idx':
        for acc in sys.argv[2:]:
            print('==',acc)
            for n,s in idx(acc):
                if n.endswith(('.htm','.txt')) and 'index' not in n: print('  ',n,s)
    else:
        doc(sys.argv[1], sys.argv[2], sys.argv[3])
