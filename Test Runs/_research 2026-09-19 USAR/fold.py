# -*- coding: utf-8 -*-
"""USAR fold: queue register + roster strike + narrative fold + overnight log, one read-modify-write."""
import os, io
os.chdir(r"C:\Users\chreh\OneDrive\Documents\BRK")

QUEUE = "Screens/WATCHLIST RUN QUEUE.md"
LIST = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
LOG = "Screens/_daily/OVERNIGHT LOG.md"

def register_count(s):
    h = s.rindex("\n## COMPLETED FROM THE QUEUE")
    w = s.index("\n## THE WRITE-EARLY PROTOCOL")
    return len([l for l in s[h:w].split("\n") if l.startswith("- **")])

q = open(QUEUE, encoding="utf-8").read()
before = register_count(q)
print("register entries BEFORE:", before)
assert "USAR (USA Rare Earth" not in q, "USAR already registered - no duplicate allowed"

ENTRY = """- **USAR (USA Rare Earth, Inc.), 2026-09-19 - FAIL at Q1 (UNKNOWABLE, closed without prejudice: the future cash flows of the two legs that carry the
  quote cannot be estimated from any document that exists).** **WAVE 6**, one of the five ordinary businesses the 2026-09-01 triage dropped with no reason
  recorded; read as unlabelled, and the label's absence did not predict the gate. **The third Q1 UNKNOWABLE after HHH (2026-09-02) and RGTI (2026-09-13), and
  the fourth counting BIRD (2026-09-19).** **CIK 0001970622** found and confirmed by `tools/sources.py:cik_for('USAR')` and by the submissions
  `formerNames` row. **THE PERIMETER, AND THE CIK DOES HOLD A PREDECESSOR'S FIGURES:** the registrant was **Inflection Point Acquisition Corp. II**, a Cayman
  SPAC incorporated 2023-03-06, until 2025-03-11; it domesticated into Delaware 2025-03-12, the business combination with **USA Rare Earth, LLC** closed
  2025-03-13, and trading began 2025-03-14. **Two 10-Ks on this CIK are the shell's** (FY2023 `0001213900-24-029041`, FY2024 `0001213900-25-026445`) **and
  nine of the eleven 10-Qs**; companyfacts therefore carries **two values for FY2024 operating cash, the shell's -$1,398,564 and USA Rare Earth LLC's recast
  -$12,991,000** - the SOUN vintage defect of 2026-09-19 in a second registrant, and a screen reading the earliest vintage understates the burn ninefold.
  **The operating company has exactly TWO recast annual periods on file**, so the corpus's five-year window [E2-42] cannot be run at all. **Q1 UNKNOWABLE on
  the separating test, applied leg by leg and aloud:** (a) **Round Top** - *"We do not have declared mineral resources as defined under Item 1300 of
  Regulation S-K"*, an *"exploration stage property ... that has no mineral reserves disclosed"*, the 2019 PEA **withdrawn from reliance by the filer**, the
  Pre-Feasibility Study unfinished and the Definitive Feasibility Study scheduled for **Q1 2027 publication**: no document exists to fetch; (b) **the
  Stillwater magnet plant** - Phase 1a commissioned in Q1 2026, the FY2025 10-K promised customer orders in Q2 2026, and the supplemental risk factors filed
  **2026-09-15, four days before this run,** still say *"we do not currently have any revenue or definitive off-take or sales agreements with customers in
  place in our magnet business"*: a contract that has not been signed cannot be retrieved; (c) **Less Common Metals**, the only leg that sells anything
  (acquired 2025-11-18), ran a **gross LOSS of $1,583k on $5,821k of Q2 2026 revenue**, with Customer 1 at 73% and Customer 2 at 18% of FY2025 revenue and
  one vendor at 81% of raw-material purchases; (d) **Serra Verde**, closed **2026-09-03** for **$300,000,000 cash and 126,849,307 shares**, sold **$588
  thousand of product in the six months to 2026-06-30 against $5,312 thousand of cost of revenue** and **$2,486k against $36,105k in FY2025** (8-K
  `0001213900-26-097399` Ex. 99.3, the filed pro forma), and **USAR's own purchase accounting keeps it a development-stage property**: *"the mine will
  continue to be designated as a development stage property ... commercial operations are expected to commence in 2027."* The [E3-47] counter-test was run in
  writing (is this laziness? is a researchable leg being ignored? would five months help under [E4-46]?) and UNKNOWABLE survived it: the determining facts are
  **scheduled, not studied**. **Q2 OUT, recorded not governing** - the commodity end of **[E2-58]** rescued by the administered pricing of **[E2-59]**, and
  the row is that 1982 paragraph filed in 2026. **Nine peers named from USAR's own Competition section, three cells filled:** MP Materials FY2025 revenue
  **$224.4M, down 57.5% from $527.5M in FY2022**, gross margin 14.1% before $89.3M of DD&A, **cash from operations MINUS $155.8M** (10-K
  `0001801368-26-000008`); Energy Fuels revenue $65.9M, margin 20.9%, **operating cash MINUS $89.5M**; **Lynas FY2026 to 2026-06-30 revenue A$977.9M, margin
  40.1%, NPAT A$222.4M** - read at the **ASX rung** of the evidence ladder (announcement of 2026-08-26) because Lynas is not an SEC registrant, **in A$ as the
  filer reports and not converted**, with its operating-cash cell **left empty rather than guessed**. **The Chinese producers' cell is UNKNOWABLE, not
  UNRESEARCHED** - no document on this project's shelf reports them - and the limit is stated with what the peers' own filings say: China at *"90% of global
  REE processing and approximately 99% of global HREE processing"*, and MP's *"The Chinese Central Government regulates production via quotas and
  environmental standards."* **The decisive finding is the floor price, and it is the same number at three companies: US$110/kg NdPr** - Lynas/JARE to 2038
  with upside sharing above US$150/kg **capped at US$10m a year**; MP Materials/Department of War, *"a price floor of $110 per kilogram"* with **30% of the
  upside above it remitted to the DoW** and a **guaranteed $140 million of EBITDA** at the 10X Facility; USAR/Serra Verde via **US SIIE, LLC**, a special
  purpose vehicle into which **the U.S. government has put $750 million**, take-or-pay on 100% of Phase I production of the four magnetic elements with
  *"floor price protection, annual price escalation, favorable upside-sharing mechanics."* Lynas's own announcement supplies the mechanism: *"The average
  China domestic price of NdPr (VAT excluded) increased from US$55.0/kg in June 2025 to US$100.8/kg in June 2026. **This was influenced by floor price
  agreements led by global governments**"* - and its NPAT went A$8.0M to A$222.4M on that move. **[E3-62]'s second step is answered in the contracts: the
  upside above the floor is remitted to the state.** Class NONE, with PROVISIONAL recorded because five cells are empty and the run states why they cannot
  rescue a moat (two private Western magnet makers, a Canadian one, an Australian metal maker being bought by a peer, and the subsidised Chinese majority -
  every missing cell points adversely). **[E4-36]** places the record in the fourth cause, **wave-riding**. **Q3 IN, recorded not governing** - declared a
  **BINARY GATE** (daily execution ticked on **three chief executives in twenty-two months**: Ballard from 2024-12-16, Humpton from 2025-10-01, Moraitis from
  2026-10-01; leverage ticked and quantified; control not ticked). **No disqualifier found** and the clean half is recorded as plainly as the flags: clean BDO
  USA, P.C. (formerly HORNE LLP, PCAOB 243) opinion with no going-concern paragraph, ICFR concluded effective (no auditor attestation, an EGC limit, stated),
  no restatement, no material weakness, no SEC matter found, **and two auditor changes in seven months that both read STRUCTURAL, not adversarial** - UHY LLP
  exiting after the de-SPAC, and Horne LLP resigning because *"the partners and professional staff of Horne LLP ... joined BDO USA, P.C."*, both with clean
  Exhibit 16.1 letters and no disagreements. Weak accounting, unintelligible footnotes and the [E4-30] tells **did not fire**, and the run says so.
  **Five flags fired and converge [E4-52]:** [E5-15] serial issuance - **60,091,000 shares at 2024-12-31 to 371,569,406 pro forma at 2026-09-03, 6.2x in
  twenty-one months**, through a de-SPAC, $303.8M of warrant exercises, a $75M PIPE, **a $1.5 billion placement of 69.77M shares on 2026-01-28**, 16,132,790
  shares plus a 17,600,584-share warrant to the Department of Commerce, and 126,849,307 to Serra Verde's owners; [E4-22]'s third flag with [E3-48]'s action -
  the 10-K's own risk factors admit *"We have set certain targets for revenues; earnings before interest, taxes, depreciation and amortization ('EBITDA');
  free cash flows; capacity; and production"*, and the one target with a filed date (customer orders in Q2 2026) **was not met**; [E4-29] fires **weakly and
  the run says which way** - the Q2 2026 earnings release presents **no** Adjusted EBITDA and does **not** add back stock pay, so what fires is the narrative
  (*"accelerate the Company's EBITDA and cash-flow generation"*) against a balance sheet carrying **$3.25bn of development-stage plant**, which is [E5-41]'s
  reverse float deleted; **[E4-27] on what pay vests on - and it is time, not output: $22,042,408 of stock awards to four named executives in FY2025 against
  total revenue of $1,643,000, 13.4x**, the CEO's $4M, $5M and $1M RSU grants vesting *"in one-third (1/3) increments on the first three anniversaries"*, and
  the Chief Legal Officer paid *"$100,000 and $100,000 ... related to the successful signing of the business combination in 2024 and successful completion of
  the de-spac in 2025"* - paid for doing the deal, not for the deal working ([E2-49]: a calendar is not a bullseye); and **promotional disclosure against
  filed fact in the SAME accession on the SAME day** - Exhibit 99.1 of 2026-09-04 calls Serra Verde *"the only scaled producer of all four magnetic ... rare
  earth elements outside Asia"* whose operation *"began production in January 2024"*, while Exhibit 99.3 calls the mine a development-stage property with
  commercial operations expected in 2027 and shows $588k of six-month revenue: **the reader who stops at the press release is misled by a document that is
  accurate**, which is [E2-26]'s half-owner test failing on placement rather than on truth. Three of four [E2-30] behaviours score, the sharpest being (2):
  **$1.5bn raised 2026-01-28, Carester agreed 2026-04-09 and Serra Verde 2026-04-19**, eleven and twelve weeks later. **[E5-44]** run on the stock deal:
  126,849,307 shares valued at **$17.85** (the 2026-09-02 close) in the filed purchase-price allocation, **$15.37 sixteen days later**. **Q4 OUT, recorded
  not governing.** Owner earnings **negative on every window at both ends of the capex band: minus $15.1M (FY2024, D&A end) to minus $264.0M (TTM, capex
  end)**, two-year mean minus $37.2M to minus $56.5M - the FLNC case, not the BE case, because the sign never changes. **The D&A end is declared INVALID
  [E5-20]** ($1.6M of D&A against $37.4M of capex in FY2025; $5.8M against $139.5M TTM) and (c) is judged at total capex **and above**, because the filer
  states *"our estimated **$4.1 billion of required long-term capital expenditures**."* **SBC-over-operating-cash is REFUSED IN WORDS** as the RGTI run did -
  operating cash is negative in every filed period, so the calibrated row (ACVA 330.5%, ROKU 140.2%, CALX 98.4%, ARM 96.6%, CRWD 68.0%) cannot take this
  name; the honest denominators are **SBC at 533.2% of FY2025 revenue and 95.5% of H1 2026 revenue**, with cumulative SBC exceeding cumulative revenue by
  63%. **[E5-11]: strength 2 PASSES** (pro forma cash **$1,392.0M**, $3.75 a share) **and strength 3 FAILS, which is the one that kills** - $4.1bn of stated
  capex (about 2.9x the cash), a contractual obligation to *"raise at least $600 million of additional equity by December 31, 2027"* and to establish a
  *"$250 million revolving credit facility by December 31, 2026"* **as milestones for the government money itself**, a **$26.0M upfront commitment fee plus a
  2.0% annual ticking fee on the undrawn $1.30bn**, and the assumed **DFC loan repayable in up to 49 sculpted quarterly instalments** secured by a first lien
  on the Brazilian business. **Burn $183.7M in H1 2026** ($75.3M operating + $108.4M capital), **runway about 3.8 years** at that rate and less at the planned
  one. [E2-54]'s coverage test cannot be met from operations at all. **Shape #8 THE EQUITY IS THE REVENUE** (fourth instance after RIVN, LCID and SOUN, and
  the most extreme by ratio: TTM revenue $13.2M against $245.5M of operating and capital outflows), **with #14 THE PATRON as a feature and one PROPOSED
  ADDITION to #14 rather than a new shape: THE PATRON WHO FLOORS THE PRICE ALSO CAPS IT, AND CHARGES AN ENTRY FEE IN EQUITY** - **$882.3 million of stock and
  warrants paid as a condition precedent for $277.0M of funding not yet received, and the terms say the government keeps it** *"whether or not the Expected
  U.S. Government Transaction is funded in full or at all ... or if the funding is received but subsequently clawed back"*; features #2, #3 and #1 also
  present. **Q5 DID NOT OPEN**; the price is reported under `COMPUTATION - NOT A CLEARANCE` with what the buyer is paying for in words: yields **-0.65% to
  -4.62%** against a 5.34% sovereign, so about **6 to 10 points BELOW the bond**; the ~10% floor [E4-28] would need about **$571M a year of owner earnings**,
  or roughly **$57,000 per tonne** on the 10,000 tpa magnet target; and per pro forma share **$3.75 is cash (24.4%), $2.46 is deferred arrangement costs
  (the equity already given to the Department of Commerce), $2.46 is goodwill and intangibles** (including $246.7M for an offtake under which *"delivery ...
  has not started"*) **and $8.85 is plant that does not yet produce**. **Nothing armed and no PORTFOLIO row** - the QLYS ruling of 2026-09-07: a file that
  closed on the business gets a reversal condition in words. **THE REVERSAL CONDITION IS THREE DOCUMENTS, EACH DATED BY THE COMPANY ITSELF:** the Round Top
  Definitive Feasibility Study (*"on track for Q4 2026 completion and Q1 2027 publication"*), a definitive magnet offtake or sales agreement with a price and
  a volume, and Serra Verde's reclassification from development-stage to operational (company estimate: 2027). The pre-committed thesis-breaking metric if it
  re-opens is **owner earnings PER SHARE, not owner earnings** - the count is the variable management controls. **The strongest single fact AGAINST the
  conclusion, stated at [E4-51] strength:** DFARS 225.7018 bars the Department of War from buying Chinese magnets **from 2027-01-01**, China has named USAR on
  an export control list (which is evidence the position matters), three governments have committed cash, a price floor and a take-or-pay, and the world NdPr
  price nearly doubled in twelve months - a holder would say the patron is not the risk but the thesis. **Register entry 122**, counted from this file's
  heading line to `## THE WRITE-EARLY PROTOCOL` inside the fold script itself (121 line-start entries before the insert, 122 after, exactly one added, no
  duplicate ticker, USAR not previously entered; the brief said the register had moved to 121 after GFF folded and the count confirmed it).
  `Test Runs/2026-09-19 Run - USAR USA Rare Earth.md` is the file; research under `Test Runs/_research 2026-09-19 USAR/`.
  **PRICE US$15.37** (2026-09-18 close, `tools/sources.py:price('USAR')`, **aggregator flagged, live quote only**) **x 371,569,406 shares** = **cap
  US$5,711M**. The share count is **244,720,099 from the 10-Q cover of 2026-08-04, accession `0001970622-26-000057`, PLUS 126,849,307 issued on 2026-09-03 as
  the Serra Verde merger consideration (8-K `0001213900-26-097399`)** - **the post-cover issuance moves the cap by 52%**, which is the RGTI precedent
  reproduced; a further issuance to Carester (EUR 11,666,700 of stock) and 3,823,328 shares to TMRC are contracted and not in the count, and a DOC warrant
  over 17,600,584 shares at $17.17 is out of the money. **companyfacts publishes no dei cover fact after 132,638,561 at 2025-10-31**, so a screen pricing this
  name off companyfacts today divides by a count **2.80x too small** - the HBB/SOUN "no share count from dei" layer on a name that was never in that list.
  **Sovereign 5.34% USD, 30-year, US Treasury daily par yield curve, 2026-09-18, struck fresh** (not FRED). **PASS/FAIL: FAIL at Q1 (UNKNOWABLE).**
  `python tools/check_framework.py` PASSES."""

import re as _re
# The anchor MUST be the LINE-START heading. The phrase "## COMPLETED FROM THE QUEUE" also
# appears inside register entries and, decisively, inside the FOLD instructions BELOW
# "## THE WRITE-EARLY PROTOCOL" - so a bare rindex() inserts OUTSIDE the slice the count
# measures, and the entry lands in the instructions. Caught by the count-before-and-after check.
_hits = [m.start() for m in _re.finditer(r"(?m)^## COMPLETED FROM THE QUEUE", q)]
assert len(_hits) == 1, "expected exactly one line-start heading, found %d" % len(_hits)
h = _hits[0]
insert_at = q.index(chr(10), h) + 1
q = q[:insert_at] + ENTRY + "\n" + q[insert_at:]

# step 2: strike the ticker in the WAVE 6 roster
old_row = "| USAR | USA Rare Earth, Inc. | ordinary | **RUN** - a recent listing; expect a short filed history, which is a finding to state, not a reason to skip |"
new_row = ("| ~~USAR~~ | USA Rare Earth, Inc. | ordinary | **RUN 2026-09-19 - struck. FAIL at Q1, UNKNOWABLE** (closed without prejudice): a de-SPAC with two "
           "recast annual periods, no declared mineral resource at Round Top under Item 1300, no definitive magnet customer agreement as of 2026-09-15, and a "
           "$2.83bn Brazilian acquisition that is still a development-stage property on its own books having sold $588k in six months. The short filed history "
           "WAS a finding and it was stated - and the gate it closed was Q1, not Q4. Price US$15.37, cap US$5,711M. See COMPLETED. |")
assert old_row in q, "WAVE 6 USAR row not found verbatim"
q = q.replace(old_row, new_row, 1)

after = register_count(q)
print("register entries AFTER:", after)
assert after == before + 1, "register count moved by %d, not 1" % (after - before)
assert before == 121, "expected 121 before the insert, found %d" % before

# step 3: the narrative fold
FOLD = """

## USAR (USA Rare Earth, Inc.) - run 2026-09-19 - Q1 UNKNOWABLE, the file closed without prejudice

`Test Runs/2026-09-19 Run - USAR USA Rare Earth.md`. **Q1 UNKNOWABLE; Q2 OUT, Q3 IN and Q4 OUT
all RECORDED, NOT GOVERNING; Q5 did not open and the price is reported under
`COMPUTATION - NOT A CLEARANCE`.** WAVE 6, one of the five ordinary businesses the 2026-09-01
triage dropped with no reason recorded. **Register entry 122**, counted inside the fold script
before and after the insert (121 -> 122, exactly one added, no duplicate). Price **US$15.37**
(2026-09-18 close, aggregator flagged) x **371,569,406** shares = **cap US$5,711M**; sovereign
**5.34% USD** (US Treasury 30Y par, 2026-09-18, struck fresh).

### WHAT THE SHARE BUYS, per pro forma share at $15.37

| | per share | share of the price |
|---|---|---|
| cash and equivalents, pro forma | **$3.75** | 24.4% |
| deferred arrangement costs - the stock and warrants already handed to the Department of Commerce | **$2.46** | 16.0% |
| goodwill and other intangibles, incl. $246.7M for an offtake under which *"delivery ... has not started"* | **$2.46** | 16.0% |
| property, plant, equipment and mineral interests, **almost all development-stage** | **$8.85** | 57.6% |
| other assets | $0.59 | 3.8% |
| less total liabilities and the 12% preferred | **$(5.42)** | (35.3)% |
| **= pro forma book value attributable to common** | **$12.69** | 82.6% |

A quarter of the price is cash; essentially all the rest is plant that does not yet produce,
goodwill on a mine that does not yet produce, and a receipt for equity given to a government.

### THE THREE FACTS THAT DECIDED Q1

1. **Round Top has no declared mineral resource, in the filer's own words** - *"We do not have
   declared mineral resources as defined under Item 1300 of Regulation S-K"*, an *"exploration
   stage property ... that has no mineral reserves disclosed"*, the 2019 PEA **withdrawn from
   reliance** and not to be updated, the Pre-Feasibility Study unfinished, the Definitive
   Feasibility Study scheduled for **Q1 2027 publication**, commercial production targeted
   **late 2028**. **No document exists to fetch.**
2. **The magnet business has no customer contract, as of four days before the run.** The
   supplemental risk factors of **2026-09-15**: *"we do not currently have any revenue or
   definitive off-take or sales agreements with customers in place in our magnet business."*
   The FY2025 10-K had said orders would begin in Q2 2026; Q2 2026 is filed and every dollar in
   it is Less Common Metals'. **A contract that has not been signed cannot be retrieved.**
3. **THE SINGLE SHARPEST NUMBER IN THE FILE, and it is in the filed pro forma of the closing
   8-K: Serra Verde sold $588 thousand of product in the six months to 2026-06-30 against
   $5,312 thousand of cost of revenue** - and $2,486k against $36,105k in FY2025. It was bought
   on 2026-09-03 for **$300,000,000 of cash and 126,849,307 shares** (consideration $2,573.9M in
   the purchase-price allocation), and **USAR's own accounting keeps it a development-stage
   property**: *"the mine will continue to be designated as a development stage property, and
   related development costs will continue to be capitalized until the milestones necessary to be
   considered operational are achieved ... commercial operations are expected to commence in
   2027."* The same accession's press release calls it *"the only scaled producer of all four
   magnetic ... rare earth elements outside Asia"* whose operation *"began production in January
   2024."* Both are filed; only one is the accounting.

### THE PRIOR THE BRIEF SET, AND HOW IT CAME OUT

The WAVE 6 roster said *"a recent listing; expect a short filed history, which is a finding to
state, not a reason to skip."* **The short history was real and it was stated** - the operating
company has **two** recast annual periods, so **the corpus's own five-year window [E2-42] cannot
be run at all**, and that is shape #3. **But the history was not what closed the file.** The
gate was Q1, not Q4: the obstacle is not that the past is short, it is that **the two legs that
carry a $5.7bn quote have no filed economics of any kind, past or contracted.** A run that had
read the roster's hint as "expect a thin Q4" would have built an owner-earnings band (it is
below, and it is negative everywhere) and missed that Q1 never opened.

### THE COMPETITOR ROW IS THE 1982 COMMODITY LETTER, FILED IN 2026

Nine peers named from USAR's own Competition section; three cells filled.

| company | window | revenue | gross margin | cash from operations |
|---|---|---|---|---|
| **USAR** | FY2025 | $1.6M | +11.9% | **-$49.0M** |
| **USAR pro forma with Serra Verde** | FY2025 | $4.1M | **-809.5%** | not presented |
| **MP Materials** | FY2025 | **$224.4M** (-57.5% from FY2022's $527.5M) | +14.1% before $89.3M of DD&A | **-$155.8M** |
| **Energy Fuels** | FY2025 | $65.9M | +20.9% | **-$89.5M** |
| **Lynas Rare Earths** | FY2026 to 30 Jun | **A$977.9M** | **+40.1%** | not in the released statement; NPAT **A$222.4M** |

- **The two producing US filers both consumed cash in FY2025**, in a year when NdPr nearly
  doubled. MP Materials is not a start-up excuse case: a mine running since 2018 and a magnet
  plant already selling to General Motors.
- **The one profitable peer says why**, in its own announcement: *"Lynas secured floor price
  agreements to supply both Japanese and U.S. industry"*, with *"sales with pricing not linked
  to the market index"*, and *"The average China domestic price of NdPr (VAT excluded) increased
  from US$55.0/kg in June 2025 to US$100.8/kg in June 2026. **This was influenced by floor price
  agreements led by global governments.**"* Its NPAT went **A$8.0M to A$222.4M**.
- **US$110/kg is the floor written by three separate governments, and the state takes a share
  of the upside**: Lynas/JARE to 2038, upside sharing above US$150/kg **capped at US$10m a
  year**; MP Materials/Department of War, *"a price floor of $110 per kilogram"* with **30% of
  the upside above $110/kg remitted to the DoW** and the DoW *"guarantee[ing] that the 10X
  Facility will generate at least $140 million of EBITDA"*; USAR/Serra Verde through **US SIIE,
  LLC**, a special purpose vehicle into which **the U.S. government has put $750 million**, plus
  a **$300M forward purchase** and a $500M bank facility that *"has not been documented, closed
  or funded."*
- **That is [E2-58] plus [E2-59] with the receipts**, and [E3-62]'s second step is answered in
  the contracts rather than left to inference: **the gains above the floor are remitted to the
  patron.** The moat is a line item in an appropriation, and the corpus names the ending.
- **Source rules stated, not skipped:** Lynas is not an SEC registrant, so the evidence ladder
  drops to the **exchange rung** (its own ASX announcement of 2026-08-26), read **in A$ and not
  converted**, with the operating-cash cell **left empty rather than guessed**. The Chinese
  producers' cell is **UNKNOWABLE, not UNRESEARCHED** - no document on this project's shelf
  reports them - and what the peers' filings say about them is used instead.

### Q3: THE ACCOUNTING CAME BACK CLEAN AND THE INCENTIVES DID NOT

Declared a **BINARY GATE** on daily execution (**three CEOs in twenty-two months**) and
leverage. **No disqualifier found.** The clean half is recorded as plainly as the flags: a clean
BDO opinion with no going-concern paragraph, ICFR concluded effective, no restatement, no
material weakness, legible footnotes that explain the deferred-arrangement-cost treatment and
why the government warrant is a liability - and **two auditor changes in seven months that both
read structural**: UHY LLP exiting after the de-SPAC, and Horne LLP resigning because *"the
partners and professional staff of Horne LLP ... joined BDO USA, P.C."* **The cockroach prompt
[E4-22] does not fire on that churn, and saying so is part of reading the flag honestly.**

Five flags did fire and they converge **[E4-52]** on one output, a high share price - which in
this business is not a scoreboard but working capital, because every asset was bought with
paper:
- **[E5-15]: 60,091,000 shares to 371,569,406 in twenty-one months, 6.2x**, including a
  **$1.5 billion placement of 69.77M shares on 2026-01-28**.
- **[E4-22]'s third flag, admitted in the 10-K's own risk factors**: *"We have set certain
  targets for revenues; earnings before interest, taxes, depreciation and amortization
  ('EBITDA'); free cash flows; capacity; and production."* [E3-48]'s action run on the one
  target with a filed date: customer orders promised for Q2 2026, not delivered.
- **[E4-29] fires weakly and the run says which way**: the Q2 2026 earnings release presents
  **no** Adjusted EBITDA and does **not** add back stock pay. What fires is the narrative, and
  [E5-41] is why it matters - EBITDA deletes depreciation, and the pro forma balance sheet
  carries **$3.25bn of plant almost all of it development-stage**.
- **[E4-27] on what pay vests on, and it is time: $22,042,408 of stock awards to four named
  executives in FY2025 against $1,643,000 of total revenue - 13.4x.** The CEO's $4M, $5M and
  $1M RSU grants vest *"in one-third (1/3) increments on the first three anniversaries of the
  grant date."* Not one tonne, magnet or dollar of cash appears in a disclosed vesting
  condition. And the Chief Legal Officer was paid *"$100,000 and $100,000 ... related to the
  successful signing of the business combination in 2024 and successful completion of the
  de-spac in 2025"* - **paid for doing the deal, not for the deal working.** [E2-49]: a calendar
  is not a bullseye.
- **Promotional disclosure against filed fact, in the same accession on the same day** (above).
  [E2-26]'s half-owner test fails on **placement**, not on truth, and that distinction is the
  finding.

**[E5-44]** run on the stock deal: 126,849,307 shares valued at **$17.85** (the 2026-09-02
close) in the filed allocation; **$15.37 sixteen days later.**

### THE DEATH: shape #8 THE EQUITY IS THE REVENUE, with #14 THE PATRON as a feature

Owner earnings are **negative on every window at both ends of the capex band, minus $15.1M to
minus $264.0M**; two-year mean minus $37.2M to minus $56.5M; TTM worse than either. **The FLNC
case, not the BE case** - there is no sign change and no positive end. **The D&A end is declared
INVALID [E5-20]** ($1.6M of D&A against $37.4M of capex; $5.8M against $139.5M TTM) and (c) is
judged at total capex and above, because the filer states **$4.1 billion of required long-term
capital expenditures**. **SBC-over-operating-cash is refused in words** as RGTI did (operating
cash negative in every period); the honest denominators are **533.2% of FY2025 revenue and 95.5%
of H1 2026 revenue**. [E5-11]: strength 2 passes on **$1,392.0M** of pro forma cash, **strength
3 fails** - $4.1bn of capex at about 2.9x the cash, a contractual obligation to raise **$600M
more equity by 2027-12-31** and a **$250M revolver by 2026-12-31** *as milestones for the
government money itself*, a **$26.0M commitment fee plus a 2% annual ticking fee on the undrawn
$1.30bn**, and a DFC loan in 49 sculpted quarterly instalments over a first lien. **Burn $183.7M
in H1 2026; runway about 3.8 years** at that rate.

The mechanism is **[E2-27] on a published schedule**: six governments funding non-Chinese chains
at once, every decision individually rational because a state is paying, collectively one
capacity build aimed at the same protected demand - **and the protection is a contract with a
term.** Strip the administered price out and the filed evidence is that nobody in this industry
earns cash. The faster mechanism is dilution, and it is not a possibility but a covenant: $600M
at $15.37 is another **39.0 million shares, 10.5% of the pro forma count**, and that is the
contractual minimum against a $4.1bn programme.

**PROPOSED ADDITION TO SHAPE #14 (not a new shape - the index warns against proliferation):
THE PATRON WHO FLOORS THE PRICE ALSO CAPS IT, AND CHARGES AN ENTRY FEE IN EQUITY.** Filed in
three companies at once (30% of the upside above $110/kg to the DoW; upside sharing capped at
US$10m a year at Lynas; *"favorable upside-sharing mechanics"* at USAR) - and at USAR
**$882.3 million of stock and warrants paid as a condition precedent for $277.0M of funding not
yet received**, which the government keeps *"whether or not the Expected U.S. Government
Transaction is funded in full or at all ... or if the funding is received but subsequently
clawed back."* **No existing shape carries that last clause.**

### THE PRICE, AND IT WOULD HAVE FAILED THERE TOO

Yields **-0.65% to -4.62%** against a 5.34% sovereign: **6 to 10 points below the bond**. The
~10% floor **[E4-28]** needs about **$571M a year of owner earnings**, which on the company's own
10,000 tpa magnet target is about **$57,000 per tonne** - against a peer that sold $224M of
product and consumed $156M of cash, and a peer whose record year made A$222.4M on 12,122 tonnes
with two governments underwriting the price.

### REVERSAL CONDITION IN WORDS (fold step 4; nothing armed, no PORTFOLIO row)

A Q1 UNKNOWABLE gets no price band - the QLYS ruling. **Three documents, each dated by the
company itself, would convert the verdict from UNKNOWABLE to researchable and oblige a fresh v4
run:** the Round Top **Definitive Feasibility Study** (*"on track for Q4 2026 completion and
Q1 2027 publication"*), a **definitive magnet offtake or sales agreement with a price and a
volume**, and **Serra Verde's reclassification from development-stage to operational** (company
estimate: 2027). The pre-committed thesis-breaking metric if it re-opens is **owner earnings
PER SHARE, not owner earnings**: the count is the variable management controls and has used six
times in twenty-one months.

### THE STRONGEST SINGLE FACT AGAINST THIS CONCLUSION, at [E4-51] strength

DFARS 225.7018 bars the Department of War from buying Chinese magnets **from 2027-01-01**; China
has placed USAR on an export control list, which is evidence the position matters; three
governments have committed cash, a floor price and a take-or-pay; Serra Verde is the only
non-Asian source of all four magnetic heavy rare earths and 100% of its Phase I output is sold
on take-or-pay; the company holds **$1.39bn of cash** and little net debt; and the world NdPr
price nearly doubled in twelve months. **A holder would say the patron is not the risk but the
thesis - that this is the one commodity where the West has decided the price will not be set by
the low-cost producer.** That case is coherent and it is why the name trades at $5.7bn.
**[E4-40]** is the framework's answer: *model exposure, not experience.* The favourable
experience is fifteen months old and was made by the same policy that can be withdrawn.

### TOOLING AND BRIEF DEFECTS FOUND (five)

1. **`CLAUDE.md` understates the ledger by 150 rows.** Its KEY FILES table says
   `principle_ledger.csv` holds *"117 verbatim rows"*; the file holds **267**. The session
   memory note says 261. Every id cited in this run was checked against the file itself, which
   is why the discrepancy was seen; a run that trusted the number would not have.
2. **companyfacts publishes no dei cover fact for USAR after 2025-10-31 (132,638,561)**, so a
   screen pricing this name off tagged data divides by a count **2.80x too small**. This is the
   HBB/SOUN "no share count from dei" layer arriving on a name that was **never in that list**,
   which means the list of affected names is not closed. The count here was read off the cover.
3. **The SOUN vintage defect reproduces on this CIK**: companyfacts carries **two** FY2024
   operating-cash values, the SPAC's **-$1,398,564** (10-K filed 2025-03-31) and the recast
   **-$12,991,000** (10-K filed 2026-03-30). Any screen reading the earliest vintage understates
   the burn ninefold. **Second registrant found with this in two days**; a general test of
   de-SPAC filers in the backtest panels still has not been run.
4. **The post-cover issuance moved the cap by 52%** - 244,720,099 on the cover of 2026-08-04
   against 371,569,406 after the 2026-09-03 closing. The RGTI precedent in the brief is what
   caught it; no tool does.
5. **Brief defect, and a small one:** the brief named *"the Chinese producers (not SEC filers:
   state the limit)"* and *"Lynas (Australian ... state the source rule)"*, which was right, but
   it did not name **Energy Fuels**, an SEC filer that USAR's own 10-K identifies as acquiring a
   named competitor, and which supplied the second negative-operating-cash cell in the row. The
   filer's own Competition section is the better peer list than any brief's.

### ONE THING TO KEEP

**A filed pro forma can refute a press release in the same accession, and the run should look
for it before trusting either.** The Serra Verde closing 8-K of 2026-09-04 contains Exhibit 99.1
calling the mine a scaled producer in production since January 2024, and Exhibit 99.3 calling it
a development-stage property with commercial operations expected in 2027 and showing $588
thousand of six-month revenue. **The accession is internally honest; the reader who stops at the
first exhibit is not informed.** The CGNX companion rule says pull the 8-K EX-99.1 before
scoring [E4-29]; this run adds: **pull EX-99.3 too, because the pro forma is where the
acquisition's real economics are, and it is the only place they appear before the next 10-Q.**
"""
lst = open(LIST, encoding="utf-8").read()
assert "## USAR (USA Rare Earth" not in lst, "narrative fold already present"
lst = lst.rstrip("\n") + "\n" + FOLD

LOGLINE = ("- 2026-09-19 15:44 EDT | USAR | **Q1 UNKNOWABLE**, closed without prejudice (Q2 OUT, Q3 IN, Q4 OUT and Q6 all RECORDED, NOT GOVERNING; Q5 did not "
  "open). CIK 0001970622 found by cik_for() and confirmed; **the CIK holds a predecessor's figures** - Inflection Point Acquisition Corp. II, a Cayman SPAC, "
  "two 10-Ks and nine 10-Qs, and companyfacts carries TWO FY2024 operating-cash values (the shell's -$1,398,564 and the recast -$12,991,000), the SOUN vintage "
  "defect in a second registrant. Only TWO recast annual periods exist, so the [E2-42] five-year window cannot be run. **Q1 turned on the separating test "
  "applied leg by leg**: Round Top has *no declared mineral resources under Item 1300*, the 2019 PEA withdrawn from reliance, PFS unfinished, DFS scheduled for "
  "Q1 2027; the Stillwater magnet plant still had *no definitive off-take or sales agreements with customers* on 2026-09-15, four days before the run; Less "
  "Common Metals, the only leg that sells, ran a GROSS LOSS of $1,583k on $5,821k in Q2 2026 with two customers at 91%; and **Serra Verde, bought 2026-09-03 for "
  "$300M cash and 126,849,307 shares, sold $588 THOUSAND in six months against $5,312k of cost and remains a DEVELOPMENT-STAGE PROPERTY on USAR's own purchase "
  "accounting (commercial operations expected 2027)** - the same 8-K's press release calls it a scaled producer in production since January 2024. [E3-47] "
  "counter-test run in writing and UNKNOWABLE survived it. Q2: nine peers named from USAR's own Competition section, three cells filled - MP Materials revenue "
  "$224.4M (-57.5% from FY2022) with operating cash MINUS $155.8M, Energy Fuels $65.9M with MINUS $89.5M, Lynas FY2026 A$977.9M/NPAT A$222.4M read at the ASX "
  "rung in A$ unconverted with its OCF cell left empty rather than guessed; China's cell UNKNOWABLE not UNRESEARCHED. **US$110/kg is the floor written by three "
  "separate governments** (Lynas/JARE capped upside above US$150/kg; MP/DoW with 30% of the upside remitted and a guaranteed $140M of EBITDA; USAR/Serra Verde "
  "via US SIIE LLC, $750M of US government money) and Lynas's own words give the mechanism: NdPr US$55.0/kg to US$100.8/kg in twelve months, *influenced by "
  "floor price agreements led by global governments* - [E2-58] plus [E2-59], with [E3-62]'s second step answered in the contracts. Q3 IN, no disqualifier: clean "
  "BDO opinion, ICFR effective, no restatement, and **two auditor changes in seven months that both read STRUCTURAL** (UHY post-de-SPAC; Horne's partners joining "
  "BDO) - the cockroach prompt does not fire and the run says so. Five flags converge [E4-52]: 60,091,000 to 371,569,406 shares in 21 months; the 10-K's own risk "
  "factors admit revenue/EBITDA/FCF/capacity/production targets and the one dated target was missed; [E4-29] fires weakly (no Adjusted EBITDA in the release, "
  "stock pay not added back) and the run says which way; **[E4-27] $22,042,408 of stock awards to four executives against $1,643,000 of revenue, 13.4x, vesting "
  "on anniversaries, plus $100,000 each for signing and for completing the de-SPAC**; and promotional disclosure against filed fact in the same accession. Q4: "
  "owner earnings negative on every window and both (c) ends, -$15.1M to -$264.0M, the FLNC case; D&A end declared INVALID; **SBC-over-operating-cash REFUSED IN "
  "WORDS** (operating cash negative) with SBC at 533.2% of FY2025 revenue instead; strength 2 passes on $1,392.0M pro forma cash, strength 3 fails on $4.1bn of "
  "stated capex, a covenant to raise $600M more equity by 2027-12-31 and a $250M revolver by 2026-12-31, a $26.0M fee plus a 2% ticking fee; burn $183.7M a "
  "half-year, runway ~3.8 years. Shape #8 THE EQUITY IS THE REVENUE with #14 THE PATRON as a feature, plus a **proposed ADDITION to #14 rather than a new shape: "
  "the patron who floors the price also caps it and charges an entry fee in equity** - $882.3M of stock and warrants paid for $277.0M not yet received and kept "
  "by the government whatever happens. Below-gate computation: yields -0.65% to -4.62%, 6-10 points BELOW the bond; the floor would need ~$571M a year, ~$57,000 "
  "a tonne. Nothing armed, no PORTFOLIO row (QLYS ruling); **reversal condition is three DOCUMENTS the company itself has dated** - the Round Top DFS (Q1 2027), "
  "a definitive magnet sales agreement, and Serra Verde reclassified to operational (2027). Register entry 122, counted 121 before and 122 after inside the fold "
  "script, exactly one added, no duplicate. Five defects, the first being that **CLAUDE.md says the ledger holds 117 rows and it holds 267** | US$15.37 "
  "(2026-09-18 close, tools/sources.py, aggregator flagged) x 371,569,406 shares (244,720,099 from the 10-Q cover of 2026-08-04, accession 0001970622-26-000057, "
  "PLUS 126,849,307 issued 2026-09-03 per 8-K 0001213900-26-097399 - the post-cover issuance moves the cap 52%; companyfacts has no dei cover after 2025-10-31 "
  "and would divide by a count 2.80x too small) = cap US$5,711M; sovereign 5.34% USD (US Treasury 30Y par, 09/18/2026, struck fresh, not FRED) | **FAIL at Q1 "
  "(UNKNOWABLE)**; check_framework PASS | see fold commit. Concurrent BLK, CB and ERIC files left untouched")

log = open(LOG, encoding="utf-8").read()
assert "| USAR |" not in log, "overnight log already has a USAR line"
log = log.rstrip("\n") + "\n" + LOGLINE + "\n"

open(QUEUE, "w", encoding="utf-8").write(q)
open(LIST, "w", encoding="utf-8").write(lst)
open(LOG, "w", encoding="utf-8").write(log)
print("WROTE queue, reading list, overnight log")
print("final register count:", register_count(open(QUEUE, encoding="utf-8").read()))
