# Owner earnings from the filed cash-flow statements (no net-income proxy).
# capex = Purchases of property and equipment + Deposits paid for property and equipment (both filed lines)
# FY2017-18: 2019 S-1; FY2019-20: 2021 424B4; FY2021-25: 10-Ks. $ thousands.
rows={2017:(1002,0,5510,3119),2018:(2717,0,22149+9759,3960),2019:(-32,0,32551+2260,5953),2020:(14547,0,29536+6946,8569),
2021:(8679,2026,4175+8206,10044),2022:(29474,2047,2657+12090,10405),2023:(53379,770,2835+6309,10783),
2024:(47982,2065,934+3134,10675),2025:(33815,1182,756+3749,10891)}
cap=1058175
print('FY    OCF    SBC  capex   D&A   OE_capex  OE_da')
oe={}
for y,(o,s,c,d) in rows.items():
    oe[y]=(o-s-c,o-s-d); print(y,o,s,c,d,oe[y][0],oe[y][1])
ys=sorted(rows)
print('\nwindows ending FY2025')
lo=1e18;hi=-1e18
for n in range(1,10):
    w=ys[-n:]
    a=sum(oe[y][0] for y in w)/n; b=sum(oe[y][1] for y in w)/n
    print(n,'yrs',w[0],'-',w[-1],'capex end %.1f'%(a/1e3),'D&A end %.1f'%(b/1e3),'yield %.2f%% / %.2f%%'%(100*a/cap,100*b/cap))
    if n>=3: lo=min(lo,a,b); hi=max(hi,a,b)
print('range, windows >=3y ending FY2025: %.1f to %.1f  = %.2f%% to %.2f%% of cap'%(lo/1e3,hi/1e3,100*lo/cap,100*hi/cap))
lo2=1e18;hi2=-1e18
for n in range(3,10):
    for i in range(0,len(ys)-n+1):
        w=ys[i:i+n]
        for k in (0,1):
            m=sum(oe[y][k] for y in w)/n
            if m<lo2: lo2=m;wl=(w[0],w[-1],k)
            if m>hi2: hi2=m;wh=(w[0],w[-1],k)
print('every window >=3y anywhere: low %.1f %s high %.1f %s'%(lo2/1e3,wl,hi2/1e3,wh))
# normalisation: FY2023-24 without the working-capital release? report OCF less working-capital lines separately
print('\nscreen reproduction')
t=[2021,2022,2023,2024,2025]
print('5y D&A end, tags only', (sum(rows[y][0]-rows[y][1]-rows[y][3] for y in t)/5)/1e3)
tagcap={2023:2835,2024:934,2025:756}
print('3y capex end, tagged capex only', (sum(rows[y][0]-rows[y][1]-tagcap[y] for y in tagcap)/3)/1e3)
print('3y capex end, with deposits', (sum(oe[y][0] for y in tagcap)/3)/1e3)
