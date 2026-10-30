import json, sys, time
from fetch import get
C = "1559720"
docs = [
 ("tenk_FY2025.htm","0001559720-26-000004","abnb-20251231.htm"),
 ("tenk_FY2024.htm","0001559720-25-000010","abnb-20241231.htm"),
 ("tenk_FY2023.htm","0001559720-24-000006","abnb-20231231.htm"),
 ("tenk_FY2022.htm","0001559720-23-000003","abnb-20221231.htm"),
 ("tenk_FY2021.htm","0001559720-22-000006","abnb-20211231.htm"),
 ("tenk_FY2020.htm","0001559720-21-000010","airbnb-10k.htm"),
 ("tenq_2026Q2.htm","0001559720-26-000027","abnb-20260630.htm"),
 ("tenq_2025Q2.htm","0001559720-25-000025","abnb-20250630.htm"),
 ("def14a_2026.htm","0001193125-26-175062","d936646ddef14a.htm"),
 ("eightk_20260316.htm","0001193125-26-108514","d106317d8k.htm"),
 ("s1_424b4.htm","0001193125-20-315318","d81668d424b4.htm"),
]
for out, acc, doc in docs:
    url = f"https://www.sec.gov/Archives/edgar/data/{C}/{acc.replace('-','')}/{doc}"
    try:
        r = get(url, out); print(out, len(r))
    except Exception as e:
        print("ERR", out, e)
# indexes for exhibits
for acc in ["0001193125-26-108514","0001193125-26-337928","0001193125-26-048670","0001193125-25-026054","0001193125-24-033706"]:
    url = f"https://www.sec.gov/Archives/edgar/data/{C}/{acc.replace('-','')}/{acc}-index.json"
    try:
        r = get(f"https://www.sec.gov/Archives/edgar/data/{C}/{acc.replace('-','')}/index.json")
        j = json.loads(r)
        print(acc, [x['name'] for x in j['directory']['item']])
    except Exception as e:
        print("ERR idx", acc, e)
