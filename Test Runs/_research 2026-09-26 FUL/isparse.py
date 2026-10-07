import re,glob,json
NUM=r'(\(?\s?[\d,]+\s?\)?)'
def val(t):
    t=t.strip(); neg=t.startswith('('); v=float(re.sub(r'[^\d]','',t))/1000; return -v if neg else v
res={}
for fn in sorted(glob.glob('tenk_*.txt')):
    y=int(fn[5:9]); s=open(fn,encoding='utf-8').read(); s=re.sub(r'[\s|$]+',' ',s)
    ps=[m.start() for m in re.finditer(r'(?i)CONSOLIDATED STATEMENTS OF (INCOME|OPERATIONS)',s) if re.search(r'(?i)In thousands',s[m.start():m.start()+300]) and re.search(r'Net revenue \(?[\d,]{5,}',s[m.start():m.start()+600])]
    if not ps: print(y,'none'); continue
    b=s[ps[0]:ps[0]+3000]
    r={}
    for k,l in dict(rev=r'Net revenue ',cos=r'Cost of sales ',gp=r'Gross profit ',sga=r'Selling, general and administrative expenses ',intx=r'Interest expense ',pti=r'Income (?:from continuing operations )?before income taxes[^\d(]*').items():
        m=re.search(l+NUM,b); r[k]=val(m.group(1)) if m else None
    res[y]=r
    gm=r['gp']/r['rev'] if r['gp'] and r['rev'] else None
    print(y,r, 'GM %.1f%%'%(gm*100) if gm else '')
json.dump(res,open('is_parsed.json','w'),indent=1)
