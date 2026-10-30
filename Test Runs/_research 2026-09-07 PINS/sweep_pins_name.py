import os,re,sys
sys.stdout.reconfigure(encoding="utf-8")
OUT=os.path.dirname(os.path.abspath(__file__))
FILES=["META_10K_FY2025.txt","META_10K_FY2024.txt","GOOGL_10K_FY2025.txt","GOOGL_10K_FY2024.txt",
 "SNAP_10K_FY2025.txt","SNAP_10K_FY2024.txt","SNAP_10K_FY2023.txt","SNAP_10K_FY2022.txt",
 "SNAP_10K_FY2021.txt","SNAP_10K_FY2020.txt","RDDT_10K_FY2025.txt","RDDT_10K_FY2024.txt","TTD_10K_FY2025.txt"]
for fn in FILES:
    t=open(os.path.join(OUT,fn),encoding="utf-8").read()
    n=len(re.findall(r"Pinterest",t,re.I))
    print(f"\n##### {fn}: 'Pinterest' n={n}")
    for m in re.finditer(r"Pinterest",t,re.I):
        print("   ...",re.sub(r"\s+"," ",t[max(0,m.start()-350):m.start()+250]))
