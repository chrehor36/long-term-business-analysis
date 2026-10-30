import os, re
D = os.path.dirname(os.path.abspath(__file__))
Q = os.path.join(D, "..", "..", "Screens", "WATCHLIST RUN QUEUE.md")
t = open(Q, encoding="utf-8").read()
orig = t

# 1. Register entry at the top of COMPLETED FROM THE QUEUE, above BAM
entry = open(os.path.join(D, "fold_entry.md"), encoding="utf-8").read()
anchor = "## COMPLETED FROM THE QUEUE\n"
i = t.index(anchor) + len(anchor)
assert t[i:i + 60].startswith("- **BAM (Brookfield Asset Management Ltd.)"), t[i:i + 80]
t = t[:i] + entry + t[i:]

# 2. Strike BN in the MINI BERK roster with a one-line annotation
old = "business; see COMPLETED)*, BN\n"
assert t.count(old) == 1
new = ("business; see COMPLETED)*, ~~BN~~ *(run 2026-09-13 - FAIL at Q2, OUT on the business: a holding company, not an "
       "asset manager, and no leg carrying the weight is a franchise; see COMPLETED)*\n")
t = t.replace(old, new)

# 2b. Dated note beside the 2026-09-02 BLOCKED paragraph's existing note
old2 = ("control of Oaktree. Verdict **Q2 OUT**; the entry is in `## COMPLETED FROM THE QUEUE`. **BN is still\n"
        "unrun and the paragraph still governs it.***\n")
assert t.count(old2) == 1
note2 = old2 + ("\n*Dated note, 2026-09-13 (later the same day), left beside the two paragraphs above rather than replacing them "
                "(operator rule 6):* ***BN WAS RUN ON 2026-09-13** and the paragraph no longer governs any name. It was wrong on the "
                "facts for BN: BN is a holding company that owns 74% of an asset manager, not an asset manager, with an audited "
                "parent-only balance sheet (40-F Note 1) and a separate SEC filer for every leg, so the perimeter was measurable. It "
                "was right that no five-year window on one perimeter exists. Verdict **Q1 IN / Q2 OUT**; the entry is in "
                "`## COMPLETED FROM THE QUEUE`. The same stale wording survives in `Framework/SECTOR METHOD - owner earnings for "
                "insurers and float-bearing holding companies.md` (\"It does not resolve BAM/BN\" and \"BAM and BN stay blocked\"); "
                "that document is outside this run's permission to edit and is flagged to the operator.*\n")
t = t.replace(old2, note2)

# 2c. Dated note beside the backfill line that says BN remains unrun
old3 = "**BN remains unrun and the sentence above still holds for it.***\n"
assert t.count(old3) == 1
note3 = old3 + ("\n*Dated note, 2026-09-13 (later the same day), added beside the lines above rather than rewriting them "
                "(operator rule 6):* ***BN was run** and is now struck in the roster, with price, share count, the filing and "
                "accession it came from, cap, sovereign and a PASS/FAIL line in `## COMPLETED FROM THE QUEUE` (Q1 IN / Q2 OUT). "
                "**No name in the MINI BERK roster remains unrun or BLOCKED.***\n")
t = t.replace(old3, note3)

assert t != orig
open(Q, "w", encoding="utf-8").write(t)
print("queue folded")
print([m.start() for m in re.finditer(r"\bBN\b.{0,40}(BLOCKED|unrun|blocked)", t)][:10])
