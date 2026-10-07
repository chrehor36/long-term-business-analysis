from fetch_core import *
import re
for acc in ["0001104659-26-054713","0001104659-25-065198","0001104659-25-013112"]:
    a=acc.replace("-","")
    t=get(f"https://www.sec.gov/Archives/edgar/data/1874178/{a}/primary_doc.xml")
    names=re.findall(r"<reportingPersonName>(.*?)</reportingPersonName>",t)
    pct=re.findall(r"<classPercent>(.*?)</classPercent>",t)
    amt=re.findall(r"<reportingPersonBeneficiallyOwnedAggregateNumberOfShares>(.*?)</",t)
    ev=re.findall(r"<eventDateRequiresFilingThisStatement>(.*?)</",t)
    print(acc, names[:3], amt[:3], pct[:3], ev)
    time.sleep(0.3)
