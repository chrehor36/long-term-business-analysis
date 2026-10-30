# Company Run — Amazon.com, Inc. (AMZN) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*WAVE 5 of the watchlist queue, row "capex unresolved [E5-20]: build (c) by hand from the filing". Research,
scripts and extracted filing text: `Test Runs/_research 2026-09-13 AMZN/`. Run under the write-early protocol;
each section was appended as it closed. Prior art read for what it found, binding nothing:
`Test Runs/2026-07-15 Run - SPOT GOOGL MSFT SHW AMZN (5-pack).md` (v3.0; it passed Amazon's moat as "WIDE,
WIDENING" and built owner earnings on a net-income proxy, which v4.1 forbids), and the Amazon/AWS peer section
of `Test Runs/_research 2026-09-06 MSFT/competitor_row.md` (the useful-life history and the 2021-2025 cash-flow
inputs, every figure of which this run re-read against the filed statements).*

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
- rate **5.35%** · date **2026-09-11** · source (issuing authority) **US Treasury daily par yield curve, 30-year**,
  struck fresh by `python tools/sources.py` on 2026-09-13 (a Sunday; 09-11 is the latest business day).
- FX: none. Amazon reports in USD and the quote is USD. International segment sales (21% of Q2 2026) are
  translated; that is an earnings mix, not a quote-currency mismatch.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines and the supplemental cash-flow table  [x] footnotes
  (property and equipment, leases, commitments, debt, stockholders' equity, segment information, non-marketable
  investments, income taxes, legal proceedings)
- documents · date · accession no.:
  - **10-Q for the quarter ended 2026-06-30**, filed 2026-07-31, `0001018724-26-000026` (primary for the balance
    sheet, the trailing-twelve-month cash flows, commitments, leases, debt, investments, segments)
  - **10-Q for the quarter ended 2026-03-31**, filed 2026-04-30, `0001018724-26-000014`
  - **10-K for FY2025**, filed 2026-02-06, `0001018724-26-000004`; and the 10-Ks for FY2024 `0001018724-25-000004`,
    FY2023 `0001018724-24-000008`, FY2022 `0001018724-23-000004`, FY2021 `0001018724-22-000005`, FY2020
    `0001018724-21-000004`, FY2019 `0001018724-20-000004`, FY2018 `0001018724-19-000004`, FY2017
    `0001018724-18-000005` (every cash-flow statement 2015-2025 and every supplemental table read off these)
  - **DEF 14A**, filed 2026-04-09, `0001104659-26-041026`
  - **Deal and financing forms**: 8-K/425 of 2026-04-14 (`0001104659-26-042880`, `0001104659-26-042891`); S-4
    2026-07-31 (`0001104659-26-089294`); S-4/A 2026-08-14 (`0001104659-26-096195`); the final information
    statement/prospectus **424B3 of 2026-08-18** (`0001104659-26-098339`, read in place of the S-4/A it
    finalises); 8-K Item 1.01 of 2026-02-27 (`0001104659-26-021050`, OpenAI equity commitment); 8-K Item 1.01
    of 2026-06-10 (`0001104659-26-072140`, $17.5bn delayed-draw term loan); 8-K Item 5.02 of 2026-09-09
    (`0001018724-26-000036`); 424B5 of 2026-09-11 (`0001104659-26-107122`)
- **figure cross-checked against the filed statement:** FY2025 net cash provided by operating activities
  **$139,514M** — `tools/run.py` (XBRL) reads 139,514; the consolidated statement of cash flows in the FY2025
  10-K reads *"Net cash provided by (used in) operating activities | 84,946 | 115,877 | 139,514"*. **Match.**
  Also: the tool's 3-year capex-only owner-earnings mean ($2,430M) and 5-year mean (−$11,342M) reproduce to
  the dollar from the hand table below, so the triage row is arithmetic, not a transcription error.
- **Share count:** **10,786,313,572** shares of common stock *"outstanding as of July 22, 2026"* — 10-Q cover,
  `0001018724-26-000026`, single class. Confirmed against the balance sheet (10,783 million outstanding at
  2026-06-30). No split after the measurement date (the last was 20-for-1 in 2022), so no split factor applies.
- **Price:** **US$256.78, close of 2026-09-11** — aggregator (the `tools/run.py` chart feed), **flagged: live
  quote only.**
- **Market cap:** 256.78 × 10,786,313,572 = **US$2,769.7bn.**

### THE LIVE DEAL — read before pricing anything (the `deal_note` fired)
**Who buys whom: AMAZON IS THE ACQUIRER.** Verbatim, 8-K of 2026-04-14: *"Amazon.com, Inc. (the "Company") and
Globalstar, Inc., a Delaware corporation ("Globalstar"), issued a joint press release announcing they have entered
into a definitive merger agreement for the Company to acquire Globalstar."* The 425, S-4, S-4/A and 424B3 are
all the registration of the Amazon shares to be issued to Globalstar holders. **Nothing on file makes Amazon a
target, so the quote is NOT a spread; it prices Amazon as it is.**

- **Consideration: cash OR stock at each holder's election, cash capped at 40% of Globalstar shares.** Verbatim,
  10-Q Note 4: *"either (i) $90.00 in cash or (ii) 0.3210 shares of Amazon common stock (with a value capped at
  $90.00 per share) … a proration mechanism that caps aggregate cash elections to a maximum of 40% of total
  Globalstar shares … and (ii) a downward adjustment of a maximum of $110 million in the event Globalstar does
  not meet certain operational milestones"* (424B3: the milestone payment is owed to Apple, *"approximately $97
  million"* at 2026-08-18). Below an Amazon measurement price of $280.38 the ratio is fixed at 0.3210; above it
  the ratio floats to deliver $90.
- **Size: small.** *"the acquisition implied a value for Globalstar of approximately $10.9 billion, including its
  debt"* (10-Q). Against Amazon's US$2,769.7bn cap: **about 0.4%.** Amazon also agreed with Apple, Globalstar's
  largest customer, *"to provide certain services after the acquisition and to redeem certain equity interests
  held by Apple in a Globalstar special purpose entity"* (amount not stated in the 10-Q).
- **Pro forma dilution, my arithmetic on the 128,598,125 Globalstar shares outstanding at signing (424B3), at
  today's US$256.78 (below $280.38, so the 0.3210 ratio applies), warrants excluded because the count was not
  extracted:** all-stock elections → 41.3M Amazon shares, **0.38%** of the cover count; the 40% cash maximum →
  24.8M shares (**0.23%**) plus about **US$4.6bn cash**. Either way the per-share effect on this run's arithmetic is
  under half a percent, and **the file prices the company as it is, pre-close.**
- **What is being bought:** a low-earth-orbit mobile-satellite operator whose largest customer is Apple, its
  planned C-3 constellation, and terrestrial spectrum (Globalstar's adviser valued the operating business at
  $1.4-2.0bn and put the rest of the value in spectrum; 424B3, Evercore sum-of-the-parts). It sits beside
  Amazon's own satellite broadband programme, whose costs Amazon *"currently expense[s]"* (10-Q MD&A).
- **Status:** Globalstar's majority holders (Thermo, 57.6% of the vote) consented in writing on 2026-04-13, so no
  vote remains. The HSR waiting period *"expired on July 17, 2026"* (after Amazon withdrew and refiled). **Still
  outstanding:** FCC, French ANFR, ARCEP and two French ministries, other foreign-investment reviews, and
  *"certain governmental authorizations relating to the C-3 system [that] have not yet been received."* Expected
  close: **"in 2027"**. Outside date 2027-04-13, extendable twice to 2028-04-13. Reverse termination fee payable
  by Amazon: $592,071,000.
- **The OpenAI equity commitment of 2026-02-27 is NOT a merger, but it is the larger event.** Item 1.01: an
  equity commitment letter to buy **$35.0bn** of OpenAI Series C preferred, *"separate from and in addition to"*
  a **$15.0bn** Series C purchase; 10-Q: $28.7bn invested by 2026-06-30 and *"Subsequent to June 30, 2026, we
  invested the remaining $21.3 billion"*. **US$50.0bn of cash to one private company in five months** — carried
  to Q3 (capital allocation) and Q4 (liquidity), and the reason the equity-investment section below exists.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Segment profit and the capital under it — trailing twelve months to 2026-06-30, built as FY2025 − H1 2025 +
H1 2026 from the FY2025 10-K and the Q2 2026 10-Q.** $M.

| segment | net sales | operating income | margin | share of OI | P&E, net 2026-06-30 | segment assets 2026-06-30 | OI ÷ avg segment assets (Dec-25, Jun-26) |
|---|---|---|---|---|---|---|---|
| North America | 453,670 | 33,651 | 7.4% | 36% | 135,013 | 249,006 | 13.9% |
| International | 173,606 | 5,380 | 3.1% | 6% | 32,879 | 85,271 | 6.4% |
| **AWS** | **148,404** | **54,681** | **36.8%** | **58%** | **263,750** | **350,170** | **18.1%** |
| consolidated | 775,680 | 93,712 | 12.1% | | 446,046 | 1,095,689 (incl. corporate 411,242) | |

**Revenue lines, TTM to 2026-06-30** (same construction, "Net sales by groups of similar products and services"):
online stores 285,081 · physical stores 23,012 · **third-party seller services 183,660** · **advertising services
76,072** · subscription services 52,853 · AWS 148,404 · other 6,598.

**AWS, the same two ratios through the build** (FY segment notes; segment assets 2022 88,491 · 2023 108,533 · 2024
155,953 · 2025 252,588):

| | 2023 | 2024 | 2025 | TTM 2Q26 |
|---|---|---|---|---|
| AWS operating income ÷ average segment assets | 25.0% | 30.1% | 22.3% | 18.1% |
| AWS net sales ÷ average P&E, net | — | 1.17x | 0.86x | 0.65x |
| AWS P&E, net, period end | 72,701 | 110,683 | 190,055 | 263,750 |

- **Unit economics in my own words, no management language:**
  1. **Retail.** Amazon buys goods and resells them at a thin margin, and it rents its storefront, warehouses and
     delivery vans to other merchants for a commission plus a per-unit handling fee. It then sells those same
     merchants and brands paid placement in front of shoppers who arrived intending to buy, and it charges shoppers
     an annual Prime fee for fast delivery and video. **The two retail segments together earned $39.0bn of operating
     income on $627bn of sales in the last twelve months, while advertising alone brought in $76.1bn of revenue.**
     Amazon files no advertising margin, so that is an arithmetic juxtaposition, not a finding that advertising is
     the whole profit; but it says where to look: the thin-margin shop is the traffic, and the fees and ads sold on
     that traffic are the earnings.
  2. **AWS.** Amazon builds data centres, fills them with servers, networking and increasingly its own and bought
     AI chips, and rents the capacity by usage and by multi-year commitment. It earned a 36.8% segment margin on
     $148bn of TTM sales. **It is a capital business**: $263.8bn of AWS net plant at mid-2026, up 3.6x in thirty
     months, and every dollar of TTM sales now stands on $1.53 of average net plant, against $1.17 in FY2025 and $0.85 in FY2024.
  3. **Where the profit comes from, and on what capital:** 58% of operating income comes from the 19% of sales
     that is AWS, on 59% of the net plant. North America earns 36% of the profit on 58% of the sales. International
     earns 6% of the profit, on thin margins that were negative as recently as 2023.
- **The scarce input this business controls:**
  - *Retail:* the largest stream of shopping-intent traffic on the Western internet, joined to a delivery network
    dense enough that sellers pay to use it (third-party seller services $183.7bn TTM). Traffic and density
    reinforce each other; neither can be bought quickly.
  - *AWS:* the installed base of customer workloads (switching them is costly and slow), plus power-connected
    data-centre capacity and in-house chips, the last two of which are now contested by every hyperscaler at once.
- **Will the fundamentals look broadly the same in ten years?**
  - *Marketplace, advertising, Prime:* broadly yes. The mechanism is thirty years old and the filings describe
    it the same way in 2017 and 2026.
  - *AWS:* renting compute will still exist; **what gets rented, on what hardware, at what price, and against
    whom, is changing now**, and the 10-K itself shortened server lives in 2025 for *"the increased pace of
    technology development, particularly in the area of artificial intelligence and machine learning."* [E3-31]
    asks for businesses "relatively simple and stable in character". The mechanism is understandable; its
    stability is a Q2 question under **[E4-04]** (rapid change is the excluded class), and is carried there,
    not assumed away here.
  - *Outside the three segments:* a satellite broadband network (costs expensed), autonomous ride-hailing,
    healthcare, the Globalstar purchase, and **roughly $240bn of carrying value in two private AI laboratories**
    (below). These are understood as what they are: option bets, marked to observed funding prices.

### EQUITY INVESTMENTS — carried separately and kept OUT of owner earnings
All from 10-Q Note 2, `0001018724-26-000026`. **No market value exists for any of the large holdings; the carrying
values are Level 3 marks to *"observable changes in price related to Anthropic's fundings"*.**

| holding | carrying value 2025-12-31 | carrying value 2026-06-30 | what Amazon paid in cash | how marks reach the income statement |
|---|---|---|---|---|
| Anthropic nonvoting preferred | 14.8bn | **92.5bn** | notes converted, plus $5.0bn Series G and $5.0bn Series H in Q2 2026 | upward adjustments in "Other income (expense), net": **$50.5bn Q2 2026, $62.8bn H1 2026** |
| Anthropic convertible notes (available-for-sale) | 45.8bn fair value | **97.9bn** fair value | $8.0bn invested Q3 2023-Q4 2025 | unrealized gain in AOCI ($92.0bn at 2026-06-30); reclassified to income on conversion ($4.5bn H1 2026) |
| OpenAI Series C preferred | — | **28.7bn** (+$21.3bn funded after quarter-end) | **$50.0bn** in 2026 | future observable price changes, through "Other income (expense), net" |
| equity warrants | 2.7bn | 4.3bn | — | fair value through income |
| marketable equity securities (Level 1 + 2) | 3.7bn | 4.7bn | — | fair value through income; issuers not named in the 10-Q |
| equity-method investments | 0.66bn | 0.40bn | — | equity-method line |

- **Commitments still open:** an Anthropic financing facility of up to $20.0bn, *"reduced … to $15.0 billion"* after
  the Series H draw, made available *"as we reach certain delivery milestones of compute capacity."*
- **Why they are kept out of owner earnings:** the marks are non-cash and are removed from operating cash flow by
  the filing itself (TTM "non-operating expense (income), net" −$79,818M; the deferred tax on them is added back).
  **The TTM net income of $135,281M contains $80,425M of pre-tax "Other income (expense), net" (FY2025 15,229 − H1 2025 3,866 + H1 2026 69,062), almost all of it Anthropic marks and reclassifications**, which is exactly why the
  framework refuses a net-income proxy (operator rule 5). Owner earnings below start from operating cash flow.
- **No look-through earnings are added [E3-04]:** neither laboratory files statements, neither is equity-method,
  and the corpus's look-through adds *undistributed earnings*, of which none are evidenced. **Stated as an absence
  in the filing, not a zero.**
- **The same two companies are AWS's largest disclosed commitments**, which is why this table is carried to Q2 and
  Q4 and not left as a balance-sheet footnote: *"AWS and OpenAI … announced an expansion of the existing $38.0
  billion multi-year commitment … by $100.0 billion over 8.0 years"*; *"AWS and Anthropic announced an expansion …
  by more than $100.0 billion over 10.0 years"* (10-Q Note 1).

- **VERDICT: [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  The mechanism of every leg is legible from the filings and statable without management's words. **What is not
  simple and stable is the AWS leg's hardware basis**, and the framework locates that test at Q2 [E4-04], so it
  is carried, not used to fail Q1 and not used to excuse Q2. No "unverified" or "provisional" caveat attaches:
  the advertising margin is undisclosed, and understanding how the business makes money does not require it.

---
*Q2 onward follows as each section closes.*

*Resume note, 2026-09-13 ~14:40, added beneath the line above rather than replacing it (operator rule 6): the session that wrote Step 0 and
Q1 was killed by a session limit while building the Q2 competitor row. This run resumed from the files on disk. **The sovereign was re-struck
at the resume** (`python tools/sources.py`: *"USD 5.35% 09/11/2026 US Treasury daily par yield curve"*), unchanged, so Step 0 stands.
Everything below Q1 was written by the resuming session.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no close
> substitute and; (3) is not subject to price regulation. The existence of all three conditions will be demonstrated by a company's ability to
> regularly price its product or service aggressively and thereby to earn high rates of return on capital."* — **[E3-03]**, **[E3-43]**, 1991

### How a business with three legs is judged, from the text
**What THE FRAMEWORK v4 says:** [E3-03] defines a franchise as *"a product or service"*, so the test runs per product. The one rule in the
document about segments is at Q3, and it is a warning about blending: the consolidated series can *"camouflage repeated failures in capital
allocation elsewhere"* — *"judge retention segment-by-segment, incrementally, never on the blended return"* **[E2-56]**. The metric set is
chosen *"by business type first"* **[E5-37]**. **No instance found** in the framework of a rule for combining leg verdicts into one Q2 verdict
(searched "segment", "leg", "conglomerate", "divisions": one hit, the [E2-56] line).
**What this queue has done, recorded as practice and not as framework:** the verdict must hold for **what the shareholder actually buys**
(GHC, 2026-09-02); where legs split, it is decided by **where the profit and the capital actually are** (HAS, 2026-09-03: IN because the profit
was *"overwhelmingly"* the franchise leg and the rest *"neither grows nor eats material capital"*; SONY, 2026-09-13: OUT with two NARROW legs
carrying ~55% of profit). MSFT and GOOGL (2026-09-06) passed Q2 on the franchise leg that carried the weight, with their cloud legs recorded as
narrowing. **That practice is followed here, and each leg is tested on its own first, so the weighting cannot hide a leg's verdict.**

**Where the weight is (filed segment note; TTM to 2026-06-30):**
| | net sales | operating income | share of OI | net additions to P&E | share of additions |
|---|---|---|---|---|---|
| North America + International (stores, marketplace, advertising, Prime) | 627,276 | 39,031 | **42%** | FY2025 43,536 · H1 2026 27,532 | FY2025 30.6% · **H1 2026 23.2%** |
| **AWS** | 148,404 | 54,681 | **58%** | FY2025 96,496 · H1 2026 90,120 | FY2025 67.8% · **H1 2026 76.0%** |
AWS's share of consolidated net additions: **51.4% (2023) → 62.1% (2024) → 67.8% (2025) → 76.0% (H1 2026)**. Corporate additions omitted from the
shares above (2,320 in 2025; 996 in H1 2026).

---
### LEG 1 — AWS (58% of operating income; three-quarters of the new capital)

**Criterion (1) — needed or desired: [x] YES.** $148.4bn TTM sales, +32.7% in H1 2026.

**Criterion (2) — thought by its customers to have no close substitute: [ ] NO, on the filed record.**
- **Three rivals of scale sell the same service, and each grows faster or earns more** (Table A, `peers/competitor_row.md`, every figure with its
  accession): FY growth AWS **+19.7%** · Microsoft Intelligent Cloud +29.7% · Google Cloud +35.8% · Oracle cloud infrastructure +76.9%. Segment margin
  AWS **35.4%** · Intelligent Cloud **41.3%** · Google Cloud 23.7%. **AWS is second of three on margin and last of four on growth.** H1 2026 closed the
  growth gap (AWS +32.7%, IC +30.7%, Google Cloud +73.1% including a new hardware line).
- **Backlog is no longer AWS's lead either:** AWS *"approximately $496 billion"* (2026-06-30) · Microsoft commercial RPO $678bn (2026-06-30) · Oracle
  $664bn (2026-08-31) · Google Cloud $513.9bn (2026-06-30).
- **The largest customers buy from more than one of them, and the rivals' filings say so.** Microsoft 10-K FY2026: *"we recorded revenue from commercial
  arrangements with OpenAI, inclusive of revenue-sharing payments, of $24.1 billion"* — the same OpenAI that expanded its AWS commitment *"by $100.0
  billion over 8.0 years"*. Oracle 10-K FY2026: *"we offer our customers multicloud services whereby our customers can combine cloud services from multiple
  clouds with the goal of optimizing cost, functionality and performance. OCI's multicloud services work with a number of our competitors' products,
  including Microsoft Azure, Amazon Web Services and Google Cloud."* Microsoft: *"higher purchases of licenses running in multi-cloud environments"*.
  Meta carries *"$349.31 billion of non-cancelable contractual commitments ... most of which are related to third-party cloud capacity arrangements"*
  (10-Q Q2 2026) and appears in Amazon's own Q1 2026 release among *"new AWS agreements"*. **Amazon's filings contain no multi-cloud, switching or
  migration sentence at all** (0 hits, 10-K FY2025 and 10-Q Q2 2026); the only customer-change language is the competitive factor *"customers' ability and
  willingness to change business practices."*

**Criterion (3) — not subject to price regulation: [x] YES**, with open investigations into *"certain aspects of AWS's offering of cloud services"*
(10-K FY2025, Item 1A) recorded.

**The pricing test [E3-03]'s own sentence names — and [E2-44](1), [E4-37]. THIS IS THE DECISIVE EVIDENCE, AND IT IS AMAZON'S OWN.**
Every annual report read (FY2015, and FY2017 to FY2025, which between them cover every year from 2013) and both 10-Qs read explain AWS's sales with the same sentence:
- FY2015 10-K: *"The sales growth primarily reflects increased customer usage, partially offset by pricing changes. Pricing changes were driven largely by
  our continued efforts to reduce prices for our customers."* and *"The decrease in AWS segment operating income in absolute dollars in 2014 ... is
  primarily due to pricing changes"*.
- FY2017, FY2018, FY2019, FY2020 and FY2021 10-Ks: the same two sentences, verbatim.
- FY2022, FY2023, FY2024, FY2025 10-Ks, 10-Q Q3 2025 and **10-Q Q2 2026** (`0001018724-26-000026`): *"The sales growth primarily reflects increased
  customer usage, partially offset by pricing changes primarily driven by long-term customer contracts."*
**Thirteen consecutive years, 2013 to H1 2026, in which the filer says price moved against AWS revenue; no year found in which it says price added to it.**
The mechanism changed from list-price cuts to discounts for multi-year commitments; the direction did not. **[E2-44](1) asks for *"an ability to increase
prices rather easily ... without fear of significant loss of either market share or unit volume"*; the filed record is the opposite behaviour, sustained.**
The releases' price claims are price cuts under another name: Graviton *"up to 40% more price-performant than leading x86 processors"*; Kiro *"up to 50%
more cost-effective than alternatives"*.

**[E3-43]/[E3-46] — high returns on capital, and their direction [E4-32]:** AWS operating income ÷ average segment assets **25.0% (2023) → 30.1% (2024) →
22.3% (2025) → 18.1% (TTM)**; net sales ÷ average P&E 1.17× → 0.86× → **0.65×**. High, and falling fast as the plant quadruples.

**[E4-04] — must the moat be continuously rebuilt? YES, on the filer's own words.** The test the framework sets: *"does the spending defend the same
advantage, or buy its replacement?"* AWS's plant is **servers on five-year lives**, shortened in 2025 *"due to the increased pace of technology development,
particularly in the area of artificial intelligence and machine learning"*; AWS net P&E **$72.7bn → $263.8bn in thirty months**; the new spending buys a
new class of hardware (Trainium, *"our chips business"*) for a new class of workload. That is the replacement case, and [E4-04] names the class:
*"industries prone to rapid and continuous change."* **[E3-51]:** the long AWS run is a **surfing run** on the cloud wave and now the AI wave, and **[E4-36]**
places it in the fourth cause (wave-riding), the one the framework says is not ownable.

**[E2-58] — is there a wide and sustainable cost advantage?** Claimed in releases (Graviton, Trainium); **not evidenced as wide** in any filing: Google
*"began recognizing revenue from the sale of TPU systems"* (10-Q Q2 2026) — a rival selling its own custom accelerators to others — and every rival spent
3.4-9.0× depreciation in its latest period (Table A). **[E2-27]:** *"viewed collectively, the decisions neutralized each other"* is the row's picture.

**The backlog is not pricing power, and part of it is bought.** At least $200bn of the $252bn backlog increase in six months is from OpenAI and Anthropic,
the two companies into which Amazon put $50.0bn (OpenAI, 2026, $21.3bn of it after June 30) and $10.0bn (Anthropic Series G and H, Q2 2026) of equity (Q1 table). A commitment financed partly by the vendor's own capital is
evidence of volume, not of the customer's view that no substitute exists — and the larger of the two also buys from Microsoft.

**Leg verdict: AWS is a strong position in a contested, rapidly changing category — the "business" of [E3-43], not a franchise.** Class NARROW, direction
**narrowing**.

---
### LEG 2 — North America and International: stores, marketplace, Prime (with advertising tested separately below)

**Criterion (1): [x] YES.** $627.3bn TTM sales; worldwide paid units **+8% to +17%** a year-on-year by quarter, Q1 2025 to Q2 2026 (EX-99.1
releases), accelerating — **the physical series [E4-55] is healthy.**

**Criterion (2) for shoppers: [ ] NO, on Amazon's own description of what it competes on.** 10-K FY2025, Item 1: *"We believe that the principal
competitive factors in our retail businesses include selection, price, and convenience, including fast and reliable fulfillment"*; every 10-K read, FY2015
to FY2025: *"To decrease our variable costs on a per unit basis and enable us to lower prices for customers, we seek to increase our direct sourcing"*; the
Q4 2025 release's guidance carries *"even sharper prices in our international stores business."* A business whose stated weapon is the lower price is
**[E4-36]'s first cause (extreme minimization of one variable, the Costco class)** — admirable, and the opposite of pricing aggressively. **The attacker's
test [E2-45] is being run on it now:** Walmart's eCommerce net sales **~$150.4bn, +24.4%** in fiscal 2026 (filed dollars, 10-K `0000104169-26-000055`),
against Amazon North America **+10.0%** in 2025; Walmart global advertising **+46%** (including VIZIO) and +37-38% in the last two quarters (releases).
North America's margin **6.9%** (2025) and **7.9%** (H1 2026) is above Walmart U.S.'s 5.2%/5.8% — a better position, measured, on the same metric.

**Criterion (2) for sellers: NOT EVIDENCED either way by any fee conduct, because none is filed.**
- **No Amazon seller, fulfillment, referral or Prime fee change, and no Prime fee history, is stated in any Amazon document on disk** (10-Ks FY2015,
  FY2017-FY2025; three 10-Qs; four releases; the search list is in `peers/tableB_retail.md` B.5(a)). The filing says only *"We earn fixed fees, a
  percentage of sales, per-unit activity fees, interest, or some combination thereof"*.
- **What is filed moves with volume, not price:** third-party seller services grew 7-16% ex-FX by quarter against paid-unit growth of 8-17%, with the
  seller unit mix flat at **60-62%** of paid units from Q2 2024 to Q2 2026. Revenue per seller unit is not rising on this evidence.
- **Sellers' alternatives, in a rival's filing:** eBay 10-K FY2025: *"Consumers and merchants that sell goods on our platforms also have many
  alternatives, including general ecommerce marketplaces, such as Amazon and Alibaba"*; *"Sellers may also choose to sell their goods through alternative
  channels, such as multi-channel services like Shopify"*. Shopify GMV $378.4bn, +29.5% (10-K `0001594805-26-000007`).
- **The strongest evidence FOR near-monopoly is an allegation, and it points at criterion (3), not at a moat certificate.** 10-K FY2024: the FTC complaint
  alleges *"that Amazon has a monopoly in markets for online superstores and marketplace services, and unlawfully maintains those monopolies through
  anticompetitive practices relating to our pricing policies, advertising practices, the structure of Prime, and promotion of our own products"*, and *"All
  three courts ... denied dismissal of claims alleging that Amazon's pricing policies are an unlawful restraint of trade."* The relief sought is
  *"injunctive and structural relief"*; Italy has already imposed *"remedial actions"* and a fine cut to €752 million. **[E5-28]** says incredible pricing
  power means *"a monopoly or a near monopoly"* — and **[E2-59]** says where a regime reaches the practices a franchise rests on, the moat belongs partly to
  the regime. **The three practices a seller-side franchise case would rest on (pricing policies, advertising placement, the structure of Prime) are the
  three under suit.** Recorded; not a finding of fact.

**Leg verdict: the stores are a strong low-price business, not a franchise under criterion (2); the marketplace's pricing cannot be tested from the filing.**
Class NARROW, direction **widening on margin and units**.

### LEG 2a — Advertising ($76.1bn TTM; no margin, price or unit figure filed)
- **The strongest candidate in the company, stated at full strength:** sponsored placement on the shelf where shoppers arrive intending to buy is not
  sold by anyone else; revenue **$31.2bn (2021) → $68.6bn (2025), 21.8% a year**; **+25.1%** in H1 2026, faster than Google advertising (+14.9%) and at
  Meta's rate (+30.1%). If any leg is a toll, it is this one.
- **What the filing lets the test see: nothing about price.** Alphabet files paid clicks and cost-per-click; Meta files impressions and price per ad; **Amazon
  files neither, nor any advertising margin** (0 hits; `peers/tableC_ads_and_cloud_text.md` C.2, C.3). **[E3-03]'s pricing sentence cannot be run on this
  leg from any document**, and the one price statement found is a cut: *"Advertisers using Ads Agent see 8% lower cost-per-impression"* (Q2 2026 release).
- **Substitutes for the advertiser's dollar are named and growing:** Meta's 10-K FY2025 and 10-Q Q2 2026: *"the online commerce vertical was the largest
  contributor to the increase in advertising revenue"*; Walmart Connect in the U.S. *"up 43%"* (ex-VIZIO, Q2 FY2027 release).
- **Can I name the document that would resolve this leg?** No Amazon filing discloses advertising price, volume or profit, so the leg's franchise case is
  **unresolvable from the record** — and **it is not decisive**: advertising sits inside segments earning 42% of operating income, and granting it a full
  franchise does not move the weight below.

---
### THE COMPETITOR ROW — required **[E3-28]** *(CONVENTION, confessed at VI)*
Full row with accessions: `Test Runs/_research 2026-09-13 AMZN/peers/competitor_row.md` (Table A cloud; B retail and marketplace; C advertising;
naming and multi-sourcing sweeps). Arithmetic ratios.

| | **Amazon** | Microsoft | Alphabet | Oracle | Walmart | eBay | Meta |
|---|---|---|---|---|---|---|---|
| Cloud segment margin, latest FY | **AWS 35.4%** | IC 41.3% | GC 23.7% | not filed | — | — | — |
| Cloud growth, latest FY / H1 2026 | **+19.7% / +32.7%** | +29.7% / +30.7% | +35.8% / +73.1% | infra +76.9% / +120.7% (Q1 FY27) | — | — | — |
| Backlog / RPO | **$496bn** (6.4 yrs) | $678bn commercial | $513.9bn GC | $664bn | — | — | — |
| Capex ÷ depreciation, latest FY | **3.15×** | 3.38× | 4.33× | 7.30× | 1.88× | 1.29× | — |
| Filed cloud price conduct | **"partially offset by pricing changes", 13 years** | no executed change filed | none filed | none filed | — | — | — |
| Retail margin, latest FY | **NA 6.9% · Intl 2.9%** | — | — | — | U.S. 5.2% · Intl 3.9% | 20.5% (marketplace) | — |
| E-commerce growth, latest FY | **NA sales +10.0%; 3P services +10.3%** | — | — | — | eCommerce +24.4% | GMV +7% | — |
| Advertising growth 2025 / H1 2026 | **+22.1% / +25.1%** | search +9.4% (FY26) | +11.4% / +14.9% | — | +46% incl. VIZIO / +38% (Q2) | ads +22% | +22.1% / +30.1% |
| Ad price or unit metric filed | **none** | — | CPC +3%, clicks +13% | — | none | none | price/ad +12%, impr. +14% |

- **Peers named: 9 companies** (Microsoft, Alphabet, Oracle; Walmart, eBay, MercadoLibre, Shopify, PDD; Meta) across the three legs, of perhaps a dozen
  real competitors. **Not rowed, and stated:** Alibaba (20-F, not fetched), Temu (inside PDD), Shein and the Chinese and private clouds (no SEC filings),
  CoreWeave (not fetched). **None is load-bearing**: the AWS verdict rests on Amazon's own pricing sentence and three filed rivals; the stores verdict on
  Amazon's own competitive-factor text and Walmart's filed dollars. **Not PROVISIONAL.**
- **Names Amazon as a competitor?** Oracle (Item 1, and Item 1A's multicloud sentence) and eBay (twice, Item 1A). Alphabet, Meta, Microsoft, Walmart,
  Shopify and PDD: no instance found. Amazon's own 10-K names no competitor.
- **The row's limit [E3-61]:** it shows position, not conduct. Whether four hyperscalers behave like *"a demented Kellogg"* in a capacity glut, no filing
  and no model can say.
- **Untapped pricing power [E3-33]:** **not claimed for any leg.** AWS prices down; the stores price down by policy; the marketplace and advertising
  prices are not filed. **[E5-28]:** the near-monopoly claim exists only as a contested allegation whose remedy would cap it.
- **[E4-23] key person:** none filed; not a moat defect here.
- **[E2-53] dominance class:** not met for any leg on the row (a rival grows faster in every one).

### What the franchise case rests on — stated at full strength, because it is the strongest case against this verdict **[E4-26, E4-51]**
*"Amazon is three tolls. AWS is the largest installed base of cloud workloads, earning 36.8% on $148bn, with $496bn of contracted revenue over 6.4
years and its own chips; the stores are the default shelf of the Western internet, with paid units accelerating to +17% and North America's margin up a
point in a year; and on that shelf Amazon sells $76bn a year of advertising nobody else can sell, growing faster than Google. Regulators and plaintiffs on
three continents say it is a monopoly. The capital is going into AI capacity that two of the world's leading laboratories have contracted to buy for a
decade."*
**The answer, on the filed record:** (1) the tolls are not priced up: AWS's own MD&A has said for thirteen years that price moved against revenue, and the
stores' own strategy is lower prices; the one leg that might be a toll files no price at all; (2) the contracted revenue comes largely from two customers
Amazon is funding, one of which also buys $24.1bn a year from Microsoft; (3) the leading position in cloud is a wave, and the filer itself shortened its
server lives for the pace of change — [E4-04]'s excluded class in its own words; (4) the monopoly claim is an allegation whose remedy is aimed at the very
practices a franchise case would rest on; (5) even granting advertising and the marketplace a franchise in full, **58% of the profit and 76% of the new
capital are in the AWS leg**, and the queue's weighting practice (HAS, SONY) passes a bundle only where the franchise leg carries the weight and the rest
eats no material capital. **The strongest case is real, and it describes excellent businesses; [E3-03] asks a narrower question, and the filings answer it.**
The omission cost of a wrong close **[E3-47]** is acknowledged: this is the largest business in wave 5, and the reopening conditions at Q6 are written to
catch the error.

- **Class: [ ] WIDE [x] NARROW [ ] NONE [ ] PROVISIONAL** · **Direction: MIXED** — narrowing at AWS (returns on segment assets 30.1% → 18.1%, growth
  last of four, backlog behind three rivals), widening in the stores on margin and units, advertising growing faster than Google with its pricing unfiled;
  **and the capital is going into the narrowing leg.**
- **Can I name the document that would resolve it?** For AWS and the stores, the documents exist and were read, and they answer criterion (2). For
  advertising, no filing discloses price or profit, and that leg does not carry the weight. **So the verdict is not UNRESEARCHED and not UNKNOWABLE.**
- **VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *OUT on the business as constituted, on [E3-03] criterion (2) as [E3-03]'s own pricing sentence, [E2-44](1) and [E4-04] test it: the AWS leg, which
  earns 58% of operating income on three-quarters of the new capital, has had price move against its revenue in every filed year from 2013 to H1 2026,
  sells a service three filed rivals sell and its largest customers buy from them too, and replaces its basis on five-year lives the filer shortened for
  the pace of AI; the stores compete on price by their own description; advertising, the strongest candidate, files no price and does not carry the weight.
  Not a finding that any leg is a poor business. **The file closes here.** Q3-Q6 below are RECORDED, NOT GOVERNING.*

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

**STEP 1: DECLARE THE WEIGHT CASE.** *How much damage can this manager do before I can react?*
- [x] **Daily execution** **[E3-38]**. Q2 found strong businesses in contested categories, not a franchise; the 1991 original then governs: *"a business,
  unlike a franchise, can be killed by poor management"* **[E3-43]**. AWS re-wins capacity, chips and price against three rivals each quarter; the
  stores compete on *"selection, price, and convenience"*.
- [ ] **Control** **[E1-16]**: not ticked (a listed minority position). Mr. Bezos's holding is recorded in the proxy; no dual class.
- [ ] **Leverage** **[E3-29]**: not ticked (long-term debt $133.0bn face against $551.6bn of equity; not a 20:1 balance sheet), though debt doubled in six months (Q4).
- **Case declared: Q3 is a BINARY GATE, on daily execution.** *(Recorded, not governing.)*

**Honesty: binary, permanent, filings-based [E5-16].** *Each matter dated to when it became public.*
- **FTC settlement, Q3 2025 (10-Q Q3 2025 `0001018724-25-000123`):** *"During Q3 2025, we recorded $ 2.5 billion of expense related to the settlement of a
  lawsuit with the Federal Trade Commission (FTC)"*. **No document on disk states which FTC lawsuit was settled** or what was admitted (searched for Prime,
  ROSCA, enrolment and cancellation terms across 26 Amazon files). A corporate consumer-protection settlement, disclosed with its amount: **not a finding of
  personal misconduct on the record read.** [E5-22]: size is not seriousness in either direction; the file cannot score the conduct because the filing
  does not describe it; **recorded as a gap in candour (below), not as a conduct finding.**
- **Italian Competition Authority (December 2021; TAR ruling September 2025; appealed December 2025):** *"claiming that certain of our marketplace and
  logistics practices in Italy infringe EU competition rules. The decision imposes remedial actions and a fine of €1.13 billion ... the Italian Administrative
  Tribunal (the "TAR") affirmed the ICA's decision but reduced the fine to €752 million."* A competition finding against corporate practices, under appeal:
  **not a personal-conduct finding.** Q4 2025: *"$1.1 billion for the resolution of tax disputes associated with our stores business in Italy, and the settlement
  of a lawsuit"* (release).
- **US antitrust (FTC and states, September 2023; private suits since March 2020):** allegations, contested, partly surviving dismissal. **Open; not a
  finding.**
- **No finding of personal misconduct by a named officer or director in any document read** (10-Ks FY2015-FY2025, three 10-Qs, DEF 14A 2026, four
  releases, 8-Ks). Written as the absence of found disqualifiers, not as a finding that the managers are honest **[E5-17]**.

**STEP 2: THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each is a prompt to READ, never a verdict. The four EX-99.1 releases were read before scoring.*
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]: NOT FIRED.** "EBITDA" appears **0 times** in the four releases and the 10-K. The headline cash measure
  is free cash flow, which **subtracts** capex: *"Free cash flow decreased to an outflow of $7.6 billion for the trailing twelve months, driven primarily by a
  year-over-year increase of $66.1 billion in purchases of property and equipment"* (Q2 2026 release). **A company that leads its release with its own
  deteriorating after-capex number is the inverse of the flag.**
- [x] **The except-for prompt [E2-57] and the restructuring charge [E3-53]: FIRES as a prompt, read, and passes on disclosure.** Two consecutive releases
  restate operating income without charges: Q3 2025 *"two special charges—$2.5 billion related to a legal settlement with the Federal Trade Commission and
  $1.8 billion in estimated severance costs ... Without these charges, operating income would have been $21.7 billion"*; Q4 2025 *"three special
  charges—$1.1 billion for the resolution of tax disputes ... $730 million in estimated severance costs, and $610 million in asset impairments primarily
  related to physical stores. Without these charges, operating income would have been $27.4 billion."* GAAP is stated first and each item is quantified,
  which [E2-26] passes; but **$6.7bn of "special" charges in two quarters, severance in both**, is the pattern [E3-53] and [E5-33] warn is a real cost
  (physical-store impairments also ran ~$1.1bn in 2022). **The charges stay in the owner-earnings mean** (they are inside OCF).
- [x] **Trumpeted projections [E4-22, third]: FIRES as a prompt; the record is checked [E3-48].** Amazon guides every quarter, in wide ranges hedged as
  *"subject to substantial uncertainty"*:
  | quarter | net sales guidance | outturn | operating income guidance | outturn |
  |---|---|---|---|---|
  | Q4 2025 | $206.0-213.0bn | **$213.4bn** (above the top) | $21.0-26.0bn | **$25.0bn** (inside, after $2.4bn of special charges) |
  | Q1 2026 | $173.5-178.5bn | **$181.5bn** (above) | $16.5-21.5bn | **$23.9bn** (above) |
  | Q2 2026 | $194.0-199.0bn | **$200.6bn** (above) | $20.0-24.0bn | **$27.5bn** (above) |
  **Met or beaten on all six items checked, five of six above the top of the range.** The corpus's concern is the ratchet **[E5-30]**, and a guidance
  culture that lands above its own range is a conservative one; recorded as a live behaviour, not a failure. (Q3 2025 guidance was not on disk.)
- [x] **Serial share issuance [E5-15]: FIRES as a prompt; read, and it is employee issuance.** Shares outstanding **10,175M (2021) → 10,242M → 10,383M →
  10,593M → 10,731M (2025) → 10,783M (2026-06-30): +6.0% in four and a half years**, ~1.3% a year; one repurchase in the period ($6.0bn, 2022). **Pending:**
  up to ~41.3M shares to Globalstar holders (Step 0). Not issuance to raise capital; the cost is SBC, subtracted at Q4.
- [x] **Filed-figure tells [E4-30]: cash taxes falling as a share of pre-tax income FIRES as a prompt; read and explained.** Cash taxes / pre-tax income:
  **29.8% (2023) → 17.9% (2024) → 8.5% (2025) → 3.8% (TTM)**. The filing gives the reasons: *"reinstating the option to claim 100% accelerated depreciation
  deductions on qualified property"* (2025 Tax Act), R&D expensing, and **$80.4bn of TTM pre-tax "other income", almost all non-cash Anthropic marks** carrying
  deferred, not current, tax (+$41.4bn TTM). Excluding that other income, cash taxes were ~7.0% of pre-tax income. **Explained on the face of the filing; not
  a tell.** Reported growth is not unnaturally smooth (2022's loss).
- [ ] weak accounting: **not fired.** The Anthropic marks follow the stated measurement-alternative policy and are disclosed with amounts each quarter; the
  releases state them beside net income (*"Second quarter 2026 net income includes non-operating pre-tax other income of $53.4 billion, primarily from our
  investments in Anthropic"*). **One presentation note:** the Q4 2025 release's full-year net income line ($77.7bn) carries no such sentence for 2025's
  $15.2bn of other income. Recorded, not a cockroach.
- [ ] unintelligible footnotes: not fired.
- [x] **Metric-switching [E2-49]: a SOFT fire, recorded for checking.** The FY2022, FY2023 and FY2024 10-Ks each published two lease-adjusted free cash flow
  measures (*"Free cash flow less principal repayments of finance leases and financing obligations"* and *"Free cash flow less equipment finance leases and
  principal repayments of all other finance leases and financing obligations"*). **Both are absent from the 10-Q for Q3 2025, the FY2025 10-K and all four
  releases read** (0 hits), with no reason found. They read **lower** than plain free cash flow, and they were dropped **while TTM free cash flow fell from
  $52,973M (Q2 2024) to $14,788M (Q3 2025)** and as finance-lease additions rose again ($642M in 2023 → $4,048M TTM). **Against it:** the retained headline is
  the deteriorating one, still led with. The Q1 and Q2 2025 10-Qs were not read, so the date of the switch is not pinned. **My [E2-49] prior (six fires,
  five failures, as of 2026-09-12) is checked, not assumed: this is a soft fire, not a finding.**
- **[E3-50] stock-price targeting: not fired.** The proxy: *"We focus on long-term shareholder value that is realized by share price appreciation"*: a
  statement of how pay is realised, not the premise *"that their job at all times is to encourage the highest stock price possible"*; no stratagem found.

**Where the flags converge [E4-52]?** The fired prompts point in different directions (conservative guidance; disclosed charges; employee dilution; tax
timing explained; one soft metric drop). **No confluence toward one outcome is found.**

**STEP 3: THE PRIMARY TEST [E2-01]**, earnings on equity, balance sheet first.
- Equity (year-end): $93,404M (2020), $138,245M (2021), $146,043M (2022), $201,875M (2023), $285,970M (2024), $411,065M (2025), $551,620M (2026-06-30).
  **Equity now includes ~$219bn of carrying value in two private laboratories and $66.3bn of AOCI**, largely unrealised Anthropic note gains.
- Net income ÷ average equity: 2021 28.8% (with a Rivian gain), 2022 −1.9% (with the Rivian loss), 2023 17.5%, 2024 24.3%, 2025 22.3%, TTM ~28% (on the
  Dec-2025/Jun-2026 average, with $80.4bn of marks).
- **Operating income after tax at 21% (CONVENTION, confessed: statutory rate, strips the marks)** ÷ average equity: 2023 16.7%, 2024 22.2%, 2025 18.1%,
  TTM ~15.4%. **Primary test: passed on the level, falling on the direction**, as equity swells with marks and the plant.
- **[E2-73] the operators' own denominator:** AWS operating income ÷ average segment assets 25.0% → 30.1% → 22.3% → 18.1% (Q2); North America 13.9% TTM.

**The half-owner test [E2-26].** The filings tell the owner the AWS pricing direction every year, the Anthropic marks with amounts, the special charges by
line, the seller unit mix and paid-unit growth, and the backlog with its life. **They do not tell the owner:** what the $2.5bn FTC settlement resolved;
what share of the $496bn backlog is OpenAI and Anthropic; any advertising margin or price; the maintenance share of $173bn of capex. **Mixed: candid where
the numbers are good or neutral; silent on the three facts a half-owner would most want about the AI bet.**

**The institutional imperative: score all four [E2-30].** *Not a fraud test.*
- [ ] resists change: not ticked (reversed its own server-life extension within a year; cut roles twice in 2025).
- [x] **projects soak up funds (prompt):** Amazon Leo satellites (*"approximately $1 billion of higher year-over-year Amazon Leo costs"*, Q4 2025 guidance),
  Globalstar ($10.9bn including debt), $60bn of AI-laboratory equity in 2026, Zoox, healthcare, quick commerce.
- [ ] staff studies to justify a craving: no evidence either way in a filing.
- [x] **peers imitated (prompt):** four hyperscalers raising capex together (Table A, 3.4-9.0× depreciation) and each tied to a frontier laboratory (Microsoft
  and OpenAI in Microsoft's own 10-K; Alphabet's TPU sales; Amazon with both OpenAI and Anthropic). **[E2-27]** is the row's picture.

**Capital allocation: buybacks [E5-08, E4-31, E5-24, E2-51].**
- **The one repurchase in the window: $6.0bn in 2022**, a year of **negative free cash flow** (OCF $46,752M less net capex $58,321M = −$11,569M) and
  $21,166M of new long-term debt. **Condition (1), ample funds after operational needs, was not met in the year it was spent.** Condition (2) cannot be scored
  without the purchase prices, which were not extracted. **CAPITAL ALLOCATION FLAG on (1)**, with the humility clause **[E4-13]**: *"They also know a whole lot
  more about them than I do."* Binds position size, never the discount rate.
- **The refusal test [E2-51]:** no repurchases since 2022. At this run's own value range (Q5: well below the quote) the refusal is consistent with owners'
  interests; **not fired.**
- **Stock paid in a deal [E5-44]:** Globalstar holders may take up to 60% in Amazon shares at the quote. On this run's range the paper given is worth more at
  the quote than at intrinsic value, which favours Amazon's holders; the question the file carries instead is the **$10.9bn price for a satellite operator
  plus spectrum** beside Amazon's own expensed satellite programme [E3-40].
- **The laboratory equity [E5-24]:** *"what is smart at one price is dumb at another."* $50.0bn into OpenAI Series C and $10.0bn into Anthropic in six months,
  alongside customer commitments from the same companies. **No price per share, valuation or return case for either purchase is supplied to owners in the
  10-Q** (the Q1 2026 10-Q's *"effective price per share"* phrase is the only hit), which is **[E4-31]'s third condition in spirit: owners cannot estimate
  what was bought against what was paid.** Recorded as a prompt under [E3-40] loss of focus, and carried to Q4's named death.

**Pay and what it vests on [E4-27].** DEF 14A 2026 (`0001104659-26-041026`): *"The base salary for each of our named executive officers was $365,000"*;
*"None of the named executive officers received an annual incentive or cash bonus in 2025"*; *"We do not tie cash or equity compensation to one or a few
discrete performance goals"*; *"No reliance upon non-GAAP or adjusted performance measures in equity awards"*. **Pay vests on continued service and its value
rides the share price over long, back-end-weighted schedules.** No element rewards EBITDA, revenue, or a capex or backlog target. **Not a flag.** The
incentive to note: nothing in pay penalises capital consumed, so the capex decision is disciplined only by the share price.

**THE GUARDRAIL: checked before the verdict.**
- [x] Nothing in this Q3 is used to **promote** the name **[E2-37, E2-38, E3-39]**.
- [x] **Key-person dependence [E4-23]:** none filed.
- [x] Is a great manager the reason to act? **No; the file is closed on the business.**

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *No integrity disqualifier found (the absence of found disqualifiers, not a finding of honesty [E5-17]). Live and carried: a capital-allocation flag on the
  2022 repurchase [E5-08]; the laboratory equity bought without a value case supplied to owners [E4-31, E5-24, E3-40]; a soft [E2-49] fire on the dropped
  lease-adjusted cash measures; candour silent on the settlement's subject, the backlog concentration and advertising economics [E2-26]. IN never promotes.*

---
## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

### First: THE SKIP REASON, TESTED. It was not [E5-20]. It was a tag-union defect fixed the next day.
The wave 5 table carries AMZN under *"capex unresolved [E5-20]: build (c) by hand from the filing"*, and the ABNB run asked this
name to test which case it is before assuming the exception. **Tested by running the screen as it stood when the label was written.**
- The watchlist queue with the "capex unresolved" row was created at commit `a8bc84f` (2026-09-01 22:15). `Screens/floor_screen.py`
  at that commit, run on Amazon's companyfacts today, returns **`CAPEX_UNRESOLVED`**, and its `annual()` returns capex only for
  FY2007-FY2016.
- **The reason is in the tags, not the business.** Amazon's capex sits under `PaymentsToAcquirePropertyPlantAndEquipment` for FY2007-2016
  (the net-of-incentives line, $6,737M for 2016) and under `PaymentsToAcquireProductiveAssets` from FY2016 on (gross, $7,804M for 2016,
  $131,819M for 2025). The old `annual()` stopped at the first tag that yielded any data (the docstring's own words: *"The previous
  version wrote `if by_end: break` - the first tag yielding ANY data won and the rest were never read"*), so every window after 2016
  had no capex and the screen refused.
- **The fix landed at `dff6ab6` (2026-09-02 12:23), fourteen hours after the label was written**, and the current `floor_screen.py`
  prices Amazon: `{'5y_da': 18,421, '5y_capex': -13,770, '3y_da': 35,874, '3y_capex': 961}` ($M). The capex end reproduces to the
  dollar from the hand table below as **gross capex plus finance-lease additions** (-13,770 and 961); `run.py`'s -11,342 and 2,430
  are the same windows on gross capex alone (Step 0). The screen's `_da` end uses the broad cash-flow D&A line ($65,756M in 2025,
  which includes capitalized content and operating-lease amortization), not property-and-equipment depreciation.
- **So the label was wrong for this name for a second, different reason than at ABNB.** At ABNB the tag gap was real (a presentation
  change) and the exception did not fit. At AMZN there was no gap in the filing at all; the gap was in the screen. **Whether the
  [E5-20] exception applies is then a separate question, and it is answered below on the filed record, not on the label.**

### The construction, audited
`oe.py` (the killed session's scratch) was read line by line and **every input re-read against the filed statements**: OCF, SBC,
purchases of property and equipment, proceeds from sales and incentives, principal repayments of finance leases and of financing
obligations (cash-flow statements, FY2017 10-K `0001018724-18-000005` through FY2025 10-K `0001018724-26-000004`, newest vintage
where restated: 2016 OCF $17,272M as first filed, $17,203M from the FY2018 10-K on); property acquired under finance (capital) leases
and build-to-suit arrangements (supplemental cash-flow tables); total net additions to property and equipment and P&E depreciation
(segment note and Note 3). TTM = FY2025 − H1 2025 + H1 2026 from the 10-Q `0001018724-26-000026`, whose cash-flow statement also prints
the twelve-month column directly (OCF 161,403; SBC 19,314; capex 173,028; proceeds 4,021; lease principal 1,599; financing-obligation
principal 308; finance-lease additions 4,048; every one matched). **One input was wrong and none of its outputs used it**: build-to-suit
additions for 2021 were carried as 5,846; the FY2021 10-K supplemental table reads *"Property and equipment acquired under build-to-suit
lease arrangements | $ | 1,362 | | | $ | 2,267 | | | $ | 5,616"*. Corrected in `oe2.py`, which also defines what `oe.py` never wrote
down:
- **"cash plant"** (oe.py's "cash basis") = purchases of P&E − proceeds from sales and incentives + principal repayments of finance leases
  + principal repayments of financing obligations. Leased plant enters when its principal is paid.
- **"formation (TNA)"** = the segment note's *"Total net additions to property and equipment"*, which *"include technology infrastructure
  assets and the effect of non-cash activity such as property and equipment acquired but not yet paid"* and include finance-lease and
  build-to-suit additions. Leased and unpaid plant enters when it is placed.
- Added: **gross capex + finance-lease additions** (the current screen), and **net capex + finance-lease and build-to-suit additions**
  (the MSFT run's convention, `_research 2026-09-06 MSFT/CORRECTION - finance leases and the screen row.md`). Operating-lease assets are
  excluded throughout: their cost is already inside OCF.

**Finance leases, decided: they are capital spending by another route and they enter (c).** 2016-2021 Amazon acquired **$58.3bn** of
property under capital/finance leases (5,704 / 9,637 / 10,615 / 13,723 / 11,588 / 7,061), almost all of it equipment (FY2019 10-K `0001018724-20-000004`,
free-cash-flow reconciliation: *"Equipment acquired under finance leases"* **$12,916M** of 2019's $13,723M), and the principal was repaid in
**financing**, never in OCF. Gross capex alone understates 2016-2020 plant by about a third (finance-lease additions were 57% of gross capex
in those five years). The two lease routes (additions at placement;
principal at payment) are both shown because they time the same spending differently.

### Stock compensation: subtracted in full **[E5-06]**; RESOLVES and is COMPLETE
- The cash-flow add-back *"Stock-based compensation"* resolves in **every year 2016-TTM** from the filed statement (2,975 / 4,215 / 5,418 /
  6,864 / 9,208 / 12,757 / 19,621 / 24,023 / 22,011 / 19,467 / TTM 19,314). XBRL carries it under `ShareBasedCompensation` (and
  `AllocatedShareBasedCompensationExpense` for interims); no year is missing, dimensioned or zero.
- **Completeness, read line by line** (the Boeing check): the operating block carries no other equity-settled line (the lines are D&A,
  SBC, non-operating expense (income), deferred income taxes, and working capital). The equity statement's *"Stock-based compensation and
  issuance of employee benefit plan stock"* is **$23,960M / $21,841M / $19,161M** (2023-25), within 0.3-1.6% of the add-back and *below*
  it. The proxy describes the 401(k) as *"401(k) with company match"*; no stock-settled match or pension contribution appears in the
  cash-flow statement or the equity statement.
- **SBC/OCF: 20.9% cumulative 2016-25; 22.6% 2021-25; 12.0% TTM** (42.0% in 2022). Far below the calibrated row (CRWD 68.0%, ABNB 49.6%).
  The [E3-70] grant-date measure was not rebuilt: under 50% of OCF, the resume state's hand-read threshold is not met; the charge is the
  floor of the subtraction and is stated as such.

### Owner earnings by year, $M (`_research .../oe2.py`, output `oe2_out.md`)
| year | OCF | SBC | OCF−SBC | gross capex (run.py) | gross capex + FL adds (screen) | net capex + FL + BTS adds | cash plant | formation (TNA) | (c)=1.3× P&E D&A | (c)=P&E D&A | TNA ÷ D&A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 17,203 | 2,975 | 14,228 | 6,424 | 720 | 578 | 3,484 | 643 | 5,908 | 7,828 | 2.12× |
| 2017 | 18,365 | 4,215 | 14,150 | 2,195 | -7,442 | -9,086 | -907 | -15,633 | 2,670 | 5,319 | 3.37× |
| 2018 | 30,723 | 5,418 | 25,305 | 11,878 | 1,263 | -274 | 6,196 | 237 | 9,526 | 13,167 | 2.07× |
| 2019 | 38,514 | 6,864 | 31,650 | 14,789 | 1,066 | 3,876 | 9,306 | 1,632 | 11,955 | 16,500 | 1.98× |
| 2020 | 66,064 | 9,208 | 56,856 | 16,716 | 5,128 | 7,957 | 11,117 | -1,120 | 35,745 | 40,617 | 3.57× |
| 2021 | 46,327 | 12,757 | 33,570 | -27,483 | -34,544 | -34,503 | -33,151 | -38,755 | 3,788 | 10,661 | 3.16× |
| 2022 | 46,752 | 19,621 | 27,131 | -36,514 | -37,189 | -35,085 | -39,379 | -33,705 | -5,270 | 2,207 | 2.44× |
| 2023 | 84,946 | 24,023 | 60,923 | 8,194 | 7,552 | 11,791 | 8,135 | 12,579 | 21,630 | 30,698 | 1.60× |
| 2024 | 115,877 | 22,011 | 93,866 | 10,867 | 10,013 | 15,257 | 13,496 | 8,114 | 52,179 | 61,799 | 2.67× |
| 2025 | 139,514 | 19,467 | 120,047 | -11,772 | -14,683 | -11,625 | -10,158 | -22,305 | 65,629 | 78,187 | 3.40× |
| **TTM 2Q26** | 161,403 | 19,314 | 142,089 | **-30,939** | -34,987 | -30,966 | -28,825 | **-60,701** | 77,426 | 92,348 | **4.08×** |

**Plant formation has run at 1.6-4.1× P&E depreciation in every year for a decade, and at 4.08× in the latest twelve months.**

### MORE THAN ONE WINDOW, BOTH (c) ENDS: THE SPREAD IS PART OF THE RANGE **[E4-25, E4-38]**
| window | gross capex | + FL adds (screen) | net + FL + BTS | cash plant | **formation (TNA)** | (c)=1.3× D&A | **(c)=D&A (INVALID, below)** |
|---|---|---|---|---|---|---|---|
| **5-yr 2021-25 (the corpus default [E2-42])** | -11,342 | -13,770 | -10,833 | -12,211 | **-14,814** | 27,591 | 36,710 |
| 3-yr 2023-25 | 2,430 | 961 | 5,141 | 3,824 | -537 | 46,479 | 56,895 |
| 10-yr 2016-25 | -471 | -6,812 | -5,111 | -3,186 | -8,831 | 20,376 | 26,698 |
| 5-yr 2016-20 | 10,400 | 147 | 610 | 5,839 | -2,848 | 13,161 | 16,686 |
| 5-yr to TTM (FY2022-25 + TTM; TTM overlaps H2 2025, stated) | -12,033 | -13,859 | -10,126 | -11,346 | -19,204 | 42,319 | 53,048 |
| **TTM to 2026-06-30** | **-30,939** | -34,987 | -30,966 | -28,825 | **-60,701** | 77,426 | **92,348** |
| 8 years 2016-25 excluding 2021-22 | 7,411 | 452 | 2,309 | 5,084 | -1,982 | 25,655 | 31,764 |

**In dollars and in words, where the bottom sits:**
- **Every capex-based construction is below zero on the five-year default window (−$10.8bn to −$14.8bn a year), on the five years to TTM
  (−$10.1bn to −$19.2bn), on the ten years (−$0.5bn to −$8.8bn) and on the TTM (−$28.8bn to −$60.7bn). That is NEGATIVE: over five years
  Amazon's owners have received no owner earnings on any construction that counts the plant it actually bought.**
- Near zero, not clearly positive: the three years 2023-25 (−$0.5bn to +$5.1bn) and the eight years excluding 2021-22 (−$2.0bn to +$7.4bn).
- **Positive only where (c) is a depreciation multiple:** +$20.4bn to +$92.3bn.
- **Excluding 2021-22 does not rescue the capex ends** (they reach at most +$7.4bn a year on the eight remaining years): the negative
  five-year mean is not a pandemic artefact. It is the plant.

### Maintenance capex: a DISCLOSED JUDGMENT with a corpus DEFAULT **[E3-44, E2-41, E5-20, E4-47]**
**Which case is this? The exception class, on the filer's own words, for the plant that is most of the spending.**
- [E5-20]'s class is *"anything whose own filing says depreciation understates renewal"* (THE FRAMEWORK v4, Q4). **Amazon's filing says it
  of its servers:** *"Effective January 1, 2025 we changed our estimate of the useful lives of a subset of our servers and networking
  equipment from six years to five years. The shorter useful lives are due to the increased pace of technology development, particularly in
  the area of artificial intelligence and machine learning. The effect of this change in estimate for the year ended December 31, 2025 ...
  was an increase in depreciation and amortization expense of $1.4 billion ... which primarily impacted our AWS segment"* (FY2025 10-K, Note
  1). The six-year life it reversed had been set a year earlier (*"Effective January 1, 2024, we changed our estimate of the useful lives for
  our servers from five to six years"*). **The depreciation charged in 2024 on that subset was, by the filer's later judgment, too low.**
- The same note **lengthened** heavy equipment (*"Ten to thirteen years"*, *"Ten years prior to January 1, 2025"*), which lowers D&A on
  fulfilment and data-centre infrastructure. The two changes run in opposite directions; the filing states no effect for the second.
- **Where the plant is:** gross P&E at 2025-12-31 **$534.1bn**: servers and networking $172.5bn, heavy equipment $65.5bn, other equipment
  $63.4bn, land and buildings $155.1bn, construction in progress $71.7bn. AWS took **67.8%** of 2025 net additions (96,496 of 142,352) and
  **76.0%** of H1 2026's (90,120 of 118,648). The five-year-lived fleet is the growing majority of the spending.
- **Renewal at current scale (CONVENTION, confessed; `oe2.py`):** gross P&E by class ÷ the midpoint of its filed useful life (buildings 40
  years with land included, servers 5.5, heavy equipment 11.5, other equipment 6.5) = **~$50.7bn for 2025, 1.21× the $41.9bn of P&E
  depreciation.** It overstates slightly (gross includes fully-depreciated assets and land) and understates for a fleet whose next
  generation costs more per unit [E4-47]. The **1.3× D&A column** sits just above it and is the most generous (c) this run will call a
  judgment. **The D&A end (1.0×) is INVALID for this business as constituted** and is shown only as the most generous number constructible.
- **Where in the band (c) sits, and why the band does not resolve.** Unit volume can be kept at ~1.2-1.3× D&A. **Competitive position cannot
  be read off any filed figure**: AWS's rivals spent 3.4-9.0× depreciation in their latest periods (Table A), AWS's backlog doubled on
  commitments from two companies Amazon funds, and the filing does not separate maintenance from growth capex (no instance found of a
  maintenance or growth split in the FY2025 10-K, the Q2 2026 10-Q or the four releases). The corpus says (c) *"must be a guess"*; the guess
  here is that **the true (c) lies somewhere between ~1.3× D&A and total plant formation, and the filing cannot place it**.
- **The prior this tests (the brief's first).** *"The negative capex-only means say something about Amazon's earning power."* **Half right.**
  They are **not** evidence that the business has no earning power: at a renewal-at-scale (c), five-year owner earnings are ~$27.6bn and TTM
  ~$77.4bn. **They are** the honest answer to what owners have been paid: nothing, for five years, on any construction that counts the plant
  bought. The split between the two readings is exactly the (c) judgment, and **the band changes the sign, so by the template's own rule the
  verdict below is UNKNOWABLE on the level** [E4-25].

### The working-capital flag, run by eye (a single line moving by more than 30% of a year's OCF)
- **Fires three times:** 2017 accounts payable **+$7,100M (38.7% of OCF)**; 2021 accounts receivable and other **−$18,163M (39.2%)**; 2022
  accounts receivable and other **−$21,897M (46.8%)**. 2020 accounts payable +$17,480M (26.5%) sits just under.
- **Read:** Amazon's supplier float is real and large (accounts payable $121,909M at 2025-12-31 and $147,440M at 2026-06-30, and *"amounts due to
  third-party sellers"* among the restricted cash pledges), and it **releases cash as sales grow**; 2020's +$17.5bn is the pandemic surge. 2021-22's receivables
  and other-assets drain is the reverse. **From 2023 the filing splits out "Other assets"** (−$12.3bn / −$14.5bn / −$15.6bn / TTM −$17.8bn),
  whose balance sheet caption includes *"video and music content, net of accumulated amortization"* and *"satellite network launch services
  deposits"*: **content and satellite prepayments are already inside OCF**, which is why no "ex-working-capital" owner-earnings figure is
  computed here (it would strip real spending along with the float).
- The increment [E2-23] is therefore included, through OCF, and the float's sign is stated: in a shrinking year the payables release reverses.

### Taxes and the marks: separated
- **The Anthropic and OpenAI marks do not reach owner earnings.** TTM *"Non-operating expense (income), net"* **−$79,818M** is removed inside
  OCF, and *"Deferred income taxes"* **+$41,441M** TTM adds back the tax booked on them, so **OCF carries neither the gain nor its deferred tax.**
  Cash taxes paid were **$6,635M TTM** against pre-tax income of $175,466M (3.8%; 7.0% of pre-tax income excluding the $80,425M of other
  income). By year: 29.8% (2023, $11.2bn of $37,557M), 17.9% (2024), 8.5% (2025, $8.3bn of $97,311M). Explained in the filing: *"reinstating
  the option to claim 100% accelerated depreciation deductions on qualified property"* (the 2025 Tax Act) and R&D expensing. **Cash taxes
  are low because the plant is being deducted as it is bought; when the spending slows, cash taxes rise. That is a Q5 sensitivity, stated,
  not stacked.**
- **Look-through [E3-04]: none added** (Q1): no undistributed investee earnings are evidenced.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · **[x] good, and on the incremental AWS capital travelling toward the boundary** · [ ] gruesome
- **Evidence:** operating income $24.9bn (2021) → $93.7bn (TTM) on total P&E, net $160.3bn → $446.0bn: **~24% pre-tax on the added plant,
  consolidated.** But the leg taking the capital earns less on it each year: **AWS operating income +$30.1bn (2023 → TTM) on segment assets
  +$241.6bn (108,533 → 350,170) = ~12.5% pre-tax on the increment**, against 25.0% on the 2023 base; net sales per dollar of average AWS
  P&E 1.17× → 0.65×. **[E4-43]'s good class passes** (*"nothing shabby"* about a reasonable return on added capital), and the gruesome test
  *"unless the cash they consume gets to earn a reasonable return"* is not met today. **But the direction is toward it**, and the two largest
  new AWS commitments are from customers Amazon funds (below).

### Staying power: score all three **[E5-11]**
- **(1) a large and reliable stream of earnings: LARGE, NOT RELIABLE AS OWNER EARNINGS.** OCF $161.4bn TTM and rising every year since 2022.
  Owner earnings: see the band; negative on every capex construction over five years.
- **(2) massive liquid assets: YES, AND ALREADY SPOKEN FOR.** *"cash, cash equivalents, and marketable securities ... were $123.0 billion as of
  December 31, 2025 and June 30, 2026"* (10-Q MD&A). **After the quarter, $21.3bn went to OpenAI.** Revolvers ($20.0bn), commercial paper
  ($30.0bn programs) and the $17.5bn delayed-draw term loan are undrawn and **not counted** [E5-39].
- **(3) no significant near-term cash requirements: NO.** 10-Q Note 4: **total commitments $650,034M at 2026-06-30, up from $439,661M at
  2025-12-31 (+$210bn in six months)**; $42,752M due in H2 2026 and $78,084M in 2027; **leases not yet commenced $137,214M** (from $96,373M);
  **unconditional purchase obligations $130,065M** (from $84,772M), of which $33,026M in 2027. Beyond the table: the Anthropic facility of up
  to **$15.0bn** available *"as we reach certain delivery milestones of compute capacity"*; the Globalstar consideration (up to ~$4.6bn cash at
  today's price, plus the Apple redemption, amount not stated); capex running at $173.0bn TTM that the filing calls investment in AI.
- **Score: 1.5 of 3.**
- **Leverage, named and quantified [E4-16, E3-29]:** face value of long-term debt **$68,836M → $132,995M in six months** (10-Q Note 5,
  including March, May and June 2026 issues in dollars, euros, Swiss francs and Canadian dollars), plus a £ offering on 2026-09-11
  (424B5 `0001104659-26-107122`: *"The net proceeds from the sale of the notes are estimated to be approximately £4.231 billion"*); finance
  lease liabilities $13,451M; financing obligations $11,070M gross; operating lease liabilities $96,320M. Equity $551,620M, of which
  **~$219bn is the carrying value of two private AI laboratories** (Q1 table) and $66,287M is AOCI.
- **Coverage [E2-54]:** interest expense TTM $3,331M (FY2025 2,274 − H1 2025 1,057 + H1 2026 2,114), cash interest on debt $1,709M TTM.
  **Against OCF: ~48×. Against OCF net of capital expenditures: not covered**: TTM free cash flow as Amazon defines it is **−$7,604M**
  (release: *"Free cash flow decreased to an outflow of $7.6 billion for the trailing twelve months"*). [E2-54]'s test (*"comfortably met out
  of current cash flow net of ample capital expenditures"*) **is failed on the TTM**, with the caveat that most of that capex is growth. The
  gap is being filled with debt: $64bn of notes in six months.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**
**The mechanism: THE ROUND TRIP** *(a proposed eighteenth shape; argued against the index below).* **Amazon finances its largest cloud
customers, books their multi-year commitments as backlog, marks its stakes in them up at the funding rounds its own cash joins, and borrows to
build the capacity they have committed to buy.** The revenue, the backlog, the capex and a large part of the equity rest on the same few
counterparties' continuing ability to raise money. The business does not die; **the owner's return on the AI plant dies** if the
counterparties stop being funded, and the retail cash that would otherwise reach owners is spent carrying the plant.

**Exposure, from the filing, not experience [E4-40]:**
- **Backlog:** *"For contracts with original terms that exceed one year, those commitments not yet recognized were approximately $496 billion
  as of June 30, 2026. The weighted-average remaining life of our long-term contracts is 6.4 years"*, against **~$244bn and 4.1 years at
  2025-12-31**. In the same six months: *"AWS and OpenAI Group PBC ("OpenAI") announced an expansion of the existing $38.0 billion multi-year
  commitment ... by $100.0 billion over 8.0 years"* and *"AWS and Anthropic announced an expansion ... by more than $100.0 billion over 10.0
  years"*. **At least $200bn of the ~$252bn increase is commitments from the two companies whose equity Amazon holds.**
- **Funding of the same counterparties:** $50.0bn of OpenAI Series C in 2026 (8-K 2026-02-27; *"Subsequent to June 30, 2026, we invested the
  remaining $21.3 billion"*); Anthropic $8.0bn of notes (2023-25), $5.0bn Series G and $5.0bn Series H in Q2 2026, and a facility of up to
  $15.0bn more tied to *"delivery milestones of compute capacity"*: **Amazon's money is paid in as the lab takes delivery of Amazon's
  capacity.**
- **The marks:** Anthropic preferred and notes $190.4bn and OpenAI $28.7bn at 2026-06-30 (+$21.3bn funded after), **~$240bn against equity of
  $551.6bn**; upward adjustments *"to reflect observable changes in price related to Anthropic's fundings"* of $62.8bn in H1 2026, in a
  quarter in which Amazon itself bought Series H.
- **The plant:** AWS P&E, net $263.8bn (from $72.7bn at 2023-12-31); AWS net additions $90.1bn in H1 2026; servers on five-year lives.

**Quantified, from filed figures (my arithmetic):**
- **If the two laboratories stop being funded:** (a) the ~$240bn of carrying value (including the $21.3bn funded after June 30) is at risk of write-down (non-cash, but ~43% of the
  June 30 book equity);
  (b) commitments of ~$238bn+ (OpenAI $138bn; Anthropic "more than $100.0 billion" plus the unstated base) stand against counterparties
  without the means to pay; (c) the capacity built for them (a share of the $90bn of H1 2026 AWS additions not stated in the filing) earns
  nothing until re-let, **in a market where Microsoft, Alphabet and Oracle have added the same capacity** (Table A: 3.4-9.0× depreciation).
  AWS TTM operating income $54.7bn is 58% of the total; **every $10bn of AWS revenue lost at the 36.8% segment margin is ~$3.7bn of operating
  income**, and depreciation on the idle plant keeps running (AWS D&A $15.4bn in H1 2026, annualising ~$31bn).
- **What survives it:** North America and International TTM operating income $39.0bn; OCF before AWS capex remains large; $123.0bn of liquidity
  (less $21.3bn); debt maturities of $14.1bn (2027) and $17.1bn (2028) including interest. **The company survives. The five-year owner
  earnings, already negative on every capex construction, stay negative for as long as the plant is carried.**
- **Likelihood:** the erosion (backlog concentrated on funded counterparties, marks rising with rounds Amazon joins, capex outrunning OCF and
  filled with debt) is **not a possibility but the filed present**. The death (the two laboratories unable to raise money, commitments
  unpaid, marks written down, plant idle into a four-way glut) is **a real possibility**: no document states the laboratories' own finances,
  and **[E4-40]** forbids reading the last three years of their fundraising as the guide.

**Against the index (17 shapes, five proposed, as read at 2026-09-13 after the ABNB fold):**
- **#1 CONTRACTED NOT TO STOP (ORCL)** is the nearest and is carried beside it: Amazon's $650bn of commitments and $137bn of leases not yet commenced
  are that shape. **The difference is the other side of the ledger**: Oracle contracted to supply OpenAI; Amazon also **owns and funds** its
  largest customers and books gains on them, so the customer's solvency, the vendor's backlog and the vendor's equity are one variable.
- **#8 THE EQUITY IS THE REVENUE (RGTI)**: customers pay a small part and new shareholders pay the rest. Close in kind; at Rigetti the subject's
  own shareholders fund the subject. **Here the customer's shareholders fund the customer, and the vendor is one of them.**
- **#11 THE PASS-THROUGH (TM)**: AWS's thirteen filed years of *"partially offset by pricing changes"* are that shape's mechanism, and it is
  recorded as a later instance.
- **#10 THE CAMOUFLAGE (SONY)**: retail cash recycled into the AWS race; true of the flow, but the retail leg is not re-winning a race each
  cycle in the filing's own words, and the camouflage is not the death.
- **Proposed as the eighteenth shape, THE ROUND TRIP**, pending the operator like #13-#17. Later instances likely on the same evidence at ORCL
  (as supplier) and MSFT (as investor and supplier); not asserted for either here.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE**
  *Can I name the document that would resolve it? **No.** The (c) judgment turns on how much of $173bn a year of plant is needed to hold AWS's
  position in a four-way race, and no filing separates maintenance from growth; the counterparties' ability to pay turns on two private
  companies' future fundraising, which no document states. **The band changes the sign of owner earnings** (−$14.8bn to +$27.6bn on the
  five-year default; −$60.7bn to +$77.4bn TTM, the INVALID D&A end excluded) and [E4-25] says a range that wide is the conclusion. The company
  survives on any reading ([E5-11] 1.5 of 3); **what cannot be known is whether owners are earning anything on it.** Not a finding against the
  business, and not what closed this file.*

---

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** **Q2 is OUT (and Q4, recorded, would read UNKNOWABLE); Q5 does not open.** What follows is headed as operator rule 3 requires, and carries no entry language.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Operator rule 3 and the queue's instruction that every run ends with a price. The file closed at Q2 (OUT). Nothing below is an entry signal, a ranking or
a verdict.*

**The price and what the buyer is paying for, in words.** At **US$256.78 × 10,786,313,572 = US$2,769.7bn**, the buyer pays **~36 times the most generous
twelve-month owner earnings this run will call a judgment** (TTM, (c) at 1.3× P&E depreciation, $77.4bn), **~100 times the five-year mean on the same
judgment** ($27.6bn), and **an infinite multiple of the five-year mean on any construction that counts the plant Amazon actually bought** (−$10.8bn to
−$14.8bn a year). Put plainly: the price already pays for **AWS's $173bn-a-year build earning a return on the backlog it has signed, the two laboratories
that signed it staying funded, the stores and advertising compounding, and capex falling back toward depreciation soon enough for the cash to reach
owners**, and it asks nothing of the 10% floor in return for the thirteen years of AWS price cuts or the four-way race.

**THE FLOOR, before the ranking [E4-28, E3-13].** Honest pre-tax expectancy at this price, on the arithmetic below: **owner-earnings yield between −0.5% and
+2.8% plus whatever growth the buyer believes**; reaching ~10% needs **7.0% a year forever from the best judged twelve months, or 8.9% from the five-year
judged mean**, and is **not computable at all from a negative base**. Below roughly 10% the name is quit on, not ranked.

**1. THE YIELD** (`_research .../q5calc.py`, output `q5calc_out.txt`; cap $2,769,710M)
| base | owner earnings $M | yield | vs sovereign 5.35% |
|---|---|---|---|
| 5-yr 2021-25, formation (TNA) end (conservative) | −14,814 | **−0.53%** | −5.88 pts |
| 5-yr 2021-25, gross capex + finance-lease additions (the screen) | −13,770 | −0.50% | −5.85 |
| 5-yr 2021-25, cash plant | −12,211 | −0.44% | −5.79 |
| 3-yr 2023-25, net capex + lease and BTS additions | 5,141 | 0.19% | −5.16 |
| **5-yr 2021-25, (c) = 1.3× P&E D&A (the renewal-at-scale judgment)** | **27,591** | **1.00%** | **−4.35** |
| 3-yr 2023-25, (c) = 1.3× P&E D&A | 46,479 | 1.68% | −3.67 |
| TTM, (c) = 1.3× P&E D&A (generous) | 77,426 | **2.80%** | −2.55 |
| TTM, (c) = P&E D&A, **INVALID end**, shown as the most generous number constructible | 92,348 | 3.33% | −2.02 |

**2. WHAT THE PRICE ALREADY ASSUMES**
- Perpetual growth needed to earn the **10% floor**: **8.9%** (five-year judged mean) · **8.2%** (three-year judged) · **7.0%** (TTM judged) · 6.5% (the
  INVALID D&A end) · **refused** on every negative base. To earn merely the **bond**: 4.3% · 3.6% · 2.5% · 2.0%.
- DCF engine (casts no vote [E3-34]): **15.0% a year for ten years, then 3% forever**, from the TTM judged base; **29.2%** from the five-year judged mean;
  12.6% from the INVALID end, to justify the cap at 10%.
- What the business has actually done: net sales +12.4% (2025), +18.2% (H1 2026); operating cash flow $66.1bn (2020) → $161.4bn (TTM), **~18% a year**;
  owner earnings on any capex construction **negative over five years and falling to −$28.8bn to −$60.7bn TTM**. **[E4-35]**: sustained 15% growth is a
  fewer-than-one-in-twenty event among the most profitable companies; the engine's 15% for a decade carries that burden in writing, on the best judged
  twelve months, and the filed record of owner earnings does not discharge it. **[E4-44]**: value cannot outgrow earnings. **The ceiling [E2-63]**: AWS is
  capped by what three rivals charge for the same capacity; the stores by Walmart's price.

**3. WHAT YOU ARE PAID**
- **−2.0 to −5.9 points against the sovereign** on today's owner earnings, depending on the (c) judgment. Nothing is paid for the certainty question.

**WHERE CERTAINTY IS PRICED: AND IT IS NOT IN THE RATE [E3-42].** Sovereign used **5.35%**, bare. The end margin is the only place certainty is priced
**[E4-11, E4-48]**; it is not needed below, because the price sits above the whole range this run can defend.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**: at the 10% floor, Gordon OE × (1+g)/(0.10−g), per share:
| owner earnings | g = 0% | 3% | 5% | 6% | 7% |
|---|---|---|---|---|---|
| $5.1bn (3-yr, net capex + leases) | $5 | $7 | $10 | $13 | $17 |
| $27.6bn (5-yr, 1.3× D&A) | $26 | $38 | $54 | $68 | $91 |
| $46.5bn (3-yr, 1.3× D&A) | $43 | $63 | $90 | $114 | $154 |
| $77.4bn (TTM, 1.3× D&A) | $72 | $106 | $151 | $190 | $256 |
| $92.3bn (TTM, D&A, INVALID) | $86 | $126 | $180 | $227 | $305 |

**Conservative: nothing computable (negative five-year owner earnings on every capex construction) to ~$25-40 on the judged five-year mean · optimistic
~$150-190 (5-6% forever on the best judged twelve months) · current price $256.78.** The price enters a cell only at **7% a year forever on the best judged
twelve months ($256)**, or at ~6-7% on the D&A end this run calls invalid.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **−0.5% to +2.8% plus growth, needing 7.0-8.9% perpetual growth from a judged base (and refused from the
  unjudged one)** vs ~10% **[E4-28]**; **below → quit on; the ranking lines are not filled in.**

**WHICH BAR? Screamer test [E4-01]:** does the price clear the conservative case? **No: the conservative case is below zero.** Price above the whole
defensible range → no. No margin added; **windage count one** (the (c) judgment at 1.3× D&A is the only conservative choice; the INVALID end is displayed,
not used; the cash-tax sensitivity at Q4 is stated, not stacked).

- **VERDICT: none. Q5 did not open (Q2 OUT).** The computation shows the price above the whole value range at the 10% floor; had every gate been IN, this
  would have failed on price, and Q4's range (which changes sign) would have closed it first under [E4-25].

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

**Pre-committed [E1-02]: reopening conditions, in words, because nothing is owned and nothing is armed:**
- **Why nothing is armed:** the file failed at Q2 on the business; a price alert would be a category error (the QLYS ruling, 2026-09-07).
- **What would reopen Q2 (the error this run most fears [E3-47]):**
  1. **AWS's MD&A drops "partially offset by pricing changes" for a full year, or says price added to sales**, with usage growth holding; the first filed
     [E2-44](1) year in thirteen.
  2. **AWS's growth and margin both lead the row for a full year** (above Microsoft Intelligent Cloud's margin and above Google Cloud's growth) with capex
     ÷ depreciation falling below the rivals', a position that no longer has to be bought.
  3. **A filed advertising margin, price or volume series** showing price per ad rising with volume (the Meta-style disclosure), **and** advertising plus the
     marketplace carrying most of consolidated operating income, which would move the weight to the one leg that might be a toll.
  4. **The FTC antitrust suit resolved without structural relief** and the Italian remedies not extended, removing the regime cap on the practices a
     seller-side franchise would rest on [E2-59].
- **What would confirm the close:** AWS return on segment assets below ~15%; the backlog's OpenAI/Anthropic share disclosed as a majority; a write-down of
  either laboratory stake; capex above operating cash flow for a second full year; Walmart eCommerce growth staying above twice Amazon North America's.
- **Next catalyst dates:** Q3 2026 results (late October 2026; guidance net sales $197.0-202.0bn, operating income $22.5-26.5bn); the FY2026 10-K (~February
  2027: the first full-year server-life, backlog and commitments tables after the laboratory expansions); Globalstar close (*"in 2027"*); Anthropic or
  OpenAI funding events (each re-marks the equity).
- **Sell rule [E2-28] / monitoring [E4-17, E3-30]:** not applicable: nothing owned. Position size: **none**.
- **VERDICT (RECORDED, NOT GOVERNING): not applicable: the file closed at Q2; reopening conditions recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → **Q2 OUT, the file closed**; Q3-Q6 recorded beneath explicit RECORDED, NOT GOVERNING banners;
  Q5 headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN (the killed session's) rests on named filings; the recorded Q3 IN
  carries no such word. The renewal-at-scale (c) and the after-tax ROE are labelled CONVENTION and sit under no IN they could promote.
- [x] Every UNRESEARCHED verdict names the artifact: none issued. The Q2 non-IN verdict was put to the separating test aloud (the AWS and stores documents
  exist and were read; the advertising leg's missing figures are not filed anywhere and are not decisive) → OUT. The recorded Q4 UNKNOWABLE names what cannot
  be known (the maintenance share of $173bn of capex; two private companies' future fundraising).
- [x] Step 0: filing read with accession numbers (the killed session's); **re-struck the sovereign at the resume, unchanged**; figures cross-checked at the resume:
  every oe.py input against the filed cash-flow statements FY2017-FY2025 and the 10-Q (one wrong input found, unused); the screen's current −13,770 and 961
  reproduced to the dollar; the triage label reproduced by running `floor_screen.py` at `a8bc84f`.
- [x] Owner earnings on multi-year means; seven windows including one without 2021-22; seven (c) constructions with both ends; SBC resolves and is complete;
  the working-capital flag run by eye (fires 2017, 2021, 2022); the marks and their deferred tax separated; (c) disclosed as a judgment [E3-44, E5-20].
- [x] Competitor row filled from filings across three legs (9 companies), limits stated [E3-61]; not PROVISIONAL, with the unrowed names and why.
- [x] Sovereign for the earnings currency, from the issuing authority, dated (USD 30-year 5.35%, US Treasury, 09/11/2026, re-struck 2026-09-13).
- [x] Value stated as a round-number range under the COMPUTATION heading.
- [x] One bar (screamer), windage count one.
- [x] Prices dated; aggregator used for the quote only and flagged (US$256.78, 2026-09-11 close).
- [x] Every ledger id cited in the resumed sections was checked against `principle_ledger.csv` before the commit ([E4-27] for what pay vests on; [E4-52] only
  for convergence, where none was found).
- [x] Run committed to git with a pathspec at each stage (Step 0 and Q1 `1327743` by the killed session; Q2 `006a110`; Q3-Q6 and audit in the next commit).

**Errors of the killed session and of mine, recorded rather than smoothed:**
1. **`oe.py` carried build-to-suit additions for 2021 as 5,846**; the FY2021 10-K supplemental table reads 5,616. The array was not used by any `oe.py`
   construction, so no `oe_out.md` figure changes. Corrected in `oe2.py`.
2. **`oe.py` never wrote down what "cash basis" and "formation" meant**; both are defined at Q4 and both reproduce from the filings.
3. **The Table A pricing sweep covered the six peer documents and not the subject's own**, which carried the decisive sentence. Added as an addendum to
   `peers/competitor_row.md`.
4. **Mine:** my first draft of the pricing paragraph said "every annual report read, FY2015 to FY2025"; FY2016 was not read. Corrected before commit to the
   ten reports actually read, which between them cover every year from 2013.
5. **Mine:** the Q2 section committed at `006a110` carries em dashes in my own prose, against the standing rule (verbatim quotes and the literal
   COMPUTATION heading excepted). Left in place because it is committed history; not repeated from Q3 on.

**Tooling and brief defects found:**
- **The skip reason was a tooling artefact, not a capex finding.** `floor_screen.py` at `a8bc84f` (2026-09-01 22:15, the commit that created the "capex
  unresolved" row) returns `CAPEX_UNRESOLVED` for Amazon because its `annual()` stopped at the first capex tag with any data
  (`PaymentsToAcquirePropertyPlantAndEquipment`, which ends at FY2016), never reading `PaymentsToAcquireProductiveAssets`; the union fix landed at `dff6ab6`
  fourteen hours later and the row was never re-triaged. **The same defect may have put other names in that row**; NVDA, CL, SPGI, TOST, EQIX and DLR should be
  re-run through the current `floor_screen.owner_earnings()` before their runs, and the [E5-20] question asked separately on the filing.
- **The current screen's `_da` end for Amazon uses the broad cash-flow D&A line** (65,756 in 2025, including capitalized content and operating-lease
  amortization), 57% above property-and-equipment depreciation; its D&A end is therefore not the [E3-44] default for this filer. Not fixed (this run edits
  no tool).
- **Brief errors:** (a) *"WMT, whose filings were not yet fetched"*: Walmart's FY2026 10-K and Q2 FY2027 10-Q were already on disk from the WMT run
  (`_research 2026-09-06 WMT/`) and were used, not refetched; (b) prior 3 called AWS's position *"AWS's lead in Table A"*: AWS leads none of Table A's
  measures (second on margin, last of four on growth, fourth of four on backlog); (c) prior 2's *"sellers pay rising fees"* has no filed support: no fee change
  of any kind appears in any Amazon document on disk; (d) the brief described the capex label as the thing to test for [E5-20] vs [E3-44]; the label's cause
  was neither. Every other brief figure checked (AWS return on segment assets, the $17.5bn term loan, the $15.0bn Anthropic facility, $50.0bn to OpenAI,
  the sovereign, the −$11.3bn mean, the template and queue line numbers) matched.
- Research dumps follow the gitignored patterns (`10K_`, `10Q_`, `8K_`, `DEF14A`); `companyfacts.json`, `submissions.json`, `424B3/424B5/425` and `EX991`
  text match no ignore pattern and were left uncommitted by pathspec.

---
## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line: FAIL at Q2 (OUT on [E3-03] criterion 2 as its pricing sentence, [E2-44](1) and [E4-04] test it): AWS, 58% of operating income on 76% of H1
  2026 net plant additions, has had price move against its sales in every filed year 2013 to H1 2026, sells what three filed rivals sell to customers who buy
  from them too, and replaces its basis on five-year lives shortened for AI; the stores compete on price by their own description; advertising files no price
  and does not carry the weight. Q1 IN. Price US$256.78 × 10,786,313,572 = US$2,769.7bn; COMPUTATION — NOT A CLEARANCE: owner earnings −$14.8bn to +$27.6bn
  on the five-year default across (c) (−$60.7bn to +$77.4bn TTM), yield −0.5% to +2.8% against USD 5.35%, 7.0-8.9% perpetual growth needed for the 10% floor
  from a judged base, value roughly $25-40 (five-year judged) to $150-190 (5-6% forever on the best judged year) a share; price above the whole range.**
- If UNRESEARCHED: not applicable. If UNKNOWABLE: not applicable (Q4, recorded beneath the close, would read UNKNOWABLE on the level of owner earnings).
