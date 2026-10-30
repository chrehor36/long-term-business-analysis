## STEP 0: THE SKIP REASON, THE RATE, THE PRICE, THE COUNT, THE PERIMETER, AND THE FILING

### The skip reason, tested on the filing rather than inherited
The wave 5 row is *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list
says *"revenue step or cross-accession restatement above threshold."* **A prompt to read, never a verdict.**

Reproduced by the brief-writer with `Screens/floor_screen.py` as it stood at `a8bc84f` (copied as
`floor_screen_a8bc84f.py`) over companyfacts pulled 2026-09-18 and cut to facts filed by 2026-09-01
(`triage_repro.py`, output `triage_repro_out.txt`, re-read by this run):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | **None** | no, but only because it had nothing to compare | companyfacts carries **no dei share-count element for Rivian at all** (only `EntityPublicFloat`); a None is "not measured", not "stable". The real count moved from 1,237,077,289 Class A (FY2025 10-K cover, 2026-01-29) to 1,443,948,130 (Q2 2026 10-Q cover, 2026-07-21), **+16.7% in six months** (below). |
| **2. `scale_shift`** | **30.1455x** | **YES: THIS IS THE GUARD THAT RETURNED RIVN UNPRICED** | **A REAL STEP, AND IT IS THE START OF PRODUCTION, NOT A PERIMETER.** Revenue $55M (FY2021) to $1,658M (FY2022), on consecutive fiscal years (2021-12-31 and 2022-12-31; the TSLA check for non-consecutive years was run and the pair is consecutive). Deliveries were **920** in FY2021 and **20,332** in FY2022 (FY2023 10-K MD&A: *"Delivery volume | 920 | 20,332 | 50,122"*); the FY2021 10-K says *"the Company began making deliveries of the R1T, R1S, and EDV in the United States in 2021."* The next step, FY2022-23 **2.67x**, is the same ramp (20,332 to 50,122 deliveries). **No acquisition in any year**: the investing section of every 10-K read carries no business-combination line (FY2019-25). FY2019 and FY2020 revenue are true zeros (no product was sold), not a tag hole. |
| 3. `filed_years` | 7 | no | FY2019-25 (FY2019-20 from the FY2021 10-K, the first annual report after the November 2021 IPO) |
| 4. `owner_earnings` | 5y D&A **-$4,489M**, 5y capex **-$5,195M** | no (priced, negative) | the triage stopped at guard 2 |
| (`restatement_shift`, not a guard) | (1.0, FY2021) | n/a | a null, as at SMCI, SNOW and TSLA |

**So the label was, for RIVN: a real organic revenue step, the start of vehicle production in late 2021, measured
off a near-zero base ($55M). Not a perimeter event, not a restatement, not a tag artefact.** Checked on the documents:
the FY2025 10-K cover leaves the error-correction box unticked (*"reflect the correction of an error to previously
issued financial statements. ¨"*); the filing index (`filings_list.txt`, 531 filings) holds **no 10-K/A and no
10-Q/A**; and the FY2021-25 revenue, operating-cash, SBC, D&A and capex figures on the FY2021, FY2023 and FY2025 10-K
faces agree with companyfacts to the million. **The perimeter events that DO matter are newer than the triage's data
and run through the share count** (below), and the guard that would have seen them returned None because the dei
element does not exist.

**What the current screen says behind the label (tagged data, a prompt only):** `owner_earnings()` prices RIVN at
5y D&A end **-$4,489M**, 5y capex end **-$5,195M**; 3y -$4,122M and -$4,527M. `working_capital_flag` fires on 2024
(*"ContractWithCustomerLiability moved 94% of 2024 OCF"*) and `da_discontinuity_flag` on 2021 (D&A $29M to $197M);
both are taken up at Q4. SBC tags FY2019-20 as zero: **the face agrees** (the FY2021 10-K cash-flow statement reads
*"Stock-based compensation | — | — | 570"*), so this is not the SBC-of-zero tag defect of the RESUME STATE note; it is
pre-IPO awards whose expense was deferred until the IPO condition was met (taken up at Q4).

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by
  this run with the cache bypassed (`treasury_out.txt`: *"09/18/2026,3.97,...,5.38,5.34"*). `tools/sources.sovereign("USD")`
  returned the cached **09/17/2026 5.29%** row at 19:12 EDT (`step0_out.txt`), the stale-cache defect SNOW and TSLA
  recorded; the newer issuing-authority figure is used. FRED was not used.
- **Earnings currency: USD.** *"Rivian vehicles are manufactured in the United States and are sold directly to
  consumer and commercial customers"* (Q2 2026 10-Q Note 1); the FY2023 10-K: *"The Company's assets and revenues are
  primarily in the United States."* The quote is in dollars. No FX or ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$14.99, the close of 2026-09-18** (Friday). Source: Yahoo Finance daily chart via `sources._chart("RIVN",
  rng="1mo", max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`). Bar: open 15.445,
  high 15.645, low 14.91, close 14.99, volume 37.1M; `regularMarketTime` 1789761600 = 16:00 EDT, so the figure is the
  closing print. `tools/sources.price()` returned the same 14.99 stamped 2026-09-18.
- Recent closes: 09-11 $16.03 · 09-14 $15.86 · 09-15 $15.54 · 09-16 $15.23 · 09-17 $15.40 · 09-18 $14.99. One-month
  range of closes $14.99-$16.97.
- **Primary-filing cross-check of the aggregator:** Form 4 accession `0001262742-26-000014` (Michael John Callahan)
  reports a 10b5-1 sale of 15,000 shares on **2026-09-11 at a weighted $16.2927** (*"prices ranging from $16.175 to
  $16.52"*), inside Yahoo's 09-11 bar (low $16.01, high $16.81); Form 4 `0001890925-26-000025` (Claire McDonough, CFO)
  reports a sale on 2026-08-20 at $16.00, inside that day's bar ($15.54-$16.18). **Corroborated.**
- **The latest primary prices for issuance sit beside it:** the July 2026 underwritten offering at **$15.50** (10-Q Note
  14), Volkswagen's April 2026 tranche at **$15.90** and Uber's May 2026 purchase at **$15.34** (30-day VWAPs, Note 1).
- **Split factor after the count's date: 1.0** (`sources.split_factor_after("RIVN", "2026-07-21")`). `close` used, never
  `adjclose`.

### The share count: from the cover, with the accession, and the classes read before summing
- **1,447,860,630 shares** = **1,443,948,130 Class A + 3,912,500 Class B**, from the cover of the **Q2 2026 Form 10-Q**
  (quarter ended 2026-06-30, filed **2026-07-30**, accession **`0001874178-26-000054`**): *"As of July 21, 2026,
  1,443,948,130 shares of the registrant's Class A common stock were outstanding, and 3,912,500 shares of the
  registrant's Class B common stock were outstanding."* `Screens/cover_shares.py` was not needed: companyfacts carries no
  dei count, so the cover was read directly.
- **Why the two classes are summed (the charter terms as the 10-Q states them, Note 14):** *"Shares of Class A common
  stock and Class B common stock are identical, except with respect to voting and conversion rights"*; *"the rights of the
  holders of Class A and Class B common stock, including liquidation and dividend rights, are identical"*; every Class B
  share *"will automatically convert into one share of Class A common stock upon the earliest to occur of (a) the
  five-year anniversary of the Company's IPO (i.e., November 2026)"*. The CEO holds all 3,912,500 Class B shares (2026
  proxy, `0001874178-26-000023`). Same economic claim, so the sum is the count.
- **The cover already includes the July 2026 offering**: 75M shares plus the 11.25M option, at $15.50, net proceeds
  about $1,317M (10-Q Note 14, *"On July 7, 2026, the Company entered into an underwriting agreement ..."*); 1,362M at
  June 30 plus 86.25M is 1,448M.
- **Instruments outside the cover count, at $14.99, stated either way:**
  1. **Green Convertible Notes, 149M shares if converted** (2029: $1,500M at $20.13; 2030: $1,725M at $23.29, with
     capped calls). **Out of the money at $14.99; excluded**, and carried as debt at Q4.
  2. **Employee awards:** RSUs 85M (unvested, the future SBC charge), options 77M (weighted exercise $12.35 at
     2025-12-31), warrants 12M (Note 14's anti-dilution table: 327M potential shares in total with the converts).
     Unvested RSUs belong to future SBC, which Q4 subtracts; not added to the count.
  3. **Volkswagen's last equity tranche**: *"$ 460 million in exchange for $ 250 million of the Company's Class A common
     stock"* at a 30-day VWAP, due at the Start of Production Milestone or 2028-01-03 (about 16.7M shares at $14.99).
     The other $210M is booked as JV revenue (Note 3). **Not yet issued; excluded.**
  4. **Uber**: up to **$950M** more across four milestones, *"certain of which require the fulfillment of proven autonomy
     quality"*, paid in **$0.001 warrants or shares** at a 30-day VWAP (about 63M shares at $14.99 if all are met).
     **Contingent; excluded, and recorded at Q3 as serial issuance.**
- **The count moved +16.7% in six months** (1,240,989,789 across both classes at 2026-01-29 to 1,447,860,630 at
  2026-07-21), all by issuance: VW 63M, Uber 20M, the offering 86.25M, employees the rest.

### The perimeter between the business and the common holder: stated, not blended
1. **Cash and short-term investments at 2026-06-30: $5,310M** ($3,592M cash, $1,718M short-term), plus about **$1,317M**
   net from the July offering (after the balance-sheet date). **Debt principal $4,475M**: 2029 convertible $1,500M,
   2030 convertible $1,725M, 2031 Green Secured Notes $1,250M at 10% (*"secured ... on a first-priority basis by
   substantially all assets"*). Nothing drawn on the $1,500M ABL (availability $536M). Net cash before the offering
   about $0.8bn; after it about $2.2bn.
2. **Undrawn government and partner loans:** the DOE loan, amended April 2026, up to **$3,355M plus $315M capitalised
   interest (Note A) and $651M plus $179M (Note B)** for the Georgia plant, conditional on, among other things, *"the
   Sponsor maintaining positive gross margin for certain periods prior to the first advance"* and *"the Borrower
   achieving certain vehicle sales metrics"*; and Volkswagen's **$1,000M** term loan, drawable **2026-10-01 to
   2026-10-30** only. **Neither is drawn**; both are taken up at Q4.
3. **A 50% partner inside the consolidated revenue.** Rivian and Volkswagen Group Technologies, LLC is consolidated,
   with Volkswagen's 50% shown as a noncontrolling interest; it produced **$590M of H1 2026 revenue** and most of the
   gross profit (Q1). **Strategic investments $697M**, of which Mind Robotics was remeasured to $569M on deconsolidation
   (a **$506M non-cash gain** in Q1 2026 other income); Also, Inc. at 35.3%.
4. **Holders who are also counterparties:** Amazon (12.9%, 162.1M shares incl. a warrant, 2026 proxy) is the EDV
   customer; Volkswagen (15.9%, 209,769,645 shares, Schedule 13G/A `0001104659-26-054713`, event 2026-04-30) is the JV
   customer and a lender; Uber is a subscriber and robotaxi partner.
5. **No live deal.** `sources.deal_filings("0001874178")` returned no merger filing and two 8-K Item 1.01s since the
   last annual (2026-03-19, the Uber subscription; 2026-04-30, the amended DOE agreement); no SC 13D, SC TO, S-4 or
   DEFM14A in the filing index (Volkswagen and Amazon file 13Gs). The quote is an owner-earnings price, not a spread.

### The market cap
- **$14.99 x 1,447,860,630 = US$21,703M ($21.7bn).** Split factor after 2026-07-21 = 1.0.
- Net cash of about $2.2bn after the July offering (about 10% of the cap) is shown, not netted.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, fiscal year ended 2025-12-31, filed **2026-02-12**, accession **`0001874178-26-000008`**
  (`10K_FY2025.txt`); auditor **KPMG LLP**, Detroit, report dated February 12, 2026, unqualified, internal control
  effective, *"We have served as the Company's auditor since 2021."* Critical audit matter: the warranty reserve
  ($463M), *"due to the Company's limited history of vehicle sales."*
- **Q2 2026 Form 10-Q**, quarter ended 2026-06-30, filed **2026-07-30**, accession **`0001874178-26-000054`**; Q1 2026
  10-Q `0001874178-26-000035`.
- Also read: 10-Ks FY2024 (`0001874178-25-000007`), FY2023 (`0001874178-24-000014`), FY2022 (`0001874178-23-000009`),
  FY2021 (`0001874178-22-000008`, which carries FY2019-20); the 2026 DEF 14A (`0001874178-26-000023`, filed 2026-04-27);
  the 8-K EX-99.1 releases named at Q3; Schedule 13G/As; and the Form 4s above. The IPO prospectus is the 424B4 of
  2021-11-12 (`0001193125-21-328239`); the FY2021 10-K states the IPO (*"approximately 176 million shares of Class A
  common stock at a public offering price of $ 78.00 per share"*, November 2021), which settles the brief's first
  unverified belief.
- **Figures cross-checked against the filed statement** (FY2025 consolidated statement of cash flows): *"Net cash used
  in operating activities | ( 4,866 ) | ( 1,716 ) | ( 779 )"*, *"Stock-based compensation expense | 821 | 692 | 741"*,
  *"Capital expenditures | ( 1,026 ) | ( 1,141 ) | ( 1,710 )"* and *"Depreciation and amortization | 937 | 1,031 | 784"*
  match companyfacts to the million. **SBC is complete on the face**: the FY2025 MD&A allocates it $43M + $68M + $306M
  + $324M = $741M across cost of revenues, R&D and SG&A, and no capitalised SBC is disclosed.
