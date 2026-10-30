## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Step 0 → Q1 IN → **Q2 UNKNOWABLE → file closed.**
      Q3-Q6 recorded under explicit NOT-A-GATE banners; the price is headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the
      audited combined statements and the separation documents. The PROVISIONAL moat class sits at Q2, which
      is not IN.
- [x] **Every UNRESEARCHED item names the artifact and where it lives.** One, non-verdict-moving: Experian
      plc Annual Report 2026, customer-segment revenue (experianplc.com, IR rung, blocked by Incapsula on
      2026-09-13).
- [x] **The UNKNOWABLE verdict states what specifically cannot be known:** CARFAX's position against
      AutoCheck and the unit trend behind its price-led growth; and names the record that would decide it (a
      defined CARFAX unit and price/volume series over two to three standalone years).
- [x] **Step 0: the filing was read, with accession numbers; three figures cross-checked** (2025 revenue
      against S&P Global's segment note; H1 2026 OCF and the cover count against companyfacts).
- [x] **Owner earnings on multi-year means; windows stated; capex band disclosed as a judgment.** The
      five-year default could not be built (no pre-2023 cash-flow statement for the perimeter) and the
      shortfall is stated, not filled from segment lines.
- [x] **Competitor row filled** with two SEC filers and one IR-rung peer; the missing direct competitor is
      the ground of the Q2 verdict, not a footnote.
- [x] **Sovereign for the earnings currency (USD), from the issuing authority (US Treasury), dated
      2026-09-11, struck fresh.**
- [x] **Value stated as a round-number range** ($9-12 conservative to $25-31 optimistic at the floor).
- [x] **One bar recorded (screamer test), windage count one.**
- [x] **Price dated (2026-09-11 close), aggregator flagged.**
- [x] **Ledger ids checked against `principle_ledger.csv` before citing** (every id in this file resolves;
      [E4-27] used for incentives, [E4-52] for converging flags — the brief's warning heeded).
- [x] **Run committed to git** with a pathspec after each section (Step 0 `de1a7d4`, Q1 `c944d57`, Q2
      `1bdc987`, Q3 `20c3866`, Q4-Q6 and audit in the commit that carries this line).

**Errors of my own, corrected before commit:** (1) Q1's first draft said no commercial agreement with S&P
Global was described; the Information Statement describes non-material reciprocal data licences. (2) My
first scan of the growth attribution read only the Form 10's vocabulary; the 10-Q's "price increases"
wording was found on a second pass and became a Q3 flag. (3) The first owner-earnings script derived a TTM
interest figure from half-year interest *expense*, which includes accrued note interest never paid by the
carve-out; replaced with FY2025 cash interest paid, stated as an approximation.

**Brief and tooling defects found (reported, not fixed):**
1. **The brief's pre-check omitted the Form 10-12B, the Form 10-12B/A and three DRS filings** under
   MBGL's own CIK — the documents that hold the only cash-flow statements for the perimeter. It sent the
   run to S&P Global for predecessor history that is filed under MBGL itself.
2. **`tools/sources.py:deal_note()` labels every EX-2.1 "plan of merger or acquisition"**; here it is a
   Separation and Distribution Agreement. The note's instruction to read the exhibit is right; the label
   invites the ACVA/ROKU spread treatment on a spin-off.
3. **The triage label "Mercedes, 20-F filer"** in `Screens/2026-08-31 PREPPED READING LIST (operator
   lists).md` line 1436 and the comment at `Screens/floor_screen.py` line 154, and the WAVE 5 grouping
   "foreign 20-F filers, short XBRL history", are wrong for this ticker.
4. **A date disagreement between two filers:** S&P Global's 10-Q Q2 2026 says the notes were issued *"On
   May 19, 2026"*; MBGL's 10-Q Note 4 says *"On May 29, 2026"*. Immaterial; recorded.
5. **The company's own disclosure record, not a tool:** the report-view metric moved from 31M+ (TTM
   Sep-2025) to 28M+ (TTM Dec-2025) across DRS versions without a stated redefinition.

## REGISTER
- Verdict: [ ] IN [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  **[x] UNKNOWABLE (about my evidence)** — at **Q2**.
- **One line:** Mobility Global (the CARFAX, Polk, automotiveMastermind and Market Scan business spun off by
  S&P Global on 2026-07-01, widely held, $2.0bn of notes paid to the former parent, nothing pending) —
  **Q1 IN; Q2 UNKNOWABLE**: a 43-45%-margin, capital-light vehicle-history franchise candidate whose position
  against its one direct substitute (Experian's AutoCheck) is measured in no filing and whose only unit
  disclosures are a frozen dealer floor and a report-view figure that fell, with B2B and Listings carrying
  no franchise; **price US$20.16 × 294,821,320 = US$5,943.6M; standalone owner earnings ~$280-350M, a
  4.7-5.9% yield against a 5.35% Treasury, needing ~4-5% perpetual growth to reach the 10% floor —
  COMPUTATION ONLY. PASS/FAIL: FAIL, closed at Q2.**
- **If UNKNOWABLE — what specifically cannot be known:** whether CARFAX's price-led growth is taken from a
  position AutoCheck cannot erode or from a unit base that is quietly shrinking. **Reopened by:** a defined
  CARFAX unit and price/volume series in MBGL's FY2026 and FY2027 filings.
- **Non-verdict-moving work order:** artifact Experian plc Annual Report 2026 (customer-segment revenue) ·
  lives at experianplc.com · rung company IR · blocked by Incapsula bot protection.
