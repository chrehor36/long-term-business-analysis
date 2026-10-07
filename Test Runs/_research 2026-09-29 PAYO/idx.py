import sys, json
sys.path.insert(0,'tools')
import sources as s
acc = sys.argv[1]
j = json.loads(s._get(f'https://www.sec.gov/Archives/edgar/data/1845815/{acc.replace("-","")}/index.json', s.SEC_UA, None))
for it in j['directory']['item']: print(it['name'], it.get('size'))
