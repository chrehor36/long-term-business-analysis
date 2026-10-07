import json
x=json.load(open('xb_rows.json')); g=lambda k,y: x[k].get(str(y))
M=lambda v: None if v is None else v/1e6
sales={2004:236.047,2005:273.533,2006:321.054,2007:389.560,2008:446.124}
cogs={2004:113.988,2005:115.827,2006:143.855,2007:160.137,2008:191.915}
roy={2002:5.5,2003:10.4,2004:20.9,2005:27.1,2006:31.4,2007:35.6,2008:37.3,2009:35.5,2010:40.2,2011:51.3,2012:58.8,2013:40.5,2014:35.6,2015:33.8,2016:37.8,2017:39.6,2018:48.9,2019:53.0,2020:41.1,2021:69.0,2022:87.0,2023:103.8,2024:117.8,2025:121.7}
ap={2004:21.8,2005:40.8,2006:46.5,2007:58.5,2008:65.8,2009:55.8,2010:69.2,2011:127.8,2012:132.7,2013:94.0,2014:86.7,2015:83.8,2016:99.0,2017:123.7,2018:139.7,2019:144.6,2020:91.7,2021:171.8,2022:212.4,2023:261.3,2024:280.5,2025:294.7}
burb={2002:41,2003:56,2004:62,2005:60,2006:57,2007:54,2008:56,2009:57,2010:53,2011:50,2012:46,2013:23,2014:0}
rows=[]
print('FY | net sales | growth | gross margin | royalty % | promotion and advertising % | operating margin | op. income on net operating capital | Burberry share of sales')
prev=None
for y in range(2004,2026):
    s=sales.get(y) or M(g('Rev',y)); gp=(s-cogs[y]) if y in cogs else M(g('GP',y))
    oi=M(g('OpInc',y)); 
    if y==2012: oi_x=oi-198.838
    else: oi_x=oi
    cap=None
    if g('EqTot',y) is not None:
        debt=sum(M(g(k,y)) or 0 for k in ('LTD','LTDc','STB'))
        cap=M(g('EqTot',y))+debt-(M(g('Cash',y)) or 0)-(M(g('STI',y)) or 0)
    gr='' if prev is None else '%+.1f%%'%(100*(s/prev-1)); prev=s
    r=f"{y} | {s:.1f} | {gr} | {100*gp/s:.1f}% | {100*roy[y]/s:.1f}% | {100*ap[y]/s:.1f}% | {'' if oi is None else '%.1f%%'%(100*oi_x/s)}{' (ex $198.8M Burberry gain)' if y==2012 else ''} | {'' if (cap is None or oi is None) else '%.1f%% on %.0f'%(100*oi_x/cap,cap)} | {str(burb.get(y,''))+('%' if y in burb else '')}"
    print(r)
