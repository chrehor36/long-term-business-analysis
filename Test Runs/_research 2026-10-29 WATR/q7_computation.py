# WATR Q7 COMPUTATION, NOT A CLEARANCE. Figures in USD millions, from the filings named in the run file.
ocf   = {2023:-2.9, 2024:-13.074409, 2025:-18.104877}     # FY2023 from DRS MD&A (rounded as filed); FY2024-25 audited CF
inv   = {2023:-0.213, 2024:-3.311146, 2025:-0.758209}     # investing = PP&E + intangibles (no acquisitions)
lease = {2023:None, 2024:-0.544387, 2025:-1.143968}       # lease principal repaid (IFRS 16); FY2023 not stated in the MD&A read
oc = {y: ocf[y]+inv[y]+(lease[y] or 0) for y in ocf}
for y in oc: print(y, 'owner cash', round(oc[y],2), '(lease principal not stated)' if lease[y] is None else '')
avg = sum(oc.values())/len(oc); print('3-yr average', round(avg,2))
sov=0.0537; floor=0.10; sh=31.639454
def pv(c,r,g=0.0,years=10):
    v=sum(c*(1+g)**t/(1+r)**t for t in range(1,years+1)); term=c*(1+g)**years/r/(1+r)**years; return v+term
whole_sov=pv(avg,sov); whole_10=pv(avg,floor)
seriesA=117.037282; cash=37.6
nd=seriesA-cash
print('no-growth whole business at sovereign', round(whole_sov,1), 'at 10%', round(whole_10,1))
print('net debt (Series A accrued value less cash stated in F-1)', round(nd,1))
print('per share, all-equity, at sovereign', round((whole_sov-nd)/sh,2), ' fair (10%)', round((whole_10-nd)/sh,2))
print('per share, equity-only, at sovereign', round(whole_sov/sh,2), ' fair (10%)', round(whole_10/sh,2))
print('market cap at 1.47', round(1.47*sh,1), ' EV all-equity', round(1.47*sh+nd,1))
