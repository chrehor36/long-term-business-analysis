# Competitor row: GAAP operating margin and gross margin, CY2021-25, computed from filed faces ($M)
d = {
 "RIVN": {"rev":[55,1658,4434,4970,5387], "oi":[-4220,-6856,-5739,-4689,-3585], "gp":[-465,-3123,-2030,-1200,144]},
 "LCID": {"rev":[27.111,608.181,595.271,807.832,1353.790], "oi":[-1530.446,-2593.991,-3099.588,-3020.820,-3501.753],
          "cost":[154.897,1646.086,1936.066,1730.943,2610.176]},
 "TSLA": {"rev":[53823,81462,96773,97690,94827], "oi":[6523,13656,8891,7076,4355]},
 "GM":   {"rev":[127004,156735,171842,187442,185019], "oi":[9324,10315,9298,12784,2909]},
 "F":    {"rev":[136341,158057,176191,184992,187267], "oi":[4523,6276,5458,5219,-9169]},
 "F Model e (segment EBIT)": {"rev":[None,None,6528,4115,7166], "oi":[None,None,-4778,-5105,-4806]},
}
for k,v in d.items():
    rev, oi = v["rev"], v["oi"]
    m = [f"{o/r*100:.1f}" if (o is not None and r) else "" for o,r in zip(oi,rev)]
    pr = [(o,r) for o,r in zip(oi,rev) if o is not None and r]
    pool = sum(o for o,_ in pr)/sum(r for _,r in pr)*100
    line = f"{k}: op margin % {m} pooled {pool:.1f}"
    if "gp" in v: line += " | gross margin % " + str([f"{g/r*100:.1f}" for g,r in zip(v['gp'],rev)])
    if "cost" in v: line += " | gross margin % " + str([f"{(r-c)/r*100:.1f}" for c,r in zip(v['cost'],rev)])
    print(line)
