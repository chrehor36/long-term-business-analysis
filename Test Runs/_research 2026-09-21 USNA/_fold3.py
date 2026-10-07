import io
narr = """

---

# USNA (USANA Health Sciences) - FOLD, 2026-09-21. Q2 OUT. Register entry 156.

**Run file:** `Test Runs/2026-09-21 Run - USNA USANA Health Sciences.md`.
**Research:** `Test Runs/_research 2026-09-21 USNA/`.
**Price $14.40 (2026-09-21, aggregator, flagged) x 18,476,534 shares (10-Q cover at 2026-08-11,
accession `0000896264-26-000056`) = cap $266.1M. Sovereign USD 5.34% (US Treasury daily par yield
curve, 09/18/2026).**

### THE SCREEN'S LOUDEST FLAG WAS OURS, NOT THE COMPANY'S

The row carried `cap_flag`: *"CAP BELOW FILED PUBLIC FLOAT - cap $263M against a filed float of
$328M (1.25x) as of 2025-06-27. A cap cannot be smaller than a subset of itself."* **Neither input
was wrong. The comparison was.** The $328M is the 10-K cover-page **non-affiliate market value**,
which Form 10-K requires to be struck at the last business day of the registrant's most recently
completed **second fiscal quarter** - here 2025-06-27, *"based on a closing market price of $31.13
per share"*, which the price series matches to the cent. The cap is struck at $14.40 fifteen months
later. **The stock fell 53.7% between the two dates.** The implied non-affiliate count, 10.5M shares
against ~19M outstanding, is exactly consistent with Gull Global (the founder Dr Myron Wentz) at
40.1% in the proxy.

**TOOLING DEFECT, RECORDED NOT FIXED.** `cap_flag` compares a live cap with a figure that can be
**up to eighteen months stale**, and in any stock that has halved it will print a claim of
arithmetic impossibility that is false. The fix is a date test, not a ratio test: the flag should
compare the float against **the cap computed at the float's own measurement date**, or refuse in
words the way `level_shift` and `growth_required` now do. **It is not fixed here** because a screen
rebuild is not a run's work and 331 rows would re-price; it is written down with the arithmetic that
proves it. **What the flag did right must be said too: it sent the run to the cover page, which is
where operator rule 4 wanted it, and the cover page is where the real share count was.** A false
positive with a true instruction is still worth firing.

### THE FINDING: A COMPANY THAT TELLS ITS OWNERS IT HAS NO MOAT, TWICE, IN ONE 10-K

Item 1, Competition: *"Our business through USANA, Hiya, and Rise is **very competitive and the
barriers to entry are not significant** ... many of our competitors are significantly larger, have
a longer operating history, higher visibility and name recognition, and greater financial
resources."* Item 1A: *"Entry to market is **not particularly capital intensive or otherwise
subject to high barriers** and as a result, **new competitors can enter easily and compete with us
for customers and distributors, including our Brand Partners.**"*

**[E3-03] condition (2) - no close substitute - is denied by the registrant**, and the row's own
demonstration test fails in both halves: the company raised prices in FY2025 (average spend +4.4%)
and **lost 14.8% of its active Customers in the same year**, which is [E2-44]'s first characteristic
inverted; and return on equity ran **28-33% every year from FY2010 to FY2021** and then **16.0 /
12.8 / 7.9 / 2.0%**, with operating margin **15.6% (FY2020) to 4.0% (FY2025)**.

**The [E4-04] verdict form of 2026-09-20 was applied and does not reach this name.** That ruling
sends to **UNKNOWABLE at Q2** a name that *passes* [E3-03] and whose durability cannot be judged
from filings. USNA does not pass [E3-03]. The evidence is in, and it fails: **OUT on the business.**

### [E4-55] IS THE WHOLE STORY, AND IT IS PRECISION STEEL AGAIN

Active Customers, each figure read from that year's own 10-K: **471,000 (FY2016), 565,000, 616,000
(FY2018, the peak), 586,000, 599,000, 560,000, 490,000, 483,000, 454,000, 387,000 (FY2025), 384,000
(2026-07-04). Minus 37% in seven years**, down in all four reported regions in FY2025.

**And consolidated net sales ROSE 8.3% in FY2025** - to $925.3M - **only because $130.0M of
purchased Hiya revenue was added.** Munger's 2006 Wesco row is the exact template: *"a precipitous
drop in physical volume"* with *"dollar volume roughly level"*. Here the dollar line was held up by
**price and by an acquisition at once**, and the physical series is the honest one. **Any run in
this queue on a company that publishes a unit count should read the unit count first.**

### THE COMPETITOR ROW: SEVEN OF SEVEN ARE SHRINKING - IT IS THE WAVE, NOT THE SURFER

Specification stated before building: every listed company whose primary business is selling
nutrition or wellness product through a commissioned distributor network, on **net sales and
operating margin from its own SEC-filed annual accounts, FY2018-FY2025**, newest vintage.

Peak-to-FY2025 net sales: **NHTC -79%, MED -76%, BODI -71%, NUS -45%, MTEX -38%, USNA core -35%,
LFVN -21%, HLF -13%.** Three of seven lost money at the operating line in FY2025. Their own filings
say the same in units: Nu Skin *"Customers decreased 10%, Paid Affiliates decreased 11% and Sales
Leaders decreased 19%"*; NHTC *"We had 14% fewer active members at December 31, 2025"*; Medifast
*"a decrease in the number of active earning coaches."*

**This is [E3-51]'s broken wave.** USANA's 2010-2021 record was real - it led the row on operating
margin in FY2018 at 15.8% - and **[E4-36]**'s fourth cause, *"Catching and riding some sort of big
wave"*, is the honest account of it. All seven surfers came off the same wave within four years,
which is the evidence that the advantage lived in the wave. USANA's 4.0% now sits **below
Herbalife's 9.5%**.

**A prior of mine was refuted by the row.** I expected the decline to be China-specific and
regulatory, because China is 41.3% of net sales and Item 1A devotes pages to it. **It is not.**
FY2025 units fell in Greater China (-15.4%), Southeast Asia Pacific (-18.2%), North Asia (-7.9%)
**and the Americas and Europe (-12.9%)** - and the US market's own line is the worst of the named
markets at -14.9% customers. A China thesis would have explained one region and missed the fact.

### THE PERIMETER: THE $210M IS TWO EVENTS, AND ONLY ONE IS A BREAK

Rise and Oola, FY2022, **$6,532 thousand** - immaterial against $103.9M of operating cash that year.
**Hiya Health Products LLC, closed 2024-12-23, $206,074 thousand cash for 78.85%**, of which
intangibles $124,200 and **goodwill $127,264**; $209.9M in total, **78.9% of the re-struck cap.**
**One real break in the series, at FY2025** - the first full Hiya year, which more than doubles D&A
from $14,539 to $32,562 almost entirely on acquired-intangible amortisation - plus a 53rd week in
the same year. **The brief's instruction to count the breaks rather than assume one was the right
instruction and it changed the reading**: every year before FY2025 is the core direct-selling
business plus a rounding error, which is what makes the long windows legible at all.

**And the acquisition is already marked down by the company.** $29,137 thousand of the Hiya goodwill
was impaired in **Q2 2026, eighteen months after closing**, on *"current lower-than-expected
financial performance"*; Hiya's FY2026 sales guidance was cut from $140-155M to $125M and Rise's
from $65-80M to $35M.

### THE SPREAD REBUILT, AND THE `spread_caveat` WAS RIGHT TO DEMAND IT

The row said the width was *"4-construction only (3y/5y x two capex ends): CANNOT see variation
older than the 5-year window; rebuild it [E4-25]."* Rebuilt across **all seventeen filed annual
periods and both (c) ends**: **owner earnings $17.0M to $79.0M, a 4.6-fold range, 6.40% to 29.67%
on the $266.1M cap.** The screen's construction saw $17M-$49M; **the rebuild widens the top end by
61%.** Five-year (the [E2-42] default) $44.4-49.4M; three-year $17.0-24.2M, **below the [E4-28]
floor at both ends**; **FY2025 alone is negative at both ends, $(24.1)M to $(5.3)M.** [E4-25]
answers its own question: a range that wide *is* the conclusion.

### "STEP DOWN" IS THE WRONG WORD FOR WHAT THE FILINGS SHOW

Three flags fired - `level_shift` 0.39, `level_shift_oe` 0.23, `level_shift_full` 0.48 - each
captioned *"STEP DOWN - the series has changed level."* **The ratios are right and the caption is
wrong, and the difference matters for how a reader treats the mean.** A step implies a level change
at a date. This is a **six-year slide**: the rolling five-year owner-earnings mean falls at every
anchor, **$108M to $105M to $89M to $77M to $44M**, and the direction never reverses.

Two hinges have filed reasons. **FY2022**: sales -15.8%, units -12.5%, margin 14.3% to 10.8%, as the
pandemic-era surge in at-home supplement buying and virtual recruiting ended. **FY2025**: units
-14.8%, margin 7.8% to 4.0%, operating cash -63%, with four causes in one year - continued unit
erosion, the first Hiya year, the $6,463 cost realignment plus $6,967 impairment, and a **72.4%
effective tax rate** because losses in some jurisdictions earn no benefit (the deferred-tax valuation
allowance went $156.1M to $178.7M). Operating cash also absorbed a **$34,685 inventory build**.

**Suggested wording change, recorded not made:** where the early and late halves differ but the
series is monotone, the flag should say **SLIDE** and name the count of consecutive declining years,
because "STEP" invites a reader to look for a date and to treat the post-step level as the new
stable one. There is no stable level here.

### RECORDED BENEATH THE CLOSE, GOVERNING NOTHING

- **[E4-29] and [E4-22]'s third flag fire in the furnished 8-Ks and are quiet in the 10-K narrative
  - the standing CGNX rule earning its keep for the second wave-7 name.** Adjusted EBITDA and
  Adjusted diluted EPS head the Key Results table of all three EX-99.1s. **FY2025 GAAP net earnings
  $10.8M against a headline Adjusted EBITDA of $101.3M; GAAP diluted EPS $0.58 against Adjusted
  $1.93.** And the measure is not merely promotional: **Note O sets the Hiya put price on "Hiya's
  Adjusted EBITDA (as defined in the LLC Agreement)"**, so a non-GAAP number determines a real cash
  obligation. That is a shape worth carrying forward - **when a non-GAAP metric is written into a
  contract, the incentive [E4-27] to define it generously is contractual, not just rhetorical.**
- **[E3-48] performed on the record.** FY2026 guidance issued 2026-02-17 at net earnings
  **$20.3M-$26.6M**; *"reaffirming our fiscal 2026 guidance across all metrics"* on 2026-05-05;
  **cut to $(11)M on 2026-08-04.** A profit forecast became a loss forecast in under six months,
  having been reaffirmed at the halfway point.
- **[E5-08]/[E5-24] capital allocation.** **$281.7M of buybacks in six years** - $177.8M of it in
  FY2021, the year the shares closed at **$101.20**, and $27.5M in FY2025 at **$29.92 a share**
  against $14.40 today. Plus $206.1M for Hiya. **$488M deployed in six years by a company now worth
  $266.1M.** [E3-54]'s retention test: $302.4M of earnings retained FY2021-FY2025 while market value
  went from about $1.94bn to $266.1M. Stated with [E4-13]'s humility clause and binding nothing,
  because there is no position.
- **[E4-30]'s cash-tax tell does NOT fire, and a test that does not fire is recorded as not
  firing.** Cash taxes **rose** to 89.5% of pretax income, for a disclosed economic reason.
- **No integrity finding of any kind.** KPMG unchanged (Auditor Firm ID 185), no restatement, no
  late filing, no enforcement matter in the filings read. **No Q3 verdict was taken** (operator
  rule 2).
- **The balance sheet is the counter-case and it is real** ([E4-51] requires it stated): cash
  **$168,560 thousand at 2026-07-04, 63% of the market cap**, zero drawn debt, H1 2026 operating
  cash **up** year-on-year at $33,078. The redeemable NCI sits at $44,667 in the mezzanine, puttable
  from 2028-04-30 and 2030-04-30, **priced on Hiya's Adjusted EBITDA - so it shrinks as Hiya
  shrinks** ([E3-52]: no covenant, long date, a different animal from bank debt). **The named death
  is not insolvency; it is the arrival at net cash**, with consolidated operating earnings crossing
  zero around FY2027-FY2028 on the company's own core guidance plus the filed SG&A stickiness. **A
  real possibility.** It is a balance-sheet case, and Q2 is a business gate: **[E5-42]** puts the
  price question after the business question, and the business question answered first.
- **No band armed in `tools/alerts.json`, no `PORTFOLIO.md` row** - the QLYS ruling of 2026-09-07.
  A name that failed on the business gets its reversal condition in words, and it is at Q6 of the
  run file: the unit count rising for four consecutive quarters, **and** the competitor row ceasing
  to be unanimous, **and** a filed 10-K that contradicts the two no-moat sentences in the FY2025 one.

### TOOLING AND PROCESS

1. **`cap_flag` compares dates that are not comparable** - above. Recorded, not fixed.
2. **`level_shift*`'s "STEP DOWN" caption mis-describes a monotone slide** - above. Recorded, not
   fixed.
3. **A PROCESS DEFECT I HIT AND CORRECTED INSIDE THE FOLD.** Writing the register entry with a
   Python `str.replace("## COMPLETED FROM THE QUEUE", ..., 1)` inserted it **at line 230**, inside a
   dated note whose text merely *mentions* the heading, not at the register on line 502. The resume
   state of 2026-09-12 already warned about this for **reading** (*"Slice from the heading line
   itself"*); **it is equally a trap for writing, and worse, because a read returns a wrong count
   while a write corrupts the file.** Caught by verifying the entry count immediately after the
   write - it came back 155, not 156, and the first entry was still CRC. Reverted with `git
   checkout` and redone with a **line-exact match** (`l == "## COMPLETED FROM THE QUEUE"`, asserted
   unique). **The lesson is the fold's own: verify the step by reading the file back, not by
   trusting that the tool did what you asked.**
4. **`tools/run.py` and `tools/sources.py` produced no wrong number.** The FY2025 OCF, SBC, D&A and
   capex it reported match the filed cash-flow statement to the dollar, and the sovereign came from
   the Treasury directly.
5. **`CLAUDE.md`'s key-files table still says `principle_ledger.csv` is 267 rows. The file counts
   311 data rows and 311 distinct ids.** The same stale pointer the SGC, JAKK and CRC cycles
   recorded. Not edited by this run; the count used in this file is the counted one.
6. **Every ledger id cited in the USNA run file was verified present in `principle_ledger.csv`
   before the file was committed**, and `python tools/check_framework.py` returned **PASS** before
   the fold commit.
7. **Em dashes normalised to hyphens** outside quoted spans; the one survivor is the
   `COMPUTATION - NOT A CLEARANCE` heading, kept in operator rule 3's literal form.
"""
P="Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
s=io.open(P,encoding="utf-8").read()
assert "USNA" not in s
narr=narr.replace("COMPUTATION - NOT A CLEARANCE","COMPUTATION — NOT A CLEARANCE")
io.open(P,"a",encoding="utf-8").write(narr)
print("narrative appended")

# the process note into the queue's FOLD section
Q="Screens/WATCHLIST RUN QUEUE.md"
q=io.open(Q,encoding="utf-8").read()
marker = "**Why this is written down rather than remembered:**"
note = """*Dated note, 2026-09-21, added by the USNA fold beside step 1 rather than rewriting it (operator
rule 6):* ***WRITE THE REGISTER ENTRY BY LINE, NOT BY STRING.*** *A `str.replace("## COMPLETED FROM
THE QUEUE", ..., 1)` inserts at **line 230**, inside a dated note that merely mentions the heading,
not at the register on line 502. The resume state of 2026-09-12 warned about this trap for READING
("Slice from the heading line itself"); it is worse for WRITING, because a bad read returns a wrong
count while a bad write corrupts the file. Match the heading **line-exactly and assert it is
unique**, then verify by counting the entries back. The USNA fold hit it, caught it on the
verification read (count came back 155 with CRC still first), and reverted with `git checkout`
before committing.*

**Why this is written down rather than remembered:**"""
assert q.count(marker)==1
q=q.replace(marker,note,1)
io.open(Q,"w",encoding="utf-8").write(q)
print("process note added")
