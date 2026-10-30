# Company Run — UiPath, Inc. (PATH) — 2026-09-19
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
## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-19 (just after midnight EDT); the template was copied and committed before any fetch
(`71c902c`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the third name in
the "no share count from dei: read the cover" row (META and DASH were the first two). Research, scripts and downloaded filings
are in `Test Runs/_research 2026-09-19 PATH/`. **No PATH row exists in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`**
(the triage skip reason says why), so there is no screen row to carry. Every figure below is from UiPath's own filings, fetched
by this run, with the accession.

### The entity, in every year used
CIK 0001734722, `submissions.json` (fetched by this run): *"UiPath, Inc."*, SIC 7372 *"Services-Prepackaged Software"*,
`stateOfIncorporation` **"DE"**, `fiscalYearEnd` **0131**, no former names, ticker PATH on NYSE. **The charter has not moved:**
the 8-K of 2026-09-03 (`0001734722-26-000047`) gives *"Delaware"* on its cover, the FY2026 10-K says the company *"was
incorporated in Delaware in June 2015"* and *"because we are incorporated in Delaware, we are governed by the provisions of
Section 203"*, and the 10-K exhibit index carries one certificate of incorporation, the 2021 one (*"3.1 | Amended and Restated
Certificate of Incorporation of UiPath, Inc. | 8-K | 001-40348 | 3.1 | 04/28/2021"*); the only later Item 5.03 (2023-03-10)
amended the bylaws. IPO April 2021 (S-1 effective 2021-04-20, 424B4 2021-04-21). One reporting entity throughout. **Fiscal years
end 31 January and are named for the calendar year in which they end: "FY2026" = the year ended 2026-01-31; "Q2 FY2027" = the
quarter ended 2026-07-31.**

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"no share count from dei: read the cover."* **A prompt to read, never a verdict.** The probe (`_probe_screen.py`,
copied from DASH's with the CIK and ticker changed; output `_probe_screen_output.txt`) shows companyfacts carries **one** dei
element for UiPath, `EntityPublicFloat` (five facts, FY2022-26 10-Ks), and **no `EntityCommonStockSharesOutstanding` at all**;
`share_count_shift` returned **None** under both the current screen and `a8bc84f` (not measured, not stable: the RIVN
reading), and `shares_outstanding` returned None. **The META and DASH hypothesis (a dimensioned per-class cover) was tested on
the inline XBRL** of the two latest periodic filings (`dei.py`, output `dei_out.txt`; raw `10Q_2026Q2_raw.htm`,
`10K_FY2026_raw.htm`), and **it holds, in META's form: two classes, both non-zero.** In the Q2 FY2027 10-Q
(`0001734722-26-000050`):

- *"name="dei:EntityCommonStockSharesOutstanding" ... 456,464,703"* in context c-2, segment
  *"dimension="us-gaap:StatementClassOfStockAxis">us-gaap:CommonClassAMember"*, instant 2026-09-03;
- the same element in context c-3, *"us-gaap:CommonClassBMember"*, **64,690,706**.

No `ixt:fixed-zero` class (UiPath has no third class). The FY2026 10-K (`0001734722-26-000012`) tags the same two dimensioned
facts at 2026-03-20 (459,231,166 A; 64,690,706 B). **companyfacts publishes only undimensioned facts, so a cover tagged per class
never reaches it. For PATH the label was the META kind: a tagging convention for a two-class cover, not a missing or stale
count.**

**The other `a8bc84f` guards, on facts filed by 2026-09-01:** `scale_shift` **1.468** (did not fire); `restatement_shift`
**(1.0, FY2021)**, a null and not a guard (the SNOW note). **Unlike DASH, the count was NOT the only thing standing between PATH
and a positive price: `a8bc84f`'s `owner_earnings()` returns NEGATIVE figures at every end** (`{'5y_da': -214.1M, '5y_capex':
-210.9M, '3y_da': -28.9M, '3y_capex': -23.7M}`), so with a count the triage would have priced it at a negative yield. The current
screen returns the same shape (`5y_capex` -211.5M). **Not a verdict**: Q4 rebuilds owner earnings from the filed statements.
Also printed by the current screen and carried to Q4 as a prompt: `working_capital_flag` on FY2023, *"DeferredRevenue moved
$160.7M in 2023 when OCF was $10.0M"*.

**Restatement check:** no 10-K/A or 10-Q/A in the submissions index since the IPO. **Auditor change** read: 8-K of 2022-04-20
(`0001734722-22-000014`, Item 4.01), Grant Thornton dismissed, KPMG engaged, *"not the result of any disagreement"*, with one
reportable event disclosed (a FY2018 revenue-recognition material weakness, *"remediated"* by 2021-01-31). Carried to Q3.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run
  at 00:02 EDT on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.29, '09/17/2026')** seconds later (`step0_out.txt`): the stale-cache defect
  again (DASH recorded the eighth occurrence; this is the ninth recorded). The issuing-authority figure is used. FRED not used.
  Struck by this run, not inherited from the brief or from DASH.
- **Earnings currency: USD, with a large foreign share** (the geography split is read at Q1). No ADR or FX conversion of the
  quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$13.39, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("PATH", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 13.39,
  `regularMarketTime` 1789761603 = **16:00:03 EDT**, the closing print; the day's bar $13.325-$13.95. `tools/sources.price()`
  returned the same 13.39 stamped 2026-09-18.
- **The month, recorded rather than choosing a day:** 08-19 $15.78 · 08-27 $18.33 · 08-31 $18.67 (the month's high close) ·
  09-03 $18.22 · **09-04 $15.19 (-16.6% on the day after the Q2 FY2027 release and the CFO change)** · 09-09 $13.57 · 09-14
  $14.66 · 09-18 $13.39. **-28% from the 08-31 close.**
- **Primary-filing cross-check (Form 4s, `f4.py`, `form4_table.txt`):** Ashim Gupta (COO) sold 117,339 shares on 2026-09-11 at
  a weighted $13.8539, range *"$13.7400 to $14.4100"* (`0001855778-26-000007`), inside Yahoo's 09-11 range ($13.74-$14.465);
  Raghu Malpani sold 98,429 on 2026-09-16 at $13.8135, range *"$13.5300 to $14.0400"* (`0002127293-26-000008`), inside Yahoo's
  09-16 range ($13.51-$14.08). **The aggregator's series is corroborated on two dates. No Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-09-03): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the class treatment from the charter
- **Class A 456,464,703 + Class B 64,690,706 = 521,155,409 shares**, from the cover of the **Form 10-Q for the quarter ended
  2026-07-31, filed 2026-09-08, accession `0001734722-26-000050`**, the latest periodic filing: *"As of September 3, 2026, the
  registrant had 456,464,703 shares of Class A common stock and 64,690,706 shares of Class B common stock, each with a par value
  of $0.00001 per share, outstanding."*
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q's face: *"547,650 and 540,898 shares issued; 456,299
  and 472,346 shares outstanding, respectively"* (Class A, thousands, 2026-07-31 and 2026-01-31) and *"64,691 shares issued and
  outstanding"* (Class B). The cover moves +166K A in 34 days. **Consistent.**
- **After the cover date:** Daniel Dines converted **5,000,000 Class B into Class A on 2026-09-08** (Form 4
  `0001855767-26-000018`, codes C and J; the 8-K of 2026-09-03 announced it with a 10b5-1 plan to sell up to 5,000,000 Class A
  *"through February 1, 2027, subject to limit prices"*). One for one, so the **sum is unchanged**; the class split is now
  about 461.5M A and 59.7M B.
- **Why the classes are added, one for one.** The governing charter is the Amended and Restated Certificate of Incorporation
  (8-K of 2021-04-28, `0001193125-21-135339`, Exhibit 3.1, read as `CHARTER_2021.txt`): dividends *"shall be paid pro rata, on an
  equal priority, pari passu basis, unless different treatment of the shares of each such class is approved by the affirmative
  vote of the holders of a majority of the outstanding shares of Class A Common Stock and a majority of the outstanding shares
  of Class B Common Stock, each voting separately as a class"* (Art. IV.D.2(a)); stock dividends only in like kind and at the
  same rate (2(b)); *"the outstanding shares of all Common Stock will be subdivided or combined in the same proportion and
  manner"* (2(c)); on a Liquidation Event, assets and acquisition consideration *"shall be distributed on an equal priority, pro
  rata basis to the holders of Class A Common Stock and Class B Common Stock"* (3). Votes differ: *"one vote"* per A,
  *"thirty-five votes"* per B (4). Class B converts into *"one fully paid and nonassessable share of Class A Common Stock"* at
  the holder's option, on transfer, and on the founder's death. The 10-K's own note: *"The rights of the holders of our Class A
  and Class B common stock, including liquidation and dividend rights, are identical except with regard to voting and conversion
  rights."* **Economically identical, so the cash-flow claim is the sum; the votes (Dines holds all Class B, *"approximately 84%
  voting power"* at 2026-01-31) belong at Q3 (control), not in the count.**
- **Dilution not in the count:** 20,956 thousand unvested RSUs, 6,560 thousand options at a weighted $0.51, and 1.2 million
  PSUs expected to vest at 2026-07-31 (10-Q Note 12), plus **5.3 million PSUs granted to senior management on 2026-09-03** (10-Q Note 16, *"Subsequent Events"*; the 8-K names
  3,075,000 of them for four officers; share-price hurdles to 2029 and 2031) and 130,368 RSUs to the new CFO: about **34.1M, 6.6%
  of the cover count.** No
  convertible debt. Shown beside the cap, not in it.

### The market cap
**$13.39 x 521,155,409 = US$6.978bn.** Split factor 1.0. **With unvested RSUs, options and PSUs: about $7.44bn.** Public float on
the FY2026 10-K cover: $4.8bn at 2025-07-31 (companyfacts, the one dei element). Cash, cash equivalents and marketable securities
$1.405bn at 2026-07-31 (EX-99.1 of 2026-09-03), no debt: carried at Q4 and Q5, not netted here.

### THE DEAL CHECK: none live on the registrant as target
`sources.deal_filings("0001734722")` returned `([], [], '2026-03-25')` and `deal_note` returned empty (`step0_out.txt`). The
submissions index since the IPO carries **no 425, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D** on this registrant. **The quote is
not a spread and buys this company.**

### The perimeter: what (c), the five-year mean and the cap must see
- **Small, cash-paid tuck-ins only.** Peak AI Limited (UK), closed 2025-03-07: intangibles $16.2M, goodwill $27.3M (10-Q Note 6);
  cash *"Payments related to business acquisitions, net of cash acquired | ( 24,821 )"* in FY2026. **WorkFusion, Inc.**, closed
  2026-02-05: goodwill $58.2M; cash **$149.4M** in H1 FY2027 plus $29.6M of contingent and deferred consideration. **No
  acquisition moves revenue by more than a few percent in any year**, so no splice is needed; cash acquisitions are carried in
  their own column at Q4 (the DASH practice).
- **One minority investment**: convertible bonds of a private company, *"the H Company, purchased during fiscal year 2025"*, Level
  3. Immaterial to (c).

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2026 Form 10-K** (year ended 2026-01-31), filed **2026-03-25**, accession **`0001734722-26-000012`** (`10K_FY2026.txt`),
  and the **Q2 FY2027 Form 10-Q** (quarter ended 2026-07-31), filed **2026-09-08**, accession **`0001734722-26-000050`**
  (`10Q_2026Q2.txt`).
- Also read: the FY2022-FY2025 10-Ks (`0001734722-22-000006`, `-23-000017`, `-24-000011`, `-25-000007`); the Q1 FY2027 and Q2
  FY2026 10-Qs (`0001734722-26-000041`, `-25-000043`); the DEF 14A of 2026-05-12 (`0001734722-26-000027`); the 8-Ks of 2022-04-20
  (4.01), 2022-06-27, 2022-11-14, 2024-07-09 and 2025-03-12 (2.05 restructurings), 2023-03-10, 2026-03-25, 2026-06-29 and
  2026-09-03; the charter; **every 8-K EX-99.1 earnings release from 2022-03-30 to 2026-09-03** (19); eight Form 4s.
- **Figures cross-checked against the filed statement** (FY2026 10-K consolidated statement of cash flows, $ thousands,
  FY2026/25/24): *"Net cash provided by operating activities | 371,208 | 320,565 | 299,082"*, *"Stock-based compensation expense
  | 290,676 | 358,151 | 371,955"*, *"Depreciation and amortization | 16,969 | 17,232 | 22,597"*, *"Purchases of property and
  equipment | ( 19,048 ) | ( 14,923 ) | ( 7,342 )"* match companyfacts (`ocf`, `sbc_annual`, `da_annual`, `annual(CAPX_TAGS)`) to
  the thousand. Revenue *"Total revenue | 1,610,572 | 1,429,664 | 1,308,072"* matches.

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in
> character. If a business is complex or subject to constant change, we're not smart enough to predict future cash
> flows."* **[E3-31]**

### What the filings show, in my own words, without management's language
A large company has clerks who copy data from one screen to another: an invoice from an email into the ledger, a claim from a
form into the claims system. UiPath sells software that does those keystrokes instead (a "robot" that drives the same screens a
person would), plus the tools to design, schedule and supervise those robots, and more recently tools that read documents and
call AI models inside the same flows (the 10-K: *"computer vision technology and user interface automations in our initial RPA
offering, which remains the foundation of our platform today"*). **It charges by the year for each product the customer
licenses** (the filer counts its renewable base *"per solution SKU"*; no filing states the unit of price, grepped for "pricing
model", "we price" and "we charge"). Revenue arrives three ways (FY2026 10-K face, $M): **licences** $606.4M (*"term licenses ...
provide customers the right to use software for a specified period of time"* on their own servers, *"recognized at the point in
time at which the customer is able to use and benefit from the software, which is generally upon delivery"*), **subscription services** $954.5M (maintenance and support on those licences,
plus the same software run in UiPath's cloud, recognised over the term) and **professional services** $49.7M. The customer
renews each year or each term; the company reports the renewable base as ARR, *"annualized invoiced amounts per solution SKU
from subscription licenses and maintenance and support obligations"* (10-K MD&A). Costs are people: sales and marketing
$683.3M (42% of revenue), research and development $385.2M (24%), general and administrative $214.3M (13%), against a cost of
revenue of $271.0M (gross margin 83%). **So each customer is: the products it licenses x their annual price, renewed or not,
less the salesforce needed to land and expand it.** The filed series (10-Ks, 10-Q, EX-99.1s):

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Q2 FY2027 |
|---|---:|---:|---:|---:|---:|---:|
| Revenue ($M) | 892.3 | 1,058.6 | 1,308.1 | 1,429.7 | 1,610.6 | 410 (qtr) |
| ARR, year end ($M) | 925.3 | 1,204 | 1,464 | 1,666 | 1,853 | 1,938 |
| ARR growth | 59% | 30% | 22% | 14% | 11% | 12% |
| Net new ARR in the year ($M) | 344.8 | 278.6 | 260 | 202.4 | 186.4 | 86 (H1) |
| Dollar-based net retention | 145% | 123% | 119% | 110% | 107% | 109% |
| Customers (approx.) | 10,100 | 10,800 | 10,830 | 10,753 | 10,747 | n/a |
| Customers with ARR >= $1M | 158 | 229 | 288 | 317 | 357 | n/a |
| GAAP operating income ($M) | (500.9) | (348.3) | (164.7) | (162.6) | 56.8 | 32 (qtr) |

FY2026 revenue by region: Americas 50%, EMEA 33%, Asia-Pacific 17%; the U.S. *"46 %"* (10-K Note 3). Of FY2026 growth, *"15% was
attributable to new customers and 85% was attributable to existing customers"* (10-K MD&A). **The company made its first
full-year GAAP operating profit in FY2026, 3.5% of revenue.**

**The scarce input the business controls:** the customer's installed automations, written in UiPath's own design tools and
running on its orchestrator; and the brand and partner network that made it the named leader in its category at the IPO. **What
it does not control, on its own filing:** the price (*"Some of our competitors offer their on-premises or SaaS solutions at a
lower price, which has resulted in, and may continue to result in, pricing pressures"*, every 10-K FY2022-26, read at Q2) and
the direction of the technology (*"AI's disruptions compel organizations to make bold changes"*; AI agents create *"the ability
to build software internally that would have otherwise been purchased"*, FY2026 10-K Item 1).

**Will the fundamentals look broadly the same in ten years?** The mechanism (an annual fee per licensed product for software that
drives other software) has held in the filed record since FY2022. Against that, in the company's own words: it describes itself
as *"pioneering the evolution from rule-based automation to intelligent agentic automation"*, says *"we operate in a very
competitive and rapidly changing environment"* (FY2026 10-K, forward-looking statements), and has changed its own name for its
market twice in two years (RPA through the FY2024 10-K, then *"agentic automation"* from FY2025, now *"Business orchestration and
automation technologies ( BOAT )"* in FY2026; grepped).

### THE CASE FOR UNKNOWABLE, AT FULL STRENGTH **[E4-26, E4-51]**
(1) The filer says the category is being remade by AI in real time; that is [E3-31]'s *"subject to constant change"* in the
company's own words. (2) AI agents may do the clerk's job without a screen-driving robot at all, which would remove the thing
UiPath charges for; no filing gives that a revenue or cost line. (3) The profit history is one year long (operating losses every
year to FY2025), and FY2026 net income of $282.3M includes a $181.7M tax benefit from *"release of valuation allowance
associated with our U.S. entity"* (10-K MD&A).

**Why it does not carry, and what is excluded.** HHH, RGTI and DJT closed at Q1 because the declared business was not the filed
one. **Here the filed business is the declared one**: nearly all revenue is annual licence, maintenance and cloud fees for
automation software, with a filed renewable-base series (ARR), a filed retention series and a filed customer count in every year
FY2022 to Q2 FY2027, and I can state the unit economics from them. **What is outside the circle is named: the future economics of
"agentic" AI products (Agent Builder, Maestro, the WorkFusion and Peak vertical agents) and whether AI agents replace
screen-driving robots.** [E4-46] says study will not repair those; they are recorded as outside the circle and **cannot be
counted at any later gate**. **Whether a product the filer says faces lower-priced and free alternatives has a position is the Q2
question, and it is carried there, not decided here.**

- **VERDICT: [x] IN** on the business the filings show (annual licence, maintenance and cloud fees for enterprise automation
  software, $1.853bn of ARR at 2026-01-31, $1.938bn at 2026-07-31, about 10,750 customers). **Not IN** for the future economics
  of agentic AI products and for the question whether AI agents displace robotic automation: outside the circle [E3-31, E4-46],
  never counted later; their cost is carried at Q2 and Q4.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its customers to have **no close
> substitute** and; (3) is not subject to price regulation."* **[E3-03]**, 1991 letter

### THE HYPOTHESIS TO BE REFUTED, AT FULL STRENGTH **[E4-26, E4-51]**
UiPath was the category's leader at listing and still is its largest pure-play SEC filer: **$1.61bn of FY2026 revenue against
Appian's $727M**, with Automation Anywhere private. Its gross margin is 83%; its renewable base has grown every quarter on
record (ARR $925M to $1,938M, FY2022 to Q2 FY2027); its existing customers still spend more each year than the year before (net
retention 107-109%, never below 100% in the filed series); the number of customers paying $1M or more has more than doubled
(158 to 357, FY2022-26) and they now pay *"52 %"* of revenue; 85% of FY2026 growth came from existing customers. Automations
written in a vendor's design tool and scheduled on its orchestrator are not free to rewrite, and a finance department that has
200 robots running its close does not rip them out for a cheaper licence. **If enterprise automation software is a franchise,
this is the candidate.**

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES.** About 10,747 paying customers at 2026-01-31; ARR +12% to $1.938bn at 2026-07-31; 357
  customers above $1M of ARR.
- **(3) Not subject to price regulation: YES.** No filing names a regulator of UiPath's prices. (AI regulation, the EU AI Act
  and data-transfer rules are named in Item 1A as compliance costs, not price-setting.)
- **(2) No close substitute: NO, on four independent records.**
  1. **The company's own filing, five 10-Ks running (FY2022 to FY2026), Item 1A, in the past tense:** *"Some of our
     competitors offer their on-premises or SaaS solutions at a lower price, which has resulted in, and may continue to result
     in, pricing pressures."* A realised pricing pressure from cheaper alternatives is the definition of a close substitute. From
     FY2024 on, the same section adds: *"open source alternatives for automation that are offered at no cost may impact our
     ability to sell our products to certain customers who may prefer to rely on these tools"*; and every year: *"sales of our
     platform and products could be adversely affected if customers or users within these organizations perceive that features
     incorporated into competitive products reduce the need for our products, or if they prefer to purchase other products that
     are bundled with solutions offered by other companies that operate in adjacent markets"*, and *"If any of these potential
     competitors were to provide an automation solution within their current service offerings as a single, integrated
     solution, our customers and potential customers may choose to adopt the integrated solution due to administrative ease."*
     The FY2026 10-K adds the AI version: AI agents create *"the ability to build software internally that would have otherwise
     been purchased"* (Item 1), and *"our customers may also internally develop their own automated solutions"* (Item 1A).
  2. **A competitor's own 10-K names the substitutes.** SS&C Technologies (owner of Blue Prism), FY2025 10-K
     (`0001193125-26-076745`), Item 1: *"SS&C competes with a range of technology providers including companies such as
     Microsoft, Pega, UiPath, Appian, and emerging agentic AI providers such as n8n and Lyzr."* UiPath's own FY2023 10-K named ten:
     *"Appian Corporation, Automation Anywhere, Inc., Blue Prism Group PLC, Celonis Inc., Kofax Inc., Microsoft Corporation, NICE
     LTD., NTT Ltd., Pegasystems Inc., and WorkFusion, Inc."* (the FY2026 10-K stops naming competitors and lists seven
     categories instead, including *"Proprietary and open-source AI model providers and coding agents"*).
  3. **The retention series, which is the customer's own vote on substitutes, measured by the company.** Dollar-based net
     retention fell or held in every one of fifteen consecutive quarterly releases, from 145% (Q4 FY2022) to 107% (Q3 and Q4
     FY2026), rising for the first time to 109% in Q1 FY2027 (the series is in the EX-99.1s, listed in the Q1 table's source).
     The count of customers stopped growing after FY2023 (about 10,800, 10,830, 10,753, 10,747). **Net new ARR has fallen every
     year: $344.8M, $278.6M, $260M, $202.4M, $186.4M** (FY2022-26), while sales and marketing spending stayed at $683-738M a year (FY2024-26).
     The filer's own list of what moves ARR includes *"pricing, competitive offerings"* (10-K MD&A). A product with no close
     substitute does not lose a third of its expansion rate while its salesforce holds.
  4. **No price rise is on record.** Five 10-Ks, nineteen earnings releases and three 10-Qs were swept for "price increase",
     "increase in price", "increased price" and "pricing" (`price_sweep.txt`), and the 10-Ks and latest 10-Q separately for
     "pricing pressure" and "discount": **no instance found of a price increase**; every hit is transfer pricing, securities
     pricing, a product description, the ARR caveat (*"pricing, competitive offerings"*) or the pressure sentence above. Revenue growth is
     attributed to more subscription and licence volume and to existing customers buying more, never to price.

### [E4-04]: MUST THE MOAT BE CONTINUOUSLY REBUILT?
The test v4 sets: does a lapse in spending destroy the structure or narrow it, and does the spending defend the same advantage
or buy its replacement? **The filer says it is buying the replacement.** (a) *"Building upon decades of leadership in
automation, UiPath is pioneering the evolution from rule-based automation to intelligent agentic automation"*; the product
lines it now leads with (Agent Builder, Maestro, Maestro Case, Maestro Flow, the IXP document products) appear in none of the
FY2022-24 10-Ks (grepped: "Maestro" first in FY2026, "Agent Builder" and "agentic" first in FY2025, "IXP" first in FY2026), and
its FY2026 10-K headline is that *"AI necessitates reinvention."* (b) The spend is continuous and large:
research and development $332-385M a year (24% of FY2026 revenue), and two AI acquisitions in twelve months (Peak, March 2025;
WorkFusion, February 2026, $149.4M cash). (c) The original basis, the screen-driving robot, is the part the company itself says
AI agents and *"coding agents"* may make internal (above). **This is the Rhodes Ridge case in v4's test (the spending buys a
replacement basis), not the Coca-Cola case (the spending defends the same trademark)**: Munger's competitive destruction, with
a surfing run on the RPA wave of 2018-2022 **[E3-51]** whose ARR growth fell from 59% to 11% as the wave passed.

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4; the corpus's own test is pricing conduct plus returns on capital [E3-43])*
Same metric, same five-year window (each filer's last five fiscal years, UiPath's ending 2026-01-31, the others 2025-12-31),
each figure from the filer's own XBRL, cross-checked for UiPath to the filed face at Step 0 (`peers/row.py`, `peers/row_out.txt`;
peer 10-Ks in `peers/`). **Owner cash** = operating cash less stock compensation less purchases of property and capitalised
software, the same construction for every filer.

| Company (10-K) | revenue, last FY | revenue growth, 4-step CAGR | owner cash / revenue, 5-yr | owner cash / revenue, last FY | retention metric, filer's own |
|---|---:|---:|---:|---:|---|
| **PATH** (`0001734722-26-000012`) | $1,610.6M | 15.9% (now 12-13%) | **-16.8%** | **3.8%** | net retention 145% (FY2022) to 107% (FY2026), 109% Q2 FY2027 |
| **APPN** Appian (`0001441683-26-000013`) | $726.9M | 18.5% | -15.4% | 2.5% | *"Commencing in 2025, we are replacing our previously reported cloud subscriptions revenue retention rate with a new key metric"* |
| **PEGA** Pegasystems (`0001013857-26-000017`) | $1,745.8M | 9.6% | 5.1% | **19.2%** | ACV (not comparable) |
| **NOW** ServiceNow (`0001373715-26-000007`), whole company | $13,278M | 22.5% | 14.7% | 19.7% | renewal rate *"98% for each of the years ended December 31, 2025, 2024 and 2023"* |
| **SSNC** SS&C (`0001193125-26-076745`), whole company, Blue Prism unsegmented | $6,272M | 5.6% | 17.5% | 18.9% | not filed for Blue Prism |

**Peers taken: four SEC filers of the eleven the filers name** (UiPath's FY2023 list of ten, plus SS&C's n8n and Lyzr). Not
taken: **Microsoft** reports its competing product inside Dynamics (*"Dynamics 365, comprising a set of intelligent, cloud-based
applications across ERP, CRM, Power Apps, and Power Automate"*, FY2026 10-K `0001193125-26-323660`, `peers/`), so no automation
figure exists, and it names UiPath in no 10-K (`fts_count` 0); **Automation Anywhere, Celonis, Kofax, n8n, Lyzr and NTT** are
not on the SEC's `company_tickers.json` (`peers/private_check.txt`); **NICE Ltd.** is an SEC registrant and was not fetched (a
work order that cannot move this verdict); **WorkFusion** is now inside UiPath. ServiceNow and SS&C are carried whole-company because
neither segments the competing product; they show what a platform that bundles automation earns, not a like-for-like. **The class
is not held PROVISIONAL on the absent peers, because the verdict rests on criterion (2) in the subject's own words and in a named
competitor's, not on a ranking the missing filers could reverse.**

**What the row shows.** UiPath is **the largest pure-play by revenue and last or second-last on owner cash per dollar of
revenue** over five years, level with Appian, and it reached a positive owner-cash year only in FY2026 (3.8%), when Pegasystems,
at about the same revenue and growing slower, kept 19.2 cents of every revenue dollar. **Direction [E4-32]:** all four filers'
owner-cash margins rose over the window, so the improvement is industry-wide, not UiPath pulling away; Pegasystems rose fastest
(-7.2% to 19.2%). **The row's limit [E3-61]:** it shows position, not conduct, and it cannot show the one number a moat claim
here would need, share of enterprise automation spend, because no filer publishes it (UiPath's FY2022-26 10-Ks contain no
instance of "market share" or "leader in", grepped; the releases describe the company as *"a leader in business orchestration
and automation"*, which is a self-description, not a share).

### THE OTHER Q2 TESTS
- **Returns on capital, asked about the business [E3-46]:** net income over average equity **-17.1% / -4.6% / -3.8% / 14.4%**
  (FY2023-26: $(328.4)M, $(89.9)M, $(73.7)M, $282.3M on average equity of $1,921M, $1,968M, $1,931M, $1,964M), the FY2026 figure
  carrying the $181.7M tax-allowance release; on pretax income, FY2026 is **5.1%**. Accumulated deficit **$1,705.5M** at
  2026-01-31. Equity is mostly IPO cash and marketable securities ($1,689.5M at 2026-01-31), so the return on tangible operating
  capital is not finite; that is true of any software company funded by customer prepayment and says nothing about substitutes.
- **[E2-44], both halves:** price with flat demand and idle capacity: **not shown** (no price rise on record; the filer records
  pressure the other way). Growth with minor capital: capex $7-24M a year, so **the second half passes**; the capital this
  business consumes is stock pay and sales spending, read at Q4.
- **[E4-37] agony pricing:** the pressure sentence, repeated five years, is the prayer session in writing; the company's
  response has been to add products (agents, test automation, document processing, vertical AI) rather than raise the price of
  the one it has.
- **[E3-33] untapped pricing power / [E5-28]:** claiming it would be claiming near-monopoly; SS&C's list of five named
  alternatives and UiPath's own list of ten refute it.
- **[E2-53] the dominance class:** position would have to set the economics regardless of execution. The record runs the other
  way: three workforce reductions in three years (about 5% in June 2022, 6% in November 2022, 10% in July 2024, the last amended
  in March 2025; 8-Ks Item 2.05), the chief executive's office changed three times in about two years (Dines and Rob Enslin as
  co-CEOs from 2022-05-16; Enslin sole CEO from 2024-02-01; Enslin resigned and Dines CEO again from 2024-06-01; 8-Ks of
  2024-01-10 and 2024-05-29), the CFO changed on 2026-09-03, and ARR growth fell through all of it.
- **[E2-45] the attacker's test:** the filer answers it: *"as our market becomes increasingly driven by cloud-based solutions,
  native cloud providers may enter this market and provide competitive offerings at lower prices"*, and *"Many of our competitors
  and potential competitors have greater name recognition, longer operating histories, more established customer relationships,
  larger marketing budgets, and greater resources than we do"* (FY2026 10-K Item 1A). An attacker with Microsoft's or
  ServiceNow's installed base does not need to beat UiPath's robot; it needs to be included.
- **[E4-36] which cause of success:** wave-riding. The ARR growth series (59%, 30%, 22%, 14%, 11%) is the wave's shape.
- **[E4-23] key person:** the founder holds about 84% of the votes (Q3) and returned as CEO in 2024 to restore growth. The filings
  do not show that the economics depend on him. Not recorded as a moat defect.

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** · not price-regulated **[x]**
- Class: **[ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL** as a franchise; a real installed base with some switching friction
  (net retention still above 100%), in a market the filer says is served by cheaper, bundled and free alternatives. Direction:
  **narrowing** on the company's own retention series [E4-32].
- **VERDICT: [x] OUT, ON THE BUSINESS. Permanent.** Criterion (2) of **[E3-03]** fails on four independent records: the
  company's own Item 1A in five consecutive 10-Ks (*"Some of our competitors offer their on-premises or SaaS solutions at a lower
  price, which has resulted in, and may continue to result in, pricing pressures"*; free open-source alternatives; bundled and
  integrated alternatives; AI agents that let customers *"build software internally that would have otherwise been purchased"*);
  a named competitor's own 10-K (SS&C lists Microsoft, Pega, UiPath, Appian, n8n and Lyzr as the field); the company's own
  retention series (145% to 107-109%, customers flat for four years, net new ARR down five years running); and a record with no
  price increase in it. **[E4-04]** fails too: the company says it is replacing its basis (rule-based robots to *"agentic
  automation"*) with continuous R&D and acquisitions. **The file closes here.** Q3 to Q6 are recorded below, **not governing**,
  as recent runs have done.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(RECORDED, NOT GOVERNING: the file closed at Q2)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution** **[E3-38, E3-43]**: Q2 found a business, not a franchise, in a market the filer calls *"increasingly
  competitive"* and *"rapidly changing"*; *"a business, unlike a franchise, can be killed by poor management"* [E3-43].
- [ ] **Control** **[E1-16]**: not the buyer's case (a minority purchase). **Recorded instead as the minority holder's
  position:** Daniel Dines holds every Class B share at 35 votes each, *"approximately 84% voting power"* at 2026-01-31, and
  *"has the ability to control the outcome of matters requiring stockholder approval, including the election of directors"*
  (FY2026 10-K Item 1A). An outside holder cannot change management; the only remedy is to sell [E4-24].
- [ ] **Leverage** **[E3-29]**: no debt; $1,405.5M of cash and securities at 2026-07-31.
- **Case declared: GATE (daily execution).** No price would compensate a failure here.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
- **2020-2022, the pre-IPO material weakness** (public in the S-1, 2021; restated in the auditor-change 8-K of 2022-04-20):
  *"improper allocation of stand-alone selling price and certain errors in deferred revenue and contract asset"* for FY2018,
  *"caused by, among other things, a lack of oversight and technical competence"*; *"remediated"* by 2021-01-31. Disclosed
  by the company in its own filings; no restatement of public-company figures followed. **Not a disqualifier; a prompt, read.**
- **2023-09-06, the 2023 Securities Action** (SDNY; class period 2021-04-21 to 2022-09-27; statements *"regarding UiPath's
  competitive position and its financial results"*): Securities Act claims dismissed 2024-11-04; the third amended complaint
  dismissed in its entirety 2025-10-02; appeal filed 2026-02-09 (Q2 FY2027 10-Q Note 10). **An allegation dismissed twice
  is not a finding.**
- **2024-06-20, the 2024 Securities Action** (SDNY; class period 2023-12-01 to 2024-05-29, statements about the AI platform
  and *"customer demand"*): dismissed 2025-07-23; second amended complaint filed 2025-09-12 naming the former CEO and the then
  CFO; motion to dismiss filed 2025-10-27, undecided at the 10-Q. Derivative suits stayed. **Pending; allegations, not
  findings.** The class period ends on the day the company cut its FY2025 guidance by about 10% and announced the CEO's
  resignation (EX-99.1 and 8-K of 2024-05-29), which is the fact pattern the complaint rests on; the run reads that fact from
  the company's own filings (below), not from the complaint.
- **Related parties (DEF 14A 2026):** the company charters an aircraft Dines owns through an LLC, at a rate *"at or below
  market rates"*, $2,555,513 in FY2026; a relative (Aharon Dines) is employed at $169,492 plus $108,290 of options. Disclosed,
  small, priced to market on the company's own analysis.
- **No regulator's finding, consent order or admitted misconduct found** in the 10-K, 10-Qs or 8-Ks read.
- **Binary: no disqualifier found.** Written as [E5-17] requires: the absence of found disqualifiers, not a finding that the
  managers are honest.

### THE INCENTIVE READ **[E4-27]**
- The CEO *"opted to receive nominal remuneration"* (DEF 14A 2026); his interest is his stake, which aligns with owners on
  value and not on control.
- **The other officers' new awards vest on the share price alone** (8-K 2026-09-03: 3,075,000 PSUs to four officers *"subject
  to (i) two stock price hurdles that must be satisfied by July 31, 2029 and July 31, 2031"*; 5.3 million PSUs in all, 10-Q
  Note 16). Pay tied to the quote, not to what the capital earns, is the premise [E3-50] disagrees with; a prompt, not a finding.
- The founder's entity adopted a 10b5-1 plan on 2026-07-15 to sell up to 5,000,000 shares, disclosed by the company in advance
  (8-K 2026-09-03), which is the candid form of an insider sale.

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [ ] weak accounting: none found. KPMG since FY2023 after a no-disagreement change (Step 0).
- [ ] unintelligible footnotes: none found; the revenue, ARR and retention definitions are stated in full.
- [x] **trumpeted projections [E4-22, E5-30]:** quarterly and full-year guidance on revenue, ARR and non-GAAP operating
  income in every Q4 release since FY2022. **Against outturn [E3-48]** (initial full-year guide at the Q4 release, then the
  10-K): FY2023 revenue $1,075-1,085M guided, **$1,058.6M actual (missed)**, ARR met; FY2024 revenue $1,253-1,258M guided,
  $1,308.1M actual (beat); **FY2025 revenue $1,555-1,560M, ARR $1,725-1,730M and non-GAAP operating income ~$295M guided, cut on
  2024-05-29 to $1,405-1,410M, $1,660-1,665M and ~$145M, the same day the CEO resigned; actual $1,429.7M** (8% below the first
  guide); FY2026 guided $1,525-1,530M, $1,610.6M actual (beat). **Two of four initial full-year revenue guides missed (FY2023, and FY2025
  after a mid-year cut), two beaten.** [E5-30]'s ratchet is on record: a guidance culture that has missed once badly.
- [x] **serial share issuance [E5-15], gross not net:** the 2021 Plan reserve *"will automatically increase on February 1 of each
  year ... in an amount equal to (1) 5 % of the total number of shares ... outstanding"* to 2031; RSU settlements of 17.7M, 15.4M
  and 13.6M shares (FY2024-26, equity statement). **The net count fell** (556.6M at 2023-01-31 to 521.2M at the 2026-09-03 cover,
  -6.4%) **only because $1,091M of cash went to buybacks** (FY2024 $102.6M, FY2025 $390.8M, FY2026 $329.1M, H1 FY2027 $268.5M)
  and about $273M more to withholding taxes on vesting awards (FY2024 $112.7M, FY2025 $77.8M, FY2026 $59.1M, H1 FY2027
  $23.2M). The owner's cost of the stock pay is the cash that retired it.
- [x] **adjusted-earnings promotion [E4-29]:** EBITDA never appears (grepped, nineteen releases). **The fifth flag fires in
  its adjusted-earnings form**: the only guided profit line is *"Non-GAAP operating income"* ($445M guided for FY2027; FY2026
  actual $369.8M against GAAP $56.8M), which excludes stock pay, the expense that consumed 206% of operating cash over five
  years; the company's own reason for not reconciling the guide is *"the effects of stock-based compensation expense"*
  (EX-99.1 2026-09-03). **"Non-GAAP adjusted free cash flow"** adds back *"cash paid for restructuring costs"* and employer
  payroll taxes on equity (definition, same release) although restructuring cash recurred in FY2025 and FY2026 ($15.3M,
  $14.1M): the except-for flag [E2-57, E5-33].
- [ ] filed-figure tells [E4-30]: cash taxes $9.8M on $100.6M pretax in FY2026, but loss carry-forwards and the valuation
  allowance release explain it; not smooth growth (the record is lumpy). Not fired.
- [ ] **[E2-49] metric withdrawal: checked, NOT fired.** ARR and dollar-based net retention are reported in every release FY2022 to Q2 FY2027 (grepped);
  customers above $100K and $1M and the total customer count in every 10-K FY2022-26; the ARR definition gained exclusions in
  FY2025 (*"nonrecurring rebates"*, *"one-time discounts"*), which narrow it, announced in the definition itself. Appian, a
  peer, did withdraw its retention metric in 2025 (Q2 row); UiPath did not. The prior's tally: fired at SHOP, MRVL, PAY, ARM,
  CALX, BE; failed at QLYS, CRM, CORT, PLTR, INOD, and now PATH.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Net income over average equity -17.1% / -4.6% / -3.8% / 14.4% (FY2023-26), 5.1% on pretax FY2026 (Q2, [E3-46]). No year earns
the corpus's test; the one positive year is carried by a tax release. [E3-54]'s retention test cannot run: there are no retained
earnings (accumulated deficit $1,705.5M).

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
The 10-K and releases state the ARR and retention definitions, show GAAP beside non-GAAP on every line, quantify restructuring
charges, and disclose the founder's plan to sell in advance. Against that: the headline profit number excludes the largest
cost, and the company stopped naming its competitors after the FY2023 10-K (the FY2024-26 10-Ks list categories; the
named companies that remain are integration partners) while its retention fell. **Mixed; no finding.**

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08, E4-31, E5-24]:** condition (1) passes ($1.4bn of cash, no debt). **Condition (2): the prices paid**, from
  the equity statements, were about **$17.57** (FY2024), **$12.34** (FY2025), **$10.96** (FY2026) and **$11.36** (H1 FY2027) a
  share, against owner earnings that were negative on the five- and three-year means (Q4). No conservatively calculated value
  this run can build puts those prices at a material discount. **CAPITAL-ALLOCATION FLAG, with the humility clause [E4-13]:**
  management knows the business better than this run does, and *"many CEOs never stop believing their stock is cheap"*
  [E5-08]. The flag binds position size, never the rate. Much of the spending is better read as the cash cost of the stock pay
  (above) than as a discretionary purchase.
- **[E2-30] institutional imperative:** (2) projects materialise to soak up funds: two AI acquisitions in twelve months ($24.8M
  and $149.4M cash) and an investment in a private AI company ($35.8M); prompt only. (4) peer imitation: the rename of the
  category to *"agentic"* tracks the industry; prompt only. (1) and (3) not observed.
- **[E3-58] delegation:** no banker-led serial M&A found.

### THE GUARDRAIL
- [x] Nothing here promotes the name; a strong Q3 could not repair Q2 [E2-37, E2-38, E3-39].
- [x] No key-person moat defect recorded at Q2 (the filings do not show the economics depend on Dines).
- [x] Not a manager-as-the-plan case: there is no intact franchise for a manager to defend [E2-35, E2-36].

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary (no disqualifier found; [E5-17]'s cap applies), GATE case, with
  three flags live as prompts** (guidance record with a mid-year cut, gross issuance retired with cash, adjusted-earnings
  headline excluding stock pay) **and a capital-allocation flag on buybacks.** The pending 2024 Securities Action is a
  monitoring item; its resolution is a future document, not an existing one, so it is not a work order.

## Q4 — WILL IT SURVIVE? *(RECORDED, NOT GOVERNING)*

### Owner earnings — the one number **[E2-23]**
Built from the filed faces (`oe.py`, `oe_out.txt`): operating cash, less stock pay, less (c). **(c)** = purchases of property
plus capitalised software (FY2022 only; none capitalised since), with D&A as the default end [E3-44, E2-41]; **not the capital-
intensive class** (capex $7-24M a year, 0.5-1.5% of revenue; no filing says depreciation understates renewal), so both ends are
valid and they nearly coincide. **The working-capital increment** is inside operating cash; the `working_capital_flag` prompt
(FY2023 deferred revenue $160.7M against operating cash of -$10.0M) was read: FY2023's cash was depressed by bonuses,
restructuring and payroll taxes on equity (10-K MD&A), and the deferred-revenue build helped rather than hurt; the five-year
mean carries it. **Stock pay** is subtracted in full [E5-06]; because it ran **205.9% of operating cash over five years (103.0%
over three)**, the grant table was read by hand [E3-70] (RSUs, options and PSUs granted x weighted grant-date fair value,
equity-award notes of each 10-K): grant value $982M, $538M, $379M, $359M, $232M (FY2022-26), and **$148M in H1 FY2027 alone**,
plus 5.3M PSUs on 2026-09-03 not yet valued. The column below uses the larger of charge and grant value per year.

| $M | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|---:|
| Operating cash | -55.0 | -10.0 | 299.1 | 320.6 | 371.2 |
| Stock pay, charge | 515.6 | 369.8 | 372.0 | 358.2 | 290.7 |
| Stock pay, grant value | 981.5 | 537.6 | 378.9 | 359.1 | 231.7 |
| (c) capex end / D&A end | 11.8 / 14.7 | 23.8 / 18.7 | 7.3 / 22.6 | 14.9 / 17.2 | 19.0 / 17.0 |
| **Owner earnings, capex end** | **-582.4** | **-403.6** | **-80.2** | **-52.5** | **61.5** |
| Owner earnings, larger stock-pay measure | -1,048.3 | -571.4 | -87.2 | -53.5 | 61.5 |

- **Five-year mean (FY2022-26):** **-$211.5M** capex end, -$214.1M D&A end, **-$339.8M** at the larger stock-pay measure,
  -$220.4M with cash acquisitions charged.
- **Three-year mean (FY2024-26):** **-$23.7M** capex end, -$28.9M D&A end, -$26.4M larger measure, -$32.0M with acquisitions.
- **Twelve months to 2026-07-31:** operating cash $373.2M, stock pay $234.6M, capex $10.3M: **$128.4M** capex end ($112.7M D&A
  end, which now carries WorkFusion's intangible amortisation). At the H1 FY2027 grant run-rate ($296.5M a year) instead of
  the charge: **$66.4M.**
- **Combined range: about -$340M to +$128M.** It spans zero. **The spread is a finding [E5-11]:** the five-year window holds two
  years of heavy post-IPO grants (FY2022-23); the favourable breaks are the falling grant prices (RSU grants fell only from 19.3M
  to 16.8M a year while the weighted grant price fell by a third, $16.95 to $11.36) and the FY2026 tax release, which is outside owner earnings anyway [E4-41].
- **Is the range too wide to reach a conclusion? Yes [E4-25].** The owner has never been paid on a multi-year mean; one year
  and one trailing twelve months are positive.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · [ ] good · [x] **gruesome-shaped on the five-year record at the owner level**: it grew (revenue +16% a year) while
  the owners paid for the growth in stock worth 206% of operating cash, and then paid $1.09bn in cash to retire the shares, for
  owner earnings that averaged below zero. FY2026 is the first year that paid. Recorded, not governing.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **NO** on the five-year record (one positive year).
- (2) massive liquid assets: **YES**, $1,405.5M of cash and securities at 2026-07-31, 20% of the cap, no debt.
- (3) no significant near-term cash requirements: **YES**; leases and a discretionary $500M buyback authority (March 2026);
  no maturities. Leverage: none [E4-16]. **Two of three.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism, in the bear's own terms:** AI agents and the platforms that bundle them (the filer's *"native cloud
  providers"*, *"coding agents"*, *"open source alternatives ... at no cost"*) do the clerk's job without a screen-driving
  robot, customers build instead of buy (*"the ability to build software internally that would have otherwise been
  purchased"*), and net retention crosses below 100%: the installed base starts to shrink while the sales force it takes to
  hold it ($683M a year, 42% of revenue) does not.
- **Quantified from filed figures:** at 95% net retention, ARR of $1.94bn loses about $97M a year from existing customers;
  new customers added at FY2026's pace (15% of that year's $180.9M revenue growth, about $27M) leave a fall of about $70M a year; with 83% gross margin and operating costs of $1.28bn, the FY2026 operating
  profit of $57M becomes a loss within a year and owner earnings return to the FY2023-25 range. The cash ($1.4bn) and the absence
  of debt mean the company does not fail; **the owner's return does**, which is how this business dies.
- **Likelihood: [x] a real possibility.** Retention fell or held for fifteen quarterly releases, 145% to 107%, before turning
  to 109%.
- **VERDICT (RECORDED, NOT GOVERNING): [x] UNKNOWABLE.** Owner earnings span about -$340M to +$128M across windows and stock-pay
  measures [E4-25]; strength (1) fails. *Can I name the document that would resolve it? No: the answer is whether AI agents
  displace this product over the next five years, which no filing contains.* **A later instance of shape #2, EARNS NOTHING FOR OWNERS AFTER
  PAYING ITS PEOPLE** (`Screens/SURVIVAL SHAPES - index.md`: stock pay 205.9% of operating cash FY2022-26 on the charge), as the
  mechanism; the substitution named above is how #2 would persist. No new shape.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** It did not open: Q2 OUT. What follows is arithmetic only.

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Headed as operator rule 3 requires; no entry language; no ranking.*
- **Cap:** US$6.978bn (Step 0; about $7.44bn with unvested awards). Cash and securities $1.405bn, no debt, so about **$5.57bn**
  for the operations. **Sovereign:** 5.34% (US Treasury, 09/18/2026). **Floor:** ~10% [E4-28].
- **Yield, owner earnings / cap:** five-year **-3.0%** (capex end) and **-4.9%** (larger stock-pay measure); three-year
  **-0.3%**; twelve months **1.8%** (capex end), the best figure the filings support; on the operations alone, 2.3%.
- **What the price assumes:** a 10% expectancy on the cap needs about **$698M a year** of owner earnings ($557M on the
  operations), **5.4 times** the best twelve months ever filed and more than the company has ever produced in operating cash.
  Reaching it by 20% annual growth takes about nine to ten years; [E4-35]'s base rate is that fewer than one in twenty of the most
  profitable companies sustain 15% for twenty years, and this one's ARR growth is 12% and has fallen for five years.
- **Value, no growth, at the floor, round numbers [E4-01]:** about **$1.3bn** for the operations on the best twelve months, plus
  $1.4bn of cash: about **$2.5-3bn** against **$7.0bn**. The ceiling [E2-63]: the product's price is set against cheaper and
  free substitutes (Q2).
- **Bar:** none chosen; no margin applied; windage count zero. **VERDICT: none. Q5 did not open (Q2 OUT).**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? *(RECORDED, NOT GOVERNING)*

**Nothing is armed.** No band, no PORTFOLIO row: a Q2 OUT is a finding about the business (the QLYS ruling). **The reversal
condition, in words, pre-committed [E1-02]:** reopen Q2 only if (1) the 10-K's Item 1A drops the sentence that lower-priced
competitors *"has resulted in"* pricing pressure, **and** (2) a filed price increase holds for three years with net retention
above 115% and the customer count growing again, **and** (3) the peer row shows UiPath's owner cash per dollar of revenue at or
above Pegasystems' for three years, **and** (4) at least one named competitor's 10-K stops listing UiPath among its substitutes
while UiPath's AI products are shown in the filings to extend, not replace, the robot base. The monitoring question [E3-30,
E4-17] does not arise for an unowned name.

**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. The file closed at Q2 (OUT); Q3-Q6 are labelled RECORDED, NOT
      GOVERNING in every heading and verdict line.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed ARR, retention,
      customer and revenue series, FY2022 to Q2 FY2027; the excluded parts (agentic AI products; whether AI agents displace
      robotic automation) are named as outside the circle, not as caveats on the IN. Q3's IN is recorded, not governing.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none is used for a governing verdict. NICE Ltd.'s filing
      is named as an unfetched peer that cannot move the Q2 verdict.
- [x] Every UNKNOWABLE verdict states what cannot be known (Q4, recorded: whether AI agents displace the product over five years;
      the range -$340M to +$128M spans zero [E4-25]).
- [x] Step 0: the filing was read, with accession numbers; operating cash, stock pay, D&A, capex and revenue cross-checked against
      the FY2026 10-K face; FY2022-23 from the FY2024 and FY2022 10-K faces; the cover count against the 10-Q balance sheet.
- [x] Owner earnings on multi-year means (five and three years, plus twelve months); windows stated; (c) disclosed as a judgment
      with both ends; stock pay subtracted in full, and because it exceeded 50% of operating cash the grant table was read by
      hand and the larger of charge and grant value shown [E3-70].
- [x] Competitor row filled from four SEC filers' own filings (APPN, PEGA, NOW, SSNC) beside PATH; the unavailable peers named
      with the reason (Microsoft unsegmented, six not on the SEC ticker list, NICE not fetched) and why the class is not PROVISIONAL.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury par yield curve), dated 09/18/2026;
      `sources.sovereign()` stale and not used.
- [x] Value stated as a round-number range (about $2.5-3bn no-growth at the floor), and only as a COMPUTATION - NOT A CLEARANCE.
- [x] One bar chosen, not both: none, because Q5 did not open; windage count zero.
- [x] Prices dated; aggregator (Yahoo) used for the live quote only, flagged, corroborated by two Form 4 sale ranges.
- [x] Run committed to git (template `71c902c`, Step 0 `2d80237`, Q1-Q2 `a022bfd`, Q3-Q6 with audit and register in the next
      commit, fold after).

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
All caught before the text they affected was committed in final form, except the first two, which were committed in Step 0
(`2d80237`) and corrected in the Q1-Q2 commit (`a022bfd`).
1. **The executive PSU count.** Step 0 first carried *"3,375,000 executive PSUs"* from an addition of the 8-K's four named awards;
   the four sum to **3,075,000**, and the 10-Q's Note 16 gives **5.3 million** granted in all on 2026-09-03. Dilution beside the
   cap was corrected from 32.2M (6.2%) to 34.1M (6.6%) and the diluted cap from $7.41bn to $7.44bn. The Step 0 commit `2d80237`
   carries the first figure; history is not edited.
2. **Note numbers cited from memory of DASH's filing.** The Step 0 draft cited 10-Q Notes 5 and 11 and 10-K Note 2; the filings'
   own numbering is Notes 6 (acquisitions) and 12 (equity awards) in the 10-Q and Note 3 (geography) in the 10-K. The 10-Q note numbers
   are in `2d80237`; corrected in `a022bfd`.
3. **Four Q1-Q2 claims drafted ahead of their evidence**, each then tested: that UiPath *"charges per robot and per user"* (no
   filing states the unit of price; replaced with what the filing says); that net retention *"fell in every one of eleven
   consecutive quarters"* (it fell or held for fifteen, with three flat readings); that the company *"restructured four times in
   four years"* (three reductions, the fourth 2.05 filing amends the third); and that it *"changed CEO twice"* (three changes to
   the office, read from the 8-Ks). Also removed: a claim that Kofax is "Tungsten Automation" and that NICE files a 20-F, both
   from memory. **Operator rule 6 in small: nothing written until its evidence exists.**
4. **The survival shape.** The Q4 draft labelled PATH a later instance of *"#11 (a spread that crosses zero)"*; #11 in the index
   is THE PASS-THROUGH. Read against `Screens/SURVIVAL SHAPES - index.md`, PATH is a later instance of **#2** only.
5. **The release count** was first written as seventeen; nineteen EX-99.1s are on disk (the 2022-11-14 8-K carries none).
6. **A shell heredoc failed** on the Step 0 text; the section was written with the Write tool instead. No file was affected.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
- None that changed a number. The brief's prior (a dimensioned per-class cover, META or DASH kind) held, in META's two-class form
  with no zero class; `stateOfIncorporation` (DE) matches the filings, so the DASH charter check found nothing.
- **One thing the brief could not have known:** unlike DASH, the share count was not the only obstacle the triage met. The
  `a8bc84f` `owner_earnings()` is negative at every end for PATH, so the name would have been priced at a negative yield even
  with a count.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`sources.sovereign("USD")` served the cached 09/17 row (5.29%) again**; the ninth recorded occurrence across runs.
- **`cover_shares.py` was not needed**: the two dimensioned dei facts were read directly from the inline XBRL (`dei.py`).
- **The SEC `index.json` endpoint returned HTTP 503** for the 2021 charter 8-K; the exhibit was fetched by its document name
  directly. A retry with a longer wait may be enough; not changed.
- **`floor_screen.capital_acquired` for FY2022** includes capitalised software ($2.95M) and matches the face; from FY2023 the filer
  capitalises none, so the capex end and the D&A end nearly coincide. No defect; recorded so a reader does not look for one.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A tense in Item 1A can be a finding.** Most competition risk factors are conditional (*"may"*, *"could"*). UiPath's has carried,
unchanged for five 10-Ks, a sentence in the past tense: lower-priced competitors *"has resulted in"* pricing pressure. A filer that
reports a realised effect in its risk factors has stated a fact about substitutes, and [E3-03]'s second criterion can be read
from it directly. Grep Item 1A for past-tense verbs before scoring Q2.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- **One line:** PATH FAILS at Q2 (OUT, on the business): criterion (2) of [E3-03] fails in the company's own words across five
  10-Ks (lower-priced competitors *"has resulted in"* pricing pressure; free open-source, bundled and build-it-yourself AI
  alternatives), in a named competitor's 10-K (SS&C lists Microsoft, Pega, UiPath, Appian, n8n and Lyzr), in the retention series
  (145% to 107-109%, customers flat about 10,750 for four years, net new ARR down five years running) and in a record with no
  price increase; [E4-04] fails because the company says it is replacing its basis (rule-based robots to agentic automation).
  Q1 IN. Price US$13.39 (2026-09-18 close); 521,155,409 shares (A 456,464,703 + B 64,690,706, Q2 FY2027 10-Q cover
  `0001734722-26-000050`); cap US$6.978bn; sovereign 5.34% (US Treasury, 09/18/2026). Q3-Q6 recorded, not governing: Q3 IN on
  the binary with flags (a GATE case), Q4 UNKNOWABLE (owner earnings about -$340M to +$128M), Q5 computation only (yield -4.9% to
  1.8% against 5.34% and a ~10% floor).
- **If UNRESEARCHED - THE WORK ORDER:** not applicable to the governing verdict.
- **If UNKNOWABLE:** not applicable to the governing verdict.
