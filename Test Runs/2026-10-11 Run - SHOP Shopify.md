# Company Run — Shopify Inc. (Nasdaq: SHOP) — 2026-10-11
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-11, after the run was committed: not held (`PORTFOLIO.md` read for this one ticker; SHOP appears in no account, only in the opportunity set).*

**Dispatch.** A dispatched blind run under the canonical brief `Screens/_daily/_dispatch_brief.md`, slots filled by the
overnight cycle of 2026-10-11. The brief's one stated departure: the lines of evidence are derived by the analyst from the
FY2025 10-K, not listed by the dispatcher. They are named below, under "Lines of evidence chosen".

**Contamination declared.** Seen by accident and not used: the session's git-status snapshot listed untracked research
folders of other companies (AYI, ARCB) and recent commit subjects about another company's fold (SBUX); the memory index
loaded into the session names queue states and counts of other runs in general terms. None of it names Shopify. No other
run file, holding review, `PORTFOLIO.md`, the register, the reading list or the resume-state file was opened, listed or
searched.

**Lines of evidence chosen** (the analyst's choice, from Item 1, Item 1A and Item 7 of the FY2025 10-K,
0001594805-26-000007): (1) from Item 1, what the business sells and how it is paid: subscription solutions and merchant
solutions, the GMV the second rides on, and the competition paragraph; (2) from Item 1A, the risk factors on the pace of
change in the field ("constant change and innovation"), on AI and agentic commerce, on competitors and large technology
platforms, and on the payment service providers (Stripe and PayPal) behind Shopify Payments; (3) from Item 7, the key
indicators (MRR and GMV), the revenue mix and what drives merchant solutions; (4) the balance sheets FY2016 to FY2025 and
the cash-flow statements, for the computation and for the facts recorded after the stop; (5) the FY2021 40-F MD&A, for
the filer's own description of 2021, the first year of the five-year window.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $170.85 (close 2026-10-09, the last trading day before the run date; from `tools/run.py`, an aggregator, live
  quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 1,208,570,347 Class A subordinate voting shares, 78,073,584 Class B
  restricted voting shares and 1 Founder Share, as of 2026-07-31 (10-Q for the quarter to 2026-06-30, filed 2026-08-05,
  accession `0001594805-26-000047`; `python Screens/cover_shares.py SHOP` gives the same three lines). Charter note read
  (10-K FY2025, note on share capital): Class A one vote, Class B ten votes, "The Class B restricted voting shares are
  convertible into Class A subordinate voting shares on a one-for-one basis at the option of the holder", and the two
  classes are "treated equally and identically, on a per share basis, in certain change of control transactions". A and B
  are therefore added as one economic class: **1,286,643,931 shares**. The Founder Share carries a variable number of
  votes, cannot convert, and is left out of the economic count (one share; immaterial either way). Check against the
  equity statement: 1,289,206,588 shares outstanding at 2026-06-30 (10-Q equity statement), less repurchases in July
  consistent with the cover's lower count; the 10-K cover gave 1,304,111,373 (A and B) at 2026-02-06, and 16,859,976
  Class A shares were repurchased in the first half of 2026 (10-Q note on the repurchase program). No 8-K after the
  10-Q states a share issue (8-Ks of 2026 listed from the EDGAR submissions index; the 2026-08-05 8-K, accession
  `0001594805-26-000046`, furnishes the Q2 results release only).
- **Market cap:** $219,823M (1,286.64M shares at $170.85).
- **Sovereign for the earnings currency:** 5.60%, the US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`). The reporting currency is the US dollar (10-K, Presentation of Financial Information);
  revenue is earned in many currencies, the statements are in USD.
- **Filings read** (operator rule 4): the 10-K for FY2025, filed 2026-02-11, accession `0001594805-26-000007` (Items 1,
  1A, 7 and the financial statements and notes); the 10-K/A filed 2026-04-29, accession `0001594805-26-000011` (Part III,
  compensation and governance: read for the facts recorded after the stop, not weighed); the 10-Q for the quarter to
  2026-06-30, accession `0001594805-26-000047`; the 8-K of 2026-08-05, accession `0001594805-26-000046`; the 40-F for
  FY2021, accession `0001594805-22-000011` (its financial statements, `shop-20211231_d2.htm`, and its MD&A exhibit). The
  40-F years FY2016 to FY2020 and FY2022 to FY2023 are taken from their XBRL facts as `tools/run.py` and the company-facts
  file transcribe them; their filed statements were not opened (stated under what could not be got). The Canadian
  management information circular was not read; the 10-K/A carries Part III.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $2,033M on
  the filed Consolidated Statement of Cash Flows (10-K, `0001594805-26-000007`), equal to the XBRL figure `tools/run.py`
  prints. A second: FY2021 operating cash, $504,428 thousand on the filed 40-F statement (`0001594805-22-000011`), equal
  to the XBRL $504.4M.
- `python tools/run.py SHOP` arithmetic lines only (saved in `Test Runs/_research 2026-10-11 SHOP/run_py_output.txt`):
  operating cash less stock pay less capital spending, by year, $290M (2023), $1,167M (2024), $1,558M (2025); capital
  spending $39M, $19M, $26M against depreciation and amortization $70M, $36M, $31M; stock pay $615M, $430M, $449M. The
  tool's share basis was a weighted average of two classes and stale; the cover count above is used instead. Nothing the
  tool prints as a rule, a yield verdict or a v4 id is used (Part VII, the tooling).

### The balance sheets, FY2016 to FY2025, read before the income account **[M2025-032]**
*(Read here in Step 0 because the file closes before Q4, as the template asks. USD millions; FY2023 to FY2025 from the
filed FY2025 10-K statements; earlier years transcribed from the filings' XBRL, first-filed vintage; "cash and
securities" is cash plus current marketable securities plus long-term debt-security investments where reported.)*

| year-end | total assets | equity | paid-in share capital | accumulated surplus (deficit) | cash and securities | trade and other receivables | loans and merchant cash advances | goodwill | convertible notes | revenue |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 491 | 411 | 469 | (83) | 392 | 10 | 12 | 16 | 0 | 389 |
| 2017 | 1,114 | 1,001 | 1,078 | (123) | 938 | 22 | 47 | 20 | 0 | 673 |
| 2018 | 2,255 | 2,091 | 2,216 | (188) | 1,970 | 41 | 47 (tag vintage; not checked) | 38 | 0 | 1,073 |
| 2019 | 3,489 | 3,016 | 3,256 | (304) | 2,455 | 91 | 92 | 312 | 0 | 1,578 |
| 2020 | 7,763 | 6,401 | 6,115 | 15 | 6,388 | 121 | 150 | 312 | 758 | 2,930 |
| 2021 | 13,340 | 11,133 | 8,040 | 2,938 | 7,768 | 192 | 245 | 357 | 911 | 4,612 |
| 2022 | 10,757 | 8,239 | 8,747 | (522) | 5,053 | 273 | 580 | 1,836 | 913 | 5,600 |
| 2023 | 11,299 | 9,066 | 9,201 | (390) | 5,123 | 282 | 816 | 427 | 916 | 7,060 |
| 2024 | 13,924 | 11,558 | 9,634 | 1,629 | 6,188 | 342 | 1,224 | 452 | 918 | 8,880 |
| 2025 | 15,189 | 13,473 | 10,376 | 2,860 | 6,753 | 500 | 1,784 | 491 | 0 | 11,556 |
| 2026-06-30 (10-Q) | 14,470 | 12,684 | 8,636 | 3,781 | 5,472 | 466 | 2,184 | 491 | 0 | (half year 6,753) |

What the figures say, and what they do not **[M2025-032]**: (1) **Equity was raised, not earned, for most of the span.**
Paid-in share capital went from $469M to $10,376M, while the accumulated deficit stood at $304M as late as 2019; the
surplus of $2,860M in 2025 is largely the net of unrealized gains and losses on equity investments carried at fair value
(net unrealized gain $1,424M in 2023 and $988M in 2024, loss $186M in 2025, income statement of the FY2025 10-K), not
retained operating earnings. (2) **Goodwill jumped to $1,836M in 2022 and fell to $427M in 2023**: the 2022 purchase of a
logistics business (acquisitions $1,753.7M cash in 2022, XBRL) and the 2023 sale of "Shopify's logistics businesses",
with an impairment of $1,340M (FY2025 10-K income statement, 2023 column); the sale was for stock (equity method
investment $780M at 2023-12-31). (3) **A lending book has grown faster than sales**: loans and merchant cash advances from
$12M (3% of revenue) in 2016 to $1,784M (15% of revenue) in 2025 and $2,184M at 2026-06-30; net loan originations run
through investing cash flow ($523M, $464M, $579M in 2023 to 2025) and merchant cash advances through operating cash.
(4) **Receivables stay small against sales** (about 3% to 6% of revenue across the span); no build-up of the kind
**[M1995-064]** warns of was found. (5) **Debt**: one convertible issue, carried at $758M to $918M from 2020, repaid in
2025 ($1,043M maturity payment, with a realized loss on an embedded derivative of $123M, FY2025 10-K); no borrowings at
2026-06-30. (6) **Cash and securities** of $5,472M at 2026-06-30 against no debt; equity and other investments of
$4,854M beside them ($3,299M carried at fair value) and an equity method investment of $559M. (7) What the balance sheet
cannot say: anything about where GMV and the take rate stand in ten years, which is the question below.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which turns on the business's ten-year economics, the same thing Q1 asks. The market serves and does not
instruct: a price of $219,823M for the equity tells "It just tells us prices." **[M2006-077]** and is no evidence of value. No macro
forecast enters. Who is paid to tell you: the brief carries no expected verdict, and the analyst has no position.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the 10-K states that "the total annual revenue generated
by each of our previous cohorts has grown on a generally consistent basis" (Item 1, `0001594805-26-000007`), which is a
long record of merchant behaviour, the kind of customer forecast **[M2017-019]** allows; (b) GMV of $378.4B in 2025, up
29%, and Shopify Payments penetration rising (Item 7); (c) owner cash turned positive in 2024 and 2025 after losses in
2022 and 2023; (d) no merchant has ever been more than five percent of revenue (Item 1); (e) an app ecosystem of more than
21,000 apps (Item 1). Each is weighed at Q1 below.

## THE STANDING RULE
The run is blind to the buyer's financing and size. Nothing in the target's filings bears on the buyer's conduct; the rule
binds the buyer: no borrowed money **[L2014-005]**, and never "risk what we have and need for what we don’t have and
don’t need" **[M2012-081]**. Not engaged by this file, which closes before any purchase question.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it.** "can I understand it?" **[M1995-051]**, where understanding is "a reasonable
probability of being able to asses where the business will be in 10 years" **[M2000-037]** ("asses" is the transcript's
spelling), "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
and "some notion of how the industry will develop and where the company will stand within the industry" **[M2012-065]**.
Understanding the product is not the test: "We just don’t know the economics of it 10 years from now" **[M2000-104]**.

**What the business is, from the filing.** Revenue of $11,556M in 2025: subscription solutions $2,752M (24%) and merchant
solutions $8,804M (76%), the second "principally" payment processing and currency conversion fees from Shopify Payments,
plus lending, referral fees, shipping labels, hardware and advertising (Item 1 and income statement,
`0001594805-26-000007`). Merchant solutions revenue is "directionally correlated" with GMV (Item 7). Merchant solutions
revenue was 2.33% of GMV in 2025 ($8,804M on $378,441M) and 2.21% in 2023 ($5,223M on $235,910M), arithmetic on Item 7
and the income statement.

**The key variables, and how predictable they are** **[M1998-044]**. (1) GMV on the platform in ten years: how much of
the world's online and in-store commerce merchants run through Shopify rather than through a marketplace, a rival platform
or software of their own. (2) The take on that GMV: how much of the merchant's payment, lending and checkout spend Shopify
keeps against payment processors and the channels where buyers now shop. (3) The cost of staying current: research and
development of $1,536M (13% of revenue) and stock pay of $449M in 2025 (income statement and cash-flow statement).

**What the filer says about the predictability of those variables.** From Item 1A of the FY2025 10-K
(`0001594805-26-000007`), in its own words:
- "The markets in which we compete are characterized by constant change and innovation and we expect them to continue to
  evolve rapidly."
- "This includes our ability to successfully translate our vision for agentic commerce into solutions that our merchants
  can effectively adopt and utilize. If we fail to effectively integrate AI tools into our products, the utility of our
  platform could diminish relative to our competitors."
- "We operate in new and developing markets that may not develop as we expect and elements of our business strategy are
  new and subject to ongoing development. We have encountered and will continue to encounter risks and difficulties
  frequently experienced by growing companies in rapidly changing industries".
- "We also expect new entrants to offer competitive services and merchants may also seek to build their own solutions,
  including using advanced tools such as AI."
- On larger rivals and platforms: "certain competitors could use strong positions in one or more markets to gain a
  competitive advantage against us [...] by [...] integrating competing platforms, applications or features into products
  they control", and "large technology platforms have imposed and are considering imposing [...] restrictions on the
  ability of other parties to access or use data from their customers and users."
- "Shopify does not currently develop its own foundational AI models" and relies on third-party models whose providers
  may "decline to partner with us".
- Shopify Payments rests on agreements with Stripe and PayPal, each of which "automatically renews every 12 months, unless
  either party terminates the agreement earlier".
From Item 1, Competition: "Our market is transforming, competitive and highly fragmented, and we expect competition to
increase in the future", and among "the principal competitive factors": "pace of innovation" and "ability to leverage
emerging technologies, including AI".

**The tests, applied.**
1. *Where will it be in ten years?* **[M1999-132]**: the ten-year Value Line page cannot be printed here. The two key
   variables depend on where commerce is transacted in ten years (storefronts, marketplaces, social channels, or AI agents
   that discover and check out for the buyer) and who keeps the checkout. The filer calls its own market "transforming".
2. *Key variables predictable?* **[M1998-044]**: "If something is not very predictable, forget it." GMV share and take
   rate are not predictable from the filings: the filer itself names the forces that could move both, and names none it
   controls (its AI models, payment rails and some channels belong to others).
3. *Do past statements tell me the future ones?* **[M2008-033]**: the past statements show a business whose operating
   result swung from $269M (2021) to a loss of $1,418M (2023, after a $1,340M impairment on a strategy built and abandoned
   inside two years) to $1,468M (2025). The filer's own words on one line: "historical patterns in our business may not be
   a reliable indicator of our future performance" (Item 1, Seasonality; said of seasonality, quoted only for that).
4. *Important and knowable?* **[M2006-076]**: the deciding variable is important and, on this evidence, not knowable.
5. *Would the insiders write it down?* **[M2000-105]**: the filer, the insider closest to the business, writes that its
   markets will "continue to evolve rapidly" and "may not develop as we expect". That is the industry's own refusal to
   put the ten-year economics on paper, the test's sign of NATURE.
6. *Can I name the winner, not just the industry?* **[M2012-067]**, **[L2009-005]**: the growth of online commerce is easy
   to see; who keeps the economics of it as "a host of competitors battle for supremacy" **[L2009-005]** is not.
7. *Customers or technology?* **[M2017-019]**, **[M2023-030]**: the strongest case for the business is here, and it is
   written down: the cohort record is a record of merchant behaviour. But the forecast that decides is not whether
   merchants like the tool today; it is whether the tool, the payment rail and the channel stay Shopify's while the
   technology of buying changes. The filer ranks "pace of innovation" and AI among the principal competitive factors.
   That is a forecast about technology, the IBM side of **[M2017-019]**, not the consumer side.
8. *How far off could I be?* **[M2011-084]**: very far. Ten years of 26% revenue growth (2021 to 2025, arithmetic on the
   income statements) or a reversal to the 2022 kind are both inside what the filing allows.
9. *Doubt?* **[M2002-092]**: "if you have doubts about something being into your circle of competence, it isn’t." There is
   doubt.
10. *Do I only think I understand it?* **[M1997-024]**: the product is easy to describe, which is the trap **[M2000-104]**
    names.

**The routing.** Where "the future technology could hurt the business as it presently exists", "it won’t make it through
the filter" **[M1998-008]**; and the framework's routing paragraph (settled 2026-10-05) closes a business whose ten-year
economics cannot be foreseen because its industry changes fast at Q1, in TOO HARD. The rows give the reason: "a business
that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics"
**[L1993-023]**; "whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass
on that" **[M1999-063]**; "We think Microsoft is a sensational company run by the best of managers. But we don’t have any
idea what that world is going to look like in 10 or 20 years." **[M1996-059]**.

**The cause: NATURE, not WORK.** The deciding question (GMV share and take rate in ten years, as the channels and tools of
commerce change) is a forecast the industry's own participant declines to write down **[M2000-105]**, and no filing not
yet read could answer it: "Our problem -- which we can't solve by studying up -- is that we have no insights into which
participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**; "We couldn't solve this
problem, moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**. WORK was
considered and rejected: a research pass could read rivals' filings and Shopify's older 40-Fs, but none of them states
where agent-led checkout, payment rails and platform access will stand in 2036.

**What the box is not.** It is no finding against the business: "It doesn’t mean it isn’t a good buy. It doesn’t mean it
isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. A miss
here is not counted as an error, because the business lies outside the circle **[M2001-006]**. The technology label is not
the reason (a label alone would not close the file **[M2022-077]**); the filer's own description of its field is.

**VERDICT: TOO HARD (NATURE)** **[M2006-013]**. Filing fact: Item 1A of the FY2025 10-K (`0001594805-26-000007`), "The
markets in which we compete are characterized by constant change and innovation and we expect them to continue to evolve
rapidly", with the agentic-commerce and AI risk factors quoted above. The file closes. Q2 to Q12 NOT REACHED.

## Q2 — NOT REACHED
The competitor row was not compiled. Recorded for a later run: the 10-K names no competitor by name, only categories
(ecommerce software vendors, content management systems, payment processors, point of sale providers, marketplaces and
others, Item 1); Stripe and PayPal are named as Shopify's payment service providers, not as rivals; so no named rival's
filings were read (the brief's instruction is to the rivals the 10-K names, and it names none).

## Q3 — NOT REACHED
## Q4 — NOT REACHED (the balance sheets were read in Step 0, above)
## Q5 — NOT REACHED
## Q6 — NOT REACHED
## Q7 — NOT REACHED (the reporting figures are computed below under COMPUTATION, NOT A CLEARANCE)
## Q8 — NOT REACHED
## Q9 — NOT REACHED
## Q10 — NOT REACHED
## Q12 — NOT REACHED

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the ten-year economics of a field its own filer calls "characterized by constant
change and innovation" cannot be foreseen **[M2000-104]**, **[L1993-023]**, **[M2000-105]**. No integrity facts were
found in the filings read (none of the kind Q5 asks about was searched for beyond the 10-K/A pay section); the box line
carries no integrity flag. Q7 was not reached; the computation below shows the price above the top of every case, for
the operator's figures only.

## COMPUTATION, NOT A CLEARANCE — the two reporting figures
*(The owner's reporting convention, Part VII, The owner's price and How the fair price is computed. Q1 closed the file;
nothing here is a verdict or entry language (operator rule 3). Arithmetic in `Test Runs/_research 2026-10-11 SHOP/q7_computation.py`,
output in `q7_output.txt`.)*

**Owner cash, FY2021 to FY2025** (USD millions; operating cash less stock pay less capital spending less net loan
originations less acquisitions, on the all-equity basis with interest income taken out after tax):

| | 2021 | 2022 | 2023 | 2024 | 2025 | five-year mean |
|---|---|---|---|---|---|---|
| operating cash | 504.4 | (136.4) | 944 | 1,616 | 2,033 | |
| stock pay | 330.8 | 549.1 | 615 | 430 | 449 | |
| capital spending | 50.8 | 50.0 | 39 | 19 | 26 | |
| net loan originations (investing) | 31.3 | 158.6 | 523 | 464 | 579 | |
| acquisitions, net of cash acquired | 59.6 | 1,753.7 | 31 | 30 | 56 | |
| interest income after tax | 11.3 | 58.1 | 177.1 | 226.4 | 243.3 | |
| **owner cash, all-equity, acquisitions deducted (central)** | **19.3** | **(2,712.3)** | **(460.6)** | **421.7** | **653.0** | **(415.8)** |
| organic pair, acquisitions left out | 78.9 | (958.6) | (429.6) | 451.7 | 709.0 | (29.7) |
| equity-only, interest kept, acquisitions deducted | 31.9 | (2,647.8) | (264.0) | 673.0 | 923.0 | (256.8) |

Sources: FY2023 to FY2025 from the filed FY2025 10-K cash-flow statement (`0001594805-26-000007`); FY2021 operating cash,
stock pay and acquisitions checked on the filed 40-F statement (`0001594805-22-000011`); FY2022 lines and the FY2021 loan
lines from the filings' XBRL. CONVENTIONS of this run, each confessed: (i) net loan originations are counted as capital
spending, by the working-capital specific (d), since the lending book is capital the business must put up to earn its
lending revenue; the variant that leaves them out is shown beside; (ii) interest income is taken out at the 2025 effective
tax rate (18.4%, $278M on $1,509M of pre-tax income), so as not to count the net cash twice on the all-equity basis;
rationale: the convention adds net cash to the range per share; (iii) net cash is cash, marketable securities and
long-term debt-security investments at 2026-06-30, $5,472M, with no borrowings; the equity investments carried at fair
value ($3,299M) are shown beside and not added, since their value is a market quote, not cash the business produces.
Rationale for (iii): the convention's "cash and securities, as the filing states them" does not say which securities.

**The range by Q7's range convention, applied in full.**
- Five-year window FY2021 to FY2025; aggregate owner cash, not per share; all spending deducted (the depreciation variant:
  depreciation exceeded capital spending in every year, so it lowers owner cash further; not material at this scale).
- Specific (a), cycles: the filer describes 2021, the first window year, as carrying "the COVID-triggered acceleration of
  ecommerce that spilled into the first half of 2021" (FY2021 40-F MD&A, `0001594805-22-000011`), so 2021 is aberrational
  on its own description. Owner cash in 2021 was low (19.3), not high, so taking 2021 out lowers the mean (to (524.6) on
  FY2022 to FY2025); no full owner-cash cycle can be read in the series. The literal window is kept and shown.
- Specific (b), decline: the series changes sign and the first half of the window (mean (1,346.5)) against the second
  (537.4) gives no meaningful rate. **The range is therefore the no-growth case alone, said so.**
- Specific (c), acquisitions: deducted (central); the organic pair beside. A merger inside the window (the 2022 logistics
  purchase, sold in 2023 for stock) is inside the averages; crediting the stock received at its 2023 carrying value ($780M)
  as proceeds would raise the central mean to (259.8), still negative.
- Specific (e), growth spending: the filing does not allow a maintenance guess; research and development is expensed and
  not split. Not applied.
- Specific (f), the cap: not reached, since no growth is carried.

**(a) VALUE RANGE (COMPUTATION):** the no-growth case alone. All-equity: (415.8) / 5.6% = $(7,425)M, plus net cash
$5,472M = $(1,953)M, **$(1.52) a share** (equity-only: (256.8) / 5.6% = $(4,585)M, **$(3.56) a share**). On the
convention the business's five-year owner cash is negative and the shares are worth no more than the net cash, $4.25 a
share ($6.82 with the fair-value equity investments), against **$170.85**.

**(b) FAIR PRICE (COMPUTATION):** the one end case valued at ten percent: (415.8) / 10% = $(4,158)M plus $5,472M =
**$1.02 a share, all-equity, the central figure**; equity-only (256.8) / 10% = **$(2.00) a share**, beside. Company's own
tax throughout (owner cash after the company's income tax, no conversion).

**Beside, generous to the business and NOT the convention's figure** (shown so the operator can see how far the price is
from any case): take the 2025 year alone as the base and carry it ten years at the business's own revenue growth, 25.8% a
year (FY2021 to FY2025), then no growth, at 5.6%:
- on the central definition (base 653.0): range **$13.32 to $71.53 a share**, all-equity; fair price at ten percent
  **$22.23**;
- with loans not deducted and acquisitions left out (base 1,288.0): range **$22.13 to $136.96**; fair price **$39.71**.
At $170.85 the price is above the top of every case shown. At ten percent the most generous case is worth $65.16 a share.
If Q7 had been reached, no case would have earned the floor at the price, and Q7 closes OUT in that event
(the floor tested first, 2026-10-10). The box stays TOO HARD (NATURE) at Q1.

The market value implies owner cash many times the record: $214,351M of enterprise value against 2025 central owner cash
of $653.0M is a yield of 0.3%, against a long government rate of 5.6%.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged, operator rule 2.)*
- **Q2.** The 10-K names no rival by name (Item 1). Merchant solutions revenue rose from 2.21% of GMV (2023) to 2.33%
  (2025), arithmetic on Item 7 and the income statement. Shopify Payments rests on Stripe and PayPal agreements renewing
  every twelve months (Item 1A). The filer states that "we anticipate that our growth rate will decline over time to the
  extent that the number of merchants using our platform increases and we achieve higher market penetration rates" (Item 1A).
- **Q3.** Property and equipment of $53M; capital spending $19M to $51M a year (2021 to 2025). The capital the business
  actually employs includes a lending book of $1,784M at 2025 and $2,184M at 2026-06-30, growing faster than revenue.
  Shareholders put in $10,376M of paid-in share capital by 2025 (balance sheet).
- **Q4.** Stock pay $449M in 2025 (3.9% of revenue), $615M in 2023. Net income swings with unrealized gains and losses on
  equity investments ($1,424M gain 2023, $988M gain 2024, $186M loss 2025; $1,249M gain in the second quarter of 2026,
  10-Q). "Revenue related to non-cash consideration" of $49M (2025), $94M (2024), $158M (2023) is deducted in operating
  cash (cash-flow statement). An impairment of $1,340M in 2023 on the sale of the logistics businesses. A realized loss of
  $123M on the convertible's embedded derivative in 2025. The filer states its key indicators, MRR and GMV, are not
  non-GAAP measures (Item 7); no adjusted-earnings figure was looked for in the releases.
- **Q5 and Q6.** Founder control: the Founder Share gives Tobias Lütke, with his family and affiliates, "at least 40%" and
  at most 49.9% of the votes, a voting power that "could be substantially greater than the economic interest of the shares he holds" (10-K Item 1A).
  The CEO takes a C$1 base salary and his 2025 pay was granted in stock options valued at $35,000,026 (10-K/A,
  `0001594805-26-000011`). Employees choose their mix of cash, options and RSUs under "Flex Comp" (10-K/A). The company
  bought a logistics business for $1,753.7M cash in 2022 and sold it for stock in 2023 at an impairment of $1,340M.
  A repurchase program of $5,000M was authorized in 2026; 16,859,976 shares were bought in the first half of 2026 at an
  average $114.63, $1,933M in all (10-Q note). The board stated no price limit in the note read.
- **Q9.** No borrowings at 2026-06-30; cash and securities $5,472M (10-Q). Exposure to merchant credit through the lending
  book and to transaction losses ("Transaction and loan losses" $417M in 2025, up from $227M in 2024, income statement).
- **Other.** The 8-K of 2026-08-05 gives the principal executive office as Las Vegas, Nevada (the 10-K gave Ottawa and New
  York); the company remains a corporation under the Canada Business Corporations Act per the 10-K; no rename, merger or
  continuance was seen in the filings read.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `212b488b`). Only one question closed (Q1); Step 0, the
      balance sheets, Q1, the computation and the facts after the stop were written into the file and committed together
      when Q1 closed, then this audit was committed. Stated plainly: the sections were drafted in one pass before the
      Q1 commit rather than each committed on its own, which write-early prefers.
- [x] Dispatched: the brief allowed per-question pathspec commits of the run file and research folder; the lock is held by
      the dispatching session (not checked by the analyst); the fold is the dispatcher's (operator rule ten). A run not in
      the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination and not used.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-11 SHOP/check_ids.py`); every filing fact has its
      accession; no number without a row or a filing; the run's own conventions are labelled.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance; the computation is headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority (US Treasury); the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as found (Foundations, and test 7 at Q1); facts for later questions are under
      AFTER THE STOP; no integrity flag in the box line, since no integrity fact was found in the filings read.
- [x] No row dated after the anchor is cited (not a point-in-time run; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the commit (run 2026-10-11); the run's own check
      (`check_ids.py`): no E-ids, 32 v5 ids all in the ledger, 15 quoted fragments beside ids all in their rows.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The computation after a Q1 STOP has no rule for a negative five-year average.** Specific (b) sends a series that
changes sign to the no-growth case alone, and here the no-growth case is negative, because one acquisition, bought for cash
and sold for stock inside the window, sits in the mean. The convention gives no instruction for crediting non-cash sale
proceeds ("net of businesses sold" reads as cash) and no floor at zero for the business before net cash; I showed the
literal result and the stock-credit variant beside it. (2) **A lending book inside an operating company is not named by
the range convention.** Whether net loan originations are capital spending (specific d, working capital) or an investment
like the marketable securities changes owner cash by about half; I counted them, confessed it as this run's CONVENTION and
showed the other figure. (3) **"Cash and securities" in the all-equity basis does not say whether equity investments
carried at fair value are counted**; here they are $3,299M, about $2.56 a share; I left them out of the central figure and
showed them beside. (4) **The brief's competitor instruction assumes the 10-K names rivals**; this one names only
categories, so the instruction was empty; recorded under Q2. (5) **Specific (a) names only the first or last window year**
as the cycle trigger; the aberrations here were in the middle years (2022 and 2023) and the convention is silent on them.
