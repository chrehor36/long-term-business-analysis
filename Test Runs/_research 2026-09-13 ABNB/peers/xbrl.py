import sys, json
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 ABNB')
from fetch import get
C={"BKNG":"0001075531","EXPE":"0001324424","TCOM":"0001269238"}
tags=["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","OperatingIncomeLoss"]
for t,c in C.items():
    j=json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json", f"{t}_companyfacts.json"))
    g=j['facts'].get('us-gaap',{})
    for tag in tags:
        if tag not in g: continue
        for unit,vals in g[tag]['units'].items():
            for v in vals:
                if v.get('fp')=='FY' and v.get('form') in ('10-K','20-F') and v['end'][:4] in ('2019','2025') and v['fy'] in (2019,2025) and v['start'][5:]=='01-01' and v['end'][5:]=='12-31':
                    print(t, tag, unit, v['start'], v['end'], v['val'], v['accn'], v['form'])
