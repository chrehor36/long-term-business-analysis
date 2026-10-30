# Company Run - SUPERIOR GROUP OF COMPANIES, INC. (SGC) - 2026-09-21

**WAVE 7, name 21 of 218. Branch B: no prior SGC run file exists in `Test Runs/` of any vintage.**
Unattended overnight cycle 2026-09-21_0946. Research folder: `Test Runs/_research 2026-09-21 SGC/`.

**THE SCREEN ROW - verbatim, unlabelled, and every field TESTED not inherited.**
Source: `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 45.

```
ticker,name,cap_m,oe_bottom_m,oe_top_m,spread,spread_dollars,cap_flag,deal_note,name_change_note,wc_note,yield_bottom,vs_sovereign,growth_required,level_shift,level_note,best_year_dep,best_year_note,level_shift_oe,level_note_oe,best_year_dep_oe,flags_disagree,level_shift_full,years_filed,window_disagree,acq_note,da_note,spread_caveat,newest_filing,newest_periodic
SGC,"SUPERIOR GROUP OF COMPANIES, INC.",196,13,35,1.784,$13M to $35M,,"1 8-K Item 1.01 filing(s) since 2026-03-03, none carrying a merger agreement (EX-2.1) - most likely a credit facility or offering; open them only if something else is odd.",,,0.0644,0.0109,0.0356,n/a,EARLY HALF STRADDLES ZERO - the pre-window years run from $-,0.229,"ONE YEAR CARRIES THE WINDOW - a tight spread here is arithmetic, not knowledge; re-price on a wi (9-yr OCF series)",n/a,EARLY HALF STRADDLES ZERO - the pre-window years run from $-17.9M to $,0.408,,n/a,16,,"acquisitions are $32M, 16% of cap, inside the window - the numerator and denominator may be different companie",,4-construction width only (3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25],2025-12-31,2026-06-30
```

*(The tail-triage correction of 2026-09-12 binds: every imperative in that row is a prompt to
read, never a score and never a verdict. Four are live and each is tested below.)*

**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** (the newest published print; today 2026-09-21 is a Monday
  and the curve for it had not posted at the time of the strike) · source (issuing authority)
  **US Treasury daily par yield curve, 30-year par yield**, struck fresh this run through
  `tools/sources.py`, which returned `(5.34, '09/18/2026', 'US Treasury daily par yield curve')`.
  **FRED DGS30 was not used; it is the fallback, not the source.** No rate was inherited from
  the dispatch brief, which deliberately supplied none.
- FX: **none needed.** Superior earns in USD. Revenue is sold to US customers in all three
  segments (10-K Item 1: Healthcare Apparel *"sells its products to healthcare laundries,
  dealers, distributors, retailers and consumers primarily in the United States"*; Contact
  Centers *"provides outsourced, nearshore and onshore business process outsourcing, contact and
  call-center support services to North American customers"*). **Note the asymmetry and carry it
  to Q4:** revenue is USD, but **5,800 of 6,520 employees are outside the US** and the cost base
  sits in El Salvador, Belize, the Dominican Republic, Haiti, China, Bangladesh, Vietnam and
  Madagascar. This is a USD-revenue business with a foreign cost base, not a USD business.

**THE PRICE - AGGREGATOR, FLAGGED, LIVE QUOTE ONLY (operator rule 5).**
- **$12.36**, the live quote at **2026-09-21 09:44 ET**, Yahoo Finance chart API via
  `tools/sources.py`. Raw metadata saved to
  `Test Runs/_research 2026-09-21 SGC/price_raw_aggregator.json` (`regularMarketPrice 12.36`,
  `currency USD`, `fullExchangeName NasdaqGM`). The five prior closes read 12.47 / 12.57 / 12.40 /
  12.45 / 12.40, so the quote is not an outlier print. **This is the only number in this file
  that comes from an aggregator.**

**THE SHARE COUNT AND THE CAP - STRUCK BY HAND OFF THE COVER OF THE NEWEST PERIODIC FILING.**
- Cover of the **Form 10-Q for the quarterly period ended June 30, 2026**, filed 2026-08-04,
  **accession 0001437749-26-025511**, verbatim: *"The number of shares of common stock of the
  registrant outstanding as of July 30, 2026 was **15,945,201** shares."*
- **ONE CLASS ONLY**, checked rather than assumed. The FY2025 balance sheet reads *"Preferred
  stock, $.001 par value - authorized 300,000 shares (none issued)"* and *"Common stock, $.001
  par value - authorized 50,000,000 shares, issued and outstanding - 15,730,615 and 16,484,921
  shares, respectively"*. The 10-Q balance sheet reads 15,945,623 issued and outstanding at
  2026-06-30. **The BELFB dual-class cover defect cannot arise here.**
- **Splits after the measurement date: none.** `split_factor_after('SGC','2026-07-30')` returns
  **1.0**. `cap = close(anchor) × shares(measurement) × splits AFTER measurement`
  = 12.36 × 15,945,201 × 1.0 = **$197.1M**, on `close`, never `adjclose`.
- **THE SCREEN'S CAP OF 196 IS RIGHT, and that is the finding.** 196 ÷ 15,945,201 implies
  $12.29 against today's $12.36 - a 0.6% difference, entirely the three-week-stale price. The
  number was reproduced, not adopted. **The cap used everywhere below is the hand-struck $197.1M.**
- **The count is falling, not rising.** 16,484,921 (2023-12-31) → 15,730,615 (2024-12-31) →
  15,945,201 (2026-07-30). Retirement by buyback, partly offset by equity grants. Carried to Q3,
  where **[E5-15]**'s serial-issuance flag is scored.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **Form 10-K for the fiscal year ended December 31, 2025**, filed 2026-03-03,
    **accession 0001437749-26-006653** (`sgc20251231_10k.htm`) - the newest ANNUAL filing, and
    exactly the `newest_filing 2025-12-31` the screen row carries.
  - **Form 10-Q for the quarter ended June 30, 2026**, filed 2026-08-04,
    **accession 0001437749-26-025511** - the newest PERIODIC filing, exactly the screen row's
    `newest_periodic 2026-06-30`. **The screen told me to read it and I read it.**
  - **DEF 14A filed 2026-03-23, accession 0001437749-26-009335** (read at Q3).
  - **8-K of 2026-08-11, accession 0001437749-26-026859**, Items 1.01/1.02/2.03/7.01/9.01 - the
    single Item 1.01 the screen's `deal_note` pointed at. **Opened; see the table below.**
  - **8-K EX-99.1 earnings releases**: Q2 2026, furnished 2026-08-04, accession
    0001437749-26-025507 (`ex_968533.htm`); FY2025/Q4, furnished 2026-03-03, accession
    0001437749-26-006593 (`ex_880700.htm`, `ex_880701.htm`).
- **figures cross-checked against the filed statements - three, by hand, not against XBRL:**
  1. **Shareholders' equity recomputed from A − L** *(the [E5-32] cross-check: Salomon's books
     carried an invented number for twelve audited years, so audited does not mean true)*: total
     assets **$421,844** less total liabilities **$229,026** = **$192,818**, which is the filed
     *"Total shareholders' equity 192,818"* to the dollar.
  2. **FY2025 operating cash flow $19,709 thousand** read off the filed Consolidated Statements
     of Cash Flows, equal to the companyfacts figure used in the series at Q4.
  3. **The segment table reconciles to pretax income**: consolidated gross margin $212,864 less
     consolidated selling and administrative $199,475 = $13,389 of operating profit, less
     interest expense $5,143 = **$8,246**, which is the filed *"Income before income tax
     expense 8,246"*. The same arithmetic on FY2024 gives $20,652 − $6,358 = $14,294, also filed.

**THE SCREEN ROW'S IMPERATIVES - EACH ONE TESTED.** *(The tail-triage correction of 2026-09-12:
every field is a prompt to read, never a score and never a verdict.)*

| screen field | what it said | what the filings say |
|---|---|---|
| `deal_note` | one Item 1.01 since 2026-03-03, *"most likely a credit facility or offering"* | **TESTED; the guess was right and is now a fact with terms.** The 8-K of 2026-08-11 (acc. 0001437749-26-026859) reports an **Amended and Restated Credit Agreement dated 2026-08-07** with PNC: *"a revolving credit facility in the aggregate maximum principal amount of $125 million and a term loan in the aggregate principal amount of $75 million"*, five-year term, SOFR + 1.125%-2.125%, *"secured by substantially all of the operating assets of the Company"*. Item 1.02 terminated the 2022 agreement, under which *"a revolving line of credit … (approximately $29.0 million outstanding balance) plus term loans with an aggregate outstanding balance of approximately $56.25 million"* was repaid. **This is a post-balance-sheet event in no filed statement, and it matters at Q4: the covenants are now named - fixed charge coverage ≥ 1.25:1, net leverage ≤ 4.0:1.** The screen's guess was honestly labelled as one; the *terms* are the news, not the existence. |
| `cap_m 196` | screening cap | **Reproduced at $197.1M** from a hand-struck cover count. Right, for once. |
| `newest_periodic 2026-06-30` | a periodic filing exists beyond the annual date | **Read.** H1 2026 operating cash $17,735k, net income $2,055k, a **$2.6M tradename impairment in Healthcare Apparel**, and the new credit agreement in the subsequent-events note. |
| `acq_note` $32M, 16% of cap | perimeter warning | **Established at Q4.** Acquisition cash inside the 5-year window is $16.4M (2021) + $11.2M (2022) + $4.0M (2024) = **$31.6M**, the screen's $32M, and **16.0% of the $197.1M cap**. Over the full 16-year filed series it is **$172.9M**, which is **88% of today's market capitalisation**. The perimeter problem is far larger than the 5-year window can show - which is the screen flag's own point, made bigger by the rebuild it also ordered. |
| `spread_caveat` - an [E4-25] rebuild ordered | the 4-construction width cannot see past 5 years | **Rebuilt to 16 years at Q4, from the filings.** The rebuild moves the answer materially and is the single most consequential piece of arithmetic in this file. |
| `best_year_note` ONE YEAR CARRIES THE WINDOW | on a 9-year OCF series | **Confirmed and named**: FY2023 operating cash of **$78.9M** against a 16-year median near $17M, and the cause is in the filed cash-flow detail - a **$24.7M inventory release** unwinding the $24.5M (2021) and $15.9M (2022) builds. It is a balance-sheet unwind, not earnings. |
| `level_note` / `level_note_oe` EARLY HALF STRADDLES ZERO | the guard refused to print a ratio | **A refusal, not a finding, and now resolved by reading.** **FY2011 operating cash was −$0.9M** and **FY2022 operating cash was −$2.6M** (owner earnings −$17.9M, the figure the truncated screen string was reaching for). Two negative operating-cash years in sixteen, one of them inside the current window. |
| `wc_note` **empty** | the flag reads ANNUAL facts only (its docstring) | **Checked by hand in the 10-Q, as the docstring requires.** H1 2026 working-capital lines: accounts receivable +$9,115k, contract assets −$8,185k, inventories +$2,386k, prepaid −$568k, other assets −$2,453k, accounts payable and other current liabilities −$4,503k, other long-term +$1,108k - **a net drag of about $3.1M on $17.7M of operating cash.** No half-year prepayment of the INOD kind. The empty flag is correct for this filer this half; it was verified, not inherited. |

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, no management language.** Superior is a **holding company over
  three unrelated sourcing-and-labour spreads**, with almost no owned production:

  1. **Branded Products (64% of FY2025 sales, $361.1M).** A promotional-merchandise and branded-
     uniform **broker**. A corporate customer wants 40,000 branded jackets or a gift-with-purchase
     item; Superior designs it, places the order with a third-party factory in Asia, imports it,
     warehouses it and ships it. The line is `units × (price to customer − landed cost of goods)`
     less the cost of the salespeople who won the programme. Landed cost includes tariff. Gross
     margin **34.3%** in FY2025; selling and administrative **26.6%** of sales; **segment
     operating margin 7.66%** ($27.6M on $361.1M, computed here from the filed segment table).
  2. **Healthcare Apparel (20%, $115.9M).** The same spread against a different buyer: scrubs, lab
     coats and patient gowns under Wink, Fashion Seal Healthcare, CID Resources and a licensed
     Carhartt Medical name, made by third parties or in Superior's own Haitian plants and sold to
     hospital laundries, distributors, retailers and consumers. Gross margin **36.2%**; S&A
     **34.1%** of sales; **segment operating margin 2.08%** ($2.4M on $115.9M).
  3. **Contact Centers (16%, $92.5M).** Not apparel at all. Superior hires bilingual agents in El
     Salvador, Belize and the Dominican Republic and rents their hours to North American
     companies. The line is `seats × utilisation × (bill rate − fully loaded wage)`; cost of goods
     sold here *is* agent payroll (10-K: *"Cost of goods sold for our Contact Centers segment
     includes salaries and payroll related benefits for agents"*). Gross margin **52.9%**; S&A
     **45.8%** of sales; **segment operating margin 7.13%** ($6.6M on $92.5M).

  Above the three sits a corporate centre that consumed **$23.3M** of selling and administrative
  expense in FY2025 (the "Other" column of the filed segment table). **That is the single most
  important fact about how this makes money: the three segments earn $36.6M of operating profit
  between them and the holding company keeps $13.4M of it**, before $5.1M of interest - a
  consolidated operating margin of **2.36%** on $566.2M of sales.

- **The scarce input this business controls.** Asked honestly, **the filings evidence none.** The
  candidates, and what the filing itself does to each:
  - *The factories*: not owned except in Haiti, and the 10-K names the redundancy as the point -
    *"The Company believes that its vast redundant network of suppliers, including its own
    manufacturing facilities in Haiti, provide sufficient capacity to mitigate most dependency
    risks on a single supplier."* A redundant network is by construction not scarce.
  - *The raw materials*: *"The majority of such fabrics are sourced in China"*, and for Branded
    Products, *"The Branded Products segment has flexibility in its suppliers, as other suppliers
    of the same or similar products are widely available."* Superior states its own input is
    commoditised.
  - *The agents*: Central American labour, hired against every other nearshore operator.
  - *The brands*: Wink and Fashion Seal Healthcare are real registered marks and the 10-K calls
    them *"critically important to the marketing and operation of Superior's Healthcare Apparel
    segment"* - but a **$2.6M tradename impairment was taken in that very segment in Q2 2026**,
    which is the filing marking its own brand value down.

  The honest answer is **customer relationships and programme incumbency** - the switching
  friction of a uniform or merchandise programme already running across a customer's estate. That
  is real and it is not nothing. Whether it is *scarce* is Q2's question, not Q1's, and Q1 does not
  borrow it.

- **Will the fundamentals look broadly the same in ten years?** **Yes, and that is not a
  compliment.** Nothing here is a technology. People will still wear scrubs and branded polos in
  2036, corporates will still buy promotional merchandise, and somebody will still answer the
  phone. The business's shape in 2036 will be what it was in 2010 and is now: buy from Asia and
  Central America, sell to America, keep the spread. The two things that can change the arithmetic
  - tariff regimes and where cheap labour is - are exogenous and are already moving (the 10-K
  records the IEEPA tariffs invalidated by the Supreme Court on 2026-02-20, a replacement 10%
  Section 122 tariff from 2026-02-24, and AGOA/HOPE/HELP preferences extended only to **December
  2026**). Those change the *level*, not the *mechanism*, and Q1 asks about the mechanism.

- **Is Q1 answerable consolidated, or only segment by segment?** *(The brief asked; the filings
  answer.)* **Consolidated, and the consolidated answer is the framework's answer.** All three
  segments are the same species of business - buy an input at a price you do not set, sell it at a
  price you do not set, live on the difference, with no owned scarce asset in between. Each one's
  arithmetic fits on one line and the lines add. This is not the ORCL/ARM class where a leg is
  opaque, and it is not the HHH/RGTI class where the filed history is too short: **sixteen years of
  annual data are on file and were rebuilt this session.** The difficulty here is not understanding
  the business; it is that understanding it tells you the advantage may not be there - and that is
  Q2's verdict to reach, not Q1's.

- **VERDICT: [x] IN**
  *Simple and stable in character **[E3-31]**; the unit economics of all three legs are written
  above without management's language; no degree-of-difficulty credit was needed **[E4-18]**; and
  no part of this verdict rests on a document I have not opened.*

## Q2 - IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** · **no close substitute [ ]** · **not price-regulated [x]**

**Criterion 1 passes easily.** Hospitals need scrubs and patient gowns; corporate customers want
branded merchandise; North American companies want cheaper phone support. None of that is in
doubt.

**Criterion 3 passes on its face.** No segment is price-regulated. But the corpus's point in
[E3-03] is that regulation *caps* a franchise **[E2-59]**; the absence of a cap says nothing
about whether there is a franchise to cap.

**Criterion 2 fails, and it fails on the registrant's own filed words, not on my reading.**
Superior's own 10-K describes each of its three markets as crowded and substitutable:

> *"Superior competes in its Branded Products segment with **a multitude of national and
> regional companies** … Superior also competes with **local firms in most major metropolitan
> areas.**"* - FY2025 10-K, Item 1, Competition

> *"The market in which our Contact Centers segment operates has evolved into a global
> multi-billion dollar marketplace that is **highly competitive and fragmented.** … TOG also
> competes with local entities in other offshore locations."* - same section

> *"**Nearshore operators can provide comparable service to their U.S. counterparts at a fraction
> of the price.**"* - FY2025 10-K, Item 7, Business Outlook

> *"The Branded Products segment has **flexibility in its suppliers, as other suppliers of the
> same or similar products are widely available.** Additionally, the nature of the promotional
> products industry is such that … it is possible that **alternative products using different
> materials could be utilized for similar promotional activities.**"* - Item 1, Raw Materials

And the company says it to the market in its own press release: *"Superior Group of Companies is
comprised of three attractive business segments each serving **large, fragmented and growing
addressable markets**"* (EX-99.1 furnished 2026-08-04, accession 0001437749-26-025507).
**"Fragmented" is the registrant's own word for all three of its markets.** A product whose
supplier network is deliberately redundant, whose materials are widely available, whose physical
form can be substituted, and whose service rivals provide *"comparable service … at a fraction of
the price"*, is the definition of a product with close substitutes.

- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]**
  **[E4-04] does not decide this file and is not used to.** *(Ruled 2026-09-20: [E4-04] is applied
  as a competence limit, never as a fourth franchise criterion, and a name whose durability cannot
  be judged from filings closes UNKNOWABLE at Q2, not OUT.)* Superior is not a rapid-change
  industry and not a depleting asset; nothing here is *"far beyond our perimeter"* **[E4-58]**.
  The durability question **is** judgeable from these filings, and the filings answer it. The file
  closes on **[E3-03] criterion 2**, which is a finding about the business, with the evidence in
  hand - the OUT branch of the four verdicts, not the perimeter close.

- **Primary moat metric, filing-sourced, and its trend.** Gross margin rate, which for a sourcing
  spread is the moat made arithmetic, and it is falling in **all three** segments at once:

| gross margin rate | FY2022 | FY2023 | FY2024 | FY2025 | direction |
|---|---|---|---|---|---|
| Branded Products | 29.6% | 33.5% | 35.3% | **34.3%** | down |
| Healthcare Apparel | 28.8% | 37.1% | 38.4% | **36.2%** | down |
| Contact Centers | 59.1% | 53.7% | 53.8% | **52.9%** | down |
| **consolidated** | 33.4% | 37.5% | **39.0%** | **37.6%** | **down** |

*(Computed this session from the filed segment tables in the FY2022 10-K (acc.
0001437749-23-007261), the FY2023 10-K (acc. 0001437749-24-007685) and the FY2025 10-K (acc.
0001437749-26-006653): segment gross margin ÷ segment net sales. The FY2025 MD&A states the
consolidated figures itself - "Gross margin rate for the Company was 37.6% for the year ended
December 31, 2025 down from 39.0%" - and the segment rates as well; my arithmetic agrees with
each.)*

  **And the MD&A names the cause, which is the moat test [E4-37] answered in the filing's own
  words:** the FY2025 decline was *"primarily due to **higher product costs**"* in Branded
  Products and *"primarily due to **higher product costs in 2025** and unfavorable sales product
  mix"* in Healthcare Apparel. **Costs rose and the price did not follow.** The 10-K states the
  mechanism in advance as a risk: *"if cost increases **cannot be entirely passed on to customers**
  and alternative suppliers or suitable product alternatives are unavailable, profit margins could
  decline."* That is agony-pricing, not yawn-pricing **[E4-37]**: *"it's not a great business when
  you have to have a prayer session before you raise your prices a penny."* Superior did not even
  get to the prayer session; the margin simply went.

- **[E2-44], the two-characteristic test, both answered from filed figures.**
  1. *Can it raise prices even when demand is flat and capacity is not fully utilised?* **No.**
     FY2025 is exactly that year - consolidated sales flat at +0.1%, three segments' gross margins
     all down on higher input cost.
  2. *Can it grow dollar volume with only minor additional investment of capital?* **No.**
     Consolidated net sales were $578.8M (2022), $543.3M (2023), $565.7M (2024), $566.2M (2025):
     **down 2.2% over three years**, and the only growth line in FY2025 was bought - *"The increase
     was primarily due to an additional **$11.0 million in net sales attributable to 3 Point
     branding company we acquired in December 2024.** This increase was partially offset by **a net
     volume decrease within existing large enterprise accounts.**"* Organic volume went backwards;
     an acquisition covered it.

- **[E4-55], the physical series, where units exist.** Apparel units are not disclosed. The one
  physical series the filings do give is the Contact Centers labour force, and it is shrinking:
  **approximately 4,300 full-time employees at 2022-12-31 and again at 2023-12-31, and
  approximately 3,900 at 2025-12-31** (Item 1, Human Capital Resources, in each 10-K) - a 9.3%
  decline in the physical unit. Segment revenue over the same span went $84.2M → $91.5M → $92.5M,
  so revenue per agent rose while the agent count fell; the MD&A gives the reason and it is not a
  good one: *"continued macroeconomic headwinds, which continue to contribute to **client
  downsizing and customer attrition outpacing new customer acquisitions**."* The dollar line was
  held up while the physical line went down - precisely the shape [E4-55] says is how a shrinking
  position hides.

- **[E3-46], the number asked about the business before the manager.** Return on capital employed
  (EBIT ÷ (total assets − total current liabilities)), computed here for ten years from the filed
  balance sheets and the filed income statements:

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| EBIT $M | 20.6 | 25.6 | 24.6 | 19.7 | 53.5 | 34.3 | −33.1 | 19.5 | 20.7 | **13.4** |
| ROCE % | 12.5 | 14.4 | 8.5 | 6.8 | 18.5 | 9.6 | −8.9 | 6.1 | 6.6 | **4.3** |

  **The best years are the oldest and the 2020 pandemic spike; the trend since is down to 4.3%.**
  A business earning 4.3% on capital employed is not what *"the best businesses, by definition"*
  **[E3-46]** look like.

- **[E2-58], the commodity doctrine, and it fits this filer.** *"persistent over-capacity without
  administered prices (or costs) equals poor profitability"*, with **one** exception - *"a cost
  advantage that is both **wide and sustainable** … By definition such exceptions are few."* Ask
  whether Superior holds that exception and the filings say no: it buys from the same third-party
  Asian factories its rivals buy from (*"other suppliers of the same or similar products are
  widely available"*), and its stated supply-chain advantage is *redundancy*, not cost - *"its
  vast redundant network of suppliers"*. In Contact Centers it hires the same Central American
  labour pool as every other nearshore operator, and it closed its Jamaica site in June 2025. **And
  [E3-62]'s second step lands on the tariff:** when landed cost moves, does the saving or the cost
  stay home or flow through? FY2025 answers it - the cost flowed *in* and the margin absorbed it.
  In a commodity business the gains go to the buyer, and here so did the losses.

**THE COMPETITOR ROW - required [E3-28].** A moat is a claim about *relative* position.

**Specification, stated before the numbers** *(this is the row's honesty condition)*: for each
company, **the most recent fiscal year on file**, **operating margin = operating income ÷
revenue**, and **ROCE = operating income ÷ (total assets − total current liabilities)**, every
figure taken from that company's own **SEC annual filing** via its XBRL companyfacts (tags
`OperatingIncomeLoss`, `Assets`, `LiabilitiesCurrent`, and the revenue tag the filer uses) and
**every ratio computed in this session**, not quoted from anywhere. Fiscal year ends differ and
are shown, because pretending they align would be a worse error than naming them.

| Company | segment it rivals | FY end | revenue $M | operating margin | ROCE | source |
|---|---|---|---|---|---|---|
| **SUPERIOR GROUP (SGC)** | - | 2025-12-31 | **566.2** | **2.36%** | **4.27%** | 10-K acc. 0001437749-26-006653, segment table recomputed |
| Cimpress plc (CMPR) | Branded Products | 2026-06-30 | 3,736.6 | 6.72% | 17.59% | 10-K, companyfacts |
| Lands' End (LE) | Branded Products / uniforms | 2026-01-30 | 1,335.1 | 3.32% | 8.40% | 10-K, companyfacts |
| FIGS, Inc. (FIGS) | Healthcare Apparel | 2025-12-31 | 631.1 | 6.04% | 7.79% | 10-K, companyfacts |
| TaskUs (TASK) | Contact Centers | 2025-12-31 | 1,183.5 | 11.88% | 15.85% | 10-K, companyfacts |
| IBEX Ltd (IBEX) | Contact Centers | 2026-06-30 | 644.1 | 8.53% | 24.58% | 10-K, companyfacts |
| Concentrix (CNXC) | Contact Centers | 2025-11-30 | 9,825.8 | −9.34% | −10.72% | 10-K, companyfacts |
| TTEC Holdings (TTEC) | Contact Centers | 2025-12-31 | 2,136.9 | −5.48% | −10.25% | 10-K, companyfacts |
| Cintas (CTAS) | uniforms, the franchise case | 2026-05-31 | 11,264.8 | **23.14%** | **33.24%** | 10-K, companyfacts |
| UniFirst (UNF) | uniforms | 2025-08-30 | 2,432.4 | 7.59% | 7.42% | 10-K, companyfacts |
| Vestis Corp (VSTS) | uniforms | 2025-10-03 | 2,734.8 | 2.36% | 2.58% | 10-K, companyfacts |

- **Peers named: 10.** *(Buffett says eight; I took ten, and the industry as Superior itself names
  it has about twenty.)*
- **The like-for-like caveat, stated rather than hidden.** Superior's **segment** operating margins
  are Branded Products 7.66%, Healthcare Apparel 2.08%, Contact Centers 7.13% - and on that basis
  Branded Products would beat Cimpress. **But those segment figures exclude the $23.3M corporate
  centre**, which the FY2022 re-segmentation explicitly removed from segment results (*"income and
  expenses related to corporate functions that are not specifically attributable to an individual
  reportable segment are **no longer presented in segment results**"*, FY2022 10-K). Every peer
  figure above is *after* its own corporate cost. **The only comparable line is Superior's
  consolidated 2.36%**, and on that line Superior is level with Vestis - a company whose own
  operating margin collapsed from 7.71% to 2.36% over two years - and below every other peer that
  is not making a loss.
- **Who I could not see, in words.** Named by Superior and **private, with no SEC filing to pull**:
  BDA Inc., HALO Branded Solutions, Staples, HH Global Group, Workwear Outfitters, Medline
  Industries, Careismatic Brands, Barco Uniforms, Encompass Medical, Standard Textile, Transparent
  BPO, Focus Services, Ubiquity, CCI and RDI. **4imprint Group plc**, the purest listed comparator
  to Branded Products, files with the UK authorities and not the SEC, and I did not go down the
  non-SEC rung this session; that is a limit of this run and it is named. **These absences do not
  hold the class PROVISIONAL here, and the reason must be stated rather than assumed:** the
  PROVISIONAL rule exists to stop an unsupported moat *claim*. No moat is being claimed. The
  verdict below rests on **the registrant's own filed description of its markets** under [E3-03]
  criterion 2, and the row is corroboration - on which Superior is last or joint-last among the
  ten competitors it could be measured against. An unseen private rival can only add competitors;
  it cannot create a substitute-free product.
- **[E3-61], the row's limit, honoured:** the row shows position and cannot show conduct. It is
  not being asked to. *"I think you'd have to know the people involved"* is Q3's job, and Q3 does
  not open on this file.

- **Untapped pricing power - could a manager raise the return simply by raising prices, and has
  not? [E3-33]** **No, and the scope rule [E5-28] is why the question is not even close.**
  Claiming that class is claiming *"a monopoly or a near monopoly"*. Superior's own 10-K says
  *"The market for promotional products is **price sensitive** and has historically exhibited price
  and demand cyclicality"*, and FY2025 is the filed experiment: input costs rose, price did not
  follow, and gross margin fell in all three segments. The pricing power is not untapped; it was
  tested and it was not there.

- **The moat that was written off, which is the strongest single piece of Q2 evidence in the
  file.** Goodwill on Superior's balance sheet ran $4.1M (2015) → $11.3M (2016) → $16.0M (2017) →
  $34.0M (2018) → $36.3M (2019) → $36.1M (2020) → $39.4M (2021) → **$0.0M (2022)**. The FY2022
  10-K: *"the Company recorded a non-cash goodwill impairment charge of **$45.9 million** during the
  year ended December 31, 2022 … **As of December 31, 2022, the Company had no remaining goodwill
  balance**"*, split $25.6M to Branded Products and $20.3M to Healthcare Apparel, plus *"a **$5.6
  million** non-cash impairment of indefinite-lived trade names"*. A further **$2.6M tradename
  impairment in Healthcare Apparel** was taken in Q2 2026 (10-Q acc. 0001437749-26-025511).
  **Every dollar of premium paid for every business bought between 2013 and 2021 was written to
  zero in a single year, and the write-down has resumed in 2026.** Whatever advantage was being
  purchased, the company's own audited accounting says it was not there. This is the filed answer
  to [E2-45]'s attacker's test as well: I do not have to imagine how I would attack this position;
  the impairment tests already did it.

- **[E4-36] - which of the four causes of extreme success is on the record here?** None of them.
  There is no extreme max/min of a variable, no non-linear combination, no extreme performance over
  many factors, and no wave. Sixteen years of filings show a company that grew revenue from $106M
  to $566M by buying businesses, wrote the premium off, and earns 4.3% on capital employed. **What
  it most resembles is [E3-51]'s shallows rather than its surfer.**

- Class: **[ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL** · Direction: **narrowing** - gross margin
  down in all three segments, organic volume negative in the largest, the Contact Centers labour
  force down 9.3%, goodwill at zero, and a fresh tradename impairment in 2026 **[E4-32]**.

- **VERDICT: [x] OUT**

  *The evidence is here and the business fails **[E3-03] criterion 2**. Superior's products and
  services have close substitutes; the registrant says so itself, in three separate places, about
  all three of its segments. The competitor row places it last or joint-last of the ten rivals it
  can be measured against. Its own accounting has written the purchased advantage to zero. This is
  an **OUT about the business**, not an UNRESEARCHED about my diligence and not an UNKNOWABLE about
  my evidence: I can name no document that would reverse it, because the documents that would
  reverse it are the ones I have already read and they say the opposite.*

  **Ask the separating test aloud [E4-19]:** *can I name the document that would resolve this?*
  There is nothing left to fetch. The 10-K, the 10-Q, the segment tables of four annual reports,
  the impairment notes and ten peers' annual filings all point the same way. **OUT.**

---
⛔ **THE HARD SEQUENCE STOPS THE FILE HERE. Q3, Q4, Q5 and Q6 are not answered, and no valuation
is reported.** Operator rule 2: no Q5 output may be reported unless Q1-Q4 each show IN.

**What follows is NOT part of the verdict.** It is recorded because the work was done before the
close and because the fold and any future reader are owed it. **None of it promotes or rescues the
name, and a strong Q3 could not [E2-37, E2-38, E3-39].**

## NOTES BENEATH THE CLOSE - NOT VERDICTS, NOT A CLEARANCE

*The file closed at Q2. Everything below was gathered before the close or is owed to the screen
row's standing orders, and it is recorded so the fold and any later reader inherit it. **None of
it is a verdict, none of it promotes the name, and a strong Q3 could not rescue Q2 [E2-37, E2-38,
E3-39].** The framework's own guardrail is the reason this section exists in this form rather than
as answered questions.*

### WHAT WOULD HAVE BEEN Q3 - recorded, not scored

**The weight case, declared even though the gate does not open.** Daily execution: **yes** -
this is a sourcing and brokerage business whose only products are relationships and delivery, the
class [E3-43] says *"can be killed by poor management"*, not a franchise that tolerates it.
Control: no. Leverage: **borderline** - $93.7M of debt against $192.8M of book equity and $25.7M
of EBITDA. **So Q3 would have run as a GATE, not an overlay, had the file reached it.**

**The [E4-29] companion the brief makes standing for every Q3, done before the close.**
`grep -c -i` counts, on the text extractions in `Test Runs/_research 2026-09-21 SGC/`:

| document | "EBITDA" | "Adjusted EBITDA" | "non-GAAP" |
|---|---|---|---|
| FY2025 10-K | **28** | 0 | 7 |
| 10-Q Q2 2026 | **51** | **49** | 9 |
| EX-99.1 Q2 2026 earnings release | **26** | **26** | 4 |
| EX-99.1 FY2025 earnings release | **28** | 4 | 6 |
| DEF 14A 2026 | 7 | 3 | 0 |

**This is the CGNX shape and worse.** The 10-K uses EBITDA as its **reportable segment measure**
("Segment EBITDA" in the Note 2 table) and again as a headline non-GAAP measure in MD&A; the
furnished earnings release leads with *"Adjusted EBITDA of $7.7 million, up from $6.1 million"*;
and the proxy closes the loop - *"the annual incentive bonus generally ties incentive compensation
to **earnings before interest, taxes, depreciation and amortization (EBITDA) as adjusted for
certain items**"* (DEF 14A acc. 0001437749-26-009335). **[E4-29]** calls trumpeting EBITDA *"a
particularly pernicious practice"* because *"it implies that depreciation is not truly an expense …
That's nonsense"*, and **[E5-41]** names the mechanism: depreciation is **reverse float**, money
already spent and recorded later, and it is exactly what the measure deletes. Superior's
depreciation and amortisation was **$12.4M** in FY2025 against **$13.4M** of operating profit, so
the deleted expense is very nearly the whole of the profit.

**The bullseye moved, and it is on the record in one document [E2-49].** *"Yardsticks seldom are
discarded while yielding favorable readings … most managers favor disposition of the yardstick
rather than disposition of the manager"* - demand *"pre-set, long-lived and small bullseyes"*. From
the same proxy, two paragraphs apart:

> *"The Earnings Target for 100% payout of the Individual Target in **2025** was set at
> **$39,656,000**"* … *"The Earnings Target for 100% payout of the Individual Target in **2026** is
> set at **$31,106,000**."*

**A 21.6% reduction in the bonus bar, set after FY2025 EBITDA came in at $25.7M.** The metric was
not switched - that is worth saying plainly, because the flag is a prompt and not a verdict
**[E5-36, E5-38]** - but the *level* of the pre-set bullseye was moved down by a fifth in the year
after it was missed. Whether that is honest re-planning or yardstick disposition is exactly the
question [E2-49] tells a reader to ask, and it is not answered here because Q3 did not open.

**Other Q3 prompts, recorded as prompts:**
- **[E3-50], stock-price targeting.** The 2024 performance-share grants to the CEO (125,000) and
  CFO (75,000) *"vest over the performance period through December 31, 2027 provided the Company
  meets certain **stock price conditions** over the vesting period"*. Pay tied to the quote is the
  premise [E3-50] says the corpus *"adamantly disagree[s]"* with.
- **[E4-27], incentives.** *"Never, ever, think about something else when you should be thinking
  about the power of incentives."* The CEO's 2026 base salary alone is **$1,044,399** at a company
  with a $197.1M market capitalisation and $7.0M of FY2025 net income; the divisional president's
  bonus is **2.5% of BAMKO EBITDA** with an explicit carve-out for acquired EBITDA - a
  well-designed carve-out, and worth noting on the credit side.
- **[E5-15], serial share issuance: does NOT fire.** The count fell from 16,484,921 (2023) to
  15,730,615 (2024) and stands at 15,945,201 (2026-07-30); $10.1M of stock was repurchased and
  retired in FY2025 and $7.4M in FY2024. A May 2025 S-3 shelf went effective 2025-05-22 and has
  not been drawn on in the filings read.
- **[E4-30], the filed-figure fraud tells: do NOT fire, in both directions.** Reported growth is
  the opposite of unnaturally smooth - a $32.0M loss in 2022 sits in the middle of the series.
  Cash taxes as a share of pretax income run 25.6% (2016), 29.0% (2017), 5.1% (2018), 46.4% (2019),
  26.0% (2020), 44.1% (2021), 16.1% (2024), 19.5% (2025) - lumpy, and the recent low readings are
  explained by the 2022 loss carryforward rather than unexplained.
- **The SEC correspondence file was opened rather than assumed.** The 2025-05-19 UPLOAD and the
  2025-05-20 CORRESP (acc. 0001437749-25-017815) are a **Rule 461 acceleration request** on the S-3
  and its acknowledgment - **not an accounting comment letter.** No cockroach found there
  **[E4-22]**.
- **[E2-56], the Pro-Am effect, is live and visible.** The consolidated series camouflages
  segments that differ by 3.7x in operating margin, and the FY2022 re-segmentation moved corporate
  cost *out* of segment results, which flatters every segment line published since.
- **[E3-54], the retention test, is degenerate here and that is the finding.** Over 2021-2025 the
  company earned **$25.2M** of cumulative net income and paid out **$43.3M** of dividends and
  **$17.5M** of buybacks - $60.8M distributed against $25.2M earned, so **retention was negative**.
  The gap was funded by the 2023 working-capital release, not by issuance, so **[E2-52]**'s
  Peter-to-Paul dividend flag does not fire on its own terms. Over the same five years the quote
  went from $23.24 (2020-12-31 close) to $12.36, and market capitalisation fell by roughly $185M.
- **Governance, neutral facts.** Michael Benstock has been CEO since 2003 and a director since
  1985, and took the chair in February 2023 with a Lead Director appointed at the same time.
  Insiders hold **29.1%**, of which Benstock-Superior Ltd. 16.7% and Michael Benstock personally
  7.3%. The proxy states *"there have not been any related party transactions that are required to
  be disclosed under Item 404 of Regulation S-K"* since 2023-01-01. **No integrity disqualifier was
  found, and under [E5-17] that is the absence of found disqualifiers and not a finding that the
  managers are honest.**
- **[E2-26], the half-owner test, splits.** On the credit side: the FY2022 re-segmentation recast
  every prior period and explained itself in full; the goodwill impairment was disclosed with its
  triggering events named; the Q2 2026 release quantified the tradename impairment separately at
  every line. On the debit side: the adjusted figure is the headline in every furnished release,
  and *"On an adjusted basis, excluding the impairment charge, second quarter net income was $3.2
  million"* is **[E2-57]**'s except-for in its pure form - *"you must count the runs scored against
  you in all nine innings."* The impairment is a real cost of a real past decision **[E5-33]**.

### WHAT WOULD HAVE BEEN Q4 - the [E4-25] REBUILD THE SCREEN ROW ORDERED

> **COMPUTATION - NOT A CLEARANCE.**
> *Operator rule 3. This arithmetic was produced after Q2 closed the file. It carries no entry
> language, no valuation verdict and no ranking. It exists because the screen row carried a
> standing `spread_caveat` instructing an [E4-25] rebuild, and a run that ignored it would leave
> the next reader with the 4-construction width the caveat exists to refuse.*

**The construction** *(the framework's CONVENTION)*: owner earnings = operating cash flow − SBC −
(c), with (c) a disclosed judgment **[E2-23]**. **No net-income proxy anywhere** - operator rule 5
forbids it and PRIME RULE 3's CONVENTION clause may not license it.

**The sixteen-year series, rebuilt from the filings, $M:**

| FY | OCF | SBC | capex | D&A | OE, (c)=capex | OE, (c)=D&A | acquisitions |
|---|---|---|---|---|---|---|---|
| 2010 | 6.5 | 0.5 | 0.8 | 2.6 | 5.2 | 3.4 | - |
| 2011 | **−0.9** | 1.0 | 0.9 | 3.0 | **−2.8** | **−4.8** | - |
| 2012 | 9.2 | 0.9 | 1.6 | 2.3 | 6.6 | 6.0 | - |
| 2013 | 8.4 | 0.8 | 1.6 | 2.6 | 6.0 | 5.0 | 32.5 |
| 2014 | 6.8 | 1.4 | 4.9 | 3.8 | 0.5 | 1.6 | - |
| 2015 | 9.9 | 1.4 | 8.1 | 3.9 | 0.5 | 4.7 | - |
| 2016 | 12.0 | 1.6 | 7.4 | 4.9 | 3.0 | 5.4 | 15.2 |
| 2017 | 22.7 | 1.7 | 4.2 | 5.7 | 16.8 | 15.4 | 8.0 |
| 2018 | 19.9 | 2.3 | 4.9 | 7.9 | 12.7 | 9.7 | 85.6 |
| 2019 | 20.0 | 1.5 | 9.7 | 8.3 | 8.9 | 10.3 | - |
| 2020 | 41.4 | 2.5 | 11.9 | 8.1 | 27.0 | 30.7 | - |
| 2021 | 17.1 | 4.0 | 17.7 | 9.3 | **−4.6** | 3.8 | 16.4 |
| 2022 | **−2.6** | 4.3 | 11.0 | 13.0 | **−17.9** | **−19.9** | 11.2 |
| 2023 | **78.9** | 3.8 | 5.0 | 14.0 | **70.2** | **61.1** | - |
| 2024 | 33.4 | 4.3 | 4.4 | 13.2 | 24.7 | 16.0 | 4.0 |
| 2025 | 19.7 | 5.3 | 3.9 | 12.4 | 10.5 | 2.1 | - |

*(Operating cash, capex, D&A, SBC and acquisition cash from SEC companyfacts on the `newest`
restatement vintage, tags `NetCashProvidedByUsedInOperatingActivities`,
`PaymentsToAcquirePropertyPlantAndEquipment`, `DepreciationAndAmortization`, `ShareBasedCompensation`,
`PaymentsToAcquireBusinessesNetOfCashAcquired`, 10-K forms only. The FY2025 row was checked line by
line against the filed Consolidated Statements of Cash Flows in the 10-K, accession
0001437749-26-006653: operating cash $19,709k, additions to property plant and equipment $3,947k,
depreciation and amortization $12,355k, share-based compensation expense $5,263k.)*

**The window means the rebuild produces, against the screen's published $13M-$35M band:**

| window | (c) = capex | (c) = D&A |
|---|---|---|
| 3y 2023-25 | 35.1 | 26.4 |
| 5y 2021-25 | 16.6 | 12.6 |
| 8y 2018-25 | 16.4 | 14.2 |
| 10y 2016-25 | 15.1 | 13.5 |
| **16y 2010-25** | **10.5** | **9.4** |

**The screen's $13M-$35M is the 3-year and 5-year corner of this table.** Seen over the whole
filed history the number is **$9M-$11M**, roughly a third of the screen's top end. *This is what
`spread_caveat` was for, and it changes the shape of the answer, not just its width.*

**[E4-41], normalizing DOWN for the favourable break.** FY2023's $78.9M of operating cash is the
year the screen's own `best_year_note` pointed at, and the filed cash-flow detail names its cause:
**inventories released $24.7M** in 2023 after building $24.5M in 2021 and $15.9M in 2022, with a
further $4.3M released from contract assets and $1.1M from receivables. **That is a balance sheet
unwinding, not earnings.** Strike it out and the same table reads:

| window, excluding FY2023 | (c) = capex | (c) = D&A |
|---|---|---|
| 5y 2021-25 | **3.2** | **0.5** |
| 10y 2016-25 | 9.0 | 8.2 |
| 16y 2010-25 | 6.5 | 6.0 |

**The combined range [E4-25] - window spread × capex band - is $9.4M to $35.1M**, a **3.7x**
width, or **$0.5M to $35.1M** if FY2023's working-capital release is normalized out as [E4-41]
instructs. Against the hand-struck cap of **$197.1M** that is a yield of **4.8% to 17.8%**, or
**0.3% to 17.8%** normalized. **Under [E4-25] that range is too wide to reach a conclusion, and
under the framework that finding would itself have been the Q4 verdict** - *"If the combined range
is too wide to reach a conclusion, that IS the conclusion."* **It is recorded as arithmetic only.
Q4 was never reached and no verdict is entered against it.**

**(c) as a disclosed judgment, since the corpus says it *"must be a guess"* [E2-09].**
*(Cited [E2-09] and not [E2-23]. THE FRAMEWORK v4.md prints both sentences inside one blockquote
headed [E2-23]; the ledger row for [E2-23] ends at the LIFO carve-out and the guess sentence is
[E2-09]'s. PRIME RULE 1: the framework's compression of two rows into one blockquote is not a
licence to repeat the wrong id. Checked against `principle_ledger.csv` `quote_verbatim`, not
against the framework's rendering.)* Superior is **not** the
[E5-20] capital-intensive class - capex was 0.7% of sales in FY2025 - so the D&A end is not invalid
here, but neither end is clean and the reason is specific to this filer:
- **The capex end understates maintenance.** Capex has run below depreciation for four straight
  years (17.7 → 11.0 → 5.0 → 4.4 → **3.9**) while net property, plant and equipment fell from
  $41.9M to $37.4M. **[E2-60]**'s third dimension applies: where the payout is sustained while the
  asset base shrinks, (c) was understated.
- **The D&A end overstates it.** Of FY2025's $12.4M of D&A, **$3.9M is amortisation of acquired
  intangibles** (10-K Note: *"Amortization expense for intangible assets for the years ended
  December 31, 2025 and 2024"*), which is the recorded cost of past purchases, not a renewal
  requirement. Stripping it leaves **$8.5M** of depreciation on physical assets.
- **The disclosed guess, had it been needed: (c) ≈ $6M to $9M**, above the $3.9M actually spent
  because four years of under-spend against a shrinking asset base is not a maintenance run-rate,
  and below the $12.4M D&A because a third of that charge is a past acquisition's ghost. On the
  8-year window that middle construction gives an owner-earnings mean of **$18.3M**; excluding
  FY2023, **$11.6M**.
- **SBC, checked against the brief's 50% trigger:** share-based compensation was **26.7%** of
  operating cash in FY2025 and **14.8%** across 2021-2025. Below the threshold, so the grant table
  was not hand-read; the reported charge is subtracted in full **[E5-06]**, and **[E3-70]**'s
  market-value measure would only make it larger.

**The perimeter the `acq_note` warned about, established.** Acquisition cash by year totals
**$172.9M** across the sixteen filed years - **88% of today's market capitalisation** - of which
$31.6M falls inside the five-year window. **Against that: goodwill went to zero in 2022 on a $45.9M
impairment, $5.6M of trade names went with it, and $2.6M more went in Q2 2026.** The numerator and
the denominator are indeed different companies, and the difference was written off rather than
earned.

**Staying power [E5-11], recorded in outline only.**
1. *A large and reliable stream of earnings*: **no.** Two negative operating-cash years in sixteen
   and a $32.0M loss in 2022.
2. *Massive liquid assets*: **no.** $23.7M of cash at 2025-12-31 against $93.7M of debt.
3. *No significant near-term cash requirements* - the one that usually kills **[E5-11, E5-39]**:
   the 2026-08-07 refinancing pushed the maturity wall out five years, which is the right direction,
   but it **added** debt ($75M of new term loan against $59.1M of old) and it attached named
   covenants: **fixed charge coverage at least 1.25:1 and net leverage no more than 4.0:1**, secured
   on substantially all operating assets. On FY2025 figures net debt of $70.0M against EBITDA of
   $25.7M is **2.7x** - inside the covenant with roughly a 30% EBITDA decline of headroom.
   **[E2-54]**'s coverage test, run properly with capex taken out first: FY2025 operating cash
   $19.7M less capex $3.9M = $15.8M against $5.7M of interest paid and $8.9M of dividends. It
   covers, and it does not cover comfortably.
   **The named way this business would die [E2-27, E3-24]:** not a single event but the covenant.
   A tariff step that the customers again refuse to absorb takes gross margin down another 150bp on
   $566M of sales - that is $8.5M, a third of EBITDA - and 4.0x net leverage arrives with the
   dividend still being paid out of a shrinking number. **A real possibility, not a likelihood**, on
   the evidence of FY2025, in which exactly that margin compression happened at a smaller scale.
   **[E4-40] applies and is why this is written from exposure and not experience**: the company has
   never breached, and the benign history is not the guide.

### [E4-51] - THE STRONGEST SINGLE FACT AGAINST MY OWN VERDICT

*"I'm not entitled to have an opinion unless I can state the arguments against my position better
than the people who are in opposition."* The strongest fact against a Q2 OUT is this one, and it is
filed:

**Superior's Branded Products segment - 64% of revenue - earned a 7.66% operating margin in
FY2025, which is higher than Cimpress plc's 6.72% and more than double Lands' End's 3.32%, the two
listed companies closest to what it does.** Its Contact Centers segment earned 7.13% while
Concentrix earned −9.34% and TTEC −5.48%, two rivals many times its size. On a segment view
Superior is not the worst operator in either market; it is a middling-to-good one. **The bear case
I have written rests on the consolidated line, and the consolidated line is dragged below every
peer by a $23.3M corporate centre - that is, by a holding-company structure, not by a competitive
failure in the operating businesses.** A reader who believed the corporate cost could be halved,
or the three segments separated, would be looking at a very different set of numbers from the ones
I have ranked.

**Why it does not change the verdict.** [E3-03] criterion 2 is a question about the *product*, not
about the operator's relative skill, and the registrant's own 10-K answers it against itself in
three separate places. A good operator inside a substitutable market is what **[E2-37]** calls *"a
remarkable textile company - but not a remarkable business"*, and **[E2-38]**'s jockey on a
broken-down nag. *(The dash inside that quotation is a HYPHEN because `principle_ledger.csv`'s
`quote_verbatim` field for [E2-37] carries a hyphen; THE FRAMEWORK v4.md renders the same
sentence with an em dash. The ledger row is the source and it wins, PRIME RULE 1 - and it happens
to agree with the standing no-em-dash rule, so no em dash appears anywhere in this file.)* And the corporate cost is not an accident to be modelled away: it has been $17.1M,
$19.6M, $23.5M and $23.3M in the four filed years since the re-segmentation, growing 36% while
revenue fell 2.2%. **[E4-26]** - hunt disconfirming evidence hardest for the favourite hypothesis -
required writing that paragraph, and it is the reason the competitor row above carries the segment
figures as well as the consolidated one instead of quietly reporting only the line that supports
the conclusion.

---
## Q3 · Q4 · Q5 · Q6 - NOT ANSWERED

**No verdict is entered at Q3, Q4, Q5 or Q6.** The hard sequence stops at the first verdict that is
not IN, and Q2 returned OUT. Operator rule 2: no Q5 output may be reported unless Q1-Q4 each show
IN. The material above is evidence held for the record, not answers.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped - Q1 IN, Q2 OUT, file closed, Q3-Q6 not
      answered and explicitly marked so.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only IN
      and rests entirely on documents opened this session.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives - **none was used.**
- [x] Every UNKNOWABLE verdict states what specifically cannot be known - **none was used.** The
      Q2 close is an OUT about the business, and the separating test [E4-19] was asked aloud in the
      verdict block.
- [x] Step 0: the filing was read, with accession numbers; **three** figures cross-checked by hand
      against filed statements, including equity recomputed from A − L **[E5-32]**.
- [x] Owner earnings on a multi-year mean; five windows stated; capex band disclosed as a judgment
      with its two defects named. **Headed COMPUTATION - NOT A CLEARANCE and carrying no entry
      language**, because it was produced after the close (operator rule 3).
- [x] Competitor row filled - ten named peers, specification stated in advance, every ratio
      computed this session from the peers' own SEC annual filings; fifteen private rivals and one
      UK filer named as unseen, with the reason the class is not held PROVISIONAL stated in words.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated: **5.34%, US
      Treasury daily par yield curve, 2026-09-18.** Not inherited from the brief.
- [x] Value stated as a round-number range, not a point estimate - **no value is stated at all**,
      because Q5 never opened. The owner-earnings arithmetic is carried as a range.
- [x] One bar chosen, not both; windage count stated - **neither bar was used**; no margin of
      safety was applied anywhere, because no valuation was performed. **Windage count: 0.**
- [x] Prices dated; aggregator used for live quotes only and flagged - $12.36, 2026-09-21 09:44 ET,
      Yahoo, flagged as the only aggregator number in the file.
- [x] Run committed to git - three commits: Q1, Q2, and the fold.
- [x] **Every ledger id cited was verified to exist in `principle_ledger.csv`** (311 rows) before
      the commit. **62 distinct ids cited, 62 verified.** Zero phantom citations.
- [x] **Every corpus quotation was matched word for word against `principle_ledger.csv`'s own
      `quote_verbatim` field, not against the framework's rendering of it.** Fourteen fragments
      checked, fourteen matched, and the check found two things worth recording: [E2-37]'s ledger
      row carries a HYPHEN where the framework prints an em dash, and *"must be a guess"* belongs
      to **[E2-09]**, not to [E2-23] whose blockquote the framework prints it inside. Both are
      corrected in place above. **Typographic note:** apostrophes and quotation marks are ASCII
      throughout this file where the ledger carries curly glyphs; the words are verbatim and only
      the glyphs differ.
- [x] **No em dash anywhere in the file**, including inside quotations: `principle_ledger.csv`'s
      own `quote_verbatim` for [E2-37] carries a hyphen where the framework renders an em dash,
      and the ledger row is the source (PRIME RULE 1).

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line:** Superior Group of Companies is a competent operator of three substitutable
  spread businesses whose own 10-K calls all three of its markets fragmented and whose own auditors
  wrote every dollar of purchased goodwill to zero in 2022; **Q2 OUT on [E3-03] criterion 2**, with
  a consolidated operating margin of 2.36% and a return on capital employed of 4.27% placing it
  last or joint-last of ten measurable rivals.
- **If UNRESEARCHED - THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.

**THE REVERSAL CONDITION, IN WORDS - NOT A PRICE BAND (the QLYS ruling, 2026-09-07).** A name that
failed on the **business** gets no alert in `tools/alerts.json`, because a price alert on it is a
category error. This file would be reopened only on evidence that the product acquired a close
substitute-free position, which would look like: **two consecutive years of rising gross margin
rate in Branded Products *and* Healthcare Apparel while input costs rise**, filed in the 10-K's own
MD&A language, **together with organic** (not acquired) **segment revenue growth above 5%**. Price
is not a reopening condition at any level.
