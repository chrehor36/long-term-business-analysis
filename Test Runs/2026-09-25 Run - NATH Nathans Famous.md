# Company Run — Nathan's Famous, Inc. (NATH) — 2026-09-25
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**CLAIMED AT DISPATCH 2026-09-25.** Unattended overnight cycle. Sections are appended as each question closes. Research: `Test Runs/_research 2026-09-25 NATH/`.

*Wave 7 name 36 of 218 (line 36 of `Screens/_daily/_wave7_order.txt`; 35 lines in `_wave7_done.txt` at claim, the last being CAH). No `*Run - NATH*.md` existed in `Test Runs/` at claim.*

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
## THE FACT THAT CHANGES WHAT THE QUOTE IS: A LIVE CASH MERGER, BY THE LICENSEE

**The screen row's `deal_note` is blank and the brief said to check anyway. A deal is live.** On
2026-01-20 Nathan's signed an Agreement and Plan of Merger with **Smithfield Foods, Inc.** (and
Boardwalk Merger Sub Inc.) at **$102.00 per share in cash** (8-K Item 1.01 filed 2026-01-21, accession
`0001104659-26-005233`, merger agreement as Exhibit 2.1; PREM14A 2026-03-06 `0001104659-26-024713`;
**DEFM14A filed 2026-09-24, accession `0001104659-26-110393`, accepted 20:05:13Z, i.e. 16:05 EDT, after
that day's close**). **Smithfield is the counterparty of Nathan's largest contract**: *"Since March 2014,
we have held an exclusive license to manufacture, distribute, market and sell "Nathan's Famous" branded
hot dogs, sausages, corned beef and certain other ancillary products through retail outlets in the U.S.
and Canada and Sam's Clubs in Mexico. The license is scheduled to expire in March 2032."* (Smithfield
10-K FY2025, accession `0000091388-26-000014`). **The licensee is buying the licensor.** What the
DEFM14A says, read:
- **HSR**: filed 2026-01-23, *"the applicable waiting period expired at 11:59 p.m., Eastern Time, on
  February 23, 2026."*
- **CFIUS** (Smithfield is about 87% owned by WH Group of Hong Kong, per its own 10-K): Declaration
  2026-01-23, Notice 2026-06-08, and *"CFIUS Clearance was obtained on September 17, 2026."* **No 8-K
  announced the clearance**: the submissions index shows nothing between the GAMCO 13D/A of 2026-08-31 and
  the DEFM14A. **The first public statement of it is the DEFM14A, filed after the 2026-09-24 close**, so the
  close used below predates it.
- **Special meeting 2026-10-23**, record date 2026-09-22 (4,097,661 shares entitled to vote). **A Voting
  Agreement binds the directors and certain holders, about 29.9%**; directors and executive officers own
  about 31.0%; Howard M. Lorber alone 989,841 shares, 24.2% (13D/A No. 14, `0001104659-26-005238`);
  GAMCO/Gabelli about 10.8% (13D/A of 2026-08-31, `0000807249-26-000078`).
- **End Date** 2026-06-22, automatically extended to 2026-10-20 for the CFIUS and HSR conditions; the
  termination right is not available *"to either party until five business days after the completion of
  the Stockholders' Meeting"* where those conditions were satisfied before the End Date, which the CFIUS
  date says they were. Company termination fee **$10,581,814**; Parent fee **$7,407,270** on a CFIUS
  turndown, conditional on Nathan's electing to extend the Smithfield licence four years to **2036-03-02**.
  **The price was cut from $103.50 to $102.00** in January 2026 after Smithfield's diligence found *"an
  approximate $20 million gap in its valuation of the Company related to certain matters identified in
  Parent's due diligence findings"* (DEFM14A, Background; carried to Q3 beneath the close).
- **The dividend stops**: *"After the payment of the June 2026 Regular Cash Dividend, the Company is no
  longer permitted to declare and pay any further dividends under the Merger Agreement."* (10-K MD&A).

**What this does, per the ROKU precedent of 2026-09-12:** it excuses no gate. Q1-Q4 are about the
business and are run on the filings in order. It changes **what the price is**: $94.29 against $102.00 in
cash, **the price is 92.4% of the consideration**, a merger spread on a transaction whose last regulatory
condition had been met a week earlier but was not yet public at that close. **Whoever buys at $94.29 is
underwriting the vote and the closing, not the hot dog.** That trade is an arbitrage, the corpus's
*parking place* category **[E2-74]**, and this framework has nothing to say about it.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never a forecast **[E4-15, E3-32]**:
- rate **5.47 %** · date **09/24/2026** (the newest row when struck on 2026-09-25) · source (issuing
  authority) **US Treasury daily par yield curve, 30 Yr**, `home.treasury.gov` daily-treasury-rates CSV for
  2026, struck fresh and saved raw as `Test Runs/_research 2026-09-25 NATH/treasury_2026.csv`; neighbouring
  row 5.40 (09/23). `python tools/run.py NATH` printed the same rate and date. **FRED not used.**
- FX: **not required.** International revenue was $3,443K of $162,063K in FY2026 (2.1%); the licences, the
  Branded Product Program and the restaurants are US-dollar businesses. USD sovereign.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the year ended 2026-03-29, filed 2026-06-09, accession `0001437749-26-019923`**
    (`nath20260329_10k.htm`). Read: cover; Item 1 whole (the three channels, the Licensing Program with the
    Smithfield terms, Provisions and Supplies, Competition, Trademarks, Seasonality); Item 1A whole; MD&A
    whole (results by line, the EBITDA and Adjusted EBITDA reconciliation, liquidity, the Credit Agreement,
    repurchases, dividends); the statements of earnings, changes in stockholders' deficit and cash flows
    with every reconciliation line; Notes A, B (policies), I (segments), J (debt), K (leases), L (stock
    plans, benefit plans), M (commitments), N (merger), O.
  - **10-K/A filed 2026-07-24, accession `0001104659-26-086491`** (Part III; carried beneath the close).
  - **10-Q for the quarter ended 2026-06-28, filed 2026-08-07, accession `0001437749-26-026427`** (cover,
    MD&A, debt note, EBITDA reconciliation).
  - **Earlier 10-Ks, FY2010-FY2025, sixteen documents downloaded from EDGAR** (accessions listed at the end
    of Q1), read for the licensing history (the SMG agreement at *"royalties ranging between 3% and 5% of
    sales"* to March 2014; John Morrell & Co., Smithfield's subsidiary, from March 2014 at 10.8%), the
    royalty-and-volume sentences of every year's MD&A, the debt-funded special dividends and the notes.
  - **8-K of 2026-01-21 with Exhibits 2.1, 2.2, 10.1, 10.2 and 99.1; the DEFM14A of 2026-09-24**; the 8-K
    earnings releases of 2025-06-10, 2025-08-08, 2025-11-06, 2026-02-05, 2026-06-09 and 2026-08-07 (on disk);
    the DEF 14A of 2025-07-25 (`0001104659-25-070823`).
  - **Smithfield Foods 10-K FY2025, accession `0000091388-26-000014`**, for the licensee's own brands, its
    competitor list and its Packaged Meats segment.
- **figure cross-checked against the filed statement: FY2026 net cash provided by operating activities,
  $18,234K**, rebuilt from its own lines: net income 20,020 + D&A 925 + amortisation of debt issuance costs
  70 + share-based compensation 1,132 + credit-loss provision 129 − deferred taxes 88 = 22,188 (the MD&A's
  *"other non-cash operating items of $2,168,000"* is 22,188 − 20,020; ties); working capital: receivables
  −5,906, inventories +330, prepaid +64, other assets +28, lease assets and liabilities −193, payables and
  accruals +2,238, deferred franchise fees −305, other liabilities −210 = −3,954 (the MD&A's *"changes in
  other operating assets and liabilities of $3,954,000"*; ties); **total 18,234. Ties.** The XBRL pull
  (`xbrl_out.txt`, `vintage="newest"`) carries the same $18.234M.
- *If the filing could not be obtained → **UNRESEARCHED**.* **Not invoked.**

**THE PRICE AND THE CAP** *(struck by this run)*
- **Share count, quoted from the cover of the 10-Q for the quarter ended 2026-06-28, accession
  `0001437749-26-026427`, the latest periodic filing:** *"At August 3, 2026, an aggregate of 4,097,661 shares
  of the registrant's common stock, par value of $.01, were outstanding."* **One class**: Section 12(b)
  registers the common stock alone; the balance sheet shows *"Common stock, $ .01 par value; 30,000,000
  shares authorized"* and no preferred. The DEFM14A's record-date count (2026-09-22) is the same 4,097,661.
  `python Screens/cover_shares.py NATH` returned the same document, accession and count.
- **Price $94.29** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint, raw
  response `price_raw.json`; 49,500 shares traded). Two-year closing range in the pull **$76.79 to
  $115.75**; $92.73 on 2026-01-20 before the announcement, $100.79 the day after, $97.94 on the CFIUS date,
  $94.29 on 2026-09-24.
- **cap = close × shares**, `close` never `adjclose`: $94.29 × 4,097,661 = **$386.4M.** At the deal price
  the shares are $418.0M. The screen's $403M is an earlier price on a similar count.
- **The balance sheet beside the cap:** Term Loan **$47.8M** at 2026-06-28 (unsecured Citibank facility,
  SOFR + 1.40%, maturing 2029-07-10; covenants a fixed charge ratio and net leverage not above 3.00x;
  *"certain Change of Control events constitute an Event of Default"*, and *"the Buyer at the Effective Time
  shall pay all outstanding obligations under the Credit Facility"*); cash $24.4M at 2026-03-29; total
  stockholders' **deficit $(14.2)M** at 2026-03-29, the residue of the debt-funded distributions below.

**THE PERIMETER, read before any question.**
- **Acquisitions: none found.** No acquisition line appears in any cash-flow statement FY2010-FY2026 read;
  Arthur Treacher's is an owned trademark carried as a small amortising intangible.
- **Two debt-funded recapitalisations and a third special dividend from cash:**
  1. **March 2015**: *"On March 10, 2015, the Company completed an offering of $135.0 million aggregate
     principal amount of 10.000% Senior Secured Notes due 2020 (the "Notes"). The Company used the net
     proceeds of the Notes offering to pay a special dividend of $25.00 per share (approximately $116.1
     million)"* (10-K FY2015, `0001437749-15-012185`).
  2. **November 2017**: $150.0M of 6.625% Senior Secured Notes due 2025, used to redeem the 2020 notes
     (*"paid a call premium of $6,750,000"*) and toward *"a special $5.00 per share cash dividend"* ($20.9M,
     paid January 2018; *"Nathan's also funded the majority of the special dividend through its existing
     cash"*) (10-K FY2018, `0001437749-18-011457`).
  3. The 2025 notes were bought down to $60M and refinanced on **2024-07-10** by the **$60M unsecured Term
     Loan**; **December 2025, a $2.50 special dividend** from cash (FY2026 dividends paid $18,403K including
     four regular $0.50 quarters).
- **Buybacks**: the sixth plan, 1,101,884 shares for about $39.0M; 5,289,515 shares in treasury at a cost
  of $86.7M; none in FY2025-26, and the merger agreement forbids them.
- **Regular dividend** from June 2018 ($0.25 a quarter, later $0.50), stopped by the merger agreement after
  June 2026.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words.** Nathan's owns a 110-year-old hot dog brand and makes money from it
  three ways.
  1. **It rents the name to a meat packer.** Smithfield makes, sells, prices and promotes Nathan's packaged
     hot dogs in US supermarkets and club stores and pays Nathan's **10.8% of net sales** monthly, *"subject
     to minimum annual guaranteed royalties"*, under an agreement that runs to **March 2032**. Nathan's
     supplies no plant, no sales force, no retail pricing. Smithfield's royalties were **$33,589K in FY2026**
     ($31,893K retail plus $1,696K foodservice), **20.7% of revenue** and *"approximately 90%"* of licence
     revenue. Smaller licences (Lamb Weston fries to July 2028, Solina spices, pickles, snacks) bring the
     licence line to $37,417K. **The Product Licensing segment earned $37,234K of operating income: 84.4% of
     the three operating segments' $44,136K in FY2026 (79.6% in FY2025).**
  2. **It sells hot dogs to foodservice (the Branded Product Program).** Nathan's buys hot dogs, mostly from
     Smithfield, and resells them to distributors and operators (stadiums, cinemas, amusement parks, chains).
     **$105,768K of revenue, 65% of the total, at a segment gross margin of 6.1% (FY2026) and 10.2%
     (FY2025)**, with beef 80-90% of cost of sales and prices set by *"sales agreements with our Branded
     Product Program customers that are correlated to our cost of beef and beef trimmings"*; five customers
     are about 80% of the segment. Segment operating income $4,285K.
  3. **It runs four restaurants (Coney Island among them) and franchises 221 more plus 476 virtual
     kitchens**, taking 5.5% royalties on franchised sales. Restaurant segment operating income $2,617K. The
     system shrank from 230 to 221 in FY2026 (23 opened, 32 closed).
  - Corporate costs of $14,034K (including $3,210K of merger fees in FY2026) sit against the three.
- **The scarce input this business controls:** the **Nathan's Famous trademarks** (registered in the US and
  in over 80 jurisdictions) and the recipe and spice formulation (*"Through this agreement, we control the
  manufacture of all "Nathan's Famous" branded hot dogs"*, of the Solina spice licence). The plants, the
  retail customers, the retail price and the promotions belong to the licensee.
- **Will the fundamentals look broadly the same in ten years?** The mechanism does not change: a royalty on
  packaged sales, a margin on foodservice resale, a franchise royalty. **The contract does**: the Smithfield
  licence expires in March 2032, inside the ten years, and if the merger closes the licensee owns the
  licensor. Whether the brand keeps its rent at the next renewal is Q2's question, not a failure of
  understanding.
- **What I cannot see from Nathan's own filings**: the retail product's price, promotion and shelf, which
  are Smithfield's decisions. That is Q2's evidence problem and is stated there, not a reason to close Q1.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — relatively simple and stable in
  character and legible from the filings **[E3-31]**.

*Earlier 10-Ks read (EDGAR primary documents): FY2025 `0001437749-25-019916`, FY2024 `0001437749-24-020013`,
FY2023 `0001437749-23-016924`, FY2022 `0001437749-22-014727`, FY2021 `0001437749-21-014536`, FY2020
`0001437749-20-012966`, FY2019 `0001437749-19-012012`, FY2018 `0001437749-18-011457`, FY2017
`0001437749-17-011019`, FY2016 `0001437749-16-033631`, FY2015 `0001437749-15-012185`, FY2014
`0001437749-14-011106`, FY2013 `0001437749-13-007587`, FY2012 `0001437749-12-005931`, FY2011
`0001144204-11-034784`, FY2010 `0001144204-10-032962`.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The rule, quoted from the ledger row itself** (`principle_ledger.csv`, E3-03, 1991 letter), not from the
framework's rendering: *"An economic franchise arises from a product or service that: (1) is needed or
desired; (2) is thought by its customers to have no close substitute and; (3) is not subject to price
regulation. The existence of all three conditions will be demonstrated by a company's ability to regularly
price its product or service aggressively and thereby to earn high rates of return on capital. Moreover,
franchises can tolerate mis-management."* **The demonstration sentence is the test the filings can answer.**

**Where the profit is, so the test is asked of the right product.** FY2026 segment operating income:
Product Licensing $37,234K, Branded Product Program $4,285K, Restaurant Operations $2,617K (Note I). **84.4%
of the business's segment profit is one royalty on one licensee's sales of one product**, so the franchise
question is asked first of the Nathan's packaged hot dog as a consumer product, and then of the two legs
Nathan's actually prices itself.

- Needed or desired [x] · no close substitute [ ] **not shown; the filings show the opposite, below** · not
  price-regulated [x]
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]** No: a
  110-year-old trademark is not a basis that must be replaced each generation, and nothing here needs a
  superstar **[E4-23]**. **[E4-04] is not the ground of this verdict, and the perimeter close (UNKNOWABLE)
  does not apply**: the business does not pass [E3-03] first.

### THE PHYSICAL SERIES OF THE PRODUCT THAT CARRIES THE PROFIT [E4-55]
*Every figure is the registrant's own sentence in that year's MD&A (retail volume and average net selling
price of the Smithfield/John Morrell licensed hot dogs, on which the 10.8% royalty is calculated).*

| FY | retail volume | net selling price | the 10-K's stated cause |
|---|---|---|---|
| 2017 | +7.3% | **−4.0%** | *"due to competitor pricing pressures experienced early in the second quarter"* |
| 2018 | +9.3% | +4.5% | *"pricing increases during the fourth quarter"* |
| 2019 | +2.2% | −1.3% | |
| 2020 | +11.0% | +2.0% | |
| 2021 | +12% | +12% | *"As consumers sheltered at home as a result of the COVID-19 pandemic"* |
| 2022 | +0.3% | +1.1% | |
| 2023 | **−4%** | +7% | |
| 2024 | **−3%** | +3% | |
| 2025 | +11% | *"comparable"* | |
| 2026 | **−13%** | **+15%** | *"The price increases year over year led to a reduction in promotional activities contributing to the decline in volume."* |
| Q1 FY2027 | +3% | +7% | 10-Q, quarter ended 2026-06-28 |

**Compounded (my arithmetic on the filed percentages):** FY2016 to FY2026, volume **+34%** and price
**+45%**; **FY2022 to FY2026, volume −10% and price +27%**, while the Smithfield royalty went from $28,970K
to $33,589K (+16%). **This is [E4-55]'s shape exactly**: *"a precipitous drop in physical volume"* with a
price rise *"holding dollar volume roughly level"*. In the one year where price rose hardest, units fell
almost one for one (−13% against +15%), and the registrant names the mechanism as promotions withdrawn:
**the volume depended on the deal.** In FY2017 the price went the other way because a competitor made it.

**[E2-44] characteristic (1)** asks for *"an ability to increase prices rather easily (even when product
demand is flat and capacity is not fully utilized) without fear of significant loss of either market share
or unit volume"*. **It fails on the filed series** (FY2023, FY2024 and FY2026). Characteristic (2) passes
strongly for the licensor, which grows dollar royalties with no capital at all. **[E4-37]**: a business where
a 15% price rise costs 13% of the units is the prayer-session end of the scale, and the prayer is said by the
licensee, who sets the price and the promotions.

### THE REGISTRANT'S OWN WORDS ABOUT SUBSTITUTES, EVERY CHANNEL
- **Retail licensing**: *"Our retail licensing program for the sale of packaged foods within retail grocery
  channels including supermarkets and club stores competes primarily on the basis of reputation, flavor,
  quality and price. In most cases, we compete against other nationally recognized brands that may have
  significantly greater resources than those at our disposal."*
- **Branded Product Program (65% of revenue)**: *"Our Branded Product Program competes directly with a
  variety of other nationally recognized hot dog companies and other food companies ... Our products
  primarily compete based upon price, quality and value to the foodservice operator and consumer."* Its
  prices follow cost, not position: FY2019, *"Our average selling prices decreased by approximately 3.5% as a
  result of our pricing strategy, which is more closely correlated to the cost of beef"*; FY2026, *"entering
  into sales agreements with our Branded Product Program customers that are correlated to our cost of beef
  and beef trimmings"*. Segment gross margin **12.6% (FY2022), 14.2%, 12.2%, 10.2%, 6.1% (FY2026)** as beef
  rose (my arithmetic from the MD&A's revenue and cost-of-sales figures), and *"Sales to our five largest
  Branded Product Program customers were approximately 80%"*. That is **[E2-58]'s commodity equation with a
  logo on it**: cost passed through with a lag, the margin decided by the beef cycle.
- **Restaurants**: *"The quick-service restaurant business of the foodservice industry is intensely competitive"*; *"Continued price
  discounting and the emphasis on value meals may adversely impact the Company's business"*; franchise units
  230 to 221 in FY2026; Company-owned traffic −2%.
- **The general statement**: *"Our success and profitability depends on our customers willingness to pay
  higher prices for our products across all channels of distribution and there is no assurance that they
  will do so."* (Item 1A).

### WHO DECIDES HOW GOOD THE PRODUCT'S ECONOMICS ARE [E2-53, E4-65, E5-57]
**[E2-53]'s dominance class** is the strongest reading of franchise: *"Once dominant, the newspaper itself,
not the marketplace, determines just how good or how bad the paper will be."* **Here the marketplace and
the licensee decide.** Smithfield sets the retail price, the promotions and the shelf, and **Smithfield
sells its own rival hot-dog brands beside Nathan's**: its 10-K lists *"Smithfield, Eckrich, Farmland,
Armour, Farmer John, Kretschmar, John Morrell, Cook's, Gwaltney"* among its trademarks and names hot dogs in
its Packaged Meats line. The retail volume is sold *"substantially ... to Sam's Club and WalMart"* (FY2019-FY2021
MD&A), which is the buyer concentration **[E4-65]** names (*"the Walmarts and the Costcos and the Sam's"*),
and Costco's own label is the **[E5-57]** case. The licensor holds a percentage of a price it does not set,
of a volume it does not promote, through a shelf it does not own.

### THE COMPETITOR ROW — required [E3-28]
*Same metric where the filings allow it: operating margin on selling packaged or foodservice meat products,
latest three fiscal years. Segment figures from the peers' 10-K text; consolidated figures from XBRL
(transcription, flagged).*

| Company | same metric | window | source |
|---|---|---|---|
| **Nathan's, Branded Product Program** (the leg that sells product) | **4.1%** FY2026, **7.8%** FY2025 | FY2025-26 | 10-K Note I, `0001437749-26-019923` |
| **Nathan's, consolidated** (royalty-weighted) | 18.6% FY2026, 24.6% FY2025 | FY2025-26 | same |
| **Smithfield Foods, Packaged Meats** (the licensee; Eckrich, Armour, Farmer John and the Nathan's licence) | **12.5%** FY2025 ($1,094M on $8,757M), **14.0%** FY2024 ($1,168M on $8,319M) | FY2024-25 | 10-K `0000091388-26-000014`, segment tables |
| **Tyson Foods, Prepared Foods** (Ball Park, Hillshire Farm, State Fair) | **9.0%** FY2025 ($898M on $9,930M), 8.9% FY2024, 8.4% FY2023 | FY2023-25 | 10-K `0000100493-25-000095`, segment table |
| **Conagra Brands** (Hebrew National, unsegmented) | consolidated 11.8% FY2025, −14.4% FY2026 (XBRL, flagged; FY2026 carries charges not read) | FY2025-26 | 10-K `0001104659-26-083905`; text: *"net sales during fiscal 2025 were impacted by approximately $24 million due to temporary manufacturing disruptions in our Hebrew National [®] business during the key grilling season"* |
| **Kraft Heinz** (Oscar Mayer, unsegmented) | no brand margin; **Oscar Mayer impaired $1.3bn in Q4 2024**, *"due to additional perceived risk in achieving our long-term cash flow forecasts for the meats business"*; fair value 10-20% over carrying at the 2025 test | 2024-25 | 10-K `0001637459-26-000009` |

- **Peers named: 5 filers of the industry's roughly 9 real competitors** (Smithfield's own list: Tyson,
  Hormel, Kraft Heinz, Conagra, Boar's Head, Johnsonville; plus Sabrett/Marathon and retailer private
  labels). **Not obtained**: Boar's Head, Johnsonville and Sabrett (private, no SEC filings); Hormel (its
  10-K fetched but not reduced to a segment figure in this run); private label (no filing). **No filer
  segments a hot-dog brand**, so no brand-level share or margin exists in any filing for any competitor.
- **What the row shows, stated with its limit [E3-61]:** the one Nathan's leg that sells product earns
  **less than half** the operating margin of the packers who make it (4.1-7.8% against 8.4-14.0%), and the
  largest branded hot-dog owner in the row wrote its meat brand down by $1.3bn. **Relative position is not
  the ground of the verdict**; the ground is the registrant's own words and its own physical series, above.
  The row cannot show conduct.
- **Untapped pricing power [E3-33]:** no. The licensee raised price 15% in FY2026 and lost 13% of the units;
  the claim of the class is a claim of near-monopoly **[E5-28]**, which nothing filed supports.
- **The attacker's test [E2-45]:** a rival with capital and people competes by being one of the national
  brands already on the shelf, by being the retailer's own label, or by being the licensee itself.
- **Direction [E4-32]:** units down in three of the last four years, dollars held by price. Not widening.
- Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: **eroding in units, held in dollars**.

### THE STRONGEST EVIDENCE AGAINST THIS VERDICT, stated as its holders would state it [E4-51, E3-47, E4-26]
1. **The brand re-priced its own licence once, and hard.** Under SMG to March 2014 the royalty was
   *"between 3% and 5% of sales"* ($5,506K in FY2013); under John Morrell/Smithfield from March 2014 it is
   **10.8%**, and hot-dog royalties went from $6,742K (FY2014) to $16,105K (FY2015). The licensees competed
   for the name. That is aggressive pricing of the product Nathan's actually sells, the licence.
2. **The licensee is paying $102.00 a share for it**, about $418M for the equity plus the $47.8M term loan,
   while owning a shelf of its own hot-dog brands. Its own brands were not a substitute for this one.
3. **The ten-year units are up 34%** and the Smithfield royalty compounded about 6.9% a year from FY2015
   ($16,105K) to FY2026 ($33,589K), on no capital; returns on capital employed are extreme **[E3-46]**; the
   royalty carries *"minimum annual guaranteed royalties"* to 2032.
4. **Q1 FY2027 turned**: volume +3% with price +7%.

**Answered, not dismissed.** (1) is one negotiation in twelve years, won because a second packer wanted
the business; the next is in 2032 against a buyer set that owns the rival brands, and if the merger closes
there is none. (2) is what the licence is worth to the one party that would stop paying 10.8% of its own
sales: the elimination of a royalty is a synergy to that buyer, and a price paid is not pricing power. It
says nothing about what consumers think the substitutes are, which is what criterion (2) asks. (3) and (4)
are real: this is a durable, valuable trademark rent, and I record it as such. **But [E3-03] asks whether
the product is thought by its customers to have no close substitute, demonstrated by the ability to price
aggressively.** The consumer product's own series says customers substitute when price rises and when a
competitor cuts; the foodservice leg, which carries two thirds of revenue, prices at cost-plus and says so;
the restaurant leg is shrinking. **The evidence is here, and the business fails the franchise test.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — **OUT, on the business.** [E3-03]
  criterion (2) is refuted by the registrant's own words in all three channels and by its own filed physical
  series; the demonstration clause fails at the consumer (price rises lost units in FY2023, FY2024 and FY2026;
  a competitor forced a price cut in FY2017) and in the foodservice leg (6.1-14.2% gross margin on
  beef-correlated pricing). The licence is a valuable rent, but a percentage of a price set by a licensee who
  sells rival brands is not a franchise under the 1991 definition. **The file closes here. Q3-Q6 are not
  opened as gates.**

*"Can I name the document that would resolve this?"* Not asked: the verdict is OUT, not a non-IN pending
evidence. Recorded for completeness: brand-level scanner data (share and price by brand) would sharpen the
competitor row, and it is not an SEC filing and was not sought; the verdict does not rest on the row.

---
## MATERIAL BENEATH THE CLOSE — recorded, not governing

*The file closed at Q2, OUT on the business. What follows was gathered for the brief's priors and is
recorded the way the CAH, MHH and ICFI runs recorded theirs: no verdict box is ticked for Q3-Q6, nothing
here reopens Q2, and nothing here is a clearance.*

### Q3 prompts (no verdict)
- **Weight case, had the gate opened:** none of the three determinants is high on the licensing leg (a
  contract to 2032 with minimum royalties is have-to-be-smart-once) **[E3-38]**; **control** is the live
  one: directors and officers hold about 31.0% and Howard M. Lorber 24.2%, and a voting agreement on 29.9%
  carries the merger vote **[E1-16]**. An overlay, most likely, with the control point stated.
- **The brief's prior of an SEC settled action around 2019 over undisclosed executive perquisites: NOT
  FOUND.** Sweep: every 10-K FY2010-FY2026 (sixteen primary documents plus the FY2026 10-K and 10-K/A) grepped
  for *Division of Enforcement*, *cease-and-desist*, *administrative proceeding*, *subpoena*; EDGAR full-text
  search restricted to CIK 0000069733, 2017-01-01 to 2026-09-25, for `"cease-and-desist"` (9 hits, all proxies
  and the 10-K/A), `perquisites "Securities and Exchange Commission"` (12 hits, all proxy boilerplate),
  `"Division of Enforcement"` (0) and `"SEC order"` (0). **No instance found** of an order against Nathan's
  or its officers. **What the sweep did find**: director **Robert J. Eide**, 10-K/A: *"On March 28, 2018,
  Mr. Eide agreed to enter into an Order Instituting Administrative and Cease-And-Desist Proceedings, with
  the SEC whereby Mr. Eide, without admitting or denying the findings, consented to the entry of an order
  finding that he was a cause, solely in his capacity as CEO, of Aegis Capital Corp.'s violations of
  Sections 17(a) and Rule 17a-8 under the Securities Exchange Act of 1934."* A director's matter at another
  firm, public since 2018 and disclosed in Nathan's own filings (full-text hits in the DEF 14As of 2018 and
  2021-2024 and the 10-K/A); he sits on the audit committee. **Limit:**
  SEC administrative orders are not EDGAR filings, so the full-text search cannot see an order Nathan's
  never disclosed; the SEC's own litigation pages were not searched in this run. The prior may have
  conflated this order with Nathan's; the run does not know.
- **[E4-29] FIRES, and in the 10-K itself.** The FY2026 10-K's MD&A carries *"Reconciliation of GAAP and
  Non-GAAP Measures"* with EBITDA ($31,972K) and Adjusted EBITDA ($36,314K, adding back share-based
  compensation and the merger fees); the 10-Q repeats it; the FY2026 results release (8-K 2026-06-09) leads
  with *"Adjusted EBITDA 1 for fiscal 2026, a non-GAAP financial measure, was $36,314,000"* (the "1" is a footnote marker). Adjusted EBITDA adds
  back share-based compensation, which **[E5-06]** calls an expense.
- **Pay [E4-27]**: discretionary cash bonuses (Gatoff $1,000,000, Steinberg $200,000 for FY2026) judged
  against *"increasing each of revenues, profits from continuing operations, pre-tax cash flow, net income
  and earnings per share"*; not EBITDA-based. Lorber: $1,000,000 base, 50,000 RSUs (2022). Merger
  payments: Lorber $5,673,430 (double trigger, 2.99x), Gatoff $5,959,691 (including a $3,250,000 retention
  bonus), Steinberg $1,525,358; together about 3.2% of the equity consideration.
- **The diligence cut**: Smithfield's bankers cited *"an approximate $20 million gap in its valuation of the
  Company related to certain matters identified in Parent's due diligence findings"* and cut the offer from
  $103.50 to $101.00, *"approximately half of Parent's identified potential costs and exposures"*; the board
  negotiated $102.00. **What the matters are is not disclosed in the documents read**; a prompt, not a
  finding.
- **Capital allocation**: the 2015 and 2017 recapitalisations paid $137M of special dividends largely with
  10.000% and 6.625% secured notes (interest about $13.5M a year FY2016-FY2018 against owner earnings of
  $8.5-17.9M); buybacks of about $39M under the sixth plan, none since FY2024; **[E2-60]**'s third dimension
  (financial strength spent on the payout) and **[E2-52]**'s form, with borrowing where issuance stands in
  the passage, are the prompts.
- **Candor [E2-26]**: the royalty sentences in the MD&A give volume and price separately every year,
  including the bad years (FY2017's competitor pressure, FY2026's lost promotions). That is the half-owner
  standard met on the one line that matters.

### Q4 prompts: owner earnings the corpus's way [E2-23], every window [E4-25, E4-38]
*OCF − SBC − (c). OCF from the filed statements (cross-checked: FY2014 $2,876K, FY2016 $12,480K, FY2018
$18,862K, FY2019 $11,156K, FY2020 $12,349K, FY2026 $18,234K each quoted in the MD&A of its year; the XBRL
pull matches every one). **SBC RESOLVES AND IS COMPLETE**: the tag resolves in 17 of 17 years; the filed
line is "Share-based compensation expense" ($1,132K FY2026, $993K FY2025, $162K FY2019, $116K FY2020 in the
MD&A); bonuses are cash; no stock-settled bonus or 401(k) stock found; SBC is 0.4-6.6% of OCF except FY2014
(25.1%, a year of low OCF), so [E3-70]'s grant-value measure moves nothing material. (c) is a disclosed
guess [E2-09], shown as the band from the smaller to the larger of capex and D&A: capex ($0.2-4.3M) and
D&A ($0.9-1.4M) are both about 1% of revenue, the business owns four restaurants and no plant, and the
licensee carries the plants, so this is [E3-44]'s default class, not [E5-20]'s exception.*

| FY | OCF | SBC | capex | D&A | OE low | OE high |
|---|---|---|---|---|---|---|
| 2010 | 7.18 | 0.43 | 2.18 | 0.84 | 4.57 | 5.91 |
| 2011 | 7.23 | 0.38 | 1.25 | 0.92 | 5.60 | 5.93 |
| 2012 | 9.61 | 0.27 | 1.36 | 0.97 | 7.98 | 8.37 |
| 2013 | 9.49 | 0.63 | 1.00 | 0.94 | 7.87 | 7.93 |
| 2014 | 2.88 | 0.72 | 4.34 | 1.16 | −2.18 | 1.00 |
| 2015 | 13.29 | 0.86 | 1.54 | 1.25 | 10.89 | 11.17 |
| 2016 | 12.48 | 0.72 | 1.13 | 1.26 | 10.50 | 10.63 |
| 2017 | 10.41 | 0.58 | 1.13 | 1.30 | 8.53 | 8.70 |
| 2018 | 18.86 | 0.40 | 0.56 | 1.35 | 17.11 | 17.90 |
| 2019 | 11.16 | 0.16 | 0.45 | 1.21 | 9.78 | 10.55 |
| 2020 | 12.35 | 0.12 | 0.87 | 1.23 | 11.00 | 11.36 |
| 2021 | 11.77 | 0.12 | 0.55 | 1.18 | 10.47 | 11.10 |
| 2022 | 16.48 | 0.07 | 0.64 | 1.05 | 15.35 | 15.77 |
| 2023 | 19.84 | 0.26 | 0.63 | 1.14 | 18.44 | 18.95 |
| 2024 | 20.00 | 0.73 | 0.31 | 1.14 | 18.13 | 18.96 |
| 2025 | 25.24 | 0.99 | 0.23 | 0.96 | 23.29 | 24.02 |
| 2026 | 18.23 | 1.13 | 0.37 | 0.93 | 16.18 | 16.73 |

*$M. Script `oe.py`, output `oe_out.txt` in the research folder.*

| window | mean owner earnings | yield on $386.4M |
|---|---|---|
| 3y FY2024-26 | $19.2M to $19.9M | 4.97-5.15% |
| **5y FY2022-26 (the corpus default [E2-42])** | **$18.3M to $18.9M** | **4.73-4.89%** |
| 5y FY2017-21 | $11.4M to $11.9M | 2.94-3.09% |
| 10y FY2017-26 | $14.8M to $15.4M | 3.84-3.99% |
| 12y FY2015-26 (the 10.8% royalty era) | $14.1M to $14.7M | 3.66-3.79% |
| 17y FY2010-26 | $11.4M to $12.1M | 2.95-3.12% |

- **The screen's `spread_caveat` answered**: its $18-20M (3y/5y) reproduces; the longer windows run
  $11-15M. The bottom never sits near zero on any window of three years or more (one year, FY2014, is
  negative at the capex end: minus $2.2M, after the $6,009K SMG litigation payment). **The width is the
  level, not the band**: (c) moves each window by about $0.6M, the window choice by $8M.
- **Three distortions in the series, named [E4-41, E5-11]**: (1) **interest**: OCF is after interest on
  the recapitalisation debt, about $13.5M a year of coupon FY2016-FY2018, then interest expense of $10.8M (FY2019),
  $10.6M (FY2020, FY2021), $10.1M (FY2022), $7.7M, $5.4M, $4.1M and $2.9M (FY2023-FY2026) from each year's
  MD&A, so **about $4M of the $7M rise** from the 5y FY2017-21 mean to the 5y FY2022-26 mean is **debt paid
  down, not business grown** (my arithmetic: the two windows' interest differs by about $5.7M pre-tax); (2) **FY2018** adds back the $8,872K
  loss on extinguishment while the $6,750K call premium sits in financing; (3) **FY2021** is the pandemic
  (Branded Product Program sales $33.6M against $57.6M) and **FY2025** the best year ($25.2M OCF, retail
  volume +11%). `level_shift_full` 1.82 against 1.4 on the shorter series is the interest line and the
  2014 royalty step, read, not a finding.
- **Great, good or gruesome [E4-20]**: the licensing leg is the great account in form (dollars grow with
  no capital); the foodservice leg is not. Recorded, not scored.
- **Staying power [E5-11]**: (1) stream: $11-19M a year of owner earnings across windows; (2) liquid
  assets: cash $24.4M (March 2026); (3) near-term requirements: term loan $47.8M, $2.4M a year of
  amortisation and **$41.2M due in FY2030**, change of control an event of default (the buyer pays it at
  closing). **Coverage [E2-54]**: interest $2.9M against about $16-19M of owner earnings after capex,
  about six times. Covenants: fixed charge ratio and net leverage not above 3.00x, in compliance.
- **Named death, as a signature only: #19 THE SHELF, with #6 THE BORROWED BALANCE SHEET as a feature.**
  The brand is owned; the route to the buyer is rented from Smithfield, which sets the price and the
  promotions and sells Eckrich, Armour and Farmer John beside it, into Walmart, Sam's Club and Costco
  **[E4-65, E5-57]**; the 2015 recapitalisation borrowed against the royalty to pay the dividend.
  **Not entered in the index's instances column** (file closed at Q2, the PAGP, CALM, ICFI, MHH and CAH
  precedent). **No new shape.**

### COMPUTATION — NOT A CLEARANCE
*No box, no ranking, no entry language.* At the ~10% floor **[E4-28]** with no growth, the 5y owner
earnings of $18.3-18.9M capitalise to $183-189M; less net debt of about $23.4M ($47.8M term loan, $24.4M
cash) that is **$160-166M, about $39-40 a share**; on the 3y mean about $41-43; on the 10y mean about
$30-32. At the 5.47% sovereign with no growth the 5y mean is worth about $76-79 a share. **Against $94.29
quoted and $102.00 in the merger.** The five-year yield of 4.7-4.9% is below the bond and below the floor.
**The deal price is about 22 times the five-year owner earnings for the equity**, a price only the party
that stops paying the royalty can make work. **Windage count: ONE** (the conservative end of the (c) band,
and nowhere else; no premium in the rate **[E3-42]**). **The quote itself is a merger spread (92.4% of
$102.00) and says nothing about this arithmetic [E2-74].**

### Q6 — reversal conditions, in words (no alert: the file failed on the business, the QLYS ruling)
The Q2 verdict would reopen on **filed evidence that the product holds its units through price**: several
years in which the licensed retail volume rises, or holds, while net selling price rises faster than beef
costs (the reverse of FY2023, FY2024 and FY2026); **or** a licence renewal in 2032 (or an extension) at a
royalty rate at or above 10.8% won against a competing bidder; **or** the Branded Product Program's gross
margin holding above its FY2022-FY2024 12-14% through a beef-cost spike. **If the merger closes on or after
2026-10-23, the security ceases to exist and the question ends there** (the LEG precedent).

---
⛔ **Q5 does not open: Q2 is OUT.** The computation above is headed as the protocol requires and carries
no box.

## Q5 — not opened. ## Q6 — not opened as a gate (reversal conditions in words above).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; the file closed at Q2)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the filing)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued; the [E4-04] perimeter
      close was considered and refused because [E3-03] is not passed first)
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026 OCF $18,234K,
      rebuilt from its lines, ties to the MD&A's two subtotals)
- [x] Owner earnings on a multi-year mean; every window from 3 to 17 years published; capex band disclosed
      as a judgment (beneath the close)
- [x] Competitor row filled (5 filers of about 9 named; private brands and brand-level data unavailable,
      stated; the verdict does not rest on the row)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (5.47%, Treasury, 09/24/2026)
- [x] Value stated as a round-number range, not a point estimate (computation only)
- [x] One bar chosen, not both; windage count stated (ONE; no bar applied, Q5 not opened)
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git (claim `a39fa24`, Step 0 and Q1 `29c61e0`, Q2 `19fdcdf`, this section and the fold
      after)

**Brief priors, each tested:**
1. *Fiscal year ends late March* — confirmed (FY2026 ended 2026-03-29; 10-Q to 2026-06-28).
2. *A licence with a meat processor, the Branded Product Program, franchising, a few company restaurants* —
   **confirmed**, with the shares: licensing 84.4% of segment operating income; Smithfield, 10.8% of net
   sales, minimum guaranteed royalties, **expiry March 2032**, optional extension to 2036 only as a condition
   of the Parent termination fee; no renewal right stated in the documents read.
3. *`deal_note` blank; check anyway* — **REFUTED as a description of the security: a live cash merger at
   $102.00 by Smithfield, the licensee**, signed 2026-01-20. The quote is a spread.
4. *An SEC settled action around 2019 over undisclosed perquisites* — **not found** (sweep stated at Q3
   prompts); the one SEC order in the record is director Eide's of 2018 at Aegis Capital.
5. *Verify SBC resolves and is complete* — **resolves 17 of 17 years and is complete** as far as the filings
   show (no stock-settled bonus found).
6. *Debt: amount, maturity, covenants, what it funded* — $47.8M unsecured term loan to 2029, 3.00x net
   leverage covenant; it refinanced notes that funded the 2015 and 2018 special dividends.
7. *Rebuild the width over every window* — done; $11.4M (17y, 5y FY2017-21) to $19.9M (3y); the bottom never
   near zero on any multi-year window.

**Brief errors found:** (1) the brief's "deal_note is blank ... still check" was right to ask, and the blank
itself was wrong (tooling, below); (2) the brief's commit trailer (Opus 5) differs from the session's
attribution instruction (Opus 5.5); the brief's trailer was used, as the CAH run recorded; (3) none
verdict-bearing.

**My own errors caught before commit:** (1) a first Treasury fetch used a wrong URL path
(`resources/` for `resource-center/`) and returned 404; the correct source was then fetched and the saved CSV
checked for the header row and 09/24/2026 before use; (2) a bash heredoc with apostrophes failed, as the brief
warned; sections were written as files instead; (3) I first quoted a restaurant sentence without *"of the
foodservice industry"* and a Conagra sentence without its ® mark, corrected against the source before commit;
(4) I first quoted the release's *"EBITDA 1 ..."* when the line reads *"Adjusted EBITDA 1 ..."*, corrected;
(5) I first wrote that interest ran at $9.9M through FY2023; the MD&As say $10.1-10.8M to FY2022 and $7.7M in
FY2023, corrected; (6) I first wrote that Nathan's disclosed the Eide order "in every proxy since", which the
full-text hits do not show for 2019-2020; narrowed to what was found.

**Tooling defects, reported, not patched:**
1. **`deal_note()` / `deal_filings()` in `tools/sources.py` cannot see a deal signed before the latest annual
   report.** It counts deal forms only after the newest 10-K (*"since"*). Nathan's merger 8-K (2026-01-21,
   with EX-2.1) and PREM14A (2026-03-06) predate the FY2026 10-K (2026-06-09), and the DEFM14A did not exist
   until 2026-09-24, so on the screen date of 2026-09-02 the column was blank for a company under a signed
   cash merger for seven months. Today the same call returns the DEFM14A line. **A pending deal is invisible
   in the window between the next 10-K and the definitive proxy.**
2. **`run.py`'s "GROWTH THE PRICE ASSUMES" printed −9.1%** while the screen's `growth_required` reads +5.46% for
   the same name: `implied_growth()` fades to a fixed 2.5% terminal rate (`tgr=0.025`), so any price below
   about 34 times owner earnings at a 5.47% rate returns a negative "required" growth. Two tools, two
   definitions, opposite signs; a prompt to read, not a number to carry.
3. `tools/sources.annual()` returned Hormel's operating income only through FY2017 (tag change, not
   investigated), so Hormel is not in the row.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **Nathan's owns a trademark rent, not a franchise: 84% of its profit is 10.8% of a price that
  Smithfield sets, promotes and shelves beside its own rival brands, and the product loses units when that
  price rises (FY2022-FY2026 retail volume −10% against price +27%; FY2026 −13% against +15%), while the
  foodservice leg earns 6-14% gross margin on beef-correlated prices. The licensee is buying the licensor
  at $102.00 cash; the $94.29 quote is a merger spread.**
- **PASS/FAIL: FAIL at Q2 (OUT, ON THE BUSINESS).** Price **$94.29** (2026-09-24 close, aggregator,
  flagged) × **4,097,661 shares** (10-Q cover, accession `0001437749-26-026427`) = cap **$386.4M**;
  sovereign **5.47%** (US Treasury, 09/24/2026). Owner earnings $11.4-19.9M across every window and both
  (c) ends (5y $18.3-18.9M, yield 4.7-4.9%). **Pending cash merger with Smithfield Foods at $102.00 (CFIUS
  cleared 2026-09-17, vote 2026-10-23); the quote is 92.4% of the consideration.**
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.
