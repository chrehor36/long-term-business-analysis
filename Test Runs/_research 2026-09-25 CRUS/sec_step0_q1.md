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
    revolving credit facility** maturing 2031-05-04 (undrawn at 2026-03-28), with EX-99.1 press release and EX-99.2
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

