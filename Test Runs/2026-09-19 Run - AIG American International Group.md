# Company Run — American International Group, Inc. (AIG) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file and that
document disagree, that document governs.

**WAVE 6 of the operator's watchlist queue; MINI BERK insurance track.** The disposition in
`Screens/WATCHLIST RUN QUEUE.md` read *"RUN on the Mini Berk track"*; the class ("insurer") and the
precedents were read as prompts, never as a verdict. **There is no screen row for AIG** in
`Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, so nothing here comes from tagged data.
**Sector method applies and was read in full, both amendments included:**
`Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`
— two measurable components plus a judgment **[E5-46, E5-47, E5-48, E5-50]**, float as the
FUNDING of the investments, **[E3-69]**'s underwriting-loss-to-float as the profitability measure,
step 2 DIAGNOSTIC, NOT ADDITIVE.

**CIK 0000005272** (`AMERICAN INTERNATIONAL GROUP, INC.`), found by `tools/sources.py:cik_for('AIG')`,
not taken from the brief. Submissions `formerNames`: *"AMERICAN INTERNATIONAL GROUP INC"* from
1994-08-12 to 2021-02-10 (a punctuation change only; same registrant). **SIC 6331, Fire, Marine &
Casualty Insurance.** Delaware; New York headquarters; USD-reporting.

**Arithmetic is reproduced by scripts in `Test Runs/_research 2026-09-19 AIG/`:** `triangles.py`
(→ `triangles_out.txt`, the Note 13 loss triangles), `peers/resolve.py` (→ `peers/resolve_out.txt`,
every peer accession re-resolved), `peers/build_row.py` (→ `peers/row_out.txt`, the competitor row),
`arith.py` (→ `arith_out.txt`, Stage 0 and Q3-Q5 arithmetic). Research notes: `notes_FY2025_10K.md`.

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

**VERDICT LINE: Q1 IN · Q2 OUT (closes the file, on the business) · Q3, Q4 RECORDED, NOT GOVERNING
· Q5 COMPUTATION ONLY, NOT A CLEARANCE · Q6 reversal conditions in words, no bands.**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]** — struck fresh for this run:
- **5.34% · 2026-09-18 · US Treasury daily par yield curve, 30-year** (the issuing authority, via
  `tools/sources.py:sovereign('USD')`, which returned `(5.34, '09/18/2026', 'US Treasury daily par
  yield curve')`; FRED DGS30 is the fallback and was not used). Struck by this run, not inherited;
  it happens to equal the CB run's figure because both read the same Treasury print.
- **The earnings currency, argued rather than assumed — and FINDING 8 recurs, larger than at
  Chubb.** Note 3 of the FY2025 10-K splits 2025 total revenue **North America $12,699M / International
  $14,076M — 52.6% of revenue is earned outside North America** ("International revenues consists of
  revenues from our General Insurance International operations"). 47% of AIG's 22,100 employees are
  in Asia-Pacific; the Global Personal segment is heavily Japanese (the 10-K names *"UK/Europe and
  Japan Personal Insurance"* as a reserve line and the JFSA as a regulator), and AIG issued
  ¥100bn of debt in 2024. **The framework has no stated answer for one company earning in many
  currencies (sector method, FINDING 8).** Per that amendment's standing instruction the exposure is
  stated, **the reporting currency's sovereign is used, and the choice is disclosed as unresolved.**
  Direction of the error: Japan's and the euro area's long rates sit below the US 30-year, so the
  USD rate is the **conservative** choice for the 53% earned abroad.
- FX: none needed. Quote and reporting currency are both USD. No ADR.

**The filing was read — not tagged data [E3-27, E4-14].** No figure in this run comes from XBRL;
`tools/run.py` was not used for this filer.
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (Notes 1, 3, 4, 13 with all
  ten loss-development triangles, the NICO reinsurance note, Note 21 tax)
- **FY2025 Form 10-K, period 2025-12-31, filed 2026-02-12, accession `0000005272-26-000023`,
  document `aig-20251231.htm`.** Also read: **FY2023 10-K `0000005272-24-000023`** (2021-2023),
  **FY2021 10-K `0001104659-22-024701`** (2019-2021), **FY2018 10-K `0000005272-19-000023`** (2016-2018),
  **Q2 2026 10-Q `0000005272-26-000076`** (filed 2026-08-07), **DEF 14A 2026-03-31
  `0000005272-26-000039`**, the four quarterly earnings 8-Ks with their EX-99.1 releases
  (`0000005272-26-000072` Q2 2026, `0000005272-26-000048` Q1 2026, `0000005272-26-000014` Q4 2025,
  `0000005272-25-000156` Q3 2025), and the two September 2026 Item 5.02 8-Ks (`0000005272-26-000088`
  with its EX-99.1, and `0000005272-26-000091`). **The 8-K EX-99.1 releases were pulled before
  scoring [E4-29] and [E4-22]'s third flag, per the standing CGNX rule.**
- **Figures cross-checked against the filed statement:**
  1. **Total AIG shareholders' equity recomputed from the balance-sheet identity** ([E5-32], the
     Salomon cross-check): total assets $161,254M − total liabilities $120,092M − non-redeemable
     noncontrolling interests $23M = **$41,139M**, the filed line exactly. At 6/30/26: $163,464M −
     $122,838M − $20M = **$40,606M**, the filed line exactly.
  2. **Book value per share recomputed**: $41,139M ÷ 538.2M shares = **$76.44**, the filed figure.
  3. **The decisive Q2 series re-added from its own components in every one of ten years**
     (AYCR ex-CAT + CAT − favourable PYD ± the filer's "other" adjustment = reported GI combined
     ratio): 96.0+4.4+18.5 = 118.9 (2016) · 97.1+16.1+4.0+0.1 = 117.3 (2017) · 99.7+10.5+1.5−0.3 =
     111.4 (2018) · 96.0+4.8−1.1−0.1 = 99.6 (2019) · 94.1+10.3−0.1 = 104.3 (2020) · 91.0+5.4−0.6 =
     95.8 · 88.7+5.0−1.8 = 91.9 · 87.7+4.3−1.4 = 90.6 · 88.2+5.0−1.4 = 91.8 · 88.3+3.9−2.1 = 90.1.
     **All ten reconcile to the reported ratio.**
  4. **General Insurance underwriting income built from dollars** (2025): NPE $23,678M − losses
     $13,968M − acquisition $4,295M − general operating $3,083M = **$2,332M**, the filed figure; and
     APTI $5,344M = GI underwriting $2,332M + GI net investment income $3,433M − Other Operations
     $421M, to the dollar.
  5. **Share count** — see Stage 0(a).

**Ladder rungs used:** SEC XBRL not used; SEC EDGAR primary documents for AIG and for every peer. No
aggregator except the live quote, flagged.

---
## STAGE 0 — THE SECTOR METHOD'S ARTIFACT CHECK

### 0(a) — SHARE CLASS AND COUNT, BY HAND OFF THE COVER
AIG has **one class** of common stock, $2.50 par (the 8-K cover lists only *"Common Stock, Par Value
$2.50 Per Share | AIG"*; the preferred series was redeemed — preferred equity $485M at 2023, nil at
2024 and 2025).
- **10-Q cover, filed 2026-08-07 (accession `0000005272-26-000076`), line 50:** *"As of July 31,
  2026, there were **522,893,169** shares outstanding of the registrant's common stock."*
- **The issued-versus-outstanding trap tested by arithmetic, not by caption.** The same 10-Q's balance
  sheet at 2026-06-30: shares issued **1,906,671,492**, treasury **1,381,952,801** → outstanding
  **524,718,691**, which is the release's "524.7" million. **The cover (522.9M) sits beside the
  outstanding figure, not the issued figure (1,906.7M).** Using issued shares would overstate the cap
  3.6-fold. The 1.8M gap from 6/30 to 7/31 is the July buyback: the 10-Q states that *"from July 1,
  2026 to July 31, 2026, AIG Parent repurchased approximately 2 million shares of AIG Common Stock for
  an aggregate purchase price of approximately $195 million."*
- **Post-cover events checked (the USAR lesson):** the 10-Q states *"as of July 31, 2026, $2.6 billion
  remained under the Board's authorization"* and a Rule 10b5-1 plan is running. **No issuance after
  the cover was found** in any 8-K through 2026-09-16 (the two later 8-Ks are Item 5.02 only). The
  direction of any post-cover drift is **down** (buybacks), so the cover count slightly **overstates**
  today's count; not adjusted, because the amount is not filed.
- Cross-check on a third document: the 10-K cover gives **536,559,663 at 2026-02-06**; the release
  gives **559.8M at 2025-06-30**, 538.2M at 2025-12-31. The count is falling fast (below).
- **Count used: 522,893,169.**

**PRICE: US$75.33 at the 2026-09-18 close** (`tools/sources.py:price('AIG')`, aggregator —
**FLAGGED**, live quotes only). **MARKET CAPITALISATION: US$39,389M.**

### 0(b) — INSURER, FLOAT-BEARING HOLDING COMPANY, OR NEITHER — AND BOTH RATIOS
**AIG is today an insurer, not a holding company that owns one** — and that is a recent fact, which
is the perimeter finding below. Three segments, all property-casualty (North America Commercial,
International Commercial, Global Personal) plus Other Operations; $23.7bn of 2025 net premiums
written; $70.7bn of gross unpaid losses.

**THE PERIMETER — the brief's prior tested, and partly refuted.**
- **Confirmed:** Corebridge (the former Life and Retirement business) was **deconsolidated on
  2024-06-09** when AIG held 48.4% and *"waived its right to majority representation"*; AIG booked a
  **$4.8bn loss in discontinued operations**, *"mainly due to the recognition of an accumulated
  comprehensive loss of $7.2 billion."* **Corebridge's historical results are presented as discontinued
  operations** (FY2025 10-K Note 4), so the 10-K's income statement shows **continuing operations for
  2023-2025 only**, with Corebridge in a single discontinued line ($1,137M income 2023, $(3,626)M loss
  2024).
- **Carrying basis, as asked:** from deconsolidation AIG *"elected the fair value option and reflects its
  retained interest in Corebridge as an equity method investment in Other invested assets using
  Corebridge's stock price as its fair value"*, with dividends and price changes in net investment
  income; at 2025-12-31 AIG held **10.1%, carried at $1,512M**.
- **REFUTED — the brief assumed AIG "still holds" Corebridge. It does not.** Q2 2026 10-Q Note 1:
  Corebridge bought back 24.7M shares from AIG at $30.42 (**$750M**, 2026-02-17); AIG lost significant
  influence at 2026-03-31; and *"On May 7, 2026, we sold 25.5 million shares of Corebridge common stock,
  representing our remaining interest in Corebridge, at a per share purchase price of $27.90"*
  (**~$710M**). **AIG's Corebridge stake is zero.** It bears on nothing in component 1 today.
- **The perimeter moved in every year of the window, and the direction was always subtraction until
  2026:** sold Fortitude Re majority (2020), Validus Re and Crop Risk Services (2023, the Validus
  dispositions line shows **$3,505M of net reserves** leaving), the global individual travel business
  (December 2024, **$718M of NPW**), deconsolidated AIG Financial Products in its December 2022 Chapter
  11 (a **$37.6bn loan receivable carried with a full allowance**), and Corebridge (2024-2026). **Then
  it turned to addition:** Everest's retail commercial renewal rights ($301M, 2025), **a 35% equity
  stake in Convex Group for $2.1bn and 9.9% of Onex for $642M (both closed 2026-02-06)**, a Convex
  whole-account quota share (7.5% → 12.5% of Convex's book, 2026-2028), and a CVC asset-management
  partnership.
- **THE FINDING THE BRIEF ASKED FOR: no five-year window on today's perimeter exists at the
  consolidated level.** Continuing operations are published for 2023-2025, and 2023 still contains
  Validus Re and Crop Risk Services; 2024 still contains the travel business. **The one series that
  runs continuously across the whole decade is the General Insurance segment's underwriting result,
  reported by the filer each year with the ratio decomposition** — and that is the series Q2 turns
  on. **So the perimeter finding bears on Q3's primary test (ROE) and on Q5's windows, NOT on Q1
  and NOT on Q2**: the decisive Q2 series is published, reconciled and continuous.

**CONVENTION 4 float** = unpaid losses and LAE + unearned premiums − reinsurance recoverable on unpaid
losses − premiums and other receivables − deferred policy acquisition costs. **The word "float" is not
used by AIG in [E5-46]'s sense and AIG publishes no float figure** (the WTM finding, recurring).

| 12/31 | float $M | investments $M | AIG equity $M | float ÷ investments | investments ÷ equity | float ÷ equity |
|---|---|---|---|---|---|---|
| 2024 | 69,168 + 17,232 − 29,026 − 10,463 − 2,065 = **44,846** | 93,613 | 42,521 | 47.9% | 2.20x | 1.05x |
| **2025** | 70,666 + 17,991 − 28,871 − 10,441 − 2,106 = **47,239** | **92,999** | **41,139** | **50.8%** | **2.26x** | **1.15x** |

*(2023 and earlier are not computed on this recipe: until 2024-06-09 the consolidated balance sheet
carried Corebridge's receivables and roughly $10bn-scale life DAC, which would corrupt two of the five
terms. For the longer diagnostic at Q4 a net-loss-reserve proxy is used and confessed there.)*

**BOTH RATIOS, STATED, against the panel (the second amendment's requirement):**

| | float ÷ investments | investments ÷ equity |
|---|---|---|
| BRK 2010, the method's calibration **[E5-46]** | 41.8% | 0.45x |
| CB 12/31/25 (this project's CB run) | 40.3% | 2.29x |
| MKL (MKL run) | 50.3% | 2.01x |
| **AIG 12/31/25** | **50.8%** | **2.26x** |

**What they imply.** On the first ratio AIG sits **above** [E5-46]'s own calibration point — float
funds half the portfolio — so step 2 is a **major** term, as at Chubb and Markel. On the second, AIG
is at Chubb's level: most of the portfolio is funded by liabilities, and CONVENTION 5 applies at full
strength — [E5-46] licenses counting the portfolio gross **on the express condition that underwriting
breaks even**, so the whole valuation leans on whether that condition holds. **Neither ratio is a
threshold. Both say the same thing: the answer lives in the underwriting record, which is Q2.**
**One more thing is not like Chubb and it is recorded here because it changes what "float" means at
this filer:** a large block of AIG's pre-2016 US long-tail reserve risk is **reinsured to Berkshire
Hathaway's National Indemnity (the NICO adverse development cover, 2017)**; its recoverable sits
inside the $28.9bn of reinsurance recoverables netted above. Part of AIG's "float" is therefore
Berkshire's balance sheet, not AIG's. (Detail at Q2 and Q4.)

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** AIG sells commercial and personal
insurance promises around the world, collects the premium now and pays claims over months (property,
travel, accident and health) to decades (US workers' compensation, excess casualty). Two engines, and
the 10-K names them itself: *"We earn revenues primarily from insurance premiums and income from
investments."*

1. **The underwriting spread.** $23.7bn of net premium earned in 2025 against $14.0bn of losses,
   $4.3bn of commissions and acquisition costs and $3.1bn of overhead, leaving **$2,332M of
   underwriting income, a 90.1 combined ratio**.
2. **The portfolio.** The $47.2bn of float plus $41.1bn of equity and $9.0bn of debt fund a
   **$93.0bn portfolio** ($71.0bn of available-for-sale bonds, $11.1bn short-term, $6.7bn other
   invested assets including the Convex stake from 2026, $2.9bn of loans). General Insurance net
   investment income was **$3,433M** in 2025.

**Where the earnings actually come from — filed numbers, 2025 ($M):**

| | $M | share of APTI |
|---|---|---|
| General Insurance underwriting income | 2,332 | 44% |
| General Insurance net investment income | 3,433 | 64% |
| Other Operations net investment income and other (parent liquidity portfolio, Corebridge dividends) | 349 | 7% |
| less corporate general operating expense, intangible amortisation, interest | (770) | −14% |
| **Adjusted pre-tax income (APTI)** | **5,344** | 100% |
| *GAAP income from continuing operations before tax, after $1,202M of realised losses, $439M of restructuring and other items excluded from APTI* | *3,879* | |

**The shape is the ordinary insurer shape, not Chubb's.** At Chubb underwriting and investment
income were roughly half and half; **at AIG the portfolio earns about 1.5 times what underwriting
earns**, and the parent costs a seventh of the total.

**The segments as filed, FY2025 ($M):**

| segment | NPW | NPE | underwriting income | CR | AYCR ex-CAT | CAT pts | PYD pts |
|---|---|---|---|---|---|---|---|
| North America Commercial | 8,759 | 8,626 | 1,144 | 86.8 | 85.8 | 5.6 | 4.6 fav |
| International Commercial | 8,663 | 8,580 | 1,118 | 86.9 | 85.6 | 2.2 | 0.9 fav |
| Global Personal | 6,253 | 6,472 | 70 | **99.0** | **95.7** | 3.9 | 0.6 fav |
| **General Insurance** | **23,675** | **23,678** | **2,332** | **90.1** | **88.3** | 3.9 | 2.1 fav |

**The two commercial segments carry the company; the personal segment runs at break-even** (combined
ratio 100.1 in 2023, 98.0 in 2024, 99.0 in 2025) on 27% of premium. That is recorded at Q2 as the
[E2-56] Pro-Am question.

**The scarce input this business controls.** Not the product — [E2-70] settles that for the whole
industry, and AIG's own Item 1 agrees: *"General Insurance operates in a highly competitive industry
against global, national and local insurers and reinsurers and underwriting syndicates."* What AIG
claims is **the global licence network** (*"over 200 countries and jurisdictions … through AIG
operations, licenses and authorizations as well as network partners"*) and **multinational capacity**
for large corporate buyers — the same class of claim Chubb makes. Whether that input produces an
advantaged *result* is a Q2 question and is tested there.

**Will the fundamentals look broadly the same in ten years?** The mechanism, yes — someone will insure
a multinational's property and liability in 2036, priced annually, with the money held in between.
**[E3-31]'s second clause is where AIG is weaker than Chubb:** *"If a business is complex or subject to
constant change, we're not smart enough to predict future cash flows."* AIG has been **subject to
constant change** for a decade — a different perimeter in every year of the window (Stage 0(b)) and,
in 2026, a **complete change of top management** (Q3). **Recorded, and judged NOT to fail Q1**, for a
stated reason: every perimeter change through 2025 was a *subtraction toward* a plain P&C insurer, so
the business a buyer owns today is simpler than at any time since 2008, and its mechanism is fully
legible from the filing. The 2026 additions (Convex, Onex) are minority stakes carried as investments.
**The constant change bears on how much history is evidence (Q2, Q5), not on whether the mechanism
is understood.**

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**State the moat claim honestly before testing it, because the corpus's own verdict on this industry
is hostile.** **[E2-70]**, 1977: *"Insurance companies offer standardized policies which can be copied
by anyone. Their only products are promises. It is not difficult to be licensed, and rates are an
open book. There are no important advantages from trademarks, patents, location, corporate longevity,
raw material sources, etc."* The sector method: *"an insurance underwriting operation is close to a
commodity, and the [E3-03] franchise question is therefore harder here than in retail, not easier."*

**AIG's own risk factors and MD&A say the same, and the Q2 2026 release says the price cycle has
turned:** *"the current market, which has transitioned from an extended phase of broad positive
pricing into a more selective environment, where profitability and growth are increasingly dependent
on line-specific dynamics"* (CEO, 2026-08-06). That is **[E2-58]**'s equation arriving on schedule —
*"persistent over-capacity without administered prices (or costs) equals poor profitability"*, set by
*"the ratio of supply-tight to supply-ample years."* **So the moat, if any, must be the funding, the
licence network or the cost base — as at Chubb — and each is tested below against the record and the
row.**

### THE DECISIVE SERIES — the MKL/CB precedent, run on ten years
**[E4-40] is why this comes first:** *"all of us in the industry made a fundamental underwriting
mistake by **focusing on experience, rather than exposure**."* The MKL run closed Markel at Q2 because
its current-accident-year combined ratio was ~100 for 2023-25; the CB run cleared Chubb because its was
**below 100 in ten of ten years, worst 97.9, mean 92.3**. AIG was put to the identical test, from the
filer's own published points, each year taken from the 10-K that first reported it.

| year | AYCR **ex** CAT | + CAT pts | **= CAY COMBINED RATIO INCL. CATASTROPHES** | PYD pts (+ fav / − adverse) | reported GI CR | source |
|---|---|---|---|---|---|---|
| 2016 | 96.0 | 4.4 | **100.4** | **−18.5** | 118.9 | FY2018 10-K `0000005272-19-000023` |
| 2017 | 97.1 | 16.1 | **113.2** | **−4.0** | 117.3 | FY2018 10-K |
| 2018 | 99.7 | 10.5 | **110.2** | **−1.5** | 111.4 | FY2018 10-K |
| 2019 | 96.0 | 4.8 | **100.8** | +1.1 | 99.6 | FY2021 10-K `0001104659-22-024701` |
| 2020 | 94.1 | 10.3 | **104.4** | +0.1 | 104.3 | FY2021 10-K |
| 2021 | 91.0 | 5.4 | **96.4** | +0.6 | 95.8 | FY2021 and FY2023 10-K `0000005272-24-000023` |
| 2022 | 88.7 | 5.0 | **93.7** | +1.8 | 91.9 | FY2023 10-K |
| 2023 | 87.7 | 4.3 | **92.0** | +1.4 | 90.6 | FY2023 and FY2025 10-K (identical) |
| 2024 | 88.2 | 5.0 | **93.2** | +1.4 | 91.8 | FY2025 10-K `0000005272-26-000023` |
| 2025 | 88.3 | 3.9 | **92.2** | +2.1 | 90.1 | FY2025 10-K |
| **10-yr mean** | **92.7** | **7.0** | **99.65** | **−1.55** | **101.2** | |
| **5-yr mean 2021-25** | **88.8** | **4.7** | **93.5** | **+1.5** | **92.0** | |

*(Each row re-adds to the reported ratio — Step 0 cross-check 3. The filer's own "other" adjustments of
−0.1, +0.3 and +0.1 points in 2017-2019 are the small residuals. AIG's GI ratios **exclude** the net
loss reserve discount and the prior-year development ceded to NICO under the retroactive covers,
*"Consistent with our definition of APTI"*; on a full GAAP basis they would be slightly worse — the
discount charge alone was $48M, $226M and $195M in 2025-2023, about 0.2 to 0.9 points.)*

**THE FINDING — and it is Chubb's result inverted for the first half of the decade.** **AIG's
current-accident-year combined ratio including catastrophes was above 100 in FIVE of the last ten
years (2016, 2017, 2018, 2019, 2020), worst 113.2, ten-year mean 99.65.** On the business it actually
wrote, AIG broke even over the decade at best. Chubb, on the identical construction and the identical
years, never exceeded 97.9 and averaged 92.3. **2017 is the cleanest same-year test — Harvey, Irma
and Maria hit both: Chubb 97.9, AIG 113.2. 2020, the COVID and catastrophe year: Chubb 97.4, AIG
104.4.** And the reserve column shows the other half of the story: **18.5 points of ADVERSE
development in 2016 (the Q4 2016 reserve charge; the FY2018 10-K: "$5.4 billion in 2016"), 4.0 more in
2017, 1.5 in 2018** — the earlier years' underwriting was worse than first reported, on top.

**The second half of the decade is a real turnaround and it is recorded as one.** Below 100 in every
year 2021-2025, mean **93.5**, the accident-year loss ratio ex-CAT down from 64.0 (2018) to 57.2
(2025), the expense ratio from 35.7 (2018) to 31.1. Favourable development in every year 2019-2025.
**The turnaround coincides with the 2019-2023 hard market [E3-51], and with a portfolio remediation
the filer describes as reducing limits, buying reinsurance and exiting lines** — and it is the product
of named managers, which is the key-person finding below.

### THE LOSS TRIANGLES — reserving is where this sector's candor lives [E2-50, E2-67]
Note 13 publishes ten ten-year net incurred triangles, **undiscounted, net of external reinsurance,
before the NICO cessions** (accident years 2016-2025, which are **outside** the ADC, which covers
2015 and prior — so every movement below is AIG's own). First estimate to the 2025 estimate
(`triangles.py`):

| line | tail | AY2016 | AY2017 | AY2018 | AY2019 | AY2020 | AY2021 | AY2022 | AY2023 | AY2024 | all AYs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **US Excess Casualty** | long | **+45.3%** | **+48.4%** | **+17.6%** | +1.2% | −2.7% | **+37.8%** | **+21.0%** | **+8.1%** (2 yrs) | 0.0% | **+22.2%** |
| **US Financial Lines** | claims-made | **+46.1%** | **+25.7%** | **+37.8%** | **+30.5%** | **+22.0%** | −13.0% | −6.5% | +3.1% | +1.4% | **+17.4%** |
| **UK/Europe Casualty & Financial Lines** | long | **+30.7%** | +7.7% | **+30.9%** | **+14.1%** | −10.5% | −9.6% | −5.6% | +0.2% | +2.8% | **+6.1%** |
| US Other Casualty | long | −7.3% | +8.6% | +6.2% | −4.7% | −4.8% | +6.3% | +8.6% | +5.4% | +3.7% | +1.5% |
| US Workers' Compensation | long | −26.3% | −15.8% | −22.9% | −22.9% | −29.5% | −10.7% | −5.2% | −4.8% | −4.8% | **−16.7%** |
| US Property & Special Risks | short | +2.1% | −8.6% | +7.6% | +1.7% | −3.0% | −6.8% | +2.0% | −6.4% | −7.0% | −2.0% |
| US Personal | short | | | | | | | | | | −2.9% |
| UK/Europe Property & Special Risks | short | | | | | | | | | | −2.4% |
| UK/Europe & Japan Personal | short | | | | | | | | | | −3.5% |

**THE DIRECTION OF THE ERROR, stated, and it is the opposite of Chubb's in the lines that matter:**
- **Excess casualty and financial lines — the core of a large-account commercial insurer — were
  systematically UNDER-reserved at first estimate.** US Financial Lines was adverse on **every accident
  year 2016-2020 by 22% to 46%**; US Excess Casualty on 2016-2018 by 18% to 48%.
- **And the adverse pattern in excess casualty is not only legacy.** **AY2021 +37.8%, AY2022 +21.0%,
  AY2023 +8.1% in two years** — accident years written **after** the turnaround began, on the
  turnaround's own book. US Other Casualty AY2021-2024 has also developed adversely in every year
  (+3.7% to +8.6%). Only US Financial Lines has turned (AY2021-22 favourable).
- **Workers' compensation and short-tail lines are over-reserved and released** — the same
  conservative bias Chubb shows there, and the source of most of AIG's favourable totals.
- **Does the filer name it? Yes, in words, line by line**: 2024, *"Unfavorable development on U.S. Excess
  Casualty of $545 million driven by a large settlement of a legacy mass tort claim … and increased
  reserves related to claims emergence"*; 2025, *"Unfavorable development on U.S. Excess Casualty of
  $303 million driven by unfavorable development in Mass Tort"*, and UK/Europe Casualty and Financial
  Lines adverse **$165M, $170M and $216M in 2023, 2024 and 2025 — three consecutive years, rising.**
  **Before the NICO cessions, 2024's total prior-year development was $254M ADVERSE**; after the cover
  and the deferred-gain amortisation it is reported as $368M favourable.

### THE NICO ADVERSE DEVELOPMENT COVER — the most informative fact in the file for Q2
FY2025 10-K: *"In the first quarter of 2017, we entered into an adverse development reinsurance
agreement with NICO, under which we transferred to NICO 80 percent of the reserve risk on
substantially all of our U.S. Commercial long-tail exposures for accident years 2015 and prior. Under
this agreement, we ceded to NICO 80 percent of the losses on subject business paid on or after
January 1, 2016 in excess of $25 billion of net paid losses, up to an aggregate limit of $25 billion
… Berkshire Hathaway Inc. has provided a parental guarantee."*
- **Inception-to-date net paid losses on the covered book: $30,157M (2023) → $31,545M (2024) →
  $32,588M (2025), against a $25,000M attachment.** Covered reserves still outstanding before
  discount: **$8,907M**. **So the pre-2016 US long-tail book has already paid $7.6bn more than the
  point at which AIG judged in 2017 that it would need protection, with $8.9bn still to pay** — the
  quantified size of the reserve deficiency AIG carried into 2016, now largely Berkshire's to fund.
- **Read against the corpus, this is [E2-67] from the other side of the table**: Berkshire published its
  own reserving errors *"so you can … judge whether we may have some systemic bias"*; here Berkshire
  is the **counterparty that priced and absorbed** another insurer's systemic bias. The cover was
  prudent and it is scored as prudent at Q3. **At Q2 what it proves is that the underwriting of the
  prior decade was not a franchise's**: a franchise does not need to pay a competitor to take its
  long-tail reserve risk away.

### THE COMPETITOR ROW — required [E3-28], EXTENDED FROM CB RATHER THAN REBUILT
The CB run's ten-name row (itself extended from MKL) is carried forward unchanged. **Every accession
it cites was re-resolved from each registrant's own submissions JSON: 15 of 15 MATCH**
(`peers/resolve_out.txt`). **Extended with AIG and with the two peers that compete with AIG in
large-account US commercial lines and were absent from a specialty-weighted row:** **Travelers**
(consolidated; FY2025 10-K `0000086312-26-000065`, FY2023 `0000086312-24-000012`, FY2022
`0000086312-23-000011`) and **The Hartford's Business Insurance segment** (FY2025 10-K
`0000874766-26-000012` lines 2311-2319, FY2023 `0000874766-24-000016` lines 2473-2481) — segment rather
than consolidated because The Hartford's P&C total is not published as one ratio in those tables;
**flagged as a segment basis.**

**BASIS 1 — reported combined ratio, 2021-2025:**

| company | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|---|
| Kinsale (KNSL) | 77.1 | 78.5 | 75.4 | 76.4 | 75.9 | **76.66** |
| Arch (ACGL) | 85.2 | 81.6 | 79.3 | 82.5 | 82.8 | **82.28** |
| RLI | 86.8 | 84.4 | 86.6 | 86.2 | 83.6 | **85.52** |
| Chubb (CB) | 89.1 | 87.6 | 86.5 | 86.6 | 85.7 | **87.10** |
| W. R. Berkley (WRB) | 89.6 | 89.3 | 89.7 | 90.3 | 90.7 | **89.92** |
| Hartford Business Ins. (HIG-BI) † | 95.8 | 90.2 | 89.6 | 89.9 | 88.3 | **90.76** |
| **AIG (General Insurance)** | **95.8** | **91.9** | **90.6** | **91.8** | **90.1** | **92.04** |
| Fairfax (FFH) | 95.0 | 94.7 | 93.2 | 92.7 | 93.0 | **93.72** |
| Travelers (TRV) ‡ | 94.5 | 95.6 | 97.0 | 92.5 | 89.9 | **93.90** |
| Markel (MKL) | 90.0 | 92.0 | 98.8 | 95.5 | 94.6 | **94.18** |
| Axis (AXS) | 97.5 | 95.8 | 99.9 | 92.3 | 89.8 | **95.06** |

**BASIS 2 — CURRENT-ACCIDENT-YEAR combined ratio including catastrophes (reported + each filer's own
favourable prior-year development points):**

| company | 2021 | 2022 | 2023 | 2024 | 2025 | mean | yrs |
|---|---|---|---|---|---|---|---|
| Kinsale (KNSL) | 82.6 | 82.9 | 78.6 | 79.1 | 79.8 | **80.60** | 5 |
| Arch (ACGL) | 89.6 | 89.5 | 83.6 | 85.9 | 86.3 | **86.99** | 5 |
| Chubb (CB) | 91.9 | 90.4 | 88.4 | 88.6 | 88.2 | **89.50** | 5 |
| W. R. Berkley (WRB) | 89.7 | 88.9 | 89.5 | 90.3 | 90.7 | **89.84** | 5 |
| Hartford Business Ins. † | 94.3 | 92.4 | 91.5 | 91.7 | 91.5 | **92.28** | 5 |
| RLI | n/a | 95.2 | 95.0 | 92.4 | 89.7 | **93.08** | 4 |
| **AIG (General Insurance)** | **96.4** | **93.7** | **92.0** | **93.2** | **92.2** | **93.50** | 5 |
| Axis (AXS) | 98.2 | 96.3 | 91.8 | 92.8 | 91.4 | **94.10** | 5 |
| Travelers (TRV) ‡ | 96.3 | 97.5 | 97.4 | 94.2 | 92.3 | **95.54** | 5 |
| Markel (MKL) | n/a | n/a | 99.3 | 101.1 | 100.4 | **100.27** | 3 |
| Fairfax (FFH) | — | — | — | — | — | NOT COMPARABLE (IFRS) | 0 |

† segment basis. ‡ consolidated, including a large personal auto and homeowners book with heavy
catastrophe load (8.4 points in 2025).

**Peers named: 10, of whom 9 supply the metric on the decisive basis.** The industry's other real
competitors for AIG's multinational commercial business — Zurich, Allianz, AXA XL, Tokio Marine, and
Liberty Mutual — are foreign IFRS/J-GAAP filers or a mutual and are **not** in the row; this is the
same limit the CB run carried, and it is named rather than estimated. **It does not make the class
PROVISIONAL here, because the verdict below does not depend on AIG's rank among the missing names: it
depends on AIG's own ten-year series and on its gap to the one closest US-filing multinational
competitor, Chubb, which is in the row.**

**WHAT THE ROW SHOWS:**
- **AIG is 7th of 11 on the reported basis and 7th of 10 on the honest basis — in its five best
  years.** Below the median on both. **4.0 points behind Chubb** on the current-accident-year basis
  (93.50 against 89.50), and **1.2 points behind The Hartford's commercial book**.
- **Against Chubb, the closest competitor in kind (global licensed network, multinational programmes,
  high-net-worth personal lines, US large-account casualty), the gap runs through every component:**
  AYCR ex-CAT 88.3 against 81.9 (2025); **expense ratio 31.1 against 26.6** — a **4.5-point cost
  disadvantage**; ten-year current-accident-year mean **99.65 against 92.3**, a 7.4-point gap.
- **The row's limit, stated [E3-61]:** *"In some businesses, the participants behave like a demented
  Kellogg. In other businesses, they don't … I think you'd have to know the people involved."* The row
  shows position; it cannot show conduct.

### THE [E3-03] CRITERIA, AND THE Q2 TESTS, SCORED
- **(1) Needed or desired — [x] YES.** Compulsory by statute or contract for most of the book.
- **(2) No close substitute — [ ] NO.** For every AIG line there is a listed competitor in the row
  writing the same product, and nine of ten of them wrote it at a lower or similar current-accident-year
  cost in 2021-2025. The global network is real and scarce, but **Chubb owns the same network class and
  runs it 4.0 points cheaper on the honest basis**, so to a multinational buyer AIG has at least one
  close substitute that is better on the filed numbers.
- **(3) Not price-regulated — [x] in the main;** personal lines are rate-filed state by state and in
  Japan; no administered-price programme of the kind Chubb's Rain and Hail carries (AIG sold Crop Risk
  Services in 2023).
- **[E2-58]'s one exception — *"a cost advantage that is both wide and sustainable"* — AIG has the
  reverse:** a general insurance expense ratio of **31.1 (2025), 32.0 (2024), 31.7 (2023)** against
  Chubb's 26.6, Travelers' 28.5 and a row whose best members run in the mid-20s. Global Personal's
  expense ratio is **41.5**.
- **[E2-44] the two-characteristic test — NO on the first half, in the CEO's words**: the market has
  *"transitioned from an extended phase of broad positive pricing into a more selective environment."*
  The 2021-2025 improvement was earned in the rising-price years; the filing shows no evidence of
  price-raising power in a flat market.
- **[E4-37] the agony metric, [E3-33] untapped pricing power, [E5-28] near-monopoly, [E2-53]
  dominance — none claimed, none evidenced.** AIG is a few percent of world commercial P&C premium.
- **[E4-36] which cause of success?** The 2021-2025 record is **wave-riding plus remediation** — the
  hard market (the wave, [E3-51]: *"if he gets off the wave, he becomes mired in shallows"*) and a
  one-time re-underwriting of a bad book. Neither is an extreme on any variable, and **the corpus says
  of the wave: the advantage lives in the wave, not the surfer.**
- **[E2-56] the Pro-Am effect:** the two commercial segments (combined ratios 86.8 and 86.9) camouflage
  a Global Personal segment that has run at **100.1, 98.0 and 99.0** — break-even underwriting on 27%
  of premium, with an expense ratio of 41.5.

### [E4-04], [E4-23] AND [E2-36] — THE MANAGER IS THE PLAN, AND THE MANAGERS ARE LEAVING
**[E4-04]:** *"A moat that must be continuously rebuilt will eventually be no moat at all.
Additionally, this criterion eliminates the business whose success depends on having a great
manager."* **[E4-23]:** *"if a business requires a superstar to produce great results, the business
itself cannot be deemed great."* **[E2-70]** says this industry specifically *"magnifies the effect
which individual managers have on company performance."*

**The filed record is as close to a controlled experiment on that sentence as this project has run:
the same licences, the same brand, the same global network and the same markets produced a
current-accident-year ratio above 100 in five straight years (2016-2020) and below 94 in four of the
next five.** What changed was the underwriting management and the book it chose to write. **That is
[E2-36]'s "corporate Pygmalion" — the turnaround in which "the managers expect — and need — to pull
off" the result — not the "localized excisable cancer" inside an intact franchise [E2-35].** The
franchise was not intact: the core long-tail lines were under-reserved for years (the triangles) and
the pre-2016 reserve risk had to be sold to Berkshire (the ADC).

**And the people who performed it are leaving, on the filed record, in the same four months:**
- **Peter Zaffino** — CEO of the company through the turnaround, then *"Executive Chair"* from early
  2026 — *"will step down as Executive Chair and a member of the Board, effective September 15, 2026"*
  (8-K `0000005272-26-000088`, filed 2026-09-02), becoming a Senior Advisor. The board chair passes to
  the Lead Independent Director, John Rice.
- **Jon Hancock** — *"Executive Vice President and Chief Executive Officer, General Insurance"* — *"will
  retire and transition to the role of Senior Advisor, effective December 31, 2026"* (8-K
  `0000005272-26-000091`, filed 2026-09-16).
- **Eric Andersen** is now *"President & Chief Executive Officer"* (Q2 2026 release). The 8-K of
  2026-01-06 (`0000005272-26-000006`) records the succession: Zaffino *"intends to transition to
  Executive Chair of the Company and retire as CEO by mid-year"*, and Andersen joins *"as President and
  CEO Elect, effective February 16, 2026"*; he *"currently serves as Senior Advisor to the Chief
  Executive Officer of Aon plc and previously served as President of Aon plc from 2020 to 2025."* **The
  new CEO comes from the broker side of the market, not from underwriting** — recorded as a fact, not as
  a judgment on him; the point is only that the record above is not his.

**Under [E4-23], that is the Mayo-Clinic test answered in the negative on the filed record, not left
open as it was at Chubb.** At Chubb the question was whether a 22-year record would survive its author;
the record itself was ten-of-ten. **At AIG the record already shows what the same franchise assets
produced without the turnaround management — five straight years above 100 — and the turnaround
management is leaving.** A moat that depends on the manager is, on the corpus's own criterion, not a
moat.

### [E4-26] — THE STRONGEST CASE AGAINST THIS VERDICT, STATED FIRST AND AT FULL STRENGTH
1. **The last five years are real and they are good.** Current-accident-year below 100 in every year
   2021-2025, mean 93.5; favourable development seven years running on the APTI basis; both commercial
   segments at an 85-86 current-accident-year ex-CAT ratio — **International Commercial's 81.7 to 85.6
   is at Chubb's Overseas General level (84.8)**. Financial strength ratings were upgraded by Fitch, S&P
   and Moody's in 2025.
2. **The five bad years may be the old book, not the old franchise.** 2016-2020 is largely business
   AIG has since exited, re-underwritten or reinsured; the ADC removed most of the pre-2016 tail.
3. **AIG beats four names in the row on the honest basis** (AXS, TRV, MKL, and on four years RLI is
   only 0.4 points better), and Travelers is a widely admired underwriter.
4. **Management's own claim:** *"The breadth of our underwriting expertise and the diversity of our
   global portfolio remain important competitive advantages."*

**Why these do not carry it.** (1) and (3) establish a competent underwriter in a hard market, not a
franchise: in AIG's *best* five years it sits below the middle of the row and 4.0 points behind the
competitor it most resembles, with a 4.5-point cost disadvantage — **a franchise is a relative claim
and the relative evidence is against it even on the favourable window** [E3-28]. (2) is exactly the
[E2-36] argument that the manager is the plan, and the excess-casualty triangles show AY2021-2023 —
the new book — developing adversely by 8% to 38%. (4) is management language; the framework asks for
the evidence, and the evidence is the row.

### THE VERDICT
- Class: **[x] NONE** · Direction: **improving 2021-2025 on the current-accident-year series (96.4 →
  92.2), from a decade mean at break-even; the pricing cycle turning against it by the CEO's own
  statement; the turnaround's two authors leaving by 2026-12-31.**
- **VERDICT: [x] OUT — the evidence is here and the business fails the franchise test.** On the
  corpus's own chosen measure for this class, AIG's current-accident-year underwriting **broke even
  over ten years (mean 99.65) and lost money on the business it wrote in five of them**; its core
  long-tail lines were under-reserved at first estimate by double digits for years, the excess-casualty
  lines still are on post-turnaround accident years, and the pre-2016 reserve risk had to be ceded to
  Berkshire; in its five best years it ranks **7th of 10** on the honest basis, **4.0 points behind
  Chubb with a 4.5-point expense disadvantage** — the reverse of [E2-58]'s one exception; and the
  improvement that exists is a manager-made turnaround in a hard market [E2-36, E3-51] whose authors
  are leaving, which [E4-04] and [E4-23] exclude by name. **This is a verdict about the business, not
  about the price. The file closes here.**
- *"Can I name the document that would resolve this?"* — asked because OUT is permanent and
  [E3-47] rates a wrongly closed file as the expensive error. **No document is outstanding:** the
  ten-year series, the triangles, the ADC note and the row are all in hand. What would *change* the
  verdict is future evidence that does not yet exist (the reversal conditions at Q6), which is not a
  work order.

---
⛔ **THE FILE IS CLOSED AT Q2 — OUT, ON THE BUSINESS.** Q3 and Q4 below are **RECORDED, NOT
GOVERNING**: they were researched because the brief required their evidence and because a later
re-run should not have to repeat it. Nothing below can reopen Q2 (the guardrail: *"a strong Q3 cannot
promote a name, repair Q2, or substitute for Q4"*).

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — RECORDED, NOT GOVERNING
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`.*

### STEP 1 — THE WEIGHT CASE
- [x] **Daily execution [E3-38, E3-43, E2-70]** — thousands of risks priced a day and reserves set by
  judgment; *"their only products are promises"* **magnifies** the manager. **[E2-50]**: *"Where
  'earnings' can be created by the stroke of a pen, the dishonest will gather."*
- [ ] Control — a marketable minority stake; exit is available.
- [x] **Leverage [E3-29]** — investments 2.26x equity, float 1.15x equity, gross reserves $70.7bn
  against $41.1bn of equity: a 5% error in gross reserves is $3.5bn, 8.6% of equity.

**CASE DECLARED: Q3 would be a BINARY GATE, on two of three determinants; no price compensates [E1-16,
E3-29, E5-35].** Recorded for a re-run; it governs nothing here because Q2 closed the file.

### THE BINARY [E5-16] — each matter dated to when it became PUBLIC
- **The present record, read:** FY2025 10-K Item 9A — *"AIG management has concluded that, as of
  December 31, 2025, our internal control over financial reporting was effective"*; PwC's opinion is
  unqualified; Note 15's legal contingencies disclose ordinary coverage and securities litigation, and
  no conduct matter involving a current officer was found in the 10-K, the proxy or any 8-K read. **Per
  [E5-17] this is the absence of found disqualifiers, not a finding that anyone is honest.**
- **The history the brief named — recorded, dated, and NOT scored, with its evidence status stated.**
  The 2008 government rescue and the 2005-2006 accounting restatement are matters of public record
  from those years. **No filing from 2005-2012 was read in this run**, so neither is characterised
  here beyond its existence; a verdict resting on them would be UNRESEARCHED, and the documents that
  would resolve them are the FY2005-FY2012 10-Ks and the 2006 SEC settlement. **They cannot bear on the
  present management in any case**: the CEO (Andersen) joined on 2026-02-16, the board chair (Rice)
  joined the board in March 2022, and the two executives who ran the 2017-2026 turnaround are leaving.
  **The filed record this run DID read carries one thing from that history, and it scores in
  management's favour:** the 2025 Investor Day deck (8-K `0000005272-25-000017`, EX-99.1) prints AIG's
  own underwriting result year by year from 2008 and labels it *"2008 – 2018 $33B underwriting loss"*,
  beside the heading *"Unprecedented Turnaround."* **A management publishing the cumulative size of its
  predecessors' underwriting losses is the [E2-26] candor case**, even though the slide's purpose is to
  flatter the turnaround.

### STEP 2 — THE FLAGS. Each a prompt to READ, never a verdict [E3-68]
**[E4-29] EBITDA — CLEAN, tested the hard way (CGNX rule).** `grep -ic ebitda` returns **0** for the
10-K, the 10-Q, the proxy, all four quarterly EX-99.1 releases and every 8-K pulled. Not fired.

**[E4-22] third flag, [E3-48], [E5-30], [E4-35] — TRUMPETED PROJECTIONS. FIRES, AT FULL STRENGTH.** The
2025 Investor Day set *"PERFORMANCE METRICS 2025 - 2027F"*: **"Operating EPS CAGR 20%+ · Core Operating
ROE 10% - 13% · GI Expense Ratio <30% · Dividends Per Share CAGR 10%+ (2025-2026)"**, and a 2030 slide
projects new-business growth of *"20%+ CAGR"* with technology. **Every quarterly release since repeats
the promise:** Q3 2025 *"We are on track to achieve the financial objectives that we set at Investor
Day"*; Q4 2025 *"We are off to a great start on our Investor Day guidance and are on track to achieve
or even exceed our financial objectives"*; Q1 2026 *"we remain on track to meet or exceed the financial
objectives that we outlined at our Investor Day"*; Q2 2026 *"We remain confident in our ability to meet
our 2025 Investor Day financial objectives."*
- **[E3-48]'s action taken — past guidance against outturn:** 2025 adjusted after-tax income per share
  **+43%** ($4.95 → $7.09) against 20%+; core operating ROE **11.1%** inside 10-13%; **GI expense ratio
  31.1% against "<30%" — not yet met.** **Two of three met, and the one met most spectacularly
  (per-share operating EPS) had help that is not operating:** diluted shares fell **13%** (657.3M →
  570.3M) on $5.8bn of buybacks, the 2024 base was depressed by the travel sale and restructuring, and
  the metric excludes $606M of 2025 restructuring, integration, pension and regulatory costs.
- **[E4-35] bites hard:** *"fewer than 10 of the 200 most profitable companies in 2000 will attain 15%
  annual growth in earnings-per-share over the next 20 years."* **A 20%+ operating-EPS CAGR target is the
  base-rate-defying number [E4-35] names, set by the management of an insurer whose ten-year
  underwriting broke even.** And **[E5-30]**: *"once you start it, it's all over. You can't quit."*

**[E2-57] THE EXCEPT-FOR FLAG and [E3-53] THE RESTRUCTURING CHARGE — FIRES.** "Adjusted pre-tax income"
excludes, **every year**, *"restructuring and other costs related to initiatives designed to reduce
operating expenses"* — **$356M (2023), $745M (2024), $439M (2025): $1.54bn in three years, recurring,
never counted** — plus integration costs ($6M, $39M, $136M), non-operating pension, "non-recurring"
regulatory costs ($22M, $18M, $16M — recurring), realised losses (negative in all three years:
−$734M, −$434M, −$966M excluding Fortitude Re), and **"net results of businesses in run-off"**,
redefined twice: *"In the fourth quarter of 2024, AIG realigned and began excluding the net results of
run-off businesses previously reported in Other Operations … In the third quarter of 2025, AIG began
excluding the net results of run-off businesses previously reported in General Insurance."*
**[E5-33]: *"to tell owners year after year, 'Don't count this' … is misleading."*** Three straight
years of excluded restructuring is the case the row was written for.

**[E2-49] METRIC-SWITCHING — READ, SCORED SMALL.** (a) The run-off exclusion moved twice in a year — it
follows **$112M of adverse development on the Blackboard run-off portfolio in 2024** (Note 13) and removes
a loss line from the headline; disclosed and recast, so [E2-49]'s candor case, but in the flattering
direction. (b) The proxy removed the PSU *"expense management"* metric *"since the expense savings
targets had been largely achieved ahead of schedule"* — dropped **after** a favourable reading, which is
not [E2-49]'s failure mode. Recorded, not fired.

**[E4-27] THE POWER OF INCENTIVES — THE SHARPEST Q3 FINDING.** *"Never, ever, think about something
else when you should be thinking about the power of incentives."* DEF 14A 2026 (`0000005272-26-000039`):
- **2025 short-term plan, four metrics at 25% each:** calendar-year combined ratio (absolute; target
  92.9, actual 90.1 → **150%**), accident-year combined ratio ex-CAT (target 88.0, actual 88.3 → 82%),
  **adjusted after-tax income per diluted share** (target **$5.55**, actual **$7.09** → **150%**), core
  operating ROE (target 9.7%, actual 11.1% → **150%**). Company score **133%**; named executives' STI
  paid at **186% of target** on average.
- **2025 PSUs, five metrics at 20% each:** calendar-year combined ratio relative to *"Business
  Competitors"*, accident-year ratio, **AATI per share growth**, **adjusted tangible book value per share
  growth**, relative TSR. **2023 PSUs vested at 161%.**
- **What the incentives point at:** (i) **per-share adjusted earnings, which buybacks raise whatever
  the price paid** — and AIG bought back 24% of its shares in 31 months; (ii) the **calendar-year**
  combined ratio, which favourable reserve development improves (2.1 points in 2025) and which
  **excludes** the development ceded to NICO; (iii) metrics that all exclude the recurring restructuring
  charges. **The pay plan rewards exactly the three things the flags above found.** [E2-01] names the
  primary test *"not the achievement of consistent gains in earnings per share."*
- **Shareholders noticed:** say-on-pay received **65% support in 2025** (proxy: *"below where we had
  hoped"*) and **77.5% in 2026** (8-K `0000005272-26-000066`: 359.8M for, 104.7M against). CEO
  annualised 2025 pay **$32,460,049; pay ratio 346:1.** Zaffino's 2026 target as Chairman & CEO was
  **$25.0M**; Andersen received a **$12.5M** make-whole RSU award on joining.
- **Counterweights, per [E4-26]:** the accident-year ratio (ex-CAT, ex-PYD) is in both plans and it
  paid only **82%** in 2025 — the one honest-basis metric is the one that under-delivered; relative TSR
  is capped at 100% when TSR is negative (a 2026 change); the combined-ratio PSU is **relative**.

**[E4-52] THE CONVERGENCE TEST.** Trumpeted 20%+ EPS targets + a pay plan paying on adjusted per-share
earnings + three years of excluded "restructuring" + a buyback that mechanically lifts the per-share
metric: **these converge on one outcome — a rising adjusted-EPS line.** That is the shape the row
describes (*"confluences of psychological tendencies acting in favor of a particular outcome"*).
**Scored as a converging set, not a fraud finding** — [E5-38]: people Buffett would trust *"would play
games with any number that came to them"*; the flags read the accounting, not the person.

**[E5-15] serial issuance — NOT FIRED; the opposite.** Shares **861.6M (12/31/20) → 522.9M (7/31/26),
−39%.** **[E2-52] dividends funded by issuance — NOT FIRED.** **[E4-30] fraud tells — NOT FIRED:**
reported results are anything but smooth (net income to common $10.3bn, $10.2bn, $3.6bn, −$1.4bn,
$3.1bn for 2021-25).

### THE PRIMARY TEST [E2-01] — and the perimeter finding bites here
Three years on the continuing perimeter: **ROE 8.6% (2023), −3.2% (2024, the Corebridge
deconsolidation loss), 7.5% (2025); mean 4.3%.** Management's "core operating ROE" (adjusted earnings
over equity excluding AOCI, the deferred tax asset and the Corebridge stake): 9.6%, 9.1%, 11.1%.
**[E2-42]'s red light — *"Red lights should start flashing if the five-year average annual gain falls
much below the return on equity earned over the period by American industry in aggregate"* — is lit on
the GAAP series and dim on management's own.** A five-year series on one perimeter does not exist
(Stage 0(b)); the longer consolidated history includes the life business and is not comparable.

**Book value per share: $76.46 (12/31/20) → $76.44 (12/31/25) — flat over five years**; on the
filer's "adjusted" basis excluding investment AOCI, **$57.01 → $78.02 (+6.5%/yr)**. Both readings are
true and both are shown: the 2020 book was inflated by unrealised gains at near-zero rates, and the 2024
deconsolidation recycled $7.2bn of Corebridge's accumulated losses.

### CAPITAL ALLOCATION [E2-29, E3-58, E3-54, E5-08]
- **[E3-54] retention test, 12/31/20 → 12/31/25:** market capitalisation **$32,620M** (861.6M × $37.86)
  → **$46,043M** (538.2M × $85.55; year-end closes, aggregator, flagged). Net income to common
  2021-25 **$25,820M** less dividends **$5,040M** = retained **$20,780M**. **$0.65 of market value per $1
  retained — FAILS.** And the construction breaks: AIG **distributed $28,434M** (dividends $5,040M +
  buybacks $23,394M) against $25,820M of net income, **110% of earnings**, funded by the Corebridge
  sell-down; the retained dollars and the perimeter moved together, so the test is recorded and
  weighted lightly, in both directions.
- **[E5-08] the two buyback conditions.** (1) Ample funds — **MET**: AIG Parent liquidity sources
  $9.3bn (Item 1), debt-to-total-capital 18.0% at 2025, upgrades by Fitch, S&P and Moody's in 2025.
  (2) **Material discount to conservatively calculated value — NOT SHOWN.** Buybacks averaged **$74.16
  (2024, 1.06x year-end book), $79.45 (2025, 1.04x), $80.00 (H1 2026, 1.03x)** — about book, for a
  business whose ten-year underwriting broke even and whose GAAP ROE averaged 4.3%. At book and a
  ~10% ROE the purchase is roughly value-neutral, not a material discount. **Humility clause [E4-13,
  E5-08]:** *"They also know a whole lot more about them than I do"* — the flag binds position size and
  nothing else. **[E5-25]**: no repurchase condition is published; the authorisation is a dollar amount
  ($7.5bn from 2025-04-01; $2.6bn remaining at 2026-07-31).
- **[E2-30] the institutional imperative:** (2) **projects soak up funds — FIRED**: $2.1bn for 35% of
  Convex, $642M for 9.9% of an asset manager (Onex, restricted from sale until 2029-02-06), a CVC
  partnership (up to $1.5bn contributed to a secondaries platform and up to $2bn allocated to CVC
  mandates), a Lloyd's syndicate with Blackstone and Amwins, and the Everest renewal rights — **all
  announced within roughly ninety days**, and the Q4 2025 release says they *"will contribute to AIG's
  earnings, earnings per share, and ROE in 2026."* **An insurer buying a stake in an asset manager is
  the [E3-40] loss-of-focus vector** — recorded, not concluded. (1), (3), (4): not found.
- **[E4-39] rare-positive tell — PARTLY PRESENT**: the Investor Day deck revisits the turnaround against
  its own history (the $33bn slide, severe-loss reductions, commercial gross limit cut from $2.7T to
  $1.4T). It does not revisit individual deals against their announcement case.

### THE GUARDRAIL
- [x] Nothing in this Q3 promotes the name, and nothing here could: the file closed at Q2.
- [x] Key-person dependence was recorded **at Q2 as a moat defect [E4-23]**, not here.
- [x] [E2-35, E2-36]: **the manager was the plan** (Q2) — a Pygmalion, not an excisable cancer.

- **VERDICT (recorded, NOT governing): would be [x] IN — as a binary gate, meaning only the absence of
  found disqualifiers [E5-17] — CARRYING a converging set of flags [E4-52]:** trumpeted 20%+ EPS targets
  [E4-22, E4-35, E5-30], three years of excluded restructuring [E2-57, E3-53], pay on adjusted per-share
  metrics that buybacks raise [E4-27], and buybacks at book with no stated condition [E5-08](2).
  **Capital-allocation flag LIVE; it would bind position size.**

## Q4 — WILL IT SURVIVE? — RECORDED, NOT GOVERNING

**No owner-earnings number is computed, and the reason is the sector method's own** — *"the answer is
not a better owner-earnings formula. The corpus does not compute one."* The Loews OCF test is not run:
with Q2 closed there is no yield to guard.

### STEP 2 — THE COST OF FLOAT [E3-69]. DIAGNOSTIC, NOT ADDITIVE.
*"A low cost of funds signifies a good business; a high cost translates into a poor business."*
**CONVENTION 4 cannot be built before 2024** (Stage 0(b)), so the ten-year series uses **average net loss
reserves from the Note 13 rollforwards as the float proxy — confessed as a narrower construction (it
omits net unearned premium less receivables and DAC)**; for 2025 the two agree in direction (−5.69% on
the proxy, −5.06% on CONVENTION 4).

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| GI underwriting income $M | −5,605 | −4,481 | −3,137 | +89 | −1,024 | +1,055 | +2,048 | +2,349 | +1,917 | +2,332 |
| **cost of float** | **+9.18%** | **+7.91%** | **+6.05%** | −0.18% | **+2.26%** | −2.42% | −4.71% | −5.65% | −4.78% | −5.69% |

**Ten years: cumulative underwriting LOSS $4,457M; cost of float +0.94% a year — POSITIVE.** Five years
2021-25: −4.63%. **Chubb, on its five: −8.58%. Berkshire (this project's BRK run): −3.6%.** On the
corpus's own chosen measure over *"a period of years"*, AIG's funding **cost** money across the decade
— and the ten-year figure **excludes** the consideration AIG paid NICO in 2017 to take the pre-2016
long-tail risk away, which sits outside the General Insurance ratio (not quantified here from a filing
read). **[E3-69] on the decade: a high cost, a poor business; on the last five: a good one. Which
describes the next five is Q2's question, and Q2 answered it.**

### Q4 SUBSTITUTION 1 — RESERVE ADEQUACY AND NET WORTH, NEVER CASH [E2-61]
Net worth **$41.1bn** (12/31/25), **$40.6bn** (6/30/26). The walking-dead test (*"redouble their efforts
to write business"*): AIG **shrank** premium from $26.7bn (2023) to $23.7bn (2025) by selling
businesses and cutting limits, then grew NPW **9%** in Q2 2026 — *"driven by growth across all three
business segments"* — into the market its CEO calls *"more selective."* **A prompt, not a finding.**
Reserve adequacy: see the triangles at Q2 — conservative in workers' compensation and short-tail,
**deficient at first estimate in excess casualty on post-turnaround accident years.**

### Q4 SUBSTITUTION 2 — RESERVE DEVELOPMENT IS THE CANDOR TEST [E2-67]
Done at Q2. **The filer names the adverse lines every year and publishes the triangles; it does not
publish a single scorecard of its own reserving error, and its headline PYD figure is struck AFTER the
NICO cessions and the deferred-gain amortisation** — 2024 reads *"$367 million"* favourable in the MD&A
text ($368M in the table) on the APTI basis and **$254 million ADVERSE** before the ADC. [E2-67]'s
standard is the scorecard with the bias named; AIG is on the compliance side of it, as Chubb was.

### Q4 SUBSTITUTION 3 — CONCENTRATION IS LICENSED BY LOSS-ABSORPTION [E2-62]
AIG does not concentrate: $71.0bn of AFS bonds against $1.0bn of equity securities at 6/30/26. **It
relies instead on reinsurance at a scale Chubb does not:** reinsurance recoverable on unpaid losses
**$28,871M against $70,666M of gross reserves — 40.9% ceded** — including $2.3bn of Fortitude Re
reserves and the NICO cover guaranteed by Berkshire. **The licence to concentrate is not claimed; the
dependence on reinsurers is named at staying-power strength 3.**

### THE GREAT, THE GOOD AND THE GRUESOME [E4-20, E4-43]
- [ ] great — [x] **good, on the last five years only** — [ ] gruesome.
- Core operating ROE 9-11%; GAAP 4.3% over three years; **on the ten-year underwriting record it was
  closer to gruesome** — *"pays an inadequate interest rate and requires you to keep adding money"* —
  the cost of float was positive and the pre-2016 reserves had to be sold. [E4-43]: *good* passes; the
  classification is **good now, on a short record**.

### STAYING POWER [E5-11], SECTOR-SCOPED
1. **Earnings stream — [x] adequate, not reliable over the decade:** GI underwriting losses in four of
   ten years; APTI positive in each of 2023-2025 ($4.3bn, $4.3bn, $5.3bn).
2. **Liquid assets, re-expressed per [E2-61] — [x] YES:** $71.0bn of AFS bonds and $11.1bn of
   short-term investments against net reserves of $41.8bn; AIG Parent liquidity sources **$9.3bn**.
3. **Near-term cash requirements — [x] YES, with the dependence named [E5-39]:** *"cash is a lot like
   oxygen."* The business model **assumes the annual renewal of a large reinsurance programme** (the
   2026 North America Commercial retention held at $500M with $500M more vertical limit bought, plus
   per-occurrence, aggregate and casualty covers). A reinsurance market that withdrew capacity at a
   renewal would force AIG to retain far more or write far less. **Kindness of strangers, renewed each
   January.**
- **Leverage, named and quantified [E4-16, E3-29]:** long-term debt $9,035M against $41,139M of equity
  (22%); the filer's debt-to-total-capital **18.0%**; interest **$396M** against APTI of $5,344M (13.5x)
  and GAAP pre-tax income of $3,879M (9.8x) — **[E2-54]'s coverage test comfortably met.** [E3-52]:
  $47.2bn of float is covenant-free; $9.0bn of debt is the other animal.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40, E4-51]
**MECHANISM: long-tail casualty reserves develop adversely again (US excess casualty — mass tort and
social inflation — and financial lines), in the same years the price cycle turns.** AIG has lived this
once: **the FY2018 10-K rollforward shows prior-year development of $5,788M ADVERSE in 2016, $1,565M in
2017 and $1,429M in 2018.** Quantified from the filer's own "reasonably possible" sensitivities at
2025-12-31: US Excess Casualty loss-cost trend +5 points **$900M**, tail factor +3.5 points **$1,150M**,
development six months slower **$750M**; US D&O loss cost +10 points **$750M**, six months slower
**$600M**; US workers' compensation tail **$900M**. **Sum $5,050M — 12.3% of equity, 1.3 times 2025 GAAP
pre-tax income, about one year of adjusted pre-tax income.** Add a worldwide 1-in-250 catastrophe year
(**$2,500M net, 4.8% of equity**, the filer's PML) and a 5% fall in the $71.0bn bond portfolio
(**$3.6bn**): **about $11.1bn, 27% of equity. AIG reports a large loss and survives.** **LIKELIHOOD:
[x] a real possibility** — the excess-casualty triangles show AY2021-2023 already developing adversely,
and the CEO has said the broad pricing phase is over. **[E4-40] exposure, not experience:** the modelled
1-in-250 ($2.5bn) is about **2.3x** the 2023-25 mean realised catastrophe charge ($1,065M), so the model
is not flattered by recent luck the way Chubb's was; the reinsurance programme that makes the net figure
small is the dependence named above. **A return event, not a survival event.**
- **VERDICT (recorded, NOT governing): would be [x] IN** on survival. It governs nothing: Q2 closed the
  file.

---
⛔ **Q5 DOES NOT OPEN.** Q2 returned OUT. What follows is headed as the protocol requires.

## Q5 — COMPUTATION — NOT A CLEARANCE
*Operator rule 3: valuation arithmetic produced after a non-IN gate is a computation, carries no entry
language, and ranks nothing. It is recorded because the strongest fact against this run's verdict is a
price fact, and [E4-26] requires that it be stated with its numbers.*

- **Price US$75.33 (2026-09-18, aggregator, FLAGGED) × 522,893,169 = cap US$39,389M.** Book value per
  share $77.39 (6/30/26): **P/B 0.97x**; core operating book $74.43: 1.01x; adjusted tangible book
  $72.18: 1.04x.
- **Pre-tax earnings yields on the cap** (sovereign 5.34%): adjusted pre-tax income 2025 $5,344M →
  **13.6%**; the same less the $606M of restructuring, integration, pension and regulatory costs it
  excludes [E5-33] → **12.0%**; GAAP pre-tax income from continuing operations 2025 $3,879M → **9.8%**;
  three-year GAAP mean $3,539M → **9.0%**.
- **Sector-method component 1** (investments $92,999M + cash $1,274M − debt $9,191M − Fortitude Re funds
  withheld payable $3,038M − policyholder liabilities that are not float $1,737M) = **$80,307M, $153.58 a
  share, gross of float.** **The gross construction is NOT licensed here, by [E5-46]'s own condition** —
  float is free only *"as long as insurance underwriting breaks even"*; AIG's ten-year
  current-accident-year mean is 99.65 and its ten-year cost of float **+0.94%**, so the condition holds
  on five years and fails on ten. **Net of float ($47,239M): $33,068M, $63.24 a share.** Component 2
  (APTI less investment income): $1,109M, $830M, $1,562M (2023-25); **after the excluded
  restructuring, $654M, $28M, $956M.**
- **What this computation shows, stated without entry language:** on adjusted earnings the quote is
  **above** the ~10% floor that quit Chubb [E4-28]; on GAAP it is near it; at 0.97x book it is the
  cheapest insurer this track has computed. **[E5-35] is why none of it reopens anything:** *"You can
  turn any investment into a bad deal by paying too much. What you can't do is turn any investment into
  a good deal by paying little."* And **[E3-29]**, on a leveraged filer whose Q3 is a gate: *"we have
  no interest in purchasing shares of a poorly-managed bank at a 'cheap' price."*
- Windage count: **0** — no margin was applied, because no valuation was performed.
- **VERDICT: NOT REACHED. Ranking position: none.**

## Q6 — WHAT WOULD PROVE ME WRONG? — THE REVERSAL CONDITION, IN WORDS, NO BANDS
**A Q2 failure is a failure on the business; a price alert on it would be a category error (the QLYS
ruling, 2026-09-07). No band is armed and no `PORTFOLIO.md` row is added.** Pre-committed now [E1-02]:
*"I believe in establishing yardsticks prior to the act."*

**THE Q2 VERDICT REVERSES ONLY IF ALL FOUR HOLD, on filed figures:**
1. **The current-accident-year combined ratio including catastrophes stays below 95 in every year
   through a full soft market** — at least FY2026 through FY2028 — **under the new management**
   (Andersen, and whoever succeeds Hancock at General Insurance). *(Falsifies "the manager was the
   plan"; tests [E4-23] directly.)*
2. **AIG's five-year current-accident-year mean moves into the top half of the competitor row** and
   closes at least half of its 4.0-point gap to Chubb. *(Falsifies "no relative advantage.")*
3. **The US Excess Casualty triangle stops developing adversely on accident years 2021 and later** —
   no accident year from 2021 on more than 5% above its first estimate at the FY2028 10-K. *(Falsifies
   "the new book is under-reserved too.")*
4. **The GI expense ratio falls below 29%** — the Investor Day's own "<30%" plus a point — without the
   exclusion of recurring restructuring. *(Falsifies "a cost disadvantage, the reverse of [E2-58]'s
   exception.")*

None can be satisfied before the FY2027 10-K (~February 2028). **Next catalyst dates:** the Q3 2026
earnings 8-K (~early November 2026), the first quarter reported with Zaffino gone; the FY2026 10-K
(~February 2027), the first with Hancock's successor named and the first full year of the "more
selective" market.

**The sell rule [E2-28]** — not applicable: no position is held or proposed. Holdings are governed by
`Framework/THE HOLDINGS FRAMEWORK.md`. **No PERMANENT designation [E2-39].**

- **VERDICT: [x] IN** as a monitoring surface. Nothing is armed.

---
## SELF-AUDIT
- [x] **Questions answered in order; stopped at the first verdict that is not IN (Q2, OUT).** Q3 and Q4
      are headed RECORDED, NOT GOVERNING; Q5 is headed COMPUTATION — NOT A CLEARANCE and carries no entry
      language; no Q5 output is reported as a verdict.
- [x] **No question marked IN carries an "unverified", "general knowledge" or "provisional" caveat.**
      The one general-knowledge matter in the file (the 2005-2008 history) is labelled as such, is
      explicitly **not scored**, and sits under a Q3 that governs nothing.
- [x] No UNRESEARCHED or UNKNOWABLE verdict is returned. The OUT was put to the separating question in
      writing; no document is outstanding.
- [x] **Step 0: the filing was read (MD&A, cash-flow statement, footnotes including all ten triangles),
      with accession numbers; five figures cross-checked** — equity from A−L at two dates, BVPS, the
      decisive series re-added in all ten years, underwriting income and APTI built from dollars, and
      the cover count against issued-less-treasury.
- [x] **Sector method applied:** Stage 0(a) count by hand off the cover with the issued/outstanding trap
      tested; Stage 0(b) states both ratios (50.8%, 2.26x) and what they imply; step 2 diagnostic,
      nothing added; gross-versus-net answered with [E5-46]'s own condition. **Owner earnings not
      computed, per the method.**
- [x] **More than one window shown** wherever numbers were computed (ten-year and five-year on the
      decisive series and on the cost of float; four constructions at Q5).
- [x] **Competitor row extended from CB, not rebuilt; 15 of 15 carried accessions re-resolved; TRV and HIG
      added with their own accessions; 9 of 10 peers on the decisive basis;** the missing foreign
      multinationals named, and the reason the class is not PROVISIONAL stated.
- [x] **Sovereign for the earnings currency, from the issuing authority, dated** (US Treasury 30-year,
      5.34%, 2026-09-18), **with the multi-currency gap disclosed as unresolved per FINDING 8** (52.6% of
      revenue international) and the direction of the error stated.
- [x] No value range stated, because no valuation was performed; windage count 0.
- [x] Prices dated; the aggregator used for quotes only and flagged.
- [x] **[E4-26] applied against the favourite hypothesis in writing** at Q2 (four counter-arguments, each
      answered) and in the register below.
- [x] Every ledger id cited checked against `principle_ledger.csv` (`check_ids.py`: 0 missing).
- [x] `python tools/check_framework.py` — run before the commit.
- [x] Run committed to git with a pathspec.
- **Process note, recorded rather than smoothed:** during this run, stripped copies of AIG's FY2017,
  FY2019 and FY2024 10-Ks, and fresh copies of the FY2021 and FY2023 10-Ks, appeared in this run's
  research folder, written by a process other than this run (file times 15:37-15:40 on 2026-09-19).
  They are the same EDGAR documents; none was relied on except as this run fetched it, and none is
  committed (stripped filings are re-fetchable; see `.gitignore`).

## REGISTER
- **Verdict: [x] OUT — about the business. Closed at Q2.** Q1 IN · **Q2 OUT** · Q3 recorded (would be IN
  as a gate, converging flags, capital-allocation flag live) · Q4 recorded (would be IN) · Q5 computation
  only · Q6 reversal conditions in words.
- **One line:** *On the MKL/CB test AIG's current-accident-year combined ratio including catastrophes was
  **above 100 in five of the last ten years** (100.4, 113.2, 110.2, 100.8, 104.4 for 2016-2020),
  **ten-year mean 99.65 against Chubb's 92.3**, ten-year cost of float **+0.94%**; the 2021-25 turnaround
  is real (mean 93.5) but ranks **7th of 10** on the honest basis, **4.0 points behind Chubb with a
  4.5-point expense disadvantage**; its excess-casualty accident years 2021-23 are already developing
  adversely; the pre-2016 long-tail risk sits with Berkshire under the NICO cover ($32.6bn paid against a
  $25bn attachment); and the two executives who made the turnaround leave by 2026-12-31 — a manager-made
  result in a hard market [E2-36, E3-51, E4-23], so OUT on the franchise, not on the price.*
- **THE STRONGEST SINGLE FACT AGAINST MY CONCLUSION:** **at US$75.33 AIG trades at 0.97x book and 12.0%
  pre-tax on its 2025 adjusted earnings even after putting the excluded restructuring back — above the
  ~10% floor that quit Chubb — and its last five years of underwriting were all profitable on the
  current accident year, with International Commercial running at Chubb's Overseas General level.** If
  the 2016-2020 record describes a book AIG no longer writes, and the new management holds the
  2021-2025 discipline through the soft market, this run has closed on the past a business whose present
  is sound and whose price is low — **[E3-47]'s error of omission, the one the corpus rates most
  expensive.** The reversal conditions at Q6 are written to catch exactly that.
- **Not UNRESEARCHED and not UNKNOWABLE.** No document was named and not fetched.

---
## ADDENDUM 2026-09-19 (same session, after the fold commit `4ed4627`) — THE REPLICATION, TWO CORRECTIONS, THREE ADDITIONS
*Operator rule 6: violations found later are corrected in an addendum, never by editing history. Nothing
above this line has been changed.*

**Who wrote into the research folder.** The process note in the self-audit recorded an unidentified
writer. It is now identified: commit `c7132f3` records that **an unattended overnight cycle dispatched a
second agent on AIG** after deleting a lock it did not hold. That agent found this file committed through
Q2, refused to write to it, and left `Test Runs/_research 2026-09-19 AIG/REPLICATION - independent second
run, findings owed to the AIG fold.md`. **It independently reproduced every core figure in this file** —
the cover count 522,893,169, cap $39,389M, equity $41,139M from A−L, the ten-year series (100.4 … 92.2,
mean 99.65), float $47,239M, 50.8% and 2.26x, cumulative underwriting −$4,457M, cost of float +0.94% ten-year
and −4.63% five-year, and the $0.65 retention result. **Two independent constructions agree to the
dollar and to the tenth of a point.** Its eight findings were checked against the filings before any is
carried here; each is marked with what this session verified.

### CORRECTION 1 — [E4-30] WAS SCORED ON ONE HALF. THE CASH-TAX HALF FIRES.
Q3 above scored the fraud tells "NOT FIRED" on smoothness alone and did not compute the second half,
*"cash taxes falling as a share of reported pretax income."* **Verified in the FY2025 10-K cash-flow
supplement ("Cash paid during the period for: … Taxes | $330 | $708 | $984"):** against income from
continuing operations before tax of $2,867M, $3,870M and $3,879M, cash taxes ran **34.3% (2023) → 18.3%
(2024) → 8.5% (2025)**, with a **$229M US federal refund** in 2025 (Note 21 table). **Caveat stated:** the
2023 and part-2024 cash figures are consolidated and include Corebridge until 2024-06-09, so the first two
ratios are overstated against a continuing-operations denominator; the 2025 figure is clean. **The
filing's explanation is disclosed:** Note 21's valuation-allowance release on US federal loss and credit
carryforwards, i.e. the tax attributes being used. **Scored as the flag instructs — fired, read,
explained — and it joins the [E4-52] converging set at small weight**, because the same deferred tax
asset is removed from "core operating" equity, which lifts the headline core ROE the pay plan uses.
**The Q3 recorded verdict is unchanged.**

### CORRECTION 2 — THE Q4 SENSITIVITY SUM ADDED ALTERNATIVES WITHIN ONE LINE
Q4 above summed **$5,050M** by adding, for US Excess Casualty, three alternative assumption shocks (loss
cost, tail factor, development speed) and, for D&O, two. The filer presents them as alternatives, and the
CB run summed **one deviation per line**. **Like-for-like with Chubb, the largest deviation per line:**
Excess Casualty tail $1,150M + D&O $750M + workers' compensation tail $900M = **$2,800M — 6.8% of equity
and 52% of 2025 adjusted pre-tax income, against Chubb's $2,764M, 3.7% and 23%**: about the same dollar
exposure on a balance sheet 56% the size and earnings 45% the size. The combined stress becomes $2.8bn +
$2.5bn catastrophe + $3.6bn bond drawdown ≈ **$8.9bn, 21.6% of equity. Survivable; the recorded Q4
verdict and the death named are unchanged.** The register entry in `Screens/WATCHLIST RUN QUEUE.md`
carried the $5.05bn figure and has a dated note beside it.

### ADDITION 1 — AN ELEVENTH YEAR
FY2017 10-K (`0000005272-18-000022`, the replication's fetch; the three components were re-read here):
2015 General Insurance combined ratio **110.1**, catastrophes **2.4** points, prior-year development
**10.7 points adverse** → current-accident-year combined ratio including catastrophes **99.4**. Eleven
years 2015-2025: above 100 in five, mean **99.6**. **Strengthens the Q2 record; changes nothing.**

### ADDITION 2 — A CANDOR INCONSISTENCY, PROXY AGAINST 10-K [E2-26]
DEF 14A `0000005272-26-000039`, the board's opening letter (line 38 of the stripped text): *"For the
first time since 2008, we generated more than $2 billion in underwriting income, and delivered Net income
per diluted share of $5."* **AIG's own 10-Ks report General Insurance underwriting income of $2,048M
(2022) and $2,349M (2023)**, both above $2bn. Read as a conjoined claim with the per-share figure it may
be defensible; read as the underwriting sentence it is plainly worded, it is wrong on the filer's own
numbers. **A small thing, recorded as a prompt: [E2-26] asks whether the reporting tells owners what
they would want to know, and a flattering "first time since 2008" in the proxy's first page is the
direction to watch.**

### ADDITION 3 — THE REST OF THE REPLICATION, CARRIED WITH ITS STATUS
- **Component 2 almost nothing** — pre-tax income less all investment income and realised losses:
  $499M, $163M, $866M (2023-25) against Chubb's $5,359M. Consistent with this run's own $654M, $28M, $956M
  after restructuring. **The valuation's centre of gravity is component 1**, the WTM finding mirrored.
- **Below-gate floor computation, keeping restructuring:** 8.54%, 9.43%, 7.82%, 11.65% (2022-25), mean
  **9.36%** — the replication's figures, not re-derived here; they bracket this run's GAAP 9.0-9.8%.
  **COMPUTATION — NOT A CLEARANCE.**
- **Restructuring excluded from adjusted income in every year read:** the FY2023 10-K shows pre-tax
  "Restructuring and other costs" of **$433M (2021), $570M (2022), $553M (2023)** on the consolidated
  basis then reported; the FY2025 10-K recasts 2023 to **$356M** on the continuing basis. (The
  replication's "$423M" for one year was not found in the documents read here; this session's figures
  are the ones above.) Five consecutive years excluded: [E3-53], [E5-33].
- **Sector-method gap, sharpened by the replication:** NICO's share of the covered book is 80% of paid
  losses above the $25bn attachment — **80% × ($32,588M − $25,000M) = $6,070M paid plus 80% × $8,907M =
  $7,126M still open, about $13.2bn in all** — against the filed *"aggregate limit of $25 billion."*
  **CONVENTION 4 nets that recoverable, so it prices Berkshire's credit as AIG's funding.** Recorded for
  the operator beside this run's own "retroactive reinsurance has no rule".

**Net effect on the verdict: none. Q2 OUT stands; the corrections move two recorded, non-governing
figures, and the additions strengthen the record Q2 rests on.**
