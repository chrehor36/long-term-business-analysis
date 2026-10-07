"""Parse the filed consolidated cash-flow statement from each Nucor annual report (EX-13 FY2001-2018, 10-K FY2019-2025).
Each filing gives three fiscal years. Prints every vintage; cfs.json keeps all. Arithmetic transcription only."""
import re,sys,io,json,os
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
LAB={'ni':r'Net earnings(?: before noncontrolling interests)?(?! attributable)(?! per)',
'dep':r'Depreciation(?! and amortization of)',
'amort':r'Amortization',
'sbc':r'Stock-based compensation',
'ocf':r'Cash provided by operating activities',
'capex':r'Capital expenditures',
'acq':r'Acquisitions? \(net of cash acquired\)|Acquisitions? of businesses|Acquisitions?, net of cash acquired',
'nci':r'Distributions to (?:minority|noncontrolling) interests?',
'div':r'Cash dividends',
'buy':r'Acquisition of treasury stock|Purchase of treasury stock|Repurchase',
'aff':r'Investment in and advances to affiliates',
'disp':r'Disposition of plant and equipment|Proceeds from the sale of property',
'dep_all':r'Depreciation and amortization'}
NUM=r'\(?\s*-?[\d,]+(?:\.\d+)?\s*\)?|—|-(?=\s)'
def nums(s):
    out=[]
    for m in re.finditer(r'\(\s*([\d,]+(?:\.\d+)?)\s*\)|(?<![\w.])([\d]{1,3}(?:,\d{3})+(?:\.\d+)?|\d+\.\d+|\d+)(?![\w])|(—|–)',s):
        if m.group(1): out.append(-float(m.group(1).replace(',','')))
        elif m.group(2): out.append(float(m.group(2).replace(',','')))
        else: out.append(0.0)
    return out
def block(fn):
    t=open(fn,encoding='utf-8',errors='replace').read()
    flat=re.sub(r'\s+',' ',t.replace('|',' '))
    # find statement: the 'Operating activities:' followed within 6000 chars by 'Cash provided by operating activities' and 'Capital expenditures'
    best=None
    for m in re.finditer(r'Operating activities:?',flat,re.I):
        seg=flat[m.start():m.start()+9000]
        if re.search(LAB['ocf'],seg) and re.search(LAB['capex'],seg) and re.search(r'Net earnings',seg[:600]):
            best=seg; break
    return best
res={}
raw={}
files=[('ex13_%d.txt'%y,y) for y in range(2001,2019)]+[('tenk_%d.txt'%y,y) for y in range(2019,2026)]
for fn,fy in files:
    seg=block(fn)
    if not seg: print(fy,'NO BLOCK'); continue
    got={}
    for key,pat in LAB.items():
        m=re.search(r'(?:^|\s)(?:'+pat+r')[^0-9(—–]{0,120}',seg)
        if not m: continue
        rest=seg[m.end():m.end()+220]
        n=nums(rest)
        # scale: older statements in dollars (>1e6 values)
        if len(n)>=3: got[key]=n[:3]
    raw[fy]=dict(got)
    # detect units
    big=max(abs(x) for v in got.values() for x in v) if got else 0
    sc=1e6 if big>1e7 else (1e3 if big>1e5 and big<1e7 and fy<2004 else 1)
    got={k:[round(x/sc,1) for x in v] for k,v in got.items()}
    res[fy]=got
    print(fy, 'scale',sc, json.dumps(got))
json.dump(res,open('cfs.json','w'),indent=0)
json.dump(raw,open('cfs_raw.json','w'),indent=0)
