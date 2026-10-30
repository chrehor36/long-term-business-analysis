import os, sys, time, urllib.request
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
D=os.path.dirname(os.path.abspath(__file__))
CIK="1428439"
FILES=[
 ("0001628280-26-008114","roku-20251231.htm","10K_FY2025.htm"),
 ("0001628280-26-054335","roku-20260630.htm","10Q_2026Q2.htm"),
 ("0001628280-26-054321","wk-20260806.htm","8K_2026-08-06.htm"),
 ("0001428439-25-000013","roku-20241231.htm","10K_FY2024.htm"),
 ("0001428439-24-000011","roku-20231231.htm","10K_FY2023.htm"),
]
def get(url,tries=4):
    last=None
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read()
        except Exception as e:
            last=e; time.sleep(1.5*(i+1))
    raise last
for acc,doc,out in FILES:
    p=os.path.join(D,out)
    if os.path.exists(p) and os.path.getsize(p)>1000:
        print("have",out,os.path.getsize(p)); continue
    a=acc.replace("-","")
    url=f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{doc}"
    b=get(url); open(p,"wb").write(b); print("got",out,len(b)); time.sleep(0.4)
