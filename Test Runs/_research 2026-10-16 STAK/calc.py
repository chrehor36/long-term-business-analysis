# STAK run 2026-10-16: arithmetic only (USD millions). Figures from filings cited in the run file.
oc={2022:-0.710,2023:-4.126,2024:-2.753,2025:-8.838}
intpaid={2022:0.0,2023:0.053,2024:0.121,2025:0.183}
m4=sum(oc.values())/4; m3=sum(oc[y] for y in (2023,2024,2025))/3
m4u=sum(oc[y]+intpaid[y] for y in oc)/4
print('mean4 %.3f mean3 %.3f mean4 before interest %.3f'%(m4,m3,m4u))
shares=19.210349; px=1.03; mcap=shares*px
debt=7.568889+0.428994; cash=1.923399; nd_dec=debt-cash; rdo=2.2; nd=nd_dec-rdo
print('mcap %.3f debt %.3f cash %.3f netdebt Dec %.3f after RDO %.3f EV %.3f'%(mcap,debt,cash,nd_dec,nd,mcap+nd))
# H1 FY2026 most favourable case, annualised (beside only)
h1=0.667; h1i=0.106
a_eq=2*h1; a_ae=2*(h1+h1i)
print('annualised H1 equity %.3f all-equity %.3f'%(a_eq,a_ae))
print('return at price: all-equity %.2f%% equity-only %.2f%%'%(100*a_ae/(mcap+nd),100*a_eq/mcap))
for r in (0.10,0.0206):
    ae=(a_ae/r-nd)/shares; eo=(a_eq/r)/shares
    print('rate %.4f: per share all-equity %.3f equity-only %.3f'%(r,ae,eo))
# no-growth case on the four-year mean, perpetuity at the sovereign and at 10%
for r in (0.0206,0.10):
    v=m4u/r; print('no-growth value at %.4f: business %.1f, per share less net debt %.2f'%(r,v,(v-nd)/shares))
# STAK margins pre and post SBC
rev={2023:21.146463,2024:18.918847,2025:24.914618}; opi={2023:3.632258,2024:2.798698,2025:-3.126081}; sbc={2025:3.906}
for y in rev: print(y,'op margin %.1f%%, before stock pay %.1f%%'%(100*opi[y]/rev[y],100*(opi[y]+sbc.get(y,0))/rev[y]))
print('H1FY26 op margin %.1f%%'%(100*2.109754/19.230376))
