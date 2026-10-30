
## UPDATE 2026-09-26 - PPG: Q2 OUT. PPG is one of the global coatings majors; its price recovers cost, its largest segment is priced by index, its growth plan is share taken from the rivals it names, and fourteen years of acquisitions have left owner earnings where they were.

**PPG Industries, Inc. (PPG), wave 7 name 44, register entry 176.** Run file `Test Runs/2026-09-26 Run - PPG PPG Industries.md`.
CIK 0000079879. Price $107.52 (NYSE close 2026-09-25, aggregator, flagged) x 222.3 million shares (10-Q cover for
2026-06-30, `0000079879-26-000252`) = cap $23,901.7M; sovereign 5.49% (US Treasury, 30 Yr, 09/25/2026). **Q1 IN, Q2 OUT
on the business.** PPG appears once earlier in this file, in the Sherwin-Williams note (*"PPG had already EXITED US/Canada
architectural"*); this is its first run.

### The finding
- **Criterion (2) fails in the registrant's own words and plan.** *"The coatings industry is highly competitive"*; price
  is a *"Major Competitive Factor"* in all three segments; competition can *"compel us to reduce prices to remain
  competitive"*; and the stated growth path is *"share gains in all three businesses"* of Industrial Coatings, and in
  packaging, protective and marine, traffic and automotive OEM: customers who can be won from Akzo, Axalta and BASF can
  be lost to them.
- **The largest segment is priced by formula.** Industrial Coatings (41% of sales) sells on *"index-based"* contracts; its
  price fell 3% in 2024 and 1% in 2025 as raw materials eased, and was *"flat for the quarter, following previous price
  declines"* in Q2 2026.
- **PPG publishes the physical series [E4-55], and it is the demonstration clause.** Organic volume about -6 to -7%
  2014-2025; price about +30%, of which 21 points came in 2021-2023 while recovering raw-material inflation (the CEO in
  July 2026: *"we covered about 90% of the cost of goods sold inflation"*); outside that window price ran at about the
  rate of inflation, +1% and +2% in the volume-down years 2019-2020 included.
- **Returns on the owner's capital fell as capital was added.** EBIT on debt plus equity less cash: 21-25% pretax
  2014-2019 before one-offs, 14.3% in 2022, 16.2% in 2025; about 6% pretax on the ~$4.0bn added since 2019; about $8.7bn
  of acquisitions and $5.4bn of disposals 2012-2025, sales $15.4bn in 2014 and $15.9bn in 2025.
- **The row** (pretax plus interest over revenue): Sherwin-Williams ahead every year; PPG level with Axalta and RPM;
  AkzoNobel behind. AkzoNobel files no 10-K, but **its F-4/A for the Axalta merger (`0001193125-26-275378`) carries its
  IFRS statements**, a rung earlier runs of coatings names did not use.

### Beneath the close
- **Owner earnings, every window 3 to 14 years, both (c) ends: $956M to $1,422M (4.0-5.9% on the cap)**; five-year
  $984-1,192M; fourteen-year $1,099-1,231M; flat for fourteen years. SBC complete (the savings-plan match is cash); NCI
  subtracted; acquired amortization ($107-172M a year) taken out of the depreciation end. At the ~10% floor with no growth
  about $43-64 a share, at the sovereign $78-117, against $107.52 (computation only).
- **[E4-29] fires** (segment EBITDA in the 10-K's MD&A; Adjusted EBITDA margin in the release) while capex runs at twice
  depreciation; **[E3-53] fires as a series** (restructuring charges in 11 of 14 years, about $1.3bn, excluded from the
  adjusted EPS that carries half the bonus); an 11% cash-flow return-on-capital bar in the PBRSUs that the company's own
  figure missed in 2025 (10.0%); a guidance culture; buybacks at $114-130 a share. The disclosure itself is candid: every
  adjusted item reconciled, price and volume published by segment every year.
- **Signature, not a verdict**: #11 THE PASS-THROUGH, with [E2-56]'s camouflage as a feature.

### What the reading list should carry forward
- **AN INCONSISTENCY BETWEEN TWO RUNS, FOR THE OPERATOR.** The RPM run (2026-08-31) classed RPM NARROW IN on 13-18%
  pretax on all capital; this run classes PPG OUT on 14-16% (2022-2025) and 21-25% (2014-2019). The difference in
  evidence is that PPG publishes a price-versus-volume bridge and RPM does not (the RPM run carried that as a defect). A
  company that discloses more should not be judged more harshly for it; either the RPM class is generous or this one is
  harsh, and the corpus's demonstration clause (*"regularly price [...] aggressively and thereby to earn high rates of
  return on capital"*) is the text to rule on. **A ruling case is owed; this run does not resolve it by preference.**
- **For foreign competitors, look for an SEC merger filing before declaring the rung blocked**: an F-4 or F-4/A carries
  the foreign issuer's audited statements.
- **Next dates**: the Q3 2026 10-Q (late October 2026) and the FY2026 10-K (February 2027), for whether Industrial price
  turns positive against its index and whether volume growth of 2% in Q2 2026 persists.

### Priors refuted or confirmed
- `cap_flag` (cap below the filed float): refuted as an error; two dates compared as one. The float reproduces the
  2025-06-30 close; the 10-K's own 2026-01-31 float reproduces that date's close.
- `deal_note` empty: confirmed; nothing deal-shaped is live.
- `acq_note` ($2,392M, 9% of cap): confirmed as five real outflows, not an absolute-value artefact; incomplete, because
  $1,074M of disposals in the same window is not mentioned.
- `spread_caveat`: acted on; every window 3 to 14 years rebuilt; the older windows agree with the newer ones.
- The screen's OE ($1,014-1,314M): close to this file's, the gap being total versus continuing operating cash and NCI.

### Tooling defects (reported, not patched)
- **`cover_shares.py` parses no count from a cover that states shares in millions** (*"222.3 million shares"*).
- **`run.py` reads total operating cash (discontinued included) against continuing capex, subtracts no NCI, and prints an
  unexplained "-9.2%" growth figure.**
- **The screen's `cap_flag` compares a cap and a float struck on different dates.**
- **`acq_note` omits disposals.**
