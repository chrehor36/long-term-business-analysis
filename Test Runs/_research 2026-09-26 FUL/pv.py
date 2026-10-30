# consolidated organic price and volume, % change on prior year, each read from the 10-K presenting that year as current (pv_tables.txt, pv_words.txt)
import json
PV={2005:(7.0,0.4),2006:(6.9,-8.8),2007:(2.8,-8.4),2008:(2.4,-6.4),2009:(3.3,-11.7),2010:(1.1,7.4),2011:(9.7,1.7),2012:(4.8,-0.6),
2013:(0.1,1.5),2014:(-0.4,3.5),2015:(0.5,4.5),2016:(-1.6,3.9),2017:(0.8,4.2),2018:(3.4,-0.3),2019:(1.0,-2.1),2020:(-0.6,-1.0),
2021:(5.6,9.6),2022:(15.4,1.2),2023:(2.9,-8.4),2024:(-2.6,1.6),2025:(0.8,-0.8)}
isp=json.load(open('is_parsed.json'))
p=v=1.0
for y,(a,b) in sorted(PV.items()):
    p*=1+a/100; v*=1+b/100
    r=isp[str(y)]; gm=r['gp']/r['rev']*100
    print(y,'price %+5.1f vol %+5.1f  cum price %5.1f%% cum vol %+5.1f%%  GM %4.1f%%'%(a,b,(p-1)*100,(v-1)*100,gm))
for a,b in [(2005,2012),(2013,2025),(2016,2025)]:
    pp=vv=1
    for y in range(a,b+1): pp*=1+PV[y][0]/100; vv*=1+PV[y][1]/100
    print(a,b,'price %+.1f%% vol %+.1f%%'%((pp-1)*100,(vv-1)*100))
