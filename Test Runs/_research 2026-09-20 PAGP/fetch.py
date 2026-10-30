import urllib.request, json, os, sys, gzip, io
UA={'User-Agent':'BRK research chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
D=os.path.dirname(os.path.abspath(__file__))
def get(url, binary=False):
    req=urllib.request.Request(url, headers=UA)
    r=urllib.request.urlopen(req, timeout=120)
    raw=r.read()
    if r.headers.get('Content-Encoding')=='gzip':
        raw=gzip.decompress(raw)
    return raw if binary else raw.decode('utf-8','replace')
def save(name, url, binary=False):
    p=os.path.join(D,name)
    if os.path.exists(p) and os.path.getsize(p)>0:
        print('have', name); return
    d=get(url, binary)
    mode='wb' if binary else 'w'
    with open(p, mode, **({} if binary else {'encoding':'utf-8'})) as f: f.write(d)
    print('saved', name, len(d))
if __name__=='__main__':
    save('submissions.json','https://data.sec.gov/submissions/CIK0001581990.json')
    save('companyfacts.json','https://data.sec.gov/api/xbrl/companyfacts/CIK0001581990.json')
