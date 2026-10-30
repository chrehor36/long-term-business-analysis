import json
S=json.load(open('peers/series.json'))
# hand-entered from the FY2010 10-K selected data (accessions in the run file), $M
NI_EXTRA={'MHO':{2006:38.9,2007:-128.1,2008:-245.4},
          'DHI':{2006:1233.3,2007:-712.5,2008:-2633.6,2009:-549.8},
          'LEN':{2006:593.9,2007:-1941.1,2008:-1109.1,2009:-417.1},
          'MTH':{2006:225.4,2007:-288.9,2008:-291.9,2009:-66.5},
          'NVR':{2006:587.4,2007:334.0,2008:100.9}}
EQ_2007={'MHO':581.3,'DHI':5655.3,'LEN':3822.1,'MTH':730.2,'NVR':1129.0}
REV_EXTRA={'MHO':{2006:1274.1,2007:1016.5,2008:607.7},'NVR':{2006:6036.2+97.9,2007:5048.2+81.2,2008:3638.7+54.3},
           'DHI':{2006:14760.5+290.8,2007:11088.8+207.7,2008:6518.6+127.5},'LEN':{2006:16266.7,2007:10186.8},
           'MTH':{2006:3461.3,2007:2343.6,2008:1523.1}}
PTI_MHO={2012:12.7,2013:41.3,2014:69.7,2015:87.0,2016:91.8,2017:120.3,2018:141.3,2019:166.0,2020:310.1,2021:509.1,2022:635.2,2023:607.3,2024:733.6,2025:526.6}
for tk in ['MHO','NVR','DHI','LEN','MTH','CCS']:
    s=S[tk]; ni={int(k):v/1e6 for k,v in s['ni'].items()}; ni.update(NI_EXTRA.get(tk,{}))
    eq={int(k):v/1e6 for k,v in s['eq'].items()}
    rev={int(k):v/1e6 for k,v in s['rev'].items()}; rev.update(REV_EXTRA.get(tk,{}))
    pti={int(k):v/1e6 for k,v in s['pti'].items()}
    if tk=='MHO': pti=PTI_MHO
    crash=[y for y in range(2007,2012) if y in ni]
    out=[tk]
    if tk in EQ_2007:
        e0=EQ_2007[tk]; tot=sum(ni.get(y,0) for y in range(2008,2026))
        loss=sum(ni.get(y,0) for y in range(2007,2012))
        out.append(f"NI 2007-11 {loss:,.0f} ({loss/ (eq.get(2006) or EQ_2007[tk]-ni.get(2007,0)) *100:.0f}% of 2006 eq approx)")
        out.append(f"NI 2008-25 {tot:,.0f} on 2007 eq {e0:,.0f}")
        # avg ROE 2008-2025 on beginning equity
        roes=[]
        for y in range(2008,2026):
            b=eq.get(y-1) or (e0 if y==2008 else None)
            if b and y in ni: roes.append(ni[y]/b)
        out.append(f"mean ROE 2008-25 {sum(roes)/len(roes)*100:.1f}% (n={len(roes)})")
    pm=[pti[y]/rev[y] for y in range(2012,2026) if y in pti and y in rev]
    if pm: out.append(f"mean pretax margin 2012-25 {sum(pm)/len(pm)*100:.1f}% (n={len(pm)})")
    if 2025 in pti and 2025 in rev: out.append(f"2025 pretax margin {pti[2025]/rev[2025]*100:.1f}%")
    if 2006 in ni and 2006 in rev: out.append(f"2006 net margin {ni[2006]/rev[2006]*100:.1f}%")
    print(' | '.join(out))
