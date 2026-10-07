import re,html,urllib.request
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
for y,a,d in [(2024,'000164437824000042','rmr-20240930.htm'),(2023,'000164437823000051','rmr-20230930.htm'),(2022,'000164437822000047','rmr-20220930.htm')]:
    u=f'https://www.sec.gov/Archives/edgar/data/1644378/{a}/{d}'
    s=urllib.request.urlopen(urllib.request.Request(u,headers=UA)).read().decode('utf-8','ignore')
    s=re.sub(r'(?is)<[^>]+>',' ',s); s=html.unescape(s); s=re.sub(r'[ \t\xa0\n]+',' ',s)
    m=re.findall(r'.{0,80}billion of assets under management.{0,40}',s)
    print(f'FY{y}:', m[0].strip() if m else 'NOT FOUND')
    m2=re.findall(r'Private Capital.{0,120}?\$[\d.]+ billion',s)
    if m2: print('    PC:', m2[0][:200])
