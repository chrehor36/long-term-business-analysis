# Company Run — Blackstone Inc. (BX) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Fill top to bottom. **Stop at the first verdict that is not IN.**

Run unattended from scratch on 2026-09-18 (evening, EDT); the template was copied and committed before any fetch
(`05f082b`). No prior run file for BX exists. WAVE 5, the sixth of the seven "perimeter or restatement above
threshold" names. Research, scripts and downloaded filings are in `Test Runs/_research 2026-09-18 BX/`; the brief is
`_BRIEF.md` there. Sections were written as they closed and committed after each gate. **The BAM run of 2026-09-13
read BX's filings for its competitor row; nothing in that run is evidence about BX, and every BX figure below was read
on BX's own filing.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

### The entity, in every year used
CIK 0001393818, `submissions.json`: *"Blackstone Inc."*, SIC *"Investment Advice"*, fiscal year end 1231; former names
*"Blackstone Group L.P."* (2007-03-22 to 2019-06-28), *"Blackstone Group Inc"* (2019-07-01 to 2021-08-05), *"Blackstone
Inc"* (from 2021-08-06). The FY2021 10-K: *"Effective August 6, 2021, The Blackstone Group Inc. changed its name to
Blackstone Inc. Blackstone Inc. was initially formed as The Blackstone Group L.P. (the "Partnership") and converted from a
Delaware limited partnership to a Delaware corporation, The Blackstone Group Inc. (the "Conversion"), effective July 1,
2019."* **One reporting entity throughout; no reverse recapitalization and no shell (the DJT check was run).** The
conversion matters for one thing only: FY2019 is part partnership and part corporation for tax, so the provision for
taxes before FY2020 is not comparable. **Every owner-earnings year used below (FY2020-25, H1 2026) is after the
conversion.**

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list: *"revenue step
or cross-accession restatement above threshold."* **A prompt to read, never a verdict.** Reproduced by the
brief-writer against `Screens/floor_screen.py` at `a8bc84f` (`floor_screen_a8bc84f.py`) over companyfacts cut to facts
filed by 2026-09-01 (`triage_repro.py`, `triage_repro_out.txt`, re-read by this run):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | 1.040 | no | ordinary vesting and unit exchanges net of buybacks; no split (`split_factor_after` 1.0); a dei element exists (the RIVN None check) but it is **common stock only** (below) |
| **2. `scale_shift`** | **3.700** | **YES: THE GUARD THAT RETURNED BX UNPRICED** | **NOT A PERIMETER AND NOT A RESTATEMENT: A MARK.** FY2020 $6,101.9M to FY2021 $22,577.1M under `Revenues`, consecutive years (the TSLA check was run: the same element carries every year FY2008-25). The FY2022 10-K statement of operations (`0001193125-23-048733`), $K FY2022 / FY2021 / FY2020: *"Performance Allocations Realized 5,381,640 5,653,452 2,106,000 Unrealized ( 3,435,056 ) 8,675,246 ( 384,393 )"* and *"Principal Investments Realized 850,327 1,003,822 391,628 Unrealized ( 1,563,849 ) 1,456,201 ( 114,607 )"*. **Unrealized marks were $10,131M of FY2021 revenue and minus $4,999M of FY2022**; the swing in those two lines ($15,130M) is larger than the whole FY2021-22 revenue fall ($14,059M). Fees did not step: *"Management and Advisory Fees, Net $ 6,303,315 $ 5,170,707 $ 4,092,549"*. The next step (0.377) is the same marks reversing. |
| 3. `filed_years` | 16 | no | |
| 4. `owner_earnings` | 5y $3,405M D&A end / $3,348M capex end | no (priced) | the triage stopped at guard 2; the figures are OCF less SBC less (c) with the firm's and the consolidated funds' investment purchases and sales inside OCF (below, and Q4) |
| (`restatement_shift`, not a guard in that pipeline) | (1.004, FY2016) | n/a | a null, as at SMCI, SNOW, TSLA, RIVN and DJT |

**So the label was, for BX: GAAP revenue that includes unrealized fair-value marks on carried interest and on the
firm's own investments, which moved +$10.1bn in FY2021 and -$5.0bn in FY2022.** Not a perimeter event, not an organic
step, not a tag hole, and not a restatement: **no 10-K/A or 10-Q/A exists in the 1,726-filing index
(`filings_list.txt`)**, and the FY2025 10-K cover leaves the error-correction box unticked (*"reflect the correction of
an error to previously issued financial statements. ☐"*). **This is the first name in the row whose label measured
neither a business event nor a tooling artefact but an accounting convention: revenue recognised on marks.** The
`scale_shift` guard will fire on any carry-earning manager in a strong mark year.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by
  this run at 20:11 EDT (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned the cached **09/17/2026 5.29%** row one second earlier (`step0_out.txt`), the
  stale-cache defect recorded a fifth time; the issuing-authority figure is used. FRED not used. Not inherited from DJT
  (the figure agrees because it is the same day's print).
- **Earnings currency: USD.** A Delaware corporation in New York reporting in dollars. No FX or ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$124.96, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("BX", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 124.96,
  `regularMarketTime` 1789761603 = 16:00:03 EDT, so the figure is the closing print. The day's bar had not finalised
  (open 124.28, high 125.17, low 122.85, close None). `tools/sources.price()` returned the same 124.96 stamped 2026-09-18.
- Recent closes: 09-11 $128.51 · 09-14 $128.29 · 09-15 $126.70 · 09-16 $123.45 · 09-17 $125.41 · 09-18 $124.96. One
  month earlier (08-19) $145.09: **down 14% in a month.**
- **Primary-filing cross-check:** Form 4 `0001193125-26-395751` (Joseph Baratta, filed 2026-09-18) reports sales on
  **2026-09-18** at weighted **$123.35** (*"prices ranging from $122.85 to $123.84, inclusive"*) and **$124.13**
  (*"$123.85 to $124.72"*), inside the Yahoo bar's range. **Corroborated.**
- **Split factor after the count's date (2026-07-31): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the units question
- **750,625,114 shares of common stock**, from the cover of the **Q2 2026 Form 10-Q** (quarter ended 2026-06-30, filed
  **2026-08-07**, accession **`0001193125-26-340208`**): *"As of July 31, 2026, there were 750,625,114 shares of common
  stock of the registrant outstanding."* `Screens/cover_shares.py BX` returns the same figure and accession.
- **The cover count is not the economic count.** 10-Q Note 13: *"As of June 30, 2026, the total shares of common stock
  and Blackstone Holdings Partnership Units entitled to participate in dividends and distributions were as follows"*:
  Common Stock Outstanding 752,601,287; Unvested Participating Common Stock 47,333,292; Total Participating Common Stock
  799,934,579; **Participating Blackstone Holdings Partnership Units 443,878,452; total 1,243,813,031.** Holders *"may
  exchange their Blackstone Holdings Partnership Units for shares of Blackstone common stock on a one-for-one"* basis
  (Note 17); Net Income Before Taxes allocated to the unitholders was *"37.2%"* for H1 2026 (MD&A). The Series I and
  Series II preferred are **one share each** (*"the holder of the sole outstanding share of our Series I preferred
  stock"*; the same for Series II), carrying votes and no economics.
- **Which count the yield uses, and why:** owner earnings below are computed for the whole operating firm, before the
  income attributed to *"Non-Controlling Interests in Blackstone Holdings"*, so they belong to common and units
  together. **The yield uses the economic count, 1,243,813,031** (one note, one date, 2026-06-30). Pairing firm-level
  owner earnings with the common count alone would overstate the yield by 66%. The unvested participating common is
  included because it receives dividends; its vesting cost is also inside the SBC subtracted at Q4, so this choice errs
  conservative by at most 3.8%.

### The market cap, on both counts
- **Common alone: $124.96 x 750,625,114 = US$93,798M ($93.8bn)** (public float $108.9bn at 2025-06-30, 10-K cover).
- **Common plus participating units (economic): $124.96 x 1,243,813,031 = US$155,427M ($155.4bn)**, the cap the yield
  uses. (Cover common at 07-31 plus the 06-30 unvested common and units gives 1,241,836,858 and $155.2bn; the same-date
  figure is used.) Split factor 1.0.

### THE DEAL CHECK: none live
`sources.deal_filings("0001393818")` returned no deal forms since the annual report of 2026-02-27 and `deal_note` returned
empty. Read on the index: **no 425, S-4, SC TO, SC 13E-3, DEFM14A or PREM14A has ever been filed by this registrant.**
The two 8-Ks with Item 1.01 in the last year are financing: 2025-10-17 (`0001193125-25-242655`, *"an amended and restated
$4.325 billion revolving credit facility"*) and 2025-11-03 (`0001193125-25-262626`, a supplemental indenture for senior
notes). The SC 13D filings in the index are Blackstone's own filings on other issuers. **The quote is not a spread and
buys this company.**

### The perimeter: consolidated funds, the firm's own balance sheet, and the fee business, stated and not blended
The 10-Q, Item 1A, *"Unaudited Consolidating Statements of Financial Condition"* at 2026-06-30, $M:

| | Consolidated Operating Partnerships | Consolidated Blackstone Funds | eliminations | consolidated |
|---|---:|---:|---:|---:|
| Cash | 2,507.1 | 266.2 (*"Cash Held by Blackstone Funds and Other"*) | | 2,773.3 |
| Investments | 30,308.8 | 5,233.8 | (954.9) | 34,587.7 |
| Total assets | 45,071.1 | 5,843.1 | (1,022.0) | 49,892.2 |
| Loans payable | 13,070.8 | 123.9 | | 13,194.7 |
| Total liabilities | 27,123.8 | 404.8 | (69.5) | 27,459.0 |
| NCI in consolidated entities (incl. redeemable) | 4,022.4 | 4,452.9 | | 8,475.4 |

- **The consolidated funds are small** (12% of assets). The FY2025 MD&A: *"The consolidation of these Blackstone Funds
  has no net effect on Blackstone's Net Income or Equity"*; *"Blackstone's share of Investments of Consolidated
  Blackstone Funds totaled 457.1 million"* of their $5,233.8M (10-Q Note 4).
- **The firm's own balance sheet is not small.** 10-Q Note 4, investments at 2026-06-30, $M: **Accrued Performance
  Allocations 13,906.8** (carried interest accrued on marks and not yet paid; a large part is owed on to employees,
  inside accrued compensation of $6,844.2M); **Partnership Investments 6,535.5** (GP and co-investment stakes, equity
  method); **Other Investments 8,510.2** (proprietary; at 2025-12-31 the MD&A counted *"$7.1 billion in Other
  Investments (which included $6.5 billion of liquid investments)"*); Corporate Treasury Investments 401.5. Against it:
  **loans payable $13,070.8M** at the operating partnerships (*"$12.4 billion in borrowings from our bond issuances"* at
  2025-12-31, and *"In February 2026, we drew $900.0 million under the Revolving Credit Facility"*, FY2025 MD&A).
  **The price therefore buys a fee business, a claim on carried interest, and a leveraged book of investments; Q1 and
  Q4 keep them apart.**

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, fiscal year ended 2025-12-31, filed **2026-02-27**, accession **`0001193125-26-082531`**
  (`10K_FY2025.txt`; Part III is inside the 10-K: the company files no proxy statement, Q3).
- **Q2 2026 Form 10-Q**, quarter ended 2026-06-30, filed **2026-08-07**, `0001193125-26-340208`; Q1 2026 10-Q
  `0001193125-26-214609`.
- Also read: FY2020-24 10-Ks (`0001193125-21-060361`, `-22-054433`, `-23-048733`, `-24-044485`, `-25-042469`) for the
  FY2018-25 statements; the 8-Ks and Form 4s named in this file.
- **Figures cross-checked against the filed statement** (FY2025 10-K consolidated statements of cash flows and of
  operations, $K, FY2025 / 2024 / 2023): *"Net Cash Provided by Operating Activities 4,663,161 3,481,662 4,056,906"*,
  *"Equity-Based Compensation Expense 1,445,352 1,168,435 987,549"*, *"Purchase of Furniture, Equipment and Leasehold
  Improvements ( 115,703 ) ( 61,409 ) ( 224,231 )"* and *"Total Revenues 14,450,265 13,229,968 8,022,841"* match
  companyfacts to the thousand. **Two lines inside operating cash are not operating in the ordinary sense**:
  *"Investments Purchased ( 3,807,149 ) ( 2,429,824 ) ( 5,010,341 )"* and *"Cash Proceeds from Sale of Investments
  6,679,186 4,342,636 7,189,240"*; they carry the firm's own and the consolidated funds' investment activity, and
  realized carried interest, which the reconciliation first removes (*"Net Realized Gains on Investments ( 4,820,209 )"*),
  can only come back through the second. Q4 takes them apart.
