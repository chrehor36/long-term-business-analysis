# Company Run — Alkami Technology, Inc. (ALKT) — 2026-09-12

**STATUS: COMPLETE. FAIL at Q2 (OUT, on the business). Q1 IN; Q3 and Q4 recorded, not governing; price headed COMPUTATION — NOT A CLEARANCE; Q6 records refutation conditions.**
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
- rate **5.35 %** · date **2026-09-11** · source **US Treasury daily par yield curve, 30-year,
  issuing authority** (`home.treasury.gov` daily_treasury_yield_curve CSV, 2026 file, fetched by
  this run at about 22:45 EDT on 2026-09-12; output kept in `_research 2026-09-12 ALKT/sov_out.txt`).
  The 2026-09-12 print was not in the file at the time of the strike, so 09-11 is the currently
  observed rate. Prior prints in the same file: 09-10 5.37%, 09-09 5.28%, 09-08 5.25%. **Struck by
  this run, not inherited from the brief** (the brief's 5.35% for 09-11 is confirmed).
- **Earnings currency: USD, read from the filing rather than assumed.** 10-K FY2025 note 2 (Operating
  Segment): *"The Company derives revenue from clients located in the United States"*, and
  *"Substantially all of the Company's principal operations, assets and decision-making functions are
  located in the United States."* The one foreign leg is a cost centre: an Indian subsidiary set up in
  2024 whose operations *"remain immaterial to our consolidated financial statements"*; FY2025 foreign
  pretax income $596k and foreign cash taxes $201k (note 10, cash-flow footnote). Rupee exposure is a
  cost-side risk named in Item 1A, not an earnings currency.
- FX: none. ADR ratio: none — ALKT is a Delaware registrant on Nasdaq.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **10-K FY2025**, period 2025-12-31, filed **2026-02-26**, accession **0001529274-26-000009**
    (`alk-20251231.htm`) — read: Item 1 in full, Item 5, Item 7 MD&A in full (including the adjusted
    EBITDA reconciliation and key business metrics), the auditor's reports and critical audit matters,
    all four primary statements, and notes 1-17.
  - **10-Q Q2 2026**, period 2026-06-30, filed **2026-07-30**, accession **0001529274-26-000052** — cover,
    condensed statements, notes 8 (repurchases), 15 (subsequent event), MD&A liquidity.
  - **10-Q Q1 2026** acc. **0001529274-26-000032** · **10-Q Q3 2025** acc. **0001529274-25-000162**.
  - **10-K FY2024** acc. **0001529274-25-000031** · **FY2023** acc. **0001529274-24-000029** ·
    **FY2022** acc. **0001529274-23-000037** · **FY2021** acc. **0001529274-22-000034** — cash-flow
    statements (for the newest vintage of each year), business-combination notes, equity statements.
  - **DEF 14A 2026**, filed **2026-04-07**, accession **0001529274-26-000023**.
  - **8-K EX-99.1 earnings releases:** Q2-2026 acc. **0001529274-26-000049** · Q1-2026 acc.
    **0001529274-26-000028** · Q4-2025 acc. **0001529274-26-000005** · Q3-2025 acc. **0001529274-25-000159**.
  - **8-K 2026-05-06** (event 2026-05-01), acc. **0001529274-26-000036** — the Item 1.01 the `deal_note`
    counted, with EX-10.1. **8-K 2026-04-01** (5.02) acc. 0001529274-26-000014 · **8-K 2026-05-20** (5.07)
    acc. 0001529274-26-000043.
  - **Deal documents:** 8-K 2025-02-27 (MANTL merger agreement, EX-99.3; credit agreement third
    amendment) acc. 0001529274-25-000028 · 8-K 2025-03-13 (2030 convertible notes, capped calls) acc.
    0001529274-25-000040 · 8-K 2025-03-17 (MANTL closing, Item 2.01) acc. 0001529274-25-000044 · 8-K
    2022-04-25 (Segmint closing) acc. 0001529274-22-000067 · 8-K 2021-09-13 (MK Decisioning asset
    purchase) acc. 0001529274-21-000057.
  - **Beneficial-ownership filings (read because the price moved +40.6% from 2026-06-22 and no 8-K
    explains it):** Schedule 13D General Atlantic 2025-08-20 (acc. 0000950142-25-002245) and 13D/As of
    2026-03-11, 2026-05-07, 2026-05-15; Schedule 13D JANA Partners 2026-04-01 (acc.
    0000902664-26-001830), 13D/A 2026-05-12, **13D 2026-06-29 (acc. 0000902664-26-002944)**; 13G/A North
    Reef Capital 2026-08-14. Read at Q3 and in the deal section below.
- figures cross-checked against the filed statement (three, all exact):
  1. **FY2025 operating cash flow rebuilt from its own detail lines.** Net loss −$47,652k + non-cash
     items ($26,912k − $854k + $76,188k + $1,951k + $1,655k − $11,794k = $94,058k) + working capital
     (−$11,276k − $9,351k + $19,708k − $12,310k + $9,729k = −$3,500k) = **$42,906k**, equal to the filed
     "Net cash provided by operating activities" to the dollar, to the MD&A table, and to the XBRL
     `NetCashProvidedByUsedInOperatingActivities` value of 42,906,000.
  2. **Gross profit.** Revenues $443,639k − cost of revenues $187,040k = **$256,599k**, equal to the filed line.
  3. **D&A composition.** Note 4 property-and-equipment depreciation and amortization **$4.6M** + note 16
     amortization of intangible assets **$22.3M** = **$26.9M**, equal to the cash-flow add-back of
     $26,912k — which establishes that **the D&A line contains no amortization of deferred commissions or
     deferred implementation costs** (those run through the "Deferred costs" working-capital line). This
     settles the ELF triple-count question at Step 0, before Q4 uses it.

**THE PRICE, THE COUNT, AND THE CAP — and the cap_flag resolved.**
- **Price $20.51**, close **2026-09-11** (Nasdaq, via Yahoo chart API — *aggregator used for the live
  quote only, and flagged*, operator rule 5; history kept at `px_history_2y.json`). 09-10 $19.06, 09-09
  $18.65. **The 09-11 close is +7.6% on the day on 3.34M shares, about 2.6x the prior session's volume;
  no SEC filing dated 09-08 to 09-12 exists in the submissions index fetched at 22:45 EDT, so the move is
  recorded and not explained.** Longer context from the same series: $30.14 (2025-06-30), $23.07
  (2025-12-31), $15.67 (2026-03-31), **$14.59 (2026-06-22, the event date of JANA's 13D)**, $18.12
  (2026-06-30).
- **Share count off the cover of the latest periodic filing** (`python Screens/cover_shares.py ALKT`, then
  the cover opened): 10-Q for the period ended 2026-06-30, filed **2026-07-30**, accession
  **0001529274-26-000052** — *"The number of shares of registrant's common stock outstanding as of June
  30, 2026 was 106,941,980."* Confirmed against the balance sheet on the same date (106,941,980 issued and
  outstanding). **One class of common stock; 10,000,000 preferred authorized and none outstanding** — no
  share-class judgment is needed.
  - **Limit stated: the cover's as-of date is the period end itself, not a later date**, so it does not
    see July. Note 15 does: *"In July 2026, the Company repurchased an additional 531,620 shares of its
    common stock ... for an aggregate consideration of $10.0 million."* RSU vesting and ESPP issuance after
    June 30 are not disclosed, so no later count can be built. The cover count is used; **the July
    buyback alone would lower the cap by 0.5%**, immaterial to anything below.
- **MARKET CAP = 106,941,980 × $20.51 = $2,193.4M.** The queue row carried **$2,079M — 5.2% low**, which
  is a price difference (the row's cap implies about $19.44-$19.59 a share), not a count error.
- **THE CAP_FLAG, RESOLVED: NEITHER NUMBER IS WRONG. THE FLAG COMPARED TWO DATES.** The flag reads *"cap
  $2,079M against a filed float of $2,400M ... A cap cannot be smaller than a subset of itself. One of the
  two is wrong."* The float is the 10-K cover's *"aggregate market value of the common equity held by
  non-affiliates ... as of ... June 30, 2025, was $2.4 billion"* — **struck at the 2025-06-30 close of
  $30.14.** On that date the cover count was 104,083,138 (10-Q Q2-2025 dei), so the cap was **$3,137M and
  the float was 76.5% of it** — a subset, as it should be. The screen's cap is struck at a price about
  35% lower fourteen months later. **"A cap cannot be smaller than a subset of itself" is true only at one
  date; the guard tests a same-date identity across two dates.** Recorded as a tooling defect at the fold
  (a price move of more than roughly a quarter since the float date will fire it on any name).
- **The count's own history** (dei covers): 85,936,693 (2021-04-30, just after the IPO) → 92,302,501
  (2023-02-16) → 102,232,922 (2025-02-21) → **106,941,980 (2026-06-30): +24.4% in five years and two
  months**, read at Q3.
- **Claims ahead of the equity, 2026-06-30** (10-Q balance sheet): **$345.0M principal of 1.50%
  convertible senior notes due 2030-03-15** (conversion $32.82, capped calls to $47.74), revolver $0
  (the $15.0M was repaid in H1-2026), against cash $45.5M and marketable securities $35.4M. **Net debt
  $264.0M.** Stockholders' equity $362.7M against goodwill $403.4M and intangibles $145.7M — **tangible
  equity is negative, −$186.4M.**

### THE DEAL NOTE, OPENED — and the thing it could not see

- **The one 8-K Item 1.01 since 2026-02-26 is a credit-agreement amendment, not a merger.** 8-K filed
  2026-05-06, acc. 0001529274-26-000036: *"On May 1, 2026, Alkami Technology, Inc. ... entered into a
  Fifth Amendment ... to the Company's Amended and Restated Credit Agreement ... The Amendment permits
  the Company to use up to $100,000,000 of its cash to repurchase its common stock."* It is the lender
  consent for the $100M buyback the board authorized on 2026-04-23 (8-K 2026-04-29, Item 8.01). The
  8-K also names a **Fourth Amendment dated April 3, 2026** that was not separately filed on an 8-K.
- **No merger agreement for ALKT exists in any filing read.** The ROKU finding does not apply: there is
  no deal consideration to price the quote against, so the quote is not a spread.
- **BUT THE QUOTE IS NOT A CLEAN OWNER-EARNINGS PRICE EITHER, AND THE DEAL NOTE CANNOT SEE WHY.** The
  control-shaped facts sit in Schedule 13D, which the `deal_note` does not read:
  - **JANA Partners, 13D event 2026-06-22, filed 2026-06-29:** *"The Reporting Person has had, and intends
    to have, discussions with the Issuer's board of directors and management regarding: (1) exploring a
    sale, including by engaging with multiple parties interested in a potential acquisition of the
    Issuer, and doing so with grounded views of the Issuer's ability to realize value in the public market
    and realistic views of its intrinsic value; (2) corporate governance; and (3) board leadership."*
    6,747,707 shares (6.3%) plus cash-settled swaps on 4,195,027 more (3.9% economic exposure). Its
    Schedule A shows purchases of 1,013,482 shares at $14.56 on 2026-06-22. Earlier, 13D/A of 2026-05-12:
    *"The Reporting Person reduced its ownership of the Issuer to below the reporting threshold to allow
    for private discussions with the Board regarding specific potential value maximizing opportunities."*
  - **General Atlantic, 13D/A event 2026-05-13: 19,420,994 shares, 18.1%**, and in the 13D/A of 2026-05-07:
    *"The board of directors of the Company granted a waiver from Section 203 of the Delaware General
    Corporation Law to the Reporting Persons with respect to purchases of common stock up to a beneficial
    ownership position of 19.9%."* 9.4M of GA's shares are pledged under Morgan Stanley margin loans
    (13D/A 2026-03-11).
  - **North Reef Capital, 13G/A 2026-08-14: 9,075,000 shares, 8.48%.**
  - **The quote since 2026-06-22 therefore carries a takeover expectation that no filed agreement
    supports.** It is not a spread (there are no terms), and it is not a pure owner-earnings price. It is
    recorded here and used at Q5 only as a caution on what the price is paying for.
- **The acquisitions inside the window, dated from the filings** (cash, net of cash acquired, per the
  cash-flow statements): **MK Decisioning, 2021-09-10, $18,326k** (asset purchase, 8-K Item 2.01) ·
  **Segmint, 2022-04-25, $131,839k** · **MANTL, 2025-03-17, $375,499k**. Sum **$525,664k — the row's $526M
  reproduces exactly.** **All three were paid in cash**: MK Decisioning's earn-out (fair value $15.5M at
  closing, up to $25M, payable partly in shares at a $35 reference price at the sellers' election) was
  written to zero in 2022 and never paid, and MANTL's only non-cash element was $821k of replacement
  awards (10-K FY2022 note 3; 10-K FY2025 note 3). So the tested source limit on stock consideration
  does not bite here. (ACH Alert, 2020-10, $25,073k, sits before the five-year window.) **The brief's
  prior that the $526M is "largely one deal" is two-thirds right: MANTL is 71.4%, Segmint 25.1%.** The
  perimeter treatment is decided at Q4.

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**
Alkami rents a website and phone app to US community and regional banks and credit unions, which
the bank puts its own name on. The bank's customers log in to it to see balances, move money, pay
bills and open accounts. **The bank pays Alkami a monthly fee per customer who has signed up for
online banking, per product switched on, with a contracted minimum**, on contracts that have averaged
**about 70 months** (a figure the 10-K has repeated, word for word, since FY2021). Revenue in FY2025
was **$443.6M: 95.0% subscription, 2.8% implementation fees (billed up front, recognised over the
contract), 2.1% other services**. The drivers are filed and simple: **22.4M registered users × $21.44
of ARR per user = $480.3M ARR** at 2025-12-31 (23.6M users, $21.69, $511.7M at 2026-06-30, Q2-2026
release). **301 banks and credit unions on the full platform**, and over 960 clients counting those
that buy only an acquired point product.

Where each revenue dollar goes (10-K FY2025, MD&A cost table and income statement): **18.9 cents is
passed straight to third parties whose services Alkami resells inside the app** (bill pay and other
licensed functions), **5.2 cents to Amazon Web Services for hosting**, 8.9 cents to the teams that
install and support clients, 2.9 cents to platform maintenance, 4.4 cents of amortization and 1.9 cents
of stock pay — a **57.8% gross margin**. Below it, **R&D 26.7 cents, sales and marketing 18.1 cents,
general and administrative 22.7 cents**, and a **12.1% operating loss**. Installing a new bank takes
**six to twelve months** after a **three-to-twelve-month** sale, and revenue only starts at go-live, so
growth is paid for about a year before it is billed. The company says renewals earn *"approximately
70% gross margin"*, which is the claim the whole model rests on: the installed base is meant to become
profitable when the up-front costs are behind it.

**Growth, with the acquisition stripped out.** Reported revenue grew **32.9%** in FY2025; MANTL
contributed **$34.9M** from 2025-03-18, so **organic growth was about 22.4%** ($408.7M against $333.8M).
H1-2026 revenue grew 22.0%; **Q2-2026, the first quarter with MANTL in both periods, grew 15.9%**.

**The scarce input this business controls.** Three filed candidates, and only one is Alkami's alone:
1. **The installed contract base** — 301 platform clients on ~70-month terms, a **$1.7bn remaining
   performance obligation** (3.8x FY2025 revenue; 49% due within 24 months), and the six-to-twelve-month
   installation any replacement vendor must repeat. The 10-K states the incumbent's advantage in plain
   words from the attacker's side: *"Potential clients may also prefer to continue their relationship
   with their existing partner rather than change to a new partner regardless of product performance or
   features."* **That switching cost is real and it is the scarce input** — for whichever vendor holds
   the client.
2. **More than 300 integrations** into core systems and fintech services, maintained in one code base.
   **But the integrations to the core are not Alkami's to control**: *"We do not have formal
   arrangements with many of these third-party providers regarding our access to their application
   program interfaces to enable these client integrations"* (Item 1A). The core providers are named
   competitors (Q2).
3. **Data** synthesised from core and digital banking activity — asserted in Item 1, not measured in any
   filed number, so not credited.

**Will the fundamentals look broadly the same in ten years?** **How it makes money, yes; who earns it,
not established here.** Per-user subscription pricing for a bank's digital channel has been the model in
every 10-K from FY2021 to FY2025, and US banks will still need a digital front
end in ten years. Two filed facts cut the other way and are carried forward rather than resolved at Q1:
the market is *"characterized by rapid changes in technology and frequent new product introductions"*
(Item 1A) — which is **[E4-04]**'s question, whether the moat must be continuously rebuilt, and that
question lives at Q2 — and the client universe is shrinking: *"FIs have experienced consolidation,
distress and failure, and very few new FIs are being created."* **Neither makes the business
unintelligible.** The test of **[E4-46]** is met: this is *"a named filing inside an understood business"*,
not a business that would take months of study.

**VERDICT: [x] IN** — the revenue formula (users × products × price, over 70-month contracts), the cost
structure, the one scarce input and the growth net of acquisitions are all filed numbers. The rate of
technological change is recorded, and is examined at Q2 under **[E4-04]**, where the corpus puts it.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Pre-registered before the competitor row was computed** (operator rule 9). My working prior, formed
reading the 10-K, was **OUT** — "recurring revenue with SBC and development excluded can look like a
franchise while earning nothing." Because that is the story I was favouring, the attack below is aimed
at it hardest **[E4-26]**. The prior fails if **any** of: (a) Alkami's owner-earnings margin sits inside
the computed row rather than below it; (b) the filings show a price increase that held; (c) the scale
curve of the one comparable pure-play competitor shows that Alkami's losses are a stage rather than a
structure. **Results: (a) went with the prior; (b) went with the prior, in the company's own words; (c)
went partly against it, and it is the strongest fact in the file for the bull case.**

### THE BULL CASE, BUILT FIRST AND AS STRONGLY AS THE FILINGS ALLOW

1. **Needed or desired, and sticky.** ~70-month contracts; $1.7bn of contracted but unrecognised
   revenue; no client above 5% of revenue; the six-to-twelve-month installation an incumbent's client
   must repeat to leave.
2. **Growing on units, not only dollars — [E4-55] passes.** Platform clients **118 (2019) → 151 → 177 →
   199 → 236 → 272 → 301 (2025)**; registered users **14.5M (2022) → 17.5M → 20.0M → 22.4M → 23.6M
   (2026-06-30)**. The physical series rises every year on the filed definitions (the target-client
   definition widened in FY2023, from $500M-$100bn of assets to the top 2,500 excluding megabanks).
3. **Existing clients buy more each year.** ARR from existing digital-banking clients **115%** of the
   prior year (10-K FY2025); products used per client **16 of 36**, new 2025 cohort **19**; cross-sell
   **54% of 2025 total contract value**.
4. **The operating economics have improved every year for three years.** Owner-earnings margin on the
   row's formula (OCF − SBC − capex incl. capitalised software, ÷ revenue): **−42.6% (FY2022) → −28.3% →
   −14.6% → −9.5% (FY2025)**; gross margin 53.0% (FY2022) → 57.8%; the company's adjusted EBITDA margin
   14.9% in Q2-2026. The 10-K says the bank and credit-union **win rates rose** in H2-2025.
5. **The scale curve of the closest competitor — the disconfirming datum for my prior.** Q2 Holdings,
   the one pure-play digital banking vendor that files with the SEC, had **$498.7M of revenue and a −10.1%
   owner-earnings margin in FY2021** — almost exactly Alkami's FY2025 position ($443.6M, −9.5%) — and
   **$794.8M and +10.9% in FY2025**, with a positive GAAP operating margin (5.0%), its first positive year of the six computed (FY2020-FY2025).
   **If Alkami follows the same curve, its losses are a stage.** That is a forecast from a peer's history,
   not a fact about Alkami, and it is recorded as the strongest argument against the verdict below.

### NOW THE ATTACK

**[E3-03] criterion (2) — "thought by its customers to have no close substitute." FAILS, on two
registrants' own words.**
- **The competitor names Alkami as a substitute.** Q2 Holdings 10-K FY2025 (acc. 0001410384-26-000006):
  *"With respect to our digital banking platform, we have several point solution competitors, including
  Candescent, Alkami Technology, CSI, Backbase and Lumin Digital in the online, consumer and SMB banking
  space and Finastra and Bottomline Technologies in the commercial banking space. We also compete with
  core processing vendors that provide systems and services such as Fiserv, Jack Henry and Associates and
  Fidelity National Information Services, or FIS."* (EDGAR full-text search for "Alkami" in 10-K forms
  since 2024-06-01: 24 hits — the Q2 Holdings 10-Ks for FY2024 and FY2025, eighteen documents in Alkami's
  own 10-Ks, and four documents of three other filers (Matterport 10-K, two NCR Voyix 10-K exhibits,
  Clearwater Analytics 10-K/As) **that were not opened**; output `fts_out.txt`. The hit list is a prompt,
  not the naming test; the Q2 Holdings sentence above was read in the document.)
- **Alkami's growth is made of customers switching.** 10-K FY2025, MD&A: *"Each of our digital banking
  client wins is a competitive takeaway"*, and *"In a replacement market, we win based on our ability to
  bring a product suite to market that is superior to the incumbent."* **A market in which every new
  client is taken from a competitor is a market whose customers treat the products as substitutes.**
  The switching cost slows the door; it does not close it — and it swings both ways at renewal.
- Alkami's own 10-K names **no** competitor; it describes *"core processing vendors that also provide
  digital banking solutions, and ... digital banking companies"*, and concedes that *"Many of our
  competitors have significantly more financial, technical, marketing and other resources than we
  have."*

**[E2-44] half one and [E4-37] — pricing. FAILS, and the company says so.** Item 1A, FY2025: *"large or
influential FI clients may demand more favorable pricing or other contract terms from us. As a result,
**in the past we have had, and expect to be required in the future, to change our pricing model, reduce
our prices or accept other unfavorable contract terms**."* And on the structure of the price itself:
*"Our pricing is tiered, with per-registered-user discounts applied as clients achieve higher levels of
customer or member penetration."* **Price falls as the client succeeds.** The per-user revenue rise
(+20.4% in FY2025, +7.0% year on year at Q2-2026) is filed as cross-sell and the MANTL products, not as
a price increase; **no price increase is described in any document read.** The Q2 Holdings 10-K confirms
the industry form of the same fact: its revenue-churn definition counts customers *"renewing their
contract for identical services at a lower price."* [E4-37]'s *"agony they go through in determining
whether a price increase can be sustained"* is not even reached: the filing describes price concessions,
not price increases.

**[E3-46] and [E3-03]'s own demonstration — "earn high rates of return on capital." FAILS; there is no
return to measure.** Operating loss in **every one of seven filed years** (FY2019-FY2025), **−12.1% of
revenue in FY2025**; net loss every year; accumulated deficit **$523.9M**; tangible equity **negative
(−$186.4M at 2026-06-30)**. Owner earnings negative in every year (Q4). [E3-03] says the three conditions
*"will be demonstrated by a company's ability to regularly price its product or service aggressively and
thereby to earn high rates of return on capital."* **Seventeen years after founding and five after the
IPO, neither half of that demonstration has occurred.**

**[E2-44] half two — "large dollar volume increases ... with only minor additional investment of
capital." FAILS.** FY2021-FY2025 revenue rose **$291.5M** (from $152.2M). Over the same five years the
business consumed: **$525.7M of cash acquisitions**; **$246.0M of stock compensation**; **$31.0M of capex
and capitalised software**; and it produced **cumulative operating cash of −$23.0M**. The acquisitions
were funded with **$345M of convertible notes and $60M of revolver** (2025) and, earlier, the **$192.8M IPO**
(2021); the share count rose **+24.4%** from 2021-04-30 to 2026-06-30.

### THE COMPETITOR ROW — required **[E3-28]**

**Formula, one for every filer** *(CONVENTION of this row, the framework's owner-earnings construction
applied at the capex end)*: owner-earnings margin = (operating cash flow − stock compensation − purchases
of property and equipment − capitalised software) ÷ revenue. Peer cells are **XBRL transcription from each
filer's companyfacts, newest vintage** (script `peers/compute.py`, output `peers/computed.json`,
`peers/row_out.txt`), **cross-checked against the filed cash-flow statements for Q2 Holdings (OCF
$201,461k, SBC $86,949k, capex $6,810k + $21,283k — all exact; revenue $794,809k and operating income
$39,897k exact to the MD&A table) and Jack Henry (OCF $761,960k, SBC $32,460k, capex $67,103k + $184,243k +
$4,108k — all exact).** Alkami's cells are from its filed statements.

| latest FY | **ALKT** | Q2 Holdings (QTWO) | Jack Henry (JKHY) | Fiserv (FISV) | nCino (NCNO) |
|---|---|---|---|---|---|
| period end | **12/31/25** | 12/31/25 | 6/30/26 | 12/31/25 | 1/31/26 |
| form · accession | **10-K `0001529274-26-000009`** | 10-K `0001410384-26-000006` | 10-K `0000779152-26-000067` | 10-K `0000798354-26-000009` | 10-K `0001902733-26-000022` |
| role | subject | pure-play digital banking; **names Alkami** | core vendor; Banno digital platform | core vendor | account opening / lending (MANTL's field; named by Q2) |
| revenue | **$443.6M** | $794.8M | $2,544.3M | $21,193M | $594.8M |
| revenue growth | **32.9% (22.4% organic)** | 14.1% | 7.1% | 3.6% | 10.0% |
| gross margin | **57.8%** | 54.1% | 43.7% | n/r | 60.6% |
| **GAAP operating margin** | **−12.1% ← last** | 5.0% | 25.0% | 27.5% | 0.6% |
| SBC ÷ revenue | **17.2% ← highest** | 10.9% | 1.3% | 1.7% | 12.4% |
| SBC ÷ operating cash | **178% ← highest** | 43% | 4% | 6% | 82% |
| **owner-earnings margin, latest FY** | **−9.5% ← last** | +10.9% | +18.6% | +18.6% | +1.5% |
| **owner-earnings margin, 5 years cumulative** | **−21.4% ← last** | −1.4% | +14.3% | +18.5% | −6.6% |

*n/r = cost of revenue not tagged in a resolving form for Fiserv. ALKT's owner-earnings cells use the
filed cash-flow SBC add-back ($76,188k for FY2025). **The screen's max-rule picks the tagged P&L charge
($80,098k), which includes $3.9M of MANTL awards settled in cash and already deducted inside operating cash
— a double count** — and on it the cells read −10.3% (latest) and −21.7% (cumulative). Last either way.
Fiserv and Jack Henry are consolidated figures for businesses of which digital banking is a part; neither
segments it. **The row compares positions in the value chain, not like-for-like digital banking units**,
and that is a limit.*

- Peers named: **5 SEC filers in the row** against **the ten companies Q2 Holdings names for its
  digital banking platform** (Candescent, Alkami, CSI, Backbase, Lumin Digital, Finastra, Bottomline,
  Fiserv, Jack Henry, FIS) — **ten substitutes for Alkami counting Q2 Holdings itself**.
- **Unavailable, and the limit stated rather than papered:** **Candescent, CSI, Lumin Digital, Backbase,
  Finastra and Bottomline** — no entity under any of those names appears in the SEC ticker map
  (`peers/private_check.txt`), so no periodic filing was available to compute; their ownership is not
  asserted here. **FIS** is a registrant and was not computed.
  **Adjudication, under the narrow-only rule carried by the ACLS, KLAC, AMAT, LRCX and ACMR runs: an
  additional competitor can only narrow a moat, never widen one.** Alkami is already last in the computed
  row on both owner-earnings measures and on GAAP margin, so no unpriced peer can lift it to IN. **The gap
  is recorded as a row limit, not as PROVISIONAL** (the PLAB rule), because no outcome of the fetch moves
  the verdict.
- **[E3-61] limit:** the row shows position, not conduct.

**What the row says, read plainly.** In this value chain the returns are earned by the **core
processors** — Jack Henry at a 25.0% operating margin and an 18.6% owner-earnings margin, Fiserv at 27.5%
and 18.6% — and the digital overlay vendors have spent the whole five-year window at or below zero on the
cumulative measure (Q2 Holdings −1.4%, nCino −6.6%, Alkami −21.4%). The Q2 Holdings 10-K states the
mechanism in a risk factor, and Alkami's 10-K carries the same dependency: core providers *"may have an
advantage over us with customers using their software by having better ability to integrate with their
software and by being able to bundle their competitive products with other applications used by our
customers and prospective customers at favorable pricing. We do not have formal arrangements with many of
these third-party providers regarding our access to their APIs."* Jack Henry's 10-K sells *"digital
banking"* as a native part of its own core platform (Banno). **The overlay vendor depends for its
integrations on the incumbents it competes with, and the incumbents can bundle.**

**[E4-04] — must the moat be continuously rebuilt, and does the spending defend the same advantage or buy
its replacement?** R&D is **26.7% of revenue** (28.8% in FY2024). The 10-K: the market is
*"characterized by rapid changes in technology"*, and *"Rapid technological changes and the introduction
of new products and enhancements by new or existing competitors or large FIs could undermine our current
market position"*; the AI risk factor adds that *"our competitive position could be harmed if we fail to
adopt and integrate AI effectively"* **The filed deal record shows spending that buys replacements:**
MK Decisioning was bought on 2021-09-10 for ~$20M plus an earn-out worth $15.5M at closing; the earn-out
was written to zero in 2022 *"as a result of changes in the expected timing of new customer sales and
implementations"*; and in March 2025, *"due to the acquisition of MANTL"*, the remaining MK intangible and
capitalised software assets were written off because they *"would not have future economic benefit"* (10-K FY2025 note 16). **The filing
ties the write-off of the 2021 purchase (~$20M, decisioning) to the 2025 one ($375.5M, onboarding, account
opening and loan origination) within four years.** That is [E4-04]'s excluded class — *"a moat that must be continuously rebuilt will
eventually be no moat at all"* — at the level of the product suite.

**[E4-32] — direction.** **Operating economics improving; moat not shown to widen.** The margins in bull
point 4 are rising, the unit series rises, win rates rose; but the one filed statement about price is a
concession, the pure-play competitor with the longest history earns a 5.0% GAAP margin at nearly twice
Alkami's size, and organic growth slowed from 22.4% (FY2025) to 15.9% (Q2-2026). **Direction recorded as
IMPROVING SCALE ECONOMICS, which is not the same thing as a widening moat** — [E4-32] is explicit that the
criterion is the moat's width, *"that does not necessarily mean that the profit is more this year than
last year."*

**Untapped pricing power [E3-33, E5-28]?** **Not claimed.** It would claim near-monopoly; Alkami serves
301 of the ~2,500 institutions it targets (about 12%), is one of ten names in its closest
rival's competitor list, and files a price-concession history. **[E2-53] dominance? No.** **[E4-36] — which cause
of success?** **Extreme performance on one variable, product breadth and speed** (*"Our ability to win and
retain clients is a function of consistently striving to offer a platform with products and configurations
that exceeds those of our competition"*) — a have-to-be-smart-every-day cause, not an ownable one.

**The attacker's test [E2-45].** How would I compete with it, with ample capital and skilled people?
**Alkami is itself the answer**: a well-funded attacker that has taken 301 platform clients from
incumbents in the replacement market since 2009. The same door is open to the next attacker, and to the
core vendors that already hold the client's core contract and can bundle.

**[E4-23] — key-person dependence.** Not filed as a founder-dependent business; the CEO (Alex Shootman) and
CFO are named as key employees in the ordinary form. **Not a moat defect here.**

- Needed or desired **[x]** · no close substitute **[ ] — fails: ten substitutes in the
  competitor's 10-K (nine named beside Alkami, plus the author), and "each of our digital banking client wins is a competitive takeaway"** · not
  price-regulated **[x]**
- Must the moat be continuously rebuilt? **Yes — rapid technological change is filed, R&D is 26.7% of
  revenue, and a 2021 acquisition was replaced by a 2025 one and written off [E4-04].** Depends on a great
  manager? **No.**
- Primary moat metric and trend: **owner-earnings margin −9.5% (last in the row) and improving; GAAP
  operating margin −12.1% (last); price concessions filed.**
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: improving scale economics, not a
  widening moat**

**VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**OUT, on the business.** The evidence is here and the business fails the franchise test on five
independent filed grounds: criterion (2) fails on the closest competitor's list of ten substitutes and on
Alkami's own statement that every win is a takeaway **[E3-03]**; the company discloses past and expected
price reductions and a price that falls as the client succeeds **[E2-44] first half, [E4-37]**; there has
been no return on capital in any of seven filed years, and Alkami is last in the computed row on every
return measure **[E3-46]**; five years of growth took $525.7M of acquisitions and $246.0M of stock pay
against −$23.0M of operating cash **[E2-44] second half**; and the moat must be continuously rebuilt, with
the product line's own acquisition history showing the spend buying replacements **[E4-04]**. **The file
closes here.**

*Asked aloud: can I name a document that would move this?* The private competitors' financials
(Candescent, CSI, Lumin, Backbase) could only narrow a moat already rated NONE; FIS's filing is of the same
class as Fiserv's. **No.** *And why OUT rather than UNKNOWABLE, given the Q2 Holdings scale curve?*
Because the verdict does not rest on Alkami's current losses alone. It rests on the substitute list, the
filed price concessions and the rebuild requirement, which are facts about the **industry position** and do
not change with scale — and the pure-play competitor that has already reached scale earns a **5.0% GAAP
operating margin**, which is not *"high rates of return on capital"* either. The scale curve is a reason
Alkami's losses may shrink; it is not evidence of a franchise. Recorded against the verdict at Q6 as the
first refutation condition.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT and the file closed there.** Built in full because the
brief required the earnings releases, the proxy and the [E2-49] check, and because a Q2 OUT written
without the manager record would be an opinion. **Nothing here promotes the name; a strong Q3 cannot
repair Q2 [E2-37, E2-38, E3-39].** No gate was assumed short.

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution — ticked, on [E3-43].** Q2 found no franchise, and the 1991 original is exact:
      *"a business, unlike a franchise, can be killed by poor management."* A vendor that must win each
      client from an incumbent, ship against *"rapid changes in technology"*, integrate an acquisition a
      quarter's revenue in size, and keep API access to cores it does not contract with is a
      have-to-be-smart-every-day business.
- [ ] **Control [E1-16]** — not ticked; an exitable Nasdaq share. *Recorded because it bears on the
      quote:* three holders of record at the 2026 record date held a third of the company (General
      Atlantic 13.9%, now 18.1% with a Section 203 waiver to 19.9%; S3 Ventures 13.3%, whose founder
      Brian R. Smith chairs the board; George B. Kaiser 6.1%), and an activist (JANA) is pressing for a
      sale. A classified board with three-year staggered terms (10-K Item 1A).
- [ ] **Leverage [E3-29]** — not ticked; not a balance-sheet-leveraged business. Named anyway: $345M of
      convertible notes against negative tangible equity (Step 0).

**One ticked → Q3 is a BINARY GATE and no price compensates [E1-16, E3-29, E5-35].**

### HONESTY — binary, filings-based, each matter dated to when it became PUBLIC [E5-16]

| date public | matter | what the filing says | disqualifier? |
|---|---|---|---|
| 10-K FY2021-FY2025 | legal proceedings | *"there are no claims or actions pending against us, the ultimate disposition of which would have a material impact"* (Item 3, FY2025) | **No.** Nothing to read. |
| 10-K FY2022-FY2025 | internal control | ICFR opinions from Ernst & Young (auditor since 2017) unqualified; **no material weakness disclosed in any 10-K read** (FY2021-FY2025 searched); MANTL excluded from the FY2025 ICFR scope as a 2025 acquisition, as the rules permit | **No.** |
| FY2023 and FY2024 10-Ks | "reclassified certain amounts ... to conform to current periods presentation" | FY2022 figures moved between vintages: OCF −$37,788k (FY2022 10-K) → −$38,045k (FY2024 10-K); cash SBC add-back $45,395k → $44,592k; capitalised software $3,645k → $3,388k. **A reclassification of $257k-$803k between lines, disclosed as such, not a restatement**; this run uses the newest vintage | **No — a weak-accounting prompt, read and closed.** |
| 10-K FY2025 note 17 | CU Cooperative, a vendor whose CEO (2016-2023) sat on Alkami's board through May 2025, paid **$6.2M in 2023** for services resold to clients | disclosed in the income-statement footnote and the related-party note | **No.** Disclosed, dated, bounded. |
| DEF 14A 2026 | related persons: Pendo (a General Atlantic portfolio company) **$606k**; Allstacks and Arpio (S3 portfolio companies) **$146k and $140k**; **the CEO bought 45,000 shares from the company on 2025-11-07 at $19.45, the Nasdaq close** (~$875k) | *"on terms the Company believes are consistent with those it could obtain in arm's length transactions"*; CEO purchase *"approved by our Board"* | **No.** Small, disclosed; the CEO purchase is at market and in his own money. |

**No integrity disqualifier found.** *A Q3 pass is the absence of found disqualifiers, not a finding that
the managers are honest [E5-17].*

### THE FLAGS [E4-22, E5-15, E4-29] — prompts to read, and I read them

- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRES, in all three places the CGNX instruction
  names, and in the pay.**
  - **The releases:** every one of the five read (Q4-2024 through Q2-2026) lists **"Adjusted EBITDA"** as a
    headline highlight and guides it quarterly and annually; **"Non-GAAP gross margin"** (cost of revenue
    excluding amortization **and stock-based compensation**) is the third bullet. The Q3-2025 release:
    *"We outperformed our Adjusted EBITDA target by 18%."*
  - **The 10-K:** Adjusted EBITDA is the **first of the four "Key Business Metrics"** in every 10-K from
    FY2021 to FY2025. It adds back **stock-based compensation ($80.1M in FY2025) — larger than the
    Adjusted EBITDA itself ($59.1M)** — and *"stockholder matters related expenses"* ($599k in FY2025, the
    first year such a line appears, the year the activists arrived).
  - **The pay:** the 2025 Senior Executive Bonus Plan was **60% GAAP revenue, 40% Adjusted EBITDA** (DEF 14A
    2026). **Revenue came in at 99.1% of target and paid 77.3%; Adjusted EBITDA came in at $59.1M against a
    $59.2M maximum and paid 197.2%; the blended payout was 125.3%.** The same shape a year earlier (DEF 14A
    2025): revenue $334M against a $335M target, Adjusted EBITDA $27M against a $28M maximum, blended
    125.1%. **In both years the GAAP metric missed and the non-GAAP metric carried the bonus above target**
    — [E5-41]'s mechanism: the measure that deletes the expense already paid is the one that pays.
  - **The long-term equity is 100% time-vested RSUs** with no performance condition (DEF 14A 2026: *"2025
    annual equity-based awards consisted of RSUs"*), so **no part of executive pay is measured on owner
    earnings, cash after stock compensation, or return on capital.**
  - *In management's favour, recorded:* the releases also publish **free cash flow** (FY2025 $34.2M;
    H1-2026 +$12.4M in Q2 against −$7.4M in Q1), and the 10-K's Adjusted EBITDA caveat is standard; and in
    2026 the committee added a **one-year holding period** on RSU shares for NEOs.
- [x] **trumpeted earnings projections [E4-22] — FIRES in form, and [E3-48]'s record check is taken.**
  Quarterly and annual guidance on revenue and Adjusted EBITDA in every release; the MANTL announcement
  (2025-02-27): *"Alkami solidifies its position as the de facto digital sales and service platform in
  the industry"* and *"the fastest-growing digital banking platform among all U.S. financial
  institutions."* **The record of the people who made the projections, on the documents held:** FY2025
  guidance at Q3-2025 **$442.5-444.0M revenue / $56.0-57.0M Adjusted EBITDA; actual $443.6M / $59.1M —
  met.** FY2026 guidance **$525.5-530.5M / $93.5-97.5M (Feb) → $527.1-530.9M / $94.9-97.9M (Apr) →
  $528.0-531.0M / $96.0-98.0M (Jul)** — narrowed upward twice. **On this short record the guide has been
  met, recorded in management's favour.** No long-term numeric target was found in the releases read.
- [x] **serial share issuance [E5-15] — FIRES.** Cover counts **85,936,693 (2021-04-30) → 106,941,980
  (2026-06-30), +24.4%**; evergreen reserves of 5% (2021 Plan) and 1% (ESPP) a year; RSU grants of 3.8M
  units in 2025. The first repurchases ($15.0M in Q2-2026 and $10.0M in July, 1,416,195 shares) came
  **after** JANA's first 13D (2026-04-01) against **4,013,092 shares added in FY2025 alone** — about 35% of one year's issuance. The cash paid to net-settle vesting taxes was $16.0M (2023), $12.8M (2024), **zero in 2025** and $5.0M in
  H1-2026; the FY2025 equity statement shows 3,295,924 RSU shares issued on vesting with no withholding
  payment, so the year's issuance ran gross.
- [ ] **weak accounting** — not ticked beyond the reclassification row above.
- [ ] **unintelligible footnotes** — **not ticked.** Deferred-cost roll-forwards, the D&A split, the
  capitalised-SBC amounts and the MANTL allocation are all filed in plain form. **One disclosure gap,
  recorded as an absence claim with its sweep:** the FY2025 10-K and the five releases were searched for
  "churn", "attrition", "retention rate" and "gross revenue retention" — **no revenue-churn or gross
  retention figure found** — while Q2 Holdings files a revenue churn rate (5.2% FY2025). Earlier Alkami
  10-Ks (FY2021, FY2022) described user growth from existing clients as *"(net of attrition)"*; from FY2023
  the parenthesis no longer appears.
- [ ] **filed-figure tells [E4-30]** — **not ticked**: revenue growth is not smooth (32.9%, 26.1%, 29.6%,
  34.2%), and cash taxes are state and Indian minimums on a loss-making filer. *One prompt recorded, not
  scored:* Adjusted EBITDA landed **$0.1M under the 200% bonus maximum** in FY2025 and $1M under it in
  FY2024.
- [ ] **metric-switching [E2-49] — NOT FIRED.** The 10-K's four key business metrics are **identical in every
  vintage FY2021-FY2025**: Adjusted EBITDA, ARR, Registered Users, RPU. The pay metrics are revenue and
  Adjusted EBITDA in both 2024 and 2025 (and *"revenue and profitability financial metrics"* in the 2023
  and 2024 proxies). **One definition was reworded, recorded as an open prompt rather than a fire:** from the
  2025 10-Qs a registered user is someone who *"has access as of the last day of the reporting period"*,
  where FY2021-FY2024 said one *"who has registered to use one or more of our solutions and has current
  access to use those solutions"*; the new text also excludes users of acquired products only. **No reason
  is given and the FY2024 comparative (19,984 thousand) is unchanged**, so whether the count basis moved
  cannot be established from the filings. **The brief's tally is stale, and so was the last fold's:** the
  prior stood at six fires and five failures only before ROKU (fired), ACMR (did not fire) and SWK (fired);
  the SWK fold's *"seventh fire against five failures"* omitted ACMR's failure. **Reconciled: FIRED at SHOP,
  MRVL, PAY, ARM, CALX, BE, ROKU, SWK (eight); FAILED at QLYS, CRM, CORT, PLTR, INOD, ACMR, and now ALKT
  (seven).**
- [ ] **dividends funded by issuance [E2-52]** — no dividend.
- [ ] **stock-price targeting [E3-50]** — no market-capitalisation vesting condition found in the proxy;
  the RSUs are time-based.
- [ ] **the restructuring charge [E3-53]** — none; the MK write-off ($1.7M) was taken as a separate line
  and quantified.

**[E4-52] — do the flags converge?** **Partly.** Adjusted EBITDA as the release headline, the first 10-K
metric, 40% of the bonus and the guided number, while the expense it deletes (stock pay) is the
business's largest cost after the resold services and the reason owner earnings are negative — **that is
one system pointing one way: the number management is paid on is the number that omits what the owners
pay.** The countervailing facts are real: guidance met, free cash flow printed, no restatement, no
price-targeting device.

### STEP 3 — THE PRIMARY TEST [E2-01]

**No earnings rate on equity to report: net loss in every year FY2019-FY2025**; ROE negative throughout
(FY2025 −13.2% on average equity of $359.5M). On [E2-43]'s *"unleveraged net tangible assets"* the
denominator is **negative** (tangible equity −$186.4M at 2026-06-30) and operating income is negative, so
the ratio is not meaningful. [E2-42]'s red light — the five-year average *"much below the return on
equity earned ... by American industry in aggregate"* — **is on.** [E3-54]'s retention test does not
apply: there are no retained earnings; the accumulated deficit is $523.9M.

**The half-owner test [E2-26].** *Mostly passes.* The deferred-cost roll-forwards, the capitalised-SBC
figures, the D&A split, the MANTL allocation and the cash-settled MANTL awards quantified separately at
every line; free cash flow printed beside Adjusted EBITDA. **Where it fails:** no churn or gross
retention figure, which is the number a half-owner of a subscription business most wants; the SBC
exclusion in every release headline; an unexplained reworded user definition.

**The institutional imperative — all four [E2-30]:**
- [ ] resists change — **no** (CEO change 2021, CFO change 2025, two new directors 2026, buyback begun).
- [x] **projects or acquisitions to soak up funds — yes, in the form available:** three acquisitions in
  five years totalling $525.7M in cash, the largest financed by $345M of convertible notes in a year of
  negative owner earnings, and the first of them written off on buying the last.
- [ ] staff studies — not observable from filings.
- [x] **peer behaviour imitated — yes, filed:** the competitor row shows Q2 Holdings with the same
  financial structure (convertible notes with capped calls in its cash-flow statement, SBC above 10% of
  revenue); the 2025 compensation peer group names Q2 and nCino.

**Capital allocation — the buyback conditions [E5-08, E4-31].**
- (1) ample funds? **No, on the owner-earnings test**: $81.0M of cash and securities at 2026-06-30 against
  $345M of notes and negative owner earnings on every construction; the repurchases were enabled by a
  lender consent (Fifth Amendment) to use $100M of cash.
- (2) a material discount to intrinsic value, conservatively calculated? **Not demonstrable**: on owner
  earnings the conservative value is not a positive number (Q5 computation), and $25.0M was spent at about
  $16.96 (Q2) and $18.81 (July).
- (3) [E4-31] shareholders supplied the information to estimate value? **Partly** — no churn figure.
- **CAPITAL ALLOCATION FLAG, stated with the humility clause [E4-13]:** *"it is natural for CEOs to be
  optimistic about their own businesses. They also know a whole lot more about them than I do."* The flag
  is the sequence: cash acquisitions funded with convertible debt while owner earnings were negative, then
  a buyback begun under activist pressure. **[E5-44] on the MANTL paper:** the $13M of replacement RSUs is
  small against $375.5M of cash, so the stock-deal law barely bites. Binds position size; there is no
  position.

**THE GUARDRAIL — checked before the verdict.**
- [x] Nothing in this Q3 is used to promote the name **[E2-37, E2-38, E3-39]**.
- [x] No key-person dependence to move to Q2 **[E4-23]**.
- [x] Is a great manager the reason to act? **No** — the franchise is not intact (Q2 NONE), so the
      excisable-cancer exception **[E2-35, E2-36]** has nothing to apply to.

**VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] NOT REACHED — closed at Q2.**
*Had Q2 been IN, this would read **IN on honesty** (no disqualifier found) with **[E4-29] firing in the
releases, the 10-K metrics and the bonus**, serial issuance, and a **capital-allocation flag** — under a
binary-gate weight case the gate would have had to be argued, not assumed.*

## Q4 — WILL IT SURVIVE?

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT.** Built in full because the brief required the screen's ends
reproduced, every window rebuilt on both (c) ends, the SBC completeness and grant-date checks, the
payables flag reconciled, and the perimeter decided.

### THE DEFECT IN THE QUEUE'S NUMBER, FOUND BEFORE ANYTHING ELSE

The row reads **`oe_bottom_m -67 | oe_top_m -57`**. **Both reproduce, and they come from different windows
AND different (c) ends — the INTC/BA/ACMR/SWK defect a fifth time.** `oe_bottom` is the **5-year
FY2021-25 mean at the D&A-as-filed end**: −$66,602k. `oe_top` is the **3-year FY2023-25 mean at the capex
end**: −$56,534k. Both use the **earliest** FY2022 vintage (OCF −$37,788k, capitalised software $3,645k)
and the SBC max-rule, which for FY2025 picks the P&L charge of $80,098k — **$3.9M higher than the
cash-flow add-back, because it includes MANTL awards settled in cash and already deducted inside operating
cash (a double count in the conservative direction).** Script: `oe.py`, output `oe_out.txt`.

**And the D&A-as-filed end is the wrong default for this filer.** FY2025 D&A of $26,912k is **$4.6M of
property-and-equipment depreciation and capitalised-software amortization plus $22.3M of amortization of
acquired intangibles** (Step 0 cross-check 3). **[E3-44]** is the default and it says what to add back:
*"the depreciation charge is not inappropriate in most companies to use as a proxy for required capital
expenditures. Which is why we think that reported earnings plus amortization of intangibles usually gives
a pretty good indication of earning power"* — and **[E2-43]**: *"amortization charges should be
ignored."* **So the corpus default end for (c) is depreciation excluding the amortization of acquired
intangibles**, and the screen's D&A end charges the MANTL purchase price as if it were maintenance.

### THE SIGN CHANGE LABEL AND THE ROW'S INTERNAL TENSION — RESOLVED FROM THE FILINGS

`level_note` says SIGN CHANGE (early years loss-making, recent ones not); `level_note_oe` says STILL
NEGATIVE (both halves at or below zero). **Both are right, because they describe different series:**

| FY | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | TTM 6/26 |
|---|---|---|---|---|---|---|---|---|
| operating cash flow | −39,085 | −38,145 | −28,959 | −38,045 | −17,502 | **+18,597** | **+42,906** | **+64,633** |
| stock compensation (equity statement) | 1,250 | 1,954 | 14,535 | 45,395 | 52,686 | 60,767 | 76,679 | 75,512 |
| **OCF − SBC** | **−40,335** | **−40,099** | **−43,494** | **−83,440** | **−70,188** | **−42,170** | **−33,773** | **−10,879** |

*$ thousands.* **Operating cash changes sign in FY2024; operating cash after stock pay never does.** Between
FY2021 and FY2025 operating cash rose **$71.9M** while stock compensation rose **$62.1M**: **86% of the
"recovery" in operating cash is the company paying its people in shares instead of cash.** The SIGN CHANGE
label is right about the line it measured and wrong about owner earnings, which is the only line the
framework asks about — **the same error class as ACMR (a label describing screen arithmetic, not the
business), in a different direction: ACMR's label was wrong in direction, ALKT's is wrong in object.** The
TTM improvement to −$10.9M is real but carries $9.7M of the payables build examined below.

### Owner earnings — the one number **[E2-23]**

**Construction** *(CONVENTION, per the framework)*: operating cash flow **less stock-based compensation in
full [E5-06]**, **less (c)**. Inputs from the **filed cash-flow statement of the newest 10-K carrying each
year**; TTM = FY2025 − H1-2025 + H1-2026 (10-Q Q2-2026).

**SBC — resolves every year, and is COMPLETE on the charge measure, with two measures shown.**
- The cash-flow add-back resolves every year FY2019-FY2025 and in both 10-Qs. **The equity-statement credit
  to paid-in capital is used as the complete measure**, because it also carries SBC capitalised into
  software and into deferred implementation costs ($0.9M and $0.6M in FY2025; note 4, note 9), which is in
  neither the add-back nor cash capex. The two differ by $0.5M-$1.5M a year; both are in `oe_out.txt`.
- **The cash-settled MANTL acceleration ($3.9M, 2025)** is inside operating cash already and is **not**
  subtracted again.
- **Stock-settled bonuses: none found. 401(k) match: in cash** (25% of contributions up to 8% of salary,
  $2.5M in FY2025, note 15) — **the Boeing class does not apply. ESPP: included** in the SBC charge (a
  compensatory 15%-discount plan, note 2). **Acquisition-related stock comp:** the MANTL replacement RSUs
  (~$13M announced; $821k treated as purchase consideration) run through SBC after the combination.
  **2020's tender offer carried $6.1M of compensation expense** (10-K FY2021 MD&A) paid through a $11.3M
  financing-section repurchase — so **FY2020 operating cash overstates by up to $6.1M**, outside the
  five-year window, recorded.
- **[E3-70], because SBC exceeds 50% of operating cash in every positive-OCF year (320% FY2024, 178%
  FY2025, 117% TTM) — the grant table read by hand.** Grants × grant-date fair value (10-K RSU and option
  roll-forwards): **FY2021 $107.0M** (2,915,667 RSUs at $28.48 + 2,811,098 options at $8.53) · **FY2022
  $81.1M** (5,771,008 at $14.06) · **FY2023 $59.3M** (3,676,190 at $16.12) · **FY2024 $68.1M** (2,550,824 at
  $26.69) · **FY2025 $106.6M** (3,790,874 at $28.13). **Five-year total $422.1M gross, $365.0M net of
  forfeitures at their own grant-date values, against a $250.1M charge.** On the net-grant measure FY2025
  owner earnings at the capex end are **−$56.8M** (charge measure −$42.5M). **Both are reported; the charge
  is the floor of the subtraction, not the measure [E3-70]. No construction changes sign.**

**(c) — what the filer capitalises, and which class it is in.**
- **Capitalised into property and equipment:** purchases of equipment ($1.5M FY2025) and **internal-use
  software development** ($7.1M FY2025, application-development-stage coding and testing, 5-year life). Both
  are investing cash. **Capitalised software is treated as capex for owner earnings** — Q2 found the
  product must be continuously rebuilt [E4-04], so it is a recurring cost of staying in business.
- **Capitalised into other assets, inside operating cash:** **deferred commissions** ($13.4M capitalised,
  $6.4M amortized, FY2025), **deferred implementation costs** ($12.2M, $6.3M), and cloud-computing
  implementation costs in prepaid and other assets (amount not separately filed). All run through the
  "Deferred costs" and "Prepaid" working-capital lines, **so they are already deducted in operating cash.**
- **The ELF triple-count class: ALKT is NOT in it.** The D&A add-back of $26,912k is exactly depreciation
  ($4.6M) plus acquired-intangible amortization ($22.3M) — **no amortization of the deferred costs sits in
  D&A** (Step 0 cross-check 3; the amortization runs inside the working-capital line). *Contrast, recorded
  for the row: Q2 Holdings adds back "Amortization of deferred implementation, solution and other costs"
  ($30.1M) as a separate non-cash line — that filer is in the class; this one is not.*
- **A disclosed judgment, not a computation [E2-23]:** the two ends shown are **depreciation excluding
  acquired-intangible amortization** (the [E3-44] default, the lenient end here) and **total capex including
  capitalised software** (the conservative end). The capex end is the better guess, for the [E4-04] reason
  above. **The growth portion of the deferred costs** (capitalised minus amortized: $12.9M in FY2025) is a
  lenient-direction consideration — a steady-state business would capitalise less than it grows now — and
  **adding it back does not change the sign of any year** (adding back the "Deferred costs" working-capital
  line, −$12.3M in FY2025 and −$12.4M TTM: FY2025 capex end −$42.5M → about −$30.2M; TTM −$20.3M → about
  −$7.9M).

| FY | OCF − SBC | (c) depreciation ex-acquired | (c) capex + cap. software | **OE, D&A-ex end** | **OE, capex end** | D&A as filed (screen) |
|---|---|---|---|---|---|---|
| 2019 | −40,335 | 2,226 | 3,689 | **−42,561** | **−44,024** | −42,561 |
| 2020 | −40,099 | 2,575 | 2,147 | **−42,674** | **−42,246** | −42,874 |
| 2021 | −43,494 | 2,343 | 3,697 | **−45,837** | **−47,191** | −46,937 |
| 2022 | −83,440 | 2,975 | 4,445 | **−86,415** | **−87,885** | −90,712 |
| 2023 | −70,188 | 3,831 | 6,292 | **−74,019** | **−76,480** | −79,364 |
| 2024 | −42,170 | 3,708 | 7,855 | **−45,878** | **−50,025** | −51,348 |
| 2025 | −33,773 | 4,612 | 8,689 | **−38,385** | **−42,462** | −60,194 |
| **TTM 6/26** | **−10,879** | 5,700 | 9,436 | **−16,579** | **−20,315** | −42,890 |

*$ thousands. OE columns use the equity-statement SBC; the last column reproduces the screen's construction
(cash-flow SBC, D&A as filed). FY2020-22 depreciation from note 4 of the FY2022-FY2024 10-Ks; acquired
amortization $0.2M / $1.1M / $5.1M / $6.8M / $6.8M / $22.3M FY2020-25; H1 splits from the Q2-2026 10-Q notes.*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38].** Every contiguous window of three
years or more, both (c) ends, both SBC measures (full table `oe_out.txt`):

| window | D&A-ex end | capex end |
|---|---|---|
| **5y FY2021-25 (the default [E2-42])** | **−$58,107k** | **−$60,809k** |
| 5y FY2020-24 | −$58,965k | −$60,765k |
| 5y FY2019-23 | −$58,301k | −$59,565k |
| 3y FY2023-25 | −$52,761k | −$56,322k |
| 3y FY2022-24 | −$68,771k | −$71,463k |
| 3y FY2021-23 | −$68,757k | −$70,519k |
| 3y FY2019-21 | −$43,691k | −$44,487k |
| 4y FY2022-25 | −$61,174k | −$64,213k |
| 6y FY2020-25 | −$55,535k | −$57,715k |
| 7y FY2019-25 (all filed OCF years) | −$53,681k | −$55,759k |
| **TTM to 2026-06-30** | **−$16,579k** | **−$20,315k** |

- **Combined range, fifteen annual windows × both (c) ends × both SBC measures: −$71.5M to −$43.7M.**
  Including the trailing twelve months: **−$71.5M to −$16.4M.**
- *Is the range too wide to conclude?* **No — it does not span zero on any window, either (c) end, either
  SBC measure, the grant-date measure, or the TTM.** The conclusion is that no construction produces owner
  earnings.
- **The perimeter decision.** MANTL (2025-03-17) sits inside only FY2025 and the TTM; Segmint (2022-04-25)
  inside FY2022 onward; MK (2021-09-10) from FY2021. **Pro forma is not buildable**: no MANTL, Segmint or
  MK standalone statements were filed (the MANTL closing 8-K's Item 9.01 lists only the merger agreement), and
  "pro forma" appears in none of the FY2025 10-K, the Q3-2025 10-Q or the Q2-2026 10-Q (searched). **A
  current-perimeter window is one year and a quarter long**, shorter than any window the corpus accepts. **So
  the windows are published as filed, with the direction of the bias stated:** MANTL entered with $79.9M of
  federal NOLs and a full valuation allowance (note 10), i.e. a loss history, so pre-2025 years do not
  flatter the current perimeter by omitting MANTL losses they never contained; and the TTM, which carries
  MANTL whole, is the least negative figure in the table. **The acquisition cash itself ($525.7M) is
  outside owner earnings by construction and is recorded against [E2-44] at Q2 and [E2-30] at Q3.** *(The DKS
  instruction asked for a pro forma where the filed pro forma table existed; here none does, and the verdict
  does not depend on it — every window is negative with or without the deals.)*
- *A distorted year in the window [E5-11]:* **FY2025, favourably, on the payables line — next.**

### THE WC_NOTE — FY2025 ACCOUNTS PAYABLE AND ACCRUED LIABILITIES, RECONCILED

- **Confirmed: "Accounts payable and accrued liabilities" +$19,708k ÷ OCF $42,906k = 45.9%** (the row's 46%).
- **What moved, from the balance sheet** (10-K note 7): accrued liabilities $24,520k → $47,359k and accounts
  payable $6,129k → $5,842k; MANTL brought $1,163k of accrued and $1,653k of payables at acquisition, so the
  organic build is about **+$19.7M, equal to the cash-flow line.** By component: **bonus accrual +$7.9M**
  ($7,989k → $15,865k), third-party solution costs +$4.4M, other +$4.3M, commissions +$2.4M, vendor purchases
  +$2.4M, client refunds +$0.9M, self-insurance +$0.5M.
- **It INFLATED FY2025.** Without the line, FY2025 operating cash was **$23.2M**, not $42.9M, and OCF − SBC was
  **−$53.5M**, not −$33.8M. FY2024's line was +$3.3M.
- **It unwound in 2026, in part, in the 10-Qs:** **Q1-2026 −$15,740k** (the 2025 bonuses paid), Q2-2026
  +$9,947k, **H1-2026 −$5,793k**; accrued liabilities fell to $35,176k while payables rose to $12,330k at
  2026-06-30. **The TTM still carries +$9.7M of it** ($19,708k − $4,199k − $5,793k); **ex-line TTM OCF − SBC is
  about −$20.6M.**

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · **[x] gruesome**
- *"grows rapidly, requires significant capital to engender the growth, and then earns little or no
  money."* **Revenue compounded 34.9% a year FY2019-FY2025 ($73.5M → $443.6M); cumulative owner earnings over
  the seven filed years −$375.8M at the D&A-ex end and −$390.3M at the capex end; $525.7M of acquisitions;
  $253.3M of stock compensation; $192.8M of IPO proceeds, $213.9M of 2020 preferred and $345M of notes to fund
  it.** **[E4-43]'s protection for the good class does not apply:** there is no rate earned on the deposits
  added. **The strongest fact against "gruesome"** is the trajectory (TTM −$16.6M to −$20.3M, about a fifth to a quarter of the
  FY2022 figure), and it is recorded for Q6.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — NO.** Owner earnings negative in every year and window;
  operating cash negative in five of seven years; the best year leaned on a payables build.
- **(2) massive liquid assets — NO.** Cash $45.5M and marketable securities $35.4M at 2026-06-30 = **$81.0M**,
  against $345M of notes. A **$225M undrawn revolver** is available — and **[E5-39]** counts no bank line:
  *"We will never be dependent on the kindness of strangers."*
- **(3) no significant near-term cash requirements — PARTIAL FAIL, and two dates are close.**
  - **The revolver covenants change on the Financial Covenant Trigger Date, 2026-12-31**: the recurring-revenue
    growth (≥10%) and $35M liquidity tests fall away and **net leverage < 5.50x, interest coverage > 3.00x and
    senior net leverage < 3.50x** take effect; a **free-cash-flow covenant ≥ $0** applies through
    2026-09-30 (note 8). *(The recurring-revenue growth covenant is 10% against Q2-2026 revenue growth of
    15.9%.)* Compliance reported at 2026-06-30.
  - **$345M of 1.50% notes due 2030-03-15, puttable at par on a "fundamental change"** — which a sale of the
    company, the outcome JANA's 13D seeks, would be (note 8).
  - Purchase commitments **$44.4M within 12 months** ($77.5M over five years); leases $2.8M.
- **Leverage, named and quantified [E4-16, E3-29]:** **net debt $264.0M**; tangible equity −$186.4M; **the
  [E2-54] coverage test fails** — FY2025 interest paid $5.9M was not *"comfortably met out of current cash flow
  net of ample capital expenditures"* on owner earnings (−$42.5M); on the company's own free cash flow ($34.2M,
  before stock pay) it would pass. **The corpus test is cash flow after all costs, and stock pay is a cost
  [E5-06].** The notes carry no maintenance covenants; the revolver does. *[E3-52]'s distinction applies: the
  notes are long-dated and covenant-light; the bank line is not.*

### Name the specific way THIS business dies **[E2-27, E3-24]**

**The mechanism: the stock stops being currency.** Alkami pays its people about $75-80M a year in shares
(17% of revenue) and cannot pay them in cash — cash after stock pay is negative. **If the share price falls
and stays down, the same grant value costs more shares (dilution accelerates) or must be replaced with cash
(owner earnings fall by the same amount).** Quantified from filed figures: **replacing FY2025's $76.7M of
stock compensation with cash would have turned $42.9M of operating cash into −$33.8M**; at the 2026-06-30
cover count, a year of grants at FY2025's value ($106.6M gross) is **5.2M shares at $20.51 and 7.3M at
$14.59** (the 2026-06-22 price) — **4.9% to 6.8% of the company a year.** Three things push toward the trigger,
all filed: (i) the core vendors bundle and control API access (Q2); (ii) organic growth has slowed from 22.4%
to 15.9%, and until 2026-12-31 the credit agreement tests recurring-revenue growth of at least 10%; (iii) FI consolidation — *"very few new FIs are being created."* **And the capital structure turns
a sale into a cash call:** the notes are puttable at par on a fundamental change, so the most likely
non-organic outcome (a sale, pressed by a 6.3% activist with 3.9% more in swaps) requires $345M to be
refinanced or converted.

**Likelihood:** [ ] likely **[x] a real possibility** [ ] a low-level possibility — for the dilution spiral in
a de-rating, because the 2026 price already fell to $14.59 (−52% from 2025-06-30) and the company responded
by buying shares back rather than cutting grants; *a low-level possibility* for insolvency, because the notes
mature in 2030 and the TTM is close to break-even before stock pay.

**[E4-51] — the bear case's opposite, stated so its holders would accept it:** *Alkami is a scale business
four years behind Q2 Holdings on the same curve; operating cash has risen five years running, Adjusted EBITDA
margin is 15% and guided to 18%; stock pay is a Silicon Valley convention that falls as a share of revenue;
the installed base renews at 70% gross margin; and the board, the largest holder and an activist all think the
company is worth more to a buyer than the market pays.* **Stated fairly, that case is about scale, a sale and
Adjusted EBITDA. It contains no owner-earnings number above zero, and the framework's Q4 is about owner
earnings.**

### THE [E5-11] SHAPE, AGAINST THE NAMED ONES

| run | shape | ALKT? |
|---|---|---|
| **ORCL** | contracted not to stop | **No.** $44.4M of 12-month purchase commitments; no build programme. |
| **ARM / CALX** | SBC ≈ all of operating cash | **Yes, and past it**: SBC 178% of FY2025 operating cash, 320% of FY2024's; cumulative FY2021-25 SBC $250.1M against cumulative OCF −$23.0M. |
| **BE** | too little filed history | **No.** Seven OCF years. |
| **BA** | spending cash undoing past work | **No.** |
| **SWK** | the self-liquidating distribution | **No** distributions; the 2026 buyback is small. |
| **ACMR** | growth refilled by selling the subsidiary | **No** subsidiary; the refill valve here is the **share register itself** — IPO, preferred, notes and RSUs. |
| **ALKT — the ARM/CALX shape with debt-funded acquisitions on top** | stock pay above operating cash, **plus** $525.7M of cash deals financed by convertible notes puttable on a sale | recorded, not named as new: it is CALX's shape with the SWK-style balance-sheet lever added. |

**VERDICT (recorded, not governing): [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** — had Q2 been IN,
Q4 would close OUT: owner earnings are negative on every window, both (c) ends, both SBC measures, the
grant-date measure and the TTM **[E2-23, E4-25]**; gruesome **[E4-20]**; strengths (1) and (2) fail
**[E5-11]**; [E2-54] fails on owner earnings. **The file's governing verdict remains Q2 OUT.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass. **Q2 returned OUT. Q5 is NOT opened.** What follows is the queue's
required price, **headed as operator rule 3 requires and carrying no entry language.**

---
# COMPUTATION — NOT A CLEARANCE

*Required by the queue's output contract of 2026-09-01: every run ends with a price. This is arithmetic
on a closed file. It ranks nothing and recommends nothing.*

**Inputs, dated.** Price **$20.51** (close 2026-09-11, aggregator quote, flagged) · share count
**106,941,980** (cover of 10-Q acc. 0001529274-26-000052, one class) · **market cap $2,193.4M** ($2,182.5M
after the July buyback alone) · net debt $264.0M, so enterprise value $2,457.4M · sovereign **5.35%** (US
Treasury 30-year par yield, 2026-09-11). Script `q5calc.py`, output `q5calc_out.txt`.

**1. THE YIELD**

| construction | owner earnings | ÷ $2,193.4M | vs 5.35% |
|---|---|---|---|
| **5y FY2021-25, D&A-ex end** *(the corpus default window [E2-42] and default (c) [E3-44])* | **−$58.1M** | **−2.65%** | **−8.00 pts** |
| 5y FY2021-25, capex end | −$60.8M | −2.77% | −8.12 pts |
| 3y FY2023-25, D&A-ex end | −$52.8M | −2.41% | −7.76 pts |
| **TTM to 2026-06-30, capex end** | **−$20.3M** | **−0.93%** | **−6.28 pts** |
| TTM, D&A-ex end | −$16.6M | −0.76% | −6.11 pts |
| TTM, capex end, without the unwinding payables build | −$30.0M | −1.37% | −6.72 pts |
| best of all fifteen annual windows (3y FY2019-21, D&A-ex) | −$43.7M | −1.99% | −7.34 pts |
| worst of all fifteen (3y FY2022-24, capex end) | −$71.5M | −3.26% | −8.61 pts |
| *for reference only:* **the best single period ever filed** (TTM, cash-flow SBC, D&A-ex) | **−$16.4M** | **−0.75%** | **−6.10 pts** |

**Every construction is negative. There is no positive year, window or trailing period in seven filed years.**

**2. WHAT THE PRICE ALREADY ASSUMES — in dollars, because a negative base has no growth rate.**
- to yield the **5.35% sovereign** at $20.51, Alkami must earn **$117.3M** of owner earnings a year
  ($131.5M on enterprise value, since the $345M of notes rank ahead of the shares).
- to clear the **~10% floor [E4-28]**, it must earn **$219.3M** ($245.7M on enterprise value).
- **$219.3M is 41.4% of the FY2026 revenue guide ($528.0-531.0M).** The highest owner-earnings margin in the
  competitor row is **18.6%** (Jack Henry, Fiserv); at that margin the floor needs **$1.18bn of revenue, 2.2x the
  guide** — about **5.7 years at 15% a year or 4.4 at 20%**, *and* a swing from −4.1% (TTM, capex end, on $489.7M of TTM revenue) to +18.6% on the margin.
  At Q2 Holdings' 10.9% it needs **$2.0bn, 3.8x the guide**. [E4-35]'s base rate applies to the growth alone:
  *"fewer than 10 of the 200 most profitable companies ... will attain 15% annual growth in earnings-per-share
  over the next 20 years"* — and this starts from **negative** owner earnings, not from the 200 most profitable.
- **What the price is also paying for, and it is not owner earnings:** the stock rose **+40.6% from $14.59 on
  2026-06-22**, the event date of JANA's 13D seeking a sale, with **General Atlantic at 18.1%** under a board
  waiver to 19.9%. **No agreement exists**, so this is not a spread (the ROKU treatment does not apply); it is a
  price for a transaction nobody has filed. [E2-28] names what a quote above the facts is for, and it is not
  buying.

**3. WHAT YOU ARE PAID.** **−6.1 to −8.6 points under the sovereign**, depending on construction; **−8.00 points**
at the default window and default (c). **A buyer at $20.51 is paid nothing on owner earnings and funds the
shortfall in dilution: FY2025's grants alone were 3.6% of the shares outstanding.**

**THE FLOOR, FIRST [E4-28].** Honest pre-tax expectancy at this price, on owner earnings: **negative on every
construction.** **Below roughly 10% the name is not ranked — it is quit on, whatever the sovereign is.** ALKT is
quit on twice: at Q2 on the business, and here on the arithmetic. **The ranking lines are not filled in [E4-21,
E3-45].**

**Value as a round-number range [E4-01].** *"Using precise numbers is, in fact, foolish."* **Every cash
construction is negative, so the owner-earnings value of the equity is not a positive number, and a range is
refused rather than invented.** What can honestly be said: the business has never produced a dollar of owner
earnings; the company's own free cash flow before stock pay ($34.2M in FY2025) capitalised at the sovereign would
be about **$0.6bn** — **and that figure treats $76.7M a year of stock compensation as free**, which [E5-06]
forbids. **Current price $20.51; cap $2.19bn.**

**WHICH BAR? NEITHER, and that is the finding.** The normal method [E4-11] needs a value to apply a margin to; the
screamer test [E4-01] needs a conservative case for the price to clear. **The conservative case is −$71.5M and the
optimistic −$16.4M; the price is above the whole range** — [E4-01]'s third outcome, *"no."* **Windage count:
one** — the (c) judgment at Q4, displayed as a band, never resolved to a point. The grant-date SBC measure
[E3-70] is reported beside the charge, not stacked on it.

**PRICE AND PASS/FAIL, PLAINLY:** **$20.51 · market cap $2,193.4M · FAIL at Q2 (OUT, on the business).**

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened as a hold/sell question — there is no position and none is contemplated.** Recorded as the
**refutation conditions** the framework requires of a closed file, pre-committed in writing per **[E1-02]** —
*"I believe in establishing yardsticks prior to the act"* — so that a re-opening is triggered by filed
evidence, not by a price move or a bid.

**THESIS-BREAKING METRICS, each read off a 10-K, 10-Q or proxy, each with a threshold.** The file re-opens at
Q2 if **three or more** turn, and is re-read if any single one does:

1. **Positive owner earnings at the capex end** (OCF − equity-statement SBC − capex − capitalised software) for
   **two consecutive fiscal years**, with the "Accounts payable and accrued liabilities" line below 20% of
   operating cash in each — the Q2 Holdings scale curve, arriving. *(The strongest fact against the verdict,
   pre-registered as the first condition.)*
2. **GAAP operating margin positive for a full fiscal year and at or above Q2 Holdings' in the same year.**
3. **A price increase filed as having held** — or the Item 1A sentence *"in the past we have had, and expect to be
   required in the future, to change our pricing model, reduce our prices or accept other unfavorable contract
   terms"* removed from a 10-K without being replaced by a weaker one.
4. **Stock compensation below 10% of revenue** for a full year, with the cover share count **not higher** than
   two years earlier (net of buybacks).
5. **A revenue churn or gross retention figure disclosed**, and at or below Q2 Holdings' filed revenue churn
   (5.2% in FY2025).
6. **Organic revenue growth at or above 15%** in FY2026 and FY2027 while condition 1 is met.
7. **Three years with no acquisition and no write-off of a prior acquisition's assets.**

**EVENTS THAT RE-OPEN STEP 0, NOT Q2:** a **definitive merger agreement** for ALKT (an 8-K Item 1.01 with a
merger agreement, a DEFM14A, SC 14D9 or SC TO-T) — the quote would then be a spread on deal terms and must be
re-struck as ROKU's was; a JANA or General Atlantic 13D/A reporting an agreement or nomination; any notice of a
fundamental-change repurchase on the 2030 notes.

**THE DIRECTION OF THE MOAT, the monitoring question [E4-17, E3-30]:** is the narrowing of the losses scale
economics arriving on a franchise that already exists, or the ordinary arithmetic of a competitive vendor growing
into its costs? *"Beliefs change quite gradually"* [E4-17]; the slow instruments are **owner-earnings margin
against Q2 Holdings'**, **stock compensation as a share of revenue**, and **organic growth**.

**Catalyst dates, all filed:** Q3-2026 release (late October 2026, per the Q3-2025 release date of 2025-10-29)
· **2026-09-30, the last quarter of the free-cash-flow covenant** · **2026-12-31, the Financial Covenant Trigger
Date** (leverage and coverage tests begin) · FY2026 10-K (~late February 2027) · the 2027 proxy (JANA's
*"board leadership"* item; Brian R. Smith drew 19,329,737 withheld votes against 52,065,034 for in 2026) ·
2028-03-20, the first date the notes may be called · 2030-03-15, note maturity.

**Position size:** none. **Reversal condition in words, not a price alert** (the QLYS ruling of 2026-09-07: a
price alert on a name that failed on the business is a category error).

**VERDICT: NOT REACHED — the file closed at Q2.**

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Step 0 → Q1 IN → Q2 OUT → file closed. Q3 and Q4 built
      under *"RECORDED, NOT GOVERNING"*; Q5 replaced by `COMPUTATION — NOT A CLEARANCE`; Q6 as refutation
      conditions only.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on filed documents;
      the unpriced-competitor limit sits at Q2, adjudicated by the narrow-only rule, and Q2 is OUT.
- [x] **Every UNRESEARCHED item names the artifact and where it lives.** Three, none verdict-moving: FIS's 10-K
      (EDGAR, CIK 0001136893, not computed); the three non-competitor documents in the "Alkami" full-text hits
      (Matterport 10-K, NCR Voyix exhibits, Clearwater Analytics 10-K/As — EDGAR, not opened); the reason for the
      2025 registered-user definition change (not in any filing; would need the company).
- [x] **Every UNKNOWABLE verdict states what cannot be known** — none used.
- [x] **Step 0: the filing was read, with accession numbers; three figures cross-checked**, all exact (OCF rebuilt
      from its detail lines; gross profit; the D&A split). Peer cells cross-checked against Q2 Holdings' and Jack
      Henry's filed cash-flow statements.
- [x] **Owner earnings on a multi-year mean; fifteen windows and TTM published; both (c) ends and both SBC measures;
      the grant-date measure beside the charge; the (c) judgment disclosed.**
- [x] **Competitor row filled** (five SEC filers, one formula), the ten companies Q2 Holdings names listed, six unpriceable
      and the limit stated.
- [x] **Sovereign for the earnings currency (USD, from note 2), from the issuing authority, dated 2026-09-11.**
- [x] **Value as a range — refused as a range, with the reason** (every construction negative).
- [x] **One bar — neither applies**, stated; windage count one.
- [x] **Prices dated; aggregator for live quotes only, flagged.**
- [x] **SBC resolves every year and is complete on the charge measure** (brief requirement): cash-flow add-back and
      equity-statement credit both shown; capitalised SBC included; cash-settled MANTL awards not double-counted;
      401(k) match in cash; ESPP inside the charge; 2020 tender-offer compensation noted; **[E3-70] grant table
      read by hand because SBC exceeds 50% of operating cash** ($422.1M gross grants vs $250.1M charge,
      FY2021-25).
- [x] **The wc_note reconciled to the filed statement** (45.9%; the bonus accrual) **and located in the 10-Qs**
      (−$15.7M Q1-2026, −$5.8M H1-2026).
- [x] **The cap_flag resolved** (two dates, neither number wrong) and **the deal_note opened** (a credit-agreement
      amendment for a buyback) — **and the 13D record read**, because the deal note cannot see it.
- [x] **The perimeter decided with its ground**: pro forma not buildable (no target statements filed; "pro forma"
      absent from the 10-K and both 10-Qs searched); windows published as filed with the bias direction stated.
- [x] **Corrections recorded here rather than by editing history (operator rule 6):**
  1. **A table cell corrected before the Q2 commit.** The first draft of the competitor row printed ALKT's latest
     owner-earnings margin as −10.3% "either way"; on the cash-flow SBC add-back it is **−9.5%** (−10.3% only on the
     screen's double-counted P&L charge). Corrected in the working file before `e9647bd`; the Q2 commit message
     carries the corrected −9.5%.
  2. **A competitor attribution softened before commit.** The draft described Candescent's ownership from general
     knowledge; replaced by what the evidence shows (no SEC ticker-map entry for any of the six private names).
  3. **A compound-growth figure corrected before the Q4 commit**: the draft said revenue compounded 43% a year
     FY2019-25; the arithmetic is **34.9%** ($73.5M → $443.6M over six years).
  5. **A count corrected in the fold (after commit `e9647bd`):** Q2 and the register said Q2 Holdings names *eleven*
     substitutes. The sentence names **ten companies, Alkami among them** — nine substitutes plus Q2 Holdings itself makes
     ten. Corrected in place; commit `e9647bd`'s message says "eleven" and stands as written, wrong by one.
  4. **Net debt is $264.0M** ($345.0M − $45.5M − $35.4M); Step 0 and Q4 were first written with $264.1 million, a rounding
     slip, corrected in the fold commit.
- [x] **Run committed to git with a pathspec** — after Step 0 (`b3bf596`), Q1/Q2 (`e9647bd`), Q3/Q4 (`bc9f7b8`),
      and the close and fold.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** **ALKT FAILS at Q2 — OUT on the business.** A legible per-user subscription business on ~70-month
  contracts, but its closest competitor's 10-K names it among ten digital-banking vendors and Alkami calls every win a
  competitive takeaway **[E3-03]**; its 10-K discloses past and expected price reductions **[E2-44, E4-37]**; it
  has earned no operating profit in seven filed years and is last in a five-filer row on every return measure
  **[E3-46]**; five years of growth took $525.7M of acquisitions and $246.0M of stock pay against −$23.0M of
  operating cash; and the moat must be continuously rebuilt, with a 2021 acquisition written off on the 2025 one
  **[E4-04]**. Recorded beneath the verdict: owner earnings negative on every window, both (c) ends, both SBC
  measures and the TTM (−$71.5M to −$16.4M); 86% of the operating-cash recovery is stock pay substituted for cash;
  an activist seeks a sale and no agreement exists. **Price $20.51 · cap $2,193.4M · COMPUTATION — NOT A
  CLEARANCE: yield −0.75% to −3.26%, −6.1 to −8.6 points under the 5.35% sovereign.**

