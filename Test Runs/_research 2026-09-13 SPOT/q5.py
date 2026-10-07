import json
cap_usd=525.75*205584205; fx=1.1592; cap=cap_usd/fx/1e6; sh=205584205
liq=9388; tme=1118; lease=466
ev=cap-liq-tme+lease
sov=0.0383; floor=0.10
cons = {
 '10y low':166,'10y high':497,'5y low tax-norm':444,'5y low':586,'5y high':877,
 '3y low':1193,'3y high':1536,'2y low tax-norm':1564,'2y low':1920,'2y high':2186,'TTM Jun-2026 high':2959}
intr={'10y':67,'5y':122,'3y':190,'2y':229,'TTM':215}
print(f'cap EUR {cap:,.0f}M  EV {ev:,.0f}M  price EUR {525.75/fx:.2f}')
rows=[]
for k,oe in cons.items():
    y=oe/cap
    g_floor=(floor-y)/(1+y); g_sov=(sov-y)/(1+y)
    v_sov=oe/sov/sh*1e6*fx; v_floor=oe/floor/sh*1e6*fx
    w=k.split()[0]; ex=oe-intr.get(w,0); yev=ex/ev
    rows.append((k,oe,round(y*100,2),round((y-sov)*100,2),round(g_sov*100,1),round(g_floor*100,1),round(v_sov),round(v_floor),round(yev*100,2)))
    print(rows[-1])
json.dump({'cap':cap,'ev':ev,'rows':rows},open('q5_out.json','w'),indent=1)
