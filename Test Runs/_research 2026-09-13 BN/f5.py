import urllib.request, os
from f2 import totext
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=240).read()
jobs=[("0001104659-26-071025","tm2616467d1_ex99-1.htm","6K_20260605_ex991.txt"),
("0001104659-26-071025","tm2616467d1_ex99-2.htm","6K_20260605_ex992.txt"),
("0001104659-26-071025","tm2616467d1_ex99-3.htm","6K_20260605_ex993_circular.txt"),
("0001104659-26-084374","tm2620706d1_ex99-1.htm","6K_20260717_ex991.txt"),
("0001104659-26-084374","tm2620706d1_ex99-2.htm","6K_20260717_ex992.txt"),
("0001104659-26-066346","tm2615584d1_ex99-1.htm","6K_20260526_ex991.txt"),
("0001104659-26-054958","tm2613497d1_ex99-1.htm","6K_20260504_ex991.txt"),
("0001104659-26-046224","tm2612378d1_ex99-1.htm","6K_20260422_ex991.txt"),
("0001104659-26-046224","tm2612378d1_ex99-2.htm","6K_20260422_ex992.txt"),
("0001171843-26-005474","exh_991.htm","6K_20260813_ex991_Q2release.txt"),
("0001171843-26-005640","exh_991.htm","6K_20260818_ex991.txt"),
("0001171843-26-005138","exh_991.htm","6K_20260803_ex991.txt"),
("0001104659-26-089206","tm2619563d1_posam.htm","POSAM_20260731.txt")]
for acc,fn,out in jobs:
    if os.path.exists(out): continue
    b=get(f"https://www.sec.gov/Archives/edgar/data/1001085/{acc.replace('-','')}/{fn}")
    open(out,"w",encoding="utf-8").write(totext(b)); print(out,len(b))
