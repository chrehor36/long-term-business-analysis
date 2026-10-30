import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
f = sources.sec_facts("0000012927")
for tags,label in [(["PaymentsForRepurchaseOfCommonStock"],"buybacks $M"),
                   (["PaymentsOfDividendsCommonStock","PaymentsOfDividends"],"common dividends $M"),
                   (["TreasuryStockValueAcquiredCostMethod"],"treasury acquired $M")]:
    d,u,un = sources.annual(f, tags, vintage="newest")
    print(f"\n{label} ({u})")
    tot=0
    for e in sorted(d):
        print("  ",e[:4], f"{d[e]:>9,.0f}")
        if 2013 <= int(e[:4]) <= 2019: tot+=d[e]
    print("   FY2013-2019 total:", f"{tot:,.0f}")
