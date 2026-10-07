import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
f = sources.sec_facts("0000012927")
node = f["facts"]
# find tags containing 401 / EmployeeBenefit / Treasury shares issued
for tax in node:
    for t in node[tax]:
        lt = t.lower()
        if "401" in lt or ("treasury" in lt and "issued" in lt) or "employeebenefit" in lt:
            print(tax, t)
