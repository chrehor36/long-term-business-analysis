## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. The file closed at Q2 (OUT); Q3-Q6 are labelled RECORDED, NOT
      GOVERNING in every heading and verdict line.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed ARR, retention,
      customer and revenue series, FY2022 to Q2 FY2027; the excluded parts (agentic AI products; whether AI agents displace
      robotic automation) are named as outside the circle, not as caveats on the IN. Q3's IN is recorded, not governing.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none is used for a governing verdict. NICE Ltd.'s filing
      is named as an unfetched peer that cannot move the Q2 verdict.
- [x] Every UNKNOWABLE verdict states what cannot be known (Q4, recorded: whether AI agents displace the product over five years;
      the range -$340M to +$128M spans zero [E4-25]).
- [x] Step 0: the filing was read, with accession numbers; operating cash, stock pay, D&A, capex and revenue cross-checked against
      the FY2026 10-K face; FY2022-23 from the FY2024 and FY2022 10-K faces; the cover count against the 10-Q balance sheet.
- [x] Owner earnings on multi-year means (five and three years, plus twelve months); windows stated; (c) disclosed as a judgment
      with both ends; stock pay subtracted in full, and because it exceeded 50% of operating cash the grant table was read by
      hand and the larger of charge and grant value shown [E3-70].
- [x] Competitor row filled from four SEC filers' own filings (APPN, PEGA, NOW, SSNC) beside PATH; the unavailable peers named
      with the reason (Microsoft unsegmented, six not on the SEC ticker list, NICE not fetched) and why the class is not PROVISIONAL.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury par yield curve), dated 09/18/2026;
      `sources.sovereign()` stale and not used.
- [x] Value stated as a round-number range (about $2.5-3bn no-growth at the floor), and only as a COMPUTATION - NOT A CLEARANCE.
- [x] One bar chosen, not both: none, because Q5 did not open; windage count zero.
- [x] Prices dated; aggregator (Yahoo) used for the live quote only, flagged, corroborated by two Form 4 sale ranges.
- [x] Run committed to git (template `71c902c`, Step 0 `2d80237`, Q1-Q2 `a022bfd`, Q3-Q6 with audit and register in the next
      commit, fold after).

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
All caught before the text they affected was committed in final form, except the first two, which were committed in Step 0
(`2d80237`) and corrected in the Q1-Q2 commit (`a022bfd`).
1. **The executive PSU count.** Step 0 first carried *"3,375,000 executive PSUs"* from an addition of the 8-K's four named awards;
   the four sum to **3,075,000**, and the 10-Q's Note 16 gives **5.3 million** granted in all on 2026-09-03. Dilution beside the
   cap was corrected from 32.2M (6.2%) to 34.1M (6.6%) and the diluted cap from $7.41bn to $7.44bn. The Step 0 commit `2d80237`
   carries the first figure; history is not edited.
2. **Note numbers cited from memory of DASH's filing.** The Step 0 draft cited 10-Q Notes 5 and 11 and 10-K Note 2; the filings'
   own numbering is Notes 6 (acquisitions) and 12 (equity awards) in the 10-Q and Note 3 (geography) in the 10-K. The 10-Q note numbers
   are in `2d80237`; corrected in `a022bfd`.
3. **Four Q1-Q2 claims drafted ahead of their evidence**, each then tested: that UiPath *"charges per robot and per user"* (no
   filing states the unit of price; replaced with what the filing says); that net retention *"fell in every one of eleven
   consecutive quarters"* (it fell or held for fifteen, with three flat readings); that the company *"restructured four times in
   four years"* (three reductions, the fourth 2.05 filing amends the third); and that it *"changed CEO twice"* (three changes to
   the office, read from the 8-Ks). Also removed: a claim that Kofax is "Tungsten Automation" and that NICE files a 20-F, both
   from memory. **Operator rule 6 in small: nothing written until its evidence exists.**
4. **The survival shape.** The Q4 draft labelled PATH a later instance of *"#11 (a spread that crosses zero)"*; #11 in the index
   is THE PASS-THROUGH. Read against `Screens/SURVIVAL SHAPES - index.md`, PATH is a later instance of **#2** only.
5. **The release count** was first written as seventeen; nineteen EX-99.1s are on disk (the 2022-11-14 8-K carries none).
6. **A shell heredoc failed** on the Step 0 text; the section was written with the Write tool instead. No file was affected.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
- None that changed a number. The brief's prior (a dimensioned per-class cover, META or DASH kind) held, in META's two-class form
  with no zero class; `stateOfIncorporation` (DE) matches the filings, so the DASH charter check found nothing.
- **One thing the brief could not have known:** unlike DASH, the share count was not the only obstacle the triage met. The
  `a8bc84f` `owner_earnings()` is negative at every end for PATH, so the name would have been priced at a negative yield even
  with a count.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`sources.sovereign("USD")` served the cached 09/17 row (5.29%) again**; the ninth recorded occurrence across runs.
- **`cover_shares.py` was not needed**: the two dimensioned dei facts were read directly from the inline XBRL (`dei.py`).
- **The SEC `index.json` endpoint returned HTTP 503** for the 2021 charter 8-K; the exhibit was fetched by its document name
  directly. A retry with a longer wait may be enough; not changed.
- **`floor_screen.capital_acquired` for FY2022** includes capitalised software ($2.95M) and matches the face; from FY2023 the filer
  capitalises none, so the capex end and the D&A end nearly coincide. No defect; recorded so a reader does not look for one.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A tense in Item 1A can be a finding.** Most competition risk factors are conditional (*"may"*, *"could"*). UiPath's has carried,
unchanged for five 10-Ks, a sentence in the past tense: lower-priced competitors *"has resulted in"* pricing pressure. A filer that
reports a realised effect in its risk factors has stated a fact about substitutes, and [E3-03]'s second criterion can be read
from it directly. Grep Item 1A for past-tense verbs before scoring Q2.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- **One line:** PATH FAILS at Q2 (OUT, on the business): criterion (2) of [E3-03] fails in the company's own words across five
  10-Ks (lower-priced competitors *"has resulted in"* pricing pressure; free open-source, bundled and build-it-yourself AI
  alternatives), in a named competitor's 10-K (SS&C lists Microsoft, Pega, UiPath, Appian, n8n and Lyzr), in the retention series
  (145% to 107-109%, customers flat about 10,750 for four years, net new ARR down five years running) and in a record with no
  price increase; [E4-04] fails because the company says it is replacing its basis (rule-based robots to agentic automation).
  Q1 IN. Price US$13.39 (2026-09-18 close); 521,155,409 shares (A 456,464,703 + B 64,690,706, Q2 FY2027 10-Q cover
  `0001734722-26-000050`); cap US$6.978bn; sovereign 5.34% (US Treasury, 09/18/2026). Q3-Q6 recorded, not governing: Q3 IN on
  the binary with flags (a GATE case), Q4 UNKNOWABLE (owner earnings about -$340M to +$128M), Q5 computation only (yield -4.9% to
  1.8% against 5.34% and a ~10% floor).
- **If UNRESEARCHED - THE WORK ORDER:** not applicable to the governing verdict.
- **If UNKNOWABLE:** not applicable to the governing verdict.
