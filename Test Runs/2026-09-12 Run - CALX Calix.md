# Company Run — Calix, Inc. (CALX) — 2026-09-12
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Write-early protocol: this file was created before any filing was read. Sections are
appended as each closes and committed after each gate.*

---
## THE SCREEN ROW THAT PROMPTED THIS RUN — a prompt to read, never a score (operator rule 8)

```
cap_m 2378 | oe_bottom_m -6 | oe_top_m -5      <-- BOTH ends NEGATIVE; spread_dollars $-6M to $-5M
yield_bottom -0.25% | vs_sovereign -5.60 pts | growth_required: n/a - negative bottom
level_shift n/a (early half straddles zero) | level_shift_oe n/a (runs from -$83.2M) | 17 years filed
best_year_dep 0.321 "ONE YEAR CARRIES THE WINDOW"
wc_note: FIRES - accounts payable moved by 45% of a year's operating cash
newest_filing 2025-12-31   newest_periodic 2026-06-27
```

Every one of those numbers is re-derived below from the filed statements. Where the
re-derivation disagrees with the row, the filing governs (operator rule 4).

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
- rate **5.35 %** · date **2026-09-11** · source **US Treasury daily par yield curve, 30-year,
  home.treasury.gov (the issuing authority; FRED is the fallback, not the source)**, struck via
  `tools/sources.py` on 2026-09-12. *(The brief quoted the 2026-09-10 print of 5.37%; the
  2026-09-11 print is 5.35% and that is the one used.)*
- FX: none. Calix is a Delaware corporation reporting in USD; the earnings currency is USD
  (geographic split recorded at Q1).

**Shares — read off the cover of the LATEST periodic filing, by hand and by tool:**
`python Screens/cover_shares.py CALX`:
```
CALX  CALIX, INC
   10-Q filed 2026-07-21, period 2026-06-27, accession 0001406666-26-000034
   Common Stock, par value $0.025 per share             62,963,989
```
One class only; no preferred; no convertible. **62,963,989 shares.**

**Price** (aggregator, flagged per operator rule 5 — live quotes only): **$35.24**, close of
**2026-09-11**, Yahoo Finance via `tools/sources.py`, struck 2026-09-12.
**Market capitalisation = 62,963,989 × $35.24 = $2,218.9M.** *(The screen row carried
`cap_m 2378`; the difference is price, not the count.)*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for FY2025, filed 2026-02-20, accession
  `0001406666-26-000005`, primary document `calx-20251231.htm`** (period 2025-12-31). Also read in
  full: 10-K FY2024 (`0001406666-25-000008`), FY2023 (`0001406666-24-000012`), FY2022
  (`0001406666-23-000026`), FY2021 (`0001628280-22-003338`), FY2020 (`0001406666-21-000029`),
  FY2019 (`0001406666-20-000018`), FY2018 (`0001406666-19-000029`), FY2016
  (`0001406666-17-000012`), FY2015 (`0001406666-16-000041`), FY2013 (`0001406666-14-000039`),
  FY2012 (`0001406666-13-000010`), FY2010 (`0001193125-11-045511`); 10-Q Q2 2026
  (`0001406666-26-000034`, period 2026-06-27); DEF 14A 2026 (`0001406666-26-000006`); and nine
  8-Ks with their EX-99.1 releases and EX-99.2 stockholder letters, 2025-01-29 through 2026-07-20.
- figure cross-checked against the filed statement: **operating cash flow FY2025 =
  $134,953 thousand**, read off the Consolidated Statements of Cash Flows at page 44 of the FY2025
  10-K, agreeing to the dollar with XBRL tag `NetCashProvidedByUsedInOperatingActivities`. Also
  cross-checked by hand: SBC $87,929k, D&A $17,710k, purchases of property and equipment
  $19,435k, and the FY2023 and FY2022 columns of the same statement as filed in the FY2023 10-K
  (OCF $56,251k and $27,183k).
- **A NOTE ON WHAT IS NOT IN THE CASH-FLOW STATEMENT — the brief's prior, refuted at the line
  level.** The brief expected **capitalised software development** to be one of the two lines
  taking operating cash flow to a negative owner-earnings figure, and warned that the HAS/CRWD
  defect had omitted it from (c) entirely. **Calix capitalises no software development.** The
  investing section of the Consolidated Statements of Cash Flows contains exactly four lines —
  purchases of property and equipment, and purchases, sales and maturities of marketable
  securities — in every one of the twelve filed cash-flow statements read. No
  `PaymentsToDevelopSoftware`, `PaymentsToDevelopComputerSoftware` or
  `CapitalizedComputerSoftwareAdditions` tag exists in the companyfacts file for any of the 17
  years 2009-2025. The only two capitalisations Calix makes are **deferred sales commissions**
  (unamortised balance $20.7M at 2025-12-31, amortised $11.2M in 2025 — a contract-cost asset
  inside operating activities, not investing) and a **tax** capitalisation of R&D under IRC §174,
  which appears only as a deferred-tax asset ($78.8M at 2025, $110.6M at 2024) and moves no cash.
  R&D of $190.4M is expensed in full, above the operating-cash-flow line. **One line, and one only,
  takes OCF negative: stock-based compensation.** Recorded here because the brief asked the question
  and the answer is an absence.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Calix buys finished electronic boxes
from contract manufacturers and original-design manufacturers — it owns no factory — and sells
them to companies that sell broadband subscriptions. Two kinds of box: one that sits in the
operator's building at the edge of its fibre network and terminates many subscriber lines
(the E-Series, what the industry calls an OLT), and one that sits in the subscriber's house and
terminates one line and radiates Wi-Fi (the GigaSpire/GigaPro family, an ONT plus a router).
On top of the boxes it sells a hosted software subscription that reads telemetry off those
boxes and presents it to the operator's marketing, support and network staff, plus a set of
consumer services the operator resells to its own subscribers (parental controls, security,
community Wi-Fi, a small-business package). **The boxes are 82.6% of revenue and the software
and services 17.4%** (FY2025: appliance $825,649k, software and service $174,361k, total
$1,000,010k — the first billion-dollar year in the company's history). Gross margin 56.8%
consolidated, 55.5% on appliances and 62.9% on software and service.

The customer is overwhelmingly a **small** operator. The only year Calix ever disclosed the split
in dollars — FY2024, and it disclosed it once and then withdrew it, on which see Q3 — the
mix was **Large $50,776k · Medium $123,977k · Small $656,765k**, i.e. **79.0% of revenue from
operators with fewer than 250,000 broadband subscribers.** The 10-K describes that class as
"over 1,000 predominantly local IOCs … municipalities, cable MSOs, electric cooperatives, fiber
overbuilders, tribal entities and WISPs", ranging "from a few subscribers to 250,000".
**Geography: 93% of revenue is the United States** (2025), 92% in 2024, 91% in 2023 and 2022,
83% in 2021. Non-US revenue is 7% and has fallen every year since 2021's 17% — while the same
filing says "we will increase our attention on international markets."

So the money is made by taking a margin on hardware sold into the capital budget of about 1,600
small American telephone, electric and municipal broadband operators, most of whose fibre
build is paid for by a federal subsidy programme. The 10-K names the number: **"The U.S. Federal
government has approved programs, totaling more than $40 billion, to fund broadband and
connectivity expansion across the rural parts of the U.S. Calix has a dedicated team of funding
specialists."** A vendor with a dedicated team of subsidy specialists has told you where the
demand comes from.

**Customer concentration.** "No customer accounted for more than 10% of our revenue for 2025,
2024 or 2023." That is true now and it is the *end* of a story, not the absence of one. The
filed series, read across nine annual reports:

| FY | largest customer, % of revenue | who |
|---|---|---|
| 2016 | **21%** | CenturyLink |
| 2017 | **31%** | CenturyLink |
| 2018 | **18%** | CenturyLink |
| 2019 | **15%** | CenturyLink |
| 2020 | **11%** | Lumen (same company, renamed) |
| 2021 | below 10% | — |
| 2022-2025 | none above 10% | — |

Concentration did not diversify away; **one customer went from nearly a third of revenue to
nothing in four years**, and gross margin collapsed to 33.9% in the year that customer was 31%
of revenue (see Q2). Concentration also survives in the receivable: Note 11 discloses **one
customer at 12% of accounts receivable at 2025-12-31 and another at 23% at 2024-12-31.**

**The scarce input this business controls.** I cannot name one that Calix controls. It owns no
fabs and no factories (CMs and ODMs make everything); it holds **98 US patents** against
competitors that hold tens of thousands; its engineers sit in San Jose, Petaluma, Nanjing,
Bangalore, Minneapolis and Richardson and "we also outsource a portion of our software and cloud
development to domestic and international third parties and depend on these partners to meet our
development plans." The nearest thing to a scarce input is the **installed base of ~1,600
operator relationships and the telemetry that runs through the deployed appliances**, which is
the bull case at Q2 and is tested there. It is not a scarce input in the sense the framework
means: nothing prevents a competitor from selling the next OLT into the same building.

**Is revenue units or price? [E2-63]** It is **units**, and the units are boxes shipped into a
subsidised build cycle. Every explanation the filer gives for a revenue movement is a volume or
a mix explanation and never a price one — FY2025's increase is "the adoption of our platform …
by new customers as we continue to take footprint from legacy box vendors and the continued
robust expansion of our appliances within our existing customer base"; FY2024's 20% decline is
"delayed purchasing decisions of our appliances as our customers evaluated and prepared for
various government stimulus programs." The software half is explicitly per-unit too: **"Our
software is sold on a per-subscriber basis."**

**DOES A UNIT OR CUSTOMER SERIES EXIST? [E4-55] — YES, IT EXISTS, IT PEAKED IN 2022, IT FELL,
AND IT HAS BEEN FROZEN FOR THREE YEARS.** This is the sharpest thing in Q1 and it is built
entirely from the Item 1 of successive annual reports:

| FY | filed active-customer count | filed adds that year |
|---|---|---|
| 2010 | "more than 600 customers" | |
| 2012 | "more than 1,150 customers" | |
| 2013 | "over 900 customers" *(fibre deployers; the base changed)* | |
| 2015 | "over 1,000 customers" | |
| 2016 | "over 1,300 customers" | |
| 2018 | "over 1,500 customers" | |
| 2019 | "approximately 1,600 customers" | |
| 2020 | "approximately 1,600 CSP customers" | **"we added 87 CSP customers"** |
| 2021 | "approximately 1,700 BSP customers" | **"we added 130 BSP customers"** |
| 2022 | **"approximately 1,900 customers"** | "over 100 new BSP customers per year for the past three years" |
| 2023 | **"approximately 1,600 active … customers"** | *(no annual add figure)* |
| 2024 | **"approximately 1,600 active … customers"** | *(no annual add figure)* |
| 2025 | **"approximately 1,600 active … customers"** | "we have averaged landing 80 new customers per year" (five-year average) |

Two facts sit in that table. First, **the count peaked at approximately 1,900 in FY2022 and was
approximately 1,600 in FY2023 — a fall of about 300 customers, roughly 16%, in one year — and
has not moved since.** Second, and in the same Item 1 that reports the frozen 1,600, the FY2025
10-K claims "For the past five years, we have averaged landing 80 new customers per year."
**Eighty a year for five years is four hundred customers landed, against a count that is exactly
where it was five years ago.** Either the gross adds are being churned out at the same rate they
arrive, or the ~1,600 is not maintained. The filing does not reconcile the two numbers and does
not acknowledge that they need reconciling. [E4-55]'s Precision Steel lesson is that the
physical series is the honest one and that dollar revenue flattered by something else is how a
shrinking franchise hides; here the physical series has been replaced by a gross-adds average
whose averaging window lengthened (one year → three years → five years) and whose number fell
(130 → "over 100" → 80) as the news got worse. That is also a Q3 matter under **[E2-49]** and is
scored there.

*(Revenue per active customer, for scale: FY2019 ~$265k, FY2022 ~$457k, FY2025 ~$625k. The
dollars per customer are rising while the customer count is not — which is the same sentence as
"the boxes per operator are rising because the operators are building fibre with federal money.")*

**Will the fundamentals look broadly the same in ten years?** Partly. Somebody will still sell
fibre access boxes to American rural operators in 2036. **But the two things that set the size
of this business in 2025 are both dated.** The subsidy programmes are appropriations with end
dates, not a permanent feature: the FY2019 10-K's demand story was the Connect America Fund
("$2.0 billion per year through the end of 2020"), the FY2024 10-K's was customers "evaluating
and preparing for various government stimulus programs", and the current story is BEAD, whose
money is being obligated now. And the product itself has been re-described four times in six
annual reports — "All Platform" (2020), "platform, cloud and managed services" (2022), and in
the FY2025 10-K the business is now "powered by agentic AI" with a "Calix Agent Workforce" of
four agent families, none of which existed in the prior year's filing. [E3-31] asks for
"relatively simple and stable in character." The revenue mechanics are simple. The demand
driver is an appropriation and the product vocabulary changes annually.

**VERDICT: [x] IN** — and it is IN on the narrow ground [E3-31] actually sets. I can state the
unit economics without management's language: a fabless box vendor takes a 57% gross margin on
hardware sold into the subsidised capital budgets of about 1,600 small US broadband operators,
plus a 17%-of-revenue software subscription sold per subscriber on top of the installed boxes.
That is understandable. What is *not* understandable from this filing is how large the business
is in ten years, and that is a Q2 and Q4 question, taken there rather than borrowed forward to
fail Q1.

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired **[x] YES** · no close substitute **[ ] NO — and the filer says so** ·
  not price-regulated **[x] not regulated, with a qualification recorded below**

**THE BULL CASE FIRST, built from the filings, because the brief's prior was OUT and [E4-26]
requires the disconfirming work to be done on my own hypothesis hardest.** The claim to be
tested is that the cloud and managed-services platform is a switching cost that turns a box
vendor into a platform company. Six filed facts support it and they are not trivial:

1. **The software line grew 27% a year straight through a 20% collapse in the hardware line.**
   Software and service revenue: **FY2023 $108,125k → FY2024 $137,371k (+27.0%) → FY2025
   $174,361k (+26.9%)**, from the Consolidated Statements of Comprehensive Income. FY2024 is the
   year *total* revenue fell from $1,039,593k to $831,518k, −20.0%. A line that compounds at 27%
   while the business around it falls a fifth is not a rounding error; it is the single best fact
   in this file.
2. **Its gross margin is the highest thing in the company and it is rising:** software and
   service gross margin **56.3% (2024) → 62.9% (2025)**, against appliance 54.2% → 55.5%.
3. **Remaining performance obligations, the one contracted-backlog instrument Calix discloses:
   $242.5M (2023-12-31) → $325.8M (2024-12-31, +34.4%) → $385.0M (2025-12-31, +18.2%)**, of which
   "39% over the next 12 months and a large majority of the remainder over the two years
   thereafter." A three-year contractual tail on 17% of revenue.
4. **Deferred sales commissions of $20.7M unamortised**, capitalised precisely because "the
   expected amortization period is greater than one year" — independent evidence that the
   subscriptions really are multi-year, not annual renewals dressed up.
5. **Consolidated gross margin is at an all-time high — 56.8% — and it is 2nd of 8 in the
   competitor row, behind only Cisco.** Seventeen filed years: 33.7% (2009), 45.7% (2013),
   33.9% (2017), 49.3% (2020), 49.9% (2023), 54.6% (2024), **56.8% (2025)**.
6. **Share is genuinely being taken from the nearest named competitor.** FY2025 revenue: Calix
   $1,000M at a +2.1% operating margin; ADTRAN $1,084M at **−1.4%**, its seventh consecutive
   operating loss. Calix's own words — "we continue to take footprint from legacy box vendors" —
   are corroborated by ADTRAN's filing, not merely asserted in Calix's.

**AND NOW THE REFUTATION, which is decisive on three separate instruments.**

**(a) [E3-03] CRITERION 2 FAILS IN THE FILER'S OWN WORDS.** Item 1, Competition, FY2025 10-K:
*"The communications software and systems equipment markets are **highly competitive**.
Competition is largely based on any one or a combination of the following factors: functionality
and features, **price**, existing business and customer relationships, product quality,
installation capability, service and support, long-term returns, scalability, development and
manufacturing capability."* It then names **nine** competitors — ADTRAN Holdings, Ciena,
CommScope, eero/Ring (Amazon companies), Harmonic, Huawei, Nokia, Plume Design, Ubiquiti — adds
"In various geographic or vertical markets, there are also several smaller companies with which
we may compete", and closes: *"**Many of our competitors have the financial resources to offer
competitive products at a below market price, which could prevent us from competing
effectively.**"* A company that lists price second among the bases of competition and then says
its competitors can undercut it is not describing a product its customers think has no close
substitute. This is the PLPC precedent (2026-09-07) reached from the same document: the Item 1
closes the gate.

**(b) [E2-44](1) — THE PRICING INSTRUMENT — FAILS, AND IT FAILS ON THE FILER'S OWN ATTRIBUTION
OF ITS BEST-LOOKING NUMBER.** The candidate event is real and is exactly what the test asks for:
**gross margin rose 470 basis points, 49.9% to 54.6%, in the year revenue fell 20%.** Demand
flat-to-falling, capacity underused, margin up. But the FY2024 10-K explains it itself, and none
of its three reasons is price:
> *"The increase in gross margin of 470 basis points … was primarily related to **a charge of
> $28.7 million that we recorded in the fourth quarter of 2023** as we wrote down obsolete
> inventory and accrued a liability for components at suppliers primarily associated with our
> legacy product family… Furthermore, there was **a mix shift** of hardware sales towards small
> customers, which generally have higher gross margins… Additionally, we continued to experience
> **growth in our licenses, cloud and managed services**, which became a greater percentage of
> our total revenue since the overall decline in revenue was related to our appliance revenue."*
Add the $28.7M write-down back to the 2023 base and 2023 gross margin was **52.6%**, not 49.9%;
the real 2024 improvement was about **200 basis points, not 470**, and the filer assigns it to
two mix effects. FY2025's 220bp is attributed the same way — "the continued adoption of our
platform … by new broadband service providers and our CXP customers winning new subscribers" —
volume and mix language again. **Across seventeen annual reports there is not one statement that
Calix raised a price.** Under **[E4-37]**, which measures a moat by the agony of a price
increase, the test cannot even be run: no instance of a price increase was found in the filings
read, and I record that as an absence found, not as an absence proven.

**And the instrument runs the other way with force.** FY2017: gross margin **collapsed from
44.3% to 33.9%** — 1,040 basis points in one year — in the year CenturyLink was **31% of
revenue**, and operating loss went to −$81.6M. **One large customer can take ten points of gross
margin out of this business.** That is the precise inverse of pricing power, and it is filed.

**(c) [E2-44](2) — GROW DOLLAR VOLUME WITH ONLY MINOR ADDITIONAL CAPITAL? YES ON CAPITAL, AND IT
DOES NOT HELP, BECAUSE THE INPUT THAT SCALES IS NOT CAPITAL.** Capital intensity really is
minimal: capex 1.9% of revenue, capex/D&A 1.097 in 2025 and ~1.0 over the whole life, no
factories. But:

| | FY2020 | FY2025 | change |
|---|---|---|---|
| Revenue | $541,239k | $1,000,010k | **+84.8%** |
| Gross profit | $266,791k | $568,316k | +113.0% |
| Gross margin | 49.3% | 56.8% | +750bp |
| Sales and marketing | $94,185k | $248,636k | +164.0% |
| Research and development | $85,258k | $190,356k | +123.3% |
| General and administrative | $44,444k | $108,334k | +143.8% |
| **Total operating expense** | $223,887k (41.4% of revenue) | $547,326k (**54.7%** of revenue) | **+1,330bp** |
| **Operating income** | **$36,846k (6.8%)** | **$20,990k (2.1%)** | **−43.0%** |

**Revenue grew 85%, gross margin gained 750 basis points, and operating income fell 43%.**
Incremental gross profit over the five years was $301.5M; incremental operating expense was
$323.4M. **The last five years of growth cost $22M more to buy than the gross profit it
produced.** This is the [E2-53] refutation shape — position did not carry the economics, and
[E4-20]'s question is asked at Q4 with this table as its evidence.

- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]**
  **Rebuilt, yes.** R&D is 19.0% of revenue and the filing promises more: "We expect our
  investments in research and development to increase in absolute dollars **and as a percentage
  of gross profit** in the short term as we accelerate the development of AI functionality."
  The *description* of the product has been replaced three times in six annual reports — "All
  Platform" (FY2020), "platform, cloud and managed services" (FY2022), and in FY2025 the whole
  business is "powered by agentic AI" with a four-family "Calix Agent Workforce" that did not
  exist in the FY2024 filing. Under [E4-04]'s scope test — does the spending **defend the same
  advantage or buy its replacement** — this is replacement: each generation of silicon and
  software supersedes the last. That is Munger's competitive destruction, and what the record
  actually looks like is **[E3-51]'s surfing run**: revenue $541M (2020) → $1,040M (2023) on
  RDOF and ARPA money, then −20% the moment the money paused. Of **[E4-36]**'s four causes of
  extreme success, this one is **wave-riding**, and the advantage lives in the wave.
- **Primary moat metric, filing-sourced, and its trend:** software-and-service share of revenue
  (10.4% → 16.5% → **17.4%**), rising; and consolidated gross margin (49.9% → 54.6% → **56.8%**),
  rising. **Both point the right way.** Against them: operating margin (6.8% → 2.1%), active
  customer count (~1,900 → ~1,600, frozen three years), non-US share (17% → 7%), and RPO
  momentum (see below) all point the wrong way. **[E4-32]** asks for direction and the direction
  is split; a split direction is not a widening moat.
- **The bull case's own instrument has stalled in the live quarter.** RPO: **$385.0M
  (2025-12-31) → $376.3M (2026-03-28) → $386.4M (2026-06-27)**. That is a **sequential decline,
  the first in the series**, and **+0.4% over six months against +18.2% over the prior twelve.**
  Worse for the switching-cost claim, the *billed* part is shrinking: total contract liability
  (deferred revenue) was **$61.5M at 2023-12-31, $47.6M at 2024-12-31, $50.3M at 2025-12-31** —
  still below its 2023 level three years later. The RPO growth is unbilled commitment, not cash
  collected. And **$385.0M of RPO with 39% inside twelve months is about $150M against $1,000M
  of revenue: roughly 85% of next year's revenue has to be re-won.**
- **The switching-cost claim has no filed instrument at all.** Searched in the FY2025 10-K:
  **no attach rate, no net revenue retention, no ARR, no gross or net churn figure, no subscriber
  count, no dollar-based expansion figure.** The only "churn" in the document is about *Calix's
  customers' own subscribers* ("many of Calix's CXP customers have experienced improved customer
  satisfaction scores, minimal churn"), which is a claim about Cox's retention, not Calix's. The
  brief asked whether there is any filed evidence of the platform as a switching cost; the answer
  is RPO, the software revenue growth rate, and nothing else.

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.
Same metric, same window (FY2025, each company's own fiscal year), each figure from that
company's own latest 10-K via its own XBRL facts.

| Company | gross margin | operating margin | SBC / revenue | SBC / OCF | owner earnings, 5-yr mean (OCF − SBC − capex) | names Calix? |
|---|---|---|---|---|---|---|
| **CALIX (CALX)** | **56.8%** | **+2.1%** | **8.8%** | **65.2%** | **−$5.4M** | subject |
| Cisco (CSCO) | 64.9% | +20.8% | 6.4% | 25.7% | +$10,653.4M | no |
| Harmonic (HLIT) | 48.5% | +3.9% | 8.8% | 29.5% | +$7.2M | **no** |
| Ubiquiti (UI) | 43.4% | **+32.5%** | 0.3% | 1.1% | **+$445.4M** | **no** |
| Ciena (CIEN) | 42.0% | +4.1% | 3.9% | 22.9% | +$129.6M | **no** |
| Cambium (CMBM) | 40.2% | −17.5% | 4.0% | −40.5% | −$17.8M | **YES, twice** |
| ADTRAN (ADTN) | 38.3% | −1.4% | 0.9% | 7.8% | −$10.9M | **YES, twice** |
| Clearfield (CLFD) | 33.7% | +1.4% | 3.1% | n/a | +$4.1M | yes, as the seller of a product line it **bought from Calix** in FY2018 |
| CommScope (COMM) | — | — | — | — | — | **no** |
| Nokia | — *(20-F filer; no us-gaap USD facts; IFRS, EUR)* | — | — | — | — | not obtainable |
| Huawei · Plume Design · eero/Ring | **no filings exist** — Huawei is a private Chinese issuer; Plume Design is private; eero and Ring are unsegmented inside Amazon | | | | | |

*Sources: ADTRAN 10-K accession `0001193125-26-073878`, filed 2026-02-26 — "In the Subscriber
Solutions category, our primary competitors include **Calix**, Ciena, Nokia, eero, RAD, and a
growing number of Asian based [vendors]" and "In our Access & Aggregation solutions category,
key competitors include Nokia, **Calix**, Vecima, Harmonic and Microchip." Cambium 10-K
`0001193125-26-201759`, filed 2026-05-01 — "Our PON Solution competes with Nokia, **Calix**,
Adtran and others" and "These devices compete with all consumer-grade, home Wi-Fi brands, as well
as commercial solutions from companies such as **Calix**." Clearfield 10-K
`0001171843-25-007594`, filed 2025-11-25 — intangibles "acquired as a result of the acquisition
of a portfolio of the active cabinet products from **Calix, Inc.** during fiscal year 2018."
Ciena `0001628280-25-056698`, Harmonic `0001193125-26-067506`, Ubiquiti `0001511737-26-000056`,
CommScope `0001193125-26-072523`: the word "Calix" does not appear.*

- **Peers named: 7 of the 9 competitors Calix itself names have obtainable primary filings, plus
  2 (Cambium, Clearfield) that Calix does not name but which name it or transact with it — so
  **9 companies in the row against the 9 Calix names**, with **3 of the 9 named unavailable**
  (Huawei, Plume, eero/Ring). Nokia files in IFRS and euros; its margin is not same-metric and is
  left blank rather than converted. **Buffett says eight; the row has nine.**
- **Any peer unavailable → moat class PROVISIONAL?** The rule exists to stop a moat being
  *claimed* on an incomplete row. **It does not bite here, and the reason must be stated:
  every missing name is larger and better-capitalised than Calix** — Huawei, Nokia, Amazon.
  Their absence can only make Calix's relative position look **better** than it is, never worse.
  A NONE verdict built on a row biased in the subject's favour does not become PROVISIONAL when
  the bias is removed.
- **The row's limit, stated [E3-61]:** identical structures produce opposite outcomes and the row
  shows position, not conduct. The sharpest single line in it — **Ubiquiti at a 43.4% gross
  margin and a 32.5% operating margin, with SG&A at 4.7% of revenue and SBC at 0.3%** — is
  **not** a like-for-like: Ubiquiti sells largely online and through distribution with community
  support and almost no direct sales force, into WISPs, enterprises and prosumers, and it sells
  no managed-services platform. It is nonetheless the **[E2-45] attacker's answer**, because it
  proves the *structure* permits high returns: a 13-point-lower gross margin converted into a
  15-times-higher operating margin. Calix spends **24.9% of revenue on sales and marketing
  alone** (35.7% with G&A) against Ubiquiti's 4.7% total. That is where the franchise would have
  to be, and the filing shows the cost, not the moat.
- **And the most damning arithmetic in the row: Calix's SBC burden is not an industry
  characteristic, it is a Calix characteristic.** Five-year mean SBC/OCF — **CALX 84.6%**,
  HLIT 61.1%, ADTN 52.5%, CIEN 35.5%, CSCO 20.4%, CLFD 20.4%, **UI 1.3%**. On owner earnings
  Calix ranks **6th of 8**, negative, ahead only of ADTRAN and Cambium — **the only two companies
  in the row that name it as a competitor.** By mutual acknowledgement Calix's real competitive
  set is the two loss-making members of its own industry.
- **Untapped pricing power? [E3-33]** **No.** Claiming the class means claiming near-monopoly
  **[E5-28]**, and the row has nine participants plus Huawei and "several smaller companies."
- **The regime qualification on criterion 3 [E2-59].** Calix is not price-regulated, so
  criterion 3 passes literally. But the *demand* is administered: the 10-K's own risk factor says
  customers "**rely significantly upon interstate and intrastate access charges and federal and
  state subsidies**", that they "use or expect to use government-supported loan programs or
  grants, such as … the **BEAD** program … to finance capital spending", that BEAD purchases
  require **BABA domestic-content compliance** without which "our products [would be] ineligible
  for purchase and use by certain customers", and that customers "may curtail purchases if they
  receive less funding than planned … **or as funding winds down**." Under [E2-59], administered
  demand can floor a business's profits, **but the moat belongs to the regime**, and "That day is
  gone" is how it ends. The FY2024 revenue decline is the same sentence in cash: revenue fell
  20% because customers were "evaluating and preparing for various government stimulus programs."
- Class: **[x] NONE** · Direction: **split — gross margin and software mix widening, operating
  margin, customer count, international share and RPO momentum narrowing. A split direction is
  not a widening moat [E4-32].**

- **VERDICT: [x] OUT.** [E3-03] criterion (2) fails on the filer's own Competition section, which
  names nine competitors, lists price second among the bases of competition, and concedes that
  competitors can undercut it. [E2-44] fails on both halves: no filed instance of a price
  increase in seventeen years, the one gross-margin expansion that looks like pricing power is
  attributed by the filer to a prior-year write-down plus mix, and the same instrument ran 1,040
  basis points the *other* way in 2017 when one customer was 31% of revenue; while dollar volume
  grew 85% with trivial capital and delivered 43% *less* operating income. The advantage that
  exists is a **surfing run on a $40bn federal appropriation [E3-51, E4-36]**, and the wave is not
  ownable.

  **THE STRONGEST SINGLE FACT AGAINST THIS VERDICT, stated as its holders would state it
  [E4-51]:** the software and managed-services line compounded at **27.0% and then 26.9%** —
  straight through a year the hardware business fell 20% — at a **62.9% gross margin**, with
  **RPO up 58.7% in two years to $385.0M** and consolidated gross margin at an **all-time high of
  56.8%, second only to Cisco in its own competitive set.** If that line keeps compounding at
  27% it is $580M of revenue in 2031 at a 63% margin, and the box business becomes the
  distribution channel for a genuine subscription franchise. I do not believe the filings support
  it — 17.4% of revenue, no attach rate, no retention figure, no churn figure, RPO flat for six
  months and billed deferred revenue still below its 2023 level — **but that is a judgment about
  what is not disclosed, and a holder who thinks the platform is real can point at three filed
  series that all go up.**

⛔ **Q2 is OUT. Under the hard sequence (operator rule 2) the file closes here: Q3, Q4 and Q5
return no verdict.** What follows is recorded because the queue requires a price from every run
(operator rule 1) and because several instruments were already built and the findings are real;
**none of it is a clearance and none of it can reopen Q2.** The sections below are written as
findings, not as gate verdicts, and each is labelled.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
### ⚠️ **NO VERDICT. THE FILE CLOSED AT Q2.** What follows is **FINDINGS ONLY**, recorded because
### the brief required the 8-K EX-99.1 to be read before scoring [E4-29] and because the sharpest
### instrument in the whole file turned up here. None of it clears anything, and none of it can
### reopen Q2.

**WHAT THE WEIGHT CASE WOULD HAVE BEEN, had Q2 cleared.** One of the three determinants is high:
**daily execution [E3-38, E2-70]** — about 85% of next year's revenue has to be re-won (RPO
$385.0M with 39% inside twelve months, against $1,000M of revenue); the filer says competition is
on "functionality and features, **price**, existing business and customer relationships"; and
FY2017 shows one customer's decisions moving gross margin **1,040 basis points** in a single year.
Control: no (minority public stake). Leverage: no (**zero borrowings** at every balance-sheet date
in the twelve filings read). **One of three high → Q3 would have been a BINARY GATE, not an
overlay.** Recorded so the Q2 OUT is not read as having spared a gate that would have been easy.

**Honesty — binary, permanent [E5-16].** **No disqualifier found.** Item 3, FY2025 10-K: "We are
not currently a party to any legal proceedings that, if determined adversely to us, in our
opinion, are currently expected to individually or in the aggregate have a material adverse
effect." No restatement, no SEC matter, no officer misconduct matter, no material weakness found
in the twelve annual reports read. Per **[E5-17]** this is the absence of found disqualifiers and
not a finding that the managers are honest.

**[E4-29] — THE FIFTH FLAG — READS CLEAN, AND THAT IS A REAL FINDING.** The standing CGNX
instruction is to pull the latest 8-K EX-99.1 before scoring it. Done, plus every furnished
earnings document on file: **the word "EBITDA" appears ZERO times** in the FY2025 10-K, zero times
in the EX-99.1 releases, and **zero times in the Q4-2025, Q1-2026 and Q2-2026 stockholder letters.**
Calix does not promote EBITDA. That is better than CGNX, better than UAL's proxy, and it should be
said plainly.

**BUT THE SAME MECHANISM IS RUNNING UNDER A DIFFERENT NAME, AND IT IS THE HEADLINE.** [E4-29]'s
objection is to deleting a real expense because it is labelled non-cash; [E5-06] says
"To say 'stock-based compensation' is not an expense is even more cavalier." Calix's non-GAAP
suite — "non-GAAP" appears **31 to 32 times per stockholder letter** — is defined as
**"Non-GAAP excludes stock-based compensation, net of the effect for income tax."**

| Q2 2026, from the stockholder letter of 2026-07-20 | GAAP | non-GAAP | the gap |
|---|---|---|---|
| Net income per diluted share | **$0.26** | **$0.47** | $0.21 of SBC, **44.7% of the headline figure** |
| Q3 2026 guided EPS | $0.16 – $0.24 | $0.37 – $0.45 | non-GAAP is **2.0x to 2.3x** GAAP |
| Q3 2026 guided operating expenses | $141.5m – $143.5m | $123.5m – $125.5m | **$18.0M per quarter, ~$72M a year, removed** |

And a **"Non-GAAP Free Cash Flow"** line: Q2 2026 "$11,932" = operating cash flow $16,512 less
capex $4,580 — with roughly **$18.6M of stock compensation sitting inside that operating cash flow
as an add-back.** Owner earnings for the same quarter, computed the framework's way, are about
**−$6.5M.** The published "free cash flow" and owner earnings differ by $18M and the whole
difference is the expense the label excludes.
**The mitigant, and it is genuine [E2-69]: the guidance table prints the GAAP column beside the
non-GAAP column on the same page**, and the reconciliations are complete. A reader who reads the
table cannot be misled. The flag fires on the *choice of headline*, not on concealment.

**[E4-22]'s THIRD FLAG — trumpeted projections — FIRES, with its own mitigants.** Calix guides
**four lines every quarter** (revenue, gross margin, operating expenses, EPS) and has done so
throughout. **[E3-48]** requires setting the guidance against the outturn, and the record is a
beat: Q2 2026 was guided (2026-04-21) at revenue $287–293M, non-GAAP EPS $0.35–0.45, non-GAAP opex
$127.0–129.0M; it delivered **revenue $293.3M (top of range), non-GAAP EPS $0.47 (above the range)
and opex $122.2M ($4.8M below the bottom of the range).** Guidance is met and the caps on pay are
hard (see below). **[E5-30]** still applies — a guidance culture is a ratchet, not this year's
fact — but the record does not show numbers being made up to hit it.

**[E2-49] — METRIC-SWITCHING — FIRES HARDEST, AND IT FIRES FOUR TIMES ON THE SAME LINE.** How the
MD&A disaggregated revenue, filing by filing:

| Filing | the disaggregation offered |
|---|---|
| FY2019 | large 22% / medium 8% / small 70% (percentages, in Item 1) |
| FY2021 | **Systems / Services**, in dollars |
| FY2022 | **one line: "Revenue"** — no split at all |
| FY2023 | **one line: "Revenue"** — no split at all |
| FY2024 | **by customer size** — Large / Medium / Small, in dollars |
| FY2025 | **Appliance / Software and service**, in dollars |

Four different bases in five filings. **The FY2024 switch runs TOWARD candor and must be credited
[E2-69]:** introducing the customer-size table in the year revenue fell 20% is how the reader
learned that Large fell 39%, Medium 26% and Small 17%. That is a deviation toward disclosure and
is not the weak-accounting flag. **The FY2025 switch runs the other way:** the customer-size table
was **removed in the very next filing** — the year in which it would have shown whether Large and
Medium recovered — and replaced with a split that shows the software line growing 27%. [E2-49]:
"Yardsticks seldom are discarded while yielding favorable readings."

**AND THE CUSTOMER COUNT, WHICH IS THE SAME FLAG ON THE MOST IMPORTANT NUMBER IN THE BUSINESS.**
Q1 built the series: ~1,900 (FY2022) → ~1,600 (FY2023) → ~1,600 (FY2024) → ~1,600 (FY2025), with
the annual-adds disclosure degrading from a specific figure (87 in 2020, 130 in 2021) to a
three-year average ("over 100") to a five-year average ("80"), each restatement longer and
smaller and each following the decline. **Then the furnished 8-K of 2026-04-21, repeated
2026-07-20, introduces new boilerplate: "More than 1,200 customers of all sizes leverage the Calix
One platform."** Two months after a 10-K saying **approximately 1,600**, the press release says
**more than 1,200**, on an undefined and different basis, and nothing reconciles them. The same
boilerplate also changed the platform's stated age from "purpose-built over two decades"
(2026-01-28) to "evolved over 15 years" (2026-04-21) within three months. **The single most
decision-relevant physical series in this business has three different values in three filings
made inside five months, and the company reconciles none of them.**

**🔴 THE SHARPEST FINDING IN THE FILE, AND IT IS IN THE FURNISHED 8-K, NOT THE 10-K — [E4-37]
RUN LIVE, AND THE ANSWER IS FILED IN THE COMPANY'S OWN WORDS.** [E4-37] says you can almost
measure the strength of a business by the agony of determining whether a price increase can be
sustained. Q2 could not run the test from the 10-K, because no price increase appears in
seventeen annual reports. **The stockholder letter of 2026-07-20 runs it in real time.** Memory
component costs are rising (the DDR4-to-DDR5 transition, named in the 10-K as well). Calix
imposed surcharges. And then it said this:

> *"Our memory surcharge programs are designed to **recover costs—not add profit**—while
> **intentionally prioritizing market-share capture and long-term customer goodwill over
> near-term margin.** We decided to apply higher surcharge rates to new orders, adjusting
> surcharges monthly, while **grandfathering backlog** scheduled to ship in the third quarter of
> 2026 at the second quarter surcharge rates."*
> *"The goal of our memory surcharge program is to partner with our customers for **cost recovery
> only.** What this means is that over time the incremental memory costs will be **neutral to
> gross profit**."*

**A company with pricing power does not publicly pre-commit that its price increase is designed
not to add profit, grandfather its backlog at the old rate, and name market-share capture as the
reason.** And it did not work even as cost recovery: **Q2 2026 gross margin was 54.6%, down 230
basis points sequentially and 170 year-over-year, and Q3 2026 is guided down a further ~280 basis
points at the midpoint to 50.5–53.5%** — while revenue is guided **up** to $301–307M from $293.3M.
**Volume up, margin down, by announced policy.** This is [E2-44](1) failing in the present tense,
it is the single most direct instrument in the file, and it was not in the annual report.
*(Recorded here rather than by editing Q2, per operator rule 6. It does not change the Q2 verdict;
it corroborates it, and it also retires the bull case's fifth fact — "gross margin at an all-time
high" was true at 2025-12-31 and has reversed in the two quarters since.)*

**AND THE BULL CASE'S SECOND-BEST NUMBER IS ALSO REVERSING, FOR THE REASON [E4-04] PREDICTS.** The
Q2 2026 10-Q, Item 2: the six-month gross margin decline was "primarily related to **a decline in
our software and service gross margin, which declined by 550 basis points** due to **the transition
from our second-generation platform to our third-generation platform where we operated in a dual
cloud environment to successfully support customer migrations**." So the 62.9% software gross
margin that carried the platform thesis at 2025-12-31 is running near **57.4%** — and the cause is
the cost of moving customers off the previous generation of the same platform. That is [E4-04]'s
excluded class in one sentence: the spending is not defending the same advantage, it is **buying
its replacement**, and the customer has to be carried across at the vendor's expense.

**[E4-30] filed-figure tells — DO NOT FIRE.** Unnaturally smooth growth: the opposite. Reported
operating income runs −$20.4M, −$26.5M, −$28.1M, −$81.6M, −$18.5M, −$15.4M, +$36.8M, +$73.9M,
+$52.6M, +$25.6M, −$43.0M, +$21.0M over 2014-2025. Nothing is being smoothed. Cash taxes: income
taxes paid $11.9M (2023), $5.9M (2024), $6.9M (2025); FY2025 cash tax is **20.2% of pretax income
of $34.2M**, and the reported tax expense is largely the drawdown of the **$165.6M deferred tax
asset** created by the 2021 valuation-allowance release. That is disclosed, explicable and not a
tell.

**[E5-15] serial share issuance — does NOT fire as written, but the share count does.** There is
no primary offering and no ATM in any year read; all issuance is employee equity. But the count:

| | 2010 | 2018 | 2023 | 2025 | 2026-06-27 |
|---|---|---|---|---|---|
| Shares outstanding | 38,711,586 | 53,955,000 | 65,052,000 | **67,120,000** | **62,963,989** (cover) |
| Weighted-average diluted | — | 52,609,000 | 69,320,000 | **69,305,000** | 65,500,000 (Q2) |

**Shares outstanding rose 73.4% from 2010 to 2025 and 24.4% from 2018 to 2025 — while $230.7
million of stock was repurchased over 2013-2025.** Cumulative repurchases of $230.7M against
cumulative option and ESPP proceeds of $196.2M: net cash out for shares over seventeen years is
**$34.5M**, and the count still went up by a quarter since 2018. **For thirteen years the
repurchase programme functioned as an incomplete offset to employee dilution, not as a return of
capital.** It only began to reduce the count in 2026, on which:

**CAPITAL ALLOCATION — [E5-08]'S TWO CONDITIONS, PLUS [E4-31]'S THIRD, AGAINST THE H1 2026
BUYBACK.**
- The scale: **$240,227k of stock repurchased in the six months to 2026-06-27** — $69.4M of it in
  Q2 — against a market capitalisation of $2,218.9M. **10.8% of the company in six months.** Board
  authorisations were raised three times in twelve months: **+$100M (2025-04-18), +$125M
  (2026-01-27), +$100M (2026-04-21)**, with **$94.1M remaining** at 2026-06-27.
- **Condition (1) — ample funds for operations and liquidity? STRAINED, and the direction is
  wrong.** Cash and investments went **$388.1M (2025-12-31) → $194.3M (2026-06-27)**, halved in six
  months, and the 10-Q names the cause: "primarily due to the repurchase of common stock." Over the
  same six months **non-cancelable purchase commitments rose from $317.8M to $338.3M.** So the
  ratio of liquid assets to outstanding purchase commitments **inverted**: 1.22x at 2025-12-31,
  **0.57x at 2026-06-27** — commitments now exceed liquid assets by **$144.0M**. Against that: no
  debt of any kind, $99.4M of receivables, $133.7M of inventory, and the commitments are staged
  (only ~$217M of the year-end $317.8M was due inside twelve months). This is not distress. It is
  **[E5-11] strength (3) moving the wrong way on purpose**, and it is the strength [E5-11] says is
  usually skipped.
- **Condition (2) — a material discount to conservatively calculated intrinsic value? FAILS.**
  Cumulative owner earnings over the seventeen filed years are **−$183.2M** (D&A end) / −$175.9M
  (capex end); the mean is negative on **35 of the 36 window-and-capex-end constructions** built at
  Q4 below; the best single year in company history is **+$29.3M**, of which **$13.2M is interest
  on the securities portfolio, not the business.** A conservatively calculated intrinsic value for
  a business on that record does not exceed its net liquid assets by much, and the repurchases were
  made at **11.4 times** those net liquid assets. → **CAPITAL ALLOCATION FLAG.**
- **The humility clause, stated as [E4-13] requires:** this rests on our own owner-earnings
  construction and our own reading of the franchise, and "it is natural for CEOs to be optimistic
  about their own businesses. **They also know a whole lot more about them than I do**"; "many CEOs
  never stop believing their stock is cheap" **[E5-08]**. The flag binds **position size, never the
  discount rate** — and there is no position to size, because the file closed at Q2.
- **Condition (3), the 1999 original [E4-31] — "Shareholders should have been supplied all the
  information they need for estimating that value." DOUBTFUL on this record.** The customer count
  reads 1,600 in the 10-K and 1,200 in the 8-K two months later; the revenue disaggregation has
  changed four times in five filings; there is no attach rate, no retention figure, no churn
  figure, no subscriber count; and executives are paid partly on **Bookings**, a number that
  appears **seven times in the proxy and is never once disclosed to shareholders in any filing.**
- **[E2-51]'s inverse does not apply** — this is not a manager refusing to repurchase. **[E5-24]**
  does: "what is smart at one price is dumb at another," and the price paid is the whole question.

**[E4-52] — THE LOLLAPALOOZA. THE FLAGS CONVERGE ON ONE MEASURE, AND THAT MEASURE IS THE PAY
MEASURE.** From the DEF 14A of 2026-03-27 (`0001406666-26-000006`):
- The annual cash incentive metrics are **Revenue and Non-GAAP Operating Income**, both quarterly,
  with both thresholds required to fund; the broader NEO set adds **Bookings** and **Non-GAAP
  Gross Margin**. The performance stock options vest on **Bookings and Non-GAAP Operating Income**.
- **"Non-GAAP Operating Income is defined as operating income on a GAAP basis less certain items
  that are not considered indicative of our performance, consisting of: stock-based compensation,
  intangible asset [amortisation]…"**
- **Management is paid on a measure that deletes the single largest expense in the business** — the
  expense that is 8.8% of revenue, 65.2% of operating cash flow, **98.4% of seventeen years of
  cumulative operating cash flow**, and the only line that takes owner earnings below zero.
- The 2025 PSO thresholds were non-GAAP operating income of **$20.0M (threshold) and $40.0M
  (target)**. GAAP operating income in 2025 was **$20,990k**; adding back $87,929k of stock
  compensation clears the $40.0M target by roughly 2.7 times. **"2025 performance-based stock
  options were earned at 100% of target."** Cash bonuses paid at **108% of target**, plus a
  separate gross-margin bonus pool of **$2,039,522**, with "non-GAAP gross margin exceeded the
  target in all four quarters."
- **The mitigants are real and must be recorded:** cash incentives are capped at **110% of target**
  and the PSOs at **100% of target ("i.e., no upside")**, and the reconciliation to GAAP is
  published. Under **[E2-49]**'s "pre-set, long-lived and small bullseyes," hard caps at 100/110%
  are a small bullseye. **The defect is the yardstick, not the size of the prize.**
- The convergence [E4-52] describes is present: the non-GAAP headline, the non-GAAP guidance, the
  non-GAAP pay measure and the buyback all point the same way — toward a figure from which the
  expense that makes owner earnings negative has been removed — and they are one reinforcing
  system, not four separate prompts.

**[E2-30] THE INSTITUTIONAL IMPERATIVE — score all four (not a fraud test).**
- [x] **resists any change in current direction** — sales and marketing has risen every year for
  six years, to 24.9% of revenue and 43.7% of gross profit, while operating margin fell from 6.8%
  to 2.1%. The FY2025 10-K's plan is more of it: R&D "to increase in absolute dollars **and as a
  percentage of gross profit**."
- [ ] projects or acquisitions materialise to soak up available funds — **does not fire.** No
  acquisition in any year read; goodwill has been **$116,175k, unchanged, in every one of the
  twelve annual reports**. Calix has been a net **seller** of product lines (the active cabinet
  portfolio to Clearfield, FY2018). This is a real positive.
- [ ] staff studies to justify a craving — no evidence found in the filings.
- [x] **peer behaviour mindlessly imitated** — the SBC-excluding non-GAAP suite and the quarterly
  four-line guidance are the sector's standard practice, adopted whole.

**[E2-01] THE PRIMARY TEST — and it is the number that would have decided Q3 if Q2 had not
decided the file.** Earnings rate on equity capital employed, balance sheet before income
statement, with [E2-43]'s adjustment for goodwill:

| FY | equity | net income | ROE | operating income | accumulated deficit |
|---|---|---|---|---|---|
| 2016 | $213.0M | — | — | **−$28.1M** | −$584.3M |
| 2017 | $145.0M | — | — | **−$81.6M** | −$667.4M |
| 2019 | $154.0M | — | — | **−$15.4M** | −$702.6M |
| 2020 | $280.3M | $33.5M | 11.9% | +$36.8M | −$669.1M |
| 2021 | $568.4M | $238.4M | *41.9%* | **+$73.9M** | −$430.7M |
| 2022 | $679.6M | $41.0M | 6.0% | +$52.6M | −$389.7M |
| 2023 | $719.0M | $29.3M | 4.1% | +$25.6M | −$360.4M |
| 2024 | $780.9M | −$29.7M | −3.8% | −$43.0M | −$390.1M |
| 2025 | $859.2M | $17.9M | **2.1%** | **+$21.0M** | **−$372.2M** |

- **2021's 41.9% is not earnings.** $168.4M of the $238.4M is the release of a deferred-tax
  valuation allowance — a non-cash item; operating cash flow that year was $56.8M. This is exactly
  why owner earnings may never run through a net-income proxy.
- **Operating income peaked in FY2021 at $73.9M on $679M of revenue and is $21.0M on $1,000M of
  revenue in FY2025. Revenue +47%, operating income −72%.**
- **[E2-43]'s denominator.** Of $859.2M of book equity at 2025-12-31, **$388.1M is marketable
  securities and cash, $116.2M is goodwill and $165.6M is a deferred tax asset.** Net tangible
  operating assets are about **$189.3M** (operating assets $388.6M less non-debt operating
  liabilities $199.3M). Return on unleveraged net tangible operating assets in the best year in
  company history: **$21.0M / $189.3M = 11.1%** — respectable, and it is the strongest Q3-adjacent
  number in the file. In FY2024 it was **negative**.
- **The one-number answer to [E2-01]:** $1,230.2M of paid-in capital has been converted into
  **$859.2M of book equity and a −$372.2M accumulated deficit.** Twenty-seven years, and the
  cumulative earnings of the enterprise are negative.

**The half-owner test [E2-26].** Mixed, and the two halves must both be said. **Against:** the
headline is a non-GAAP figure that deletes the largest expense; the customer count contradicts
itself across two filings five months apart; Bookings is paid on and never published; the revenue
disaggregation has changed four times. **For:** the reconciliations are complete and printed
beside the GAAP column, the FY2024 customer-size table disclosed the damage rather than hiding it
**[E2-69]**, guidance is beaten rather than made, EBITDA is absent entirely, goodwill has never
moved, there is no debt and no off-balance-sheet structure, and the stockholder letter is written
in the first person by the CEO and CFO who then take questions — which **[E2-72]** rates as a tell
in the right direction.

- **VERDICT: NONE. Q3 was not reached.** Findings only. The material above would have been read as
  a **CAPITAL ALLOCATION FLAG** plus a fired **[E2-49]** and a fired **[E4-52]** convergence
  against a clean **[E4-29]**, a clean honesty binary and a clean acquisition record — into a
  **binary gate**, not an overlay. **[E2-37, E2-38, E3-39]** govern regardless: nothing in this
  section could repair Q2, and it is not offered as promotion of anything.

## Q4 — WILL IT SURVIVE?
### ⚠️ **NO VERDICT. THE FILE CLOSED AT Q2.** **FINDINGS ONLY** — recorded because the screen row
### that prompted this run is an owner-earnings row and the brief required it rebuilt over every
### window and both (c) ends, cross-checked to the dollar against the filed statements.

### Owner earnings — the one number **[E2-23]**

**WHICH LINES TAKE A POSITIVE OPERATING CASH FLOW TO A NEGATIVE OWNER-EARNINGS FIGURE — the
brief's central question, answered to the dollar across every filed year. THE ANSWER IS ONE LINE:
STOCK-BASED COMPENSATION.** Not two. The brief's second candidate — capitalised software
development — **does not exist at Calix**, in any of the seventeen years (the line-level evidence
is recorded at Step 0 above). Seventeen years, in $ thousands, every figure as originally reported:

| FY | revenue | gross margin | OCF | **SBC** | **SBC/OCF** | D&A | capex | OE (D&A end) | OE (capex end) |
|---|---|---|---|---|---|---|---|---|---|
| 2009 | 227,500 | 33.7% | 1,390 | 9,196 | **661.6%** | 4,942 | 5,064 | −12,748 | −12,870 |
| 2010 | 281,600 | 40.0% | 9,176 | 25,575 | **278.7%** | 5,015 | 5,614 | −21,414 | −22,013 |
| 2011 | 315,200 | 37.9% | 14,589 | 21,603 | **148.1%** | 7,954 | 7,355 | −14,968 | −14,369 |
| 2012 | 322,700 | 42.6% | 27,678 | 17,437 | 63.0% | 8,562 | 10,179 | +1,679 | +62 |
| 2013 | 374,300 | 45.7% | 40,818 | 19,921 | 48.8% | 10,181 | 6,987 | **+10,716** | **+13,910** |
| 2014 | 392,900 | 45.3% | 38,075 | 16,017 | 42.1% | 9,263 | 11,961 | +12,795 | +10,097 |
| 2015 | 399,100 | 47.7% | **−5,341** | 13,805 | n/m | 10,262 | 7,278 | −29,408 | −26,424 |
| 2016 | 454,700 | 44.3% | 24,419 | 14,285 | 58.5% | 8,319 | 9,839 | +1,815 | +295 |
| 2017 | 510,400 | **33.9%** | **−62,772** | 12,368 | n/m | 10,178 | 8,026 | **−85,318** | **−83,166** |
| 2018 | 441,300 | 44.7% | 3,560 | 17,473 | **490.8%** | 9,187 | 10,426 | −23,100 | −24,339 |
| 2019 | 424,300 | 44.3% | 4,654 | 11,181 | **240.2%** | 10,316 | 13,353 | −16,843 | −19,880 |
| 2020 | 541,239 | 49.3% | 51,409 | 13,960 | 27.2% | 13,718 | 7,819 | +23,731 | +29,630 |
| 2021 | 679,394 | 52.5% | 56,793 | 24,230 | 42.7% | 15,012 | 10,463 | +17,551 | +22,100 |
| 2022 | 867,827 | 50.2% | 27,183 | 44,826 | **164.9%** | 14,315 | 14,067 | −31,958 | −31,710 |
| 2023 | 1,039,593 | 49.9% | 56,251 | 62,771 | **111.6%** | 16,631 | 17,855 | −23,151 | −24,375 |
| 2024 | 831,518 | 54.6% | 68,400 | 70,761 | **103.5%** | 19,550 | 18,054 | −21,911 | −20,415 |
| 2025 | 1,000,010 | 56.8% | 134,953 | 87,929 | 65.2% | 17,710 | 19,435 | **+29,314** | **+27,589** |
| **H1 2026** | 573,313 | 55.7% | **31,146** | 37,295 | **119.7%** | 8,788 | 12,698 | **−14,937** | **−18,847** |

*FY2021-2025 and H1 2026 read directly off the filed Consolidated Statements of Cash Flows;
FY2009-2020 from `companyfacts` at the as-originally-reported value, with FY2011-2013 spot-checked
against the filed FY2013 statement. Revenue 2009-2019 derived as gross profit plus cost of
revenue, which is why 2009-2012 differ marginally from the `Revenues` tag.*

**THE ONE-LINE ANSWER, IN A SINGLE RATIO:** **cumulative operating cash flow over seventeen years
$491.2M; cumulative stock-based compensation $483.3M. SBC is 98.4% of every dollar of operating
cash the business has ever produced.** Cumulative depreciation $191.1M and cumulative capex
$183.8M against it. **Cumulative owner earnings 2009-2025: −$183.2M at the D&A end, −$175.9M at
the capex end.**

**Place it in the calibrated row the brief supplied — and it goes to the top.**
**CALX 98.4% over its filed life** · ARM 96.6% over its listed life (69.0% FY2026) · PINS 68.6% ·
CRWD 68.0% (closed the file) · ELF 40.9% · PLTR 32.0% · QLYS 24.9% · CRM 23.4% · SHOP 22.1% ·
PAY 11.5%. On the FY2025 single year Calix is **65.2%**, which sits between CRWD and PINS; on the
seventeen-year cumulative it is **the highest figure this project has recorded.** And per the Q2
competitor row, **it is not the industry**: five-year mean SBC/OCF is CALX 84.6% against Harmonic
61.1%, ADTRAN 52.5%, Ciena 35.5%, Cisco 20.4% and **Ubiquiti 1.3%.**

**[E3-70] — the measure is market value, not the accounting charge.** The subtraction above uses
the reported charge, which [E3-70] makes the **floor** of the correct subtraction, not the measure.
Most of the awards are RSUs and ESPP, whose grant-date fair value is close to market value, so the
gap is smaller here than for an options-heavy filer. **No windage is added for it** — [E4-11]
spends conservatism once and it is spent below — but the direction of the error is noted: the
honest subtraction is **larger** than $87,929k, not smaller.

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25], PUBLISHED IN FULL PER [E4-38].**
Thirteen rolling five-year windows plus five span windows, at both (c) ends — **36 constructions**:

| window | OE mean, D&A end | OE mean, capex end |
|---|---|---|
| FY2009-2013 | −$7.35M | −$7.06M |
| FY2010-2014 | −$2.24M | −$2.46M |
| FY2011-2015 | −$3.84M | −$3.34M |
| FY2012-2016 | −$0.48M | −$0.41M |
| FY2013-2017 | −$17.88M | −$17.06M |
| FY2014-2018 | −$24.64M | −$24.71M |
| **FY2015-2019** | **−$30.57M** | **−$30.70M** ← the bottom |
| FY2016-2020 | −$19.94M | −$19.49M |
| FY2017-2021 | −$16.80M | −$15.13M |
| FY2018-2022 | −$6.12M | −$4.84M |
| FY2019-2023 | −$6.13M | −$4.85M |
| FY2020-2024 | −$7.15M | −$4.95M |
| **FY2021-2025 (the five-year default [E2-42])** | **−$6.03M** | **−$5.36M** |
| 3-yr FY2023-2025 | −$5.25M | −$5.73M |
| 7-yr FY2019-2025 | −$3.32M | −$2.44M |
| 10-yr FY2016-2025 | −$12.99M | −$12.43M |
| 17-yr FY2009-2025 | −$10.78M | −$10.35M |
| **6-yr FY2020-2025** | −$1.07M | **+$0.47M** ← the only positive |

- **Short-window mean** (3-yr FY2023-25): **−$5.25M to −$5.73M**
- **Long-window mean** (17-yr FY2009-25): **−$10.78M to −$10.35M**
- **Combined range, all 36 constructions: −$30.70M to +$0.47M. Width $31.17M.**
- **THE WIDTH IN A WORD, as the brief asked: the range is WIDER THAN ANYTHING INSIDE IT AND IT
  STRADDLES ZERO.** The width ($31.2M) is **66 times** the largest positive value in it (+$0.47M)
  and **3.0 times** the seventeen-year mean. **Thirty-five of the thirty-six constructions are
  negative; the single positive one is +$0.47M, which is 0.05% of one year's revenue and 0.02% of
  the market capitalisation.** Per [E4-25], *"usually, the range must be so wide that no useful
  conclusion can be reached"* — and here the honest statement is stronger and simpler than "too
  wide": **there is no window in seventeen filed years on which this business has produced positive
  owner earnings as a multi-year mean, to within rounding.** That is a conclusion, not a failure to
  reach one.
- **THE SCREEN ROW REPRODUCES TO THE DOLLAR, and the run says which window it used.** The row read
  `oe_bottom_m -6 | oe_top_m -5`. The **FY2021-2025 five-year window** gives **−$6.03M** at the D&A
  end and **−$5.36M** at the capex end. Both ends reproduce exactly. The row's
  `level_shift_oe (runs from -$83.2M)` is FY2017's capex-end figure, **−$83,166k**, also exact.
- **A wide spread is also a Q4 finding — name the distorted year [E5-11].** Two, and they are
  opposite. **FY2017** is the disaster: operating cash flow **−$62,772k** and owner earnings
  **−$83.2M** in the year CenturyLink was **31% of revenue** and gross margin collapsed to 33.9%.
  **FY2025** is the record: operating cash flow **$134,953k**, more than double any prior year, and
  the **only** year in seventeen whose owner earnings exceed $30M. Under **[E4-41]** the mean must
  be normalised **down** for luck, and FY2025 carries two favourable exogenous items: a working-capital
  release of **+$17,297k** from prepaid expenses and other assets (reversing FY2023's −$60,795k),
  and **$13,178k of interest income** on the securities portfolio, which is not the business. **Strip
  the interest income and FY2025's owner earnings fall from +$29.3M to about +$16.1M — the best
  year the business has ever had is $16M of operating owner earnings on $1,000M of revenue.**
- **[E3-55] scope check, honestly applied:** volatility with a certain endgame is not a defect. Does
  that rescue this spread? **No.** [E3-55]'s case is See's losing money eight months a year around a
  certain annual result. Here the *level* is what is uncertain: the business produced +$29.3M in
  FY2025 and **−$14.9M in the very next half-year**, on revenue up 24.1%. That is uncertainty about
  the level, which is precisely what the spread is allowed to measure.
- **THE WORKING-CAPITAL FLAG — the screen's `wc_note` — FIRES, AND IT FIRES IN THE LIVE PERIOD, NOT
  WHERE THE SCREEN LOOKED.** The row said "accounts payable moved by 45% of a year's operating
  cash"; that is **FY2022** ($12,111k against $27,183k = 44.6%). But the flag's real event is
  current: **H1 2026 accounts payable rose $50,936k against operating cash flow of $31,146k —
  163.5% of the half's operating cash.** Without the payables build, H1 2026 operating cash flow
  would have been about **−$19.8M.** The filer's own metric confirms it: **days payable outstanding
  54 days at 2026-06-27, "up 17 days from the prior quarter and up 37 days from the year ago
  quarter", against a stated "Target Financial Model for DPO … between 25 and 35 days"** — 19 days
  beyond the top of their own target, funding a $46,744k inventory build. **This is the DELL shape
  the flag exists to catch, and per the brief's instruction no window containing it is used without
  saying so: every H1-2026 figure above carries this caveat on its face.** FY2019 is worse in ratio
  terms (payables −$29,440k against OCF of $4,654k, −632%) and is inside the FY2015-2019 window that
  produces the range's bottom.
- **MAINTENANCE CAPEX — (c) AS A DISCLOSED JUDGMENT [E3-44, E2-41], AND THE (c) BAND IS
  IMMATERIAL HERE.** Calix is **fabless**: "We rely on CMs, ODMs and third-party logistics
  partners for the supply and distribution of our products." Capex is **1.9% of revenue**, and
  **capex/D&A = 1.097 (2025)** with a seventeen-year mean of about **0.96** (range 0.570 in 2020 to
  1.294 in 2019). **This is squarely the [E3-44]/[E2-41] default class and NOT the [E5-20] railroad
  exception** — nothing in the filing says depreciation understates renewal, there is no plant to
  renew, and the two ends of the band differ by **less than $2M in every single year.** Across all
  36 constructions the D&A end and the capex end never differ by more than **$1.7M**. **(c) is
  therefore judged at total capex, the marginally more conservative end in 2025, and it changes
  nothing:** the entire width of the range is the *window*, and the entire level of the range is
  **SBC**. *(Disclosed judgment: the working-capital increment [E2-23] is already inside operating
  cash flow by construction, and the H1-2026 payables caveat above is how its distortion is
  handled rather than by a further adjustment.)*
- Stock compensation subtracted in full **[E5-06]**: **yes, at the reported charge, which
  [E3-70] makes the floor.**
- *If the capex band changes the verdict → UNKNOWABLE.* **It does not.** At both ends, on every
  window, the answer is the same.

### Great, good, or gruesome? **[E4-20]**
- [x] **gruesome, and on the corpus's exact definition.** *"The worst sort of business is one that
  grows rapidly, requires significant capital to engender the growth, and then earns little or no
  money."* Revenue grew **+84.8% from FY2020 to FY2025** and **+340% from FY2009 to FY2025**;
  operating income fell **−43.0%** over the first span and operating income is **$21.0M** on
  $1,000M of revenue. The capital it consumed is not plant — capex is 1.9% of revenue — it is
  **equity**: $483.3M of stock compensation over seventeen years, 98.4% of all operating cash ever
  produced, and a share count up 73.4% since 2010.
- **[E4-43]'s caution applied, because the *good* class passes and I must not over-read the test.**
  Is this the good class — "nothing shabby about earning $82 million pre-tax on $400 million of net
  tangible assets"? On the narrow reading it has a case: **return on unleveraged net tangible
  operating assets was 11.1% in FY2025**, which is near [E5-40]'s "quite satisfactory" ~12%. **The
  reason it is not the good class is that the denominator is not where the capital went.** The
  capital went into the share count, and the share count is not in the $189.3M of net tangible
  operating assets. Measured against the capital actually supplied — **$1,230.2M of paid-in
  capital, standing against a −$372.2M accumulated deficit** — the return over the life of the
  enterprise is **negative**. [E4-20]'s gruesome account "both pays an inadequate interest rate and
  requires you to keep adding money at those disappointing returns," and the money added here is
  equity issued to employees.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — FAILS on "reliable."** Operating income over
  twelve years: six losses and six profits, peak $73.9M (2021), trough −$81.6M (2017), current
  $21.0M. Owner earnings positive in 6 of 17 years and negative as a mean on 35 of 36 windows.
- **(2) massive liquid assets — PASSES, but it is being spent.** $388.1M at 2025-12-31; **$194.3M
  at 2026-06-27**; **zero debt** at every balance-sheet date read; interest paid $0 in FY2024 and
  FY2025 and $253k in FY2023. [E3-52]'s reading applies in the company's favour: its liabilities
  are trade payables, accruals and deferred revenue — **no covenants, no due dates, no bank lines
  depended on.** [E5-39] is satisfied on the structure and undermined on the trajectory.
- **(3) no significant near-term cash requirements — THIS IS THE ONE THAT MOVES, AND IT MOVED IN
  THE WRONG DIRECTION BY CHOICE.** **Non-cancelable purchase commitments $338.3M at 2026-06-27**
  (of which the analogous year-end split put ~$217M inside twelve months) **against $194.3M of
  liquid assets**, plus **$94.1M of unexercised repurchase authorisation** the company says it
  intends to use, in a business whose half-year operating cash flow was positive only because
  payables rose $50.9M. At 2025-12-31 liquid assets covered commitments **1.22x**; at 2026-06-27,
  **0.57x**. Against that: $99.4M of receivables, $133.7M of inventory, no debt, and commitments
  that convert to saleable product. **Not distress — a deliberate erosion of the strength [E5-11]
  says is the one usually skipped.**
- **Leverage, named and quantified [E4-16, E3-29]: there is none.** Zero borrowings, zero interest
  paid in the two most recent years, $18.4M of undiscounted operating lease payments through 2033.
  **This is the cleanest single thing about Calix and the brief's expectation of "cash and no debt"
  is confirmed** — with the qualification that the cash halved in the six months to 2026-06-27.

### Name the specific way THIS business dies **[E2-27, E3-24]**
**The mechanism, and it is the one the brief named — but the filing puts the two halves in a
specific order.** Not consolidation first. **Subsidy first, and consolidation as its consequence.**
1. **The appropriation is spent.** The 10-K's own risk factor: customers "rely significantly upon
   … federal and state subsidies," "use or expect to use government-supported loan programs or
   grants, such as … the **BEAD** program … to finance capital spending," and "**Customers may
   curtail purchases if they receive less funding than planned … or as funding winds down.**"
   Calix keeps "a dedicated team of funding specialists." The $40bn is an appropriation with an end.
2. **The dress rehearsal is already filed.** FY2024: revenue **−20.0%** ($1,039.6M → $831.5M),
   with the filer's explanation being that small customers made "delayed purchasing decisions of
   our appliances as our customers evaluated and prepared for various government stimulus
   programs," and large and medium customers **−39% and −26%** because "a small set of significant
   customers … slowed purchases." **A pause in the programme, not its end, cost a fifth of
   revenue and $43.0M of operating income in one year.**
3. **Then consolidation, quantified from the concentration disclosure.** 79.0% of revenue comes
   from operators with under 250,000 subscribers. When the subsidy stops, the marginal
   fibre overbuilder in a two-provider market — and the 10-K forecasts exactly that market:
   "we anticipate **at least two fiber-to-the-home providers vying for subscribers in every
   market**" — is acquired or fails. Its boxes are not replaced; they are absorbed. **And Calix has
   already lived the large-customer version of this: CenturyLink/Lumen went from 31% of revenue
   (2017) to under 10% (2021), and the transition year took gross margin from 44.3% to 33.9%.**
4. **The arithmetic.** Operating expense is **$547.3M a year and 54.7% of revenue**, of which
   $248.6M is a direct sales force sized for landing new customers. **Apply FY2024's actual
   experience — a 20% revenue decline — to FY2025's cost base held flat:** revenue $800.0M, gross
   profit at FY2024's realised 54.6% = $436.8M, against $547.3M of operating expense =
   **an operating loss of about $110M**, against $194.3M of liquid assets and $338.3M of purchase
   commitments. **Two such years and the balance sheet is gone.** FY2017 is the filed precedent at
   smaller scale: one bad year produced **−$62.8M of operating cash flow and −$83.2M of owner
   earnings.**
5. **[E4-40] — model exposure, not experience.** The temptation is to read FY2025's record year and
   H1 2026's +24.1% revenue as the trend. They are the **experience**; the **exposure** is a cost
   base of 54.7% of revenue, 79% of revenue from subsidy-funded operators under 250,000
   subscribers, a gross margin now guided **down** while volume is bought with surcharges held at
   cost, and a liquidity buffer that has been halved to buy stock.
- **Likelihood: a real possibility** — not a likelihood, on the vocabulary [E3-24] supplies. The
  BEAD money is being obligated now, which supports revenue for some years; the balance sheet is
  unlevered; and the software line is growing. **But it is more than a low-level possibility,
  because the filings already contain one full rehearsal of the mechanism (FY2024) and one full
  rehearsal of its cost (FY2017), and the company has spent half its liquidity since.**
- **VERDICT: NONE. Q4 was not reached.** Findings only.

---
⛔ **Q5 does not open.** Q2 returned OUT. Under the framework's hard sequence and operator rule 2,
**UNRESEARCHED and UNKNOWABLE both close the file and OUT closes it permanently; none is a pass.**
Q5's yield, floor, bar and value range are **not filled in**, and no ranking position is assigned.

---
## COMPUTATION — NOT A CLEARANCE
*(Operator rule 3, and the queue's rule 1: every run ends with a price. This section carries no
entry language, no band, no alert and no ranking. It exists so the operator gets a number.)*

**The price, re-struck by this run.**
- **Price $35.24**, close of **2026-09-11**, Yahoo Finance (aggregator, live quote only, flagged
  per operator rule 5), struck 2026-09-12. Five-day tape: 35.96 · 35.34 · 34.44 · 34.93 · 35.24.
- **Shares 62,963,989**, one class, read off the cover of the 10-Q for the period ended
  **2026-06-27**, filed **2026-07-21**, accession **`0001406666-26-000034`**. No preferred issued;
  no convertible.
- **Market capitalisation = 62,963,989 × $35.24 = $2,218.9M.** *(The queue row carried
  `cap_m 2378`. The difference is price, not the count — the count is exactly right, and this is
  the eighth run to check the queue's cap and the first several to find the count itself correct.)*
- **Sovereign 5.35%, dated 2026-09-11**, US Treasury daily par yield curve, 30-year, from the
  issuing authority via `tools/sources.py`. Earnings currency USD (93% of revenue is US).

**What the buyer at $35.24 is paying for, in words.**
At 2026-06-27 Calix held **$194.3M of cash and marketable securities and no debt** — **$3.09 a
share.** The buyer pays $35.24. **$32.15 a share, or 91.2% of the price, is being paid for the
operating business**, and that business has these filed properties: over seventeen years it has
converted **$491.2M of operating cash flow and $483.3M of stock compensation into −$183.2M of
cumulative owner earnings**; its owner-earnings mean is negative on **35 of 36** window-and-capex
constructions; its single best year, FY2025, produced **+$29.3M, of which $13.2M was interest on
the securities** — so about **$16.1M from the business**; and in the following half-year it
produced **−$14.9M** while revenue grew 24.1%.

**What the price already assumes, expressed as the number the business would have to earn.**
- To yield the bare sovereign of **5.35%** at $2,218.9M, owner earnings must be **$118.7M** —
  **4.1 times the best year in company history**, or **7.4 times** that year stripped of interest
  income.
- To clear the **[E4-28] ~10% floor** — *"that's the figure we quit on"* — owner earnings must be
  **$221.9M**, which is **7.6 times** the best year ever, **22% of FY2025 revenue**, and more than
  **ten times** FY2025's GAAP operating income of $21.0M.
- **The growth rate required cannot be stated, and that is the honest answer, not a gap.** Both
  the five-year mean and the seventeen-year mean are negative; a compound growth rate from a
  negative base is not a number. The queue row said the same thing — `growth_required: n/a -
  negative bottom` — and it reproduces.

**What it would be worth on the single most favourable construction the filings permit** — the
best year in the company's history, taken alone, which is **not** an owner-earnings figure under
[E2-23]'s first constraint and is shown only to bound the answer:
- FY2025 owner earnings ex-interest **$16.1M** ÷ 5.35% = **$301M**, plus **$194.3M** of net liquid
  assets = **$495M**, i.e. about **$7.90 a share.**
- The same at the [E4-28] floor: $16.1M ÷ 10% = $161M + $194.3M = **$355M**, about **$5.65 a
  share.**
- On the multi-year mean the framework actually requires, owner earnings are negative, the
  operating business capitalises at or below zero, and what is left is the net liquid assets:
  **$194.3M, about $3.10 a share.**
- **As a round-number range [E4-01], and it is a computation and not a valuation: roughly $3 to $8
  a share. The price is $35.24.**
- **No margin of safety is applied and no bar is chosen** — [E4-11] and [E4-01] are Q5 machinery
  and Q5 did not open. **Windage count: zero.** Every input above is the filed figure.

**PASS / FAIL, plainly, as the queue requires:**
**FAIL. The file closed at Q2 — OUT, on the business, permanently.** [E3-03] criterion (2) fails
on the filer's own Competition section. Q1 returned IN. Q3, Q4, Q5 and Q6 returned **no verdict**;
the Q3 and Q4 material above is findings only.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**NOT REACHED.** There is no position, so there is no sell rule, no pre-committed metric, no
position size and no permanent designation. **[E1-02]** forbids retro-fitting yardsticks after the
act, and writing an entry trigger on a name that failed Q2 on the business would be the category
error the QLYS ruling of 2026-09-07 names. **The reversal condition is recorded in words instead,
and it is a Q2 condition, not a price:** Calix would have to show, in filed documents, (a) a
disclosed and rising **net revenue retention or attach rate** on the software platform, (b)
**software and service revenue above roughly 35% of total** with its gross margin intact, (c) a
**price increase taken and held** — the opposite of the 2026-07-20 "cost recovery only, neutral to
gross profit" surcharge policy — and (d) a **reconciled, non-contradictory customer or subscriber
count** that rises. **None of those is a price alert and none arms one.**
- **VERDICT: NOT REACHED.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → Q2 OUT → **stop**. Q3 and Q4 carry
      material but are explicitly labelled **FINDINGS ONLY, NO VERDICT**; Q5 was not opened; Q6 is
      recorded as NOT REACHED. Operator rule 2 preserved by the labelling, not by withholding.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only IN
      and it rests on documents named with accession numbers.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives — **none was returned.**
- [x] Every UNKNOWABLE verdict states what cannot be known — **none was returned.** Q2 is OUT on
      evidence in hand, not UNKNOWABLE; the document that settles it is the filer's own Item 1.
- [x] Step 0: the filing was read, with accession number, and a figure was cross-checked.
      FY2025 10-K `0001406666-26-000005`, filed 2026-02-20. **Cross-check: operating cash flow
      $134,953 thousand, read off the filed Consolidated Statements of Cash Flows at page 44,
      agreeing to the dollar with the XBRL tag.** Twelve annual reports, one 10-Q, one proxy and
      nine 8-Ks with their exhibits were read; none of the arithmetic above rests on tagged data
      alone except FY2009-2011, which is flagged where used.
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.
      **Thirty-six constructions published in full [E4-38]**, five-year default named [E2-42], (c)
      judged at total capex with the reasoning stated and the [E5-20] exception explicitly rejected.
- [x] Competitor row filled — **nine companies**, each figure from that company's own filing with
      the accession number given; the three unobtainable names (Huawei, Plume, eero/Ring) are named
      and the direction of their absence is stated. **The moat is NOT held PROVISIONAL, and the
      reason is written down:** every missing peer is larger than Calix, so the row is biased in the
      subject's favour and the NONE verdict does not depend on them.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated: **USD 5.35%,
      2026-09-11, US Treasury daily par yield curve.** 93% of revenue is US.
- [x] Value stated as a round-number range, not a point estimate — **roughly $3 to $8 a share**,
      inside a section headed **COMPUTATION — NOT A CLEARANCE**.
- [x] One bar chosen, not both; windage count stated. **Neither bar was used** — Q5 did not open.
      **Windage count: zero.** Every input in the computation is a filed figure.
- [x] Prices dated; aggregator used for live quotes only and flagged. $35.24 close 2026-09-11,
      Yahoo Finance, flagged under operator rule 5; the five-day tape is printed.
- [x] Run committed to git — after Q1, after Q2, after the Q3/Q4 findings, and again at the fold.
- [x] **Operator rule 9 applied to myself.** My Q2 prior was OUT and the verdict is OUT, which is
      the outcome [E4-26] says to distrust. The disconfirming work is on the page: the bull case is
      built first from six filed facts, the strongest fact against the conclusion is stated in the
      form its holders would state it [E4-51], and the two bull facts that *reversed* after Q2 was
      written and committed are recorded as additions below the gate rather than folded silently
      into the Q2 text (operator rule 6).

## REGISTER
- Verdict: **[x] OUT (about the business)** — [ ] IN [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Calix is a fabless vendor of fibre-access boxes to about 1,600 small US broadband
  operators whose fibre is paid for by a $40bn federal appropriation; it fails [E3-03] criterion
  (2) on its own Competition section, which names nine competitors, lists price second among the
  bases of competition and concedes that competitors can undercut it — and seventeen years of
  filings show $483.3M of stock compensation against $491.2M of operating cash flow, cumulative
  owner earnings of **−$183.2M**, and a business that publicly pre-commits that its price increases
  are "designed to recover costs — not add profit."
- **PRICE AND PASS/FAIL: $35.24 (close 2026-09-11), 62,963,989 shares off the cover of the 10-Q
  for the period ended 2026-06-27, accession `0001406666-26-000034`, market capitalisation
  $2,218.9M against a 5.35% USD sovereign of 2026-09-11 — FAIL, closed at Q2, OUT ON THE
  BUSINESS.** No band, no alert, no PORTFOLIO row: a name that failed Q2 failed on the business and
  a price alert on it would be a category error (the QLYS ruling, 2026-09-07). The reversal
  condition is recorded in words at Q6.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable; no rung of the evidence ladder was blocked.
  Rung 1 (SEC XBRL) and rung 2 (EDGAR primary documents) both served. *Two fetch notes: the FY2020,
  FY2021 and FY2022 10-Ks had failed with HTTP 503 during the first session and were re-fetched
  successfully in this one, which is what completed the [E4-55] customer-count series and found the
  ~1,900 peak; and the EDGAR full-text-search endpoint used for the "does the peer name Calix"
  test returned zero hits for every ticker including known positives, so that test was re-run by
  downloading each peer's latest 10-K primary document directly. **The full-text-search result was
  a false negative and is a tooling defect, recorded below.***
- **If UNKNOWABLE:** not applicable.

---
## ADDENDUM — WHAT WAS FOUND AFTER Q2 WAS WRITTEN AND COMMITTED
*(Operator rule 6: violations and corrections go in an addendum, never by editing history. Neither
item below is a correction — both sharpen the Q2 verdict — but both were found after Q2 was on
disk and committed, so they are recorded here with their dates.)*

1. **[E4-37] can be run after all, and it fails.** Q2 recorded "no instance of a price increase was
   found in the filings read" and could not run the agony test. The **stockholder letter furnished
   on 2026-07-20** runs it: surcharges imposed against rising memory costs, stated to be "designed
   to **recover costs—not add profit**" while "**intentionally prioritizing market-share capture
   … over near-term margin**", with backlog grandfathered at the old rate — and gross margin down
   230bp sequentially anyway, guided down a further ~280bp. **The one Q2 test that could not be run
   from the annual report was run from the furnished 8-K, and it points the same way as the
   verdict.** This is the CGNX lesson operating exactly as the queue's standing instruction says it
   will.
2. **Two of the six bull facts have reversed in the live quarters.** Consolidated gross margin —
   "at an all-time high, 56.8%" at 2025-12-31 — was **54.6% in Q2 2026** and is guided to
   **50.3–53.3% GAAP** for Q3 2026. And software-and-service gross margin, the 62.9% that carried
   the platform thesis, **declined 550 basis points** in H1 2026 on the cost of migrating customers
   from the second-generation to the third-generation platform in a dual cloud environment. **Q2's
   bull case is stated as it stood at the annual report and is not rewritten; the reversal is
   recorded here.**

---
## TOOLING AND BRIEF DEFECTS FOUND BY THIS RUN
**Tooling — three, one of them material to other runs:**
1. **The EDGAR full-text-search call used to test "does this peer name Calix" returns zero hits for
   every CIK, including ADTRAN and Cambium, which both name Calix twice in their latest 10-Ks.**
   The endpoint spelling in `_research .../fts.py` is wrong and it **fails silently with a
   well-formed zero-hit response**, which is the worst possible failure mode: a run that trusted it
   would have concluded "no competitor names the subject" and recorded a finding that is false. The
   test was re-run from the primary documents (`peer10k.py`) and the correct answer is **two of nine
   name Calix**. Any run that has used this call for a naming test should re-run it from the
   primary documents.
2. **`best_year_dep 0.321` in the screen row does not reproduce on either obvious construction.**
   Best-year operating cash flow over the five-year FY2021-25 window is 134,953/343,580 = **0.393**;
   over the full seventeen years it is 134,953/491,235 = **0.275**. Neither is 0.321. The row's
   verdict string "ONE YEAR CARRIES THE WINDOW" is right in substance — FY2025 is 39.3% of the
   five-year window's operating cash — but the number it prints is from a third construction the
   row does not name. (Same defect class as the `best_year_dep` finding in the earlier queue notes:
   the diagnostic reaches the reader without its basis.)
3. **`wc_note` pointed at the wrong year, and the right one is current.** The row's "accounts
   payable moved by 45% of a year's operating cash" is **FY2022** ($12,111k / $27,183k = 44.6%).
   The material event is **H1 2026: payables +$50,936k against $31,146k of operating cash flow =
   163.5%**, without which the half's operating cash flow was about **−$19.8M** — and the filer's
   own DPO metric (54 days against a stated target of 25-35) confirms it. A working-capital flag
   computed only on completed fiscal years cannot see the live half. **FY2019 is also worse than
   the flagged year (−$29,440k against $4,654k of OCF, −632%) and sits inside the window that
   produces the range's bottom.**

**The brief — two defects, one of them the whole prior:**
1. **The brief's prior on which lines take operating cash flow negative was half wrong, and the
   wrong half was its own warning.** It named **SBC and capitalised software development**, and
   flagged the HAS/CRWD defect of omitting capitalised development from (c). **Calix capitalises no
   software development in any of seventeen filed years** — no such line exists in the investing
   section of twelve filed cash-flow statements and no such XBRL tag exists at all. The answer is
   **SBC alone**, and it is 98.4% of cumulative operating cash flow. The prior's diligence was
   right and its content was wrong, and the run had to prove an absence to say so.
2. **The brief described a "2023-25 inventory-correction downturn." The downturn is FY2024 alone**
   — revenue $1,039.6M (2023) → $831.5M (2024) → $1,000.0M (2025) — and FY2023 was the **record
   revenue year at the time**. The distinction matters because the brief asked what the downturn did
   to gross margin: over "2023-25" the answer looks like a clean +690bp expansion, while the
   year-by-year filed answer is that the FY2024 rise was **a $28.7M Q4-2023 write-down in the base
   plus mix**, on the filer's own attribution, and the FY2026 quarters are giving it back.

**One thing the brief got exactly right and it decided the file:** *"pull the latest 8-K EX-99.1
before scoring [E4-29] and [E4-22]'s third flag."* [E4-29] read clean in the 10-K **and in the
8-K** — zero occurrences of EBITDA anywhere, which is the honest finding — but the same document
contained the memory-surcharge passage that answered the Q2 pricing question the annual report
could not. **The instruction found the sharpest fact in the file at the gate it was not aimed at.**
