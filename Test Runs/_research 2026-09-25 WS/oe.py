# FY: OCF, SBC, capex, D&A, payments to NCI, working-capital change inside OCF  ($M, filed statements)
rows={2021:(152.550,10.136,28.801,44.951,10.690,-72.748),
      2022:(39.491,8.668,36.442,59.501,35.160,-203.981),
      2023:(315.011,10.351,45.470,69.583,20.235,139.932),
      2024:(199.5,10.3,103.4,65.3,8.8,-30.4),
      2025:(230.3,11.0,130.4,66.0,17.0,20.2),
      2026:(201.2,13.9,121.2,84.2,6.0,28.8)}
MGMT=42.5  # 10-K FY2026: maintenance "between approximately $40.0 million and $45.0 million", midpoint
cap=1807.6
print("FY  OCF   SBC  capex  D&A   OE_lo(max c)  OE_hi(min c)  OE_mgmt  NCIpay  WC")
oe={}
for y,(o,s,c,d,n,w) in rows.items():
    lo=o-s-max(c,d); hi=o-s-min(c,d); mg=o-s-MGMT
    oe[y]=(lo,hi,mg,n,w)
    print(y,f"{o:6.1f} {s:5.1f} {c:6.1f} {d:5.1f}   {lo:7.1f}      {hi:7.1f}     {mg:6.1f}  {n:5.1f}  {w:7.1f}")
def win(a,b,lab):
    ys=[y for y in rows if a<=y<=b]; k=len(ys)
    lo=sum(oe[y][0] for y in ys)/k; hi=sum(oe[y][1] for y in ys)/k; mg=sum(oe[y][2] for y in ys)/k
    nci=sum(oe[y][3] for y in ys)/k
    print(f"{lab:26s} {k}y  OE ${lo:6.1f}M to ${hi:6.1f}M (mgmt-c ${mg:6.1f}M)  yield {100*lo/cap:4.2f}%-{100*hi/cap:4.2f}%   after NCI payments ${lo-nci:6.1f}M to ${hi-nci:6.1f}M  ({100*(lo-nci)/cap:4.2f}%-{100*(hi-nci)/cap:4.2f}%)")
win(2024,2026,"3y FY2024-26")
win(2022,2026,"5y FY2022-26 (default)")
win(2021,2025,"5y FY2021-25")
win(2021,2023,"3y FY2021-23")
win(2021,2026,"6y FY2021-26 (all filed)")
