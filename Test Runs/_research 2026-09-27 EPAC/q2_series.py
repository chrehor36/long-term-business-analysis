# Q2 series from the segment notes of each 10-K (thousands where given; $M otherwise). Newest vintage per year.
# Industrial segment (the Enerpac hydraulic-tools business, restated perimeter from the FY2009 10-K on)
IND={2007:(278732,86344,180652),2008:(374498,113808,251384),2009:(286851,67451,190397),2010:(299983,66344,241036),
2011:(393013,98415,263680),2012:(419295,114777,268735),2013:(422620,117644,280110),2014:(413902,120250,307058),
2015:(402464,105652,293738),2016:(360000,79773,308222),2017:(380000,84936,329134)}
# 2016 and 2017 sales from MD&A in $M (360, 380); op profit and assets from the segment note
# old perimeter (FY2007 10-K, Industrial incl. joint integrity): FY2005 218,625/54,565/213,957 ; FY2006 324,688/85,511/332,428
OLD={2005:(218625,54565,213957),2006:(324688,85511,332428)}
ITS={2016:(588207,119922,None),2017:(552582,95825,599321),2018:(591085,99432,589926),2019:(609515,101411,553615),2020:(454863,65549,592086),
2021:(493125,81683,641256),2022:(527342,78735,618412),2023:(555178,135883,632113),2024:(571153,153105,613797),2025:(595825,163869,672123)}
print('INDUSTRIAL SEGMENT (Enerpac hydraulic tools), segment note of each 10-K')
print(' FY    sales   op.profit  margin  seg.assets  pre-tax on avg seg assets (incl. goodwill)')
for y,(s,o,a) in sorted(OLD.items()):
    print(' %d %8.1f %8.1f %6.1f%% %9.1f   (old perimeter, with joint integrity)'%(y,s/1e3,o/1e3,100*o/s,a/1e3))
p=None
for y in sorted(IND):
    s,o,a=IND[y]; r=(o/((a+p)/2)) if p else o/a
    print(' %d %8.1f %8.1f %6.1f%% %9.1f   %5.1f%%%s'%(y,s/1e3,o/1e3,100*o/s,a/1e3,100*r,'' if p else ' (on year-end assets)'))
    p=a
tot_s=sum(v[0] for v in IND.values()); tot_o=sum(v[1] for v in IND.values())
print(' FY2007-FY2017 cumulative margin %.1f%%'%(100*tot_o/tot_s))
print('\nIT&S SEGMENT (Industrial + Hydratight services from FY2018 reorganisation; corporate allocation widened FY2023)')
p=None
for y in sorted(ITS):
    s,o,a=ITS[y]
    r=(o/((a+p)/2)) if (a and p) else None
    print(' %d %8.1f %8.1f %6.1f%% %9s   %s'%(y,s/1e3,o/1e3,100*o/s,('%.1f'%(a/1e3)) if a else '-',('%5.1f%%'%(100*r)) if r else '-'))
    p=a
