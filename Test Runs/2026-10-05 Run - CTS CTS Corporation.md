# Company Run — CTS Corporation (NYSE: CTS) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. Copied from the template to this dated name before any fetch.

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is barred by this run's blind rule; the
analyst does not know whether the operator holds or wants the name and did not try to learn it.

**CONTAMINATION, declared.** (1) The session's commit subjects name the boxes of other runs of the same day (electrical
contractors and equipment makers); none is about CTS or its competitors' run files, and none was opened. (2) The
directory listing of `Test Runs/` showed other 2026-10-05 file names; none was opened. (3) `tools/run.py` printed v4
material; only its arithmetic lines were used (Part VII), and its SBC column (zero in every year) is wrong: the filed
cash-flow statements show stock pay of $4.9M to $5.7M a year (Step 0). (4) In the research pass at the end, one capital
figure was computed before steps 1 and 2 were written; it is named there.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $62.31 (2026-10-05, live quote via `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares** from the latest filing's cover: 28,556,195 common, without par value, one class (10-Q for the period ended
  2026-06-30, filed 2026-07-28, accession `0001193125-26-320492`; `python Screens/cover_shares.py CTS`).
- **Market cap:** 28.556M x $62.31 = **$1,779M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-02 (issuing authority; via `tools/run.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-24, `0001193125-26-067039`): Items 1, 1A, 5, 7, 7A, the
  cash-flow statement, Notes 1, 3, 7, 11, 17; 10-Q Q2 2026 (filed 2026-07-28, `0001193125-26-320492`): MD&A, customers,
  buybacks; proxy DEF 14A (filed 2026-04-02, `0001193125-26-140010`): ownership, CD&A, clawback, adjusted-EPS
  reconciliation; 8-Ks of 2025-07-02 (`0000950170-25-092631`), 2025-11-06 (`0001193125-25-268239`), 2025-11-24 credit
  agreement (`0001193125-25-293643`), 2025-11-26 (`0001193125-25-300535`), 2026-06-25 CEO succession
  (`0001193125-26-282712`). For the record: 10-K FY2022 (`0000950170-23-004366`), FY2023 (`0000950170-24-019292`),
  FY2019 (`0000026058-20-000016`), FY2016 (`0000026058-17-000026`), FY2013 (`0001193125-14-080179`), FY2009 10-K and its
  Exhibit 13 (`0000026058-10-000009`), FY2007 Exhibit 13 (`0000026058-08-000011`). Texts are in the working folder.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 = $102,105K
  in the filed cash-flow statement (10-K FY2025) against 102 in `tools/run.py` and 102.105 in XBRL: agrees.
- `tools/run.py` arithmetic lines: 3-year OE band 65 to 80, 5-year 69 to 83 ($M), sovereign 5.63%. Its SBC column is
  zero and wrong (above); its OE lines are therefore not used. Owner cash is recast below from the filed statements
  (`Test Runs/_research 2026-10-05 CTS/arithmetic.py`).

**Owner cash after every real cost** ($M): operating cash less stock pay less all capital spending; 2022 less the $34.0M
pension-asset reversion received that year (10-K FY2022: "approximately $ 34,016 was transferred to the Company"); 2022
to 2025 less the yearly fall in the qualified replacement plan, which pays the US 401(k) contribution outside operating
cash (QRP $17.5M at January 2022, then $15.2M, $13.4M, $11.4M, $9.0M at the year-ends 2022 to 2025; 10-K FY2022, FY2023,
FY2025 fair-value notes).

| year | OCF | stock pay | capex | adj. | **owner cash** | depreciation-variant | acquisitions paid |
|---|---|---|---|---|---|---|---|
| 2014 | 33.3 | 2.7 | 12.9 | | 17.8 | | 0 |
| 2015 | 39.2 | 3.2 | 9.7 | | 26.3 | | 1.3 |
| 2016 | 47.2 | 2.7 | 20.5 | | 24.0 | | 73.1 |
| 2017 | 58.0 | 4.2 | 18.1 | | 35.8 | | 19.1 |
| 2018 | 58.2 | 5.3 | 28.5 | | 24.4 | 37.2 | 0 |
| 2019 | 64.4 | 5.0 | 21.7 | | 37.7 | 42.6 | 73.9 |
| 2020 | 76.8 | 3.4 | 14.9 | | 58.5 | 55.8 | 8.3 |
| 2021 | 86.1 | 6.1 | 15.6 | | 64.4 | 62.5 | 0.3 |
| 2022 | 121.2 | 7.7 | 14.3 | -36.3 | 62.9 | 59.1 | 96.9 |
| 2023 | 88.8 | 5.2 | 14.7 | -1.9 | 67.0 | 64.1 | 3.4 |
| 2024 | 98.2 | 5.7 | 18.6 | -2.0 | 71.9 | 73.0 | 121.9 |
| 2025 | 102.1 | 4.9 | 15.7 | -2.4 | **79.1** | 76.4 | 0 |

Five-year average 2021 to 2025: **$69.1M** (depreciation variant $67.0M). Aggregate growth shown 2021 to 2025: 5.3% a
year, while $222.4M was paid for acquisitions in the same five years ($398.1M over 2015 to 2025). Stock pay from the
filed cash-flow statements: FY2016 10-K (2014 to 2016), FY2019 10-K (2017 to 2019), FY2022 10-K (2020 to 2022), FY2025
10-K (2023 to 2025). Capex from the cash-flow statements (XBRL `PaymentsToAcquireProductiveAssets`, cross-read). The
QRP adjustment uses the net fall in the plan; the true 401(k) draw is that fall plus the plan's investment gains, so the
adjustment is a lower bound.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would hold CTS "if the market closed for five years" **[M1997-109]**,
which turns entirely on whether its niches keep earning. Margin of safety bears directly: at $62.31 the price sits near
the top of any range the filings support (COMPUTATION below), so whatever the questions find, a case at this price would
need a pencil, and "it’s too close to think about" **[M1996-084]**. Who is paid to tell you: the proxy's pay metric is an
adjusted EPS that removes environmental charges every year, and the 10-K's risk factors speak of "any sales or earnings guidance or outlook we may
provide from time to time" (10-K FY2025, Item 1A). The analyst's habit asked of me is to look for "what you’re
missing" **[M2025-013]** and to scuttle "to possibly reject your original hypothesis" **[M1998-144]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The filer's own words, every year from FY2016 to FY2025: "highly competitive and characterized by price erosion" (and
   until FY2024 "rapid technological change"); revenue reserves estimate "future credits to customers for price
   adjustments" (10-K FY2025, critical accounting estimates).
2. Transportation net sales (share of sales times sales): $271M (2014), $256M (2015), $262M (2016), $275M (2017), $301M
   (2018), $300M (2019), $242M (2020), $282M (2021), $305M (2022), $303M (2023), $252M (2024), **$233M (2025), the lowest
   in the span**, below the pandemic year. The FY2025 MD&A cause: "lower volumes of our commercial vehicle related products
   and our customers' loss of market share in China."
3. Customer concentration falling: Toyota 12.5% / 12.2% / 11.2% (2023 to 2025), 8.1% in Q2 2026; Cummins 15.0% / 11.7% /
   8.4% (10-K FY2025; 10-Q Q2 2026). Volumes are "estimates, but not firm volume commitments" (10-K FY2025, Item 1A).
4. Growth bought: $398M of cash acquisitions 2015 to 2025 against a market cap of $1,779M; goodwill plus intangibles rose
   from $68M (2014) to $363M (2025), 66% of equity.
5. Two acquisitions under their projections: contingent consideration written down by $1.8M (2024) and $3.6M (2025)
   (cash-flow statement, "Change in fair value of contingent consideration liability"); the SyQwest unit's revenue and
   cost of goods were misstated before and after the purchase and corrected twice, Q1 2025 and Q4 2025 (10-K FY2025,
   Note 1, "Immaterial Correction of Prior Period Errors"); the proxy calls it an "Accounting Restatement".
6. Environmental charges in every year 2014 to 2025 ($0.3M to $18.6M; reserve $16.5M at 2025; Asheville and Mountain
   View NPL sites; an EPA cost claim in mediation, loss recorded $6.6M), excluded from the adjusted EPS that pays the
   executives (proxy reconciliation: environmental charges $0.18, $0.05, $0.11, $0.09 a share).
7. Capex below depreciation in five of the six years 2020 to 2025, 2024 the exception (depreciation $17.5M to $18.4M;
   capex $14.3M to $18.6M).
8. Operating margin below the two large connector and sensor makers through the cycle (competitor row, Q2).
9. The record through 2009: the predecessor of today's business, the Components and Sensors segment, earned 8.8% (2007),
   8.4% (2008) and **4.8% (2009)** on sales falling 27%, and those earnings included pension income (FY2009 Exhibit 13).

## THE STANDING RULE
Nothing in the target forces the buyer's conduct: the rule is satisfied by paying cash, at a size that a total loss
would not threaten, with no borrowed money, since "borrowed money has no place in the investor's tool kit" **[L2014-005]**
and "We are never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. No finding
here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the industry"
  **[M2011-014]**. CTS makes engineered parts to customer specification: accelerator pedals, position and temperature
  sensors, piezoelectric ceramics and actuators, EMI/RFI filters, capacitors, frequency-control parts, rotary actuators,
  sonar transducers, sold to OEMs and tier-one suppliers; 86% of 2025 sales through its own sales engineers working on
  "application-specific products" (10-K FY2025, Item 1).
- **The key variables** **[M1998-044]**: (1) transportation platform awards, volumes and price-downs (43% of 2025 sales);
  (2) growth and margins of the industrial, medical and defense niches (57%); (3) what acquired businesses earn on their
  price. Each is identifiable. Whether each is predictable is the castle question, carried to Q2.
- **Routing (fast change).** The filer wrote "rapid technological change" from FY2016 to FY2024 and "technological change"
  in FY2025 (both phrases the filer's, 10-K risk factors); Q1 closes TOO HARD where "the future technology could hurt the business as it presently exists"
  **[M1998-008]** in a way that puts the ten-year economics out of reach **[L1993-023]**. I do not route it there: the
  product families in the FY2009 10-K ("automotive sensors and actuators", "electronic components", "fabricated
  piezoelectric materials and substrates") are the families of the FY2025 10-K sixteen years later; what has changed is
  the end-market mix, which is a question about customers and competitors, not about a technology outrunning the
  forecast. The filing does not let the past statements tell the future ones by part **[M2008-033]**: CTS reports "one
  reportable segment". That limits Q2, not Q1.
- **Doubt test** **[M2002-092]**: my doubt is not about what CTS does or how it makes money; it is about whether its
  positions last. That is Q2's question, and it is taken there.
- **VERDICT: IN**, with **[M2012-065]**, **[M2011-014]**; the doubts are carried to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and of its key factors, "how permanent are they?" **[M1995-038]**.

**The castle tests, each with its filing fact.**
1. **Key factors and their permanence** **[M1995-038]**. The reason a customer comes is design-in: a part engineered to
   a platform or instrument, qualified, then bought for the program's life ("purchase agreements that have program
   lifetime volume estimates", 10-K FY2025, Major Customers). Its permanence is the program's life, then a re-bid; the
   customer "may choose to use multiple vendors" and "could choose to manufacture and develop particular products
   themselves" (Item 1A). For transportation that is a lead renewed at every platform: "A moat that must be continuously
   rebuilt will eventually be no moat at all." **[L2007-005]**. For the niches (piezo ceramics for medical ultrasound and
   sonar, Navy sonar systems from SyQwest, filters and sensors for industrial and defense) the filings give no fact about
   permanence beyond the acquisitions' own dates.
2. **The attacker with money** **[M2011-015]**. The filer: "some of which have substantially greater manufacturing,
   financial, research and development, and marketing resources than we do", "No one competitor competes with us in every
   product line" (Items 1 and 1A). The rows' failing answer is that "one competitor is frequently enough to ruin a
   business" **[M2012-108]**. Against it, the rows name a moat of size: "very small markets that aren’t really too
   attractive to anybody with any sense to enter" **[M2011-017]**, and firms "of a size and have specialized skills that
   other organizations just can’t get into it" **[M1997-071]**. CTS's niche businesses may be of this kind; the filing does
   not show it, and with one segment I cannot read their returns apart.
3. **Pricing power and the agony before a rise** **[M2005-020]**. No filing in the span records a price rise held against
   competitors; it records the opposite direction: "price erosion", "credits to customers for price adjustments",
   "Significant pricing and margin pressures exerted by a major customer", and if competitors "substantially lower their
   prices, we may lose customers or have to reduce prices" (10-K FY2025, Items 1A and 7). Gross margin rose from 33.2%
   (2015) to 38.4% (2025) and 40.5% (H1 2026), which the filer attributes to "an improved mix of sales by end market" and
   "operational improvements", not price.
4. **Unit volume** (test 5). Transportation sales flat in nominal dollars for a decade, then down 23% in two years to a
   span low of $233M (Contrary evidence, item 2). The volume does not show a place held in the customer's plans; it shows
   the customer's own share loss passing straight through.
5. **The low-cost position** (test 6). No filing claims it; the filer competes "principally based on product features,
   technology, price, quality, reliability, delivery, and service" (Item 1). Not shown.
6. **Would the customer choose it over the low bid?** **[M2017-009]**. For transportation the filer's own account is the
   low-bid one: "Customers demand lower cost and higher quality, reliability, and delivery standards from us as well as
   from our competitors" (Item 1). For a defense sonar or a medical transducer the low bid is less likely to rule, but no
   filing fact shows it.
7. **Ask the competitors / the competitor row** (below). CTS's operating margin averaged 12.6% over 2015 to 2025, with a
   low of 4.7% (2015); Amphenol 20.5% with a low of 19.1%; TE 15.0%; Sensata 12.8%; Allient 7.2%.
8. **Widening or narrowing** **[M1999-108]**, **[M2000-075]**. Two movements in opposite directions. The company margin
   widened, from 8.8% in its sensors segment of 2007 and 4.7% in 2015 to 15.3% in 2025. The transportation franchise
   narrowed: the rows' "lost still another notch" **[L1995-023]** reads close to a decade-flat business now at a span
   low. The widening was bought: $398M of acquisitions shifted the mix, and the earnouts on two of them were cut.
9. **What could destroy, modify or reduce it** **[M2000-014]**. For transportation: the shift of vehicle share in China to
   OEMs CTS does not supply (named by the filer), the commercial-vehicle cycle, and powertrain change at Cummins. For the
   niches: loss of a defense program or a medical OEM, and "a product that can be shipped in from abroad very easily"
   **[M2007-116]**; CTS itself makes parts in China, Mexico, the Czech Republic, Denmark, the Philippines, Poland and
   Taiwan (Item 1), so its own goods cross borders and tariffs (named in Item 1A).

**The competitor row** (operating income over net sales, GAAP as filed, impairments not separated; XBRL company facts
as filed in each company's 10-Ks; latest 10-K accession shown; TE's fiscal year ends in September).

| company | 2009 | 2015 | 2019 | 2020 | 2022 | 2025 | avg 2015-25 | latest 10-K |
|---|---|---|---|---|---|---|---|---|
| CTS | -3.6% (goodwill charge; adjusted 3.5%) | 4.7% | 11.5% | 10.6% | 15.8% | 15.3% | 12.6% | `0001193125-26-067039` |
| Amphenol (APH) | 17.3% | 19.8% | 19.7% | 19.1% | 20.5% | 25.4% | 20.5% | `0001104659-26-013549` |
| TE Connectivity (TEL) | -33.9% | 14.3% | 14.7% | 4.4% | 16.9% | 18.6% | 15.0% | `0001104659-25-109150` |
| Sensata (ST) | 5.2% | 13.2% | 16.1% | 11.1% | 16.6% | 6.4% | 12.8% | `0001477294-26-000007` |
| Littelfuse (LFUS) | n/a | n/a | 12.8% | 11.2% | 19.9% | 1.6% | 12.4% (9 yrs) | `0001628280-26-009585` |
| Allient (ALNT) | n/a | 9.0% | 7.9% | 6.3% | 6.3% | 7.9% | 7.2% | `0001104659-26-024123` |

Read plainly: CTS sits in the middle of its field, below Amphenol in every year and below TE in most, above Allient, level
with Sensata. Nothing in the row says CTS holds a position the others cannot reach; Amphenol's steadiness through 2009
and 2020 is what a protected return looks like, and CTS's 2009 (segment 4.8%) and 2015 (4.7%) are not that.

**The one fact for the castle.** Operating earnings on tangible capital employed (equity plus debt less cash, less goodwill
and intangibles) were 26% in 2014 and 50% in 2025 ($82.6M on $163.8M); that is not what a pure low-bid supplier earns, and
it is the strongest evidence for a castle. On all capital employed, goodwill included because "we paid for it"
**[M2011-060]**, it was 18.4% in 2014 and 15.7% in 2025. The high tangible return may sit in the niches, in the
transportation programs, or in both; one reportable segment does not say which.

**Where it lands.** The castle is not shown open on the evidence for the whole company: the tangible returns and the
widening margin argue against that, and the niches may be the kind of small, skilled markets the rows admire
**[M2011-017]**, **[M1997-071]**. But it is not shown standing either. The largest single business re-bids its moat at
every program and reports price erosion and a span-low volume; the rest was bought in the last decade and cannot be read
apart; and "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge
what its profit margins and returns on capital will be as a host of competitors battle for supremacy" **[L2009-005]**. A
castle whose future cannot be judged is TOO HARD: "it’s just too risky. We don’t know how to valuate that, and therefore
we leave it alone" **[M2000-019]**; the box is "too hard" among the three **[M2006-013]**.

**Which cause.** WORK. The deciding questions are "things that are important and knowable" **[M2006-076]**: whether
the transportation fall is customer volume or CTS's own lost programs; what the acquired niches earn and whether they
hold their customers; whether price-downs are quantified anywhere in CTS's own documents. Each has a primary source and a
span (research pass, below). One part is not knowable: where the transportation business stands against Chinese OEMs and
powertrain change in ten to twenty years is a forecast its own industry "would not want to put down on paper"
**[M2000-105]**; under refinement (c) of Part VII it is recorded and set aside, and the transportation business is valued
at no more than no growth in any later Q7. That I have not done the work is the reader's cause, "I haven’t done the work
and I’m not sure if I did the work I would understand them" **[M1994-026]**, not the industry's.

- **VERDICT: TOO HARD (WORK)**, with **[M1995-038]**, **[L2007-005]**, **[M2000-019]**, **[M2006-013]**, **[M2006-076]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. WEIGHING. NOT REACHED
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion. NOT REACHED
## Q5 — WHO RUNS IT. STOP on integrity. NOT REACHED
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. WEIGHING. NOT REACHED
## Q7 — WHAT IS IT WORTH. STOP. NOT REACHED
## Q8 — BETTER THAN THE ALTERNATIVES. STOP. NOT REACHED
## Q9 — COULD IT RUIN US. WEIGHING. NOT REACHED
## Q10 — THE FAT PITCH. WEIGHING. NOT REACHED
## Q12 (optional): NOT ASKED

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this section was computed after the file closed at Q2 (operator rule 3). It is reported at the owner's
request so the research pass knows what is at stake; none of it is a verdict on Q3 to Q10, and none of it is entry
language.*

**The balance sheets, 2014 to 2025, read before the income account** **[M2025-032]** ($M, year-end; XBRL first-filed,
read against the filed statements of FY2016, FY2019, FY2022 and FY2025):

| | 2014 | 2016 | 2018 | 2019 | 2021 | 2022 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| equity | 289.8 | 317.9 | 377.9 | 405.2 | 463.6 | 506.2 | 530.9 | 551.8 |
| goodwill + intangibles | 67.9 | 126.1 | 131.3 | 191.3 | 179.7 | 260.5 | 363.8 | 363.2 |
| cash | 134.5 | 113.8 | 100.9 | 100.2 | 141.5 | 156.9 | 94.3 | 82.3 |
| revolver debt | 75.0 | 89.1 | 50.0 | 99.7 | 50.0 | 83.7 | 91.3 | 57.5 |
| receivables | 56.9 | 62.6 | 79.5 | 78.0 | 82.2 | 90.9 | 77.6 | 88.1 |
| inventory | 27.9 | 28.7 | 43.5 | 42.2 | 49.5 | 62.3 | 53.6 | 52.9 |
| net PP&E | 71.4 | 82.1 | 99.4 | 105.0 | 96.9 | 97.3 | 94.4 | 89.7 |
| treasury stock (cumulative) | 325.2 | 343.3 | 352.7 | 364.4 | 381.3 | 402.8 | 487.0 | 543.7 |

What the figures say: equity grew $262M in eleven years and goodwill plus intangibles grew $295M, so every dollar of
equity added, and some cash besides, went into purchased intangibles; tangible capital employed is the same in 2025 as in
2014 ($164M against $162M) while sales rose from $404M to $541M. Receivables and inventory rose with sales and then fell
back (inventory 62 to 53 from 2022 to 2025); the tell of "prepaid expense, deferred asset accounts start building up
suspiciously high" **[M1995-064]** was looked for and not found in these lines. Debt is a single unsecured revolver, $57.5M at 2025 and $55.0M at
June 2026, against $300M of commitments to 2030 (8-K 2025-11-24). Cash is mostly abroad: $97.6M of $107.5M at June 2026
(10-Q). Retained earnings fell only in 2021, by the non-cash US pension termination charge; the pension surplus came back
as $34.0M of cash and $17.5M of QRP assets in 2022. What they cannot say: what the niches and the transportation programs
each earn, since there is one segment.

**The real costs.** Stock pay $4.9M to $7.7M a year 2021 to 2025, a real cost **[L2021-003]**; deducted. Depreciation
exceeds capex in five of the six years 2020 to 2025 (not 2024), and "I wish we could keep our businesses competitive while spending less than our
depreciation charge" **[L2015-004]**: the depreciation variant is shown. Amortization of acquired intangibles ($16.2M in
2025) is of customer relationships and technology, mostly the kind that "arise through purchase-accounting rules"
**[L2012-003]**; it is not deducted from owner cash, which starts from operating cash. Environmental remediation recurs in
every year of the span and its cash is inside operating cash; the adjusted EPS that removes it each year is the habit
"to tell owners year after year" what not to count **[L2016-007]**.

**Capital arithmetic** (earnings after depreciation against capital employed): operating earnings rose $40.3M from 2014 to
2025 on $296.7M more capital employed (goodwill included), **13.6% pre-tax on the increment**, against 18.4% on the
2014 base. Cash version (cash earnings against capital spending): owner cash rose from $17.8M (2014) to $79.1M (2025);
acquisitions plus capex over 2015 to 2025 were $398.1M plus $192.4M. The 2014 base year is low ($17.8M, a year of heavy
restructuring), so any growth rate from it is the kind that "can produce a breathtaking, but meaningless, growth rate"
**[L2005-003]**; the range below uses 2021 to 2025 only.

**The value range** (CONVENTION of Q7: five-year average owner cash $69.1M; no-growth end; shown-growth end at 5.3% for
ten years, then zero nominal growth; both at the 30-year Treasury 5.63%, the rate the rows name **[L2000-021]**; plus net
cash less the environmental reserve, $1.26 a share):
- **No growth:** $1,227M = **$44.2 a share**. **Shown growth:** $1,862M = **$66.5 a share**. Width 1.5 to 1, inside the
  three-to-one line. Depreciation variant $43.0 to $64.5.
- **Caveat the Q3 cap would impose:** the 5.3% was shown while $222M was paid for acquisitions. If the growth case is
  charged with the acquisition spend that bought it (owner cash net of $44.5M a year), it is worth $24.5 a share, below
  the no-growth case. The top of the range is therefore generous.
- **Against the price $62.31:** inside the range, near its top. Expected return at the price: 4.0% after corporate tax
  with no growth, 6.0% at the shown growth; **5.1% and 7.7% pre-tax**.
- **The floor and the conversion.** The floor is the Q7 CONVENTION's figure (the framework's words: about ten percent pre-tax), the speakers' own: "at
  least 10% pre-tax returns" **[L2002-020]** (the row itself gives the after-tax translation at the corporate rate of its
  day, with a damaged character), "real expectancy is below 10 percent" **[M2003-149]**. Owner cash is after corporate
  tax, so the floor is converted to after-tax at CTS's FY2025 effective tax rate of 22.0% (10-K FY2025, MD&A): 10% x
  (1 - 0.22) = **7.8% after tax**. H1 2026's rate was 24.1%; at that rate the floor would be 7.6% after tax and the
  prices below rise by about $1.
- **FAIR-PRICE BAND (COMPUTATION):** **$44 to $47**, the prices inside the range at which the expected return reaches
  7.8% after tax (10% pre-tax), and only on the shown-growth case: at $47.0 the shown-growth case returns exactly the
  floor; at $44.2, the bottom of the range, the no-growth case returns 5.7% after tax (7.3% pre-tax), below it.
- **CHEAP PRICE (COMPUTATION):** **about $32**, where the no-growth case alone earns 7.8% after tax (10% pre-tax), the
  "big discount from that present value" **[M1997-126]** that would need no pencil; below it the case would "scream at
  you" **[M2009-005]**.
- **What this means for the open file:** at $62.31 even an IN at Q2 would close OUT at Q7 on the floor; the research pass
  has decision value only at prices near $47 or below.

**Observations for Q5 and Q6, not verdicts (facts only, with the rows they would be read against):**
- Pay: MIP on adjusted EPS (60%), sales (30%), working capital (10%); PSUs on three-year **reported** sales growth (60%)
  and operating cash flow (40%) with a relative-TSR modifier (proxy 2026). Acquired sales count toward the sales metric;
  no metric charges for capital. To be read against "you get what you reward for" **[M2016-083]** and pay tied "to what is
  actually under the reasonable control of the person that’s being measured" **[M2003-019]**.
- The clawback review of the "Accounting Restatement" was analysed by "The Company’s Chief Executive Officer and Chief
  Financial Officer" and found nothing to recover; the MIP's adjusted EPS was moved by $0.08 for the tax law and the
  acquisition's errors. To be read against "the beneficiary is the one that also really does all the design"
  **[M1997-041]**.
- The chief executive was also chairman from 2014 to July 2026 and is now executive chairman, his successor the COO of
  seven months (8-K 2026-06-25): to be read against **[L2014-026]**. Insiders and directors own 2.4% including deferred
  units; the outgoing chief executive 388,395 shares, about $24M (proxy 2026).
- Buybacks: $56.2M in 2025 (the Q4 purchases at $40.23 to $44.43 a share), $12.0M in H1 2026 at up to $58.69 (May 2026); the programme
  names no price (10-K FY2025, Item 5; 10-Q). Prices up to $44 sit at the bottom of the range above; the May 2026 prices
  sit inside it. To be read against **[L2016-002]**.
- All acquisitions 2012 to 2024 were paid in cash; no stock was issued for a deal, so the STOP of **[L2009-019]** does not
  arise.

---
## THE BOX
**TOO HARD (WORK) at Q2.** The castle cannot be judged from the filings: the transportation business (43%) re-bids its
moat at every program, reports price erosion and sits at a decade-low $233M; the niches (57%) were largely bought for
$398M since 2015 and are reported as one segment with the rest. The cause is work, not the industry's nature: the
deciding facts are knowable from primary documents (research pass, below). *(COMPUTATION, not a clearance: value range
$44 to $66 a share against $62.31; fair-price band $44 to $47; cheap about $32. At this price the file would close OUT
at Q7 even if Q2 cleared.)*

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Not committed: the operator's instruction
      for this run forbids commits; the file was written in sections in one session.*
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script; result below); every filing fact has its
      accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; everything after it is headed COMPUTATION — NOT A CLEARANCE and carries no
      entry language.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; stock pay deducted
      (run.py's zero corrected); the sovereign from the US Treasury, dated; the price flagged as aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (nine items, Foundations).
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its SBC column was found wrong and replaced.
- [x] `python tools/check_framework.py`: **PASS** (2026-10-05, after the last edit). Script check of this file: 69 id
      citations, 54 distinct, every one present in `principle_ledger_v5.csv`, no E-id; 37 quoted fragments set beside an
      id, each found verbatim in that row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The Q7 range convention has no rule for growth bought with acquisitions.** It says the cash input
"deducts all capital spending" and carries "the growth the business has actually shown", but CTS's shown growth came
with $222M of acquisitions in the same five years; read literally (acquisitions not deducted, growth credited) the top
of the range is $66, read consistently (acquisition spend deducted from the cash that grows) the growth case is $24,
below the no-growth case. I reported the literal range and printed the consistent figure beside it; a ruling is needed
on whether acquisitions are "capital spending" for the range. (2) **Q2 has no rule for a company that is two businesses
in one segment**, one with evidence leaning toward a castle filling in and one unreadable. Q1 has a by-parts CONVENTION
for holding companies; Q2 has none, so I closed TOO HARD on the whole rather than OUT on the part. (3) **"The two causes
of TOO HARD" assume one deciding question;** here one part (the twenty-year transportation forecast) is NATURE and the
rest is WORK. I used Part VII refinement (c) to set the unknowable part aside and called the box WORK; the framework
should say whether a mixed case is WORK with the NATURE part valued at no growth, as I did, or NATURE outright. (4) **The
fair-price band is defined against the range, but the range's two ends give different floor prices** ($32 no growth, $47
shown growth); "prices inside the range at which the expected return is at or above the floor" is satisfied only on the
upper case. I reported the band on the shown-growth case and said so; the convention should name which case sets it.
Minor: `tools/run.py` still prints zero stock pay for CTS (the company tags stock pay only in its cash-flow text after
2012), a defect of the kind the protocol expects runs to report.

---
## RESEARCH PASS: STEPS 1 AND 2 (written, not run)
*(Part VII form, with the four refinements. No holding facts appear here. Contamination named: the capital figure in
question B2 below, 13.6% pre-tax on the 2014-to-2025 increment, was computed in this run before these steps were
written; the OUT answer for B2 is therefore set on a different span and source, so the computed figure cannot decide it.)*

**Step 1. "What do I not know that I need to know?"** **[M1999-129]**, each marked knowable or not **[M2006-076]**.
- **A. Is the 2023-to-2025 fall in transportation sales CTS's own loss of programs, or its customers' volumes?** Knowable.
- **B1. What do the non-transportation businesses earn, apart from transportation?** Knowable only if CTS has published
  it; with one reportable segment it may prove unanswerable from primary documents (refinement (c)).
- **B2. Did the acquisitions of 2019 to 2024 earn on their price?** Knowable.
- **C. Are price-downs to transportation customers quantified by CTS?** Knowable.
- **D. Do the acquired niches hold their customers: has CTS lost a defense program or a medical OEM?** Knowable.
- **E. Where does the transportation business stand against Chinese OEMs and powertrain change in ten to twenty years?**
  **Not knowable**: a forecast its own industry would not write down **[M2000-105]**. Recorded and set aside; in any later
  Q7 the transportation business is carried at no growth or below.
The deciding questions are A, B1, B2, C and D; they are knowable, so the file does not close TOO HARD (NATURE) at step 1.

**Step 2. For each knowable question: the evidence, where it is, its span, and the single fact that closes the file
OUT** (the research is "to possibly reject your original hypothesis" **[M1998-144]**).
- **A.** Evidence: CTS's own explanation of transportation sales changes. Source: 10-K MD&A and 10-Q MD&A, and 8-K Item
  7.01 investor presentations filed by CTS. Span: FY2023 10-K through the 10-Q for Q3 2026 (filed or due by 2026-10-31).
  **OUT fact:** any of these documents attributes a fall in transportation sales to a program or platform CTS lost, did
  not win at re-bid, or exited, rather than to customer volumes.
- **B1.** Evidence: operating margin or earnings of the non-transportation end markets. Source: CTS 8-K Item 7.01
  exhibits and 10-K segment note. Span: FY2021 to FY2025. **OUT fact:** a CTS document shows the non-transportation
  markets earning a lower operating margin than transportation in two or more years of the span. If no CTS document gives
  the split, record B1 unanswerable with the search that failed, and decide on the rest.
- **B2.** Evidence: what the acquired units earned against what was paid (earnings after depreciation against capital
  employed, never cash against GAAP). Source: CTS 10-K acquisition notes (purchase price) and any CTS disclosure of
  acquired units' sales and earnings; the contingent-consideration roll-forward in the fair-value note. Span: the
  purchases of 2019 (QTI), 2022 (TEWA, Ferroperm), 2023 (maglab), 2024 (SyQwest), read through FY2025. **OUT fact:** a
  CTS filing records an impairment of goodwill or intangibles from any of these five acquisitions in the span.
- **C.** Evidence: the size of price reductions or customer price credits. Source: 10-K revenue-recognition note and
  MD&A sales bridges, FY2019 to FY2025. **OUT fact:** a CTS filing in the span states that price reductions to customers
  reduced net sales by 2% or more in any year. *(The 2% line is a CONVENTION, ours: a size at which price erosion alone
  would absorb a decade of nominal volume growth; rationale: one figure must be fixed in advance so two readers close
  alike.)*
- **D.** Evidence: the loss of a named defense program or medical customer. Source: CTS 10-K and 10-Q MD&A and risk
  factors, 8-K Items 7.01 and 8.01. Span: FY2023 10-K through the Q3 2026 10-Q. **OUT fact:** a CTS document reports the
  loss, cancellation or non-renewal of a program or customer that it says will reduce its aerospace-and-defense or medical
  sales.
- **The IN rule (conjunction):** none of the five OUT facts is found, B1 is either answered in the niches' favour or set
  aside under refinement (c), and transportation is carried at no growth; Q2 then closes IN and the run continues at Q3,
  where Q7's floor prices of this file stand to be checked against the price of that day.
- **The pass never outvotes a doubt**: "if you have doubts about something being into your circle of competence, it
  isn’t" **[M2002-092]**; a pass that ends unsure ends TOO HARD (NATURE). It closes once on these questions and is not
  reopened as TOO HARD (WORK): "if we can’t make a decision in five minutes, we can’t make it in five months"
  **[M2008-086]**.
