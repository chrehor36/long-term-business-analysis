import re,json
blocks={}
t=open('cfs_blocks.txt',encoding='utf-8').read()
for b in t.split('== ')[1:]:
    blocks[int(b[:4])]=b
def row(b,lab):
    m=re.search(lab+r' (\(?[\d,]+\)?|-) (\(?[\d,]+\)?|-) (\(?[\d,]+\)?|-)',b)
    if not m: return None
    return [0 if g=='-' else (-1 if g.startswith('(') else 1)*int(g.strip('()').replace(',','')) for g in m.groups()]
data={}
for Y in range(2003,2026):
    b=blocks[Y]
    for k,lab in (('ocf','Cash provided by operating activities'),('dep','Depreciation'),('capex','Capital investments'),('sbcface','Stock-based compensation expense')):
        r=row(b,lab)
        if r is None: continue
        for i,v in enumerate(r):
            yr=Y-i
            if yr<2003: continue
            data.setdefault(yr,{})
            # newest vintage wins: later Y overwrites
            data[yr][k]=v; data[yr][k+'_vint']=Y
sbc_note={2008:65,2009:58,2010:74,2011:82,2012:93,2013:98,2014:112,2015:98,2016:82,2017:103,2018:96,2019:93,2020:73,2021:88,2022:99,2023:107,2024:118,2025:142,2007:44,2006:35}
sbc_pf={2003:50,2004:35,2005:50}  # after-tax pro forma fair-value totals, FY2005 10-K
caplease={2007:82,2008:175,2009:842,2010:0,2011:154,2012:290,2013:39,2014:0,2015:13,2016:0,2017:19,2018:12,2006:16}
cap=273.79*594075498/1e6
rows=[]
for y in range(2003,2026):
    d=data[y]; sbc=sbc_note.get(y,sbc_pf.get(y))
    ocf=d['ocf']; cx=-d['capex']; dep=d['dep']; cl=caplease.get(y,0)
    oe_cx=ocf-sbc-cx; oe_da=ocf-sbc-dep; oe_cl=oe_cx-cl
    rows.append((y,ocf,sbc,cx,dep,cl,oe_cx,oe_da,oe_cl,d['ocf_vint']))
print('cap',round(cap,1))
print('FY ocf sbc capex dep caplease OEcapex OEda OEcapex+lease vintage cx/dep')
for r in rows: print(*r, round(r[3]/r[4],2))
tc=sum(r[3] for r in rows); td=sum(r[4] for r in rows)
print('cum capex',tc,'cum dep',td,round(tc/td,3))
print('\nwindow capex-end D&A-end capex+lease  (yield on cap)')
res={}
for n in range(1,24):
    w=rows[-n:]
    a=sum(r[6] for r in w)/n; b=sum(r[7] for r in w)/n; c=sum(r[8] for r in w)/n
    res[n]=(a,b,c)
    print(f'{n}y {w[0][0]}-{w[-1][0]}: {a:,.1f} ({a/cap*100:.2f}%)  {b:,.1f} ({b/cap*100:.2f}%)  {c:,.1f} ({c/cap*100:.2f}%)  capex/dep {sum(r[3] for r in w)/sum(r[4] for r in w):.2f}')
print('\nrolling 5y capex-end')
for i in range(len(rows)-4):
    w=rows[i:i+5]; print(w[0][0],'-',w[-1][0], round(sum(r[6] for r in w)/5,1), round(sum(r[7] for r in w)/5,1))
json.dump(rows,open('oe_rows.json','w'))
