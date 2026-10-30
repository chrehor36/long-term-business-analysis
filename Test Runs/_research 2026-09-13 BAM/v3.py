import re
t=re.sub(r'[ \t]+',' ',open('10K_FY2025.txt',encoding='utf-8',errors='replace').read())
q=re.sub(r'[ \t]+',' ',open('10Q_2026Q2.txt',encoding='utf-8',errors='replace').read())
for v in ['3,221,160','375,000','785,664','268','1,611','732','there was no material outstanding litigation',
          'almost entirely based on share price over the long term','not formulaic','sole discretion',
          'at least approximately 90% of its Distributable Earnings','1,240','no material outstanding litigation']:
    print(repr(v),'K:'+('OK' if v in t else '-'),'Q:'+('OK' if v in q else '-'))
