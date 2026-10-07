import sys, datetime
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
c = sources._chart("KO", rng="2y", max_age_h=0)
r = c["chart"]["result"][0] if "chart" in c else c
ts = r["timestamp"]; q = r["indicators"]["quote"][0]
rows=[(datetime.datetime.utcfromtimestamp(t).date(), q["close"][i]) for i,t in enumerate(ts) if q["close"][i]]
import statistics
by={}
for d,c in rows: by.setdefault(d.strftime("%Y-%m"),[]).append(c)
for m in sorted(by): print(m, round(statistics.mean(by[m]),2), round(min(by[m]),2), round(max(by[m]),2))
lo=min(rows,key=lambda x:x[1]); hi=max(rows,key=lambda x:x[1]); print("2y low",lo,"2y high",hi)
