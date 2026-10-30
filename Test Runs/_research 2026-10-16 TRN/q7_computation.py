# COMPUTATION, NOT A CLEARANCE. Q7 range and fair price for TRN, from filed cash-flow lines (USD millions).
# Sources: 10-K FY2020 (0000099780-21-000012) for 2018-2020; 10-K FY2022 (0000099780-23-000013) for 2021-2022;
# 10-K FY2025 (0000099780-26-000014) for 2023-2025; segment D&A from the segment notes of the same filings.
yrs=[2018,2019,2020,2021,2022,2023,2024,2025]
ocf  ={2018:274.2,2019:393.6,2020:651.7,2021:611.8,2022:-12.8,2023:295.6,2024:573.8,2025:359.7}  # 2018 continuing only (Arcosa spun off)
sbc  ={2018:29.2,2019:29.2,2020:26.9,2021:20.7,2022:22.5,2023:22.7,2024:23.6,2025:22.9}
opcx ={2018:37.3,2019:97.0,2020:102.3,2021:23.6,2022:38.0,2023:41.3,2024:53.8,2025:45.6}
flcx ={2018:948.3,2019:1122.2,2020:602.2,2021:547.2,2022:928.8,2023:668.8,2024:541.9,2025:749.3}
proc ={2018:230.5,2019:205.7,2020:138.7,2021:454.3,2022:750.7,2023:381.8,2024:360.7,2025:399.3}
acq  ={2018:0,2019:0,2020:0,2021:16.6,2022:80.4,2023:62.2,2024:0,2025:0}
lda  ={2018:196.6,2019:232.2,2020:214.7,2021:226.0,2022:236.4,2023:258.0,2024:262.2,2025:273.8}
gain ={2018:50.4,2019:50.5,2020:17.3,2021:54.1,2022:126.2,2023:82.8,2024:57.3,2025:91.4}
intp ={2018:158.9,2019:208.1,2020:205.5,2021:178.4,2022:190.5,2023:246.2,2024:271.4,2025:272.8}
rev  ={2018:2509.1,2019:3005.1,2020:1999.4,2021:1516.0,2022:1977.3,2023:2983.3,2024:3079.2,2025:2156.9}
T=0.21; R=0.0543; F=0.10
debt=5226.5; cash=155.7; restricted=114.2; shares=79.669486; price=25.22
netdebt=debt-cash
A={y:ocf[y]-sbc[y]-opcx[y]-flcx[y]+proc[y]-acq[y] for y in yrs}          # all spending, equity basis
M={y:ocf[y]-sbc[y]-opcx[y]-lda[y]+gain[y]-acq[y] for y in yrs}           # maintenance guess = lease-fleet D&A
U=lambda s:{y:s[y]+intp[y]*(1-T) for y in yrs}                           # add back after-tax interest
def mean(s,ys): return sum(s[y] for y in ys)/len(ys)
def pv(c,g,r):  # c = base-year cash; grows at g for 10 years, then flat (zero nominal growth) forever
    v=0; x=c
    for t in range(1,11):
        x=x*(1+g); v+=x/(1+r)**t
    return v + x/r/(1+r)**10
def halves(s,ys):
    h=len(ys)//2; a=mean(s,ys[:h]); b=mean(s,ys[h:])
    return (b/a)**(1/h)-1 if a>0 and b>0 else None, a, b
out=[]
P=lambda *a: out.append(' '.join(str(x) for x in a))
P('year   A_all-spend  M_maint  M_unlev  A_unlev  intpaid*0.79')
for y in yrs: P(y, round(A[y],1), round(M[y],1), round(U(M)[y],1), round(U(A)[y],1), round(intp[y]*(1-T),1))
for label,ys in (('CYCLE BASE FY2018-FY2025',yrs),('LITERAL WINDOW FY2021-FY2025',yrs[3:])):
    P('\n==',label)
    for nm,s,basis in (('M all-equity (central)',U(M),'ae'),('M equity-only',M,'eq'),('A all-equity',U(A),'ae'),('A equity-only',A,'eq')):
        c=mean(s,ys); g,a,b=halves(s,ys)
        less = netdebt if basis=='ae' else 0
        ng=(pv(c,0,R)-less)/shares
        gr=(pv(c,g,R)-less)/shares if g is not None else None
        ng10=(pv(c,0,F)-less)/shares
        gr10=(pv(c,g,F)-less)/shares if g is not None else None
        fair=(ng10+gr10)/2 if gr10 is not None else ng10
        yld = c/((price*shares)+less)
        P(f'{nm}: base {c:.1f}; halves {a:.1f} -> {b:.1f}, rate {"n/a" if g is None else f"{g*100:.1f}%"}; '
          f'value/share no-growth {ng:.2f}, shown-growth {"n/a" if gr is None else f"{gr:.2f}"}; '
          f'fair (ends at 10%, averaged) {fair:.2f}; cash yield at price {yld*100:.2f}%')
P('\nnet debt (debt 5226.5 less unrestricted cash 155.7, 2026-06-30 10-Q) =',round(netdebt,1),'; with restricted cash also deducted =',round(netdebt-restricted,1))
P('market cap at', price, '=', round(price*shares,1), '; EV =', round(price*shares+netdebt,1))
rg=(mean(rev,yrs[4:])/mean(rev,yrs[:4]))**(1/4)-1
P('sales growth between halves FY2018-21 -> FY2022-25:', f'{rg*100:.1f}%/yr')
open('q7_computation_out.txt','w').write('\n'.join(out)); print('\n'.join(out))
