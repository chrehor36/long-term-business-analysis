import sys, os, json, time, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1477294'
def doc(acc, name, out):
    a=acc.replace('-','')
    if os.path.exists(out): return out
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{name}')
    open(out,'w',encoding='utf-8').write(strip(b)); time.sleep(0.2)
    return out
def index(acc):
    a=acc.replace('-','')
    idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
    return [it['name'] for it in idx['directory']['item']]
if __name__=='__main__':
    if sys.argv[1]=='index': print(index(sys.argv[2]))
    else: print(doc(sys.argv[1],sys.argv[2],sys.argv[3]), os.path.getsize(sys.argv[3]))
