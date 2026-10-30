# Company Run — The Sherwin-Williams Company (NYSE: SHW) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, holding
reviews, the session-state files, the register, the prepped reading list and `tools/alerts.json` were not opened, and no
earlier run or research folder for this ticker was opened.

**CONTAMINATION, declared.** (1) A listing of `Test Runs/` showed the names of the 2026-10-05 run files (names only); the
box lines of all of them were printed by a grep for FORM, and one file (HUBB, an electrical manufacturer) was read for
form; at Q4 the lines citing **[M2002-026]** in the HUBB and TSCO runs were read to see how EBITDA talk had been
weighed (form only); none is about Sherwin-Williams or a paint maker. (2) The analyst knows Sherwin-Williams from training (a large US
paint and coatings maker with its own store chain, the buyer of Valspar in 2017); that is a prior to be replaced by the
filings, and every fact below is taken from the filings cited.

Working folder: `Test Runs/_research 2026-10-06 SHW/` (`fetch.py`, `h2t.py`, `listfilings.py`, the tool outputs, the
arithmetic scripts; raw filings under its gitignored `cache/`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$318.46** (close 2026-10-05, printed by `python tools/run.py SHW`; an aggregator quote, live price only,
  flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock $0.33-1/3 par, **242,758,151** "As of June
  30, 2026" (Form 10-Q for the quarter to 2026-06-30, filed 2026-07-28, accession `0000089800-26-000049`;
  `python Screens/cover_shares.py SHW`, output in the research folder). No second class appears on the cover or in the
  balance sheet (`CommonStockSharesIssued` equals the outstanding count after the Q4 2025 treasury retirement).
- **Market cap:** 242.758M x $318.46 = **$77,309M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, dated 2026-10-05
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-19, `0000089800-26-000008`): Item 1, Item 1A, Item 5,
  Item 7 in full, the statements, Notes 1 (non-traded investments), 22 (segments); 10-Q Q2 2026 (filed 2026-07-28,
  `0000089800-26-000049`); proxy DEF 14A filed 2026-03-11 (`0000089800-26-000025`); 8-K of 2026-07-28 with Exhibit 99.1,
  the Q2 2026 earnings release (`0000089800-26-000046`); for the record: 10-K FY2022 (`0000089800-23-000007`, cash flows
  2020 to 2022 and segments), 10-K FY2019 (`0000089800-20-000005`, segments 2017 to 2019), 10-K FY2016 with Exhibit 13
  (`0000089800-17-000005`, segments 2015 to 2016), 10-K FY2010 with Exhibit 13 (`0000950123-11-017092`, segments 2008 to
  2010). Further documents are named where they are used.
- **One figure cross-checked against the filed statement:** net operating cash FY2025 **$3,451.6M** and capital
  expenditures **$797.6M** in the filed Statements of Consolidated Cash Flows (10-K FY2025, `0000089800-26-000008`)
  against `tools/run.py`'s 3,452 and 798: they agree. Stock-based compensation 123.5 (filed) against the tool's 124: agrees.
- **`python tools/run.py SHW`, arithmetic lines only** (output saved as `run_py_output.txt`). Nothing it prints as a rule,
  id, floor or verdict is used (Part VII). Its share count (242.758M as of 2026-06-30) agrees with the cover. Its owner
  cash omits one real cost the filing names: "Amortization of non-traded investments" (U.S. affordable-housing and
  historic-renovation partnerships bought for their tax credits; the credits reduce taxes inside operating cash while the
  contributions are paid outside it; Note 1, 10-K FY2025). The amortization is deducted below as the cost of those credits.

**Owner cash after every real cost** = net operating cash − stock pay − all capital expenditures − amortization of
non-traded (tax-credit) investments (USD millions; interest, taxes and pension payments are already inside operating
cash; stock pay is added back inside it and deducted again here as the real cost it is). Script `owner.py`, output
`owner_output.txt`.

| FY | net operating cash | stock pay | capex | tax-credit amortization | **owner cash** | depreciation variant | source |
|---|---|---|---|---|---|---|---|
| 2016 | 1,308.6 | 72.1 | 239.0 | not filed | **997.5** | 1,064.4 | companyfacts, `0000089800-17-000005` |
| 2017 | 1,884.0 | 90.3 | 222.8 | not filed | **1,570.9** | 1,508.7 | `0000089800-18-000004` (Valspar from June 2017) |
| 2018 | 1,943.7 | 82.6 | 251.0 | not filed | **1,610.1** | 1,582.9 | `0000089800-19-000004` |
| 2019 | 2,321.3 | 101.7 | 328.9 | not filed | **1,890.7** | 1,957.5 | `0000089800-20-000005` |
| 2020 | 3,408.6 | 95.9 | 303.8 | 84.8 | **2,924.1** | 2,959.9 | 10-K FY2022 `0000089800-23-000007` |
| 2021 | 2,244.6 | 97.7 | 372.0 | 53.6 | **1,721.3** | 1,830.2 | same |
| 2022 | 1,919.9 | 99.7 | 644.5 | 38.5 | **1,137.2** | 1,517.7 | same |
| 2023 | 3,521.9 | 115.9 | 888.4 | 65.4 | **2,452.2** | 3,048.3 | 10-K FY2025 `0000089800-26-000008` |
| 2024 | 3,153.2 | 138.1 | 1,070.0 | 75.0 | **1,870.1** | 2,642.7 | same |
| 2025 | 3,451.6 | 123.5 | 797.6 | 104.0 | **2,426.5** | 2,883.8 | same |

- **Five-year mean 2021 to 2025: $1,921.5M** (all capex); depreciation variant $2,384.5M (depreciation only; the
  amortization of acquired intangibles, about $310M to $337M a year since Valspar, is not deducted, since "Some truly
  deplete over time while others never lose value" **[L2012-003]**). Ten-year mean 2016 to 2025: $1,860.1M.
- **The capex is lumpy for a reason the filing names.** The Administrative function, which carries the new global
  headquarters and research-and-development center, spent $434.8M, $623.2M and $348.1M of capex in 2023, 2024 and 2025
  (Note 22, 10-K FY2025); the buildings were placed in service in 2025, and the company sold and leased back the
  headquarters for $800M received from 2022 to 2025, booked as a financing (MD&A, Real Estate Financing). "Core capital
  expenditures are targeted to be approximately 2% of Net sales in 2026" (MD&A, 10-K FY2025). The maintenance judgment is
  at Q3.
- **Operating cash swings with working capital and tax timing:** 2020 was lifted and 2021 to 2022 lowered by working
  capital (inventories rose from $1,804M at the end of 2020 to $2,626M at the end of 2022, and 2023 drew $323M back
  out of them), and 2025 by $153M of deferred taxes from the 2025 tax law's immediate
  expensing (MD&A, Deferred Income Taxes). The five-year mean is used so that no single year sets the base **[L2005-003]**.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**, and what decides the outcome is "the prospects of the businesses" **[M1998-099]**, not the quotation.
The market serves and does not instruct **[M2006-077]**: a well-known, widely admired name is where the price is most
likely to carry the crowd's opinion, so the analysis below sets price aside until Q7. Margin of safety is an attitude
here and an arithmetic only at Q7 **[M1997-126]**. No macro forecast enters **[M2000-094]**: the filer itself calls 2026
"softer-for-longer demand" (MD&A outlook); that is not used as a reason to buy or to wait. Who is paid to tell you: the
filer's "Adjusted diluted net income per share" and "Adjusted EBITDA" are management's numbers, and the company's
statement that net debt "was 2.4 times the Company's EBITDA" is a target set in the filer's own EBITDA terms; they are
read at Q4 **[M2020-037]**. The analyst's habits: the analyst came in with a favourable prior on this name (a known
high-quality franchise); that is the anchor the rows warn of, "always your previous conclusion" **[M2016-054]**, so the
search below is for what is wrong **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) owner cash after all capital spending has barely grown in five years (five-year mean 2016 to 2020 $1,798.7M,
2021 to 2025 $1,921.5M, about 1.3% a year), while sales grew from $18.4B to $23.6B; (2) Paint Stores Group sales volume
fell "low-single digit" in 2025 and was carried by price (MD&A); (3) Consumer Brands margin fell from 19.0% to 16.1% and
Performance Coatings from 15.1% to 13.9% in 2025 (Note 22); (4) total debt rose to $10.871B against equity of $4.598B,
with the company targeting net debt at "2.0 to 2.5 times EBITDA" (MD&A); (5) the 2017 Valspar purchase left $8.0B of
goodwill and $4.0B of intangibles that are now 46% of total assets (balance sheet, 10-K FY2025).

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money, unlevered and sized so that a fall of half would not force a
sale, does not put the buyer at risk of ruin: "always be sure you can play the next day" **[M2025-015]**; no borrowed
money **[L2014-005]**; the target's own debt is weighed at Q9, not here. The rule is met if the purchase is financed and
sized that way; nothing in this run asks for anything else **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** Three segments (10-K FY2025, Item 1 and Note 22): **Paint Stores Group**,
  4,853 company-operated paint stores in the US, Canada and the Caribbean selling Sherwin-Williams and controlled-brand
  architectural paint to "architectural and industrial paint contractors and do-it-yourself homeowners", $13,606M of
  sales (58% of the total) and $3,061.5M of pre-tax income (22.5% of sales); **Consumer Brands Group**, the brands sold
  through home centres and dealers (Valspar, Minwax, Krylon, Purdy, Dutch Boy, HGTV HOME, Suvinil and others) plus 307
  Latin American stores, $3,166M of outside sales and the manufacturing and distribution base for the stores ("Approximately
  63% of the total sales of the Consumer Brands Group in 2025 were intersegment transfers"); **Performance Coatings
  Group**, industrial wood, general industrial, automotive refinish, protective and marine, coil and packaging coatings
  worldwide, $6,795M of sales and 13.9% pre-tax.
- **The key variables and how predictable they are** **[M1998-044]**: (1) gallons of architectural paint bought by
  professional painters for repaint, new residential and commercial work in North America, a product consumed and
  re-bought as buildings age; (2) the price per gallon against raw-material cost (resins, latex, pigments, solvents, "derived
  from various upstream petrochemical and related commodity feedstocks, notably propylene", Item 1); (3) the count of
  stores, which the segment's stated objective grows "by an approximate average of 2% each year" (MD&A); (4) shares
  outstanding. The first is tied to the stock of buildings and the habit of repainting, which changes slowly; the second
  is tested at Q2. The product is not one that "must deal with fast-moving technology" **[L1993-023]**: paint for a
  house wall in ten years will be bought by the same contractor for the same reason.
- **Do the past statements tell me the future ones?** **[M2008-033]**. For the stores, yes: the segment earned 13.4%,
  14.3% and 14.2% pre-tax in 2008 to 2010 (Note 19, Exhibit 13 to 10-K FY2010, `0000950123-11-017092`), 19.9% and 20.8%
  in 2015 and 2016 (Exhibit 13 to 10-K FY2016, `0000089800-17-000005`), 19.4% to 22.1% in 2017 to 2022 as The Americas
  Group (10-K FY2019 and FY2022) and 22.3%, 22.0% and 22.5% in 2023 to 2025 as recast (Note 22, 10-K FY2025); in the
  2009 trough, with segment sales down 13%, the margin rose. Performance Coatings is the less foreseeable part (industrial
  customers, "numerous competitors", technology and price as stated competitive factors, Item 1), but it is 29% of sales
  and about a fifth of segment profit, and its products (finishes for wood, metal, cars, cans, coil) are not a field of
  rapid invention.
- **Would the insiders write the forecast down?** **[M2000-105]** The filer states a numbered store-growth objective and
  a capex target as a share of sales; the forecast the analyst needs (paint gallons and price in North America in ten
  years) is of the kind an industry insider would write down. "Is it important and knowable?" **[M2006-076]**: yes.
- **Contrary evidence written down** **[M1997-127]**: Performance Coatings and the Latin American business (Suvinil,
  bought October 2025 for about $1.15B; Argentina named among "highly inflationary economies", MD&A) are outside an
  easy forecast; the analyst's understanding of them is thinner. They are minority parts of the profit, and the doubt
  rule "if you have doubts about something being into your circle of competence, it isn't" **[M2002-092]** is applied to
  the whole: the part that sets the value, the North American paint stores, is understood; the rest is carried as a
  weight on certainty at Q7 **[M1999-104]**, not as an exclusion.
- **Routing.** Not a fast-changing industry (no Q1 TOO HARD on change **[M1998-008]**); not a financial institution; not
  a holding company.
- **VERDICT: IN.** The economics of the main part can be foreseen ten years out with "a reasonable fix on about what the
  earning power and competitive position will look like" **[M2012-065]**; paint is understood as a product and, more to
  the point, as an economic dynamic **[M2011-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is asked of each part, since the parts do not share one castle **[M1995-038]**. The value rests on the
Paint Stores Group (58% of sales, about two-thirds of segment profit in 2025, Note 22); Consumer Brands and Performance
Coatings are read for whether they are open.

- **The castle questions: what keeps it standing, and how permanent?** **[M1995-038]** The filer names its stores'
  customer: "architectural and industrial paint contractors and do-it-yourself homeowners", served through 4,853
  company-operated stores selling only its own and controlled brands, most of them made in its own plants (Item 1). The
  reason the contractor comes is the one the filing lists, "Product quality, product innovation, breadth of product
  line, technical expertise, service and price" (Item 1), delivered from a store within reach of the job; Q2 2026's
  release names the levers it is pulling now: "new account wins and increased share of wallet" (EX-99.1,
  `0000089800-26-000046`). The record says the reason has held for at least seventeen years (margins below).
- **Would it stand without the lord?** **[L2007-006]** The chief executive changed in the period read (John G. Morikis as
  chairman and chief executive in the January 2023 release, `0000089800-23-000002`; Heidi G. Petz as chief executive from
  the January 2024 release, `0000089800-24-000011`), and the stores' margin held across the change (below). The advantage
  sits in the store network, the plants and the trade accounts, not in one person.
- **The money test: could a well-funded attacker take it?** **[M2011-015]**, **[M1997-103]** The test has been run by a
  rich attacker, and the attacker's own filing reports the result. PPG Industries, a $15.9B coatings maker (PPG 10-K
  FY2025, `0000079879-26-000046`), owned a U.S. and Canada architectural coatings business with its own stores; its
  results as filed: net sales $2,038M, $2,004M, $1,878M and pre-tax income $26M, $58M and $71M before the loss on sale in
  2022, 2023 and 2024 (1.3%, 2.9%, 3.8% of sales). PPG sold it in December 2024 to American Industrial Partners for
  $516M "and recorded a loss on the sale of $285 million", calling the sale "a strategic shift" that would "improve our
  financial profile, including higher operating margins" (PPG 10-K FY2024, `0000079879-25-000034`, Note 2 and Item 7).
  "Ask the competitors" **[M1999-130]**: the competitor that tried with money said, in its own filing, that it was better
  off out. "If the answer had been yes, we wouldn't have done it." **[M2011-015]**: on this evidence the answer is no.
- **Pricing power, and the agony before a rise** **[M2005-020]**, **[M2000-031]**. Prices rose in the stores in every year
  read: 2010 ("selling price increases", Exhibit 13 to 10-K FY2010), 2019 and 2022 ("selling price increases", 10-K FY2019
  and FY2022), 2023 and 2024 (low-single-digit price, 10-K FY2023 `0000089800-24-000033` and FY2024
  `0000089800-25-000030`), 2025 (price "by a mid-single digit percentage" against a "low-single digit decrease in sales
  volume", 10-K FY2025), and Q2 2026 (mid-single-digit price with low-single-digit volume growth, EX-99.1). In 2025 the
  segment's gross profit rose $364.2M "primarily due to growth in Net sales from favorable selling prices and moderating
  raw material costs" while volume fell (10-K FY2025 MD&A): it charged more and held its customers, the mark of
  "something very special in people's minds" **[M2000-031]**. Contrary evidence **[M1997-127]**: the 2025 volume fall
  shows the price is not without cost; whether price is running ahead of the moat **[M2001-087]** is watched, not shown.
- **Unit volume and share of mind** **[M1999-054]**. Store count 3,390 at the end of 2010 (US, Canada, Caribbean;
  Exhibit 13 to 10-K FY2010), 4,180 at the end of 2016 (Exhibit 13 to 10-K FY2016), 4,853 at the end of 2025, growing
  about 2% a year by the stated objective. Same-store sales rose 11.7% (2022, US and Canada), 6.8% (2023), 1.7% (2024),
  1.7% (2025), 4.2% (Q2 2026). Volume in gallons is not disclosed; the direction words are (2023 mid-single growth, 2024
  low-single growth, 2025 low-single decline, Q2 2026 low-single growth).
- **The low-cost position** **[M2018-043]**, **[L2000-017]**. The segment earned $3,061.5M pre-tax on $6,378.6M of
  identifiable assets in 2025, about 48% (Note 22), and the attacker with money earned 1% to 4% of sales in the same
  product and country. The cost advantage is the scale of a network the competitor could not make pay. Against the
  other large North American maker, Masco's Decorative Architectural Products (Behr, Kilz), sold mainly through The
  Home Depot under a retail exclusivity (Masco 10-K FY2025, `0000062996-26-000005`): operating profit $549M on $2,975M
  (18.5%) in 2024 and $443M on $2,570M (17.2%) in 2025, with 2025 sales volume down 8%; the Paint Stores Group earned
  22.0% and 22.5% pre-tax in the same years with volume down low-single-digit (its figure is after store costs and
  carries no manufacturing mark-up, which sits in Consumer Brands, as the FY2010 segment note says of its day).
- **The brand in the customer's mind; would the customer still choose it over the low bid?** **[M2017-009]**,
  **[M2023-073]**. The professional buys by name from the maker's own store; the filing calls trademark recognition a
  collective contributor "significantly to our sales" (Item 1). No filing figure separates the brand from the service;
  the evidence is the price taken with volume nearly held, above.
- **Widening or narrowing?** **[M1999-108]**, **[L2005-010]**. The stores' pre-tax margin: 13.4% (2008), 14.3% (2009),
  14.2% (2010); 19.9% (2015), 20.8% (2016); 19.4% to 22.1% in 2017 to 2022 as The Americas Group (which then included the
  Latin American stores); 22.3% (2023), 22.0% (2024), 22.5% (2025); 24.6% in Q2 2026 against 24.8% (filings named above).
  The segment's margin rose in the 2009 trough. On the record the moat has widened.
- **What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]**. (1) The home centres reaching
  for the professional painter (The Home Depot holds Behr's retail exclusivity, Masco 10-K FY2025); (2) the divested PPG
  stores under a new owner; (3) a long housing slump, which the 2009 record says cut sales without opening the castle;
  (4) raw-material spikes: the margin dipped to 20.0% and 19.2% in 2021 and 2022 and was back to 22.3% in 2023. None is shown on the evidence
  to be filling the moat. "would you trade our operation for theirs?" **[M2022-021]**: the one rival with stores traded
  out.
- **Consumer Brands and Performance Coatings.** Consumer Brands sells through retailers whose size is a stated risk
  ("the loss of any of our largest customers", Item 1A); its pre-tax margin moved from 9.2% (2023) to
  19.0% (2024) and 16.1% (2025) and its outside sales are $3.2B; much of its value is as the stores' factory. Performance
  Coatings is an ordinary industrial coatings business: 13.9% pre-tax in 2025 (about 17.7% before $258.3M of Valspar
  intangible amortization, Note 22), against PPG's Performance Coatings 20.8% and Industrial Coatings 13.4% segment
  income in 2025 (PPG 10-K FY2025, segment note) — inside the band, no castle shown and none shown open. These two parts
  are carried at Q7 as cash of ordinary certainty **[M1999-104]**; they do not close the file, because the castle that
  carries most of the value is shown standing.

**The competitor row** (same metric: segment pre-tax or operating income as a percent of sales, from each filer's own
10-K):

| business | 2022 | 2023 | 2024 | 2025 | source |
|---|---|---|---|---|---|
| SHW Paint Stores Group (Americas Group in 2022) | 19.2% | 22.3% | 22.0% | 22.5% | 10-K FY2022 `0000089800-23-000007`; 10-K FY2025 `0000089800-26-000008` |
| PPG U.S. and Canada architectural (sold Dec 2024) | 1.3% | 2.9% | 3.8% (before loss on sale) | sold | PPG 10-K FY2024 `0000079879-25-000034`, Note 2 |
| Masco Decorative Architectural (Behr) | | | 18.5% | 17.2% | Masco 10-K FY2025 `0000062996-26-000005` |
| SHW Performance Coatings Group | | 14.5% | 15.1% | 13.9% | 10-K FY2025 Note 22 |
| PPG Performance Coatings / Industrial Coatings | | 19.9% / 13.7% | 21.8% / 13.4% | 20.8% / 13.4% | PPG 10-K FY2025 `0000079879-26-000046` |

- **VERDICT: IN.** The stores' castle is standing on the evidence: a rich attacker with stores earned 1% to 4% and sold
  at a loss, prices rose in every year read, and the margin widened through a trough **[M2011-015]**, **[M1999-108]**,
  **[M2000-031]**. The other two parts are ordinary, not open, and are weighed at Q7.
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**. Tangible operating capital (current assets
  less cash, plus net plant and operating-lease assets, less payables, accruals and operating-lease liabilities;
  `capital.py`, companyfacts first-filed vintage, output `capital_output.txt`) against pre-tax operating income (income
  before taxes plus interest expense less interest income), with the amortization of acquired intangibles added back, since purchased goodwill is set aside when judging the
  business and counted when judging the allocation **[M2011-060]**:

  | FY | tangible capital $M | operating income $M | before acquired amortization $M | pre-tax return |
  |---|---|---|---|---|
  | 2018 | 2,440 | 1,721 | 2,039 | 71% / 84% |
  | 2020 | 1,969 | 2,856 | 3,169 | 145% / 161% |
  | 2022 | 3,288 | 2,956 | 3,273 | 90% / 100% |
  | 2024 | 4,022 | 3,856 | 4,183 | 96% / 104% |
  | 2025 | 4,972 | 3,792 | 4,129 | 76% / 83% |

  The business runs on little tangible capital: accounts payable of $2,354.2M nearly matched inventories of $2,318.2M at
  the end of 2025 (balance sheet). The Paint Stores Group alone earned 48% pre-tax
  on its identifiable assets in 2025 (Note 22). The 2025 fall in the ratio is the new headquarters and R&D center
  (buildings up $1.491B in 2025, MD&A), capital that adds no earning power. A high return is read with care for "a
  cyclical peak in earnings, a monopolistic position, or leverage" **[L1994-009]**: the ratio here is on operating
  capital before financing, so leverage does not make it; the 2009 record (stores margin 14.3% in the trough) says it is
  not a peak artefact alone.
- **Judged with the goodwill in, as capital allocation** **[M2011-060]**: operating income before acquired amortization
  of $4,129M in 2025 on tangible capital plus goodwill and intangibles ($4,972M + $8,037M + $3,966M = $16,975M) is about
  24% pre-tax. The Valspar purchase (2017, $8,810.3M of acquisition spending, companyfacts) is what brings the figure down;
  it is weighed at Q6.
- **What is reinvested to stand still, and to grow** **[L2000-035]**, **[L1999-024]**, **[M2000-144]**. Depreciation was
  $340.3M in 2025 ($263M to $297M in 2018 to 2024). The filer's own guess at the steady need: "Core capital expenditures
  are targeted to be approximately 2% of Net sales in 2026 ... for investments in various productivity improvement and
  maintenance projects ... and new store openings" (MD&A, 10-K FY2025), about $470M at 2025 sales, of which part is
  growth (80 to 100 new stores a year). The Paint Stores Group's own capex was $111.4M, $141.3M and $120.2M in 2023 to
  2025 against its depreciation of $79.0M to $90.2M (Note 22): the store network grows on little capital. The
  Administrative function's $1.4B of capex in 2023 to 2025 (Note 22) was the headquarters and R&D center, a one-off
  that the owner still paid for. **Maintenance judgment:** about the depreciation charge, $300M to $340M a year, so the
  depreciation variant of owner cash ($2,384.5M five-year mean) is the nearer estimate of the steady cash, and the
  all-capex figure ($1,921.5M) carries the store growth and the headquarters.
- **The growth arithmetic** **[M2001-019]**, **[L2007-010]**. From 2018 to 2025, operating income before acquired
  amortization rose $2,089M while tangible operating capital rose $2,532M (`capital_output.txt`), about 83% pre-tax on the
  increment; counting the $2,846M spent on acquisitions in 2019 to 2025 (companyfacts: 77.3, 0, 210.9, 1,003.1, 264.7,
  78.9, 1,211.3) as added capital as well, about 39%. Either reading is the "second" account of L2007-010 at least: growth
  "earned also on deposits that are added". The rate cannot run past its base **[M2003-120]**: sales grew from $17.5B (2018)
  to $23.6B (2025), about 4% a year, and owner cash after all capex from $1,610M to $2,427M (6.0% a year point to point);
  the five-year means grew only about 1.3% a year (2016 to 2020 against 2021 to 2025), because the second five years
  carried the headquarters build and a raw-material squeeze.
- **WEIGHS FOR.** High returns on the tangible capital the business needs and on its increments, with modest compulsory
  reinvestment: the first of the three grades, "more and more money every year without putting up anything to get it, or
  very little" **[M1998-081]**, for the stores; the acquired parts earn less on what was paid for them. (The "little or no
  debt" criterion is applied at Q9.)
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends** **[M2025-032]** (`run_py_output.txt`, first-filed XBRL vintage, read against
  the filed balance sheets of 10-K FY2025, FY2022 and FY2019; USD millions):

  | year-end | assets | equity | goodwill | intangibles | receivables | inventory | total debt | net sales |
  |---|---|---|---|---|---|---|---|---|
  | 2016 | 6,753 | 1,878 | 1,127 | 255 | 1,231 | 1,068 | 1,953 | 11,856 |
  | 2017 | 19,958 | 3,692 | 6,814 | 6,002 | 2,105 | 1,801 | 10,521 | 14,984 |
  | 2019 | 20,496 | 4,123 | 7,005 | 4,734 | 2,089 | 1,890 | 8,685 | 17,901 |
  | 2021 | 20,667 | 2,437 | 7,135 | 4,002 | 2,352 | 1,927 | 9,615 | 19,945 |
  | 2023 | 22,954 | 3,716 | 7,626 | 3,880 | 2,468 | 2,330 | 9,851 | 23,052 |
  | 2025 | 25,902 | 4,598 | 8,037 | 3,966 | 2,791 | 2,318 | 10,871 | 23,574 |

  What moved and why. (1) **2017 is the Valspar purchase**: goodwill and intangibles rose from $1.4B to $12.8B and debt
  from $2.0B to $10.5B in one year; debt has not come down since, standing at $10.9B in 2025 against $8.3B at the 2020 low.
  (2) **Equity is small and says little**: $4.6B against $25.9B of assets, because the company buys in its stock
  ($0.9B to $2.8B a year in 2020 to 2025, companyfacts) and has twice retired the treasury shares against retained
  earnings ($8,061.6M in 2020, statement of shareholders' equity in 10-K FY2022; $7,996M in Q4 2025, MD&A of 10-K FY2025),
  which is why retained earnings print $844M in 2020 and $1,029M in 2025. Book value "means nothing" as a measure here
  **[M1998-116]**. (3) **Receivables and inventory track sales**: receivables 10.4% of sales in 2016 and 11.8% in 2025
  (62 days against 58 in 2024, MD&A, with the Suvinil purchase in the year-end figure); inventory 9.0% and 9.8%. No
  build-up out of line with sales **[M1995-064]**. (4) **Cash is kept minimal** ($207M) and the seasonal working capital
  is financed with commercial paper (Item 1, Working Capital). (5) **Other current assets** rose from $438M (2023) to
  $691M (2025), "primarily related to prepaid expenses and recoverable income taxes" (MD&A); written down as a watch item
  under the prepaid-accounts tell **[M1995-064]**, explained in part by the 2025 tax law's expensing, not suspicious on
  its own. What the figures cannot say: the stores' profit carries no manufacturing mark-up, which the segment note sets
  in Consumer Brands, so the stores' castle is understated in the segment figures and Consumer Brands' overstated **[M2025-032]**.
- **The real costs** **[L2021-003]**, **[R1996-023]**. Depreciation ($340.3M in 2025) is deducted in full; capital spending
  ran above it in every year 2022 to 2025 (Step 0), so depreciation does not understate the cost **[L2015-004]**. Stock
  pay ($115.9M to $138.1M a year) is a real cost and deducted **[L2015-003]**; the company's adjusted figures do **not**
  exclude it (EX-99.1 reconciliations). Restructuring ("Severance and other restructuring expenses") was $15.3M of
  provisions in 2023, none in 2024, $111.0M in 2025, and continues in 2026 ($0.07 a share in Q2 2026, EX-99.1): three of
  four years, a recurring "one-time" cost that is left in the owner-cash figure **[L2016-007]**. The amortization of
  acquired intangibles ($336.6M) is not deducted from owner cash, since "Some truly deplete over time while others never
  lose value" **[L2012-003]**; it is mostly Valspar's trademarks and customer relationships. The cost of tax credits bought
  through affordable-housing partnerships ($104.0M amortization in 2025) is deducted (Step 0). Pensions are small: $83.3M
  underfunded and $125.6M of retiree medical liability at the end of 2025 (MD&A).
- **EBITDA in the filer's own mouth** **[M1998-086]**, **[L2012-002]**. The 10-K reports "EBITDA of $4.480 billion and
  Adjusted EBITDA of $4.609 billion", targets "Net debt ... to be 2.0 to 2.5 times EBITDA", and the credit covenant is set
  on EBITDA (MD&A, Financial Covenant); the Q2 2026 release leads with EBITDA and "adjusted EBITDA margin". Coverage the
  rows' way, "pre-tax earnings/interest, not EBITDA/interest" **[L2012-002]**: ($3,338.2M + $465.0M) / $465.0M = **8.2
  times** in 2025. The EBITDA talk weighs against; it is used as a leverage yardstick, not offered as the earnings (the
  owners are given net income and an adjusted per-share figure after depreciation), and capital spending runs above
  depreciation, so the habit has not hidden a capital cost here. Whether EBITDA talk of this kind is the STOP of
  **[M2002-026]** or a weighing is not settled in the framework's Q4 text; it is read here as a weighing (see the last
  section).
- **Adjusted earnings featured; guidance and the habit of making it.** The releases headline "Adjusted diluted net income
  per share", which removes Valspar amortization and restructuring (EX-99.1, `0000089800-26-000046`) **[L2016-006]**. The
  company gives annual earnings guidance. The record against it (January releases, `guidance_extract.txt`): 2023 guided
  $6.79 to $7.59 diluted, reported $9.25; 2024 guided $10.05 to $10.55, reported $10.55; **2025 guided $10.70 to $11.10,
  reported $10.26, below the range** (adjusted guided $11.65 to $12.05, reported $11.43). A management that misses its own
  range in a soft year is not one that "consistently reach[es] their declared targets" **[L2002-041]**; no make-the-numbers
  habit is shown, so the two-tell line (Q4 CONVENTION) is not reached.
- **What the accounts say of management's character** **[M1995-064]**. The headquarters sale-leaseback was booked as a
  financing, with the building kept on the balance sheet and the $800M as a liability (MD&A, Real Estate Financing): the
  conservative treatment. Supplier finance is disclosed with its rollforward and is stable ($213.1M, $215.7M, $206.1M,
  10-K FY2025). The adjusted figures leave stock pay in. The 10-K explains price, volume and mix by segment in plain words.
- **VERDICT: IN on confusion** (the accounts can be read and say what the business earns); **WEIGHS AGAINST on
  weighing**, lightly: EBITDA used as the debt yardstick and adjusted earnings headlined **[L2016-006]**, **[M2002-026]**,
  with a recurring restructuring line. Owner cash for Q7 is the Step 0 figure, after every real cost.
## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet **[M2007-081]**; the reading is the 10-K, the releases and the
proxy (DEF 14A, `0000089800-26-000025`).

- **The first yardstick: the record against the hand dealt** **[M1994-008]**. The stores' margin widened from 13% to 14% in
  2008 to 2010 to about 22% in 2023 to 2025 while the one rival with stores and money (PPG) earned 1% to 4% and left
  (Q2). The managers are long-service insiders: the chief executive, Heidi G. Petz, ran the Consumer Brands Group and
  then The Americas Group before becoming president and chief operating officer (2022) and chief executive (2024); the
  head of Global Architectural has been with the company since 1997 and the head of Consumer Brands since 1993 (10-K FY2025,
  executive officers). Ability shows in "a long record, not a promise" **[M1996-038]**; the record here is the
  company's over many managers, not one person's **[L2007-006]**.
- **The second yardstick: how they treat the owners** **[M1994-009]**, read at Q6 Part B (pay, board, buybacks).
- **The tells of dishonesty, looked for** **[M1995-111]**, **[M2007-082]**, **[M2003-029]**. (1) The key figures are
  reported: price and volume direction by segment, same-store sales, store counts, the stores' margin, every year read.
  (2) The bad year is reported as one: the January 2026 release states diluted EPS "decreased 2.7%" and the 10-K Outlook
  names "continued demand choppiness" and a "softer-for-longer demand environment"; the 2025 miss against guidance was
  not dressed up as a beat (Q4). (3) Too good to be true **[M2002-028]**: no; guidance was cut-to-cloth and missed in
  2025. (4) Stock price in the lobby **[M2004-067]**: no instance found (a text search of the 10-K FY2025, the proxy and the
  Q2 2026 release for "price target" returns none; the proxy's pay-versus-performance table reports TSR as required). (5) Language: the
  10-K and proxy carry consultant-style slogans ("Success by Design", "Create Your Possible", "above market growth")
  **[M1998-038]**, **[M2007-083]**; the CEO's quarterly remark that the company "continued to outperform the market" is
  promotion of a mild kind. (6) Accounting conduct: the conservative financing treatment of the headquarters
  sale-leaseback, stock pay kept in the adjusted figures (Q4). (7) A candidate tell considered: the 2025 annual-incentive
  "Adjusted EPS" target of $11.05 sat below the $11.65 to $12.05 adjusted range the company had guided owners to in
  January 2025 (proxy, 2025 Annual Cash Incentive Financial Performance Goals; release `0000089800-25-000015`). Both
  figures are disclosed, and the proxy reconciles its adjusted measures in Appendix A; it is a fact about how the board
  pays the managers, not a concealment, and it is weighed at Q6 Part B rather than read as dishonesty.
- **Love of the business, and the same after being paid** **[M2000-098]**, **[M2009-072]**. Hired managers, not
  founder-sellers, so the after-the-sale test does not apply as written **[M2007-081]**. What can be read: the chief
  executive owned 26,867 shares at the record date of 25 February 2026, about $8.6M at $318.46, against 2025 pay of
  $14,914,317 (proxy, ownership table and Summary Compensation Table); all 19 directors and officers together owned
  199,598 shares, under 0.1% (proxy). The executives are bound to six times salary (CEO) by guideline (proxy, Stock
  Ownership Guidelines). Ownership is modest beside the pay; no instance found of an executive buying shares with his or
  her own money in the documents read **[L2019-008]**.
- **What ability shows in** **[M2000-153]**, **[L1996-033]**. Focus: one industry, paint and coatings, for the whole
  record read. Facing reality: the 2026 outlook calls demand soft rather than forecasting a recovery. Against: the
  Valspar purchase loaded $10B of debt and $11B of goodwill and intangibles onto the balance sheet (Q4), and its
  Performance Coatings part earns an ordinary margin (Q2); the Suvinil purchase added $1.15B more in 2025.
- **VERDICT on integrity: IN** (no doubt found that the people are dishonest; the rows apply the rule on doubt
  **[M2013-088]**, and the doubts found are about pay design and promotion, which are weighed, not about honesty).
  **Ability WEIGHS FOR**: the record of the stores against the hand dealt **[M1994-008]**, with the acquisition record
  weighed at Q6.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**, **[M2011-072]**. Over 2021 to 2025, diluted earnings per share
  were $6.98, $7.72, $9.25, $10.55 and $10.26 (sum $44.76; 10-K FY2022 and FY2025) and dividends per share $2.20, $2.40,
  $2.42, $2.86 and $3.16 (sum $13.04; statements of shareholders' equity, 10-K FY2022, FY2024 `0000089800-25-000030`,
  FY2025): **$31.72 a share retained**. The filed price at each end: the company's own December purchases, $724.82 a share
  in December 2020 (10-K FY2020, `0000089800-21-000010`, Item 5), $241.61 after the 2021 three-for-one split, and $333.93
  for the employee transactions of December 2025 (10-K FY2025, Item 5): **$92.32 a share of market value added**, about
  $2.9 for each dollar kept. The market leg passes. The forward leg reads less well: diluted EPS rose from $7.36 (2020,
  as recast in 10-K FY2022) to $10.26 (2025), $2.90 a share on $31.72 retained, about 9% after tax, and most of the
  retained money did not stay in the business: treasury stock purchases of $8,462M in 2021 to 2025 exceeded net income
  less dividends ($8,180M) (companyfacts; cash-flow statements). "Can you keep using all of the capital you generate,
  effectively, for a very long time?" **[M2010-097]**: the stores can use a little at very high returns (Q3); the rest is
  returned through buybacks or spent on acquisitions.
- **Buybacks** **[L1999-023]**, **[L2011-003]**, **[L2016-002]**. The programme names no price: shares are bought "for
  general corporate purposes, and depending on its cash position and market conditions", with "no expiration date"
  (10-K FY2025, Item 5 and MD&A). Prices actually paid (purchases / shares, from the 10-Ks and the Q2 2026 10-Q): 2022
  $883.2M / 3.4M = **about $260**; 2023 $1,432.0M / 5.6M = **about $256**; 2024 $1,738.8M / 5.2M = **about $334**; 2025
  $1,656.4M / 4.8M = **about $345**; first half of 2026 $1,837.0M for 5.6M shares at **$328.04** on average, including an
  accelerated share repurchase entered into in June 2026 (10-Q, Treasury Stock). The Q7 range (below) is **$140 to $225** a share
  (all-capex) or $174 to $279 (depreciation variant). Every year's average price sat above the top of the all-capex range,
  and the 2024 to 2026 prices above the top of the depreciation variant too. Under the Q6 CONVENTION (the prices paid set
  against the bottom of the Q7 range), the exception is not met: **weighs against** **[L2016-002]**, **[M1996-013]**. The
  first half of 2026 was paid for partly with borrowed money: total debt rose from $10,871.3M to $12,072.1M in the six
  months while $1,837.0M went to repurchases and $394.6M to dividends against $1,486.6M of operating cash (10-Q
  `0000089800-26-000049`), so the purchases were not made only with funds "beyond the near-term needs of the business"
  **[L1999-023]**; the company manages to a leverage target, "Net debt ... 2.0 to 2.5 times EBITDA" (MD&A).
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**. No stock was issued for acquisitions in the period read; the
  share count fell from 254.5M (end 2023) to 242.8M (June 2026). Valspar (2017, $8,810.3M of acquisition spending,
  companyfacts) and Suvinil (2025, about $1.15B, MD&A) were paid in cash raised largely by borrowing. The all-stock STOP
  **[L2009-019]** does not arise. Value given against value got: in 2025 the parts that are mostly Valspar (Performance
  Coatings, and the non-store sales of Consumer Brands) earned 13.9% and 16.1% pre-tax, and the whole company earned about
  24% pre-tax on tangible capital plus purchased goodwill and intangibles (Q3), against a debt of about $10B still carried
  from the purchase (Q4): a fair, not a rich, return on what was paid; no post-mortem against the 2017 projections was
  found in the documents read **[L2014-013]**.
- **Dividends** **[M2000-051]**, **[L2012-015]**. Raised for 47 consecutive years and set as a ratio: "The Company's
  2025 annual cash dividend of $3.16 per share represented 30% of 2024 diluted net income per share" (MD&A). Consistent
  and clear; set by ratio, which the rows call "nuts" as a method **[M2000-051]**, though small beside the buybacks.
- **Part A WEIGHS AGAINST**: the buybacks are made at prices above the value range, with no stated price and in 2026
  partly with debt; the market leg of the retention test passes.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls?** **[M2003-019]**, **[M2016-083]**. The 2025 annual incentive for the CEO,
  CFO and chief legal officer: net sales 25%, Adjusted EPS 40%, Adjusted FCF 35%; for the segment heads, sales, profit
  before tax and return on net assets employed of their business (proxy, 2025 Annual Cash Incentive). The segment
  measures fit the people; the per-share measure rises with buybacks made above value.
- **The hurdle** **[M2004-097]**. The bars sit at or below what was already earned. The 2025 annual Adjusted EPS target
  was **$11.05** (threshold $8.84) against $11.33 adjusted earned in 2024 and the $11.65 to $12.05 the company guided owners
  to in January 2025 (release `0000089800-25-000015`); NEOs nonetheless earned "an average of 110.86% of their 2025 target
  annual cash incentive" in the year the company fell below its own guidance (proxy). The 2023 to 2025 PRSUs set a
  cumulative Adjusted EPS target of **$23.20** (about $7.73 a year) when 2022 adjusted EPS had been $8.73 (release
  `0000089800-23-000002`); the result was $30.77 and the units vested at **200%** (proxy, Vesting of 2023–2025 PRSUs). The
  2025 to 2027 target is $34.85 cumulative (about $11.62 a year), threshold $31.37 (about $10.46 a year, below the $11.43
  of 2025). "a lousy manager will always suggest an arrangement like that" **[M2004-097]**: a bar set below the year
  already in hand pays for treading water **[L1994-021]**.
- **Options** **[L1998-028]**, **[M1997-043]**, **[M2011-067]**. Options are 40% of the long-term award, ten-year term,
  strike at the grant-date average price, no step-up for retained earnings (proxy, 2025 Stock Option Grants). They are
  expensed (stock pay is in the income statement and deducted in owner cash). No repricing, double-trigger vesting, no
  hedging or pledging, a clawback (proxy).
- **Who designs it** **[M1997-041]**, **[M1998-066]**. Targets "using the market median" and a compensation peer group
  (proxy); a consultant (Mercer, retained 2025) whose affiliates were also paid about $920,200 for other services to the
  company in 2025 (proxy). Ratchet by comparables **[M2012-095]**.
- **The board** **[L2014-026]**, **[M2007-120]**. The chief executive also chairs the board (since January 2025, 10-K FY2025),
  with a lead independent director (proxy). Directors are paid partly in RSUs that count toward their ownership
  guideline; the directors' own holdings in the ownership table range from 173 to 11,754 shares (proxy), small against
  the pay; no instance found of directors' purchases "with their savings" **[L2019-008]**.
- **Owners as partners** **[L1994-023]**, **[M2022-054]**. Annual earnings guidance and an adjusted per-share figure as the
  headline (Q4) are the opposite of Berkshire's own practice by inversion **[M2022-054]**; the 10-K's disclosure is full
  and plain (Q4, Q5).
- **Part B WEIGHS AGAINST**: bars set at or below results already earned, paid above target in a year below guidance and
  at 200% on a three-year target below the prior year's level **[M2004-097]**, **[L1994-021]**; a combined chair and chief
  executive **[L2014-026]**; modest ownership.

**WEIGHS AGAINST** on both parts. No STOP in Q6 is met (no all-stock deal by an undervalued acquirer **[L2009-019]**; no
serial issuance **[L2014-015]**).
## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[R1996-018]**, as a range
**[L2000-024]**. Construction by the CONVENTION (Q7, with the four PG specifics); script `value.py`, output
`value_output.txt`.

- **Cash input:** five-year mean of owner cash after every real cost, 2021 to 2025, **$1,921.5M** (Step 0; all capital
  spending deducted); the depreciation variant, $2,384.5M, is shown beside it, and the maintenance judgment at Q3 puts the
  steady cash nearer the second figure once the headquarters build is past.
- **Growth shown** on aggregate owner cash: five-year mean to five-year mean (2016 to 2020 against 2021 to 2025) **1.3% a
  year**; 2018 (the first full year with Valspar) to 2025, point to point, **6.0% a year**; 2021 to 2025 point to point
  9.0% a year, rejected because 2021 was a working-capital trough year and "a base year in which earnings were poor can
  produce a breathtaking, but meaningless, growth rate" **[L2005-003]**. The top case uses 6.0%, the highest rate the
  record supports without a picked base year. **Capped by Q3:** 6.0% sits just above the discount rate; carried ten years
  and then stopped, it does not run "into infinite numbers" **[M1997-095]**, and owner cash of about $3.4B in 2035 against
  sales of $23.6B today is not an absurdity **[M1999-067]**; the strict reading (no rate above the discount rate) gives
  5.66%, shown below.
- **Ten years, then no real growth** (zero nominal), discounted throughout at **5.66%**.

| case | value $M | per share (242.758M) | depreciation variant, per share |
|---|---|---|---|
| no growth (bottom) | 33,949 | **$139.85** | $173.54 |
| 1.3% for ten years (five-year means) | 37,627 | $155.00 | $192.34 |
| 5.66% for ten years (strict cap) | 53,164 | $219.00 | $271.77 |
| 6.0% for ten years (top) | 54,616 | **$224.98** | $279.19 |
| 9.0% (2021 base, rejected) | 69,018 | $284.31 | $352.81 |

- **Value range: $140 to $225 a share against $318.46** (depreciation variant $174 to $279). Width about 1.6 to 1, inside
  the three-to-one CONVENTION, so a conclusion can be drawn **[L2000-025]**.
- **How sure** **[M1999-104]**. The stores' cash is sure in the sense the rows mean (Q2); Performance Coatings and the
  Latin American parts are of ordinary certainty; the debt is serviced 8.2 times by pre-tax earnings (Q4). Two items lower
  the base and are not in the five-year mean: interest expense "is expected to increase by approximately $85 million in
  2026" (MD&A), which takes about $65M after tax off the base (no growth $135.09, top $217.33), and the $1.2B of debt
  added in the first half of 2026 for buybacks (Q6). Neither moves the box.
- **The price against the range.** The price is above the top of the range on both variants. At $318.46 the expected
  return on owner cash is **2.5% to 4.1% a year after corporate tax** (no growth to 6.0% growth), 3.1% to 5.0% on the
  depreciation variant. The price implies owner cash growing about **10.4% a year for ten years** at the bond rate, and
  about **15.2% a year** to earn the floor; the record shows 1.3% to 6.0%.
- **Pre-tax and after-tax, stated.** Owner cash is after corporate tax. The floor CONVENTION is about ten percent pre-tax
  ("at least 10% pre-tax returns" **[L2002-020]**); at Sherwin-Williams' own 2025 effective rate of 23.1% (MD&A) that is
  **7.69% on after-tax owner cash**, and the expected returns above are about 3.2% to 5.3% pre-tax (4.0% to 6.5% on the
  depreciation variant). Under the CONVENTION's fourth specific, a price above the top of the range closes OUT through the
  floor: "there’s just a point at which we drop out of the game" **[M2003-149]**.

**Reported for the operator (COMPUTATION — NOT A CLEARANCE, since the file closes at this STOP):**
- **Value range:** $140 to $225 a share (all-capex); $174 to $279 (depreciation variant).
- **Fair price** (the top case, 6.0% growth for ten years, returns the floor of about 10% pre-tax, 7.69% after tax):
  **about $161** (depreciation variant about $199). Below the bottom of the range, so the floor and the range agree that
  any price inside the range is too close.
- **Cheap price** (owner cash with **no growth at all** returns the floor): **about $103** (depreciation variant about
  $128); below it the case "ought to just kind of scream" **[M1996-084]**. The price is 3.1 times the cheap price and about
  2.0 times the fair price.
- **Q6's buyback test, recorded back:** every year's average repurchase price, 2022 to the first half of 2026 ($256 to
  $345), sat above the top of this range (Q6).

- **VERDICT: OUT.** Valued, with a range narrower than three to one, and the price above its top: the expected return at
  the price (about 3% to 5% pre-tax, at most about 6.5% on the most generous variant) is below the floor of about ten
  percent **[M2003-149]**, **[L2002-020]**, and nowhere near a price that would "scream" **[M2009-005]**. The castle is real
  (Q2) and the business is good (Q3), but "You can turn any investment into a bad deal by paying too much" **[M2019-015]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (the file closed OUT at Q7). For the record only: the 30-year Treasury at 5.66% exceeds the 3.2% to 5.3%
pre-tax expected return at the price, so the bond would win the first filter **[M1997-089]**.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a clearance. Noted for a later run: total debt $12.072B at 2026-06-30 against equity of $4.598B at the end of 2025, a
leverage covenant of 3.75 times EBITDA, a stated target of 2.0 to 2.5 times, $2.246B of short-term borrowings and
$1.498B of current long-term debt (10-Q); pre-tax interest cover 8.2 times (Q4); the lead-pigment litigation named in
Item 1A. The "little or no debt" criterion **[R1997-001]** is stated for whole businesses and would not be met here.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. What the draft would have the buyer do: nothing; "your default position is always short-term instruments"
**[M2004-045]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT ASKED (the file closed at Q7). Noted: paint and coatings are not among the named businesses; the legacy lead-pigment
litigation (Item 1A) would be the newspaper-test item **[M2008-011]**.
---
## THE BOX
**OUT, at Q7.** Value range **$140 to $225 a share** (depreciation variant $174 to $279) against **$318.46**: the price is
above the top of the range, the expected return at the price is about 3% to 5% pre-tax against a floor of about ten
percent **[M2003-149]**, **[L2002-020]**; fair price about $161, cheap price about $103 (COMPUTATION). Q1 IN, Q2 IN (the
paint stores' castle: PPG's stores earned 1% to 4% and were sold at a loss; prices up in every year read; margin widened
from 13% to 22%), Q3 weighs for, Q4 IN on confusion and weighs against (EBITDA and adjusted EPS featured), Q5 IN on
integrity and ability for, Q6 weighs against (buybacks above the range with no stated price, partly debt-funded in 2026;
pay bars set below results already earned). Not a TOO HARD, so no research pass is opened. **What would reverse it:** a
price at or below about $161 (the top case clears the floor) or, for no pencil, about $103; or five more years of owner
cash growing near the 10% a year the price now implies.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits 923dad2 (template), de8c4ed (Step 0 to Q1), 7b86420 (Q2), 853ce82 (Q3), 450bc02 (Q4), 83574ba (Q5),
      1f09382 (Q6), 9c56749 (Q7 to Q12), and the final commit.
- [x] Every v5 id resolves (`ids.py` checks every M, L and R id in this file against `principle_ledger_v5.csv`: none
      missing); every filing fact has its accession; no number without a row or a filing, and the conventions used
      (Q7 range and floor, the Q6 buyback reading, the two-tell line) are named as such.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are marked NOT REACHED and carry no
      clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash less stock pay, all
      capital spending and the cost of tax credits bought; the sovereign from the US Treasury (issuing authority); the
      price is an aggregator quote and is flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations; Q1; Q2 on the 2025 volume fall).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its owner-cash figure was recomputed with the
      tax-credit cost it omits.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The growth input of the Q7 CONVENTION is still a choice.** "The growth the business has actually shown"
gave 1.3% (five-year mean on five-year mean), 6.0% (2018 to 2025), 7.1% (three-year means 2016-18 to 2023-25, which
include the Valspar purchase) or 9.0% (2021 to 2025) from the same filed table; and on the all-capex basis a one-off
headquarters build ($1.4B in 2023 to 2025) depresses the growth that the depreciation variant shows at 9% a year. The run
took 6.0% (no picked base year, no acquisition step) and showed the others; the box did not depend on it, since even the
rejected 9.0% case ($284) and the depreciation variant's top ($279) sit below the price. A rule for the window (and for
an acquisition inside it) would remove the choice. (2) **EBITDA talk: STOP or weighing?** Q4's text quotes
**[M2002-026]** as a stop "stated as a count" and lists "managements that talk it" under What it rules OUT, while the
heading makes Q4 a STOP only on confusion or suspicion. Sherwin-Williams uses EBITDA as its leverage yardstick and
covenant, not as earnings; the run weighed it, as the 2026-10-05 runs read for form did, but the text does not say which
reading governs. (3) **Pay targets below public guidance** have no named place: Q5's tells and Q6 Part B's hurdle test
**[M2004-097]** both touch a board that sets the managers' bar below what it tells owners to expect; the run weighed it in
Q6 Part B. (4) **The pre-tax floor against after-tax owner cash** needs a stated conversion; the run used the company's
own effective rate (23.1%), as the HUBB run did, which the framework does not say.
