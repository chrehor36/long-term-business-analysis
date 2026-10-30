# Owner cash by year, HK$ millions, from the consolidated cash-flow statements and reconciliation notes (ARs 2015-2025).
# OC (all-equity, before interest, after the company's own tax as paid) =
#   cash generated from operations (excludes interest income and listed dividends; includes working capital)
#   - income tax paid - stock pay (added back in the reconciliation; a real cost)
#   - PPE, leasehold land and intangible purchases + PPE disposal proceeds
#   - lease payments - Macau gaming concession payments (from 2023)
#   + dividends received from joint ventures and associates (equity-method income counted as cash received)
# acquisitions (net) shown separately.
D={ # cgo, tax, sbc, capex(ppe+land+intang), disp, lease, conc, jvdiv, acq_net(paid +), revenue, exempt_tax_value
2015:(6753.375,67.249,439.846,6594.138,5.568,0.164,0,105.095,650.0,50991.0,1066.138),
2016:(12865.401,88.309,410.265,2127.839,21.903,0,0,48.371,0,52826.0,1167.301),
2017:(18737.538,94.380,381.049,2021.997,9.668,16.002,0,89.392,0,62520.0,1572.377),
2018:(14051.765,128.140,209.253,3033.046,50.902,0,0,186.438,0,55210.901,1843.375),
2019:(19702.265,140.704,275.391,4171.658,2.483,42.511,0,300.711,0,51901.991,1809.473),
2020:(-7418.491,139.844,297.811,5797.018,1.342,52.455,0,430.156,0,12876.099,0),
2021:(-3274.964,130.923,206.043,6930.761,5.115,53.350,0,376.952,0,19695.530,332.846),
2022:(-2882.847,96.534,181.190,5077.238,61.980,52.862,0,354.511,0,11473.793,0),
2023:(11663.166,69.325,251.279,6018.284,0.273,79.461,267.948,167.259,850.342,35684.253,1064.617),
2024:(11713.501,163.238,261.373,4868.198,5.825,91.384,268.880,59.127,-27.423,43432.373,1330.582),
2025:(14460.713,207.150,229.454,3482.126,5.224,93.639,269.827,27.966,-0.730,49242.325,1582.775),
}
OC={}
print('year  CGO     OC_paid  OC_stat  capex   OC_pre_capex(maint=D&A?)  acq   rev    OC/rev')
for y,(cgo,tax,sbc,cap,disp,lease,conc,jv,acq,rev,ex) in D.items():
    oc=cgo-tax-sbc-cap+disp-lease-conc+jv
    ocs=oc-ex
    OC[y]=(oc,ocs,acq,rev,cap)
    print(y, round(cgo), round(oc), round(ocs), round(cap), round(oc+cap), round(acq), round(rev), f'{oc/rev:.1%}')
