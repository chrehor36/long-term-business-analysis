# Company Run — Texas Instruments Incorporated (Nasdaq: TXN) — 2026-10-11
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-11, after the run was committed: not held (`PORTFOLIO.md` names TXN only in the opportunity set, from a v4.1 run; no account holds it).*

**Dispatched run.** Written by a dispatched analyst under the canonical brief `Screens/_daily/_dispatch_brief.md`, with
the one departure the brief states (the lines of evidence derived by the analyst from the 10-K, not hand-written by the
dispatcher). The lock in `Screens/_daily/` was present when the run began (written by the dispatcher, not by this analyst).

**Contamination declared.** A directory listing of `Test Runs/`, made only to check whether a file of this date existed
before copying the template, showed the names of three other run files of 2026-10-11 (SHOP, SPGI, TECH) and their
research folders. The session context also showed commit subjects about the TECH run. None was opened, read or used.
Nothing about this company from any other run, holding review, `PORTFOLIO.md` or the register was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $283.74 (close 2026-10-09, the last trading day before the run; printed by `tools/run.py` from an
  aggregator, **flagged as an aggregator quote, live quote only**, operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $1 par, **913,247,686** shares as of
  2026-07-15 (Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-24, accession `0000097476-26-000152`;
  `python Screens/cover_shares.py TXN`). Cross-check: shares issued 1,741 million less treasury 828 million = 913 million
  at 2026-06-30 on the same 10-Q's balance sheet; the 8-Ks filed after that 10-Q (2026-09-17, a planned dividend
  increase, accession `0000950103-26-014118`) change no count, and no prospectus was filed after it.
- **Market cap:** $259,125M (913.248M x $283.74).
- **Sovereign for the earnings currency (USD):** 5.60%, the US Treasury daily par yield curve, 30-year, 2026-10-09
  (issuing authority; printed by `tools/run.py` from `tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K for 2025, filed 2026-02-06, accession `0000097476-26-000059` (Items 1, 1A, 5, 7, 7A, 8 with notes 2, 4, 10, 11).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-07-24, accession `0000097476-26-000152`; 10-Q for the quarter ended
    2026-03-31, accession `0000097476-26-000101` (fetched; the June 10-Q supersedes it for the balance sheet).
  - Proxy (DEF 14A) filed 2026-03-04, accession `0000097476-26-000078` (governance, compensation discussion, tables).
  - 8-Ks: 2026-02-04 (Silicon Labs agreement, Exhibits 99.1 and 99.2, accession `0001193125-26-036727`); 2026-07-22
    (second-quarter release, Exhibit 99, accession `0000097476-26-000148`); 2026-06-02 (CFO succession, accession
    `0000950103-26-008325`); 2026-03-25 (an SVP's retirement, accession `0001193125-26-124057`); 2025-10-16 (executive
    chairman's retirement, the CEO named chairman, accession `0000950103-25-013275`); 2026-09-17 and 2025-09-18 (dividend
    increases, accessions `0000950103-26-014118`, `0000097476-25-000048`).
  - The filings that cover the last cycle: 10-Ks for 2019 (`0000097476-20-000009`), 2021 (`0000097476-22-000009`), 2022
    (`0000097476-23-000007`), 2023 (`0000097476-24-000007`), 2024 (`0000097476-25-000007`), read for the cycle wording;
    the 2014 to 2025 annual series from the SEC's XBRL company facts (transcription, checked against the 2025 statements).
  - Silicon Labs (the pending acquisition): 10-K for fiscal 2025 (year ended 2026-01-03), accession
    `0001038074-26-000005`, cash-flow statement.
  - Competitors, from their own XBRL company facts: Analog Devices (CIK 6281), Microchip Technology (CIK 827054), NXP
    Semiconductors (CIK 1413447).
- **One figure cross-checked against the filed statement:** cash flows from operating activities for 2025, **$7,153M**,
  on the filed Consolidated Statements of Cash Flows of the 2025 10-K, equals the `tools/run.py` line (7,153) and the
  MD&A's non-GAAP reconciliation (7,153). Depreciation for 2025, $1,918M, likewise agrees.
- `python tools/run.py TXN` arithmetic lines only (its output is kept at `Test Runs/_research 2026-10-11 TXN/runpy_output.txt`):
  owner cash (OCF less stock pay less capital spending) 2023 $987M, 2024 $1,111M, 2025 $2,184M; on the depreciation basis
  $4,883M, $4,423M, $4,816M; five-year window 2021 to 2025: $3,196M capex basis, $5,851M depreciation basis; stock pay
  2023 to 2025 $362M, $387M, $419M (complete; one tag, `ShareBasedCompensation`); no securities purchases inside
  operating cash, no other stock-pay line, no intangible, software or mine payment beside capital spending. Nothing the
  tool prints as a rule, an id or a verdict was read (Part VII, the tooling).

**The lines of evidence this run chose, and why** (the brief's departure: derived from the 10-K by the analyst).
1. **The semiconductor cycle** (Item 1, "Semiconductor cycle"; Item 7, "Macroeconomic factors": in 2025 "global
   semiconductor shipments remain at levels below the prior peak"; the 2022 10-K: "After a sustained period of growth, a
   market correction began in 2022."). Owner cash must be read over a full cycle, not five years that start near a peak.
2. **The six-year elevated capital-spending cycle** (Item 1: "about $24 billion to capital expenditures" over 2016 to
   2025, "near completion of our six-year elevated capital expenditures cycle"; Item 7: $2 billion to $3 billion expected
   in 2026). This decides the maintenance guess, the return on the added capital (Q3) and the cash input (Q7).
3. **The CHIPS Act incentives** (note 2 and the cash-flow supplement: an investment tax credit and direct funding that
   reduce the carrying amount of the fabs and their depreciation; $3.35 billion of receivables at year-end 2025). They
   bear on whose tax (Q7), on the true depreciation (Q4) and on net debt.
4. **Competition, including China** (Item 1A: "intense technological and pricing competition", competitors in Asia,
   China "actively promoting and reshaping its domestic semiconductor industry"; about 50% of 2025 revenue shipped into
   China and about 20% from customers headquartered there). The castle question (Q2).
5. **The manufacturing cost claim** (Item 1: a 300mm chip "costs about 40% less" than a 200mm one; "most of our
   manufacturing in-house"). The low-cost-producer test (Q2), checked against the gross margins of the field.
6. **Fixed costs and margins** (Item 1A, "Our margins vary": "a significant portion of our operating costs is fixed").
7. **The capital-return policy and the debt** (Item 1 and the deal release: return "100% of free cash flow to
   shareholders over time"; long-term debt $3.6 billion in 2016 to $14.0 billion in 2025). Q6 and Q9.
8. **The pending Silicon Labs acquisition and its financing** (8-K of 2026-02-04; 10-Q: a $5 billion 364-day delayed-draw
   term loan entered in June 2026, undrawn, conditioned on the closing). Q6 and Q7 (valued beside, not in the central
   figure).
9. **The inventory strategy** (Item 1, "build ahead of demand"; 222 days of inventory at year-end 2025, 196 at 2026-06-30).
   Working capital in owner cash (Q7, specific (d)).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the owner would be content to hold this "if the market closed for five years"
**[M1997-109]**, valued on what the asset itself produces, "Not by selling it to somebody else" **[M1997-052]**. The market
serves and does not instruct **[M2006-077]**: the price of $283.74 is read only against the value the filings support. The
margin of safety is an attitude here and arithmetic only at Q7 **[M1996-084]**. No macro forecast enters
**[M2000-094]**: the trade, tariff and China questions in Item 1A enter only as properties of the castle (Q2), never as a
forecast. Who is paid to tell you **[M2020-037]**: the company's featured measure, "free cash flow", adds CHIPS Act
proceeds to operating cash less capital spending, and the deal release calls the purchase "accretive" to earnings per
share "excluding transaction-related costs"; both are read as the seller's description, not as the analyst's figure:
"don’t ask the barber whether you need a haircut" **[M2011-083]**. The analyst's habits: "What do I not know that I need to know?" **[M1999-129]**, and the worst anchor
"is always your previous conclusion" **[M2016-054]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Item 1A: "intense technological and pricing competition", competitors "particularly in Asia", and China promoting its
   own industry, while about 50% of revenue is shipped into China (10-K 2025).
2. Gross margin fell from 68.8% (2022) to 57.0% (2025) while the 300mm "structural cost advantage" was being built; in
   2025 TI's gross margin (57.0%) sat below Analog Devices' (61.5%), the rival whose margins this run compares (Q2).
3. Tangible capital employed rose from about $5.4 billion (2018) to $17.5 billion (2025) while after-tax operating profit
   went from $5.6 billion to $5.3 billion (Q3 table): the added capital has so far earned nothing that the accounts show.
4. Dividends ($5.0 billion in 2025) exceeded the company's own free cash flow ($2.9 billion) in 2025, and in 2023 and 2024
   as well, while long-term debt rose to $14.0 billion (10-K 2025, 2024, 2023 cash-flow statements).
5. Embedded Processing's operating margin fell to 11.3% in 2025 (13.9% in 2024) under the cost of the LFAB fab (10-K 2025).
6. The company gives quarterly revenue and earnings-per-share guidance ranges (8-K of 2026-07-22, Exhibit 99).
7. The Silicon Labs target has negative owner cash over its last four fiscal years (Q7, beside), at an enterprise value of
   about $7.5 billion, paid in cash.
8. *(found while reading the proxy for Q5)* A shareholder proposal printed in the 2026 proxy states that "In September,
   China’s Ministry of Commerce launched an anti-dumping investigation targeting U.S. chipmakers, including Texas
   Instruments" (DEF 14A `0000097476-26-000078`, the proponent's text, not the company's). A text search for "dumping" in
   the 2025 10-K and the two 2026 10-Qs found no instance; the company's own risk factor speaks only generally of
   "administrative measures". Not verified from a primary Chinese source. Found after Q2 had closed; it bears on Q2 test 11
   (the threat from China) and adds to that test's weight against without changing its verdict; recorded and weighed at Q5.

## THE STANDING RULE
Owning this share, bought with the buyer's own money and not on borrowed money, puts nothing at risk of ruin: the rule
binds the buyer's conduct, "never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**, and "the use of borrowed money can destroy the decent returns that a life-long owner of equities would
otherwise enjoy" **[L2014-005]**. Nothing in this run reaches a purchase, so no sizing arises.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**, not
knowledge of the product **[M2000-104]**: "What is important is that I understand the economic dynamics of the industry"
**[M2011-014]**.

**The key variables, and whether they are foreseeable** **[M1998-044]**:
1. *Volume over the cycle.* Revenue was $13.0 billion in 2014 and 2015, $15.8 billion at the 2018 peak, $14.4 billion in
   2019, $20.0 billion at the 2022 peak, $15.6 billion at the 2024 trough, $17.7 billion in 2025 and $19.5 billion for
   the twelve months to 2026-06-30 (10-K 2025; 10-Q `0000097476-26-000152`, non-GAAP reconciliation table). Compound growth
   2015 to 2025 is 3.1% a year, with falls of 9% (2019), 13% (2023) and 11% (2024). The cycle is large but its shape
   repeats, and the filer describes it the same way in every 10-K read (2019 to 2025, Item 1, "Semiconductor cycle").
2. *Product life.* The filer states that "New products do not tend to have a significant impact on our revenue in any given
   period because we sell such a large number of products" (10-K 2025, Item 7), more than 80,000 products to more than
   100,000 customers, with "about half of our revenue derived from customers outside of our largest 50" (Item 1); the
   2019 10-K adds that industrial and automotive markets "benefit from long product life cycles". Embedded customers
   "often invest their own R&D to develop software that operates on our products", which lengthens relationships (Item 1).
   The economics do not turn on winning the next product generation, which separates this business from the
   "fast-moving technology" of **[L1993-023]**.
3. *The cost position against rivals.* A margin record is on file for the whole span (Q2), so this variable can be read.
4. *China.* About 50% of revenue shipped into China, about 20% from China-headquartered customers, and a state-backed
   domestic industry (Item 1A). This is the variable least foreseeable; it is a threat to the castle and is weighed at
   Q2 test 11 **[M2000-014]**, not a reason the economics cannot be pictured at all.

**Would the insiders write it down?** **[M2000-105]**. The filer does: a long-term capacity plan "to meet demand over
time", the expectation that semiconductor content in industrial, automotive and data-center equipment "is expected to
continue well into the future", and a ten-year allocation record (Item 1). That is a forecast of customers' design and
purchase behaviour across 100,000 accounts, the kind of forecast **[M2017-019]** and **[M2023-030]** put inside the
analysable class, not a bet on which technology wins.

**Do the past statements tell me the future ones?** **[M2008-033]**. Mostly yes: operating margins 30% to 51% across
2014 to 2025, every year profitable, the same two segments throughout. The one break is capital intensity (capital
spending 3% to 7% of revenue 2014 to 2020, 13% to 31% from 2021 to 2025), which the filer explains and says is ending
(Item 1, Item 7). How far off could I be **[M2011-084]**: far off on the cycle's timing and on China, narrowly on whether
TI will still be selling analog and embedded chips into industrial and automotive equipment in ten years.

**Routing.** Not a bank or financial institution; not a holding company. The parts: Analog 79% of 2025 revenue and $5.41
billion of $6.02 billion operating profit (more than half: it decides under the parts convention); Embedded Processing 15%;
Other 6% (10-K 2025, segment results). Both reported segments are understood by the same tests.

**The doubt rule** **[M2002-092]**. The doubt that exists is about the castle's width against Chinese rivals and about what
the new fabs will earn, both judged at Q2 and Q3 on the evidence; it is not a doubt about whether the business's
economics can be pictured. A technological component that "could hurt the business as it presently exists" **[M1998-008]**
was looked for: the 10-K's own risk factor on "Rapid technological change" is generic, and the filer's statement that new
products do not move revenue in any period answers it for this business.

- **VERDICT: IN.** The economics are those of a broad, cyclical, slowly growing supplier of long-lived analog and embedded
  chips whose key variables (cycle-average volume, cost position, China share) can be named and read from its filings
  **[M1998-044]**, **[M2012-065]**, **[M2011-014]**. Doubt about the castle is carried to Q2, where it belongs.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. A moat is what "protects excellent
returns on invested capital" **[L2007-004]**.

**The castle tests, each with its filing fact.**
1. *The key factors and how permanent they are* **[M1995-038]**. The filer names four: in-house manufacturing and
   process technology, a broad portfolio (more than 80,000 products), the reach of its channels (more than 80% of 2025
   revenue sold direct, including TI.com), and "diversity and longevity of our products, markets and customer positions"
   (10-K 2025, Item 1). The record behind them: operating margins every year from 30.3% (2014) to 50.6% (2022), never a
   loss year, after-tax returns on tangible capital of 60% to 105% a year from 2014 to 2022 (Q3 table). Breadth and
   longevity are permanent in kind: they were built over decades and are not undone by one product cycle.
2. *Would it stand without the lord?* **[M1996-037]**, **[M1999-106]**. Yes on the evidence: a business of 80,000 small
   products and 100,000 customers turns on no single decision; the chief executive changed in 2023 and the executive
   chairman retired at the end of 2025 (8-K `0000950103-25-013275`) with no break in the way the business is described or
   run.
3. *The money test* **[M2011-015]**. A well-funded attacker exists and is named by the filer: "China actively promoting
   and reshaping its domestic semiconductor industry through policy changes and investment" (Item 1A). What it must
   overcome is breadth, not one product: to take TI's position it must be designed into tens of thousands of products at
   tens of thousands of customers, where embedded customers' own software "tends to increase the length of our customer
   relationships" (Item 1). Microchip's own 10-K (fiscal 2026, accession `0000827054-26-000016`) describes the same
   threat to itself: Chinese government "assistance financial or otherwise, to some of our competitors, or to new
   entrants", and competitors that "copied, cloned, pirated or reverse engineered" its lines in China and Taiwan. One
   competitor "is frequently enough to ruin a business" **[M2012-108]**. Written down as contrary evidence; the filings
   show no collapse: revenue from China-headquartered customers is "about 20%" in each of the 2023, 2024 and 2025 10-Ks,
   and revenue rose 13% in 2025 and 23% in the second quarter of 2026 (10-Q).
4. *Pricing power and the agony before a rise* **[M2005-020]**. No price series is filed. The filer says changes in its
   revenue "are attributable to changes in customer demand, which are evidenced by fluctuations in shipment volumes"
   (Item 7), and Item 1A speaks of "pricing pressures". No instance found in the filings read of a price rise or of price
   erosion at TI; Microchip's 10-K says the industry "has historically been characterized by price erosion". The test is
   not passed on evidence; it is not failed either. Near-monopoly pricing power **[M2010-092]** is absent in a field the
   filer calls "highly fragmented".
5. *Unit volume.* Shipment volume drives revenue (Item 7). Volume over the cycle: revenue up 3.1% a year from 2015 to 2025,
   organically; the 2026 proxy notes TI's 2023 to 2025 revenue growth fell below the peer median while "the median growth
   rate of Semiconductor Peers includes the benefit of acquisitions, whereas TI’s growth rate is entirely organic"
   (DEF 14A `0000097476-26-000078`).
6. *The low-cost position* **[M2018-043]**, **[L2000-017]**, **[M1997-010]**. The filer's claim: a 300mm chip "costs about
   40% less" (Item 1). The field's record (competitor row below): TI's operating margin averaged 39.5% over 2014 to 2025
   against 26.5% (Analog Devices), 18.9% (Microchip) and 20.4% (NXP); but TI's gross margin averaged 62.4% against Analog
   Devices' 63.6%, and in 2025 it was 57.0% against Analog Devices' 61.5%. The advantage on file is in operating cost and
   in the absence of acquisition charges, not (yet) in the cost of goods; the 300mm cost claim is not visible in the
   gross margin while the new fabs are under-loaded (Item 7: "When factory loadings decrease [...] our profit margins
   decrease"). The low-cost operator "must pursue an unrelenting foot-to-the-floor strategy" **[L2004-007]**; the six-year
   capital programme is that strategy, and whether it buys the cost lead is Q3's question.
7. *The brand in the customer's mind* **[M2015-038]**. Not the castle here: the customer is an engineer choosing a part.
8. *Would the customer still choose it over the low bid?* **[M2017-009]**, **[M1997-102]**. The design-in and software
   reuse (Item 1) make a part, once chosen, hard to replace for the life of the customer's product; at the next design the
   low bid competes again. The filer's own 2024 10-K: "Over time, we have gained market share in Analog and Embedded
   Processing" (a claim, unquantified).
9. *Ask the competitors* **[M2017-091]**, **[M1998-145]**. From the public record: NXP's 10-K for 2025 (accession
   `0001413447-26-000008`) names "Texas Instruments Inc." among its "primary key public competitors"; Analog Devices' 10-K
   (`0000006281-25-000153`) and Microchip's name no rival. TI's proxy names its own "Semiconductor Peers", "suppliers that
   operate in our key markets or offer technology that competes with our products".
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**, **[M2000-075]**. Mixed on the evidence. For: the share claim
    above; Analog's operating margin back to 43.8% in the first half of 2026 (38.0% a year earlier, 10-Q). Against:
    gross margin from 68.8% (2022) to 57.0% (2025); Embedded Processing's margin from 38.5% (2021) to 11.3% (2025), its
    revenue from $3.37 billion (2023) to $2.70 billion (2025) (10-Ks 2021, 2023, 2025).
11. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. Chinese domestic rivals backed by
    the state, and trade measures that could "cause customers to seek alternate suppliers" (Item 1A), against about half
    of revenue shipped into China. This is the threat the run cannot size; it is the strongest evidence against the business.

**The competitor row** (same metrics from the competitors' own filings, XBRL company facts, GAAP; the rivals' operating
margins carry heavy amortization of acquired intangibles, TI's carry none since 2022, so the gap overstates the operating
difference; Microchip's capital-spending tag reads near zero for 2015 to 2017 and is not used).

| | span | operating margin, average (low to high) | gross margin, average | 2025 operating / gross | growth route |
|---|---|---|---|---|---|
| Texas Instruments (CIK 97476) | 2014 to 2025 | 39.5% (30.3% to 50.6%) | 62.4% | 34.1% / 57.0% | organic |
| Analog Devices (CIK 6281) | FY2014 to FY2025 | 26.5% (21.6% to 31.1%) | 63.6% | 26.6% / 61.5% | Linear, Maxim acquisitions |
| Microchip (CIK 827054) | FY2015 to FY2026 (March years) | 18.9% (6.7% to 36.9%) | 59.6% | 10.4% / 57.7% (FY2026) | Atmel, Microsemi acquisitions |
| NXP (CIK 1413447) | 2014 to 2025 | 20.4% (-1.6% to 33.0%) | 51.5% | 24.8% / 54.7% | Freescale merger |

**Named rivals that do not file with the SEC, flagged:** the 10-K for 2025 names no competitor ("dozens of large and small
companies, including both broad-based and niche suppliers", Item 1); the proxy's peer list names Infineon Technologies and
Renesas Electronics, which do not file with the SEC, and STMicroelectronics, which files a 20-F; none was read. The
rivals compared were taken from the proxy's list as the filer's own naming of companies that "compete with our products",
since the 10-K names none (stated under What in the framework was wrong or unclear).

**The parts table** (five-year operating profit 2021 to 2025, segment results in the 10-Ks for 2021, 2023, 2025; Other
includes restructuring and corporate items).

| part | five-year operating profit | share | castle | decides |
|---|---|---|---|---|
| Analog | $31,593M | 83% | standing (tests 1 to 6, the margin record) | yes, more than half |
| Embedded Processing | $4,091M | 11% | in doubt: margin 38.5% to 11.3% and revenue falling 2023 to 2025 | no |
| Other (DLP, calculators, custom ASICs) | $2,235M | 6% | not judged | no |

Embedded Processing does not decide; under the parts convention it is carried to Q7 as an ordinary business at no growth.

**The field's returns over the last full cycle.** TI's own: after-tax operating returns on tangible capital of 90% to 105%
across 2018 to 2022 and still 30% in 2025 (Q3 table); the rivals' GAAP operating margins of 19% to 27% on average, after
acquisition charges. These are not ordinary returns; the "ordinary returns" exclusion does not apply.

**Change for the better.** None is credited; no re-look condition arises.

- **VERDICT: IN.** The castle is standing on the record: excellent returns across two full cycles **[L2007-004]**, built on
  breadth, design-in and in-house manufacturing that do not depend on the lord **[M1995-038]**, **[M1996-037]**. It is not
  shown on the evidence to be filling in: revenue from China-headquartered customers held at about a fifth through 2023 to
  2025 and revenue is recovering. The threat from a state-backed domestic industry is real and not sizeable from the
  filings **[M2000-014]**, **[M2012-108]**; it is written down as the strongest evidence against and carried into the
  certainty of Q7 rather than closing the file here. The gross-margin record does not yet show the claimed cost lead.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The measure is the return on the capital the business needs, not on a purchase price **[M2010-090]**, read as "return on
tangible assets" **[M2011-060]**, and of any added capital "whether that’s good or bad depends on what we earn on that
incremental $130 million over time" **[M2001-019]**.

**Return on the capital actually needed** (tangible capital = net property, plant and equipment + receivables +
inventory - payables - accrued compensation, year-end; after-tax operating profit at the year's effective tax rate;
10-K statements via XBRL; script `Test Runs/_research 2026-10-11 TXN/scripts/rotc.py`):

| year | revenue $M | operating margin | tangible capital $M | after-tax operating profit $M | return |
|---|---|---|---|---|---|
| 2014 | 13,045 | 30.3% | 4,782 | 2,874 | 60% |
| 2016 | 13,370 | 36.3% | 4,463 | 3,540 | 79% |
| 2018 | 15,784 | 42.5% | 5,405 | 5,603 | 104% |
| 2020 | 14,461 | 40.8% | 5,456 | 5,481 | 100% |
| 2021 | 18,344 | 48.8% | 7,406 | 7,805 | 105% |
| 2022 | 20,028 | 50.6% | 9,878 | 8,843 | 90% |
| 2023 | 17,519 | 41.8% | 14,147 | 6,434 | 45% |
| 2024 | 15,641 | 34.9% | 15,934 | 4,810 | 30% |
| 2025 | 17,682 | 34.1% | 17,502 | 5,275 | 30% |

The property figure is net of $4.51 billion of CHIPS Act incentives that "reduced the carrying amounts of manufacturing
assets" (10-K 2025, note 2), so the capital actually put in is larger than the table shows, and the true 2025 return
lower. The high reported return before 2021 is not a cyclical peak artefact (2016 and 2020 were not peaks), nor leverage
**[L1994-009]**: it is the return on tangible operating capital, before financing.

**Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending was $385M to $1,131M a year
from 2014 to 2020 (3% to 7% of revenue), when depreciation ran $539M to $850M; from 2021 to 2025 it was $2.46 billion,
$2.80 billion, $5.07 billion, $4.82 billion and $4.55 billion, "about $24 billion" over 2016 to 2025 by the filer's count,
"to support future revenue growth" (Item 1). The filer calls it a "six-year elevated capital expenditures cycle" that is
"nearing the end", with $2 billion to $3 billion expected in 2026 (Item 7; repeated in the June 2026 10-Q). The
maintenance guess the filing allows: depreciation, which the rows accept as a proxy in most companies **[M1998-127]**,
taken gross of the CHIPS reduction because the replacement fabs will not carry the credit: $1,918M + $353M = $2,271M for
2025, rising as the new fabs come into service. Inventory doubled from $2.0 billion (2020) to $4.8 billion (2025) by a
stated strategy to "build ahead of demand"; that is working capital the business now needs.

**The growth arithmetic** **[M2001-019]**, **[M2023-081]**. Tangible capital rose by about $12.1 billion between 2018 and
2025 (before the CHIPS reduction), while after-tax operating profit went from $5.6 billion to $5.3 billion. Against the
2022 peak the comparison is worse; against the twelve months to 2026-06-30 (operating profit about $7.25 billion before
tax, 10-K 2025 less the first half of 2025 plus the first half of 2026) it is better but still well short of the earlier
return on the earlier capital. So far: "We just put way more capital into the business" **[M2023-081]**. The capacity is
said to be built ahead of demand, so its return is not yet knowable; the best businesses do not "generate lots of
opportunities to earn high returns on incremental capital" **[M2003-120]**, and this one has not yet shown that it has.
The capital-heavy second best is acceptable only on "decent returns on the incremental sums they invest" **[L2009-012]**;
the evidence for that is not yet on file.

- **WEIGHS AGAINST**, for now: a business that earned very high returns on little capital **[M1998-081]** has become a
  capital-heavy one whose added $12 billion or more has not yet earned anything the accounts show **[M2023-081]**,
  **[L2009-012]**. The base business's returns weigh for it; the added capital's undemonstrated return weighs against.
  (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (`tools/run.py` table, first-filed
XBRL vintage, read against the filed balance sheets of the 2025 10-K and the June 2026 10-Q; $M):

| year-end | equity | cash | receivables | inventory | goodwill | intangibles | net PP&E | long-term debt (incl. current) | retained | treasury stock |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 10,473 | 1,154 | 1,267 | 1,790 | 4,362 | 1,264 | 2,512 | 3,609 | 33,107 | 25,523 |
| 2018 | 8,994 | 2,438 | 1,207 | 2,217 | 4,362 | 628 | 3,183 | 5,068 | 37,906 | 32,130 |
| 2020 | 9,187 | 3,107 | 1,414 | 1,955 | 4,362 | 152 | 3,269 | 6,798 | 42,051 | 36,578 |
| 2022 | 14,577 | 3,050 | 1,895 | 2,757 | 4,362 | - | 6,876 | 8,735 | 50,353 | 40,214 |
| 2024 | 16,903 | 3,200 | 1,719 | 4,527 | 4,362 | - | 11,347 | 13,596 | 52,262 | 40,895 |
| 2025 | 16,273 | 3,225 | 1,963 | 4,804 | 4,330 | - | 12,320 | 14,048 | 52,236 | 42,130 |
| 2026-06-30 | 18,007 | 3,660 | 2,520 | 4,605 | 4,330 | - | 11,911 | 14,052 | 53,161 | 41,941 |

(Short-term investments beside cash: $2,336M in 2016, $4,380M in 2024, $1,656M in 2025, $3,341M at 2026-06-30. The
odd years 2017, 2019, 2021, 2023 are in the tool's table and move between their neighbours.)

**What the figures say.** (1) Goodwill is the 2011 National Semiconductor purchase, unchanged for a decade but for a $32M
impairment in 2025; acquired intangibles amortized to nothing by 2021; no purchase since, so no merger reserve or big
bath is on the books. (2) Receivables track revenue (40 days of sales in 2025, 39 in 2024, 42 at June 2026): no build.
(3) Inventory went from 1,790 to 4,804 while revenue went from $13.4 billion to $17.7 billion; the filer explains it as
a strategy to "build ahead of demand" with products of "low risk of obsolescence", gives days of inventory each quarter
(241 at end-2024, 222 at end-2025, 196 at June 2026), and the figure is now falling. Inventories "out of line" with sales
**[M1995-064]** is what this looks like on the face, so it was read: the build is disclosed, explained and reversing; it
is a cost in working capital (Q7), not a tell. (4) Prepaid expenses and other long-term assets rose because of CHIPS Act
receivables ($904M current and $2,246M long-term at end-2024, $1,709M and $1,639M at end-2025, $1,005M and $1,158M at June
2026, note 11 and the 10-Q): a "prepaid" build **[M1995-064]**, again read: they are government incentives earned on fab
spending, disclosed in amount, and $1.40 billion of them came in as cash in the first half of 2026 (10-Q cash-flow
supplement). (5) Debt rose from $3.6 billion to $14.1 billion while equity barely moved and treasury stock rose $16.6
billion: the owners were paid out partly with borrowed money (Q6, Q9). (6) What the figures do not say: what the new fabs
will earn; the balance sheet shows the capital, not its return.

**The real costs** **[L2021-003]**:
- *Depreciation* **[R1996-023]**, **[L2015-004]**: real, and understated by the accounting for incentives, which "reduce
  depreciation expense over the useful lives of the assets" ($353M in 2025, $159M in 2024, $45M in 2023, note 2). Owner
  cash in Q7 adds it back to depreciation as a cost.
- *Stock pay*: $419M in 2025, expensed in GAAP and deducted in owner cash **[L2015-003]**. Options are expensed.
- *Software*: capitalized software licenses amortized ($81M in 2025) are a real expense **[L2012-003]**, deducted.
- *Restructuring*: $85M in 2025 (closing the last two 150mm factories), $8M in 2024, none in 2023, plus a 2024 gain of
  $132M on a property sale; not recurring in size, not featured as "one-time" in any adjusted figure.
- *The CHIPS tax credit inside operating cash*: $588M (2024) and $335M (2025) of investment tax credit "used to reduce
  income taxes payable" sit inside operating cash flow (cash-flow supplement). They are a rebate on fab spending, not an
  earning of the business; owner cash in Q7 removes them from the maintenance case and nets them against capital
  spending in the all-spending case.
- *Taxes*: effective rate 12.4% (2025), 12.0%, 12.2%; the reconciliation (note 4) shows foreign-derived intangible income
  (-4.0 points), Malaysian incentives (-2.2), R&D credit (-1.4) and stock pay (-1.1). These are standing features of the
  law and of the company's footprint, not carryforwards that run out inside ten years ("tax loss carryforwards were not
  material"); owner cash is taken at the company's own tax.
- *Pensions*: overfunded plans $324M, underfunded $124M at end-2025; immaterial.

**EBITDA in the filer's own mouth** **[M1998-086]**, **[L2000-036]**: none. No instance of "EBITDA" or an "adjusted"
earnings figure was found in the 2025 10-K or the second-quarter 2026 release (text search). The one non-GAAP measure is
"free cash flow", operating cash less capital spending plus CHIPS proceeds, reconciled to GAAP each quarter; it is
featured as "the best metric for owners", and it counts CHIPS proceeds the run does not count as earnings.

**What the accounts say of management's character** **[M1995-064]**, **[M1994-018]**. The filings explain in plain terms
what moved and why (inventory days, the fixed-cost effect of loadings, the CHIPS mechanics), a plus **[M1994-018]**.
**Carried to Q5:** the company gives quarterly guidance, "revenue in the range of $5.65 billion to $6.15 billion and
earnings per share between $2.23 and $2.57" for the third quarter of 2026 (8-K `0000097476-26-000148`, Exhibit 99), the
scourge of "guidance" **[L2019-006]**; the same release states that second-quarter earnings per share "included a 5-cent
benefit that was not in the company's original guidance", which tells the reader where the beat came from rather than
claiming it.

- **VERDICT on the accounts: IN** (no confusion: every unusual item is disclosed and explained, and the confusing-looking
  builds in inventory and prepaid assets are traced to stated causes **[M1995-063]**, **[M2003-029]**). **WEIGHS FOR** on
  clarity **[M1994-018]**, with the guidance habit weighed against and carried to Q5 **[L2019-006]**. The recast earnings
  (depreciation gross of incentives, stock pay and software deducted, the tax credit removed) feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the speakers read rather than meet **[M2007-081]**: the yardsticks are how well they run the
business against "the hand they were dealt" and "how well that they treat their owners" **[M1994-008]**, read in the
proxy, "how they treat themselves versus how they treat the shareholders" **[M1994-009]**.

**The first yardstick: the record against the hand dealt** **[M1994-008]**. The hand: a cyclical, fragmented field in
which every rival compared grew by large acquisitions. The record: organic revenue growth of 3.1% a year 2015 to 2025,
operating margins above every compared rival in every year of the span (Q2 row), returns on tangible capital of 60% to
105% before the capital programme (Q3). Against it: the company's own proxy concedes that 2023 to 2025 revenue growth
was "below the median for Semiconductor Peers" and one-year and three-year shareholder returns were below the median;
and the $24 billion capital programme, the largest decision of the period, has not yet shown a return (Q3).

**Integrity, read on doubt alone** **[M2013-088]**. The tells looked for:
- *Too good to be true; reports that dance* **[M2007-082]**: the 10-K and 10-Qs explain the hard items plainly (the
  fixed-cost effect of factory loadings, inventory days each quarter, the CHIPS mechanics with amounts); the second-quarter
  release volunteers that a 5-cent benefit "was not in the company's original guidance". One gap: the anti-dumping
  investigation the proxy's proponent describes (contrary evidence 8) is not named in the 10-K or the 2026 10-Qs; the
  company's risk factor covers "administrative measures" in general. It is a question of how much an owner is told
  **[M1998-036]**, recorded as a weight, not a doubt about honesty: no filing read shows the company saying anything
  untrue about it.
- *The habits carried from Q4*: quarterly revenue and earnings-per-share guidance **[L2019-006]**. Read with the rest of
  the record: no adjusted earnings figure is featured **[L2016-006]**; the guidance is a range, not a promise to "make the
  numbers" **[L2002-041]**, and the release explains a beat rather than claiming it. A weight against, not doubt.
- *A management fixed on its stock price* **[M2004-067]**: the stated objective is "growth of free cash flow per share
  over the long term" (Item 1), a business measure; bonuses do include total shareholder return against peers (Part B
  of Q6). No instance found of the price "posted in the lobby" **[M2004-067]**.
- *Owners as marks; serial issuance* **[L2014-015]**: none; the diluted share count fell from 1,021 million (2016) to 913
  million (2025) (10-K income statements via XBRL).
- *Legal and regulatory*: "various inquiries and proceedings that arise in the ordinary course", none material (10-K
  Item 3); the officers have no employment contracts and options "have never" been repriced (proxy).
No doubt about honesty was found. The open item is candour on the China investigation, which is a weight, not doubt.

**Love of the business, and after the cheque.** The 10-K's stated ambitions: "act like owners who will own the company
for decades" and be a company "that we would want as our neighbor" (Item 1). The officers are long-serving: all have
been employees for more than five years, the new CFO for more than 25 (8-K `0000950103-26-008325`), and the company
describes "a promote-from-within culture" (Item 1). The chief executive holds 760,717 shares and units (about $216M at
the price) and the former executive chairman 2,680,196 (proxy, ownership table). The hired executive's question,
"What can I do for Berkshire," not, "What can Berkshire do for me?" **[M2017-070]**, inverted: nothing read shows the
company run for the managers' benefit; their pay is examined at Q6, Part B.

**Ability, the weighing** **[M1996-037]**, **[M1999-106]**. The business is good enough that it does not depend on brilliance
at the top (Q2 test 2). Ability shows in the margin record and in plain reporting; it is open on the capital programme,
whose return is the chief test of this management's judgment and is not yet on file.

- **VERDICT on integrity: IN** (no doubt found on the record read **[M2013-088]**; candour on the Chinese investigation and
  the guidance habit are weighed, not doubted **[M1998-036]**, **[L2019-006]**). **Ability WEIGHS FOR** on the operating
  record **[M1994-008]**, with the capital programme left as the open test.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *The retention test* **[M1998-033]**, **[R1995-009]**, **[M1998-110]**. Over 2021 to 2025 net income was $32.8 billion;
  dividends $22.5 billion and buybacks $6.8 billion took $29.4 billion of it out (10-K cash-flow statements). What was
  kept, and more, went into fabs: capital spending of $19.7 billion over the five years, financed in part by $7.25
  billion of added debt (long-term debt $6.80 billion at end-2020, $14.05 billion at end-2025). The test asks whether the
  dollars kept became more than a dollar of value: the owner cash per share the fabs were to grow is lower in 2025 than in
  2021 (Q7 table), so on the intrinsic leg the test is not yet met; the filer says the capacity was built ahead of demand,
  so the check "after three or four years" **[M1998-110]** falls due around 2027 to 2029. "Can you keep using all of the
  capital you generate, effectively" **[M2010-097]**: not shown.
- *Dividends* **[M2004-089]**, **[M2000-051]**, **[L2012-015]**. Policy: "return 100% of free cash flow to shareholders over
  time via dividends and share repurchases" (8-K of 2026-02-04, Exhibit 99.1), a payout ratio of the kind the rows call
  "nuts" **[M2000-051]**. In practice dividends exceeded the company's own free cash flow in each of 2023 ($4.56 billion
  against $1.35 billion), 2024 ($4.80 billion against $1.50 billion) and 2025 ($5.00 billion against $2.94 billion), and
  were raised again in September 2025 and September 2026 (8-Ks). The policy is clear and consistent; paying out more than
  the business produced while borrowing to build it is not shown to be rational **[L2012-015]**.
- *Buybacks* **[L1999-023]**, **[L2016-002]**, **[L2011-003]**. Authorizations of $12.0 billion (2018) and $15.0 billion
  (2022), "No expiration date", no price named (10-K Item 5). Average prices paid (amount over shares, 10-K MD&A for each
  year): 2019 about $108; 2021 about $182; 2022 about $163; 2023 about $163; 2024 about $198; 2025 about $174; first half of
  2026 about $206 (10-Q). Buying was heavy in 2022 ($3.6 billion) and light in 2023 and 2026. Repurchases also continued
  while the business needed its money for fabs and was borrowing **[L2016-003]**. *The test against the bottom of the Q7
  range (written back from Q7):* the bottom of the central range is $116.70 a share. Every year's average price from 2021
  to the first half of 2026 ($163 to $206) sits above it; only 2019's (about $108) sat below. The buyback with no stated
  price therefore weighs against: the prices paid were not at or below "intrinsic value, conservatively-calculated"
  **[L1999-023]**, and "what is smart at one price is dumb at another" **[L2011-003]**.
- *Issuance and deals* **[M1995-001]**, **[L2014-012]**, **[M2007-123]**. No serial issuance (share count down 11% since
  2016). The one deal: Silicon Labs for $231.00 a share in cash, "a total enterprise value of approximately $7.5 billion"
  (8-K of 2026-02-04). Value given against value got: the target's owner cash (operating cash less stock pay less capital
  spending, its 10-K `0001038074-26-000005` and XBRL) was about $53M in fiscal 2022, -$101M in 2023, -$87M in 2024 and
  -$14M in 2025; its revenue was $785M in fiscal 2025. The case rests on "~$450 million of annual manufacturing and
  operational synergies within three years post-close", and the speakers "never count on synergies" **[L2016-008]**; the
  release's claim that the deal is "accretive to Texas Instruments’ earnings per share, excluding transaction-related
  costs, in the first full year" is the measure the rows warn of, since a debt-financed deal "will usually boost per-share
  earnings" **[L2017-004]**. It is a cash deal, so the narrower STOP (an all-stock deal in undervalued stock) does not arise.
- **Part A WEIGHS AGAINST**: dividends above free cash flow paid with borrowed money, a payout set by ratio, buybacks at no
  stated price, and a $7.5 billion purchase of a business with negative owner cash justified by synergies.

**Part B: the pay, the board and the owners.**
- *Pay tied to what the person controls* **[M2003-019]**. The bonus is set on one-year and three-year revenue growth,
  operating margin and total shareholder return "as compared with peer companies", plus "strategic progress", with "no
  formulas, thresholds or multiples" (proxy). Shareholder return is the stock price, which the executive does not
  control **[L1997-022]**. Profit sharing for all employees runs on one stated formula, a plus.
- *Options* **[L1994-021]**, **[M1997-043]**, **[L2004-016]**. Half of each officer's equity is in fixed-price options at
  the market price on the grant date, vesting over four years, with no escalation for retained earnings; the strike is
  the quoted price, not a conservatively calculated value. Options are expensed and never repriced.
- *The ratchet* **[M2012-095]**, **[L2005-015]**, **[M2004-016]**. Equity is "generally targeted at the median level of
  equity compensation awarded to executives in similar positions within the Comparator Group", with data from the
  compensation consultant, Pearl Meyer. The chief executive's total was $22.7 million in 2025, $19.1 million in 2024 and
  $16.2 million in 2023 (summary compensation table), rising while three-year revenue growth and shareholder return were
  below the peer median, by the proxy's own account.
- *The board* **[L2014-026]**. Since 2026-01-01 the chief executive is also chairman (8-K `0000950103-25-013275`), with an
  elected lead director. Directors' holdings are largely grants, options, units and deferred fees (ownership table
  notes), not shares bought by "purchasing shares with their savings" **[L2019-008]**, **[L2002-033]**.
- *Owners as partners.* Plain reporting (Q4) and no adjusted earnings; against it, quarterly guidance **[L2019-006]**, and
  the board opposed a written-consent proposal the proponent says won 78% support in 2021.
- **Part B WEIGHS AGAINST**, mildly: pay benchmarked to peers through a consultant, fixed-price options and a stock-price
  element in the bonus; offset in part by no employment contracts, no repricing, ownership guidelines of six times salary
  for the chief executive, a clawback and plain disclosure.

- **Q6: WEIGHS AGAINST** on both parts **[M1995-001]**, **[L2016-008]**, **[L2016-002]**, **[M2012-095]**.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
net of what must go back in **[M2014-068]**, at the long government rate, "working with a range of possibilities"
**[L2000-024]**. Arithmetic in `Test Runs/_research 2026-10-11 TXN/scripts/value.py` and `scripts/q7_final.py`; outputs
saved beside them (`value_output.txt`, `q7_output.txt`).

**Owner cash after every real cost, all-equity basis** (Q4's recast; operating cash flow less stock pay, less software
amortization, less depreciation taken gross of the CHIPS reduction as the maintenance guess, less the CHIPS tax credit
used inside operating cash, plus interest paid net of other income after tax at 21%; 10-K cash-flow statements 2014 to
2025 via XBRL, 2025 checked to the filed statement; $M):

| 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2,932 | 3,388 | 3,673 | 4,535 | 6,334 | 5,655 | 5,018 | 7,744 | 7,525 | 4,681 | 3,586 | 4,293 |

The all-spending variant (all capital spending, CHIPS proceeds and credits netted against it) is $830M (2023), $1,021M
(2024), $2,684M (2025); it is shown beside, as specific (e) requires, and the maintenance-only case is central because the
filing allows the maintenance guess (Q3). *CONVENTION of this run:* net interest is taken out at the 21% US statutory
rate and other income (mostly interest on cash) is removed with it, so that cash is not counted twice against net debt;
rationale: the all-equity basis needs owner cash before financing, and the filer's interest deduction falls in the US.

**The cash input: which years** (specific (a)). The literal window 2021 to 2025 begins in the upturn the filer describes
("After a sustained period of growth, a market correction began in 2022", 10-K 2022) and the series falls from $7,744M to
$4,293M, a compound -13.7% a year: the first year is "aberrational" on the filer's own description **[L2005-003]**. The
base is therefore the last full cycle of owner cash, trough to trough: troughs in 2014, 2020 and 2024 (the lowest years of
the series), so the last cycle is 2020 to 2023, average **$6,242M**, and the one before it 2014 to 2019, average $4,419M.
Growth between the cycle averages (centres five years apart): **7.15%** a year. Revenue between the same cycles: 4.53% a
year ($14,091M to $17,588M average).

**The cap** (specific (f)). Owner cash of $6,242M carried at 7.15% for ten years would be $12,451M against revenue of
$27,403M at the business's own sales growth: 45.4% of sales, above the highest share earned on file (42.2%, 2021). The cap
applies: the growth carried is the sales growth between the same cycles, **4.53%**, below the discount rate after year ten
**[M1997-095]**, **[M1999-067]**. Both the shown rate and the cut are written down; the uncapped case is shown beside.

**The part that does not decide** (Q2 parts convention): Embedded Processing, 10.8% of 2021 to 2025 operating profit, is
carried at no growth in the growth case.

**Net debt** at 2026-06-30 (10-Q `0000097476-26-000152`): long-term debt $14,052M (carrying, including current portion)
less cash $3,660M and short-term investments $3,341M = $7,051M; less CHIPS Act receivables of $2,163M ($1,005M current,
$1,158M long-term), the earned shelter added at face because it is being collected within about two years (whose tax,
the shelter's value added) = **$4,888M**. Operating leases left out, as the convention says. The $5 billion delayed-draw
term loan is undrawn and conditioned on the Silicon Labs closing; it is not added (the deal is valued beside).
Enterprise value at the price: $259,125M + $4,888M = $264,013M.

**Rate:** 5.60% (Step 0). After year ten, zero nominal growth.

**COMPUTATION feeding the STOP (central, all-equity):**

| case | owner cash base | growth, years 1 to 10 | value $M | per share less net debt | expected return at $283.74 |
|---|---|---|---|---|---|
| bottom: no growth | 6,242 | 0% | 111,461 | **$116.70** | 2.4% |
| top: capped growth | 6,242 | 4.53% (Embedded at 0%) | 154,547 | **$163.88** | 3.4% |
| beside: shown growth, uncapped | 6,242 | 7.15% | 187,421 | $199.87 | 4.1% |
| beside: uncapped, Embedded growing too | 6,242 | 7.15% | 196,618 | $209.94 | 4.3% |
| beside: all-spending, cycle base (2020 to 2023) | 4,405 | 0% (shown growth between cycles 0.0%) | 78,666 | $80.79 | 1.7% |
| beside: literal window, no growth (top under rule (b)) | 5,566 | 0% | 99,389 | $103.48 | 2.1% |
| beside: literal window, -13.7% (bottom under rule (b)) | 5,566 | -13.71% | 34,762 | $32.71 | 0.5% |

Equity-only beside (owner cash after interest, against the market value; cycle base $6,265M): range **$122.51 to
$169.87** a share, expected return at the price 2.4% to 3.4%.

Silicon Labs as if closed, beside and not in the central figure (specific (c), the signed and unclosed deal): its own
filed owner cash is negative (about $53M, -$101M, -$87M, -$14M in fiscal 2022 to 2025, Q6), so it is credited at nothing,
and its enterprise value of about $7.5 billion is added to net debt: every per-share figure falls by $8.21, the central
range to $108.48 to $155.66 and the fair price to $65.89. The $450 million of promised synergies is not credited
**[L2016-008]**.

**The floor, tested first** (Part VII convention of 2026-10-10). At $283.74 the expected return is 2.4% on the no-growth
case, 3.4% on the capped-growth case, and 4.3% on the most generous case the run could construct (uncapped growth, every
part growing). No case in the range, and no case beside it, earns the floor of about ten percent on owner cash after the
company's own tax **[M2003-149]**. The file closes OUT on the floor, whatever the width.

**The width** (shown, not deciding): $163.88 / $116.70 = 1.40 to 1, inside the three-to-one limit; the range is narrow
enough to conclude from, and the conclusion is that the price is above the top of it. "If you need to use a computer or a
calculator to make the calculation, you shouldn’t buy it" **[M2009-005]**; here no calculator is needed in the other
direction: the price is 1.7 times the top of the central range.

**Value range: $116.70 to $163.88 a share against $283.74** (all-equity, after the company's own tax, net debt at
2026-06-30 less CHIPS receivables; the literal window's $32.71 to $103.48 shown beside).

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent instead of the
long rate, the two averaged, per share less net debt: no-growth end $62.99, capped-growth end $85.21, **fair price
$74.10 a share on the all-equity basis** (the central figure); **$79.76 on the equity-only basis** beside it (ends $68.61
and $90.90). After the company's own tax (effective 12.4% in 2025), no conversion. No cheap price is reported. With
Silicon Labs as if closed, the all-equity fair price would be $65.89.

- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case **[M2003-149]**: "there’s just a point at
  which we drop out of the game". The range is narrow and the price sits far
  above its top, so the case is not close; it is not a matter of a pencil **[M2009-005]**, **[L2000-025]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** Nothing to buy: inaction is the default.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (Not a named business in any case: semiconductors are none of casinos, tobacco or loading schemes.)

---
## THE BOX
**OUT at Q7 on price: at $283.74 no case earns the floor of about ten percent (expected return 2.4% to 4.3%); value range
$116.70 to $163.88 a share all-equity (equity-only $122.51 to $169.87; literal window $32.71 to $103.48 beside); fair price
$74.10 all-equity, $79.76 equity-only.** Q1 IN, Q2 IN (China threat carried), Q3 weighs against, Q4 IN and weighs for, Q5
integrity IN and ability weighs for, Q6 weighs against on both parts. No integrity facts are left unjudged (Q5 was reached
and answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts found before the STOP that bear on later questions, written down and not weighed; the box is unchanged
**[M1997-127]**.

**Q9 (debt and exposures).**
- Debt $14.15 billion face at 2026-06-30, all fixed-rate notes, maturities laddered from 2026 ($500M) and 2027 ($1.15
  billion) to 2063 ($1.55 billion); a $1 billion revolving facility to March 2027, undrawn; no commercial paper (10-Q
  `0000097476-26-000152`, notes). Cash and short-term investments $7.0 billion at the same date.
- Coverage on the rows' measure, pre-tax earnings plus interest over interest: 2025 ($5,710M + $543M) / $543M = 11.5
  times (10-K 2025 income statement).
- A $5 billion 364-day delayed-draw term loan for the Silicon Labs consideration, entered June 2026, undrawn,
  conditioned on the closing (10-Q). If drawn in full, debt would be about $19 billion.
- The CHIPS Act award agreement "includes certain events of default and related rights and remedies, including clawbacks"
  (10-K 2025, note 2); incentives recognized to date reduced asset carrying amounts by $4.51 billion and $2.16 billion of
  receivables were outstanding at 2026-06-30.
- Purchase commitments of $1.44 billion over 2026 and after (10-K 2025, note 10); product-liability and warranty claims
  described as historically low (note 10).
- About 50% of 2025 revenue was shipped into China (Item 1A); the anti-dumping investigation described by the proxy's
  proponent (contrary evidence 8).

**Q8, Q10, Q12.** No facts beyond those above.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      Step 0 to Q1, Q2, Q3, Q4, Q5, Q6, Q7 (with the Q6 buyback write-back), and the close, each a pathspec commit of the
      run file and research folder only.
- [x] Dispatched: the brief allowed the per-question commits; the lock in `Screens/_daily/` was present (the dispatcher's)
      throughout. The fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, with one exception declared at
      the top: a directory listing of `Test Runs/` to check the date, which showed three other runs' file names; none
      opened or used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row (check
      script `Test Runs/_research 2026-10-11 TXN/scripts/check_run.py`, result in `check_run_output.txt`); every filing
      fact has its accession; no E-ids.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost (stock pay, software amortization, depreciation gross of incentives, the CHIPS
      credit removed), never a net-income proxy; the sovereign from the US Treasury curve; the price flagged as an
      aggregator quote.
- [x] Contrary evidence written down as found (eight items, the eighth found during Q5 and dated so); facts found for the
      questions after the STOP are under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor issue.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the research folder notes).

**Honest notes on the self-audit.** (1) The maintenance guess (depreciation gross of the CHIPS reduction) is a judgment;
the all-spending case beside it is far lower, so the guess flatters the value, and the verdict holds on either. (2) The
cycle troughs (2014, 2020, 2024) are read from the owner-cash series as the convention says; reading the cycle from
revenue (troughs 2015, 2019, 2024) gives a base of $6,124M and growth of 7.2%, the same verdict (early working in
`value_output.txt`). (3) Silicon Labs' fiscal 2021 owner cash was not read; its four later years are all that is
cited. (4) The price is an aggregator close of 2026-10-09, two days before the run.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The competitor slot when the 10-K names no rival.** The brief says to take the rivals "the 10-K itself names"; TI's
   10-K names none ("dozens of large and small companies"). The run took them from the filer's own proxy, whose peer list
   is described as suppliers that "offer technology that competes with our products", and chose the three analog and
   embedded SEC filers among them (Analog Devices, Microchip, NXP). A rule for this case is missing; the proxy's peer list
   seems the nearest filer-named list, but a compensation peer group is chosen for pay, not for competition.
2. **Which series defines the cycle when owner cash and revenue disagree.** Specific (a) says owner cash defines the cycle;
   here owner cash troughs (2020, 2024) and revenue troughs (2019, 2024) differ by a year, and trough-to-trough leaves open
   whether the closing trough year is in the cycle. The run used owner cash and excluded the closing trough; the
   alternative is shown in the notes. The convention could say which end years belong to a cycle.
3. **The maintenance guess when growth capital is being depreciated.** Depreciation as the maintenance proxy is
   inflated by the depreciation of new fabs built for growth (and deflated by incentives that cut carrying amounts). The
   framework gives no instruction for incentives that reduce asset cost; the run added the reduction back on the reasoning
   that replacements will not earn the credit, which is the run's own judgment.
4. **Government incentives inside operating cash.** A tax credit on capital spending shows up in operating cash flow; the
   Whose-tax convention speaks of carryforwards and credits that run out, not of credits that are really rebates on
   capital spending. The run netted them against capital spending (all-spending case) and removed them from the
   maintenance case; a sentence in Q7 would settle it.
5. **"Net debt ... as the filing states them" and receivables from a government.** Whether earned but uncollected CHIPS
   receivables reduce net debt is not said; the run reduced net debt by them (worth $2.37 a share) under the shelter
   clause and says so.
