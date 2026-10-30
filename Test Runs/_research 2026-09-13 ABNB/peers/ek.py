import json
rows=[]
for f in ["sub_EXPE.json","sub_EXPE_CIK0001324424-submissions-001.json"]:
    j=json.load(open(f)); r=j['filings']['recent'] if 'filings' in j else j
    rows+=list(zip(r['form'],r['filingDate'],r['accessionNumber'],r['primaryDocument'],r['items'] if 'items' in r else ['']*len(r['form'])))
for x in sorted(set(rows)):
    if x[0]=="8-K" and "2.02" in x[4] and x[1]>="2020-01-01" and x[1][5:7] in ("02","08"): print(x)
