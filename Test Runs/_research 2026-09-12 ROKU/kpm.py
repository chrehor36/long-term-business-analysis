import re
files={2017:'10K_FY2017.txt',2018:'10K_FY2018.txt',2019:'10K_FY2019.txt',2020:'10K_FY2020.txt',
2021:'10K_FY2021.txt',2022:'10K_FY2022.txt',2023:'10K_FY2023.txt',2024:'10K_FY2024.txt',2025:'10K_FY2025.txt'}
for y,f in files.items():
    t=open(f,encoding='utf-8').read()
    print("="*20,y)
    for pat in [r'[^.\n]{0,90}(?:active accounts|Streaming Households)[^.\n]{0,140}\.',
                r'ARPU (?:was|grew|increased|decreased)[^.\n]{0,150}\.',
                r'(?:streamed|Streaming Hours were)[^.\n]{0,140}(?:billion|hours)[^.\n]{0,80}\.']:
        for m in re.finditer(pat,t,re.I):
            s=m.group(0)
            if re.search(r'\d',s) and ('million' in s or 'billion' in s or '$' in s):
                print('  ',s.strip()[:260])
