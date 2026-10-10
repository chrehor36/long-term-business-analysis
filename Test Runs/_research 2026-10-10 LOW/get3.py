import fetch
rows=fetch.subs(354950)
k=[r for r in rows if r[0]=="10-K"]
for r in k: print(*r,sep=" | ",flush=True)
want={"2010-01-31":"HD_10K_FY2009","2022-01-30":"HD_10K_FY2021","2026-02-01":"HD_10K_FY2025","2018-01-28":"HD_10K_FY2017","2014-02-02":"HD_10K_FY2013"}
for r in k:
    if r[4] in want:
        t=fetch.doc(354950,r[2],r[3],want[r[4]]); print(want[r[4]],len(t),flush=True)
