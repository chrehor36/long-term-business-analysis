# Company Run: Harmony Biosciences Holdings, Inc. (NASDAQ: HRMY), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-06 HRMY/` (raw filings as text,
`fetch.py`, `value.py`, the `tools/run.py` and `Screens/cover_shares.py` output). This file was copied from the template
before any fetch. *(The template's title line and the protocol's computation heading carry em dashes; this file writes
them with a colon and a hyphen under the operator's standing no-em-dash rule. The wording is otherwise the protocol's.)*

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this session by the blind rule
of the brief; whether the operator holds HRMY is unknown to the analyst.

**CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`, the run queue, the
prepped reading list, any other HRMY file (a listing of `Test Runs/` for "HRMY" or "Harmony" found none), other companies'
2026-10-05 and 2026-10-06 run or research files, and the unadopted gaps case. Seen without opening: the session's git
status and recent commit subjects, which name the KTB (TOO HARD (NATURE) at Q2, with its prices), SBH (OUT at Q2) and AMN
(OUT at Q2) runs of record and the untracked file names of the POOL and GPOR runs and several research folders; and the
auto-memory index line "57 gate-clearers, nothing buyable". None of these concerns HRMY or its industry; declared all the
same.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $39.92 (close 2026-10-05; aggregator quote as printed by `tools/run.py`, flagged per operator rule 5, live
  quote only).
- **Shares by class** from the latest filing's cover: 58,236,393 common, one class (10-Q for the period ended 2026-06-30,
  filed 2026-08-04, cover as of 2026-07-31, accession `0001104659-26-090090`; `python Screens/cover_shares.py HRMY`).
  Balance-sheet count 58,120,695 at 2026-06-30. Diluted weighted average Q2 2026: 58,755,359.
- **Market cap:** $2,324.8M (58.236M x $39.92).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 10/05/2026 (as
  printed by `tools/run.py` from `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-24, `0001104659-26-018859` (Business, Competition,
  Bioprojet agreements, Intellectual Property, MD&A, cash-flow statement, Note 13 ANDA litigation, Note 14 equity); 10-Q Q2
  2026, filed 2026-08-04, `0001104659-26-090090` (balance sheet, cash flows, Novitium and MSN licences, ANDA update);
  proxy DEF 14A filed 2026-04-03, `0001104659-26-039449` (directors, related-party transactions); 8-Ks
  `0001104659-26-090086` (Q2 2026 release), `0001104659-26-084095` (CFO departure July 2026), `0001104659-26-042886` (CFO
  change April 2026), `0001104659-26-038888` (COO from the board), `0001104659-25-092776` (ZYN002 Phase 3 failure),
  `0001558370-25-008415` (Lupin settlement), `0001558370-24-004945` (BP1.15205 sublicence), `0001558370-23-012348`
  (2023 term loan); earlier 10-Ks `0001558370-25-001441`, `0001558370-24-001466` (and its 10-K/A
  `0001558370-24-002037`, which only adds 10b5-1 plan disclosure), `0001558370-23-001574`, `0001558370-22-002257`,
  `0001564590-21-015274` for the cash-flow and patient series.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $348,199
  thousand on the face of the 10-K cash-flow statement (`0001104659-26-018859`), against 348.2 in `tools/run.py`. Agrees.
- `python tools/run.py HRMY` arithmetic lines only (its rule and id text ignored, Part VII): OCF 2023/2024/2025 =
  219.4 / 219.8 / 348.2; SBC 31.7 / 42.7 / 45.0; capex 0.3 / 1.2 / 0.3; D&A 24.4 / 24.1 / 23.8 ($M). The tool's owner
  earnings do **not** deduct the in-licensing and acquisition payments, which this filer books in investing activities
  (the IPR&D charge is added back inside operating cash flow); they are capital and are deducted below. The recast is in
  the record after the close.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**. For HRMY a five-year closure runs past the settled generic entry dates of WAKIX (2030), so the owner
would be holding through the event that decides the value; the question cannot be answered without knowing what replaces
WAKIX. Margin of safety: if it needs pencil and paper, "it’s too close to think about" **[M1996-084]**. The analyst's
habits: contrary evidence written down at once, "write it down in the first 30 minutes" **[M1997-127]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Every dollar of revenue is one drug, licensed, not owned: WAKIX is 100% of net product revenue, sold through three
   specialty pharmacies that took 100% of gross revenue (Caremark 38%, Accredo 36%, PANTHERx 26%), made by contract
   manufacturers, on a licence from Bioprojet that costs 13% to 24% tiered royalties plus 3% for the trademark (10-K
   `0001104659-26-018859`). Royalties were 23.3% of Q2 2026 revenue ($60.8M of $261.3M, 10-Q).
2. Generic entry is settled with five of seven ANDA filers for **March to July 2030 if WAKIX receives pediatric
   exclusivity**, "or earlier under certain circumstances"; the Lupin 8-K gives "no earlier than January 2030 (or July
   2030 with pediatric exclusivity)" (`0001558370-25-008415`). Pediatric exclusivity has not been granted; the trial meant
   to support it (TEMPO, PWS) reads out mid-2027 (10-Q). The seventh filer, AET, is unsettled: bench trial 17 to 19
   February 2026, oral argument 22 October 2026 (10-Q). The Orange Book patents expire September 2029 ('947) and March
   2030 ('197) (10-K Note 13).
3. A new class of drug for the same disease was approved after the last HRMY filing: FDA approved Takeda's ORZEYFUL
   (oveporexton), an oral orexin-2 agonist, for narcolepsy type 1 in adults on 5 August 2026, launch after DEA scheduling
   "expected within 90 days" (Takeda 6-K filed 2026-08-06, `0001395064-26-000329`). Takeda's 20-F
   (`0001395064-26-000177`) records both Phase 3 studies meeting "all primary and secondary endpoints". HRMY's Q2 2026
   release (4 August) predates it.
4. Pipeline failures on the record: pitolisant in idiopathic hypersomnia missed in Phase 3 and drew a refusal-to-file in
   February 2025; ZYN002 (bought with Zynerba in October 2023, $37.0M net cash plus a $15.0M milestone in 2025) failed its
   Phase 3 in Fragile X in September 2025 and is being phased out; the first pediatric cataplexy sNDA was not approved in
   June 2024 (approved on resubmission in February 2026) (10-K; 8-K `0001104659-25-092776`).
5. Two of the generic filers who settled were paid as licensors in the same weeks: Novitium (settled January 2026;
   licence January 2026, $15.0M upfront, up to $10.0M milestones, low single-digit royalties on "current and future
   pitolisant based products") and MSN (settled January 2026; licence February 2026, $17.0M upfront, $25.0M on patent
   grant). The Novitium royalty is the filer's own stated cause of the rise in cost of product sold from 19.0% to 24.2%
   of revenue (10-Q). AET and Sandoz answered HRMY's April 2026 suit on a Novitium-licensed patent with antitrust
   counterclaims against HRMY and Novitium (10-Q). Recorded as a fact pattern, not a finding.
6. A related-party payment: $15.0M upfront in June 2025 to CiRC Biosciences, "an entity controlled by Paragon"; the
   chairman of HRMY, Jeffrey Aronin, is chairman and chief executive of Paragon and sits on CiRC's board (proxy
   `0001104659-26-039449`).
7. Two chief financial officers left in three months: Sandip Kapadia stepped down 14 April 2026; his successor Glenn
   Reicin stepped down 16 July 2026 (8-Ks `0001104659-26-042886`, `0001104659-26-084095`); the controller is interim
   principal financial officer.
8. The case for the business, stated as strongly as the filings allow: average patients rose every year from about 2,500
   (end 2020) to 8,950 (Q2 2026); Q2 2026 revenue grew 30% year over year in the seventh year on market; WAKIX is the only
   approved narcolepsy treatment not scheduled by the DEA and is priced below the oxybates; the company holds $962.5M of
   cash and investments against $154.0M of term debt (10-Q); a gastro-resistant reformulation has a PDUFA date of 1 April
   2027 with formulation patents filed to October 2044 (Q2 release). Jazz's own record shows a reformulation can carry a
   franchise past generic entry (competitor row below).

## THE STANDING RULE
Owning HRMY puts the buyer at risk of ruin only through the buyer's own financing and sizing; bought without borrowed
money, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and at a size that cannot matter, it does
not touch "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. The
target's own debt is small against its cash (record below).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The test: "the first question is, can I understand it?" **[M1995-051]**, where understanding is "our definition of
understanding is thinking that we have a reasonable probability of being able to asses where the business will be in 10
years." **[M2000-037]**, a fix on "what the earning power and competitive position will look like in five or 10 years"
**[M2012-065]**.

**The key variables, and how predictable they are** ("If something is not very predictable, forget it." **[M1998-044]**):
1. *When WAKIX's exclusivity ends.* Partly knowable: five settlements put licensed entry at January to July 2030, earlier
   on "certain circumstances" the filer does not disclose, and the AET case is before the court with argument on 22
   October 2026. Whether the '947 and '197 patents hold against AET is a patent judgment, and on that the rows are
   explicit: "we bring nothing to the table when it comes to evaluating patents, manufacturing processes or geological
   prospects. So we simply don't get into judgments in those fields." **[L1999-019]**.
2. *What WAKIX earns after entry.* The precedent in the same market is on file: Jazz's Xyrem fell from $1,741.8M (2020) to
   $146.0M (2025) once high-sodium oxybate generics and authorised generics arrived in 2023, volumes down 57% in 2024 and
   33% in 2025 (Jazz 10-Ks `0001232524-23-000015`, `0001232524-26-000013`). Seven filers hold ANDAs for pitolisant. This
   variable is foreseeable: the stream largely ends within two years of entry.
3. *Whether the reformulations replace it before entry.* Pitolisant GR (bioequivalent to WAKIX, no titration, enteric
   coat; PDUFA 1 April 2027) and Pitolisant HD (Phase 3 readouts 2027, PDUFA 2028), with formulation patents still
   pending. The outcome depends on an FDA decision, on how many patients and payers switch in the 33 months between a GR
   launch and January 2030, and on whether pending patents issue and survive. Jazz's switch to Xywav worked (Xywav $1,657.0M
   in 2025), but Xywav carried a clinical difference the label states (92% less sodium) and its own orphan exclusivity in IH
   to 2028; whether GR's difference is enough is not a fact on file. Not predictable.
4. *What the orexin class does to the market.* ORZEYFUL was approved on 5 August 2026 for narcolepsy type 1, which is
   narcolepsy with cataplexy, the indication WAKIX added in 2020; orexin programmes are also named at Jazz/Sumitomo,
   Centessa, Alkermes (which bought Avadel in February 2026 partly for its orexin strategy, per Jazz's 10-K), Merck and
   Eisai. How much of WAKIX's 8,950 patients an orexin agonist takes, and whether HRMY's own BP-205 (Phase 1 single-dose
   data only) is competitive, is unknowable from any filing today. "one competitor is frequently enough to ruin a
   business." **[M2012-108]**.
5. *What management does with the WAKIX cash.* The filer is spending it on in-licensed and acquired candidates: $25.5M
   (BP1.15205), $33.1M (Epygenix), $37.0M (Zynerba), $15.0M (CiRC), $15.0M (Novitium), $17.0M (MSN), plus milestones,
   with up to $123.3M and $240.0M more due on BP-205 alone (10-K, 10-Q). The value of those bets is a forecast of
   clinical trials.

**The tests applied.**
- *Do the past statements tell me the future ones* **[M2008-033]**? No. Six years of rising WAKIX revenue describe a
  product inside its exclusivity; the statements of 2031 depend on variables 3 to 5, none of which appears in them.
- *Would the insiders write it down* **[M2000-105]**? The filer guides one year of revenue ($1.0B to $1.04B for 2026) and
  calls its own industry "highly competitive and subject to rapid and significant change" (10-K, Competition). Whether
  the insiders "would not want to put down on paper their predictions" **[M2000-105]** of HRMY's economics cannot be
  proved from outside; what can be said is that no filing puts the 2031 or 2036 economics on paper, and the drivers are
  trial, FDA and court outcomes.
- *Can I name the winner, not just the industry* **[M2012-067]**? Narcolepsy treatment is growing ($3.1B US net sales in
  2025 by the filer's figure), but which of histamine H3 agents, oxybates and orexin agonists, and which company's, will
  hold the patients in ten years is the question the rows say they cannot answer about drug companies: "than it is for me
  to figure out which one in the pharmaceutical." **[M1997-119]**; and of pipelines, "one drug company has a better drug
  pipeline than another" **[M2007-069]** is the guess the rows tell the investor not to make.
- *Does the business live on continued invention?* Yes, by its own plan: "Take pharmaceuticals, if they had never invented
  any more pharmaceuticals, it would be a terrible business." **[M1999-075]**. Without GR, HD, BP-205 or EPX-100 working,
  HRMY after 2030 is the case the row describes.
- *Is it important and knowable* **[M2006-076]**? The deciding variables (3 and 4) are important and not knowable: "If
  something’s important but unknowable, forget it." **[M2006-076]**.
- *Do I doubt it is inside?* "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**.

**Disconfirming rows, hunted and weighed.** The rows also record that the speakers misjudged pharmaceuticals the other
way: "if we could buy a group of leading pharmaceutical companies at a below-market multiple, I think we’d do it in a
second." **[M1999-043]**; and Munger: "the future of the pharmaceutical industry was easier to predict than the future of
the high-technology sector" **[M2001-002]**. Both are said of the industry bought as a group of leaders, the basket the
rows accept where companies cannot be told apart; neither is said of a single licensed product with a settled generic date.
And "They’re not a questionable patent." **[M2016-065]** warns that patents are rarely what decides; here the same row's
test, "What counts is whether you’re wrong about" **[M2016-065]** the basic economics, points at the same unknowns
(variables 3 and 4), so it does not reopen the file.

**Routing, and the cause.** HRMY's ten-year economics cannot be foreseen because they turn on clinical, regulatory, patent
and competing-invention outcomes. The framework sends that to TOO HARD at Q1, and the reason is ignorance, not a finding
against the business: "It doesn’t mean it isn’t a good buy." **[M2000-038]**; "We view change as more of a threat into the
investment process than an opportunity." **[M1999-063]**. The cause is **NATURE**: "in other cases the nature of the
industry would be the roadblock" **[L1993-023]**; more reading of filings does not tell the analyst how a court rules on
the AET patents, whether the FDA approves GR, or how many NT1 patients move to an orexin agonist, and on patents the rows
decline the judgment outright **[L1999-019]**. Study does not cure it: "if we can’t make a decision in five minutes, we
can’t make it in five months." **[M2008-086]**. A lower price does not reopen it **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE).** The file closes here. Filing facts: WAKIX 100% of revenue (10-K `0001104659-26-018859`);
  settled generic entry January to July 2030, earlier on undisclosed circumstances, AET unresolved (10-Q
  `0001104659-26-090090`); ORZEYFUL approved 5 August 2026 (`0001395064-26-000329`); IH and ZYN002 Phase 3 failures
  (10-K; `0001104659-25-092776`). *(An OUT reading was also open: the framework's Q1 list of what it rules out names, as OUT,
  the business that lives on continued invention, on the strength of the pharmaceuticals row quoted above. Both close the
  file; see the last section.)*

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED. (The competitor row gathered for it is in the record after the close, as evidence only.)

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion.
NOT REACHED. (The eight-year balance-sheet reading is in the record after the close, as evidence only.)

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED. (Contrary evidence items 5, 6 and 7 above would be read here.)

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting request is met below under COMPUTATION - NOT A CLEARANCE.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED. What the draft would have the buyer do: nothing; inaction is the default.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Item 5 above, settlements paired with licence payments to the settling generic filers and the antitrust
counterclaims, is the fact a Q12 or Q5 reading would start from.)

---
## THE BOX
**TOO HARD (NATURE), at Q1.** The deciding question, where HRMY's earning power will be in ten years, turns on whether a
reformulation and an early-stage pipeline replace a single licensed drug whose generic entry is settled for 2030, against a
new drug class approved for the same disease in August 2026; those are trial, court and FDA outcomes the industry's own
participants do not forecast. The computation below (pipeline at zero) puts the WAKIX stream plus net cash at about $20.63
to $37.93 a share against $39.92; it is not a range for the business, and it clears nothing. No research pass is opened
(NATURE).

---
## RECORD AFTER THE CLOSE: COMPUTATION - NOT A CLEARANCE
*Everything in this section was gathered for the owner's reporting request or as evidence for questions not reached. No
question is answered here, nothing in it carries entry language, and none of it reopens the box.*

### Owner cash after every real cost ($M; OCF less stock pay less capex less the licence, milestone and acquisition payments booked in investing)
| Year | OCF | SBC | capex | WAKIX licence milestones | pipeline licences, milestones, acquisitions | owner cash | without the WAKIX milestones |
|---|---|---|---|---|---|---|---|
| 2021 | 98.6 | 15.7 | 0.3 | 100.0 (cataplexy) | 0 | **-17.4** | 82.6 |
| 2022 | 144.5 | 26.2 | 0.2 | 40.0 (sales) | 0 (the $30.0M 2022 LCA fee was expensed inside OCF) | **78.1** | 118.1 |
| 2023 | 219.4 | 31.7 | 0.3 | 0 | 37.0 (Zynerba) | **150.4** | 150.4 |
| 2024 | 219.8 | 42.6 | 1.2 | 0 | 59.6 (Epygenix 33.1, BP1.15205 25.5, milestone 1.0) | **116.5** | 116.5 |
| 2025 | 348.2 | 44.9 | 0.3 | 0 | 34.3 (milestones 19.25, CiRC 15.0) | **268.7** | 268.7 |
| 5-yr mean | | | | | | **119.3** | 147.3 |

Sources: cash-flow statements in 10-Ks `0001104659-26-018859` (2023 to 2025), `0001558370-23-001574` (2020 to 2022),
`0001558370-22-002257`. H1 2026: OCF 120.2, SBC 20.0, licences 32.0 (Novitium 15.0, MSN 17.0), owner cash 68.2 (10-Q).
Depreciation-and-amortization variant (D&A in place of capex and the WAKIX milestones): mean 124.5. Notes: 2025 OCF carries
about $100M of favourable working capital (other liabilities +68.0, prepaid +31.8), partly reversed in H1 2026 (-23.3);
2025 cash taxes were $19.8M against a $56.4M charge. Stock pay ran 5.2% to 6.0% of revenue from 2022 to 2025, a real cost
by the rows' own account, "is the most egregious example" **[L2015-003]**.

### The value range (CONVENTION of this run, at the owner's request, confessed)
The framework's Q7 construction (five-year average carried ten years then flat) does not fit a stream with a settled end,
so, as the owner asked, the WAKIX stream is valued as declining after its generic entry, and the pipeline is valued at
zero (counted as worth what it costs, which is the TOO HARD part). Construction, `value.py` in the working folder:
- Valuation date 2026-10-06; Q4 2026 then 2027 to 2029 at full stream; generic entry January 2030 (no pediatric
  exclusivity granted); 2030 and 2031 at a residual share of the 2029 figure; nothing after. Cash at mid-period.
- **Low end:** the five-year mean owner cash, $119.3M, flat; residual 30% in 2030 and 10% in 2031.
- **High end:** the 2025 owner cash, $268.7M, grown 15% a year to 2029 (below the 29.9% revenue CAGR of 2021 to 2025 and the
  17% the 2026 guidance implies; the cap is ours, set because carrying the shown growth into an orexin launch is not a
  number the filing supports); residual 40% in 2030 and 15% in 2031 (Jazz's Xyrem kept 41% of its 2023 sales in 2024 and
  26% in 2025, with an authorised-generic royalty beside it).
- Discounted at the sovereign, 5.66%. Net cash added at face: cash 549.8 + short-term investments 118.0 + long-term
  investments 294.7 less term debt 154.0 (20.0 current, 134.0 long-term) = **$808.5M, $13.88 a share** (10-Q balance sheet).
  Net interest income stays in the owner-cash base as well, a double count of roughly $0.3 a share, confessed and left.
- **VALUE RANGE: $20.63 to $37.93 a share** (top over bottom 1.84) **against $39.92.** The price sits above the top of the
  WAKIX-plus-cash range; the market is paying about $26.04 a share ($1,516M) for everything beyond net cash, which the
  WAKIX stream alone fills at the high end only.
- **FAIR PRICE: about $28.80.** The central case (the mean of the two streams) clears the floor of about 10% pre-tax
  **[M2003-149]** (the framework's CONVENTION at Q7) at or below this price. Tax treatment: owner cash is after cash tax, so
  the floor is applied as 10% x (1 - 26.2%) = 7.38% after tax, 26.2% being the filer's 2025 effective rate (10-K). The floor
  is applied to the operating stream with net cash credited dollar for dollar, which is the floor on equity with cash at
  face, equivalently on equity less net cash (enterprise value). At $39.92 the central case returns about -17% a year after
  tax; only the high end gets above zero (about 1.7% after tax, 2.3% pre-tax).
- **CHEAP PRICE: about $13.63** (rule, ours: the price at which the low end, valued at the floor rate with net cash at face,
  is worth one and a half times the price; the rows ask that the margin "scream at you" **[M2009-005]**, and no row gives a
  ratio, so the 1.5 is a CONVENTION of this run). It sits just below net cash per share, which is the honest meaning: no
  pencil is needed only where the buyer pays nothing for WAKIX.

### Balance sheets, eight year-ends ($M; `tools/run.py` table from first-filed XBRL, read against the filed statements)
| Year-end | equity | cash | receivables | intangibles | term debt | retained earnings |
|---|---|---|---|---|---|---|
| 2018 | -243 | 84 | | | | |
| 2019 | -423 | 24 | 4 | 72 | 98 | -423 |
| 2020 | 97 | 229 | 22 | 162 | 194 | -488 |
| 2021 | 187 | 234 | 35 | 144 | 192 | -454 |
| 2022 | 403 | 244 | 55 | 161 | 192 | -272 |
| 2023 | 467 | 312 | 74 | 137 | 194 | -143 |
| 2024 | 659 | 453 | 83 | 113 | 179 | 2 |
| 2025 | 870 | 753 | 97 | 89 | 164 | 161 |
| 2026-06 | 999 | 550 (+413 investments) | 111 | 77 | 154 | 269 |

What the figures say **[M2025-032]**: a preferred-funded deficit turned by the 2020 IPO and five years of retained profit;
no goodwill; the one intangible is the capitalised WAKIX licence, amortising $23.8M a year and on course to reach about
zero near the 2029 to 2030 patent dates; receivables held at 11% to 14% of revenue over the span (no build-up against
sales); inventory negligible; debt refinanced twice (2021, with $22.0M of exit fees; 2023 JPMorgan term loan, SOFR plus
3.5% to 4.0%, secured on substantially all assets) and amortising; buybacks once, $100.0M in 2023, none since under a
remaining $150.0M authorisation; deferred tax asset $156.8M. What they do not say: the balance sheet carries no asset for
the reformulations or the pipeline, and nothing in it describes the business after 2030. Accrued expenses ($191.0M at
YE2025) include unpaid ANDA settlement amounts the filer does not quantify.

### Margins over the whole span (from the 10-K income statements)
Cost of product sold rose from 17.3% of revenue (2020) to 22.8% (2025) and 24.2% (Q2 2026), royalties driving it; operating
margin 28.7% (2021), 33.0% (2023), 24.0% (2025), 26.6% (H1 2026), with R&D rising from 10.0% to 21.8% of revenue as the
company buys and develops successors. Revenue per average patient about $111k (2025) and $117k annualised (Q2 2026).

### The competitor row (each from its own filings; evidence for Q2, which was not reached)
| Product, filer | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | source |
|---|---|---|---|---|---|---|---|
| WAKIX, HRMY | 159.7 | 305.4 | 437.9 | 582.0 | 714.7 | 868.5 | HRMY 10-Ks |
| Xyrem, JAZZ | 1,741.8 | 1,265.8 | 1,020.5 | 569.7 | 233.8 | 146.0 | `0001232524-23-000015`, `0001232524-26-000013` |
| Xywav, JAZZ | 15.3 | 535.3 | 958.4 | 1,273.0 | 1,473.2 | 1,657.0 | same |
| High-sodium oxybate AG royalty, JAZZ | | | | 75.9 | 217.6 | 211.7 | same |
| Lumryz, AVDL | | | | 28.0 | 169.1 | not filed (acquired by Alkermes Feb 2026) | `0001012477-25-000010` |
| Sunosi (Jazz to May 2022, then AXSM) | 28.3 | 57.9 | 28.8 (Jazz part-year) | | 90.3 | 120.1 | Jazz 10-K 2022; AXSM `0001193125-26-064267` |
| ORZEYFUL, Takeda (non-SEC detail via 6-K) | | | | | | approved 2026-08-05 for NT1 | `0001395064-26-000329` |

Read over the span: WAKIX grew in every year while the oxybates changed hands; the lesson of the row is Jazz's, that a
leading narcolepsy drug lost about 86% of its 2022 sales by 2025, the third year of generic and authorised-generic
competition (92% from its 2020 peak, part of it Jazz's own move of patients to Xywav), and that the company kept its
oxybate revenue (about $1,757M in 2020, about $2,015M in 2025 with the royalty) only by moving patients to a differentiated
successor before entry. WAKIX's US share of a $3.1B market is about 28% (filer's
market figure, 2025). Takeda, the largest attacker, now has an approved drug for the more severe half of the disease.

### What could not be got
The "certain circumstances" that accelerate the settled entry dates (the agreements are not filed in full); the MSN
settlement's terms (confidential); the amounts paid to settle ANDA cases; the AET ruling (argument 22 October 2026); the
DEA schedule and price of ORZEYFUL; the split of WAKIX patients between narcolepsy type 1 and type 2; any filed forecast of
GR conversion; the 2026 proxy's pay tables were not read (Q5 and Q6 not reached).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **not done**;
      the brief forbade commits, and the file was written in one pass after the reading. Declared.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script; no v4 id used); every filing fact has its
      accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance; the computation is headed as the protocol
      requires.
- [x] Owner cash after every real cost (stock pay and the licence and acquisition payments deducted), never a net-income
      proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**.
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its owner-earnings figure was recast because it omits the
      investing-section licence payments.
- [x] `python tools/check_framework.py` run before reporting (result in the reply; no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Pharmaceuticals sit in two boxes at Q1.** The framework's Q1 list of what it rules out names, as OUT, the business
that lives on continued invention, resting on the pharmaceuticals row (M1999-075); the paragraph below that list, and the
routing fixed on 2026-10-05, send a business whose ten-year economics cannot be foreseen to TOO HARD and never to OUT on
the business. A drug company is both. This run chose TOO HARD (NATURE), because the reason the rows give for leaving drugs
alone is the analyst's ignorance (rows L1999-019, M1997-119 and M2007-069, quoted at Q1) rather than a finding that the
business is bad, and recorded the OUT reading beside it. The framework should say which governs. (2) **No rule for a single product or a dated end to the stream.** The Q7 range
convention (five-year mean carried ten years, then flat) assumes a going concern; for a licensed drug with a settled generic
date it overstates the low end and has no place for the decline, so this run built its own declining-stream range at the
owner's request and confessed it. (3) **In-licensing payments and `tools/run.py`.** The tool's owner earnings omit licence,
milestone and acquisition payments that this filer books in investing activities (with the IPR&D charge added back inside
operating cash flow), which would overstate owner cash by $34M to $100M a year; Part VII tells a run to read only the
tool's arithmetic lines but does not warn that a line can be incomplete. (4) **The fair and cheap prices** asked by the
owner have no framework rule; the tax treatment of the ~10% pre-tax floor against after-tax owner cash, and whether net
cash sits inside or beside the floor, are not stated in Q7, and two analysts could differ by several dollars a share on
those choices alone.
