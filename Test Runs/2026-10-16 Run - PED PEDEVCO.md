# Company Run: PEDEVCO Corp. (NYSE American: PED), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch (commit
`4108301b`).

**Dispatched blind run.** Analyst working from the canonical brief with its one stated departure (the lines of evidence are
derived by the analyst from Items 1, 1A and 7 of the 10-K, below). Research folder: `Test Runs/_research 2026-10-16 PED/`
(raw filings in its ignored `cache/`; the scripts `fetch.py`, `totext.py`, `facts.py`, `peers.py`, `row.py` and the notes
file are tracked).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: not held (`PORTFOLIO.md` carries no line for PED or PEDEVCO).

**Contamination, declared.** (1) A directory listing of `Test Runs/` filtered on the run date, made to check that this file
did not already exist, showed the file names of ten other runs dated 2026-10-16 (HMH, INVX, NESR, NGS, NOV, OIS, OMSE,
RCON, SEI, USAC) and their research folders; none was opened. (2) The session context carried recent commit subjects about
the RCON fold, a git status naming two other research folders (ARCB, AYI), and memory-index lines about queue state
("57 gate-clearers, nothing buyable"). (3) The project map (`CLAUDE.md`) loaded with the session. None of these concerns
PED or any former name of it (Blast Energy Services, Verdisys, Reconstruction Data Group, Rocker & Spike Entertainment);
none was used.

**Lines of evidence, chosen by this analyst** from Item 1 (business), Item 1A (risks) and Item 7 (MD&A) of the 10-K filed
2026-03-31 (accession 0001654954-26-003098), this brief's stated departure; the dispatcher wrote none:
1. The cost of production against the operators in the same basins (Item 1 claims "Low-Cost Development" and, after the
   mergers, "a low-cost operating profile"; Item 1A names "Intense competition"; Item 7 gives lease operating expense). Q2.
2. The full-cycle record of operating results (Item 1A: "We have incurred net losses of $121,860,000 from the date of
   inception (February 9, 2011) through December 31, 2025"). Q2, Q3.
3. The mergers of 2025-10-31 with North Peak Oil & Gas and Century Oil and Gas Sub-Holdings: consideration, financing,
   control passing to Juniper Capital Advisors (Items 1, 1A, 7). Q6, Q7, Q9.
4. The revolving credit facility ($98.0M drawn at filing), borrowing base redeterminations, hedging covenants (Items 1A, 7). Q9.
5. Reserve replacement and capital needs: 49% of proved reserves undeveloped, decline, the 2026 capital budget (Items 1A, 7). Q3, Q7.
6. Restatements of FY2022, FY2023 and FY2024 and material weaknesses (Items 1A, 9A). Q4, Q5.
7. Controlled-company status, the corporate-opportunity waiver, the affiliate midstream contract (Items 1, 1A). Q5, Q6.
8. Federal leases in the Powder River Basin under litigation; the New Mexico plugging order (Items 1, 1A). Q9.
9. Dilution and the issuance record (Item 1A). Q6.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $13.48 (close 2026-10-15; `tools/run.py`'s live quote, an **aggregator, flagged** under operator rule 5).
- **Shares by class:** 13,290,902 common, single class (10-Q for the quarter to 2026-06-30, filed 2026-08-13, accession
  0001654954-26-007591; `python Screens/cover_shares.py PED`, cover as of 2026-08-11). Checked: the 10-Q balance sheet gives
  13,290,902 shares "issued and outstanding", no treasury shares; the 10-K gives 13,300,815 outstanding on 2026-02-27 after
  the 8,506,818-share preferred conversion and before the 1-for-20 reverse split's fractional cash-outs (8-K of 2026-03-13,
  accession 0001654954-26-002217); the Series A preferred is gone (A&R charter, 8-K of 2026-03-03, accession
  0001654954-26-001835). Filings after the 10-Q: an S-3 (2026-08-25) and a 424B3 (2026-09-09), the S-8 of 2026-09-15 for
  the plan increase approved at the 2026-08-27 meeting (8-K accession 0001654954-26-007962), and RSU grants (8-K of
  2026-06-24, accession 0001654954-26-006156) not yet settled; no issued share count beyond 13,290,902 was found.
- **Market cap:** 13,290,902 x $13.48 = **$179.2M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-15
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2025, filed 2026-03-31, accession 0001654954-26-003098 (Items 1, 1A, 7,
  8, 9A, 10 to 13 searched); the 10-Qs for Q1 2026 (0001654954-26-004891) and Q2 2026 (0001654954-26-007591); the proxy
  (DEF 14A, filed 2026-07-15, 0001654954-26-006667); the information statement on the mergers (DEFM14C, filed 2026-02-02,
  0001654954-26-000782), which carries the acquired companies' MD&A for 2023, 2024 and nine months of 2025; the 8-Ks of
  2026 (accessions 0001654954-26-000231, -000763, -000956, -001566, -001835, -002217, -004632, -005181, -006156, -006257,
  -006724, -006883, -007586, -007962, -008401, -008485) and the 8-K/A of 2026-08-25 (-007860); the 10-Ks for FY2019
  (0001654954-20-003503), FY2021 (0001654954-22-003008), FY2022 (0001654954-23-003759), FY2023 (0001654954-24-003240) and
  FY2024 (0001654954-25-003703) for the cycle.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $10,758
  thousand in the XBRL transcription and $10,758 thousand on the filed Consolidated Statement of Cash Flows of the 10-K
  (0001654954-26-003098). Agrees.
- **`tools/run.py PED`, arithmetic lines only.** Its owner-earnings columns are **wrong for this filer**: the tool took
  "PaymentsToAcquireOtherPropertyPlantAndEquipment" (vehicles, $0.0M to $0.2M) as capital spending, while the filer's
  capital spending is the line "Cash paid for drilling and completion costs". Its "OE capex" figures (21.4, 10.7, 8.0) are
  therefore not used. Its D&A-basis figures (10.6, -5.0, -10.0) agree with the hand figures below. Its ten balance sheets
  are used for Q4 (read below, since the file may close before Q4).

**Owner cash, recast by hand from the filed cash-flow statements** (USD thousands; legacy PEDEVCO before the mergers, with
November and December 2025 of the acquired companies inside FY2025). Capital spending is the filer's net cash used in
investing, less the merger cash in 2025 ($115,646) and less a note lent to the buyer of a subsidiary in 2023 ($1,122);
2021's figure nets property-sale proceeds the statement shows only as the difference between the lines (inferred, flagged).
| FY | OCF | stock pay | capital spending, net | owner cash, all spending | DD&A | owner cash, DD&A variant | cash interest |
|---|---|---|---|---|---|---|---|
| 2021 | 5,970 | 2,452 | 2,761 | 757 | 7,380 | -3,862 | 0 |
| 2022 | 15,981 | 2,097 | 12,266 | 1,618 | 11,153 (as first filed; restated lower) | 2,731 | 0 |
| 2023 | 23,481 | 2,043 | 34,621 | -13,183 | 9,440 (restated) | 11,998 | 0 |
| 2024 | 12,766 | 1,859 | 26,874 | -15,967 | 15,920 | -5,013 | 0 |
| 2025 | 10,758 | 2,763 | 17,537 | -9,542 | 18,009 | -10,014 | 590 |
| **mean** | | | | **-7,263** | | **-832** | |

Never a net-income proxy (operator rule 5). Stock pay is complete as the filer reports it (one line, "Share-based
compensation expense"). No cash income tax was paid in any year read (cash-flow supplements); the company carries net
operating losses. The 2025 operating cash includes $7,457 thousand of merger costs (Item 7, Adjusted EBITDA reconciliation).

---
## THE FOUNDATIONS (not a gate)
Three bear on this name. A share is a business: the question is whether I would be content to own this producer "if the
market closed for five years" **[M1997-109]**, which turns attention from the quotation to the cost of each barrel. No
macro conclusion enters: "macro conclusions are — just never enter into the discussion" **[M2000-094]**, and the speakers
say of themselves "we are not two fellows who think we can predict the price of soybeans or corn or oil or anything else"
**[M2016-025]**; so no oil-price view is used to clear or to close this file, and the 2026 price spike that Item 1A
describes (WTI to about $98 after "the initiation of the recent conflict in Iran") is read as a fact about one half-year,
not a forecast. The market serves and does not instruct **[M2006-077]**. The analyst's habits: look "for what’s wrong in
things" **[M2025-013]**, and write contrary evidence at once.

**Contrary evidence, written down as found** **[M1997-127]**: (1) the first half of 2026 shows operating income of $22.1M
on $86.3M of revenue (10-Q, 0001654954-26-007591), the first sizeable operating profit in the record read; (2) management
claims "Low-Cost Development" and "a low-cost operating profile" (10-K, Item 1); (3) the half-year run rate of owner cash
after a depreciation charge, annualized, is positive and large against the price (computed under Q7's heading below, beside
the convention's figure). Each is answered where it bears.

## THE STANDING RULE
Owning this would be bought with the buyer's own money and sized so that a total loss cannot touch what the buyer has and
needs; the rule binds the buyer's conduct, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and
leverage is "the one thing that ends — or can prevent you from playing out your hand" **[M2004-065]**. Nothing in the
target forces a call on the buyer (no partly-paid shares, no guarantee). **No ruin to the buyer from an unlevered,
sized holding.** The target's own debt is weighed at Q9.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filings.** An onshore producer of oil (about 72% of proved reserves; Item 1A), natural
  gas and NGLs from legacy fields in the D-J Basin (Colorado and Wyoming), the Powder River Basin (Wyoming, 89% of net acres on
  federal land) and the San Andres of the Permian (New Mexico); 2,494 Boe a day in 2025, 7,442 Boe a day in the first half
  of 2026 after the mergers; sold at index prices less differentials to a few purchasers on short, cancellable contracts
  (Item 1, Marketing). It sells a commodity at a price it does not set.
- **The key variables** **[M1998-044]** are four: the price of oil (not foreseeable by anyone, and the rows do not ask it to
  be **[M2016-025]**, **[M2011-044]**); volumes, which decline unless capital is put back (Item 1A: "Unless we replace our oil
  and natural gas reserves, our reserves and production will decline"); the cost of each barrel lifted, against the other
  producers in the same basins; and the capital needed to stand still. The last three are read off the figures, which is
  what the rows ask of a commodity producer: "if you can’t make a decision on something like PetroChina off the figures,
  forget about going further" **[M2008-069]**; "What is important is that I understand the economic dynamics of the
  industry" **[M2011-014]**.
- **Do the past statements tell me the future ones** **[M2008-033]**? In kind, yes: ten years of filed statements show a
  price-taking, depleting producer whose cost position has not moved relative to its neighbours (Q2). In scale, only in
  part: the mergers of 2025-10-31 tripled the volumes, and the acquired companies' record (2023, 2024, nine months of 2025)
  is in the information statement, not in PEDEVCO's own history. That is a limit on the valuation (Q7), not on
  understanding what kind of business this is.
- **Routing.** A dependence on a commodity price is never by itself a STOP at Q1 (the framework's commodity paragraph,
  **[M2016-025]**, **[M2008-069]**); where the business sits on the cost curve is Q2's test, "more by cost of production than
  we would by whether copper was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**. Not a bank, not a fast-
  changing technology; the parts (three basins) have the same economics and are read as one business.
- **Doubt, tested** **[M2002-092]**: what would put this outside the circle is a confusing account of what a barrel costs.
  The filings state unit production costs every year (Item 1 tables), so the fix on "earning power and competitive position"
  that **[M2012-065]** asks for can be taken from them.
- **VERDICT: IN.** The economics are a commodity producer's and are read from its own and its neighbours' figures
  **[M2008-069]**, **[M2011-014]**; the decisive question is where it stands on cost, which Q2 asks.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The test that decides, for a commodity producer.** The framework's commodity paragraph places it here: Q2 asks whether
the business is the low-cost producer, "read from its own and its operators' filings", and "a high-cost producer in a
commodity field is OUT". The rows: "commodity businesses have risk unless you’re the low-cost producer, because the
low-cost producer can put you out of business" **[M1997-010]**; "when a company is selling a product with commodity-like
economic characteristics, being the low-cost producer is all-important" **[L2000-017]**; the measure is "cost of
production" **[M2006-004]**, and "The figures are available." **[M2009-059]**.

**The competitor row.** The Competition section of Item 1 names no company. Item 1 does name the operators in the same
basins: in the D-J, "Chevron Corporation [...], SM Energy Company (which merged with Civitas Resources, Inc. in January
2026 [...]), EOG Resources, Inc., Occidental Petroleum Corporation, Bison Oil & Gas IV, and Peoria Resources, LLC (a U.S.
subsidiary of Japan Petroleum Exploration Co., Ltd.)"; in the Powder River, "Anschutz Exploration Corporation, Continental
Resources, Inc., Devon Energy Corporation, EOG Resources, Occidental Petroleum Corporation"; in the Permian, its partner
Evolution Petroleum Corporation. They are named as offset operators and partners, not as competitors, which is the nearest
the filing comes. **Chosen, three that file with the SEC:** Civitas Resources (the D-J pure player of the period, formerly
Bonanza Creek), SM Energy (its successor in the D-J after January 2026) and Evolution Petroleum (PED's partner in the same
Chaveroo field). **Named and filing, not chosen:** Chevron, EOG, Occidental, Devon, whose per-Boe costs span many basins and
do not isolate these. **Named and not filing with the SEC:** Bison Oil & Gas IV and Anschutz Exploration (private); Peoria
Resources (subsidiary of a Japanese filer); whether Continental Resources still files was not checked. The table with every
source is `Test Runs/_research 2026-10-16 PED/q2_cost_and_margin.csv`.

| Unit production cost, $ per Boe (each filer's own definition) | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| **PEDEVCO** (excl. workover, marketing, ad valorem, severance) | 13.62 | 19.77 | 15.32 | 13.09 | 13.44 | 13.12 | 8.98 | 10.36 | 11.62 | 13.72 (direct LOE) |
| Acquired companies (LOE and workover) | | | | | | | 15.09 | 18.63 | | |
| Civitas / Bonanza Creek (LOE and midstream opex, excl. taxes) | 9.28 / 8.20 | 7.11 | 4.35 | 4.00 | 3.41 | 3.25 | 4.47 | 4.96 | | |
| SM Energy (LOE; transport and taxes separate) | 4.43 | 4.74 | 4.67 | 3.97 | 4.39 | 5.03 | 5.13 | 5.11 | 5.71 | |
| Evolution Petroleum, Chaveroo field only (FY to June) | | | | | | | | | | 13.76 (FY2026) |

Sources: PEDEVCO 10-Ks FY2019 (0001654954-20-003503), FY2022 (0001654954-23-003759), FY2025 (0001654954-26-003098), 10-Q
(0001654954-26-007591); acquired companies, DEFM14C (0001654954-26-000782); Civitas 10-Ks FY2019 (0001509589-20-000011),
FY2022 (0001509589-23-000017), FY2024 (0001509589-25-000009); SM Energy 10-Ks FY2019 (0000893538-20-000009), FY2022
(0000893538-23-000014), FY2025 (0000893538-26-000032); Evolution 10-K FY2026 (0001104659-26-108258). The definitions differ
at the edges (PED's leaves out workovers, Civitas's adds midstream opex), and the gap does not depend on them: across nine
years PEDEVCO lifted a barrel at 1.5 to 4.2 times what Civitas and SM Energy spent (1.5 times Bonanza Creek in
2017, 1.75 times SM Energy in 2023, three to four times both in 2019 to 2022, about twice both in 2024 and 2025), and the companies it bought in 2025
were costlier still. The one field the record lets me compare like for like, Chaveroo, costs its partner $13.76 a Boe.

| The full span, from the filers' XBRL (USD millions) | years | revenue | operating result | margin | loss years |
|---|---|---|---|---|---|
| **PEDEVCO** | 2015-2025 | 200.0 | -93.2 | -46.6% | 8 of 11 |
| SM Energy | 2015-2025 | 22,887.3 | 2,749.4 | 12.0% | 5 of 11 |
| Civitas (pretax; 2017 not on a twelve-month basis) | 2015-2024 | 14,704.0 | 3,156.8 | 21.5% | 2 of 9 |
| Evolution Petroleum (June years) | FY2016-FY2026 | 702.5 | 137.5 | 19.6% | 1 of 11 |

The span runs through the 2015-2016 trough, the 2020 collapse and the 2022 peak, a full oil cycle. PEDEVCO earned an
operating profit in three of eleven years (2022, 2023 as restated, 2024), never more than $4.7M, and its own 10-K counts
"net losses of $121,860,000 from the date of inception (February 9, 2011) through December 31, 2025" (Item 1A). The
neighbours, on the same prices, earned positive operating results over the span.

**The castle tests, each against the filing.**
- *The attacker with money* **[M2011-015]**: acreage is bought at auction; PEDEVCO itself bought Wyoming acreage at the
  BLM lease sale of 2026-09-09/10 (8-K, 0001654954-26-008401). Anyone with money can enter, and larger operators surround
  its acreage (Item 1). Item 1A: "Many of our competitors have substantially greater financial resources".
- *Pricing power and the agony before a rise* **[M2005-020]**: none; oil is "indexed to published posted refinery prices"
  less deductions (Item 1, Marketing). The price is set for it, the case of **[M2012-109]** and **[M2023-079]**.
- *Would the customer choose it over the low bid*: the purchasers buy a barrel at index; Item 1 says there are "a
  substantial number of alternative buyers for its production at comparable prices", which is the commodity's mark.
- *The low-cost position* **[M2018-043]** is the one moat open to a commodity producer **[L2004-007]**; the table shows the
  opposite position, and not narrowing: PEDEVCO's cost per Boe rose from 8.98 (2023) to 11.62 (2025) to 13.72 on direct LOE
  in the first half of 2026, while the gap to the neighbours held.
- *Widening or narrowing* **[M1999-108]**: the mergers added assets whose own cost was $15.09 to $18.63 a Boe and whose
  production fell 18.0% in 2024 (DEFM14C); combined volumes fell from about 8,090 Boe a day in Q1 2026 to 6,801 in Q2 2026
  (10-Q; the Q1 figure is the six-month total less Q2, my subtraction).
- *What could destroy it* **[M2000-014]**: a lower oil price meets the highest-cost barrels first, "One is going to go broke
  at a buck-fifty a pound. And the other one’s going to still be doing fine." **[M2009-059]**; and 89% of the PRB acreage sits
  on federal land, part of it "placed in suspense" by the BLM litigation (Item 1).
- *Ask the competitors* **[M2017-091]**: not possible from the public record beyond their filings, which are the table.

**The field's returns over the cycle, judged in words** (the framework's "ordinary" CONVENTION, no figure). The durable
players in these basins earned positive but uneven results: SM Energy lost money in five of eleven years, Bonanza Creek went
through Chapter 11 in January 2017 (10-K FY2019), Evolution's margins fell to 4% to 9% after FY2023. It is an ordinary field
at best, in which the low-cost operators survive the troughs. That finding alone would be a second route to OUT under the
"standing castle that protects only ordinary returns" item; it is not needed, since PEDEVCO is not among the durable
low-cost players but the high-cost one.

**A change for the better?** The framework credits one only on a full cycle **[M2017-026]**, **[L1995-022]**, and the
mergers are the only candidate. The evidence it would need, a lower cost per barrel, runs the other way: the acquired
assets cost more per Boe than the legacy ones, and the combined direct LOE in 2026 is above every legacy year since 2022.
The operating profit of the first half of 2026 ($22.1M) came with a realized price of about $64.10 a Boe ($86,335 thousand
over 1,347,053 Boe) against $50.27 in 2025 ($45,751 thousand over 910,068 Boe): price, not cost. There is no change in the
cost position to credit, so the change-for-the-better route (TOO HARD (NATURE) with a re-look) does not arise.

**Contrary evidence, answered** **[M1997-127]**: management's "low-cost operating profile" (Item 1) is a claim; the filed
unit costs answer it. The 2026 operating profit is answered above.

**Why OUT and not TOO HARD.** The castle's future is not unjudgeable here; it is shown open on the evidence of nine years of
filed unit costs and eleven years of operating results against three neighbours over a full cycle. "In an unregulated
commodity business, a company must lower its costs to competitive levels or face extinction." **[L1994-035]**; "sooner or
later, the nature of a capitalist society is that the guy with the lower cost comes in and kills you." **[M2001-013]**; and
"you do not want to have something whose competitive position is going to erode over time." **[M2007-117]**. The list of
what Q2 rules OUT names the high-cost producer in a commodity field, on the three rows just quoted.
Price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

**VERDICT: OUT.** A high-cost producer in a commodity field, shown on its own and its basin neighbours' filings over a
full cycle **[M1997-010]**, **[L1994-035]**, **[M2006-004]**, **[M2009-059]**. The file closes here; Q3 to Q12 are NOT REACHED
as clearances. Facts already found for later questions are written under AFTER THE STOP, and the value figures the owner
asks for are computed under COMPUTATION, NOT A CLEARANCE.


## Q3 to Q12: NOT REACHED
The Q2 STOP closed the file OUT. Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are not answered and nothing below is a clearance
(operator rule 2). Q11 belongs to a holding review.

---
## THE BOX
**OUT at Q2**: a high-cost producer in a commodity field, shown open on its own and its basin neighbours' filings over a full
oil cycle (unit production cost 1.5 to 4.2 times Civitas's and SM Energy's in every year 2017 to 2025; operating losses in 8
of 11 years 2015 to 2025 against positive results for the neighbours). **Integrity facts recorded, not judged.** Beneath
the stop, the COMPUTATION shows owner cash negative on the convention's window and a value range and fair price below zero
(central about -15.58 a share all-equity, fair about -11.06 all-equity and -5.46 equity-only) against $13.48; not armed.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged.)* **[M1997-127]**

**Q3 (capital).** Equity of $91.5M to $115.6M in 2021 to 2024 (as last filed, after the restatements) earned operating results of -$1.9M to
+$4.7M in those years, through the 2022 price peak. Capital spending exceeded operating cash after stock pay in 2023 and 2024
by $13.2M and $16.0M (Step 0 table). 49% of proved reserves are undeveloped (Item 1A). The 2026 capital budget is $16M to
$20M (Item 7) against DD&A of $22.6M in the first half of 2026 alone (10-Q), while combined volumes fell from about 8,090 to
6,801 Boe a day between Q1 and Q2 2026.

**Q4 (the numbers).** The ten balance sheets (`tools/run.py`, first-filed XBRL, read against the filed statements named):
shareholders' equity was negative at three year-ends (2014, 2016, 2017; -$37.1M at 2017) and liabilities exceeded assets in
2016 and 2017; the accumulated deficit never turned positive (-$101.7M in 2016, -$138.1M in 2017, -$121.9M in 2025, -$130.0M
at 2026-06-30) while paid-in capital rose to $330.1M (10-Q). At the end of 2018 the company owed $30.2M of subordinated notes
to a related party and $7.7M of other related-party notes (10-K FY2019, 0001654954-20-003503); in 2019 paid-in capital went
from $101.5M to $201.0M and the notes were gone from the balance sheet. Cash was never large ($0.7M to $29.4M). No goodwill.
Receivables rose from $8.0M to $25.7M and payables from $2.6M to $32.4M at the 2025 merger; working capital went from a $6.3M
surplus to a $26.7M deficit (Item 7). The filer **restated FY2022 and FY2023** (depletion overstated; Audit Committee
conclusion of 2025-03-28) and **FY2024** (tax benefit and deferred tax asset overstated by about $5.5M; conclusion of
2025-10-27); disclosure controls and internal control over financial reporting were **not effective** at 2025-12-31, with
material weaknesses in the depletion calculation (extended to the acquired properties) and the tax provision (10-K Items 1A
and 9A). The 10-K features EBITDA and Adjusted EBITDA ($27.0M for 2025) in Item 7, the figure **[M1998-086]** calls "utter
nonsense"; a credit-agreement amendment of 2026-05-05 (8-K, 0001654954-26-004632) redefined covenant EBITDAX to add back
transaction costs and an estimated October 2025 EBITDAX of the acquired companies.

**Q5 (who runs it). Integrity facts.** Control: Juniper Capital Advisors' funds beneficially own 51.6% (proxy,
0001654954-26-006667, through director Edward Geiser) and appoint three of six directors under a shareholder agreement; the
former chairman and chief executive Dr. Simon Kukes and his trust own 33.1%; together 84.7% of the shares. The charter
adopted 2026-02-27 lets both groups "engage in other business ventures, including those that compete with or overlap with
our business" and waives the company's claim to such opportunities, alterable only by a two-thirds vote (8-K
0001654954-26-001835; 10-K Item 1A). The acquired companies paid "affiliate expense" to operating teams ($7.3M in 2024;
DEFM14C) and keep long-term midstream contracts with Roaring Fork Midstream, which Juniper "previously controlled" and in
which it "retains a minority equity interest", stated to be "on arm’s-length terms" (10-K Item 1). Both control groups bought
into the merger financing at $11.00 a share post-split (the Kukes trust $15.4M, a Juniper entity $18.55M; 10-K Item 1). The
chief accounting officer left on 2026-06-23 (8-K 0001654954-26-006257) and the chief executive on 2026-09-21, replaced on an
interim basis by the chief operating officer who ran the acquired companies for Juniper (8-K 0001654954-26-008485); the
departing chief executive's separation pays 2.5 times salary and target bonus with accelerated vesting. The three restatements
and the material weaknesses (Q4) are on the record. The proxy's ten-year legal-proceedings disclosure covers the serving
directors and officers only and reports none. Chief executive pay for 2025 was $2,017,600, of which $1,518,800 in stock
awards, in a year with a net loss of $10.4M (proxy).

**Q6 (the money and the owners).** The mergers of 2025-10-31 cost $179.9M: $115.6M in cash (funded by an $87.0M draw on the
revolver and $35.0M of Series A preferred sold to the PIPE investors) and $64.2M in Series A preferred (10-K Note 6). Paid in
both, the cash part is the larger, so by the framework's definition this is an acquisition, not a merger, and Q6's STOP on an
all-stock deal in undervalued stock does not reach it; recorded only. Shares outstanding went from 4,797,239 to 13,290,902
(+177%) on the preferred's conversion (10-K; 10-Q). An at-the-market programme of $8.0M is open (Item 7). On 2026-08-05,
nine months after buying it, the company agreed to **pay** a buyer $3.8M to take its Pine Haven subsidiary, an acquired
company (10-Q Note 18). No buyback, no dividend.

**Q9 (debt and exposures).** Revolver drawn $85.0M at 2026-06-30 (10-Q) against a borrowing base of $125M redetermined twice
a year (8-K 0001654954-26-005181), maturity 2029-10-31; covenants of net debt to EBITDAX of 3.0 or less and a current ratio
of 1.0 or more; hedges required on 75% of projected proved developed production for 24 months (Item 7); derivative
liabilities $12.8M at 2026-06-30; asset retirement obligations $14.4M; a New Mexico order to reimburse the plugging of about
299 legacy wells at $2.00 a barrel sold, at least $30,000 a month (Item 1); 89% of PRB acreage on federal land, some leases
"placed in suspense" pending the Ninth Circuit (Item 1). Interest paid $2.9M in the first half of 2026.

**Q12.** An oil producer is not among the named businesses; not asked.

## COMPUTATION, NOT A CLEARANCE
*(Beneath the Q2 STOP. Q7's construction as its text and Part VII state, for the owner's two reporting figures; no entry
language; nothing here reopens the box. Script and output: `Test Runs/_research 2026-10-16 PED/q7_computation.py`.)*

**Inputs.** Owner cash after every real cost from the Step 0 table, FY2021 to FY2025, before interest for the all-equity
basis (cash interest $590 thousand in 2025, nil before) and after the company's own tax (none paid; the series is negative,
so the statutory-rate treatment of the carryforward shelter has nothing to tax and adds nothing; said so). Sovereign 5.43%.
Net debt $75.5M: revolver $85.0M less cash $10.8M at 2026-06-30 (restricted cash $1.3M left out), plus the $3.8M Pine Haven
payment and less the $2.5M Weld County proceeds, the two subsequent events the 10-Q states (Note 18); operating leases and
derivative liabilities left out, said so. Whether the $2.5M overlaps the $2.0M deposit already in cash was not resolved (a
$0.15 a share question). Shares 13,290,902.

**The specifics, applied.** The mergers: cash $115.6M against preferred $64.2M, so classed by the larger part as an
**acquisition** (the framework's "Which deals are mergers"), capital spending for the range. **The serial-acquirer test:**
net purchases over the window ($115.6M) exceed half of owner cash before purchases (which is negative), so the **central
figure is the organic pair** (purchases left out; the filer reports no organic growth rate, so the series' own) with the
default pair beside. **(b) Decline:** the series changes sign (first half of the window $1.19M a year, second half -$12.46M,
before interest), so the growth is meaningless and **the range is the no-growth case alone**, said so. **(a) Cycle base:**
2025 carries $7.5M of merger costs the filer itself sets apart (Item 7); shown beside with them added back. **(d) Working
capital** is inside the operating cash used. **(e) Maintenance:** the filing gives no maintenance figure for the legacy window;
the depreciation charge is shown beside as the proxy the rows allow, "not inappropriate in most companies to use as a proxy
for required capital expenditures" **[M1998-127]**. **(f) Cap:** not reached; no growth is carried. The literal window is the
central series itself.

| Case (USD thousands a year; per share after net debt) | owner cash | value at 5.43% | fair at 10% |
|---|---|---|---|
| **CENTRAL, organic pair, no growth, all-equity** | -7,145 | **-15.58** | **-11.06** |
| Equity-only beside (owner cash after interest, against the market value) | -7,263 | -10.06 | -5.46 |
| Default pair beside (merger cash deducted in 2025) | -30,275 | -47.63 | -28.46 |
| 2025 merger costs added back (a) | -5,654 | -13.51 | -9.93 |
| Depreciation variant, maintenance proxy (e) | -714 | -6.67 | -6.22 |
| Combined companies 2023-2025 (CONVENTION of this run, below) | -2,948 | -9.77 | -7.90 |

**Floor tested first.** No case of the range earns the floor at $13.48; every case is below zero. By Q7's convention the
file would close **OUT** here too, before the width test. Market value $179.2M; with net debt, $254.7M.

**The two reporting figures (a reporting convention, not a verdict):**
- **(a) VALUE RANGE: about -$15.58 a share at both ends** (the no-growth case alone, all-equity basis, central); equity-only
  about -$10.06; against **$13.48**.
- **(b) FAIR PRICE: about -$11.06 a share all-equity (central), -$5.46 equity-only**, the price at which the range's midpoint
  earns ten percent after the company's own tax. Not positive on any case of the convention, so no price makes the midpoint
  earn the floor. Under the serial-acquirer rule the alert would sit on the organic pair, which is the central figure and is
  not positive: **no alert is armed** (there is no positive price to arm it at).

**CONVENTION of this run (the combined companies).** The text values a merger inside the window on the combined companies'
averages but classes this deal an acquisition, and gives no rule for an acquisition that changes the size of the business at
the window's last edge; the organic pair then values a company about a third the size of the one priced. Rationale: to show
what the bought business's own record adds, the acquired companies' filed cash flows (operating cash plus interest paid less
investing, 2023, 2024, nine months of 2025; DEFM14C; no stock pay disclosed, flagged) are added to the legacy series for the
three years both exist. The mean stays negative (combined -$31.7M, +$22.1M, +$0.7M). Beside only; it decides nothing.

**Contrary evidence, computed and written down** **[M1997-127]**: the first half of 2026, doubled, gives owner cash before
interest of about **$32.2M a year after a depreciation charge** (operating cash before working-capital changes $36.7M, less
stock pay $0.9M and DD&A $22.6M, plus cash interest $2.9M) and about $41.4M on cash capital spending; on the enterprise value
that is 12.7% and 16.3%, and it would put a "fair" figure near $18.56 a share (depreciation basis) against the price. It is
**not the convention's figure** and is not a case of the range: one half-year, at a realized $64.09 a Boe lifted by the 2026
price spike that Item 1A describes, with volumes falling about 16% from Q1 to Q2 and capital spending incurred well below the
depreciation charge. It is the only arithmetic in the record that makes the price look low, and it rests on the oil price,
which the rows do not forecast: "If you own oil, you should only own oil, if you expect these prices to go up significantly."
**[M2020-035]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `4108301b`); written question by question; committed after each
      (Q1 `666fa632`, Q2 `7fb5620a`, this close in the next commit).
- [x] Dispatched: the brief allowed per-question pathspec commits of this file and the research folder only; the lock is
      the dispatching session's and was not touched. The fold is the dispatcher's (operator rule ten).
- [x] No other run file, holding review, `PORTFOLIO.md`, resume-state file, queue or reading list was opened, listed or
      searched; the one filtered directory listing of `Test Runs/` and the session context are declared under contamination.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row (check script
      `Test Runs/_research 2026-10-16 PED/check_citations.py`, PASS); every filing fact carries its accession.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the value figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost, recast by hand from the filed cash-flow statements, never a net-income proxy
      (operator rule 5); `tools/run.py`'s owner-earnings columns were found wrong for this filer and not used; sovereign
      from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations; Q2; the computation's run-rate paragraph); integrity facts under
      AFTER THE STOP and flagged in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded in the commit message).
- Honest limits: the competitor costs are each filer's own definition, not one definition; 2021's capital spending nets an
  inferred property-sale figure; the 2022 depletion is as first filed (restated lower, not read); the acquired companies'
  series lacks stock pay; Continental Resources' filing status not checked; the counterparty of the acquired companies'
  "affiliate expense" was not identified beyond the information statement's words.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **A transforming acquisition at the window's edge.** The mergers closed two months before the window ended,
were paid more in cash than in shares (so an acquisition, not a merger, by the 2026-10-12 definition), and tripled the
business. The specifics then make the organic pair central (the serial-acquirer test fires whenever owner cash before
purchases is negative, since any purchase exceeds half of a negative number) and value a business about a third the size of
the one the price buys; the merger rule that would use the combined averages is closed off by the cash-versus-shares
classification. I showed the combined companies beside under a CONVENTION of this run; the text should say how an acquisition
that dwarfs the acquirer is valued, and whether the serial-acquirer test is meant to fire when owner cash before purchases is
negative. (2) **The competitor row when the Competition section names no one.** The brief's fallback (choose basin producers
as a CONVENTION) assumes no company is named anywhere; this filing names its basin operators and partners as offset operators,
not as competitors. I treated them as the named rivals and said so; the template could say whether "named" means named as a
competitor or named in the same basin. (3) **Unit-cost definitions differ across filers** (PEDEVCO excludes workovers and
taxes, Civitas includes midstream opex, SM separates transport). The commodity paragraph says to read the cost position "from
its own and its operators' filings" but gives no rule for comparing unlike definitions; here the gap (1.5 to 4.2 times) was
wider than any definitional difference, but a closer case would need one. Also noted: `tools/run.py` took a vehicle-purchase
tag as capital spending for a filer whose spending is tagged as drilling and completion costs, which overstated its
capex-basis owner earnings by about $17M to $35M a year in its three-year table.
