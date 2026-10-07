import json,os,sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
OUT=os.path.dirname(os.path.abspath(__file__))
MAP={"PINS":("companyfacts.json","10K_FY2025.txt",1000),"META":("cf_META.json","META_10K_FY2025.txt",1_000_000),
 "GOOGL":("cf_GOOGL.json","GOOGL_10K_FY2025.txt",1_000_000),"SNAP":("cf_SNAP.json","SNAP_10K_FY2025.txt",1000),
 "RDDT":("cf_RDDT.json","RDDT_10K_FY2025.txt",1000),"TTD":("cf_TTD.json","TTD_10K_FY2025.txt",1000)}
TAGS=["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","OperatingIncomeLoss","NetIncomeLoss",
 "NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","PaymentsToAcquirePropertyPlantAndEquipment",
 "DepreciationDepletionAndAmortization"]
for tk,(cfn,txt,scale) in MAP.items():
    cf=json.load(open(os.path.join(OUT,cfn))); us=cf["facts"]["us-gaap"]
    t=open(os.path.join(OUT,txt),encoding="utf-8").read()
    print(f"\n=== {tk} FY2025 cross-check (units scale 1/{scale}) ===")
    for tag in TAGS:
        d=us.get(tag)
        if not d: continue
        best=None
        for unit,rows in d["units"].items():
            for r in rows:
                if r.get("form")!="10-K" or r.get("end")!="2025-12-31" or not r.get("start"): continue
                if not (330<=(date.fromisoformat("2025-12-31")-date.fromisoformat(r["start"])).days<=400): continue
                if best is None or r["accn"]>best[1]: best=(r["val"],r["accn"])
        if not best: continue
        v=best[0]//scale if scale>1 else best[0]
        s=f"{abs(int(v)):,}"
        print(f"  {tag:58s} {best[0]:>16,} -> search {s!r}: n={t.count(s)}  acc={best[1]}")
