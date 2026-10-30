
---
⛔ **Q5 does not open: Q2 is OUT.** The computation above is headed as the protocol requires and carries
no box.

## Q5 — not opened. ## Q6 — not opened as a gate (reversal conditions in words above).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; the file closed at Q2)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the filing)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued; the [E4-04] perimeter
      close was considered and refused because [E3-03] is not passed first)
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026 OCF $18,234K,
      rebuilt from its lines, ties to the MD&A's two subtotals)
- [x] Owner earnings on a multi-year mean; every window from 3 to 17 years published; capex band disclosed
      as a judgment (beneath the close)
- [x] Competitor row filled (5 filers of about 9 named; private brands and brand-level data unavailable,
      stated; the verdict does not rest on the row)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (5.47%, Treasury, 09/24/2026)
- [x] Value stated as a round-number range, not a point estimate (computation only)
- [x] One bar chosen, not both; windage count stated (ONE; no bar applied, Q5 not opened)
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git (claim `a39fa24`, Step 0 and Q1 `29c61e0`, Q2 `19fdcdf`, this section and the fold
      after)

**Brief priors, each tested:**
1. *Fiscal year ends late March* — confirmed (FY2026 ended 2026-03-29; 10-Q to 2026-06-28).
2. *A licence with a meat processor, the Branded Product Program, franchising, a few company restaurants* —
   **confirmed**, with the shares: licensing 84.4% of segment operating income; Smithfield, 10.8% of net
   sales, minimum guaranteed royalties, **expiry March 2032**, optional extension to 2036 only as a condition
   of the Parent termination fee; no renewal right stated in the documents read.
3. *`deal_note` blank; check anyway* — **REFUTED as a description of the security: a live cash merger at
   $102.00 by Smithfield, the licensee**, signed 2026-01-20. The quote is a spread.
4. *An SEC settled action around 2019 over undisclosed perquisites* — **not found** (sweep stated at Q3
   prompts); the one SEC order in the record is director Eide's of 2018 at Aegis Capital.
5. *Verify SBC resolves and is complete* — **resolves 17 of 17 years and is complete** as far as the filings
   show (no stock-settled bonus found).
6. *Debt: amount, maturity, covenants, what it funded* — $47.8M unsecured term loan to 2029, 3.00x net
   leverage covenant; it refinanced notes that funded the 2015 and 2018 special dividends.
7. *Rebuild the width over every window* — done; $11.4M (17y, 5y FY2017-21) to $19.9M (3y); the bottom never
   near zero on any multi-year window.

**Brief errors found:** (1) the brief's "deal_note is blank ... still check" was right to ask, and the blank
itself was wrong (tooling, below); (2) the brief's commit trailer (Opus 5) differs from the session's
attribution instruction (Opus 5.5); the brief's trailer was used, as the CAH run recorded; (3) none
verdict-bearing.

**My own errors caught before commit:** (1) a first Treasury fetch used a wrong URL path
(`resources/` for `resource-center/`) and returned 404; the correct source was then fetched and the saved CSV
checked for the header row and 09/24/2026 before use; (2) a bash heredoc with apostrophes failed, as the brief
warned; sections were written as files instead; (3) I first quoted a restaurant sentence without *"of the
foodservice industry"* and a Conagra sentence without its ® mark, corrected against the source before commit;
(4) I first quoted the release's *"EBITDA 1 ..."* when the line reads *"Adjusted EBITDA 1 ..."*, corrected;
(5) I first wrote that interest ran at $9.9M through FY2023; the MD&As say $10.1-10.8M to FY2022 and $7.7M in
FY2023, corrected; (6) I first wrote that Nathan's disclosed the Eide order "in every proxy since", which the
full-text hits do not show for 2019-2020; narrowed to what was found.

**Tooling defects, reported, not patched:**
1. **`deal_note()` / `deal_filings()` in `tools/sources.py` cannot see a deal signed before the latest annual
   report.** It counts deal forms only after the newest 10-K (*"since"*). Nathan's merger 8-K (2026-01-21,
   with EX-2.1) and PREM14A (2026-03-06) predate the FY2026 10-K (2026-06-09), and the DEFM14A did not exist
   until 2026-09-24, so on the screen date of 2026-09-02 the column was blank for a company under a signed
   cash merger for seven months. Today the same call returns the DEFM14A line. **A pending deal is invisible
   in the window between the next 10-K and the definitive proxy.**
2. **`run.py`'s "GROWTH THE PRICE ASSUMES" printed −9.1%** while the screen's `growth_required` reads +5.46% for
   the same name: `implied_growth()` fades to a fixed 2.5% terminal rate (`tgr=0.025`), so any price below
   about 34 times owner earnings at a 5.47% rate returns a negative "required" growth. Two tools, two
   definitions, opposite signs; a prompt to read, not a number to carry.
3. `tools/sources.annual()` returned Hormel's operating income only through FY2017 (tag change, not
   investigated), so Hormel is not in the row.
