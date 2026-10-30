import sys, json, os
from fetch import get, strip
cik='1767258'
def idx(acc):
    a=acc.replace('-','')
    b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json')
    return [x['name'] for x in json.loads(b)['directory']['item']]
def doc(acc,name,out):
    if os.path.exists(out): return
    a=acc.replace('-','')
    b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{name}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out))
L=[l.split() for l in open('sub_list.txt').read().splitlines()[2:] if l[:2]=='20']
want={'10-K':'k','10-Q':'q','10-K/A':'ka','DEF':'proxy','10-12B':'form10','10-12B/A':'form10a','CORRESP':'corresp'}
def main():
  for l in L:
      if l[1] in ('DEF','SCHEDULE'): l=[l[0],l[1]+' '+l[2]]+l[3:]
      fd,form,acc,docn=l[0],l[1],l[2],l[3]
      tag=None
      if form in ('10-K','10-Q','10-K/A','10-12B','10-12B/A','CORRESP'): tag=want[form]
      elif form=='DEF 14A': tag='proxy'
      if tag:
          doc(acc,docn,f'cache/{tag}_{fd}.txt')
if __name__=='__main__' and len(sys.argv)==1: main()
if __name__=='__main__' and len(sys.argv)>1:
    for acc in sys.argv[1:]: print(acc, idx(acc))
