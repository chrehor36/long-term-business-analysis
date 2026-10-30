import sys, json, re
sys.path.insert(0, '.')
import edgar
from fetch2 import totext
s = json.load(open('submissions.json'))
r = s['filings']['recent']
for i in range(len(r['form'])):
    if r['form'][i] == '6-K' and r['filingDate'][i] >= sys.argv[1] and r['filingDate'][i] <= sys.argv[2]:
        acc = r['accessionNumber'][i]
        idx = json.loads(edgar.get(f"https://www.sec.gov/Archives/edgar/data/313838/{acc.replace('-','')}/index.json"))
        files = [f['name'] for f in idx['directory']['item'] if f['name'].lower().endswith(('.htm','.html','.txt','.pdf'))]
        main = r['primaryDocument'][i]
        t = totext(edgar.get(f"https://www.sec.gov/Archives/edgar/data/313838/{acc.replace('-','')}/{main}"))
        name = f"6K_{r['filingDate'][i]}_{acc[-6:]}"
        open(name + '.txt','w',encoding='utf-8').write(t)
        m = re.search(r'Documents attached hereto:(.{0,300})', t.replace('\n',' '), re.S)
        print(name, len(t), files, '::', (m.group(1)[:220] if m else t.replace('\n',' ')[900:1150]))
