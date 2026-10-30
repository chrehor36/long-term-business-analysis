import sys, datetime
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
c = sources._chart("SOUN", rng="2y", max_age_h=0)
r = c["chart"]["result"][0] if "chart" in c else c
ts = r["timestamp"]; q = r["indicators"]["quote"][0]
rows=[(datetime.datetime.utcfromtimestamp(t).date(), q["open"][i], q["high"][i], q["low"][i], q["close"][i], q["volume"][i]) for i,t in enumerate(ts) if q["close"][i]]
with open("price2y_daily.txt","w") as f:
    for x in rows: f.write("%s %.4f %.4f %.4f %.4f %s\n" % x)
for d in ["2025-12-31","2026-02-24","2026-04-20","2026-04-21","2026-07-02","2026-08-05","2026-08-06","2026-09-02","2026-09-04","2026-08-31","2026-09-01","2026-09-18"]:
    for x in rows:
        if str(x[0])==d: print(x)
lo=min(rows,key=lambda x:x[4]); hi=max(rows,key=lambda x:x[4]); print("low",lo[0],lo[4],"high",hi[0],hi[4])
