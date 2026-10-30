from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
jobs = [("0000021344-20-000006","a2019123110-k.htm","10K_FY2019"),
        ("0000021344-19-000014","a2018123110-k.htm","10K_FY2018"),
        ("0000021344-18-000008","a2017123110-k.htm","10K_FY2017"),
        ("0000021344-17-000009","a2016123110-k.htm","10K_FY2016")]
for acc, doc, name in jobs:
    try: grab(acc, doc, name)
    except Exception as e: print("ERR", name, e)
