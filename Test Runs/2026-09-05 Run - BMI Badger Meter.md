# Company Run — Badger Meter (BMI) — 2026-09-05
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

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

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24%** · date **2026-09-04** · source (issuing authority) **US Treasury daily par
  yield curve, 30-yr** (struck fresh via `tools/sources.py`; the brief's ~5.25% was stale by
  one basis point)
- FX: none — USD quote, USD earnings (US = $825.9M of $916.7M FY2025 sales = 90.1%, Note 9)

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **10-K FY2025, filed 2026-02-17, accession
  0001193125-26-054739** (primary doc `bmi-20251231.htm`); **10-Q Q2-2026, filed
  2026-07-23, accession 0001193125-26-313981** (`bmi-20260630.htm`); both downloaded to
  `Test Runs/_research 2026-09-05 BMI/`
- figure cross-checked against the filed statement: **FY2025 net cash provided by
  operations $183,698k** — run.py's XBRL $184M matches the filed Consolidated Statements
  of Cash Flows to rounding. Also verified there: capex $14,026k, SBC $9,190k,
  acquisitions net of cash $184,024k (SmartCover), dividends $43,529k, **interest paid $0**.

**PRICE AND SHARES (Stage 0, by hand):**
- price **$132.49** · 2026-09-04 · **aggregator (run.py live quote), flagged** [operator rule 5]
- shares **28,986,847** — hand-read off the Q2-2026 10-Q cover, as of 2026-07-10, single
  class, $1 par. run.py's 29.6M is the known weighted-average defect; corrected by hand.
- **market cap $3,840M** (28,986,847 × $132.49)

**SCREEN ROW REPRODUCED before adjudicating:** the brief's row (yield 2.80%, growth required
7.20%, spread 22.6%) is the **5-yr window** at ~this cap: run.py 5-yr OE $106–109M → yield
2.71–2.79% at its $3.92B weighted-average cap; spread = 3-yr bottom $130M / 5-yr bottom
$106M − 1 = **+22.6%** — reproduced. The 3-yr window yields 3.31–3.36%. level_shift
"STEP UP — normalize down [E4-41]" is live: OE roughly tripled FY2019→FY2025 (verified at
Q4). **run.py's D&A read is depreciation ONLY ($11.1M), excluding amortization ($23.5M)** —
the band ends are re-derived by hand at Q4.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **BMI sells the cash register of
  a water utility.** Every billed gallon passes through a meter; the meter is a small line
  in a utility's budget but its accuracy IS the utility's revenue (an under-reading meter
  is unbilled water). One product line is 89% of sales (Utility Water, FY2025); the US is
  90% of revenue. The sale used to be a $50-100 brass meter every 15-20 years; it is now
  meter + battery radio endpoint (ORION, increasingly cellular) + a cloud reading
  subscription (BEACON SaaS, $73.6M FY2025, filed series), which multiplies revenue per
  connection and adds a recurring layer. Demand is replacement-cycle driven — the filer:
  "Water meter replacement and the adoption and deployment of new technologies comprise
  the majority of smart water product sales... Housing starts have only a minimal impact."
  The industry is mid-conversion from manual/drive-by reading to AMI networks (filer's
  estimate: **~40% of US connections converted**), and from mechanical to ultrasonic
  meters. Economics: GM 41.7%, capex ~1.5% of sales ($14.0M on $916.7M), working capital
  ~21% of sales (PWC, the filer's own metric), **zero debt, interest paid $0**, tax ~25%.
  FY2025: $916.7M sales → $183.4M operating earnings → $141.6M net.
- The scarce input this business controls: **the spec-in position and installed
  radio/software ecosystem across thousands of fragmented municipal buyers.** 50,000+ US
  water utilities, mostly small, risk-averse, buying a 15-20-year asset whose failure is
  their own revenue line; once a utility deploys ORION endpoints and BEACON, subsequent
  meters, sensors and software renew inside the same ecosystem. A century-old brand
  (incorporated 1905; auditor unchanged since 1927) in a market where "brand recognition,
  product breadth and utility sales channels" are the filer's own stated barrier.
- Will the fundamentals look broadly the same in ten years? Water will still be metered,
  meters will still wear out, and utilities will still bill from them — yes at the level of
  the trade. The open question — what happens to the growth RATE when the AMI conversion
  wave completes — is a Q2/Q4 question about level, not a Q1 question about mechanism.
  H1-2026 already shows the first slack: utility sales −8.8%, "uneven AMI project pacing"
  (10-Q, filer's words).
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] — the meter is how a water utility generates its revenue; a
  statutory and operational necessity, replaced on a 15-20 year cycle.
- No close substitute [x, at the ecosystem level, with the limit stated] — at the initial
  bid, four-plus rational competitors sell functionally similar meters (see row). The
  no-close-substitute claim attaches to the INSTALLED ecosystem, not the meter: once a
  utility runs ORION endpoints and BEACON, switching vendors means replacing the radio
  network, software, and billing workflow mid-life. The moat is filed by a COMPETITOR:
  MWA's 10-K — "end users will be reluctant to adopt brands other than their historically
  preferred brand." And BMI's own filing on entrants: "new static metering market entrants
  lack brand recognition and product breadth and do not have the appropriate utility sales
  channels to meaningfully compete in the North American market."
- Not price-regulated [x] — BMI's prices are unregulated; the buyers are rate-regulated
  monopolies buying through competitive bids. **[E3-03] criterion 3 held with care (the
  AATC lesson): what has realized pricing actually done?** Units are NOT disclosed — no
  unit series has ever been filed by BMI [E4-55 limit], so revenue-per-meter is not
  derivable. The honest instrument is the GM series, and it does NOT show price-taking:
  **GM 38.5% (2019) → 39.5 → 40.7 → 38.9 (2022 dip) → 39.3 → 39.8 → 41.7% (2025)** — not
  monotonic, and the filed attribution is MIX every single year ("favorable product mix,
  driven by sales growth in ultrasonic meters, ORION Cellular radios, water quality
  products and SmartCover"), never price. The only price language in the FY2025 10-K is
  tariff cost-recovery. The margin expansion is real but it is the attach-rate economics
  (cellular endpoint + SaaS per meter), not realized price increases on like units.
- Must the moat be continuously rebuilt? **[E4-04]** — the technology layer turns over
  (radio generations, cellular sunsets, batteries), but the turnover IS the revenue model:
  replacement demand. The spending (R&D $21.6M, 2.4% of sales) defends the same advantage
  — the utility relationship and installed base — not a replacement deposit. A lapse
  narrows, not destroys. **The [E3-51] surfing question is the live one**: the last five
  years' growth rode the AMI conversion wave (filer's own estimate: ~one-third of US
  connections converted in the FY2023 10-K → ~40% in the FY2025 10-K), and the wave is
  finite. Part of the record is position, part is wave [E4-36 combination]; the wave share
  is priced at Q4/Q5 by normalizing the level down, not here by denying the moat.
- Does success depend on a great manager? No — [E4-23] passes; multi-decade positions,
  internal bench, no superstar dependence.
- Primary moat metric, filing-sourced, and its trend: **utility water revenue and the
  recurring layer.** Utility water $344.3M (2020) → $816.1M (2025), +137% in five years;
  SaaS $42.2M → $56.9M → $73.6M (2023-25, filed series, +35%/+29%); contract liabilities
  $78.3M → $97.0M. Countertrend, displayed not hidden: H1-2026 utility water **−8.8%**
  ("uneven AMI project pacing") and over-time revenue +1.6% — the wave paces lumpy.

**THE COMPETITOR ROW — required [E3-28].** Same metric: FY2025 10-K filings, revenue
growth / GAAP margin / pre-tax return on net tangible operating assets where computable.
Full workings: `Test Runs/_research 2026-09-05 BMI/row ITRI.md, row XYL.md, row ROP.md,
row MWA.md`.

| Company | FY2025 revenue (growth) | op margin / GM | RONTA pre-tax | source |
|---|---|---|---|---|
| **BMI** | $916.7M (+10.9%); utility $816.1M (+12.5%) | 20.0% / 41.7% | **~138%** ($183.4M / ~$133M) | 10-K acc 0001193125-26-054739 |
| ITRI (whole co) | $2,367.2M (−3.0%); bookings −22%, book-to-bill 0.89 | 13.2% / 37.7% | 43.5% | 10-K acc 0000780571-26-000033 |
| XYL M&CS (Sensus inside) | $2,086M (+11.5%, energy-led; **NA water DECLINED**) | 11.7% GAAP seg (16.9% adj) | n/a — segment assets not filed | 10-K acc 0001524472-26-000012 |
| ROP TEP (Neptune inside) | $1,818.7M (+7.3%, "led by medical products"; Neptune not named) | 34.5% seg (medical-mixed) | co. denominator NEGATIVE ex-Indicor | 10-K acc 0000882835-26-000009 |
| MWA (metering a slice of 42%) | $1,429.7M (+8.7%) | 18.2% / 36.1% | not computed (minimal entry) | 10-K FY2025 (Sep FYE) |

- Peers named: **5 rowed (BMI + 4 filings) of the ~7 real water-metering competitors MWA's
  own 10-K names** (Sensus, Neptune, Badger, Itron, Master Meter) plus Kamstrup and
  Aclara/Hubbell from BMI's list. **Row limits stated [E3-61]: Neptune's and Sensus's own
  figures are unknowable from filings** (held at their disclosed segment units, said
  plainly in the row files); Kamstrup and Master Meter are private non-filers. This is the
  disclosed reality of the industry, not a research gap with a nameable document — the row
  is as complete as filings permit, so the class is judged, not held PROVISIONAL (the
  TSCO/SBUX precedent).
- **[E2-45] the attacker record convicts the attackers, not BMI:** Itron — the $2.4bn
  attacker with the network stack — grew +25.7% TOTAL in ten years (FY2015 $1,883.5M →
  FY2025 $2,367.2M, ~2.3%/yr; still below its FY2011 $2,426.1M), its water segment
  ($519.4M in FY2015 — LARGER than BMI's utility line then) has disappeared from its own
  disclosure, and its FY2025 competitor list doesn't name Badger Meter (it frames itself
  against Ericsson/Landis+Gyr — electric grid). Sensus under Xylem: NA water declined
  FY2025 after backlog execution; not visibly compounded since the 2016 purchase. Neptune
  under Roper: TEP growth attributed to medical products. Meanwhile BMI's utility line
  went $344M → $816M. The would-be attacker with ample capital has been losing the water
  account for a decade.
- **[E2-44] two-characteristic test:** (1) raise prices with flat demand — **NOT PROVEN**;
  no unit series filed, GM attributed to mix, bidding market (stated as the moat's
  ceiling). (2) grow dollar volume with minor additional capital — **passes loudly**:
  revenue +116% FY2019→FY2025 on ~$133M of net tangible operating assets, capex 1.5% of
  sales; the only real capital line is working capital (~21% of sales, the filer's own
  PWC metric).
- **Untapped pricing power [E3-33]:** not claimed — claiming it is claiming near-monopoly
  [E5-28], and the row shows a four-brand oligopoly with competitive bidding. [E2-53]
  dominance: no. [E3-46] high returns on capital employed: yes, top of the row by a wide
  margin.
- Class: **[x] NARROW** [ ] WIDE — real (spec-in ecosystem, brand, channel, verified from
  competitors' filings) but bid-priced at the front door, pricing power unproven, and part
  of the five-year record is a finite conversion wave [E3-51]. · Direction **[E4-32]:
  widening inside water** — recurring software layer compounding ~30%/yr, deferred revenue
  rising, share record vs all three attackers; H1-2026's −8.8% is project pacing, judged
  an aberrational cycle question [E3-30], watched at Q6, one half-year against five
  structural years.
- **VERDICT: [x] IN (NARROW)**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**
Case declared, and why: **OVERLAY.** Zero debt (interest paid $0 three filed years — the
[E5-11] brief item verified at the cash line), public minority position, and a
differentiated product with multi-decade spec-in relationships — the kind of position that
would stand a stumble [E5-18]. None of the three magnifiers applies.

**Honesty — binary, permanent, filings-based [E5-16].** No integrity matter found in any
document read: "There are currently no material legal proceedings pending" (Note 6,
FY2025 10-K); unqualified ICFR opinion; auditor Ernst & Young **since 1927**; no
restatement in any vintage read (FY2021, FY2023, FY2025, Q2-2026). CEO Bockhorst holds
Chairman+President+CEO combined (noted, not charged); CFO succession Jan 2026 orderly,
internal, disclosed. Full workings: `_research 2026-09-05 BMI/Q3 proxy notes DEF14A
2026.md` (DEF 14A filed 2026-03-13, acc 0001193125-26-106185).

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — none found: SBC expensed, pension trivial ($1.2M accrual), GAAP-only
  reporting, no restatements
- [ ] unintelligible footnotes — no; the 10-K is ~60 readable pages
- [ ] trumpeted earnings projections / growth targets — **none found**: no revenue or EPS
  guidance anywhere in the FY2025 10-K or Q2-2026 10-Q (sweep stated; the only forward
  number is capex "$15.0-19.0 million"); earnings releases not swept, claim scoped to SEC
  filings. [E5-30]'s ratchet never started on the documents read.
- [ ] serial share issuance — no: issued shares 37,221,098 UNCHANGED across every vintage
  read; basic count 29.0M (2019) → 29.0M (cover, July 2026)
- [x] EBITDA / adjusted-earnings promotion **[E4-29]** — **fires, scoped to the PAY
  DESIGN**: the annual bonus is 50% adjusted EBITDA and the 402(v) company-selected
  measure is EBITDA. The FINANCIAL REPORTING is clean: zero EBITDA/adjusted-earnings/
  non-GAAP occurrences in the FY2025 10-K (counted); the 10-Q's six mentions are all the
  UDlive earn-out formula. A prompt read, recorded, not a promotion culture.
- [ ] filed-figure tells **[E4-30]**: smoothness — no (revenue path 0%, +18.7, +11.9,
  +24.4, +17.5, +10.9, −7.8% H1-26); cash-tax % of pretax 31.9 → 33.7 → **25.8%** — the
  FY2025 fall coincides with the 2025 tax act's restored R&D expensing (industry-wide);
  book ETR steady at 24-25%. Explained; watched, not charged.
- [E2-49] metric-switching: none found across FY2021/FY2023/FY2025 vintages — the
  utility/flow split, over-time disaggregation, and AMI-conversion estimate all run
  continuously; the SaaS dollar table was ADDED in the FY2024 10-K (expansion, the
  [E2-69] direction).

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth.
- Years used, and the series: FY2020-FY2025, zero leverage throughout, average equity:
  **14.2% → 16.0% → 15.8% → 19.3% → 22.3% → 21.5%** — rising, unlevered, and understated
  by a growing cash pile inside the denominator (cash was $226M of $713M equity at FY2025).
  On net tangible operating assets [E2-43]: ~138% pre-tax (FY2025), top of the competitor
  row by 3x. The goodwill wedge reported separately: goodwill+intangibles $354.1M of the
  $713.3M book (FY2025), built by ~$278M of acquisitions 2020-2025.

**The half-owner test [E2-26]:** passes on what was read — the SmartCover and UDlive
purchase-price allocations are itemized to the million including the earn-out fair value;
the warranty note volunteers that new technology "generally caused our annual warranty
claims rates to increase over time" (a fact against interest); the H1-2026 sales decline
is explained in plain words ("uneven AMI project pacing") with no adjusted-revenue
cushion invented. One deduction: no unit volumes, ever — the reader cannot decompose
price×volume [E4-55]; recorded at Q2 as the moat evidence ceiling.

**The institutional imperative — score all four [E2-30].**
- [ ] resists any change in current direction — no; the cellular-AMI pivot cannibalized
  its own fixed-network/AMR lines years early
- [x] projects/acquisitions materialise to soak up available funds — **watch item**: with
  the core decelerating, ~$290M went to two sewer-monitoring deals in 16 months
  (SmartCover $184.0M ≈ 4.6x revenue, Jan 2025; UDlive $94.4M + earn-out ≤$50M ≈ 7-8x
  run-rate revenue, May 2026) — adjacent, strategy-consistent, small vs the cap, but
  revenue multiples the core itself does not trade at. [E3-40] loss-of-focus: not yet —
  both bolt onto the same utility customer and BEACON platform.
- [ ] staff studies to justify the leader's craving — not in evidence
- [ ] peer behaviour mindlessly imitated — no (peers are conglomerates running adjusted
  reporting; BMI reports GAAP-only)

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? **Yes** — no debt, $95.7M cash after the
  H1-2026 spend, $150M line undrawn (extended 2026-06-05 to 2031).
- (2) repurchases at a **material discount** to conservatively calculated IV? **FAILS on
  this run's numbers**: H1-2026 repurchases $63.5M at ~$157-159 average (treasury
  +399,891 shares) vs this run's zero-growth conservative value of ~$70-105/share (Q5).
  Nov 2025 authorization $75M through Nov 2028, ~$11.5M left. → **CAPITAL ALLOCATION
  FLAG**, stated with the humility clause **[E4-13]**: this rests on our own IV range,
  management knows the business better than we do, and "many CEOs never stop believing
  their stock is cheap" [E5-08]. **Binds position size, never the discount rate.**
- The rest of the record, for completeness: retention [E3-54] passes (~$394M retained
  FY2019→H1-2026 against ~$1.9bn of market value added even after a 45% drawdown);
  dividend increased every filed year checked; **the RPM decomposition PASSES — five-year
  DPS +112% (0.700→1.481) against EPS +183%, payout ratio FELL 41%→31%, retirement ≈ nil:
  dividend growth is entirely earnings-driven** (first clean pass in the queue since DRI).
  The proxy's "increased its dividend for 33 consecutive years" verifies by arithmetic
  for every year the filings on disk cover (2020-2025); earlier years rest on the filer's
  claim, stated as such. Bonus targets set ABOVE prior actuals both metrics in FY2025
  (EBITDA target 210.0 vs 190.1 prior actual; FCF 145 vs 142.2) and paid 179.8% on a
  real beat — the DG/ULTA rigging pattern does not replicate. LTIP: 3-yr FCF-conversion
  + ROIC PSUs, CEO mix 80% performance-based; CAP fell with TSR in 2025 ($9.64M → $6.29M)
  — the plan transmits the stock down into pay. 402(v): TSR $100 → $192.28 vs peer group
  $177.87, Russell 2000 $134.40.

**THE GUARDRAIL — check before writing the verdict.**
- [x] Confirmed: nothing in this Q3 promotes the name. A strong record cannot repair Q2's
      NARROW class or substitute for Q4 **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence: none recorded — [E4-23] handled at Q2.
- [x] A great manager is not the reason to act; no excisable-cancer case is being made.

- **VERDICT: [x] IN** — *no disqualifier found. NOT a finding that the managers are honest
  [E5-17]. IN never promotes. Two live items carried forward: the buyback condition-2
  flag (binds position size) and the acquisition-multiple watch item [E2-30](2).*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
- Owner earnings by year (OCF − SBC − capex, $M, all hand-transcribed from filed
  statements; series file in `_research 2026-09-05 BMI/`):
  **2019: 72.0 · 2020: 79.1 · 2021: 78.5 · 2022: 73.4 · 2023: 92.9 · 2024: 136.0 ·
  2025: 160.5 · H1-2026: ~51.3** (60.6 OCF − 9.3 capex, SBC not separately filed in the
  10-Q line read — displayed, not annualized)
- **Short-window mean** (3-yr, 2023-25): **$129.8M**
- **Mid-window mean** (5-yr, 2021-25): **$108.3M**
- **Long-window mean** (7-yr, 2019-25): **$100.3M**
- **Leave-two-out (drop 2024+2025, the brief's ordered check): $79.2M** — the pre-wave level.
- **Spread, conservative end:** 3-yr vs 5-yr bottoms = **+22.6%** (the screen row's number,
  reproduced); full construction spread 79.2 to 129.8 = 64%.
- **Combined range: $79M to $130M, judged $105M** (below).
- *Too wide to conclude?* **No — and this is the unusual case where the width is harmless:
  every construction in the range, including the single best year ever ($160.5M), yields
  BELOW the 5.24% sovereign at today's cap. The verdict at Q5 is identical at every point
  of the range.*
- *The distorted years, named [E4-41]:* **2023-2025 sit on the AMI-wave crest plus the
  post-shortage backlog catch-up — and the evidence is filed by all three competitors and
  by BMI itself.** BMI FY2023 MD&A: record backlog from 2021-22 component shortages fed
  +24.4% growth. Itron's FY2025 10-K: the 2024 spike "included a significant amount of
  catch-up of previously supply chain constrained revenue," and its bookings then fell
  22%. Xylem's FY2025 10-K: "declines in water in North America due to lower demand
  following strong prior year backlog execution." BMI's own H1-2026: utility sales −8.8%,
  "uneven AMI project pacing," OE running −34% yoy. **The step-up decomposition: the
  durable part is the permanently larger installed base and the recurring layer (SaaS
  $42.2 → $73.6M filed, over-time revenue 5.0% → 10.4% of sales, deferred revenue $97.0M);
  the finite part is the conversion-wave crest in hardware. Normalized DOWN [E4-41]:
  judged OE $105M** — at the 5-yr mean and ≈ the level H1-2026 is actually printing
  (~$103-116M annualized), above the $79M leave-two-out floor because the recurring layer
  and installed base do not revert.
- **Maintenance capex — the (c) judgment [E2-23].** This is the [E3-44]/[E2-41] DEFAULT
  case, not the [E5-20] exception: capex $5.9-14.0M runs AT depreciation ($10.9-11.1M);
  5-yr average capex $10.3M ≈ depreciation. BMI is the anti-railroad — [E3-44] validated,
  the D&A end and capex end nearly coincide (the screen's tight $130/$132 band). (c) is
  taken at TOTAL capex each year (conservative: includes growth capex). Two disclosed
  judgments on top: (i) the working-capital increment (constraint 3) is inside OCF and
  during growth years SUBTRACTS more than steady-state would — conservative direction;
  (ii) the tuck-in acquisition stream (~$278M, 2020-2026) is treated as growth capital,
  NOT (c) — but it is noted against interest that the "product breadth" barrier the filer
  claims has been maintained partly by purchase, so a zero-acquisition BMI would be a
  narrower company over decades.
- Stock compensation subtracted in full **[E5-06]**: yes, every year (1.2 → 9.2M, from the
  filed cash-flow adjustment line).
- *The capex band does not change the verdict — both ends yield below the bond at Q5.*

### Great, good, or gruesome? **[E4-20]**
- [x] **great** — high return, rising, little capital needed
- Evidence: ROE 14→22% with zero leverage; ~138% pre-tax on net tangible operating assets;
  revenue +116% (FY2019→25) on capex of 1.5% of sales; the deposit added (working capital
  ~21% of sales) earns at the same extraordinary rate. **The ceiling stated [E2-63]:** the
  AMI conversion is finite (filer: ~40% converted); at completion the market reverts to
  replacement + SaaS, which bounds the upside case.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings — **pass**: profitable every filed year read;
  earnings rose through COVID (2020) and the 2022 supply shock both.
- (2) massive liquid assets — **pass, with the note**: $95.7M cash, zero debt; was $295.3M
  before 16 months of SmartCover + UDlive + buybacks drew the pile down $200M. Scale: cash
  covers ~6x annual capex + dividend combined.
- (3) **no significant near-term cash requirements** — **pass, the cleanest in the queue**:
  borrowings ZERO, interest paid $0 (filed supplemental line, three years), no maturities
  ever, leases $3.5M/yr, postretirement $0.2M/yr. The only contingent call is the UDlive
  earn-out, ≤$50.0M payable ~mid-2028 ($12.0M booked). Nothing depends on the kindness of
  strangers [E5-39]; the $150M revolver (extended 2026-06-05 → 2031) is not counted.
- Leverage, named and quantified **[E4-16, E3-29]**: none. [E2-54] coverage: no interest
  to cover. [E2-60]: does not fire on the earnings level (FY2025 payout $58.5M vs OE
  $160.5M); H1-2026's $181.2M of acquisitions+buybacks+dividends against ~$51M OE was
  funded from the cash pile with financial strength intact (still debt-free) — a spend-down,
  not restricted-earnings distress; watched.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- **Mechanism 1 — the wave ends (a valuation death, already partially filed):** AMI
  conversion pacing stalls; 2023-25 proves to be the crest; OE reverts toward the
  leave-two-out $79M and grows only at replacement + SaaS. Quantified: at $79M the yield
  on today's $3,840M cap is 2.06%; zero-growth value ~$52/share. H1-2026 (−8.8% utility
  sales, OE −34%) is the opening chapter. Likelihood: **[x] a real possibility** — for
  the LEVEL, not for solvency.
- **Mechanism 2 — the ecosystem lock dissolves (technology diagonal):** multi-commodity
  network players or the carriers commoditize the water endpoint; utilities buy
  connectivity + any meter; BMI reverts to a hardware vendor at attacker margins.
  Quantified: at Itron's 13.2% op margin on BMI's $916.7M revenue, operating earnings fall
  $183.4M → ~$121M (−34%). Likelihood: **a low-level possibility** — the row shows the
  attackers failing at exactly this for a decade, and MWA files the brand-reluctance
  moat from outside.
- **Mechanism 3 — solvency:** effectively unnameable at zero debt and $0 interest; the
  worst filed-precedent stress is a mass field-failure warranty event (Itron FY2015:
  $29.4M special charge for "prematurely failing communication modules"; BMI's reserve
  $21.6M, claims rates rising by the filer's own admission). A 10x-reserve catastrophe
  (~$200M) ≈ one year's OCF + part of cash — painful, survivable. **A low-level
  possibility.** Exposure modeled, not experience [E4-40]: 1-20 year warranties on
  batteries+electronics in pits, and cloud/software liability as BEACON scales.
- **VERDICT: [x] IN**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** Honest pre-tax expectancy at this price:
**~7-9%** (judged yield 2.73% + an honest 4-6%/yr of growth — the recurring layer and
replacement base support mid-single-digit growth; the wave-top level does not support
re-running the last three years' 14%/yr, per [E4-35]'s base rate and the filed H1-2026
downturn). **Below ~10%: the name is QUIT ON, not ranked.**

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD** (cap $3,840M = 28,986,847 sh × $132.49, 2026-09-04; sovereign **5.24%**)
- leave-two-out $79.2M → **2.06%** · 7-yr $100.3M → 2.61% · **judged $105M → 2.73%** ·
  5-yr $108.3M → 2.82% · 3-yr $129.8M → 3.38% · best year ever $160.5M → **4.18%**
- **Every construction, including the best single year in the company's history, yields
  below the bond.**
- Screen row adjudicated: its 2.80%/7.20% is the 5-yr window at this cap — reproduced and
  confirmed; the step-up flag was right, and the judged level lands at the 5-yr mean, not
  the 3-yr [E4-41].

**2. WHAT THE PRICE ALREADY ASSUMES**
- growth needed to match the BARE BOND: **+2.5%/yr perpetual** at the judged level
  (+1.9% at the 3-yr window) — the strongest thing sayable for the price
- growth needed for the ~10% floor: **+7.3%/yr perpetual from a wave-top level**
- what the business has actually done: OE +6.5%/yr (2019 → judged level), +14.3%/yr raw
  2019→2025 (wave-flattered), **H1-2026 negative (−34%)**

**3. WHAT YOU ARE PAID**
- return at the current price = **−2.5 points UNDER the sovereign** at the judged level
  (−1.9 at the 3-yr window; −1.1 at the best year ever)

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.24%** — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero-growth at the sovereign, per share
(29.0M shares):
- conservative **~$50** (leave-two-out) · judged **~$70** ($105M/5.24%) · optimistic
  **~$85** (3-yr window) · best-year-ever construction ~$105 · **current price $132.49**
- at the ~10% floor: **~$27-45, judged ~$36**
- **The price sits ABOVE the entire zero-growth band, above even the construction that
  capitalizes the best year in the company's history.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- floor verdict first: honest pre-tax expectancy **~7-9%** vs ~10% **[E4-28]** — **BELOW →
  quit on; the ranking lines are not filled in.**

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [x] **Screamer test [E4-01]** — the price sits above the WHOLE zero-growth range →
      **outcome three: no.** No margin was added on top.
- **Windage count: ONE** — the [E4-41] normalization of the level down to $105M. The value
  band then displays every construction including those above the judged level; no second
  margin was applied anywhere **[E4-11]**.

- **VERDICT: FAIL AT THE FLOOR, ON PRICE — quit on, not ranked [E4-28].** *All four
  business gates are IN; the price is the only thing wrong. Pre-committed re-look
  [E1-02]: at a 5.24% sovereign the judged zero-growth value is ~$70/share — recompute at
  the rate of the day; below ~$70 the honest expectancy clears the bond and approaches
  the floor only if the recurring layer keeps compounding. Reopen tests: FY2026 full-year
  utility sales (does the pacing recover); the SaaS series (a break below ~+20%/yr breaks
  the durable-layer half of the thesis); the over-time share of revenue; any [E2-49]
  withdrawal of the SaaS table or the utility/flow split; buybacks continuing above the
  judged band.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**NOT OPENED — the file closed at Q5 on price; there is no position.** The pre-committed
re-look and reopen tests are recorded at the Q5 verdict [E1-02]. The monitoring items
if it is ever owned: SaaS growth rate, utility-water sales direction, buyback prices vs
value, the acquisition-multiple watch item, and warranty reserve development.

**Pre-committed before entry [E1-02]:**
- Thesis-confirming metric: n/a — no entry
- **Thesis-breaking metric and its threshold:** n/a — no entry
- Next catalyst date: FY2026 10-K (~Feb 2027) re-tests the wave question with a full year

**The sell rule [E2-28]** — two triggers, three hold conditions:
- SELL if the market judges it more valuable than the facts indicate ____
- SELL if funds are needed for something more undervalued or better understood ____
- HOLD while: return on equity capital satisfactory ____ · management competent and honest
  ____ · market does not overvalue ____
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring
question: is this erosion an aberrational cycle, or has the business slipped in a way that
permanently reduces intrinsic value? ____

**Do not trim winners [E5-14].** **Position size** — a judgment, stated: ____
*(sized DOWN if a capital-allocation flag is live)*

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1→Q5 in sequence; Q6 not opened,
  stated why)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q2's row
  limits are stated as the industry's disclosed reality [E3-61], not as unverified claims
- [x] No UNRESEARCHED verdicts issued
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: MD&A, cash-flow detail lines, footnotes read; accessions recorded; FY2025
  OCF $183,698k cross-checked against the filed statement
- [x] Owner earnings on multi-year means; FOUR windows displayed; capex band disclosed as
  a judgment with the [E3-44] default validated
- [x] Competitor row filled: 5 filings, limits stated
- [x] Sovereign 5.24%, USD (90.1% US revenue), US Treasury daily par yield curve,
  2026-09-04
- [x] Value stated as a round-number range
- [x] One bar (screamer test); windage count ONE, stated
- [x] Price dated 2026-09-04, aggregator, flagged (run.py live quote)
- [x] Run committed to git after every question (write-early protocol; survived one
  session kill with zero question loss)

**DEFECTS CONFESSED:**
1. The brief's "owner earnings roughly tripled 2019-2025" did not reproduce: 2.2x
   ($72.0M → $160.5M) on the year-end constructions.
2. The brief's "gross margin has EXPANDED steadily" is loose: 40.7% (2021) → 38.9% (2022)
   → 41.7% (2025) — a dip and recovery; the five-year direction is up, the path is not
   steady, and the filed driver is mix, not price.
3. run.py defects, again: weighted-average share basis (29.6M vs 28,986,847 cover count)
   and a D&A read that takes depreciation only ($11.1M), silently excluding amortization —
   immaterial here because capex≈depreciation, material for any filer where they diverge.
4. The row sub-agent died in a session kill after writing ITRI/XYL/ROP; MWA rebuilt
   minimally by the lead session from the already-downloaded filing.
5. SBC for H1-2026 not separately transcribed (10-Q condensed line not pulled); H1 OE
   shown gross of it and displayed only, never averaged.
6. Earnings releases were not swept; the no-guidance finding is scoped to SEC filings.
7. The FY2021 10-K's AMI-conversion estimate was not captured before the session kill
   (regex missed the vintage's wording); the one-third → ~40% trend rests on the FY2023
   and FY2025 vintages only.

## REGISTER
- Verdict: **FAIL AT Q5, ON PRICE, at the [E4-28] floor — about the price, not the
  business.** Q1 IN · Q2 IN (NARROW) · Q3 IN (overlay, no disqualifier) · Q4 IN — the
  NINTH name in the queue's history to clear all four business gates (ACLS closed as
  eighth earlier the same day, found on the post-kill re-read of the queue), and the best
  business economics in the queue to date (~138% pre-tax on net tangible operating
  assets, zero debt, $0 interest paid).
- One line: **a genuinely great small business at a price that already capitalizes its
  best year ever and then some — every owner-earnings construction, including the record
  year, yields below the 30-year Treasury at $132.49.**
