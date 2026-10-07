import json,sys,re,time
from fetch import get, strip
def idx(cik,acc):
    b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/index.json')
    return [i['name'] for i in json.loads(b)['directory']['item']]
if __name__=='__main__':
    cik,acc=sys.argv[1],sys.argv[2]
    names=idx(cik,acc); print(names)
    for n in sys.argv[3:]:
        m=[x for x in names if re.search(n,x)]
        for x in m:
            out=f'{acc}_{x}.txt'
            open(out,'w',encoding='utf-8').write(strip(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{x}')))
            print('wrote',out); time.sleep(0.3)
