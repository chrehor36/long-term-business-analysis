import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_core import *
L = [("0001375365-26-000022","smci-20260630.htm","10K_FY2026"),
     ("0001375365-25-000027","smci-20250630.htm","10K_FY2025"),
     ("0001375365-25-000004","smci-20240630.htm","10K_FY2024"),
     ("0001375365-23-000036","smci-20230630.htm","10K_FY2023"),
     ("0001375365-22-000103","smci-20220630.htm","10K_FY2022"),
     ("0001375365-21-000060","smci-20210630.htm","10K_FY2021"),
     ("0001375365-20-000064","smci-2020630x10k.htm","10K_FY2020"),
     ("0001375365-19-000079","smci-2019630x10k.htm","10K_FY2019"),
     ("0001375365-19-000039","smci-2017630x10kxa.htm","10K_FY2017_filed2019"),
     ("0001375365-26-000014","smci-20260331.htm","10Q_2026-03-31"),
     ("0001375365-26-000008","smci-20260303.htm","DEF14A_2026"),
    ]
for acc, doc, nm in L:
    try: grab(acc, doc, nm)
    except Exception as e: print("ERR", nm, e)
