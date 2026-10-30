import io
p = "Test Runs/2026-09-21 Run - IIIN Insteel Industries.md"
t = io.open(p, encoding='utf-8').read()
lines = t.split('\n')
i0 = next(i for i, l in enumerate(lines) if l.startswith('## Q3 — ARE THEY HONEST'))
i1 = next(i for i, l in enumerate(lines) if l.startswith('## SELF-AUDIT'))
head = '\n'.join(lines[:i0])
rest = '\n'.join(lines[i1:])
new = r'''## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
### ⛔ NOTES BENEATH THE CLOSE. NO VERDICT IS TICKED. The file closed at Q2.
*Recorded because the work was done before the Q2 verdict was written, because operator rule 2
permits notes below a close, and because these facts bear on the reversal condition at the end.*

**THE WEIGHT CASE, declared** *(a note, not a gate, since the file is closed)*:
- [x] **Daily execution [E3-38]** — **ticked.** The product is undifferentiated by the filing's
  own account and the year's result is made by rod-buying timing, inventory positioning and the
  willingness to push price. FY2022 is the proof: **inventories absorbed $118.6 million of cash**
  and FY2023 released **$97.6 million** of it, a $216 million swing on management's positioning
  in a company with a $574M market value. That is have-to-be-smart-every-day.
- [ ] Control [E1-16] — no, a marketable minority stake.
- [ ] Leverage [E3-29] — no. **Total debt $0** at FY2025 and at 2026-06-27; the FY2025 MD&A's own
  table reads *"Total debt - "* and *"Shareholders' equity … 100 %"* of total capital.
- **Had the file remained open, one box ticked makes Q3 a binary gate and no price compensates.**

**Honesty — no disqualifier found in the documents read.** *Written as [E5-17] requires:*
**a Q3 pass is the absence of found disqualifiers, not a finding that the managers are honest.**
Legal proceedings are boilerplate ordinary-course; auditor Grant Thornton LLP, *"has served as
our auditor since its appointment in 2002"* (DEF 14A 2026), so no auditor churn. No restatement
appears in the filings read.

**THE FLAGS [E4-22, E5-15, E4-29, E4-30] — each checked, most clean, and the clean reads matter
because they were taken in the place the CGNX run proved they must be taken.**

- [ ] **weak accounting** — one item to record rather than to score: the FY2025 10-K states
  *"We have reviewed our accounting estimates, and none were deemed to be considered critical
  for the accounting periods presented."* A filer declaring **no** critical accounting estimate
  is an absence claim inside a filing. On this business it is plausible — no reserves, no
  percentage-of-completion, no pension asset-return assumption driving income — but it is
  recorded as an oddity, not waved through.
- [ ] unintelligible footnotes — no. Twenty notes, plain English, tables that foot.
- [ ] **trumpeted earnings projections / growth targets — DOES NOT FIRE, and it was checked in
  the 8-K EX-99.1 releases, not only in the annual report.** Four quarterly releases read
  (2025-10-16, 2026-01-15, 2026-04-16, 2026-07-16). **No numeric earnings, EPS, margin or
  growth guidance appears in any of them.** The only forward number of any kind is capital
  spending, and the one revision to it is explained as timing: *"The revised outlook reflects
  the timing of certain projects rather than any change in our planned investment activities,
  with a portion of the related expenditures now expected to be incurred in fiscal 2027."*
  The outlook language is adjectival — *"cautiously optimistic"*, *"Favorable outlook for the
  remainder of fiscal 2026"* — which **[E5-30]** does not reach; the ratchet it warns about is
  forecasting earnings, and no earnings are forecast.
- [ ] **serial share issuance [E5-15]** — does not fire. Shares issued and outstanding ran
  **17,609k (FY2011) → 19,420k (FY2025)**, about **+0.7% a year**, all of it option and RSU
  settlement; the cash raised from option exercises across the whole 17-year series never
  exceeded $5.1 million in a year and was **$62 thousand** in FY2025. Nothing here resembles
  *"one of the surest indicators of a promotion-minded management."*
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] — CLEAN, and this is a real finding rather
  than an absence of looking.** The string *"EBITDA"* appears **zero times** in the FY2025 10-K,
  **zero times** in the Q3 FY2026 10-Q, **zero times** in the 2026 proxy, and **zero times in
  any of the six 8-K exhibits read**, as do *"non-GAAP"* and *"adjusted earnings"*. The company's
  public narrative is built on GAAP net earnings, GAAP diluted EPS and return on capital. Under
  **[E5-41]** — depreciation as *"reverse float"*, the expense already paid being exactly the one
  EBITDA deletes — a capital-intensive filer that never reaches for it is making the honest
  choice at the point where the temptation is largest.
- [ ] **filed-figure tells [E4-30]** — neither fires. *Unnaturally smooth growth*: the opposite;
  net earnings ran −22.1, 0.5, −0.4, 1.8, 11.7, 16.6, 21.7, 37.2, 22.6, 36.3, 5.6, 19.0, 66.6,
  125.0, 32.4, 19.3, 41.0 ($M, FY2009–FY2025). *Cash taxes as a share of reported pretax income*:
  45.0%, n/m, 6.5%, 14.8%, 31.3%, 23.7%, 34.1%, 27.2%, 18.2%, 23.4%, 7.9%, 19.5%, 25.7%, 18.8%,
  13.2%, 20.0% — noisy with the cycle and with no downward drift, and **the two best years paid
  19.5% and 25.7%**, which is the wrong direction for the tell.
- **[E2-49] metric-switching — MY OWN PRIOR WAS TESTED AND DID NOT FIRE. The count is
  UNCHANGED at six fires and six failures; IIIN is not a seventh fire.** *"Yardsticks seldom are
  discarded while yielding favorable readings. But when results deteriorate, most managers favor
  disposition of the yardstick rather than disposition of the manager"* — demand *"pre-set,
  long-lived and small bullseyes"* **[E2-49]**. Insteel's annual incentive has been **return on
  capital, and only return on capital, for at least fifteen consecutive years**, and the 2026
  proxy prints the whole series including the years it paid nothing: *"we do not apply subjective
  factors to adjust compensation during periods where our failure to meet our return on capital
  targets may be due to factors outside the control of our executive officers"*, with payouts of
  **0.0% in 2011, 0.0% in 2012, 0.0% in 2019 and 29.0% in 2024**. **Publishing your own worst
  readings in a table is the [E2-67] positive pole** — Berkshire published its reserving errors
  *"so you can … judge whether we may have some systemic bias"* — transposed to a compensation
  disclosure. The CEO's own non-equity incentive fell from **$1,500,000 (FY2025, 200% of target)
  to $204,673 (FY2024, 29% of target)** and back; the pay moved with the number.

**THE PRIMARY TEST [E2-01] — a number, multi-year, balance sheet before income statement.**
Net income ÷ year-end shareholders' equity, FY2010–FY2025, **unlevered because there is no
leverage**: 0.3, −0.3, 1.2, 7.3, 9.3, 10.8, 16.6, 10.1, 15.0, 2.3, 7.2, 22.1, 32.1, 8.5, 5.5,
11.0 — **sixteen-year mean 9.9%**. The company's own ROCICP series (NOPAT ÷ invested capital)
means **14.2% over fifteen years and 9.9% over the thirteen years excluding the 2021-22 spike**.
**[E2-42]**'s red light — *"Red lights should start flashing if the five-year average annual gain
falls much below the return on equity earned over the period by American industry in
aggregate"* — is the test this series should be read against, and it is recorded here without a
verdict because the file is closed.

**The half-owner test [E2-26] — this reporting mostly passes, and the sharpest instance is an
admission against interest.** On the acquisition the 10-K says: *"Following the EWP Acquisition,
net sales of the former EWP facilities in 2025 were approximately $ 59.3 million. The actual net
sales specifically attributable to the EWP Acquisition, however, cannot be quantified due to our
integration efforts … we have determined that the presentation of EWP's earnings is impracticable
for 2025."* It then **publishes the pro forma anyway**, and the pro forma is unflattering:
FY2024 combined **net earnings $17,510 thousand against the $19,305 thousand actually reported**
— **the acquired business, at FY2024 industry conditions, would have REDUCED earnings by $1.8
million on $93.3 million of additional sales.** Restructuring is quantified by category
(separation $251k, relocation $340k, closure $492k, impairment $895k) rather than buried, which
is what **[E5-33]** asks for and **[E3-53]** warns about.

**THE INSTITUTIONAL IMPERATIVE [E2-30] — one of four observable, and it is not a fraud test.**
- [ ] resists any change in current direction — no; it has closed plants and redeployed equipment.
- [x] **projects or acquisitions materialise to soak up available funds** — the shape is present.
  Cash peaked at **$125.7M (FY2022) → $111.5M (FY2024) → $38.6M (FY2025)** and was spent on
  **$72.1M of acquisitions plus a $48.6M special dividend the year before and a $19.4M special
  dividend the year after.** Recorded as [E2-30]'s *"Institutional dynamics, not venality or
  stupidity"*, not as an accusation — a cash pile in a cyclical with no debt is exactly the
  condition the passage describes.
- [ ] staff studies to justify the leader's craving — nothing in the filings.
- [ ] peer behaviour mindlessly imitated — nothing in the filings; the consolidation is
  idiosyncratic rather than industry-wide in the documents read.

**CAPITAL ALLOCATION — recorded, with the humility clause [E4-13] attached.**
- **Buyback condition (1), ample funds [E5-08]:** met — no debt, $98.7M of the $100M revolver
  available at FY2025 year end.
- **Buyback condition (2), a material discount to conservatively calculated IV:** **not
  evidenced either way.** Repurchases are token and continuous — $2.3M (FY2023), $1.8M (FY2024),
  $2.3M (FY2025) against dividends of $41.3M, $50.9M and $21.8M — and no filing states a
  value test. **[E2-51]**'s *"A manager who consistently turns his back on repurchases … reveals
  more than he knows of his motivations"* does not cleanly apply, because the cash is returned,
  just through dividends. **[E5-31]**'s ordering test — business needs first, then acquisitions
  versus repurchases **by per-share value added at the price** — is the one the record cannot
  answer from the filings, and that is a limit, not a finding. **The humility clause [E4-13]:**
  *"it is natural for CEOs to be optimistic about their own businesses. They also know a whole
  lot more about them than I do."*
- **The retention test [E3-54] — BOTH WINDOWS PUBLISHED, because [E4-38] forbids choosing one.**
  *"growth-rate presentations can be significantly distorted by a calculated selection of either
  initial or terminal dates"* **[E4-38]**.

  | window | retained (NI − dividends) | market value, start → end | $ of market value per $1 retained |
  |---|---|---|---|
  | **FY2021–FY2025**, to the FY2025 year-end close | $98.0M | $366.7M → $747.5M | **$3.89 — passes** |
  | **FY2021–FY2025**, to 2026-09-18 | $98.0M | $366.7M → $574.2M | **$2.12 — passes** |
  | **FY2017–FY2025 (nine years)**, to the FY2025 close | $129.4M | $687.7M → $747.5M | **$0.46 — fails** |
  | **FY2017–FY2025 (nine years)**, to 2026-09-18 | $129.4M | $687.7M → $574.2M | **−$0.88 — fails** |

  **The corpus's own test is five-year rolling, and on that window it passes.** The five-year
  window begins at the **October 2020 trough** and the nine-year window begins at a **2016
  peak**, which is precisely the artifact [E4-38] names. The honest statement is that **the
  retention test on this name measures the steel cycle more than it measures the allocator**,
  and both numbers are printed so that nobody has to take my word for which window I preferred.
- **Tenure, and what it implies [E3-58]:** *"Mr. Woltz has served as our Chief Executive Officer
  since 1991 and as Chairman of the Board since 2009"* (DEF 14A 2026). **Thirty-five years.**
  [E3-58]'s arithmetic — a CEO of long tenure has allocated an enormous share of all the capital
  the business has ever had — applies at close to its maximum here. Against it: allocation is
  visibly **not** outsourced; there is no serial banker-led M&A programme (two deals in
  seventeen years of filings) and no consultant-driven capital programme in the documents read.
- **The one allocation fact that deserves to be written plainly, without an accusation
  attached.** The $67.0M EWP purchase bought two production facilities, **Upper Sandusky, Ohio
  and Warren, Ohio.** Warren was closed in **November 2024, within weeks of closing the deal**
  (*"Production at the Warren facility ceased in November 2024"*, $2.3M of FY2025 restructuring,
  the building sold at a $0.5M impairment). Upper Sandusky's closure was announced on
  **2026-08-21**, twenty-two months after purchase, with *"restructuring charges of approximately
  $4.6 million"* and *"the elimination of up to 65 positions"*. **Both acquired plants closed
  within two years.** The stated logic is coherent and is in the release — the remaining WWR
  plants *"have ample open capacity to accommodate additional volumes"* and *"We do not expect
  this action to affect the Company's revenue"* — which is buying volume and killing the
  capacity, a rational consolidation move. **It is also, in the same sentence, the company's own
  testimony that its industry has ample open capacity**, which is [E2-58]'s *"persistent
  over-capacity"* stated by the subject.
- **[E5-33] applies to the charges:** *"to tell owners year after year, 'Don't count this' … is
  misleading."* The FY2025 $2.3M and the FY2026 $4.6M are real costs of owning this business and
  are inside the owner-earnings series below by construction, not annualized away.

**THE GUARDRAIL — checked.**
- [x] Confirmed: nothing in this Q3 is used to promote the name. It could not be: **the file
  closed at Q2, and [E2-37]/[E2-38]/[E3-39] say a good jockey does not repair the horse.** *"a
  textile company that allocates capital brilliantly within its industry is a remarkable textile
  company — but not a remarkable business"* **[E2-37]**. That sentence is the whole of this Q3.
- [x] Key-person dependence is recorded at **Q2 as a moat question, not here as a strength**
  **[E4-23]** — and the Q2 finding was that this business does not need a superstar, it needs a
  steel cycle.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE — NO VERDICT. THE FILE CLOSED AT
  Q2 AND TICKING A BOX HERE WOULD BREACH OPERATOR RULE 2.**

## Q4 — WILL IT SURVIVE?
### ⛔ NOTES BENEATH THE CLOSE. NO VERDICT IS TICKED.

# COMPUTATION — NOT A CLEARANCE

*Everything from here to the end of the file is arithmetic produced after a closed gate. It
carries no entry language and no verdict, per operator rule 3.*

### The owner-earnings rebuild, over EVERY filed year — what the five-year window hides

**Construction (the confessed CONVENTION, section VI):** owner earnings = operating cash flow
− stock-based compensation − the (c) guess, with the working-capital increment already netted
inside operating cash flow as **[E2-23]** constraint 3 requires. Two ends for (c): **D&A**, which
is the corpus default **[E3-44, E2-41]**, and **total capital expenditure**. No net-income proxy
is used anywhere (operator rule 5; PRIME RULE 3's clause of 2026-09-20).

| FY | OCF | SBC | D&A | capex | **OE (c)=D&A** | **OE (c)=capex** |
|---|---|---|---|---|---|---|
| 2010 | 12.88 | 2.26 | 7.00 | 1.49 | **3.62** | **9.13** |
| 2011 | −2.91 | 2.92 | 9.57 | 7.94 | **−15.40** | **−13.76** |
| 2012 | 13.14 | 2.21 | 9.76 | 8.07 | **1.17** | **2.87** |
| 2013 | 36.83 | 2.16 | 9.83 | 5.03 | **24.83** | **29.64** |
| 2014 | 29.23 | 2.66 | 10.27 | 8.96 | **16.30** | **17.62** |
| 2015 | 35.77 | 2.30 | 11.93 | 7.15 | **21.54** | **26.32** |
| 2016 | 56.25 | 2.44 | 11.54 | 12.98 | **42.27** | **40.84** |
| 2017 | 20.84 | 2.25 | 11.65 | 20.57 | **6.95** | **−1.98** |
| 2018 | 53.97 | 2.08 | 12.82 | 18.45 | **39.07** | **33.44** |
| 2019 | 6.61 | 2.06 | 13.55 | 10.51 | **−9.00** | **−5.96** |
| 2020 | 56.22 | 2.03 | 14.26 | 7.11 | **39.94** | **47.08** |
| 2021 | 69.88 | 1.99 | 14.52 | 17.50 | **53.37** | **50.39** |
| 2022 | 5.67 | 2.43 | 14.49 | 15.90 | **−11.25** | **−12.66** |
| 2023 | 142.20 | 2.42 | 13.30 | 30.70 | **126.47** | **109.07** |
| 2024 | 58.21 | 3.07 | 15.41 | 19.15 | **39.72** | **35.99** |
| 2025 | 27.16 | 3.49 | 18.39 | 8.21 | **5.28** | **15.46** |

*(FY2009 is excluded from the means: its D&A does not resolve undimensioned in companyfacts, so
only one end could be computed. Stated rather than filled in.)*

**THE WINDOWS, ALL OF THEM PUBLISHED [E4-25, E4-38]:**

| window | OE, (c)=D&A | OE, (c)=capex |
|---|---|---|
| **3 years, FY2023–25** | **$57.2M** | **$53.5M** |
| **5 years, FY2021–25** *(the corpus default [E2-42])* | **$42.7M** | **$39.7M** |
| **9 years, FY2017–25** | **$32.3M** | **$30.1M** |
| **16 years, FY2010–25 — every filed year the data supports** | **$24.1M** | **$24.0M** |
| **TTM to 2026-06-27** *(FY2025 less 9M FY2025 plus 9M FY2026)* | **−$20.5M** | **−$13.3M** |

- **Short-window mean** (window: 5 years, FY2021–25): **$39.7M–$42.7M**
- **Long-window mean** (window: 16 years, FY2010–25): **$24.0M–$24.1M**
- **Spread, conservative end:** the long window is **44% below** the five-year window, and the
  three-year window is **2.4×** the sixteen-year one.
- **Combined range** (window spread × capex band): **−$20.5M to $57.2M.**
- **Is that range too wide to reach a conclusion? YES, and [E4-25] says that IS the conclusion.**
  *"Usually, the range must be so wide that no useful conclusion can be reached."* A band running
  from **negative twenty** to **plus fifty-seven** on a $574M market value cannot rank anything.
  **This is a second, independent ground on which the file does not proceed** — and it was
  reached from the filings, not from the screen.
- **The distorted year, named [E5-11, E4-41]: FY2023, and it is not a small distortion.**
  **FY2023 alone is 59.2% of the five-year window's total owner earnings at the D&A end.** And
  **FY2023's cash was not earnings**: the filed cash-flow statement shows working capital
  *providing* **$97.6M** of the year's $142.2M of operating cash — **68.6%** — of which
  **$94.3M was the inventory line alone**, unwinding the $118.6M build of FY2022 as steel prices
  fell. Strip the working-capital swing and FY2023's owner earnings are **about $29M, not
  $126M**. **[E4-41]** requires exactly this: *"normalize the mean DOWN for luck"*, favourable
  exogenous breaks *"named and removed before the mean is trusted."* The break here is the
  2021-22 steel spike and its unwind, and it is the whole of the short window's advantage.
- **The step-up the screen reported is real and it is a wave, not a level.** On the nine-year
  operating-cash series the recent three years mean **$75.9M** against the earlier six's
  **$35.5M**, a ratio of **2.13** — which reproduces the screen's figure exactly. The sixteen-year
  owner-earnings series says what that ratio is made of: **[E3-51]**'s surfer.

### Maintenance capex — a DISCLOSED JUDGMENT, and the corpus default holds here

**(c) "must be a guess"** **[E2-09]**. **The guess, stated:** **~$15–18M a year**, i.e. at the
**D&A end**, and here is the reasoning rather than a computation.
- **[E3-44]**'s default — *"by and large, the depreciation charge is not inappropriate in most
  companies to use as a proxy for required capital expenditures"* — and **[E2-41]**'s *"At 95% of
  American businesses, capital expenditures that over time roughly approximate depreciation are a
  necessity."* **Insteel is visibly inside the 95%: over FY2010–FY2025 D&A averaged $12.39M and
  capital expenditure averaged $12.48M, a ratio of 1.01.** Sixteen years of the two lines
  matching to one per cent is as clean a case for the default as the corpus's own wording asks
  for, and it is why the two owner-earnings ends converge on the long window ($24.1M vs $24.0M)
  and diverge only on short ones.
- **[E5-20]**'s exception class — railroads, airlines, anything whose own filing says depreciation
  understates renewal — **is argued by the filing but refuted by the series.** The 10-K's risk
  factors do say *"Our operations are capital intensive and require substantial recurring
  expenditures for the routine maintenance of our equipment and facilities"*, and FY2026 capital
  spending is guided *"up to approximately $20.0 million"* against FY2025 D&A of $18.4M. But the
  same MD&A says the spending is **not** all renewal — *"Capital expenditures for both years
  focused on cost and productivity improvement initiatives in addition to recurring maintenance
  requirements"* — and, decisively, *"Our investing activities are largely discretionary,
  providing us with the ability to significantly curtail outlays should future business
  conditions warrant"*, which is the opposite of a railroad's position. **So the D&A end is valid
  here, and it is the conservative end in the recent years** (FY2025: D&A $18.4M against capex
  $8.2M).
- **[E4-47]**, the inflation conditioner, is noted and not spent twice: replacement cost of
  wire-drawing and welding equipment in current dollars runs ahead of depreciation charged on
  older dollars, which argues the true (c) sits at the **upper** end of $15–18M rather than the
  lower. That judgment is applied once, inside the guess, and not again as a margin.
- **Stock compensation subtracted in full [E5-06]:** yes, every year, at the cash-flow add-back.
  **[E3-70]**'s stricter market-value measure is not reached for: SBC is **$3.49M on $27.2M of
  operating cash** in FY2025 and averages **$2.4M a year**, and the resume-state threshold for
  hand-reading the grant table is SBC/OCF above 50%. Recorded, not skipped.

### THE SCREEN ROW, TESTED LINE BY LINE — what survived and what did not

| screen field | value | verdict after the hand rebuild |
|---|---|---|
| `cap_m` | **588** | **2.4% HIGH.** Hand cap **$574.2M** on 19,358,247 cover shares × $29.66. Stale price, not a share-count defect. |
| `oe_bottom_m` / `oe_top_m` | **40 / 57** | **REPRODUCED EXACTLY** — 3y and 5y means × two capex ends give **$39.7M, $42.7M, $53.5M, $57.2M**. The arithmetic is right. |
| `wc_note` | *"ONE LINE MADE THE CASH: AccountsPayableAndAccruedLiabilities moved 71% of 2025 OCF"* | **ARITHMETIC RIGHT, DIRECTION INVERTED — the BELFB failure repeated.** $19,260 ÷ $27,163 = **70.9%**, correct. But the line was a **source** inside a working-capital block that was a **net drain of $35.7M, −131% of operating cash.** The MD&A says so in words: *"**Working capital used $37.6 million of cash** due to a $36.5 million increase in inventories and a $20.4 million increase in accounts receivable **partially offset by** a $19.3 million increase in accounts payable and accrued expenses."* **The payable did not make the cash; it softened the loss of it.** |
| `level_shift` / `level_note` | **2.13**, *"STEP UP - normalize down [E4-41]"* | **REPRODUCED AND CORRECT AS ARITHMETIC** (recent 3 = $75.9M, earlier 6 = $35.5M on the 9-year OCF series) — **and the instruction was right**: it is a wave, and the mean does need normalizing down. |
| `best_year_dep` | **0.238** | **REPRODUCED** on the 9-year OCF series. **But it understates the problem by more than half**: on the series the framework actually values, **FY2023 is 59.2% of the five-year owner-earnings window**, not 23.8%. |
| `level_shift_oe` / `level_note_oe` | refused, *"EARLY HALF STRADDLES ZERO … $-12.7M"* | **REPRODUCED EXACTLY** — the 9-year capex-end series runs −$1.98M, $33.44M, −$5.96M, $47.08M, $50.39M, **−$12.66M**, so the refusal is correct and the **$-12.7M is FY2022**. |
| `flags_disagree` | *"one series refuses the ratio and the other does not"* | **EXPLAINED.** The **operating-cash** series' early half has one small negative and a positive mean, so the guard passes it and it prints 2.13; the **owner-earnings** series' early half straddles zero properly, so the guard refuses. **The refusing series is the right one** — a ratio across a sign change is not a ratio, and operating cash simply hides the sign changes that netting capex reveals. |
| `window_disagree` | *"the 9yr base may already contain the wave"* | **CONFIRMED, and worse than stated.** Not only does the 9-year base contain the wave; **the 5-year base is 59% made of one year of inventory liquidation.** |
| `spread_caveat` | *"4-construction width only … CANNOT see variation older than the 5-year window; rebuild it"* | **THE INSTRUCTION WAS RIGHT AND THE REBUILD CHANGED THE ANSWER.** Sixteen filed years give **$24.0–24.1M**, against the published **$40–57M**. **The long-window mean is 41% of the published band's midpoint.** |
| `acq_note` | *"acquisitions are $72M, 12% of cap, inside the window"* | **CONFIRMED, at 12.6% of the hand cap**, and the perimeter is worse than the note implies — see below. |
| `growth_required` 0.0326, `yield_bottom` 0.0674, `vs_sovereign` 0.0139 | | **All three are computed on a band the rebuild refutes and on a cap 2.4% high.** No Q5 number is reported; the file closed at Q2. |
| `newest_filing` 2025-09-27 / `newest_periodic` 2026-06-27 | | **BOTH CORRECT.** FY2026 closes 2026-10-03 and no 10-K for it exists. |

### THE AGGREGATE WORKING-CAPITAL CHECK — computed by hand, as the ADM defect requires

**The standing check after ADM:** `working_capital_flag()` tests **single** lines against a 30%
threshold, so it missed a **50.7% aggregate** at ADM. Insteel is the mirror image — the note fires
on a **combined** tag — so the net block was computed by hand for every year, as
**cash = −ΔAR − ΔInventories + ΔAP&accrued − ΔOther**, reconciled to the filed statement in FY2025
and FY2023.

| FY | net WC cash | as % of OCF | the line that did it |
|---|---|---|---|
| 2021 | **−$13.2M** | −18.9% | inventories building as prices rose |
| **2022** | **−$135.8M** | **−2,395%** of $5.7M of operating cash | **inventories absorbed $118.6M** |
| **2023** | **+$97.6M** | **+68.6%** | **inventories released $94.3M** |
| 2024 | +$17.6M | +30.2% | inventories $14.5M |
| **2025** | **−$35.7M** | **−131.5%** | inventories −$36.5M and receivables −$20.4M, **AP +$19.3M an offset** |
| 9M FY2026 | **−$18.6M** | −103% of $18.0M | inventories −$29.1M, **AP +$13.7M an offset** |

**Three things follow, and none of them is in the screen row.**
1. **Insteel's operating cash IS a working-capital series**, in both directions, and in FY2022 and
   FY2023 the working-capital line was larger than the operating cash itself.
2. **The flagged line is an offset in both of the two most recent periods.**
3. **The unflagged line is the one that matters.** In FY2023 the inventory release was **66.3% of
   operating cash**, over the flag's 30% threshold, in the flag's own five-year window — and
   **the flag never saw it.**

### TOOLING DEFECTS FOUND — reported, not patched *(a tool may remove friction, never add a step)*

1. **`WC_TAGS` contains no inventory tag and no receivables tag.** The list is
   `IncreaseDecreaseInAccountsPayableAndAccruedLiabilities`, `IncreaseDecreaseInAccountsPayable`,
   `IncreaseDecreaseInContractWithCustomerLiability`, `IncreaseDecreaseInDeferredRevenue` — all
   four are **liability** lines. **A working-capital flag that cannot see inventories is blind to
   every inventory-cycle business there is**, which is most of industrials, distribution and
   retail. Insteel tags `IncreaseDecreaseInInventories` and `IncreaseDecreaseInAccountsReceivable`
   in every year, so the data was present and the test did not ask for it. **This is the same
   defect class the queue keeps finding: a guard that reads one side of the series while the
   defect lives on the other.**
2. **The flag reports only the single largest line and stops.** FY2025's payable at 70.9% beat
   FY2023's inventory release at 66.3%, so only the payable was printed — **and the payable was
   an offset while the inventory release carried the whole published band.** Reporting the maximum
   is not the same as reporting the material one; the honest output is every line over the
   threshold, in every year of the window, with its sign.
3. **The direction defect is now confirmed twice.** BELFB found it and IIIN reproduces it: the
   note's sentence *"ONE LINE MADE THE CASH"* asserts a direction the function never tests. It
   computes `abs(v)/abs(o)` and then prints a directional claim. **Two runs, two inversions —
   this is no longer a one-off.**
4. **A note, not a defect, about the band:** `oe_bottom`/`oe_top` are constructed from 3- and
   5-year windows only, and on this name the sixteen-year mean sits **$16M below the published
   bottom**. The `spread_caveat` says this in words and the CSV's own columns then carry the
   narrow band as if it were the answer.

### The acquisition perimeter [the standing check]

- **$72.1M of cash out in FY2025** — EWP $67.0M (2024-10-21) and OWP $5.1M (2024-11-26) — against
  a hand cap of $574.2M: **12.6%.**
- **The acquired operations' cash is inside the operating-cash series from 2024-10-21 onward and
  the purchase price is nowhere inside maintenance capex.** Eleven and a half months of acquired
  operating cash sit in FY2025's $27.2M; the $72.1M sits in investing. **Any owner-earnings
  series that spans the deal is comparing two different companies**, which is why the sixteen-year
  mean is the honest one and the three-year mean is not.
- **The tested source limit applies and was not re-attempted** (resume state, section 5):
  **stock consideration does not resolve undimensioned in companyfacts.** It does not bite here —
  **both deals were all cash** (*"The EWP Acquisition was funded with cash on hand"*), read from
  the filing rather than inferred from a tag.
- **What the filing will not tell anyone**: *"the presentation of EWP's earnings is impracticable
  for 2025."* The **pro forma is the only quantification that exists**, and it says the
  acquisition would have **cut FY2024 net earnings by $1.8M**. $25.9M of the $67.0M became
  **goodwill**; FY2025 goodwill rose $9.7M → $37.8M and intangibles $5.3M → $16.6M.

### Great, good, or gruesome? **[E4-20]**

- [ ] great · [ ] good · [x] **gruesome, on the sixteen-year record, and the test is [E4-43]'s
  boundary rather than a slur.** *"The worst sort of business is one that grows rapidly, requires
  significant capital to engender the growth, and then earns little or no money."* Insteel does
  not grow rapidly, which is the one respect in which it is not the airline. But **[E4-43]** says
  the *good* class passes on the strength of *"nothing shabby about earning $82 million pre-tax on
  $400 million of net tangible assets"* — roughly **20% pre-tax on tangible capital** — and
  Insteel's sixteen-year unlevered ROE is **9.9%** while the working capital that funds the volume
  has to be **re-lent to the cycle at every upturn**: $118.6M of it in FY2022 alone, on a business
  whose equity was then $390M. **The savings-account image decides it**: the deposits added in
  FY2022 earned nothing, and the account only looked good in FY2023 when the deposit was
  withdrawn. **[E5-40]**'s ~12% *"quite satisfactory"* return-on-retention benchmark is not
  reached on the long window either.

### Staying power — score all three **[E5-11]**

1. **A large and reliable stream of earnings — LARGE, NOT RELIABLE.** Net earnings over seventeen
   filed years: −$22.1M to +$125.0M. **[E5-29]** is honoured — volatility is not risk — but
   [E5-11] asks for *reliable*, and the FY2019 and FY2022 owner-earnings years are negative.
2. **Massive liquid assets — YES, AND RECENTLY HALVED AND HALVED AGAIN.** Cash $125.7M (FY2022)
   → $111.5M (FY2024) → **$38.6M (FY2025)** → **$14.9M at 2026-06-27**, plus an undrawn $100M
   revolver ($98.7M available at FY2025 year end, $1.3M of letters of credit). **No debt at any
   date read.**
3. **No significant near-term cash requirements — THE ONE THAT USUALLY KILLS, AND IT IS THE ONE
   TO WATCH HERE.** The FY2025 commitments note: *"we had $ 92.3 million in non-cancelable
   purchase commitments for raw material extending as long as approximately 60 days"*, against
   **$38.6M of cash**. The gap is covered by the revolver and by the receivables those purchases
   turn into — but **[E5-39]**'s standard is *"We will never be dependent on the kindness of
   strangers"*, and a borrowing base *"calculated based upon a percentage of eligible receivables
   and inventories"* is exactly the facility that shrinks when the cycle turns, because the
   collateral shrinks with it. **That is the structural weakness in an otherwise conservative
   balance sheet, and it is not visible in the debt-to-capital ratio of zero.**
- **Leverage, named and quantified [E4-16, E3-29]:** **none.** Total debt $0; other liabilities
  $25.1M (operating leases and the supplemental retirement plan). **[E3-52]**'s reading — covenant
  terms matter more than quantity — finds nothing covenanted and nothing due. **On leverage this
  is among the cleanest balance sheets the queue has read.**

### Name the specific way THIS business dies **[E2-27, E3-24]**

**The mechanism: the spread inverts and the inventory is on the wrong side of it.** Insteel buys
rod on monthly pricing (*"most recently monthly for domestic suppliers"*) and sells into a market
where *"we may be unable to fully recover increased rod costs during weaker market environments"*
and where, when rod falls, *"our financial results would be negatively impacted if the selling
prices for our products decrease to an even greater extent **and if we are consuming higher cost
material from inventory**."* The kill is the second clause: a cost shock that cannot be passed
on, landing on an inventory bought at the old price.

**Quantified from filed figures — and the company quantifies it itself.** Q3 FY2026 10-Q, Item 3:

> *"Based on our shipments and average wire rod cost reflected in cost of sales for the first nine
> months of 2026, **a 10% increase in the price of wire rod would have resulted in a $33.1 million
> decrease in our pre-tax earnings** (assuming there was not a corresponding change in our selling
> prices)."*

**Nine-month pre-tax earnings were $28,104 thousand.** So **a 10% rod move with no price response
erases 118% of the year's pre-tax earnings** — more than all of it. The second, slower form is the
inventory whipsaw already on the record: **$118.6M absorbed in FY2022 and $94.3M released in
FY2023**, a swing of 38% of the current market value inside two years, on a decision about when to
buy steel.

**The exposure, not the experience [E4-40].** *"all of us in the industry made a fundamental
underwriting mistake by focusing on experience, rather than exposure."* The experience is
reassuring — seventeen years, no debt, never a loss year after 2009. **The exposure is $33.1M of
pre-tax earnings per 10% of rod price, a 50% Section 232 tariff on the steel content of its own
product (*"recently increased to 50% from 25%"*), 27% of rod purchased abroad, and a trade regime
in its finished markets that has to be re-petitioned each decade.**

**Likelihood: [x] a real possibility** for a year of negative owner earnings — it has happened in
**FY2011, FY2019 and FY2022** within the sixteen years read, which is roughly one year in five.
**[ ] likely** is not claimed for permanent impairment: with no debt and a discretionary capex
budget, the mechanism above produces **bad years, not death**. **The honest statement is that this
business is very hard to kill and quite easy to make worthless as a compounder** — which is Q2's
finding arriving at Q4 by another road.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE — NO VERDICT. THE FILE CLOSED AT
  Q2.** *Note for the record: had it reached here, **[E4-25]**'s too-wide-a-range rule would have
  closed it independently — the combined range runs from −$20.5M to $57.2M.*

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### ⛔ Q5 DOES NOT OPEN. Q2 is OUT. **No yield, no value range, no ranking, no floor verdict.**

**One line is recorded and it is a statement about the screen, not about the price.** The screen
ranked this name on a yield of **6.74%** computed from a band of **$40M–$57M** over a cap of
**588**. On the hand-struck cap of **$574.2M** and the **sixteen-year** owner-earnings mean of
**$24.0–24.1M**, the same arithmetic gives **4.2%**, against a sovereign of **5.34%** — *below the
bond, before any judgment about the business is made at all.* **This is COMPUTATION, NOT A
CLEARANCE**, it is reported only to record what the rebuild did to the screen's input, and
**[E4-28]**'s floor is not adjudicated because the question is not open.

- **VERDICT: NOT OPENED. Q2 closed the file.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

### ⛔ No position, no entry, no exit metric. **NO PRICE ALERT — the QLYS ruling.**

**A name that failed on the BUSINESS gets no price band.** **[E5-35]**: *"You can turn any
investment into a bad deal by paying too much. **What you can't do is turn any investment into a
good deal by paying little.**"* Arming a price alert on IIIN would assert the opposite.

**THE REVERSAL CONDITION, IN WORDS, PRICE EXCLUDED.** This file reopens only if the **business**
changes, and the change would have to be visible in filings as one of these:

1. **A structural change in the industry's supply**, not a cyclical one — filed evidence that the
   named competitors' capacity has permanently left the market, such that the FY2025 statement
   *"our remaining welded wire reinforcement production facilities … have ample open capacity"*
   ceases to be true industry-wide. **[E2-58]**'s equation turns on over-capacity, and only its
   removal turns it back.
2. **Pricing conduct that survives a flat-demand year** — a fiscal year in which shipments are
   flat or down and **average selling prices rise**, reported in the MD&A in those terms. That is
   **[E2-44]**'s test, and FY2024 is the filed counter-example.
3. **A physical series that grows without being bought** — shipments up on an organic basis, with
   the MD&A separating organic from acquired tonnage, for three consecutive years. **[E4-55]**.
4. **Backward integration into wire rod**, which would be the only visible route to the *"wide and
   sustainable"* cost advantage **[E2-58]** names as its single exception — and would itself be a
   new business needing its own run.

**None of these is a price. [E4-17]**'s *"beliefs change quite gradually"* governs the formation
of this view, and nothing above would be read from one quarter.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE — NO VERDICT. THE FILE CLOSED AT
  Q2.**

---
'''
io.open(p, 'w', encoding='utf-8').write(head + '\n' + new + rest)
print("ok")
