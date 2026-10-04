# Company Run — Coca-Cola Consolidated, Inc. (COKE) — 2026-09-04
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

**The structural question this run was briefed to answer: WHOSE FRANCHISE IS IT?** COKE is
a bottler, not The Coca-Cola Company — it manufactures and distributes KO's products in a
licensed territory under comprehensive beverage agreements. The brief's declared prior
[E4-26]: Q2 OUT on the licence structure — with the confession that the margin record since
2016 is exactly what "no franchise" predicts cannot happen. Run straight; research in
`Test Runs/_research 2026-09-04 COKE/`.

**SCREEN ROW, REPRODUCED BEFORE ADJUDICATING** (queue row, `Screens/2026-09-02 MASTER RUN
QUEUE (corrected).csv` line 122): cap $13,794M · oe_bottom $455M · oe_top $684M · spread
50.4% · yield 3.30% · growth required 6.70% · level_shift 2.24 "STEP UP — normalize down
[E4-41]" · sovereign 5.27%.
- **oe_bottom 455 REPRODUCED to the million from the filed statements**: 5-yr (FY2021–25)
  mean of OCF − capex = (521.8−155.7 + 554.5−298.6 + 810.7−282.3 + 876.4−371.0 +
  931.9−312.3)/5 = 2,275.4/5 = **$455.1M**. (SBC is zero in every year of the window —
  COKE's incentive comp is cash-settled; the last stock-comp line in a filed cash-flow
  statement is $2.0M in FY2019.)
- **oe_top 684 reproduced within tag noise, and the tag is WRONG**: 3-yr mean of OCF −
  D&A. The tool took D&A of 177/194/195 for FY2023/24/25 — the 2023 and 2024 figures
  include intangible amortization, the 2025 figure does not. Filed totals (D&A from PP&E
  and financing leases + amortization of intangibles and deferred proceeds): 177.0/193.8/
  218.5, giving a corrected top of **$676.6M**, not 684. Same first-tag-pick defect family
  as MCD/HAS. Immaterial to any verdict (1.1%); logged as a tool defect below.
- spread (684−455)/455 = 50.3% ≈ 50.4% ✓ · yield 455/13,794 = 3.30% ✓ · growth required
  10% floor − 3.30% = 6.70% ✓ (the row's cap is 66,564,294 shares at ~$207, the 2026-09-01
  quote; today's quote is lower — see Step 0).
- **level_shift 2.24 STEP UP is real and is the run's [E4-41] question**: OE at the capex
  end went $119M (FY2019) → $505M (FY2024) — roughly a quadrupling over five years —
  and the whole of Q4 turns on how much survives normalization.
- **The acquisition flag's NET CASH INFLOW, established from the filing as the brief
  ordered**: `PaymentsToAcquireBusinessesNetOfCashAcquired` for FY2018 is **−$456
  thousand** — an inflow — on the line "Acquisition of distribution territories and
  regional manufacturing plants, net of cash acquired **and purchase price settlements**"
  (FY2018 10-K, acc 0001564590-19-005000). The FY2019 10-K's business-combination note
  states: "Measurement period adjustments relate to post-closing adjustments made in
  accordance with the terms and conditions of the applicable asset purchase agreement or
  asset exchange agreement for distribution territories acquired or exchanged by the
  Company in April 2017 and October 2017 as part of the System Transformation. All final
  post-closing adjustments for these transactions were completed during 2018." **No
  business was acquired for negative consideration; the 2017 System Transformation
  true-ups (working-capital and purchase-price settlements received from CCR) exceeded
  residual payments in fiscal 2018 by $0.456M.** The tag is zero from FY2019 onward; no
  acquisition sits inside any owner-earnings window. Flag closed.

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
- rate **5.25%** (30-yr) · date **2026-09-03** · source **US Treasury daily par yield curve,
  issuing authority** (20-yr also 5.25%). The screen's 5.27% was the 2026-09-01/02 print;
  both are carried where they appear.
- FX: none — USD quote, USD earnings. No ADR.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- documents: **10-K FY2025, filed 2026-02-18, period 2025-12-31, acc 0001628280-26-009057**
  (primary); 10-Q Q2-2026, filed 2026-08-05, period 2026-07-03, acc 0001628280-26-053370;
  DEF 14A 2026, acc 0001628280-26-020505; 10-Ks FY2023/FY2022/FY2021/FY2019 for the series
  (accessions in the research extraction file).
- figure cross-checked against the filed statement: **OCF FY2025 $931,904k** read off the
  consolidated statement of cash flows in coke-20251231.htm matches the tool's XBRL read
  ($931.9M); **oe_bottom $455M reproduced to the million** from five filed OCF/capex pairs
  (see screen block above).

**STAGE 0(b) — the hand checks the brief ordered:**
- **Share count, TWO CLASSES, off the cover by hand**: Q2-2026 10-Q cover (2026-08-05):
  Common **56,517,334** · Class B **10,046,960** · total **66,564,294**. `cover_shares.py`
  agrees. `run.py`'s 9.4M/$1.86bn cap is the known weighted-average one-class defect
  (10-for-1 split 2025 compounds it) — discarded.
- **Economic equivalence, from the charter/filings**: Class B has 20 votes vs Common's 1;
  Class B converts 1:1 into Common; dividends on Common must equal or exceed Class B's
  (the FY2025 10-K equity statements show identical per-share dividends both classes,
  2023–2025; the 2023 declaration was "$0.50 per share on the Common Stock and the Class B
  Common Stock", one rate). Basic EPS differs by pennies only through two-class-method
  allocation (6.82 vs 6.78 in 2025). **Judged economically equivalent for the cap; both
  classes summed.** Class B is the Harrison family's control instrument: J. Frank Harrison
  III controls 10,043,940 B shares ≈ **78% of total voting power** (right to exchange into
  2,923,860 more → ~83%) — recorded at Q2/Q3, priced nowhere.
- **Price**: **$197.40**, 2026-09-03, aggregator quote, flagged as such. **Market cap =
  66,564,294 × $197.40 = $13,140M.** (Screen row's $13,794M was the ~$207 print of
  2026-09-01; the stock fell ~5% between screen and run.)
- **Dividend record (the WEYS regular-vs-special test)**: regular quarterly dividend held
  at $0.25/sh pre-2023 equivalent ($9.37M/yr paid 2019–2022), then **raised** (Dec 2023
  declaration: $0.50/q pre-split) — plus **specials**: $3.00/sh (2023), **$16.00/sh
  special paid 2024-02-09** (~$155M, pre-split). Cash paid: 9.4/9.4/9.4/9.4/46.9/185.6/86.7
  ($M, 2019→2025). The payout is episodic and small against owner earnings; the 2024-25
  capital-return event was the **buyback**, not the dividend. No dividend-funded-by-issuance
  flag [E2-52]: share count only ever falls.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: COKE buys concentrate from
  Atlanta at a price that moves with COKE's own realized selling prices (the incidence
  agreement), buys cans, bottles, sweetener and CO2 on the commodity market (~20% of COGS
  ex-concentrate), mixes and packages the drinks in its own plants, trucks them on its own
  vehicles to every grocery, club, convenience store and vending machine across fourteen
  Southeast/Mid-Atlantic/Midwest states (~60 million consumers), stocks the shelf itself,
  and keeps the difference between the shelf price and all of that. In FY2025 that
  difference was $18.68 a case gross of selling costs, on 354 million cases: a 39.7% gross
  margin, a 13.2% operating margin. It also pays Atlanta a quarterly sub-bottling royalty
  (~$69M in 2025, contracted through the ~40-year life of the acquired territories) for the
  exclusive licence itself. One business, one segment, one country, one currency.
- The scarce input this business controls: **the exclusive territory licence plus the
  route density built on it** — the only legal seller of the world's strongest beverage
  brand across its territories, delivered through a DSD network (trucks, warehouses,
  cooler placements, shelf relationships) that took decades and billions to build. The
  brand itself is NOT controlled — it is licensed, terminable on default, and its
  concentrate price is set by the licensor. That split is Q2's whole subject.
- Will the fundamentals look broadly the same in ten years? Yes in structure: Americans
  will still drink branded nonalcoholic beverages, KO will still route them through
  bottlers, DSD will still put them on shelves. The mix shifts (Still growing, Sparkling
  flat; ARTM nibbling at the DSD share for post-mix and some bottle/can) but the
  fundamental machine is stable in character [E3-31].
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**THE STRUCTURAL QUESTION FIRST — WHOSE FRANCHISE IS IT?**

**The licence terms, from the filings, verbatim where it matters:**
- **Duration**: "The Final CBA has a term of ten years and is **renewable by the Company
  indefinitely** for successive additional terms of ten years each unless earlier
  terminated as provided therein." (8-K, 2017-04-04, acc 0001193125-17-108876.) **The
  renewal option sits with Charlotte, not Atlanta** — perpetual in practice, terminable
  on "customary termination and default rights" (FY2019 10-K). This is the decisive
  structural difference from QCOM (QTL licences expire fiscal 2027–2031) and AATC: there
  is no expiry wall. The licence dies by DEFAULT (failing minimum capex or minimum volume
  requirements — FY2025 10-K Item 1A: "Failure to satisfy these requirements could result
  in the loss of distribution and manufacturing rights"), not by the calendar.
- **Pricing mechanism — what incidence pricing means for the bottler's margin**: the
  incidence-based pricing agreement "establishes the prices charged by The Coca-Cola
  Company to the Company for (i) concentrates... Under the incidence-based pricing
  agreement, the prices charged by The Coca-Cola Company are impacted by a number of
  factors, including **the incidence rate in effect, our pricing and sales of finished
  products, the channels in which the finished products are sold [and] the package mix**...
  The Coca-Cola Company has **no rights** under the incidence-based pricing agreement **to
  establish the prices... at which we sell products**" (FY2025 10-K, Item 1). So:
  concentrate cost is a roughly proportional royalty on COKE's own realized revenue —
  when Charlotte raises the shelf price, Atlanta's concentrate revenue rises with it
  automatically, and the incidence RATE itself is Atlanta's long-run lever. Charlotte
  keeps the spread; Atlanta cannot set Charlotte's price, Charlotte cannot set Atlanta's.
- **The second royalty**: quarterly sub-bottling payments to CCR "on a continuing basis"
  for the System Transformation territories — $68.9M (2025) / $64.3M (2024) / $28.2M
  (2023), liability $717.9M at FV, running through the ~40-year life of the distribution
  assets, resized upward as territory cash-flow projections rise. Atlanta shares directly
  in the acquired territories' gross profit growth.
- **The cage**: exclusivity runs BOTH ways but the covenants run one way — COKE may not
  handle any non-KO beverage without consent (Ancillary Business Letter), must make
  minimum ongoing capex in distribution AND manufacturing, must meet minimum volume, needs
  KO approval to sell the company or the business, and RMA prices for inter-bottler/CCNA
  sales are "unilaterally established" by Atlanta. Strategic freedom is licensed away.

**WHO CAPTURED THE PRICE INCREASE — the ten-year gross-margin series answers it**
(all filed; FY2019/FY2021/FY2023/FY2025 10-Ks; full table in the research extraction):

| FY | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Gross margin % | 35.1 | 33.6 | 34.6 | 35.3 | 35.1 | 36.7 | 39.1 | 39.9 | **39.7** |
| Op margin % | 2.4 | 1.3 | 3.7 | 6.3 | 7.9 | 10.3 | 12.5 | 13.3 | **13.2** |

Through the 2022–2024 industry pricing wave COKE's gross margin EXPANDED ~460bp
(35.1 → 39.7). Under incidence pricing Atlanta's concentrate take rises proportionally
with realized price — so proportional pass-through would hold GM% roughly flat.
It did not stay flat. **Charlotte kept the wave and more**: gross profit per case
$5.34 (2021) → $8.11 (2025), +52%, faster than price per case (+40%). Payments to KO
(concentrate etc., ex sub-bottling): $2,019M → $2,110M → $2,264M (2023–25) — +12.1%
over two years against +9.4% bottle/can revenue: Atlanta's take grew roughly in line,
not ahead. **The answer to the brief's question is BOTH — proportionally Atlanta,
incrementally Charlotte.** The margin tripling (op margin 2.4% → 13.2% since 2017) is
half gross-margin capture, half SD&A leverage (30.9% → 26.6% of sales).

**[E4-55] — the unit series, the cleanest in the queue as briefed** (standard physical
cases, bottle/can; absolute cases first filed for FY2020):

| FY | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1-26 adj |
|---|---|---|---|---|---|---|---|
| Cases (M) | 358.8 | 366.0 | 362.2 | 355.4 | 353.1 | 354.0 | **+7.1%** |
| $/case | 12.27 | 13.34 | 15.30 | 17.00 | 17.94 | 18.68 | + |

Nominal price per case +52.2% over five years (CPI-U ≈ +23%: **real price/case ≈ +24%**)
against cumulative volume of **−1.3%** (−3.3% from the 2021 peak, stabilized 2024, up 0.3%
in 2025, **+7.1% adjusted in H1-2026** — six extra days excluded, filer's own adjustment).
*Vintage caveat, recorded: the case metric is re-measured between filings (the FY2022 10-K
filed 2022 as 366,115 — FLAT vs 2021 — where the FY2023 10-K re-bases it to 362,191, with
the filer's standing note that re-measurement differences are "not material"). Within-
filing comparisons are consistent-metric; the cross-vintage stitch carries ~1% noise, and
on the original vintages volume was flat through 2022, making the wave-era decline
SMALLER, not larger.*
2019's +1.6% was the last pre-metric-change year. **[E2-44](1) passes on the filed
record**: prices were raised hard for four consecutive years, demand flattened but did
not leave, and volume is now growing on top of the higher price level. Set beside the
precedents: PEP took ~+33% FLNA pricing and volume fell ~6% cumulative with segment
margin DOWN 530bp; TGT's nominal ticket FELL three straight years; MCD's US real comps
ran negative for twelve. **COKE is the first name in this queue whose physical series
holds through its own pricing wave while gross margin expands.** [E2-44](2) fails,
however: dollar growth requires real capital (capex 2.3x D&A in 2024–25; NTOA rising) —
recorded honestly at Q4.

- Needed or desired **[x]** (the licensed brands are the strongest in the category) ·
  no close substitute **[x] at the consumer level for the brand; [ ] NOT at the retail
  shelf** (PEP/KDP bottlers compete on every aisle; Item 1: "The nonalcoholic beverage
  industry is highly competitive... Our principal competitors include local bottlers of
  PepsiCo, Inc. products and, in some regions, local bottlers of Dr Pepper products") ·
  not price-regulated **[x]** (retail free; input price licensor-set)
- Must the moat be continuously rebuilt? **No — [E4-04]'s excluded class this is not.**
  The advantage is territory exclusivity plus DSD route density; the required spending
  (minimum capex, fleet, automated DCs) DEFENDS the same advantage rather than buying a
  replacement. It is contractually mandatory defence — a moat with a maintenance covenant
  attached. Does success depend on a great manager? The 2017–2025 margin rebuild was
  execution, but the licence, the territories and the density survive any CEO [E4-23];
  key-person dependence is NOT the defect here. The defect is that **the moat's title
  deed is Atlanta's brand**, held on a perpetual-at-the-bottler's-option lease.
- Primary moat metric, filing-sourced, and its trend: **return on unleveraged net
  tangible operating assets [E2-43]: 49.4% (FY2024), 48.4% (FY2025)** (NTOA $1,862M /
  $1,963M vs OI $920.4M / $950.7M — computation in the research file; treating the $74.9M
  current portion of contingent consideration as debt-like moves it ~1pt, flagged), on
  gross margin held ~39.7-39.9% two years running. Trend: high and stable; H1-2026 GM
  −125bp on tariff aluminum — pass-through lagging input spikes, not a structural break,
  but pre-committed for re-read at Q6.

**THE COMPETITOR ROW — required [E3-28].** Six external rows, filing-sourced (full tables
with accessions in `_research 2026-09-04 COKE/competitor row - bottlers CCEP PRMB KOF.md`
and the PEP run's KO/KDP file; the original row sub-agent was lost to a session kill and
the row was rebuilt minimally by this run):

| Filer | FY | Op margin | GM | structure |
|---|---|---|---|---|
| **COKE (subject)** | 2025 | **13.2%** | **39.7%** | licensed KO bottler, USD |
| CCEP | 2025 | 13.4% | 35.6% | licensed KO bottler, EUR/IFRS (11.0→13.4% over 5 yrs) |
| KOF | 2024 | n/a (tag gap) | 46.0%* | licensed KO bottler, MXN (*IFRS cost classification — not level-comparable) |
| PRMB | 2024 | 11.5% | n/a | own-brand US bottler; FY2025 impaired to a loss |
| PEP PBNA segment | 2025 | ~11.7% core | n/a | owned bottling (PEP run) |
| KDP | 2025 | 21.5% | n/a | brand owner + bottler blended |
| KO (licensor) | 2025 | 28.7% (31.5% on NTOA) | n/a | concentrate/brand economics |

- Peers named: **6** of the industry's ~6–8 real comparators reachable from SEC filings
  (Arca Continental and Swire do not file with the SEC — named as the missing rungs;
  their absence does not change the class, because the licensed-bottler economics are
  already bracketed by CCEP and KOF).
- What the row shows: COKE's operating margin sits at the TOP of the pure-bottler set
  (13.2% vs CCEP 13.4% — level; PBNA ~11.7%; PRMB 11.5%) with the highest US GM, and
  its **48.4% return on unleveraged net tangible operating assets [E2-43] exceeds even
  the licensor's 31.5%** — though KO's number carries $28bn of intangibles outside the
  NTOA base and the two businesses are not the same claim. Peer NTOA for the IFRS
  filers was NOT computed (stated gap); the [E2-43] cross-check rests on KO/KDP.
- **The row's limit [E3-61], stated**: identical licence structures produce different
  outcomes (CCEP's five-year margin path 11.0 → 13.4% resembles COKE's rebuild; PBNA
  under the SAME beverage wave went nowhere) — the row shows position, not conduct,
  and conduct is where COKE's record was made.
- Row class impact: the licensed-KO-bottler model earns 11–13.5% operating margins
  everywhere it files; COKE is at the top of that band, not outside it. **What is
  COKE-specific is the return on tangible capital and the pricing-with-volume-held
  conduct; what is generic is the band itself — the moat's ceiling is set in Atlanta.**
  Consistent with NARROW, inconsistent with WIDE.

- **Untapped pricing power [E3-33]**: no — the pricing lever has been pulled annually
  since 2021 (+52% cumulative); this is USED pricing power, with [E4-37]'s inverse metric
  benign so far (annual Q1 pricing actions executed without visible agony, volume
  positive in H1-2026). The class claim is NOT near-monopoly [E5-28] at the shelf — it is
  exclusive supply of the leading brand within a territory.
- **[E2-45] the attacker's test**: to compete with COKE inside its territories you would
  need (i) a comparably desired brand portfolio — there are exactly two, and both (PEP,
  KDP) are already distributed there by incumbent systems; (ii) a DSD network of ~14
  states' density — Walmart/Kroger (36% of volume) could vertically integrate
  distribution (ARTM is the thin end: <10% of bottle/can volume, two-thirds of post-mix
  gallons, fees preserved to COKE by exclusivity), but cannot replicate the licence;
  (iii) Atlanta itself is the only real attacker — it repurchased and refranchised these
  territories once (2013–2017) and could only re-take them on COKE's default. **The
  strongest attacker holds the brand, and it just sold its entire equity stake to the
  bottler (Q4 2025) rather than deepen it.**
- Class: **[x] NARROW** — a real franchise at the bottler level (exclusive perpetual-
  at-its-option territory licence on the category's strongest brand, route density, filed
  pricing conduct, ~48% returns on tangible operating capital), narrow because the
  licensor holds the incidence-rate lever and a gross-profit-linked royalty above it,
  the covenants cage strategy, and shelf competition is unlicensed. · Direction: stable
  units improving (H1-2026 +7.1%), margin flat-to-slightly-narrowing (tariff aluminum).
- **VERDICT: [x] IN — class NARROW.** The brief's declared prior (Q2 OUT on the licence
  structure) is **REFUTED by the filed record [E4-26]**, exactly along the line the brief
  itself flagged as the likely error: (i) the licence has no expiry wall — renewal is
  indefinitely at the BOTTLER's option, the anti-QCOM/anti-AATC structure; (ii) the
  ten-year gross-margin series shows the bottler KEPT the pricing wave (GM 35.1 → 39.7%
  through it) rather than passing it upstream; (iii) the unit series held through +52%
  nominal pricing and is growing again; (iv) returns on tangible operating capital are
  ~48%, top of the row. NARROW, not WIDE, because the ceiling is Atlanta's: the
  incidence rate, the RMA prices and the sub-bottling royalty sit above the bottler,
  the covenants cage its strategy, and [E3-03](2) holds only at the brand level, not at
  the shelf.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Case declared, and why: DSD execution is
daily-intensive operationally, but [E3-43]'s test is whether the BUSINESS can be killed by
poor management — a Q2-NARROW franchise with territory exclusivity tolerates mediocrity
(the 2017–2019 filings, 1.3–3.7% operating margins under the same licence, are the
on-record proof that it survives being run badly). Leverage after the Repurchase is real
($2.79bn debt, negative book equity) but asset-error magnification is nothing like 20:1
(gross interest coverage ~9x). **OVERLAY — with one caveat recorded: the Harrison family's
78% voting control means no outside reaction is possible on ANY horizon; what the family
does with the cash is the whole Q3 question for a minority holder.**

**Honesty — binary, permanent, filings-based [E5-16].** No integrity matter found in the
filings read (FY2019–FY2025 10-Ks, 2026 proxy, Q2-2026 10-Q): no restatement, no SEC
enforcement, no clawback event under the 2023-adopted recovery policy, no related-party
self-dealing beyond disclosed system agreements. The largest related-party event — the
$2.4bn Repurchase of KO's entire stake, with Harrison personally a party to the
agreement — was disclosed with price ($127.00/sh), counterparty and terms. **No
disqualifier found.**

**STEP 2 — THE FLAGS [E4-22, E5-15].** *Each a prompt to read, never a verdict.*
- [ ] weak accounting — none found; pension terminated 2022/settled 2023, disclosed
- [ ] unintelligible footnotes — the opposite: the contingent-consideration note is a
  model (Level-3 roll-forward, WACC driver, payment guidance $50–70M/yr)
- [ ] trumpeted earnings projections — **COKE gives no earnings guidance at all**; the
  only forward number in the MD&A is capex (~$300M). [E5-30]'s ratchet never started.
- [ ] serial share issuance — the inverse: 29% of the company retired in eighteen months
- [ ] EBITDA promotion [E4-29] — does NOT fire: pay runs on EBIT (D&A in), "EBITDA"
  appears once in the 10-K, inside the goodwill-impairment-test methodology, zero in the
  proxy's incentive metrics
- [ ] filed-figure tells [E4-30] — cash taxes 25.4%/26.1%/36% of pretax (2025/2024/2023),
  not falling; reported growth is lumpy (MTM swings), not smoothed
- [x] **pay-design flags, three, recorded**: (i) FY2025 annual-bonus EBIT target $922.0M
  was set at FY2024 actual ($920.4M) + 0.2% — a low bar, paid at 127.9%; (ii) a uniform
  1.24 "individual performance factor" applied to every NEO — discretionary multiplier,
  same number for all; (iii) LTPP maximum payout raised 150% → 200% in 2025 "to remain
  competitive with the market" — the ratchet direction. Against them: the metrics are
  GAAP-anchored (EBIT = income from operations, as adjusted; adjustments itemized in
  Appendix A), the committee's adjustment policy excludes buyback/financing effects from
  operating goals, and the 2023 LTPP paid its 150% max on EBIT achieved 28% OVER target —
  earned, not rigged. The DG/ULTA rigging pattern does NOT replicate.

**STEP 3 — THE PRIMARY TEST [E2-01].** Book equity is NEGATIVE (−$739.7M) after the
Repurchase — ROE is meaningless from FY2025 on, which [E2-43] anticipates: use
unleveraged net tangible operating assets. **OI/NTOA: 49.4% (FY2024), 48.4% (FY2025)**;
pre-buyback ROE for context: 17.2% (2021), 38.6% (2022), 28.4% (2023), 44.7% (2024) on
year-end equity. No accounting gimmickry found in the numerator; the denominator shrank
by choice (leveraged buyback), stated at Q4.

**The half-owner test [E2-26]:** passes. Price-vs-volume attribution in dollars every
year; the ARTM shift and its revenue-vs-volume accounting asymmetry explained unprompted;
specials labeled specials; the KO Repurchase disclosed with every term; the MTM line kept
OUT of operating income and reconciled. Adjusted (non-GAAP) net income is presented
beside GAAP with itemized bridges.

**The institutional imperative [E2-30]:** none of the four fire. No empire acquisitions
(zero business acquisitions since 2018); funds NOT soaked up — returned ($3.5bn in
2024–25) or repaid ($425M of term loans within eight months of drawing); no imitation of
peer M&A (contrast KDP/JDE Peet's, PEP's serial deals).

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? **Yes, narrowly** — $282M cash + $500M
  undrawn revolver retained at close ([E5-39] refuses to count the revolver; the cash
  plus $930M/yr OCF covers the $100M 2026 maturity and capex several times over).
- (2) repurchases at a material discount to conservatively calculated IV? **The FY2025
  average was $126.3/sh (20.6M shares, $2.61bn) against this run's zero-growth-at-the-
  sovereign band of ~$115–180 (judged ~$145, Q5 below)** — bought at ~13% under the
  judged zero-growth value, at a 5.6% owner-earnings yield on judged OE, above the bond.
  **Condition 2 PASSES on this run's own conservative numbers** — the first buyback in
  this queue's eighteen files bought below judged value (anti-ORLY, anti-MCD pattern).
  The borrowing that funded it is licensed by the discount [E4-50] — "the discount does
  the licensing" — and the discipline test was passed in real time: **the authorization
  was REDUCED $1bn → $400M on 2025-11-07** (the board shrank its own program as the
  price rose toward value) and H1-2026 repurchases were zero at $150–200.
- **[E4-31]'s third condition** (an informed register): the run notes the sellers were
  KO itself and public holders under a standing program, with the CC-liability and
  volume data all filed. No information asymmetry finding.

**Item 402(v) pay-versus-performance, transcribed:** TSR on $100 (2020-12-31 base):
**$602.04 (COKE) vs $128.37 (peer group: KDP, FIZZ, KO, PEP)** at FY2025 — the stock
six-folded while the licensor-and-peers basket gained 28%. CEO CAP over the same five
years: $13.5M → $14.7M → $18.7M → $19.0M → $15.3M — pay did NOT scale with the six-fold;
the [E3-59] "how well they treat their owners" read and the [E3-54] retention test both
pass trivially on this record (market value added is a large multiple of the ~$1.6bn
retained over five years). **[E4-52] convergence check: the three pay flags do not
converge with any accounting or disclosure flag — no lollapalooza.**
- [x] Nothing here promotes the name — Q2's class and Q4's numbers stand on their own
  [E2-37, E2-38, E3-39].
- [x] The business does not require a great manager (Q2: the licence and density survive
  any CEO [E4-23]); the margin rebuild was execution on an intact franchise.
- [x] No manager-is-the-plan reasoning anywhere in this file [E2-35, E2-36].

- **VERDICT: [x] IN (overlay)** — no disqualifier found; three pay-design flags and the
  family-control caveat recorded. *NOT a finding that the managers are honest [E5-17];
  IN never promotes.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**THE CONSTRUCTION, stated first.** OE = OCF − SBC − (c), per the framework CONVENTION —
**plus one COKE-specific subtraction this run adds and confesses: the quarterly
sub-bottling payments to CCR** ($39.1/36.5/28.2/64.3/68.9M, FY2021–25). They are a
recurring, gross-profit-linked payment for the licence itself, contracted through ~2057,
guided at $50–70M/yr — economically a royalty, but CLASSIFIED as financing (contingent
consideration), so OCF never sees them and the screen's numbers silently exclude them.
Subtracting the payments and NOT also deducting the $717.9M liability from the valuation
is the one-or-the-other choice made here (both would double-count); **windage count: this
is conservatism spend #1.**

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
- OE by year, capex end / D&A end ($M): 2021: 318.0 / 302.1 · 2022: 188.8 / 346.4 ·
  2023: 500.2 / 605.5 · 2024: 441.1 / 618.3 · 2025: 550.7 / 644.5
  (capex end also subtracts distribution-rights purchases: $9.0M 2021, $30.6M 2022 —
  BODYARMOR rights; D&A end = OCF − full filed D&A incl. intangible amortization − CC
  payments)
- **Short-window mean** (3-yr, FY2023–25): **$497M** (capex end) · $623M (D&A end)
- **Long-window mean** (5-yr, FY2021–25): **$400M** (capex end) · $503M (D&A end)
- **Spread, conservative end:** 24.3% between windows; **combined range $400M–$623M**
  (width 55.7% on the bottom)
- Too wide to conclude? **No — for the Q5 question it does not matter: the ENTIRE range
  sits below the sovereign yield at today's cap** (3.0%–4.7% vs 5.25%), the ORLY
  precedent exactly. The capex band cannot change the verdict, so UNKNOWABLE does not
  fire.
- The distorted years, named [E5-11]: FY2021–22 carry the pre-rebuild margin structure
  AND the 2022 capex surge ($298.6M + $30.6M rights); FY2023 is the pricing wave's big
  step (OCF +46%). The 5-yr mean averages two margin regimes — displayed, not blended
  into the judgment (the ACMR/ALKT rule).
- **[E4-41] — the step-up decomposed, as the brief ordered. The screen's STEP UP (2.24x)
  is real: OE quadrupled FY2019→FY2024.** How much is durable?
  (i) *The margin rebuild* (SD&A 30.9% → 26.6% of sales; ARTM post-mix conversion; DC
  automation; the FY2018–19 cost base was the System Transformation hangover) — durable
  in character, and management-guided capex keeps buying it.
  (ii) *The industry pricing wave 2022–24* (+52% $/case over five years vs ~+23% CPI) —
  the part PEP just failed on. COKE's own filed evidence says the LEVEL is holding:
  volume −1.3% cumulative over the whole wave, positive in 2025, **+7.1% adjusted in
  H1-2026 with pricing still positive** — no negative-pricing quarter anywhere in the
  filed record, against PEP's H1-2026 −2%.
  (iii) *What does NOT survive normalization*: the H1-2026 gross margin is already
  −125bp on tariff aluminum, and a real-price giveback toward CPI would take gross
  margin back toward ~37% ≈ −$190M of OE.
  **Judged OE: $500M** — the 3-yr capex end (497), i.e. the recent margin structure at
  the FULL capex end with the royalty subtracted, NOT the D&A end and NOT the boom-top
  single year (2025's 550.7). A reversion case of ~$400–450M and the D&A-end case of
  ~$620M bound it. **This normalization-down is windage spend #2 — justified in writing:
  [E4-41] requires naming and removing favourable exogenous breaks (the 2022–24 industry
  pricing wave is one), and the sub-bottling subtraction (#1) is a classification
  correction, not conservatism stacked on the same number.**
- **Maintenance capex — the disclosed judgment.** Which case: **the [E5-20] question was
  put to the filing and the filing answers it directly — the CBA and RMA CONTRACTUALLY
  REQUIRE "minimum, ongoing capital expenditures" in both the distribution and
  manufacturing businesses** (FY2025 10-K Items 1 and 1A: failure "could result in the
  loss of distribution and manufacturing rights"). A licence whose survival requires
  capex makes the D&A end structurally optimistic: capex has run 1.6–2.2x PP&E
  depreciation (312/195, 371/170), guided ~$300M for 2026, with no maintenance/growth
  split disclosed in any vintage read. (c) is judged **at total capex** (the capex end),
  with the D&A end displayed as the optimistic bound only. [E4-47] reinforces: trucks,
  coolers and automation replace at inflated prices against depreciation charged on old
  dollars.
- Stock compensation subtracted in full [E5-06]: **there is none to subtract** — no SBC
  line in any cash-flow statement FY2020–FY2025; incentive comp is cash-settled and
  already inside OCF via accrued compensation (the CEO's equity-plan award was elected
  in cash; last filed SBC was $2.0M in FY2019).

### Great, good, or gruesome? **[E4-20]**
- [x] **good** — a ~48% return on net tangible operating assets, but dollar growth
  requires added capital (capex 2.3x depreciation at the 2024–25 pace, $30M+ of
  distribution-rights purchases when brands are added) and the licence obliges the
  reinvestment. Not great (the added capital earns well but MUST keep being added under
  covenant; the licensor shares the growth via incidence + sub-bottling); nowhere near
  gruesome ([E4-43]: the good class passes).

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **pass** — an essential-consumable at 39.7%
  gross margin that grew net sales through 2008–09, 2020 and every year since 2017.
- (2) massive liquid assets: **FAIL** — $171.7M cash at H1-2026 against $2.5bn debt and
  negative book equity; the $500M revolver is not counted [E5-39]. This is a CHOSEN
  posture (the Repurchase) being unwound at speed ($425M of term loans repaid within
  eight months of drawing), but as scored today it fails.
- (3) no significant near-term cash requirements: **pass** — 2026 maturities $100M (Oct)
  against $171.7M cash + ~$930M OCF; the real wall is the $900M Three-Year Term Loan due
  2028-12-08, addressable by ~two years of retained OE at the judged level, and
  management is visibly prepaying. No commercial paper. Covenants exist on the bank debt
  (fixed-charge and leverage ratios, "in compliance"); the public bonds are
  covenant-light.
- Leverage, named and quantified [E4-16, E3-29]: total debt $2,786M at FY2025
  ($2,511M at H1-2026 after prepayments) + $717.9M contingent consideration at fair
  value + $121M lease liabilities, against judged OE ~$500M and gross interest $102.9M —
  **~5x judged OE at the peak, coverage [E2-54] = OCF before interest ≈ $1,035M vs
  interest+accrued ~$103M ≈ 10x, comfortably met "out of current cash flow net of ample
  capital expenditures" ($1,035 − 312 − 69 = $654M vs $103M ≈ 6.3x)** — zip-up-the-wallet
  does not fire; the leverage is a 2025 event, not a structure.
- **[E2-60] restricted earnings — FIRES for the FY2024–25 window and is answered in the
  file**: distributions + buybacks of ~$3.50bn against ~$0.99bn of capex-end OE over the
  two years, funded by +$1.55bn of net new debt and the liquidation of the cash pile —
  financial strength (the third maintenance dimension) was spent, by choice, on retiring
  29% of the shares. The [E4-50] counterweight applies (the discount licenses the
  borrowing — repurchases at ~$126 vs judged ~$145 zero-growth value) and the payout is
  NOT a run-rate: H1-2026 buybacks were zero and $425M of the loans are already repaid.
  Fires, recorded, judged non-structural.
- **Software capex (the HAS fix, checked)**: no separate software-development cash-flow
  line exists; internal-use software is capitalized inside PP&E additions and its
  amortization ($1.1M in 2025) is inside depreciation — immaterial here, no OE
  correction needed.
- ASC 842 (the standing check): finance leases $1.7M liability — **immaterial again**;
  operating leases $119.5M total liability, 10-K discloses related-party leases
  separately. Included in (c) by construction (rent inside OCF).

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: **the licensor's lever, pulled while the balance sheet is stretched.**
  Atlanta cannot take the territories (the renewal option is Charlotte's) but it owns
  every economic dial above the bottler: the incidence rate, the RMA transfer prices,
  the sub-bottling royalty resized on territory cash flows, brand/marketing funding
  ($209.5M in 2025, "generally do not obligate such funding"), and consent over any
  sale or diversification. The system precedent is filed history: KO's 2000s concentrate-
  price escalation against CCE ended with CCE's equity gutted and KO buying the North
  American bottler in 2010 — the very territories COKE then re-acquired. **And KO's
  equity alignment with COKE holders ended 2025-11-07 — it now profits from COKE only
  through the dials.**
- Quantified from filed figures: claw back the whole 460bp gross-margin capture
  (2021→2025) via incidence/royalty escalation on $7.23bn of sales ≈ −$330M pre-tax;
  judged OE falls ~$500M → ~$170M; interest ~$103M is still covered ~2.6x on
  OCF-before-interest arithmetic, but equity value at the sovereign falls toward
  ~$3bn — **a valuation death, not a solvency death** (the HAS shape), unless it lands
  simultaneously with a volume shock (GLP-1-class demand break: Sparkling −10% ≈
  −$425M revenue ≈ −$170M gross profit) AND the 2028 refi. All three at once is the
  solvency case.
- Likelihood: [x] **a real possibility** (the lever exists, the precedent is in the
  system's own history, the incidence agreement's rate is Atlanta's to move over time) —
  though the observed conduct runs the other way: through the largest pricing wave on
  record Atlanta took proportionally, not incrementally, and it sold its stake back to
  the family at $127.
- **VERDICT: [x] IN** — earnings reliable at the judged level, coverage ample, deaths
  named and survivable singly; the [E5-11](2) fail and the 2028 wall are recorded and
  monitored at Q6, not fatal today.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: **~8–9% judged (range ~6% to ~9.7%)**. Below roughly 10%,
the name is not ranked — it is
quit on, whatever the sovereign is. Above it, rank, and capital goes to rank #1 [E3-45].
**No risk premium in the discount rate [E3-42]** — certainty lives at Q1 and in Bar 1's
end discount, never in the rate.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings **$500M judged ($400–623M range)** ÷ market cap **$13,140M** =
  **3.81% (range 3.04%–4.74%)** · sovereign **5.25%** — **below the bond on every
  construction, including the D&A-end optimistic bound.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- growth needed to justify the quote at the bare sovereign: **≈ +1.5%/yr perpetual** on
  judged OE (range +0.5% to +2.2%) — achievable and the strongest thing sayable for the
  price; growth needed to clear the ~10% floor: **≈ +6.2% to +7.0%/yr perpetual**, which
  faces [E4-35]'s base rate (fewer than 1-in-20 of the best businesses sustain 15%; a
  6–7% PERPETUAL claim on a flat-unit bottler carries the burden of proof and cannot
  carry it — units −1.3% over five years; the H1-2026 +7.1% is one adjusted half).
- what the business has actually done: revenue +5.3%/yr (FY2017–25), volume ≈ 0%/yr,
  OE growth 2019→2024 a one-time rebuild [E4-41], not a rate.

**3. WHAT YOU ARE PAID**
- return at the current price = **−1.4 points UNDER the sovereign** (range −2.2 to −0.5).

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.25%** (US Treasury 30-yr par, 2026-09-03) — **the bare rate, no
  per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support:
- **Zero-growth at the sovereign (5.25%): ~$115 – $180 per share, judged ~$145.**
- **At the ~10% floor [E4-28]: ~$60 – $95 per share, judged ~$75.**
- **Current price $197.40** (2026-09-03, aggregator, flagged) — **above the entire
  zero-growth band at the sovereign.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: **honest pre-tax expectancy 3.8% yield + ~4–5% honest nominal
  growth ≈ 8–9% at the judged center (conservative construction ~6%, optimistic ~9.7%)
  vs ~10% [E4-28] — BELOW THE FLOOR ON EVERY CONSTRUCTION → quit on, and the ranking
  lines are not filled in.** *"That's the figure we quit on."*
- *(For the record only: at the buyback prices of FY2025 — $121–127 — the same arithmetic
  gave 5.6% yield + 4–5% ≈ 9.5–10.5%, which is the floor's edge; the board's own program
  cut at $400M says they saw the same line.)*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [x] **Screamer test [E4-01]** — does the price already clear the conservative case?
      **Price $197.40 sits ABOVE the whole zero-growth range ($115–180) → outcome three:
      no.** No margin added on top; no useful conclusion needed beyond it.
- **Windage count: 2, justified in writing at Q4** — (1) the sub-bottling royalty
  subtraction (a classification correction confessed as a construction choice; the
  alternative books the $718M liability against the valuation instead), (2) the [E4-41]
  normalization to the 3-yr capex end rather than the D&A end or the 2025 single year.
  No risk premium in the rate [E3-42]; the bare sovereign was used everywhere.

- **VERDICT: [x] quit on at the [E4-28] floor — FAIL ON PRICE. Ranking position: not
  ranked.** The fifth name in this queue to clear all four business gates (after ORLY,
  BRK-B, MCD, HAS) and the fifth to fail at Q5 on price.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*(No position exists or is opened — this section pre-commits the re-look, per queue
practice on floor-fail names.)*

**Pre-committed before entry [E1-02]:**
- Thesis-confirming metric: physical case volume (the [E4-55] series — positive or flat)
  WITH positive $/case, and gross margin held ≥ ~39%.
- **Thesis-breaking metrics and thresholds:** (i) a negative-pricing year (the PEP shape —
  $/case down nominally) or gross margin < 37% for a full year; (ii) any disclosed
  amendment to the incidence-based pricing agreement or CBA economics, or sub-bottling
  payments breaking above the filed $50–70M/yr guidance band without a volume/GP
  explanation — the licensor's-lever tell; (iii) [E2-49]: withdrawal of the standard-
  physical-case tables or the $-per-case ingredients.
- **Re-look price: ~$145/sh at a 5.25% sovereign (zero-growth judged value), recomputed
  at the rate of the day.** At the floor: ~$75.
- Next catalyst dates: Q3-2026 10-Q (~2026-10-29) — tariff-aluminum pass-through and
  whether H1's +7.1% volume holds; FY2026 10-K (~2027-02) — the $900M 2028 term-loan
  refi plan.

**The sell rule [E2-28]** — recorded for a future holder: HOLD conditions map to (i)
OI/NTOA staying ~40%+, (ii) no integrity event and capital returns staying price-
disciplined (the $400M authorization cut is the standard to hold them to), (iii) quote
vs the zero-growth band.

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring
question here: is a gross-margin slide tariff-cycle noise (aberrational) or Atlanta
re-dividing the system's economics (permanent)? The incidence agreement is the document
that decides; read every amendment disclosure.

- **VERDICT: [x] IN as a monitoring plan; no position.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN → Q2 IN → Q3 IN → Q4 IN →
  Q5 quit-on-floor → Q6 monitoring plan). Q5's arithmetic was drafted while Q2's row was
  in flight; the Q2 verdict closed BEFORE this audit and before any Q5 output leaves the
  file — the hard sequence is preserved in the reported artifact.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. Q2's row
  carries two stated DATA gaps (KOF op-profit tag; peer NTOA for IFRS filers) — recorded
  as limits of the row, with the class judged on what is filed and computed; Arca/Swire
  named as non-SEC-reachable rungs.
- [x] No UNRESEARCHED verdicts; no UNKNOWABLE verdicts.
- [x] Step 0: FY2025 10-K read (MD&A, cash-flow detail lines, footnotes), acc
  0001628280-26-009057; OCF $931,904k cross-checked tool-vs-filed; oe_bottom reproduced
  to the million.
- [x] Owner earnings on multi-year means (3-yr and 5-yr, both ends); capex band disclosed
  as a judgment with the CBA's minimum-capex covenant cited; sub-bottling subtraction
  confessed as a construction choice.
- [x] Competitor row filled (6 external rows) with limits stated.
- [x] Sovereign 5.25%, USD, US Treasury daily par yield curve (issuing authority),
  2026-09-03.
- [x] Value as round-number ranges (~$115–180; ~$60–95 at the floor).
- [x] One bar (screamer [E4-01]); windage count 2, justified in writing.
- [x] Prices dated; $197.40 aggregator quote flagged.
- [x] Run committed to git question-by-question (write-early protocol; survived TWO
  session kills with zero question loss).

**TOOL/METHOD DEFECTS logged for the queue:**
1. `run.py` share basis on COKE: 9.4M single-class weighted average → $1.86bn cap and
   29-37% yields — the known defect, compounded by the 2025 10-for-1 split. Cover count
   by hand is the only safe read (66,564,294).
2. D&A tag pick inconsistent across years (FY2025 missed $23.4M intangible amortization
   that FY2023/24 included): screen oe_top 684 should be 676.6. Same family as MCD/HAS.
3. **Queue-wide methods finding: the screen's OE construction is blind to recurring
   contingent-consideration payments classified as FINANCING** (COKE: $28–69M/yr,
   perpetual-in-practice sub-bottling royalty to CCR, guided $50–70M/yr). Any filer
   paying a licence royalty through an acquisition-contingent-consideration structure
   has OCF-based OE overstated by the full payment. The screen's 3.30% yield was ~0.5pt
   too HIGH on its own cap before the price moved.
4. The bottler-row sub-agent was lost to a session kill; rebuilt minimally in-session.
   Fan-out research for a run should write to disk incrementally (the row landed only
   because the rebuild did).

## REGISTER
- Verdict: **[x] IN on the business (Q1–Q4), quit on at the Q5 floor — FAIL ON PRICE.**
- One line: **A real narrow franchise held on a perpetual-at-the-bottler's-option licence
  — the bottler kept the pricing wave and its volume — but at $197.40 the yield is 3.8%
  against a 5.25% bond and an ~8–9% expectancy against the 10% floor: quit on, re-look
  ~$145.**
