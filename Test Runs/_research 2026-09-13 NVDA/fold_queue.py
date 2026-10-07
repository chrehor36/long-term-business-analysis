"""The NVDA fold, steps 1-2: register entry at the top of COMPLETED FROM THE QUEUE, strike in the WAVE 5 table, dated note beside it."""
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
p = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
t = open(p, encoding="utf-8").read()
entry = open(ROOT + r"\Test Runs\_research 2026-09-13 NVDA\fold_register.md", encoding="utf-8").read()
h = "## COMPLETED FROM THE QUEUE\n"
assert t.count(h) == 1 and "- **NVDA (NVIDIA" not in t
t = t.replace(h, h + entry, 1)
old = "| capex unresolved [E5-20]: build (c) by hand from the filing | ~~ABNB~~, ~~AMZN~~, NVDA, CL, SPGI, TOST, EQIX, DLR |"
assert old in t
t = t.replace(old, old.replace(" NVDA,", " ~~NVDA~~,"))
anchor = "(for Amazon the filing answered it: the server-life shortening puts the plant in the exception class).*\n"
assert t.count(anchor) == 1
note = ("\n*Dated note, 2026-09-13 (the NVDA run), left beside the table rather than editing its row (operator rule 6): **for NVDA the label was the same tooling "
        "artefact and something more.** `floor_screen.py` at `a8bc84f` returns `CAPEX_UNRESOLVED` because NVIDIA used `PaymentsToAcquirePropertyPlantAndEquipment` "
        "only for FY2010-FY2012; the current screen prices it. **But companyfacts carries no capex fact under any tag for FY2013-FY2021**, so the fix does not reach "
        "any window longer than five years: those must be built from the filed cash-flow statements (the run did, FY2017-TTM). **The [E5-20] question, asked on the "
        "filing, answered no for the plant**: NVIDIA lengthened server lives in February 2023, capex ran 1.28-2.61x depreciation, and the two plant ends differ by "
        "about 4%; the product cadence writes down inventory, and those provisions are already inside operating cash flow. **Of the three names run from this row, "
        "one had a real presentation gap (ABNB), one had no gap (AMZN), and one had a tag gap plus a history gap (NVDA); the exception class applied only at AMZN.** "
        "CL, SPGI, TOST, EQIX and DLR should still go through the current `owner_earnings()`, and a check for missing early-year capex facts, before their runs.*\n")
t = t.replace(anchor, anchor + note, 1)
open(p, "w", encoding="utf-8").write(t)
print("queue updated")
