from oc import rows
import statistics as st
SH=45.008622; PRICE=103.88; ND=2002.339-42.826; MCAP=PRICE*SH; EV=MCAP+ND
def pv(c,g,r,n=10):
    s=0; x=c
    for t in range(1,n+1):
        x=x*(1+g); s+=x/(1+r)**t
    return s + x/r/(1+r)**n
def irr(c,g,price):
    lo,hi=0.0001,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c,g,m)>price: lo=m
        else: hi=m
    return m
def avg(k,a,b): return st.mean(rows[y][k] for y in range(a,b+1))
print('mcap %.1f  net debt %.1f  EV %.1f'%(MCAP,ND,EV))
R=0.0556
bases={}
for lab,(a,b) in {'cycle 2019-2024':(2019,2024),'literal 2021-2025':(2021,2025),'2019-2025':(2019,2025)}.items():
    bases[lab]=dict(m_pre=avg('oc_m_pre_int',a,b), all_pre=avg('oc_allpre_pre_int',a,b), allacq_pre=avg('oc_all_pre_int',a,b),
                    m_post=avg('oc_m',a,b), all_post=avg('oc_all_pre',a,b), allacq_post=avg('oc_all',a,b))
    print(lab, {k:round(v,1) for k,v in bases[lab].items()})
def case(lab,c_pre,c_post,g):
    v=pv(c_pre,g,R); ps=(v-ND)/SH; ve=pv(c_post,g,R)/SH
    f=(pv(c_pre,g,0.10)-ND)/SH; fe=pv(c_post,g,0.10)/SH
    i=irr(c_pre,g,EV); ie=irr(c_post,g,MCAP) if c_post>0 else float('nan')
    print('%-55s base pre-int %6.1f g %+.1f%% | value/sh %7.2f (eq-only %7.2f) | at 10%%: %7.2f (eq-only %7.2f) | return at price %.1f%% (eq-only %.1f%%)'%(lab,c_pre,100*g,ps,ve,f,fe,100*i,100*ie))
    return ps,ve,f,fe
import sys
for lab in bases:
    B=bases[lab]; print('==',lab)
    top=case('TOP maintenance-only, no growth',B['m_pre'],B['m_post'],0.0)
    bot=case('BOTTOM all spending (programme), organic -2.0%',B['all_pre'],B['all_post'],-0.020)
    case('beside: maintenance-only, organic -2.0%',B['m_pre'],B['m_post'],-0.020)
    case('beside: all spending, no growth',B['all_pre'],B['all_post'],0.0)
    case('beside: default pair, acquisitions deducted, total growth',B['allacq_pre'],B['allacq_post'],0.0)
    print('   fair (avg of ends at 10%%): all-equity %.2f  equity-only %.2f ; width top/bottom %.2f'%((top[2]+bot[2])/2,(top[3]+bot[3])/2, top[0]/bot[0] if bot[0]>0 else float('inf')))
# total growth between halves 2016-2020 vs 2021-2025 (maintenance, pre-int) for the default pair, shown
h1=avg('oc_m_pre_int',2016,2020); h2=avg('oc_m_pre_int',2021,2025); print('halves maint pre-int',round(h1,1),round(h2,1),'growth/yr %.1f%%'%(100*((h2/h1)**(1/5)-1)))
h1=avg('oc_all_pre_int',2016,2020); h2=avg('oc_all_pre_int',2021,2025); print('halves all-incl-acq pre-int',round(h1,1),round(h2,1))
