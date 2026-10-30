"""Libbey 2010-2019: operating margin and pre-tax return on tangible capital employed, from the run.py
balance-sheet table and the XBRL income lines (transcription; impairments added back where filed)."""
sales={2010:799.8,2011:817.1,2012:825.3,2013:818.8,2014:852.5,2015:822.3,2016:793.4,2017:781.8,2018:797.9,2019:782.4}
opi={2010:68.8,2011:63.5,2012:81.3,2013:72.5,2014:81.2,2015:43.7,2016:45.3,2017:-53.7,2018:27.0,2019:-33.3}
imp={2017:79.7,2019:65.2}
# year-end: equity, cash, goodwill, intangibles, debt (current+noncurrent), USD M
bs={2010:(11.3,76.3,169.3,23.1,447.1),2011:(27.8,58.3,166.6,21.2,397.0),2012:(24.5,67.2,166.6,20.2,466.5),
    2013:(130.8,42.2,167.4,19.3,411.9),2014:(77.5,60.0,164.1,17.8,443.9),2015:(148.4,49.0,164.1,16.4,431.0),
    2016:(145.1,61.0,164.1,15.2,407.8),2017:(66.9,24.7,84.4,14.6,384.4),2018:(49.9,25.1,84.4,13.4,397.7),
    2019:(-25.8,48.9,38.4,11.9,391.8)}
ni={2010:70.1,2011:23.6,2012:7.0,2013:28.5,2014:5.0,2015:66.3,2016:10.1,2017:-93.4,2018:-8.0,2019:-69.0}
rows=[]
for y in range(2010,2020):
    e,c,gw,it,d=bs[y]; tce=e-gw-it+d-c; oi=opi[y]+imp.get(y,0)
    rows.append((y,sales[y],opi[y],oi,100*opi[y]/sales[y],100*oi/sales[y],tce,100*oi/tce))
    print(f"{y} sales {sales[y]:6.1f} opinc {opi[y]:6.1f} ex-impairment {oi:6.1f} margin {100*opi[y]/sales[y]:5.1f}% ex-imp {100*oi/sales[y]:5.1f}%  tangible cap employed {tce:6.1f}  pre-tax ROTCE ex-imp {100*oi/tce:5.1f}%")
import statistics as s
print("mean margin as filed %.1f%%, ex-impairment %.1f%%; mean ROTCE ex-imp %.1f%%"%(s.mean(r[4] for r in rows),s.mean(r[5] for r in rows),s.mean(r[7] for r in rows)))
print("net income sum 2010-2019: %.1f"%sum(ni.values()))
