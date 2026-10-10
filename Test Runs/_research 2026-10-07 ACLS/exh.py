import sys, json, urllib.request, time
cik=1113232 if len(sys.argv)<3 else int(sys.argv[2])
acc=sys.argv[1].replace('-','')
u=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/index.json"
d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Chris Hrehor chrehor36@gmail.com"})).read())
for it in d['directory']['item']: print(it['name'])
time.sleep(0.2)
