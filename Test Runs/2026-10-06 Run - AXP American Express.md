# Company Run — American Express Company (NYSE: AXP) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Blind analyst run
of record, dispatched by the operator. Research folder: `Test Runs/_research 2026-10-06 AXP/` (tool outputs, the XBRL
transcription script, the arithmetic; raw filings under its `cache/`, gitignored). The template was copied to this file
before any fetch, and the file is written question by question.

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. I did not open `PORTFOLIO.md`,
any holding review, any earlier AXP run or research folder, the session-state files, the queue register, the prepped
reading list or `tools/alerts.json`.
**Contamination, declared.** (1) My training memory holds a long prior on this company, including that Berkshire has owned
it for decades; that prior is to be replaced by the filings, not confirmed by them. (2) The v5 ledger itself carries rows in
which the speakers praise this very business (**[M2013-043]**, **[M2018-073]**, **[M2019-074]**) and rows in which they
doubt it (**[M1995-028]**, **[M1996-036]**). These are the framework's own evidence and are allowed, but the speakers are
holders of the stock: the 2026 proxy lists Berkshire Hathaway Inc. and subsidiaries as the owner of 151,610,700 shares,
22.1% (DEF 14A, accession `0001104659-26-034163`). The foundation "who is paid to tell you" applies to them as to anyone
**[M2020-037]**, and Buffett applies it to his own commentary when he has "a dog in this fight" **[L2009-015]**. I therefore
treat every AmEx-specific row as a statement by an interested holder about a past period, usable as a test the speakers
put, never as a finding about the business today. (3) The name may be held by the operator; I have not looked. Operator
rule 9's incentive is declared and the antidote is the row's: "if you have doubts about something being into your circle of
competence, it isn’t." **[M2002-092]**.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $304.02 (close 2026-10-05, read through `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common shares, par $0.20, **675,309,833** outstanding
  (Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-24, accession `0000004962-26-000322`; cover as of
  2026-07-14; `python Screens/cover_shares.py AXP`). Preferred: 1,600 Series D shares (outstanding at 2025-12-31, 10-K
  balance sheet) and 1,600 Series E shares (6.450% fixed-rate reset noncumulative, issued 2026-08-12, 8-K accession
  `0000004962-26-000338`, 1,600,000 depositary shares); neither is common, and neither is added to the share count.
- **Market cap:** about **$205,310M** (675,309,833 × $304.02).
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, dated 2026-10-05
  (issuing authority; `python tools/sources.py`).
- **Filings read** (operator rule 4), all from EDGAR, CIK 0000004962:
  - Form 10-K for FY2025, filed 2026-02-06, accession `0000004962-26-000080` (business, competition, supervision,
    risk factors, MD&A tables, funding and deposit tables, the consolidated statements, legal proceedings).
  - Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-24, accession `0000004962-26-000322` (balance sheet,
    capital, Part II Item 2 repurchases).
  - DEF 14A, filed 2026-03-25, accession `0001104659-26-034163` (pay, scorecard, LTIA design, board, ownership).
  - Form 8-K of 2026-07-24, Item 2.02, EX-99.1 (Q2 2026 earnings release), accession `0000004962-26-000318`, read
    before judging non-GAAP habits.
  - Form 8-K of 2025-01-16, Item 8.01 (resolution of the small-business sales-practices investigations), accession
    `0000004962-25-000005`.
  - Form 8-K of 2026-08-12, Items 3.03 and 5.03 (Series E preferred), accession `0000004962-26-000338`.
  - Competitors' own 10-Ks for FY2025: Capital One Financial, filed 2026-02-19, accession `0000927628-26-000024`;
    Synchrony Financial, filed 2026-02-06, accession `0001601712-26-000006`.
- **One figure cross-checked against the filed statement:** net income for FY2025, **$10,833M** on the consolidated
  statement of income and on the cash-flow statement of the 10-K (accession `0000004962-26-000080`), against
  10,833,000,000 in the XBRL `NetIncomeLoss` fact of the same accession (`Test Runs/_research 2026-10-06 AXP/xbrl_axp.txt`).
  They agree.
- **`tools/run.py AXP`, arithmetic lines only** (`Test Runs/_research 2026-10-06 AXP/run_py_output.txt`). Price, shares,
  sovereign and the ten-year balance-sheet transcription are used. Its "owner earnings" line (operating cash flow less
  stock pay and capex: $14,514M on the three-year lower mean, a printed yield of 7.08%) is **not used**: for a card lender,
  operating cash flow adds back the provision and leaves the growth of card loans and receivables ($19,573M in 2025,
  $23,259M in 2024, $25,124M in 2023, in investing activities) outside it, so it is not the cash an owner can take out.
  The owner-cash figure this run uses is built at Q4 from the filed statements. Nothing printed by the tool as a rule,
  an id or a verdict was read (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this card network and lender will earn in ten years, not
what the quotation does. The market serves and does not instruct **[M2006-077]**. Who is paid to tell you **[M2020-037]**
bears hard here twice: on management, which publishes a full-year EPS range ("We continue to expect full-year EPS of $17.30
to $17.90", EX-99.1, 2026-07-24) and a "growth aspiration" (risk language of the same release), and on the speakers, whose
rows on this company come from a 22.1% holder (contamination note above). No macro enters **[M2000-094]**: the earnings
release's list of macro risks is not weighed. The analyst's habits: write down at once what flies in the face of the prior
**[M1997-127]**, and look for "what’s wrong" and "what you’re missing" **[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The deposit side is not cheap. U.S. interest-bearing deposits cost an average **3.7%** in 2025 (4.3% in 2024, 4.0% in
   2023; 10-K Table 19), and about $25.6B of the $151.4B are brokered CDs and third-party sweep accounts (10-K Table 7.2).
   Capital One paid 3.21% on its interest-bearing deposits in 2025 (its 10-K). The row that opens the bank door asks for
   "very cheap money on the deposit side" **[M2002-022]**.
2. The merchant price drifts down: discount revenue as a share of billed business **2.29% (2023), 2.27% (2024), 2.24%
   (2025)** (10-K Table 5), "lower average merchant discount rates due to shifts in geographic and merchant spend mix";
   and the 10-K says "We have also experienced erosion of our merchant discount rates as we increase merchant acceptance."
3. The cost of keeping the customer rises faster than revenue: Card Member services expense **+27%** in 2025 and +21% in
   2024, Card Member rewards $18,409M (+11%), against revenue +10% (10-K income statement).
4. Surcharging and steering against the card are rising where the law allows them ("we have seen an increase in merchant
   surcharging on American Express cards", 10-K risk factors); a proposed Visa/Mastercard settlement of November 2025
   "may result in greater surcharging generally, decreased acceptance by merchants of certain types of cards, such as
   premium cards, or downward pressure on our merchant discount rates" (10-K).
5. A competitor with money bought a network: Capital One, the largest U.S. card issuer by balances, acquired Discover
   ("the Transaction"), and the 10-K now lists Discover and Diners Club as "owned by Capital One".
6. In January 2025 the company agreed to pay about $230M to resolve DOJ and Federal Reserve investigations "into
   historical sales practices for certain U.S. small business customers, which the company ended in 2021 or earlier"
   (8-K, accession `0000004962-25-000005`).
7. The 2021 owner cash includes a release of excess capital (equity fell from $22,984M to $22,177M while net income was
   $8,060M), so a five-year average that starts in 2021 is flattered (Q4).
8. Capital is being added at the top of the capital structure while common stock is bought back: $1.6B of 6.450% Series
   E preferred issued 2026-08-12, while $3,905M of common was repurchased in the first half of 2026 at prices around
   $310 to $319 (10-Q Part II Item 2).

## THE STANDING RULE
Owning a common share bought with cash risks what is paid and nothing more: no borrowing, no collateral, no option given
**[M2012-081]**, **[L2023-005]**, **[L2014-024]**. The rule is not engaged by this purchase; it would be engaged only by
financing or sizing it so that a total loss of the position mattered to the buyer **[L2014-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**; for a bank, "inside the circle when both sides
of its balance sheet can be read from its filings" and "outside it when the asset side cannot" (Q1, The door against the
exclusion, settled; **[M2002-022]**, **[M2005-068]**). AXP is a bank holding company (10-K, Supervision and Regulation:
"American Express Company, a bank holding company"; U.S. bank subsidiary American Express National Bank, AENB) and also
the fourth-largest general-purpose card network by purchase volume (10-K, Competition). So it is read twice: as a lender,
both sides of the balance sheet; as a network and fee business, its key variables.

**1. The asset side, 2025-12-31 (10-K balance sheet, accession `0000004962-26-000080`; $M):** Card Member loans
145,923 net of a 5,909 reserve; Card Member receivables 61,851 (charge balances due in full each month) net of 180;
loans held for sale 2,457; other loans 10,605; cash and equivalents 47,792 (of which 43,491 interest-bearing deposits
in other banks); investment securities 1,043. What the book is, the filing says plainly: unsecured card credit to
"premium, high-spending and high-credit-quality customers" (10-K, Business). How it behaves is disclosed every quarter:
net write-off rate, principal only, consumer and small business **2.0% (2025), 2.0% (2024), 1.8% (2023)**; 30+ days past
due **1.3%** each year; 2.0% again in Q2 2026 (EX-99.1). There is no trading book; derivatives are hedges (foreign-exchange
forwards of about $54B notional "designed to offset pretax impacts from currency movements", interest-rate swaps), with
net derivative fair values in the hundreds of millions (10-K derivatives note). The asset side can be read: it is the kind
of short, granular, self-liquidating consumer and small-business credit whose losses the filing measures, not a book whose
condition "no one probably knows" **[M2005-068]**. Contrary, written down: this is not "very little risk on the asset
side" **[M2002-022]** in the sense of a mortgage bank; it is unsecured credit at a 2% annual principal loss, carried by
a net interest yield of 8.1% (10-K key metrics). Readable, not riskless. Danger "It’s always on the asset side."
**[M2011-022]**, so the asset side is read again at Q9.

**2. The deposit side (10-K Tables 7.2 and 19):** customer deposits $152,488M; U.S. savings $116,867M, checking $2,965M,
direct CDs $5,979M, brokered CDs $9,919M, third-party sweep $15,696M; "approximately 92 percent of these deposits were
insured"; the direct programme had "approximately 3.9 million accounts"; uninsured deposits about $13.0B. This is money
"from a natural customer base", mostly not "on a wholesale basis" **[M2012-012]**, though about 17% is brokered or swept
in. It is readable. It is **not cheap**: 3.7% in 2025 (contrary evidence 1). The rest of the funding is long-term debt of
$56,387M (unsecured notes and card-backed securitizations) and short-term borrowings of $1,371M; no commercial paper was
outstanding at any point in 2025 (10-K, Short-term funding programs).

**3. The key variables and whether they are foreseeable** **[M1998-044]**, **[M2008-033]**. AXP earns from four lines
(10-K, FY2025, $M): discount revenue from merchants 37,401; net card fees 9,993; service fees and other 7,471; net interest
income 17,364; total revenues net of interest expense 72,229. The variables are: card member spending (billed business
$1,669.8B), the merchant discount rate on it (2.24%), the number of fee-paying cards and the fee per card (86.6M
proprietary cards, $117 average fee), loan balances and their loss rate, the cost of deposits and debt, and the cost of the
rewards and services that keep the card member (rewards 18,409; Card Member services 6,057; business development 6,457).
These have been reported in the same form for years, and the ten-year question about them is a question about the
behaviour of premium spenders and of merchants: "much more of a consumer products business" than a technology forecast
**[M2017-019]**, "what we think we can project out in terms of consumer behavior and threats to a business" **[M2023-030]**.
The past statements tell the shape of the future ones **[M2008-033]**: spend times rate, fees times cards, balances times
spread less losses.

**4. The doubt, recorded, and where it goes.** The 10-K's own list of threats names agentic commerce, stablecoins, real-time
account-to-account payment, buy now pay later, surcharging and the Visa/Mastercard settlement. Does that put the ten-year
economics out of reach, so that the industry "changes fast" and the file closes here (Q1, The routing, fixed;
**[M1998-008]**)? The filing's own numbers say the core economics have moved slowly: the discount rate moved five basis
points in two years; the write-off rate one-fifth of a point; card fees rose every year. The threats named are threats to
the castle, which Q2 owns (Q1, What understanding means: "Rapid change is owned by Q2"), not evidence that the economics
cannot be pictured. The insiders do write the forecast down **[M2000-105]**: management publishes a revenue and EPS
range every year (EX-99.1). That is a reason for suspicion of the forecast at Q4 and Q6, but it is also proof that the
industry's insiders do not call it "too hard". I record the doubt and carry it to Q2, tests 10 and 11.

**The row against this verdict, read in full.** Of "a very large finance company": "even though I could understand every
individual transaction they did, I don’t regard the whole enterprise, or the operation of it, necessarily as being within
my circle of competence." **[M2002-094]**. AXP is a very large finance company. What separates it, on its filings, from the
case the row describes is that the whole enterprise's credit result is disclosed as one number each quarter (write-offs,
delinquencies, reserve, by segment), the book is granular card credit rather than a set of large transactions, and there
is no wholesale derivatives or trading operation whose condition is hidden. That is my reading, not a speaker's; it is the
point at which a second analyst could disagree, and it is recorded as such.

**5. Can the winner be named, not just the industry?** **[M2012-067]**. The question is not which payments company wins;
it is whether this one keeps its premium spenders and its merchant price. That is the castle question, and it can be
asked of the filings.

**VERDICT: IN.** Both sides of the balance sheet can be read from the filings **[M2002-022]**, **[M2012-012]**; the
asset side is disclosed by loss and delinquency every quarter and carries no derivatives book of the kind that closes the
door **[M2005-068]**, **[M2002-094]**; the key variables are named and have been reported in the same form for years
**[M1998-044]**, **[M2008-033]**; the ten-year question is about customers more than technology **[M2017-019]**,
**[M2023-030]**. The deposit side is readable but not cheap, which is a fact about the economics, weighed at Q2 and Q3,
not about whether the institution can be seen.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.

"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The castle the filing describes is a
closed loop: AXP issues most of the cards on its own network, acquires most of the merchants, and so sees both sides of the
transaction (10-K, Business: "card-issuing, merchant-acquiring and card network businesses"). The customer it seeks is
"premium, high-spending and high-credit-quality", whose "Spending on our cards, which is higher on average on a per-card
basis versus our network competitors, offers superior value to merchants" (10-K, Business). The tests, each with its fact:

**1. The key factors and their permanence** **[M1995-038]**. Three, from the revenue lines: the premium card member who
pays a fee to carry the card (net card fees $9,993M, up 18%), the merchant who pays a discount for that card member's
spend (discount revenue $37,401M), and the credit quality of that card member (write-offs below half the competitors',
test 6). None depends on "the genius of the lord in the castle" **[M1995-038]**: the speakers' own row on this company is
a scandal in 1963 that nearly took the company down, through which "nobody quit using the card" **[M2018-073]**; and in
2025, the year after the sales-practices settlement (contrary evidence 6), card acquisitions were 12.5M and fees rose 18%.
"if you have a business where your customers are mad at you and you’re growing, you know, that has met a certain test, in
my mind, of utility." **[M2000-032]**.

**2. Pricing power, and the agony before a rise** **[M2005-020]**, **[M2000-031]**. Average fee per proprietary card
**$92 (2023), $103 (2024), $117 (2025)**, **$131** annualized in Q2 2026 (10-K Table 5; EX-99.2 of accession
`0000004962-26-000318`), while proprietary cards-in-force grew 80.2M, 83.6M, 86.6M and new cards acquired held at 12.2M,
13.0M, 12.5M. The fee rose about 42% in two and a half years and the base still grew. Q2 2026: "our Platinum portfolio
is now the fastest growing in our U.S. Consumer business" after the Platinum refresh (EX-99.1). "Anytime you can charge
more for a product and maintain or increase market share against wellentrenched, well-known competitors, you have
something very special in people’s minds." **[M2000-031]**. **Contrary, on the merchant side:** the merchant price is
not rising but slipping, 2.29% to 2.24% of billed business in two years, and the 10-K names erosion "as we increase
merchant acceptance" and from regulation of competitors' pricing. The card member pays more each year; the merchant pays
slightly less. The test "price past the moat" **[M2001-087]**, **[M2001-088]** is not failed on the evidence (the fee
base still grows), but the merchant side is where the pricing power is weakest.

**3. Would the customer still choose it over the low bid?** **[M2017-009]**. Fee-free cards on the Visa and Mastercard
networks are offered by every large bank; 86.6M proprietary AXP cards carry an average fee of $117 and the number grows 4%
a year. The card member is not buying on the low bid. On the merchant side the low bid is the debit or bank-network card,
and the merchant's answer in some places is to surcharge or steer (contrary evidence 4): the merchant would take the low
bid where the law lets him, and the card member's preference is what holds the merchant. The speakers' row on a large
merchant who "could not get rid of American Express, or even get them to cut their fees" **[M2013-043]** is a holder's
report of one conversation, used here as the test, not as the finding.

**4. The money test: could a well-funded attacker take it?** **[M2011-015]**, **[M1997-103]**. The attacker exists and
has spent: Capital One, "the largest issuer of credit cards in the United States" by balances (COF 10-K), bought Discover
and its networks. Its own 10-K says of AXP: "American Express is also a strong competitor with international merchant
acceptance, competitive transaction fees and an upscale brand image", and of its own network, "we cannot be certain that
we will achieve global market parity with Visa or Mastercard". The attacker's 2025 return on average common equity was
**2.03%** (COF 10-K), against AXP's **33.9%**. One competitor can be enough **[M2012-108]**; this one has the money but
not yet the result.

**5. Share of mind** **[M1997-099]**. Billed business $1,669.8B, +8%; average proprietary basic card member spending
$25,453, +3% (10-K Table 5); Q2 2026 card member spending +9%, "the highest rate we've seen in three years on an
FX-adjusted basis" (EX-99.1). Volume in the hands of the customers the castle is built for is rising.

**6. The competitor row** (same metrics, each company's own FY2025 10-K; three fiscal years, 2025 / 2024 / 2023):

| | AXP | Capital One | Synchrony |
|---|---|---|---|
| Return on average equity | 33.9% / 34.6% / 31.5% | 2.03% / 8.08% / 9.10% (on average common equity) | 21.1% / 22.5% / 16.4% |
| Net write-off (charge-off) rate, cards | 2.0% / 2.0% / 1.8% (principal only, consumer and small business); 2.3% / 2.3% / 2.0% with interest and fees | 5.09% / 5.88% / 4.57% (Credit Card segment) | 5.65% / 6.31% / 4.87% (all loan receivables) |
| Average rate on interest-bearing deposits | 3.7% / 4.3% / 4.0% (U.S.) | 3.21% / 3.54% / 3.02% | 4.1% / 4.6% / 3.9% |
| Accession | `0000004962-26-000080` | `0000927628-26-000024` | `0001601712-26-000006` |

The definitions differ (AXP gives principal-only and all-in write-off rates; Capital One's 2025 return carries the costs
of the Discover transaction), so the row is read for order of magnitude, not decimals. Read so: AXP earns about a third on
its equity while losing less than half as much on its loans as the two large card lenders, and it pays **more** than
Capital One for its deposits. The castle is not cheap money; it is the customer and the merchant fee.

**7. Ask the competitors** **[M1999-130]**. Capital One's filing names AXP's "upscale brand image" and acceptance as
strengths it must meet; Synchrony lists AXP among its competitors for partners and for direct deposits (SYF 10-K). No
competitor filing read here calls it weak.

**8. Widening or narrowing?** **[M1999-108]**, **[L2005-010]**, **[M2000-075]**.
- *Widening:* net card fees **$2,700M (2015)** to **$9,993M (2025)** (XBRL `FeesAndCommissionsCreditCards` for 2015,
  accession `0001193125-16-469798`; 10-K for 2025): the part of revenue the card member pays directly rose about 3.7
  times in ten years; write-offs below peers; spend growth accelerating in 2026.
- *Narrowing:* the merchant rate slips (2.29%, 2.27%, 2.24%); and the cost of keeping the premium customer rises faster
  than what he brings. Card Member rewards, Card Member services and business development together were **61.4%** of
  discount revenue plus net card fees in 2023, **62.5%** in 2024 and **65.2%** in 2025 (10-K income statement: 24,992 /
  40,671; 27,267 / 43,641; 30,923 / 47,394). The 10-K calls the product cycle "our ongoing cycle of product refreshes".
  "A moat that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**. Whether the refresh cycle
  adds to a standing advantage or replaces what competitors take each year is, the framework says, a judgment with no
  further test (Q2, The maintained lead against the rebuilt one). My judgment from these numbers: the fee base and the
  spend base grow while the engagement-cost share rises about two points a year; that is a moat maintained at a rising
  price, not yet one being filled in, and the rising price is carried into Q7's certainty.

**9. What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]**. The filing names the threats:
surcharging and steering against the card where law allows; the Visa/Mastercard settlement proposed in November 2025 that
"may result in greater surcharging generally, decreased acceptance by merchants of certain types of cards, such as premium
cards, or downward pressure on our merchant discount rates"; pricing regulation, including "potential credit card interest
rate caps"; and new rails and wallets that "could choose not to accept, suppress use of, or degrade the experience of
using our products" (10-K risk factors). Would the business be started today against its substitutes **[L2006-008]**? A
new entrant would need a global merchant network and a premium base, which is the money test above, and the best-funded
attempt is the one in the competitor row. None of the threats is shown on the evidence to be filling the moat now: the
2025 numbers show the card member paying more and spending more. They are carried as the reasons the range at Q7 cannot
be narrow.

**Why not TOO HARD.** A castle whose future cannot be judged goes to TOO HARD **[M2000-019]**, **[M2006-013]**. The
future here can be judged on the variables that matter (fee-paying cards, spend per card, merchant rate, engagement cost,
credit), each reported for years; the threats are named and their present size is measurable in those same lines. The
speakers' own doubts about this franchise in 1995 and 1996 ("It is not what it was 20 years ago, relative to the
competition." **[M1996-036]**; also **[M1995-028]**) are a reminder that a notch can be lost; the years since show, on the
numbers read here, that the fee and the credit edge were not lost. That is a fact about the past, weighed and not
extrapolated.

**VERDICT: IN.** The castle stands for a reason a competitor with money has not yet overcome **[M2011-015]**: premium
card members who pay rising fees and spend more each year **[M2000-031]**, **[M2017-009]**, and a credit book that loses
half what the large rivals lose (competitor row). Its weak walls are named and carried forward: the merchant rate drifting
down, the cost of keeping the customer rising faster than revenue **[L2007-005]**, and deposits that cost more than the
bank-funded rival's. The narrowing signs weigh at Q7 in "the degree of certainty" **[M1999-104]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.

"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**. For a lender the capital
that must go in is equity held against the loans and receivables, at a ratio the regulator and the company set: "We seek to
maintain capital levels and ratios in excess of our minimum regulatory requirements, specifically within a 10 to 11 percent
target range for American Express Company’s Common Equity Tier 1 (CET1) risk-based capital ratio" (10-K, Capital); CET1
was 10.5% at the end of 2023, 2024 and 2025 and 10.4% at 2026-06-30 (10-K key metrics; 10-Q). Physical capital is small:
capital spending $2,425M in 2025 against depreciation and amortization of $1,777M (10-K cash-flow statement).

**1. Return on the capital the business needs** **[M2010-090]**, **[M2011-060]**. Net income $10,833M on average
tangible equity of about $27,233M in 2025 (equity less goodwill and other intangibles: $28,512M at 2025-12-31,
$25,954M at 2024-12-31; 10-K balance sheet and `run_py_output.txt`), about **39.8%**; reported ROE 33.9%, 34.6%, 31.5%
(2025, 2024, 2023). Read before crediting it **[L1994-009]**:
- *Leverage.* Equity was 11.2% of assets at 2025-12-31 (33,474 / 300,052). The bank row asks how much of a high return
  "dealing in what is basically a commodity — money" is gearing **[M2007-013]**. Here the comparison that answers it is
  the competitor row: Synchrony runs at 14.14% equity to assets and earned 21.1%; Capital One earned 2.03%. AXP's return is
  higher than both at a similar or lower equity ratio, and most of its revenue (discount revenue and card fees, $47,394M
  of $72,229M) is not interest on money at all. Gearing is part of the return; it is not most of it.
- *Equity kept low by buybacks.* "if you keep the equity low enough by buying shares back, why, you could make return on
  equity whatever you want" **[M1998-017]**. AXP bought back $26,638M of common stock in 2021-2025 (xbrl_axp.txt). But the
  equity it may keep is not its choice alone: the CET1 range binds from below, and the CET1 ratio held at 10.5%. So the
  buybacks return what the capital rule does not require; they do not push equity below what the book needs. The ROE that
  results is still flattered relative to an unlevered business, and that is why Q7 values owner cash, not ROE.
- *Cyclical peak?* Write-offs of 1.8% to 2.0% are not a credit-cycle trough figure that cannot last; the competitor
  rates show the cycle running at the same time through the whole industry.

**2. What must be reinvested to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Each added dollar of loans
and receivables needs about a tenth of a dollar of common equity (the CET1 range). Over 2021-2025 net income totalled
$44,910M and equity rose $10,490M (22,984 to 33,474), so about **23%** of earnings stayed in the business and **77%** went
out (`arithmetic_output.txt`). Physical capital to stand still: capital spending ran below depreciation in 2023 (by
$88M) and above it in 2024 (by $235M) and 2025 (by $648M); the filing does not split maintenance from growth, so my stated
guess **[M2000-144]** is that depreciation ($1,777M in 2025) approximates the maintenance need and the excess is growth
outlay (technology and premises). Both are already inside net income (as depreciation) and inside the retained equity
(as the asset), so the owner-cash figure at Q4 is after them.

**3. What the added capital earned** **[M2001-019]**, **[M2023-081]**. From 2021 to 2025 net income rose $2,773M (8,060 to
10,833) while equity rose $11,297M (22,177 to 33,474): about **24.5%** on the added equity. That is lower than the
average return (the added equity came while net interest income was helped by rates: net interest income $13,134M in
2023, $17,364M in 2025), but it is well above any bond. "it’s growth. [...] But whether that’s good or bad depends on what
we earn on that incremental $130 million over time" **[M2001-019]**: here the incremental capital earns about a quarter.

**4. The growth arithmetic and its caps** **[M1999-067]**, **[M1997-095]**, **[M2003-120]**. Revenue net of interest expense
grew from $42,380M (2021) to $72,229M (2025), about 14.3% a year, from a 2021 base still depressed by the pandemic's effect
on travel spending; net income grew 7.67% a year over the same span. The business cannot carry 14% for ten years without
its spend outgrowing the economies it serves many times over; 7.67% is the rate Q7 may carry, and any higher rate is shown
beside it, not used, under the cap **[M1999-067]**.

**WEIGHS FOR.** The business earns about a third on its equity and about a quarter on the equity added since 2021 **[M2010-090]**,
**[M2001-019]**, while needing only a tenth of a dollar of equity per added dollar of loans, so most of what it earns can
leave **[M1998-081]**; the return is partly gearing and partly flattered by buybacks **[M2007-013]**, **[M1998-017]**, which is why
Q7 values the cash that leaves, not the ROE.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.

**The balance sheets first, ten year-ends** **[M2025-032]** (`run_py_output.txt`, first-filed XBRL vintages, accessions
listed there; deposits from `xbrl_axp_deposits.txt`; read against the FY2025 filed balance sheet; $M):

| year-end | assets | equity | goodwill | cash | long-term debt | deposits | retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 158,893 | 20,501 | 2,927 | 25,494 | 46,990 | n/t | 10,371 |
| 2018 | 188,602 | 22,290 | 3,072 | 27,808 | 58,423 | 69,960 | 12,499 |
| 2020 | 191,367 | 22,984 | 3,852 | 32,965 | 42,952 | 86,875 | 13,837 |
| 2021 | 188,548 | 22,177 | 3,804 | 22,028 | 38,675 | 84,382 | 13,474 |
| 2022 | 228,354 | 24,711 | 3,786 | 33,914 | 42,573 | 110,239 | 16,279 |
| 2023 | 261,108 | 28,057 | 3,851 | 46,596 | 47,866 | 129,144 | 19,612 |
| 2024 | 271,461 | 30,264 | 4,187 | 40,640 | 49,715 | 139,413 | 22,148 |
| 2025 | 300,052 | 33,474 | 4,872 | 47,792 | 56,387 | 152,488 | 25,487 |

(n/t: the deposits element is not in the tool's ten-year window for 2016; the 2017 and 2019 rows are in the tool output
and move with their neighbours.) What the figures say **[M2025-032]**: assets nearly doubled in nine years while equity
rose about 63%, so equity fell from 12.9% to 11.2% of assets; the growth was funded by deposits, which more than doubled
from 2018, not by long-term debt, which is about where it was in 2018. Goodwill is small against equity (4,872 against
33,474) and rose with recent acquisitions (cash paid for acquisitions $633M in 2025, $454M in 2024). Retained earnings
rose only from $10,371M to $25,487M against cumulative net income far larger, because repurchases are charged partly to
retained earnings (statement of shareholders' equity: 2023 repurchases $3,519M, of which $3,181M to retained earnings).
Cash is large and rising (liquidity held at banks, $43,491M interest-bearing). What they cannot say: the quality of the
$207,774M of card loans and receivables is not on the balance sheet; it is in the write-off and delinquency series read at
Q1 and Q2, and in the reserve (card loans $5,909M, 3.9% of gross loans of $151,832M at 2025-12-31).

**The real costs** **[L2021-003]**:
- *Credit losses* are expensed through the provision ($5,256M in 2025) under CECL, and the reserve moves with a macro
  model; the 10-K describes the reserve build in 2025 as driven by loan growth and "deterioration in the macroeconomic
  outlook used in our reserve models". Contrary, written down: Q2 2026 pretax income rose 15% with a card-loan reserve
  **release** of $190M against a $198M build a year earlier (10-Q), while 30+ day delinquencies were 1.2% against 1.3%
  and the write-off rate was flat at 2.0% (EX-99.1). A release that follows lower delinquencies is the model working, not
  a tell; it is recorded because it helped the quarter.
- *Rewards* are a real, estimated cost: the Membership Rewards liability rests on an ultimate redemption rate and a cost
  per point; "an increase in the estimated URR of current enrollees of 25 basis points would increase the Membership
  Rewards liability and corresponding rewards expense by approximately $229 million" (10-K, critical accounting
  estimates). Rewards were $18,409M in 2025, expensed.
- *Depreciation* $1,777M is expensed and is a true cost **[L2015-004]**; capital spending above it is in the retained
  equity (Q3).
- *Stock pay* $551M in 2025 is expensed inside salaries; no figure excludes it.
- *Restructuring and "one-time" items:* none presented as excluded in the 10-K's headline figures; the proxy's "EPS growth
  adjusted for the prior year gain on sale from Accertify" removes a **gain**, the conservative direction.
- *EBITDA in the filer's mouth:* no instance found in the 10-K, the 10-Q or EX-99.1 (text search for "EBITDA" in the
  three cached texts). The only non-GAAP measure in the earnings release is FX-adjusted growth, labelled as such
  (EX-99.1, footnote 1). The release reports GAAP net income and EPS first **[M1994-018]**.

**What the accounts say of the management's character** **[M1995-064]**. The make-the-numbers habit: management publishes
a full-year EPS range and revenue guidance and in 2026 raised the revenue guidance mid-year (EX-99.1: "raising our
full-year revenue growth guidance to 10 percent"); the proxy pays the annual award on a scorecard of revenue growth, EPS
and ROE against plan. Predicting growth rates is "both deceptive and dangerous" **[L2000-037]**; "we become downright
incredulous if they consistently reach their declared targets" **[L2002-041]**. Found alone, the habit weighs against and
is not a STOP (Q4, The make-the-numbers habit, tested; CONVENTION). A second tell, searched for: no adjusted earnings
featured over GAAP (L2016-006's tell; the release leads with GAAP); no reserves moving suspiciously against an offering
(the Q2 2026 release preceded the August preferred issue by three weeks, but followed lower delinquencies, and a preferred
issue is not a sale of the common); no prepaid or deferred accounts building out of line (other assets $24,263M against
$21,179M, +15%, with assets +11%; not read further as a tell, since no line inside it was flagged in the filing); no
profits booked on both sides of a contract. **No second tell found.**

**The owner cash, after every real cost** (operator rule 5; CONVENTION of construction confessed here, since the rows do
not give one for a lender). For a bank the cash an owner can take out is what is left after the equity the growing book
needs is kept back: owner cash = net income − the rise in shareholders' equity. Net income is after interest, tax,
depreciation, credit losses, rewards and stock pay **[L2021-003]**; keeping back the equity rise keeps the CET1 ratio
where the regulator and the company set it (Q3). The check is that this figure matches what was actually paid out
(dividends + repurchases − issuance), year by year (`arithmetic_output.txt`; $M):

| year | net income | rise in equity | owner cash | paid out |
|---|---|---|---|---|
| 2021 | 8,060 | (807) | 8,867 | 9,036 |
| 2022 | 7,514 | 2,534 | 4,980 | 5,011 |
| 2023 | 8,374 | 3,346 | 5,028 | 5,402 |
| 2024 | 10,129 | 2,207 | 7,922 | 7,919 |
| 2025 | 10,833 | 3,210 | 7,623 | 8,028 |
| five-year mean | | | **6,884** | |

The two columns agree within a few hundred million each year, so the figure is the cash that actually left. Contrary,
recorded: 2021 includes a release of capital held over from 2020 (equity fell while $8,060M was earned), so 2021 flatters
the mean; without it, the 2022-2025 mean is **$6,388M**. Both are carried to Q7. This is not a net-income proxy: net income
is the starting line and the capital the business must keep is subtracted from it.

**VERDICT on confusion: IN** (the accounts can be read; GAAP leads; no EBITDA; one tell, the guidance habit, and no second)
**[M1995-063]**, **[M2003-029]**; **WEIGHS AGAINST** on the guidance habit alone **[L2000-037]**, **[L2002-041]**. The owner
cash above feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.

Stephen J. Squeri has been Chairman and Chief Executive Officer since 2018 and is also CEO of AENB (DEF 14A). For a
marketable stock the speakers read rather than meet **[M2007-081]**; the yardsticks are the record against the hand dealt
and the treatment of owners **[M1994-008]**, **[M1994-009]**.

**The first yardstick: the record against the hand dealt** **[M1994-008]**. Revenue net of interest expense $40,338M
(2018) to $72,229M (2025); net income $6,921M (2018) to $10,833M (2025), through a year (2020) in which net income fell to
$3,135M as travel and entertainment spending stopped (`xbrl_axp.txt`, `xbrl_axp_revenue.txt`). Against the competitors in
the same years and the same rate cycle: write-offs less than half of Capital One's and Synchrony's, and a return on equity
above both (Q2 competitor row). Net card fees, the line that most depends on the customer valuing the product, were
$7,255M, $8,449M and $9,993M in 2023, 2024 and 2025 (10-K). That record is made in the business the speakers call strong; how much is
the hand and how much the player cannot be separated from outside **[M1996-037]**, **[M1999-106]**.

**The second yardstick and the integrity question** **[M2015-047]**, **[M2013-088]**. The facts that bear on it, all from
the filings:
1. **The sales-practices resolution.** 8-K of 2025-01-16 (accession `0000004962-25-000005`): agreements with the DOJ and
   an agreement in principle with the Federal Reserve staff "to resolve previously disclosed investigations into
   historical sales practices for certain U.S. small business customers, which the company ended in 2021 or earlier",
   about $230M in total; the company says it "took decisive voluntary action to address these issues, including
   discontinuing certain products several years ago, conducting a comprehensive internal review, taking appropriate
   disciplinary measures, making organizational changes, and enhancing policies, compliance, and training programs."
   The FY2025 10-K repeats: "in 2025 we entered into agreements to resolve governmental investigations related to
   historical sales practices for certain U.S. small business customers." The practices ran in part under the present
   chief executive (he took office in 2018; they ended "in 2021 or earlier").
2. **Rewards and benefits issues:** "as previously disclosed, we have identified issues related to our rewards and
   benefits programs and have taken actions to remediate the issues and enhance our related procedures and controls"
   (10-K, operational risk).
3. **How they speak of it.** The 8-K is in the company's newsroom voice ("cooperated extensively", "decisive voluntary
   action") and does not describe what the salespeople did. The rows read reports for "the things that we would want to
   know about if we owned a hundred percent of the company" **[M1998-036]**; a newsroom statement that names the remedy but
   not the conduct falls short of that, and the language of the 10-K and the release ("Membership Model", "premium
   lifestyle brand powered by technology", "value propositions") is the "standardized bunch of popular jargon" the rows
   find a turnoff **[M1998-038]**, **[M2007-083]**.

How the rows read such a case. The error at Wells Fargo, as the speakers put it, was not that bad incentives existed but
that management ignored them: "they had the wrong incentives", and the greater error was ignoring it **[M2018-012]**; "the
main problem was they didn’t act when they learned about it" **[M2017-005]**. Incentives that tie a salesperson's pay to
"bringing in dubious people into the door" drive decent people wrong **[M2004-110]**. And a large institution having such a
problem is "not unique"; what counts is that "They cleaned it up" **[M2018-013]** (a row in which the speakers, as holders,
speak of this company's earlier troubles; used for the test, not the verdict). The filing records action: products
discontinued, discipline, organizational changes, a penalty paid. It does not record when management first learned, and I
could not establish that from the documents read; that is an unknown, written down. On the evidence read, the doubt is
about a sales force's conduct and how fast the remedy came, not about the honesty of the people who run the company in
their dealings with its owners: the accounts are GAAP-first (Q4), the proxy bans hedging and pledging by directors and
senior management and carries clawback policies (DEF 14A), and no instance was found in the filings read of the
management's own statements to owners being shown false. The rule is "If you’ve got doubts, forget it." **[M2013-088]**,
and "we may be wrong about a fair number that we’re ruling out" **[M2007-092]**. I judge the doubt is about the
institution's sales controls, which is Q6 Part B's ground (incentives) and Q9's (compliance cost), and not a doubt about
the integrity of the managers. A second analyst could close this OUT on the same facts; the point is recorded as the run's
nearest call before Q7.

**Love of the business, and the same after the cheque** **[M2000-098]**. The chief executive (Chairman and CEO since 2018, DEF 14A)
owns 223,990 shares (DEF 14A beneficial ownership table), about $68M at $304.02,
against 2025 compensation the board set at $48.1M (Q6). Ownership worth less than two years' pay is a stake, not an
owner's fortune; this is weighed at Q6 Part B.

**Ability** **[M1994-008]**, **[M1996-037]**. The record above, a credit book run at half the losses of the rivals through the
same cycle, and capital held inside the target band each year, show ability. That the business would do well under lesser
management **[M1999-106]** limits how much of the record is his.

**VERDICT on integrity: IN** (with the sales-practices doubt recorded and carried to Q6 Part B and Q9; no instance found of
dishonesty toward owners in the documents read) **[M2018-012]**, **[M2017-005]**, **[M2013-088]**; **ability WEIGHS FOR**
**[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.

### Part A: the money

**The retention test** **[R1995-009]**, **[M1998-110]**, **[R2009-002]**. Over 2021-2025 the company kept $10,490M (equity
22,984 to 33,474) of $44,910M earned. Market leg: market value rose from about $97.3B at 2020-12-31 (805M shares × $120.91)
to about $253.8B at 2025-12-31 (686M shares × $369.95) (share counts from the 10-K balance sheets, `xbrl_axp_shares.txt`;
year-end closes **from the aggregator, flagged**, `yearend_closes_aggregator.txt`). Each dollar kept is matched by many
dollars of market value; most of that is a re-rating, not the retained dollars, so the market leg is passed but proves
little **[R2009-002]**. Intrinsic leg: owner cash, the cash that left after the kept equity, rose from $4,980M (2022) to
$7,623M (2025) (Q4), so the kept dollars produced more cash to distribute, at about a quarter on the added equity (Q3).
The forward question, "Can you keep using all of the capital you generate, effectively, for a very long time?"
**[M2010-097]**: it keeps about a quarter and pays out three-quarters, which is the right split for a business whose
growth needs a tenth of a dollar of equity per dollar of loans **[M1994-061]**. **For.**

**Buybacks** **[L1999-023]**, **[L2011-003]**, **[L2016-002]**. The programme is an authorization of "up to 120 million common
shares from time to time, subject to market conditions and in accordance with our capital plans" (10-Q Part II, note c),
with no price above which it stops; the company describes its returns as a share of earnings ("These share repurchase and
common share dividend amounts collectively represent approximately 93 percent and 86 percent of net income available to
common shareholders", 10-Q). Prices paid: about $159 a share in 2023 ($3.5B for 22M shares), about $246 in 2024 ($5.9B for
24M), about $312 in 2025 ($5.3B for 17M) (10-K note on share repurchases, cost including excise tax), and $315.77 in
Q2 2026 (10-Q Part II). **Against the Q7 range (recorded back from Q7):** the bottom is **$180** a share; the 2023 purchases
sat below it, those of 2024, 2025 and 2026 above it, the last ones near the top of the range ($331). By the CONVENTION (Q6,
The buyback with no stated price, tested) the programme **weighs against**: the prices recently paid sit well above the
bottom of the range, so "Continuing shareholders are hurt unless shares are purchased below intrinsic value"
**[L2011-003]** is not shown to be met **[M2014-008]**. Contrary, written down: buying at a fixed share of earnings is the
"show confidence" pattern **[L1999-028]**, and in August 2026 the company issued $1.6B of 6.450% preferred (8-K,
`0000004962-26-000338`), which counts toward Tier 1 capital, while repurchasing common at about $316: preferred capital in,
common capital out, at prices above the bottom of the range.

**Issuance and deals** **[L2009-019]**, **[L2014-015]**. No all-stock acquisition was found in the filings read; acquisitions
were small and for cash ($633M in 2025, $454M in 2024; TheFork proposed in 2026, EX-99.1). Common shares outstanding fell
from 805M (2020) to 686M (2025); stock pay ($551M in 2025) dilutes and the buybacks more than offset it. The one STOP in
Part A is not engaged.

**Part A: UNDECIDED.** Retention passes **[R1995-009]**, **[M2010-097]**; the buybacks are made at prices above the bottom of the
Q7 range with no stated limit **[L2016-002]**, **[L2011-003]**.

### Part B: the pay, the board and the owners

**Pay** (DEF 14A, accession `0001104659-26-034163`). The board set the chief executive's 2025 compensation at **$48.1M**,
"37% above target and 23% above actual compensation for 2024", of which an annual incentive of $11.3M and a long-term award
of **$35M** "set in reflection of competitive positioning". The annual award runs on a Company Scorecard: shareholder 60%
(revenue growth 50%, EPS 25%, ROE 25%), customer 10% (retention, merchant locations), colleague 10%, strategic 20%. The
long-term award is in PRSUs that vest on **relative ROE and relative TSR** against a peer group; stock options were part of
it until the 2026 grant; a 2022 special award of performance options vests on a 40% total shareholder return hurdle and
positive cumulative net income. The board's consultant is Semler Brossy; a compensation peer group is used for
benchmarking.
- Pay tied to what the person controls **[M2003-019]**: revenue growth and retention are; relative TSR is not, and an option
  or share award that rises with the market pays for "an option on [...] S&P futures" **[M2000-062]**.
- ROE as a pay metric in a company that buys back a large part of its earnings each year is the metric the rows warn can be
  made "whatever you want" by keeping equity low **[M1998-017]**; the CET1 floor limits it (Q3) but does not remove it.
- "set in reflection of competitive positioning" with a peer group and a consultant is the ratchet the rows name
  **[M2012-095]**, **[L2005-015]**, **[M2004-016]**.
- The options: a fixed-price option on a company that retains about a quarter of its earnings carries no step-up for the
  retention **[L1994-021]** and pays nothing on dividends **[M2003-018]**; the 2026 change to drop options removes this for
  new grants.
- Pluses, written down: hedging and pledging are prohibited for directors and senior management; clawback policies apply
  "for all NEOs in the event of a restatement or detrimental conduct"; the size of the number is not the sin
  **[M2007-006]** where the manager is able (Q5).

**The board.** The chief executive is also chairman, with a lead independent director (DEF 14A); "I've seen how hard it is
to replace a mediocre CEO if that person is also Chairman." **[L2014-026]**. The chief executive here is not mediocre on the
record (Q5), so this weighs lightly. The largest owner, Berkshire, holds 22.1% (DEF 14A), which is the "very large
shareholder" the rows count on where boards fail **[M2006-011]**.

**The owners.** Earnings guidance is given each year and updated during it (EX-99.1), the habit the rows call destructive
**[M2022-054]** and the "hit the number" pressure **[L2019-006]**; the inversion of Berkshire's own rule weighs against.

**Part B: WEIGHS AGAINST.** Pay set against peers and benchmarked by a consultant, paid on relative TSR and on an ROE that
buybacks raise **[M2000-062]**, **[M1998-017]**, **[M2012-095]**; a combined chairman and chief executive **[L2014-026]**; earnings
guidance **[M2022-054]**. The person outranks the plan **[M2007-006]**, and the person passed Q5, so this is a weight, not a
close.

## Q7 — WHAT IS IT WORTH? STOP.

"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is the
risk-free interest rate" **[L2000-021]**. Value is "the discounted value of the cash that can be taken out of a business
during its remaining life" **[R1996-018]**; the moat and the management enter as "the degree of certainty" **[M1999-104]**.

**The construction (CONVENTION, Part VI).** Owner cash after every real cost, five-year mean **$6,884M** (2021-2025, Q4),
carried at the growth shown, capped by Q3, for ten years, then zero nominal growth, discounted at the sovereign **5.66%**
**[L2000-021]**, **[M1996-025]**; the ends are the no-growth and shown-growth cases **[L2000-024]**, **[L1999-027]**.

**The growth input.** The CONVENTION measures growth on aggregate owner cash. Here the endpoints are both distorted by
capital moves: 2021 to 2025 gives **-3.71%** a year, because 2021 carries the release of capital held over from 2020; 2022
to 2025 gives **15.25%**, because 2022 is a low year in which equity was built back ($2,534M kept). "it will pay you to be
suspicious as to why the beginning and terminal years have been selected" **[L2005-003]**. Neither is the business's
growth. I therefore use the growth of the earnings from which owner cash is taken, net income 2021 to 2025, **7.67%** a
year, with the payout share held level (77% paid out, Q3), and show the 15.25% case beside it, uncapped, for the reader.
Q3's cap: 7.67% for ten years carries owner cash from $6,884M to about $14,417M, about 1.3 times 2025 net income, a
plausible path for a business whose revenue grew 9% to 10% a year in 2024 to 2026; 15.25% for ten years carries it to about
$28,455M, 2.6 times 2025 net income, which needs spend and fees to keep compounding well above the economies served for a
decade **[M1999-067]**, **[M2003-120]**.

**COMPUTATION** (`Test Runs/_research 2026-10-06 AXP/arithmetic.py`, output saved beside it; USD; per share on 675.31M
shares):

| case | base | growth yrs 1-10 | value at 5.66% | per share | value at 10% | per share | expected return at $304.02 |
|---|---|---|---|---|---|---|---|
| no growth | 6,884 | 0% | $121.6B | **$180** | $68.8B | $102 | 3.35% |
| shown growth (net income), Q3-capped | 6,884 | 7.67% | $223.4B | **$331** | $116.9B | $173 | 6.10% |
| uncapped (owner cash 2022-2025) | 6,884 | 15.25% | $404.4B | $599 | $199.5B | $295 | 9.78% |
| no growth, 2022-2025 base (2021 excluded) | 6,388 | 0% | $112.9B | $167 | $63.9B | $95 | 3.11% |
| shown growth, 2022-2025 base | 6,388 | 7.67% | $207.3B | $307 | $108.5B | $161 | 5.71% |

Ten-year growth needed for a 10% return at $304.02 with the $6,884M base: **15.66%** a year, above every rate the run
can defend.

**Value range: $180 to $331 a share** (Q3-capped), **against $304.02.** Width 1.84 to 1, inside the three-to-one line. The
range built without the 2021 capital release, $167 to $307, is narrower and lower.

**The floor and the tax reading.** The floor (CONVENTION) is about ten percent pre-tax **[M2003-149]**, **[L2002-020]**,
**[M1994-004]**, qualified by the long rate **[M2003-151]**, **[M2016-078]**. Owner cash is after AXP's corporate tax
(effective rate 21.5% in 2025); I read the 10% as the holder's return before the holder's own tax, so AXP's after-tax owner
cash is discounted at 10% without grossing up, as the ETN run of 2026-10-05 did. Read the other way (10% before AXP's tax),
the after-tax equivalent is about 7.85%; the capped case's 6.10% is below both. Only the uncapped case (9.78%) would clear
the lower reading, and it rests on a base-year rate the run has rejected.

**Reported at the owner's request (COMPUTATION, NOT A CLEARANCE beyond what Q7 decides):**
- **Value range:** $180 to $331 a share (Q3-capped); $180 to $599 uncapped.
- **Fair price** (the central, shown-growth case clears the ten percent floor): **about $173**.
- **Cheap price** (no-growth owner cash clears the floor, no pencil needed): **about $102**.
- **The price, $304.02,** sits inside the capped range, near its top, and above the fair price; its expected return in the
  central case (6.10%) is below the floor, and even the uncapped case (9.78%) does not reach it.

**Certainty** **[M1999-104]**, **[L2010-002]**. The narrowing signs from Q2 (merchant rate drifting down, engagement cost
rising faster than revenue, surcharging and the bank-network settlement), the credit cycle that a 2.0% write-off rate has
not yet tested in this book's present size, and the guidance and pay habits of Q4 and Q6 all bear on how sure the birds
are. They would lower or widen the range; none raises it.

**Closes.** The range is narrower than about three to one, and the price sits inside it, near its top: not a screamer, a
case that would need far more than a pencil **[M2009-005]**, **[M1996-084]**; "there’s just a point at which we drop out of
the game" **[M2003-149]**. The close does not depend on my growth cap: no case written, capped or not, reaches the floor at
this price.

**VERDICT: OUT.** The file closes here. Q8 to Q12 are NOT REACHED.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Carried for a later run, not weighed: deposits that can move fast in a direct bank ("Competition among direct
banks is intense because online banking provides customers the ability to rapidly deposit and withdraw funds", SYF 10-K, of
a market AXP is named in), about $25.6B of brokered and swept deposits, $56.4B of long-term debt including card-backed
securitizations, and an unsecured card book whose losses in a deep recession are not shown by the 2023-2025 series
**[M2012-012]**, **[L2010-020]**.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. What the draft would have the buyer do: nothing; inaction is the default **[M1996-006]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (The sales-practices resolution of 2025 would be read here under the newspaper test **[M2008-011]** if a later
run reaches it.)

---
## THE BOX
**OUT**, decided at **Q7**: value range **$180 to $331** a share (Q3-capped; $180 to $599 uncapped) against **$304.02**;
fair price about $173, cheap price about $102. Q1 IN (a bank whose two sides can be read; deposits readable but not cheap),
Q2 IN (premium card members paying rising fees; credit losses half the rivals'; narrowing signs named), Q3 weighs for, Q4
IN on confusion and weighs against on guidance, Q5 IN on integrity with the sales-practices doubt recorded, Q6 Part A
undecided and Part B weighs against. **Reversal condition, in one line:** a price at or below about $173 (the central case
clearing the ten percent floor), on owner cash and growth no worse than shown here, would reopen the file at Q7; below about
$102 no pencil would be needed.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): commits
      for STEP 0 to Q1, Q2, Q3, Q4, Q5, Q6, and Q7 with the close.
- [x] Every v5 id resolves (`Test Runs/_research 2026-10-06 AXP/check_ids.py`: missing none); every filing fact has its
      accession; no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): net income less the equity the book
      must keep, checked year by year against the cash actually paid out; the sovereign from the U.S. Treasury; the live
      price and the year-end closes flagged as aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (eight items at the foundations, and each question's
      contrary lines).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): this is a run of today, not a point-in-time
      test.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII): price, shares, sovereign, ten-year balance sheets;
      its owner-earnings line was rejected for a lender (STEP 0).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **Owner cash for a lender has no construction.** The Q7 CONVENTION says "owner cash after every real cost"
and the tool computes it from operating cash flow, which for a card lender adds back the provision and leaves loan growth
outside, so the tool's $14.5B "owner earnings" and 7.08% "yield" would have cleared a floor this run closes on. I built owner
cash as net income less the rise in equity (the capital the regulated book must keep), checked against dividends plus
buybacks less issuance; that is a CONVENTION of mine, confessed at Q4, and the framework should state one for banks and
card lenders (the SECTOR METHOD covers insurers only). (2) **The growth input fails when the endpoints are capital moves.**
The PG specific requires growth "measured on the aggregate owner cash"; here that gives -3.71% (2021 to 2025) or 15.25%
(2022 to 2025) depending on one year, both artefacts of capital release and rebuild, against **[L2005-003]**. I used net
income growth with a level payout and showed the 15.25% case; the CONVENTION should say what to do when owner cash for a
regulated lender is driven by capital ratios rather than by the business. (3) **The bank door's two halves.** The row asks
for "very cheap money on the deposit side" **[M2002-022]**; the settled rule asks only that both sides "can be read". AXP's
deposits are readable and cost more than Capital One's; I read the settled rule as governing and carried the cost to Q2,
but the text does not say whether cheapness is part of the Q1 test or only a Q2 weight. (4) **Rows spoken by holders about
the company under analysis.** The ledger carries several rows in which the speakers, holders of about a fifth of this
company, praise it; the framework has an anchor-date rule for later rows but no rule for a row that is an interested
holder's statement about the very name being run. I used them as tests, not findings, and declared it; the framework should
say so. **Tool defect:** `tools/run.py` prints an operating-cash-flow "owner earnings" line, a yield against the sovereign and
a "growth the price assumes" for banks and card lenders without a warning; its ten-year balance-sheet table omits deposits,
the main liability of a bank. Not fixed here (the brief forbids it); reported.
