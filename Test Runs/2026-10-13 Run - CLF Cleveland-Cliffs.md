# Company Run: Cleveland-Cliffs Inc. (NYSE: CLF), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Filled top to
bottom from the template `Test Runs/_TEMPLATE - Company Run.md`; every judgment cites a v5 ledger id in bold; every filing
fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Copied to this dated name before any fetch (commit bef1f0c9). Dispatched blind run, under the canonical brief
`Screens/_daily/_dispatch_brief.md` with one stated departure: the lines of evidence were derived by the analyst from the
2025 10-K's Items 1, 1A and 7 (listed in Step 0).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled at the fold by the dispatching session (overnight 2026-10-13, after the run was committed): not held (`PORTFOLIO.md` carries no line for CLF or Cleveland-Cliffs).

**Contamination, declared and not used.** (1) A `ls` of `Test Runs/` filtered to names beginning "2026-10-13" (run to
find whether today's file name was free) printed the file names of 27 other run files dated today (other companies:
ACHC, AMBBY, ASTE, BAC, CYH, EMAT, GRFXY, HDSN, HRIBF, HTCMY, HY, JCSE, KIGRY, KMTUY, LHSW, LONKF, LZ, MSM, MTW, SIEGY,
SITE, SQFT, TEX, THC, TPICQ, UHS, VELO). None names CLF or Cleveland-Cliffs; none was opened. (2) The session's opening
git status and recent-commit list showed research-folder names for AYI and ARCB, daily digest file names, and commit
subjects about UHS and THC runs (a box word for UHS was in a subject line). (3) The session's memory index carries one-line
summaries of the queue state and a count of gate-clearers. None of this bears on CLF; none of it was used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $12.86 (2026-10-13, printed by `tools/run.py` as "aggregator, live quote only"; flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 570,540,047 common shares, par $0.125, one class (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-23, accession `0000764065-26-000100`; `python Screens/cover_shares.py CLF`).
  Check: the 10-Q balance sheet shows 606,051,530 issued less 35,523,974 in treasury = 570,527,556 outstanding at
  2026-06-30, agreeing with the cover count. Filings after the 10-Q: an 8-K of 2026-07-24 (Item 5.02, officer change,
  `0000764065-26-000102`), Forms 4, a Form SD and a Schedule 13G; no 8-K, S-3 or prospectus issuing shares after
  2026-07-23 was found in the EDGAR submissions list. The 75,000,000 shares of the October 2025 offering (8-K of
  2025-10-31, `0000764065-25-000160`; 424B5 `0000764065-25-000158`) are inside the count. No split seen.
- **Market cap:** 570.540M x $12.86 = **$7,337M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-09 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-09, `0000764065-26-000025` (Items 1, 1A, 7, 8 read;
  the statements and the equity, lease and tax notes used); 10-Q for the quarter ended 2026-06-30, filed 2026-07-23,
  `0000764065-26-000100` (statements, debt note, subsequent-events note, POSCO paragraph); DEF 14A filed 2026-04-02,
  `0000764065-26-000054` (summary compensation table, pay versus performance, ownership table); 10-K for FY2022, filed
  2023-02-14, `0000764065-23-000032` (cash flow statements 2020 to 2022, equity statement); 8-K of 2026-07-24,
  `0000764065-26-000102`. Ten balance sheets from the XBRL filings printed by `tools/run.py` (accessions in the research
  folder, `run_py_output.txt`).
- **One figure cross-checked against the filed statement:** net cash used by operating activities for 2025, $(462)M on
  the filed Statement of Consolidated Cash Flows (10-K `0000764065-26-000025`), equals the XBRL value `tools/run.py`
  printed; revenue 2025 $18,610M likewise agrees.
- `python tools/run.py CLF`, arithmetic lines only: OCF less stock pay less capital spending, 2023 $1,580M, 2024
  $(640)M, 2025 $(1,080)M; three-year mean $(47)M (capex basis), $(466)M (D&A basis); the five-year window $675M
  (capex basis). Finance-lease principal printed as an alternate (2023 $92M, 2024 $49M, 2025 $67M). Stock pay 2023 to 2025
  $41M, $50M, $57M. The tool's own text beyond these lines (the v4 yields, "REFUSED" lines) was not used (Part VII).

**The lines of evidence this name needs, derived from the 2025 10-K (the brief's stated departure):**
1. *The cost position against the electric-arc-furnace producers and the integrated rivals* (Item 1, Competition: "EAFs
   comprise over 70% of steel production and more than 50% of flat-rolled steel production in the U.S."; the company's
   claim of "our inherent cost advantage in flat-rolled steel" under Strategy). Read from its own and rivals' margins.
2. *Who sets the price* (Item 1, Products and Markets: "approximately 35-40% of our flat-rolled steel shipments under
   fixed price contracts", the rest "based on the spot market at prevailing market prices or under contracts that involve
   variable pricing that is tied to an independently published steel index"; HRC called "the most significant index").
3. *Dependence on trade protection* (Item 1A, II, the first regulatory risk; Item 1, Competition: the 50% Section 232
   tariffs of 2025).
4. *Debt, liquidity and the capital raised* (Item 1A, III, the first financial risk; Item 7, Cash Flow, Liquidity and
   Capital Resources: the 2025 notes, the share issue, the ABL Facility).
5. *The acquisitions* (Item 1A, III, Stelco; Item 7 and Note 3), and *pension, OPEB and labor* (Item 1A, VI; Item 1,
   Competition, retiree benefits "which impacts our overall cost of production").

**The balance sheets, read first (Q4's eight to ten years, read here because the file may close before Q4)**
**[M2025-032]**. Ten year-ends 2017 to 2025 (`tools/run.py`, first-filed XBRL) and 2026-06-30 (10-Q):
- *Two companies in one table.* 2017 to 2019 is Cliffs Natural Resources, an iron-ore miner: assets $3.0B to $3.5B,
  equity negative in 2017 ($(444)M) and $358M in 2019, retained deficit $(4,207)M in 2017. In 2020 assets jump to
  $16.8B with AK Steel (paid in shares, 127M shares) and ArcelorMittal USA (78M shares, Series B preferred and cash;
  FY2022 10-K equity statement and cash flows). Nothing before 2020 describes the business now offered.
- *Equity against goodwill and intangibles.* Equity rose from $2.0B (2020) to $7.9B (2023) on the 2021 to 2022 boom and
  fell to $6.1B (2025) and $5.6B (2026-06-30). Goodwill $1.4B (2020), cut by a $125M impairment in 2023, back to $1.8B
  with Stelco (2024); intangibles $1.1B. Tangible equity at 2026-06-30 is about $2.8B against $7.7B of debt.
- *Debt.* Long-term debt $5.4B (2020), paid down to $3.1B (2023), then $7.1B (2024, Stelco), $7.3B (2025), $7.7B
  (2026-06-30: senior notes $6,878M principal plus ABL Facility $895M; 10-Q debt note). Finance leases a further $402M
  at 2025 year-end (10-K, Item 1A financial risk paragraph).
- *Cash.* Never more than $198M since 2020; $57M at 2025 year-end, $70M at 2026-06-30. Liquidity is the ABL Facility.
- *Receivables and inventory against sales.* Inventory $5.2B on $20.4B of revenue (2021), $4.8B on $18.6B (2025): about
  a quarter of a year's sales held as inventory throughout; receivables 7% to 11% of sales. No build out of line with
  sales was found; the 2024 build and 2025 release of pellet inventory are explained in the 2025 MD&A.
- *Retained earnings.* $(2,989)M (2020) to $1,733M (2023), back to $(529)M (2025) and $(911)M (2026-06-30): two years of
  losses have taken back most of what the boom retained.
- *Share count.* 271M shares at 2019 to 570.5M now: AK and AM USA (2020), 10M issued 2021, buybacks 2022 to 2024 (10.4M
  in 2023, 37.9M in 2024), 25.9M issued for Stelco (2024), 75M sold at $12.69 (2025).
- *What the figures cannot say:* the pension and OPEB promises (net liability $70M at 2026-06-30 on the face, with $154M
  paid in 2025), the asset-retirement and environmental obligations ($695M), and the Stelco employee-trust payments to
  2042 (10-K Note 20) sit outside debt and depend on assumptions.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is that a share is a business: would one be content to own this "if the market
closed for five years" **[M1997-109]**? The price of $12.86 is one the market quotes; it "just tells us prices"
**[M2006-077]**, and a move in it is no evidence. No macro forecast enters **[M2000-094]**: neither the steel price nor the
tariff regime is forecast here, which matters because both are named by the filer as the largest drivers (lines 2 and 3
above). The analyst's habit applied: look for "what’s wrong" **[M2025-013]**, and ask "What do I not know that I need to
know?" **[M1999-129]**. Who is paid to tell: the 10-K's competitive-strengths section is the seller's own description of
what it sells; its claim of a cost advantage is tested against the figures, not taken.
**Contrary evidence, written down as found** **[M1997-127]**:
- *For the business (found in Item 1):* internally sourced iron-ore pellets give "a stable and predictable cost"; busheling
  scrap averaged $424 per long ton in 2025 against a ten-year average of about $385, which the filer says favours an
  integrated producer; 50% tariffs from 2025; multi-year fixed-price automotive contracts signed in 2025; the unprofitable
  slab contract (about 10% of volume) expired 2025-12-09; Stelco described as "one of the lowest cost flat-rolled
  steelmaking assets in North America". Q2 2026 operating loss narrowed to $(49)M from $(501)M a year earlier (10-Q).
- *Against (found in Items 7 and 8 and the rivals' filings):* steelmaking gross margin (5)% in 2025 while the HRC price
  averaged $851 a ton, 10% above 2024; Adjusted EBITDA $37M for the whole of 2025; operating losses in 2024, 2025 and the
  first half of 2026 under the tariffs; six operations idled or closed in 2025.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin if the position is paid for with the buyer's own money and sized so that
its loss cannot end anything: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "Never risk
permanent loss of capital." **[L2023-005]**. The rule binds the buyer's conduct, not the target's; the target's debt is Q9's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as written.** Understanding is "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (a) the price of flat-rolled steel (HRC index,
  line 2); (b) the company's cost per ton against the producers who set that price (line 1); (c) North American
  light-vehicle volume (30% of 2025 revenue direct to automotive); (d) the trade regime (line 3). (a) and (d) are not
  foreseeable, and the framework says so is not by itself a stop: "We don’t think we can predict commodity prices."
  **[M2016-025]**; the business is judged "off the figures" **[M2008-069]**. Under the commodity-business paragraph of
  Q2 (decided 2026-10-12), Q1 asks only whether the business can be understood from its figures, and Q2 asks whether it is
  the low-cost producer.
- **Can it be understood from its figures?** Yes, by the rows' test: an integrated blast-furnace steelmaker selling flat
  steel into autos, service centres and manufacturing, with mines and coke ovens behind it. The technology is old and
  slow-changing in the sense of **[M1999-063]**; the change that matters (the shift to electric-arc furnaces) is a change in
  who is the low-cost producer, which is Q2's question, and it is readable from the filers' own figures: "The figures are
  available." **[M2009-059]**. Not a bank, not a black box, not a start-up. One segment decides (Steelmaking, 96% of 2025
  revenue: $17,953M of $18,610M, 10-K Item 7).
- **The doubt rule** **[M2002-092]** was put: the doubt found is about the price and the tariff, which the commodity
  paragraph sends to Q2 and Q7, not about whether the economics can be read.
- Routing: no fast-moving technology; the industry's insiders do write down cost-per-ton and margin figures **[M2000-105]**.
- **VERDICT: IN** **[M1995-051]**, **[M2012-065]**, on the filings above (10-K `0000764065-26-000025`).

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing" **[M1995-038]**. The commodity-business
paragraph (adopted 2026-10-12) sets the test for this name: is it the low-cost producer, read from its own and its
rivals' filings, "we would measure it, probably, more by cost of production than we would by whether copper was selling
for $2.00 a pound or a dollar a pound" **[M2006-004]**; and the same paragraph sends a high-cost producer in a commodity
field to OUT, on the row "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**.

**The competitors.** The 10-K names no rival by name: its Competition section names classes, "domestic and foreign
producers of flat-rolled carbon, plate, stainless and electrical steels", "EAF producers", and aluminum and other
substitutes; U.S. Steel appears only as the seller of the MinnTac option (Note 20). **CONVENTION of this run:** the rivals
compared are Nucor (NUE), Steel Dynamics (STLD) and United States Steel (X). Rationale: the 10-K says the price-setting
class is the domestic EAF flat-rolled producers (over half of U.S. flat-rolled output) and the other integrated mills;
NUE and STLD are the largest SEC-filing EAF flat-rolled producers and X the other SEC-filing integrated producer. X's last
10-K in its XBRL record is FY2024 (`0001163302-25-000018`); no FY2025 figure was found, so its span ends there. **Named
classes that do not file with the SEC:** the foreign producers (and the Canadian mills competing with Stelco), and the
aluminum producers as substitutes; not compared.

**The competitor row** (pre-tax income over revenue, each from its own 10-K XBRL; CLF before 2020 was an iron-ore miner
and is shown only for the record; research folder `compare_output.txt`):

| | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2020-25 aggregate | H1 2026 |
|---|---|---|---|---|---|---|---|---|
| CLF (`0000764065-26-000025`, `0000764065-23-000032`; H1 `0000764065-26-000100`) | (3.6)% | 18.6% | 7.8% | 2.6% | (5.0)% | (10.8)% | 2.8% | (4.5)% |
| NUE (`0001193125-26-071575`) | 4.1% | 25.2% | 24.7% | 18.1% | 9.4% | 7.9% | 16.3% | not found in the cached facts |
| STLD (`0001104659-26-021395`; H1 `0001104659-26-087414`) | 7.4% | 22.9% | 22.6% | 17.1% | 11.3% | 8.2% | 15.9% | 10.6% |
| X (`0001163302-25-000018`) | (13.4)% | 21.4% | 15.5% | 5.8% | 2.8% | n/a | 9.2% (2020-24) | n/a |

Over the whole span since CLF became a steelmaker, CLF has the lowest margin of the four in every year from 2021 to 2025
and in the first half of 2026, including 2021, the boom year. Its aggregate 2020 to 2025 pre-tax margin is 2.8% against
16.3% and 15.9% for the two EAF producers. Pre-tax income plus interest over year-end equity plus long-term debt, the
same span: CLF (0.3)%, 38.2%, 17.0%, 7.6%, (5.1)%, (11.6)% (2020 to 2025); STLD 11.0%, 45.8%, 45.7%, 27.8%, 17.1%, 12.5%.
And the mix runs in CLF's favour, not against it: its average selling price was $1,005 a ton in 2025, on a book weighted
to automotive grades that "generally allows for higher selling prices" (10-K Item 1). A higher price and a lower margin
means a higher cost per ton.

**The parts table** (10-K Item 7 and the segment note): one reportable segment.

| Part | 2025 revenue | 2025 Adjusted EBITDA (filer's measure) | Castle | Decides |
|---|---|---|---|---|
| Steelmaking | $17,953M | $(16)M (2024: $715M) | tested below | yes: more than half of revenue and the only reportable segment |
| Other Businesses (tubing, tooling and stamping) | $657M | $53M | not tested; "highly fragmented markets" (Item 1) | no |

Operating income is not reported by segment; the file closes on Steelmaking. (In 2025 the small part out-earned the large
one on the filer's own measure; carried as a fact, not weighed.)

**The castle tests, each with its filing fact.**
1. *The castle questions and the low-cost position (tests 1 and 6; the commodity exception).* "commodity businesses have
   risk unless you’re the low-cost producer, because the low-cost producer can put you out of business" **[M1997-010]**.
   The filer claims "our inherent cost advantage in flat-rolled steel" (Item 1, Strategy). The figures above say the
   opposite in every year read: "It’s like comparing a copper producer whose costs are $2.50 a pound with a copper
   producer whose costs are $1 a pound. Those are two different kinds of businesses." **[M2009-059]**. In 2025, with
   HRC averaging $851 a ton (10% above 2024) and imports down under 50% tariffs, Steelmaking's gross margin was (5)% and
   the company lost $1,579M at the operating line; STLD earned an 8.2% pre-tax margin in the same market.
2. *Who sets the price (the commodity marks).* 60% to 65% of flat-rolled shipments are sold at spot or on an
   independently published index (Item 1); the HRC index is "the most significant index in driving the revenues and
   profitability of our Steelmaking segment". "whatever he charged for gas was my price" **[M2012-109]**; "he determined
   our profit, because we looked at his price every day" **[M2023-079]**. The price is set in the market the EAF mills
   supply, and CLF takes it.
3. *The money test.* "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?
   [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The attackers are already building: the
   10-K itself records "recently completed and further announced flat-rolled EAF capacity additions in the U.S." and that
   EAFs make "more than 50% of flat-rolled steel production". "one competitor is frequently enough to ruin a business"
   **[M2012-108]**.
4. *Pricing power.* None found: the filer's own explanation of 2025 is that revenue fell about $1.2B on "inconsistent
   buying behavior" and about $400M on mix (Item 7), and a higher HRC price did not reach its margin. "it’s not a great
   business when you have to have a prayer session before you raise your prices a penny" **[M2005-020]**.
5. *The automotive book, the one part of the claim the filings partly support.* Automotive grades are "more operationally
   and technologically intensive to produce" and the company is "a leading supplier of automotive-grade steel in the U.S."
   (Item 1); multi-year fixed-price contracts were signed in 2025. But direct automotive revenue fell 9% in 2025 ($5,047M
   from $5,571M) and was 30% of the total, and the premium it earns did not lift the company off the bottom of the row in
   any year. A moat is what "protects excellent returns on invested capital" **[L2007-004]**; a niche that does not show in
   the margin over the whole span is not one the figures can credit.
6. *Widening or narrowing (test 10).* Narrowing on the filer's own record: six operations idled or closed in 2025
   (Dearborn's hot end, Steelton, Conshohocken, Riverdale, Minorca, part of Hibbing); Weirton idled in 2024; margins 7.8%,
   2.6%, (5.0)%, (10.8)% from 2022 to 2025 while the EAF share of flat-rolled passed half. "you do not want to have
   something whose competitive position is going to erode over time" **[M2007-117]**.
7. *What could destroy, modify or reduce it (test 11)* **[M2000-014]**: the end of the 50% tariffs (Item 1A, II, first
   risk); the further EAF additions (line 1); retiree costs, "which impacts our overall cost of production relative to
   certain other steelmakers" (Item 1, Competition).
8. *A change for the better?* The filer points to the tariffs, the end of the slab contract and the Stelco cost base.
   The rows credit such a change only on a full cycle **[M2017-026]**, **[L1995-022]**. Here no credit is needed to answer
   the question, because the change has already been tried against the evidence: a full year of 50% tariffs with Stelco
   owned (2025), and a half-year after the slab contract ended (H1 2026: operating loss $(262)M on $10,148M of revenue,
   10-Q `0000764065-26-000100`), leave CLF at the bottom of the row while STLD earned 10.6% pre-tax in the same half. The
   question is answered on the evidence, so the box is not TOO HARD **[M2000-019]**.

**The field's returns over the last full cycle.** The field's durable low-cost players (NUE, STLD) earned about 16% pre-tax
on revenue in aggregate over 2020 to 2025, and STLD 11% to 46% pre-tax on equity plus debt in every year; the field's
castle belongs to them. The "ordinary returns" clause does not decide this name; the high-cost clause does.

- A castle shown open on the evidence closes OUT **[M2011-015]**: here, the high-cost producer in a commodity field
  **[M1997-010]**, **[L1994-035]**: "In an unregulated commodity business, a company must lower its costs to competitive
  levels or face extinction." The filer's statements that it holds a cost advantage are weighed against its own and its
  rivals' figures **[M2009-059]**, and the figures decide. Price does not reopen it: "What you can’t do is turn any
  investment into a good deal by paying little" **[M2019-015]**.
- **VERDICT: OUT**, with ids above. Q3 to Q12 NOT REACHED.

## Q3 to Q12: NOT REACHED (the Q2 STOP closed the file; operator rule 2). Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q2: the high-cost producer in a commodity field** (**[M1997-010]**, **[L1994-035]**, **[M2009-059]**): the lowest
pre-tax margin of CLF, Nucor, Steel Dynamics and U.S. Steel in every year from 2021 to 2025 and in the first half of 2026,
2.8% in aggregate over 2020 to 2025 against about 16% for the two EAF producers, under 50% tariffs in 2025 and with the
slab contract gone in 2026. **Integrity facts recorded, not judged** (Q5, below). COMPUTATION, NOT A CLEARANCE, beside the
price of $12.86: value range (the no-growth case alone, see below) $1.77 a share all-equity, central, cycle base; $9.63 on
the literal window beside; equity-only $9.25 (cycle) and $16.58 (literal); no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.)*

**Bearing on Q3 (capital).**
- Capital spending $525M, $705M, $943M, $646M, $695M, $561M (2020 to 2025); the filer expects about $700M in 2026, which
  "primarily consists of sustaining capital spend" (10-K Item 7, Cash requirements). D&A $897M to $1,235M (2021 to
  2025), above capital spending from 2023; 2025 D&A includes about $300M from idled facilities and Stelco (Item 7).
- Environmental capital $66M, $67M, $66M (2023 to 2025), about $71M a year expected for 2026 to 2028; the 2024 NESHAP
  rules for taconite, iron and steel and coke carry compliance obligations from 2027 that "could be material"; a selenium
  treatment system (Empire liability about $143M; Tilden about $32M of capital) (10-K Item 1, Regulatory Developments).
- Owner cash over revenue: 9.3%, 5.6%, 6.5%, (3.8)%, (6.6)% (2021 to 2025, equity-only, before purchases;
  `value_output.txt`).

**Bearing on Q4 (the accounts).**
- *An error corrected:* the 2025 10-K (Note 1, "Correction of an immaterial error") reports an accrual for employment
  costs that understated cost of goods sold in 2022, 2023, 2024 and the first two quarters of 2025; 2023 and 2024 cost of
  goods sold raised $18M and $7M; accrued employment costs at 2024 year-end raised $39M and retained earnings cut $30M.
- *The adjusted figure the filer features:* Adjusted EBITDA, which "management believes [...] is a useful measure to assess
  the earnings power of the business" (Item 7, Non-GAAP measure); $1,893M, $773M, $37M (2023 to 2025) against operating
  income of $659M, $(763)M, $(1,579)M. The proxy's pay-versus-performance table names it as the company-selected measure.
- *Guidance:* Item 1A, III: "Our actual operating results may differ significantly from our guidance."
- *Charges that recur:* goodwill impairment $125M (2023); restructuring $129M and $86M, asset impairment $79M and $39M
  (2024, 2025); idled-facility charges in cost of goods sold and in miscellaneous (2025 about $70M and $40M).
- Ten balance sheets read in Step 0; no receivable or inventory build out of line with sales was found.

**Bearing on Q5 (the people): integrity facts recorded, not judged.**
- The Chief Financial Officer, Celso Goncalves, is the son of the Chairman and CEO, Lourenco Goncalves (10-K, executive
  officers). On 2026-07-21 the board named him President and CFO and a director, raised his salary from $884,000 to
  $1,000,000 and his change-in-control severance multiple from two years to three (8-K `0000764065-26-000102`).
- CEO total pay in the summary compensation table: $26.1M (2023), $15.2M (2024), $19.0M (2025), the 2025 figure in a year
  of a $1,428M net loss; pay-versus-performance shows a $100 investment worth $91.20 at 2025 year-end against $324.78 for
  the company's chosen peer group (DEF 14A `0000764065-26-000054`). The CEO beneficially owned 2,378,347 shares at
  2026-03-16 (same proxy), about $31M at the price.
- The 10-K and the 10-Q call the unsigned POSCO transaction "highly accretive to our shareholders" while stating that its
  terms remain to be negotiated (10-K Item 1; 10-Q Note on the POSCO memorandum).
- The habits carried for Q5 by Q4's convention: the featured Adjusted EBITDA and the guidance, above.

**Bearing on Q6 (the money and the owners).**
- *Buybacks:* a $1.5B programme authorised 2024-04-22 naming no price (10-K Item 5); 37.9M shares bought in 2024 for
  $737M (equity statement), an average of about $19.45 a share; 10.4M in 2023 for $153M (about $14.70); $240M in 2022.
  The Q6 test reads these against the bottom of the Q7 range; the COMPUTATION below puts every case under $17 a share,
  so every 2024 purchase was above it (written here as the line back to Q6, not weighed).
- *Issuance:* 75M shares sold at $12.69 on 2025-10-30 for $951M of net proceeds, used to repay the ABL Facility (Item 7),
  ten months after buying 37.9M at about $19.45. Shares outstanding 271M (2019) to 570.5M (2026).
- *Deals:* AK Steel (2020, paid in shares: 127M shares), ArcelorMittal USA (2020: 78M shares, Series B preferred
  redeemed for $1,343M in 2021, and cash), FPT (2021, $761M cash), Stelco (2024: C$60.00 cash and 0.454 share per Stelco
  share; $2,512M net cash and 25.9M shares), sale processes for non-core assets launched 2025, the POSCO memorandum.
- No common dividend since 2020 ($41M paid that year).

**Bearing on Q9 (debt and exposures).**
- Debt $7,703M at 2026-06-30 (senior notes due 2029 to 2040, $6,878M principal, coupons 4.875% to 7.625%; ABL Facility
  $895M, maturing June 2028, with a springing fixed-charge covenant of 1.0 to 1.0); finance leases $402M at 2025 year-end;
  cash $70M (10-Q). Interest paid $459M in 2025. Pre-tax losses in 2024, 2025 and the first half of 2026.
- Liquidity $3.3B at 2025 year-end (cash plus ABL availability); surety bonds and surety-backed letters of credit $278M.
- Pension and OPEB: $154M paid in 2025, $126M expected in 2026; Stelco employee-trust payments to 2042.
- The acquisition criteria's "(3) Businesses earning good returns on equity while employing little or no debt"
  **[R1997-001]** is noted against these figures, not applied.

**Bearing on Q7: COMPUTATION, NOT A CLEARANCE.** *(All of the following is arithmetic under Q7's convention, after a closing
STOP; it is no verdict and carries no entry language. Script and output: research folder `value.py`, `value_output.txt`.)*
- *Owner cash* after every real cost **[L2015-004]**: operating cash flow less stock pay less capital spending less
  finance-lease principal less distributions to the minority partners ($M; FY2022 and FY2025 10-Ks):

  | | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|
  | OCF | (258) | 2,785 | 2,423 | 2,267 | 105 | (462) |
  | less stock pay | 17 | 18 | 28 | 41 | 50 | 57 |
  | less capital spending | 525 | 705 | 943 | 646 | 695 | 561 |
  | less finance-lease principal | 15 | 94 | 96 | 92 | 49 | 67 |
  | less minority distributions | 61 | 62 | 74 | 67 | 48 | 76 |
  | **owner cash, equity-only, before purchases** | (876) | 1,906 | 1,282 | 1,421 | (737) | (1,223) |
  | interest paid | 170 | 299 | 249 | 256 | 255 | 459 |
  | **owner cash before interest (all-equity)** | (748) | 2,130 | 1,469 | 1,613 | (546) | (879) |
  | businesses bought, net of sold | 1,527 | 707 | 31 | (35) | 2,512 | (53) |

  The interest add-back is taken after tax at 25%: **CONVENTION of this run**, the filer's own effective rate for 2024
  (25%; 2023 25%, 2025 29%), since Q7 states the all-equity basis but no rate for the add-back.
- *(a) The cycle base.* The literal window 2021 to 2025 opens on the boom year (record results) and closes on a year the
  filer calls one of "recession-like conditions" in its largest end markets (Item 7); both ends are aberrational
  **[L2005-003]**. The only full cycle the steelmaker has is trough to trough, 2020 to 2025; 2020 holds AK Steel only
  from 2020-03-13 and ArcelorMittal USA only from 2020-12-09, so the year understates, and the merger-inside-the-window
  rule (combined companies' averages) was not built (the pre-merger AK figures were not read; confessed). Cycle base: all-equity
  $506M, equity-only $296M. Literal window beside: all-equity $758M, equity-only $530M.
- *(c) The serial acquirer.* Net purchases 2021 to 2025, $3,162M, exceed half of owner cash before purchases ($1,324M),
  so the central figure is the organic pair (purchases left out), with the default pair beside. Stelco is classed an
  acquisition (paid mostly in cash, C$60.00 against 0.454 share). The filer reports no organic growth rate.
- *(b) Growth.* The owner-cash series changes sign; the halves are $1,594M (2021 to 2022) and $(980)M (2024 to 2025),
  also a change of sign, so the growth is meaningless and **the range is the no-growth case alone**, said so. (f), the cap:
  no growth carried. (d) Working capital is inside operating cash. (e) The filer calls its capital spending
  "primarily" sustaining; the whole of it is taken as maintenance, so the maintenance case and the all-spending case are
  the same; the depreciation variant beside: window equity-only $222M.
- *Net debt* at 2026-06-30: debt $7,703M plus finance leases $402M (2025 year-end, the latest stated figure) less cash $70M
  = **$8,035M**; operating leases, pension and OPEB, asset-retirement obligations and the Stelco trust payments left out,
  said so. The 10-Q's subsequent-events note states no event.
- *The range, at the 5.60% sovereign, zero growth after year ten as before it:*
  - **Central, all-equity, cycle base: $506M / 5.60% = $9,036M less $8,035M = $1,001M = $1.77 a share** (the script's
    unrounded average).
  - Literal window, all-equity: $758M → **$9.63 a share**.
  - Equity-only beside: **$9.25** (cycle base), **$16.58** (literal window).
  - Default pair beside (acquisitions deducted, total growth credited): window all-equity $125M, below net debt at any
    rate; equity-only $(103)M. No positive value.
- *The floor, tested first:* owner cash before interest over market value plus net debt ($15,372M) is 3.3% on the cycle
  base and 4.9% on the literal window; equity-only, owner cash over market value ($7,337M) is 4.0% and 7.2%. **No case
  earns about ten percent at $12.86** **[M2003-149]**; the price is above the top of the central range. Q7 would close
  OUT on the floor; the width test does not arise (one case).
- *Reporting figures (Part VII; a reporting convention, not a rule; no verdict, no entry language).* **VALUE RANGE: $1.77 a
  share** (all-equity, central; the no-growth case alone, so the two ends coincide), $9.63 on the literal window beside;
  equity-only $9.25 (literal $16.58). **FAIR PRICE: none positive on the all-equity basis** ($506M / 10% = $5,060M, less
  net debt $8,035M = $(5.21) a share; literal window $(0.81)); **equity-only fair price $5.18 a share** (cycle base;
  $9.29 on the literal window). Tax: the company's own, inside operating cash. The central figure is the all-equity one;
  the equity-only figure is beside it and does not decide. The purchases-stop-after-year-ten rule changes nothing here,
  since the central figure is already the organic pair. Owner cash before interest of about $1,537M a year would be
  needed for ten percent on market value plus net debt at the price; it was reached in 2021 and 2023 only.

**Bearing on Q8, Q10, Q12:** nothing found beyond the above.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit bef1f0c9); written question by question; committed after Step
      0 to Q1 (ffd65125), after Q2 (a8aff8f3), and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's. The run binds
      nothing until folded into the register (operator rule ten).
- [x] No other run file, holding review, `PORTFOLIO.md`, RESUME STATE, queue or reading-list file was opened or searched.
      One directory listing filtered to today's date showed other companies' run-file names; declared under
      contamination at the top, not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by the research folder's `check_ids.py` (every id exists;
      every quoted fragment beside an id is in that row; no E-id). Every filing fact carries its accession or names its
      filing.
- [x] The order was kept; Q2's STOP closed the file; everything after it is headed as facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, all capital spending, finance-lease principal, minority distributions),
      never a net-income proxy; sovereign from the US Treasury, dated; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP; the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor rule arises.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before the closing commit (result in the closing commit message).
- Honest weaknesses: (1) the margin comparison is whole-company pre-tax margin, not cost per ton; mix, mining and
  downstream businesses differ among the four, and CLF's higher selling price makes the conclusion stronger, not weaker,
  but a per-ton cost from each filer's segment note was not built. (2) NUE's first-half 2026 figure was not found in the
  cached XBRL facts. (3) X's FY2025 is missing. (4) The 2020 year in the cycle base is a partial-merger year.
  (5) Finance leases at 2026-06-30 were not stated; the 2025 year-end figure was used.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) The brief and Q2 ask for the rivals the 10-K names; CLF's 10-K names classes, not companies, so the
choice of NUE, STLD and X is a convention of this run, and a run choosing differently (say, only integrated mills) could
read the field's returns differently; the commodity paragraph's "its operators' filings" does not say which operators.
(2) Q7(a) asks for the last full cycle, but this business has existed as a steelmaker for one cycle only, and the trough
year that opens it is a partial-merger year; (a) and (c)'s merger rule pull against each other and the text does not say
which governs when the cycle's first year is the merger year. The cycle base was used, the merger rule not built, and the
literal window shown beside. (3) The serial-acquirer threshold (purchases over half of owner cash before purchases) is
tripped here by one large deal (Stelco) in a window where owner cash nets to little; the label "serial" fits awkwardly,
but the text was applied as written. (4) Q7's all-equity basis states owner cash "before interest" without saying whether
the interest is added back before or after tax; 25%, the filer's own rate, was confessed. A smaller point: when the range
is the no-growth case alone, Part VII's "each end case valued at ten percent, the two averaged" collapses to one case;
it was read that way.
