import urllib.request, json, sys, urllib.parse
UA={'User-Agent':'Mozilla/5.0 research'}
for q in sys.argv[1:]:
    u='https://projects.propublica.org/nonprofits/api/v2/search.json?q='+urllib.parse.quote(q)
    try:
        b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
        d=json.loads(b)
        for o in d.get('organizations',[])[:6]:
            print(q,'|',o.get('ein'),o.get('name'),o.get('city'),o.get('state'))
    except Exception as e: print(q,'FAIL',e)
