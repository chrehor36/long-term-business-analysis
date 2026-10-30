import re, sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
H = os.path.dirname(os.path.abspath(__file__))
def T(k):
    t = open(os.path.join(H, k + "_10K_FY2025.txt"), encoding="utf-8").read()
    t = re.sub(r"\s*\|\s*", " ", t); t = re.sub(r"\s+", " ", t).replace(" $ ", " ")
    return t
# (ticker, label, keyword regex, numbers expected in order within 1500 chars after keyword)
CHK = [
 ("KKR","GAAP Management Fees FY25/24",r"Management Fees",["2,496,783","1,994,089"]),
 ("KKR","segment Management fees FY25/24",r"Management Fees",["4,100,841","3,461,381"]),
 ("KKR","FPAUM YE25/YE24",r"Fee Paying Assets Under Management",["604,144","511,963"]),
 ("KKR","FRE FY25/24",r"Fee Related Earnings",["3,714,313","3,267,796"]),
 ("APO","GAAP mgmt fees",r"Management fees",["2,378","1,899"]),
 ("APO","FGAUM YE24/YE25",r"Fee-Generating AUM",["568,666","709,139"]),
 ("APO","FGAUM YE23",r"Fee-Generating AUM",["492,952"]),
 ("APO","FRE FY25/24",r"Fee Related Earnings",["2,528","2,063"]),
 ("APO","segment mgmt fees",r"Management fees",["3,391","2,776"]),
 ("CG","Fund management fees",r"Fund management fees",["2,396.6","2,188.1"]),
 ("CG","FEAUM",r"Fee-earning AUM",["307,418","304,358"]),
 ("CG","FEAUM YE25",r"Fee-earning AUM",["336,778"]),
 ("CG","FRE",r"Fee Related Earnings",["1,236.2","1,104.6"]),
 ("ARES","Mgmt fees",r"Management fees",["3,680,467","2,942,126"]),
 ("ARES","FPAUM",r"FPAUM",["292,553","384,949"]),
 ("ARES","FPAUM YE23",r"FPAUM",["262,357"]),
 ("ARES","FRE",r"Fee related earnings",["1,775,300","1,361,737"]),
 ("OWL","Mgmt fees",r"Management fees, net",["2,521,937","1,994,064"]),
 ("OWL","FPAUM",r"FPAUM",["102,696","159,794"]),
 ("OWL","FPAUM YE25",r"FPAUM",["187,735"]),
 ("OWL","FRE",r"Fee-Related Earnings",["1,496,536","1,253,366"]),
 ("TPG","Mgmt fees",r"Management fees",["1,826,411","1,637,990"]),
 ("TPG","FAUM",r"FAUM",["136,794","141,286"]),
 ("TPG","FAUM YE25",r"FAUM",["170,102"]),
 ("TPG","FRE",r"Fee-Related Earnings",["952,572","764,228"]),
 ("BLK","advisory+lending",r"Total investment advisory, administration fees and securities lending revenue",["19,179"]),
 ("BLK","AUM",r"Total",["11,551,251","14,041,518"]),
 ("TROW","advisory fees",r"Investment advisory fees",["6,602.3"]),
 ("TROW","AUM",r"Ending",["1,606.6","1,775.6"]),
 ("BAM","base mgmt fees",r"Base management fees",["4,896","4,233"]),
 ("BAM","FBC",r"Fee-Bearing Capital",["538,541","602,714"]),
 ("BAM","FBC YE23",r"Fee-Bearing Capital",["456,998"]),
]
cache = {}
for k, lab, kw, nums in CHK:
    t = cache.setdefault(k, T(k))
    hit = None
    for m in re.finditer(kw, t):
        w = t[m.start(): m.start() + 3000]
        pos = [w.find(n) for n in nums]
        if all(p >= 0 for p in pos):
            hit = (m.start(), w[:min(max(pos) + 40, 700)]); break
    print(("OK  " if hit else "MISS") + f" {k:5} {lab:32} {nums}")
    if hit: print("     ", hit[1][:420])
