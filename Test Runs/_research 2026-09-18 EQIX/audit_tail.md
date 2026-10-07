
### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **DATED CORRECTION, 2026-09-18, to Step 0 (the price cross-check). Step 0 says *"EDGAR shows no
   Form 4 after 2026-08-06 with a transaction price in September"* and records the cross-check as a
   limit. That was written without querying the Forms 4, and it is wrong.** EDGAR, re-queried at the
   audit, carries Forms 4 of 2026-09-03 (`0001101239-26-000152`) and 2026-09-08
   (`0001101239-26-000153`), reporting person Michael Shane Paladin: open-market sales on
   **2026-09-02 at $1,008.0191 and $1,018.43**, and on **2026-09-04 at $1,035.01**. The Yahoo bars
   are 09-02 low $1,002.24 / high $1,025.61 and 09-04 low $1,031.26 / high $1,048.34. **All three
   filed prices sit inside the filed days' ranges: the aggregator series IS corroborated by a primary
   document, as at TOST.** Step 0 is left as written (operator rule 6); this note governs.
2. **Q4 draft arithmetic, corrected before commit.** The three-year, ten-year and TTM rows of the
   windows table and the per-share line were first written from a scaling I had not run; recomputed
   from `oe.py` before the section was committed. Nothing wrong reached a commit.
3. **A heredoc containing apostrophes failed** while writing Q2 (the environment limit the brief
   names); nothing was appended by the failed call, which was verified before the section was
   rewritten through a file.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **The five capex checks were framed as tag questions, and EQIX's problem was not a tag.** The
   current screen prices EQIX (no `CAPEX_UNRESOLVED`); the defects are (i) the same element holding
   different values in FY2010-13, where `annual()` kept the real-estate figure and dropped the plant
   figure, and (ii) **a second capital line on the face, "Real estate acquisitions", that no
   `CAPX_TAGS` element reaches** ($994M in FY2025). "Check whether overlapping capex tags carry
   different values" would not have found (ii); reading the face of the statement did.
2. **The short-seller characterisation is the brief's, not the filings'.** The brief says the 2024
   report was *"about AFFO and maintenance capex"*. No Equinix filing names the allegations beyond
   *"certain allegations related to components of our operating results and other strategic
   matters"*, and the report itself is not a filing. Recorded as unverified at Q3; the (c) judgment
   was made on the filed capex record, independently of what the report said.
3. **The brief's hypothesis that the company's recurring capex is "ITS definition of maintenance"
   was right, and the brief under-stated how far it sits from the corpus's**: 11-17% of D&A for ten
   years, the lowest ratio in the filed row (Digital Realty's is 18-20%), justified until October
   2025 by a sentence the company then withdrew.
4. **The brief did not anticipate the [E5-20] exception class applying.** It listed the six prior
   names and that the class had applied at AMZN alone; here it applies (shortened lives, project cost
   per cabinet doubled, old buildings short of power).
5. **The REIT routing note** pointed at a sector method that does not exist; the brief said so and
   was right. Recorded at Step 0.
6. **The "SKIPPED WITH A REASON" section of the queue** says of this row *"the only available
   construction is the D&A end and the corpus calls it INVALID for this class"*. For EQIX today both
   ends price on the screen; what is wrong is the capex end's completeness, not its availability.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.price()` returns an intraday `regularMarketPrice` stamped with today's date** while
  its docstring says *"Latest close."* Reproduced on a second name (TOST, then EQIX at 17:40 UTC).
- **`floor_screen.CAPX_TAGS` does not reach `PaymentsToAcquireRealEstate`.** For a filer that splits
  real estate from other plant on the face (EQIX; possibly every data-centre REIT, DLR next in the
  queue), the capex end omits a real capital line. Adding the element would change a number, so it
  is a proposal for the operator, not a fix made here.
- **`floor_screen.annual()` keeps one value where one element carries several for the same year**
  (EQIX FY2012: $24.7M and $1,098.6M), and here kept the wrong one. Harmless inside five years;
  wrong for any longer window.
- **`capital_acquired()` adds non-cash finance-lease additions** where the cash cost is the lease
  principal in financing; the two differ ($236M against $155M in FY2025). A judgment, disclosed.
- **`sbc_annual()` max-rule** picks $311.0M for FY2020 against $295.0M on the face (the ARM-type
  limit in the resume note). Conservative in direction.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**Price the company's maintenance claim against its own construction table.** Equinix publishes,
every year, the capex and sellable cabinets of each project under construction. Dividing one by the
other ($58.7k per cabinet in FY2020, $126.2k in FY2025) against the book cost per cabinet ($80.0k)
turned an argument about "recurring" capex into an observed replacement cost, from the filer's own
page. Any builder of plant that publishes a project table can be tested the same way.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** EQIX FAILS AT Q2 (OUT, on [E3-03]'s demonstration clause and [E3-46]: the best
  return on plant in the filed row, about 1.6x Digital Realty's, but about 8-9% pre-tax on net plant
  and falling for a decade; [E2-44](2) fails outright on capex of 32-58% of revenue; [E4-04] engaged,
  the plant is replaced at twice the unit cost). Q1 IN; Q3 IN on the binary (recorded; SEC closed its
  inquiry without action; [E4-29] in the pay; the capex-minor sentence withdrawn in 2025; dividends
  matched by issuance over eleven years); Q4 IN on survival (recorded; [E5-20] exception class
  applies; five-year owner earnings about zero to $1.4bn, central about $1.0bn; staying power 1 of 3);
  price $1,025.94 x 98,671,686 = $101.2bn, headed COMPUTATION — NOT A CLEARANCE: 0.9-1.1% business
  yield against a 5.29% sovereign; Q6 arms nothing.
- Work order: none. UNKNOWABLE: none.
