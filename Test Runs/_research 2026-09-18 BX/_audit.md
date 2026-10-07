
---
## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT, on the business); Q3-Q6 recorded beneath explicit
  RECORDED, NOT GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed segment note
  and the company's own GAAP-to-DE bridge, FY2020-25. Q3's and Q4's INs are recorded and not governing.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned; the case for UNKNOWABLE at Q1 is recorded at full strength and
  not taken, with the reason.
- [x] Step 0: the skip reason reproduced and explained on the face of the FY2022 10-K statement of operations (unrealized
  performance allocations and principal investment income); the entity checked across the 2019 conversion and the 2021
  rename; the filing read with accession numbers; OCF, SBC, capex and revenue cross-checked to the FY2025 10-K face; the
  FY2020-22 faces read from the FY2022 10-K and matched to companyfacts.
- [x] Owner earnings on the five-year default window and on three-year, six-year and TTM windows, both (c) ends and two
  constructions; the consolidated funds stripped by the company's own line and bracketed at the cash level; the three
  sources of cash separated with the ledger ids that govern their treatment [E2-23, E4-41, E4-25, E5-06]; the windows
  that do not exist (before FY2020) named with the reason.
- [x] Competitor row filled from nine peers' own FY2025 10-Ks, each re-fetched from EDGAR by this run and each figure
  found in the filer's own text (`peers/verify.py`); the foreign managers named and shown to be directionally unable to
  reverse the finding.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched directly; the
  cached 09/17 row from `sources.sovereign()` recorded and not used.
- [x] Value stated as a range under COMPUTATION — NOT A CLEARANCE ($27-42 a share at the floor with no growth, $56-87
  with 5% perpetual growth).
- [x] One bar (the screamer test); windage count one, stated.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, corroborated by a same-day Form 4.
- [x] Share count from the Q2 2026 10-Q cover with its accession, and the economic count (with Holdings units) from the
  same 10-Q's Note 13, the cap shown on both and the yield's choice stated; the wrong pairing shown so it is not repeated.
- [x] Deal check run on EDGAR: none live; the Item 1.01 8-Ks are financing.
- [x] Run committed after Step 0, Q1, Q2 and Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this session wrote (the template's headings and the required `COMPUTATION — NOT A
  CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded 10-K/10-Q texts, the peers' 10-Ks, the SEC order PDF and press release,
  and `companyfacts.json` were left out of every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **A commit ran after a failed edit.** The Q2 commit `5b58f32` was chained after a Python edit whose assertion failed;
   the commit still ran, carrying the uncorrected research copy `_q2.md` and a run file without Q2. Corrected in
   `9e6d3f2`, which put Q2 into the run file with the row positions restated; history kept. The lesson: chain a commit
   only on the edit's success.
2. **Q1, corrected before the run-file commit:** a draft gave FY2020's net-realizations share of Total Segment DE as 43%;
   the filed figures give 36% ($1,310.6M of $3,680.6M), and the text says 36%.
3. **Q1, removed:** a draft said the marks had *"a Level 3 input set behind most of them"*; this run did not read the
   fair-value hierarchy table, so the clause was deleted.
4. **Q2, corrected in `9e6d3f2`:** a draft said BX was the slowest-growing alternative manager *"except Carlyle"* over
   FY2023-25 while KKR's FY2023 base had not been read, and that five peers grew faster; the text now gives both windows
   separately and six faster in FY2025. A draft note that Ares grew partly by acquisition was not checked on Ares's
   roll-forward and was removed from the table.
5. **Q3-Q4, corrected before commit:** the price-to-range multiple (1.4-4.6x, not 1.2-4.5x), the floor-growth span
   (6.7-7.9 points), *"rising every year"* for SBC (true in dollars, not as a share of OCF or DE), and a vehicle name
   (*"a BREIT-adjacent credit sleeve"*) that no filing read by this run carries.
6. **Tooling friction, not an error:** the first attempt to write Step 0 by bash heredoc failed on an apostrophe, as the
   brief warned; the section was written with the file tool instead.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **"FY2014-15 absent from the tag series" (section 2) is not what the probe output shows.** The current screen's `ocf()`
   in `_probe_screen_output.txt` carries FY2014 $1,655.0M and FY2015 $2,397.0M (listed at the end of the dictionary,
   out of date order, which is probably what was misread), and FY2014-15 SBC and capex are present too. Nothing is
   absent. No window this run used reaches those years (the conversion rule at Q4).
2. **"Read the proxy" (section 4) and "settle on the DEF 14A" (section 3): Blackstone files no proxy statement.** No DEF
   14A exists in the 1,726-filing index; as a controlled company whose common holders cannot nominate directors, it puts
   Part III (compensation, ownership, related parties) inside the 10-K. Read there.
3. **"Strip the consolidated funds out of operating cash using ... the consolidating schedules" (section 4):** the
   company publishes consolidating schedules for the **statement of financial condition only**, not for cash flows. The
   funds can be removed exactly at the income level (the company's *"Impact of Consolidation"* line) and only bracketed
   at the cash level (the NCI contribution and distribution lines also carry the operating partnerships' non-controlling
   holders). The run did both and said which is exact.
4. **The memory-sourced beliefs (section 3), settled:** GAAP revenue includes performance allocations and principal
   investment income, and 2021/2022 made the step and reversal: **held**, and it is the whole skip reason. Consolidated
   Blackstone Funds run through operating cash: **held**, but small (12% of assets; $457.1M Blackstone share), and the
   bigger distortion in OCF is the firm's own investment turnover. Conversion 2019-07-01 and rename 2021: **held**
   (2021-08-06). Economic count larger than common: **held** (1,243,813,031 against 750,625,114; Series I and II one
   share each). FRE margin 58.3% and fee rate 92.2bp (0.86%): **held**, re-read on BX's 10-K. Schwarzman chairman, CEO,
   co-founder with a large holding: **held** (231.9M units, no common stock); Gray president and COO: **held**; *"named
   successor"*: **not settled** on the filings read (the 10-K names him beside the co-founder, not as successor). BREIT
   limited redemptions late 2022 into 2023: **held** (proration from November 2022; $13.3bn of FY2023 outflows). High
   payout of DE: **held** (*"approximately 85%"*).
5. **The brief did not know about the UC Investments return support** (an 11.25% target return on $4.5bn backed by a
   $1.1bn pledge of Blackstone's own BREIT holdings, 2023), which is the sharpest single Q2 fact in the file, or the 2015
   SEC order (IA-4219), which is the one conduct matter on record.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`scale_shift` fires on mark-driven revenue.** A carry-earning manager's `Revenues` element includes unrealized
  performance allocations and principal marks, so the guard will return every such name unpriced in a strong or weak mark
  year. A screen could flag filers whose revenue carries an unrealized component (BX tags no
  `RevenueFromContractWithCustomer...` annual fact at all, `triage_repro_out.txt`); not built.
- **`owner_earnings()` for a fee manager includes investment turnover in OCF**: $1.9-5.1bn a year at BX. The screen's
  figure is construction A; the company's bridge gives B, 54% higher on five years. Only a reader sees which a filer is.
- **`tools/sources.sovereign()` served the cached 09/17 row** at 20:11 EDT while the Treasury had published 09/18: the
  SNOW, TSLA, RIVN and DJT note, reproduced a fifth time.
- **`sources._chart()` returned `close None` for the day's bar** after the close; `regularMarketPrice` with its
  `regularMarketTime` carried the closing print. Recorded so a later run does not read None as no trade.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**For an asset manager, "revenue" includes the marks and "operating cash" includes the balance sheet.** The skip label
here measured an accounting convention, not a business event; and owner earnings for a fee manager sit between two
constructions whose gap is the manager's own capital committed to its funds, which no filing splits into maintenance and
growth. State both, say which is exact, and carry the gap as the range.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)**, at Q2. [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** BX CLOSES AT Q2 (OUT, ON THE BUSINESS, [E3-03] criterion 2, with [E4-04], [E4-32], [E3-51], [E4-23]):
  the 10-K itself says competitors *"charge lower fees"* and investors ask it *"to decrease fees"*; BREIT prorated
  repurchases from November 2022 and Blackstone pledged $1.1bn of its own BREIT holdings behind an 11.25% target return
  to hold one subscriber; on a nine-filer row re-read from each 10-K, the largest firm is fourth of eight alternative
  managers on price (92.2bp) and second slowest on fee-earning growth (11.0% FY2025; 9.9% a year FY2023-25), its own fee
  rate drifting 0.88% to 0.83%; 14% of fee-earning capital had to be replaced in FY2025 alone. Q1 IN (fees on long-dated
  capital, realized carry less the employees' share, and a balance sheet beside the funds, separable on the company's own
  bridge). Q3 recorded IN on the binary (the 2015 SEC fee-disclosure order, remedied before contact) with [E4-29] ticked
  on pre-SBC headline measures and a controlled-company structure in which common holders elect no director; Q4 recorded
  IN (owner earnings five-year $3.3bn to $5.2bn a year, the gap being the firm's own fund commitments; #11 with #9's
  feature); price $124.96 x 1,243,813,031 economic shares = $155.4bn (common alone $93.8bn), headed COMPUTATION — NOT A
  CLEARANCE: yield 2.2-3.3% against 5.34% and a ~10% floor; Q6 records the reversal condition in words and arms nothing.
- **The skip reason, as it turned out:** unrealized marks in GAAP revenue (+$10.1bn FY2021, -$5.0bn FY2022), not a
  perimeter change and not a restatement.
