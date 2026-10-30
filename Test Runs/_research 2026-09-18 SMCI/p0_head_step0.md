# Company Run — Super Micro Computer, Inc. (SMCI) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stop at the first verdict that is not IN.** Run unattended from scratch (no
prior run file for SMCI exists; the DELL run of 2026-09-07 used Super Micro's filings as one line of its
competitor row, and every SMCI figure below is recomputed from SMCI's own filings). WAVE 5, the first of
the seven "perimeter or restatement above threshold" names. Research, scripts and downloaded filings are
in `Test Runs/_research 2026-09-18 SMCI/`.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Asked aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0: THE SKIP REASON, THE RATE, THE PRICE, THE COUNT, THE PERIMETER, AND THE FILING

### The skip reason, tested on the filing rather than inherited
The wave 5 row is *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason
list says *"revenue step or cross-accession restatement above threshold."* **A prompt to read, never a
verdict.** The brief's probe (`_probe_screen.py`) and this run's reproduction of the 2026-09-01 triage
code (`triage_repro.py`, running `Screens/floor_screen.py` as it stood at commit `a8bc84f`, the commit
that wrote the wave 5 table, over the same companyfacts pull) say what each guard was reacting to:

| guard | value | what it was reacting to, on the filings |
|---|---|---|
| `share_count_shift` (the guard that fires FIRST in the `a8bc84f` code and returns the name unpriced) | **11.22x** | **A 10-for-1 forward split, not a perimeter change.** The Yahoo split feed carries *"10:1"* effective 2024-10-01; the dei cover counts read 58,556,527 (2024-04-30) then 593,481,352 (2025-01-31). The `a8bc84f` guard did not divide out splits; the split fix landed on 2026-09-02 (docstring: *"SPLITS ARE NOW DIVIDED OUT FIRST"*) and **the row was never re-triaged**, the AMZN kind of tooling artefact. The current guard with the ticker passed returns **1.12x**. The brief's probe called it without the ticker and reprinted the old 11.2x. |
| `scale_shift` | **2.10x** | **A real revenue step, and it is organic.** Net sales **$7,123.5M (FY2023) to $14,989.3M (FY2024)** (FY2024 10-K income statement), then $21,972.0M and **$39,063.1M (FY2026)**. `acquisition_flag` reads $2.5M; the only acquisition line on any cash-flow face read is *"Acquisition, net of cash acquired ( 296 )"* thousand in FY2024. The step is AI rack demand, not a merger. |
| `restatement_shift` | **(1.0, 2018-06-30)** | **A ratio of 1.0 is a NULL: no disagreement found.** The function reads the first revenue tag that has data (`RevenueFromContractWithCustomerExcludingAssessedTax`, FY2017 onward), where FY2018 carries $3,360.5M in both the FY2019 and FY2020 10-Ks. **It is structurally blind to the restatement that did happen**: FY2015-FY2016 were restated in the FY2017 10-K filed 2019-05-17 (below), and the original and restated values sit under different elements (`SalesRevenueNet` FY2015 **$1,991.2M** original; `Revenues` FY2015 **$1,954.4M** restated, -1.8%; FY2016 $2,215.6M to $2,225.0M). |

**So the label was, for SMCI: a split artefact (the guard that actually stopped the name), a genuine
organic revenue step, and a real restatement history that the restatement guard cannot see.** The
restatement is a Q3 matter and is read there.

**What the current screen says behind the label (tagged data, a prompt only):** `owner_earnings()` prices
SMCI and returns **negative owner earnings at every end** (5y D&A -$1,730M, 5y capex -$1,794M, 3y D&A
-$2,906M, 3y capex -$3,003M), driven by operating cash of **-$6,809.9M in FY2026**. `working_capital_flag`
returned `None` on this series, and the reason is the flag's scope, not the data: `WC_TAGS` reads only the
liability side (payables, accrued liabilities, deferred revenue; built for DELL's payables and INOD's prepayment),
and none of those crossed 30% of operating cash (deferred revenue +$1,880.7M is 27.6% of FY2026's). **The asset
side is where SMCI's cash went and the flag cannot see it**: the FY2026 inventory line moved **-$8,876.7M**
and receivables **-$3,921.9M**, against operating cash of **-$6,809.9M** (`IncreaseDecreaseInInventories`,
`IncreaseDecreaseInAccountsReceivable`; tooling note at the audit). SBC resolves for every year FY2010-26 (`ShareBasedCompensation`
= face *"Stock-based compensation expense | 412,115 | 314,452 | 231,507"*) and is complete on the face (one line,
no separate capitalised-SBC or 401(k) stock line found). The screen's D&A for FY2026 (**$53.0M**,
`DepreciationDepletionAndAmortization`) is **not the face figure** (*"Depreciation and amortization | 53,673"*),
which sits in no element companyfacts publishes (searched by value); the difference is $0.7M and immaterial.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.29%** · **09/17/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority.** Struck
  by this run: the cached curve was deleted and `tools/sources.sovereign("USD")` re-fetched it on
  2026-09-18 at about 18:40 UTC, returning `(5.29, '09/17/2026', 'US Treasury daily par yield curve')`
  (`step0_out.txt`). Not inherited from the DLR run; it happens to be the same figure because 09/17 is still
  the newest row published. FRED was not used.
- **Earnings currency: USD.** 10-K Item 7A: *"substantially all of our sales and purchases are denominated
  in United States dollars."* Sales outside the US were *"29.1%, 40.6%, and 32.0% of net sales in fiscal
  years 2026, 2025, and 2024"*.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$40.35, the close of 2026-09-17**, the last completed close. Source: Yahoo Finance daily chart via
  `sources._chart("SMCI", rng="1mo")` (aggregator, permitted for live quotes only, **flagged**;
  `step0_out.txt`). Bar: open 38.04, high 41.01, low 37.82, close 40.35, volume 62.4M.
- **`tools/sources.price()` was NOT used for the struck price.** At about 18:41 UTC on 2026-09-18 it
  returned `(38.72, '2026-09-18', 'USD')`, the intraday `regularMarketPrice` stamped with today's date,
  while its docstring says *"Latest close."* **The TOST, EQIX and DLR defect reproduces on a fourth name.**
- Recent closes: 09-10 $37.38 · 09-11 $40.10 · 09-14 $36.74 · 09-15 $35.64 · 09-16 $36.85 · 09-17 $40.35.
  Range over the month shown: $35.17 (08-24) to $40.35.
- **Primary-filing cross-check of the aggregator: two Form 4s, both inside the day's range.** Accessions
  **`0001392942-26-000013`** (Charles Liang) and **`0001392941-26-000014`** (Sara Liu, the same jointly held
  shares), filed 2026-09-08: sales of 42,565 shares at **$36.60** and 57,435 at **$37.62** on 2026-09-03 (Yahoo
  bar low $35.75, high $38.22) and 100,000 at **$40.00** on 2026-09-04 (low $37.92, high $40.91). The
  founders' own sales are also a Q3 fact.
- **Split factor after the count's date (2026-07-31): 1.0** (`sources.split_factor_after`); the one split
  in the full history is the 10-for-1 of 2024-10-01. `close` used, never `adjclose`.

### The share count: from the cover, with the accession
- **656,965,384 shares**, from the cover of the **FY2026 Form 10-K** (period ended 2026-06-30, filed
  **2026-08-31**, accession **`0001375365-26-000022`**): *"As of July 31, 2026, there were 656,965,384 shares
  of the registrant's common stock, $0.001 par value, outstanding, which is the only class of common stock of
  the registrant issued."* `Screens/cover_shares.py SMCI` returns the same figure from the same accession,
  *"(single class / undimensioned)"*. This is the latest periodic filing (the Q1 FY2027 10-Q is not due
  until November).
- **ERIC trap checked**: the balance sheet reads *"Issued and outstanding shares: 656,882 and 594,137 at June
  30, 2026 and 2025"* (thousands); no treasury line. **SPGI trap checked**: no exclusion clause on the cover;
  the preferred is a separate listed class (SMCIP) and is not common.
- **The count grew 10.6% in the year**, almost all in June 2026: 594,136,852 (2025-06-30) to 656,882,499
  (2026-06-30); **52,272,726 shares sold in a public offering** (45,454,545 plus the 6,818,181 option; 8-K
  `0001193125-26-269703`, 2026-06-12; *"Issuances of common stock in public offerings, net of issuance costs |
  52,272,726 | 1,405,950"*, statement of equity), the rest option exercises and RSU releases net of
  withholding. A **$1.25bn at-the-market programme** was opened the same week (same 8-K).

### The perimeter between the business and the common holder: stated, not blended
1. **7.00% Series A Mandatory Convertible Preferred Stock, issued June 2026**: 4,312,500 shares, $1,000
   liquidation preference each, **$4,231.6M net cash** (cash-flow statement), dividends 7.00% (**about $302M a
   year**, payable in cash or stock), and **mandatory conversion in June 2029 *"into between 30.3040 and 36.3640
   shares of Common Stock"*** per preferred share (8-K `0001193125-26-270430`, 2026-06-15). That is **130.7M to
   156.8M common shares, +19.9% to +23.9%** on the cover count; at any price above about $33.00 the lower
   figure applies, and $40.35 is above it. **Treatment: this claim is equity that WILL become common, so the
   perimeter-consistent cap adds the 130.7M shares at the struck price, and the preferred dividend is NOT
   also deducted from owner earnings on that basis** (it is one or the other, never both). Both caps are shown
   at Q5.
2. **Convertible notes**: $1,725.0M due 2029 (0.00%), $700.0M due 2028 (2.25%, conversion price *"approximately
   $ 61.06"*), $2,300.0M due 2030 (conversion price *"approximately $ 55.20"*) (10-K Note on convertible notes).
   All out of the money at $40.35; treated as debt, with capped calls purchased in FY2024 and FY2025.
3. **Bank debt**: *"$2.0 billion of outstanding borrowings under our Revolving Credit Facility with JP Morgan,
   $1,763.5 million outstanding borrowings under our CTBC Revolving Credit Facilities"*; total indebtedness
   *"approximately $8.7 billion"* at 2026-06-30. Cash $7,521.5M.
4. **No goodwill, no intangibles, no equity-method stake of size** (equity investees' share of loss $2.5M);
   non-controlling interest $0.2M.

### The market cap
- **$40.35 × 656,965,384 = US$26,508.6M.** Split factor after 2026-07-31 = 1.0.
- **Perimeter-consistent, with the mandatory preferred at its minimum conversion (130,686,000 shares):
  $40.35 × 787,651,384 = US$31,781.7M.** Displayed side by side, not blended.

### LIVE-DEAL CHECK: run by this run, not inherited
- `sources.deal_filings("0001375365")` returned `([], [], '2026-08-31')` and `deal_note` returned an empty
  string: no DEFM14A, PREM14A, S-4, SC 14D9, SC TO-T or 425 since the 10-K, and no 8-K Item 1.01 since it.
- **Every 8-K since 2024-01-01 was downloaded and the Item 1.01 ones were read** (`fetch8k.py`, `8k/`):
  credit agreements (JPMorgan revolver 2025-12-29 and amendments 2026-01-26, 2026-06-10; CTBC Taiwan facility
  2026-01-21), the MUFG receivables purchase agreement (2025-07-16), convertible-note indentures (2024-02,
  2025-02, 2025-06), the June 2026 common offering, ATM and mandatory-preferred filings. **None is an offer for
  Super Micro's shares and no EX-2.1 plan of merger was found. The quote is an owner-earnings price, not a
  spread.**

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2026 Form 10-K**, period ended 2026-06-30, filed **2026-08-31**, accession **`0001375365-26-000022`**
  (`10K_FY2026.txt`; auditor BDO USA, P.C., report dated August 31, 2026). It carries Part III (directors,
  compensation, related parties) in the 10-K itself.
- Also read: 10-Ks FY2025 (`0001375365-25-000027`), **FY2024 (`0001375365-25-000004`, filed 2025-02-25, six
  months late)**, FY2023 (`0001375365-23-000036`), FY2022 (`0001375365-22-000103`), FY2021
  (`0001375365-21-000060`), FY2020 (`0001375365-20-000064`), **FY2019 (`0001375365-19-000079`, filed
  2019-12-19)** and **the FY2017 10-K filed 2019-05-17 (`0001375365-19-000039`) carrying the FY2015-16
  restatement**; the Q3 FY2026 10-Q (`0001375365-26-000014`); the DEF 14A of 2026-03-03
  (`0001375365-26-000008`); 8-Ks and EX-99.1 releases 2024-2026 and the selected earlier ones named at Q3.
- **Figures cross-checked against the filed statement** (FY2026 consolidated statement of cash flows):
  *"Net cash (used in) provided by operating activities | ( 6,809,886 ) | 1,659,524 | ( 2,485,972 )"*,
  *"Stock-based compensation expense | 412,115"* and *"Purchases of property, plant, and equipment ... | (
  161,999 )"* all match companyfacts exactly (`NetCashProvidedByUsedInOperatingActivities`,
  `ShareBasedCompensation`, `PaymentsToAcquirePropertyPlantAndEquipment`, accession `0001375365-26-000022`).
  The face D&A line is the one that does not (above).
