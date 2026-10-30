import json
cpi={int(k):sum(v)/len(v) for k,v in json.load(open('cpi_bls.json')).items()}
# freight (commodity) revenue $M, carloads 000, fuel surcharge $M, operating ratio %, source vintage
S={1997:(9712,8453,None,87.4),1998:(9072,7998,None,95.4),1999:(9851,8556,None,82.0),2000:(10270,8901,None,82.3),2001:(10391,8916,None,80.7),2002:(10663,9131,None,79.0),
2003:(11041,9239,112,81.5),2004:(11692,9458,330,89.4),2005:(12856,9544,963,86.8),2006:(14791,9852,1619,81.5),2007:(15486,9733,1478,79.3),2008:(17118,9261,2323,77.3),2009:(13373,7786,605,76.0),
2010:(16069,8815,1200,70.6),2011:(18508,9072,2200,70.7),2012:(19686,9048,2600,67.8),2013:(20684,9022,2600,66.1),2014:(22560,9625,2800,63.5),2015:(20397,9062,1300,62.9),2016:(18601,8442,560,63.7),
2017:(19837,8588,966,61.8),2018:(21384,8908,1700,62.7),2019:(20243,8346,1600,60.6),2020:(18251,7753,1000,59.9),2021:(20244,8038,1700,57.2),2022:(23159,8169,3700,60.1),2023:(22571,8112,3000,62.3),2024:(22811,8334,2600,59.9),2025:(23220,8447,2300,59.8)}
base=2025
print('FY rev carl ARC ARCexfuel realARC(2025$) realARCexfuel OR')
out={}
for y,(r,c,f,o) in sorted(S.items()):
    arc=r/c*1000; ax=(r-f)/c*1000 if f is not None else None
    ra=arc*cpi[base]/cpi[y]; rx=ax*cpi[base]/cpi[y] if ax else None
    out[y]=(arc,ax,ra,rx)
    print(y,r,c,f,round(arc),round(ax) if ax else '', round(ra), round(rx) if rx else '', o)
def chg(a,b,i): return (out[b][i]/out[a][i]-1)*100
for a,b in ((2003,2025),(2005,2025),(2008,2025),(2014,2025),(2018,2025),(2019,2025),(2003,2014)):
    print(f'{a}-{b}: nominal ARC {chg(a,b,0):+.1f}%  ex-fuel nominal {chg(a,b,1):+.1f}%  real ex-fuel {chg(a,b,3):+.1f}%  real total {chg(a,b,2):+.1f}%  CPI {(cpi[b]/cpi[a]-1)*100:+.1f}%  carloads {(S[b][1]/S[a][1]-1)*100:+.1f}%')
print('1997-2025 real ARC total', round(chg(1997,2025,2),1), 'carloads', round((S[2025][1]/S[1997][1]-1)*100,1))
