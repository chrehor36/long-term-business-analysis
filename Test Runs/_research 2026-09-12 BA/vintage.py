import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
f = sources.sec_facts("0000012927")
for v in ("earliest","newest"):
    o,_,_ = sources.annual(f, ["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"], vintage=v)
    c,_,_ = sources.annual(f, ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"], vintage=v)
    d,_,_ = sources.annual(f, ["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet","DepreciationAndAmortization"], vintage=v)
    s,_,_ = sources.annual(f, ["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"], vintage=v)
    print("vintage",v)
    for w in ([str(y) for y in range(2021,2026)], [str(y) for y in range(2023,2026)]):
        oe_da=[];oe_cx=[]
        for y in w:
            k=y+"-12-31"
            oe_da.append(o[k]-s[k]-d[k]); oe_cx.append(o[k]-s[k]-c[k])
        print("  ",w[0],"-",w[-1],"D&A end %.1f  capex end %.1f"%(sum(oe_da)/len(oe_da), sum(oe_cx)/len(oe_cx)))
    # show restated OCF diffs
    print("   OCF 2021", o.get("2021-12-31"), "2024", o.get("2024-12-31"))
