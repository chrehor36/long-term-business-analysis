# Company Run - ADT Inc. (NYSE: ADT) - 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any
fetch. Working folder: `Test Runs/_research 2026-10-06 ADT/` (filings as text, the arithmetic script `owner_cash.py` and its
output `owner_cash_out.txt`, the `tools/run.py` and `Screens/cover_shares.py` outputs, and the competitor filings in `peers/`).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred by this run's blind rule, so the
analyst does not know whether the operator holds ADT. The run is written as for a name not held.

**CONTAMINATION, declared.** (1) The session context showed recent commit subjects: KTB Kontoor Brands TOO HARD (NATURE) at
Q2; SBH Sally Beauty OUT at Q2 ("filer says few barriers to entry"); AMN Healthcare OUT at Q2 ("low barriers to entry (a
rival's own 10-K)"). This run's Q2 also leans on a filer's statement of low barriers to entry, so the steering risk is
named: the reading below was built from ADT's own filings and the competitors' filings, and the counter-evidence is
written down beside it. (2) The git status listed untracked file names `2026-10-05 Run - POOL` and `2026-10-06 Run - GPOR`;
neither was opened. (3) The memory index loaded with the session mentions queue counts and holdings reviews owed; it names
no ADT fact. (4) No other `Test Runs/` file about ADT exists (directory listing checked by name only). (5) The lock in
`Screens/_daily/` was not written: the dispatching instruction confines this session to its output file and working folder.

---
## STEP 0 - THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $6.21 (close 2026-10-05; Yahoo chart via `tools/sources.py`; aggregator, live quote only, flagged per operator
  rule 5). Closes 2026-09-24 to 2026-10-05 ran $6.08 to $6.40.
- **Shares by class**, cover of the 10-Q for the quarter ended 2026-06-30 (filed 2026-07-30, accession
  `0001703056-26-000100`; `python Screens/cover_shares.py ADT`): Common Stock 675,814,723; Class B Common Stock 54,744,525
  (held only by Google). The charter note: diluted EPS counts "incremental shares of Common Stock issuable upon the
  conversion of Class B Common Stock" and Class B shares the same per-share income and dividends (10-K FY2025, Note 12,
  accession `0001703056-26-000022`), so the two classes are added: **730,559,248 shares**. Not added: about 8.0 million
  unvested RSUs at 2025 year-end, the stock options (the 2025 grants alone were 3.68 million to the CEO), and the S-8
  registering 8.1 million shares for the Origin AI retention awards. `tools/run.py` printed a stale 771.0M count of
  2020-12-31; it was not used.
- **Market cap:** $6.21 x 730.56M = **$4,537M**. Debt principal $7,775M at 2026-06-30 (10-Q, Note on debt), less cash and
  restricted cash of $28M, is net debt of **$7,747M**; a further $100M term loan A was drawn on 2026-08-28 (8-K
  `0001703056-26-000106`). Enterprise value about $12.3B.
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-03-02, `0001703056-26-000022`), Items 1, 1A in part, 5, 7, 8
  (balance sheet, operations, equity, cash flows, Notes 2, 7, 10, 11, 12, 16); 10-Q Q2 2026 (filed 2026-07-30,
  `0001703056-26-000100`); proxy DEF 14A (filed 2026-04-14, `0001703056-26-000032`), CD&A, summary compensation table,
  related-person transactions; 8-K 2023-07-10 Item 4.02 (`0001703056-23-000140`); 8-K 2026-08-31 (`0001703056-26-000106`);
  the IPO prospectus 424B4 (2018-01-22, `0001193125-18-016233`); and for the span, the 10-Ks for FY2017
  (`0001703056-18-000008`), FY2018 (`0001703056-19-000042`), FY2019 (`0001703056-20-000013`), FY2020
  (`0001703056-21-000020`), FY2021 (`0001703056-22-000042`), FY2022 as amended (10-K/A `0001703056-23-000146`), FY2023
  (`0001703056-24-000020`), FY2024 (`0001703056-25-000022`), and The ADT Corporation's 10-Ks for fiscal 2012
  (`0001193125-12-482228`) and fiscal 2015 (`0001546640-15-000031`).
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025 $1,884,163 thousand
  (10-K FY2025 cash flow statement) against `tools/run.py`'s 1,884; total assets $15,818,511 thousand against 15,819. Both agree.
- **`tools/run.py ADT`, arithmetic lines only** (Part VII: nothing it prints as a rule, id or verdict is used). Its "capex"
  is purchases of property and equipment only ($176M in 2025) and its "capex alt" adds the dealer-account purchases
  ($596M) but **misses the line "Subscriber system asset expenditures" ($396M in 2025, $523M in 2024, $631M in 2023)**, which
  the filing reports under investing activities. Its "OE capex alt" of $1,027M for 2025 is therefore overstated by $396M and
  is not used. The table below is rebuilt from the filed cash-flow lines.

### Owner cash after every real cost (USD millions; filed cash-flow lines; arithmetic in `owner_cash.py`)
Owner cash = operating cash flow less stock pay, less every capital line the filing shows: dealer-generated and bulk
account purchases, subscriber system asset expenditures, purchases of property and equipment, and finance-lease principal
(financing section). Installation costs and commissions for accounts the company owns are deferred and already sit inside
operating cash flow ("Deferred subscriber acquisition costs", $(381)M in 2025, against $225M of "Deferred subscriber
acquisition revenue" received). Cash interest and cash taxes are inside operating cash flow; the two right-hand columns
add them back for the floor tests.

| Year | OCF | SBC | Dealer accts | Subscriber systems | PP&E | Fin. leases | **Owner cash** | + cash tax = pre-tax | + cash interest (all-equity) | D&A variant (OCF-SBC-D&A) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 1,591.9 | 11.3 | 653.2 | 582.7 | 130.6 | n/s | **214.1** | 233.5 | 894.8 | -282.6 |
| 2018 | 1,787.6 | 135.0 | 693.5 | 576.3 | 126.8 | n/s | **256.0** | 262.3 | 950.4 | -278.3 |
| 2019 | 1,873.1 | 85.6 | 669.7 | 542.3 | 158.8 | n/s | **416.7** | 415.7 | 960.9 | -201.6 |
| 2020 | 1,366.7 | 96.0 | 380.7 | 418.4 | 157.2 | 28.0 | **286.5** | 312.3 | 822.5 | -643.0 |
| 2021 | 1,649.7 | 61.2 | 675.1 | 694.7 | 168.2 | 32.1 | **18.3** | 20.2 | 532.8 | -326.3 |
| 2022 | 1,887.9 | 66.6 | 621.7 | 734.6 | 176.7 | 45.0 | **243.4** | 266.0 | 737.0 | 127.8 |
| 2023 | 1,657.7 | 51.1 | 588.6 | 630.5 | 176.4 | 43.7 | **167.3** | 227.6 | 750.4 | 217.9 |
| 2024 | 1,884.9 | 48.6 | 585.8 | 523.1 | 163.8 | 29.0 | **534.5** | 556.2 | 928.2 | 491.6 |
| 2025 | 1,884.2 | 54.6 | 596.5 | 396.0 | 175.7 | 30.2 | **631.2** | 773.4 | 1,182.8 | 462.4 |
| **5-yr mean 2021-25** | | | | | | | **318.9** | 368.7 | 826.2 | 194.7 |
| **9-yr mean 2017-25** | | | | | | | **307.6** | 340.8 | 862.2 | -48.0 |
| **2024-25 mean** | | | | | | | **582.8** | 664.8 | 1,055.5 | 477.0 |

n/s = not shown as a separate line that year. Sources by year: FY2019 10-K (2017-2019), FY2021 10-K (2020-2021), FY2023
10-K (2021-2023 cash interest and taxes, 2022-2023 lines), FY2025 10-K (2023-2025). Cash taxes paid: 19.4, 6.3, -1.0, 25.8,
1.9, 22.7, 60.3, 21.7, 142.2. Cash interest: 661.3, 688.1, 545.2, 510.2, 512.6, 470.9, 522.8, 372.0, 409.4.

What the table carries that the arithmetic does not: (a) the cash flows of the commercial business (sold October 2023) and
of the solar business (exited 2024) are not segregated in the cash-flow statements (10-K FY2025, MD&A, "ADT Solar Exit"),
so 2017-2023 mix them in; (b) ADT used up its NOLs in 2024 and "became a federal cash taxpayer in 2025" (10-K FY2025,
MD&A, Tax Matters), so after-tax owner cash before 2025 is flattered, which is why the floor tests use the pre-tax column;
(c) since the second quarter of 2024 a growing share of new accounts are "outright sales" in which the customer buys the
equipment (about 25% of new direct subscribers in 2025, and the company said it would move further non-ADT+ transactions to
that model in 2026), which moves capital from the subscriber-system line into installation revenue and is part of why
owner cash rose in 2024-2025; (d) the 2026 first half shows OCF $1,304M against $1,031M a year earlier, with "Other, net"
of +$210M explained by the filer as timing of tax, interest and payroll payments (10-Q MD&A); one half-year is not used.

**Is any of the acquisition spending growth?** The filing's own figures say no. RMR was $353M at 2023 year-end, $359M at 2024
and $359M at 2025 (10-K FY2025, KPI table); 2025 monitoring revenue rose on "an increase in average prices of $113
million, partially offset by a decrease in volume of $53 million" (MD&A). Gross customer revenue attrition of 13.1% on
annualized RMR of about $4.30B is about $564M of revenue lost a year; at the proxy's stated "revenue payback period of 2.3
years" (DEF 14A 2026, CD&A) replacing it costs about $1.30B a year, against $1,148M of net acquisition cash in 2025 (dealer
accounts 596 + subscriber systems 396 + deferred costs 381 - deferred revenue received 225) before the installation revenue
of outright sales. The subscriber spending is the cost of standing still, the inverse of the case the rows prize, a
business that would "remain more or less the same size" without the spending **[M2009-054]** ("If GEICO would remain more or
less the same size if we didn’t advertise so healthy"). All of it is therefore treated as maintenance; no growth capital is
backed out.

### The balance sheets, ten year-ends, before the income account
Read "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. USD millions.
2016-2018 from the filed statements (FY2017 and FY2018 10-Ks); 2019-2025 as `tools/run.py` transcribed them from each year's
first-filed XBRL (2022 is the pre-restatement figure), with 2024-2025 checked against the FY2025 filed balance sheet.

| Year-end | Total assets | Goodwill | Intangibles | LT debt (noncurrent) | Equity | Tangible equity (computed) | Accumulated deficit | Cash |
|---|---|---|---|---|---|---|---|---|
| 2016 | 17,176 | 5,013 | 8,309 | 9,470 + 634 preferred | 3,805 | -9,517 | -591 | 76 |
| 2017 | 17,015 | 5,071 | 7,857 | 10,121 + 682 preferred | 3,433 | -9,495 | -998 | 123 |
| 2018 | 17,209 | 5,082 | 7,488 | 9,944 | 4,225 | -8,345 | -1,680 | 363 |
| 2019 | 16,084 | 4,960 | 6,670 | 9,634 | 3,184 | -8,446 | -2,742 | 49 |
| 2020 | 16,117 | 5,236 | 5,907 | 9,448 | 3,039 | -8,104 | -3,491 | 205 |
| 2021 | 16,894 | 5,943 | 5,413 | 9,575 | 3,249 | -8,107 | -3,953 | 24 |
| 2022 | 17,873 | 5,819 | 5,092 | 8,957 | 3,433 | -7,478 | -3,910 (restated -3,950) | 257 |
| 2023 | 15,964 | 4,904 | 4,877 | 7,523 | 3,789 | -5,992 | -3,618 | 15 |
| 2024 | 16,051 | 4,904 | 4,854 | 7,511 | 3,801 | -5,957 | -3,318 | 96 |
| 2025 | 15,819 | 4,886 | 4,818 | 7,379 | 3,779 | -5,925 | -2,907 | 81 |

What the figures say, what they do not say, and what they cannot say:
- **Equity did not grow in ten years** ($3.8B to $3.8B) although owners put in about $1.4B at the 2018 IPO
  (`0001193125-18-016233`, $14.00 a share), $0.45B from Google in 2020 and $1.2B from State Farm in 2022 (offset by a $1.2B
  tender). What came out: a $750M special dividend in 2017 funded by incremental borrowing (FY2019 10-K, "used to fund a
  special dividend of $750 million"), ordinary dividends, and $1.7B of buybacks in 2024 to mid-2026. The accumulated
  deficit went from -$0.6B to -$4.0B (2022) before recovering to -$2.9B. Net income was a loss in 2016, 2018 (-$609M),
  2019 (-$424M), 2020 (-$632M) and 2021 (-$341M); 2017 (+$343M) rested on a $764M tax benefit; profits from 2022 on.
- **Tangible equity is about -$5.9B.** Intangibles fell from $8.3B to $4.8B as the customer relationships bought in the 2016
  Apollo buyout were amortized ("fully amortized during 2023", 10-K FY2025, critical estimates). Those charges were real:
  the rows separate intangibles that "truly deplete over time" from those that "never lose value" **[L2012-003]** ("Some truly
  deplete over time while others never lose value."), and the bought customers did leave at the 13% a year the attrition line
  shows. The ADT trade name ($1.3B, indefinite-lived) is the one intangible the filer says does not deplete.
- **Debt came down only by selling businesses.** Noncurrent debt was $9.5-10.1B (plus $0.6-0.7B of Koch preferred) from
  2016 to 2021 and fell to $7.4-7.5B only after the $1.6B commercial sale in 2023. Since then it has been refinanced, not
  repaid: principal $7.80B at 2025 year-end and $7.78B at 2026-06-30, plus $0.1B in August 2026, while $1.2B went to buybacks.
- **Cash is thin by design**: $81M at 2025 year-end, $28M including restricted cash at 2026-06-30; liquidity is the $800M
  revolver and an uncommitted receivables securitization (10-K FY2025, Liquidity). The filer: "We are a highly leveraged
  company with significant debt service requirements".
- **Deferrals grew large**: deferred subscriber acquisition costs (an asset) from $179M (2016) to $1,452M (2025) and deferred
  subscriber acquisition revenue (a liability) from $167M to $2,084M, the accounting of the company-owned equipment model;
  receivables rose from $246M (2018) to $385M (2025) with allowances of $64M and a 2025 provision for losses on receivables
  and inventory of $202M ($151M in 2023), the "higher non-payment" disconnects the MD&A names.
- **What they cannot say**: whether the subscriber base, the only asset that earns, will hold its value; the balance
  sheet carries it at cost less accelerated amortization over 15 years.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**; for ADT the answer turns entirely on whether the subscriber base holds, which is Q2's question. Who is paid
to tell you: the stock has been sold down by a financial owner in five registered offerings and one open-market sale from
March 2025 to May 2026, with the company buying shares in three of them (proxy 2026, related-person transactions; 10-Q Q2
2026, Note 14), and the rows warn "you do not get impartial advice from Wall Street" **[M2020-037]** and of businesses where
"figures get dressed up before they sell them and leveraged up" **[M2006-003]**. The analyst's habits: "What do I not know
that I need to know?" **[M1999-129]**; scuttlebutt aimed "to possibly reject your original hypothesis" **[M1998-144]**.

**Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**):
1. Gross customer revenue attrition has been stable for fifteen years: 13.3% (FY2010), 13.0%, 13.8%, 13.9%, 13.5%, 12.2%
   (FY2015, revenue basis) at The ADT Corporation; 14.8% (2016), 13.7%, 13.3%, 13.4%, 13.1%, 13.1%, 12.5%, 12.9%, 12.7% and
   13.1% (2025) at ADT Inc. The DIY decade did not move it.
2. Price per account has risen: The ADT Corporation's average revenue per customer was $36.10 (FY2010) and $42.65 (FY2015);
   RMR of $358.7M over 6.1 million subscribers is about $58.80 in 2025 (arithmetic; RMR includes contracts monitored but not
   owned, so the figure is approximate). That is roughly 3% a year of price, and 2025's price gain of $113M exceeded the
   volume loss of $53M.
3. Owner cash rose to $535M (2024) and $631M (2025); on those two years alone the stock yields 14.7% pre-tax (computation
   below). A reader who takes the post-divestiture business as the new base reaches a different price than this run does.
4. The rivals who tried to build the same castle failed (Monitronics bankrupt in 2019; Vivint lost money every year
   2017-2022 and was sold), which can be read as evidence that the incumbent's scale is hard to attack profitably.
5. Apollo's overhang ended in May 2026; shares outstanding (with Class B) fell 18% from 891.3M at 2024 year-end to 730.6M.

## THE STANDING RULE
Owning the common, bought with cash and sized so that its loss is bearable, does not put the buyer at risk of ruin: the
buyer's ruin comes through the buyer's own borrowing, "borrowed money has no place in the investor's tool kit"
**[L2014-005]**, and "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**
ADT's own leverage ($7.8B against a $4.5B equity value) is the target's exposure, Q9's subject, and could make a small
position a total loss; it is no reason for the buyer to borrow, and none is assumed.

---
## Q1 - CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The definition applied.** Understanding is "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**. The business is one product: a monitored-security subscription
  (monitoring and related services were $4.35B of $5.13B revenue in 2025; 6.1 million subscribers; one segment; revenue
  outside the US "not material"; 10-K FY2025 Item 1).
- **The key variables and how predictable they have been** ("trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**): (1) attrition, 12.2% to 14.8% in every year
  from FY2010 to 2025 (above); (2) the cost of a new account, a revenue payback of 30.1 months in 2017 (FY2017 10-K,
  management incentive table, "Revenue Payback Period 30.1x") and 2.3 years in 2025 (proxy); (3) price per account, rising
  about 3% a year; (4) cost to serve and interest, both on the face of the statements. The statements over sixteen years let
  the next statements be sketched, which is the test of "the financial statements will tell me the information that’s
  useful to me" **[M2008-033]**, once the company-owned and outright-sale accounting is recast as in Step 0.
- **Customers, not technology.** The forecast is about consumer behavior, of the kind the rows say can be projected, "we
  know what we think we can project out in terms of consumer behavior and threats to a business" **[M2023-030]**. The filer
  describes technology change (AI ambient sensing, the ADT+ platform, DIY), but the measured variables moved slowly
  through the decade in which Ring, SimpliSafe and Google Nest entered; this is not the "fast-moving technology" that "is not
  going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]**. The warning that "slow change
  can be much harder to perceive, and can lull you to sleep easier" **[M2014-038]** is carried to Q2, where the castle is judged.
- **The doubt test.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**
  The doubt here is not about what drives the economics, which are few and measured; it is about whether the castle holds,
  which is Q2's question and not a reason to stop at Q1 (the framework's routing: Q1 asks whether the economics can be
  foreseen at all; Q2 asks what the foresight shows).
- **VERDICT: IN.** The economics are a few variables with a sixteen-year public record, a case of one "where you really do
  know the key variables" **[M1998-044]**, giving "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**.

## Q2 - WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, starting from the attacker, since "all moats are
subject to attack in a capitalistic system" **[M1995-038]**.

**The money test, answered by the defender.** The test is the See's question: could an attacker with money take it on, and
"If the answer had been yes, we wouldn’t have done it." **[M2011-015]** ADT's own FY2025 10-K (Item 1, Competition,
`0001703056-26-000022`) answers it: the residential and small business security markets "remain highly competitive and
fragmented, with several major companies; many smaller national, local, and regional companies; and an increasing number of
new entrants, which is primarily the result of relatively low barriers to entry and the availability of other companies
providing outsourced monitoring services. Technology trends and innovation provide new opportunities while also lowering
the barriers to entry for automation, interactive, and smart home solutions." The same text in 2015: "Innovation has lowered
the barriers to entry in home automation, and new business models and competitors have emerged." (The ADT Corporation
10-K FY2015, `0001546640-15-000031`.) This is the single fact the run rests on: the incumbent states, under its own
signature and in two eras, that the barriers are low and entrants are increasing. The rows' failing answer is the same
words: "there are some industries that are just never going to have barriers to entry" and "you better be running very
fast" **[M2012-106]**.

**The other castle tests, each with its filing fact.**
- **Continuously rebuilt.** ADT must replace about one customer in eight every year (attrition 13.1% in 2025) at about 2.3
  years of that customer's revenue, roughly $1.15-1.30B a year (Step 0), to keep RMR flat. "A moat that must be continuously
  rebuilt will eventually be no moat at all." **[L2007-005]** The rebuilding has kept pace (RMR $353M to $359M, 2023-2025)
  but has not gained: subscriber volume fell (2025 volume effect -$53M; 6.4 million subscribers at 2024 year-end, about
  0.2 million sold with the multifamily business in October 2025, 6.1 million at 2025 year-end and at 2026-06-30), and
  attrition rose from 12.7% to 13.1% in 2025 and to 13.1% from 12.8% for the twelve months to 2026-06-30 (10-Q).
- **Unit volume over the span.** The ADT Corporation served 6,285 thousand customers at FY2010, a count that already
  included about 1.4 million accounts bought with Broadview Security (Brink's Home Security) in 2010, 6,422 thousand at
  FY2012 and 6,594 thousand at FY2015 (US and Canada, residential and business). ADT Inc. served 7.2 million at 2017 and
  2018 after the Protection One and ASG combination, 6.5 million at 2019 after selling Canada, 6.7 million at 2022, 6.4
  million at 2023 after selling the commercial business, and 6.1 million at 2025. Across fifteen years and several bought
  customer bases, no organic growth in the count is visible; the business holds its size by buying and rebuilding it.
- **Pricing power and the low bid.** Price has risen about 3% a year, and 2025's price gain ($113M) came with a volume loss
  ($53M). The rows' strong form is "Anytime you can charge more for a product and maintain or increase market share"
  **[M2000-031]**; the volume line shows share not maintained. The rows ask whether the customer would choose it over "the low
  bid" **[M2017-009]** ("it wouldn’t be a question of people buying candy for the low bid"); the filer says "some
  self-monitored solutions do not require a monthly fee for home automation services, which allows for no-cost
  alternatives to the professionally monitored, fee-based solutions that we provide" (10-K FY2025, Competition).
- **The defender is adopting the attacker's model.** The filer is "increasingly focused on expanding and enhancing our DIY
  offerings", sells equipment outright on its new platform, and "Although the DIY market typically has lower monthly
  recurring fees than our professional installations, we believe this approach will allow us to grow our subscriber base"
  (10-K FY2025, Items 1 and 7). In January 2024 it amended the Google agreement "to remove exclusivity for DIY products and
  services" (Item 1). Its interactive platform for the legacy ADT Pulse base is supplied by a third party: Alarm.com's
  "Connect provides a custom, on-premise interactive security and home automation platform for ADT Pulse" (Alarm.com 10-K
  FY2025, `0001459200-26-000005`), and legacy subscribers whose systems are "not currently compatible" with ADT+ carry "a
  heightened risk of attrition" (10-K FY2025, MD&A).
- **The low-cost or low-churn position.** In a field without barriers the rows allow one escape, "commodity businesses have
  risk unless you’re the low-cost producer" **[M1997-010]**, measured against rivals, "if your costs are on parity or less"
  **[M2001-013]**. ADT's retention is not the best in its field: Brink's Home Security reported a disconnect rate of 7.0% to
  8.2% in 2007-2009; Vivint's average subscriber lifetime of 108 months (2022) implies about 11% a year; ADT's is 13.1%.
  Monitoring cost per subscriber is about parity (ADT monitoring and related services cost $642M in 2025 over 6.1 million
  subscribers, about $8.77 a month, arithmetic; Vivint's net service cost per subscriber was $9.68 a month in 2022). No
  filing shows ADT as the low-cost operator.
- **The returns the industry has earned.** Where a castle is open the returns are competed away, and "you can have only two
  competitors and they’re still terrible businesses" **[M2013-052]**. The competitor row below shows the second and third
  largest pro-installed providers losing money for years or failing, and ADT itself reporting losses in five of the seven
  years 2016-2022.
- **What could destroy, modify or reduce it** ("destroy, or modify, or reduce the economic strengths" **[M2000-014]**):
  self-monitoring at no or low fee, AI ambient sensing bundled with broadband (the filer names "technology companies,
  telecommunications providers, and smart home platform providers" offering "presence detection"), and the end of the
  company-owned-equipment contract that tied the customer for three to five years. The newspaper test, would the business
  be started today against its substitutes **[L2006-008]** ("newspapers as we know them probably would never have
  existed"), is answered by the defender's own move to outright sales and DIY.
- **Ask the competitors.** ADT names as principal competitors SimpliSafe, Xfinity, Vivint and Brinks Home in professional
  installation and Ring, SimpliSafe, Roku, Arlo and Wyze in self-installation (10-K FY2025). Vivint named ADT, Alarm.com,
  Brinks, FrontPoint, Guardian and SimpliSafe and the DIY offerings of Amazon and Google (10-K FY2022). Alarm.com names Ring
  and SimpliSafe. No filer names a rival that cannot get in.

**The competitor row** (same metrics, competitors' own filings; whole span where the filings allow):

| Company | Customers / subscribers | Attrition | Earnings | Source (accession) |
|---|---|---|---|---|
| ADT (The ADT Corporation to 2015; ADT Inc. from 2016) | 6,285K (FY2010, incl. ~1.4M Brink's/Broadview bought 2010), 6,594K (FY2015); 7.2M (2017), 6.5M (2019), 6.7M (2022), 6.4M (2023), 6.1M (2025) | 13.0-13.9% (FY2010-14); 12.2% (FY2015); 14.8% (2016) to 12.5-13.4% (2018-2025) | net loss 2016, 2018-2021; profit 2022-2025; owner cash $18-631M (2017-2025) | `0001193125-12-482228`, `0001546640-15-000031`, ADT Inc. 10-Ks listed in Step 0 |
| Brink's Home Security / Broadview (history) | about 1.4M (2009) | disconnect rate 7.0-8.2% (2007-2009) | merged into Tyco (ADT) 2010, about $2.0B | 10-K FY2009 `0001193125-10-038854` |
| Monitronics, brand Brinks Home from 2018 | 1,059K (2014), 1,090K (2015), 976K (2017), 922K (2018), 848K (2019), 934K (2020 incl. bulk buy) | unit 12.9% (2014), 13.6% (2015), 15.7% (2017), 17.1% (2018), 17.0% (2019), 14.9% (2020) | going-concern qualification on FY2018; Chapter 11 June 2019, emerged August 2019; net loss $181.8M (2020); deregistered (Form 15, 2021) | 10-Ks `0001265107-16-000052`, `0001265107-19-000004`, `0001265107-21-000019` |
| Vivint Smart Home (now NRG) | 1,695.5K (2020), 1,855.1K (2021), 1,924.6K (2022) | average lifetime 92, 106, 108 months (about 13%, 11.3%, 11.1% a year) | net loss $410.2M (2017), $472.6M (2018), $395.9M (2019), $603.3M (2020), $305.6M (2021), $51.7M (2022); sold to NRG for $12.00 a share in cash (March 2023) | 10-Ks `0001193125-20-073113`, `0001713952-23-000008`; 8-K `0001193125-23-066979` |
| Alarm.com (platform) | more than 2.6M subscribers (2015) | SaaS and license revenue renewal rate 94%, 95%, 95% (2023-2025) | ADT is 15-20% of its revenue (2023-2025); supplies ADT Pulse's platform | 10-Ks `0001459200-16-000024`, `0001459200-26-000005` |
| Ring (Amazon) | no metric filed: Amazon's 10-K FY2025 names Ring only among devices it "manufacture[s] and sell[s]" | n/a | n/a | `0001018724-26-000004` (flagged: no filed metric) |
| SimpliSafe | private; no filing (flagged) | n/a | n/a | none |

**Why the castle is still standing, in the filings' terms**: a brand associated with home security since 1874, six
redundant UL-listed monitoring centers, a dealer network of about 140, insurers' premium incentives, and multi-year
contracts with termination payments. **What keeps it standing for ten to twenty years**: on the filer's own account, the
continuing purchase of new accounts at about 2.3 years' revenue each against low barriers and no-fee alternatives. That is
the description of a castle defended by spending, not by a moat; the rows' summary for such a case is that the moat is
"tenuous", "it’s just too risky. We don’t know how to valuate that" **[M2000-019]**, or the See's answer, "If the answer had
been yes, we wouldn’t have done it." **[M2011-015]**

**OUT or TOO HARD.** The framework sends "a castle shown on the evidence to be filling in" to OUT and "a castle whose future
cannot be judged" to TOO HARD. The contrary evidence (fifteen years of stable attrition and rising price) says the castle has
not fallen; it does not say the castle is protected. The decisive fact is not a forecast: the defender's own sworn statement
that the barriers are low and entrants increasing answers the money test yes, and the span shows what that means in money:
flat customers, the second and third players broke, and the leader's own decade of losses on its acquired base. The castle
is shown open on the evidence. The reading that it is TOO HARD (NATURE), because the ten-year contest between professional
monitoring and DIY is a forecast nobody in the industry writes down, is recorded in the last section; it closes the file
too, and neither box is a pass. In the rows' three boxes, "in, out, and too hard" **[M2006-013]**, this is out.

- **VERDICT: OUT.** The money test, answered yes by the filer: "If the answer had been yes, we wouldn’t have done it."
  **[M2011-015]**; "there are some industries that are just never going to have barriers to entry" **[M2012-106]**; "A moat
  that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**; "you can have only two competitors
  and they’re still terrible businesses" **[M2013-052]**. Price does not reopen it.

---
## Q3 - HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed at Q2). The capital reading in Step 0 is recorded as fact, not weighed.
## Q4 - DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. The ten-year balance-sheet reading is in Step 0, as the template requires when the file closes before Q4.
## Q5 - WHO RUNS IT. NOT REACHED.
## Q6 - WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 - WHAT IS IT WORTH. NOT REACHED (see the computation below, which clears nothing).
## Q8 - IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 - COULD IT RUIN US. NOT REACHED.
## Q10 - IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) - WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

### Facts read on the way, recorded and not weighed (no verdict is drawn from them)
These were read for Step 0 or met in the documents above. The questions they belong to were not reached, so none of them
is weighed, and none is a clearance or a finding against the managers.
- **Accounts (Q4 material).** On 2023-07-10 the company filed Item 4.02, non-reliance on its statements for the periods
  ended September 30 and December 31, 2022 and March 31, 2023, for errors in the solar goodwill impairment and related tax,
  and reported a material weakness in internal control as of December 31, 2022 (`0001703056-23-000140`; 10-K/A
  `0001703056-23-000146`). The key performance indicators are Adjusted EBITDA (which adds back stock pay and the
  amortization of deferred acquisition costs, and deducts the amortization of deferred acquisition revenue) and, from 2025,
  Adjusted EPS, which adds back stock pay; the rows' tell list includes managements that wave away costs by highlighting
  adjusted per-share earnings, which "makes us nervous" **[L2016-006]**. Q4's two-tell rule was not applied because Q4 was
  not reached.
- **Pay (Q5 and Q6, Part B material).** The 2025 annual bonus paid on Adjusted EPS and total revenue, initial result about
  150%, set at 135% after negative discretion. The 2025 long-term awards were ten-year stock options at the grant-date price
  (CEO 3,681,118 options, grant value $9.94M); a fixed-price ten-year option is the form the rows say can reward a manager
  "who has done no more than tread water in his job" **[L1994-021]**. Legacy awards from the Apollo buyout, whose vesting
  depended on Apollo "achieving certain investment return objectives", were "deemed satisfied" by the Compensation Committee,
  50% vesting in 2024 and 50% on 2025-03-31 (proxy 2026, "Distributed Shares and Top-Up Options"). The CEO is also Chairman;
  his 2025 total compensation was $14.88M (summary compensation table).
- **Capital allocation (Q6, Part A material).** Buybacks of $6.57 to $8.31 a share in 2025-2026 under fixed-sum programs with
  no stated price ($500M, then $1.5B through April 2029), including 20M shares at $7.62 (March 2025), 11M at $8.31 (July 2025)
  and 29M at $7.25 (May 2026) bought alongside Apollo's secondary offerings; 2026 first-half buybacks of $600M against owner
  cash that had averaged $319M a year over five years; quarterly dividend $0.055. Apollo exited fully in May 2026.
- **Debt (Q9 material).** Principal $7.80B at 2025 year-end: first-lien term loans of $3.53B at SOFR plus 1.50-2.00%,
  first-lien notes of $1.0B at 3.375% due 2027, $1.0B at 4.125% due 2029 and $1.0B at 5.875% due 2033, $0.75B of ADT notes at
  4.875%, and a $443M receivables securitization; 2025 cash interest $409M; a maximum net first-lien leverage covenant on the
  term loan A. The rows' narrated case of buyout debt is acquirees "in mortal danger because of the debt piled on them by
  their private-equity buyers" **[L2008-007]**; ADT has serviced its debt and refinanced it, and no going-concern doubt
  appears in its filings.

## COMPUTATION - NOT A CLEARANCE
*(Operator rule 3. The file closed OUT at Q2; everything in this section is arithmetic reported at the owner's request and
carries no entry language. The protocol's heading uses a dash this run renders as a hyphen; see the last section.)*

**Inputs.** Owner cash after every real cost, the stated owner-cash definition being "a figure calculated after interest,
taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**, from the Step 0 table; shares 730.56M;
sovereign 5.66%; price $6.21.

**Growth input.** Aggregate owner cash went from $18M (2021) to $631M (2025), a rate that is the product of an aberrant base
year, "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate" **[L2005-003]**, and
that runs past the discount rate, where "you get into infinite numbers" **[M1997-095]**; the Q3 cap binds ("if you trace out
the mathematics of it, you bump into absurdities" **[M1999-067]**). The shown-growth end therefore uses the growth of the
revenue base the cash comes from, RMR $353.1M (2023) to $358.7M (2025), 0.8% a year (CONVENTION of this run, confessed
below).

**(a) VALUE RANGE** (Part VI convention: five-year mean, ten years at the shown growth, then zero nominal growth, at the
sovereign; the two ends are no growth and shown growth):

| Window | Owner cash | No growth | 0.8% for ten years | Top / bottom |
|---|---|---|---|---|
| **Five years 2021-25 (the convention)** | $318.9M | **$7.71** | **$8.22** | 1.07 |
| Whole cycle 2017-25 (2021 is abnormal: owner cash $18M in the solar-acquisition year) | $307.6M | $7.44 | $7.92 | 1.07 |
| Post-divestiture 2024-25 only (sensitivity, not the convention) | $582.8M | $14.10 | $15.02 | 1.07 |
| Depreciation variant, five years (OCF - SBC - D&A) | $194.7M | $4.71 | n/a | n/a |

Against **$6.21**: the price sits 19% below the bottom of the conventional range. The range is narrow (1.07, well under the
three-to-one width that would make it TOO HARD), so by the convention the close would be OUT or IN on the floor and the
screamer test: the expected return at the price, owner cash over market value with no growth, is 7.0% after the taxes
actually paid and **8.1% pre-tax**, below the CONVENTION floor of about ten percent pre-tax (the speakers' own "very high
probability of at least 10% pre-tax returns" **[L2002-020]**, "there’s just a point at which we drop out of the game"
**[M2003-149]**). On the whole-cycle window it is 6.8% after tax and 7.5% pre-tax. Only the two-year post-divestiture window
clears the floor (12.8% after tax, 14.7% pre-tax). Even there the case needs the pencil this section has used, and the rows' own sign of a
case that needs pencil and paper is "it’s too close to think about" **[M1996-084]**, which is why no window here is a screamer ("It should scream at you." **[M2009-005]**).

**(b) FAIR PRICE** (the price at or below which the central case clears about 10% pre-tax). Tax treatment: owner cash plus
the cash taxes actually paid, so that the NOL years and the full-taxpayer year are put on one pre-tax footing; the 2025
effective rate was 28.0%. Two bases:
- **On equity** (owner cash is after interest, so this is the equity holder's stream): five-year pre-tax mean $368.7M / 10% =
  $3,687M = **$5.05 a share**; whole cycle $340.8M, **$4.66**; post-divestiture 2024-25 $664.8M, **$9.10**.
- **On equity plus net debt** (pre-interest, pre-tax owner cash; the all-equity view in which the rows "evaluate
  acquisitions on an all-equity basis" **[L2017-004]**): five-year $826.2M / 10% = $8,262M of enterprise value, less net debt
  of $7,747M, = **$0.71 a share**; whole cycle $1.20; 2024-25 $3.84. On this basis the whole enterprise yields about 6.7%
  pre-tax at today's price ($826M on $12.3B); the 8% on equity exists because the debt costs about 4-6%.

**(c) CHEAP PRICE** (below which no pencil is needed). Rule (CONVENTION of this run): the price at which the central-case
pre-tax owner cash yields twice the floor, 20% on equity, so that the cash could be overstated by half and still clear the
floor. Five-year: $368.7M / 20% = **$2.52 a share**; whole cycle **$2.33**; 2024-25 $4.55. For comparison, half the bottom
of the conventional range is $3.86.

| | Five-year (convention) | Whole cycle | 2024-25 only |
|---|---|---|---|
| Value range | $7.71-$8.22 | $7.44-$7.92 | $14.10-$15.02 |
| Fair price, 10% pre-tax on equity | $5.05 | $4.66 | $9.10 |
| Fair price, 10% pre-tax on equity + net debt | $0.71 | $1.20 | $3.84 |
| Cheap price (20% pre-tax on equity) | $2.52 | $2.33 | $4.55 |
| Price 2026-10-05 | $6.21 | $6.21 | $6.21 |

The value range sits above the price because it discounts at the 5.66% sovereign; the fair price sits below it because the
floor asks about ten percent. The two are not in conflict: the range is what the cash is worth at the risk-free rate, the
fair price what the speakers' minimum expectancy would pay.

---
## THE BOX
**OUT at Q2** (why is the castle still standing): the filer's own 10-K states "relatively low barriers to entry" and "an
increasing number of new entrants"; the business stands by rebuilding about 13% of its customer base every year at about 2.3
years' revenue per account, its customer count has not grown organically in fifteen years, and its next two
pro-installed rivals lost money for years or went bankrupt. Not a TOO HARD, so no research pass is opened. For the record
only (COMPUTATION, not a clearance): value range $7.71-$8.22 (whole cycle $7.44-$7.92) against $6.21; fair price $5.05 on
equity ($0.71 on equity plus net debt); cheap price $2.52.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Not committed: the dispatching instruction
      forbids commits, so the write-early commits were not made; the file was written in one pass after the reading.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, together with every quoted fragment beside
      an id); every filing fact has its accession; numbers carry a filing or are labelled arithmetic or CONVENTION.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; nothing after it is a clearance (Q3-Q12 NOT REACHED; the facts
      section draws no verdict; the computation carries no entry language).
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): every capital line on the cash-flow
      statement deducted, stock pay deducted; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found, "write it down in the first 30 minutes" **[M1997-127]** (five
      items under the foundations).
- [x] No row dated after the anchor is cited (the anchor is today; this is not a point-in-time run).
- [x] Only the arithmetic lines of `tools/run.py` were used, and its capital line was corrected (it missed subscriber
      system asset expenditures).
- [x] `python tools/check_framework.py` run after writing (result recorded in the session report).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **OUT against TOO HARD at Q2 when the evidence is two-sided.** The framework separates "a castle shown on the evidence
to be filling in" (OUT) from "a castle whose future cannot be judged" (TOO HARD), but gives no rule for the case here: the
filer swears the castle is open, the rivals' failures and the flat customer count agree, and yet fifteen years of stable
attrition and rising price say the castle has not fallen. I closed OUT on the single fact of the filer's own statement
answering the money test, and record that a second analyst could close TOO HARD (NATURE) on the DIY forecast; the file
closes either way, but a holder's review would act differently on the two. A line saying whether the defender's own
statement of low barriers is by itself the evidence that a castle is open would settle it. (2) **The growth input when the
owner-cash series starts from an aberrant year.** The Q7 convention measures growth on aggregate owner cash over the five
years and caps it by Q3's absurdity rows, but names no fallback when the cap binds; I used the growth of RMR, the revenue
base, as a CONVENTION of this run. (3) **Floor on equity or on the enterprise.** The floor convention does not say whether
the ten percent is on the equity or on equity plus net debt; for a business with $7.7B of debt against a $4.5B equity the
two give $5.05 and $0.71, and the Q9 row on evaluating "on an all-equity basis" points to the second while the owner's
request names both. (4) **Divestitures inside the window.** The cash-flow statements do not segregate the businesses sold in
2023-2024, so the five-year window mixes them in; the framework has no rule for a window that straddles a change in what
the company is. (5) **The tool.** `tools/run.py` missed a custom-tagged capital line ($396-631M a year) and printed a
share count six years stale; both were caught by reading the filing, as Part VII requires. (6) **Presentation.** Operator rule
3's heading contains an em dash, which the dispatching instruction forbids; the heading is written with a hyphen and the
same words. **CONVENTIONS of this run, confessed:** the RMR growth rate as the shown-growth input when the owner-cash rate
is capped; the cheap-price rule (twice the floor, 20% pre-tax on equity); the pre-tax treatment by adding back cash taxes
paid; the inclusion of finance-lease principal among the capital lines.
