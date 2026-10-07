## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34** % · date **2026-09-18** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year constant maturity**. Struck fresh by `python tools/sources.py` on
  2026-09-20; not inherited from the dispatch brief.
- FX if the quote and the earnings differ in currency: quote and earnings are both USD.
  53.6% of FY2025 revenue is international (FY2025 10-K, revenues by geographic region:
  United States $579.1M, International $501.3M), but reporting and listing are USD.
  **New sterling exposure noted**: the Owen Mumford purchase price is denominated in GBP.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025**, period ended 2025-09-30, filed 2025-11-25, **0001872789-25-000036**
  - **10-Q Q3 FY2026**, period ended 2026-06-30, filed 2026-08-07, **0001872789-26-000033**
  - **8-K Item 1.01**, filed 2026-03-20, **0000947871-26-000310** (the deal note)
  - **8-K Item 2.01**, filed 2026-05-15, **0000947871-26-000546** (the deal closed)
  - **8-K/A Item 9.01**, filed 2026-07-31, **0001872789-26-000026** (acquiree accounts, pro formas)
  - **10-K FY2022**, period ended 2022-09-30, filed 2022-12-22, **0001872789-22-000024**
- figure cross-checked against the filed statement (say which): **operating cash flow
  FY2025 $191.7M.** XBRL `NetCashProvidedByUsedInOperatingActivities` returns 191,700,000;
  the filed Consolidated Statements of Cash Flows in the FY2025 10-K reads
  `Net Cash Provided by Operating Activities | $ | 191.7 | $ | 35.7 | $ | 67.7`. Agrees.
  Capex likewise: XBRL 9,300,000 against the filed `Capital expenditures | ( 9.3 )`.

---
## STEP 0A — THE THREE LIVENESS FLAGS ON THE SCREEN ROW

*The screen row is transcription and screening only. Each flag was resolved from a primary
document before Q1 opened (operator rule 4).*

### FLAG 1 — the `deal_note`: EMBECTA IS THE ACQUIRER, AND THE DEAL HAS CLOSED

The 8-K filed 2026-03-20 (**0000947871-26-000310**, Item 1.01, event date 2026-03-19):

> "On March 19, 2026, Embecta Corp. (“embecta”) entered into a definitive Agreement for the
> Sale and Purchase of Owen Mumford Holdings Limited (the “Purchase Agreement”) ... pursuant
> to which embecta has agreed to acquire Owen Mumford Holdings Limited (“OM”), a privately
> held, UK-based innovator and manufacturer of medical devices and drug-delivery
> technologies, in a transaction valued at up to £150 million (the “Transaction”)."

Terms, from the same document: **an upfront cash payment of £100 million at closing
(subject to customary adjustments, including for closing net cash), and up to an additional
£50 million upon the achievement of certain commercial milestones related to sales of the
Aidaptus® next-generation auto-injector platform through the end of 2028.** Unanimously
approved by the embecta board. **No shareholder vote**; consummation was "subject to
customary closing conditions and regulatory approvals". The sellers are six named
individuals and family trustees, so there is no listed counterparty.

The 8-K filed 2026-05-15 (**0000947871-26-000546**, Item 2.01): *"On May 15, 2026, Embecta
Corp. (“embecta”) completed its previously announced acquisition (the “Transaction”) of all
of the issued share capital of Owen Mumford Holdings Limited."* The milestone window is
restated there as *"the period ending June 30, 2029"*, a later end date than the March
8-K's *"through the end of 2028"*. Both are quoted as filed; the run does not reconcile
them and does not need to.

**So the quote is NOT a merger spread.** Embecta is not being taken private; Embecta is the
buyer, and the consideration was cash it already had or borrowed, not its own shares, so
[E5-44] does not bite. A Q5 on this price would not be a category error on that ground.

What the flag resolves to is the second branch the brief named: **the perimeter changed.**
The 8-K/A of 2026-07-31 carries Owen Mumford's audited accounts and the pro formas. Every
annual figure through FY2025 is the pre-acquisition perimeter; FY2026 will be a stub year
carrying about four and a half months of Owen Mumford.

No later 8-K amends or terminates anything. The newest filings are the Q3 FY2026 10-Q of
2026-08-07 and the earnings 8-K of the same day, and **the stock still trades on Nasdaq
under EMBC** (10-Q cover, 2026-08-07). This is not the LEG case.

### FLAG 2 — the `cap_flag`: RE-STRUCK BY HAND, AND IT IS A DRAWDOWN DETECTOR

The screen's $286M cap against a filed public float of $732M is not a broken input. It is
the shape the CALM fold of 2026-09-20 identified: the float is measured at a past date and
the cap at a recent one, and **the share price collapsed in between.**

- **Float, as filed.** FY2025 10-K cover (**0001872789-25-000036**): *"The aggregate market
  value of the voting common equity held by non-affiliates of the registrant, computed by
  reference to the closing price at which the common stock was sold as of the end of the
  second fiscal quarter ended March 31, 2025, was approximately $ 732 million."* Same cover:
  *"The registrant had outstanding 58,512,841 shares of common stock as of November 18,
  2025."* That implies roughly **$12.50 a share at 2025-03-31**.
- **Share count, from the cover of the newest periodic filing.** 10-Q for the quarter ended
  2026-06-30, accession **0001872789-26-000033**, filed 2026-08-07: *"The number of shares
  of Embecta Corp. common stock outstanding as of July 31, 2026 was 56,659,599 shares, par
  value $0.01 per share."* The count **fell** by 1.85 million shares over eight months.
- **Price: $5.29, close of 2026-09-18.** *Aggregator, flagged: Yahoo Finance chart endpoint,
  raw response saved at `_research 2026-09-20 EMBC/quote_yahoo.json`. Live quote only, per
  operator rule 5.* The same series gives a 52-week high of $14.71, a 52-week low of $2.90,
  and $14.34 one year back.
- **RE-STRUCK CAP: 56,659,599 × $5.29 = $299.7M, call it $300M.** The screen's $286M was
  about 5% low and otherwise sound.

**Finding: the equity is down roughly 63% in twelve months, from about $14.34 to $5.29.**
The flag fired on a real collapse, not a stale input. That is a fact about the price, and
by **[E5-42]** it belongs at Q5 and is not evidence about the business. It is recorded here
only because the brief ordered the cap re-struck before anything used it.

### FLAG 3 — the `name_change_note`: THE SERIES IS NOT ONE COMPANY

"Berra Newco, Inc." appears in the EDGAR submissions file as a former name of CIK
0001872789 from 2021-07-15 to 2021-09-03. It is neither a reverse merger nor a de-SPAC. It
is **the registration shell for a spin-off**: Embecta Corp. was separated from Becton,
Dickinson and Company on 2022-04-01. The FY2025 10-K says so in its own words: *"In
connection with our separation from Becton, Dickinson and Company ("BD") in 2022 (the
"Separation"), we entered into a cannula supply agreement with BD."*

**The consequence is the part that matters.** The six annual years in companyfacts do not
describe one company on one perimeter:

| FY ended | Revenue $M | Net income $M | Operating cash $M | What the entity was |
|---|---|---|---|---|
| 2020-09-30 | 1,085.5 | 427.6 | 498.5 | BD carve-out: no spin debt, no standalone corporate cost |
| 2021-09-30 | 1,165.3 | 414.8 | 456.3 | BD carve-out |
| 2022-09-30 | 1,129.5 | 223.6 | 412.2 | **stub year: carve-out to 2022-04-01, standalone after** |
| 2023-09-30 | 1,120.8 | 70.4 | 67.7 | first full standalone year |
| 2024-09-30 | 1,123.1 | 78.3 | 35.7 | standalone |
| 2025-09-30 | 1,080.4 | 95.4 | 191.7 | standalone |

*(All six rows from `companyfacts.json`, `NetIncomeLoss`,
`RevenueFromContractWithCustomerExcludingAssessedTax` and
`NetCashProvidedByUsedInOperatingActivities`, 10-K annual facts; the FY2023-FY2025 column
cross-checked against the filed FY2025 statements above.)*

A 39.4% net margin in FY2020 against 8.8% in FY2025 on almost identical revenue is not a
business that deteriorated by that much. It is **two different accounting entities under
one CIK.** The carve-out years carry no share of the roughly $1.6bn of debt the separation
loaded on, no standalone corporate infrastructure, and BD's allocated rather than incurred
costs. Interest expense alone is $107.3M in FY2025 and did not exist in FY2020.

**So the multi-year mean owner earnings requires [E2-23] has three clean standalone years,
not six, against the corpus default window of five [E2-42].** Carried into Q4 as a finding,
not a footnote, exactly as the brief instructed. It also accounts for every `level_shift`
and `window_disagree` flag on the screen row without any of them being a defect in the
business.

---
