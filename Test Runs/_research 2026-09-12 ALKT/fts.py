import json, urllib.request, urllib.parse, collections, sys
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept":"application/json"}
def q(phrase, forms="10-K", start="2024-06-01", end="2026-09-12", frm=0):
    p={"q":'"%s"'%phrase,"forms":forms,"dateRange":"custom","startdt":start,"enddt":end,"from":frm}
    u="https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode(p)
    return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
out=[]
for phrase in ["Alkami"]:
    d=q(phrase)
    tot=d["hits"]["total"]["value"]; print(phrase,"total 10-K hits",tot)
    c=collections.Counter()
    for h in d["hits"]["hits"]:
        s=h["_source"]; c[(tuple(s.get("display_names",[])), s.get("form"), s.get("file_date"), h["_id"])]+=1
    for k in sorted(c, key=lambda x:x[2]): print("  ",k)
