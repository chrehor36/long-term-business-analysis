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
  machines** — Item 1: *"A majority of our dealers and distributors are multi-line and also
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

- Needed or desired **[x]** · no close substitute **[ ] — FAILS** · not price-regulated **[x]**

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

  **And the core segment alone, so that acquired mix cannot explain it** — ORV/Snowmobiles
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
| **Polaris (subject)** | GM 23.5 · 22.8 · 21.9 · 20.4 · **19.1** — **mean 21.5%**; OM 9.6 · 9.4 · 7.8 · 4.1 · **(4.9)** — **mean 5.2%** | FY2021-25 (Dec) | income statements, 10-K FY2025 `0001628280-26-008033` (2023-25) and 10-K FY2022 `0001628280-23-004043` (2021-22, continuing operations) |
| **BRP Inc.** (Can-Am, Ski-Doo, Sea-Doo), **CAD** | GM 27.9 · 24.9 · 26.3 · 22.5 · **22.4** — **mean 24.8%**; OM 15.5 · 13.6 · 14.1 · 7.0 · **4.7** — **mean 11.0%** | FY2022-26 (years ending 31 January, so FY2022 ≈ calendar 2021) | "Selected Consolidated Financial Information", EX-99.3 MD&A to 40-F FY2026 `0001193125-26-125055` (FY2024-26, continuing basis after the Marine disposal) and to 40-F FY2024 `0001193125-24-079609` (FY2022-23, Marine still inside at ~5% of revenue) |

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
- **[E3-46], the second question about the business is a number.** On a return-on-capital view
  the business once looked like a franchise: **16.0% operating margins in 2014-15** on a
  consolidated asset base far smaller than today's. The number has not held: operating margin
  **halved in 2016 and never returned**, and the 2021-22 peak (9.6% and 9.4%) was below the 2015 level on a sales base 58% to 82%
  larger. **[E4-32], direction outranks existence**: whatever the
  advantage was in 2014, it has **narrowed in nine of eleven annual steps** on gross margin.
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
