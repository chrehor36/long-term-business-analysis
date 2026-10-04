# Company Run — Worthington Steel, Inc. (WS) — 2026-09-25
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**CLAIMED AT DISPATCH 2026-09-25.** Unattended run. Sections are appended as each question closes. Research: `Test Runs/_research 2026-09-25 WS/`.

*Wave 7 name 37 of 218 (line 37 of `Screens/_daily/_wave7_order.txt`; 36 lines in `_wave7_done.txt` at claim, the last being NATH). No `*Run - WS *.md` existed in `Test Runs/` at claim.*

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

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The rule, quoted from the ledger row itself** (`principle_ledger.csv`, E3-03, 1991 letter): *"An economic franchise
arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no close
substitute and; (3) is not subject to price regulation. The existence of all three conditions will be demonstrated
by a company's ability to regularly price its product or service aggressively and thereby to earn high rates of
return on capital."* **The commodity end has its own row, [E2-58] (1982 letter)**: *"For the great majority of
companies selling "commodity"products, a depressing equation of business economics prevails: persistent
over-capacity without administered prices (or costs) equals poor profitability."* Its one exception is *"a cost
advantage that is both wide and sustainable. By definition such exceptions are few"*. The question is asked of the
business as it now stands: WS's own processing (one third of pro forma sales) and Klöckner's distribution (two
thirds).

- Needed or desired [x] · no close substitute [ ] **refuted by the registrant, below** · not price-regulated [x]
  (Section 232 tariffs shape the input price; they administer no processing price)
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]** Not the ground: the
  business does not pass [E3-03] first, so the perimeter close (UNKNOWABLE) is not available **[E4-08]**.

### THE REGISTRANT'S OWN WORDS ABOUT SUBSTITUTES AND PRICE (10-K FY2026, `0001968487-26-000026`)
- *"The steel processing industry is fragmented and highly competitive. There are many competitors, including other
  independent intermediate processors. Competition is primarily on the basis of price, product quality and the
  ability to meet delivery requirements."*
- *"Processed steel products are priced competitively, primarily based on market factors, including, among other
  things, market pricing, the cost and availability of raw materials, transportation and shipping costs, and
  overall economic conditions in the U.S. and abroad."* And: *"The market price of our products is closely
  correlated to the price of HRC"*.
- On the two things that could differentiate it: *"the extent to which technical service and support capability has
  improved our competitive position has not been quantified"*; *"The extent to which plant location has impacted our
  competitive position has not been quantified."*
- **Where FY2026 volume was lost, the stated cause is competition**: *"with construction, heavy truck, agriculture,
  and service center volumes down 8%, 10%, 10%, and 33%, respectively. The decrease in construction and service
  center volumes was largely driven by increased competition"*; and *"an $8.8 million unfavorable impact due to
  value-added market spread compression"*.
- **The one leg the company calls highly engineered, electrical steel laminations (Tempel, Sitem)**: goodwill
  **fully impaired** in Q4 FY2026, $53.8M, plus $58.4M of long-lived assets: *"The impairments resulted from weakened
  demand in certain end markets, particularly industrial motors in both Europe and the United States, due to
  increased foreign competition, and in automotive, some delayed program launches."* That leg was bought in FY2022
  for most of $376.7M.
- **Price against the input, in the registrant's own risk language, every year FY2021-FY2026**: *"In an environment
  of increasing prices for steel and other raw materials, competitive conditions may impact how much of the price
  increases we can pass on to our customers."* The margin rides the cycle through inventory: holding gains of $15.2M
  in FY2026 after holding losses of $10.4M in FY2025; the Form 10 records *"lower inventory holding gains, down an
  estimated $53.1 million from fiscal 2021"* in fiscal 2022, and *"an estimated $70.5 million unfavorable swing related
  to estimated inventory holding losses of $48.6 million in fiscal 2023 compared to estimated inventory holding gains of
  $21.9 million in fiscal 2022"*, so FY2021's holding gains were about **$75M** (my arithmetic), about a third of that
  year's $221.5M operating income. That is **[E2-58]'s mechanism**: profitability set by the
  steel cycle (HRC averaged **$869 a ton in FY2021, $1,588 in FY2022, $889, $866, $754 and $915** in FY2023-FY2026,
  the 10-Ks' CRU tables), not by the processor.

### THE PHYSICAL SERIES [E4-55] (tons shipped, from each year's MD&A; the row is itself a steel service-center passage)
*[E4-55], 2006 Wesco letter, of Precision Steel: "This decline in physical volume is a serious reverse, not likely to
disappear in some ""bounce back'' e�ect. Nor do we expect another sharp rise in prices like the approximately 40%
rise that recently occurred, holding dollar volume roughly level despite a precipitous drop in physical volume."*
*(The ledger row carries the OCR artifact "e�ect" for "effect"; flagged, not smoothed.)*

| FY | tons | direct / toll | net sales $M | gross margin $M | per ton | operating income $M (margin) | HRC $/ton |
|---|---|---|---|---|---|---|---|
| 2021 | 4,172,823 | 49 / 51 | 2,127.4 | 370.8 | $89 | 221.5 (10.4%) | 869 |
| 2022 | 4,285,335 | 52 / 48 | 4,068.9 | 395.5 | $92 | 226.6 (5.6%) | 1,588 |
| 2023 | 3,954,575 | 57 / 43 | 3,607.7 | 336.5 | $85 | 120.2 (3.3%) | 889 |
| 2024 | 4,007,373 | 56 / 44 | 3,430.6 | 439.8 | $110 | 194.5 (5.7%) | 866 |
| 2025 | 3,793,752 | 57 / 43 | 3,093.3 | 388.6 | $102 | 147.0 (4.8%) | 754 |
| 2026 | 3,586,817 | 64 / 36 | 3,443.8 | 403.3 | $112 | (1.4) (0.0%) | 915 |

*Sources: Form 10 EX-99.1 (FY2021-FY2023), 10-K FY2024, FY2025, FY2026; per-ton and margin columns my arithmetic.*

- **Tons fell 14% FY2021-FY2026 while two acquisitions were added** (Tempel in FY2022, Sitem in FY2026); **toll tons
  fell about 39%** (2.13M to 1.29M, partly the Jackson sale and the Cleveland closure, partly *"softening demand from
  mill customers"*), direct tons rose about 12% (2.04M to 2.30M, with Sitem inside the last year).
- **Gross margin per ton rose from $89 to $112.** That is the strongest number in the file for the company and is
  answered below: it is mix (toll out, direct and laminations in), acquired, and it did not reach operating income,
  which has not exceeded the FY2021-FY2022 level in any year since.
- **Direct selling prices: down about 6% in FY2025, up 3% in FY2026 while the HRC average rose 21%** ($754 to $915).
  A processor that captured the input rise would show the reverse.

### THE COMPETITOR ROW — required [E3-28]
*Metric: operating income over net sales, as reported, the last three filed fiscal years (a five-year view where
filed). Peers' calendar years against WS's May years. WS and Olympic Steel from the filed statements; Reliance and
Ryerson from XBRL company facts (transcription, flagged); Klöckner from its audited IFRS statements filed as EX-99.1
to WS's 8-K/A.*

| Company | operating margin | window | source |
|---|---|---|---|
| **Worthington Steel** | **5.7% / 4.8% / 0.0%** (FY2026 after $114.3M impairments and $35.8M deal fees; about 4.3% before them, my arithmetic); five-year 5.6%, 3.3%, 5.7%, 4.8%, 0.0% | FY2022-26 | 10-Ks `0000950170-24-090031`, `0000950170-25-099742`, `0001968487-26-000026` |
| **Reliance, Inc.** (RS; the largest US service center) | **11.7% / 8.4% / 7.1%**; five-year 13.8%, 14.7%, 11.7%, 8.4%, 7.1% | 2021-25 | 10-K FY2025 `0001104659-26-020651` (XBRL, flagged) |
| **Ryerson Holding** (RYI) | **4.5% / 0.7% / −0.7%**; 2021 9.6%, 2022 9.2% | 2021-25 | 10-K FY2025 `0001193125-26-062397` (XBRL, flagged) |
| **Olympic Steel** (ZEUS; flat-rolled processor and service center) | **5.2% / 3.6% / 2.5%** (2022-2024) | 2022-24 | 10-K FY2024 `0001437749-25-004742` and FY2023 `0001437749-24-005372`, statements of operations read. **No FY2025 10-K: a Form 15-12G deregistration was filed 2026-02-23 (`0001193125-26-063593`); why it deregistered was not read.** |
| **Klöckner & Co** (now 61.87% WS) | **−0.3%** (2024: operating result −€19.9M on sales €6,632.2M) / **0.5%** (2025: €30.9M on €6,380.2M); net loss −€175.6M (2024), −€53.4M (2025) | 2024-25 | EX-99.1 to 8-K/A `0001193125-26-356964`, PwC audit report dated 2026-08-10 |

- **Peers named: 4 filers plus Klöckner, of roughly ten real competitors** (the registrant names none; the others I
  can name are private or foreign: Steel Technologies (Mitsui), Samuel, Majestic, Heidtman, Russel Metals on
  SEDAR+, and the mills' own processing lines). **Not obtained**: the private processors (no filings) and Russel
  Metals (not an SEC registrant; rung not attempted). **The verdict does not rest on the row.**
- **What the row shows, with its limit [E3-61]:** WS sits **mid-pack, below the leader by roughly half** (Reliance
  7.1-14.7% against WS 3.3-5.7% in comparable years), level with Olympic Steel, above Ryerson in the last two years,
  and far above Klöckner, which is now two thirds of it. **[E2-58]'s exception is "a cost advantage that is both
  wide and sustainable"; on the filed row, the only candidate for it is Reliance, not WS.** The row shows position,
  not conduct.

### THE OTHER Q2 TESTS
- **[E2-44] characteristic (1)**, raising prices *"even when product demand is flat and capacity is not fully
  utilized"*: fails. Prices follow HRC (up 3% against HRC up 21% in FY2026; down 6% in FY2025) and pass-through of
  rises is *"competitive conditions"*-dependent in every filing.
- **[E3-46]**, returns on capital over time: net earnings attributable over average controlling equity **20.1%
  (FY2022, on a carve-out equity base swollen by parent funding of Tempel), 8.1%, 15.4%, 10.7%, 0.8% (FY2026)**, my
  arithmetic from the equity statements; tracking the HRC cycle, not rising.
- **[E4-37]**, the prayer session: the registrant's own sentence is the prayer, *"competitive conditions may impact
  how much of the price increases we can pass on"*, repeated every year.
- **Untapped pricing power [E3-33, E5-28]**: no. Claiming it is claiming near-monopoly in a market the registrant
  calls *"fragmented and highly competitive"*.
- **The attacker's test [E2-45]**: a rival with capital buys a slitting line, a pickle line or a blanking press and
  the automakers' qualification in time; the mills themselves are the rival for the toll leg (*"mill customers ...
  required less outside processing"*).
- **[E3-62]'s second step**: the FY2024-FY2026 capex of $355M went mostly to *"strategic expansions of our electrical
  steel operations in Canada and Mexico"*, the leg whose goodwill was then written off *"due to increased foreign
  competition"*. The gain from better equipment flowed to the customer, as the row predicts in a commodity business.
- **Direction [E4-32]**: tons down, operating margin never back to FY2021-22, the engineered leg impaired, and the
  business now two thirds a sub-1%-margin distributor. Not widening.
- **Which cause of success [E4-36]**: the FY2021-FY2022 peak is the steel price wave (HRC $869 to $1,588 and back),
  a surfing run **[E3-51]**, not a position.
- Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: **flat to eroding in tons and margin; perimeter
  now mostly a lower-margin distributor**.

### THE STRONGEST EVIDENCE AGAINST THIS VERDICT, stated as its holders would state it [E4-51, E3-47, E4-26]
1. **Share gains where it counts**: *"Shipments to the Detroit Three automakers increased 17% in fiscal 2026 as
   compared to fiscal 2025, which significantly outpaced the reported 2% growth in the Detroit Three automakers
   production"*, *"share gains from new programs"*; direct automotive shipments +14%. Automakers qualify few
   suppliers for exposed and tailor-welded parts.
2. **Leadership claims in the 10-K** (FY2025 wording, repeated in FY2024 and FY2026): *"The Company maintains market leading positions in the North American carbon
   flat-rolled steel and tailor welded blank industries and is one of the largest global producers of electrical
   steel laminations."* The Form 10: *"we believe we are the largest independent tailor welded blank operation in the
   region"*.
3. **Gross margin per ton up from $89 to $112** over six years, and operating income positive in every year before
   the FY2026 charges; a thin but durable processor that has survived 70 years.
4. **Klöckner may be bought near the bottom**: its 2025 operating result is €30.9M on €6.4bn of sales, a trough
   margin in a cyclical distributor; WS paid €11.00, a *"98%"* premium to an undisturbed price that was itself low.

**Answered, not dismissed.** (1) is share won in a year, stated beside volume lost to competition in four other
markets in the same paragraph; share won on price and delivery is not a customer's belief that there is no close
substitute. (2) is the registrant's claim of size, and its own next sentences say the effect of its service and
location on its competitive position *"has not been quantified"*; the largest position in a fragmented market is not
[E2-53]'s dominance. (3) is real and is mix and acquisition; the operating margin it produced was 3.3-5.7%, below
the leader and below the FY2021 level. (4) is a Q5 argument about price, not a Q2 argument about position, and
[E2-37] applies to it exactly: *"a textile company that allocates capital brilliantly within its industry is a
remarkable textile company - but not a remarkable business."* **The evidence is here, and the business fails the
franchise test.**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — **OUT, on the business.** [E3-03] criterion (2) is
  refuted by the registrant's own words (*"Competition is primarily on the basis of price"*; products *"priced
  competitively, primarily based on market factors"*; volume lost *"largely driven by increased competition"*; the
  engineered laminations leg impaired *"due to increased foreign competition"*), and the demonstration clause fails
  on its own filed series (prices follow HRC; returns on equity 0.8-15.4% FY2023-FY2026 tracking the steel cycle;
  operating margin 3.3-5.7% against Reliance's 7.1-14.7%). **This is [E2-58]'s commodity class without its wide and
  sustainable cost exception, and the June 2026 purchase made two thirds of it a distributor earning −0.3% to 0.5%
  on sales.** The file closes here. Q3-Q6 are not opened as gates.

*"Can I name the document that would resolve this?"* Not asked: the verdict is OUT, not a non-IN pending evidence.
Recorded: the first 10-Q with Klöckner consolidated (quarter to 2026-08-31, due in October) will show the combined
margins; it cannot turn a price-competed commodity into a franchise.

---
## MATERIAL BENEATH THE CLOSE — recorded, not governing

*The file closed at Q2, OUT on the business. What follows was gathered for the brief's priors and is recorded the
way the NATH, CAH, MHH and ICFI runs recorded theirs: no verdict box is ticked for Q3-Q6, nothing here reopens Q2,
and nothing here is a clearance.*

### Q3 prompts (no verdict)
- **Weight case, had the gate opened: a GATE.** Daily execution is high: a spread business priced against HRC every
  month is have-to-be-smart-every-day **[E3-38, E3-43]**; and after June 2026 **leverage** is high: $1,400M of new
  secured debt plus Klöckner's own against controlling equity of $1,063.3M at 2026-05-31 **[E3-29]**. Control is not
  the determinant (a buyer of WS shares would be a minority beside John P. McConnell, **33.6%**, 17,134,583 shares,
  DEF 14A 2026 `0001193125-26-352256`; BlackRock 9.8%) **[E1-16]**.
- **[E4-29] FIRES, in the deal announcement and the results release.** The Klöckner release (8-K 2026-01-22, EX-99.1)
  prices the deal in EBITDA and counts unrealised synergies inside the leverage figure: *"The offer price implies an
  enterprise value of $2.4 billion and represents EV / EBITDA multiples 1 of approximately 8.5x based on Kloeckner’s
  TTM EBITDA as of September 30, 2025, and 5.5x considering anticipated run-rate synergies of $150 million."* (the "1"
  is a footnote marker) and *"At closing, Worthington Steel anticipates pro forma net leverage to be in the ~4.0x
  range including synergies."* On the audited figures Klöckner's 2025 operating result was **€30.9M** on €6,380.2M of
  sales, after €119.8M of depreciation and amortization; the depreciation EBITDA deletes is the whole difference
  between a loss-maker and a business **[E5-41]**. The FY2026 results release (8-K 2026-06-25, EX-99.1) reports
  *"Trailing 12 months adjusted EBITDA $ 245.6"* million beside an operating loss.
- **[E4-22] third flag, trumpeted projections, FIRES**: *"$150 million of highly actionable, identified annual
  run-rate synergies"*, *"Expected to be substantially accretive to Worthington Steel’s EPS within the first full
  year of operation"*, *"approximately $9.5 billion of combined revenue while maintaining margins above 7%, including
  synergies"*, and *"Worthington Steel’s goal is to reach net leverage levels below 2.5x within 24 months after
  closing."* **[E3-48]'s remedy** (set past guidance against outturn) cannot yet be run: the first dates fall in
  FY2027-FY2028. Recorded as the yardstick for the next reader.
- **Pay [E4-27]**: the annual bonus for both halves of FY2026 was *"tied to achieving specified levels (threshold,
  target and maximum) of EVA (25% weighting) and Adjusted EPS (75% weighting)"*, and the proxy names Adjusted EPS as
  *"the most important performance measure"* linking pay to performance. A deal announced as *"substantially accretive
  to ... EPS"* is an EPS-accretive purchase paid for in debt at 7.75%: an incentive paid on the metric the deal was
  sold on. **EVA's 25% weight is the counterweight**, and the proxy's EVA definition was not read to its capital
  charge.
- **Capital allocation, the prompts**: (1) **[E5-24]** *"what is smart at one price is dumb at another"*: €11.00 was
  a *"98%"* premium to Klöckner's undisturbed three-month price, for a company with an operating result of −€19.9M
  (2024) and €30.9M (2025) and a net loss both years, bought with 7.750% secured notes and SOFR + 4.00% term loans;
  WS's stake of 61,710,791 shares at €11.00 is **€678.8M, about $787M** at the $668.3M-for-€576.3M rate the 10-K
  implies (my arithmetic), against Klöckner's 2025 operating result of €30.9M. (2) **The previous large purchase was
  written off**: the FY2022 acquisitions ($376.7M, chiefly Tempel) led to the FY2026 impairment of *all* Electrical
  Steel goodwill ($53.8M) and $58.4M of its long-lived assets, while FY2024-FY2026 capex went mostly to expanding
  that same leg. **[E4-39]'s candid post-mortem: no instance found** in the 10-K's impairment discussion beyond the
  cause stated (*"increased foreign competition"*). (3) **[E2-30] behaviour (2)**, acquisitions materialising to soak
  up funds, is the prompt the pair raises; **[E3-40]** (loss of focus) does not fit, because the purchase is inside
  the base business, not away from it. (4) **[E5-33, E2-57]**: Adjusted EBIT excludes the impairments because they
  *"do not occur in the ordinary course of our ongoing business operations"*; the owner-earnings mean below keeps
  every one of them in the cash (impairments are non-cash, and the cash that bought Tempel sits in the FY2022
  acquisitions line, outside owner earnings by construction).
- **Candor [E2-26]**: the MD&A quantifies inventory holding gains and losses every year, states the causes of lost
  volume, and the 10-K says in plain words that the effect of its service and location *"has not been quantified"*.
  That is the half-owner standard met on the question that decided Q2.
- **No integrity matter found** in the documents read (10-K Item 3: *"a dispute relating to the import of steel
  across international borders"*, reasonably possible loss $2.0-4.0M); **no EDGAR full-text sweep for enforcement
  was run**, so this is an absence in the documents read, not a sweep result.
- **[E3-66], jurisdiction**: under the DPLTA the German minority keeps statutory compensation rights (€0.67 a year
  or €11.00 cash, appraisal proceedings that *"may adjudicate higher compensation"*), which stand ahead of WS's own
  claim on Klöckner's profits.

### Q4 prompts: owner earnings the corpus's way [E2-23], every window [E4-25, E4-38]
*OCF − SBC − (c), no net-income proxy. OCF from the filed statements: FY2021-FY2023 from the Form 10's combined
statements (in thousands), FY2024-FY2026 from the 10-Ks; FY2023's $315.0M and FY2026's $201.2M cross-checked to
the XBRL pull and the MD&A. **SBC RESOLVES AND IS COMPLETE**: the cash-flow line "Stock-based compensation" resolves
in 6 of 6 years (FY2021 $10.1M in the carve-out, allocated under the Former Parent's plans; FY2026 $13.9M), and the
note's total, *"pre-tax stock-based compensation expense of $ 13.9 million"*, equals the cash-flow line; the 401(k)
match is cash (*"The Company matches 50 cents per dollar on contributions of the first 4 %"*); no stock-settled bonus
found; SBC is 3-7% of OCF except FY2022 (22%, a year of low OCF), so **[E3-70]**'s grant-value measure moves nothing
material. **(c) is a disclosed guess [E2-09]**, shown three ways: the band from the smaller to the larger of capex
and D&A; and management's own stated figure, *"We estimate our annual maintenance capital needs to be between
approximately $40.0 million and $45.0 million"* (midpoint $42.5M), pre-Klöckner. Steel processing is equipment-heavy
but not [E5-20]'s railroad class: capex ran **below** D&A in FY2021-FY2023 ($28.8-45.5M against $45.0-69.6M) and
above it only in FY2024-FY2026, when the MD&A attributes it to *"strategic expansions of our electrical steel
operations in Canada and Mexico"*. So [E3-44]'s D&A default is the guess, and the band's capex end is conservative.*

| FY | OCF | SBC | capex | D&A | working capital inside OCF | OE low (larger c) | OE high (smaller c) | OE at mgmt $42.5M | paid to NCI |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 152.6 | 10.1 | 28.8 | 45.0 | −72.7 | 97.5 | 113.6 | 99.9 | 10.7 |
| 2022 | 39.5 | 8.7 | 36.4 | 59.5 | **−204.0** | **−28.7** | **−5.6** | −11.7 | 35.2 |
| 2023 | 315.0 | 10.4 | 45.5 | 69.6 | **+139.9** | 235.1 | 259.2 | 262.2 | 20.2 |
| 2024 | 199.5 | 10.3 | 103.4 | 65.3 | −30.4 | 85.8 | 123.9 | 146.7 | 8.8 |
| 2025 | 230.3 | 11.0 | 130.4 | 66.0 | +20.2 | 88.9 | 153.3 | 176.8 | 17.0 |
| 2026 | 201.2 | 13.9 | 121.2 | 84.2 | +28.8 | 66.1 | 103.1 | 144.8 | 6.0 |

*$M. Script `oe.py`, output `oe_out.txt` in the research folder.*

| window | mean owner earnings | yield on $1,807.6M | after payments to noncontrolling interests |
|---|---|---|---|
| 3y FY2024-26 | $80.3M to $126.8M | 4.44-7.01% | $69.7M to $116.2M (3.85-6.43%) |
| **5y FY2022-26 (the corpus default [E2-42])** | **$89.4M to $126.8M** | **4.95-7.01%** | $72.0M to $109.3M (3.98-6.05%) |
| 5y FY2021-25 | $95.7M to $128.9M | 5.29-7.13% | $77.3M to $110.5M (4.28-6.11%) |
| 3y FY2021-23 | $101.3M to $122.4M | 5.60-6.77% | $79.3M to $100.4M (4.38-5.55%) |
| 6y FY2021-26 (every filed year) | $90.8M to $124.6M | 5.02-6.89% | $74.5M to $108.3M (4.12-5.99%) |

- **Where the bottom sits near or below zero: FY2022, minus $28.7M to minus $5.6M (negative)**, when working capital
  absorbed $204.0M as HRC averaged $1,588; **FY2023 then released $139.9M** (receivables +$113.0M, inventories
  +$154.5M, payables −$124.3M). The screen's `wc_note` (payables 39% of FY2023 OCF) and its "early half straddles
  zero" (the −$5.6M is FY2022's high end here) are the same pair, read: **no multi-year window is near zero**; the
  pair nets to about −$64M over two years, and the five-year default carries it.
- **The screen's `spread_caveat` answered**: its $78-127M reproduces ($80.3-126.8M on the three-year window). The
  width here is the band, not the window: (c) moves each window by about $30-65M; the window moves it by about $20M.
- **The noncontrolling interests take a slice before the WS owner**: payments to them averaged $17.4M a year over the
  five-year window (Spartan 48%, TWB 45%, WSCP 37%, Sitem 48%). The WS shareholder's owner earnings are the right-hand
  column, **$72.0M to $109.3M on the five-year default, 3.98-6.05% of the cap**.
- **Distortions named [E4-41, E5-11]**: (1) **inventory holding gains** in the good years (about $75M in FY2021,
  $21.9M in FY2022, $15.2M in FY2026) and losses in the bad ($48.6M FY2023, $10.4M FY2025) sit inside OCF; (2) the
  **$21.4M of Klöckner fees paid in cash** in FY2026 (MD&A) depress FY2026 OCF and are a real cost of the purchase,
  kept in; (3) Serviacero's distributions ($23.5M in FY2026, $12.8M in FY2025) are inside OCF.
- **THE PERIMETER THESE NUMBERS DO NOT COVER**: none of the above includes Klöckner. **Klöckner's own filed cash
  (EX-99.1, audited)**: 2025 operating cash flow **€109.5M** (after €54.7M of interest paid and €28.7M of tax), less
  payments for intangibles and PP&E **€111.9M**, less lease repayments €35.4M = **about −€37.8M**; 2024 continuing
  operations €160.2M less €110.3M less €34.2M = **about €15.7M** (my arithmetic; IFRS places lease principal in
  financing, so it is taken out here). Against that, WS now carries about **$110M a year of new pretax interest**
  ($700M at 7.750% is $54.25M; $700M at SOFR + 4.00% is about $56M at the 4.01% one-month bill of 09/24/2026 as a
  stand-in for SOFR, my arithmetic), less whatever Klöckner debt the proceeds repaid, plus the DPLTA's obligation to
  *"absorb all annual losses"* and pay the minority. **No filed statement combines them**; the pro forma's FY2025
  net earnings attributable to WS were **$(12.4)M**. **This is the [E4-25] case at Q4: the combined owner earnings
  cannot be read from any filed statement until the FY2027 10-K, and on the filed pieces they sit near zero.**
- **Great, good or gruesome [E4-20]**: on the WS perimeter, the good-to-gruesome border: FY2024-FY2026 capex of
  $355M against D&A of $216M went into the laminations leg that was then impaired; returns on controlling equity
  8.1-15.4% FY2023-FY2025 and 0.8% in FY2026. Recorded, not scored.
- **Staying power [E5-11]**: (1) stream: $72-109M a year to the WS owner before June 2026, cyclical, one negative
  year in six; (2) liquid assets: $84.6M of cash at 2026-05-31, the new $550M borrowing-base revolver; (3) near-term
  requirements: none large before 2031-2033 on the new debt, but *"certain funds"* guaranteed for the delisting
  offer, the DPLTA's loss absorption and minority compensation, and the Sitem and Stanzwerk facilities held under a
  **standstill** with UBS to 2028. **Coverage [E2-54]**: pro forma FY2025 interest $158.6M against pro forma operating
  income $204.4M, **1.3 times before capex**; *"comfortably met out of current cash flow net of ample capital
  expenditures"* is not shown on the filed pro forma.
- **Named death, as a signature only: #11 THE PASS-THROUGH, with #6 THE BORROWED BALANCE SHEET as a feature.** A
  processor whose spread follows HRC passes its gains to customers (the laminations capex impaired by foreign
  competition; the FY2021 holding gains gone by FY2023), and in June 2026 it borrowed $1.4bn at 7.75% and SOFR + 4.00%
  to buy control of a distributor earning under 1% on sales and to promise to absorb its losses. **Mechanism, from
  filed figures**: a year like FY2023 (HRC −44%, holding losses $48.6M, WS operating income $120.2M) arriving with
  about $110M of new interest, a Klöckner result like 2024's (−€19.9M operating, −€175.6M net) and the DPLTA in force
  leaves the combined company without earnings for its owners. **Likelihood: a real possibility**, stated in the
  corpus's vocabulary **[E3-24]**. **Not entered in the index's instances column** (file closed at Q2, the PAGP,
  CALM, ICFI, MHH, CAH and NATH precedent). **No new shape.**

### COMPUTATION — NOT A CLEARANCE
*No box, no ranking, no entry language.* The pre-deal five-year owner earnings to the WS owner, **$72.0M to
$109.3M** after payments to noncontrolling interests, are **3.98-6.05% of $1,807.6M**, against the 5.47% sovereign
and below the ~10% floor **[E4-28]**. At the floor with no growth they capitalise to **$720M-$1,093M, about $14-21 a
share**, against **$35.48** quoted; at the 5.47% sovereign with no growth, about $26-39 a share. **Both figures are for
a company that no longer exists**: since June 2026 the WS share also carries 61.87% of Klöckner (bought for about
$787M) and about $1.4bn of new debt, and on Klöckner's filed 2024-2025 cash the purchase adds nothing positive to
owner earnings before the promised $150M of synergies, which are a projection, not a filed figure. **Windage count:
ONE** (the conservative end of the (c) band; no premium in the rate **[E3-42]**). Upside ceiling **[E2-63]**: a
3-6% operating margin business capped by the HRC cycle.

### Q6 — reversal conditions, in words (no alert: the file failed on the business, the QLYS ruling)
The Q2 verdict would reopen on **filed evidence that the combined business prices independently of HRC**: several
years in which operating margin holds at or above Reliance's through a falling-HRC year without inventory holding
gains; **or** the combined company's own target, *"margins above 7%, including synergies"*, met in filed statements
through a down year and held; **or** the Electrical Steel leg earning back its capital against the *"foreign
competition"* that impaired it. **Next dates**: the first 10-Q with Klöckner consolidated (quarter ended 2026-08-31,
due in October 2026); the Klöckner general meeting on the DPLTA (about 2026-10-23); the synergy deadline, the end of
FY2028; the leverage goal, *"below 2.5x within 24 months after closing"* (by June 2028).

---
⛔ **Q5 does not open: Q2 is OUT.** The computation above is headed as the protocol requires and carries no box.

## Q5 — not opened. ## Q6 — not opened as a gate (reversal conditions in words above).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; the file closed at Q2)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 IN rests on the 10-K, the Form 10
      and the Klöckner statements filed with the 8-K/A)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none issued)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none issued; the [E4-04] perimeter close
      was considered and refused because [E3-03] is not passed first)
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026 OCF $201.2M, rebuilt
      from its lines, ties to the statement, the MD&A and XBRL; FY2023 $315.0M ties Form 10 to XBRL)
- [x] Owner earnings on a multi-year mean; every window FY2021-FY2026 published with both (c) ends and management's
      own maintenance figure; the negative year (FY2022) named in dollars and a word (beneath the close)
- [x] Competitor row filled (4 filers plus Klöckner, of roughly ten; private processors and Russel Metals not
      obtained, stated; the verdict does not rest on the row)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (5.47%, Treasury, 09/24/2026; the
      EUR sovereign owed to any future Q5, stated)
- [x] Value stated as a round-number range, not a point estimate (computation only)
- [x] One bar chosen, not both; windage count stated (ONE; no bar applied, Q5 not opened)
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git (claim `0bee3d3`, Step 0 and Q1 `54d8e48`, Q2 `e0ea7e7`, beneath the close `3efc36e`,
      this section and the fold after)

**Brief priors, each tested:**
1. *Spun off from Worthington Industries in December 2023; fiscal years end May 31; pre-spin years only as carve-out
   statements* — **confirmed**: Separation 2023-12-01; the Form 10's combined statements for FY2021-FY2023 carry the
   same figures the FY2024 10-K later restated for FY2022-FY2023, judged one perimeter with its acquisitions named.
2. *The deal_note's Item 1.01 "most likely a credit facility or offering"* — **refuted**: it is the Klöckner DPLTA
   (2026-09-08), the last step of a cross-border takeover in which **WS is the acquirer** (60.86% on 2026-06-03, 61.87%
   on 2026-06-15, about 62% at the delisting offer). The quote is not a spread.
3. *wc_note: accounts payable moved 39% of FY2023 OCF* — **confirmed and read**: payables −$124.3M against $315.0M;
   working capital as a whole released $139.9M in FY2023 after absorbing $204.0M in FY2022.
4. *Do not assume the perimeter is stable* — **confirmed unstable**: Tempel and a blanking business (FY2022,
   $376.7M), Sitem 52% (FY2026), two toll plants out, and Klöckner (two thirds of pro forma sales) three days after
   the last filed year.
5. *Verify SBC resolves and is complete* — **resolves 6 of 6 years and is complete** (note total equals the cash-flow
   line; 401(k) match in cash).
6. *Any live merger or tender for WS* — **none found**; the tender offers in the record are WS's for Klöckner.

**Brief errors found:** none verdict-bearing. The brief's commit trailer (Opus 5) differs from the session's
attribution instruction (Opus 5.5); the brief's trailer was used, as the NATH and CAH runs recorded.

**My own errors caught before commit:** (1) my first XBRL script passed the `(cik, name)` tuple `cik_for()` returns
into `sec_facts()` and failed; fixed to take the first element; (2) my first draft of the holding-gain sentence at Q2
said the Form 10 recorded a $53M fall "in fiscal 2023"; the Form 10 says fiscal 2022 against fiscal 2021, and the
$48.6M holding losses are fiscal 2023's; corrected and quoted before commit; (3) I first attributed the "market
leading positions" quote to the FY2026 10-K, whose extracted text reads *"c arbon"*; re-attributed to the FY2025
10-K's clean wording; (4) two quotes carried straight apostrophes where the release has curly ones; corrected
against the source.

**Tooling defects, reported, not patched:**
1. **`deal_note()` guessed "most likely a credit facility or offering" for an Item 1.01 that is a German domination
   and profit-and-loss transfer agreement**, and, as the NATH run found, **`deal_filings()` counts deal forms only
   after the newest 10-K**: the business combination agreement with its EX-2.1 (8-K `0001193125-26-019521`, filed
   2026-01-22) predates the 10-K of 2026-07-30, so the screen saw one ambiguous 1.01 and no deal. **A second case
   of the same blind spot, this time on the acquirer's side.**
2. **`acq_note` reads the "acquisitions, net of cash acquired" line only through the newest annual statement**, so a
   purchase closed after the year end (Klöckner, about $787M for the stake plus the debt) is invisible, and the
   stake-building sat on a different line ("Purchases of equity securities", $106.2M in FY2026).
3. `run.py`'s "GROWTH THE PRICE ASSUMES" printed −6.6% against the screen's +5.52%; the fixed 2.5% terminal-rate
   definition the NATH run reported, not a new defect.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **Worthington Steel is a steel processor that says it competes *"primarily on the basis of price"*, prices
  *"primarily based on market factors"* and follows HRC; tons fell 14% FY2021-FY2026 through two acquisitions, its
  engineered laminations leg was written off to *"increased foreign competition"*, and its 3.3-5.7% operating margin
  sits at half the leader's. In June 2026 it borrowed $1.4bn to buy 62% of Klöckner & Co, a distributor earning −0.3%
  to 0.5% on sales, which is now two thirds of it. [E2-58]'s commodity class, no wide and sustainable cost exception.**
- **PASS/FAIL: FAIL at Q2 (OUT, ON THE BUSINESS).** Price **$35.48** (2026-09-24 close, aggregator, flagged) ×
  **50,948,146 shares** (10-K cover, accession `0001968487-26-000026`) = cap **$1,807.6M**; sovereign **5.47%** (US
  Treasury, 09/24/2026). Owner earnings on the pre-Klöckner perimeter $80.3-128.9M across every window of three years
  or more and both (c) ends (5y $89.4-126.8M, 4.95-7.01%; $72.0-109.3M to the WS owner after payments to
  noncontrolling interests, 3.98-6.05%); FY2022 negative (−$28.7M to −$5.6M). The combined company has no filed
  owner-earnings record.
- **If UNRESEARCHED — THE WORK ORDER:** n/a.
- **If UNKNOWABLE:** n/a.
