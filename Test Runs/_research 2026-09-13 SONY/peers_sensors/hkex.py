import urllib.request, json, re, sys
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read().decode("utf-8","replace")
t = get("https://www1.hkexnews.hk/search/prefix.do?&callback=callback&lang=EN&type=A&name=00501&market=SEHK")
print(t[:600])
m = re.search(r'"stockId":(\d+)', t)
sid = m.group(1)
u = ("https://www1.hkexnews.hk/search/titleSearchServlet.do?sortDir=0&sortByOptions=DateTime&category=0&market=SEHK"
     "&stockId=%s&documentType=-1&fromDate=20250601&toDate=20260913&title=&searchType=0&t1code=-2&t2Gcode=-2&t2code=-2&rowRange=200&lang=EN" % sid)
r = json.loads(get(u))
res = json.loads(r["result"]) if isinstance(r.get("result"), str) else r.get("result")
for x in res:
    print(x.get("DATE_TIME"), "|", x.get("TITLE")[:110].replace("\n"," "), "|", x.get("FILE_LINK"), "|", x.get("SHORT_TEXT","")[:60])
