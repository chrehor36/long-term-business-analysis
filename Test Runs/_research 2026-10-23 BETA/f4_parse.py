import json,sys,os,time,urllib.request,re
import xml.etree.ElementTree as ET
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
d=json.load(open('cache/submissions.json'));r=d['filings']['recent']
out=[]
for i in range(len(r['form'])):
    if r['form'][i]!='4' or r['filingDate'][i]<'2026-01-01': continue
    acc=r['accessionNumber'][i]; doc=r['primaryDocument'][i].split('/')[-1]
    fn=f"cache/f4/{acc}.xml"
    if not os.path.exists(fn):
        url=f"https://www.sec.gov/Archives/edgar/data/1784570/{acc.replace('-','')}/{doc}"
        try:
            data=urllib.request.urlopen(urllib.request.Request(url,headers=UA)).read()
        except Exception as e:
            print('ERR',acc,e); continue
        open(fn,'wb').write(data); time.sleep(0.25)
    t=ET.parse(fn).getroot()
    owner=t.findtext('.//reportingOwner/reportingOwnerId/rptOwnerName')
    title=t.findtext('.//reportingOwnerRelationship/officerTitle') or ('Director' if t.findtext('.//reportingOwnerRelationship/isDirector') in ('1','true') else '') or ('10%' if t.findtext('.//reportingOwnerRelationship/isTenPercentOwner') in ('1','true') else '')
    for tx in t.findall('.//nonDerivativeTransaction'):
        code=tx.findtext('.//transactionCoding/transactionCode')
        sh=float(tx.findtext('.//transactionAmounts/transactionShares/value') or 0)
        p=tx.findtext('.//transactionAmounts/transactionPricePerShare/value')
        p=float(p) if p else 0
        dt=tx.findtext('.//transactionDate/value')
        plan='10b5-1' if '10b5-1' in open(fn,encoding='utf-8',errors='ignore').read() else ''
        out.append((dt,owner,title,code,sh,p,acc,plan))
agg={}
for o in out:
    k=(o[1],o[2],o[3]); a=agg.setdefault(k,[0,0,o[0],o[0],set()]); a[0]+=o[4]; a[1]+=o[4]*o[5]; a[2]=min(a[2],o[0]); a[3]=max(a[3],o[0]); a[4].add(o[7])
for k,v in sorted(agg.items(),key=lambda x:-x[1][1]):
    print(k, 'shares %.0f value $%.1fM'%(v[0],v[1]/1e6), v[2],'to',v[3], v[4])
