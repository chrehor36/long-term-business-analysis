import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_core import *
old = json.loads(get("https://data.sec.gov/submissions/CIK0001297996-submissions-001.json"))
open(os.path.join(HERE,"submissions_001.json"),"w",encoding="utf-8").write(json.dumps(old))
for i in range(len(old["form"])):
    if old["form"][i] == "10-K" and old["filingDate"][i] >= "2015-01-01":
        print("OLD10K", old["filingDate"][i], old["accessionNumber"][i], old["primaryDocument"][i])
        grab(old["accessionNumber"][i], old["primaryDocument"][i], "10K_FY" + str(int(old["filingDate"][i][:4]) - 1))
for acc, doc, nm in [("0001297996-18-000026","dlr12311710k.htm","10K_FY2017"),("0001297996-19-000032","dlrq412311810kss.htm","10K_FY2018"),
                     ("0001558370-20-001906","dlr-20191231x10kabe894.htm","10K_FY2019"),("0001558370-21-002191","dlr-20201231x10k.htm","10K_FY2020"),
                     ("0001308179-26-000296","dlr015307-def14a.htm","DEF14A_2026"),("0001104659-26-054255","dlr-20260331x10q.htm","10Q_2026-03-31"),
                     ("0001193125-20-072868","d903260d8k.htm","8K_2020-03-13_Interxion_close"),("0001193125-17-285083","d399230d8k.htm","8K_2017-09-14_DFT_close")]:
    try: grab(acc, doc, nm)
    except Exception as e: print("ERR", nm, e)
for nm in exhibits("0001500081-26-000009"):
    if nm.endswith(".xml"): 
        open(os.path.join(HERE,"form4_0001500081-26-000009.xml"),"w",encoding="utf-8").write(get(f"https://www.sec.gov/Archives/edgar/data/1297996/000150008126000009/{nm}")); print("form4", nm)
