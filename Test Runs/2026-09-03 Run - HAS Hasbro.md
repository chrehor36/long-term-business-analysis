# Company Run — Hasbro, Inc. (HAS) — 2026-09-03
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
- rate **5.27%** · date **2026-09-02** · source: **US Treasury daily par yield curve (issuing
  authority)**, via `tools/sources.py`
- FX: not needed — US filer, USD quote, majority-USD earnings (US revenue $3,010.1M of
  $4,701.3M FY2025, per the 10-K geographic note; non-US earnings left at the USD sovereign,
  which is the conservative direction at current rate ranks)

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- documents · dates · accession nos.:
  - **10-K FY2025** (fifty-two weeks ended 2025-12-28), filed 2026-02-25, **accession
    0000046080-26-000011** — MD&A, segment note, cash flow incl. detail lines, debt note,
    lease note, goodwill note read
  - **10-K FY2023** (FYE 2023-12-31), filed 2024-02-28, **accession 0000046080-24-000034**
    — read FIRST for the business-combination/divestiture history, per the
    `acquisition_flag()` prompt (34% of cap; operator rule 8: a prompt to read, never a score)
  - **10-Q Q2-2026** (period 2026-06-28), filed 2026-07-30, **accession 0000046080-26-000050**
    — cover share count and H1-2026 trajectory
  - **DEF 14A**, filed 2026-04-17, accession 0001193125-26-160426
- figure cross-checked against the filed statement: **FY2025 operating cash flow $893.2M**
  — run.py's XBRL pull matches the filed Consolidated Statements of Cash Flows to the
  decimal. **The same check FAILED on capex**: run.py read $63.3M (PP&E line only) and
  missed the separate filed line "Additions to software development" $135.0M — see TOOL
  DEFECT at the foot of this file.

**Price and share count:**
- price **$93.00**, 2026-09-03, aggregator — live quote only, flagged as such
- shares **141,044,467** hand-read off the 10-Q cover (single class, $0.50 par), verified by
  `cover_shares.py` — run.py's 140.2M is a weighted-average EPS denominator, not a count
- **market cap $13,117M**
- Screen-row reproduction: the queue's spread **40.9% reproduces exactly** as
  (634−450)/450 from the two screen windows; its 3.37% yield is the 5-yr capex-end OE
  (~$450M) on the screen-date cap. Both screen windows carry the capex defect below, so the
  hand-built series in Q4 governs.

**THE PERIMETER — the acquisition_flag finding, established before any question was scored.**
The filed history contains an entertainment company the cap no longer prices:
- **eOne bought for ~$4.6bn, closed 2019-12-30**, funded in part by **$2.4bn of senior notes
  issued November 2019** (2022/2024/2026/2029 tranches — the debt note in the FY2025 10-K
  still names the eOne acquisition as their origin).
- **Dismembered:** eOne Music sold Q3 2021 ($378.5M proceeds per the FY2021 investing line;
  $108.8M goodwill impairment); **eOne Film and TV sold to Lionsgate 2023-12-27 for $375.0M
  cash** plus assumed production loans (FY2023 10-K, Note 3). FY2023 charges: **$1,278.2M of
  non-cash goodwill/asset impairments plus a $539.0M loss on disposal**; residual
  loss-on-disposal adjustments of $37.4M (2024) and $25.0M (2025) are still trailing through.
- **Perimeter consequence for the owner-earnings window:** FY2021–2023 cash flows contain
  the entertainment company — program spend net of amortization dragged OCF by ~$69M (2021)
  and ~$212M (2022), and FY2023 contains the disposal year. Content spend is now down "over
  90%" by the filer's own Item 1. **A five-year mean averages two different companies; the
  window treatment in Q4 refuses the blended mean and says so** (same rule as the queue's
  ACMR/ALKT class).
- And the pattern repeated inside the new perimeter: **FY2025 took a further $1,021.9M
  goodwill impairment in Consumer Products** (Q2-2025, tariff-triggered interim test) — the
  second billion-dollar impairment in three fiscal years.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **Three different businesses under
  one cap.** (1) **Wizards of the Coast** prints trading cards: it designs a Magic set,
  prints cardboard at commodity cost, and sells it at collectible prices to a 30-year-old
  player/collector base that buys every release; D&D sells rulebooks and a digital toolset
  (D&D Beyond). It also licenses Hasbro game IP to outside studios (Monopoly Go! royalties
  $168.0M FY2025; Baldur's Gate 3) — royalty income on other people's capital. FY2025 segment
  revenue $2,186.9M, operating profit $1,006.8M, **46.0% margin**. (2) **Consumer Products**
  designs toys, has them made by third parties in China/Vietnam/India, and sells through
  Walmart/Amazon/Target at low single-digit margins (4.5% in FY2024, ~3% ex-impairment/
  ex-tariff FY2025) — plus an out-licensing royalty stream that Item 1 concedes carries the
  segment's profit. About a third of the toy shelf is OTHER people's brands (Marvel, Star
  Wars) rented from Disney for a royalty. (3) A residual **Entertainment** stub (Peppa Pig /
  Family Brands content, $76.8M revenue, ~$0 profit).
- The scarce input this business controls: **the Magic: The Gathering and D&D player bases
  and card ecosystems** (a 30-year installed base of players, collections, game stores and
  tournament infrastructure that a new entrant cannot print), plus the classic-game
  trademarks (Monopoly, Play-Doh, Transformers, Nerf, Peppa Pig). It does NOT control the
  scarce input of its partner-brand toy revenue — Disney does — nor the shelf, which
  Walmart/Amazon control (top five customers 35% of revenue).
- Will the fundamentals look broadly the same in ten years? For WotC tabletop and the
  licensing toll-stream, plausibly yes — Magic is 30 years old, Monopoly 90. For Consumer
  Products, the filer itself says the category is shortening product life cycles and
  competing with screens. The self-published AAA video-game push (four studios, EXODUS and
  WARLOCK due 2027, $385.6M of capitalized development) is a hits business Hasbro has NOT
  proven it can run — that piece is not "simple and stable in character," and it is where
  the incremental capital is going. Understood, with that stated.
- **VERDICT: [x] IN** — the money-making is legible from the filing: a card/games franchise
  claim, a royalty stream, and a commodity toy business. The verdict is IN on
  understanding; what the blend is WORTH as a franchise is Q2's question, judged separately
  per segment **[E5-37]**.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Hasbro is two franchise claims and a toy company, judged separately [E5-37], from the
segment tables — and then the blend is judged, because the blend is what $13.1bn buys.**

**THE SEGMENT-PROFIT MIX, THE FACT THAT DECIDES THE SHAPE OF THIS QUESTION** (filed segment
tables, FY2023-FY2025 10-Ks):

| $M | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| WotC revenue | 1,286.6 | 1,325.1 | 1,457.6 | 1,511.3 | 2,186.9 |
| — Tabletop | 950.6 | 1,067.0 | 1,072.5 | 1,039.6 | 1,686.6 |
| — Digital & Licensed | 336.0 | 258.1 | 385.1 | 471.7 | 500.3 |
| WotC operating profit | 547.0* | 538.3* | 525.7 | 632.0 | 1,006.8 |
| WotC margin | 42.5% | 40.6% | 36.1% | 41.8% | 46.0% |
| Consumer Products revenue | 3,981.6 | 3,572.5 | 2,886.4 | 2,543.9 | 2,437.6 |
| CP operating profit | 401.4 | 217.3 | (64.7) | 115.3 | (942.6); **+79.3 ex-impairment** |
| CP margin | 10.1% | 6.1% | (2.2)% | 4.5% | ~3.3% ex-impairment |

*\*2021/2022 WotC OP derived by arithmetic from the filed segment totals (FY2023 10-K
segment note prints CP, Entertainment, Corporate and the total; WotC is the remainder).*

**WotC is ~92% (FY2024) and ~97% (FY2025, ex-impairment) of segment operating profit, and
was >100% in FY2023 when the rest lost money. The brief's stated prior — the QCOM/QTL
shape, franchise as a minority of what you buy — is REFUTED by the profit mix [E4-26]:
QTL was 12.6% of revenue with licenses expiring 2027-2031; WotC is 46.5% of revenue,
substantially all of the profit, and expires never. This is a franchise with a toy company
attached.** H1-2026 extends it: WotC +27.1% in Q2, tabletop +31.9% H1, segment OP $270.0M
(+11.6%) in the quarter.

**CLAIM (a) — WIZARDS OF THE COAST: a genuine franchise, class NARROW.**
- Needed or desired [x] — 30 years of Magic, the record 2025 slate absorbed at premium
  prices; D&D the dominant tabletop RPG. Not price-regulated [x]. No close substitute
  [x, scoped]: for the *enfranchised* Magic player/collector the collection, the format
  ecosystem, the store/tournament network and 30 years of secondary-market value do not
  transfer to Pokémon, One Piece or Lorcana — the substitution cost is the abandoned
  collection. For the *marginal new* player the substitutes are real and well-capitalized;
  that is the boundary of the moat, and the class is NARROW, not WIDE.
- **[E2-44] both halves, answered from filed revenue, not forums:** Half 1 (price with flat
  demand): tabletop dollars sat FLAT for three years (1,067.0 → 1,072.5 → 1,039.6,
  2022-2024) across annual price increases and premium collector products — dollars held
  by pricing is the filed fact; **no unit series exists to separate price from volume
  [E4-55], and unlike ANF, Hasbro does not even confess the absence — dollar revenue
  flattered by pricing is exactly how a shrinking physical franchise hides, and this filer
  has removed the reader's ability to check.** Half 2 (grow dollar volume on minor
  capital): FY2025 revenue +$675.6M on **$12.9M of segment capex** — emphatic yes; this is
  the two-characteristic test's cleanest pass in nineteen runs.
- **The wrinkle inside the record year: the growth is partly rented.** The 2025-26 wave is
  Universes Beyond — Final Fantasy (Square Enix), Spider-Man (Disney), Avatar: The Last
  Airbender (Paramount) — *"for which the Company is obligated to pay a royalty"* (MD&A);
  royalty expense +$84.7M (+30%) in the record year. Pricing power is demonstrably real;
  a growing slice of it is shared upstream with other people's IP, and the supply of
  marquee crossover universes is finite. D&D revenue DECLINED in 2025 (named in MD&A).
- **[E4-04]:** the set treadmill is product cadence, not moat replacement — a weak set year
  narrows the moat, does not destroy it (the 2022-2024 plateau demonstrates exactly this:
  three flat years and the franchise then printed its best year ever). Spending defends
  the SAME advantage (the game, the base). Not the excluded class. **Success does not
  depend on a great manager** — WotC earned $525-547M through three CEOs and a proxy
  fight. **But the AAA self-publishing bet DOES depend on sustained hit-making skill the
  company has not demonstrated — recorded here as the moat defect [E4-23]:** four studios,
  $385.6M capitalized, first titles 2027, in the business where TTWO — owner of the
  biggest franchise in interactive entertainment — just ran goodwill impairments of
  $2,342.1M and $3,545.2M in consecutive fiscal years.
- Primary moat metric, filing-sourced, and its trend: **WotC segment operating margin:
  42.5 → 40.6 → 36.1 → 41.8 → 46.0%** — narrowed three years, then widened two years
  running [E4-32]; direction currently WIDENING, on a licensed-IP wave.

**CLAIM (b) — THE LICENSED-BRANDS ENTANGLEMENT: Disney's franchise, rented.** Marvel and
Star Wars are named in the 10-K as owned by Disney; the agreement was recently extended
(Item 1); royalties carry advances and **minimum guarantees** (Item 1, "Royalties and
Participations"). The filed precedent for how this ends: **the Disney Princess and Frozen
licenses expired December 2022** (FY2023 10-K names the expiration driving Partner Brands
−35%) — and the FY2026 Harry Potter licensing win (10-Q, Warner Bros. Discovery, 2027
start) shows the same door swinging the other way. A rented brand is a revenue stream, not
a moat; the licensor holds the pricing power over the toymaker. **Not a franchise claim
Hasbro owns.**

**CLAIM (c) — CONSUMER PRODUCTS: a commodity business in structural decline [E2-58].**
Revenue −38.8% in four years (3,981.6 → 2,437.6) with margins of 10.1 → ~3.3%; a fresh
$1,021.9M goodwill impairment (Q2-2025) on the filer's own reduced forecasts; $44.9M of
tariff costs absorbed with advertising CUT $30.3M to offset — **[E5-23] fires: the moat
budget paid the tariff bill**; top five customers 35% of revenue, Amazon 11% + Walmart 9%;
private label named as competition in Item 1; JAKK's FY2025 10-K files the industry
structure in one line: *"the toy industry has no significant barriers to entry."* The
[E2-53] dominance test fails structurally: JAKK calls Hasbro one of *"the toy industry's
most dominant companies"* — and the dominant position earns 3-4% margins. In toys,
position does NOT set economics; the category does.

**THE COMPETITOR ROW — required [E3-28].** Same metric (FY2025 operating profit ÷
unleveraged net tangible operating assets, identical formula; operating margin beside it),
same window, filing-sourced. Research: `_research 2026-09-03 HAS/competitor_row_toys.md`,
`competitor_row_games_lego.md`, `competitor_row_tcg.md`.

| Company | FY2025 op ÷ NTOA | FY2025 op margin | Revenue path 2021→2025 | source |
|---|---|---|---|---|
| **HAS (subject)** | **83.6% ex-imp** (0.9% rep.; NTOA $1,235.0M) | 22.0% ex-imp (0.2% rep.) | 6,420→4,701 (perimeter) | 10-K 0000046080-26-000011 |
| Mattel | 33.9% (NTOA $1,612.8M) | 10.2% | 5,458→5,348 flat | 10-K 0001628280-26-010716 |
| JAKKS Pacific | 8.8% (NTOA $161.8M) | 2.5% | 621→571 | 10-K 0001185185-26-000723 |
| Funko | −45.6% (NTOA $99.9M) | −5.0% | 1,029→908 | 10-K 0001704711-26-000020 |
| LEGO (rung 3, private) | n/c from published AR | **26.4%** | DKK 55,294→83,530 (+51%) | AR 2025 |
| Electronic Arts (games econ.) | n/c (different structure) | 15.4% (FY Mar-2026) | 7,562→7,531 (3yr) | 10-K 0001628280-26-033617 |
| Take-Two (games econ.) | n/c | −1.5% (−67.1%, −78.0% prior) | 5,350→6,656 (3yr) | 10-K 0001628280-26-037434 |

**THE TCG ATTACKERS — rung-3/4 evidence, because none files with the SEC** (all from
`competitor_row_tcg.md`; Bandai Namco TSE 7832 English disclosures; obstacles named):
- **Bandai Namco** (One Piece Card Game, Dragon Ball, Union Arena): Toys and Hobby segment
  net sales **¥596,933M (~$4.0bn) FY2025.3, +17.1% — segment operating profit ¥102,202M at
  a 17.1% margin** (vs WotC's 46.0%); One Piece IP sales groupwide ¥112.1bn → ¥139.5bn
  (+24%); its own FY2026.3 presentation: *"Continued strong popularity of ONE PIECE Card
  Game both around the world."* One Piece Japan Toys&Hobby sales plateau in FY2026.3
  (¥94.2bn → ¥95.1bn) — the attacker's own wave crested.
- **The category is exploding under everyone**: Bandai's Fact Book puts the **Japan**
  physical card market at **¥59.0bn (FY2021) → ¥319.7bn (FY2025) — 5.4x in four years** —
  with Bandai's own share only 16.3%. Scope stated: this series is Japan-only and
  Pokémon/One Piece-driven, while Magic skews Western; it cannot prove a global share
  split. What it does establish: the attackers' category boomed through exactly the years
  MTG tabletop dollars sat flat (2022-2024), so the plateau was NOT an industry tide —
  which sharpens, without settling, the set-fatigue question [E4-55 absence noted above].
- **Ravensburger (Disney Lorcana)**: private German group; publishes an annual results
  press release, not financial statements. **The Pokémon Company**: private Japanese KK
  publishing no financial statements; **no named per-affiliate figure was found** in the
  Nintendo English investor documents checked (sweep recorded in `competitor_row_tcg.md`,
  worded per the absence-claim rule). Neither absence is load-bearing: the moat judgment
  below does not lean on either attacker's unit economics.

- Peers named: **9-10 of the industry's real competitors across the three legs** (toys: MAT,
  JAKK, FNKO, LEGO; games economics: EA, TTWO; TCG attackers: Bandai Namco, Ravensburger/
  Lorcana, The Pokémon Company; plus retail private label, named but unrowable). Buffett
  says eight; this row takes as many as the three sub-industries actually have with
  obtainable documents, and says which lack them.
- **The row's limit [E3-61] stated:** identical structures produce opposite outcomes — the
  row shows position (HAS's blended tangible returns are 1st of the four SEC toy filers,
  by 2.5x, BECAUSE of WotC), it cannot show whether Wizards' set-cadence conduct is
  Kellogg-demented or disciplined. The 2023 filing said "fewer, bigger" sets; the 2025-26
  slate is more and bigger. Conduct is the open question, and the corpus says no model
  predicts it.
- **The attacker's test [E2-45], both legs:** In TOYS the attacker record is Lego's, and it
  is devastating to the category's moat claim: revenue +14%/yr for six years to DKK 83.5bn
  at a 26.4% margin, *"significantly outperformed the toy industry, which grew with 7
  percent"* (AR 2025) — a private attacker took the industry while Hasbro's CP shrank 39%.
  In TCGs the attack on WotC is live and funded by the best IP owners on earth — Disney
  licensed Lorcana (Ravensburger, 2023), Bandai launched One Piece (2022) — and the filed
  subject-side evidence is that MTG's dollars went flat for exactly those three years,
  then took the crown back by RENTING the attackers' class of IP into its own engine
  (Universes Beyond). The attack is real; the counterattack worked; the fight is not over.
- **Untapped pricing power [E3-33]:** largely TAPPED — premium collector products and
  crossover pricing are being exercised now; [E5-28]'s near-monopoly claim holds only
  inside the enfranchised-player niche. No yawn-priced reserve remains.
- Class: [ ] WIDE **[x] NARROW** (the WotC leg; the CP leg is NONE) [ ] NONE
  [ ] PROVISIONAL · Direction: **widening two years running after three narrowing years;
  the widener is currently borrowed IP.**
- **VERDICT: [x] IN — decided by the segment-profit mix.** What $13.1bn buys is, in profit
  terms, overwhelmingly a genuine NARROW franchise (WotC) with a commodity toy business
  attached that neither grows nor eats material capital, plus rented Disney shelf revenue.
  The moat defects are recorded: no unit disclosure [E4-55]; growth leg royalty-entangled;
  set-fatigue exposure on a three-year filed record; the AAA-games key-skill dependence
  [E4-23]; the toy anchor. **IN at NARROW — and Q5 must price a narrow, single-engine
  franchise, not a wide one.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** Record findings; manager quality alone does
not stop the run. **Any ticked → Q3 is a BINARY GATE and no price compensates.**
Case declared, and why: **OVERLAY.** The profit engine is a franchise leg that can tolerate
mismanagement in the [E3-43] sense (WotC earned $525-547M of segment profit straight
through three different CEOs, a proxy fight, a pandemic and the eOne fiasco). The toy leg
is a daily-execution business, but it is ~5% of profit. Book leverage is optically high
(debt $3,281.9M vs equity $565.5M) but that is an artifact of impairments crushing book
equity, not 20:1 asset leverage in the [E3-29] sense; interest is covered ~4.4x out of
cash flow net of capex. No box ticked. **And the record must be read against the hand
dealt [E3-59]: the eOne destruction was authored under prior leadership (CEO Brian Goldner
died October 2021); the current team (Cocks CEO 2022-02, Goetter CFO 2023-05) inherited it
and spent 2022-2025 dismembering it.**

**Honesty — binary, permanent, filings-based [E5-16].** *"understanding about business
mistakes; tolerance for personal misconduct is zero."* Each matter dated to when it became
PUBLIC, so the test stays point-in-time honest: **No personal-misconduct disqualifier found**
in the FY2017-FY2025 10-Ks, the FY2026 proxy, or the litigation notes read. The failures
on record are business failures (eOne, ~$3bn+ destroyed; FY2025 CP impairment $1,021.9M),
which the corpus is "understanding about." A Q3 pass is the absence of found
disqualifiers, not a finding of honesty **[E5-17]**.

**STEP 2 — THE FOUR FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — comp not expensed, fanciful pension assumptions → *"seldom just one cockroach in the kitchen"*
- [ ] unintelligible footnotes
- [ ] trumpeted earnings projections / growth targets
- [ ] serial share issuance
- [x] EBITDA / adjusted-earnings promotion **[E4-29]** *(the fifth flag; 12+ corpus statements)*
- [ ] filed-figure tells: unnaturally smooth reported growth; cash-tax % of pretax falling **[E4-30]**
- For every box ticked, what the filing actually says:
  - **"EBITDA" appears ZERO times in the FY2025 10-K** — the classic form does not fire.
    What fires is the adjusted-earnings variant: the proxy headlines **"adjusted operating
    profit of $1,140 million"** against **GAAP operating profit of $11.1 million** — a
    $1.13bn adjustment gap in one year — and the company's four named non-GAAP measures
    (adjusted OP, adjusted margin, adjusted net earnings, adjusted EPS) are the public face
    of results ("Reported net loss of $2.30 per share; adjusted net earnings of $5.54").
  - **[E4-52] the restructuring-exclusion streak, counted from the filings: NINE consecutive
    years, 2017-2025**, each with one-time/restructuring-class charges carried outside the
    company's own adjusted measures: 2017 tax-reform charge $296.5M · 2018 restructuring
    $89.3M severance + Toys"R"Us + Backflip impairment · 2019 pension settlement $111.0M +
    eOne transaction items · 2020 eOne acquisition/integration $218.6M + $97.9M eOne
    amortization + $8.5M severance · 2021 eOne Music loss $116-118M + eOne amortization ·
    2022 Power Rangers impairment $281.0M + severance $94.1M + transformation-office fees ·
    2023 impairments $1,278.2M + disposal loss $539.0M + Operational Excellence charges ·
    2024 disposal loss $37.4M + environmental $31.1M · 2025 impairment $1,021.9M + disposal
    loss $25.0M. (2016 showed no comparable language in the FY2017 10-K scan; the streak is
    stated as nine, not more.) PEP's record is 12; Hasbro is at nine and running — the
    Operational Excellence program is described as **"ongoing."** **[E2-57] the except-for
    flag fires on the culture**: nine years of "except for," where the recurring lesson —
    what was paid for acquisitions and what the toy business is worth — is exactly what
    keeps being excepted. Charges are real costs **[E5-33]**; the OCF-based owner-earnings
    construction in Q4 keeps the cash ones in.
  - Filed-figure tells: **acquit.** Results are lumpy, not smoothed; cash taxes paid rose
    $92.7M → $196.8M while adjusted profit rose — no [E4-30] tell.
  - Serial issuance: **acquit** — issued 220,286,736 flat two years running; count moves
    only on comp; buybacks resumed 2026.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, *without
undue leverage or accounting gimmickry* — **not** EPS growth. Multi-year series, balance
sheet before income statement.
- Years used, and the series: **Book ROE is unusable here** — impairments took equity from
  $2,936.7M (2020) to $565.5M (2025), so the denominator is the confession, not the capital.
  Per **[E2-43]**, the denominator for an acquisitive filer is **unleveraged net tangible
  operating assets**, goodwill wedge reported separately: NTOA = (assets − cash − ST inv −
  goodwill − intangibles) − (liabilities − debt). **FY2025: (5,552.0 − 776.6 − 105.4 −
  1,256.7 − 456.7) − (4,986.5 − 3,264.9) = $1,235.0M; operating profit ex-impairment
  $1,033.0M → 83.6%** (as reported: 0.9%). FY2024: NTOA $1,074.2M, OP $690.0M → **64.2%**.
  The tangible business earns enormously; **the goodwill wedge is where the money went** —
  ~$4.6bn paid for eOne against ~$760M recovered. **The third denominator [E2-73]** —
  managers judged on underlying assets — favors the operators: WotC runs $1,006.8M of
  segment profit on $12.9M of segment capex and $17.6M of segment D&A.

**The half-owner test [E2-26]:** does this reporting tell me what I would want to know if the
positions were reversed? **Mostly yes at the line level** — every one-time item above is
quantified separately, per line, per year, in the MD&A (the FY2023 and FY2025 bullet lists
are exemplary); segment tables are clean; the tabletop/digital split exists **[E4-55]
partially satisfied**. **Two failures:** (a) no unit, player-count, or set-count series is
published anywhere, so a reader cannot separate Magic price from Magic volume — the exact
[E2-49]-adjacent hole where a shrinking physical franchise could hide; (b) the brand
portfolio categories were re-cut twice in three fiscal years (Franchise/Partner/Portfolio
recast FY2023; Grow/Optimize/Reinvent introduced FY2025, prior periods reclassified), so no
brand-level series survives five years. Both stated with reasons, so the candor read is
"adequate, with the volume question unanswerable from the filings."

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [x] resists any change in current direction — the 2022 proxy contest (Alta Fox) demanding
  a WotC separation was fought and won by the board; the conglomerate structure stands
- [x] projects/acquisitions materialise to soak up available funds — the eOne case entire:
  $4.6bn of debt-and-equity-funded acquisition at the top of the content cycle
- [ ] staff studies — not observable from the filings read
- [x] peer behaviour mindlessly imitated — eOne WAS the imitation ("content is king" era,
  2019); the FY2025 self-published AAA video-game push (four studios, $385.6M capitalized,
  EXODUS/WARLOCK 2027) repeats the shape: entering a hits business where the incumbent
  comps (TTWO) just impaired $5.9bn across two years. Scored, not convicted.

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? **Yes** — $1,378.2M liquid at Q2-2026
  (cash $880.5M + ST investments $497.7M), the Nov-2026 maturity pre-funded.
- (2) repurchases at a **material discount** to conservatively calculated IV? **The H1-2026
  purchases (392,108 shares at $86.1 average; $41.5M) sit at the TOP of this run's
  zero-growth value band (~$70-95) — a discount only under a growth assumption.** Small
  dollars so far; the $1.0bn authorization (Feb 2026) is the thing to watch. **Condition-2
  FLAG, stated with [E4-13]'s humility clause**: management knows the business better than
  we do, and the flag binds position size, never the discount rate.
- **[E3-54] retention cannot run in scored form: five-year retention is NEGATIVE**
  (cumulative net earnings 2021-2025 ≈ −$794M while ~$1.93bn of dividends were paid; equity
  $2,936.7M → $565.5M). Market cap is roughly where it stood at end-2020 (~$13bn). The
  five years returned the dividend and nothing else.
- **Dividend record, established from the filings, not assumed: NO CUT.** $0.68/quarter held
  through 2020-2021 ("In 2020, Hasbro maintained its quarterly dividend rate of $0.68" —
  FY2020 10-K), raised once to $0.70 in 2022, **flat for four years since**. Dividends paid
  $374.5M → $392.5M across five years. In FY2022 the $385.3M payout ran 3.3x that year's
  $115.3M owner earnings — funded from the balance sheet, not borrowings (debt fell) —
  the **[E2-60]** financial-strength dimension bent but did not break, and the eOne
  disposals were partly, in substance, the dividend's funding source.
**THE ONE FLAG THAT OUTWEIGHS THE REST — pay in the loss year.** The 2025 annual incentive
paid the CEO, CFO, WotC head and CLO **200% of target — the plan maximum — in a fiscal year
with a $318.2M reported net loss**, because the pay metric was adjusted operating profit
(goal $892M, "actual" $1,114M) with the $1,021.9M impairment excluded; the toys head was
paid 40%, so the plan does discriminate — it discriminates against everything except the
capital already destroyed. This is [E5-33]'s "don't count this" run through the incentive
system: Berkshire's restructurings were *"borne by shareholders"* every time; Hasbro's are
borne by shareholders and excluded from the bonus math. Two acquittals recorded beside it:
the revenue half of the goal ($4,111M) was set below prior-year actual ($4,135.5M) — the
DG/ULTA rigging *shape* — but the delivered 112%/125% achievements were genuine operating
results, not target-lowering artifacts; and the Committee removed the cost-savings metric
**while it was paying well**, announced with reasons — the candor case of [E2-49], not the
violation.

**[E4-39] the acquisition post-mortem test:** no filed post-mortem of eOne against its
announcement case exists — the $4.6bn → ~$760M history must be assembled by the reader
from five filings, as this run did. The rare-positive tell is absent.

**THE GUARDRAIL — check before writing the verdict.**
- [x] Confirmed: nothing in this Q3 is being used to **promote** the name. A strong manager
      cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**. The current team's
      real operating record (WotC refocus, $800M gross savings, deleveraging, the Nov-2026
      maturity pre-funded) promotes nothing.
- [x] If this business **requires** a great manager, that is recorded at **Q2 as a moat
      defect [E4-23]** — the WotC franchise does not require one (it earned through three
      CEOs); the AAA video-game bet DOES require sustained hit-making skill, recorded at Q2.
- [x] If a great manager is the reason to act: is the franchise **already intact** and the
      damage **excisable**, or is the manager the plan? **[E2-35, E2-36]** The eOne cancer
      WAS excised (sold 2021/2023); what remains is the intact WotC franchise plus a weak
      toy business. The manager is not the plan; no manager-based promotion is made.

- **VERDICT: [x] IN — as an overlay, with two live flags: the buyback condition-2 flag and
  the pay-metric/exclusion-culture flag ([E4-52] nine years). Both bind position size,
  never the discount rate. [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *IN = no disqualifier found. NOT a finding that the managers are honest — "sincerity and
  empathy can easily be faked" **[E5-17]**. IN never promotes.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** *"Using precise numbers is,
in fact, foolish; working with a range of possibilities is the better approach."* Do **not**
pick a window and defend it; carry the spread alongside the capex band.
- Owner earnings by year (OCF − SBC − total capex incl. software additions, $M, all from the
  filed Consolidated Statements of Cash Flows — FY2025 and FY2023 10-Ks):

  | FY | OCF | SBC | capex (PP&E + software) | OE (capex end) | OE (D&A end)* |
  |---|---|---|---|---|---|
  | 2021 | 817.9 | 97.8 | 132.7 | **587.4** | — |
  | 2022 | 372.9 | 83.4 | 174.2 | **115.3** | — |
  | 2023 | 725.6 | 72.4 | 209.3 (135.5 + 73.8) | **443.9** | 525.5 |
  | 2024 | 847.4 | 50.8 | 197.5 (87.2 + 110.3) | **599.1** | 701.9 |
  | 2025 | 893.2 | 80.4 | 198.3 (63.3 + 135.0) | **614.5** | 743.3 |

  *(D&A end = (c) at depreciation of PP&E only: 127.7 / 94.7 / 69.5. Displayed, not used —
  see the (c) judgment below.)*
- **Short-window mean** (window: FY2024-2025, the post-eOne perimeter): **$606.8M**
- **Mid-window mean** (window: FY2023-2025): **$552.5M**
- **Long-window mean** (window: FY2021-2025): **$472.0M — DISPLAYED AND REFUSED as the
  judgment base**: FY2021-2023 contain eOne Film/TV and (part-year) eOne Music — program
  spend net of amortization dragged OCF ~$69M (2021) and ~$212M (2022), and the businesses
  are SOLD. A five-year mean averages two different companies (the queue's ACMR/ALKT rule;
  [E4-25]). The refusal is stated, not silent; the figure stays on display.
- **Spread, capex end, across displayed windows:** 472.0 → 606.8 = **28.6%**
- **Combined range** (window spread × capex band): **$472M to $743M** — yield 3.60% to 5.66%
  on the $13,117M cap
- *Too wide to conclude?* **No — because every construction lands on the same side of the
  Q5 floor** (even the most generous end, $743M, yields 5.66% against a ~10% floor), the
  width cannot change the verdict, so [E4-25]'s close-the-file clause does not fire (the
  ORLY precedent).
- *The distorted years, named [E5-11]:* FY2022 (toy-glut collapse + eOne content spend peak
  — OE $115.3M) and FY2023 (disposal year) sit in the long window; **and FY2025-H1-2026
  carry the OTHER distortion — the Universes Beyond record wave (Final Fantasy = highest-
  selling Magic set of all time). [E4-41] cuts both ways: the mean is not taken off the
  spike either.**
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** Which case: **neither
  the clean D&A-default case nor the [E5-20] railroad case — the D&A end is REJECTED here
  on the filing's own facts, in the conservative direction.** Capex runs 2.8x PP&E
  depreciation, but the excess is *"Additions to software development"* ($135.0M in FY2025,
  balance $385.6M and growing) — internal AAA game development (EXODUS, WARLOCK, due 2027)
  plus digital-platform work (Arena, D&D Beyond). Some of that is growth investment, but
  the digital leg's *unit volume* ($500.3M of Digital and Licensed revenue) cannot be
  maintained without continuous title and platform development — the AATC/Qualcomm shape
  where development spend IS the (c). **(c) is judged at total capex, ~$198M/yr.**
  Conservatism count: this is the single place conservatism is spent in the OE build.
- Band used: **$472M (refused blend, shown) to $743M (D&A end, shown); judged
  OE = $600M** — the two-year post-perimeter mean, rounded down, not normalized down
  further for the Magic wave because H1-2026 (tabletop +31.9%) shows the level holding,
  and not up because CP declines are offsetting. Reason cited from the filing: content
  spend down "over 90%" (Item 1), program spend now −$10.2M/yr, so the post-2023 cash
  engine is the ongoing company.
- Stock compensation subtracted in full **[E5-06]**: yes, $80.4M (FY2025) at the reported
  charge — the [E3-70] floor; no options program of consequence beyond RSU/PSU grants.
- LIFO/working-capital carve-out [E2-23]: working-capital swings run through OCF by
  construction; no separate increment added (no double-count).
- *The capex band does not change the verdict* — see above.

### Great, good, or gruesome? **[E4-20]**
- [x] great — **the WotC leg alone**: $1,006.8M of segment operating profit on $12.9M of
  segment capex and $17.6M of segment D&A, margin rising 41.8% → 46.0%
- [x] good-at-best — **the blend actually purchasable**: judged OE ~$600M on ~$1.2bn of
  tangible operating capital is a high rate, but the toy leg neither grows nor earns
  (CP revenue −38.8% over four years at a 3-4.5% margin) and the incremental corporate
  capital is going into a hits business (video games) with an unproven return
- [ ] gruesome — no: CP shrinks but does not eat significant capital ($45-60M segment capex)
- Evidence: segment supplemental tables, FY2025 10-K (capex/D&A by segment); the eOne
  chapter was the gruesome act and it is sold.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings — **QUALIFIED PASS.** Large, yes. Reliable: the
  five-year OE series runs 587 → 115 → 444 → 599 → 615; the FY2022 collapse is on the
  record, and today's stream is concentrated in ONE product line's release slate (WotC =
  ~95% of ex-impairment segment profit; scored at Q2 as the concentration it is). Worst
  case is scored, not the expected case **[E2-55]**.
- (2) massive liquid assets — **PASS, without the adjective.** $1,378.2M at Q2-2026 (cash
  $880.5M + Treasury-bill investments $497.7M). The $1.1bn revolver and $1.0bn CP program
  are NOT counted **[E5-39]** (both undrawn; CP intentionally unused).
- (3) **no significant near-term cash requirements** — **PASS, and the mechanism is the
  anti-UAL pattern**: the $497.0M 3.55% Notes due November 2026 were **pre-funded** — the
  Q2-2026 10-Q states the 2031 Notes proceeds sit in short-term investments "expected to be
  utilized to repay the 2026 Notes" — borrowed BEFORE the need [E2-64]. Next maturities:
  $475.0M (2027), $109.9M (2028), $900.0M (2029). Dividend ~$392M/yr is discretionary in
  law, sacred in practice.
- Leverage, named and quantified **[E4-16, E3-29]**: **$3,281.9M face debt** (all fixed-rate
  unsecured notes, no covenanted bank debt drawn), net debt ~$1.9bn ≈ **3.2x judged OE
  gross / ~1.9x net**. **[E2-54] coverage test: OCF $893.2M less capex $198.3M = $695M
  against interest paid $158.4M = 4.4x, comfortably met out of current cash flow net of
  capex** — zip-up-the-wallet does not fire. Covenants (interest coverage ≥3.0x, leverage
  ≤3.75-4.00x) are the banks' EBITDA-based constructions, noted, not adopted.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: **collector-fatigue reversal in Magic while the toy leg keeps shrinking —
  the one engine throttles back onto a leveraged, single-engine airframe.** The exposure
  (not experience [E4-40]): WotC is asking a finite enfranchised base to absorb an
  accelerating slate of premium crossover sets; tabletop revenue was FLAT 2022-2024
  (1,067.0 → 1,072.5 → 1,039.6) the last time the base was saturated, exactly the years
  Bandai's One Piece and Disney's Lorcana launched; the record 2025-26 wave rides licensed
  third-party IP whose royalties already lifted royalty expense 30%. A second, slower
  vector: Disney takes back or re-prices the Marvel/Star Wars toy licenses (the
  Frozen/Princess expiration of December 2022 is the filed precedent), and the AAA game bet
  ($385.6M capitalized and rising) misses — the TTWO comparator just impaired $5.9bn across
  two years in that exact business.
- Quantified from filed figures: tabletop reverts to its 2022-2024 plateau (~$1.05bn) at
  the pre-wave ~40% segment margin → WotC OP ~$550-630M; CP ex-impairment ~$80M continues
  shrinking; corporate −$54M → consolidated OP ~$580-660M − interest ~$160M → pre-tax
  ~$420-500M; owner earnings ~$350-420M. **The company does not die — coverage stays
  ~3.5-4x, the dividend ($392M) becomes the thing that has to give — but the equity case
  dies: at today's $13.1bn the reverted yield is ~2.7-3.2%.** Insolvency requires the
  reversal AND a refusal to cut the dividend AND a refi wall — none due before 2027-2029.
- Likelihood: [ ] likely [x] **a real possibility** (the plateau is on the record, three
  years of it, ended by a licensed-IP wave with a finite supply of marquee universes)
  [ ] a low-level possibility — for the *equity-case* death; balance-sheet death is a
  low-level possibility.
- **VERDICT: [x] IN — it survives.** The three strengths score pass/pass/pass (first one
  qualified), interest is covered 4.4x out of cash flow net of capex, the near maturity is
  pre-funded, and the named death is a valuation death, not a solvency death.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: **4.6% at zero growth; ~6.6-7.6% granting +2-3%/yr of
durable growth; reaching ~10% requires +5.4%/yr PERPETUAL growth on the blend** — against a
post-perimeter record of +2.6% (one clean OE year-pair) and a blend in which the growing
half (WotC, +14.2%/yr revenue over four years) is being offset by the shrinking half (CP,
−11.5%/yr). [E4-35]'s burden of proof for a sustained-growth carry is not met in writing.
**Below roughly 10% on every honest construction: the name is QUIT ON, not ranked.**
**No risk premium in the discount rate [E3-42]** — the bare 5.27% sovereign is used.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings **$600M judged** ÷ market cap **$13,117M** = **4.57%** · sovereign **5.27%**
- full construction range: **3.60%** (refused blended 5-yr window, shown) · **4.21%**
  (3-yr) · **4.63%** (2-yr post-perimeter) · **5.67%** (D&A end, rejected as (c))

**2. WHAT THE PRICE ALREADY ASSUMES**
- growth needed to justify the quote against the bond: **+0.70%/yr perpetual** (the gap
  from 4.57% to 5.27%) — **modest, and this is the strongest thing sayable for the price**
- what the business has actually done: post-perimeter OE +2.6% (one year-pair);
  WotC revenue +14.2%/yr (4-yr); CP revenue −11.5%/yr (4-yr); blend ex-Entertainment
  revenue −3.2%/yr (2021→2025)

**3. WHAT YOU ARE PAID**
- return at the current price = **−0.70 points UNDER the sovereign** on the judged
  construction (−1.67 to +0.40 across the range) — under the bond before any growth

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.27%** — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support. Zero-growth at the 5.27% sovereign, on 141,044,467 shares:
- conservative **~$65/sh** ($472M refused-blend construction ≈ $9.0bn) · judged **~$80/sh**
  ($600M ≈ $11.4bn) · optimistic **~$100/sh** ($743M D&A-end ≈ $14.1bn) ·
  **current price $93.00** — inside the range, in its upper reaches
- at the ~10% floor **[E4-28]**: **~$35-55/sh, judged ~$43** ($600M ÷ 10% ≈ $6.0bn)
- **the upside bound [E2-63], named:** the engine's ceiling is the enfranchised Magic
  base's absorption rate for premium sets and the finite slate of marquee crossover
  universes — the record year is not a run-rate entitlement

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- floor verdict first: honest pre-tax expectancy **4.6-7.6% vs ~10% [E4-28] — BELOW →
  quit on, and the ranking lines below are not filled in.**
- *Take the best available, or nothing.*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] Normal method [E4-11] — not used
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      **No. $93.00 sits INSIDE the zero-growth range (~$65-100) — the middle outcome, a
      finished answer: no useful conclusion from price, move on.** No margin added on top.
      The floor verdict above closes the file regardless of the bar.
- **Windage count: ONE** — (c) judged at total capex. The window judgment (post-perimeter
  mean) is a perimeter correction, not conservatism; the sovereign is bare; no margin was
  stacked on the screamer test. **[E4-11]**

- **VERDICT: [ ] IN — **the file FAILS AT Q5, ON PRICE, at the [E4-28] floor.** Q1 IN ·
  Q2 IN (NARROW) · Q3 IN (overlay, two flags) · Q4 IN — the fourth name in this queue's
  history to clear all four business gates (after ORLY, BRK-B, MCD), and the first whose
  franchise is priced within sight of the bond: the judged yield misses the sovereign by
  only 0.70 points and the D&A end clears it. But the floor is the figure we quit on:
  honest expectancy 4.6-7.6% vs ~10%. **Quit on, not ranked.**
  [ ] UNRESEARCHED [ ] UNKNOWABLE · ranking position: **none — below the floor**

**Pre-committed re-entry arithmetic (not a Q6 — the file closed at Q5):** at ~$43/sh the
zero-growth expectancy meets the ~10% floor at today's judged OE; at ~$80/sh the name
matches the 5.27% bond with zero growth. Recompute both at the sovereign of the day and
the OE of the latest filings — the Magic plateau question (tabletop revenue vs the
2022-2024 flat line) is the first thing to re-read, per the named death in Q4.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened — the file closed at Q5 on the floor.** No position exists or is licensed, so
no exit yardsticks are pre-committed here beyond the re-entry arithmetic recorded at the
foot of Q5. The monitoring item carried forward for any future re-run: **the Magic tabletop
revenue line against its 2022-2024 plateau (1,067.0 / 1,072.5 / 1,039.6), and the share of
WotC growth attributable to royalty-bearing Universes Beyond sets** — the [E4-37]
agony-metric analogue for a set-cadence business — plus the FY2027 releases of EXODUS and
WARLOCK as the first test of the $385.6M capitalized-games bet.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN → Q2 IN → Q3 IN → Q4 IN →
  Q5 FAIL on the floor → Q6 not opened)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — the
  TCG-attacker sub-row is filled from published rung-3/4 documents (Bandai Namco disclosed
  figures; Ravensburger/Pokémon documented to the extent documents exist, absences named);
  the Q2 verdict does not rest on any unverified figure
- [x] Every UNRESEARCHED verdict names the artifact — none issued
- [x] Every UNKNOWABLE verdict states what cannot be known — none issued
- [x] Step 0: filings read with accession numbers; FY2025 OCF $893.2M cross-checked to the
  filed statement (and the capex cross-check FAILED, caught the tool defect)
- [x] Owner earnings on multi-year means; three windows displayed; the blended 5-yr window
  displayed AND refused with the reason stated; capex band disclosed as a judgment
- [x] Competitor row filled: 4 SEC toy filers (incl. subject), 2 SEC games filers, LEGO
  rung-3, Bandai Namco rung-4, Ravensburger/Pokémon documented-or-absence-named
- [x] Sovereign 5.27% USD, US Treasury daily par yield curve (issuing authority), 2026-09-02
- [x] Value stated as a round-number range (~$65-100 zero-growth; ~$35-55 floor)
- [x] One bar (screamer), windage count stated: one
- [x] Prices dated; $93.00 aggregator live quote flagged as such
- [x] Run committed to git after every question (five commits this run plus the
  session-kill preservation commit)

## TOOL DEFECTS FOUND THIS RUN (operator rule 8: tools compute, this file concludes)
1. **run.py capex misses "Additions to software development."** It read FY2025 capex as
   $63.3M (PP&E line only) against a filed $198.3M (PP&E $63.3M + software $135.0M) —
   OE overstated by ~$135M/yr for FY2024-2025, and the 3-yr screen window (584-634 vs the
   true 552.5) inherits it. Any filer that capitalizes software on a separate cash-flow
   line (the tag family PaymentsToDevelopSoftware / PaymentsForSoftware) is affected
   queue-wide. Same class as the MCD D&A first-tag defect: fix in the tag union, not by
   hand-editing outputs.
2. **run.py share basis again a weighted-average EPS denominator** (140.2M) rather than the
   cover count (141,044,467) — known defect, harmless here (0.6%), caught by
   `cover_shares.py` as designed.
3. **The screen row's 3.37% yield is a double artifact**: the refused blended 5-yr window
   (two different companies averaged, eOne inside) on a stale cap. Reproduced, then
   corrected by hand to 4.57% judged. The 40.9% "spread" reproduces exactly as
   (634−450)/450 — both ends carrying defect 1.
4. `acquisition_flag()` at 34% did its job as a PROMPT (the eOne note was read first, and
   the perimeter finding shaped the whole run) — noted because AATC showed the same flag
   can fire on stale history; here the history was the point.

## BRIEF DEFECTS (the operator asked; MCD found three)
1. **"HAS cut its dividend? Verify" — it never cut.** $0.68/quarter held 2019-2021, one
   raise to $0.70 (2022), flat four-plus years since. The true fact is a frozen dividend
   paid straight through a year (FY2022) when it ran 3.3x owner earnings.
2. **The brief's QCOM-shape prior is refuted by its own suggested test**: WotC is ~92-97%
   of segment profit (three years running), not a QTL-like minority — the operator's
   [E4-26] hedge ("the WotC share of PROFIT may be high enough to flip that") was the
   correct fork.
3. **"Establish what disappeared [E2-49]" presumes something disappeared — nothing did.**
   The tabletop/digital split has been published continuously since the segment existed
   (FY2021). What fires [E2-49] instead is the brand-portfolio recategorization twice in
   three years; and the deeper [E4-55] fact is that **no physical series has EVER existed
   in the filings** — units/players were never disclosed, by Hasbro or by any SEC toy peer.
4. Small: the brief filed Monopoly Go under "WotC digital licensing" — correct and filed
   ($168.0M FY2025); and the "no step" screen note is right (no level_shift fired; the
   FY2022 trough is a V, not a step).
5. The proxy's Item 402(v) pay-versus-performance table was located but its CAP series was
   not transcribed — the incentive-calculation tables (which name the goals, actuals and
   payouts) carried the Q3 weight instead. Recorded as a gap, judged immaterial to the
   verdict.

## REGISTER
- Verdict: [ ] IN **[x] OUT — about the PRICE, at the Q5 floor** (business gates all IN)
  [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **A genuine narrow franchise (Wizards: ~95% of profit, 46% margins, $13M of
  capex) wearing a shrinking commodity toy business and $3.3bn of eOne's leftover debt —
  priced at 4.6% against a 5.27% bond and a ~10% floor: quit on, not ranked.**
