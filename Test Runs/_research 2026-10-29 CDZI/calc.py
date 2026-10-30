# CDZI run 2026-10-29: COMPUTATION, NOT A CLEARANCE. USD millions. Sources: 10-K cash-flow statements
# (accessions in the run file) and companyfacts; cash interest from each 10-K's long-term debt note.
yrs=[2021,2022,2023,2024,2025]
ocf=[-15.274,-18.599,-20.924,-21.532,-18.930]
sbc=[4.747,1.876,1.496,4.605,5.299]
capex=[22.908,3.376,5.787,0.934,7.576]
deposit=[0,0,0,0,5.000]          # 2025 pipe purchase option deposit (investing)
dep=[0.423,0.654,1.247,1.214,1.264]
cashint=[2.6,3.5,1.6,1.5,1.7]
sov=0.0537; floor=0.10
shares=84.677
netdebt=86.978+0.007+29.446-5.319   # 2026-06-30 10-Q: LT debt + current + related-party lease obligation - cash
pref=2300*25000/1e6                  # Series A liquidation preference
avg=lambda x:sum(x)/len(x)
allsp=[o-s-c-d for o,s,c,d in zip(ocf,sbc,capex,deposit)]
allsp_bi=[a+i for a,i in zip(allsp,cashint)]
mnt=[o-s-d for o,s,d in zip(ocf,sbc,dep)]
mnt_bi=[m+i for m,i in zip(mnt,cashint)]
for n,v in [('all-spending, after cash interest',allsp),('all-spending, before interest',allsp_bi),('maintenance (dep), after cash interest',mnt),('maintenance (dep), before interest',mnt_bi)]:
    print(f'{n:42s}',[round(x,3) for x in v],'avg',round(avg(v),3))
print('net debt',round(netdebt,3),'preferred',pref)
top=avg(mnt_bi)/sov; bot=avg(allsp_bi)/sov
print('ALL-EQUITY range EV: top',round(top,1),'bottom',round(bot,1))
for lab,extra in [('',0),(' less preferred',pref)]:
    print(' per share'+lab, round((top-netdebt-extra)/shares,2), round((bot-netdebt-extra)/shares,2))
fair_ev=(avg(mnt_bi)/floor+avg(allsp_bi)/floor)/2
print('fair EV at 10%',round(fair_ev,1),'per share',round((fair_ev-netdebt)/shares,2),'less pref',round((fair_ev-netdebt-pref)/shares,2))
eq_top=avg(mnt)/sov; eq_bot=avg(allsp)/sov
print('EQUITY-ONLY range per share',round(eq_top/shares,2),round(eq_bot/shares,2),'fair',round((avg(mnt)/floor+avg(allsp)/floor)/2/shares,2))
price=4.72
print('market cap',round(price*shares,1),'EV',round(price*shares+netdebt,1),'EV+pref',round(price*shares+netdebt+pref,1))
print('owner-cash yield at price (all-equity, maintenance):',round(avg(mnt_bi)/(price*shares+netdebt)*100,2),'%')
