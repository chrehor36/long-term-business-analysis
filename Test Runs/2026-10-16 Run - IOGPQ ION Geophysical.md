# Company Run: ION Geophysical Corporation (OTC Expert Market, formerly NYSE IO: IOGPQ), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the brief's stated departure (the lines of evidence are
derived by the analyst from the FY2020 10-K, below). Template copied to this dated name before any fetch (commit
`48c3e094`). SEC CIK 0000866609; named Input/Output, Inc. until 2007-09 (EDGAR submissions record, former names).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for IOGPQ, IO or ION Geophysical).

**CONTAMINATION, declared.** Before any work the session context showed recent commit subjects of the repository, among them
a fold and a run of another name (ENYN) described as "TOO HARD (NATURE) at Q1, a bankrupt filer", and a fold of another name
(CTBG), and the index lines of the operator's memory file (queue counts, gate-clearer counts). No run file, holding review,
`PORTFOLIO.md`, register or reading list was opened, listed or searched. The ENYN subject concerns a different bankrupt filer;
it was seen, it is declared, and it was not used: the box below is decided on this filer's own record and the framework's text,
and where it differs from or agrees with that subject, the reasoning is given from the text alone (see WHAT IN THE FRAMEWORK
WAS WRONG OR UNCLEAR).

**Lines of evidence chosen** (from the FY2020 10-K, filed 2021-02-12, accession 0001437749-21-002669): (1) Item 1, Business
and Competition: two segments, E&P Technology & Services (multi-client data library "Ventures" and imaging) and Operations
Optimization (software and devices), in a market the filer itself calls "highly competitive and characterized by frequent
changes in technology"; chosen because Q1 and Q2 turn on it. (2) Item 1A and Item 7, going concern: the 9.125% notes due
2021-12-15 "raise substantial doubt about our ability to continue as a going concern"; chosen because it bears on what the
share is now. (3) Item 7 and the cash-flow statement: investment in the multi-client data library, the business's main
capital spending, which `tools/run.py` did not pick up; chosen because owner cash depends on it. (4) The Chapter 11 record
(8-Ks of 2022, the confirmation order on the court docket, the FINRA notice) and the SEC revocation order; chosen because
they decide what a holder of the share owns.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** no usable quote. The NYSE suspended trading after the close of 2022-05-18 and the 8-K of 2022-05-19 (accession
  0001437749-22-013087) says the stock "may be quoted and traded on the OTC Expert Market SM under the trading symbol IOGPQ";
  the Expert Market does not publish a public quote, the aggregator route in `tools/sources.py` returns HTTP 404 for IOGPQ,
  and the SEC's revocation opinion (Release No. 98904, 2023-11-13) records the Division's allegation, deemed true, that "as of
  May 8, 2023, the common stock of Respondent was not publicly quoted or traded." The NYSE's Form 25 was filed 2022-06-03
  (accession 0000876661-22-000472).
- **Shares by class:** the last cover count is "29,617,040 shares of common stock, par value $0.01 per share, outstanding"
  (as of 2021-11-01) on the 10-Q for the quarter to 2021-09-30, filed 2021-11-03, accession 0001437749-21-025105; the same 10-Q's
  balance sheet states "outstanding 28,627,268 and 14,333,101 shares at September 30, 2021 and December 31, 2020" (the
  difference of about 1.0M between the two dates was not traced; the count doubled in 2021 through a registered sale and the
  exchange of the 2021 notes for convertible 2025 notes, 10-Q footnote 4). One share
  of Series A Preferred Stock was held by the trustee of the 2025 notes (10-Q footnote 4). `python Screens/cover_shares.py
  IOGPQ` returns "NOT AN SEC REGISTRANT in the live ticker file"; the count above is read from the filing by hand. Issued less
  treasury cannot be checked against a later filing: no 10-K for 2021 was filed. **Shares today: none.** The First Amended
  Joint Chapter 11 Plan became effective 2022-09-12, and under it "all ION Geophysical Common Interests will be cancelled,
  released, and extinguished, and will be of no further force or effect" (FINRA Uniform Practice Advisory UPC#28-22,
  2022-09-13, quoting the plan; a regulator's notice, flagged as secondary to the plan itself). The confirmation order
  (docket no. 660, Case 22-30987 (MI), filed 2022-08-18, read from the court record via the RECAP archive, flagged as a
  primary court record obtained through a third-party mirror) says the Debtors "shall be deemed to have cancelled pursuant to
  the Plan all Interests".
- **Market cap:** not computable (no quote); on the plan, nil.
- **Sovereign for the earnings currency:** 5.43%, US Treasury daily par yield curve, 30-year, 2026-10-15 (`tools/run.py`
  through `tools/sources.py`; issuing authority). The filer earned in US dollars ("The majority of our foreign sales are
  denominated in U.S. dollars", FY2020 10-K).
- **Filings read** (operator rule 4): FY2020 10-K, filed 2021-02-12, accession 0001437749-21-002669 (Items 1, 1A, 7, the
  statements and notes); FY2017 10-K, accession 0000866609-18-000006 (cash flows and segments 2015 to 2017); 10-Q to
  2021-09-30, accession 0001437749-21-025105 (balance sheet); DEF 14A filed 2021-05-14, accession 0001104659-21-066388
  (fetched, not read beyond the cover, the file having closed before Q5); 8-Ks of 2021-12-13 (0001437749-21-028423),
  2021-12-16 (0001437749-21-028758) and its re-filing 2021-12-17 (0001437749-21-028807), 2021-12-23 (0001437749-21-029204),
  2022-04-13 (0001437749-22-008791, with Exhibit 10.1, the Restructuring Support Agreement, Plan and Disclosure Statement),
  2022-04-22 (0001437749-22-009552), 2022-05-19 (0001437749-22-013087), 2022-07-08 (0001437749-22-016915), 2022-07-22
  (0001437749-22-017628); the NT 10-K filed 2022-04-01 (0001437749-22-007933); the SEC order of revocation, Release No.
  98904, 2023-11-13, Admin. Proc. File No. 3-21444 (EDGAR filing 9999999997-23-004662, 2023-11-14).
  **One figure cross-checked against the filed statement:** total net revenues 2020, $122,674 thousand on the FY2020 10-K's
  statement of operations, against the XBRL transcription of $122.7 million; and net cash provided by operating activities
  2020, $9,159 thousand on the filed cash-flow statement, against `tools/run.py`'s 9.2.
- `tools/run.py` could not resolve the delisted ticker; it was run through a wrapper that routes IOGPQ to CIK 866609 and sets
  the missing price to "NO QUOTE" (`Test Runs/_research 2026-10-16 IOGPQ/scripts/run_cik.py`; output in `run_py_output.txt`).
  Only its arithmetic lines are used. **It understates the capital spending:** it found "no intangible, software or
  mine-development payment beside capex", but the filer's largest investing outflow is "Investment in multi-client data
  library" ($27.2M in 2020, $28.8M in 2019, $28.3M in 2018), which the tool does not read. Owner cash is therefore done by hand
  below from the filed cash-flow statements.

**Facts checked against the brief's list.** All confirmed in the filings: the missed 2021-12-15 payment (8-K 2021-12-16: the
company "elected to miss the December 15, 2021 due date to pay the outstanding principal and interest (a combined total of
$7.7 million) on its 9.125% Notes"); the Chapter 11 filing on 2022-04-12 by the company and three subsidiaries (GX Technology
Corporation, ION Exploration Products (U.S.A.), I/O Marine Systems, Inc.) in the Southern District of Texas (8-K 2022-04-13);
the NT 10-K (2022-04-01), and no 10-K for 2021 in the EDGAR submissions list; the last 10-Q to 2021-09-30 filed 2021-11-03;
the suspension 2022-05-18 and the move to the Expert Market as IOGPQ (8-K 2022-05-19); the auction of 2022-06-29 and the
board's approval of the bids 2022-07-01 (8-K 2022-07-08); the First Amended Joint Chapter 11 Plan filed 2022-07-18 (8-K
2022-07-22); the revocation on 2023-11-13 (Release No. 98904). One fact to add: the brief's description of the 8-K of
2022-05-19 lists it under Item 2.04 on EDGAR, while the document heads its text "Item 2.04. Notice of Delisting", a
mislabel in the filing itself (the content is Item 3.01). Nothing has been filed since the revocation; the EDGAR submissions
record ends with the REVOKED entry of 2023-11-14.

## THE FOUNDATIONS (not a gate)
The foundation that bears is the first: a share is a business. The test is "Would I be happy buying this stock if the market
closed for five years?" **[M1997-109]**, and a share is bought for what "the asset, itself, produces", "Not by selling it to
somebody else" **[M1997-052]**. The record shows that what this share was a claim on no longer exists: the operating assets
were auctioned in June 2022 (8-K 2022-07-08), the estates were placed under a Plan Administrator to "wind down and dissolve
the Estates" (confirmation order, docket no. 660, paragraph 13), and the common interests were cancelled on the effective
date (FINRA UPC#28-22). Whatever trades under the symbol, if anything does, is not a business. The market-serves foundation
has nothing to serve here: there is no public price to be out of line with anything. **Contrary evidence, written down as
found** **[M1997-127]**: (1) the original plan of April 2022 gave the common something: "each Holder thereof shall receive
its Pro Rata share of and interest in 0.25% of the New Common Stock" (Plan, Class 9, in Exhibit 10.1 to the 8-K of
2022-04-13); the record was checked to see whether that survived, and the confirmed First Amended Plan cancelled the
interests instead (FINRA UPC#28-22; confirmation order paragraph 13). (2) The confirmation order read is the version filed on
the docket on 2022-08-18 as docket no. 660; whether the entered order differs in its equity paragraph was not checked
against the entered copy; the FINRA notice of the plan's effectiveness confirms the cancellation independently.

## THE STANDING RULE
The rule binds the buyer: "We are never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**; "Never risk permanent loss of capital." **[L2023-005]**. A purchase of a cancelled interest, at any price,
is a permanent loss of the price paid on the plan's own terms; no financing, sizing or holding of it can be squared with the
rule. Recorded; the rule governs the buyer's conduct and does not by itself close the file on the company.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable probability of being able to asses where the business
  will be in 10 years" **[M2000-037]**, "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, and the decision is made "off the figures" **[M2008-069]**.
- **The key variable, and whether it is foreseeable.** There is one: does the security carry any claim on any earning power?
  The filings and the court record answer it. The company and three subsidiaries filed Chapter 11 on 2022-04-12 (8-K
  2022-04-13); the 8-K warned that "The Company expects that its equity holders could experience a significant or complete
  loss on their investment"; the marine data and processing, software, land data, devices, and IP and inventory assets were
  sold at auction (8-K 2022-07-08); the confirmed plan vested what remained in the Debtors "under the control of the Plan
  Administrator" for "holders of Claims receiving a distribution", directed the wind-down and dissolution of the estates, and
  deemed "all Interests" cancelled (docket no. 660, paragraphs 11 and 13); the plan became effective 2022-09-12 and the common
  interests were "cancelled, released, and extinguished" (FINRA UPC#28-22); the registration of the securities was revoked on
  2023-11-13 (Release No. 98904). Where the business will be in ten years is therefore not a forecast at all: the
  business left the company's hands in 2022 and the share's claim on it was extinguished by court order.
- **Which reading of the test.** The question is important and it is knowable, and it has been answered: "things that are
  important and knowable" **[M2006-076]**. Test 5, would the insiders write the forecast down **[M2000-105]**, is met in the
  plainest way: the debtors, the creditors and the court wrote it down, in the plan. There is no doubt about the perimeter to
  trigger the doubt rule **[M2002-092]**. So this is not TOO HARD of either cause: not WORK (no knowable question is left
  unread), not NATURE (no industry forecast is needed, because the share does not depend on the industry any more).
- **The routing check.** Had the share still been a claim on the operating business, Q1 would have had to face the filer's own
  description of its field, "highly competitive and characterized by frequent changes in technology" (FY2020 10-K, Item 1,
  Competition), which the routing sends to TOO HARD at Q1 where change puts the ten-year economics out of reach
  **[M1998-008]**, **[L1993-023]**. That reading is recorded and not applied, because the thing on offer is not that business.
- **VERDICT: IN.** The position is understood with certainty from the filings and the court record: a cancelled interest in
  a dissolved estate whose operating assets belong to others **[M2000-037]**, **[M2006-076]**, **[M2008-069]**. The file
  passes to Q2, where the castle question is put to what the share now owns. (Why IN and not OUT here is argued in WHAT IN
  THE FRAMEWORK WAS WRONG OR UNCLEAR.)

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. It is put twice: to what the share owns today, and to the business as it stood in its
last filed decade, because the second is the evidence on whether the first could ever have been otherwise.

- **What the share owns today.** No castle. The operating assets were auctioned on 2022-06-29 and the bids approved on
  2022-07-01 (8-K 2022-07-08); the confirmation hearing order names "the TGS Sale Transaction", so at least one named rival
  bought part of the business (docket no. 660, recital d); the two segment heads were "released from employment" on 2022-07-08
  (same 8-K); the estates are in wind-down under a Plan Administrator and "all Interests" are deemed cancelled (docket no. 660,
  paragraph 13). A castle sold to the attacker is the plainest case of "If the answer had been yes, we wouldn’t have done it."
  **[M2011-015]**.
- **The castle tests on the last filed decade** (FY2011 to FY2020, each year's operating income and revenue from that year's
  10-K by XBRL transcription, `peers_output.txt`; 2016 to 2020 checked against the filed statements):
  - *The attacker with money.* The filer says of its two main rivals in imaging that "Both of these companies are
    significantly larger than ION in terms of revenue, processing locations and sales, marketing and financial resources"
    (FY2020 10-K, Item 1, Competition). One of them, through WesternGeco, held patents ION was found to infringe; the
    "decade-long patent litigation" ended only on 2020-04-07 with a licence and the lifting of "the injunction that prevented
    the Company from manufacturing DigiFIN ® in the United States" (FY2020 10-K, footnote 9); the 2016 cash flow carries a
    "$20.8 million damages payment" for it (FY2017 10-K, Item 7).
  - *Pricing power and the low-cost position.* No year of operating profit from 2014 to 2020: operating margin -23.1%, -45.4%,
    -25.0%, -4.4%, -30.1%, -14.0%, -11.9% (2014 to 2020), after 14.7%, 14.2% and 3.0% in 2011 to 2013. Over the ten years the
    filer's operating income sums to about -$206M on about $3,109M of revenue. Revenue fell from $549.2M (2013) to $122.7M
    (2020). A business whose rivals set the terms and which cannot earn its costs through a cycle is the high-cost producer in a
    field where "the low-cost producer can put you out of business" **[M1997-010]**.
  - *Widening or narrowing.* Narrowing to nothing: retained deficit -$424M (2011) to -$1,012M (2020); stockholders' equity
    $425M to -$73M (10-year balance-sheet table, `run_py_output.txt`, from each year's first-filed XBRL); a going-concern
    doubt in the FY2020 10-K; default on the 2021 notes; Chapter 11.
  - *Change.* The filer's own words: a market "highly competitive and characterized by frequent changes in technology"
    (FY2020 10-K, Item 1). "A moat that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**; the
    multi-client library had to be refilled every year ($14.9M to $28.8M of investment a year, 2016 to 2020) and was written
    down in 2017, 2019 and 2020 (impairments of $2.3M, $9.1M and $1.2M on the filed cash-flow statements).
- **The competitor row** (operating income over revenue, each from its own filings; `scripts/peers.py`):

  | Company | Filing | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 |
  |---|---|---|---|---|---|---|---|
  | ION (filer) | 10-Ks, e.g. 0001437749-21-002669 | -45.4% | -25.0% | -4.4% | -30.1% | -14.0% | -11.9% |
  | CGG (named rival; Sercel is its subsidiary) | 20-F FY2017, 0001193125-18-101439 | -55.1% | -33.2% | -20.0% | no SEC filing after the FY2017 20-F | | |
  | Schlumberger (named rival) | 10-Ks, e.g. 0001564590-21-002477 | 18.4% | 11.8% | 12.9% | 12.8% | 12.1% | 10.2% |
  | Geospace Technologies (named rival of INOVA in land equipment) | 10-Ks, e.g. 0001564590-20-054742 | -61.9% | -89.4% | -73.7% | -27.4% | 1.1% | -20.5% |

  Flags: Schlumberger's figure is the whole oilfield-services company, of which seismic is a small part, so it shows the
  customer-facing scale advantage, not a seismic margin; Geospace's fiscal year ends in September and its XBRL years are taken
  as filed. **Named rivals that do not file with the SEC:** TGS, PGS, Shearwater, Polarcus and BGP. The only named seismic
  specialists with SEC filings over the span, CGG and Geospace, lost money in most years shown, as ION did.
- **The parts table** (segment income from operations before support and other; FY2017 10-K for 2016 and 2017, FY2020 10-K
  for 2018 to 2020; $M):

  | Part | 2016 | 2017 | 2018 | 2019 | 2020 | five-year sum | share of the positive sum | castle | decides |
  |---|---|---|---|---|---|---|---|---|---|
  | E&P Technology & Services | -16.4 | 42.5 | 21.8 | 8.8 | 13.1 | 69.8 | about 71% | open (above) | yes |
  | Operations Optimization | 9.7 | 8.0 | 7.3 | 8.2 | -4.6 | 28.6 | about 29% | not judged | no |
  | Ocean Bottom Seismic Services, later "Other" | -1.8 | -16.3 | in support and other | | | | | | no |

  "Support and other" was -$83.3M, -$41.5M and -$23.2M in 2018 to 2020, so no part's profit covered the company's costs.
  The deciding part closes the file **[L2008-005]**.
- **The field's returns over the last full cycle.** From 2011 (before the oil-price peak) to 2020 (a trough the filer
  attributes to COVID-19 and "reduced E&P spending levels", FY2020 10-K, Item 7), the filer's and the two filing seismic
  rivals' own statements show losses through most of the cycle. Judged in words, as the convention asks: not ordinary returns
  but negative ones; "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. A castle
  that protected excellent returns **[L2007-004]** is not in this record.
- **Price does not reopen it.** "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**;
  "If you really think a business is declining, most of the time you should avoid it." **[M2012-062]**. The cigar butt "that
  had one puff remaining in it" **[L2014-006]** is the generous case; this one has none, the puff having gone to the creditors
  under the plan.
- **VERDICT: OUT.** The castle is shown open on the evidence: it did not protect any return through the last full cycle,
  and it has since been sold to others while the share's claim was cancelled **[M2011-015]**, **[L2007-004]**,
  **[M2013-052]**, **[M1997-010]**. Not TOO HARD: the future of the castle is not unjudgeable **[M2000-019]**; it is known.

## Q3 to Q12: NOT REACHED
Q2 closed the file OUT (operator rule 2). Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are NOT REACHED. What follows under
COMPUTATION and AFTER THE STOP is recorded, not weighed.

---
## COMPUTATION, NOT A CLEARANCE (the owner's two reporting figures, after the Q2 STOP)
*Reporting convention of the brief and of Part VII, The owner's price; neither figure is a verdict or entry language
(operator rule 3). Arithmetic in `Test Runs/_research 2026-10-16 IOGPQ/scripts/compute.py`, output `compute_output.txt`.*

**Owner cash after every real cost, by year ($M), from the filed cash-flow statements** (2016 and 2017: FY2017 10-K,
0000866609-18-000006; 2018 to 2020: FY2020 10-K, 0001437749-21-002669): operating cash flow, less stock-based compensation,
less purchases of property, plant and equipment, less investment in the multi-client data library.

| Year | Operating cash | Stock pay | PP&E | Library investment | Owner cash, equity-only (after interest) | Interest paid | Owner cash, all-equity (before interest) |
|---|---|---|---|---|---|---|---|
| 2016 | 1.571 | 3.267 | 1.488 | 14.884 | -18.068 | 15.691 | -2.377 |
| 2017 | 28.030 | 2.552 | 1.063 | 23.710 | 0.705 | 14.181 | 14.886 |
| 2018 | 7.098 | 3.337 | 1.514 | 28.276 | -26.029 | 12.463 | -13.566 |
| 2019 | 34.150 | 4.701 | 2.411 | 28.804 | -1.766 | 12.381 | 10.615 |
| 2020 | 9.159 | 2.043 | 1.121 | 27.247 | -21.252 | 12.520 | -8.732 |
| mean | | | | | **-13.282** | | **0.165** |

Notes on the inputs. The library investment is the business's main capital spending (it is how the Ventures business makes
its product); library amortization ran above it in 2018 and 2019 ($49.0M and $39.5M against $28.3M and $28.8M) and below it in
2020 ($22.3M against $27.2M), so no maintenance case lower than the spending itself can be stated from the filing, and
specific (e) is not applied: the all-spending case is the only case. The company's own tax is the same on both bases: it paid
foreign income taxes ($4.5M, $7.0M, $3.3M, $11.1M, $8.2M, 2016 to 2020, inside operating cash) while losing money before tax,
so the interest added back carries no tax shield to remove; said so rather than computed. The 2016 operating cash includes the
$20.8M WesternGeco damages payment; it is a real cost of the business and is kept. The 2020 operating cash includes the
Paycheck Protection Program effect (FY2020 10-K: "Receipt of Paycheck Protection Program loan" of $6.9M in financing and
"Amortization of government relief funding expected to be forgiven" of -$6.9M among the operating adjustments) and is kept as
filed. The XBRL transcription used by `tools/run.py` gives 2016 and 2017 operating cash as 1.0 and 27.6 (a later filing's
recast); the FY2017 10-K's own 1,571 and 28,030 thousand are used. The FY2017 10-K's MD&A calls 2016 both "net cash used in
operating activities of $1.6 million" and "Net cash provided by operating activities was $1.6 million for 2016"; the statement
shows 1,571 provided.

**Window and growth, by Q7's specifics.** (a) The window 2016 to 2020 runs trough to trough on the filer's own description
(2016 revenue down 22% on 2015, FY2017 10-K; 2020 down 30% on COVID-19 and "reduced E&P spending levels", FY2020 10-K), so the
cycle base is the window itself, and the literal window is the same figures. (b) The all-equity series changes sign; measured
between the half-window averages (2016 to 2017: 6.255; 2019 to 2020: 0.941) it declines at about -46.8% a year, which is
carried as the bottom of the range, the no-growth case as the top. The equity-only series is negative in both halves and its
rate is meaningless, so its range is the no-growth case alone, said so. (c) No acquisitions in the window. (d) Working capital
is inside operating cash as filed. (f) No cap is needed; nothing grows.

**Net debt** at the latest filed date, 2021-09-30 (10-Q, 0001437749-21-025105): current maturities of long-term debt $26.447M
plus long-term debt $107.379M, less cash $24.143M = **$109.683M**; operating leases left out (current $8.263M, and the
long-term part inside "Operating lease and other long-term liabilities" of $32.509M) and said so. Subsequent events the record
states: the default of 2021-12-15 and the acceleration on filing of "$15.6 million" under the credit agreement and "$116.2
million" of 2025 notes (8-K 2022-04-13); these raise, not lower, the debt. Shares: 29,617,040 (last cover).

**(a) VALUE RANGE** at the 5.43% Treasury rate, ten years then zero nominal growth: whole business $0.17M (decline case) to
$3.04M (no-growth case); **per share, all-equity basis: about -$3.70 to -$3.60** (whole-business value less net debt, over
29,617,040 shares). **Equity-only, beside it: about -$8.26 a share** (no-growth case alone). Against: **no usable price.** The
floor test: no case earns ten percent at any positive price, so the computation would close OUT before the width is looked at
(Q7, the floor tested first; "there’s just a point at which we drop out of the game" **[M2003-149]**). The width test does not
arise.

**(b) FAIR PRICE** (each end case valued at ten percent, the two averaged, after the company's own tax): **all-equity, about
-$3.67 a share** (ends $0.16M and $1.65M of whole-business value, less net debt); **equity-only, about -$4.48 a share**.
Both are negative; there is no positive price at which the midpoint earns the floor. On the plan's terms the share's legal
claim is nil whatever these figures say: the computation is of the business as last filed, not of anything a buyer of the
symbol could own.

## THE BALANCE SHEETS, EIGHT TO TEN YEARS (read in Step 0 because the file closed before Q4)
The table in `run_py_output.txt` (first-filed XBRL, FY2011 to FY2020, transcription; the 2020 and 2021-09-30 figures checked
against the filed statements above) was read before the income account **[M2025-032]**. What moved: total assets $674M to
$194M; stockholders' equity $425M to -$73M; the retained deficit from -$424M to -$1,012M, about $588M of losses in nine
years; goodwill $54M to $20M and intangibles $18M to nil (with a $4.2M goodwill impairment in 2020); cash $42M to $37M, held
roughly flat only by borrowing ($27.3M drawn on the revolver in 2020) and by issuing stock ($47.0M in 2018; in 2021 a
registered sale and the note exchange took the count from 14.3M to 29.6M); inventory $70M to $11M as revenue fell from $455M
to $123M; balance-sheet debt between about $105M and $220M throughout (2013 peak), the 2021 notes current at 2020-12-31
($143.7M current maturities). What the figures say: a decade in which the business consumed its equity and its owners' new
money. What they do not say: what the multi-client library was worth; its carrying value ($50.9M at 2020-12-31, $56.5M at
2021-09-30) was written down in three of four years, and what it fetched at auction was not found in a primary document.

## THE BOX
**OUT at Q2** (the castle shown open on the evidence: no return protected through the last full cycle, the operating assets
sold to others in 2022, the common interests cancelled under the confirmed plan effective 2022-09-12). COMPUTATION on the
filed record: value about -$3.70 to -$3.60 a share all-equity (-$8.26 equity-only), fair about -$3.67 all-equity (-$4.48
equity-only), no usable quote. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).*
- **Q4 (the accounts).** The FY2017 10-K's MD&A features figures "as adjusted" beside GAAP: "our loss from operations was $2.6
  million , as adjusted, compared to a loss of $41.2 million , as adjusted, for 2016", and a segment table with an adjustment
  column (FY2017 10-K, Item 7); the GAAP loss from operations for 2017 was $8.7M (XBRL, same filing). An adjusted figure
  featured is a weighing against at Q4, carried to Q5 **[L2016-006]**. The same MD&A states 2016 operating cash both as
  "used" and as "provided" (above). Library impairments in 2017, 2019 and 2020.
- **Q5 (integrity, flagged).** The company "elected to miss" the 2021-12-15 payment of principal and interest on the 2021
  notes and the interest on the 2025 notes, "in order to protect the value of the enterprise and preserve liquidity" (8-K
  2021-12-16), days after an 8-K of 2021-12-13 announcing it had regained NYSE compliance. It filed no 10-K for 2021 after an
  NT 10-K giving as reason "delays in its preparation of its financial statements" (2022-04-01), and the Commission found it
  in default, deemed the allegations true, and revoked registration for failure to file periodic reports; it answered neither
  the order instituting proceedings nor the order to show cause (Release No. 98904). The filer was in "decade-long patent
  litigation" with WesternGeco, under an injunction against U.S. manufacture of DigiFIN until the 2020 settlement, and paid
  $20.8M of damages in 2016 (FY2020 10-K, footnote 9; FY2017 10-K, Item 7). Doubt closes at Q5 **[M2013-088]**; these facts
  are for any later run that reaches Q5 to answer.
- **Q6 (the money and the owners).** Share count about doubled in 2021 (14,333,101 to 28,627,268 on the balance sheet) through
  a registered sale of 2,990,001 shares (securities purchase agreement of 2021-02-16, 10-Q to 2021-09-30) and the exchange of
  the 2021 notes into 8% convertible 2025 notes convertible at about $3.00 a share; $47.0M of stock issued in 2018; no buybacks
  and no dividends in the window.
- **Q9 (debt).** Notes of $120.6M due 2021-12-15 described as raising "substantial doubt about our ability to continue as a
  going concern" (FY2020 10-K, Item 1A); $133.8M of debt against $24.1M of cash at 2021-09-30; accelerated on the filing.
- **Q12.** Nothing found that bears on it.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 48c3e094); written question by question; committed after Q1 and
      after Q2, and at the close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's. The fold is the
      dispatcher's; a run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the commit subjects and memory index
      lines seen at session start are declared under CONTAMINATION and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `scripts/check_ids.py`, output `check_ids_output.txt`); every filing fact carries its accession, docket or release
      number; the court docket and the FINRA notice are flagged as to their channel.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; every figure after it is under COMPUTATION.
- [x] Owner cash after every real cost from the filed cash-flow statements, the library investment included, never a
      net-income proxy; the sovereign from the US Treasury; no aggregator quote exists and none is used.
- [x] Contrary evidence written as found (the April 2022 plan's 0.25% to the common; the proposed order read from the
      docket); facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its missing library spending is declared and corrected by hand.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The framework has no route for a security that no longer exists. Every question is written for a going business, and a
cancelled interest in a dissolved estate fits each box awkwardly. Three readings were open. **Q1 TOO HARD (NATURE)**: rejected,
because NATURE is defined as a forecast the industry's own insiders would not write down, and here the debtors, the creditors
and the court wrote the outcome down in the plan; nor WORK, since nothing knowable is left unread. **Q1 OUT**: tempting, since
section I says OUT means "a question has been answered against it"; but Q1 asks whether the analyst can understand the
position, and the position is understood with certainty, so an OUT at Q1 would be a judgment of the business's worth, which
belongs to Q2 and Q7. **Q1 IN, Q2 OUT** was chosen: understanding passes, and the castle question is answered against the name
on the evidence of the last decade and of the sale. A one-line rule would settle it for every later bankrupt or cancelled
filer, for instance "a security cancelled under a confirmed plan, or whose registration is revoked with nothing filed since,
closes at [question] in [box], the plan or the revocation order being the filing fact"; which question and which box is a
structural choice for the operator (PRIME RULE 5). Another session reading the same text could defensibly pick a different
box, and that inconsistency is the defect worth fixing. Two further gaps: (1) the two reporting figures are defined for a
share that exists; for a cancelled one they can only be computed on the business as last filed, they come out negative, and
the brief's "against the price" has no price to set them against; (2) `tools/run.py` does not read "Investment in
multi-client data library" as capital spending, so for a seismic or data-library company its owner-cash lines overstate owner
cash by the whole library investment, and its ticker lookup cannot resolve a delisted filer by CIK.
