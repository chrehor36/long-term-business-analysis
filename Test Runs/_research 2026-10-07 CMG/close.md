## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED: the file closed OUT at Q7. Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED: the file closed OUT at Q7. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED: the file closed OUT at Q7.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED: the file closed OUT at Q7. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7, by the floor**: value range **$18.00 to $31.52** a share (all-equity basis, central construction, 1.75 to
one) against **$30.90**, the price inside the range near its top; expected return at the price 3.2% (no growth) to 5.7%
(growth capped at 8.1%). Fair price (reporting figure) **$13.02** all-equity, **$12.84** equity-only. Q1 IN, Q2 IN with
the weight stated, Q3 weighs for, Q4 weighs for on the accounts, Q5 integrity IN and ability weighs for weakly, Q6 weighs
against. Not a TOO HARD; were Q7's growth cut-back refused, the uncapped ranges (3.1 to 4.0 to one) would close TOO HARD on
width, never IN.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury yields 5.64% (2026-10-06). Owner cash at the price, all-equity basis: the
  five-year maintenance-only average $1,240.6M is 3.2% of the enterprise value of $38,326M; the all-spending average
  $1,003.6M is 2.6%; 2025's maintenance-only figure $1,576.7M is 4.1% (`q7calc.out`).
- **Q9 (debt and exposures).** No borrowings at any year-end 2016-2025 or at 2026-06-30; a $500M revolver, undrawn, with
  covenants of total leverage at most 3.0x and fixed-charge coverage at least 1.5x (8-K `0001058090-25-000047`; Note 12).
  Operating lease liabilities $5,419.2M at 2026-06-30, cash rent paid $520.3M in 2025; legally binding leases signed but not
  commenced $834.4M; purchase obligations $1,887M at 2025-12-31 (Note 9; MD&A). Cash and investments $775.0M at 2026-06-30,
  down from about $2.29B at 2024 year-end after buybacks. "Certain key ingredients are purchased from a small number of
  suppliers" (10-K Item 1). One event's size on the record: the 2015 outbreaks took comparable sales down 20.4% for 2016
  and operating income from $763.6M to $34.6M; the company did not borrow through it.
- **Q12 (how the money is made).** Not a named business of the section. Facts for the newspaper test: the 2020 Deferred
  Prosecution Agreement for adulterating food (two misdemeanor counts, fine paid); the 2022 New York City Fair Workweek
  settlement and other employment-law audits (10-Ks FY2020-FY2024); a food-safety modifier in executive bonuses (proxy).
- **Q10.** No position is taken by a blind run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `768687a9`, made after `tools/run.py` and `cover_shares.py` had
      run but after the copy; see the note below); written question by question; committed after each with a pathspec of
      the run file and the research folder only (write-early).
- [x] Dispatched: the brief allowed the per-question commits; the lock `Screens/_daily/_overnight.lock` was present when
      the run began and was not touched by this analyst; the fold is the dispatcher's (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched by me. Seen by accident and
      declared at the top: commit subjects and untracked-folder names in the session context, and a memory index line. The
      acceptance test, which the brief requires, reads every run file (its check 5); I viewed only the tail of its output,
      which names framework files only.
- [x] Every v5 id resolves: `python "Test Runs/_research 2026-10-07 CMG/check_run.py"` reports 119 citations (85 distinct),
      none missing, no E-ids, every quoted fragment standing before an id found in that row. Every filing fact carries its
      document and accession here or in `filings.md` and `comp.md`.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 NOT REACHED; nothing after it is a
      clearance. No figure was reported as a clearance before Q1-Q4 closed IN (operator rules 2 and 3).
- [x] Owner cash after every real cost: operating cash flow less stock pay less capital spending (or depreciation for the
      maintenance case), never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations, seven items) **[M1997-127]**; facts for later questions under
      AFTER THE STOP. Integrity facts were judged at Q5 (reached), so the box line carries no integrity flag.
- [x] No row dated after the anchor is cited: this is not a point-in-time run (anchor today).
- [x] Only the arithmetic lines of `tools/run.py` were used; its rule text, ids and floor were ignored (Part VII).
- [x] `python tools/check_framework.py` PASS before the closing commit.
- **Declared departures.** (1) `tools/run.py` and `Screens/cover_shares.py` ran a minute before the first commit of the
  copied template; the copy itself was made before any fetch. (2) Two passages were corrected inside this run before its
  close and the corrections are visible: Q3's quotation of the unit goal ("in the U.S." was a truncated read of "in the
  U.S. and Canada", marked in place), and six sentences in Q2, Q4, Q5 and Q7 restructured so that no id stands beside a
  filing quotation or the framework's own wording (found by the brief's check script; the quotations themselves were
  unchanged). (3) Two CONVENTIONS of this run, confessed in Q7: the peak-to-peak growth reading in place of specific (a)'s
  cycle averages, and the cut-back of growth to 8.1% computed from the filer's unit goal and the decade's average-sales
  growth. (4) The new-unit return in Q3 is computed from company averages; the filer files no new-unit sales or payback.
  (5) Competitor data are thin before 2021 for the company-owned rivals (CAVA and Sweetgreen file from their IPOs) and some
  MCD and Taco Bell years were not extracted (`comp.md`, gaps line).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (a), cycles, fails for a grower whose cycle was its own collapse.** The window's first year (2021) is
aberrational on the filer's own words, so (a) sends the base to the last full cycle's average and the growth to successive
cycles' averages. The owner-cash cycle runs peak to peak 2015-2024; its average ($506.8M) is half of today's earning power
because the business doubled inside the cycle, and no earlier full cycle exists in the filings, so the growth step cannot be
run. I kept the five-year base and measured growth peak to peak, confessed as a CONVENTION of this run. (2) **Specific
(f), the cut-back, has no target.** "Any result that traces to an absurdity is cut back" says to cut, not to what. Here the
cut decides the box: capped at 8.1% the range is 1.75 to one and the file closes OUT; uncapped (15.3% or 18.0%) the range
is 3.1 to 4.0 to one and closes TOO HARD on width. Two analysts could split OUT and TOO HARD on this name exactly as Test A'
did before the range convention. I cut to growth at today's margin on the filer's own unit goal; the framework should say
what the cut-back lands on. (3) **Specific (e) is silent on year eleven.** When growth spending is charged against the
growth for ten years and growth then stops, does the cash after year ten return to the maintenance-only figure? I assumed
yes (it raises the top); the text does not say. (4) **The fair price's "midpoint".** Midpoint of the range in dollars, but
the floor must be applied to a cash stream; I mapped the dollar midpoint to the growth rate that produces it on the central
construction and discounted that stream at 10%. A second reading (the midpoint of the two ends' growth rates) would give a
different figure. (5) **All-equity basis for a net-cash company.** The text defines owner cash "before interest" with net
debt added; for a company that earns interest on cash, the after-tax interest income must come out of owner cash or the cash
is counted twice. I removed it; the text does not say so. (6) **Q2 test 9, ask the competitors**, cannot be run from filings
by a blind analyst; recorded as not available. (7) **Section C's "full cycle" for a change for the better** was
satisfied here by one trough-to-peak span; the text does not say whether a company-specific collapse and recovery counts as
the "cycle" the convention means.
