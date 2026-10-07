import json,urllib.request,sys,time,os
H={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url,headers=H)).read()
def idx(cik,acc):
    a=acc.replace('-','')
    return json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json'))
if __name__=='__main__':
    cik='1789832'
    for acc in sys.argv[1:]:
        j=idx(cik,acc)
        print('===',acc)
        for it in j['directory']['item']:
            print('  ',it['name'],it['size'])
        time.sleep(0.2)
