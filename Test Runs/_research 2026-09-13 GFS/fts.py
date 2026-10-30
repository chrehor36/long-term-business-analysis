"""SCREEN, NOT EVIDENCE (operator rule 8): EDGAR full-text-search hit counts for 'GlobalFoundries' in customers' and
competitors' annual reports, through tools/sources.py:fts_count(). An HTTP error is recorded as an error, never a zero."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import sources as S
CIKS = {"QCOM": 804328, "AMD": 2488, "SWKS": 4127, "QRVO": 1604778, "CRUS": 772406, "NXPI": 1413447, "MRVL": 1835632,
        "AVGO": 1730168, "SONY": 313838, "HIMX": 1342338, "TSEM": 928876, "LSCC": 855658, "MCHP": 827054, "SLAB": 1038074,
        "SMTC": 88941, "MTSI": 1493594, "INDI": 1841925, "NVTS": 1821769, "ALGM": 866291, "ON": 1097864, "ADI": 6281,
        "TXN": 97476, "INTC": 50863, "UMC": 1033767, "TSM": 1046179, "NVDA": 1045810, "AAPL": 320193, "CSCO": 858877,
        "POET": 1437424, "COHR": 820318, "LITE": 1633978, "MXL": 1288469, "SIMO": 1329394, "AMBA": 1280263, "RMBS": 917273}
out = {}
for tk, c in CIKS.items():
    try:
        n, url = S.fts_count("GlobalFoundries", cik=f"{c:010d}", forms="10-K,20-F")
        out[tk] = n
    except Exception as e:
        out[tk] = f"ERROR {e}"
    print(tk, out[tk]); time.sleep(0.3)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fts_out.json"), "w"), indent=1)
