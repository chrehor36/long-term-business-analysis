# technology segment (FY2009-FY2023, as filed in each year's 10-K segment note) and continuing operations (FY2023 recast, FY2024-FY2026)
# $M: net sales (or total revenues), cost of sales, operating income (segment earnings before FY2015)
rows=[
('FY2009',643.6,None,10.8,'k_2009 Total revenues, segment earnings (gross presentation as first filed)'),
('FY2010',511.9,410.9,14.6,'k_2012 restated net presentation'),
('FY2011',680.7,551.9,26.9,'k_2012'),
('FY2012',792.4,645.6,31.6,'k_2012'),
('FY2013',943.2,767.4,46.5,'k_2013 (earnings before tax; interest 0.1)'),
('FY2014',1021.4,827.9,51.3,'k_2014'),
('FY2015',1108.4,887.7,61.0,'k_2015'),
('FY2016',1169.1,931.8,63.7,'k_2016'),
('FY2017',1294.9,1025.2,68.9,'k_2017'),
('FY2018',1369.5,1082.2,62.4,'k_2018'),
('FY2019',1329.5,1034.9,56.7,'k_2021'),
('FY2020',1530.1,1189.6,62.2,'k_2021'),
('FY2021',1508.0,1161.7,75.7,'k_2021'),
('FY2022',1733.0,1324.9,109.0,'k_2023'),
('FY2023',2015.2,1540.8,140.1,'k_2023 technology segment'),
('FY2023c',2016.1,2016.1-475.0,138.6,'8-K 2026-01-26 recast, continuing'),
('FY2024c',2178.2,1666.5,133.8,'10-K FY2026, continuing'),
('FY2025c',2000.2,1488.0,99.7,'10-K FY2026, continuing'),
('FY2026c',2442.5,1826.5,166.1,'10-K FY2026, continuing'),
]
for y,s,c,o,src in rows:
    gm='%.1f%%'%(100*(s-c)/s) if c else '-'
    print(f'{y:8} sales {s:8.1f}  GM {gm:>6}  OI {o:6.1f}  OM {100*o/s:4.1f}%   {src}')
print('gross billings FY2024 3,329.8 FY2025 3,280.4 FY2026 3,838.5; GP/billings', ['%.1f%%'%(100*g/b) for g,b in ((511.7,3329.8),(512.1,3280.4),(616.1,3838.5))], 'OI/billings', ['%.1f%%'%(100*g/b) for g,b in ((133.8,3329.8),(99.7,3280.4),(166.1,3838.5))])
import statistics as st
om=[o/s for y,s,c,o,src in rows if y not in('FY2023',)]
print('mean OM FY2010-FY2021', '%.1f%%'%(100*st.mean([o/s for y,s,c,o,src in rows if y in [f'FY{k}' for k in range(2010,2022)]])))
print('mean OM FY2022-FY2026', '%.1f%%'%(100*st.mean([o/s for y,s,c,o,src in rows if y in ('FY2022','FY2023c','FY2024c','FY2025c','FY2026c')])))
# continuing operating capital
for y,eq,cash,gw,oi in (('FY2025',970.7-177.2,389.4,202.9+82.0,99.7),('FY2026',1069.0,410.8,202.9+61.3,166.1)):
    print(y,'equity(continuing) %.1f cash %.1f opcap %.1f OI/opcap %.1f%%  tangible opcap %.1f OI/tangible %.1f%%'%(eq,cash,eq-cash,100*oi/(eq-cash),eq-cash-gw,100*oi/(eq-cash-gw)))
