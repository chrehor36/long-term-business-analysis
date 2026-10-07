## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT, on the business); Q3-Q6 recorded beneath explicit
  RECORDED, NOT GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed revenue note
  FY2021-26 and the unit economics stated from it; the forecast revenue is excluded by name. Q3's IN is recorded and not
  governing.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned; the case for UNKNOWABLE at Q1 is recorded at full strength and
  not taken, with the reason.
- [x] Step 0: the skip reason reproduced and explained on the FY2022 10-K (an organic step on consecutive years and one
  element, 82% from onsemi); the entity checked (one corporation; the fiscal-year change of 2026-04-02 recorded); the
  filing read with accession numbers; OCF, SBC, capex, acquisition cash and revenue cross-checked to the FY2026 10-K face and
  FY2017-25 to the earlier faces.
- [x] Owner earnings on the five-year default and on three-year, ten-year, wave and pre-wave windows, both (c) ends and an
  acquisition-inclusive column; the working-capital increment itemized by year and shown not to have reversed; the windows
  that were not built (before FY2017) named with the reason.
- [x] Competitor row filled from three SEC filers' own 10-Ks (FORM, COHU, TER), each re-fetched and each figure found in the
  filer's text; the direct burn-in competitors named and shown to file nothing with the SEC; the class not PROVISIONAL,
  with the directional reason.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched directly; the cached
  09/17 row from `sources.sovereign()` recorded and not used.
- [x] Value stated as a range under COMPUTATION — NOT A CLEARANCE (no earning-power value; tangible equity about $6 a share).
- [x] One bar (the screamer test); windage count zero, stated.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, the series corroborated by two Form 4 withholding prices
  (2026-09-01 and 2026-09-03) that equal the aggregator's closes.
- [x] Share count from the FY2026 10-K cover with its accession, the latest periodic filing; nothing sold after the cover
  date found; dilution shown beside the cap.
- [x] Deal check run on EDGAR: none live.
- [x] Run committed after Step 0, after Q1-Q2, and after Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this session wrote (the template's headings and the required `COMPUTATION — NOT A
  CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded 10-K, 10-Q, 8-K, proxy and prospectus texts, the peers' 10-Ks and
  companyfacts, and `companyfacts.json` were left out of every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q2 was committed (`17882a0`) saying the company names no competitor anywhere.** Reading the litigation note for Q3
   found Suzhou Semight Instruments, a Chinese maker of wafer burn-in systems against which Aehr's infringement claims were
   dismissed at first instance in December 2025. Q2 was amended in the Q3-Q6 commit to add it (a named rival, the patents
   *"upholds part of the claims"*, the attacker already in the field); the verdict did not change, and the amendment
   strengthens it. History kept.
2. **Step 0, corrected before its commit:** a stray draft fragment in the D&A reclassification sentence; the August insider
   sale range (first written as $127.50 to $143.77; the parsed Form 4s give $100.70 to $143.77).
3. **Step 0, corrected in the Q1-Q2 commit:** "no 10-K/A in the 1,005-row index" did not say the index begins 2018-08-20;
   EDGAR full-text search finds 10-K/As for FY2005 and FY2008 only, and the sentence now says so.
4. **Q1-Q2, corrected before commit:** the FY2021 customer names were first attributed to the FY2021 10-K (they are quoted
   from the FY2022 10-K); the inventory build was first written as $36.5M (the faces give $29.9M for FY2022-24); a draft
   said the 82% buyer had left the 10% list, which the filings do not show, because the 10-K names no customer after FY2022.
5. **Q4, corrected before commit:** stock sold for cash over ten years was first $144M (the FY2017 private placement of
   $5.3M was missing; $149M); *"SBC exceeded operating cash in every positive year but one"* (two of three); revenue
   without Incal $40M (it is $39M).
6. **Tooling friction, not an error:** re-running the flattener on already-flattened files made `.flat.flat.txt` copies;
   deleted, never committed.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **"settle on the 10-K competition section, which names them" (section 3): it names nobody.** No Aehr 10-K FY2019-26 names
   a competitor in its competition section; the only rival named anywhere is Semight, in the litigation note. Advantest,
   Teradyne, FormFactor and Cohu are named in no Aehr filing read; EDGAR full-text search shows FormFactor named Aehr in its
   FY2008-12 10-Ks only, and Cohu and Teradyne never.
2. **"Fiscal year ends on the last Friday of May" (section 1)** is the Friday *nearest* May 31 (52- or 53-week year), and **it
   is changing**: from FY2027 the year ends on the Friday nearest June 30 (board approval 2026-04-02; FY2027 runs 2026-06-27
   to 2027-06-25), leaving a four-week transition period no filing yet covers. `submissions.json` also gives
   `fiscalYearEnd` 1231, which no filing supports.
3. **Tagged D&A "0.31 (FY2022)" (section 2)** is the earliest vintage; the FY2024 10-K face restates FY2022 D&A to $356K.
   The screen's `da_annual` also gives FY2024 $700K against the face's $657K (its source element was not traced).
4. **The memory-sourced beliefs (section 3), settled:** SiC for EVs made FY2022-24 with onsemi the large customer: **held**
   (named at 82% for FY2022; 79% and 67% unnamed for FY2023-24; EV and power 92% at the peak). Incal bought in FY2025,
   package-level: **held** ($22.2M, closed 2024-07-31, $18.6M revenue in its first ten months). FY2024 valuation-allowance
   release: **held** ($21.9M; pretax $12.5M against net income $33.2M). New markets AI, HDD, GaN, silicon photonics:
   **held in the releases and business section**; package-level revenue (Sonoma, Tahoe, Echo) is 37% of FY2026
   revenue and the July 2026 release ties Sonoma orders to a hyperscale AI customer; the rest is forecast and was kept
   outside the circle. Erickson CEO: **held** (since January 2012). ATM
   programmes: **held**, four of them ($25M 2021, $25M 2023, $40M 2024, $60M 2026) plus a 2017 offering. Competitors
   Advantest, Teradyne, FormFactor, Cohu: **not named by Aehr** (defect 1).
5. **The brief did not know** about the December 2024 guidance class action (voluntarily dismissed 2025-05-16), the
   metric switch in FY2025 guidance from "net profit before taxes" to "non-GAAP net profit before taxes", the Semight
   litigation, or the fiscal-year change; each is in the file.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.sovereign()` served the cached 09/17 row** at 20:41 EDT while the Treasury had published 09/18: the
  SNOW, TSLA, RIVN, DJT and BX note, reproduced a sixth time.
- **`sources._chart()` returned `close None` for the day's bar** after the close, as at BX; `regularMarketPrice` with its
  `regularMarketTime` carried the closing print.
- **`submissions.json` `fiscalYearEnd` can be wrong** (1231 for a May filer); any tool that reads it to align years would
  misplace AEHR's.
- **`scale_shift` cannot tell a one-customer capacity build from a business step.** Only the customer-concentration note
  shows that the FY2022 step was 82% one buyer; a screen could read `ConcentrationRiskPercentage1` where tagged; not built.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A consumable is only an annuity if the installed base keeps producing.** Aehr's per-device contactors looked like the
razor-blade half of a franchise; the filed record shows them falling 60% in two years when one customer's end market
slowed. Read the consumable line through a customer's cycle before calling it recurring.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)**, at Q2. [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** AEHR CLOSES AT Q2 (OUT, ON THE BUSINESS, [E3-03] criterion 2, with [E2-44], [E4-37], [E3-46], [E4-04],
  [E3-51], [E4-23]): the FY2026 10-K says customers *"build their own burn-in systems"* or buy from *"captive or affiliated
  suppliers"* and that competitors are developing *"full-wafer and single-touchdown probe cards"*; it says a price rise to
  recover costs *"could result in a decrease in the competitiveness of our products"* while gross margin fell from 49.1% to
  35.3% (FY2024-26); the only rival it names, Semight, had Aehr's infringement claims dismissed at first instance (December 2025); the
  consumable contactor line fell 60% in two years as EV and power revenue went from 92% to 17%; the largest customer went
  from 82% (onsemi, FY2022) to 26%; on a three-filer row (FORM, COHU, TER) re-read from each 10-K, the subject has the
  steepest margin fall and the only negative five-year owner cash. Q1 IN (systems, per-device contactors and service; the AI
  and HBM forecast revenue outside the circle). Q3 recorded IN on the binary (the guidance class action voluntarily
  dismissed) with four converging flags: guidance missed by 34% (FY2024) and withdrawn (FY2025), serial issuance (2.4 times
  in ten years), non-GAAP net income before stock pay as the headline, and the FY2025 target switched to non-GAAP as results
  fell; pay vests on revenue; insiders sold about $61M in fifteen months. Q4 recorded OUT (gruesome: owner earnings
  five-year FY2022-26 **-$4.8M to -$8.0M** a year, positive only in FY2023; survival bought with $97.4M of FY2026 stock
  sales; proposed shape #20 THE WAVE with #8's feature); price $93.49 x 32,620,450 = $3,049.7M, headed COMPUTATION — NOT A
  CLEARANCE: yield about -0.2% against 5.34% and a ~10% floor, price about fifteen times tangible equity; Q6 records the
  reversal condition in words and arms nothing.
- **The skip reason, as it turned out:** a real organic revenue step (FY2021 $16.6M to FY2022 $50.8M, consecutive years,
  one element), made by one customer's silicon-carbide capacity build (onsemi 82%); not a perimeter change and not a
  restatement.
