import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
L=[('FY2009','0000950123-09-037707','h67823e10vk.htm'),('FY2010','0000950123-10-082514','h75463e10vk.htm'),('FY2011','0000950123-11-081150','h84293e10vk.htm'),('FY2012','0000096021-12-000062','syy-20120630x10k.htm'),('FY2013','0000096021-13-000073','syy-20130629x10k.htm'),('FY2014','0000096021-14-000040','syy-20140628x10k.htm'),('FY2015','0000096021-15-000057','syy201510-k.htm'),('FY2016','0000096021-16-000275','syy201610-k.htm'),('FY2017','0000096021-17-000120','syy201710-k.htm'),('FY2018','0000096021-18-000126','syy2018q410-k.htm'),('FY2019','0000096021-19-000093','syy2019q410-k.htm'),('FY2020','0000096021-20-000100','syy-20200627.htm'),('FY2021','0000096021-21-000093','syy-20210703.htm'),('FY2022','0000096021-22-000151','syy-20220702.htm'),('FY2023','0000096021-23-000117','syy-20230701.htm'),('FY2024','0000096021-24-000128','syy-20240629.htm'),('FY2025','0000096021-25-000099','syy-20250628.htm')]
for fy,acc,doc in L:
    fn=f'tenk_{fy}.txt'
    if os.path.exists(fn): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/96021/{acc.replace("-","")}/{doc}')
    open(fn,'w',encoding='utf-8').write(strip(b)); print(fn,os.path.getsize(fn)); time.sleep(0.3)
