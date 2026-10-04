# Company Run — Tractor Supply Company (TSCO) — 2026-09-04
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

*Prior file: `2026-07-15 Run - TSCO (Tractor Supply).md` — a v3.0 run that PASSED the name
at "STATUTE-ONLY (starter size)" on a 6.52% yield against a 5.10% hurdle, with Gate 3
marked "PASS (provisional)" — the exact protocol violation v4.1 forbids (a gate marked IN
carrying "provisional" is UNRESEARCHED). This run replaces it and inherits nothing from it.*

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
- rate **5.25%** · date **2026-09-03** · source **US Treasury daily par yield curve, 30-yr,
  from the issuing authority** (`tools/sources.py`, struck fresh 2026-09-04)
- FX: none — USD quote, USD earnings. No ADR.

**Price and cap:**
- price **$34.99**, 2026-09-04, **aggregator — live quote only, flagged**
- shares **521,040,137** hand-read off the Q2-2026 10-Q cover (filed 2026-08-06, period
  2026-06-27, accession **0000916365-26-000059**), single class ("Common Stock, $0.008 par
  value"). `cover_shares.py` audit run and verified. The **5-for-1 split of December 2024**
  is inside the filed history; the cover count is post-split and the split-adjusted
  perimeter guard reads "no step" (verified below at the screen reproduction).
- market cap **$18,231M** (= 521,040,137 × $34.99)
- *Tool defect, still live (queue-wide): `run.py` used a 532.2M weighted-average diluted
  share basis — an EPS denominator, not a share count — 2.1% above the cover count.*

**SCREEN ROW — REPRODUCED BEFORE ADJUDICATING (operator instruction).**
The brief's row: *yield 3.29%, growth required 6.71%, spread 22.7%, "no step".*
- The 2026-09-01 WATCHLIST TRIAGE row as it stands on disk today: **cap $18,122M,
  oe_bottom $554M, yield 3.06%, vs sovereign −2.12%, growth required 6.94%, spread 74.1%,
  no level shift** ("no step" verified — the split-adjusted perimeter guard handled the
  5:1 split correctly; `already_run False, financial False, lease False`).
- `run.py` fresh today: 3-yr OE $598–964M, 5-yr OE $557–935M, yield 3.21–5.18% on its
  (defective) 532.2M-share cap.
- **The brief's yield reproduces**: oe_bottom ~$598M (3-yr capex end) ÷ the triage cap
  $18,122M = **3.30% ≈ 3.29%**, and growth required 6.71% = 10% − 3.29% ([E4-28] floor
  arithmetic). **The brief's "spread 22.7%" does NOT reproduce from any construction on
  disk** — the capex-end vs D&A-end spread is 61–74% depending on window ((964−598)/598 =
  61.2%; the triage's stored 74.1%). Logged as a **brief defect**; the true spread is
  wide, not narrow, and it is the FY2025 capex step-up ($895M vs $494M D&A) that drives it.
- Adjudication of the row is at Q4, from the filed statements, by hand.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **FY2025 10-K, fiscal year ended 2025-12-27, filed
  2026-02-19, CIK 0000916365, accession 0000916365-26-000014** — MD&A, the cash-flow
  statement including its detail lines, and Notes 1-13 read in full; Q2-2026 10-Q accession
  **0000916365-26-000059**
- figure cross-checked against the filed statement: **FY2025 operating cash flow
  $1,635,259k on the filed Consolidated Statements of Cash Flows = the screen's $1,635M
  OCF input; FY2025 capex $894,770k filed = the screen's $894.8M**. Both match to the
  thousand.
- ladder rung: SEC EDGAR primary documents (rung 2)

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** TSCO buys feed, fencing, pet
food, tools, trailer parts and workwear from 1,100+ vendors (no vendor over 10% of
purchases), moves ~81% of it through ten distribution centers (7.8M sq ft, an eleventh
building in Nampa, Idaho), and sells it through 2,602 small-box stores (15-20k sq ft
inside selling space plus a side lot) sited in towns outlying metro areas — places
generally too small to host a second dedicated farm-supply box. Roughly half the basket
is C.U.E. — consumable, usable, edible: livestock feed, pet food, bird seed, propane,
fertilizer — bought on repeating trips; the customer owns animals and land, and animals
eat every day. Gross margin 36.4%; SG&A incl. D&A 27.0%; operating margin 9.45%
(FY2025, filed). The store base is **97% leased, 3% owned**, and the company deliberately
builds new owned stores and then sells and leases them back (41 stores for $252.6M in
FY2025), so the lease book, not the property line, is where the store network lives:
operating lease liabilities $4,141.7M PV at a 10.8-year weighted term.

- **The scarce input the business controls:** store-network density in small-town trade
  areas plus the distribution network that reaches them at 81% self-supply — the same
  scarce input as ORLY's, one rung shallower (parts availability there, trip
  consolidation here). Filing: *"we act as a trip consolidator for numerous needs-based
  requirements of farm, ranch, and rural customers."*
- **Will the fundamentals look broadly the same in ten years?** Yes. Horses will eat,
  fences will break, dogs will be fed. The product set (feed 27%, companion animal 24%)
  is the least fashion-exposed in specialty retail. The open question is not the
  category's existence but who serves it — that is Q2's question, not Q1's.
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
*Research: `_research 2026-09-04 TSCO/comp series 10yr.md` (the decade, verbatim, per-year
accessions), `competitor row and attackers.md`, `cpi deflators.md`, `long series and wave
arithmetic.md`. The brief called this "the closest Q2 call in tier 2" and it is.*

- Needed or desired **[x]** — roughly half the basket is C.U.E. (consumable, usable,
  edible: feed, pet food, bird seed, propane); animals eat daily; the filing's own frame is
  *"needs-based, demand-driven product categories"* and *"trip consolidator."*
- No close substitute **[x, at the format level; NOT at the SKU level]** — every SKU has a
  substitute channel; the claim that survives is the consolidated needs-trip in a small
  town, held by density (2,395 TS stores; ~4x the store count of any farm-channel
  competitor) and 81% self-distribution.
- Not price-regulated **[x]**.
- Must the moat be continuously rebuilt? **Defended, not rebuilt [E4-04]:** the basis
  (store density + DC network) persists; remodels and DC additions defend the same
  advantage rather than buying its replacement. Success does not depend on a great manager
  [E4-23] — no key person is the moat.

### [E4-55] THE PHYSICAL SERIES — the brief's decisive instrument, ten years, as filed
*(each year from its own 10-K, accessions in the research file; NEVER restated across
vintages, checked year-by-year — finding 7 of the research file)*

| FY | Comp sales | **Transactions** | Ticket (nominal) | CPI y/y | Ticket (real) |
|---|---|---|---|---|---|
| 2016* | +1.6% | **+2.6%** | (0.9)% | +1.3% | ~−2.1% |
| 2017 | +2.7% | **+2.2%** | +0.5% | +2.1% | ~−1.6% |
| 2018 | +5.1% | **+2.2%** | +2.8% | +2.4% | ~+0.3% |
| 2019 | +2.7% | **+0.3%** | +2.4% | +1.8% | ~+0.6% |
| 2020 | +23.1% | **+10.9%** | +12.2% | +1.2% | ~+10.8% |
| 2021 | +16.9% | **+7.1%** | +9.8% | +4.7% | ~+4.9% |
| 2022* | +6.3% | **(0.6)%** | +6.9% | +8.0% | ~−1.0% |
| 2023 | 0.0% | **(0.4)%** | +0.4% | +4.1% | ~−3.6% |
| 2024 | +0.2% | **+0.8%** | (0.6)% | +3.0% | ~−3.4% |
| 2025 | +1.2% | **+1.4%** | (0.2)% | +2.6% | ~−2.8% |
| H1-2026 | (0.6)% | **(1.4)%** | +0.8% | +3.3% | ~−2.4% |

*53-week years. CPI-U annual averages, BLS.*

**What the series answers, question by question:**
- **Did transactions grow through the 2022–25 price cycle?** Through it, essentially yes:
  two mild declines in the wave's teeth (−0.6, −0.4) then two gains (+0.8, +1.4) as pricing
  went to zero — cumulative **+1.2% over the four post-wave years, and the +18.8% pandemic
  transaction surge was RETAINED, not given back.** This is what DG, TGT, DRI and MCD could
  not show. The FY2024 10-K states the mechanism: *"positive unit growth was offset by
  average unit price pressure, principally due to commodity price deflation."*
- **[E2-44] both halves.** (1) Price held when volume was tested: FY2022 ticket **+6.9%**
  against transactions only −0.6 — price went up and volume held. And the reverse leg:
  through three years of nominal ticket DECLINE, gross margin ROSE (36.26% → 36.42%) — the
  deflation was passed to the customer while the spread was kept. (2) Grow dollar volume
  with only minor additional capital — **no**: growth is stores + DCs (capex 1.8x D&A).
  Half one passes; half two fails, which is the difference between WIDE and NARROW here.
- **The deflated ticket (the 5-for-10 instrument):** REAL ticket negative four consecutive
  years (~−3%/yr) — **direction guilty**; real revenue per store **+13–14% above the
  pre-pandemic FY2019 base** (revenue +85.9% vs CPI +25.9% on ~+30% stores) — **level
  acquitted**, the ANF shape. The tiebreak goes to the purer physical series above.
- **[E2-49] — what disappeared:** the comp transactions/ticket series itself has been
  published for a decade, **never withdrawn, never restated** — the ORLY pattern. What DID
  go: the entire Item 6 table (FY2021 10-K, with Reg S-K Item 301's repeal) took the dollar
  ticket ($51.90 last print), absolute selling square footage (32.1M sq ft last print),
  inventory turns and average inventory per store out of the 10-K. Sales per square foot
  was **never** disclosed in any vintage; Neighbor's Club member counts were **never** in a
  10-K or proxy — "record members" claims live in earnings releases only, so **the brief's
  "very high share of sales" loyalty premise cannot be verified from the filings at all**.
  The FY2025 10-K also REDEFINED the exclusive-brands metric upward (Owned Brands →
  Owned + Exclusive Product Categories, 30% new basis, priors recast) — the one
  metric-switch found, cosmetic in size, noted.
- **The wave question [E3-51] the brief ordered asked:** the pandemic DID pull demand
  forward (+23.1%/+16.9% comps), and real comps have been negative four years since
  (−1.7/−4.1/−3.4/−1.4, and H1-2026 ~−3.9). But the fade is in the REAL TICKET (mix and
  commodity deflation), not in trips: the transaction base kept the surge. The nominal
  numbers hide a real fade in comp DOLLARS; they do not hide a volume exit. Pre-wave
  base rate for honesty: FY2016-19 OI grew only +7% TOTAL — TSCO was a mid-single-digit
  compounder before the wave, and the wave roughly doubled its scale.

### THE COMPETITOR ROW — required [E3-28]. Identical formula, filing-sourced.
*Return on unleveraged net tangible operating assets = operating income ÷ (total assets −
goodwill − intangibles − cash − non-interest-bearing operating liabilities); operating
lease ROU assets IN the base, lease liabilities treated as financing — uniformly. Full
arithmetic per company in the research file.*

| Company | OI / NTOA (pre-tax) | FY | source |
|---|---|---|---|
| **TSCO** | **18.50%** (FY2019: 18.27% — flat; incremental capital earned 18.74%) | FY2025 | 10-K 0000916365-26-000014 |
| BOOT (Boot Barn) | 17.65% | FY2026 (Mar) | 10-K 0001104659-26-061346 |
| WMT (consolidated; segment b/s not filed) | 23.03% | FY2026 (Jan) | 10-K 0000104169-26-000055 |
| DG (restated to this formula from the completed run) | 12.3–12.6% | FYE 2026-01 | run of 2026-09-02 |
| CHWY (pet attacker; NEGATIVE operating capital −$652M) | n/m | FY2025 | run of 2026-08-31 |

- **Peers named: 4 filers of an industry whose closest competitors do not file.** The
  direct-format peers — Rural King, Bomgaars, Atwoods, Family Farm & Home, C-A-L Ranch,
  Southern States and the co-ops — are **private; no document exists** that would build
  their row (the AATC situation, stated rather than stretched over). TSCO itself BOUGHT
  the 81-store Orscheln chain in 2022. The row's limit [E3-61] is therefore real: position
  can be shown only against the adjacent listed formats, and conduct not at all.
- **What the row shows:** TSCO's return is HIGH-STABLE (18.3 → 18.5% across six years in
  which NTOA doubled), **but it is not of the dominance class [E2-53]** — Boot Barn earns
  the SAME return (17.65%) one niche over, while opening 80 stores a year against a
  stated 1,200-store target and comping +7.2%. **Identical formulas produce matched
  returns; position is not setting super-normal economics, execution is.** Walmart U.S.
  comped +5.5/+4.8/+4.3 on a flat store base against TSCO's 0.0/+0.2/+1.2 across the same
  three years.
- **Untapped pricing power [E3-33]:** cannot be claimed — claiming it claims near-monopoly
  [E5-28], and EDLP + three years of nominal ticket decline is the filed opposite. [E4-37]
  reads the same way: no demonstrated ability to push price beyond commodity pass-through.

### [E2-45] THE ATTACKER RECORD — filed, not argued
- **Chewy (the pet flank, 24% of TSCO sales):** CHWY was **Q2 OUT in this project**
  (2026-08-31) as a business — but as an ATTACKER its filed record runs: net sales $8.9bn →
  $12.6bn in five years (+6.2% in FY2025), active customers back to peak at 21.3M,
  **Autoship 83.3% of sales**, on **negative net operating capital**. And TSCO's own
  filings concede this flank: H1-2026 comps were dragged by *"continued below-average
  performance in the companion animal category"*; **Petsense goodwill was impaired to
  ZERO and ~75 of 209 stores are closing (Q2-2026, $71.7M of charges — the SECOND Petsense
  impairment in six years, $74.1M in FY2020)**; and TSCO bought the online/services side
  of the same trade twice in 18 months (Allivet, online pet pharmacy, $135M, 12/2024;
  VIP Petcare, mobile vet, $133.8M, 5/2026). **The small-box pet moat is not holding and
  the filer's own capital allocation says so.** Recorded as a moat defect on 24% of sales.
- **Amazon in farm/feed:** the brief's structural argument (bulky, low value-per-pound)
  has **no filed support either way — "Amazon" appears ZERO times and "bulky" ZERO times
  in the FY2025 10-K** (checked absences). The filing names only *"internet-based
  retailers"* generically and flags *"increased presence of online retailers"* as a comp
  risk. Unlike ORLY (which filed its structural defence: "We do not sell tires"), TSCO
  files no freight-economics defence. The farm-core attacker question is **unevidenced in
  either direction** from primary documents.
- **Boot Barn (the western/rural flank):** the sharpest LISTED analogue: 539 stores,
  +7.2% comps, 17.65% returns, 1,200-store target — capital IS entering rural retail at
  TSCO-like returns. Overlap is the apparel/gift slice (~10% of TSCO sales) plus
  customer-base adjacency, not feed.
- `acquisition_flag()` context, run honestly: Allivet ($142.8M consideration, $100.3M
  goodwill, **no contingent consideration — checked absence**, allocation FINAL Q3-2025;
  the COKE flag does not fire) and VIP Petcare ($130.4M preliminary, $100.9M goodwill, no
  contingent consideration disclosed). Both under 1% of market cap each; the flag stays
  quiet on size and fires nothing on structure.

### Class and verdict
- **Primary moat metric, filing-sourced, and its trend:** return on unleveraged net
  tangible operating assets **18.27% (FY2019) → 18.50% (FY2025), flat through a doubling
  of the capital base**; comp transaction count cumulative **+28% over ten years with the
  pandemic surge retained**. Direction [E4-32]: **not widening — held at the core, conceded
  at the pet edge.**
- **[E3-62] the second step:** revenue +$7.17bn (2019→25) brought OI +$724M — incremental
  margin 10.1%, at/above the 9.45% aggregate (ex-SLB-gains ~8.8%, in line). Something
  stuck; contrast TGT (0.4%) and UAL (nothing).
- **Class: [x] NARROW.** The evidenced moat is trip-consolidation density in the farm
  core — needs-based demand, ~4x the nearest chain's store count, 81% self-distribution,
  and a physical series that held through a full price cycle. It is NOT WIDE: returns are
  matched by an adjacent attacker (BOOT), the pet flank (24% of sales) is being lost on
  the filer's own evidence, pricing power beyond pass-through is undemonstrated, and
  growth eats capital.
- **Direction: eroding at the edges, held at the core.** H1-2026 transactions −1.4% is the
  first adverse reading of the physical series since 2023 — **one half-year against two
  positive full years**; under [E3-30]/[E4-17] a moat belief changes gradually, and the
  same one-half-does-not-override rule that refused TGT's favourable H1 refuses TSCO's
  unfavourable one. It is pre-committed at Q6 as the thesis-breaking metric instead.
- **VERDICT: [x] IN — narrowly, and decided by the filed series, not the story:** the
  transaction count held through the 2022-25 price cycle and kept the pandemic surge
  [E4-55, E2-44(1)], the return on capital held flat-high through a doubling of the base
  [E3-46], and the disclosure record is decade-clean [E2-49]. The brief's fade hypothesis
  is TRUE of real ticket and real comp dollars but NOT of the physical series, and the
  physical series is the honest one [E4-55]. The pet-flank concession and the
  matched-return attacker are why the class is NARROW and cannot be more.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

*Research: `_research 2026-09-04 TSCO/proxy pay dividends.md` (2026 proxy accession
0001193125-26-126620; the sub-agent died mid-file and its tail was rebuilt by this thread).*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
- [x] **Daily execution [E3-38, E3-43]** — TICKED. A merchant retailer selling substitutable
  SKUs at everyday-low-price, repriced against Walmart, online and the co-ops continuously.
  Q2 found a NARROW moat, not a full franchise; *"a business, unlike a franchise, can be
  killed by poor management."* The DRI precedent: **Q3 is a GATE.**
- [ ] Control [E1-16] — marketable minority; exit exists.
- [ ] Leverage [E3-29] — funded debt $1.78bn against ~$0.9bn owner earnings; small asset
  errors do not destroy equity. (The $4.1bn lease book is rent, priced at Q4.)

**Honesty — binary, permanent, filings-based [E5-16].** No disqualifier found: no
restatement, no material weakness, EY unqualified since 2001, no NEO misconduct matter in
the filings read. The 2026-02-11 8-K is a director appointment, not an officer exit. CEO
Lawton since 2020-01; CFO Barton (routine 10b5-1 plan disclosed). *A pass here is the
absence of found disqualifiers, not a finding of honesty [E5-17].*

**STEP 2 — THE FLAGS [E4-22, E5-15].**
- [ ] weak accounting — SBC expensed; no pension; the two big estimates (shrink,
  self-insurance) carry filed 10%-sensitivities ($4.7M / $12.0M).
- [ ] unintelligible footnotes — Notes 1–13 are short and plain.
- [x] **trumpeted projections — the culture exists [E5-30]:** annual guidance ritual, every
  Q4 release. **But the record runs the honest way [E3-48]: FY2025 guidance was MISSED on
  net sales (+4.3% vs +5–7%), operating margin (9.45% vs 9.6–10.0%) and EPS ($2.06 vs
  $2.10–2.22) — and nothing bent to meet it:** the CIP took zero adjustments both years,
  the 2023 PSUs were **forfeited in full** (threshold missed on both metrics), and the
  Q4 release opens *"Our fourth quarter results came in below our expectations."* The
  ratchet risk is noted; the make-up-the-numbers corollary is not in evidence.
- [ ] serial share issuance — count falls every year; ESPP/awards only.
- [ ] EBITDA promotion [E4-29] — **zero occurrences** in the FY2025 10-K, the 2026 proxy
  and the Q2-2026 10-Q; "EBITDAR" appears only as the credit-agreement covenant definition
  (the ORLY distinction: a covenant computation, not a promotion).
- [x] **filed-figure tells [E4-30], read closely:** reported NI is unnaturally smooth —
  1,107.2 / 1,101.2 / 1,096.1 across three years — **and the smoothing agent is
  identified and DISCLOSED: sale-leaseback gains inside SG&A rose $41.7M → $62.2M →
  $91.7M (Note 6, plainly stated) while the ex-gain core fell three straight years
  (1,437.2 → 1,405.3 → 1,375.7).** No adjusted figure either trumpets or strips them; MD&A
  calls it *"a modest benefit."* Cash-tax % of pretax fell to 16.8% in FY2025 — explained
  in the filing itself ($168.9M of the federal figure is the discounted PURCHASE of
  transferable tax credits; OBBBA deferral +$61.3M). **Both tells fire and both resolve to
  disclosed mechanics, not concealment; the SLB-gain dependence is carried to Q4 as an
  earnings-quality fact, not held here as a conduct finding [E5-38].**
- [x] one metric-switch [E2-49]: the exclusive-brands redefinition (Q2), upward, recast,
  cosmetic in scale. Pay metrics (net income, net sales, GAAP EPS) unchanged for years.

**STEP 3 — THE PRIMARY TEST [E2-01].** Book equity is treasury-shrunk ($6.39bn of treasury
stock against $2.58bn of equity), so [E2-43]'s denominator is used: **operating income on
unleveraged net tangible operating assets 18.27% (FY2019) → 18.50% (FY2025), incremental
capital at 18.74% pre-tax (~14.5% after tax)** — a high, stable earnings rate achieved
without undue leverage or gimmickry, on a base that doubled. (EPS +17%/five years is partly
buyback arithmetic; not the test.)

**The half-owner test [E2-26]:** passes on the evidence above — the misses are stated as
misses, the Petsense failure was charged and explained twice rather than annualized away,
the SLB gains are quantified at every appearance, and the CIP targets were set ABOVE prior
actuals in both proxy years read (FY2025 NI target +4.1–6.2% over FY2024 actual; paid
80.8%; FY2024 target +2.0–4.0% over actual, paid 86.6%). **The DG/ULTA target-rigging
pattern does NOT replicate** — the brief's 3x-replicated flag comes back negative here.
One pay flag the other way: the threshold was lowered from 90% to 85% of target in FY2024
(disclosed), and FY2024's NI component paid 86.4% in a year NI FELL slightly. And one
scale flag: the **$20M one-time CEO retention grant (Nov-2025)** — the proxy itself notes
no comparable award in a decade; 60% is TSR-gated PSUs (55th percentile for target, capped
at 100% if absolute TSR is negative), 40% time-vested to 2031. Noted, sized, not a
disqualifier.

**The institutional imperative [E2-30].**
- [ ] resists change — no: Petsense cut by a third, online pet bought, EDLP held.
- [x] projects to soak up funds — the 80–100 stores/yr cadence plus DC #11 is a standing
  program; it earns 18.7% incrementally, so it is not yet soak-up, but the cadence never
  varies with the comp environment (100 more guided for FY2026 into negative comps).
- [ ] staff studies — not observable from filings.
- [x] peer imitation — buying the online/services side of pet (Allivet, VIP Petcare) as
  small-box pet fails is the sector's standard move; flagged as imitation-shaped.

**Capital allocation — the record, both directions.**
- **Petsense is a filed capital-allocation failure, handled candidly:** acquired 2016,
  impaired $74.1M (FY2020, with a one-time adjusted-EPS presentation), goodwill written
  **to zero** and ~75 of 209 stores closing (Q2-2026, $71.7M). No [E4-39] post-mortem
  published; the charges themselves were taken plainly. [E5-33]: both charges belong in
  any long-window mean and are in the figures used at Q4.
- **[E3-54] retention, five years FY2020→FY2025, both readings reported:** ~$3.35bn
  retained after dividends. At fiscal-2025-year-end prices (~$54) the market value change
  was ~+$12bn → **~$3.6 per $1 retained — passes**. At today's $34.99 the change is
  ~+$1.9bn → **~$0.6 per $1 — fails.** The swing is the 2026 sector repricing (−36% YTD);
  recorded as price-dependent, with the failure reading at the measurement date the run
  actually uses.
- **Buybacks [E5-08]:** condition (1) marginal — liquidity is a drawn revolver [E5-39];
  condition (2) **FLAG**: FY2023–25 tranches at $43.71 / $53.02 / $54.53 average sit at or
  above the top of this run's zero-growth value band (~$20–35/sh, Q5) — repurchases were
  made above conservatively-calculated IV for three years. Stated with the humility clause
  [E4-13]: the band is ours, management knows more, and every dollar was at prices the
  market itself paid until months ago. The pattern is NOT dollar-budget-blind: spend fell
  as price rose ($602.9M → $566.4M → $361.0M) and the FY2025 guide was undershot by a
  third. **Flag binds position size, never the rate.**
- Dividend record (Stage 0(b), the RPM test): raised every year for a decade (split-adj
  DPS 0.184 → 0.92), the FY2022 raise a one-time +77.9% reset. **The five-year RPM
  decomposition FAILS: ~34% earnings / ~8% retirement / ~58% payout expansion** (payout
  ratio 23.1% → 44.5% of NI). Post-reset (FY2022→25): DPS +24.3% vs NI +0.7% — no
  earnings leg at all. Softer than PEP (payout still only 44.5%), but the direction is
  the PEP direction and dividend growth from here needs earnings growth that has not
  appeared for three years.
- [E2-52] dividends funded by issuance: no — issuance is trivial against $487.7M paid.

**THE GUARDRAIL — checked.**
- [x] Nothing here promotes the name; Q2's class was set on its own evidence.
- [x] No key-person dependence to record; the moat, such as it is, is structural [E4-23].
- [x] No excisable-cancer case is being argued; the manager is not the plan.

- **VERDICT: [x] IN — as a GATE: no integrity disqualifier found; the primary test is
  passed on the level; the live flags are condition-2 buybacks, the RPM dividend
  decomposition, the guidance ratchet and the imitation-shaped pet acquisitions — all
  recorded, none disqualifying [E5-38]. IN never promotes.**

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
By year, $M, from the filed cash-flow statements (FY2023-25 cross-checked to the 10-K;
FY2021-22 XBRL transcription):

| FY | OCF | SBC | capex | D&A | OE (capex end) | OE (D&A end) |
|---|---|---|---|---|---|---|
| 2021 | 1,138.7 | 47.6 | 628.4 | 270.2 | 462.7 | 820.9 |
| 2022* | 1,357.0 | 53.8 | 773.4 | 343.1 | 529.8 | 960.1 |
| 2023 | 1,334.0 | 57.0 | 753.9 | 393.0 | 523.1 | 884.0 |
| 2024 | 1,420.8 | 48.4 | 784.0 | 447.2 | 588.4 | 925.2 |
| 2025 | 1,635.3 | 57.1 | 894.8 | 494.0 | 683.4 | 1,084.2 |

- **Short-window mean** (3-yr, FY2023-25): capex end **$598.3M** · D&A end **$964.5M**
- **Long-window mean** (5-yr, FY2021-25): capex end **$557.5M** · D&A end **$934.9M**
- **Spread, conservative end:** (964.5−598.3)/598.3 = **61.2%** (5-yr: 67.7%). **The
  screen's stored boundaries (554/oe_bottom, 74.1% spread) reproduce by hand to the
  million; the BRIEF's "spread 22.7%" does not reproduce from any construction on disk —
  logged at Step 0 as a brief defect. The true spread is wide.**
- **Distorted years inside the window, named [E4-25, E5-11]:** FY2021-22 carry the wave's
  working-capital swings; **FY2025 OCF carries ~$60-85M of one-time tax tailwind** (OBBBA
  deferred-tax swing +$61.3M vs −$22.6M prior year; disclosed) **[E4-41] — normalized
  down**; and every year's OI carries growing sale-leaseback gains (to $91.7M in FY2025)
  which the OCF construction correctly EXCLUDES (gains subtracted in the reconciliation,
  proceeds in investing) — the cash construction is cleaner than the income statement
  here, which is a point in the method's favor.
- **Maintenance capex — (c) is a DISCLOSED JUDGMENT, and TSCO files the evidence for it
  (the DG measured-split precedent applies):** the MD&A splits capex five ways every year.
  New/relocated stores $376.0M (FY2025) is growth; existing stores + IT + corporate =
  $391.0M (FY2025), $447.0M (FY2024), $293.3M (FY2023), plus the improvements share of DC
  spend (~$30-50M of $95.8-330.0M; the named projects — Maumelle, Nampa — are capacity).
  **Maintenance-ish spend ≈ $400-480M/yr, which brackets D&A (393.0/447.2/494.0): the
  [E3-44] D&A default is VALIDATED by the filed split, and this is NOT the [E5-20]
  exception class** — capex/D&A of 1.8x buys units (99 net new stores, DC #11, +4% sq ft),
  the filing never says depreciation understates renewal, and 97% of the store estate is
  leased so building renewal rides in rent, already inside OCF. Two considerations push
  (c) to the TOP of that bracket: Project Fusion remodels are competitive-position
  maintenance [E2-23] in a fleet whose real comp dollars are flat, and the IT spend
  ($158M/yr) is non-optional. **(c) judged $500M** (range $450-550M).
- **Owner earnings judged: ~$875M** = 3-yr mean (OCF−SBC) $1,409.2M, less ~$35M OBBBA
  normalization spread across the mean, less (c) $500M. **Displayed range $557-964M**
  (both windows × both capex ends). The range is wide but does not close the file: the
  verdict below is the same at every point in it.
- Stock compensation subtracted in full [E5-06]: yes, $57.1M (FY2025); reported charge
  used as the floor of the subtraction [E3-70] — at 0.37% of revenue the market-value
  correction is immaterial.
- Working-capital increment: included via the OCF construction [E2-23]; unit volume is
  growing, so the increments belong in (c) and are captured (inventory −$225.7M in FY2025
  OCF, netted against AP +$143.4M).
- Software capex (the HAS defect): checked — TSCO's cash-flow statement carries ONE capex
  line; IT capex ($158.1M) is inside the filed split, not a separate uncaptured line. No
  leakage.

### Great, good, or gruesome? **[E4-20]**
- [x] **good** — an attractive return (18.5% pre-tax on unleveraged net tangible operating
  assets) earned ALSO on added capital (18.74% incremental across a doubling of the base,
  FY2019→FY2025). Not great: the growth requires the capital (capex 1.8x D&A, plus $928M
  of new lease liabilities signed in FY2025 alone); OE per dollar of revenue is thin
  (~5.6%). Not gruesome: the added dollars earn well above the bond. *"Nothing shabby"
  [E4-43] — the good class passes Q4 and ranks below great at Q5.*

### Staying power — score all three **[E5-11]**
- (1) **Large and reliable earnings — PASS, strongly:** operating income ROSE through the
  GFC (2008: $178M → 2009: $192M → 2010: $266M) and through 2020; half the basket is
  needs-based consumables. The most defensible earnings stream in the specialty-retail
  cohort after ORLY's.
- (2) **Massive liquid assets — FAIL:** $194.1M of cash (FYE) / $231.6M (H1-2026) against
  $1.78-2.17bn of borrowings; liquidity is a $1.2bn revolver that was **drawn $230M at
  FYE and $620M at H1-2026** — [E5-39] refuses to count bank lines, and this filer is
  actually using them for seasonal inventory build and acquisitions.
- (3) **No significant near-term cash requirements — PASS, with the revolver named:** no
  bond matures before Aug-2029 ($150M), then Nov-2030 ($650M), 2033 ($750M); no current
  portion of long-term debt on the balance sheet at all. The near-term items are the 2027
  revolver maturity (extension options, $620M drawn at H1) and $619.7M of 2026 operating
  lease payments, which are rent, paid from operations. The buyback ($375-450M guided)
  and one-third of the dividend are discretionary — the anti-UAL pattern.
- **Leverage, named and quantified [E4-16]:** borrowings $1,780M (FYE) ≈ 2.0x judged OE;
  finance leases $36.1M (immaterial — but **ASC 842 is NOT immaterial here on the
  OPERATING side: $4,141.7M of lease liabilities at a 10.8-year weighted term, growing
  $928M/yr, IS the store network**, and the sale-leaseback program moves ~$250M/yr of
  owned stores into that book, monetizing the estate at a booked gain while adding
  fixed rent). Coverage [E2-54]: cash flow net of ample capex (OCF $1,635M − total capex
  $895M = $740M) covers cash interest ($69.8M) **~10.6x**; the covenant fixed-charge
  test (≥2.0x incl. rent) is in compliance. Wallet stays open.
- **[E2-60] restricted earnings — FIRES at the conservative construction, three years
  running:** FY2023-25 dividends + buybacks $2,926M against capex-end OE of $1,795M
  (1.63x), bridged by +$602M of net new borrowings and **$478.7M of sale-leaseback
  proceeds — the payout is partly funded by selling the estate and renting it back.** At
  the D&A-end OE (~$2,774M) the payout is 1.05x — marginal. Softening facts: the FY2025
  buyback was cut to $361M (guide undershot by a third), and H1-2026 buybacks slowed
  while the revolver funded VIP Petcare. Named, carried to Q6.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- **Mechanism 1 — the valuation death (the DG shape, one level deeper):** rural-lifestyle
  demand fade resumes (H1-2026 comp transactions −1.4% is its first reading), 100
  stores/yr keep opening into cannibalization (the filing names the proximity effect),
  and the sale-leaseback gain engine exhausts — only **3% of stores remain owned**, so
  the $91.7M/yr of gains propping the flat NI print has a visibly finite runway.
  Quantified: comp transactions −2%/yr for three years, SLB gains to zero, new-store
  contribution halved → OI ~$1.15-1.25bn, D&A-end OE ~$800M, judged OE ~$700M → value at
  the sovereign ~$13-15bn ≈ **$25-29/sh against $34.99 today**. [x] **a real
  possibility** — the ex-gain OI series (1,437 → 1,405 → 1,376) says its first three
  years are already filed.
- **Mechanism 2 — the solvency death:** a TGT-FY2022-shape inventory glut plus recession.
  Modeled: even FY2022's worst working-capital year left TSCO's OCF at $1,357M; interest
  coverage at the stress-year construction stays ~8-10x; nearest bond 2029; covenant
  headroom (≤4.0x funded debt/EBITDAR) wide. The GFC record (OI rose) is the on-record
  test. [x] **a low-level possibility** — the dividend and buyback absorb the shock
  before the balance sheet does.
- **[E4-40] exposure, not experience:** the exposure the benign history does not price is
  the **pet flank** — 24% of sales in the category where the filed attacker (CHWY) runs
  on negative capital and TSCO's own small-box format was just written to zero. A
  pet-category share loss of a quarter of that leg is ~6% of revenue at above-average
  margin — roughly the whole growth budget. Carried into mechanism 1's arithmetic.
- **VERDICT: [x] IN** — the staying-power profile is 2-of-3 with the middle failure
  (cash-poor, revolver-dependent) shared by ORLY and MCD before it, coverage is ~10x,
  and both named deaths are priced, not existential.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Q1 IN · Q2 IN (NARROW) · Q3 IN (gate) · Q4 IN — the SIXTH name in this queue's history
to clear all four business gates (after ORLY, BRK-B, MCD, HAS, COKE), and the first
merchant retailer to do it.** Q5 opens as a normal output, not a computation heading.

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: **~6.8-8.8% judged (full band 5.1-9.3%)** = the 4.80%
judged yield plus honest growth of +2-4% (what the record supports: revenue +2-4%/yr,
comps 0 to +1.2% for four years, OI ex-SLB-gains −2.2%/yr for two, FY2026 guided NI +1.3
to +6.7%, store adds at 18.7% incremental returns arguing the top of the band). **Below
roughly 10% on every construction → quit on, not ranked.** Growth needed for the floor is
**+4.7% to +6.9% perpetual** — roughly double the honest rate, and the [E4-35] base rate
stands against paying for it in advance.

**One book. Owner earnings against the bond.** No DCF was run; no vote was needed.

**1. THE YIELD**
- owner earnings **$875M judged ($557-964M displayed)** ÷ market cap **$18,231M** =
  **4.80% (range 3.06-5.29%)** · sovereign **5.25%** (US Treasury 30-yr, 2026-09-03)

**2. WHAT THE PRICE ALREADY ASSUMES**
- growth needed to justify the quote at the sovereign: **+0.45% perpetual** from the
  judged construction (= 5.25% − 4.80%); +9.4% in year one to yield the bond outright;
  from the bottom construction +2.19% perpetual
- what the business has actually done: comps 0.0/+0.2/+1.2/−0.6(H1); revenue +2.2 to
  +4.3%/yr; OE capex-end +10%/yr (construction-noisy); OI ex-gains **−2.2%/yr**
- **the strongest thing sayable for the price: matching the bare bond needs only ~+0.5%
  perpetual growth, which even the eroded record supports. The floor needs ~5-7%, which
  it does not.**

**3. WHAT YOU ARE PAID**
- return at the current price = **−0.45 points under the sovereign (judged); −2.19 to
  +0.04 across the band** — at the generous D&A end TSCO is bond-adjacent, the closest
  any retailer in this queue has come to the bond at its judged construction

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used ____ % — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:**
- zero-growth at the 5.25% sovereign: conservative **~$20/sh** (capex-end 5-yr) ·
  judged **~$30-32/sh** · optimistic **~$35/sh** (D&A-end 3-yr) — cap equivalents
  $10.6bn / $16.7bn / $18.4bn on 521,040,137 shares
- at the [E4-28] floor: **~$11-18.5/sh, judged ~$17**
- **current price $34.99** (2026-09-04, aggregator, flagged) — **at the very top of the
  zero-growth band; roughly 2x the floor value**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **~6.8-8.8%** vs ~10% **[E4-28]** —
  **below → quit on, and the ranking lines are not filled in.**
- *For the record only: even ranked, −0.45 points under the sovereign buys nothing the
  bond does not.*

**WHICH BAR ARE YOU USING?**
- [x] **Screamer test [E4-01]** — the price ($34.99) does not sit below the conservative
  case (~$20); it sits at the TOP of the whole zero-growth range. Outcome three: **no.**
  No margin was added on top.
- **Windage count: ONE** — (c) judged at the top of the filed maintenance bracket ($500M
  vs the $400-480M split evidence). The OBBBA normalization [E4-41] is realism, not
  windage; Bar 2 adds no end margin. **[E4-11]**

- **VERDICT: [x] quit on at the floor — FAIL ON PRICE. Not ranked. UNKNOWABLE and
  UNRESEARCHED do not apply; the evidence is complete and the answer is the price.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*No entry occurred; this section pre-commits the re-look terms for the watchlist [E1-02].*

**Pre-committed re-look: ~$30-32/sh at a 5.25% sovereign, recomputed at the rate of the
day.** At that price the judged yield meets the bond and the floor question is re-asked,
not pre-answered.

- **Thesis-confirming metrics:** comp transaction count positive for FY2026; ticket
  within a point of CPI; pet flank stabilized (Companion Animal holding ~24% of sales);
  Nampa DC absorbed without margin damage.
- **Thesis-breaking metrics and thresholds (these reopen Q2's direction question, which
  the H1-2026 reading has already put on watch [E3-30]):**
  1. **FY2026 full-year comparable transaction count negative** — the physical series
     failing for a full year, not a half;
  2. **[E2-49]: withdrawal of the transactions/ticket decomposition** from the MD&A —
     the decade-clean disclosure ending is itself the signal;
  3. **SLB-gain dependence deepening**: gains >$100M/yr, or the owned pool (3% of
     stores) exhausting while NI still prints flat;
  4. Companion Animal share of sales below ~22% (the CHWY flank cutting into the core
     mix);
  5. Buybacks re-accelerating above the judged value band while the revolver funds them
     ([E2-60] + condition-2 together).
- Next catalyst dates: Q3-2026 10-Q (~2026-11); FY2026 10-K (~2027-02) with the
  full-year transaction print.

**The monitoring question [E4-17, E3-30]:** is the H1-2026 transaction decline an
aberrational half (seasonal softness, May weather, as management frames it) or the start
of the permanent slip the real-comp series has hinted at for four years? Slow to
conclude; the FY2026 full-year print decides which file it goes in.

**Position size — none.** The name failed at the floor; the condition-2 and [E2-60]
flags would have sized it down even above the floor.

- **VERDICT: [x] IN as a monitoring plan; no position exists to sell.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped; Q5 opened only after Q1-Q4 all IN
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — the 2026-07-15
  v3.0 run's "PASS (provisional)" at its Gate 3 is superseded by this file
- [x] No UNRESEARCHED verdicts issued
- [x] No UNKNOWABLE verdicts issued; the private-peer gap at Q2 is stated as a row limit
  (no document exists — not a work order)
- [x] Step 0: FY2025 10-K read (MD&A, cash-flow detail lines, Notes 1-13), accession
  0000916365-26-000014; OCF and capex cross-checked to the thousand
- [x] Owner earnings on multi-year means (3-yr and 5-yr shown); capex band displayed;
  (c) disclosed as a judgment ($500M) against the filed five-way split
- [x] Competitor row filled on one formula (TSCO/BOOT/WMT/DG + CHWY attacker); private
  non-filers named as the row's limit [E3-61]
- [x] Sovereign 5.25%, USD (the earnings currency), US Treasury daily par curve
  (issuing authority), 2026-09-03
- [x] Value as a round-number range (~$20-35 zero-growth; ~$11-18.5 floor)
- [x] One bar (Bar 2, screamer); windage count ONE, stated
- [x] Price $34.99 dated 2026-09-04, aggregator, flagged as live-quote-only
- [x] Committed after Step 0, Q1, Q2, Q3, Q4, and at close (write-early protocol;
  survived one session kill with zero question loss)

**Brief defects found (assume some, the brief said):**
1. The screen row's "spread 22.7%" does not reproduce from any construction on disk; the
   true capex-vs-D&A spread is 61-74%. Yield 3.29% reproduces (3-yr bottom ÷ the 09-01
   triage cap).
2. "Neighbor's Club loyalty covers a very high share of sales" — **unverifiable from
   filings**: no member count or member-share-of-sales figure has EVER appeared in a TSCO
   10-K or proxy; the claim lives in earnings releases only.
3. The Amazon "bulky, low value-per-pound" structural argument has no filed support either
   way — "Amazon" and "bulky" both appear zero times in the FY2025 10-K.
4. RUSHA is a truck-dealership network (Rush Enterprises), not a farm-retail comp; left
   out of the row deliberately.
5. The brief asked whether TSCO discloses new-store vs maintenance capex: it does better —
   a five-way split, filed annually (the DG measured-split precedent applies directly).
6. [E4-52] restructuring streak: does not exist at TSCO — five consecutive clean years
   (FY2021-25), zero uses of "restructuring" in ten years of 10-Ks until the Q2-2026
   Petsense plan; the pattern here is two Petsense impairments six years apart, not a
   streak.
7. Target-below-actual pay rigging (replicated 3x elsewhere): does NOT replicate — both
   proxy years read set targets ABOVE prior actuals and paid below target.

**Tool defects (standing):** run.py share basis is a weighted-average EPS denominator
(532.2M vs the 521.0M cover count); its capex tag read is complete for TSCO (single
capex line — no software-line leakage here, unlike HAS/DRI).

## REGISTER
- Verdict: **[x] FAIL AT Q5, ON PRICE, at the [E4-28] floor — about the price, not the
  business. Q1 IN · Q2 IN (NARROW) · Q3 IN (gate, no disqualifier) · Q4 IN.**
- One line: **the first merchant retailer to clear all four gates — the filed transaction
  series held through the price cycle where DG/TGT/DRI's collapsed — but at $34.99 the
  judged yield is 4.80% against a 5.25% bond and the floor needs ~5-7% perpetual growth
  the record does not support; quit on, with a pre-committed re-look at ~$30-32.**
