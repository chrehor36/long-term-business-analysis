# Company Run — Honda Motor Co., Ltd. (HMC) — 2026-09-13
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
later section is appended as it closes. The brief was read as a set of hypotheses to refute; it named
no expected verdict and none is assumed here. Every fact the brief supplied was re-derived from
Honda's own filings below; the one it got right and the two places it was incomplete are marked.
**Two prior mentions of Honda in this tree are context only, not inherited:** the GM run of
2026-09-01 put Honda in its competitor row (automobile segment (9.96)%, motorcycles 18.21% / 18.29%,
EV losses ¥1,577,805M) and the concurrent TM run is writing now. Every Honda figure used here is
re-read from Honda's own documents.*

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 3.995% (≈4.00%) · JGB 30-year · date 2026-09-10 · source: Japan Ministry of Finance, official
  JGB curve `jgbcme.csv`, struck fresh this run through `python tools/sources.py`**
  (`sovereign('JPY')` returned `(3.995, '2026-09-10', 'Japan MOF official JGB curve')`). Tenor 30Y, the
  tenor of every JPY run in this tree (MITSY 2026-08-28, SONY 2026-09-13). The brief's ≈4.00% is
  confirmed to rounding.
- **USD shown for sensitivity only: 5.35%, 30-year, 2026-09-11, US Treasury daily par yield curve**
  (`sovereign('USD')`, the issuing authority, not the FRED fallback).
- **Where Honda earns, from the filing.** Sales by customer location, FY ended 2026-03-31 (20-F Item 4.B
  table; Consolidated Financial Summary 1): **Japan ¥2,536.9bn of ¥21,796.6bn = 11.6%**; North America
  ¥12,578.8bn (57.7%); Asia ¥4,094.8bn (18.8%); Europe ¥1,005.5bn (4.6%); other ¥1,580.4bn (7.3%).
  **88.4% of sales are earned outside Japan.** Operating profit by location of the company (20-F Item 5,
  "Geographical Information Based on the Location of the Company and Its Subsidiaries"): FY3/25, the last
  year without EV write-offs, **Japan ¥191.1bn of ¥1,217.8bn = 15.7%**, North America ¥435.2bn (35.7%),
  Asia ¥408.3bn (33.5%), other ¥177.9bn (14.6%), Europe ¥5.3bn; FY3/26, **Japan (¥765.0bn) and North
  America (¥227.3bn) both losses**, Asia +¥352.5bn, other +¥214.0bn, Europe +¥15.8bn. **Roughly 84% of
  pre-write-off profit is earned outside Japan**, and in the motorcycle segment ~85% of group units are
  sold in Asia (Item 4.B: *"approximately 85% of Honda's motorcycle units on a group basis were sold in
  Asia"*).
- **Why JPY anyway — argued, not defaulted.** [E4-15] makes the rate a gravity on the value of the
  claim; the claim a Tokyo shareholder holds is **denominated, reported, paid and priced in yen**: the
  statements are in yen, the ¥70 dividend is declared in yen (FY3/26 actual and FY3/27 forecast, results
  6-K 2026-05-14), the ¥1.1tn buyback was paid in yen, and the quote used below is the Tokyo quote in yen.
  **[E3-32] forbids a view on rates, and choosing the dollar rate because the profit is American would be
  a view on which currency's rate the owner will one day be paid in.** The foreign earning base is
  therefore carried as **width in the yen owner-earnings figure** (it moves with the dollar and the rupee),
  not as a second rate — the MITSY and SONY precedent, argued again here on Honda's own mix, which is more
  foreign than Sony's. **And the choice cannot change a verdict at Q5:** the ~10% floor [E4-28] holds
  *"whether short rates are 6 percent or whether short rates are 1 percent"*, above both 4.00% and 5.35%.
- **FX, quote vs earnings: none needed.** The cap is taken **in yen from the Tokyo quote (7267.T)**, so cap
  and yen owner earnings share a currency by construction. **The USD ADR is never used for the cap.**
- **ADR ratio, from the filing:** 20-F cover, *"American Depositary Receipts evidence American Depositary
  Shares, each American Depositary Share representing three shares of Common Stock"*; repeated in the
  results 6-Ks (*"One American Depositary Share represents three common shares"*). Derived check: HMC
  $32.52 and 7267.T ¥1,664, both 2026-09-11 close (Yahoo, **aggregator, live quotes only, flagged**) →
  ¥1,664 × 3 ÷ $32.52 = **¥153.5/$**, a plausible spot for the date, consistent with 1 ADS = 3 shares.
  Cover: 222,860,406 of the shares are represented by ADSs (5.7%).

**THE SHARE COUNT — by hand (a 20-F filer: `cover_shares.py` cannot see a 6-K, RESUME STATE §5).**
1. **20-F cover, "as of the close of the period covered", March 31, 2026: Common Stock 3,892,580,441**,
   with the footnote *"'outstanding shares' excludes the number of shares held by the BIP Trust"*.
   Cross-check, results 6-K 2026-05-14 (`0001193125-26-222672`): issued **4,533,000,000**, treasury
   **640,419,559** → 3,892,580,441. **Exact match**, which shows the TDnet treasury figure includes the BIP
   and ESOP trust shares.
2. **The cancellation inside the year:** issued fell 5,280,000,000 → 4,533,000,000 (747,000,000 cancelled;
   statement of changes in equity, "Cancellation of treasury stock ¥1,046,188M"). **Cancelling treasury
   stock does not change the outstanding count.**
3. **Latest filed count: Q1 FY3/27 results, 6-K filed 2026-08-05 (`0001193125-26-333722`): "As of June 30,
   2026 | 4,533,000,000 shares" issued; treasury "639,983,417 shares" → outstanding 3,893,016,583**
   (treasury fell 436,142, trust deliveries to officers).
4. **No repurchase is running.** The ¥1.1tn programme announced 2024-12-23 was *"completed September
   2025"* (20-F Item 16E; 453,777,400 shares bought in FY3/26 at an average ¥1,476); **no "Status of
   Acquisition of Own Shares" 6-K has been filed since the 2025-09-11 completion notice**
   (`0001193125-25-200616`; every 6-K through 2026-08-31 read by title, list in
   `_research 2026-09-13 HMC/filings_list.txt`), and the FY3/26 results set only a ¥70 dividend.
5. **Shares used: 3,893,016,583** (as at 2026-06-30). Trust deliveries after that date would raise it by
   a few hundred thousand shares (0.01%).
- **Split:** *"As of the effective date of October 1, 2023, the Company implemented a three-for-one stock
  split of its common stock"* (20-F Note 24). **It sits inside the owner-earnings window, but owner
  earnings are a yen total, not per share, so it moves nothing there.** For the cap, [CLAUDE.md]'s
  split-invariant rule: close(2026-09-11) × shares(2026-06-30) × splits after 2026-06-30 = × **1.0**
  (`split_factor_after('7267.T','2026-06-30')` returns 1.0; the full Yahoo history shows only the 2:1 of
  2006 and the 3:1 of 2023). **Every per-share figure from before October 2023 is on the old basis and is
  not used.**
- **Price ¥1,664** (7267.T close 2026-09-11, Yahoo, aggregator flagged) × **3,893,016,583** =
  **market cap ¥6,478bn (≈ ¥6.48 trillion)**.

**THE PERIMETER — the filings, with dates. Nothing here is from memory.**
- **Nissan business integration: AGREED TO CONSIDER, THEN ABANDONED, and it never closed.** 6-K
  2024-12-23 (`0001193125-24-283680`): *"Notice of Execution of Memorandum of Understanding regarding the
  Consideration of a Business Integration through the Establishment of a Joint Holding Company (Joint Share
  Transfer) between Honda Motor Co., Ltd. and Nissan Motor Co., Ltd."* — planned definitive agreement June
  2025, effective August 2026, a ¥100bn break fee on a competing transaction, a target of *"sales revenue
  exceeding JPY 30 trillion and an operating profit of more than JPY 3 trillion"*. A tripartite MOU with
  Mitsubishi Motors was signed the same day. 6-K 2025-02-13 (`0001193125-25-025577`), Exhibit 2: the
  companies *"today agreed to terminate the Memorandum of Understanding"*, noting *"Honda's proposal to
  change the scheme of Business Integration to a stock swap, which would make Nissan a wholly owned
  subsidiary of Honda"*, and *"there is no impact on the Companies' financial result"*. **Honda's FY3/26
  20-F does not mention Nissan at all** (no instance found in a text search). Collaboration continues by
  contract: 6-K 2026-08-31 (`0001193125-26-375276`), *"Nissan and Honda Conclude Joint Development Agreement
  to Standardize ECUs and Software for Next-Generation SDVs"*. **Perimeter effect: none.** Capital-allocation
  effect: large, read at Q3 (the ¥1.1tn buyback was resolved the same day as the MOU).
- **Astemo: SIGNED, NOT CLOSED — a future perimeter change, outside the window.** 6-K 2025-12-16
  (`0001193125-25-319940`): Honda *"has resolved to acquire an additional 21% equity interest in Astemo,
  Ltd. … from Hitachi, Ltd. … and to make Astemo a consolidated subsidiary"*, 40% → 61%, **¥152.3bn**.
  Astemo's own filed figures in that notice: FY3/25 sales revenue ¥2,186.5bn, operating profit ¥67.4bn,
  **net loss attributable ¥10.2bn** (and losses in each of the three years shown). 6-K 2026-06-30
  (`0001193125-26-289265`): closing moved *"to by the end of the third quarter of the fiscal year ending
  March 31, 2027"*; *"not anticipated to have a material impact"* on FY3/27 results. **Nothing in the
  FY3/22–FY3/26 window is on the post-Astemo perimeter**; after closing, a ~¥2.2tn, ~3%-margin, loss-making
  parts maker enters the consolidated industrial figure. Recorded at Q4 and Q6.
- **Yachiyo Industry: a small buy-and-sell inside the window.** Tender offer to take the 50.4%-owned
  subsidiary private (6-K 2023-10-04, results 6-K 2023-11-21) under a framework to transfer 81.0% to the
  Motherson Group; the FY3/24 cash flow statement shows "Proceeds from sales of subsidiaries … (18,544)".
  **Sized against Honda: immaterial** (Yachiyo's share count of 24.0M at a ¥1,390 tender price values the
  whole company at ¥33bn, 0.5% of Honda's cap today). Stated, not rebuilt.
- **Hitachi Astemo formation, January 1, 2021 — before the window.** Keihin, Showa and Nissin Kogyo were
  **equity-method affiliates before and after** (FY3/22 20-F: *"our former affiliates accounted for using
  the equity method"*; the merged company *"became our affiliate accounted for using the equity method"*),
  so no consolidated perimeter moved. It matters only to a window reaching FY3/21.
- **Sony Honda Mobility and the LG Energy Solution battery JV** are equity-method or joint arrangements;
  their losses run through equity-method income and impairments, not through a perimeter change (read at
  Q3/Q4).
- **How this run handles the perimeter:** the five-year default window FY3/22–FY3/26 sits on one
  consolidated perimeter (Yachiyo immaterial, stated). **No mean crosses the Astemo closing, because it has
  not happened.** Owner earnings are built on the **non-financial services perimeter** below.

**THE FINANCIAL SERVICES SEPARATION — settled before any gate opens (the GM and F method).**
- **The problem, in Honda's own statement.** The consolidated cash-flow statement runs the lending book
  through operating cash: *"Receivables from financial services (1,454,357) | (904,344) | (246,923)"* and
  *"Equipment on operating leases 12,661 | (690,110) | (365,571)"* (FY3/24–26, 20-F F-12). Consolidated
  OCF was ¥747.3bn, ¥292.2bn and ¥1,135.3bn — **a screen on it reads Honda's industrial cash as a third of
  what it is.**
- **The split exists, filed by Honda, in its strongest available form short of a separate registrant for
  the whole arm:** every fiscal-year results release carries **"CONSOLIDATED FINANCIAL SUMMARY 3 —
  Unaudited Consolidated Statements of Cash Flows Divided into Non-financial Services Businesses and Finance
  Subsidiaries"**, with a reconciling-items column to the audited consolidated statement. Retrieved from
  Honda's IR site (evidence ladder rung 3, English) for FY3/15–FY3/26 (`_research 2026-09-13 HMC/ir/pdf/`),
  and the same five-year non-financial OCF is on the IR data page "Cash Flows (Non-financial Services
  Businesses)". **It is unaudited, so it is reconciled before it is used (below).** Rung 1–2 limit stated:
  **the 20-F itself carries no split cash-flow statement** (no instance of a non-financial cash-flow table
  found in the FY3/21–FY3/26 20-F texts), and American Honda Finance Corporation files its own 10-K for the
  North American arm only.
- **The reconciliation (operator rule 4's cross-check, done on this schedule).** FY3/26: non-financial
  **¥1,681,944M** + finance subsidiaries **(¥451,812M)** + reconciling **(¥94,871M)** = **¥1,135,261M**,
  the audited 20-F figure to the million. FY3/25: 1,883,139 − 1,284,845 − 306,142 = **292,152**, which is
  also **SEC XBRL companyfacts `ifrs-full:CashFlowsFromUsedInOperatingActivities` = ¥292,152,000,000 (accn
  0001193125-25-142316)** and the FY3/26 20-F's printed 2025 column. **Three documents, one number.**
- **The one construction choice the schedule forces, disclosed now so it cannot be made quietly later.**
  The non-financial column's "Dividends received" includes **dividends paid up by the finance
  subsidiaries**, visible as the reconciling item on that line: FY3/22 ¥175,335M · FY3/23 ¥213,276M ·
  FY3/24 ¥225,018M · FY3/25 ¥305,047M · FY3/26 ¥96,248M. **The industrial owner-earnings figure at Q4
  strips them out** (the lending arm's cash must not sit inside an industrial figure, per the brief and
  the GM/F method); the finance arm is then carried as a **separate component** — its distributions and
  its segment profit — never blended into (c).
- **Company name:** the registrant is "HONDA MOTOR CO LTD", CIK 0000715153, **no former names**
  (`submissions.json`); `deal_note` and `name_change_note` returned empty — **confirmed**, and shown above to
  be blind to what the 6-Ks carry (a 6-K MOU and its termination are not an 8-K Item 1.01).

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A (Item 5: operating results by segment and region, FY3/26 vs FY3/25 and FY3/25 vs FY3/24;
  liquidity and capital resources; contractual obligations; R&D by segment) — read in full
- [x] cash-flow statement incl. detail lines (20-F F-12, three years; the unaudited non-financial /
  finance-subsidiary split for FY3/15–FY3/26 from the results releases)
- [x] footnotes (segment information, EV-related losses, impairments, equity, financing liabilities, and
  others cited where used at each gate)
- **Primary document: Form 20-F for the fiscal year ended March 31, 2026, filed 2026-06-18, accession
  `0001193125-26-274991`** (`d116494d20f.htm`) — **confirmed**. Also read: 20-Fs FY3/25
  (`0001193125-25-142316`), FY3/24 (`0001193125-24-163995`), FY3/23 (`0001193125-23-173074`), FY3/22
  (`0001193125-22-178101`), FY3/21 (`0001193125-21-196757`); every 6-K from 2021-04 through 2026-08-31
  (149 filings, text in `_research 2026-09-13 HMC/6k/`), including the Q1 FY3/27 results
  (`0001193125-26-333722`) and the **latest 6-K, 2026-08-31, `0001193125-26-375276` — confirmed**.
- **Figure cross-checked against the filed statement:** consolidated net cash provided by operating
  activities FY3/25, **¥292,152M**, identical in XBRL companyfacts (accn 0001193125-25-142316), the FY3/26
  20-F cash-flow statement, and the sum of the three columns of Honda's split schedule (above).
- **Tooling note (the brief's skip reason, tested):** companyfacts had **not ingested the FY3/26 20-F**
  (latest 20-F accession in the facts is `0001193125-25-142316`), the SONY finding repeated; and the
  history it does hold is IFRS from FY3/15. **The "short XBRL history" skip was a stale-ingestion and
  finance-arm problem, not a short-history one**: a screen on consolidated OCF would also have priced
  Honda on a figure that nets the lending book.

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**The security is four businesses under one balance sheet; Q1 is answered per segment (GHC 2026-09-02,
SONY 2026-09-13), and the understanding verdict is about the money-making, not its durability (Q2/Q4).**
All figures are the filed segment note (Note 4 "Segment Information"): FY3/16–FY3/18 from the FY3/18 20-F
(`0001193125-18-197283`), FY3/19–FY3/21 from the FY3/21 20-F (`0001193125-21-196757`), FY3/22–FY3/23 from
the FY3/23 20-F (`0001193125-23-173074`), FY3/24–FY3/26 from the FY3/26 20-F (`0001193125-26-274991`).
Sales include intersegment; segment profit is operating profit before equity-method income; ¥bn.
Computation: `_research 2026-09-13 HMC/seg.py` → `seg.json`.

| Segment | Sales FY3/22 → FY3/26 | Segment margin FY3/22 · 23 · 24 · 25 · 26 | 5-yr segment profit, and share of the four-segment total | Segment profit ÷ segment assets FY3/26 | Capex ÷ sales FY3/26 |
|---|---|---|---|---|---|
| Motorcycle | 2,185 → 4,019 | 14.3 · 16.8 · 17.3 · 18.3 · **18.2%** | **¥2,752bn · 71.8%** | **27.0%** (¥731.9bn ÷ ¥2,713.7bn) | 3.4% (D&A 1.8%) |
| Automobile | 9,361 → 14,167 | 2.5 · (0.2) · 4.1 · 1.7 · **(10.0)%** | **(¥387bn) · (10.1)%** | (11.3)% | 6.2% (D&A 4.2%) |
| Financial services | 2,823 → 3,533 | 11.8 · 9.7 · 8.4 · 9.0 · **7.8%** | ¥1,484bn · 38.7% | 1.6% (¥275.5bn ÷ ¥17,282.6bn) | leases, not plant |
| Power products & other | 422 → 420 | (2.3) · 4.8 · (2.1) · (2.3) · **(2.5)%** | (¥16bn) · (0.4)% | (1.8)% | 5.6% |
| **Four-segment total** | 14,791 → 22,139 | 5.9 · 4.6 · 6.7 · 5.5 · (1.9)% | **¥3,833bn** | — | — |

*The longer record, same note, same definitions: motorcycle margin FY3/16–FY3/21 10.1 · 9.9 · 13.1 · 13.9 ·
13.9 · 12.6%; automobile margin FY3/16–FY3/21 1.4 · 4.9 · 3.4 · 1.9 · 1.5 · 1.0%. **Across eleven filed
years the automobile segment's best margin is 4.9% and the motorcycle segment's worst is 9.9%.** Yen
translation flatters every line: the yen weakened across the window, and the MD&A's FY3/26 automobile
revenue decline of 2.2% becomes 1.6% at constant rates.*

- **Unit economics in my own words, no management language:**
  1. **Motorcycles — a volume toll on the commuting of the developing world.** Honda builds cheap, durable
     petrol two-wheelers (Activa and SP in India, Pop and CG in Brazil, Super Cub and Wave-class commuters
     across Asia) and sells about 22 million a year through the group, 14.7 million consolidated; *"approximately
     85% of Honda's motorcycle units on a group basis were sold in Asia"* (Item 4.B). A consolidated unit
     brings in about **¥274,000 (≈$1,800) and leaves ¥50,000 of segment profit** (¥4,018.8bn and ¥731.9bn over
     14,673 thousand units, FY3/26). The Indonesian volume (about 4.94 million units) sits in P.T. Astra Honda
     Motor, an equity-method affiliate, and arrives as equity income (¥65.2bn for the segment, FY3/26). The
     plant is cheap: segment capex ¥136.0bn and D&A ¥74.3bn against ¥4.0tn of sales. **It makes money by
     selling a great many low-priced machines at a steady margin on very little capital**, and by the parts
     and service trade that follows them. Price is not the engine: the MD&A says in FY3/26 and FY3/25 alike,
     *"Despite changes in sales price, the impact of the price changes was immaterial on sales revenue"*;
     growth came from units (+7.2% and +12.0%).
  2. **Automobiles — an assembler that earns its keep in North America and hands most of it back.** Honda
     designs and assembles cars and light trucks (CR-V, Civic, Accord, Pilot, HR-V; N-BOX in Japan), **66.5% of
     segment external revenue in North America** (¥9,213.4bn of ¥13,863.3bn); a consolidated unit brings in about **¥5.2M (≈$34,000)** and in FY3/25,
     the last year before the write-offs, left **¥86,000 of segment profit (1.7%)**. The cost that recurs is
     the next platform: capitalised development and plant for each model cycle (segment capex ¥879.0bn,
     D&A ¥601.3bn, FY3/26), plus warranty (*"Provisions for product warranties accrued … ¥536,590 million,
     ¥454,502 million and ¥319,613 million"*). **China is now a loss-maker by equity method** (segment equity
     income (¥59.9bn) FY3/25 and (¥228.4bn) FY3/26, after ¥215.8bn in FY3/18), and the EV programme cost
     **¥1,577.8bn** in FY3/26 alone (Note 4(d)).
  3. **Financial services — a spread lender that exists to sell Honda products.** Finance subsidiaries in the
     US, Canada, Japan, the UK, Germany, Brazil and Thailand make retail loans and leases to Honda buyers and
     wholesale loans to dealers; the book (*"receivables from financial services and equipment on operating
     leases of finance subsidiaries"*) was **¥16,327.2bn** at March 2026, funded by **¥12,252.7bn** of finance-
     subsidiary liabilities (Item 5.B). It earns a funding spread plus lease-residual outcomes; it earned
     **1.6% on segment assets** in FY3/26 and 1.9–2.9% across the window, and it bears the credit and
     residual risk (*"Provision … for credit and lease residual losses"* ¥50.1bn → ¥71.0bn → ¥87.9bn,
     FY3/24–26). North America is ¥2,895.5bn of its ¥3,529.4bn of revenue.
  4. **Power products and other — engines and garden machines, plus an aircraft maker.** General-purpose
     engines, generators, mowers and outboards around break-even, carrying **HondaJet**, whose *"operating
     loss of aircraft and aircraft engines … was ¥37.2 billion"* (FY3/26). Immaterial to the whole
     (1.9% of sales).
- **The scarce input this business controls — per segment, and it differs in kind:** Motorcycles, **a dealer
  and service network and a brand across the high-volume two-wheeler markets of Asia and Brazil, joined to
  cost-at-scale manufacturing** (plus the Astra partnership in Indonesia); Automobiles, **a North American
  light-truck and hybrid franchise of reputation for reliability**, not scarce in the [E3-03] sense (tested at
  Q2); Financial services, **nothing scarce** — a captive funded at Honda's A3/BBB+ rating (Item 5.B) against
  banks and finance companies that the risk factor names as competitors; Power products, a brand in engines.
- **"On what capital?" — answered from the filing, because the segment note gives segment assets** (unlike
  Sony's): FY3/26 Motorcycle ¥2,713.7bn, Automobile ¥12,484.8bn, Financial services ¥17,282.6bn, Power
  products ¥593.6bn. **Motorcycles earn 27.0–30.9% pre-tax on their segment assets across FY3/23–26 (29.4–34.0%
  including equity income); Automobiles earned 0.5–5.3% including equity income across FY3/22–FY3/25 and
  (13.1)% in FY3/26.**
- **Will the fundamentals look broadly the same in ten years?** **Motorcycles: the business, yes; the power
  unit, not certainly** — the 20-F sets *"carbon neutrality in all of its motorcycle products during the
  2040s"* and has begun an electric range (WN7, UC3, ICON e:), while saying *"demand for EVs has not grown as
  much as expected"*. Asian commuting on two wheels is not going away in ten years; whether the petrol
  cost-and-network advantage carries to battery two-wheelers is the open question, named for Q2 and Q4.
  **Automobiles: no** — the filing describes *"a period of major change, including intensifying competition
  due to the rise of emerging Chinese EV companies"* and a strategy reset twice in a year (the ¥1.58tn
  write-off, a three-year ¥6.2tn investment plan). **Financial services: yes, as a function of auto volume.**
  **Power products: yes, small.**
- **The hunt for disconfirming evidence [E4-26], before the verdict.** [E3-31] asks for businesses
  *"relatively simple and stable in character"*, and [E4-46] puts a business needing months of study outside
  the circle. The automobile segment is not stable in character, and Honda's own management mis-forecast it
  badly enough to write off ¥1.58tn. **But Q1 asks whether the money-making can be understood, not whether its
  future can be predicted; the latter is Q2's [E4-04] and Q4's range, and GM (2026-09-01) and F (2026-09-02)
  were both answered the same way on the same industry.** Each leg's money-making is legible from the filing in
  a paragraph, the capital each consumes is filed, and the separation of the lender from the manufacturer is
  filed and reconciled (Step 0). What is not stable is named above so it cannot be averaged away later.
- **VERDICT: [x] IN** — the money-making is understandable segment by segment from the filed 20-F, and the
  capital each segment uses is filed. Understanding is the gate; durability and relative position are Q2 and
  Q4's. *(No "unverified" or "provisional" caveat is carried.)*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Per segment, with the metric set chosen by business type first [E5-37]; the verdict must hold for what the shareholder
actually buys (GHC 2026-09-02), and where some legs pass and some fail it is decided by where the profit AND the capital
are (HAS 2026-09-03: IN because the franchise leg was overwhelming and the rest *"neither grows nor eats material capital"*;
SONY 2026-09-13: OUT).** Competitor rows were transcribed from filed documents by two research passes and are on disk with
accession numbers, URLs and verbatim lines: `_research 2026-09-13 HMC/peers_moto.md` and `peers_auto.md`; the automobile row
also uses the Toyota run's transcription (`_research 2026-09-13 TM/peers/COMPETITOR ROW - five-year industrial margins.md`),
**spot-checked against the filing text on disk before use** (GMNA 2025 net sales 154,317 and EBIT-adjusted 10,452 in GM's
10-K `0001467858-26-000013` Note 23; Stellantis "Total Consolidated shipments" 5,484 in its 20-F `0001605484-26-000021`: both
found, both match). Pooled margins below are arithmetic on those filed figures; Honda's are from its own 20-Fs (Q1).

### Is there a group-level moat, as at Berkshire?
**No filed evidence of one.** The 20-F's group claim is *"the world's largest power unit manufacturer"* language in the
decks and *"Respect for the Individual"* in the 20-F; no filed number attaches a shared cost of capital (the finance arm
borrows at A3/BBB+), a shared customer, or a shared plant across motorcycles and cars. **The legs carry the verdict.**

### Segment by segment

**1. MOTORCYCLES — [x] needed or desired · [~] no close substitute · [x] not price-regulated. NARROW, direction
widening. The position is real and rowed; the class is not WIDE.**

| Maker (fiscal years) | measure, as filed | margin, five years | pooled | units, first → last year | source |
|---|---|---|---|---|---|
| **Honda Motorcycle** (FY3/22–26) | IFRS segment profit ÷ segment sales | 14.3 · 16.8 · 17.3 · 18.3 · **18.2%** | **17.2%** | group 17,027k → **22,101k (+30%)**; consolidated 10,721k → 14,673k | 20-Fs, Note 4; Item 4.B |
| Bajaj Auto, standalone (FY3/22–26) | "Operating Profit Margin" (incl. three-wheelers) | 15.4 · 17.1 · 18.8 · 19.3 · **19.6%** | 18.4% | two-wheelers 3,837k → 4,317k (+13%) | Annual Reports 2021-22, 2023-24, 2025-26 (bajajauto.com) |
| Hero MotoCorp, standalone (FY3/22–26) | "Operating Profit Margin (%)" | 9.30 · 9.85 · 12.13 · 12.49 · **12.97%** | 11.6% | 4,944k → 6,469k (+31%) | Annual Reports 2022-23 to 2025-26 (heromotocorp.com) |
| Yamaha Motor, "Motorcycle" business (CY2022–25) | operating income ÷ revenue (earnings decks; the audited segment is "Land mobility", 5.8–8.0%) | 6.6 · 8.9 · 8.1 · **7.8%** | 7.9% | 4,531k (2021) → 4,999k (+10%) | Financial Reports / presentations FY2021–25 (global.yamaha-motor.com) |
| Harley-Davidson, HDMC (CY2021–25) | segment operating income ÷ revenue | 10.6 · 13.9 · 13.6 · 6.7 · **(0.8)%** | 9.4% | 188.0k → 124.5k (−34%) | 10-Ks `0000793952-22-000014` … `0000793952-26-000011` |
| Suzuki Motorcycle (FY3/22–26) | segment profit ÷ net sales (J-GAAP to FY3/24, IFRS after; incl. ATVs) | 4.3 · 8.8 · 10.6 · 10.3 · **9.9%** | 9.1% | 1,292k → 1,962k (+52%) | Consolidated Financial Summaries and References FY2021–25 (globalsuzuki.com) |
| Kawasaki Powersports & Engine (FY3/22–26) | segment / business profit ÷ total revenue (incl. SxS, ATV, PWC, engines) | 8.4 · 12.1 · 8.1 · 7.8 · **3.3%** | 7.8% | wholesale motorcycles 491k → 509k (+4%) | audited Consolidated Financial Statements and results decks (global.kawasaki.com) |
| TVS Motor (FY3/22–26) | "Operating EBITDA (%)" — EBITDA, not comparable | 9.4 · 10.1 · 11.1 · 12.3 · **12.9%** | — | two-wheelers 3,513k (FY3/23) → 5,670k | Annual Reports 2023-24, 2025-26 (tvsmotor.com) |

*Row limits stated:* **7 peers taken — six on an operating-profit measure, TVS on EBITDA only**; Eicher/Royal Enfield and the
Chinese makers are not rowed (not obtained in this pass).
Bajaj and Hero are standalone Indian GAAP companies with no segment note (Bajaj includes three-wheelers and a large export
book); Yamaha's motorcycle figure is from its decks, not its audited note; Harley is a premium US niche, not a commuter
competitor; fiscal years and currencies differ. **Source rule stated (the brief asked):** none of the six non-US makers is
an SEC filer; they were read at evidence-ladder rungs 3–4 (the company's own English annual report or results filings on
its IR site, the same rung the SONY run used for UMG), never through an aggregator. **[E3-61]:** the row shows position, not
conduct.

- **What the row shows.** **Scale leader** — Honda's 22.1M group units against Yamaha's survey of *"FY2025 worldwide demand"*
  of 59,286 thousand units is ~37% of the world by volume (mixed definitions: Honda's includes ATVs/SxS and a March year) —
  **and margin co-leader with Bajaj**, 5.6 points above Hero, ~8 points above Suzuki, ~9 above Yamaha and Kawasaki. **Units growing faster than every
  peer but Hero and Suzuki [E4-55]** (TVS two-wheelers +61% in three years, on EBITDA margins). Return on segment assets 27.0–30.9% FY3/23–26 against Suzuki 10.7%, Yamaha Land mobility 8.5–10.5%,
  Kawasaki 2.8–6.9% and HDMC (0.7)–20.8% (Bajaj's segment-asset figure excludes its treasury and is not like-for-like).
- **(2) no close substitute — partly.** For a commuter in India, Hero, Bajaj and TVS are close substitutes: Hero files a
  **28.7%** domestic two-wheeler ICE share and **90%+** of the Deluxe 100 segment; Bajaj files a **15.6%** domestic motorcycle
  share and *"a series of pricing and product interventions"*. Honda's own FY3/24 deck shows its CY2023 share only as unlabelled
  pie charts (*"Image of Honda's Share"*) — no filed share number was found in Honda's documents, so none is claimed. **The
  position looks like [E2-58]'s exception — a cost-and-network advantage — wide against Yamaha, Suzuki, Kawasaki and Harley, not against Bajaj.**
- **[E2-44] two-characteristic test.** *Price:* Honda's own bridge (FY3/25 and FY3/26 results decks, IR site) shows **"Price
  revision +174.2"** and **"+79.0"** ¥bn to motorcycle operating profit, with incentives −14.1 and −12.0 — **but in years when
  volume rose 12% and 7%, so demand was not flat** and the test's hard case is not observed. The one flat-volume read is
  Honda's own FY3/24 slide: operating profit ¥291.6bn (13.9%) FY3/19 → ¥556.2bn (17.3%) FY3/24 on consolidated units
  **13,215K → 12,219K** — profit nearly doubled on 7.5% fewer units (price and mix not separated). **A discrepancy is recorded,
  not resolved:** the same years' 20-F MD&A says *"Despite changes in sales price, the impact of the price changes was
  immaterial on sales revenue"* while the deck books ¥174.2bn (4.8% of segment sales) of price revision to profit;
  hyperinflation-market pricing (Turkey, Argentina) against FX effects of −¥74.6bn is a candidate explanation the filings do
  not state. *Volume with minor capital:* **partly** — segment assets rose ¥1,449bn → ¥2,714bn as sales went ¥2,185bn →
  ¥4,019bn (turnover flat at ~1.5x), but the incremental ¥420bn of profit came on ¥1,265bn of incremental assets (33%).
- **[E4-04] — must the moat be rebuilt?** The advantage is a petrol-engine cost position and a dealer network; the filing
  names the replacement risk itself: carbon neutrality *"in all of its motorcycle products during the 2040s"*, a first
  electric range launched 2025–26. **A lapse in spending would narrow it; the battery transition could require buying the
  replacement.** Not yet visible in the numbers; carried as a durability defect, not a failure.
- **Attacker's test [E2-45]:** a funded attacker cannot buy 22 million units of dealer and service coverage across Asia and
  Brazil; an attacker building battery scooters for Indian cities can enter without it. **[E3-33] untapped pricing power:**
  not claimed — [E5-28] would require near-monopoly, and Hero's filed 28.7% and Bajaj's 15.6% domestic shares show a
  contested Indian market.

**2. AUTOMOBILES — [x] needed or desired · [ ] no close substitute · [x] not price-regulated. NONE, direction narrowing.
FAILS.**

| Maker (fiscal years) | measure, as filed | pooled five-year margin | units, first → last year | source |
|---|---|---|---|---|
| Toyota Automotive (FY3/22–26) | IFRS segment operating income | 8.22% | 8,230k → 9,595k (+17%) | 20-Fs `0001193125-22-179197` … `-26-264811` |
| Stellantis, six vehicle segments (2021–25) | AOI, non-GAAP | 9.61% | 5,836k → 5,484k (−6%) | 20-Fs (TM transcription) |
| GM, GMNA + GMI (2021–25) | EBIT-adjusted, non-GAAP | 8.60% | 2,859k → 3,799k wholesale | 10-Ks (TM transcription, spot-checked) |
| Hyundai, vehicle segment (2021–25) | K-IFRS operating profit ÷ net sales | 7.01% | 3,891k → 4,138k wholesale | audited FS and decks (hyundai.com) |
| BYD, "Automobiles and related products and other products" segment (2021–25; includes batteries, solar and rail — no automobile-only segment) | CAS segment "Total profit" (pre-tax) | 5.29% | NEV 604k → 4,602k | HKEX annual reports and December sales announcements |
| Suzuki Automobile (FY3/22–26) | segment operating profit (J-GAAP FY3/22–23, IFRS after — mixed basis) | 8.48% | consolidated 2,853k → 3,572k (+25%) | Annual Securities Reports FY2024–25, Financial Summaries FY2021–23 (globalsuzuki.com) |
| Volkswagen Automotive Division | IFRS operating result, stated ratios | ~5.6% | 8,576k → 9,022k (group) | Annual Report 2025 (TM transcription) |
| Ford, Blue + Model e + Pro (2021–25) | segment EBIT, non-GAAP | 4.71% | 3,942k → 4,394k wholesale | 10-Ks (TM transcription) |
| Tesla automotive (2021–25) | segment GROSS profit — not comparable | 20.3% gross | 936k → ~1.64M delivered | 10-Ks (TM transcription) |
| **Honda Automobile** (FY3/22–26) | IFRS segment profit (EV losses inside) | **(0.62)%**; **1.70% excluding the FY3/26 EV losses** | group **4,074k → 3,387k (−17%)** | 20-Fs, Note 4; Item 4.B |
| Nissan Automobile (FY3/22–26) | J-GAAP segment profit | (0.88)% | retail 3,876k → 3,151k (−19%) | Securities Report translations (nissan-global.com) |

*Row limits:* **10 peers named of the industry's ~10–12 at global scale**; measures differ (non-GAAP adjusted for GM, Ford and
Stellantis exclude charges Honda's includes; Honda ex-EV is shown beside it for that reason; BYD's segment is not automobile-only;
Suzuki's pooled figure mixes J-GAAP and IFRS).
- **Position: second from the bottom of eleven, ahead only of Nissan**, and the only volume maker besides Nissan whose group
  units fell double digits. Even with the ¥1,453.6bn of FY3/26 EV losses taken out of operating profit, Honda's 1.70% is
  below every peer but Nissan. **The eleven-year record (Q1): best year 4.9%.**
- **[E2-58], on the filing's own terms.** *"intensifying competition due to the rise of emerging Chinese EV companies"*;
  *"deteriorating profitability of internal combustion engine (ICE)/hybrid vehicles caused by tariffs"*; China JV units
  *"substantially decreased by 25.4%"* after −33.7% the year before. No administered price; no cost advantage wide and
  sustainable — the row shows the opposite.
- **[E3-62], the second step, from Honda's own bridge:** FY3/25 **"Price revision +326.3"** against **"Incentive −253.1"**
  and a margin that fell 4.1% → 1.7%; FY3/26 **"Price revision +232.4"**, then **"Tariff impacts −331.6"** and an adjusted
  margin of **0.3%** before the EV losses. **Price was taken; none of it stayed home.**
- **[E4-04] / [E2-27]:** a model platform is replaced each cycle (the 20-F's next-generation hybrid platform *"scheduled to
  be adopted for hybrid models to be introduced from 2027 onward"*), and the EV programme built and wrote off capacity in
  step with GM, Ford and Stellantis. **[E4-55] units:** group units 5,199k (FY3/18) → 3,387k while yen revenue rose.

**3. FINANCIAL SERVICES — NONE.** *"customers can also obtain financing … through a variety of other sources that compete
with our financing services, including commercial banks and finance and leasing companies"* (Item 3.D). A captive whose
volume is the automobile leg's volume and whose margin fell 11.8% → 7.8% FY3/22–26 on rising provisions. **Every peer in the
automobile row runs one** (GM Financial, Ford Credit, Toyota FS, Hyundai Capital, Nissan sales financing): no relative moat.

**4. POWER PRODUCTS AND OTHER — NONE.** Segment margin (2.5)% to 4.8%; HondaJet losses ¥37.2bn a year. Immaterial.

### What the shareholder buys — the mix, and where the capital goes
| | Motorcycle | Automobile | Financial services | Power products & other |
|---|---|---|---|---|
| Share of five-year segment profit FY3/22–26 | **71.8%** | (10.1)% | 38.7% | (0.4)% |
| Share of FY3/26 industrial segment assets (ex-FS) | 17.2% | **79.1%** | — | 3.8% |
| Share of FY3/26 industrial capex (accrual) | 13.1% | **84.6%** | — | 2.3% |
| Share of FY3/26 R&D expenditure (Item 5.C) | 9.6% | **87.6%** | — | 2.8% |
| The next three years (20-F, Financial Strategy) | *"growth of our Motorcycle … businesses"* | **¥6.2tn: ¥4.4tn ICE and hybrid, ¥1.0tn software, ~¥0.8tn EV** | — | — |

- **This is not HAS.** HAS passed because the non-franchise legs *"neither grow nor eat material capital"*. Honda's
  automobile leg takes 79% of the industrial assets, 85% of the capex, 88% of the R&D, and a ¥6.2tn plan — the leg that
  fails consumes the capital the leg that passes earns. **It is not BRK:** no group-level moat is filed. **It is SONY's
  shape, more sharply:** Sony's franchise legs were 55% of profit with the capital spread; Honda's franchise leg is 72% of
  profit with 17% of the assets.
- **Key-person dependence [E4-23]:** low in every leg — recorded in the business's favour.
- **Dominance [E2-53]:** no leg; in India the leader is Hero on its own filing.
- **Return on capital [E3-46], the second question as a number:** industrial five-year owner earnings of ~¥558bn on ¥15.8tn
  of non-financial segment assets is ~3.5% (Q4); motorcycles alone earn ~27–31% pre-tax on theirs.

### THE FAIR COUNTER-CASE, stated as its best advocate would state it [E4-51]
**Honda owns the largest, most profitable volume motorcycle business in the world — 22 million units, an 18% margin that has
widened five years running, 27–31% pre-tax on its assets, units growing faster than Bajaj and Yamaha — and at ¥1,664 the
market capitalisation (¥6.48tn) is less than ten times that one segment's FY3/26 pre-tax profit (¥731.9bn), before ¥3.3tn of
industrial net cash and ¥3.2tn of finance-arm equity.** The automobile leg is already recovering: Q1 FY3/27 (6-K
2026-08-05) shows automobile segment profit **¥192.1bn on ¥3,879.2bn (5.0%)** and motorcycles **¥234.0bn (20.5%)**; the EV
write-off is a one-time reset; the ¥6.2tn goes mostly to hybrids, where Honda's technology is competitive; and a franchise is
judged on the business, which here is overwhelmingly the motorcycle profit. **What defeats it is the capital, not the profit
share:** a franchise verdict on the security needs the franchise leg to be what the shareholder's retained money goes into,
and Honda's filing says in writing that it goes into the other leg. One quarter at 5.0% sits inside an eleven-year range whose
best year was 4.9%.

- Class: **[x] NONE on the business as constituted** (Motorcycles NARROW, widening; Automobiles, Financial services and Power
  products NONE). Direction: **narrowing at the enterprise level** (automobile units, margin and China equity income all down;
  capital share rising).
- **VERDICT: [x] OUT — on the business as constituted.** The motorcycle leg is a narrow, widening position and passes on its
  own; the security fails because the automobile leg, which fails [E3-03] criterion 2 on Honda's own filing and sits second
  from the bottom of an eleven-name filed row, takes 79% of the industrial assets, 85% of the capex, 88% of the R&D and the
  ¥6.2tn plan. **The entry run stops here. [E5-13]: most names should end here, and that is the system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT. Everything below is **RECORDED, NOT GOVERNING**, and the price
block carries operator rule 3's header.

---

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business as constituted).
*Hard sequence (operator protocol 2): nothing below can reopen the file, and a strong Q3 could not have repaired Q2
[E2-37, E2-38, E3-39]. The record is kept because the operator's instruction asks every run for the whole file,
and because Honda's capital allocation is where the Q2 finding becomes a price at Q5.*

**STEP 1 — THE WEIGHT CASE. [x] Daily execution · [ ] Control · [x] Leverage → BINARY GATE.**
- **Daily execution [E3-38, E3-43, E2-70]: yes, for the automobile leg** — a model-cycle and technology-bet
  business, *"a business, unlike a franchise, can be killed by poor management"*; the ¥1,577.8bn FY3/26 write-off
  is management's own bet reversed inside four years (targets set 2021–2022, cancelled 2025–2026, below).
- **Leverage [E3-29]: yes, for the finance arm** — finance-subsidiary assets ¥17,282.6bn on ¥3,182.4bn of arm
  equity (5.4x, March 2026, Consolidated Financial Summary 2), up from 4.3x in March 2022. The industrial perimeter
  itself holds net cash (Q4).
- **Control [E1-16]: no** — a minority holding in a listed company.

**Honesty — binary, filings-based [E5-16], each matter dated to when it became PUBLIC:**
1. **2024-06-03, type-designation certification (6-K `0001193125-24-152398`).** After a regulator's directive of
   2024-01-26, Honda reported *"cases of improper conduct, such as deviations from test conditions in sound emission tests
   and tests for vehicle-mounted engine power … and the use of data different from actual measured values in test
   reports"*, in tests conducted **2009–2017**, stated cause *"avoid increasing the man-hours for re-testing"*, with
   *"no confirmed cases of improper testing in the certification of four-wheeled vehicles currently sold"*. The 20-F keeps
   it in the risk factors. **Read as [E4-22]'s cockroach, dated and disclosed by the company when asked; it is the same
   industry-wide Japanese certification episode the TM run recorded at four Toyota group companies.** Not a board-level
   disqualifier on the filed record; the prompt stays live.
2. **2025-04-07, a Representative Executive Officer resigned (6-K `0001193125-25-074141`).** *"facing an allegation of
   inappropriate conduct during a social gathering outside of work hours"*; the Audit Committee investigated and the
   board *"determined that it is appropriate for Mr. Aoyama to resign"*; the CEO returned 20% of two months' pay.
   **[E5-22]: the failure that counts is not acting; the filing shows action within the disclosure.** Personal conduct,
   handled; not a disqualifier of the remaining management.
3. **2023-06-16/23, a ¥58.6bn warranty estimate changed after the audit report and the results were re-issued**
   (6-Ks `0001193125-23-168401`, `-173064`) — a subsequent event reflected before the 20-F, disclosed with the reason.
   **Direction: toward candor [E2-69].**
4. **Airbag inflators:** the 20-F notes *"it is not possible for Honda to reasonably estimate the amount and timing of
   potential future losses"*; legal proceedings are described as *"ordinary routine litigation incidental to our
   business"* (Item 8). No filed conduct finding against the company in the window.
- **Result:** no integrity disqualifier found. *[E5-17]: "Sincerity and empathy can easily be faked" — this is the absence
  of found disqualifiers, not a finding that the managers are honest.*

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49, E2-57, E3-53].** *Each a prompt to read, never a verdict.*
- [x] **weak accounting — the cockroach prompt**: the certification matter above; and IFRS 5 held-for-sale impairment on
  an unnamed parts-subsidiary group (¥48,328M, Note 4). Pensions and SBC are not the issue (SBC is trivial, Q4).
- [ ] **unintelligible footnotes** — no: Note 4(d) itemises the EV losses by line and cause, and Note 17 rolls the EV
  provision forward. **This is the positive pole of [E2-26].**
- [x] **trumpeted projections / growth targets [E4-22, E3-48, E5-30]** — Honda guides every year and sets long-dated
  targets. **The record, from Honda's own results 6-Ks (initial May operating-profit forecast → outturn):** FY3/22
  ¥660.0bn → ¥871.2bn · FY3/23 ¥810.0bn → ¥780.8bn · FY3/24 ¥1,000.0bn → ¥1,382.0bn · FY3/25 ¥1,420.0bn → ¥1,213.5bn ·
  **FY3/26 ¥500.0bn → (¥414.3bn)** (revised ¥700bn in August, ¥550bn in November and February, *"-270.0 ～ -570.0"* on
  2026-03-12). **The long-dated targets** are the sharper read: *"EV/FCV unit sales ratio of 40% by 2030, 80% by 2035 and
  100% by 2040"* and ¥5tn of R&D over six years (6-K 2021-04-26); *"30 EV models globally by 2030 with production volume
  of more than 2 million units annually"* (6-K 2022-04-12); **by FY3/26 the 20-F records cancellations of North American
  and Chinese EV models and ¥1,577.8bn of losses**, and replaces the targets with new ones: *"eliminate EV-related losses"*
  by FY3/29, *"an all-time high fiscal year operating profit"* in FY3/29, *"ROIC … target of 10%"* in FY3/31. [E3-48]'s base
  rate is that projections justify a decided course; **this record shows a course decided, projected, and reversed.**
- [ ] **serial share issuance [E5-15]** — no: shares fell from 5,280,000,000 issued to 4,533,000,000 and outstanding from
  ~4.64bn (Nov 2024) to 3.89bn; the only issuance is trust-delivered officer stock.
- [x] **EBITDA / adjusted-earnings promotion [E4-29, E2-57]** — **two consecutive "except-for" headlines and a cash metric
  that adds back an expense.** FY3/25 results deck: *"Operating Profit 1,213.4 bil. yen (excl. the impact of the change in
  the estimation model for automobile product warranties: 1,341.0 bil. yen)"*; FY3/26 deck: *"Operating profit - 414.3
  billion yen (Adjusted operating profit excluding EV-related losses : 1,039.3 bil. yen)"*, and the FY3/27 target is
  framed as *"Adjusted operating profit excluding EV-related losses ：1 trillion yen"*. **And the headline cash figure is
  "Operating cash flows after R&D adjustment 2,657.9 bil. Yen"** (FY3/25: 2,806.6), defined in the 20-F as *"CFO of
  non-financial services businesses + R&D expenditures – amount transferred to capitalized development cost"* — **an
  operating cash flow with research and development added back**, which is [E4-29]'s mechanism applied to the largest
  recurring cost of a car company. **The CGNX companion rule paid again:** the 20-F's audited statements carry none of
  these; the results decks lead with them. **Fires.** Mitigant, stated fairly: the IFRS figure is always printed first and
  the EV losses are quantified line by line.
- [x] **metric-switching [E2-49] — weak.** The dividend yardstick moved from payout ratio to DOE *"from FYE March 31, 2026
  onward"*, announced 2025-05-13 with a reason (*"to … ensure stable dividends even during periods of uncertainty"*) — before
  the loss, but in the same release that guided operating profit down 58.8%. A switch announced ahead of the bad year and
  after the bad forecast; recorded as a weak fire. *(The [E2-49] prior's ledger in the RESUME STATE is not recounted here.)*
- [ ] **filed-figure fraud tells [E4-30]** — no: income taxes paid ¥540.7bn on ¥1,642.4bn pre-tax (32.9%) FY3/24 and
  ¥523.2bn on ¥1,317.6bn (39.7%) FY3/25; reported growth is anything but smooth.
- [x] **restructuring charge [E3-53, E5-33]** — the EV charge is dumped into one year (¥1,310.6bn of it on 2026-03-12
  alone), with more promised: *"we expect that additional expenses and/or losses will be incurred in the fiscal year
  ending March 31, 2027"* and Note 31's unquantified supplier claims. **The run keeps it inside the owner-earnings mean
  (Q4), as [E5-33] requires, and does not annualise it away.**

**STEP 3 — THE PRIMARY TEST [E2-01], balance sheet first.** Return on equity attributable to owners (Honda IR "Financial
Indicators", tying to the 20-F): FY3/22 7.2% · FY3/23 6.0% · FY3/24 9.3% · FY3/25 6.7% · FY3/26 (3.5)%, **never 10% in
five years**, on a balance sheet whose industrial half holds ~¥3.3tn net cash. **Judged by segment, as [E2-56] and [E2-73]
require:** the motorcycle managers earned 27.0–30.9% pre-tax on segment assets FY3/23–26; the automobile managers 0.5–5.3%
including equity income FY3/22–25 and (13.1)% in FY3/26. **The consolidated ROE is the average of a remarkable operation and
a poor one — [E2-56]'s camouflage, visible because Honda files segment assets.**

**The half-owner test [E2-26]:** passes on the statements (every EV line quantified in Note 4(d), the provision rolled
forward in Note 17, the unquantifiable supplier exposure disclosed in Note 31 rather than omitted), **fails in the decks**
(adjusted operating profit and R&D-added-back cash flow as headlines). Mixed, and the mixed read is recorded.

**The institutional imperative — [E2-30], scored:**
- [x] **resists change in current direction** — the automobile leg earned a best margin of 4.9% across eleven filed years;
  the response has been more capital into the same leg, twice re-planned (2021/2022 EV targets; 2026 ¥6.2tn plan, ¥4.4tn
  of it ICE and hybrid).
- [x] **projects soak up available funds** — the 20-F's own words: *"We will leverage … the strong profitability and cash
  generation capabilities of the Motorcycle business and Financial services business"* to fund the automobile transition;
  the Nissan integration (a ¥30tn-revenue combination) was pursued and dropped inside 52 days.
- [ ] staff studies to justify a craving — not observable from the filings.
- [x] **peer behaviour imitated** — the EV capacity build and its reversal ran in step with GM, Ford and Stellantis (the GM
  run's row: ~$35bn written off by four manufacturers in the same year); Honda names the same cause, *"a shift in the United
  States government policy"*. **[E2-27] completed at Honda too.**

**Capital allocation — the buyback conditions [E5-08, E4-31, E5-24]:**
- **Scale:** repurchases ¥62.2bn, ¥156.6bn, ¥250.0bn, **¥722.0bn**, **¥670.3bn** (FY3/22–FY3/26, cash-flow statements) —
  ¥1.86tn in five years, beside ¥1.28tn of dividends, **¥3.14tn distributed against ¥2.88tn of net income attributable**.
- **(1) ample funds:** yes on the industrial balance sheet (Q4).
- **(2) material discount to IV, conservatively calculated:** **not established.** FY3/26 purchases averaged ¥1,476
  (Item 16E) against 3,997,276,887 average shares outstanding (results 6-K 2026-05-14), a price near **¥5.9tn**; this
  run's conservative industrial owner earnings (Q4, five-year, (c) = capex, EV provisions charged) are ~¥558bn, so the
  buyback bought the industrial stream near a **9.5% yield**, below the ~10% floor [E4-28] before any margin (with the
  finance arm's paid-up distributions added, ~12.9% — the flag is a judgment inside the range, not outside it). **CAPITAL ALLOCATION FLAG**, with the humility clause
  [E4-13]: it rests on this run's range, and management knows the business better. Binds position size, never the rate.
- **(3) shareholders supplied the information [E4-31]:** **fails for the first weeks of the programme.** The ¥1.1tn
  authority (*"Up to 1,100,000,000 shares (23.7 % of total number of issued shares …)"*) was resolved on **2024-12-23, the
  same board meeting as the Nissan integration MOU**, and purchases began 2025-01-06, **while a joint holding company with an
  undetermined share-transfer ratio was under consideration** — an owner could not estimate the value of what Honda's
  share would become. The MOU was terminated 2025-02-13; purchases ran to September 2025.
- **Stock deals [E5-44]:** none completed; Honda's own proposal was a stock swap making Nissan *"a wholly owned subsidiary
  of Honda"* (6-K 2025-02-13), a share-for-share deal at a P/B near 0.5 — recorded, not tested, because it never happened.

**Pay and what it vests on [E4-27]** (20-F Item 6.B): STI on *"operating profit margin and profit attributable to owners
of the parent"*; LTI 60% on the same two IFRS figures, 20% on brand value, CO₂ and engagement, 20% on TSR against TOPIX.
**What it does not vest on: return on capital, cash, or the automobile segment's margin separately.** It vests on reported
(not adjusted) figures, and FY3/26 pay moved with the loss: *"the STI for the President … was set at zero"*, LTI paid at
40–61%; total accrued STI ¥147M and LTI ¥112M for all executive officers. **[E4-27] reads it as aligned to scale and margin,
not to capital; small in amount.**

**Flags that converge [E4-52]:** projections trumpeted and reversed + adjusted-profit and R&D-added-back cash headlines +
an imitated capital build + a buyback resolved beside a merger MOU **all point the same way: toward presenting the
automobile transition as fundable and on plan.** A reinforcing system around one course, not a fraud finding
([E2-30]: *"Institutional dynamics, not venality or stupidity"*).

**THE GUARDRAIL**
- [x] Nothing in this Q3 promotes the name.
- [x] Key-person dependence: low; recorded at Q2 in the business's favour for motorcycles.
- [x] No great-manager case is made; the motorcycle franchise is intact and the damage is in another leg — **not an
  excisable cancer [E2-36], because the damaged leg is two-thirds of revenue and most of the capital.**

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN — no integrity disqualifier found**, with live prompts: [E4-29]/[E2-57]
  headline metrics, a projection record reversed at ¥1.58tn, [E2-56] camouflage across segments, a buyback flag on
  condition (2) and a condition-(3) failure during the MOU weeks. *IN never promotes.*

## Q4 — WILL IT SURVIVE?

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business as constituted).
*Built in full because Q5's computation needs the number and the operator asked for the record. Computation:
`_research 2026-09-13 HMC/oe.py` → `oe_out.json`; ¥ millions unless marked.*

### Owner earnings — the one number **[E2-23]**, on the non-financial services perimeter
> "(c) **the average annual amount** … that the business **requires to fully maintain** its long-term competitive
> position and its unit volume. (… the working capital **increment also should be included in (c)**.)" … "**(c) must be
> a guess**."

**Construction, every line disclosed (CONVENTION: OCF less SBC less the (c) guess, per the framework's Section VI):**
1. **Start: non-financial services operating cash flow** from Honda's split schedule (Step 0), reconciled to the audited
   consolidated OCF. It nets the working-capital increment from one line, so constraint 3 is met by construction.
2. **Less the finance arm's dividends paid up** (the reconciling item on the "Dividends received" line), so no lending cash
   sits in the industrial figure. The finance arm is carried **separately** below.
3. **Less lease repayments** (consolidated financing line, ¥47–81bn a year): after IFRS 16 these operating costs left OCF;
   they are put back as a cost. *(CONVENTION: ours; conservative by ~¥80bn a year; without it the yields below rise ~1.2
   points.)*
4. **Less the FY3/26 EV provisions recognised and not yet paid**: Note 17, *"EV-related losses … Additional provisions
   667,366 … Write-offs (82,954)"* → **¥584,412M** charged to FY3/26. The charge is a cash cost owed mostly within a year
   (*"Outflows of resources … are expected to occur within one year"* for the onerous contract); leaving it out would book
   the loss in the P&L and never in owner earnings. **[E5-33]: the restructuring charge stays in the mean.** Shown both
   ways.
5. **Less SBC, in full [E5-06], resolved and complete:** Honda's only share-based schemes are the BIP trust (officers;
   *"2,603,000 shares … for three fiscal years"*, ¥1,940M trust money) and the ESOP trust (operating executives; 2,335,000
   shares, ¥2,940M + ¥1,048M), 20-F Item 6.B; LTI accrued for all executive officers in FY3/26 was **¥112M**. **Subtracted as
   a ¥3,000M-a-year upper bound** (4.94M shares × ¥1,664 ÷ 3 = ¥2.7bn); **0.2–0.5% of owner earnings — negligible, stated.**
   [E3-70]'s market-value measure cannot exceed the share count granted; no option programme exists.
6. **Less (c)**, the disclosed judgment below.

| FY3/ | industrial OCF | EV provision unpaid | lease repay. | capex (PP&E + intangibles, cash) | D&A (segment note, ex-FS) | **OE, (c) = capex** | OE, (c) = D&A | FS dividends paid up | equity-method: income less dividends |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 1,077,419 | — | 47,088 | 604,876 | 684,002 | **422,455** | 343,329 | 60,927 | +53,585 |
| 2020 | 985,344 | — | 78,659 | 597,807 | 637,407 | **305,878** | 266,278 | 69,679 | (21,537) |
| 2021 | 985,025 | — | 67,628 | 546,959 | 599,143 | **367,438** | 315,254 | 65,931 | +81,629 |
| 2022 | 876,483 | — | 80,165 | 446,793 | 593,196 | **346,525** | 200,122 | 175,335 | +8,965 |
| 2023 | 1,139,520 | — | 78,297 | 629,518 | 687,934 | **428,705** | 370,289 | 213,276 | (127,454) |
| 2024 | 2,063,111 | — | 80,513 | 611,281 | 745,240 | **1,368,317** | 1,234,358 | 225,018 | (47,272) |
| 2025 | 1,578,092 | — | 78,137 | 848,558 | 731,305 | **648,397** | 765,650 | 305,047 | (125,357) |
| 2026 | 1,585,696 | 584,412 | 80,222 | 920,711 | 691,665 | **(2,649)** | 226,397 | 96,248 | (252,159) |

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38]:**
| window | OE, (c) = capex | OE, (c) = D&A *(display)* | (c) = capex, FY3/26 EV provision not charged | FS dividends paid up (mean) |
|---|---|---|---|---|
| 3-yr FY3/24–26 | **¥671bn** | ¥742bn | ¥866bn | ¥209bn |
| **5-yr FY3/22–26 (default [E2-42])** | **¥558bn** | ¥559bn | ¥675bn | ¥203bn |
| 8-yr FY3/19–26 | **¥486bn** | ¥465bn | ¥559bn | ¥151bn |
| 5-yr FY3/21–25 (before the write-off) | **¥632bn** | ¥577bn | ¥632bn | ¥197bn |

- **Spread, conservative end:** ¥486bn (8-yr) to ¥671bn (3-yr) on the governing (c); **the conservative end is 28% below
  the high end.**
- **Combined range (window × EV treatment, on the governing (c)), industrial only: ¥486bn to ¥866bn** (the invalid D&A end
  would widen it to ¥465bn); with the finance arm at zero at the low end and at its paid-up distributions at the high end:
  **¥486bn to ¥1,075bn**.
- **Is that range too wide to reach a conclusion?** Not on survival (every construction is positive over every window).
  On value, it is wide (Q5 carries it as width).
- **The distorted years, named [E5-11, E4-41]:** **FY3/24** (¥1,368bn, the record year: automobile segment profit ¥560.6bn
  on a weak yen — Honda's own 6-K of 2024-02-06 says *"a recovery in automobile production due to the normalization of
  the supply network and the weak yen are boosting profits"*, and the TM run measured the same tailwind at Toyota); **FY3/26**
  (the EV reversal). **[E4-41] normalises down for luck:** the 3-year window contains the FY3/24 tailwind, which is why the
  5- and 8-year windows govern. No view on the yen is taken [E3-32]; the width carries it.
- **Owner earnings by year:** the table above.
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT. Which case, and why: the exception class [E5-20],
  argued on Honda's own filed units, not borrowed from the TM or GM runs.** The default is D&A [E3-44, E2-41]. [E2-23]
  defines (c) as what *"fully maintain[s] … its long-term competitive position and its unit volume"*. **Honda spent
  0.95x its industrial D&A over FY3/17–FY3/26 (¥6,410bn of capex against ¥6,746bn of D&A) and did NOT hold unit volume:**
  automobile group units **5,199k (FY3/18) → 3,387k (FY3/26), −35%**; consolidated **3,748k (FY3/19) → 2,711k, −28%**; and
  the 20-F attributes part of the decline to under-investment in the legacy line: *"a decline in the competitiveness of our
  products in Asia stemming from the impact of the allocation of more resources to EV development"*. **Spending at D&A did
  not maintain the unit volume, so the D&A end is INVALID as a maintenance figure, and even the capex end is a generous
  guess.** Motorcycles are the opposite case (capex ¥136.0bn vs D&A ¥74.3bn FY3/26 while units grew, *"expanding production
  capacity in India"*): some of the capex end there is growth. **Band used: (c) = total industrial cash capex, PP&E plus
  capitalised development; D&A displayed, not used.** Over the default window the two ends are within ¥2bn of each other
  (capex 1.00x D&A FY3/22–26), so the judgment moves the five-year number by less than 1%; it moves the 3-year and 8-year
  windows by ±¥70bn.
- **Stock compensation subtracted in full [E5-06]:** ¥3,000M a year, an upper bound, negligible (item 5).
- **The finance arm, as a separate component — never blended into (c).** Paid-up distributions averaged ¥203bn a year
  (5-yr). **But [E2-60]'s third dimension bites:** finance-arm assets rose from 4.3x to 5.4x its equity (March 2022 → March
  2026; equity ¥2,638bn → ¥3,182bn while assets went ¥11,319bn → ¥17,283bn), and the two largest distributions (FY3/24
  ¥225bn, FY3/25 ¥305bn) came in the years leverage rose most. **Distributions that raise the lender's leverage are partly
  restricted earnings.** The arm is carried at Q5 as **paid-up distributions at the high end and zero at the low end**.
- **Look-through [E3-04]:** equity-method investees earned less than they paid Honda in four of the last five years
  (China JVs): the look-through adjustment is **negative, −¥109bn a year over five years**. Displayed; not in the governing
  figure; it would lower it.
- *If the capex band changes the verdict → UNKNOWABLE:* it does not change the survival verdict.

### Great, good, or gruesome? **[E4-20]**
- [x] **great — the motorcycle leg**: 27.0–30.9% pre-tax on segment assets FY3/23–26, capex ¥136bn on ¥4.0tn of sales,
  units up 7–12% a year.
- [ ] good
- [x] **gruesome — the automobile leg**: yen revenue up 51% FY3/22–26 (¥9.4tn → ¥14.2tn) while group units fell 17% (4,074k →
  3,387k; consolidated units only recovered from the FY3/22 chip trough, 2,424k → 2,711k), capex rising to ¥879bn, segment profit summed (¥387bn) over five years, and a ¥6.2tn three-year plan to keep adding money at those
  returns.
- **As constituted:** the great account is being used to fund the gruesome one — the 20-F's own words, *"leverage … the
  strong profitability and cash generation capabilities of the Motorcycle business and Financial services business"*.
  Consolidated, the five-year industrial owner earnings (¥558bn) earn **~3.5%** on the ¥15.8tn of non-financial segment
  assets. [E4-43]'s *good* class does not rescue it: the automobile leg does not earn *"a reasonable return"* on the cash it
  consumes.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — large yes, reliable no.** Five-year industrial owner earnings ¥558bn, but
  annual figures run from (¥3bn) to ¥1,368bn. The finance arm's segment profit is steadier (¥274–333bn a year).
- **(2) massive liquid assets — yes.** Industrial cash **¥4,563.5bn** against industrial financing liabilities **¥1,238.9bn**
  (¥507.9bn current, ¥731.0bn non-current) → **net cash ¥3.32tn** (March 2026, Consolidated Financial Summary 2); up from
  ¥3.22tn a year earlier after ¥955bn of FY3/26 distributions.
- **(3) no significant near-term cash requirements — NOT clean, and it is the one that usually kills.** Filed and dated:
  EV-related provisions **¥647.5bn** at March 2026 (current provisions rose ¥388.4bn → ¥948.3bn); **"additional payments to
  suppliers may arise" and cannot be estimated** (Note 31); a subsidiary's agreed purchase of buildings from an affiliate
  for **US$2,530M** (~¥388bn, agreed May 2026, Note 31); the Astemo 21% for **¥152.3bn** by December 2026; the **¥6.2tn**
  three-year resource plan; ~¥272bn a year of dividends at ¥70. **And the finance arm must roll ¥4,508.6bn of current
  financing liabilities** (Summary 2), backstopped by *"committed lines of credit equivalent to ¥1,769.8 billion"* against
  ¥917.5bn of short-term borrowings (Item 5.B) — that is the [E5-39] *"kindness of strangers"* the industrial net cash
  stands behind. **Scored: covered, not absent.**
- **Leverage, named and quantified [E4-16, E3-29, E2-54]:** industrial — net cash; interest expense ¥83.6bn (FY3/26,
  consolidated) against ¥558bn of five-year owner earnings after capex, **comfortably met [E2-54]**. Finance arm —
  ¥14,100bn of liabilities on ¥3,182bn of equity; funded by *"medium-term notes, bank loans, securitization … commercial paper
  and corporate bonds"*, **covenanted and dated, the opposite of [E3-52]'s float**. Ratings A3 / BBB+ / AA (R&I) / A-.
- **Jurisdiction [E3-66]:** a Japanese company with nominating, audit and compensation committees (the compensation committee chaired by an
  independent outside director, Item 6.B), whose
  cross-shareholders have been selling (secondary offering of 259.9M shares by insurers and banks, 6-K 2024-07-05). **The
  shareholder's place in the queue:** the filing's capital policy puts *"investments for the future"* first (*"During this
  transformation phase, investments for the future will take precedence"*) and the dividend on a 3% DOE; buybacks
  *"at a timing that it deems optimal"*. Behind the automobile plan, in writing.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**
- **The mechanism — THE CAMOUFLAGE (the tenth registered shape, SONY 2026-09-13), in its declared form.** Not one of
  ORCL's, ARM's, BE's, BA's, SWK's, ACVA/FLNC/NEGG's, CNR's, RGTI's, BAM's WAREHOUSE or TM's PASS-THROUGH: **the company
  does not die; the owner's return does**, because a franchise leg's cash (motorcycles, ¥2,752bn of five-year segment
  profit) and a lender's distributions are recycled into a leg that must re-win a technology and cost race every model
  cycle (automobiles, (¥387bn) over the same five years), and the consolidated series hides the rate earned on the
  recycling [E2-56]. **Honda differs from Sony in one way that sharpens the shape: the filing announces the transfer**
  (*"leverage … the strong profitability and cash generation capabilities of the Motorcycle business"*) and sizes the next
  round (¥6.2tn, FY3/27–29). It shares TM's PASS-THROUGH only in industry, not in mechanism: Honda did not over-spend to hold
  units; it under-spent and lost them, then wrote off the bet it made instead. **No new shape is named; the register stays at
  eleven.**
- **Quantified from filed figures [E3-24]:** if the automobile leg earns its FY3/22–25 pre-write-off average segment
  margin (2.0%, including FY3/24's 4.1%) on FY3/26's ¥14.2tn of sales, it contributes ~¥285bn a year before tax on
  ¥12.5tn of segment assets (2.3%), beside motorcycles' ~¥730bn on ¥2.7tn; **the ¥6.2tn plan then needs roughly ¥620bn a
  year of added pre-tax profit to earn 10% on itself — more than the whole swing between the automobile leg's best
  pre-write-off year (¥560.6bn, FY3/24) and its worst ((¥16.6bn), FY3/23).** The tail at the lender: [E3-24]'s own arithmetic, 10% of the ¥9.90tn receivables and 10% of the ¥6.43tn
  lease book each losing 30%, is **¥490bn — 15% of the arm's equity and 4% of group equity**; survivable from industrial net
  cash. Exposure, not experience [E4-40]: residual values are set by the used-car market Honda's own EV cancellations and
  US tariffs have just moved.
- **Likelihood:** insolvency — **a low-level possibility** on the filed balance sheet; **the camouflage — likely**: five
  consecutive years of automobile margin at or below 4.1%, a ¥1.58tn reversal, additional FY3/27 losses promised, and a
  consolidated loss-making Astemo entering the perimeter.
- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival** — it survives: strength (2) is ample, (3) is covered by it, and
  (1) is large if unreliable. **The named death is the owner's return, not the company.**

⛔ **Q5 does not open for entry.** Q1 IN · **Q2 OUT**. Q3 and Q4 are recorded above, not governing. Everything
below carries operator rule 3's header and no entry language.

---
## COMPUTATION — NOT A CLEARANCE

### THE PRICE AND THE PASS/FAIL LINE (the operator's instruction of 2026-09-01)
- **Price: ¥1,664** (7267.T close 2026-09-11, Yahoo — aggregator, live quote only, flagged). ADR **$32.52** (same date,
  same flag), **1 ADS = 3 shares** (20-F cover).
- **Shares: 3,893,016,583** (issued 4,533,000,000 less treasury 639,983,417 at 2026-06-30, Q1 FY3/27 results 6-K
  2026-08-05 `0001193125-26-333722`; the 20-F cover's 3,892,580,441 at 2026-03-31, accession `0001193125-26-274991`,
  reconciles exactly). No split after the measurement date; the October 1, 2023 three-for-one split is already in the
  count and the price.
- **Market cap: ¥6,478bn (≈ ¥6.48 trillion).** Sovereign: **JGB 30-year 3.995%, Japan MOF, 2026-09-10.**
- **PASS/FAIL: FAIL — the file closed at Q2, OUT on the business as constituted** (Q1 IN; Q2 OUT; Q3 IN and Q4 IN
  recorded, not governing).

### What the buyer is paying for, in words
**A cash-rich balance sheet and a lender, with the world's most profitable volume motorcycle business inside it and a
car company attached that has not earned 5% on its sales in eleven years.** At ¥1,664 the cap is **¥6.48tn** — almost
exactly **industrial net cash (¥3.32tn) plus the finance arm's equity (¥3.18tn)**, and 0.55x book. The buyer is paid for
that: the five-year industrial owner earnings capitalise at **8.6%**, **11.7%** with the lender's paid-up distributions
beside them. **What the buyer is also buying is the ¥6.2tn the filing commits to the automobile leg over three years**,
with further EV losses promised and a loss-making Astemo arriving — the reason the net cash is not the owner's to count.

### 1. THE YIELD
| Owner earnings (Q4) | ÷ cap ¥6,478bn | per share | points over the JGB 3.995% |
|---|---|---|---|
| **5-yr default, industrial, (c) = capex, EV provision charged ¥558bn** | **8.61%** | ¥143 | **+4.6** |
| 8-yr, industrial ¥486bn | 7.50% | ¥125 | +3.5 |
| 3-yr, industrial ¥671bn (contains the FY3/24 weak-yen year) | 10.36% | ¥172 | +6.4 |
| 5-yr before the write-off (FY3/21–25), industrial ¥632bn | 9.76% | ¥162 | +5.8 |
| 5-yr industrial + finance arm's paid-up distributions ¥761bn | 11.75% | ¥196 | +7.8 |
| 8-yr industrial + distributions ¥637bn | 9.83% | ¥164 | +5.8 |
| high end: 3-yr, EV provision not charged, + distributions ¥1,075bn | 16.59% | ¥276 | +12.6 |

*Not netted, and why:* industrial net cash ¥3.32tn (¥854 a share) is committed in the filing's own words (EV provisions
¥647.5bn, the US$2,530M building purchase, Astemo ¥152.3bn, the ¥6.2tn plan, the finance arm's ¥4.5tn of current funding
it stands behind); netting it would lift the five-year industrial yield to ~17.7%, **a number this run does not use**,
because the filing has already spent it.

### 2. WHAT THE PRICE ALREADY ASSUMES
- **Perpetual growth needed for a ~10% expectancy** (yield + growth, the engine [E3-34], casting no vote): **1.4%** on the
  five-year industrial base, **2.5%** on the eight-year; **none** once the lender's distributions are counted, or on the
  three-year base.
- **What the business has actually done:** industrial owner earnings have **no usable growth rate** (¥347bn FY3/22 →
  ¥1,368bn FY3/24 → ¥(3)bn FY3/26). Motorcycle segment profit grew **23.8% a year in yen** FY3/22–26 (¥311.5bn → ¥731.9bn)
  on consolidated units +8.2% a year; automobile segment profit went ¥236.2bn → (¥1,411.1bn).
- **[E4-35]'s base rate:** the requirement is low single-digit — not the long shot — **but [E4-44] caps value growth at
  earnings growth, and the earnings that must grow are the automobile leg's**, where the filed record is a 4.9% best margin.
  **What bounds the upside [E2-63]:** India and Brazil two-wheeler volume, the ICE-to-battery transition in Asian
  two-wheelers, US tariffs, and whether ¥6.2tn earns more than the leg it goes into has ever earned.

### 3. WHAT YOU ARE PAID
**+3.5 to +12.6 points over the JGB** on the owner-earnings range; **+4.6 on the default construction.** No per-name premium
was added to the rate [E3-42].

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01] — engine display, no vote
- Capitalised at the ~10% floor **with no growth**, net cash not added: **roughly ¥1,250 to ¥1,750 a share** on industrial
  owner earnings (8-yr to 3-yr); **roughly ¥1,650 to ¥2,250** with the lender's paid-up distributions counted.
- At the floor **with 3% perpetual growth** (a stated assumption, not a finding): **roughly ¥1,800 to ¥3,250 a share.**
- **Current price ¥1,664 — inside the range on every construction**, at the low edge of the with-distributions range and
  near the top of the industrial-only no-growth range.

### THE FLOOR, THEN THE RANKING [E4-28, E4-21]
- Honest pre-tax expectancy at this price: **~7.5% to ~12% before growth** on the governing constructions (industrial,
  and industrial plus paid-up distributions), **around the floor, not clearly above it.** On the default industrial figure
  alone it is **below** the floor unless ~1.4% perpetual growth is assumed.
- **Bar: screamer test [E4-01]** — the price is **inside the range**: *"no useful conclusion — move on."* It is not
  startlingly low against the conservative case (¥1,250 on eight-year industrial owner earnings). **Windage count: one** —
  the capex end of (c) (itself argued generous); the EV provision charge is a cost, not a margin; the window spread and the
  finance-arm treatment are carried as range, not stacked. No end margin is applied because no entry is under consideration.
- **Price at which the floor would be met on the conservative end, if Q2 were ever reopened** (recorded in words; **no alert
  armed** — a Q2 failure is a business failure, the QLYS ruling of 2026-09-07): **a cap of ~¥4.9tn on eight-year industrial
  owner earnings, ~¥5.6tn on five-year — roughly ¥1,250–¥1,450 a share.**

- **VERDICT: not reached — the file closed at Q2. This block is a computation, not a clearance.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

### ⚠ RECORDED, NOT GOVERNING — nothing is owned and nothing is armed.
**Pre-committed [E1-02] — what would make Q2 worth re-running (the reversal conditions, in words):**
1. **Perimeter, the HAS condition.** The capital moves to the franchise: the motorcycle business separated or listed, or
   the automobile leg's share of industrial capex and R&D falling below half for three filed years while motorcycles stay
   the majority of segment profit. *(FY3/26: automobiles took 85% of industrial capex and 88% of R&D expenditure.)*
2. **Direction [E4-32].** Automobile segment margin, including equity-method income and EV charges, at or above the
   filed volume-peer median for three consecutive years, on flat-to-rising group units **[E4-55]**, not on the yen.
3. **Capital allocation.** Filed returns on the ¥6.2tn FY3/27–29 plan: the 20-F's own test is *"eliminate EV-related
   losses"* by FY3/29 and *"ROIC … 10%"* in FY3/31; a buyback programme announced with a stated intrinsic-value basis
   ([E5-25]'s published-conditions standard) rather than beside a merger MOU.
- **Thesis-breaking for the OUT verdict** (what would show it was wrong): the motorcycle franchise carrying the whole at
  high returns on the incremental capital through the battery transition in India and ASEAN, **and** the automobile leg
  earning its cost of capital without further write-offs through FY3/29 — both, not either.
- **Next catalysts:** Q2 FY3/27 results (≈ early November 2026) with the first read on EV provision utilisation and supplier
  claims (Note 31); **Astemo closing "by the end of the third quarter of the fiscal year ending March 31, 2027"**; the FY3/27
  20-F (≈ June 2027), the first year of the ¥6.2tn plan and the first on the Astemo perimeter.

**The sell rule [E2-28]** — not applicable; no position. **The monitoring question [E3-30, E4-17]:** is the automobile
leg's collapse an aberrational cycle (tariffs, one EV reversal) or a permanent slippage? Eleven filed years with a best
margin of 4.9% answer most of it already; the plan's first two years answer the rest. **Position size:** none. **[E5-14]**
not engaged.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN** — the reopening conditions are written, dated and falsifiable; no band is
  armed and no PORTFOLIO row is added (FOLD step 4, gate-clearers only).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, **Q2 OUT (closes)**; Q3–Q6 recorded under explicit
      "RECORDED, NOT GOVERNING" banners; the price under COMPUTATION — NOT A CLEARANCE with no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's motorcycle row takes 7 makers (TVS
      on EBITDA only) and names the missing ones; the class (NARROW) does not govern, because the verdict turns on the automobile leg's
      share of capital, which is filed by Honda. The unaudited split cash-flow schedule was reconciled to the audited
      statement before use.
- [x] Every UNRESEARCHED verdict names the artifact — none used.
- [x] Every UNKNOWABLE verdict states what cannot be known — none used.
- [x] Step 0: the FY3/26 20-F was read (Items 3, 4, 5 in full, 6.B, 8, 15, 16E; F-8 to F-12 statements; Notes 4, 5, 17, 24,
      31), accession `0001193125-26-274991`; 20-Fs FY3/18, FY3/21–FY3/25 for the segment notes; 149 6-Ks 2021-04 to
      2026-08-31; cross-check: consolidated OCF FY3/25 ¥292,152M = XBRL = filed statement = sum of Honda's split schedule.
- [x] Owner earnings on multi-year means; four windows; (c) disclosed as a judgment with the default named and the exception
      class argued on Honda's own filed units (capex 0.95x D&A over ten years while automobile units fell); the lender
      separated at its dividend line and carried as a second component; FY3/26 EV provisions charged and shown both ways;
      SBC resolves and is complete (trust schemes only, ≤¥3bn a year); lease repayments restored as a cost (CONVENTION,
      stated); look-through shown and not used; **no mean crosses a perimeter** (Nissan never closed; Astemo not closed;
      Yachiyo sized immaterial).
- [x] Competitor rows filled: motorcycles 7 peers, automobiles 10 peers, every figure with accession or URL in
      `peers_moto.md`, `peers_auto.md` and the TM transcription (spot-checked twice against filing text).
- [x] Sovereign for the earnings currency (JPY, argued on 88% foreign sales and ~84% foreign pre-write-off profit; USD shown),
      from the issuing authority (Japan MOF), dated 2026-09-10; tenor 30Y.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar (screamer); windage count stated: one.
- [x] Prices dated; aggregator used for live quotes only and flagged.
- [x] Ledger ids checked against `principle_ledger.csv` before citing (every id cited exists; the check script listed none
      missing). The brief's own ids were used as given: [E4-27] for incentives and [E4-52] only for converging flags.
- [x] Run committed to git with a pathspec, section by section (Step 0 `030ab5c`, Q1 `4afe80c`, Q2, Q3–Q6, audit/fold).

**Errors caught in this run before commit, recorded rather than hidden:** (1) Q1's first draft put **57%** of automobile
revenue in North America — that was the company-wide share; the segment figure is **66.5%**. (2) Q3's first draft priced the
FY3/26 buyback on ~4.2bn shares (**¥6.2tn**); the filed average share count is 3,997,276,887 (**¥5.9tn**, 9.5% yield). (3) Q4's
first draft said the automobile leg's yen revenue rose "on units down" — group units fell, consolidated units rose from the
FY3/22 chip trough; both now stated. (4) Q4's first draft said the ¥6.2tn plan needed "more than twice" the automobile leg's
best-less-worst swing; it needs slightly more than that swing, not twice it. (5) Q4's first combined range took its low end
from the D&A construction the same section calls INVALID; corrected to the governing (c). (6) Q2's first draft said Hero's
Indian share "is larger than Honda's" — no Honda share is filed, so the comparison was removed. (7) Q2's Tesla pooled gross
margin was first written 20.9%; the arithmetic is 20.3%.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Honda is the world's largest and one of its two most profitable volume motorcycle makers (18.2% margin,
  22.1M units, 72% of five-year segment profit) bolted to a car company that has not earned 5% on sales in eleven filed
  years and takes 79% of the industrial assets, 85% of the capex, 88% of the R&D and a ¥6.2tn plan; Q2 OUT on the business as
  constituted. Price ¥1,664 × 3,893,016,583 = ¥6.48tn, capitalising five-year industrial owner earnings of ¥558bn at 8.6%
  (11.7% with the lender's paid-up distributions) against a 4.00% JGB and a ~10% floor, inside the value range
  (COMPUTATION — NOT A CLEARANCE).
- **The strongest single fact against this conclusion:** at ¥1,664 the whole company is valued at less than ten times the
  motorcycle segment's FY3/26 pre-tax profit alone (¥6.48tn against ¥731.9bn), with ¥3.3tn of industrial net cash and ¥3.2tn
  of finance-arm equity on top, and Q1 FY3/27 shows the automobile leg at a 5.0% margin — the market may already be paying
  nothing for the leg this verdict turns on. The file's answer: Q2 judges the business, not the price, and the filing commits
  the motorcycle cash to that leg in writing.
