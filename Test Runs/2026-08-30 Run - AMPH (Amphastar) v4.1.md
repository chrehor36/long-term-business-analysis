# Company Run — Amphastar Pharmaceuticals, Inc. (NASDAQ: AMPH) — 2026-08-30
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`.

**Position context: NONE HELD. Fresh entry run.**

**Bias declared per operator rule 9, up front as tasked:** ~$2,750 of taxable capital
seeks a dividend payer that compounds. **AMPH pays no dividend and never has.** It does
not fit the operator's stated dividend-compounder wish, so the only honest reason to run
it is the framework's own terms, and the analyst's incentive to clear an interesting name
is the thing to guard against. The iron prescription [E4-51] is applied; disconfirming
evidence hunted hardest [E4-26]. **A "no" verdict is a fully successful run.**

**The tasked Q2 question, carried as the run's spine:** each generic product individually
melts under competition — is there a durable capability moat (complex generics,
interchangeability barriers, own API), or a portfolio of melting ice cubes that the
pipeline must perpetually replace ([E4-04]'s excluded class: basis replaced, not
defended — the MITSY logic)? The answer is at Q2.

Evidence pack, transcriptions and the competitor row:
`Test Runs/_research 2026-08-26/AMPH evidence pack + competitor row (Hikma-TEVA-VTRS, Kabi gap).md`

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · 2026-08-27 · FRED DGS30**, pulled directly from `fredgraph.csv`
  (issuing-authority series) and dated. 95% of FY2025 revenue is US ($681.4M of $719.9M);
  France $35.3M, China $3.2M — USD governs. `tools/run.py AMPH` failed on its FRED fetch
  from this environment (read timeout, same failure as the CCS/ETD/FLO runs); recorded.
  FRED's 1-2 day lag noted, immaterial.
- FX: none. Quote currency = earnings currency = USD.
- Price: **$22.01, NASDAQ close 2026-08-28 (Yahoo chart API — aggregator, live quote
  only, flagged).**
- **Market cap, verified first as tasked:** 42.54M shares (filed cover count, Q2-2026
  10-Q, as of 2026-07-31) × $22.01 = **$936M**, against the sweep's ~$938M: 0.2% gap
  (price-date drift). **Verified.** The sweep's "6.6% statute yield" was not reproduced
  by this run's owner-earnings arithmetic (all windows computed below run 7.5-13.2%);
  the cap half of the sweep line is confirmed, the yield half is superseded by the
  filed-figure computation. Book equity $768.2M at 2026-06-30 → $18.06/share;
  **price/book 1.22×; TTM P/E ~11.9×.**

**The filing was read — not tagged data [E3-27]:**
1. **FY2025 Form 10-K, filed 2026-02-26, accession 0001297184-26-000009** (year ended
   2025-12-31; auditor Ernst & Young, unqualified; ICFR effective) — [x] MD&A
   [x] cash-flow statement incl. detail lines [x] footnotes (revenue by product Note 3;
   segments Note 5; customer/supplier concentration Note 6; intangibles Note 9; debt
   Note 13 in full — the tasked BAQSIMI terms; related-party Note 18; litigation Note 19;
   subsequent events Note 20) [x] Item 1 (products, pipeline, manufacturing, competition)
   [x] Item 1A (China, FDA, HFC/AIM Act, tariffs).
2. **Q2-2026 Form 10-Q, filed 2026-08-06, accession 0001297184-26-000047** — MD&A with
   product price/volume decomposition, BAQSIMI milestone note, warning-letter risk
   factor, pledged-share risk factor, buyback tables.
3. **Q1-2026 Form 10-Q, filed 2026-05-07, accession 0001297184-26-000033** (quarterly series).
4. **DEF 14A, filed 2026-04-13, accession 0001297184-26-000023** (officers, ages,
   ownership, comp, related-party — the tasked family/succession read).
5. 8-Ks: FY2025 results Ex-99.1 (2026-02-26, acc 0001297184-26-000007); Q2-2026 results
   Ex-99.1 (2026-08-06, acc 0001297184-26-000045) — both read for the [E3-48] test and
   the non-GAAP read; warning-letter 8-K (event 2026-07-02, filed 2026-07-08, acc
   0001297184-26-000041); Letop supply-agreement 8-K (acc 0001297184-26-000013);
   director-appointment 8-K (acc 0001104659-26-082772).
- **Figure cross-checked against the filed statement:** FY2025 OCF three ways — filed
  consolidated statement of cash flows "Net cash provided by operating activities
  **156,115**" = MD&A prose "$156.1 million" = XBRL $156.1M. **Match.** FY2024 also
  checked ($213.4M, both). H1-2026 OCF $99.2M statement = XBRL.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words:** AMPH develops and manufactures ~25 hard-to-make
  prescription drugs — sterile injectables (glucagon kits, epinephrine, lidocaine,
  enoxaparin, naloxone, emergency pre-filled syringes), inhalers (Primatene MIST OTC,
  albuterol, ipratropium), and nasal sprays (BAQSIMI, REXTOVY) — plus insulin API, in
  five plants (two California, one Massachusetts, one France, one Nanjing China), and
  sells them almost entirely through three drug wholesalers (McKesson 24% + Cencora 22% +
  Cardinal 19% of revenue) into hospitals and pharmacies. The model: pick generic drugs
  whose chemistry, device or API sourcing is hard enough that few competitors file;
  launch into the limited-competition window at 50%+ gross margin; milk the product while
  competition arrives and price erodes; replace it with the next launch. Since 2023 a
  second engine: a branded acquisition (BAQSIMI nasal glucagon, bought from Lilly for
  $500M + $125M + sales milestones, debt-funded), which is 26% of revenue. Profit =
  (limited-competition price − in-house manufacturing cost) × volume, minus 12% of
  revenue of R&D that IS the replacement machine, minus modest capex (~5% of revenue).
- **The scarce input the business controls:** a stack of regulatory/technical execution
  assets — FDA-cleared sterile facilities, complex-molecule characterization, its own
  API for key products (insulin, heparin starting material via ANP China, France) — and
  two semi-exclusive branded positions (only OTC epinephrine inhaler; only nasal
  glucagon). Whether that stack is a moat or a treadmill is exactly Q2.
- **Ten years:** the mechanism will look the same (complex generics + a branded layer);
  the individual products mostly will not — the filing itself forecasts decline for its
  #4 product and fluctuation for the rest. Legible, well disclosed, understandable.
- **VERDICT: [x] IN** — the business is understandable; what it lacks is not
  intelligibility.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — emergency and chronic medicines.
- Not price-regulated **[~]** — no statutory price control, but 65% of revenue passes
  through three wholesaler/GPO combines and government channels set rebates; pricing is
  administered by consolidated buyers.
- No close substitute **[ ] — FAILS, product by product, in the filing's own words.** A
  generic injectable is the definitionally substitutable product: the 10-K's Competition
  section states the class mechanism outright — *"As competing generic manufacturers
  receive regulatory approval on the same products, market size, revenue and gross profit
  typically decline."* The two branded exceptions have filed substitute pressure too:
  BAQSIMI competes with ready-to-use rescue pens (Gvoke, Zegalogue named class) and its
  OWN net price fell $15.9M in H1-2026; Primatene MIST competes with prescription
  albuterol at the same counter.

**The tasked melting-ice-cube test [E4-04], run on the revenue-by-product disclosure
[E4-55].** The FY2025 10-K and Q2-2026 10-Q give per-product price/volume decomposition —
unusually good disclosure — and it answers the question:

| product (share of FY2025 rev) | filed trajectory | filed cause |
|---|---|---|
| Glucagon (9.6%) | 113.7 → 108.3 → 69.1; **H1-26 −49%** (price −$13.7M, units −$6.6M) | "competition and the continued shift to ready to use glucagon products such as BAQSIMI®"; company forecasts continued decline |
| Epinephrine (9.8%) | 81.7 → 94.1 → 70.6 (FY25 units −$13.4M, price −$10.0M) | "increased competition for our multi-dose epinephrine vial product"; H1-26 held up only by "other supplier shortages" lifting the pre-filled syringe |
| Enoxaparin / dextrose (in Other) | FY25 −$9.9M / −$9.6M | "increased competition" |
| BAQSIMI (25.7%) | 126.9 → 185.4 (full distribution assumed); **H1-26 −8%: price −$15.9M, units +$8.8M** | gross-to-net discounts, chargebacks, rebates, customer mix — the branded flagship is now price-eroding too |
| Primatene MIST (15.1%) | 89.3 → 102.0 → 108.7; H1-26 −2% (timing; in-store demand growing) | the one product with an intact price story |
| Replacements | albuterol (8/24), iron sucrose (8/25), teriparatide (12/25), ipratropium (4/26) = the entire H1-26 growth | each begins its own melt clock at launch |

FY2025 total revenue: **−2%.** H1-2026: **+3%, all of it from four launches plus
competitor shortages.** The machine replaces the melt at roughly 1:1.

**[E4-04]'s own scope test:** *does a lapse in spending destroy the structure, or merely
narrow it — and does the spending defend the same advantage, or buy its replacement?* A
lapse in AMPH's R&D/filing cadence destroys the earnings within one product cycle — the
filed melt rates are −25% to −49% a year on mature lines. The $86M of R&D and the $729M
paid for BAQSIMI buy **replacements**, not defense of existing positions. That is the
excluded class — Munger's competitive destruction — and the long record is a **surfing
run [E3-51]**: twenty-five years of skilled wave-catching (first generic glucagon kit,
only OTC epinephrine MDI, only nasal glucagon, first teriparatide pen alternative). The
advantage lives in each wave's limited-competition window; the surfer must catch the next
one forever. Of the four causes of extreme success [E4-36], this record is extreme skill
on one or two variables plus wave-riding — not a structure that prospers on position
[E2-53].

- **The two-characteristic test [E2-44]: 0 of 2.** (1) Raise prices when demand is flat?
  The opposite is filed on every major line including the branded one — [E4-37] agony
  pricing. (2) Grow dollar volume with only minor additional capital? Capex is light
  (~5% of revenue) but the growth capital is the 12%-of-revenue R&D plus episodic
  nine-figure acquisitions; the replacement spend is mandatory, not optional.
- **Untapped pricing power [E3-33]:** claiming it means claiming near-monopoly [E5-28].
  Claimable nowhere: the two near-monopoly routes (nasal glucagon, OTC epinephrine MDI)
  show filed price erosion and substitute pressure respectively.
- **The Mayo test [E4-23], recorded HERE as tasked:** the CEO is also the Chief
  Scientific Officer, age 79; the co-founder COO/Chairman (his wife, 76) is the Chief
  Scientist. The 10-K's "Our Strengths" section leans on management's scientific
  expertise by name. The capability stack that is the moat claim is personified in two
  people in their late seventies. *"The moat will go when the surgeon goes"* — a
  key-person moat defect, recorded at Q2, not as a Q3 compliment.

**THE COMPETITOR ROW [E3-28]** — built and committed as
`Test Runs/_research 2026-08-26/AMPH evidence pack + competitor row (Hikma-TEVA-VTRS, Kabi gap).md`:

| Company | FY2025 ROE | 5-yr picture | injectables-class read (filed) |
|---|---|---|---|
| **AMPH (Dec-25)** | **12.9%** | mean ~18.5% (2021-25); TTM ~10.1% | gross margin 49%; the melt/replace table above |
| Hikma (Dec-25) | 16.3% | not pulled — work order | Injectables core op margin **35.3% → 31.0% → 2026 guide 27-28%; medium-term margin target WITHDRAWN**; US erosion named (testosterone, calcitonin) |
| Teva (Dec-25) | 21.2% (one good year) | **5-yr NI sum −$2.8B** | revenue flat five years; no injectables split — row limit |
| Viatris (Dec-25) | **−21%** | NI −1.27, +2.08, +0.05, −0.63, −3.51 ($B) | revenue $17.9B → $14.3B; no injectables split — row limit |
| Fresenius Kabi | **GAP — private within Fresenius SE** | — | parent deck: €8.6bn revenue, 17-19% EBIT-margin ambition |

- Peers named: **4 of the ~16 real competitors the 10-K itself lists** (most are private
  — BPI, Apotex, American Regent, Par, Meitheal, Medefil, Accord — or unsegmented giants:
  Pfizer, Fresenius Kabi). Row limit [E3-61] stated: the row shows position, not conduct.
- **What the row shows:** AMPH sits at the TOP of its row — double-digit ROE against a
  loss-making Teva/Viatris and beside Hikma. The claim "better operator in the class" is
  supported. The claim "franchise" is not: the best pure comparable (Hikma Injectables)
  just printed a four-point margin decline and withdrew its medium-term margin target —
  the whole class's pricing is eroding as post-shortage capacity returns.
- **Moat direction [E4-32], read on units [E4-55]:** mature-product units falling on
  every line the filing decomposes; totals held level only by launch cadence. The moat is
  not widening; the treadmill is running faster to stand still.
- Class: **[x] NONE as a franchise** (portfolio of wasting limited-competition windows,
  replaced by a genuinely skilled machine, in a class whose tide is going out) ·
  peer-gap caveat: with Kabi/private peers unpulled the *relative-position* claim is
  PROVISIONAL, but the *class* verdict rests on the subject's own filings and does not
  need the missing rows.
- **VERDICT: [x] OUT.** Under [E3-03] a franchise's product has no close substitute; a
  complex generic's substitute is licensed by the FDA on a schedule, and the filing
  concedes the consequence in its own Competition section. The two-characteristic test
  scores 0 of 2, pricing runs [E4-37] agony-side on every major line including the
  branded flagship, the moat's basis is replaced rather than defended ([E4-04]'s
  excluded class — the MITSY logic, as tasked), and the science leadership is two
  founders aged 79 and 76 [E4-23]. What remains is a **skilled, well-disclosed,
  top-of-row pipeline-replacement machine** — a business, not a franchise, in the class
  where *"a business, unlike a franchise, can be killed by poor management"* [E3-43].
  **The entry run stops here. [E5-13]: most names should end here, and that is the
  system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT — the hard sequence closes the
file for any BUY decision. No position exists, so no [E2-28] hold read is required.
Everything below is FOR THE RECORD, as the operator tasked — Q3 through Q5 sit under
operator rule 3's header. **Nothing below is entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands
regardless; Q3 can stop a run, never start one.*

**STEP 1 — THE WEIGHT CASE.** [x] **Daily execution HIGH** — sterile-injectable cGMP
manufacturing is a have-to-be-smart-every-day business, and the live warning letter is
the demonstration: one December inspection became a Form 483, an Official Action
Indicated classification, and a July warning letter inside seven months. [E3-38]'s
retailer logic applies. [ ] Control — no (marketable minority; exit exists).
[~] Leverage — MODERATE, named and quantified per [E4-16, E3-29]: $620M total debt
against $768M equity and $290M cash+investments; not bank-class magnification, but a
$609M maturity wall sits in 2028-29. **One determinant high → Q3 would be a BINARY GATE
for entry; no price compensates [E3-29, E5-35].**

**Honesty — the binary [E5-16]:** **no integrity disqualifier found in the documents
read** (worded per the absence-claim rule). The sweep, named: FY2025 10-K Note 19
(three CA wage/hour/PAGA employee suits — ordinary-course for a large CA employer; one
$34.1M personal-injury jury verdict, $23.1M uninsured, settled and paid Q4-2025 — a
product/operations loss, not financial dishonesty toward owners; the TJX calibration
applies); no restatement, no SEC enforcement, no auditor change (E&Y, unqualified, ICFR
effective); warning letter 8-K'd within four business days with the specific
observations named — timely disclosure conduct.

**STEP 2 — THE FLAGS [E4-22, E4-29, E5-15, E4-30, E2-52, E3-50, E2-57, E3-53, E2-49].**
- [ ] **Trumpeted projections — NOT FIRED, and notably so.** Neither earnings release
  read contains revenue or EPS guidance; the words do not appear. The [E5-30] ratchet
  was never started. Better: the filings volunteer bad news unprompted — *"We anticipate
  that sales of glucagon will continue to decline"*, ASP declines quantified per product
  per period. On the [E3-48] axis (projections vs outturn) there is nothing to test,
  which is the good case.
- [x] **Adjusted-earnings promotion [E4-29] — FIRED.** Every release headlines "adjusted
  non-GAAP net income": FY2025 **$156.6M against $98.1M GAAP (+60%)**. The add-backs:
  intangible amortization $25.0M (the annual consumption of a bought, wasting,
  24-year-life product right — a real cost), **share-based compensation $27.3M** (the
  exact adjustment [E5-06] calls cavalier), and the $23.1M litigation verdict ([E5-33]:
  the cost was real and was paid). No EBITDA promotion found; the sin here is the
  adjusted-NI headline.
- [ ] Serial share issuance [E5-15] — NOT fired; the reverse. Diluted count 53.0M (2023)
  → 42.54M cover (7/2026), −20%. Caveat recorded: the buyback program's own stated
  "primary goal" is offsetting equity-comp dilution, and grants are heavy (CEO ~$6.6M/yr
  in stock+options) — the count shrinks because repurchases far outrun generous grants.
- [ ] Weak accounting — not found: SBC expensed in GAAP, no pension, footnotes legible,
  segment note honest (one segment), related-party note names names and dollars.
- [ ] Metric-switching [E2-49] — not found across the releases read: the adjusted-NI
  definition (amortization + SBC + deal/one-time items) is stable 2024-2026; the
  litigation add-back is single-year, disclosed on its own line.
- [ ] Filed-figure tells [E4-30] — growth is visibly lumpy (fine); cash taxes paid
  $22.7M vs pretax $123.6M (18.4%) in 2025 against a ~21-26% book rate — one year only
  is retrievable from the tag; no falling multi-year pattern found in the documents read.
- [x] **Pledged shares — flagged (an open-list item; conduct/alignment, not a listed
  four-flag).** Drs. Zhang and Luo have pledged **5.7M shares — 46% of their 12.4M-share
  26.7% stake, ~13% of the company** — against credit lines of up to $57M to themselves
  and their private company APCL. The 10-Q's own words: UBS *"has an unlimited and
  unilateral right to call each of the credit lines for any reason whatsoever."* The
  company's pledging policy (2021, amended 2026) permits up to 60% of an individual's
  holding. Disclosed fully; not dishonesty; but the controlling family's personal
  leverage is collateralized by the float, with a forced-sale mechanism a lender
  controls. Monitoring item at Q6.
- [x] **The related-party web — the largest single Q3 finding [E2-68].** The family's
  private company **Hanxin** (majority owned by Zhang/Luo and family; their son Henry
  Zhang is equity holder, GM and chairman; AMPH holds 11.5%) sits on the other side of:
  the insulin/peptide **research cell banks** underlying AMPH's biosimilar candidates;
  a January 2026 manufacturing amendment granting territories for **semaglutide API and
  tablets globally**; the **corticotropin license** ($2M upfront, up to $89M milestones,
  5% royalty capped at $60M cumulative); and exclusive **Greater-China distribution of
  both flagship products** (Primatene via Genreach, BAQSIMI via Chengong) — plus Letop
  (son-controlled) supplying intermediates. Dollars to date are small ($1.1M revenue,
  $0.4M paid, $2M upfront) and disclosure is detailed and prompt (eight related 8-Ks and
  notes) — the *conduct* is clean. The *structure* is the finding: the founding family
  holds private economics in several of the company's possible next products and in its
  lead products' China rights, so every future negotiation over what could matter most
  happens across the family's own table. [E2-68] is the test — the clean case lays all
  negative factors face up, and so far this one does — but the asymmetry is permanent
  and compounding.

**Convergence check [E4-52]:** the fired flags do NOT converge on concealment — the
disclosure conduct runs the other way (no guidance, volunteered declines, prompt 8-Ks,
per-product price/volume decomposition, the half-owner test [E2-26] passes better than
most filers read under this framework). They converge instead on **family-first
structure**: heavy comp (below), pledging, and the related-party web.

**STEP 3 — THE PRIMARY TEST [E2-01].** Balance sheet first [E5-27], ten years: equity
$293.5M (2015) → $788.8M (2025), built from retained earnings; goodwill trivial ($3.3M —
acquisitions are asset deals, honestly impaired/amortized); debt $40M → $620M in one
step (BAQSIMI, 2023) on terms read in full (Note 13); cash+investments $66M → ~$290M.
ROE series (NI ÷ avg total equity, filed figures): **−1.6% (2018) · 12.4% (2019) · 0.3%
(2020) · 13.9% (2021) · 18.8% (2022) · 23.5% (2023) · 23.3% (2024) · 12.9% (2025) ·
~10.1% TTM.** Without undue leverage and, at the GAAP line, without gimmickry (the
gimmickry pressure sits in the non-GAAP layer, flagged above). Against the hand dealt
[E3-59]: top of the peer row through a period in which Teva and Viatris destroyed
capital. The 2025-26 fade is the melt showing through.

**Institutional imperative [E2-30], scored:** (1) resists change — no; the development
focus visibly shifted (generics → biosimilars/proprietary). (2) Projects to soak up
funds — not fired on M&A (BAQSIMI is one large deal, at a price the milestone structure
disciplines); partially fired on the China buildout (continued "significant investment"
at ANP with $3.2M of China revenue to show — strategic, but capital soaking into the
highest-risk jurisdiction). (3) Staff studies — not observable. (4) Peer imitation —
not fired; no guidance culture, no EBITDA theater, no serial M&A.

**Capital allocation — buybacks [E5-08, E5-31, E2-51]:** condition (1) ample funds —
qualified pass: $290M liquid against a $100M milestone due Q3-2026; H1-2026 spent $74.7M
on buybacks while OCF was $99.2M — funded from operations, not the revolver. Condition
(2) material discount to conservative IV — at H1-2026 average ~$20.30 (≈4.4× FY2024 EPS,
~1.1× book) against this run's Q5 range, repurchases sit at or below the conservative
end; the humility clause [E4-13] attached. Retention test [E3-54]: a dollar retained
2015-2025 became ~$1 of equity plus the buyback shrink at sensible prices; market value
per retained dollar depends on the quote and is currently ~1.2× book. The genuinely
strong conduct: **$485M cumulative buyback authorization executed into weakness at
single-digit multiples while insiders never sold the company a share of new stock.**
The genuinely weak conduct: **comp** — the founder couple took **$12.34M in 2025, 12.6%
of a $98M NI year** (CEO $8.31M + COO $4.03M), pay ratio 135:1, on top of 26.7%
ownership; and the remaining buyback authorization was down to $0.4M at 2026-06-30 with
no re-up announced in the documents read (watch item).

**THE GUARDRAIL:** [x] nothing here promotes the name (Q2 OUT stands; a skilled
replacement machine is a *remarkable operator, not a remarkable business* [E2-37]);
[x] key-person dependence is recorded at Q2 as a moat defect [E4-23], not here as a
strength; [x] no excisable-cancer case is argued — there is no submerged franchise to
excise [E2-36]; the managers are not the plan because there is no plan to buy.

- **Q3 FOR-THE-RECORD READ: no honesty disqualifier found; the entry gate would still
  not clear on structure.** The disclosure conduct is among the best this project has
  read (no guidance, volunteered declines, prompt bad-news 8-Ks). Set against it: the
  adjusted-NI promotion [E4-29], nearly half the controlling stake pledged to
  call-at-will lenders, comp at 12.6% of net income, and a permanent related-party
  structure that puts the family's private company inside the pipeline, the China
  rights, and the succession. *A pass here is the absence of found disqualifiers, never
  a clearance [E5-17]; IN never promotes.*

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings — **COMPUTATION — NOT A CLEARANCE** [E2-23]
Convention: multi-year mean of (OCF − SBC) − (c).

**(c), the disclosed judgment:** PP&E is NOT the [E5-20] exception class — capex runs
~5% of revenue and brackets depreciation; the filing states ongoing expansion (Rancho
capacity, Canton, ANP), so filed capex ≥ maintenance; (c) is taken at **full capex**
anyway (conservative, one windage — counted below). The REAL maintenance item in this
business is the replacement R&D: [E2-23] defines (c) by what is required to *"fully
maintain … long-term competitive position and unit volume,"* and for a melting-portfolio
business that is the R&D line — **already expensed inside OCF at $85.8M (2025)**. FY2025
answers whether the current spend level holds the position: revenue −2%. So OCF − SBC −
capex is the honest OE form here, with the melt visible in the trend rather than
hidden in an add-back. SBC subtracted in full [E5-06] at the reported charge — the
**floor** of the subtraction, not the measure [E3-70]; grants are options-heavy and the
buyback note itself says the program exists to offset them. No look-through increment
[E3-04]: the 11.5% Hanxin stake is equity-method and immaterial.

**Windows [E2-42, E4-25] — shown, not chosen-and-defended ($M):**
| window | OCF | −SBC | −capex | **OE** | yield on $936M |
|---|---|---|---|---|---|
| 5-yr mean 2021-25 | 148.0 | 21.7 | 33.1 | **93.2** | 10.0% |
| 3-yr mean 2023-25 | 184.3 | 24.0 | 38.0 | **122.3** | 13.1% |
| FY2025 | 156.1 | 27.3 | 34.9 | **93.9** | 10.0% |
| TTM 6/2026 | 184.6 | 28.9 | 31.7 | **124.0** | 13.2% |

Spread: the 3-yr/TTM windows run ~30% above the 5-yr and FY2025 windows. The distorted
years are named: 2021-22 predate BAQSIMI (smaller business, different capital
structure); 2023-24 carry the BAQSIMI step-up plus peak glucagon/epinephrine pricing;
TTM OCF is flattered by working-capital timing (H1-26 OCF $99.2M against NI $36.8M).

**Normalize DOWN for luck [E4-41], then the bottom boundary [E5-34] — the tasked moves:**
favourable exogenous breaks inside the window, named from the filing: (a) **competitor
shortage demand** — epinephrine PFS +$6.1M (H1-26), sodium bicarbonate, atropine,
dextrose, phytonadione all up "due to … other supplier shortages" — the filing itself
calls these fluctuating; (b) **glucagon's remaining stream** — ~$40M/yr run-rate falling
at −49%, declared terminal by the filing; (c) **BAQSIMI price** — filed drift of
−$15.9M/half not yet annualized through. Bottom boundary: start TTM $124M; strip
glucagon's after-tax contribution (~$15-20M), shortage luck (~$5-10M), one further
BAQSIMI gross-to-net notch (~$10-15M); credit launched products only at filed H1
run-rates (ipratropium, teriparatide, iron sucrose ramps partially offset). **Bottom
boundary OE ≈ $70-95M → yield 7.5-10.2%.** The 3-yr and TTM windows are refused as OE
bases in writing [E4-41]; they are displayed as the top of the range.

### Great, good, or gruesome? [E4-20]
**Good, not great [E4-43].** Returns on added capital have been real — mid-to-high-teens
ROE across the window, top of the peer row — but the added capital is **mandatory**
(every retained dollar must buy the next product before the current one melts), and the
class tide (Hikma's withdrawn margin target) says the reinvestment rate is drifting
down. Not gruesome: capex is light, cash conversion is real, thirteen years of retained
earnings built $495M of equity and a fivefold revenue base.

### Staying power — all three [E5-11]
1. **Large and reliable stream:** large; NOT reliable at the product level — top five
   products are 68% of revenue, the #1 (26%) is price-eroding, the #4 is in terminal
   decline, and the melt/replace cadence resets every year. Profitable every year since
   2019 (loss year 2018); reliability caveat written.
2. **Massive liquid assets:** $290M cash+investments against $620M debt. The $219.5M
   unused revolver is [E5-39] kindness-of-strangers capital and is NOT counted.
   Adequate, not massive.
3. **No significant near-term cash requirements — the leg that bites:** **$100M BAQSIMI
   milestone due Q3-2026** (triggered June 2026, filed); further sales milestones
   contingent; then the wall: **$255.7M (term loan, June 2028) + $353.5M (converts,
   March 2029)** against ~$150-185M/yr OCF. The converts sit at a $62.96 conversion
   price against a $22 stock — they will be **cash** obligations, and the term loan is
   secured by substantially all assets [E3-52 read: covenanted, due-dated bank debt, the
   opposite of float]. Coverage test [E2-54]: interest $25.5M against pretax+interest
   ~$149M and OCF $156M, net of ample capex — comfortably met today; the wall is a
   refinancing dependence, not a current strain. [E2-64] watch: whether they term out
   early or wait.

### The specific ways THIS business dies [E2-27, E3-24] — exposure, not experience [E4-40]
1. **The FDA facility death (live, filed):** IMS South El Monte — Dec-2025 inspection →
   Form 483 → **Official Action Indicated (Apr-2026)** → **Warning Letter (2026-07-02)**:
   investigation procedures, environmental monitoring, equipment. Today: no distribution
   stop, one product suspended, remediation raising costs. The exposure: warning letter
   → consent decree/import detention is the industry's known cascade; IMS makes the
   emergency-syringe portfolio and naloxone. Site revenue is not filed (stated below);
   if remediation slips and the site halts, the loss is plausibly a nine-figure revenue
   event plus fixed-cost drag. An OAI facility also typically blocks NEW approvals from
   that site while open. **Likelihood: a real possibility** for material drag; a
   low-level possibility for the full halt.
2. **The BAQSIMI concentration cliff:** 26% of revenue, price already fading (filed
   −$15.9M/half), single-CMO supply (Note 6), rescue-pen competition, and $350M of
   remaining milestones that only bite if sales GROW. A 30% revenue cut (~$55M) at
   ~70% incremental margin ≈ **$38M pretax ≈ 30-40% of bottom-boundary OE.**
   **Likelihood: price pressure is certain (it is filed); the cliff is a real
   possibility across a holding period.**
3. **The China death [E4-40]:** ANP (Nanjing) makes the heparin starting material for
   enoxaparin, Amphadase starting material, three other APIs, the insulin API buildout
   and the GLP-1 APIs; $110M of long-lived assets; the 10-K names expropriation ("total
   loss of our investment"), tariffs (Section 232 pharma investigation pending),
   export controls, and swine-flu heparin import risk. A China supply cut disrupts
   multiple US products simultaneously with FDA-approval lag on any alternative source.
   **Likelihood: low-level possibility for the total-loss form; a real possibility for
   tariff/friction cost.**
4. **The Primatene propellant death:** the AIM Act phases down the HFC propellant in
   the #2 product (15% of revenue, high margin); reformulation to a new propellant
   needs FDA approval the filing says cannot be assured. **Likelihood: a low-level
   possibility, on the filing's own naming.**
5. **The pipeline-failure death (the class's base case):** if the launch cadence
   misses for two-three years while glucagon/epinephrine/enoxaparin melt at filed
   rates, revenue declines mid-single-digits annually and the 2028-29 wall meets a
   shrinking OCF. The insulin bet (AMP-004 on file; interchangeability sought) lands in
   a market where three global incumbents and Biocon already fight at prices that
   humbled Viatris. **Likelihood: some product-cycle miss over a decade — likely; the
   full compounding form — a real possibility.**
6. **The pledged-stock spiral (a stock death, not a business death):** 5.7M pledged
   shares, one lender callable at will; a drawdown forces sales into weakness, which
   forces more. Named because the operator's account would live through the quote.
   **Likelihood: a real possibility in any deep drawdown.**
- **Q4 FOR-THE-RECORD READ: survives the current regime on the filed balance sheet —
  every death above wounds value before solvency except the wall-meets-melt compound
  (5), which is the class's terminal mechanism. Were the gate live it would read IN on
  current-regime survival with the [E5-11] leg-3 refinancing dependence and leg-1
  concentration caveats written.**

---
## Q5 — FOR THE RECORD — **COMPUTATION — NOT A CLEARANCE**
*(Q1-Q4 did not close IN; operator rule 3 header governs; no entry language.)*

**THE FLOOR [E4-28] — "that's the figure we quit on."**

**1. THE YIELD** (owner earnings ÷ market cap $936M · sovereign **5.19%**):
| OE basis | OE | yield | points over sovereign |
|---|---|---|---|
| **Bottom boundary [E5-34, E4-41]** | **$70-95M** | **7.5-10.2%** | **+2.3 to +5.0** |
| 5-yr mean / FY2025 (they agree) | $93-94M | 10.0% | +4.8 |
| 3-yr mean (refused as base, shown) | $122M | 13.1% | +7.9 |
| TTM (refused as base, shown) | $124M | 13.2% | +8.0 |

**2. WHAT THE PRICE ALREADY ASSUMES:** $936M × 10% floor = $94M of OE — i.e. the price
asks for FY2025's exact result to hold **flat forever**: every filed melt (glucagon to
zero, BAQSIMI price drift, epinephrine competition) must be fully replaced by launches,
every year, indefinitely, with no net growth required but none of the filed decline
either. That is not a rate call; it is a **perpetual-replacement call** on a machine
whose founders are 79 and 76 — which is Q2's finding priced in dollars. The ceiling
[E2-63] is stated: without continuous successful reinvestment the portfolio shrinks at
the filed melt rates; the upside case (insulin interchangeability, BAQSIMI
international) carries [E4-35]'s burden of proof and is not credited at the floor.

**3. WHAT YOU ARE PAID:** +2.3 to +5.0 points over the sovereign at the bottom
boundary, BEFORE any pipeline success is credited — and the pipeline succeeding is the
same assumption that holds the boundary up.

**THE FLOOR VERDICT, stated plainly:** the 10% quit-figure sits **inside** the
bottom-boundary band (7.5-10.2%). Honest pre-tax expectancy at $22.01 is *roughly at*
the floor: the melt and the replacement machine currently cancel, so expectancy ≈ the
current yield ≈ 8-10%, with the tails owned by the FDA letter, BAQSIMI, and succession.
**Bar: screamer test only [E4-01]** — the price does NOT clear the conservative case
(bottom boundary capitalized at the floor rate gives $0.7-0.95B ≈ **$16.50-22.30/share**
against $22.01: the quote sits at the very top of the floor-clearing band, not below
it), and it sits well below the flat-forever sovereign capitalization ($1.35-1.85B ≈
$32-43/share). **Price inside the range → the middle box: no useful conclusion; move
on.** That is the finished answer [E4-25], and it agrees with Q2's stop. **Windage
count: one** — (c) taken at full capex despite filed expansion inside it; the [E4-41]
strip-outs are that rule's required moves, not windage.

**The value, as a round-number range [E4-01], for the record only:** roughly **$0.7-1.0B**
(bottom boundary at the quit-rate) to roughly **$1.4-1.8B** (bottom boundary held flat
forever at the bare sovereign); cap $936M sits in the lower half of the range. Too wide
to conclude on, and that is the conclusion.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists; pre-committed yardsticks for the WATCH LIST, set prior to any act
[E1-02]. **Alert thresholds LISTED ONLY** — `tools/alerts.json` not edited.)*

**Q2 REOPEN CONDITIONS (the only route back to entry) — BOTH required:**
1. **Evidence, not price.** Q2 failed on CLASS (basis replaced, not defended) plus the
   [E4-23] key-person defect, so the reopen bar is structural: **(a)** filed evidence of
   a *defended* position — a flagship (Primatene MIST or BAQSIMI) posting two-plus years
   of RISING price with flat-or-rising units in the 10-K's own decomposition, or an
   interchangeable-insulin franchise with filed pricing power rather than launch-year
   share-buying; AND **(b)** the Mayo fix — a disclosed post-founder technical
   organization (a CSO who is not the CEO, a chief scientist who is not the chairman)
   that keeps the launch cadence through a leadership transition. A big pipeline
   approval alone reopens nothing; it is one more wave.
2. **Price [E4-28]:** the bottom boundary pays the floor with zero growth credited at
   **≤ ~$700-800M cap ≈ roughly $16.50-19/share.** Below ~$16.50 this file gets re-read
   for the record; entry still requires condition 1, which today does not exist.

**Watch-list metrics and thresholds (review triggers, not auto-executions):**
- **The warning letter:** any 8-K on IMS escalation (consent decree, import alert,
  recall) = death 1 forming; a closeout letter = the drag lifting. Also watch whether
  new approvals stall (an OAI site blocks approvals from that facility).
- **The melt rate:** glucagon below $10M/half (terminal); BAQSIMI gross-to-net — a
  third consecutive half of price decline > $10M = the branded story failing;
  epinephrine PFS reverting when competitor shortages end.
- **The replacement rate:** launch cadence — fewer than two meaningful launches per
  year, or "Other products" declining two halves running = the treadmill slowing.
- **AMP-004 insulin aspart:** FDA action (approval/CRL) — the biggest single wave in
  the pipeline; action dates not published (noted below).
- **The wall:** any refinancing 8-K for the 2028 term loan / 2029 converts — early
  action = [E2-64] conduct; silence into 2027 = leg-3 pressure.
- **The family:** pledged-share count each 10-Q/proxy (above ~6M or any forced-sale
  8-K/Form 4 cluster = the spiral); related-party dollars (any Hanxin agreement
  crossing ~$10M/yr = the asymmetry going material); succession announcements; comp
  trajectory in the 2027 proxy.
- **Buybacks:** whether the board re-ups beyond the $0.4M remaining authorization at
  prices below ~1.2× book = the rational pattern holding; a re-up used at higher
  multiples while the melt runs = conduct downgrade.
- **China:** Section 232 pharma tariff outcome; any ANP supply disruption 8-K.
- **Price alert (list only):** AMPH below **$16.50** → re-run both reopen conditions.
- **Next catalysts:** Q3-2026 10-Q ~early Nov 2026 · FY2026 results + 10-K ~late Feb
  2027 · DEF 14A ~Apr 2027 · warning-letter resolution 8-Ks as filed · AMP-004 action
  (date not public).

**The taxable never-switch test, answered for the operator's account [E2-46, E3-64]:**
the earmarked account wants a dividend-paying compounder taxed once at the end. **AMPH
pays no dividend, so it fails the account's mandate on its face** — stated up front and
again here. Beyond the mandate: a melting-and-replacing portfolio is a business whose
intrinsic value must be re-underwritten every product cycle; [E2-28]'s hold conditions
would be under permanent review, which is the opposite of the never-switch shape. The
buyback is the only shareholder-cash channel, and its continuation now depends on a
board re-up.

- **VERDICT: [x] IN** — what would prove this run wrong is written, dated and
  document-named on both sides (structural evidence + price for reopen; melt rate,
  replacement rate, FDA cascade, family metrics for the class thesis).

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (Q2 OUT); Q3-Q5 written
      for the record only, headed COMPUTATION — NOT A CLEARANCE per operator rule 3
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q2's
      peer-gap PROVISIONAL attaches to the relative-position claim inside an OUT
      verdict, not to any IN)
- [x] Market cap verified vs filed shares FIRST as tasked ($936M vs sweep ~$938M, 0.2%;
      the sweep's 6.6% yield figure not reproduced — computed yields 7.5-13.2% shown
      with their bases)
- [x] Step 0: filings read with accession numbers; FY2025 OCF cross-checked three ways
      (statement 156,115 = MD&A $156.1M = XBRL); FY2024 and H1-2026 also checked
- [x] Owner earnings multi-year: all four windows shown with the spread; 3-yr and TTM
      refused as bases IN WRITING under [E4-41]; bottom boundary [E5-34] computed with
      named luck stripped; (c) a disclosed judgment (full capex; replacement R&D
      identified as the true maintenance line, already inside OCF); SBC subtracted in
      full at the reported-charge floor [E3-70]
- [x] BAQSIMI acquisition debt terms read from Note 13 as tasked [E3-52]: converts
      2%/2029/$62.96 strike (cash obligation at this price), secured term loan
      SOFR+margin swapped 4.04%, wall 2028-29 $609M, $100M milestone due Q3-2026
- [x] Competitor row: 4 of the 10-K's ~16 named competitors pulled (Hikma from its
      audited results release; TEVA/VTRS from 10-K XBRL, labelled); Fresenius Kabi and
      Pfizer gaps NAMED with the blocked rung; row limit [E3-61] stated; committed as a
      research file
- [x] Sovereign for the earnings currency (USD) from the issuing-authority series,
      dated 2026-08-27; tools/run.py failure recorded
- [x] Value stated as round-number ranges; price-inside-range identified as itself the
      conclusion [E4-25]; floor verdict stated plainly
- [x] One bar (screamer, for the record); windage count: one, justified in writing
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Q6 written regardless as tasked; alerts LISTED ONLY; no-dividend mismatch stated
      up front AND at the account-mandate test
- [x] The market-beating claim not made anywhere; judgments carry ledger ids or are
      labelled judgments/estimates
- [x] No shared files edited; only this run file + one evidence file created
- [ ] Run committed to git — pending

## REGISTER
- Verdict: **[x] OUT (about the business, at Q2 — for entry).** No position held.
  Q3 for the record: no honesty disqualifier found; disclosure conduct unusually good
  (no guidance, volunteered declines, prompt 8-Ks); the adjusted-NI promotion, the
  pledged half-stake, 12.6%-of-NI founder comp, and the Hanxin related-party structure
  keep the gate shut on structure. Q4 for the record: survives the current regime;
  $100M milestone Q3-2026 and a $609M 2028-29 wall are the dated cash requirements;
  six deaths named and quantified. Q5 computation: the floor sits inside the
  bottom-boundary band (7.5-10.2% on $936M); price inside the range → no useful
  conclusion.
- One line: **a genuinely skilled, honestly disclosed pipeline-replacement machine at
  the top of a decaying class — every mature product's price and volume decline is
  filed in its own MD&A, the branded flagship is already price-eroding, the moat's
  basis is replaced rather than defended [E4-04], the science leadership is a married
  couple aged 79 and 76 who have pledged nearly half their stake and whose family's
  private company owns pieces of the pipeline, the China rights, and therefore the
  succession — and at $22 the market is paying almost exactly for the machine to run
  flat forever, which is the one thing the filings say it cannot do without perpetual
  new waves.**
- **Work orders (UNRESEARCHED, with routes):**
  1. Hikma 5-yr ROE/margin series — hikma.com annual reports 2021-2024, ordinary PDF
     retrieval; completes the row's best comparable.
  2. FDA Warning Letter text for IMS — fda.gov warning-letters database (published with
     a lag); sharpens death 1's severity read.
  3. 2026 annual-meeting voting results (say-on-pay outturn) — 8-K of ~June 2026, acc
     0001297184-26-000038, EDGAR; completes the comp read.
  4. FY2026 10-K (~Feb 2027) — glucagon terminal rate, BAQSIMI gross-to-net, IMS
     remediation cost, buyback re-up.
  None blocks the verdict; Q2 is decided on the subject's own filed concessions.
- **UNKNOWABLE (named):** IMS site-level revenue (not filed at product-site
  granularity — death 1 stays banded); AMP-004 FDA action timing (biosimilar user-fee
  dates are not published); succession intent (no document exists that resolves it).
- **The single biggest concern:** the succession lollapalooza [E4-52] — a 79-year-old
  CEO-CSO and a 76-year-old COO-Chairman (married, 26.7% control, classified board)
  with ~46% of their stake pledged to lenders one of whom can call at will, whose son
  runs and whose family majority-owns the private company holding the insulin cell
  banks, global semaglutide territories, corticotropin IP and Greater-China rights to
  both flagship products — so the moment the key-person moat defect [E4-23] matures,
  the company must negotiate for pieces of its own future with the founder's estate,
  possibly mid-margin-call, and possibly with an unresolved FDA warning letter running.
  Nothing in the filings says anyone is being dishonest; everything in the filings
  says the structure concentrates exactly where the business is already weakest.

*This file is a judgment by the AI running the framework; underlying facts are the
FY2025 10-K (acc 0001297184-26-000009), the Q2-2026 10-Q (acc 0001297184-26-000047),
the Q1-2026 10-Q (acc 0001297184-26-000033), the 2026 DEF 14A (acc
0001297184-26-000023), the five 8-Ks cited in Step 0, Hikma's audited FY2025 results
release, TEVA/VTRS 10-K XBRL fact sets, the Fresenius SE FY/25 deck, FRED DGS30, and
one flagged live quote — transcribed in the committed evidence pack. Where a number is
a judgment or estimate — the (c) treatment, the bottom-boundary band, the death
quantifications, the reopen band — it is labelled as one.*
