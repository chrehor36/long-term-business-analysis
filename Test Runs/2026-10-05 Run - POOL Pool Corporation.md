# Company Run: Pool Corporation (NASDAQ: POOL), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-05 POOL/`
(raw filings as text, `fetch.py`, `series.py`, `oc.py`, `value.py`, `ids.py`, `check_cites.py`, peer files in `peers/`).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this session by the blind rule
of the brief, so the analyst does not know whether the operator holds POOL.

**CONTAMINATION, declared.** Seen before or during the run, none of it about POOL: the file names of other companies'
2026-10-05 run, holding-review and research-pass files (a directory listing taken to confirm no POOL run existed; none
opened); the five commit subjects in the session header (INVA, PBH, RHI, run.py on SKYW, session state); the memory index
lines that mention a portfolio and a paused queue without names. No POOL file, holding review, queue file, resume file or
prepped list was opened. The brief named "the 2021 FTC consent order"; the filings date it 2011 (see Q5), and the brief's
date was not carried in.

**Session note.** The run was interrupted at the session limit after the filings and peer data were downloaded and before
this file was written; it was resumed on the coordinator's instruction on 2026-10-06 from the files on disk. Nothing was
re-fetched except as listed. The run is dated to the price date, 2026-10-05.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $159.38 (close 2026-10-05, `tools/run.py`, aggregator quote, flagged per operator rule 5: live quote only).
- **Shares, one class:** 36,340,747 common shares, par $0.001 (10-Q for the quarter to 2026-06-30, filed 2026-07-29,
  accession `0001193125-26-322532`, via `python Screens/cover_shares.py POOL`). `tools/run.py` used the older dei count of
  36.443M (2026-04-23); the later cover count is used here.
- **Market cap:** $159.38 x 36.341M = **$5,792M**. Total debt $1.3B at 2026-06-30 (10-Q MD&A); cash $105M at 2025-12-31.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 2026-10-05 (the
  issuing authority; read through `tools/run.py`'s sovereign line).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-26, `0001193125-26-074833` (Items 1, 1A, 3, 5, 7, the
  equity statement, Note 9); 10-Q Q2 2026, `0001193125-26-322532` (MD&A, liquidity, covenants, buybacks); proxy DEF 14A
  2026-03-26, `0000945841-26-000077` (ownership, CD&A, summary compensation); proxy DEF 14A 2025-03-27,
  `0000945841-25-000053` (the 2024 cash-flow metric); 8-Ks of 2026-01-12 `0001193125-26-010379`, 2026-02-13
  `0001193125-26-051351`, 2026-05-04 `0001193125-26-204112` (CEO change), 2026-08-28 `0001193125-26-374331`
  (receivables facility), 2026-09-25 `0001193125-26-402912` (new director). History: 10-Ks FY2005 `0001193125-06-047003`,
  FY2007 `0000945841-08-000016`, FY2009 `0000945841-10-000036`, FY2010 `0000945841-11-000020`, FY2011
  `0000945841-12-000018`, FY2019 `0000945841-20-000041`, FY2022 `0000945841-23-000015`; 8-K 2011-11-22
  `0000945841-11-000103` (FTC settlement); 10-Q Q3 2016 `0000945841-16-000285` (antitrust class actions concluded);
  XBRL company facts (transcription and screening only).
- **One figure cross-checked against the filed statement:** net sales FY2025 $5,289.4M and net cash from operations
  $365.9M, read in the 10-K's MD&A text (`0001193125-26-074833`), match the XBRL series `oc.py` uses.
- **`tools/run.py` arithmetic lines only** (its v4 text, ids and floor ignored per Part VII). Owner cash = OCF less stock
  pay less all capital spending (the D&A variant beside it), USD millions, from the XBRL cash-flow series (checked above):

| FY | sales | gross % | op. % | net income | OCF | stock pay | capex | D&A | **owner cash (capex)** | owner cash (D&A) | acquisitions | buybacks | dividends | diluted sh. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2008 | 1,783.7 | 28.9 | 6.5 | 57.0 | 93.3 | 6.7 | 7.0 | 9.7 | 79.6 | 76.8 | 35.5 | 7.7 | 24.4 | 48.5 |
| 2009 | 1,539.8 | 29.2 | 5.7 | 19.2* | 113.2 | 6.4 | 7.2 | 9.1 | 99.7 | 97.7 | 10.9 | 1.2 | 25.3 | 49.0 |
| 2010 | 1,613.7 | 29.2 | 6.3 | 57.6 | 94.0 | 7.8 | 8.1 | 10.9 | 78.1 | 75.3 | 6.2 | 13.7 | 25.7 | 50.2 |
| 2012 | 1,954.0 | 29.0 | 7.4 | 82.0 | 119.1 | 8.5 | 16.3 | 12.5 | 94.3 | 98.1 | 4.7 | 81.8 | 29.1 | 48.1 |
| 2014 | 2,246.6 | 28.6 | 8.4 | 110.7 | 121.8 | 9.1 | 17.3 | 15.3 | 95.4 | 97.5 | 10.6 | 136.5 | 37.6 | 45.4 |
| 2016 | 2,570.8 | 28.8 | 10.0 | 149.0 | 165.4 | 9.9 | 34.4 | 21.4 | 121.1 | 134.1 | 19.7 | 178.4 | 49.7 | 43.0 |
| 2017 | 2,788.2 | 28.9 | 10.2 | 191.6 | 175.3 | 12.5 | 39.4 | 25.1 | 123.4 | 137.7 | 12.8 | 146.0 | 58.0 | 42.4 |
| 2018 | 2,998.1 | 29.0 | 10.5 | 234.5 | 118.7 | 12.9 | 31.6 | 27.2 | 74.2 | 78.6 | 2.6 | 187.5 | 69.4 | 41.7 |
| 2019 | 3,199.5 | 28.9 | 10.7 | 261.6 | 298.8 | 13.5 | 33.4 | 28.9 | 251.9 | 256.4 | 8.9 | 23.2 | 83.8 | 40.9 |
| 2020 | 3,936.6 | 28.7 | 11.8 | 366.7 | 397.6 | 14.5 | 21.7 | 29.0 | 361.4 | 354.1 | 124.6 | 76.2 | 91.9 | 40.9 |
| 2021 | 5,295.6 | 30.5 | 15.7 | 650.6 | 313.5 | 15.2 | 37.7 | 29.6 | 260.6 | 268.7 | 812.0 | 138.0 | 119.6 | 40.5 |
| 2022 | 6,179.7 | 31.3 | 16.6 | 748.5 | 484.9 | 14.9 | 43.6 | 38.2 | 426.4 | 431.8 | 9.3 | 471.2 | 150.6 | 39.8 |
| 2023 | 5,541.6 | 30.0 | 13.5 | 523.2 | 888.2 | 19.6 | 60.1 | 39.4 | 808.6 | 829.3 | 11.5 | 306.4 | 167.5 | 39.0 |
| 2024 | 5,311.0 | 29.7 | 11.6 | 434.3 | 659.2 | 19.2 | 59.5 | 44.6 | 580.5 | 595.4 | 4.7 | 306.3 | 179.6 | 38.2 |
| 2025 | 5,289.4 | 29.7 | 11.0 | 406.4 | 365.9 | 22.7 | 56.3 | 50.7 | 286.8 | 292.4 | 10.8 | 346.3 | 184.9 | 37.3 |

  *2009 net income carries a $26.5M equity-method write-off of the investment in Latham Acquisition Corporation (10-K
  FY2010, Item 6 note 2, `0000945841-11-000020`). Odd years 2011, 2013 and 2015 are in `oc.py`'s output and omitted here
  for width. Before XBRL, from the filed statements: 2003 sales $1,155.8M, gross 27.3%, operating 7.6% (FY2005 10-K);
  2004 $1,310.9M, 28.3%, 8.7% (FY2005 10-K); 2005 $1,552.7M, 27.9%, 8.7%; 2006 $1,909.8M, 28.3%, 8.8%; 2007 $1,928.4M,
  27.5%, 6.9% (FY2007 10-K, `0000945841-08-000016`; 2004 and 2005 as restated there for stock pay).
- **Averages:** five-year (2021-2025) owner cash $472.6M (capex basis), $483.5M (D&A basis); ten-year (2016-2025)
  $329.5M / $337.8M; eighteen-year (2008-2025) $220.8M. `tools/run.py`'s three-year window ($558.6M) is reported and
  not used (the Q7 convention fixes five years). Stock pay is in every year and is subtracted. Cumulative OCF over net
  income: 1.03 (2008-2025), 0.98 (2016-2025).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether owning POOL with the market closed would be wanted, and the price fall
from about $246 (fourth-quarter 2025 buybacks, 10-K Item 5) to $159.38 says nothing by itself, since the market "It just
tells us prices." **[M2006-077]**. The buyer must be ready to see the price halve, and on borrowed money "you could have
been cleaned out" **[M2020-022]**. No macro view of housing or rates enters; the business's own record through 2007-2010
and 2020-2025 stands in for it. Margin of safety is carried to Q7, where the test is that a case needing pencil is "too
close to think about" **[M1996-084]**. **Contrary evidence, written down as found** (each item was entered here when read,
to "write it down in the first 30 minutes" **[M1997-127]**):
1. The 10-K says of its own industry: "Barriers to entry in our industry are relatively low" and, in Item 1A, "New
   competitors may emerge as there are low barriers to entry in our industry" (`0001193125-26-074833`).
2. Heritage Pool Supply Group, the second national pool distributor, is owned by Home Depot through SRS Distribution,
   acquired in Home Depot's fiscal 2024 (Home Depot 10-K FY2025, `0001628280-26-019436`; Leslie's 10-K FY2025,
   `0001193125-25-323811`, names "Heritage Pool Supply Group, owned by Home Depot"). The attacker with money exists.
3. At Hayward, POOL's share of sales fell from 36% (2024) to 33% (2025) while a second customer rose from 11% to 12%;
   in 2022 and 2023 no second customer reached 10% (Hayward 10-Ks `0001834622-26-000008`, `0001834622-24-000010`,
   `0001834622-23-000017`).
4. The largest suppliers "acting individually or in concert" could sell direct, bypassing POOL (10-K Item 1A).
5. An FTC consent order (final 2012-01-10) resolved an investigation of "conduct in violation of Section 5 of the Federal
   Trade Commission Act", without admission; customer antitrust class actions alleging monopolization followed and ended
   in summary judgment for POOL in 2016 (FY2011 10-K `0000945841-12-000018`; Q3 2016 10-Q `0000945841-16-000285`).
6. Inventory rose from 18.9% of sales (2016) to 27.5% (2025), and turns fell to 2.6 at mid-2026.
7. The CEO left by "mutual" agreement on 2026-05-04 after two years; the successor joined in January 2026 from Motion
   Industries (8-K `0001193125-26-204112`).
8. Debt rose $249M in 2025 "primarily to fund open market share repurchases of $341.1 million" (10-K MD&A); buybacks
   2021-2024 averaged about $360-$383 a share against today's $159.
9. Five-year TSR ended 2025 was 65.10 against the S&P 500's 196.16 (10-K Item 5).

## THE STANDING RULE
No ruin to the buyer from the purchase itself if it is bought for cash and sized so that a halving is borne: "We are never
going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**; "borrowed money has no place
in the investor's tool kit" **[L2014-005]**. Nothing in POOL's own structure calls on its shareholders. Passes as to the
buyer's conduct; the target's debt is Q9's.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **The test:** "a reasonable fix on about what the earning power and competitive position will look like in five or 10
  years" **[M2012-065]**; the product may be plain, but "What is important is that I understand the economic dynamics of
  the industry." **[M2011-014]**.
- **The key variables,** "trying to identify the key variables in that particular business" **[M1998-044]**: (1) the US
  installed base of in-ground pools, about 5.5 million, which grows by new construction (about 62,000 units in 2024, just
  below 60,000 in 2025, 10-K Item 1); (2) the share of sales tied to that base: 64% maintenance and minor repair, 22%
  remodel and upgrade, 14% new construction in 2025 (10-K Item 1); (3) POOL's gross margin per dollar of product, which
  has stayed between 27.3% and 31.3% every year 2003-2025 (table above); (4) the channel: Hayward estimates about 80% of
  US residential pool equipment went through distributors in 2025 and about 75% in 2022 (Hayward 10-Ks).
- **Foreseeable?** A chlorinated pool needs chemicals and its pump and filter fail on a cycle; the variables are slow and
  physical, not technological. The insiders would write the ten-year forecast for the maintenance base down, unlike the
  tech forecasts they "would not want to put down on paper" **[M2000-105]**; nothing here is "a business that must deal
  with fast-moving technology" **[L1993-023]**. The record through 2007-2010 is direct evidence: sales fell 19% from 2006
  to 2009, operating margin fell from 8.8% to 5.7%, and owner cash rose (2009: $99.7M), because working capital came
  home. Doubt, which would put it outside **[M2002-092]**, attaches to who captures the margin (Q2), not to whether the
  economics can be seen.
- **VERDICT: IN.** The economics are those of distributing a maintenance consumable into a large, slowly growing installed
  base; the uncertainty is competitive and belongs to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question, "why is that castle still standing?", is asked knowing "most moats aren’t worth a damn" **[M1995-038]**.

- **What keeps it standing (the filings' evidence):**
  - **Low-cost position in a commodity-like trade.** The products are the suppliers' brands, sold to contractors who also
    buy elsewhere, so the trade is commodity-like, and there "being the low-cost producer is all-important"
    **[L2000-017]**; "the low-cost producer can put you out of business" **[M1997-010]**. POOL's operating margin
    (10.0%-11.0% in 2016-2019 and 2025) sits well above SiteOne's, the national landscape distributor (3.8%-6.6% outside
    2022's 9.0%; SiteOne XBRL from its 10-Ks, CIK 1650729), on a similar gross margin structure, which is what the lower
    cost per dollar of sales would show. Scale: 456 sales centers, more than 200,000 products, about 125,000 customers,
    no customer at 10% (10-K Item 1).
  - **Pricing power, read as pass-through.** Gross margin held in a 4-point band for 23 years, through the 2007-2010
    housing collapse, the 2012 FTC order, the boom and its unwind; the firm "generally pass[es] industry price increases
    through our supply chain" (10-K Item 1). The rows' form is that strong positions "manage to pass through increases in
    raw material costs" **[M2005-017]**. No prayer session is visible: "you can almost measure the strength of a business
    over time by the agony they go through" **[M2005-020]**; in 2025 sales were flat and gross margin unchanged at 29.7%.
  - **The suppliers need it.** POOL is 33% of Hayward's net sales and 46% of its receivables (2025), and was 26% in 2019;
    Pentair's largest customer (named as POOL through 2020) is 18% of Pentair's consolidated sales (2025), up from 15%
    in 2018-2020 (Pentair 10-Ks `0000077360-26-000007`, `0000077360-21-000005`). POOL buys 20%, 12% and 11% of its
    product cost from Pentair, Zodiac and Hayward (10-K). Mutual dependence of this size makes bypass costly for the
    supplier.
  - **The channel did not shift to retail.** Leslie's, the national DIY retailer, went from a 15.6% operating margin
    (FY2021) to -13.7% (FY2025) with a Nasdaq minimum-bid deficiency notice in April 2025 (Leslie's 10-K
    `0001193125-25-323811`), while POOL's maintenance sales were "stable". The professional channel POOL serves held.
- **Against it (the tests applied to the evidence):**
  - **The money test.** "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. Could $10B take on POOL?
    Home Depot has spent more than that on SRS, which owns Heritage and also bought GMS (Home Depot 10-K). And "one
    competitor is frequently enough to ruin a business" **[M2012-108]**. The filer itself calls entry barriers low; the
    rows warn that in such fields "you better be running very fast" because "there are some industries that are just
    never going to have barriers to entry" **[M2012-106]**.
  - **Widening or narrowing,** "whether it’s likely to widen further or shrink on you" **[M1999-108]**: the first year of
    numbers after Home Depot's purchase shows POOL down 3 points at Hayward and the other customer up 1; POOL's 2026 gross
    margin guided 30 basis points lower, citing freight and "an unfavorable shift in customer mix" (10-Q). One year is not
    a trend, and Pentair's figure moved the other way (15% to 18-20%).
  - **The low bid.** The contractor is not buying a brand of POOL's; whether he takes "the low bid" **[M2017-009]**
    depends on breadth, availability and credit terms, which the 10-K lists among the competitive factors with price.
    POOL owns no brand that protects it "against the intermediaries making all the money" **[M2019-041]**; it is the
    intermediary, and its suppliers earn the brand margin (Pentair Pool segment income 31.0%-33.8% of sales, 2023-2025;
    Hayward operating margin 17.7%-22.7%, 2021-2025).
- **What could destroy, modify or reduce it,** "destroy, or modify, or reduce the economic strengths" **[M2000-014]**:
  (a) Home Depot pricing Heritage to buy share; (b) a large supplier going direct; (c) drought rules in the four states
  that are 53% of sales. Each is a threat to the margin, not to the installed base.
- **The competitor row** (same metrics, from each company's own filings):

| company | role | metric over the span | source |
|---|---|---|---|
| POOL | distributor | gross 27.3-31.3%, operating 5.7-16.6% (2003-2025); 10.0-11.0% outside the boom | 10-Ks above, XBRL |
| SiteOne (SITE) | landscape distributor, Horizon's rival | gross 26.4-34.9%, operating 3.8-9.0% (FY2014-FY2025) | XBRL, 10-K `0001650729-26-000005` |
| Leslie's (LESL) | DIY pool retailer | operating 13.1-15.6% (FY2019-2022), 7.0%, 4.3%, -13.7% (FY2023-2025) | XBRL, 10-K `0001193125-25-323811` |
| Hayward (HAYW) | supplier | operating 13.5-22.7% (2019-2025); POOL 26%, 30%, 36%, 35%, 36%, 36%, 33% of its sales (2019-2025) | 424B4 2021, 10-Ks 2022-2025 |
| Pentair (PNR) | supplier | Pool segment income 31.0%, 33.2%, 33.8% (2023-2025); largest customer 15% (2018-20), 20% (2022), 18% (2025) | 10-Ks |
| Heritage Pool Supply | distributor, Home Depot via SRS | no separate figures; not an SEC filer at that level (flagged) | Home Depot 10-K |
| Fluidra (Zodiac) | supplier, 12% of POOL's cost | not an SEC filer (flagged); not read | n/a |

- **VERDICT: IN, narrowly.** The castle is a scale and low-cost distribution position whose margin has held through a
  housing collapse, an FTC order that removed whatever exclusionary terms there were, a boom and an unwind; that is
  evidence on the record, not a forecast. A castle shown open would need the margin or the share filling in on the
  evidence, and one year at one supplier does not show it. The moat is not "tenuous in any way" in the sense of
  **[M2000-019]** on today's record, but the Home Depot attack is the live threat and is carried to Q7 as lower certainty,
  which there means the no-growth end weighs heavier.

## Q3: HOW MUCH CAPITAL MUST GO IN, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, measured as the rows ask, "look at return on tangible
  assets" **[M2011-060]**: operating income over net tangible capital (equity plus debt less cash, goodwill and
  intangibles) was 61% (2016), 50% (2019), 66% (2022), 45% (2025); with capitalized operating leases added, 40% (2019),
  36% (2025). A distributor's thin margin "only works in terms of return on capital if you turn your equity
  extraordinarily fast" **[M2017-096]**, and POOL's does, at about 4 times sales to net tangible capital. The high figure
  is checked for "a cyclical peak in earnings, a monopolistic position, or leverage" **[L1994-009]**: the 2016-2019
  figures precede the boom; leverage flatters return on equity but not this measure.
- **To stand still and to grow:** capex has averaged about 1% of sales (10-Q: "Historically, our capital expenditures
  have averaged roughly 1.0% of net sales"), roughly equal to D&A; the real growth cost is working capital, since
  inventory alone is 24-28% of sales since 2021. Each added dollar of sales needs about 20-25 cents of working capital,
  which is the "amount of capital required to produce incremental revenues" **[M2000-088]**, and it still earns well above
  "decent returns on the incremental sums they invest" **[L2009-012]**.
- **Acquisitions:** $812M in 2021 (Porpoise Pool & Patio, the Pinch A Penny franchisor) at the top of the boom; its
  reporting unit carries $401.6M of goodwill (10-K critical estimates). Judging the allocation, "you have to include
  goodwill, because we paid for it" **[M2011-060]**: with goodwill and intangibles counted, 2025 pretax return on all
  capital employed is about 25% (580.2 over equity plus debt less cash, 2,279). The 2009 Latham equity write-off ($26.5M)
  was a capital error of the earlier management.
- **WEIGHS FOR.** High returns on tangible capital through the cycle; growth needs working capital but earns well on it.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion; otherwise WEIGHING.
- **Balance sheets first, ten year-ends** (USD M; `tools/run.py` table, read against the FY2025 and FY2019 statements),
  "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**:

| year-end | equity | goodwill | intangibles | cash | receivables | inventory | debt | retained earnings | inventory/sales |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 205 | 185 | 13 | 22 | 61 | 486 | 437 | -184 | 18.9% |
| 2018 | 224 | 188 | 12 | 16 | 69 | 673 | 658 | -219 | 22.4% |
| 2019 | 410 | 189 | 11 | 29 | 77 | 702 | 501 | -65 | 21.9% |
| 2020 | 639 | 268 | 12 | 34 | 122 | 781 | 404 | 134 | 19.8% |
| 2021 | 1,071 | 688 | 313 | 24 | 155 | 1,339 | 1,173 | 527 | 25.3% |
| 2022 | 1,235 | 692 | 305 | 46 | 128 | 1,591 | 1,362 | 653 | 25.7% |
| 2023 | 1,313 | 700 | 298 | 67 | 146 | 1,365 | 1,053 | 700 | 24.6% |
| 2024 | 1,273 | 699 | 291 | 78 | 116 | 1,289 | 950 | 648 | 24.3% |
| 2025 | 1,185 | 707 | 284 | 105 | 136 | 1,455 | 1,199 | 521 | 27.5% |

  (Receivables here are the unpledged line; total net receivables including pledged are larger and are financed by the
  securitization facility; DSO was 26.3 days in 2025 and 2024.) **What moved and why.** Equity is small and was below
  goodwill until 2020 because buybacks are charged to retained earnings (negative through 2019; 10-K equity note); the
  2021 step in goodwill and intangibles ($688M, $313M) is the Porpoise purchase. Debt tracks buybacks more than
  operations: it fell in 2023-2024 when inventory was released and rose $249M in 2025 to fund $341M of repurchases.
  The one figure to look at twice is inventory: "inventories look out of line, you know, with sales" **[M1995-064]** is
  the tell the rows name. Inventory rose from 18.9% to 27.5% of sales; the filer's reasons are buying ahead of price
  increases, inflation, new centers and broader categories (tile, building materials, private label), and the reserve
  fell from $26.7M to $23.9M. Not a confusion: the 2023 release ($226M lower inventory, OCF $888M) shows the stock is
  real and saleable. What the figures cannot say: whether the higher stock is a permanent cost of the broader line or
  defensive buying against a rival's availability.
- **The real costs.** Stock pay ($22.7M in 2025) is expensed and subtracted here; the rows call omitting it "the most
  egregious example" **[L2015-003]**, and POOL does not omit it. D&A ($50.7M) is close to capex ($56.3M). Leases
  ($103M paid in 2025) are operating costs above the owner-cash line. No EBITDA in the filer's mouth (the covenants use
  it, not the reporting). Restructuring: none recurring.
- **Earnings presentation.** POOL publishes "adjusted" EPS excluding the ASU 2016-09 tax benefit (which lowers adjusted
  EPS below GAAP in 2024 and 2025) and, in 2026, CEO transition costs (raises it); it gives annual EPS guidance. A
  management that "attempts to wave away very real costs" **[L2016-006]** is one tell; here the adjustments run both
  ways and are small. Guidance is the habit the rows distrust, "we become downright incredulous if they consistently
  reach their declared targets" **[L2002-041]**; POOL has not reached them consistently (the 2023 and 2024 EPS-growth
  awards did not vest; 2025 operating income missed its bonus target). One habit, no second tell, so a weighing against
  under the framework's two-tell convention. Growth claims in the proxy use a 10-year window (net sales 8%, diluted EPS
  14% CAGR); the rows say to "be suspicious as to why the beginning and terminal years have been selected"
  **[L2005-003]**: that window starts below the boom and ends after it, so it is fair.
- **Cash against earnings:** cumulative OCF was 1.03 times net income over 2008-2025 and 0.98 over 2016-2025.
- **VERDICT on confusion: IN. WEIGHS FOR** on the accounts as a whole, against only lightly for guidance; "we can’t afford
  to use it as a total exclusionary factor" **[M1994-018]**. The recast owner cash feeds Q7.

## Q5: WHO RUNS IT? STOP on integrity; WEIGHING on ability.
- **The two yardsticks** **[M1994-008]**. Running the business, against "the hand they were dealt": sales from $1.16B
  (2003) to $5.29B (2025), operating margin from 7.6% to 11.0%, diluted shares from 48.5M (2008) to 37.3M (2025), no loss
  year through 2007-2010; the boom was taken (margin 16.6% in 2022) and given back to about the pre-boom level.
  Treating owners: dividends every quarter since 2004, raised yearly 2011-2025; buybacks (Q6).
- **Integrity.** The tells looked for: the FTC matter of 2010-2012 under the earlier chief executive (Manuel Perez de la
  Mesa, now a director holding 978,182 shares, 3%) ended in a non-monetary consent order without admission; the
  follow-on monopolization class actions were defeated on summary judgment in 2016. That is a finding on competitive
  conduct, not on candour to owners; it is carried to Q12. The proxy shows one place where a bonus metric was adjusted:
  operating cash flow excluded hurricane-deferred taxes in both 2024 (lowering the measured figure from 151.8% to 136.0%
  of net income) and 2025 (raising it), which is symmetrical. Misses are allowed to fail: the 2023 EPS awards paid zero,
  the 2024 awards are not expected to vest, and 2025 bonuses paid 56% on operating income. No related-party transactions
  disclosed for the new director. On the record, no doubt rises to "If you’ve got doubts, forget it." **[M2013-088]**.
- **Ability, and the change at the top.** The CEO of two years left on 2026-05-04 by "mutual" agreement with no reason
  given; the successor (age 47) came from Motion Industries in January 2026, so he has no record in this business; the
  chair since 2017 (director since 2000) became Executive Chair at $50,000 a month. The rows name the danger plainly:
  "the number one risk factor is that this business gets the wrong management" **[M2021-042]**. The business is one that
  needs operating discipline (inventory, pricing, cost) more than genius, which tilts Q2 test 2 in its favour, but the
  new man is unproven.
- **VERDICT on integrity: IN. Ability: UNDECIDED,** strong institutional record, unproven new chief executive.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, retention.** Earnings are mostly paid out: 2021-2025 dividends ($802M) and buybacks ($1,568M) took 86% of net
  income ($2,763M); with the $812M acquisition of 2021 added, outlays exceeded earnings and debt rose. The market leg of the test, "if after three or four
  years, you’ve found that the dollars we’ve retained hasn’t created more of that in value" **[M1998-110]**, fails for
  2021-2025 (price $383 average paid in 2021, $159 now), but little was retained, so the test bites on the buybacks.
- **Buybacks.** The programme names no price ("in the open market at prevailing market prices", 10-K Item 5); the rows
  find value "entirely purchase-price dependent" **[L2016-002]**, and the test is a price "below its intrinsic value,
  conservatively-calculated" **[L1999-023]**. Average prices paid: 2017 $107.9, 2018 $145.2, 2019 $149.6, 2020 $190.0,
  2021 $383.4, 2022 $381.9, 2023 $358.8, 2024 $363.2, 2025 $274.8 (dollars over shares retired, equity statements of the
  FY2019, FY2022 and FY2025 10-Ks); Q2 2026 $177-$203. Read against the Q7 range run below (bottom $229.76 on the
  convention, $160.19 on the whole-cycle variant): 2017-2020 purchases sat below both bottoms; 2021-2025 purchases,
  $1.57B, sat above both, and 2025's were debt-funded; Q2 2026 purchases sit below the convention bottom and above the
  whole-cycle bottom. Under the framework's convention this **weighs against**: "what is smart at one price is dumb at
  another" **[L2011-003]**.
- **Issuance and deals:** no stock-paid deals found in the filings read; the 2021 Porpoise purchase was in cash. The one
  STOP of Part A does not apply.
- **Part B, pay and board.** Annual bonus on operating income (64% weight for the CEO), cash flow, and individual goals;
  equity half time-based, half on three-year EPS growth or average ROIC. The ROIC award's threshold is 10% against an
  achieved 21.3%: "it’s silly to have something that starts at 10 percent or 15 percent" **[M2004-097]** for a business
  this good. Operating income is "under the reasonable control of the person that’s being measured" **[M2003-019]**.
  Total CEO pay $6.5M (2025), moderate. Directors other than the former CEO own little (the chair 14,586 shares, others
  under 8,000); the chair became executive chair, which the rows warn against when the person is mediocre, "how hard it
  is to replace a mediocre CEO if that person is also Chairman" **[L2014-026]**, though here the board did replace a CEO.
- **WEIGHS AGAINST (Part A, the 2021-2025 buybacks above value on either range); UNDECIDED (Part B).**

## Q7: WHAT IS IT WORTH? STOP.
The questions are "How certain are you that there are indeed birds in the bush? When will they emerge and how many will
there be?" and the rate, "What is the risk-free interest rate (which we consider to be the yield on long-term U.S.
bonds)?" **[L2000-021]**, held "working with a range of possibilities is the better approach" **[L2000-024]**.

- **Construction (the framework's Q7 CONVENTION):** five-year average owner cash after every real cost (capex basis,
  2021-2025) $472.6M; growth shown on aggregate owner cash, 2021 to 2025, (286.8/260.6)^(1/4) - 1 = 2.4% a year; ten years
  at that rate, then zero nominal growth; discounted at 5.66%; equity basis (owner cash is after interest), 36.341M shares.
- **CONVENTION of this run (confessed): the whole-cycle variant.** The five-year window holds the boom (2021-2022) and the
  inventory release (2023), so the owner asked for a variant across a whole cycle: the ten-year average 2016-2025
  ($329.5M), with growth shown 2016 to 2025 on aggregate owner cash, (286.8/121.1)^(1/9) - 1 = 10.1% for ten years (capped
  below the discount rate's infinity problem by the ten-year term and zero growth after). Rationale: a base year in a
  boom or a trough is the distortion **[L2005-003]** names.
- **CONVENTION of this run (confessed): a normalized central case** for the fair price only: $360M of owner cash (2025
  net income $406M, less about $42M of working capital to support 4% nominal sales growth at 20% of sales, less capex
  over D&A of about $6M), growing 4% for ten years then flat. Rationale: the five-year average carries boom and release
  years, the ten-year average carries a smaller, pre-boom company; the maintenance judgment from the filing (capex about
  1% of sales, working capital about a fifth of sales) gives the cash the present business throws off.

| case | owner cash | growth 10 yrs | value | per share | expected return at $159.38 | price at which it returns 10% |
|---|---|---|---|---|---|---|
| convention, no growth (bottom) | 472.6 | 0% | $8,350M | **$229.76** | 8.2% | $130.05 |
| convention, shown growth (top) | 472.6 | 2.4% | $10,116M | **$278.38** | 9.6% | $153.39 |
| whole cycle, no growth | 329.5 | 0% | $5,822M | $160.19 | 5.7% | $90.67 |
| whole cycle, shown growth | 329.5 | 10.1% | $12,900M | $354.98 | 11.2% | $182.02 |
| central (normalized) | 360.0 | 4% | $8,732M | $240.28 | 8.3% | **$130.25** |

  ("Expected return" is the discount rate at which the case's cash stream equals the market cap; owner cash is after
  POOL's corporate tax and interest and before the buyer's own tax, which this run treats as the pre-tax return to the
  buyer, a CONVENTION of this run stated because the rows' "10% pre-tax" was Berkshire's own pre-tax figure. With 4% growth
  carried for ever instead of ten years, the central case returns about 10.5%; the answer turns on that terminal choice.)
- **Value range: $229.76 to $278.38 a share** (convention; top over bottom 1.21, well inside three to one), **against
  $159.38.** Whole-cycle variant: $160.19 to $354.98 (2.2 to one). The price sits 31% below the convention's bottom, so
  on the rate alone it would look cheap; but the rate here is 5.66% and the floor is not.
- **The floor (CONVENTION, about 10% pre-tax):** "we don’t want to buy equities where our real expectancy is below 10
  percent" **[M2003-149]**; "a very high probability of at least 10% pre-tax returns" **[L2002-020]**. At $159.38 the
  convention range returns 8.2% to 9.6%, the central case 8.3%, the whole-cycle variant 5.7% to 11.2%. Only the
  whole-cycle top clears 10%, and it rests on 10.1% growth measured from a 2016 base. The floor is qualified by the
  speakers, "we are guessing at our future opportunity cost" **[M2003-151]**, and cheap money moves it "a little"
  **[M2016-078]**; at a 5.66% long rate money is not cheap, so no downward qualification applies. Below the floor,
  "there’s just a point at which we drop out of the game" **[M2003-149]**.
- **Not a screamer either way.** Whether POOL returns 8% or 10.5% depends on the terminal assumption and on which window
  is honest; "if you really need a calculator to figure out that it’s" the one rate or the other, "forget about the whole
  exercise" **[M2009-005]**; "It should scream at you." **[M2009-005]**. It does not.
- **Reported at the owner's request:**
  - **FAIR PRICE about $130** (central case clears 10%; $130.05 on the convention's bottom, $153.39 on its top, $130.25
    normalized). Tax: owner cash after corporate tax, before the buyer's tax. Floor applied on equity (market cap against
    owner cash after interest), not on equity plus net debt; on an enterprise basis (adding $1.3B debt and $336M leases
    to the price, and interest back to the cash) the expected return is lower still, because the debt costs about 4.2%.
  - **CHEAP PRICE about $91.** Rule (CONVENTION of this run): the lower of (a) the price at which the most conservative
    case, whole-cycle owner cash with no growth ($329.5M), returns 10% ($90.67), and (b) 30% below the convention range's
    bottom ($160.83), the margin the rows describe as "25 or 30 percent less than it was worth" **[M2019-002]**. Below
    about $91 the no-growth, whole-cycle cash alone pays the floor, so no growth and no window choice is needed.
- **VERDICT: OUT.** The range is narrow, the price is below it at the long rate, but the expected return at $159.38 is
  below the about-ten-percent floor in every case but one, and the case is a pencil case, "too close to think about"
  **[M1996-084]**.

---
## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP. NOT REACHED (closed at Q7).
## Q9: COULD IT RUIN US? WEIGHING. NOT REACHED.
*COMPUTATION: NOT A CLEARANCE.* Facts recorded for a later run only: total debt $1.3B at 2026-06-30 (revolver $424M,
term loan $500M due 2029, term facility $90M due 2029, receivables facility $316M); covenant average leverage 1.78x
against a 3.25x maximum, fixed-charge cover 4.67x against 2.25x (10-Q); the receivables facility, shown maturing
2026-10-30 in the 10-Q, was extended to 2028-08-25 (8-K `0001193125-26-374331`); floating rate, partly swapped; target
leverage 1.5 to 2.0 times EBITDA by policy. Operating leases $336M. Chemical storage at every center (10-K Item 1A).
## Q10: IS IT THE FAT PITCH? WEIGHING. NOT REACHED.
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.
*Recorded for a later run, not a verdict:* the 2011 FTC consent order is the item the newspaper test, "if a story were
written by an unfriendly but intelligent reporter" **[M2008-011]**, would read first.

---
## THE BOX
**OUT, at Q7** (Q1 IN; Q2 IN narrowly; Q3 for; Q4 IN; Q5 integrity IN; Q6 against). Value range $229.76 to $278.38 a
share on the convention (whole-cycle variant $160.19 to $354.98) against $159.38; expected return at the price 8.2% to
9.6% on the convention, 8.3% central, below the about-ten-percent floor. **Fair price about $130; cheap price about $91.**
Not TOO HARD: the deciding question is the price against a floor, and it is answered. The question most likely to move
the next run is Q2: whether Home Depot's Heritage takes share or margin from POOL.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **not done**;
      the brief forbade commits, and the session limit interrupted the run before the questions were written, so the
      file was written in one pass on resumption from the research on disk.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row's text
      (`check_cites.py` in the working folder); every filing fact has its accession; no E-ids.
- [x] The order was kept; Q7 closed the run; Q8 to Q12 are NOT REACHED and the Q9 facts are marked not a clearance.
- [x] Owner cash after every real cost, stock pay and all capex subtracted, never net income; the sovereign from the US
      Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found, in nine items under the foundations.
- [x] Not a point-in-time run; rows cited span 1994-2025, none after the run date.
- [x] Only the arithmetic lines of `tools/run.py` were used; its share count was replaced by the later cover count.
- [x] `python tools/check_framework.py` run on the finished file: PASS (2026-10-06); `check_cites.py`: 57 ids, 0 problems.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The floor against a price below the range.** The Q7 convention discounts at the long rate (5.66%) and closes OUT
"if the price sits inside or just below" the range, but says nothing of a price well below the range's bottom whose
expected return is still under the ten-percent floor. Here the price is 31% below the bottom and fails the floor; the
run closed OUT through the floor, which the text supports, but the convention as written reads as if any price far below
the range is IN. When the long rate is far below the floor, the range and the floor are two different tests and the
text should say which governs (the run took the floor). (2) **"Pre-tax" is not defined for a minority buyer.** The rows'
10% pre-tax was Berkshire's own return before Berkshire's tax; owner cash is after the company's tax. The run treated
owner cash as pre-tax to the buyer and said so; a rule should fix it. (3) **The growth shown, measured first year to
last on a working-capital business,** swings with inventory timing (2.4% on 2021-2025, 10.1% on 2016-2025); the
convention's "growth shown" needs a rule for endpoints in a distributor (an average of first and last two years, or a
regression). (4) **The zero-growth-after-year-ten rule** decides this case: with 4% growth carried on, the central case
clears 10%; with it stopped, it does not. A nominal zero after ten years is harsh for a business whose cash grows with
prices, and the PG specifics adopted it without a row. (5) **Operator rule 3's label contains an em dash,** which the
session's standing style rule forbids; the run wrote "COMPUTATION: NOT A CLEARANCE". (6) **The template's position
note** tells the analyst to check `PORTFOLIO.md`, which the blind rule of a purchase brief forbids; the note should
allow "not checked, blind".
