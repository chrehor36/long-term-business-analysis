# Company Run - Cirrus Logic, Inc. (CRUS) - 2026-09-25
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

*CLAIMED 2026-09-25 04:48 EDT (write-early, commit `d57a391`; no `*Run - CRUS *.md` existed in `Test Runs/`). CIK 0000772406, NASDAQ, fiscal year ends late March. Research folder `Test Runs/_research 2026-09-25 CRUS/`. WAVE 7 name 32 of 218 (counted: line 32 of `_wave7_order.txt`; 31 lines in `_wave7_done.txt` at claim). Unattended session. Sections below are filled as they close.*

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
## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never a forecast
**[E4-15, E3-32]**:
- rate **5.47** % · date **09/24/2026** (the newest row the curve carried when this run struck it, 04:50 EDT on
  2026-09-25) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr, `home.treasury.gov`
  daily-treasury-rates.csv for 2026**, struck fresh by this run and saved raw as
  `Test Runs/_research 2026-09-25 CRUS/treasury_2026.csv`. Neighbouring rows 5.40 (09/23), 5.29 (09/22). The brief's
  5.47% was checked, not inherited; it is the same figure because no newer row exists yet. **FRED DGS30 was not used.**
- FX: **not required.** *"Our sales are denominated primarily in U.S. dollars"* (FY2026 10-K, MD&A, Net Sales).
  International sales are 99% of net sales, but that line counts *"sales to U.S.-based end customers that manufacture
  products through contract manufacturers or plants located overseas"*; the dominant customer is Apple Inc., a US
  company. USD sovereign.

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the fiscal year ended 2026-03-28, filed 2026-05-21, accession `0000772406-26-000018`**
    (`crus-20260328.htm`). Read: the cover; Item 1 whole (strategy, products, customers, manufacturing, patents,
    competition, backlog); Item 1A in the parts cited below (customer concentration, competition, the GlobalFoundries
    agreement, custom-product arrangements, acquisitions); Item 5 (repurchases); Item 7 MD&A whole through Capital
    Requirements; the income statement, balance sheet and cash-flow statement with every reconciliation line; notes on
    revenue recognition, intangibles, the revolving credit facility, commitments (GlobalFoundries), equity.
  - **10-Ks FY2023 `0000772406-23-000019`, FY2020 `0000772406-20-000007` and FY2017 `0001193125-17-181625`**, each
    carrying three years of cash-flow and income statements, so **FY2015-FY2026 (twelve fiscal years) is covered
    without a gap** from filed statements.
  - **10-Q for the quarter ended 2026-06-27, filed 2026-08-05, accession `0000772406-26-000037`** (cover, statements,
    equity note).
  - **8-K 2026-05-06 (`0000772406-26-000012`)**: Item 1.01/2.03, a third amended and restated **$350M senior secured
    revolving credit facility** maturing 2031-05-04 (*"no amounts outstanding"* at 2026-06-27, 10-Q), with EX-99.1 press release and EX-99.2
    shareholder letter for Q4 FY2026. **8-K 2026-08-05 (`0000772406-26-000036`)**: EX-99.1 and EX-99.2 for Q1 FY2027,
    the latest. **8-K 2026-03-31 (`0000772406-26-000009`)**: the CFO also became principal accounting officer; the prior
    PAO's move *"was not the result of any disagreement with the Company"*.
  - The submissions index (`subs.json`) was listed for 2024-2026: **no merger agreement, tender, S-4, 425 or
    DEFM14A. Nothing deal-shaped is live**, so the quote is an owner-earnings price, not a spread (the ROKU precedent
    tested and not triggered).
- figure cross-checked against the filed statement (say which): **FY2026 net cash provided by operating activities,
  $650,598K**, rebuilt from its own reconciliation lines: net income 414,408 + D&A 52,300 + SBC 81,811 - deferred taxes
  1,123 - other non-cash 188 = 547,208; working-capital lines -4,140 + 58,221 + 53,339 + 8,653 + 17,483 + 286 - 12,940
  - 17,512 = **+103,390**; total **650,598. Ties**, and the working-capital sum ties to MD&A's *"a $103.4 million
  favorable change in working capital"*.
- *If the filing could not be obtained -> **UNRESEARCHED**.* **Not invoked; every document came from SEC EDGAR primary
  documents.**

**THE PRICE AND THE CAP** *(struck by this run, not carried from the screen)*
- **Share count, quoted from the cover of the 10-Q for 2026-06-27, accession `0000772406-26-000037`:** *"The number of
  shares of the registrant's common stock, $0.001 par value, outstanding as of August 3, 2026 was 50,117,561 ."* One
  class; *"Preferred stock, 5,000 shares authorized but unissued"* (thousands, FY2026 balance sheet). No classes summed.
  `python Screens/cover_shares.py CRUS` returned the same document, date and count.
- **Price $118.80** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint,
  `regularMarketTime` 2026-09-24 20:00 UTC; raw response saved as `price_raw.json`). Two-year closing range in the same
  pull $77.43 to $178.90. **No split event in the two-year pull.** The pull carries a null close for 2026-09-22, a gap
  in the aggregator's series, recorded not filled.
- **cap = close x shares**, split-invariant, `close` never `adjclose`: $118.80 x 50,117,561 = **$5,954 million.**
- The screen's $5,437M implies about $108.5 a share on this count; a mid-September price, no cap flag to resolve.
  The FY2026 10-K cover's non-affiliate float, *"$ 5,001,900,563 ... as of September 27, 2025"*, is consistent.
- **The count is still falling after the cover date**: the 10-Q says *"subsequent to June 27, 2026, as of August 5,
  2026, the Company utilized $ 50.5 million to repurchase 0.4 million shares at an average price of $ 140.53"*. The
  cover count is used as the brief and the protocol require; the cap is overstated by well under 1% if those shares
  were retired after 3 August.

**THE PERIMETER, read before any question. The screen's `acq_note` sees only the five-year window [E4-25].**
1. **Wolfson Microelectronics, FY2015**: *"Acquisition of Wolfson, net of cash obtained"* **$(444,138)K**, funded by a
   $226,439K revolver draw repaid over FY2015-FY2018 (FY2017 10-K cash-flow statement). Its MEMS microphone line was
   discontinued in Q4 FY2020: *"including discontinuing efforts relating to the MEMS microphone product line. The
   Company recorded charges of approximately $21.9 million"* (FY2020 10-K MD&A).
2. **Smaller acquisitions, FY2016**: *"Acquisition of businesses, net of cash obtained"* **$(36,759)K**.
3. **Lion Semiconductor, FY2022**: *"Acquisition of business, net of cash obtained"* **$(276,884)K** (the screen's
   $277M), plus a *"Payment of acquisition-related holdback"* of **$(30,949)K** in FY2023 financing and
   acquisition-related liabilities running through operating cash (+39,656K FY2022, +12,654K FY2023, -21,361K FY2024).
   **Impaired a year later**: *"due to the prolonged weakness in the China smartphone market, which has had an adverse
   effect on sales of our general market battery and power products associated with the acquisition of Lion
   Semiconductor, Inc. ... the Company recorded an intangibles impairment charge of $ 85.8 million in fiscal year 2023"*
   (FY2023 10-K, Note 7).
4. **The GlobalFoundries prepayment, FY2022, unwinding FY2024-FY2026.** *"Prepaid wafers"* **$(195,000)K** out of
   operating cash in FY2022, then **+47,571K (FY2024), +79,357K (FY2025), +53,339K (FY2026)** back in: $180.3M of the
   prepayment has flowed back through operating cash inside the screen's three-year window. **This is a
   working-capital timing item, not earnings, and it is the first candidate for the screen's STEP UP flag** (tested at
   Q4 below).
5. **Nothing live.** No pending transaction (above). The new $350M secured revolver is undrawn.

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

*Priors from the brief, stated as hypotheses to refute and tested against the filing:*
*fabless mixed-signal company (CONFIRMED: "As a fabless semiconductor company, we contract with third parties for wafer
fabrication and product assembly and test"); fiscal year ending late March (CONFIRMED: 2026-03-28); one customer believed
to be Apple and a very large majority (CONFIRMED, and larger than "very large": 91%); foundries believed GlobalFoundries
and TSMC (CONFIRMED, with ASE, Amkor, STATS ChipPAC, SFA Semicon and SPIL for assembly and test).*

- **Unit economics in my own words.** Cirrus designs small analog and mixed-signal chips (audio amplifiers and codecs;
  haptic drivers, camera-module controllers, battery and power chips) and pays foundries and packaging houses to make
  them. Almost all of what it sells is designed for one customer's phones: the customer specifies a part for the next
  generation of a device, Cirrus spends engineering money to design it, and if the part is chosen it ships in
  hundreds of millions of units for one or a few model years, then the socket is contested again. The FY2026 income
  statement in one line: **revenue $1,997M, cost of sales $943M (gross margin 52.8%), R&D $434M (21.7% of sales),
  SG&A $160M, operating income $460M (23.0%).** Capital needs are small: purchases of property, equipment and software
  were $14.0M in FY2026 and $14.0-55.2M a year across FY2015-FY2026. The cost that matters is the R&D line, which
  is spent a year or two ahead of revenue that may or may not arrive.
- **Where the money comes from, filed:** *"we had one end customer, Apple Inc., who purchased through multiple contract
  manufacturers and represented approximately 91 percent, 89 percent, and 87 percent, of the Company's total net
  sales"* (FY2026, FY2025, FY2024); ten largest end customers 96%, 96%, 95%. **Audio $1,160M (58%), HPMS $837M (42%).**
- **The scarce input this business controls:** mixed-signal design engineering (71% of 1,668 employees are in
  research and product development), about 1,620 granted US patents, and the engineering relationship with the
  customer's product teams: *"We focus on building strong engineering relationships with our customers' product teams
  and developing highly differentiated components"*. Whether that input is scarce **relative to the customer's own
  alternatives** is the Q2 question, not this one.
- **Will the fundamentals look broadly the same in ten years?** The *mechanism* will: design a part, win a socket,
  ship it for a model cycle, re-win. The filing is plain that the *outcome* is re-decided every cycle (*"many consumer
  products have shorter design-in cycles; therefore, our competitors have increasingly frequent opportunities to
  achieve design wins in next-generation systems"*). That is a question about durability, which [E4-04] and the
  2026-09-20 ruling place at Q2, and it is carried there rather than used to close Q1.
- **The five-minute test [E4-46]:** the business can be stated in a paragraph and the filing confirms each clause.
  Nothing here needs months of study to understand what it is; what it needs is a judgment about whether the socket
  holds, which is a different thing.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

## Q2 - IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its
> customers to have no close substitute and; (3) is not subject to price regulation. The existence of all three
> conditions will be demonstrated by a company's ability to regularly price its product or service aggressively and
> thereby to earn high rates of return on capital."* **[E3-03]**, 1991 letter

**The hypothesis I came to believe while reading, stated so it can be attacked [E4-26]:** *Cirrus is a well-run
supplier whose customer holds the franchise.* The disconfirming evidence was hunted hardest, and it is set out in
full below, before the verdict.

### The three criteria, on the registrant's own words

- **(1) Needed or desired: PASSES.** Revenue $1,997M in FY2026, a record, and a record Q1 FY2027 ($459.7M).
- **(2) Thought by its customers to have no close substitute: FAILS, and the evidence is filed, dated and in the
  registrant's own words.** There is one customer that matters (91% of FY2026 sales, 90% of Q1 FY2027), so the test
  is what that customer does and what the registrant says it does. **An inference, stated:** the risk factors say
  *"our customers"* and *"some key customers"*, never the name; with one customer at 91% of sales, I read them as
  describing that customer, and a reader who declines the inference still has the pricing reductions in the
  shareholder letters, which concern the smartphone business that customer is:
  - **The customer can walk each cycle, at no cost.** *"most of our customers can stop incorporating our products into
    their own products with limited notice to us and suffer little or no penalty"*; *"our agreements with our
    customers typically do not require them to purchase a minimum quantity of our products"*; and of custom work,
    *"our customers are not always obligated to purchase new products that we develop for them"* (FY2026 10-K, Item
    1A).
  - **The customer seeks the substitute, and says so to the supplier. First filed in the FY2024 10-K (2024-05-24),
    repeated FY2025 and FY2026:** *"our customers regularly evaluate alternative sources of supply in order to
    diversify their supplier base, which increases their negotiating leverage with us and their ability to either
    obtain or dual-source components from other suppliers"*, and *"our current customers may be hesitant in some cases
    to award new business to us based on their desire to manage their supply chain risks around any potential
    over-dependence on a supplier"*. Neither bullet is in the FY2022 or FY2023 10-K; both are in FY2024's.
  - **The customer is itself a substitute.** *"many of our customers have sufficient resources to internally develop
    technology solutions and semiconductor components that could replace the products that we currently supply"*
    (in every 10-K this run opened, FY2017 and FY2020 to FY2026), and *"Our customers, particularly in the smartphone market, could potentially
    transition to different audio and system architectures, develop their own competing technologies and ICs, integrate
    the functionality that our ICs and software have historically provided into other components in their systems, or
    eliminate certain functionality that our products provide"*. **That this customer does it is on file in another
    registrant's 10-K**: Qualcomm, FY2025 10-K `0000804328-25-000085`, *"Apple began utilizing its own modem (rather
    than our products) in its recently released smartphones and we expect that Apple will increasingly use its own
    modem products"* (quoted from the QCOM run's research folder, `Test Runs/_research 2026-09-02 QCOM/02 - ...md`,
    where it was read from the filing).
  - **The customer sets the price, by contract. First filed in the FY2023 10-K (2023-05-19):** *"we have made
    commitments not to exceed certain pricing with some key customers on some of our products, and as a result, we may
    not be able to pass on any unexpected or additional cost increases or fees associated with our suppliers"*, beside
    *"We have experienced pricing pressure from certain key customers, and we expect that the average selling prices
    ("ASPs") for certain of our products will decline from time to time"*. **And the price-downs are in the current
    releases as a scheduled event**: FY2026 revenue growth *"was partially offset by pricing reductions"* (Q4 FY2026
    shareholder letter, EX-99.2 to `0000772406-26-000012`); Q1 FY2027 gross margin fell quarter on quarter on
    *"previously anticipated pricing reductions, which were partially offset by cost reductions"* (EX-99.2 to
    `0000772406-26-000036`).
  - **Where customers choose freely, they have chosen the substitutes.** The open-market business is the honest
    series here in the way units are for [E4-55]: it is the part of Cirrus's revenue not held by a single design
    partnership. Computed from the filed net sales and the filed Apple percentages (each *"approximately"*, so each
    figure is good to about $10-20M):

    | FY | net sales $M | Apple % | non-Apple $M |
    |---|---|---|---|
    | 2015 | 917 | 72 | 257 |
    | 2016 | 1,169 | 66 | **398** (Samsung alone *"approximately 15 percent"*) |
    | 2017 | 1,539 | 79 | 323 |
    | 2018 | 1,532 | 81 | 291 |
    | 2019 | 1,186 | 78 | 261 |
    | 2020 | 1,281 | 79 | 269 |
    | 2021 | 1,369 | 83 | 233 |
    | 2022 | 1,781 | 79 | 374 (Lion Semiconductor's Android business acquired this year) |
    | 2023 | 1,898 | 83 | 323 |
    | 2024 | 1,789 | 87 | 233 |
    | 2025 | 1,896 | 89 | 209 |
    | 2026 | 1,997 | 91 | **180** |

    Sources: FY2017 10-K (FY2015-17: *"79 percent, 66 percent, and 72 percent"*; *"Samsung Electronics represented
    approximately 15 percent of the Company's total sales for fiscal year 2016"*), FY2020 10-K (79/78/81), FY2023 10-K
    (83/79/83), FY2026 10-K (91/89/87). **Non-Apple revenue is down about 55% from FY2016 and about 52% from FY2022,
    after $277M was spent in FY2022 to buy diversification that was written down by $85.8M a year later** *"due to the
    prolonged weakness in the China smartphone market, which has had an adverse effect on sales of our general market
    battery and power products"*. Samsung, 15% of sales in FY2016, has not been named as a 10% customer since (every later 10-K read says *"No other customer or distributor represented more than 10 percent"*). In Q1
    FY2027 non-Apple revenue was about $46M against about $57M a year earlier (10-Q: Apple *"approximately 90 percent
    and 86 percent"* of $459.7M and $407.3M). **Those customers are buying the same functions from someone; the 10-K names eleven competitors, and
    which of them won each lost socket is in no filing this run read.** This is [E3-03] criterion (2) tested on conduct, in the open market, and it fails.
- **(3) Not subject to price regulation: passes literally, and is worth little.** No regulator sets Cirrus's prices.
  But the customer does, by contract (*"commitments not to exceed certain pricing"*), which is the same economic
  fact [E2-59] warns about in another form: the price is administered by someone other than the seller.
- **[E3-03]'s own demonstration clause runs the wrong way.** The criteria *"will be demonstrated by a company's
  ability to regularly price its product or service aggressively"*. Cirrus's filings demonstrate the opposite each
  year: price caps agreed with the customer, price reductions scheduled into the guidance, and *"reductions in selling
  prices made to retain key customer relationships"* named as a risk. The high return on capital is real (below); the
  aggressive pricing that [E3-03] says should accompany it is absent.

**Checklist:** Needed or desired [x] · no close substitute [ ] **fails** · not price-regulated [x] *(literally; the
customer caps the price by contract)*

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**
**I do not rest the verdict on [E4-04], and the reason is the 2026-09-20 ruling's own distinction.** The filing
says the socket is re-contested every generation (*"many consumer products have shorter design-in cycles; therefore,
our competitors have increasingly frequent opportunities to achieve design wins in next-generation systems"*), and
R&D of $426-458M a year (21.7-24.2% of sales, FY2023-FY2026) is the cost of re-winning. But the ruling says *"a lead
**maintained** through the generations does not"* fail [E4-04], and the filings show the Apple lead maintained: Apple
was 72% of sales in FY2015 and 91% in FY2026, and the Q4 FY2026 letter calls it *"the deep engineering partnership
that we have cultivated over the past 20 years"*. **That is a maintained lead, and I record it as the strongest fact
for the name.** What fails is not durability of the relationship but the direction of bargaining power inside it,
which is [E3-03](2) and [E2-53], below. No single great manager is named by the filing as the source; the CEO
(John Forsyth) and the CFO (Jeff Woolard, also principal accounting officer from 2026-03-25) are recorded without a
finding.

### Primary moat metric, filing-sourced, and its trend
Gross margin (the price the customer lets Cirrus keep over its foundry cost) and operating margin, FY2016-FY2026, from
the filed income statements (FY2017, FY2020, FY2023, FY2026 10-Ks; the XBRL pull in `peers_xbrl.txt` reproduces every
Cirrus figure to one decimal):

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gross margin % | 47.5 | 49.2 | 49.6 | 50.4 | 52.6 | 51.7 | 51.8 | 50.4 | 51.2 | 52.5 | 52.8 |
| operating margin % | 15.4 | 20.6 | 17.1 | 8.5 | 13.5 | 17.3 | 20.6 | 13.1 | 19.2 | 21.6 | 23.0 |

**Trend: gross margin up about five points in ten years, operating margin 8.5-23.0% with no downward trend. This is
the most important disconfirming evidence in the file and it is stated before the verdict.** A supplier whose
customer held all the bargaining power might be expected to show margins ground down over a decade. Cirrus's were not.

### THE COMPETITOR ROW - required **[E3-28]**

**Same metric (gross margin and operating margin on consolidated GAAP figures), same window (latest fiscal year and
FY2022), SEC XBRL companyfacts, `vintage="newest"`. XBRL transcription, flagged as such: the Cirrus row was checked
against its filed statements and ties; the peer rows were not opened in their filings, and the verdict does not rest
on them.**

| Company | gross margin, latest FY | operating margin, latest FY | operating margin, FY2022 | revenue, latest FY | period | named by Cirrus? |
|---|---|---|---|---|---|---|
| **Cirrus Logic (CRUS)** | **52.8%** | **23.0%** | 20.6% | $1,997M | FY to 2026-03-28 | subject |
| Texas Instruments (TXN) | 57.0% | 34.1% | 50.6% | $17,682M | FY2025 | yes |
| Qualcomm (QCOM), consolidated | 55.4% | 27.9% | 35.9% | $44,284M | FY to 2025-09-28 | yes |
| Analog Devices (ADI) | 61.5% | 26.6% | 27.3% | $11,020M | FY to 2025-11-01 | yes |
| Skyworks (SWKS) | 41.2% | 12.2% | 27.8% | $4,087M | FY to 2025-10-03 | yes |
| Synaptics (SYNA) | 44.7% | -5.6% | 20.1% | $1,197M | FY to 2026-06-27 | yes |
| STMicroelectronics (STM) | 33.9% | 1.5% | 27.5% | $11,800M | FY2025 | yes |
| Qorvo (QRVO) | 45.9% | 11.2% | 26.4% | $3,679M | FY to 2026-03-28 | no; added as the second Apple-concentrated supplier on the shelf |
| AKM (Asahi Kasei Microdevices) · Realtek · Renesas · Shanghai Awinic · Shenzhen Goodix | **not obtained** | | | | | yes |

- **Peers: 11 named by the subject** (*"AKM Semiconductor Inc., Analog Devices Inc., QUALCOMM Incorporated, Realtek
  Semiconductor Corporation, Renesas Electronics Corporation, Shanghai Awinic Technology Co., Ltd., Shenzhen Goodix
  Technology Co, Ltd., Skyworks Solutions Inc., ST Microelectronics N.V., Synaptics Incorporated and Texas
  Instruments, Inc."*); **same-metric figures obtained for 6 of them, plus Qorvo.** The five not obtained are
  non-SEC filers: AKM is a unit of Asahi Kasei (Japan, not separately reported in a comparable form), Renesas (TSE),
  Realtek (TWSE), Awinic and Goodix (Shanghai exchanges). Rung 3 (company IR, English) and rung 4 (exchange filings)
  exist for Renesas and Realtek and were **not attempted by this run**; for AKM the segment is not published in a
  comparable form. **For a moat CLAIM this would hold the class PROVISIONAL. It does not here, because the verdict
  below is OUT on the registrant's own words and its customers' conduct, and no peer's margin can reverse a filed
  admission that the customer caps the price and dual-sources** (the QCOM precedent, 2026-09-02). The most
  important competitor, the customer itself, publishes no comparable metric for its in-house silicon.
- **What the row shows, including the part that cuts for Cirrus.** (i) Cirrus sits **mid-table**: below the three
  broad-line analog and SoC companies (TXN, QCOM, ADI) on both margins, above the rest. (ii) **The two other
  Apple-concentrated suppliers are the warning label and Cirrus is the exception to it**: Skyworks' operating margin
  27.8% to 12.2% and Qorvo's 26.4% to 11.2% since FY2022, while Cirrus's rose 20.6% to 23.0%. Stated plainly because
  [E4-26] requires it: **Cirrus has held its position with the customer better than either RF supplier has.** (iii)
  The row's limit [E3-61]: *"In some businesses, the participants behave like a demented Kellogg. In other
  businesses, they don't. ... I think you'd have to know the people involved"*. The row shows where each company
  stands; it cannot show what the customer's silicon team decides for the next generation.

### The remaining Q2 tests
- **[E3-33] / [E5-28], untapped pricing power: No.** Claiming it is claiming *"a monopoly or a near monopoly"*;
  the filing shows a contractual price ceiling and scheduled price-downs.
- **[E4-37], the agony metric:** *"you can almost measure the strength of a business over time by the agony they go
  through in determining whether a price increase can be sustained"*. Here the question does not arise: the filing
  says Cirrus *"may not be able to pass on any unexpected or additional cost increases"* because of its pricing
  commitments. **Beyond agony; the decision is not the seller's.**
- **[E2-44], the two-characteristic test.** (1) *"an ability to increase prices rather easily (even when product demand
  is flat ...)"*: **fails** on the pricing language above. (2) *"large dollar volume increases ... with only minor
  additional investment of capital"*: **passes easily** (capex $14.0-55.2M a year, FY2015-FY2026, on $0.9-2.0bn of
  sales). The capital-light half is real and carries to Q4; it does not repair criterion (2).
- **[E2-45], the attacker's test:** *"how I would like, assuming I had ample capital and skilled personnel, to compete
  with it"*. **As an outside chip company, I would not like it much**: twenty years of co-design, 1,620 US patents, and
  the customer's own statement that *"new products introduced by the Company often utilize custom components available
  from only one source"* (Apple FY2025 10-K `0000320193-25-000079`, read in the AAPL run's folder) mean an outsider
  wins a socket only when the customer opens one. **As the customer, I would like it well**: the customer has ample
  capital and skilled personnel, has done it before in another socket (the Qualcomm filing above), writes the
  supplier's price ceiling, and asks for a second source. **The attacker who matters is the buyer.**
- **[E2-53], the dominance class:** *"Once dominant, the newspaper itself, not the marketplace, determines just how
  good or how bad the paper will be."* Cirrus is not in this class; **one customer determines how good Cirrus will
  be**, each generation, and the filing says so in the words above.
- **[E4-32], direction:** within the customer, content has grown (HPMS $705M to $837M, FY2024-FY2026) and the lead is
  maintained; outside it, the open-market business has halved. **Direction: narrowing everywhere except inside the one
  relationship, where it is set by the other party.**
- **[E4-36] / [E3-51], which cause of success:** the record is **wave-riding** on one customer's product cycles. FY2019
  shows what happens when the wave dips: revenue fell 22.6% (1,532 to 1,186) *"attributable primarily to reduced unit
  volumes of our portable products shipping in smartphones"* and operating margin fell to 8.5% (FY2020 10-K MD&A).
- **[E3-62], the second step:** the gains from each new Cirrus part are shared with the customer by agreed price
  reductions, and Q1 FY2027's margin line says it in one clause (*"pricing reductions, which were partially offset by
  cost reductions"*). Some stays home, visibly (gross margin 52.8%); how much is the customer's decision.

### THE VERDICT, AND THE REASONING STATED SO IT CAN BE ATTACKED

**Cirrus Logic is a very good supplier and not a franchise.** [E3-03] asks whether customers think the product has no
close substitute. Cirrus's customers answer by conduct and Cirrus reports the answer: the one customer that buys 91%
caps the price by contract, takes scheduled price reductions, buys without minimums, can stop with *"little or no
penalty"*, has told its supplier since 2024 that it evaluates and dual-sources alternatives, and has the resources to
build the part itself, which it has done in another socket on filed record. The customers who are free to choose,
outside that relationship, have chosen others: non-Apple revenue has fallen from about $398M to about $180M in ten
years while Cirrus bought a company to reverse it. **[E2-53] names what is left: the marketplace, in the form of one
customer, not Cirrus, determines how good Cirrus will be.**

**The strongest evidence against the verdict, stated so the verdict can be judged against it:** a twenty-year
relationship maintained through every product generation; gross margin up five points in ten years; operating margin
at a ten-year high; the customer's own 10-K saying its new products *"often utilize custom components available from
only one source"*; and a better record with that customer than Skyworks or Qorvo have. **[E3-47] warns that closing a
file wrongly is the costliest error class.** I weighed it, and it does not move the verdict, because every item on
that list is compatible with the customer continuing to choose Cirrus, and none of them is evidence that the customer
*cannot* choose otherwise. Sole-source within a product is a choice the customer makes for each new product; the
margin is what the customer has so far let Cirrus keep; and the filing tells me the customer is now actively managing
its dependence down. **[E5-42] keeps the two judgments apart**: this is a question about whether the advantage belongs
to the business, and the answer in the filing is that it belongs to the relationship, whose other party holds the
terms.

**Why OUT and not the perimeter close (UNKNOWABLE at Q2).** The 2026-09-20 ruling reserves UNKNOWABLE for *"A name that
passes [E3-03] and whose durability cannot be judged from filings"*. Cirrus does not pass [E3-03]: criterion (2)
fails on filed conduct and filed contract terms, and [E3-03]'s own demonstration clause (aggressive pricing) fails on
the same filings. The durability of the relationship is the part I cannot judge, and I do not need to: even if it
lasts another twenty years on these terms, the terms are the customer's.

- **Untapped pricing power** **[E3-33]**: none; the price is capped by contract.
- Class: [ ] WIDE [ ] NARROW **[x] NONE** [ ] PROVISIONAL · **Direction: the open-market business narrowing (non-Apple
  revenue down about 55% from FY2016); dependence on the one customer rising (72% to 91%, FY2015-FY2026); margins
  inside the relationship holding.**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

> **Q2 closes the file. Under the hard sequence (operator rule 2), no verdict below this point is reached and no Q5
> clearance exists.** What follows is recorded beneath the close, as the CVS and QCOM runs did, because the brief asked
> for the owner-earnings rebuild and because a later reader deciding whether to reopen Q2 needs it. None of it is a
> verdict and none of it promotes the name.

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?
**VERDICT: NOT REACHED** (Q2 closed the file). *Recorded beneath the close as prompts, without a verdict. IN would
never have promoted the name; nothing here repairs Q2 [E2-37, E2-38, E3-39].*

- **Weight case, had it been declared:** **daily execution** would be ticked. Every product generation is a new design
  contest (*"our competitors have increasingly frequent opportunities to achieve design wins in next-generation
  systems"*), which is the have-to-be-smart-every-day class [E3-38], and [E3-43]'s *"a business, unlike a franchise,
  can be killed by poor management"* applies to a name that failed [E3-03]. Control and leverage would not be ticked
  (no debt; the $350M secured revolver is undrawn at 2026-06-27). **So Q3 would have been a binary gate.**
- **Honesty matters found, dated to publication:** none in the documents read. Item 3 (Legal Proceedings) and the
  8-Ks listed in Step 0 carry no conduct matter. The 2026-03-31 8-K moving the principal-accounting-officer role to
  the CFO states the move *"was not the result of any disagreement with the Company"*. **Absence of a found matter, not
  a finding of honesty [E5-17].** The DEF 14A (2026-06-03, `0000772406-26-000024`) was not read.
- **The flags, as prompts:**
  - **[E4-29] EBITDA promotion: does not fire.** The word does not appear in the Q4 FY2026 or Q1 FY2027 release or
    letter; the 10-K's uses are the credit-agreement covenant definitions.
  - **Adjusted earnings / [E5-06]: fires as a prompt.** The releases lead with non-GAAP EPS that excludes stock-based
    compensation: Q4 FY2026 non-GAAP diluted EPS **$1.95**, with *"Effect of Stock-based compensation expense"* of
    **$0.38** a share added back (EX-99.1 to `0000772406-26-000012`). SBC was $81.8M in FY2026, 12.6% of operating cash.
    GAAP figures are presented first and reconciled line by line, which is the half-owner test [E2-26] passed on form.
  - **[E4-22] projections: quarterly guidance ranges, not growth targets.** One outturn checked: Q1 FY2027 guided
    *"$430 million to $490 million"* (Q4 FY2026 letter), reported **$459.7M**, inside the range. No multi-year target
    found in the documents read.
  - **Serial issuance [E5-15]: the reverse.** Basic weighted shares 63.4M (FY2018) to 51.1M (FY2026); cover count
    50.1M. Repurchases FY2015-FY2026 **$1,738M** plus **$229M** for employee tax withholding, against SBC of **$723M**
    over the same twelve years.
  - **[E4-30] filed-figure tells:** the reported growth is not smooth (revenue -22.6% in FY2019; operating margin
    8.5-23.0%). The FY2026 tax rate fell to 16.6% from 25.5% on a filed, named cause (the OBBBA's restoration of R&D
    expensing, MD&A); cash taxes paid were $49.6M against $51.7M a year earlier. No tell found.
- **Capital allocation, the record:** two acquisitions bought to diversify and both written down: **Wolfson ($444M,
  FY2015)**, whose MEMS microphone line was discontinued with $21.9M of charges in FY2020, and **Lion Semiconductor
  ($277M, FY2022)**, impaired by **$85.8M** in FY2023. **[E2-56]'s camouflage test would be the first read**: a
  marvellous core relationship hiding acquisition failures elsewhere. The buyback prompt [E5-08] would need an IV range
  this run did not reach; recorded only that the company bought at an average **$142.54** in Q4 FY2026 and **$140.53**
  in July-August 2026, against **$118.80** now.
- **Candor, one line from the latest letter:** *"While we understand there is intense interest in this customer, in
  accordance with our policy, we do not discuss specifics about this business."* The customer is named in every 10-K;
  the specifics are withheld. Recorded under [E2-26], without a finding.

## Q4 - WILL IT SURVIVE?
**VERDICT: NOT REACHED.** *The owner-earnings rebuild the brief asked for, recorded beneath the close. It is not a
verdict.*

### Owner earnings **[E2-23]**, FY2015-FY2026, from the filed cash-flow statements (four 10-Ks, twelve years)
*CONVENTION (framework section VI): operating cash flow less SBC, less the (c) guess.* **No net-income proxy.**
(c) is carried as a band: **total capex** (purchases of property, equipment and software, plus *"Investments in
technology"*) at the high-OE end, **D&A** at the low-OE end ([E3-44]'s default proxy). **SBC resolves in every one of
the twelve years** from the filed *"Stock-based compensation expense"* line; it is complete and subtracted in full
[E5-06].

| FY | OCF | SBC | D&A | capex + tech | OE, capex end | OE, D&A end | prepaid-wafer line in OCF |
|---|---|---|---|---|---|---|---|
| 2015 | 163.5 | 37.5 | 34.9 | 36.7 | 91.1 | 89.2 | - |
| 2016 | 149.0 | 33.5 | 58.1 | 46.1 | 69.5 | 57.5 | - |
| 2017 | 369.8 | 39.6 | 63.4 | 51.3 | 278.9 | 266.7 | - |
| 2018 | 318.7 | 48.7 | 81.4 | 84.5 | 188.6 | 185.5 | - |
| 2019 | 206.7 | 49.7 | 79.8 | 35.8 | 121.2 | 77.2 | - |
| 2020 | 295.8 | 53.8 | 68.2 | 21.6 | 220.5 | 173.8 | - |
| 2021 | 348.9 | 56.8 | 47.1 | 20.5 | 271.7 | 245.1 | - |
| 2022 | 124.8 | 66.4 | 62.1 | 30.0 | 28.4 | -3.7 | **-195.0** |
| 2023 | 339.6 | 81.6 | 71.2 | 36.7 | 221.2 | 186.7 | - |
| 2024 | 421.7 | 89.3 | 48.3 | 38.3 | 294.1 | 284.1 | **+47.6** |
| 2025 | 444.4 | 84.1 | 51.0 | 28.8 | 331.5 | 309.3 | **+79.4** |
| 2026 | 650.6 | 81.8 | 52.3 | 14.8 | 554.0 | 516.5 | **+53.3** |

$ millions. Arithmetic in `Test Runs/_research 2026-09-25 CRUS/oe.py` and `oe_out.txt`.

- **Which (c) case, and why:** fabless, so the ordinary case. Total capex runs below D&A in ten of twelve years (above it only in FY2015 and FY2018), and
  D&A carries the amortization of acquired intangibles (Wolfson, Lion), which [E3-44] itself adds back (*"reported
  earnings plus amortization of intangibles usually gives a pretty good indication of earning power"*), so the D&A
  end over-states (c) and is the conservative end. Band carried whole; not resolved by preference [E2-09]'s *"(c) must
  be a guess"*.
- **THE SCREEN'S STEP UP, found and named [E4-41].** Three things stepped, and only one is earnings:
  1. **The GlobalFoundries prepayment unwinding**: $195.0M paid out of operating cash in FY2022, **$180.3M returned
     through operating cash in FY2024-FY2026**, $14.7M still on the FY2026 balance sheet. A timing item. **Stripped**
     from every window below (the "adjusted" rows); in the five-year window it nets to -$14.7M and barely matters, in
     the three-year window it is $60M a year.
  2. **An inventory release in FY2026**: +$58.2M. Left in (working-capital noise inside a window, and FY2025 carried a
     -$71.8M build).
  3. **Real operating growth**: income from operations $343M, $410M, $460M (FY2024-FY2026); the tax rate fell on a
     named statute. **This is the part that persisted.**
  4. **And one favourable item flagged for the next quarter, not yet in any window**: the Q1 FY2027 letter expects
     *"a temporary benefit from wafers purchased under prior agreements with GlobalFoundries at favorable pricing ...
     after which gross margin should normalize"*.
- **MORE THAN ONE WINDOW [E4-25], prepaid-wafer line stripped:**

  | window | OE mean, D&A end | OE mean, capex end |
  |---|---|---|
  | 3 years, FY2024-26 | $310M | $333M |
  | **5 years, FY2022-26 (the default [E2-42])** | **$262M** | **$289M** |
  | 7 years, FY2020-26 | $247M | $277M |
  | 10 years, FY2017-26 | $226M | $253M |
  | 12 years, FY2015-26 | $200M | $224M |
  | FY2026 alone | $463M | $501M |

  **Spread, conservative end: the five-year figure sits 16% below the three-year; the combined range across windows and both (c) ends is
  $200M to $333M**, and FY2026 alone sits far above every multi-year mean. The screen's own five-year band ($259-288M)
  is reproduced to within $3M; its three-year $370-396M is the unstripped figure. **What the range says [E5-11]:** the
  earnings level has stepped up, and a distorted item (the prepayment) sat in the short window.
- **Great, good or gruesome [E4-20], a prompt only:** on its filed capital, closer to great: operating income $460M
  in FY2026 on about $518M of net tangible operating assets (equity $2,128M less goodwill $436M, intangibles $21M and
  cash and securities $1,154M), and capex $14.8M. That is a statement about the capital the business needs [E5-42],
  not about whether it holds its customer.
- **Staying power [E5-11], a prompt only:** (1) earnings stream large but not reliable (FY2019 fell 22.6% on the
  customer's units); (2) **massive liquid assets**: $1,167M of cash and securities at 2026-06-27 against no debt;
  (3) **no significant near-term cash requirements** found beyond the GlobalFoundries purchase commitment through
  calendar 2026 and leases ($134M of lease liabilities).
- **The named way it dies [E2-27, E3-24]**: the customer designs the function in-house, or integrates it, or awards the
  next generation to a second source. The filing names all three. **Quantified**: at 91% of sales, losing half of the
  customer's business in one product cycle would take roughly $900M of revenue from a company whose FY2026 operating
  expenses were $594M; against FY2019, when unit volumes alone cut revenue 22.6% and operating margin to 8.5%. **Likely
  a real possibility, over a decade**; the likelihood is not something the filings let me estimate. Modelled on
  exposure, not experience [E4-40]: twenty years without the loss is experience.

---
⛔ **Q5 does not open. Q2 is OUT.**

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**VERDICT: NOT REACHED.** No ranking position exists; a name that failed Q2 is not ranked.

### COMPUTATION — NOT A CLEARANCE
*Arithmetic only, no box ticked, no entry language. Produced because the queue records it for every run.*
- **Yield on the $5,954M cap:** five-year stripped owner earnings $262-289M = **4.4% to 4.9%**; three-year stripped
  $310-333M = 5.2% to 5.6%; FY2026 alone $463-501M = 7.8% to 8.4%. Sovereign **5.47%**.
- **Net of cash, stated as a judgment**: take out $1,167M of cash and securities and about $31M of after-tax interest
  income (FY2026 interest income $37.7M at the 16.6% rate; a disclosed estimate) and the five-year figure is 4.8% to
  5.4% on $4,787M; FY2026 alone is 9.0% to 9.8%.
- **At the ~10% floor [E4-28] with no growth:** the five-year owner earnings less the interest estimate, capitalised
  at 10%, are worth roughly $2.3-2.6bn, plus $1.2bn of cash, about **$3.5-3.7bn against a $5.95bn quote**; the best
  single year ever filed (FY2026, stripped), on the same construction, is worth about $5.5-5.9bn. **The quote is above
  every no-growth construction here, narrowly so at the top of the best year.**
- **Windage count: ONE** (the prepayment strip, [E4-41]); the (c) band and the window spread are displayed, not spent.

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**VERDICT: NOT REACHED** (nothing to sell; no position). **The reversal conditions, in words, for whoever reopens
Q2** (the QLYS ruling: a Q2 failure gets no price alert):
1. **A 10-K in which the pricing commitments and the dual-sourcing language are withdrawn**, and the shareholder
   letters stop reporting *"pricing reductions"* as a scheduled item, while gross margin holds or rises. That would
   be [E3-03]'s demonstration clause turning.
2. **Non-Apple revenue recovering on the open market**: three consecutive fiscal years of growth in revenue from
   customers other than the largest, to above the FY2016 level (about $400M), from general-market products rather
   than an acquisition. That would show customers who are free to choose choosing Cirrus.
3. **A multi-year supply or co-development agreement filed as a material contract** that binds the customer (minimum
   purchases, exclusivity running in Cirrus's favour, or price terms that pass costs through). The 10-K says today's
   agreements *"typically do not require them to purchase a minimum quantity"*.
- **The moat-downgrade question, for the record [E3-30]:** the open-market decline is not an aberrational cycle on
  the filed series; it runs FY2016 to FY2026 through two smartphone cycles and an acquisition.
- **Next catalyst dates:** the Q2 FY2027 results (guided *"$510 million to $570 million"*; the prior year's Q2 release was filed 2025-11-04) and the
  FY2027 10-K (May 2027), whose Item 1A is where conditions 1 and 3 would first appear.

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Step 0, Q1 IN, Q2 OUT; Q3-Q6 marked NOT REACHED and their
      material recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the 10-K's own
      description, confirmed clause by clause.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued. The five unobtained peers are
      named at Q2 with their exchanges and the rung not attempted.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued; the perimeter close was
      considered at Q2 and refused in writing.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026 operating cash $650,598K
      rebuilt from its lines; ties, and its working-capital sum ties to the MD&A's $103.4M).
- [x] Owner earnings on a multi-year mean; five windows stated; capex band disclosed as a judgment (beneath the close).
- [x] Competitor row filled: 6 of 11 named peers plus Qorvo, XBRL transcription flagged; the verdict does not rest
      on the row, and why is stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury par curve), dated
      09/24/2026.
- [x] Value stated as a round-number range, not a point estimate (inside a COMPUTATION block only).
- [x] One bar chosen, not both: none; Q5 not reached. Windage count stated (one).
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git, with pathspecs, after the claim, after Q1, after Q2 and after this section.

**The brief's priors, scored:**
- *Fabless mixed-signal, fiscal year to late March/early April*: **confirmed.** Product list confirmed (amplifiers,
  codecs, smart codecs; camera controllers, haptics and sensing, battery and power ICs).
- *FY2026 10-K filed, and a 10-Q to 2026-06-27*: **confirmed**: `0000772406-26-000018` (filed 2026-05-21) and
  `0000772406-26-000037` (filed 2026-08-05).
- *One customer, believed Apple, a very large majority*: **confirmed and named by the registrant**: 91% of FY2026 and
  90% of Q1 FY2027. What it means was tested, not assumed, and it is the Q2 verdict.
- *Foundry believed GlobalFoundries, TSMC and others*: **confirmed**; terms read (capacity reservation through calendar
  2026, amended February 2025; $195M prepaid in FY2022, now down to $14.7M; a new process programme at GF's Malta,
  New York fab under the customer's American Manufacturing Program).
- *acq_note $277M inside the window*: **confirmed as Lion Semiconductor (FY2022)**, and the run found what the
  five-year window cannot: Wolfson ($444M, FY2015) behind it, both written down in part. **Nothing deal-shaped live.**
- *Share count fallen through buybacks*: **confirmed**; 63.4M basic weighted (FY2018) to 50.1M on the cover;
  $1,738M of repurchases over twelve years against $723M of SBC.
- *STEP UP flags*: **found and split** into a timing item ($180.3M of prepaid wafers returning through operating cash
  in FY2024-FY2026, stripped), an inventory release, and real operating growth that persisted.

**My own errors, caught before commit:**
1. First wrote the capex range as "$13.9-55.2M" (the low end is $14.0M, FY2026). Corrected.
2. First wrote R&D as "22-24% of sales"; the filed range is 21.7-24.2%. Corrected.
3. First wrote that the "internally develop" risk factor appeared in "every 10-K read, FY2017 to FY2026"; I had
   opened FY2017 and FY2020-FY2026, not FY2018-FY2019. Narrowed to what was opened.
4. First wrote that *"the eleven competitors the 10-K names are the ones those customers chose"*: no filing read says
   which competitor won which lost socket. Removed and replaced with what is filed.
5. First presented the risk-factor language (*"our customers"*, *"some key customers"*) as if it named Apple. It does
   not; the inference is now stated as an inference.
6. First wrote "total capex runs below D&A in eleven of twelve years"; it is ten (FY2015 and FY2018 are above).
7. First computed the no-growth value at the floor by adding cash to owner earnings that already contain the interest
   on that cash (a double count, about $0.3bn). Corrected by removing an estimated $31M of after-tax interest first.
8. First attributed *"(c) must be a guess"* to [E2-23]; the ledger row carrying those words is [E2-09]. Corrected.
9. First wrote the new revolver as "undrawn at 2026-03-28", a date before it existed; now quoted from the 10-Q at
   2026-06-27.

**Errors in the brief:** none of substance found. The brief's "WAVE 7 name 32 of 218" was counted and is right
(line 32 of `_wave7_order.txt`; 31 lines in `_wave7_done.txt` at claim). The brief's ledger count "311 rows at last
count" was counted: `csv.DictReader` returns **311** rows (312 physical lines with the header). The brief's
"newest_filing 2026-03-28 is a period end" is right; the 10-K was filed 2026-05-21.

**Tooling observations (reported, not patched):**
- `tools/run.py CRUS` did **not** miss a filed 10-K (the CLX defect did not recur here): its FY2024-FY2026 columns
  match the filed statements. It **reads capex as purchases of property, equipment and software only and omits
  "Investments in technology"** ($0.7-29.3M a year; $29.3M in FY2018), so its capex end runs slightly high. It also
  prints the three-year window as the headline yield (6.21-6.65%) with the GlobalFoundries prepayment unwind inside
  it; the stripped three-year figure is $310-333M, not $370-396M. The tool prints the divergence warning, correctly;
  it cannot see a prepayment.
- `tools/sources.cik_for()` returns a tuple (CIK, name), not a CIK string; a script passing it straight to
  `sec_facts()` builds a malformed URL. Not a defect in the tool's own callers, a trap for new scripts.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **CRUS FAIL at Q2 (OUT, ON THE BUSINESS). Q1 IN. [E3-03] criterion (2) fails on filed conduct and contract
  terms: the customer that is 91% of sales caps prices by contract, takes scheduled price reductions, buys without
  minimums, can stop with "little or no penalty" and has dual-sourced since the FY2024 10-K, while customers free to
  choose have moved away (non-Apple revenue about $398M in FY2016 to about $180M in FY2026); [E2-53]: one customer, not
  the business, sets how good it will be.** Price $118.80 (2026-09-24, aggregator, flagged) x 50,117,561 shares (10-Q
  cover, `0000772406-26-000037`) = $5,954M; sovereign 5.47% (US Treasury, 09/24/2026).
- **If UNRESEARCHED:** not applicable.
- **If UNKNOWABLE:** not applicable.
