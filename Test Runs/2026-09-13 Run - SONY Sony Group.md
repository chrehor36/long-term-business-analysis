# Company Run — Sony Group Corporation (SONY) — 2026-09-13
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

*Run written under the WRITE-EARLY protocol: this section was written before Q1 opened and every
later section is appended as it closes. The brief was read as a set of hypotheses to refute; it
named no expected verdict and none is assumed here. The 2026-07-14 v3.0 SONY pass in
`Test Runs/2026-07-14 Test Run - SONY, TBTC, NTDOY.md` ran on a net-income proxy
("Owner earnings uses **net income as first proxy**") and is superseded, not inherited; its
figures are not used anywhere below.*

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 3.995% (≈4.00%) · JGB 30-year · date 2026-09-10 · source: Japan Ministry of Finance,
  official JGB curve `jgbcme.csv`, struck fresh this run through `python tools/sources.py`
  (`sovereign('JPY')` returned `(3.995, '2026-09-10', 'Japan MOF official JGB curve')`).** The same
  MOF row: 20Y 3.754%, 25Y 4.016%, 40Y 4.003%; tenor used is 30Y, as in every JPY run in this
  tree (MITSY 2026-08-28). The brief's 4.00% is confirmed to rounding.
- **USD shown for sensitivity only: 5.35%, 30-year, 2026-09-11, US Treasury daily par yield curve**
  (`sovereign('USD')`, issuing authority, not the FRED fallback).
- **Why JPY, argued rather than defaulted.** The earnings currency is *plural* in substance. The
  20-F's geographic note (Note 4, sales by customer location, FY ended 2026-03-31) puts **Japan at
  ¥1,333.2bn of ¥12,479.6bn = 10.7%** of sales; United States ¥4,064.4bn (32.6%), Europe ¥2,826.8bn
  (22.7%), China ¥1,428.7bn (11.4%), Asia-Pacific ¥1,694.9bn (13.6%), other ¥1,131.6bn (9.1%).
  **Nearly 90% of sales are earned outside Japan**, and 48% of non-current assets sit in the United
  States (¥3,328.9bn of ¥6,870.2bn). Profit by currency is **not disclosed** (no instance found in a
  search of the 20-F text for a profit-by-currency table; the FX sensitivity in Item 5 is by
  segment, read at Q4). The case for JPY anyway: [E4-15]'s gravity acts on the rate "that the
  investors need", and the owner of a Tokyo share is paid, measured and priced in yen — the cash
  flows are reported in yen, the dividend (¥25/share FY3/26) and the ¥500bn buyback are paid in
  yen, and the quote used below is the Tokyo quote in yen. [E3-32] forbids a view on rates, which
  includes a view on which currency's rate will fall. **The foreign earning base is carried as
  WIDTH at Q4-Q5 (the yen owner-earnings figure moves with the yen), not as a second rate** — the
  MITSY precedent. **And the choice cannot change a verdict at Q5**: the ~10% floor [E4-28]
  *"that's true whether short rates are 6 percent or whether short rates are 1 percent"* governs
  above both the 4.00% JGB and the 5.35% UST.
- **FX, quote vs earnings: none needed.** Market cap is taken in **JPY from the Tokyo quote**
  (6758.T), so the cap and the yen owner earnings share a currency by construction. **Never mixed
  with the USD ADR.** For reference only: SONY ADR $23.90 and 6758.T ¥3,632, both 2026-09-11 close
  (Yahoo, **aggregator, live quotes only, flagged**) imply ¥151.97/$.
- **ADR ratio, from the filing:** 20-F cover, *"Each American Depositary Share represents one share
  of Common Stock."* Derived check: ¥3,632 ÷ $23.90 = ¥151.97/$, a plausible spot for 2026-09-11,
  consistent with 1:1.

**THE SHARE COUNT — by hand (a 20-F filer: `cover_shares.py` is blind to 6-Ks, RESUME STATE §5).**
1. **20-F cover, "as of the close of the period covered", March 31, 2026: Common Stock 5,907,667,254**
   (of which ADS 523,381,332). Item 9/10 cross-check: *"As of March 31, 2026, there were
   6,149,810,645 shares of Common Stock outstanding, including 242,144,891 shares of treasury
   stock"* → 5,907,665,754 ex-treasury. **The two filed figures differ by 1,500 shares (0.00003%)**;
   recorded, immaterial, the cover figure is not used below because a later filed count supersedes it.
2. **Cancellation:** 6-K 2026-05-08 (`0001104659-26-057643`): *"184,494,319 shares"* of treasury
   stock cancelled, planned date May 29, 2026. Issued falls 6,149,810,645 → **5,965,316,326** —
   confirmed exactly by the monthly Share Buyback Report for May (6-K 2026-06-12,
   `0001104659-26-073315`). Cancelling treasury stock does not change the outstanding count.
3. **Latest filed month-end count: Share Buyback Report for July 2026, 6-K filed 2026-08-12
   (`0001104659-26-094573`), "Status of Shares Held in Treasury (as of July 31, 2026)": total issued
   5,965,316,326; treasury 111,510,451 → outstanding 5,853,805,875.**
4. **Walked forward through August:** repurchased **−11,613,200** (*"August 1, 2026 to August 31,
   2026"*, 6-K 2026-09-03, `0001104659-26-104960`); treasury delivered on RSU vesting **+1,142,196**
   (maximum; payment date August 3, 2026, 6-K 2026-07-17, `0001104659-26-084484`). August option
   exercises are unknown until the August Share Buyback Report (~mid-September); July's were
   263,500, so the unknown is of order 0.005% of the count.
5. **Shares used: 5,843,334,871** (as at 2026-08-31, ±~0.5M). Repurchases continue daily under the
   May 8, 2026 facility (230M shares / ¥500bn max, May 11, 2026–May 10, 2027; 67,581,300 shares for
   ¥237.4bn done by Aug 31), so September purchases already made are not in the count — the
   direction of that omission slightly *overstates* the cap.
- **Split:** *"a five-for-one stock split of its common stock effective October 1, 2024, with a
  record date of September 30, 2024"* (20-F Item 5 and Item 10). **It sits inside the owner-earnings
  window, but the owner-earnings series is a yen total, not per-share, so it moves nothing there.**
  For the cap, [CLAUDE.md]'s split-invariant rule: close(2026-09-11) × shares(2026-08-31) × splits
  after 2026-08-31 = × **1.0** (`split_factor_after('SONY','2020-01-01')` returns 5.0, the 2024 split
  only; none after the measurement date). The ADR ratio was 1:1 on the 2026 cover; the 2024 split
  is not re-checked against the ADR because the ADR is not used for the cap.
- **Price ¥3,632** (6758.T close 2026-09-11, Yahoo, aggregator flagged) × **5,843,334,871** =
  **market cap ¥21,223bn (≈ ¥21.2 trillion)**.

**THE PERIMETER — the brief's memory is CONFIRMED from the filing, with the details it lacked.**
- 20-F, forepart and Note 33: *"At a meeting of Sony Group Corporation's Board of Directors held on
  May 14, 2025, Sony Group Corporation decided on a plan for the execution of a partial spin-off of
  Sony Financial Group Inc. ("SFGI") … as of October 1, 2025"*; *"the Financial Services business
  was classified as a discontinued operation and has been excluded from the reporting segments.
  Consequently, the figures for comparative periods have been re-presented."*
- Mechanics (Note 20(5), Note 33): dividend in kind of *"one SFGI share to one share of common stock"*
  to holders of record September 30, 2025; fair value distributed **¥955,700 million (¥159.89 per
  share)**. *"As a result, Sony Group Corporation held 16.40 % of SFGI shares as of October 1, 2025"*;
  SFGI *"was deconsolidated as of October 1, 2025"* and *"is accounted for as an affiliate using the
  equity method."* Recycling of AOCI produced a **¥1,377,795 million loss** in discontinued
  operations (debt-instrument FVOCI loss ¥1,640,079M less insurance finance income ¥263,298M), which
  is why FY3/26 **net income attributable was a loss of ¥326,865M** while continuing pre-tax income
  was ¥1,422,374M.
- **Presentation: discontinued operations with re-presented comparatives, three years deep.** The
  FY3/26 20-F's cash-flow statement shows *"Total net cash provided by operating activities from
  continuing operations"* for FY3/24, FY3/25 and FY3/26 on the new perimeter. **Earlier years exist
  only on the old (consolidated-with-insurer) perimeter**, where the insurer's and bank's
  policyholder and deposit flows run through operating cash flow (FY3/23 consolidated OCF was
  ¥314.7bn; FY3/25 ¥2,321.7bn — the insurer's investment purchases and reserve increases, not
  industrial earnings).
- **How this run handles it (the CNR rule): no mean crosses the perimeter.** Owner earnings are built
  only on the non-financial perimeter. Two sources exist for it: (A) the **audited IFRS
  continuing-operations cash flow** (FY3/24–FY3/26, three years, FY3/26 20-F); and (B) the
  **unaudited "Sony without Financial Services" condensed cash-flow schedule** that Sony has printed
  in every 20-F's Item 5 (*"Information on Cash Flows Separating Out the Financial Services
  Segment"*), which carries the non-financial perimeter back to FY3/21 and earlier. **The two bases
  are measured against each other in the overlap before either is used** (Q4). The retained 16.40%
  SFGI stake is **excluded from owner earnings** and noted as a separate asset; the insurer's cash
  flows never enter an industrial figure.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A (Item 5: operating results by segment, the separated-cash-flow schedules, liquidity and
  capital resources, the fifth mid-range plan targets) — read in the sections cited at each gate
- [x] cash-flow statement incl. detail lines (continuing and discontinued, three years; content-asset
  line; payments for PP&E and intangibles; purchases of businesses; treasury stock)
- [x] footnotes (Note 4 segments and geography; Note 20 equity and dividends in kind; Note 26 EPS
  and split; Note 33 discontinued operations; others cited where used)
- **Primary document: Form 20-F for the fiscal year ended March 31, 2026, filed 2026-06-18,
  accession `0001193125-26-274893`** (`d28719d20f.htm`). Also read: 20-F FY3/25 filed 2025-06-20
  (`0001193125-25-143137`); 20-F FY3/24 (`0001193125-24-167500`), FY3/23 (`0001193125-23-169510`),
  FY3/22 (`0001193125-22-183263`) for the separated schedules; the 6-Ks cited above; Q1 FY3/27
  results 6-K 2026-07-31 (`0001104659-26-088915`, `-088922`).
- **Figure cross-checked against the filed statement:** consolidated net cash provided by operating
  activities, FY ended 2025-03-31 — **SEC XBRL companyfacts `ifrs-full:CashFlowsFromUsedInOperatingActivities`
  = ¥2,321,675,000,000 (accn 0001193125-25-143137); the FY3/26 20-F cash-flow statement prints
  "Net cash provided by operating activities … 2,321,675" for 2025. Match to the million.**
  **Tooling note:** companyfacts had **not yet ingested the FY3/26 20-F** at this run (latest
  20-F accession in the facts is 0001193125-25-143137), which is exactly the "short XBRL history"
  the triage recorded; every FY3/26 figure here is from the document.
- Company name: the CIK was "SONY CORP" until 2021-05-14 (submissions `formerNames`), renamed Sony
  Group Corporation; same registrant, same CIK 0000313838. `deal_note`/`name_change_note` returned
  nothing per the brief; the rename is a name, not a perimeter.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**The security is a conglomerate; Q1 is answered per segment, as GHC (2026-09-02) and HAS
(2026-09-03) were, and the understanding verdict is about the money-making, not its durability
(Q2/Q4).** All figures are the filed segment note (Note 4): FY3/22–FY3/23 from the FY3/24 20-F
(`0001193125-24-167500`), FY3/24–FY3/26 from the FY3/26 20-F (`0001193125-26-274893`); sales
include intersegment; ¥bn. Computation: `_research 2026-09-13 SONY/seg.py`.

| Segment | Sales FY3/22 → FY3/26 | OI margin FY3/22 · 23 · 24 · 25 · 26 | 5-yr OI, share of segment total | D&A ÷ sales FY3/26 | FY3/26 OI share |
|---|---|---|---|---|---|
| Game & Network Services | 2,740 → 4,686 | 12.6 · 6.9 · 6.8 · 8.9 · **9.9%** | ¥1,764bn · 28.8% | 3.1% | 30.3% |
| Music | 1,117 → 2,120 | 18.9 · 19.1 · 18.6 · 19.4 · **21.1%** | ¥1,580bn · 25.8% | 6.2% | 29.2% |
| Pictures | 1,239 → 1,499 | 17.5 · 8.7 · 7.9 · 7.8 · **7.0%** | ¥677bn · 11.0% | 34.5% (content amortization) | 6.8% |
| Entertainment, Technology & Services | 2,339 → 2,261 | 9.1 · 7.2 · 7.6 · 7.9 · **7.0%** | ¥929bn · 15.2% | 4.6% | 10.4% |
| Imaging & Sensing Solutions | 1,076 → 2,152 | 14.5 · 15.1 · 12.1 · 14.5 · **16.6%** | ¥1,180bn · 19.2% | 12.3% | 23.3% |
| All Other / Corporate | — | FY3/26 All Other −¥74.6bn (Sony Honda Mobility EV loss ¥44.9bn) | — | — | — |

*Yen growth flatters every foreign-earning segment: the MD&A's average rate was 150.7 yen/$ in FY3/26;
Music's own dollar-basis streaming growth for FY3/26 was "+9% year-on-year for Recorded Music and +14%
for Music Publishing" (FY2025 results presentation, 6-K 2026-05-08, `0001104659-26-057456`).*

- **Unit economics in my own words, no management language:**
  1. **G&NS — a toll road with a loss-leader on-ramp.** Sony sells a console at roughly break-even
     (hardware ¥1,391.6bn of FY3/26 customer sales, falling) to put a machine in the home; it then
     takes a cut of every game and add-on bought through its store (digital software and add-on
     content ¥2,415.3bn), charges a monthly subscription for online play and a game library (network
     services ¥763.1bn), and makes some games itself. The toll base is the active account base: *"Total
     PlayStation® Monthly Active Users* reached 125 million accounts in June, up 2% year-on-year"* (Q1
     FY26 presentation, 6-K 2026-07-31, `0001104659-26-088922`). The cost that recurs is the next
     console generation — *"investments for the next-generation platform"* are already in the FY3/27
     cost base (same document).
  2. **Music — a rent on copyrights.** Sony owns or controls recordings and song compositions; every
     stream, sync licence, broadcast and live-event merchandising use pays it a royalty, and streaming is
     the largest line (Recorded Music streaming ¥852.7bn, publishing ¥419.9bn FY3/26). The capital is
     the catalog (music catalogs carried at ¥1,585.9bn, March 2026, content note) and new-artist
     advances; growth is bought as well as developed (Pink Floyd, Queen, the GIC partnership and
     Recognition Music Group named in the 20-F and Q1 FY26 materials). A Japan anime/game-app business
     (Visual Media & Platform, ¥325.3bn) rides inside the segment.
  3. **Pictures — a hit-driven film and TV factory with a library and a subscription tail.** Sony pays
     up front to make films and series (film-cost additions ¥475.6bn FY3/26), recovers it over years
     through theatres, licensing and its own channels, and runs Crunchyroll (21 million paid anime
     subscribers, March 2026) and India's SonyLIV. Profit is the difference between what a slate costs
     and what the hits and the library return; D&A is a third of sales because film amortization runs
     through it.
  4. **ET&S — consumer electronics sold on brand and imaging technology.** Cameras and lenses (¥722.5bn),
     TVs (¥476.3bn, down from ¥662.2bn in FY3/24 and now being placed into a TCL partnership, 20-F
     Item 5), headphones, phones and services. A manufacturer's margin, 7–9%.
  5. **I&SS — a semiconductor fab business selling image sensors to phone makers.** Sony designs and
     manufactures CMOS image sensors in its own Japanese fabs and sells them mainly into high-end
     smartphones, with a named concentration: *"strong shipments to our major customer"* (FY2025
     presentation). Capex runs at D&A (I&SS D&A ¥265.1bn; *"approximately 265.3 billion yen in the
     I&SS segment, representing additions to long-lived assets … approximately 246.7 billion yen to
     increase image sensor production capacity"*, 20-F Item 4). **A perimeter change is signed:**
     *"a legally binding definitive agreement for the establishment of Advanced Vision Semiconductor
     Manufacturing Corporation as a joint venture"* with TSMC, Sony contributing ~¥465bn including the
     new Koshi fab, TSMC ~¥282bn cash, volume production *"in 2029"* (6-K 2026-08-11,
     `0001104659-26-093634`); and **the Kumamoto fabs were struck on July 28, 2026**: the Kumamoto
     Technology Center *"suspended production immediately after the earthquake. Restoration efforts to
     resume production are currently underway"*, impact not estimated (Q1 FY26 presentation).
- **The scarce input this business controls — per segment, and it differs in kind:**
  G&NS, the **installed account base** third-party publishers must reach, plus first-party IP;
  Music, **copyrights** (a legal monopoly on each work, for decades); Pictures, a **library** but not
  its talent; ET&S, the **brand and imaging know-how**, not scarce in TVs; I&SS, **stacked-sensor
  process know-how and fab capacity**, a technical lead that must be re-won every node.
- **"On what capital?" — answered by proxy, and the limit stated.** The segment note says: *"The CODM
  does not evaluate segments using discrete asset information."* **No segment asset figure was found
  in the FY3/22–FY3/26 20-F segment notes or MD&A** (searched; the Sony IR site was not swept, so
  this is worded as "no instance found in the filings", per the absence-claim rule). The filed proxies
  are: goodwill by segment (March 2026: Music ¥864.9bn, G&NS ¥487.6bn, Pictures ¥285.4bn, ET&S
  ¥30.7bn, I&SS ¥5.3bn); content assets by class (film costs ¥633.8bn, broadcasting rights ¥137.4bn,
  music catalogs ¥1,585.9bn, game content ¥121.6bn); and D&A by segment (table). The capital a
  segment consumes each year is read from those at Q2 and Q4, not invented here.
- **Will the fundamentals look broadly the same in ten years?** **Music: yes** — the rent on
  copyrights predates streaming and is extended by it. **G&NS: the toll-road shape yes, the road no**
  — two console generations will pass, and the 20-F names cloud streaming and PC as live channels.
  **Pictures: the slate economics yes, the distribution mix no.** **ET&S: no** — TVs are being moved
  out. **I&SS: the business, yes; its ownership of manufacturing, no** — the fab moves into a TSMC
  joint venture by 2029, and the technology resets every process node.
- **The hunt for disconfirming evidence [E4-26], stated before the verdict.** [E3-31] asks for
  businesses *"relatively simple and stable in character"* and **[E4-46]** puts a business needing
  months of study outside the circle. Sony is five unrelated industries, two of them hit-driven and one
  a semiconductor race, reporting in yen on ~90% foreign sales. The answer: each leg's money-making is
  legible from the filing in a paragraph, which is what Q1 tests; **"stable in character" is not
  assumed here — it is the question Q2 ([E4-04]) and Q4 ([E4-25], the spread) must answer, and the
  segments that are not stable are named above so they cannot be averaged away later.**
- **VERDICT: [x] IN** — the money-making is understandable segment by segment from the filed 20-F.
  Understanding is the gate; durability, relative position and the capital each leg consumes are judged
  at Q2 and Q4. *(No "unverified" or "provisional" caveat is carried: the capital-proxy limit is a limit
  of what the filer discloses, stated, and it is not load-bearing for the understanding verdict.)*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Per segment, with the metric set chosen by business type first [E5-37]; the verdict must hold for
what the shareholder actually buys (GHC, 2026-09-02), and where some legs pass and some fail, it is
decided by what the profit and the capital are actually in (HAS, 2026-09-03: IN because the profit was
*"overwhelmingly"* the franchise leg and the rest *"neither grows nor eats material capital"*; BRK,
2026-09-02: IN because a group-level structural moat, the float, carried legs that were individually
substitutable).** Competitor rows were built from filed documents by four research passes and are on
disk: `_research 2026-09-13 SONY/peers_games.md`, `peers_music.md`, `peers_sensors.md`,
`peers_pictures.md` (every peer figure there carries its accession number or URL and a verbatim
line). Peer margins below are arithmetic on those filed figures.

### Is there a group-level moat, as at Berkshire?
**No filed evidence of one.** The 20-F's group-level claim is management language — the *"Creative
Entertainment Vision"*, *"cross-business collaborations"* — with no filed number attached to it: no
shared cost of capital advantage (Sony borrows at A2/A+, US$ notes at 4.657%–5.089%, 6-K 2026-06-24),
no float, no inter-segment economics beyond G&NS/ET&S/I&SS component sales. The legs must carry the
verdict themselves.

### Segment by segment

**1. MUSIC — [x] needed or desired · [x] no close substitute · [~] not price-regulated. NARROW
franchise, direction widening. PASSES.**
- *(2) no close substitute:* a copyright is a legal monopoly on each work, and the industry is an
  oligopoly of three, filed by a competitor: *"the three largest recorded music companies were
  Universal Music Group, Sony Music Entertainment and us, which collectively accounted for approximately
  70% of global recorded music revenues … followed by Sony Music Entertainment with an approximately 23%
  share"*; and *"Sony Music Publishing was the market leader in music publishing in 2024 with an
  approximately 25% share"* (WMG FY2025 10-K, `0001319161-25-000034`, quoting Music & Copyright). A
  streaming service cannot offer a catalogue without all three.
- *(3) price regulation:* partial. WMG's filing records a *"CRB Rate Benefit"* in publishing
  streaming revenue (FY2024 10-K) — US mechanical rates are set by a statutory board, so the publishing
  leg's price is partly administered **[E2-59]**. Recorded-music rates are negotiated.
- **[E4-04]:** the catalogue is not replaced, it accumulates; new-artist signing defends share rather
  than buying a replacement asset — the continuous *defence* **[E5-23]** permits, not the replacement
  [E4-04] excludes.
- **Competitor row (segment operating income ÷ segment revenue, recorded music + publishing, company
  fiscal years, filed):**

  | | FY-2 | FY-1 | latest | source |
  |---|---|---|---|---|
  | **Sony Music** (FY3/24 · 25 · 26) | **18.6%** | **19.4%** | **21.1%** | 20-F Note 4 |
  | UMG, RM + Publishing (2023 · 24 · 25) | 16.0% | 18.8% | 20.1% | UMG AR 2024/2025 Note 3 (rung 3, IFRS) |
  | WMG, RM + Publishing (FY9/23 · 24 · 25) | 17.8% | 17.9% | 16.0% | WMG 10-Ks, segment note |

  *Row limits stated:* Sony's segment carries Visual Media & Platform (anime and game apps, ¥325.3bn of
  ¥2,090.5bn customer sales), which no peer has, and whose hit (*Demon Slayer: Kimetsu no Yaiba Infinity
  Castle*) is named as a FY3/26 driver and a FY3/27 headwind; year-ends and currencies differ; UMG and
  WMG print segment OI before corporate costs of €370M and $380M. **Position: top of the three on the
  same metric, and widening two years running [E4-32].** 3 of 3 majors rowed; RSVR held as context.
- **[E2-44] two-characteristic test:** price — the filed evidence is the *streaming services'* price
  rises (*"in 2025, Spotify increased the price of its premium individual tier in multiple markets"*,
  WMG FY2025 10-K), and **no filing quantifies how much reaches the labels**; Sony's own dollar-basis
  streaming growth *"+9% year-on-year for Recorded Music and +14% for Music Publishing"* (FY3/26) cannot
  be split into price and volume. Volume with minor capital — **no**: growth is also bought (music
  catalogs carried at ¥1,585.9bn; additions ¥141.9bn and ¥152.8bn in the last two years plus ¥202.7bn of
  catalogs through business combinations in FY3/25; Music goodwill ¥864.9bn). [E3-33] untapped pricing
  power: not claimed; [E5-28] would require near-monopoly and the share is 23–25%.
- **Attacker's test [E2-45]:** filed by WMG — artists self-distributing (*"has become an easy option"*),
  investment funds buying catalogues, and generative AI (*"could create vast quantities of new musical
  works to compete with and dilute the impact of our copyright-protected material"*). A funded attacker
  can buy catalogues at auction prices; it cannot buy the installed 23%.

**2. GAME & NETWORK SERVICES — [x] needed or desired · [~] no close substitute · [x] not
price-regulated. NARROW, generation-contingent; units flat. PASSES WITH A DURABILITY DEFECT.**
- *(2)* **For a publisher, no close substitute, and the filings of the publishers say so:** *"Many key
  commercial terms of our relationships with Sony and Microsoft — such as manufacturing terms, delivery
  times, policies and approval conditions — are determined unilaterally, and are subject to change by the
  console manufacturers"* (Electronic Arts 10-K FY3/26); *"Sony may terminate the agreement for any or
  no reason upon 30 days' notice"* (Take-Two 10-K FY3/26) — both carried from `_research 2026-09-03
  HAS/competitor_row_games_lego.md`. That is a toll-keeper's position. **For the player, close
  substitutes exist** — Nintendo, PC and mobile — and Microsoft's own 10-K dropped the sentence naming
  *"Nintendo and Sony"* from FY2025 while its console hardware revenue fell *"25%"* and *"29%"* (FY2025,
  FY2026 10-Ks): the third platform is withdrawing from hardware, which **narrows the substitute set**.
- **[E4-04] — the scope test, applied: does the spending defend the same advantage or buy its
  replacement?** Both. The account base and digital libraries carry across generations (the toll base);
  the console itself is a replacement asset bought every cycle, and first-party games are hits bought
  before acceptance is known: *"the G&NS, Music and Pictures segments must invest substantial amounts,
  which may include significant upfront investments … before knowing whether their products will
  receive customer acceptance"* (20-F Item 3). **The filed cost of the replacement cycle:** G&NS
  operating margin **12.6% (FY3/22) → 6.9% (FY3/23) → 6.8% (FY3/24)** while sales rose 56% into the PS5
  ramp, and *"investments for the next-generation platform"* are already in the FY3/27 cost base. The
  same shape shows at the attacker: Nintendo's margin went **31.6% → 24.3% → 15.6%** through its own
  transition. A console moat is re-won each generation — a **surfing run [E3-51]** on a wave that has,
  so far, been re-caught.
- **Competitor row (operating income ÷ revenue; Sony and Nintendo on the same April–March years):**

  | | FY3/24 | FY3/25 | FY3/26 | source |
  |---|---|---|---|---|
  | **Sony G&NS** | **6.8%** | **8.9%** | **9.9%** | 20-F Note 4 |
  | Nintendo (consolidated, single segment, J-GAAP) | 31.6% | 24.3% | 15.6% | Annual Reports 2024–2026 (rung 3) |
  | Microsoft gaming (June years) | **not disclosed** — no gaming profit line; *"It is impracticable for us to separately identify the amount of amortization and depreciation by segment"* | | | MSFT 10-Ks |

  *Row limits:* not the same metric in substance — Sony's MD&A counts *"sales of non-first-party game
  software titles"* in its own sales, and EA's 10-K says the console manufacturers *"pay us either a
  wholesale price or a royalty percentage on the revenue they derive from their sales of our products"*,
  so Sony's revenue carries the publishers' share while Nintendo's is mostly first-party; margin-on-sales
  therefore understates Sony's toll economics (Sony's 20-F states no gross-versus-net policy for this;
  none was found), and no filed capital figure exists to fix it (Q1). 2 of 3 platform
  holders rowed with a profit figure; Microsoft's absence is a filer limit, not load-bearing, because
  Microsoft's filed revenue direction (hardware −25%, −29%) is what the row uses it for.
- **Units [E4-55]:** *"Total PlayStation® Monthly Active Users* reached 125 million accounts in June, up 2%
  year-on-year"*; March 2026 MAU *"increasing 1% year-on-year to 125 million"*; total playtime Q1 FY26
  *"decreased 4% year-on-year"*; hardware sales down on *"a decrease in unit sales"* in FY3/25, FY3/26 and
  Q1 FY26. **Profit is rising on a flat user base** — through network services (¥545.5bn → ¥763.1bn in
  two years) and mix, which is monetisation of the toll base, not widening of it.
- **Pricing [E4-37, E2-44]:** **no Sony price statement for PS5 hardware or PlayStation Plus was found in
  the 20-F or the 6-Ks read.** The row's pricing evidence is Nintendo's: hardware and subscription
  increases announced 2026-05-08, *"we made the difficult decision to reflect a portion of our costs in
  the selling price"*, which *"raises the barrier for entry to a certain extent"* — cost pass-through with
  a stated volume cost, i.e. the prayer session [E4-37] names, at the stronger-margin peer.
- **Class: NARROW. Direction: margin widening, units flat, and the next generation's cost already
  being booked.** Recorded as a durability defect under [E4-04], not a failure, because the account base
  and the publisher terms carry across generations on the filed evidence.

**3. IMAGING & SENSING SOLUTIONS — [x] needed · [ ] no close substitute over time · [x] not
price-regulated. Position LEADING, class NONE under [E4-04]. FAILS.**
- **Position is real and filed at one remove:** the OmniVision H-share prospectus (HKEX, 2025-12-31;
  Frost & Sullivan, commissioned, not audited) ranks *"Company A"* first in global CMOS image sensors at
  *"44.0%"* of 2024 revenue and *"46.4%"* in smartphones, describing it as *"headquatered in Japan,
  founded in 1946, listed on the NYSE"* (typo as filed). **Judgment, stated as one:** Company A is Sony —
  the 20-F: *"Sony Group Corporation was established in Japan in May 1946"*, NYSE-listed. onsemi names
  *"Sony Semiconductor Manufacturing Corporation"* as a competitor in three consecutive 10-Ks.
- **Competitor row:** Sony I&SS operating margin **14.5% · 15.1% · 12.1% · 14.5% · 16.6%** (FY3/22–26);
  onsemi ISG segment *gross* margin 48.7% · 46.7% · 15.1% (2023–25; automotive/industrial, fab-owning;
  revenue −29% in two years); OmniVision imaging *gross* margin 22.2% · 33.1% · 36.0% (fabless; IFRS then
  CAS); Samsung and ST do not disclose image sensors (System LSI and AM&S are the lowest levels). **Not
  the same metric** (gross vs operating) — held as position evidence only: Sony grew while the one
  segmented fab-owning peer shrank.
- **Why the leader still fails the class — [E4-04]'s own scope, "rapid-change industries":** the
  industry's filers describe it in one sentence: *"The semiconductor industry is highly competitive and
  characterized by constant and rapid technological change, short product lifecycles, significant price
  erosion and evolving standards"* (STMicroelectronics 20-F FY2025, `0000932787-26-000009`), and Sony's
  own 20-F lists image sensors among products *"offered in highly competitive markets characterized by
  severe price competition and continual new product and service introductions, rapid development in
  technology"* (cautionary statement (ii); **the same sentence names "game and network platforms" and
  televisions** — it is boilerplate across legs, so it is carried as the filer's description, and the
  I&SS failure rests on the node-by-node rebuild and the capital below, not on this sentence). The lead is re-won node by node (*"increase density in the horizontal plane through
  process node adaptation … and … in the vertical plane through multi-layered stacking technology"*,
  Item 5), with capital at D&A (¥265.3bn additions, ¥265.1bn D&A, FY3/26), a named single-customer
  dependence (*"strong shipments to our major customer"*), a yield problem in FY3/24 (*"the resolution of
  the manufacturing yield issues that began in the fiscal year ended March 31, 2024"*, 20-F FY3/25), and
  the next node's manufacturing now placed in a joint venture with the foundry leader. **[E3-43]: "a
  business" earns exceptional profits *"only if it is the low-cost operator or if supply of its product
  or service is tight"*** — a 12–17% operating margin at 44% share is the evidence that it is neither
  a pricing franchise nor a toll.

**4. PICTURES — [x] needed · [ ] no close substitute · [x] not price-regulated. NONE. FAILS.**
- Hit-driven by every filer in the row: Warner Bros. Discovery, content acceptance *"may be unpredictable
  and volatile"*; Lionsgate, results *"may depend significantly on the performance of a limited number
  of motion pictures"*; Comcast, *"we typically incur losses on a film prior to and during the film's
  exhibition in movie theaters"*; Nintendo, of its own business, *"The presence or lack of hit products …
  significant impact on operating results"*. Sony's 20-F names technology companies as competitors for
  talent and distribution.
- **Row (each peer's own segment measure — not one metric, stated):** Sony Pictures OI margin 7.9% ·
  7.8% · 7.0%; WBD Studios operating income 1.7% · 4.6% · 13.3%; Disney Content Sales/Licensing (segment
  OI) −2.0% · 4.2% · 4.6%; Lionsgate Motion Picture segment profit 18.8% · 19.0% · 17.2%; Comcast
  Studios Adj. EBITDA 10.9% · 12.7% · 9.7%; Paramount Filmed Entertainment Adj. OIBDA −4.0% · −3.2%.
  **Sony is mid-row; the row itself is the finding — no studio earns franchise economics on a consistent
  measure.**
- **The cash says the same:** film-cost and broadcasting-rights additions exceeded their amortization by
  ¥100.3bn (FY3/25) and ¥104.0bn (FY3/26) (content note), so segment OI + content amortization − content
  additions = **¥17.0bn and ¥0.9bn** against reported OI of ¥117.3bn and ¥104.9bn
  (`segcash.py`; pre-tax, before other capex — a COMPUTATION, not owner earnings). Crunchyroll (21M
  paid subscribers) is the one niche asset inside; it is not separately reported.

**5. ENTERTAINMENT, TECHNOLOGY & SERVICES — [x] needed · [ ] no close substitute · [x] not regulated.
NONE. FAILS.** Sales ¥2,339bn → ¥2,261bn, margin 9.1% → 7.0%; Displays sales ¥662.2bn → ¥476.3bn in two
years and placed in a TCL partnership; the 20-F: *"intensified competition in Displays"*, and the
risk-factor language on *"ongoing price erosion that frequently affects its consumer products"*.
[E2-58]'s territory. No peer row is built for a leg whose failure is filed by the subject itself and on
which no moat is claimed (the GHC manufacturing precedent: absence stated, nothing held PROVISIONAL on it).

### What the shareholder buys — the mix, and where the capital goes

| | 5-yr segment OI share (FY3/22–26) | FY3/26 OI share | class |
|---|---|---|---|
| Music | 25.8% | 29.2% | NARROW, widening |
| G&NS | 28.8% | 30.3% | NARROW, generation-contingent |
| **Franchise legs** | **54.6%** | **59.5%** | |
| I&SS | 19.2% | 23.3% | NONE ([E4-04]) |
| ET&S | 15.2% | 10.4% | NONE |
| Pictures | 11.0% | 6.8% | NONE |
| **Non-franchise legs** | **45.4%** | **40.5%** | |

- **The capital:** I&SS alone took ¥265.3bn of the ¥804.9bn of FY3/26 capital expenditure (20-F Item 4;
  33%, for 23% of segment profit), almost all of it *"to increase image sensor production capacity"*;
  Pictures' content additions ran ¥100bn a year above amortization while its margin fell. [E2-56]: the
  marvelous core legs *"camouflage repeated failures in capital allocation elsewhere"* is the risk the
  consolidated series hides, and the Q3 acquisition record (Bungie ¥510.5bn, written down; Sony Honda
  Mobility) sits in it.
- **The consolidated primary metric [E3-46, E4-32]:** return on equity of Sony without Financial
  Services **22.0% → 17.2% → 14.7% → 14.5% → 13.0%** (FY3/22–26, computed in Q3 from the company's
  separated statements) — **down every year** on an equity base that nearly doubled. Direction outranks
  existence [E4-32], and the direction of the whole is down.

### The hunt for the strongest case FOR a franchise [E4-26], stated as its holders would state it
*"Sony is not a TV maker any more. Sixty per cent of profit is a music oligopoly where it is the top-margin
major and the #1 publisher, and a console platform whose publishers sign terms Sony sets unilaterally,
whose only Western rival is walking away from hardware, and whose segment profit is guided to ¥660bn
(14.5%) for FY3/27. The sensor business is 44% of its world market and is moving its capital burden into
a joint venture with TSMC; TVs are going to TCL; the insurer is gone. The perimeter is converging on the
franchise legs, and the row shows Sony at or near the top in every leg it keeps."*
**The answer, on the filed record:** (1) the perimeter that exists is the one priced — the TSMC joint
venture is a controlled, consolidated subsidiary into which Sony contributes ~¥465bn (6-K 2026-08-11),
so the capital burden stays on Sony's balance sheet; the TCL partnership is signed, not closed; (2) the
FY3/27 figures are a forecast, and [E3-48] forbids reading a forecast as a moat; (3) leading position in
a rapid-change industry is the [E3-51] surfing run, not the [E4-04] class — the corpus separates them
explicitly; (4) even granting both franchise legs in full, 40–45% of the profit and the largest single
call on capital are in legs that fail [E3-03] or [E4-04], and HAS passed only where the franchise was
overwhelming and the rest ate no material capital; (5) the whole's return on equity has fallen five
years running. **The strongest case is a case about a future perimeter. Q2 judges the present one.**

- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04, E4-23]:**
  Music no; G&NS partly (each generation); I&SS yes (each node); Pictures yes (each slate). No
  key-person dependence is filed for any leg.
- **Untapped pricing power [E3-33]:** not claimed for any leg; [E5-28] would require near-monopoly, and
  the highest filed share is I&SS at 44% (consultant-sourced), the leg with the weakest pricing evidence.
- **Peers named: 12 across four industries** (music: UMG, WMG, RSVR context; platforms: Nintendo,
  Microsoft, EA/TTWO context; sensors: onsemi, ST, Samsung, OmniVision; studios: WBD, Disney, Lionsgate,
  Comcast, Paramount). Unavailable at the needed level and said so: Microsoft gaming profit, Samsung and
  ST image-sensor lines, the named-but-unrowed SmartSens and GalaxyCore. **None of the missing figures is
  load-bearing for the verdict** — the two passes rest on the subject's and the peers' filed segment
  figures and filed industry structure; the three failures rest on the subject's own filing and industry
  structure, not on a peer margin. **So the class is not held PROVISIONAL.**
- **The row's limit [E3-61]:** the row shows position; it cannot show conduct — whether the three music
  majors or the two remaining console makers behave like a *"demented Kellogg"*. No model predicts it.
- **Class: [ ] WIDE [ ] NARROW [x] NONE for the security as constituted** — two NARROW legs (Music,
  G&NS) inside a conglomerate whose other three legs, ~45% of five-year segment profit and its largest
  capital programme, are not franchises. · **Direction: the whole's ROE falling five years running;
  Music widening; G&NS margin widening on flat units; I&SS position gaining in a class that does not
  hold one.**
- **VERDICT: [x] OUT** — on the business as constituted: the shareholder buys five legs, and the
  franchise verdict does not hold for that bundle. Not a finding that Music or PlayStation lack moats; a
  finding that Sony, as filed, is not a franchise. **OUT closes the file. Q3–Q6 are RECORDED, NOT
  GOVERNING, below; the price is reported under COMPUTATION — NOT A CLEARANCE (operator rule 3).**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business).
*Operator protocol 2: no later question can reopen it. Q3 is recorded because the brief asks for capital allocation,
pay and guidance against outturn, and because Q6's reopening conditions need it. Nothing below is a clearance.*

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution** **[E3-38]** — for the legs that are *"a business"* rather than a franchise in
  [E3-43]'s sense (*"a business, unlike a franchise, can be killed by poor management"*): Pictures
  (a slate greenlit every year), first-party G&NS (the 20-F: *"the G&NS, Music and Pictures segments
  must invest substantial amounts, which may include significant upfront investments … before knowing
  whether their products will receive customer acceptance"*), and I&SS (fab commitments of ¥227.4bn
  and ¥246.7bn in two years *"mainly for the purpose of increasing image sensor production capacity"*,
  now a ~¥465bn contribution to a TSMC joint venture). These are have-to-be-smart-every-cycle
  decisions, and Q2 found that part of the profit is in them.
- [ ] **Control** — a public minority position, exit available **[E1-16]**.
- [ ] **Leverage** — after the spin-off, no insurer or bank balance sheet remains; the non-financial
  perimeter holds net cash (Q4) **[E3-29]**.
- **Case declared: Q3 is a BINARY GATE, on daily execution for the non-franchise legs.** No price
  compensates a failure here **[E1-16, E3-29, E5-35]**. The gate's binary is integrity; competence
  errors are priced, not refused **[E5-16]**.

**Honesty — binary, permanent, filings-based [E5-16].** Matters dated to when public:
- **Legal proceedings, 20-F FY3/26 Item 8:** *"Sony believes that the outcome from such legal and
  regulatory proceedings would not have a material impact on Sony's results of operations and financial
  position."* No named proceeding is disclosed; the risk factor names *"antitrust scrutiny of market
  practices for alleged anti-competitive conduct"* as a class. No conduct matter was found in the 20-F
  or the 6-Ks read (2026-04-01 to 2026-09-12). **Absence-claim wording: no instance found in those
  documents; proceedings reported only outside SEC filings were not swept.**
- **The error-correction cover boxes** of the FY3/26 20-F (*"reflect the correction of an error to
  previously issued financial statements"*, and the clawback box) are **unchecked**.
- **One correction outside the 20-F text:** the FY2025 results presentation (6-K 2026-05-08) names
  *"expenses resulting from a correction in the amount of certain previously capitalized development
  costs (18.3 bln yen) recorded in FY25"* in G&NS. **No instance of the word "correction" in that sense
  was found in the 20-F text.** It is 1.3% of FY3/26 operating income and is disclosed, quantified and
  footnoted in the presentation, so it reads as a small capitalisation error caught and expensed, not
  as concealment; it is recorded as a **prompt to read [E4-22]**, not a finding.
- **No integrity disqualifier found.** Written per **[E5-17]**: this is the absence of found
  disqualifiers, not a finding that the managers are honest.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49, E3-48].**
- [ ] **weak accounting** — SBC is expensed (Note 21: ¥21,657M / ¥29,416M / ¥39,102M, FY3/24–26);
  IFRS, integrated audit with an internal-control opinion (auditor's report at F-2, PCAOB ID 2743). One prompt: the ¥18.3bn development-cost
  correction above.
- [ ] **unintelligible footnotes** — the spin-off accounting (Note 33) is long but legible, and it
  prints the loss it recycled (¥1,377,795M) and the offsetting ¥188,888M gain-and-impairment pair in
  full. Not fired.
- [x] **trumpeted earnings projections / growth targets — FIRES IN FORM.** Sony publishes a full-year
  forecast every May and revises it every quarter, and runs three-year mid-range plans with numeric
  KPIs (5th plan: *"an average annual growth rate of consolidated operating income … of 10% or more,
  and a three-year cumulative consolidated operating income margin of 10% or more"*). **[E5-30]**
  names the ratchet. **[E3-48]'s action — the record against outturn — reads the other way:**

  | Forecast (date, filing) | Outturn | |
  |---|---|---|
  | FY3/25 OI, Sony without FS: ¥1,130bn (6-K 2024-05-14, `0001104659-24-060824`) | ¥1,276.6bn | beat +13% |
  | FY3/25 OCF, Sony without FS: ¥1,400bn (same) | ¥1,972.4bn | beat +41% |
  | FY3/26 OI, continuing, after tariff: ¥1,280bn (6-K 2025-05-14, `0001104659-25-048173`) | ¥1,447.5bn | beat +13% |
  | FY3/26 segment: G&NS 480 · Music 355 · Pictures 125 · ET&S 180 · I&SS 280 | 463.3 · 447.0 · 104.9 · 158.6 · 357.3 | three misses, two beats |
  | 4th mid-range plan: cumulative Adjusted EBITDA ¥4.3tn, FY3/22–24 (20-F FY3/22) | 1,597.9 (20-F FY3/22) + 1,797.6 + 1,818.0 (20-F FY3/24) = ¥5,213.5bn | beat +21% |
  | 5th plan: OI CAGR ≥10% | *"18%"* two years in (20-F FY3/26) | ahead |

  The consolidated record is conservative-and-beaten; the segment record is mixed, and the misses
  are where Q2 puts the non-franchise legs (Pictures, ET&S) plus G&NS's Bungie write-off. **Nine in
  ten projections justify a decided course [E3-48]; this record shows forecasts set low enough to beat,
  which is a guidance culture, not a fabrication.** Flag stands as a prompt; no fabrication tell.
- [ ] **serial share issuance** — the share count fell: issued 6,149,810,645 → 5,965,316,326 after
  the May 2026 cancellation; RSU and option deliveries come from treasury stock bought back. Not fired.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, at full strength historically, and
  partly retired.** The 4th mid-range plan (FY3/22–24) made Adjusted EBITDA *"the most important
  financial performance KPI"* and paid on it: the FY3/22 20-F's remuneration table gives *"Adjusted
  EBITDA (*1) | 50% | Amount determined in order to achieve the Adjusted EBITDA (defined below) target
  of 4.3 trillion yen"*, and the MD&A justified it because it *"represents the sustainable earnings power
  of a business"* (20-F FY3/22) and because *"they are often used to calculate corporate value"* (20-F FY3/24,
  of Adjusted OIBDA and Adjusted EBITDA together). **[E4-29]'s own
  words answer that justification: "That's nonsense."** Its formula excludes *"amortization for film
  costs and broadcasting rights, as well as for internally developed game content and master
  recordings"* from the add-back — so it does charge the content Sony spends most on, which is more
  honest than a raw EBITDA — but it adds back all PP&E depreciation, and I&SS is a fab business whose
  capex runs at D&A. **The switch:** the 5th plan (announced May 2024) replaced the EBITDA KPI with
  operating income growth and margin, and pay followed (FY3/26 KPIs: *"CAGR of operating income
  (continuing operations) and operating income margin (continuing operations)"*). **[E2-49]
  metric-switching does NOT fire**: the EBITDA yardstick was discarded while it was reading
  *favourably* (¥5.21tn against ¥4.3tn), toward a stricter measure, with reasons stated — the
  candor case the framework names. **But the metric survives in the public narrative:** every segment
  page of the FY2025 and Q1 FY2026 results presentations still charts "Adjusted OIBDA" beside
  operating income (e.g. I&SS FY3/26 Adjusted OIBDA ¥658.8bn against operating income ¥357.3bn).
  **Per the CGNX companion rule, the 8-K/6-K earnings release was read before this box was scored.**
- [ ] **filed-figure tells [E4-30]** — reported growth is not smooth (G&NS OI 346 → 250 → 290 → 415
  → 463; Pictures 217 → 119 → 118 → 117 → 105); income taxes paid ¥231.5bn / ¥308.4bn / ¥234.3bn
  against continuing pre-tax ¥1,095.1bn / ¥1,343.2bn / ¥1,422.4bn = 21.1% / 23.0% / 16.5%. **The FY3/26
  dip is a prompt**; the MD&A attributes the FY3/25 tax line to one-offs (capital repayment and a
  subsidiary dissolution reducing expense), and FY3/26 effective rate rose to 25.8%, so cash tax
  running below book tax in the spin-off year reads as timing, not the [E4-30] pattern of a falling share
  sustained over years. Recorded, not
  fired.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity, Sony without Financial Services
(the company's own separated balance sheet and income statement, Item 5 of each 20-F; FY3/26 is the
continuing-operations figure over total equity attributable, which now includes the 16.40% SFGI stake):

| | FY3/22 | FY3/23 | FY3/24 | FY3/25 | FY3/26 |
|---|---|---|---|---|---|
| Net income (¥bn) | 817.1 | 818.1 | 896.6 | 1,067.4 | 1,030.9 (continuing) |
| Equity, year-end (¥bn) | 4,341.1 | 5,156.1 | 7,062.7 | 7,695.5 | 8,119.0 |
| Return on average equity | 22.0% | 17.2% | 14.7% | 14.5% | 13.0% |

*Two scope limits stated rather than smoothed: (1) the "without FS" equity includes the parent's
investment in the FS subsidiary, so the denominator is not purely industrial; (2) equity rose partly on
translation: *"Exchange differences on translating foreign operations"* were +¥442.4bn, −¥79.3bn and +¥424.4bn
in FY3/24–FY3/26 (continuing, consolidated statements of comprehensive income, 20-F FY3/26).* **Direction:
falling every year**, ~22% to ~13%, on an equity base that nearly doubled — the incremental return on
the equity added is well below the average. Without undue leverage (net cash). [E2-43]'s unleveraged
net tangible assets cannot be built by segment (no segment assets, Q1).

**The half-owner test [E2-26]:** mixed, and specific. **Passes:** one-time items are quantified at
every line in the MD&A and presentations (Bungie ¥120.1bn, Peanuts remeasurement gain ¥34.7bn, land
realisation ¥43.9bn, SHM ¥44.9bn, Israel sale loss ¥19.9bn), in both directions — gains are named as
readily as losses. The separated "Sony without Financial Services" statements were published for years
precisely so an owner could see the industrial business apart from the insurer. **Fails in one place:**
the management OCF used for capital allocation *"does not include the impact of investments in major
music catalogs"* (FY2025 presentation, note *4), which are inside IFRS operating cash flow — the
company's own source-of-capital figure is higher than the audited line by the catalog spend, and the
reconciling amount is not printed on that page.

**The institutional imperative — score all four [E2-30]:**
- [ ] resists any change in current direction — **no**: the insurer was spun, TVs placed with TCL,
  the EV joint venture scaled down, Pixomondo wound down, Sony Semiconductor Israel sold.
- [x] projects/acquisitions materialise to soak up available funds — **prompt fires**: the 5th plan
  carries a standing *"strategic investment target of 1.8 trillion yen"* (unchanged when the OCF forecast
  rose ¥0.9tn — the increase went to buybacks), and *"approximately 1.0 trillion yen of strategic
  investments have been executed or determined already"*. A pre-set budget for acquisitions is the
  shape [E2-30](2) describes. The record inside it: **Bungie ¥510.5bn total consideration (July 2022),
  every non-goodwill asset written off in FY3/26 (¥120.1bn) with ¥193.8bn of goodwill still carried
  inside the G&NS CGU group; Sony Honda Mobility ¥44.9bn additional loss and EV launch cancelled;
  Pixomondo shut (¥27.1bn)**; against Crunchyroll (¥135.9bn, 2021, now 21M subscribers) and the music
  catalogs, which the Music margin supports.
- [ ] staff studies produced to justify the leader's craving — no evidence either way in the filings.
- [ ] peer behaviour mindlessly imitated — the Bungie rationale was *"access to Bungie's approach to
  live game services"* (20-F FY3/23, Note 30), bought in the year the whole industry bought live-service
  studios; recorded as a possibility, not scored, because the filing gives no evidence of imitation as
  the motive.

**Capital allocation — the buyback conditions [E5-08, E4-31]:**
- (1) ample funds for operations and liquidity? **Yes** — ¥2,208.9bn cash against ¥1,042.0bn of
  borrowings ex-leases at March 2026, CP programmes undrawn, *"no financial covenants"* (Item 5.B).
- (2) repurchases at a **material discount** to conservatively calculated IV? **Item 16E: 140,877,962
  shares in FY3/26 at an average ¥3,705.97**, the April–September 2025 tranches still carrying the
  SFGI shares that were then distributed; FY3/27 to August: 67,581,300 shares for ¥237.35bn = ¥3,512
  average (6-K 2026-09-03). **Against this run's owner earnings (Q4), ¥586bn–¥1,077bn across windows and
  both (c) ends = ¥100–¥184 per share, the buyback prices capitalise owner earnings at 2.7%–5.2%** —
  below the ~10% floor at every combination, below the JGB at the five-year window. **CAPITAL
  ALLOCATION FLAG**, with the humility clause **[E4-13]**: it rests on this run's owner-earnings
  range; *"They also know a whole lot more about them than I do"*, and *"infractions, even serious ones,
  are innocent; many CEOs never stop believing their stock is cheap"* **[E5-08]**. **Binds position
  size, never the discount rate.**
- (3) [E4-31]'s third condition — information supplied for estimating value: the separated statements
  and segment detail are generous; the missing segment assets (Q1) and the catalog-excluded OCF are the
  gaps.
- **Stock paper at IV [E5-44]:** no material stock-funded acquisition in the window (Bungie was cash plus
  retention payments).
- **Buybacks while borrowing:** US$1.0bn of senior notes issued June 30, 2026 (4.657% 2031, 5.089%
  2036; 6-K 2026-06-24) *"for general corporate purposes"*, in the same quarter the ¥500bn facility ran.
  [E4-50] licenses aggressive buying, borrowing included, at a true discount; the discount does the licensing, and condition (2) is the flag above.

**Pay and incentives [E4-27].** *(The brief cited [E4-52] for pay; in the ledger [E4-52] is the
lollapalooza row, not pay. The incentive row is [E4-27].)* CEO Hiroki Totoki FY3/26: fixed ¥240M,
business-results ¥371M, stock options ¥708M (grant-criteria amount), RSUs ¥1,062M + ¥96M, plus ¥278M
recorded for the spin-off value adjustment to prior grants (20-F Item 6). The bonus KPIs are OI CAGR and
OI margin **plus a "Group Sustainability Evaluation"**; the FY3/26 results *"each exceeding the targeted
range"*. **The KPI pays on operating income, which includes the one-off remeasurement and land gains
named above (¥78.6bn together) and excludes the capital used to earn it** — nothing in the pay formula
charges for the ¥1.8tn strategic budget or the buyback price. [E4-27]: the incentive points at growth
in reported profit, not at owner earnings per share. A prompt, not a finding.

**Foreign jurisdiction [E3-66].** Japanese company law; the 20-F describes shareholder rights under
the Companies Act, dividends and buybacks by board resolution under Article 459 and the articles, no
pre-emptive rights, and the board able to issue treasury stock *"at such times and upon such terms as
the Board of Directors or the CEO determines"* short of a special-resolution threshold. A US-listed ADR
holder stands behind the Tokyo register. Item 7: *"To the knowledge of Sony Group Corporation, it is not directly
or indirectly owned or controlled by any other corporation, by any foreign government or by any other natural or
legal person"*; the largest bulk holding report is BlackRock Japan and joint holders, 8.53% (December 5, 2024).

**THE GUARDRAIL — check before writing the verdict.**
- [x] Confirmed: nothing in this Q3 is used to **promote** the name **[E2-37, E2-38, E3-39]**. The
  portfolio actions (spin, TCL, SHM) are rational pruning, and they cannot repair Q2 or substitute for Q4.
- [x] **Key-person dependence** is not the Q2 finding here; no leg's profit is attributed in the filings
  to one person **[E4-23]**.
- [x] Is a great manager the reason to act? **No** — no one proposes the manager as the plan
  **[E2-35, E2-36]**.

- **VERDICT: [x] IN (no integrity disqualifier found)** — with two live flags (projection culture,
  historic EBITDA-pay; both read and scored as prompts), one live **capital-allocation flag** (buybacks
  above conservatively calculated value) and one acquisition record with a full write-off (Bungie).
  *IN = no disqualifier found, not a finding that the managers are honest [E5-17]. IN never promotes.*

## Q4 — WILL IT SURVIVE?

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business).
*Recorded because the operator's instruction requires a price, and a price needs owner earnings; and
because the brief asks for owner earnings by window and both (c) ends. Nothing below reopens Q2.*

### Owner earnings — the one number **[E2-23]**

**The perimeter rule applied (the CNR rule): no mean crosses the October 1, 2025 spin-off.** Every
year below is on the **non-financial perimeter**. Source by year:
- **FY3/24, FY3/25, FY3/26 — audited IFRS "continuing operations"** (FY3/26 20-F cash-flow statement:
  *"Total net cash provided by operating activities from continuing operations"* ¥1,103,645M /
  ¥1,971,349M / ¥1,966,292M).
- **FY3/21, FY3/22, FY3/23 — the unaudited "Sony without Financial Services" condensed cash-flow schedule**
  (Item 5 of the FY3/22, FY3/23 and FY3/24 20-Fs), **rebuilt onto the continuing basis** by removing the
  one intra-group flow the two bases treat differently: the Financial Services segment's dividends to the
  parent (FS column *"Dividends paid"* ¥30,454M / ¥39,159M / ¥41,335M), which the "without FS" schedule
  counts and continuing operations eliminates. The company's own reconciliation note: *"The difference in
  results of Continuing Operations and results of 'Sony without Financial Services' is the amount
  equivalent to intersegment transactions between the Financial Services segment and other segments, and
  such difference is immaterial. This difference also applies to operating cash flows"* (FY2025 results
  presentation, 6-K 2026-05-08).
- **The splice was measured, not assumed, in the two overlap years:** FY3/24 without-FS ¥1,177,828M less
  FS dividend ¥50,037M = ¥1,127.8bn against continuing ¥1,103.6bn — **residual ¥24.1bn (2.2%)**; FY3/25
  ¥1,972.4bn against ¥1,971.3bn — residual ¥1.1bn. The FY3/24 residual is stated, not smoothed; it is
  inside the rebuilt years' error bar in the direction of *overstating* them by up to ~2%.
- **The insurer's cash flows are nowhere in this series.** The retained 16.40% SFGI stake (equity method
  from October 2025) is excluded from owner earnings and noted as an asset in Q5 [E3-04 is not applied to
  it: its earnings are an insurer's, and the sector method would be required].

**Content and film costs — where they are, and how treated.** Note 27(1): *"Sony classifies the cash
flows from the additions, except for additions from purchases of businesses and other, and disposals of
content assets as cash flows from operating activities"* — so **film, TV, broadcasting-rights, music-catalog,
artist-advance and game-content spending is already deducted inside operating cash flow** (*"Increase in
content assets"* ¥(486,183)M / ¥(683,388)M / ¥(665,894)M, FY3/24–26). **And "Depreciation and amortization"
in the cash-flow statement includes content amortization** (Pictures segment D&A ¥517.8bn in FY3/26 against
film-cost and broadcasting amortization of ¥475.6bn in the content note). **Consequence for (c): the D&A
default must exclude content amortization, or content is charged twice** — once as cash in OCF and again
as the (c) proxy. Content amortization by year (content-asset note): ¥293.2bn · ¥400.9bn · ¥510.1bn ·
¥571.0bn · ¥535.8bn · ¥595.2bn (FY3/21–26). **Catalog purchases made directly (not through acquisitions)
also sit in OCF** — *"The consideration for the content assets (music catalogs) directly acquired from
other rights holders was 84,382 million yen, which was recorded in cash flows from operating activities"*
(FY3/25) — and management's own capital-allocation OCF *"does not include the impact of investments in
major music catalogs"*. **This run leaves them in** (a growth outlay charged as if it were maintenance,
the conservative direction); net music-catalog growth (additions less amortization) averaged ~¥44bn a year
over FY3/22–26 and is carried as width, not added back.

**IFRS leases.** Lease principal is a financing outflow under IFRS 16, so OCF is flattered by it. The
capex end of (c) adds lease cash (*"Payments of lease liabilities"* FY3/24–26; *"Net cash outflows for
leases"* ¥81.4bn / ¥83.5bn / ¥89.7bn for FY3/21–23, which includes interest and a small FS share —
over-deducting by <¥10bn a year, the conservative direction). The D&A end carries ROU depreciation
inside D&A as the lease charge.

**Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT [E3-44, E2-41].** Which case: **the
default applies, with the band carried.** Capex plus lease cash exceeded D&A-ex-content in four of the
five default-window years (mean ¥628.8bn against ¥519.8bn), and the excess is mostly labelled growth by the
filer — I&SS *"approximately 246.7 billion yen to increase image sensor production capacity"* (FY3/26),
*"227.4 billion yen"* (FY3/25) — **not** a statement that depreciation understates renewal, which is what
[E5-20]'s exception class requires. **The D&A end is therefore not INVALID, but it is the optimistic end:**
I&SS renews by node, and a node is a capacity decision and a renewal decision at once. The conservative
end, total capex plus leases, is carried beside it.

**Stock compensation subtracted in full [E5-06] — RESOLVES and is COMPLETE for every year:** Note 21,
*"The stock-based compensation expense for the fiscal years ended March 31, 2024, 2025 and 2026 was 21,657
million yen, 29,416 million yen and 39,102 million yen"*; FY3/21–23 from SEC XBRL
`ifrs-full:ExpenseFromSharebasedPaymentTransactionsWithEmployees` ¥8,892M / ¥11,105M / ¥15,781M (these
include the FS segment's small share; subtracting it is conservative). SBC is 1–4% of OCF, so [E3-70]'s
grant-date measure would not move a verdict; not rebuilt.

**Owner earnings by year, ¥bn** (`_research 2026-09-13 SONY/oe.py`; every input is a filed figure named
above):

| | FY3/21 | FY3/22 | FY3/23 | FY3/24 | FY3/25 | FY3/26 |
|---|---|---|---|---|---|---|
| OCF, non-financial perimeter | 1,119.8 | 774.1 | 374.1 | 1,103.6 | 1,971.3 | 1,966.3 |
| − SBC | 8.9 | 11.1 | 15.8 | 21.7 | 29.4 | 39.1 |
| (c) D&A-ex-content | 370.3 | 409.4 | 468.1 | 546.3 | 589.8 | 585.5 |
| (c) capex + lease cash | 540.1 | 504.1 | 680.0 | 696.6 | 719.9 | 543.6 |
| **OE at the D&A end** | 740.6 | 353.6 | **−109.8** | 535.7 | 1,352.2 | 1,341.7 |
| **OE at the capex end** | 570.8 | 258.9 | **−321.6** | 385.4 | 1,222.0 | 1,383.6 |
| *working-capital lines (receivables + inventories + payables)* | *+61.4* | *−222.6* | *−735.8* | *−188.2* | *+533.2* | *+350.0* |

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38].**

| Window | OE at the capex end | OE at the D&A end | mean OCF |
|---|---|---|---|
| **5-year default, FY3/22–FY3/26 [E2-42]** | **¥585.6bn** | **¥694.7bn** | ¥1,237.9bn |
| 6-year, FY3/21–FY3/26 | ¥583.2bn | ¥702.3bn | ¥1,218.2bn |
| 5-year ending before the spin year, FY3/21–FY3/25 | ¥423.1bn | ¥574.5bn | ¥1,068.6bn |
| **3-year, audited continuing only, FY3/24–FY3/26** | **¥997.0bn** | **¥1,076.5bn** | ¥1,680.4bn |

- **Combined range (window spread × capex band): ¥423bn to ¥1,077bn; on the default window and the
  audited window, ¥586bn to ¥1,077bn.** The high end is 84% above the low end.
- **Is that range too wide to reach a conclusion?** For a **valuation**, nearly — the top is 1.8x the
  bottom **[E4-25]**. For **this price** it is not: every end of it capitalises at 2.0%–5.1% of the ¥21.2tn
  cap (Q5), all below the ~10% floor, so the conclusion is the same at both ends and no preference was
  needed to reach it.
- **The distorted years, named [E5-11]:** **FY3/23**, a ¥560.4bn inventory build (*"(Increase) decrease in inventories"*, without-FS schedule; the filing does not split it by segment) that
  took OE below zero at both ends; **FY3/25–FY3/26**, the release of that working capital (+¥533.2bn and
  +¥350.0bn), which is why the audited three-year window is the high one. **[E4-41] normalises down for
  favourable breaks:** the three-year window contains the release and not the build, so it is flattered;
  the five-year window contains both and nets the working capital to −¥263bn. Management's own FY3/27
  operating-cash forecast is **¥1,500bn, "-24%"** (FY2025 and Q1 FY26 presentations) — a forecast, not
  used as a figure, but it points the same way. **The five-year default is the honest centre; the
  three-year window is carried as the top of the range, not its middle.**
- **Two more perimeter facts inside the window, stated so they are not mistaken for trend:** FY3/26
  capex fell to ¥457.7bn (from ¥621.0bn) as I&SS capacity spending moved toward the TSMC joint venture —
  the capex end is flattered in that one year; and the ET&S Displays business is being placed with TCL
  (signed, not closed).

**Segment-level owner earnings: not computable from the filings, and a cash proxy instead.** Segment capex
is not disclosed except I&SS; segment working capital and tax are not disclosed at all. **COMPUTATION —
segment cash proxy, pre-tax, before non-content capex and working capital (`segcash.py`), ¥bn:**

| Segment | FY3/25 proxy (OI) | FY3/26 proxy (OI) | construction |
|---|---|---|---|
| Music | 268.6 (357.3) | 355.9 (447.0) | OI + catalog/artist/distribution amortization − those additions |
| G&NS | 398.7 (414.8) | 501.2 (463.3) | OI + game-content amortization and impairment − game-content additions |
| Pictures | 17.0 (117.3) | **0.9** (104.9) | OI + film/broadcasting amortization − those additions |
| I&SS | ≈ OI (261.1) | ≈ OI (357.3) | additions to long-lived assets ¥265.3bn ≈ segment D&A ¥265.1bn (FY3/26) |
| ET&S | n/c | n/c | no segment capex or content figure |

*These are not owner earnings and are not summed; they show where the cash is: Music and G&NS convert
profit to cash; Pictures, on this measure, did not in the last two years.*

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [x] **good, for the whole, with a gruesome-leaning leg inside** · [ ] gruesome
- Evidence: five-year OE ¥586–695bn on average Sony-without-FS equity of ~¥6.5tn is **~9–11%**; the
  FY3/26 year, ¥1,342–1,384bn on ¥8.1tn, ~17%, is the working-capital release year. Growth has required
  capital beyond (c): **¥1,240bn of "Payments for purchases of businesses and other" and ¥656bn of
  "Payments for investments and advances" over FY3/22–26**, plus the I&SS capacity programme and a ~¥465bn
  joint-venture contribution ahead. **[E4-43]: the good class passes Q4** — capital-hungry growth *"may
  well prove to be a satisfactory investment"* — but the return on the equity that growth added is falling
  (Q3: 22.0% → 13.0%), and Pictures' two-year cash proxy of ¥18bn on ¥222bn of reported profit is the
  gruesome account in miniature: money added at returns that do not show up as cash.

### Staying power — score all three **[E5-11]**
- **(1) large and reliable stream of earnings — PARTIAL.** Large: five-year mean OCF ¥1.24tn. Reliable: no
  — OCF ranged ¥374bn to ¥1,971bn inside five years on working capital alone, and three of five legs are
  hit- or cycle-driven.
- **(2) massive liquid assets — PASS.** Cash and equivalents **¥2,208.9bn** (March 31, 2026); CP programmes
  of ¥1,299.3bn undrawn; committed lines ¥789.6bn unused (Item 5.B).
- **(3) no significant near-term cash requirements — PASS, with commitments named.** Short-term borrowings
  ¥51.2bn and current portion of long-term debt ¥166.4bn (¥217.6bn together, 10% of cash); Note 32 purchase
  commitments of ¥941.5bn in total — PP&E and intangibles ¥85.0bn, Music artist and songwriter contracts
  ¥342.2bn, Pictures talent and rights ¥184.7bn, G&NS game contracts ¥33.7bn, materials ¥78.1bn, IT services
  ¥217.8bn — spread *"mainly within four years"* and three years, i.e. the running cost of the content legs,
  covered by one year's operating cash; the TSMC joint-venture contribution of ~¥465bn
  is *"in phases based on market demand"* and partly an asset transfer; the ¥500bn buyback facility and
  the ~¥204bn dividend (¥35 × ~5.84bn shares, planned FY3/27) are discretionary. Nothing contractual is
  large against cash.
- **Leverage, named and quantified [E4-16, E3-29]:** borrowings ex-leases ¥1,042.0bn (short-term ¥51.2bn,
  current long-term ¥166.4bn, long-term ¥824.4bn) plus lease liabilities ¥627.7bn, against cash ¥2,208.9bn:
  **net cash ¥1,166.9bn ex-leases, ¥539.2bn including leases** (the company's own figure: *"Net Cash
  Position"* ¥539.2bn, FY2025 presentation). US$1.0bn of notes added June 30, 2026. *"there are no
  financial covenants in any of Sony's material financial agreements with financial institutions that
  would cause an acceleration of the obligation"* (Item 5.B) — **[E3-52]'s covenant-free class.**
  **Coverage [E2-54]:** interest paid from continuing operations ¥16.5bn (FY3/26, Note 27(2)) against
  five-year OE of ¥586bn+ at the capex end — **over 35 times**, after capex.
- **Jurisdiction [E3-66]:** recorded at Q3 — Japanese Companies Act; no controlling shareholder; the ADR
  holder stands behind the Tokyo register.

### Name the specific way THIS business dies **[E2-27, E3-24]**
**The registered shapes, tested:** ORCL (contracted not to stop) — no; ARM (earns nothing for owners after
paying its people) — SBC is 1–4% of OCF; BE (too little history) — six years rebuilt; BA (spends cash
undoing past work) — no; SWK (dividend by selling the business) — the SFGI dividend in kind was a
distribution *of* a business, but it was a separation, not a funding source for the payout; ACVA/FLNC/NEGG
(the borrowed balance sheet) — no, net cash; CNR (the long tail on a short cycle) — no long claims; RGTI
(the equity is the revenue) — no, buying back; BAM (the warehouse: its balance sheet lent to its own funds' deals, with
distribution above owner earnings) — no warehouse; **but its second feature is partly present and is recorded [E2-60]:** cash
distributions were ¥657bn in FY3/26 (dividends ¥135.0bn, buybacks ¥522.1bn) and are planned at up to ~¥704bn
for FY3/27 (¥35 a share, ¥500bn facility) — at or above five-year owner earnings (¥586–695bn), below the
three-year figure (¥997–1,077bn); funded from the working-capital release and net cash, with US$1.0bn of
notes in June 2026 the one borrowed element. **None of the nine fits. A TENTH SHAPE, NAMED: THE CAMOUFLAGE.** A
conglomerate that does not die; its **owner's return** dies, because the cash of two franchise legs is
recycled into legs that must re-win a race every cycle — the fab node, the film slate, the console
generation's first-party hits, the studio acquisition — and the consolidated series hides the rate earned
on the recycling **[E2-56]**. It is the 1985 letter's *"after each round of investment, all the players had more
money in the game and returns remained anemic"* **[E2-27]**, run inside one company instead of across an
industry.

- **The mechanism, quantified from filed figures:** return on equity (Sony without FS) **22.0% → 17.2% →
  14.7% → 14.5% → 13.0%** while equity rose from ¥4.34tn to ¥8.12tn; over the same five years
  **¥1.90tn** went to acquisitions and investments outside (c), including **Bungie (¥510.5bn total
  consideration, July 2022; every non-goodwill asset written off, ¥120.1bn, FY3/26)**, Sony Honda Mobility
  (¥44.9bn additional loss, EV launch cancelled), Pixomondo (shut, ¥27.1bn) and Sony Semiconductor Israel
  (sold at a ¥19.9bn loss); **the next call is filed: ~¥465bn into the image-sensor joint venture, volume
  production 2029**. **Outcome if the pattern holds:** owner earnings grow more slowly than the equity
  retained to produce them, the buyback runs above value (Q3), and the per-share return converges on the
  incremental rate **[E3-17]** — not a loss of capital, a loss of compounding.
- **The acute exposures, modelled as exposure not experience [E4-40]:** (a) **the Kumamoto fabs** — the
  Q1 FY26 presentation: the Kumamoto Technology Center *"suspended production immediately after the
  earthquake"* (July 28, 2026), impact *"difficult to reasonably estimate"* — I&SS is 23% of FY3/26
  segment profit and its fabs are concentrated in one seismic region (*"several semiconductor facilities
  located in Kumamoto prefecture and neighboring prefectures"*); a year of I&SS profit lost is ~¥357bn
  pre-tax, **~2–3% of the ¥21.2tn cap, covered 6x by cash**; (b) **a console generation missed** — G&NS
  margin fell to 6.8–6.9% for two years in the last transition; a repeat at FY3/26 sales is ~¥140bn of OI a
  year below FY3/26 for two to three years; (c) **the memory-price surge** already named at G&NS, ET&S and
  I&SS; (d) **generative AI diluting catalog value**, filed by WMG and litigated by the majors.
- **Likelihood:** insolvency — **not a real possibility on the filed balance sheet**; the camouflage —
  **a real possibility**, and on the ROE series, **already in progress**; each acute exposure — **a
  low-level possibility** of permanent damage, a real possibility of a lost year.
- **The bear case its holders would accept as fairly stated [E4-51]:** *"Sony is two excellent businesses
  paying for three races, and the scoreboard for the races is the return on equity, which has fallen every
  year the races have been run."* **The bull's reply, also stated:** the perimeter is being pruned
  (insurer, TVs, EVs, Pixomondo, Israel), and the next five years' ROE could turn if the pruning continues;
  that is a claim about a future perimeter, and Q6 records it as a reopening condition.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival** — it survives: two of three strengths pass,
  the third is partial, and leverage is net cash with covenant-free debt. **The owner-earnings range is
  wide [E4-25] but not verdict-changing at this price.** The named way it dies is the owner's return, not
  the company. Neither finding governs; Q2 closed the file.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is **OUT**. The file is closed. What follows is
the operator's required price, headed as operator rule 3 requires, and it carries no entry language.

---
## COMPUTATION — NOT A CLEARANCE

### THE PRICE AND THE PASS/FAIL LINE (the operator's instruction of 2026-09-01)
- **Price: ¥3,632** (6758.T close 2026-09-11, Yahoo — aggregator, live quote only, flagged). ADR
  **$23.90** (same date, same flag), 1 ADS = 1 share.
- **Shares: 5,843,334,871** (July 2026 Share Buyback Report treasury count, 6-K 2026-08-12
  `0001104659-26-094573`, walked through August by hand; Step 0). No split after the measurement date;
  the October 1, 2024 five-for-one split is already in the count and the price.
- **Market cap: ¥21,223bn (≈ ¥21.2 trillion).** Sovereign: **JGB 30-year 3.995%, Japan MOF, 2026-09-10.**
- **PASS/FAIL: FAIL — the file closed at Q2, OUT on the business** (Q1 IN; Q2 OUT; Q3 IN and Q4 IN
  recorded, not governing).

### What the buyer is paying for, in words
Two narrow franchises — a 23%/25% share of the world's recorded music and song copyrights, and the
PlayStation toll on a flat 125 million monthly accounts — joined to an image-sensor fab race, a film and
TV studio, and a consumer-electronics business, **at a price that capitalises the five-year owner earnings
at 2.8%–3.3%, below the 30-year JGB, and the flattered three-year owner earnings at 4.7%–5.1%.** To earn the
~10% the corpus quits at **[E4-28]**, the buyer needs yen owner earnings to grow **about 5%–7% a year in
perpetuity** from here.

### 1. THE YIELD
| Owner earnings (Q4) | ÷ cap ¥21,223bn | per share | points over the JGB 3.995% |
|---|---|---|---|
| 5-yr default, capex end ¥585.6bn | **2.76%** | ¥100 | −1.24 |
| 5-yr default, D&A end ¥694.7bn | **3.27%** | ¥119 | −0.72 |
| 3-yr audited, capex end ¥997.0bn | **4.70%** | ¥171 | +0.70 |
| 3-yr audited, D&A end ¥1,076.5bn | **5.07%** | ¥184 | +1.08 |
| 5-yr pre-spin-year, capex end ¥423.1bn | 1.99% | ¥72 | −2.00 |

*Not netted, and why:* net cash ex-leases ¥1,166.9bn at March 31, 2026 (≈5.5% of cap; since reduced by
¥237bn of buybacks and a ¥73.8bn dividend and raised by US$1.0bn of notes); the retained 16.40% SFGI stake
(≈ ¥187bn at the spin-date fair value implied by the ¥955,700M dividend in kind for the 83.60% distributed —
arithmetic, not a mark); listed stakes in other financial assets (Spotify, Bandai Namco, KADOKAWA named in
the 20-F; not valued here). Netting all of them would lift each yield by roughly a tenth of itself — 2.76%
becomes ~3.1% — and moves no conclusion.

### 2. WHAT THE PRICE ALREADY ASSUMES
- **Perpetual growth in owner earnings needed for a ~10% expectancy** (yield + growth, the engine
  **[E3-34]**, casting no vote): **7.2% / 6.7%** from the five-year base; **5.3% / 4.9%** from the three-year
  base.
- **What the business has actually done:** segment operating income on the non-financial perimeter
  ¥1,160.9bn (FY3/22, total less Financial Services) → ¥1,456.4bn (FY3/26), **5.8% a year in yen** — across
  a period when the average dollar went from 112.3 yen (FY3/22) to 150.7 yen (FY3/26) (MD&A, each 20-F) — a
  weaker yen, so an unmeasured and possibly large part of the yen growth is translation; owner earnings themselves have no usable growth rate (negative in FY3/23).
- **[E4-35]'s base rate:** fewer than one in twenty of the best businesses sustain double-digit growth; the
  requirement here is mid-single-digit, which is not the long shot — **but it is required from a business
  whose return on retained equity has fallen every year (Q3), and [E4-44] caps value growth at earnings
  growth.** What bounds the upside **[E2-63]**: music streaming penetration and price, the PS6 cycle, and
  the share of I&SS the TSMC joint venture leaves with Sony's owners.

### 3. WHAT YOU ARE PAID
**−1.2 to +1.1 points over the JGB**, on the owner-earnings range. **No per-name premium was added to
the rate [E3-42].**

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01] — engine display, no vote
- Capitalised at the ~10% floor with **no growth**, plus March-2026 net cash ex-leases: **roughly
  ¥1,200 to ¥2,050 a share** (five-year to three-year owner earnings).
- At the floor **with 3% perpetual growth** (a stated assumption, not a finding): **roughly ¥1,650 to
  ¥2,850 a share.**
- **Current price ¥3,632 — above the whole range on both constructions.**

### THE FLOOR, THEN THE RANKING [E4-28, E4-21]
- Honest pre-tax expectancy at this price: **~3% to ~5% plus whatever growth the owner earnings deliver** —
  below ~10% unless growth of 5%–7% a year is assumed in perpetuity. **Below the floor: quit on, not ranked.**
- **Bar: screamer test [E4-01]** — the price is above the whole range, including the three-year window the
  run calls flattered. **No.** **Windage count: one** — the capex end of (c); the window spread is carried
  as range, not as a second margin. No end margin is applied because no entry is under consideration.
- **Price at which the floor would be met, if Q2 were ever reopened** (recorded in words; no alert armed —
  a Q2 failure is a business failure, per the QLYS ruling of 2026-09-07): **a cap of ¥5.9–6.9tn on five-year
  owner earnings, ¥10.0–10.8tn on three-year — roughly ¥1,000–¥1,850 a share before net cash.**

- **VERDICT: not reached — the file closed at Q2. This block is a computation, not a clearance.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

### ⚠ RECORDED, NOT GOVERNING — nothing is owned and nothing is armed.
**Pre-committed [E1-02] — what would make Q2 worth re-running (the reversal conditions, in words):**
1. **Perimeter.** The profit and the capital move into the franchise legs: I&SS deconsolidated or
   separated (the TSMC joint venture is planned as a *consolidated* subsidiary, which does not qualify),
   Pictures and ET&S shrinking to the point that Music and G&NS are the overwhelming share of segment profit
   AND of the capital spent — the HAS condition, not a forecast of it.
2. **Direction.** Return on equity on the continuing perimeter rising for three consecutive filed years
   **[E4-32]**, with the rise not explained by working-capital release **[E4-41]**.
3. **G&NS units [E4-55].** Monthly active users growing through the next console transition, and the
   transition passing without the 6.8%–6.9% margin trough of FY3/23–FY3/24.
- **Thesis-breaking for the OUT verdict** (what would show it was wrong): segment disclosure showing I&SS
  and Pictures earning high returns on filed segment capital over five years; or a Sony price statement for
  PlayStation Plus or hardware with flat volume **[E2-44]**, which would lift G&NS from NARROW.
- **Next catalysts:** the August 2026 Share Buyback Report (≈ mid-September, completes the share count);
  Q2 FY3/27 results (≈ early November 2026) — the first filed read on the **Kumamoto earthquake** damage;
  closing of the TCL partnership and of the TSMC joint venture; the FY3/27 20-F (≈ June 2027), the first
  full year on the new perimeter and the first year of four audited continuing years.

**The sell rule [E2-28]** — not applicable; no position. **The monitoring question [E3-30, E4-17]:** is the
falling return on equity an aberrational cycle (the PS5 ramp, the spin-off year) or a permanent slippage
from recycling franchise cash into races? The next two filed years separate them.
**Position size:** none. **[E5-14]** not engaged.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN** — the reopening conditions are written, dated and
  falsifiable; no band is armed and no PORTFOLIO row is added (FOLD step 4, gate-clearers only).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 OUT (closes); Q3–Q6 recorded under
      explicit "RECORDED, NOT GOVERNING" banners; the price under COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's capital-proxy limit is
      a filer disclosure limit stated as such; Q2's missing peer figures are named and shown not
      load-bearing, so no class is held PROVISIONAL.
- [x] Every UNRESEARCHED verdict names the artifact — none used.
- [x] Every UNKNOWABLE verdict states what cannot be known — none used.
- [x] Step 0: the 20-F was read (MD&A, cash-flow statement with detail lines, Notes 4, 8, 11, 12, 20, 21,
      26, 27, 32, 33 and the sections of Items 3–8 and 16E cited at each gate), accession `0001193125-26-274893`; FY3/22–FY3/25 20-Fs read for the
      separated schedules, segment and content notes; cross-check: consolidated OCF FY3/25 ¥2,321,675M,
      XBRL = filed statement.
- [x] Owner earnings on multi-year means; four windows stated; both (c) ends; (c) disclosed as a judgment
      with the default and why the exception class does not apply; **content amortization excluded from the
      D&A end to avoid double-counting content already inside OCF**; SBC resolves and is complete for all
      six years; **no mean crosses the spin-off perimeter** (rebuilt, splice residual measured).
- [x] Competitor rows filled for four segments (12 peers), same-metric limits stated, the fifth (ET&S)
      failing on the subject's own filing with the absence stated.
- [x] Sovereign for the earnings currency (JPY, argued, with the ~90% foreign-sales fact stated and USD
      shown), from the issuing authority (MOF), dated 2026-09-10; tenor 30Y.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar (screamer); windage count stated: one.
- [x] Prices dated; aggregator used for live quotes only and flagged.
- [x] Ledger ids checked against `principle_ledger.csv` before citing (every id cited exists). **Brief defect
      recorded:** the brief cited [E4-52] for pay; [E4-52] is the lollapalooza row; the incentives row
      [E4-27] was used.
- [x] Run committed to git with a pathspec, section by section (Step 0, Q1, Q2–Q3, Q4, Q5–Q6/fold).

**Errors caught in this run before commit, recorded rather than hidden:** a first draft of Q3 summed the
4th-plan KPI with a year of Adjusted OIBDA (¥1,816.9bn) instead of Adjusted EBITDA (¥1,797.6bn) — corrected
to ¥5,213.5bn; a first draft attributed the 1985 letter's "more money in the game" line to Munger —
corrected; a first draft named an audit firm from memory — replaced by the filed PCAOB ID; a first draft
attributed the FY3/23 inventory build to two segments the filing does not name — removed. **And one error that reached history:** commit `67c60e1`'s message calls THE CAMOUFLAGE the "ninth" survival shape; BAM's run had already named a ninth (THE WAREHOUSE), so it is the **tenth**, corrected in this file before the fold and left standing in the commit message (operator rule 6).

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Sony Group is two narrow franchises (Music, PlayStation) inside a five-leg conglomerate whose
  other three legs — image sensors, pictures and electronics, ~45% of five-year segment profit and its
  largest capital programme — are not franchises, and whose return on equity has fallen five years running;
  Q2 OUT on the business as constituted. Price ¥3,632 × 5,843,334,871 = ¥21.2tn, capitalising five-year
  owner earnings of ¥586–695bn at 2.8%–3.3% against a 4.00% JGB and a ~10% floor (COMPUTATION — NOT A
  CLEARANCE).
- **The strongest single fact against this conclusion:** the publishers' own 10-Ks — *"Many key commercial
  terms of our relationships with Sony and Microsoft … are determined unilaterally"* (EA) and *"Sony may
  terminate the agreement for any or no reason upon 30 days' notice"* (Take-Two) — combined with Microsoft's
  console hardware revenue falling 25% and 29% in consecutive years: the PlayStation toll may be widening
  into a near-duopoly faster than the conglomerate discount in this verdict allows, and G&NS plus Music were
  already 59.5% of FY3/26 segment profit.

