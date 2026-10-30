
## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed the file OUT). The bond fact is under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT** — decided at **Q7**: the price does not clear the floor on any case in the range. Central value range EUR 59.86 to
119.80 a share (all-equity), against EUR 81.40. Expected returns 0.5% to 5.5% against about 10%.

Q1 IN, Q2 IN (Pulp & Paper decides), Q3 weighs for, Q4 IN with weighings against, Q5 IN (ability for), Q6 Part A for narrowly and
Part B against. The box is a price close, not a business close: the castle stood on the evidence read. Reporting figures: fair
price EUR 35.02 (all-equity; equity-only EUR 31.84).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**, with sources. No verdict on them, and the box is unchanged (operator rule 2).

**Bearing on Q8 (the alternatives).** The euro 30-year AAA sovereign yields 3.78% (ECB, 2026-10-08). The best case at Q7 returns
5.5% at EUR 81.40, and the literal no-growth case 3.3%.

**Bearing on Q9 (debt and exposures).**
- Net cash of 593.3 at 2026-06-30. Borrowings of 370.3: Schuldscheindarlehen 301.4 at end-2025, an OeKB loan of 51.0, a bank
  loan of 100.0, a 50.0 RCF drawing and other local bank debt (FR2025 C 5 c; H1 2026 balance sheet). A committed 500 MEUR
  revolving facility runs to 2030. There are unused committed facilities of 737 and unused guarantee and surety lines of 3,417
  (FR2025 C 5 d). The guarantees issued against performance, advances and warranty are a contingent claim of the kind the
  standing rule names (collateral and sudden demands); **their amount outstanding was not extracted in this run.**
- Part of the net cash is customers' money. Contract liabilities were 2,181.2 at 2026-06-30 (1,718.9 + 462.3, H1 2026), and net
  working capital moved from -639.2 (2011) to +118.0 (2025). A fall in orders unwinds advances: operating cash was 7.8 in 2018,
  with a working-capital draw of -278.7.
- Fixed-price contracts with liabilities that "can vastly exceed the value of the contract in question" (FR2025 D 2 d), EPC and
  consortium risk (D 2 c), and government contracts with weaker safeguards (D 2 e).
- "The product liability area includes some recent cases involving alleged physical injuries and/or deaths due to asbestos
  exposure." (FR2025 D 2 f). Count, amounts and provisions were not extracted. The rows carry "So we don’t go near asbestos."
  **[M2001-032]** as a candidate exclusion, not a ruling (framework Q9); recorded here, not weighed.
- Pension and similar provisions of 348.3 (2026-06-30). The defined-benefit details were not read.

**Bearing on Q12.** No named business of Q12 is involved (equipment for pulp, paper, metals, hydropower, environment and feed).
Nothing was found.

**Bearing on Q5 (integrity):** none beyond what Q5 weighed. The box line carries no integrity flag, because Q5 was reached and
answered.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 995b258e); written question by question; committed after each
      (Q1 dda4a67d, Q2 3fab7d2a, Q3 d97d3fec, Q4 22853453, Q5 584fb925, Q6 aeb9f499, Q7 e3d3ce21, close in the commit after).
- [x] Dispatched run: the brief allowed pathspec commits of my two paths only; the lock and the fold are the dispatching
      session's (operator rule ten). This run binds nothing until it is folded into the register.
- [x] Blind rule kept: no other run file, holding review, `PORTFOLIO.md`, resume-state file, run queue or prepped reading list
      was opened, listed or searched. `ls "Test Runs" | grep -i -E "ADRZY|andritz"` was run once at the start, before the
      template copy, and returned nothing. It was a name search of the folder listing, and I declare it. The accidental
      sightings (commit subjects, a memory line) are under Contamination and were not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in its row
      (`check_citations.py`: 0 problems). No E-ids. Every filing fact names its report and section; no SEC accessions exist for
      this name, so the brief's departure was used (title, date, URL).
- [x] The order was kept; the first failing STOP (Q7) closed the run; Q8 to Q12 are NOT REACHED and nothing after Q7 is a
      clearance.
- [x] Owner cash after every real cost, from the filed cash flow statements (operating cash less all capital spending, lease
      principal and acquisitions); never net income. Sovereign from the ECB. The price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, seven items); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor rule applies.
- [x] `tools/run.py` produced no lines (not an SEC filer); all arithmetic is mine, in `computations.py` and `balance_sheets.py`.
- [x] `python tools/check_framework.py` PASS before each commit.
- **Weaknesses I admit.** (1) The 2019 lease principal is an estimate (lease interest not found); it is outside the central window
      and only touches the cycle base. (2) Company-wide stock-pay cost was not extracted, only the Executive Board figure. (3)
      The remuneration report, the guarantee amounts and the asbestos provisions were not read. (4) Segment scope changes in
      2018/2019 and 2023 blur the 2011 to 2025 Pulp & Paper margin series. (5) Valmet is the only rival with primary figures,
      and its group figures after 2022 include Neles. (6) The Q7 cycle definition is a CONVENTION of this run, and a
      different reasonable one changes the range. It does not change the close: the literal window, the organic pair and the
      equity-only basis all fail the floor too.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Specific (a) assumes an industry cycle, and this series has none.** Owner cash here swings with acquisitions and project
   working capital, not with one industry cycle. The rule says "peak to peak or trough to trough" and gives no way to pick
   cycles when the troughs are deal years and working-capital years. I used two successive five-year windows and confessed it
   as a CONVENTION of this run. The rule could say what to do when the aberration is a spending choice (an acquisition spike)
   rather than a cyclical turn.
2. **"Operating leases left out" has no meaning for an IFRS 16 lessee.** IFRS 16 puts every lease on the balance sheet. I
   deducted lease principal from owner cash and left lease liabilities out of net debt, consistently. The basis rule should
   say which treatment an IFRS filer takes.
3. **A non-deciding open part "carried to Q7 as an ordinary business at no growth"** (Q2, business of parts) has no mechanism in
   Q7, which values group owner cash. I could not value Metals separately from cash-flow data the filer does not split by
   segment. The instruction could say whether segment EBITA after a capital charge, or a share of group owner cash, is meant.
4. **Net cash that is customers' prepayments.** The basis rule subtracts all cash and securities as filed. For an
   advance-funded project business, part of that cash is owed back in work, and it unwinds when orders fall (2018). The rule
   is silent. I followed it as written and recorded the fact at AFTER THE STOP.
5. **Q1's doubt rule against Q4's and Q9's ground.** "If you have doubts [...] it isn't" **[M2002-092]** does not say whether doubt
   about the size and timing of single years (fixed-price project tails) is doubt about the circle. I read it as not, and
   carried that doubt to Q4, Q7 and Q9. A sentence in Q1 would settle it.
6. **The template's Step 0 asks for accessions and `cover_shares.py`**, which do not exist for a non-SEC filer. The brief's
   departure covered it. The template could carry the non-SEC substitute (document, date, URL; issued less treasury from the
   report) itself.
