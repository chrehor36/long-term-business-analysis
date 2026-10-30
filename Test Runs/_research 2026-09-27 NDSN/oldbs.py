import re,json
fs={'2003-01-27_10-K_0000950152-03-000680.txt':(2002,2001),'2004-01-21_10-K_0000950152-04-000365.txt':(2003,2002),'2005-01-14_10-K_0000950152-05-000245.txt':(2004,2003),'2006-01-13_10-K_0000950152-06-000197.txt':(2005,2004),'2007-01-12_10-K_0000950152-07-000253.txt':(2006,2005),'2007-12-21_10-K_0000950152-07-009783.txt':(2007,2006),'2008-12-19_10-K_0000950152-08-010466.txt':(2008,2007),'2009-12-18_10-K_0000950123-09-071805.txt':(2009,2008)}
labels={'cash':r'Cash and cash equivalents','mkt':r'Marketable securities','gw':r'Goodwill[^|]{0,12}','intang':r'Intangible assets[^|]{0,12}','notes':r'Notes payable','curltd':r'Current maturities of long-term debt','ltd':r'Long-term debt','equity':r"Total shareholders\S{0,3} equity",'assets_ppe':r'Property, plant and equipment[^|]{0,8}'}
num=r'\(?[\d,]+\)?'
def nums(seg,k=2):
    out=[]
    for t in re.findall(r'\|\s*\$?\s*\|?\s*(\(?[\d,]{1,12}\)?|—|�|-)\s*(?=\|)',seg):
        if t in ('—','�','-'): out.append(0.0)
        else: out.append(float(t.strip('()').replace(',',''))*(-1 if t.startswith('(') else 1))
        if len(out)==k: break
    return out
res={}
for f,(y0,y1) in fs.items():
    s=open('filings/'+f,encoding='utf-8').read()
    s=re.sub(r'\s+',' ',s); s=re.sub(r'(\| )+','| ',s)
    m=[x for x in re.finditer(r'Consolidated Balance Sheets',s) if re.search(r'\d{3},\d{3}',s[x.start():x.start()+800])]
    b=s[m[0].start():m[0].start()+5000]
    row={}
    for k,l in labels.items():
        mm=re.search(l+r'\s*\|',b)
        row[k]=nums(b[mm.end()-1:mm.end()+80]) if mm else None
    print(y0,y1,row)
    for i,y in enumerate((y0,y1)):
        res.setdefault(y,{})
        for k,v in row.items():
            if v and len(v)>i and k not in res[y]: res[y][k]=v[i]
json.dump(res,open('oldbs.json','w'),indent=0)
