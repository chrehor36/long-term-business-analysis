# -*- coding: utf-8 -*-
"""CCB fold, part 2 - the survival-shape insert and the overnight log.

WHY THIS FILE EXISTS: fold.py asserted on the closing sentence of the Open paragraph in
`Screens/SURVIVAL SHAPES - index.md` and stopped. The reason is the thing the brief warned
about - CONCURRENT RUNS SHARE THIS TREE. Between the CCB run reading that file and folding it,
the CB and BLK folds added shapes 23 (THE CUSHION) and 24 (THE BOUGHT AVERAGE) and rewrote the
closing sentence from "All ten" to "All twelve". The assert did its job: it refused to write a
number that had been taken. THE INDEMNITY is therefore #25, and every reference to "#23" written
by fold.py into the queue entry and the narrative fold is corrected here in the same pass.
"""
import io, os, re, sys

ROOT = "C:/Users/chreh/OneDrive/Documents/BRK"


def read(p):
    return io.open(os.path.join(ROOT, p), encoding="utf-8").read()


def write(p, s):
    io.open(os.path.join(ROOT, p), "w", encoding="utf-8", newline="").write(s)


def out(m):
    sys.stdout.buffer.write((m + "\n").encode("utf-8", "replace"))


# ------------------------------------------------- the shape, renumbered to 25
SP = "Screens/SURVIVAL SHAPES - index.md"
s = read(SP)
assert "THE INDEMNITY" not in s and "The indemnity" not in s, "the shape is already present"
rows = re.findall(r"(?m)^\| (\d+) \|", s)
nmax = max(int(x) for x in rows)
out("highest shape number on disk: %d -> THE INDEMNITY becomes %d" % (nmax, nmax + 1))
assert nmax == 24, "expected 24 shapes on disk, found %d - re-read before writing" % nmax

row = ("| 25 | **The indemnity** *(proposed, pending the operator)* | CCB (2026-09-19) | "
       "the balance sheet holds the assets and the legal losses, and the losses have been "
       "contracted away to counterparties smaller and less-capitalised than the lender, so the "
       "reported credit quality is a receivable from the borrowers' own promoters; the promise is "
       "booked as income on the way in and reversed as expense on the way out, and it fails when "
       "one promoter cannot pay | |\n")
m = re.search(r"(?m)^\| 24 \|.*\n", s)
assert m, "shape 24 row not found"
s = s[:m.end()] + row + s[m.end():]

addendum = (
    "CCB proposed THE INDEMNITY (2026-09-19, **the first bank the project has run**), arguing it is "
    "neither #6 nor #11 nor #13: #6 is inverted, because Coastal Community Bank *lends* its balance "
    "sheet to 28 financial-technology partners rather than borrowing one; #11 is present only as a "
    "feature (BaaS loan expense rose from 40.4% to 47.0% of CCBX interest income FY2023-25, and one "
    "partner's own 10-K records an amendment cutting Coastal's program fee by 0.75%); and #13 is "
    "inverted, because Coastal is the landlord whose rent is being negotiated down. The mechanism is "
    "that **the credit loss is legally the bank's and contractually the partner's**: CCBX charged "
    "off $196.8M in 2025, 11.38% of average CCBX loans, of which 97.7% was reimbursed, and the "
    "matching receivable is recognised as NONINTEREST INCOME at the moment the allowance is booked - "
    "so the loss enters the income statement as revenue and leaves it as a valuation adjustment. It "
    "failed once, in the quarter to 2026-06-30: a $22.8M provision plus a $46.0M write-down of the "
    "credit enhancement asset on ONE non-public partner, $68.8M pre-tax, 14.8% of equity, out of "
    "1.26% of assets at 9.66:1 leverage - **[E3-29]**'s mechanism without [E3-29]'s ratio. "
)
old = "All twelve are listed so briefs count correctly; none is settled."
assert old in s, "closing sentence not found"
new = ("All of the proposed shapes are listed so briefs count correctly; none is settled.** *(This "
       "sentence has said \"All ten\" and then \"All twelve\" while the table grew; the CCB fold of "
       "2026-09-19 found it at twelve and made it thirteen, and two shapes it had planned to number "
       "23 were taken by the CB and BLK folds the same day. **Count the table, never this line.**)*")
s = s.replace("**" + old + "**", addendum + "**" + new, 1)
write(SP, s)
out("survival shape 25 added and the count sentence corrected")

# ------------------------------------------------- correct #23 -> #25 where fold.py wrote it
for p in ("Screens/WATCHLIST RUN QUEUE.md",
          "Screens/2026-08-31 PREPPED READING LIST (operator lists).md",
          "Test Runs/2026-09-19 Run - CCB Coastal Financial.md"):
    t = read(p)
    n = 0
    for a, b in (("#23 THE INDEMNITY", "#25 THE INDEMNITY"),
                 ("SURVIVAL SHAPE #23 \u2014 THE INDEMNITY",
                  "SURVIVAL SHAPE #25 \u2014 THE INDEMNITY"),
                 ("**PROPOSED, #23 \u2014 THE INDEMNITY**",
                  "**PROPOSED, #25 \u2014 THE INDEMNITY**"),
                 ("SURVIVAL SHAPE: #23 THE INDEMNITY", "SURVIVAL SHAPE: #25 THE INDEMNITY"),
                 ("all twenty-two in `Screens/SURVIVAL SHAPES - index.md`",
                  "all twenty-four in `Screens/SURVIVAL SHAPES - index.md` as they stood when this "
                  "file was written; the CB and BLK folds of the same day took 23 and 24, so this "
                  "one is 25")):
        if a in t:
            n += t.count(a)
            t = t.replace(a, b)
    write(p, t)
    out("%s: %d reference(s) renumbered" % (p, n))

# ------------------------------------------------- the overnight log
LP = "Screens/_daily/OVERNIGHT LOG.md"
l = read(LP)
assert "| CCB |" not in l, "CCB already in the overnight log"
line = (
    "- 2026-09-19 15:43 EDT | CCB | Q1 IN / **Q2 OUT** (on the business; Q3, Q4 and Q6 recorded, "
    "not governing; Q5 did not open and appears only as COMPUTATION - NOT A CLEARANCE, where it "
    "ALSO fails the ~10% floor). **THE FIRST BANK THIS PROJECT HAS EVER RUN**; CIK 0001437958 found "
    "by cik_for() and confirmed - no formerNames, no split, one undimensioned share class, so none "
    "of the HBB/LCID/SOUN/BIRD count layers arise. [E3-03] criterion 2 refuted from the CUSTOMERS' "
    "filings rather than Coastal's: Dave Inc.'s 10-K says *\"our partnerships with Evolve and "
    "Coastal, our two bank partners\"*, and Prosper's originates personal loans at WebBank while "
    "recording an amendment that *\"reduces the program fee percentage that the Company pays to "
    "Coastal by 0.75%\"*; net BaaS loan income per dollar of average CCBX loans 9.71% -> 9.09% -> "
    "8.41%. The eleven-peer row inverted the bull case - Coastal pays 3.52% for CCBX deposits "
    "against Pathward's 0.09% and The Bancorp's 2.06%, so it is NOT getting the free-deposit prize - "
    "while the clean supervisory record HELD (zero \"consent order\" hits in six 10-Ks, against "
    "Green Dot's $44M Fed penalty, Customers Bancorp's Written Agreement plus Pennsylvania order and "
    "Metropolitan's two 2023 orders). THE EVENT NO BRIEF KNEW: Q2 2026 net loss $42.1M, ROE -33.10%, "
    "from a $22.8M provision plus a $46.0M valuation adjustment to the credit enhancement asset on "
    "ONE partner - $68.8M pre-tax, 1.26% of assets, 14.8% of equity, [E3-29]'s mechanism at 9.66:1. "
    "Weak accounting fires at full strength: FY2024 material weaknesses in the COSO control "
    "environment for BaaS partner information, a restatement of FY2023 and six quarters, declared "
    "remediated at 2025-12-31 and attested by Baker Tilly - then the same failure class five months "
    "later. Return on equity capital measured per [E2-01] with a (c) CONVENTION = dAssets x the Tier "
    "1 leverage ratio: $316.0M of capital required 2021-25 against $204.4M earned, and $146.3M of "
    "the equity increase bought from new shareholders; ROE 18.24% -> 10.17% -> -12.04%. Stress "
    "[E3-24]: the community bank passes at the corpus's own parameters ($59.5M against $61.2M of "
    "pre-tax, roughly break even) and the counterparty does not (two enhancement-free years take "
    "equity through the 5% well-capitalised line). Shape #25 THE INDEMNITY proposed. Four framework "
    "gaps for banks written up for the operator. Nothing armed | US$45.97 (2026-09-18, aggregator, "
    "corroborated by Form 4 prices of $41.80 and $46.85) | cap US$702.7M, 15,286,327 shares from the "
    "Q2 2026 10-Q cover of 2026-08-03, sovereign 5.34% | Test Runs/2026-09-19 Run - CCB Coastal "
    "Financial.md\n"
)
if not l.endswith("\n"):
    l += "\n"
write(LP, l + line)
out("overnight log line appended")
