## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. The file closed at Q2 (OUT); Q3-Q6 are labelled RECORDED, NOT
      GOVERNING in every heading and verdict line.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed order, GOV and Net
      Revenue Margin series, FY2020-H1 2026; the excluded parts (autonomy, AI, grocery and international futures) are named as
      outside the circle, not as caveats on the IN.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (Q3: the D.C. Superior Court complaint and consent
      judgment in *District of Columbia v. DoorDash*, and the 2019 internal record; recorded, not governing).
- [x] Every UNKNOWABLE verdict states what cannot be known (Q4: the next five years' operating cash of a business whose
      industry the filer calls "nascent"; the range -$801M to +$1,093M is too wide [E4-25]).
- [x] Step 0: the filing was read, with accession numbers; operating cash, stock pay, D&A, both capital lines and revenue
      cross-checked against the FY2025 and FY2022 10-K faces; the cover count cross-checked against the 10-Q balance sheet
      and equity statement.
- [x] Owner earnings on multi-year means (five and three years, plus TTM); windows stated; (c) disclosed as a judgment with
      both ends; stock pay subtracted in full, capitalised stock pay added to (c), grant value shown [E3-70].
- [x] Competitor row filled from three SEC filers' own filings (DASH, UBER Delivery, CART) plus Deliveroo through DASH's own
      Note 4; the non-SEC competitors named and the reason the class is not held PROVISIONAL stated.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury par yield curve), dated 09/18/2026;
      `sources.sovereign()` stale and not used.
- [x] Value stated as a round-number range (about $0-10bn no-growth at the floor), and only as a COMPUTATION - NOT A CLEARANCE.
- [x] One bar chosen, not both: none, because Q5 did not open; windage count zero.
- [x] Prices dated; aggregator (Yahoo) used for the live quote only, flagged, corroborated by three Form 4s.
- [x] Run committed to git (template `e30b2f8`, Step 0 `2d30b95`, Q1-Q2 `3bcaa7b`, Q3-Q6 with audit and register in the next
      commit, fold after).

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **A commit failed on a relative path** (the Step 0 commit ran `git commit` from the wrong directory). Nothing was
   committed wrongly; the commit was re-run with absolute pathspecs and contains only this run's files.
2. **A web search summary offered a checkout quotation** about tips that is **not in the Assurance of Discontinuance** this
   run read. It was not used; only text found in `NYAG_AOD_2025.txt` is quoted.
3. **Two quotations from the DEF 14C were first cut mid-clause** and a revolver line first described the facility as $800M,
   the pre-amendment figure. All three were corrected against the documents before the Q3-Q6 text entered the run file
   (the revolver is $2.0bn from 2026-08-05, 10-Q Part II Item 5).
4. **A first guess at the attorneys' general URLs returned 404**; the AOD was then found on the NY AG's own server. The D.C.
   matter was not fetched and stands as the Q3 work order rather than being described from memory.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
- None that changed a number. The brief told the run to verify the Deliveroo and SevenRooms deals from filings rather than
  take them as fact; both are confirmed (Note 4), and a third 2025 acquisition (Symbiosys) was found in the tax note. The brief
  did not know of the **Nevada reincorporation effective on the run date**, which changes which charter governs the class
  treatment; the run read the new articles rather than the Delaware certificate the brief implied.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`sources.sovereign("USD")` served the cached 09/17 row (5.29%) again**; the eighth recorded occurrence across runs.
- **`acquisition_flag` misreads FY2025**: it reports a *"NET CASH INFLOW on the acquisition line ($4,222M ...)"* where the face
  shows an outflow of $4,151M. Not investigated further; the face was used.
- **`working_capital_flag` returned None** although the accrued-liabilities line moved by 44% of operating cash in FY2024
  ($943M of $2,132M); it reads specific tags and may not reach this filer's line. A prompt for the operator, not a fix.
- **`cover_shares.py` was not needed**: the three dimensioned dei facts were read directly from the inline XBRL (`dei.py`).
  The C class is tagged `ixt:fixed-zero` over the word "no"; any parser that expects a number there should expect that.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A rising take rate is not pricing power until the filer says why it rose.** DoorDash's Net Revenue Margin rose from 11.7%
to 13.4% while orders nearly tripled, which reads at a glance as [E2-44]'s price-with-volume. The filer's own explanation in
three consecutive 10-Ks is logistics efficiency and advertising, and because revenue is reported **net of courier pay**, a
cheaper delivery raises the margin with no change in any price. For any net-revenue marketplace, read the MD&A's stated
driver of the take rate before scoring it at Q2.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- **One line:** DASH FAILS at Q2 (OUT, on the business): criterion (2) of [E3-03] fails in the company's own words
  (*"It is relatively easy to switch between offerings in our industry"*; all three sides multi-home; competition *"led us
  ... to change our commission rates and fees"*), in the largest peer's 10-K (Uber names DoorDash, *"low switching costs"*,
  $90.9bn of delivery bookings), and in the price series (margin gains from efficiency and advertising, growth bought with
  lower DashPass fees); [E4-04] fails because every side is held by payment renewed each order; criterion (3) is capped by
  minimum-pay and commission rules. Price US$192.94 (2026-09-18 close); 433,295,654 shares (A+B+C, Q2 2026 10-Q cover
  `0001792789-26-000050`); cap US$83.60bn; sovereign 5.34% (US Treasury, 09/18/2026). Q3-Q6 recorded, not governing: Q3
  UNRESEARCHED on the binary (NY AG AOD 25-007 read; D.C. matter the work order), Q4 UNKNOWABLE (owner earnings -$801M to
  +$1,093M across windows and ends), Q5 computation only (yield 0.02-1.31% against 5.34% and a ~10% floor).
- **If UNRESEARCHED - THE WORK ORDER:** not applicable to the governing verdict.
- **If UNKNOWABLE:** not applicable to the governing verdict.
