## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT); Q3-Q6 recorded beneath explicit RECORDED, NOT
  GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed statements
  and is scoped in writing to the business the filings show; the AI and robot businesses are recorded as outside
  the circle, not as a provisional IN. The energy segment's position is PROVISIONAL at Q2, and Q2 is OUT on the car
  business, which the provisional part cannot rescue.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned. One document is named as a work order for any future
  upgrade only: BYD's 2025 annual report on HKEXnews (not re-attempted; the TM run recorded the obstacle).
- [x] Step 0: the filing was read with accession numbers; OCF, SBC and capex cross-checked to the FY2025 10-K face;
  the one tagged series that does not match the face (D&A) named and handled at Q4.
- [x] Owner earnings on the five-year default window and a three-year window, both (c) ends, TTM shown; SBC made
  complete with the capitalised part; working capital read from the face; (c) disclosed as a judgment inside the band.
- [x] Competitor row filled: nine peers named, five complete from SEC filings via the TM run's accessioned row with
  every Tesla figure recomputed here; gaps stated (BYD blocked; CATL, Sungrow, Wärtsilä unpulled for energy).
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched uncached.
- [x] Value stated as a round-number range under a COMPUTATION — NOT A CLEARANCE heading.
- [x] One bar (the screamer test); windage count one.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, corroborated by a Form 4.
- [x] Run committed after Step 0, Q1, Q2 and Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this session wrote (the template's own headings and the required
  `COMPUTATION — NOT A CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q2, corrected before commit:** the first draft of the "Tesla less regulatory credits" row carried wrong margins
   (9.40 / 14.58 / 7.34 / 4.42 / 2.49, pooled 7.30); recomputed from the stated numerators and denominators they are
   9.66 / 14.91 / 7.48 / 4.54 / 2.54, pooled 7.40, and the text now uses those.
2. **Q2, corrected before commit:** a draft said Tesla less credits was below every volume maker in FY2025 except
   those in charge years; GM's GAAP 1.57% and VW's 1.8% are below its 2.54%, and the sentence now names who is above
   and who is below.
3. **Q2, corrected before commit:** a draft put idle capacity at "about 30%" from the Q2 2026 capacity table against
   FY2025 deliveries; the price cuts were made in FY2023-25, so the capacity figure now comes from the Q4 2023 Update
   (about 2.35 million) and the idle share is stated as a quarter to a third (76% and 70% utilisation).
4. **Q1, corrected before commit:** a draft said 97% or more of revenue came from the car and battery mechanism; the
   filed figure is 86.8% for automotive plus energy, with services and other (13.2%) sold to the same fleet.
5. **Q3, corrected before commit:** a draft set the pay plan's $400bn Adjusted EBITDA against "$16.3bn TTM"; the four
   latest quarters in the Update sum to $15.3bn. A draft said the 10-K does not use EBITDA; it uses it 11 times, all in
   the pay-award note. A draft put the CEO's share of issuance at 18% of the 2021 base; it is 23%.
6. **Committed 33 JPEG slide images** of the Q2 2026 Update (`8k/q2_2026_deck/*.jpg`, about 3.9 MB) in the Q2 commit
   `251f6f1`. The deck's text layer (`exhibit991.htm.txt`) was what the run used; the images are re-fetchable from
   EDGAR and should not have been committed. `.gitignore` covers `.htm`, `.html`, `.pdf` and `.xlsx` in research
   folders but not `.jpg`. **History is not rewritten**; a tooling note below.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **"Pull ... the proxy"**: there is no 2026 proxy statement. The FY2025 Part III was filed as a **10-K/A**
   (`0001104659-26-053166`, 2026-04-30), whose explanatory note says the original 10-K omitted Items 10-14; the latest
   DEF 14A is 2025-09-17 (`0001104659-25-090866`, for the 2025-11-06 meeting). Both were used.
2. **"Check any large `share_count_shift` against the split feed first"**: held and worth doing, but the answer at
   TSLA is that the shift (1.23x) was **not** a split (both splits sit before the older observation) and **not** the
   guard that fired; it is the CEO's awards, 10.7% of the cover count unearned.
3. **The SNOW register discrepancy (104 counted vs 103 stated)**: **not reproduced.** Counting line-start
   `- **TICKER (` entries from the heading line `## COMPLETED FROM THE QUEUE` to `## THE WRITE-EARLY PROTOCOL` gives
   **103, no duplicate ticker**, so SNOW's "103" was right and TSLA is **104**. Two looser counts give 105, not 104:
   slicing from the phrase's first occurrence (the trap the 2026-09-13 resume note records), and matching `- **X (`
   anywhere in a line, which picks up two unit series in prose (*"- **806 (2018)**"* and *"- **600 (2025)**"*). No
   count tried gives 104.
4. **"`restatement_shift` cannot have fired"** (from the SNOW note): held; the TSLA guard was `scale_shift`, as at
   SNOW, but for a different reason (a tag hole, not an organic step).

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`scale_shift` at `a8bc84f` compares non-consecutive years when the first element read has a hole.** Tesla's
  `RevenueFromContractWithCustomerExcludingAssessedTax` skips FY2019-20, so FY2018 sat beside FY2021 as a "one-year"
  step of 2.51x. The current screen reads the union of elements and returns 1.71x; any other name re-triaged from the
  old code could carry the same false step. A guard that also required the two period ends to be about a year apart
  would have refused the pair.
- **`share_count_shift` reads the legal cover count, which includes unearned restricted stock**: Tesla's cover
  carries 423.7M shares that basic EPS excludes. Any cap built on the dei element for a filer with issued-but-unearned
  performance shares is overstated by that block.
- **`tools/sources.sovereign()` served the cached 09/17 row at 18:41 EDT** while the Treasury had published 09/18
  (5.34%): the SNOW run's note, reproduced.
- **`.gitignore` does not cover `.jpg`** in research folders; image-only 8-K exhibits (Tesla's Updates) will slip
  through the same way.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A five-year pooled margin can be two years of wave and three of sand.** Tesla's 9.54% leads the automaker row and
looks like a moat; year by year it is 16.8% in the supply-tight year and 4.6% three years later, below Toyota, with
46% of the last year's operating income paid by a regulator. Read the pool one year at a time, and take the credits
out, before a row-leading average is allowed to argue for a franchise.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** TSLA FAILS AT Q2 (OUT, on [E3-03] criterion (2) not shown and contradicted in its own 10-Ks:
  *"extremely competitive markets"*, competitors with *"significantly more or better-established resources"*, and
  three years of lower revenue per car explained by *"price reductions"* and *"attractive financing options"* with a
  quarter to a third of installed capacity idle [E2-58, E2-44]; the row-leading five-year margin (9.54%) was a
  supply-tight lead, 16.8% in FY2022 to 4.6% in FY2025 and 2.6% in H1 2026, below Toyota and Hyundai [E3-46, E4-32];
  46% of FY2025 operating income from regulatory credits being withdrawn [E2-59]; buying its replacement platform
  [E4-04, E5-23]; the plan requires one manager per the board [E4-23]). Q1 IN on the business the filings show, the
  AI and robot businesses outside the circle; Q3 IN on the binary (recorded; gate case; [E3-50] and [E4-29] in the pay
  contract, [E5-15], [E4-22], an [E3-40] prompt on the xAI/SpaceX investment; the 2018 SEC settlement carried to the
  operator); Q4 IN on survival, gruesome on the FY2022-25 record, five-year owner earnings $3.1bn to $8.2bn (recorded;
  shape #11 with #14's feature); price $364.27 x 3,949,547,394 = $1.44tn legal, $1.28tn economic, headed COMPUTATION —
  NOT A CLEARANCE: yield 0.2-0.6% against 5.34%, $128bn of owner earnings needed for the floor; Q6 arms nothing.
- Work order: none for this verdict. UNKNOWABLE: none.
