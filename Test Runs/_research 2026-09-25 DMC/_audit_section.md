
---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; Q3-Q6 not opened as gates)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 rests on the 10-K read whole)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none used)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none used; the [E4-04] perimeter close was
      considered and refused, reason at Q2)
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2025 OCF $245.1M rebuilt from
      its lines; ties)
- [x] Owner earnings on a multi-year mean; every window stated (3, 5, 10, 18 years); capex band disclosed as a
      judgment (beneath the close, not governing)
- [x] Competitor row filled (5 filers of roughly 9; four peers flagged as companyfacts-only for some years); the verdict
      does not rest on it
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (5.47%, US Treasury, 09/24/2026, raw CSV)
- [n/a] Value stated as a round-number range (the computation beneath the close is in round dollars and carries no box)
- [n/a] One bar chosen, not both; windage count stated (ONE, stated in the computation; no bar chosen because Q5 did
      not open)
- [x] Prices dated; aggregator used for the live quote only and flagged (Yahoo, close 2026-09-24)
- [x] Run committed to git (commits listed in the register)
- [x] **Every ledger id cited resolves**: 56 distinct ids, all found in `principle_ledger.csv` (311 rows by
      `csv.DictReader`); rows quoted in this file were copied from the ledger dump in the research folder
      (`ledger_q2.txt`, `ledger_q4.txt`), not from memory.
- [x] **No net-income proxy** anywhere; owner earnings built from OCF, SBC and capex or D&A only.
- [x] **Commits by pathspec only**; nothing of the other session's (the CRM re-look hunks in the queue file and
      `tools/alerts.json`) staged or committed.

**Limits of this run, stated.**
- The 10-K footnotes were read for the acquisition, divestiture, impairment, tax and legal matters, not line by line
  for every note; the segment note was read through the MD&A and releases.
- The peer row's Chiquita, Dole Food and Seneca figures and Dole plc's 2021-2022 are companyfacts values not checked
  against their statements (flagged in the row). Del Monte Pacific (Singapore) was not attempted.
- No SEC enforcement or litigation sweep beyond Item 3 and the documents listed; no guidance history pulled [E3-48].
- The acquired Del Monte Foods business has no filed financial statements at this registrant (no 8-K/A found), so its
  own economics were judged from the filer's segment line (one full quarter) and its sale out of bankruptcy.

**The brief's priors, tested.**
1. **"Verify which SEC registrant trades as DMC by CIK"**: done first. CIK 0001047340, Del Monte Corporation, formerly
   Fresh Del Monte Produce Inc. (EDGAR former-name dates 1999-02-10 to 2026-06-04), Cayman Islands, December fiscal
   year (last Friday), large accelerated filer. The screen label is the registrant's current name. **Confirmed.**
2. **The deal_note's EX-2.1 and Item 1.01 of 2026-03-25**: read. **DMC is the buyer, not the target**: an asset purchase
   of Del Monte Foods' US packaged-foods business and the global Del Monte® brand out of Chapter 11 ($285M cash, $310.2M
   total consideration), closed 2026-03-19; the EX-2.1 is the APA's Amendment No. 1. The quote is not a spread; the
   perimeter changed (19% of Q2 2026 sales). No DEFM14A, SC TO, S-4, 425 or other bid for DMC in the filing list.
   **The "if bought" branch refuted; the "if buying" branch confirmed.**
3. **The wc_note (payables 61% of 2021 OCF)**: arithmetic confirmed (60.9%); **the inference refuted**: the year's
   total working capital was a $31.8M use, the payables line offsetting a $105.1M inventory build.
4. **level_shift_oe STEP UP 3.89x**: cause found in the filings: capex cut below D&A after 2021 and the 2021-2022
   inventory build reversing in 2023. Normalise down [E4-41].
5. **Width of 4 constructions over 5 years**: rebuilt over 3, 5, 10 and 18 years at both (c) ends: **$65.9M to
   $135.2M**; the screen's range reproduces and the longer windows sit inside it.
6. **Name change and perimeter**: established; the filed annual record FY2008-FY2025 is Fresh Del Monte Produce's,
   with Mann Packing in (2018) and out (2025); Del Monte Foods from 2026-03-19 is in no annual statement.

**Brief errors found: none verdict-bearing.** One discrepancy recorded, as the WS run recorded it: the brief's commit
trailer (`Claude Opus 5 (1M context)`) differs from the session's attribution instruction (`Claude Opus 5.5`); the
brief's form was used on every commit of this run for consistency with the queue's recent history.

**Tooling defects, REPORTED, NOT PATCHED.**
1. **`deal_note()` named the amendment (8-K of 2026-03-25) and not the Asset Purchase Agreement itself (8-K of
   2026-02-12, `0001047340-26-000009`, filed seven days before the FY2025 10-K)**: the known `deal_filings()` blind spot
   for a deal signed before the latest 10-K, recorded at WS the same day. Its label *"plan of merger or
   acquisition"* was right in kind; it cannot say which side the registrant is on, and here it is the buyer.
2. **`working_capital_flag()` fired against a total working-capital use** (2021: one source line offsetting a larger
   inventory use), second instance after CAH. Its wording *"ONE LINE MADE THE CASH"* is wrong in that case.
3. `run.py` prices on the intraday quote ($30.43) where the queue's convention is the prior close; immaterial here
   ($1.43B either way). Its implied growth (-18.6%) differs from the screen's `growth_required` (5.61%) by the known
   definitional difference; not a new defect.
4. `series.py` in this research folder (not a repository tool) initially accepted only 10-K facts, so Dole plc's 20-F
   years were invisible until the form filter was widened; recorded because the same filter lives in several research
   scripts and would hide a 20-F peer silently.

**My own errors, caught before commit.** (1) I first wrote the 2008-2025 capex sum as $1,641M and then $1,941M from
memory of the table; recomputed from `series_DMC.txt` as **$1,883.9M** before the Q2 commit. (2) A first draft of the
beneath-close section said the revolver was $900M with $606M available at year end; the year-end facility was $750M
with $605.5M available, raised to $900M in July 2026; corrected before commit. (3) Two bash heredocs failed on
apostrophes; the sections were written with the Write tool and appended, as the brief warned.

---
## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **FAIL at Q2 (OUT, on the business).** Fresh Del Monte, renamed Del Monte Corporation in June 2026, is a
  banana, pineapple and prepared-foods grower and shipper whose own 10-K says bananas have *"few barriers to entry"*,
  sales depend on *"the availability of seasonal and alternative produce"*, prepared-food *"Consumer choices are driven
  by price"* against private label, and premium pineapple *"has also led to increased competition"*; eighteen filed years
  give an operating margin averaging 3.1% (best 6.1%) and a return on equity averaging 4.6%, level with Dole plc,
  Chiquita and Dole Food in the same years. The 2026-03-25 Item 1.01 is its own $285M purchase of Del Monte Foods' US
  canned business out of bankruptcy: DMC is the buyer, and the quote is not a spread.
- Commits: `4050c0b` (claim), `26ed7ce` (Step 0, Q1), `f844e7c` (Q2), `f8e3ce3` (beneath the close), the audit and
  register commit, and the fold commit.
