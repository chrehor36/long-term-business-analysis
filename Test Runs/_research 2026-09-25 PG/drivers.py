"""Transcribe the TOTAL COMPANY row of each 'Net Sales Change Drivers' table. Transcription only."""
import re
src=[('tenk_FY2014.txt',None),('tenk_FY2017.txt',None),('tenk_FY2019.txt',None),('tenk_FY2020.txt',None)]
import glob
for f in ['tenk_FY2014.txt','tenk_FY2016.txt','tenk_FY2017.txt','tenk_FY2018.txt','tenk_FY2019.txt','tenk_FY2020.txt']:
    L=open(f,encoding='utf-8').read().split('\n')
    for i,l in enumerate(L):
        if 'Net Sales Change Drivers' in l:
            # find TOTAL COMPANY after i
            j=next(k for k in range(i,i+400) if 'TOTAL COMPANY' in L[k] or 'Total Company' in L[k])
            hdr=' '.join(x.strip() for x in L[i:i+40] if x.strip() not in('','|'))[:600]
            row=' '.join(x.strip() for x in L[j:j+40] if x.strip() not in ('','|'))
            row=re.sub(r'\s*\|\s*',' ',row)[:260]
            print(f,'line',i+1,'|',re.sub(r'\s*\|\s*',' ',hdr)[:420]); print('   ROW line',j+1,':',row); print()
