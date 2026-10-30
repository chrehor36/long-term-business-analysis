# -*- coding: utf-8 -*-
"""Fold step 3: append the CRTO narrative fold to the PREPPED READING LIST."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

p = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
s = open(p, encoding="utf-8").read()
if "CRTO (Criteo S.A.) — WAVE 7, name 16" in s:
    print("ALREADY PRESENT")
    sys.exit(0)

text = """

---

# CRTO (Criteo S.A.) — WAVE 7, name 16 — 2026-09-21 — **Q2 OUT, ON THE BUSINESS**
*Register entry 148. Run file: `Test Runs/2026-09-21 Run - CRTO Criteo.md`. Research:
`Test Runs/_research 2026-09-21 CRTO/`.*

**Q1 IN. Q2 OUT on `[E3-03]` criterion 2. Q3, Q4, Q5 and Q6 not opened.** Cap struck by hand at
**$818.3M**; sovereign **USD 5.34%, 2026-09-18, US Treasury 30-year**, chosen over the euro after
an argument from the filings rather than an assumption.

## What the run found

**1. The company hands you the competitor row in one sentence, and it is nine names long.** FY2025
10-K, Item 1: *"We currently compete with large, well-established companies, such as Amazon, Meta
Platforms, Google, and Microsoft, pure play DSPs, such as The Trade Desk, pure play SSPs such as
Magnite or PubMatic, and pure play retail SSPs such as Publicis' CitrusAd, that focus on monetizing
retailers' media, as well as smaller, privately held companies such as Kevel or Koddi."* The
sentence before it: *"Our market is complex, rapidly evolving, highly competitive, still fragmented
and yet rapidly consolidating."* **[E3-03] criterion 2 asks whether the customers think there is no
close substitute; the subject's own Item 1 lists nine.**

**2. The unit series is the honest one, and it has fallen four years running.** `[E4-55]`.
Number of clients, from each year's own "key metrics" table: 18,990 (2022), 18,197 (2023), 17,269
(2024), **16,786 (2025)**, while revenue was held level at $1,949.4M, $1,933.3M, $1,944.9M.
**The pre-2023 figures are NOT on this basis and the run refused to quote across the break**: the
FY2024 10-K footnotes *"In the first quarter of 2023, we streamlined our client count methodology
which is now based on unique billing accounts"*, so the headline-friendly 21,745 of 2021 to 16,786
of 2025 (-22.8%) is not a legitimate comparison and **-11.6% over three years on one basis** is.
A run that had smoothed the break would have doubled its own finding.

**3. Two customers removed a fifth of the segment that was supposed to be the franchise.** Q2 2026
EX-99.1: *"Retail Media Contribution ex-TAC decreased (21)% ... reflecting a $21 million headwind
from previously communicated scope changes with two specific Retail Media clients."* Two clients
out of roughly 16,800. **Retail Media was the growth story — 24% in 2024, 2% in 2025, -21% in Q2
2026.** Criteo does not own the retailer's on-site inventory; it runs the auction under a contract
the retailer can end, and CitrusAd, Kevel and Koddi are named in the same paragraph as the people
who would run it instead.

**4. THE CENTRAL FINDING, AND IT IS A `[E3-62]` FINDING: the margin improved because the input got
cheaper, not because the output got dearer.** Contribution ex-TAC went from 52.5% to 60.4% of
revenue over 2023-2025 and gross profit grew 34.2% on a top line that fell 13.7%. **That is the
disconfirming case, and it is strong.** It fails because the MD&A itself states the cause:
*"lower traffic acquisition costs in Performance Media, related primarily to the decrease of the
average CPM for inventory purchased."* `[E3-62]` asks who keeps the saving; `[E3-51]` names the
class — *"when a surfer gets up and catches the wave and just stays there, he can go a long, long
time. But if he gets off the wave, he becomes mired in shallows."* **The FY2026 guidance is getting
off the wave**: *"We now expect Contribution ex-TAC to decrease -12% to -10% at constant currency."*

**5. The `[E4-32]` inversion, recorded as a pattern worth carrying to other names.** Criteo grew
profit in each of the last three years **while the moat narrowed on four independent filed series**
— clients, revenue, segment contribution and forward guidance. `[E4-32]` warns that a widening moat
*"does not necessarily mean that the profit is more this year than last year"*. **The inverse is the
one a screen actually meets, and a yield screen cannot see it at all**: CRTO reached this queue on a
`growth_required` of 0.82%, the lowest band in wave 7, because the screen was looking at the three
best cash years the company ever filed.

## Priors refuted, priors confirmed

- **REFUTED: the take-rate collapse carried over from the PUBM run of 2026-09-19.** PubMatic's
  revenue per million impressions fell 66% over FY2021-25. **Criteo's take went UP**, 52.5% to
  60.4% of revenue in three years. The two positions in the chain are not the same trade and the
  PUBM finding does not generalise. The brief framed it as a prior to argue against, which is the
  right form, and the answer came back negative.
- **REFUTED: `cap_flag` as an error claim.** Settled on arithmetic as a pure **date mismatch**:
  $1,254M / $23.96 = 52.34M non-affiliate shares at 2025-06-30, against 48,997,559 shares at $16.70
  on 2026-09-18; the two movements (price -30.3%, count -6.7% on buybacks) reconcile the two
  figures to **0.4%**. Neither number was wrong and neither was discarded.
- **REFUTED: the `deal_note` as a ROKU-class spread warning.** **Both tracks are redomiciliations
  with no counterparty.** Track one, France to Luxembourg, **COMPLETED on 2026-07-29** on a Form
  **8-K12B** the dispatcher's brief never mentioned; track two, Luxembourg to Delaware, merges the
  company into **its own wholly owned subsidiary** at 12:00:01 a.m. on 2027-01-01, one share for
  one. LEG does not apply either: the security trades continuously under CRTO. **The quote is an
  owner-earnings price.**
- **REFUTED: `[E2-49]` metric withdrawal. It does not fire, and the opposite is true.** The same
  three key metrics — number of clients, Contribution ex-TAC, Adjusted EBITDA — appear in the
  FY2018, FY2021, FY2024 and FY2025 10-Ks; **the client count has fallen for four years and they
  have kept publishing it**; and when the definition changed in Q1 2023 they footnoted it and
  restated the prior year **downward**. **The standing prior moves to six fires and SIX failures**
  (was six and five). This is now the eleventh company it has been run on.
- **CONFIRMED, which is rarer: `level_shift "no step"` and `best_year_dep "no single-year
  dependence"` survive the longer window.** The `spread_caveat` said the four-construction width
  could not see past five years; twelve filed years of operating cash flow (2014-2025) were built
  and the twelve-year mean of $216.0M against the five-year $254.1M is a ratio of 1.18, with the
  best year at 1.22x the five-year mean. **Two screen verdicts rebuilt on a longer window and held.**
- **CONFIRMED: treasury shares sit outside the cover count at a European issuer**, as the brief
  predicted. 53,728,895 issued against 48,550,453 outstanding at 2026-06-30 — 5,178,442 in
  treasury — and the cover figure of 48,997,559 is already net of them.

## Tooling and source findings

- **`acq_note` is the SEVENTH consecutive acquisition-perimeter understatement, and it confirms
  the RESUME STATE section-5 SOURCE limit rather than revealing a new bug.** The screen reports
  $156M; that is the investing-cash line. The FY2021 10-K states IPONWEB was bought *"for $380
  million comprised of a mix of cash and treasury shares of the Company"*. Three legs are invisible
  to the flag: the **stock** (`BusinessCombinationConsiderationTransferred1` is ABSENT from CRTO's
  companyfacts, as it is for CRM, CERT, MRVL and AVGO), **$74.0M of contingent consideration paid
  through the FINANCING section** in 2023-2024, and **Lock-Up Shares expensed through share-based
  compensation** (*"LUS were issued to the Iponweb seller as partial consideration for the Iponweb
  Acquisition"*). **$380M is 46% of the hand-struck cap, not the 18% the screen reports.** No tool
  change is proposed; the hand read is the remedy the limit already names.
- **An empty `wc_note` is not a clean one, and CRTO is the sharpest case of it yet.** FY2025 carries
  **+$246.0M on trade receivables against -$265.4M on trade payables** — each about 80% of a year's
  operating cash flow, roughly 2.6x the flag's 30% trigger — and the six working-capital lines net
  to just **-$13.3M**, so nothing fired and nothing needed to. Receivables were $800.9M at
  2024-12-31, **41% of that year's revenue**. **The flag's docstring limit (annual facts only) is
  not what hid these; they are annual and they offset.** The reader still has to open the detail
  lines, because a net of -$13.3M and two gross swings of a quarter of a billion dollars each are
  the same number to the flag.
- **The sovereign question was genuinely undetermined and had to be decided in the run.** Reporting
  currency USD; **parent functional currency EUR** (*"The functional currency of the Company is the
  euro, while our reporting currency is the U.S. dollar"*, Item 7A); revenue 43.0% Americas
  (US alone 38.7%), 37.4% EMEA (Germany 10.7%, France 4.6%), 19.5% Asia-Pacific (Japan 11.4%).
  **Decided USD** on the largest single-currency block and on the fact that every figure in the
  owner-earnings construction is a USD figure. **The EUR alternative is stated (ECB SR_30Y 3.7502%
  at 2026-09-17) and the USD choice is 159bp harder on the buyer**, which is the direction a
  contestable currency call should be decided in. **A filer with a euro functional currency, a
  dollar reporting currency and no dominant revenue currency is a class, not a one-off**, and the
  next one should copy the argument rather than the answer.
- **The PUBM peer folder was used as the brief directed and its vintage was checked.** The five
  companyfacts files and two peer 10-K texts were fetched 2026-09-19 and were **copied** into this
  run's folder; PUBM's own companyfacts was fetched fresh. **Criteo's own figures were taken from
  Criteo's filings only.**

## Defects found in the dispatcher's brief

1. **The brief missed the 8-K12B of 2026-07-29** (accession `0001628280-26-050326`), which is where
   track one COMPLETED, where the ADS structure was terminated and the Deposit Agreement cancelled,
   where the listed instrument changed from an ADS to an ordinary share, and where Rule 12g-3
   succession is asserted. It listed six deal filings and described track one as ending at the
   February vote. **A run that trusted the list would have struck a cap on the wrong instrument.**
2. **The brief posed "what Criteo was BEFORE Luxembourg" as open research**; the answer is in the
   former-address box of that same missed filing (*"32 Rue Blanche , Paris , France 75009"*).
3. **The brief's quotation of the 2026-08-05 Item 1.01 is accurate** and is confirmed word for word,
   including the *"12:00:01 a.m., New York City time, on January 1, 2027"* Effective Time. Recorded
   because the brief asked to be checked and a confirmation is as much a finding as a correction.
4. **Both tracks were framed as candidates for a ROKU-class spread. Neither could be**, because
   there is no counterparty on either.
5. **`acq_note` understates the perimeter by three legs, not one** — see above.
6. **The brief passed through `CLAUDE.md`'s stale ledger count of 267.** The file is **311 rows**.
   **Not a new finding**: the MNRO fold of 2026-09-21 already records it as the thirteenth
   consecutive fold to do so, with `CLAUDE.md` deliberately unedited under PRIME RULE 5. **This
   fold makes it the fourteenth.**

## No price band, and the reversal condition in words

The QLYS ruling (2026-09-07) bars a price alert on a name that failed on the **business**, so
`tools/alerts.json` and `PORTFOLIO.md` are untouched. **The condition that would reopen this file:
the client count rising for two consecutive fiscal years on one methodology, AND Contribution
ex-TAC returning to growth without a fall in the average CPM of purchased inventory being the
stated cause, AND no single pair of Retail Media clients being able to move a reporting segment by
a fifth in one quarter.** The middle clause is the one that matters: a recovery driven again by
cheaper media would be the same wave, not a moat, and `[E4-17]`'s gradualism cuts both ways — one
quarter is not the start of anything.

## Acceptance test

`python tools/check_framework.py` and `python tools/ledger_verbatim.py` were run before the commit;
the result is recorded in the commit message. **Every ledger id cited in the CRTO run was resolved
against `principle_ledger.csv` before it was written** — 62 ids considered, **0 phantom**, and the
`[E4-55]` OCR artifacts (the doubled quotation marks and the corrupted `e?ect`) are reproduced in
the run file rather than smoothed, per PRIME RULE 1.
"""

open(p, "w", encoding="utf-8").write(s + text)
print("appended", len(text), "chars")
