# All inputs FILING-SOURCED above; every output here is COMPUTED.
P = {
 # name: (feeRev$M, feeEarningAUM$M or None, AUM$M, NIconsol$M, NIparent$M, eqIncNCI$M, eqExNCI$M, prevEqIncNCI$M)
 'RMR  FY25(9/30)': (182.703, 27180.0, 39000.0, 38.679, 17.596, 402.013, 227.656, 419.417),
 'BRDG FY24':       (324.153, 22306.0, 49845.0, 16.716, 8.005, 505.900, 83.423, 545.348),
 'AINC FY24':       (48.488,  None,    None,    -3.992, -3.288, -346.534, -360.914, -304.567),
 'OWL  FY25':       (2521.937,187735.0,307432.0,305.487,78.833, 6054.199,2205.362,5806.036),
 'ARES FY25':       (3680.467,384900.0,622500.0,834.454,527.362,8676.092,4275.463,6824.190),
 'BAM  FY25':       (3384.0,  602714.0,None,    2398.0, 2029.0, 8912.0,  None,    9088.0),
 'CNS  FY25':       (524.834, 90544.0, 90544.0, 157.398,153.217, 611.043, 561.953, 521.443),
 'KW   FY25':       (115.2,   11000.0, 36400.0, 23.8,  -38.8,   1573.4,  1535.1,  1636.0),
 'NMRK FY25':       (1244.233,None,    None,    155.446,126.186,1739.755,1461.574,1524.169),
}
print(f"{'':17} {'fee rate on FEAUM':>18} {'fee rate on AUM':>16} {'ROE(consol/avg tot eq)':>23} {'ROE(parent/avg parent eq)':>26}")
for k,(fee,fe,aum,nic,nip,eq,eqx,peq) in P.items():
    fr  = f"{fee/fe*100:.3f}% ({fee/fe*10000:.0f}bp)" if fe else "n/d"
    fra = f"{fee/aum*100:.3f}% ({fee/aum*10000:.0f}bp)" if aum else "n/d"
    roe = f"{nic/((eq+peq)/2)*100:.1f}%" if eq and peq and (eq+peq)>0 else "n/m (neg eq)"
    print(f"{k:17} {fr:>18} {fra:>16} {roe:>23}")
