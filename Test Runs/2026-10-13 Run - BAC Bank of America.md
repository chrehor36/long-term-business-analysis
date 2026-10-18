# Company Run — Bank of America Corporation (NYSE: BAC) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run under `Screens/_daily/_dispatch_brief.md`. The template was copied and committed (commit 9091497a)
before any fetch. A US bank holding company in four segments: Consumer Banking, Global Wealth & Investment Management
(Merrill and the Private Bank), Global Banking, Global Markets, with the rest in All Other. No rename, merger or spin in the
last five years; the deals that made it (Countrywide, 2008; Merrill Lynch, 1 January 2009) are older and are named where
they bear. Research folder: `Test Runs/_research 2026-10-13 BAC/` (notes, the arithmetic script and its output; raw
filings under its ignored `cache/`).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**How each question is applied to a bank (read before anything else, as the brief asks).** Q1 carries the framework's own
bank text: the exclusion ("the exact condition of some of the biggest, you know, banks in the world" **[M2005-068]**; "we don't
understand how much risk the institution is running" **[L2002-018]**), the door ("very little risk on the asset side and very
cheap money on the deposit side" **[M2002-022]**; "It’s always on the asset side." **[M2011-022]**), and the settled sentence that a bank with "a readable deposit
base and a wholesale or derivatives book that its own filing calls unpredictable closes TOO HARD" (Q1, The door against the
exclusion, settled), with test 12's lender items. Q1 owns financial institutions; Q9's test 10 only catches what Q1 missed.
Q2's castle tests would be read on the deposit franchise and on each segment by the business-of-parts paragraph; the cost of
deposits through the 2022 to 2024 rise is the low-cost test (test 6) for a bank. Q3 for a bank reads the capital the
regulators require as the reinvestment that growth compels ("You can change the math of banking [...] by capital
requirements" **[M2016-027]**). Q4 reads the balance sheets first and names financial institutions as "particularly, probably,
prone to it" **[M2013-086]**. Q7's all-equity basis does not fit a bank (stated at the computation below). Q9 reads deposits
that run, wholesale funding and collateral calls (tests 4 to 6). This file closed at Q1, so only Q1 was applied as a STOP.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $54.58 (close 2026-10-12, Yahoo chart through `tools/sources.py`; aggregator, live quote only, flagged per
  operator rule 5). Intraday 2026-10-13 at 15:43 UTC: $54.29.
- **Shares by class** from the latest filing's cover: 6,992,748,365 common, one class ("On July 30, 2026, there were
  6,992,748,365 shares of Bank of America Corporation Common Stock outstanding"), 10-Q for the quarter to 2026-06-30, filed
  2026-07-31, accession `0000070858-26-000394`; `python Screens/cover_shares.py BAC` returns the same. Check: the company holds
  no treasury stock (repurchased shares are retired; the 10-K balance sheet shows 7,212,464,345 "issued and outstanding" at
  2025-12-31, accession `0000070858-26-000157`); the fall to 6.99bn is the repurchase programme ($40bn authorised from
  2025-08-01, 10-Q note 2 to the repurchase table). No 8-K or prospectus filed after 2026-07-31 (EDGAR submissions list read
  2026-10-13). Preferred stock ($25,992m carrying value at 2025-12-31) is a separate senior class and is not added.
- **Market cap:** $381,664m (6,992.7m x $54.58).
- **Sovereign for the earnings currency:** 5.60%, US Treasury daily par yield curve, 30-year, 2026-10-09 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-25, accession `0000070858-26-000157` (Items 1, 1A, 7, 7A,
  8: balance sheet, equity statement, Note 3 Derivatives, Note 12 Commitments and Contingencies, Note 23 segments, the
  fair-value Level 3 note); 10-Q Q2 2026, `0000070858-26-000394`; proxy DEF 14A filed 2026-03-23, `0001193125-26-118929`; for
  the span, the 10-Ks for FY2010 (`0000950123-11-018743`, five-year summary 2006 to 2010, TARP note), FY2015
  (`0000070858-16-000137`), FY2019 (`0000070858-20-000011`), FY2021 (`0000070858-22-000062`), FY2022 (`0000070858-23-000092`)
  and FY2023 (`0000070858-24-000122`). **One figure cross-checked against the filed statement:** total assets $3,411,738m at
  2025-12-31 on the filed Consolidated Balance Sheet equals the XBRL `Assets` fact; net income $30,509m on the filed
  income statement equals the XBRL `NetIncomeLoss` fact.
- `python tools/run.py BAC` printed one line: "BAC: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." A bank's
  cash-flow statement carries no capex tag it reads, so no arithmetic line was usable; the arithmetic was done by hand from the
  filings in `Test Runs/_research 2026-10-13 BAC/arith.py` (output in `arith_output.txt`). Stock pay: $4,001m in 2025
  (XBRL `ShareBasedCompensation`), expensed inside net income. Depreciation and amortization $2,314m in 2025.

**The balance sheets, 2015 to 2025, read in Step 0 because the file closes before Q4** **[M2025-032]** (USD bn, year ends;
XBRL facts from each year's 10-K, the 2024 and 2025 columns read on the filed statement):

| | 2015 | 2017 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Total assets | 2,144 | 2,281 | 2,434 | 2,820 | 3,169 | 3,051 | 3,180 | 3,261 | 3,412 |
| Loans and leases | 885 (net) | 926 (net) | 974 (net) | n/a | 979 | 1,046 | 1,054 | 1,096 | 1,186 |
| Held-to-maturity debt securities, at cost | 85 | 125 | 216 | 438 | 675 | 633 | 595 | 559 | 523 |
| Held-to-maturity, fair value | 84 | 123 | 220 | 448 | 666 | 524 | 497 | 451 | 442 |
| Trading account assets | 177 | 209 | 230 | 199 | 247 | 296 | 277 | 314 | 367 |
| Deposits | 1,197 | 1,310 | 1,435 | 1,795 | 2,064 | 1,930 | 1,924 | 1,965 | 2,019 |
| Repo and fed funds purchased | 174 | 177 | 165 | 170 | 192 | 196 | 284 | 332 | 345 |
| Long-term debt | 237 | 227 | 241 | 263 | 280 | 276 | 302 | 283 | 318 |
| Shareholders' equity | 256 | 267 | 265 | 273 | 270 | 273 | 290 | 294 | 303 |
| Goodwill | 70 | 69 | 69 | 69 | 69 | 69 | 69 | 69 | 69 |
| Accumulated OCI | -5 | -7 | -7 | -2 | -5 | -21 | -18 | -15 | -11 |
| Retained earnings | 88 | 114 | 156 | 164 | 188 | 207 | 225 | 241 | 262 |

What moved and why, in the filings' own figures: deposits rose 69% over the decade and 44% in 2019 to 2021 alone, while
loans rose about a third (gross loans $897bn in 2015, $1,186bn in 2025); the surplus went into held-to-maturity bonds bought at the low rates of 2020 and 2021 (at cost $216bn in 2019,
$675bn in 2021), and when rates rose those bonds fell to $108.6bn below cost at the end of 2022, $98.0bn in 2023, $108.1bn in
2024 and $80.2bn at the end of 2025. That last loss is 29% of common equity ($277.3bn = $303.2bn less $26.0bn preferred) and is
carried nowhere in equity or in regulatory capital. Goodwill has sat at $69bn to $70bn since 2011, the residue of past acquisitions. Retained earnings tripled ($88bn to $262bn) while total equity rose only 18%: the difference went out in
repurchases (common stock and paid-in capital fell from $62.4bn at 2021 to $26.1bn at 2025). Repo funding rose 76% from 2022
to 2025 ($196bn to $345bn) and trading assets rose 32% in the two years to 2025, as the markets book grew. What the figures cannot say: the
value of the $1.03 trillion markets book under stress, and how long the deposits stay; Q1 turns on the first.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is to ask "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, and for a bank the answer depends wholly on whether its condition can be known from the outside, which is
Q1. No macro view is used: rates moved this bank's deposit cost from $0.5bn to $38.4bn in three years, but "macro conclusions
are — just never enter into the discussion" **[M2000-094]**; the rate rise enters only as evidence of how the deposit franchise
behaved. Nobody paid to sell me this name was consulted; the 10-K's "Responsible Growth" language was read as the filer's own.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the filer's trading measures look small against its capital:
total market-based portfolio VaR averaged $78m in 2025 (10-K Table 42), trading-related revenue was positive on more than 99
percent of trading days with the largest daily loss $2m, and recurring Level 3 assets were 0.29 percent of total assets; this
argues the markets book is readable. (2) A ledger row names this bank for the soundness of its funding, "If you look at the
Bank of America or Wells Fargo, they get an enormous amount of money from a natural customer base" **[M2012-012]**. (3) Under
Q1's parts reading, Global Markets earned 16.8% of five-year segment net income and does not decide. (4) Against the deposit
side: deposits fell $134bn (6.5%) in 2022, and $857.9bn (42%) of deposits were uninsured at 2025-12-31 (10-K, Liquidity), where
the speakers say "if people think that deposits are sticky anymore, they’re just living in a different era" **[M2023-047]**.
(5) Against the asset side: net charge-offs were $16.2bn, $33.7bn and $34.3bn in 2008 to 2010 and net income to common was
$2.6bn, minus $2.2bn and minus $3.6bn (FY2010 10-K five-year summary), with a $45.0bn TARP preferred investment repaid in
December 2009.

## THE STANDING RULE
The buyer's conduct only: no position is taken by this run, and any purchase would be from cash without borrowing, since
"borrowed money has no place in the investor's tool kit" **[L2014-005]**; a common shareholder's loss is capped at the price
paid, so nothing in the target's books reaches the buyer's ruin except through the buyer's own sizing, "We are never going to
risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. Not engaged.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it for a bank.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**. For a financial institution the door is narrow: a bank
can be understood when it has "very little risk on the asset side and very cheap money on the deposit side" **[M2002-022]**,
"It’s always on the asset side" **[M2011-022]**; and the settled sentence closes TOO HARD the bank that has both a readable deposit
base and a wholesale or derivatives book that its own filing calls unpredictable, because "even though I could understand every
individual transaction they did, I don’t regard the whole enterprise, or the operation of it, necessarily as being within my
circle of competence" **[M2002-094]**. Size alone decides nothing, on the framework's own reading of the row that speaks of
"the exact condition of some of the biggest, you know, banks in the world" **[M2005-068]**.

**The deposit side: readable.** Deposits $2,018.7bn at 2025-12-31, of which $532.1bn noninterest-bearing (26%), against total
assets of $3,411.7bn (10-K balance sheet, `0000070858-26-000157`). Interest on deposits, against the average of the year-end
balances: 0.03% in 2021, 0.24% in 2022, 1.36% in 2023, 1.98% in 2024, 1.73% in 2025 (XBRL `InterestExpenseDeposits` and
`Deposits`, same accession). Against the three rivals' own filings, the same measure in 2023, 2024 and 2025: JPMorgan Chase
1.69%, 2.06%, 1.82%; Wells Fargo 1.20%, 1.78%, 1.46%; Citigroup 2.71%, 3.11%, 2.60% (tagged data from their FY2025 10-Ks,
accessions `0001628280-26-008131`, `0000072971-26-000133`, `0000831001-26-000011`; transcription, not cross-checked to the
filed statements). This is money from "a natural customer base" **[M2012-012]**, cheaper through the rate rise than two of
the three rivals. The deposit side passes the door's first half.

**The asset side, in three parts.**
1. *Loans, $1,185.7bn, and the bond books: readable.* Loans by category, the allowance ($13.2bn) and the charge-off history are
   filed; the held-to-maturity book is disclosed at cost ($522.7bn) and at fair value ($442.4bn), so its $80.2bn loss can be
   read off the balance sheet. The credit record over the last real cycle is filed too (provisions $26.8bn, $48.6bn and $28.4bn
   in 2008 to 2010). "Banks [...] get into trouble because they make big mistakes in lending, but it’s not required of you"
   **[M2003-115]**.
2. *The markets book: the filer calls it unpredictable.* Global Markets held $1,032.9bn of assets at 2025-12-31, 30% of the
   total, up from $747.8bn at 2021-12-31 (Note 23 of the FY2025 and FY2022 10-Ks). On the balance sheet: trading account assets
   $367.0bn, securities borrowed or bought under resale agreements $316.6bn, derivative assets $40.9bn, funded in part by
   repurchase agreements $344.7bn, trading liabilities $106.0bn and short-term borrowings $48.1bn. Note 3 lists derivative
   contracts with a total notional of about $42.4 trillion (the sum of the table's contract/notional column: interest rate
   $29.6tn, foreign exchange $8.7tn, equity $2.6tn, commodity $0.4tn, credit $1.1tn), gross derivative assets of $292.2bn
   reduced to $40.9bn by $224.1bn of master netting agreements and $27.2bn of cash collateral; a footnote adds that a small part
   ($3.3bn of gross assets) sits under "master netting agreements where the enforceability of these agreements is uncertain under bankruptcy laws in
   some countries or industries", and the credit-derivative note says "the notional amount is not a reliable indicator of the
   Corporation’s exposure to these contracts". The filer's own words, Item 1A: "Our derivatives businesses may expose us to
   unexpected risks, which may result in losses and adversely affect liquidity"; "We are party to a large number of derivatives
   transactions that may expose us to unexpected market, credit and operational risks that could cause us to suffer unexpected
   losses", including "losses resulting from risks not taken into account or anticipated in the development, structuring or
   pricing of a derivative instrument"; and of the market-risk models, "Our models and strategies to assess and control our
   market risk exposures are subject to inherent limitations. In times of market stress or other unforeseen circumstances,
   previously uncorrelated indicators may become correlated" (10-K FY2025, Item 1A, `0000070858-26-000157`).
3. *The growth of that book.* Global Markets assets rose 38% in four years. The framework's lender test reads it: "in all types
   of financial institutions, rapid growth sometimes masks major underlying problems (and occasionally fraud). The real test of
   the earning power of a derivatives operation is what it achieves after operating for an extended period in a no-growth mode"
   **[L2004-009]**.

**Weighed against the contrary evidence.** The VaR, Level 3 and daily-loss figures written down under the foundations are the
filer's own model outputs, and the same filing says those models "are subject to inherent limitations" in stress; the lender test is "what it achieves after operating for an
extended period in a no-growth mode" **[L2004-009]**, and a quiet year's distribution is not that. The parts reading (Q1's holding-company paragraph,
extended to operating segments on 2026-10-06) would let Consumer Banking decide, since it earned 39.5% of 2021 to 2025 segment
net income and Global Markets 16.8% (Note 23, All Other's net loss left out of the base: Consumer Banking $59.0bn, Global Banking $43.5bn, Global Markets $25.2bn, GWIM
$21.9bn over the five years); but the markets book is not a separate company: it sits on the one balance sheet, against the
one equity that protects the deposits, and the settled sentence was written for exactly this case (a very large bank in Test
B'), on the row that says understanding each transaction is not understanding the whole: "I don’t regard the whole
enterprise, or the operation of it, necessarily as being within my circle of competence" **[M2002-094]**. The bank-specific sentence governs (see What in the framework was wrong or
unclear). The ledger row naming this bank, "they get an enormous amount of money from a natural customer base" **[M2012-012]**,
speaks of its funding, not its asset side, and by the framework's convention a row about one company never decides a STOP
alone.

**The tests, in short.** Key variables, "evaluating how predictable they were first" **[M1998-044]**: the deposit cost and the loan losses can be
read and bounded; the markets book's loss in a stress cannot, on the filer's own statement. How far off could I be, "some model
in our mind of how far off we can be" **[M2011-084]**: in 2008 to 2010 this bank's net income to common summed to minus $3.2bn against plus $29.3bn at JPMorgan Chase
and plus $22.0bn at Wells Fargo (tagged data, same accessions), and its average share count rose from 4.4bn (2007) to 9.8bn
(2010) (FY2010 10-K). Doubt about the perimeter: "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**. The derivatives row of the shelf is the same finding from the same reading: "When Charlie and I finish
reading the long footnotes detailing the derivatives activities of major banks, the only thing we understand is that we don't
understand how much risk the institution is running" **[L2002-018]**; "with financial institutions, it’s much tougher. Then
you add — throw in derivatives on top of it" **[M2005-068]**.

**Which cause.** NATURE. The documents that could answer were read (Item 1A, Note 3 in full with its netting and downgrade
tables, the VaR and Level 3 disclosures, five 10-Ks across the span), and what remains is a forecast the filer itself declines
to make: it writes that its derivatives may bring losses from "risks not taken into account or anticipated". That is test 5
answered by the insider in the filing: "They would say, “That’s too hard.”" **[M2000-105]**. More reading does not cure it:
"Charlie and I could’ve spent 24 hours a day, and had the help of 10 or 20 math Ph.Ds. and we still wouldn’t have known what
was going on" **[M2013-089]**; "We couldn't solve this problem, moreover, even if we were to spend years intensely studying
those industries" **[L1993-023]**. A lower price does not reopen it: "It doesn’t mean it isn’t a good buy. It doesn’t mean it
isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE).** A readable deposit base (cheaper than two of three rivals through the rate rise) and a
  readable loan and bond book sit beside a $1.03 trillion markets book with about $42.4 trillion of derivative notional that the
  filing itself says may bring "unexpected losses" (Item 1A). The rows: "I don’t understand everything that’s going on within
  it" **[M2002-094]**; "we don't understand how much risk the institution is running" **[L2002-018]**; "a lot of things end up in
  the “too hard” pile, and it doesn’t bother us" **[M2006-013]**. The file closes here.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (Q1 closed the file). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The reporting figures are computed beneath the stop under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)** at **Q1**: a readable, cheap deposit base and a readable loan and bond book beside a $1.03 trillion
markets book (about $42.4 trillion of derivative notional) that the filer's own Item 1A says may bring "unexpected losses"
from "risks not taken into account or anticipated". Integrity facts recorded, not judged (Q5 below). No research pass: the
cause is NATURE, and no reading reopens it. COMPUTATION, NOT A CLEARANCE, beside: value range $51.83 to $64.97 a share against
$54.58; fair price $32.65 a share (equity-only, the central basis for a bank; see Q7 below). Q11 belongs to a holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box is unchanged (operator rule 2), each fact with its source, as the habit asks:
"write it down in the first 30 minutes" **[M1997-127]**.*

**Bears on Q2 (the castle; the parts; the field).**
- The parts (Note 23, FY2025 and FY2022 10-Ks; segment net income, USD bn, 2021 / 2022 / 2023 / 2024 / 2025; the 2023 to 2025
  figures as revised in the FY2025 10-K):

  | Part | Net income by year | Five-year sum | Share of the four | Year-end assets 2025 | Decides? |
  |---|---|---|---|---|---|
  | Consumer Banking | 11.9 / 12.5 / 11.6 / 10.8 / 12.2 | 59.0 | 39.5% | $1,039bn | the largest, so it decides |
  | Global Banking | 9.8 / 7.8 / 10.1 / 8.0 / 7.8 | 43.5 | 29.1% | $735bn | no |
  | Global Markets | 4.6 / 4.2 / 4.7 / 5.6 / 6.1 | 25.2 | 16.8% | $1,033bn | no |
  | GWIM | 4.3 / 4.7 / 3.9 / 4.3 / 4.7 | 21.9 | 14.6% | $335bn | no |
  | All Other | 1.4 / -1.7 / -4.0 / -1.7 / -0.3 | -6.2 | left out of the base | $270bn | n/a |
- Deposits through the rate rise: down $134bn in 2022 (6.5%), flat in 2023, up to $2,018.7bn by 2025; interest on deposits
  $0.5bn (2021), $4.7bn, $26.2bn, $38.4bn, $34.5bn (2025). The competitor row (tagged data, accessions under Q1), cost of
  deposits against the average of year-end balances, 2023 / 2024 / 2025: BAC 1.36% / 1.98% / 1.73%; JPM 1.69% / 2.06% / 1.82%;
  WFC 1.20% / 1.78% / 1.46%; C 2.71% / 3.11% / 2.60%. Deposits from 2015 to 2025: BAC up 69% ($1,197bn to $2,019bn), JPM up 100%
  ($1,280bn to $2,559bn), WFC up 17% ($1,223bn to $1,426bn), C up 55% ($908bn to $1,404bn).
- The field's returns over the last full cycle and since: net income to common in 2008 to 2010 summed to minus $3.2bn (BAC),
  plus $29.3bn (JPM), plus $22.0bn (WFC), minus $28.3bn (C). In 2021 to 2025, net income to common over year-end equity less
  goodwill (preferred left in, so understated alike) averaged 12.6% at BAC, 17.8% at JPM, 11.4% at WFC and 7.2% at C (computed
  in `arith_output.txt` from the tagged figures). The FY2025 10-K names no rival, only classes of competitor (Item 1,
  Competition), so the brief's fallback three were used.
- The 10-K's own account of the attackers: "We are increasingly competing with firms offering products solely over the internet
  and with nonfinancial companies, including firms utilizing emerging technologies, such as digital assets" (Item 1).

**Bears on Q3 (capital in, earnings out).** To hold its start-of-year CET1 ratio against the growth in standardized
risk-weighted assets, the bank needed to retain $16.4bn in 2021, released $1.4bn in 2022, and retained $5.2bn, $5.3bn and
$9.2bn in 2023 to 2025 (`arith_output.txt`). Net income to common, after that capital, was 15.9% to 28.8% of revenue in the
window. The bank carried $69.0bn of goodwill against $277.3bn of common equity at 2025.

**Bears on Q4 (the accounts).** The held-to-maturity book stood $80.2bn below cost at 2025-12-31 (fair value $442.4bn against
$522.7bn), outside equity and outside regulatory capital, and $108.6bn below at 2022. Stock pay $4,001m in 2025 (expensed).
The effective tax rate was 5.9% in 2021 and 5.8% in 2020, which the FY2021 10-K attributes to "recurring tax preference
benefits" (tax credits from affordable-housing and renewable-energy investments) and to positive adjustments from U.K. tax law
changes; 2025 tax was $7,186m. Litigation: "a decrease of $15.2 billion in litigation expense which was primarily related to
previously disclosed legacy mortgage-related matters" in 2015 against 2014 (FY2015 10-K, `0000070858-16-000137`); at
2025-12-31 the estimated range of possible loss above accruals was "$ 0 to $ 0.5 billion" (Note 12).

**Bears on Q5 (integrity facts, recorded, not judged).**
- "BANA agreed to a Consent Order announced by the Office of the Comptroller of the Currency (OCC) on December 23, 2024 [...]
  relating to certain aspects of its BSA/AML and Economic Sanctions Compliance Programs" (Note 12, FY2025 10-K).
- "in recent years we have entered into orders or settlements with certain government agencies regarding the rates paid on
  uninvested cash in brokerage and investment advisory accounts that is swept into interest-paying bank deposits, credit card
  sales and marketing practices and representment fee practices and our participation in implementing COVID-19-related
  government relief measures [...] including unemployment benefit processing for California and certain other states"
  (Item 1A, FY2025 10-K); and possible matters "related to fraud perpetrated against our clients in connection with their use
  of electronic payments (including Zelle)" (same).
- The legacy mortgage litigation of 2010 to 2014 (Q4 above).
- Chief executive pay by performance year, 2021 to 2025: $32.0m, $30.0m, $29.0m, $35.0m, $41.0m (proxy filed 2026-03-23,
  `0001193125-26-118929`), against net income to common of $30.6bn, $26.0bn, $24.7bn, $25.3bn, $29.1bn.
- The speakers ask for the bank's culture before a firm buy decision, "that’s hard to do for 99 percent of the banks"
  **[M2008-090]**; not attempted here.

**Bears on Q6 (the money and the owners).** Repurchases, with the average price paid (equity statements, FY2022 and FY2025
10-Ks): 2021 615.3m shares for $25,126m ($40.84); 2022 125.9m for $5,073m ($40.29); 2023 146.7m for $4,576m ($31.19); 2024
331.5m for $13,104m ($39.53); 2025 451.9m for $21,433m ($47.43). The $40bn programme of 2025 states no price. Common dividends
declared $6,575m (2021) to $8,083m (2025); the quarterly dividend was raised 14% to $0.32 in July 2026 (10-Q). The share count:
average 4.4bn in 2007, 9.8bn in 2010 (the Merrill Lynch and Countrywide deals were paid in stock, and $19.3bn of common
equivalent units were sold in 2009 toward repaying TARP; FY2010 10-K), 7.2bn at 2025, 6.99bn at 2026-07-30. Against the bottom
of the computed range ($51.83, below), every year's average repurchase price sat below it; this is the line Q6's buyback test
would read, recorded and not weighed.

**Bears on Q7: COMPUTATION, NOT A CLEARANCE.** Every figure here is arithmetic beneath a closed STOP and carries no entry
language (operator rule 3). Script and output: `Test Runs/_research 2026-10-13 BAC/arith.py`, `arith_output.txt`.
- *Owner cash for a bank, a CONVENTION of this run* (the framework has a sector method for insurers and none for banks; one-line
  rationale: a bank's operating cash flow swings with its trading and loan balances and is not cash an owner can take out,
  while the capital the regulators require is its compulsory reinvestment). Maintenance-only owner cash is net income
  applicable to common shareholders, which is after interest, the provision for credit losses, depreciation, amortization,
  all stock pay and the company's own tax, with depreciation taken as the maintenance spend, "the depreciation charge is not
  inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**. Owner cash after growth
  spending deducts the CET1 capital retained to hold the start-of-year CET1 ratio against the year's growth in standardized
  RWA. Cross-check: cash actually returned to common owners averaged $21.2bn a year in 2021 to 2025 against $20.2bn of owner cash
  after growth capital. Not a net-income proxy in the sense operator rule 5 forbids: no cost is left out, and the capital charge
  is added.
- *Tax:* the company's own (Q7, Whose tax). The low rates come from recurring credits bought with new investment each year, not
  a carryforward that runs out inside ten years, so the statutory recomputation does not apply; the 2021 U.K. adjustment sits in
  an aberrational year already handled by the cycle base.
- *Specific (a), the cycle base:* the first window year, 2021, is aberrational on the filer's own description ("The allowance
  for credit losses had a reserve release of $6.8 billion for 2021"; provision a $4.6bn benefit; FY2021 10-K). The base is the
  last full cycle, 2019 to 2025, from the last pre-pandemic year through the 2020 reserve build and the 2021 release: average
  net income to common $25,443m (maintenance-only), owner cash after growth capital $19,770m. The literal window 2021 to 2025
  is shown beside: $27,125m and $20,192m.
- *Growth:* between successive cycles it cannot be measured on a comparable basis (the 2007 to 2018 cycle holds the stock-paid
  Countrywide and Merrill deals, whose own averages were losses, and RWA was measured under earlier capital rules), so it is the
  cycle's own end-to-end rate on aggregate owner cash after growth capital, 2019 to 2025: 0.33% a year (both end years ordinary
  on the filer's description). The halves rate, 3.6%, is beside. Literal window: end-to-end 8.9% runs from the aberrational 2021,
  so by specific (b) the halves rate applies there, minus 1.3%, a decline carried as the bottom.
- *Specifics (c) to (f):* (c) no acquisition for cash was found in the window in the 10-Ks read; (d) a bank's working capital is
  its balance sheet, and its growth is charged through the capital retained; (e) the maintenance-only case is the no-growth end,
  and the growth case carries the capital charge against the growth it bought; (f) the shown rates are below the discount rate,
  and year-ten owner cash would be 20.2% of revenue grown at its own rate against a highest share in the window of 28.8%, so no
  cut.
- *The range, at the 5.60% sovereign, zero growth after year ten:* no-growth (maintenance-only) $454,332m, $64.97 a share;
  growth case **$51.83** a share. The growth case sits below the no-growth case: at the cycle's rate, the capital retained for
  growth bought less than its cost at the long rate, the inversion the specific names, "growth can destroy value"
  **[L2000-023]**. **Range $51.83 to $64.97 a share against $54.58**; width 1.25 to one. Literal window beside: $46.51 to $69.27.
  The long cycle beside, not central: 2007 to 2019 net income to common averaged $9,911m, which at no growth is $25.31 a share at
  the sovereign.
- *The floor, tested first:* at $54.58 no case earns about ten percent: the no-growth yield is 6.67% and the growth case returns
  5.32% (literal window: 7.11% and 4.76%). Had Q7 been reached it would close OUT on the floor, "there’s just a point at which we
  drop out of the game" **[M2003-149]**; it was not reached.
- *Basis, and why the all-equity basis does not apply to a bank (a CONVENTION of this run):* deposits, repurchase agreements and
  the bank's own debt are the materials of its business, and their interest is already inside owner cash; deducting them as net
  debt would charge the cost twice, the reasoning of Q7's own inventory-secured trade finance convention, and the speakers treat
  a receivables book financed "almost entirely with debt (just as a bank would)" **[L2003-019]** as the business, not its
  capital structure. On the template's definition, net debt would be negative by about $790bn (borrowings $365.9bn against cash
  $231.8bn and debt securities $925.6bn), which would add more than twice the market value and is meaningless, since those
  assets back the deposits. The central figure is therefore the equity-only figure, owner cash to common against the market
  value of the common; preferred stock is handled by taking owner cash after preferred dividends and is not deducted again.
- **Fair price (a reporting figure, never a verdict; Part VII): $32.65 a share** (equity-only; each end case valued at ten
  percent: no-growth $36.38, growth case $28.91, averaged). Literal window beside: $32.62. There is no all-equity figure for the
  reason above. No cheap price is reported.

**Bears on Q8.** The bond at 5.60% against a no-growth owner-cash yield of 6.67% at $54.58 (computation above).

**Bears on Q9 (debt and exposures).** Uninsured deposits $857.9bn of $2,018.7bn (42%) at 2025-12-31; repurchase agreements
$344.7bn; short-term borrowings $48.1bn; long-term debt $317.8bn. CET1 ratio 11.4% (standardized) against a regulatory minimum
of 10.0%; stress capital buffer 2.5% and G-SIB surcharge 3.0% (Item 1); Tier 1 leverage ratio 6.8%; total assets 11.3 times
total equity. Downgrade triggers: additional collateral of $146m at one notch and $1,057m at two (Note 3); $2.8bn of
contractual collateral not yet posted. Collateral held $119.7bn and posted $97.8bn under derivative agreements. In 2008 to
2010 the bank took a $45.0bn TARP preferred investment, repaid in December 2009 (FY2010 10-K). The speakers on deposits today:
"you don’t know what has happened to the stickiness of deposits at all" **[M2023-054]**.

**Bears on Q12.** No business of the kind the newspaper test names was found in the filings read.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 9091497a); written question by question; committed after Q1 (commit
      7e56e314) and at the close (write-early).
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (an `_overnight.lock` file
      was present in `Screens/_daily/` when that folder was listed); the fold is the dispatcher's (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, read or searched. Contamination, declared and not used: a
      directory listing of `Test Runs/` (to confirm my folder did not exist) showed the file names of twenty-one other runs dated
      2026-10-13 (ASTE, EMAT, GRFXY, HDSN, HRIBF, HTCMY, HY, JCSE, KIGRY, KMTUY, LHSW, LONKF, LZ, MSM, MTW, SIEGY, SITE, SQFT, TEX,
      TPICQ, VELO); the session context carried the git status (other research folders such as AYI and ARCB), recent commit
      subjects (an MTW fold) and a memory index line saying holding reviews are owed under v5, without names. No file or line
      about BAC was seen.
- [x] Every v5 id resolves (`check_ids.py`, PASS); every filing fact has its accession; the rivals' figures are tagged data,
      marked as transcription.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, with the bank CONVENTION confessed and cross-checked to cash returned; the sovereign
      from the Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (foundations, five items); facts for later questions under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` printed no arithmetic line for a bank; nothing it printed was used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Two of Q1's rules point opposite ways for a large bank. The holding-company paragraph, extended to operating segments on
2026-10-06, lets the deciding part (Consumer Banking, 39.5% of segment profit) carry the file, and Global Markets (16.8%) would
not "matter"; the settled bank sentence closes TOO HARD on the derivatives book whatever its share of profit. The text does not
say which governs. I applied the bank sentence, because the markets book sits on the one balance sheet against the one equity
that protects the deposits, and its share of assets (30%) is not its share of profit; a sentence saying so would settle it.
(2) "a wholesale or derivatives book that its own filing calls unpredictable" does not say whether a risk-factor sentence counts,
or whether the filer's quantitative measures (VaR averaging $78m, Level 3 at 0.29% of assets) can answer it. Every money-centre
bank's 10-K carries such risk factors, so the sentence as written closes them all at Q1, perhaps as intended, but it is not
said. (3) There is no owner-cash method for a bank, as there is for insurers; operator rule 5 forbids a net-income proxy and
`tools/run.py` cannot read a bank, so this run confessed its own capital-retention convention. (4) Q7's cycle base does not say
which cycle a bank's is: the 2019 to 2025 cycle (a mild credit year) gives a range of $51.83 to $64.97, while the 2007 to 2019
cycle that holds the bank's own losses gives about $25 at no growth; the choice moves the figure more than any other input.
(5) The all-equity basis and "net debt" are undefined for a bank; this run reasoned from the trade-finance convention to an
equity-only central figure. (6) The brief's error, as found: it says to take the lines of evidence from "the latest 10-K's Item
1, Item 1A and Item 7", but one of the lines it names, "loan losses over the cycle including 2008 to 2010", is not in that
10-K at all (its Item 7 covers 2023 to 2025 and Item 6 is reserved); it came from the FY2010 10-K. A second: it applies "Q2's
business-of-parts paragraph" to the four segments, but for a bank the parts first meet the bank rule at Q1 (the holding-company
paragraph, which uses the same threshold), and the file closed there; and BAC reports a fifth line, All Other, with a five-year
net loss, which the parts threshold does not say how to treat (left out of the base here, said so).
