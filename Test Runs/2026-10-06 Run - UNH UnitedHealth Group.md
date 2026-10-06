# Company Run — UnitedHealth Group Incorporated (NYSE: UNH) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template before any fetch (commit
`b5cabf7`).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the run queue, the prepped reading list and `tools/alerts.json` were not opened. Whether
the operator holds or wants the name is unknown to this analyst.

**Contamination declared.** (1) A directory listing of `Test Runs/` made to check the template copy showed a file named
`2026-08-31 Run - UNH (UnitedHealth) v4.1.md`. It was not opened; its name says only that a v4.1 run of this company exists,
nothing of its result. (2) Training memory of the company, held as a prior to be replaced by the filings, not confirmed by
them: the 2025 guidance withdrawal and chief executive change, press reports of a Justice Department investigation of the
Medicare Advantage business, and a Berkshire purchase of the shares in 2025. Each was checked against primary filings and
is cited below only from them (the Berkshire holding from its own 13F-HR). (3) The analyst's general prior that UNH was a
steady compounder for most of two decades; written down here so that the filings, not the prior, decide Q1.

Working folder: `Test Runs/_research 2026-10-06 UNH/` (tool outputs, `FILINGS READ and extracts.md` with every accession
and the quoted extracts, `arithmetic.py` and its output).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $378.58 (2026-10-05; `tools/run.py` live quote, **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock $.01 par value, **897,594,847** shares (10-Q
  for the quarter to 2026-06-30, filed 2026-08-10, accession `0000731766-26-000197`; `python Screens/cover_shares.py UNH`).
  No other class on the cover.
- **Market cap:** 897.594847M x $378.58 = **$339,811.5M** (`arithmetic.py`).
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for 2025, filed 2026-03-02, accession `0000731766-26-000062` (Items 1, 1A in part,
  7, 8 in part); 10-Q for the quarter to 2026-06-30, filed 2026-08-10, accession `0000731766-26-000197` (MD&A regulatory
  trends, legal note); the 2026 proxy, DEF 14A filed 2026-04-21, accession `0001104659-26-046125` (fetched; Q5 and Q6 were not
  reached and nothing in it is relied on); the latest earnings release, 8-K EX-99.1 of 2026-07-16, accession
  `0000731766-26-000191`, with the four releases and the 8-K of 2025 that carry the 2025 outlook and its withdrawal, and the
  8-K item 8.01 of 2025-07-24 (accessions in the working folder file and at Q1).
- **One figure cross-checked against the filed statement:** cash flows from operating activities 2025, `tools/run.py`
  19,697 ($M, XBRL) against the filed consolidated statement of cash flows **19,697** (10-K, accession `0000731766-26-000062`).
  Agrees. Capital spending 2025, tool 3,622 against the filed "Purchases of property, equipment and capitalized software
  (3,622)". Agrees.
- `python tools/run.py UNH` refused to price the name: "SIC 6324 (Hospital & Medical Service Plans) is an insurer. THIS SCRIPT
  CANNOT PRICE IT. Operating cash flow contains float growth" (saved as `run_py_output.txt`). Run again with the cover count
  supplied (`--shares 897.594847 --years 5`, saved as `run_py_output_shares_override.txt`) for the arithmetic lines only (its
  rule text, ids and floor are v4 material and are ignored, Part VII): OCF 2021 to 2025 = 22,343 / 26,206 / 29,068 / 24,204 /
  19,697 $M; SBC 800 / 925 / 1,059 / 1,018 / 971; D&A 3,103 / 3,400 / 3,972 / 4,099 / 4,361; capex 2,454 / 2,802 / 3,386 /
  3,499 / 3,622; the ten-year balance-sheet table (equity $38,177M in 2016 to $100,090M in 2025, goodwill $47,584M to
  $110,499M, debt on the face $78,389M at 2025). **These are not owner cash.** The tool's own warning is borne out by the
  filed cash-flow statement: the 2025 operating cash includes an increase in medical costs payable of **$5,824M** (2024
  $2,503M, 2023 $3,482M), which is float, money held but not owned, and the operating cash also carries investment income.
  The sector method (`Framework/SECTOR METHOD v5 - insurers and float companies.md`) would govern the insurance part at Q3,
  Q4 and Q7; the run closed at Q1 before either was needed, so no owner-cash figure is computed and none is offered.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one "would be happy buying this stock if the market closed for five years"
**[M1997-109]**, and so the run asks what UnitedHealth will earn, not what the quotation will do. No macro forecast enters: "macro
conclusions are — just never enter into the discussion" **[M2000-094]**. The question that decides this run is not macro: it
is what one customer, the federal government (44% of 2025 revenue through CMS premiums alone, 10-K accession
`0000731766-26-000062`), and the states will pay, which is the price of the product, and the run keeps the two apart. Who is
paid to tell you: the chairman's "long-term growth objective of 13 to 16 percent" (8-K EX-99.1 of 2025-05-13, accession
`0000731766-25-000134`) is the seller describing what he sells, "don’t ask the barber whether you need a haircut"
**[M2011-083]**; the rows ask for the projector's past projections **[M1995-050]**, and the company's own one-year projection
for 2025 is set beside its outcome at Q1. The analyst's habits: the worst anchor "is always your previous conclusion"
**[M2016-054]**, and the analyst's prior (a steady compounder) is declared above so that it can be destroyed or kept on the
evidence; the run looks for "what’s wrong" and "what you’re missing" **[M2025-013]**, in the case against its own close as
much as in the case for it.

**Contrary evidence, written down as found** **[M1997-127]** (the case against the Q1 close, set down as it came up):
1. **The record.** Operating earnings rose in every one of the fifteen years 2009 to 2023, from $6,359M to $32,358M, through
   the 2010 health law, a decade of Medicare Advantage rate notices and a pandemic (XBRL OperatingIncomeLoss from the 10-Ks;
   `arithmetic.py`). A business whose earnings marched that steadily looked foreseeable for most of two decades.
2. **The speakers on regulation.** "we tended to overestimate the difficulties from regulation" **[M2004-058]**; and in a
   business exposed to politics "economics usually win out" **[M2012-074]**. Health spending grows: 19% of GDP in 2025 on the
   company's figure (10-K Item 7).
3. **A distinction the speakers draw.** A political threat over "pricing, and distribution" is of a different order from one
   aimed at the product itself **[M1999-119]**; nobody proposes to abolish health cover.
4. **The insider wrote a number.** Management states a long-term growth objective of 13 to 16 percent (above), which bears on
   test 5 at Q1.
5. **Berkshire's own conduct.** Berkshire's 13F-HR for 2025-06-30 (accession `0000950123-25-008343`) lists 5,039,564 UNH
   shares in two lines; someone at Berkshire judged the shares buyable in mid-2025. The 13F-HR for 2026-06-30 (accession
   `0001193125-26-352200`) lists none. This is a fact about Berkshire's conduct, not a row; it is not used as evidence for or
   against the close, and is written down because it runs against it.
6. **The system's moat.** Buffett called the moat of the health system as a whole "a huge moat" (the row's note to
   **[M2018-041]**); the row itself says that does not give each company in it a moat.

## THE STANDING RULE
Owning the shares outright, unborrowed, at a size the buyer could see halved without being forced to sell, puts the buyer at
no risk of ruin; the rule binds the buyer's financing and sizing, which this run does not set: "Never risk permanent loss of
capital." **[L2023-005]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in this run
asks the buyer to borrow or to commit what he has and needs **[M2012-081]**.

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
