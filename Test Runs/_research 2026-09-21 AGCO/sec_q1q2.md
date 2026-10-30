## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34** % · date **09/18/2026** · source (issuing authority) **US Treasury daily par
  yield curve, 30 Yr, `home.treasury.gov` daily-treasury-rates.csv for 2026.** Struck fresh by
  this run on 2026-09-21; the file's newest row is 09/18/2026 (the Friday). **FRED DGS30 was
  not used.** Neighbouring rows read 5.29 (09/17), 5.35 (09/16), 5.36 (09/15), 5.34 (09/14) —
  the rate is still moving several basis points a day and no brief-supplied figure was
  inherited.
- FX if the quote and the earnings differ in currency: **not required.** AGCO reports in USD
  and the quote is USD. *But note the earnings are not USD-EARNED*: 64% of 2025 net sales came
  through Europe/Middle East dealers and 11% through South America (10-K Item 1, dealer table),
  against 17% North America. The USD sovereign is used because the **reporting and
  distribution currency** is USD. Recorded as a stated limit of the single-sovereign rule, not
  resolved.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025, filed 2026-02-13, period 2025-12-31, accession `0000880266-26-000010`**
    (primary document `agco-20251231.htm`) — Item 1, Item 1A, Item 5, MD&A, the three primary
    statements, and Notes 1, 2, 3, 6, 10, 11, 12, 13, 15, 16, 18, 19 and 25.
  - **10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession
    `0000880266-26-000068`** — cover page, balance sheet, the receivable-sale and
    supplier-finance notes, the credit facilities.
  - **10-K FY2022, accession `0000880266-23-000010`** (FY2020–22 statements);
    **10-K FY2021, accession `0000880266-22-000006`** (FY2019–21);
    **10-K FY2019, accession `0000880266-20-000006`** (FY2017–19);
    **10-K FY2016, accession `0000880266-17-000005`** (FY2014–16).
  - Competitor filings: **Deere & Company 10-K FY2025 (period 2025-11-02), accession
    `0001104659-25-122321`** and **10-K FY2022, accession `0001558370-22-018703`**;
    **CNH Industrial N.V. 10-K FY2025, accession `0001567094-26-000006`** and **10-K FY2023,
    accession `0001628280-24-007899`**.
- figure cross-checked against the filed statement (say which):
  **three, by hand, against the filed statements and not against the tag layer.**
  1. FY2025 **net cash provided by operating activities $988.1 million** and its detail lines,
     read off the Consolidated Statements of Cash Flows at page 53 of the FY2025 10-K, and
     re-derived from its own components: 719.0 − 251.9 − 366.5 + 256.5 + 71.1 + 28.4 + 10.0
     + 10.8 − 20.6 + 35.7 = 492.5 of earnings-side cash, **plus 495.6 of working-capital
     release** (231.0 + 237.5 − 17.1 + 43.4 − 114.1 + 114.9) = **988.1**. It ties.
  2. **Total stockholders' equity $4,273.5 million** at 2025-12-31 on the Consolidated Balance
     Sheet, re-derived from the closing row of the Consolidated Statements of Stockholders'
     Equity (0.7 + 0.5 + 6,047.2 − 1,774.9 = 4,273.5). It ties.
  3. **Deere's FY2025 equipment segment operating profit $4,906 million** (PPA 2,671 + SAT
     1,207 + CF 1,028) against external net sales of **$38,917 million**, both read off Deere's
     own Note 27 SEGMENT DATA, which independently prints the $6,020 million total including
     Financial Services. It ties.
- *If the filing could not be obtained → **UNRESEARCHED**. Name the ladder rung that failed
  and the obstacle.* — **not invoked; every rung used was SEC EDGAR primary documents.**

**THE PRICE AND THE CAP** *(struck by this run; repeated below under COMPUTATION — NOT A
CLEARANCE)*
- **Share count, quoted verbatim from the cover page of the 10-Q filed 2026-07-30, accession
  `0000880266-26-000068`:** *"As of July 27, 2026, there were 70,031,729 shares of the
  registrant's common stock, par value of $0.01 per share, outstanding."*
- **One equity class only.** The balance sheet in that same 10-Q carries exactly two capital
  lines: *"Preferred stock; $ 0.01 par value, 1,000,000 shares authorized, no shares issued or
  outstanding in 2026 and 2025"* and *"Common stock; $ 0.01 par value, 150,000,000 shares
  authorized, 70,002,207 and 72,629,310 shares issued and outstanding at June 30, 2026 and
  December 31, 2025, respectively."* No second class; no preferred outstanding.
- **Price $120.68** (2026-09-21, **aggregator quote, flagged** — Yahoo Finance chart endpoint;
  raw response written to `Test Runs/_research 2026-09-21 AGCO/price_raw.json`; intraday, not
  a settled close). Prior closes from the same response: 119.79 (09-18), 121.57 (09-17),
  119.89 (09-16), 123.79 (09-15).
- **cap = close × shares** — split-invariant, `close` and never `adjclose`:
  $120.676 × 70,031,729 = **$8,451 million.**
  *(The screen row carried cap_m 7,939. The difference is the quote date, not a share-count
  dispute.)*

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:** AGCO designs and assembles farm
  machinery — mostly tractors — in its own plants and sells it at wholesale to about **2,800
  independent dealers and distributors in about 140 countries**, who resell it to farmers. It
  does not own the dealers and it does not lend the money: the retail paper and the dealer
  floor-plan run through **finance joint ventures with Rabobank in which AGCO holds 49%**
  (Note 10), so the credit book sits off AGCO's balance sheet and reaches the income statement
  as one line, *"Equity in net earnings of affiliates."* Roughly **a quarter of the wholesale
  price is gross margin** (FY2025: net sales $10,082.0m, cost of goods sold $7,515.2m, gross
  profit $2,566.8m = 25.5%), out of which come selling and administrative costs of $1,309.3m
  and engineering of $487.7m. What is left, $595.7m in FY2025, is income from operations —
  **5.9 cents on the sales dollar.** Cash follows volume with a lag through a very large
  working-capital block (receivables $1,079.4m, inventories $2,709.3m at 2025-12-31) which
  fills on the way up and empties on the way down: **$495.6 million, or 50% of FY2025's entire
  operating cash flow, was working capital being released as net sales fell 13.5%.** Tractors
  and combines were **68.8% of 2025 net sales**; parts and everything else make up the balance.
- **The scarce input this business controls:** the **dealer network, and the brands attached to
  it** — Fendt, Massey Ferguson, Valtra, PTx. A farmer buying a high-horsepower machine is
  buying a twenty-year service relationship with a dealer inside driving distance, and the
  makers compete for the dealers as hard as for the farmers. The 10-K says so under Item 1A:
  *"We maintain an independent dealer and distribution network in the markets where we sell
  products. The financial and operational capabilities of our dealers and distributors are
  critical to our ability to compete in these markets. In addition, we compete with other
  manufacturers of agricultural equipment for dealers."* It is a real asset. **It is not an
  exclusive one** — Deere and CNH each hold a larger version of it, and AGCO's own Item 1 says
  its sales *"are not dependent on any specific dealer, distributor or group of dealers."*
- **Will the fundamentals look broadly the same in ten years?** **Yes for the core.** Row-crop
  farming needs high-horsepower tractors and combines; farm income drives the replacement
  rate; the three-maker structure has stood for decades. The one moving part is precision
  agriculture and autonomy, into which AGCO put **$1,910.0 million of cash in a single
  transaction on 2024-04-01** (Note 2). That is a genuinely changing field, and it is treated
  below at Q2 as a durability question rather than here as a comprehension one, because it is
  **23% of today's market capitalisation and 2.5% of one year's net sales** ($171.3m of PTx
  Trimble sales in the nine months after closing) — a bolt-on in the revenue line and a large
  bet in the balance sheet, not a change in what the company is.
- **VERDICT: [x] IN**
  *A machinery assembler with a dealer channel and an off-balance-sheet credit JV. Three
  sentences describe it and the ten-year picture is recognisable. No figure above is
  "unverified", "general knowledge" or "provisional" — all of it is off the filed FY2025
  statements and Item 1.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** · no close substitute **[ ] — FAILS** · not price-regulated **[x]**

**Clause (2) fails, and it fails on the registrant's own words, twice.** Item 1, under
"Competition":

> *"The agricultural industry is highly competitive. We compete with several large national
> and international full-line suppliers, as well as numerous short-line and specialty
> manufacturers with differing manufacturing and marketing methods. **Our two principal
> competitors on a worldwide basis are Deere & Company and CNH Industrial N.V.** We have
> regional competitors around the world that have significant market share in a single country
> or a group of countries."*

and Item 1A:

> *"The agricultural equipment business is highly competitive, particularly in our major
> markets. **Our two key competitors, Deere & Company and CNH Industrial N.V., are
> substantially larger than we are and have greater financial and other resources.**"*

and the buying decision itself, in the sentence immediately after the competition paragraph:

> *"We believe several key factors influence a buyer's choice of farm equipment, including the
> strength and quality of a company's dealers, **the quality and pricing of products**, dealer
> or brand loyalty, product availability, **terms of financing** and customer service."*

A product chosen on price and finance terms against two larger full-line rivals, plus regional
makers and short-liners, is a product with close substitutes. **[E3-03] criterion (2) is not
met.**

- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]**
  Not the rebuilt-from-zero class — a tractor brand is maintained, not replaced — so [E4-04]'s
  competence limit is **not** why this file closes, and the UNKNOWABLE perimeter close is **not**
  the right verdict here. The evidence on the franchise question is in hand and it is negative.
  This is [E2-58]'s commodity end — *"persistent over-capacity without administered prices (or
  costs) equals poor profitability"* — and the one exception [E2-58] allows is *"a cost
  advantage that is both **wide and sustainable** … By definition such exceptions are few."*
  The competitor row below tests for exactly that and finds the subject **last of three, at the
  top of the cycle and at the bottom of the same cycle.**
- **Primary moat metric, filing-sourced, and its trend: operating margin on equipment sales,
  five years, each figure from the company's own filing.** AGCO consolidates no captive finance
  book, so its GAAP income from operations *is* an equipment-operations margin; Deere and CNH
  both report their equipment/industrial businesses separately and those are the figures taken.
  AGCO's trend: **9.0% → 10.0% → 11.8% → −1.1% → 5.9%**, five-year mean **7.1%**, and the
  window contains an operating loss year.

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.

| Company | same metric — operating margin on equipment / ag net sales | same window FY2021–FY2025 | source |
|---|---|---|---|
| **AGCO (subject)** | 9.0% · 10.0% · 11.8% · **−1.1%** · 5.9% — **mean 7.1%** | FY2021–25 (Dec) | income from operations ÷ net sales, Consolidated Statements of Operations, 10-K FY2025 acc. `0000880266-26-000010` and 10-K FY2022 acc. `0000880266-23-000010` |
| **Deere & Company** — *ag only (PPA + SAT)* | 19.0% · 17.9% · 23.2% · 19.3% · **14.1%** — **mean 18.7%** | FY2021–25 (Oct/Nov) | segment operating profit ÷ segment external net sales, Note 27 SEGMENT DATA, 10-K FY2025 acc. `0001104659-25-122321`; FY2021–22 from SEGMENT DATA in 10-K FY2022 acc. `0001558370-22-018703` |
| **Deere & Company** — *all equipment (PPA+SAT+CF)* | 17.3% · 17.4% · 21.9% · 18.2% · **12.6%** — **mean 17.5%** | FY2021–25 | same notes; equipment net sales 39,737 / 47,917 / 55,565 / 44,759 / 38,917 |
| **CNH Industrial N.V.** — *Agriculture segment* | 12.3% · 13.7% · 14.5% · 10.5% · **6.2%** — **mean 11.4%** | FY2021–25 (Dec) | segment **Adjusted EBIT** ÷ segment net sales; 10-K FY2025 acc. `0001567094-26-000006` (2023–25) and 10-K FY2023 acc. `0001628280-24-007899` (2021–22) |

**Read the row with its three limits stated, because all three run in AGCO's favour and it
still comes last.** (i) **CNH's measure is its own non-GAAP "Adjusted EBIT"**, which excludes
restructuring, goodwill impairment and discrete items and *includes* equity income of joint
ventures; AGCO's and Deere's are GAAP operating profit carrying every charge. CNH is therefore
**flattered** against the other two, and AGCO is still below it in four years of five. (ii) CNH
restated its 2023 Agriculture figure between its FY2023 10-K ($2,732m, 15.05%) and its FY2025
10-K ($2,636m, 14.53%) on the ASU 2023-07 basis; the later filing's figure is used and the
earlier one recorded here rather than smoothed away. (iii) Deere's fiscal year ends in late
October, so its "2025" is roughly AGCO's twelve months to October 2025 — a quarter's offset,
which cannot account for an eleven-point gap.

**What the row shows, at both ends of one cycle:**
- **Peak (2023):** AGCO **11.8%**, CNH-Ag 14.5%, Deere-Ag **23.2%**. AGCO last.
- **Trough (2025):** AGCO **5.9%**, CNH-Ag 6.2% (on the flattered measure), Deere-Ag **14.1%**.
  AGCO last.
- **2024**, the year both of AGCO's own structural moves landed: AGCO **−1.1%**, an operating
  loss, against Deere-Ag 19.3% and CNH-Ag 10.5%.

**Deere earned a higher margin in its worst year of the five (14.1%) than AGCO earned in its
best (11.8%).** That is not a narrow moat measured imprecisely. It is the absence of one,
measured the same way on three companies over the same five years, each from its own filing.

- **Peers named: 2 of the industry's 2 worldwide full-line competitors.** The number is not a
  choice this run made: AGCO's Item 1 names exactly two *"principal competitors on a worldwide
  basis"*, and both are SEC registrants, so the row is **complete at the level the registrant
  itself defines.** Buffett's *"eight"* **[E3-28]** cannot be reached here and the reason is
  named rather than assumed — the remaining real competitors are **regional and short-line
  makers that do not file with the SEC**: Kubota (Tokyo-listed, deregistered from the NYSE, no
  20-F), CLAAS and SDF/Deutz-Fahr (private, German), Mahindra & Mahindra (Indian listing).
  **The ladder rung that stops is rung 4/5 — exchange filings and EDINET**, EDINET blocked by a
  paid key (resume state of 2026-09-12, section 5). **This does not make the row PROVISIONAL**,
  because the missing class is *smaller and regional* while the two that are missing-by-size
  are the two that are present. A moat claim surviving Deere and CNH would then be tested
  against the regionals; there is no such claim left to test.
- **Untapped pricing power — could a manager raise the return simply by raising prices, and
  has not? [E3-33]** **No — and the filings answer it with a number, every year, in AGCO's own
  words.** The 10-K MD&A discloses an estimated worldwide average price change:

  | 2014 | 2015 | 2016 | 2018 | 2019 | 2021 | 2022 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|
  | +1.5% | +1.8% | +1.5% | +1.4% | +1.9% | +6.6% | +11.6% | **−0.9%** | +1.1% |

  *(FY2016 10-K acc. `0000880266-17-000005`; FY2019 acc. `0000880266-20-000006`; FY2022 acc.
  `0000880266-23-000010`; FY2025 acc. `0000880266-26-000010`. Verbatim from the last: "We
  estimate that worldwide average price increases (decreases) were approximately 1.1% and
  (0.9)% in 2025 and 2024, respectively.")*

  This is **[E2-44]'s two-characteristic test failed on the first characteristic.** The test is
  whether the business can raise prices *"even when product demand is flat and capacity is not
  fully utilized"* — and in 2024, with demand falling and net sales down 19%, **AGCO's
  worldwide average price fell 0.9%.** The 2021–22 double-digit numbers are cost pass-through
  in a general inflation, not pricing power: they are bracketed by 1–2% years on both sides, at
  or below inflation. South America in 2025 is described in the MD&A as carrying *"negative
  pricing impacts"* in two consecutive sentences. **[E4-37]**'s inverse metric — *"you can
  almost measure the strength of a business over time by the agony they go through in
  determining whether a price increase can be sustained"* — reads at the agony end. There is no
  untapped pricing power here; there is barely-tapped pricing power.
- **[E4-55], where units exist, monitor units.** AGCO discloses no unit series. It discloses
  the next best thing and it points the same way: *"Consolidated net sales of tractors and
  combines, which comprised approximately 68.8% of our net sales in 2025, decreased
  approximately 6.4% in 2025 compared to 2024"* — a 6.4% dollar decline in the core line
  against a **+1.1% price**, so the physical decline is *worse* than the dollar decline.
  **The franchise is not hiding a volume gain behind price; it is hiding a volume loss behind
  price.**
- **[E4-36], which of the four causes of extreme success?** None is claimed and none is found.
  No max/min extreme (AGCO is third of three on margin); no nonlinear combination evidenced in
  the numbers; no many-factor extreme performance; and the 2021–23 result is plainly
  **wave-riding** — a grain-price and farm-income boom that lifted all three makers and has now
  receded, taking AGCO's margin from 11.8% to 5.9% in two years. *"the advantage lives in the
  wave, not the surfer."* **[E3-51]**
- **[E5-28] scope check:** claiming the untapped-pricing class would be claiming near-monopoly.
  The competitor row refuses it.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: NARROWING.** Proportionally
  AGCO fell from **47% of Deere-Ag's margin in 2021 to 42% in 2025**, and the 2024 operating
  loss has no counterpart in either competitor's year. **[E4-32]**'s primary criterion of a
  great business — the moat widened every year — reads the other way here.
- **VERDICT: [x] OUT**

  **[E3-03] clause (2) fails on the registrant's own words, and [E2-58]'s single exception — a
  cost advantage both wide and sustainable — is refuted by the competitor row.** This is a
  finding about the business, from evidence in hand; it is not a limit of my diligence and not
  an indeterminate future, so it is **OUT and not UNRESEARCHED or UNKNOWABLE.** The separating
  test was asked aloud: *can I name the document that would resolve this?* No — the three
  companies' own filed segment notes **are** the document, and they agree.

  **What this verdict does not say.** It does not say AGCO is a bad company, or that Fendt is
  not a strong brand in Europe. **[E3-61]** binds the row: it shows position, never conduct, and
  *"I think you'd have to know the people involved."* What it says is that on the corpus's own
  franchise test, a full-line farm-equipment assembler earning a mean **7.1%** operating margin
  across a full cycle, against two larger rivals earning **18.7%** and **11.4%** on the same
  test over the same years, **has no franchise to buy.**

  **Q2 OUT is permanent and it closes the file.** Q3, Q4 and the price arithmetic below are
  recorded **WITHOUT VERDICTS**, under operator rules 2 and 3.
