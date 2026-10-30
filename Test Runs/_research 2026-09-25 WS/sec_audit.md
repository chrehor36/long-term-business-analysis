
---
⛔ **Q5 does not open: Q2 is OUT.** The computation above is headed as the protocol requires and carries no box.

## Q5 — not opened. ## Q6 — not opened as a gate (reversal conditions in words above).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; the file closed at Q2)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the 10-K, the Form 10
      and the Klöckner statements filed with the 8-K/A)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued; the [E4-04] perimeter close
      was considered and refused because [E3-03] is not passed first)
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026 OCF $201.2M, rebuilt
      from its lines, ties to the statement, the MD&A and XBRL; FY2023 $315.0M ties Form 10 to XBRL)
- [x] Owner earnings on a multi-year mean; every window FY2021-FY2026 published with both (c) ends and management's
      own maintenance figure; the negative year (FY2022) named in dollars and a word (beneath the close)
- [x] Competitor row filled (4 filers plus Klöckner, of roughly ten; private processors and Russel Metals not
      obtained, stated; the verdict does not rest on the row)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (5.47%, Treasury, 09/24/2026; the
      EUR sovereign owed to any future Q5, stated)
- [x] Value stated as a round-number range, not a point estimate (computation only)
- [x] One bar chosen, not both; windage count stated (ONE; no bar applied, Q5 not opened)
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git (claim `0bee3d3`, Step 0 and Q1 `54d8e48`, Q2 `e0ea7e7`, beneath the close `3efc36e`,
      this section and the fold after)

**Brief priors, each tested:**
1. *Spun off from Worthington Industries in December 2023; fiscal years end May 31; pre-spin years only as carve-out
   statements* — **confirmed**: Separation 2023-12-01; the Form 10's combined statements for FY2021-FY2023 carry the
   same figures the FY2024 10-K later restated for FY2022-FY2023, judged one perimeter with its acquisitions named.
2. *The deal_note's Item 1.01 "most likely a credit facility or offering"* — **refuted**: it is the Klöckner DPLTA
   (2026-09-08), the last step of a cross-border takeover in which **WS is the acquirer** (60.86% on 2026-06-03, 61.87%
   on 2026-06-15, about 62% at the delisting offer). The quote is not a spread.
3. *wc_note: accounts payable moved 39% of FY2023 OCF* — **confirmed and read**: payables −$124.3M against $315.0M;
   working capital as a whole released $139.9M in FY2023 after absorbing $204.0M in FY2022.
4. *Do not assume the perimeter is stable* — **confirmed unstable**: Tempel and a blanking business (FY2022,
   $376.7M), Sitem 52% (FY2026), two toll plants out, and Klöckner (two thirds of pro forma sales) three days after
   the last filed year.
5. *Verify SBC resolves and is complete* — **resolves 6 of 6 years and is complete** (note total equals the cash-flow
   line; 401(k) match in cash).
6. *Any live merger or tender for WS* — **none found**; the tender offers in the record are WS's for Klöckner.

**Brief errors found:** none verdict-bearing. The brief's commit trailer (Opus 5) differs from the session's
attribution instruction (Opus 5.5); the brief's trailer was used, as the NATH and CAH runs recorded.

**My own errors caught before commit:** (1) my first XBRL script passed the `(cik, name)` tuple `cik_for()` returns
into `sec_facts()` and failed; fixed to take the first element; (2) my first draft of the holding-gain sentence at Q2
said the Form 10 recorded a $53M fall "in fiscal 2023"; the Form 10 says fiscal 2022 against fiscal 2021, and the
$48.6M holding losses are fiscal 2023's; corrected and quoted before commit; (3) I first attributed the "market
leading positions" quote to the FY2026 10-K, whose extracted text reads *"c arbon"*; re-attributed to the FY2025
10-K's clean wording; (4) two quotes carried straight apostrophes where the release has curly ones; corrected
against the source.

**Tooling defects, reported, not patched:**
1. **`deal_note()` guessed "most likely a credit facility or offering" for an Item 1.01 that is a German domination
   and profit-and-loss transfer agreement**, and, as the NATH run found, **`deal_filings()` counts deal forms only
   after the newest 10-K**: the business combination agreement with its EX-2.1 (8-K `0001193125-26-019521`, filed
   2026-01-22) predates the 10-K of 2026-07-30, so the screen saw one ambiguous 1.01 and no deal. **A second case
   of the same blind spot, this time on the acquirer's side.**
2. **`acq_note` reads the "acquisitions, net of cash acquired" line only through the newest annual statement**, so a
   purchase closed after the year end (Klöckner, about $787M for the stake plus the debt) is invisible, and the
   stake-building sat on a different line ("Purchases of equity securities", $106.2M in FY2026).
3. `run.py`'s "GROWTH THE PRICE ASSUMES" printed −6.6% against the screen's +5.52%; the fixed 2.5% terminal-rate
   definition the NATH run reported, not a new defect.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **Worthington Steel is a steel processor that says it competes *"primarily on the basis of price"*, prices
  *"primarily based on market factors"* and follows HRC; tons fell 14% FY2021-FY2026 through two acquisitions, its
  engineered laminations leg was written off to *"increased foreign competition"*, and its 3.3-5.7% operating margin
  sits at half the leader's. In June 2026 it borrowed $1.4bn to buy 62% of Klöckner & Co, a distributor earning −0.3%
  to 0.5% on sales, which is now two thirds of it. [E2-58]'s commodity class, no wide and sustainable cost exception.**
- **PASS/FAIL: FAIL at Q2 (OUT, ON THE BUSINESS).** Price **$35.48** (2026-09-24 close, aggregator, flagged) ×
  **50,948,146 shares** (10-K cover, accession `0001968487-26-000026`) = cap **$1,807.6M**; sovereign **5.47%** (US
  Treasury, 09/24/2026). Owner earnings on the pre-Klöckner perimeter $80.3-128.9M across every window of three years
  or more and both (c) ends (5y $89.4-126.8M, 4.95-7.01%; $72.0-109.3M to the WS owner after payments to
  noncontrolling interests, 3.98-6.05%); FY2022 negative (−$28.7M to −$5.6M). The combined company has no filed
  owner-earnings record.
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.
