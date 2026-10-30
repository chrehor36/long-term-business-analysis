# Company Run — Hyster-Yale, Inc. (NYSE: HY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run (operator rule 10), written by the analyst question by question with pathspec commits of this file
and `Test Runs/_research 2026-10-13 HY/` only. Former registrant names on EDGAR: Hyster-Yale Materials Handling, Inc.
(to 2024-05-30) and NMHG Holding Co (to 2012-06-28).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (HY; also searched for Hyster and Yale); not held.*

**Contamination declared.** Nothing of the blind-listed files was opened, listed or searched. Seen by accident before the
run began, and not used: the recent commit subjects shown in the session's opening context (they concern another company,
HTCMY, a construction-machinery maker, closed OUT at Q2 on ordinary returns); the memory index lines carried into the session
(general project state, nothing about this company). No file under `Test Runs/` other than the template and this run's
own two paths was opened; the only listings were of this run's own paths.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $31.93 (close 2026-10-12; aggregator quote via `tools/run.py`, flagged per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: Class A 14,488,232 and Class B 3,442,155 at July 31, 2026 (10-Q for
  the quarter to 2026-06-30, filed 2026-08-04, accession `0001173514-26-000202`; `python Screens/cover_shares.py HY`
  agrees). The charter note: Class B is "convertible into Class A on a one-for-one basis" (balance sheet, 10-K FY2025,
  accession `0001173514-26-000049`), carries ten votes a share against one for Class A, and has "the same cash dividend
  rights per share" (10-K FY2025, note on capital stock). The classes are economically equivalent, so the count is
  **17,930,387**. Check against issued less treasury: the FY2025 balance sheet shows 14,283,983 Class A and 3,449,811
  Class B outstanding at 2025-12-31 (17,733,794); the rise to July 2026 is consistent with the stock awards of the year
  (S-8 of 2026-08-04, accession `0001173514-26-000205`, registers director-plan shares). No 8-K or prospectus after the
  10-Q changes the count (8-K list read to 2026-08-06).
- **Market cap:** $572.5M (17.930387M x $31.93).
- **Net debt, latest filed date (2026-06-30):** total debt $500.0M (revolver $95.7M, term loan $215.2M net, other debt
  $169.4M, the rest finance leases) less cash $72.6M = **$427.4M** (10-Q, Capital Structure and Financing Activities).
  Operating leases left out. No floor-plan debt of the company's own (dealer floor plans are financed by the
  Wells Fargo joint venture, with recourse; see Q9 facts). Enterprise value at the price: about $999.9M.
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 10/09/2026
  (`python tools/sources.py`, the issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 filed 2026-03-03, accession `0001173514-26-000049` (Items 1, 1A, 5, 7
  and 8); 10-Q to 2026-06-30 filed 2026-08-04, accession `0001173514-26-000202`; proxy DEF 14A filed 2026-03-24,
  accession `0001173514-26-000083`; 8-K of 2025-11-19 (`0001173514-25-000133`, restructuring of about 575 employees,
  about $21M pre-tax), 8-K of 2026-08-06 (`0001173514-26-000213`, a COO appointed); the 10-Ks for FY2016 to FY2024 for
  the segment tables and the 2021 inflation narrative (accessions in `Test Runs/_research 2026-10-13 HY/notes.md`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 $86.1M on
  the filed Consolidated Statement of Cash Flows (10-K FY2025, F-9) equals the XBRL figure `tools/run.py` printed.
- `python tools/run.py HY`, arithmetic lines only: OCF 150.7 / 170.7 / 86.1, stock pay 29.3 / 23.6 / 7.5, capex
  35.4 / 47.8 / 62.5, D&A 45.1 / 47.6 / 45.8 for FY2023 / 2024 / 2025; finance-lease principal 14.6 / 9.6 / 15.7 and
  dividends to minority partners 1.3 a year shown as alternates. Its three-year window and its "yield" lines are not used
  (Part VII); the five-year window it prints is negative. The ten-year series used below is in
  `Test Runs/_research 2026-10-13 HY/computation.py`, transcribed from the filed cash-flow statements.

### The lines of evidence, chosen from Item 1, Item 1A and Item 7, and why
1. **Segment margins over the cycle** (Item 7 segment tables, FY2014 to FY2025): the company reports four parts with very
   different results, and the castle question is answered by parts (Q2, business of parts).
2. **Pricing through the last inflation** (Item 7 of FY2021 and FY2022): the 10-K says the backlog carried fixed prices
   while material costs rose; that is the "agony before a price rise" test made by the filings themselves.
3. **Competitors and cost position** (Item 1, Competition; Item 1A, "Failure to compete effectively"; 10-Q outlook): the
   filer says its rivals "may have lower manufacturing costs" and compete "aggressively with lower-priced value and standard
   products".
4. **Customers and dealers** (Item 1, Distribution; Financing of Sales): independent dealers in 111 countries; direct sales
   to major accounts rising from 19% to 28% of new-truck revenue 2023 to 2025; recourse obligations on dealer financing.
5. **Suppliers, tariffs and raw materials** (Item 1, Key Suppliers; Government and Trade Regulations; 10-Q outlook):
   steel and a limited number of suppliers for engines, drive systems, counterweights; about $100M of tariff costs in 2025.
6. **Acquisitions and their goodwill** (Bolzoni 2016, Maximal 2018, the JAPIC goodwill impairment of $55.6M in 2021).
7. **Debt and leases** (10-Q, Financing Activities; capital structure 55% debt to total capitalization at 2026-06-30).
8. **Buybacks, dividends and stock pay** (10-K Item 5; cash-flow statements; proxy summary compensation table).
9. **Restructurings** (8-K 2025-11-19; restructuring charges of $22.6M in 2024 and $38.4M in 2025; the earlier
   programs of 2009 to 2013 in the XBRL tags).
10. **Litigation and investigations:** 10-Q Part II, Item 1 Legal Proceedings, "None"; the 10-K carries product-liability
    self-insurance and environmental remediation as routine risks. No investigation found in the filings read.

### The balance sheets first, ten years (read in Step 0 because the file may close before Q4) **[M2025-032]**
Year-end figures, USD millions (`tools/run.py` table, first-filed XBRL, checked for FY2025 against the filed balance sheet):

| | 2016 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Stockholders' equity | 463.8 | 527 | 544 | 617 | 357 | 204 | 390 | 475 | 472 |
| Inventory | n/r | 534 | 560 | 509 | 781 | 800 | 816 | 754 | 634 |
| Receivables | n/r | 466 | 468 | 412 | 457 | 524 | 498 | 488 | 490 |
| Goodwill | n/r | 108 | 107 | 115 | 56 | 51 | 53 | 55 | 56 |
| Debt on the face (lines tagged) | n/r | 315 | 295 | 290 | 518 | 553 | 494 | 441 | 494 |
| Retained earnings | n/r | 407 | 427 | 443 | 249 | 153 | 256 | 375 | 289 |

(n/r: not in the tool's table; equity 2016 from the XBRL facts; FY2017 equity 565.5.) What the figures say: book equity
is where it was ten years ago (463.8 in 2016, 472.0 in 2025) while the company paid $216.8M of dividends over
FY2016 to FY2025 against net income attributable to stockholders of $160.0M over the same years; retained earnings fell from
407 (2018) to 289 (2025). Debt roughly doubled from about $290M (2018 to 2020) to $494M (2025) and $500M (June 2026).
Inventory swelled to about 20% of sales in 2023 (816 on 4,118) and was worked back to 17% (634 on 3,769) in 2025.
Goodwill was halved in 2021 by the $55.6M JAPIC impairment (the Maximal purchase of 2018). Gross deferred tax assets of
$187.7M carry a valuation allowance of $165.9M (10-K FY2025, Critical Accounting Policies): the company itself does not
expect to use most of its past tax losses. What they cannot say: whether the 2023 and 2024 earnings are a new level or a
peak of the cycle; only the next full cycle can.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would own this lift-truck maker if the market closed **[M1997-109]**, so
the run asks what the business earns over its cycle, not where the quote goes. The price is out of line only where "the
facts and reasoning lead you" **[M2006-077]**; the margin of safety must "scream" without pencil **[M1996-084]**. No macro
enters: tariffs and the lift-truck cycle are read as properties of this business (its ability to pass costs through),
not as forecasts. Who is paid to tell you: the 10-Q's "long-term objective of achieving approximately 7% operating profit
over the business cycle" is the seller's projection and is not used as an input **[M1995-050]**. **Contrary evidence,
written down as found** **[M1997-127]**: (1) the Americas segment earned 8.0% and 9.9% operating margins in 2023 and 2024
on record revenue, and the backlog and bookings rose for four quarters into mid-2026; a reader could take these as a
castle newly shown; (2) bookings "more than doubled from the prior year" in Q2 2026 (10-Q). Against: the same segment
lost money in 2021 and earned 2.4% in 2025; the decade's company margin is 1.5%.

## THE STANDING RULE
Owning a small, unlevered stake in a $572M company does not put the buyer at risk of ruin; the buyer would not borrow to
own it **[M2012-081]**, **[L2014-024]**. The target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The product
  is old and plain: counterbalanced and warehouse lift trucks, parts and service sold through independent dealers, plus
  forks and attachments (10-K FY2025, Item 1, accession `0001173514-26-000049`). The key variables **[M1998-044]** are
  unit volume through the capital-goods cycle, price against steel, components and tariffs, the share held against
  global rivals and Chinese low-cost makers, and the parts annuity on the installed base. All of them are visible in the
  filings over a decade: revenue, segment margin, the inflation pass-through of 2021, the tariff cost of 2025.
- **Change.** Electrification (electric trucks 31% of revenue in 2025, lithium-ion), automation and hydrogen are named in
  Item 1; they change the product slowly and are not "fast-moving technology" in the sense of **[L1993-023]**: the
  industry's insiders put long-term objectives for it on paper (the company's own, in the 10-Q), which is the test of
  whether the forecast is too hard: the tech insiders "would not want to put down on paper" theirs **[M2000-105]**.
  Change is "more of a threat" than an opportunity **[M1999-063]**, and it is weighed at Q2. The economics can be read "off the figures" **[M2008-069]**:
  what matters is "the economic dynamics of the industry", "are there competitive moats? Is there ease of entry?"
  **[M2011-014]**, and those are Q2's questions, answerable from the filings.
- **Routing.** Not a fast-changing industry; not a financial institution (the 20% interest in the Wells Fargo finance
  joint venture is an equity-method holding with recourse obligations, read at Q9); the parts are operating segments,
  each readable.
- **VERDICT: IN.** The ten-year economics of a cyclical, mature, dealer-sold capital good can be foreseen in kind from ten
  years of segment filings; whether they are good is Q2's question, not Q1's **[M1995-051]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (five-year operating profit FY2021 to FY2025, as reported each year, USD millions; 10-Ks FY2021 to
FY2025, accessions in `Test Runs/_research 2026-10-13 HY/notes.md`):

| Part | 5-yr operating profit | share of the company's 240.0 | castle | decides |
|---|---|---|---|---|
| Americas lift trucks (incl. corporate HQ; Nuvera merged in from 2025) | 646.6 | more than all of it | see below | **yes**, more than half **[L2008-005]** |
| EMEA lift trucks | (111.8) | negative | none shown: losses in three of five years, "unfavorable pricing" in 2025 | no |
| JAPIC lift trucks (incl. Maximal, China) | (149.9) | negative | none shown: losses every year, goodwill impaired 2021 | no |
| Bolzoni attachments | 29.1 | 12% | a niche maker, 0.1% margin in 2025 | no |
| Nuvera fuel cells (to 2024) | (174.0) | negative | a start-up, folded into Americas 2025 | no |

The file closes on the Americas castle. The parts that do not decide are open and would be carried at no growth.

**The castle tests, each with its filing fact, for the Americas part and the company:**
- **Returns over the full cycle, the filer's own figures.** Americas operating margin FY2016 to FY2025: 4.4, 6.0, 3.8,
  4.2, 5.4, (1.0), 1.9, 8.0, 9.9, 2.4 percent; 1,096.2 of operating profit on 22,833.0 of revenue, **4.8%** over the
  decade, before interest and tax and with headquarters inside. The company as a whole: operating profit of $493.5M on
  revenue of $33,343M over FY2016 to FY2025, **1.5%**; net income attributable to stockholders of $160.0M over the decade
  on book equity that started and ended near $470M. An approximate after-tax return on capital employed, FY2018 to
  FY2025 (operating profit plus equity income, taxed at 21%, over equity plus face debt less cash, about $800M; a
  CONVENTION of this run, rationale: the filer reports no return on capital and Q2 asks for the field's returns in words)
  is about 6%, roughly the long government rate of 5.60%. What a moat protects is "excellent returns on invested capital"
  **[L2007-004]**; here there are none to protect.
- **Pricing power and the agony before a price rise** **[M2005-020]**. The last inflation is the test the filings ran
  for us. FY2021 Americas: "material cost inflation and increased freight costs of $107.5 million, net of price
  increases of $22.1 million" turned an operating profit of $102.1M into a loss of $19.7M (10-K FY2021, accession
  `0001173514-22-000013`, Item 7); the company "implemented price increases several times over the course of 2021 and at
  the beginning of 2022, but many of the orders in the backlog" were at fixed prices, and it expected "very low margins"
  into 2022. In 2025, about $100M of tariff costs (10-K FY2025, Item 7), and in mid-2026 the company "does not currently
  expect to offset all tariff-related expenses" (10-Q, Outlook). A strong position will "pass through increases in raw
  material costs" over time **[M2005-017]**; the pass-through came, but two years late and after a loss, and the margin
  it restored in 2023 and 2024 fell back to 2.4% in 2025 when volume fell.
- **The low-cost position.** In a business whose customers buy largely on "new lift truck sales prices" and "cost of
  ownership" (Item 1, Competition), the question is whether this is the low-cost producer **[L2000-017]**, **[M2006-004]**.
  The filer says the opposite of itself: rival manufacturers "may have lower manufacturing costs, offer differentiated
  products at competitive prices" (Item 1A, "Failure to compete effectively"), and in 2026 "competitors continue to
  compete aggressively with lower-priced value and standard products", which "is expected to limit the pace of margin
  improvement" (10-Q, Outlook). The company's answer is to move down into "value and standard" trucks itself. A
  commodity-type field rewards "the low-cost operator" **[L2004-007]**; "commodity businesses have risk unless you’re
  the low-cost producer" **[M1997-010]**; the cost is measured against the competitor **[M2001-013]**, **[M2009-059]**.
- **The competitor row, same metric, the rivals' own reports.** The 10-K names no rival (Item 1 and Item 7 say only
  "several global lift truck manufacturers"; a text search of the FY2021 to FY2025 10-Ks found no rival named as a
  competitor). None of the global lift-truck makers files with the SEC: Toyota Industries and Mitsubishi Logisnext
  (Japan), KION GROUP and Jungheinrich (Germany), Hangcha and Anhui Heli (China) report at home, and Crown Equipment is
  private. The comparison set is therefore the two largest European makers, from their own annual reports (not SEC
  filings; read from the issuers' report files, transcribed in `Test Runs/_research 2026-10-13 HY/notes.md`):

  | Company | metric | span | result | source |
  |---|---|---|---|---|
  | Hyster-Yale | operating profit / revenue | FY2016 to FY2025 | **1.5%** (Americas part alone 4.8%); losses 2021, 2022, 2025 | 10-Ks, accessions in notes |
  | Jungheinrich AG | EBIT / revenue | FY2016 to FY2024 | **7.5%**; never below 5.7% (2020); 8.5% in 2021 and 8.1% in 2022, the years HY lost money; ROCE 10.8% to 20.2% | annual reports 2019 and 2024, five-year overviews |
  | KION GROUP AG | reported EBIT / revenue | FY2016 to FY2025 | **6.0%**; low of 1.5% in 2022 (includes the Dematic warehouse-automation business) | multi-year overviews 2020 and 2025 |

  Toyota Industries, the largest maker, was not read (its reports are on EDINET); flagged as not obtained. Over the
  same decade, through the same inflation and the same cycle, the two rivals earned four to five times this company's
  margin. That is the copper producer at $2.50 set beside the one at $1, "two different kinds of businesses"
  **[M2009-059]**: here the high-cost producer, not the castle.
- **Unit volume and share of mind.** Hyster and Yale are old brands with a dealer network in 111 countries and a parts
  business on a large installed base (parts 16% of 2025 revenue). The brand did not let the company price through 2021
  **[M2005-020]**, and the direct-sales share to large accounts rose from 19% to 28% of new-truck revenue (2023 to 2025),
  buyers who purchase centrally across territories. EMEA lost volume in 2025 to "a market shift toward lighter-duty,
  lower-priced truck models" (Item 7). The customer here does take the low bid **[M2017-009]**.
- **The money test and new entrants.** The filer itself names the attacker: lower-cost global makers and "value and
  standard" trucks from rivals; the company bought a Chinese maker, Maximal, in 2018, and impaired the JAPIC goodwill
  in 2021. "one competitor is frequently enough to ruin a business" **[M2012-108]**; a product that "can be shipped in
  from abroad very easily" is the case the speakers avoid **[M2007-116]**; and the company now pays tariffs on its own
  imported components.
- **Widening or narrowing.** No full cycle shows a widening: the decade's best years (2023, 2024) followed the worst
  (2021, 2022), and 2025 and the first half of 2026 are losses again (operating loss of $46.4M for the six months, 10-Q).
  A change for the better is credited only on a full cycle (Q2, section C of the gaps case); the 2023 and 2024 margins
  came on catch-up pricing of a backlog, not on a cycle in which price held through a downturn **[L1995-022]**.
- **What could destroy it.** Low-priced rivals moving up the range, tariffs on a supply chain that crosses borders, and
  the cyclical swing of capital-goods orders (Item 1A). The filer's own long-term objective of "approximately 7%
  operating profit over the business cycle" (10-Q) is a projection, not a record, and is not used **[M1995-050]**.

**The field's returns over the last full cycle, judged in words.** The field is a commodity-like durable good with a
handful of global makers. Its best-run member read here (Jungheinrich) earned good and steady returns; its largest
European member (KION) earned middling ones and fell to a 1.5% margin in 2022; this company earned poor ones, about the
long government rate on its capital over the decade, and lost money in three of the last five years. Whatever castle
the Hyster and Yale names and the dealer network make, it protects at best ordinary returns for this company, and the
filer's own words place it as a higher-cost maker meeting cheaper rivals: "you can have only two competitors and they’re
still terrible businesses" **[M2013-052]**. A durable castle that protects only ordinary returns closes OUT, not TOO
HARD (Q2, What it rules OUT), and the high-cost producer in a commodity field is OUT **[L1994-035]**, **[M1997-010]**.
The returns are known from ten years of filings, so the TOO HARD route for a moat that cannot be valued **[M2000-019]**
does not apply.

- **VERDICT: OUT.** The deciding part's castle protects only ordinary returns over a full cycle (Americas 4.8% operating
  margin FY2016 to FY2025, company 1.5%, after-tax return on capital about the long government rate), the filer names
  lower-cost rivals and failed to pass through the 2021 inflation, and the two rivals read earned four to five times its
  margin over the same span. The See's test, "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**:
  here the attacker with money already exists and already prices below it.

Q3 to Q12: **NOT REACHED.** The run closes at Q2 (operator rule 2).

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (the ten balance sheets were read in Step 0).
## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 — WHAT IS IT WORTH. NOT REACHED; the arithmetic below is a computation, not a clearance.
## Q8, Q9, Q10, Q12. NOT REACHED.

---
## COMPUTATION, NOT A CLEARANCE (operator rule 3; the owner's reporting figures, Part VII)
Built by Q7's range convention after the stop, for the operator's reporting figures only. No entry language. Arithmetic
in `Test Runs/_research 2026-10-13 HY/computation.py`; inputs from the filed cash-flow statements FY2016 to FY2025.

- **Owner cash after every real cost** = cash from operations (which already deducts interest and the company's own tax)
  less stock pay less all capital spending, with purchases of businesses shown separately. Working capital is counted
  (specific d). Depreciation is a true cost **[L2015-004]**.
- **The base (specific a).** The literal five-year window FY2021 to FY2025 opens on a year the filer describes as
  aberrational **[L2005-003]** (supply-chain constraints, "significant material cost inflation", an inventory build that took operating
  cash to minus $253.5M; 10-K FY2021), so the base is the cycle FY2016 to FY2025, which holds two downturns (2020, and
  2025 into the first half of 2026, which the 10-Q calls "the bottom of the current lift truck market cycle") and two
  peaks (2019, 2024). The literal window is shown beside.
- **Purchases (specific c).** Net purchases of businesses over the cycle were $211.5M (Bolzoni 2016 $116.1M, Maximal 2018
  $78.0M, smaller ones after) against owner cash before purchases of $79.2M: more than half, so the serial-acquirer
  convention puts the organic pair at the centre, with the default pair (purchases deducted) beside it.
- **Maintenance (specific e).** Capital spending over the decade ($442.7M) equals depreciation ($440.2M) within 1%; the
  10-Q describes the spending as "improvements at manufacturing locations and manufacturing equipment, product development
  and improvements to information technology infrastructure". The maintenance guess is depreciation, and the
  maintenance case and the all-spending case are nearly the same.
- **Growth (specific b).** Organic owner cash averaged $34.8M a year in FY2016 to FY2020 and minus $19.0M in FY2021 to
  FY2025; the series changes sign between halves, and the compound rate is meaningless, so the range is the no-growth
  case alone, said so. Revenue grew from $2,569.7M to $3,769.3M over the decade; owner cash did not follow it.
- **All-equity basis.** Interest expense added back after tax at 21% (CONVENTION of this run: the US statutory rate as the
  shield, because the company's reported tax rate swings with valuation allowances, minus 35.2% in 2025 and 34.2% in
  2024); net debt $427.4M at 2026-06-30; 17,930,387 shares; sovereign 5.60%.

| Case (cycle base FY2016 to FY2025, no growth) | equity-only owner cash a year | all-equity owner cash a year | value at 5.60%, per share, all-equity | per share, equity-only |
|---|---|---|---|---|
| Organic, all spending (central) | $7.9M | $25.1M | **$1.12** | $7.89 |
| Organic, maintenance = depreciation | $8.2M | $25.3M | **$1.37** | $8.14 |
| Default, purchases deducted | minus $13.2M | $3.9M | minus $19.94 | minus $13.18 |
| Literal window FY2021 to FY2025, organic, all spending | minus $19.0M | $4.1M | minus $19.75 | minus $18.92 |

- **VALUE RANGE (reporting figure (a)):** **$1.12 to $1.37 a share on the all-equity basis** (the no-growth case alone, the
  all-spending and maintenance variants as its two ends), **$7.89 to $8.14 on the equity-only basis**, against a price of
  **$31.93**. The price sits above the top of every case. The floor is tested first: the central case is owner cash of
  about $25.1M a year against an enterprise value of about $999.9M, a return of about 2.5%, against the floor of about ten
  percent **[M2003-149]**. No case in the range earns the floor at the price; Q7, had it been reached, would close OUT
  whatever the width. Width: not tested, since the floor closes first.
- **FAIR PRICE (reporting figure (b)):** each end valued at ten percent and the two averaged, after the company's own tax:
  **all-equity basis (central): not positive, minus $9.79 a share** (the business valued at ten percent is worth about
  $251M against net debt of $427.4M); **equity-only basis beside it: $4.49 a share.** The central figure is the all-equity
  one. Since the central fair price is not positive and the organic pair is already the centre, no further alternative
  pair exists; the alert, if one is set, can only be on the equity-only figure, labelled so.
- **Beside it, not a case.** The two best years of the window, FY2023 and FY2024, averaged organic owner cash of $92.7M
  and about $120.7M all-equity; at that level the all-equity value at ten percent would be about $43 a share. They are
  the peak of the cycle by the filer's own record (the record revenue of 2024 was followed by an operating loss in 2025),
  so specific (a) bars them as the base. Written down because it is the strongest case for the business **[M1997-127]**:
  if the company reached and held its stated 7% operating margin through a full cycle, the answer would change; nothing
  in ten years of filings shows that it has.

---
## THE BOX
**OUT at Q2**: the deciding part's castle protects only ordinary returns over a full cycle (Americas operating margin
4.8% FY2016 to FY2025, company 1.5%, after-tax return on capital about the long government rate; a higher-cost maker by
its own filing against rivals earning 6.0% to 7.5%). COMPUTATION beneath the stop: range $1.12 to $1.37 a share
all-equity ($7.89 to $8.14 equity-only) against $31.93; no case earns the floor at the price; fair price not positive
all-equity (minus $9.79), $4.49 equity-only. **Integrity facts recorded, not judged** (guidance and a stated margin
objective, carried for Q5 below).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q3 (capital).** Capital spending equal to depreciation over the decade ($442.7M against $440.2M); working capital the
  company targets at "approximately 15% of revenue over time" (10-Q, Outlook); inventory was 17% to 20% of sales
  2018 to 2025. Two purchases (Bolzoni 2016, $116.1M; Maximal 2018, $78.0M): JAPIC, where Maximal sits, lost money every
  year 2021 to 2025 and its goodwill was impaired by $55.6M in 2021; Bolzoni earned $29.1M over five years.
- **Q4 (accounts).** Restructuring charges in 2009, 2010, 2012, 2013 (about $21M to $24M each), 2024 ($22.6M) and 2025
  ($38.4M), with a further program announced 2025-11-19 (8-K, about $21M); a valuation allowance of $165.9M against
  gross deferred tax assets of $187.7M; an add-back of "Restructuring and impairment charges" in operating cash. No
  confusing or suspicious item found in the statements read; no adjusted earnings figure was looked for in the earnings
  releases (8-K exhibits not read).
- **Q5 (integrity facts, recorded, not judged).** The 10-Q publishes an outlook ("a moderate operating loss for full-year
  2026") and a "long-term objective of achieving approximately 7% operating profit over the business cycle", a target the
  decade's record (1.5%) has not met; earnings-release 8-Ks with Item 7.01 accompany every quarter. Under the gaps-case
  convention these are habits weighed at Q4 and judged at Q5 **[L2002-041]**, **[M2004-067]**; any later run that reaches
  Q5 must answer them **[M2013-088]**. No restatement, investigation or legal proceeding found (10-Q Part II Item 1:
  "None").
- **Q6 (money and owners).** Dividends of $216.8M paid FY2016 to FY2025 against net income attributable to stockholders of
  $160.0M; debt roughly doubled. A $50M or 1.5M-share buyback authorised 2024-11-18, no price stated, $44.2M unused at
  2026-06-30; treasury purchases $14.0M (2024) and $4.5M (2025), none in 2026's second quarter **[L2016-002]**; the
  prices paid were not read against a Q7 range, which was not reached. Control: the Rankin and Taplin families, through
  a stockholders' agreement, hold 94.29% of Class B (ten votes a share) and 22.51% of Class A (proxy, accession
  `0001173514-26-000083`); Class A holders had about 29% of the voting power at 2025-12-31 (10-K Item 1A). Pay, 2025
  summary compensation table: CEO Rajiv Prasad $4.40M (2024 $8.10M; 2023 $8.69M); Executive Chairman Alfred M. Rankin, Jr.
  $3.48M (2024 $6.67M; 2023 $9.98M), in years when the company earned $125.9M (2023), $142.3M (2024) and lost $60.1M (2025).
- **Q9 (debt and exposures).** Total debt $500.0M at 2026-06-30 against total temporary and permanent equity of $410.0M, 55% debt to total capitalisation (10-Q);
  a $300M secured revolver to June 2030 with $200.1M available, and a $225M term loan maturing May 2028 at 7.28% with
  $213.8M outstanding; covenants limit dividends unless net leverage is at or below 2.50 to 1 (term loan) or availability
  thresholds are met. Recourse or repurchase obligations on dealer and customer financing of $134.5M at 2025-12-31
  ($219.2M at 2024-12-31). The term loan's 2028 maturity falls in a business that lost money in 2025 and the first half of
  2026 **[L2010-020]**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 482c4b2e); written question by question; committed after each
      (Step 0 to Q1, then Q2, then this close).
- [x] Dispatched by an overnight cycle: the brief allowed the per-question pathspec commits; the lock is the dispatching
      session's and was not touched; the fold into the register is the dispatcher's (operator rule ten).
- [x] No other run file, holding review, `PORTFOLIO.md` or blind-listed screen file was opened, listed or searched;
      what was seen by accident is declared under Contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check
      script `Test Runs/_research 2026-10-13 HY/check_ids.py`, run before the commit); every filing fact has its
      accession or the notes file's accession list; the rivals' figures are from their own annual reports, not SEC filings,
      and are flagged so.
- [x] The order was kept; Q2 closed the run; everything after it is under COMPUTATION or AFTER THE STOP.
- [x] Owner cash after every real cost from cash from operations less stock pay less all capital spending, never a
      net-income proxy (operator rule 5); the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, and the peak-year figure beside the computation); the facts
      for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used (its yield and growth lines and its v4 material ignored).
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **No SEC-filing rival exists and the 10-K names none.** The brief allows a comparison set from elsewhere if the 10-K
names none, but Q2's template asks for "the competitors' own filings (name, metric, accession)"; for a field whose makers
all report in Germany, Japan or China, there is no accession. I used the rivals' own annual reports and flagged them; the
framework does not say whether a non-SEC annual report counts as "their own filings", nor how to compare an IFRS EBIT
with a US GAAP operating profit (I compared them as stated, which is close enough for a four-to-one gap and would not be
for a narrow one). (2) **The business of parts with a negative total.** The five-year operating profit of the company
($240.0M) is less than the Americas part's alone ($646.6M); "more than half of the company's five-year operating
profit" is then met trivially and the share column reads oddly. The rule worked, but it was written for parts that all
earn. (3) **"Ordinary" returns and a part that includes headquarters.** The Americas segment carries corporate costs, so
its margin understates the part's own economics slightly and overstates the whole's; the convention says to judge in
words, which I did, but a run with a closer call would need a rule on how to treat segment margins that include the
centre. (4) **Q7 specific (b) and the range of one case.** Where the series changes sign the range is "the no-growth case
alone", and the fair price is "each end case valued at ten percent, the two averaged"; with one case there are no two
ends. I used the all-spending and maintenance variants as the two ends, which here differ by 1%; the text could say so.
(5) **The interest shield rate for the all-equity basis** is not stated; I confessed the US statutory 21% as a CONVENTION
of this run because the company's reported rate is distorted by valuation allowances.
