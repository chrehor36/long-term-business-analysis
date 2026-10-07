import sys, json, re, os
from fetch import get, strip
cik='1289460'
def idx(acc):
    a=acc.replace('-','')
    b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json')
    return [x['name'] for x in json.loads(b)['directory']['item']]
def doc(acc,name,out):
    a=acc.replace('-','')
    b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{name}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out))
if __name__=='__main__':
    for acc in sys.argv[1:]:
        print(acc, idx(acc))
