p=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-12 Run - ROKU Roku.md"
t=open(p,encoding='utf-8').read()
reps=[
("**Documents fetched and read:** eleven Roku 10-Ks (FY2015 figures via the FY2017 filing\n  through FY2025)",
 "**Documents fetched and read:** nine Roku 10-Ks (FY2017 through FY2025, which between them\n  carry filed figures back to FY2015)"),
("accession numbers for eleven 10-Ks\n      one 10-Q, four 8-Ks",
 "accession numbers for nine 10-Ks,\n      one 10-Q, four 8-Ks"),
]
for a,b in reps:
    if a in t:
        t=t.replace(a,b); print("done:",a[:40])
    else:
        print("MISS:",a[:60])
open(p,'w',encoding='utf-8').write(t)
