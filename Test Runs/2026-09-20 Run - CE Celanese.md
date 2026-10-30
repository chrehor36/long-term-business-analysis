# Company Run — Celanese Corporation (CE) — 2026-09-20
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
## STEP 0 — THE RATE, THE FILING, AND THE FIVE THINGS THE SCREEN GOT WRONG

**Sovereign, for the currency the business EARNS in** -- the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **09/18/2026** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, struck in this run with `python tools/sources.py` on 2026-09-20.
  FRED DGS30 is the fallback and was not used.
- **The currency question is NOT automatic here, and the brief was right to say so.** Net
  sales by geographic destination, FY2025 10-K Note 22, from the filed table: North America
  **$2,898M**, Europe and Africa **$3,059M**, Asia-Pacific **$3,357M**, South America
  **$230M**, of **$9,544M**. **North America is 30.4% of sales; no currency is a majority.**
  USD is used anyway, and the ground is stated rather than assumed:
  (1) the registrant reports in USD and the quote is USD on the NYSE;
  (2) the Acetyl Chain's products -- acetic acid, VAM, acetate tow -- are globally traded
  intermediates whose pricing the filer itself ties to *"industry utilization rates and
  changes in the cost of raw materials"*, not to a domestic price list; and
  (3) **USD at 5.34% is the HIGHEST of the three sovereigns `tools/sources.py` returned**
  (JPY 4.05%, EUR 3.75%, both 2026-09-17), so choosing it is the conservative choice and
  cannot flatter this name.
  **Disclosed limit:** destination-of-sale is not currency-of-settlement and the filing does
  not disaggregate settlement currency. A euro- or yen-weighted blend would lower the
  reference rate by roughly 120-150bp and would make this name look BETTER, not worse. The
  ~10% floor **[E4-28]** does not move with the sovereign in any case -- *"that's true
  whether short rates are 6 percent or whether short rates are 1 percent."*

**The filing was read** -- not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for the fiscal year ended 2025-12-31, filed
  2026-02-24, accession 0001306830-26-000031.** Superseded in part by the **Form 10-Q for the
  quarter ended 2026-06-30, filed 2026-08-05, accession 0001306830-26-000117**, which is the
  source of the current share count and the H1 2026 cash flows. Also read: the **FY2022 10-K,
  accession 0001306830-23-000023** (the acquisition perimeter and the filed FY2022 cash-flow
  statement); the **DEF 14A filed 2026-03-04, accession 0001306830-26-000052**; four
  consecutive 8-K EX-99.1 earnings releases (2025-11-06, 2026-02-17, 2026-05-05, 2026-08-04);
  and three 8-Ks (2026-08-04 Item 1.01, accession 0001104659-26-090359; 2026-06-10 Item 8.01,
  accession 0001104659-26-072110; 2026-09-16 Item 5.02, accession 0001306830-26-000119).
- **figure cross-checked against the filed statement:** XBRL
  `PaymentsToAcquireBusinessesNetOfCashAcquired` for FY2022 returns **10,589,000,000**. The
  filed Consolidated Statements of Cash Flows in the FY2022 10-K reads, verbatim,
  *"Acquisitions, net of cash acquired | ( 10,589 )"* under Investing Activities, in $
  millions. They agree, **and the parentheses are the whole of flag (ii) below.** A second
  cross-check: XBRL `NetCashProvidedByUsedInOperatingActivities` FY2025 returns
  1,146,000,000; the filed FY2025 statement reads *"Net cash provided by (used in) operating
  activities | 1,146"*. They agree.

### FLAG (i) — `cap_flag`. RESOLVED. Both numbers are right; the gap is an 18% price fall over fourteen months, inside a 74% fall over thirty.

The screen said: *"CAP BELOW FILED PUBLIC FLOAT - cap $4,861M against a filed float of
$6,048M (1.24x) as of 2025-06-30. A cap cannot be smaller than a subset of itself."*

- **The float figure is real and I have read it on the cover.** FY2025 10-K cover, accession
  0001306830-26-000031: *"The aggregate market value of the registrant's common stock held by
  non-affiliates as of June 30, 2025 (the last business day of the registrants' most recently
  completed second fiscal quarter) was $ 6,048,316,998 ."*
- **How many classes, read from the same cover and from the 10-Q cover.** *"Common Stock, par
  value $0.0001 per share | CE | The New York Stock Exchange"* -- **one class of stock.** The
  four other NYSE-listed securities on the cover are **debt**: the 2.125% Senior Notes due
  2027 (CE /27), the 0.625% Senior Notes due 2028 (CE /28), the 5.337% Senior Notes due 2029
  (CE /29A) and the 5.000% Senior Notes due 2031 (CE /31). **That is flag (v), and it is the
  most important structural fact in this file.**
- **THE CAP, RE-STRUCK BY HAND.** `cap = close(anchor) x shares(measurement) x splits AFTER
  measurement`.
  - shares(measurement): **109,748,926**, from the **cover of the newest periodic filing**,
    the 10-Q for the quarter ended 2026-06-30, accession 0001306830-26-000117: *"The number
    of outstanding shares of the registrant's Common Stock, $0.0001 par value, as of
    August 3, 2026 was 109,748,926 ."*
  - splits after 2026-08-03: **none.** The chart endpoint returns `events: None` over both a
    5-day and a 3-year range; raw responses saved to `quote_CE_raw.json` and
    `quote_CE_3y_monthly.json`.
  - close(anchor): **$45.41 on 2026-09-18**, the last regular session before this run.
    **AGGREGATOR, FLAGGED** -- Yahoo Finance chart API, live quote only, raw response saved
    to `Test Runs/_research 2026-09-20 CE/quote_CE_raw.json`. Used `close`, never `adjclose`.
  - **cap = 109,748,926 x $45.41 = $4,983,698,730, i.e. $4,984M.**
- **Which branch of the flag is this?** The CALM/EMBC branch, not MCFT. There is no
  share-count error. At the float's measurement date CE closed at **$55.33**, and
  $6,048,316,998 / $55.33 = **109,313,701 shares**, against roughly 109.4M then outstanding.
  **Non-affiliates hold essentially all of the stock**, so the "float" IS the cap, and the
  1.24x ratio is just the price change: 55.33 / 45.41 = 1.218. The screen's own $4,861M
  implies $44.29, a slightly staler quote. **Neither number is wrong.**
- **What the flag actually found.** Monthly closes: **$171.86 (2024-03), $135.96 (2024-09),
  $73.21 (2024-11), $55.33 (2025-06), $42.08 (2025-09), $65.77 (2026-03), $45.41
  (2026-09-18).** The equity has lost **74%** in thirty months and round-tripped a 56% rally
  in between. A cap below its own filed float is, on this name, a de-rating and not a data
  fault. **No yield is reported anywhere in this file before Q1-Q4 close.**

### FLAG (ii) — `acq_note`. THE SCREEN INVERTED THE SIGN AND SUMMED THREE YEARS INTO ONE. The real number is a $10,589M OUTFLOW in 2022, and it is the central fact of this company.

The screen said: *"NET CASH INFLOW on the acquisition line ($11,783M, 242% of cap) - cash
acquired exceeded cash paid."* **Every clause of that is wrong, and the arithmetic that made
it is recoverable.**

`PaymentsToAcquireBusinessesNetOfCashAcquired`, newest vintage, the three years that matter:

| FY | filed value, $M | direction | what it is |
|---|---|---|---|
| 2021 | **(1,142)** | OUTFLOW | the **Santoprene TPV** business bought from ExxonMobil, closed 2021-12-01 |
| 2022 | **(10,589)** | **OUTFLOW** | the **DuPont Mobility & Materials** acquisition, closed 2022-11-01 (8-K Item 2.01, accession 0001104659-22-113226) |
| 2023 | **+52** | inflow | a post-closing purchase-price settlement -- **$52M, not $11.8bn** |

- **10,589 + 1,142 + 52 = 11,783.** That is the screen's number exactly. It summed three
  consecutive years of the acquisition line on **absolute** values, then took the sign of the
  smallest of the three -- the +52 -- and reported it as the sign of the whole. The "242% of
  cap" is a three-year sum divided by today's cap and means nothing.
- **The filed FY2022 statement reads *"Acquisitions, net of cash acquired | ( 10,589 )"***,
  and the FY2022 MD&A: *"Net cash used in investing activities increased $10.0 billion to
  $11.1 billion for the year ended December 31, 2022 compared to $1.1 billion for the same
  period in 2021"*. The FY2025 10-K's comparative column confirms 2023:
  *"Acquisitions, net of cash acquired | — | — | 52"*.
- **So the magnitude is within $1.2bn, the YEAR is wrong, and the SIGN is inverted.**
  Celanese did not receive $11.8bn. It **paid** $11.7bn across two years, and it paid with
  debt. That is flag (v).

### FLAG (iii) — `deal_note`. The liveness check paid again: the one Item 1.01 is a COVENANT RELIEF amendment.

The screen said: *"1 8-K Item 1.01 filing(s) since 2026-02-24, none carrying a merger
agreement (EX-2.1) - most likely a credit facility or offering; **open them only if something
else is odd.**"* It is a credit facility. **It is also the loudest document in this file.**
8-K filed 2026-08-04 for an event of 2026-07-31, accession 0001104659-26-090359, verbatim:

> "The Amendment (i) **increases the consolidated net leverage ratio financial covenant
> level** applicable under the Revolving Credit Agreement from the fiscal quarter ending
> March 31, 2027 through the maturity date to initially **5.50:1.00** and provides for
> modified step-down levels for such covenant thereafter, (ii) increases the size of the
> combined negative covenant baskets available under the Revolving Credit Agreement for
> incurring debt of foreign subsidiaries in connection with acquisitions by such foreign
> subsidiaries and for incurring debt of Chinese subsidiaries for corporate purposes from
> $900 million to $1,050 million"

A borrower asks for its leverage covenant to be **raised** for one reason. **"Open them only
if something else is odd" was the wrong instruction and it is recorded here as a defect in
the brief** -- the CGNX error in a new place, telling a run which document will be boring.

**Liveness, confirmed on four independent marks:**
- Common stock listed on the NYSE, on the cover of the 8-K dated 2026-08-04 and of the 10-Q
  filed 2026-08-05.
- Newest periodic filing: 10-Q for the quarter ended 2026-06-30, filed 2026-08-05.
- Forms 4 filed 2026-08-12 (six), 2026-08-13 and 2026-08-17; a Form 3 on 2026-09-17.
- **The one alarming-looking filing is not alarming.** A **Form 25-NSE was filed 2026-06-25**
  (accession 0000876661-26-000556, filed by the NYSE). It is **not** a delisting of the
  equity. The 8-K of 2026-06-10, accession 0001104659-26-072110: *"Celanese US Holdings LLC
  ... issued a notice of redemption for all of its outstanding 4.777% Senior Notes due
  July 19, 2026 ... The redemption is expected to occur on June 25, 2026"*. The 25-NSE removes
  the redeemed **notes**. Two earlier 25-NSEs (2025-02-11, 2023-09-26) match earlier note
  maturities the same way.

### FLAG (iv) — `spread_caveat` and `years_filed = 19`. The window is rebuilt: nineteen years, 2007 through 2025, and the perimeter moved twice inside it.

The screen could see a 4-construction width over five years. The full series, from
`companyfacts` at the **newest vintage** for each fiscal year end, every figure traceable to
a 10-K under CIK 0001306830, $ millions:

| FY | net sales | net earnings | OCF | capex | D&A | SBC |
|---|---|---|---|---|---|---|
| 2007 | 6,444 | 426 | 566 | 288 | 311 | not tagged |
| 2008 | 6,823 | 281 | 586 | 274 | 360 | not tagged |
| 2009 | 5,082 | 498 | 596 | 176 | 319 | not tagged |
| 2010 | 5,918 | 377 | 452 | 201 | 300 | not tagged |
| 2011 | 6,763 | 427 | 638 | 349 | 298 | not tagged |
| 2012 | 6,418 | 372 | 722 | 349 | 308 | 20 |
| 2013 | 6,510 | 1,101 | 762 | 277 | 305 | 24 |
| 2014 | 6,802 | 624 | 962 | 254 | 292 | 46 |
| 2015 | 5,674 | 304 | 862 | 232 | 357 | 40 |
| 2016 | 5,389 | 900 | 893 | 246 | 290 | 31 |
| 2017 | 6,140 | 843 | 803 | 267 | 305 | 47 |
| 2018 | 7,155 | 1,207 | 1,558 | 337 | 343 | 71 |
| 2019 | 6,297 | 852 | 1,454 | 370 | 352 | 48 |
| 2020 | 5,655 | 1,985 | 1,343 | 364 | 350 | 28 |
| 2021 | 8,537 | 1,890 | 1,757 | 467 | 371 | 95 |
| 2022 | 9,673 | 1,894 | 1,819 | 543 | 462 | 60 |
| 2023 | 10,926 | 1,943 | 1,899 | 568 | 706 | 40 |
| 2024 | 10,268 | **(1,542)** | 966 | 435 | 801 | 32 |
| 2025 | 9,544 | **(1,165)** | 1,146 | 343 | 760 | 24 |

**Nineteen years, FY2007 to FY2025.** Each year is taken from the newest 10-K that reports it
(the restatement-vintage rule; FY2007-08 from the 10-K filed 2010-02-12, FY2025 from the
10-K filed 2026-02-24, accession 0001306830-26-000031). **SBC is not tagged before FY2012**;
that is a source limit, not a zero, and the pre-2012 years are therefore not used as an
owner-earnings base (the BE ruling: a silently substituted SBC of zero overstates owner
earnings, which is the one direction that matters when the question is whether to buy).

**The perimeter moved twice inside any window longer than four years.** `name_change_note`
and `wc_note` were both empty; empty is an absence of a finding, not a finding of absence:
1. **Santoprene / TPV**, bought from ExxonMobil for $1,142M net of cash, closed 2021-12-01.
2. **DuPont Mobility & Materials**, bought for $10,589M net of cash, closed 2022-11-01. It
   roughly doubled Engineered Materials and is why net sales step from $8,537M to $10,926M
   and D&A steps from $371M to $801M.
3. **A disposal inside the same window:** FY2023 carries *"Proceeds from sale of businesses
   and assets, net | 480"* and *"Gain (loss) on disposition of business and assets, net |
   505"* -- a one-off gain inside the highest OCF year in the table.

**A mean taken across 2021-2025 averages three different companies.** Recorded here, before
any averaging, as the window rule requires **[E4-38]**.

### FLAG (v) — NOT ON THE SCREEN AT ALL, AND IT GOVERNS THE FILE. The equity is a third of the capital.

From the filed FY2025 consolidated balance sheet and the 10-Q for 2026-06-30, $ millions:

| | 2025-12-31 | 2026-06-30 |
|---|---|---|
| Short-term borrowings and current installments of long-term debt | **1,204** | **1,311** |
| Long-term debt, net of unamortized deferred financing costs | **11,394** | **10,696** |
| **Total debt** | **12,598** | **12,007** |
| Cash and cash equivalents | 1,263 | 1,364 |
| **Net debt** | **11,335** | **10,643** |
| Total equity (incl. $423M noncontrolling interests) | 4,472 | 4,588 |
| Total assets | 21,695 | 21,408 |

Interest expense, from the filed income statement: **$701M (FY2025), $676M (FY2024), $720M
(FY2023).**

**Market cap $4,984M against net debt of $10,643M.** The enterprise costs roughly **$15.6bn**
and the equity is **32%** of it.

**The brief's prior about what that does to the screen's yield is HALF WRONG, and the
correction is written down here.** The framework's owner-earnings construction is operating
cash flow, less SBC, less the (c) guess -- and **operating cash flow is already net of the
$690-700M of interest the debt costs every year.** The numerator is a levered residual and it
belongs against the equity cap. Dividing an OCF-based owner-earnings figure by enterprise
value would **double-count the debt**. The debt does not mechanically destroy the equity
yield. **Where it bites is Q4** -- [E5-11]'s third strength, [E2-54]'s coverage test, and the
named way this business dies -- and that is where it is scored.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language.** Celanese buys methanol,
ethylene, carbon monoxide and natural gas and runs them through two chains.

**The Acetyl Chain** (FY2025: **$4,154M** of third-party net sales, 43.5% of the total;
segment operating profit **$539M**). It makes acetic acid and its derivatives -- acetic
anhydride, vinyl acetate monomer, acetate esters, emulsion polymers, redispersible powders --
plus acetate tow for cigarette filters. **These are commodities in the strict sense.** The
filer says so itself, in the 10-Q MD&A: *"The pricing of products within the Acetyl Chain is
influenced by industry utilization rates and changes in the cost of raw materials. Therefore,
in general, there is a directional correlation between these factors and our Net sales for
most Acetyl Chain products."* The money is the spread between a globally set price and the
company's own cost of conversion, times tonnes. The company's claim is a cost position:
*"We believe our production technology is among the lowest cost in the industry and provides
us with global growth opportunities through low cost expansions and a cost advantage over our
competitors"*, resting on AOPlus 3 for acetic acid and VAntage 2 for VAM. Whether that
survives a competitor row is Q2's problem, not Q1's.

**Engineered Materials** (FY2025: **$5,390M**, 56.5%; segment operating profit **$594M**
before $1,552M of impairment and other charges). It compounds and sells engineering polymers
under brand names -- POM (Celcon, Hostaform), nylon (Zytel), LCP (Vectra, Zenite), PBT
(Celanex, Crastin), TPV (Santoprene), UHMW-PE (GUR), EVA (VitalDose). **These are sold into a
specification**: a part designer qualifies a resin grade into a mould, and switching means
re-qualifying the part. The filer calls it *"a project-based business where growth is driven
by increasing new project commercializations from the pipeline"*, and states the pricing
mechanism plainly: *"the pricing of products in this segment is primarily based on the
value-in-use and is generally independent of changes in the cost of raw materials. Therefore,
in general, margins may expand or contract in response to changes in raw material costs."*
**That last sentence is the honest one and it is the whole unit economics: EM prices lag
input costs in both directions.** The money is a per-pound spread over resin cost, earned on
volumes locked in years earlier at the design stage, and lost when the end market -- roughly
half of it automotive -- stops building.

**The scarce input this business controls.** Two different answers for two segments, and the
difference is itself the Q1 answer:
- **Acetyl Chain:** low-cost, scaled, integrated acetyls capacity -- the Clear Lake, Texas
  methanol-to-acetic-acid complex, the Nanjing integrated site, and a 25% interest in
  National Methanol Company (Saudi Arabia) supplying methanol feedstock. **The scarce thing
  is the plant, not the product**, and a plant is replicable by anyone with capital and time.
- **Engineered Materials:** the qualified position inside a customer's part -- **the
  switching cost of re-certifying an automotive or medical component** -- plus 17 strategic
  affiliates, of which Korea Engineering Plastics (50%-owned, POM) is the largest.

**Will the fundamentals look broadly the same in ten years?** Yes, and that is not a
compliment. Acetic acid has been made by methanol carbonylation since the 1970s; the company
traces itself to 1918 and *"The American Cellulose & Chemical Manufacturing Company"*. The
end markets -- automotive, construction, coatings, adhesives, paints, packaging, medical,
cigarette filters -- are the same ones it served ten years ago. **The business is "relatively
simple and stable in character" [E3-31] in what it sells; it is emphatically not stable in
what it earns**, which the nineteen-year table shows in one column: OCF of $452M in 2010,
$1,899M in 2023, $966M in 2024. Two sub-questions that could have made this UNRESEARCHED and
do not:
- *Does acetate tow disappear with smoking?* It is disclosed and located: acetate tow sits
  inside the Acetyl Chain, and the 10-K names *"China National Tobacco Corporation, a Chinese
  state-owned tobacco entity"* as venture partner *"for over three decades"* in *"three
  separate ventures in China"* held at *"approximately 30%"*. A declining annuity inside a
  segment, not a black box.
- *Can the two halves be told apart in the numbers?* Yes. Note 21 gives net sales, gross
  profit, operating profit, D&A, capex, equity earnings of affiliates and total assets for
  Engineered Materials, Acetyl Chain and Other Activities, for three years each.

**The honest caveat, and it does not close Q1.** Eleven thousand four hundred employees, 51
production facilities, 20 affiliate facilities, two segments, four selling regions, 17
strategic affiliates, $12.6bn of debt in several currencies. This is not a simple company.
But **[E4-46]** is the test -- *"if we can't make a decision in five minutes, we can't make
it in five months"* -- and the decision does not need five months of study: the filing says
what it sells, to whom, at what margin, in two segments, with the commodity half labelled a
commodity by the filer itself.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The three conditions, scored on the filer's own numbers and its own words.**

- **(1) Needed or desired — YES.** Acetic acid, VAM and POM are inputs to paints, adhesives,
  packaging, cigarette filters, fuel systems and window-lift mechanisms. The demand is real
  and it is old.
- **(2) Thought by its customers to have NO CLOSE SUBSTITUTE — NO, in both segments, and the
  filings of the company and of its competitors both say so.** This is where the file closes.
- **(3) Not subject to price regulation — YES, not regulated.** No relief here either: the
  corpus is explicit that regulation *floors* a commodity business and *caps* a franchise
  **[E2-59]**, and neither creates the class. Celanese has neither the floor nor the cap.

### The evidence for criterion 2 — the price and volume series, which the filer publishes itself

The 10-K and 10-Q MD&A give an annual decomposition of the net-sales change into volume,
price and currency, by segment. This is **[E4-55]**'s physical series and **[E4-37]**'s
pricing metric in one table, filed by the company, in percentages:

| period | EM volume | EM price | AC volume | AC price | source |
|---|---|---|---|---|---|
| FY2023 vs FY2022 | +54 *(the M&M acquisition)* | **(1)** | +2 | **(17)** | FY2023 10-K, accn 0001306830-24-000029 |
| FY2024 vs FY2023 | **(5)** | **(3)** | +4 | **(6)** | FY2024 10-K, accn 0001306830-25-000027 |
| FY2025 vs FY2024 | **(4)** | **(1)** | **(6)** | **(6)** | FY2025 10-K, accn 0001306830-26-000031 |
| H1 2026 vs H1 2025 | **(3)** | +2 | **(3)** | +7 | 10-Q, accn 0001306830-26-000117 |
| Q2 2026 vs Q2 2025 | **(6)** | +5 | 0 | **+18** | same 10-Q |

**Engineered Materials — the half that is supposed to be differentiated — has cut price in
three consecutive years while volume fell in three consecutive years.** The 10-K names the
cause in its own words: *"lower pricing ... as well as our Engineered Materials segment,
primarily due to **competitive market dynamics**, and product mix"* (FY2025), and the
identical phrase in FY2024. **[E4-37]** is the inverse metric -- *"it's not a great business
when you have to have a prayer session before you raise your prices a penny"* -- and a
business that cuts price for three years while losing units is at the far end of it. **The
[E3-33] question therefore answers itself: there is no untapped pricing power here. A
manager could not raise the return by raising prices; the manager has been lowering them.**

**The Acetyl Chain is the commodity case, stated by the filer.** FY2025 10-K: *"lower pricing
in our Acetyl Chain segment, primarily due to **an environment with greater supply than
demand**"*; FY2024 10-K, identically: *"lower pricing, driven by our Acetyl Chain segment due
to **an environment with greater supply than demand**"*; and the mechanism, from the 10-Q:
*"The pricing of products within the Acetyl Chain is influenced by industry utilization rates
and changes in the cost of raw materials."* That is **[E2-58]** word for word from the other
side of the table: *"persistent over-capacity without administered prices (or costs) equals
poor profitability"*, with long-run profitability set by *"the ratio of supply-tight to
supply-ample years."* Acetyl price: **-17%, -6%, -6%, then +18% in a single quarter.** The
ratio of supply-tight to supply-ample years IS this business's income statement.

**[E2-44]'s two-characteristic test, scored:** (1) can it raise prices easily when demand is
flat and capacity is not fully utilised? **No** -- 2025 had volume -4% and price -4%
simultaneously, company-wide. (2) can it accommodate large dollar-volume increases with only
minor additional investment of capital? **No** -- it bought $11.7bn of revenue for $11.7bn of
cash. Both characteristics fail.

### THE COMPETITOR ROW — required [E3-28]. A moat is a claim about *relative* position.

**How many competitors the industry actually has, taken from a competitor's own filing rather
than from this company's.** Eastman Chemical's 10-K for FY2025 (filed 2026-02-13, accession
0000915389-26-000013) prints a "Principal Competitors" column against each product line:

> *Intermediates -- Oxo alcohols and derivatives, **Acetic acid and derivatives**, **Acetic
> anhydride** ... Principal Competitors: **Lyondell Bassell, BASF SE, Dow Inc., OXEA,
> Celanese Corporation, Lonza, Ineos Group Holdings S.A**"*

> *"**Acetate Tow** Estron cellulose acetate tow -- Principal Competitors: **Celanese
> Corporation, Cerdia International, Daicel Corporation, Jinan Acetate Chemical**"*

So the acetyls business has **at least eight** named producers including Celanese and
Eastman, and acetate tow **at least five**. Eastman names Celanese three separate times.
**The industry does not lack competitors; it is a census of them.**

**The row, same metric, same window, each figure from the named filer's own 10-K XBRL at the
newest vintage.** The metric is **[E3-46]**'s -- *"the best businesses, by definition, are
going to be businesses that earn very high returns on capital employed over time"* --
computed identically for every filer as **EBIT = pretax income + interest expense**, over
**capital employed = total assets less current liabilities**. Window FY2018-FY2025, eight
years, one full cycle:

| Company | ROCE 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **8-yr mean** | **2023-25 mean** |
|---|---|---|---|---|---|---|---|---|---|---|
| **Celanese (CE)** | 21.7 | 14.3 | 26.4 | 24.7 | 8.2 | 8.4 | (1.8) | (2.9) | **12.4** | **1.2** |
| LyondellBasell (LYB) | 24.9 | 17.4 | 6.4 | 24.8 | 17.1 | 9.3 | 5.9 | (2.6) | **12.9** | 4.2 |
| Westlake (WLK) | 14.0 | 5.8 | 3.8 | 17.7 | 17.1 | 4.7 | 5.1 | (9.3) | 7.4 | 0.2 |
| Dow (DOW) | 7.1 | (0.6) | 5.8 | 17.8 | 13.7 | 2.9 | 5.1 | (3.3) | 6.1 | 1.6 |
| Huntsman (HUN) | 11.6 | 6.2 | 4.9 | 17.0 | 10.7 | 1.6 | (0.7) | (3.5) | 6.0 | (0.9) |
| Eastman (EMN) | 7.6 | 4.8 | 2.3 | 7.0 | 7.0 | 7.2 | 7.0 | 2.9 | 5.7 | **5.7** |
| DuPont (DD) | 0.6 | 0.9 | (1.0) | 4.8 | 5.2 | 0.3 | 1.6 | 2.7 | 1.9 | 1.5 |
| Avient (AVNT) | 1.8 | 1.9 | (0.3) | 3.2 | (1.1) | (0.5) | 4.4 | 2.2 | 1.4 | 2.0 |

- **Peers named: 7, from an industry that names at least 8 in acetyls alone.** Chosen because
  each is an SEC registrant whose own filed statements can be read on the same basis, and
  each competes in at least one of Celanese's two segments: **EMN** (acetic acid, acetic
  anhydride, acetate tow, additives -- the closest single comparator, and it names Celanese),
  **DOW** and **LYB** (acetyl derivatives, VAE emulsions, intermediates), **WLK** and **HUN**
  (scaled commodity chemical converters running the same over-capacity equation), **AVNT**
  (specialty polymer compounding -- the direct Engineered Materials comparator), **DD** (the
  seller of the Mobility & Materials business and still a specialty-materials competitor).
- **Rejected, with the reason:** **BASF SE, Kuraray, Wanhua, Daicel/Polyplastics, Cerdia,
  Jinan Acetate, Ineos, OXEA, Lonza, SABIC, Covestro, Syensqo** -- all real competitors
  (BASF, Dow, OXEA, Ineos and Lonza are named by Eastman; Daicel, Cerdia and Jinan are named
  in tow), none an SEC registrant on a comparable basis. **That absence cannot rescue the
  verdict and it does not make the class PROVISIONAL, because the missing names can only ADD
  competitors to the row, never remove them, and criterion 2 fails on the presence of close
  substitutes rather than on their absence.** Said plainly so the limit is on the record.

### What the row shows, and the one place I hunted hardest against my own reading [E4-26]

**The claim to test is the company's own, and it is the only [E2-58] exception that exists:**
*"We believe our production technology is among the lowest cost in the industry and provides
us with ... a cost advantage over our competitors"* (FY2025 10-K, Item 1). **[E2-58]** allows
exactly this escape and no other: *"A few producers in such industries may consistently do
well if they have a cost advantage that is both **wide and sustainable** ... By definition
such exceptions are few."*

**Wide: yes, historically.** Over the eight-year window Celanese's 12.4% mean ROCE is second
of eight, effectively tied with LyondellBasell and roughly double Eastman's, Dow's and
Huntsman's. From 2018 to 2021 the lead was large and real.

**Sustainable: no, and this is the finding.** Over the three years since the M&M acquisition
closed, Celanese's mean ROCE is **1.2%, sixth of the eight**, behind Eastman (5.7%),
LyondellBasell (4.2%), Avient (2.0%), Dow (1.6%) and DuPont (1.5%). **The company that says
it has the industry's lowest cost position has earned less on its capital than the company
Eastman's own filing puts beside it, for three consecutive years.**

**I tested the obvious objection, because most of that gap is impairment.** Adding back the
filed asset impairment losses from the cash-flow statement ($1,639M in 2024, $1,513M in 2025)
and stripping the $505M disposal gain from 2023, Celanese's ROCE becomes **6.1% (2023), 6.8%
(2024), 5.5% (2025) -- a three-year mean of 6.1%.** That is an honest number and it is
**still only at the peer median**, against Eastman's unadjusted 5.7%. **The impairments were
not what destroyed the lead. The lead is gone on cash economics.**

**And [E2-43]'s denominator makes the point sharper, as it is supposed to for an acquisitive
filer.** Capital employed at 2025-12-31 is $18,012M, of which **$4,171M is goodwill and
$3,184M is net intangible assets** -- a $7,355M wedge, almost all of it created by the M&M
purchase. On **unleveraged net tangible assets of $10,657M**, the 2025 ex-impairment EBIT of
$994M is **9.3%**. On the capital the owners actually committed, it is **5.5%.** *"the
managers of the units should be judged by the returns they achieve on the underlying assets;
what we pay for a business does not affect the amount of capital its manager has to work
with"* **[E2-73]** -- the plants earn about 9%; the shareholders earn about 5.5%; the
difference is the price paid, and it is a Q3 fact, recorded here because the row is where it
becomes visible.

### The category test — and the distinction the SMPL run turned on

**Most of what is depressing about this row is a CATEGORY fact and is not scored against
Celanese.** Every one of the eight filers is at or near a cyclical trough: five of the eight
have negative ROCE in 2025. A cost or price fact true of the whole category is not a moat,
and its mirror is also true -- **a downturn true of the whole category is not a moat defect.**
The Q2 verdict below therefore does **not** rest on the 2024-25 collapse.

**It rests on the two things in this row that are RELATIVE:**
1. **Celanese's rank fell from second to sixth within its own category**, on an
   eight-year-consistent metric, over precisely the three years in which the lowest-cost
   claim should have been paying. A relative fall inside a common downturn is not a category
   fact.
2. **The price series is the company's own, segment by segment, and it is the one thing
   [E3-03] criterion 2 actually tests.** Engineered Materials cut price in three consecutive
   years while losing units. A product whose maker must cut price to hold a shrinking volume
   is a product its customers believe has a close substitute, whatever the category is doing.

### The other Q2 tests, scored

- **[E4-04] -- must the moat be continuously rebuilt?** The Acetyl Chain's advantage is a
  **plant**, and a plant is a depleting, replicable asset whose lead is rebuilt by building
  the next one. AOPlus 3 and VAntage 2 are process technologies; the filer's own claim is
  that they let it *"construct a world scale greenfield acetic acid facility at a lower
  capital cost"* -- that is the advantage of the **next** build, not the defence of the
  existing one. This is the Mitsui/Rhodes Ridge side of the scope test, not the Coca-Cola
  side. **It is not applied as a verdict here**, per the 2026-09-20 ruling that [E4-04] is a
  competence limit and never a fourth franchise criterion; criterion 2 has already failed on
  filed evidence, which is an OUT on the business and not a perimeter close.
- **[E4-32] direction:** the moat is narrowing, not widening. Accumulated goodwill impairment
  in Engineered Materials reached **$2.7 billion** by 2025-12-31 (Note 9: *"Includes
  accumulated impairment losses of $ 2.7 billion in the Engineered Materials segment"*),
  against $1.5bn a year earlier, plus **$463M of indefinite-lived trade-name impairments**
  ($117M in 2024 and $346M in 2025, the latter *"primarily Zytel"*). **A company writing off
  the trade name it bought three years ago is filing its own opinion of the brand.**
- **[E2-53] the dominance class:** no. Position does not set the economics here; industry
  utilisation does, and the filer says so.
- **[E4-36] which of the four causes of extreme success:** wave-riding. The 2018 and
  2021 ROCE peaks are acetyls up-cycles, as the -17%/+18% price swings show. *"when a surfer
  gets up and catches the wave ... But if he gets off the wave, he becomes mired in
  shallows"* **[E3-51]**. **A surfing run is not a moat; the advantage lives in the wave.**
- **[E3-61] the row's limit, stated:** the row shows position and cannot show conduct. Eight
  producers could behave like a demented Kellogg or could not, and *"you'd have to know the
  people involved."* Nothing in this row predicts what the other seven will do with their
  next capacity decision -- which is itself the point of [E2-27], recorded at Q4 below.

- Class: **[x] NONE** (Acetyl Chain) / **narrow and narrowing, refuted on the filed price and
  volume series** (Engineered Materials) · Direction: **narrowing**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**Why OUT and not UNKNOWABLE.** The separating test **[E4-19]**: can I name the document that
would resolve this? There is no missing document. The company publishes its own
price-and-volume decomposition by segment, its own goodwill and trade-name impairments, and
its own description of acetyls pricing as a function of industry utilisation; a competitor
publishes the census of producers. **The evidence is here and the business fails criterion 2
of [E3-03].** This is not the perimeter close that the 2026-09-20 [E4-04] ruling creates for
a business whose durability cannot be judged from filings -- it can be judged, and it is
judged.

**THE FILE CLOSES HERE.** Everything below is recorded **WITHOUT VERDICTS**, under the hard
sequence.


---
# RECORDED BELOW THE CLOSE — NO VERDICTS

⛔ **Q2 returned OUT. Under the hard sequence, Q3 through Q6 carry no verdicts and Q5 opens
no clearance.** What follows is recorded because the operator protocol requires a closed run
to state what it found at the later gates, and because two of these findings are sharper than
the one that closed the file.

## Q3 — WHAT THE FILINGS SHOW ABOUT HONESTY AND RATIONALITY *(no verdict)*

**THE WEIGHT CASE, declared.** *How much damage can this manager do before I can react?*
- [ ] **Daily execution [E3-38]** — no. Acetic acid does not need a smart decision every day.
- [ ] **Control [E1-16]** — no. This would be a minority position in a listed security.
- [x] **Leverage [E3-29]** — **YES.** Total debt $12,007M against book equity of $4,588M at
  2026-06-30, and a market cap of $4,984M. *"leverage of 20:1 magnifies the effects of
  managerial strengths and weaknesses"* is said of banks, but the mechanism is the mechanism:
  here a 15% permanent impairment of enterprise value wipes out roughly half the equity.
  **One box ticked, so if this file had reached Q3 it would have been a BINARY GATE and no
  price would compensate.** Recorded, not scored.

### The capital-allocation record, from the filed cash-flow statements

| FY | share repurchases, $M | common dividends, $M | acquisitions, $M | net debt at year end, $M |
|---|---|---|---|---|
| 2018 | 805 | 280 | (144) | |
| 2019 | 996 | 300 | (91) | |
| 2020 | 650 | 293 | (100) | |
| 2021 | **1,000** | 304 | **(1,142)** | |
| 2022 | 17 | 297 | **(10,589)** | |
| 2023 | **0** | 305 | +52 | |
| 2024 | **0** | 307 | 0 | ~11,600 |
| 2025 | **0** | **13** | 0 | **11,335** |

**The sequence, read in order.** Between 2018 and 2021 Celanese spent **$3,451M** buying its
own shares, at prices that the monthly series puts between roughly $90 and $160. In 2021 and
2022 it spent a further **$11,731M** buying two businesses, at the top of the best two years
in the company's filed history -- the FY2021 release says *"record GAAP diluted earnings per
share of $17.06 and record adjusted earnings per share of $18.12 ... record operating cash
flow of $1.8 billion and record free cash flow of $1.3 billion"*. In 2023 the buyback stopped
and has not restarted. In 2025 the dividend was cut by **95%**, in the 10-K's own words:
*"In furtherance of our deleveraging efforts, we have paused our share repurchase program ...
we reduced our quarterly dividend by approximately 95% beginning in the first quarter of
2025."* The shares are now $45.41.

- **[E5-24], the first law: *"what is smart at one price is dumb at another."*** Applied to
  both legs. The buybacks were made at three times today's price; the acquisition was made at
  the cycle peak and has since been written down by **$2.7bn of goodwill and $463M of trade
  names**. **[E5-31]**'s real test is per-share value added at the price paid, and on the
  filed record the answer is negative on both.
- **[E2-30], the institutional imperative, behaviour (2): *"corporate projects or
  acquisitions will materialize to soak up available funds."*** A record-cash year was
  followed by the largest acquisition in the company's history. The last clause of [E2-30]
  governs and is quoted so the finding is not overstated: *"Institutional dynamics, not
  venality or stupidity, set businesses on these courses."*
- **[E2-52] and [E2-60].** The dividend was NOT funded by share issuance, so [E2-52]'s literal
  test does not fire. **[E2-60] does**: restricted earnings are those whose payout costs the
  business *"its ability to maintain its unit volume of sales, its long-term competitive
  position, **its financial strength**."* Celanese paid $297M, $305M and $307M of dividends
  in 2022, 2023 and 2024 while net debt sat above $11bn and while it was amending its
  leverage covenants -- *"During the years ended December 31, 2025 and 2024, we amended
  certain covenants in certain U.S. Credit Facilities, including financial ratio maintenance
  covenants"* (FY2025 10-K, Covenants). Then it cut the dividend by 95% and amended the
  covenant again in July 2026. **(c) was understated by exactly the amount of those
  dividends**, which is [E2-60]'s point and is carried into the Q4 arithmetic below.
- **[E2-51], the refusal tell, does NOT fire against them here.** Declining to repurchase
  stock at $45 while carrying $12bn of debt and a 5.50x covenant is the correct decision under
  [E5-08] condition (1) -- ample funds for operations and liquidity -- which is not satisfied.
  The flag fired seven years ago, not now.
- **[E4-13], the humility clause, stated as the rule requires:** *"it is natural for CEOs to
  be optimistic about their own businesses. They also know a whole lot more about them than
  I do."* This is a reading of a filed record, not a claim to have known better in 2022.

### The flags [E4-22, E4-29, E5-15, E2-49], each a prompt to read

- [ ] weak accounting — **one item, and it points toward candour.** The FY2025 10-K discloses
  an *"Immaterial Revision of Prior Period Financial Statements"*: errors in a distributor
  rebate accrual and prepaid insurance, corrected by *"decreasing Retained earnings by $ 46
  million, increasing total liabilities by $ 27 million and decreasing Total assets by $ 19
  million"*, voluntarily revised *"to promote the consistency and comparability of the
  financial statements."* Small, quantified line by line, and disclosed without being
  required to be. **[E2-69]**: a deviation toward candour is not the weak-accounting flag.
- [ ] unintelligible footnotes — no. The debt, goodwill and segment notes are legible and the
  price-and-volume decomposition that closed this file is the company's own publication.
- [x] **trumpeted earnings projections** — **FIRES.** Q1 2026 release: *"This progress
  supports our decision to **raise our full-year free cash flow outlook to $700 to $800
  million**"*. Guidance on a non-GAAP cash measure, revised upward mid-year. **[E5-30]**:
  *"once you start it, it's all over ... And forecasting earnings, I can't imagine anything
  more destructive."* A ratchet, not a one-year fact.
- [ ] serial share issuance **[E5-15]** — **no, and emphatically not.** Shares outstanding
  went 108.5M (2023) → 109.3M (2024) → 109.6M (2025) → 109.7M (Aug 2026), the increase being
  stock-plan vesting only. *"The Company did not repurchase any Common Stock during the years
  ended December 31, 2025, 2024 and 2023."* No equity was issued to service the debt. **This
  is the strongest single fact on the management's side of the ledger** and it is recorded as
  such: faced with a covenant problem, they did not dilute.
- [x] **EBITDA / adjusted-earnings promotion [E4-29]** — **FIRES AT FULL STRENGTH, AND IT IS
  IN THE PAY.** Every earnings release leads with it. FY2025, verbatim: *"full year 2025 U.S.
  GAAP diluted **loss** per share of $10.44 and **adjusted earnings per share of $3.98** ...
  consolidated operating loss of $786 million, **adjusted EBIT of $1.2 billion, and operating
  EBITDA of $1.9 billion** at margins of (8), 12, and **20** percent"*, with *"the difference
  ... primarily due to **Certain Items totaling $1.6 billion**."* A GAAP operating margin of
  minus 8% is presented beside a 20% "operating EBITDA" margin in the same sentence. The word
  "operating EBITDA" appears **eight times** in that one release and once in the FY2021
  release. **[E5-41]** is the mechanism and it is exact here: *"Depreciation is where you
  spend the money first ... and record the expense later. And it's reverse float."* Celanese
  spent $11.7bn of cash first; the amortisation of that spend is what the headline metric
  deletes.
- [x] **[E2-49] metric-switching — FIRES, with a date and a quotation.** The DEF 14A filed
  2023-03-09 (accession 0001306830-23-000047) says, of the annual incentive plan: *"**Use of
  Adjusted EBITDA as the primary financial metric (in lieu of Adjusted EBIT)**"*, and in the
  pay-versus-performance footnote: *"Adjusted EBIT and Working Capital as a Percentage of Net
  Sales were the primary metrics in our 2022 Annual Incentive Plan for NEOs. **For the 2023
  Annual Incentive Plan, these metrics were replaced with Adjusted EBITDA and Free Cash
  Flow.**"* **The M&M acquisition closed on 2022-11-01 and took D&A from $462M to $706M to
  $801M. The yardstick was changed from one that charges that amortisation to one that does
  not, in the first plan year after the acquisition that created it.** [E2-49]: *"Yardsticks
  seldom are discarded while yielding favorable readings ... most managers favor disposition
  of the yardstick rather than disposition of the manager."* The 2026 proxy confirms the new
  metric is still primary: *"continuing to use operating EBITDA as the primary financial
  metric while increasing the weight of free cash flow."*
  *(The prior on this flag stood at six fires and five failures before this run; it now fires
  a seventh time.)*
- [x] **A structural point about the long-term plan's own ROCE, offered as a prompt and not
  as a finding about anyone's honesty [E5-38].** The 2026 proxy defines the PRSU metric:
  *"Return on capital employed, which we define as **Adjusted EBIT** divided by capital
  employed, which is the beginning and end-of-year average of the sum of property, plant and
  equipment, net; trade working capital ...; **goodwill; intangible assets**, and investments
  in affiliates, adjusted to eliminate noncontrolling interests, **and certain items as
  determined by the Company**."* Impairments are Certain Items, so they do not reduce the
  numerator -- **and they DO reduce the denominator, because goodwill and intangibles sit in
  it.** Mechanically, writing off $2.7bn of the acquisition raises the metric that pays
  management. Whether that has ever mattered to a payout is not established here and is not
  claimed. **[E4-34]**'s auditor's-eye test is the place this belongs, and the answer to its
  fourth question is not in the filings.
- [ ] filed-figure tells **[E4-30]** — reported growth is the opposite of unnaturally smooth
  (OCF 1,899 / 966 / 1,146). Cash taxes are not falling as a share of pretax income in a way
  that fires; the FY2025 effective rate of 7.4% against FY2024's (49.8)% is explained line by
  line in Note 15 by non-deductible goodwill impairment and valuation allowances.
- [x] **[E2-57], the except-for flag.** *"Certain Items totaling $1.6 billion"* in 2025 and
  $1.7bn in 2024 are excluded from the headline earnings figure. **[E3-53]** and **[E5-33]**
  are the rule: *"to tell owners year after year, 'Don't count this' ... is misleading"*, and
  charges of this kind belong in the owner-earnings mean. They are in it, below.

### A corporate conduct record, dated to when it became public

**July 2020 — a European Commission competition-law settlement.** FY2025 10-K, verbatim:
*"in July 2020 we settled a European Commission competition law investigation involving
certain of our subsidiaries and three other companies related to certain past ethylene
purchases. Shell Chemicals Europe, certain Repsol entities ..., TotalEnergies, OMV, Borealis,
LyondellBasell, and more recently, Stichting, on behalf of Versalis entities, have each filed
separate claims for damages ... BASF, Dow, ExxonMobil, BP, MOL Group and Braskem have filed
similar claims against Celanese in the Court of Munich, Germany ... **In sum, 11 new claims
were filed against Celanese and other ethylene purchasers in 2025 and early 2026**."*

**This is the second run in this project to reach a Q3 resting on the COMPANY's own record
rather than on named people's conduct** (the first was UMC, 2026-09-13, whose question the
operator has not yet answered). It is recorded here with no verdict attached, because the
file closed at Q2 and because the question UMC raised is still open. **[E5-16]**'s binary is
about *personal* misconduct and the passage does not on its face reach a corporate
settlement; **[E5-22]** is the warning against reading a penalty's size as its seriousness,
in either direction. **A future run on this name must resolve that question before scoring
Q3, and this is the artifact: the 2020 settlement decision and the damages docket.**

### [E2-01]'s primary test, run and then scoped

Net earnings attributable to Celanese over Celanese shareholders' equity: **40.4% (2018),
34.0%, 56.3%, 45.1%, 33.6%, 27.5% (2023), (30.1)% (2024), (28.8)% (2025)**. **That series is
not usable as stated and [E2-47] says why**: the test excludes *"unusual debt-equity
ratios"*, and a $4.0bn book equity carrying $12.6bn of debt produces a ROE that measures the
gearing and not the operators. **[E2-43]**'s denominator -- unleveraged net tangible assets,
with the goodwill wedge reported separately -- is the one used at Q2 above: **9.3% on the
tangible assets, 5.5% on the capital actually committed.**

### The half-owner test [E2-26]

**Mixed, and worth stating on both sides.** *For*: the segment note is detailed; the
volume/price/currency decomposition is published every quarter and is the most honest thing
in the filing; the goodwill note names the cause of its own impairment against the company's
interest (*"the projected cash flows of the engineered materials reporting unit **had not
declined** from the projections used in the December 31, 2024 quantitative analysis"*); the
immaterial revision was voluntary; the dividend cut and the buyback pause are stated plainly
in Item 5 with the consequence attached (*"Any further reduction or elimination of our
dividends could adversely affect the price of our common stock"*). *Against*: the release
that opens with a $10.44 GAAP loss per share and a 20% "operating EBITDA margin" in adjacent
clauses is not telling me what I would want to know if the positions were reversed. **The
10-K is candid; the 8-K is promotional.** That is precisely the CGNX pattern, found again.

---
## Q4 — WHAT THE FILINGS SHOW ABOUT SURVIVAL *(no verdict)*

### Owner earnings — the arithmetic, with the (c) judgment disclosed

**COMPUTATION — NOT A CLEARANCE.**

Convention: mean of (operating cash flow less stock-based compensation) less the (c) guess
**[E2-23]**. All inputs from the filed consolidated statements of cash flows.

**(c) IS A DISCLOSED JUDGMENT AND THE CORPUS DEFAULT IS WRONG HERE IN BOTH DIRECTIONS.**
- **[E3-44]**'s default is depreciation, and the same passage says *"reported earnings plus
  **amortization of intangibles** usually gives a pretty good indication of earning power"* --
  so the intangible amortisation created by the M&M purchase ($164M, $159M, $164M in 2023-25,
  and $158M a year scheduled through 2030) is **not** a renewal cost of plant and does not
  belong in (c). The full-D&A end of the band therefore overstates (c).
- **And the capex end understates it, on the filing's own numbers.** Capex has run **$568M →
  $435M → $343M → $256M annualised (H1 2026)** while depreciation-only has run about **$575M →
  $664M → $622M**. **Capex is at 55% of depreciation and falling**, at a company with 51
  production facilities. **[E5-20]**'s exception class is *"anything whose own filing says
  depreciation understates renewal"*; here the filing shows the opposite arithmetic and the
  same conclusion -- **the current capex number is a deleveraging decision, not a maintenance
  estimate.** [E2-60] names what that is: spending below renewal to fund a payout or a
  repayment is (c) understated.
- **My disclosed guess: (c) = depreciation excluding intangible amortisation, a three-year
  mean of $620M.** Stated as a guess because *"(c) must be a guess"* **[E2-23]**. Both band
  ends are shown anyway, because the band is the display of the guess and not two equally
  legitimate answers.

**Short window, FY2023-FY2025** (the only window in which the perimeter is constant):

| | FY2023 | FY2024 | FY2025 | mean |
|---|---|---|---|---|
| operating cash flow | 1,899 | 966 | 1,146 | **1,337** |
| less stock-based compensation **[E5-06]** | (40) | (32) | (24) | **(32)** |
| = cash before (c) | 1,859 | 934 | 1,122 | **1,305** |
| (c) at total capex | | | | (449) → **OE 856** |
| **(c) at depreciation ex-intangible amortisation — the disclosed guess** | | | | **(620) → OE 685** |
| (c) at full D&A | | | | (783) → **OE 522** |

**Long window, FY2021-FY2025** (five years, the corpus default **[E2-42]**, but **the
perimeter is not constant** -- 2021 and 2022 are a different, unlevered company):
mean OCF $1,517M, less mean SBC $50M = $1,467M; (c) at capex $471M → **OE 996**; (c) at full
D&A $636M → **OE 831**.

**A third construction, because one year in the short window is a working-capital
liquidation.** The FY2023 release: *"Reduced working capital balances by $579 million, driven
by a $451 million reduction in inventory."* The filed changes in operating assets and
liabilities contributed **+$538M (2023), −$181M (2024), +$235M (2025)**. Neutralised, cash
before (c) is $1,108M and, at the disclosed (c), **OE = $487M**. **[E4-41]** requires
favourable exogenous breaks to be named and removed before the mean is trusted; a shrinking
business releasing working capital is not repeatable earnings.

**THE COMBINED RANGE [E4-25]: owner earnings of roughly $330M to $1,000M**, a **threefold**
spread across two windows and three treatments of (c). On the re-struck cap of $4,984M that
is **6.5% to 20.0%**. *"Usually, the range must be so wide that no useful conclusion can be
reached."* **It is that wide, and the width is itself the Q4 finding [E5-11]** -- and it is
**not** the benign kind **[E3-55]** allows, because the uncertainty is about the *level*, not
about a certain mechanism bouncing year to year.

### Great, good, or gruesome? **[E4-20]**

Not gruesome by the definition -- it does not grow rapidly while consuming capital; it is not
growing at all. It is the **good** class degraded to its boundary. **[E5-40]** is the test
that decides it: *"cash-consuming businesses, by their nature, are unattractive unless the
cash they consume gets to earn a reasonable return."* The $11.7bn consumed in 2021-22 has so
far earned a return management has written down by $3.2bn, and the capital actually committed
earns **5.5%** against a 5.34% sovereign.

### Staying power — all three, scored **[E5-11]**

1. **A large and reliable stream of earnings — LARGE, NOT RELIABLE.** OCF $1,899M → $966M →
   $1,146M, and **$285M in H1 2026 against $447M in H1 2025**. Segment operating profit in the
   Acetyl Chain: $1,105M → $946M → $539M.
2. **Massive liquid assets — ADEQUATE, NOT MASSIVE.** Cash $1,364M at 2026-06-30, plus
   $1,750M undrawn under the U.S. Revolving Credit Facility and $50M in China. **$3.1bn of
   liquidity against $12.0bn of debt.** **[E5-39]** is the standard and it is not met: *"We
   will never be dependent on the kindness of strangers"* -- $1,750M of that liquidity is a
   bank line, which is exactly what the passage refuses to count.
3. **No significant near-term cash requirements — FAILS, and this is *"the one that usually
   kills."*** Principal payments scheduled, from the filed Note 11: **2026 $1,204M · 2027
   $1,357M · 2028 $1,564M · 2029 $1,356M · 2030 $1,800M · thereafter $5,423M · total
   $12,704M.** **$7,281M falls due inside five years** against owner earnings this run puts at
   $330M-$1,000M a year. Plus an accounts-receivable purchasing facility under which **$1.5bn
   a year of receivables are sold and derecognised**, whose term ran only *"until June 17,
   2026"* before the June 2025 amendment extended it -- an annually renewed, off-balance-sheet
   funding line. **[E3-52]** says read the terms and not just the quantity: none of this is
   the covenant-free, long-dated, customer-prepaid kind. It is covenanted bank and bond debt
   with dates on it.

**Leverage, named and quantified** (there is no ratio ceiling in this framework and the
corpus supplies none **[E4-16, E3-29]**): total debt $12,007M, net debt $10,643M, book equity
$4,588M, market cap $4,984M, interest expense $701M in FY2025 and **$369M in H1 2026 alone**,
annualising to roughly $740M and rising.

**Why it is rising, from the filed debt note.** *"In November 2024, S&P Global Ratings
downgraded the Company's credit rating and on February 12, 2025, Moody's Ratings downgraded
the Company's credit rating, which together had the effect of increasing interest rates by 50
basis points on certain senior unsecured notes ... On November 17, 2025, S&P Global Ratings
downgraded the Company's credit rating and on November 25, 2025, Moody's Ratings downgraded
the Company's credit rating, which together will have the effect of increasing interest rates
for certain senior unsecured notes by an additional 50 basis points."* **Four downgrades in
thirteen months and 100bp of contractual step-ups.** And the refinancing arithmetic is on the
same page: the December 2025 offering issued **$600M at 7.000% and $800M at 7.375%** to
retire notes tendered at 2027 and 2028 maturities, while the legacy euro notes still on the
books carry **0.625% and 2.125%**. **Every roll from here re-prices low-coupon debt at 6.5%
to 7.4%.**

### [E2-54]'s coverage test, computed

*"whenever someone creates a capital structure that does not allow all interest, both payable
and accrued, to be comfortably met out of current cash flow net of ample capital expenditures
-- zip up your wallet."*

| | FY2025 | H1 2026 annualised |
|---|---|---|
| operating cash flow | 1,146 | 570 |
| add back interest (already deducted in OCF) | ~690 | ~740 |
| = cash flow before interest | 1,836 | 1,310 |
| less **ample** capital expenditure (at depreciation, $620M, not the $343M spent) | (620) | (620) |
| = available for interest | **1,216** | **690** |
| interest | (701) | (740) |
| **cover** | **1.7x** | **0.93x** |

**On the most recent half-year, annualised, and charging maintenance capex at depreciation
rather than at the reduced spend, the business does not cover its own interest.** It covers
it on the reported capex number (1.6x) and it covered it comfortably in FY2023. The gap
between those two answers is the whole question.

### Name the specific way THIS business dies **[E2-27, E3-24]**

**The mechanism.** Not a single event. It is **[E2-27]**'s collective-irrationality loop
running through a levered balance sheet: *"Viewed individually, each company's capital
investment decision appeared cost-effective and rational; viewed collectively, the decisions
neutralized each other ... After each round of investment, all the players had more money in
the game and returns remained anemic."* Eight named acetyls producers each add low-cost
capacity because each has the lowest cost; acetic acid and VAM prices stay at the
supply-ample end of **[E2-58]**'s ratio for longer than one refinancing cycle; Engineered
Materials volumes keep falling at 3-6% a year as its automotive end market contracts;
Celanese meets $1.2bn-$1.8bn of maturities every year by refinancing at 7% instead of 2%;
interest passes $800M; the 5.50:1.00 covenant that was amended in 2024, in 2025 and again in
July 2026 is amended a fourth time or is not; and the equity, which is 32% of the enterprise,
absorbs the whole of it.

**Quantified from filed figures.** Consider some mathematics, in the corpus's own form
**[E3-24]**. The enterprise is worth roughly $15.6bn at today's prices ($4,984M of equity plus
$10,643M of net debt). **A 15% permanent fall in enterprise value takes $2.3bn, which is 47%
of the equity.** Conversely, since owner earnings before interest are roughly $1.2bn-$1.5bn
and interest is $740M and rising, **a further 300bp of refinancing cost on the $7.3bn
maturing inside five years adds about $220M a year**, which is between a fifth and two-thirds
of every owner-earnings estimate in the range above. **And the covenant is the tripwire**: at
5.50:1.00 on net debt of $10.6bn, the covenant EBITDA floor is about **$1.93bn**, against a
2025 "operating EBITDA" of $1.9bn as the company itself computes it. **The amendment was
granted because the existing covenant was about to be breached.**

**Likelihood: [x] a real possibility.** Not *likely* -- there is $1.36bn of cash, $1.75bn of
undrawn revolver, no maturity wall in any single year, a lender group that has amended three
times, and the Acetyl Chain priced **+18% year on year in Q2 2026**, which is the up-leg of
the same cycle that caused the problem. Not *a low-level possibility* either -- four rating
downgrades, three covenant amendments, a 95% dividend cut, a paused buyback, capex at 55% of
depreciation, and asset sales ($493M in H1 2026) are what a balance sheet under pressure
looks like while it is still working.

**[E4-40], modelling exposure rather than experience.** The temptation is to read the +18%
Acetyl price in Q2 2026 and the *"highest adjusted earnings per share in nearly three years"*
as the answer. *"all of us in the industry made a fundamental underwriting mistake by focusing
on experience, rather than exposure."* The exposure is the maturity schedule and the covenant,
and neither improved in Q2.

**[E4-51], the arguments against my position, stated better than the opposition would.** The
bear case above can be answered: a cyclical trough in chemicals is the historically correct
time to own the low-cost producer; the $3.2bn of write-downs are non-cash and the filing says
the cash-flow projections did **not** decline; the company generated $773M of free cash flow
by its own definition in a trough year and has repaid $591M of debt in H1 2026; Engineered
Materials operating profit ran at a $600M annual rate ex-charges through the worst of it; and
the equity at $45 is 32% of an enterprise whose replacement cost is far higher. **All of that
is true and none of it repairs Q2.** [E2-38]: *"Good jockeys will do well on good horses, but
not on broken-down nags"*, and the Q2 finding is that the horse's relative position fell from
second to sixth inside its own category in the three years the cost advantage should have
been paying.

---
## Q5 — **COMPUTATION — NOT A CLEARANCE**

⛔ **Q5 does not open.** Q2 returned OUT. No entry language appears below, no box is ticked,
no band is armed and no `PORTFOLIO.md` row is written. **The arithmetic is recorded only so
that a future reader can see what the screen's row was measuring.**

- owner earnings, this run's range: **$330M to $1,000M** · re-struck cap **$4,984M**
  → **6.5% to 20.0%** · sovereign **5.34%** (USD, 2026-09-18, US Treasury).
- **The screen's `yield_bottom` of 10.71% reproduces almost exactly** -- it is $521M over
  $4,861M -- and this run's equivalent construction ($522M at full D&A over $4,984M) gives
  **10.5%.** The screen's arithmetic was right. **What it could not see is that the same
  business, on a window whose perimeter is constant and with the working-capital release
  removed and maintenance charged at depreciation, produces $487M, and that the denominator
  of the real question is not the equity.**
- **`growth_required = -0.0071` reproduces and the brief's question about it has an answer.**
  A price that clears the sovereign with no growth is what a **trough earnings base on a
  levered cyclical** looks like when the market disagrees with the base. The numerator here is
  measuring **neither a mid-cycle nor a peak**: FY2023 was the peak (post-acquisition revenue,
  a $579M working-capital release, a $505M disposal gain, $1.9bn of OCF) and FY2025 is near
  the trough. A three-year mean that straddles them is a blend, and the -0.71% growth
  requirement is the arithmetic consequence of dividing a blend by a price that has already
  fallen 74%.
- **The brief's prior that the debt destroys the screen's yield is recorded as WRONG**, for
  the reason given at Step 0 flag (v): operating cash flow is already net of interest, so the
  levered numerator belongs against the levered denominator, and putting it against enterprise
  value would count the debt twice. **The debt is fatal at Q4, not at Q5.**
- No bar is chosen. No margin of safety is applied. **[E4-28]**'s floor is not adjudicated,
  because a floor verdict on a name that failed Q2 would be a category error (the QLYS
  ruling).

---
## Q6 — THE REVERSAL CONDITION, IN WORDS *(no verdict, no bands, no alert)*

**No price alert is armed and no `PORTFOLIO.md` row is written.** This name failed on the
**business**, and a price alert on a business failure is the category error the QLYS ruling
names. What is recorded instead is the condition under which the Q2 finding would deserve
re-examination -- pre-committed now, before any future run, per **[E1-02]**:

**The Q2 OUT rests on two relative facts. It would be reversed only by their reversal, both
of them, over multiple years:**
1. **The price-and-volume decomposition turns positive on VOLUME in Engineered Materials for
   four consecutive quarters**, not on price. EM volume has printed (5), (4), (3) and (6) in
   the last three annual periods and the most recent quarter. **[E4-55]**: the physical series
   is the honest one, and a price-led recovery is the thing that hides a shrinking franchise.
2. **Celanese's ROCE, on the same EBIT-over-capital-employed definition used in the competitor
   row above, returns to the top two of that row of eight for three consecutive years.** The
   claim under test is a cost advantage *"both wide and sustainable"* **[E2-58]**, and only a
   sustained relative position can evidence it.

**Neither is a price condition, and that is deliberate.** **[E4-17]**: *"we sell -- really
when we ... reevaluat[e] the economic characteristics of the business ... And those beliefs
change quite gradually."* The re-examination date is the FY2026 10-K, expected February 2027,
which will carry the fourth annual volume/price decomposition and the covenant's first test
at 5.50:1.00 for the quarter ending 2027-03-31.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, file closed. Q3-Q6
      recorded **without verdicts**, headed as such.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the
      only IN and its one caveat (a complex multinational) is answered from [E4-46], not
      deferred.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives — **none used.**
- [x] Every UNKNOWABLE verdict states what cannot be known — **none used.** The Q2 close is
      OUT on filed evidence and the reason it is not UNKNOWABLE is written into the verdict.
- [x] Step 0: the filing was read, with accession numbers; two figures were cross-checked
      against the filed statements (FY2022 acquisitions line; FY2025 operating cash flow).
- [x] Owner earnings on a multi-year mean; **two windows plus a working-capital-neutral
      third**; capex band disclosed as a judgment with the corpus default explicitly
      **rejected in both directions** and the reason cited from the filing.
- [x] Competitor row filled — seven SEC registrants, one metric, one window, each from the
      named filer's own 10-K XBRL; the industry census taken from Eastman's own 10-K; the
      non-SEC competitors named and their absence argued to be non-load-bearing.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated — **and the
      currency choice is argued rather than assumed, with its limit disclosed.**
- [x] Value stated as a round-number range, not a point estimate — and headed
      **COMPUTATION — NOT A CLEARANCE**, with no entry language and no box ticked.
- [x] One bar chosen, not both — **neither bar used**, because Q5 did not open. Windage count:
      **one**, spent at (c), and stated.
- [x] Prices dated; aggregator used for the live quote only and flagged; raw responses saved.
- [x] Run committed to git, with a pathspec, after Q1 and after Q2.

## REGISTER
- Verdict: **[x] OUT (about the business)** — at **Q2**.
- **One line:** Celanese sells a commodity (Acetyl Chain, 43.5% of sales, priced off industry
  utilisation by the filer's own account, price -17%/-6%/-6% then +18% in one quarter) and a
  specification polymer business (Engineered Materials) that cut price in three consecutive
  years while losing volume in three consecutive years, so **[E3-03]** criterion 2 fails in
  both halves; the only escape **[E2-58]** allows, a cost advantage *"both wide and
  sustainable"*, is refuted by the competitor row, where Celanese's ROCE ranks second of eight
  over FY2018-FY2025 and **sixth of eight over FY2023-FY2025**, the three years since it paid
  $11.7bn for the advantage it has since written down by $3.2bn.
- **Recorded below the close, without verdicts:** [E2-49] metric-switching fires with a dated
  quotation (Adjusted EBIT replaced by Adjusted EBITDA for the 2023 plan year, the first after
  an acquisition that took D&A from $462M to $801M); [E4-29] fires at full strength in the
  8-Ks and is the primary pay metric; three covenant amendments (2024, 2025, July 2026, the
  last raising consolidated net leverage to 5.50:1.00); four rating downgrades in thirteen
  months worth 100bp of contractual step-ups; $7.3bn of debt maturing inside five years; and
  a 2020 European Commission competition settlement with 11 new damages claims in 2025-26,
  which is the second corporate-record Q3 this project has met and which the operator's open
  UMC question still governs.
