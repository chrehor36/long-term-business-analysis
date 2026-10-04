# Company Run — Ethan Allen Interiors Inc. (NYSE: ETD) — 2026-08-30
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`.

**Position context: NONE HELD. Fresh entry run.** Surfaced by the 2026-08-30 sourcing
sweep (9% statute yield; the largest non-bank on the reading list). **Bias declared per
operator rule 9:** $2,750 of taxable capital is earmarked for the first name that
graduates, so the analyst's incentive is to clear this name. The iron prescription
[E4-51] is therefore applied — the bear case is stated as its best advocate would state
it (conveniently, a real bear holding 5.0% is on the record in SEC filings this month,
and his case is quoted, checked against the filings, and where the filings support him,
credited). Disconfirming evidence was hunted hardest [E4-26]. **A "no" verdict is a fully
successful run.**

**The live event, declared up front:** ETD is in an open proxy contest. Douglas G.
Bergeron / DGB Investment (5.0% beneficial owner; SC 13D filed 2026-08-05, acc.
0001193805-26-001025; amended 2026-08-27, acc. 0000921895-26-002351) has nominated a
director slate for the 2026 annual meeting (DFAN14A 2026-08-20, acc.
0000921895-26-002266). The company responded with DEFA14As on 2026-08-07 (acc.
0001437749-26-026594, a Bloomberg TV transcript) and 2026-08-19 (acc.
0001437749-26-028555, declaring a **$3.00/share special dividend, ~$76M**, record
2026-09-03, payable 2026-09-17). A prior activist 13D campaign ran in 2015-16 (SC 13D
2015-08-18, acc. 0000902664-15-003427, amendments into January 2016).

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · 2026-08-27 · FRED DGS30** (Treasury constant maturity; the
  project's standing USD source). `tools/sources.py` USD fetch failed twice from this
  environment (remote disconnect); the identical series was pulled directly from
  `fredgraph.csv` and is dated. FRED's known 1-2 day lag is immaterial and noted.
- FX: none. Quote currency = earnings currency = USD.
- Price: **$23.47, NYSE close 2026-08-28 (Yahoo — aggregator, live quote only, flagged).**
- **Quote basis warning:** the quote is CUM the declared $3.00 special dividend (record
  2026-09-03; ex-date ~2026-09-02). Every yield below is shown on both the cum basis and
  the ex basis, because $76M of the market cap is cash already leaving.
- Market cap: 25,446,339 shares (filed cover count, 10-Q of 2026-04-29, as of 2026-04-22)
  less 250,000 Q4 repurchases (FY2026 press release) ≈ **25.20M shares** (the company's
  own "$76M ÷ $3.00" implies ≈25.3M; the 0.4% gap is vesting timing). Cap ≈ **$592M cum
  the special · ≈$516M ex the special.**

**The filing was read — not tagged data [E3-27]:**
- **The FY2026 10-K (year ended 2026-06-30) is NOT YET FILED.** EDGAR checked 2026-08-30:
  the most recent ETD filing is the 2026-08-27 13D/A; last year's 10-K arrived 2025-08-22,
  so this year's is due within days. This run therefore uses:
  1. **FY2025 Form 10-K, filed 2025-08-22, accession 0001437749-25-027594** (audited;
     auditor CohnReznick LLP) — [x] MD&A [x] cash-flow statement incl. detail lines
     [x] footnotes (leases Note 6; credit facility; legal; advertising; equity statement);
  2. **FY2026 Q4/full-year press release, 8-K Ex-99.1, filed 2026-07-29, accession
     0001437749-26-024880** (unaudited full-year statements incl. balance sheet and
     key-measures reconciliation);
  3. **Q3 FY2026 Form 10-Q, filed 2026-04-29, accession 0001437749-26-013892** (nine-month
     cash-flow detail; cover share count);
  4. **DEF 14A, filed 2025-09-26, accession 0001104659-25-093869** (comp, board,
     related-party) plus the contest filings named in the header.
- **Figure cross-checked against the filed statement:** FY2025 OCF. The filed
  consolidated statement of cash flows (10-K, p. 41 area) reads "Net cash provided by
  operating activities **61,696**"; XBRL companyfacts carries 61.7M; the FY2026 press
  release comparative column carries $61,696K. Three-way match. Second check: FY2025 net
  sales $614,649K identical in the 10-K income statement and the PR comparative column.
- Standing work order: **re-run the arithmetic against the FY2026 10-K when it files
  (~days away)** — the FY2026 D&A and SBC below are 9-month-annualized estimates.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words:** Ethan Allen sells rooms, not sofas. A client walks
  into one of 141 company design centers (171 in North America counting 30 independents),
  gets a free interior designer who plans the whole room, and orders custom-covered
  furniture that ETD builds to order in its own eleven North American plants (four US
  plants plus sawmill/rough mill/kiln, three in Mexico, one in Honduras — ~75% of product)
  and delivers flat-rate nationwide through its own logistics. Because it owns the
  factory, the retail margin and the manufacturing margin stack: 61.2% consolidated gross
  margin in FY2026, the highest in its peer set. The client pays a deposit at order
  ($62.7M of customer deposits held at 2026-06-30), which funds the work-in-process. It
  is a housing-linked, big-ticket, discretionary cyclical: FY2026 net sales $579.5M,
  operating income $45.0M (7.8%), net income $39.9M, OCF $52.5M, zero debt, $187.5M cash
  and investments.
- **The scarce input the business controls:** the interior-designer relationship network
  (500+ designers whose client books are the sales engine) plus quick-turn custom
  manufacturing capacity in North America. Nobody else in the set owns both at this scale
  (Bassett tries at half the margin; Arhaus and RH design-serve but import).
- **Ten years:** the mechanism (design service + custom make + white-glove delivery) will
  look the same. The two honest overhangs are the housing cycle (demand level
  unpredictable, mechanism intact) and a secular question — the unit base has shrunk for
  two decades (see Q2) — which is a Q2/Q4 matter, not an intelligibility failure.
- **VERDICT: [x] IN** — the business is legible; the cyclical level lands at Q4/Q5 as
  range width, and the secular direction is Q2's question.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — premium home furnishing, demonstrated demand for 94 years.
- Not price-regulated **[x]** — none.
- No close substitute **[ ] — FAILS at the margin, and the filed record is the evidence.**
  For the installed clientele the bundle (their designer + custom make + delivery) has no
  close substitute — they accepted price increases through four down years, gross margin
  59.3% → 61.2% (FY2022→FY2026) with capacity underutilized (FY2025 MD&A: "increased
  plant inefficiencies and higher manufacturing variances" from lower volume). That is
  the [E2-44] first characteristic, genuinely passed. But the marginal customer — the one
  who decides whether the franchise grows — demonstrably substitutes: ETD revenue fell
  **29% from the FY2022 peak** ($817.8M → $579.5M) while in the same premium category
  Arhaus GREW +12% and RH held ~flat (row below). Two decades: ~$1.0B of net sales in
  FY2007 (put to the CEO on Bloomberg, 2026-08-07 DEFA14A transcript, premise accepted)
  → $579.5M in FY2026.

**The [E2-44] two-characteristic test: 1 of 2.** Prices up under slack demand — pass
(and note the row: HVT, LZB and BSET also raised GM in the same slump, so the pricing
hold is industry conduct among the shrinking incumbents, not a unique power). Dollar
volume growth with minor capital — fail: four consecutive down years, two-decade halving.

**The units are the honest series [E4-55].** ETD files no unit-volume series, but the
physical proxies all point one way while price rises held the dollar line up: FY2025
MD&A attributes the FY2025 decline to "lower delivered unit volume" offset by "higher
average ticket prices"; the CEO's own words (2026-08-07 DEFA14A): "We have today about
30 to 40% less interior designers than we had 4 or 5 years back"; design centers 142
company-operated at FY2025, 141 at FY2026; 20 manufacturing plants "8 or 10 years back"
→ 11 today. Precision Steel's lesson verbatim: dollar revenue flattered by pricing is
how a shrinking franchise hides.

**The attacker's test [E2-45] — answered empirically, not hypothetically.** The question
is how one would attack it with ample capital and skilled personnel. Arhaus IS the
answer: a premium furniture retailer with in-store designers, built to $1.38B of revenue
(2.4× ETD) and +12% growth through the identical demand slump, at a 38.9% gross margin —
it priced below ETD's umbrella and took the growth. RH did the same above it. The attack
happened, in the filed record, and succeeded.

**Direction [E4-32]: NARROWING.** The moat over the installed base holds (pricing
conduct still yawn-class, not agony-class [E4-37]); the base itself shrinks every year.
The knight question is deferred to Q3 — but note [E4-23] here where it belongs:

**The Mayo test [E4-23] — a moat defect recorded AT Q2.** The strategy is explicitly one
man's: Chairman/President/CEO since 1988, the sole executive under a written employment
agreement, and on the record this month personally as the author of every strategic
refusal ("I said, no, we're going to continue the focus on interior design" — 2026-08-07
DEFA14A). The brand, plants and designer network would survive him; the operating
formula has never been demonstrated under anyone else in 38 years. "The moat will go
when the surgeon goes" cannot be ruled out from filings, and the surgeon is 82.

**The tariff regime is not a moat [E2-59].** Section 301 furniture tariffs of 10-12.5%
effective 2026-07-24 (FY2026 PR) penalize import-based competitors and favor ETD's ~75%
North American manufacturing — but ETD's own Q4 FY2026 margin was hit by tariffs on its
imported quarter (adjusted operating margin 7.4% "reflects the impact of tariffs"), and
$5.0M of prior IEEPA tariffs was refunded. A regime floor belongs to the regime: "That
day is gone" is how it ends. Recorded as a tailwind, credited as nothing.

**Commodity check [E2-58]:** not a commodity at the custom-premium end — differentiation
is real (the margin structure proves it). The franchise question fails on substitution
at the margin and direction, not on commoditization.

**Untapped pricing power [E3-33]:** none unexercised — pricing has been used
continuously (it is what held the dollar line up), and it did not stop the melt. The
near-monopoly claim [E5-28] cannot be made for a company losing share.

**THE COMPETITOR ROW [E3-28]** — built and committed as
`Test Runs/_research 2026-08-26/ETD competitor row (LZB-HVT-ARHS-BSET-RH).md`; summary
(latest fiscal year each, filing-sourced, accessions in the row file; fiscal calendars
differ and are stated there):

| Company | net sales | gross margin | op margin | revenue peak→latest |
|---|---|---|---|---|
| **ETD** (FY Jun-2026) | $579.5M | **61.2%** | 7.8% GAAP / 8.1% adj | **−29.1%** |
| La-Z-Boy (FY Apr-2026) | $2,127M | 44.0% | 6.1% | −9.4% (rising again) |
| Haverty's (CY2025) | $759M | 60.7% | ~3.5% pretax | −27.5% |
| Arhaus (CY2025) | $1,379M | 38.9% | 6.4% | **+12.2%** |
| Bassett (FY Nov-2025) | $335M | 56.3% | 2.3% (losses CY23-24) | −31.1% |
| RH (FY Jan-2026, context) | $3,440M | 44.1% | 11.3% (NI margin 3.6% after interest) | −4.2% |

- Peers named: **5 of the industry's ~6-8 real public competitors** (WSM and the
  Wayfair-class import channel not pulled; retrievable, work order in the row file).
- What the row gives ETD: the best margins in the set at the trough, and the best
  like-for-like comparison of all — Bassett, the other vertically integrated
  maker-retailer with design service, ran operating LOSSES through the same slump ETD
  crossed at 7.8-10.2%. The vertical-integration advantage is real.
- What the row takes away: everyone shrank except the attackers; ETD shrank second-worst;
  the premium category's growth went to Arhaus and RH. Position without direction.
- Row limit [E3-61] stated: the row shows position, not conduct.

- Class: **[x] NARROW** (real, over an installed and aging clientele) · Direction:
  **NARROWING** (units, designers, centers, share — every physical series down)
- **VERDICT: [x] OUT.** Under [E3-03] a franchise is thought by its customers to have no
  close substitute; the marginal customer's substitution is a filed, two-decade,
  accelerating-competitor fact. The two-characteristic test scores 1 of 2; the attacker's
  test was run in the real world by Arhaus and the attack won; the direction test — "the
  primary criterion of a great business" [E4-32] — reads narrowing on every physical
  series; and the strategy's dependence on one 82-year-old author is a durability defect
  recorded here per [E4-23]. What remains is a genuinely differentiated, superbly
  margined, honestly run **business in secular unit decline** — "a business, unlike a
  franchise, can be killed by poor management" [E3-43] — and at Q3 weight this class of
  business makes the manager a gate precisely when the manager question is at its least
  answerable. **The entry run stops here. [E5-13]: most names should end here, and that
  is the system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT — the hard sequence closes the
file for any BUY decision. No position exists, so no [E2-28] hold read is required.
Everything below is FOR THE RECORD — the operator tasked this run with nailing the Q3
succession facts, the owner-earnings range, and the floor arithmetic, and Q6 is written
regardless. **Every valuation figure below operator rule 3's header. Nothing below is
entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless
— Q3 can stop a run, never start one.*

**STEP 1 — THE WEIGHT CASE.** [x] **Daily execution HIGH** — this is [E3-38]'s own
worked example: "For a retailer, hiring that nephew would be an express ticket to
bankruptcy." A design-led, order-book retailer must be run well every day. [ ] Control —
no (marketable minority; exit exists). [ ] Leverage — no (zero debt, net cash $187.5M).
**One determinant high → Q3 would be a BINARY GATE for entry; no price compensates
[E3-29, E5-35].**

**Honesty — the binary [E5-16]:** no integrity matter found. The sweep, named: FY2025
10-K Legal Proceedings (ordinary-course only, no material loss expected); DEF 14A
related-party section ("there have been **no** related person transactions requiring
approval, ratification or disclosure" since FY2025 began — Item 404); no SEC enforcement
or restatement found in the filings read. Worded per the absence-claim rule: no instance
found in the documents read, not "none exists."

**STEP 2 — THE FLAGS [E4-22, E4-29, E5-15, E4-30, E2-52, E3-50, E2-57, E3-53].**
- [ ] Weak accounting — not fired. SBC expensed; no pension plan found in the statements
  read (NEO pension column zero); auditor opinions unqualified (CohnReznick LLP,
  ratified 22.5M-for at the 2025 meeting).
- [ ] Unintelligible footnotes — not fired; the statements are unusually simple (no
  debt, no derivatives, no segments games; two segments, deposits and backlog disclosed).
- [ ] Trumpeted projections [E3-48] — not fired: **no quantitative revenue or EPS
  guidance found in any document read** (FY2026 PR, Q2/Q3 releases, MD&A). The guidance
  ratchet [E5-30] never started. This is the strongest single Q3 positive.
- [ ] Serial share issuance — the reverse: shares 27.6M (FY2018) → 25.2M (FY2026); no
  dividends-by-issuance [E2-52].
- [ ] EBITDA / adjusted promotion [E4-29] — barely present: EBITDA appears once in the
  FY2025 10-K, inside the credit-facility covenant definition only. Adjusted measures in
  the PR are small, reconciled, and in Q4 FY2026 ran AGAINST management's favor (they
  adjusted OUT a $5.0M one-time tariff-refund gain, reporting adjusted GM 59.7% below
  GAAP 63.1%) — the [E2-69] candor direction.
- [ ] Filed-figure tells [E4-30] — not fired: growth is visibly lumpy; cash taxes ÷
  pretax = 29.7% (FY23), 23.3% (FY24), 26.9% (FY25) — no falling pattern.
- [x] **Board conduct 2026 — FIRED, the live item.** Three linked facts: (1) six
  directors were elected 2025-11-05 (8-K acc. 0001437749-25-033364); per DGB's account —
  uncontradicted in either company DEFA14A read — the board "reduced its size from six
  to five directors in January 2026," and this was disclosed only privately,
  counsel-to-counsel, in August 2026 upon direct inquiry, two weeks after the
  nomination; **no Item 5.02 8-K disclosing a director departure appears in the EDGAR
  submissions list between 2025-11-05 and 2026-08-27** (the 2026-01-28 8-K is Q2
  earnings only — checked). A shrunk board of four independents, none with retail,
  furniture, luxury-goods or e-commerce operating background (2025 proxy bios: UN
  finance, two advertising executives, commercial real estate, healthcare/tech). (2) The
  **$3.00 special dividend (~$76M, ≈15% of the ex-div market cap) was declared
  2026-08-19, two weeks into the contest** — the sixth consecutive year of specials, but
  12× August 2025's $0.25 special, and the second special declared within a month. (3)
  Succession: the CEO is 82 (10-K: age 81 at 2025-08-22), sole executive under a written
  agreement (amended 2024-07-30, term ends **2027-06-30**), no successor or process
  disclosed anywhere read, and his on-record answer to the question this month was
  personal fitness ("I look much younger than I am... Our board... has never raised this
  issue" — 2026-08-07 DEFA14A). For a binary-gate retailer, the half-owner test [E2-26]
  fails on exactly the facts a half-owner would most want: who is the next operator, and
  what happened to the sixth board seat.

**STEP 3 — THE PRIMARY TEST [E2-01].** Balance sheet first [E5-27]: eight years of
year-end equity $383.7M → $471.5M (FY2018→FY2026) with **net cash every year**, no
goodwill games (goodwill static at $25.4M), treasury stock from real buybacks of an
earlier era. ROE series (NI ÷ avg equity; FY23-25 as filed in the MD&A): **9.5% (FY18) ·
6.9% · 2.6% (COVID) · 17.7% · 27.2% · 23.5% · 13.4% · 10.8% · 8.4% (FY2026)** — the
housing cycle in miniature, full-cycle mean ~13%, earned with roughly a third of equity
sitting in cash and investments. On operating equity the trough return is ~12%
(judgment: ~$34M after-tax operating income on ~$284M equity ex-cash). Passes as a
record, without leverage or gimmickry.

**Institutional imperative [E2-30], scored:** (1) resists any change in current
direction — **fired, textbook**: one strategy, one author, 38 years, defended this month
against a shareholder demanding change; whether the strategy is right is a different
question from whether the institution can change it. (2) Projects soak up funds — not
fired in the acquisition sense (no empire-building found; the cash went out as
dividends, $402M over the decade per the 2026-08-19 release). (3) Staff studies — not
observable. (4) Peer imitation — not fired; the refusal to imitate (no e-commerce pivot,
no Wayfair listing) is the strategy itself, for better and worse.

**Buybacks [E5-08, E2-51]:** condition (1) ample funds — always. Condition (2) discount
— the only repurchases in four years were 250,000 shares in Q4 FY2026 at ≈$19.20 average
($4.8M), below every value reading in this file — passes at the price. **But the
refusal-tell [E2-51] fires across the window:** zero buybacks FY2022-FY2025 while the
stock traded at trough multiples and $196M of dividends went out — a CEO holding ~8.4%
(mostly from compensation grants, per the DFAN14A; his family collects "more than $6
million" from the special, same source) consistently preferring taxed distributions to
per-share compounding at a discount "reveals more than he knows of his motivations."
Stated with [E4-13]'s humility clause: management knows the business better than I do,
and the melt makes shrinking the equity base defensible. The flag binds position size —
moot here.

**Comp [E2-01 context]:** Kathwari FY2025 total $3.83M (salary $1.15M, stock $1.52M,
incentive $1.04M — DEF 14A Summary Compensation Table); moderate against $51.6M of net
income; CFO $0.69M. Not a comp-extraction story. Say-on-pay passed 19.2M to 1.2M.

**THE GUARDRAIL:** [x] nothing here promotes the name (Q2 is OUT and stays OUT — a
strong record cannot repair it [E2-37, E2-38, E3-39]); [x] key-person dependence was
recorded at Q2 as a moat defect [E4-23], not here as a compliment; [x] no
excisable-cancer case is argued — on the contest's own terms the manager IS the plan
(both sides': the incumbent's plan is himself; the activist's plan is replacing him),
which is the unbuyable configuration [E2-35, E2-36].

- **Q3 FOR-THE-RECORD READ: no honesty disqualifier found; the gate would still not
  clear today** — succession vacuum at 82 in a daily-execution business, plus the fired
  board-conduct flag, are exactly the "how much damage before you can react" facts the
  gate exists for. **UNRESEARCHED, and the documents are named and dated:** the 2026
  DEF 14A (~Sept/Oct 2026 — board slate, any successor disclosure, the sixth-seat
  explanation), any Item 5.02 8-K, and the 2026 annual meeting outcome (~Nov 2026).
  *A pass here would be the absence of found disqualifiers, never a clearance [E5-17] —
  and IN never promotes; Q2 OUT stands regardless.*

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings — **COMPUTATION — NOT A CLEARANCE** [E2-23]
Convention applied: multi-year mean of (OCF − SBC) − (c); OCF nets the working-capital
increment (constraint 3) from one audited line — and here that matters: customer-deposit
swings (−$43.3M FY2023, −$12.3M FY2026) are the cycle passing through the order book.

Per year ($M; FY2022-25 filed 10-K figures; FY2026 OCF/capex filed in the PR, FY2026 SBC
≈1.2 and D&A ≈15.3 are 9-month 10-Q figures annualized ×4/3 — **estimates, labelled,
pending the FY2026 10-K**):

| FY | OCF | SBC | D&A | capex | OE (c=D&A) | OE (c=capex) |
|---|---|---|---|---|---|---|
| 2022 | 69.4 | 1.1 | 16.0 | 13.4 | 52.3 | 54.9 |
| 2023 | 100.7 | 1.3 | 15.6 | 13.9 | 83.8 | 85.5 |
| 2024 | 80.2 | 1.5 | 16.0 | 9.6 | 62.7 | 69.1 |
| 2025 | 61.7 | 1.5 | 15.5 | 11.3 | 44.7 | 48.9 |
| 2026 | 52.5 | 1.2e | 15.3e | 11.0 | 36.0 | 40.3 |

- **Short-window mean (3-yr, FY2024-26): $47.8M .. $52.8M**
- **Long-window mean (5-yr, FY2022-26, the corpus default [E2-42]): $55.9M .. $59.7M**
- **Spread, conservative end: +17.0%** (5-yr above 3-yr) — **material, and it is a Q4
  finding [E5-11]:** the distorted years are named. FY2022-23 delivered the FY2021-22
  written-order boom (net sales $817.8M/$791.4M against $579.5M today; the FY2023 OCF
  carries the boom's backlog conversion; the −$43.3M deposit unwind shows the tide going
  out). **[E4-41] governs: normalize DOWN for luck** — the 5-yr mean is flattered by a
  demand regime that has ended, and the honest weight sits at the 3-yr mean or below.
- **The bottom boundary [E5-34]:** FY2026 itself — the only year fully clear of boom
  backlog — less the one-time $5.0M IEEPA tariff refund inside FY2026 OCF: **OE ≈
  $31M-$35M.** Written orders were still falling through it (retail −6.1%, wholesale
  −11.2%; Q4 worse at −10.8%/−11.9%), so even this may not be the floor of the melt.
- Honest context the other way (recorded per [E4-26] symmetry): pre-boom owner earnings
  were $22-36M (FY2018-20 same convention), so two decades of revenue decline have NOT
  shrunk the profit pool — the margin rebuild (GM 54.2% → 61.2% since FY2018) roughly
  offset the volume loss. The bear case is about the runway of that trick, not the past.
- **Maintenance capex — the disclosed judgment:** capital-light (capex 1.9% of FY2026
  sales), the [E5-20] exception is NOT invoked (no filing statement that depreciation
  understates renewal; no railroad-class assets). **But the D&A end is taken as the
  operative (c), not the capex end** — actual capex has run BELOW D&A for five straight
  years while the design-center fleet ages, and the live activist case says
  under-investment outright (advertising "below every year from 2006 through 2021,"
  five-year capex $59M — DFAN14A, consistent with the filed $9.6-13.9M/yr series and
  advertising of $16.4-17.7M/yr FY2023-25). A shrinking store fleet spending below
  depreciation is consistent with harvesting, and (c) for MAINTAINING competitive
  position is judged at D&A ≈ $15.5M/yr, with the band displayed. Both windows shown;
  the verdict below does not change anywhere in the band.
- Stock compensation subtracted in full [E5-06] (~$1.2-1.5M/yr; option-value uplift
  [E3-70] immaterial at this scale).
- No look-through increment [E3-04]: no equity-method investees found.

### Great, good, or gruesome? [E4-20]
**[x] GOOD, on the capital actually employed — with a negative reinvestment runway.**
Trough after-tax operating return on ex-cash equity ≈12% (judgment, from filed figures);
full-cycle ROE mean ~13% carrying a third of equity in cash; capex below D&A; the
business consumes no capital. It fails "great" because the deposit base cannot take new
money at the old rate — there is nowhere inside the shrinking unit base to add capital,
which is why the cash leaves as dividends. Not gruesome: it eats nothing.

### Staying power — all three [E5-11]
1. **Large and reliable stream:** profitable every year since the 1993 IPO (company
   statement, 2026-08-19 release; the filed series FY2018-26 confirms positive NI
   through COVID's $8.9M trough). Cyclical, never near a loss. Pass.
2. **Massive liquid assets:** $187.5M cash+investments at 2026-06-30 against **zero
   debt** (10-Q: no bank borrowings; facility undrawn; fixed-charge covenant springs
   only below $14M availability). ≈32% of the cum-dividend market cap. Pass — **eroding
   by declared policy:** post-special ≈$111M.
3. **No significant near-term cash requirements:** no debt maturities, no pension,
   leases $124.4M total (wtd 5.6 yrs, 6.0% discount, ~$33M/yr — ordinary covenant-free
   rent [E3-52], paid from operations). The one large declared outflow is the $76M
   special plus the $39M/yr regular dividend — discretionary in law, reputationally
   sticky in a contest. Pass, with the [E2-60] restricted-earnings note: **at
   bottom-boundary OE ($31-35M) the regular dividend alone ($39.3M) exceeds owner
   earnings** — FY2027's payout program spends the balance sheet, disclosed and
   deliberate. Coverage test [E2-54]: interest ≈$0.2M vs OCF $52.5M — trivial.

### The specific ways THIS business dies [E2-27, E3-24] — the iron prescription applied
1. **The melt (the slow death, and the bear's own case — stated at full strength):**
   units, designers (−30-40% in ~5 years, CEO's words), centers, and share have declined
   for two decades ($1.0B FY2007 → $579.5M FY2026, ≈−2.9%/yr nominal, worse in units)
   while the growth in the premium category went to Arhaus and RH. The margin offset is
   finite: SG&A is 53.3% of sales and fell only 0.4% in a −5.7% sales year (fixed-cost
   floor), and the FY2025 10-K already files manufacturing inefficiencies from
   underutilization at $615M of sales. Below roughly $500M of sales the eleven-plant,
   141-center structure deleverages faster than price can offset; the shrink-to-margin
   lever that saved the last two decades exhausts. **Likelihood: LIKELY** — it is the
   filed trend, not a scenario. This is the named death.
2. **Cyclical deepening (the fast wound):** FY2026 written orders −6.1% retail / −11.2%
   wholesale, Q4 worse. A further −10% delivered year (~$521M): ≈−$35M gross profit at
   61% GM against maybe $10-12M of SG&A relief → operating income ≈$15-20M, OCF perhaps
   $25-35M against a $39M regular dividend. Solvency untouched (cash covers years; "a
   year like that would not distress us" in [E3-24]'s solvency sense) — the wound is to
   valuation and the dividend. **Likelihood: a real possibility** (the order book is
   already printing it).
3. **The Kathwari transition (the event death):** contract ends 2027-06-30; age 82; no
   disclosed successor; a live contest that may force an abrupt outcome either way
   (entrenchment hardened, or the founder-figure ejected and the designer network — the
   actual asset — churning under new owners' urgency). In a daily-execution retailer the
   transition is the single point where "how much damage before you can react" is
   maximal. Not quantifiable from filed figures; **likelihood of the seat turning over
   inside the window: near-certain; of a value-destructive transition: a real
   possibility.**
4. **Cash-pile dissipation in defense (the governance death):** $76M (~15% of the
   ex-div cap) leaves 2026-09-17, declared mid-contest; a repeat at FY2027's pace with
   OE at $31-53M halves the remaining pile within ~2 years and erodes staying-power leg
   (2). **Likelihood: the first $76M is certain (declared); full dissipation a
   low-level possibility.**
- **Q4 FOR-THE-RECORD READ: survival as a solvent company is not in doubt on the filed
  balance sheet (deaths 2-4 wound value, not solvency); the going-concern question is
  the melt (death 1), which is a Q2 finding restated — the business survives; the
  franchise erodes.** Were this gate live it would read IN on survival with the melt
  carried as the central valuation fact.

---
## Q5 — FOR THE RECORD — **COMPUTATION — NOT A CLEARANCE**
*(Q1-Q4 did not close IN; operator rule 3 header on everything below; no entry language.)*

**THE FLOOR [E4-28] — "that's the figure we quit on."**
Honest pre-tax expectancy at $23.47 (cum) / ≈$20.47 (ex the declared special):

**1. THE YIELD** (owner earnings ÷ market cap · sovereign **5.19%**):
| OE basis | on $592M (cum) | on $516M (ex-special) |
|---|---|---|
| Bottom boundary $31-35M [E5-34, E4-41] | 5.2% - 6.0% | 6.0% - 6.8% |
| 3-yr mean $47.8-52.8M | 8.1% - 8.9% | 9.3% - 10.2% |
| 5-yr mean $55.9-59.7M (boom-flattered) | 9.4% - 10.1% | 10.8% - 11.6% |

**2. WHAT THE PRICE ALREADY ASSUMES:** ex-special operating value ≈ $405M ($516M less
≈$111M post-special net cash). Against bottom-boundary OE ($31-35M) that is ≈12x, i.e.
the price assumes the FY2026 trough persists with a melt of roughly 2.5-3%/yr forever
(31-35 ÷ (5.19% + ~2.75%) ≈ $390-440M). Against the 3-yr mean held flat it assumes
almost nothing (the operating business at ~8x). What the business has actually done:
revenue −29% over four years; written orders still falling; OE bottom ≈ pre-boom FY2019
level. The price is not stupid; it is pricing the melt.

**3. WHAT YOU ARE PAID:** +0.8 to +1.6 points over the sovereign at the bottom boundary
(ex basis) · +4.1 to +5.0 points at the 3-yr mean · +5.6 to +6.4 points at the
boom-flattered 5-yr mean. **The answer depends entirely on which OE you believe — that
spread IS the finding [E4-25].**

**THE FLOOR VERDICT, stated plainly as tasked:** at the bottom boundary — the base
[E5-34] says to buy against — the expectancy is **6-7% ex-dividend plus honest growth,
and honest near-term growth is negative** (the order book). Clearing 10% from here
requires writing a housing-recovery-plus-clean-succession belief into the growth term —
[E4-35]'s burden-of-proof against a two-decade down unit series, refused per [E4-26].
**The floor does not clear at the bottom boundary. It clears only on the boom-inclusive
5-yr mean measured ex-dividend — a mean [E4-41] instructs this run not to trust.** Had
the gates been open, the honest verdict here would be the [E4-25]/[E5-34] middle box:
the price sits inside a range whose width is the unresolved cyclical-vs-secular
question — **no useful conclusion; move on.** (Bar: screamer test only; no margin
stacked. **Windage count: one** — the melt-rate term in "what the price assumes,"
justified in writing by the filed unit series; the bottom-boundary base and the
tariff-refund removal are [E5-34]'s and [E4-41]'s own required moves, not extra
windage.)

**The value, as a round-number range [E4-01], for the record only:** operating value
roughly **$390-440M** on the melting bottom boundary … **$920-1,150M** on flat mean OE
at the bare sovereign; plus ~$111M net cash; against $516M ex-div at the quote. The
range is too wide to conclude on, and that is the conclusion [E4-25].

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists; these are pre-committed yardsticks for the WATCH LIST, set prior
to any act [E1-02]. Alert thresholds are LISTED here only — `tools/alerts.json` not
edited.)*

**Q2 REOPEN CONDITIONS (the only route back to entry) — BOTH required:**
1. **Evidence, not price:** the melt measurably stopping — two consecutive fiscal years
   of rising written orders AND stable-or-rising design-center and designer counts
   (FY2027/FY2028 10-Ks and PRs), PLUS a resolved, named CEO succession (2026 DEF 14A /
   Item 5.02 8-K / annual-meeting outcome). Unit stabilization would falsify this run's
   direction finding, which is the load-bearing member of the Q2 OUT.
2. **Price [E4-28]:** the bottom boundary must pay the floor with zero growth credited:
   OE $31-35M × 10 ≈ $310-350M + ~$111M net cash ≈ $421-464M ≈ **roughly $17-18/share
   ex-special-dividend** (≈$20-21 cum, until 2026-09-02 only). Below that, the
   worst-case base alone pays ~10% and the housing recovery rides free. At $23.47 cum
   (≈$20.47 ex) the quote sits ~15-20% above the band top.

**Watch-list metrics and thresholds (review triggers, not auto-executions):**
- **Melt rate:** written orders (both segments) each quarterly release; two consecutive
  quarters of retail orders positive year-over-year = re-read.
- **Margin floor:** consolidated GM below 58% or adjusted operating margin below 5% in
  any full year = the shrink-to-margin lever failing (Q4 death 1 accelerating).
- **Dividend action:** any cut to the $0.39 regular = the [E2-60] arithmetic biting —
  re-read immediately (it is also the event that would re-rate the stock toward the
  entry band).
- **Succession event:** any Item 5.02 8-K naming a successor, a new operating chief, or
  a director departure; the 2026 DEF 14A (~Sept/Oct); the annual-meeting result (~Nov
  2026). A credible operator-successor installed WITH Kathwari's designer network intact
  is the bull path this file cannot price today.
- **Contest economics:** further specials or a large tender mid-contest (staying-power
  leg 2); any poison pill or bylaw amendment (board-conduct flag hardening).
- **Price alert (list only):** ETD below **$18.00 ex-dividend basis** → re-run both
  reopen conditions. FY2026 10-K filing (~days away) → refresh FY2026 SBC/D&A estimates
  and this file's arithmetic.
- **Next catalyst dates:** ex-special ~2026-09-02 · special paid 2026-09-17 · FY2026
  10-K ~early Sept · DEF 14A ~late Sept/Oct · FY2027 Q1 earnings ~late Oct · annual
  meeting ~Nov 2026. Monthly housing data: context only, never a trigger [E3-32].

**Sizing note, as tasked (moot at entry, recorded for the record):** the earmarked
account is TAXABLE, and [E2-46]/[E3-64] make it prefer never-switch compounders taxed
once at the end. ETD is the opposite shape even on its own bull case: the return arrives
substantially as ordinary-income dividends every year (7.6% regular-dividend yield on
the ex price, plus specials), and the thesis (cyclical recovery + succession + contest)
is a re-rating trade with a sell discipline, not a hold-forever name. **ETD does not
qualify as a taxable-account never-switch name even if it graduates on price.**

- **VERDICT: [x] IN** — the question "what would prove me wrong" is answered with
  pre-committed, dated, document-named conditions on both sides.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (Q2 OUT); Q3-Q5 written
      for the record only, headed COMPUTATION — NOT A CLEARANCE per operator rule 3
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q1's two
      overhangs are carried to Q2/Q4 as findings, not caveats on the verdict)
- [x] Every UNRESEARCHED item names the artifact and where it lives: FY2026 10-K (EDGAR,
      ~days away — refresh SBC/D&A estimates and re-check all FY2026 figures against the
      audited statements); 2026 DEF 14A (EDGAR, ~Sept/Oct — succession, board seat six);
      WSM/Wayfair-class competitor rows (EDGAR, work order in the row file)
- [x] Q2 OUT states what specifically fails and on which filed evidence (substitution at
      the margin: the subject's own revenue/unit series against the row; direction; the
      Mayo defect)
- [x] Step 0: filing read with accession numbers; FY2026 10-K absence stated and the
      substitute documents named; OCF $61,696K cross-checked three ways; net sales
      cross-checked twice
- [x] Owner earnings on multi-year means; both windows shown (spread +17.0%, material,
      distorted years named); capex band displayed; (c) a disclosed judgment at the D&A
      end with the reason written; SBC subtracted in full; FY2026 SBC/D&A labelled as
      estimates pending the 10-K
- [x] Competitor row: 5 of ~6-8 peers, filing-sourced with accessions, committed as a
      separate research file; shortfall recorded as a work order (moat class was decided
      on the subject's own filed series plus five rows — not PROVISIONAL)
- [x] Sovereign for the earnings currency (USD) from the standing issuing-authority
      source (FRED DGS30), dated 2026-08-27; tools/sources.py USD failure recorded
- [x] Value stated as round-number ranges; the too-wide range identified as itself the
      conclusion [E4-25]
- [x] One bar (screamer, for the record); windage count: one, justified in writing
- [x] Prices dated; aggregator used for the live quote only and flagged; cum/ex
      dividend basis stated everywhere it matters
- [x] The market-beating claim not made anywhere; judgments carry ledger ids or are
      labelled judgments/estimates
- [ ] Run committed to git — pending

## REGISTER
- Verdict: **[x] OUT (about the business, at Q2 — for entry).** No position held; no
  hold read required. Q3 for the record: UNRESEARCHED (documents named, all arriving
  Sept-Nov 2026); Q4 for the record: survivable, melting; Q5 computation: floor fails at
  the bottom boundary.
- One line: **the best margins in its industry, no debt, honest books and no guidance
  culture — attached to a two-decade unit melt, an 82-year-old sole author with no
  disclosed successor, a board that shrank quietly during a proxy fight, and a $76M
  special dividend walking out the door mid-contest; a real business, not a franchise,
  and the price already knows it.**
- **Work orders (UNRESEARCHED):** (1) FY2026 10-K — EDGAR, imminent (audited FY2026
  D&A/SBC; re-run the OE table); (2) 2026 DEF 14A — EDGAR ~Sept/Oct (succession, the
  sixth seat, beneficial ownership refresh); (3) 2026 annual-meeting 8-K — EDGAR ~Nov
  (contest outcome); (4) WSM row — EDGAR, ordinary retrieval.
- **The single biggest concern:** the succession-times-contest window — a
  daily-execution retailer whose one operator for 38 years is 82 with a contract ending
  2027-06-30, no disclosed successor, a four-independent board with no retail operating
  experience, and an activist fight whose most likely outcomes both run the transition
  under stress — while the balance-sheet cushion that would buy the transition time is
  being paid out at $76M a check to win the vote.

*This file is a judgment by the AI running the framework; underlying facts are the
FY2025 10-K (acc. 0001437749-25-027594), the FY2026 Q4 press release (8-K acc.
0001437749-26-024880), the Q3 FY2026 10-Q (acc. 0001437749-26-013892), the 2025 DEF 14A
(acc. 0001104659-25-093869), the contest filings named in the header, five peer 10-Ks
cited in the committed row file, FRED DGS30, and one flagged live quote. Where a number
is a judgment or estimate — the (c) choice, the FY2026 D&A/SBC annualization, the melt
rate, the operating-equity return, the entry band — it is labelled as one.*
