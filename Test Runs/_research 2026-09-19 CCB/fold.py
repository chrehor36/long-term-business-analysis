# -*- coding: utf-8 -*-
"""CCB fold - one read-modify-write per shared file, run immediately before the commit.

CONCURRENT RUNS SHARE THIS TREE. The register insert is anchored on a LINE-START regex and
the entries are counted inside the slice from the '## COMPLETED FROM THE QUEUE' heading LINE
to the '## THE WRITE-EARLY PROTOCOL' heading line, because the heading string also appears
inside the FOLD instructions below (10 occurrences in the file) and a bare last-occurrence
search inserts outside the slice the count measures. That is the USAR fold trap.
"""
import io, os, re, sys

ROOT = "C:/Users/chreh/OneDrive/Documents/BRK"
D = os.path.dirname(os.path.abspath(__file__))


def read(p):
    return io.open(os.path.join(ROOT, p), encoding="utf-8").read()


def write(p, s):
    io.open(os.path.join(ROOT, p), "w", encoding="utf-8", newline="").write(s)


def out(m):
    sys.stdout.buffer.write((m + "\n").encode("utf-8", "replace"))


# ---------------------------------------------------------------- 1 + 2: the queue
QP = "Screens/WATCHLIST RUN QUEUE.md"
q = read(QP)

mh = re.search(r"(?m)^## COMPLETED FROM THE QUEUE[ \t]*$", q)
mw = re.search(r"(?m)^## THE WRITE-EARLY PROTOCOL", q)
assert mh and mw and mh.end() < mw.start(), "anchors not found in the expected order"
slice_before = q[mh.end():mw.start()]
n_before = len(re.findall(r"(?m)^- \*\*", slice_before))
assert "**CCB (Coastal Financial Corporation)" not in slice_before, "CCB already entered"
out("register slice: entries before = %d" % n_before)

entry = io.open(os.path.join(D, "fold_queue_entry.md"), encoding="utf-8").read().rstrip("\n")
entry = entry.replace("**Register entry 125**", "**Register entry %d**" % (n_before + 1))
entry = entry.replace("**124 line-start entries before the insert, 125 after",
                      "**%d line-start entries before the insert, %d after"
                      % (n_before, n_before + 1))

# insert at the TOP of the register slice, which is where every prior entry went (newest first)
q = q[:mh.end()] + "\n" + entry + q[mh.end():]

# re-measure inside the same slice
mh2 = re.search(r"(?m)^## COMPLETED FROM THE QUEUE[ \t]*$", q)
mw2 = re.search(r"(?m)^## THE WRITE-EARLY PROTOCOL", q)
n_after = len(re.findall(r"(?m)^- \*\*", q[mh2.end():mw2.start()]))
out("register slice: entries after  = %d  (added %d)" % (n_after, n_after - n_before))
assert n_after == n_before + 1, "insert added %d entries, not one" % (n_after - n_before)

# step 2 - strike the ticker where it reads as unrun. CCB is NOT in the eleven-name WAVE 6
# table (adding a row would falsify its own "eleven" and the 151-of-151 reconciliation), so it
# is struck in the operator-ruling sentence and in the excluded subsection, with a dated note.
a = "**So CCB, ACNB, SOFI, JPM and TFC are run**"
b = "**So ~~CCB~~, ACNB, SOFI, JPM and TFC are run**"
assert a in q, "operator-ruling sentence not found"
q = q.replace(a, b, 1)

a = "**CCB (Coastal Financial) and ACNB (ACNB Corporation)** were priced in the triage"
b = "**~~CCB~~ (Coastal Financial) and ACNB (ACNB Corporation)** were priced in the triage"
assert a in q, "excluded subsection sentence not found"
q = q.replace(a, b, 1)

note = (
    "\n*Dated note, 2026-09-19 (the CCB run), left beside the ruling rather than editing the "
    "eleven-name table (operator rule 6): **CCB is RUN and STRUCK - FAIL at Q2, OUT on the "
    "business. It is struck HERE and in the `#### EXCLUDED UNDER THE OPERATOR'S BANK DIRECTIVE` "
    "subsection below, and NOT as a row in the WAVE 6 table, because CCB is not in that table** - "
    "the table is the eleven businesses the 2026-09-01 triage dropped, CCB was not one of them "
    "(it had already been written down with the financial flag), and adding a twelfth row would "
    "falsify both its own \"eleven\" and the 151-of-151 reconciliation above. The brief for this "
    "run said to strike CCB \"in the WAVE 6 table\"; the table does not contain it, and the "
    "discrepancy is recorded rather than resolved by editing the count. **THE FIRST BANK THIS "
    "PROJECT HAS EVER RUN; four remain (ACNB, SOFI, JPM, TFC), and the run file carries FOUR "
    "STRUCTURAL GAPS the framework has for banks** - chief among them that **[E3-43]** classes a "
    "bank as *\"a business, unlike a franchise\"*, which is why **[E3-29]** raises Q3 to gate "
    "weight, and which read literally makes **Q2 OUT automatic for every bank**; the CCB run did "
    "NOT decide Q2 on that ground (it decided on the counterparties' own filings) and the general "
    "question is the operator's call under PRIME RULE 5. See `Test Runs/2026-09-19 Run - CCB "
    "Coastal Financial.md`, section WHAT THE FRAMEWORK NEEDS IN ORDER TO RUN A BANK.*\n"
)
anchor = ("and the \"EXCLUDED UNDER THE OPERATOR'S BANK DIRECTIVE\" section below is superseded "
          "for those five and kept\nas the record of why they were held.\n")
assert anchor in q, "ruling paragraph tail not found"
q = q.replace(anchor, anchor + note, 1)

write(QP, q)
out("queue written")

# ---------------------------------------------------------------- 3: the narrative fold
NP = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
n = read(NP)
assert "UPDATE 2026-09-19 — CCB" not in n, "narrative fold already present"
narr = io.open(os.path.join(D, "fold_narrative.md"), encoding="utf-8").read()
if not n.endswith("\n"):
    n += "\n"
write(NP, n + narr)
out("narrative fold appended")

# ---------------------------------------------------------------- 3b: the survival shape
SP = "Screens/SURVIVAL SHAPES - index.md"
s = read(SP)
assert "THE INDEMNITY" not in s, "shape 23 already present"
row = ("| 23 | **The indemnity** *(proposed, pending the operator)* | CCB (2026-09-19) | "
       "the balance sheet holds the assets and the legal losses, and the losses have been "
       "contracted away to counterparties smaller and less-capitalised than the lender, so the "
       "reported credit quality is a receivable from the borrowers' own promoters; the promise is "
       "booked as income on the way in and reversed as expense on the way out, and it fails when "
       "one promoter cannot pay | |\n")
m = re.search(r"(?m)^\| 22 \|.*\n", s)
assert m, "shape 22 row not found"
s = s[:m.end()] + row + s[m.end():]
addendum = (
    " CCB proposed THE INDEMNITY (2026-09-19, **the first bank the project has run**), arguing it "
    "is neither #6 nor #11 nor #13: #6 is inverted, because Coastal Community Bank *lends* its "
    "balance sheet to 28 financial-technology partners rather than borrowing one; #11 is present "
    "only as a feature (BaaS loan expense rose from 40.4% to 47.0% of CCBX interest income "
    "FY2023-25 and one partner's own 10-K records an amendment cutting Coastal's program fee "
    "0.75%); and #13 is inverted, because Coastal is the landlord whose rent is being negotiated "
    "down. The mechanism is that **the credit loss is legally the bank's and contractually the "
    "partner's**: CCBX charged off $196.8M in 2025, 11.38% of average CCBX loans, of which 97.7% "
    "was reimbursed, and the matching receivable is recognised as NONINTEREST INCOME when the "
    "allowance is booked - so the loss enters the income statement as revenue and leaves it as a "
    "valuation adjustment. It failed once, in the quarter to 2026-06-30: a $22.8M provision plus a "
    "$46.0M write-down of the credit enhancement asset on ONE non-public partner, $68.8M pre-tax, "
    "14.8% of equity, from 1.26% of assets at 9.66:1 leverage - [E3-29]'s mechanism without "
    "[E3-29]'s ratio."
)
m2 = re.search(r"\*\*All ten are listed so briefs count correctly; none is settled\.\*\*", s)
assert m2, "closing sentence of the Open paragraph not found"
s = s[:m2.start()] + addendum.strip() + " " + s[m2.start():]
s = s.replace("**All ten are listed so briefs count correctly; none is settled.**",
              "**All of the proposed shapes are listed so briefs count correctly; none is "
              "settled.** *(This sentence said \"All ten\" when eleven were proposed; corrected "
              "2026-09-19 by the CCB fold, which made it twelve. Count the table, never this "
              "line.)*", 1)
write(SP, s)
out("survival shape 23 added")

# ---------------------------------------------------------------- the overnight log
LP = "Screens/_daily/OVERNIGHT LOG.md"
l = read(LP)
assert "| CCB |" not in l, "CCB already in the overnight log"
line = (
    "- 2026-09-19 15:43 EDT | CCB | Q1 IN / **Q2 OUT** (on the business; Q3, Q4 and Q6 recorded, "
    "not governing; Q5 did not open and appears only as COMPUTATION - NOT A CLEARANCE, where it "
    "ALSO fails the ~10% floor). **THE FIRST BANK THIS PROJECT HAS EVER RUN**; CIK 0001437958 "
    "found by cik_for() and confirmed, no formerNames, no split, one undimensioned share class. "
    "[E3-03] criterion 2 refuted from the CUSTOMERS' filings, not Coastal's: Dave Inc.'s 10-K says "
    "*\"our partnerships with Evolve and Coastal, our two bank partners\"* and Prosper's originates "
    "personal loans at WebBank while recording an amendment that *\"reduces the program fee "
    "percentage that the Company pays to Coastal by 0.75%\"*; net BaaS loan income per dollar of "
    "CCBX loans 9.71% -> 9.09% -> 8.41%. Eleven-peer row inverted the bull case - Coastal pays "
    "3.52% for CCBX deposits against Pathward's 0.09% and TBBK's 2.06%, so it is NOT getting the "
    "free-deposit prize - but the clean supervisory record held (zero \"consent order\" hits in six "
    "10-Ks, against Green Dot's $44M Fed penalty, Customers Bancorp's Written Agreement and "
    "Metropolitan's two 2023 orders). THE EVENT NO BRIEF KNEW: Q2 2026 net loss $42.1M, ROE "
    "-33.10%, from a $22.8M provision plus a $46.0M valuation adjustment to the credit enhancement "
    "asset on ONE partner - $68.8M pre-tax, 1.26% of assets, 14.8% of equity, [E3-29]'s mechanism "
    "at 9.66:1. Weak-accounting flag fires at full strength: FY2024 material weaknesses in the "
    "COSO control environment for BaaS partner information, a restatement of FY2023 and six "
    "quarters, declared remediated at 2025-12-31 and attested - then the same failure class five "
    "months later. Return on equity capital measured per [E2-01] with a (c) CONVENTION = dAssets x "
    "the Tier 1 leverage ratio: $316.0M of capital required 2021-25 against $204.4M earned, and "
    "$146.3M of the equity increase bought from new shareholders. Stress [E3-24]: the community "
    "bank passes at the corpus's own parameters ($59.5M vs $61.2M of pre-tax - roughly break even) "
    "and the counterparty does not (two enhancement-free years take equity through the 5% "
    "well-capitalised line). Shape #23 THE INDEMNITY proposed. Nothing armed | US$45.97 (2026-09-18, "
    "aggregator, corroborated by Form 4 prices of $41.80 and $46.85) | cap US$702.7M, 15,286,327 "
    "shares from the Q2 2026 10-Q cover 2026-08-03, sovereign 5.34% | Test Runs/2026-09-19 Run - "
    "CCB Coastal Financial.md\n"
)
if not l.endswith("\n"):
    l += "\n"
write(LP, l + line)
out("overnight log line appended")
out("FOLD DONE - steps 1, 2, 3 and the log; step 4 deliberately skipped (Q2 OUT = no alert, no "
    "PORTFOLIO row, QLYS ruling 2026-09-07); step 5 check_framework; step 6 pathspec commit")
