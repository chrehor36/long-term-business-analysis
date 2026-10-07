import re,json
t=open('cf_statements.txt',encoding='utf-8').read()
labs={'ocf':r'(?:Net )?Cash (?:Flow )?(?:From|Provided [Bb]y|provided by) (?:\(?used in\)? )?(?:Continuing )?Operating Activities',
'capex':r'(?:Property additions|Capital expenditures)','da':r'Depreciation(?: and amortization)?','sbc':r'Stock-based compensation(?: \(Note \d+\))?',
'plx':r'Product liability expense(?: \(Note \d+\))?','plp':r'Product liability payments(?: \(Note \d+\))?','ins':r'Collections on insurance receivable[^|]*?(?:\(Note \d+\))?','contr':r'Contribution on divestiture of MSA LLC(?: \(Note \d+\))?','acq':r'Acquisitions?(?:, net of cash acquired)?(?: \(Note \d+\))?(?:,? and other investing)?'}
res={}
for blk in t.split('######## ')[1:]:
    fy=int(blk[2:6])
    b=re.sub(r'\s+',' ',blk); b=re.sub(r'\.{2,}',' ',b)
    b=b.replace('(','(').replace('—','0').replace('�','0')
    m=re.search(r'Year Ended December 31,?\s*(?:\|\s*)*(\d{4})\D+(\d{4})\D+(\d{4})',b,re.I)
    yrs=[int(x) for x in m.groups()] if m else [fy,fy-1,fy-2]
    for k,p in labs.items():
        mm=re.search(p+r'\s*((?:[\s|$]*(?:\(\s*[\d,]+\s*\|?\s*\)|[\d,]+|—|0)){3})',b)
        if not mm: continue
        vals=re.findall(r'\(\s*[\d,]+\s*\|?\s*\)|[\d,]+',mm.group(1))[:3]
        nums=[(-1 if v.startswith('(') else 1)*float(re.sub(r'[^\d]','',v) or 0)/1000 for v in vals]
        for y,v in zip(yrs,nums):
            res.setdefault(y,{}).setdefault(k,{})[fy]=v
out={}
for y in sorted(res):
    row={}
    for k,d in res[y].items():
        row[k]=d[max(d)]  # newest filing vintage
    out[y]=row
    print(y,{k:round(v,1) for k,v in row.items()})
json.dump(out,open('cf_text.json','w'),indent=0)
