
## UPDATE 2026-09-13 - ABNB: Q2 OUT, the cheapest demand in travel, sold into a category with two rivals of its size
`Test Runs/2026-09-13 Run - ABNB Airbnb.md`. **Q1 IN, Q2 OUT, file closed; Q3 recorded (no disqualifier, gate case, buyback flag, converging
stock-price flags); Q4 recorded (would read IN on survival; THE PERMIT proposed); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded with nothing
armed.** Price **US$170.19** x **589,585,682 shares** = cap **US$100.3bn**; sovereign **USD 30-year 5.35%** (US Treasury, 09/11/2026). **The first of
wave 5's eight "capex unresolved [E5-20]" names.** **Register count at the fold, read from the register: {{COUNT}} runs** (ABNB adds one Q2 OUT).

### THE SKIP REASON, TESTED - A REAL TAG GAP, THE WRONG CORPUS LABEL
- **The gap is real and it is presentation:** from the FY2023 10-K, *"Purchases of property and equipment"* is folded into *"Other investing activities,
  net"* on the face of the cash-flow statement and appears only in the MD&A FCF reconciliation ($33M in 2025, 0.27% of revenue). `PaymentsToAcquire
  PropertyPlantAndEquipment` therefore ends at FY2022 and `run.py` priced three years.
- **The [E5-20] label does not fit:** D&A exceeds capex in five of six listed years; the renewal cost of this business is expensed (product development,
  marketing, a $1.7bn hosting commitment). **The D&A default [E3-44] applies, and the (c) band is under 5% of owner earnings in every window.** The skip reason's
  generic wording ("the corpus calls it INVALID for this class") was written for railroads and attaches to every missing capex tag; the next seven names in
  the row (AMZN, NVDA, CL, SPGI, TOST, EQIX, DLR) should test which case they are before assuming the exception.

### THE BRIEF'S QUESTIONS, ANSWERED FROM THE FILED RECORD
- **Share classes:** A and B identical in dividends and liquidation (20 votes on B), summed; **Class H excluded** (9.2M, held by a wholly-owned subsidiary,
  "issued and zero shares outstanding" on the balance sheet, though the cover calls it outstanding); Class C zero.
- **Customer funds:** unlike PAY, **the host funds never touch operating cash** - their swing is financing and their cash is restricted cash. Operating
  cash carries the unearned-fee float and the interest on held funds; owner earnings are shown with each removed.
- **SBC:** resolves to the dollar; **49.6% of OCF since the IPO year, 31.7% ex-2020** - below CRWD's 68.0% in the calibrated row, rising four years.
  Withholding on net settlement counted with buybacks, not subtracted twice. $16.4bn of repurchases and withholding since 2022 cut the count 6.6%.
- **Taxes:** the 2023 $2,897M valuation-allowance release and the 2025 $213M allowance are non-cash; set aside.
- **Regulation:** New York City's Local Law 18 (September 2023) - *"Prior to September, New York City represented approximately 1% of Airbnb global
  revenue"*; *"Approximately 80% of our top 200 markets by revenue already have some form of regulation"* (Q3 2023 letter); EU STR Regulation from May 2026;
  Spain €65M proposed fine; Italy $957M settled for 2017-23. The 10-K quantifies no other market.

### WHY OUT AND NOT UNKNOWABLE
- **For IN, stated at full strength:** brand and performance marketing 13.0% of revenue against Booking's 30.4%; cut from $1,140M (2019) to $723M (2021)
  while GBV rose $38.0bn to $46.9bn; 2020 bookings -37% against Booking -63% and Expedia -66%; recovered first.
- **Against, and decisive:** criterion 2 is what the customer thinks. Airbnb's 10-K says hosts often cross-list and guests compare sites; Expedia's 10-Ks name
  property managers listing on Airbnb, Vrbo and Booking.com; Booking.com's homes listings nearly doubled since 2019 to ~3.9M and reached ~36% of its room
  nights; the take rate has been flat for three years below Booking's, and the 15.5% single host fee is take-rate-neutral by design, introduced because
  cross-listed homes look cheaper elsewhere. **The documents that decide criterion 2 exist and were read; they agree.**

### REFUTED OR NARROWED PRIORS
- **"Direct demand = franchise" is narrowed:** marketing efficiency is a measured advantage in how demand is acquired, not evidence the customer sees no
  substitute. The fee conduct is the test, and it is defensive.
- **"Funds payable is the owner-earnings trap" is narrowed for marketplaces that ring-fence host money:** the separation still has to be done, but here it
  moves owner earnings ~8-18%, not the sign.
- **"Stock compensation is the centre of the file" did not hold** at 31.7-49.6% of OCF; the franchise question closed it.

### NEW FOR THE OPERATOR
- **A proposed survival shape, THE PERMIT** (it would be the seventeenth, after THE TENANT, THE PATRON, THE DOWRY and THE FLAG, none registered): the
  product is a use of other people's property that governments permit, cap or withdraw market by market, while making the platform enforce the rules and
  collect and pay the tax. Nearest are THE PATRON (but the permit-giver pays nothing) and THE FLAG (but supply is lost to the regulator, not a rival bid).
  **The register of shapes is unchanged; added to the index as proposed.**
- **The OTA row is now on disk** (`Test Runs/_research 2026-09-13 ABNB/peers/PEER_ROW.md`): Booking, Expedia (with Vrbo's last segmented year) and Trip.com
  2019-2025, with take rates, units, 2020 collapses, marketing, SBC/OCF, float treatment and verbatim competition language - for any later BKNG, EXPE or TCOM run.

### TOOLING AND SOURCE DEFECTS FOUND
- **`tools/sources.py:fts_count()` does not guard the phrase:** a phrase that already carries quote marks returns an inflated count (98 against 2 for
  "Local Law 18" in Airbnb's filings). It guards the CIK only; same defect class as the CALX harness.
- **`run.py` / `sources.annual()` read capex from one tag**; a filer that moves capex into a combined investing line and the MD&A reconciliation goes
  unpriced, and the skip reason then names the wrong corpus case.
- **`Screens/cover_shares.py` sums a subsidiary-held class** the balance sheet excludes (Class H here); the tool's MULTIPLE CLASSES warning is right, but the
  "outstanding" cover wording does not identify it.
- **Airbnb's shareholder letters are mostly images**, but their text layer carried the outlook, fee and regulation passages this run quotes.
