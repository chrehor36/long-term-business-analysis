# Company Run — FLUENCE ENERGY, INC. (FLNC) — 2026-09-12
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Run opened 2026-09-12 from a brief that told this run to read its row as UNLABELLED: the
tier-3 triage had filed FLNC under "NEGATIVE ON EVERY CONSTRUCTION ... the cheapest in the
queue", and the correction of 2026-09-12 records that label as the defect. Every gate is
open. Sovereign, price and share count are re-struck here per operator rule 5; the screen
row's cap was a hand override **frozen at 2026-09-02** and is not used. Research folder:
`Test Runs/_research 2026-09-12 FLNC/` (filing dumps pattern-ignored; the scripts that
fetched them are kept).*

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
- **rate 5.35%** · **date 2026-09-11** · source: **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`daily_treasury_yield_curve` CSV, struck 2026-09-12 via
  `tools/sources.py:sovereign("USD")`, which returned `(5.35, '09/11/2026', 'US Treasury daily
  par yield curve')` — the Treasury rung, **not** the FRED fallback). 2026-09-12 is a Saturday,
  so the 09/11 print is the currently observed rate. The brief quoted 5.35% for 09-11; this
  figure was read fresh, not inherited, and it agrees.
- **Earnings currency: USD, with a real non-USD exposure that does not change the answer.**
  Fluence reports in US dollars and its centralized procurement entity's functional currency
  is the dollar (10-Q Q3 FY2026, Note 18: *"the functional currency of the centralized
  procurement legal entity is the U.S. dollar"*). Revenue by customer location for the nine
  months to 2026-06-30 was **Americas $890.9M (56.0%), APAC $470.0M (29.6%), EMEA $229.0M
  (14.4%)** (Note 4). The non-dollar revenue is hedged back to dollars with forwards
  (notional $263.0M at 2026-06-30, Note 18). **No FX conversion is applied and no ADR ratio
  exists** — FLNC is a Delaware corporation listed on Nasdaq.
- **FX note, not a conversion:** the exposure is an exposure; the quote, the statements and
  the sovereign are all dollars.

**THE SHARE COUNT — THIS IS AN UP-C, AND THE ECONOMIC COUNT IS 184,596,369.**

*Read off the cover, then reasoned from the charter and the LLC agreement as the filings
describe them. `Screens/cover_shares.py` refuses to sum classes on purpose; the summing
below is a judgment and is justified in words.*

- **The cover** of the **Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-05,
  accession `0001868941-26-000029`**: *"As of July 31, 2026, the registrant had
  **143,163,588 shares of Class A common stock** outstanding and **41,432,781 shares of Class
  B-1 common stock** outstanding."*
- **What each class is, in the filing's words.** Fluence Energy, Inc. *"is a holding company
  whose sole material assets are the limited liability company interests (the "LLC
  Interests") in Fluence Energy, LLC. All of our business is conducted through Fluence
  Energy, LLC"* (Note 1). **Class B-1 carries votes and no economics:** *"Shares of our Class
  B-1 common stock are not entitled to receive any distributions or dividends"* (Note 3), and
  *"the shares of our Class B-1 common stock held by AES entitle them to **five votes per
  share**"* (FY2025 10-K, Item 1A). **Each B-1 share is paired with one LLC Interest held by
  AES, redeemable one-for-one:** the LLC Agreement grants the Founders the right *"to have
  their LLC Interests redeemed … [for] newly-issued shares of our Class A common stock on a
  **one-for-one basis** or a cash payment … equal to a volume weighted average market price of
  one share of Class A common stock for each LLC Interest so redeemed"*, and on redemption
  *"such Founder will be required to surrender a share of Class B-1 common stock … which we
  will cancel for no consideration"* (FY2025 10-K Item 1A; 10-Q Note 3). Class B-2: 0 shares
  issued (balance sheet). Preferred: none issued.
- **The charter-level rule, verbatim:** the LLC Agreement *"requires that Fluence Energy, LLC at all times
  maintains (a) a one-to-one ratio between the number of shares of Class A common stock issued and
  outstanding and the number of LLC Interests owned by us and (b) a one-to-one ratio between the aggregate
  number of shares of Class B-1 and Class B-2 common stock issued and outstanding and the number of LLC
  Interests owned by the Founders"* (DEF 14A filed 2026-01-26, `0001140361-26-002380`).
- **So the economic count is Class A + the LLC Interests held outside Fluence, Inc.** — which
  equal the B-1 count one-for-one: **143,163,588 + 41,432,781 = 184,596,369.** That is the
  number of equal economic claims on the operating LLC's equity. **The filing states the
  ratio directly:** *"Controlling Interest Ownership 77.55% · Non-Controlling Interest
  Ownership (AES) 22.45%"* at 2026-06-30 (Note 2), and 143,136,891 ÷ (143,136,891 +
  41,432,781) = **77.55%** on the balance-sheet counts — the arithmetic reproduces the filed
  percentage to the hundredth, which is the check that B-1 maps to LLC units one-for-one.
- **The count moved inside the window this run reads.** On 2026-05-15 AES redeemed
  **10,066,414** LLC Interests for new Class A shares (8-K filed 2026-05-15, accession
  `0001104659-26-062654`, Item 3.02), taking Fluence, Inc.'s interest from 71.81% to 77.55%.
  **The economic total did not change** (51,499,195 + 131,164,365 at 2025-09-30 was
  182,663,560; the rise to 184.6M is option exercises and RSU vesting). An Up-C redemption
  moves a claim from one column to the other; it is not dilution, and it is correctly
  invisible to the economic count.
- **Potential dilution not in the count, named:** 18,738,880 shares underlying the 2030
  Convertible Senior Notes (conversion price ~$21.35, capped call to $28.74, **far out of
  the money at $9.93**); 1,205,058 pre-IPO options at $2.45; 1,649,622 RSUs; 964,545 PSUs;
  623,653 NQSOs (Note 3). In-the-money dilution at this price is the $2.45 options and the
  RSUs/PSUs, about **3.8M shares, 2.1%** — noted, not added, because the SBC subtraction in
  owner earnings is the charge for exactly this class and adding the shares too would count
  it twice.
- **THE TOOL READ THE WRONG CLASS.** `tools/run.py FLNC` printed `shares 51.5M · market cap
  0.51B · share basis: dei cover-page count as of 2025-09-30` — **51,499,195 is the Class B-1
  count**, the non-economic class. The tool's cover-count reader returned the B-1 figure and
  priced Fluence at **28% of its economic count**, a cap 3.6x too low. The hand override on
  the screen row existed because of this; the tool was never fixed. **Recorded as a tooling
  defect**, carried to the fold.

**PRICE AND CAP.**
- **Price $9.93**, close of **2026-09-11** (aggregator via `tools/sources.py:price`,
  **flagged**, operator rule 5 — aggregators for live quotes only).
- **Cap = 184,596,369 × $9.93 = $1,833.0M** (economic, whole-LLC basis).
- **The screen row carried `cap_m 1949`** = the same count at **$10.56 frozen at 2026-09-02**.
  The price fell **6.0% in nine days** and the queue's cap is **$116M (6.3%) high**. The count
  the override used was right; only the price was stale.
- **Context for the quote, not a valuation input:** the aggregator's one-year series runs
  **$7.00 (2025-09-12) → $32.23 (2026-02-03) → $9.69 (2026-09-10)**, and the Founders sold 23.0M
  shares at **$21.00** on 2026-05-12 (8-K Item 8.01). A 4.6x range in five months on a business
  whose owner earnings are the subject of this file. **[E5-29]**: volatility is not risk; it is
  recorded so that no reader mistakes any one print for a considered price.

**THE DEAL NOTE — OPENED. The "2 Item 1.01 filings" are ONE agreement filed twice.**
- **8-K filed 2026-04-03, accession `0001104659-26-039628`**, Item 1.01: *"Amendment Number
  Four to Syndicated Facility Agreement"* — the $500M revolver. It *"(i) extends the 'Trigger
  Date' … from December 31, 2025 to December 31, 2026, (ii) extends the minimum liquidity
  covenant of $150.0 million through December 31, 2026, and (iii) moves the initial test date
  of the 3.50:1.00 consolidated leverage ratio covenant from January 1, 2026 to January 1,
  2027"*; adds a $50.0M cash-collateral requirement above $450.0M of extensions of credit and a
  $150.0M cap on certain investments.
- **8-K/A filed 2026-04-06, accession `0001868941-26-000012`**: *"being filed to correct a
  clerical error in Item 1.01"* — the original read *"a $150.0 aggregate cap"*; the amendment
  reads *"$150.0 million"*. **Same agreement.**
- **What it is:** not a merger, not a share sale. **It is covenant relief** — the second
  consecutive deferral of the leverage-ratio test. That makes it a Q4 fact (staying power,
  strength 3), and it is scored there.
- **No deal-form filing exists** (no DEFM14A, S-4, 425, SC TO-T in the submissions index since
  the 10-K). The 2026-08-05 non-GAAP table does disclose *"$3.8 million for legal and
  consulting fees related to potential strategic transactions"* in the nine months — **a
  prompt, not a deal**; nothing has been filed that makes the quote a spread. Carried to Q6.
- **What the deal note CANNOT see, found by reading the index:** a Form S-3ASR (2026-05-12,
  `0001104659-26-059052`) registering **94,666,665 more Class A shares for resale by selling
  stockholders**, a secondary of 23.0M shares at $21.00 by AES, SPT Holding (Siemens pension
  trust) and Qatar Holding, and two Schedule 13D filings on 2026-05-18/19. **The sponsors are
  sellers.** Scored at Q3.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Anchor annual: Form 10-K, FY ended 2025-09-30, filed 2025-11-25, accession
  `0001868941-25-000081`** (`flnc-20250930.htm`). Read: Item 1 (business, products, supply
  chain, customers, IRA/OBBBA), Item 1A (including the organizational-structure, TRA, Founder
  and controlled-company risks), Item 7 MD&A and key operating metrics, the four statements,
  and the notes on revenue, inventory, debt, commitments and contingencies, related parties,
  SBC, supply chain financing and income taxes.
- **The 10-K series FY2021 → FY2025**, so every owner-earnings year rests on a filed statement:
  FY2021 `0001868941-21-000012` (2021-12-14, the LLC-era 10-K) · FY2022 `0001868941-22-000120`
  (2022-12-14) · FY2023 `0001868941-23-000085` (2023-11-29) · FY2024 `0001868941-24-000070`
  (2024-11-29) and its **10-K/A** `0001104659-25-036111` (2025-04-18) · FY2025 as above.
- **The current perimeter document: Form 10-Q, quarter ended 2026-06-30 (Q3 FY2026), filed
  2026-08-05, accession `0001868941-26-000029`** — read in full: statements, all 20 notes,
  MD&A, Part II. Also fetched for the quarterly walk (each is cited where it is used): 10-Qs for 2026-03-31
  `0001104659-26-056304`, 2025-12-31 `0001868941-26-000005`, 2025-06-30
  `0001868941-25-000076`, 2025-03-31 `0001868941-25-000060`, 2024-12-31
  `0001868941-25-000015`, 2024-06-30 `0001868941-24-000059`, 2024-03-31
  `0001868941-24-000045`, 2023-12-31 `0001868941-24-000014`.
- **Six 8-K EX-99.1 earnings releases** (FY23 Q4, FY24 Q4, FY25 Q4, FY26 Q1, Q2, Q3), fetched
  **before** scoring `[E4-29]` and `[E4-22]`'s third flag, per the standing CGNX instruction.
- **DEF 14A filed 2026-01-26, accession `0001140361-26-002380`**, fetched for related-person
  transactions and pay metrics. **8-K 2026-09-01** (`0001868941-26-000037`, Siemens director
  designation). **8-K 2026-05-15** (AES redemption and secondary). **S-3ASR 2026-05-12.**
- **Figure cross-checked against the filed statement:** *Net cash (used in) provided by
  operating activities*, FY2025 Consolidated Statements of Cash Flows, **$(145,538) thousand**
  — agrees with XBRL `NetCashProvidedByUsedInOperatingActivities` −145.5M. Checked at four more
  lines in the same filed statement: *Stock-based compensation* **$19,540** (XBRL 19.5),
  *Depreciation and amortization* **$29,343** (XBRL 29.3), *Accounts payable* **$(119,228)**
  (XBRL −119.2), *Deferred revenue* **$361,903**. And FY2024's *Accounts payable* **$370,124**
  against *Net cash provided by operating activities* **$79,685** — 464.5%, which **reproduces
  the screen's `wc_note` of 464%** and names its year: **FY2024**.
- *No ladder rung was blocked. Everything above is SEC EDGAR rung 2; the only aggregator
  input in the file is the live quote, flagged above.*

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Fluence buys the parts of a
grid battery from other people and sells the assembled system to a power-plant owner on a
fixed-price contract. The parts are battery cells and modules (the majority of the cost),
inverters, enclosures and cooling. **It does not make cells, and it does not own the
factories that assemble its racks**: *"we rely on third party contract manufacturers to
support production across multiple product lines and geographies"* in Utah, Arizona and South
East Asia, and the stated design is to *"maintain a capital light business model"* (FY2025
10-K, Item 1, Manufacturing). What it does own is the system design, the controls software that
runs every system (Fluence OS), the project-management and commissioning capability, and the
contracts.

The contract is the unit. It is priced when signed and delivered twelve to eighteen months
later: *"Our projects have a lead time from date of contract execution to substantial
completion, typically ranging from approximately twelve up to eighteen months"* (10-Q Note 2).
Revenue is booked as cost is incurred (percentage of completion); the customer pays on
milestones; late delivery costs **liquidated damages** that come straight off the price
(*"the contract price is reduced by the expected LD amount"*). So the money is made in the gap
between the price fixed at signing and the cost of cells, inverters, freight, tariffs and
contract-manufacturing labour **as they turn out over the following year and a half**, less any
damages for lateness. After the system is running, Fluence sells a service contract
(maintenance, warranty, capacity augmentation) and a software subscription (Mosaic bidding,
Nispera asset monitoring).

**THE THREE LINES, FILED.** Revenue by line is filed; **cost and gross margin by line are NOT
filed** — Fluence reports one segment and one cost-of-goods line (*"the Company has determined
that it operates in one operating segment"*, Note 1). The BE run could read four matched cost
lines; this file cannot, and says so.

| fiscal year (Sept) | storage solutions $M | services $M | digital $M | total $M | **gross margin, total** | related-party share of revenue |
|---|---|---|---|---|---|---|
| FY2020 | 556.7 | 3.8 | — | 561.3 | **1.4%** | n/r |
| FY2021 | 673.8 | 5.7 / 6.1† | 1.0 | 680.8 | **−10.2%** | 12.7% |
| FY2022 | 1,180.1 | 15.9 / 16.0† | 2.5 | 1,198.6 | **−5.2%** | 53.9% |
| FY2023 | 2,197.6 | 16.0 | 4.4 | 2,218.0 | **6.4%** | 29.5% |
| FY2024 | 2,648.0 | 45.4 | 5.2 | 2,698.6 | **12.6%** | 40.7% |
| FY2025 | 2,172.4 | 84.4 | 6.0 | 2,262.8 | **13.1%** | 24.6% |
| 9M FY2026 | 1,511.8 | 72.0 | 6.2 | 1,590.0 | **6.5%** (Q3 alone **5.1%**) | 17.1% |

*Sources: revenue-disaggregation notes of the FY2022, FY2023 and FY2025 10-Ks and the Q3 FY2026
10-Q; gross profit and related-party revenue off the filed statements of operations.
† the FY2022 10-K and FY2023 10-K print slightly different services figures for FY2021-22
(5,706 vs 6,060; 15,912 vs 16,038, with an "Other" line absorbed) — a reclassification, recorded
not smoothed.*

**What the table says in one line: six fiscal years, a best gross margin of 13.1%, and the most
recent quarter at 5.1%.** Services and software together were **4.0% of revenue in FY2025**. This
is a hardware-integration business with a small annuity attached, not a software business with
hardware attached — whatever the bull case calls it.

**THE UNIT SERIES — [E4-55] RUN.** Fluence files a real physical series: cumulative **GWh
deployed** (systems at substantial completion), contracted backlog in GW, pipeline in GW and
GWh, and order intake in GW (MD&A Key Operating Metrics, every 10-K since FY2022; FY2021 in MW).

| at fiscal year end | deployed GWh (cumulative) | deployed in year, GWh | contracted backlog, storage (GW) | order intake, storage (GW) | backlog $bn |
|---|---|---|---|---|---|
| FY2021 | 2.2 | — | 2.7 | 1.3 | — |
| FY2022 | 5.0 | 2.8 | 3.7 | 1.9 | — |
| FY2023 | 7.2 | 2.2 | 4.6 | 2.2 | 2.9 |
| FY2024 | 12.8 | 5.6 | 7.5 | 5.2 | 4.5 |
| FY2025 | 17.8 | 5.0 | 9.1 | **3.4** | 5.3 |
| 2026-06-30 (9M) | 19.3 | **1.5** | 12.6 | 4.2 (9M) | 6.4 |

*FY2021 figures from the FY2021 10-K (MW: 2,679 MW backlog, 1,311 MW contracted) and the FY2022
10-K comparative (2.2 GWh). Backlog dollars from the EX-99.1 releases and the 10-Q RPO note.*

**Two things the unit series shows that dollar revenue hides.** First, **units deployed fell in
FY2025 (5.0 GWh against 5.6)** while backlog rose — the company was contracted but could not
deliver, which the FY2025 MD&A attributes to *"delays in fulfilling certain projects in the U.S.
due to tariff uncertainties"* and *"delays due to our contract manufacturer scaling newly
commissioned U.S. production facility in Arizona."* Second, **nine months of FY2026 deployed 1.5
GWh against $1.59bn of revenue** — revenue is booked as cost goes in, units count only at
completion, and the Q3 FY2026 release says *"$400.0 million in project deliveries will be delayed
into fiscal 2027 due to production issues at a new international contract manufacturing facility
and construction related delays"* at a new U.S. one. **The physical series is the honest one
[E4-55] and here it says: the bottleneck is Fluence's ability to get contracted systems out of
other people's factories, not demand.**

**THE PRICE-PER-KWH AGAINST COST-PER-KWH TEST — the BE test, run on Fluence.** BE's filed
cost-per-kW series showed the customer taking 104% of the cost curve. Fluence files no
price-per-kWh or cost-per-kWh series, so it is constructed here, and **its limit is stated first:
revenue is recognised on percentage of completion while GWh count at substantial completion, so a
single year's ratio is meaningless** (9M FY2026 would print over $1,000/kWh). Two-year windows
damp the timing mismatch; they do not remove it, and cost of goods includes the small services
cost. *COMPUTATION on filed figures, arithmetic only:*

| window | GWh deployed | total revenue / kWh | cost of goods / kWh | gross profit / kWh | gross margin |
|---|---|---|---|---|---|
| FY2022 + FY2023 | 5.0 | **$683** | **$668** | **$16** | 2.3% |
| FY2024 + FY2025 | 10.6 | **$468** | **$408** | **$60** | 12.8% |
| change | | **−$215** | **−$260** | **+$44** | |

**On this construction the customer took ~83% of the cost decline and Fluence kept ~17%** — better
than BE's 104%, and it is the whole of the margin improvement from 2% to 13%. **But the filing
states the mechanism in words, and the words are the stronger evidence than the arithmetic:**

- **When cell costs fall, price falls.** FY2025 revenue fell $435.7M, *"mainly attributable to a
  $475.7 million decrease in revenue from our energy storage solutions which was primarily driven
  by **lower average price per GWh** of our newer Gridstack Pro solutions projects **as the cost of
  lithium-ion batteries has continued to decline** ... while the total volume of solutions
  projects fulfilled was relatively consistent year over year"* (FY2025 10-K MD&A). And the
  business description: revenue is affected by *"changes in price, which is **primarily dependent
  on the cost of lithium-ion energy storage hardware**"* (10-Q MD&A).
- **When cell costs rise, Fluence pays.** FY2022: cost of goods rose *"as a result of **higher
  battery module prices passed on to us from our supplier**"* (FY2022 10-K MD&A), and the
  supplier *"sought to renegotiate the price we were to pay for battery modules purchased in
  calendar year 2022 as well as those expected to be purchased during the remainder of calendar
  year 2022 and calendar year 2023"* (FY2023 10-K, "Negotiations with our Largest Battery Module
  Vendor") — the year the gross margin was −5.2%. **9M FY2026**: *"increased estimated total
  contract costs on certain projects **due to increases in battery prices**"* (10-Q MD&A), with the
  MD&A noting *"an increase in prices of lithium carbonate and other commodities since December
  2025"* — the half the gross margin fell to 6.5%.

**So the cost curve is asymmetric for the integrator, and in the wrong direction [E3-62]:** a fall
is passed through in price, a rise on a signed fixed-price contract is absorbed. *"How much is
going to stay home and how much is just going to flow through to the customer"* — on the filed
record, most of the down-move flows to the customer and most of the up-move stays home. The
company says it plainly: *"We do not currently hedge against changes in the price of raw materials
as we do not directly purchase raw materials; instead, we buy the components ... and **we rely on
our suppliers to hedge** the underlying raw materials."*

**The scarce input this business controls.** Tested against each candidate:
- **Cells — no.** Bought from *"a mix of Tier 1 global manufacturers"*; the largest supplier
  repriced a signed agreement in 2022; the company lent a cell supplier $30.0M in May 2026 as a
  *"working capital loan to the supplier in connection with a master supply agreement for the
  purchase of battery cells"* (10-Q Note 6(b)). A buyer who has to finance its supplier does not
  control that input.
- **Manufacturing — no.** Contracted; and the contract manufacturers are the current bottleneck.
- **Controls software and system design — partly.** 165+ granted patents, Fluence OS in every
  system, 22.8 GW of digital assets under management. Real, but the controls stack is a feature of
  every competitor's system too (Tesla's Autobidder is named in Tesla's own 10-K).
- **Bankability — the strongest candidate, and it is borrowed.** Customers finance these projects
  and want a counterparty whose performance guarantees are good for ten-plus years. Fluence's are
  partly backed by its sponsors: *"the Company has outstanding performance guarantees issued ...
  by AES and Siemens Industry and their respective affiliates that guarantee Fluence's performance
  obligations with certain Fluence customers"* (10-Q MD&A, Credit Support and Reimbursement
  Agreement), and the 10-K risk factor says *"Any perceived loss of our Founders' scale, capital
  base, and financial strength, or any actual loss or reduction in the Founders' ownership ... may
  prompt business partners to reprice, modify, or terminate their relationships with us."* **The
  scarce input is the sponsors' balance sheets, lent — and the sponsors sold 23.0M shares in May
  2026.**
- **A U.S. domestic-content supply chain — yes, currently, and it belongs to a statute.** *"we
  expect that U.S. policies favoring domestic companies, such as the OBBBA and IRA, will continue to
  further enhance our competitive position in the U.S. market"* (FY2025 10-K, Competition). Scored
  at Q2 under [E2-59].

**Will the fundamentals look broadly the same in ten years?** The *economic structure* probably
will: an integrator standing between cell makers and power-plant owners, paid a thin spread,
carrying fixed-price execution risk. The *product* will not — Gen6 Gridstack, then Gridstack Pro
(*"our recently launched Gridstack Pro product"*, FY2023 Q4 release, 2023-11-28), then Smartstack (announced FY2025, *"a revolutionary split architecture
design"*), with the current quarter's overruns *"primarily related to deployment of newer solutions
offerings."* Three platforms in roughly five years is [E3-31]'s *"subject to constant change"* at
the product level. **That is not a failure to understand how the money is made; it is a finding
about whether the position lasts, and it is carried to Q2 under [E4-04].**

**The five-minute test [E4-46].** Can the unit economics be stated without months of study? Yes:
fixed price at signing, pass-through cost of bought-in cells, milestone billing, damages for
lateness, a thin spread, a small service tail. Nothing here needs a battery chemist. **The
understanding gate is not where this file turns, and inventing an UNKNOWABLE here would dignify a
Q2 finding as a Q1 one** — the error [E3-47] rates most expensive runs the other way, and this run
has named what it understands.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *IN on understanding, with no "provisional" attached: the unit economics are stated from the
  filing, the unit series and the price/cost test are built, and the one thing not filed (gross
  margin by line) is named as absent rather than guessed. What Q1 found that governs later — no
  owned scarce input, an asymmetric cost curve, borrowed bankability, a statutory domestic-content
  advantage, a product replaced every two years — is carried to Q2.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] · no close substitute [ ] · not price-regulated [x]
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]** —
  **the product platform is replaced every two to three years, and the bankability that wins
  contracts is lent by the sponsors.** Detail below.
- Primary moat metric, filing-sourced, and its trend: **gross margin on hardware sold at a fixed
  price, against the vertically integrated competitor's gross margin on the same product class,
  and the direction of both.** Fluence 2.3% (FY22-23) → 12.8% (FY24-25) → **6.5% (9M FY2026)**;
  Tesla energy 18.9% → 26.2% → **29.8%** (2023 → 2025). Narrowing against widening.

*My prior, stated before the evidence and framed to be refuted [E4-26]: OUT on criterion (2).
The bull case is built first and in full, because the analyst writing this has an incentive to
confirm a prior that closes the file early [E4-27], and a file closed wrongly inside the circle
is the error the corpus rates most expensive [E3-47].*

### THE BULL CASE, built as its holders would state it
1. **Bankability is scarce, and the market just proved it.** Grid batteries are financed for
   fifteen to twenty years; the buyer pays deposits up front and depends on the integrator for
   warranties, augmentation and performance guarantees for a decade. When an integrator fails,
   the customer loses real money: **Powin LLC, a battery-storage integrator Fluence itself named as
   a *"principal competitor"* in its FY2022 10-K, filed for Chapter 11 on June 10, 2025**, and
   Ameresco's 10-K discloses *"$26,683 [thousand] in deposits paid to Powin LLC, one of our battery
   energy storage system suppliers, who filed for Chapter 11 bankruptcy protection on June 10,
   2025"* — *"deposits for transactions that never materialized"* (Ameresco 10-K FY2025, filed
   2026-03-03, accession `0001628280-26-013574`). Fluence's guarantees are backed by Siemens and
   AES under the Credit Support and Reimbursement Agreement. **A utility choosing between a
   sponsor-backed integrator and a bankrupt one is not choosing between close substitutes.**
2. **Scale outside China and outside Tesla.** 19.3 GWh deployed, 12.6 GW contracted storage
   backlog, **$6.4bn of backlog, the highest in company history**, Q3 FY2026 order intake of
   *"more than $1.44 billion ... nearly triple"* the prior-year quarter.
3. **A U.S. domestic-content supply chain that Chinese integrators cannot legally copy.** U.S.-made
   cells (AESC, Tennessee — *"a battery supply agreement with AESC, under which Fluence will procure
   U.S. manufactured battery cells"*, FY2023 10-K), modules assembled in Utah, and a claimed
   *"complete U.S. supply chain of modules, cells, inverters, battery pack, enclosures, and thermal
   management systems"* (FY2025 10-K). The OBBBA's Prohibited Foreign Entity rules deny the ITC and
   the AMPC to projects that source too much from PFEs, and the 10-Q says *"our U.S. domestic
   suppliers are in compliance with the new applicable prohibited foreign entity ("PFE")
   restrictions."*
4. **A software and service annuity on the installed base.** ARR of approximately $148.0M at
   FY2025 year-end, guided to $180.0M by FY2026 year-end (EX-99.1 releases); **22.8 GW** of digital
   assets under management (Mosaic, Nispera), **6.3 GW** of services assets under management.
5. **A new demand leg.** *"Secured approximately $850.0 million of data center business through
   July, including the Company's first large, behind-the-meter order ... and approximately $550.0
   million of awards from a hyperscaler in July 2026"* (Q3 FY2026 release).
6. **A captive anchor customer.** AES was **24% of FY2025 revenue** and **13% of backlog**, under an
   *"amended and restated storage core frame purchase agreement ... under preferred purchasing
   conditions"* with exclusivity terms running to October 27, 2028 (FY2025 10-K Item 1A).

**That is the strongest honest case, and none of it is invented.** Now it is attacked.

### THE ATTACK
**(a) Criterion (2), no close substitute — FAILS, on the company's own naming and a rival's.**
- **Fluence names its substitutes, and the list got longer and more Chinese:** FY2021 *"Our
  principal competitors include Tesla and Wartsila"*; FY2022 *"Tesla, Wartsila, and Powin"*; FY2025
  *"Our key competitors currently include, but are not limited to, Tesla, Inc., Wärtsilä, Sungrow,
  and Contemporary Amperex Technology Co., Limited ("CATL")."* **At least one of the four is a battery
  maker integrating forward**, on another registrant's filed description: ESS Tech's FY2025 10-K lists *"sodium-ion
  batteries including those developed by Contemporary Amperex Technology Co."* among its competitors. *(Sungrow's line of
  business is described in no filing read here, and is not characterised.)*
- **A competitor names Fluence as a substitute:** Eos Energy's FY2025 10-K — *"Our Znyth™ battery
  system competes with products from traditional Li-ion battery manufacturers and solution
  providers such as **Fluence Energy**, Panasonic, Samsung Electronics Co. Ltd., LG Chem Ltd., Tesla,
  BYD, Sungrow and Contemporary Amperex Technology Co. Limited"* (Eos 10-K FY2025, filed 2026-02-26,
  accession `0001628280-26-011961`). *EDGAR full-text via `fts_count` with the padded CIK returned 1
  hit for "Fluence" in Eos 10-Ks and 1 in Tesla 10-Ks; the Eos hit was opened and is quoted above;
  the Tesla hit was not located in the FY2025 10-K text on disk and is not relied on.*
- **The customer's own conduct says substitute:** the FY2025 guidance cut of 2025-02-10 cites
  *"customer-driven delays in signing certain contracts that, coupled with **competitive
  pressures**, result in the need to lower our fiscal year 2025 outlook"*, and lowers Adjusted
  EBITDA *"primarily driven by lower expected revenue and **lower expected gross margins on recently
  signed contracts**"* (EX-99.1, Q1 FY2025, accession `0001868941-25-000013`). A buyer who can move
  margin at signing is a buyer with an alternative.

**(b) [E2-44], both halves — FAILS BOTH.**
- *Raise prices when demand is flat and capacity idle?* **The filed mechanism is the reverse: price
  per GWh is set by the cost of cells.** *"lower average price per GWh ... as the cost of lithium-ion
  batteries has continued to decline"* (FY2025 MD&A), while rises on signed contracts are absorbed
  (FY2022 supplier repricing; 9M FY2026 *"increases in battery prices"*). The Q1 price/cost test gave
  the customer ~83% of the cost decline. **There is no untapped pricing power [E3-33]:** claiming it
  would be claiming near-monopoly [E5-28], and the row below refutes that.
- *Grow dollar volume with only minor additional capital?* Revenue went from $561.3M (FY2020) to
  $2,262.8M (FY2025) and **cumulative operating cash over FY2021-FY2025 was −$725.4M, −$1,092.0M
  through 2026-06-30**, funded by a **$935.8M IPO** (FY2022 financing) and **$400.0M of convertible
  notes** (FY2025). Growth here consumed capital. Scored in full at Q4.

**(c) [E4-37], the agony test — the prayer session is on the record.** Three revenue-guidance cuts
and one move to the *"lower end"* across the seven releases from February 2025 to August 2026, one
of them attributing the cut to competition and margin on signed contracts rather than timing.
Detail at Q3 under [E3-48].

**(d) THE COMPONENT SUPPLIER IS THE COMPETITOR — the brief's hypothesis, tested and held.** CATL and
Sungrow are named by Fluence as key competitors, and China is where Fluence's cells come from: *"the
Company imports components from overseas, **including battery cells from China**, into the United
States for customers and projects in the United States"* (FY2025 10-K, Recent U.S. Tariffs). The
filing names no cell supplier except AESC and (historically) Northvolt, so **whether a named
competitor is also a named supplier is not filed** — but the dynamic is described without naming anyone: *"Several competitors, especially those with ties to China, benefit
from vertically integrated supply chains and state support ... This integration has enabled many
Chinese competitors to offer energy storage solutions at prices lower than other market
participants. If Chinese competitors offer lower prices, bid below cost, or operate at sustained
losses, it could negatively affect our pricing flexibility, market share, and overall financial
performance"* (FY2025 10-K, Competition). **An integrator whose largest input is made by its
lowest-priced competitor has its margin set by that competitor.** And the supplier's power is
already filed: the largest module vendor *"sought to renegotiate the price"* of a signed supply
agreement (FY2023 10-K), and in May 2026 Fluence **lent a cell supplier $30.0M** to secure supply
(10-Q Note 6(b)).

**(e) [E2-59] — the U.S. advantage belongs to the regime, and the regime has already moved twice
inside this file's window.** The claimed edge is statutory: *"we expect that U.S. policies favoring
domestic companies, such as the OBBBA and IRA, will continue to further enhance our competitive
position in the U.S. market."* What the filings said when it changed:
- **April-May 2025, tariffs:** guidance cut *"Citing Decisions to Pause Certain U.S. Projects Due to
  Tariff Uncertainty"* — *"mutual decisions made during the second quarter by the Company and its
  customers to pause U.S. projects under existing contracts, and to defer entry into pending
  contracts"* (EX-99.1, Q2 FY2025, accession `0001868941-25-000055`).
- **July 2025, OBBBA:** PFE rules added; the FY2025 10-K said *"certain of our U.S. domestic
  suppliers may be impacted by these new PFE restrictions"*; by the Q3 FY2026 10-Q the company
  *"believe[s]"* they comply, *"subject to Treasury guidance issued on February 12, 2026 and any
  future regulations."*
- **February 2026, the Supreme Court:** IEEPA tariffs invalidated; Fluence filed **$57.0M** of refund
  claims, which offset cost of goods in 9M FY2026 (10-Q MD&A).
- **U.S. share of revenue, filed:** **67.4% (FY2023) → 53.4% (FY2024) → 38.8% (FY2025)**
  ($1,495.0M → $1,442.0M → $877.3M, 10-K Note on revenue by geography).
The 10-K does not quantify how much demand the storage ITC creates; it says only that changes
*"ha[ve] impacted and may in the future impact customer demand."* **Named document that would
quantify it: none found in the filings — so this is carried as exposure, not measured.** What the
record does show is [E2-59]'s mechanism exactly: *"administered pricing ... can floor a commodity
business's profits"* — and even the floor is thin: the **$18.9M** of Section 45X AMPC credited to cost
of goods in 9M FY2026 (10-Q Note 2) and the IEEPA refunds sit inside a **$102.9M** nine-month gross
profit. **Remove the regime's contributions and the nine-month gross margin is lower than 6.5%.**

**(f) [E4-04] and the scope rule — the moat's BASIS is replaced, not defended.** Gen6 Gridstack →
Gridstack Pro (*"our recently launched Gridstack Pro product"*, release of 2023-11-28) → Smartstack
(*"Announced during fiscal year 2025"*), and 9M FY2026 gross profit fell on *"cost overruns primarily
related to deployment of newer solutions offerings."* The test the framework sets: *does the spending
defend the same advantage, or buy its replacement?* Each platform is a replacement; the prior one's
margin does not carry forward. This is Munger's competitive destruction [E3-51], and the record's
best run — FY2024-25 — reads as a **surfing run on the post-2023 storage wave** [E4-36] (cause four,
wave-riding), which is not ownable.

**(g) The bankability moat is BORROWED, and the lenders are leaving.** Item 1 of the bull case is
real, but it is the sponsors' credit. *"Any perceived loss of our Founders' scale, capital base, and
financial strength, or any actual loss or reduction in the Founders' ownership ... may prompt
business partners to reprice, modify, or terminate their relationships with us"* (FY2025 10-K). In
May 2026 AES, Siemens' pension trust (SPT Holding) and Qatar Holding **sold 23.0M shares at $21.00**
and registered **94,666,665 more for resale** (8-K 2026-05-15; 10-Q MD&A, Shelf Registration). The
AES frame agreement ends *"the earlier of (x) October 27, 2028 and (y) the date on which AES Grid
Stability holds less than 10% of the then outstanding voting power."* **[E4-23] applied to a
sponsor instead of a surgeon: a moat that goes when the guarantor goes is not the business's moat.
Recorded here as a moat defect, as the framework requires, not at Q3.**

**(h) [E3-46] — the second question about the business is a number, and it is negative.**
Cumulative owner earnings FY2021-FY2025 are below zero in four of five years (Q4). There is no
"very high return on capital employed over time" to defend.

**(i) [E2-58], the commodity end.** *"persistent over-capacity without administered prices (or
costs) equals poor profitability."* The domestic peers without manufacturing scale are the evidence:
Stem **exited** battery hardware (below), Powin went bankrupt, Eos and ESS lose money on every unit.
Fluence survives on sponsor credit and a statutory floor — the two things [E2-58] and [E2-59] say do
not make a franchise.

### THE COMPETITOR ROW — required [E3-28]

**Metric:** gross margin on energy-storage hardware/systems, and scale in GWh deployed, same window
within one quarter (Fluence's fiscal year ends September; peers' December).

| Company | gross margin, latest full year | trend | scale (latest year) | source |
|---|---|---|---|---|
| **Fluence (FLNC)** | **13.1%** (FY Sep-2025) | 6.4% → 12.6% → 13.1% → **6.5% (9M FY26)** | **5.0 GWh** deployed; revenue $2,262.8M | 10-K FY2025 `0001868941-25-000081`; 10-Q `0001868941-26-000029` |
| **Tesla (TSLA) — energy generation & storage segment** | **29.8%** (CY2025) | 18.9% → 26.2% → 29.8% | **46.7 GWh** deployed (CY2025); **22.3 GWh in H1 2026**; segment revenue $12,771M | 10-K FY2025 `0001628280-26-003952`; 10-Q Q2 2026 `0001628280-26-049270` |
| **Stem (STEM)** | 38.4% total (CY2025) **after exiting hardware**; battery hardware line **−2.2%** in CY2023 ($399.0M revenue, $407.6M cost) | hardware revenue $399.0M → $76.8M → $68.6M | software/services pivot | 10-K FY2025 `0001758766-26-000016` |
| **Eos (EOSE)** | **−126%** (CY2025: revenue $114.2M, gross loss $143.8M) | gross loss widening in dollars | zinc long-duration; names Fluence as a substitute | 10-K FY2025 `0001628280-26-011961` |
| **ESS Tech (GWH)** | revenue $1.6M, gross loss $27.7M (CY2025) | *"substantial doubt about our ability to continue as a going concern"* | iron-flow long-duration | 10-K FY2025 `0001819438-26-000012` |
| **Powin (private)** | not filed | **Chapter 11, 2025-06-10** | named by Fluence as a principal competitor in FY2022 | Ameresco 10-K FY2025 `0001628280-26-013574` |
| **AES (AES) — customer and sponsor** | n/a (buyer) | 24% of Fluence FY2025 revenue; 13% of backlog; *"As of December 31, 2025, AES holds a 28.19% economic interest in Fluence"* (22.45% after the May 2026 redemption, per Fluence's 10-Q); equity-method | — | AES 10-K FY2025 `0000874761-26-000063` |
| **Generac (GNRC)** | no storage-segment margin filed | — | residential/C&I PWRcell, not a utility-scale peer | 10-K FY2025 `0001437749-26-004568` — **excluded as a same-metric peer, reason stated** |
| **Wärtsilä, Sungrow, CATL, BYD, LG** | **not pulled** | — | — | **not SEC registrants** (Helsinki, Shenzhen, Hong Kong, Seoul exchange filings) — limit stated below |

**Tesla, the one integrated peer with filed numbers, in per-kWh terms** *(COMPUTATION, and a prompt
not a measurement — Tesla's segment includes solar generation and residential Powerwall, and the
definitions differ)*: CY2025 segment revenue ÷ GWh = **$273/kWh**, cost **$192/kWh**, gross profit
**$81/kWh**, against Fluence FY24-25 **$468 / $408 / $60**. **The integrated rival earns more per kWh
while charging ~40% less per kWh**, and says why in its own MD&A: *"a decrease in average cost per
unit for Megapack and Powerwall from lower raw material costs, lower manufacturing costs for Megapack
in part from the ramp of Shanghai Megafactory"* against *"a decrease in average selling price of
Megapack."* Tesla kept its cost curve because it owns the factory; Fluence rents its factories and
passes its cost curve on.

- Peers named: **12** (Tesla, Stem, Eos, ESS, Powin, AES and Generac individually; Wärtsilä, Sungrow,
  CATL, BYD and LG as a foreign group) of an industry whose real utility-scale competitors, on Fluence's own list, are Tesla,
  Wärtsilä, Sungrow and CATL. **Same-metric filed rows obtained: Tesla, Stem, Eos, ESS (4).**
- **Peers unavailable:** Wärtsilä, Sungrow, CATL and BYD are foreign and file no 10-K; their numbers
  were not pulled. **This does not hold the verdict PROVISIONAL, and the reason is directional:**
  Fluence's own 10-K says those competitors *"offer energy storage solutions at prices lower than
  other market participants"* and may *"bid below cost."* An absent row can only make a lower-cost
  rival look lower-cost; it cannot rescue a moat that the present rows and the company's own words
  already refute. **Can I name the document that would change the verdict? No** — Sungrow's annual
  report could only confirm the attack. The row's limit, per **[E3-61]**: it shows position, not
  conduct; whether Chinese integrators behave like a *"demented Kellogg"* is exactly what Fluence's
  risk factor fears and cannot be read from any row.
- **Untapped pricing power [E3-33]:** none. Price is a function of cell cost; no manager could raise
  the return by raising prices without losing the order.
- **The attacker's test [E2-45]:** with ample capital and skilled people, how would one compete with
  Fluence? **Buy cells from the same suppliers and rent the same contract manufacturers** — which is
  what Powin did, and the entry cost was low enough that Powin existed. The better attack is Tesla's
  and CATL's: **own the cell and the factory, and price below Fluence's cost.** Both are happening.
- **Direction [E4-32]:** **narrowing.** The margin fell from 13.1% to 6.5% in nine months while the
  integrated rival's rose three years running.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: narrowing, against a widening
  integrated rival**
- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  **OUT on [E3-03] criterion (2), named precisely: the customer has close substitutes — named by
  Fluence itself (Tesla, Wärtsilä, Sungrow, CATL), naming Fluence in return (Eos), and priced below
  it (Fluence's own risk factor) — and the proof that the customer treats them as substitutes is in
  the filed price mechanism: price per GWh follows the cost of cells down, and the integrator eats
  cost rises on signed contracts. Compounded by: the scarce inputs (cells, factories, credit) all
  belong to someone else [E2-58]; the U.S. edge belongs to a statute [E2-59]; and the platform is
  replaced every two to three years [E4-04].** *Evidence is in and the business fails the test; this
  is a finding about the business, not about the price.*

---
> ⛔ **THE FILE CLOSES HERE — Q2 OUT, on the business.** Per the hard sequence, Q5 does not open.
> **Q3 and Q4 are RECORDED BELOW, NOT GOVERNING**, at the brief's instruction and per the queue's
> prohibition on skimming a gate: the triage label that filed this name as "the file's work is Q1-Q2"
> is the defect the correction of 2026-09-12 names. Nothing below can reopen Q2 **[E2-37, E3-39]**,
> and nothing below is a clearance.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 on the business. This section is done in full
> because the queue forbids skimming a gate, and because a Q3 read on a sponsor-controlled Up-C is
> evidence the next run of this name will need. **It cannot reopen Q2 [E2-37, E3-39].**

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution** — have-to-be-smart-every-day **[E3-38]**. Every contract is a fixed price
  on bought-in parts delivered eighteen months later through rented factories, with liquidated
  damages for lateness and an estimate-at-completion that decides revenue and margin each quarter.
  The current quarter's gross margin of 5.1% is the product of *"liquidated damages incurred due to
  project delays"*, *"cost overruns primarily related to deployment of newer solutions offerings"*
  and *"increased estimated total contract costs"* — three execution failures in one sentence (10-Q
  MD&A). **Without a franchise the manager is magnified [E3-43]:**
  *"a business, unlike a franchise, can be killed by poor management"* — and Q2 found no franchise.
- [ ] **Control** — a minority Class A holder, no control, can exit **[E1-16]**.
- [ ] **Leverage** — no bank-scale asset leverage **[E3-29]**; the leverage here is operating (a thin
  margin on a large cost base) and is scored at Q4.

**Case declared: GATE, on daily execution.** Were Q3 governing, no price would compensate a failure
here **[E5-35]**.

**Honesty — binary, filings-based [E5-16], each matter dated to when it became PUBLIC:**
- **2024-02-22 — short-seller report.** The Audit Committee's internal investigation *"demonstrated
  that the allegations of wrongdoing contained in the Short Seller Report are without merit"* (FY2025
  10-K). **Open: an SEC formal investigation**, which the company says is *"reviewing the Company's
  revenue recognition practices, a previously-disclosed material weakness in internal controls,
  capitalization of internal-use software costs, as well as certain service contracts with related
  parties"* (FY2025 10-K Item 1A); still *"fully cooperating"* at the 2026-08-05 10-Q.
- **2025-03-11 and 2025-04-15 — securities class actions** (Abramov; Kramer, which also names AES
  Grid Stability and AES). **Dismissed in its entirety, without prejudice, 2026-03-31**, with leave to
  amend (10-Q Note 14).
- **2025-03-25 onward — derivative suits** (Elmajian, Al Amad, Hyung), stayed. **2026-07-21 — Levitan
  v. The AES Corporation et al.**, Delaware Chancery, *"claims for breach of fiduciary duties, unjust
  enrichment, and aiding and abetting breach of fiduciary duties"* against officers, directors *"as
  well as certain other entities"* (10-Q Note 14). The complaint itself is not on EDGAR and was not
  read; the 10-Q gives only the claim types.
- **Finding:** **no integrity disqualifier found in the filings.** Allegations are not findings, and
  [E5-22] cuts both ways: an unresolved SEC inquiry is neither small because no penalty exists nor
  serious because it exists. **But the inquiry's subject is exactly the estimate that produces every
  margin in this file.**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E2-49, E2-57]** — each a prompt to read; what the filing says:
- [x] **weak accounting — a revenue-recognition material weakness in three consecutive annual
  reports.** FY2022: *"a material weakness in the internal control over the revenue recognition
  process and the related inventory has not been fully remediated."* FY2023: *"not remediated as the
  EAC controls did not consistently operate for a sufficient period of time."* FY2024: *"The Company
  did not consistently apply controls in its revenue recognition process related to the evaluation of
  contract terms for purposes of determining their impact on **when costs are included in the measure
  of progress**."* Remediated *"as of December 31, 2024"* (10-Q Q1 FY2025). **Under percentage of
  completion, "when costs are included in the measure of progress" IS when revenue is booked** — the
  [E4-34] fourth question (*"moving revenues or expenses from one reporting period to another"*) is the
  control that failed, and [E2-50]'s scope applies: in an estimate-driven filer the conduct record and
  the estimate history carry the weight. *"There is seldom just one cockroach"*: the SEC inquiry names
  the same area plus capitalised software.
- [x] **unintelligible footnote — the supply-chain-financing note contradicts the company's own
  reconciliation.** Note 17: the SCF program's *"impact ... to the condensed consolidated statements of
  cash flows is **a reduction of cash used in operating activities** of $101.9 million offset by an
  increase in cash provided by financing activities of $77.2 million."* The non-GAAP table then **adds
  the same $101.9M back to operating cash** to reach Free Cash Flow. If the note is literal, the add-back
  double-counts; if the add-back is right, the note is misworded. The balance sheet supports the second
  reading (other current liabilities +$70.1M on the balance sheet against +$10.7M in the operating
  cash-flow line), but **a reader should not have to reconcile a footnote against a press-release table
  to learn which way $101.9M runs.** The same wording appears at Q2 FY2026 ($70.8M).
- [x] **trumpeted projections — a full guidance culture, with a record [E3-48]:**

| guidance for | first given | revenue range | Adj. EBITDA range | revisions | **outturn** |
|---|---|---|---|---|---|
| FY2024 | 2023-11-28 | $2.7-3.3bn | $50-80M | — | **$2,698.6M / $78.1M** (revenue $1.4M below the floor; EBITDA inside) |
| FY2025 | 2024-11-25 | **$3.6-4.4bn** (*"65% ... covered by ... backlog"*) | **$160-200M** | 2025-02-10 → $3.1-3.7bn / $70-100M (*"competitive pressures"*); 2025-05-07 → $2.6-2.8bn / $0-20M (tariff pause); 2025-08-11 revenue *"lower end"* | **$2.26bn / $19.5M** — revenue **$337M below the floor of the twice-cut range**; EBITDA **89% below** the first midpoint |
| FY2026 | 2025-11-24 | **$3.2-3.6bn** (*"85% ... covered by the backlog"*; *"confident in our ability to deliver 50% revenue growth"*) | $40-60M | 2026-02-04 reaffirmed, *"midpoint ... fully covered by orders in backlog"*; 2026-05-06 reaffirmed; **2026-08-05 cut → $2.9-3.1bn / −$30M to +$10M** | pending (9M: $1.59bn, Adj. EBITDA −$90.8M) |

  **The internal budget was higher still:** the 2025 AIP revenue target was **$4.3 billion** and
  Adjusted EBITDA **$190 million**, against actuals of **$2.3 billion and $19 million** (DEF 14A 2026,
  Corporate Scorecard). **Backlog "coverage" has twice failed to convert** (65% covered → 57% of
  midpoint delivered; "fully covered" → cut). On Buffett's stated base rate [E3-48] this is the ordinary
  case, and [E5-30]'s point is that the culture, once started, is a ratchet.
- [ ] **serial share issuance** — **does not fire.** No primary equity sale since the IPO; the 2024
  convertible is debt; Up-C redemptions move claims between columns without adding any. Economic share count
  growth is SBC-only (180.9M at FY2024 → 182.7M at FY2025 → 184.6M at 2026-07-31, about 1% a year). **Named for the next reader:** the S-3ASR of 2026-05-12 lets the
  company itself sell *"Class A common stock, preferred stock ... debt securities, warrants"* at will.
- [x] **EBITDA promotion [E4-29]** — **fires at full strength.** Adjusted EBITDA is the only profit
  line in every guidance; it is **65% of the PSU metric** (*"cumulative Adjusted EBITDA (65% weight)
  and cumulative revenue (35% weight)"*, 10-Q Note 16) and **25% of the annual bonus scorecard** (DEF
  14A); the CODM *"uses gross margin, earnings before interest, taxes, depreciation and amortization
  ("EBITDA") ... to assess performance"* (Note 1). In a business that capitalises software ($14.9M
  FY2025) and whose FCF definition deducts only property and equipment, the metric deletes exactly the
  expense [E5-41] calls reverse float.
- [x] **metric-switching [E2-49]** — **fires twice.** (i) **Free Cash Flow was a headline when
  positive and absent when negative:** FY2024 release, *"Free cash flow ... was approximately $71.6
  million"* and the CFO on *"robust margin expansion and free cash flow"* — the year payables were 464%
  of operating cash; FY2025 release, no free-cash-flow highlight at all. (ii) **Free Cash Flow was
  redefined in the quarter it would have read worst:** FY2023-Q1 FY2026 releases, *"net cash provided by
  (used in) operating activities, less purchase of property and equipment"*; Q2 FY2026 (2026-05-06),
  *"adjusted to exclude purchases made under supply chain financing arrangements"* — adding **$70.8M**
  to a six-month operating cash of −$347.9M. A switch that *follows* deterioration is [E2-49]'s case.
- [x] **the except-for flag [E2-57]** — every miss arrives with an external cause: *"customer-driven
  delays"*, *"tariff uncertainty"*, *"slower than expected production ramp up"*, *"production issues at
  a new international contract manufacturing facility"*. And the FY2025 year-end release led with the
  number still inside a range — *"Our unwavering discipline drove our adjusted EBITDA to the top end of
  our guidance range"* — the same year revenue missed the bottom of its twice-lowered range. Repeated in
  the proxy: adjusted metrics *"both at the top of our guidance range."*
- [ ] **filed-figure tells [E4-30]** — **do not fire.** Cash taxes paid rose (FY2023 $1.2M → FY2024
  $2.7M → FY2025 $19.0M) while pretax income fell; that is profitable foreign subsidiaries under a U.S.
  valuation allowance, the opposite of the tell. Reported growth is anything but smooth.
- [ ] **restructuring charge [E3-53]** — small (FY2025 severance ~$4.5M, excluded from Adjusted
  EBITDA; 9M FY2026 $3.8M *"legal and consulting fees related to potential strategic transactions"*,
  also excluded). Noted, not fired.

**THE CONVERGENCE [E4-52].** Weak accounting in the estimate that makes revenue + a guidance culture
with a miss record + EBITDA as the paid and published yardstick + a yardstick redefined after it turned
+ except-for explanations. **These are not five prompts; they point one way** — toward a narrative
metered in adjusted numbers while the audited ones deteriorate. *This is not a fraud finding
[E2-30]*: the same filings disclose the damages, the overruns, the cyber incident and the covenant
deferral in plain words.

**STEP 3 — THE PRIMARY TEST [E2-01]** — net income on total equity (including non-controlling interest,
the whole LLC), year-end, filed statements:

| FY | net income $M | total equity $M | return |
|---|---|---|---|
| FY2022 | −289.2 | 629.2 | **−46.0%** |
| FY2023 | −104.8 | 556.3 | **−18.8%** |
| FY2024 | +30.4 | 607.1 | **+5.0%** |
| FY2025 | −68.0 | 548.8 | **−12.4%** |
| TTM 2026-06-30 | −112.0 | 431.2 | **−26.0%** |

The equity base was built by a **$935.8M IPO** and has shrunk to $431.2M. **One positive year in five,
at 5%.** [E2-73]'s denominator for judging operators (*"what we pay for a business does not affect the
amount of capital its manager has to work with"*) gives the same answer: there is no goodwill wedge to
speak of ($28.3M).

**The half-owner test [E2-26]:** mixed. **Passes:** the physical unit series is kept and filed every
quarter (no [E2-49] deletion, unlike BE); liquidated damages, cost overruns, battery-price hits, the IEEPA
refund and the 2026 cyber incident are named in plain words; the 2025 AIP paid **0% on every financial
metric** and the 2024-2026 PSUs were **forfeited** by every NEO (*"both financial performance metrics not
meeting threshold performance expectations"*) — *"The Board and Compensation and Human Resources
Committee did not exercise their discretion to adjust any 2025 AIP award payouts"* (DEF 14A). The pay
system bit the managers when the numbers missed; that is the candor case. **Fails:** the SCF footnote;
the FCF headline that appears and vanishes; *"Revenue of $2.3 billion"* in the FY2025 headline for a
filed $2,262.8M against a $2.6bn floor.

**RELATED PARTIES — the Up-C's own Q3 question.** *(The brief's instruction; read closely.)*
- **AES is owner, customer and guarantor at once.** Owner of **22.45%** of the LLC (10-Q Note 2) with
  **five votes per B-1 share**; buyer of **$555.1M** of product in FY2025 (DEF 14A, *"AES Affiliates ...
  Revenue $555,103"* thousand) = 24.5% of revenue, under a frame agreement granting *"preferred
  purchasing conditions"* — **the preference is not quantified in any filing read**; owed Fluence
  **$362.5M** at FY2024 year-end and **$200.7M** at FY2025 year-end in related-party receivables, mostly
  *unbilled* ($270.3M and $174.1M); and paid **guarantee fees** by Fluence *"based on the affiliates'
  weighted-average cost for bank guarantees and their per annum cost with a reasonable markup."* **A
  22.45% owner that buys a quarter of the output on preferred terms captures more of the economics than
  its share** — unquantifiable from the filings, and named as the thing the Levitan complaint's claim
  types (breach of fiduciary duty, unjust enrichment, aiding and abetting, against AES) point at.
- **Siemens is owner and supplier.** 41,432,781 Class A shares (22.45% economic); **$79.8M** of cost of
  goods bought from Siemens affiliates in FY2025 (DEF 14A); three board designation rights while ≥20%
  (8-K 2026-09-01).
- **The sponsors sold.** On 2026-05-15 AES, SPT Holding and Qatar Holding sold 23,000,000 shares at
  $21.00 — **2,867,172 by Qatar** (Qatar's 13D/A of 2026-05-19) and, by arithmetic on the filed counts,
  **10,066,414 each by AES and the Siemens side** (AES's redeemed units; Siemens' Class A holding fell from
  51,499,195 in the FY2025 10-K to 41,432,781 in the 10-Q, Note 15) — Qatar's 13D/A also states its original 13D *"was filed in error and should be disregarded"*) —
  and registered 94,666,665 more. Insiders selling is not an integrity flag; it is information about
  what the best-informed holders think $21 was worth, and the price is now $9.93.
- **The corporate-opportunity waiver:** the charter provides that *"the doctrine of 'corporate
  opportunity' will not apply with respect to any of our Continuing Equity Owners"*, so the sponsors
  *"are not prohibited from operating or investing in compet[ition with] us in the energy storage
  business"* (FY2025 10-K Item 1A).
- **The Tax Receivable Agreement:** Fluence, Inc. pays the Founders **85% of realised tax savings** from
  the basis step-ups on their redemptions. After the May 2026 redemption, *"The redemptions will result
  in future tax savings of $194.2 million. The Founders will be entitled to receive payments ... equaling
  85% of such amount, or $165.1 million"* (10-Q MD&A; it was $137.6M of savings at the FY2025 10-K).
  **Not recognised** except $0.3M paid, *"given the projected inability to fully utilize the related tax
  benefits"*; nonpayment for a specified period *"may constitute a material breach ... resulting in the
  acceleration of payments."* **A claim senior to Class A that exists only if Fluence becomes
  profitable** — carried to Q4's perimeter.

**The institutional imperative — score all four [E2-30]:**
- [ ] resists any change in current direction — no; three product platforms and a U.S. supply chain
  built in four years.
- [x] projects materialise to soak up funds — **weakly:** the $30.0M supplier loan (May 2026) and
  $3.8M of *"potential strategic transactions"* fees in a year of negative operating cash.
- [ ] staff studies to justify the leader's craving — no evidence in the filings.
- [x] peer behaviour imitated — **weakly:** the data-centre pivot and the domestic-content build track
  the whole industry's 2025-26 narrative; not a finding, a prompt.

**Capital allocation — the buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? **No.** Cash $339.3M, a revolver covenant requiring Total
  Liquidity of at least $150.0M through 2026-12-31, and nine-month operating cash of −$366.5M. *"Issuer Purchases of Equity Securities: None."*
- (2) material discount to IV? **Not computed** — Q5 does not open. No buyback, no flag.

**THE GUARDRAIL.**
- [x] Nothing here promotes the name; the pay system's honest zero cannot repair Q2 **[E2-37, E2-38, E3-39]**.
- [x] Great-manager dependence: none claimed. **The dependence is on sponsors, recorded at Q2(g) [E4-23].**
- [x] Is a manager the plan? The Q3 FY2026 release is a plan to *"achieve targeted production levels
  early in fiscal 2027"* — a turnaround of execution, **[E2-36]'s Pygmalion case, not an excisable
  cancer inside an intact franchise.**

- **VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE → the open
  SEC formal investigation into revenue recognition, capitalised software and related-party service
  contracts.** *Asked aloud: can I name the document that would resolve it?* **No document yet exists** —
  the SEC's closing letter or order has not been issued, and the company's own description is all that
  is public. On a daily-execution gate, in an estimate-driven filer with three years of material weakness
  in exactly that estimate, "no disqualifier found" would be written only after that outcome. **No
  integrity finding is made against anyone.** The rationality read — guidance record, EBITDA yardstick,
  FCF redefinition, except-for — is adverse and would size a position to zero on its own **[E3-48,
  E4-52]**; it is a competence-and-candor finding, priced, not refused **[E5-16]**.

## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING** — the file closed at Q2. Done in full per the brief and the queue's
> prohibition; nothing here reopens Q2.

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

*Construction (the framework's CONVENTION, narrowed 2026-08-28): multi-year mean of operating cash flow
less stock compensation, less the (c) guess. Operating cash carries the working-capital increment from
one audited line. Every input below is read off a filed cash-flow statement (FY2023 10-K for FY2021-22,
FY2025 10-K for FY2023-25, 10-Qs for interim); the arithmetic is in `_research .../wc_walk.py`.*

**Owner earnings by year, $M** — (c) low = D&A, (c) high = total capex (property and equipment **plus**
capitalised software, both filed investing lines):

| FY | OCF | SBC | D&A | total capex | **OE, capex end** | **OE, D&A end** |
|---|---|---|---|---|---|---|
| FY2021 | −265.3 | 0.0 | 5.1 | 4.3 | **−270.4** | **−269.6** |
| FY2022 | −282.4 | 44.1 | 7.1 | 7.9 | **−334.4** | **−333.6** |
| FY2023 | −111.9 | 26.9 | 10.7 | 12.2 | **−151.1** | **−149.5** |
| FY2024 | +79.7 | 23.9 | 14.5 | 19.0 | **+36.9** | **+41.3** |
| FY2025 | −145.5 | 19.5 | 29.3 | 29.8 | **−194.9** | **−194.4** |
| TTM to 2026-06-30 | −100.8 | 18.2 | 41.1 | 31.1 | **−160.1** | **−150.1** |

*(The table's max/min takes the larger of D&A and capex as the conservative end in each year; FY2021's
SBC of zero is filed — pre-IPO awards were not probable until the IPO, so the expense landed in FY2022's
$44.1M. The five-year window contains both years and is complete.)*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
- **Short-window mean** (FY2023-FY2025, three years): **−$103.0M to −$100.9M**
- **Long-window mean** (FY2021-FY2025, five years — the corpus default [E2-42]): **−$182.8M to −$181.2M**
- **Four-year** (FY2022-FY2025): −$160.9M to −$159.1M · **TTM**: −$160.1M to −$150.1M
- **Spread, conservative end:** the five-year is **77% more negative** than the three-year.
- **Combined range: −$183M to −$101M.** **Every window and both (c) ends are negative.** The screen's
  `oe_bottom_m −184 | oe_top_m −101` **reproduces** to within $1.2M at the bottom (a vintage difference
  in one D&A line), and `run.py` printed the same −183 / −101.
- *Is that range too wide to conclude?* **No — it is wide, but it does not span zero, so the sign is the
  conclusion.** Unlike BE (whose rebuilt band spanned zero), there is no construction on filed figures
  that produces positive multi-year owner earnings.
- **The one positive year is the distorted year, and it is named:** FY2024's +$79.7M operating cash
  carried **accounts payable +$370.1M (464% of OCF) and accruals +$160.2M**; without supplier credit
  it was **−$450.6M**. The next year the payables unwound (FY2025 AP −$119.2M, accruals −$93.6M).
  **[E4-41] normalises down, and in this file every favourable break points the same way:** FY2023
  carries a **$19.5M** supplier-claim settlement credited to cost; 9M FY2026 carries **$18.9M** of 45X
  credits, IEEPA tariff refunds (claims of $57.0M, $32.0M received), a **$39.4M** sale of receivables
  in operating cash (Note 19) and $3.5M of state tax-refund interest. **Stripping them widens the loss.**
- **The supply-chain-financing sensitivity (Q3's footnote):** if Note 17's words are literal, TTM
  operating cash is **$101.9M too high** and TTM owner earnings are **−$262M to −$252M**. The balance
  sheet supports the gross reading, so the table uses reported OCF; the literal reading is carried as
  the downside, not averaged in.

**Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** D&A is the default **[E3-44, E2-41]**
and this is the case it fits: an asset-light integrator (*"maintain a capital light business model"*)
whose total capex tracks D&A year by year ($29.8M against $29.3M in FY2025). **Not the [E5-20]
exception class.** The band is $0.4-10M wide in any year and **does not move the verdict** — the
number that decides this file is not (c), it is the working-capital line, and [E2-23]'s own
parenthetical puts that increment inside (c) *"if the business requires additional working capital to
maintain its competitive position and unit volume."* **It does:** inventory, supplier advances and
receivables rise with every GWh contracted (inventory $455.0M → $783.0M and advances $126.8M → $226.4M
in nine months of FY2026). **The OCF convention already charges it; no separate judgment is needed and
none is added.**

**Stock compensation subtracted in full [E5-06] — VERIFIED RESOLVED AND COMPLETE.** The brief asked,
because BE's SBC silently resolved to zero and Boeing's sat under an unreached tag.
- **Resolves:** `ShareBasedCompensation` (cash-flow add-back) returns FY2021 0 · FY2022 44,131 · FY2023
  26,920 · FY2024 23,855 · FY2025 19,540 thousand, **undimensioned**, and each agrees to the filed
  cash-flow statement line. `AllocatedShareBasedCompensationExpense` (the P&L charge) also resolves,
  undimensioned: FY2024 23,875, FY2025 19,650 — **$20k and $110k above** the add-back. The max-rule
  difference is immaterial and the table uses the filed add-back.
- **Complete:** the plans are RSUs, PSUs, NQSOs and pre-IPO unit options, all equity-settled; the
  pre-IPO **Phantom Incentive Plan** conveyed *"the right to receive cash or equity"* and has *"no phantom
  unit awards previously issued outstanding"* at FY2025 (10-K Note 18) — any cash settlement ran through
  operating cash, where it is already charged. **No SBC sits under an unreached tag.**
- **[E3-70] market measure:** SBC runs ~$18-20M a year, about **1% of the $1,833M cap** and a tenth of
  the owner-earnings loss. The grant-date/market adjustment cannot change the sign; not computed.

### THE PERIMETER — THE UP-C ITSELF
*The ACMR question in a different legal form: how much of the consolidated owner earnings belongs to the
public shareholder?*

- **The consolidated figures above are the operating LLC's.** Fluence, Inc. owns **77.55%** of it; AES
  owns **22.45%** through LLC Interests paired with non-economic B-1 shares (10-Q Note 2). The LLC Agreement
  *"requires that Fluence Energy, LLC at all times maintains (a) a one-to-one ratio between the number of
  shares of Class A common stock issued and outstanding and the number of LLC Interests owned by us and (b)
  a one-to-one ratio between the aggregate number of shares of Class B-1 and Class B-2 common stock issued
  and outstanding and the number of LLC Interests owned by the Founders"* (DEF 14A 2026, "Maintenance of
  One-to-one Ratio"). **This is the sentence that makes 184,596,369 the economic count.**
- **So the share of consolidated owner earnings belonging to Class A holders is 77.55%** — on the
  range above, **−$142M to −$78M a year attributable to Class A**, **−$0.99 to −$0.55 per economic
  share**. Because the cap is struck on the whole-LLC economic count (184,596,369), the yield is the same
  whether computed on 100% of owner earnings against 100% of the units or 77.55% against Class A's 77.55%.
  **The 22.45% is not a leak from Class A's yield; it is a separate owner of the same pool.**
- **But Class A sits BEHIND two claims AES does not face, both at Fluence, Inc.:**
  1. **Corporate income tax on its allocable share** — the LLC is a partnership; AES is taxed on its
     share in its own hands, Fluence, Inc. at the corporate rate (10-K Item 1A, "we incur income taxes on
     our allocable share").
  2. **The Tax Receivable Agreement** — Fluence, Inc. owes the Founders **85% of the tax it saves** from
     the basis step-ups on their redemptions: **$165.1M** on **$194.2M** of projected savings after the
     May 2026 redemption (10-Q MD&A), up from $137.6M of savings at the FY2025 10-K. It is **unrecorded**
     (*"not probable ... given the projected inability to fully utilize the related tax benefits"*),
     survives the Founders' exit (*"not conditioned upon continued ownership"*), and accelerates on
     prolonged nonpayment. **Today it costs nothing, because there is nothing to shield. It is a claim
     on exactly the success case** — of each dollar of corporate tax Class A's basis step-up saves, 85
     cents goes to AES and Siemens.
- **And the Class A register itself is sponsor-heavy:** Siemens 41,432,781 Class A shares (22.45% of the
  economic count, 10-Q Note 15), Qatar Holding 11,801,103 (6.4%, 13D/A 2026-05-19). **Non-sponsor
  holders own roughly 48.7% of the economics** (184.6M − 41.4M AES units − 41.4M Siemens − 11.8M
  Qatar = ~89.9M) — and hold a minority of the votes against AES's five-vote B-1 shares.

### WHAT OPERATING CASH LOOKS LIKE NET OF PAYABLES AND CUSTOMER DEPOSITS — the brief's first question

**The shape is BA's, running at a thin positive margin, and the operating cash is BE's —
deposit-and-payables-unreadable.** By year, $M, from the filed cash-flow statements ("customer money" =
deferred revenue + deferred revenue with related parties; "supplier credit" = accounts payable +
accruals, which the 10-Q defines as *"milestones not yet invoiced for inventory"*):

| FY | reported OCF | supplier credit Δ | customer money Δ | **OCF net of both** | pre-working-capital cash result* | working capital absorbed |
|---|---|---|---|---|---|---|
| FY2021 | −265.3 | +95.2 | +153.0 | **−513.5** | −116.9 | −148.4 |
| FY2022 | −282.4 | +120.1 | +279.4 | **−681.9** | −204.1 | −78.3 |
| FY2023 | −111.9 | −254.6 | −198.4 | **+341.1** | −64.8 | −47.1 |
| FY2024 | +79.7 | **+530.3** | −82.0 | **−368.6** | +89.0 | −9.4 |
| FY2025 | −145.5 | −212.8 | **+403.6** | **−336.4** | −1.6 | −144.0 |
| 9M FY2026 | −366.5 | +4.1 | **+296.6** | **−667.2** | −94.4 | −272.1 |
| **cumulative** | **−1,092.0** | **+282.3** | **+852.3** | **−2,226.6** | **−392.7** | **−699.2** |

*\*net income plus the filed non-cash add-backs (D&A, SBC, debt-cost amortisation, inventory provision,
deferred tax, loss-contract provisions).*

**Read in words:**
- **Over five and three-quarter years, customers and suppliers lent Fluence $1.13bn of working capital
  — and the business still consumed $1.09bn of cash.** Net of other people's money, it consumed **$2.23bn**.
  The operating result before working capital was **−$392.7M**; the rest was inventory, supplier advances
  and receivables growing faster than deposits and payables could fund them.
- **Quarter by quarter the signal is noise:** FY2025 Q1 operating cash **−$211.2M** with payables
  −$333.6M and customer money +$311.8M; FY2025 Q4 **+$265.7M** on an inventory release of $191.0M and
  customer money of $129.5M; FY2026 Q3 **−$18.6M**, which net of payables (+$105.8M), accruals and
  customer money (+$144.6M) was **−$285.7M**. **No single quarter's operating cash says anything about
  earning power.**
- **Deposits against cash, today:** deferred revenue including related parties **$1,014.0M** against
  **$365.0M** of cash and restricted cash at 2026-06-30. The customer's money is **2.8x** the cash.
- **Which shape: BA's, at a thin positive margin.** Boeing's advances were *"the inverse of float"*
  because they are discharged by building at a negative margin. Fluence's are discharged by building at
  a **5.1% (Q3) to 13.1% (FY2025) gross margin — below the ~$350M a year of operating expense** (9M FY2026:
  R&D $63.4M + S&M $70.6M + G&A $116.8M + D&A $12.0M = $262.8M). **Each deposit dollar costs about 95
  cents of product to discharge and the overhead is paid on top.** Float is money you hold at no cost
  **[E3-52]**; this is money you must turn into a battery that loses money after overhead. **It is not
  float. It is a customer-funded treadmill that must speed up to stand still.**

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · [x] **gruesome** — *"grows rapidly, requires significant capital to engender the
  growth, and then earns little or no money."*
- Evidence: revenue **$561.3M (FY2020) → $2,262.8M (FY2025)**, 4.0x; cumulative operating cash **−$1,092.0M** (FY2021 to 2026-06-30)
  funded by a **$935.8M IPO** and **$400.0M** of convertibles; owner earnings negative in four of five
  years; equity **$629.2M → $431.2M**. [E4-43]'s saving clause — capital-hungry growth can be *"a
  satisfactory investment"* — does not apply, and [E5-40] says why: cash-consuming businesses are
  unattractive *"unless the cash they consume gets to earn a reasonable return"*, and this capital has
  earned a negative one in four of five years.

### Staying power — score all three **[E5-11]**, the worst case **[E2-55]**
- **(1) a large and reliable stream of earnings — NO.** Owner earnings −$183M to −$101M on every window;
  the adjusted metric guided for FY2026 is **−$30M to +$10M**.
- **(2) massive liquid assets — NO, and what exists is partly borrowed.** Cash **$339.3M** + restricted
  **$25.6M** at 2026-06-30, down from $714.6M in nine months. The company's *"total liquidity of
  approximately $863.0 million"* adds revolver availability ($307.0M after $193.0M of letters of credit;
  cash draws capped at $150.0M) and supply-chain-financing capacity — **[E5-39]'s "kindness of strangers",
  counted as liquidity.**
- **(3) no significant near-term cash requirements — NO. This is the one that kills [E5-11].**
  - **Deferred revenue $1,014.0M** to be discharged by delivery at cost; **accounts payable $295.1M;
    accruals $274.9M** (10-Q balance sheet).
  - **Purchase commitments for cells and modules: $1,101.1M in FY2027 and $1,002.3M in FY2028**, with
    **$111.6M and $122.8M** of liquidated damages if volumes are not taken (10-Q Note 14). **Take-or-pay
    on the input whose price is rising, against fixed-price output.**
  - **The revolver's covenants:** minimum Total Liquidity **$150.0M through 2026-12-31**, then **3.50:1
    consolidated leverage from 2027-01-01** — **the first test moved back a year** (from 2026-01-01) by
    the Item 1.01 amendment of 2026-03-31, which also extended the Trigger Date to 2026-12-31 and added a
    $50.0M cash-collateral trigger. With Adjusted EBITDA guided negative at the FY2026 midpoint, a 3.50x
    leverage test is not obviously passable in January 2027 either.
  - **$6.9bn of contingent guarantees, letters of credit and surety bonds** for project performance
    (Note 14), some backstopped by the sponsors.
  - **$400.0M 2.25% convertible notes due 2030-06-15**, conversion price ~$21.35 — **out of the money at
    $9.93, so a cash repayment, not an equity conversion, on today's price.**
- **Leverage, named and quantified [E4-16, E3-29]:** no bank borrowings; $400.0M converts; $93.9M of
  supply-chain-financing obligations (debt in substance, 45-180 day terms); $193.0M of letters of credit.
  **Terms [E3-52]:** the converts are covenant-light and long-dated; the revolver is covenanted and near;
  the deposits carry no covenants but must be performed.
- **Coverage [E2-54]:** interest paid **$14.1M** in nine months (10-Q supplemental). Cash flow net of
  capex, TTM: **−$100.8M − $31.1M = −$131.9M**. **Interest is not covered by current cash flow at all.**
  *"Zip up your wallet."*

### Name the specific way THIS business dies **[E2-27, E3-24]** — and state it as its holders would [E4-51]
- **The mechanism — the treadmill stops.** A fixed-price integrator whose working capital is lent by
  customers (deposits), suppliers (payables, supply-chain finance) and sponsors (guarantees), and whose
  own operating result has never covered its overhead, survives only while **order intake outruns
  delivery**. Two things stop it together: **(i) a margin shock on signed backlog** — cell prices rising
  since December 2025 are already doing this — and **(ii) a slowdown in new orders**, which turns the
  deposit line from a source into a use. **This is exposure, not experience [E4-40]:** the benign
  FY2024-25 run was late in a falling-cell-price cycle, the most favourable input the business can have.
- **Quantified from filed figures:**
  - **Margin:** backlog **$6.4bn**, of which *"approximately 48% to 53%"* recognises in the next twelve
    months = **$3.1-3.4bn**. Each point of gross margin on that is **$31-34M**. At the Q3 FY2026 margin of
    5.1%, gross profit on $3.2bn is ~$163M against ~$350M of annual operating expense: **an operating loss
    of ~$190M a year before any working-capital move.**
  - **Deposits:** customer money was **$312.7M** at 2024-09-30 and is **$1,014.0M** now. A return to the
    FY2024 level is **−$701M** of operating cash against **$365.0M** of cash. **It has happened:** −$198.4M
    in FY2023; −$105.6M in a single quarter (FY2025 Q3). Order intake has also fallen before: storage GW
    contracted **5.2 → 3.4** (FY2024 → FY2025).
  - **Suppliers:** −$242.3M of payables in FY2023; **−$333.6M in one quarter** (FY2025 Q1).
  - **The floor:** the $150.0M liquidity covenant.
  - **Outcome:** a cash call inside two to four quarters of an order slowdown, met by **equity issued under
    the 2026-05-12 S-3ASR at a price near today's**, a sponsor rescue on sponsor terms, or covenant relief a
    third time. **The likeliest permanent loss for a Class A holder is dilution, not bankruptcy** — the
    sponsors' incentives and a 2030 convert maturity make a filing the tail, not the path.
- **The case against this death, stated fairly [E4-51]:** Q3 FY2026 order intake was **$1.44bn**, nearly
  triple the prior-year quarter; **$850.0M** of data-centre orders arrived through July; customer money
  **rose** $296.6M in nine months. **The treadmill is currently accelerating, not stopping**, and the named
  death requires orders to fall. The holders would add that the sponsors have supported the company before
  (credit support, the $100.0M of SCF guarantees) and that the revolver was amended rather than called.
- **Likelihood:** [ ] likely **[x] a real possibility** [ ] a low-level possibility — *real, because both
  triggers have each occurred inside the five-year window, and the margin trigger is occurring now.*
- **THE SURVIVAL SHAPE — THE SIXTH (ACVA's), IN A SEVENTH FORM: THE TREADMILL.** Not ORCL's (contracted
  not to stop), not ARM's (SBC consuming the owners' share — here SBC is ~$20M a year and immaterial), not
  BE's (too little history — five filed years say one thing), not SWK's (a dividend paid by selling the
  business — no dividend). **Closest to BA's** (advances discharged by building at a loss), but BA's cash
  undoes past work. *Added at the fold, 2026-09-13:* the concurrent ACVA run, folded at 00:03 the same
  night, named a **sixth shape, THE BORROWED BALANCE SHEET** — *"liquidity that belongs to the customers
  ... and runs backwards in exactly the downturn"* that hurts the business. **Fluence belongs to that
  shape** (deferred revenue 2.8x cash; the named death is an order slowdown turning deposits into a use),
  **with a difference that changes the arithmetic:** ACV's float is sellers' cash passing through at no
  cost to discharge; **Fluence's deposits carry a performance obligation that costs ~95 cents per dollar to
  discharge before overhead, on fixed-price contracts exposed to the input price.** So the borrowed balance
  sheet here must keep **growing** — new deposits funding the cost of performing the old ones — to stand
  still. **Name: THE TREADMILL** — *a thin-spread fixed-price integrator whose working capital,
  bankability and liquidity are all lent by customers, suppliers and sponsors, and whose survival depends
  on order intake continuing to outrun delivery.* Recorded as the sixth shape's second instance in a
  distinct form, not as a new class, so the register stays countable.

- **VERDICT (recorded, not governing): [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  **Would be OUT on its own:** negative owner earnings on every construction [E2-23], gruesome [E4-20],
  all three strengths failing with the third live [E5-11], and interest uncovered by cash flow [E2-54].
  *Not governing: the file closed at Q2.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT; Q3 is recorded UNKNOWABLE; Q4 is recorded
OUT. The block below is **COMPUTATION — NOT A CLEARANCE** and carries no entry language.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Q2 closed the file. This block exists so that no reader has to guess what the quote implies; it
carries no entry language, ranks nothing, and uses no margin of safety (operator rule 3).*

**THE FLOOR [E4-28].** Not applied — a floor is a test for a positive expectancy, and there is no
positive owner-earnings base on any construction to test.

**1. THE YIELD**
- owner earnings **−$183M to −$101M** ÷ economic cap **$1,833.0M** (184,596,369 × $9.93, 2026-09-11) =
  **−10.0% to −5.5%** · sovereign **5.35%** (US Treasury 30-year, 2026-09-11)
- Against the screen row: `yield_bottom −9.43%` was −$184M on the frozen $1,949M cap; re-struck at today's
  price the bottom is **−10.0%**. **The label "negative on every construction" was factually right for
  FLNC** — unlike BE — **and it was still the wrong thing to tell a run**, because the reasons it is
  negative (the asymmetric cost curve, the borrowed bankability, the treadmill) sit in Q1, Q2 and Q4.

**2. WHAT THE PRICE ALREADY ASSUMES**
- year-1 growth needed to justify the quote: **REFUSED** — a growth rate applied to a negative base is
  not a number [E5-34], and `run.py` correctly refused it.
- **In words instead — what the buyer at $9.93 is paying for.** $1.83bn for the whole LLC, against owner
  earnings that have been negative on every multi-year window. To earn even the ~10% floor on this price
  the LLC would need **about +$183M a year of owner earnings — a swing of roughly $284M from the
  three-year mean**. *(Arithmetic on filed run-rates, not a forecast:)* with operating expense excluding
  D&A of ~$334M a year (9M FY2026 R&D + S&M + G&A, annualised), SBC ~$19M and capex ~$30M, that requires
  **~$566M of annual gross profit with working capital standing still** — **~$4.3bn of revenue at FY2025's
  best-ever 13.1% gross margin, or ~$8.7bn at the nine-month FY2026 margin of 6.5%**, against FY2026 revenue guided at **$2.9-3.1bn**.
  And for the Class A holder specifically, 77.55% of it, then corporate tax, with 85% of the resulting
  basis-step-up savings owed to the Founders under the TRA.
- **What the business has actually done:** the largest gross profit ever filed is **$341.1M (FY2024)**,
  60% of the ~$566M needed — and it came in the year suppliers funded the operating cash. The best gross
  margin ever filed is the 13.1% the arithmetic already assumes. The price is a bet on a revenue base and
  a working-capital behaviour the filed record has never shown together.
- **The corpus base rate on the growth belief [E4-35]:** sustained high growth is a fewer-than-one-in-
  twenty event among the *best* businesses; this one also needs margin expansion against an integrated
  rival whose costs are falling faster.

**3. WHAT YOU ARE PAID**
- return at the current price: **REFUSED on the same ground** — **−15.3 to −10.9 points** is the naive
  subtraction of −10.0% and −5.5% from 5.35%, printed only so that the negative is explicit.

**WHERE CERTAINTY IS PRICED [E3-42]:** not reached — sovereign used bare (5.35%), no premium, no margin.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]:** **not stated.** A range of values on negative owner
earnings would be a projection of a turnaround, which is the artifact the corpus refuses [E3-34, E4-21].
**The ceiling [E2-63] is stated instead:** even the success case is capped *"unless more capital is
continuously invested"* — the treadmill's defining property — and the TRA takes 85 cents of each dollar
of the Class A holder's basis-step-up tax saving.

**Context, not a valuation:** the Founders sold 23.0M shares at **$21.00** on 2026-05-12, 2.1x today's
quote; the one-year range on the aggregator is **$7.00 to $32.23**. **[E5-29]**: volatility is not risk —
here the risk is the negative sign, and it does not move with the quote.

**WHICH BAR?** Neither — **[ ] Normal method [ ] Screamer test**, both closed by the hard sequence.
**Windage count: 0.**

- **VERDICT: not opened — Q2 OUT. Ranking position: none.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Nothing is bought, so nothing is sold, and no price alert is armed.** A name that failed at Q2 failed on
the business; an alert on it would be a category error (the QLYS ruling, 2026-09-07). **What follows are
the refutation conditions, written in advance [E1-02], for whoever reopens this name.**

**What would reverse Q2 OUT — each a filed fact, not a price:**
1. **The price mechanism reverses.** A 10-K or 10-Q MD&A stating that average price per GWh **held or rose
   while cell costs fell**, or that a battery-cost increase on signed contracts was **recovered from
   customers** rather than absorbed. This is the single fact that would falsify criterion (2) as named.
2. **Gross margin on the integrated rival's terms.** Fluence's gross margin sustained at or above
   Tesla's energy-segment margin (29.8% in CY2025) over a multi-year window **[E4-32]** — not one quarter,
   and not flattered by 45X credits or tariff refunds **[E4-41]**. *(A yardstick chosen by this run, not a
   corpus threshold; the corpus's own test is direction, which is currently narrowing.)*
3. **Bankability shown to be Fluence's own.** Sponsor credit support (performance guarantees, the $100.0M
   of SCF guarantees) withdrawn or lapsed **without** customers repricing or order intake falling — the
   proof that the scarce input is not borrowed.
4. **The domestic-content advantage survives a regime change.** U.S. share of revenue and U.S. margins
   holding through a change to the ITC, the PFE rules or tariffs **[E2-59]** — the test that the moat is
   not the statute's.

**What would reverse the recorded Q3 UNKNOWABLE:** the SEC formal investigation closed without action, in a
filed disclosure — and then a real Q3 read, starting from the guidance record [E3-48].

**What would reverse the recorded Q4 OUT:** positive owner earnings on the **five-year** window, not a
payables year; deferred revenue and payables flat or falling while operating cash stays positive (the
treadmill standing still and earning).

**Monitoring dates — for a reader, not triggers:**
- **FY2026 10-K** (fiscal year ends 2026-09-30; last year's was filed 2025-11-25): outturn against the
  cut $2.9-3.1bn guidance; whether the SCF footnote is reworded; the SEC matter.
- **2026-12-31** revolver Trigger Date and end of the $150.0M liquidity covenant period; **2027-01-01**
  first 3.50x leverage test.
- **FY2027 production ramp** — the Q3 FY2026 release's *"steps to achieve targeted production levels
  early in fiscal 2027"*; the $400.0M of deliveries moved into FY2027.
- **2027-2028 cell purchase commitments** ($1,101.1M and $1,002.3M) against cell prices.
- **2028-10-27** end of the AES storage core frame purchase agreement.
- **2030-06-15** convertible maturity ($400.0M).

**The sell rule [E2-28]** — not applicable; nothing held. **The monitoring question [E3-30]:** is the 9M
FY2026 margin collapse (13.1% → 6.5%) an aberrational cycle (new-platform overruns, a battery-price spike)
or a permanent slip? **This file's answer is that the question is moot at Q2**: even the best cycle
(FY2024-25) produced negative owner earnings on every window that contains it.

**Position size:** **zero** — the business failed Q2 **[E3-45]**.

- **VERDICT: not reached — the file closed at Q2. Refutation conditions recorded above; nothing armed.**

---
## SELF-AUDIT
- [x] Questions answered in order; Q2 is the first non-IN and it closes the file; Q3 and Q4 recorded under
      an explicit NOT GOVERNING banner at the brief's instruction; Q5 headed COMPUTATION — NOT A CLEARANCE
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1 IN names the one thing
      not filed (gross margin by line) as absent rather than guessed
- [x] Every UNRESEARCHED verdict names the artifact — **none used**
- [x] Every UNKNOWABLE verdict states what specifically cannot be known — Q3 (recorded): the outcome of the
      SEC formal investigation; the asked-aloud test is answered (no such document exists yet)
- [x] Step 0: the filing was read, with accession numbers; figures cross-checked — FY2025 OCF $(145,538)K,
      SBC $19,540K, D&A $29,343K, AP $(119,228)K against XBRL; FY2024 AP/OCF reproduces the screen's 464%
- [x] Owner earnings on multi-year means; windows stated (3-, 4-, 5-year and TTM); capex band disclosed as a
      judgment; SBC verified resolved and complete; working-capital walk by year and by quarter
- [x] Competitor row filled — 4 same-metric filed rows (Tesla, Stem, Eos, ESS), Powin and AES named, Generac
      excluded with reason, foreign integrators named as unavailable **with the directional reason the
      verdict does not wait on them**
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury), dated 2026-09-11
- [x] Value stated as a range — **not applicable**: no positive base; the refusal is stated with its reason
- [x] One bar chosen, not both — neither opened; windage count 0
- [x] Prices dated; aggregator used for live quotes only and flagged ($9.93, 2026-09-11)
- [x] Run committed to git with a pathspec after each section
- [x] **The share count is the economic count, justified from the LLC Agreement's one-to-one clause** — not the
      Class B-1 count `run.py` read, and not a sum made by habit
- [x] Brief's claims tested, not inherited: the "2 Item 1.01 filings" (one agreement filed twice), the 5.35%
      sovereign (re-struck), the frozen cap (re-struck), the label (read as unlabelled)
- [x] **Self-audit against operator rule 9:** the prior (Q2 OUT) was stated before the evidence, the bull case
      was built first and in full, and the strongest fact against the conclusion is recorded in the register
- [ ] **Not done, named:** the Levitan derivative complaint (Delaware Chancery, not on EDGAR) was not read;
      Wärtsilä, Sungrow and CATL filings were not pulled; the Tesla full-text hit for "Fluence" was not located
      in the FY2025 10-K on disk. None can reverse a Q2 OUT reached on the company's own filed price mechanism.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **Four-verdict line: Q1 IN · Q2 OUT · Q3 UNKNOWABLE (recorded, not governing) · Q4 OUT (recorded, not
  governing) · Q5 not opened (COMPUTATION — NOT A CLEARANCE: yield −10.0% to −5.5%) · Q6 not reached
  (refutation conditions recorded, nothing armed).**
- **One line:** Fluence is an understandable, capital-light integrator of other people's cells whose price
  per GWh follows the cost of cells down while it absorbs cost rises on signed fixed-price contracts, whose
  named substitutes (Tesla, Wärtsilä, Sungrow, CATL) include the integrated rival earning 29.8% to its 13.1%
  and falling to 6.5%, and whose bankability is lent by sponsors who sold at $21 — **OUT at Q2 on [E3-03]
  criterion (2)**; recorded behind it, owner earnings of −$183M to −$101M on every window and
  the sixth survival shape (ACVA's BORROWED BALANCE SHEET) in its fixed-price form, **THE TREADMILL**.
- **PASS/FAIL: FAIL at Q2, on the business.** Price $9.93 × 184,596,369 economic shares = $1,833.0M;
  sovereign 5.35%.
- **THE STRONGEST SINGLE FACT AGAINST THIS CONCLUSION:** **Powin — a competitor Fluence itself named —
  went bankrupt in June 2025 and stranded $26.7M of one customer's deposits (Ameresco 10-K).** In a market
  where the buyer pre-pays and depends on the integrator for a decade of warranties, a sponsor-backed,
  19.3-GWh-deployed integrator may genuinely *not* be a close substitute for a weak one, and the record
  $1.44bn quarter of orders and $850M of data-centre awards after Powin's failure are consistent with
  customers paying for exactly that. **Why it does not reverse the verdict:** the bankability is the
  sponsors', not Fluence's [E4-23]; and the customer's pricing power over Fluence is filed in the price
  mechanism regardless of how safe Fluence is as a counterparty.
- **Priors refuted or modified (operator rule 9):**
  - **The screen label "negative on every construction" was RIGHT for FLNC** (unlike BE) — and still wrong as
    instruction, because every reason it is negative is a Q1/Q2/Q4 finding.
  - **"The customer took the whole cost curve" (the BE analogy) — MODIFIED:** on two-year GWh windows the
    customer took ~83%, not 104%; Fluence kept ~17%, the whole of its move from a 2% to a 13% gross margin.
    The sharper finding was the asymmetry: falls passed on, rises absorbed.
  - **"Two Item 1.01 8-Ks" — REFUTED:** one revolver amendment and its clerical correction.
  - **"Powin (bankrupt — check)" — CONFIRMED** from a filing (Ameresco 10-K), and it turned out to be the
    strongest evidence *for* the bull case, not against it.
  - **"The deposit line is BE's shape or BA's" — BOTH, split by question:** the operating cash is BE's
    (unreadable in any single period); the economics are BA's (advances discharged by building), at a thin
    positive gross margin that does not cover overhead.
  - **"A battery-cell supplier dispute and a cybersecurity/US-content controversy may appear" — PARTLY:** the
    supplier dispute is filed (the largest module vendor repriced a signed agreement in 2022; $19.5M settlement);
    a cybersecurity incident is filed (June-July 2026 social engineering, confidential data taken, *"operations
    were not affected"*); a U.S.-content **controversy** was not found in the filings read — what is filed is
    PFE-compliance uncertainty (*"certain of our U.S. domestic suppliers may be impacted"*, FY2025 10-K; now
    *"believe ... in compliance"*).
- **If UNRESEARCHED — THE WORK ORDER:** none.
- **If UNKNOWABLE:** not the register verdict; the recorded Q3 UNKNOWABLE is the SEC investigation's outcome.
- **The metric-withdrawal prior [E2-49]: FIRED** (Free Cash Flow headlined when positive, absent when
  negative, redefined in Q2 FY2026 to add back supply-chain financing). Tally after ACVA's fold: **ten fires,
  seven failures.**

### TOOLING DEFECTS FOUND
1. **`tools/run.py` priced FLNC on the non-economic class.** `cover_count()` found no `dei` cover count (a
   multi-class cover is dimensioned by class, and companyfacts drops dimensioned facts), fell through to
   `us-gaap:CommonStockSharesOutstanding`, and took its **only undimensioned fact — 51,499,195 at 2025-09-30,
   the Class B-1 comparative in the 10-Q filed 2026-08-05** — printing `shares 51.5M · market cap 0.51B`.
   The docstring says it *"DOES NOT SUM SHARE CLASSES"*; it does not refuse either, and **on an Up-C the one
   class that happens to be undimensioned can be the one with no economics.** Cap 3.6x low. The screen's hand
   override was right; the tool that made it necessary is unchanged. *A prompt for the tool's owner, not a
   fix made here (operator rule 8: the run does not change tooling mid-run).*
2. **`deal_note` counted one agreement twice.** The 8-K of 2026-04-03 and its 8-K/A of 2026-04-06 (a clerical
   correction of the same Item 1.01) both carry item 1.01 in the submissions index; the note printed "2".
3. **`wc_note` sees payables, not customer deposits or supply-chain finance.** It fired correctly on FY2024's
   464%, but the larger line in this file is deferred revenue (+$403.6M FY2025, +$296.6M 9M FY2026), which it
   did not name, and SCF moves operating cash through a line (`Purchases under supply chain financing
   arrangements`) no working-capital tag reaches.
4. **The screen's owner-earnings ends reproduce** (−$182.8M vs `−184`; −$100.9M vs `−101`), the bottom within
   $1.2M — recorded because the last several runs found the ends built from different windows and (c) ends;
   here the bottom is the five-year capex end and the top the three-year D&A end, **the seventh such pair**.

### DEFECTS IN THE BRIEF (every brief contains one; this one's)
1. **"2 8-K Item 1.01 filings" is one revolver amendment filed twice** — the deal note's count, inherited.
2. **"a cybersecurity/US-content controversy may appear"** — the cyber incident is filed (June-July 2026);
   **no U.S.-content controversy was found** in the filings read, only PFE-compliance uncertainty that the
   company now says it has resolved.
3. **"Generac (GNRC)" is not a same-metric peer** — residential and C&I storage, no storage segment margin.
4. **"the customer took 104% of the cost curve" as the BE analogy** — the test ran and gave ~83%; the sharper
   Fluence finding was the asymmetry, which the analogy did not predict.
5. **"five named survival shapes"** — six by the time this run folded (ACVA's, the same night).
