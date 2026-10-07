# COMPUTATION - NOT A CLEARANCE. Q7 convention arithmetic only, run after a Q2 close at the owner's request.
r = 0.0566; sh = 60.5; tax = 98.8/468.7
def val(C, g):
    v = sum(C*(1+g)**t/(1+r)**t for t in range(1,11))
    return v + C*(1+g)**10/r/(1+r)**10
oc_capex = [607,66,695,652,586]; oc_da = [692,51,678,468,374]
for name, s in [("capex", oc_capex), ("D&A", oc_da)]:
    C = sum(s)/5; g = (s[-1]/s[0])**(1/4)-1
    print(name, "C", round(C), "g", round(100*g,2), "no-growth $/sh", round(val(C,0)/sh,2), "shown-growth $/sh", round(val(C,g)/sh,2),
          "fair(10% pre-tax) $/sh", round(C/(1-tax)/0.10/sh,2), "15% pre-tax $/sh", round(C/(1-tax)/0.15/sh,2),
          "pre-tax yield at 124.93", round(100*C/(1-tax)/(124.93*sh),2))
# whole-cycle variant: owner cash / sales FY2009-FY2025 applied to FY2025 sales
for name, tot in [("capex wc", 7722), ("D&A wc", 8148)]:
    C = tot/148969*10785.4
    print(name, "C", round(C), "no-growth $/sh", round(val(C,0)/sh,2), "fair $/sh", round(C/(1-tax)/0.10/sh,2), "15% $/sh", round(C/(1-tax)/0.15/sh,2))
print("tax", round(tax,3))
