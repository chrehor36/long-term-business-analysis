# Offshore (Manufactured) Products segment, as filed (USD millions): revenue, operating income, total assets, goodwill
D={2014:(961.6,200.1,983.5,145.8),2015:(724.1,146.4,930.9,159.4),2016:(508.8,87.1,810.5,158.6),2017:(381.9,38.2,760.1,162.9),
2018:(394.1,38.9,683.3,162.5),2019:(402.9,36.0,677.0,162.8),2020:(340.3,-80.8,548.0,76.5),2021:(298.7,15.4,541.3,76.4),
2022:(381.7,45.3,556.8,79.3),2023:(381.7,56.3,521.9,79.9),2024:(397.9,65.3,510.4,69.7),2025:(431.1,69.2,546.8,70.5)}
CORP={2014:-68.2,2015:-47.2,2016:-48.5,2017:-52.9,2018:-54.5,2019:-45.2,2020:-35.7,2021:-32.3,2022:-40.6,2023:-41.1,2024:-22.8,2025:-46.8}
TOTREV={2014:1819.6,2015:1100.0,2016:694.4,2017:670.6,2018:1088.1,2019:1017.4,2020:638.1,2021:573.2,2022:737.7,2023:782.3,2024:692.6,2025:669.0}
GWIMP={2020:86.5}
for y,(r,oi,a,g) in D.items():
    share=r/TOTREV[y]; alloc=CORP[y]*share
    print(y,'margin %.1f%%  OI/assets %.1f%%  OI/(assets-gw) %.1f%%  after corp share %.1f%%'%(100*oi/r,100*oi/a,100*oi/(a-g),100*(oi+alloc)/(a-g)))
def avg(ys,adj=True):
    oi=sum(D[y][1]+(GWIMP.get(y,0) if adj else 0) for y in ys); ta=sum(D[y][2]-D[y][3] for y in ys); al=sum(CORP[y]*D[y][0]/TOTREV[y] for y in ys)
    return 100*oi/ta, 100*(oi+al)/ta
print('2014-2025 pre-tax on (assets-gw), goodwill impairment added back: %.1f%%, after revenue-share of corporate: %.1f%%'%avg(range(2014,2026)))
print('2017-2022: %.1f%% / %.1f%%'%avg(range(2017,2023)))
print('2023-2025: %.1f%% / %.1f%%'%avg(range(2023,2026)))
