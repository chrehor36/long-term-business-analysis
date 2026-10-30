import sys, os, json, time
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
from sources import fts_count
C = {"GFS": 1709048, "TSEM": 928876, "INTC": 50863, "AMD": 2488, "QCOM": 804328, "TXN": 97476, "HIMX": 1342338, "SIMO": 1329394,
     "SYNA": 817720, "MCHP": 827054, "LSCC": 855658, "NVTS": 1821769, "MPWR": 1280452, "ON": 1097864, "NXPI": 1413447, "SWKS": 4127,
     "QRVO": 1604778, "AMBA": 1280263, "POWI": 833640, "SITM": 1451809, "ALGM": 866291, "PI": 1111063, "CRUS": 772406, "SLAB": 1038074}
res = {}
for tk, cik in C.items():
    for ph in ["United Microelectronics", "UMC"]:
        try:
            n, url = fts_count(ph, cik=f"{cik:010d}", forms="10-K,20-F")
        except Exception as e:
            n, url = "ERR " + str(e)[:60], ""
        res[f"{tk}|{ph}"] = (n, url)
        time.sleep(0.15)
    print(tk, res[f"{tk}|United Microelectronics"][0], res[f"{tk}|UMC"][0])
json.dump(res, open(r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 UMC\fts_out.json", "w"), indent=1)
