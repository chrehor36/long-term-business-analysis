import json,urllib.request,time,re
from fetch import get, strip
for t,cik in [('TTEK','0000831641'),('MMS','0001032220')]:
    u='https://efts.sec.gov/LATEST/search-index?q=%22ICF+International%22&forms=10-K&ciks='+cik
    j=json.loads(get(u))
    hits=sorted(j['hits']['hits'],key=lambda h:h['_source']['file_date'],reverse=True)
    h=hits[0]; src=h['_source']; adsh=src['adsh']; fn=h['_id'].split(':')[1]
    url='https://www.sec.gov/Archives/edgar/data/%d/%s/%s'%(int(cik),adsh.replace('-',''),fn)
    print(t,src['file_date'],adsh,fn,src.get('period_ending'))
    s=strip(get(url)); open('peer_%s_10K.txt'%t,'w',encoding='utf-8').write(s)
    for m in re.finditer(r'[^.]*ICF International[^.]*\.',s): print('   ',m.group(0).strip()[:900])
    time.sleep(1)
