# Company Run — DoorDash, Inc. (DASH) — 2026-09-18
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
## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended from scratch on 2026-09-18 (night, EDT); the template was copied and committed before any fetch (`e30b2f8`).
**This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the second name in the
"no share count from dei: read the cover" row (META was the first). Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-18 DASH/`. **No DASH row exists in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`**
(grepped: zero hits), so there is no screen row to carry. Every figure below is from DoorDash's own filings, fetched by this
run, with the accession.

### The entity, in every year used
CIK 0001792789, `submissions.json` (fetched by this run): *"DoorDash, Inc."*, SIC *"Services-Business Services, NEC"*,
`fiscalYearEnd` 1231 (correct: every 10-K reports a December 31 year end), one former name (*"DoorDash Inc"*, 2020-02-13 to
2021-02-24, a punctuation change). SEC `company_tickers.json`: *"{'cik_str': 1792789, 'ticker': 'DASH', 'title': 'DoorDash,
Inc.'}"*. One reporting entity throughout; IPO 2020-12-09 (*"33,000,000 shares of Class A common stock at the public offering
price of $102 per share"*, FY2022 10-K), so FY2020 is the first public year and FY2018-19 are pre-IPO figures carried in the
S-1-era comparatives. No shell, no reverse recapitalization (the DJT check does not apply).

**`submissions.json` gives `stateOfIncorporation` "NV", while every filing through the Q2 2026 10-Q says Delaware.** Both are
right: the 8-K of **2026-09-18** (accession `0001140361-26-037109`, Item 8.01): *"the reincorporation of the Company from the
State of Delaware to the State of Nevada (the " Nevada Reincorporation ") became effective on September 18, 2026, at 12:02 a.m.
Pacific Time"*, and *"the affairs of the Company ceased to be governed by the laws of the State of Delaware"*. It was approved
not at a meeting but by written consent of the founders and their trusts (8-K of 2026-08-11, `0001140361-26-032235`, Item 5.07:
*"certain stockholders ... holding at least a majority of the voting power ... adopted resolutions by written consent in lieu of
a meeting of stockholders"*; the Consenting Stockholders are Tony Xu, Andy Fang, Stanley Tang and their trusts), with an
information statement on Schedule 14C (DEF 14C, 2026-08-27, `0001140361-26-034688`). **The run is of the same company; the
charter that governs the share classes from today is the Nevada articles (Appendix C of the DEF 14C), read below. The
governance meaning is carried at Q3.**

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"no share count from dei: read the cover."* **A prompt to read, never a verdict.** The probe (`_probe_screen.py`,
copied from META's with the CIK changed; output `_probe_screen_output.txt`) shows companyfacts carries **one** dei element for
DoorDash, `EntityPublicFloat` (six facts, FY2021-25 10-Ks and the 10-K/A), and **no `EntityCommonStockSharesOutstanding` at
all**; `share_count_shift` returned **None** under both the current screen and the `a8bc84f` code (not measured, not stable: the
RIVN reading) and `shares_outstanding` returned None. **The META note's hypothesis (a dimensioned per-class cover) was tested on
the inline XBRL** of three filings (`dei.py`; raw documents `10Q_2026Q2_raw.htm`, `10K_FY2025_raw.htm`, `10KA_FY2025_raw.htm`),
and it holds, with one difference from META: **three classes, not two**. In the Q2 2026 10-Q (`0001792789-26-000050`):

- *"name="dei:EntityCommonStockSharesOutstanding" ... 408,992,917"* in context c-2, segment *"dimension="us-gaap:StatementClassOfStockAxis">us-gaap:CommonClassAMember"*, instant 2026-07-30;
- the same element in context c-3, *"us-gaap:CommonClassBMember"*, **24,302,737**;
- the same element in context c-4, *"us-gaap:CommonClassCMember"*, value tagged `format="ixt:fixed-zero"` over the word **"no"**.

The FY2025 10-K (`0001792789-26-000013`) and its 10-K/A (`0001792789-26-000035`) tag the same three dimensioned facts at
2026-02-12 (409,966,858 A; 24,459,494 B; zero C). **companyfacts publishes only undimensioned facts, so a cover tagged per class
never reaches it. For DASH the label was the META kind: a tagging convention for a multi-class cover (here three classes, one of
them empty), not a missing or stale count.** The other `a8bc84f` guards on facts filed by 2026-09-01: `scale_shift` **1.694**
(did not fire); `restatement_shift` (1.0, FY2019), a null and not a guard (the SNOW note). The `a8bc84f` `owner_earnings()`
priced the name (`{'5y_da': 68.0M, '5y_capex': 378.6M, '3y_da': 393.7M, '3y_capex': 838.0M}`), so **the count was the only
thing that stopped it.** The current screen prices it lower at the capex end (`5y_capex` 168.0M, `3y_capex` 579.7M) because it
now reads capitalised software as capital; that is not a verdict and is rebuilt from the filed statements at Q4.

**Restatement check:** the **10-K/A of 2026-05-06** exists and was read: *"We are filing this Amendment to correct a clerical
error in the report of KPMG LLP ("KPMG"), our independent registered public accounting firm"*; both covers leave the
error-correction box unticked (*"reflect the correction of an error to previously issued financial statements. ☐"*). No 10-Q/A
in the recent index. **No restatement of the business's figures exists.**

**One tag defect found and carried:** the current screen's `acquisition_flag` reports *"NET CASH INFLOW on the acquisition line
($4,222M ...)"* for FY2025, but the filed face reads *"Acquisitions, net of cash acquired | — | — | ( 4,151 )"* (FY2025 10-K).
The flag reads a sign or an element the face does not carry; the face is used. (Recorded under TOOLING NOTES.)

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this run
  at 23:07 EDT (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.29, '09/17/2026')** a second later (`step0_out.txt`): the stale-cache defect
  again (META recorded its seventh occurrence; this is the eighth recorded). The issuing-authority figure is used. FRED not
  used. Struck by this run, not inherited from the brief or from META.
- **Earnings currency: USD, with a growing foreign share.** The company reports in dollars; Wolt (from 2022-05-31) and Deliveroo
  (from 2025-10-02) earn in euros, sterling and other currencies (the geography split is read at Q1). No ADR or FX conversion of
  the quote applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$192.94, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("DASH", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 192.94,
  `regularMarketTime` 1789761601 = **16:00:01 EDT**, the closing print; the day's bar closes at 192.94 (range $192.35-$196.01).
  `tools/sources.price()` returned the same 192.94 stamped 2026-09-18.
- **The month, recorded rather than choosing a day:** 08-19 $220.22 · 08-26 $236.93 (the month's high close) · 09-01 $225.66 ·
  09-04 $211.73 · 09-08 $200.44 · 09-11 $201.95 · 09-17 $194.56 · 09-18 $192.94. **-19% from the 08-26 close.** The Q2 2026
  10-Q gives *"the closing price of the Company's Class A common stock of $ 184.53 on the last trading day of the quarter"*.
- **Primary-filing cross-check (Form 4s, `f4.py`, `form4_table.txt`):** Andy Fang sold on 2026-09-01 at $225.754-$232.231 in
  seven lots (`0001832390-26-000023`), inside Yahoo's 09-01 range ($225.26-$232.87); Stanley Tang sold on 2026-09-02 at
  $223.601-$227.229 (`0001832614-26-000032`), inside $222.11-$227.58; Gordon Lee sold 413 shares on 2026-09-04 at **$221.50**
  (`0001635648-26-000016`), inside $211.18-$222.05. **The aggregator's series is corroborated on three dates (inside the day's
  range; these are sales, not withholding at the close). No Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-07-30): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession, and the class treatment from the charter
- **Class A 408,992,917 + Class B 24,302,737 + Class C 0 = 433,295,654 shares**, from the cover of the **Form 10-Q for the
  quarter ended 2026-06-30, filed 2026-08-05, accession `0001792789-26-000050`**, the latest periodic filing: *"The registrant
  had outstanding 408,992,917 shares of Class A common stock, 24,302,737 shares of Class B common stock, and no shares of Class
  C common stock as of July 30, 2026."*
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q's face: *"408,925 Class A shares issued and outstanding
  as of ... June 30, 2026"* and *"24,331 Class B shares"* (thousands); the cover moves +68K A and -28K B in thirty days (B
  converting to A on founders' sales, above). The equity statement: *"Balances as of June 30, 2026 | $ | 11 | 433,256"*
  (thousand shares, all classes), against 433,296K on the cover. **Consistent.**
- **Why the classes are added, one for one.** The governing charter from 2026-09-18 is the Nevada Articles of Incorporation
  (DEF 14C Appendix C): *"2. Identical Rights . Except as otherwise provided in these Articles of Incorporation or required by
  applicable law, shares of Common Stock shall have the same designations, limitations, restrictions and relative rights
  (including as to dividends and other distributions, and any liquidation, dissolution or winding up of the Corporation but
  excluding voting and other matters as described in Section V.3 below), share ratably and be identical in all respects as to
  all matters"*; dividends *"paid pro rata, on an equal priority, pari passu basis"* (2.1) and liquidation *"distributed on an
  equal priority, pro rata basis to the holders of Common Stock"* (4), each unless the adversely treated class approves
  otherwise by separate class vote; splits must apply to all classes alike (2.3). Conversion: *"Each share of Class B Common
  Stock will automatically convert into one fully paid and nonassessable share of Class A Common Stock on the Final Conversion
  Date"* (5.1), and on any transfer to a non-Permitted Transferee (5.2(b)). The Delaware certificate it replaced carried the
  same clause (*"shall have the same rights and powers, rank equally ... share ratably and be identical in all respects"*,
  DEF 14C Appendix E, the Delaware certificate reproduced there, page E-5 onward). The one difference is votes: *"(a) Class A ... one vote"*,
  *"(b) Class B ... twenty votes"*, *"(c) Class C ... no voting rights"* (3.1). **Economically identical, so the cash-flow
  claim is the sum; the votes belong at Q3 (control), not in the count.**
- **Sold after the cover date: nothing found.** No equity offering, S-3 or 424B in the index after 2026-07-30; post-cover Form
  4s are founders' and officers' sales of existing shares (above). Buybacks: 6.8M shares at $155.25 in H1 2026 ($1.0bn),
  retired (10-Q Note 11), before the cover date.
- **Dilution not in the count:** **26,732 thousand unvested RSUs** at 2026-06-30 (including the CEO Performance Award's
  9,341,100 eligible PSUs) and 2,067 thousand options at a weighted $7.10 (10-Q Note 11): 6.6% of the cover count. The 2030
  convertible notes ($2.75bn, conversion price about $291.97, principal settled in cash) are out of the money, hedged to
  $291.97 and capped by warrants struck at $512.225 (about 9.4M shares each side). Shown beside the cap, not in it.

### The market cap
**$192.94 x 433,295,654 = US$83.60bn** (Class A $78.91bn; Class B at the Class A price, $4.69bn, which the charter's
identical-rights clause licenses). **With unvested RSUs and options: $89.16bn.** Split factor 1.0. Public float on the FY2025
10-K cover: $90.8bn at 2025-06-30 (companyfacts, the one dei element).

### THE DEAL CHECK: none live on the registrant as target
`sources.deal_filings("0001792789")` returned `([], [], '2026-02-18')` and `deal_note` returned empty (`step0_out.txt`). Read on
the recent submissions index (2022-04 to 2026-09): the only 425s are of **May 2022**, the Wolt stock acquisition (closed
2022-05-31); **no 425, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D on this registrant since.** The Deliveroo offer ran under the
UK Takeover Code (8-Ks of 2025-05-06, `0001140361-25-017438`, and 2025-10-02, `0001140361-25-037039`), with DoorDash as buyer.
The one corporate action live today is the Nevada conversion, completed. **The quote is not a spread and buys this company.**

### The perimeter: what (c), the five-year mean and the cap must see
- **Wolt Enterprises Oy, closed 2022-05-31, paid in stock:** *"on May 31, 2022, the Company acquired Wolt Enterprises Oy (Wolt)
  in a business combination for $2,838 million"* (FY2022 10-K, auditor's critical audit matter); the cash-flow face shows *"Net
  cash acquired (used) in acquisitions | ( 28 ) | — | 71"* (FY2020/21/22), so the consideration was shares and never touched the
  cash-flow statement. **Inside every window from FY2022 on**; FY2021 is DoorDash alone.
- **SevenRooms, closed 2025-06-13, for cash:** *"Cash | $ | 902 | Deferred cash consideration | 250 | Total consideration | $ |
  1,152"*; goodwill $886M; revenue since acquisition *"not material"* (FY2025 10-K Note 4).
- **Deliveroo plc, closed 2025-10-02, for cash:** *"the Company acquired Deliveroo plc (Deliveroo) in a business combination for
  $3,724 million"*; *"eligible Deliveroo shareholders were entitled to receive 180 pence in cash for each Deliveroo share held"*
  (8-K 2025-10-02); goodwill $1,950M, intangibles $1,498M (lives 2-11 years), contingent liabilities $102M *"relate to
  outstanding legal provisions"*; revenue and net loss since acquisition *"$ 347 million and $ 49 million"*; pro forma FY2024
  revenue $11,984M against the reported $10,722M, FY2025 $14,743M against $13,717M (FY2025 10-K Note 4). Funded from cash and
  the **$2.75bn 0% Convertible Senior Notes due 2030** (May 2025; *"Proceeds from issuance of convertible notes, net of issuance
  costs | ... | 2,720"*), with a $680M note hedge and $341M of warrants. The face: *"Acquisitions, net of cash acquired | — | —
  | ( 4,151 )"* (FY2025).
- **HOW THE SPLICE IS HANDLED.** The five-year window FY2021-25 contains DoorDash alone (FY2021), DoorDash plus seven months of
  Wolt (FY2022), DoorDash plus Wolt (FY2023-24), and FY2025 with SevenRooms for 6.5 months and Deliveroo for one quarter. **No
  pro forma operating cash exists for any year** (the 10-K gives pro forma revenue and net income only; Deliveroo's own
  statements are filed in the UK, not with the SEC). So the run does **not** build a pro forma mean. It (i) computes owner
  earnings on the reported consolidated figures, (ii) charges the **cash** acquisitions ($4,151M in FY2025 plus the $20M
  deferred and later payments) in a separate column so the reader sees the mean with and without them (the SPGI and AEHR
  practice), (iii) records the Wolt stock consideration ($2,838M) as a share-count cost already inside the cover count, and
  (iv) reads H1 2026 (the first half-year with all three businesses inside) separately, because it is the only filed period
  that is not a splice.
- **Cash and liquidity at 2026-06-30** are read at Q4.

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2025 Form 10-K**, filed **2026-02-18**, accession **`0001792789-26-000013`** (`10K_FY2025.txt`), its **10-K/A** of
  2026-05-06 (`0001792789-26-000035`, the KPMG clerical correction), and the **Q2 2026 Form 10-Q**, filed **2026-08-05**,
  accession **`0001792789-26-000050`** (`10Q_2026Q2.txt`).
- Also read: the FY2022, FY2023 and FY2024 10-Ks (`0001628280-23-005131`, `0001628280-24-005600`, `0001628280-25-005715`); the
  Q3 2025 and Q1 2026 10-Qs (`0001792789-25-000020`, `0001792789-26-000037`); the DEF 14A of 2026-04-20
  (`0001792789-26-000018`); the DEF 14C of 2026-08-27 with the Nevada articles; the 8-Ks of 2025-05-06, 2025-05-27, 2025-05-28,
  2025-06-02, 2025-10-02, 2026-06-12, 2026-08-11 and 2026-09-18; the 8-K EX-99.1 earnings releases (listed at Q3); four Form 4s.
- **Figures cross-checked against the filed statement** (FY2025 10-K consolidated statement of cash flows, $M, FY2023/24/25):
  *"Net cash provided by operating activities | 1,673 | 2,132 | 2,431"*, *"Stock-based compensation | 1,088 | 1,099 | 1,051"*,
  *"Depreciation and amortization | 509 | 561 | 747"*, *"Purchases of property and equipment | ( 123 ) | ( 104 ) | ( 257 )"*
  and *"Capitalized software and website development costs | ( 201 ) | ( 226 ) | ( 348 )"* match companyfacts (`ocf`,
  `sbc_annual`, `da_annual`, `annual(CAPX_TAGS)`, and `capital_acquired` = the two capital lines summed: 324, 330, 605) to the
  million. The FY2022 10-K face (FY2020/21/22: operating cash 252, 692, 367; SBC 322, 486, 889) matches likewise. Revenue
  $8,635M / $10,722M / $13,717M matches.

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in
> character. If a business is complex or subject to constant change, we're not smart enough to predict future cash
> flows."* **[E3-31]**

### What the filings show, in my own words, without management's language
A person orders a meal or a basket of groceries in an app. DoorDash takes the order to a restaurant or shop, sends an
independent courier to collect and deliver it, charges the customer a delivery fee and a service fee, charges the
merchant a commission on the basket, and pays the courier. **Revenue is what it keeps**: the customer's fees plus the
merchant's commission, **net** of the courier's pay and of refunds and credits (*"We typically earn a fee from merchants
for the services we provide based on the size of each transaction"*; consumers pay *"a fixed delivery fee and a service
fee that varies based on the size of the transaction"*, FY2025 10-K Item 1). On top sit a subscription (DashPass, Wolt+,
Deliveroo Plus: a monthly fee in exchange for lower delivery and service fees), advertising sold to merchants and
packaged-goods makers, white-label delivery for merchants' own channels (Drive) and merchant software (reservations since
SevenRooms). The costs that remain are customer support, payment processing, insurance, the engineers, sales and
marketing, and promotions. **So each order is: basket x (commission + fees) minus courier pay minus refunds; the business
earns a thin margin on a very large volume.** The filed series, FY2020-H1 2026 (10-Ks and 10-Q; FY2020-21 from the FY2022
10-K):

| | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Total Orders (M) | 816 | 1,390 | 1,736 | 2,161 | 2,583 | 3,172 | 970 |
| Marketplace GOV ($M) | 24,664 | 41,944 | 53,414 | 66,771 | 80,231 | 102,018 | 33,078 |
| GOV per order ($, computed) | 30.23 | 30.18 | 30.77 | 30.90 | 31.06 | 32.16 | 34.10 |
| Net Revenue Margin (revenue / GOV) | 11.7% | 11.7% | 12.3% | 12.9% | 13.4% | 13.4% | 13.5% |
| Revenue ($M) | 2,886 | 4,888 | 6,583 | 8,635 | 10,722 | 13,717 | 4,454 |
| GAAP income (loss) from operations ($M) | | (452) | (1,124) | (579) | (38) | 723 | |

FY2025 revenue: United States $11,460M (83.5%), International $2,257M (FY2025 10-K Note 3; *"No individual country
outside the United States represented 10% or more"*). FY2025 GOV growth was 27%, *"23% Y/Y excluding the impact of
Deliveroo"*; Q2 2026 GOV +36%, *"23% Y/Y excluding the impact of Deliveroo"* (EX-99.1s of 2026-02-18 and 2026-08-05).
The company made its first full-year GAAP operating profit in FY2025, **0.71% of GOV**.

**The scarce input the business controls:** density. In any one town, the number of merchants listed, customers ordering
and couriers idle at the same time determines how fast and cheaply an order is fulfilled, and density is what a new
entrant lacks. **What it does not control, on its own filing:** the loyalty of any of the three sides (*"It is relatively
easy to switch between offerings in our industry"*, Item 1A, read at Q2), the courier's legal status and pay floor
(Proposition 22 in California, the New York City minimum-pay rule of December 2023, the EU platform-work rules for Wolt and
Deliveroo riders, Item 1A), and the merchants, who can leave on *"at least 7 or 30 days' advance notice"* (Item 1A).

**Will the fundamentals look broadly the same in ten years?** The mechanism (take a cut of a delivered basket, pay a
courier) has not changed in the filed record. Two things in the company's own words argue that it may: *"Local on-demand
delivery services for food and the other areas in which we compete are nascent, and we cannot guarantee that they will
stabilize at a competitive equilibrium that will allow us to maintain or increase profitability"* (FY2025 10-K Item 1A),
and the company is investing to replace the courier with *"our autonomous delivery platform"* (Q4 2025 EX-99.1) while it
rebuilds *"significant portions of our products using our new global technology platform"*, to be *"fully rolled out ...
in the first half of 2027"* (Q2 2026 EX-99.1).

### THE CASE FOR UNKNOWABLE, AT FULL STRENGTH **[E4-26, E4-51]**
(1) The filer says the industry has not reached an equilibrium and may not reach one that lets it keep its profit: that
is [E3-31]'s *"subject to constant change"* in the company's words. (2) Autonomy, if it works, removes the largest cost
in the order (couriers earned *"over $20 billion"* in 2025, FY2025 10-K) and would reset who earns what; no filing gives
it a revenue or cost line. (3) The company's profit history is one year long (operating losses every year to FY2024).

**Why it does not carry, and what is excluded.** HHH, RGTI and DJT closed at Q1 because the declared business was not the
filed one. **Here the filed business is the declared one**: nearly all revenue is fees and commissions on delivered
orders, with a filed volume series (orders), a filed value series (GOV) and a filed margin series (Net Revenue Margin)
in every year FY2020 to H1 2026, and I can state the unit economics from them. **What is outside the circle is named:
autonomous delivery, the AI products, and the future economics of grocery and international markets that the company
says are not yet profitable** (*"We currently expect unit economics in our grocery and retail categories to turn positive
in 2H 2026"*, Q4 2025 EX-99.1). [E4-46] says study will not repair those; they are recorded as outside the circle and
**cannot be counted at any later gate**. Their cost is being paid now and is carried at Q2 ([E4-04]) and Q4. **Whether an
industry the filer calls nascent and short of equilibrium gives this company a position is the Q2 question, and it is
carried there, not decided here.**

- **VERDICT: [x] IN** on the business the filings show (a delivery marketplace earning fees and commissions net of courier
  pay, 3.2 billion orders and $102.0bn of GOV in FY2025). **Not IN** for autonomy, AI products, and the future profitability
  of grocery, retail and international: outside the circle [E3-31, E4-46], never counted later; their cost is carried at
  Q2 and Q4.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its customers to have **no close
> substitute** and; (3) is not subject to price regulation."* **[E3-03]**, 1991 letter

### THE HYPOTHESIS TO BE REFUTED, AT FULL STRENGTH **[E4-26, E4-51]**
DoorDash is the largest delivery marketplace filing with the SEC: **$102.0bn of GOV in FY2025 against Uber's $90.9bn of
Delivery Gross Bookings and Instacart's $37.2bn of GTV** (row below). Its volume has grown every year (orders 816M to
3,172M, FY2020-25) while the share of each basket it keeps **rose** from 11.7% to 13.4% (FY2021-25) and average GOV per
order rose from $30.18 to $32.16; that looks like [E2-44]'s first half (price with volume). It became profitable in FY2025
on the GAAP line, and its working capital is funded by merchants and couriers (accrued liabilities of $5,747M at
2026-06-30 against receivables of $1,100M, 10-Q face), so its return on tangible operating capital is not even finite. A
density network that feeds on itself (*"An increase in merchants attracts more consumers to our platform and an increase in
consumers attracts more merchants"*, Item 1A) is the textbook case for a local-dominance position [E2-53]. If any delivery
business is a franchise, this is the candidate.

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES.** 3,172M orders in FY2025, +23%; 970M in Q2 2026, +27% (+17% excluding Deliveroo); over 56
  million monthly active users and over 35 million paid members at 2025-12-31 (FY2025 10-K).
- **(3) Not subject to price regulation: NO, IN PART, and the filer says the regulation reaches price.** The FY2025 10-K
  lists among its forward-looking risks *"regulations regarding the classification of and the rates that we pay Dashers ...
  and regulations impacting the commission rates we charge to merchants"*; *"some jurisdictions in which we operate have
  established minimum earnings standards for certain delivery workers, including Dashers ... These minimum earnings
  standards and similar regulations have caused, and may in the future cause, us to increase the fees we charge to
  consumers and merchants"*; *"in December 2023, a New York City rule mandating certain minimum earnings standards for
  certain food delivery workers took effect"*; and in the FY2022 10-K, on Proposition 22: *"To offset a portion of these
  increased costs, in certain circumstances we charge higher fees and commissions, which could result in lower order
  volumes over time."* The Q4 2025 release names *"an annual increase in cost in regulated markets"*. **A regulator sets a
  floor under the largest cost and, in some cities, a ceiling on the commission; the price the company can charge is set
  partly by the regime [E2-59].** Recorded as a cap, not the ground of the verdict.
- **(2) No close substitute: NO, on three independent records.**
  1. **The company's own filing, FY2025 10-K Item 1A:** *"It is relatively easy to switch between offerings in our
     industry. Consumers have a propensity to shift based on cost, quality, and selection and could use more than one local
     commerce platform; independent contractors who provide delivery services could use multiple platforms concurrently as
     they attempt to maximize earnings; and merchants could prefer to use the local commerce platform that offers the lowest
     commission rates and adopt more than one platform to maximize their volume of orders."* And on price: *"Many of our
     competitors are well capitalized and may offer discounted services, lower merchant commission rates and consumer fees
     ... Such competitive pressures have led us, and may lead us in the future, to change our commission rates and fees or
     change our incentives, discounts, and promotions to remain competitive. Such efforts have negatively affected, and will
     likely continue to negatively affect, our financial performance."* **All three sides of the market multi-home, in the
     filer's own words, and the filer says competition has already moved its price.**
  2. **A competitor of almost equal size, in its own filing, names DoorDash and says the same about switching.** Uber's FY2025
     10-K (`0001543151-26-000015`): *"Our Delivery offering competes with numerous companies ... including DoorDash,
     Instacart, Gopuff, Rappi, Delivery Hero, Just Eat Takeaway, and Amazon"*, in industries with *"low barriers to entry, low
     switching costs, and well-capitalized competitors in nearly every major geographic region"*. Uber's Delivery Gross
     Bookings were **$90.9bn in FY2025 (+21.8%) and $53.5bn in H1 2026 (+26.9%)** (quarterly table, FY2025 10-K and Q2 2026
     10-Q): a substitute at 89% of DoorDash's volume, growing about as fast as DoorDash does without Deliveroo. Instacart's
     FY2025 10-K names *"local on-demand delivery companies such as DoorDash, Uber Eats via Uber's native applications, and
     Grubhub (acquired by Wonder)"* as competitors to its restaurant offering. **[E2-45]'s attacker's test was run by a real
     attacker**: Uber built a delivery business at nine-tenths of DoorDash's scale inside the filed decade.
  3. **The price series, read for what drove it rather than its direction [E4-38, E4-55].** The rise in Net Revenue Margin is
     explained by the filer, every year, as **efficiency and advertising, not price**: FY2023 *"primarily due to improved
     logistics efficiency and quality, as well as increasing contribution from advertising revenue"*; FY2024 *"primarily due
     to an increased contribution from advertising revenue"*; FY2025 *"consistent with 2024"*, revenue outpacing GOV
     *"primarily due to improved logistics efficiency, increasing contribution from advertising revenue, and a reduction in
     credits and refunds"*. Because revenue is **net of courier pay**, cheaper delivery raises the margin with no change in
     the price anyone pays. And the company's growth engine is a price **cut**: *"Because DashPass lowers consumer fees, it
     typically drives an increase in average consumer order frequency and retention, but it does so at a lower gross margin
     percentage compared to non-DashPass orders. We are happy to make this trade"* (Q2 2026 EX-99.1), with *"approximately
     75% of Total Orders in our U.S. grocery and retail categories"* placed by members. **Average GOV per order rose 6.5% in
     five years (FY2020-25), below inflation; the unit that grew is orders, bought partly with lower fees.**

### [E4-04]: MUST THE MOAT BE CONTINUOUSLY REBUILT?
The test v4 sets: does a lapse in spending destroy the structure or narrow it, and does the spending defend the same
advantage or buy its replacement? **Both answers go the wrong way here.** (a) **The courier side is bought again with every
order**: couriers *"could use multiple platforms concurrently as they attempt to maximize earnings"*, so supply is held only
by current pay (*"We must provide Dashers with opportunities to earn that are competitive with alternative opportunities"*,
FY2025 10-K Item 1). (b) **The merchant side can leave in a week or a month** (*"at least 7 or 30 days' advance notice"*),
and *"merchants could prefer to use the local commerce platform that offers the lowest commission rates"*. (c) **The
customer side is held with fee reductions** (DashPass, above) and promotions. A lapse in any of the three is not a
narrowing: the filer says each side moves to whoever pays or charges better. (d) **The company is now buying a replacement
basis**: a rebuilt global technology platform, autonomous delivery, AI features, with D&A guided to *"approximately $1.1
billion to $1.2 billion"* in 2026 against $747M in FY2025 and capitalised software rising from $53M (FY2020) to $348M
(FY2025) (Q4 2025 EX-99.1; cash-flow faces). The density advantage is real, but on the filer's own description it is
**defended by continuous payment on three sides**, which is Munger's competitive destruction and not a moat that stands
when spending stops [E4-04, E3-51].

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4; the corpus's own test is pricing conduct plus returns on capital [E3-43])*
Same window (FY2023-25, H1 2026 growth), each figure from the filer's own 10-K or 10-Q, fetched by this run (`peers/`).

| Company (filing) | volume FY2025, growth FY2025; H1 2026 | revenue / volume FY2023-24-25 | profit / volume FY2023-24-25 | owner cash / volume FY2023-24-25 |
|---|---|---|---|---|
| **DASH** (10-K `0001792789-26-000013`, 10-Q `-26-000050`) | GOV $102.0bn, +27.2% (+23% ex-Deliveroo); Q2 2026 +36% (+23% ex-Deliveroo) | 12.9% / 13.4% / 13.4% | GAAP operating income -0.87% / -0.05% / **0.71%**; Adjusted EBITDA 1.78% / 2.37% / 2.72% | **0.39% / 0.88% / 0.76%** (0.15% / 0.67% / 0.57% after SBC capitalised into software) |
| **UBER Delivery segment** (10-K `0001543151-26-000015`, `-25-000008`; 10-Q `-26-000032`) | Gross Bookings $90.9bn, +21.8%; H1 2026 +26.9% | 19.2% / 18.4% / 19.0% (not like-for-like: Uber books delivery revenue gross in some markets, *"present the respective Mobility and Delivery revenue on a gross basis"*) | Segment Adjusted EBITDA 2.36% / 3.31% / **3.93%**; H1 2026 3.77% (the filed ASC 280 segment measure; excludes corporate G&A, platform R&D, SBC and D&A, so it overstates against DASH's company-wide figure) | not filed at segment level |
| **CART** Instacart (10-K `0001579091-26-000018`, 10-Q `-26-000042`) | GTV $37.2bn, +11.2%; H1 2026 +13.4% | 10.0% / 10.1% / 10.1% (transaction revenue 7.2% throughout) | GAAP operating income -7.06% (IPO stock charge) / 1.46% / **1.34%**; Adjusted EBITDA 2.11% / 2.64% / 2.92% | -7.33% (IPO) / 0.97% / **1.50%** |
| **Deliveroo plc**, pre-acquisition, from DASH's own Note 4 | FY2024 revenue about $1,262M implied (pro forma $11,984M less DASH's $10,722M) | n/a | pro forma net income FY2024 $220M lower than DASH alone (includes purchase-accounting amortization) | not filed with the SEC |

**Owner cash** = operating cash less stock compensation less purchases of property and capitalised software (the same
construction for both filers that file it). **Peers taken: three SEC filers plus Deliveroo through DASH's own note, of
the eight the filers name** (Amazon, Uber, Prosus/Just Eat Takeaway, Delivery Hero, Instacart, Gopuff, Rappi, Grubhub).
Not taken: **Delivery Hero** (Frankfurt), **Prosus/Just Eat Takeaway** (Euronext), **Meituan** (Hong Kong) file nothing with
the SEC; **Grubhub** is private under Wonder; **Gopuff** and **Rappi** are private; **Amazon** does not segment delivery.
The class is not held PROVISIONAL on their absence, because the verdict rests on criterion (2) in the subject's own words
and in the largest peer's, not on a ranking the missing filers could reverse.

**What the row shows.** DoorDash is **first on volume, first on growth, and last or second-last on profit and owner cash per
dollar of volume**. Instacart, at 36% of its size, keeps **1.50 cents of owner cash per dollar of GTV to DoorDash's 0.76**,
and earns 1.34% on GAAP operating income to DoorDash's 0.71%. **Direction [E4-32]**: all three profit lines rose together
over FY2023-25 (DASH +0.94 points, Uber +1.57, Instacart +0.81 on Adjusted EBITDA per volume), so the margin gain is
industry-wide, not DoorDash pulling away; Uber's delivery margin widened fastest. **The row's limit [E3-61]:** it shows
position, not conduct, and it cannot show the U.S.-only share that a local-dominance claim would need (no filer publishes
it; DoorDash's 10-K makes no market-share statement, grepped).

### THE OTHER Q2 TESTS
- **Returns on capital, asked about the business [E3-46]:** net income attributable to common holders **-8.2% / 1.7% / 10.5%**
  of average equity (FY2023-25: $(558)M, $123M, $935M on $6,780M, $7,305M, $8,918M), the FY2025 figure including a one-time
  release of *"a portion of the U.S. valuation allowance"* (FY2025 10-K MD&A); accumulated deficit **$4,986M** at 2026-06-30.
  On tangible operating capital the return is not finite, because merchants and couriers fund the working capital: that is
  real, and it is what a pass-through intermediary looks like, not evidence that the intermediary cannot be replaced.
- **[E2-44], both halves:** price with flat demand and idle capacity: **not shown**; the filer ties price rises to lost volume
  (*"could result in lower order volumes over time"*, FY2022 10-K) and grows by lowering fees (DashPass). Growth with minor
  capital: capex plus capitalised software $605M in FY2025 on $102.0bn of GOV, so **the second half passes**, which is why
  this business is not the gruesome kind (Q4).
- **[E4-37] agony pricing:** the filer's own sentence, *"Such competitive pressures have led us ... to change our commission
  rates and fees ... Such efforts have negatively affected ... our financial performance"*, is the prayer session in writing.
- **[E3-33] untapped pricing power / [E5-28]:** claiming it would be claiming near-monopoly, and the peer row (Uber at 89% of
  volume) and the filer's switching sentence refute it.
- **[E2-53] the dominance class:** position would have to set the economics regardless of execution. The filer says the
  opposite: the industry is *"nascent"* and may not *"stabilize at a competitive equilibrium that will allow us to maintain
  or increase profitability"*.
- **[E4-36] which cause of success:** the record is extreme performance over many factors (execution in logistics, density,
  membership), which the corpus lists as a cause and which is not ownable the way a trademark is; the courier-cost gains
  flow partly to customers through DashPass (the [E3-62] second step: *"how much is going to stay home and how much is just
  going to flow through to the customer"*).
- **[E4-23] key person:** the co-founder holds 54% of the votes (Q3); the filings do not show that the economics depend on
  him. Not recorded as a moat defect.

### CLASS AND VERDICT
- Needed or desired **[x]** · no close substitute **[ ]** · not price-regulated **[ ]** (caps and floors in regulated markets)
- Class: **[ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL** as a franchise; a real scale and density **position** in a market
  the filer calls easy to switch. Direction: margins rising, but industry-wide (Uber fastest), not a widening moat.
- **VERDICT: [x] OUT, ON THE BUSINESS. Permanent.** Criterion (2) of **[E3-03]** fails on three independent records: the
  company's own Item 1A (*"It is relatively easy to switch between offerings in our industry"*; all three sides
  multi-home; competitive pressure *"led us ... to change our commission rates and fees"*); the largest peer's own 10-K
  (Uber names DoorDash first among its delivery competitors, in industries with *"low switching costs"*, at $90.9bn of
  bookings, 89% of DoorDash's volume); and the price series, whose rise the filer attributes to efficiency and advertising
  while it grows by lowering fees. **[E4-04]** fails too: each of the three sides is held by payment renewed with every
  order, and a replacement technology base is being bought now. Criterion (3) is capped by minimum-pay and commission
  regulation [E2-59]. **The file closes here.** Q3 to Q6 are recorded below, **not governing**, as recent runs have done.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**RECORDED, NOT GOVERNING. The file closed at Q2 on the business.** Q3 to Q6 are recorded because the evidence was
gathered and a later reader should not have to fetch it again; none of them can reopen the file, and IN here would not
promote the name [E2-37, E3-39].

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution** **[E3-38]**: an undifferentiated service run at a GAAP operating margin of 0.71% of GOV (FY2025);
  every order is priced, routed and paid in real time on three sides that the filer says can switch. A dispatch or pricing
  error repeated for a quarter moves the whole year's profit. This is have-to-be-smart-every-day.
- [ ] **Control [E1-16]**: a minority buyer of Class A, not an owner of the whole; not engaged. (The founders' control is read
  below as a fact about the owners' position, not as this determinant.)
- [ ] **Leverage [E3-29]**: $2.75bn of 0% convertible notes against $6.2bn of cash and investments; not engaged.
- **Case declared: a GATE**, on daily execution.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
- **New York Attorney General, Assurance of Discontinuance No. 25-007, effective 2025-02-24** (fetched from the AG's own
  server, `NYAG_AOD_2025.pdf`/`.txt`; the PDF text carries OCR-style artifacts such as *"Att01ney"* and *"Libe1ty"*, flagged
  and not smoothed). The AG's findings: *"Throughout the Relevant Period, DoorDash employed a guaranteed pay model that
  subsidized a portion of the company's payments to Dashers with consumer tips"*; *"for the typical order, the consumer's tip
  made no difference at all to the Dasher's pay"*; and *"During the Relevant Period, DoorDash made misleading and ambiguous
  representations to consumers and Dashers, and omitted material information to consumers and Dashers"* (Relevant Period
  *"approximately May 2017 through September 2019"*). *"DoorDash does not admit the findings made by the OAG"* (para. 14).
  $16,750,000 to Dashers as restitution; an injunction to keep tips *"distributed to Dashers in their entirety"* in New York.
  **Public from 2025-02-24** (the conduct from 2017-2019; press criticism of the model in 2019, when the period ends).
- **What the company files about it**, Q2 2026 10-Q Item 1A: *"under a former pay model for Dashers in the United States, we
  would increase the amount paid to Dashers on a delivery in cases when a consumer left little or no tip. Although this
  additional pay was intended to help Dashers by making every delivery economically worthwhile, it also had the effect of
  causing some people to be under the misimpression that not all tips were being received by Dashers. Government
  authorities have brought claims against us related to that former Dasher pay model."* **The candor read [E2-26, E2-68]:**
  the AG's finding is that the tips *"typically subsidized guaranteed pay"*, i.e. that the impression was correct; the filing
  describes a correct impression as a misimpression and names none of the authorities. That is a direction-of-deviation read
  [E2-69], recorded as a prompt, not a finding of personal misconduct: the AG made no finding against a named person,
  and no admission was made.
- **The other authorities are not named in any filing read.** The District of Columbia Attorney General's suit over the same
  pay model is known to this run only from the 10-Q's plural (*"Government authorities have brought claims"*), not from a
  document read. **Can I name the document that would resolve it? Yes**: the D.C. Superior Court complaint and consent
  judgment in *District of Columbia v. DoorDash*, and the record of when management learned the model was misread and when
  it changed it (the September 2019 end of the Relevant Period is the only date on file). **[E5-22]**: the test is not the
  penalty's size but whether *"they didn't act when they learned"*.
- **Worker classification and regulators:** the California EDD assessment of January 2023 for payroll taxes (*"the Company
  has recorded an accrual for this matter"*, Q2 2026 10-Q Note 9); PAGA and arbitration claims; *"regulatory and administrative
  investigations ... concerning the Company's business practices, the classification and compensation of Dashers"*. These
  are disputes about a business model's legal status, read at Q4 as exposure, not as conduct.
- **The founders' control, and today's change of charter.** Class B carries twenty votes; *"Tony Xu ... Andy Fang ... and
  Stanley Tang ... collectively held 54% of the voting power"* at 2026-06-30, with Mr. Xu directing the other founders' votes
  under the Voting Agreement (Q2 2026 10-Q Item 1A). On 2026-08-06 the founders approved by written consent, with no meeting
  and no vote of the public holders, the conversion of the company to a Nevada corporation, effective **2026-09-18** (8-Ks of
  2026-08-11 and 2026-09-18). The information statement describes what the minority gives up in its own words: *"NRS 78.240
  also provides that the only fiduciary duty owed by a controlling stockholder is to refrain from exerting undue influence
  over a director or officer with the purpose and proximate effect of inducing a breach of fiduciary duty by such director or officer"* (a narrowing the DEF 14C sets beside Delaware's
  standard), and *"the Nevada Supreme Court has previously clarified that Nevada's codified business judgment rule, and not an
  "entire fairness" standard, applies to judicial review of director and officer actions in the context of a transaction
  involving a controlling stockholder"* (DEF 14C, 2026-08-27, "Fiduciary Duties and Business Judgment"). The Nevada articles
  also deny Class A a class vote under NRS 78.2055(3), 78.207(3) and 78.390(2) (Nevada articles, Article V, section 3.1(a) and (c), DEF 14C Appendix C).
  **[E3-59]'s second yardstick, *"how well that they treat their owners"***: a controlling holder, whose own pay vests on the
  share price (below), moved the company by his own written consent to a law that narrows his duties to the minority. Legal,
  disclosed, and a prompt at the highest level this file records; not a finding of misconduct.
- **VERDICT ON THE BINARY (RECORDED, NOT GOVERNING): UNRESEARCHED** - work order: the D.C. Superior Court complaint and
  consent judgment in *District of Columbia v. DoorDash* (D.C. Superior Court docket; the D.C. OAG's site), and the 2019
  record of when the tip model's effect was known internally and when it was changed.

### THE INCENTIVE READ **[E4-27]**
The CEO received no equity in 2025; his whole incentive is the **2020 CEO Performance Award**: 10,379,000 RSUs in nine
tranches *"eligible to vest based on the achievement of stock price goals measured using an average of our stock price over a
consecutive 180-day period"*, performance period ending **2027-11-23**; two tranches vested in 2025 at 180-day averages above
*"$187.60 and $226.80 per share"*; *"No additional tranches ... will vest unless our stock price ... is $265.80 per share, and
the 2020 CEO Performance Award will vest in full only if our stock price is $501.00 per share"* (DEF 14A 2026-04-20). **Pay
vests on the share price and on nothing the capital earns.** Seven tranches (9,341,100 RSUs) remain, and the deadline is
fourteen months away. **[E3-50] fires as a prompt**: the stock-price-targeting premise is built into the CEO's only award.
Set beside the buybacks below (Q2 2026, $887M at $156.88), the prompt is live; no finding that repurchases were timed to
the award is made or supportable from the filings.

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [x] **EBITDA / adjusted-earnings promotion [E4-29, E5-41]: FIRES at full strength in the 8-K releases.** Guidance is given
  **only** in Marketplace GOV and Adjusted EBITDA (Q4 2025 EX-99.1: *"Q1 2026 | $31.0 billion - $31.8 billion | $675 million -
  $775 million"*), and the Q2 2026 release's fifth bullet reads *"GAAP net income attributable to DoorDash, Inc. common
  stockholders decreased 30% Y/Y to $200 million"* beside *"Adjusted EBITDA increased 40% Y/Y to $914 million"*. Adjusted
  EBITDA removes stock pay ($1,056M FY2025), D&A ($747M) **and, every year, "Certain legal, tax, and regulatory settlements,
  reserves, and expenses" of $162M, $180M and $135M** (FY2023-25, 10-K reconciliation). FY2025: Adjusted EBITDA $2,779M
  against GAAP net income $935M.
- [x] **The except-for flag [E2-57] and the recurring-charge flag [E5-33]:** $477M of legal and regulatory cost in three
  years, excluded from the headline as *"not indicative of our core operating performance"*, arising from the business model's
  legal status (worker classification, pay rules). A cost that recurs every year and grows out of the model is a cost of the
  model; *"you must count the runs scored against you in all nine innings."*
- [x] **Trumpeted projections [E4-22, E3-48, E5-30]:** quarterly guidance ranges every quarter read, plus year-shape guidance
  (*"we expect Adjusted EBITDA as a percent of Marketplace GOV to increase slightly compared to 2025"*). **The record [E3-48],
  set against outturn:** Q1 2026 guided GOV $31.0-31.8bn, reported $31.604bn; Adjusted EBITDA guided $675-775M, reported
  $754M (both inside the range, Q1 and Q2 2026 EX-99.1); the company's own claim is that *"we have historically exceeded the
  high end of our guidance range for Marketplace GOV"* (Q4 2025 EX-99.1). **Guidance is met, and it is a guidance culture
  [E5-30] on a non-GAAP yardstick.**
- [x] **Serial share issuance [E5-15], through stock pay:** cover counts 392.08M (2023-02-15), 404.00M (2024-02-09), 420.10M
  (2025-02-07), 434.43M (2026-02-12), 433.30M (2026-07-30): **+10.8% in three years after $974M of buybacks in 2023-24**, with
  no equity sold for cash since the 2020 IPO. Wolt ($2,838M) was paid in stock in 2022 before this window.
- [ ] **Weak accounting / unintelligible footnotes [E4-22]:** not found; SBC is expensed and the capitalised part is disclosed
  in the supplemental cash-flow lines. The 10-K/A corrected a clerical error in KPMG's report, not the statements.
- [ ] **Filed-figure tells [E4-30]:** growth is not smooth (Q1 2026 Net Revenue Margin 12.8% against 13.5% either side); cash
  taxes are negligible because of accumulated losses, so the tax tell is not readable.
- [ ] **Metric-switching [E2-49]:** Net Revenue Margin *"which we referred to in past SEC filings as Take Rate"* (FY2022 10-K)
  is a rename without a change of definition; the headline has been Adjusted EBITDA throughout the releases read (Q4 2022 to
  Q2 2026). Not fired. (The operator's prior on this flag, six fires and five failures, is checked and not assumed.)
- **Convergence [E4-52]:** four prompts point one way (a non-GAAP headline that excludes recurring regulatory cost, guidance
  on that headline, stock pay large enough to raise the count 10.8% net of buybacks, and a CEO award that pays only on the
  price). Read together, as one system, they describe a reporting and pay design built around the share price and a
  pre-cost profit figure.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Net income to common holders on average equity: **FY2023 -8.2%, FY2024 1.7%, FY2025 10.5%** (FY2025 includes a one-time
valuation-allowance release); equity of $9,921M at 2026-06-30 includes $5,495M of goodwill and $2,005M of intangibles, so on
[E2-43]'s unleveraged net tangible assets the operating business needs no capital at all (merchants and couriers fund it), and
the whole return question is **what the acquired capital earns**: Deliveroo ($3,724M) was guided to contribute *"approximately
$200 million to our Adjusted EBITDA in 2026"* (Q4 2025 EX-99.1), a pre-stock-pay, pre-D&A figure against a $1,498M intangible
base amortising over two to eleven years.

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
**Mixed.** For: the releases quantify Deliveroo's contribution against the stated expectation (*"a contribution to Adjusted
EBITDA that slightly exceeded our stated expectation of $45 million"*), which is the [E4-39] post-mortem habit in small; GOV
growth is given *"excluding the impact of Deliveroo"* every quarter; the FCF table subtracts capitalised software. Against:
the tip model is described as a customer misimpression and the authorities are not named; recurring regulatory cost is
removed from the headline; guidance is given only on a figure that excludes stock pay.

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08, E4-31, E5-24]:** $400M at $71.84 (2022), $750M at $62.66 (2023), $224M at $105.12 (2024), none in 2025,
  **$1.0bn at $155.25 in H1 2026** (6.8M shares; May alone 5,368K at $157.29), each retired (10-K Note 11s; Q2 2026 10-Q).
  Condition (1), ample funds: met ($6.2bn of cash and investments). Condition (2), a material discount to intrinsic value
  conservatively calculated: **fails on this run's figures** (owner earnings of $0.02-1.09bn a year, Q4, capitalise at 10% to
  $0.2-11bn against a cap of about $67bn at $155). **CAPITAL ALLOCATION FLAG, with the humility clause [E4-13, E5-08]**:
  *"They also know a whole lot more about them than I do"*, and *"many CEOs never stop believing their stock is cheap."* The
  buyback also offsets stock pay rather than shrinking the count (above). Binds position size, never the rate.
- **The institutional imperative [E2-30]:** (2) acquisitions soaking up funds: **[x]** $4.15bn of cash acquisitions in FY2025
  (SevenRooms $1,152M, Deliveroo $3,724M, Symbiosys), funded partly with $2.75bn of converts; (4) peer imitation: **[x]**
  as a prompt (autonomy, AI assistants, a single global stack: the sector's agenda); (1) and (3) not evidenced.
- **Loss of focus [E3-40]:** grocery, retail, international, advertising, reservations software, autonomy and AI at once,
  with grocery unit economics expected to *"turn positive in 2H 2026"*; a prompt, carried to Q6.
- **Dividends funded by issuance [E2-52]:** no dividend. Not engaged.

- **VERDICT (RECORDED, NOT GOVERNING): UNRESEARCHED on the binary** (work order above); a GATE case; capital-allocation flag on
  the 2026 buybacks; [E4-29], [E2-57]/[E5-33], [E5-15] and [E3-50] prompts converging [E4-52]. *IN would have meant no
  disqualifier found, not a finding of honesty [E5-17].*

### THE GUARDRAIL
- [x] Nothing in this Q3 promotes the name; a strong Q3 could not have repaired Q2 [E2-37, E2-38, E3-39].
- [x] Key-person dependence was asked at Q2 and not recorded as a moat defect.
- [x] No manager is "the plan" here; the question does not arise after Q2 OUT.

## Q4 — WILL IT SURVIVE?

**RECORDED, NOT GOVERNING.**

### Owner earnings — the one number **[E2-23]**
Built from the filed cash-flow faces (`oe.py`, `oe_out.txt`): operating cash **less stock pay expensed in full [E5-06]**, less
(c). Two ends of (c), both disclosed judgments:
- **Capex end (central):** purchases of property + capitalised software (cash) + **stock pay capitalised into software**
  ($93M, $132M, $161M, $165M, $193M), which sits in neither the expensed SBC nor the cash capex line (the TOST lesson).
- **D&A end:** D&A **less amortisation of acquired intangibles** ($13M, $99M, $127M, $125M, $212M), because the purchased
  intangibles are not plant the business must renew; the (c) question they raise is acquisitions, shown separately.
- **[E5-20] asked: NO.** Property and equipment net $1,246M on $13.7bn of revenue; capex plus software 4.4% of revenue. The
  default [E3-44, E2-41] applies; the capex end is higher than the plant D&A end in every year because the business is
  growing and rebuilding its technology, so the capex end is taken as central and the D&A end as the optimistic display.

| $M | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM to 2026-06-30 |
|---|---:|---:|---:|---:|---:|---:|
| Operating cash | 692 | 367 | 1,673 | 2,132 | 2,431 | 2,830 |
| Stock pay expensed | (486) | (889) | (1,088) | (1,099) | (1,051) | (1,114) |
| (c) capex end, incl. capitalised stock pay | (330) | (478) | (485) | (495) | (798) | (925) |
| **Owner earnings, capex end** | **(124)** | **(1,000)** | **100** | **538** | **582** | **791** |
| Owner earnings, D&A end (plant and software) | 63 | (792) | 203 | 597 | 845 | 1,093 |
| Working-capital lines inside operating cash | 435 | 148 | 530 | 252 | (400) | (275) |
| Cash paid for acquisitions | 0 | (71) received | 0 | 0 | 4,171 | 3,048 |
| Interest income inside operating cash | | | 152 | 199 | 211 | |

- **Five-year mean FY2021-25 [E2-42]:** **$19M at the capex end**, $183M at the D&A end; excluding the working-capital inflow,
  **-$174M** and -$10M; **with cash acquisitions charged, -$801M** and -$637M.
- **Three-year mean FY2023-25:** **$407M** (capex end), $548M (D&A end); excluding working capital $279M / $421M.
- **TTM to 2026-06-30:** $791M (capex end), $1,093M (D&A end).
- **Spread [E4-25, E4-38]:** from -$801M (five years, capex end, acquisitions charged) to +$1,093M (TTM, D&A end); on the
  organic construction alone, $19M to $1,093M. **FY2022 is the distorted year** (Wolt replacement awards lifted stock pay to
  $889M, operating cash fell to $367M) and **FY2025 carries a working-capital outflow of $400M and the first quarter of
  Deliveroo**; the window is a splice (Step 0), and no pro forma operating cash exists.
- **Stock pay at grant value [E3-70]:** RSUs granted in FY2025, *"9,143 | $ | 195.33"* = **$1,786M** ($1,533M net of
  forfeitures) against a charge of $1,244M including the capitalised part; H1 2026 grants *"9,611 | $ | 187.56"* = **$1,803M
  in six months** against a half-year charge of $712M. On grant value, FY2025 owner earnings at the capex end fall from $582M
  to between about $40M and $290M. **Stock pay was 51.2% of operating cash in FY2025 and 73.4% over FY2021-25** (charge
  basis, capitalised part included): section 5 of the resume note's threshold for reading the grant table by hand, which this
  run did.
- **Interest on the cash pile** ($211M in FY2025) is inside operating cash and is not earned by the delivery business.
- **The working-capital increment [E2-23] constraint 3:** the business does not require added working capital; growth
  **releases** it (merchants and couriers are paid after customers pay). A no-growth state would stop the inflow, so the
  ex-working-capital means are the more conservative reading of what the business itself produces.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · [ ] good · [ ] gruesome, **between good and gruesome, and the split is organic against acquired.** The organic
  business grows with little capital ([E2-44]'s second half passes) but earns little: owner earnings of about 0.4-0.8 cents
  per dollar of GOV. The acquired capital ($3.7bn for Deliveroo, $1.15bn for SevenRooms, $2.8bn of stock for Wolt) has not yet
  shown a return in owner earnings; charged at cost, the five-year mean is -$801M. [E4-43] forbids over-reading capital-hungry
  growth as gruesome; the file records the question rather than the class.

### Staying power — score all three **[E5-11]**
- (1) **Large and reliable earnings:** not yet. One GAAP-profitable year (FY2025, $723M operating income); owner earnings
  positive in three of five years.
- (2) **Massive liquid assets:** cash and investments **$6,216M** at 2026-06-30 ($4,424M cash, $923M short-term, $869M
  long-term), plus $308M restricted; a revolver raised on 2026-08-05 *"from an aggregate principal amount of up to $800 million to an aggregate principal amount of up to $2.0 billion"*, maturity 2031, *"no revolving loans outstanding"* (10-Q Part II Item 5), which [E5-39] counts as nothing.
- (3) **No significant near-term cash requirements:** accrued expenses and other current liabilities of **$5,747M**, mostly
  amounts owed to merchants and couriers, are settled within days and are rolled by continuing volume; **$5.3bn of
  non-cancelable purchase commitments**, *"primarily relate to the purchase of technology platform infrastructure"* (FY2025 10-K commitments note); the
  $2.75bn 2030 notes are zero-coupon, principal payable in cash on conversion, due 2030-05-15. **Passes while volume flows;
  the float that funds the business reverses if volume falls.**
- **Leverage, named [E4-16, E2-54]:** no interest to cover (0% notes); no leverage ratio is applied (the framework supplies
  none for subject companies).

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism:** the courier's legal status or pay floor is reset (reclassification as employees; minimum-earnings rules
  spreading from New York City; the EU's platform-work rules for Wolt and Deliveroo riders) **while** a competitor of equal
  size (Uber, $90.9bn of delivery bookings) or a new one (Amazon, named by the filer) prices to hold volume, so the cost cannot
  be passed on. The company's own words: minimum-earnings standards *"have caused, and may in the future cause, us to increase
  the fees"*, and fee increases *"could result in lower order volumes over time"*.
- **Quantified from filed figures:** FY2025 GAAP operating income $723M is **0.71% of GOV**. Couriers earned *"over $20
  billion"* in 2025 (tips included). **A 3.6% rise in courier cost that cannot be passed on erases the year's operating
  income**; a one-point fall in Net Revenue Margin (13.4% to 12.4%) removes $1.0bn of revenue, more than the TTM owner
  earnings at either end. The CA EDD assessment, the PAGA claims and the $477M of regulatory cost excluded from Adjusted EBITDA
  in three years are this mechanism already running at low intensity. **Model exposure, not experience [E4-40]:** the one
  profitable year is late in a period of rising margins across all three filers.
- **Against the shapes index (`Screens/SURVIVAL SHAPES - index.md`):** a later instance of **#11 THE PASS-THROUGH** (the efficiency
  gains go to customers through lower DashPass fees and to couriers through regulated pay floors) with **#17 THE PERMIT** as a
  feature (governments set the courier's status and pay and, in some cities, the commission, market by market) and **#2** as a
  feature (stock pay 73.4% of operating cash FY2021-25). No new shape proposed.
- **Likelihood:** **[x] a real possibility** (the company names it in its own risk factors every year; the direction of rules
  in the filings is one way).
- **VERDICT (RECORDED, NOT GOVERNING): [x] UNKNOWABLE.** The combined range runs from -$801M to +$1,093M a year (acquisitions
  charged or not, window, working capital, stock pay at charge or grant value), so wide that no useful conclusion can be
  reached [E4-25], and one year of GAAP profit does not settle strength (1). *Can I name the document that would resolve it?
  No: the answer is the next five years' operating cash of a business whose industry the filer calls "nascent", not a filing
  that exists.*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** It did not open: Q2 OUT. What follows is arithmetic only.

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
*Headed as operator rule 3 requires; no entry language; no ranking.*
- **Cap:** US$83.60bn (Step 0; $89.16bn with RSUs and options). **Sovereign:** 5.34% (US Treasury, 09/18/2026). **Floor:**
  ~10% [E4-28].
- **Yield, owner earnings / cap:** five-year capex end **0.02%**; three-year capex end **0.49%**; TTM capex end **0.95%**; TTM
  D&A end **1.31%** (the best figure the filings support); five-year with acquisitions charged, negative.
- **What the price assumes:** a 10% expectancy needs about **$8.4bn a year** of owner earnings, **10.6 times** the TTM capex-end
  figure and 7.6 times the TTM D&A end. At 20% a year compounded that is 13 years; [E4-35]'s base rate is that fewer than one
  in twenty of the most profitable companies sustain 15% for twenty years.
- **Value, no growth, at the floor, round numbers [E4-01]:** about **$0-10bn** against **$84bn**. The ceiling [E2-63]: GOV
  cannot compound faster than local spending forever, and the share of it kept is set by three multi-homing sides and
  regulators (Q2).
- **Bar:** none chosen; no margin applied; windage count zero. **VERDICT: none. Q5 did not open (Q2 OUT).**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**RECORDED, NOT GOVERNING; nothing is armed.** No band, no PORTFOLIO row: a Q2 OUT is a finding about the business (the
QLYS ruling). **The reversal condition, in words, pre-committed [E1-02]:** reopen Q2 only if (1) the company's Item 1A drops
the sentence that switching is *"relatively easy"* and the multi-homing description, **and** (2) the filed price series shows
fees and commissions raised (not efficiency, not advertising) for three years with order growth intact **and** DashPass fee
discounts not widened, **and** (3) the peer row shows DoorDash's owner cash per dollar of volume at or above Instacart's and
its operating margin pulling away from Uber Delivery's for three years, **and** (4) a courier-cost reset (a reclassification
ruling or a new minimum-pay regime in a large market) has been absorbed without a fall in operating income. The monitoring
question [E3-30, E4-17] does not arise for an unowned name.

**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. The file closed at Q2 (OUT); Q3-Q6 are labelled RECORDED, NOT
      GOVERNING in every heading and verdict line.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed order, GOV and Net
      Revenue Margin series, FY2020-H1 2026; the excluded parts (autonomy, AI, grocery and international futures) are named as
      outside the circle, not as caveats on the IN.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (Q3: the D.C. Superior Court complaint and consent
      judgment in *District of Columbia v. DoorDash*, and the 2019 internal record; recorded, not governing).
- [x] Every UNKNOWABLE verdict states what cannot be known (Q4: the next five years' operating cash of a business whose
      industry the filer calls "nascent"; the range -$801M to +$1,093M is too wide [E4-25]).
- [x] Step 0: the filing was read, with accession numbers; operating cash, stock pay, D&A, both capital lines and revenue
      cross-checked against the FY2025 and FY2022 10-K faces; the cover count cross-checked against the 10-Q balance sheet
      and equity statement.
- [x] Owner earnings on multi-year means (five and three years, plus TTM); windows stated; (c) disclosed as a judgment with
      both ends; stock pay subtracted in full, capitalised stock pay added to (c), grant value shown [E3-70].
- [x] Competitor row filled from three SEC filers' own filings (DASH, UBER Delivery, CART) plus Deliveroo through DASH's own
      Note 4; the non-SEC competitors named and the reason the class is not held PROVISIONAL stated.
- [x] Sovereign for the earnings currency (USD), from the issuing authority (US Treasury par yield curve), dated 09/18/2026;
      `sources.sovereign()` stale and not used.
- [x] Value stated as a round-number range (about $0-10bn no-growth at the floor), and only as a COMPUTATION - NOT A CLEARANCE.
- [x] One bar chosen, not both: none, because Q5 did not open; windage count zero.
- [x] Prices dated; aggregator (Yahoo) used for the live quote only, flagged, corroborated by three Form 4s.
- [x] Run committed to git (template `e30b2f8`, Step 0 `2d30b95`, Q1-Q2 `3bcaa7b`, Q3-Q6 with audit and register in the next
      commit, fold after).

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **A commit failed on a relative path** (the Step 0 commit ran `git commit` from the wrong directory). Nothing was
   committed wrongly; the commit was re-run with absolute pathspecs and contains only this run's files.
2. **A web search summary offered a checkout quotation** about tips that is **not in the Assurance of Discontinuance** this
   run read. It was not used; only text found in `NYAG_AOD_2025.txt` is quoted.
3. **Two quotations from the DEF 14C were first cut mid-clause** and a revolver line first described the facility as $800M,
   the pre-amendment figure. All three were corrected against the documents before the Q3-Q6 text entered the run file
   (the revolver is $2.0bn from 2026-08-05, 10-Q Part II Item 5).
4. **A first guess at the attorneys' general URLs returned 404**; the AOD was then found on the NY AG's own server. The D.C.
   matter was not fetched and stands as the Q3 work order rather than being described from memory.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
- None that changed a number. The brief told the run to verify the Deliveroo and SevenRooms deals from filings rather than
  take them as fact; both are confirmed (Note 4), and a third 2025 acquisition (Symbiosys) was found in the tax note. The brief
  did not know of the **Nevada reincorporation effective on the run date**, which changes which charter governs the class
  treatment; the run read the new articles rather than the Delaware certificate the brief implied.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`sources.sovereign("USD")` served the cached 09/17 row (5.29%) again**; the eighth recorded occurrence across runs.
- **`acquisition_flag` misreads FY2025**: it reports a *"NET CASH INFLOW on the acquisition line ($4,222M ...)"* where the face
  shows an outflow of $4,151M. Not investigated further; the face was used.
- **`working_capital_flag` returned None** although the accrued-liabilities line moved by 44% of operating cash in FY2024
  ($943M of $2,132M); it reads specific tags and may not reach this filer's line. A prompt for the operator, not a fix.
- **`cover_shares.py` was not needed**: the three dimensioned dei facts were read directly from the inline XBRL (`dei.py`).
  The C class is tagged `ixt:fixed-zero` over the word "no"; any parser that expects a number there should expect that.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A rising take rate is not pricing power until the filer says why it rose.** DoorDash's Net Revenue Margin rose from 11.7%
to 13.4% while orders nearly tripled, which reads at a glance as [E2-44]'s price-with-volume. The filer's own explanation in
three consecutive 10-Ks is logistics efficiency and advertising, and because revenue is reported **net of courier pay**, a
cheaper delivery raises the margin with no change in any price. For any net-revenue marketplace, read the MD&A's stated
driver of the take rate before scoring it at Q2.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- **One line:** DASH FAILS at Q2 (OUT, on the business): criterion (2) of [E3-03] fails in the company's own words
  (*"It is relatively easy to switch between offerings in our industry"*; all three sides multi-home; competition *"led us
  ... to change our commission rates and fees"*), in the largest peer's 10-K (Uber names DoorDash, *"low switching costs"*,
  $90.9bn of delivery bookings), and in the price series (margin gains from efficiency and advertising, growth bought with
  lower DashPass fees); [E4-04] fails because every side is held by payment renewed each order; criterion (3) is capped by
  minimum-pay and commission rules. Price US$192.94 (2026-09-18 close); 433,295,654 shares (A+B+C, Q2 2026 10-Q cover
  `0001792789-26-000050`); cap US$83.60bn; sovereign 5.34% (US Treasury, 09/18/2026). Q3-Q6 recorded, not governing: Q3
  UNRESEARCHED on the binary (NY AG AOD 25-007 read; D.C. matter the work order), Q4 UNKNOWABLE (owner earnings -$801M to
  +$1,093M across windows and ends), Q5 computation only (yield 0.02-1.31% against 5.34% and a ~10% floor).
- **If UNRESEARCHED - THE WORK ORDER:** not applicable to the governing verdict.
- **If UNKNOWABLE:** not applicable to the governing verdict.

