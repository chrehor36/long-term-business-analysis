# Owner earnings, LSI Industries, $K. OCF, capex: filed cash-flow statements (latest filed vintage; equal to companyfacts).
# Depreciation: companyfacts Depreciation (plant only; amortization of acquired intangibles excluded, [E2-43]).
# SBC complete: stock option / stock compensation expense + deferred compensation plan (shares) + shares issued as compensation + ESPP discount, as filed.
OCF={2010:16729,2011:-3806,2012:24360,2013:8850,2014:11559,2015:20930,2016:18125,2017:21250,2018:11500,2019:11491,2020:29712,2021:28009,2022:-3863,2023:49588,2024:43392,2025:38118,2026:44148}
CAPEX={2010:6150,2011:4731,2012:3436,2013:7571,2014:5245,2015:4754,2016:10211,2017:6633,2018:3406,2019:2618,2020:2739,2021:2233,2022:2122,2023:3208,2024:5388,2025:3465,2026:5142}
DEP={2010:5294,2011:5288,2012:5174,2013:4702,2014:5411,2015:5804,2016:6171,2017:7005,2018:7462,2019:7500,2020:6000,2021:5200,2022:5300,2023:4900,2024:5000,2025:6700,2026:7900}
SO={2010:2633,2011:851,2012:410,2013:842,2014:1005,2015:1239,2016:2903,2017:3049,2018:3012,2019:981,2020:599,2021:1977,2022:3288,2023:3698,2024:3814,2025:4164,2026:3946}
DC={2010:-49,2011:126,2012:124,2013:169,2014:99,2015:-761,2016:491,2017:455,2018:359,2019:266,2020:473,2021:1534,2022:3610,2023:2017,2024:1875,2025:1943,2026:1884}
SC={2010:46,2011:41,2012:48,2013:57,2014:193,2015:191,2016:248,2017:409,2018:319,2019:355,2020:300,2021:315,2022:300,2023:368,2024:450,2025:450,2026:360}
ES={2023:142,2024:194,2025:218,2026:335}
import json
Y=sorted(OCF); rows={}
print('FY    OCF    SBCcomplete  capex  dep   OE_capex  OE_dep')
for y in Y:
    sbc=SO[y]+DC[y]+SC[y]+ES.get(y,0)
    a=OCF[y]-sbc-CAPEX[y]; b=OCF[y]-sbc-DEP[y]
    rows[y]=(a,b,sbc)
    print(f'{y} {OCF[y]:7} {sbc:7} {CAPEX[y]:7} {DEP[y]:6} {a:8} {b:8}')
cap=785841
print('\nWindows ending FY2026 (mean OE, $K) and yield on cap $785.8M:')
res=[]
for n in range(2,18):
    ys=[y for y in Y if y>2026-n]
    ma=sum(rows[y][0] for y in ys)/n; mb=sum(rows[y][1] for y in ys)/n
    res+= [ma,mb]
    print(f'{n:2}y FY{ys[0]}-FY2026  capex end {ma:8.0f}  dep end {mb:8.0f}  yield {100*ma/cap:5.2f}% / {100*mb/cap:5.2f}%')
print('\nAll windows of 3+ years ending FY2026: min %.0f max %.0f'%(min(res[2:]),max(res[2:])))
# every window of length>=3 anywhere, both ends
allw=[]
for i,a0 in enumerate(Y):
    for b0 in Y:
        if b0-a0>=2:
            ys=[y for y in Y if a0<=y<=b0]
            for k in (0,1): allw.append((sum(rows[y][k] for y in ys)/len(ys),a0,b0,k))
allw.sort()
print('Every window of 3+ years anywhere FY2010-FY2026, both ends: min %.0f (FY%d-FY%d) max %.0f (FY%d-FY%d)'%(allw[0][0],allw[0][1],allw[0][2],allw[-1][0],allw[-1][1],allw[-1][2]))
json.dump({str(k):v for k,v in rows.items()},open('oe_rows.json','w'))

# screen reproduction: 5y FY2021-FY2025, SBC tag only, capex end and D&A end
TAG={2021:1977,2022:3288,2023:3698,2024:3814,2025:4164}
DA={2021:8114,2022:10118,2023:9664,2024:9999,2025:12575}
ys=range(2021,2026)
print('screen-style 5y FY2021-25, tag SBC: capex end %.0f, D&A end %.0f'%(sum(OCF[y]-TAG[y]-CAPEX[y] for y in ys)/5, sum(OCF[y]-TAG[y]-DA[y] for y in ys)/5))
ys=range(2023,2026)
print('screen-style 3y FY2023-25, tag SBC: capex end %.0f, D&A end %.0f'%(sum(OCF[y]-TAG[y]-CAPEX[y] for y in ys)/3, sum(OCF[y]-TAG[y]-DA[y] for y in ys)/3))
