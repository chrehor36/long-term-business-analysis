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

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses
where the business will be in 10 years" **[M2000-037]**; knowing the product is not enough, "We just don’t know the
economics of it 10 years from now" **[M2000-104]**. The quick decision is made from the documents **[M2008-069]**,
**[M2005-015]**, and they were read first (Step 0).

**What the business is, from the filings.** Three parts that matter. Google Services, more than 70% of 2025 revenue from
online advertising (10-K FY2025, Item 1A, `0001652044-26-000018`), with Search & other at $224,532M of $402,836M of 2025
revenue and Services operating income of $139,404M. Google Cloud, $58,705M of 2025 revenue and $13,910M of operating
income, $44,796M of revenue in the first half of 2026 alone and a revenue backlog of $513.9B (10-Q Q2 2026,
`0001652044-26-000071`). And the company-wide AI build that feeds both: capital spending of $32.3B (2023), $52.5B (2024),
$91.4B (2025), $80.6B in the first half of 2026, with "2026 capital expenditures ... expected to be $180-$190 billion" and
"2027 capital expenditures to significantly increase compared to 2026" (EX-99.1, `0001193125-26-257724`), funded in part
by over $85B of new debt and an $80B equity raise. A holding company is understood when each part that matters can be
understood (CONVENTION, Q1, the holding company by its parts) **[M2002-092]**.

**The key variables, and how predictable each is** **[M1998-044]**.
1. *Search queries and what an advertiser pays for them, ten years out.* The filer: "We believe AI is quickly reshaping
   the advertising industry ... There is no assurance that we will adapt effectively and competitively to meet this
   shift", and "the consumers may change how they obtain information online, potentially reducing the utility of our
   existing products and services" (10-K FY2025, Item 1A). Its competitor list now includes "AI model developers and
   providers of AI products and services". The variable is a change in how people look for information, under way now,
   whose end state no one has filed.
2. *What the AI capital earns.* The 2026 budget alone is about four times the owner cash of any year 2023 to 2025
   ($46,166M to $49,964M), and 2027 is to be higher. Whether that capital earns more than a dollar per dollar depends on
   prices for compute and models set "as a host of competitors battle for supremacy" **[L2009-005]**: the filer says "AI
   technology and services are highly competitive, rapidly evolving, and require significant investment" and that others
   "may develop AI products and technologies that are similar or superior to our technologies or more cost-effective to
   develop or deploy" (10-K FY2025, Item 1A). The $513.9B backlog says what customers have committed to buy, not what the
   capital will earn after the build.
3. *The legal shape of distribution.* The December 2025 final judgment in the search case "imposes restrictions on how
   Google distributes its services and requires Google to share certain search data with and offer syndication services
   to certain competitors"; appealed January 2026 (10-Q Q2 2026, legal matters).

**The tests, applied.**
- *Do the past statements tell me the future ones?* **[M2008-033]**. No, and the filer says so: "our historical revenue
  growth rate and historical operating margin may not be indicative of our future performance" (10-K FY2025, Item 1A).
  The statements of 2016 to 2024 describe a business that spent a fraction of its operating cash on plant; the 2026
  statements describe one whose first-half capital spending ($80,598M) nearly equalled its operating cash ($84,859M), with
  owner cash after stock pay about minus $10.9B for the half (Step 0). The past is "only useful to you in the extent to
  which it gives you insights into the future, and sometimes the past doesn’t give you any insights into the future"
  **[M2007-025]**.
- *Would the insiders write it down?* **[M2000-105]**. The best-informed insiders, the filer's own management, write that
  the business "is characterized by rapid change as well as new and disruptive technologies" and give no assurance of
  adapting; they commit $180-190B for one year without a stated return. No filing read states where search monetization
  or the return on the AI build will stand in ten years.
- *Can I name the winner, not just the industry?* **[M2012-067]**, **[M2014-097]**. The AI industry's growth is visible in
  the filings (Cloud revenue, backlog); which participants will earn good returns on capital in it is not, which is the
  case **[L2009-005]** names.
- *Is the forecast about customers or about technology?* **[M2017-019]**, **[M2023-030]**. Both, and the customer half is
  the moving one: whether people keep typing queries into a page that carries paid links, or ask an assistant whose
  answers carry fewer. Consumer habit can be projected where it does not change **[M2002-050]**; here the filer itself
  names the change.
- *How far off could I be?* **[M2011-084]**. Very far. Owner cash after every real cost could, ten years out, be a
  multiple of the $46,997M five-year mean if the build earns well, or stay near or below zero for years if it does not;
  the speakers set this exact contrast against Google in 2012, "The chances of being way wrong in IBM are probably less,
  at least for us, than being way wrong with Google" **[M2012-073]**.
- *Do I doubt it is inside?* **[M2002-092]**. Yes, so it is not.

**Contrary evidence, carried and answered** **[M1997-127]**. The search franchise is growing, not shrinking (Q2 2026
Search & other +16.8%, paid clicks +13%); Cloud's profit and backlog are rising fast; Berkshire Hathaway bought in; and
the speakers once judged Google's economics visible and counted the miss as their error **[M2017-021]**, **[M2019-024]**,
**[M2001-006]**. Answered: the rows that call the miss an error describe the economics of a click bought by GEICO,
"that’s a good business, unless somebody’s going to take it away from you" **[M2017-021]**; the 2026 question is that
qualifier itself, and the same speakers said of Google, "The mystery was how much competition would come along, and how
effective they would be" **[M2018-088]**, and earlier, "other people will always understand those two companies better
than we do. We have the reverse of an edge" **[M2012-072]**. Current growth is the past, and "You don’t get paid for
what’s already happened" **[M2007-025]**. Another buyer's purchase is not this analyst's understanding **[M1994-014]**.

**Routing.** Fast change that puts the ten-year economics out of reach closes here, at Q1, in TOO HARD, not OUT: "it won’t
make it through the filter" **[M1998-008]**; "We view change as more of a threat into the investment process than an
opportunity" **[M1999-063]**; "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its
worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. This is no finding that the castle is open
(that would be Q2's OUT); it is a finding that its future cannot be foreseen from here.

**The cause: NATURE, not WORK.** The deciding question, what search earns and what the AI capital earns in a field still
being fought over, is one the industry's insiders do not write down (test 5, **[M2000-105]**), and the rows say more
study does not cure it: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying
those industries" **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we have no insights into
which participants in the tech field possess a truly durable competitive advantage" **[L1999-018]**. A wider margin of
safety would not cure it **[M2007-022]**, a lower price does not reopen it **[M2000-038]**, and the circle is not widened
to find something to buy **[M1995-018]**.

**VERDICT: TOO HARD (NATURE).** The ten-year earning power of the search franchise under AI substitution, and the return
on capital spending of $180-190B in 2026 rising in 2027, cannot be foreseen from the filings or by the filer, so the
whole cannot be understood by its parts **[M2012-065]**, **[M2000-105]**, **[L2009-005]**, **[M2002-092]**,
**[M2006-013]**. The file closes here; Q2 to Q12 are NOT REACHED.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1). No competitor row was filled, because the castle tests are not run.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED. (The capital figures in Step 0 are arithmetic, recorded, not weighed.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion.
NOT REACHED. Recorded for a later reader, not judged: non-marketable equity securities of $124.3B at 2026-06-30, "of which
$87.9 billion was remeasured at fair value during the three months ended June 30, 2026" (10-Q Q2 2026), which would bear
on reported net income against owner cash.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED (operator rule 2: no Q5 output without Q1 to Q4 IN).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Recorded, not judged: $45.4B of repurchases in 2025 (10-K FY2025), none in the first half of 2026 (10-Q
cash flow statement), then about $80B of new equity offered from June 2026, of which "approximately $30 billion of ATM
program proceeds will be used to meet these 2026 calendar year tax obligations" on vesting employee equity awards
(EX-99.1, `0001193125-26-257724`).

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED. No value range was built. (COMPUTATION — NOT A CLEARANCE: the only valuation arithmetic in this file is
Step 0's yield, owner cash of $46,997M five-year mean against a cap of $4,237,328M, 1.11% against a 5.66% sovereign. It
carries no entry language and clears nothing.)

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED. What the framework would have the buyer do: nothing; inaction is the default **[M1996-006]**.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT ASKED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** The ten-year economics of search under AI substitution and the return on an AI
build of $180-190B in 2026, rising in 2027, are a forecast the filer itself declines to write down **[M2000-105]**,
**[L1999-018]**; the run did not reach Q7, so no range stands beside the price ($346.47, cap $4,237,328M). NATURE is the
closed box: no research file is opened (Part VII applies to WORK only), and a lower price does not reopen it
**[M2000-038]**. **What would reopen it is a change in the business, not the price:** the AI build reaching a level where
several years of filed statements again show search revenue and owner cash after stock pay and all capital spending
settling, so that the past statements tell the future ones (test 3, **[M2008-033]**). Q11 belongs to the holding review.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `713291d`); written question by question; committed after Step 0
      (`3297325`) and after Q1 (`77660ef`) with a pathspec; this section in the final commit.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`: 44 ids before this section, none
      missing); every filing fact has its accession; the one CONVENTION of this run (one class price for all three
      classes) is labelled, and the Q1 by-parts reading is the framework's own CONVENTION, named as such.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance; Q5 output was not produced
      (operator rule 2); the only valuation arithmetic is headed COMPUTATION — NOT A CLEARANCE (operator rule 3).
- [x] Owner cash after every real cost (operating cash less all stock pay less all capital spending), never a net-income
      proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found **[M1997-127]**: in the foundations (four items) and answered at Q1.
- [x] No row dated after the anchor is cited: this is a run of today, not a point-in-time test; no row is later than 2025.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The speakers' own verdicts on the very company.** The framework and the ledger carry the speakers' views of Google
by name (**[M2012-071]**, **[M2012-072]**, **[M2012-073]**, **[M2017-021]**, **[M2018-088]**, **[M2019-024]**), and they
pull both ways: "the reverse of an edge" in 2012, "we blew it" in 2017 and 2019, with **[M2019-049]** against
**[M2019-024]** carried OPEN in section VI. Part VII's anchor CONVENTION governs only point-in-time tests; nothing says how
a live run should treat a row that is a verdict on the name being run. This run read them as evidence of method about an
earlier business and decided on the 2026 filings, and it says so; a rule would stop two analysts diverging here.
(2) **Q1 against the omission error.** **[M2001-006]** counts a missed business "we understand" as the real error, and the
speakers counted Google as such; Q1's doubt rule **[M2002-092]** sends the same name to TOO HARD. The framework does not
say how to tell an understood business passed over from one honestly outside the circle when the speakers themselves
called it inside; this run used the change since 2017 (the AI build, the filer's own disclaimer) as the separating fact.
(3) **Test 5 and a capital commitment.** "Would the insiders write it down?" **[M2000-105]**: the management writes no
forecast, but it commits $180-190B, which is an implicit one. The framework does not say whether a commitment of capital
counts as writing the forecast down; this run read it as not, because no return is stated. (4) **The by-parts
CONVENTION** is written for a holding company; Alphabet is one company with segments and a shared AI build that crosses
them; the run applied it to segments, which the text neither allows nor forbids. (5) **The template's share and cap lines**
give no rule for classes that carry identical rights but trade at different prices, nor a line for dilutive securities
known at the run date but not in the cover count (here a $15B mandatory convertible preferred and a $40B ATM); both were
handled in Step 0 and confessed. **Tool notes, no tool edited:** `tools/run.py` heads its owner-earnings block "(OCF −
SBC) − maintenance capex" while its columns deduct all capital spending (the honest figure, wrongly labelled);
`Screens/cover_shares.py` reports the cover in the filer's rounded millions (the filer's own rounding, not a defect, but
the exact count is not on this cover); and run.py has no interim line, so the negative first half of 2026 was computed by
hand from the 10-Q.
