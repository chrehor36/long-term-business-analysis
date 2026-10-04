# Company Run — ACV Auctions Inc. (ACVA) — 2026-09-12

**STATUS: COMPLETE. FAIL at Q2 (OUT, on the business). Q1 IN; Q3 and Q4 recorded, not governing; price headed COMPUTATION — NOT A CLEARANCE; Q6 records refutation conditions. ACV is the subject of a pending $10.50 cash tender by Copart (8-K 2026-09-10).**
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

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
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.35 %** · date **2026-09-11** · source **US Treasury daily par yield curve, 30-year, issuing
  authority** (`home.treasury.gov` daily_treasury_yield_curve CSV, 2026 file, fetched by this run on
  2026-09-12; output `_research 2026-09-12 ACVA/s0_out.txt`). Prior prints in the same file: 09-10 5.37%,
  09-09 5.28%, 09-08 5.25%, 09-04 5.24%. **Struck by this run, not inherited** (the brief's 5.35% is confirmed).
- **Earnings currency: USD, read from the filing.** 10-K FY2025 note 19: *"revenue outside of the United
  States, based on the billing address of the customer, was not material. As of December 31, 2025 and 2024,
  long-lived assets located outside of the United States were not material."* Operations in India and a
  French AI subsidiary (Monk SAS, bought 2022) are cost centres. FX: none. ADR ratio: none — a Delaware
  registrant on the NYSE.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025**, period 2025-12-31, filed **2026-02-23**, accession **0001637873-26-000011**
    (`acva-20251231.htm`) — Item 1, Item 1A (competition, ACV Capital, float and settlement risk), Item 7 MD&A in
    full (key metrics, revenue lines, Tricolor, the marketplace-float paragraph, debt, cash flows), the auditor's
    report and critical audit matter, all primary statements, notes 1, 5, 7, 8, 9, 13, 16, 17, 19.
  - **10-Q Q2 2026**, period 2026-06-30, filed **2026-08-10**, accession **0001637873-26-000034** — cover,
    condensed statements, equity roll-forward (the ASR), MD&A. **10-Q Q1 2026** acc. 0001637873-26-000020 ·
    **10-Q Q2 2025** acc. 0001637873-25-000011.
  - **10-K FY2024** acc. 0001628280-25-006439 · **FY2023** acc. 0000950170-24-018066 · **FY2022** acc.
    0000950170-23-005445 · **FY2021** acc. 0000950170-22-001792 — cash-flow statements (newest vintage of each
    year carried in companyfacts is cross-read against these), business-combination notes, key metrics.
  - **Prospectus 424B4** (IPO, 2021-03-24) acc. 0001193125-21-092803 — FY2019-2020 statements and the pre-IPO
    unit series.
  - **DEF 14A 2026** (filed 2026-04-16) acc. 0001193125-26-158987 · **DEF 14A 2025** acc. 0001193125-25-084378.
  - **8-K EX-99.1 earnings releases:** Q2-2026 acc. 0001637873-26-000031 · Q1-2026 acc. 0001637873-26-000019 ·
    Q4-2025 acc. 0001637873-26-000010 · Q3-2025 acc. 0001637873-25-000019 · Q4-2024 acc. 0001628280-25-006357 ·
    Q4-2023 acc. 0000950170-24-017935 · Q4-2022 acc. 0000950170-23-003752 · Q4-2021 acc. 0000950170-22-001351.
  - **Every 8-K carrying Item 1.01 since 2024** — opened below: 2026-09-10 acc. **0000950103-26-013780** (with
    EX-2.1 merger agreement, EX-10.1 support agreement, EX-99.1 joint release, EX-99.2 Copart investor
    presentation) · 2026-05-13 acc. **0001637873-26-000023** (with EX-10.1 ASR master confirmation) · 2025-12-18
    acc. 0001637873-25-000025 (warehouse amendment) · 2025-07-01 acc. 0001637873-25-000005 (revolver fourth
    amendment) · 2024-06-26 acc. 0001628280-24-030155 (warehouse facility).
- figures cross-checked against the filed statement (three, all exact):
  1. **FY2025 operating cash flow rebuilt from its own detail lines.** Net loss −$66,141k + D&A $43,743k + SBC net
     of capitalised $56,862k + provision for bad debt $34,050k + other non-cash $3,542k = **$72,056k** before
     working capital; working capital: trade receivables −$31,022k, other operating assets −$10,541k, **accounts
     payable +$46,823k**, other operating liabilities +$916k = **+$6,176k**; total **$78,232k**, equal to the filed
     "Net cash provided by (used in) operating activities", the MD&A table, and XBRL
     `NetCashProvidedByUsedInOperatingActivities` 78,232,000.
  2. **Total revenue** = marketplace and service $677,964k + customer assurance $81,642k = **$759,606k**, equal to
     the filed line and to note 19's segment table.
  3. **SBC reconciles across three statements** (note 13): cash-flow add-back "net of amounts capitalized" $56,862k
     + capitalised SBC $7,602k (cash-flow supplemental, non-cash investing) = **$64,464k**, equal to note 13's
     "Stock-based compensation expense". The equity-statement credit ($72,503k) differs, and why is settled at Q4.

**THE PRICE, THE COUNT, AND THE CAP — and the fact the queue row cannot see.**
- **Price $10.41**, close **2026-09-11** (NYSE, via Yahoo chart API — *aggregator used for the live quote only,
  and flagged*, operator rule 5; history kept at `px_history_2y.json`). **09-10 $7.22 on 19.6M shares; 09-11
  $10.41 on 115.4M shares, +44.2% in one session.** Longer context from the same series: $16.22 (2025-06-30), $8.02
  (2025-12-31), **$4.24 (2026-03-31)**, $5.84 (2026-05-12, the ASR date), $7.19 (2026-06-30), **$7.26 (2026-08-10,
  the "unaffected" date named in the merger release)**, $7.26 on 25.7M shares (2026-08-11, the day of the media
  reports).
- **Share count off the cover of the latest periodic filing:** 10-Q for the period ended 2026-06-30, filed
  **2026-08-10**, accession **0001637873-26-000034** — *"As of August 3, 2026, there were 169,807,980 shares of the
  registrant's common stock with a par value of $0.001, outstanding."* **A later count exists and is used: the
  merger agreement's representation (EX-2.1 §4.05), "As of 5:00 p.m., New York City time, on September 8, 2026 …
  there were outstanding (i) 169,824,232 Shares, (ii) no Company Preferred Shares, (iii) 10,359,498 Shares subject
  to outstanding Company Restricted Stock Unit Awards, (iv) 2,364,836 Shares subject to outstanding Company
  Performance Stock Unit Awards (at target levels), (v) 1,126,024 Shares subject to outstanding Company Stock
  Options and (vi) 0 Shares were held by the Company in its treasury."** The two counts differ by 16,252 shares
  (0.01%). One class of common stock since the 2025 charter amendment removed Class B.
- **MARKET CAP = 169,824,232 × $10.41 = $1,767.9M** (on the 10-Q cover count, $1,767.7M). **The queue row carried
  `cap_m 1148` — 35.1% LOW** — and the 2026-09-11 pre-check's $1,226M (169,807,980 × $7.22) was **right at its
  own date and stale one session later**: it used the 09-10 close, struck before the after-hours announcement.
  **This is the twelfth cap check and the tenth to be wrong at the moment of use** — this time not a count error
  and not a price drift but **an event**.
- **THE CAP_FLAG ($1,148M against a $2,700M float), RESOLVED: NEITHER NUMBER WAS WRONG; THE FLAG COMPARED TWO
  DATES** — the ALKT finding, again. The 10-K cover float is *"based on the closing price of the shares of Common
  stock on the New York Stock Exchange on June 30, 2025, was $2.7 billion"*; the close that day was **$16.22**,
  and the cover count nearest (10-Q, 2025-08-04) was 172,107,121, so the cap on the float date was **~$2,792M and
  the float was ~96.7% of it** — a subset, as it should be. The stock then fell 74% to $4.24 by 2026-03-31.
- **Claims ahead of the equity, 2026-06-30** (10-Q balance sheet): **long-term debt $205.0M** (2021 Revolver
  and the ACV Capital warehouse facility; at 2025-12-31 $70.0M revolver + $120.0M warehouse), against cash
  $242.3M. **But the cash is not the company's to count** (Q1 and Q4): accounts payable $410.1M, most of it owed
  to sellers for vehicles, against trade receivables $216.1M, most of it owed by buyers. Stockholders' equity
  $389.9M against goodwill $182.9M and acquired intangibles $75.7M — **tangible equity +$131.4M**, of which
  capitalised software is $87.1M.

### ⚠️ THE DEAL NOTE, OPENED — ACVA IS A PENDING ACQUISITION, BY A COMPETITOR IN THIS FILE'S OWN ROW

- **Item 1.01 #1 — 8-K filed 2026-09-10, acc. 0000950103-26-013780: an Agreement and Plan of Merger with
  COPART, INC.** *"Parent will cause Merger Sub to commence a cash tender offer … to acquire all of ACV's
  outstanding shares of common stock … for $10.50 per share, net to the seller in cash"*. Minimum condition a
  majority of shares; HSR; no financing condition (*"Copart intends to fund the transaction through cash on
  hand"*, EX-99.1); second-step merger under DGCL §251(h). **Termination fees: $57,700,000 payable by ACV** (on a
  superior proposal, among other cases) and **$115,300,000 payable by Copart** on an HSR/competition-law failure.
  **End Date 2027-09-10**, automatically extended **180 days** if only the HSR or competition-law injunction
  condition is outstanding (EX-2.1 §10.01(b)(i)). A **Support Agreement** covers holders of **~4.1%** of the shares.
  **Unvested RSUs, PSUs and options roll into Copart awards** at an Exchange Ratio of $10.50 ÷ the Parent Stock Price.
  Boards unanimous; **close expected by calendar year-end 2026**; ACV to *"operate as an independent subsidiary of
  Copart led by ACV's existing leadership team."* Implied equity value *"approximately $1.9 billion"* — which
  reconciles: (169,824,232 + 10,359,498 + 2,364,836) × $10.50 = **$1,916.8M**, plus in-the-money options.
  Premium stated as *"approximately 45% to ACV's unaffected closing stock price on August 10, 2026"* —
  $10.50 ÷ $7.26 = 1.446, reconciles. **SC TO-C** (Copart, 2026-09-10 and 09-11) and **SC 14D9-C** (ACV, three
  filings 09-10 and 09-11) are on file; **the SC TO-T had not been filed at the time of this run's submissions
  fetch.**
- **At $10.41 the quote is a 0.86% gross spread to $10.50 ($0.09 a share), not an owner-earnings price.** On
  a 2026-12-31 close that is about a 2.9% annualised return; on the 2027-09-10 End Date, about 0.9%; both
  against a 5.35% bond. **This is the ROKU treatment, which the ALKT fold pre-registered: "A definitive merger
  agreement re-opens Step 0, not Q2."** It is recorded here and it changes what the price means at the
  computation, not what the business is at Q1-Q4.
- **Item 1.01 #2 — 8-K filed 2026-05-13, acc. 0001637873-26-000023: an accelerated share repurchase with
  Citibank, $50 million.** *"on May 13, 2026, the Company will make an aggregate payment of $50 million to
  Citibank and expects to receive an initial delivery of approximately 70% of the shares"*. The Q2-2026 equity
  statement records **5,993k shares retired for $50,196k** (the initial delivery), at a 2026-05-12 close of $5.84.
  The initial delivery is ~70% of the notional, so the reference price sits near the $5.84 close (final
  settlement is VWAP-based and was open at 2026-06-30). **ACV bought back 3.5% of its shares for $50M at around $6-8 a
  share four months before agreeing to sell itself at $10.50.** Read at Q3.
- **The acquisitions inside the window, rebuilt from the business-combination notes — the flag's $270M reproduces
  and understates only slightly this time** (full table at Q4): cash $269.5M FY2021-25 (**$64.5M 2021, $18.9M
  2022, $29.6M 2023, $156.5M 2024, $0 2025 — sum $269.5M, the row's $270M**), **plus $8.6M of stock** (639,976
  Class A shares to the Alliance Auto Auctions sellers, 2024-01-30) **plus $2.0M of contingent consideration**
  at fair value (2021, *"based on acquired company performance"*; $1.9M reversed as a gain in 2022), **less
  $14.1M** recovered by selling Indiana Auto Auction's real estate (2024-08-06). **Gross perimeter $280.1M; net
  of the real-estate sale $266.0M.** The investing line understates the gross by 3.8% — the seventh perimeter
  checked, and the first where the understatement is immaterial. **And what was bought is the finding:** Max
  Digital (inventory software, $61.4M, 2021), Monk SAS (AI imaging, $18.6M, 2022), and then **five physical
  auction houses** — the April 2023 and August 2023 acquisitions, Alliance Auto Auctions, 166 Auto Auction, a
  March 2024 business and Indiana Auto Auction — each *"offers wholesale car auction services"*. Read at Q2.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**
When a car dealer takes a trade-in it does not want to retail, it needs to sell it to another dealer, fast.
ACV sends one of its ~800 employed inspectors to the dealer's lot, who photographs the car, records the
engine sound and the underside, and writes a condition report. The car goes into a short online auction
(typically minutes long) open to every registered dealer in the country. **When — and only when — the car
sells, ACV charges the buyer a fee that rises with the sale price and the seller a fixed fee plus the
inspection fee** (10-K FY2025 MD&A: *"Buyer auction fees are variable based on the price of the vehicle, while
seller auction fees include a fixed auction fee and an optional fee for the elective condition report"*). The
price of the car itself is never revenue (*"We act as an agent when facilitating a vehicle auction … reported as
revenue on a net basis"*). Around the auction ACV sells four more things: **it books the truck** to move the car
(recorded gross, as principal, so it looks large and earns little), **it lends the buyer the purchase money**
(floorplan loans through ACV Capital, funded by a bank warehouse line), **it insures the seller** against the
buyer later claiming the report was wrong ("Go Green", a guarantee priced at its fair value), and **it sells
inventory-pricing software and reports** to dealers (ACV MAX, True360).

**FY2025, per car sold (829,276 cars; script `units.py`, output `units_out.txt`; revenue and cost lines from the
10-K MD&A):**

| line | revenue | per car | direct cost | per car | what is left | margin |
|---|---|---|---|---|---|---|
| auction fees | $347.6M | $419 | $68.3M | $82 | $337 | 80.4% |
| transport + finance ("other marketplace") | $295.8M | $357 | $206.9M | $249 | $107 | 30.1% |
| data services | $34.5M | $42 | $12.9M* | $16 | $26 | 62.6% |
| assurance (Go Green, price guarantees) | $81.6M | $98 | $73.3M | $88 | $10 | 10.2% |
| **total** | **$759.6M** | **$916** | | | | |

*\*after a $7.6M one-off class-action settlement credited against data cost of revenue.* Below these lines the
business spends **$182.7M on operations and technology** (inspections, titles, payments, engineering) and **$235.0M
on selling, general and administrative** — **$418M of overhead against ~$393M of line-level contribution** — and
posts a **GAAP operating loss of $63.2M (−8.3%)**, the seventh consecutive operating loss on file (FY2019-FY2025).
**The whole model is: an ~$420 fee on a ~$12,500 car, earned only if it sells, financed by an inspector
workforce paid whether it sells or not.**

**THE CUSTOMER FUNDS — ESTABLISHED FROM THE FILING, AND THE OPPOSITE OF PAY.** The brief asked whether auction
proceeds in transit sit on the balance sheet and inside operating cash. **They do, both.** 10-K FY2025 MD&A,
liquidity: *"We settle transactions among buyers and sellers using the marketplace, and as a result the value of
the vehicles passes through our balance sheet. Because our receivables typically have been, on average, settled
faster than our payables, our cash position at each balance sheet date has been bolstered by marketplace
float."* The buyer's purchase price is a **trade receivable** ($197.2M at 2025-12-31; $216.1M at 2026-06-30), the
amount owed to the seller is **accounts payable** ($390.8M; $410.1M), and both movements run through **operating
cash flow** (MD&A: *"an increase in accounts payable to sellers partially offset by an increase in accounts
receivable from buyers"*). Risk factor list: *"fluctuations in the amount of auction float on our balance sheet."*
**Net float (payables less trade receivables) was $193.6M at 2025-12-31 and $194.0M at 2026-06-30 — 71% and 80%
of the cash on the balance sheet.** Paymentus's customer funds were off balance sheet; ACV's are on it, in the
cash line, and in the operating cash flow. **What operating cash looks like without the line is built at Q4.**

**And one leg of the lending business sits OUTSIDE operating cash.** The growth of the floorplan loan book is an
**investing** outflow (*"Net increase in finance receivables"*, −$75.8M FY2025) funded by the warehouse line in
**financing**, while the **provision for credit losses on those loans is added back inside operating cash**
(*"Provision for bad debt"* +$34.1M FY2025, of which **$31.3M on finance receivables**, note 5, including **$18.7M
for Tricolor**, a dealer borrower that went into Chapter 7 on 2025-09-10 amid *"allegations of significant fraud"*).
**So operating cash never sees a floorplan credit loss: the cash that is not repaid shows up in investing.** Q4
charges it back.

**The unit series, and the answer to [E2-63] — is growth units or price?** Filed Marketplace Units (424B4 for
2019-20; 10-K key-metrics tables for 2021-25; 10-Qs for H1):

| period | units | YoY | GMV per unit | auction fee per unit | auction fee ÷ GMV |
|---|---|---|---|---|---|
| FY2019 | 241,477 | | $7,454 | $204 | 2.73% |
| FY2020 | 391,466 | +62.1% | $8,430 | $253 | 3.01% |
| FY2021 | 560,959 | +43.3% | $14,083 | $293 | 2.08% |
| FY2022 | 546,088 | **−2.7%** | $16,481 | $322 | 1.95% |
| FY2023 | 598,767 | +9.6% | $14,697 | $352 | 2.40% |
| FY2024 | 743,008 | +24.1% ⁽ᵃ⁾ | $12,786 | $408 | 3.19% |
| FY2025 | 829,276 | +11.6% ⁽ᵃ⁾ | $12,541 | $419 | 3.34% |
| H1-2026 | 424,964 | **+1.6%** | $12,707 | $438 | 3.45% |
| **Q2-2026** | **211,472** | **+0.5%** | $12,768 | **$437 (Q2-25: $438)** | 3.42% |

⁽ᵃ⁾ *includes the units of five acquired physical auctions (four in 2024, the full-year effect in 2025); the 10-K
does not split organic units, so organic growth is lower than shown and cannot be computed from the filing.*

- **Both, and the mix has turned.** From FY2019 to FY2025 auction fee revenue grew 7.1x: units 3.4x and fee per
  unit 2.1x — **about 63% volume and 37% price** on a log split. FY2023-FY2025: units +38.5% (with acquisitions),
  fee per unit +19.0%. **The fee per unit is filed as a price decision, not only as car values:** *"we raised the
  buyer fees charged on our marketplace effective in December 2021"* (10-K FY2021); *"higher buyer fee rates"*
  (10-K FY2025); *"buy fee rate increases"* (10-Q Q2-2026). Through 2022 the fee tracked car prices (GMV per unit
  +121% FY2019-22); from 2023 car prices fell (−24% FY2022-25) while the fee per unit kept rising (+30%) — **that
  is the price increase showing.**
- **[E4-55], run as the corpus runs it:** *"a serious reverse, not likely to disappear in some 'bounce back'
  effect"* is the question for **H1-2026: units +1.6%, Q2 +0.5%, and in Q2 the auction fee per unit FELL $1
  despite a filed "buy fee rate increase"** — the first quarter in the series where a price rise did not show up
  per unit. Recorded at Q2 against the competitor's own H1 units.

**The scarce input this business controls.** Three candidates, and the filing supports one only partially:
1. **Two-sided liquidity in a territory** — enough local dealers bidding that a seller trusts the auction to clear
   (the 424B4 filed the density effect: in a five-year-old territory the gap between auction revenue and auction
   expense per unit was $131, against $38 in a three-year-old one). **22,062 buyers and 14,905 sellers in FY2025.**
2. **The inspection network and the condition data** — ~800 inspectors, ~100 recorded details a car, a
   proprietary engine-sound sensor. Asserted as a *"Growing Technology and Data Moat"*; no filed number measures it.
3. **Go Green** — the seller guarantee against condition claims, which only the party that wrote the report can
   price. Filed number: **$10 of margin per car** (the table above).
**None is ACV's alone** — OPENLANE, Manheim and ADESA run inspected digital auctions (Q2). The scarce input is
real in the sense of being hard to build; whether it is scarce *relative to the rivals* is Q2's question.

**Will the fundamentals look broadly the same in ten years?** **The job, yes; the economics, not established
here.** Dealers have sold trade-ins to each other through auctions for as long as the industry has filed; the
move from the lane to the phone is the change ACV was founded on and is still under way (10-K: *"Wholesale vehicle
online penetration is in the early stages"*). Two filed facts cut the other way and are carried to Q2: the
"digital" company **bought five physical auction houses** in 2023-24, and its **2026 targets set in 2022 ($1.3bn
revenue, $325M Adjusted EBITDA) became a 2026 guide of $845-855M and $73-77M.** Neither makes the business
unintelligible.

**[E4-46] — five minutes or five months?** Auction fees, a truck booking, a floorplan loan and a guarantee are each
legible; the balance-sheet float and the investing-side loan book are disclosed in plain words. **A named filing
inside an understood business.**

**VERDICT: [x] IN** — the fee formula, the per-car economics, the float mechanics, the loan book's cash-flow
classification and the unit series (units and price separated) are all filed and understood. Whether the
position is a franchise is Q2's question.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Pre-registered before the competitor row was computed** (operator rule 9). **My working prior, from the brief
and from reading the 10-K: OUT on criterion (2).** Because that is the story I favour, the attack is aimed at it
hardest **[E4-26]**. The prior FAILS if **any** of: (a) ACV's owner-earnings margin sits inside the computed row
rather than at its bottom; (b) a named competitor's filing shows ACV taking share while that competitor loses it in
the same period; (c) a price increase is filed as having held with units growing; (d) a well-funded attacker is
shown to have failed against the incumbent position. **Results: (a) with the prior; (b) against ACV in the latest
period; (c) partly against the prior through 2025, with the prior in Q2-2026; (d) AGAINST the prior — CarGurus
wound down its digital dealer-to-dealer marketplace in 2025. Recorded as the strongest fact for the bull case.**

### THE BULL CASE, BUILT FIRST AND AS STRONGLY AS THE FILINGS ALLOW

1. **Network effects are filed, not asserted.** Territory density raised per-unit auction margin from $38 to $131
   (424B4); buyers 12,373 (2020) → 22,062 (2025), sellers 7,152 → 14,905 (10-K FY2021 and FY2025 tables). A seller
   goes where the bidders are; bidders go where the cars are.
2. **Units grew 3.4x in six years while the industry did not.** ACV's own guidance assumptions describe the dealer
   wholesale market as *"approximately flat"* (2025) and *"expected to decline in the mid-single digits"* (2026,
   Q1 release) — so FY2025's +11.6% and H1-2026's +1.6% are share gains against a flat-to-shrinking pool.
3. **Price increases were taken and held through 2025, in a flat market — [E2-44] half one.** Buyer fees raised
   December 2021, again in 2025 and 2026; auction fee per unit +30% FY2022-25 while GMV per unit fell 24%. That is
   *"raise prices even when product demand is flat and capacity is not fully utilized."*
4. **The best-funded attacker quit.** CarGurus 10-K FY2025 (acc. 0001193125-26-059435): *"On August 6, 2025, our Board
   of Directors determined … to wind down CarOffer, including the CarOffer Dealer-to-Dealer and Instant Max Cash
   Offer products … we concluded that the CarOffer Transactions Business has proven less effective in today's more
   volatile and unpredictable pricing environment"*. **[E2-45]'s attacker, with ample capital and a consumer car
   marketplace for a funnel, tried and left.**
5. **A strategic buyer is paying 45% over the unaffected price for it.** Copart, the salvage-auction leader with a
   36.5% operating margin, is paying $1.9bn in cash and calls ACV *"market-leading digital wholesale platform"*
   (EX-99.1). Recorded as a buyer's opinion, not evidence of a moat — but it is an informed opinion.

### NOW THE ATTACK

**[E3-03] criterion (2) — "no close substitute." FAILS, in three registrants' own words.**
- **ACV names three.** 10-K FY2025, Item 1: *"We mainly compete with large, national vehicle auction companies, such as
  Manheim, a subsidiary of Cox Enterprises, Inc., Adesa, a subsidiary of Carvana, and OPENLANE. … Manheim has
  expanded into online wholesale marketplaces and auctions, and OPENLANE is competing in the online wholesale auction
  market."*
- **OPENLANE names ACV.** OPENLANE 10-K FY2025 (acc. 0001395942-26-000006): *"Our principal sources of competition
  primarily come from: (i) large, established competitors (e.g., Manheim, ADESA U.S. (Carvana), America's Auto
  Auction, ACV Auctions, EBlock and NextGear Capital)"*.
- **Copart names ACV** — before it agreed to buy it. Copart 10-K FY2025 (acc. 0001628280-25-042946): *"The largest national
  or regional vehicle auctioneers in the U.S. include RB Global (including its subsidiary Insurance Auto Auctions,
  Inc.), Carvana, Openlane, Manheim, Inc. and ACV Auctions Inc."* (EDGAR full-text search, "ACV Auctions" in 10-Ks
  2024-01-01 to 2026-09-12: 40 hits — ACV 28, OPENLANE 3, Copart 2, RB Global 1, CarGurus 1, Rand Capital 4, Core
  Scientific 1; `fts_count` per peer CIK, bare padded form: OPENLANE 8, Copart 19, RB Global 1, Carvana 0, CarMax 0,
  America's Car-Mart 0 — output `peers/get_out.txt`. The counts are prompts; the two sentences above were read in the
  documents.)
- **And ACV's customers owe it nothing.** 10-K FY2025, Item 1A: *"Our customers have no obligation to conduct a minimum
  number of transactions on our marketplace platform or to continue using our marketplace platform over time."* No
  contract, no minimum, no switching cost filed — the dealer can list the next car on OPENLANE or run it through
  Manheim's lane.

**(b) — who is taking share now? THE COMPETITOR'S UNITS, SAME PERIOD, AGAINST ACV'S.** OPENLANE 10-Q Q2-2026 (acc.
0001395942-26-000031): **dealer consignment vehicles sold 205,000 against 182,000 (+12.6%) in Q2 and 399,000 against
354,000 (+12.7%) in H1-2026**; FY2025 710,000 against 620,000 (+15%) (10-K). **ACV: Q2-2026 +0.5%, H1-2026 +1.6%,
FY2025 +11.6% with acquisitions.** In the dealer-to-dealer lane ACV calls its own, **the closest digital competitor
grew units eight times faster than ACV in the first half of 2026, and faster in 2025 too.** ACV's releases in the same
quarters say *"market share gains in dealer wholesale"* — which can be true against a shrinking market and still
describe a company losing ground to the rival it names. **The prior's condition (b) goes to the prior.**

**(c) and [E2-44] half one / [E4-37] — pricing. Held through 2025; the industry raised together; and in Q2-2026 the
increase did not show.**
- **OPENLANE raised prices in the same year:** *"Auction fees per vehicle sold for the year ended December 31, 2025
  increased $50, or 16%, to $357 … The increase in auction fees per vehicle sold reflects the mix of vehicles sold in
  2025 and the impact of price increases."* **ACV's fee per unit rose 2.7% in FY2025 ($408 → $419) while OPENLANE's rose
  16%.** When the whole oligopoly lifts fees in the same year, the pricing belongs to the structure, not to one firm —
  and the row cannot tell conduct from position **[E3-61]**.
- **ACV charges promotions against revenue:** *"From time to time, we provide promotions and incentives to buyers and
  sellers in various forms including discounts on fees, credits and rebates"* (10-K note 1). Amounts not disclosed.
- **Q2-2026:** filed *"buy fee rate increases"*, **fee per unit $437 against $438**, units +0.5%. The price was
  raised; the realised price per car did not move. That is the first reading of [E4-37]'s agony, not a franchise's
  yawn.

**[E3-46] and [E3-03]'s demonstration — "high rates of return on capital." FAILS; there is no return.** Operating loss
in every filed year FY2019-FY2025 (−8.3% in FY2025); net loss every year; **accumulated deficit $587.6M** at
2026-06-30. The row below puts ACV **last of five marketplace filers on both owner-earnings measures and on GAAP
operating margin.**

**[E2-44] half two — "large dollar volume increases … with only minor additional investment of capital." FAILS.**
FY2021-FY2025 revenue rose $401.2M ($358.4M → $759.6M). Over the same five years ACV spent **$269.5M of cash plus $8.6M
of stock and $2.0M of contingent consideration on acquisitions**, **$256.0M of stock compensation** (cash-flow add-back
$237.0M + capitalised $19.0M), **$122.7M of capitalised software and $21.7M of equipment**, and grew a floorplan loan
book funded by $120M of warehouse debt — while the IPO raised the capital (424B4, $25.00 a share, 2021-03).

**[E4-04] — must the moat be continuously rebuilt, and does the spend defend the advantage or buy its replacement?
BOTH HALVES FIRE.**
- **The technology is rebuilt every three years.** Capitalised software $35.6M in FY2025 (4.7% of revenue), with
  **in-service software carrying a 1.8-year weighted remaining life** and $39.2M more in work-in-progress (note 7);
  amortization $29.2M. A lapse in that spend does not narrow the product; it ages it out in under three years.
- **The "digital" model bought physical auctions to reach the supply it could not win digitally.** Five acquisitions
  in 2023-24 (April 2023, August 2023, Alliance Auto Auctions, 166 Auto Auction, March 2024, Indiana Auto Auction)
  each *"offers wholesale car auction services"*; the 10-K's own risk factor: *"our acquisition strategy related to
  Remarketing Centers involves certain risks … coordinate with our digital marketplace so as to minimize any internal
  competition."* **The spend buys a different channel, not a wider version of the same moat.**

### THE COMPETITOR ROW — required **[E3-28]**

**Formula, one for every filer** *(CONVENTION of this row, the framework's owner-earnings construction at the capex
end)*: owner-earnings margin = (operating cash flow − stock compensation add-back − purchases of property and equipment
− capitalised software) ÷ revenue. Cells are **XBRL transcription from each filer's companyfacts, newest vintage**
(script `peers/compute.py`, output `peers/row_out.txt`), **cross-checked against the filed statements for ACV (every
FY2025 input exact, Step 0), OPENLANE (OCF $391.9M exact to its MD&A) and Copart (capex $569.0M against "Capital
expenditures and acquisitions" $570.2M in its MD&A).**

| latest FY | **ACVA** | OPENLANE (OPLN) | Copart (CPRT) | RB Global (RBA) | CarGurus (CARG, ex-CarOffer) | Carvana (CVNA) | CarMax (KMX) |
|---|---|---|---|---|---|---|---|
| period end | **12/31/25** | 12/31/25 | 7/31/25 | 12/31/25 | 12/31/25 | 12/31/25 | 2/28/26 |
| 10-K accession | **0001637873-26-000011** | 0001395942-26-000006 | 0001628280-25-042946 | 0001628280-26-011682 | 0001193125-26-059435 | 0001690820-26-000009 | 0001170010-26-000021 |
| role | subject | digital wholesale + AFC floorplan; **names ACV** | salvage online auctions; **names ACV**; now the buyer | salvage (IAA) + equipment | consumer marketplace; **quit D2D in 2025** | retail principal; owns ADESA US lanes | retail principal; own wholesale auctions |
| revenue | **$759.6M** | $1,934.5M | $4,647.0M | $4,590.7M | $907.0M | $20,322M | $25,881M |
| **GAAP operating margin** | **−8.3% ← last** | 10.2% | 36.5% | 15.5% | 27.0% | 9.3% | n/t |
| SBC ÷ revenue | **7.5% ← highest of the five marketplaces** | 0.8% | 0.8% | 1.4% | 5.6% | 0.5% | 0.4% |
| **owner-earnings margin, latest FY** | **−3.1% ← last of five** | +16.6% | +25.7% | +14.2% | +23.8% | +3.9% | +4.4% |
| **owner-earnings margin, 5 years cumulative** | **−9.2% ← last of five** | +9.5% | +22.2% | +14.5% | +11.0% | −4.1% | −0.8% |
| units, latest FY | **829,276** | 1,472,000 (710,000 dealer) | >4 million (release) | n/c | — | n/c | 780,684 retail |
| auction fee per unit | **$419** | $357 | n/c | n/c | — | — | — |
| **dealer units, H1-2026 YoY** | **+1.6%** | **+12.7%** | — | — | — | — | — |

*n/t = operating income not tagged in a resolving form; n/c = not computed. **The margin comparison is valid for the five
marketplace/agency filers (ACV, OPENLANE, Copart, RB Global, CarGurus)**; Carvana and CarMax are retail principals whose
revenue is the car and whose operating cash carries retail inventory, so their margins are shown and **not ranked**.
ACV's owner-earnings cells here use the cash-flow SBC add-back and **do not yet adjust for the float or for floorplan
credit losses** (Q4 does both; each makes ACV's cells worse, not better). OPENLANE's and ACV's floorplan books both sit in
investing, so the row treats them alike.*

- Peers named: **7 SEC filers in the row** against the industry's real competitors as ACV and OPENLANE name them —
  **Manheim (Cox Automotive), ADESA US (Carvana), OPENLANE, America's Auto Auction, EBlock, NextGear Capital (Cox), and the
  smaller independents.** **America's Car-Mart** (named in the brief) is a buy-here-pay-here **retailer — a customer
  class, not a competitor**; its 10-K contains no "ACV" (`fts_count` 0) and it is excluded with that ground.
- **Unavailable, with the limit stated rather than papered: Manheim (Cox Enterprises, private — the largest competitor
  and no periodic filing exists), America's Auto Auction and EBlock** (no SEC ticker-map entry found for either name in
  this run's lookup; ownership not asserted). **Adjudication under the narrow-only rule carried by ACLS, KLAC, AMAT,
  LRCX, ACMR and ALKT: an additional competitor can only narrow a moat, never widen one.** ACV is already last in the
  computed marketplace row on every return measure, so no unpriced peer can lift it to IN. **Recorded as a row limit,
  not PROVISIONAL** (the PLAB rule).
- **[E3-61] limit:** the row shows position, not conduct — and the 2025 price increases at both OPENLANE and ACV are
  exactly the conduct it cannot explain.

**What the row says, read plainly.** In used-vehicle remarketing the returns sit with **scale in salvage** (Copart
+25.7%, RB Global +14.2%) and with **the incumbent that owns the commercial off-lease supply** (OPENLANE +16.6%, whose 10-K
calls its *"exclusive off-lease inventory not available on any other competitor digital platform or physical auction"* a
*"meaningful competitive differentiator"*). **ACV, the dealer-to-dealer specialist, has never shown a positive
owner-earnings margin across a five-year window, and in 2026 its closest digital competitor is outgrowing it in its own
lane.** The buyer of the business is a salvage incumbent at a 36.5% operating margin — the row's top, buying the row's
bottom.

**[E4-32] — direction.** **Operating economics improving; moat not shown to widen.** Operating margin −25.2% (FY2022) →
−8.3% (FY2025); Adjusted EBITDA −$56.4M → +$58.8M. But units stalled in H1-2026 while OPENLANE's dealer units grew
12.7%, and the Q2-2026 fee rise did not show per car. **Direction recorded as IMPROVING COST LEVERAGE, NARROWING POSITION
IN 2026**, which [E4-32] does not count as widening (*"that does not necessarily mean that the profit is more this year
than last year"*).

**Untapped pricing power [E3-33, E5-28]?** **Not claimed** — it would claim near-monopoly, and three registrants name the
substitutes. **[E2-53] dominance? No** — the largest competitor (Manheim) is larger and private. **[E4-36] — which cause
of success?** **Wave-riding on the digitisation of dealer wholesale plus extreme performance on one variable (inspection
trust)** — the wave is available to Manheim, OPENLANE and ADESA too.

**[E2-45] — the attacker's test, both ways.** CarGurus attacked and quit (bull point 4) — *for a newcomer* the door is
hard. But ACV is itself the attacker that entered in 2015 and took 829,276 units from incumbents; OPENLANE has converted
a physical-auction company into a digital marketplace that now grows faster than ACV; and Copart's stated reason for the
purchase is to *"leverage its global buyer network and physical infrastructure"* — the incumbents can absorb the
digital model. **A door that a newcomer finds hard and incumbents walk through is a structure without a single owner.**

**[E4-23] — key-person dependence.** Founder-era CEO (George Chamoun) retained through the merger; no founder-dependence
disclosed as a business risk beyond the ordinary key-employee factor. **Not a moat defect here.**

- Needed or desired **[x]** · no close substitute **[ ] — fails: ACV names three substitutes; OPENLANE and Copart each
  name ACV among theirs; customers owe no minimum** · not price-regulated **[x]**
- Must the moat be continuously rebuilt? **Yes — software on a sub-three-year life, and five physical auctions bought to
  reach supply [E4-04].** Depends on a great manager? **No.**
- Primary moat metric and trend: **owner-earnings margin −3.1% latest / −9.2% five-year (last of five); units +1.6% in
  H1-2026 against OPENLANE's dealer units +12.7%; fee per unit flat in Q2-2026 despite a filed increase.**
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: improving cost leverage, narrowing position in 2026**

**VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**OUT, on the business.** The evidence is here and the business fails the franchise test on five filed grounds:
criterion (2) fails on ACV's own list of substitutes, on OPENLANE's and Copart's lists naming ACV, and on customers who
owe no volume **[E3-03]**; the closest digital competitor grew dealer units 12.7% in H1-2026 against ACV's 1.6%, so the
position is not widening **[E4-32, E4-55]**; the 2025 price increases were taken industry-wide (OPENLANE +16% per
vehicle) and ACV's Q2-2026 increase did not reach the realised fee **[E2-44] first half, [E4-37], [E3-61]**; there is no
return on capital in seven filed years and ACV is last in the marketplace row on every return measure **[E3-46]**; and
the growth took $280M of acquisitions, $256M of stock pay and $144M of capitalised software and equipment, with the
technology on a sub-three-year life and the supply bought as physical auctions **[E2-44] second half, [E4-04]**. **The
file closes here.**

*Asked aloud: can I name a document that would move this?* Manheim's financials do not exist publicly and could only
narrow a moat rated NONE; America's Auto Auction and EBlock likewise. **No.** *And why OUT rather than UNKNOWABLE, given
CarGurus's exit?* Because CarOffer's exit shows the lane is hard for a **newcomer**, which is a fact about barriers to
entry for outsiders, while the verdict rests on the **substitutes already inside** — Manheim, OPENLANE and ADESA — each
named by a registrant, and on the returns, which are filed. The exit is recorded at Q6 as a refutation condition.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT and the file closed there.** Built because the brief required the proxy,
the EX-99.1 releases, [E3-48], [E4-52] and the [E2-49] check, and because a Q2 OUT written without the manager record
would be an opinion. **Nothing here promotes the name; a strong Q3 cannot repair Q2 [E2-37, E2-38, E3-39].** No gate
was assumed short — and this one was not.

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution — ticked, on [E3-43].** Q2 found no franchise: *"a business, unlike a franchise, can be killed by
      poor management."* A marketplace that must win each car from three named rivals, write guarantees on its own
      condition reports, and underwrite floorplan loans to dealers (one of which went into Chapter 7 amid fraud
      allegations) is a have-to-be-smart-every-day business.
- [ ] **Control [E1-16]** — not ticked; an exitable NYSE share (and, from 2026-09-10, a pending cash tender).
- [ ] **Leverage [E3-29]** — not ticked as a gate, **named**: a $192M floorplan book funded by $125M of warehouse debt,
      and a balance sheet whose cash is 80% other people's money (Q1). The Tricolor loss ($18.7M, 4.4% of year-end equity)
      is what one small asset error costs here.

**One ticked → Q3 is a BINARY GATE and no price compensates [E1-16, E3-29, E5-35].**

### HONESTY — binary, filings-based, each matter dated to when it became PUBLIC [E5-16]

| date public | matter | what the filing says | disqualifier? |
|---|---|---|---|
| 10-K FY2021-FY2025 | legal proceedings | *"We are not presently subject to any pending or threatened litigation that we believe, if determined adversely to us, individually, or taken together, would reasonably be expected to have a material adverse effect"* (Item 3, FY2025) | **No.** |
| 10-K FY2021-FY2025 | internal control | Ernst & Young (auditor since 2018), unqualified; the one critical audit matter is the automated revenue systems; **"material weakness" appears only in generic risk-factor text and the auditor's standard paragraph in each 10-K searched** | **No.** |
| 10-K FY2025, 10-Q Q2-2026 | Tricolor, a floorplan borrower, Chapter 7 on 2025-09-10 amid *"allegations of significant fraud"* | $18.7M reserved and quantified at every line; $25.1M of finance receivables written off in H1-2026 | **No** — the fraud alleged is the borrower's. A credit-control prompt, carried to [E2-57] below. |
| releases and 10-Q non-GAAP tables, 2024-2026 | *"Litigation-related costs are related to an anti-competition case"* ($1.55M 2024, $1.10M 2025) | **the case is never named, nor ACV's side of it** (searched: 10-K FY2023-FY2025, 10-Q Q2-2026, releases) | **No** — an **unintelligible-footnote prompt [E4-22]**: a cost excluded as non-representative for two years whose subject is undisclosed. |
| **10-Q Q2-2026, filed 2026-08-10** (Part II, Item 5) | **new executive severance agreements approved 2026-05-04**, replacing the prior change-of-control plan: CEO 2.0x salary + 1.5x target bonus, others 1.5x + 1.0x; **full vesting of time awards, and of performance awards "with performance deemed achieved at the greater of target or actual"**; a **"Change in Control Protection Period" beginning "three months prior to" a change in control** | **disclosed 98 days after approval, in the quarterly report's "Other Information" item** — the May 2026 8-Ks carry Items 2.02, 1.01 and 5.07 only. **The "unaffected" date the merger release names, 2026-08-10, is the day this 10-Q was filed.** | **No disqualifier found — a candor prompt under [E2-68]**, conduct where management holds the information advantage. Whether sale discussions had begun by 2026-05-04 is in the **Background of the Offer** section of the SC 14D-9, **not yet filed** (UNRESEARCHED, non-governing). |
| 8-K 2026-08-10 (EX-99.2) | CFO Bill Zerella departs *"to become Chief Financial Officer of another company"*; the VP of Investor Relations becomes CFO | one month before the merger agreement | **No.** Recorded. |
| 10-Q Q2-2026, Item 5 | Chief Accounting Officer adopted a Rule 10b5-1 sale plan on 2026-06-15, first trade not before 2026-09-14 | up to 8,000 shares plus net RSU vesting | **No.** Recorded against the same Background-of-the-Offer work order. |

**No integrity disqualifier found.** *A Q3 pass is the absence of found disqualifiers, not a finding that the managers are
honest [E5-17].*

### THE FLAGS [E4-22, E5-15, E4-29] — prompts to read, and I read them

- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, in the releases, the 10-K, the guidance and the pay.**
  Every release read (Q4-2021 through Q2-2026) headlines **Adjusted EBITDA** and guides it; it is one of the five key
  metrics in every 10-K FY2021-FY2025; it adds back **stock compensation of $56.9M — 97% of the $58.8M Adjusted EBITDA
  itself** (FY2025) — and **"Tricolor bankruptcy losses" of $18.7M**. **The bonus plan gates on Adjusted EBITDA and GAAP
  revenue** (DEF 14A 2026). *In management's favour, recorded:* **the gate worked** — *"Given neither the GAAP Revenue
  threshold nor the EBITDA threshold was met, and meeting both such thresholds is a gating requirement to earn any bonus,
  no bonus was earned in 2025"* ($59M against a $65M threshold; $760M against $765M).
- [x] **[E2-57] — the except-for flag — FIRES.** A company whose business includes lending to dealers excludes the credit
  loss on a dealer loan from Adjusted EBITDA and non-GAAP net income as *"not representative of our ongoing operating
  performance"*. The same note 5 then needed **a further $12.6M of finance provision beyond Tricolor in FY2025** for
  *"reserves on specific borrowers exhibiting signs of stress and to a lesser degree, due to deterioration in collection
  experience on the Company's broader finance receivable portfolio."* *"you must count the runs scored against you in all
  nine innings."*
- [x] **trumpeted projections [E4-22] — FIRES, and [E3-48]'s record is taken: the long-term target was missed by a third
  and by three-quarters.**
  - **8-K 2022-02-16, EX-99.1: *"Establishes 2026 financial targets of $1.3 billion in revenue and $325 million of Adjusted
    EBITDA."*** The **2026 guidance** (Q2-2026 release, reaffirmed): **revenue $845-855M, Adjusted EBITDA $73-77M** — **35% and
    77% below the targets** at the midpoints, on the company's own non-GAAP measure.
  - Annual guidance against outturn: **FY2022** $450-460M revenue → **$421.5M, 6.3% below the low end**; **FY2023** $460-470M /
    −$30M to −$35M → $481.2M / −$18.2M (beat); **FY2024** $610-625M / $20-25M → $637.2M / $28.1M (beat); **FY2025** $765-785M /
    $65-75M, cut in November to $756-760M / $56-58M → **$759.6M / $58.8M: below the original low end on both lines.**
    **Record: two beats, two misses, and the four-year target missed by a third on revenue.**
- [x] **metric-switching [E2-49] — FIRES, on the long-term target.** The 2026 targets appear in the February 2022 release
  and in **no later document read**: sweep for "1.3 billion", "2026 financial target" and "2026 target" across the eight
  releases (Q4-2021 through Q2-2026), the 10-Ks FY2021-FY2023 and the 2025 and 2026 proxies — **hits only in the February
  2022 release; no withdrawal statement found.** FY2022 then came in below guidance with units down 2.7%. **A yardstick set,
  followed by deterioration, followed by silence, is the disposition of the yardstick [E2-49]** — not the candor case, which
  announces the switch ahead with reasons. *Also recorded, not scored:* the release highlight **"Auction Marketplace
  revenue"** (Q4-2021, Q4-2022) is absent from Q4-2023 on; and "Marketplace Participants" (424B4) became Buyers and Sellers
  in the FY2021 10-K **with restated comparatives while both were rising** — the candor form. *(An analyst day was held
  2025-03-11 per the Q4-2024 release; no 8-K furnished its materials, so any later target is off the shelf — UNRESEARCHED,
  non-governing.)* **Tally reconciled: FIRED at SHOP, MRVL, PAY, ARM, CALX, BE, ROKU, SWK and now ACVA (nine); FAILED at QLYS,
  CRM, CORT, PLTR, INOD, ACMR, ALKT (seven).**
- [x] **stock-price targeting [E3-50] — FIRES, and the merger converts the target.** The 2024 PSUs vest only if the 30-day
  average price *"equals or exceeds $26 (the "Stock Price Condition")"* by 2027-07-01; the 2025 and 2026 PSUs vest on relative
  TSR against the Russell 2000. **The merger agreement converts each PSU "based on the greater of target and actual performance
  (as determined by the Compensation Committee of the board of directors in its discretion)"** into Copart awards subject to
  the same terms *"other than applicable performance goals"* — **2,364,836 PSUs at target, $24.8M at $10.50**, including 2024
  awards whose $26 hurdle a $10.50 sale could never meet. The May 2026 severance agreements (table above) had already written
  the same "greater of target or actual" into the change-in-control terms. **[E4-27], turned on the sellers: the pay changed
  ahead of the sale in the direction that pays on a sale.**
- [x] **serial share issuance [E5-15] — FIRES, moderately.** Class A + B outstanding **156,266,553 (2022-02-15, 10-K FY2021
  cover) → 173,179k (2025-12-31), +10.8%**; SBC 8.5% of FY2025 revenue including the capitalised portion; **bonuses for 2023
  and 2024 paid "in the form of RSUs that were vested upon grant"** (DEF 14A 2026; the 2025 proxy says the same of 2022). The
  May 2026 ASR retired 5,993k shares, leaving 169,824,232 (+8.7% net since 2022).
- [ ] **weak accounting** — **not ticked**, one classification recorded rather than scored: floorplan loan growth runs through
  investing while its credit-loss provision is added back inside operating cash (Q1), so **operating cash never carries a
  floorplan loss**. The classification is standard for finance receivables and disclosed; OPENLANE's AFC book sits the same way.
- [x] **unintelligible footnotes — one prompt:** the unnamed anti-competition case (table above).
- [ ] **filed-figure tells [E4-30]** — not ticked; revenue growth is not smooth (+72%, +18%, +14%, +32%, +19%, FY2021-25) and
  cash taxes are minimum state and foreign amounts on a loss-maker.
- [ ] **dividends funded by issuance [E2-52]** — no dividend.
- [ ] **the restructuring charge [E3-53]** — none found.

**[E4-52] — do the flags converge?** **Yes.** Adjusted EBITDA headlined, guided and paid on while excluding a stock-pay line
nearly its own size and a lender's credit loss; a four-year target that vanished after the first miss; performance awards on
a stock price, converted at target in a sale; enhanced change-in-control terms adopted three months before the unaffected date
and disclosed in a quarterly report. **Several flags pointing one way are one reinforcing system, not a sum of prompts.** The
countervailing facts are real: the bonus gate withheld the 2025 bonus; Tricolor was quantified at every line; no restatement;
clean audit opinions.

### STEP 3 — THE PRIMARY TEST [E2-01]

**No earnings rate on equity to report: net loss in every year FY2019-FY2025** (FY2025 −$66.1M on average equity of $434.8M,
−15.2%). On [E2-43]'s unleveraged net tangible assets: tangible equity **$131.4M** at 2026-06-30 (Step 0), of which capitalised
software is $87.1M, against an operating loss. **[E2-42]'s red light is on.** [E3-54]'s retention test does not apply:
accumulated deficit **$587.6M**; the IPO share sold at $25.00 in March 2021 is bid $10.50 in cash.

**The half-owner test [E2-26].** *Mixed.* **Passes:** the float paragraph says in plain words that the cash position is
*"bolstered by marketplace float"*; Tricolor quantified at every line; revenue and cost split by line every year. **Fails:** no
organic unit figure in the years five physical auctions were bought; promotions and incentives charged against revenue never
quantified; the anti-competition case unnamed; the change-in-control severance reached shareholders a quarter late; the 2026
target never revisited.

**The institutional imperative — all four [E2-30]:**
- [ ] resists change — **no** (product launches, CFO change, the sale itself).
- [x] **projects or acquisitions to soak up funds — yes:** seven acquisitions FY2021-24 ($280.1M gross), five of them physical
  auctions, bought by a company whose IPO case was the digital replacement of the physical lane.
- [ ] staff studies — not observable from filings.
- [x] **peer behaviour imitated — yes, filed:** OPENLANE runs AFC floorplan finance beside its marketplace; ACV's financing was
  *"immaterial to date"* at the IPO (424B4) and became a $192M book on a warehouse line (2024). Copart names *"physical
  infrastructure"* as what it brings; ACV had already begun buying it.

**Capital allocation — the buyback conditions [E5-08, E4-31].**
- (1) ample funds? **Not of the company's own.** At 2026-06-30, after the ASR: cash $242.3M, of which net seller float $194.0M —
  **own cash about $48M** against $80M drawn on the revolver and $125M on the warehouse line. The $50M ASR was paid from a
  balance sheet whose cash belongs mostly to sellers.
- (2) a material discount to intrinsic value, conservatively calculated? **The owner-earnings value is not a positive number
  (computation below).** On the board's own later act, yes: the initial ASR delivery averaged **$5.72** (10-Q Part II Item 2) and
  the board agreed to sell at **$10.50** four months later. **Both halves recorded:** the repurchase was accretive to holders at
  the sale price; and a company cash-negative after stock pay spent float-supported cash on its own shares within four months of
  agreeing to sell itself.
- (3) [E4-31] shareholders supplied the information to estimate value? **Partly** — no organic units, no incentive amounts.
- **CAPITAL ALLOCATION FLAG, stated with the humility clause [E4-13]:** *"it is natural for CEOs to be optimistic about their own
  businesses. They also know a whole lot more about them than I do."* The flag is the sequence: $280M of acquisitions, a floorplan
  book grown into a fraud loss, a buyback on customer float, and a sale at 42% of the IPO price. **[E5-44] barely bites** — the
  only stock consideration was $8.6M. Binds position size; there is no position.

**THE GUARDRAIL — checked before the verdict.**
- [x] Nothing in this Q3 is used to promote the name **[E2-37, E2-38, E3-39]**.
- [x] No key-person dependence to move to Q2 **[E4-23]**.
- [x] Is a great manager the reason to act? **No** — the franchise is not intact (Q2 NONE); **[E2-35, E2-36]** has nothing to
      apply to.

**VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] NOT REACHED — closed at Q2.**
*Had Q2 been IN, this would read **IN on honesty** (no disqualifier found) under a **binary-gate** weight case, with [E4-29],
[E2-57], [E4-22]/[E3-48], [E2-49], [E3-50] and [E5-15] firing and converging [E4-52], a capital-allocation flag, and one work
order (the SC 14D-9 Background of the Offer) that could move the candor read on the May 2026 severance terms.*

## Q4 — WILL IT SURVIVE?

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT.** Built because the brief required the payables flag, the customer funds, the
SBC completeness check, the perimeter and the named death. Script `oe.py`, output `oe_out.txt`.

### THE DEFECT IN THE QUEUE'S NUMBER, FOUND BEFORE ANYTHING ELSE

The row reads **`oe_bottom_m -52 | oe_top_m -44`**. **Both reproduce, and — for the sixth time (INTC, BA, ACMR, SWK, ALKT, ACVA)
— from different windows AND different (c) ends.** `oe_bottom` is the **3-year FY2023-25 mean at the capex end** (−$51,947k);
`oe_top` is the **5-year FY2021-25 mean at the D&A-as-filed end** (−$44,234k). **Both carry three further defects specific to this
filer:** (i) **the seller float** — +$122.7M in FY2021 alone — is counted as earnings; (ii) **floorplan credit losses are
omitted**, because the provision is added back in operating cash and the loss sits in investing ($31.3M in FY2025); (iii) the
D&A end charges **acquired-intangible amortization and the amortization of capitalised SBC** as maintenance, the second of which
double-counts SBC. The row's *"from −$137.9M"* is FY2022 on the screen's formula and reproduces (−$75,175k − $39,324k − $3,211k
− $20,185k).

### THE WC_NOTE, RECONCILED — AND WHAT OPERATING CASH IS WITHOUT THE CUSTOMERS' MONEY

- **Confirmed: FY2021 accounts payable +$242,856k ÷ operating cash $85,290k = 284.7%** (the row's 285%), as filed in the FY2022
  and FY2023 10-K cash-flow statements (read; the tag matches the line). **It is seller float:** FY2021 GMV rose from $3.3bn to
  $7.9bn and the amount owed to sellers at year-end rose with it; trade receivables from buyers rose $120,155k on the other side.
  **The next year it ran backwards:** FY2022 payables −$73,087k, receivables +$47,170k, operating cash −$75,175k.
- **Operating cash with the two float lines removed** (accounts payable and trade receivables, as filed; *the payables line also
  holds ordinary vendor payables, which the filing does not split — the MD&A attributes the movements to sellers and buyers*):

| $k | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM 6/26 |
|---|---|---|---|---|---|---|---|---|
| operating cash, as filed | −72,460 | 10,368 | **85,290** | **−75,175** | −17,885 | 65,397 | 78,232 | 38,905 |
| float lines (payables + trade receivables) | −5,543 | 36,991 | **122,701** | −25,917 | −20,206 | 33,633 | 15,801 | −37,226 |
| **operating cash without the float** | **−66,917** | **−26,623** | **−37,411** | **−49,258** | **2,321** | **31,764** | **62,431** | **76,131** |

- **FY2021-25 cumulative: operating cash $135.9M as filed, $9.8M without the float. Over all seven filed years: +$73.8M as filed,
  −$83.7M without it.** Every dollar of cumulative operating cash ACV has reported came from holding sellers' money; **FY2021's
  "positive year" was −$37.4M.** In the trailing twelve months the float ran the other way (−$37.2M), so the underlying figure
  ($76.1M) is **better** than reported — the improvement is real, and it is recorded.
- **The INOD and DELL lesson, applied:** the as-filed series manufactures a sign change out of a float swing. **The "SIGN CHANGE —
  recoveries" label described operating cash moved by customers' money — wrong in object, as at ALKT, by a different mechanism
  (ALKT's was stock pay).** Without the float, operating cash does turn positive (FY2023); **owner earnings never do** (below).

### Owner earnings — the one number **[E2-23]**

**Construction** *(CONVENTION, per the framework, plus two filer-specific adjustments disclosed as judgments)*: operating cash
**less the float lines** — *judgment: the seller float is money in transit that is owed to sellers; Berkshire describes its own
float as "money we temporarily hold in our insurance operations that does not belong to us" and values it as the funding of
investments, never as earnings [E5-46]; applying that to an auction house is our analogy, so the as-filed construction is shown
beside it* — **less the floorplan credit-loss provision** (the loss the cash-flow classification moves to investing) — **less
stock compensation in full [E5-06]** — **less (c)**.

**SBC — resolves every year, and is COMPLETE on the charge measure; the stock-settled bonus reconciles without contradiction.**
- The cash-flow add-back resolves FY2019-FY2025 and in both 10-Qs. **The measure used is note 13's total — add-back plus capitalised
  SBC** ($64,464k FY2025), because capitalised SBC is in neither operating cash nor cash capex.
- **The Boeing test — stock-settled pay outside the tag:** bonuses were paid in vested RSUs. **The equity-statement credit differs
  from the note 13 total by +$8,039k (FY2025), −$3,910k (FY2024) and −$519k (FY2023).** If each year's bonus is expensed as SBC while
  earned and credited to equity when settled the next February or March, the differences imply bonuses of **$3.6M (2022), $4.1M
  (2023), $8.0M (2024) and zero for 2025** (proxy: *"no bonus was earned in 2025"*). **Three equations in three unknowns cannot
  confirm that reading; they could have refuted it on sign, and they do not.** On it, the charge measure already contains the
  bonus. **Residual risk stated:** over FY2023-25 the equity credit exceeds the charge by $3.6M in total; using the equity credit
  instead moves no construction's sign. **401(k): no discretionary contributions 2023-2025** (note 14). ESPP expense is inside
  note 13 and not separately stated.
- **SBC ÷ operating cash, the calibrated row:** **ACVA 330.5% cumulative over seven filed years ($243.8M ÷ $73.8M), and 174.5% over
  FY2021-25 — above every name in the row** (ROKU 140.2% · CALX 98.4% · ARM 96.6% · CRWD 68.0% · ELF 40.9% · PLTR 32.0% · QLYS
  24.9% · SHOP 22.1% · PAY 11.5%). **On operating cash without the float the ratio is not meaningful: the seven-year cumulative is
  negative.** By year: 55% (FY2020), 27% (FY2021), 104% (FY2024), 73% (FY2025), 137% (TTM).
- **[E3-70], because SBC exceeds 50% of operating cash: the grant table.** RSUs granted in FY2025: 5,719k at $15.52 = **$88.8M**
  against a $64.5M charge. The charge is the floor of the subtraction; the grant measure makes every construction more negative
  and is reported, not stacked.

**(c) — what the filer capitalises, and which class it is in.**
- **Capitalised internal-use software: $35.6M in FY2025**, in-service weighted remaining life **1.8 years** (note 7) — a recurring
  cost of staying in the market (Q2, [E4-04]); treated as capex. Equipment $9.1M.
- **D&A contains three things:** depreciation and software amortization; **acquired-intangible amortization** ($10.6M FY2025 —
  [E3-44] and [E2-43] add it back); and **amortization of capitalised SBC** ($6.2M FY2025 — already subtracted in the SBC line).
  **So the corpus default end is D&A less both: $26,975k in FY2025.** *(ELF's triple-count class: not in it — no deferred contract
  costs sit in D&A.)*
- **A disclosed judgment [E2-23]:** the capex end is the better guess, because amortization on a software base that has grown every
  year lags the spend.

| $k | OCF ex-float | SBC total | floorplan provision | (c) D&A-ex | (c) capex | **OE, D&A-ex** | **OE, capex** | as filed, capex end |
|---|---|---|---|---|---|---|---|---|
| FY2019 | −66,917 | 998 | 65 | 1,739 | 6,593 | **−69,719** | **−74,573** | −80,051 |
| FY2020 | −26,623 | 5,705 | 107 | 4,282 | 8,885 | **−36,717** | **−41,320** | −4,222 |
| FY2021 | −37,411 | 23,692 | 1,210 | 4,741 | 14,029 | **−67,054** | **−76,342** | **+47,569** |
| FY2022 | −49,258 | 41,337 | 4,214 | 5,923 | 23,396 | **−100,732** | **−118,205** | −139,908 |
| FY2023 | 2,321 | 53,031 | 4,286 | 11,949 | 28,170 | **−66,945** | **−83,166** | −99,086 |
| FY2024 | 31,764 | 73,526 | 4,323 | 20,446 | 34,241 | **−66,531** | **−80,326** | −42,370 |
| FY2025 | 62,431 | 64,464 | 31,309 | 26,975 | 44,653 | **−60,317** | **−77,995** | −30,885 |
| **TTM 6/26** | 76,131 | 60,628 | 33,587 | 29,589 | 45,905 | **−47,673** | **−63,989** | −67,628 |

*"As filed, capex end" = operating cash as reported − SBC total − capex, with no float or provision adjustment — the lenient display.
Acquired amortization FY2019-21 and FY2022-23 from note 17 of the FY2021 and FY2023 10-Ks; capitalised-SBC amortization from the MD&A
footnotes; floorplan provisions from note 5 of the FY2021, FY2022, FY2023 and FY2025 10-Ks and the Q2-2026 10-Q; H1 splits from the
Q2-2026 release and 10-Q.*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38].** Every contiguous window of three years or more (fifteen),
both (c) ends, full table in `oe_out.txt`:

| window | OE, D&A-ex | OE, capex | as filed, D&A-ex | as filed, capex |
|---|---|---|---|---|
| **5y FY2021-25 (the default [E2-42])** | **−$72,316k** | **−$87,207k** | −$38,045k | −$52,936k |
| 3y FY2023-25 | −$64,598k | −$80,496k | −$41,549k | −$57,447k |
| 3y FY2019-21 (best) | −$57,830k | −$64,078k | −$5,986k | −$12,235k |
| 3y FY2022-24 (worst) | −$78,069k | −$93,899k | −$77,958k | −$93,788k |
| 7y FY2019-25 | −$66,859k | −$78,847k | −$37,863k | −$49,850k |
| **TTM to 2026-06-30** | **−$47,673k** | **−$63,989k** | −$51,312k | −$67,628k |

- **Combined range, fifteen windows × both (c) ends: −$93.9M to −$57.8M; with the TTM, −$93.9M to −$47.7M.** On the as-filed display
  (float counted, floorplan losses omitted): −$93.8M to −$6.0M. **No window, no (c) end, no SBC measure and neither construction
  produces a positive owner-earnings figure.** *Is the range too wide to conclude?* **No — it does not span zero.**
- **The perimeter, rebuilt from the business-combination notes** (Step 0): **$269.5M cash + $8.6M stock + $2.0M contingent = $280.1M
  gross, $266.0M net of the Indiana real-estate sale.** Pro forma not buildable: the 10-Ks call the acquisitions *"not material to its
  existing operations"* and omit pro forma information (FY2021 note 16; FY2023-25 notes give none). **Direction of the bias stated:**
  the acquired auctions add units and revenue to the later years of every window — **and the later years are still negative.**
- *Distorted years in the window [E5-11]:* **FY2021 (float +$122.7M, GMV +140%)** favourable and **FY2025 (Tricolor, $18.7M)**
  unfavourable; **[E4-41] removes the favourable one**, which the ex-float construction already does.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · **[x] gruesome**
- *"grows rapidly, requires significant capital to engender the growth, and then earns little or no money."* **Revenue compounded
  38.7% a year FY2019-25 ($106.8M → $759.6M); owner earnings negative in every year; FY2021-25 consumed $280.1M of acquisitions,
  $256.0M of stock pay, $144.5M of software and equipment and $45.3M of floorplan losses, funded by $385.7M of IPO proceeds, customer
  float and $205M of debt.** [E4-43]'s protection for the good class does not apply — no rate is earned on the deposits added.
  **The strongest fact against "gruesome"** is the trend: owner-earnings margin at the capex end −28.0% (FY2022) → −10.3% (FY2025) →
  −8.0% (TTM).

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — NO.** Negative in every year on every construction.
- **(2) massive liquid assets — NO, and the cash line misleads.** Cash $242.3M at 2026-06-30, of which **$194.0M is net seller float**;
  own cash about $48M. [E5-39]: *"We will never be dependent on the kindness of strangers"* — ACV's liquidity *is* strangers' money,
  in transit.
- **(3) no significant near-term cash requirements — FAILS on two dates and one mechanism.** The **warehouse facility's revolving
  feature ends 2027-12-10** and it matures twelve months later ($125M drawn, secured by the floorplan receivables themselves); the
  **revolver** ($80M drawn of $250M, matures 2030-06-26) carries minimum-liquidity and minimum-revenue covenants until the
  **Covenant Conversion Date, no later than 2027-07-30**, then a **maximum total net leverage of 4.0x**, stepping to 3.5x. **And the
  float reverses when volume or car prices fall** — FY2022 is the filed case: units −2.7%, Q4-2022 GMV −29%, float −$25.9M, operating
  cash −$75.2M.
- **Leverage, named and quantified [E4-16, E3-29]:** **$205M of debt**; tangible equity $131.4M; **[E2-54] fails** — FY2025 cash interest
  of $7.9M was not *"comfortably met out of current cash flow net of ample capital expenditures"*: owner earnings were −$60M to −$78M.
  **[E3-52]'s distinction cuts the other way here:** the float carries no covenant but is due to sellers within days; the bank lines
  carry covenants.

### Name the specific way THIS business dies **[E2-27, E3-24]**

**The mechanism: a volume or price shock turns the customers' money back into a liability at the same moment the loan book takes its
losses.** ACV's liquidity is the gap between what buyers owe it and what it owes sellers; the gap widens when GMV grows and narrows when
it falls. The same shock — falling used-car prices, a dealer credit squeeze — raises floorplan defaults, and the Tricolor year shows one
dealer costing 4.4% of equity. Stock pay (8.5% of revenue) cannot be turned into cash pay without deepening the losses.

**Quantified from filed figures:** a 2022-shaped year (Q4-2022 GMV −29%) applied to the 2026-06-30 net float of $194.0M releases
**~$56M** to sellers; add **a 2022-shaped operating year (owner earnings −$118M at the capex end)** and **a Tricolor-scale floorplan loss
($18.7M)**: **~$193M of cash need against ~$48M of own cash and $170M of undrawn revolver**, with a warehouse line secured by the
receivables that the downturn shrinks. Survivable only by drawing most of the revolver — and, after 2027-07-30, meeting a net-leverage
covenant on a business with no positive owner earnings — or by raising equity at a depressed price.

**Likelihood:** [ ] likely **[x] a real possibility** [ ] a low-level possibility — for a liquidity squeeze requiring new capital in a
used-car downturn, because FY2022 already produced the float reversal and −$75M of operating cash, and the stock fell to $4.24 in March
2026 without a price collapse in used cars; **a low-level possibility** for insolvency while the Copart tender is pending, because Copart
funds from cash on hand and the offer carries no financing condition.

**[E4-51] — the bull case stated so its holders would accept it:** *ACV is the scaled digital dealer-to-dealer marketplace; operating
margin improved from −25% to −8% in three years and Adjusted EBITDA from −$56M to +$59M; the float is a structural feature of every
auction house, not a risk; floorplan losses outside Tricolor are small; stock pay falls as a share of revenue; and a strategic buyer with
a 36.5% operating margin has just paid 45% over the market for it.* **Stated fairly, that case is about operating leverage and a buyer's
valuation. It contains no owner-earnings figure above zero.**

### THE [E5-11] SHAPE, AGAINST THE FIVE NAMED ONES

| run | shape | ACVA? |
|---|---|---|
| **ORCL** | contracted not to stop | **No.** Commitments are leases ($47.0M) and ordinary purchases. |
| **ARM / CALX** | earning nothing for owners after paying its people | **Yes, and past both** — SBC 330% of cumulative filed operating cash. |
| **BE** | too little filed history | **No** — seven years filed. |
| **BA** | spending cash undoing past work | **No.** |
| **SWK** | a dividend paid by selling the business | **No** dividend. The $50M ASR was paid from a float-supported balance sheet — adjacent, not the same. |
| **ACVA — A SIXTH: THE BORROWED BALANCE SHEET** | **liquidity that belongs to the customers**: every dollar of cumulative operating cash ever reported came from seller float, 80% of the cash line is float, and the float runs backwards in exactly the downturn that also raises the lender's losses | **Named here as new.** ARM's shape explains why there are no owner earnings; this one explains why the balance sheet looks liquid anyway, and when it stops. |

**VERDICT (recorded, not governing): [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — had Q2 been IN, Q4 would close OUT: owner
earnings are negative on fifteen windows, both (c) ends, both constructions, the grant-date measure and the TTM **[E2-23, E4-25]**;
gruesome **[E4-20]**; strengths (1) and (2) fail and (3) fails on the float mechanism **[E5-11]**; [E2-54] fails. **The file's
governing verdict remains Q2 OUT.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass. **Q2 returned OUT. Q5 is NOT opened.** What follows is the queue's
required price, **headed as operator rule 3 requires and carrying no entry language.**

---
# COMPUTATION — NOT A CLEARANCE

*Required by the queue's output contract of 2026-09-01: every run ends with a price. This is arithmetic on a closed
file. It ranks nothing and recommends nothing.*

**Inputs, dated.** Price **$10.41** (close 2026-09-11, aggregator quote, flagged) · share count **169,824,232** (merger
agreement §4.05, 2026-09-08; 10-Q cover 169,807,980) · **market cap $1,767.9M** · sovereign **5.35%** (US Treasury
30-year par yield, 2026-09-11). Debt $205.0M ($80M revolver, $125M warehouse) against own cash of ~$48M after the seller
float — **enterprise value ~$1,800M** on the revolver alone, ~$1,925M with the warehouse line. Script `q5calc.py`, output
`q5calc_out.txt`.

**1. THE YIELD**

| construction | owner earnings | ÷ $1,767.9M | vs 5.35% |
|---|---|---|---|
| **5y FY2021-25, D&A-ex end** *(default window [E2-42], default (c) [E3-44]; float excluded, floorplan losses charged)* | **−$72.3M** | **−4.09%** | **−9.44 pts** |
| 5y FY2021-25, capex end | −$87.2M | −4.93% | −10.28 pts |
| **TTM to 2026-06-30, D&A-ex end** (the best period on the construction) | **−$47.7M** | **−2.70%** | **−8.05 pts** |
| TTM, capex end | −$64.0M | −3.62% | −8.97 pts |
| worst of fifteen windows (3y FY2022-24, capex end) | −$93.9M | −5.31% | −10.66 pts |
| *display only:* as filed, float counted and floorplan losses omitted, best window (3y FY2019-21) | −$6.0M | −0.34% | −5.69 pts |
| *display only:* the queue row's own ends on the stale $1,148M cap | −$52M / −$44M | −4.52% / −3.85% | — |

**Every construction is negative, including the one that counts the customers' money as earnings.**

**2. WHAT THE PRICE ALREADY ASSUMES — and it is not owner earnings. THE QUOTE IS A MERGER SPREAD.**
- **At $10.41 a buyer is paying for $10.50 in cash from Copart**, due when the tender closes (expected *"by calendar
  year-end 2026"*), subject to a majority tender and HSR. **Gross spread 0.86% ($0.09); about 2.9% annualised to 2026-12-31,
  about 0.9% if it runs to the 2027-09-10 End Date — against a 5.35% bond.**
- **If the deal breaks on antitrust, Copart pays ACV $115.3M — $0.68 a share.** The unaffected price was $7.26 (2026-08-10);
  $7.26 plus the fee is **$7.94, 23.7% below the quote** (30.3% below without the fee, as on a break for any other reason).
  **And ACV pays Copart $57.7M ($0.34 a share) if it takes a superior proposal.**
- **The owner-earnings arithmetic a buyer would face without the bid, in dollars because a negative base has no growth rate:**
  to yield the **5.35% sovereign** on $1,767.9M ACV must earn **$94.6M** of owner earnings a year; to clear the **~10% floor
  [E4-28]**, **$176.8M** — **20.8% of the FY2026 revenue guide midpoint ($850M)**, or **$213 of owner earnings on every car
  sold, on a $419 auction fee.** At OPENLANE's 16.6% owner-earnings margin the floor needs **$1.06bn of revenue, 1.25x the
  guide**, and a swing from −8.0% (TTM, capex end) to +16.6%. At Copart's 25.7% it needs $688M — revenue ACV already has —
  **so the floor is not a volume problem; it is a margin that ACV has never earned in any year and that only the salvage
  incumbent in the row earns.** [E4-35]'s base rate governs any growth path: *"fewer than 10 of the 200 most profitable
  companies"* sustain 15% a year, and this starts from below zero.
- **The ceiling [E2-63] is explicit: $10.50.** The merger agreement caps the upside for a public holder, and the downside is
  the unaffected price.

**3. WHAT YOU ARE PAID.** On owner earnings, **−8.1 to −10.7 points under the sovereign**; **−9.44 points** at the default
window and (c). On the deal, **0.86% gross** for bearing HSR and tender risk. **Neither is an owner-earnings return.**

**THE FLOOR, FIRST [E4-28].** Honest pre-tax expectancy on owner earnings at this price: **negative on every construction.**
**Below roughly 10% the name is not ranked — it is quit on, whatever the sovereign is.** ACVA is quit on twice: at Q2 on the
business, and here on the arithmetic. **The ranking lines are not filled in [E4-21, E3-45].**

**Value as a round-number range [E4-01].** **Every owner-earnings construction is negative, so the owner-earnings value of the
equity is not a positive number, and a range is refused rather than invented.** What can be said: **the only number supporting
the quote is Copart's $10.50**, a strategic buyer's price for synergies it names (*"near-term cost and revenue synergies"*) —
not an owner-earnings value of ACV as it stands. The company's Adjusted EBITDA guide ($73-77M) capitalised at the sovereign
would be about $1.4bn, **and that figure treats $63M a year of stock pay as free and counts a lender's losses as
non-recurring**, which [E5-06] and [E2-57] forbid.

**WHICH BAR? NEITHER, and that is the finding.** The normal method [E4-11] needs a value to apply a margin to; the screamer test
[E4-01] needs a conservative case for the price to clear. **The conservative case is −$93.9M and the optimistic −$47.7M; the
price is above the whole range** — [E4-01]'s third outcome, *"no."* **Windage count: one** — the (c) judgment, displayed as a
band. The float exclusion and the floorplan provision are corrections of classification, not conservatism, and the as-filed
display is shown beside them; the grant-date SBC measure is reported, not stacked.

**PRICE AND PASS/FAIL, PLAINLY:** **$10.41 · market cap $1,767.9M · FAIL at Q2 (OUT, on the business).** **The quote is a
0.86% spread to Copart's $10.50 cash tender, not an owner-earnings price.**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened as a hold/sell question — there is no position and none is contemplated.** Recorded as refutation conditions,
pre-committed in writing per **[E1-02]** — *"I believe in establishing yardsticks prior to the act"* — so that a re-opening is
triggered by filed evidence, not by a price move or a bid.

**THE EVENT THAT GOVERNS FIRST.** **If the Copart tender closes, ACV ceases to be a public company and this file closes
permanently** — there is no equity left to analyse. **If the merger agreement terminates** (a Form 8-K Item 1.02, a Copart
statement that HSR failed, or the End Date passing), **Step 0 re-opens** (the ROKU treatment): the quote reverts toward an
unaffected price, and the conditions below govern whether Q2 re-opens.

**THESIS-BREAKING METRICS, each read off a 10-K, 10-Q or release, each with a threshold.** The file re-opens at Q2 if **three
or more** turn, and is re-read if any one does:

1. **Owner earnings positive for two consecutive fiscal years on this file's construction** (operating cash less the
   payables and trade-receivable lines, less floorplan provision, less note 13 SBC, less capex and capitalised software).
2. **Marketplace Units growth at or above OPENLANE's dealer consignment growth** for four consecutive quarters, both from the
   filed series. *(The pre-registered condition (b) of Q2.)*
3. **Auction fee per unit rising in a year in which units also rise and a fee increase is filed** — the price increase that
   shows per car, with volume.
4. **GAAP operating margin positive for a full fiscal year.**
5. **An organic unit figure disclosed** that shows organic growth above the dealer wholesale market's stated change.
6. **SBC (note 13 total) below 4% of revenue** for a full year with the share count not above the prior year's.
7. **CarGurus's exit holding as a pattern** — **no new national digital dealer-to-dealer entrant filing with the SEC for three
   years** while ACV's share gains show in units. *(The strongest fact against the verdict, pre-registered.)*

**THE DIRECTION OF THE MOAT, the monitoring question [E4-17, E3-30]:** is the narrowing of the losses cost leverage on a
position that is holding, or the ordinary arithmetic of a competitive marketplace growing into its overhead while a rival grows
faster? *"Beliefs change quite gradually"* [E4-17]; the slow instruments are **units against OPENLANE's dealer units**, **fee per
unit against units**, and **owner earnings ex-float**.

**Catalyst dates, all filed or contractual:** SC TO-T and SC 14D-9 (due within 7 business days of 2026-09-10 — the 14D-9's
Background of the Offer is this file's open Q3 work order) · tender expiry (at least 10 business days after commencement) ·
HSR waiting period · **expected close "by calendar year-end 2026"** · **End Date 2027-09-10**, extendable 180 days on HSR ·
2027-07-30, the latest Covenant Conversion Date · 2027-12-10, the warehouse revolving period's end.

**Position size:** none. **Reversal condition in words, not a price alert** (the QLYS ruling of 2026-09-07: a price alert on a
name that failed on the business is a category error).

**VERDICT: NOT REACHED — the file closed at Q2.**

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Step 0 → Q1 IN → Q2 OUT → file closed. Q3 and Q4 built under
      *"RECORDED, NOT GOVERNING"*; Q5 replaced by `COMPUTATION — NOT A CLEARANCE`; Q6 as refutation conditions only.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on filed documents; the private
      competitors (Manheim, America's Auto Auction, EBlock) sit at Q2 under the narrow-only rule, and Q2 is OUT.
- [x] **Every UNRESEARCHED item names the artifact and where it lives.** Four, none verdict-moving: the **SC 14D-9 Background of
      the Offer** (EDGAR, ACV CIK 0001637873, not yet filed at the run's fetch) — whether sale talks preceded the 2026-05-04
      severance agreements; the **2025-03-11 analyst-day materials** (company IR site; no 8-K furnished them); the **identity of
      the "anti-competition case"** (not in any filing read); **Manheim's financials** (Cox Enterprises, private — no document
      exists publicly, so strictly UNKNOWABLE for the row, adjudicated as a row limit).
- [x] **Every UNKNOWABLE verdict states what cannot be known** — none used.
- [x] **Step 0: the filing was read, with accession numbers; three figures cross-checked**, all exact (FY2025 OCF rebuilt from its
      detail lines; total revenue; SBC across cash-flow statement, supplemental and note 13). FY2021-23 cash-flow tags verified
      against the filed FY2022 and FY2023 statements. Peer cells cross-checked against OPENLANE's and Copart's filed figures.
- [x] **Owner earnings on a multi-year mean; fifteen windows and the TTM published; both (c) ends; the as-filed display beside
      the corrected construction; the (c), float and floorplan judgments disclosed.**
- [x] **Competitor row filled** (seven SEC filers; five ranked on margin, two retail principals shown and not ranked), the named
      competitors listed, three unpriceable, the limit stated; America's Car-Mart excluded as a customer class with its ground.
- [x] **Sovereign for the earnings currency (USD, note 19), from the issuing authority, dated 2026-09-11.**
- [x] **Value as a range — refused, with the reason** (every construction negative; the quote is a deal spread).
- [x] **One bar — neither applies**, stated; windage count one.
- [x] **Prices dated; aggregator for live quotes only, flagged.**
- [x] **Brief requirements discharged:** the payables flag reconciled (284.7%, FY2021, seller float); **customer funds established
      ON the balance sheet and INSIDE operating cash** and operating cash restated without them; the perimeter rebuilt from the
      notes ($280.1M gross — the investing line understated by 3.8%); both Item 1.01 8-Ks opened (the Copart merger agreement; the
      $50M ASR); SBC resolves and reconciles, the stock-settled bonus tested; SBC/OCF placed in the calibrated row (330.5%, a new
      high); the unit and fee-per-unit series built and split into volume and price; [E2-49] checked across vintages (fired);
      [E3-48] guidance against outturn; [E4-52] pay; the survival shape named against the five.
- [x] **Corrections recorded here rather than by editing history (operator rule 6):**
  1. **Two arithmetic slips fixed before the Step 0 commit (`776cbb9`):** an annualised spread first written as 3.5% (it is 2.9% to
     2026-12-31), and an ASR price range first written as "$5.84-$8.38" (the initial delivery averaged $5.72, per the 10-Q).
  2. **One figure fixed before the Q2 commit (`622a4fa`):** GMV per unit FY2019-22 was first written +95%; it is +121%.
  3. **Fixed before the Q3/Q4 commit (`6456222`):** revenue CAGR first drafted as 38.4% (38.7%); the revolver first described as a
     "$170M line" (it is $250M with $170M undrawn); and the bonus reconciliation first said the three differences "solve exactly",
     which three equations in three unknowns always do — reworded to what the test can show (it could have failed on sign, and did
     not).
- [x] **Run committed to git with a pathspec** — after Step 0 (`776cbb9`), Q1/Q2 (`622a4fa`), Q3/Q4 (`6456222`), and the close and fold.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** **ACVA FAILS at Q2 — OUT on the business.** A legible marketplace — an ~$420 fee on a ~$12,500 car, earned only on a
  sale — but ACV names three substitutes and OPENLANE and Copart each name ACV among theirs, and its customers owe it no volume
  **[E3-03]**; OPENLANE's dealer units grew 12.7% in H1-2026 against ACV's 1.6% **[E4-32, E4-55]**; the 2025 fee increases were
  industry-wide and the Q2-2026 increase did not reach the realised fee **[E2-44, E4-37, E3-61]**; seven years of operating losses,
  last of five marketplaces on owner-earnings margin (−3.1% latest, −9.2% five-year) **[E3-46]**; and growth took $280M of
  acquisitions (five of them physical auctions), $256M of stock pay and software on a sub-three-year life **[E2-44, E4-04]**.
  Recorded beneath: **the customer funds sit on the balance sheet and inside operating cash — every dollar of cumulative operating
  cash ever reported was seller float**; owner earnings −$93.9M to −$47.7M on fifteen windows and the TTM, never positive; SBC 330%
  of cumulative operating cash; a sixth survival shape, the borrowed balance sheet. **On 2026-09-10 Copart agreed to buy ACV for
  $10.50 cash. Price $10.41 · cap $1,767.9M · COMPUTATION — NOT A CLEARANCE: yield −2.70% to −5.31%, −8.1 to −10.7 points under the
  5.35% sovereign; the quote is a 0.86% merger spread.**
