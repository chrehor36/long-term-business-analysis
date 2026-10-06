# Company Run — Amgen Inc. (NASDAQ: AMGN) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule (`PORTFOLIO.md` not opened). Contamination: the analyst carries a training-memory prior of Amgen (a large biotechnology company; Enbrel, Prolia, Repatha; the Horizon acquisition of 2023); it is a prior to be replaced by the filings.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
Working folder: `Test Runs/_research 2026-10-06 AMGN/` (`run_py_output.txt`, `cover_shares_output.txt`,
`sources_output.txt`, `facts.py` and `facts_output.txt` (SEC companyfacts transcription), `calc.py` and
`calc_output.txt` (the arithmetic below), `row.py` (ledger lookup), `h2t.py`; raw filings and their text in `cache/`,
gitignored).

- **Price:** $402.98 (2026-10-05; `tools/run.py` live quote, AGGREGATOR, flagged per operator rule 5).
- **Shares by class:** 540,632,005 common, $0.0001 par, one class, cover of the 10-Q for the quarter to 2026-06-30, filed
  2026-08-05, accession `0000318154-26-000126` (`python Screens/cover_shares.py AMGN`). Balance-sheet count 540.6M at
  2026-06-30 (same 10-Q). Average diluted shares Q2 2026: 544M (earnings release, below).
- **Market cap:** about $217,864M (540.632M x $402.98).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-13, accession `0000318154-26-000010` (Item 1 business,
  significant developments, products, the patent table; Item 1A risk factors in part; Item 7 MD&A overview and product
  sales; the cash-flow statement); 10-Q for the quarter to 2026-06-30, filed 2026-08-05, `0000318154-26-000126` (cover,
  cash-flow statement); 8-K of 2026-08-04, `0000318154-26-000124`, Exhibit 99.1, the second-quarter 2026 earnings release
  (product table, non-GAAP reconciliation, 2026 guidance, pipeline update); 8-K of 2026-07-31, `0000318154-26-000119`
  (Item 1.05, a material cybersecurity incident); 8-K of 2026-01-30, `0001193125-26-030518` (Item 1.02, the rocatinlimab
  collaboration terminated); 8-K of 2026-02-19, `0001193125-26-059490` (Item 1.01, $4.0B of new senior notes); 8-Ks of
  2026-04-22 `0000318154-26-000048` and 2026-05-19 `0000318154-26-000097` (Item 5.02, the chief technology officer's
  retirement and a new chief financial officer from 2026-09-01). DEF 14A filed 2026-04-07, `0001193125-26-145588`:
  retrieved, not read, because the file closed at Q1 before the pay questions.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 $9,958M,
  Consolidated Statements of Cash Flows, 10-K `0000318154-26-000010`; `tools/run.py` transcribed 9,958. Agrees.
  **A discrepancy found in the same check:** stock-based compensation FY2023 is $431M on the filed cash-flow statement
  (10-K FY2025 and the companyfacts value from 10-K FY2023 `0000318154-24-000011`); `tools/run.py` printed 473 from the
  element `AllocatedShareBasedCompensationExpense`. The filed 431 is used below. Reported as a tool defect.
- **Arithmetic lines** (`tools/run.py` for 2023 to 2025; 2021 and 2022 from SEC companyfacts, the values reported in the
  10-Ks `0000318154-22-000010` and `0000318154-23-000017`; `calc.py`; USD M):

| FY | OCF | stock pay | capex | owner cash (capex basis) | D&A | owner cash (D&A basis) | businesses acquired, net of cash | owner cash after acquisitions |
|---|---|---|---|---|---|---|---|---|
| 2021 | 9,261 | 341 | 880 | 8,040 | 3,398 | 5,522 | 2,529 | 5,511 |
| 2022 | 9,721 | 401 | 936 | 8,384 | 3,417 | 5,903 | 3,839 | 4,545 |
| 2023 | 8,471 | 431 | 1,112 | 6,928 | 4,071 | 3,969 | 26,989 (Horizon) | -20,061 |
| 2024 | 11,490 | 530 | 1,096 | 9,864 | 5,592 | 5,368 | 0 | 9,864 |
| 2025 | 9,958 | 494 | 1,858 | 7,606 | 5,167 | 4,297 | 53 | 7,553 |

  Five-year mean: 8,164 (capex basis), 5,012 (D&A basis), 1,482 after the businesses bought. Shown change of the
  aggregate, capex basis, 2021 to 2025: -1.4% a year. Against the market cap: 3.75% (capex basis) and 0.68% (after
  acquisitions). D&A runs four to five times capex because most of it is amortization of acquired product rights
  (`run.py` balance-sheet table: intangibles $32,641M at the end of 2023, $22,276M at the end of 2025). Which of these
  bases is the owner's cash, and whether buying products is the reinvestment needed to stand still, is a Q3 and Q4
  question; it is NOT REACHED (the file closes at Q1), and nothing above is a clearance. **COMPUTATION — NOT A
  CLEARANCE.** 2026 guidance (earnings release): capex about $2.6B; share repurchases "not to exceed $3.0 billion".

## THE FOUNDATIONS (not a gate)
Two foundations bear. **A share is a business:** "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**; the answer turns entirely on what the business will be when the market reopens, which is Q1's
question here. **The analyst's habits:** the prior carried into this run (a durable large biotechnology franchise) is
the anchor the rows warn about, "the worst anchoring effect, which is always your previous conclusion" **[M2016-054]**,
and every business is read for "what’s wrong in things" **[M2025-013]**. **Who is paid to tell you:** the one forward
statement on file is the chief executive's, "we remain confident in our ability to deliver growth well into the next
decade" (earnings release, 8-K `0000318154-26-000124`); "don’t ask the barber whether you need a haircut"
**[M2011-083]**, and projections are not consulted **[M1995-050]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the record is strong on its face: product sales grew
10% in 2025 on 13% volume growth (10-K MD&A); Repatha (+36%), EVENITY (+34%), TEZSPIRE (+52%) and BLINCYTO (+28%) grew in
2025; in Q2 2026 "Twenty-two products delivered at least double-digit sales growth" and "Seventeen products are
annualizing at more than $1 billion" (release); owner cash, capex basis, has stood between $6.9B and $9.9B a year for five
years. (b) The rows themselves record the pharmaceutical group, read as a group, as a moat they underrated: "the
pharmaceutical industry, as a whole, has done very well" and "we did blow it" **[M1999-043]**. (c) The cybersecurity 8-K
says the company "has not identified any impact to its products, manufacturing operations, or financial reporting
systems" (`0000318154-26-000119`). All three are carried into Q1.

## THE STANDING RULE
A cash purchase of this stock, without borrowed money and sized so that a fall of half the price would not force a
sale, does not put the buyer at risk of ruin: "We are never going to risk what we have and need for what we don’t have
and don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**; the owner must
be prepared "to have it go down 50 percent — or more — and be comfortable with it" **[M2020-022]**. The rule is met by the
buyer's conduct, not by the target.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- The test as the draft states it, applied to the filings; the key variables and whether they are foreseeable.
- Routing: a business whose ten-year economics cannot be foreseen because its industry changes fast closes here, TOO
  HARD; a bank is inside the circle when both sides of its balance sheet can be read; a holding company is understood
  by its parts.
- **VERDICT: IN / OUT / TOO HARD**, with ids and the filing fact.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- The castle tests, each with its filing fact: the attacker with money; pricing power and the agony before a rise; unit
  volume and share of mind; the low-cost position; the brand in the customer's mind; would the customer still choose it
  over the low bid; ask the competitors; widening or narrowing; what could destroy it.
- **The competitor row**, same metric from the competitors' own filings (name, metric, accession).
- A castle shown open on the evidence closes OUT; a castle whose future cannot be judged closes TOO HARD.
- **VERDICT: IN / OUT / TOO HARD**, with ids.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- Return on the capital actually needed; reinvestment to stand still and to grow; the growth arithmetic and its caps.
- **WEIGHS FOR / AGAINST / UNDECIDED**, one sentence, with ids. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eight to ten years of them, before the income account** **[M2025-032]** (`tools/run.py`
  prints the ten-year table; read the filed statements behind it). Say what moved and why: equity against goodwill and
  intangibles, cash, receivables and inventory against sales, debt, retained earnings; "what the figures are saying and
  what they don’t say and what they can’t say" **[M2025-032]**. *(line added 2026-10-05: the rule was in Q4 of the
  framework from adoption, and no run had been asked to do it.)*
- The real costs (depreciation, stock pay, restructurings, the recurring "one-time"); EBITDA in the filer's own
  mouth; what the accounts say of management's character. The make-the-numbers habit alone weighs against; with a
  second tell it is suspicion.
- **VERDICT on confusion: IN / OUT; WEIGHS FOR / AGAINST** otherwise, with ids. The recast earnings feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- The two yardsticks; the tells of dishonesty (the proxy, the letters, how they talk about mistakes); love of the
  business; what ability shows in. Integrity applied on doubt alone.
- **VERDICT on integrity: IN / OUT; ability WEIGHS FOR / AGAINST**, with ids.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- Part A: the retention test (a dollar kept worth more than a dollar, over time); buybacks (only below value; a buyback
  with no stated price weighs against unless the prices paid sit at or below the bottom of the Q7 range); issuance and
  deals (value given against value got; an all-stock deal at an undervalued price is the one STOP here).
- Part B: pay tied to what the person controls; the board; the owners as partners.
- **WEIGHS FOR / AGAINST / UNDECIDED**, one sentence per part, with ids.

## Q7 — WHAT IS IT WORTH? STOP.
- How much cash, how sure, how soon, at the long government rate, as a range (the CONVENTION construction: five-year
  average of owner cash after every real cost, carried at the growth shown and capped by Q3, ten years then no real
  growth, at the sovereign; the ends are the no-growth and shown-growth cases).
- The floor (CONVENTION): about ten percent pre-tax expected return, as the speakers stated and qualified it; below it
  the name is quit on, not ranked.
- **Value range:** $ ___ to $ ___ a share against $ ___. **Closes:** TOO HARD if the range is wider than about three
  to one; OUT if the price sits inside or just below a narrower range (not a screamer); IN only if the price is so far
  below that no pencil is needed.
- **VERDICT: IN / OUT / TOO HARD**, with ids.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
- The bond as the first filter, then the ranking against the best thing already held (for a private holder, more of
  what he owns; for a company, its own stock below value).
- **VERDICT: IN / OUT**, with ids.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
- Debt in the business, demands for sudden large sums, counterparties, aggregation; "little or no debt" is the one STOP
  for a whole business bought.
- **WEIGHS FOR / AGAINST**, with ids.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
- Inaction as the default; sizing when sure; the omission as the costliest error. No position is taken here; say what
  the draft would have the buyer do.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
- The newspaper test; the businesses named. **STOP for named businesses; otherwise WEIGHS FOR / AGAINST.**

---
## THE BOX
One line: **IN / OUT / TOO HARD (WORK) / TOO HARD (NATURE)**, the question that decided it, and for a name that reached
Q7 the range beside the price. A TOO HARD names its cause (the framework's section I, the two causes): WORK when the
deciding question is knowable and the work is not done, which opens a research file (Part VII); NATURE when the
industry's insiders would not write the forecast down. Q11 (has the business changed, or only its price) belongs to the holding review, not to a purchase run.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
- [ ] Every v5 id resolves (grep it in `principle_ledger_v5.csv`); every filing fact has its accession; no number
      without a row or a filing.
- [ ] The order was kept; the first STOP that failed closed the run; nothing after it is a clearance.
- [ ] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; aggregator quotes flagged.
- [ ] Contrary evidence was written down as it was found **[M1997-127]**.
- [ ] No row dated after the anchor is cited in a point-in-time run (Part VII).
- [ ] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [ ] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
One paragraph: the instruction found ambiguous, missing or unworkable in this run, and what was done. Every run so far
has had one; a run that reports none is suspect.
