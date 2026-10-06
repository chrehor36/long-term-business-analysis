# Company Run — The Goldman Sachs Group, Inc. (NYSE: GS) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
Blind analyst run of record, at the operator's request. Research folder: `Test Runs/_research 2026-10-06 GS/` (tool
output, the filing extracts with accessions, the peer XBRL script, the id check). The skeleton of this file was copied
from the template before any fetch.

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. I did not open
`PORTFOLIO.md`, any earlier run or research folder for GS, any holding review, the session-state files, the queue
register, the prepped reading list or `tools/alerts.json`. **Contamination, declared:** I read one other company's v5 run
of 2026-10-05 (CCB Coastal Financial, a bank) for form only, which showed me how a previous analyst applied the bank door
at Q1; that is a form contamination toward a Q1 close and is named here so it can be discounted. My training-memory of
Goldman Sachs (a dealer-bank whose earnings swing with markets) is a prior; it is replaced below by what the filings say.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $893.46 (quote of 2026-10-05 read through `python tools/run.py GS` on 2026-10-06; **aggregator, flagged** per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class of common stock, **291,171,408** shares (Form 10-Q for the
  period ended 2026-06-30, filed 2026-08-03, accession `0000886982-26-000297`; cover as of 2026-07-17;
  `python Screens/cover_shares.py GS`). The preferred series and depositary shares listed on the 8-K covers are not common
  equity and are not added. The 10-Q balance sheet shows 291,442,355 outstanding at 2026-06-30.
- **Market cap:** about $260,150M (291,171,408 × $893.46).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, dated 2026-10-05
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4), all from EDGAR, CIK 0000886982:
  - Form 10-K for FY2025, filed 2026-02-25, accession `0000886982-26-000091` (business, risk factors, MD&A including the
    deposit table, market risk and VaR, liquidity, the statistical disclosures; Notes 4, 5 and 7 on fair value and
    derivatives; the balance sheet and statement of changes in equity).
  - Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-03, accession `0000886982-26-000297` (balance sheet, Level 3
    table, derivative note totals).
  - DEF 14A, filed 2026-03-20, accession `0001193125-26-117433` (fetched; not read for Q5 or Q6, which were not reached).
  - Form 8-K, 2Q26 earnings, filed 2026-07-14, accession `0000886982-26-000294`, EX-99.1 (`a2q26gsearningsresults.htm`),
    the latest earnings release on 2026-10-06.
  - Form 8-K, Items 2.02 and 8.01, filed 2026-01-08, accession `0000886982-26-000004` (the Apple Card transition: a $2.48B
    reserve release against a $2.26B revenue reduction in Q4 2025; the segment change).
- **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $1,809,320M on the Consolidated
  Balance Sheet of the 10-K, against $1,809,320M in `tools/run.py`'s XBRL transcription of the same accession. They agree;
  total shareholders' equity, $124,972M, agrees likewise.
- **`python tools/run.py GS`, arithmetic lines only** (output saved as `run_py_output.txt`). Price, shares, sovereign and
  the ten balance-sheet year-ends are used. Its "owner earnings" lines (operating cash flow of −$12,587M, −$13,212M and
  −$45,154M for 2023 to 2025, giving a negative "yield") are **meaningless for a dealer-bank**: its operating cash flow is
  dominated by changes in trading assets, trading liabilities and customer receivables and payables (the tool itself
  flags +$57,560M of trading-liability change inside 2025's figure) and says nothing about cash an owner can take out.
  They are not used. Nothing the tool prints as a rule, an id or a verdict was read (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this firm's earning power and condition will be in ten years,
not where a stock that has run to 2.4 times book goes next. The market serves and does not instruct **[M2006-077]**: a
record quarter (2Q26 net earnings $6,628M, annualized ROE 23.5%, EX-99.1) and the price that follows it carry no
instruction about value. **Who is paid to tell you** bears with unusual force here, because the subject *is* the barber:
"you do not get impartial advice from Wall Street — (laughs) — when there’s (an) enormous amount of fees possible from one
action, and no fees applicable from another action." **[M2020-037]**; "don’t ask the barber whether you need a haircut"
**[M2011-083]**. Goldman's own descriptions of its risk are read as a seller's. The analyst's habits: the worst anchor
"is always your previous conclusion" **[M2016-054]**; my prior about the firm, and the form of the CCB run I read, are the
anchors to resist in either direction.

**Contrary evidence, written down as found** **[M1997-127]**, in the order the filings gave it (against my prior that the
firm's condition cannot be read, as well as for it):
1. *Against the prior:* Level 3 financial assets were only 1.1% of total assets at 2025-12-31 ($20,324M), and "the fair
   values for substantially all of our financial assets and liabilities are based on observable prices and inputs" (10-K,
   `0000886982-26-000091`). Most of the book is marked to observable prices.
2. *Against the prior:* average daily VaR was $90M in 2025 and $92M in 2024, small against equity of $124,972M; one-day
   regulatory VaR was exceeded on only three days in 2025 (10-K).
3. *Against the prior:* deposits are now $501,422M, the largest single funding source, of which $269.63B is FDIC-insured;
   consumer deposits are $207,902M (10-K deposit table). There is a retail deposit base that did not exist a decade ago.
4. *For the prior:* derivative notional of $43,530,881M at 2025-12-31, up from $37,127,322M, and $52,831,907M at
   2026-06-30 (10-Q, `0000886982-26-000297`); gross fair values of $360,080M (assets) and $391,214M (liabilities) are
   reduced to $52,953M and $84,405M only by netting agreements and collateral.
5. *For the prior:* those deposits cost 3.94% on average in 2025, against 2.68% at Morgan Stanley and 1.82% at JPMorgan
   (peer row below); the "consumer" deposits are Marcus and Apple Card balances, and Apple Card is being transitioned away
   over about 24 months (8-K, `0000886982-26-000004`).
6. *For the prior:* the 10-K's own words on its market risk measure: "Previous moves in market risk factors may not
   produce accurate predictions of all future market moves", and VaR "is most effective in estimating risk exposures in
   markets in which there are no sudden fundamental changes or shifts in market conditions."
7. *For the prior:* total assets rose 17.6% in six months, from $1,809,320M to $2,127,711M, with trading assets from
   $656,796M to $789,083M (10-Q); the balance sheet a reader studies at year-end is not the one at risk six months later.
8. *Against the prior, on test 5 below:* the insiders do write a number down. "Our target (through-the-cycle) is to achieve
   ROE within a range of 14% to 16% and ROTE within a range of 15% to 17%." (10-K MD&A). The same table shows the return
   achieved: 13.9% (2025), 12.0% (2024), 7.3% (2023), and average equity to average assets of 7.0% in 2025.

## THE STANDING RULE
Owning a common share bought with cash puts the buyer at risk of losing what is paid and nothing more; no borrowing, no
collateral and no option given is involved **[M2012-081]**, **[L2023-005]**. The rule is not engaged by the purchase as
such; it would be engaged only by financing it with borrowed money **[L2014-005]** or by sizing it so that a total loss
mattered.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it for a bank.** "A bank is inside the circle when both sides of its balance sheet can
be read from its filings, the little-risk asset side and the cheap deposit side **[M2002-022]**, and outside it when the
asset side cannot **[M2005-068]**." And: "A bank that has both a readable deposit base and a wholesale or derivatives book
that its own filing calls unpredictable closes TOO HARD: the readable half does not make the unreadable half readable
**[M2002-094]**." (Q1, The door against the exclusion, settled). The door is the oddball bank with "very little risk on the
asset side and very cheap money on the deposit side" **[M2002-022]**; "It’s always on the asset side." **[M2011-022]**.

**The balance sheet at 2025-12-31** (10-K, accession `0000886982-26-000091`; $M; share of total assets of $1,809,320):

| Assets | $M | % | Liabilities and equity | $M | % |
|---|---|---|---|---|---|
| Trading assets (fair value) | 656,796 | 36.3 | Deposits | 501,422 | 27.7 |
| Securities borrowed + resale agreements | 334,215 | 18.5 | Repo + securities loaned + other secured | 305,049 | 16.9 |
| Customer and other receivables | 185,842 | 10.3 | Customer and other payables | 231,865 | 12.8 |
| Cash | 164,259 | 9.1 | Trading liabilities (fair value) | 262,552 | 14.5 |
| Loans, net | 237,734 | 13.1 | Unsecured short- and long-term borrowings | 355,959 | 19.7 |
| Investments (AFS, HTM, other) | 194,262 | 10.7 | Other liabilities | 27,501 | 1.5 |
| Other assets | 36,212 | 2.0 | Shareholders' equity (incl. $15,153 preferred) | 124,972 | 6.9 |

Segment assets: Global Banking & Markets $1,582,670M of the $1,809,320M (10-K segment note). At 2026-06-30 total assets
were $2,127,711M and equity $122,742M (10-Q, `0000886982-26-000297`).

**1. The deposit side: partly natural, not cheap, and not the main funding.**
- Deposits are $501,422M, 27.7% of assets, by source: consumer $207,902M (Marcus and Apple Card customers), private bank
  $100,770M, transaction banking $69,764M, brokered certificates of deposit $47,288M, deposit sweep programs with
  broker-dealers $34,363M, other (substantially all institutional) $41,335M. Time deposits are $185,270M, with a weighted
  average maturity of about 0.7 years (10-K deposit table).
- What they cost: 3.94% on interest-bearing deposits in 2025 (4.73% in 2024), against a net yield on all interest-earning
  assets of 0.82% (10-K statistical disclosures). The peer row below sets this beside Morgan Stanley at 2.68% and JPMorgan
  at 1.82% on the same arithmetic. This is not "very cheap money on the deposit side" **[M2002-022]**; it is money bought
  at near-market rates, a good part of it through brokers and from rate-shopping savers, and the Apple Card half of the
  consumer base is being handed to another issuer over about 24 months (8-K, `0000886982-26-000004`).
- What carries the rest of the balance sheet: repo, securities lending and other secured financings of $305,049M, customer
  payables of $231,865M, trading liabilities of $262,552M and unsecured borrowings of $355,959M. The secured and unsecured
  borrowed funding alone ($661,008M by my sum of those lines, research notes) exceeds the deposits. The rows' test is
  whether funds come "from a natural customer base" or "on a wholesale basis, and that money can run pretty fast."
  **[M2012-012]**; and of a finance company, whether "I can continually fund it, you know, on a basis, independent from
  using Berkshire’s credit" **[M2002-094]**. The private-bank and transaction-banking deposits are natural; most of the
  funding is not.
- Verdict on this half: readable, and the reading is that it is a dealer's funding with a bank's deposit book attached,
  not the cheap deposit side of the door.

**2. The asset side: the loan book can be read; the dealer book, which is most of the balance sheet, cannot.**
- Loans, $237,734M net, are 13.1% of assets; the investment portfolios, $194,262M, are mostly marked or held to maturity.
  Taken alone these could be read as a lender's book is read.
- The rest is a dealer's: trading assets of $656,796M, securities borrowed and resale agreements of $334,215M, customer
  receivables of $185,842M. Behind them is a derivatives book with a **total notional of $43,530,881M** at 2025-12-31
  ($37,127,322M a year earlier; $52,831,907M at 2026-06-30), about 348 times shareholders' equity. Its gross fair values,
  $360,080M of assets and $391,214M of liabilities, become $52,953M and $84,405M on the balance sheet only after
  $261,175M of counterparty netting and about $46B of cash-collateral netting (10-K Note 7). What the owner holds is
  therefore a net position whose value depends on the enforceability of netting agreements, the sufficiency of collateral
  and the solvency of counterparties in the event that tests them.
- This is the case the rows name in so many words: "When Charlie and I finish reading the long footnotes detailing the
  derivatives activities of major banks, the only thing we understand is that we don't understand how much risk the
  institution is running." **[L2002-018]**; "But with financial institutions, it’s much tougher. Then you add — throw in
  derivatives on top of it, and, you know, it’s — no one probably knows, you know, perfectly, what some of the — or even
  within a reasonable range — the exact condition of some of the biggest, you know, banks in the world." **[M2005-068]**.
  Test 12 of Q1 asks of a derivatives book whether both sides of a trade "put on the books a profit that day"
  **[M2004-026]**; no outside reader of Note 7 can answer that for this book.
- **The filing's own words on the predictability of this book** (10-K, risk factors and MD&A): credit spreads are "subject
  at times to unpredictable and highly volatile movements", and "The market for credit default swaps has proven to be
  extremely volatile and at times has lacked a high degree of transparency or liquidity"; "In periods when volatility is
  increasing, but asset values are declining significantly, it may not be possible to sell assets at all or it may only be
  possible to do so at steep discounts"; and of the firm's own risk measure, "Previous moves in market risk factors may not
  produce accurate predictions of all future market moves" and VaR "is most effective in estimating risk exposures in
  markets in which there are no sudden fundamental changes or shifts in market conditions". The filing calls the book
  unpredictable in exactly the circumstances in which its condition would matter.

**3. The key variables and the ten-year question.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**, and the first step is "trying to identify the key
variables in that particular business, and evaluating how predictable they were first" **[M1998-044]**. Here the variables
are the level of market volatility and client activity (the 10-K: "Certain of our market-making activities depend on
market volatility"; market making was $17,993M of $58,283M of 2025 net revenues, and FICC and Equities together
$31,057M), the cost and availability of wholesale funding, and the capital rules, which "can change the math of banking,
and the attractiveness of banking, totally" **[M2016-027]**. The return achieved moved from 7.3% to 13.9% on equity in two
years, on average equity of 7.0% of average assets; a high return in "basically a commodity — money" is read for how much
of it is gearing **[M2007-013]**, and assets to equity went from 9.9 times at 2016-12-31 ($860,165M / $86,893M,
`tools/run.py` transcription) to 14.5 times at 2025-12-31 and 17.3 times at 2026-06-30 ($2,127,711M / $122,742M). None of
these variables is one I can forecast for ten years, and the condition of the book at any moment inside those ten years
is the thing the rows say "no one probably knows" **[M2005-068]**.

**4. Weighed against the contrary evidence (items 1 to 3 and 8 above).** Level 3 assets are 1.1% of assets and daily VaR
is about $90M; these are real, and they say that most positions are marked to observable prices on a normal day. They do
not reach the deciding question, because VaR by the firm's own description "does not estimate potential losses over
longer time horizons where moves may be extreme" and "does not take account of the relative liquidity of different risk
positions" (10-K), and because a netted derivatives book is as good as its counterparties and its collateral on the bad
day, which no footnote can show. The ROE target is a number the insiders do write down; it is a target for the earnings,
not a statement of the book's condition, and it was missed in each of the three years shown. Understanding each
transaction is not understanding the whole: "even though I could understand every individual transaction they did, I
don’t regard the whole enterprise, or the operation of it, necessarily as being within my circle of competence."
**[M2002-094]**. And the doubt rule decides what is left: "if you have doubts about something being into your circle of
competence, it isn’t." **[M2002-092]**.

**5. Which cause: WORK or NATURE.** The test between them is whether the insiders would write the forecast down (test 5,
**[M2000-105]**). The deciding question here is not the earnings forecast, for which the firm does publish a target, but
the condition of a $43.5 trillion notional derivatives book and the funding that carries it across ten years of markets.
The rows say that question is not answered by more reading: the footnotes were read and taught only that "we don't
understand how much risk the institution is running" **[L2002-018]**; of a book of 23,000 contracts, "Charlie and I
could’ve spent 24 hours a day, and had the help of 10 or 20 math Ph.Ds. and we still wouldn’t have known what was going
on. [...] But nobody can." **[M2013-089]**; "You spot troubles in financial institutions late. It’s just the nature of the
beast." **[M2001-066]**. That is the industry's cause, "We couldn't solve this problem, moreover, even if we were to spend
years intensely studying those industries." **[L1993-023]**, not the reader's. No research pass is opened (section I, the
two causes), and a lower price does not reopen the box: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t
selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. The circle is
not widened to find something to buy **[M1995-018]**.

**The peer row** (same arithmetic, each company's own FY2025 10-K XBRL facts; recorded as evidence for the deposit-side
reading, not as a castle test, since Q2 is not reached):

| Company (accession) | Assets $M | Deposits $M | Equity $M | Assets / equity | Deposits / assets | Deposit interest / average of year-end deposits |
|---|---|---|---|---|---|---|
| Goldman Sachs (`0000886982-26-000091`) | 1,809,320 | 501,422 | 124,972 | 14.48 | 27.7% | 3.94% |
| Morgan Stanley (`0000895421-26-000086`) | 1,420,270 | 415,523 | 111,632 | 12.72 | 29.3% | 2.68% |
| JPMorgan Chase (`0001628280-26-008131`) | 4,424,900 | 2,559,320 | 362,438 | 12.21 | 57.8% | 1.82% |

Deposit interest 2025: GS $18,393M, MS $10,626M, JPM $45,112M; prior year-end deposits GS $433,013M, MS $376,007M, JPM
$2,406,032M (script `peers_xbrl.py` in the research folder). Of the three, GS has the thinnest deposit funding and the
dearest deposits.

- **VERDICT: TOO HARD (NATURE)**, closed at Q1. The deposit half is readable and is not the cheap deposit side of the door
  **[M2002-022]**, **[M2012-012]**; the asset half is a dealer book with $43.5 trillion of derivative notional whose
  condition the filing itself calls unpredictable in stress and the rows say no one can know **[M2005-068]**,
  **[L2002-018]**; "the readable half does not make the unreadable half readable" **[M2002-094]**; the box is "too hard"
  **[M2006-013]**.

**COMPUTATION — NOT A CLEARANCE.** At $893.46 the market capitalisation of about $260,150M is about 2.43 times the book
value per common share of $367.67 at 2026-06-30 (EX-99.1, `0000886982-26-000294`). Recorded as arithmetic only; Q4 and Q7
were not reached, no owner cash was computed and no value is stated.

---
## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (Q1 closed TOO HARD).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED. The ten balance-sheet year-ends of `tools/run.py` were read for
the gearing line in Q1 only; no recast of earnings was made.
## Q5 — WHO RUNS IT? NOT REACHED. The proxy was fetched and not read for a verdict.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED. No range, no fair price, no cheap price.
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED. Its test 10 points back to Q1, where the financial-institution question was decided.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED; not asked by the operator.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**. Goldman's deposit half ($501,422M, costing 3.94% in 2025, 27.7% of assets) is
readable but is not the cheap deposit side of the bank door; its asset half is a dealer book (trading assets $656,796M,
derivative notional $43,530,881M at 2025-12-31 and $52,831,907M at 2026-06-30, about 348 times equity) whose condition
the 10-K itself calls unpredictable in stress and the rows say no one can know **[M2005-068]**, **[L2002-018]**,
**[M2002-094]**. The cause is the industry's, not the reader's: more reading of the footnotes does not cure it
**[L1993-023]**, **[M2013-089]**, so no research pass is opened, and a lower price does not reopen the box **[M2000-038]**.
Q7 not reached; no range, no fair price and no cheap price are stated. Price $893.46 (aggregator, flagged), market cap
about $260,150M, sovereign 5.66%.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each with a pathspec
      (step 0 and the foundations, then Q1 with the NOT REACHED questions, then this close). Q2 to Q12 were not reached,
      so there were no further questions to commit separately.
- [x] Every v5 id resolves: `check_ids.py` (research folder) read every bracketed id in this file against
      `principle_ledger_v5.csv` and found none missing; quoted fragments were taken from the rows' own text. Every filing
      fact has its accession; the derived figures (sums, shares of assets, ratios) are stated with their inputs.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance. The peer row and the price-to-book line are
      recorded as evidence and as a COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy: not computed, because Q4 and Q7 were not reached;
      `tools/run.py`'s operating-cash "owner earnings" was rejected as meaningless for a dealer-bank and not used. The
      sovereign is from the US Treasury, dated 2026-10-05; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (eight items under the foundations, four of them
      against my prior), and weighed in Q1, point 4.
- [x] No row dated after the anchor is cited in a point-in-time run: not a point-in-time run (the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) **"A wholesale or derivatives book that its own filing calls unpredictable."** No 10-K says "our book is
unpredictable" in those words; Goldman's says credit spreads are "subject at times to unpredictable and highly volatile
movements" and that past moves "may not produce accurate predictions of all future market moves". Every dealer-bank 10-K
carries risk-factor language of this kind, so read literally the clause sends every dealer bank to TOO HARD on
boilerplate, and read strictly it sends none. I read it by substance (the size of the book against equity, the dependence
on netting and collateral, the firm's own limits on its risk measure) and said so; the framework should say whether the
test is the words or the book. (2) **Test 5 and the two causes.** The WORK/NATURE test asks whether the insiders would
write the forecast down **[M2000-105]**. Goldman's insiders do write one down, an ROE target of 14% to 16%, so the test
passes on earnings while the deciding question, the book's condition, is one the rows say nobody can answer. The framework
does not say which forecast test 5 is asked of; I applied it to the deciding question and recorded the target as contrary
evidence. (3) **"Very cheap money" has no yardstick.** The door asks for cheap deposits **[M2002-022]** and gives no
measure; I used the cost of deposits against two peers from their own filings, which is my choice, not a rule, and a second
analyst could use the sovereign or the asset yield instead. (4) **Evidence beyond the stop.** As in the CCB run, the
template asks for the competitor row at Q2, which a Q1 close never reaches; I recorded a peer row under Q1 as evidence for
the deposit reading and said it was not a castle test. (5) **Tool defects, reported, not fixed:** `tools/run.py` prints an
operating-cash "owner earnings" for a dealer-bank (−$12,587M to −$45,154M a year) and a negative "yield", which is
meaningless for a firm whose operating cash flow is its trading inventory; and its ten-year balance-sheet table shows "lt
debt" only for 2016 to 2018 (the `LongTermDebtNoncurrent` tag stops) and marks the debt sums for 2016 to 2021 as partial,
so the gearing of a bank cannot be read from it without the filed statements. There is still no sector method for banks
at Q4 and Q7; had this run reached them, the cash figure would have had to be invented and confessed.
