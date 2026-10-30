import fetch,sys
L=[("0000060667-26-000029","low-20260130.htm","LOW_10K_FY2025"),
("0000060667-25-000049","low-20250131.htm","LOW_10K_FY2024"),
("0000060667-23-000034","low-20230203.htm","LOW_10K_FY2022"),
("0000060667-22-000038","low-20220128.htm","LOW_10K_FY2021"),
("0000060667-20-000036","form10k01312020.htm","LOW_10K_FY2019"),
("0000060667-18-000051","form10k_02022018.htm","LOW_10K_FY2017"),
("0000060667-15-000057","lowesform10k.htm","LOW_10K_FY2014"),
("0000060667-12-000096","lowesform10k02032012.htm","LOW_10K_FY2011"),
("0000060667-10-000059","lowesform10k01292010.htm","LOW_10K_FY2009"),
("0000060667-08-000067","lowesform10k02012008.htm","LOW_10K_FY2007"),
("0000060667-26-000117",None,"LOW_10Q_Q2FY2026"),
("0000060667-26-000056","low-20260415.htm","LOW_DEF14A_2026"),
]
rows=fetch.subs(60667)
for acc,prim,name in L:
    try:
        if prim is None: prim=[r[3] for r in rows if r[2]==acc][0]
        t=fetch.doc(60667,acc,prim,name); print(name,len(t),flush=True)
    except Exception as e: print(name,"ERR",e,flush=True)
for r in rows:
    if r[0]=="8-K" and r[1]>="2025-01-01": print(*r,sep=" | ")
