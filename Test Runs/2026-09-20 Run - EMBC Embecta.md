# Company Run — Embecta Corp. (EMBC) — 2026-09-20
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Wave 7, name 7. Research folder: `Test Runs/_research 2026-09-20 EMBC/`.
Corpus quotes are verbatim with a ledger id.

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
- rate **5.34** % · date **2026-09-18** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year constant maturity**. Struck fresh by `python tools/sources.py` on
  2026-09-20; not inherited from the dispatch brief.
- FX if the quote and the earnings differ in currency: quote and earnings are both USD.
  53.6% of FY2025 revenue is international (FY2025 10-K, revenues by geographic region:
  United States $579.1M, International $501.3M), but reporting and listing are USD.
  **New sterling exposure noted**: the Owen Mumford purchase price is denominated in GBP.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025**, period ended 2025-09-30, filed 2025-11-25, **0001872789-25-000036**
  - **10-Q Q3 FY2026**, period ended 2026-06-30, filed 2026-08-07, **0001872789-26-000033**
  - **8-K Item 1.01**, filed 2026-03-20, **0000947871-26-000310** (the deal note)
  - **8-K Item 2.01**, filed 2026-05-15, **0000947871-26-000546** (the deal closed)
  - **8-K/A Item 9.01**, filed 2026-07-31, **0001872789-26-000026** (acquiree accounts, pro formas)
  - **10-K FY2022**, period ended 2022-09-30, filed 2022-12-22, **0001872789-22-000024**
- figure cross-checked against the filed statement (say which): **operating cash flow
  FY2025 $191.7M.** XBRL `NetCashProvidedByUsedInOperatingActivities` returns 191,700,000;
  the filed Consolidated Statements of Cash Flows in the FY2025 10-K reads
  `Net Cash Provided by Operating Activities | $ | 191.7 | $ | 35.7 | $ | 67.7`. Agrees.
  Capex likewise: XBRL 9,300,000 against the filed `Capital expenditures | ( 9.3 )`.

---
## STEP 0A — THE THREE LIVENESS FLAGS ON THE SCREEN ROW

*The screen row is transcription and screening only. Each flag was resolved from a primary
document before Q1 opened (operator rule 4).*

### FLAG 1. The `deal_note`: EMBECTA IS THE ACQUIRER, AND THE DEAL HAS CLOSED

The 8-K filed 2026-03-20 (**0000947871-26-000310**, Item 1.01, event date 2026-03-19):

> "On March 19, 2026, Embecta Corp. (“embecta”) entered into a definitive Agreement for the
> Sale and Purchase of Owen Mumford Holdings Limited (the “Purchase Agreement”) ... pursuant
> to which embecta has agreed to acquire Owen Mumford Holdings Limited (“OM”), a privately
> held, UK-based innovator and manufacturer of medical devices and drug-delivery
> technologies, in a transaction valued at up to £150 million (the “Transaction”)."

Terms, from the same document: **an upfront cash payment of £100 million at closing
(subject to customary adjustments, including for closing net cash), and up to an additional
£50 million upon the achievement of certain commercial milestones related to sales of the
Aidaptus® next-generation auto-injector platform through the end of 2028.** Unanimously
approved by the embecta board. **No shareholder vote**; consummation was "subject to
customary closing conditions and regulatory approvals". The sellers are six named
individuals and family trustees, so there is no listed counterparty.

The 8-K filed 2026-05-15 (**0000947871-26-000546**, Item 2.01): *"On May 15, 2026, Embecta
Corp. (“embecta”) completed its previously announced acquisition (the “Transaction”) of all
of the issued share capital of Owen Mumford Holdings Limited."* The milestone window is
restated there as *"the period ending June 30, 2029"*, a later end date than the March
8-K's *"through the end of 2028"*. Both are quoted as filed; the run does not reconcile
them and does not need to.

**So the quote is NOT a merger spread.** Embecta is not being taken private; Embecta is the
buyer, and the consideration was cash it already had or borrowed, not its own shares, so
[E5-44] does not bite. A Q5 on this price would not be a category error on that ground.

What the flag resolves to is the second branch the brief named: **the perimeter changed.**
The 8-K/A of 2026-07-31 carries Owen Mumford's audited accounts and the pro formas. Every
annual figure through FY2025 is the pre-acquisition perimeter; FY2026 will be a stub year
carrying about four and a half months of Owen Mumford.

No later 8-K amends or terminates anything. The newest filings are the Q3 FY2026 10-Q of
2026-08-07 and the earnings 8-K of the same day, and **the stock still trades on Nasdaq
under EMBC** (10-Q cover, 2026-08-07). This is not the LEG case.

### FLAG 2. The `cap_flag`: RE-STRUCK BY HAND, AND IT IS A DRAWDOWN DETECTOR

The screen's $286M cap against a filed public float of $732M is not a broken input. It is
the shape the CALM fold of 2026-09-20 identified: the float is measured at a past date and
the cap at a recent one, and **the share price collapsed in between.**

- **Float, as filed.** FY2025 10-K cover (**0001872789-25-000036**): *"The aggregate market
  value of the voting common equity held by non-affiliates of the registrant, computed by
  reference to the closing price at which the common stock was sold as of the end of the
  second fiscal quarter ended March 31, 2025, was approximately $ 732 million."* Same cover:
  *"The registrant had outstanding 58,512,841 shares of common stock as of November 18,
  2025."* That implies roughly **$12.50 a share at 2025-03-31**.
- **Share count, from the cover of the newest periodic filing.** 10-Q for the quarter ended
  2026-06-30, accession **0001872789-26-000033**, filed 2026-08-07: *"The number of shares
  of Embecta Corp. common stock outstanding as of July 31, 2026 was 56,659,599 shares, par
  value $0.01 per share."* The count **fell** by 1.85 million shares over eight months.
- **Price: $5.29, close of 2026-09-18.** *Aggregator, flagged: Yahoo Finance chart endpoint,
  raw response saved at `_research 2026-09-20 EMBC/quote_yahoo.json`. Live quote only, per
  operator rule 5.* The same series gives a 52-week high of $14.71, a 52-week low of $2.90,
  and $14.34 one year back.
- **RE-STRUCK CAP: 56,659,599 × $5.29 = $299.7M, call it $300M.** The screen's $286M was
  about 5% low and otherwise sound.

**Finding: the equity is down roughly 63% in twelve months, from about $14.34 to $5.29.**
The flag fired on a real collapse, not a stale input. That is a fact about the price, and
by **[E5-42]** it belongs at Q5 and is not evidence about the business. It is recorded here
only because the brief ordered the cap re-struck before anything used it.

### FLAG 3. The `name_change_note`: THE SERIES IS NOT ONE COMPANY

"Berra Newco, Inc." appears in the EDGAR submissions file as a former name of CIK
0001872789 from 2021-07-15 to 2021-09-03. It is neither a reverse merger nor a de-SPAC. It
is **the registration shell for a spin-off**: Embecta Corp. was separated from Becton,
Dickinson and Company on 2022-04-01. The FY2025 10-K says so in its own words: *"In
connection with our separation from Becton, Dickinson and Company ("BD") in 2022 (the
"Separation"), we entered into a cannula supply agreement with BD."*

**The consequence is the part that matters.** The six annual years in companyfacts do not
describe one company on one perimeter:

| FY ended | Revenue $M | Net income $M | Operating cash $M | What the entity was |
|---|---|---|---|---|
| 2020-09-30 | 1,085.5 | 427.6 | 498.5 | BD carve-out: no spin debt, no standalone corporate cost |
| 2021-09-30 | 1,165.3 | 414.8 | 456.3 | BD carve-out |
| 2022-09-30 | 1,129.5 | 223.6 | 412.2 | **stub year: carve-out to 2022-04-01, standalone after** |
| 2023-09-30 | 1,120.8 | 70.4 | 67.7 | first full standalone year |
| 2024-09-30 | 1,123.1 | 78.3 | 35.7 | standalone |
| 2025-09-30 | 1,080.4 | 95.4 | 191.7 | standalone |

*(All six rows from `companyfacts.json`, `NetIncomeLoss`,
`RevenueFromContractWithCustomerExcludingAssessedTax` and
`NetCashProvidedByUsedInOperatingActivities`, 10-K annual facts; the FY2023-FY2025 column
cross-checked against the filed FY2025 statements above.)*

**The filing says this itself.** FY2022 10-K, Note 1, accession **0001872789-22-000024**:

> "Prior to the Separation on April 1, 2022, the Company's historical combined financial
> statements were prepared on a standalone basis and were derived from BD's consolidated
> financial statements and accounting records. ... Prior to the Separation, the Company was
> referred to as the Diabetes Care Business. ... **The Consolidated Financial Statements did
> not purport to reflect what the Company's results of operations, comprehensive income,
> financial position, equity or cash flows would have been had the Company operated as a
> standalone public company during the periods presented.**"

A 39.4% net margin in FY2020 against 8.8% in FY2025 on almost identical revenue is not a
business that deteriorated by that much. It is **two different accounting entities under
one CIK.** The carve-out years carry no share of the roughly $1.6bn of debt the separation
loaded on, no standalone corporate infrastructure, and BD's allocated rather than incurred
costs. Interest expense alone is $107.3M in FY2025 and did not exist in FY2020.

**So the multi-year mean owner earnings requires [E2-23] has three clean standalone years,
not six, against the corpus default window of five [E2-42].** Carried into Q4 as a finding,
not a footnote, exactly as the brief instructed. It also accounts for every `level_shift`
and `window_disagree` flag on the screen row without any of them being a defect in the
business.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language:**
  Embecta makes tiny disposable steel needles and plastic syringes for injecting insulin. A
  pen needle is a single-use part that screws onto an insulin pen; the patient throws it away
  after the shot and buys another. There is no service contract, no razor, no installed base
  the company owns; the razor is the drug maker's pen and the blade is the needle. Embecta
  manufactures at three sites (Ireland, the United States, China) and sells, in its own
  words, *"primarily ... to wholesalers and distributors that sell to retail and
  institutional channels who in turn sell to patients"* (FY2025 10-K, MD&A). So the cash
  comes from volume times price on a consumable costing pennies, times about 30 million
  users, netted of rebates and chargebacks negotiated with payors and group purchasers.
  FY2025: revenue $1,080.4M, cost of products sold $403.6M, gross profit $676.8M (62.6%),
  operating income $242.1M, interest expense $107.3M, net income $95.4M. Capital spending was
  $9.3M, under 1% of sales, against depreciation and amortization of $40.7M.
  All figures from the filed FY2025 Consolidated Statements of Income and Cash Flows,
  accession 0001872789-25-000036.

- **The scarce input this business controls:** **on the filings, it does not control one.**
  This is the sharpest thing in Q1 and it is a document finding, not an opinion.
  1. *The needle itself.* FY2025 10-K, Raw Materials and Components: *"we entered into a
     cannula supply agreement with BD, whereby BD sells to us cannulas for incorporation into
     our pen needles and syringes. **BD retained ownership of all cannula production
     activities and the associated intellectual property rights** of BD and its subsidiaries
     relating to cannula, the manufacture thereof and other critical cannula-related
     technology."* The thin-wall cannula is the hard part of a pen needle, and the seller owns
     it and its IP.
  2. *The brand.* FY2025 10-K, Item 1A: *"Embecta has historically marketed its products using
     the "BD" name and logo, which is a globally recognized brand ... Embecta received a
     **temporary license** to use the "BD" and "Becton Dickinson" name and logo."*
  What Embecta does own is scale in high-volume moulding and assembly, 655 US and foreign
  patents and 455 trademark registrations, and shelf and formulary position with distributors
  in over 100 countries. That is a real position. It is not a controlled scarce input.

- **Will the fundamentals look broadly the same in ten years?** The *product* will: a pen
  needle in 2036 will be a pen needle. The *volume* is the open question, and the company's
  own MD&A answers it in the past tense (quoted in full at Q2). I record that at Q2 and Q4,
  where the franchise and the survival questions live, and not here, because [E3-31] asks
  whether the business is *"relatively simple and stable in character"* and whether I can
  write down how the money is made. I can: it is a single-product consumable manufacturer
  with one reporting unit (FY2025 10-K Note 2: *"The Company has one reporting unit"*), one
  income statement, no segments, no float, no equity-method stakes, and no financial
  engineering in the revenue line. There is nothing here I do not understand.

- **VERDICT: [x] IN**

---

## Q2 — IS IT A FRANCHISE? **[E3-03]**

*The corpus test: a franchise is a product or service that "(1) is needed or desired; (2) is
thought by its customers to have **no close substitute** and; (3) is not subject to price
regulation."*

- **Needed or desired** [x]. Yes, and not in doubt. Insulin has to get through skin.
- **No close substitute** [ ]. **FAILS, and it fails out of the company's own filing.**
- **Not price-regulated** [~]. Not price-regulated in the tariff sense, but the FY2025 10-K
  names *"increased scrutiny by regulators on healthcare spending"* and *"a shift towards
  volume-based procurement and group purchasing organizations"* as forces that *"have placed
  significant pressure on Embecta to lower price in both developed and emerging markets."*
  Criterion 3 survives on a technicality and no more.

### The company files that its own category is commoditized

FY2025 10-K, MD&A, *Key Trends Affecting Our Results of Operations*. The headings are the
filer's own:

> "**Commoditization of Injection Devices.** Given the growing demand for medical devices to
> assist in the treatment of diabetes and difficulties around access to diabetes care due to
> complex and costly insurance plans, patient care is increasingly focused on providing more
> affordable products, **which has led to the commoditization of more traditional injection
> delivery devices, such as insulin syringes and pen needles.** Existing and new local and
> regional low-cost providers, in combination with a shift from insulin vials to insulin
> pens, **have made the pen needle category highly competitive.**"

> "**Pricing Pressures.** We face significant pricing pressures from competitors in the pen
> needle and insulin syringe categories who not only can provide competitive products at
> lower costs, but also provide payors and customers with more choices for formulary partners
> in these categories. ... **have placed significant pressure on Embecta to lower price in
> both developed and emerging markets.** These trends may reduce our operating margins, which
> are only partially offset by our ability to differentiate our products and sell at higher
> prices."

> "**Changes in Clinical Practice.** Introduction of new drugs and increased penetration of
> oral and once-weekly anti-diabetic drugs (e.g., SGLT-2s, once-weekly insulin, GLP-1s and
> GLP-1 combination products) **have delayed initiation of insulin therapy and contributed to
> less demand for our products.** ... Additionally, **insulin therapy in developed markets
> continues to transition to infusion pumps.**"

That third paragraph is a filed admission, in the past tense, that close substitutes exist
and are already taking the volume. **[E3-03]** criterion 2 does not survive it.

This is **[E2-58]**'s class, not a franchise: *"persistent over-capacity without administered
prices (or costs) equals poor profitability"*, with the single exception being *"a cost
advantage that is both wide and sustainable ... By definition such exceptions are few."* A
producer with a wide and sustainable cost advantage does not write that low-cost providers
have forced it to lower price in developed *and* emerging markets. The filing rules itself
out of the exception.

### The primary moat metric, filing-sourced, and its trend: UNITS AND PRICE, BOTH NEGATIVE

**[E4-55]** orders the physical series where units exist: *"Dollar revenue flattered by
pricing is how a shrinking franchise hides; the physical series is the honest one."* Embecta
does not disclose needle counts, but it discloses the price/volume/FX bridge, which is the
same information. From the filings, verbatim:

| Period | filed bridge | source |
|---|---|---|
| FY2025 vs FY2024 | *"primarily driven by $52.9 million of unfavorable changes in volume"* and *"$3.5 million associated with the negative impact of foreign currency translation"*, partly offset by *"a $2.0 million increase associated with favorable changes in price"* | 10-K FY2025, MD&A, 0001872789-25-000036 |
| 9M FY2026 vs 9M FY2025 | *"primarily driven by $60.0 million of unfavorable changes in volume, **$27.4 million of unfavorable changes in price**, and a $2.9 million decrease in contract manufacturing revenue"* | 10-Q Q3 FY2026, MD&A, 0001872789-26-000033 |
| Q3 FY2026 vs Q3 FY2025 | *"primarily driven by **$20.1 million of unfavorable changes in price**, $19.9 million of unfavorable changes in volume"* | same 10-Q |

Volume has been negative for two years running. **Price turned negative in FY2026 and the
turn is accelerating**: $20.1M of price give-back in a single quarter on a $271.7M revenue
base is 7.4% of that quarter's sales.

**[E2-44]**'s two-characteristic test asks whether the business can raise prices *"even when
product demand is flat and capacity is not fully utilized"*. Demand is not flat, it is
falling, and the answer on price is not a small yes but a measured no. **[E4-37]**'s inverse
metric asks about *"the agony they go through in determining whether a price increase can be
sustained"*. There is no agony on the record because there is no price increase; there is a
filed price decrease of $27.4M in nine months.

The product line carries it. Pen Needles, the 73% of revenue that is the franchise claim:

| | FY2023 | FY2024 | FY2025 | 9M FY2025 | 9M FY2026 |
|---|---|---|---|---|---|
| Pen Needles $M | 829.2 | 844.4 | 784.1 | 596.3 | **517.6 (-13.2%)** |
| United States revenue $M | 601.4 | 607.2 | 579.1 | 437.1 | **347.1 (-20.6%)** |

*(FY columns from the FY2025 10-K revenue disaggregation note; the 9M columns from the Q3
FY2026 10-Q revenue note. The 9M FY2026 "Other" line of $23.2M includes the newly acquired
Owen Mumford products, so total revenue understates the core decline.)*

A 20.6% fall in United States revenue in nine months is not an aberrational cycle in a
100-year-old consumable. **[E4-32]** makes direction the primary criterion of a great
business: *"the moat widened every year"*. Every filed metric here narrows.

### [E4-04], and the brand basis is being rebuilt from zero, not defended

> "A moat that must be **continuously rebuilt** will eventually be no moat at all."
> — **[E4-04]**, 2007 letter

The framework's own scope test for [E4-04] is *"does a lapse in spending destroy the
structure, or merely narrow it, and does the spending defend the same advantage, or buy its
replacement?"*, with Coca-Cola's advertising as the defending case and Mitsui's Rhodes Ridge
as the replacing case. Embecta's brand spending is unambiguously the **replacing** case, on
the filing's own words:

> "Following the expiration of this license, Embecta will be required to rebrand and update,
> as applicable, its products and marketing, manufacturing, supply chain, and regulatory
> registrations and licenses using the "Embecta" name or other names and marks and remove the
> "BD" name and logo ... **While we have officially launched our brand transition from the
> "BD" name and logo in the U.S. and Canada**, the remaining launches worldwide are planned to
> occur in phases, and **these new names and brands may not benefit from the same recognition
> and association with product quality as the BD name**, which could adversely affect
> Embecta's ability to attract and maintain its customers and end users, who may prefer to
> use products with a stronger brand identity." — FY2025 10-K, Item 1A

The brand transition launched in the United States and Canada first. **United States revenue
then fell 20.6% in the following nine months.** The run does not claim the filing proves
causation; the filing itself predicted exactly this effect and the effect then appeared in
the segment where the transition happened first. It is recorded as what it is: the named
risk and the matching outturn, in that order.

Note also which advantage is being rebuilt. The 100-year brand was BD's, the cannula IP is
BD's, and the only thing the spin carried out of the parent was the customer position. The
framework's 2026-09-20 [E4-04] ruling says *"A name whose advantage the filings show must be
**rebuilt from zero** each generation fails [E4-04] on the business."* This is a one-time
rebuild rather than a generational one, but it is a rebuild from zero of the single asset the
company's own risk factor calls its customer-retention mechanism.

**And the register of the four causes [E4-36].** The pre-2022 economics, a 39.4% net margin
in FY2020, came from riding a wave: injected insulin as the dominant diabetes modality,
under a parent's brand, inside a parent's cost base. That is **[E3-51]**'s surfing run, not a
moat: *"when a surfer gets up and catches the wave and just stays there, he can go a long,
long time. But if he gets off the wave, he becomes mired in shallows."* The advantage lived in
the wave. The wave is named in the filing and it is turning.

### THE COMPETITOR ROW, required **[E3-28]**

*A moat is a claim about relative position. Same metric, same window, filing-sourced.*

The FY2025 10-K names its direct competitors: *"Companies with whom we currently compete in
the diabetes drug injection business include Novo Nordisk, MTD Group, and Terumo Medical
Corporation. We also compete with providers of insulin pumps and other insulin administration
devices."* That is six real competitors once the pump class is unpacked (Novo Nordisk, MTD
Group, Terumo, Insulet, Tandem, and Medtronic Diabetes, now MiniMed). I took **three**.

**Metric: revenue direction and gross margin over the same window, FY2023 through the most
recent filed full year, from each filer's own statements.**

| Company | revenue, start of window | revenue, end of window | change | gross margin, start → end | source |
|---|---|---|---|---|---|
| **Embecta (EMBC)** | $1,120.8M (FYE 2023-09-30) | $1,080.4M (FYE 2025-09-30) | **-3.6%** | 66.9% → **62.6%** (and **58.7%** in 9M FY2026) | 10-K FY2025, 0001872789-25-000036; 10-Q 0001872789-26-000033 |
| Insulet (PODD) | $1,697.1M (FYE 2023-12-31) | $2,708.1M (FYE 2025-12-31) | **+59.6%** | 68.3% → **71.6%** | companyfacts, 10-K annual facts, CIK 1145197 |
| Tandem Diabetes (TNDM) | $747.7M (FYE 2023-12-31) | $1,014.7M (FYE 2025-12-31) | **+35.7%** | 49.2% → **53.8%** | companyfacts, 10-K annual facts, CIK 1438133 |
| Novo Nordisk (NVO) | DKK 232,261M (FYE 2023-12-31) | DKK 309,064M (FYE 2025-12-31) | **+33.1%** | 84.6% → 81.0% | companyfacts, 20-F annual facts, CIK 353278 |

- **Peers named: 3 of the industry's 6 real competitors.** Buffett says eight; this industry
  does not have eight at scale, and three is what the filings reach.
- **Peers unavailable, with the rung and the obstacle named** (evidence ladder, section II):
  - **Terumo Medical Corporation**. Japanese parent, Tokyo listed, **no SEC filer**. Rung 3
    (company IR site, English) attempted 2026-09-20 and returned **HTTP 403 Forbidden**.
  - **Ypsomed**. SIX Swiss Exchange, **no SEC filer**. Rung 3 attempted and returned **HTTP
    404**. (Not named by the 10-K but a real pen and autoinjector competitor.)
  - **MTD Group**. Private Chinese manufacturer, no public filings in any accessible rung.
  - **Medtronic Diabetes / MiniMed**. Was inside Medtronic plc's 10-K during most of the
    window and is not separately reported on a comparable basis.
- **The row's own limit [E3-61]:** *"In some businesses, the participants behave like a
  demented Kellogg. In other businesses, they don't ... I think you'd have to know the people
  involved."* The row shows position, not conduct. The subject's conduct is nevertheless
  filed: it cut price.
- **Why the three missing peers do not make this PROVISIONAL.** The framework holds a moat
  class PROVISIONAL where a missing peer might *establish* a moat that the available data
  cannot. Here the verdict runs the other way. The class is **NONE**, and it is established
  from the subject's own filings, without any peer at all: criterion 2 of [E3-03] fails on a
  filed admission that substitutes have already taken demand, and [E2-58]'s exception is
  disclaimed by the subject's own pricing paragraph. The three missing names are precisely the
  *"existing and new local and regional low-cost providers"* the subject blames for its price
  cuts. Their filings could only deepen the finding; they cannot reverse it. The
  unavailability is recorded as an open item, not as a caveat on an IN, because there is no
  IN here to caveat.

**What the row says in one line: the three measurable competitors compounded revenue at
between 33% and 60% over the same two years in which the subject shrank by 3.6%, and two of
the three widened gross margin while the subject's fell 4.3 points and then another 3.9.**
Insulet and Tandem are the substitute modality the subject's own MD&A says developed-market
insulin therapy *"continues to transition to"*. The substitution is not a forecast in this
run; it is measured on both sides of the trade.

### The remaining Q2 tests, scored

- **Untapped pricing power [E3-33]?** **No, and the opposite.** A manager could not raise the
  return by raising prices; the company is cutting them by a filed $27.4M in nine months. The
  scope rule **[E5-28]** would require near-monopoly to claim the class, and there is none.
- **The dominance class [E2-53]?** No. *"Good or bad, it will prosper"* describes a position
  that sets its own economics. This position does not set price.
- **[E3-46], the second question is a number.** In fairness to the business, the return on
  capital is **high**: operating income $242.1M for FY2025 against total assets of $1,090.9M,
  of which goodwill and intangibles are only $22.4M. Total Equity is **negative $650.6M**, so
  [E2-01]'s book-equity denominator is meaningless here and **[E2-43]**'s unleveraged net
  tangible assets is the right one; on roughly $0.7bn of net tangible capital that is a
  pre-tax return in the low thirties. **This is the one genuinely franchise-shaped number in
  the file, and it is not enough.** [E4-32] makes *direction* the primary criterion, and
  [E2-58] explains why a high current return in a commoditizing category is not evidence of
  durability: prosperity breeds the next glut, and *"nothing fails like success."*
- **The attacker's test [E2-45]**. How would I compete with it, given ample capital and
  skilled people? I would not attack it. I would wait. The filing says low-cost regional
  producers are already doing the attacking and winning on price, and the pump and GLP-1
  makers are removing the customers from the category altogether. That is the worst answer a
  franchise can give to this question: the business does not need to be attacked to be taken.
- **Key-person dependence [E4-23]?** Not found. This is not a Mayo-versus-surgeon case.

- Class: [ ] WIDE [ ] NARROW [x] **NONE** [ ] PROVISIONAL · Direction: **narrowing on every
  filed metric: units, price, gross margin, geography, and brand ownership.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**Why OUT and not UNKNOWABLE.** The framework's ruling of 2026-09-20 makes [E4-04] a
competence limit, so a name that *passes* [E3-03] but whose durability cannot be judged from
filings closes UNKNOWABLE at Q2, the perimeter close. That is not this case. This name **fails
[E3-03] itself**, on criterion 2, on its own filed words, with the volume and price bridge
showing the substitution already in the numbers. The evidence is here and the business fails
the test. That is the definition of OUT.

**The separating question, asked aloud: "Can I name the document that would resolve this?"**
There is no missing document. The FY2025 10-K and the Q3 FY2026 10-Q resolve it, against.

---
⛔ **THE FILE CLOSES HERE. Q3, Q4, Q5 and Q6 are not opened** (operator rule 2: stop at the
first verdict that is not IN; UNRESEARCHED and UNKNOWABLE both close the file, and OUT closes
it permanently). What follows is recorded because the brief ordered specific reads, and
because a closed file that names the way it would reopen is worth more than a blank one. **No
line below is a clearance, and no valuation appears anywhere in this run.**

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
**NOT OPENED. No verdict.** Q2 returned OUT, and operator rule 2 stops the run at the first
question that is not IN. What was read at Q3 is recorded beneath the close, unscored.

## Q4 — WILL IT SURVIVE?
**NOT OPENED. No verdict.** What was read at Q4 is recorded beneath the close, unscored.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** It did not open. **No valuation, no yield,
no floor test, no ranking and no price target appears in this file.**

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**NOT OPENED.** The sovereign was struck at Step 0 because the template asks for it there, not
because anything was discounted against it.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**NOT OPENED** as a sell discipline, because nothing is owned and nothing was cleared.
**The reversal condition is recorded instead**, per the QLYS ruling that a price alert on a
name that failed on the business is a category error:

> **WHAT WOULD REOPEN THIS FILE.** Q2 failed because the filer's own MD&A says its category
> is commoditized, its price is falling, its units are falling, and close substitutes have
> already taken demand. The file reopens only on **filed evidence that the direction
> reversed**: two consecutive periods in which the 10-Q price/volume bridge shows **favourable
> price**, with **pen needle revenue and United States revenue both growing**, on a perimeter
> that excludes the Owen Mumford contribution. Not a lower share price. Not a higher one.
> Nothing in `tools/alerts.json`, and no band.

---
## BENEATH THE CLOSE: READ, AND NOT SCORED

*Q2 returned OUT, so Q3 and Q4 were not run and carry no verdict. The standing instruction
from the CGNX run is to pull the furnished release before [E4-29] and [E4-22]'s third flag are
recorded, and the brief ordered the proxy, the debt note and the [E4-25] window rebuild. What
follows is observation, recorded so a later reader need not refetch. **None of it is a finding
about the managers or about survival, and none of it contributed to the Q2 verdict, which
rests entirely on [E3-03], [E2-58], [E4-04], [E3-51], [E4-55], [E2-44] and [E4-37] applied to
the filed price and volume bridge.***

**[E4-29], the fifth flag, seen and NOT scored.** *"Trumpeting EBITDA … is a particularly
pernicious practice."* The Q3 FY2026 release (EX-99.1 to the 8-K of 2026-08-07, accession
**0001872789-26-000029**) uses "Adjusted EBITDA" seven times, "Adjusted Operating" seven times,
"Adjusted Gross" six times and "Constant Currency" fourteen times across the two casings; the
FY2025 release (EX-99.1 to the 8-K of 2025-11-25, **0001872789-25-000033**) is the same shape.
Both highlight lists give the GAAP figure and the adjusted figure side by side on every line,
which is better disclosure than a release that gives only the adjusted one. What the release
does **not** do is reconcile its forward guidance: *"We are unable to present a quantitative
reconciliation of our expected adjusted operating margin and expected adjusted earnings per
diluted share."*

**The incentive structure, from the proxy, seen and NOT scored.** DEF 14A filed 2025-12-18,
accession **0001140361-25-046025**. The annual bonus plan is *"80% Financial Metrics (40%
Adjusted Constant Currency Revenue $, 40% Adjusted EBITDA $)"*. The FY2023 PSUs ran on
*"Constant Currency Revenue Growth %, weighted at 45% and Adjusted Operating Income $, weighted
at 30%"* with an Adjusted EBITDA threshold. So the measure **[E4-29]** calls pernicious is not
merely promoted in the release; it is the pay system. **[E4-27]**: *"Never, ever, think about
something else when you should be thinking about the power of incentives."* FY2025 targets were
*"Adjusted Constant Currency Revenue $ of $1,110.0 million and Adjusted EBITDA $ of $419.0
million"*; actuals were *"$1,076.0 million"* and *"$415.0 million"*; the plan funded at
**110.2% of target** in a fiscal year when reported revenue fell 3.8% on falling volume. The
proxy also records the Committee applying **negative discretion** to eliminate the Net Debt
Focus Plan from results even though *"The Net Debt target was also exceeded"*, which is a
point in the other direction and is recorded as such. **[E3-48]**'s guidance-versus-outturn
exercise was not performed, because the gate was not reached.

**[E5-08] and [E4-31], the buyback conditions, seen and NOT scored.** In a single month, May
2026, the board did three things (10-Q Q3 FY2026, Notes and MD&A):
*"approved a reduction in the quarterly cash dividend from $0.15 to $0.01 per share"*;
*"approved a three-year $ 100.0 million stock repurchase authorization"*; and closed the Owen
Mumford purchase, drawing on the revolver to fund it. The buyback then ran: *"the Company
repurchased 2.7 million shares of its common stock for $ 8.7 million during the three and nine
months ended June 30, 2026"*, an average of about $3.22 a share. **[E5-08]**'s first condition
is *"a company has ample funds to take care of the operational and liquidity needs of its
business"*; a 93% dividend cut in the same month a buyback is authorised is the fact to set
against it. **[E5-25]** shows what compliance looks like when it is real: Berkshire published
both conditions as numbers in advance. No such numbers are published here. **Not scored, and
not a venality finding [E5-38].**

**[E5-11] strengths 2 and 3, and the capital structure, seen and NOT scored.** From the FY2025
10-K debt note and the Q3 FY2026 release:
- **$500.0M of 5.00% senior secured notes due February 15, 2030**; **$200.0M of 6.75% senior
  secured notes due February 15, 2030**; a **Term Loan B**, originally $950.0M, **$716.8M
  outstanding at 2025-09-30, maturing March 2029**, priced at *"300 basis points over the
  secured overnight financing rate ("SOFR"), with a 0.50% SOFR floor"*; and a **$500.0M
  Revolving Credit Facility with a five-year term that matures in 2027**.
- At 2026-06-30: *"approximately $218.2 million in cash and equivalents and restricted cash and
  $1.469 billion of debt principal outstanding, including $129.9 million drawn on its $500
  million Revolving Credit Facility to fund the acquisition of Owen Mumford."*
- Credit ratings, as the FY2025 10-K states them: *"Our Moody's Investors Services credit
  rating is B1 and our Standard & Poor's Rating Services credit rating is B+."*
- The covenant, verbatim: *"a total net leverage ratio covenant, which measures the ratio of
  (i) consolidated total net debt to (ii) consolidated earnings before interest, taxes,
  depreciation and amortization, and subject to other adjustments, must meet certain defined
  limits which are tested on a quarterly basis"*. **As of September 30, 2025 the company was
  *"in compliance with all of such covenants."***
- **Had Q4 opened, this is where it would have been decided.** The covenant denominator is
  EBITDA, and the filer's own Adjusted EBITDA fell from $325.4M to $247.5M over the nine months
  to 2026-06-30, a decline of 23.9%, while the revolver that now funds the acquisition matures
  in 2027. That is **[E5-11]**'s third strength, *"no significant near-term cash
  requirements"*, which the corpus calls the one that usually kills, set against a covenant
  tested quarterly on a falling denominator. **[E2-54]**'s coverage test and **[E5-39]**'s
  *"kindness of strangers"* would both have been run here. They were not, because the gate was
  not reached.

**Total Equity is negative $650.6M** at 2025-09-30 (filed Consolidated Balance Sheets), against
total assets of $1,090.9M. **[E2-01]**'s book-equity denominator is unusable, and **[E2-43]**'s
unleveraged net tangible assets is the denominator the corpus supplies for exactly this case.
Recorded at Q2 under [E3-46]; not scored at Q3.

---
## COMPUTATION: NOT A CLEARANCE
*Operator rule 3. Q1 to Q4 did not all show IN; Q5 never opened. **This block carries no entry
language, no yield, no sovereign comparison and no value.** It exists only because the screen
row's `spread_caveat` ordered an **[E4-25]** rebuild of the owner-earnings window, and because
the answer turned out to be a finding about the data rather than about the price.
Reproducible: `_research 2026-09-20 EMBC/oe_rebuild.py`.*

Owner earnings, on the framework's confessed CONVENTION (section VI): operating cash flow, less
share-based compensation in full **[E5-06]**, less (c). The (c) band runs from D&A, which is the
corpus default **[E3-44, E2-41]**, to total capex. Inputs are 10-K annual facts, with FY2023 to
FY2025 cross-checked against the filed FY2025 Consolidated Statements of Cash Flows.

| window | mean OCF | mean SBC | (c) = D&A | (c) = capex | OE at capex end | OE at D&A end |
|---|---|---|---|---|---|---|
| FY2023-FY2025, 3y, **standalone only** | 98.4 | 26.5 | 36.5 | 17.2 | **54.7** | **35.4** |
| FY2022-FY2025, 4y, includes the stub year | 176.8 | 24.5 | 35.3 | 18.8 | 133.5 | 117.0 |
| FY2021-FY2025, 5y, **the corpus default [E2-42]** | 232.7 | 22.2 | 35.9 | 22.4 | 188.1 | 174.6 |
| FY2020-FY2025, 6y, everything filed | 277.0 | 20.6 | 36.3 | 25.7 | 230.8 | 220.1 |

*(All figures $M.)*

**What the rebuild found, and it is the sharpest thing in this file after the pricing bridge.**
The screen row publishes a band of **$35M to $181M, a spread of 4.151x**, flagged
`TWO YEARS JOINTLY CARRY THE WINDOW`. Set the table against it:

- **$35M is the three-year standalone window at the D&A end: $35.4M.**
- **$181M sits inside the five-year window: $174.6M to $188.1M.**

**So the published 4.151x spread is not business volatility at all. It is the spin.** The
bottom of the band is Embecta Corp., a leveraged standalone company; the top is the Diabetes
Care Business of Becton, Dickinson and Company, carrying none of the debt, none of the
standalone corporate cost and none of the interest. The `level_shift` and `window_disagree`
flags are reading the boundary between two entities, exactly as the FY2022 10-K warned they
would: *"did not purport to reflect what the Company's results of operations ... would have
been had the Company operated as a standalone public company during the periods presented."*

**And the [E4-25] rebuild the caveat ordered cannot be performed in the direction it assumed.**
The caveat says the four-construction width *"CANNOT see variation older than the 5-year
window; rebuild it"*. Rebuilt by hand from the filed statements, the finding is that **there is
no older window to see.** Before FY2023 there is no standalone company. The corpus's five-year
default **[E2-42]** is **unavailable here**, and the honest window is three years, one of which
(FY2024) carries a $174.7M trade-receivable build and another (FY2025) carries its partial
reversal plus $63.2M of receivables sold under an agreement entered *"during the third quarter
of fiscal year 2025"*. Had Q4 opened, **[E4-25]**'s own verdict would have been in play: *"If
the combined range is too wide to reach a conclusion, that IS the conclusion."*

**On the `wc_note`, which the brief ordered read.** The screen flagged
`AccountsPayableAndAccruedLiabilities moved 168% of 2024 OCF`, and it reproduces: FY2024's
*"Accounts payable, accrued expenses and other current liabilities | 60.0"* against operating
cash of $35.7M is 168%. **But the flag named the wrong line.** The larger mover in FY2024 was
*"Trade receivables, net | ( 174.7 )"*, which is **489% of that year's operating cash** and in
the opposite direction. FY2024's $35.7M of operating cash is a number produced by a receivable
build, and FY2025's $191.7M is a number produced by its partial reversal plus $63.2M of
receivables sold. **Operating cash is not owner earnings in either year**, which is precisely
what the DELL and INOD cases established and what the flag exists to send a reader to check.
Recorded; not scored.

---
## WHAT THIS RUN REFUTED, AND WHAT IT CONFIRMED

**Refuted (four):**
1. **The `deal_note`'s first branch.** Embecta is not a target and the quote is not a merger
   spread. The EX-2.1 is a purchase agreement in which Embecta is the buyer of a private UK
   company from six individuals, closed 2026-05-15 for cash. The note's own instruction
   (*"if this company is being bought the quote is a SPREAD, if it is buying the perimeter
   changes"*) resolves to the second branch.
2. **The `cap_flag`'s premise that one of the two inputs is wrong.** Both are right. The float
   is a 2025-03-31 measurement and the cap a 2026-09 one, and the share price fell about 63%
   in between. **Second confirmation of the CALM drawdown-detector reading in one day.**
3. **The `name_change_note`'s odds.** The note says *"~60% of these are real perimeter
   events"*. This one is, but not in the shape the note guesses: not a reverse merger, not a
   de-SPAC, but a spin-off registration shell, and the perimeter break is at FY2022 rather than
   at the 2021 name change.
4. **The `wc_note`'s named line.** `AccountsPayableAndAccruedLiabilities` at 168% of FY2024
   operating cash is real but is not the biggest mover; `IncreaseDecreaseInAccountsReceivable`
   at 489% is. The flag's 30% threshold fired correctly and its pointer was second-best.

**Confirmed (three):**
1. **The screen's owner-earnings band ends both reproduce**, and they reproduce from *different
   entities*: $35M is the standalone three-year D&A end, $181M is inside the five-year window
   that reaches back into the BD carve-out.
2. **[E4-55]'s unit discipline keeps earning its place.** Dollar revenue fell 3.8% in FY2025
   while the filed bridge showed $52.9M of volume loss offset by FX and mix. The nine-month
   figure then showed both legs negative. The physical series was the honest one again.
3. **The CGNX standing instruction earned its keep.** The FY2025 10-K alone would not have
   shown the dividend cut, the buyback authorisation, the revolver drawdown, the 24.6% United
   States decline, or that Adjusted EBITDA is the pay metric. All of those are in the furnished
   release, the 10-Q and the proxy.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first that is not IN; no verdict skipped
- [x] **No question marked IN carries an "unverified", "general knowledge" or "provisional"
      caveat.** Q1 is the only IN in this file and it rests on the filed Item 1, the filed
      income statement and the filed cash-flow statement
- [x] No UNRESEARCHED verdict was returned, so none needs an artifact named. The three
      unavailable competitors are recorded as an open item inside Q2 with the ladder rung and
      the HTTP obstacle named; they do not carry a verdict and could not reverse an OUT
- [x] No UNKNOWABLE verdict was returned. Q2's OUT is explicitly distinguished from the
      [E4-04] perimeter close that the framework's 2026-09-20 ruling makes UNKNOWABLE
- [x] Step 0: the filing was read, with accession numbers; operating cash flow $191.7M and
      capital expenditures $9.3M were cross-checked against the filed FY2025 statements
- [x] Owner earnings: **not reported as a verdict input, and no verdict rests on it.** The only
      owner-earnings arithmetic in this file sits inside the COMPUTATION block, headed as
      operator rule 3 requires, carrying no entry language. **No net-income proxy was used
      anywhere** (operator rule 5; the addendum of 2026-09-20 on the net-income-proxy seven)
- [x] Competitor row filled: 3 peers plus the subject, same metric, same window, every cell
      filing-sourced. The moat is **not** marked PROVISIONAL; the class is NONE, established
      from the subject's own filings
- [x] The furnished 8-K EX-99.1 releases were pulled and read before [E4-29] was recorded, per
      the standing CGNX instruction; recorded beneath the close and NOT scored
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury
      daily par yield curve), dated 09/18/2026, struck fresh in this run
- [x] No value range stated; Q5 did not open
- [x] No bar chosen; Q5 did not open. **Windage: not spent. Nothing was valued.**
- [x] Price dated 2026-09-18 and flagged as an aggregator live quote (Yahoo Finance), used for
      the quote only; the share count came from the cover of the newest periodic filing with
      the accession number and the as-of date quoted
- [x] `principle_ledger.csv` was **counted, not taken from the pointer: 311 data rows**, not
      the 267 the stale KEY FILES table in `CLAUDE.md` records. Every ledger id cited in this
      file was checked to exist in that file; **zero phantoms**
- [x] Run committed to git with a pathspec and a freshly written message file
- [x] No em dashes in this run's own prose. The 17 that remain are the template's own
      headings and boilerplate, plus punctuation inside verbatim corpus and filing quotes,
      which PRIME RULE 1 forbids smoothing

## REGISTER
- Verdict: **[x] OUT (about the business)**
- One line: **EMBC FAILS at Q2. [E3-03] criterion 2 fails on the company's own filed words:
  the FY2025 10-K's MD&A carries the headings "Commoditization of Injection Devices" and
  "Pricing Pressures" and states that GLP-1s, once-weekly insulin and SGLT-2s "have delayed
  initiation of insulin therapy and contributed to less demand for our products" while
  developed-market insulin therapy "continues to transition to infusion pumps", which is a
  filed admission that close substitutes have already taken the volume; the price and volume
  bridge measures it, with FY2025 minus $52.9M of volume and nine-month FY2026 minus $60.0M of
  volume AND minus $27.4M of price, the single Q3 price give-back of $20.1M running at 7.4% of
  that quarter's revenue, so [E2-44] and [E4-37] both answer no and [E2-58]'s exception for "a
  cost advantage that is both wide and sustainable" is disclaimed by the filer itself; the
  physical read [E4-55] shows pen needles minus 13.2% and United States revenue minus 20.6%
  over nine months, in the region where the BD-to-Embecta brand transition launched first, and
  under [E4-04] that brand spending buys a replacement rather than defending the same
  advantage, since the 100-year brand and the cannula IP both stayed with Becton Dickinson;
  the pre-2022 economics were [E3-51]'s surfing run and the wave is named in the filing and
  turning; and the competitor row confirms the relative claim, with Insulet up 59.6%, Tandem up
  35.7% and Novo Nordisk up 33.1% over the same two years in which Embecta shrank 3.6% and its
  gross margin fell from 66.9% to 62.6% to 58.7%.**
- **If UNRESEARCHED, THE WORK ORDER:** not applicable; no UNRESEARCHED verdict was returned.
- **If UNKNOWABLE:** not applicable.
