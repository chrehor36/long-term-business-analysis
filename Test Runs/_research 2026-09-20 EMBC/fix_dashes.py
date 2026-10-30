# Replace em dashes in this run's OWN prose. Template headings, template boilerplate and
# verbatim corpus/filing quotes keep theirs (PRIME RULE 1: verbatim only).
p = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-20 Run - EMBC Embecta.md"
s = open(p, encoding="utf-8").read()
M = "\u2014"
pairs = [
 ("### FLAG 1 "+M+" the `deal_note`:", "### FLAG 1. The `deal_note`:"),
 ("### FLAG 2 "+M+" the `cap_flag`:", "### FLAG 2. The `cap_flag`:"),
 ("### FLAG 3 "+M+" the `name_change_note`:", "### FLAG 3. The `name_change_note`:"),
 ("**Needed or desired** [x] "+M+" yes,", "**Needed or desired** [x]. Yes,"),
 ("**No close substitute** [ ] "+M+" **FAILS", "**No close substitute** [ ]. **FAILS"),
 ("**Not price-regulated** [~] "+M+" not price-regulated", "**Not price-regulated** [~]. Not price-regulated"),
 ("### [E4-04] "+M+" and the brand basis", "### [E4-04], and the brand basis"),
 ("structure, or merely narrow it "+M+" and does the spending", "structure, or merely narrow it, and does the spending"),
 ("The pre-2022 economics "+M+" a 39.4% net margin\nin FY2020 "+M+" came from riding a wave:",
  "The pre-2022 economics, a 39.4% net margin\nin FY2020, came from riding a wave:"),
 ("### THE COMPETITOR ROW "+M+" required", "### THE COMPETITOR ROW, required"),
 ("**Terumo Medical Corporation** "+M+" Japanese parent", "**Terumo Medical Corporation**. Japanese parent"),
 ("**Ypsomed** "+M+" SIX Swiss Exchange", "**Ypsomed**. SIX Swiss Exchange"),
 ("**MTD Group** "+M+" private Chinese manufacturer", "**MTD Group**. Private Chinese manufacturer"),
 ("**Medtronic Diabetes / MiniMed** "+M+" was inside", "**Medtronic Diabetes / MiniMed**. Was inside"),
 ("**The attacker's test [E2-45]** "+M+" how would I compete", "**The attacker's test [E2-45]**. How would I compete"),
 ("filed metric "+M+" units, price, gross margin", "filed metric: units, price, gross margin"),
 ("## BENEATH THE CLOSE "+M+" READ, AND NOT SCORED", "## BENEATH THE CLOSE: READ, AND NOT SCORED"),
 ("## COMPUTATION "+M+" NOT A CLEARANCE", "## COMPUTATION: NOT A CLEARANCE"),
 ("**If UNRESEARCHED "+M+" THE WORK ORDER:**", "**If UNRESEARCHED, THE WORK ORDER:**"),
]
for a, b in pairs:
    if a not in s:
        print("MISS:", a[:70])
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("remaining em dashes:", s.count(M))
