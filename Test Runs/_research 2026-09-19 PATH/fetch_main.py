from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
jobs = [("0001734722-26-000041","path-20260430.htm","10Q_2026Q1"),
        ("0001734722-25-000007","path-20250131.htm","10K_FY2025"),
        ("0001734722-24-000011","path-20240131.htm","10K_FY2024"),
        ("0001734722-23-000017","path-20230131.htm","10K_FY2023"),
        ("0001734722-22-000006","path-20220131.htm","10K_FY2022"),
        ("0001734722-25-000043","path-20250731.htm","10Q_2025Q2"),
        ("0001734722-26-000027","path-20260512.htm","DEF14A_2026"),
        ("0001734722-26-000047","path-20260901.htm","8K_2026-09-03"),
        ("0001734722-26-000015","path-20260324.htm","8K_2026-03-25"),
        ("0001734722-26-000043","path-20260625.htm","8K_2026-06-29"),
        ("0001734722-23-000007","path-20230307.htm","8K_2023-03-10_503"),
        ("0001734722-22-000014","path-20220414.htm","8K_2022-04-20_401"),
        ("0001734722-25-000004","path-20250306.htm","8K_2025-03-12"),
        ("0001734722-24-000044","path-20240708.htm","8K_2024-07-09_205"),
        ("0001734722-22-000039","path-20220624.htm","8K_2022-06-27_205"),
        ("0001734722-22-000056","path-20221110.htm","8K_2022-11-14_205"),
       ]
for acc, doc, name in jobs:
    try: grab(acc, doc, name)
    except Exception as e: print("ERR", name, e)
# earnings releases
L=[l.split() for l in open("filings_list.txt")]
for x in L:
    if x[1]=="8-K" and "2.02" in x[4] and x[0] >= "2022-03-01":
        acc=x[2]
        try: names=exhibits(acc)
        except Exception as e: print("ERR idx",acc,e); continue
        ex=[n for n in names if re.search(r"ex[-_]?99[-_.]?1|ex991|exhibit991", n.lower())]
        print(x[0],acc,ex, [n for n in names if n.endswith('.htm')])
        if ex: grab(acc, ex[0], "EX991_"+x[0], cik=1734722)
        time.sleep(0.3)
