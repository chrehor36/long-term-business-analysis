# Company Run — Chipotle Mexican Grill (CMG) — 2026-09-05
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
  yield curve, 30-yr, via `tools/sources.py` (struck fresh this run)**
- FX: none — USD quote, USD earnings (104 international restaurants are immaterial to the
  earnings currency; revenue is essentially all USD).

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **FY2025 10-K, filed 2026-02-04, accession
  0001058090-26-000009 (period 2025-12-31)**; also read: Q2-2026 10-Q (filed 2026-07-31,
  0001058090-26-000066), DEF 14A (filed 2026-04-28, 0001140361-26-017294), and 10-K
  vintages FY2017/FY2019/FY2021/FY2023/FY2024 for the decade series.
- figure cross-checked against the filed statement: **FY2025 net cash provided by operating
  activities $2,113,926 thousand, read off the consolidated statement of cash flows in the
  10-K — matches the XBRL screen's $2,114M to the thousand.**

**STAGE 0 BY HAND:**
- Price **$36.96**, 2026-09-04 close (aggregator — live quote only, flagged).
- Shares **1,265,418,000** hand-read off the Q2-2026 10-Q cover: "As of July 24, 2026,
  there were 1,265,418 [thousands; iXBRL scale=3] shares of the registrant's common stock,
  par value of $0.01 per share, outstanding." Single class. Cross-checked against the SEC
  dei concept series (1,265,418,000 at 2026-07-24).
- **Split guard verified**: 50-for-1 split effected 2024-06-26, all share history
  retroactively adjusted in the FY2025 10-K (Note 1); the cover count is post-split and
  needs no adjustment. run.py's 1,342.6M is a weighted-average EPS denominator — the known
  defect — corrected by the cover count.
- **Share count is FALLING fast**: 1,347.4M (2025-04) → 1,265.4M (2026-07), −6.1% in five
  quarters — buybacks, all shares retired immediately, no treasury stock.
- **No dividend — verified**: "have not declared or paid any cash dividends" (FY2025 10-K,
  Item 5).
- **Market cap = $36.96 × 1,265.418M = $46,770M** (vs screen row $48,118M and run.py
  $49,620M — both stale/defective; all yields below are at the hand cap).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **Chipotle builds a restaurant
  for about $1.5M ($1.3M after the landlord chips in), and that restaurant then sells about
  $3.1M a year of burritos and bowls off a deliberately tiny menu, keeping roughly a
  quarter of it as cash contribution before overhead (FY2025 filed cost lines: food 29.6%
  + labor 25.1% + occupancy 5.2% + other operating 14.7% = 74.6% of revenue). It owns
  every store — zero franchising beyond 14 Middle-East partner units — so 100% of each
  till accrues to the company, and every new store is paid for out of the till, never with
  debt (no debt has ever been drawn; $500M revolver undrawn). Corporate overhead is 5.5%,
  D&A 3.0%, tax ~24%, leaving ~13% of revenue as net income. The engine is an assembly
  line the customer walks along: few ingredients, no freezers, no microwaves, high orders
  per labor-hour, at a price point between fast food and casual dining, plus a digital
  layer (36.7% of food revenue, Chipotlane pick-up lanes in 257 of 334 new stores). Growth
  is arithmetic: ~8%/yr new units toward a filed "long-term goal of 7,000 restaurants in
  the U.S. and Canada" (Risk Factors, FY2025 10-K) plus whatever the comp does. A payback
  arithmetic the filing supports: ~$790k cash contribution on ~$1.3M net build cost —
  roughly 60% cash-on-cash per new unit before G&A, which is why the growth has never
  needed outside capital.**
- The scarce input this business controls: **the brand's value perception — "real food,
  fast, at a fair price" — and the single-format operating system that converts it into
  throughput. Structurally, it also controls 100% of its own economics: no franchisee
  layer shares the unit cash flow, and no franchisee layer buffers the shocks (the E. coli
  record shows both edges).**
- Will the fundamentals look broadly the same in ten years? **Yes — burrito assembly is
  simple and stable in character [E3-31]; the menu has barely changed in twenty years; the
  digital share shifts the ordering channel, not the product. The ten-year risk is demand
  (value perception), not comprehensibility.**
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] · no close substitute [~] *(the crux — adjudicated below on filed
  conduct, not on category labels)* · not price-regulated [x]
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**
  **The moat is brand + a single-format throughput system + scale-fed unit economics; it
  needs continuous DEFENCE (marketing, food safety, value perception), not replacement —
  the [E5-23]/[E3-49] class, not the competitive-destruction class. The key-person question
  is answered by a filed natural experiment: Niccol, the turnaround architect, left
  2024-08-31 [E4-23] — and the system printed +5.3% transactions in 2024 and stabilized a
  category-wide 2025 break within four quarters (Q2-2026 T +1.0% lapped). The moat did not
  go when the surgeon went. Recorded anyway as a Q2 watch item, not a Q3 compliment.**
- Primary moat metric, filing-sourced, and its trend: **the [E4-55] physical series —
  comparable TRANSACTIONS, which CMG files split from price every year, INCLUDING the bad
  ones.** Filed decade (see `_research 2026-09-05 CMG/cmg_decade_series.md`): 2019 +7.0 ·
  2021 +10.3 · 2022 +0.9 · 2023 +5.0 · 2024 +5.3 · **2025 −2.9 (the break, dated: went
  negative Q1-2025, trough Q2-2025 at −4.9)** · H1-2026 +0.8 lapped-positive. Cumulative
  2021-25: **menu price +34.3%, transactions +19.5%, mix −8.6%** — the price ladder
  [E2-44] was steep (+8.5/+12.0/+5.2/+2.9/+2.1) and traffic held POSITIVE through the
  steepest years (2021-24 cumulative +23.1%), breaking only in 2025 AFTER pricing had
  slowed to +2.1% — a demand/value-perception break, not concurrent-price elasticity.
  **This is the best physical series in the restaurant cohort**: EAT's decade was price
  +41%/traffic +6.9% (one viral year); DRI's guest counts negative; MCD's US real comps
  95.4 on 2013=100 with the guest-count disclosure withdrawn; SBUX chained traffic −17%
  under +20% real price. CMG took price AND grew transactions for a decade — until 2025.

**THE COMPETITOR ROW — required [E3-28].** 7 filed peers taken, of an industry with many
more (fast-casual bowls: both public attackers filed; Qdoba/Moe's/Panera private — row
limit stated [E3-61]).

| Company | latest-FY comps (traffic) | AUV | rest-level margin | units (growth) | source |
|---|---|---|---|---|---|
| **CMG** | **−1.7% (T −2.9%) FY25; H1-26 +1.4% (T +0.8%)** | $3.104M | ~25.4% (100−74.6 filed cost lines) | 4,042 (+8.5%) | FY2025 10-K 0001058090-26-000009 |
| CAVA | +4.0% (T +1.6%) FY25; **2026 YTD +9.4% (T +6.1%)** | $2.93M→$3.09M | 24.4%→25.7% (Q2-26) | 439→476 (+19-20%/yr) | CAVA 10-K 0001628280-26-011296, 10-Q |
| SG | −7.9% (**T −10.4%**) FY25; YTD26 −9.3% | $2.92M→$2.52M | ~15.2% (derived, flagged) | 281; growth cut 35→~13/yr, 9 closures, $11.3M impairments | SG 10-K 0001628280-26-012520 |
| WING | dom. SSS −3.3% FY25 → **−8.1% YTD26** (no T split filed) | $2.0M (from $2.14M) | n/a — 98% franchised, 25.7% op margin on royalties | 3,056 (+19.2%) | WING 10-K 0001636222-26-000008 |
| MCD | US guest counts negative every disclosed yr but 2017; disclosure withdrawn FY2020 [E2-49] | $3.07M/unit | 46.1% op margin (franchisor-landlord) | ~44k system | MCD run 2026-09-03 |
| SBUX | US T −5/−4 FY24-25, then +3/+4.3/+4.2 Q1-Q3 FY26 | — | — | — | SBUX run 2026-09-04 |
| EAT | FY26 T +3.6% (wave); decade price +41%/T +6.9% | $5.0M | 82.1% NTOA | ~1,100 | EAT run 2026-09-05 (Q2 OUT) |
| DRI | guest counts negative (Q2 OUT) | — | 38.5% NTOA | ~2,000 | DRI run 2026-09-04 |

- **What the row shows**: (1) the 2025 fast-casual demand crack was CATEGORY-WIDE (CAVA
  traffic +8.7→+1.6, WING −3.3, SG −10.4 traffic) — CMG's −2.9% was a middling print in a
  bad category year, not isolated share loss; (2) **the 2026 divergence is the live
  threat**: CAVA re-accelerated to +6.1% traffic while CMG limps at +0.8% — the [E2-45]
  attacker with ample capital and skilled personnel is CAVA, and its filed trajectory
  (CMG-level AUV and restaurant margins at 1/8th the footprint, 20%/yr unit growth) is the
  attack succeeding at the margin; (3) SG's collapse kills any "bowls category rising"
  story — the migration is brand-specific; (4) nobody else in the row runs CMG's model at
  CMG's scale — the closest economics (CAVA) are 1/8th the size, and the franchised names
  (WING, MCD) own different assets.
- **[E2-53] dominance test**: fails the strong form — this is not a one-paper town; a
  competitor at equal AUV/margin exists and is scaling. **[E2-44]**: (1) price-raising
  power PROVEN on the 2021-24 filed record, but spent — check mix negative five straight
  years (customers trading down inside the menu), price increases slowed to ~+2%, and the
  filer now leads with "exceptional value" language — the [E4-37] agony metric reads
  rising agony; (2) dollar-volume growth requires ~$1.3-1.5M of capital per unit — fails
  the minor-additional-capital half; this is [E4-20]'s GOOD class, priced at Q5, not a
  disqualifier [E4-43].
- **The [E3-30] base case, used honestly**: 2015-16 was an EXISTENTIAL brand crisis —
  comps −20.4%, AUV −23%, zero franchisee buffer — and the brand recovered fully, passing
  its 2015 AUV peak by ~2021 and printing its best traffic years after. The 2025
  disturbance is ~1/7th that size and stabilized in four quarters (filed: Q2-25 T −4.9 →
  Q2-26 T +1.0). The one filed precedent for this brand under stress says it recovers.
- **[E2-49] check across ten vintages**: the transactions/check decomposition has NEVER
  been withdrawn — the FY2025 10-K files the negative year in the same 5-line table as
  the good years (menu price, mix, all of it), and AUV is disclosed continuously through
  both collapses (−23% in 2016, −3.4% in 2025). The anti-MCD. Candor direction positive.
- **Untapped pricing power [E3-33]**: No. The ladder was used (+34% in 5 years); the
  near-monopoly claim [E5-28] cannot be made in a category this substitute-dense.
- Class: [x] **NARROW** · Direction: **narrowed through 2025 (traffic break + CAVA
  divergence); stabilized, not yet re-widening, in H1-2026. The single-brand,
  single-format concentration is the structural defect — no second engine [E4-23 watch],
  and the moat lives in a value perception that 2025 proved crackable.**
- **VERDICT: [x] IN** — NARROW. The filed decade of transactions-led comps through a +34%
  price ladder, the E. coli recovery precedent, and top-of-row unit economics at 10x the
  nearest attacker's scale clear [E3-03] on conduct. The 2025 traffic year alone does not
  convict a decade-long physical series that EAT/DRI/MCD could not show at all — but the
  CAVA divergence is named as the thesis-breaker and goes to Q6.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [x] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**Q3 is a BINARY GATE — daily execution.** A company-operated restaurant chain with 130,301
employees serving fresh, raw-handled food is the have-to-be-smart-every-day class in its
purest form: one food-safety lapse took comps down 20.4% and the AUV down 23% (2016, filed),
and there is no franchisee layer to absorb any of it. The E. coli record is the filed proof
that a bad eighteen months here destroys what a decade built. (Zero balance-sheet leverage;
no control position — the gate rests on execution alone.)

**Honesty — binary, permanent, filings-based [E5-16].** Dated record (full workpaper:
`_research 2026-09-05 CMG/cmg_q3_conduct.md`):
- **2020-04-21: DOJ Deferred Prosecution Agreement** — two-count Class A misdemeanor
  (adulterated food, FDCA) for the 2013-18 food-safety record; $25M fine; three-year
  compliance term, completed. Verified in the FY2020 10-K on disk. **A corporate criminal
  resolution about the product — the gravest item on file. Read under [E5-22]
  (acted-when-learned): the rebuilt food-safety program is Item 1's longest section, and
  the AIP's food-safety modifier can only cut pay, never raise it. A business-conduct
  failure, remediated on the filed record; not a personal-misconduct disqualifier.**
- 2022: NYC Fair Workweek settlement; a SECOND NYC compliance audit is ongoing (filed,
  FY2025 risk factors) — company-operation concentrates employment liability franchised
  peers disperse.
- Pending: Stradford securities class action (portion-size statements + insider-trading
  allegations; dismissed 2025-12-18 with leave to amend, refiled 2026-01-20) and a stayed
  derivative suit (adds buybacks-at-inflated-prices). Unadjudicated; watched, not charged.
- 2024-08-31: **Niccol left for Starbucks [E4-23]** — forfeited all unvested equity
  ($27.9M reversal, filed). What changed since: Boatwright (internal — COO through the
  whole 2017-24 turnaround; 18 years of Arby's operations before) took over with $52M of
  retention RSUs holding the rest of the team; the operating system, pay design, and
  disclosure practice are unchanged across the transition (same tables, same metrics, no
  restatements). The 2025 traffic year is the first test of the post-architect system and
  it stabilized in four quarters.

**STEP 2 — THE FLAGS [E4-22, E5-15].**
- [ ] weak accounting — **none found**: GAAP-only, single capex caption, E&Y since 1997
- [ ] unintelligible footnotes — no
- [x] trumpeted earnings projections — **mild and scoped**: filed guidance is comp
  direction ("about flat" for 2026) + opening counts + capex; no EPS guidance in any SEC
  filing read (ERs not swept — scope stated). Not the [E5-30] ratchet shape.
- [ ] serial share issuance — inverse: −6.1% count in five quarters
- [ ] EBITDA / adjusted-earnings promotion **[E4-29]** — **ZERO occurrences of EBITDA in
  the FY2025 10-K and Q2-2026 10-Q (counted). No non-GAAP earnings measure anywhere in the
  annual report. The cleanest [E4-29] read in the restaurant cohort; pay uses restaurant
  cash flow metrics, disclosed as such.**
- [x] filed-figure tells [E4-30] — cash-tax %: 24.4/26.5/21.1% of pretax FY2023-25; the
  2025 dip fires and is **acquitted with the named driver**: OBBBA payment deferral,
  disclosed in the filing's own cash-flow MD&A (the TSCO/EFX shape). Growth is not
  smooth — the filed series swings −20.4% to +19.3%.

**STEP 3 — THE PRIMARY TEST [E2-01].** FY2024-25: NI $1,534.1M/$1,535.8M on average equity
~$3.4bn/$3.2bn → **ROE ~46-47% with ZERO debt** (the revolver has never been drawn; leases
are the only quasi-debt). RONTA ~80%+ (the SBUX run row computed 82.6% on FY2025 filings).
New-unit cash-on-cash ~60% pre-G&A ($790k contribution on $1.3M net build). The business
passes [E3-46] on every denominator, without gimmickry — the equity is SHRINKING from
buybacks while returns rise, so the ROE series overstates nothing.

**The half-owner test [E2-26]: PASSES, and notably.** The FY2025 10-K files the negative
transactions year in the same five-line decomposition as the boom years; the G&A bridge
itemizes the retention awards and legal contingencies to the million; the Niccol forfeiture
is quantified; buyback prices are averaged per vintage in Note 7. The 2016 and 2025
collapses are both displayed, not adjusted away. (Reservation: the "portion size" episode —
what the Stradford complaint alleges management said off-filing — is exactly the
half-owner-test terrain, and it is unresolved in court.)

**The institutional imperative [E2-30]:**
- [ ] resists change — no (channel, menu, international model all changed)
- [x] projects to soak up funds — **mild**: the Cultivate Next venture fund ($100M
  authorized, $63M in) is a classic soak-up item at 0.2% of cap; the material cash sink is
  buybacks, scored below
- [ ] staff studies for the leader's craving — not observed
- [ ] peer imitation — **inverse**: the model refuses the industry's franchising playbook
  entirely; no dividend despite every peer paying one

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds: **yes** — net cash, zero debt, $500M revolver undrawn; though FY2025
  buybacks ($2,425.5M) ran ~$1bn past OCF−capex, funded by draining investments and cash
  ($778M→$386M), not by borrowing (the [E4-50] boundary respected).
- (2) material discount to conservative IV: **FAILS on the FY2024 vintage — $995.8M at a
  $57.21 average, 2.6-2.9x this run's judged zero-growth value, bought at the multiple
  peak (stock at 217 on the 10-K's own 2020=100 chart, now 134). The FY2025/H1-2026
  vintages ($42.54 → ~$35.95, accelerating into the decline — Nov-2025 10.9M shares at
  $31.30) still sit above the zero-growth band and are defensible only on the growth case.
  CAPITAL-ALLOCATION FLAG, carried with [E4-13]: management knows the unit runway better
  than I do, and the vintage pattern (buying MORE as the price fell, three authorizations
  in six months) is the right-shaped response to their own belief. Binds position size,
  never the discount rate.**
- Pay-versus-performance: **clean by the DG/ULTA test** — 2025 CPF paid 40% (CRS and RCF
  margin components paid ZERO against targets set above prior actuals; only the SARs
  pipeline metric paid); 2023-25 PSUs paid 273% on the crest years, symmetric. Metrics
  stable across the CEO change; the one modifier eliminated (Brand Purpose) was announced
  ahead with reasons — [E2-49]'s candor case, not its flag.

**THE GUARDRAIL — checked.**
- [x] Nothing here promotes the name; Q2 was decided on the filed physical series, not on
      management.
- [x] Key-person dependence recorded at Q2 as a watch item [E4-23], not here as a strength.
- [x] No manager-as-plan reasoning: the franchise question was decided before this section.

- **VERDICT: [x] IN** — no disqualifier found (GATE case; the DPA is the closest call and
  it is a remediated business-conduct matter, not personal misconduct). *IN = absence of
  found disqualifiers, not a finding of honesty [E5-17]. IN never promotes.* Live flags
  carried: buyback condition-2 (position-size), Stradford (watch), NYC second audit (watch).

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** All hand-transcribed
from four 10-K vintages (series in `_research 2026-09-05 CMG/cmg_decade_series.md`); OE =
OCF − SBC − (c), $M:
- **3-yr mean (2023-25):** capex end **$1,268.8** · D&A end **$1,536.8**
- **5-yr mean (2021-25):** capex end **$1,043.1** · D&A end **$1,280.0**
- **10-yr mean (2016-25):** capex end **$619.7** — *displayed and REFUSED as a level: it
  averages a 2,200-store company with a 4,000-store one (the ACMR/ALKT doctrine — the mean
  of two different businesses). The step-up is structural unit growth (+80% units since
  2018), not a price wave.*
- **Spread, conservative end (5-yr vs 3-yr capex ends):** −17.8% — *run.py's divergence
  reproduced; the screen row's 1,043/1,537 band reproduced to the million by hand.*
- **Combined range carried: $1,043M to $1,537M** · judged **$1,400M** (below the FY2025
  D&A-end level, see normalization)
- Distorted years NAMED [E4-41], all directions: **FY2025 OCF flattered by the OBBBA
  cash-tax deferral** (taxes paid $532.9M→$423.5M on a flat provision; filed: "timing of
  tax-related payments, including the impacts of H.R.1") ≈ $80-110M one-time; **gift-card
  breakage re-estimate** added ~$20-27M of FY2025 revenue (breakage $1.2M→$7.8M→$27.9M
  FY2023-25, disclosed); **lease-book growth timing** puts ~+$74.5M inside FY2025 OCF (ROU
  amortization $332.7M vs cash lease payments $258.2M) — recurring only while the lease
  book grows. Downward: 2016 (E. coli, OE ≈ $26M) and 2020 (pandemic) sit in the 10-yr
  window. FY2024-25 D&A-end ~$1.63bn less the named items ≈ $1.45-1.50bn; judged $1,400M
  adds a step for the flat-comps/cost-inflation direction management itself guides to.
- Owner earnings by year (capex end, $M): 26.2 / 186.2 / 265.0 / 296.3 / 207.9 / 663.2 /
  746.0 / 1,098.7 / 1,379.7 / 1,328.0 (FY2016-25)
- **Maintenance capex — (c) is a DISCLOSED JUDGMENT and CMG files the measured split (the
  DG/TSCO precedent):** FY2025 total capex $666.3M, of which new-restaurant construction ≈
  $500M ("we spent on average about $1.5 million in development and construction costs per
  new restaurant" × 334 openings; $1.3M net of landlord reimbursements), leaving ~$166M of
  existing-restaurant + corporate/tech spend. 2026 guide filed: $834.1M total = $531.8M
  new-restaurant + $266.9M existing restaurants (remodels, equipment, technology) + corporate.
  D&A is $361.4M — ABOVE the filed maintenance-ish bucket in both years. **This is the
  anti-railroad: [E5-20] does not apply; (c) is judged AT the [E3-44] default, D&A ≈
  $360M**, which covers the filed existing-restaurant spend with ~$100-150M of headroom
  for the true long-run remodel cycle on 4,042 aging boxes. The D&A end is therefore the
  honest (c) construction; the capex end (all growth charged as maintenance) is displayed
  as the conservative floor of the band.
- Stock compensation subtracted in full **[E5-06]**: yes, every year, at the reported
  charge ($119.5M FY2025). [E3-70] noted: the charge is the floor of the subtraction;
  PSUs run 0-300% and a small development-team slice is capitalized into PP&E (disclosed) —
  at ~1% of revenue the gap moves nothing.
- The capex band does not change the verdict (both ends yield far below the bond at Q5).

### Great, good, or gruesome? **[E4-20]**
- [x] **good — top of the class** — attractive return earned also on added capital
- Evidence: every incremental dollar goes into a new restaurant at ~$1.3M net that returns
  ~$790k/yr of restaurant-level cash (~60% pre-G&A cash-on-cash); ROE ~46-47% unlevered;
  RONTA ~80%+. Not "great" only because growth genuinely consumes capital (~$500M/yr) —
  [E2-44](2) fails — and not remotely gruesome: the added capital earns extraordinary
  rates [E4-43]. The 12%-is-satisfactory benchmark [E5-40] is beaten five times over on
  retained capital.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **PASS** — OE positive in every year of the
  filed decade INCLUDING the E. coli year ($26M) and the pandemic ($208M); FY2025 OCF
  $2.1bn through a negative-traffic year.
- (2) massive liquid assets: **MARGINAL PASS** — $1,049M cash+marketable at YE2025, but
  drained to **$678M by 2026-06-30** ($228.2M cash + $449.7M investments) by the buyback
  pace; zero debt; the $500M revolver is NOT counted [E5-39]. The cushion is thinner than
  at any recent year-end and still falling — but the drain is discretionary (buybacks),
  stoppable same-day.
- (3) no significant near-term cash requirements: **PASS** — no debt, no maturities, ever.
  Fixed charges are rent ($569M due 2026; lease PV $5,075.8M, 14.1-yr weighted term,
  5.48% discount) and food-linked purchase obligations ($1,135M due 2026, self-liquidating
  against sales). Nothing depends on the kindness of strangers.
- Leverage, named and quantified **[E4-16, E3-29]**: financial debt ZERO (revolver undrawn
  since inception; SOFR+1.125% if ever used). The lease stack is the only leverage:
  $5.1bn PV / $8.3bn undiscounted incl $834M signed-not-commenced — ~3.6x judged OE
  undiscounted, with rent a hard fixed charge against a variable guest count [E4-40].
  Coverage [E2-54]: no interest; OCF after maintenance capex covers 2026 rent ~3.1x
  ((2,114−361)/569); in the 2016 stress template coverage held above 1x and the company
  never borrowed.
- ASC 842 NOT immaterial and stated: occupancy is only 5.2% of revenue (the fast-casual
  advantage over EAT's casual-dining 8-9%), but the 14-year tail means a shrinking-brand
  scenario carries a decade of contracted rent on every dark box.
- Gift-card float [E5-46] noted: $218.8M unearned revenue, covenant-free customer prepay;
  negative working capital throughout ("guests generally pay using cash or credit...
  generally within ten days" — the filing's own words). Small but structural.
- Software capex: NO separate caption in any vintage read (single "Purchases of leasehold
  improvements, property and equipment" line) — the HAS defect does not bite; a small
  development-SBC capitalization into PP&E is disclosed and immaterial.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- **Mechanism 1 — a second food-safety catastrophe at 4,000-store scale.** The exposure is
  filed in the filer's own words [E4-40]: "We may have higher risk for food safety
  incidents than some of our competitors because we use fresh, unprocessed produce, handle
  raw chicken in our restaurants... and don't use artificial preservatives or frozen
  ingredients" — and it has already happened once (2015-16: comps −20.4%, AUV −23%, op
  income $763.6M → $34.6M, −95.5%, plus a criminal DPA). Quantified at today's scale: a
  2016-shape year takes revenue −$2.4bn and, at the filed 2016 flow-through, OI from
  $1.94bn to ~$0.1-0.4bn and OE to ~$0-300M for 1-2 years; with zero debt, $678M liquid,
  buybacks halted, and rent covered ~1.2-1.5x even then, the company survives it — the
  2016-19 recovery is the filed precedent (5 years to prior AUV). The single-brand,
  company-operated structure means NOTHING dilutes the hit (no second banner, no
  franchisee buffer) — the AATC-shape concentration named in the brief. Likelihood:
  **a real possibility** (once per filed decade; the Q2-2026 10-Q already names fresh
  "U.S. food safety concerns" as a live traffic headwind).
- **Mechanism 2 — value-perception bleed to the attacker (the valuation death).** Traffic
  never durably recovers (2025 −2.9%, H1-2026 +0.8% lapped); CAVA takes the marginal
  customer (+6.1% traffic YTD-2026 at CMG-level AUV/margins); unit growth masks per-store
  decline until the 7,000-box target fills the runway; OE plateaus at ~$1.2-1.4bn while
  cost inflation eats ~100bps of margin/yr un-offset (the 2025 miniature: restaurant costs
  74.6% of revenue, +1.2pts YoY). The company lives; the growth the price assumes dies —
  the DG-shape stagnation. Likelihood: **a real possibility** — this is the live 2025-26
  filed record extended, and it is the Q5/Q6 question.
- **Mechanism 3 — solvency.** Essentially unnameable on the filed structure: no debt, no
  walls, rent 5.2% of revenue with 3x coverage after maintenance capex, float-positive
  working capital. Even stacking mechanism 1 on a recession leaves rent covered with
  buybacks stopped. Likelihood: **a low-level possibility**.
- **VERDICT: [x] IN**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: **~8-10%, judged ~9%** (yield ~3.0% + credited growth
+5 to +7 — see the growth adjudication below). **Below roughly 10%: quit on, not ranked.**
The top of the honest range TOUCHES the floor — the closest any name in this queue has
come — and what it requires is stated below, in writing, against [E4-35]'s base rate.

**The screen row reproduced before adjudicating:** the row's OE band $1,043M/$1,537M =
my 5-yr capex end (to the million) / 3-yr D&A end; the row's 47.4% spread = 1,537/1,043 − 1
✓; the row's 2.17% yield was struck at a stale $48.1bn cap — at today's hand cap the same
construction yields 2.23%. Row verified in shape and in figure.

**One book. Owner earnings against the bond.** A DCF ran as an engine only (to convert the
runway into a rate); it cast no vote **[E3-34]**.

**1. THE YIELD**
- owner earnings **$1,400M judged** ($1,043-1,537M carried) ÷ market cap **$46,770M**
  = **2.99%** (range 2.23-3.29%) · sovereign **5.24%**
- Every construction on every window — including the best year ever at the D&A end
  ($1,638M → 3.50%) — yields below the 30-year Treasury at $36.96.

**2. WHAT THE PRICE ALREADY ASSUMES**
- growth needed to justify the quote at the bare bond rate: **+2.2%/yr perpetual** (range
  +1.9 to +3.0) — the strongest thing sayable for this price
- growth needed for the ~10% floor: **+6.5 to +7.6%/yr perpetual** (judged +6.8%) — the
  screen's 7.83% reproduced in shape at the stale cap
- what the business has actually done: units **+8.4-8.5%/yr** (filed, decade); OE
  +19%/yr (2021-25) and +28%/yr (2017-25, off the crisis base); revenue +5.4% in the BAD
  year. **This is the rare name where the floor's required growth sits BELOW the filed
  decade's actual** — the brief's stated prior, confirmed in the arithmetic.

**3. WHAT YOU ARE PAID**
- return at the current price = **−2.25 points under the sovereign** (range −3.0 to −1.95)
  before any growth is credited.

**THE GROWTH ADJUDICATION — what the floor may credit, and why it still fails [E4-35,
E4-51].** The creditable engine is units: 4,042 toward a FILED "long-term goal of 7,000
restaurants in the U.S. and Canada" — ~8 more years at the current 334-370/yr pace, each
box at ~$1.3M net cost returning ~60% cash-on-cash, funded internally. Credit that
visible runway in full at flat comps and today's margins and the expectancy is yield
~3.0% + ~6-7 points ≈ 9-10%: **brushing the floor from below**. To CLEAR 10% the run
must ALSO believe some combination of (a) durably positive traffic (the 2025-26 record:
−2.9% then +0.8% lapped, with CAVA taking the marginal customer at +6.1%), (b) year-one
AUVs holding as saturation doubles (the comp bridge already shows the 2024 class at
~$1.6M in its ramp year), and (c) margins holding against the cost inflation the filer
itself names — with the ceiling [E2-63] that after 7,000 the engine is comps plus an
unproven 104-store international layer. That is a burden-of-proof case, not a filed
record. **Judged honest expectancy ~9%: below the floor. Quit on, not ranked.**

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

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support:
- **Zero-growth at the sovereign: roughly $16 to $23 per share, judged ~$21** (OE
  $1,043-1,537M ÷ 5.24% ÷ 1,265.4M shares).
- **At the ~10% floor, zero-growth: roughly $8 to $12 per share.**
- **With the visible unit runway credited in full** (7%/yr for 8 years to the 7,000 goal,
  then the bond rate, demanded at 10%): **roughly $25 per share** — the price a
  floor-honoring buyer could pay while crediting the whole filed record.
- **Current price: $36.96** (2026-09-04, aggregator, flagged) — 1.75x judged zero-growth
  value, and ~1.5x even the full-runway floor value. The price is buying the runway AND
  the post-7,000 era on faith.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **~9% judged (8-10% range)** vs ~10%
  **[E4-28]** — **below → quit on.** The ranking lines below are informational only, per
  the queue's completed-entry convention:
- points over sovereign, this name: **−2.25** on the current yield; the highest honest
  EXPECTANCY of the gate-clearers to date (vs TSCO 6.8-8.8%, MCD 7.6-9.2%, EFX 5.5-7.5%,
  and parallel-run CTAS at a ~2.0% yield on its $80.2bn cap) — rank #1 among them, and
  still under the floor. Take the best available, or nothing: **nothing.**
- **ORDINAL RULING (operator instruction, 2026-09-06):** CMG and CTAS cleared their gates
  the same evening and both Q5 states were preserved in the SAME thirteenth-kill-wave
  commit (a8886a3, 2026-09-06T07:04:52-04:00), so the Q5-commit tiebreak is a dead heat.
  Falling back to the gate-clearing commits: CMG Q4 IN at 98635fe 2026-09-05T16:21:05-04:00,
  CTAS Q4 IN at 5775f90 2026-09-05T16:22:45-04:00. **CMG is the ELEVENTH name to clear all
  four business gates, CTAS the TWELFTH, by 100 seconds of commit timestamp.**

**WHICH BAR ARE YOU USING?**
- [x] **Screamer test [E4-01]** — the price ($36.96) sits ABOVE the entire zero-growth
      band ($16-23) and above the full-runway floor value (~$25), but below a
      bond-rate-discounted full-growth construction — **outcome: inside the wide range at
      generous constructions, above it at conservative ones → no useful conclusion in the
      buy direction; the floor already closed the file. No margin added on top.**
- **Windage count: ONE** — the judged OE ($1,400M vs the $1,505M normalized level) is the
  single place conservatism was spent; the floor test, the value band, and Bar 2 all run
  on realistic inputs with no further margin **[E4-11, E4-48]**.

- **VERDICT: quit on at the [E4-28] floor — the name is not ranked for purchase.
  Q5 closes the file: FAIL, ON PRICE. · ranking position: #1 of the gate-clearers on
  expectancy, unranked for capital.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened for entry — the file closed at Q5. Pre-committed RE-LOOK terms [E1-02],
written before any position exists:**
- **Re-look price: ~$21/sh judged zero-growth at a 5.24% sovereign, recomputed at the rate
  of the day; below ~$25-26 the floor case clears on the VISIBLE runway alone** (at $25:
  cap $31.6bn, floor growth needed ~5.3%/yr vs the filed 8%/yr unit record) — re-open the
  file there, whatever the tape says.
- Thesis-confirming metrics (the [E3-30] monitoring question — aberration or permanent
  slip): FY2026 full-year transactions positive on the lapped base; CAVA's traffic
  converging toward CMG's rather than diverging; year-one cohort revenue per the comp
  bridge holding ≥ the 2024-class ~$1.6M; restaurant costs ≤ ~74.5% of revenue.
- **Thesis-breaking metrics:** a second negative transactions year in three (FY2026
  full-year T < 0); CAVA sustaining ≥ +5pts of traffic divergence through FY2027;
  withdrawal or blurring of the transactions/check decomposition table [E2-49]; buybacks
  continuing at >$2bn/yr above the judged band while cash+investments falls below ~$400M;
  any multi-state food-safety incident (the mechanism-1 tripwire).
- Next catalyst dates: Q3-2026 10-Q (~2026-10-30, the "food safety concerns" headwind
  quantified); FY2026 10-K (~2027-02, the lapped traffic year adjudicated).
- **VERDICT: file closed at Q5; re-look terms pre-committed above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1→Q5 in sequence; Q6 re-look only)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — one peer
  DISPLAY metric (SG's derived restaurant margin) is flagged inside the row; the Q2
  verdict does not rest on it
- [x] No UNRESEARCHED verdicts issued
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: FY2025 10-K read (MD&A, cash-flow detail lines, footnotes), accession
  0001058090-26-000009; FY2025 OCF $2,113,926k cross-checked filed-vs-XBRL
- [x] Owner earnings on multi-year means (3/5/10-yr, both capex ends); (c) disclosed as a
  judgment at the [E3-44] default with the filed measured split cited
- [x] Competitor row filled: 8 rows, 7 filed peers + 4 completed-run cohort names; private
  non-filers named with the [E3-61] limit
- [x] Sovereign 5.24%, USD (the earnings currency), US Treasury daily par yield curve
  (issuing authority), 2026-09-04, struck fresh
- [x] Value as round-number ranges ($16-23 / $8-12 / ~$25)
- [x] One bar (Bar 2 screamer); windage count ONE, stated
- [x] Prices dated; aggregator flagged, live quote only
- [x] Run committed after every question (3cbb3d8 Q2 · 73a80e6 Q3 · 98635fe Q4; Q5/Q6
  preserved by kill-wave a8886a3; ordinal + audit committed after resume)

**DEFECTS CONFESSED (assume some; here are the found ones):**
1. run.py's weighted-average share basis again (1,342.6M vs the 1,265.4M cover count) —
   corrected by hand; the screen row's 2.17% yield was struck at a stale $48.1bn cap.
2. The brief's "price ladder ~+20%+" UNDERSTATED the filed record: +31.6% (2021-24),
   +34.3% (2021-25). The brief's AUV ~$3.2M was the 2024 figure; 2025 filed $3.104M.
3. The ten-year traffic decomposition has two filed holes: no full-year T/check split in
   the FY2018 and FY2020 vintages (stated as n/f in the series, not interpolated).
4. Earnings releases were not swept — the no-EPS-guidance claim is scoped to SEC filings.
5. H1-2026 OE not fully constructed (OCF displayed; SBC/capex for the half not
   transcribed).
6. Peer restaurant-margin definitions differ at the edges (CAVA/SG define restaurant-level
   margin per their own filings; CMG's derived from cost lines; proxy CPF actual 25.62%
   used as the check).
7. The thirteenth-kill-wave commit (a8886a3) swept CMG and CTAS files into one commit —
   the standing broad-add defect, structural to the kill-preserve mechanism, noted again.
8. The DPA is cited from the FY2020 10-K on disk; the dismissal-then-refile docket state
   of Stradford is as of the FY2025 10-K only (no later docket check).

## REGISTER
- Verdict: **Q1 IN · Q2 IN (NARROW) · Q3 IN (GATE, no disqualifier) · Q4 IN — the
  ELEVENTH name to clear all four business gates — then FAIL AT Q5, ON PRICE, at the
  [E4-28] floor.** (About the business: IN. About the price: quit on.)
- One line: **The best honest expectancy in the queue (~9%) still sits under the floor:
  a 3.0% judged yield needs ~6.8%/yr perpetual growth, and only the visible 8-year unit
  runway — not a perpetuity — has a filed record behind it; at ~$25-26 the floor clears
  on the record alone, and the re-look is pre-committed there.**
