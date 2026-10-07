import json
cpi={int(k):sum(v)/len(v) for k,v in json.load(open('cpi_bls.json')).items()}
# ARC by group, $ per car, fuel surcharge included (FY2020 10-K for 2018; FY2025 10-K for 2025)
a18={'Grain & grain products':3811,'Fertilizer':3303,'Food & refrigerated':5171,'Coal & renewables':2216,'Industrial chemicals & plastics':3049,'Metals & minerals':3067,'Forest products':5025,'Energy & specialized markets':3772,'Automotive':2438,'Intermodal':1276,'Average':2400}
a25={'Grain & grain products':4461,'Fertilizer':3970,'Food & refrigerated':6233,'Coal & renewables':2241,'Industrial chemicals & plastics':3568,'Metals & minerals':2935,'Forest products':6369,'Energy & specialized markets':4446,'Automotive':3024,'Intermodal':1380,'Average':2749}
c18={'Grain & grain products':723,'Fertilizer':194,'Food & refrigerated':206,'Coal & renewables':1176,'Industrial chemicals & plastics':599,'Metals & minerals':822,'Forest products':241,'Energy & specialized markets':565,'Automotive':891,'Intermodal':3491,'Average':8908}
c25={'Grain & grain products':880,'Fertilizer':216,'Food & refrigerated':163,'Coal & renewables':797,'Industrial chemicals & plastics':704,'Metals & minerals':747,'Forest products':203,'Energy & specialized markets':587,'Automotive':793,'Intermodal':3357,'Average':8447}
k=cpi[2025]/cpi[2018]
print(f'CPI-U 2018 {cpi[2018]:.3f} 2025 {cpi[2025]:.3f} (11 months; Oct 2025 not published) ratio {k:.4f}')
print('fuel surcharge revenue 2018 $1.7bn, 2025 $2.3bn (both years include it)')
for g in a18:
    n=a25[g]/a18[g]-1; r=a25[g]/a18[g]/k-1
    print(f'{g:35s} {a18[g]:>6} {a25[g]:>6} nominal {n*100:+6.1f}% real {r*100:+6.1f}%  carloads {c18[g]:>5}->{c25[g]:>5} {((c25[g]/c18[g])-1)*100:+6.1f}%')
# fixed-weight (2018 carloads) index removes mix
num=sum(a25[g]*c18[g] for g in a18 if g!='Average'); den=sum(a18[g]*c18[g] for g in a18 if g!='Average')
print(f'fixed-2018-mix ARC index nominal {(num/den-1)*100:+.1f}%  real {(num/den/k-1)*100:+.1f}%')
# 2014 -> 2025 comparable groups
k2=cpi[2025]/cpi[2014]
for g,x,y in (('Coal',2334,2241),('Intermodal',1250,1380),('Automotive',2602,3024)):
    print(f'2014->2025 {g}: {x}->{y} nominal {(y/x-1)*100:+.1f}% real {(y/x/k2-1)*100:+.1f}%')
print('carloads 2014 total 9,625 coal 1,768 ex-coal 7,857; 2025 total 8,447 coal 797 ex-coal 7,650:', f'{(7650/7857-1)*100:+.1f}% ex-coal')
