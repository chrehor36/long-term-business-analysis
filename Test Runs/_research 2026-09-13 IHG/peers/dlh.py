import sys, json
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 IHG')
import edgar
for fy,acc,doc in [('2022','0001468174-23-000009','h-20221231.htm'),('2023','0001468174-24-000014','h-20231231.htm')]:
    url=f"https://www.sec.gov/Archives/edgar/data/1468174/{acc.replace('-','')}/{doc}"
    t=edgar.strip_html(edgar.get(url)); open(f'H_10K_FY{fy}.txt','w',encoding='utf-8').write(t); print(fy,len(t))
