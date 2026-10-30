# Company Run — Snowflake Inc. (SNOW) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **This is a NEW NAME, not a
holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.**

Filled top to bottom. **Stop at the first verdict that is not IN.** Run unattended from scratch. No prior
run file for SNOW exists; the PLTR run of 2026-09-11 used Snowflake as a data-platform comparator, and every
SNOW figure below is recomputed from Snowflake's own filings. WAVE 5, the second of the seven "perimeter or
restatement above threshold" names. Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-18 SNOW/`.

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
The wave 5 row is *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list
says *"revenue step or cross-accession restatement above threshold."* **A prompt to read, never a verdict.**

**Which code produced the label.** The wave 5 table was written at `a8bc84f` (2026-09-01 22:15). The watchlist
triage itself ran at `ce98258` (2026-09-01 20:53) *"through the same pipeline as the sweep"* (reading list,
WATCHLIST TRIAGE section). The watchlist harness was not committed (`ce98258` carries only the CSV, the reading
list, `floor_screen.py` and `tools/resume_ping.py`), so the guard ORDER is read from the sweep's
`Screens/new_candidates.py` at `ce98258` (identical at `a8bc84f`), and the guard FUNCTIONS from
`floor_screen.py` at `a8bc84f` (`floor_screen_a8bc84f.py` in the research folder). The order is:
(1) `share_count_shift` outside **0.75-1.50x** returns "perimeter"; (2) `scale_shift` **> 2.0** returns
"perimeter by revenue step"; (3) `filed_years < 5`; (4) `owner_earnings() == "CAPEX_UNRESOLVED"`.
**`restatement_shift` is not called anywhere in that pipeline** (grepped at both commits): it exists as a
function and never gates a name. Reproduction, on companyfacts cut to facts filed by 2026-09-01
(`triage_repro.py`, output `triage_repro_out.txt`):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | **1.034x** | no (inside 0.75-1.50) | ordinary issuance net of buybacks; no split in the window (`split_factor_after` 1.0) |
| **2. `scale_shift`** | **2.0595x** | **YES, at the 2.0x line: THIS IS THE GUARD THAT RETURNED SNOW UNPRICED** | **FY2021 revenue $592.0M to FY2022 $1,219.3M**, the oldest pair in its six-year window (every later step is 1.29-1.69x). **Organic, on the face of the filing**: the FY2022 10-K cash-flow statement shows *"Cash paid for business combinations, net of cash acquired — ( 6,035 ) ( 6,314 )"* for FY2022, FY2021 and FY2020, i.e. **zero** in FY2022. Snowflake's first acquisition of size (Streamlit, $362.6M cash plus $438.9M of stock) closed in FY2023, the year AFTER the step. |
| 3. `filed_years` | 8 | no | |
| 4. `owner_earnings` | 5y D&A **-$527M**, 5y capex **-$450M** | no (priced, and negative) | the triage stopped at guard 2 and never reached this |
| (`restatement_shift`, not a guard) | (1.0, FY2020) | n/a | **a null**: only one revenue element carries data (`RevenueFromContractWithCustomerExcludingAssessedTax`, 18 annual observations; the other three `REV_TAGS` carry none), and every period end agrees across accessions |

**So the label was, for SNOW: a genuine revenue DOUBLING that was ORGANIC (the 2.0x line is a merger proxy, and
a 106% growth year trips it), with no perimeter event and no restatement.** Checked for a restatement on the
documents as well as in the tags: the FY2026 10-K cover leaves both error-correction boxes unticked (*"reflect the
correction of an error to previously issued financial statements. ☐"*); the filing index shows **no 10-K/A or
10-Q/A** in the company's history (`filings_list.txt`, `filings_list_old.txt`); and the FY2020-FY2026 revenue,
operating-cash and SBC figures read off the FY2022, FY2023 and FY2026 10-K faces agree with companyfacts to the
thousand. **The step leaves the window by itself**: when the FY2027 10-K is filed, FY2021-22 drops out of
`scale_shift`'s six years and the guard would pass at 1.69x. **The perimeter events that DO matter are newer than
any guard read and run the other way**: acquisitions paid substantially in stock (FY2023-FY2027, below), and
$2.3bn of convertible notes now deep in the money (below).

**What the current screen says behind the label (tagged data, a prompt only):** `owner_earnings()` prices SNOW and
returns **negative owner earnings at every end** (5y D&A -$527M, 5y capex -$471M, 3y D&A -$580M, 3y capex
-$488M), because stock compensation exceeds operating cash in every year. `working_capital_flag` fires on FY2022
*"ContractWithCustomerLiability moved 478% of 2022 OCF"* (deferred revenue +$526.2M against operating cash of
+$110.2M): taken up at Q4. SBC resolves for every year and the face line is *"Stock-based compensation, net of
amounts capitalized"*, so it is **not complete** on its own: the capitalised part is a separate supplemental line
(taken up at Q4).

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.29%** · **09/17/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority.** Struck by
  this run: `tools/sources.sovereign("USD")` returned `(5.29, '09/17/2026', 'US Treasury daily par yield curve')`
  on 2026-09-18 (`step0_out.txt`). Not inherited from the brief; 09/17 is still the newest row published, so it
  is the same figure the SMCI run struck. FRED was not used.
- **Earnings currency: USD.** FY2026 10-K Item 7A: *"The majority of our sales are currently denominated in U.S.
  dollars, although we also have sales in Euros and, to a lesser extent, in British pounds, Australian dollars,
  Canadian dollars, Brazilian reals, and Indian rupees."* Revenue by customer location FY2026: United States
  $3,524.0M of $4,683.9M (75.2%). No FX or ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$338.39, the close of 2026-09-17**, the last completed close. Source: Yahoo Finance daily chart via
  `sources._chart("SNOW", rng="1mo")` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`).
  Bar: open 334.00, high 344.66, low 328.77, close 338.39.
- **`tools/sources.price()` was NOT used for the struck price.** It returned `(332.835, '2026-09-18', 'USD')`,
  the intraday `regularMarketPrice` stamped with today's date, while its docstring says *"Latest close."* **The
  TOST, EQIX, DLR and SMCI defect reproduces on a fifth name.**
- Recent closes: 09-10 $329.72 · 09-11 $328.99 · 09-14 $332.35 · 09-15 $322.98 · 09-16 $331.02 · 09-17 $338.39.
  The Q2 release day moved the stock: 09-02 close $305.84, 09-03 open $377.24 and close $356.47.
- **Primary-filing cross-check of the aggregator, three Form 4s:** accession `0002127025-26-000007` (Jonathan
  Beaulier) reports tax withholding at **$332.35** on 2026-09-15, which is exactly Yahoo's 09-14 close, and an
  open-market sale on 2026-09-16 at a weighted **$336.124** (*"ranging from $335.888 to $336.140"*), inside
  Yahoo's 09-16 bar (low $317.45, high $338.00); `0001821737-26-000014` (Benoit Dageville) the same $332.35
  withholding price; `0001640147-26-000038` (Christian Kleinerman) withholding at **$337.18** on 2026-09-08,
  exactly Yahoo's 09-04 close, and a 10b5-1 sale on 09-09 at $335.72 inside that day's range ($331.00-$339.59).
  **The aggregator series is corroborated by primary documents.**
- **Split factor after the count's date: 1.0** (`sources.split_factor_after("SNOW", "2026-08-21")`). `close`
  used, never `adjclose`.

### The share count: from the cover, with the accession
- **352.8 million shares**, from the cover of the **Q2 FY2027 Form 10-Q** (quarter ended 2026-07-31, filed
  **2026-09-04**, accession **`0001640147-26-000037`**): *"As of August 21, 2026, there were 352.8 million shares
  of the registrant's common stock, par value of $0.0001 per share, outstanding."* One class of common stock;
  200,000 thousand preferred authorised, *"zero shares issued and outstanding"*.
- **The filer rounds its cover to the hundred thousand**, and no exact count exists on the cover. The balance
  sheet is in thousands: *"352,836 and 344,317 shares issued as of July 31, 2026 and January 31, 2026,
  respectively; 352,455 and 343,918 shares outstanding"*, with 381 thousand in treasury. **ERIC trap checked**:
  the cover says "outstanding"; the balance-sheet outstanding figure three weeks earlier is 352.455M, and the
  cover's 352.8M is consistent with three weeks of RSU vesting. **SPGI trap checked**: no exclusion clause.
- **`Screens/cover_shares.py SNOW` returned a broken figure: `1,640,147,000,000` shares.** Reading the same
  `R1.htm` by hand shows why: the row runs *"Entity Common Stock, Shares Outstanding 352.8 Entity Central Index
  Key 0001640147"*, the renderer header says *"shares in Millions"*, and the tool took the CIK that follows the
  count, scaled by a million. Tooling note at the audit; the count here is read off the document.

### The perimeter between the business and the common holder: stated, not blended
1. **Convertible senior notes, deep in the money.** 10-Q Note 10: $1.15bn of 0% notes due 2027-10-01 and $1.15bn
   due 2029-10-01, each at *"Initial Conversion Price $ 157.50"*, **7,302 thousand shares per series, 14.604M in
   total**; the company *"may choose to pay or deliver, as the case may be, cash, shares of our common stock or a
   combination of cash and shares of our common stock, at our election"*. Capped calls reduce dilution *"subject
   to a cap based on a cap price initially equal to $ 225.00 per share"*. **At $338.39 the notes' if-converted
   value is 14.604M x $338.39 = $4,941.9M against $2,300M of principal; the capped calls return at most 14.604M x
   ($225.00 - $157.50) = $985.8M; the notes' net claim on the equity is therefore about $3,956M, or about 11.7M
   shares at the struck price (+3.3%).** Treatment: shown as a perimeter-consistent cap beside the plain one,
   and the notes are then not also deducted as debt. The 10-Q says conversions of the 2027 Notes through July 31,
   2026 were *"not material"*.
2. **Acquisitions paid in stock, inside and after the window.** Cash paid for business combinations FY2022-26
   **$847.5M** (0; 362.6; 275.7; 30.3; 178.9) plus stock issued **$714.0M** (438.9 FY2023; 174.3 FY2024; 87.7
   FY2025; 13.1 FY2026); and in H1 FY2027 alone **$254.4M cash plus $420.6M of "Non-cash consideration for
   business combinations"** (goodwill $1,194.4M to $1,639.0M in six months). Taken up at Q3 and Q4.
3. **Cash and investments at 2026-07-31: $4,329.2M** (cash $1,707.2M, short-term $637.5M, long-term $1,984.5M);
   no bank debt; strategic equity investments carried in other assets.

### The market cap
- **$338.39 x 352.8M = US$119,384M ($119.4bn).** Split factor after 2026-08-21 = 1.0.
- **Perimeter-consistent, with the convertibles' net claim: US$123,340M** ($119,384M + $3,956M), the notes then
  not deducted as debt. Displayed side by side, not blended.

### LIVE-DEAL CHECK: run by this run, not inherited
- `sources.deal_filings("0001640147")` returned `([], [], '2026-03-20')` and `deal_note` an empty string: no
  DEFM14A, PREM14A, S-4, SC 14D9, SC TO-T or 425.
- The full EDGAR submissions index was read (`filings_list.txt`): every 8-K since the FY2026 10-K carries Items
  7.01, 2.02, 5.07 or 5.02; **no Item 1.01 since the 2024-09-23 convertible-note 8-K**, no SC TO, no SC 13D. **The
  quote is an owner-earnings price, not a spread.**

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2026 Form 10-K**, fiscal year ended 2026-01-31, filed **2026-03-20**, accession **`0001640147-26-000008`**
  (`10K_FY2026.txt`); auditor **PricewaterhouseCoopers LLP**, San Jose, report dated March 20, 2026, *"We have
  served as the Company's auditor since 2019."*
- **Q2 FY2027 Form 10-Q**, quarter ended 2026-07-31, filed **2026-09-04**, accession **`0001640147-26-000037`**.
- Also read: 10-Ks FY2025 (`0001640147-25-000052`), FY2024 (`0001640147-24-000101`), FY2023
  (`0001640147-23-000030`), FY2022 (`0001640147-22-000023`), FY2021 (`0001640147-21-000073`); the Q1 FY2027
  10-Q (`0001640147-26-000030`); the DEF 14A of 2026-05-18 (`0001640147-26-000019`); the 8-K EX-99.1 releases
  and Item 5.02 8-Ks named at Q3; and the Form 4s above.
- **Figures cross-checked against the filed statement** (FY2026 consolidated statement of cash flows):
  *"Net cash provided by operating activities 1,221,942 959,764 848,122"*, *"Stock-based compensation, net of
  amounts capitalized 1,599,547 1,479,314 1,168,015"*, *"Purchases of property and equipment ( 101,628 ) ( 46,279
  ) ( 35,086 )"* and revenue *"$ 4,683,946 | $ 3,626,396 | $ 2,806,489"* all match companyfacts exactly. The one
  that does not is capex before FY2026: `annual(CAPX_TAGS)` returns property and equipment only, while the face
  carries a second line, *"Capitalized software development costs — ( 29,433 ) ( 34,133 )"*, which
  `capital_acquired()` adds (Q4).

---
