import json, urllib.parse, urllib.request
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept": "application/json"}
for cik, phrase, forms in [("0000059558", "cost of funds", "10-K"), ("0001333986", "cost of funds", "8-K"), ("0001822993", "net investment spread", "8-K")]:
    q = urllib.parse.urlencode({"q": '"%s"' % phrase, "ciks": cik, "forms": forms})
    d = json.loads(urllib.request.urlopen(urllib.request.Request("https://efts.sec.gov/LATEST/search-index?" + q, headers=UA), timeout=60).read())
    for h in d["hits"]["hits"]:
        s = h["_source"]
        print(cik, phrase, h["_id"], s.get("file_date"), s.get("root_forms"), s.get("file_type"))
