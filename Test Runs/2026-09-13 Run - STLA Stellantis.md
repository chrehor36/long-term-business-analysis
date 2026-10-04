# Company Run — Stellantis N.V. (STLA, STLAM.MI, STLAP.PA) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**Queue context.** **WAVE 5** of `Screens/WATCHLIST RUN QUEUE.md` (the unpriced watchlist
businesses), the eighth of the eleven foreign 20-F filers to be run (after SONY, TM, HMC, TSM, UMC,
ERIC; SPOT runs concurrently). The 2026-09-01 triage skipped it as *"foreign 20-F filers, short XBRL
history."* **Read here as UNLABELLED: a prompt to read the 20-F by hand, not a verdict.** The run
file was created before any fetch (write-early protocol). Research on disk:
`Test Runs/_research 2026-09-13 STLA/`.

**Why the screen never priced it, found rather than assumed (measured 2026-09-13).** `companyfacts`
for CIK 0001605484 carries namespaces `dei`, `ifrs-full`, `invest`, `ffd` and **no `us-gaap`**;
`ifrs-full:CashFlowsFromUsedInOperatingActivities` has **27 annual facts FY2015-FY2025, every one in
unit `EUR`, and the FY2025 20-F (accession 0001605484-26-000021) IS ingested** (FY2025 value
−4,650,000,000). So the SONY/TM/HMC/TSM cause (companyfacts lag) **does not apply**; the cause is the
10:05 handoff note's first two: **the USD-only unit filter and the US-GAAP tag names.** Nothing in the
filings is short. **And the tagged history hides a worse defect than shortness**, recorded below
under THE MERGER PERIMETER: the same CIK carries **two different companies' figures for the same
fiscal year.**

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

### The earnings currency, established from the filing — and the regional profit split the brief asked for

**The reporting currency is the euro** (€ million throughout; the 20-F's consolidated statements are
IFRS). **The profit is not mostly earned in Europe.** From Note 30, *Segment reporting*, the CODM
measure (*"Adjusted operating income/(loss)"*, non-GAAP, including the share of equity-method
investees on the post-2022 definition), six vehicle segments, € million:

| AOI | North America | Enlarged Europe | Middle East & Africa | South America | China/India/AP | Maserati | six-segment sum |
|---|---|---|---|---|---|---|---|
| 2021 (Jan 17 – Dec 31) | 11,089 | 5,373 | 672 | 873 | 437 | 116 | 18,560 |
| 2022 | 13,987 | 6,218 | 1,188 | 2,048 | 641 | 201 | 24,283 |
| 2023 | 13,298 | 6,519 | 2,503 | 2,369 | 502 | 141 | 25,332 |
| 2024 | 2,660 | 2,419 | 1,901 | 2,272 | (58) | (260) | 8,934 |
| 2025 | **(1,892)** | **(651)** | 1,429 | 1,963 | 74 | (198) | 725 |
| **five-year sum** | **39,142 (50.3%)** | **19,878 (25.5%)** | 7,693 (9.9%) | 9,525 (12.2%) | 1,596 (2.1%) | 0 | 77,834 |
| share of five-year net revenues | 45.0% | 37.7% | 5.2% | 9.2% | 2.0% | 1.0% | €809,985M |

Sources: 2023-2025 **20-F FY2025 Note 30** (accession 0001605484-26-000021); 2022 **20-F FY2024 Note 30**
(0001605484-25-000013) and FY2023 (identical, *"as adjusted"*); 2021 **20-F FY2022 Note 29**
(0001605484-23-000020) reported segment AOI on the old definition (NA 11,103, EE 5,419, MEA 554, SA 873,
CIAP 444, Maserati 116) **plus** the segment share of equity-method investees in the same table (−14,
−46, +118, 0, −7, 0). The 2021 pro forma (adding FCA's January 1-16) is NA 11,342, EE 5,324 (20-F FY2023
Note 29, *"Pro Forma Adjusted operating income, as adjusted"*). Tables extracted by `tables.py` into
`tbl/seg_FY20xx.txt`; shares computed, not filed. **Every Stellantis figure the TM row
(`_research 2026-09-13 TM/peers/COMPETITOR ROW - five-year industrial margins.md`) carries for
2021-2025 was re-read from Stellantis's own 20-Fs and matches; the TM row's 2021 column is the
reported (not pro forma) basis, derived exactly as above.**

- **North America earned half of five years' segment profit on 45% of revenue (10.75% margin against
  Enlarged Europe's 6.51%)**, and in 2021-2023 it earned 53-60% of it. In 2024-2025 both big regions
  collapsed and MEA plus South America carried the group.
- **The judgment, and its ground.** The sovereign enters as *"the currently observed rate for the
  currency the business earns in"* **[E4-15, E3-32]**. Stellantis's reporting currency, dividend,
  hybrid capital, primary quotes (Milan, Paris) and the parent's own debt are euros; **half its segment
  profit is earned in dollars** and much of the rest in reais, lira, dinars and pesos. **The owner
  earnings are computed in euros and the cap is priced in euros, so the euro sovereign is the
  consistent pairing** (the TM/HMC/ERIC precedent: the reporting-and-quote currency, with the foreign
  earnings carried as width, never a second rate). **What the choice does NOT decide:** the [E4-28]
  floor of roughly 10% *"does not move with the sovereign"*, so the gap between the EUR 3.83% and the
  USD 5.35% moves only the points-over-sovereign display, never the quit-on line. The dollar exposure
  is carried into Q4 as a named risk (tariffs, the North American margin), not into the rate **[E3-42]**.

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 3.826% (prints 3.83%) · tenor 30-year · date 2026-09-10 · source (issuing authority) ECB
  euro-area AAA government yield curve, series `YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y`, struck fresh
  2026-09-13 through `tools/sources.py`** (no certificate failure this time). **The brief's 3.83% on
  2026-09-10 is confirmed.** *(The ECB curve is a fitted AAA-sovereign curve published by the central
  bank, not a single issuer's bond; it is the source CLAUDE.md names for EUR, and it is used as named.)*
- Reference only (not used): **USD 30-year 5.35%**, US Treasury daily par yield curve, 09/11/2026,
  struck the same call.
- **FX: the cap is priced in euros directly** from the Milan quote; no conversion is needed. **Cross-check
  at the ECB euro reference rate of 2026-09-11, 1.1592 USD per EUR** (ECB data API, series
  `EXR/D.USD.EUR.SP00.A`): NYSE STLA **$5.40** ÷ 1.1592 = **€4.658**, against Milan **€4.670** and Paris
  **€4.678** the same day, a 0.3% gap explained by closing times. **No USD cap is used anywhere against
  euro earnings.**
- **ADR ratio: none. The NYSE, Euronext Milan and Euronext Paris lines are the same Dutch registered
  common shares** (20-F, *Articles of Association and Information on Stellantis Shares*: *"Beneficial
  interests in Stellantis common shares that are traded on the NYSE are held through the book-entry
  system provided by The Depository Trust Company … Beneficial interests in Stellantis common shares
  traded on Euronext Milan are held through Monte Titoli S.p.A. … Euronext Paris are held through
  Euroclear France"*). One share, three lines; about 504 million shares (17.4%) held in the United States.

### The share count, read by hand — the ERIC trap tested, the special voting shares ruled on

| date | count | what it is | document · accession |
|---|---|---|---|
| 2025-12-31 | **2,897,483,196 common shares** and 866,409,062 special voting shares | **20-F cover**, *"number of outstanding shares of each of the issuer's classes"* | 20-F FY2025, 0001605484-26-000021 |
| 2025-12-31 | issued **2,903,716,295** common, **of which 6,233,099 held in treasury**; special voting A issued 866,522,224 of which 113,162 in treasury | Note 28, *Equity*: *"At December 31, 2025, there were 2,897,483,196 outstanding common shares"* | same |
| 2025 movements | +9,348,189 treasury shares delivered to LTIP participants; +7,642,728 shares issued for LTIP and employee share purchase; **no buyback in 2025** | Note 28 table; cash-flow statement *"(Purchases)/sales of treasury shares — "* in 2025 | same |
| **2026-06-30** | issued 2,903,716,295; treasury **2,775,043** ⇒ **2,900,941,252 outstanding common shares** | *"At June 30, 2026 there were 2,900,941,252 outstanding common shares … 3,458,056 were delivered in execution of the Share-based compensation plans"* | **Semi-annual report H1 2026, 6-K 2026-07-30, 0001605484-26-000064** (`stellantisnv20260630semi-a.htm`) |
| 2026-07-01 → 09-13 | no issuance or repurchase disclosed | every 6-K filed 2026-07-13 to 2026-09-03 opened (shipments, results dates, Q2 results, the CEO conference notice); the S-8 of 2026-08-03 registers plan shares, not an issuance; the 424B5/FWP of 2026-09-10/11 are **debt** | listed under *The filing was read* |

- **THE ERIC TRAP, TESTED: IT DOES NOT FIRE.** The 20-F cover figure 2,897,483,196 is the
  **outstanding** count (issued 2,903,716,295 less 6,233,099 treasury, to the share), not the issued
  count. The major-shareholders table *does* use issued shares including special voting shares as its
  percentage base (*"Issued shares includes common shares as well as 866,522,224 Class A special voting
  shares"*), which is where a hand reader would pick up the wrong denominator; it is not used.
- **SPECIAL VOTING SHARES: EXCLUDED FROM THE CAP.** Read from the articles as summarised in the 20-F:
  the loyalty structure grants *"an extra voting right by means of granting a special voting share …
  without entitling such shareholders to any economic rights, other than those pertaining to the common
  shares. However, under Dutch law, the special voting shares cannot be totally excluded from economic
  entitlements"*; their only entitlement is a reserve of *"one percent of the aggregate nominal amount of
  all special voting shares"* (1% × 866.5M × €0.01 = **€86,652 a year**); *"Holders of special voting
  shares shall not receive any dividends in respect of the special voting shares"*; on liquidation they
  rank for that reserve and their nominal value (**€8.7M**) after the common shares' reserves and
  nominal value; *"Special voting shares cannot be traded"* and are *"transferred to us for no
  consideration"* when the common share leaves the loyalty register. **Votes, not economics: excluded.**
  They matter at Q3: Exor 15.48% of common shares carries **23.84%** of the votes, EPF 7.72% → **11.89%**,
  BPI 6.64% → **10.22%** (20-F, *Major Shareholders*, as of 2026-02-25).
- **Split history: none** in the window. **The merger share issuance is inside the long window**: PSA
  holders received *"1.742 FCA common shares for each PSA ordinary share … which represented
  1,545,220,196 shares"* on 2021-01-16, and *"all special voting shares of FCA held by Exor were
  repurchased by FCA for no consideration"* (20-F FY2021). Per-share series before 2021 are FCA's and
  are not used.
- **Senior to the common, and not in the count: €4.9bn of hybrid perpetual notes issued March 2026**
  (€2.2bn at 6.250%, €1.8bn at 6.875%, £865M at 8.250%; H1 2026 report: *"Coupon payments may be deferred
  indefinitely at the Company's discretion … Deferred coupons will accumulate"*), **classified as equity
  under IFRS**. They are a claim ahead of the common shareholder and are treated at Q4/Q5 as such
  (coupons deducted, principal added to the claims ahead), never as common equity.

### The price and the cap (aggregator for the live quote only, flagged)
- **Price €4.670** (Euronext Milan STLAM close, **2026-09-11**, Yahoo Finance chart API, symbol
  STLAM.MI; **aggregator, flagged**). Paris STLAP €4.678; NYSE STLA $5.40 = €4.658 at the ECB 1.1592.
- **Cap = €4.670 × 2,900,941,252 = €13,547M (€13.5bn).** Orientation only: ~$15.7bn at 1.1592, never
  used against euro earnings.
- The market-cap rule in CLAUDE.md (`close × shares(measurement) × splits after measurement`) is
  satisfied trivially: no split after 2026-06-30.

### THE MERGER PERIMETER — what the figures under this CIK describe (the brief's first question)

**Established from the filings, not assumed:**
- **Closing.** *"On January 16, 2021, Peugeot S.A. ("PSA") merged with and into Fiat Chrysler Automobiles
  N.V. ("FCA N.V."), with FCA N.V. as the surviving company in the merger … On January 17, 2021, the
  combined company was renamed Stellantis N.V. … January 17, 2021 is the acquisition date for the
  business combination."* (20-F FY2021, 0001605484-22-000023, *Presentation of financial and other data*.)
- **Legal acquirer: FCA N.V.** (the surviving entity, whose CIK this is; the combination agreement was
  signed 2019-12-17). **Accounting acquirer: PSA.** *"management determined that PSA was the acquirer for
  accounting purposes and as such, the merger has been accounted for as a reverse acquisition. As a
  result, the financial statements of Stellantis N.V. will represent the historical financial statements
  of PSA."* The indicators named: the board (*"six of whom were to be nominated by PSA, PSA shareholders
  or PSA employees"*), the first CEO (*"the president of the PSA Managing Board prior to the merger"*),
  and *"the payment of a premium by pre-merger shareholders of PSA."*
- **So the pre-2021 figures under this CIK describe TWO DIFFERENT COMPANIES depending on which filing you
  read.** The 20-Fs for FY2014-FY2020 (the last filed 2021-03-04, 0001605484-21-000032, under the new name
  but reporting FCA's year) carry **FCA**. The 20-F FY2021 carries **PSA** as the 2020 and 2019
  comparatives (its Note 29 shows North America net revenues of **€122M in 2020 and €140M in 2019**, which
  is PSA, not FCA). `companyfacts` holds both, for the same period, under the same element:

| `ifrs-full:CashFlowsFromUsedInOperatingActivities` | FY2019 | FY2020 |
|---|---|---|
| from FCA's 20-Fs (0001605484-20-000011, -21-000032) | **€10,462M** | **€9,183M** |
| from Stellantis's FY2021/FY2022 20-Fs (PSA comparatives) | **€8,667M** | **€6,241M** |

  **A screen that took "the latest vintage" for FY2019-2020 would read PSA; one that took "the earliest"
  would read FCA; neither is Stellantis.** This is the NEGG/`name_change_note` class, confirmed as a real
  perimeter event, not a rebrand.
- **The five-year default window 2021-2025 does not cross the merger**: every year is filed by
  Stellantis on the combined perimeter, **except that 2021 omits FCA's January 1-16** (FCA net revenues
  €2,704M for those sixteen days, 1.8% of the pro forma year; FCA operating income €80M). Carried as a
  named, small understatement in 2021, not rebuilt.
- **Other perimeter events inside 2021-2025, from the filings** (each checked at Q1/Q4 for effect on the
  means): **Faurecia** (PSA's ~39%) was *"excluded from the continuing operations of PSA as of December 31,
  2019"*, control lost *"on January 11, 2021"*, and 53,130,574 Faurecia shares plus €302M distributed to
  Stellantis holders on 2021-03-22 (20-F FY2021), so **no Stellantis year consolidates it**; the pre-close
  **€2.9bn FCA Extraordinary Dividend** went to FCA holders before the merger; **Comau**: *"In December 2024,
  Stellantis completed the sale of its 100 percent interest in Comau for a base purchase price of €300
  million … Stellantis retained 49.9 percent"* by reinvesting, now an associate (20-F FY2024), immaterial
  to the means; Leapmotor 21% acquired 2023 and
  the Leapmotor International JV; Stellantis Türkiye sold to the Tofaş JV (2025); the NextStar Energy 49%
  stake agreed to be sold to LG Energy Solution (6-K 2026-02-06). **How owner earnings cross 2020/2021 is
  stated at Q4, window by window.**

### The filing was read — not tagged data **[E3-27, E4-14]**
- [x] MD&A (*Operating and Financial Review*, including Results by Segment, Liquidity and Capital
  Resources, *Industrial free cash flows* and *Industrial net financial position*) [x] cash-flow statement
  incl. detail lines and Note 31, *Explanatory notes* [x] footnotes (Note 2 basis of preparation and the
  2025 reclassification and *Strategic plan undergoing reassessment*; Note 21 provisions; Note 28 equity;
  Note 30 segments)
- **Primary document: Form 20-F, fiscal year ended 2025-12-31, filed 2026-02-26, accession
  `0001605484-26-000021`, `stellantis-20251231.htm`, CIK 0001605484.**
- Also read for the windows: 20-F FY2024 `0001605484-25-000013` · FY2023 `0001605484-24-000022` · FY2022
  `0001605484-23-000020` · FY2021 (first Stellantis year) `0001605484-22-000023` · FY2020 (FCA's last year,
  filed as Stellantis) `0001605484-21-000032`.
- 6-Ks read: the FY2025 results release (2026-02-26, `0001605484-26-000019`); the **H1 2026 semi-annual
  report** and Q2 2026 release (2026-07-30, `-000064`, `-000062`) and supplemental (`-000066`); the
  **H2 2025 charges pre-announcement** (2026-02-06, `-000009`, with the NextStar sale); the AGM notice,
  agenda and **2025 Remuneration Report** (2026-03-03, `-000026`); the **hybrid issue** (2026-03-11,
  `-000028`); AGM results (2026-04-16, `-000032`); **FaSTLAne 2030 investor day** (2026-05-22, `-000047`);
  shipments and results-date notices (2026-01-13, 01-29, 02-16, 04-01, 04-17, 07-13, 07-15); the CEO
  conference notice (2026-09-03, `-000081`, the latest 6-K, confirmed). **Debt, not equity:** 424B5
  2026-09-11 (`0001193125-26-389250`) and FWP (`-388266`), Stellantis Finance US Inc. **$1.25bn 6.750%
  notes due 2031 and $1.25bn 7.400% notes due 2036**, guaranteed by Stellantis N.V., off the F-3ASR of
  2026-08-03 (`0001605484-26-000079`).
- **Figure cross-checked against the filed statement:** **cash flows from/(used in) operating activities
  €(4,650) million for 2025** in the audited *CONSOLIDATED STATEMENT OF CASH FLOWS* equals the MD&A
  reconciliation to Industrial free cash flows (*"Cash flows from/(used in) operating activities (1) |
  (4,650)"*) and `companyfacts` (−4,650,000,000, accession -26-000021) to the million. **And the
  cross-check found a restatement:** the same element reads **€22,485M for 2023 and €4,008M for 2024 in the
  earlier 20-Fs, and €17,954M and €1,535M in the FY2025 20-F**, because *"Effective June 2025, two types of
  cash flows were reclassified to cash flows from operating activities: (i) the net change in receivables
  related to financial services activities have been reclassified from investing activities … and (ii)
  certain financial receivables related to factoring transactions have been reclassified from financing
  activities."* Consolidated operating cash flow is **not comparable across the FY2024/FY2025 filings**;
  Q4 builds the industrial figure from the company's own financial-services split in each filing, and
  states the splice.
- **The 20-F/A the brief mentioned (2018-08-08, `0001605484-18-000053`) was opened:** Amendment No. 2 to
  **FCA's FY2017** 20-F, filed because the ICFR attestation *"inadvertently omitted the name and conformed
  signature of the auditor, Ernst & Young S.p.A."*, plus a typographical error in the Section 906
  certifications; *"No other changes were made."* Clerical, pre-merger, outside every window used.
  **Not relevant to any verdict.** (FCA also filed 20-F/As for FY2015 and FY2016; not opened, pre-merger.)

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Two businesses under one ticker, separated from the filed statements

**1. The vehicle maker (the "industrial activities").** Stellantis designs, builds and ships cars and light
commercial vehicles to dealers, distributors and fleets in five regions (Note 30: *"responsible for the design,
engineering, development, manufacturing, distribution and sale of passenger cars, light commercial vehicles and
related parts and services in specific geographic areas"*), on a *"where-sold"* basis. Per consolidated shipment,
from Note 30 and the shipment tables (computed):

| per vehicle shipped | North America | Enlarged Europe | Middle East & Africa | South America | group |
|---|---|---|---|---|---|
| net revenue, 2023 | €45.5k | €23.7k | €23.8k | €18.3k | €30.7k |
| AOI, 2023 | **€6,988** | €2,317 | €5,650 | €2,695 | €3,947 |
| net revenue, 2025 | €41.4k | €23.2k | €21.4k | €16.2k | €28.0k |
| AOI, 2025 | **€(1,285)** | €(261) | €3,155 | €1,963 | €(154) |

In plain words: **a Ram pickup or Jeep sold to an American dealer brings in almost twice what a Peugeot or Fiat
brings in Europe, and in 2021-2023 it carried three times the profit.** The cost of the vehicle is materials,
parts and plant labour (*"Cost of revenues"* 79.9% of net revenues in 2023, 86.9% in 2024, 101.4% in 2025 with the
charges inside); selling and overhead 5.0-5.9%; research and development 3.0-3.7% before 2025's write-offs. **The
profit is the thin difference between two very large numbers**, so a few points of price or volume move it from
€25bn to nothing: 2023 AOI €24,343M on €189,544M; 2025 **€(842)M on €153,508M**.

**The capital the maker consumes every year, whatever the volume** (industrial *"Capital expenditures and
capitalized research and development expenditures and change in amounts payable on property, plant and equipment
and intangible assets for industrial activities"*, from each Industrial free cash flows reconciliation):
**€10,081M, €8,938M, €9,031M, €10,761M, €9,090M** for 2021-2025, 4.8-6.9% of revenue, **1.39x depreciation and
amortization over five years** (D&A €5,871M, €6,797M, €7,549M, €7,226M, €6,981M, cash-flow statements). Of that,
capitalised development spend (intangible-assets note, *"Capitalized development expenditures — Additions"*) was
**€3,128M, €3,589M, €4,352M, €4,150M, €3,452M**, amortised at €1,575-2,193M a year, **and written off at €151M, €67M,
€122M, €693M and €6,190M.** Where that sits and how it is treated is at Q4.

**Where the profit came from (Step 0 table):** North America 50.3% of five-year segment AOI, Enlarged Europe 25.5%,
South America 12.2%, Middle East & Africa 9.9%, China/India/AP 2.1%, Maserati nil. **Where the capital sits** (the
IFRS 8 entity-wide note, *non-current assets other than financial instruments, deferred tax assets and
post-employment benefits assets*, 2025-12-31): North America **€51,633M (54%)**; the European countries named
€34,218M (36%: France 17,120, Italy 7,045, Germany 5,140, Spain 1,583, UK 1,290, Poland 1,172, Slovakia 582, Serbia
286); Brazil €3,780M (4%); other countries €6,011M (6%). *(Segment assets are not disclosed: "Operating assets are
not included in the data reviewed by the chief operating decision maker, and as a result and as permitted by IFRS 8,
the related information is not provided.")*

**2. The lender (Stellantis Financial Services) — SEPARATED, the GM/F/TM/HMC method.**
- **How Stellantis finances dealers and customers, from 20-F FY2025 Item 4:**
  - **United States, on the balance sheet.** *"Stellantis Financial Services U.S. Corp ("SFS U.S.") provides U.S.
    customers and dealers with a complete range of financing options, including retail loans, leases, and floorplan
    financing. SFS U.S. is currently playing a predominant role in retail and leasing financing with a market share of
    approximately 18 percent and 90 percent respectively and a total market share of approximately 40 percent. As of
    December 31, 2025, SFS U.S. provided wholesale (i.e. floorplan and others) lines of credit to 264 dealers
    representing approximately 10 percent of the Stellantis network in the U.S, with Bank of America and Ally
    Financial Inc. complementing wholesale funding offer to, approximately an additional 8 percent and 25 percent
    respectively, in 2025 Stellantis terminated the agreement with Santander Consumer USA Inc."* (OCR-like run-on
    punctuation is the filing's own.)
  - **Enlarged Europe, off the balance sheet in 50% joint ventures.** *"(i) Leasys, a 50 percent held joint venture
    with Crédit Agricole Consumer Finance & Mobility dedicated to pan-European multi-brand long-term operational
    leasing activities; (ii) A partnership between Stellantis Financial Services Europe ("SFSE"), and BNP Paribas
    Personal Finance ("BNPP PF") related to financing activities carried-out through approximately a 50 percent
    interest in a joint-venture operating in Germany, Austria and the UK; and (iii) A partnership between SFSE and
    Group Santander Consumer Finance ("SCF") related to financing activities carried out through 50 percent held
    joint-ventures in France, Italy, Spain, Belgium, Poland, the Netherlands"*. Equity-accounted. The 2023
    reorganisation produced €1,532M of *"Net proceeds related to the reorganization of financial services in Europe"*,
    which the company excluded from Industrial free cash flow (20-F FY2023).
  - **Brazil consolidated** (Banco Stellantis S.A.; Stellantis Financiamentos, Note 3 list); **Mexico** a 23.4%
    associate in STM Financial (Inbursa), *"expected to increase to 49.9 percent"*; **Canada** third-party banks.
- **Size, consolidated part only:** *"Total Receivables from financing activities"* **€15,731M** at 2025-12-31
  (€12,531M a year earlier: dealer €3,087M, retail €10,703M, finance leases €540M); financial-services debt with third
  parties **€20,798M** (€13,156M), against industrial debt €25,149M (Industrial net financial position table).
  **Including the JVs:** *"SFS entities already manage more than €85 billion of net receivables"*, targeting *"a
  contribution of more than €1.5 billion of AOI in 2030"* (FaSTLAne 2030 financial framework, 6-K 2026-05-22, Ex.99.3).
- **The split the owner-earnings build uses is the company's own.** Every Industrial free cash flows reconciliation
  removes the lender's operating cash flow (*"Operating activities not attributable to industrial activities"* to
  FY2023; *"Financial services, net of inter-segment eliminations"* from FY2024): **€276M (2021), €211M (2022),
  €(753)M (2023), €(5,209)M (2024, new basis; €(2,736)M old basis), €(9,700)M (2025)**. Industrial operating cash flow
  is therefore **€18,370M, €19,748M, €23,238M, €6,744M, €5,050M**. **The 2024 figure is the same on both bases**
  (4,008 + 2,736 = 1,535 + 5,209 = 6,744), so the June 2025 reclassification moved cash between the lender and the
  consolidated total, not into the industrial figure: the splice is clean.
- **The lender's profit is not disclosed in any year** (*"Other activities includes … our financial services
  activities"*). In plain words: a fast-growing U.S. auto lender and lessor funded with €20.8bn of borrowed money,
  whose volume is the maker's volume and whose 2025 growth absorbed €9.7bn of operating cash. **It does not rescue
  the maker's economics; it is carried at Q4 as a claim on the group, not a source of owner earnings.**

### The scarce input this business controls
**Positions, not inputs.** The filings name the positions: *"Stellantis maintains No. 1 positions in Brazil and
Argentina, with market shares of 25.6% and 26%"*; *"leadership in the EU30 LCV segment, achieving a 28.7% market
share"*; in MEA *"Türkiye, which maintained its No. 1 position across passenger car and LCV segments"* (Q2 2026
release, 6-K 2026-07-30); the Ram and Jeep nameplates in North America; dealer networks on four continents. **Nothing
in the filing describes an input a competitor cannot buy**: steel, batteries, engines, software and plant labour are
bought on the same terms by every maker in the row, and the brands are the thing whose position moved most (U.S.
share 12.6% → 7.6%, at Q2). Recorded here and tested at Q2, where it belongs.

### Will the fundamentals look broadly the same in ten years?
**The business model, yes; the product, the regulation and the trade regime, no — and the filing is its own
evidence.** *"H2 2025 charges of approximately €22 billion primarily reflect a strategic shift to put freedom of
choice – from a growing range of EVs, hybrids and advanced internal combustion engines – at the heart of the
Company's plans"* (6-K 2026-02-06, Ex.99.1): the 2021-2024 product assumptions were reversed inside five years
(Note 30, 2025: *"Costs related to product plan realignments and program cancellations"* €9,072M, *"Platform
impairments"* €6,583M, *"Battery JVs"* €2,054M, *"Hydrogen fuel cell program discontinuation"* €1,094M), the U.S.
CAFE penalty regime was removed (*"the elimination of CAFE fines with the enactment of OBBB"*) and U.S. tariffs arrived
the same year. **Understanding how the money is made does not require predicting the powertrain; judging whether the
profit persists does**, and that is Q2's [E4-04] and Q4's named death. **[E4-46] passes:** nothing here takes months
of study; the mechanism is price minus cost per vehicle times volume, less the capital to stay in the game, plus a
lender.

- **VERDICT: [x] IN.** A vehicle maker (€28-31k revenue and, in 2021-2023, €3.2-3.9k AOI per vehicle; half its
  profit from North America; capital spending at 1.39x D&A every year) and a lender (€15.7bn consolidated
  receivables, €85bn with the European JVs), separable on the company's own cash-flow split. The mechanism is simple;
  its stability is not, and that is carried to Q2 and Q4 as named questions, not as a Q1 caveat. *(Consistent with
  GM, F, TM and HMC, each IN at Q1.)*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Method (the HMC/SONY/HAS rule, applied by region because that is how Stellantis reports and how the brief asked):
the verdict must hold for what the shareholder actually buys, so each regional leg is judged on filed margins and
units against filed peers, and the security is decided by where the profit AND the capital sit.** Every Stellantis
figure below is from its own 20-Fs (Step 0 and Q1 sources); peer figures are from the TM run's transcription
(`_research 2026-09-13 TM/peers/COMPETITOR ROW - five-year industrial margins.md`, re-checked here against the GM and
Ford 10-K text on disk for the market-share lines) and from Renault's own results reports fetched for this run
(`peers/RENAULT_FY2025_financial_report.txt`, `RENAULT_FY2024_earnings_report.txt`, evidence-ladder rung 3; Renault is
not an SEC registrant).

### Is there a group-level moat?
**No filed evidence of one.** The merger case was synergies (*"Synergies (less implementation costs)"*, 30% of the
2021 annual bonus, reported at €7.1bn by 2022: 20-F FY2023 remuneration tables), which are cost savings any combination
could buy, not a customer advantage. The legs carry the verdict.

### [E3-03], criterion 2, in the filer's own words
> *"The automotive industry has historically experienced intense price competition resulting from the variety of
> available competitive vehicles and excess global manufacturing capacity."* (20-F FY2025, *Trends, Uncertainties and
> Opportunities — Pricing*)

> *"Intense competition, excess global manufacturing capacity and the proliferation of new products introduced in key
> segments is expected to continue to put downward pressure on inflation-adjusted vehicle prices"* (20-F FY2025, Risk
> Factors)

- [x] needed or desired · **[ ] no close substitute — FAILS on the filer's own sentence** · [x] not price-regulated
  (with the regulatory exception noted under MEA and the CAFE/EU CO2 regimes, which shape product, not price).

### THE QUESTION THE BRIEF ASKED: what happened to North American margin and share after the price-led years?
**Tested from the filed record, not assumed. The answer is that the margin was bought with share, and when the price
was given back the share did not come back.**

| North America | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|---|
| **U.S. market share** (20-F sales tables) | 12.6% | 12.2% | 11.5% | 10.9% | 9.6% | 8.0% | **7.6%** | — |
| U.S. sales (000) | 2,204 | 1,821 | 1,777 | 1,547 | 1,527 | 1,304 | **1,260** | — |
| NA consolidated shipments (000) | FCA | FCA | 1,764 | 1,861 | 1,903 | 1,432 | 1,472 | 824 |
| **NA AOI margin** (Note 30) | — | — | 16.38% | 16.36% | 15.37% | 4.19% | **(3.10)%** | 1.6% |
| NA "Vehicle Net Price" in the AOI walk, €M | — | — | — | **≈ +5,470** | **≈ +1,740** | **≈ −2,050** | **−883** | — |
| NA "Volume & Mix", €M | — | — | — | ≈ −820 | ≈ −2,250 | ≈ −6,960 | −1,430 | — |

*2019-2020 U.S. share and sales are FCA's, from FCA's 20-F FY2020 and restated identically in Stellantis's 20-F FY2021
(12.6%, 12.2%); the 2021-2025 series is from each Stellantis 20-F. **The AOI-walk figures for 2022-2024 are MEASURED
FROM THE FILED CHART IMAGES, not transcribed**: the FY2023 and FY2024 20-Fs print the walks as unlabelled images
(`stellantis-20231231_g5/g6.gif`, `stellantis-20241231_g3.gif`); `charts/measure.py` scales bar heights from the two
filed endpoint values and reproduces the filed end value within 0.4-3.9%, assuming the bar order of the labelled FY2025
chart (Volume & Mix, Vehicle Net Price, Industrial, SG&A, R&D, FX and Other). They are marked ≈ and carry no more weight
than the narrative they agree with. **One disagreement, recorded:** the 2023 chart's third bar measures ≈ +410 (green)
where the narrative names *"production disruptions and costs related to labor agreements"*, so either those costs sit in
another bar or the FY2023 order differs; the price and volume bars used above agree with the 2023 narrative (*"higher net
pricing"*, *"unfavorable mix"*), and nothing in the verdict rests on the 2023 bars alone. **The 2025 figures are read from the labelled FY2025 chart** (`charts/NA_2025v2024.png`:
Volume & Mix (1,430), Vehicle Net Price (883), Industrial (1,557), SG&A (81), R&D (139), FX and Other (462)).*

**The company's own account of the sequence, verbatim:**
1. 2022: *"In 2022, our ability to maintain strong pricing across all of the regions where we operate, particularly in
   North America and Enlarged Europe, allowed us to offset significant inflationary, supply chain and logistics-related
   pressure."* (20-F FY2022)
2. 2023: *"The decrease in North America Adjusted operating income in 2023 … was primarily due to unfavorable mix,
   foreign exchange and production disruptions and costs related to labor agreements, partially offset by higher net
   pricing and volumes."* (20-F FY2023)
3. 2024: *"In 2024, relatively high retail pricing, together with a gap in our product portfolio refreshment,
   contributed to an unusually high level of dealer-owned inventories particularly in the U.S. To address these
   inventory levels we repositioned our pricing relative to peers and implemented incentives which had an adverse
   impact on our net pricing."* and *"primarily due to significant impacts from volume/mix, increased sales incentives
   and higher warranty costs."* (20-F FY2025; 20-F FY2024)
4. 2025: *"In 2025, net pricing declined in North America, Enlarged Europe and South America"*; NA AOI down *"primarily
   due to unfavorable mix, U.S. tariffs, change in estimate for contractual warranties and increased incentive spend"*
   (the stripped text reads *"U.S. t a riffs"*, a span-splitting artifact of the HTML, flagged not smoothed);
   and *"in order to address an actual or perceived affordability issue in our product portfolio, we are launching
   several new models at lower price points."* (20-F FY2025)

**Read against the corpus:**
- **[E4-55], units over dollars — the Precision Steel shape, exactly.** U.S. unit sales fell **2,204k → 1,260k (−43%)**
  from 2019 to 2025, and share 12.6% → 7.6%, **while 2021-2023 NA revenue rose to €86.5bn and the margin held above 15%.**
  Dollar revenue flattered by pricing is how a shrinking position hides; the physical series is the honest one, and it
  fell in every year of the series.
- **[E2-44](1), the two-characteristic test's first half — FAILS.** The price rises of 2022-2023 were taken in a supply
  shortage, not *"when product demand is flat and capacity is not fully utilized"*. When demand normalised in 2024, the
  company's own words are that its prices were *"relatively high"*, inventories *"unusually high"*, and it
  *"repositioned our pricing relative to peers"*: **relative to peers** is the no-close-substitute test answered by the
  filer.
- **[E4-37], the agony metric.** A price that must be *"repositioned … relative to peers"* one year after it was raised
  is agony-pricing, the downgrade detected in real time.
- **[E3-62], the second step.** The ≈€7.2bn of net price taken in 2022-2023 did not stay home: ≈€2.9bn was given back in
  2024-2025 as incentives, and the unit loss it bought cost ≈€11.5bn of volume and mix over 2022-2025.
- **[E4-32], direction.** **Narrowing, measured**, and not recovered: H1 2026 NA AOI margin 1.6% on shipments +27%
  (Q2 2026 release: *"North America market share increased to 7.4%, up 40 basis points year-over-year"*, a
  North-America-wide figure, below the 7.8% of 2024).

### THE COMPETITOR ROW — required [E3-28]. By region, same measure where filed, same window.

**North America (50.3% of five-year segment AOI; 54% of non-current assets)**

| maker | measure, as filed | 2021 | 2022 | 2023 | 2024 | 2025 | pooled 2021-25 | U.S. share 2021 → 2025 | source |
|---|---|---|---|---|---|---|---|---|---|
| **Stellantis North America** | segment AOI ÷ net revenues | 16.38% | 16.36% | 15.37% | 4.19% | **(3.10)%** | **10.75%** (2023-25: 6.67%) | **11.5% → 7.6%** | 20-Fs FY2021-25 |
| GM North America (GMNA) | EBIT-adjusted ÷ net sales and revenue | 10.18% | 10.12% | 8.70% | 9.22% | 6.77% | **8.87%** (2023-25: 8.23%) | **14.4% → 17.2%** | 10-Ks `0001467858-24-000031`, `-26-000013` (TM row; share table GM-23 line 192, GM-25 line 196) |
| Ford (Blue + Model e + Pro; global segments, no NA segment filed) | segment EBIT ÷ external revenue | 4.02% | 5.33% | 5.96% | 5.31% | 2.91% | 4.71% | **12.4% → 13.2%** | 10-Ks `0000037996-24-000009`, `-26-000015` (TM row; share table F-23 line 285, F-25 line 280) |
| Toyota, Honda, Hyundai-Kia, Tesla | no North American segment margin on a like basis (Toyota's geographic operating income is by booking entity: FY2026 North America ¥(192.6)bn while exports are booked in Japan; Honda and Hyundai file no NA segment; Tesla automotive is gross margin) | | | | | | not rowed | | TM and HMC runs |

- **Position:** in 2021-2023 Stellantis North America **out-earned GMNA by 5-7 points of margin on less than half the
  volume**; in 2024-2025 it fell **14 points below** while GM **gained 2.8 points of U.S. share** and Ford 0.8. **Two
  filed peers in the same market, same years, went the other way on units.** The row shows position; it cannot show
  conduct [E3-61], but here the filer names its own conduct (the pricing sequence above).
- **Class for the leg: NONE, direction narrowing.** A position that earned 16% for three years and lost 40% of its U.S.
  units in six is [E3-51]'s surfing run: the advantage lived in the 2021-2023 shortage wave.

**Enlarged Europe (25.5% of five-year segment AOI; ~36% of non-current assets)**

| maker | measure, as filed | 2021 | 2022 | 2023 | 2024 | 2025 | pooled | share | source |
|---|---|---|---|---|---|---|---|---|---|
| **Stellantis Enlarged Europe** | segment AOI ÷ net revenues | 9.15% | 9.82% | 9.79% | 4.10% | **(1.13)%** | **6.51%** (2023-25: 4.52%) | **EU30 22.1% (2021) → 19.7 → 18.3 → 17.0 → 16.0% (2025)**; Italy 39.0% → 28.7%; France 35.8% → 28.0%; Spain 25.4% → 15.9% | 20-Fs FY2021-25 |
| Volkswagen Automotive Division (global) | IFRS operating result ÷ sales revenue | 6.4%* | 7.1%* | 7.0%* | 5.6% | 1.8% | 2024-25: 3.71% | group units 8,576k → 9,022k | VW Annual Report 2025 (TM row; *company-stated ratios) |
| Renault Group, Automotive | *"Automotive operating margin"* ÷ *"Automotive revenue"* | not fetched | not fetched | 6.3% (€3,051M; revenue derived from the FY2024 report's *"up 4.9%"*) | 5.9% (€2,996M on €50,519M) | 4.2% (€2,184M on €51,442M) | 2023-25: 5.48% | — | Renault FY2024 earnings report; FY2025 financial report (rung 3). The FY2023 report URL returned HTTP 403. |
| Ford in Europe (share only) | retail share | | | | | | | UK 11.8% → 9.8%; Germany 5.7% → 5.3%; Italy 6.2% → 5.5% | Ford 10-Ks |

- **Position:** Stellantis Europe was the best of three European-scale peers in 2021-2023 and **the worst in 2025**
  (Renault 4.2%, VW Automotive 1.8% on a global division, Stellantis Europe (1.13)%), with **the steepest share loss
  of any row entry** (EU30 −6.1 points in four years). Renault's own 2025 walk names the same cause in the same
  market: *"increased commercial pressure, especially in Europe"*. The one filed strength is LCVs (*"leadership in the
  EU30 LCV segment, achieving a 28.7% market share"*), and the 2025 Europe walk charges *"higher industrial costs related
  to warranty and LCV compliance provisions"* to it.
- **[E2-44](1) FAILS in the filer's own labelled 2025 walk** (`charts/EE_2025v2024.png`): **Vehicle Net Price (1,830)**
  on flat industry volume (*"the EU30 automotive market recorded results broadly in line with the previous year"*),
  alongside Volume & Mix (981). **Class for the leg: NONE, narrowing.**

**South America (12.2% of profit; ~4% of non-current assets in Brazil) — PROVISIONAL for want of a filed peer margin**
- Stellantis SA margin 8.32% → 13.11% → 14.75% → 14.32% → 12.12% (pooled 12.83%); Brazil share **32.0% → 32.9% → 31.4%
  → 29.4% → 29.3%**, Argentina 29.1% → 30.5%. **GM's Brazil share, same years: 11.4% → 13.8% → 14.2% → 12.0% → 10.3%**
  (GM 10-Ks), so the Brazilian share loss of 2023-2025 hit both incumbents. No peer files a South American margin (GM
  inside GMI; VW and Renault no regional profit): **the leg's class is PROVISIONAL, and "no peer data" is a named
  obstacle, not a pass.** The filer's own words cap the leg: 2025 AOI fell on *"Brazilian Real devaluation impact on
  industrial costs and Argentine Peso devaluation impact on price"*, cushioned by *"a benefit from recognition of
  Brazilian indirect tax credits"*, whose *"non-repeat"* halved Q2 2026 SA AOI (€782M → €402M). **A leg whose margin
  includes recurring tax-credit recognitions is not shown to be a franchise by its margin.**

**Middle East & Africa (9.9% of profit) — PROVISIONAL, and partly a regime, not a moat**
- MEA margin 13.01% → 18.41% → 23.70% → 18.83% → 14.72% (pooled 18.32%); Türkiye share **34.0% → 27.7% → 26.3%** (2023-25),
  Algeria **86.5% → 65.2% → 85.4%** from a local plant; the 2025 walk (`charts/MEA_2025v2024.png`) books **Vehicle Net
  Price +860 against FX and Other (1,411)**: pricing in a hyperinflationary currency (*"From April 1, 2022, Türkiye's
  economy was considered to be hyperinflationary"*) is a currency pass-through, not [E2-44] pricing power. An 85% share
  behind a local-production requirement, with cash *"subject to restrictions on transfer"* (€276M in Algeria), is
  **[E2-59]'s administered floor, owned by the regime.** No filed peer margin: PROVISIONAL.

*Row limits stated:* **peers named with a filed regional or divisional margin: GM, Ford, Volkswagen, Renault (4) of the
industry's ~10-12 global-scale makers; Toyota, Honda, Hyundai-Kia, BYD, Tesla and Nissan carried from the TM/HMC rows
at enterprise level only (in the HMC row Stellantis's six-segment pooled 9.61% for 2021-25 was the highest operating
measure of the eleven, Tesla's gross margin excepted; its 2025 figure of 0.49% was below GM's 6.67%, Toyota's 6.11%,
Hyundai's 5.05%, Ford's 2.91% and VW's 1.8%).** Measures differ (non-GAAP adjusted for Stellantis, GM, Ford; IFRS for VW and
Renault); Stellantis's AOI excludes the €4,130M 2025 warranty re-estimate and €9,072M of programme cancellations, so its
2025 figure is **flattered**, not penalised, against VW's IFRS result. **[E3-61]:** the row shows position, not conduct.

### The remaining Q2 tests
- **[E4-04] — must the moat be rebuilt?** Yes, and the filing measures it: capitalised development **€18,671M added
  2021-2025 against €9,904M amortised and €7,223M written off** (Q1), i.e. **the spending bought replacements that were
  cancelled, not the defence of a standing advantage**; the 2025 notes name *"platform impairments"* (€6,583M) and
  *"product plan realignments and program cancellations"* (€9,072M). By [E4-04]'s own test, a lapse in spending
  destroys the product line, and the spending buys its replacement.
- **[E3-46] / [E2-43] — the second question, as a number:** industrial owner earnings (Q4) of roughly €4bn a year
  over 2021-2025 at the capex end, on non-current assets of €95.6bn (2025), is **~4%**, and 2024 and 2025 were each
  about €(5.0)bn. Not the class the corpus calls the best businesses.
- **[E3-33] / [E5-28] untapped pricing power:** refuted by the filing (prices *"repositioned … relative to peers"*).
- **[E2-45] attacker's test:** the attacker is already filed — *"Manufacturers in countries that have lower production
  costs, such as China and India, have become competitors"* (GM-25); in Stellantis's own case the answer was to **buy
  into the attacker** (Leapmotor 21% and the 51% Leapmotor International JV, distributed through Stellantis's European
  dealers: *"Leapmotor vehicles in Europe … introduced in more than 400 dealerships"*). A moat does not license its
  attacker's products into its own castle.
- **[E2-53] dominance:** no leg, except Algeria (a regime).
- **[E4-23] key-person dependence:** low; the 2024-2025 CEO change (Q3) moved strategy, not the moat.
- **[E4-36] which cause of success:** the 2021-2023 record is **wave-riding** (the chip-shortage price wave) plus a
  one-time merger cost programme; neither is ownable.

### THE FAIR COUNTER-CASE, stated as its best advocate would state it [E4-51]
**Stellantis earned a 12.5-13.7% six-segment margin for three straight years, the highest of any volume maker in the
eleven-name filed row, on the merger's €7bn+ of synergies; it owns the pickup and SUV nameplates that make American
automobile profits, the European LCV leader, the Brazilian and Argentine leader and the Turkish leader; the 2024-2025
collapse is a self-inflicted, diagnosed and reversible pricing and inventory error by a CEO who has left, and it is
already mending: Q2 2026 North America shipments +38%, AOI positive in every region but Europe, U.S. share up 40bp,
the CAFE penalty regime abolished (a structural tailwind for a truck maker), a €6bn cost programme and a 7% AOI
target for 2030.** What defeats it for Q2 is that it argues position and management, not franchise: the three strong
years were the years the whole industry priced up in a shortage (GMNA + GMI 8.6-9.8%, Renault 6.3% in 2023, VW Automotive 6.4-7.1%), Stellantis
took more price than peers and **paid for it in units in every year of the series**, and the filer's own sentences
concede substitutes (*"relative to peers"*). A reversible error by a replaceable manager is Q3 material; a business
whose best years depended on the error being profitable is not a franchise.

- Class: **[x] NONE on the business as constituted** (North America NONE, narrowing; Enlarged Europe NONE, narrowing;
  South America PROVISIONAL; Middle East & Africa PROVISIONAL, partly an administered floor; lender NONE). Direction:
  **narrowing** (share down in every region reported, 2021-2025).
- **Are the PROVISIONAL legs a reason for UNRESEARCHED instead of OUT?** Asked aloud: *"Can I name the document that
  would resolve this?"* For South America, a peer's filed regional margin (VW do Brasil, Hyundai Brazil) is not in any
  document obtained, and **even at the most favourable reading the two legs are 22% of five-year profit on ~10% of
  non-current assets, while North America and Europe are 76% of the profit, ~90% of the assets, all of the capital plan
  and both fail on the filer's own words.** The HMC/SONY rule decides the security by where the profit and the capital
  are; no document about South America can reverse the verdict on the legs that carry the capital. So the verdict is
  OUT, and the two legs stay recorded as PROVISIONAL rather than scored.
- **VERDICT: [x] OUT — on the business as constituted.** [E3-03] criterion 2 fails on Stellantis's own risk factor and
  on its own 2024 account of pricing *"relative to peers"*; [E2-44](1) fails in its own 2025 walks (North America
  Vehicle Net Price (883), Europe (1,830)); [E4-55] units fell in every year (U.S. sales −43% 2019-2025, U.S. share
  12.6% → 7.6%, EU30 share 22.1% → 16.0%) while two filed North American peers gained share; and [E4-04] the spending
  buys replacement programmes, €7.2bn of which were written off. **The entry run stops here. [E5-13]: most names should
  end here, and that is the system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT. Everything below is **RECORDED, NOT GOVERNING**, and the
price block carries operator rule 3's header.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business as constituted).
*Nothing below can reopen Q2 [E2-37, E2-38, E3-39]. Every ledger id cited here was checked against
`principle_ledger.csv` before use (the brief's [E4-27] for incentives and [E4-52] for converging flags are the correct
rows).*

### STEP 1 — THE WEIGHT CASE, declared first
- [x] **Daily execution [E3-38, E3-43, E2-70]** — the filings show the manager's daily choices moving the result by
  tens of billions inside two years: *"relatively high retail pricing, together with a gap in our product portfolio
  refreshment"* (2024), *"a deterioration in quality, as a result of operational choices, which did not deliver the
  expected quality performance"* (the €4,130M warranty re-estimate, 2025), and the product-plan reversal (€9,072M). An
  undifferentiated product (Q2) magnifies the manager.
- [ ] **Control [E1-16]** — a minority holding in a listed company.
- [~] **Leverage [E3-29]** — the industrial arm is net cash (€10,035M at 2026-06-30, of which €4.9bn is hybrid capital);
  **the lender is not**: financial-services debt €28,406M at 2026-06-30 against €20,798M six months earlier and €13,156M
  at 2024-12-31. Not ticked for the maker; recorded as a rising exposure.
- **Case declared: BINARY GATE** (daily execution). No price compensates a failure here [E1-16, E3-29, E5-35].

### Honesty — the binary [E5-16], each matter dated to when it became PUBLIC
| public | matter | status, from the filings |
|---|---|---|
| **2021-01-27** | FCA US *"agreed to plead guilty to a single count of conspiracy to violate the Labor Management Relations Act"* over *"past misconduct of certain former FCA US employees involving the UAW-Chrysler National Training Center"*; fine not material; *"an independent compliance monitor for three years"* | court approval 2021-07-19 (20-F FY2021, FY2022) |
| **2022-06-03** | FCA US diesel-emissions criminal settlement: *"a guilty plea, a fine of approximately $96 million, and the forfeiture of approximately $204 million in gains"*, after DoJ charges against three employees (2019, 2021), *"placed on administrative leave following their indictments"* | resolved; related private suits continue (20-F FY2022) |
| 2021-06 / 2021-07 | Automobiles Peugeot and Citroën *"placed under examination by the Judicial Court of Paris"* (Euro 5 diesel, 2009-2015); FCA Italy the same (Euro 6, 2014-2017); *"The Public Prosecutor has requested that the companies involved be referred to criminal court on consumer fraud charges"* | **pending** (20-F FY2025) |
| 2024-07 | KBA formal decision of non-compliance, Opel Euro 5 diesels; *"the cost of any recall … may be significant"* | objected, cooperating |
| 2025-03 | Frankfurt prosecutor: Stellantis Europe *"negligently breached supervisory duties"*, fine not material, *"The decision did not involve a finding of intent or fraud and is now final."* | final |
| 2024-08 | U.S. securities class action alleging *"material misstatements relating to the Company's 2024 financial guidance"* against the company and *"certain of its former officers"* | motion to dismiss filed June 2025; pending |

**Reading.** Two corporate guilty pleas by the principal operating subsidiary (FCA US, the source of half the profit)
for conduct in roughly 2009-2016, before the Stellantis board existed; the company acted when it learned (employees on
leave, cooperation, accruals, a monitor), which is the test [E5-22] names (*"they didn't act when they learned"*).
**No Stellantis-era integrity finding was found in the filings read.** **Flagged, not resolved: the same scope question the
UMC run raised for the operator** (a corporate plea against [E5-16]'s *"personal misconduct"*); STLA differs from UMC in
that no current employee was named in a conviction. **As recorded: the binary would read IN (no disqualifier found),
with the scope question open.** *"Sincerity and empathy can easily be faked"* [E5-17]: IN is the absence of a found
disqualifier, not a finding of honesty.

### STEP 2 — THE FLAGS (prompts to read, never verdicts)
- [x] **Weak accounting, as the except-for and restructuring flags [E2-57, E3-53, E5-33] — FIRES, and it is the sharpest
  finding in Q3.** Adjusted operating income, the headline and the pay metric, excluded **€38,793M of costs over
  2021-2025 (2,712 + 3,741 + 1,967 + 4,961 + 25,412, Note 30/29 of each filing; 2021's on the full-year basis the filing
  gives, *"Total adjustments Jan 1 - Dec 31, 2021"*) against cumulative AOI of €74,730M: the headline was 2.08x cumulative
  IFRS operating income (€35,948M).** The "unusual" items recur: *"Restructuring"* in 5 of
  5 years (€5,708M); **warranty estimate changes in 3 of 5 years** (*"Change in estimate of non-contractual warranties"*
  €732M 2021, €314M 2022; *"Change in estimate for contractual warranties"* **€4,130M 2025**); *"Takata recall campaign"*
  in 4 of 5 years (€951M, €(10)M, €768M, €622M); *"CAFE penalty rate"* 2022 and 2025; *"Collective agreements related
  costs"* €428M in 2023 (the UAW settlement year); *"Argentina currency devaluation"* €302M in 2023. **Warranty, recalls,
  regulatory penalties and labour agreements are the ordinary costs of making cars**; [E5-33]: *"to tell owners year after
  year, 'Don't count this' … is misleading."*
- [ ] Unintelligible footnotes — the notes are long and legible; **but the AOI walks by operational driver were images
  without numbers in the FY2023 and FY2024 20-Fs** (the numbers were added to the FY2025 chart). Recorded as a disclosure
  prompt under [E4-22]'s second flag, not scored.
- [x] **Trumpeted projections [E4-22] third flag, and the record against outturn [E3-48] — FIRES:**

| said | when, document | outturn |
|---|---|---|
| *"Net Revenues to double to €300 billion by 2030 while sustaining double-digit AOI margin through the entire plan period"*; *"reaching 100% of passenger car BEV sales mix in Europe"* by 2030; *"Achieve 100% of the €5 billion annual cash merger synergies target by the end of 2024"* | Dare Forward 2030, 6-K 2022-03-01 | AOI margin 5.5% (2024), (0.5)% (2025); replaced 2026-05-21 by FaSTLAne 2030: *"Revenue growth, from €154 billion in 2025 to €190 billion by 2030"*, *"AOI margin of 7% by 2030"*; the EV course reversed at €22bn of charges |
| 2024: *"a minimum commitment of double-digit adjusted operating income (AOI) margin in 2024, as well as positive industrial free cash flow"* | FY2023 release, 6-K 2024-02-15 | withdrawn 2024-09-30: *"Expected to be between 5.5 - 7.0% for the FY 2024 period, down from prior "double digit""*, IFCF *"Expected to range from -€5 billion to -€10 billion"*; outturn 5.5%, €(6,045)M |
| 2025: *"Mid-Single Digits"* AOI margin, *"Positive"* IFCF | FY2024 release, 6-K 2025-02-26 | *"suspending its 2025 financial guidance due to tariff-related uncertainties"* (6-K 2025-04-30); H2 2025 re-set to *"AOI margin: Low-single digits"* (6-K 2025-10-30); outturn **H2 2025 (1.7)%**, FY (0.5)%, IFCF €(4,525)M |
| 2026: *"AOI margin: Low-Single Digit %"*; IFCF *"Improved Y-o-Y"*; *"Expect positive Industrial free cash flows in 2027"* | FY2025 release 2026-02-26; reaffirmed 2026-07-30 | H1 2026 AOI margin 2.1%, IFCF €(921)M — on track so far |

  **Four consecutive plan-level commitments missed or withdrawn in four years**, each replaced by a new one. [E5-30]: a
  guidance culture is a ratchet, and the 2026 plan continues it (targets to 2030).
- [ ] **Serial share issuance [E5-15]** — clean: common shares outstanding 3,132.6M (2022-01-01) → 2,900.9M (2026-06-30).
  The merger issued 1,545M shares once. **The March 2026 hybrids are senior capital, not common issuance**, recorded at Q4.
- [ ] **EBITDA promotion [E4-29]** — **clean**: zero occurrences in the 20-Fs FY2021-FY2025, the FY2025 release, and the H1
  2026 supplemental (FCA's last 20-F, FY2020, used it three times). The promoted metric is AOI, scored above.
- [ ] **Filed-figure tells [E4-30]** — not firing: cash taxes paid ÷ pretax profit 14.3% (2021: €2,170M / €15,129M),
  14.7% (2022), 11.8% (2023), 69.2% (2024), paid €204M on a loss (2025) (Note 31 and the cash-flow statements); reported
  profit was not smooth.
- [~] **Metric-switching [E2-49]** — the synergy metric left the annual bonus after 2023 once its maximum had been beaten
  (€7.1bn against a €5.0bn maximum for 2022), not after deterioration; **the EV-nameplates metric (30% of the 2023-2025
  and 2024-2026 PSUs) was replaced by *"Quality 3MIS kppm"* in the 2025-2027 plan after the quality deterioration was
  booked**, i.e. a yardstick added where the damage was, which is the candor direction. Not firing.
- [x] **Dividends funded by borrowing [E2-52], restricted earnings [E2-60] — FIRES in substance.** 2024: dividends
  €4,651M and buybacks €3,000M against Industrial free cash flows of €(6,045)M; 2025: dividends €1,959M against €(4,525)M;
  gross long-term debt raised €13,115M and €14,194M; industrial net financial position **€29,487M (2023) → €15,128M (2024)
  → €6,694M (2025)**, then the 2026 dividend suspended and *"the issuance of up to €5 billion of hybrid bonds"* authorised
  (FY2025 release). The payout was replaced by senior capital at 6.25-8.25%.

### STEP 3 — THE PRIMARY TEST [E2-01], balance sheet first
Net profit from continuing operations ÷ year-end equity attributable to owners of the parent (balance sheets, 20-Fs):
**2021 23.6%** (€13,218M / €55,907M) · **2022 23.3%** (€16,779M / €71,999M) · **2023 22.8%** (€18,625M / €81,693M) · **2024
6.8%** (€5,520M / €81,692M) · **2025 (41.7)%** (€(22,332)M / €53,551M). Equity carries ~€29-32bn of goodwill and
indefinite-lived intangibles from the FCA purchase accounting; without undue leverage at the industrial level. **Five-year
cumulative net profit €31,810M on equity that averaged ~€69bn: ~9% a year**, earned in three shortage years and given
back in two. Not a high earnings rate on equity capital over the cycle.

### The half-owner test [E2-26]
**Split.** Candid where it counts in the text: the 20-F names the quality failure as the company's own (*"operational
choices, which did not deliver the expected quality performance"*), names the 2024 pricing error, and pre-announced the
€22bn of H2 2025 charges three weeks before the results (6-K 2026-02-06). **Not candid in the number the company leads
with and pays on**: the same warranty cost is excluded from AOI and from the AOI-based incentive metrics. [E2-26]: *"the
CEO who misleads others in public may eventually mislead himself in private"*; the adjusted number is where that risk
lives.

### The institutional imperative [E2-30]
- [ ] (1) resists change — no: the plan was reversed twice (2024, 2026).
- [x] (2) projects soak up funds — *"Contributions of equity to joint ventures and minor acquisitions"* €811M, €769M,
  €2,767M, €2,376M, €1,116M (2021-25; battery JVs, Leapmotor 21% in 2023), then *"Battery JVs"* €2,054M and *"Hydrogen fuel
  cell program discontinuation"* €1,094M written off in 2025; NextStar Energy 49% sold to LG Energy Solution (6-K
  2026-02-06).
- [x] (3) studies support the craving — Dare Forward 2030's 75 BEVs and 5 million BEV sales by 2030, reversed at €22bn.
- [x] (4) peers imitated — GM (*"charges for our EV strategic realignment"*, GM-25 Note 23) and Ford (Model e segment losses
  $(892)M to $(5,105)M a year, 2021-2025) built and wrote off the same EV capacity in the same years (TM row). *"Institutional dynamics,
  not venality or stupidity."*

### Capital allocation — the buyback conditions [E5-08, E4-31, E5-24]
- **What was bought, from the filings:** 2022 €923M; **2023 €2,434M (142.1M shares)**; **2024 €3,000M (164.2M shares,
  ~€18.3 average)**; 2025 nil. **~306M shares for ~€5.4bn in 2023-24 at ~€17.7; worth ~€1.4bn at €4.67.**
- **(1) ample funds:** met in 2023 (industrial net cash €29.5bn); **doubtful in 2024**, when the third €1bn tranche
  (announced 2024-08-01, window to 2024-11-29) was **completed early on 2024-10-02**, including **€92M bought
  2024-09-20 to 09-26 at €13.59** (6-K 2024-09-30) and purchases on **30 September, 1 and 2 October** at €12.50-12.75 —
  **the same 30 September on which the company cut its 2024 IFCF guidance to "-€5 billion to -€10 billion"** (6-K
  2024-10-03: *"the Company has purchased a total of 72,041,332 common shares for a total consideration of €999,999,880"*).
- **(3) owners informed [E4-31]:** the 20-26 September purchases were made while a guidance revision of that size was
  being prepared and before it was public. **A prompt, stated with the humility clause**: the filing does not say when the
  board decided the revision, and a pre-set programme under a mandate can run in a closed period. *"many CEOs never stop
  believing their stock is cheap"* [E5-08]; *"They also know a whole lot more about them than I do"* [E4-13].
- **(2) material discount to value conservatively calculated:** against the Q5 computation (a conservatively calculated
  value at the ~10% floor of roughly €0-12 a share across valid windows), purchases at €12.5-18 fail. **CAPITAL-ALLOCATION
  FLAG, live**, binding position size, never the rate.
- **Merger synergy claims against outturn:** the claim was *"€5 billion annual cash merger synergies"* by 2024; the filed
  remuneration table reports **€7.1bn net cash synergies for 2022** (20-F FY2023, SAIP table). The claim was met on the
  company's measure; **the outturn the owner receives is the AOI and cash record above**, which the synergies did not
  protect. [E4-39]: no filed post-mortem of the merger case against the announcement was found in the documents read.

### Pay [E4-27] — *"Never, ever, think about something else when you should be thinking about the power of incentives"*
- **What it vests on:** the annual bonus (SAIP) on AOI margin and Industrial free cash flow (25% each in 2021, 32.5% each
  in 2024), synergies, quality and ESG metrics; the PSUs on **3-year average adjusted AOI (40%)**, relative TSR against eleven
  OEMs (30%), and EV nameplates (30%, replaced by quality in 2025-27). **The largest pay metric is the adjusted figure whose
  exclusions fired above**: a warranty re-estimate classified as "unusual" is also a warranty cost removed from the pay
  metric. [E4-52] below.
- **What was paid:** former CEO Tavares **€19.2M (2021), €23.5M (2022), €36.5M (2023), €23.1M (2024), €11.9M (2025)**
  (20-F FY2025 remuneration five-year table). The 2024 and 2025 figures each include **€10,000,000 from the *"2021-2025
  Transformation Incentive"*** (the first milestone paid March 2024; the second *"to be paid in 2025"* under the December 2024
  Separation and Release Agreement, after he resigned *"with immediate effect"* on 2024-12-01), plus **€2,000,000 severance**
  and **800,000 shares in January 2026** under the Shareholder Return Incentive (the TSR result of *"200% of target - 2,000,000
  PSUs"* cut to 800,000, the rest forfeited). The 2023-2025 PSUs paid **23.4% of target**; the 2024 SAIP paid **0%** (payout
  trigger). **The fixed and milestone elements paid in full across the collapse; the formula elements responded.**
- **Leadership change [E3-48] and governance:** CEO resigned 2024-12-01; an Interim Executive Committee *"chaired by John
  ELKANN"* ran the company; Antonio Filosa (South America head; appointed North America COO, 6-K 2024-10-11) selected 2025-05-28 (6-K
  2025-05-29). **Controlling holders (20-F FY2025, as of 2026-02-25):** Exor 15.48% of common shares, **23.84% of votes**;
  Établissements Peugeot Frères (Peugeot Invest) 7.72%, **11.89%**; **Bpifrance (the French state and Caisse des Dépôts, via
  EPIC Bpifrance and CDC, 49.3% each) 6.64%, 10.22%**, plus CDC's 0.28% directly. **Together ~30% of the economics and ~46% of
  the votes**, with nomination rights in the articles; the Chairman *"established Exor N.V., which is currently the largest shareholder"* (20-F FY2025, directors' biographies). [E3-66]: a Dutch N.V. with a
  loyalty-vote structure and a state shareholder whose constituencies include plants and jobs; the minority owner stands
  behind them in the queue.

### [E4-52] — the flags converge, and that is a different event
**Four prompts point at one outcome, the headline number:** (a) pay vests on adjusted AOI; (b) recurring warranty, recall,
penalty and labour costs are excluded from AOI; (c) a guidance culture promised double-digit AOI through 2030 and missed it
four times; (d) cash was returned at the top (€9.6bn of dividends and buybacks in 2024-25 while IFCF was €(10.6)bn),
including buybacks run to completion across the day of the profit warning. **Not a fraud finding** [E2-30, E5-38]: each is a
normal practice; together they are one reinforcing system, and it rewarded the number rather than the owner's cash.

### THE GUARDRAIL
- [x] Nothing here promotes the name; the new CEO's credible early record (South America, then North America shipments
  +38% in Q2 2026) cannot repair Q2 [E2-37, E2-38, E3-39].
- [x] Key-person dependence is recorded at Q2: low.
- [x] Is the franchise intact and the damage excisable [E2-35, E2-36]? **No**: Q2 found no franchise to excise into, so the
  manager would be the plan.

- **VERDICT: NOT ISSUED — Q2 closed the file.** *For the record only:* on the filings, **no integrity disqualifier found in
  the Stellantis era** (the FCA US pleas of 2021 and 2022 stated and flagged as the UMC scope question), with **converging
  flags [E4-52]** (adjusted-metric exclusions that recur, a four-miss guidance record, pay on the adjusted figure,
  distributions funded by borrowing) and a **live capital-allocation flag** on the 2023-24 buybacks. *IN never promotes.*

---
## Q4 — WILL IT SURVIVE?

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business as constituted).

### Owner earnings — the one number **[E2-23]**, industrial perimeter, € million
**Construction (the framework's CONVENTION, applied):** industrial operating cash flow (consolidated OCF less the
company's own financial-services OCF, Q1) **less share-based compensation** (PSU/RSU expense plus employee share purchase
plan cost) **less (c)**, where (c) at the capex end is industrial capex including capitalised development and the change
in capex payables, **plus IFRS 16 lease principal** (at the D&A end, D&A already contains right-of-use depreciation, so
lease principal is not deducted twice). Script and inputs: `_research 2026-09-13 STLA/oe.py`, output `oe_out.json`.

| year | perimeter | industrial OCF | SBC | capex incl. capitalised development | lease principal | D&A | **OE, capex end** | OE, D&A end |
|---|---|---|---|---|---|---|---|---|
| 2019 | **pro forma FCA + PSA** | 17,526 | 129 | 12,050 | 484 | 7,636 | **4,863** | 9,761 |
| 2020 | **pro forma FCA + PSA** | 14,259 | 132 | 11,548 | 566 | 7,519 | **2,013** | 6,608 |
| 2021 | Stellantis (from Jan 17) | 18,370 | 201 | 10,081 | 566 | 5,871 | **7,522** (5,709 with FCA Jan 1-16) | 12,298 (10,485) |
| 2022 | Stellantis | 19,748 | 170 | 8,938 | 568 | 6,797 | **10,072** | 12,781 |
| 2023 | Stellantis | 23,238 | 225 | 9,031 | 693 | 7,549 | **13,289** | 15,464 |
| 2024 | Stellantis | 6,744 | 103 | 10,761 | 874 | 7,226 | **(4,994)** | (585) |
| 2025 | Stellantis | 5,050 | 105 | 9,090 | 867 | 6,981 | **(5,012)** | (2,036) |

**Sources, line by line.** 2021-2025 industrial OCF and capex: the Industrial free cash flows reconciliations in 20-F FY2022
(2021-22), FY2024 (2023, old basis) and FY2025 (2024-25, new basis; 2024 identical on both, Q1); D&A: consolidated
cash-flow statements; SBC: *"Total expense for the PSU awards and RSU awards of approximately €201 million, €170 million,
€189 million, €45 million, €73 million"* plus employee-share-plan *"total cost of the plan"* €36M (2023 plan), €58M (2024),
€32M (2025); leases: Note 31 *"cash payments for the principal portion of lease liabilities"*. **2019-2020 pro forma:**
FCA from its own 20-F FY2020 (0001605484-21-000032) Industrial free cash flows table (*"Cash flows from operating
activities - continuing operations"* 10,770 / 9,183 less *"Operating activities not attributable to industrial
activities"* 74 / 29; *"Capital expenditures for industrial activities"* 8,383 / 8,598), PSU/RSU expense €92M / €98M, lease
principal €299M / €389M, D&A €5,445M / €5,143M; **PSA from Stellantis's 20-F FY2021 comparatives** (*"Net cash from operating
activities"* 8,667 / 6,241 less *"Net cash from operating activities - discontinued operations"* 1,837 / 1,136, i.e.
Faurecia removed; investments in PP&E and intangibles 3,544 / 2,733 plus change in capex payables 123 / 217; share-based
expense €37M / €34M; lease principal €185M / €177M; D&A 2,191 / 2,376). PSA's finance companies were equity-accounted JVs
(PSA 2020 statements, 6-K 0000950157-21-000293: *"Equity method investments - finance companies"* €2,632M; consolidated
finance receivables €31M), so its consolidated OCF is industrial.

**THE MERGER PERIMETER — HOW THE MEANS CROSS IT (the brief's rule, stated): REBUILT, on one perimeter, from both
predecessors' filed cash-flow statements (the CNR rule), for 2019 and 2020 only.** The two companies' filed figures are
added; **no eliminations are filed, and none are made** (pre-merger dealings between them, e.g. the Sevel van joint
venture, were between separate groups; the rebuild is addition, as CNR's was). **2021 is shown both as filed (FCA from 17
January) and with the company's own *"Add: Industrial free cash flows of FCA, January 1 - 16, 2021 | (1,813)"*** (20-F
FY2022), which is the one-perimeter figure. **Windows before 2019 are refused:** they would need PSA's 2016-2018 cash flows
with Opel acquired mid-2017 and Faurecia consolidated, and FCA's with Magneti Marelli, on bases no filing reconciles; the
refusal is the CNR rule, not a data gap.

### MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25]
Hybrid coupons (€2.2bn × 6.250% + €1.8bn × 6.875% + €0.997bn × 8.250% = **€344M a year**, from March 2026) are senior to the
common holder and are deducted **in the right-hand column only**, as a pro forma of today's capital structure.

| window | (c) = capex | (c) = capex + equity contributions to JVs | (c) = capex, 2025 provision build charged | D&A end (INVALID, shown) | capex end less hybrid coupons |
|---|---|---|---|---|---|
| **5-yr 2021-25, one perimeter (FCA stub added) — the default [E2-42]** | **3,813** | 2,245 | 1,846 | 7,222 | 3,469 |
| 5-yr 2021-25 as filed | 4,175 | 2,607 | 2,208 | 7,584 | 3,832 |
| 7-yr 2019-25 pro forma | 3,706 | — | 2,301 | 7,497 | 3,362 |
| 3-yr 2023-25 | **1,094** | (992) | (2,183) | 4,281 | 751 |
| 2-yr 2024-25 | **(5,003)** | — | — | (1,310) | (5,347) |

- **Combined range, valid constructions: about €(5.0)bn to +€3.8bn a year**; on the five-year default, €1.8-3.8bn.
- **Is that range too wide to reach a conclusion? YES [E4-25].** It spans zero. The five-year mean is three shortage years at
  +€5.7-13.3bn and two bust years at −€5.0bn; no window is "the" earning power, and **[E4-41] requires the lucky years
  normalised down before the mean is trusted**: 2021-2023 carried the industry-wide shortage pricing Q2 measured (NA net
  price ≈ +€7.2bn in 2022-23 alone). Normalised, the five-year figure is an upper bound, not a centre.
- **Distorted years named [E5-11]:** 2020 (pandemic, pro forma), 2021-2023 (shortage pricing, favourable), 2024 (inventory
  correction), 2025 (tariffs, programme cancellations, warranty). **And the 2025 OCF is flattered by unpaid charges:**
  total provisions rose **€23,080M → €32,913M** (Note 21: product warranty and recall €9,308M → €14,124M; commercial risks
  €3,118M → €8,781M), and the company says ~€2bn of H2 2025 charges will be paid in cash in 2026 (*"Includes ~€2 billion of
  cash payments related to H2 2025 charges, of which €0.9 billion was paid in H1 2026"*, Q2 2026 release). The
  "provision build charged" column moves that €9.8bn into the window, the HMC precedent for unpaid EV provisions.
- **Maintenance capex — a DISCLOSED JUDGMENT, and this is the exception class [E3-44, E5-20]. The D&A end is INVALID.**
  Industrial capex was **1.39x D&A over 2021-2025 (1.44x over 2019-2025)** while consolidated shipments fell (5,836k →
  5,484k) and U.S. unit sales fell 29% (2021-2025): no growth to capitalise, so the excess over D&A was spent to stand
  still. **Capitalised development is where the proof sits:** €18,671M added 2021-2025, €9,904M amortised, **€7,223M written
  off** (€6,190M in 2025 alone, with *"Platform impairments"* €6,583M and *"Costs related to product plan realignments and
  program cancellations"* €9,072M excluded from AOI). **Treatment: capitalised development is capex, deducted in full in
  (c); expensed R&D (€2.9-3.3bn a year) is already inside OCF; nothing is added back.** An amortisation charge of ~€2bn a
  year understated development spend of €3.1-4.4bn a year, and the written-off balance shows the spend did not maintain the
  position. (c) is judged **at total capex, with the JV-contribution column as the upper end** (the battery JV contributions were spent to keep a product line competitive and *"Battery JVs"* €2,054M was written off
  in 2025; the Leapmotor stake is not written down). The 2026 guidance puts *"Full-year capital expenditures and R&D spending
  estimated at 6.5% - 7.0% of Net revenues"* (Q2 2026 release), i.e. no step down in spending.
- **Stock compensation subtracted in full [E5-06]: RESOLVES and is COMPLETE** — PSU/RSU expense found for every year 2019-2025
  (both predecessors for 2019-20) and the employee share purchase plan cost added for 2023-25 (plans of November 2023,
  November 2024, September 2025; none found for 2021-22); equity-settled (*"together with a corresponding increase in
  equity"*); cash-settled awards, where any, sit in OCF. Material? No (€103-225M a year against €5-23bn of OCF), so the
  [E3-70] market-value measure would not move the range.
- **If the capex band changes the verdict → UNKNOWABLE:** the valid band already spans zero on every window but the
  five-year.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · [x] **gruesome** — capital spending above depreciation every year, owner earnings of ~€3.8bn at
  best on €95.6bn of non-current assets (≈4%), negative in two of the last three years; **2024-2025 Industrial free cash
  flows €(10,570)M**. [E4-43]'s good class needs an attractive return on the added capital; the filings show the added
  capital written off.

### Staying power — score all three **[E5-11]**. The liquidity is real, stated first.
- (1) **Large and reliable stream of earnings: NO.** AOI €24.3bn (2023) → €(0.8)bn (2025); owner earnings +€13.3bn → −€5.0bn.
- (2) **Massive liquid assets: YES on cash, partly on lines.** At 2026-06-30: industrial cash €31,217M plus securities €604M;
  *"Industrial available liquidity"* €44,145M including *"Undrawn committed credit lines"* €13,839M (down from €18,287M in
  six months: *"€4.1 billion reduction in available credit lines"*); **industrial net financial position €10,035M, of which
  €4,927M is the March 2026 hybrid capital** (€5,108M, ~€1.76 a share, without it). The lines are *"the kindness of
  strangers"* [E5-39] and are not counted as cash.
- (3) **No significant near-term cash requirements: NO.** Current provisions €14,317M at 2025-12-31 (warranty €4,562M,
  sales incentives €5,321M, commercial risks €2,779M); ~€2bn of H2 2025 charges payable in 2026; €2.5bn of bonds repaid in
  H1 2026 and **$2.5bn raised at 6.750% (2031) and 7.400% (2036)** on 2026-09-10 (424B5, 0001193125-26-389250); and **the
  lender's €28,406M of debt** (securitisations €19,084M) a debt that grew €15.2bn in eighteen months (from €13,156M at 2024-12-31), which must
  be refinanced continuously in the market the maker's credit now prices at 6.75-7.40% in dollars.
- **Leverage, named and quantified [E4-16, E3-29]:** industrial gross debt €23,656M, net cash €10,035M including hybrids;
  consolidated net financial position **€(16,382)M** (the lender's €(26,417)M). **Coverage [E2-54]:** interest paid €2,245M in
  2025 against interest received €2,556M (consolidated, Note 31), but industrial operating cash flow net of capex was
  **€(4,040)M** (2024: €(4,017)M), so interest was met from the cash pile and its yield, not *"comfortably met out of current
  cash flow net of ample capital expenditures"*. **Terms [E3-52]:** the hybrids carry no maturity
  and deferrable coupons; the bonds and securitisations do. **Jurisdiction [E3-66]:** Dutch N.V.; anchor holders ~46% of
  votes including a state shareholder.

### Name the specific way THIS business dies **[E2-27, E3-24]** — exposure, not experience **[E4-40]**
**THE PASS-THROUGH (the eleventh shape, TM's), run into THE CASH IS SPENT UNDOING PAST WORK (the fourth, Boeing's), with the
self-liquidating distribution of the fifth [E2-60] in between. No new shape: the three registered shapes in sequence.**
- **The mechanism.** Every maker spends above depreciation to replace the same volume, each round rational and collectively
  neutralising **[E2-27]**; in the lucky years the price stays home briefly (2021-23), then flows back to the customer as
  incentives **[E3-62]** (Q2); the cash of the good years is distributed (€24.7bn of dividends and buybacks 2021-2025) rather
  than retained against the bad **[E2-60]**; and the next years' cash goes to undoing the last plan (€9,072M of cancellations,
  €6,583M of platform impairments, €4,130M of warranty re-estimates on *"a deterioration in quality"*, €14.1bn of warranty
  provisions and €8.8bn of commercial-risk provisions to be paid). **It does not die of insolvency. It dies of return on
  capital for the common holder**, who now also stands behind €4.9bn of hybrids and a lender with €28.4bn of debt.
- **Quantified from filed figures.** *A repeat of 2024-2025* (Industrial free cash flows €(10,570)M over two years) against
  industrial net cash of €5,108M excluding hybrids (€10,035M with them) and ~€1.1bn of the announced 2026 charge payments
  still to come: **industrial net cash is exhausted inside two such years**, leaving the €13.8bn of lines and market access for
  both the maker and the lender. *Against it:* H1 2026 IFCF €(921)M, better by €2.1bn year on year; €44.1bn of industrial
  available liquidity; no dividend.
- **Likelihood:** the owner's-return death — **[x] likely** (it is the filed record of 2021-2025, and the 2026 guidance is
  *"Low-Single Digit %"* AOI); insolvency of the maker — **[x] a low-level possibility** (liquidity and hybrids buy time);
  a funding squeeze at the lender in a credit downturn that also cuts vehicle demand — **a real possibility**, not quantifiable
  from the filings beyond its size.
- **VERDICT: NOT ISSUED — Q2 closed the file.** *For the record only:* **Q4 would read UNKNOWABLE on the range [E4-25]**
  (valid owner earnings span €(5.0)bn to +€3.8bn a year and the corpus says that range is the conclusion); survival of the
  maker over the next two to three years is supported by liquidity, not by earnings; gruesome [E4-20]; [E5-11] one of three.

---
⛔ **Q5 did not open for entry.** Q1 IN · Q2 OUT. What follows is arithmetic under operator rule 3, carrying no entry
language.

---
## COMPUTATION — NOT A CLEARANCE

### THE PRICE AND THE PASS/FAIL LINE (the operator's instruction of 2026-09-01)
- **Price €4.670** (Euronext Milan STLAM, close 2026-09-11, Yahoo, aggregator flagged) × **2,900,941,252** common shares
  outstanding (H1 2026 semi-annual report, 6-K 0001605484-26-000064) = **cap €13,547M**. Special voting shares excluded
  (Step 0). NYSE $5.40 ÷ ECB 1.1592 = €4.658.
- **Sovereign EUR 3.83%** (ECB AAA 30-year, 2026-09-10, `tools/sources.py`); USD 5.35% shown only for reference.
- **PASS/FAIL: FAIL at Q2** (OUT, on the business as constituted).

### What the buyer is paying for, in words
€13.5bn buys a vehicle maker that earned about €3.5-3.8bn a year of owner earnings over five years that included the best
pricing the industry has had and the worst self-inflicted correction, and lost €5bn a year in the last two; with €10bn of
industrial net cash that is half hybrid capital, €32.9bn of provisions (up €9.8bn in a year) to work through, a lender
carrying €28.4bn of debt, and three shareholders holding 46% of the votes. **The price assumes neither 2021-2023 nor
2024-2025 is the normal year, and the filings do not say which is.**

### 1. THE YIELD
- Owner earnings less hybrid coupons ÷ €13,547M: **five-year default 25.6%** (€3,469M); five-year with the 2025 provision
  build charged **11.1%**; with JV contributions in (c) **14.0%**; seven-year pro forma 24.8%; **three-year 5.5%** (€751M);
  **two-year (39.5)%**; three-year charged (18.7)%. Sovereign **3.83%**.
- **Spread across valid constructions: (39.5)% to +25.6%.** [E4-25]: *"Usually, the range must be so wide that no useful
  conclusion can be reached."*

### 2. WHAT THE PRICE ALREADY ASSUMES
- At the three-year owner earnings the ~10% floor needs **~4.5% perpetual growth** from a business whose shipments fell 6%
  and whose U.S. units fell 29% in five years; at the five-year default it needs **none** — and needs the shortage years to be
  representative, which Q2 found they were not. [E4-35]: sustained growth is the rare case.

### 3. WHAT YOU ARE PAID
- Points over the 3.83% sovereign: **(43.3) to +21.8** across the valid range. No single figure is honest.

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01] — engine display, no vote
- Owner earnings less hybrid coupons capitalised at the ~10% floor with no growth, per share: **five-year default ~€12**;
  seven-year pro forma ~€11.5; with JV contributions ~€6.5; five-year with provisions charged ~€5; three-year ~€2.5; two-year
  and three-year-charged **nil**. Plus industrial net cash excluding hybrids ~€1.76 a share. **Roughly €0 to €15 a share.**
- **Current price €4.67: inside the range.**

### THE FLOOR, THEN THE RANKING [E4-28, E4-21]
- Honest pre-tax expectancy at this price: **not statable** — the range spans negative to above 20%; the floor verdict
  cannot be reached, so nothing is ranked. *(Q5 did not open; this line is the computation's result, not a verdict.)*
- **Screamer test [E4-01]:** does the price clear the conservative case? **No** — the conservative case is negative owner
  earnings. **Inside the range → no useful conclusion, move on.**
- **Windage count [E4-11]:** conservatism applied once, in (c) at total capex (the corpus's exception class); the hybrid-coupon
  deduction and the provision column are claims and costs, not windage.
- **The 2023-24 buybacks against this range:** ~306M shares at ~€17.7 sit above the whole range (Q3 flag).

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

### ⚠ RECORDED, NOT GOVERNING — nothing is owned and nothing is armed.
**Pre-committed reopening conditions [E1-02], in words (the QLYS ruling: a Q2 failure gets no price alert):**
- **Q2 reopens only on units, not dollars [E4-55]:** U.S. market share back above its 2021 level (11.5%) for two consecutive
  20-F years **with** North American net price positive in the AOI walk in a year of flat industry volume ([E2-44](1)), and
  EU30 share stable while Europe's net price is positive. One quarter of share gain (Q2 2026: 7.4% North America, +40bp) is
  not it.
- **Q3 would need:** AOI adjustments that exclude no warranty, recall, penalty or labour cost for three consecutive years, or
  pay moved to a measure that includes them; a guidance year met without a reset.
- **Q4 would need:** five consecutive years of positive owner earnings at the capex end, and industrial net cash rebuilt
  excluding hybrid capital.
- **What would prove this file wrong:** North American margin and share rising together while GM's and Ford's filed shares
  fall; that would be a position being won, and Q2 would be re-run on it.
- **Thesis-breaking metric (for the file's OUT):** none needed; the file holds no position. **Next catalysts:** Q3 2026
  shipments (October 2026), FY2026 20-F (February 2027), the Paris investigating judge's referral decision, the SDNY class
  action ruling.
- **Sell rule [E2-28], moat downgrade [E4-17, E3-30], position size:** not applicable — nothing owned. *(For the record:
  2024-2025 was not an aberrational cycle on the filed unit series; it was the slip.)*
- **VERDICT: NOT ISSUED.** The file closed at Q2.

---
## SELF-AUDIT (operator rule 6)
- [x] Questions answered in order; the file stopped at Q2 and Q3-Q6 carry RECORDED, NOT GOVERNING banners; the price block
  carries **COMPUTATION — NOT A CLEARANCE** and no entry language.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. Q1 IN is unqualified. The PROVISIONAL marks
  sit inside Q2's OUT on two legs (South America, MEA) and the reason they cannot reverse the verdict is written.
- [x] No UNRESEARCHED verdict issued. The document asked for at Q2 (a peer's filed South American margin) is named and shown
  not to be verdict-changing.
- [x] Q4's would-be UNKNOWABLE states what cannot be known: which of the shortage years and the bust years is the normal year.
- [x] Step 0: 20-F FY2025 read with accession `0001605484-26-000021`; OCF €(4,650)M cross-checked statement = MD&A = companyfacts,
  and the cross-check found the 2023-24 restatement.
- [x] Owner earnings on multi-year means, five windows, (c) disclosed with the D&A end ruled INVALID; SBC resolves and is
  complete; the merger crossed only on a rebuilt pro forma (2019-20) with the FCA stub added for 2021.
- [x] Competitor row filled by region on filed margins and units (GM, Ford, VW, Renault; Toyota and Honda carried from the
  TM/HMC rows); Stellantis's figures in those rows re-read from its own 20-Fs; row limits stated.
- [x] Sovereign for the earnings currency, from the issuing authority's named source (ECB), dated; EUR argued with the
  regional profit split.
- [x] Value stated as a round-number range; one bar (screamer) used; windage count stated.
- [x] Prices dated; aggregator used for live quotes only and flagged; the ECB reference rate for FX.
- [x] Every ledger id cited checked against `principle_ledger.csv` (95 distinct ids in this file, none missing).
- [x] Run committed to git with a pathspec after each section.

**Errors of my own caught before commit, recorded (operator rule 6):**
1. The Q1 append first failed on a bash heredoc containing an apostrophe (the brief's warning); nothing was written; the
   section was re-appended from a file with `append.py`.
2. A Q2 draft claimed Stellantis's 2025 figure *"sat 9th of 11"* in the HMC row; the HMC row does not carry every peer's
   2025 figure, so the rank was replaced by the five peers that do.
3. A Q2 draft said *"the three years since 2023 are negative at the capex end"*; the arithmetic shows 2023 at +€13.3bn and
   the three-year mean at +€1.1bn; corrected to "2024 and 2025 were each about €(5.0)bn".
4. A Q2 draft gave GM's 2021-2023 margin as *"8.6-10.1%"* (a GMNA-only figure); corrected to GMNA+GMI 8.6-9.8%.
5. A Q3 draft called the Chairman *"Exor's chief executive"* from memory; the 20-F says he *"established Exor N.V."*; the
   filing's words replaced mine.
6. A Q3 draft put Ford's Model e losses in euros; they are dollars.
7. The 2023 AOI-walk chart measurement disagrees with the 2023 narrative on one bar; recorded beside the table rather than
   dropped.

## REGISTER
- Verdict: [x] **OUT (about the business)** at Q2.
- One line: **STLA — Q1 IN / Q2 OUT: a vehicle maker whose best years were bought with share (U.S. 12.6% → 7.6%, EU30 22.1% →
  16.0%) and whose price was given back *"relative to peers"*; €4.67, cap €13.5bn, owner earnings €(5.0)bn to +€3.8bn a year,
  price inside a range too wide for a conclusion. FAIL at Q2.**

### TOOLING AND DOCUMENT DEFECTS FOUND
1. **The skip reason's cause for STLA is the USD unit filter and US-GAAP tag names, not companyfacts lag** (FY2025 20-F is
   ingested). The 10:05 handoff note's first two causes confirmed for a EUR filer.
2. **`companyfacts` carries two companies under one element for FY2019-2020** (FCA €10,462M / €9,183M from FCA's 20-Fs; PSA
   €8,667M / €6,241M from Stellantis's) because PSA was the accounting acquirer. **No vintage rule in `sources.annual()` can make
   that series one company**; `name_change_note` fired correctly; a reverse-acquisition flag would be the narrower test.
3. **The 2023 and 2024 consolidated OCF were restated by a classification change** (€22,485M → €17,954M; €4,008M → €1,535M);
   a screen reading the latest vintage would see a collapse in 2023 that did not happen at the industrial level.
4. **The AOI walks in the FY2023 and FY2024 20-Fs are unlabelled images**, so the pricing line the TM row recorded as BLOCKED is
   recoverable only by measuring bars (`charts/measure.py`, endpoints reproduced within 4%); the FY2025 charts carry labels.
5. **A bash heredoc with an apostrophe fails silently as a parse error before any command runs** (the brief warned); section
   files plus `append.py` avoid it.
6. The Renault FY2023 results report URL (`assets.renaultgroup.com`) returned HTTP 403 to a scripted fetch; Renault 2023 margin
   derived from the FY2024 report instead and labelled.

### DEFECTS IN THE BRIEF
1. **"Special voting shares carry votes, not economics"** is right in substance but not absolute: Dutch law forces a minimum
   entitlement (1% of nominal, **€86,652 a year**, and €8.7M nominal on liquidation). Excluded as immaterial, and said so.
2. **The brief listed segments including "China/India & Asia Pacific" and "Maserati"**; from 2026-01-01 Maserati is eliminated as
   a segment and China and India & Asia Pacific become "Asia Pacific" (H1 2026 report). The 2021-2025 row uses the old segments.
3. **"Whether its lending sits in joint ventures off its balance sheet"**: it does in Europe and does not in the U.S.; the U.S.
   captive has grown to the point where the lender's debt (€28.4bn) exceeds the maker's (€23.7bn), which the brief's framing
   (financing as a side question) under-weights.
4. No other defect found; the brief named no expected verdict and no effort level (the CGNX prohibition held).
