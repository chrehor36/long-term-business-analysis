
---
## THE FACT THAT CHANGES WHAT THE BUSINESS IS: WS BOUGHT CONTROL OF KLÖCKNER & CO THREE DAYS AFTER ITS YEAR END

**The screen row's `deal_note` saw one Item 1.01 8-K since the 10-K and guessed "most likely a credit facility or
offering". It is neither.** The 8-K of 2026-09-08 (accession `0001193125-26-385371`) reports that Worthington
Steel GmbH, an indirect wholly owned subsidiary, *"entered into a Domination and Profit and Loss Transfer Agreement
(the "DPLTA") with Klöckner & Co SE"*. Under it, when effective, *"(i) Worthington Steel GmbH will be entitled to
issue binding instructions to the management board of Kloeckner, (ii) Kloeckner will transfer all of its annual
profits to Worthington Steel GmbH, subject to, among other things, the creation or dissolution of certain reserves,
and (iii) Worthington Steel GmbH will generally absorb all annual losses incurred by Kloeckner."* Each outside
Klöckner holder may elect *"a cash compensation of EUR 11.00 per share"* or *"a recurring annual compensation
payment ... in a gross amount of EUR 0.67 per share"*, and *"it is possible that the courts in such appraisal
proceedings may adjudicate higher compensation than agreed upon in the DPLTA."* Klöckner's general meeting votes
on it on or about 2026-10-23; effectiveness no earlier than 2027-01-01.

**The deal it completes, read from the filings:**
- **2026-01-15**: business combination agreement and a voluntary cash offer at **€11.00** per Klöckner share, *"a
  significant premium of 98% to the undisturbed three-month volume-weighted average share price of Kloeckner on
  December 5, 2025"* (8-K `0001193125-26-019521` and the 2026-03-10 release, `0001193125-26-099427`, which cut the
  minimum acceptance to 57.5% when about 56.9% had been secured).
- **2026-06-01**: **$700.0M of 7.750% Senior Secured Notes due 2033 and a $700.0M seven-year Term Loan B at SOFR +
  4.00%** (8-K `0001193125-26-253821`; 10-K Recent Business Developments).
- **2026-06-03**: settlement. *"the Company now holds a total of 60,710,791 Klöckner Shares, representing
  approximately 60.86% of Klöckner's total outstanding share capital. The total aggregate consideration for the
  Tendered Shares was €576,284,588."* (8-K Item 2.01, `0001193125-26-254547`). One million more shares on
  2026-06-15 took it to **61.87%** (10-K). Before settlement WS had already spent **$106.2M** buying Klöckner shares
  in FY2026 (cash-flow statement, "Purchases of equity securities").
- **2026-06-25**: a $550.0M asset-based revolver to 2031 replaced the old facility (8-K `0001968487-26-000018`).
- **2026-07-15 to 2026-08-12**: a delisting offer at €11.00, *"not subject to any closing conditions and does not
  include a minimum acceptance threshold"*; delisting effective 2026-08-12 (8-K `0001193125-26-304049`; the
  2026-09-08 release). **The tender count from the delisting offer is not stated in any WS filing read**; the last
  filed figure is "approximately 62%".
- **2026-08-19**: 8-K/A (`0001193125-26-356964`) with Klöckner's audited IFRS statements for 2025 and 2024 (PwC,
  Düsseldorf, report dated 2026-08-10; EX-99.1) and the unaudited pro forma combination (EX-99.2).

**What this does to the run.** WS is the **acquirer**, so the quote is not a spread and no gate is excused (the ROKU
precedent). It changes **what the business is**. On the pro forma, Klöckner is **two thirds of combined sales**:
FY2025 WS $3,093.3M plus Klöckner as adjusted $6,122.8M = **$9,216.1M**; nine months to 2026-02-28, $2,514.6M
plus $4,707.1M. Pro forma long-term debt **$2,264.8M** against WS's own $31.6M; pro forma interest expense
**$158.6M** for FY2025 against pro forma operating income of **$204.4M**; pro forma net earnings attributable to
WS **$(12.4)M** for FY2025 (EX-99.2). **No filed statement yet shows the combined company**: the FY2026 10-K ends
2026-05-31, three days before settlement, and the first 10-Q with Klöckner consolidated (quarter to 2026-08-31) is
not yet filed.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never a forecast **[E4-15, E3-32]**:
- rate **5.47 %** · date **09/24/2026** (the newest row when struck on 2026-09-25) · source (issuing authority) **US
  Treasury daily par yield curve, 30 Yr**, `home.treasury.gov` daily-treasury-rates CSV for 2026, struck fresh by this
  run and saved raw as `Test Runs/_research 2026-09-25 WS/treasury_2026.csv` (neighbouring row 5.40 on 09/23).
  `python tools/run.py WS` printed the same rate and date. **FRED not used.**
- FX: **USD sovereign for the WS perimeter of record** (FY2026: the US is most of 34 plants and the automotive
  customers are North American). **After June 2026 the earnings currency is mixed**: Klöckner's 2025 sales were
  €3,731.7M in Kloeckner Metals Americas (US and Mexico) and €2,648.4M in Kloeckner Metals Europe (Germany €1,126.4M,
  Switzerland €1,036.7M) (EX-99.1, sales by region). The EUR sovereign is not struck because no question beyond Q2
  opens (below); recorded as owed to any future Q5 on this name.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K for the year ended 2026-05-31, filed 2026-07-30, accession `0001968487-26-000026`** (`ws-20260531.htm`).
    Read: cover; Item 1 whole (products, toll versus direct, competition, raw materials and suppliers, joint
    ventures, the Separation); Item 1A summary and the competition and Kloeckner risk factors; MD&A whole (end
    markets, the HRC table, inventory holding gains and losses, results by line, the impairments, Adjusted EBIT and
    its reconciliation, liquidity, the maintenance-capex estimate, the debt); the statements of earnings, equity and
    cash flows with every reconciliation line; Note 2 (acquisitions), Note 5 (goodwill and impairment), Note 9
    (debt), Note 21 (subsequent events).
  - **10-K FY2025, `0000950170-25-099742`** and **10-K FY2024, `0000950170-24-090031`** (cash-flow statements
    FY2022-FY2025, volumes, the direct/toll mix, the competition sentences).
  - **Form 10, Amendment No. 2, filed 2023-11-13, `0001193125-23-274723`, Exhibit 99.1 (the information
    statement)**: the carve-out ("combined") statements of the Steel Processing business of Worthington Industries
    for FY2021-FY2023, including the FY2021 cash-flow statement and tons FY2021-FY2023.
  - **8-Ks**: 2026-01-22 `0001193125-26-019521`; 2026-03-10 `0001193125-26-099427`; 2026-06-02
    `0001193125-26-253821`; 2026-06-03 `0001193125-26-254547`; 2026-06-25 `0001968487-26-000015`; 2026-06-30
    `0001968487-26-000018`; 2026-07-15 `0001193125-26-304049`; **8-K/A 2026-08-19 `0001193125-26-356964` (EX-99.1
    Klöckner audited 2025 and 2024 and its Q1 2026 interim report; EX-99.2 the pro forma)**; 2026-09-08
    `0001193125-26-385371` (the DPLTA, EX-10.1 and EX-99.1); 2026-09-24 `0001968487-26-000029` (annual meeting vote).
  - Peer filings for the competitor row are listed at Q2.
- **figure cross-checked against the filed statement: FY2026 net cash provided by operating activities, $201.2M**,
  rebuilt from its own lines: net loss (12.9) + D&A 84.2 + impairments 114.3 − deferred tax 10.4 + bad debt 0.8 +
  equity income net of distributions 3.2 − gain on sale 4.7 + stock-based compensation 13.9 − unrealized gain on
  equity securities 16.0 = 172.4; working capital: receivables (16.3), inventories 47.2, payables (17.4), accrued
  compensation 5.4, other 9.9 = 28.8; **total 201.2. Ties** to the statement and to the MD&A's *"we generated $201.2
  million of cash from operating activities"*. The XBRL pull (`xbrl_out.txt`) carries the same $201.2M; FY2023's
  $315.0M ties to the Form 10's $315,011K.
- *If the filing could not be obtained → **UNRESEARCHED**.* **Not invoked.**

**THE PRICE AND THE CAP** *(struck by this run)*
- **Share count, quoted from the cover of the 10-K for the year ended 2026-05-31, accession
  `0001968487-26-000026`, the latest periodic filing** (no 10-Q has been filed since; the first-quarter period ended
  2026-08-31): *"The number of common shares (the only common stock of the registrant) outstanding, as of July 24,
  2026, was 50,948,146 ."* **One class**: the balance sheet reads *"Preferred shares, without par value ; authorized
  – 1,000,000 shares; no shares issued or outstanding"*. `python Screens/cover_shares.py WS` returned the same
  document, accession and count. The 2026-09-24 8-K gives 50,946,619 shares entitled to vote at the 2026-07-28
  record date.
- **Price $35.48** (close 2026-09-24, **aggregator quote, flagged**: Yahoo Finance chart endpoint, raw response
  `price_raw.json`; 355,800 shares traded; the same-day intraday quote at the fetch was $35.28 and is not used).
  Closing range since listing on 2023-12-01 in the pull: **$22.20 to $48.69**.
- **cap = close × shares**, `close` never `adjclose`: $35.48 × 50,948,146 = **$1,807.6M.** The screen's $1,729M is an
  earlier price on a similar count; `run.py` printed $1.81B.
- **The balance sheet beside the cap (2026-05-31, before the deal):** total debt **$256.8M** (revolver $185.4M,
  current maturities $27.0M, long-term $44.4M); cash, equivalents and restricted cash $84.6M. **After the deal: the
  $1,400M of new secured debt above plus Klöckner's debt not repaid**, which *"will be reflected in our consolidated
  debt profile once Kloeckner is consolidated"* (10-K MD&A). Noncontrolling interests (Spartan 48%, TWB 45%, WSCP
  37%, Sitem 48%, and now about 38% of Klöckner) sit between the consolidated cash flow and the WS shareholder.

**THE PERIMETER, read before any question.**
- **Spin-off 2023-12-01** from Worthington Industries (now Worthington Enterprises). Statements before that date are
  carve-out ("combined") statements of the Steel Processing business; the FY2021-FY2023 statements in the Form 10
  and the FY2024-FY2026 statements in the 10-Ks are the same perimeter restated in the same form (the FY2024 10-K
  carries FY2022-FY2023 combined figures identical to the Form 10's), so **the six years FY2021-FY2026 are judged one
  reporting perimeter, with three acquisitions inside it** named next.
- **Acquisitions inside the window**: FY2022 **$376.7M** (Tempel Steel, electrical laminations, and a tailor-welded
  blanking business; *"contributions from the Tempel acquisition"*, Form 10 MD&A); FY2024 **$21.0M**; FY2026 **Sitem
  Group, 52%**, completed 2025-06-03 ($2.9M net of cash acquired; Sitem added $165.7M of FY2026 sales). The screen's
  `acq_note` ($401M, 23% of cap) is these three.
- **Disposals and closures**: the WSP Jackson, Michigan toll facility sold 2022-10-31; WSCP's Cleveland toll plant
  closed May 2025 and sold in FY2026.
- **Klöckner, from 2026-06-03**: about two thirds of the combined business by sales, and none of it inside any
  filed WS cash-flow statement.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words.** Worthington Steel buys hot-rolled, cold-rolled and galvanized coil from the
  big US mills (Cleveland-Cliffs, NLMK, North Star BlueScope, Nucor, Steel Dynamics, U.S. Steel), about **2.57
  million tons in FY2026**, and changes it: pickles it, rolls it thinner, galvanizes it, slits, cuts and blanks it to
  a customer's exact size, welds blanks of different gauges together (TWB), or stamps it into motor and transformer
  laminations (Tempel, Sitem). It earns money two ways:
  1. **Direct sales (64% of FY2026 tons)**: it owns the steel and sells it processed. Its margin is the **spread**
     between the selling price and the coil it bought, and that spread carries the steel price cycle inside it:
     *"direct spreads (calculated as sales less material costs) were favorably impacted by a $25.6 million change
     from $10.4 million of inventory holding losses in fiscal 2025 to an estimated $15.2 million of inventory holding
     gains in fiscal 2026."* The selling price is *"closely correlated to the price of HRC"*.
  2. **Toll processing (36%)**: the mill or customer keeps title and pays a fee per ton for the processing. No
     inventory risk; volume depends on the mills' own capacity (*"softening demand from mill customers as they
     required less outside processing"*).
  - Plus a 50% share of Serviacero in Mexico (equity income $20.3M in FY2026, cash distributions $23.5M).
  - **FY2026 in figures**: sales $3,443.8M, gross margin $403.3M (11.7%), SG&A $297.4M, operating income $(1.4)M
    after $114.3M of impairments and $35.8M of Klöckner fees; 55% of sales to automotive, the top three customers
    (all automotive) **34.5%**.
- **Klöckner, now two thirds of it**: a producer-independent **steel service center and distributor** (about 110
  warehouses and processing sites in the US, Mexico, Germany, Austria and Switzerland; *"more than 60,000
  customers"*), buying from mills and selling in smaller lots at a gross profit per ton (19.0% gross margin in Q1
  2026 per its interim report in EX-99.1). The same economics as WS's direct leg with more distribution and less
  processing: **the spread over metal cost, net of warehouse and people costs.**
- **The scarce input this business controls:** none that the filings name as scarce. The steel is bought *"in the
  open market on a negotiated basis"* and *"In nearly all market conditions, steel is available from multiple
  suppliers"*; its intellectual property is not *"of material importance to our business"*. What it has is
  **processing capacity located near automotive plants** (*"Our ability to meet tight delivery schedules is, in
  part, based on the proximity of our facilities to customers"*), qualification with the automakers, and the
  metallurgical service; the registrant itself says the effect of the last two *"has not been quantified"*.
- **Will the fundamentals look broadly the same in ten years?** The mechanism, yes: coil in, processed steel out,
  a spread over the HRC price. **The company, no**: it tripled in sales in June 2026 by buying a loss-making European
  and American distributor with borrowed money, and it will be a different mix of businesses from the one whose
  record is filed. That is a question for Q2 (what the combined business is) and Q4 (what the filed history can
  say), not a failure to understand how a steel processor or a service center makes money.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — the unit economics are relatively simple and
  legible from the filings **[E3-31]**; what changes is the perimeter, recorded above and carried forward.
