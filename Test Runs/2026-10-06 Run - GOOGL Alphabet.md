# Company Run: Alphabet Inc. Class A (NASDAQ: GOOGL), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. The template was copied to this dated name before any fetch (commit
`713291d`). Working folder: `Test Runs/_research 2026-10-06 GOOGL/` (`run_py_output.txt`, `cover_shares_output.txt`,
`sources_output.txt`, `notes - filings read and arithmetic.md`; raw filings under `cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md` was not opened,
so whether the operator holds GOOGL is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) No earlier run file or research folder for GOOGL or GOOG was searched for or opened; no
queue, resume-state, reading-list or alerts file was opened. (2) The governing document itself names Google: the Q1 tests
quote **[M2012-073]** ("being way wrong with Google or Apple"), Q6 quotes **[M2004-092]** (Google's owner's manual), Q10
narrates the Google omission (**[M2019-024]**, **[M2017-021]**), and section VI carries the pair **[M2019-049]** against
**[M2019-024]** OPEN. These are the speakers' views of a 2004 to 2021 Google, read as evidence of method, not as a verdict
on the 2026 business. (3) The filings themselves disclose that Berkshire Hathaway bought $10B of Alphabet stock in a private
placement in June 2026 and has held a position "since Q3 2025" (8-K, 2026-06-04, `0001193125-26-257724`, EX-99.1). That is
a fact about another buyer, and the analyst is exposed to it as social proof; it is written down below as contrary
evidence and given no weight as a reason, since decisions are not made "based on what other people think" **[M1994-014]**.
(4) Training memory of the company (search, YouTube, Cloud, Waymo, the AI race) is a prior; every fact used below is from a
filing read today.

*Dash note: the only em dashes in this file are inside quotations printed that way.*

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $346.47 (GOOGL close 2026-10-05; Yahoo Finance chart endpoint via `tools/run.py`; **aggregator, live quote
  only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: Class A 5,868 million, Class B 835 million, Class C 5,527 million,
  "As of July 15, 2026" (Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-23, accession `0001652044-26-000071`;
  `python Screens/cover_shares.py GOOGL` returned the same three figures). Sum **12,230 million**. Charter note read before
  adding: "The rights of the holders of each class of our common and capital stock are identical, except with respect to
  voting" (10-K FY2025, equity note, `0001652044-26-000018`); B carries ten votes, A one, C none. Not in the count: the
  6.25% Series A and B mandatory convertible preferred sold in June 2026 ($15B, converting after about three years into a
  variable number of A or C shares) and any shares sold after the cover date under the $40B at-the-market program begun
  in Q3 2026 (8-K, 2026-06-04, `0001193125-26-257724`, EX-99.1; 8-K, 2026-06-05, `0001193125-26-259830`).
- **Market cap:** 12,230.0M x $346.47 = **$4,237,328M** (about $4.24 trillion). CONVENTION of this run: the Class A price
  is applied to all three classes, because their economic rights are identical by the charter note; rationale: the C
  shares trade a little below A (the June offering priced A at $355.1982 and C at $351.8018), and the difference does not
  move any line below.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  10/05/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-05, `0001652044-26-000018`: Item 1A (competition, advertising, AI, margins), Item 7
    (revenues by type, monetization metrics, segment operating income, capital expenditures, leases, financing,
    repurchases), the cash flow statement, the equity note.
  - 10-Q Q2 2026, filed 2026-07-23, `0001652044-26-000071`: the cover, the revenue table and backlog note, the
    non-marketable securities note, the stock-pay note, legal matters (search, ad tech, Play), MD&A capital expenditures
    and financing, the cash flow statement.
  - 8-K, 2026-07-22, `0001652044-26-000066`, EX-99.1 (Q2 2026 results): its non-GAAP habits read. The release offers
    three non-GAAP measures only, "free cash flow; constant currency revenues; and percentage change in constant currency
    revenues", each reconciled; free cash flow is defined "as net cash provided by operating activities less capital
    expenditures", before stock pay. No adjusted earnings figure found in the release.
  - 8-K, 2026-06-04, `0001193125-26-257724`, Item 8.01 and EX-99.1 (the $80B equity raise and the Berkshire private
    placement); 8-K, 2026-06-05, `0001193125-26-259830` (cover and items list only: 1.01, 3.03, 5.03, the preferred).
  - DEF 14A, filed 2026-04-24, `0001308179-26-000342`: fetched and located (the director slate, the 2025 Summary
    Compensation Table); not read further, because Q5 and Q6 are NOT REACHED.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$164,713M**
  on the filed consolidated statement of cash flows (10-K FY2025) equals the tagged 164,713 that `tools/run.py` printed;
  purchases of property and equipment FY2025 $91,447M also agree.
- **`tools/run.py GOOGL --framework v5`, arithmetic lines only** (Part VII; nothing it prints as a rule, id or verdict was
  used; full output in `run_py_output.txt`). Owner cash = operating cash flow less all stock pay less all capital
  spending, USD millions:

| FY | OCF | stock pay | capex | owner cash (capex basis) | D&A basis |
|---|---|---|---|---|---|
| 2023 | 101,746 | 22,460 | 32,251 | 47,035 | 67,340 |
| 2024 | 125,299 | 22,800 | 52,535 | 49,964 | 87,188 |
| 2025 | 164,713 | 27,100 | 91,447 | 46,166 | 116,477 |

  Five-year mean (run.py's other window, capex basis): $46,997M, a yield of 1.11% on the cap against a sovereign of 5.66%.
  First half of 2026 (10-Q): OCF $84,859M, capex $80,598M, stock-pay expense $15.2B (the note's figure, not the cash-flow
  add-back; labelled so): owner cash about **minus $10.9B** for the half. The company's own free cash flow, before stock
  pay, was minus $5,855M in Q2 2026 (EX-99.1). These are recorded here as arithmetic; no valuation is made, since the run
  closes before Q7 (operator rule 3).
- **Balance sheets, ten year-ends** (run.py transcription, first-filed XBRL; read as context, the run closing before Q4):
  equity rose from $139,036M (2016) to $415,265M (2025); long-term debt from $3,935M to $46,547M, most of the rise in
  2025, and to a carrying value of **$98.2B** at 2026-06-30 (10-Q MD&A); goodwill stayed small against equity ($33,380M in
  2025). The balance sheet is moving from net cash toward debt and new equity in the same year: "over the last year,
  Alphabet has raised over $85 billion of debt across six major currencies and markets, bringing its total debt balance to
  over $100 billion" (EX-99.1, `0001193125-26-257724`).

## THE FOUNDATIONS (not a gate)
Two bear hardest. **A share is a business** **[M1997-109]**: the question is what this business's cash will be over the
holding period, not what the quotation will do, and the quotation has risen to a level ($4.2 trillion) that tells nothing
about value **[M2006-077]**. **The analyst's habits**: the first test is "What do I not know that I need to know?"
**[M1999-129]**, and the worst anchor "is always your previous conclusion" **[M2016-054]**, here a remembered Google of
capital-light search economics that the 2026 filings no longer describe. Who is paid to tell: the June 2026 equity offering
was underwritten by three banks, and the release that announced it is a selling document; its forecasts ("unprecedented
customer demand") are read as the seller's **[M1994-014]**. **Contrary evidence, written down as found** **[M1997-127]**:
(a) Search & other revenue grew from $54,190M to $63,271M in Q2 2026 over Q2 2025, with paid clicks up 13% (10-Q), so the
search franchise has not shrunk to date under generative AI; (b) Google Cloud's revenue backlog was $513.9B at 2026-06-30
and its Q2 operating income $8,814M against $2,826M a year earlier (10-Q); (c) Berkshire Hathaway bought $10B of the stock
in June 2026 and has held a position since Q3 2025 (EX-99.1, `0001193125-26-257724`); (d) the speakers saw the search economics from GEICO's side, "that's a good business, unless somebody's going to take it
away from you", and called the miss their own error, "But I blew it" **[M2017-021]**, "I feel like a horse’s ass for not
identifying Google better" **[M2019-024]**, **[M2017-080]**.

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Not by the business itself; ruin would come only from the buyer's own
conduct, borrowing to own it or sizing it so that a fall of half forces a sale **[M2012-081]**, **[L2014-005]**,
**[M2020-022]**. No purchase is reached in this run, so no financing or size is proposed; nothing in it engages the rule.
