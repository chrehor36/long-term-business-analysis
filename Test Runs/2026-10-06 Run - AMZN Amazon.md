# Company Run — Amazon.com, Inc. (NASDAQ: AMZN) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run from the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch (commit `0a17bc9`). Every
judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes
the run and later questions are marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-06 AMZN/` (tool outputs,
the fetch scripts `fetch.py` and `idx.py`, the owner-cash arithmetic `owner_cash.py` and its output, and the ledger rows
read, `rows.txt`; raw filings and text dumps sit in its `cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the queue register, the prepped reading list and `tools/alerts.json` were not opened,
and no attempt was made to learn whether the operator holds or wants this name.

**CONTAMINATION, declared.** (1) No earlier run file or research folder for AMZN was opened or listed by name; the
directory listing of `Test Runs/` used to find a form example was filtered to files dated 2026-10-05, and one of them, the
ETN run, was read (its first ninety lines) for form only. (2) The ledger itself carries the speakers' own remarks on this
company (M2012-045, M2012-046, M2016-012, M2016-065, M2017-022, M2017-080, M2019-022, M2019-024, M2025-056); they are
v5 rows, not an earlier run, and are cited below where they bear, with the reading rule that a speaker's admiration is
not a forecast. (3) My training memory of Amazon (a founder-led retailer that built the largest cloud business) is a
prior; every fact below is from the filings, and where the filings moved past the prior (the scale of the 2026 build, the
OpenAI and Anthropic stakes, the doubled debt) I record it as found.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$251.40** (2026-10-05, live quote via `tools/run.py`; aggregator, flagged per operator rule 5, used for
  the quote only).
- **Shares:** one class of common stock. The 10-Q for the quarter ended 2026-06-30 (filed 2026-07-31, accession
  `0001018724-26-000026`) gives **10,786,313,572** shares outstanding on its cover as of 2026-07-22
  (`python Screens/cover_shares.py AMZN`, which read the same filing; the balance sheet of the same 10-Q gives 10,783M at
  2026-06-30, and 11,298M issued including treasury). The 10-K says "shares outstanding plus outstanding stock awards"
  were 11.0 billion at 2025-12-31 (10-K FY2025, MD&A overview).
- **Market cap:** $251.40 × 10,786.3M = **$2,711.7B** (`owner_cash.py` and `tools/run.py` agree).
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 10/05/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-06, accession `0001018724-26-000004` (Item 1, Item
  1A to the operating risks, MD&A in full, the four statements, Note 1 on useful lives, Note 10 segment information);
  10-Q for Q2 2026, filed 2026-07-31, `0001018724-26-000026` (MD&A liquidity and results, Note 5 debt, stock repurchase
  note); proxy DEF 14A filed 2026-04-09, `0001104659-26-041026` (CD&A summary, Summary Compensation Table, beneficial
  ownership); the latest earnings release, 8-K of 2026-07-30, EX-99.1, `0001018724-26-000024`; 8-K of 2026-02-27,
  `0001104659-26-021050` (the OpenAI equity commitment, Item 1.01, and its EX-99.1); 8-K of 2026-06-10,
  `0001104659-26-072140` (a $17.5B delayed-draw term loan, Items 1.01 and 2.03); 8-K of 2026-09-09,
  `0001018724-26-000036` (a director elected, Item 5.02). History: 10-K for FY2022, `0001018724-23-000004` (the filed
  cash-flow statement for 2021 and 2022).
- **One figure cross-checked against the filed statement:** operating cash flow 2025, $139,514M in the XBRL facts
  (`tools/run.py`) and $139,514M on the filed Consolidated Statement of Cash Flows (10-K FY2025, page 36). Agrees. Gross
  purchases of property and equipment 2025, $131,819M, also agree.
- **`tools/run.py AMZN`, arithmetic lines only** (Part VII; its v4 wording, ids and floor were ignored). Its stock-pay
  column is complete (the `ShareBasedCompensation` line every year). Its capex basis does **not** pick up the filed line
  "Proceeds from property and equipment sales and incentives" ($3.5B to $5.7B a year), so its capex basis overstates
  net capital spending by that much; and its main column leaves out the principal repayments of finance leases, which
  its alternate column adds. Both read by hand instead, below.

**Owner cash after every real cost** (operating cash flow, which adds stock pay back, less stock pay, less purchases of
property and equipment net of the filed proceeds and incentives, less the principal repaid on finance leases and
financing obligations, which is how much of the equipment was paid for; USD millions; every input from the filed
cash-flow statements, 10-K FY2022 for 2021 and 2022, 10-K FY2025 for 2023 to 2025; `owner_cash.py`):

| year | OCF | stock pay | P&E purchases | proceeds and incentives | lease and obligation principal | **owner cash** | D&A | D&A variant |
|---|---|---|---|---|---|---|---|---|
| 2021 | 46,327 | 12,757 | 61,053 | 5,657 | 11,325 | **−33,151** | 34,433 | −863 |
| 2022 | 46,752 | 19,621 | 63,645 | 5,324 | 8,189 | **−39,379** | 41,921 | −14,790 |
| 2023 | 84,946 | 24,023 | 52,729 | 4,596 | 4,655 | **8,135** | 48,663 | 12,260 |
| 2024 | 115,877 | 22,011 | 82,999 | 5,341 | 2,712 | **13,496** | 52,795 | 41,071 |
| 2025 | 139,514 | 19,467 | 131,819 | 3,499 | 1,885 | **−10,158** | 65,756 | 54,291 |
| five-year mean | | | | | | **−12,211** | | 18,394 |

The D&A variant is OCF less stock pay less depreciation and amortization (which already includes the amortization of
finance-lease assets); it equals `tools/run.py`'s "OE D&A" column. Per share: −$1.13 on the five-year mean, $1.71 on the
variant; against the price, −0.45% and 0.68%, beside a sovereign of 5.66%. The trailing twelve months to 2026-06-30 are
worse again: OCF $161,403M against net purchases of property and equipment of $169,007M, the filer's own "free cash flow"
an outflow of $7,604M before stock pay and lease principal (10-Q Q2 2026, MD&A, non-GAAP reconciliation). These lines
are computation, not clearance (operator rule 3); Q7 is where they would be used.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the analyst's habits: "What do I not know that I need to know?" **[M1999-129]**, and
the warning that the forecast is the trap here. Amazon's own filings carry more forward-looking language about
technology than about any figure (the 10-K's MD&A: "advances in technology, specifically the speed and reduced cost of
processing power [...] and the practical applications of artificial intelligence and machine learning, will continue to
improve users’ experience"), and "macro conclusions are — just never enter into the discussion" **[M2000-094]**: the AI
trend is a forecast and is kept out of every question below except as the fact the filer reports about its own
spending. Second, a share is a business **[M1997-109]**: at $2.7 trillion the price capitalises a cash stream that has
been negative after every real cost in three of the last five years, so whatever the buyer is paying for lies in years
the filings do not yet show. Third, the market serves and does not instruct **[M2006-077]**; and who is paid to tell you
**[M2020-037]**: the release leads with run rates and growth percentages ("AWS is booming, growing 36.7% year-over-year"),
not with the cash after the build.

**Contrary evidence, written down as found** **[M1997-127]**: (a) against the prior that Amazon is a low-capital
retailer: the 2025 capital spending of $131.8B was 2.5 times 2023's $52.7B, and the first half of 2026 ran at $96.3B
against $55.6B a year earlier (10-K FY2025; 10-Q Q2 2026); (b) against the prior that the cloud's assets are durable:
"Effective January 1, 2025 we changed our estimate of the useful lives of a subset of our servers and networking
equipment from six years to five years. The shorter useful lives are due to the increased pace of technology
development, particularly in the area of artificial intelligence and machine learning" (10-K FY2025, Note 1), a year
after lengthening them from five to six; (c) against a clean balance sheet: face value of long-term debt went from
$68.8B at 2025-12-31 to $133.0B at 2026-06-30 (10-Q Note 5), with a $17.5B delayed-draw term loan added (8-K
2026-06-10); (d) against the reported earnings: Q2 2026 net income of $62.6B "includes non-operating pre-tax other income
of $53.4 billion, primarily from our investments in Anthropic" (EX-99.1, 2026-07-30); (e) in Amazon's favour, and
written down because it pulls the other way: operating income rose from $68.6B (2024) to $80.0B (2025) and from $37.6B to
$51.3B in the first half of 2026, AWS sales grew 37% in Q2 2026, and the speakers say of the stores "It’s very hard to
find people who have done business with Amazon that are unhappy about the transaction. They have happy customers."
**[M2012-046]**.

## THE STANDING RULE
Bought for cash, unlevered, at a size the buyer can hold through a fall of half, a share of Amazon puts the buyer at no
risk of ruin; the rule binds the buyer's financing and sizing, and borrowing to buy is ruled out **[L2014-005]**,
**[M2012-081]**. Nothing about the target changes this line; the target's own debt and commitments would be weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" and "some notion of how the industry will develop and where the company will stand within the
industry" **[M2012-065]**; "a reasonable probability of being able to asses where the business will be in 10 years"
**[M2000-037]**. Knowing the product is not the test: "We understand what it does for people. We just don’t know the
economics of it 10 years from now." **[M2000-104]**. Amazon reports three segments and holds large stakes outside them,
so it is read by its parts, and a part that matters and cannot be understood keeps the whole outside (CONVENTION, section
VI of the framework; **[M2002-092]**).

**The parts, from the filings** (10-K FY2025 `0001018724-26-000004`, MD&A and Note 10; 10-Q Q2 2026
`0001018724-26-000026`, MD&A):

| part | 2025 sales | 2025 operating income | share of 2025 operating income | H1 2026 operating income | share of H1 2026 |
|---|---|---|---|---|---|
| North America (stores, sellers, advertising, Prime) | $426,305M | $29,619M | 37% | $17,390M | 34% |
| International | $161,894M | $4,750M | 6% | $3,141M | 6% |
| AWS (compute, storage, database, AI services, chips) | $128,725M | $45,606M | 57% | $30,782M | 60% |
| consolidated | $716,924M | $79,975M | | $51,313M | |

Outside the segments: an equity commitment to buy $35.0B of OpenAI Series C preferred, beside an initial investment, the
whole announced as "Amazon will invest $50 billion in OpenAI" (8-K 2026-02-27, `0001104659-26-021050`, Item 1.01 and
EX-99.1); $28.7B of it paid in the first half of 2026 and "the remaining Commitment Amount of $21.3 billion" funded after
June 30; $10.0B more into Anthropic preferred in Q2 2026 (10-Q, liquidity). And inside "Technology and infrastructure",
"the development of a satellite network for global broadband service and autonomous vehicles for ride-hailing
services" (10-K, MD&A).

**Test 2, the key variables and how predictable they are** **[M1998-044]**. The part that carries most of the earnings is
AWS, and its key variable is now what the capital going into it will earn. The filings show the size of that capital and
how fast it is changing:
- AWS property and equipment, net: $72,701M (2023), $110,683M (2024), $190,055M (2025); AWS net additions to property
  and equipment $24,843M, $53,267M, $96,496M in the same years (10-K Note 10). AWS segment assets $108,533M, $155,953M,
  $252,588M; AWS operating income on year-end segment assets was 25.5% in 2024 ($39,834M / $155,953M) and 18.1% in 2025
  ($45,606M / $252,588M), arithmetic from the same note.
- Consolidated cash capital spending "primarily reflect investments in technology infrastructure (the majority of which
  is to support AWS business growth) [...] both of which we expect to increase in 2026" (10-K, liquidity); $96.3B in the
  first half of 2026 against $55.6B (10-Q); the trailing year's free-cash-flow outflow is put down to purchases of
  property and equipment, "This increase primarily reflects investments in artificial intelligence" (EX-99.1,
  2026-07-30, `0001018724-26-000024`).
- The life of the assets is itself moving with the technology: servers lengthened from five to six years in 2024, then a
  subset shortened back to five in 2025 "due to the increased pace of technology development, particularly in the area
  of artificial intelligence and machine learning" (10-K, Note 1).

So the ten-year earning power of the largest part turns on the return that a build of $96.5B of AWS net additions in 2025 alone, the build the filer ties to artificial intelligence, will earn
across chip generations whose economic life the filer has changed twice in two years. That is "a technological
component that’s of significance" **[M1998-008]**, in an industry the filer itself describes as "rapidly evolving and
intensely competitive" and in which "Each of our businesses is also subject to rapid change and the development of new
business models and the entry of new and well-funded competitors" (10-K, Item 1, Competition, and Item 1A). The rows
send that case here: "Our criterion of "enduring" causes us to rule out companies in industries prone to rapid and
continuous change" **[L2007-005]**; "there are many businesses — industries where it’s very hard to evaluate moats. There
— those are the businesses of rapid change." **[M2001-069]**; "whenever we look at a business and we see lots of change
coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**.

**Test 3, do the past statements tell me the future ones?** **[M2008-033]**. No. The five-year owner cash in Step 0 runs
−$33B, −$39B, +$8B, +$13B, −$10B, and each swing is a change in the build rate, not in the business's earning power: the
2021–22 fulfillment build, its pause in 2023–24, the AI build from 2025. The statements record where the capital went,
not what it will return.

**Test 5, would the insiders write it down?** **[M2000-105]**. The filer does not: its guidance runs one quarter ahead,
an operating-income range of $22.5B to $26.5B for Q3 2026, "subject to substantial uncertainty. Our results are inherently
unpredictable" (EX-99.1); the 10-K says "We are not always able to accurately forecast our growth rate" and that "any
projections of future cash needs and cash flows are subject to substantial uncertainty" (Item 1A; MD&A liquidity). If the
people spending the money will not write down one year, the ten-year economics of the build are not in the documents.

**Test 6, can I name the winner, not just the industry?** **[M2012-067]**, **[M2014-097]**. The growth of AI computing may
be visible; "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge
what its profit margins and returns on capital will be as a host of competitors battle for supremacy." **[L2009-005]**.
The 10-K names among the competitors "companies that provide information technology services or products, including
on-premises or cloud-based infrastructure, tools and services relating to artificial intelligence", some with "greater
resources" and "greater control over inputs critical to our various businesses", and the release names the two largest
AI laboratories as both Trainium customers and investees. Who earns what in that field in ten years is the question the
rows say cannot be answered "by studying up" **[L1999-018]**.

**Test 7, is the forecast about customers or about technology?** **[M2017-019]**, **[M2023-030]**. For the stores it is
partly about customers, and the speakers' one reading of them is favourable **[M2012-046]**. But even there the 10-K names
"web search engines, comparison shopping websites, social networks, web portals, virtual assistants [...] including
through artificial intelligence" as competitors for the customer's first click, and the rows warn that retail is where
it is "easy to sort of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**. For AWS
the forecast is about technology. By the parts rule, the stores cannot carry the whole when 57% to 60% of the operating
income sits in the part that cannot be foreseen.

**Test 9, do I doubt it is inside?** Yes, so it is not: "if you have doubts about something being into your circle of
competence, it isn’t." **[M2002-092]**; and the edge is drawn narrow on purpose **[M2005-101]**.

**What the speakers said of this company** (rows, not forecasts). They placed it outside their own circle and said so
without regret: "it was not at all obvious that it was all going to work as well as it did. I don’t feel any regret
about missing out on the achievements of Amazon." **[M2017-080]**; "I don’t mind not having caught Amazon early. The guy
is kind of a miracle worker." **[M2019-024]**; "Charlie and I are not going to out-Bezos Bezos, by a long shot."
**[M2016-012]**; and "both in the cloud and in retail, there are a lot of people that would aim that silver bullet at
Jeff." **[M2017-022]**. The speakers' rule on such misses fits: a miss outside the circle "is not an error, as far as
we’re concerned" **[M2001-006]**.

**Contrary evidence, written down** **[M1997-127]**. (1) The rows carry an open tension against this verdict: BYD, bought
"surfing along on the developing edge of new technology" **[M2010-095]** against avoiding futures that cannot be evaluated
**[L2009-005]**; the framework carries it OPEN (section VI, Q1), and the speakers' bridge was a judgment of people, which
Q1 does not admit in place of the economics. (2) Apple was read as "much more of a consumer products business"
**[M2017-019]**; the same reading fits Amazon's stores and Prime, and fails for AWS, whose customers are "developers and
enterprises" buying "on-demand technology services" (10-K, Item 1). (3) AWS has been profitable for every year the
segment note shows here and its operating income rose 14% in 2025 and 42% in the first half of 2026; a record of
profit is not a fix on the return of the capital now going in, and "we would not want to buy things on the basis that these returns
would be sustained" is the rows' caution against reading it forward (Q3, **[M1998-016]**, cited as the framework cites it).

**VERDICT: TOO HARD (NATURE).** The economics of the part that earns most of the money cannot be foreseen ten years out,
because they turn on the return of an AI-computing build in an industry of rapid change whose insiders, the filer
included, will not write down more than a quarter **[M1998-008]**, **[L2007-005]**, **[M2000-105]**. The cause is the
industry, not unread work: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying
those industries." **[L1993-023]**; "Our problem -- which we can't solve by studying up" **[L1999-018]**. It is no judgment
of quality: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just
means that we don’t know how to evaluate it." **[M2000-038]**; the box is "too hard" **[M2006-013]**, and a
lower price does not reopen it. The circle is not widened to find something to buy **[M1995-018]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED. Q1 closed the file TOO HARD (NATURE). The competitor row was not built.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED. (The capital figures in Step 0 and Q1 are recorded as filing facts for the Q1 test, not weighed here.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. Facts noticed in passing and left for any later run, not weighed: net income in 2025 and in Q2 2026 is
swollen by non-operating marks on the Anthropic stake ($15.2B of other income in 2025, $53.4B in Q2 2026); the server
lives were lengthened in 2024 and shortened in 2025; the filer's non-GAAP measure is free cash flow before stock pay and
lease principal, and it gives a one-quarter guidance range; the Q3 2026 guidance excludes "energy derivative contract
remeasurements", a line not met elsewhere in the documents read.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. (Facts read for Step 0 only: the chief executive's 2025 salary was $365,000 with no stock award that year
and no cash bonus programme, per the proxy's Summary Compensation Table and CD&A; the founder and executive chair
beneficially owned 950,434,581 shares, 8.8%, per the proxy's ownership table. Not weighed.)

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range was computed. The owner-cash lines in Step 0 are computation, not clearance (operator rule 3).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. (Recorded as found, not weighed: long-term debt at face $68.8B to $133.0B in six months, 10-Q Note 5; a
$17.5B delayed-draw term loan, 8-K 2026-06-10.)

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** The part that earns 57% to 60% of the operating income, AWS, is in the middle of an
AI-computing build whose ten-year return cannot be foreseen and which the filer itself will not forecast past one
quarter **[M1998-008]**, **[L2007-005]**, **[M2000-105]**, **[L1999-018]**. No range was computed; price $251.40,
market cap $2,711.7B, sovereign 5.66%. The cause is the industry's, not unread work, so no research pass is opened (Part
VII applies to TOO HARD (WORK) only), and a lower price does not reopen it **[M2000-038]**. What would change the box is
the business, not the price: the build ending, and AWS then showing several years of stable returns on a segment asset
base that has stopped doubling, so that its ten-year economics become a record that can be read rather than a forecast
of a technology. That is written as the condition of a new run, not as a promise that one would pass. Q11 (has the
business changed, or only its price) belongs to the holding review, not to a purchase run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `0a17bc9`, before the first EDGAR request); written question by
      question; committed after Step 0 (`572ba02`), after Q1 (`7d7fe2f`) and at the close.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv`; the rows read are saved in `rows.txt`, which shows
      none missing; M1998-016 checked separately); every filing fact has its accession; the percentages and ratios are
      arithmetic on filed figures, with both inputs shown.
- [x] The order was kept; Q1, the first STOP, failed and closed the run; nothing after it is a clearance, and the facts
      noted under Q4, Q5 and Q9 are marked not weighed.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): stock pay, all purchases of property
      and equipment net of the filed proceeds, and lease and financing-obligation principal deducted; the sovereign from
      the US Treasury; the price quote flagged as aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: five items in the foundations, three in Q1.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the anchor is
      today and every row is earlier.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its capex basis was corrected by hand (below).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts rule has no threshold for "matters".** Q1's CONVENTION says a part "that matters to its earnings" and
cannot be understood keeps the whole outside. Here the unreadable part is 57% to 60% of operating income, so nothing
turned on it; but the stores alone are 37% and could have been argued either way, and with a 20% part the rule would
give no answer. I applied the rule as written to the part that is plainly material and did not grade the stores. (2) **A
NATURE box caused by a phase, not by the industry for ever.** Section I says no further work is done on TOO HARD (NATURE)
and a lower price does not reopen it, but says nothing of a business whose unreadable stretch is a build that may end;
I wrote the reopening condition as a change in the business (THE BOX), which is my reading, not a rule. (3) **Q7's range
cannot run on a negative five-year mean.** Not reached here, but the CONVENTION carries the five-year mean of owner cash
forward at the growth shown; Amazon's mean is −$12.2B while its depreciation variant is +$18.4B, and the framework does
not say whether a mean made negative by growth spending is a "cannot be valued" STOP or a case for the depreciation
variant with the maintenance judgment of Q3. A run that reached Q7 on such a name would have to invent the answer.
(4) **The speakers' own remarks on the named company.** The ledger holds nine rows about Amazon; the framework has no
rule on how a speaker's opinion of the very company enters (as a row like any other, as contamination, or not at all).
I cited them as rows, declared them at the top, and did not let them decide the verdict. **Tool defects, reported, not
fixed:** `tools/run.py` (a) misses the filed line "Proceeds from property and equipment sales and incentives" for AMZN
($3.5B to $5.7B a year), which is not under the tags it reads, so its capex basis overstates net capital spending;
(b) leaves finance-lease principal out of its main owner-earnings column (it appears only in the alternate), although for
AMZN in 2021 it was $11.2B; (c) still prints a three-year mean as its headline while v5's Q7 CONVENTION uses five years
(it does print the five-year window beside it). `Screens/cover_shares.py` read the 10-Q cover correctly.
