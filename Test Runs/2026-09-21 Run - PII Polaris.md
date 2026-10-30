# Company Run - Polaris Inc. (PII) - 2026-09-21
**CIK 0000931015. NYSE. December fiscal year end. WAVE 7, name 27 of 218.**
**STATUS: COMPLETE 2026-09-25, Q1 IN / Q2 OUT. HISTORY - name claimed at 15:49 EDT 2026-09-21 (commit 62de14d); that session was killed
before filling anything. RESUMED 2026-09-24 by a fresh session, which kept this file name and the
research folder `Test Runs/_research 2026-09-21 PII/` and used nothing from the prior session beyond
the bare file. Every figure below was fetched and struck on 2026-09-24 unless its line says otherwise.**
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
- rate **5.47** % · date **09/24/2026** · source (issuing authority) **US Treasury daily par
  yield curve, 30 Yr, `home.treasury.gov` daily-treasury-rates.csv for 2026**, struck fresh by
  this run on 2026-09-24 and saved raw as `Test Runs/_research 2026-09-21 PII/treasury_2026.csv`.
  `python tools/sources.py` returned the same figure from the same source. **FRED DGS30 was not
  used.** The neighbouring rows read **5.40 (09/23)** and **5.29 (09/22)**: the long bond moved
  18 basis points in two sessions, and the 5.34% the AGCO run struck on 09/18 is already stale.
  Nothing was inherited from a brief or a neighbouring run.
- FX if the quote and the earnings differ in currency: **not required.** Polaris reports in USD
  and the quote is USD; **79% of 2025 sales were in the United States** ($5,662.3M of $7,152.0M,
  MD&A geographic table), 6% Canada, 15% other countries. The USD sovereign is the earnings
  currency's.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025, filed 2026-02-13, period 2025-12-31, accession `0001628280-26-008033`**
    (primary document `pii-20251231.htm`): Item 1, Item 1A, Item 5, the whole of Item 7
    including Non-GAAP Financial Measures and Liquidity, the auditor's report and its two
    critical audit matters, the four primary statements, and Notes 1 (investment in finance
    affiliate, long-lived asset impairment), 4 (Indian Motorcycle disposal group), 8 (intangibles),
    11 (Polaris Acceptance), 14 (product liability).
  - **10-Q for the quarter ended 2026-06-30, filed 2026-07-28, accession
    `0001628280-26-050104`**: cover page, balance sheet, cash-flow statement, Note 4
    (divestitures), the tariff-refund note, the new segment note, MD&A.
  - **10-Q for the quarter ended 2026-03-31, filed 2026-04-28, accession
    `0001628280-26-027854`**: cash-flow statement and MD&A (the Q1 working-capital build).
  - **10-K FY2022, accession `0001628280-23-004043`** (FY2020-22 statements, continuing
    operations after the TAP disposal); **10-K FY2019, accession `0001628280-20-001541`**
    (FY2017-19); **10-K FY2016, accession `0001628280-17-001442`** (FY2014-16).
  - **8-Ks read**: 2025-10-14 (`0001628280-25-044839`, Items 2.02/2.06/5.02, the Indian sale
    and its impairment, with EX-99.1 and the EX-10.1 transaction bonus); 2025-11-13
    (`0001193125-25-279172`, the 2031 notes); 2026-01-09 (`0001628280-26-001582`, Item 5.02);
    2026-05-01 (`0001628280-26-029305`, Items 5.02/5.07); 2026-06-22 (`0001628280-26-044485`,
    Item 5.02 with EX-99.1); 2025-07-02 EX-99.1 (`0001628280-25-033840`, the covenant
    amendment); and the four earnings releases, EX-99.1 to `0001628280-25-046532` (Q3 2025),
    `0001628280-26-003502` (Q4 2025), `0001628280-26-027677` (Q1 2026) and
    `0001628280-26-049902` (Q2 2026). **DEF 14A filed 2026-03-17, accession
    `0001308179-26-000087`.**
  - **Competitor filings: BRP Inc. (CIK 0001748797), 40-F for FY2026 (period 2026-01-31)
    accession `0001193125-26-125055`, EX-99.3 MD&A; 40-F FY2024 accession
    `0001193125-24-079609`, EX-99.3 MD&A; 40-F FY2022 accession `0001193125-22-084532`; 6-K of
    2026-09-03 (Q2 FY2027) accessions `0001193125-26-380894` (press release) and
    `0001193125-26-380888` (interim statements).**
- figure cross-checked against the filed statement (say which): **two, by hand, by
  re-derivation.**
  1. FY2025 **net cash provided by operating activities $741.0 million**, read off the
     Consolidated Statements of Cash Flows (10-K page 48) and rebuilt from its own lines:
     (464.8) + 286.5 + 59.9 − 42.1 − 139.1 + 155.9 + 327.1 + 5.2 = **188.6 of earnings-side
     cash**, plus working capital (34.1) + 183.6 + 196.7 + 137.4 + 24.3 + 44.5 = **552.4** =
     **741.0**. It ties. *(And it is itself a finding: 74.5% of the year's operating cash was
     working capital released. See Q4.)*
  2. **Total equity $832.9 million** at 2025-12-31 on the balance sheet, rebuilt from the
     equity statement's closing row: 0.6 + 1,328.9 − 469.0 − 32.1 + 4.5 = **832.9**. It ties.
- *If the filing could not be obtained → **UNRESEARCHED**.* **Not invoked; every rung used was
  SEC EDGAR primary documents.**

**THE PERIMETER, checked before anything else (the ROKU lesson).** EDGAR shows **no 8-K after
the Q2 2026 earnings release of 2026-07-28** and no merger, tender or exchange filing of any
kind; the filings since are three Schedule 13G/13G-A holder reports. **No deal is live, so the
quote is an owner-earnings price, not a spread.** The perimeter did move, and it moved **out**:
the **Indian Motorcycle business was sold to Carolwood LP on 2026-02-02 "for a nominal sales
price"** (10-K Note 4), with **$330.4M of FY2025 charges** and a further **$12.1M** pre-tax loss
in Q1 2026 (10-Q Note 4), and Polaris **paid out $79.3M of cash** on the line captioned *"Sale
of business"* in the H1 2026 investing section. A Vietnam motorcycle plant and *"certain
manufacturing assets"* are held for sale at 2026-06-30. **The disposed business carried ~$478M
of trailing revenue** (HOG competitor row of 2026-08-31, from the same filings) inside the
FY2025 On Road segment of $926.5M.

**THE SCREEN'S ACQUISITION-LINE NOTE, READ, AND IT IS A DISPOSAL, NOT AN ACQUISITION.** The
screen row read *"NET CASH INFLOW on the acquisition line ($65M, 2% of cap) - cash acquired
exceeded cash paid."* The filings say otherwise. The inflow is the **2022 sale of TAP
(Transamerican Auto Parts)**: the FY2022 10-K investing section carries *"Proceeds from sale of
businesses, net 42.2"*, and the income statement carries *"Loss from sale of discontinued
operations, net of tax (142.6)"* (TAP was bought in November 2016; that year's cash-flow line, mostly TAP, reads
*"Acquisition of businesses, net of cash acquired (723,705)"* in thousands). The tag
layer then carries the same $42.2M for 2022 as a **negative** `PaymentsToAcquireBusinessesNet
OfCashAcquired` in the FY2023 10-K (`0001628280-24-005284`), which is how a disposal became an
"acquisition inflow"; the remaining ~$23M of the screen's $65M is small positive-sign facts in
other years (2017's $1.6M; 10-Q-only facts) that I did not chase further because none is
material to a $2,981M cap. **Recorded as a tag-layer sign artifact, not a tooling defect to fix
tonight: the flag did its job and sent a reader to the filing.** The perimeter consequence is
real and is carried into Q4: **the owner-earnings series crosses three perimeters** (TAP in
2016-2021 and out; Boat Holdings in from 2018-07-02; Indian out from 2026-02-02).

**THE PRICE AND THE CAP** *(struck by this run)*
- **Share count, quoted verbatim from the cover of the 10-Q filed 2026-07-28, accession
  `0001628280-26-050104`:** *"As of July 21, 2026, 56,903,524 shares of Common Stock, $.01 par
  value, of the registrant were outstanding."* `python Screens/cover_shares.py PII` returned the
  same filing and **56,903,524, single class / undimensioned.**
- **One equity class.** The same 10-Q balance sheet: *"Preferred stock $ 0.01 par value per
  share, 20.0 shares authorized, no shares issued and outstanding"* and *"Common stock $ 0.01
  par value per share, 160.0 shares authorized, 56.9 and 56.5 shares issued and outstanding."*
  Nothing to sum; no charter reading required.
- **Price $52.38** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart
  endpoint, `regularMarketTime` 20:00 UTC; raw response saved as `price_raw.json`). Prior closes
  in the same response: 52.94 (09-23), 54.41 (09-21), 54.07 (09-18).
- **cap = close × shares**, split-invariant, `close` and never `adjclose`:
  $52.38 × 56,903,524 = **$2,981 million.** *(The screen row carried cap_m 3,628; the whole
  difference is the quote date. Item 5 of the 10-K records a last sale of $69.33 on 2026-02-06, so the
  quote has fallen 24% since the annual report.)*

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** Polaris designs and assembles
  off-road vehicles (four-wheel utility and sport machines, the bulk of the company),
  snowmobiles, three-wheel roadsters, small European commercial vehicles and pontoon boats, and
  sells them at wholesale to about **2,400 independent North American dealers** and about 1,500
  international dealers plus 70 distributors (10-K Item 1). **Most dealers also sell a rival's
  machines**. Item 1: *"A majority of our dealers and distributors are multi-line and also
  carry competitor products."* The dealer's inventory is financed by **Polaris Acceptance, a
  50/50 joint venture with a Wells Fargo subsidiary** (Note 11), so Polaris is paid *"within a
  few days of shipment"* and the $1,781.4M of dealer receivables sits off its balance sheet;
  Polaris's half of the JV's profit arrives as one line, *"Income from financial services."*
  In return Polaris shares the dealers' interest cost and stands behind repossessions (a 15%
  annual cap, **$275.0M** for 2025). Of each sales dollar in 2025, **80.9 cents was cost of
  sales** ($5,783.3M on $7,152.0M, 83% of it purchased materials and logistics), 7.1 cents
  selling, 5.2 cents engineering, 7.6 cents administration; finance income added 1.2 cents.
  Before the year's impairments and the Indian loss, that leaves **about one cent of operating
  profit on the dollar in 2025** (operating loss $(348.7)M, plus $52.6M goodwill impairment,
  $330.4M disposal loss and $53.9M of intangible impairment in G&A = $88.2M, **1.2%**); in 2023
  it was 7.8 cents, in 2014 it was 16.0 cents. Cash follows volume through a large
  working-capital block (inventories $1,412.4M at year end, 20% of sales) that empties when
  the company cuts shipments to dealers and fills when it ships ahead of retail.
- **The scarce input this business controls:** the **brands on the North American off-road
  market-share leader** (RANGER, RZR, Sportsman, GENERAL, all listed as key trademarks in
  Item 1), the **largest ORV dealer network in North America**, and in-house engines and
  powertrains. Item 1, verbatim: *"In 2025, we continued to be the North America market share
  leader in off-road vehicles."* **It is not an exclusive input**: the same dealers sell the
  competitor's product, and the competitor row at Q2 tests whether leadership earns anything.
- **Will the fundamentals look broadly the same in ten years?** **Yes.** Farms, ranches and
  trails will still use four-wheel utility and sport vehicles, sold through dealers on floor
  plan, bought on retail credit (30% of 2025 U.S. vehicles were consumer-financed, MD&A). The
  moving parts are tariffs (a Mexico-and-China supply chain, and a 2025 tariff charge the MD&A
  calls *"notable"*), electrification, and the arrival of lower-priced Asian makers, which is
  treated at Q2 as a competition question, not here as a comprehension one. The portfolio has
  been reshaped twice in five years (TAP out 2022, Indian out 2026) and the remaining business
  is simpler than the one the long series describes.
- **VERDICT: [x] IN**
  *An assembler of discretionary vehicles selling through independent multi-line dealers with
  an off-balance-sheet floor-plan JV. The economics can be written in four sentences and none
  of them rests on anything "unverified", "general knowledge" or "provisional": every figure
  is off the filed FY2025 statements, Item 1 and Note 11.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** · no close substitute **[ ] FAILS** · not price-regulated **[x]**

**Clause (2) fails on the registrant's own words.** Item 1, the Off Road segment:

> *"The ORV industry in the United States, Canada and other global markets is highly
> competitive. As an ORV original equipment manufacturer (“OEM”), our competition primarily
> comes from North American and Asian manufacturers. **Competition in such markets is based upon
> a number of factors, including price**, quality, reliability, styling, product features,
> warranties and a manufacturer’s ability to produce vehicles to meet changing consumer
> demand."*

Snowmobiles, the same Item: *"Competitive market share position is driven heavily by product
news (styling, technology, performance) and **pricing**."* *(The FY2022 10-K,
`0001628280-23-004043`, had the last words as "**attractiveness of promotional incentives**".)*
Item 1A, headed *"We face intense competition in all product lines"*: *"Certain of our
competitors are more diversified and have advantageous manufacturing footprints, and may
invest more heavily in intellectual property, product development, promotions and advertising
or online presence."* And the sales and marketing paragraph of Item 1: *"We make available and
advertise discount or rebate programs, retail financing or other incentives for our dealers
and distributors **to remain price competitive** to accelerate retail sales to consumers."*
**A product sold beside its competitor on the same dealer's floor, on price and incentives, is
a product the customer thinks has close substitutes. [E3-03] criterion (2) is not met.**

- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]**
  Not the rebuilt-from-zero class: an RZR or RANGER platform is refreshed every few model
  years and defended by engineering spend ($371.9M in 2025, 5.2% of sales), which is
  **defence of the same advantage, not purchase of its replacement** in the framework's scope
  paragraph. So [E4-04]'s competence limit is **not** why this file closes, and the
  UNKNOWABLE perimeter close is refused explicitly: the franchise question is answerable from
  the filings, and the answer is negative. The applicable doctrine is **[E2-58]**'s commodity
  end, whose one exception is *"a cost advantage that is both wide and sustainable … By
  definition such exceptions are few."* The row below tests for it.
- **Primary moat metric, filing-sourced, and its trend: gross margin and operating margin,
  twelve years, from Polaris's own four 10-Ks** (FY2016, FY2019, FY2022, FY2025; income
  statement lines divided by sales; 2020-22 on the continuing-operations basis the FY2022 10-K
  restated after TAP was sold):

  | | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | sales $M | 4,479.6 | 4,719.3 | 4,516.6 | 5,428.5 | 6,078.5 | 6,782.5 | 6,281.4 | 7,439.2 | 8,589.0 | 8,934.4 | 7,175.4 | 7,152.0 |
  | gross margin | **29.4%** | 28.4% | 24.5% | 24.4% | 24.7% | 24.3% | 24.4% | 23.5% | 22.8% | 21.9% | 20.4% | **19.1%** |
  | operating margin | **16.0%** | 15.2% | 7.8% | 6.6% | 8.0% | 7.1% | 8.3% | 9.6% | 9.4% | 7.8% | 4.1% | **(4.9)%** |

  **And the core segment alone, so that acquired mix cannot explain it**: ORV/Snowmobiles
  (FY2016 and FY2019 10-Ks), then Off Road (FY2022 and FY2025 10-Ks), segment gross margin:
  **32.3% (2014), 32.1%, 27.7%, 29.5%, 28.4%, 28.6% (2019), 27.1% (2020), 23.9%, 23.7%, 21.9%,
  20.3%, 20.2% (2025).** Twelve points lost in the franchise segment itself over eleven years.
  *(Limit stated: the segment perimeter and the corporate cost allocation were redrawn in 2020
  and again in 2026, and Section 301 tariffs from 2018-19 and the 2025 tariffs sit inside the
  later years; none of that reverses a twelve-point fall, and tariffs are paid by every
  importing competitor, which is what the row tests.)*

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.

| Company | same metric: gross margin / operating margin, as filed | same window: five fiscal years ≈ calendar 2021-2025 | source |
|---|---|---|---|
| **Polaris (subject)** | GM 23.5 · 22.8 · 21.9 · 20.4 · **19.1**; **mean 21.5%**; OM 9.6 · 9.4 · 7.8 · 4.1 · **(4.9)**; **mean 5.2%** | FY2021-25 (Dec) | income statements, 10-K FY2025 `0001628280-26-008033` (2023-25) and 10-K FY2022 `0001628280-23-004043` (2021-22, continuing operations) |
| **BRP Inc.** (Can-Am, Ski-Doo, Sea-Doo), **CAD** | GM 27.9 · 24.9 · 26.3 · 22.5 · **22.4**; **mean 24.8%**; OM 15.5 · 13.6 · 14.1 · 7.0 · **4.7**; **mean 11.0%** | FY2022-26 (years ending 31 January, so FY2022 ≈ calendar 2021) | "Selected Consolidated Financial Information", EX-99.3 MD&A to 40-F FY2026 `0001193125-26-125055` (FY2024-26, continuing basis after the Marine disposal) and to 40-F FY2024 `0001193125-24-079609` (FY2022-23, Marine still inside at ~5% of revenue) |

**BRP out-earned Polaris in every one of the five years on both metrics**, at the top of the
cycle (2021-22: GM 27.9% and 24.9% against 23.5% and 22.8%; OM 15.5% and 13.6% against 9.6%
and 9.4%) and at the bottom (2025: GM 22.4% against 19.1%; OM 4.7% against (4.9)%). **Read with
its limits, which cut both ways and are stated rather than netted:** (i) BRP's FY2026 operating
income carries a **CAD 229.8M impairment** (EV assets and the light-mobility unit); without it
BRP's FY2026 operating margin is **7.5%**. Polaris's 2025 carries the $330.4M Indian disposal
loss and **$106.5M** of goodwill and intangible impairment; without them Polaris's is **1.2%**.
On that like-for-like basis the gap in the trough year is **6.3 points, not 9.6.** (ii)
Polaris's operating line **includes** $84.3M (1.2% of sales) of JV finance income; BRP has
no captive finance and no such line, so Polaris is **flattered** by about a point every year and
still trails. (iii) The fiscal years are offset by one month and the currencies differ; margins
are unitless and a one-month offset cannot account for a five-to-six-point mean gap. (iv)
BRP's FY2022-23 figures include its small Marine segment (CAD 512.8M and 489.6M of revenue,
about 5%), which **lowered** BRP's reported margin in those years.

- **The row's second witness, from BRP's own filings: share is moving toward the attacker.**
  BRP's FY2026 MD&A: retail growth *"driven by … market share gains in ORV and Snowmobile"*;
  its Q2 FY2027 release (2026-09-03): *"Market share gains for ORV in North America."* Polaris's
  own Q2 2026 release claims ORV share gains in an overlapping quarter, so both cannot be taking
  it from each other alone; BRP's 40-F risk factors name who else is in the market: *"growing
  competition from Asian manufacturers entering the powersports market … These competitors are
  increasingly offering products with lower MSRPs, which may not only accelerate pricing
  pressures but may also intensify the challenge of maintaining and growing the Company’s market
  share."* A market whose two leaders both describe a third, cheaper entrant is not a market
  with no close substitute.
- **Peers named: 1 of the industry's real competitors at a comparable metric, and the rest are
  named with the reason each is excluded.** Polaris's Item 1 names none by name (*"North American
  and Asian manufacturers"*). The real ones: **BRP** (taken, the only pure-play powersports
  filer at the SEC); **Textron** (Arctic Cat, inside Textron Specialized Vehicles, which sits
  in the Industrial segment with Kautex and reports one combined segment profit, **not
  separable**); **Honda** (20-F filer, but ATVs and side-by-sides sit inside a Motorcycle segment
  dominated by Asian commuter motorcycles, **not comparable**); **Deere** (Gator, inside Small
  Agriculture and Turf, **not separable**); **Kawasaki, Yamaha, Kubota** (Tokyo-listed, **no SEC
  filing; the rung that stops is exchange filings/EDINET, EDINET blocked by a paid key**);
  **CFMOTO** (Shanghai-listed) and **Hisun, Segway and other Chinese makers** (not SEC
  registrants). Buffett's eight **[E3-28]** is not reachable at a comparable metric. **The row is
  not PROVISIONAL**: the one competitor that can be measured the same way is the one both
  companies' filings identify as the rival that matters, it is Polaris's size, and it wins every
  year; the unmeasured class is either inside conglomerates or, by BRP's own account, **cheaper**,
  which can only widen the gap against a claim of no close substitute. *(For the 7% Marine
  segment the MCFT run of 2026-09-20 built a seven-filer row, `Test Runs/2026-09-20 Run - MCFT
  MasterCraft Boat Holdings.md`: Brunswick's gross margin exceeded Polaris's consolidated figure
  in every year 2019-2025, and Polaris Marine's own segment gross margin fell 22.1% → 16.8% →
  14.2% over 2023-25 against Brunswick's 27.9% → 25.8% → 24.8%. Not rebuilt here; the segment
  cannot carry a franchise the core lacks.)*
- **Untapped pricing power — could a manager raise the return simply by raising prices, and has
  not? [E3-33]** **No; the MD&A reports the opposite in the latest full year.** Polaris does not
  disclose a clean price number: its sales bridge combines *"Product mix and price"*, which read
  **+6% (2015), (1)% (2016), +3% (2018), +6% (2019), +8% (2021), +16% (2022), +1% (2024), +3%
  (2025)** (FY2016, FY2019, FY2022 and FY2025 10-Ks). What it does say in words is decisive for
  **[E2-44]**'s first characteristic, raising prices *"even when product demand is flat and
  capacity is not fully utilized"*: 2025, with volume down 3%, *"lower net pricing driven by
  higher promotional costs"* (MD&A overview, sales discussion and the Off Road segment, where
  *"The average per unit sales price for the Off Road segment decreased approximately two
  percent, primarily due to lower net pricing driven by higher promotional costs."*); 2016, with
  volume down 5%, mix-and-price **(1)%** and gross margin down *"due to increased warranty and
  promotional costs"*. **[E4-37]**'s inverse metric reads at the agony end: when demand softens,
  this company pays to hold volume. **The 2026 recovery is recorded as the disconfirming
  evidence it is**: the Q2 2026 release reports *"positive price and lower promotions"* and
  Powersports segment gross margin of 25.1%, **but $66M of that segment's quarter was a tariff
  refund** (the release: *"Results include a tariff refund of approximately $66 million"*), the
  price rise follows a year of discounting, and it arrives alongside BRP's claim of share gains
  in the same market. One recovering quarter does not reverse a twelve-year slope.
- **[E4-55], where units exist, monitor units.** Polaris discloses no unit series of its own,
  only the industry's (management estimates): North America ORV retail **820,000 (2023) →
  775,000 → 780,000 (2025)**, snowmobiles worldwide **125,000 → 110,000 → 90,000** seasons
  2023-25 (Item 1). Its sales bridge gives volume at **(21)% in 2024 and (3)% in 2025.** The
  FY2016 10-K attributes that year's 9% ORV sales fall in part to *"heightened competitive
  product offerings"* and the snowmobile fall in part to *"market share declines."* There is no
  hidden volume gain behind the dollar series.
- **[E3-46], the second question about the business is a number, and it is the strongest thing
  against this verdict, so it is stated in full.** On **[E2-43]**'s unleveraged net tangible assets
  (total equity plus debt as captioned, less cash, less goodwill and intangibles, each from the
  year-end balance sheet in the four 10-Ks), pre-tax operating income earned **68% in 2015**
  (716.1 on 1,051.5), **42% in 2019** (483.7 on 1,139.6), **42% in 2022** (804.5 on 1,914.3),
  **13.6% in 2024** (290.6 on 2,142.5) and **6.1% in 2025** (88.2 before the impairments and the
  Indian loss, on 1,434.4). An assembler whose dealers' floor-plan lender pays it within days
  employs little tangible capital, and for years this one earned very high returns on it. **Two
  reasons it does not rescue the franchise:** with **the goodwill wedge put back** (the $1.5bn of
  goodwill and intangibles carried at 2019, mostly TAP and Boat Holdings, paid for in cash) the
  2019 return is **18.4%** and 2022's **28.5%**, and the acquired part of that wedge has since been
  written down or sold at a loss (Q3 below); and the return is **falling with the margin**, not
  holding against it. Operating margin **halved in 2016 and never returned**, and the 2021-22 peak
  (9.6% and 9.4%) was below the 2015 level on a sales base 58% to 82% larger. **[E4-32], direction
  outranks existence**: whatever the advantage was in 2014, it has **narrowed in nine of eleven
  annual steps** on gross margin.
- **[E4-36], which of the four causes of extreme success?** The 2014-15 record looks like the
  first cause, one variable at an extreme (the RZR sport side-by-side, which created a category),
  and the category was then entered by everyone; BRP's Can-Am Maverick line and the Asian makers
  followed. What is left is **wave-riding** in 2020-22 (a pandemic outdoor-recreation boom that
  lifted every powersports and boat maker at once, the MCFT run's seven-filer row shows it), and
  *"the advantage lives in the wave, not the surfer"* **[E3-51]**.
- **[E2-53] dominance and [E5-18] stand-a-little-mismanagement.** Leadership has not set the
  economics: the market-share leader earns less than the number two every year of the row. And
  the business did not stand a stumble: the 2016 RZR recalls cost ~200 basis points of "one-time"
  gross margin (FY2016 10-K) and the margin never came back.
- **[E2-45], the attacker's test**, is not hypothetical here: BRP ran it from a smaller base
  and now out-earns the leader, and the Asian makers are running it again at lower prices.
- **[E5-28] scope check:** claiming the untapped-pricing class would be claiming near-monopoly.
  The row refuses it.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: NARROWING.** Proportionally
  Polaris's operating margin fell from **62% of BRP's in 2021** (9.6/15.5) to **16% of BRP's
  ex-impairment figure in 2025** (1.2/7.5).
- **VERDICT: [x] OUT**

  **[E3-03] clause (2) fails on the registrant's own words (competition on price, incentives
  "to remain price competitive", multi-line dealers carrying competitor products), and
  [E2-58]'s single exception, a cost advantage both wide and sustainable, is refuted by the
  competitor row: the one comparable rival out-earned Polaris in each of five years, at the peak
  and at the trough.** This is a finding about the business, from evidence in hand, so it is
  **OUT and not UNRESEARCHED or UNKNOWABLE.** The separating test, asked aloud: *can I name the
  document that would resolve this?* No; the two companies' own filed statements are the
  document, and they agree, and Polaris's own twelve-year series agrees with them.

  **What this verdict does not say.** It does not say Polaris is badly run, or that RANGER and
  RZR are weak brands; it is still the North American ORV share leader by its own account, and
  2026 is recovering. **[E3-61]** binds the row: it shows position, never conduct. What it says
  is that on the corpus's franchise test, a leader whose core-segment gross margin fell from
  32.3% to 20.2% in eleven years, which cuts price with promotions when demand softens, and which
  earns less than its nearest rival at every point of a cycle, **has no franchise to buy.**

  **Q2 OUT is permanent and it closes the file.** Q3, Q4 and the price arithmetic below are
  recorded **WITHOUT VERDICTS**, under operator rules 2 and 3.

---
# BELOW THE CLOSE: MATERIAL RECORDED WITHOUT VERDICTS

**Operator rule 2 (HARD SEQUENCE).** Q2 returned OUT. Nothing below carries a verdict, no box
is ticked, and no entry language appears anywhere in it. The material is recorded because the
standing brief for this wave requires the owner-earnings rebuild, the SBC check, the
earnings-release read and the proxy read on every name, and because a reader reopening Polaris
deserves the evidence rather than a summary of it.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? MATERIAL ONLY, NO VERDICT
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`, read before this section.*

**STEP 1: THE WEIGHT CASE, declared.**
- [x] **Daily execution** **[E3-38]**. Declared from Q2's own finding: the 1991 original says
  *"a business, unlike a franchise, can be killed by poor management"* **[E3-43]**, and Q2 found
  a business, not a franchise. Polaris re-wins its dealers' floor space every model year against
  a rival that out-earns it, sets promotions quarter by quarter, and runs a Mexico-and-China
  supply chain through a changing tariff regime. That is have-to-be-smart-every-day.
- [ ] **Control** **[E1-16]**: a minority purchase of a listed company; not ticked.
- [ ] **Leverage** **[E3-29]**: **not ticked, and it is close.** Debt to total capital was **70%**
  at 2026-06-30 on the company's own statement (10-Q MD&A), total financing obligations
  **$1,951.3M** against total equity of **$841.0M**, and the credit agreement's covenant relief
  period ended on 2026-06-30. This is not the 20:1 of a bank, where small asset errors destroy
  equity; it is an operating company with a leveraged capital structure. Carried at Q4.
- **Case declared: one determinant high, so Q3 would be a binary GATE and no price would
  compensate.** Recorded; it governs nothing here because Q2 has closed the file.

**Honesty, dated to when each matter became public [E5-16].** *(A Q3 pass would be the absence
of found disqualifiers, never a finding that the managers are honest [E5-17].)*
- **2018-04 (10-Q for the quarter ended 2018-03-31, accession `0001628280-18-005117`):** *"On
  April 2, 2018, the Company agreed to a $27,250,000 settlement with the Consumer Product Safety
  Commission that resolves two 2016 late-reporting claims."* A company settlement for **late
  reporting of product-safety hazards to the regulator**, which is a conduct matter touching
  candor, not a business mistake. **[E5-22]**: penalty size is not seriousness in either
  direction. The FY2017 10-K (`0001628280-18-001709`, filed 2018-02-15) had already accrued it
  under the words *"At December 31, 2017 and 2016, the Company has accrued for probable losses"*
  without naming it; the 10-Q named it the quarter after it was agreed. **This is a corporate
  settlement without individuals identified in any filing I read, the same reading question the
  UMC run (2026-09-13) raised for the operator about a corporate plea.** No verdict is set here
  and no precedent is claimed.
- **Class actions, continuing:** the fire-hazard and heat-hazard putative class actions (filed
  2016 and 2018, FY2019 10-K Item 3) and the California rollover-protection certification class
  actions (*Guzman/Albright*, first reported in the FY2020 10-K, a California class certified
  2023-09-27, FY2025 10-K Item 3). The company says it cannot estimate the loss. Product
  liability accrual **$374.1M** at 2025-12-31 (a critical audit matter for EY), **$255.0M** at
  2026-06-30, with probable insurance recoveries falling from $182.5M to $55.7M over the same six
  months (10-Q product liability note).
- **Board:** the Audit Committee chair since 2013 resigned from the Board effective 2026-01-14,
  the 8-K (`0001628280-26-001582`) stating *"not the result of any disagreement with the Company,
  its management, the Board, or any committees thereof."* Recorded as a date, not a flag.

**STEP 2: THE FLAGS [E4-22, E5-15, E4-29, E4-30], each a prompt to read.**
- [x] **EBITDA / adjusted-earnings promotion [E4-29] FIRES, and it fires in the 10-K itself**,
  not only in the releases (the CGNX lesson checked in both directions). The FY2025 10-K MD&A
  Overview, its fourth sentence: *"We reported Adjusted EBITDA of $410.2 million in 2025 compared
  to $635.4 million in 2024."* Adjusted EBITDA and its margin sit in the consolidated results
  table beside the GAAP lines. Every one of the eleven earnings releases read (Q4 2022 to Q2 2026)
  sets adjusted EPS beside reported EPS in its highlights and prints *"Adjusted EBITDA margin"*
  in its KEY FINANCIAL DATA box.
  The credit agreement tests both covenants on *"Adjusted EBITDA"*. The annual bonus was paid on
  it (below). [E5-41]'s reverse float applies literally: depreciation of **$263.5M** in 2025 is
  the largest recurring add-back in the reconciliation.
- [x] **Trumpeted projections [E4-22 third flag], with the record [E3-48]:** full-year
  guidance is issued every January, and the last three are on file against outturn:

  | year | January guidance, adjusted EPS | outturn | sales guidance | sales outturn |
  |---|---|---|---|---|
  | 2023 | *"down three percent to up three percent"* | **$9.16, down 12%** | flat to +5% | +4% |
  | 2024 | *"down 10 to 15 percent"* | **$3.25, down 65%** (lowered at Q2 and Q3) | down 5-7% | **down 20%** |
  | 2025 | *"down ~65 percent"* (about $1.14) | **withdrawn at Q1**; outturn **$(0.01)** | down 1-4% | flat |
  | 2026 | $1.50-1.60, then $1.60-1.70 (*"provided on March 3, 2026"*), then **$3.00-3.10** at Q2, *"of which approximately $0.96 is attributed to the benefit of tariff refunds"* | open | up 1-3% | open |

  *(Releases: EX-99.1 to `0001628280-23-001772`, `0001628280-24-002474`, `-24-032498`,
  `-24-043222`, `0001628280-25-002715`, `-25-020396`, `-25-036283`, `-25-046532`,
  `0001628280-26-003502`, `-26-027677`, `-26-049902`.)* Three consecutive EPS misses on the
  downside, the middle one by fifty points. **[E5-30]**: a guidance culture is a ratchet, and
  this one survived a withdrawal.
- [x] **Metric switching [E2-49] FIRES, and the switch follows the deterioration.** The 2026
  proxy (`0001308179-26-000087`), CD&A: *"in January 2025 the Committee returned to its usual
  practice of implementing only an annual incentive plan based on full-year Adjusted EBITDA
  (versus Adjusted EPS in prior years) performance results."* The year before, when 2024 adjusted
  EPS fell 65%, *"the Committee adopted a supplemental bonus plan as a strategic retention
  tool"*; and in 2025 *"The Committee did not grant performance-based restricted stock unit
  awards in 2025 for the first time in several years."* The 2023-2025 PRSUs, the ones set before
  the fall, paid **0%**. Every yardstick that read unfavourably was replaced or suspended in the
  year it read unfavourably.
- [x] **The number the bonus was paid on is not the number the 10-K publishes, under the same
  name and the same definition, and the proxy does not reconcile the two.** This is the sharpest
  finding in Q3. The AIP: *"The final performance level for 2025 Adjusted EBITDA was $538M, which
  was 106.6% of the target performance level of $505M, resulting in a payout percentage of 165.6%
  of target."* The Pay-versus-Performance table prints the same **538.2** as the company-selected
  measure. **The same proxy's Appendix A reconciles 2025 Adjusted EBITDA to $410.2M**, which is
  the 10-K's figure, and the CD&A defines the AIP measure in words identical to the 10-K's and
  says it was chosen *"because it is a well-understood financial measure communicated in the
  public disclosures of our financial results."* **The $128.0M difference is not reconciled
  anywhere I found in the document** (searched: Appendix A, the CD&A metric section, the PvP
  footnote (6), every occurrence of "reconcil"). The PvP column also carries **1,069.2 for 2023
  against the 10-K's 1,020.9**, while its 2024 figure (635.4) matches. The surrounding CD&A says
  the tariffs *"negatively affected 2025 financial performance in ways largely outside
  management’s control"*, which makes a tariff exclusion the likeliest reading, **but the document
  does not say so and I record it as unreconciled, not as explained.** The payout grid is
  threshold $227M → 40%, target $505M → 100%, maximum $556M → 200%; the target itself sat
  **$130M below 2024's published $635.4M.** CEO incentive **$2,719,747, 223.6% of salary**; SCT
  total **$11,144,637**; compensation actually paid **$14,526,291**; in a year of a $465.5M net
  loss, and with the company's own five-year TSR at **$77.64 against the S&P 1500 Leisure index's
  $95.74**. **[E2-26]**: a reader of the 10-K alone could not know the bonus measure exceeded the
  published measure by 31%.
- [x] **[E2-57] "except for" FIRES on recurring items adjusted out as if non-recurring**:
  *"Class action litigation expenses"* removed from Adjusted EBITDA in every year shown (**$8.5M,
  $7.0M, $8.0M** for 2023-25, and again in the 2026 releases), *"Restructuring"* in every year
  (**$8.2M, $23.4M, $20.1M**), *"Product wind downs"* two years running (FTR, Timbersled).
  **[E3-53]/[E5-33]**: these are real costs of this business and belong in the mean; the
  owner-earnings build below never removes them (it starts from operating cash).
- [x] **Incentives [E4-27]: a transaction bonus for giving a business away.** The 8-K of
  2025-10-14 (`0001628280-25-044839`, EX-10.1): the On Road president was offered *"a transaction
  bonus equal to four times his then-current base salary"* plus his 2025 bonus *"based on the
  greater of target and actual performance"*, **conditional on closing the Indian sale and on
  nothing about its price**; the price was *"nominal"* and Polaris paid $79.3M of cash out at
  closing. And the same agreement pays the bonus in full *"in an event that the Company in its
  sole discretion determines that the Transaction Closing will not occur."*
- [ ] **Serial share issuance [E5-15]: clean.** The count fell from about 66M in 2014 to
  **56.9M**; issuance is employee-plan only.
- [ ] **Weak accounting / unintelligible footnotes [E4-22]: no instance found** in the notes read
  (1, 4, 8, 11, 14 of the FY2025 10-K; 4 and the tariff note of the Q2 10-Q). The tariff-refund
  asset ($83.0M) is recognised on *"probable"* recovery of refund claims after the Supreme Court
  ruling, and the release separates it rather than burying it (*"$74 million of tariff refunds,
  which benefited adjusted EPS by $0.96"*), which is the candor case.
- [ ] **Filed-figure tells [E4-30]: clean.** Cash taxes as a share of pre-tax income: 37%, 36%,
  40% (2014-16), 15% (2017, the tax-reform year), 17%, 22%, 15% (2020, continuing), 20%, 26%,
  30% (2023), 88% (2024); nothing smoothed, and the post-2017 step down is the statutory rate.
- [x] **Dividends against capital [E2-60], a prompt.** 2024: operating cash **$268.2M** less
  capex **$261.7M** left **$6.5M**, against dividends of **$147.7M** and buybacks of **$82.7M**,
  and net borrowings were **$165.8M** (MD&A). 2025: dividends of **$150.3M** paid in a year of a
  **$465.5M** net loss while the credit agreement was amended to relieve the covenants. The
  31-year increase streak was preserved with borrowed money in 2024. Not issuance, so not
  [E2-52]; it is [E2-60]'s third dimension, a payout whose cost is financial strength.

**STEP 3: THE PRIMARY TEST [E2-01], balance sheet first, and scoped as its sources scope it.**
Return on year-end shareholders' equity: **46%** (2015), 25% (2016), 39% (2018), 29% (2019),
40% (2021), 41% (2022), 35% (2023), **8.6%** (2024), **(56)%** (2025). The high readings are
built on a shrinking equity base and a debt-to-capital ratio of 62-70%, which is the *"undue
leverage"* [E2-01] excludes and [E2-47] carves out. On [E2-43]'s unleveraged net tangible assets
the pre-tax series is 68% (2015), 42% (2019), 42% (2022), 13.6% (2024), 6.1% (2025), and with
the goodwill wedge put back 18.4% (2019) and 28.5% (2022) (all four worked at Q2). **The
operators' own return, judged by [E2-73] on the capital they work with, fell by five-sixths in
three years.**

**The half-owner test [E2-26].** Mixed. For the tariff refund and the Indian disposal the
reporting passes: each is quantified separately at every line of the releases and the 10-Q. For
the bonus measure it fails, as above.

**The institutional imperative [E2-30].**
- [ ] resists change: **not ticked.** The company exited TAP, Indian, Victory, FTR, Timbersled
  and the Vietnam plant; it changes direction readily.
- [x] **projects and acquisitions soak up funds**, and the record is on file: **TAP**, bought
  November 2016 (the year's acquisition line $723.7M), **$270.3M of Aftermarket goodwill impaired
  in 2020**, sold 2022-07-01 for **$42.2M** with a **$187.6M pre-tax loss on sale** (FY2022 10-K);
  **Boat Holdings**, bought 2018-07-02 (the year's line $759.8M), whose Marine segment gross margin
  fell from 22.1% to 14.2% in two years and whose goodwill ($230.6M) is an EY critical audit
  matter and whose fair value, the MD&A says, *"was particularly dependent upon future industry
  strength"*; **Indian Motorcycle**, given
  away for *"a nominal sales price"* with **$330.4M + $12.1M of charges, $52.6M of goodwill
  written to zero and $79.3M of cash paid out**; plus 2024's **$62.7M** developed-technology
  purchase and *"strategic investments"* written down in 2025 (**$49.4M** inside the $155.9M of
  impairments, the balance being the goodwill and intangible charges). **[E3-40]**: the base
  business's margin halved over the same decade that its cash went into adjacencies.
- [ ] staff studies for the leader's craving: no evidence either way in the filings.
- [ ] peers imitated: a prompt only. BRP also bought boat builders in the same years and exited
  marine in FY2025-26 (its 40-F FY2026 continuing-operations restatement); two makers doing the
  same thing is not proof that either copied the other.

**Capital allocation, the buyback conditions [E5-08, E4-31].**
- (1) **ample funds? No, in the largest years.** 2021: repurchases **$461.6M** and dividends
  **$153.4M** against operating cash of **$293.7M**, with net borrowings of **$351.3M** (FY2022
  10-K cash-flow statement).
- (2) **material discount to conservatively calculated value?** The run cannot state a value,
  because Q2 closed it; what the filings show is **10.8M shares repurchased 2021-24 for
  $1,227.9M, an average of about $113.70** (equity statements: 3.8M for $461.6M, 4.4M for
  $505.0M, 1.6M for $178.6M, 1.0M for $82.7M), against a quote today of **$52.38**, followed
  within a year by a covenant amendment that *"limits us from repurchasing shares and paying
  dividends other than regular quarterly dividends."* **CAPITAL-ALLOCATION FLAG, stated with the
  humility clause [E4-13]**: management knows the business better than I do, and *"many CEOs
  never stop believing their stock is cheap"* [E5-08]. It would bind position size, never the
  rate; no position exists.
- **Retention [E3-54]:** undefined over 2021-25, because distributions exceeded earnings:
  net income **$1,089.1M** against dividends **$748.7M** and buybacks **$1,230.3M**. The retained
  dollar was negative; the quote halved.

**THE GUARDRAIL.**
- [x] Nothing in this Q3 is used to promote the name; it could not be, the file is closed.
- [x] Key-person dependence: none recorded at Q2; the moat defect found there is competitive, not
  a surgeon.
- [x] The excisable-cancer exception **[E2-35, E2-36]** does not arise: the franchise is not
  intact, so there is nothing for a skilled surgeon to save.

- **VERDICT: not written.** Q2 closed the file.

## Q4 — WILL IT SURVIVE? MATERIAL ONLY, NO VERDICT

### Owner earnings — the one number **[E2-23]**

**Built year by year for twelve years, 2014-2025, from the filed cash-flow statements of four
10-Ks** (FY2016 `0001628280-17-001442`, FY2019 `0001628280-20-001541`, FY2022
`0001628280-23-004043` on the continuing-operations basis after TAP, FY2025
`0001628280-26-008033`). Script and every input: `Test Runs/_research 2026-09-21 PII/oe.py`.
**No net-income proxy anywhere.** Construction (the framework's CONVENTION, section VI):
operating cash flow, **plus** the 2014-16 excess tax benefit that was then classified in
financing (**$37.0M, $34.7M, $3.6M**, a real cash tax saving reclassified to operating from 2017),
**less stock compensation in full**, **plus the net cash received from Polaris Acceptance**
(distributions less contributions, both in investing; the equity income itself is removed from
operating cash by the filer as *"Noncash income from financial services"*), **less (c)**.

**SBC RESOLVES AND IS COMPLETE, checked off the filer's own line and not a tag.** The cash-flow
line is *"Noncash compensation"*: **$57.4M, $49.2M, $59.9M** for 2023-25. The notes give
share-based compensation of **$42.2M, $33.2M, $48.2M** (Note 5) and ESOP expense, stock-settled
and requiring *"no cash payments from the recipient"*, of **$17.3M, $15.2M, $16.2M** (Note 6).
The note sums are **$59.5M, $48.4M, $64.4M**; the cash-flow line is within $2.1M in 2023 and
$0.8M in 2024 and **$4.5M below the note sum in 2025**. **The larger of the two is subtracted in
every year where both exist** (59.5, 49.2, 64.4), so the Boeing class (a stock-settled plan
sitting outside the SBC tag) is inside the subtraction, not beside it. For 2014-2022 the
cash-flow line alone is used, which on the 2023-24 evidence carries the ESOP. **[E3-70]'s
grant-value measure is not needed**: SBC was 10.5% of cumulative operating cash over the twelve years, not
the >50% class where the resume state requires the grant table.

| year | OCF | + tax reclass | − SBC | + JV net cash | base | D&A | capex | OE, (c)=D&A | OE, (c)=capex | working-capital lines | OE (c)=capex, ex-WC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2014 | 529.3 | 37.0 | 63.2 | (1.3) | 501.8 | 127.5 | 205.1 | 374.3 | 296.7 | (15.6) | 312.3 |
| 2015 | 440.2 | 34.7 | 61.9 | 19.4 | 432.4 | 152.1 | 249.5 | 280.3 | 182.9 | (155.6) | 338.5 |
| 2016 | 571.8 | 3.6 | 57.9 | 35.2 | 552.7 | 167.5 | 209.1 | 385.2 | 343.6 | 179.7 | 163.9 |
| 2017 | 585.4 | 0.0 | 50.1 | 32.3 | 567.6 | 191.1 | 184.4 | 376.5 | 383.2 | 96.4 | 286.8 |
| 2018 | 477.1 | 0.0 | 64.0 | 26.8 | 439.9 | 211.0 | 225.4 | 228.9 | 214.5 | (142.2) | 356.7 |
| 2019 | 655.0 | 0.0 | 75.0 | 13.8 | 593.8 | 234.5 | 251.4 | 359.3 | 342.4 | 58.5 | 283.9 |
| 2020 | 961.8 | 0.0 | 65.3 | 69.8 | 966.3 | 235.8 | 204.3 | 730.5 | 762.0 | 319.5 | 442.5 |
| 2021 | 286.8 | 0.0 | 60.6 | 17.8 | 244.0 | 216.4 | 282.8 | 27.6 | (38.8) | (536.2) | 497.4 |
| 2022 | 534.5 | 0.0 | 62.9 | (28.7) | 442.9 | 232.8 | 306.6 | 210.1 | 136.3 | (300.1) | 436.4 |
| 2023 | 925.8 | 0.0 | 59.5 | (6.5) | 859.8 | 258.9 | 412.6 | 600.9 | 447.2 | 235.9 | 211.3 |
| 2024 | 268.2 | 0.0 | 49.2 | 58.2 | 277.2 | 286.3 | 324.4* | (9.1) | (47.2) | (67.6) | 20.4 |
| 2025 | 741.0 | 0.0 | 64.4 | 47.3 | 723.9 | 286.5 | 182.9 | 437.4 | 541.0 | 552.4 | **(11.4)** |

*\* 2024 capex includes the **$62.7M** "Acquisition of developed technology assets", carried at the
capex end as capital the business spent to keep its product line; excluding it moves 2024 by
$62.7M and the twelve-year mean by $5.2M.* D&A includes acquired-intangible amortisation
($17.7-23.0M a year in 2023-25), so the D&A end overstates (c) by about that much; recorded, not
adjusted.

**THE SCREEN'S ACCOUNTS-PAYABLE PRIOR, TESTED AGAINST THE FILED STATEMENT.** *"ONE LINE MADE THE
CASH: AccountsPayable moved 53% of 2024 OCF."* **The arithmetic is right and the inference is
backwards.** 2024's accounts-payable line was **$(141.8)M against operating cash of $268.2M
(52.9%)**: payables were **paid down**, taking cash **out**. The year the shape the screen was
looking for actually occurs is **2025, and it is not one line**: inventories **+$183.6M**,
payables **+$196.7M**, accrued expenses **+$137.4M** and the rest, **$552.4M of working capital
released, 74.5% of the year's $741.0M**, while 2025's earnings-side cash was **$188.6M**. The
liquidity note says it in words: *"The increase in net cash provided by operating activities in
2025 was primarily the result of working capital improvements."* **And it reversed at once**:
H1 2026 operating cash was **$(90.0)M** with inventories **$(169.8)M** and accrued expenses
**$(171.2)M** (10-Q). `working_capital_flag()` reads one line at a time and pointed at the right
statement in the wrong year; recorded as an observation, not a defect (the AGCO run found the
same two-line shape).

**Five windows and two (c) ends, published rather than defended [E4-38, E4-25]:**

| window | (c) = D&A | (c) = total capex | (c) = judged $253.2M | mean working-capital lines |
|---|---|---|---|---|
| 12 years 2014-25 | $333.5M | $297.0M | $297.0M | +18.8 |
| 10 years 2016-25 | $334.7M | $308.4M | $313.6M | +39.7 |
| **5 years 2021-25 (the default [E2-42])** | **$253.4M** | **$207.7M** | **$256.4M** | (23.1) |
| 5 years 2016-20 | $416.1M | $409.1M | $370.9M | +102.6 |
| 6 years after TAP, 2020-25 | $332.9M | $300.1M | $332.5M | +34.0 |
| 3 years 2023-25 | $343.1M | $313.7M | $367.1M | **+240.2** |
| TTM to 2026-06-30 | $(32.2)M | $55.9M | n/a | (H1 2026 build) |

- **(c) is a disclosed guess, placed at $253.2M, the twelve-year mean of total capital spending
  including the 2024 technology purchase.** Capex exceeded D&A in **9 of 12 years**, mean ratio
  **1.17**, on a sales base that has been roughly flat since 2019 ($6.78bn to $7.15bn): tooling
  for a model line refreshed every few years, which the D&A default [E3-44, E2-41] understates
  for this filer. Not the railroad class [E5-20]; a modest step up from the default.
- **The spread, conservative end:** the three-year window's apparent strength is **2025's
  working-capital release**; strip the working-capital lines and the capex-end series for
  **2023, 2024, 2025 reads $211.3M, $20.4M, $(11.4)M.** Working capital belongs in (c) where the
  business needs it **[E2-23]**, and over twelve years it nets to a small release (+$18.8M a
  year), so the long means are fair; the recent means are not.
- **Interest is inside every figure, and the capital structure changed under the window.** Interest
  paid was **$11.3M in 2014 and $125.5M in 2025**; the twelve-year mean is **$64.0M**. On today's
  debt the long-window means overstate what the equity now earns by about **$61M pre-tax, $47M
  after tax** at the company's own 23.8% statutory adjustment rate (proxy Appendix A, note 9).
  **Twelve-year owner earnings on today's balance sheet: about $250M.**
- **The perimeter moves under the window**: TAP inside 2016-19 (and outside from 2020 on the
  restated basis), Boat Holdings from mid-2018, Indian inside through 2025 and gone from February
  2026. Indian lost money (its disposal charges and the On Road goodwill say so) but its cash
  loss is not separately filed; **the rung that stops is the filer's own segment disclosure**,
  which gave On Road only as gross profit and moved Indian into "Corporate" in 2026. Its removal
  should raise future owner earnings by an amount I cannot measure from the filings; the
  company's own claim (an Adjusted EBITDA accretion, HOG row) is in the metric Q3 flags.
- **Combined range: roughly $50M to $420M.** The bottom is the trailing twelve months and the
  last two ex-working-capital years; the top is 2016-20. **The spread is about eight times the
  conservative end.** Per **[E4-25]**, *"Usually, the range must be so wide that no useful
  conclusion can be reached"*; this is that case, and it is also a Q4 finding in its own right
  **[E5-11]**: a distorted year sits in every window (the 2016 recall year, the 2020 pandemic
  boom, the 2021-22 inventory build, the 2024 destock, the 2025 release, the 2026 tariff refund).

### Great, good, or gruesome? **[E4-20]**: *stated, unticked; this is not a verdict*
Not gruesome by capital intensity: the business does not need growing capital to stand still,
and its twelve-year mean owner earnings are positive. **Its record is "good" in 2014-22 and
"earning little" in 2024-25**, and what makes the recent years look like [E4-20]'s third
account is not capex but price: the same capital now earns a sixth of what it did. [E4-43]'s
scope is noted: only the gruesome fails Q4.

### Staying power, all three scored **[E5-11]** *(no verdict; the scores stand as findings)*
- **(1) a large and reliable stream of earnings: NO.** Net income 502.8 → 110.8 → (465.5) over
  2023-25; ex-working-capital owner earnings 211 → 20 → (11). The 2026 recovery (Q2 net income
  $106.4M) includes **$74M of tariff refunds** that do not recur.
- **(2) massive liquid assets: NO.** Cash **$302.1M** at 2026-06-30 against financing obligations
  of **$1,951.3M**; the liquidity is a **borrowed** $1.4bn revolver with **$459.8M** drawn, which
  is [E5-39]'s *"kindness of strangers"*.
- **(3) no significant near-term cash requirements: NOT MET, and this is where it would bite.**
  (a) **The covenant relief period ended on 2026-06-30**, so from the quarter ending 2026-09-30
  the leverage test reverts from 5.50x to **3.50x** and interest cover from 2.00x to **3.00x**,
  both on trailing *"Adjusted EBITDA"*. My approximation (the covenant's definitions are not
  public in full, so this is illustrative, not a compliance finding): funded debt $1,951.3M less
  cash capped at $300M, **$1,651M**, against trailing Adjusted EBITDA of **$580.7M** (2025's
  $410.2M − H1 2025's $171.7M + H1 2026's $342.2M, releases) = **2.8x**; without the $74M tariff
  refund, **3.3x**; **at 2025's own $410.2M, 4.0x, a breach.** (b) The Polaris Acceptance
  partnership agreement *"is effective through February 2027"* (Note 11): the floor-plan lender
  that pays Polaris within days of shipment must be renewed within five months. (c) Dividends of
  about **$155M a year** at the current $0.68 quarterly rate, term-loan amortisation of $25.0M,
  interest of about $120M. (d) The $500M 6.95% notes mature **March 2029**; the revolver and term
  loan **December 2029**.
- **Leverage, named and quantified [E4-16, E3-29]**, with the corpus's coverage test **[E2-54]**:
  interest paid out of operating cash before interest, net of capex, was covered **1.05x in 2024**
  (268.2 + 141.5 − 261.7 = 148.0 against 141.5) and **1.6x on the trailing twelve months**
  (247.5 + 112.1 − 180.6 = 179.0 against 112.1). That is not *"comfortably met out of current
  cash flow net of ample capital expenditures."* **[E3-52]**: all of it is covenanted bank and
  bond debt with due dates.

### Name the specific way THIS business dies **[E2-27, E3-24]**: *modelled from exposure, not from experience [E4-40]*
- **The mechanism: survival shape #11, THE PASS-THROUGH, with #10, THE CAMOUFLAGE, as a
  feature** (`Screens/SURVIVAL SHAPES - index.md`; no new shape is proposed). The company lives;
  the gains are passed to customers. A leader facing a rival that out-earns it and cheaper Asian
  entrants holds share by paying for it in promotions (*"lower net pricing driven by higher
  promotional costs"*, 2025), and each round of platform investment by every maker is
  neutralised by the others **[E2-27]**, so the leader's margin steps down cycle by cycle
  (core-segment gross margin 32.3% → 28.6% → 23.9% → 20.2% at 2014, 2019, 2021, 2025). The
  feature: for a decade the cash from the core went into adjacencies that were then written down
  or given away (TAP, Indian, the Marine goodwill still under test).
- **Quantified from filed figures.** Each point of consolidated gross margin is **$71.5M** of
  pre-tax income on 2025 sales. 2025's operating income before the impairments and the Indian
  loss was **$88.2M**, and interest expense was **$131.4M**. **Two more points of margin given
  away in promotions, from 19.1% to 17.1%, take the pre-impairment operating line to a loss of
  about $55M before interest**, and they take trailing Adjusted EBITDA down by about $143M, which
  on the approximation above moves the reverted 3.50x leverage test from 2.8x to about **3.8x**.
  The death is not insolvency first; it is **a covenant renegotiation at the lenders' price, the
  dividend streak ended, and the equity diluted or subordinated**, while the vehicles keep
  selling.
- **Likelihood: a real possibility.** 2025 already printed the margin, the covenant needed
  relief within six months of the downturn's second year, and the only thing between 2025's 4.0x
  and today's 2.8x is one strong half with a non-recurring refund. Against: the 2026 half-year
  shows positive net price, lower promotions and share gains, and Indian's losses are gone.
- **VERDICT: not written.** Q2 closed the file.

## COMPUTATION — NOT A CLEARANCE

*Q1 IN, Q2 OUT. Q5 is not open. What follows is arithmetic only; it carries no box, no ranking
and no entry language.*

- **Owner earnings ÷ market cap** at $52.38 × 56,903,524 = **$2,981M**:
  TTM capex end **$55.9M → 1.9%**; five-year capex end **$207.7M → 7.0%**; twelve-year on today's
  debt **~$250M → 8.4%**; twelve-year as filed **$297.0M → 10.0%**; 2016-20 **$409.1M → 13.7%**.
  Sovereign **5.47%**; points over it run from **−3.6 to +8.2**.
- **The ~10% floor [E4-28]:** only the twelve-year mean as filed, which carries a 2014 interest
  bill of $11M against today's $125M, reaches it, and it reaches it exactly. On today's capital
  structure the long mean is **8.4%**, and the price would need about **1.6% a year of growth**
  from it to reach the floor; from the five-year mean, about **3.0%**; from the trailing year,
  about **8%**.
- **What the price already assumes at the bare sovereign:** capitalising $250M at 5.47% gives
  **~$4.6bn** against a $3.0bn quote, so at the long mean the quote implies **shrinkage of about
  3% a year**; at the trailing year it implies a large recovery.
- **Value as a round-number range [E4-01]: roughly $1bn to $7.5bn against $3.0bn**, about
  **$18 to $130 a share against $52.38.** That is [E4-25]'s range too wide for a useful
  conclusion, recorded as arithmetic and not as a verdict. **Windage count: ONE**, spent placing
  (c) at the twelve-year capex mean; the interest normalisation is a correction to today's
  capital structure, not conservatism, and is shown separately so a reader can undo it.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? REVERSAL CONDITIONS, NO POSITION

No position, no alert and no PORTFOLIO.md row: the name failed on the **business** (the QLYS
ruling of 2026-09-07). What would reopen Q2, written before any re-look **[E1-02]**:
- **The MD&A reporting positive net pricing, not "mix and price", in a year when shipment volume
  is flat or down**, which is [E2-44]'s first characteristic passed in Polaris's own words; 2025
  read the opposite.
- **The Powersports segment's gross margin above BRP's consolidated gross margin for three
  consecutive fiscal years**, each from its own filing, excluding tariff refunds. It has been below
  in every year of the row.
- **Core-segment gross margin back above 25% with the tariff refund excluded**, which would
  reverse part of the eleven-year slope rather than one quarter of it.
- **The monitoring question [E3-30]**: is 2024-25 an aberrational cycle or a permanent slip? The
  2016 step down never reversed, which is the prior; one half-year of 2026 does not answer it.
- Watch items that bear on Q4 if Q2 ever reopens: the 2026-09-30 covenant test at 3.50x; the
  Polaris Acceptance renewal due February 2027; any reconciliation of the $538.2M bonus measure
  to the published $410.2M.

- **VERDICT: not written.** Q2 closed the file.

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN, Q2 OUT. Q3, Q4 and Q6 carry
  material and the words "not written"; Q5's template block is replaced by the COMPUTATION —
  NOT A CLEARANCE heading, with no box, no ranking and no entry language (operator rule 3).
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's figures are
  off the filed FY2025 statements, Item 1 and Note 11.
- [x] Every UNRESEARCHED verdict names the artifact: **none issued.** The two limits met were
  named with their rung instead: Arctic Cat, Gator and Honda's ORVs sit inside conglomerate
  segments (not separable), and Kawasaki, Yamaha, Kubota, CFMOTO and Hisun do not file with the
  SEC (**exchange filings / EDINET, EDINET blocked by a paid key**); Indian's own cash result is not
  separately filed (**the filer's own segment disclosure**).
- [x] Every UNKNOWABLE verdict states what cannot be known: **none issued.** [E4-04]'s perimeter
  close was considered and refused in writing at Q2.
- [x] **Step 0: the filing was read, with accession numbers; two figures cross-checked by
  re-derivation** (FY2025 operating cash $741.0M from its own lines; total equity $832.9M from
  the equity statement's closing row). The Q2 2026 10-Q, both 2026 10-Qs' cash-flow statements,
  eleven earnings releases, five 8-Ks, the DEF 14A and three older 10-Ks were read for the
  material they are cited for.
- [x] **Owner earnings on a multi-year mean, every window published, both (c) ends and a judged
  (c) disclosed**; SBC off the filer's own line, checked against the note sums and the larger
  taken; no net-income proxy anywhere (PRIME RULE 3 as amended 2026-09-20).
- [x] **Competitor row filled** with the one comparable filer (BRP, two 40-Fs and a 6-K, accessions
  recorded), and every excluded competitor named with the reason. Not PROVISIONAL, and the reason is
  written at Q2.
- [x] **Sovereign for the earnings currency, from the issuing authority, dated**: 5.47%, US
  Treasury daily par yield curve, 30 Yr, 09/24/2026, raw file saved; FRED not used.
- [x] Value stated as a round-number range ($1bn to $7.5bn), inside the COMPUTATION only.
- [x] One bar only: none chosen, because Q5 did not open; windage count stated (ONE).
- [x] **Prices dated; the aggregator used for the live quote only and flagged** ($52.38, close
  2026-09-24, Yahoo chart endpoint, raw response saved).
- [x] **Every ledger id cited in this file resolves against `principle_ledger.csv`** (checked by
  script at the fold, zero phantoms), and `python tools/check_framework.py` PASS before the fold
  commit.
- [x] Run committed to git with pathspecs: `c9c1aa6` (Step 0, Q1, Q2) and the fold commit.

**ERRORS AND ARTIFACTS, recorded rather than smoothed.**
1. **My own error, caught before commit:** the working-capital sum for 2018 was first keyed as
   **$(141.2)M**; re-adding the six filed lines gives **$(142.2)M**. Fixed in `oe.py` with the
   correction noted; no owner-earnings figure depended on it (the line is displayed, not
   subtracted). The 2015 sum was likewise first written (155.5) in the table against the script's
   (155.6) and corrected to the script.
2. **My own error, caught before commit:** a first draft of the Q2 [E3-46] bullet described the
   2014-15 return only as *"16.0% operating margins ... on a consolidated asset base far smaller"*,
   which conceded nothing measurable. It was replaced, before this file was finished, by the
   unleveraged-net-tangible-asset series (68% / 42% / 42% / 13.6% / 6.1%), which is **the strongest
   evidence against the Q2 verdict** and belongs beside it in numbers.
3. **A first draft of Q3 said SBC was "6-12% of operating cash in normal years", then "9.2%"; the
   script gives 10.5% of cumulative operating cash.** Corrected before commit.
4. **A first draft attributed the words "particularly dependent upon future industry strength" to
   EY's critical audit matter; they are the MD&A's.** Corrected before commit.
5. **Tag-layer sign artifact:** the FY2023 10-K tags the 2022 TAP disposal proceeds ($42.2M) as a
   negative `PaymentsToAcquireBusinessesNetOfCashAcquired`, which the screen read as an acquisition
   inflow. Recorded at Step 0; not a tooling fix.
6. **The price response carries a null close for 2026-09-22**; that day is simply not quoted in
   the run.
7. **The prior session's claim file `_msg_claim.txt`** was left untouched and uncommitted in the
   research folder, as found.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: Q1 IN / Q2 OUT, on the business.** The North American off-road share leader
  competes on price and incentives in its own words, has lost twelve points of core-segment gross
  margin in eleven years (32.3% to 20.2%), and earned less than BRP on gross and operating margin
  in every year of five; at $52.38 (cap $2,981M) against a 5.47% sovereign the owner-earnings range
  runs from about $50M to $420M, too wide for a conclusion, recorded as arithmetic only.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

**STATUS: COMPLETE 2026-09-25 (resumed 2026-09-24).** Fold: register entry 159 (158 before, 159 after,
counted by line index), `_wave7_done.txt` (26 lines before, 27 after), narrative fold in the PREPPED READING
LIST, OVERNIGHT LOG line; **no strike was needed**: the whole queue file was searched and `PII` appears only
twice, both inside the MCFT entry's competitor sentence, which is not a roster (wave 7 records completion in
`_wave7_done.txt` instead of a roster). No new survival shape. No alert and no PORTFOLIO.md row (failed on
the business, the QLYS ruling).
