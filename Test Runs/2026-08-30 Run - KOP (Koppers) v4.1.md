# Company Run — Koppers Holdings Inc. (NYSE: KOP) — 2026-08-30
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`. Evidence pack:
`Test Runs/_research 2026-08-26/KOP evidence pack + competitor row (SJ).md`.

**Position context: NONE HELD. Fresh entry run.** Surfaced by the dividend lens (sweep:
cap ~$879M, 6.0% statute yield). **Bias declared per operator rule 9:** ~$2,750 of
taxable capital seeks a dividend payer that compounds, so the analyst's incentive is to
clear this name. The iron prescription [E4-51] is applied; disconfirming evidence hunted
hardest [E4-26]. **A "no" verdict is a fully successful run.**

**Brief corrections, against the filings (the text wins):**
1. **The dividend is smaller than the brief's ~1.4%.** The filed rate is $0.09/quarter
   ($0.36/yr; Q3-2026 declared 2026-08-05), which at the verified $46.56 close is
   **0.77%**. The ~1.4% figure corresponds to a ~$26 share price — the stock's January
   2026 level (the 2026-01-03 PSU grant price was $26.93, DEF 14A/10-Q) — and the shares
   have since risen ~73%. The yield the sweep saw no longer exists at this price.
2. **The sweep's "6.0% statute yield" is reproduced** as FY2025 owner earnings at the
   friendliest (c): ($122.5M OCF − $13.8M SBC − $55.0M guided capex) ÷ $879M ≈ 6.1%.
   It is the best single-year, best-(c) case, not the mean — see Q4.

**The quarter that redefines the company, read before any gate:** on 2026-05-08 KOP
announced the shutdown of coal tar distillation at Stickney, Illinois — its founding
business — taking a $215.8M Q2-2026 charge that cut book equity from $549.5M to $387.0M
in one quarter. Two treating plants (Vance, AL; Florence, SC) were idled the same
half-year. This run tests the company as filed, not the company the transformation
promises for 2028.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · 2026-08-27 · FRED DGS30** via `fredgraph.csv` direct (the
  operator-directed route; `tools/sources.py` USD bypassed per brief). FRED's 1-2 day
  lag noted, immaterial. Majority-USD earnings (US revenue $1,280.9M of $1,879.3M,
  FY2025 10-K geographic note); AUD/EUR minorities noted, not separately discounted.
- FX: quote currency = reporting currency = USD. (CADUSD 0.7195, Yahoo aggregator
  2026-08-30, flagged — used only for competitor scale context.)
- Price: **$46.56, NYSE close 2026-08-28 (Yahoo — aggregator, live quote only, flagged).**
- **Market cap, verified as tasked:** 18,911,568 shares (filed cover count, Q2-2026
  10-Q, as of 2026-07-31) × $46.56 = **$880.5M**, against the sweep's ~$879M: a 0.2%
  gap. **Verified.** Book value $387.0M at 2026-06-30 → $20.47/share; **price/book
  2.27×** post-impairment (1.58× on YE2025 book of $29.51/share).

**The filing was read — not tagged data [E3-27]:**
1. **FY2025 Form 10-K, filed 2026-02-26, accession 0001315257-26-000012** (year ended
   2025-12-31; auditor KPMG LLP) — [x] MD&A [x] cash-flow statement incl. detail lines
   [x] footnotes (debt Note 15; commitments/environmental Note 17; leases Note 16;
   segments; goodwill assumptions; critical accounting policies; Item 1 business; Item
   1A leverage and competition risk factors; Item 3; Item 5 buyback table).
2. **Q2-2026 Form 10-Q, filed 2026-08-06, accession 0001315257-26-000048** (period
   2026-06-30) — full read: restructuring Note 2, derivatives Note 4, segments Note 7,
   taxes Note 8, debt Note 11, commitments Note 12, MD&A.
3. Q1-2026 Form 10-Q, accession 0001315257-26-000038 — series only, not fully read.
4. DEF 14A, filed 2026-03-27, accession 0001315257-26-000026 (comp, ownership,
   say-on-pay).
5. Earnings 8-Ks for the [E3-48] ledger: 2025-02-27 (acc. 0000950170-25-028398, initial
   FY2025 guidance), 2026-02-26 (acc. 0001315257-26-000010, FY2025 results + initial
   FY2026 guidance), 2026-08-06 (acc. 0001315257-26-000046, revised FY2026 guidance);
   CFO 8-K 2026-01-09 (acc. 0001315257-26-000004).
6. Competitor: Stella-Jones 2025 Annual Report (audited IFRS statements) and Q2-2026
   fact sheet, both from stella-jones.com IR (English) — route unobstructed, recorded.
- **Figure cross-checked against the filed statement:** FY2025 OCF. Filed consolidated
  statement of cash flows reads "Net cash provided by operating activities **122.5**";
  MD&A prose "$122.5 million"; XBRL companyfacts $122.5M. Three-way match. Second
  check: H1-2026 OCF "96.3" in the 10-Q statement = release prose. Match.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words:** three legs. (1) RUPS (49% of FY2025 sales): buy
  hardwood from hundreds of small sawmills, air-season it six to nine months, pressure-
  treat it with creosote at 18 plants sited on the customers' own rail lines, sell
  crossties to the six-ish Class I railroads (~75% under long-term contracts, all Class
  I served) and treated pine poles to utilities (8 of the top 10). Hardwood is ~70% of
  a finished tie's cost. (2) PC (29%): make copper-based wood preservatives from ~30M
  lbs/yr of scrap copper and sell them to 10 of the 11 largest US lumber treaters —
  a chemicals formulator riding deck-and-fence repair/remodel demand. (3) CMC (22%):
  distill coal tar — a byproduct of coke-making — into creosote (fed to RUPS), carbon
  pitch (aluminum smelters), naphthalene and carbon black feedstock. Profit = treated
  units × (price − wood/copper/tar − freight) − a heavy fixed plant network − $66M of
  interest.
- **The scarce input the business controls:** the treating-plant network sited on
  Class I rail lines with 6-9 months of seasoning inventory — a real logistics barrier
  — plus internally-sourced creosote. Honestly stated: the second is a wasting asset.
  The filing says coal tar supply is in "long-term decline" with blast-furnace steel,
  and the company is now shutting its own North American distillation and substituting
  "petroleum-blended products." Hardwood, copper and tar are all market-priced.
- **Ten years:** RUPS and PC will look broadly the same (450M-tie installed base,
  18-22M ties/yr replacement demand, poles aging; the 10-K expects the tie market
  "stable"). CMC will not — the shrink is filed and in progress. Legible, cyclical,
  understandable.
- **VERDICT: [x] IN** — the business is understandable; what it lacks is not
  intelligibility.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — ties and poles are replacement-cycle infrastructure.
- Not price-regulated **[x]**.
- No close substitute **[ ] — FAILS on the subject's own filings.** The 10-K risk
  factors state it in one sentence: **"We believe that the most significant competitive
  factor for our products is selling price."** Concrete/composite ties and steel poles
  exist at the margin; the binding substitute is simply the other treater's identical
  tie: the CEO's own 2026 outlook concedes **"net price erosion due to hyper
  competitive market conditions"** (8-K 2026-02-26) and the 10-Q MD&A opens with "the
  current intensely competitive environment" and "an increasingly cost-conscious
  customer base."

**The commodity doctrine [E2-58] governs, and the filing supplies its own evidence.**
The 10-K on CMC: **"For years, the coal tar distillation industry has operated in an
excess capacity mode"** — persistent over-capacity without administered prices, the
[E2-58] equation verbatim. The Stickney shutdown note is the equation's outcome: "unit
operating costs outpacing our ability to capture higher pricing." The one [E2-58]
exception is a cost advantage **wide and sustainable**; tested against the row below.

**The two-characteristic test [E2-44]: 0 of 2.**
1. Raise prices when demand is flat and capacity not fully utilized? No. Demand is flat
   by the company's own market data (RTA: 19.9M ties 2025 → 19.8-19.9M 2026), capacity
   is filed as underutilized (two plants idled in Feb 2026 for "plant underutilization,
   redundancy"), and prices are falling: Q2-2026 RUPS sales fell on "price decreases
   across multiple markets, particularly for crossties"; carbon pitch prices −6%
   (2025), −2% more (Q2-2026); PC prices lower in Europe. The FY2025 crosstie price
   increases ($11.0M) were cost recovery that reversed within two quarters — [E4-37]
   agony pricing, not a prayer session but a permanent negotiation.
2. Grow dollar volume with only minor additional capital? No. The filed decade: revenue
   $1,637.0M (2019) → $1,879.3M (2025), +2.3%/yr nominal, bought with $601M of capex
   (2019-2025), $134.7M of tagged acquisitions (2022-2025) on top of the pre-2019
   debt-funded deal era that left $1,002.6M of debt against $67.0M of equity at
   YE2018 — and now $292.4M of cumulative impairment/restructuring charges taking part
   of that capital back out. This is [E3-62]'s second step worked in filings: the
   Nyborg "yield enhancement project" and "projects to increase distillation yields"
   were vendor-projection capex into a commodity line; the gains flowed through to
   customers, and the line is now being shut.

**The claimed advantages, tested.** The 10-K claims two: internally-sourced creosote
and "our national network of treating plants which have direct access to our major
customers' rail lines." The network is real (a genuine logistics barrier; 75% long-term
contracts; all Class I railroads served). But the creosote leg is being dismantled by
its own economics (Stickney shut; supply shifting to Denmark and petroleum blends) —
a moat whose **basis must be replaced**, [E4-04]'s excluded class — and the network leg
must answer the row: does it produce a wide, sustainable cost advantage?

**THE COMPETITOR ROW [E3-28]** — the 10-K names **one principal competitor** in ties and
poles: Stella-Jones Inc. Row built from SJ's audited FY2025 IFRS statements and Q2-2026
fact sheet (stella-jones.com IR, English, route unobstructed); full table in the
evidence pack. Ratios are currency-independent; scale converted at CADUSD 0.7195
(aggregator, flagged).

| same metric, same window | **KOP** (US GAAP) | **Stella-Jones** (IFRS, CAD) |
|---|---|---|
| FY2025 ROE (NI ÷ avg equity, filed) | **10.5%** | **16.9%** |
| FY2024 ROE | 9.8% | 17.8% |
| FY2025 operating margin | 8.9% (11.7% pre-charges) | 14.8% |
| FY2025 sales growth | −10.2% | +0.7% |
| net debt / adj EBITDA | 3.3× (covenant basis) | 2.6× |
| ties revenue | $551.5M | ≈C$803M ≈ US$578M |
| utility products revenue | $304.6M | ≈C$1,711M ≈ US$1.23B (~4× KOP) |
| 5-yr share-price total return to YE2025 (each filer's own 10-K/AR graph) | $100 → $89.66 | n/a (not pulled) |

- Peers named: **1 of the ~2 principal competitors the industry has in ties/poles**,
  plus "several smaller regional competitors" (10-K), all private; CMC's principal
  competitor Rain Carbon Inc. is private; PC competitors unnamed and private. KOP's own
  Item 5: its competitors are "principally privately held concerns or subsidiaries."
  The row limit [E3-61] stands: structure shown, conduct not derivable. **No moat
  class is being claimed that would need the missing private rows — the verdict below
  rests on the subject's own filed concessions plus the one principal peer, so
  PROVISIONAL does not arise.**
- **The dominance test [E2-53], answered by the row:** KOP is the self-described #1 in
  crossties, and position does not carry it — the #1 earns 10.5% on equity at 3.3×
  net leverage while the other principal earns 16.9% at 2.6×. Good or bad, it does
  NOT prosper on position; that is the opposite of the dominance class.
- **Units [E4-55]:** no physical unit series is disclosed; the dollar series must
  serve, and it shows the [E4-55] pattern's cousin — FY2025 revenue −10.2% with volume
  losses in Class I crossties and a filed **"shift in United States market share"**
  against PC (volumes −17% in 2025), partially recovered in H1-2026 by... price
  concessions (PC +11% volume, "lower prices").
- **Untapped pricing power [E3-33, E5-28]:** claiming it claims near-monopoly; a #1
  losing share to its one principal competitor and idling a tie plant because its
  largest customer cut its forecast (Florence, SC — filed) has none.
- **Moat direction [E4-32]:** narrowing on every filed axis — the CMC leg exiting, PC
  share lost in 2025, crosstie pricing negative in 2026, the vertical-integration
  rationale (internal creosote) being unwound by the Stickney closure.
- Class: **[x] NONE** (commodity class; the network advantage is real but the row
  shows no wide-and-sustainable cost exception — the [E2-58] exception fails). The PC
  segment is the closest thing to a narrow-moat asset in the portfolio (global-leader
  position, 18.9-21.9% adj EBITDA margins, 10 of 11 largest treaters as customers) —
  recorded honestly — but it lost double-digit share in one year, and this run buys
  the whole company, including CMC and the balance sheet, not a segment.
- **VERDICT: [x] OUT.** Under [E3-03] a franchise's customers must believe it has no
  close substitute; KOP's own 10-K says the most significant competitive factor is
  selling price, its own releases say prices are eroding under "hyper competitive"
  conditions, the two-characteristic test scores 0 of 2, the [E2-58] doctrine is
  conceded verbatim for the historic core business, and the one-principal-peer row
  shows the peer earning half again KOP's return at lower leverage. What remains is a
  legible, substantial, heavily-levered **commodity processor mid-amputation** — in
  the class where "a business, unlike a franchise, can be killed by poor management"
  [E3-43]. **The entry run stops here. [E5-13]: most names should end here, and that
  is the system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT — the hard sequence closes
the file for any BUY decision. No position exists, so no [E2-28] hold read is required.
Everything below is FOR THE RECORD — the operator tasked this run with the leverage
weight question, the [E2-54] coverage test, the [E2-60] restricted-earnings check, the
quantified deaths, and Q6 regardless. **Everything below operator rule 3's header.
Nothing below is entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands
regardless; Q3 can stop a run, never start one.*

**STEP 1 — THE WEIGHT CASE (the operator's named question).** [x] **Leverage HIGH** —
the [E3-29] determinant fires on the debt footnote, read as tasked [E3-52]: total debt
$905.7M (Q2-2026) against $387.0M book equity; **100% of it is secured bank paper** —
revolver $427.0M at 5.56% + Term Loan B $478.7M at 6.15% — first-priority lien on
substantially all assets, covenanted (net leverage ≤4.75×, actual 3.3× at YE2025; cash
interest coverage ≥2.0×, actual 4.4×), **every dollar maturing in 2030** (ladder: $4.9M
a year through 2029, then $916.7M). This is the exact opposite of [E3-52]'s
covenant-free, long-dated, customer-prepaid liability class. Rate hedged to 2030 via
swaps ($400M at 3.97% to Apr 2027, forwards at ~4.0% after). [~] Daily execution
MODERATE — a thin-margin processor with commodity inputs must run well continuously;
not retail-grade, but no franchise cushion exists (Q2). [ ] Control — no.
**One determinant high → Q3 would be a BINARY GATE for entry; no price compensates
[E3-29, E5-35].**

**Honesty — the binary [E5-16]:** no integrity disqualifier found. The sweep, named:
Item 3 / Note 17 (10-K) and Note 12 (10-Q) carry environmental and regulatory matters,
not financial dishonesty toward owners; the IL AGO air-emissions complaint (filed
2026-06-17, Cook County — civil penalties sought over Stickney permit violations;
probable penalty accrued) is the TJX-class distinction: an environmental-compliance
failure, real and adverse, not dishonesty toward owners. Disclosure conduct around it
was read: the 10-K (Feb 2026) disclosed the referral with no reserve; the 10-Q
disclosed the complaint, the accrual, and that the settlement may require the very
plant closure management frames as economic — both facts are on the page for a reader
who reads both notes. No restatement, no SEC enforcement, no related-party matter
found in the documents read. Worded per the absence-claim rule: no instance found, not
"none exists."

**STEP 2 — THE FLAGS [E4-22, E4-29, E5-15, E4-30, E2-49, E2-52, E3-53].**
- [x] **Trumpeted projections [E4-22] — FIRED, with the [E3-48] ledger run as tasked:**
  FY2025 guidance (Feb 2025): sales ~$2.17B, adj EBITDA ~$280M, OCF ~$150M. Outturn:
  $1.88B / $256.7M / $122.5M — **misses of 13% / 8% / 18%**. FY2026 guidance then cut
  twice inside six months (adj EPS $4.20-5.00 → $3.80-4.60 → $3.80-4.20; adj EBITDA
  $250-270M → $240-250M). Against this record the MD&A carries a three-year promise:
  "a roadmap to reshape our company into a higher earning, higher margin, higher free
  cash flow and higher return on capital business by the end of 2028." [E5-30]'s
  ratchet applies; the outturn record is the base rate for the promise.
- [x] **EBITDA / adjusted promotion [E4-29] — FIRED, institutionalized.** The filing
  itself: "adjusted EBITDA represents the most relevant measure of segment profit and
  loss," and it is "the primary measure used to determine... management's short-term
  incentive goals." Adjusted EPS 2025 of $4.07 vs GAAP $2.74 — a 49% uplift — with
  the adjustments deleting $51.9M of impairment/restructuring (a real cost in 2 of the
  last 3 years, $292.4M cumulative; [E5-33]: to tell owners year after year "don't
  count this" is misleading), LIFO in every period, and MTM hedging. "Record free cash
  flow" headlines (H1-2026) ride a working-capital release while $38.4M of accrued
  Stickney cleanup cash sits unpaid downstream — the record is partly timing.
- [x] **Metric-switching [E2-49] — noted, half-fired:** PSU metrics for 2026 grants
  switched from 3-yr cumulative adjusted EBITDA (which had gone flat: $261.6M →
  $256.7M) to adjusted EPS + free cash flow with an adjusted-EBITDA-margin modifier —
  the new yardsticks match the new narrative (EPS via buybacks, FCF via working
  capital). Announced ahead with reasons in the proxy, which is the candor case's
  form; the direction of travel still followed the deterioration.
- [ ] Serial share issuance [E5-15] — NOT fired, the reverse: diluted shares 21.5M
  (2023) → 20.4M (2025) → 18.9M cover count (Jul-2026); no dividends-by-issuance
  [E2-52] (dividends $6.4M vs issuance proceeds $1.4M, both trivial).
- [ ] Filed-figure tells [E4-30] — NOT fired: growth is visibly lumpy; cash taxes ÷
  pretax bounce (19.6% · 21.7% · 27.5% · 39.8% · 11.6%, 2021-2025) with the 2025 drop
  explained by the pension settlement; no unnatural smoothness.
- [ ] Weak accounting basics — not fired: SBC expensed, LIFO inventories (conservative
  in an inflation regime), the US qualified pension terminated and annuitized 2025 (a
  balance-sheet-shrinking act), unqualified KPMG opinions, effective ICFR attestation.
- **Convergence [E4-52] — the finding:** the guidance culture, the adjusted-measure
  promotion, and comp tied to the adjusted measure all push one direction: report the
  transformation as better than GAAP shows. One reinforcing system, sitting exactly
  where a binary-gate Q3 looks.

**STEP 3 — THE PRIMARY TEST [E2-01], scoped by [E2-47/E2-43].** Balance sheet first
[E5-27]: equity $67.0M (YE2018, the residue of the debt-funded acquisition era, against
$1,002.6M of debt and two loss years 2014-15) rebuilt to $574.3M (YE2025) from retained
earnings — issuance trivial, buybacks net negative — then cut to $387.0M by the Q2-2026
write-off. Debt $1,002.6M → $905.7M over the same eight years. That is a real repair
record, and it is also why raw ROE is unusable early in the window ([E2-47]: unusual
debt-equity ratios — 2019's "59% ROE" is $66.6M of earnings on $112.9M of average
equity). On the [E2-43] basis — return on average total capital (NI + after-tax
interest ÷ avg debt+equity), computed and labelled an estimate: **9.7% (2021) · 7.8%
(2022) · 10.9% (2023) · 7.0% (2024) · 7.0% (2025), mean ≈ 8.5%** — below the 10%
opportunity-cost bar in four of five years, below Stella-Jones throughout, achieved
with undue leverage present. The hand [E3-59] is a genuinely hard one (dying input
stream, six customers with total power); it has been played energetically —
restructuring 2014, again 2020, again 2024-26 — without ever reaching distinction.

**Institutional imperative [E2-30], scored:** (1) resists change — NOT fired: this
management amputates (phthalic 2024, Stickney 2026, two plants idled, railroad
services sold, pension terminated). (2) Projects/acquisitions soak up funds —
partially fired: Brown Wood $99.3M (2024) and Greenhill $20.7M (Dec 2025) bought at
3.3× net leverage, and the CEO's stated intent to "evaluate inorganic growth
opportunities" continues while the balance sheet says deleverage. (3) Staff studies —
the "Catalyst" transformation runs on named consulting engagements ($21.0M cumulative
consulting in the restructuring table) — [E3-58]'s outsourced-allocation prompt fires
softly. (4) Peer imitation — the pole-market expansion tracks Stella-Jones's playbook;
noted, not damning.

**Capital allocation — the two buyback conditions [E5-08], plus [E2-60] as tasked:**
- Condition (1) ample funds: questionable. FY2025 dividends + buybacks = $44.6M against
  owner earnings of ~$35M (D&A-basis, Q4) — **~127% of OE returned** while net debt sat
  near $890M; H1-2026 returned a "record" $47.4M (buybacks $43.9M at avg ~$38.06)
  while the $38.4M Stickney cleanup accrual waits unpaid and the whole debt stack
  matures in 2030. The buyback pace runs at the Credit Facility's own $50M/yr baseline
  restricted-payments basket. **The [E2-60] restricted-earnings check fires:** the
  distribution is being made ahead of a named deleveraging-and-cleanup need; financial
  strength is the third dimension of maintenance, and these payouts draw on it.
- Condition (2) material discount to conservative IV: on THIS run's conservative
  numbers (bottom-boundary OE $30-55M, Q4), conservatively-calculated IV sits below
  the market cap — the repurchases at $28.60 (Nov 2025) were plausibly below IV; the
  H1-2026 purchases at ~$38 and any at today's $46.56 are **above the conservative
  case** and rest on management's adjusted-EPS view. Stated with the humility clause
  [E4-13]: they know the business better, and the flag binds position size only (none
  held).
- Comp and conduct: CEO Ball (11 years in seat) SCT total $6.36M for 2025 — 11.4% of
  a $56.0M NI year — but the annual cash incentive paid **$0** on missed 2025 targets
  (the plan enforced itself); ownership 780,721 shares ≈ 4.0% incl. options is real
  alignment; say-on-pay ~98% (2025). CFO Smith "retired" effective 2026-01-05, four
  years in seat, mid-transformation, interim CFO = the CAO, external search running —
  a watch item, not a disqualifier.

**THE GUARDRAIL:** [x] nothing here promotes the name (Q2 OUT stands; an energetic
restructurer cannot repair a commodity class [E2-37, E2-38, E3-39]); [x] no key-person
moat exists to record; [x] **the manager IS the plan** — the entire bull case is
Catalyst's 2028 pygmalion, which is [E2-36]'s named unbuyable class, not the
excisable-cancer case (the cancer being excised — CMC — was a third of the founding
business, and the franchise it leaves behind was not demonstrated at Q2).

- **Q3 FOR-THE-RECORD READ: no honesty disqualifier found; the entry gate would still
  not clear.** In a leverage-gated name, the guidance culture with a two-year miss
  ledger [E3-48], institutionalized adjusted-measure promotion [E4-29] tied to comp,
  the yardstick switch after the yardstick flattened [E2-49], and distributions ahead
  of the deleveraging need [E2-60] converge [E4-52] exactly where the gate looks. Set
  against them: honest GAAP statements, LIFO, a terminated pension, a shrinking share
  count, a zero bonus actually taken, real deleveraging since 2019, and 4% CEO
  ownership. *A pass here would be the absence of found disqualifiers, never a
  clearance [E5-17]; IN never promotes.*

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings — **COMPUTATION — NOT A CLEARANCE** [E2-23]
Convention: multi-year mean of (OCF − SBC) − (c). Both windows shown [E2-42, E4-25];
the spread carried, not resolved by preference.

**The (c) judgment, disclosed:** this is a mid-intensity industrial. The D&A default
[E3-44, E2-41] applies in form, but the filed record complicates both ends: capex ran
far above D&A in 2021-2023 ($125.0/$105.3/$120.5M vs ~$57M) — partly growth, partly
defensive spend into the dying CMC line now written off — then below it in 2024-2025
($77.4/$55.0M vs $67.5/$73.6M), with 2026 guided at $55M and management claiming the
transformation "will lower our maintenance and capital requirements." Against the low
end: the plants are old, and deferred maintenance surfaces as cash at closure ($52-62M
of "plant cleaning, waste disposal and demolition" for Stickney alone). **(c) is
judged at $55M-$75M (guided-to-D&A), a disclosed guess per [E2-23]; the 5-yr actual
capex mean ($96.6M) is shown as the harsh cross-check, not blended.**

| basis | OCF−SBC | (c) | OE | yield on $880.5M |
|---|---|---|---|---|
| 5-yr mean 2021-2025 | $103.1M | D&A $62.4M | **$40.7M** | 4.6% |
| 5-yr mean 2021-2025 | $103.1M | actual capex $96.6M | $6.4M | 0.7% |
| 3-yr mean 2023-2025 | $112.0M | D&A $66.0M | $46.0M | 5.2% |
| FY2025 | $108.7M | D&A $73.6M | $35.1M | 4.0% |
| FY2025 | $108.7M | guided capex $55.0M | $53.7M (the sweep's 6.0%) | 6.1% |
| TTM at 2026-06-30 | $178.7M | $55-74M | $105-124M | 11.9-14.1% |

- OE by year at the D&A default: 32.3 (2021) · 33.0 (2022) · 71.8 (2023) · 31.1
  (2024) · 35.1 (2025).
- **The spread is the finding [E4-25]:** the TTM figure is 2.6-3.5× the 5-yr mean. The
  distortion is named: H1-2026 OCF ($96.3M vs $27.8M) carries a +$71.7M year-over-year
  working-capital swing, the absence of 2025's ~$14M pension funding, and none of the
  $52-62M Stickney cleanup cash that is accrued but unpaid — a spike, not a level.
  **Normalized DOWN per [E4-41]:** the TTM window is refused as an OE basis in
  writing; the company's own $110-130M FCF guidance is likewise refused as a basis
  (its provenance is the [E3-48] ledger above).
- **Bottom boundary [E5-34]: OE ≈ $30-55M** (the 5-yr and FY2025 rows at the disclosed
  (c) band). **Bottom-boundary yield ≈ 3.4-6.2% against the 5.19% sovereign** — the
  equity is priced to earn roughly the bond rate before any equity risk is carried.
- Stock compensation subtracted in full [E5-06]; reported charge used (no repricing
  found; options exercisable 423K at $30.10). No look-through increment [E3-04]: no
  material equity-method investees. LIFO carve-out noted per [E2-23]: KOP is LIFO on
  US inventories ($101.2M LIFO reserve), so flat-volume working-capital needs are
  modest — the convention's OCF basis nets this from the audited line.

### Great, good, or gruesome? [E4-20]
**Closer to gruesome than good over the filed decade, with the good class not yet
demonstrated.** The consolidated record: growth (+2.3%/yr revenue since 2019) that
required significant capital ($601M capex + $135M tagged acquisitions since 2019) and
earned 7-11% on total capital (mean ~8.5%) — below the ~12% the corpus calls "quite
satisfactory" [E5-40], with $292.4M of the spent capital now confessed as impairment.
CMC ran the gruesome sentence verbatim (grew via yield-enhancement capex, earned
little, written off). PC alone would test as good. Management's 2028 roadmap promises
exactly the migration from gruesome toward good; the promise is not a filed result.

### Staying power — score all three [E5-11]
1. **Large and reliable stream of earnings:** mid-sized and cyclical, not reliable at
   the GAAP line (NI $89.8M → $48.6M → $56.0M → TTM −$86.9M on the charge); adjusted
   EBITDA steadier ($256.7M vs $261.6M) but that is the promoted measure, not the
   bankable one. Partial.
2. **Massive liquid assets:** NO. Cash $40.7M against a $1.72B balance sheet; stated
   liquidity ($383M at YE2025, ~$390M at Q2-2026) is overwhelmingly the **undrawn
   revolver** — [E5-39] kindness-of-strangers capital by definition, from the same
   banks holding the first lien on everything. Fail as the corpus means it.
3. **No significant near-term cash requirements:** pass to 2029, then the wall:
   amortization $4.9M/yr through 2029, **$916.7M — the entire capital structure — due
   in 2030** (revolver Jan-2030, TLB Apr-2030). Nearer-term named cash: $60-75M of
   remaining restructuring cash (Stickney $52-62M cleanup + severance + PA tail) across
   2026-2027; ~$1.5M pension (terminated — genuine strength); purchase commitments
   $234.1M (2026) are market-priced pass-throughs. **The [E2-54] coverage test, run as
   tasked:** FY2025 pre-interest operating cash (OCF $122.5M + interest paid $63.5M =
   $186.0M), net of ample capex, against ALL interest payable and accrued ($66.1M
   expense; $63.5M paid): at D&A capex → **1.70×**; at guided $55M → 1.98×; at the 5-yr
   capex mean → 1.35×. FY2024 the same: 1.71×. Interest is met; **"comfortably" it is
   not** — one bad year of the 2024-25 kind at 2023 interest rates would put the ratio
   near 1. The covenant arithmetic: at $865M net debt, adjusted EBITDA below ~$182M
   breaches the 4.75× net-leverage test — a 27% fall from the guided $240-250M, within
   the observed range of segment swings (PC fell 28% in 2025 alone).
- Leverage, named and quantified [E4-16, E3-29] — no ratio ceiling exists in the
  framework and none is applied: total debt $905.7M · net debt ~$865M · book equity
  $387.0M · covenant net leverage 3.3× · every dollar secured, covenanted, and due in
  one year (2030), partially rate-hedged to maturity.

### The specific ways THIS business dies [E2-27, E3-24] — exposure, not experience [E4-40]
1. **Leverage meets the 2030 wall (the structural death):** $916.7M of secured bank
   debt matures inside a single year, refinanceable only on terms the 2029-30 credit
   market sets [E2-64 inverted]. Quantified: a downturn taking adjusted EBITDA to
   ~$182M (−27% from guidance; PC alone moved −28% in 2025) breaches the leverage
   covenant while the refinancing is being negotiated; the facility then owns every
   lever (dividends, buybacks, acquisitions, asset sales all restricted). The company
   survived 2018-19 at far worse ratios, which is experience, not exposure.
   **Likelihood: a low-level possibility in any given year; the refinancing event
   itself is certain, only its price is open.**
2. **The environmental tail (the legacy death) — footnote read as tasked:** reserves
   are **$10.0M** against "contamination... identified at most manufacturing and other
   sites of our subsidiaries," one owned NPL site, and Portland Harbor — a $1.1B-NPV /
   $1.7B-undiscounted remedy ("will likely increase") allocated privately among 60-80+
   parties **with the allocation expected to clarify by end-2026**. KOP's accrual for
   it is $3.8M on a de-minimis self-assessment the filing itself caveats ("actual cost
   could be materially higher"). Quantified: 1% of the undiscounted remedy ≈ $17M
   (≈2.5× the annual dividend); 5% ≈ $85M ≈ 22% of book equity. The load-bearing wall
   is the 1988 Beazer East indemnity (Beazer Limited guarantee) — unlimited in amount
   but **closed to newly-tendered third-party claims since July 14, 2019**, so new
   claims land on Koppers first; and if the indemnitor ever fails to perform, the
   pre-1988 legacy lands on a $387M-equity company. Creosote itself is the
   regulatory-pressure product KOP is uniquely integrated in. **Likelihood: a real
   possibility that the Portland Harbor allocation materially exceeds the $3.8M
   accrual; a low-level possibility for the indemnity failing.**
3. **Rail-customer power (the demand death):** six-ish Class I buyers take ~70% of all
   crossties; ~75% of KOP's NA railroad sales are long-term contracts with those
   buyers; one customer's forecast cut idled the Florence plant this year (filed).
   Quantified: RUPS adjusted EBITDA $108.1M (FY2025); a reversion to FY2024's margin
   (8.7% vs 11.7%) costs ~$28M ≈ half the bottom-boundary OE. A PSR-style
   maintenance-deferral cycle across two or three Class I's does this without any
   recession. **Likelihood: a real possibility, cyclically recurring.**
4. **The coal-tar input death (in progress, filed):** CMC's raw material shrinks with
   blast-furnace steel ex-Asia ("long-term decline of coal tar supply"); segment
   adjusted EBITDA ran $45.9M (FY2025) → $8.5M (H1-2026); the Stickney closure is this
   death being managed, at a filed cost of $233-252M plus the loss of the internal
   creosote advantage RUPS was built on. Quantified: CMC fading to zero removes ~18%
   of FY2025 adjusted EBITDA; the restructuring's remaining cash cost is $60-75M.
   **Likelihood: likely — it is happening; the open question is only the residual
   value of the European/Australian remainder.**
- **Q4 FOR-THE-RECORD READ: survives the current regime on the filed balance sheet —
  no maturity before 2030, covenant headroom real (3.3 vs 4.75), interest hedged,
  liquidity adequate if the banks stay friendly. It does not meet [E2-55]'s
  certain-under-adverse-conditions standard: leg 2 of [E5-11] fails outright, leg 3
  fails at the 2030 wall, and the [E2-54] coverage answer is "met, not comfortably."
  Were the gate live it would read IN on current-regime survival with those two legs
  failed and written.**

---
## Q5 — FOR THE RECORD — **COMPUTATION — NOT A CLEARANCE**
*(Q1-Q4 did not close IN; operator rule 3 header governs; no entry language.)*

**THE FLOOR [E4-28] — "that's the figure we quit on."**

**1. THE YIELD** (owner earnings ÷ market cap $880.5M · sovereign **5.19%**, FRED
DGS30 2026-08-27):
| OE basis | OE | yield | points over sovereign |
|---|---|---|---|
| **Bottom boundary [E5-34]** | **$30-55M** | **3.4-6.2%** | **−1.8 to +1.0** |
| 5-yr mean, D&A default | $40.7M | 4.6% | −0.6 |
| FY2025 at guided capex (the sweep's statute yield) | $53.7M | 6.1% | +0.9 |
| TTM spike (refused [E4-41], shown) | $105-124M | 11.9-14.1% | +6.7 to +8.9 |
| management-guided 2026 FCF (refused [E3-48], shown) | $110-130M | 12.5-14.8% | +7.3 to +9.6 |

**2. WHAT THE PRICE ALREADY ASSUMES:** $880.5M × 10% floor = **$88M of OE** — 60%
above the best filed single-year case at the friendliest (c), 2.2× the five-year mean
at the D&A default, and almost exactly the midpoint of management's guided 2026 free
cash flow. **The price IS the guidance.** Holding it means believing the roadmap of a
management whose last full-year guidance missed by 13-18% and whose current-year EPS
guidance has been cut twice in six months — a growth belief carrying [E4-35]'s burden,
against a filed record of ~8.5% returns on capital. The ceiling [E2-63] is stated: a
commodity processor's mean return caps the upside unless capital is continuously
reinvested above its cost, and the filed decade shows the opposite.

**3. WHAT YOU ARE PAID:** −1.8 to +1.0 points over the sovereign at the bottom
boundary — bond-rate compensation for equity-in-a-levered-cyclical risk — with the
entire excess return residing in a transformation not yet in the filed numbers.

**THE FLOOR VERDICT, stated plainly:** honest pre-tax expectancy at $46.56 ≈
bottom-boundary yield 3.4-6.2%, call it ~4-6%, plus whatever fraction of Catalyst
survives contact with the [E3-48] record. **The floor does not clear — it is not
close.** It clears only on the TTM spike or the guidance, both refused in writing
above. Bar: **screamer test only [E4-01]** — the price ($880.5M) sits at or above the
top of the honest range (below), which is the third box: **no.** Windage count:
**one** — the (c) band inside the bottom boundary; the refusals of the TTM spike and
the guidance are [E4-41]'s and [E3-48]'s required moves, not windage.

**The value, as a round-number range [E4-01], for the record only:** roughly
**$300-550M** (bottom-boundary OE at the 10% quit-rate — the price at which this file
would be re-read, ~$16-29/share) to roughly **$600M-1.1B** (bottom boundary held flat
forever at the bare sovereign, ~$31-56/share). The $880.5M cap sits in the top half of
even the flat-forever band and above the whole quit-rate band. A capitalization of
management's 2028 promise ($1.1-1.3B) is shown once and refused as a basis.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists; pre-committed yardsticks for the WATCH LIST, set prior to any act
[E1-02]. **Alert thresholds LISTED ONLY** — no shared file edited.)*

**Q2 REOPEN CONDITIONS (the only route back to entry) — BOTH required:**
1. **Evidence, not price:** Q2 failed on class, so the bar is structural: two or more
   post-Stickney fiscal years (FY2027-28 10-Ks at the earliest) showing return on
   unleveraged net tangible capital ≥ 12%, the ROE gap to Stella-Jones closed on the
   same-window row, crosstie/pole pricing holding without share loss, AND the 2030
   wall refinanced early into laddered maturities at survivable spreads. A guidance
   beat alone reopens nothing; the metric is the filed return, not the adjusted one.
2. **Price [E4-28]:** the bottom boundary pays the floor with zero transformation
   credited at **$300-550M ≈ roughly $16-29/share**. Below **~$25** this file gets
   re-read for the record; entry still requires condition 1, which today does not
   exist and cannot exist before the FY2027 10-K.

**Watch-list metrics and thresholds (review triggers, not auto-executions):**
- **Guidance ledger [E3-48]:** a third 2026 cut, or FY2027 guidance again above the
  filed run-rate = the culture confirmed; a clean FY2026 beat on the ORIGINAL February
  range = first contrary datum.
- **Leverage line:** covenant net leverage above 4.0× in any quarter = wall risk
  rising; any early refinancing of the 2030 stack = the single most thesis-relevant
  positive event; watch its pricing vs the current 5.6-6.2%.
- **Restricted earnings [E2-60]:** buybacks continuing above ~$40/share while net
  leverage exceeds 3× = the flag deepening; a dividend raise announced alongside a
  guidance cut = same.
- **Environmental tail:** the Portland Harbor private allocation (due ~end-2026) — any
  allocated share above ~1% of remedy costs = death 2 materializing; IL AGO settlement
  amount vs the undisclosed accrual; any Beazer East performance dispute reaching
  arbitration = re-read immediately.
- **Restructuring cash:** Stickney cleanup outflows vs the $52-62M estimate; total
  program cash vs $79-93M — overruns here are the deferred-maintenance tell.
- **The remaining business:** CMC-remainder adjusted EBITDA (Nyborg/Australia) — two
  quarters below ~$5M = the segment heading to zero; PC US share trajectory (volume
  vs price disclosure each quarter); RUPS crosstie pricing direction; utility-pole
  volume growth (the one filed growth market — data centers, grid hardening).
- **Officers:** permanent CFO hire and provenance; any second C-suite exit within the
  transformation window.
- **Price alert (list only):** KOP below **$25** → re-run both reopen conditions.
- **Next catalysts:** Q3-2026 10-Q ~early Nov 2026 · Portland Harbor allocation
  ~end-2026 · FY2026 results + initial FY2027 guidance ~late Feb 2027 (the next
  [E3-48] data point) · FY2026 10-K ~Feb 2027 · DEF 14A ~Mar 2027.

**The taxable never-switch test, answered for the operator's mandate [E2-46, E3-64]:**
the earmarked account wants a dividend payer that compounds, taxed once at the end.
**KOP is structurally not that name at any price.** The filed dividend is 0.77% and
$6.8M/yr against a company that returned $44.6M in 2025 mostly as buybacks; the payout
is safely covered by even bottom-boundary OE (12-23%) precisely because it is
negligible; dividend growth is +$0.04/qtr/yr on a base that keeps it immaterial for a
decade; and the equity's return path runs through a leveraged transformation with a
2030 refinancing gate — a sell-discipline holding, not a hold-forever compounder. The
brief's bias warning is confirmed rather than resisted: the wished-for profile is not
in this filing.

- **VERDICT: [x] IN** — what would prove this run wrong is written, dated and
  document-named on both sides (structural evidence + price for reopen; guidance,
  leverage, allocation, restructuring-cash and segment lines for the class thesis).

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (Q2 OUT); Q3-Q5 written
      for the record only, Q4/Q5 math headed COMPUTATION — NOT A CLEARANCE per
      operator rule 3
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] Market cap verified against the sweep as tasked ($880.5M vs ~$879M, 0.2% gap;
      filed cover share count × dated aggregator quote, flagged); the sweep's 6.0%
      statute yield reproduced and its basis identified; the brief's ~1.4% dividend
      corrected against the filed $0.36/yr rate (0.77% at the verified price)
- [x] Step 0: filings read with accession numbers; FY2025 OCF cross-checked three ways
      ($122.5M statement = MD&A = XBRL); H1-2026 OCF cross-checked twice
- [x] Owner earnings on multi-year means; both windows shown with the spread; the TTM
      spike and management guidance refused as bases IN WRITING [E4-41, E3-48]; (c)
      disclosed as a judgment with the corpus default and both cross-checks [E3-44,
      E2-41, E5-20]; SBC subtracted in full; LIFO carve-out noted
- [x] Competitor row: the one principal public peer (Stella-Jones) filled from audited
      statements, route recorded (stella-jones.com IR, unobstructed); private-peer gaps
      named with the row limit [E3-61]; no moat class claimed that needs the missing
      rows
- [x] Debt footnote terms read and transcribed [E3-52]; [E2-54] coverage computed at
      three capex levels (1.35-1.98×); [E2-60] restricted-earnings check run and fired
- [x] Environmental footnote read; deaths quantified from filed figures with
      likelihood vocabulary [E3-24, E4-40]
- [x] Sovereign for the earnings currency (USD) from the issuing-authority series
      (FRED DGS30 via fredgraph.csv direct), dated 2026-08-27
- [x] Value stated as round-number ranges; floor verdict stated plainly; one bar
      (screamer, for the record); windage count: one, justified in writing
- [x] Prices dated; aggregators used for live quotes/FX only and flagged
- [x] Q6 written regardless; alerts LISTED ONLY; taxable never-switch test answered;
      no shared file edited
- [x] The market-beating claim not made anywhere; judgments carry ledger ids or are
      labelled judgments/estimates
- [ ] Run committed to git — pending

## REGISTER
- Verdict: **[x] OUT (about the business, at Q2 — for entry).** No position held.
  Q3 for the record: no honesty disqualifier found; leverage makes Q3 a binary gate,
  and the guidance-miss ledger, institutionalized adjusted-EBITDA promotion, yardstick
  switch and payout-ahead-of-deleveraging converge against it. Q4 for the record:
  survives the current regime; liquidity leg and 2030-wall leg fail [E5-11]; coverage
  met, not comfortably [E2-54]. Q5 computation: floor fails at the bottom boundary
  (3.4-6.2% vs 10%); the current price capitalizes management's guidance, not the
  filed record.
- One line: **the #1 North American crosstie supplier whose own 10-K says the most
  significant competitive factor is selling price, earning ~7-11% on capital against
  its one principal competitor's ~17% ROE, now amputating its founding coal-tar
  business at a $233-252M cost while carrying $906M of secured bank debt that all
  matures in 2030 — priced at 2.3× post-impairment book on the strength of a
  transformation roadmap, guided by a team whose last annual forecast missed by
  13-18%; the dividend the sweep saw is 0.77% at the verified price and the
  compounding is a promise, not a filing.**
- **Work orders (UNRESEARCHED, none blocking):** (1) SJ 2021-2022 equity for a full
  5-yr ROE row — SJ prior annual reports, stella-jones.com IR, ordinary retrieval;
  (2) Rain Carbon scale — private, likely UNKNOWABLE beyond trade press; (3) FY2026
  10-K (~Feb 2027) — post-Stickney segment shape, IL AGO settlement, Portland Harbor
  allocation, the next guidance ledger row; (4) 2027 DEF 14A — permanent CFO, comp
  metric conduct. Q2 is decided on the subject's own filed concessions plus the
  principal-peer row; none of these reopens it.
- **The single biggest concern:** the shape of the balance sheet against the shape of
  the liabilities — every dollar of debt is secured bank paper due in one year (2030),
  the environmental legacy is reserved at $10M against a filing that concedes
  contamination "at most" sites and a $1.7B site allocation landing within months, the
  indemnity that has carried that legacy since 1988 closed to new claims in 2019, and
  $52-62M of shutdown cleanup cash is accrued but unpaid — while the company spends
  its record free-cash half-year buying back stock above this run's conservative value
  range at the covenant basket's limit. Nothing there is dishonest; all of it is
  disclosed; and all of it is what [E2-60] means by distributing restricted earnings.

*This file is a judgment by the AI running the framework; underlying facts are the
FY2025 10-K (acc. 0001315257-26-000012), the Q2-2026 10-Q (acc. 0001315257-26-000048),
the 2026 DEF 14A (acc. 0001315257-26-000026), the four 8-Ks cited in Step 0, XBRL
companyfacts (CIK 0001315257), Stella-Jones's audited FY2025 statements and Q2-2026
fact sheet (stella-jones.com IR), FRED DGS30, and flagged aggregator quotes for price
and FX. Where a number is a judgment or estimate — the (c) band, the bottom-boundary
band, the return-on-capital series, the covenant-breach arithmetic, the reopen band —
it is labelled as one.*
