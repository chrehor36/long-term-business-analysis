# Arithmetic only: compounding of the filed organic components (price/mix, volume), 2023-2025 and H1 2026.
comp={'Total':[(7.7,-2.7),(2.7,-1.2),(0.1,-2.3)],'Self Care':[(7.1,1.3),(2.5,-0.6),(0.4,-3.4)],
      'Skin Health and Beauty':[(6.6,-4.8),(1.6,-3.5),(-0.9,-1.8)],'Essential Health':[(9.6,-6.0),(3.9,0.2),(0.5,-1.2)]}
for k,v in comp.items():
    p=1;q=1
    for a,b in v: p*=1+a/100; q*=1+b/100
    print(f'{k}: price/mix {100*(p-1):+.1f}%  volume {100*(q-1):+.1f}%  (2023-2025, three filed years)')
seg={'2023':{'SC':(2299,6451),'SHB':(679,4378),'EH':(1011,4615)},'2024':{'SC':(2173,6527),'SHB':(607,4240),'EH':(1162,4688)},'2025':{'SC':(2109,6378),'SHB':(477,4114),'EH':(1176,4632)}}
for y,d in seg.items():
    tot=sum(a for a,b in d.values())
    print(y, ' '.join(f'{k} {a/b:.1%} ({a/tot:.0%} of segment profit)' for k,(a,b) in d.items()), 'total', tot)
# operating income ex-impairment, as filed
oi={2021:2920,2022:2675,2023:2512,2024:1841+578,2025:2414+23}
for y,v in oi.items(): print('op income ex-impairment',y,v)
jnj={2008:16.05,2009:15.8,2010:14.6,2013:14.7,2015:13.507,2016:13.307,2018:13.853,2019:13.898,2020:14.053,2021:14.635,2022:14.950,2023:15.444,2024:15.455,2025:15.124}
print('sales $bn:',jnj)
print('2009->2025 CAGR', (15.124/15.8)**(1/16)-1)
