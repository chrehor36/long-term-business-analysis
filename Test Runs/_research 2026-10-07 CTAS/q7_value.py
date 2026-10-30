# Q7 arithmetic for the CTAS run of 2026-10-07. All $M. Inputs from filed 10-K cash-flow statements (latest-filed
# vintage, XBRL company facts cross-checked to the FY2026 10-K for FY2024-FY2026).
yrs=[2022,2023,2024,2025,2026]
ocf ={2022:1537.6,2023:1586.2,2024:2068.5,2025:2165.9,2026:2276.3}
sbc ={2022:109.3,2023:103.6,2024:117.0,2025:128.3,2026:128.1}
capx={2022:240.7,2023:331.1,2024:409.5,2025:408.9-24.0,2026:395.1}   # FY2025 net of $24.0M property sale proceeds
acq ={2022:164.2,2023:46.4,2024:186.8,2025:232.9,2026:164.5}
dep ={2022:249.4,2023:257.0,2024:280.9,2025:303.4,2026:318.6}
nint={2022:88.6,2023:109.5,2024:95.0,2025:95.5,2026:101.2}         # interest expense less interest income
etr ={2022:263.0/1498.8,2023:345.1/1693.1,2024:402.0/1973.6,2025:451.9/2264.2,2026:505.4/2505.3}
R=0.0564; FLOOR=0.10; SH=400.17; PRICE=196.98
debt=2436.55; cash=289.0; post=48.4   # face of senior notes; cash; buybacks after year-end stated in the 10-K
ND=debt-cash+post
def series(kind,basis):
    out={}
    for y in yrs:
        c=ocf[y]-sbc[y]
        c-= dep[y] if kind=='maint' else capx[y]
        if kind=='all': c-=acq[y]
        if basis=='ae': c+=nint[y]*(1-etr[y])
        out[y]=c
    return out
def cagr(s): return (s[2026]/s[2022])**(1/4)-1
def halves(s): a=(s[2022]+s[2023])/2; b=(s[2025]+s[2026])/2; return (b/a)**(1/3)-1
def pv(c,g,r):
    v=0;x=c
    for t in range(1,11): x*=1+g; v+=x/(1+r)**t
    return v + x/r/(1+r)**10
def irr(c,g,price_total):
    lo,hi=0.0001,0.5
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c,g,m)>price_total: lo=m
        else: hi=m
    return m
out=[]
for basis in ['ae','eq']:
    nd = ND if basis=='ae' else 0.0
    for kind in ['all','noacq','maint']:
        s=series(kind,basis); avg=sum(s.values())/5
        out.append((basis,kind,{y:round(s[y],1) for y in yrs},round(avg,1),round(cagr(s)*100,2),round(halves(s)*100,2)))
for o in out: print(o)
print('net debt',round(ND,1))
def report(basis,c_lo,g_lo,c_hi,g_hi,label):
    nd = ND if basis=='ae' else 0.0
    lo=(pv(c_lo,g_lo,R)-nd)/SH; hi=(pv(c_hi,g_hi,R)-nd)/SH
    # fair price: midpoint stream (average of the two end streams) discounted at the floor
    fair=((pv(c_lo,g_lo,FLOOR)+pv(c_hi,g_hi,FLOOR))/2-nd)/SH
    ev=PRICE*SH+nd
    r_lo=irr(c_lo,g_lo,ev); r_hi=irr(c_hi,g_hi,ev)
    print(f'{label} [{basis}] range ${min(lo,hi):.2f} to ${max(lo,hi):.2f}  width {max(lo,hi)/min(lo,hi):.2f}x  fair ${fair:.2f}  return at price {r_lo*100:.2f}% (end 1) to {r_hi*100:.2f}% (end 2)')
S={}
for basis in ['ae','eq']:
    a=series('all',basis); m=series('maint',basis); n=series('noacq',basis)
    A=sum(a.values())/5; M=sum(m.values())/5; N=sum(n.values())/5; g=cagr(a)
    report(basis,A,0.0,A,g,'DEFAULT (c): all spending incl. acquisitions; no growth / total growth')
    report(basis,M,0.0,A,g,'CENTRAL (e): maintenance-only no growth / all spending at total growth')
    report(basis,N,0.0,N,0.091,'ORGANIC PAIR: acquisitions left out; organic revenue growth 9.1%')

# BESIDE, not central: the pending UniFirst merger (not closed; FTC timing agreement to 2026-12-11). UniFirst owner cash
# from its own filings FY2021-FY2025 (OCF - SBC - capex, acquisitions left out; it has no debt), valued at no growth
# (its shown growth is meaningless: the series changes sign with acquisitions in). Cash paid $155 x 18.47M shares
# (14,261,683 new Cintas shares / 0.7720), UniFirst cash and short-term investments of $210M at 2025-08-30 netted.
unf=[212.3-7.0-133.6,122.6-9.1-144.3,215.8-9.1-172.0,295.3-9.8-160.4,296.9-12.2-154.3]
U=sum(unf)/5; unf_sh=14.261683/0.7720; cash_paid=155*unf_sh; new_sh=14.261683
print('UniFirst owner cash ex-acq',[round(x,1) for x in unf],'avg',round(U,1),'cash paid',round(cash_paid,1))
a=series('all','ae'); M=sum(series('maint','ae').values())/5; A=sum(a.values())/5; g=cagr(a)
ndc=ND+cash_paid-210
lo=(pv(M,0,R)+U/R-ndc)/(SH+new_sh); hi=(pv(A,g,R)+U/R-ndc)/(SH+new_sh)
fair=((pv(M,0,FLOOR)+pv(A,g,FLOOR))/2+U/FLOOR-ndc)/(SH+new_sh)
print(f'COMBINED (beside) [ae] range ${lo:.2f} to ${hi:.2f}  fair ${fair:.2f}')
