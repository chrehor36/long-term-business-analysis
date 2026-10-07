import re
def load(f): return re.sub(r'[ \t]+',' ',open(f,encoding='utf-8',errors='replace').read())
pairs=[('6K_2023-11-09_Q3letter.txt',['surpassing $1 trillion in fee-bearing capital by 2028','approximately $5 billion by 2028','close to $150 billion','$7 billion of annual gross carried interest','18% compounded annual growth']),
('6K_2024-11-12_Q3letter.txt',['more than $1 trillion over the next five years','15%+ annual growth','$5.0 billion','by 2034','doubling the size of our business']),
('6K_2024-02-07_Q4_2023.txt',['We raised $93 billion','$143 billion','American Equity Investment Life']),
('10K_FY2025.txt',['approximately 90% of its Distributable Earnings','$108 billion','we do not add performance conditions to our vesting terms','BAM does not have a legal right to the'])]
for f,vals in pairs:
    t=load(f)
    for v in vals:
        print(f[:24], repr(v), 'OK' if v in t else 'MISS')
