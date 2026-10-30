## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT); Q3-Q6 recorded beneath explicit RECORDED, NOT
  GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed statements and
  is scoped in writing to the business the filings show; R2 as a profit case, the robotaxi programme, Autonomy+, Mind
  Robotics and Also are recorded as outside the circle, not as a provisional IN. The software-and-services position is
  PROVISIONAL at Q2, and Q2 is OUT on the automotive business, which the provisional part cannot rescue.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned. One document is named as a work order for any future upgrade
  only: BYD's 2025 annual report on HKEXnews (not re-attempted; the TM run recorded the obstacle).
- [x] Step 0: the filing was read with accession numbers; OCF, SBC, capex and D&A cross-checked to the FY2025 10-K face;
  SBC shown complete on the face by the MD&A's line allocation; the skip reason reproduced and explained on the filings.
- [x] Owner earnings on the five-year default window, a three-year window and TTM, both (c) ends; no ten-year window
  exists and that is said; the contract-liability line shown both ways; D&A's composition and both flagged steps
  explained; (c) disclosed as a judgment in the [E5-20] class.
- [x] Competitor row filled: eleven peers named, seven complete from SEC filings (Rivian, Lucid, Ford's Model e
  segment, Tesla, GM and Ford recomputed from their own faces; Toyota, Stellantis and Honda carried from the TM run's
  accessioned row and labelled as not recomputed); Volkswagen and Hyundai carried from that row in the text only; BYD
  named and not pulled.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched uncached.
- [x] Value stated as a range (negative at both ends) under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count none spent.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, corroborated by two Form 4s.
- [x] Share count from the Q2 2026 10-Q cover with its accession; the two classes summed only after the charter terms
  (as Note 14 states them) were read; converts, awards, VW and Uber instruments considered and stated either way.
- [x] Deal check run on EDGAR: no merger, tender or going-private filing; two 8-K Item 1.01s opened (Uber, DOE).
- [x] Run committed after Step 0, Q1, Q2 and Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written, and the [E3-70]
  quotation was replaced with the ledger's own text when a first draft carried the framework's paraphrase in quote marks.
- [x] No em dashes in anything this session wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded filings (10-K, 10-Q, DEF 14A text, Lucid 10-Ks, 8-K exhibits) and the
  1.1 MB `companyfacts.json` were left out of every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q1 and Q2, corrected before the Q2 commit:** a draft set FY2025 production against the 215,000-unit capacity
   (about 20% utilisation). That capacity arrived with the 2025 paint-shop upgrade for R2; the FY2023 and FY2024 10-Ks
   state *"up to 150,000 vehicles annually"*, so the utilisation is 38%, 33% and 28% (FY2023-25). Q1 was corrected in the
   run file after its own commit (`35cfec9`) and the corrected text went in with the Q2 commit.
2. **Q1 (after its own commit, fixed in the Q2 commit) and Q2 (before commit):** a draft said the bank lease channel *"passed the federal 45W credit to
   drivers"*. No filing read says so; the text now says only what the 10-K says, that deliveries fell *"due in part to
   the expiration of 45W tax credits"*, and the credit's size comes from the FY2024 10-K (*"between $7,500 and
   $40,000"*), replacing a $7,500 figure from memory.
3. **Q2, corrected before commit:** a draft said every profitable maker in the row has a combustion business; Tesla
   sells only battery vehicles and is profitable at about 1.64 million units. The sentence now says every profitable
   maker is a volume maker.
4. **Q2, corrected before commit:** a draft put Volkswagen's equity purchases at $2,745M; the filed steps are a $1,000M
   note converted in December 2024, $750M in June 2025 and $1,000M in April 2026, about $2.75bn, and the text says that.
5. **Q3, corrected before commit:** the FY2023 10-K cover count was mis-summed (976,449,611 for 977,449,611); the
   derivative suits were counted as seven (the filings show ten); the guidance scorecard's summary line was rewritten
   to match its own table; and the [E3-70] line carried framework prose in quotation marks (fixed, item above).
6. **Q5, corrected before commit:** the new shares needed a year were put at 17-18% of the count (16-18% on the
   arithmetic), and the swing to the floor was attributed to the five-year means when its low end is the TTM figure.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The register-counting instruction gives the wrong number.** The brief says to count entries under `## COMPLETED
   FROM THE QUEUE` *"stopping at the next `##`/`###` heading"*. The next such heading is `### REGISTER BACKFILL
   2026-09-13`, which holds ten entries (GM, F, OXY, AEO, KR, NKE, PLAB, CVX, HHH, GHC); stopping there gives **94**. The
   TSLA fold's 104 counts to `## THE WRITE-EARLY PROTOCOL`, which includes the backfill. Counted that way, with no
   duplicate ticker, RIVN is **105**.
2. **"a Q2 2026 10-Q exists"** and the DEI public-float date: held (filed 2026-07-30, `0001874178-26-000054`). But the
   brief's framing of the count as a dei problem missed that **the cover already includes a July 2026 offering of
   86.25M shares** made after the quarter's balance sheet (1,362M at June 30).
3. **The "unverified beliefs" list, settled:** IPO November 2021: **held** (176M shares at $78.00, FY2021 10-K;
   424B4 `0001193125-21-328239`). Class A and B with a founder-held super-voting class: **held**, and the Class B
   **converts automatically in November 2026** (the five-year anniversary), which the brief did not have. Amazon as a
   large holder and EDV launch customer with a lapsed exclusivity: **held in substance** (12.9%, 2026 proxy); the
   exclusivity was *amended* in November 2023, not simply lapsed, and fees to Amazon on third-party van sales run five and
   ten years from 2024-01-01. VW joint venture of June 2024 with up to about $5.8bn: **partly held**; the JV entity was
   established in **November 2024** (FY2025 10-K Note 19; the June 2024 8-K, `0001193125-24-167944`, Items 1.01, 2.03 and
   3.02, is in the index and was not opened), the filed consideration is a $1,295M licence, a $250M milestone, $210M at start of production,
   equity tranches and a $1,000M loan, and VW now holds 15.9%; this run did not reconcile the total to $5.8bn. DOE loan of
   about $6.6bn: **not settled for January 2025** (the 8-K of 2025-01-16 was not opened), **and superseded**: the
   amended agreement of April 2026 sets **$3,355M plus $315M and
   $651M plus $179M** (about $4.5bn with capitalised interest), undrawn and conditional on positive gross margin.
   Regulatory credits material and gross profit positive around Q4 2024: **held** (Q4 2024 gross profit $170M); but the
   FY2025 positive gross profit is the VW work, not credits. R2 at Normal in 2026: **held** (external deliveries from
   2026-06-09). Securities class actions over the IPO: **held** (settled for $250M, judgment May 2026), plus a second,
   open action from 2024. Large CEO performance award: **held, and it was repriced** (2025 CEO Award, above). Adjusted
   EBITDA headlining: **held**.
4. **"Class B with super-voting rights"**: the voting ratio was not needed and was not read; the 10-Q states the classes
   differ only in voting and conversion, which is what the count needed.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`share_count_shift` returns None when companyfacts carries no dei count**, and the triage reads None as a pass.
  Rivian's count rose 16.7% in six months and 61% in four years without any guard seeing it. A None here means "not
  measured"; a screen could say so in words rather than pass silently.
- **`working_capital_flag` read the FY2024 contract-liability line correctly** and is the reason the Volkswagen
  prepayment was found; its limit (annual facts only) did not bite, because the unwinding shows in the H1 2026 10-Q face.
- **`tools/sources.sovereign()` served the cached 09/17 row at 19:12 EDT** while the Treasury had published 09/18
  (5.34%): the SNOW and TSLA note, reproduced a third time.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A first positive gross profit can be a partner's prepayment.** Rivian's FY2025 consolidated gross profit ($144M)
and about half of its FY2024 improvement in operating cash came from Volkswagen paying in advance for engineering work
that ends in 2028; the vehicles still lost money. Read the segment note and the deferred-revenue line before a
"turned gross-profit positive" headline is allowed to argue for a business.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** RIVN FAILS AT Q2 (OUT, on [E3-03] criterion (2) not shown and contradicted in its own 10-K: *"highly
  competitive"*, competitors with *"significantly greater financial, technical, manufacturing, marketing, or other
  resources"*; deliveries fell 18% in FY2025, *"due in part to the expiration of 45W tax credits"*, after three flat
  years; no return on capital in any year (pre-tax ROCE -117%, -86%, -70% FY2023-25) and no filer in an eleven-peer row
  showing a battery-vehicle business earning a return at this scale (Lucid -258.7%, Ford Model e -67.1%, Rivian -66.5%
  operating margin in FY2025) [E3-46, E3-43]; both legs of [E2-44] and [E4-37] fail; credits and manufacturing tax
  credits administered by governments [E2-59]; a platform replaced every two to three years [E4-04, E5-23]; the 10-K says
  the plan depends on the founder [E4-23]). Q1 IN on the business the filings show, with R2's profit case, the Uber
  robotaxi programme, Mind Robotics and Also outside the circle; Q3 IN on the binary (recorded; gate case; [E2-49] and
  [E3-50] in the repriced 2025 CEO award, a $350M upward adjustment to the bonus FCF yardstick, [E5-15] +61% shares in
  four years, [E4-29], [E4-22] with a mixed guidance record); Q4 OUT (recorded; gruesome; five-year owner earnings
  $(5,177)M capex end to $(4,489)M D&A end, negative at every window and end; the FY2024 Volkswagen prepayment is not
  float; shape #8 with #14's feature); price $14.99 x 1,447,860,630 = $21.7bn, headed COMPUTATION — NOT A CLEARANCE:
  yield about -16% to -24% against 5.34%; Q6 arms nothing.
- Work order: none for this verdict. UNKNOWABLE: none.
