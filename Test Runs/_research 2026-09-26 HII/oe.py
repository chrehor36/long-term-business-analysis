import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
cf=json.load(open('cf_parsed.json'))
order=['tenk_FY%d.txt'%y for y in range(2012,2025)]+['tenk25_hii-20251231.htm.txt']
S={}
for fn in order:  # later files overwrite: latest filed vintage wins
    r=cf[fn]
    for i,y in enumerate(r['years']):
        if y<2011: continue
        d=S.setdefault(y,{})
        for k in ['ocf','sbc','dep','amort','capex','capex_old','grant','retiree','ap','acq','div','buyback','int_paid']:
            if k in r: d[k]=r[k][i]
for y,d in S.items():
    d['cx']=-(d.get('capex',d.get('capex_old',0)))-d.get('grant',0)
CAP=10403.6; SOV=5.49
print('FY   OCF   SBC  dep  amort  netcapex  OE_capex  OE_DA   retiree  AP&acc')
for y in sorted(S):
    d=S[y]; d['oe_c']=d['ocf']-d['sbc']-d['cx']; d['oe_d']=d['ocf']-d['sbc']-d['dep']
    print(f"{y} {d['ocf']:6.0f} {d['sbc']:4.0f} {d['dep']:4.0f} {d['amort']:4.0f} {d['cx']:6.0f} {d['oe_c']:7.0f} {d['oe_d']:7.0f} {d.get('retiree',0):6.0f} {d.get('ap',0):6.0f}")
ttm=dict(ocf=1196-428-421,sbc=54-33+31,dep=225-110+112,amort=104-52+43,cx=(402-6)-(163-3)+(193-3))
ttm['oe_c']=ttm['ocf']-ttm['sbc']-ttm['cx']; ttm['oe_d']=ttm['ocf']-ttm['sbc']-ttm['dep']
print('TTM',ttm)
print('\nwindow  capex_end  DA_end  y_capex  y_DA   capex/dep')
W=[]
for n in range(3,16):
    ys=range(2026-n,2026)
    c=sum(S[y]['oe_c'] for y in ys)/n; a=sum(S[y]['oe_d'] for y in ys)/n
    ratio=sum(S[y]['cx'] for y in ys)/sum(S[y]['dep'] for y in ys)
    W.append((n,c,a)); print(f"{n:2d}y FY{2026-n}-25  {c:7.1f}  {a:7.1f}  {100*c/CAP:5.2f}%  {100*a/CAP:5.2f}%  {ratio:.2f}")
lo=min(min(c,a) for n,c,a in W); hi=max(max(c,a) for n,c,a in W)
print('range',lo,hi,100*lo/CAP,100*hi/CAP)
tot_sbc=sum(S[y]['sbc'] for y in S); tot_ocf=sum(S[y]['ocf'] for y in S); print('SBC share of OCF',tot_sbc,tot_ocf,tot_sbc/tot_ocf)
json.dump(S,open('oe_series.json','w'))
