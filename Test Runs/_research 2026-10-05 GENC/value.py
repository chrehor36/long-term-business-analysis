r=0.0563; sh=14.657702
t=0.222
op={2016:7816,2017:10236,2018:13715,2019:9470,2020:5536,2021:701,2022:4167,2023:13425,2024:13687,2025:14018}
da={2016:1397,2017:1128,2018:1380,2019:1600,2020:1643,2021:2591,2022:2823,2023:2834,2024:2602,2025:2356}
cx={2016:306,2017:1624,2018:3550,2019:2104,2020:1595,2021:2659,2022:4516,2023:2746,2024:840,2025:1963}
wc={2016:-1719,2017:-2968,2018:-10445,2019:-7351,2020:6281,2021:1303,2022:-14169,2023:-12525,2024:-3325,2025:5341}
acq={2021:13777}
rate=lambda y: 0.36 if y<=2017 else (0.245 if y==2018 else t)
oc={};dv={}
for y in op:
    nopat=op[y]*(1-rate(y))
    dv[y]=nopat+da[y]-cx[y]
    oc[y]=dv[y]+wc[y]-acq.get(y,0)
    print(y,'NOPAT %.0f  dep-variant %.0f  WC %d  acq %d  owner cash %.0f'%(nopat,dv[y],wc[y],acq.get(y,0),oc[y]))
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
f5=range(2021,2026); t10=range(2016,2026)
print('5y avg owner cash (all capital) %.0f; ex-acq %.0f; 10y avg %.0f; 10y ex-acq %.0f'%(avg(oc,f5),avg(oc,f5)+13777/5,avg(oc,t10),avg(oc,t10)+1377.7))
print('5y avg dep-variant %.0f; 10y %.0f'%(avg(dv,f5),avg(dv,t10)))
g=(dv[2025]/dv[2016])**(1/9)-1; print('dep-variant growth 2016->2025 %.2f%%'%(100*g))
def pv(c0,g,r,n=10):
    v=0;c=c0
    for i in range(1,n+1):
        c*=1+g; v+=c/(1+r)**i
    return v + (c/r)/(1+r)**n
base=avg(dv,f5)
print('op value dep-variant no-growth %.0f, shown growth %.0f'%(base/r, pv(base,g,r)))
cash=26258; sec=137911; cost=136069; utb=2582
taxu=(sec-cost)*t
full=cash+sec-taxu-utb; net=full-15000
print('securities full %.0f (%.2f/sh) net of reserve %.0f (%.2f/sh)'%(full,full/sh,net,net/sh))
low=net+avg(oc,f5)/r; high=full+pv(base,g,r)
print('LOW %.0f = %.2f/sh ; HIGH %.0f = %.2f/sh ; ratio %.2f'%(low,low/sh,high,high/sh,high/low))
# ratio on operating part alone
print('op part only: low %.0f high %.0f'%(avg(oc,f5)/r, pv(base,g,r)))
# central case pre-tax expected return at price
P=17.64*sh; print('market cap %.0f'%P)
opinc10=avg(op,t10); dacx=avg(da,t10)-avg(cx,t10); 
rev25=115437; capint=72847/rev25
gc=0.03; wcneed=capint*gc*rev25
opcash_pt=opinc10+dacx-wcneed
print('10y avg op income %.0f, D&A-capex %.0f, WC need at 3%% growth %.0f -> central pre-tax op owner cash %.0f'%(opinc10,dacx,wcneed,opcash_pt))
y_sec=0.045
port=(cash+sec)*y_sec
print('portfolio pre-tax income at 4.5%%: %.0f'%port)
er=(port+opcash_pt)/P + gc*(P-(cash+sec))/P
print('expected pre-tax return at $17.64: %.2f%%'%(100*er))
# fair price, securities at face (assume they can be had at face) : P = sec_face + op value at 10% with g
opval10=opcash_pt/(0.10-gc)
fair_face=(cash+sec-taxu-utb)+opval10
fair_trap=port/0.10+opval10
print('op value at 10%% floor %.0f (%.2f/sh)'%(opval10,opval10/sh))
print('FAIR (securities at face) %.0f = %.2f/sh'%(fair_face,fair_face/sh))
print('FAIR (securities as trapped 4.5%% income) %.0f = %.2f/sh'%(fair_trap,fair_trap/sh))
print('CHEAP = 2/3 of low %.2f'%(2/3*low/sh))
