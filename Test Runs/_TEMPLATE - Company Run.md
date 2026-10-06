# Company Run — <COMPANY> (<EXCHANGE>: <TICKER>) — <YYYY-MM-DD>
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** the operator holds / does not hold this name (check `PORTFOLIO.md`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $ ___ (close YYYY-MM-DD; source; aggregator flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: ___ (document, date, accession `__________-__-______`;
  `python Screens/cover_shares.py TICKER`; read the charter note before adding classes).
- **Market cap:** $ ___M.
- **Sovereign for the earnings currency:** ___% (issuing authority, dated; `python tools/sources.py`).
- **Filings read** (operator rule 4): the 10-K / 20-F / securities report (document, date, accession), the latest 10-Q,
  the proxy. **One figure cross-checked against the filed statement:** ___.
- `python tools/run.py TICKER` arithmetic lines only: owner cash after every real cost by year, five-year average,
  capex and D&A, SBC resolved and complete.

## THE FOUNDATIONS (not a gate)
One paragraph: which foundation bears on this name (a share is a business; the market serves, not instructs; margin of
safety; no macro enters; who is paid to tell you; the analyst's habits), with ids. **Contrary evidence, written down as found** **[M1997-127]**: ___. *(This line asked for a pre-committed
falsifier until 2026-10-05; that CONVENTION was removed under the v5 scope directive.)*

## THE STANDING RULE
Does owning this put the buyer at risk of ruin (the buyer's conduct, not the target's)? One line, with ids.

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
- [ ] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session; the run is folded into the register before the dispatcher moves on (operator rule ten). A run not in the
      register binds nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); anything of
      them seen by accident is declared under contamination, not used.
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
