# Company Run: Everforth, Inc. (formerly ASGN Incorporated) (NYSE: EFOR), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not known to this analyst. The run was dispatched blind: `PORTFOLIO.md`
was not opened, by instruction, so whether the operator holds this name is not stated here.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, the prepped reading list, any other `Test Runs/` file on this company, other companies'
2026-10-05 run or research files, the unadopted gaps case. Seen without opening: (1) a directory listing of `Test Runs/`
showed a file named `2026-07-16 Run - Services & Payments 5-pack (MAN WU EPAM G EFOR).md`; its name was read, its
contents were not (a listing for the former ticker ASGN found no file); (2) the five most recent commit subjects in the
session header (CAG, GIII, HOS runs closing OUT at Q2; a small-cap triage screen; a session-state commit). None names this
company. (3) The task brief named the screen's owner-earnings yield (16.6% to 20.9%). Nothing else about this name from
inside the repository was seen.

**Identity.** SEC EDGAR `company_tickers.json` maps EFOR to CIK 890564, "Everforth Inc". EDGAR's submissions record lists
former names ASGN Inc (2018-04-02 to 2026-04-22) and ON ASSIGNMENT INC (1996 to 2018). The 8-K of 2026-04-24 (accession
0000890564-26-000025), Item 5.03: "On April 24, 2026, ASGN Incorporated (the “Company”) changed its corporate name to
Everforth, Inc." and the ticker moved from ASGN to EFOR on the NYSE that day. A rename, not a merger; no stockholder vote
was needed. Business: IT staffing and IT consulting to Fortune 1000 companies (Commercial segment: Apex Systems, Creative
Circle, CyberCoders, GlideFast, TopBloc, and from March 2026 Quinnox) and IT services to US federal agencies (Federal
Government segment: ECS). Glen Allen, Virginia; incorporated 1992 (10-K FY2025, accession 0000890564-26-000013, Item 1).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $36.32 (2026-10-05 intraday, `tools/run.py`, aggregator, live quote only, flagged per operator rule 5). A
  second aggregator read the same day showed $36.14; the closes of 2026-09-22 to 2026-10-02 ran $32.28 to $36.19
  (aggregator). The price is used at $36.32.
- **Shares by class** from the latest filing's cover: one class, common stock, **41.0 million** outstanding at
  2026-07-24 (10-Q for the quarter to 2026-06-30, filed 2026-07-31, accession 0000890564-26-000050, cover:
  "At July 24, 2026, the total number of outstanding shares of the Common Stock of Everforth, Inc. [...] was 41.0
  million."). `python Screens/cover_shares.py EFOR` returned 890,564,000,000, which is the CIK read as a share count, a
  parse failure; the cover was read by hand. Balance sheet at 2026-06-30: 40.9 million; 75.0 million authorized; no
  preferred issued.
- **Market cap:** 41.0M x $36.32 = **$1,489M**.
- **Debt at 2026-06-30** (10-Q, Note 5): $1,451.8M principal (revolver $318.0M, term loan A $97.5M, term loan B $486.3M,
  4.625% senior notes due 2028 $550.0M); cash $152.9M; net debt about **$1,299M**. Enterprise value about $2,788M.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-25, accession 0000890564-26-000013): Item 1, Item 1A,
  Item 7, cover; 10-Q Q2 2026 (filed 2026-07-31, accession 0000890564-26-000050): statements and Notes 1 to 9, MD&A;
  10-Q Q1 2026 (accession 0000890564-26-000037); proxy DEF 14A (filed 2026-04-27, accession 0000890564-26-000031);
  8-Ks of 2026-04-24 (rename), 2026-07-09 (credit agreement amendment, accession 0000890564-26-000045), 2026-07-29
  (Q2 results, accession 0000890564-26-000047), 2025-07-31 (accession 0000890564-25-000042), 2025-03-06 (accession
  0000890564-25-000014).
- **One figure cross-checked against the filed statement:** FY2025 net cash from operating activities, $327.9M in the
  XBRL series printed by `tools/run.py`, matches the 10-K MD&A text: "Net cash provided by operating activities was
  $327.9 million in 2025, compared with $400.0 million in 2024." (accession 0000890564-26-000013). FY2025 revenue
  $3,980.4M (XBRL) matches the MD&A segment table ("Consolidated | $ | 3,980.4").
- `python tools/run.py EFOR`, arithmetic lines only (USD millions; owner cash = OCF less stock pay less capex, and the
  depreciation-and-amortization variant beside it):

  | FY | OCF | SBC | D&A | capex | OCF-SBC-capex | OCF-SBC-D&A |
  |---|---|---|---|---|---|---|
  | 2021 | 193.7 | 52.7 | 89.6 | 34.7 | 106.3 | 51.4 |
  | 2022 | 307.8 | 49.3 | 91.4 | 37.5 | 221.0 | 167.1 |
  | 2023 | 456.9 | 44.0 | 100.3 | 39.9 | 373.0 | 312.6 |
  | 2024 | 400.0 | 42.3 | 96.3 | 35.3 | 322.4 | 261.4 |
  | 2025 | 327.9 | 47.9 | 113.5 | 39.8 | 240.2 | 166.5 |
  | 5-yr mean | | | | | 252.6 | 191.8 |

  (2021 and 2022 rows from the XBRL company facts, accessions in the tool's balance-sheet list; the tool's five-year
  means, 252.6 and 191.8, match.) The tool printed no securities line in operating cash, no other stock-pay line, no
  intangible, software or mine payment beside capex. Yields at $1,489M: 16.96% (capex basis, five-year), 12.88% (D&A
  basis, five-year); the three-year means give the screen's 20.94% and 16.58%. **Neither is an owner-cash figure yet:**
  the series is before acquisitions ($304.1M in 2025 for TopBloc, $283.6M in H1 2026 for Quinnox, $484.6M in 2022,
  $222.8M in 2021), and D&A here includes $58M to $72M a year of amortization of acquired customer lists. Read at Q4.

## THE FOUNDATIONS (not a gate)
Three foundations bear on this name. **The market serves, it does not instruct:** the 10-K cover gives the stock held by
non-affiliates a market value of $2.1 billion at 2025-06-30, and the whole company is quoted at about $1.49 billion
today; the fall "doesn’t tell us anything. It just tells us prices." **[M2006-077]**, and it is read as a price, not as a
finding about the business. **Who is paid to tell you:** the one forecast in the documents that says the business will
do well out of the technology now changing its industry comes from the seller of the service, the chief executive in his
own earnings release ("We believe that the last mile of the AI valuation equation will be IT services", 8-K exhibit 99.1,
2026-07-29, accession 0000890564-26-000047); "don’t ask the barber whether you need a haircut" **[M2011-083]**. **The
analyst's habits:** the screen yield (16.6% to 20.9% on owner cash) is a reason the name was sent, and the analyst's
incentive is to find it cheap; the work looked "for what’s wrong in things" **[M2025-013]** and stated the opposing case at
Q1 before rejecting it **[M2016-055]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) Commercial
consulting bookings were $1,522.8M in 2025 against $1,281.3M in 2024, a book-to-bill of 1.2 to 1 (10-K, MD&A), and
consulting revenue rose 14.4% (part of it TopBloc, acquired March 2025); (2) Technology, Media and Telecom revenue rose in
Q2 2026 ($144.7M against $137.0M, 10-Q Note 9); (3) Q2 2026 revenue and adjusted earnings came in above the company's own
guidance (exhibit 99.1); (4) a direct rival, Kforce, writes that AI "will continue to drive higher levels of demand for
technology resources" (10-K FY2025, accession 0000930420-26-000007); (5) the Federal segment carries $2.9 billion of
contract backlog, 2.5 times its revenue (10-K, MD&A). Each is weighed at Q1.

## THE STANDING RULE
A part-interest in a listed company, bought for cash, unborrowed, and sized so that its total loss would not touch what
the buyer has and needs, puts the buyer at no risk of ruin: "We are never going to risk what we have and need for what we
don’t have and don’t need." **[M2012-081]**

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years. So I’ve got some notion of how the industry will develop and
where the company will stand within the industry." **[M2012-065]** The first step is "trying to identify the key variables
in that particular business, and evaluating how predictable they were first" **[M1998-044]**.

**What the business is, from the filings.** Everforth rents out technical people by the hour and sells IT projects built
by the same people. "In 2025, we employed approximately 19,600 billable professionals on a full-time-equivalent basis"
(10-K, Item 1). Costs of services "consist primarily of compensation for our billable professionals" (10-K, MD&A).
"Approximately 90% of Commercial Segment revenue was generated from time-and-materials" contracts (10-Q Q2 2026, Note 9).
Revenue 2025: Commercial $2,790.2M (70%), of which consulting $1,290.1M and assignment (staff placed on client projects)
$1,500.1M; Federal Government $1,190.2M (30%), all of it consulting to defense, intelligence, national-security and
civilian agencies (10-K, MD&A segment table). Virtually all revenue is earned in the United States.

**The key variables** **[M1998-044]**. Two: (1) the number of hours of technical work, mostly software and data work, that
large companies and federal agencies will buy from outside firms; (2) the spread the firm keeps on each hour (consolidated
gross margin 28.9% in 2025; Commercial 32.8%, Federal 19.7%; 10-K, MD&A). The second has moved slowly: 32.6% in 2016,
29.9% in 2022, 28.9% in 2025, 28.3% in Q2 2026 (XBRL gross profit over revenue; the 10-Q). The first is the whole
question.

**Is the first variable foreseeable ten years out?** The technology now moving through the industry does the very work
that is billed. The filer says so in its own risk factors: "We have been integrating AI into our business and services
in both the commercial and government markets to meet client demand and to maintain competitiveness in a highly
competitive and rapidly evolving market. [...] If we are unable to quickly develop, adopt, and deploy AI technologies, we
risk falling behind our industry competitors." and "Our success depends on our ability to keep pace with rapid
technological changes in the development and implementation of our services." (10-K FY2025, Item 1A, accession
0000890564-26-000013). The company renamed itself in April 2026 from a staffing parent to "a technology and digital
engineering company" (10-Q Note 1), and the mix moved from assignment to consulting: assignment revenue fell 13.8% in 2025
while consulting rose (10-K, MD&A). The industry's own insiders, in filings made the same month, disagree on the sign:

| Who | Filing | What it says of AI and the demand for its hours |
|---|---|---|
| EPAM Systems (digital engineering) | 10-K FY2025, filed 2026-02-26, accession 0001352010-26-000015, Item 1A | "AI, large language model, and machine learning technologies enable clients and potential clients to develop, customize, and maintain software solutions internally and could reduce reliance on third-party service providers such as EPAM [...] Our current and prospective clients have and may continue to use AI-powered tools to create or modify software applications themselves, or elect to replace traditional software with agentic AI, rather than purchasing our services" |
| Kforce (technology staffing) | 10-K FY2025, filed 2026-02-20, accession 0000930420-26-000007 | "Over the long term, we believe that AI and other innovative technologies will continue to drive higher levels of demand for technology resources and that the pace of change will accelerate." |
| Everforth (this company) | 8-K exhibit 99.1, 2026-07-29, accession 0000890564-26-000047 | "We believe that the last mile of the AI valuation equation will be IT services" |

None of the three writes a number. The test the framework sets is whether the insiders would put the forecast down:
"they would not want to put down on paper their predictions about where 10 companies you would choose in the tech field
would be in 10 years, in terms of their economics. They would say, “That’s too hard.”" **[M2000-105]**. Here three of
them, writing within months of each other, point in opposite directions and none commits a figure.

**Do the past statements tell me the future ones?** **[M2008-033]** The record does not separate the cycle from the
change. Revenue was $4,581.1M in 2022 and $3,980.4M in 2025 (XBRL, first-filed), down 13% while $304.1M was spent on
TopBloc; H1 2026 revenue was $1,975.3M against $1,988.9M, down 0.7% while $283.6M was spent on Quinnox (10-Q). Operating
income fell from $409.5M (2022) to $230.3M (2025) and was $68.8M in H1 2026 against $106.2M (10-Q). The filer attributes
the fall to "adverse macroeconomic conditions, including, but not limited to, increasing interest rates, tariffs, efforts
by the Department of Government Efficiency ("DOGE"), and a government shutdown" (10-K, Item 1A). A direct rival says
clients have already chosen AI tools over its services (above). Three years of figures cannot say which reading will
govern the next ten, and the filings disclose no acquired-revenue figure from which an organic rate could be read (no
instance found in the 10-K, the two 2026 10-Qs or the Q2 release, by a search for "organic", "pro forma" and the acquired
companies' names beside "revenue").

**The industry, not only the company, moved.** Same metric, from each company's own 10-K filings (XBRL company facts,
first-filed values; operating margin = operating income over revenue):

| Operating margin | 2016 | 2019 | 2022 | 2025 |
|---|---|---|---|---|
| Everforth (EFOR) | 7.8% | 8.1% | 8.9% | 5.8% (H1 2026: 3.5%) |
| Kforce (KFRC) | 4.5% | 5.6% | 6.8% | 3.8% |
| Robert Half (RHI) | 10.6% | 10.2% | 12.3% | 1.4% |
| EPAM (EPAM) | 11.5% | 13.2% | 11.9% | 9.5% |
| SAIC (federal IT; fiscal years end about February) | 5.9% | 5.8% | 6.5% | 7.2% |

The rivals that rent technical hours to companies fell together from 2022, as Everforth did; only the federal contractor
held. The forecast at issue is therefore one about the industry's demand, which no participant has written down, not one
about this company's execution, which more work could read.

**The opposing case, stated as strongly as I can** **[M2016-055]**. The company (On Assignment until 2018, ASGN until
2026) has rented technical and professional people since its incorporation in 1992 (10-K, Item 1), through offshoring,
the internet, mobile and the cloud, and each wave raised the demand for people to build and connect the new systems;
Kforce and the chief executive argue AI will do the same. The spread business itself is simple: an hour bought, an hour
sold, about 29 cents of each revenue dollar kept, little fixed capital (capex $39.8M on $3,980.4M of revenue in 2025). A
third of revenue is federal work under three-to-five-year contracts with $2.9 billion of backlog. Commercial consulting
bookings ran at 1.2 times revenue in 2025. **Why it does not carry.** The earlier waves changed what was built; this one
is sold on changing who, or what, does the building, and a rival in the same trade states in its own filing that some
clients have already substituted. The simplicity of the spread is not the predictability of the hours: "Oh, we understand
the product. We understand what it does for people. We just don’t know the economics of it 10 years from now."
**[M2000-104]**. The federal backlog is mostly unfunded ($2,455.6M of $2,948.5M is negotiated unfunded; 10-K, MD&A), its
new awards ran 0.9 to 1 in 2025 and 0.8 to 1 on the trailing twelve months to Q2 2026 (exhibit 99.1), and the 70%
Commercial segment carries the question either way. The contrary items written down at the foundations (bookings, TMT
growth, a guidance beat, Kforce's view, the backlog) are each a year's evidence or an insider's belief; none is a
ten-year forecast.

**The routing.** The framework fixes it: a business whose ten-year economics cannot be foreseen because its industry
changes fast closes at Q1 in TOO HARD (Q1, What understanding means). The rows behind it: "where we think the future
technology could hurt the business as it presently exists" [...] "it won’t make it through the filter." **[M1998-008]**;
"a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its
long-term economics." **[L1993-023]**; "whenever we look at a business and we see lots of change coming, 9 times out of
10, we’re going to pass on that." **[M1999-063]**. The forecast is about what a technology will do to the hours, not about
the habits of a customer **[M2017-019]**, and the industry's winners cannot be named: "there’s industries we know that may
have a wonderful future, but we don’t have the faintest idea who the winners will be" **[M2012-067]**; "Just because
Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge what its profit margins and
returns on capital will be as a host of competitors battle for supremacy." **[L2009-005]**. The edge of the circle is drawn
on doubt: "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**

**Which cause: NATURE, not WORK.** The test between them is whether the insiders would write the forecast down (section I,
the two causes; Q1 test 5, **[M2000-105]**). They would not and do not: three of them, opposite signs, no figure. The
deciding question is important but not knowable from where any analyst stands, "If something’s important but unknowable,
forget it." **[M2006-076]**, and more reading does not cure it: "We couldn't solve this problem, moreover, even if we were
to spend years intensely studying those industries." **[L1993-023]**; "Our problem -- which we can't solve by studying up
-- is that we have no insights into which participants in the tech field possess a truly durable competitive advantage."
**[L1999-018]**. The work that could be done (a decade of segment hours and bill rates, organic rates if a later filing
gives them, rivals' headcounts) would describe the past more finely; it would not supply the ten-year demand for hours
that the insiders themselves decline to state, so no research pass is opened. A lower price does not reopen it: "It
doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we
don’t know how to evaluate it." **[M2000-038]**

**What the analyst does not claim.** That the business will shrink; that AI will cut its hours; that the chief executive
is wrong. The claim is narrower: neither the filer, nor its rivals, nor this analyst can say where its earning power will
be in ten years, and the first filter asks exactly that **[M2000-104]**, **[M2012-065]**.

- **VERDICT: TOO HARD (NATURE).** The ten-year demand for rented technical hours, the business's key variable, turns on a
  technology its own industry's insiders forecast in opposite directions and will not put a number to **[M2000-105]**,
  **[M1998-008]**, **[L1993-023]**, **[M2002-092]**; in the rows' three boxes, "too hard" **[M2006-013]**. The file closes
  here.

---
## Q2 TO Q10 AND Q12: NOT REACHED
The hard sequence closes the run at Q1 (operator rule 2). Nothing below is a clearance. What follows was computed at the
owner's request for reporting and is headed accordingly.

---
## RECORDED AFTER THE CLOSE: COMPUTATION — NOT A CLEARANCE
*Everything in this section was produced after the Q1 STOP closed the file. It carries no entry language, answers no
question and does not reopen Q1 (operator rule 3). Where a row is named it locates the framework's method, not a verdict.*

### A. The balance sheets, ten year-ends and the latest quarter (what the Q4 read would start from)
USD millions; 2016 to 2025 from `tools/run.py` (first-filed XBRL vintages, accessions 0000890564-17-000046 to
0000890564-26-000013), 2026-06-30 from the 10-Q (accession 0000890564-26-000050). Tangible equity = equity less goodwill
less identifiable intangibles. Receivable days = year-end receivables over that year's revenue times 365 (2026: over
trailing-twelve-month revenue of $3,966.8M). The 2016 to 2020 figures include Oxford Global Resources, sold in 2021 for
$503.8M (XBRL, ProceedsFromDivestitureOfBusinesses).

| Year-end | Equity | Goodwill | Intangibles | Tangible equity | Cash | Receivables | Receivable days | Long-term debt | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 869 | 874 | 378 | -383 | 27 | 387 | 58 | 640 | 316 |
| 2017 | 991 | 894 | 353 | -256 | 37 | 429 | 60 | 575 | 428 |
| 2018 | 1,182 | 1,421 | 489 | -728 | 42 | 614 | 66 | 1,100 | 586 |
| 2019 | 1,376 | 1,487 | 476 | -587 | 95 | 649 | 69 | 1,032 | 745 |
| 2020 | 1,587 | 1,618 | 488 | -519 | 274 | 679 | 71 | 1,033 | 926 |
| 2021 | 1,865 | 1,570 | 488 | -193 | 530 | 708 | 64 | 1,034 | 1,174 |
| 2022 | 1,901 | 1,892 | 570 | -561 | 70 | 854 | 68 | 1,067 | 1,200 |
| 2023 | 1,892 | 1,894 | 498 | -500 | 176 | 742 | 61 | 1,037 | 1,196 |
| 2024 | 1,777 | 1,893 | 440 | -556 | 205 | 651 | 58 | 1,034 | 1,097 |
| 2025 | 1,804 | 2,143 | 454 | -793 | 161 | 674 | 62 | 1,169 | 1,092 |
| 2026-06-30 | 1,805 | 2,280 | 596 | -1,071 | 153 | 766 | 71 | 1,438 | 1,082 |

What the figures say. (1) **Every dollar of equity, and more, is purchased goodwill and customer lists.** Tangible
equity has been negative in every year and is now about minus $1.07 billion, its lowest; the business's own tangible
capital is its receivables, funded by accrued payroll and debt. (2) **Debt has more than doubled** (640 to 1,452 of
principal at 2026-06-30, 10-Q Note 5) while the equity line stood still from 2021: the decade's cash went to acquisitions
($2,100.2M gross, 2016 to 2025; $283.6M more in H1 2026) and buybacks ($1,382.2M, 2016 to 2025), more than the business
produced, the gap filled by borrowing and by the Oxford sale. (3) **Retained earnings have fallen since 2022** (1,200 to
1,082) because repurchased shares are retired against them (10-Q, statement of equity, "Stock repurchase and retirement of
shares"). (4) **Receivable days are back at their highs**: 71 at 2026-06-30, against 58 to 62 in 2023 to 2025; the 10-K
MD&A ties the 2025 fall in operating cash to "accounts receivable days sales outstanding which increased in 2025", and
receivables rose $72.3M in H1 2026 (10-Q cash flow). What the figures cannot say: how much of the goodwill still earns,
since the 2025 impairment test was qualitative ("the Company performed a qualitative assessment and determined there were
no indicators of impairment", 10-K, MD&A), while the market value of the whole company ($1.49 billion) now sits below the
goodwill alone ($2.28 billion). The rule this follows: "what the figures are saying and what they don’t say and what they
can’t say" **[M2025-032]**.

### B. Owner cash, recast (the Q4 arithmetic, not judged)
USD millions; OCF, stock pay, D&A and capex from XBRL as printed by `tools/run.py` and the company facts; acquisitions and
divestitures from the cash-flow statements (XBRL).

| FY | OCF | Stock pay | Capex | D&A | Owner cash before acquisitions | Acquisitions paid in cash | Divestiture proceeds |
|---|---|---|---|---|---|---|---|
| 2016 | 199.3 | 27.0 | 27.1 | 62.2 | 145.2 | 0.0 | 6.0 |
| 2017 | 196.4 | 24.0 | 24.3 | 58.6 | 148.1 | 25.9 | 0.0 |
| 2018 | 287.4 | 31.5 | 28.7 | 95.0 | 227.2 | 760.2 | 0.0 |
| 2019 | 313.2 | 39.3 | 32.7 | 91.2 | 241.2 | 116.4 | 0.0 |
| 2020 | 424.8 | 32.3 | 32.6 | 89.7 | 359.9 | 186.2 | 0.0 |
| 2021 | 193.7 | 52.7 | 34.7 | 89.6 | 106.3 | 222.8 | 503.8 |
| 2022 | 307.8 | 49.3 | 37.5 | 91.4 | 221.0 | 484.6 | 9.8 |
| 2023 | 456.9 | 44.0 | 39.9 | 100.3 | 373.0 | 0.0 | 0.0 |
| 2024 | 400.0 | 42.3 | 35.3 | 96.3 | 322.4 | 0.0 | 0.0 |
| 2025 | 327.9 | 47.9 | 39.8 | 113.5 | 240.2 | 304.1 | 0.0 |
| Ten-year sum | | | | | 2,384.5 | 2,100.2 | 519.6 |
| TTM to 2026-06-30 | 256.9 | 51.9 | 35.8 | | 169.2 | 283.6 (H1 2026) | |

Owner cash before acquisitions = OCF less stock pay less capex. Readings the Q4 work would have to settle. (1) Capex
($39.8M in 2025) is close to depreciation ($38.0M, XBRL Depreciation), so all capex is treated as maintenance; D&A of
$113.5M is mostly amortization of acquired customer lists ($64.8M in 2025). (2) 2021 is abnormal: income taxes paid were
$170.3M against $54.5M in 2022 (XBRL IncomeTaxesPaidNet), the tax on the Oxford gain sitting inside operating cash while
the $503.8M of proceeds sit in investing; 2023 was lifted by a receivables release. (3) The recurring "one-time":
acquisition, integration and strategic planning expenses of $26.5M in 2025, $8.3M in Q2 2025 and $9.8M in Q2 2026 (10-K
and 10-Q MD&A); they are inside operating cash already. (4) **The deciding reading is the acquisitions.** Revenue fell 13%
from 2022 to 2025 with TopBloc bought, and 0.7% in H1 2026 with Quinnox bought; over the decade, $1,580.6M of acquisition
spending net of divestitures (and $28.7M of stock issued for TopBloc) left operating income at $230.3M in 2025 against
$189.7M in 2016, when the company still owned Oxford. Part of the deal spending has been the cost of standing still; the
filings give no acquired-revenue figure from which to say how much. Ten years of cash actually left for owners after net
acquisitions: (2,384.5 less 1,580.6 less 28.7) / 10 = **$77.5M a year**; before acquisitions, $238.4M a year (ten years)
or $252.6M (five years, the screen's basis). Coverage on the framework's definition, pre-tax earnings over interest (the
definition is **[L2012-002]**'s): 2025 pre-tax income $162.6M over interest $67.7M, 2.4 times; H1 2026, $31.3M over
$37.5M, 0.8 times.

### C. The competitor row over the whole span (same metric, each company's own 10-K filings, XBRL company facts)
Chosen because each is the closest listed rival to one part of the business: **Kforce** (US technology staffing and
consulting to large companies, the nearest match to Apex Systems and the assignment business); **Robert Half** (the
largest US professional staffer, with technology staffing and the Protiviti consultancy); **EPAM** (digital engineering
and software consulting, what the Commercial consulting business says it is becoming); **SAIC** (federal IT services, the
nearest match to ECS in the Federal segment). Latest 10-K accessions: KFRC 0000930420-26-000007, RHI
0000315213-26-000006, EPAM 0001352010-26-000015; SAIC from its company facts (fiscal years ending about February,
labelled by calendar frame).

| Gross margin | 2016 | 2019 | 2022 | 2025 | Revenue 2016 to 2025 | Revenue 2022 to 2025 |
|---|---|---|---|---|---|---|
| Everforth | 32.6% | 28.4% | 29.9% | 28.9% | $2,440M to $3,980M (with acquisitions; 2016 with Oxford) | -13% |
| Kforce | 31.0% | 29.3% | 29.3% | 27.2% | $1,320M to $1,329M | -22% |
| Robert Half | 41.2% | 41.6% | 42.7% | 37.2% | $5,250M to $5,379M | -26% |
| EPAM | 36.5% | 35.1% | 31.9% | 28.8% | $1,160M to $5,457M | +13% |
| SAIC | 9.9% | 11.1% | 11.5% | 12.0% | $4,442M to $7,262M (Engility bought 2019) | -6% |

Read over the span, not one year: the hour-renting businesses (Kforce, Robert Half, Everforth) earned thin and falling
spreads and gave back from 2023 what they gained in 2021 and 2022; Kforce's revenue is where it was in 2016, Robert
Half's barely above; EPAM grew, but its gross margin fell nearly eight points over the decade; SAIC's margin is steady and
low. Operating margins are in the Q1 table. Everforth's 2025 gross margin sits between the staffers and EPAM, and its
operating margin (5.8% in 2025, 3.5% in H1 2026) is in Kforce's band, not that of a business with a cost or brand edge.
The filer's own words on entry, recorded here and not judged since Q2 was not reached: "The IT industry is highly
competitive and fragmented with limited barriers to entry." and "Many of our agreements may be terminated by clients at
will" (10-K, Item 1A).

### D. Value range (the Q7 CONVENTION construction), whole-cycle variant, fair and cheap prices
Sovereign 5.63%; 41.0M shares; owner cash is after interest and after the company's own tax, so the present value is the
equity's. Zero nominal growth after year ten, as the convention reads "no real growth".

| Case (cash definition) | Cash a year | Growth, ten years | Value | Per share |
|---|---|---|---|---|
| Convention, no-growth end, five-year mean before acquisitions (the screen's basis) | $252.6M | 0% | $4,487M | $109.43 |
| Convention, shown-growth end, same basis | $252.6M | +2.8% (2022 to 2025; 2021 is an aberrant base) | $5,602M | $136.63 |
| Five years, acquisitions deducted, divestiture proceeds counted | $147.3M | 0% | $2,616M | $63.81 |
| Five years, acquisitions deducted, divestiture proceeds left out (a sale is not cash earned) | $44.5M | 0% | $790M | $19.28 |
| **Whole-cycle variant**: ten years 2016 to 2025, net of acquisitions and divestitures, stock for deals deducted | $77.5M | 0% | $1,377M | **$33.58** |
| Ten years before acquisitions | $238.4M | 0% | $4,235M | $103.30 |

- **The shown growth.** Owner cash before acquisitions rose from $106.3M (2021) to $240.2M (2025), +22.6% a year, from a
  base year depressed by the Oxford tax: "a base year in which earnings were poor can produce a breathtaking, but
  meaningless, growth rate." **[L2005-003]**. Measured from 2022 it is +2.8%, and it came with $788.7M of acquisitions in
  that window (2022 and 2025). Revenue over 2022 to 2025 fell 4.6% a year and operating income 17.5% a year, so the
  shown-growth end is the generous one.
- **VALUE RANGE: $33.58 to $109.43 a share** on the convention's no-growth ends of the two cash definitions that matter
  (after and before the acquisitions), against **$36.32**. The top is 3.26 times the bottom: wider than the convention's
  three to one, so Q7, had it been reached, would have closed TOO HARD on width alone (the convention's rows,
  **[L2000-025]**, **[M2007-022]**); across all the cash definitions above, the spread is $19.28 to $136.63, about seven to
  one. The whole-cycle variant ($33.58) is the one that charges the business for what it actually spent to stay the size
  it is. The price sits just above the bottom of the narrower range: not a screamer on any reading that charges the
  acquisitions (the convention's row, **[M2009-005]**).
- **What the price assumes.** $1,489M at 5.63% is $83.8M a year forever with no growth: almost exactly the decade's cash
  after acquisitions. The market is pricing the deal spending as the cost of standing still.
- **FAIR PRICE: $38.54 a share.** Central case (CONVENTION of this run): $158.0M a year, the midpoint of the ten-year cash
  before acquisitions ($238.4M) and after them ($77.5M), at zero growth. Rationale: the filings do not disclose acquired
  revenue, so the share of deal spending that only holds the business in place cannot be read; the midpoint splits that
  ignorance evenly and is confessed as such; the trailing-twelve-month cash before acquisitions ($169.2M) sits near it.
  The floor (the framework's CONVENTION of about ten percent pre-tax, from **[M2003-149]** among others) is applied to
  owner cash, which is after the company's corporate tax and before the buyer's own tax: $158.0M / 10% = $1,580M, or
  $38.54 a share. **Tax treatment, the looser reading:** if "pre-tax" is read as before the company's corporate tax, the
  central cash grossed up at the 27.0% effective rate of 2024 (10-K, MD&A) is $216.4M and the fair price $52.79. If the
  2022 to 2025 revenue decline (4.6% a year) were carried ten years, the central case's present value would fall from
  $68.45 to about $48 a share, and the fair price with it.
- **CHEAP PRICE: $18.91 a share.** Rule (CONVENTION of this run): the price at which the whole-cycle cash after
  acquisitions ($77.5M) alone yields the ten percent floor ($775M), so that the decision would not depend on how much of
  the deal spending is maintenance, the one question the filings cannot answer. Below it no pencil would be needed on the
  cash; it would still not reopen Q1 **[M2000-038]**.
- **The price against these: $36.32** is inside the range, 8% above its bottom ($33.58), 6% below the fair price on the
  strict reading ($38.54), and 92% above the cheap price ($18.91).

### E. Noted for the questions not reached (context only, no weighing)
- Q4: the Q2 2026 release leads with "Adjusted EBITDA (a non-GAAP measure) was $96.7 million" under a headline that
  results "Exceed the High-End of Guidance Estimates" (exhibit 99.1); GAAP net income was $14.2M. The framework names both
  kinds of tell (Q4, The tells); with Q4 not reached they are recorded, not weighed.
- Q5 and Q6: the 2025 cash bonus was set on "the Company's adjusted EBITDA (earnings before interest, tax, depreciation and
  amortization) growth percentage" and "the Company's revenue growth percentage"; performance shares vest on three-year
  NOPAT growth with a relative-TSR modifier; the chief executive's 2025 total compensation was $10,475,672 (DEF 14A,
  accession 0000890564-26-000031). Buybacks were $1,382.2M over 2016 to 2025 and $50.5M in H1 2026; whether the
  programmes name a price was not searched, since Q6 was not reached.
- Q9: $1,451.8M of debt principal at 2026-06-30; the $550M of 4.625% notes fall due in 2028 and term loan B ($486.3M) in
  2030; term loan A was repaid from the revolver, now $600M and due 2031 subject to the 2028 notes being refinanced (10-Q
  Note 5; 8-K 2026-07-09). The covenant caps senior secured debt at 3.75 times lender-defined EBITDA (2.17 at
  2026-06-30), stepping down to 3.50 and 3.25 from mid-2027 and mid-2028.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** The business's key variable, the ten-year demand for rented technical hours, turns
on what AI does to software and data work, a forecast its own industry's insiders write in opposite directions and will
not put a number to **[M2000-105]**, **[M1998-008]**. Q7 was not reached; computed for reporting only, the range is $33.58
to $109.43 against $36.32, fair $38.54, cheap $18.91 (COMPUTATION — NOT A CLEARANCE). No research file is opened: the
cause is NATURE, and a lower price does not reopen it **[M2000-038]**.

## SELF-AUDIT
- [x] Copied to the dated file before any filing was fetched (the EDGAR ticker file was read first, to learn the company
      name for the file title; no filing was read before the copy); written question by question. **Not committed:** the
      dispatch instruction forbids commits, so the write-early commits were not made.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      script); every filing fact carries its document and accession; every number has a filing or a CONVENTION label.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance, and the post-close section carries the
      protocol's heading.
- [x] Owner cash after stock pay and capex, never a net-income proxy (operator rule 5); the sovereign from the US
      Treasury; aggregator quotes flagged.
- [x] Contrary evidence was written down as it was found (foundations, five items) and weighed at Q1 **[M1997-127]**.
- [x] Not a point-in-time run; no anchor bars any row.
- [x] Only the arithmetic lines of `tools/run.py` were used; `Screens/cover_shares.py` failed and the cover was read by
      hand.
- [x] `python tools/check_framework.py` run after writing.
- Em dashes: none in the analyst's own text; the only ones in the file are the protocol's mandated label "COMPUTATION —
  NOT A CLEARANCE" (operator rule 3); no quotation used here contains one.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Two closing STOPs, and the sequence records the one that sounds softer.** The filer's own risk factor ("limited
barriers to entry") and the competitor row would very likely have closed Q2 OUT on the evidence; the routing sends fast
change to Q1 TOO HARD first, so the run records a NATURE box where an OUT was also in view. Both are closed boxes, but a
reader of the register sees "too hard" and may think the castle was never examined; the framework could say whether a run
that closes at Q1 should record, as context, a Q2 finding the evidence already shows (this run did, in section C, without
weighing it). (2) **Q1's insider test is written for "the tech field"** **[M2000-105]**; whether it reaches a services
business whose demand depends on someone else's technology is not stated. It was applied through **[M1998-008]**, which
names technology that could hurt "the business as it presently exists". (3) **The Q7 convention says the cash input
"deducts all capital spending" but not whether cash acquisitions are capital spending.** For a business that has spent,
net of divestitures, about two thirds of its pre-acquisition cash on deals for a decade, the answer moves the value by a
factor of three to five; this run showed both and named the whole-cycle variant. A sentence is needed for serial
acquirers. (4) **"Pre-tax" in the floor is not defined against the target's corporate tax**; the run applied it to owner
cash after corporate tax and showed the looser reading beside it. (5) `Screens/cover_shares.py` read the CIK (890,564) as a
share count for this filer and scaled it by a million; it should refuse a cover count equal to the CIK.
