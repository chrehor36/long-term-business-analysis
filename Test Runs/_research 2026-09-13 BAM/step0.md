## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.35%** · date **2026-09-11** (latest print; 09-12 and 09-13 are a weekend) · source
  **US Treasury daily par yield curve, 30-year** (issuing authority), struck fresh through
  `tools/sources.py:sovereign("USD")` on 2026-09-13. It agrees with the brief's figure; it was
  not inherited from it.
- **Earnings currency USD, established from the filing.** Reporting currency USD (10-K FY2025,
  "presented in U.S. dollars"). Item 7A: *"a majority of our private funds are denominated in USD.
  This means that a majority of the Fee Revenues that we earn are paid in USD, irrespective of the
  local currency of our underlying investment base. Additionally, the majority of our revenues are
  earned in the U.S."* FY2025 management and advisory fees by geography (MD&A): United States
  $2,551M, United Kingdom $943M, Canada $764M, Other $668M, plus $561M of incentive distributions
  from BIP/BEP/BBU. The 8-K of 2026-08-14 (`0001104659-26-097349`): 49% of AUM and ~50% of LTM
  capital raised are US-sourced. **The non-US legs are real (UK 17%, Canada 14% of management
  fees) and are disclosed, not blended; the reporting-currency sovereign is used, per the WTM open
  question (SECTOR METHOD, Finding 8).**
- FX: none needed — the NYSE line is USD. **Jurisdiction [E3-66]:** a British Columbia
  corporation, head office New York, co-listed TSX. Dividends to a US holder carry Canadian
  withholding tax at 25%, reduced to 15% under the Treaty (10-K Item 5). Stated, not priced.

**Price and share count — re-struck, not inherited:**
- Price **$47.26**, 2026-09-11 close (`sources.price("BAM")`, Yahoo chart API — **aggregator,
  flagged, live quote only**). No split after the measurement date (`split_factor_after` = 1.0).
- **Share classes, from the cover and the charter note.** Two classes: **Class A Limited Voting
  Shares** (NYSE/TSX: BAM) and **Class B Limited Voting Shares, 21,280, all held by BAM Partners
  Trust** (10-K Item 5: *"The BAM Partnership is the sole holder of the Class B Shares
  outstanding"*). Both participate in dividends (two-class EPS method; dividends *"Per Class A
  Share and Class B Share"* $1.75 in 2025). Class B is economically trivial (21,280 x $47.26 =
  $1.0M) and is counted.
- **Cover count confirmed: 1,597,230,353 Class A and 21,280 Class B at 2026-08-06**, 10-Q for the
  period ended 2026-06-30, filed 2026-08-10, accession `0001628280-26-054933` (balance sheet:
  1,638,280,619 issued, **1,597,215,738 outstanding**, 41,064,881 in treasury at 2026-06-30).
  **This cover post-dates the Oaktree close of 2026-07-31** and moved only +14,615 shares from the
  June balance sheet.
- **A COVER-DEFINITION BREAK, found by reading both covers.** The 10-K cover (filed 2026-03-02,
  `0001628280-26-013098`) reports **1,638,147,590 Class A at 2026-02-23 — the ISSUED count,
  including ~29.5M+ treasury shares** held by escrowed-stock-plan subsidiaries (balance sheet
  2025-12-31: 1,637,942,656 issued, 1,608,492,642 outstanding). The 10-Q cover reports the
  OUTSTANDING count. BN's 13D/A (`0001104659-26-040030`, 2026-04-06) also computes its percentage
  on the issued 1,638,131,687. **A screen reading the two covers in sequence sees a 40.9M-share
  (2.5%) fall and reads a buyback that is mostly a definition change** (actual net treasury
  acquisitions H1 2026: 11,614,867 shares, $592M, equity statement).
- **BN's holding is INSIDE the count.** **1,193,021,145 Class A shares** held by Brookfield
  Corporation through subsidiaries and by Brookfield Wealth Solutions (BNT) and its subsidiaries
  (13D/A Item 5(a); 10-K Item 12: *"Brookfield Corporation owns or controls approximately 73% of
  BAM, which includes approximately 4% held by subsidiaries of BWS"*). **74.7% of the outstanding
  count** (72.8% of issued). These are economic Class A shares, identical to the float.
  **65,000,000 of them are pledged** under a US$1.0bn RBC margin loan to BWS BAM Financing LP,
  maturing 2028-04-02 (13D/A Item 4).
- **Count used: 1,597,251,633 economic shares** (Class A outstanding 1,597,230,353 + Class B
  21,280). **Cap = $47.26 x 1,597,251,633 = $75,486M.** The public float is ~404M shares
  (~$19.1bn); **a cap computed on the float would understate the company by 75%** — the public-
  float guard's reason for existing. Diluted: weighted-average diluted shares Q2 2026 1,612.5M
  (escrowed stock and options, +14.9M), cap ~$76.2bn.

**The filing was read** — not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **10-K FY2025**, filed 2026-03-02, accession `0001628280-26-013098` (Items 1, 5, 7 incl. Key
  Measures, Fee-Bearing Capital, DE and the GAAP-to-non-GAAP reconciliation, Liquidity,
  Contractual Obligations; Item 7A; Item 8 statements; Notes 1-2 (organization, tracking shares,
  consolidation, revenue); the auditor's report incl. both critical audit matters; Items 11-13).
- **10-Q Q2 2026**, filed 2026-08-10, `0001628280-26-054933` (statements; equity statements;
  Note 17 subsequent events; FBC and DE tables; share repurchases).
- **10-K FY2024**, filed 2025-03-17, `0001937926-25-000007` — **the first 10-K under this CIK,
  not the 10-K of 2026-03-02 as the brief's pre-check said** (it followed an NT 10-K of
  2025-03-03) — and its **EX-99.1** (audited consolidated and combined statements of **Brookfield
  Asset Management ULC**, FY2022-FY2024) and **EX-99.2** (audited combined statements of the
  **Oaktree Asset Management Operating Group**, FY2022-FY2024). 10-K FY2025 **EX-99.1** fetched.
- **8-K 2025-02-05** (`0001104659-25-009249`, Items 1.01, 2.01, 3.02, 3.03, 5.01, 5.03, 5.07,
  7.01) and EX-99.1 — the 2025 Arrangement. **8-K 2026-08-03** (`0001104659-26-089471`, Item 2.01)
  and EX-99.1 — the Oaktree close. **8-K 2026-04-17** (`0001104659-26-044893`, Items 1.01/2.03).
  **8-K 2026-09-08** (`0001171843-26-005900`, Item 8.01) and EX-99.1. **8-K 2026-08-14**
  (`0001104659-26-097349`, Item 7.01). **8-K EX-99.1 Q2 2026 results release**
  (`0001171843-26-005272`). **Schedule 13D/A** 2026-04-06 (`0001104659-26-040030`).
- **Figure cross-checked against the filed statement:** FY2025 cash from operating activities
  **$2,101M** on the 10-K cash-flow statement = companyfacts
  `NetCashProvidedByUsedInOperatingActivities` 2,101,000,000 (accession `0001628280-26-013098`).
  FY2025 stock-based equity awards **$123M** (cash-flow add-back) = `ShareBasedCompensation`
  123,000,000. FY2025 distributions to common stockholders **$2,818M** = `PaymentsOfDividends`
  2,818,000,000. H1 2026 operating cash **$883M** on the 10-Q.

### THE TWO PROMPTS, OPENED
- **`deal_note` (one 8-K Item 1.01 since 2026-03-02, no EX-2.1) — OPENED: a notes offering.**
  8-K 2026-04-17: US$550M 4.832% senior notes due 2031 and US$450M 5.298% notes due 2036 (a
  re-opening of the $400M series), unsecured, lien covenant only, 101% change-of-control offer.
  **Not a merger.** The prompt was right that it is not a merger and **silent on the transaction
  that does change the perimeter** — the Oaktree close was filed under **Item 2.01** (8-K
  2026-08-03). The Oaktree **Transaction Agreement of 2026-04-14 is incorporated by reference as
  Exhibit 2.1 from Brookfield Oaktree Holdings, LLC's 8-K** (10-Q exhibit index), a different
  registrant — which is exactly why this CIK carries no EX-2.1.
- **8-K 2026-09-08 (`0001171843-26-005900`) — OPENED: a press release, Item 8.01.** The UK
  Nuclear Liabilities Fund selected Brookfield's Investment Solutions Group for a multi-asset
  mandate, **initial $1bn commitment**, proceeds *"expected to be reinvested … rather than
  routinely distributed"*. Immaterial to the perimeter (0.15% of $672bn Fee-Bearing Capital); it
  is Q2 evidence of a mandate won *"Following a competitive selection process"*.
- `name_change_note` returned nothing; confirmed — `formerNames` is empty in the submissions index.

### THE PERIMETER, FROM THE FILINGS — every reorganisation, dated
| date | event | what one BAM share owned | source |
|---|---|---|---|
| to 2022-12-09 | the asset management business sits **inside Brookfield Asset Management Inc. (now BN)**; carve-out statements only | no BAM shares exist | ULC EX-99.1 Note 1 (*"combined standalone basis … derived from the consolidated and combined financial statements and accounting records of BN"*) |
| 2022-07-04 | BAM Ltd and Brookfield Asset Management ULC incorporated (British Columbia) | — | 10-K FY2025 Note 1; ULC Note 1 |
| **2022-12-09** | **2022 Arrangement**: BN transfers its asset management business into the ULC and **25% of the ULC to BAM Ltd**, distributed to BN holders; Relationship Agreement (BN: 100% of mature-fund carry, 33.3% of new-fund carry); BUSHI/BMHL tracking shares issued to BN | **~25% (later ~27%) of the ULC**, equity-accounted | ULC EX-99.1 Note 1; 10-K FY2025 Items 1, 13 |
| 2023-2025 | BAM Ltd files a 20-F (FY2022, `0001937926-23-000004`), a 40-F (FY2023, `0001937926-24-000004`), then a 10-K (FY2024) as the ~27% holder | ~27% of the ULC | submissions index |
| **2025-02-04** | **2025 Arrangement**: BAM acquires BN's ~73% of the ULC for **1,194,021,145 new Class A shares**, one-for-one; BN ends at ~73% of BAM; board-election rules amended (A and B vote as one class while BN > 50%); BAM voluntarily moves to 10-K/10-Q/8-K | **100% of the asset manager** (subject to the carry split below) | 8-K `0001104659-25-009249`; 10-K FY2025 Note 1 |
| 2025-10-02 | Angel Oak, 51.3% economic interest, ~$149M cash | + | 10-K FY2025 Item 1 |
| **2026-07-31** | **Oaktree**: Brookfield acquires the remaining ~26% for ~$3.0bn of cash and BN/BAM shares, **~$2.2bn attributable to BAM**; **BAM obtains control** — equity method to that date, consolidated after it | + the Oaktree remainder; BAM's post-step economic share is not stated in the 10-Q | 10-Q Note 17; 8-K `0001104659-26-089471` |

**What the share buys today, from the filings: 100% of Brookfield Asset Management ULC (since
2025-02-04), which keeps 100% of base management fees, advisory fees and incentive distributions,
66.7% of carried interest on new and open-ended funds (BN takes 33.3%) and 0% of carried interest
on mature funds (BN takes 100%, through BUSHI tracking shares)**, plus equity-method stakes in
partner managers (Castlelake 51% of FRE, LCM 49.9%, Primary Wave 44% then +6% on 2026-07-01,
Angel Oak 51.3%, Pretium ~11%) **and, since 2026-07-31, control of Oaktree.** BN also holds BUSHI
preferred shares (class B senior preferred, $1.36375/yr cumulative; class B preferred, 6.7%
non-cumulative; class A preferred) — **$1,238M of preferred shares redeemable NCI at 2026-06-30
ranks ahead of the Class A holder.**

**THE FILED HISTORY OF THE 100% BUSINESS IS LONGER THAN THE CIK, AND SHORTER THAN FIVE YEARS.**
Because the ULC was the accounting acquirer in 2025, the 10-K FY2025 presents **the ULC as
Predecessor**: FY2023, FY2024 and FY2025 are the whole business on one perimeter. **FY2022 exists
(ULC EX-99.1) but is a separation year** — operating cash **−$374M** after a $7,396M due-to-
affiliates settlement and a $5,155M contribution from parent; the statements say they *"may not be
indicative of what they would have been had the Company been an independent standalone entity"*.
**Pre-2022 carve-out statements are in the F-1/424B3 of 2022-11-21 (`0001193125-22-289950`)**, on
costs allocated inside BN.

**COMPANYFACTS SPLICE — A FOURTH MECHANISM, stated so a tool can be fixed.** Under this CIK,
`NetCashProvidedByUsedInOperatingActivities` holds **both entities under the same period keys**:
BAM Ltd as a 27% holder (FY2023 **$508M**, FY2024 **$627M**; accessions `0001937926-24-000004`,
`0001937926-25-000007`) and the ULC-as-Predecessor restatement (FY2023 **$1,439M**, FY2024
**$1,612M**; `0001628280-26-013098`). **`sources.annual()` at its default `vintage="earliest"`
returns {2023: 508, 2024: 627, 2025: 2,101} — a 27% holding company spliced onto the 100%
business, a 3.4x step that is a perimeter change, not growth.** The same split holds for
`ShareBasedCompensation` (6 / 3 against 33 / 103) and `PaymentsOfDividends` (505 / 630 against
2,101 / 2,478). `tools/run.py BAM` (which uses `newest`) returned *"no overlapping OCF/D&A/capex
annual facts. UNRESEARCHED"* — D&A exists only in the newest filing and no capex tag resolves.
**No companyfacts row is used below; every figure is from the filed statements.** Same class as
NEGG's splice and RGTI's colliding de-SPAC keys; a different mechanism — **a predecessor
restatement filed by a registrant that had been the minority holder.**

**THE BLOCK OF 2026-09-02, TESTED.** The queue's note called BAM a *"different perimeter problem,
closer to the DKS/HON class"*. What the filings show: (1) the 2025 perimeter change is **fully
restated** — the Predecessor presentation gives three consistent years of the whole business;
(2) **consolidated funds are small and separately captioned** — BSI II at $505M of investments at
2025-12-31, $3,090M at 2026-06-30, each with its own revenue, expense, borrowing, cash-flow and NCI
lines, so they can be stripped; (3) **BN's carry share is separately captioned** (NCI in
consolidated entities; preferred shares redeemable NCI); (4) Oaktree was equity-accounted, with its
own audited statements filed as exhibits. **The perimeter is MEASURABLE from filings. The block was
a scheduling judgment, not a measurement finding.** Two things the block anticipated are real and
are carried forward: **a five-year window on one perimeter does not exist** (three clean years plus
H1 2026), and **the perimeter moved again on 2026-07-31** when BAM took control of Oaktree, whose
consolidation enters the statements from Q3 2026.
