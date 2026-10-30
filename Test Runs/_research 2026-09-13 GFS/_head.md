# Company Run — GLOBALFOUNDRIES Inc. (GFS) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**Queue context.** A name in **WAVE 5** of `Screens/WATCHLIST RUN QUEUE.md` (the unpriced watchlist businesses), the ninth
of the eleven foreign 20-F filers to be run (after TM, SONY, HMC, TSM, UMC, ERIC, SPOT, and alongside a concurrent STLA run).
The 2026-09-01 triage skipped it as *"foreign 20-F filer ... short XBRL history."* **Read here as UNLABELLED: a prompt to read the
20-F by hand, not a verdict.** The run file was created from the template before any fetch (write-early protocol). Research on
disk: `Test Runs/_research 2026-09-13 GFS/`. **The TSM and UMC runs of the same morning were read in full before anything was
built here; their foundry competitor row, their [E4-04], [E3-03](2) and [E2-44] readings and their survival shapes are precedent,
not conclusions: GlobalFoundries has a different business mix (specialty processes, no leading edge, fabs in the US, Germany and
Singapore, government funding, a controlling shareholder), and every figure below is taken from GFS's own filings.**

**Why the screen could not price it, found rather than assumed.** `companyfacts` (fetched 2026-09-13) carries namespaces **`dei`,
`ifrs-full` (260 tags) and `srt` only; no `us-gaap`**. GlobalFoundries reports under **IFRS as issued by the IASB, in US dollars**
(20-F FY2025 cover: *"International Financial Reporting Standards as issued by the International Accounting Standards Board ☑"*;
Item 5.E: *"prepared in accordance with International Financial Reporting Standards ("IFRS")"*). Measured (`facts_probe.py`):
`ifrs-full:CashFlowsFromUsedInOperatingActivities`, `PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities`,
`AdjustmentsForSharebasedPayments` and `DepreciationAndAmortisationExpense` each carry **unit USD, annual periods 2019-12-31
to 2025-12-31 (seven), from five 20-F accessions, including the FY2025 20-F `0001709048-26-000022`.**
- **The USD-only unit filter is NOT the cause** (the unit is USD).
- **companyfacts lag is NOT the cause** (FY2025 is ingested), unlike TM, TSM and UMC.
- **The cause is the tag names:** `tools/run.py GFS` returns *"GFS: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED."*
  because its lists carry only US-GAAP element names (`NetCashProvidedByUsedInOperatingActivities`), and `sources.annual()`
  searches `ifrs-full` with those same names. **ERIC's diagnosis, confirmed on a USD filer where the other two causes are absent.**
- **"Short history" is partly true and is not the reason:** seven annual cash-flow periods exist (2019-2020 as comparatives in
  the first 20-F, filed after the **October 2021 IPO**), which covers the framework's five-year default [E2-42] but not a ten-year
  window. **What that does to the width is stated at Q4.**

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
## STEP 0 — THE RATE, AND THE FILING

### The earnings currency, established from the filing
- 20-F FY2025 Item 3.D: *"The majority of our sales are denominated in U.S. dollars, and therefore, our revenue is not subject to
  foreign currency risk."* Item 11: *"we have costs, assets and liabilities denominated in foreign currencies, primarily the Euro,
  the Singapore dollar and the Japanese yen"*, hedged with forwards.
- Presentation currency US dollars; revenue by customer headquarters 2025: **United States $3,395M (50.0%)**, EMEA $1,710M, Other
  $1,686M (Note 31). Non-current assets 2025: **Singapore $4,364M, United States $3,608M, Germany $2,137M**, other $488M.
- Cash at 2025-12-31: United States $1,133M, Singapore $436M, other $240M (Note 6).
- **The judgment [E4-15, E3-32]:** revenue billed in dollars, statements in dollars, quote in dollars, cash mostly in the United
  States. **The USD sovereign is the natural pairing**, and no currency conversion enters any yield below. The euro and Singapore
  dollar cost base is a margin exposure, carried to Q4, not a reason to change the rate.

### Sovereign — struck fresh 2026-09-13 through `tools/sources.py` [E4-15, E3-32]
- **Rate used: USD 30-year 5.35%**, US Treasury daily par yield curve, **09/11/2026** (the issuing authority; `sources.sovereign("USD")`
  returned `(5.35, '09/11/2026', 'US Treasury daily par yield curve')`). The brief's 5.35% is confirmed, not inherited.
- **The [E4-28] floor of roughly 10% governs above it** (*"that's true whether short rates are 6 percent or whether short rates are
  1 percent"*).
- FX: none needed (USD earnings, USD quote). ADR: none (ordinary shares listed directly on Nasdaq, 20-F cover: *"Ordinary shares, par
  value US$0.02 per share | GFS | The NASDAQ Global Select Market"*).

### The share count, read by hand and walked forward — the issued-versus-outstanding trap checked explicitly
| date | count | what the filing says | document · accession |
|---|---|---|---|
| 2024-12-31 | 552,912,823 | *"555,888,455 and 552,912,823 shares issued and outstanding as of December 31, 2025 and 2024"* | 20-F FY2025 balance sheet (F-5) |
| **2025-12-31** | **555,888,455** | cover: *"As of December 31, 2025, 555,888,455 ordinary shares, par value US$0.02 per share, were outstanding."* Balance sheet: the same figure *"issued and outstanding"*; Note 17: *"556 million ordinary shares issued and outstanding"* | **20-F FY2025, `0001709048-26-000022`, filed 2026-02-27** |
| 2026-03-13 | −7,344,840 | *"7,344,840 ordinary shares of which were repurchased by the Company at a price equal to the price paid by the underwriters of $40.8450 per share"* (from Mubadala, inside its secondary offering) | 6-K 2026-03-13, `0001709048-26-000043` |
| 2026-03-13 | 549,072,416 | *"549,072,416 ordinary shares ... issued and outstanding as of March 13, 2026"* (information the issuer gave Mubadala) | Mubadala Schedule 13G/A No. 2, `0001140361-26-016895` |
| H1 2026 | about −2.3M | *"the Company repurchased an additional 2.3 million ordinary shares for $ 100 million for a weighted average price of $ 43.88 in open market transactions"* | Q2 2026 interim report, 6-K 2026-08-05, `0001709048-26-000219` |
| 2026-06-01 | 548,700,833 | *"548,700,833 ordinary shares were issued and outstanding"* (AGM record date) | 6-K 2026-06-15, `0001709048-26-000141` |
| **2026-06-30** | **548,751,082** | *"Ordinary shares, $ 0.02 par value, 548,751,082 and 555,888,455 shares issued and outstanding as of June 30, 2026 and December 31, 2025"* | **Q2 2026 interim statements, 6-K 2026-08-05, `0001709048-26-000219`** |
| **agreed 2026-09-03** | **+9,907,399** | *"GF will issue to the DOC 9,907,399 ordinary shares, par value $0.02 per share, of GF (the "Shares"), at an issuance price of $37.85 per share"* | **6-K 2026-09-08, `0001709048-26-000234`** (the latest 6-K) |

- **The ERIC trap, checked, and it does NOT fire.** The cover says *"outstanding"*; the balance sheet says the same number is *"issued
  and outstanding"*; repurchased shares are cancelled, not held in treasury (Note 17: *"On May 28, 2024, our Board of Directors resolved
  to cancel the 3.9 million shares"*; policy, Note 3: *"When the Company repurchases and cancels its own equity shares (treasury
  shares), the amount of consideration ... is deducted against the issued ordinary share capital"*). **Issued equals outstanding at
  every date in the table.** No treasury balance to exclude.
- **Count used: 558,658,481** = 548,751,082 (2026-06-30, filed) + 9,907,399 (the Department of Commerce issuance agreed 2026-09-03).
  **The larger count is used deliberately**: the agreement is signed and the 6-K says the shares *"will"* be issued; no filing
  read confirms the issuance completed by 2026-09-11, and leaving them out would understate the cap by 1.8%. **Arithmetic,
  recorded and not over-read:** 9,907,399 × $37.85 = **$375.0M**, the exact amount of *"an expected $375 million grant by the U.S.
  Department of Commerce, pursuant to a letter of intent"* for the quantum programme (Q2 2026 release, 6-K `0001709048-26-000218`).
  **No filing read states that the shares are the consideration for that grant**; the match is arithmetic only. Carried to Q3 and Q4.
- **Not in the count, stated:** open-market repurchases after 2026-06-30 under the *"approximately $ 100 million"* left on the
  authorisation (at most ~2.1M shares at $46.95; no filing reports any); 8.7M RSUs, 3.0M PSUs and 0.3M options outstanding at
  2025-12-31 (Item 6.B), carried to Q4 as SBC; no convertible or warrant found. **No split** (Yahoo `events.splits` null), so
  `close × shares(measurement) × splits after measurement` holds trivially.

### The price and the cap (aggregator for live quotes only, flagged)
- **Price US$46.95**, GFS Nasdaq close **2026-09-11** (Yahoo Finance chart API, `regularMarketTime` 2026-09-11 20:00 UTC; **aggregator,
  flagged**; `px.py` / `prices_2026-09-13.json`).
- **Cap = US$46.95 × 558,658,481 = US$26,229M** (US$25,764M on the filed 2026-06-30 count alone).
- **Price context, from filings and the same flagged series:** Mubadala sold to the public at **$50.75 (May 2024)** and **$42.00 (March
  2026)**; the company bought from Mubadala at $50.75 and **$40.845**; the Department of Commerce issuance is priced at **$37.85**;
  Mubadala's Form 144 of **2026-05-26** reports **22,000,000 shares with an aggregate market value of $1,979,120,000** ($89.96 a share).
  The quote went from $41.59 (2026-03-12) to **$89.96 (2026-05-26)** and back to **$46.95**: a doubling and a halving inside six months.

### Controlling shareholder, recorded at Step 0 because it moves the count and the cap
| date | Mubadala's shares | % | source |
|---|---|---|---|
| 2025-12-31 | 450,387,613 | 81.0% | 20-F FY2025 Item 7.A |
| 2026-03-31 | 423,042,773 | 77.05% | Schedule 13G/A No. 2, `0001140361-26-016895` |
| **2026-06-30** | **399,573,756** | **72.82%** | **Schedule 13G/A No. 3, `0001140361-26-032099`, filed 2026-08-10** |

FMR LLC 69,848,380 shares, 12.7% at 2026-06-30 (Schedule 13G/A, `0000315066-26-002033`). **Free float excluding Mubadala about
27%.** Control, the Shareholder's Agreement and the related-party terms are read at Q3.

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A (Item 5: operating results, single-sourced mix, LTAs, shipment utilisation, ASP, liquidity, cash flows) [x] cash-flow
  statement incl. detail lines (F-8, FY2025; F-9/F-8/F-6/F-8 in FY2021-FY2024) [x] footnotes (government grants, trade payables and
  contract liabilities, long-term debt, issued capital, share-based payments, related parties, segments and geography, customer and
  supplier concentration, subsequent events)
- **Primary document: Form 20-F, fiscal year ended 2025-12-31, filed 2026-02-27, accession `0001709048-26-000022`, `gfs-20251231.htm`,
  CIK 0001709048.**
- **Also read:** 20-F FY2024 `0001709048-25-000024` · FY2023 `0001709048-24-000013` · FY2022 `0001709048-23-000013` · FY2021
  `0001709048-22-000008` (which carries 2019 and 2020) · the IPO prospectus 424B4 `0001193125-21-313344` · every 6-K and exhibit
  2021-11-30 to 2026-09-08 (73 filings, `k/`), including the quarterly earnings releases and interim reports, the two Mubadala
  secondary offerings (424B7 2024-05-24 and 2026-03-12), the CHIPS Direct Funding Agreement release (2024-11-20), the Term Loan A
  prepayment (2025-01-02), the IBM settlement release (2025-01-02), the revolving credit agreement (2026-08-27) and the Department
  of Commerce Securities Issuance Agreement (2026-09-08); Schedules 13G/A of Mubadala and FMR; Form 144 filings 2026.
- **Figure cross-checked against the filed statement:** **Net cash provided by operating activities $1,731M for 2025** in the audited
  CONSOLIDATED STATEMENTS OF CASH FLOWS (F-8) equals the MD&A table (*"Cash provided by operating activities | $ | 1,731"*) and
  `companyfacts` `ifrs-full:CashFlowsFromUsedInOperatingActivities` 2025-12-31 **USD 1,731,000,000**. **One restatement found
  between vintages and resolved toward the later filing:** 2020 operating cash is **$1,005.9M** in the FY2021 20-F and **$1,004M** in
  the FY2022 20-F (re-presented in millions with interest and tax paid reclassified); the difference is immaterial and the later
  figure is used.

