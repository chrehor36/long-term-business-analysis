import sys, datetime
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
c = sources._chart("PUBM", rng="2y", max_age_h=0)
r = c["chart"]["result"][0] if "chart" in c else c
ts = r["timestamp"]; q = r["indicators"]["quote"][0]
rows=[(datetime.datetime.utcfromtimestamp(t).date(), q["close"][i]) for i,t in enumerate(ts) if q["close"][i]]
for d,cl in rows[::10]: print(d, round(cl,2))
lo=min(rows,key=lambda x:x[1]); hi=max(rows,key=lambda x:x[1]); print("low",lo,"high",hi)
