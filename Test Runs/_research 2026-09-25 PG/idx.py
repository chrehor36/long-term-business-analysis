import json,sys,time
from fetch import get
accs=sys.argv[1:]
for a in accs:
    n=a.replace('-','')
    j=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/80424/{n}/index.json"))
    print(a,[ (i['name'],i.get('size')) for i in j['directory']['item'] if not i['name'].endswith(('.jpg','.gif','.png','.xsd','.css','.js'))][:30])
    time.sleep(0.3)
