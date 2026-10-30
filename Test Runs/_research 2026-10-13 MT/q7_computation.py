# COMPUTATION, NOT A CLEARANCE (the file closed at Q2). Figures in $ millions from the 20-F cash flow statements.
yrs=list(range(2016,2026))
ocf ={2016:2708,2017:4563,2018:4196,2019:6017,2020:4082,2021:9905,2022:10203,2023:7645,2024:4852,2025:4808}
capex={2016:2444,2017:2819,2018:3305,2019:3572,2020:2439,2021:3008,2022:3468,2023:4613,2024:4405,2025:4337}
da  ={2016:2721,2017:2768,2018:2799,2019:3067,2020:2960,2021:2523,2022:2580,2023:2675,2024:2632,2025:2945}
lease={2016:0,2017:0,2018:0,2019:320,2020:242,2021:199,2022:185,2023:253,2024:224,2025:234}  # pre-2019 finance-lease principal sits inside debt repayments; not separable
nci ={2016:61,2017:141,2018:119,2019:129,2020:181,2021:260,2022:331,2023:162,2024:187,2025:121}
intpaid={2019:723,2020:604,2021:479,2022:440,2023:788,2024:799,2025:828}
intrec ={2019:118,2020:69,2021:73,2022:178,2023:553,2024:358,2025:308}
sales={2016:56791,2017:68679,2018:76033,2019:70615,2020:53270,2021:76571,2022:79844,2023:68275,2024:62441,2025:61352}
# net purchases of businesses and joint-venture stakes, net of disposals (20-F investing lines; see run file)
np_={2020:-98,2021:-2897,2022:939,2023:2343,2024:1241,2025:70}
T=0.2387  # Luxembourg statutory rate from 2025 (20-F), used for the interest tax shield
allsp={y:ocf[y]-capex[y]-lease[y]-nci[y] for y in yrs}
maint={y:ocf[y]-da[y]-lease[y]-nci[y] for y in yrs}
addb={y:(intpaid[y]-intrec[y])*(1-T) for y in intpaid}
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
print('year  allspend  maint  interest_addback  allsp/sales  maint/sales')
for y in yrs: print(y, allsp[y], maint[y], round(addb.get(y,0)), '%.1f%%'%(100*allsp[y]/sales[y]), '%.1f%%'%(100*maint[y]/sales[y]))
cyc=range(2020,2026); prev=range(2016,2021); lit=range(2021,2026)
for name,ys in [('cycle 2020-2025',cyc),('literal 2021-2025',lit),('ten-year 2016-2025',yrs)]:
    print(name,'allsp %.0f maint %.0f addback %.0f sales %.0f'%(avg(allsp,ys),avg(maint,ys),avg(addb,[y for y in ys if y in addb]),avg(sales,ys)))
gm=(avg(maint,cyc)/avg(maint,prev))**(1/4.5)-1
ga=(avg(allsp,cyc)/avg(allsp,prev))**(1/4.5)-1
gs=(avg(sales,cyc)/avg(sales,prev))**(1/4.5)-1
print('growth between cycle averages: maint %.1f%%  allsp %.1f%%  sales %.2f%%'%(100*gm,100*ga,100*gs))
mx=max(maint[y]/sales[y] for y in yrs)
print('max maint share of sales %.1f%%; base*(1+gm)^10 / sales = %.1f%%'%(100*mx,100*avg(maint,cyc)*(1+gm)**10/avg(sales,cyc)))
def pv(base,g,r):
    v=0; c=base
    for t in range(1,11):
        c=c*(1+g); v+=c/(1+r)**t
    v+= c/r/(1+r)**10   # zero nominal growth after year ten
    return v
R=0.056; ND=9500; SH=754.041698; P=63.47
def report(label,top_base,top_g,bot_base,bot_g):
    out={}
    for r in (R,0.10):
        a=pv(top_base,top_g,r); b=pv(bot_base,bot_g,r)
        out[r]=(a,b)
    a,b=out[R]; print(label)
    print('   at 5.60%%: ends %.0f and %.0f; per share %.2f and %.2f; width %.2f to 1'%(a,b,(a-ND)/SH if 'all' in label else a/SH,(b-ND)/SH if 'all' in label else b/SH, max(a,b)/min(a,b)))
    a10,b10=out[0.10]
    fp=((a10+b10)/2-(ND if 'all' in label else 0))/SH
    print('   at 10%%: ends %.0f and %.0f; fair price per share %.2f'%(a10,b10,fp))
    # floor test: implied return at price for each end
    ev=P*SH+(ND if 'all' in label else 0)
    for nm,base,g in (('end1',top_base,top_g),('end2',bot_base,bot_g)):
        lo,hi=0.0001,0.5
        for _ in range(100):
            mid=(lo+hi)/2
            if pv(base,g,mid)>ev: lo=mid
            else: hi=mid
        print('   %s implied return at the price %.2f%%'%(nm,100*lo))
c_p=avg(np_,cyc); print('avg net purchases 2020-2025 %.0f'%c_p)
c_m=avg(maint,cyc)-c_p; c_a=avg(allsp,cyc)-c_p; c_i=avg(addb,cyc)
print('market value of equity %.0f; plus net debt %.0f'%(P*SH,P*SH+ND))
report('CENTRAL all-equity, cycle base: maintenance-only no-growth vs all-spending at sales growth', c_m+c_i,0.0, c_a+c_i,gs)
report('equity-only, cycle base', c_m,0.0, c_a,gs)
l_p=avg(np_,lit); print('avg net purchases 2021-2025 %.0f'%l_p)
l_m=avg(maint,lit)-l_p; l_a=avg(allsp,lit)-l_p; l_i=avg(addb,lit)
report('beside: all-equity, literal window 2021-2025', l_m+l_i,0.0, l_a+l_i,gs)
t_m=avg(maint,yrs); t_a=avg(allsp,yrs); t_i=avg(addb,[y for y in yrs if y in addb])
report('beside: all-equity, ten-year 2016-2025', t_m+t_i,0.0, t_a+t_i,gs)
report('beside: all-equity, purchases left out (organic pair; the filer reports no organic growth, so sales growth stands in)', avg(maint,cyc)+c_i,0.0, avg(allsp,cyc)+c_i,gs)
report('beside: all-equity, PG default pair (all spending deducted, no-growth vs sales growth)', c_a+c_i,0.0, c_a+c_i,gs)
# literal window with its own shown decline carried as the bottom (specific (b)), beside only
gl=(maint[2025]/maint[2021])**(1/4)-1
gla=(allsp[2025]/allsp[2021])**(1/4)-1
print('literal window shown growth: maint %.1f%%, all-spending %.1f%%'%(100*gl,100*gla))
report('beside: all-equity, literal window, shown decline carried as the bottom', l_m+l_i,0.0, l_m+l_i,gl)
