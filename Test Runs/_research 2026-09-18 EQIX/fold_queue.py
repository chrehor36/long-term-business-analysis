import re
P = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\WATCHLIST RUN QUEUE.md"
t = open(P, encoding="utf-8").read()

# 1. strike in the wave 5 table
old = "~~TOST~~, EQIX, DLR |"
assert t.count(old) == 1
t = t.replace(old, "~~TOST~~, ~~EQIX~~, DLR |")

# 2. dated note beside the capex row, after the TOST note
anchor = "*Dated note, 2026-09-18 (the TOST run)"
i = t.index(anchor)
j = t.index("\n", i)
note = ("\n\n*Dated note, 2026-09-18 (the EQIX run), left beside the table rather than editing its row (operator rule 6): "
"**for EQIX there is NO tag gap on the current screen, but the capex end is incomplete in two ways the five checks did not describe, and the [E5-20] "
"exception class APPLIES - the second name after AMZN.** `owner_earnings()` prices it (`{'5y_da': 885.9M, '5y_capex': -559.9M, '3y_da': 1,029.0M, "
"'3y_capex': -602.2M}`). (i) **The same element carries different values for the same year**: `PaymentsToAcquireProductiveAssets` holds both Equinix's "
"real-estate purchases and its plant capex for FY2010-13 (FY2012: $24.7M and $1,098.6M), and `annual()` kept the small one, overstating FY2010-13 owner "
"earnings by about $1bn a year (outside every five-year window). (ii) **The face of the cash-flow statement carries a second capital line no `CAPX_TAGS` "
"element reaches**: *\"Real estate acquisitions | ( 994 ) | ( 337 ) | ( 384 )\"* beside *\"Purchases of other property, plant and equipment | ( 4,311 )\"* "
"(FY2025 10-K); `PaymentsToAcquireRealEstate` totals $2,878M over FY2015-25. `capital_acquired()` also adds non-cash finance-lease additions ($236M) where "
"the cash cost is lease principal in financing ($155M). **D&A is 90% plant and software** (real-estate depreciation $1,282M, non-real-estate $568M, "
"intangibles $200M); `da_annual()` matches the face ($2,066M). **[E5-20] asked on the filing: YES** - useful lives shortened in FY2024 and FY2025, the "
"company's own project cost per sellable cabinet rose from $58.7k (FY2020) to $126.2k (FY2025) against $80.0k of book plant per cabinet, and older "
"buildings lack the power to fill their own space. The company's \"recurring capital expenditures\" run 11-17% of D&A; the run rejected them as (c), "
"built (c) three ways and set it at total capex less growth ($1.15-2.0bn a year FY2021-25, bracketing depreciation). **The file closed at Q2, not at the "
"capex question.** **Of the seven names now run from this row: ABNB a real presentation gap, AMZN none, NVDA a tag gap plus a history gap, CL a tag gap, "
"SPGI a tag gap plus a (c) question about acquisitions, TOST a tag gap plus a definition break, and EQIX no tag gap but a mis-assigned early-year value "
"and an unread real-estate capital line; the exception class has applied at AMZN and EQIX.** **DLR, the last name in the row, should be checked for the "
"same real-estate line before its run.** (The skip-reason list under `## SKIPPED WITH A REASON` still names EQIX unstruck, as it still names the six "
"before it; it records the triage's reason, and its premise that *\"the only available construction is the D&A end\"* does not hold for EQIX today.)*")
t = t[:j] + note + t[j:]

# 3. register entry at the top of COMPLETED FROM THE QUEUE
entry = open(r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-18 EQIX\register_entry.md", encoding="utf-8").read().rstrip("\n")
h = "\n## COMPLETED FROM THE QUEUE\n"
k = t.index(h) + len(h)
t = t[:k] + entry + "\n" + t[k:]
open(P, "w", encoding="utf-8").write(t)
lines = t.split("\n")
s = next(i for i, l in enumerate(lines) if l.strip() == "## COMPLETED FROM THE QUEUE")
e = next(i for i in range(s + 1, len(lines)) if lines[i].startswith("## "))
print("entries now", sum(1 for l in lines[s+1:e] if re.match(r"^- \*\*[A-Z0-9.\-]+ ?\(", l)))
