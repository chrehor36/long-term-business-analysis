import json
d=json.load(open('cf_parsed.json'))
x=json.load(open('xbrl_series.json'))
amort={int(k):v/1e3 for k,v in x['AmortizationOfIntangibleAssets'].items()}
Y={}
src={}
for fy in sorted(d,key=int):
    fy=int(fy); rec=d[str(fy)]
    scale=1 if fy>=2021 else 1/1000
    n=len(rec['ocf'])
    for j in range(n):
        yr=fy-j
        if yr<2006: continue
        vals={k:(rec[k][j]*scale if k in rec and j<len(rec[k]) else None) for k in ['ni','da','sbc','ocf','capex','ar','inv','pre','ap','acc']}
        if yr in Y:
            for k in ('ocf','sbc','capex','da'):
                if vals[k] is not None and Y[yr][k] is not None and abs(vals[k]-Y[yr][k])>1: print('RESTATED',yr,k,Y[yr][k],'->',vals[k],'in FY',fy)
        Y[yr]=vals; src[yr]=fy
rows=[]
print('yr src   OCF    SBC    D&A  amort   dep  capex  WC4   OE_DA  OE_capex  OE_capex_WCstrip  NI')
for yr in sorted(Y):
    v=Y[yr]; am=amort.get(yr,0.0)
    dep=v['da']-am
    wc=sum(v[k] for k in ['ar','inv','pre','ap','acc'])
    oe_da=v['ocf']-v['sbc']-dep
    oe_cx=v['ocf']-v['sbc']+v['capex']
    rows.append(dict(yr=yr,ocf=v['ocf'],sbc=v['sbc'],da=v['da'],am=am,dep=dep,capex=-v['capex'],wc=wc,oe_da=oe_da,oe_cx=oe_cx,strip=oe_cx-wc,ni=v['ni'],ap=v['ap']))
    print(f"{yr} {src[yr]} {v['ocf']/1e3:6.2f} {v['sbc']/1e3:6.2f} {v['da']/1e3:6.2f} {am/1e3:5.2f} {dep/1e3:6.2f} {-v['capex']/1e3:6.2f} {wc/1e3:6.2f} {oe_da/1e3:7.2f} {oe_cx/1e3:8.2f} {(oe_cx-wc)/1e3:8.2f} {v['ni']/1e3:6.2f}")
json.dump(rows,open('oe_rows.json','w'),indent=0)
cap=None
import sys
cap=float(sys.argv[1]) if len(sys.argv)>1 else 205.4
print('\nwindows ending 2025; cap',cap)
ys=[r['yr'] for r in rows]
for w in range(3,len(rows)+1):
    sel=rows[-w:]
    a=sum(r['oe_cx'] for r in sel)/w/1e3; b=sum(r['oe_da'] for r in sel)/w/1e3; s=sum(r['strip'] for r in sel)/w/1e3
    print(f"{w:2d}y {sel[0]['yr']}-{sel[-1]['yr']}  capex-end {a:6.2f} ({a/cap*100:5.2f}%)  D&A-end {b:6.2f} ({b/cap*100:5.2f}%)  capex-end WC-stripped {s:6.2f}")
