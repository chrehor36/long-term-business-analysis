
## SELF-AUDIT
*Operator rule 6: a run is incomplete until its self-audit is checked. Each line is answered, not ticked.*

- [x] **Questions answered in order; no verdict skipped.** Step 0 and Q1 on 2026-09-13; Q2, Q3, Q4, Q5, Q6 on 2026-09-18,
  each written and committed as it closed (`ea8e241`, `a0f392b`, `32f5edb`, `cf49823`). **Q5 was written only after Q1-Q4 all
  showed IN**, so it carries no "COMPUTATION — NOT A CLEARANCE" heading and is not required to.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat — with one qualification that is stated rather
  than hidden.** Q2 is IN and holds the moat class **PROVISIONAL for Pet Nutrition only (23% of 2025 sales)**, because Nestlé
  Purina and Mars are not SEC registrants. **This is not the protocol violation the rule targets**, because the framework's own
  Q2 text prescribes PROVISIONAL for exactly this case, the provisional part is quantified and does not carry the verdict (the
  verdict rests on Oral Care at 44% of sales, where the row is complete with PG, Unilever and Haleon), and no document exists
  that would resolve it — so it is not UNRESEARCHED either. **Recorded here so an auditor sees it without having to find it.**
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** No verdict in this run is UNRESEARCHED.
- [x] **Every UNKNOWABLE verdict states what cannot be known.** No verdict in this run is UNKNOWABLE. **Two disclosure gaps are
  recorded inside IN verdicts** and neither is a document that exists: hyperinflationary remeasurement is inside net income and
  is not separately quantified in any Colgate filing (Q4); and Purina's and Mars's figures are in no SEC filing (Q2).
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** Twelve 10-Ks, the FY2017 10-K/A, five
  10-Qs, three DEF 14As, every 8-K since 2021 with its EX-99. FY2025 net cash provided by operations $4,198M matched between
  companyfacts, `tools/run.py` and the filed statement. **A second, independent cross-check was added this session on the peer
  side** (operator protocol 4 applied to the competitor row, which it does not strictly require): PG's FY2026 filed income
  statement reads `"NET SALES | $ | 87,032"` and `"OPERATING INCOME | 19,748"`, matching the computed 22.7% cell exactly.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.** Six windows run; the
  **five-year 2021-25 default [E2-42]** is named as the governing one and the spread is carried as part of the range [E4-25].
  **(c) is a disclosed judgment**: total capital expenditures rather than the D&A default, on [E4-47]'s inflation condition,
  with [E5-20] asked on the filing and answered **not** in the exception class. Built by hand from the filed cash-flow
  statements; **no net-income proxy anywhere**.
- [x] **Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED.** Ten peers with the same metrics on the same
  construction; the two unmeasurable competitors named with what cannot be measured, and the affected segment marked
  PROVISIONAL as the framework requires.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 30-year **5.29%, 09/17/2026, US
  Treasury daily par yield curve** — the issuing authority, not the FRED redistribution. The currency choice (USD against a
  two-thirds-international earnings stream) was argued from the documents at Step 0 with its limit stated, and not re-opened.
- [x] **Value stated as a round-number range, not a point estimate.** *"roughly $50 to $75 a share"* on the default window,
  *"roughly $50 to $90"* if two optimistic choices are made together. The cell-by-cell table is shown as the working behind
  the range, never as the answer.
- [x] **One bar chosen, not both; windage count stated.** **Bar 2, the screamer test**, is the bar reported at Q5 and its
  answer is "no". **Bar 1's end margin is deliberately NOT applied on top**, and the reason is written into Q5: **windage was
  spent twice at Q4** — (c) at total capex rather than depreciation, and the working-capital release stripped — and a third
  application would be the stacking [E4-11] forbids. **The count is two, both named, and no third was taken.**
- [x] **Prices dated; aggregator used for live quotes only and flagged.** **$87.73, close of 2026-09-17**, aggregator, flagged.
  Step 0's **$86.80 of 2026-09-11** is recorded beside it as struck-and-superseded, and is independently confirmed by a primary
  filing (the Forms 4 of 2026-09-15 report the same $86.80 for 2026-09-11).
- [x] **Run committed to git.** Six commits, each with a fresh message file and an explicit pathspec; no bare `git commit` and
  no `git add -A` at any point, because the index is shared with a live session working on NCLTY.

### VIOLATIONS AND CORRECTIONS FOUND IN THIS RUN, recorded rather than repaired silently
1. **Two hard-sequence defects in the killed session's `sec_q3_draft.md`, both corrected on the record at Q3:** a leverage line
   asserting *"a franchise's earning power"* before Q2 existed, and a capital-allocation line importing a value range from an
   unrun Q5. The Q5 reference is deleted and the [E5-08](2) test was left OPEN at Q3 and closed at Q5.
2. **An arithmetic error in the same draft, corrected at Q3 with the filed lines:** it put 2016-2025 cash uses at $29,266M
   against "$27,376M of capex-end owner earnings" and concluded a structural reliance on debt. On the filed cash-flow lines the
   uses are $29,326M (its option proceeds of $4,615M do not reconcile to the filed $4,555M) against $28,615M of operating cash
   less capex — a gap of about $711M, roughly a fiftieth of the cash generated.
3. **An over-conservatism in the owner-earnings draft, removed at Q4:** it deducted ESOP dividends from owner earnings as an
   "upper bound". The ESOP note says *"Annual expense related to the ESOP was $ 0 in 2025, 2024 and 2023"* and the shares are
   already inside the count, so the deduction was unjustified and would have been a third spend of conservatism.
4. **Two blank cells in the volume/price extraction, filled from the filings at Q2 and flagged:** Latin America 2018 and
   Africa/Eurasia 2023, both missed by the extractor's sentence pattern, not by the filing.
5. **An error in the resume brief itself, corrected here as the instruction requires.** `_brief_resume_2035.md` section 0 says
   *"Only `SECTION_PG.md` and `SECTION_GIS.md` were finished"* and lists CHD and KMB among those with *"scratch scripts but no
   section"*. **`SECTION_CHD.md` and `SECTION_KMB.md` both exist on disk, complete, written 2026-09-13 20:41**, three minutes
   before the brief's own companion file. Four peer sections were finished, not two.
6. **A tooling defect, and its cause named:** `_research 2026-09-13 CL/ledger.py` crashes with `UnicodeEncodeError` on rows
   containing characters outside cp1252 (it hits [E4-55] and [E2-58]) whenever stdout is the Windows console codepage. It is
   not a data defect and the workaround is `PYTHONIOENCODING=utf-8`. Reported, not patched, because the file belongs to this
   run's scratch folder and the same pattern may exist in other runs' copies.
7. **The WAVE 5 "capex unresolved [E5-20]" label is confirmed a tooling artefact, and the mechanism is now named exactly.**
   The capex fact did not disappear and the line never left the face of the statement: **the XBRL tag changed from
   `PaymentsToAcquirePropertyPlantAndEquipment` (10-K years 2011-2022) to `PaymentsToAcquireProductiveAssets` (2020-2025)**.
   Any reader following only the first tag sees capex stop after FY2022. The filed line reads *"Capital expenditures in the year
   ended December 31, 2025 were $564, an increase from $561 in 2024"*.
8. **A stale line in `PORTFOLIO.md`, reported and NOT edited.** Its header still reads *"Q5 sets no hurdle — it RANKS
   [E4-21]"*, which is the pre-Test-D wording the framework rewrote on 2026-08-28 and which `CLAUDE.md` corrected on
   2026-09-02. The ranked rows beneath it already apply the floor correctly (the ASML row says *"below the [E4-28] floor"*).
   **Left for the operator**: changing a governing header is not this run's to make.

## REGISTER
- **Verdict: [x] IN (about the business) — with the price failing at Q5.**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
- **One line:** *Colgate is a franchise, narrowly — 41.3% of the world's toothpaste dollars, 61.5%-101.0% pre-tax on net
  tangible operating assets across a decade, top of a ten-company competitor row — whose moat has not widened since 2015, whose
  units have grown 7.7 points in ten years while price grew 38 and most of that price recovered devaluation; all four business
  gates are IN, and at **$87.73** the honest pre-tax expectancy on the corpus's default five-year window is **9.35%**, **0.65
  points below the ~10% floor [E4-28]**, so it is **NOT RANKED** and goes to the watch list at **$75.61** and **$50.77**.*
- **If UNRESEARCHED — THE WORK ORDER:** not applicable; no verdict is UNRESEARCHED.
- **If UNKNOWABLE:** not applicable; no verdict is UNKNOWABLE.
- **Named death (Q4):** not insolvency but the transfer of the franchise's rent to the owner of the shelf. **Survival shape #19
  THE SHELF, PROPOSED, pending the operator.**
- **Commits:** Step 0 `d4398ab` · Q1 `0c3de6e` · Q2 `ea8e241` · Q3 `a0f392b` · Q4 `32f5edb` · Q5 and Q6 `cf49823` · this
  audit and the fold, below.
