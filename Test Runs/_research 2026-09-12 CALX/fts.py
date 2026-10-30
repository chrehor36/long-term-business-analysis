import urllib.parse
import json, urllib.request, time
H={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
ciks={"ADTN":"926282","CIEN":"936395","HLIT":"851310","CMBM":"1738177","UI":"1511737","CLFD":"796505","COMM":"1517228","NOK":"924613","CSCO":"858877"}
for t,c in ciks.items():
    u=f'https://efts.sec.gov/LATEST/search-index?q=%22Calix%22&forms=10-K&ciks=CIK{int(c):010d}'
    u=f'https://efts.sec.gov/LATEST/search-index?q="Calix"&forms=10-K&ciks=CIK{int(c):010d}'
    u=urllib.parse.quote(u, safe=":/?&=")
    try:
        r=urllib.request.Request(u,headers=H)
        d=json.load(urllib.request.urlopen(r,timeout=60))
        hits=d.get("hits",{}).get("total",{}).get("value",0)
        print(t, "hits", hits, [h["_source"]["file_date"] for h in d.get("hits",{}).get("hits",[])[:6]])
    except Exception as e:
        print(t,"ERR",e)
    time.sleep(0.4)
