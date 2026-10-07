import sys,os,time
sys.path.insert(0,'.')
from fetch import get,strip
CIK='1758021'
L=[('k2025','0001758021-26-000010','krt-20251231.htm'),('k2024','0001628280-25-012816','krt-20241231.htm'),('k2023','0001628280-24-011444','krt-20231231.htm'),('k2022','0001628280-23-008299','krt-20221231.htm'),('k2021','0001628280-22-007993','krt-20211231.htm'),('k2021A','0001628280-22-029151','krt-20211231.htm'),('q2606','0001758021-26-000026','krt-20260630.htm'),('q2603','0001758021-26-000021','krt-20260331.htm'),('p424b4_2021','0001104659-21-051026','tm2029131-15_424b4.htm'),('s1_2019a','0001144204-19-047791','tv530715_s1a.htm'),('proxy2026','0001758021-26-000015','krt-20260424.htm'),('proxy2023','0001628280-23-014225','krt2022proxywithproxycar.htm')]
for p,acc,doc in L:
    fn=p+'.txt'
    if os.path.exists(fn): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(fn,'w',encoding='utf-8').write(strip(b)); print(fn,os.path.getsize(fn)); time.sleep(0.3)
