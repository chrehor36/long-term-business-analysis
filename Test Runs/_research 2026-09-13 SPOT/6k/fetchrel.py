import sys, json, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0,'.')
import edgar
CIK=1639920
rel = ['2021-02-03:0001193125-21-026331','2021-04-28:0001193125-21-135262','2021-07-28:0001193125-21-226476','2021-10-27:0001193125-21-308632',
'2022-02-02:0001140361-22-003619','2022-04-27:0001140361-22-016067','2022-07-27:0001193125-22-202574','2022-10-25:0001140361-22-038378',
'2023-01-31:0001140361-23-003467','2023-04-25:0001140361-23-020032','2023-07-25:0001140361-23-035965','2023-10-24:0001140361-23-049225',
'2024-02-06:0001140361-24-005769','2024-04-23:0001140361-24-021146','2024-07-23:0001140361-24-033792','2024-11-12:0001140361-24-046169',
'2025-02-04:0001140361-25-002936','2025-04-29:0001140361-25-016186','2025-07-29:0001140361-25-027654','2025-11-04:0001140361-25-040271',
'2020-02-05:0001193125-20-024715','2019-02-06:0001193125-19-028762','2023-01-23:0001193125-23-012552','2023-12-04:0001140361-23-055913']
for r in rel:
    d,acc=r.split(':')
    a=acc.replace('-','')
    try:
        idx=json.loads(edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json'))
    except Exception as e:
        print(d,'ERR',e); continue
    names=[it['name'] for it in idx['directory']['item'] if it['name'].lower().endswith(('.htm','.html')) and 'index' not in it['name']]
    ex=[n for n in names if re.search(r'ex99|ex-99|dex99|ex991',n.lower())] or names
    for n in ex:
        t=edgar.strip_html(edgar.get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{n}'))
        fn=f'R_{d}__{n.rsplit(".",1)[0]}.txt'
        open(fn,'w',encoding='utf-8').write(t); print(fn,len(t))
