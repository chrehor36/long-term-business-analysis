# Company Run — PepsiCo, Inc. (PEP) — 2026-09-03
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
- rate **5.27%** · date **2026-09-02** · source **US Treasury daily par yield curve (issuing
  authority), via `tools/sources.py`**. PEP's earnings currency is predominantly USD (56% of
  FY2025 net revenue is US; reporting currency USD). No ADR ratio; single primary listing.
- FX: 44% of net revenue is non-US (Mexico, Russia, Canada, China, UK, Brazil, South Africa
  collectively 25%). Earnings are translated into USD and the dividend is paid in USD; the
  USD sovereign is used, with the FX exposure carried at Q4, not in the rate.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document: **10-K FY2025, period 2025-12-27, filed 2026-02-03, accession
  0000077476-26-000007**; also 10-Q Q2-2026 (period 2026-06-13, filed 2026-07-09, accession
  0000077476-26-000035) and DEF 14A filed 2026-03-27 (accession 0001308179-26-000169).
- figure cross-checked against the filed statement: **FY2025 operating cash flow $12,087M,
  capex $4,415M, D&A $3,451M, SBC $288M — the XBRL pre-fill (`tools/run.py`) matches the
  filed Consolidated Statement of Cash Flows line for line.**

**STAGE 0 — screen row and cover count, reproduced by hand:**
- Screen row REPRODUCED to the decimal (`Screens/regen_queue.py`, 2026-09-03): cap
  **$191,958M**, OE bottom **$6,741M**, top **$9,149M**, spread **35.7%** ((9,149−6,741)/6,741),
  yield bottom **3.51%**, vs sovereign **−1.76 pts**, growth required **6.49%** (to the ~10%
  [E4-28] floor), level_shift **"no step"**, best-year dependence **0.026**.
- Shares **1,364,891,558**, hand-read off the 10-Q cover dated 2026-06-13 (single class,
  undimensioned; `cover_shares.py` verified). `run.py`'s 1,373.0M is a diluted weighted
  average — an EPS denominator, not a count — and is replaced.
- Price **$140.52** (2026-09-02, aggregator — live quote only, flagged). Cap at the hand
  count: **$191.8bn**. The screen's $191,958M used the same count at $140.64; immaterial gap,
  both stated.
- Dividend: **regular quarterly only — no special dividend in the filings examined.**
  Declared per share $4.9450 (2023) → $5.3300 (2024) → $5.6225 (2025); on 2026-02-03 a 4%
  increase to $5.92 annualized was announced. The 10-K claims only *"We have paid consecutive
  quarterly cash dividends since 1965"* — the increase-streak claim and its arithmetic are
  verified in the Stage 0(b) block below from the proxy and the DPS series.

### STAGE 0(b) — THE DIVIDEND STREAK, VERIFIED, AND THE DECOMPOSITION
*Series and accessions: `_research 2026-09-03 PEP/PEP restructuring streak + dividend
series.md`. DPS declared, filed year by year: 2.5325 (2014) · 2.7625 · 2.96 · 3.1675 ·
3.5875 · 3.7925 · 4.0225 · 4.2475 · 4.5250 · 4.9450 · 5.3300 · 5.6225 (2025).*
- **The claim, verbatim (2026 DEF 14A):** *"Announced our 54th consecutive annualized
  dividend per share increase, effective with the expected June 2026 dividend payment."*
- **Arithmetic verified as far as fetched: the declared series rises monotonically every
  year 2014→2025, all regular quarterly, zero hits for "special dividend" across six 10-Ks
  and the proxy.** Pre-2014 years rest on the proxy claim, stated as such.
- **THE DECOMPOSITION (the RPM/ITW/SHW test) — and PEP FAILS it where RPM passed.**
  (1+div growth) = (1+EPS growth) × (1+payout-ratio change); both windows reconcile exactly:
  | Window | dividend growth | from EPS (earnings + retirement) | from payout expansion |
  |---|---|---|---|
  | FY2020→25 | **+39.8%** (6.9%/yr) | +17.2% (NI +15.7%, shares −1.4%) | **+19.3%** (78.6% → 93.7% of EPS) |
  | FY2015→25 | **+103.5%** (7.4%/yr) | +63.5% (NI +51.1%, shares −7.5%) | **+24.5%** (75.3% → 93.7%) |
  Share retirement is negligible (~0.3%/yr recently). **Roughly HALF of the last five
  years' dividend growth was bought by payout-ratio expansion, not earned** — and against
  owner earnings the expansion is starker: DPS was ~59% of capex-end OE per share in
  FY2016 ($2.96 vs $5.05) and is ~104% in FY2025 ($5.6225 vs $5.38). **The streak is real;
  its funding has shifted from earnings to ratio to, at the margin, the balance sheet
  ([E2-60] at Q4: total debt $33,284M (FY2015) → $44,150M (FY2020) → $49,182M (FY2025)
  while the payout ratio rose 18 points).**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **Two different businesses under
  one cover. (1) Snacks: buy potatoes, corn and oil; fry, season and bag them under brands
  built by decades of advertising (Lay's, Doritos, Cheetos); drive them to every store in
  the company's own trucks and stock the shelf with the company's own people. The bag costs
  cents to fill and sells for dollars; the margin lives in the brand and in owning the last
  hundred feet to the shelf. FY2025: PFNA $27.5bn revenue, $6.2bn GAAP segment profit
  (22.4%), plus LatAm Foods at 19.1% — the snack system worldwide is most of the company's
  profit. (2) Beverages: sell concentrate to bottlers where possible, but in North America
  PEP owns most of its own bottling — a capital-heavy, low-margin manufacturing and haulage
  business bolted to a brand business. PBNA: $28.2bn revenue, core margin ~11.7% against
  KO's company-level ~30%+. The two segments have nearly identical revenue and a 2:1
  difference in profit. Money is made by brand price premium × physical case volume, less
  commodity input, less the world's largest DSD payroll.**
- The scarce input this business controls: **shelf position and the DSD network that holds
  it (306,000 employees; the trucks and merchandisers are the moat's physical layer), plus
  the trademarks. Frito-Lay's DSD in salty snacks has no same-scale rival; in beverages the
  same asset exists but faces KO's equally large franchise system.**
- Will the fundamentals look broadly the same in ten years? **Yes for salty snacks and
  broadly yes for beverages — people will buy branded snacks and soft drinks in 2036; the
  live questions (GLP-1 drugs, health regulation, private label) are Q2/Q4 magnitude
  questions, not comprehension questions. The filing is long but the business is simple and
  stable in character [E3-31].**
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**PepsiCo is two franchise claims sharing one filing, judged separately before blending
[E5-37]: (1) Frito-Lay/PFNA — the salty-snack position with its own DSD system; (2) the
beverage business — a permanent #2 to KO. The international food/franchise-beverage
segments are weighed in the blend.**

- Needed or desired [x] · no close substitute — **split verdict, see below** · not
  price-regulated [x] (sugar/snack taxes cap pricing in spots [E3-03](3) but do not set it)
- Must the moat be continuously rebuilt? **The trademark moat is defended, not rebuilt
  [E4-04] — but the defence budget was CUT in FY2025: advertising $3.9bn → $3.4bn, and
  "lower advertising and marketing expenses" is cited as a profit driver in three segment
  discussions of the FY2025 MD&A. [E5-23] — the maintenance obsession lapsed in the year
  volume was negative.** Success does not depend on a great manager [E4-23]: no key-person
  dependence; the moat defect recorded here is category, not personal.
- Primary moat metric, filing-sourced, and its trend: **return on unleveraged net tangible
  operating assets 42.0% (FY2024) → 32.9% (FY2025) GAAP; 47.9% → 42.7% on core operating
  profit. Falling either way. (Subject NTOA: FY2025 $34,958M = assets 107,399 − cash 9,159
  − STI 371 − goodwill 18,916 − indefinite intangibles 13,847 − amortizable 1,219 − ROU
  3,745 − non-debt non-lease current liabilities 25,184; FY2024 $30,671M same construction.)**

### THE [E2-44] TABLE — organic volume vs effective net pricing (the whole question)
*PEP publishes the decomposition itself, every year. FY2025 (10-K) and H1-2026 (10-Q),
analyst-read; the ten-year series is in
`_research 2026-09-03 PEP/PEP pricing vs volume series FY2016-FY2025.md`.*

| Period | PFNA/FLNA vol | PFNA pricing | PBNA vol | PBNA pricing | Total vol | Total pricing |
|---|---|---|---|---|---|---|
| FY2025 | (2) | 1 | (3.5) | 5 | (2) | 4 |
| Q2-2026 (12wk) | — | **(2)** | (2) | 3 | 1 | 2 |
| H1-2026 (24wk) | 1 | **(1)** | (3) | 4 | 1 | 2 |

MD&A verbatim, Q2-2026: *"Net revenue decreased 2%, primarily driven by unfavorable net
pricing. Unit volume was even with the prior year"* (PFNA); *"Unit volume declined 4%,
primarily driven by a 4% decline in noncarbonated beverage (NCB) volume and a 3% decline
in CSD volume"* (PBNA). FY2025 MD&A: PFNA *"Unit volume declined 2%, driven by a 3%
decrease in savory snacks volume"*; PBNA *"Unit volume declined 3%, driven by a 6% decline
in non-carbonated beverage volume."*

**The answer to the question the table was built for: the volume did NOT come back at the
higher price — North American volume is negative in FY2025 and PBNA volume is still
negative through H1-2026 — and in snacks the price is now being GIVEN BACK: PFNA effective
net pricing is negative in both the 12- and 24-week 2026 periods, while PFNA core
operating profit fell 8% (12wk) / 6% (24wk). [E4-37] read in reverse: three years from
yawn-pricing to negative pricing.**

### THE COMPETITOR ROW — required [E3-28]
**Beverages (full row: `_research 2026-09-03 PEP/competitor row - beverages KO KDP.md`):**

| FY2025 | **PEP (whole co)** | **KO** | **KDP** |
|---|---|---|---|
| accession | 0000077476-26-000007 | 0001628280-26-010047 | 0001418135-26-000016 |
| Return on NTOA | 32.9% (core 42.7%) | **31.5%** (5-yr 31.0–35.7%) | n.m. (NTOA $4.6bn vs $44bn of goodwill+intangibles) |
| ROIC incl goodwill | 16.7% | **19.2%** | 7.4% |
| GAAP op margin | 12.2% | **28.7%** | 21.5% |
| FY2025 organic volume | **(2)** | **+1** (concentrate; unit cases even) | +1.0% LRB |
| FY2025 pricing | +4 | +4 price/mix | +3.8 |
| FY2024 volume / pricing | (0.5)/(1)* | **+2 / +11** | +2.7 / +1.2 |
| FY2023 volume / pricing | * | **+2 / +10** | (2.1) / +7.0 |

*\*PEP FY2016–FY2024 series from the research file; PBNA volume negative in every year of
the comparison window.*

- **The sharpest single cell: H1-2026, same country, same quarter — KO North America
  price/mix +5 on volume −1; PFNA pricing −2 on volume even. Coca-Cola holds its price;
  Frito-Lay is buying its volume back.** KO's FY2025 10-K states its pricing *"included
  both new and carryover pricing increases from the prior year"* in ALL segments.
- KDP's U.S. Refreshment Beverages grew volume/mix +2.7% (FY2024) and +2.8% organic
  (FY2025, ex-GHOST) with positive pricing — the #3 is taking share in CSDs while PBNA's
  CSD volume declines.
- **The Rockstar record [E2-45 answered by events]: PEP paid $3.85bn for Rockstar (2020),
  impaired $1.9bn pre-tax (FY2025), and transferred the US/Canada brand ($0.5bn) to
  Celsius (2025-08-28) — then became the DISTRIBUTOR of Celsius, Alani Nu and the
  ex-Rockstar brand. The attacker won the energy category inside PEP's own trucks; the
  franchise layer failed and the logistics layer survived. A franchise owns the brand;
  a hauler hauls it.**
- Snacks row (MDLZ, GIS, UTZ): `_research 2026-09-03 PEP/competitor row - snacks MDLZ GIS
  UTZ.md`.
- Peers named: **5 filed (KO, KDP, MDLZ, GIS, UTZ)** of an industry whose named-in-Item-1
  competitor set is ~13 (Campbell's, Conagra, Hormel, Kraft Heinz, Link, Mars†, Monster,
  Nestlé†, Primo, Red Bull† also named; †private/foreign — Mars and Red Bull do not file;
  Nestlé files IFRS abroad). The five filed peers cover both halves; the moat class is
  judged on them, with the private attackers evidenced from the subject's own filing.

### The attacker record [E2-45] and the physical series [E4-55]
- **GLP-1, in the filer's own words (FY2025 10-K, Item 1A):** consumer preferences evolve
  due to *"diet (whether due to changes in consumer behavior and eating habits, increasing
  use of weight-loss drugs, such as GLP-1 medications, or other factors)"*. The filed
  volume series (savory snacks −3% FY2025) is consistent with pressure but does not
  isolate the cause; recorded as a named exposure, not a quantified one.
- **The physical series exists and it convicts the pricing, not the position: PEP measures
  convenient-food volume in pounds/kilograms and beverages in 8-oz cases [E4-55], and the
  filed unit series is negative in North America for snacks and beverages alike in FY2025
  while dollar revenue rose — the Precision Steel shape: dollars held up by price while
  units fall.**
- Private label: PEP's own Item 1A — retailers are *"focusing on introducing and
  developing private-label brands"*; the snacks-row file carries the peer statements.

### THE TEN-YEAR SERIES, ASSEMBLED (accessions per year in the research file)

| FY | FLNA/PFNA vol | FLNA pricing | PBNA/NAB vol | PBNA pricing | Consol vol | Consol pricing |
|---|---|---|---|---|---|---|
| 2016 | 2 | 2 | 1 | 1 | 2 | 2 |
| 2017 | 1 | 2.5 | (2.5) | 1 | — | 3 |
| 2018 | 1 | 2 | (1) | 2 | 1 | 3 |
| 2019 | 2 | 3 | (1) | 4 | 0.5 | 4 |
| 2020 | 3 | 3 | (1) | 3 | 2 | 2 |
| 2021 | 2 | 5 | 5 | 5 | 4 | 5 |
| 2022 | — | **17** | 1 | **10** | — | **14** |
| 2023 | (1) | **10** | (5) | **12** | (3) | **13** |
| 2024 | (2.5) | 2 | (3.5) | 4 | (2) | 4 |
| 2025 | (2) | 1 | (3.5) | 5 | (2) | 4 |
| H1-26 | 1 | **(1)** | (3) | 4 | 1 | 2 |

**Read against [E2-44], the two claims separately [E5-37]:**

**Claim 1 — Frito-Lay (FLNA/PFNA), the strongest single claim.** The 2022–23 event proved
once-in-a-generation pricing power: **+17 then +10 effective net pricing — cumulative
~+33% over 2022–25 — against a CPI rise of roughly +16% over the same window.** But the
filed record of what that pricing BOUGHT:
- **Volume never came back:** unit volume −1, −1, −2.5, −2 (2022→2025), cumulative
  ~−6.4%; H1-2026 +1 only after price was cut.
- **The price is now being given back:** pricing +2 (2024) → +1 (2025) → **negative**
  (H1-2026), while UTZ's 10-K files the mirror image: *"beginning in 2024, certain
  competitors began to take certain discrete pricing actions in specific channels,
  resulting in an environment that has become far more promotional. Such promotions have
  impacted our sales and, in response, we have increased our promotional activities."*
  The category itself shrank (Circana: US salty retail sales −0.5% in 2025) while UTZ's
  retail sales rose 2.9% — **the #3 is taking share from the leader inside a shrinking
  category.**
- **Nothing stuck to the ribs [E3-62]:** FLNA operating margin 30.8% (2019, pre-surge) →
  29.4 → 28.7 → 26.3 → 27.1 → 25.5% (2024); PFNA 22.4% GAAP / 23.8% core (2025, Quaker
  perimeter added). Five-plus points of margin LOST through a +33% pricing wave.
  Incremental economics 2019→2024: revenue +$7,677M, operating profit +$1,058M — a 13.8%
  incremental margin, BELOW the segment average. The "pricing" was cost pass-through plus
  mix, not owner-accruing pricing power.
- **The dominance economics [E2-53] are intact at the level:** FLNA still earns 25.5%
  GAAP segment margins on ~$25bn revenue, and UTZ — the #3 platform — earns **4.6% on
  NTOA, 0.9% ROIC incl. goodwill, 1.4% operating margin** (snacks-row file): position,
  not execution, still sets these economics, and private-label penetration in salty is
  low by UTZ's own filed statement. **Existence: YES, still. Direction [E4-32]: DOWN on
  volume, margin, price and profit simultaneously — and direction outranks existence.**

**Claim 2 — Beverages (PBNA + IB Franchise).** PBNA volume is **negative in eight of the
ten filed years** (positives: 2021's reopening +6, 2022 "slightly"); NAB/PBNA segment
operating profit **$2,947M (2016, restated) → $1,089M GAAP / $3,285M core (2025)** — a
decade of nothing on $28bn of revenue; margin 13.8% → 11.7% core. Against the row: KO
grew concentrate volume **+2/+2/+1 (2023/24/25)** at price/mix **+10/+11/+4** and earns
28.7% operating margins and 31.5% on NTOA; KDP's US Refreshment grew organic volume with
positive pricing both years. **Gatorade declined by the filer's own sentences in 2023,
2024 (water, tea, juice likewise); CSDs declined in 9 of 10 years; the energy bet
(Rockstar, $3.85bn) was impaired and surrendered to Celsius, whose brands PBNA now hauls
as a distributor.** [E3-03](2) fails: for every PBNA category there is a close substitute
winning on the filed series. IB Franchise (international concentrate, 35.4% margin,
volume growing) is a real franchise but is $5.0bn of a $93.9bn filer. **Not a franchise.**

- **Untapped pricing power [E3-33]: NO — the inverse.** The pricing power was TAPPED in
  2022–23 and the give-back is now on the filed record; [E5-28]'s near-monopoly claim
  cannot be made for beverages at all, and for salty snacks the monopoly position priced
  itself into a promotional war.
- **The row's limit [E3-61]:** the row shows position, not conduct — KO's discipline and
  Frito-Lay's promotional turn are conduct, read from the filings, not predicted.
- Peers: **6 filed peers used (KO, KDP, MDLZ, GIS, UTZ + the subject)** across both
  halves; Mars, Red Bull, Nestlé and the private/foreign rest are named and unfiled — the
  moat class is NOT held provisional for them, because the failing series is the
  subject's own filed data, not an inference from missing peers.
- Class: **[x] NARROW and narrowing (FLNA dominance intact at the level; PBNA none; the
  blend priced as one security fails the direction test)** · Direction: **DOWN — the
  moat did not widen this year or last [E4-32]; the defence budget was cut while the
  attacker's filing records the leader promoting.**

- **VERDICT: [x] OUT.** *The evidence is here and the business fails the franchise test
  as a whole filer: the beverage half was never a franchise on its own ten-year series;
  the snack half's 2022–23 pricing is now measured — volume −6%, margin −5 points,
  pricing negative, share leaking to the #3 — the [E2-44] table answers its own question:
  the price increase was partly borrowed, and it is being repaid through promotion.
  This is the KR/DG shape, at higher quality. Permanent, about the business at this
  structure; a Frito-Lay separated from the beverage system would be re-run on its own
  filing.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [ ] **Daily execution** — branded staples with dominant category positions are the
  franchise class [E3-43], not promises-only daily execution **[E3-38]**
- [ ] **Control** — public minority position, exit available **[E1-16]**
- [ ] **Leverage** — $49.2bn total debt against $12.1bn OCF and A-grade ratings is
  material but not the small-asset-errors-destroy-equity class **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Findings recorded; nothing here gates, and
per the guardrail nothing here promotes.

**Honesty — binary, permanent, filings-based [E5-16].** No integrity disqualifier found in
the filings read: no restatement, no fraud or accounting enforcement matter disclosed, audit
opinions unqualified (KPMG). The Quaker recall (2023-24) was disclosed with charges
quantified line by line — a product failure handled in the open, not a conduct matter.

**STEP 2 — THE FLAGS.**
- [ ] weak accounting — **acquits mostly**: SBC expensed, pension expected return 7.1–7.3%
  (aggressive side of normal, disclosed with sensitivity); the accrual detail is legible
- [ ] unintelligible footnotes — no; items-affecting-comparability reconciled line by line
- [x] **trumpeted earnings projections / growth targets — FIRES.** A standing guidance
  culture: annual organic-revenue and core-EPS guidance, proxy targets built on it
  (*"Performance targets are set taking external guidance into consideration"*), [E5-30]'s
  ratchet on the record: FY2025 targets (organic +3.0%, core CC EPS +7.0%) missed at 1.7%
  and 0.0%
- [ ] serial share issuance — no; count 1,452M (FY2016) → 1,365M cover count, slow shrink
- [ ] EBITDA promotion **[E4-29] — does NOT fire: zero occurrences of "EBITDA" in the
  FY2025 10-K AND the 2026 proxy.** The non-GAAP unit is "core" operating profit/EPS —
  D&A stays IN it; the vice here is the *exclusion list*, handled below
- [ ] filed-figure tells **[E4-30] — ACQUIT: cash taxes paid rose 16.3% (FY2016) → 25.6%
  (FY2024) → 30.1% (FY2025) of pretax; reported growth is lumpy, not smoothed**
- [x] **the restructuring flag [E3-53, E5-33, E4-52] — FIRES, and it is the big one.** The
  "2019 Productivity Plan" was *extended in 2024 through 2030*: a program of ~$6.15bn of
  expected pre-tax charges, $3.61bn taken plan-to-date, ~$900M more guided for 2026 —
  charges 445/727/983 in FY2023/24/25, every dollar excluded from "core" results, on top
  of the 2014 Productivity Plan before it (streak count from the research file: charges
  taken and excluded every year since 2014). *"To tell owners year after year, 'Don't
  count this' … is misleading"* [E5-33]. Core EPS $8.14 vs GAAP $6.00 in FY2025 — a 36%
  premium of story over statement, the widest of the modern years
- [x] **[E2-49] metric-switching — fires SMALL, dated:** beginning FY2025, *"on a
  prospective basis"*, the organic-revenue and constant-currency calculations were changed
  to apply constant-currency treatment to *"subsidiaries operating in highly inflationary
  economies"* — a definitional change to the compensation-linked headline metric, adopted
  in a year the metric missed its target even so. Disclosed plainly; not a withdrawal of a
  deteriorating series (the volume/pricing decomposition keeps publishing). Noted, not a
  lollapalooza.

**STEP 3 — THE PRIMARY TEST [E2-01]** — run on unleveraged net tangible operating assets
[E2-43], since book equity ($20.4bn, after $41.8bn of treasury stock and −$15.0bn AOCI) is
meaningless as a denominator here:
- **Return on NTOA 42.0% (FY2024) → 32.9% (FY2025) GAAP; core 47.9% → 42.7%. The LEVEL is
  franchise-class; the direction is down. The goodwill wedge reported separately: $18.9bn
  goodwill + $15.1bn other intangibles carry the Quaker/SodaStream/Rockstar/poppi/Siete
  acquisition history, and ROIC including goodwill is 16.7% — half the tangible return.
  What the operators earn on the assets [E2-73] is excellent; what the ALLOCATORS have
  earned on the prices paid is ordinary.**
- The allocation record, priced by its own filings: SodaStream $3.2bn (2018) → $1.16bn
  impaired 2023, fair value still only *"narrowly exceeds"* carrying value; Rockstar
  $3.85bn (2020) → $1.9bn impaired and the brand handed to Celsius (2025); poppi $2.15bn
  and Siete $1.2bn (2025) — bought at ~100% goodwill+intangibles — bolted on in the same
  year the flagship advertising budget was cut $0.5bn. **[E3-40] loss of focus is the
  live worry: capital flows to bought growth while the base business's defence spending
  falls and its price position is given back.**

**The half-owner test [E2-26]:** the disclosure itself is good — every excluded item
quantified at every line, the volume/pricing decomposition published for decades, segment
detail deep. It fails only where "core" asks the owner to un-count a 12th consecutive year
of restructuring. Half-pass, stated as such.

**The institutional imperative [E2-30]:**
- [x] resists change in direction — PBNA has owned its bottling since 2010 while KO
  refranchised; fifteen years of an 11.7%-vs-28.7% margin gap and no revisitation in the
  filing
- [x] acquisitions materialise to soak up funds — $3.4bn in FY2025 alone (poppi, Siete),
  plus Sabra consolidation, in the year operating profit fell 11%
- [ ] staff studies — not evidenceable from filings
- [x] peer behaviour imitated — the energy-drink M&A wave (Rockstar 2020, industry-wide),
  now the functional-soda wave (poppi 2025)

**Capital allocation — the buyback conditions [E5-08]:** repurchases run at a flat $1.0bn
a year (FY2023/24/25 identical to the dollar), a dollar-budget program, ~0.5% of the cap,
dwarfed by $7.6bn of dividends — price-indifferent by construction, too small to flag
either way. The real allocation is the dividend ratchet plus M&A, judged at Q4 under
[E2-60]. **Pay-versus-performance, the 3x-replicated pattern, tested and it does NOT
replicate: FY2025 targets were set ABOVE the prior year's outturn, were missed (organic
1.7% vs 3.0%; core CC EPS 0.0% vs 7.0%; only FCF beat, $10.0bn vs $9.9bn), and payouts
came in BELOW target — CEO $3,136,000 against a $3,608,333 target (86.9%), new CFO 79%,
2023 PSUs 88.4%, 2023 LTC 50% on relative TSR. Targets not reset mid-year, by stated
policy and observed outcome.** The pay flag here is structural, not conduct: every
incentive metric is a non-GAAP measure that excludes the perpetual restructuring.

**THE GUARDRAIL.**
- [x] Nothing above promotes the name; the strong tangible returns are the business, not
  the management [E2-37].
- [x] No key-person dependence to record at Q2.
- [x] No manager-as-plan case is being made.

- **VERDICT (recorded, not a gate — Q3 is an overlay here): IN — no integrity
  disqualifier found. NOT a finding that the managers are honest [E5-17]. The
  capital-allocation findings (perpetual restructuring exclusion, imperative behaviours,
  bought-growth-while-cutting-advertising) stand recorded and bind position size, never
  the rate.**

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
*Construction: OCF − SBC − (c), per the framework CONVENTION; working capital nets inside
OCF ([E2-23] carve-out); restructuring CASH payments flow through OCF and are therefore
counted, as [E5-33] requires. All figures $M, from the filed cash-flow statements
(FY2023-25 cross-checked line by line; earlier years from 10-K XBRL, undimensioned).*

| Window | (c) = total capex | (c) = D&A |
|---|---|---|
| 3-yr (FY2023–25) | **7,252** | 9,149 |
| 5-yr (FY2021–25) | **6,741** | 8,751 |
| 7-yr (FY2019–25) | **6,428** | 8,363 |
| 10-yr (FY2016–25) | **6,498** | 8,068 |

- **Spread, conservative end (7-yr capex) to generous end (3-yr D&A): $6,428M → $9,149M,
  width 42.3%.**
- Owner earnings by year (capex end): 7,339 · 6,769 · 5,877 · 5,180 · 6,109 · 6,690 ·
  5,261 · 7,544 · 6,827 · 7,384 (FY2016→FY2025). **Ten years, +0.6% total. Flat.**
- *Is the range too wide to conclude?* **No — because the ENTIRE range prices below the
  sovereign (top of range 4.77% yield vs 5.27%), the band cannot change the price verdict
  (the ORLY precedent), so [E4-25] does not close the file on width.*
- Distorted years named [E5-11]: FY2020 (pandemic), FY2022 (working-capital build in the
  inflation spike), FY2023 (OCF peak on the pricing surge — the highest OCF in history sits
  in every window). **[E4-41]: the 2022–23 double-digit-pricing surge is IN every window,
  and the mean IS priced off it. H1-2026's negative snack pricing says part of that
  pricing was borrowed; the judged figure is therefore set at the LOW end of the windows,
  not the middle.**
- **Maintenance capex — the (c) judgment, disclosed:** capex ran 1.67x D&A over five years
  ($25.1bn vs $15.0bn). The filing never says D&A understates renewal — but management's
  own free-cash-flow note says the opposite of the D&A default: *"Since net capital
  spending is essential to our product innovation initiatives and maintaining our
  operational capabilities, we believe that it is a recurring and necessary use of cash."*
  With North American volume FLAT-TO-DOWN across the decade, the capital that was
  nominally growth capex has not produced unit growth at home; internationally it has.
  **(c) is judged at total capex net of PP&E sale proceeds for the system as it stands —
  the capex end of the band — with the D&A end displayed but judged INVALID here for the
  [E4-47] reason (a high-inflation half-decade means replacement in current dollars runs
  well past historical-cost D&A) as well as the filer's own sentence.**
- **Judged owner earnings: ~$6,800M** (low end of the 3-yr/5-yr capex-end range, [E4-41]
  normalization down for the pricing surge; sale-leaseback gains of $291M (FY2025, up from
  $52M in FY2023) noted as a growing non-operating flatterer inside operating profit,
  though not inside OCF).
- Stock compensation subtracted in full [E5-06]: yes, $288M (FY2025) and each year's
  figure in its year. SBC here is ~2% of OE; reported charge used as the floor [E3-70].
- Look-through [E3-04]: equity-method affiliates ($2.0bn carrying value; Lipton/Starbucks
  JVs, TBG) contribute modest undistributed earnings not added — conservative, immaterial
  at this scale, stated.
- *The capex band does not change any verdict → no UNKNOWABLE trigger.*

### Great, good, or gruesome? **[E4-20]**
- [x] **A GREAT base account taking new deposits at a GRUESOME rate.** The existing system
  earns 32.9–42.7% on tangible operating assets — franchise-class. But the marginal
  decade: ~$10.1bn of capex above D&A plus ~$8bn of acquisitions (SodaStream, Rockstar,
  poppi, Siete, Sabra) produced owner earnings of $7,384M in FY2025 against $7,339M in
  FY2016 — **the incremental return on roughly $18bn of added capital rounds to zero.**
  [E4-20]'s middle case requires the added deposits to EARN the attractive rate; these
  did not. The account pays a high rate on old money and ~0% on new money.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **PASS** — $8.2–9.6bn net income, revenue
  never fell in the decade, demand staple-stable.
- (2) massive liquid assets: **QUALIFIED PASS** — $9.5bn cash+STI, two undrawn $5bn
  revolvers; but **20% of consolidated cash sits in Russia** (filed), and net of $49.2bn
  total debt the balance sheet is a net borrower of ~$39.7bn ≈ 5.8x judged OE.
- (3) no significant near-term cash requirements: **PASS ONLY WITH [E5-39] FLAGGED** —
  2026 calls: $4.0bn current LTD + $2.6bn CP (grown to **$6.1bn CP by 2026-06-13**) +
  $965M final TCJ transition-tax payment + a $7.9bn announced dividend intention. Covered
  by $12bn OCF — but the filing states the liquidity MODEL is *"maintaining Tier 1
  commercial paper access"*: the kindness of strangers is the written policy, and H1-2026
  paid $3.9bn of dividends against $2.4bn of seasonal OCF by drawing CP. Coverage test
  [E2-54]: interest $1,840M against OCF-less-capex $7,672M = 4.2x — comfortably met, wallet
  stays open.
- Leverage, named and quantified [E4-16, E3-29]: total debt $49,182M (ST $6,861 + LT
  $42,321), net debt ~$39,652M, 5.8x judged OE, all covenant-light investment-grade paper,
  maturities laddered to 2060. Operating leases $3.8bn PV. Not a solvency question at
  current ratings; the cost is optionality.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- **The mechanism — the dividend ratchet meets the volume leak.** Two slow forces
  compound: (i) North American physical volume declines 2–4%/yr (savory −3%, NCB −6%,
  CSD slightly down in FY2025) under health/GLP-1/private-label pressure while price can
  no longer be raised against it (PFNA pricing negative H1-2026) — operating leverage on
  a 306,000-employee DSD system runs in reverse; (ii) a 54-year dividend-increase
  institution now pays out ~113% of judged owner earnings ($7,718M declared vs ~$6,800M),
  before $1bn of buybacks and $3.4bn of acquisitions. **[E2-60] FIRES on the filed
  arithmetic: distributions + buybacks exceeded capex-end owner earnings in each of
  FY2023 ($7,682 vs $7,544), FY2024 ($8,229 vs $6,827) and FY2025 ($8,638 vs $7,384),
  funded how: total debt +$4.9bn in FY2025 alone (LT issuance $8.2bn vs repayment
  $4.1bn), CP $2.6bn → $6.1bn in six months.** *"A company that consistently distributes
  restricted earnings is destined for oblivion"* — three years running and guided to a
  fourth ($8.9bn announced for 2026).
- Quantified: a decade of −2.5%/yr NA volume with pricing capped at CPI−1 compresses
  PFNA+PBNA core profit (~$9.8bn) by roughly a third; judged OE falls toward $5bn while
  the ratcheted dividend runs $8–9bn; net debt compounds +$3–5bn/yr toward $70–80bn by
  the mid-2030s, at which point the rating, the CP model and the streak break together —
  the balance-sheet expression of a demand problem.
- Likelihood: **the funding gap is present fact (three filed years); the completed death
  (forced dividend break / downgrade spiral) is [x] a real possibility on a ten-year
  horizon, a low-level possibility inside five.**
- **VERDICT (recorded, not a gate — the file's gate is Q2): the business SURVIVES any
  horizon the framework prices — strengths (1) and (3) pass — but Q4's owner-earnings
  finding is the run's spine: flat for ten years, distributed beyond its means, [E2-60]
  firing. Marked IN for survival, with the restricted-earnings flag carried to the price.**

---
⛔ **Q5 does not open. Q2 returned OUT — the file is closed at the second gate.** Q3 and Q4
above are recorded findings, not clearances. Per the queue's output contract the price is
still reported, under the mandatory heading, with no entry language.

---
## COMPUTATION — NOT A CLEARANCE
*(operator rule 3: valuation math produced without Q1–Q4 clearance; carries no entry
language. Sovereign 5.27% bare, no per-name premium [E3-42]. One book: owner earnings
against the bond; no DCF voted.)*

**1. THE YIELD.** Judged owner earnings **$6,800M** (range $6,428M–$9,149M across four
windows and the capex band) ÷ market cap **$191.8bn** (1,364,891,558 shares × $140.52,
2026-09-02) = **3.55%** (range 3.35%–4.77%) against the **5.27%** sovereign. **Below the
bond on every construction, −1.7 points at the judged figure; honest pre-tax expectancy
3.4–4.8% sits far under the ~10% figure-we-quit-on [E4-28].**

**2. WHAT THE PRICE ALREADY ASSUMES.** Perpetual growth needed merely to MATCH the bond:
**+1.7 points**; to reach the [E4-28] floor: **+6.5%** (screen's 6.49% reproduced) —
against a business whose owner earnings compounded **+0.1%/yr for ten years** ($7,339M →
$7,384M), whose GAAP operating profit compounded +1.6%/yr, and whose NA volumes are
falling. [E4-35]: a floor case needing 6.5% forever from a base of zero carries a burden
of proof this filing cannot meet.

**3. THE VALUE, AS A ROUND-NUMBER RANGE [E4-01].**
- **Zero-growth at the bare sovereign: roughly $90–125 per share** ($6,428M–$8,751M ÷
  5.27%, per share on the cover count; the judged $6,800M gives **~$95**). The 3-yr D&A
  end ($9,149M) stretches the top to ~$127 and is judged INVALID for (c) here.
- **At the [E4-28] ~10% floor: roughly $47–65 per share** (judged ~$50).
- **Current price: $140.52 (2026-09-02).** The price sits **above the entire
  sovereign-rate range** — Bar 2's third outcome (above the whole range → no); no margin
  arithmetic is reached, so conservatism is spent nowhere else (windage count: one, the
  [E4-41] normalization inside the judged OE — stated).
- The 42.3% owner-earnings width does not bar the conclusion, because the whole width
  prices below the bond [E4-25]; the band cannot change the answer.

**PASS/FAIL: FAIL. Closed at Q2 (OUT). The price would also have failed Q5 on the floor
and the bond had it reached them.**

## Q6 — NOT OPENED
The file closed at Q2. No position exists; no exit rules are pre-committed. The Q6-class
monitoring item that would reopen a future run is named in the register.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN · Q2 OUT closes the file;
  Q3/Q4 explicitly recorded as findings, not clearances; Q5 not opened; price under
  COMPUTATION — NOT A CLEARANCE)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1's IN
  rests on the filed statements; the pre-2014 dividend years rest on the proxy claim and
  are labelled as such in Stage 0(b), which gates nothing)
- [x] No UNRESEARCHED verdicts issued
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: 10-K FY2025 read (MD&A, cash-flow detail lines, footnotes), accession
  0000077476-26-000007; OCF/capex/D&A/SBC cross-checked XBRL-vs-filed line for line
- [x] Owner earnings on multi-year means; four windows stated; (c) disclosed as a judgment
  (total capex end; D&A end displayed and judged invalid, with the filer's own
  recurring-and-necessary sentence cited)
- [x] Competitor row filled from six filed sets (subject + KO, KDP, MDLZ, GIS, UTZ);
  unfiled competitors (Mars, Red Bull, Nestlé et al.) named; class not held provisional
  because the closing series is the subject's own
- [x] Sovereign 5.27% USD, US Treasury daily par yield curve (issuing authority),
  2026-09-02
- [x] Value stated as round-number ranges at both the sovereign and the floor
- [x] Bar 2 only (price above the whole range); windage count: one ([E4-41] normalization
  in the judged OE)
- [x] Price $140.52 dated 2026-09-02, aggregator, flagged as live-quote-only
- [x] Run committed to git question by question (write-early protocol; survived two
  session kills with zero loss of committed work)

## REGISTER
- Verdict: **[x] OUT (about the business)** — at Q2, the franchise gate.
- One line: **The [E2-44] table PEP publishes about itself answers the question: +33%
  snack pricing over 2022–25 bought −6% volume, −5 points of margin, a promotional war
  the #3 attacker documents, and pricing that went negative in H1-2026 — while the
  beverage half logged its eighth volume decline in ten years and surrendered the energy
  category to a brand it now delivers; the price ($140.52) sits above the whole
  zero-growth range (~$90–125) and needs 6.5% perpetual growth from a base that grew
  0.1%/yr for a decade.**
- Q6-class reopen trigger (for the watchlist, not a position): **two consecutive fiscal
  years of positive PFNA organic volume WITH non-negative effective net pricing** — that
  is what "the volume came back at the higher price" would look like in the filed table —
  or a structural separation of the snack and beverage businesses, which would re-run
  Frito-Lay on its own filing.

## JOB 2 — METHOD AND BRIEF FINDINGS (recorded for the operator)
1. **[BRIEF DEFECT — date]** The brief is dated 2026-09-03 and cites corrections "corrected
   2026-09-02"; CLAUDE.md's one-screen summary still carries v4.0's *"there is no hurdle —
   it ranks"* line at Q5, which v4.1 rewrote to floor-first [E4-28]. The framework document
   governs and the floor was applied, but CLAUDE.md misleads every session that reads only
   the summary. Same line survives in `tools/run.py` output ("There is no hurdle. Rank
   this…") — flagged by the BRK-B run as [BRK-MF 5] and still unfixed.
2. **[BRIEF DEFECT — segment names]** The brief says "use the segment tables" for
   "Frito-Lay North America" — FLNA ceased to exist as a reporting segment in FY2025
   (merged with Quaker/Sabra into PFNA; international re-segmented twice in the window).
   Any tool or reader keying on the FLNA name against the FY2025 10-K finds nothing; the
   series had to be spliced across three segment structures, with the FY2018 pension
   restatement breaking $-comparability of 2016–2017 operating profit.
3. **[BRIEF DEFECT — "~60% category share"]** The brief's Frito-Lay share figure appears
   in no filing read; the filed, citable facts are UTZ's Circana-based numbers ($42bn US
   salty category; UTZ #3 at 4.4%) and PEP's own "we and The Coca-Cola Company represented
   approximately 16% and 20% of the U.S. liquid refreshment beverage category". The ~60%
   is directionally consistent with third-party retail data but entered the run only as
   the brief's claim — it was not needed for the verdict.
4. **[BRIEF DEFECT — attacker metric on KDP]** The brief prescribed return on unleveraged
   net tangible operating assets for the beverage row; KDP's NTOA is negative-to-tiny
   (79.3% of assets are goodwill+intangibles), so the metric returns 3,065% (FY2022) —
   arithmetic artifact, unusable, exactly the [MF] class the WTM run logged for [E5-48].
   ROIC-including-goodwill carried the comparison instead.
5. **[METHOD] The restructuring streak instrument [E4-52] scales:** RPM fired at nine
   years; PEP shows **twelve consecutive years verified with core-exclusion (FY2014–25),
   fourteen with charges (FY2012–25), and the 2012 Plan's inception total implies a start
   at FY2011 or earlier** — three named plans, $5.3bn+ of "one-time" charges, the current
   plan extended twice and guided through 2030. The instrument's output here: "core" EPS
   has excluded a recurring ~$0.15–0.58/share cost every year for over a decade.
6. **[METHOD] The dividend decomposition (RPM/ITW/SHW instrument) produced its clearest
   negative yet:** ~half of five-year dividend growth from payout-ratio expansion,
   retirement ~nil, DPS now ~104% of capex-end owner earnings per share — and it agrees
   with [E2-60] computed independently from the cash-flow statement. Two instruments, one
   finding: the streak is being financed, not earned.
7. **[TOOL] `cover_shares.py` and `regen_queue.py` both clean on PEP** (single class;
   screen row reproduced to the decimal). `run.py`'s weighted-average share basis
   overstated the count by 0.6% vs the cover — immaterial here, caught by the mandated
   hand-read.
8. **[SESSION] Two session-limit kills; zero questions lost** — the write-early protocol
   did exactly what it was written to do. Cost of the kills: three research agents
   re-spawned once.
