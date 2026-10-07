## AIG (American International Group, Inc.) - run 2026-09-19 - Q1 IN, **Q2 OUT on the business**
Run file: `Test Runs/2026-09-19 Run - AIG American International Group.md`. WAVE 6, MINI BERK insurance track, sector method with both
amendments. Price US$75.33 (2026-09-18, aggregator, flagged); 522,893,169 shares off the Q2 2026 10-Q cover (`0000005272-26-000076`);
cap US$39,389M; sovereign 5.34% (US Treasury 30-year, 2026-09-18). Q3 and Q4 recorded, not governing; Q5 a computation only; no band.

### WHAT THIS RUN ADDS TO THE INSURER PANEL
- **The MKL/CB decisive series separates Chubb from AIG more sharply than any other measure in either file.** Current-accident-year
  combined ratio including catastrophes, 2016-2025, from the filer's own published points in four 10-Ks, every row re-added to the reported
  ratio: **100.4 / 113.2 / 110.2 / 100.8 / 104.4 / 96.4 / 93.7 / 92.0 / 93.2 / 92.2.** Above 100 in five of ten years; ten-year mean
  **99.65 against Chubb's 92.3**. The same hurricanes in 2017: Chubb 97.9, AIG 113.2. The same pandemic year: Chubb 97.4, AIG 104.4.
- **A new Q2 shape for the panel: the manager-made turnaround.** Same licences, same brand, same markets: five years above 100, then five
  below 94 in four of them. [E2-36]'s corporate Pygmalion rather than an excisable cancer, and [E4-04]/[E4-23] then close it, because the
  two executives who performed the turnaround leave on the filed record (Zaffino off the board 2026-09-15; Hancock, CEO of General
  Insurance, retiring 2026-12-31). Chubb's key-person question was open; AIG's is answered by its own first half-decade.
- **The competitor row now has AIG, TRV and HIG Business Insurance in it** (`Test Runs/_research 2026-09-19 AIG/peers/row_out.txt`): on the
  current-accident-year basis 2021-25, KNSL 80.60, ACGL 86.99, CB 89.50, WRB 89.84, HIG-BI 92.28, RLI 93.08, **AIG 93.50**, AXS 94.10,
  TRV 95.54, MKL 100.27. AIG is 7th of 10 in its best five years. **My TRV figures (96.3 / 97.5 / 97.4 / 94.2 / 92.3) match the TRV run's
  own, computed independently the same afternoon**, which is a cross-check on both files.
- **Reserving candor, read two ways.** AIG names every adverse line in words each year and publishes ten triangles, and its 2025 Investor
  Day deck prints its predecessors' *"2008 – 2018 $33B underwriting loss"* - a candor point. But its headline prior-year figure is struck
  after the NICO cessions: 2024 was **$254M adverse before the cover** and is reported as $368M favourable. [E2-67]'s scorecard is not
  published, as at Chubb.
- **The NICO adverse development cover is the panel's most direct evidence of what a non-franchise reserve book costs:** the pre-2016 US
  long-tail book has paid **$32.6bn against the $25bn attachment**, with $8.9bn still to pay, the excess funded by Berkshire.

### THE REFUTED PRIORS
- **"Check what AIG still holds in Corebridge" - it holds nothing.** Corebridge bought back $750M of stock from AIG on 2026-02-17 and AIG
  sold its last 25.5M shares on **2026-05-07** (Q2 2026 10-Q, Note 1). The carrying basis the brief asked about was the fair value option
  inside an equity-method line (2024-06-09 to 2026-03-31), then an equity security, then nothing.
- **"Management changed completely since 2008" - true, and it is changing again right now**, which the brief did not mention and which
  became the centre of Q2: a new CEO from 2026-02-16 (from Aon's presidency, not from underwriting), the executive chair gone on
  2026-09-15, the General Insurance CEO gone on 2026-12-31.
- **"A five-year window on one perimeter may not exist" - confirmed, and it bore on Q3 and Q5, not Q1, Q2 or Q4.** The consolidated
  statements carry continuing operations for 2023-2025 only, and 2023 still holds Validus Re and Crop Risk Services; the General Insurance
  segment series is continuous and is what Q2 used.
- **"Large adverse reserve charges in the 2010s" - confirmed from the rollforward**: prior-year development of $5,788M adverse in 2016,
  $1,565M in 2017, $1,429M in 2018 (FY2018 10-K).
- **The death candidate:** the brief listed catastrophe, long-tail reserves and the portfolio. The filings support long-tail reserves;
  the catastrophe exposure is small **net** (1-in-250 worldwide $2.5bn, 4.8% of equity) because AIG cedes 40.9% of gross reserves and
  buys a large catastrophe programme. The dependence on reinsurers' annual renewal is the [E5-39] item instead.

### DEFECTS FOUND
- **Tooling: `.gitignore` does not cover the `tenk_*.txt` / `tenq_*.txt` names** that the CB fetcher and this run's fetcher use for
  stripped filings (the patterns match `*10-K*`, `*10K*`, `*10k*`, `*10-Q*` and so on). The CB run's five stripped 10-K/10-Q files entered
  history that way. This run did not commit its stripped filings; the pattern is left for the operator to extend, not edited here.
- **Process: something other than this run wrote into this run's research folder** during the run (stripped AIG 10-Ks for FY2017,
  FY2019 and FY2024, and fresh copies of FY2021 and FY2023, at 15:37-15:40). Same EDGAR documents, no harm done, and not committed; but a
  second writer in a run's folder is the precondition for the crossings the fold rule exists to prevent.
- **`tools/sources.py:cik_for()` returns a `(cik, name)` tuple**, not a CIK string; a script that formats it as a number fails. Not a bug,
  a signature worth knowing.
- **Sector method gap 1 - CONVENTION 4 cannot be built on a consolidated balance sheet that still holds a life insurer** (AIG before
  2024-06-09: life receivables and DAC corrupt two of five terms). This run used average net loss reserves from the rollforward as the
  float proxy for the ten-year cost of float and confessed it; the two agree in direction for 2025 (-5.69% against -5.06%).
- **Sector method gap 2 - retroactive reinsurance has no rule.** AIG's ratios and cost of float exclude the development ceded to NICO
  and the deferred-gain amortisation; the consideration paid for the 2017 cover is outside the General Insurance ratio entirely. A filer
  that has sold its reserve deficiency looks cheaper to fund than it was. The run disclosed it rather than adjusting for it.
- **Sector method pointer: "Schedule P"** - the method cites the statutory Schedule P triangles; this run (like CB) used the 10-K Note
  triangles, which are GAAP, net, undiscounted and by line. Schedule P was not pulled.

### ONE THING TO KEEP
The price is the strongest fact against the verdict: **0.97x book and 12.0% pre-tax on 2025 adjusted earnings with the excluded
restructuring put back** - above the ~10% floor that quit Chubb. A Q2 OUT on a cheap insurer is [E3-47]'s omission risk by definition;
the Q6 reversal conditions (current-accident-year ratio under 95 through FY2028 under the new management; a top-half row position; no
adverse excess-casualty development on AY2021+; expense ratio under 29%) are the written test of whether it was the wrong close.
