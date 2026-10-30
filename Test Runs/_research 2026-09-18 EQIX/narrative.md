
## UPDATE 2026-09-18 - EQIX: Q2 OUT, the best landlord in the row, earning a landlord's return
`Test Runs/2026-09-18 Run - EQIX Equinix.md`. **Q1 IN, Q2 OUT, file closed; Q3 recorded (IN on the binary, overlay case, [E4-29] in the pay); Q4 recorded (IN on
survival; [E5-20] exception class applies; staying power 1 of 3); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded with nothing armed.** Price **US$1,025.94**
(2026-09-17 close, aggregator flagged, confirmed by three Form 4 prices) x **98,671,686 shares** (10-Q cover `0001101239-26-000147`) = cap **US$101,231.2M**;
sovereign **USD 30-year 5.29%** (US Treasury, 09/17/2026). **The seventh of wave 5's eight "capex unresolved [E5-20]" names; run unattended from scratch.**
**Register count at the fold, read from the register: 100 runs** (EQIX adds one Q2 OUT).

### WHY Q2 CLOSED, ON THE FILED RECORD
- **The best return in the row is not a high return.** (Operating income + D&A) over average gross plant: Equinix **11.9% / 11.1% / 11.6%** (FY2023-25) against
  Digital Realty **7.0% / 6.9% / 7.4%** and AMT's data centres about 7-8%. Equinix leads by about 1.6x. But after depreciation it earns **8.6% on net plant (FY2025),
  7.0-8.6% every year FY2020-25, down from 9.6-10.7% in FY2015-19**, and **7.0% on book equity over five years** with debt at 1.4x equity. [E3-03]'s demonstration
  (*"thereby to earn high rates of return on capital"*) and [E3-46] fail on the leader.
- **[E2-44](2) fails outright**: capital spending **32-58% of revenue every year FY2015-25**, now guided at **$5-7bn a year** to 2029.
- **[E4-04] in the company's words**: old buildings *"may exceed the designed electrical capacity"*, new ones carry *"power and cooling needs twice that of
  previous IBX data centers"*, lives shortened in FY2024 and FY2025, and *"If we fail to invest before or contemporaneously with our competitors, our results of
  operations could suffer."* The ecosystem is defended; the building is replaced.
- **The toll is real and not separable.** Interconnection is 18% of revenue (DLR 7.8%), about 500,000 connections, revenue per connection up about 4.7% in FY2025.
  But it lives inside buildings whose space and power sell in a market of *"more than 2,400 companies"*, and the Q2 2026 10-Q added a sentence that providers may
  *"bypass colocation environments"*. SPGI passed on a separable leg; EQIX has none.
- **The pricing in the window is the market's**: DLR renewals +6.7% cash FY2025 and +15.9% H1 2026; Equinix's Americas MRR per cabinet +2.2% a year FY2020-25
  while its own project cost per cabinet doubled.

### THE CAPEX LABEL AND (c), FROM THE FILED RECORD
- **No tag gap now; an incomplete capex end.** The screen prices EQIX, but `CAPX_TAGS` never reaches the face line *"Real estate acquisitions"* ($994M FY2025,
  $2,878M FY2015-25), and `annual()` kept real-estate values instead of plant values for FY2010-13 where one element carries both.
- **[E5-20] APPLIES, the second name after AMZN.** The company's own construction tables: project cost per sellable cabinet **$58.7k (FY2020) to $126.2k
  (FY2025)** against **$80.0k** of book plant per cabinet. Depreciation on historical cost does not renew the plant [E4-47].
- **The company's "recurring capital expenditures" run 11-17% of D&A** (DLR's 18-20%), and the 10-K sentence that justified them, *"future capital expenditures
  remain minor relative to our initial investment throughout its useful life"*, **disappeared from the Q3 2025 10-Q onward without explanation**, three weeks
  before the SEC closed its inquiry.
- **(c) built three ways**: total capex less growth $1.15-2.0bn a year (FY2021-25), depreciation $1.66bn, replacement cost about $2.9bn (FY2025). Five-year
  owner earnings **about zero to $1.4bn, central about $1.0bn**; FY2025 central $1.32bn. **Dividends exceeded owner earnings at the D&A end every year FY2015-25,
  and $11,234M of dividends were matched by $11,141M of equity raised** [E2-52].

### Q3 FINDINGS WORTH KEEPING
- **The 2024 episode, from the filings only**: short-seller report 2024-03-20; Audit Committee concluded on 2024-05-08 that reporting *"has been accurate"*;
  SEC closed without recommending action on 2025-11-19; the class action settled and was dismissed with prejudice, paid by insurance; one Delaware derivative
  suit pending. CEO, CFO and CAO all changed 2024-2026. **No disqualifier found.** The filings never state what the allegations were.
- **[E4-29] in the pay, with the [E4-27] incentive named**: the bonus is funded on equal-weighted revenue and AFFO per share; AFFO deducts only the capex the
  company classes as recurring. The FY2025 10-K says depreciation is *"derived from historical costs and we believe are not indicative of current or future
  expenditures"*.
- **[E2-49] fires small**: the Fabric attach metric missed threshold in 2025 and was replaced in the 2026 plan. **The [E2-49] prior now stands at seven fires and
  six failures.**

### REVERSAL CONDITION, IN WORDS (fold step 4; nothing armed, no PORTFOLIO row)
Reopen Q2 only on operating income over average net plant back above 9.6-10.7% and rising for three 10-Ks at the guided capex pace; Americas MRR per cabinet
outrunning project cost per cabinet for three years; revenue per interconnection still rising after the new bypass risk; or a filed maintenance figure that meets
[E2-23]'s (c).

### FOR THE OPERATOR
- **Tooling proposal (not made, because it changes a number):** add `PaymentsToAcquireRealEstate` to the capex construction, at least as a flag. **DLR, the last
  name in this row, should be checked for the same line before its run.**
- **`tools/sources.price()` returns intraday quotes stamped as closes**, now reproduced on two names (TOST, EQIX).
- **The REIT routing note in the wave 5 table points at a sector method that does not exist.** v4 was applied as written; whether a REIT method is wanted is a
  structural question for the operator under PRIME RULE 5.

### DEFECTS IN THE BRIEF (six) AND IN THIS RUN (one reaching a commit)
The brief framed the capex checks as tag questions (the defect was a second face line and a same-element value clash); characterised the short-seller report in
words no filing uses; under-stated the gap between the company's maintenance and the corpus's (c); did not anticipate the exception class; correctly flagged the
missing REIT method; and the queue's SKIPPED section still says only the D&A end is available. **This run's Step 0 said no September Form 4 existed**; the audit
found three filed sale prices (09-02 and 09-04), all inside Yahoo's ranges, and corrected it by dated note.

### ONE THING TO KEEP
**Price a builder's maintenance claim against its own project table.** Project capex over sellable cabinets, year by year, against book plant per cabinet, turned
an argument about "recurring" capex into an observed replacement cost from the filer's own page.
