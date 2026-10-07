import json, sys, urllib.parse, urllib.request
def hits(phrase, cik):
    q={"q":'"%s"'%phrase,"ciks":cik}
    url="https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode(q)
    r=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}),timeout=60).read())
    out=[]
    for h in r['hits']['hits']:
        s=h['_source']; out.append((s.get('file_date'), s.get('form'), h['_id']))
    return r['hits']['total']['value'], sorted(out)
for ph, cik in [(a.split('|')[0], a.split('|')[1]) for a in sys.argv[1:]]:
    n, o = hits(ph, cik); print(ph, cik, n)
    for x in o: print('   ', x)
