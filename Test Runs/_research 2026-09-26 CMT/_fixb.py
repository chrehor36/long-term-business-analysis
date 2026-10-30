p='beneath.md'
s=open(p,encoding='utf-8').read()
R=[("capital spending of $182.8M against depreciation of $144.8M over the twenty years","capital spending of $169.2M against depreciation of $134.0M ($148.0M of D&A as filed) over the twenty years"),
("with H1 2026 revenue of $121.4M against about $142M in H1 2025","with H1 2026 revenue of $121.3M against $140.7M in H1 2025 (10-Q)"),
("a fixed-charge-coverage covenant that now *\"deduct[s] Consolidated Unfunded Capital Expenditures from the numerator\"*","a fixed-charge-coverage covenant revised *\"by deducting Consolidated Unfunded Capital Expenditures from the numerator thereof\"*")]
for a,b in R:
    assert s.count(a)==1,a; s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
run='../2026-09-26 Run - CMT Core Molding Technologies.md'
t=open(run,encoding='utf-8').read()
assert 'MATERIAL BENEATH THE CLOSE' not in t
open(run,'w',encoding='utf-8').write(t.rstrip('\n')+'\n'+s)
print('ok')
