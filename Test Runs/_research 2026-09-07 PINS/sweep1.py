import os,re,sys
sys.stdout.reconfigure(encoding="utf-8")
OUT=os.path.dirname(os.path.abspath(__file__))
CHECKS={
 "META_10K_FY2025.txt":["200,966","83,276","60,458","115,800","20,427","69,691","18,616","Family daily active people"],
 "GOOGL_10K_FY2025.txt":["402,836","129,039","132,170","164,713","24,953","91,447","294,691"],
 "SNAP_10K_FY2025.txt":["5,931,431","(532,203","(460,491","656,244","1,016,845","218,999","5,931","656,2","1,016,8"],
 "RDDT_10K_FY2025.txt":["2,202,533","441,957","529,749","690,865","343,152","6,712","2,202","690,8"],
 "10K_FY2025.txt":["4,221,834","319,873","416,891","1,284,343","880,469","32,412","4,221","1,284"],
 "TTD_10K_FY2025.txt":["2,896,271","589,340","443,331","992,678","490,619","197,0","2,896"],
}
for fn,strs in CHECKS.items():
    t=open(os.path.join(OUT,fn),encoding="utf-8").read()
    print(f"--- {fn} ({len(t)} chars) ---")
    for s in strs:
        print(f"   {'HIT ' if s in t else 'MISS'} {s!r}  n={t.count(s)}")
