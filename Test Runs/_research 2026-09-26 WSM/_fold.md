
## UPDATE 2026-09-26 - WSM: Q2 OUT. Williams-Sonoma designs and sells its own home furnishings through its own websites and stores; its own 10-K says rivals sell similar goods at lower prices, the same brands earned 8.4% of revenue over fiscal 1997-2019 and 1.2% before tax in fiscal 2008, and the post-2020 doubling was a wave the whole row rode. A well-run merchant, not a franchise.

**Williams-Sonoma, Inc. (WSM), wave 7 name 50, register entry 192.** Run file `Test Runs/2026-09-26 Run - WSM Williams-Sonoma.md`.
CIK 0000719955, fiscal year to the Sunday closest to 31 January. Price $231.90 (NYSE close 2026-09-25, aggregator,
flagged) x 117,779,173 shares (10-Q cover at 2026-08-23, `0000719955-26-000208`, outstanding) = cap $27,313M; sovereign
5.49% (US Treasury, 30 Yr, 09/25/2026). **Q1 IN, Q2 OUT on the business.** One unattended session ran the whole file,
from the claim to the fold.

### The finding
- **[E3-03] criterion (2) fails in the registrant's own words**: *"We compete with other retailers that market lines of
  merchandise similar to ours"*; *"discount retailers selling similar products at reduced prices"*; *"managing against
  increasingly competitive promotional activity"*; *"style and color trends are constantly evolving"*, the product re-won
  each season with *"newness"* and collaborations.
- **[E2-53]'s dominance test fails on its own twenty-nine years**: aggregate margin 8.4% over fiscal 1997-2019, level with
  a row that includes Bed Bath & Beyond and Pier 1 (both since bankrupt); 1.2% before tax in fiscal 2008 on occupancy
  deleverage and markdowns; 16.9% over fiscal 2020-2025.
- **The step was the row's**: RH 24.7%, Ethan Allen 16.9% and Arhaus 15.0% at their 2021-2022 peaks. Williams-Sonoma
  kept its margin afterwards (17.6% in 2023-2025 against 8.6-13.5%), and that is the strongest fact against the verdict;
  it kept it by cutting promotions and giving up volume and share (revenue 2022-2025 −10.0% against RH −4.2%, Arhaus
  +12.2%, Wayfair +2.0%), which [E2-44] and [E4-37] read as a merchant's choice, not a franchise's ease.

### Beneath the close
- **Owner earnings, every window 3 to 20 years and both ends: $455.2M to $1,131.9M (1.67-4.14%), every window below the
  5.49% sovereign.** The screen's $1,011M and $1,132M reproduce to the million. Owner earnings were 14.6% of revenue in
  fiscal 2023-2025 and 4.9-5.3% in fiscal 2006-2019: the spread is the step. Rent is paid inside operating cash; no lease
  adjustment. SBC resolves from fiscal 2006; no NCI. At the ~10% floor with no growth about $40-95 a share, at the
  sovereign $70-175, against $231.90 (computation only).
- **Q3 prompts**: the FTC's 2020 Made in USA order was violated and a record $3.175M civil penalty followed (FTC release
  2024-04-26), not mentioned in any 10-K read; no EBITDA anywhere; a $10bn revenue target for fiscal 2024 missed by 23%;
  the fiscal 2025 bonus EPS adjusted for tariffs; buybacks at about $175-179 above the floor range.
- **Signature, not a verdict**: #20 THE WAVE, with #13 THE TENANT as a feature.

### What the reading list should carry forward
- **The designer-retailer reading, for the next specialty retailer of its own brands (RH, Arhaus, Ethan Allen, Lululemon)**:
  set the post-2020 margin against the company's own pre-2020 decade and against the row in the same years. Where the
  whole row stepped up in 2021-2022, the step is the wave; what matters is who kept it afterwards, and at what cost in
  volume and share.
- **Rent is inside operating cash for every lessee retailer under both lease standards**; no lease adjustment is needed to
  build owner earnings, and none should be invented.
- **Read the regulator's own releases for conduct matters a 10-K leaves out**: the FTC Made in USA penalty is in no
  Williams-Sonoma 10-K.
- **Next dates**: the 10-Q for the quarter to 2026-11-01 (late November 2026); the fiscal 2026 10-K (March 2027), the
  first full year with tariff refunds and the new Section 301 tariffs.

### Priors refuted or confirmed
- `deal_note` empty: confirmed (the June 2025 credit agreement is the only Item 1.01 since 2021). `level_shift` STEP UP -
  normalize down [E4-41]: confirmed, and it decided Q2 as much as Q4. `best_year_dep` "no single-year dependence (9-yr OCF
  series)": true of the nine years; over twenty the dependence is on the six post-2020 years together. `spread_caveat`:
  rebuilt over twenty years. `years_filed` 18 is the XBRL span; the 10-Ks run to fiscal 1994.

### Tooling defects (reported, not patched)
- **`run.py` printed "GROWTH THE PRICE ASSUMES -4.8%"** (about +1.3% on its own figures): the seventh run running (MATX,
  PPG, LNN, SYY, MLI, CMT, WSM).
- **`run.py` printed "POINTS OVER THE SOVEREIGN +1.28 .. +1.39"** on yields of 4.08-4.18% against 5.49%: the fourth run with
  this line wrong (SYY, MLI, CMT, WSM).
- `run.py`'s per-year minimum and maximum mix the two (c) ends inside one window; it stops at five years; the screen's
  level notes are truncated in the CSV. `cover_shares.py` read this cover correctly ("outstanding").
