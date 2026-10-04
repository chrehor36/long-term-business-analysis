# Company Run — Chubb Limited (CB) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file and that
document disagree, that document governs.

**WAVE 6 of the operator's watchlist queue; MINI BERK insurance track.**
**Sector method applies and was read in full, both amendments included:**
`Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`
— **two measurable components plus a judgment [E5-46, E5-47, E5-48, E5-50]**, float as the
**FUNDING** of the investments and never an earnings stream, and **[E3-69]**'s
underwriting-loss-to-float-developed as the profitability measure rather than the combined ratio
alone. Step 2 is **DIAGNOSTIC, NOT ADDITIVE** (the MKL amendment's arithmetic correction).

**CIK 0000896159** (`Chubb Ltd`), found by `tools/sources.py:cik_for('CB')` — not taken from the
brief. Former name **ACE Ltd** to 2016-01-15 (submissions `formerNames`): the registrant is the
old ACE Limited, which bought The Chubb Corporation on 2016-01-14 and took its name. **SIC 6331,
Fire, Marine & Casualty Insurance.** Swiss-incorporated, headquartered in Zurich, USD-reporting.

**All arithmetic in this file is reproduced by `Test Runs/_research 2026-09-19 CB/arith.py`
(output `arith_out.txt`) and `peers/build_row.py` (output `peers/row_out.txt`).** Every input is
hand-read from a filed statement and carries its accession in the script comments.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**VERDICT LINE: Q1 IN · Q2 IN (NARROW) · Q3 IN (as a GATE) · Q4 IN · Q5 NOT IN — quit on at the
[E4-28] floor, on PRICE · Q6 re-look bands, no position.**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]** — struck fresh for this run:
- **5.34% · 2026-09-18 · US Treasury daily par yield curve, 30-year** (the issuing authority;
  FRED DGS30 is the fallback and was not used). `tools/sources.py:sovereign('USD')`.
- **The earnings currency, argued rather than assumed.** Chubb reports in USD and is
  USD-functional at the parent. Of FY2025 net premiums written of $54,842M, the segments written
  substantially in USD are North America Commercial $21,280M, North America Personal $7,024M and
  North America Agricultural $2,926M = **$31,230M, 57.0%**. Global Reinsurance ($1,309M) is mixed.
  **Overseas General ($15,024M) and Life ($7,279M) — $22,303M, 40.7% — are earned overseas**, and
  Overseas General's own filed split is EMEA 43% / Asia 36% / Latin America 20%, with Life
  concentrated in Asia. Chubb holds cross-currency swaps hedging the net investment in foreign
  subsidiaries in **GBP 957M, JPY 43.0bn, CHF 96M and CNH 9.3bn**, and EUR 1.8bn of debt.
  **This is FINDING 8 of the sector method's first amendment recurring: the framework has no
  stated answer for one company earning in many currencies.** Per that amendment's standing
  instruction the exposure is stated, **the reporting currency's sovereign is used, and the
  choice is disclosed as unresolved.** The direction of the error is not neutral and is stated:
  Japan's 30-year is far below the US 30-year and the euro's is below it too, so using the USD
  rate is the **conservative** choice for the 41% earned abroad.
- FX: none needed. The quote and the reporting currency are both USD. No ADR.

**The filing was read — not tagged data [E3-27, E4-14].** No figure in this run comes from XBRL;
`tools/run.py` was not used for this filer.
- [x] MD&A  [x] cash-flow statement including its detail lines  [x] footnotes (Notes 1, 2, 8, 13,
  14, 15, and the Note 8 loss-development tables in full)
- **FY2025 Form 10-K, period 2025-12-31, filed 2026-02-27, accession `0000896159-26-000005`,
  document `cb-20251231.htm`.** Also read: **FY2023 10-K `0000896159-24-000003`**, **FY2021 10-K
  `0000896159-22-000005`**, **FY2018 10-K `0000896159-19-000005`** (to reach 2016), **Q2 2026
  10-Q `0000896159-26-000017`**, **DEF 14A 2026-04-03 `0001104659-26-039513`**, **DEF 14A
  2025-04-01 `0001104659-25-030554`**, and the four quarterly earnings 8-Ks with their EX-99.1
  releases and EX-99.2 Financial Supplements (`0001193125-26-310312`, `0001193125-26-166937`,
  `0001193125-26-035589`, `0001193125-25-245172`). **The 8-K EX-99.1 was pulled before scoring
  [E4-29] and [E4-22]'s third flag, per the standing CGNX rule.**
- **Figures cross-checked against the filed statement, four of them:**
  1. **Total Chubb shareholders' equity recomputed from the balance sheet identity:** total assets
     $272,327M − total liabilities $192,548M − noncontrolling interests $6,022M = **$73,757M**,
     which is the filed line exactly. (This is the [E5-32] Salomon cross-check: equity from A−L.)
  2. **The whole current-accident-year reconciliation re-derived:** for each of 2019–2025,
     `CAY loss ex CAT = losses and LAE − catastrophe losses gross + PPD gross` reproduces the
     filer's own B line to the dollar in all seven years (script asserts it).
  3. **P&C underwriting income built two ways:** net premiums earned $45,790M − losses $27,077M −
     acquisition and administrative $12,185M = **$6,528M**, which equals the segment note's
     $7,309M of segment underwriting income less the $781M corporate underwriting loss.
  4. **Share count** — see Stage 0(a) below.

**Ladder rungs used:** SEC XBRL not used at all; SEC EDGAR primary documents for Chubb and for
every peer. No aggregator except the live quote, flagged.

---
## STAGE 0 — THE SECTOR METHOD'S ARTIFACT CHECK

### 0(a) — SHARE CLASS AND COUNT, BY HAND OFF THE COVER, WITH THE SWISS DEFINITION CHECKED
Chubb has **one class** of Common Shares, CHF 0.50 par value. The brief asked for the
cover-definition check the ERIC and IHG runs found, and here is the answer, with the arithmetic:

- **10-Q cover, 2026-07-28 (accession `0000896159-26-000017`), line 60:** *"The number of
  registrant's Common Shares (CHF 0.50 par value) **outstanding** as of July 20, 2026, was
  **385,799,859**."*
- **The trap tested, not assumed.** The same 10-Q's balance sheet at 2026-06-30 reads
  *"400,120,847 and 412,107,421 shares **issued**; 385,634,049 and 391,101,227 shares
  **outstanding**"* — a gap of **14,486,798 treasury shares** at 2026-06-30. The cover figure
  (385,799,859) sits **beside the outstanding line (385,634,049), not the issued line
  (400,120,847)**. **The cover is net of treasury. Treasury shares ARE excluded. Confirmed by
  arithmetic, not by the caption.** Using the issued figure would have overstated the market
  capitalisation by **$4,879M**.
- Cross-check on a third document: the 2026 proxy states **390,229,029 Common Shares outstanding
  at 2026-03-06**, falling to 385.8M by 2026-07-20 — consistent with continued repurchase.
- Options and rights outstanding: **9,222,037 at a weighted-average exercise price of $213.93**
  (proxy). In the money, and about 2.4% of the count; noted, not added.
- **Count used: 385,799,859.**

**PRICE: US$340.64 at the 2026-09-18 close** (`tools/sources.py:price('CB')`, aggregator —
**FLAGGED**, live quotes only). **MARKET CAPITALISATION: US$131,419M.**

### 0(b) — INSURER, FLOAT-BEARING HOLDING COMPANY, OR NEITHER — AND BOTH RATIOS
**Chubb is an insurer, not a holding company that owns one.** Six segments, all insurance;
$54.8bn of net premiums written; $88.0bn of unpaid losses. This is not the WTM case.

**CONVENTION 4 float** = unpaid losses and LAE + unearned premiums − reinsurance recoverable on
losses − insurance and reinsurance balances receivable − deferred policy acquisition costs. **The
word "float" does not appear in Chubb's 10-K in [E5-46]'s sense and Chubb publishes no float
figure**, which is the WTM finding recurring; the construction is shown rather than cited.

| 12/31 | float $M | ÷ investments | ÷ Chubb equity | investments ÷ equity |
|---|---|---|---|---|
| 2020 | 53,989 | 45.5% | 0.94x | 2.06x |
| 2021 | 57,843 | 47.3% | 0.99x | 2.10x |
| 2022 | 58,637 | 51.6% | 1.16x | 2.25x |
| 2023 | 61,690 | 45.1% | 1.04x | 2.30x |
| 2024 | 64,947 | 43.1% | 1.01x | 2.35x |
| **2025** | **68,007** | **40.3%** | **0.92x** | **2.29x** |
| 6/30/26 | 68,084 | 39.4% | 0.90x | 2.29x |

*(Subtracting prepaid reinsurance premiums as well — the same logic that removes the other assets
already standing against the liability — gives $64,133M at 2025, a 5.7% reduction. Both are
shown; the recipe as written is used.)*

**BOTH RATIOS, STATED, against the panel (the second amendment's requirement):**

| | float ÷ investments | investments ÷ equity |
|---|---|---|
| BRK 2010, the method's calibration **[E5-46]** | 41.8% | 0.45x |
| BRK 6/30/26 (this project's BRK run) | 24.6% | 0.96x |
| **CB 12/31/25** | **40.3%** | **2.29x** |
| MKL | 50.3% | 2.01x |
| Loews consolidated | 41.8% | 2.96x |
| CNA | 45.8% | 4.34x |
| WTM | 22.0% | — |

**What they imply, stated.** On the first ratio **Chubb sits almost exactly on [E5-46]'s own
calibration point** — float funds 40% of the portfolio against Berkshire's 41.8% in 2010. So the
first amendment's low-side guard does not bite and **step 2 is a MAJOR term here, not a rounding
item**: this is the first name in the Mini Berk panel where the cost of float carries real weight.
**On the second ratio Chubb is the most stretched name in the panel except Loews and CNA — 2.29x,
above Markel's 2.01x and five times Berkshire's 0.45x.** CONVENTION 5's rationale applies at full
strength: [E5-46] licenses counting the portfolio gross **on the express condition that
underwriting breaks even**, and at 2.29x *most of the portfolio is funded by liabilities*, so the
valuation leans almost entirely on a condition the same passage calls *"volatile, swinging
erratically between profits and losses."* **Neither ratio is a threshold and neither disqualifies
the name. What they do is tell the run where the answer lives, and here it lives in whether the
break-even condition holds — which is exactly what Q2 measures.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Chubb sells promises to pay for
future accidents, collects the money now, and pays the claims later — five to ten years later in
casualty, decades later in workers' compensation. Two separate earning engines, and the filing
names them itself in Item 1: *"We generate earnings from three primary sources of income: P&C
underwriting income, investment income, and life segment income."*

1. **The underwriting spread.** Take in $54.8bn of net premium; pay out $27.1bn of losses and
   $12.2bn of commissions, brokerage and overhead on the P&C book. What is left, **$6,528M in
   2025**, is what the promise sold for above its cost. Chubb's whole operating philosophy, as
   filed, is to shrink rather than write at an inadequate price — the FY2025 MD&A reports Major
   Accounts premium up only **1.4%** because of *"rate decreases in our Large Risk and E&S
   brokerage property lines"*, and the Q2 2026 release says *"we will not underwrite knowingly at
   a loss."*
2. **The portfolio.** The money held between premium and claim — **$68.0bn of float** — plus
   $73.8bn of shareholders' equity and $17.6bn of borrowed money funds a **$168.7bn** portfolio
   ($122.7bn of available-for-sale fixed maturities, $17.2bn of private equities, $10.8bn of
   public equities, $10.7bn of other, $4.8bn short-term). It earned **$6,465M** in 2025 at a
   **4.5% book yield against a 5.0% market yield on fixed maturities**, so the yield is still
   rising as the book rolls over.

**Where the earnings actually come from — the brief's question, answered in filed numbers.** Of
FY2025 pre-tax operating income of **$12,312M** (income before tax $13,044M less $211M of
realised gains, plus $288M of market-risk-benefit losses, less $809M of private-equity marks):

| | $M | share |
|---|---|---|
| P&C underwriting income (after the $781M corporate run-off underwriting loss) | 6,528 | 53% |
| Net investment income | 6,465 | 53% |
| Life Insurance segment underwriting result | −12 | 0% |
| Equity in partially-owned entities and other operating income | ~1,400 | 11% |
| less interest expense, purchased-intangible amortisation, integration and severance | −1,144 | −9% |
| less noncontrolling interests | −312 | −3% |
| **pre-tax operating income attributable to Chubb** | **12,000** | 100% |

**The answer is: roughly half and half, and the split has been stable.** Underwriting is not a
loss leader funding a portfolio (the ordinary insurer shape), and the portfolio is not a
sideshow. **Chubb Life is the one leg that is purely a portfolio: net premiums earned $7,224M
against losses $109M, policy benefits $4,961M, acquisition $1,330M and administrative $836M =
minus $12M of underwriting result, and its entire $1,242M of segment income is investment income
plus other income.** Under [E5-48] that income is removed from component 2 as portfolio income,
which is why the Life segment contributes almost nothing to the two-component sum below.

**The segments as filed, FY2025 ($M):**

| segment | NPW | NPE | underwriting income | net inv. income | segment income | CR | CAY CR ex CAT |
|---|---|---|---|---|---|---|---|
| North America Commercial P&C | 21,280 | 20,381 | 3,783 | 3,840 | 7,559 | 81.4 | 80.8 |
| North America Personal P&C | 7,024 | 6,763 | 573 | 486 | 1,048 | 91.5 | 72.3 |
| North America Agricultural | 2,926 | 2,919 | 517 | 86 | 577 | 82.3 | 85.0 |
| Overseas General | 15,024 | 14,374 | 2,156 | 1,139 | 3,167 | 85.0 | 84.8 |
| Global Reinsurance | 1,309 | 1,353 | 280 | 354 | 634 | 79.3 | 74.3 |
| Life Insurance | 7,279 | 7,224 | NM (−12) | 1,127 | 1,242 | n/a | n/a |
| Corporate (A&E and non-A&E run-off) | — | — | −781 | −93 | — | — | — |
| **Total** | **54,842** | **53,014** | **6,528 (P&C)** | **6,465** | **14,227** | **85.7** | **81.9** |

**North America Commercial is the company**: 39% of premium and 53% of segment income. North
America Personal is the highest-quality book in the file on a normalised basis — a **72.3%
current-accident-year combined ratio excluding catastrophes** — and the most catastrophe-exposed
(its reported 91.5 carries 25.5 points of California wildfire and other cat load). **32% of
segment income does not reach pre-tax income** ($14,227M to $13,044M less the corporate items,
through $764M of interest, $781M of run-off underwriting loss, $301M of amortisation and $79M of
integration and severance, partly offset by $676M of corporate other income).

**The scarce input this business controls.** Not the product: [E2-70] settles that and Chubb's own
risk factors agree (*"Insurance and reinsurance markets are highly competitive"*). Three things
are genuinely scarce and Chubb names them in Item 1: **(i) local admitted licences** — *"one of
the few international insurance groups with a global network of licensed companies able to write
policies on a **locally admitted basis**"*, which is what a multinational buying one programme
across fifty jurisdictions is actually paying for; **(ii) a balance sheet large enough to carry a
$150M gross limit on a single Bermuda high-excess policy**; and **(iii) the high-net-worth
personal-lines book**, where the product is a claims service and an appraisal capability rather
than a price. The [E5-46] funding advantage — $68bn held at a negative cost — is the fourth, and
it is measured at Q4.

**Will the fundamentals look broadly the same in ten years?** Yes, and this is the class of
business [E3-31] was written about: *"relatively simple and stable in character."* Somebody will
insure a factory in 2036, priced annually, with the money held in between. The specific
uncertainty is not the mechanism but the price level, which is cyclical by the filer's own account
and is addressed at Q2 and Q5, not here.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**State the moat claim honestly before testing it, because the corpus's own verdict on this
industry is hostile.** **[E2-70]**, 1977: *"Insurance companies offer standardized policies which
can be copied by anyone. **Their only products are promises.** It is not difficult to be licensed,
and rates are an open book. There are **no important advantages from trademarks, patents,
location, corporate longevity, raw material sources**, etc."* The sector method quotes it and adds:
*"an insurance underwriting operation is close to a commodity, and the [E3-03] franchise question
is therefore harder here than in retail, not easier."*

**Chubb's own filing agrees, twice, in its risk factors:**
> *"Insurance and reinsurance markets are highly competitive. We compete on an international and
> regional basis with major U.S., Bermudian, European, and other international insurers and
> reinsurers and with underwriting syndicates, some of which have greater financial,
> technological, marketing, distribution and management resources than we do."*

> *"The insurance and reinsurance markets have historically been cyclical, characterized by
> **periods of intense price competition due to excessive underwriting capacity** as well as
> periods when shortages of capacity permitted favorable premium levels. **An increase in premium
> levels is often offset by an increasing supply of insurance and reinsurance capacity**, either
> by capital provided by new entrants or by the commitment of additional capital by existing
> insurers or reinsurers, which may cause prices to decrease."*

**That is [E2-58]'s equation in the filer's own words** — *"persistent over-capacity without
administered prices (or costs) equals poor profitability"*, long-run profitability set by *"the
ratio of supply-tight to supply-ample years"*, and *"nothing fails like success."* **So the moat
claimed here is NOT a product moat.** It is three things, each filing-sourced and each tested
below: **the cost of the funding, the licence network, and the cost base.**

### THE DECISIVE SERIES — the MKL precedent, run on ten years, not five
**[E4-40] is why this comes first:** *"all of us in the industry made a fundamental underwriting
mistake by **focusing on experience, rather than exposure**."* The MKL run of 2026-09-02 closed
Markel at Q2 because its current-accident-year combined ratio was **99.3 / 101.1 / 100.3** for
2023–25 — *"on the business it actually wrote in each of the last three years, Markel's
underwriting lost money in two of them"* — so the entire reported underwriting profit was prior-year
reserve releases, which is **[E4-40]**. **Chubb was put to the same test, over ten years rather
than three, and it passes it.**

Every cell is the filer's own published point. Chubb publishes the decomposition itself in each
10-K MD&A: CAY loss ratio excluding catastrophes, catastrophe points, favourable PPD points,
acquisition ratio, administrative ratio, reported P&C combined ratio.

| year | CAY CR **ex** CAT | + cats | **= CAY COMBINED RATIO INCLUDING CATASTROPHES** | − favourable PPD | = reported P&C CR | expense ratio |
|---|---|---|---|---|---|---|
| 2016 | 88.6 | 4.0 | **92.6** | 4.3 | 88.3 | 30.6 |
| 2017 | 87.7 | 10.2 | **97.9** | 3.2 | 94.7 | 28.9 |
| 2018 | 88.1 | 5.8 | **93.9** | 3.3 | 90.6 | 28.5 |
| 2019 | 89.3 | 4.1 | **93.4** | 2.8 | 90.6 | 28.5 |
| 2020 | 86.8 | 10.6 | **97.4** | 1.3 | 96.1 | 27.6 |
| 2021 | 84.8 | 7.1 | **91.9** | 2.8 | 89.1 | 26.5 |
| 2022 | 84.4 | 6.0 | **90.4** | 2.8 | 87.6 | 25.6 |
| 2023 | 84.1 | 4.5 | **88.6** | 1.9 | 86.5 | 25.9 |
| 2024 | 83.2 | 5.5 | **88.7** | 2.0 | 86.6 | 26.2 |
| 2025 | 81.9 | 6.3 | **88.2** | 2.5 | 85.7 | 26.6 |
| **10-yr mean** | **85.9** | **6.4** | **92.3** | **2.69** | **89.6** | **27.5** |

**Sources:** 2023–25 FY2025 10-K p.51 (`0000896159-26-000005`); 2021–23 FY2023 10-K
(`0000896159-24-000003`); 2019–21 FY2021 10-K (`0000896159-22-000005`); 2016–18 FY2018 10-K
(`0000896159-19-000005`). The 2023 PPD point was **restated by the filer from 2.1 to 1.9** between
the FY2023 and FY2025 10-Ks; both are shown and the later basis is used.

**INDEPENDENT RECONSTRUCTION, because a published non-GAAP point is not evidence on its own.** The
same series was rebuilt from the filer's *dollar* reconciliation table (numerator lines A/B/C/D,
denominator lines E/F, for 2019–2025) without using any published ratio:
**93.33 / 97.34 / 91.86 / 90.08 / 88.40 / 88.57 / 88.22** against the published-points series
**93.4 / 97.4 / 91.9 / 90.4 / 88.6 / 88.7 / 88.2**. **Two independent constructions agree within
0.3 points in every year.** The residual is the treatment of reinstatement premiums and expense
adjustments in the denominator, and is named rather than smoothed.

**THE FINDING, and it is the opposite of Markel's.** **Chubb's current-accident-year combined
ratio including catastrophes has been below 100 in every one of the last ten years, worst year
97.9 (2017, the Harvey-Irma-Maria year), best 88.2 (2025), ten-year mean 92.3.** The reported
underwriting profit is not reserve releases. In 2025 the releases contributed **$1,132M of the
$6,528M of underwriting income — 17%; 83% was earned on the year's own business.** The reserve
release is the icing, not the cake. **[E4-40] is satisfied on exposure, not on experience,
because the series includes 2017 and 2020 — the two worst catastrophe years of the decade — and
they were still underwriting-profitable on the current accident year.**

**And the PPD contribution is DECLINING, which matters at Q4 and Q5, not here:** 4.3 → 3.2 → 3.3
→ 2.8 → 1.3 → 2.8 → 2.8 → 1.9 → 2.0 → 2.5 points.

### THE EXPENSE RATIO TREND — the brief's second series, and it turned
**28.5 (2018) → 27.6 (2020) → 26.5 (2021) → 25.6 (2022) → 25.9 (2023) → 26.2 (2024) → 26.6
(2025).** Four points of improvement to a trough in 2022, then **1.0 point of deterioration over
three years, all of it in the policy acquisition cost ratio (17.8 → 18.6) while administrative
held at 8.0–8.1.** The filer's stated reason, twice: *"an increase in the policy acquisition cost
ratio from **changes in mix of business**"*. **This is the same shape the MKL run found and
recorded against Markel** (expense ratio 34.4 → 35.5 → 36.1), and it is recorded here against
Chubb too. The difference is level: Chubb's 26.6 is **9.5 points below Markel's 36.1** and the
deterioration is 1.0 point against Markel's 1.7. A rising expense ratio in a softening market is
the mechanical signature of a shrinking property book with fixed distribution costs, and it is a
**live Q6 monitoring item**, not a Q2 failure.

### THE COMPETITOR ROW — required [E3-28], EXTENDED FROM MKL RATHER THAN REBUILT
The MKL run built a seven-peer five-year row (`Test Runs/_research 2026-09-02 MKL/competitor-row.md`)
covering **KNSL, ACGL, RLI, WRB, FFH, AXS and WTM**. It is carried forward unchanged on the
reported basis and **extended on the basis this run cares about.** Every accession in that file
was independently re-resolved from each registrant's submissions JSON and **all five matched**.

**BASIS 1 — reported GAAP consolidated combined ratio, 2021–2025 (carried from the MKL run):**

| company | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|---|
| Kinsale (KNSL) | 77.1 | 78.5 | 75.4 | 76.4 | 75.9 | **76.66** |
| Arch (ACGL) | 85.2 | 81.6 | 79.3 | 82.5 | 82.8 | **82.28** |
| RLI | 86.8 | 84.4 | 86.6 | 86.2 | 83.6 | **85.52** |
| **CHUBB (CB)** | **89.1** | **87.6** | **86.5** | **86.6** | **85.7** | **87.10** |
| W. R. Berkley (WRB) | 89.6 | 89.3 | 89.7 | 90.3 | 90.7 | **89.92** |
| Fairfax (FFH) † | 95.0 | 94.7 | 93.2 | 92.7 | 93.0 | **93.72** |
| Markel (MKL) | 90.0 | 92.0 | 98.8 | 95.5 | 94.6 | **94.18** |
| Axis (AXS) | 97.5 | 95.8 | 99.9 | 92.3 | 89.8 | **95.06** |
| White Mountains (WTM) ‡ | — | — | — | — | — | **NOT REPORTED** |
| Berkshire (BRK-B) § | — | — | — | — | — | **NOT REPORTED** |

**BASIS 2 — CURRENT-ACCIDENT-YEAR combined ratio, the same window, same filings: reported plus
each filer's OWN published favourable prior-year development. This is the extension, and it
changes the ranking.**

| company | 2021 | 2022 | 2023 | 2024 | 2025 | mean | yrs |
|---|---|---|---|---|---|---|---|
| Kinsale (KNSL) | 82.6 | 82.9 | 78.6 | 79.1 | 79.8 | **80.60** | 5 |
| Arch (ACGL) | 89.6 | 89.5 | 83.6 | 85.9 | 86.3 | **86.99** | 5 |
| **CHUBB (CB)** | **91.9** | **90.4** | **88.4** | **88.6** | **88.2** | **89.50** | 5 |
| W. R. Berkley (WRB) | 89.7 | 88.9 | 89.5 | 90.3 | 90.7 | **89.84** | 5 |
| RLI | n/a | 95.1 | 95.0 | 92.4 | 89.7 | **93.08** | 4 |
| Axis (AXS) | 98.2 | 96.3 | 91.8 | 92.8 | 91.4 | **94.10** | 5 |
| Markel (MKL) | n/a | n/a | 99.3 | 101.1 | 100.4 | **100.27** | 3 |
| Fairfax (FFH) | n/a | n/a | n/a | n/a | n/a | **NOT COMPARABLE** | 0 |

**The prior-year development points the two bases differ by, with the source of each:**

| company | 2021 | 2022 | 2023 | 2024 | 2025 | how obtained |
|---|---|---|---|---|---|---|
| **CB** | +2.80 | +2.80 | +1.90 | +2.00 | +2.50 | published in points, MD&A combined-ratio table, three 10-Ks |
| KNSL | +5.50 | +4.40 | +3.20 | +2.70 | +3.90 | published ratio *"Effect of prior year development"*; FY2025 `0001669162-26-000015`, FY2023 `0001669162-24-000006`, FY2022 `0001669162-23-000009` |
| ACGL | +4.39 | +7.95 | +4.32 | +3.36 | +3.52 | **computed here**: dollars ($355/769/538/507/600M) ÷ net premiums earned ($8,082/9,679/12,440/15,100/17,065M); FY2025 `0000947484-26-000017`, FY2023 `0000947484-24-000020` |
| RLI | n/a | +10.75 | +8.42 | +6.22 | +6.13 | **computed here**: dollars ($123/109/95/99M) ÷ NPE ($1,144.4/1,294.3/1,526.4/1,614.3M); FY2025 `0001104659-26-018013`, FY2023 `0001558370-24-001599` |
| WRB | +0.08 | **−0.38** | **−0.18** | +0.04 | +0.03 | **computed here**: net prior year development ($6.6/−36.4/−18.9/4.4/3.2M) ÷ NPE; FY2025 `0000011544-26-000005`, FY2023 `0000011544-24-000005` |
| AXS | +0.70 | +0.50 | **−8.10** | +0.50 | +1.60 | published *"Prior year reserve development ratio"*; FY2025 `0001214816-26-000097`, FY2023 `0001214816-24-000024` |
| MKL | n/a | n/a | +0.50 | +5.60 | +5.80 | published *"Prior accident years loss ratio"*; FY2025 `0001096343-26-000020` |
| FFH | n/a | n/a | n/a | n/a | n/a | IFRS 17; no comparable separation of the undiscounted ratio located in Exhibit 99.3 |

**Peers named: 7, of whom 6 supply the metric on this basis.** Fairfax does not: it is a 40-F
IFRS filer whose combined ratio is a declared non-GAAP supplementary measure covering only the P&C
operations, with a basis break at IFRS 17 in 2022 and a *discounted* variant that is a different
construct. **Recorded as NOT COMPARABLE, not estimated.** Kinsale's 2021 and RLI's 2021 could not
be put on this basis from the filings pulled: Kinsale's 2021 point (+5.50) is on the denominator
its FY2023 10-K superseded — **the basis break the MKL row already flagged, still standing** — and
RLI's FY2022 10-K would be needed for 2021. **Both gaps are named; neither is estimated.**

**WHAT THE EXTENSION SHOWS, and it is the reason the brief insisted on it:**
- **The ranking changes.** Reported basis: KNSL > ACGL > **RLI** > **CB** > WRB. Current-accident-year
  basis: KNSL > ACGL > **CB** > WRB > **RLI**. **RLI's headline 85.52 is built on 6 to 11 points of
  reserve releases a year; on the business it actually wrote it runs 93.08 — 3.6 points WORSE than
  Chubb.** A run that stopped at the reported row would have ranked Chubb behind a company it is
  in fact ahead of.
- **Markel is 10.8 points behind Chubb on this basis** and is the only name in the row above 100.
  The MKL verdict replicates from a second direction.
- **Axis inverts:** its 2023 reported 99.9 contained **8.1 points of ADVERSE** development, so its
  current-accident-year ratio that year was 91.8 — better than reported. The basis cuts both ways
  and is not a device for flattering the subject.
- **W. R. Berkley is the reserving-integrity benchmark of the row and it is worth saying so:
  three consecutive years of essentially zero net development on a $10–12bn book (+0.08, −0.38,
  −0.18, +0.04, +0.03 points). Its reported combined ratio needs no adjustment at all.** Its
  level is 0.3 points worse than Chubb's; its honesty of presentation is better than anybody's in
  the row, Chubb included.
- **Chubb is third of seven on the honest basis, at 33 times Kinsale's premium volume.** Kinsale
  beats it by 8.9 points — the MKL run's Kinsale finding recurring — but Kinsale writes E&S only,
  retains almost no catastrophe, runs a 22% expense ratio on a $1.6bn book and has been flat on
  this metric for five years. **Being beaten by a specialist a thirty-third of your size is a real
  limit on the moat claim and it is recorded as one, not explained away.**

**THE ROW'S LIMIT, stated [E3-61]:** *"In some businesses, the participants behave like a demented
Kellogg. In other businesses, they don't … **I think you'd have to know the people involved.**"*
The row shows position. It cannot show conduct, and in an industry whose cycle is made entirely of
conduct that limit is unusually binding.

### THE [E3-03] CRITERIA, SCORED HONESTLY, INCLUDING WHERE THEY FAIL
- **(1) Needed or desired — [x] YES.** Compulsory by statute for autos and employers, by contract
  for every mortgaged building and every financed project. Demand is not the question.
- **(2) No close substitute — [x] at the structural level; [ ] at the product level.** For a
  middle-market commercial package, an E&S property layer or a casualty treaty there are dozens of
  close substitutes and Chubb's own risk factor says rates are competed. For a single global
  programme on locally admitted paper in fifty countries, for a $150M Bermuda high-excess limit,
  and for a $20M coastal home with an appraisal service, the substitute set is small. **Chubb's own
  claim is scale and breadth, not absence of substitutes:** *"Our broad market capabilities …
  **help define our competitive advantage.**"*
- **(3) Not price-regulated — [x] in the main, [ ] and it FAILS outright for part of the book,
  which is recorded rather than glossed.** **North America Agricultural (NPW $2,926M, 5.3% of the
  group) is a literally administered-price business** and the filing says so: Rain and Hail
  *"primarily operates in a **federally regulated program where all approved providers offer the
  same product forms and rates**."* That is **[E2-59]** exactly — administered pricing can floor a
  commodity business's profits, *"but the moat belongs to the **regime**"*, and *"That day is
  gone"* is how it ends. It is carried the way the BRK run carried Berkshire Hathaway Energy: a
  **[E5-40]** good-not-great leg whose regulation is a floor as much as a cap. North America
  Personal homeowners ($7.0bn) is rate-filed state by state; that regulation caps, and California
  is the standing demonstration.

### [E2-44]'s TWO-CHARACTERISTIC TEST — AND IT FAILS THE FIRST HALF, ON THE FILER'S OWN WORDS
*Can it raise prices **"even when product demand is flat and capacity is not fully utilized"**?*
**No, and the current filing is the evidence against it.** FY2025: *"partially offset primarily by
**rate decreases** in our Large Risk and E&S brokerage property lines"*; Major Accounts premium
+1.4%. Q2 2026 release, the CEO: *"**soft market conditions are spreading to certain areas of
casualty while financial lines also remain soft**"* and *"the growth penalty we are paying in
property will dissipate going forward."* **Chubb's answer to inadequate price is to shrink, not
to raise price.** That is disciplined underwriting and it is the opposite of pricing power.

*Can it grow dollar volume **"with only minor additional investment of capital"**?* **Partly.**
Premium grew 61% from 2019 to 2025 while Chubb equity grew 28% and $15.8bn was returned in
buybacks — so the marginal capital intensity is modest, but an insurer's growth does consume
regulatory and rating-agency capital roughly in proportion to premium, and the [E2-44] answer is
"no" in the strong form.

**[E4-37], the inverse metric — the agony of a price rise.** The strongest business is the one
that *"yawns"* at a price increase. Chubb does not yawn; it walks. The 2025 MD&A and the 2026
releases are a record of **declining to write property at the offered price**, which detects a
**moat downgrade in real time** in exactly the way [E4-37] says it should. Direction: **negative in
property and financial lines as of Q2 2026, by management's own account.**

**[E3-33] untapped pricing power — NO, and the [E5-28] scope test explains why.** Claiming that
class is claiming *"a monopoly or a near monopoly"*; Chubb is roughly 2–3% of global P&C premium.
No claim made.

**[E2-53] the dominance class — NO.** Nothing here resembles *"the newspaper itself, not the
marketplace, determines just how good or how bad the paper will be."*

**[E4-36], which of the four causes of extreme success?** **Extreme performance over many
factors** — expense ratio, reserving, geographic licensing, claims, portfolio duration, none of
them extreme alone — with a **wave** component (the 2019–2023 hard market) that is now receding by
the filer's own account. Not a max/min of one variable, not a nonlinear combination. The
many-factors class is ownable; the wave is not, and the run separates them below.

**[E4-04] durability, and the [E5-23] scope test.** Does a lapse in spending destroy the structure
or merely narrow it? **Narrow it.** Nothing in the moat must be periodically *replaced*: the
licences persist, the float replenishes by writing ordinary insurance, the claims organisation is
an overhead. The test is **discipline — not writing bad business — not genius**, which is the
[E4-04] pass condition. There is no competitive-destruction mechanism and no depleting asset.

**[E4-23]/[E2-70] — KEY-PERSON DEPENDENCE, RECORDED HERE AT Q2 AS A MOAT DEFECT, NOT AT Q3 AS A
STRENGTH.** Evan Greenberg has been CEO since 2004 and Chairman since 2007 — the entire record
above is his. And **[E2-70]** says of this industry specifically: *"there is no question that the
nature of the insurance business **magnifies the effect which individual managers have on company
performance**."* **[E4-23]**: *"if a business requires a superstar to produce great results, the
business itself cannot be deemed great."* **The Mayo-Clinic test is LIVE and unanswered here.** The
2026 proxy names Executive Management as four people and combines Chairman and CEO in one of them;
**55.2M shares (17.7% of those voting) were cast AGAINST his election as Chairman in 2026, and
74.7M (22.6%) in 2025** — the largest dissent at either meeting. No successor is identified in
either proxy. **This is the single largest defect in the Q2 case and it is why the class is NARROW
rather than WIDE.**

### THE MOAT CLAIM, AS THE EVIDENCE ACTUALLY SUPPORTS IT
Three things, filing-sourced, relative:
1. **The cost of the funding.** Measured at Q4 under [E3-69]: **−8.58% a year over five years**, on
   average float of $60.8bn. Chubb is **paid** to hold other people's money, and the payment has
   grown in each of the five years (−6.61 → −9.82%). Berkshire on the identical five years, from
   this project's own BRK run: **−3.6%**. **On the corpus's own chosen measure of insurer
   profitability, Chubb's funding is better than Berkshire's.** [E4-32] direction: widening on the
   filed series — with the [E4-40] caveat that the widening coincides with the hard market.
2. **The licence network.** Not replicable in years, and the filer's claim is specific and
   checkable: local admitted paper across the network, plus Lloyd's Syndicate 2488 with **£630M of
   2026 underwriting capacity** and Chubb's own managing agency, plus 87.2% of Huatai in China
   where the competitor set is *"China-based insurers, including state-owned or government related
   entities."*
3. **The cost base.** 26.6% expense ratio against a row whose members run 25–38%, and a
   current-accident-year combined ratio third of seven. **[E2-58]'s one exception is *"a cost
   advantage that is both wide and sustainable"* — and this one is real but NOT wide.** Kinsale is
   8.9 points better. Recorded as good, not as the exception.

- Class: **[x] NARROW** · Direction: **widening on the cost of float 2021–25; NEGATIVE on pricing
  in property and financial lines as of Q2 2026, on management's own statement; expense ratio
  deteriorating 1.0 point off the 2022 trough.**
- **VERDICT: [x] IN — NARROW.** The franchise is the funding structure, the licence network and the
  cost base, exactly as the BRK run found Berkshire's to be the funding structure rather than the
  product. It clears because the current-accident-year series is under 100 in ten of ten years
  including the two worst catastrophe years, and because the relative position is third of seven on
  the honest basis. **It clears NARROWLY, and four defects are on the record and carried to Q6:**
  [E3-03](3) fails outright for the 5.3% of premium written inside a federal programme with
  administered rates; [E2-44] fails on the first half, on the filer's own 2025 and 2026 words;
  there is no untapped pricing power and no dominance; and key-person dependence is unanswered.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`.*

### STEP 1 — THE WEIGHT CASE. Nothing below counts until this is filled in.
- [x] **Daily execution [E3-38, E3-43, E2-70]** — an insurer prices thousands of risks a day and
  sets reserves by judgment. **[E2-70]** is the root and it names this industry: *"their only
  products are promises"* **magnifies** the manager. **[E2-50]** is the sharper form: *"Where
  'earnings' can be created by the **stroke of a pen**, the dishonest will gather."*
- [ ] Control — a marketable minority stake; exit is available.
- [x] **Leverage [E3-29]** — **investments are 2.29x Chubb equity and float is 0.92x.** A 5%
  error in the value of the portfolio is 11% of equity; a 4% error in $88.0bn of gross reserves is
  $3.5bn, 4.8% of equity. Small asset and liability errors move equity materially. This is not
  20:1 banking leverage, and it is not the unlevered case either.

**CASE DECLARED: Q3 IS A BINARY GATE, on two of the three determinants. No price compensates
[E1-16, E3-29, E5-35].** This is the correct weight for any insurer and it is the reason
this gate is scored at length below rather than as an overlay.

### THE BINARY [E5-16] — honesty, dated to when each matter became PUBLIC
*"We are understanding about business mistakes; our tolerance for personal misconduct is zero."*
**No personal-misconduct matter involving Chubb's executive officers was found in the FY2025 10-K
(Item 3 Legal Proceedings, Item 9A Controls), in either proxy, or in any 8-K read.** Internal
control over financial reporting: **no material weakness; PwC's attestation is unqualified; the
10-K records "no changes … that have materially affected" internal controls in Q4 2025.** Statutory
auditor PricewaterhouseCoopers AG (Zurich) and PricewaterhouseCoopers LLP (US) both re-elected at
the 2026 AGM. **Per [E5-17] this is the ABSENCE OF FOUND DISQUALIFIERS, not a finding that the
managers are honest** — *"Sincerity and empathy can easily be faked"* — and per **[E5-32]** the
filed statement is not bedrock either, which is why the equity was recomputed from A−L above.

### STEP 2 — THE FLAGS. Each a prompt to READ, never a verdict. The list is open [E3-68].

**[E4-29] EBITDA — CLEAN, AND TESTED THE HARD WAY.** The CGNX rule was applied: the four most
recent quarterly earnings 8-Ks and their EX-99.1 releases and EX-99.2 Financial Supplements were
pulled and searched *before* this flag was scored. **`grep -ic ebitda` returns 0 for every
document: both proxies, all four releases, all four supplements, all four 8-K bodies, both annual
meeting 8-Ks.** Chubb does not use the measure anywhere. **Not fired.**

**Headline construction — the candor test [E2-26], and it passes.** The Q2 2026 headline and first
paragraph put **GAAP net income first** and core operating income second: *"Chubb Reports Second
Quarter Per Share Net Income of $7.30 and Per Share Core Operating Income of $7.26"*. All four
releases are built the same way. The non-GAAP measures are defined in a Regulation G section that
runs to several hundred words per measure, reconciled, with the exclusions itemised. **Catastrophe
losses and prior period development are each disclosed as a separate quantified headline bullet
every quarter** ($475M of cats and $283M of favourable PPD in Q2 2026). A one-time item quantified
separately at every line passes [E2-26]; this is that case.

**[E4-22] third flag, and [E3-48]/[E5-30] — TRUMPETED PROJECTIONS. THIS ONE FIRES.** There is no
guidance table and no section headed outlook — searches for *guidance*, *outlook*, *we target*,
*on track to*, *ambition* return nothing structural. **But the CEO's quoted commentary carries a
numeric growth promise in every single release read, and a multi-year ROE target in one:**
> Q3 2025: *"I am confident we will maintain superior earnings growth, including **double-digit
> growth in EPS, book and tangible book value, with core operating ROE increasing to 14% plus over
> the medium term**, CATs and FX notwithstanding."*
> FY2025: *"We anticipate an excellent '26 with strong growth in operating earnings and
> **double-digit growth in EPS and tangible book value**, macro conditions notwithstanding."*
> Q1 2026: *"I remain confident in our ability to continue generating strong growth in operating
> earnings, and **double-digit growth in EPS and tangible book value**."*
> Q2 2026: *"we are confident in our ability to continue to outperform and generate strong growth
> in operating earnings and EPS, and **double-digit growth in tangible book value**."*

**[E5-30] is the reason this matters and it is not this year's fact, it is a ratchet:** *"once you
start it, it's all over. You can't quit … And forecasting earnings, I can't imagine anything more
destructive."* **[E3-48]'s prescribed action was taken: the company's own past commitment was set
against outturn.** The double-digit tangible-book-value promise has been met — TBVPS $131.93 at
6/30/26, **+17.1% year on year**; +15.8% excluding AOCI — and core operating ROE was **14.5%
annualised in Q2 2026** against the *"14% plus over the medium term"* target, i.e. the target is
already achieved rather than aspirational. **A met forecast earns weight [E3-48], and it is
weighed: the flag is FIRED and SCORED SMALL — no metric was invented to hit it, no guidance table
exists, GAAP leads the headline, and the promises have been beaten. But a quarterly repeated
numeric promise is the behaviour [E5-30] calls irreversible, and it is now on the record for this
name.**

**[E2-49] METRIC-SWITCHING — FIRES, SCORED SMALL, AND THE DISCLOSURE IS THE MITIGANT.** *"Yardsticks
seldom are discarded while yielding favorable readings."* Chubb **redefined its own leverage ratio
in the FY2025 10-K**: footnote (3) to the Capital Resources table reads *"Leverage ratios
calculations have been **redefined to exclude** Chubb unrealized gains (losses) on investments, net
of deferred tax, from total capitalization. Prior year has been updated to reflect current
definition for better comparability."* **The switch follows a period in which unrealised losses
were large** ($4,552M at 2024, $1,997M at 2025) and it **improves the ratio**: financial debt ÷
total capitalisation is 18.85% on the old definition and **18.44%** on the new — **0.4 points.**
**Scored as [E2-49] prescribes:** it was **announced with reasons in the filing that first used
it, the prior year was restated for comparability, and the effect is 0.4 points on a ratio the
framework has no threshold for.** That is the candor case, not the disposition-of-the-yardstick
case. **Fired, read, and it changes nothing.**

**[E4-30] FILED-FIGURE FRAUD TELLS — NOT FIRED, and both halves were computed.**
- *Unnaturally smooth reported growth?* **No.** Reported P&C combined ratio over ten years:
  88.3 / 94.7 / 90.6 / 90.6 / 96.1 / 89.1 / 87.6 / 86.5 / 86.6 / 85.7 — a **10.4-point range**.
  Pre-tax income: $5,249 / 4,162 / 9,816 / 6,485 / 9,526 / 11,455 / 13,044M — 2022 is **34% below
  2021**. Net income fell **38% in 2022**. Nothing is smoothed.
- *Cash taxes falling as a share of reported pre-tax income?* Effective tax rate 13.0% (2021),
  19.1% (2022), **5.4% (2023)**, 15.8% (2024), 18.6% (2025). **The 2023 trough is explained in the
  filing** and is not an unexplained drift: it is the recognition of a deferred tax asset on the
  Bermuda Economic Transition Adjustment when Bermuda enacted its 15% corporate income tax. The
  rate has since **risen** two years running, which is the opposite direction from the tell. **The
  amortisation of that Bermuda deferred tax asset is one of the items excluded from core operating
  income** — disclosed, and noted here as a non-GAAP exclusion that flatters the adjusted figure.

**[E5-15] SERIAL SHARE ISSUANCE — NOT FIRED, and the opposite is true.** Shares outstanding
450,732,625 (12/31/20) → 391,101,227 (12/31/25) → **385,799,859 (7/20/26)**: **−14.4% in five and
a half years.** $15,764M repurchased 2021–25 against net issuance under employee plans of a few
hundred million a year. **One item read carefully rather than scored reflexively:** the 2026 AGM
renewed a Swiss **capital band authorising the Board to increase or decrease share capital by up to
20% for one year**. That is a standing authority to issue. The proxy states its purpose — *"enable
us to continue to **cancel** shares earmarked for cancellation that are acquired under our share
repurchase program"* — and the filed record is of cancellation, not issuance ($1,923M of treasury
cancelled in 2025, $2,527M in 2024, $2,869M in 2023). **Authority noted; behaviour is the
reverse.**

**[E2-52] DIVIDENDS FUNDED BY ISSUANCE — NOT FIRED, and this one needed reading rather than
grepping.** Chubb's equity statement shows *"Funding of dividends declared to Retained earnings"*
of **$1,520M taken OUT of Additional paid-in capital**, which fell $14,393M → $13,250M. On its
face that is a dividend paid out of paid-in capital, which is [E2-52]'s shape. **It is not.** It is
the Swiss withholding-tax mechanism: under Swiss law dividends are distributed from *capital
contribution reserves* transferred to free reserves, and the proxy records the statutory auditor
confirming *"that the proposed appropriation of available earnings complies with Swiss law."*
Retained earnings rose $61,561M → $69,950M in the same year on $10,310M of net income against
$1,520M of dividends. **A legal routing, not a return of capital masquerading as a dividend.
Cleared, with the arithmetic shown so the next reader does not have to repeat it.**

**[E2-57] THE EXCEPT-FOR FLAG — READ AND NOT FIRED.** Chubb's non-GAAP suite excludes a great deal
(realised gains, market risk benefits, integration and severance, the Bermuda deferred tax
amortisation, acquired-asset fair value amortisation), which is an "except for" apparatus. But the
GAAP figure leads the headline, the reconciliation is complete, and **the reported combined ratio —
not the current-accident-year one — is what executive pay vests on** (below), which is the harder
test on itself. **[E3-53] restructuring charges:** integration expenses and severance of $79M
(2025), $39M (2024), $69M (2023) — small, recurring, disclosed, and **included** in the pre-tax
operating figures used at Q5 rather than annualised away, per [E5-33].

**[E3-50] STOCK-PRICE TARGETING — NOT FIRED.** Nothing in either proxy or any release states that
management's job is the highest possible price. The one price statement found is the inverse — a
claim of **undervaluation** used to justify buying, addressed below.

**[E2-30] THE INSTITUTIONAL IMPERATIVE — score all four. *"Institutional dynamics, not venality or
stupidity."***
- [ ] **Resists any change in current direction** — no. The record is of exiting and shrinking:
  property and Large Risk premium cut on price in 2025; Combined International's supplemental A&H
  book *"no longer writing new business"*.
- [x] **Projects or acquisitions materialise to soak up available funds — FIRED, and it is the
  real one.** The acquisition record is continuous: **Cigna's Asian A&H and life business (2022)**;
  **Huatai Group to a controlling 76.5% (July 2023), then 85.5% (2024), then 87.2% (2025)**;
  **Healthy Paws (2024)**; **LMG Insurance Thailand, $321M with $183M of goodwill (April 2025)**;
  **Liberty Insurance Vietnam (February 2026)**. Goodwill $15,213M (2021) → **$20,207M (2025)**;
  goodwill plus other intangibles plus VOBA **$29,423M, 40% of Chubb shareholders' equity.** The
  individual deals are small and none is impaired, but the pattern is a company that buys something
  every year. **[E3-40] loss of focus is the vector to watch and it is not yet visible** — every
  acquisition is inside insurance and inside the geographies the base business already licenses;
  nothing has wandered. **Fired as a prompt, monitored at Q6.**
- [ ] Staff studies to justify the leader's craving — nothing found.
- [ ] Peer behaviour mindlessly imitated — the evidence is against it: Chubb shrank property while
  the market chased it.

**[E2-56] THE PRO-AM EFFECT — tested, and the segment detail does not hide a bad leg.** Every
segment earned an underwriting profit in 2025 and in each of 2023–25. The only negative column is
**Corporate, a $781M underwriting loss**, and it is a **run-off book closed since 1994** (A&E and
molestation), not a live business absorbing capital. **Nothing is camouflaged by a strong core
because there is no weak leg to camouflage.** The Life segment's ~zero underwriting result is
disclosed and is by design (it is a spread business).

### THE PRIMARY TEST [E2-01] — AND IT IS A NUMBER
*"The primary test of managerial economic performance is the achievement of a high earnings rate
on equity capital employed (without undue leverage, accounting gimmickry, etc.) and not the
achievement of consistent gains in earnings per share."* **Balance sheet before income statement;
three denominators, because [E2-43] and [E2-73] say the denominator is chosen by the question.**

| | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|---|
| ROE, net income to Chubb ÷ average Chubb equity | 14.70% | 9.64% | 16.41% | 15.01% | 14.97% | **14.14%** |
| ROE on equity **excluding AOCI** | 14.69% | 8.74% | 14.22% | 13.34% | 13.62% | **12.92%** |
| Chubb equity ($M) | 58,328 | 50,519 | 59,507 | 64,021 | 73,757 | |

**[E2-43]'s unleveraged-net-tangible denominator, for an acquisitive filer — and the goodwill wedge
reported separately, never hidden in book equity.** Tangible equity (Chubb equity less goodwill,
other intangibles and VOBA): **$34,842M (2024) → $44,334M (2025)**. **2025 return on tangible
equity: 26.0%.** The wedge is **$29,423M, 40% of book.** So: the operators earn 26% on the capital
they actually work with, and the shareholders earn 14–15% because $29.4bn of the book is what was
paid to acquire other people's businesses. **Both numbers are true and the framework requires both
to be shown.**

**[E2-42]'s red-light test:** *"Red lights should start flashing if the five-year average annual
gain falls much below the return on equity earned over the period by American industry in
aggregate."* 14.14% nominal over five years is above the long-run American-industry average and
below the current S&P 500 aggregate, which is itself inflated by buyback-shrunken equity. **No red
light; no boast either.** The 2022 trough (9.64%) is the LDTI-restated AOCI year, not an operating
failure — on equity excluding AOCI it was 8.74%, and the current-accident-year combined ratio that
year was the third best of the decade at 90.4.

**[E3-59]'s two yardsticks.** *How well do they run the business,* judged against *"the hand they
were dealt"* and against competitors' reports: the competitor row above answers it — third of
seven on the honest basis, ahead of five names including four direct specialty competitors. *How
well do they treat their owners:* the disclosure is unusually full (a ten-year loss triangle by
product line, a reserve sensitivity table with four quantified scenarios, catastrophe PML at three
return periods, PPD split short-tail from long-tail with the adverse lines **named**), $15.8bn
returned in buybacks and $7.1bn in dividends over five years, and the share count down 14.4%.
**And [E3-56]'s caution is honoured: the numbers are not the whole read, and the parts that are not
numbers — the chairman-CEO combination, the 512x pay ratio, the absence of a named successor —
are recorded below rather than netted against the numbers.**

### CANDOR, AND THE [E2-67] BENCHMARK — THE CENTRAL Q3 QUESTION FOR THIS SECTOR
**[E2-50]** puts the Q3 weight on the reserve record; **[E2-67]** sets the standard: Berkshire
published a table of its own reserving errors *"so you can … judge whether we may have some
systemic bias"*, and **named the direction** (*"always presented a better underwriting picture than
was truly the case"*). **The sector method makes this a required Q4 substitution too: read the
triangle, state the direction of the error, and say whether the filer names it.** All three were
done.

**WHAT CHUBB PUBLISHES.** Nine ten-year net incurred-and-paid loss development triangles by product
line (Note 8, section c), with net IBNR and cumulative reported claim counts beside each, plus a
reconciliation to the balance sheet naming what is excluded, plus **a per-line supplementary
"(Favorable)/Adverse Prior Period Development" figure for the year**, plus A&E three-year survival
ratios gross and net, plus a four-scenario reserve sensitivity table. **This is more than the
minimum and it includes the one thing [E2-67] actually asks for: a reader can compute the direction
of the filer's own error line by line.** Here it is, computed:

**PPD BY PRODUCT LINE, 2025, from the nine triangles' own supplementary lines ($M; positive =
ADVERSE):**

| line | tail | 2025 PPD |
|---|---|---|
| NA Commercial — Workers' Compensation | long | **(519) favourable** |
| NA Commercial — Liability (incl. excess/umbrella, D&O, E&O) | long | **+319 ADVERSE** |
| NA Commercial — Other Casualty | long | **+162 ADVERSE** |
| NA Commercial — Non-Casualty | short | (371) favourable |
| NA Personal | short | (397) favourable |
| Overseas General — Casualty | long | (20) favourable |
| Overseas General — Non-Casualty | short | (329) favourable |
| Global Reinsurance — Casualty | long | (3) favourable |
| Global Reinsurance — Non-Casualty | short | (21) favourable |
| **sum of the triangles** | | **(1,179) favourable** |
| Corporate run-off (A&E and molestation), outside the triangles | long | **+306 ADVERSE** |

**THE ARITHMETIC THAT MATTERS, and the filer states it in words before I state it in numbers:**
> *"Pre-tax net favorable PPD for 2025 was $1,439 million in our active companies, including
> favorable development of **$1,329 million in short-tail lines** and favorable development of
> **$110 million in long-tail lines**. … Net favorable development for long-tail lines reflects
> favorable development primarily in **workers' compensation partially offset by adverse
> development in casualty lines**. Our corporate run-off portfolio had **adverse development of
> $306 million**, primarily driven by adverse development for environmental and
> molestation-related claims."*

**From the triangles: long-tail net is (61) favourable — a $519M workers' compensation release
against $481M of adverse North America casualty development. 95% of the favourable development is
SHORT-TAIL.** The 2024 MD&A says the same thing in the same shape: $1,144M short-tail favourable,
**$8M** long-tail favourable, $296M of run-off adverse.

**THE DIRECTION OF THE ERROR, STATED, and it is not one direction — it is two, by tail:**
- **Short-tail lines are systematically over-reserved and released.** Ten consecutive years of
  favourable total development (4.3 / 3.2 / 3.3 / 2.8 / 1.3 / 2.8 / 2.8 / 1.9 / 2.0 / 2.5 points).
  The bias is **conservative**, the opposite direction to the one Berkshire confessed in [E2-67].
- **North America long-tail casualty is systematically UNDER-reserved.** From the Liability
  triangle, first estimate to the 2025 estimate: **AY2016 +5.6%, AY2017 +6.8%, AY2018 +18.7%,
  AY2019 +16.5%, AY2020 −8.2%, AY2021 +3.3%, AY2022 +4.5%, AY2023 +8.8% in two years, AY2024
  +2.2% in one year. Adverse in eight of the last nine accident years.** Net IBNR is 52% of
  incurred on AY2023 and 71% on AY2024, so most of those years is still an estimate.
- **The run-off book is under-reserved and has been topped up every year:** +$306M (2025), +$296M
  (2024), and the FY2018 10-K records $216M (2018) and $239M (2017). A&E is 1.4% of gross reserves.

**DOES THE FILER NAME IT? YES, in words, every year, with the lines named** — *"adverse development
in casualty lines, predominantly commercial excess and umbrella and commercial auto liability"* —
**and it publishes the triangles that let a reader measure it. [E2-67] is SATISFIED.**

**Three things read the other way and all three are recorded.**
1. **The filer discourages the very analysis the disclosure enables.** Note 8: *"We believe the
   information provided in the 'Loss Development Tables' section of the disclosure is **of limited
   use for independent analysis** or application of standard actuarial estimations."* And on A&E:
   *"we urge caution in using these very simplistic ratios to gauge reserve adequacy."* Both
   cautions are technically fair. **Both also tell the reader not to do what [E2-67] exists to let
   him do, and that is worth noting in a filer whose pay vests on the ratio the reserves feed.**
2. **Chubb does not publish a single consolidated table of its own reserving error over time** the
   way [E2-67]'s benchmark does. The nine triangles and the per-line supplementary figures let a
   reader build one; the filer does not hand it over. **The difference between "the data is there"
   and "we published the scorecard and named our bias" is the difference between compliance and
   [E2-67], and Chubb is on the compliance side of it.**
3. **The actuarial function reports to the CFO** (*"Corporate units under his management include
   accounting and financial reporting, investment management, treasury, **actuarial** and tax"*),
   i.e. to the officer responsible for the reported number. **Mitigants, filed:** the Audit
   Committee's charter names *"the process for establishing insurance reserves"*; the Chief Actuary
   attends all four quarterly meetings; and **in January 2026 the Audit Committee met the Chief
   Actuary to review "the external independent actuaries' review and their annual independent
   assessment of the Company's loss reserves"**, with a further external-actuary presentation to a
   joint Audit/Risk & Finance session in February 2025. **An annual independent actuarial
   assessment reported to an all-independent Audit Committee is a real control and it is scored as
   one.**

**[E2-72] AUTHORSHIP — the one candor item Chubb does not clear.** *"owners are entitled to hear
directly from the CEO … A once-a-year report of stewardship should not be turned over to a staff
specialist or public relations consultant."* **Chubb publishes no shareholder letter in its 10-K.**
The CEO's voice reaches owners in three paragraphs of quoted commentary per quarterly press
release. **Recorded as a gap against the benchmark, not as a disqualifier** — it is the ordinary
practice of every name in the competitor row.

**[E4-34] the auditor's-eye test, fourth question — period-shifting.** *"any action with the
purpose and effect of moving revenues or expenses from one reporting period to another."* **This is
what a reserve IS**, which is why this sector gets the [E2-50] weight. The answer from the evidence
above: **short-tail reserves have moved expense from earlier years into later income at 2–4 points
a year for a decade, and it is fully disclosed and quantified in both directions.** Disclosed
period-shifting quantified at every line is the [E2-26] pass; undisclosed period-shifting is the
failure. This is the former.

### RATIONALITY IS CAPITAL ALLOCATION [E2-29, E3-58]
Greenberg has been CEO 22 years. **[E3-58]** makes the stakes tenure-weighted: a CEO that long into
a 14% ROE business paying out 15% has allocated nearly all the capital the company has ever had.
Three tests.

**[E3-54] THE SCORED TEST — $1 of market value per $1 retained, five-year rolling, run on the
CURRENT five years, not the legend:**
- Market capitalisation **12/31/20: $69,377M** (450,732,625 shares at $153.92) → **12/31/25:
  $122,071M** (391,101,227 at $312.12). **Increase $52,694M.**
- Net income to Chubb 2021–25 **$42,381M** less dividends declared **$7,147M** = **retained
  $35,234M**.
- **$1.50 of market value per $1 retained.** Treating the $15,764M of buybacks as a distribution
  too: **$2.71 per $1**. **PASSES on either construction.**
- Underneath it: **book value per share $127.99 → $188.59, +47.3% (8.06%/yr)**; book value per
  share **excluding AOCI $125.63 → $201.31, +60.2% (9.89%/yr)**; **price +102.8% (15.19%/yr)**.
- **AND THE DECOMPOSITION, because [E3-54] passing is not the same as value having been created.**
  The multiple went from **1.20x book at 12/31/20 to 1.66x at 12/31/25** (1.78x today). **Of the
  15.19%/yr price return, roughly 8.1 points is book value per share and roughly 6.6 points is
  multiple expansion.** The retention test passes partly because the market re-rated the shares.
  **[E4-44]** binds: *"the value of an asset, whatever its character, cannot over the long term
  grow faster than its earnings do."* That is a Q5 fact and it is carried there rather than
  credited here.

**[E5-08] THE TWO BUYBACK CONDITIONS, PLUS [E4-31]'s THIRD:**
- **(1) ample funds for operations and liquidity — MET.** $2.5bn of cash, $4.8bn of short-term
  investments, $12.8bn of operating cash flow, $4.3bn of committed facilities, an A.M. Best and
  S&P rated balance sheet with financial debt at 18.4% of adjusted capitalisation, and the filer's
  own statement that sources *"will be sufficient to meet our anticipated cash requirements for at
  least the next twelve months."*
- **(3) [E4-31] — the register is INFORMED. MET, and unusually well.** Nine loss triangles, a
  four-scenario reserve sensitivity table, PML at three return periods, the full non-GAAP
  reconciliation, quarterly Financial Supplements. A buyback made against an under-informed
  register fails even at a discount; this register is not under-informed.
- **(2) a MATERIAL DISCOUNT to conservatively calculated intrinsic value — THIS ONE FAILS ON MY
  OWN ARITHMETIC, AND THE FLAG IS LIVE.** $15,764M was repurchased 2021–25, at average prices of
  **$209.52 (2023) = 1.43x** that year-end book value per share, **$269.23 (2024) = 1.69x**,
  **$282.57 (2025) = 1.50x**, and **$326.03 for the first half of 2026** — against tangible book
  value per share of $131.93 at 6/30/26, i.e. **2.5x tangible book.** Against the Q5 range derived
  below (roughly **$250 to $310** a share on the honest pre-tax expectancy), the 2024, 2025 and
  2026 repurchases were made **above** the conservative end and, for 2026, above the whole range.
- **Management's own stated ground, quoted so the disagreement is explicit** (Q3 2025 release, the
  only price statement in any document read): *"In the quarter, we increased share buybacks **since
  our stock is trading well below intrinsic value**. Given our earning power, increased buyback
  activity will continue."*
- **THE HUMILITY CLAUSE, and it is not decoration [E4-13, E5-08].** *"it is natural for CEOs to be
  optimistic about their own businesses. **They also know a whole lot more about them than I do**"*
  and *"infractions, even serious ones, are innocent; many CEOs never stop believing their stock is
  cheap."* **This flag rests on MY range, and my range is built on a ~10% pre-tax floor that is
  itself a judgment Buffett calls arbitrary.** On a sum-of-the-two-components basis (Q5 below) the
  shares are cheap and management is right. **The flag is recorded as what it is — a disagreement
  about the discount rate applied to a levered portfolio, not a finding of irrationality — and per
  [E5-08] it BINDS POSITION SIZE, never the discount rate.** Since no position is proposed, its
  operative effect is the pre-committed line at Q6: **if this name ever clears, it is SIZED DOWN.**
- **[E5-25] is the contrast that shows what full compliance looks like and Chubb does not meet
  it:** Berkshire published **both conditions as numbers in advance** — the 110%-of-book limit and
  the $20bn liquidity floor. **Chubb publishes no repurchase condition of any kind.** Neither proxy
  states a policy; the authorisation is a dollar amount and a date ($5.0bn from 2025-07-01, $2.1bn
  remaining at 2026-02-26). **[E2-51]** cuts the other way and is noted for balance: a manager who
  *refuses* repurchases when they are clearly in owners' interests *"reveals more than he knows of
  his motivations"* — Chubb is not that manager.

**[E4-39] THE RARE-POSITIVE TELL — NOT PRESENT.** No candid acquisition post-mortem was found in
either proxy or any 10-K read. Cigna Asia, Huatai and Healthy Paws are described at acquisition and
never revisited against the announcement case. *"Almost never witnessed"* is the base rate, so its
absence is not a mark against; it is simply weight not earned.

**[E4-27] THE POWER OF INCENTIVES — *"Never, ever, think about something else when you should be
thinking about the power of incentives."* THIS IS THE SHARPEST FINDING IN Q3 AND IT WAS NOT IN THE
BRIEF.**
**100% of the CEO's annual equity award is performance-based, and the performance metrics are:**
> *"our performance criteria tie the three-year cliff vesting of these awards to specified
> relative performance targets, namely our **tangible book value per share growth (70% weighting)
> and P&C combined ratio (30% weighting)**."*

**Both metrics are improved by favourable prior-period reserve development, and the combined-ratio
metric is the REPORTED ratio, not the current-accident-year one.** The proxy's PSU/PSA criteria
language contains **no catastrophe exclusion and no prior-period-development exclusion**; the
catastrophe adjustment appears only as a discretionary lens in the annual cash bonus. So: **30% of
a $21.4M long-term award turns on a ratio that 2.5 points of reserve release improved in 2025, and
70% turns on tangible book value per share, which reserve releases also build.** In a business
where *"earnings can be created by the stroke of a pen"* **[E2-50]**, that is the incentive pointed
at the pen.

**Now the counterweights, because [E4-26] requires hunting hardest against the favourite
hypothesis, and here the favourite hypothesis is the flag:**
1. **Both metrics are measured RELATIVE to a Financial Performance Peer Group over three years.**
   Releasing reserves helps only to the extent peers do not — and the row above shows peers release
   more: **RLI 6.1–10.8 points a year, ACGL 3.4–8.0, KNSL 2.7–5.5, MKL 5.6–5.8, against Chubb's
   1.9–2.8.** **Chubb is the second-least reserve-release-dependent name in a seven-name row, on a
   metric that pays it to be the most.** That is the incentive pointing one way and the behaviour
   going the other, and it is the strongest single piece of evidence for this management's
   reserving integrity.
2. **The vesting calculation is verified by an independent accounting firm** — *"We have retained
   Ernst & Young Ltd. (EY) … to verify the calculations of our performance criteria."*
3. **Reserve releases are a zero-sum trade against the accident year they came from**, and the
   accident-year series above shows the current year was profitable anyway.
4. **The Committee cannot increase vesting above actual performance** — *"The Compensation
   Committee lacks discretion to increase the vesting of any performance-based equity award other
   than what was achieved."*
5. **The buyback behaviour argues against metric-gaming in the other direction:** repurchases at
   2.5x tangible book **REDUCE** tangible book value per share, which is 70% of the vesting metric.
   Chubb bought $3.4bn in 2025 and $2.1bn in H1 2026 anyway. **A management optimising the metric
   would not do that.**

**[E4-52] THE CONVERGENCE TEST — the reason the flags are read together and not summed.** *"extreme
consequences from **confluences** of psychological tendencies acting in favor of a particular
outcome."* Three flags fired: quarterly numeric growth promises, a leverage-metric redefinition
that improves the ratio, and pay vesting on two reserve-sensitive metrics. **Do they converge on one
outcome?** They would if they were accompanied by declining reserve conservatism, smoothed reported
results and releases running ahead of peers. **The filed record is the reverse on all three: the
reported series is the least smooth in the row (a 10.4-point range), the current-accident-year
ratio is under 100 in ten of ten years, and the releases are the second-smallest in the row. There
is no lollapalooza here. Three prompts, read, and they do not reinforce.**

**And [E5-38]'s boundary is honoured:** a fired flag is not a venality finding. People Buffett
would trust with his wallet *"would play games with any number that came to them."* The flags read
the accounting; [E5-16] judges the person on conduct; the two tests stay separate.

### PAY, THE PAY RATIO, AND THE GOVERNANCE STRUCTURE — recorded, not scored as a disqualifier
- **CEO total compensation $33,180,582 (2025), $30,138,094 (2024), $27,661,317 (2023)**; the
  Committee's own "total direct compensation" for 2025 performance **$34.0M, up 13.5%**, base
  salary frozen. Say-on-pay 2026: **299.8M for / 13.1M against (95.8% for).**
- **CEO pay ratio 512x (2025), 477x (2024).** The median employee was identified as of **December
  31, 2023** and has been carried forward through three proxies.
- **The Swiss binding maximum aggregate compensation for Executive Management (four people) rises
  from $78M for 2026 to $98M for 2027, +25.6%**, approved 305.7M to 6.8M. The proxy explains the
  *"cushion"* rather than the level.
- **Chairman and CEO are the same person.** The mitigants are filed and real (an independent Lead
  Director, Michael P. Connors, with power to convene meetings and set the agenda; all other
  directors independent; all four principal committees fully independent; executive sessions at
  every regular meeting). **The dissent is also filed: 17.7% against his election as Chairman in
  2026 and 22.6% in 2025, the largest against-vote at either meeting.** And compensation committee
  member David H. Sidwell drew 16.5% against.
- **[E3-66] jurisdiction — where do shareholders stand in the queue?** Swiss incorporation is on
  balance shareholder-favourable and more so than the US on two axes: **shareholders vote annually
  and in a binding vote on the maximum executive compensation**, and **annually on the dividend
  itself** (up to $3.88 per share approved for the year to the 2026 AGM). The costs are procedural:
  dividends must be stated in Swiss francs, distributions run through capital contribution
  reserves, a capital band must be renewed annually to permit share cancellation, and the
  statutory auditor is a second Swiss audit appointment. **No constituency stands ahead of
  shareholders in the way [E3-66] warns about.**

### THE GUARDRAIL — check before writing the verdict
- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** The Q2 verdict was
  reached on the current-accident-year series and the competitor row before any of this was read,
  and the Q5 verdict below is negative. **[E2-37, E2-38, E3-39]** stand: *"a good managerial record
  … is far more a function of what business boat you get into than it is of how effectively you
  row."*
- [x] **Key-person dependence is recorded at Q2 as a moat defect [E4-23]**, not here as a strength.
  Greenberg's 22-year record is the reason the Q2 class is NARROW.
- [x] **Not a turnaround.** No excisable cancer, no corporate Pygmalion, no manager-is-the-plan
  case. **[E2-66]** is the closer analogue: an operation run better than one's own, bought
  passively — *"the proper policy also would be to sit back and let management do its job."* The
  question here is price, not stewardship.

- **VERDICT: [x] IN — as a BINARY GATE, and IN means only the absence of found disqualifiers
  [E5-17], never a finding that the managers are honest. IN never promotes.**
  **Three flags fired and are carried: the quarterly numeric growth promise [E4-22, E3-48, E5-30];
  the 2025 leverage-metric redefinition [E2-49], scored at 0.4 points and disclosed; and the
  acquisition-every-year pattern [E2-30](2).** **One CAPITAL-ALLOCATION FLAG is LIVE: repurchases
  in 2024, 2025 and H1 2026 above the conservative end of this run's own value range [E5-08](2),
  with no published repurchase condition to test them against [E5-25]. It binds position size and
  nothing else [E4-13].** Against all of that, the reserving behaviour is the second most
  conservative in a seven-name row measured on filed figures, which is the test that matters most
  in this sector **[E2-50]**.

## Q4 — WILL IT SURVIVE?

### THE SECTOR METHOD'S SUBSTITUTIONS APPLY, NOT THE ORDINARY OWNER-EARNINGS CONSTRUCTION
**No owner-earnings number is computed for this filer, and the reason is the method's own:** *"the
answer is not a better owner-earnings formula. The corpus does not compute one."* Float is not
operating cash flow; (c) has no referent for a securities portfolio; and the cash test inverts
**[E2-61]**.

**THE LOEWS TEST, RUN EXPLICITLY, BECAUSE THE BRIEF ASKED FOR IT AND BECAUSE THIS IS THE ERROR THE
METHOD EXISTS TO PREVENT.** The L run of 2026-09-02 watched an 11.5% screen yield collapse to 1.8%
once reserve growth was stripped. Here is the same test on Chubb:
- Operating cash flow FY2025 **$12,816M**, less share-based compensation **$400M** = **$12,416M**,
  which is **9.45% of the $131,419M market capitalisation**. A run that reported that number
  **and** also noted the $168.7bn portfolio would have counted the portfolio twice — *"there is no
  windage that fixes that; it is an arithmetic error."*
- Strip the **$3,402M of net reserve growth** (net unpaid losses $66,270M → $69,672M) and the
  **$2,775M of unearned premium growth** ($23,504M → $26,279M): **$6,239M, 4.75% of the cap. A 50%
  collapse.** The Loews shape is present in Chubb's cash flow statement too. It is milder only
  because Chubb's underwriting is genuinely profitable, and the way to see that is not the cash
  flow statement at all.
- **Neither figure is used below.** This paragraph exists so the next reader can see that the guard
  was applied rather than assumed.

### STEP 2 — THE COST OF FLOAT [E3-69]. DIAGNOSTIC, NOT ADDITIVE.
*"a comparison of underwriting loss to float developed … when the ratio takes in a period of years,
it gives a rough indication of the cost of funds generated by insurance operations. **A low cost of
funds signifies a good business; a high cost translates into a poor business.**"*

| | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr |
|---|---|---|---|---|---|---|
| P&C underwriting income $M | +3,696 | +4,555 | +5,460 | +5,850 | +6,528 | **+26,089** |
| average float $M | 55,916 | 58,240 | 60,163 | 63,318 | 66,477 | **60,823** |
| **cost of float** | **−6.61%** | **−7.82%** | **−9.08%** | **−9.24%** | **−9.82%** | **−8.58%** |

**CONVENTION 2: the window is five years and is stated.** **[E3-69]** forbids a one-year figure and
**[E5-49]** forbids a flattering one; the five-year mean is reported and the year detail is shown so
the trend is visible rather than buried. Extending to 2019 and 2020 on the same construction gives
roughly −5.3% and −2.2% — **negative in every one of seven years, including the worst catastrophe
year of the decade.**

**THE DIAGNOSTIC'S JUDGMENT, STATED.** Chubb is **paid about 8.6% a year to hold $60.8bn of other
people's money**, while the 30-year Treasury pays 5.34%. Against borrowing the same sum at its own
cost of debt (interest expense $764M on $17.6bn of debt = 4.3%), the float advantage is worth
roughly **$7.8bn a year pre-tax**. **Berkshire, on the identical five years and from this project's
own BRK run: −3.6% on ~$162bn.** On the corpus's own chosen measure of insurer profitability,
**Chubb's funding is better than Berkshire's, per dollar.** What Chubb does not have is Berkshire's
loss-absorption per dollar of float (float ÷ equity 0.92x against 0.24x), and **[E2-62]** is
explicit that the method transfers and the licence to concentrate does not.
**NOTHING HERE IS ADDED TO ANYTHING.** Underwriting income enters the valuation once, in component
2. That is the MKL amendment's ruling and it is obeyed.

### Q4 SUBSTITUTION 1 — LIQUIDITY READ AS RESERVE ADEQUACY AND NET WORTH, NEVER CASH ON HAND [E2-61]
*"you can be broke but flush … insolvent insurers don't run out of cash until long after they have
run out of net worth. In fact, these 'walking dead' often **redouble their efforts to write
business**, accepting almost any price or risk, simply to keep the cash flowing in."*
**The walking-dead test is the growth-versus-price test, and Chubb fails it in the right
direction:** it **cut** property premium on price in 2025 (Major Accounts +1.4%, *"rate decreases
in our Large Risk and E&S brokerage property lines"*) and says *"we will not underwrite knowingly
at a loss."* A company redoubling to keep cash coming in does not shrink its largest short-tail
line into a soft market. **Net worth: $73,757M of Chubb equity, $79,779M including minorities, up
from $50,519M in 2022.** Reserve adequacy is scored in substitution 2.

### Q4 SUBSTITUTION 2 — RESERVE DEVELOPMENT IS THE CANDOR TEST [E2-67]
Done at Q3 in full. The result, restated as a survival fact: **the reserving error is
conservative in short-tail lines and adverse in North America long-tail casualty, the two roughly
offset inside a $1.1–1.4bn annual net release, and the run-off book is topped up $300M a year.**

### Q4 SUBSTITUTION 3 — CONCENTRATION IS LICENSED BY LOSS-ABSORPTION [E2-62], AND THE LICENCE DOES
NOT TRANSFER
*"This concentration makes sense only because our insurance business is conducted from a position
of exceptional financial strength. For almost all other insurers, a comparable degree of
concentration … would be totally inappropriate."* **The sector method calls this "an explicit
warning against reading the eight smaller names as small Berkshires," and it is applied here
rather than quoted.** Chubb's equity is **$73.8bn against Berkshire's $747.9bn — one-tenth**, a
figure this project's own BRK run computed from the other side. **Chubb does not concentrate:** the
portfolio is $122.7bn of AFS fixed maturities against $10.8bn of public equities — **6.4% of
investments in listed equities**, against Berkshire's roughly half. **The licence is not claimed
and it is not needed, because the behaviour it would license is not present.**

### THE GREAT, THE GOOD AND THE GRUESOME [E4-20, E4-43]
- [ ] great — [x] **good** — [ ] gruesome.
- **Evidence.** *"The good one pays an attractive rate of interest that will be earned also on
  deposits that are added."* Chubb earns **14.1% on equity and 26.0% on tangible equity**, and it
  earns it on added capital: equity grew from $50.5bn (2022) to $73.8bn (2025) while ROE stayed in
  a 13–16% band. It is not **great**, because the return is not rising and the business does need
  capital roughly in proportion to premium; it is not remotely **gruesome**, because the cash it
  consumes earns 14% and the cash it holds is other people's at a negative cost.
- **[E4-43] governs and is applied:** the good class **passes** Q4 — *"nothing shabby about earning
  $82 million pre-tax on $400 million of net tangible assets."* **[E5-40]**'s ~12%-on-retention
  number is met and exceeded. **Good ranks below great at Q5, and that is all.**

### STAYING POWER — SCORE ALL THREE [E5-11], SECTOR-SCOPED
1. **A large and reliable stream of earnings — [x] YES.** Pre-tax operating income $5,779 / 4,660 /
   6,558 / 7,740 / 9,936 / 10,817 / 12,000M across 2019–2025: **positive in all seven years,
   trough $4,660M in the COVID year.** [E5-29] is honoured: *"Volatility is far from synonymous
   with risk."* The stream is volatile in level and certain in sign.
2. **Massive liquid assets — [x] YES, and re-expressed per [E2-61] so it does not return a false
   pass.** Not cash on hand ($2,470M, trivially small against $88.0bn of gross reserves). The right
   reading: **$122,680M of available-for-sale fixed maturities marked to market**, a fixed-income
   portfolio the filing describes as *"relatively short duration"*, against $24.8bn of gross loss
   payments estimated due in twelve months. **Net worth $73.8bn against a modelled 1-in-250
   worldwide natural-catastrophe aggregate of $9.3bn — 12.6% of equity.**
3. **NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — [x] YES, with two items named.** The filer's own
   twelve-month schedule: **$24.8bn of gross loss payments** (funded by $54.8bn of premium),
   **$2.6bn of policy benefits**, **$1.5bn of debt maturities plus $0.6bn of interest**, **$3.7bn
   of invested-asset commitments**, **$1.0bn of deposit liabilities**, **$0.2bn of leases** —
   against $12.8bn of operating cash flow and a $168.7bn portfolio. **The two [E5-39] items, named
   rather than netted:** *"cash is a lot like oxygen … if it's absent, it's the only thing you
   notice."* (i) **$3.3bn of repurchase agreements, all maturing within five months**, described by
   the filer as *"a low-cost funding alternative"* — rollable in normal markets, and exactly what
   is not rollable in the market where the portfolio is also down. (ii) **A bank notional
   cash-pooling programme under which "Chubb entities may incur overdraft balances as a means to
   address short-term liquidity needs," guaranteed by Chubb Limited up to $1,500M**, with the
   $3.0bn syndicated facility available for same-day drawing to fund a pool overdraft — and that
   facility *"require[s] that we maintain certain financial covenants."* **$4.8bn of
   kindness-of-strangers funding inside a $272bn balance sheet: small, real, and named.**
- **LEVERAGE, NAMED AND QUANTIFIED — there is no ratio ceiling in this framework and the corpus
  supplies none [E4-16, E3-29].** Financial debt **$17,227M** plus hybrid **$422M** plus repos
  **$3,324M** = **$20,973M against $73,757M of equity, 28.4%**; on the filer's own measure,
  financial debt is **18.4% of total adjusted capitalisation**. **[E2-54]'s coverage test, run
  properly — all interest, payable and accrued, comfortably met out of current cash flow net of
  ample capital expenditures:** interest $764M against pre-tax operating income of $12,000M
  (16.7x) and operating cash flow of $12,816M (16.8x). **[E3-52] is the point that matters and it
  is the whole thesis of this sector:** float and deferred taxes are *"liabilities **without
  covenants or due dates** attached to them … the benefit of debt … but saddle us with none of its
  drawbacks."* **$68.0bn of Chubb's $199bn of liabilities is exactly that animal — customer-prepaid,
  covenant-free, no due date — and $21.0bn is the other animal, covenanted and dated.** Reading
  them as one number is how this sector gets misjudged in both directions.
- **[E2-55]'s design principle applied: score the worst case, not the expected one.** A 1-in-250
  worldwide natural-catastrophe year ($9,285M) **plus** the sum of the filer's own four
  "reasonably likely" adverse reserve deviations ($2,764M) **plus** the loss of the 2.5 points of
  favourable development, in one year, is roughly **$13.2bn pre-tax — about one year's pre-tax
  operating income and 18% of equity.** Chubb would report a loss and remain solvent, well
  capitalised and able to write. **That is *"acceptable long-term results under extraordinarily
  adverse conditions."***

### NAME THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40, E4-51]
**The bar is [E4-51]: state the arguments against the position better than the people in
opposition. Two mechanisms, both quantified from filed figures, and the second is the real one.**

**MECHANISM 1 — the catastrophe, and it is NOT how this business dies.** Filed modelled net
pre-tax PML at 2025-12-31: **1-in-10 $3,003M (4.1% of equity) · 1-in-100 $5,862M (7.9%) · 1-in-250
$9,285M (12.6%)** worldwide annual aggregate; US hurricane 1-in-250 $6,552M; California earthquake
single-occurrence 1-in-250 $2,176M; a 10-ton truck bomb at the largest US exposure location $2.3bn
net of reinsurance and TRIPRA. **A 1-in-250 natural-catastrophe year costs about one year's pre-tax
operating income. It cannot kill this company. Likelihood: a real possibility; consequence:
survivable.**
**And the [E4-40] discipline applied against the filer's own model, because the numbers invite
it:** realised catastrophe losses 2019–25 were **$1,175 / 3,249 / 2,411 / 2,231 / 1,828 / 2,401 /
2,863M, mean $2,308M** — on a book whose premium was **58% smaller at the start of the window.**
Scaled to today's book the realised mean is near **$3.3bn, i.e. AT or slightly ABOVE the modelled
1-in-10 aggregate of $3,003M.** An annual aggregate whose realised mean sits at its own modelled
90th percentile is either an optimistic model or an unusually bad seven years. **The comparison's
limit is stated rather than hidden: the PML excludes non-modelled perils (man-made, pandemic) and
covers only named natural perils, while the reported catastrophe figure is PCS-defined and
includes events the model does not carry. The two are not the same population.** Recorded as a
prompt to read the next PML table against the next realised year, not as a finding.

**MECHANISM 2 — THE REAL ONE: THE RESERVE CUSHION RUNS OUT AT THE SAME MOMENT THE PRICE CYCLE
TURNS. Two things that have been helping stop helping together.** Quantified from the triangles:
- **The release engine is a depleting, non-renewable asset concentrated in identifiable accident
  years.** Workers' compensation net incurred, first estimate to 2025: **AY2016 −19.8%, AY2017
  −26.0%, AY2018 −15.2%, AY2019 −11.0%, AY2020 −15.2% — and then AY2021 +0.1%, AY2022 +6.5%,
  AY2023 +3.8%, AY2024 −0.9%.** **The redundancy is entirely in 2016–2020 and there is none in
  2021–2024.** Net workers' compensation reserves are $10,015M, of which $3,023M is pre-2016.
- **The offsetting drain is live and growing.** North America Commercial Liability developed
  **adversely in eight of the last nine accident years** (AY2018 +18.7%, AY2019 +16.5%, AY2023
  +8.8% in two years) and cost **$319M in 2025**; Other Casualty cost a further **$162M**. Net
  reserves on those two lines are **$26,500M** with net IBNR of $2,645M on AY2023 alone and
  $3,749M on AY2024 — 52% and 71% of incurred, so most of it is still an estimate.
- **The 2025 long-tail net was $110M favourable — a $519M workers' compensation release against
  $481M of casualty strengthening. It is within $110M of flipping.** In 2024 it was $8M.
- **The filer's own four "reasonably likely" deviations, each its word not mine:** workers'
  compensation 1-point tail factor **±$1,100M** on $10,015M (11.0%); US excess/umbrella 5-point
  tail factor **±$900M** on $4,900M (18.4%); Overseas General long-tail six-month lengthening
  **+$540M** on $5,600M (9.6%); Global Reinsurance 20% pattern change **±$224M** on $1,040M
  (21.5%). **Sum $2,764M — 3.7% of equity and 23% of 2025 pre-tax operating income.**
- **AND THE SECOND HALF, from the same filings: the price cycle is turning NOW, by management's own
  account.** *"rate decreases in our Large Risk and E&S brokerage property lines"* (FY2025 10-K);
  *"soft market conditions are spreading to certain areas of casualty while financial lines also
  remain soft"* (Q2 2026). **[E2-58]:** *"persistent over-capacity without administered prices (or
  costs) equals poor profitability"*, and *"nothing fails like success."*

**THE MECHANISM, QUANTIFIED, WITH ITS OUTCOME.** Long-tail development flips from +$110M favourable
to **$2,000M adverse** (below the filer's own combined "reasonably likely" range) and the 2.5 points
of favourable development is lost, while the current-accident-year ratio drifts back toward its
ten-year mean of 92.3 as rate falls:
- **P&C combined ratio 85.7 → about 92.6.** Underwriting income **$6,528M → about $3,403M**.
- **Pre-tax operating income $12,000M → about $8,875M**, a 26% cut.
- **Pre-tax yield on today's price 9.13% → 6.75%.**
- Chubb reports a profit in every year of that scenario, pays every claim, and keeps writing.
- **LIKELIHOOD: [x] a real possibility** — the filer itself calls each component *"a reasonably
  likely deviation"*, and the pricing half is already happening in its own words.

**THIS IS A RETURN EVENT, NOT A SURVIVAL EVENT, AND IT BELONGS AT Q5.** What would make it a
survival event is a combination the filed figures do not support: a 1-in-250 catastrophe year, a
$2.8bn reserve charge and a 20% portfolio drawdown together would cost roughly **$25bn — 34% of
equity — and Chubb would still be writing.**

**SURVIVAL SHAPE, against `Screens/SURVIVAL SHAPES - index.md`:** **#7 THE LONG TAIL ON A SHORT
CYCLE** (first named by CNR, 2026-09-13 — *decades-long claims fixed in dollars against a
years-long price cycle, the balance sheet the only buffer*) is the closest existing shape and is
named as the mechanism, **with #11 THE PASS-THROUGH as a feature** (the 2019–23 hard-market gains
are being handed back to buyers as capacity returns: property rate down in 2025, casualty and
financial lines softening in 2026, on management's own statement). **A refinement is PROPOSED, not
asserted: #23 THE CUSHION** — *the reported profit is real on the year's own business, but the
reported line is smoothed by releasing reserves set in a closed and identifiable set of older
accident years; that redundancy is non-renewable and is already exhausted in the newer years, while
the same book's long-tail casualty develops adversely — so the reported ratio converges upward to
the current-accident-year ratio at the same moment the price cycle turns against the current
accident year, and the owner's reported return steps down with no deterioration in the business
itself.* **The argument for separating it from #7:** #7 is about a long-tail liability that can
outrun the pricing cycle and kill the company (CNR's asbestos-type case, where the balance sheet is
the only buffer). **#23 is not lethal at all** — it is about a depleting *accounting* cushion whose
exhaustion changes the reported number without changing the business, and it is the class mechanism
for every well-reserved insurer, which is why it is worth a number. **Proposed for the operator, as
#13 through #22 were; nothing is asserted as settled.**

- **VERDICT: [x] IN.** Survival is not in question. Return is, and that is Q5's question.

---
⛔ **Q5 opens legitimately: Q1, Q2, Q3 and Q4 each returned IN.** This is the **second insurer** and
the **third name** in this queue's history to open Q5 (ORLY, BRK-B, and now CB), and the second
under the sector method.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Why this is arithmetic at all [E4-42]:** *"What's needed is an antidote, and in my opinion that's
quantification. If you quantify, you won't necessarily rise to brilliance, but neither will you sink
into craziness."*

### STEP 1 — COMPONENT 1: THE INVESTMENTS, AT MARKET [E5-46]. GROSS VERSUS NET, STATED, WITH THE
### ARGUMENT AND NOT JUST THE CHOICE — the MKL amendment's requirement
**CONVENTION 1: "at market" is the balance-sheet fair value the filer reports**, with **[E5-32]**'s
limit disclosed — the filed statement is not bedrock. All figures 2025-12-31 ($M):

| construction | $M | per share |
|---|---|---|
| **GROSS: total investments 168,720 + cash 2,470** | **171,190** | **$444** |
| less noncontrolling interests 6,022 (VIE and Huatai minorities) | 165,168 | $428 |
| less debt 17,227 + hybrid 422 + repurchase agreements 3,324 | 144,195 | $374 |
| **less life and annuity liabilities that are NOT float**: future policy benefits 18,420 + policyholders' account balances 8,576 + market risk benefits 659 | **116,540** | **$302** |
| *(further less float 68,007 — shown only to locate the answer, NOT used)* | *48,533* | *$126* |

**WHICH IS USED, AND WHY — the $116,540M line ($302 a share).** Three deductions are made from the
gross figure and each has a reason:
1. **Noncontrolling interests** are not the buyer's. Berkshire's own run treated $2.3bn as de
   minimis and did not net it; Chubb's $6.0bn is 3.6% of investments and is netted.
2. **Debt, hybrids and repurchase agreements are covenanted and dated [E3-52].** They are not
   float. Component 2 charges their interest; the principal is a claim and is deducted.
3. **The life and annuity liabilities are not float either.** They carry credited interest and
   mortality risk, and Chubb Life's entire segment income is investment income (its underwriting
   result was −$12M). Deducting the liability and removing its investment income from component 2
   prices the leg at its spread, which is what it is. **This deduction is not in the sector method
   and is CONFESSED AS THIS RUN'S OWN JUDGMENT — see the defects section.**
4. **Float is NOT deducted, and that is the method [E5-46]:** *"all of our investments … those
   funded **both by float and by retained earnings** … can be viewed as an element of value"* — on
   the express condition *"as long as insurance underwriting breaks even."* **Chubb meets that
   condition in the strongest form the panel has produced: underwriting profitable on the CURRENT
   ACCIDENT YEAR INCLUDING CATASTROPHES in ten of ten years, worst year 97.9.** Berkshire's own run
   licensed gross on three years of the same test; Chubb has ten.

**[E3-71] — THE DEFERRED TAX, VALUED AS THE ADVANTAGE OF AN INTEREST-FREE LOAN, NEVER AT FACE AND
NEVER AT ZERO.** Munger valued Wesco's at about $25 a share. **At Chubb it is almost nothing, and
the reason is instructive:** the net position is a deferred tax **liability** of $429M ($1,741M
liability less $1,312M asset), and **the AFS portfolio carries an unrealised LOSS, not a gain** —
amortised cost $124,726M against fair value $122,680M, a **$2,046M deficit**. There is no embedded
appreciation to defer. **Charge: nil, and it is a disclosed judgment, not an omission.** *(The
Bermuda Economic Transition Adjustment deferred tax asset is the one sizeable item of this kind and
it runs the other way — an asset whose amortisation Chubb excludes from core operating income.)*

### STEP 2 — THE COST OF FLOAT: **−8.58% over five years. DIAGNOSTIC. NOTHING IS ADDED.** (Q4 above.)

### STEP 3 — COMPONENT 2: PRE-TAX EARNINGS OF EVERYTHING ELSE, INCLUDING UNDERWRITING INCOME, WITH
### DIVIDENDS AND INTEREST FROM STEP 1 REMOVED [E5-48]
*"We exclude in the second factor the dividends and interest from the investments we hold because
including them would produce a **double-counting of value**. … Income taxes, though, are not
deducted. That is, the earnings are pre-tax."*

Construction: income before income tax, less net investment income, less net realised gains, less
market-risk-benefit gains, less all of Other (income) expense (which is where the private-equity
marks and the equity in partially-owned entities sit):

| $M | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean | 3-yr mean |
|---|---|---|---|---|---|---|---|
| **component 2, pre-tax** | **2,850** | **3,837** | **4,667** | **4,525** | **5,359** | **4,247** | **4,850** |

**BOTTOM-UP CROSS-CHECK, 2025, built from different lines entirely:** P&C underwriting income
$6,528M + Life underwriting −$12M − interest $764M − purchased-intangible amortisation $301M −
integration and severance $79M = **$5,372M**, against the top-down **$5,359M**. **Agreement within
$13M, 0.2%.**
**Two disclosures about the construction.** (a) Removing *all* of Other (income) expense removes a
small amount of genuinely operating income along with the portfolio marks — the direction is
**conservative**, and it is stated rather than tuned. (b) Noncontrolling interests are deducted at
the after-tax figure the filing gives ($312M in 2025), because no pre-tax NCI line is published;
the understatement is immaterial and named.

### THE SUM OF THE TWO COMPONENTS — AND WHY IT DISAGREES WITH THE FLOOR TEST, WHICH IS THE WHOLE
### POINT OF STEP 4
| construction | $M | per share |
|---|---|---|
| component 1 (as above) + component 2 5-yr mean capitalised at the ~10% floor rate | 116,540 + 42,475 = **159,015** | **≈ $412** |
| component 1 + component 2 5-yr mean capitalised at the sovereign 5.34% | 116,540 + 79,532 = **196,072** | **≈ $508** |
| component 1 + component 2 3-yr mean at the sovereign | 116,540 + 90,824 = **207,364** | **≈ $537** |

**On the sum of components, Chubb is worth $412 to $537 a share against a price of $340.64 — 17% to
36% below. THAT ANSWER IS REPORTED AND IT IS NOT THE VERDICT, AND THE REASON IS IN THE METHOD'S
OWN STEP 4**, which was corrected on 2026-09-02 by the BRK run for exactly this collision:
*"Berkshire is the exact case where the two disagree: **above the bond on every construction, below
the floor.**"*

**HERE IS WHY THE SUM IS THE HIGHER NUMBER, in one paragraph, because a run that reports both
without reconciling them has not done the work.** Component 1 counts the portfolio at market — i.e.
it capitalises a 3.8%-yielding bond book at about 26 times its income, which is correct for a bond
— while deducting none of the $68.0bn of float that funds 40% of it. **At Berkshire's 2010
calibration (investments 0.45x equity) that construction produces a component 1 BELOW book value
and adds nothing out of thin air. At Chubb's 2.29x it produces $302 a share against a book value of
$188.59 — 1.6x book — and $174 of that $302 is float that is not deducted.** CONVENTION 5 says
precisely this: *"where they are twice equity, most of the portfolio is funded by liabilities and
the valuation leans almost entirely on a condition the same passage calls volatile."* **The sum is
the right arithmetic for the components. The floor is the check on what the buyer's money actually
earns, and the floor comes first.**

### STEP 4 — THE FLOOR, FIRST [E4-28]
*"that's the figure we quit on … we don't want to buy equities where our real expectancy is below
10 percent. Now, that's true whether short rates are 6 percent or whether short rates are 1
percent."*

**MORE THAN ONE WINDOW, AND THE SPREAD IS PART OF THE RANGE [E4-25, E4-38].** *"growth-rate
presentations can be significantly distorted by a calculated selection of either initial or
terminal dates"* — so **every** window is published, as the corpus's own remedy prescribes.
Pre-tax operating income attributable to Chubb (income before tax, less realised gains, less
market-risk-benefit gains, less private-equity marks, less noncontrolling interests):

| window | pre-tax operating $M | per share | **yield on $131,419M** | sovereign | points over | growth needed to reach 10% |
|---|---|---|---|---|---|---|
| 2025 only | 12,000 | $31.10 | **9.13%** | 5.34% | **+3.79** | **0.87%/yr** |
| 3-yr 2023–25 | 10,799 | $27.99 | **8.22%** | 5.34% | **+2.88** | **1.78%/yr** |
| 5-yr 2021–25 | 9,339 | $24.21 | **7.11%** | 5.34% | **+1.77** | **2.89%/yr** |
| 7-yr 2019–25 | 8,162 | $21.16 | **6.21%** | 5.34% | **+0.87** | **3.79%/yr** |

*(2019 and 2020 are pre-LDTI and the private-equity mark is not separately disclosed for those
years, so those two cells remove realised gains only. Stated, not smoothed.)*

**THE WINDOW SPREAD IS 2.92 POINTS — 6.21% to 9.13% — AND IT IS ITSELF A Q4/Q5 FINDING [E5-11],
not an inconvenience to be resolved by preference.** What sits inside it: 2020 (a COVID and
catastrophe year, pre-tax operating $4,660M) and 2025 (a record, $12,000M). **[E3-55] scopes it
honestly:** where the mechanism is certain and only the year-to-year figure bounces, the bounce is
noise. **Here it is not only noise.** The seven-year series rises because premium rose 61% and
because margins improved; a mean of a rising series understates current earning power, and the
current year overstates normal margin. So both ends are wrong in known directions, and the fix is
to normalise rather than to pick.

**[E4-41] NORMALISE DOWN FOR LUCK — the corpus's own pro-forma that disclosed earnings too HIGH.**
The favourable exogenous break in this window is named: **the 2019–2023 commercial P&C hard
market.** Chubb's current-accident-year combined ratio including catastrophes improved from 93.4
(2019) to 88.2 (2025), 5.2 points on 58% more premium. Two normalisations, both shown:
- **Hard:** apply the ten-year mean current-accident-year combined ratio (92.3) to 2025 premium.
  Underwriting income $6,528M → **$3,526M**; pre-tax operating **$9.0bn**; **yield 6.85%; growth
  needed 3.15%/yr.** *This over-penalises, because four points of the improvement is a structural
  fall in the expense ratio (30.6 → 26.6) and not the cycle.*
- **Fair:** hold the expense ratio at today's 26.6, hold the catastrophe load at the ten-year mean
  6.4 (2025's actual was 6.3 — effectively unchanged), and take the current-accident-year loss ratio
  excluding catastrophes at the five-year mean 57.5 rather than 2025's 55.3. Current-accident-year
  combined ratio **90.5**; underwriting income **$4,350M**; pre-tax operating **$9.8bn**; **yield
  7.48%; growth needed 2.52%/yr.**
- **NORMALISED RANGE: 6.9% to 7.5% pre-tax. ONE windage, applied once, at one place. WINDAGE COUNT:
  1 [E4-11, E4-48].**

**AND THE AFTER-TAX FIGURE, SHOWN BECAUSE THE BUYER PAYS TAX AND THE READER IS ENTITLED TO SEE IT.**
Chubb's effective rate was 18.6% (2025) and 15.8% (2024), and Bermuda's 15% corporate income tax now
applies. **Net income attributable to Chubb ÷ cap: $10,310M / $131,419M = 7.85% (2025); on the
normalised base roughly 5.7–6.1%.** The pre-tax figure is the one the framework's template asks for
and the one the sovereign is quoted on, so pre-tax governs; the after-tax number is 1.3 to 1.5
points lower on every construction and it does not rescue any of them.

**THE FLOOR VERDICT.** **[E5-34]** states the routine: *"we will buy the stock … if it sells at a
reasonable price in relation to **the bottom boundary of our estimate**."* The bottom boundary here
is **6.21% unadjusted, 6.9% normalised** — and even the best single year is **9.13%, still below
the floor.** **Honest pre-tax expectancy: about 7% (range 6.2% to 9.1%). Against ~10%: BELOW.
THE NAME IS NOT RANKED — IT IS QUIT ON.** The lines below are filled in for the record and for the
Q6 bands, not as a ranking.

**[E4-35]'s BASE-RATE BURDEN, DISCHARGED HONESTLY IN BOTH DIRECTIONS.** *"fewer than 10 of the 200
most profitable companies in 2000 will attain 15% annual growth in earnings-per-share over the next
20 years."* **The growth this floor case needs is 2.5% to 3.8% a year, not 15%, so [E4-35] does not
bite** — and the realised record clears it easily (net premiums written +6.6% in 2025 and +8.7% in
2024; book value per share excluding AOCI +9.89%/yr over five years; share count −2.5%/yr).
**So why is the verdict still negative? Because 2.5–3.8% of growth on top of a ~7% normalised yield
reaches 10% only if the growth is real, perpetual, and not the cycle running in reverse — and
management's own current words say the cycle is turning: property rate down in 2025, casualty and
financial lines softening in 2026.** A floor case that needs growth from a business whose CEO is
describing a softening market is the case **[E4-18]** warns about: *"A conclusion that required
fighting for it is worth less, not more."* **I am not fighting for it.**

**[E2-63] — STATE THE CEILING TOO, NOT JUST THE YIELD.** What bounds the upside here is arithmetic,
not sentiment. Over five years the shares returned 15.19% a year, of which **about 8.1 points was
book value per share and about 6.6 points was the multiple going from 1.20x book to 1.66x.**
**[E4-44]:** *"the value of an asset, whatever its character, cannot over the long term grow faster
than its earnings do."* At today's 1.78x book (1.74x on the 6/30/26 book of $195.45), the multiple
is at the top of its own five-year range. **Forward return at an unchanged multiple is book value
growth plus the dividend yield: roughly 9.9% + 1.1% ≈ 11% if the hard-market ROE persists, and
roughly 8% if it does not. Forward return at a multiple that reverts to 1.2x over ten years is
about 3 to 6 points lower.** The multiple is the whole swing factor and it is not a business fact.
*"The Tinker Bell approach — clap if you believe — just won't cut it."*

### THE THREE REPORTED THINGS
**1. THE YIELD** — pre-tax operating income ÷ market capitalisation:
**6.21% (7-yr) to 9.13% (2025), normalised 6.9–7.5% · sovereign 5.34% (USD 30-yr, 2026-09-18).**

**2. WHAT THE PRICE ALREADY ASSUMES** — to justify $340.64 at the ~10% floor the business must
deliver **2.5% to 3.8% a year of perpetual growth in pre-tax operating income** from a normalised
base. What it has actually done: **+12.9%/yr from 2019 to 2025 through a hard market**, and
**+3.4%/yr in net premiums written in North America Commercial in 2025**, its largest segment, with
Major Accounts at **+1.4%**. **The needed rate is below the seven-year realised rate and above the
most recent year's rate in the segment that matters.** That is the honest statement of the gap and
it is why this is a price verdict rather than a business verdict.

**3. WHAT YOU ARE PAID** — **+0.9 to +3.8 points over the sovereign** (normalised: +1.5 to +2.1),
before any credit for growth, against a floor that is 4.7 points above the sovereign.

### WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42]
- **Sovereign used: 5.34%, the bare rate. No per-name premium added.** *"If you say I'm going to
  stick an extra 6 percent in on the interest rate … it's mathematical gibberish."*
- Certainty is handled **twice and neither place is the rate**: at Q1's understanding gate (passed —
  the mechanism is simple and stable), and in the end discount. **Priced ONCE. Windage count: 1**
  (the [E4-41] margin normalisation above). **No margin is stacked on top of it.**

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]
**Derived from the floor, which is the test that governs — the price at which the honest pre-tax
expectancy reaches 10%:**

| construction | pre-tax operating $M | price that clears the floor |
|---|---|---|
| hard normalisation (10-yr mean current-accident-year ratio) | 9,000 | **≈ $233** |
| fair normalisation | 9,800 | **≈ $254** |
| 3-year mean, unnormalised | 10,799 | **≈ $280** |
| 2025 alone, the record year | 12,000 | **≈ $311** |

> ### **PRICE: US$340.64** (2026-09-18 close, aggregator, **FLAGGED**) · **CAP US$131,419M**
> ### **VALUE, ROUND NUMBERS: ≈ $235 conservative · ≈ $275 central · ≈ $310 optimistic**
> ### Book value per share **$188.59** (12/31/25) and **$195.45** (6/30/26) · **price/book 1.74–1.78x**
> ### Tangible book value per share **$131.93** (6/30/26) · **price/tangible book 2.58x**
> ### **The sum of the two components, reported and not used, is $412–$537.**

**WHICH BAR — and only one is used.**
- [x] **Screamer test [E4-01]** — *"even very conservative estimates … reveal that the price quoted
  is startlingly low."* **The price is ABOVE the whole range. Outcome: NO.** This is not the
  price-inside-the-range case; it is 10% above the optimistic end and 24% above the central.
- [ ] Normal method [E4-11] — not used, and the reason is stated: applying a 35% bridge margin on
  top of the [E4-41] normalisation would spend conservatism twice, which **[E4-48]** forbids.
  **Windage count: 1.**
- **[E3-60]'s graded margin, for the record if a future run needs it:** this is a business one can
  understand (Q1 IN) with a volatile annual figure and a certain mechanism, so it sits nearer
  **[E4-12]**'s *"closer to a dollar on the dollar"* than the Grand Canyon's 60% — which is why the
  range above is derived from the floor rather than from a margin at all.

- **VERDICT: NOT IN — closed at Q5, ON PRICE. The [E4-28] floor is not met (honest pre-tax
  expectancy about 7%, range 6.2–9.1%, against ~10%). NOT RANKED — quit on [E4-28]. No position
  proposed. Ranking position: none.**
  **All four business gates returned IN. This is a verdict about the price on 2026-09-18, not about
  Chubb Limited.**

### STEP 5 — THE THIRD ELEMENT, STATED RATHER THAN SILENT [E5-50, E3-54]
*"a third, more subjective, element … that can be either positive or negative: the efficacy with
which retained earnings will be deployed in the future. … Some companies will turn these retained
dollars into fifty-cent pieces, others into two-dollar bills."*
**The judgment: MILDLY POSITIVE, and smaller than the retention test alone would suggest.**
- **For:** **[E3-54]** passes at **$1.50 of market value per $1 retained** (or $2.71 counting
  buybacks as distributions) over the current five years. Retained dollars go into an insurance
  book earning **26.0% on tangible equity**, and into a portfolio whose book yield (4.5%) is still
  below its market yield (5.0%), so the next retained dollar earns more than the last. No
  impairment has ever been taken on the $20.2bn of goodwill. The acquisitions are small, inside
  insurance, and inside the licensed geographies.
- **Against, and this is why it is mild not strong:** roughly **6.6 of the 15.19 points of annual
  return came from the multiple, not from retention**, so the retention test flatters. The capital
  allocation flag is **live** — repurchases at 1.5x book and 2.5x tangible book in 2025–26, above
  the conservative end of this run's range, with **no published repurchase condition** to test them
  against **[E5-25]**. The acquisition-every-year pattern is **[E2-30]**(2) fired. And the whole
  record belongs to one 22-year CEO with no named successor, which is **[E4-23]** at Q2 and
  **[E5-50]** here: *"if the CEO's talents or motives are suspect, today's value must be
  discounted"* — the talents are not suspect; their **duration** is the open question.
- **Net effect on the range: none, deliberately.** The third element is **stated as a judgment and
  not converted into a number**, because doing so would be a second windage on a name already
  normalised once.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**No position is held and none is proposed, so this is the re-look surface, pre-committed now
[E1-02]:** *"I believe in establishing yardsticks prior to the act."*

**THESIS-CONFIRMING METRIC:** the **current-accident-year combined ratio including catastrophes**,
rebuilt each year from the filer's own published points (CAY ex-CAT + catastrophe points). Ten-year
mean 92.3; 2025 88.2. **Confirms while it stays below 95.**

**THESIS-BREAKING METRICS AND THEIR THRESHOLDS — each one falsifies a specific sentence above:**
1. **The current-accident-year combined ratio including catastrophes exceeds 100 in any year other
   than a named 1-in-100 catastrophe year.** That is the MKL test failing, and it would reverse Q2
   to OUT. *(Falsifies: the ten-of-ten record.)*
2. **Long-tail prior-period development turns net ADVERSE for two consecutive years.** It was +$110M
   favourable in 2025 and +$8M in 2024; it is $110M from flipping. *(Falsifies: the cushion still
   has something in it.)*
3. **North America Commercial Liability adverse development exceeds $500M in a year**, or net IBNR
   on any accident year 2023 or later is revised up by more than 10%. *(Falsifies: the casualty
   drain is contained.)*
4. **The P&C expense ratio exceeds 28.0%** (it is 26.6%, up 1.0 point from the 2022 trough of
   25.6%). *(Falsifies: the cost advantage is durable.)*
5. **Net premiums written fall in North America Commercial for two consecutive years**, or the
   phrase describing rate decreases spreads from property to casualty in the 10-K itself rather
   than only in the CEO's commentary. *(Falsifies: the shrink-on-price discipline is cyclical
   rather than terminal.)*
6. **The cost of float turns positive on a five-year mean.** It is −8.58%. *(Falsifies: the funding
   moat.)*
7. **Any acquisition outside insurance, or any acquisition above $3bn, reopens the file at Q3
   before any price is read** — [E3-40] loss of focus is the vector, and the 2021 record of this
   management is a company that buys something every year.
8. **A CEO succession announcement reopens Q2** — the Mayo-Clinic test [E4-23] is live and
   unanswered, and the moat class is NARROW because of it.
9. **The leverage-metric redefinition recurring** — a second yardstick change following
   deterioration converts the [E2-49] prompt into a pattern.

**NEXT CATALYST DATES:** **Q3 2026 earnings 8-K, ~2026-10-20** (the current-accident-year ratio and
the PPD split for the quarter); **FY2026 10-K, ~late February 2027** — the document that carries the
next loss-development triangles, the next reserve sensitivity table, the next PML, and the first
full year in which management's own softening-market statement can be tested against outturn. **The
bands below must be re-derived at that filing and at the rate of the day.**

**THE RE-LOOK BANDS — a ping is a prompt to RE-RUN the gates, never a purchase [E5-36]:**
- **$310 or below** — the ~10% floor is met **only on 2025's record pre-tax operating income of
  $12.0bn**, which is above the normalised base and which management's own words say is a cyclical
  peak. **A prompt for a full v4.1 re-run in which that peak is re-tested before it is spent.**
- **$255 or below** — the floor is met on the **fairly normalised** base ($9.8bn), i.e. with the
  hard-market margin taken out, no growth granted, and the reserve cushion at zero. **The band
  where the arithmetic works on the filed record rather than on the cycle.**
- **Both bands VOID if any of falsifiers 1, 2, 3 or 6 has fired.** Both re-derive at the FY2026
  10-K.
- **PRE-COMMITTED SIZING, per [E5-08] and [E4-13]: if this name ever clears, it is SIZED DOWN,
  because the capital-allocation flag is live and because [E2-62] denies this balance sheet the
  concentration licence Berkshire's has.** And **[E4-45]**: a half-point ranking inversion moves
  nothing; the switching bar is tax plus friction plus a material gap.

**The sell rule [E2-28]**, recorded for the day it might apply: SELL if the market judges it more
valuable than the facts indicate; SELL if funds are needed for something more undervalued or better
understood; HOLD while the return on equity capital is satisfactory, management is competent and
honest, and the market does not overvalue. **Holdings are governed by
`Framework/THE HOLDINGS FRAMEWORK.md`, not by this file.** **No PERMANENT designation is made
[E2-39].** **[E4-17]**'s gradualism governs how the moat belief forms; **[E2-40]**'s
crystallized-view rule governs once it has formed.

- **VERDICT: [x] IN** as a monitoring surface. Nothing is armed as an action.

---
## SELF-AUDIT
- [x] **Questions answered in order; stopped at the first verdict that is not IN (Q5, on price).**
      No Q5 output was produced before Q1–Q4 each showed IN.
- [x] **No question marked IN carries an "unverified", "general knowledge" or "provisional"
      caveat.** Q2's class is NARROW, which is a moat class, not a caveat on the verdict; the two
      unobtainable peer cells (KNSL 2021 on the current basis, RLI 2021) are named, and neither
      changes the row's ranking or the verdict.
- [x] Every UNRESEARCHED verdict names the artifact — **there are none in this run.**
- [x] Every UNKNOWABLE verdict states what cannot be known — **there are none.**
- [x] **Step 0: the filing was read (MD&A, cash-flow statement including its detail lines,
      footnotes), with the accession number; FOUR figures were cross-checked against the filed
      statement**, including equity recomputed from assets less liabilities less minorities and the
      whole current-accident-year reconciliation re-derived for seven years.
- [x] **Sector method applied, both amendments included.** Stage 0(a) share count by hand off the
      cover with the Swiss issued-versus-outstanding trap tested by arithmetic; Stage 0(b) states
      **both** ratios (float ÷ investments 40.3%, investments ÷ equity 2.29x) and says what each
      implies; **step 2 is diagnostic and nothing was added to anything**; step 1 states gross
      versus net **with the argument**; **[E3-71]** deferred tax valued (nil, and why); step 4 puts
      the floor before the ranking; step 5's third element is stated, not silent.
- [x] **Owner earnings: NOT computed, and the reason is the method's own.** The Loews OCF test was
      run explicitly and its answer discarded, with the arithmetic shown.
- [x] **More than one window; the spread is carried as part of the range [E4-25, E4-38]** — four
      windows published, spread 2.92 points, and the distorted years named.
- [x] **Competitor row filled — extended from the MKL run rather than rebuilt, on two bases**, with
      seven peers, every accession independently re-resolved, and the two unobtainable cells named.
      The moat class is **not** marked PROVISIONAL: the metric was obtained for six of seven peers
      on the decisive basis.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated** (US Treasury
      30-year par yield, 5.34%, 2026-09-18), **with the multi-currency gap disclosed as unresolved
      per the sector method's FINDING 8** and the direction of the error stated.
- [x] **Value stated as a round-number range, not a point estimate.**
- [x] **One bar chosen, not both** (screamer test). **Windage count: 1** — the [E4-41]
      normalisation. No margin stacked on it.
- [x] **Prices dated; the aggregator is used for the live quote only and is flagged.**
- [x] **[E4-26] applied against the favourite hypothesis at three places**, in writing: the Q2
      moat case (six disconfirming facts listed), the Q3 incentive flag (five counterweights
      listed), and the Q5 sum-of-components result (reported, then reconciled against the floor and
      set aside with the reason).
- [x] `python tools/check_framework.py` — run before the commit.
- [x] Run committed to git with a pathspec.

## REGISTER
- **Verdict: [x] NOT IN — closed at Q5 ON PRICE (about the price, not the business).** Q1 IN · Q2
  IN (NARROW) · Q3 IN (as a binary gate) · Q4 IN.
- **One line:** *Chubb is the first name in this queue to pass the MKL test outright — its
  current-accident-year combined ratio including catastrophes has been under 100 in ten of ten
  years, worst 97.9, so the reported underwriting profit is earned and not released — and it holds
  $68.0bn of float at a five-year cost of **minus 8.58%**, better than Berkshire's −3.6% on the same
  five years; the funding moat, the licence network and a 26.6% expense ratio put it **third of
  seven** on the honest basis where the reported basis put it fourth; and at **$340.64** the honest
  pre-tax expectancy is about **7%** (6.2–9.1% across four windows) against the ~10% floor, so it is
  **quit on, not ranked**, with re-look bands at **$310** and **$255**.*
- **THE STRONGEST SINGLE FACT AGAINST MY CONCLUSION:** on the sector method's own two-component
  sum — investments at market with float counted as free funding, exactly as **[E5-46]** prescribes
  and on the ten-year break-even record that licenses it — **Chubb is worth $412 to $537 a share
  against a price of $340.64**, and management says in a filed release that *"our stock is trading
  well below intrinsic value."* My negative verdict rests entirely on preferring the earnings-yield
  floor to the sum of the parts, and on a ~10% hurdle Buffett himself calls arbitrary. **If
  counting a bond portfolio at market rather than at ten times its coupon is right — and for a bond
  it plainly is — then this run is wrong and Chubb is cheap.**
- **Not UNRESEARCHED and not UNKNOWABLE.** No document was named and not fetched.
