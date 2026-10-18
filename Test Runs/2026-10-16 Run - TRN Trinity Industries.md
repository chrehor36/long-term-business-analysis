# Company Run: Trinity Industries, Inc. (NYSE: TRN), 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 97421540). Dispatched blind run;
working folder `Test Runs/_research 2026-10-16 TRN/` (raw filings in its gitignored `cache/`; the scripts and their
outputs beside it). Ledger text is quoted in double quotes beside its id; filing and
other text is quoted in single quotes ‘thus’.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.  *Filled at the fold by the dispatching session, 2026-10-16, after the run was committed: `PORTFOLIO.md` read for this ticker only; not held.*

**CONTAMINATION, declared.** Before any fetch, the session's opening git snapshot showed recent commit subjects of
another company's run (GBX, Greenbrier), one of which reads in part ‘Q2 OUT, commodity-type builder; better margins than
Trinity, ordinary returns for the field over FY2016 to FY2025’. That is a conclusion about this company's field reached in
another run. It was not opened and is not used; every figure below for Trinity and its rivals comes from their own filings,
and the comparison was built from them. Because I saw it before forming my own Q2 judgment, it is a possible anchor
(operator rule 9), and I name it here so the reader can weigh that. Also seen: the names of other research folders in the
git status (AYI, ARCB) and the memory index lines on queue state; nothing in them concerns this company. No blind-listed
file was opened, listed or searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $25.22 (2026-10-16, live quote printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares:** one class, common stock, 79,669,486 outstanding at 2026-07-23 (cover of the 10-Q for the quarter ended
  2026-06-30, filed 2026-07-30, accession `0000099780-26-000119`; `python Screens/cover_shares.py TRN`). Cross-check: the
  FY2025 balance sheet shows 79.8 million shares issued and outstanding and treasury stock of 0.0 million shares at
  2025-12-31 (10-K, accession `0000099780-26-000014`); the 10-Q records repurchases of $20.3 million in the first half of
  2026. No 8-K or prospectus after the 10-Q changes the count (the last filing on EDGAR is the 2026-07-30 8-K).
- **Market cap:** 79.669 million x $25.22 = **$2,009.3M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, 30-year par yield, US Treasury daily par yield curve, 2026-10-15
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 filed 2026-02-19 (`0000099780-26-000014`): Items 1, 1A, 7, the
  statements, Notes 5 (segments) and 6 (partially-owned subsidiaries); 10-Q Q2 2026 filed 2026-07-30 (`0000099780-26-000119`):
  balance sheet, revenue note, repurchases; DEF 14A filed 2026-04-09 (`0000099780-26-000024`): pay; 8-Ks of 2026-01-06
  (`0000099780-26-000006`, the Triumph and RIV 2013 exchange), 2026-02-17 (`0000099780-26-000011`, the leasing EVP),
  2026-04-15 (`0000099780-26-000028`, the TRIP contribution and deconsolidation), 2026-06-16 (`0000099780-26-000100`, the
  $600.0 million revolver), 2026-07-30 (`0000099780-26-000117`, Q2 results, Exhibit 99.1 read). For the cycle: 10-Ks for
  FY2016 (`0000099780-17-000014`), FY2018 (`0000099780-19-000019`), FY2020 (`0000099780-21-000012`), FY2022
  (`0000099780-23-000013`), FY2023 (`0000099780-24-000017`): segment notes, Leasing Group discussions, cash-flow statements.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $359.7M in
  `tools/run.py` = $359.7M on the filed Consolidated Statement of Cash Flows (10-K FY2025). Also total debt at 2025-12-31,
  $5,442.5M on both.
- **`tools/run.py TRN`, arithmetic lines only** (output in `run_py_out.txt`): OCF 295.6 / 573.8 / 359.7 (FY2023 to FY2025),
  SBC 22.7 / 23.6 / 22.9, D&A 293.2 / 293.8 / 305.1, capex as tagged 41.3 / 53.8 / 45.6. The tagged capex is the operating
  and administrative line only; the alternates column adds the lease-fleet line (`PaymentsToAcquireEquipmentOnLease`,
  668.8 / 541.9 / 749.3), which is the business's main capital spending, and neither column nets the proceeds from lease
  portfolio sales (381.8 / 360.7 / 399.3), which recur every year. So the tool's ‘OE capex’ column (231.6 / 496.4 / 291.2)
  overstates owner cash by leaving out the fleet, and its alternate (-437.2 / -45.5 / -458.1) understates it by leaving out
  the sale proceeds. Owner cash is built from the filed lines below, not from either column.

**Owner cash after every real cost, by year (USD millions; filed cash-flow lines; `q7_computation.py`, output in
`q7_computation_out.txt`).** All-spending: OCF less stock pay, less operating capex, less lease-fleet capex, plus lease
portfolio sale proceeds, less acquisitions. Maintenance guess: OCF less stock pay, less operating capex, less the Leasing
Group's depreciation, plus the gains on lease portfolio sales, less acquisitions (the maintenance guess is defended under
AFTER THE STOP, Q3). FY2018 uses operating cash from continuing operations only (Arcosa, spun off in November 2018, took its
cash with it).

| FY | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|---|---|---|
| All-spending, after interest | -510.1 | -649.1 | 59.0 | 458.0 | -331.8 | -117.6 | 315.2 | -58.8 | -104.4 |
| Maintenance guess, after interest | 61.5 | 85.7 | 325.1 | 379.0 | -263.9 | -5.8 | 291.5 | 108.8 | 122.7 |
| Maintenance guess, before interest (after-tax interest added back at 21%) | 187.0 | 250.1 | 487.4 | 519.9 | -113.4 | 188.7 | 505.9 | 324.3 | 293.8 |

FY2020 and FY2021 carry the two halves of a CARES Act tax carryback: a $431.1M build in the income tax receivable in FY2020
and a $440.4M decrease in FY2021 (cash-flow statements, FY2020 and FY2022 10-Ks). The five-year window FY2021 to FY2025
holds the refund without the build, so FY2021 is aberrational on the filer's own figures; the cycle base below is FY2018 to
FY2025, which holds both halves.

**The balance sheets, ten year-ends, read before the income account** **[M2025-032]** (`tools/run.py` table, first-filed
XBRL, read against the filed statements of FY2016, FY2018, FY2020, FY2022, FY2023 and FY2025): total assets were $9,125M
at 2016 and $8,424M at 2025 (8,232 at 2026-06-30), essentially flat for the decade while the fleet's railcar count went
from 85,110 (2016) to 109,295 (2023) and back to 101,485 (2025, after 10,850 cars left with Triumph). Trinity stockholders'
equity fell from $3,918M (2016, before the Arcosa spin-off) to $2,211M (2018) and to $1,030M (2021), and has sat at $1.0 to
$1.1 billion since; what took it down was the November 2018 spin-off of Arcosa, the FY2020 loss ($396.4M impairment of small
cube covered hoppers and a $151.5M pension settlement), and share repurchases of $506.1M (2018), $224.7M (2019), $191.3M
(2020) and $833.4M (2021); capital in excess of par is zero, the buybacks having been charged through it to retained
earnings. Debt is $5,226.5M at 2026-06-30 ($598.8M recourse, $4,627.7M non-recourse in wholly-owned subsidiaries), against
equity of $1,143M: about 4.6 to 1. Deferred income taxes are $1,178M, the second-largest claim on the assets. Goodwill is
$221.5M, about a fifth of equity. Cash is small ($155.7M unrestricted, $114.2M restricted). Inventory was $469M against Rail
Products revenue of $1,420M at FY2025 (33%) and $629M against $2,075M at FY2022 (30%); receivables $389M against $2,157M of
revenue (18%). What the figures say: the asset base did not grow in ten years, and every rise in return on equity came with
a shrinking equity and an unchanged debt. What they do not say: the market value of the fleet against its depreciated cost,
which the gains on every lease portfolio sale suggest is above book. What they cannot say: what the fleet's lease rates will
be at the next downturn.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is whether I would be content to own Trinity's fleet and plants if the
market closed for years, which turns on the fleet's returns, not on the quotation. The market serves and does not
instruct **[M2006-077]**; the company's own releases point to ‘above-market returns’ and a ‘freight cycle’ turning, which is
a macro forecast and enters nothing here **[M2000-094]**. Who is paid to tell you: the company's featured measures are
Adjusted ROE and ‘cash flow from operations with net gains on lease portfolio sales’, both its own non-GAAP constructions,
and its 2025 return on equity was lifted by a non-cash $194.2M partnership gain; these are read as the filer's framing,
not as findings. **Contrary evidence, written down as found** **[M1997-127]**: (1) Leasing Group pre-tax operating profit on
its own assets, about 5 to 7% a year over FY2017 to FY2025 (Q2); (2) unlevered after-tax return on total assets of 4.2%
over FY2016 to FY2025, with return on equity made by debt of about 5 to 1 (Q2); (3) owner cash on the all-spending basis
negative in total over FY2018 to FY2025 (Step 0); (4) a $396.4M impairment in FY2020 on one railcar type (Q2); (5) the 2025
annual bonus paid at the maximum on profit before tax that included the non-cash $194.2M gain (after the stop, Q6); (6) the
looking-for-what-is-wrong habit **[M2025-013]** turned up the run of partnership gains, $194.2M in December 2025 and $132M in
Q2 2026, which the CEO's Q2 statement says ‘anchored’ the quarter's EPS.

## THE STANDING RULE
The buyer would pay cash for a part-interest, with no borrowing and no position that can call for more money, so owning
this does not put the buyer at risk of ruin: "We are never going to risk what we have and need for what we don’t have and
don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt
is the business's risk, weighed at Q9, not the buyer's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. What matters is the
  economics, not the engineering: "What is important is that I understand the economic dynamics of the industry."
  **[M2011-014]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (a) the fleet's lease rates and utilization on
  renewal (97.6% at 2016, 98.5% at 2018, 94.5% at 2020, 97.9% at 2022, 97.1% at 2025, the 10-Ks' Item 1; average remaining
  lease term 2.8 years, so much of the book reprices every year); (b) the cost of keeping the fleet: depreciation,
  maintenance and compliance ($161.3M in FY2025, up 22.4%), and the price of a new car (backlog average $142,504); (c) the
  cost and availability of the non-recourse debt that funds about four-fifths of the assets; (d) railcar demand for the
  manufacturing part, which the 10-K calls cyclical and correlated with North American industrial production. None of these
  changes fast in kind: a railcar is a steel vessel leased for one to ten years and kept for decades, the customer base is
  industrial shippers and railroads, and the 10-K's Item 1A names no technology that displaces it; the named changes are
  regulatory obsolescence of car types and modal shift, both slow. The level of each variable through a cycle is not
  foreseeable, but the shape of the economics is: the financial statements of past years do tell what later ones will look
  like **[M2008-033]**, as the ten-year record below shows (the same fleet economics in every year, moving with the cycle).
- **Routing.** Not a fast-changing industry, so no TOO HARD at Q1 **[M1998-008]**; not a bank (the lessor's asset side is
  railcars on operating leases, readable from the segment notes); the two parts are read separately at Q2 **[L2008-005]**.
- **VERDICT: IN.** The ten-year economics of a North American railcar lessor and builder can be pictured from its filings:
  fleet size, lease rates, utilization, maintenance cost and funding cost, all reported by year (10-K FY2025 Items 1 and 7,
  `0000099780-26-000014`). Doubt about the edge of the circle is applied at Q2, where it belongs.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**; a moat is what "protects excellent returns on invested
capital" **[L2007-004]**.

**The parts table** (segment notes; `segments.py`, output in `segments_out.txt`), FY2021 to FY2025:

| Part | Five-year segment operating profit | Share | Castle | Decides |
|---|---|---|---|---|
| Railcar Leasing and Services Group | $2,384.1M ($2,189.9M without the non-cash $194.2M Triumph gain) | 84% (83%) | scale fleet, integrated with its own builder; ordinary returns on its assets | **yes**, more than half |
| Rail Products Group | $440.1M | 16% | none shown: commodity-type builder at about half its capacity | no; carried to Q7 as an ordinary business at no growth |

The parts are read separately because "lumping them together, as is done in standard financial statements, impedes
analysis" **[L2008-005]**. The file closes on the Leasing Group.

**The castle tests, on the deciding part (the Leasing Group).**
- **The attacker with money** **[M2011-015]**. Railcars are bought from any of the builders and leased by anyone with
  capital: the 10-K says the Leasing Group competes ‘primarily against five major railcar lessors, as well as numerous
  smaller lessors’ and that its investor-owned vehicles are funded by third-party investors (Napier Park, Wafra and
  others, Note 6). Two such investors took over 10,850 cars and then the TRIP fleet in 2025 and 2026. The money to assemble
  a fleet is plainly available, and Trinity itself supplies the cars to it; this is not a field where "You really couldn’t
  create another railroad" **[M2013-054]**.
- **Pricing power, and the agony before a rise** **[M2005-020]**. The filer competes ‘primarily on the basis of the quality
  and craftsmanship of our railcars, competitive pricing, and our ability to provide an outstanding customer experience’
  (10-K FY2025, Item 1). Lease rates fell in the downturns: FY2018 operating profit fell ‘primarily from pricing pressures on
  certain railcar types in our railcar manufacturing business and lower lease rates in our leasing business’ (10-K FY2018),
  and FY2020 leasing revenue fell ‘as a result of lower utilization and lower lease rates on renewals’ (10-K FY2020). The
  rise since 2022 (a ‘Future Lease Rate Differential of positive 3.5%’ at 2026-06-30, Exhibit 99.1 of the 2026-07-30 8-K)
  is a market price moving with the cycle, not a price the lessor sets.
- **Unit volume** **[M1999-054]**: the fleet was 85,110 cars at 2016, 99,215 at 2018, 107,045 at 2020, 108,440 at 2022,
  109,295 at 2023 and 101,485 at 2025; flat from 2020 to 2024 while lease-fleet capital spending net of sale proceeds ran
  $92.9M to $463.5M a year, and lower at 2025 after cars were moved to partners. Utilization held between 94.5% (2020) and
  98.5% (2018).
- **The low-cost position** **[M1997-010]**. The deciding question for a commodity-type business is whether it is the
  low-cost producer, measured "more by cost of production" **[M2006-004]** and from the filings, since "The figures are
  available." **[M2009-059]**. The integration with its own plants (the owned cars are ‘substantially all’ built by the
  Rail Products Group) gives cars at cost, but the rival lessor below earns the same return on its assets, so no cost
  advantage shows in the returns.
- **Would the customer still choose it over the low bid** **[M2017-009]**: no filing fact shows a lessee paying more for a
  Trinity car than for a comparable car from another lessor; the 10-K names competitive pricing beside quality among the
  grounds of competition.
- **Widening or narrowing** **[M1999-108]**: the recurring leasing-and-management operating profit was $312.5M in FY2016,
  $341.3M in FY2017 and $295.8M in FY2022, flat while the fleet grew by about a quarter; it rose to $406.7M (FY2024) and
  $422.8M (FY2025, both without sale gains) in the upswing of lease rates. The change for the better is three years old and
  has not met a downturn; it is credited only on a full cycle, as with the railroads that "then they got good"
  **[M2017-026]** only after decades, and even the improved years earn an ordinary return (below).
- **What could destroy or reduce it** **[M2000-014]**: a car type made obsolete. In FY2020 the company wrote down its small
  cube covered hoppers by $396.4M, more than a full year of the Leasing Group's operating profit; Item 1A names
  regulatory obsolescence and modal shift as the continuing forms of the risk.

**The competitor row.** The 10-K names no rival in Item 1 or Item 1A (a search of the FY2025 10-K for GATX, Greenbrier,
Union Tank, UTLX, Wabtec, FreightCar, Procor, CIT and ‘competitor’ found GATX only as a co-defendant in the East Palestine
litigation, Note 15). **CONVENTION of this run:** the rivals are GATX Corporation (railcar lessor), The Greenbrier
Companies (builder and lessor) and FreightCar America (builder), three SEC filers among North America's railcar lessors and
builders; rationale: the 10-K counts ‘five major railcar lessors’ and ‘four major railcar manufacturers’ without naming
them, and these three file statements comparable over the span. Rivals in the trade that do not file with the SEC (Union
Tank Car, a Berkshire subsidiary; Procor; private lessors) are flagged and not used. Same metric for all, from each
company's own first-filed 10-K XBRL (`returns.py`, output in `returns_out.txt`): unlevered after-tax return on average
total assets, (net income + interest x 0.79) / average assets, and return on average equity, FY2016 to FY2025.

| Company | 10-K accessions (first and last of the span) | Unlevered after-tax return on assets, mean | Return on equity, mean | Comment |
|---|---|---|---|---|
| Trinity | `0000099780-17-000014` to `0000099780-26-000014` | 4.2% (3.4% FY2018 to FY2025, after the Arcosa spin-off) | 9.5% (8.7% FY2018 to FY2025) | FY2016 and FY2017 include Arcosa; FY2017 includes the tax-reform benefit |
| GATX | `0000040211-17-000012` to `0000040211-26-000018` | 4.6% | 13.5% | FY2017 includes the tax-reform benefit; debt about 3 to 4 times equity |
| Greenbrier (FY ends August) | `0001193125-16-746547` to `0001193125-25-253612` | 4.8% | 9.5% | 10.6% in FY2016, 1.7% in FY2021; interest is cash interest paid |
| FreightCar America | `0001193125-17-069639` to `0001193125-26-098668` | negative (losses in eight of ten years) | equity negative from FY2021 | FY2022 to FY2025 net result is the figure available to common holders |

The Leasing Group on its own assets (segment assets less the deferred profit eliminated in consolidation, segment notes of
the 10-Ks listed in Step 0): pre-tax operating profit, including the recurring gains on lease portfolio sales and leaving
out the Triumph gain, of 8.1% (FY2017), 5.6%, 5.7%, 5.2%, 5.2%, 6.0%, 6.1%, 6.2% and 7.2% (FY2025): **6.2% on average, 5.5%
with the FY2020 impairment charged in its year; 4.9% and 4.4% after tax at 21%**, against a long Treasury of 5.43% today.
Rail Products' operating margin averaged 6.4% over FY2016 to FY2025 (14.8% in FY2016, 0.4% in FY2021, 5.2% in FY2025;
capacity utilization ‘approximately 50%’ in FY2025, Item 2), with one customer at 19% of consolidated revenue in FY2025 and
22% in FY2024 (Note 5).

**The field's returns over the last full cycle, judged in words.** The span FY2016 to FY2025 runs from the top of a
delivery cycle (Trinity's Rail Products margin of 14.8% in FY2016) through the trough (8,875 cars delivered and a 0.4%
margin in FY2021) to the upswing of FY2023 and FY2024 and the fall of FY2025 (9,500 deliveries against 17,570). Over it the
lessors, Trinity's Leasing Group and GATX, earn on their assets, before the effect of their debt, a return at or below what
the long government bond pays; their equity returns of nine to fourteen percent are made by debt of four to five times
equity, which is one of the three explanations the rows rule out before a high return is credited, "a cyclical peak in
earnings, a monopolistic position, or leverage" **[L1994-009]**; "That sort of thing does wonders for returns on equity as
reported" **[M2001-054]**. The builders earn less and worse. These are ordinary returns, and on the rows' marks the field is
commodity-type: a standard car available from several builders and lessors, as the insurers' "product is available from
many suppliers" **[L2004-003]**; "the improvement you get one day, your competitor gets the next day" **[M2004-053]**; and few
rivals do not cure it: "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. Trinity is
not shown to be the low-cost operator that is the exception **[L2004-007]**: its leasing return is no higher than GATX's
over the same span.

**What the castle is, and why it does not save the file.** The castle is real and standing: a fleet of about 100,000 cars
at 97% utilization, a builder in-house, a maintenance network, and a long record. It protects a return that is ordinary,
and the framework's list of what Q2 rules out names ‘The standing castle that protects only ordinary returns’: OUT, not TOO
HARD, because the returns are known from the filings and the tenuous-moat row's reason for TOO HARD, "We don’t know how to
valuate that" **[M2000-019]**, does not apply. The framework's CONVENTION gives ‘ordinary’ no figure, so the judgment is in
words: a lessor that earns on its railcars, before its debt, about what a Treasury bond pays, through every phase of a
decade's cycle, and shares that return with a rival that earns the same, is protecting an ordinary return. Price does not
reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "We’re going to be
investors in businesses, not commodities, by and large." **[M2007-131]**

- **VERDICT: OUT.** The deciding part, the Railcar Leasing and Services Group (84% of FY2021 to FY2025 segment operating
  profit), has a standing castle that protects only ordinary returns: pre-tax operating profit of 5.5% to 6.2% a year on its
  own assets over FY2017 to FY2025, 4.4% to 4.9% after tax, matched by GATX (4.6% unlevered after-tax return on assets over
  FY2016 to FY2025); the equity returns are made by leverage. The non-deciding part, Rail Products, is a commodity-type
  builder with a 6.4% average margin. The file closes here; everything below is recorded, not weighed, and every figure
  after this line is a COMPUTATION, NOT A CLEARANCE.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict (the balance sheets were read in Step 0, as the template asks when the file closes before Q4).
## Q5: WHO RUNS IT. NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7: WHAT IS IT WORTH. NOT REACHED as a verdict; the reporting figures are computed below under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.
## Q8, Q9, Q10, Q12. NOT REACHED.

---
## THE BOX
**OUT at Q2** (after Q1 IN): the deciding part, the Railcar Leasing and Services Group, has a standing castle that
protects only ordinary returns over FY2016 to FY2025 (pre-tax operating profit of about 5.5% to 6.2% a year on its own
assets, a return matched by GATX; equity returns made by debt of four to five times equity); Rail Products is a
commodity-type builder. COMPUTATION, NOT A CLEARANCE: value range on the all-equity basis -$34.91 to $4.26 a share against
$25.22; fair price -$36.13 all-equity ($8.74 equity-only); no case earns the floor at the price. **Integrity facts
recorded, not judged** (the 2025 annual bonus paid at the maximum on profit before tax that included a $194.2M non-cash
gain; EPS guidance; featured Adjusted ROE; see AFTER THE STOP, Q5 and Q6).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found, each with its source* **[M1997-127]**; *no verdict; the box is unchanged (operator rule 2).*

**Q3 (capital).**
- Lease-fleet capital spending net of sale proceeds, FY2018 to FY2025: $717.8M, $916.5M, $463.5M, $92.9M, $178.1M,
  $287.0M, $181.2M, $350.0M (sum $3,187.0M), against Leasing Group depreciation of $1,899.9M over the same years (cash-flow
  statements and segment notes of the 10-Ks in Step 0). In FY2020 to FY2024, while the fleet count stayed between 106,970
  and 109,635 cars (107,045 at 2020, 106,970 at 2021, 108,440 at 2022, 109,295 at 2023, 109,635 at 2024), the net fleet spending summed to $1,202.7M and the Leasing Group's depreciation to $1,197.3M: on the
  filer's own figures, standing still cost about the fleet's depreciation. That is the basis of the maintenance guess used
  in Step 0 and below.
- The FY2020 change in estimated useful lives and salvage values lowered that year's depreciation by about $30.8M (10-K
  FY2020, Leasing Group table, note 5).
- Company guidance for 2026: net fleet investment of $450M to $550M and operating capital spending of $55M to $65M (10-K
  FY2025, Item 7).

**Q4 (the accounts).**
- The featured measures are non-GAAP: Adjusted ROE (24.4% for FY2025, on income that includes the $194.2M non-cash gain)
  and ‘cash flow from operations with net gains on lease portfolio sales’ (10-K FY2025, Item 7). The Q2 2026 release
  reports EPS of $1.25 ‘anchored by the $132 million non-cash pre-tax gain’ from the second partnership transaction
  (Exhibit 99.1, `0000099780-26-000117`).
- The covenant leverage test is set on EBITDA (‘consolidated total indebtedness to consolidated EBITDA’, maximum 3.75,
  actual 1.22, 10-K FY2025); the Q2 2026 release and call also present EBITDA (8-K Item 2.02).
- The FY2020 $396.4M impairment and the useful-life change of the same year (above) are the two large judgments on the
  fleet's carrying value in the span.
- Gains on lease portfolio sales recur every year ($17.7M to $127.5M) and sit inside operating profit.
- Cash taxes paid were $51.4M in FY2025 against a provision of $90.9M; the One Big Beautiful Bill Act's 100% bonus
  depreciation is expected to lower cash taxes (10-K FY2025, Item 7). Deferred income taxes are $1,178M at 2026-06-30.

**Q5 (the people) and Q6 (the money and the owners).** Integrity facts, recorded, not judged:
- **The 2025 annual bonus.** Profit before tax carried 65% of the annual incentive, with a target of $220M and a maximum
  of $264M; the company reported PBT of $375.4M, ‘which exceeded the maximum level’, and every named officer was paid
  178% of target (CEO $2,136,000) (DEF 14A 2026, Table 5, `0000099780-26-000024`). The $375.4M includes the non-cash
  $194.2M Triumph gain; without it PBT was $181.2M, below the $220M target. The cash metric of the same plan ‘excludes any
  non-cash gains’; the PBT metric, as described, does not. The 10-K also records ‘incentive compensation expense related to
  the gain on the divestiture of Triumph’ in selling and administrative expense. The proxy states ‘The HR Committee
  believed that the 2025 AIP performed as designed.’
- **Guidance.** Full-year EPS guidance of $2.20 to $2.40 (Exhibit 99.1, 2026-07-30), restated as ‘intact’ by the CEO.
- **How they talk.** The CEO, Q2 2026: ‘we are confident in Trinity's ability to continue generating above-market
  returns for our shareholders’ (Exhibit 99.1).
- **Board.** An independent chairman (10-K FY2025, Item 1, Governance). CEO total pay $7,480,164 in 2025, $7,162,779 in 2024,
  $5,729,556 in 2023 (Summary Compensation Table); CEO pay ratio about 220 to 1.
- **People.** The Executive Vice President, Leasing and Services stepped down from the role 2026-02-16 and retires
  2026-10-15 (8-K `0000099780-26-000011`). No employment contracts with key managers (Item 1A).
- **Buybacks.** The program is a $250.0M authorization of December 2022 with no expiration and no stated price; $137.0M
  remained at 2026-06-30. Purchases in Q2 2026 were made at average prices of $32.40, $34.06 and $33.79 (10-Q Part II, Item
  2). Earlier buybacks: $506.1M (2018), $224.7M (2019), $191.3M (2020), $833.4M (2021), $51.8M (2022), none (2023), $20.7M
  (2024), $71.3M (2025). The Q6 test of a buyback with no stated price needs the bottom of the Q7 range: on the computation
  below, the bottom is -$34.91 a share all-equity and $2.39 equity-only, and every recorded purchase price sits far above
  both. Recorded, not weighed.
- **Dividends.** $0.31 a quarter from December 2025; $98.7M paid in FY2025 against all-spending owner cash of -$58.8M that
  year.
- **Deals.** In 2025 and 2026 the company exchanged and contributed its partnership interests (Triumph, RIV 2013, TRIP) for
  a wholly-owned RIV 2013 and an 11.2% limited partnership interest in NP SPE Holdings (8-Ks `0000099780-26-000006` and
  `0000099780-26-000028`), and in Q2 2026 bought a 32.0% interest in an Indian railcar leasing joint venture (Exhibit 99.1).
  No deal paid in shares was found.

**Q7, COMPUTATION, NOT A CLEARANCE** (`q7_computation.py`; outputs `q7_computation_out.txt` and `q7_literal_capped_out.txt`).
Built by Q7's range convention in full, the floor tested first:
- **Base.** Owner cash as in Step 0. FY2021 is aberrational on the filer's own figures (the $440.4M CARES refund, whose
  $431.1M build sits in FY2020), so by specific (a) the base is the cycle FY2018 to FY2025, which holds both halves; the
  literal window FY2021 to FY2025 is shown beside. By specific (e) the central case is the maintenance guess (the filing
  allows it, Q3 above), the all-spending case beside. By (d) working capital is inside operating cash. By (c) acquisitions
  ($16.6M, $80.4M, $62.2M in FY2021 to FY2023) are deducted, total growth credited; purchases were far below half of owner
  cash, so the business is not a serial acquirer; no deal paid in shares; no signed unclosed deal.
- **Basis.** All-equity (central): owner cash before interest (cash interest paid added back at 21%), after the company's
  own tax, mean $293.8M a year over the cycle; against market value $2,009.3M plus net debt $5,070.8M (debt $5,226.5M less
  unrestricted cash $155.7M at 2026-06-30, the TRIP deconsolidation already in it; $4,956.6M if restricted cash is also
  deducted; operating leases left out). Equity-only beside: owner cash after interest, mean $122.7M.
- **Growth shown.** The series changes sign (FY2022), so by (b) growth is measured between the halves: all-equity $361.1M
  (FY2018 to FY2021) to $226.4M (FY2022 to FY2025), -11.0% a year; equity-only $212.8M to $32.6M, -37.4% a year. A decline
  is carried as the bottom, the no-growth case as the top. The cap (f) does not bind on a decline.
- **Range at the sovereign 5.43%, ten years then zero nominal growth:** all-equity **-$34.91 (bottom) to $4.26 (top)** a
  share against $25.22; equity-only $2.39 to $28.37.
- **The floor (tested first).** Cash yield at the price: all-equity 4.15% (owner cash $293.8M against an enterprise value of
  $7,080.1M); equity-only 6.11%; each is the no-growth case, and the growth cases are lower. **No case earns about ten
  percent at the price**, so Q7 would close OUT on the floor whatever the width.
- **Fair price** (each end valued at ten percent, the two averaged, Part VII): **-$36.13 a share all-equity (central)**;
  **$8.74 equity-only**, beside.
- **Literal window FY2021 to FY2025, beside:** all-equity mean $285.1M; halves growth +29.3% a year, which carried ten years
  would put owner cash at about 170% of FY2025 sales against a highest share of 34.3% in the filings read, so by (f) it is
  cut to the business's own sales growth between the same halves (25.2%), never above the discount rate: 5.43%. Range
  $2.25 to $38.04; fair -$19.78 all-equity, $15.68 equity-only (range $23.56 to $36.35). Even here the ten-percent value of
  every case is below $25.22.
- **Not deducted, and so flattering the figures:** distributions to the minority partners of the consolidated partnerships
  ($32.4M, $8.9M and $18.2M in FY2023 to FY2025); the retained highway-products liabilities are inside operating cash.
- **All-spending case, beside:** all-equity mean $66.6M (cash yield 0.94%), equity-only -$104.4M; value no-growth -$48.25
  all-equity and -$24.13 equity-only.

**Q9 (debt and exposures).**
- Scheduled principal at 2025-12-31: $1,096.1M in 2026, $680.4M in 2027, $1,679.8M in 2028 (including the $600.0M 7.750%
  senior notes due 2028 and a $443.5M warehouse termination payment), of $5,466.5M in total (10-K FY2025, Note 9); the
  company states it intends ‘to use cash from operations and our available liquidity to repay or refinance’ the notes due
  in the next twelve months. Interest payable in the next twelve months about $244.8M.
- Liquidity at 2025-12-31: $1.1 billion committed ($201.3M cash, $592.7M revolver, $321.5M warehouse). New $600.0M unsecured
  revolver of 2026-06-12, maturing 2031, or 2028 if the 2028 notes are not repaid (8-K `0000099780-26-000100`).
- Recourse debt is $598.8M; the rest is non-recourse, secured by railcars in limited-purpose subsidiaries.
- Litigation: East Palestine derailment suits name TILC as owner of one leased tank car; reasonably possible losses on all
  matters $8.0M to $19.7M (Note 15, Item 7).
- Customer concentration in Rail Products: one customer at 19% of consolidated revenue in FY2025 (Note 5). Most cars are
  built in Mexico (Item 1A).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 97421540); written question by question; committed after Step 0
      and Q1 (0328c766), after Q2 (680622a0), and at the close.
- [x] Dispatched: the brief allowed the per-question pathspec commits and states that the dispatching session holds the
      lock; the run binds only once folded into the register by that session (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (a GBX
      commit subject with a conclusion about this field) is declared under CONTAMINATION and not used. No text search of
      `Test Runs/` was made.
- [x] Every v5 id resolves (`check_ids.py`: no E-ids, every id in `principle_ledger_v5.csv`, every double-quoted fragment
      beside an id found in that row); every filing fact carries its document and accession.
- [x] The order was kept; Q2 closed the file; every figure after it is headed COMPUTATION, NOT A CLEARANCE and carries no
      entry language.
- [x] Owner cash after every real cost from the filed cash-flow lines, never a net-income proxy; stock pay deducted; the
      sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor date bars rows.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its owner-earnings columns were not (Step 0 says why).
- [x] `python tools/check_framework.py` PASS before each commit.
- Honest notes: the rivals are a CONVENTION of this run because the 10-K names none. The rivals' figures are first-filed
  XBRL, not cross-checked line by line against their filed statements (one Trinity figure was). GATX's 2025 assets jump with
  an acquisition, which lowers its last-year return. Trinity's FY2016 and FY2017 consolidated figures include Arcosa; the
  Leasing Group's own returns (FY2017 to FY2025) do not depend on that. The leasing asset base for FY2023 to FY2025 deducts
  the whole eliminations line as filed, which also carries non-leasing eliminations, so those three returns are slightly
  overstated. Lease portfolio sale gains for FY2016 to FY2020 are the two railcar-sale lines of the older presentation.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Owner cash for a lessor.** The framework and the tool assume capital spending is one line; for a lessor the
business's main capital spending (the fleet) sits in its own line and recurs with proceeds from selling cars out of the
fleet at a gain. `tools/run.py`'s as-filed owner-earnings column leaves the fleet out and its alternate leaves the sale
proceeds out, so neither is usable; I built owner cash from the filed lines and defended the maintenance guess from the
filer's own fleet count (net fleet spending equal to fleet depreciation in the years the fleet did not grow). A sentence in
Q7 on how a lessor's net fleet investment enters owner cash would make runs comparable. (2) **The competitor rule** asks
for rivals the 10-K names; this 10-K counts them and names none, which the brief foresaw; the CONVENTION is stated. (3)
**The field's returns for a levered lessor.** Q2's "ordinary returns" test is judged in words with no stated measure; for a
business financed four or five to one, return on equity and return on assets point opposite ways (nine to fourteen percent
against four to five). I judged on the return on assets before the effect of debt, citing the rows that refuse returns
made by leverage, but the framework does not say which measure the test reads, and a run that read return on equity could
reach a different box on the same filings. (4) **Specific (b) and the halves.** The cycle base of eight years splits into
halves of four; the literal window of five years does not split evenly, and the text does not say how to split an odd
window (the script puts two years in the first half and three in the second). (5) **Specific (f) on the literal window**
cuts an absurd rate to sales growth "never above the discount rate", which here is the binding limit; the cut is
mechanical and the text does not say whether the sales growth itself must pass the same absurdity test.
