# Company Run — Shimmick Corporation (Nasdaq: SHIM) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from `Test Runs/_TEMPLATE - Company Run.md`
before any fetch (commit `be18bf5e`). Dispatched blind run under `Screens/_daily/_dispatch_brief.md`; working folder
`Test Runs/_research 2026-10-17 SHIM/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (6e5c3078): not held; `PORTFOLIO.md` has no line for SHIM, Shimmick or SCCI.*

**CONTAMINATION, declared.** (1) At session start I ran a directory listing of `Test Runs/` filtered for "SHIM|SCCI"
to check the target file name was free; it returned no matches. The brief counts a listing of `Test Runs/` as opening it,
so I declare it; nothing was seen. (2) The commit subjects shown at session start name another company's run (TSSI,
TOO HARD (NATURE) at Q1, with its Q7 figures); not used. (3) The project memory index loaded at start carries counts of
"gate-clearers" and a wave state; it names no company relevant here; not used. (4) The 10-K itself states that "most
recently Berkshire Hathaway" has provided surety bonding and that Berkshire Hathaway Specialty Insurance Company is a
lender under the revolving credit agreement (10-K, accession 0001193125-26-105064, Item 1 and Item 7). That is a filing
fact and is used only as one: who bonds and lends to the company. It is not read as a judgment by anyone on the shares.

**Lines of evidence chosen (the brief's departure: derived by me from the 10-K's Items 1, 1A and 7).** Item 1 says what
the company sells and to whom: public-sector water, dam, lock and transit construction, mostly California, with
"approximately 96% of our current backlog representing prime contracts" and nine named competitors. Item 1A and Item 7
make the following material, so these are the lines I followed: (a) contract type and fixed-price losses (fixed-price
revenue $434.9M of $492.8M in FY2025; the "Non-Core Loss Projects"); (b) project charges, claims and unapproved change
orders recorded in revenue; (c) backlog quality (cancellable, includes claims and unpriced change orders); (d) customers
and concentration (four customers over 10% of FY2025 revenue); (e) how contracts are won ("generally being made to the
lowest bidder"); (f) pricing through the last inflation (COVID-era cost overruns on fixed-price work); (g) debt, PIK
interest, leases and bonding; (h) liquidity language; (i) equity raises and their prices; (j) stock pay and the bonus
plan; (k) litigation (the AECOM Chancery suit and its release). Item 1A's going-concern search: "going concern" and
"substantial doubt" appear in none of the 10-K, the two 2026 10-Qs or the 2025 10-K (text search, no instance found).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $2.41 (close 2026-10-16; `tools/run.py`, aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 41,335,823 common, one class, par $0.01 (10-Q for the quarter
  to 2026-07-03, filed 2026-08-10, accession 0001193125-26-342455, cover as of 2026-08-07; `python Screens/cover_shares.py
  SHIM`). Cross-checks: the 10-Q balance sheet gives 41,335,823 "issued and outstanding" at 2026-07-03, so no treasury
  shares; the count includes the 4,289,500 shares sold at $3.50 in the underwritten offering that closed 2026-05-26
  (424B5 of 2026-05-22, accession 0001193125-26-237202; 10-Q note "Underwritten Offering"). The at-the-market agreement
  of 2025-09-08 (up to $7.8M, Roth Capital; 8-K accession 0000950170-25-113548) is described again in the 10-Q with no
  sales stated (text search of the 10-Q's ATM paragraphs, no instance found of shares sold under it). No 8-K after the
  10-Q reports an issuance; the 8-K of 2026-10-08 (accession 0001193125-26-418076) is a loan. Forms 3 and 4 of
  2026-10-15 were not read (insider holdings, not the count).
- **Market cap:** 41.336M x $2.41 = **$99.6M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (year to 2026-01-02), filed 2026-03-13, accession
  0001193125-26-105064 (Items 1, 1A, 7, 8 statements and the revenue, contract-balance and customer notes); 10-Q for the
  quarter to 2026-07-03, filed 2026-08-10, accession 0001193125-26-342455 (statements, MD&A liquidity, debt table); 10-Q
  to 2026-04-03, accession 0001193125-26-225083 (fetched, not read beyond its existence); 10-K for FY2024, accession
  0000950170-25-042721 (interest paid); 10-K for FY2023, accession 0000950170-24-038024 (FY2023 statements); the IPO
  prospectus (424B4 of 2023-11-15, accession 0001193125-23-277906) for FY2021 and FY2022; proxy DEF 14A of 2026-04-22,
  accession 0001193125-26-170397 (ownership, pay); 8-Ks of 2024-05-20 (0000950170-24-062130, AECOM settlement, credit
  agreement, share issuance), 2025-09-08, 2026-05-26 (0001193125-26-239410), 2026-04-28 (0001193125-26-183757) and
  2026-10-08 (0001193125-26-418076).
- **One figure cross-checked against the filed statement:** net cash used in operating activities FY2025, $(65,114)
  thousand on the filed cash-flow statement (10-K, accession 0001193125-26-105064), against `tools/run.py`'s -65.1M:
  agrees. Also FY2025 revenue $492,844 thousand on the filed statement of operations.
- **`python tools/run.py SHIM`, arithmetic lines only** (three fiscal years tagged; the earlier two from the prospectus):

| FY (USD M) | Revenue | Gross margin | Operating result | OCF | SBC | Capex | D&A | Owner cash (OCF − SBC − capex) |
|---|---|---|---|---|---|---|---|---|
| 2021 | 572.7 | (132.8) | (211.9) | (54.0) | 1.2 | 2.9 | 14.9 | **(58.1)** |
| 2022 | 664.2 | 23.5 | 12.9 | (3.1) | 2.3 | 10.4 | 16.0 | **(15.8)** |
| 2023 | 632.8 | 22.4 | 0.4 | (88.1) | 2.1 | 7.0 | 17.3 | **(97.2)** |
| 2024 | 480.2 | (55.6) | (119.3) | (21.3) | 6.1 | 10.5 | 15.1 | **(37.9)** |
| 2025 | 492.8 | 33.6 | (19.4) | (65.1) | 5.2 | 6.4 | 13.0 | **(76.7)** |
| H1 2026 | 194.6 | 23.4 | (5.0) | (24.6) | n/r | 0.7 | n/r | (25.2 before SBC) |

  Sources: FY2021 and FY2022 from the prospectus (accession 0001193125-23-277906: statement of operations and cash-flow
  statement); FY2023 from accession 0000950170-24-038024; FY2024 and FY2025 from accession 0001193125-26-105064; H1 2026
  from accession 0001193125-26-342455. Five-year average owner cash after every real cost: **$(57.1)M**, negative in every
  year. The operating results include items that flatter them: FY2022's $12.9M includes $52.5M of equity in earnings of
  joint ventures; FY2023's $0.4M includes a $31.8M gain on sale of assets; FY2024 includes a $20.7M gain (the Tracy yard
  sale-leaseback and the foundation-drilling asset sale). Excluding the gains, FY2023 is about $(31.4)M and FY2024 about
  $(140.1)M. `tools/run.py`'s alternates: finance-lease principal of $0.3M a year (capex alternate), no securities or PIK
  lines inside operating cash; the PIK interest ($3M accrued in FY2025, 10-K Item 7) is not cash and is not in OCF. Its
  line "GROWTH THE PRICE ASSUMES REFUSED" is taken as arithmetic: the base is negative.
- **The balance sheets, read before the income account** **[M2025-032]** (the run closes before Q4, so they are read here
  as the template asks). The company has filed as a stand-alone business only since the AECOM sale of January 2021, so
  "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]** cannot be had:
  six year-ends exist. USD thousands:

| Year-end | Total assets | Total liabilities | Equity | Cash | Receivables | Debt | Retained earnings |
|---|---|---|---|---|---|---|---|
| 2021-12-31 | 491,996 | 444,975 | 47,021 | 73,176 | n/r | 0 | n/r |
| 2022-12-30 | 446,799 | 395,204 | 51,595 | 77,762 | 56,430 | 0 | 49,083 |
| 2023-12-29 | 426,652 | 356,162 | 70,490 | 62,939 | 54,178 | 29,627 | 46,537 |
| 2025-01-03 | 233,864 | 268,538 | (34,674) | 33,730 | 42,988 | 9,478 | (78,211) |
| 2026-01-02 | 218,763 | 275,403 | (56,640) | 19,969 | 30,179 | 64,459 | (103,795) |
| 2026-07-03 | 224,936 | 275,258 | (50,322) | 16,875 | 31,314 | 72,389 | (113,160) |

  What moved and why. The equity of 2021 was made by the purchase, not by the business: FY2021 carried a $233.1M "bargain
  purchase gain" and $160.4M of "cash acquired in business combination", against a loss from operations of $(211.9)M and
  an $80.8M build in the forward loss reserve (prospectus cash-flow statement, accession 0001193125-23-277906); AECOM paid
  a further $32.0M "net working capital settlement" in FY2022. The seller, in effect, paid the buyer to take loss-making
  contracts, and the cash it handed over has since been spent: cash fell from $77.8M to $16.9M, retained earnings from
  $49.1M to $(113.2)M, equity to a deficit of $(50.3)M, and debt rose from nil to $72.4M. Equity was propped three times
  by new shares (the IPO, about $19M net at $7.00 in November 2023; 8,777,337 shares worth $12.9M issued in FY2024, mostly
  to AECOM under the 2024 share-issuance agreement; $13.8M net at $3.50 in May 2026) and fell anyway. Receivables fell with
  revenue, but contract assets rose from $70.1M to $122.5M between 2025-01-03 and 2026-07-03 while revenue fell (10-K
  contract-balances note; 10-Q balance sheet): retainage receivable doubled to $46.1M, and "Costs and estimated earnings in
  excess of billings" rose to $64.1M at 2026-01-02. That is revenue booked ahead of cash, in a company that records
  "change orders (approved and unapproved) and claims" in its contract price (10-K, Item 7, critical estimates). What the
  figures "can't say" **[M2025-032]**: how much of the $122.5M of contract assets is claims and unapproved change orders;
  the 10-K and 10-Q describe them and give no amount (text search for an amount beside "unapproved change orders", no
  instance found). Property, plant and equipment fell from $19.1M to $6.7M in eighteen months, the fleet being sold or
  leased back, so capex below depreciation is shrinkage, not thrift.

## THE FOUNDATIONS (not a gate)
A share is a business: would I own this "if the market closed for five years?" **[M1997-109]**; the question is what the
business will put out in cash, and on the record it has put out none in any year since it became independent. The
market serves and does not instruct **[M2006-077]**: the fall from the $7.00 IPO price to $2.41 tells me nothing about
value; the filings do. Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to
think about" **[M1996-084]**. Who is paid to tell you: the 10-K's "Business and Growth Strategy" and the featured
"Adjusted EBITDA" are the company's own case, written by the people who need the next raise to succeed, and the
underwriter of the May 2026 offering is the agent of the ATM. **Contrary evidence, written down as found** **[M1997-127]**
(I wrote these into the notes file the hour they were found): the gross margin on the post-2021 "Shimmick Projects" rose
from $12M on $356M of revenue in FY2024 to $40M on $397M in FY2025 (10-K, Item 7), the Non-Core loss projects are
"substantially completed" for the drilling part and winding down for the rest, backlog rose from $793M at 2026-01-02 to
$991M at 2026-07-03 (10-Q, Item 2), and the company reports a growing share of collaborative, open-book contracts. These
are the facts that would argue the business is turning; they are weighed at Q2.

## THE STANDING RULE
The buyer's conduct: a part-interest bought for cash, unlevered, at a size that cannot hurt the buyer, does not risk
ruin; "You never get in a position, obviously, where the other fellow can call your tune." **[M2006-079]**. Nothing in
the purchase would need borrowed money or a promise to a counterparty. The target's own exposures (a lender-controlled
budget, bonding, joint-and-several venture liability) are the target's and are Q9's, not this rule's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the framework states it:** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about
  what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**. The first step is
  "trying to identify the key variables in that particular business, and evaluating how predictable they were first"
  **[M1998-044]**.
- **What the business is, from the filing.** A heavy civil contractor: it bids for, and then builds, public water
  treatment plants, desalination, dams, levees, locks and transit lines, mostly for California public agencies, as
  prime contractor on "approximately 96% of our current backlog", self-performing much of the work with 590 union craft
  workers (10-K, Item 1, accession 0001193125-26-105064). It owns no product, no patent and no franchise; it sells its
  capacity to estimate and build, bonded by a surety, contract by contract.
- **The key variables and whether they are foreseeable.** (1) The margin at which work is won, which the 10-K says is
  set by "a competitive bid process, with awards generally being made to the lowest bidder" (Item 1A, "We work in a
  highly competitive marketplace"); (2) the accuracy of the estimate on fixed-price work, which is 88% of FY2025 revenue
  ($434.9M of $492.8M, revenue note); (3) the recovery of claims and change orders; (4) bonding capacity, which "depends
  upon our capitalization, working capital" (Item 1). None of these is a technology forecast, and the industry's own
  insiders do write the economics down: the filer and its rivals publish margins and backlog every quarter, so this is not
  a field where the insiders "would not want to put down on paper their predictions" **[M2000-105]**. What the economics of
  the field will look like in ten years is foreseeable in kind: thin margins on bid work, the same public customers, the
  same bonding constraint. The decision can be made "off the figures, forget about going further" **[M2008-069]** if they
  do not show it.
- **The doubt I hold, and where it belongs.** What I cannot foresee is whether this company will earn anything inside
  that field, given its losses since 2021. That is a question about its competitive position against rivals with more
  capital, which is Q2's castle question, not a question the industry cannot answer. A doubt about whether the business
  is inside the circle would close the file, "if you have doubts about something being into your circle of competence"
  **[M2002-092]**; I do not hold that doubt about the field. I hold it about the company's place in it, and Q2 is built
  to answer exactly that.
- Routing: not a fast-changing industry, not a financial institution, not a holding company. One reportable segment
  (10-K, segment note).
- **VERDICT: IN.** The economics of a bid-won, fixed-price public contractor can be read from its filings and its
  rivals' filings **[M2012-065]**, **[M1998-044]**; the deciding question passes to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, asked from the attacker's side, since "all moats
are subject to attack in a capitalistic system" **[M1995-038]**.

**The castle tests, each with its filing fact.**
- **What brings the customer, and how permanent is it.** The filing's own answer is price. "In the past, a majority of
  the contracts on which we bid were awarded through a competitive bid process, with awards generally being made to the
  lowest bidder" (10-K, Item 1A, accession 0001193125-26-105064); in Item 7, the "traditional public “competitive bid”
  method, in which price is the major determining factor", beside a "best value" method that weighs qualifications and
  price. The customer is a public agency bound by procurement rules, which is the customer of **[L2004-003]**: "most
  insureds don't care from whom they buy", and the low bid of **[M2017-009]**, "people buying candy for the low bid". The
  company's claimed advantages (self-perform crews, technical scopes, local knowledge) are stated as beliefs: "We believe
  this provides us with a distinct pricing advantage" (Item 7). No figure in the filings shows that advantage in the
  margins (below).
- **The attacker with money.** The 10-K answers it against itself: "there are a number of international and national
  companies in our industry that are larger than we are that, if they so desire, could establish a presence in our
  markets and compete with us for contracts" (Item 1A). It names nine of them, among them Kiewit, Granite, Fluor, Skanska
  and Flatiron Dragados (Item 1). Could a rival with a hundred million dollars take this business on? The filing says
  rivals already do, contract by contract; and of See's, "If the answer had been yes" **[M2011-015]**, it would not have
  been bought. This is a field of the kind where "there are some industries that are just never going to have barriers
  to entry" **[M2012-106]**.
- **Pricing power and the agony before a rise.** On fixed-price work there is no price rise to agonise over: the price
  is fixed at the bid and the cost is not. The loss projects "experienced significant cost overruns due to the COVID
  pandemic, design issues, legal costs and other factors" (10-K, Item 7), and the risk factors list "continuing operating
  cost inflation" as a risk of fixed-price contracts. Inflation was absorbed, not passed on: gross margin was negative in
  FY2021 and FY2024. That is the opposite of a business whose strength shows in "the agony they go through in determining
  whether a price increase can be sustained" **[M2005-020]**; this one could not raise its price at all once bid.
- **Unit volume.** Revenue fell from $664.2M (FY2022) to $492.8M (FY2025), and to $194.6M in H1 2026 against $250.5M a
  year earlier; backlog rose to $991M at 2026-07-03 (10-Q, accession 0001193125-26-342455). Backlog "may be canceled or
  modified at the election of the customer" and includes "claims, unpriced change orders" (10-K, Item 7), so it is not
  volume in hand.
- **The low-cost position.** No filing states a cost advantage. The margin record (the competitor row below) is the
  evidence of cost against rivals: negative over every span for Shimmick, positive over the cycle for Granite. In a
  commodity field "the guy with the lower cost comes in and kills you" **[M2001-013]**, and "The guy who could sell it
  cheaper than we could made it risky for us." **[M1997-010]**.
- **Brand.** Engineering News Record rankings (#8 in dams and reservoirs, #12 water supply, #11 treatment and
  desalination; Item 1) are a record of size and experience, not a customer asking for the firm by name; the award goes
  through a bid or a scored proposal.
- **Would the customer still choose it over the low bid.** The filing's answer is that the majority of awards went "to
  the lowest bidder" (Item 1A). The company's strategy is to move toward collaborative contracts chosen "largely based on
  qualifications" (Item 1), where "Currently our portfolio includes a small but growing number of these projects". The
  share is not given in any figure I found (text search of the 10-K and the 10-Q for a percentage of backlog or revenue
  under collaborative contracts, no instance found); cost-reimbursable revenue, the nearest figure, was $56.8M of $492.8M
  in FY2025 (revenue note).
- **Ask the competitors.** Not on the public record for this company; not done.
- **Widening or narrowing.** The test is "whether it’s likely to widen further or shrink on you" **[M1999-108]**. The
  company says it is replacing the AECOM-era "large scale projects with higher risk and lower margins" with "smaller to
  mid-sized projects with less risk and higher margins" (Item 1). The evidence: gross margin on the post-2021 "Shimmick
  Projects" was $12M on $356M of revenue in FY2024, $40M on $397M in FY2025, and $21M on $184M in H1 2026 (10-K Item 7;
  10-Q Item 2). That is a claimed change for the better, credited only "on the evidence of a full cycle" (Q2, Change); it
  has two years and no downturn behind it. Even taken at face value, the whole company's gross margin of $23.4M in H1
  2026 did not cover its $30.4M of selling, general and administrative expense (10-Q statement of operations).
- **What could destroy it.** The test is what will "destroy, or modify, or reduce the economic strengths" **[M2000-014]**
  five to fifteen years out: one fixed-price job that goes wrong (it happened in FY2021 and again in FY2024); the loss of
  bonding, which "depends upon our capitalization, working capital" (Item 1) when equity is a deficit; a lender's
  covenant. The company's own short history has shown each of the three in some form (the waived MidCap defaults of May
  2024 and the waived "Material Project Documents" covenant of March 2026; 8-K accession 0000950170-24-062130 and 10-K
  Item 7).

**The competitor row** (same metrics, each from the company's own filings; operating income over revenue, and profit
over equity, summed over the span; USD M). The 10-K names nine rivals (Item 1). Two file with the SEC and are used:
Granite Construction (CIK 861459) and Fluor (CIK 1124198). **Named rivals that do not file with the SEC, flagged:**
Barnard Construction, Ames Construction, Flatiron Dragados (a unit of the Spanish ACS group), Kiewit, Skanska USA (a unit
of the Swedish Skanska), Traylor Bros. and The Walsh Group.

| Company | Span | Revenue | Operating income | Op. margin over span | Profit over span against average equity | Source |
|---|---|---|---|---|---|---|
| Shimmick | FY2021 to FY2025 | 2,842.7 | (337.3) | **(11.9)%** | equity in deficit from 2025-01-03; not meaningful | accessions in Step 0 |
| Shimmick, without the purchase year | FY2022 to FY2025 | 2,270.0 | (125.4) | **(5.5)%** | as above | accessions in Step 0 |
| Granite | FY2014 to FY2025 | 38,627 | 817 | **2.1%** | 472 over twelve years on about 976 of average equity: **about 4.0% a year** | XBRL company facts as last filed; latest 10-K accession 0000861459-26-000004 |
| Fluor | FY2017 to FY2025 | 140,092 | (169) | **(0.1)%** | 313 over nine years on about 2,220 of average equity: **about 1.6% a year**, with FY2024's 2,084 of profit against 463 of operating income | XBRL company facts as last filed; latest 10-K accession 0001124198-26-000007 |

Granite's operating income by year runs 65, 110, 92, 63, 8, (42), (158), 25, 85, 80, 207, 282; Fluor's 213, 510, (828),
(232), (273), 209, 147, 463, (378). Both spans include losing years (2019 to 2021) and a recovery, so each covers a full
cycle of the field. Granite's figures for 2018 to 2021 are as last filed after its restatement; the restatement itself
was not read (flagged). The rivals' figures were transcribed from tagged data and not read in their filed statements
(flagged; operator rule 4 binds the target's filing, and these rows only set the field's returns).

**The parts table.** One reportable segment (10-K segment note), but the filer reports two parts with different
economics: Shimmick Projects (FY2025 revenue $397.2M, gross margin $40M) and Non-Core Projects (revenue $95.6M, gross
margin $(7)M) (10-K revenue note and Item 7). Five-year operating profit by part is not reported; gross margin by part is
reported for FY2024 and FY2025 only. Shimmick Projects is the largest part and the only one with positive margin, so it
decides (Q2, A business of parts: the largest part decides where none shows more than half of five-year operating
profit; here no part has five years of figures, recorded as a gap below). Its castle is the bid-won castle tested above.

**The field's returns over the last full cycle, judged in words.** Granite, the largest SEC-filing rival the 10-K
names, earned about two cents of operating income on each dollar of revenue over twelve years and about four percent a
year on its equity; Fluor earned nothing on its operations over nine. These are the field's durable players, and what
stands of their castles has protected ordinary returns at best. Shimmick earned less than either, losing money at the
operating line in four of five years once its asset-sale gains are set aside. A great business's moat "protects
excellent returns on invested capital" **[L2007-004]**; here no player shows them. The field is one where "you can have
only two competitors and they’re still terrible businesses" **[M2013-052]**, and where "the improvement you get one day,
your competitor gets the next day" **[M2004-053]**. The moat is judged, not measured: "You have to understand the
businesses." **[M1999-108]**.

**Why OUT and not TOO HARD (NATURE).** The framework sends a castle whose future cannot be judged to TOO HARD, and a
claimed change for the better is credited only after a full cycle (Q2, Change). The change here is the move to
collaborative contracts and smaller jobs. But the question that decides the box is not whether that change succeeds:
even if it succeeds in full, it brings Shimmick to the returns its field earns, and the field's own filings show those
returns to be ordinary over a full cycle. "The standing castle that protects only ordinary returns" closes OUT on that
evidence (Q2, What it rules OUT, the CONVENTION of 2026-10-06: "ordinary" judged in words, no figure). The tenuous-moat
row, "just too risky" **[M2000-019]**, sends a castle to TOO HARD because its value cannot be judged; here the returns are
known. Three more items of Q2's list of what it rules OUT apply on the filing's own words: the customer who buys on the
low bid **[L2004-003]**, **[M2017-009]**; the field without barriers **[M2012-106]**; and the business a cheaper rival can
undercut **[M1997-010]**. Price does not reopen it: the rows refuse "the idea of buying the cigar butts that are
declining or poor businesses for a bargain price" **[M2019-015]**.

- **VERDICT: OUT.** The castle is open on the evidence: contracts are won "generally" by "the lowest bidder" (10-K,
  Item 1A), larger rivals "could establish a presence in our markets" (Item 1A), and the field's durable SEC-filing players
  earned ordinary returns over a full cycle while this company lost money at the operating line in four of five years
  **[L2004-003]**, **[M2017-009]**, **[M2012-106]**, **[L2007-004]**, **[M2011-015]**. The file closes here. Q3 to Q12 are
  NOT REACHED.

## Q3 to Q10, Q12: NOT REACHED (Q2 closed the file OUT).

---
## COMPUTATION: the reporting figures at the owner's request

### COMPUTATION, NOT A CLEARANCE
*(Operator rule 3: computed after a closing STOP, carrying no entry language. A reporting convention of the brief, not a
rule; neither figure is a verdict. Script: `Test Runs/_research 2026-10-17 SHIM/q7_computation.py`.)*

- **Cash input.** Owner cash after every real cost (OCF less stock pay less all capital spending), FY2021 to FY2025:
  (58.1), (15.8), (97.2), (37.9), (76.7); five-year average **$(57.1)M** on the equity-only basis. The all-equity basis
  adds back cash interest paid (FY2021 $0.07M and FY2022 $0.16M, prospectus; FY2024 and FY2025 $2M each, 10-Ks; FY2023 not
  found and taken at the upper bound of FY2023 "Other expense, net", $2.7M): average add-back $1.4M, owner cash before
  interest **$(55.8)M**. The depreciation variant (D&A in place of capex) averages $(65.0)M equity-only, $(63.6)M before
  interest. The company's own tax: none paid on losses (FY2025 "no income tax expense was recorded"; 10-K Item 7); no
  carryforward shelter is priced, since there is no positive income for it to shelter in the computation.
- **Specifics applied.** (a) Cycle base: the company has filed only since 2021 and no year of the five is described by
  the filer as a cyclical peak or trough; the whole window is the loss-project window (the "Non-Core Loss Projects",
  10-K Item 7), so the literal window is the base and is the only window there is. (b) Decline: owner cash is negative in
  every year and more negative in the second half of the window (average (37.0) for FY2021 and FY2022, (57.3) for FY2024
  and FY2025); a compound rate on a negative series is meaningless, so **the range is the no-growth case alone, said so**.
  (c) No acquisitions in the window (the 2021 purchase of the company itself is the window's start; its $160.4M of cash
  acquired is an investing inflow from the seller and is not counted as owner cash). (d) Working capital is counted (it is
  inside OCF); no year's draw is tied by the filer to one contract. (e) The filing does not allow the maintenance guess:
  capex ran below depreciation while the fleet was being sold (PP&E $19.1M to $6.7M), so capex understates what keeps the
  business in place; the capex basis is central and the depreciation basis is shown beside. (f) The cap: not engaged.
- **Net debt** at 2026-07-03 (10-Q debt table, face amounts): Credit Agreement $61.3M + ACF $3.5M + Ansley $10.1M =
  $75.0M, less unrestricted cash $16.9M = **$58.1M**; operating leases ($10.7M non-current) left out, said so. After the
  10-Q, the 8-K of 2026-10-08 (accession 0001193125-26-418076) adds a $14.3M equipment loan at 9.31% and repays Ansley:
  at most about $4.2M more if fully drawn, shown here and not added.
- **VALUE RANGE (COMPUTATION):** no-growth case at the 5.43% sovereign, all-equity basis: whole business **$(1,085)M**,
  **$(26.25) a share**; depreciation variant $(29.73) a share. The range is a single case and lies wholly below zero,
  against a price of **$2.41**. Equity-only beside it: $(25.46) a share (capex basis). The floor is tested first: **no
  case earns the floor at the price**, nor at any positive price, so the computation also closes OUT (Q7, the floor
  tested first), whatever the width.
- **FAIR PRICE (COMPUTATION, a reporting figure, never a verdict):** each end valued at ten percent and averaged (one end
  here): all-equity basis (central) **$(14.90) a share**, equity-only **$(13.83) a share**, both after the company's own
  tax (nil). There is no positive price at which the midpoint of this range earns the floor. No cheap price is reported.
- **The most favourable reading the filings allow, as a check on the sign.** The Shimmick Projects' FY2025 gross margin
  of $40M (10-K Item 7), with the loss projects assumed gone entirely, less the company's FY2025 selling, general and
  administrative expense of $54.6M, is still $(14.6)M before interest, depreciation of the remaining fleet and working
  capital. The sign of the range does not depend on the discount rate, the window or the basis.

---
## THE BOX
**OUT**, decided at **Q2** (the castle is open: contracts won on the low bid, larger rivals free to enter, and the
field's durable SEC-filing players earning ordinary returns over a full cycle while this company lost money at the
operating line in four of five years). Computation beneath the stop: value range $(26.25) a share, a single no-growth case
wholly below zero, against $2.41; fair price $(14.90) all-equity, $(13.83) equity-only. **Integrity facts recorded, not
judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box is unchanged, operator rule 2.)*

- **Q3 (capital).** Property, plant and equipment net fell from $19.1M (2025-01-03) to $6.7M (2026-07-03) (10-K;
  10-Q). Working capital is the capital: contract assets $122.5M, retainage receivable $46.1M at 2026-01-02 (10-K
  contract-balances note). The business consumed cash in every year of the window (Step 0). The 10-K calls the industry
  "capital-intensive" with "significant fixed and semi-fixed costs" (Item 1A).
- **Q4 (the accounts).** Revenue is recognised over time on cost-to-cost; contract prices include "change orders
  (approved and unapproved) and claims on those contracts that we conclude to be enforceable" (10-K, critical estimates);
  no amount of unapproved change orders or claims is given (text search, no instance found). The forward loss reserve
  was $35.9M at 2026-01-02, down from $52.1M (contract-balances note). The 10-K features "Adjusted net loss" and
  "Adjusted EBITDA", adding back stock pay, transformation costs and "legal fees and other costs for Non-Core Projects"
  (Item 7). The company is an emerging growth company presenting two audited years; auditor Deloitte & Touche (proxy).
  The speakers name "construction in progress or progress payment-type things" among the places where "so many ways you
  can cheat in accounting" **[M2013-086]**; recorded, not weighed.
- **Q5 (the people; integrity facts).** A controlled company: GOHO, LLC (Executive Chairman Mitchell B. Goldsteen) holds
  20,974,873 shares, 57.8%, and AECOM 6,714,448, 18.5% (proxy, accession 0001193125-26-170397, on 36,300,928 shares);
  the company uses the controlled-company exemptions for its board and compensation committee (10-K Item 1A). The seller
  sued: AECOM v. SCCI National Holdings, Inc., et al., Delaware Chancery Court C.A. No. 2022-0727-MTZ, dismissed with
  prejudice under the mutual release of May 2024, in which the company released AECOM "from all claims" and issued AECOM
  7,745,000 shares (8-K accession 0000950170-24-062130; the complaint was not read). The same day the MidCap facility's
  amendment "waives all existing defaults", and a side letter with AECOM required a Special Committee of independent
  directors to oversee "the budget and use of funds under the Credit Agreement", asset sales and "certain compensation
  matters", and a chief transformation officer (same 8-K). Chief executive turnover: Steven Richards was CEO "from March 2020 through December 2024"
  and retired from the board at the 2026 annual meeting (8-K of 2026-03-31, accession 0001193125-26-132130); Ural Yal
  CEO effective 2024-12-02 (proxy); Sarah Tacker, from FlatironDragados, chief operating officer from 2026-04-28 (8-K
  accession 0001193125-26-183757). A run of
  Form 144 notices from June to August 2025 and Forms 4 (submissions index); not read.
- **Q6 (money and owners).** Shares went from 25,493,877 (2023-12-29) to 41,335,823 (2026-08-07), up 62% in under three
  years: the IPO of 3,575,000 shares at $7.00 (November 2023), 8,777,337 shares issued in FY2024 for $12.9M (most of
  them to AECOM under the release, which agreed 7,745,000), restricted-stock vesting, and 4,289,500 shares at $3.50 in May 2026 ($14.0M net); an
  ATM for up to $7.8M stands open (10-K equity statement; 10-Q; 8-Ks). No buyback, no dividend. Stock pay $6.1M (FY2024)
  and $5.2M (FY2025). The CEO's 2025 pay was $1,547,445, including a $720,000 non-equity incentive in a year of a $25.6M
  net loss; his offer letter sets a bonus "target award equal to 120% of base salary and a guaranteed minimum award equal
  to 80% of base salary", and the CFO's 90% and 70% (proxy). The speakers name systems "that payoff no matter what
  happens" **[M1999-018]**, and companies "hell-bent on issuing shares" **[L2014-015]**; recorded, not weighed.
- **Q9 (debt and exposures).** Total debt $72.4M net at 2026-07-03 against an equity deficit of $(50.3)M; total
  liquidity $33M (cash $17M, availability $4M and $12M) (10-Q Item 2). The main credit agreement (lenders AECOM and
  Berkshire Hathaway Specialty Insurance) bears SOFR plus 3.50% with a 1% floor, interest payable "in kind or in cash at
  our election", $3M of PIK accrued in FY2025, a leverage covenant tested from Q2 2027, liens on "substantially all
  assets", amended eleven times by 2026-10-02 and in March 2026 to waive a covenant breach on non-bonded contracts (10-K
  Item 7; 8-K accession 0001193125-26-418076). Bonding: "We have pledged proceeds and other rights under our contracts to
  our bond surety company"; AECOM is credit support for the Non-Core bonds (10-K Item 1A, Item 7). Joint-venture
  liability is "usually joint and several" and the company is "unable to estimate the maximum potential amount of future
  payments" (Item 7). Customers: four over 10% of FY2025 revenue (19.1%, 13.3%, 11.7%, 11.3%); one customer 38.8% of
  receivables at 2026-07-03 (10-K and 10-Q notes). Multiemployer pension plans are named as a risk (Item 1A). The 10-K
  and 10-Q state the cash is sufficient "for at least the next twelve months" and that "Our future success will be highly
  dependent on our ability to access outside sources of capital" (Item 7). "count on the kindness of strangers"
  **[L2008-019]**; recorded, not weighed.
- **Q12.** Nothing found that bears on it.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `be18bf5e`); written question by question; committed after each
      (Step 0 `b3a2d295`, Q1 `c27f1308`, Q2 `05e5535f`, then this section).
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's (not checked by
      me, by the brief); the fold into the register is the dispatcher's (operator rule ten). A run not in the register binds
      nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One filtered listing of `Test Runs/`
      was run at the start and returned nothing; declared under contamination, with the commit subjects and memory lines
      seen at start.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-17 SHIM/check_ids.py` (ids
      exist, no E-ids, every quoted fragment beside an id is in that row); every filing fact carries its accession or its
      document and note.
- [x] The order was kept; Q2's STOP closed the run; everything after it is headed COMPUTATION, NOT A CLEARANCE or is
      under AFTER THE STOP.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); sovereign from the US Treasury; the
      price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the notes file and the foundations paragraph); facts for later questions
      under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Weak points I own: the rivals' figures are tagged data, not read in their filed statements; FY2023 cash interest was
  not found and was bounded; the Forms 4 and 144, the 2026-04-28 8-K text and the AECOM complaint were not read; the
  10-K's statement that "most recently Berkshire Hathaway" provides bonding was seen and used only as a fact.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Q2's change-for-the-better rule and the ordinary-returns rule meet here without a rule for which
governs.** The company claims a turn (new projects at higher margins, more collaborative contracts) with two years and no
downturn behind it, which Q2, Change, sends to TOO HARD (NATURE) with a re-look condition; the field's own filings show
ordinary returns over a full cycle, which Q2's list sends to OUT. I closed OUT on the reading that a change which, if it
succeeds, only reaches the field's ordinary returns cannot reopen the box, so the change need not be judged; the text
does not say this, and another analyst could close TOO HARD (NATURE). A sentence saying that the ordinary-returns test is
applied to the field before the change test is applied to the company would settle it. (2) **The parts paragraph assumes
five years of operating profit by part.** Shimmick reports two parts (Shimmick Projects and Non-Core Projects) with gross
margin only, and only for two years; I took the largest part as deciding, which the convention allows "where no part
does", but the threshold cannot be computed at all and the text does not say what to do then. (3) **Q4's eight-to-ten
year balance-sheet reading cannot be done for a company carved out five years ago**, and nothing says whether the
predecessor's years (here, the AECOM era, which was never filed separately) should be sought or the shortfall simply
recorded; I recorded it. A smaller point: the Q7 range convention gives no case for an owner-cash series negative in every
year; specific (b) gets there through "meaningless" growth and "the no-growth case alone", but a stated line for an
all-negative base (the range is below zero and the floor test closes it) would save the next run the reasoning.
