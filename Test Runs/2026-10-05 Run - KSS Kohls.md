# Company Run: Kohl's Corporation (NYSE: KSS), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch** (2026-10-05).

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`,
so the analyst does not know whether the operator holds KSS. No holding review was opened.

**CONTAMINATION, declared.** (1) Listing `Test Runs/` to check for an earlier KSS file showed the file names of other
companies' 2026-10-05 runs, holding reviews and research passes (ABG, ADNT, AHCO, AMR, AROC, ATKR, BN, BOOT, BRK.B, CAG,
CCB, CSW, CTS, DBD, DY, EFOR, EME, ENSG, ETN, EXTR; HRB, MBUU, SONY, TBTC, V, MITSY, NCLTY, QQQM); none was opened. No
file about KSS or Kohl's was found or opened. (2) The session context carried recent commit subjects: three v5 runs of
record (ADNT, MBC, AMR) closed OUT at Q2, with their prices and computed values, and a session-state commit naming an
S&P 600 screen. (3) The session's memory index says the operator's queue has "57 gate-clearers, nothing buyable". None
of this concerns Kohl's; it does tell the analyst that recent runs have mostly closed at Q2, which is a pull toward the
same close, and the Q2 verdict below was checked against the contrary evidence for that reason.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $19.48 (2026-10-05, live quote through `tools/run.py`; aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 113,376,445 common, one class (10-Q for the quarter ended
  2026-08-01, filed 2026-09-03, accession `0001193125-26-381893`; `python Screens/cover_shares.py KSS`). The balance
  sheet of 2026-01-31 shows 127 million issued and 15 million in treasury (10-K, `0001193125-26-115982`).
- **Market cap:** $19.48 × 113.376M = **$2,209M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025 (year to 2026-01-31), filed 2026-03-19, `0001193125-26-115982`: Items 1, 1A, 2, 3, 5, 7 in full; the
    balance sheet, income statement, equity statement and cash-flow statement; Notes 2 (debt) and 3 (leases).
  - 10-Q for the quarter ended 2026-08-01, filed 2026-09-03, `0001193125-26-381893`: statements, debt note, tariff
    refund note, MD&A.
  - Earlier 10-Ks for the fifteen-year record (selected data, MD&A headlines, store counts, free-cash-flow
    reconciliations): FY2010 `0001193125-11-071252`; FY2013 `0000885639-14-000007`; FY2016 `0000885639-17-000007`;
    FY2019 `0001564590-20-011512`; FY2021 `0000950170-22-004076`; FY2022 `0000950170-23-008444`; FY2023
    `0000950170-24-034691`; FY2024 `0000950170-25-042662`.
  - 8-Ks: 2025-01-10 `0001193125-25-004437` (27 store closures); 2025-05-01 `0001193125-25-109074` (CEO terminated for
    cause); 2025-11-24 `0001193125-25-292314` (Bender appointed CEO); 2026-08-26 `0001193125-26-365860` (Q2 results).
  - Proxy 2026, `0001104659-26-041769`: searched, not read in full (say-on-pay history only); the file closed before Q5.
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025 **$1,380M** in
  the consolidated statement of cash flows of `0001193125-26-115982` equals the XBRL figure `tools/run.py` printed. The
  run.py balance-sheet line for 2026-01-31 (equity $4,048M, cash $674M, inventory $2,745M, long-term debt $1,436M) also
  matches the filed balance sheet line by line.
- **`tools/run.py KSS` arithmetic lines only** (its rule and id lines ignored, Part VII):
  - OCF, SBC, D&A, capex FY2023-FY2025: 1,168/42/749/577; 648/30/743/466; 1,380/34/700/372 ($M). Three-year
    OCF−SBC−capex 558; OCF−SBC−D&A 299. Five-year (FY2021-FY2025) 544 and 345.
  - The tool's "OE capex" leaves out the finance-lease and financing-obligation payments. They are real rent on stores
    the company accounts for as finance leases ($83M, $79M, $93M in FY2025, FY2024, FY2023 per the filer's own
    adjusted free cash flow table, `0001193125-26-115982`), so this run uses the filer's free-cash-flow lines and
    deducts stock pay. Owner cash after every real cost, $M (FCF as filed = OCF + proceeds from financing obligations −
    capex − finance lease and financing obligation payments; then − SBC):

    | FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
    |---|---|---|---|---|---|---|---|---|---|---|
    | FCF as filed | 1,264 | 881 | 1,403 | 700 | 908 | 1,556 | (639) | 519 | 104 | 935 |
    | SBC | 41 | 55 | 87 | 56 | 40 | 48 | 30 | 42 | 30 | 34 |
    | **Owner cash** | **1,223** | **826** | **1,316** | **644** | **868** | **1,508** | **(669)** | **477** | **74** | **901** |
    | D&A variant (OCF−SBC−D&A) | 1,169 | 645 | 1,056 | 684 | 424 | 1,385 | (556) | 377 | (125) | 646 |

    Sources: FCF lines from the reconciliations in `0000885639-17-000007` (FY2016), `0001564590-20-011512` (FY2017-2019),
    `0000950170-23-008444` (FY2020-2022), `0001193125-26-115982` (FY2023-2025, "adjusted free cash flow"); SBC and D&A
    from the cash-flow statements (XBRL). **Five-year mean (FY2021-2025): $458M; D&A variant $345M. Ten-year mean
    (FY2016-2025): $717M; D&A variant $571M. Three-year mean: $484M; D&A variant $299M.**
  - Abnormal years in the five-year window: FY2021 (the post-lockdown year, gross margin about 38.0%, owner cash
    $1,508M) and FY2022 (the inventory glut, gross margin 33.2%, owner cash −$669M). FY2025 holds a one-time $129M cash
    legal settlement and a $203M inventory release (cash-flow statement, `0001193125-26-115982`).

### The balance sheets, ten year-ends, read before the income account (template Q4 instruction; the file closes before Q4)
"I like to look at balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.
`tools/run.py` table (first-filed XBRL), checked against the filed statements for 2026-01-31 and 2026-08-01:

| year-end | assets | equity | cash | inventory | lt debt | retained |
|---|---|---|---|---|---|---|
| 2017-01-28 | 13,574 | 5,177 | 1,074 | 3,795 | 2,795 | 12,522 |
| 2019-02-02 | 12,469 | 5,527 | 934 | 3,475 | 1,861 | 13,395 |
| 2021-01-30 | 15,337 | 5,196 | 2,271 | 2,590 | 2,451 | 13,468 |
| 2023-01-28 | 14,345 | 3,763 | 153 | 3,189 | 1,637 | 13,995 |
| 2025-02-01 | 13,559 | 3,802 | 134 | 2,945 | 1,174 | 1,008 |
| 2026-01-31 | 13,362 | 4,048 | 674 | 2,745 | 1,436 | 1,223 |
| 2026-08-01 (10-Q) | 13,410 | 4,168 | 821 | 2,913 | 1,325 | 1,332 |

What the figures say:
- **Retained earnings did not fall by losses.** The drop from $13,995M to $2,934M and then $1,008M is the retirement
  of treasury stock: $11,155M charged to retained earnings in FY2023 and $1,811M in FY2024 (statement of changes in
  equity, `0001193125-26-115982`). Treasury stock at cost stood at $13,715M at the start of FY2023. Repurchases in
  the cash-flow statements total about $10.8 billion FY2010-FY2022 (XBRL `PaymentsForRepurchaseOfCommonStock`, summed),
  against a market value today of $2.2 billion. Diluted shares fell from 307M (FY2008) to 114M (FY2025).
- **Equity fell** from $5,177M to $4,048M while total assets stayed near $13.4 billion. There is no goodwill line;
  there are no customer receivables (the card accounts belong to Capital One).
- **Inventory against sales:** inventory fell 28% (3,795 to 2,745) while net sales fell 21% (18,686 to 14,775), so
  inventory was cut faster than sales. This is the one balance-sheet line that moved the right way and stayed there.
- **Debt:** long-term debt halved (2,795 to 1,325), but its terms worsened: $360M of 10.000% senior secured notes due
  2030, secured through subsidiary guarantees on eleven distribution and e-commerce centres; the 2031 notes' coupon
  stepped up 175 basis points on downgrades; corporate ratings B2 (Moody's), B+ (S&P, negative outlook) at 2026-01-31;
  the notes' fair value $1.2 billion against $1,342M principal at 2026-08-01 (10-Q, `0001193125-26-381893`).
- **Leases are the larger debt.** From FY2019 (ASC 842) the balance sheet carries the leases: $4,739M of lease
  liabilities at 2026-01-31 (operating $2,744M, finance $1,995M), plus financing obligations; future lease payments
  $8,269M including renewal options "reasonably certain" to be exercised (Note 3). About $450M a year is due under
  them in each of 2026-2030. Debt plus lease liabilities, about $6.1 billion, is nearly three times the market value.
- **Cash** swung from $2,271M (2021) to $134M (2025) and back to $821M (2026-08-01, of which $682M short-term
  investments).
What they cannot say: the market value of the 402 owned stores, the distribution centres and the headquarters. No fair
value of the owned real estate was found in the filings read.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether one would be "happy buying this stock if the market closed for five
years" **[M1997-109]**, which for Kohl's turns entirely on what the stores will earn, since the quotation "just tells us
prices" **[M2006-077]**. The margin of safety bears hardest: the arithmetic below needs a calculator to say whether the
price clears, and "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**.
No macro view enters, "macro conclusions are — just never enter into the discussion" **[M2000-094]**; tariffs and consumer credit appear below only as properties of the business. The
analyst's habit governs the method: "looking for what’s wrong in things" **[M2025-013]**, and the anchor to avoid is
"always your previous conclusion" **[M2016-054]**, here the run of Q2 closes the contamination note names.
**Contrary evidence, written down as found** "in the first 30 minutes" **[M1997-127]**:
1. The price is about 4.8 times five-year owner cash ($2,209M against $458M), a 21% owner-cash yield, and below every
   computed case but the worst. A cheap price for a shrinking business is the newspaper exception the framework
   carries: papers bought "at a very low multiple of current earnings" **[L2012-010]**, "because the earnings will go
   down" **[M2013-026]**.
2. Dillard's, a department store, has earned 10.6% to 16.4% pretax on revenue every year FY2021-FY2025 (table at Q2):
   the format can earn well.
3. Kohl's itself earned 9.9% pretax in FY2011, at TJX's level of that year; the castle once stood.
4. The decline slowed: comparable sales −1.0% in the first half of FY2026 after −6.5% and −3.1%; digital sales +3.4%;
   inventory managed down faster than sales; debt cut by half since 2017; cash $821M.
5. The owned real estate (402 stores, most distribution centres, the headquarters) has a value the accounts do not show.
6. The credit-card revenue share with Capital One is a stream a pure retailer would not have.
Each is answered at Q2 or in the computation, not dismissed.

## THE STANDING RULE
Buying the shares outright, unleveraged, in a size the buyer can lose entirely, does not break "never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**; bought on margin it would breach the rule outright: "borrowed money has no place in the investor's tool
kit" **[L2014-005]**. The target's own debt and leases are Q9's question (NOT REACHED). No breach on an unleveraged,
sized purchase.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, about "the economic dynamics of the industry. Is there — are there
  competitive moats? Is there ease of entry?" **[M2011-014]**.
- **The key variables** "and evaluating how predictable they were" **[M1998-044]**: (1) store traffic, read in
  comparable sales and transactions (transactions −4% in FY2025, 10-K MD&A); (2) merchandise gross margin; (3) the
  credit-card revenue share (other revenue $752M in FY2025, more than the year's pretax income of $336M); (4) fixed
  occupancy, about $450M a year of lease payments plus owned-store costs; (5) the competitors' prices, which the filer
  says decide the sale: "consumers can quickly and conveniently comparison shop with digital tools, which can lead to
  decisions based solely on price" (Item 1A, `0001193125-26-115982`).
- **Can the past statements tell me the future ones**, whether "the financial statements will tell me the information that’s useful" **[M2008-033]**? The direction, yes: fifteen years of filings show
  one slow trend, sales per selling square foot and margin falling while off-price rivals grow (Q2). The level, no:
  whether the decline stops at −1% or runs at −5% is not foreseeable from the filings.
- **Contrary evidence on Q1 itself, written down.** The rows warn about this exact field: "it’s easy to sort of think
  you understand retail, and then subsequently find out you don’t, as we did with the department store in Baltimore"
  **[M2014-052]**; and of "many retailing businesses I can think of", "I’m not sure I’d know where we would stand in the
  competitive pecking order five or 10 years from now" **[M1996-062]**. And "if you have doubts about something being
  into your circle of competence, it isn’t" **[M2002-092]**.
- **The routing.** Q1 closes TOO HARD a business whose ten-year economics cannot be foreseen "because its industry
  changes fast" (framework, Q1, The routing, fixed). The department-store change is slow and has run one way for fifteen
  years; the analyst cannot name the level of Kohl's earnings in ten years, but can say with reasonable confidence where
  its competitive position will stand: below the low-cost operators, as it stands now and has stood for a decade. That
  is the "notion of how the industry will develop and where the company will stand within the industry"
  **[M2012-065]** that Q1 asks for. The doubt the retail rows raise is a doubt about the castle's future, which Q2 owns.
- **VERDICT: IN**, narrowly, with the M2014-052 and M1996-062 doubt carried forward to Q2 and recorded in the closing
  section. *(An analyst who reads that doubt as a doubt about the circle would close here TOO HARD (NATURE) under "if you have doubts about
  something being into your circle of competence, it isn’t" **[M2002-092]**; the box would still not be IN.)*

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**.

**The record, fifteen years, from the filer's own filings** (comparable sales and gross margin as the filer printed
them; store counts at year-end; FY2020 and FY2021 comparable sales not found in the filings read):

| FY | net sales $M | comp sales | gross margin | stores | source |
|---|---|---|---|---|---|
| 2008 | 16,389 | −6.9% | 36.9% | 1,004 | `0001193125-11-071252` |
| 2010 | 18,391 | +4.4% | 38.2% | 1,089 | `0001193125-11-071252` |
| 2011 | 18,804 | +0.5% | 38.2% | 1,127 | `0000885639-14-000007` |
| 2012 | 19,279 | +0.3% | 36.3% | 1,146 | `0000885639-14-000007` |
| 2013 | 19,031 | −1.2% | 36.5% | 1,158 | `0000885639-14-000007` |
| 2014 | 19,023 | −0.3% | 36.4% | 1,162 | `0000885639-17-000007` |
| 2015 | 19,162 | +0.7% | 36.0% | 1,164 | `0001564590-20-011512` |
| 2016 | 18,636 | −2.4% | 35.9% | 1,154 | `0001564590-20-011512` |
| 2017 | 19,036 (53 wks) | +1.5% | 36.0% | 1,158 | `0001564590-20-011512` |
| 2018 | 19,167 | +1.7% | 36.4% | 1,159 | `0001564590-20-011512` |
| 2019 | 18,885 | −1.3% | 35.7% | 1,159 | `0001564590-20-011512` |
| 2020 | 15,031 | not found | ~31.0% | not read | `0000950170-23-008444` |
| 2021 | 18,471 | not found | ~38.0% | 1,165 | `0000950170-22-004076` |
| 2022 | 17,161 | −6.6% | 33.2% | 1,170 | `0000950170-23-008444` |
| 2023 | 16,586 (53 wks) | −4.7% | 36.7% | 1,174 | `0000950170-24-034691` |
| 2024 | 15,385 | −6.5% | 37.2% | 1,175 | `0000950170-25-042662` |
| 2025 | 14,775 | −3.1% | 37.5% | 1,153 | `0001193125-26-115982` |
| H1 2026 | 6,316 | −1.0% | 41.5% (tariff refunds) | 1,151 | `0001193125-26-381893` |

Sales per selling square foot: $229 in FY2010 ($18,391M over 80.1M sq ft, computed from the FY2010 filing), $229 in
FY2019 (as printed), about $182 in FY2025 ($14,775M over 81M sq ft, computed). FY2020 and FY2021 net sales are from the FY2022
income statement; their gross margins are derived from the basis-point changes the FY2021 and FY2022 10-Ks state (+700
and −485 basis points), so they are marked approximate.

**The castle tests, each with its filing fact.**
1. **What keeps it standing**, "What are the key factors? And how permanent are they?" **[M1995-038]** The filer names its own competitive factors:
   "Management considers product and value to be the most significant competitive factors" and its competitors are
   "online retailers, off-price retailers, warehouse clubs, mass merchandisers, specialty stores, traditional department
   stores" (Item 1, `0001193125-26-115982`). It names no advantage those competitors lack. The FY2025 operating income of
   $624M is smaller than the other-revenue line ($752M, chiefly the card revenue share) plus the $129M legal gain: before
   the other-revenue line, the stores' operating result was about −$257M in FY2025, against about +$10M in FY2019 and
   +$188M in FY2016 (operating income less other revenue, computed from the filed statements; approximate, since some
   card expenses sit in SG&A). What keeps the castle standing today is a share of interest and late fees on a card
   portfolio Capital One owns, which the filer says is exposed to "potential federal limits on credit card interest
   rates" and to "lower sales to our Kohl's credit card customer" (Item 1A and MD&A, same 10-K).
2. **Would it stand without the lord?** "In retailing, to coast is to fail" **[L1995-008]**; "you cannot coast in
   retailing" **[M1995-040]**. Kohl's has had three chief executives since December 2022 (Kingsbury, interim from
   December 2022 and CEO from February 2023, FY2022 10-K; Buchanan, from January 2025 to his termination for cause on
   2025-04-30; Bender, interim from May 2025 and permanent from November 2025: 8-Ks `0001193125-25-109074`,
   `0001193125-25-292314`). The business has needed a lord and has
   not kept one.
3. **The money test**: "if I had a hundred million dollars and I wanted to go in and take on See’s
   Candy, could I do it?" **[M2011-015]** The attack on Kohl's is not hypothetical; it has been made and is winning. TJX describes its
   offer as "prices below regular prices for comparable merchandise at full-price retailers, including department,
   specialty, and major online retailers" (TJX 10-K FY2025, `0000109198-26-000008`); Ross says "There are limited
   economic barriers for others to enter the off-price retail sector" (Ross 10-K FY2025, `0000745732-26-000006`). "If
   the answer had been yes, we wouldn’t have done it" **[M2011-015]**.
4. **Pricing power.** The stated strategy is to "reestablish Kohl’s as a leader in value and quality" (10-K MD&A), and
   part of the 2026 tariff refunds was "invested to deliver greater value to our customers" (10-Q tariff note): the
   gains go to the customer, not the owner. "you can almost measure the strength of a business over time by the agony
   they go through in determining whether a price increase can be sustained" **[M2005-020]**.
5. **Unit volume.** Transactions fell about 4% in FY2025 and 2% in the first half of FY2026 (10-K and 10-Q MD&A);
   cumulative reported comparable sales FY2011-FY2025 sum to about −21%, matching net sales of $18.8 billion falling to
   $14.8 billion.
6. **The low-cost position.** Kohl's is the high-cost operator against the off-price chains: "commodity businesses have
   risk unless you’re the low-cost producer, because the low-cost producer can put you out of business" **[M1997-010]**;
   "In an unregulated commodity business, a company must lower its costs to competitive levels or face extinction"
   **[L1994-035]**; "the guy with the lower cost comes in and kills you" **[M2001-013]**.
7. **The brand in the customer's mind.** The one line that grew in FY2025, Accessories "including Sephora" (+2.0%),
   rests on another company's brand, and "The parties share equally in the operating profit of the arrangement" (10-K,
   Sephora arrangement). The proprietary brands sell at "lower selling prices" than national brands. "the value of having
   the brand moves over to the retailer from the product itself" **[M2001-090]** is the case where the retailer is the
   trusted name; here the traffic-drawing name belongs to the supplier, who takes half the profit.
8. **Would the customer still choose it over the low bid?** The filer's own words are that comparison shopping "can lead
   to decisions based solely on price" (Item 1A). That is the case of "people buying candy for the low bid" **[M2017-009]**, and "most insureds don't care from
   whom they buy" **[L2004-003]** is the same failing answer in another trade.
9. **Ask the competitors.** Read from their filings: TJX names "department" stores as the full-price retailers it
   undersells; Ross says "We compete for customers [...] with other off-price retailers, traditional department stores" (its 10-K). No competitor filing read
   names Kohl's as a threat. Interviews were not possible (Part VII step 3 would be needed; not opened, see the box).
10. **Widening or narrowing**, "whether it’s likely to widen further or shrink on you" **[M1999-108]**: narrowing on every measure the filings give (the table above; the
    competitor row below). "Every day, in countless ways, the competitive position of each of our businesses grows
    either weaker or stronger" **[L2005-010]**.
11. **What could destroy it**, "say five, 10, 15 years from now — that will destroy, or modify, or reduce the economic strengths" **[M2000-014]**: further share loss to off-price and online,
    a cap on card interest rates, tariff costs it cannot pass on, and the lease and debt load meeting a further fall in
    sales.

**The competitor row, same metric from the competitors' own filings** (pretax income from continuing operations over
revenue; XBRL company facts, transcription; latest 10-K accessions TJX `0000109198-26-000008`, ROST
`0000745732-26-000006`, M `0001628280-26-021721`, DDS `0000028917-26-000006`; J. C. Penney last 10-K
`0001166126-20-000022`; Kohl's revenue is net sales to FY2015 and total revenue from FY2016, as tagged):

| FY | KSS rev / pretax % | TJX | ROST | Macy's | Dillard's | J. C. Penney |
|---|---|---|---|---|---|---|
| 2008 | 16,389 / 8.7% | 19,000 / 7.6% | 6,486 / 7.6% | 24,892 / −19.8% | 6,988 / −5.4% | 18,486 / 4.9% |
| 2011 | 18,804 / 9.9% | 23,191 / 10.4% | 8,608 / 12.2% | 26,405 / 7.5% | 6,400 / 6.2% | 17,260 / −1.3% |
| 2014 | 19,023 / 7.1% | 29,078 / 12.2% | 11,042 / 13.5% | 28,105 / 8.5% | 6,780 / 7.5% | 12,257 / −6.1% |
| 2016 | 19,681 / 4.4% | 33,184 / 11.2% | 12,867 / 13.9% | 25,908 / 3.7% | 6,418 / 4.0% | 12,918 / 0.0% |
| 2019 | 19,974 / 4.5% | 41,717 / 10.6% | 16,039 / 13.5% | 24,560 / 3.0% | 6,343 / 2.1% | 11,167 / −2.4% |
| 2021 | 19,433 / 6.3% | 48,550 / 9.1% | 18,916 / 11.9% | 25,399 / 7.3% | 6,624 / 16.4% | Chapter 11, 2020-05-15 |
| 2023 | 17,476 / 2.1% | 54,217 / 11.0% | 20,377 / 12.1% | 23,866 / 0.5% | 6,874 / 13.3% | |
| 2025 | 15,527 / 2.2% | 60,372 / 12.1% | 22,751 / 12.5% | 22,621 / 3.8% | 6,563 / 10.6% | |

Over the whole span FY2011-FY2025: Kohl's net sales −21% ($18,804M to $14,775M) and pretax margin 9.9% to 2.2% (1.3%
without the legal gain); TJX revenue +160% at 9% to 12%; Ross +164% at 12% to 14%; Macy's −14% at 7.5% to 3.8%; J. C. Penney from 4.9% (FY2008)
to losses or break-even every year FY2011-FY2019 and a Chapter 11 petition on 2020-05-15 (J. C. Penney 8-K, `0001193125-20-144411`).
TJX's comparable sales rose 5% in its FY2025 and Ross's 5% (their 10-Ks above). The comparison is made over the span,
not one year.

**The contrary evidence, answered.**
- *Dillard's earns 10% to 16%.* It did so from FY2021 on, after 2.1% to 7.5% in FY2011-FY2019, on flat-to-falling
  revenue ($6,988M FY2008 to $6,563M FY2025). The format can earn in a given stretch; Dillard's revenue shows no gain of
  share either. It does not show Kohl's castle standing: Kohl's margin fell in the same five years.
- *The newspaper exception.* The papers were bought where Buffett expected "modest
  erosion" **[L2012-010]**. Kohl's erosion is not modest (pretax margin from 9.9% to about 1.3% before the one-time gain;
  the stores' operating result before the card income negative), and the exception carries no lease load like Kohl's
  $8.3 billion of future lease payments. The framework keeps the exception as a tension marked [SPEAKER] (VI, Q2) and
  the STOP as the rule.
- *The 2026 stabilisation.* Comparable sales −1.0% in the half, but the half's margin gain "was driven by tariff
  refunds" (10-Q), about $100M recognised in gross margin, a one-time item. One half-year does not reverse fifteen
  years; L1995-022 sorts a bad year as "a cyclical problem, not a secular one" only where "we at least maintained, and in
  some instances widened, our competitive superiority" **[L1995-022]**, and the competitor row shows the opposite.
- *Kohl's earned 9.9% in FY2011.* It did; it stood at 4.4% in FY2016, 6.3% in the FY2021 rebound and 2.2% in FY2025; "Leadership alone provides no
  certainties" **[L1996-031]**; "most big businesses — eventually fall into mediocrity or worse" **[M2008-031]**.
- *The real estate and the card income* are assets and a revenue stream; neither is a moat around the retail business,
  and Q2 asks about the business.

**The rows on this very field.** The speakers' own department store: "we were wrong on the economics of the business"
**[M1998-176]**; "if we’d kept it, we would have gone out of business" **[M2016-031]**; "you could apply all kinds of
energy to them. And it didn’t do any good" **[M1997-105]**; the department stores "lost all three of those advantages"
**[M1999-015]**; "the internet, in many forms of retailing, is likely to pose such a threat that we simply wouldn’t want
to get into the business" **[M1999-013]**; "I think it’s terrible for most retailers" **[M2012-047]**; and the figures
that please from a growing utility, "if the numbers you recited came from a declining department store, we would just
hate it" **[M2014-088]**.

**Why OUT and not TOO HARD.** The TOO HARD row is the tenuous moat that cannot be valued: "it’s just too risky. We don’t
know how to valuate that" **[M2000-019]**. The OUT row is the attacker who could win: "If the answer had been yes, we
wouldn’t have done it" **[M2011-015]**. The evidence here is not a forecast: it is fifteen years of the
filer's and its competitors' own figures, all pointing the same way, and the filer's own statement that the customer
decides on price. The rows' failing answers fit by name: "the low-cost producer can put you out of business" **[M1997-010]**; "must lower its costs to competitive levels or face
extinction" **[L1994-035]**; "you do not want to have something whose competitive position is going to
erode over time" **[M2007-117]**. And price does not reopen it: "What you can’t do is turn any investment into a good deal
by paying little" **[M2019-015]**; "If you really think a business is declining, most of the time you should avoid it"
**[M2012-062]**; marginal businesses bought cheap "are the wrong foundation on which to build a large and enduring
enterprise" **[L2014-009]**.

- **VERDICT: OUT.** The castle is shown open on the evidence: the low-cost off-price operators have taken the field
  Kohl's sells in, the filer says its customer chooses on price, and its stores earn nothing before the card income.
  The rows' boxes are "in, out, and too hard" **[M2006-013]**; this is the second.

---
## COMPUTATION — NOT A CLEARANCE
*Written at the owner's request after the closing STOP. No entry language; nothing here reopens Q2:
"What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.* Value is "the discounted value of the cash that can be taken out of a business during its remaining
life" **[R1996-018]**, at "the yield on long-term U.S. bonds" **[L2000-021]**: 5.63%.

**(a) VALUE RANGE, the Q7 CONVENTION** (five-year average of owner cash after every real cost, carried ten years at the
growth shown on aggregate owner cash, then zero nominal growth, at the sovereign; ends = no-growth and shown-growth).
- Five-year owner cash $458M. Growth shown on the aggregate, FY2021 to FY2025 endpoints: **−12.1% a year** (the linear
  trend over the same five years: −10.3% of the mean a year). The endpoints are both abnormal (FY2021 high, and FY2025
  holding the $129M settlement), which "will be distorted" **[L2005-003]**; both measures are shown and the endpoint
  figure, the convention's, is used.
- **Range: $28.28 (shown growth, −12.1%) to $71.78 (no growth) a share, against $19.48.** Width 2.5 to 1, under the
  three-to-one line. The no-growth end assumes the fifteen-year decline stops today; nothing in the record supports it.
  The convention's flat terminal after year ten is likewise generous to a business that has shrunk for fifteen years.
- **D&A variant** (OCF − SBC − D&A, $345M): $21.31 to $54.11. Capex has run below D&A for a decade ($372M against $700M
  in FY2025; ten-year means about $605M against $852M), and depreciation is "almost always true costs" **[L2015-004]**,
  so the capex basis may overstate what the stores can pay out while still standing still; the filer's capex guidance
  for FY2026 is $350M to $400M.
- **Whole-cycle variant** (the five-year window holds two abnormal years): ten-year owner cash $717M with the ten-year
  endpoint growth −3.3% a year: **$86.58 to $112.30**. This variant overstates: its base averages a business that was about
  28% larger in revenue, with two to three times FY2025's pretax income, in FY2016-FY2019, and the decline is secular, not cyclical (Q2), so averaging over it
  carries the old earning power into the new.
- **A further case, shown for honesty:** the shown decline continuing for ever (capex basis, −12.1%, at the sovereign)
  is worth $20.04 a share, about the price. The market price is consistent with the record continuing.

**(b) FAIR PRICE** (the price at or below which the central case clears the ~10% pre-tax floor, the Q7 CONVENTION, from
"we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**). *CONVENTION of this run:* the central case is the shown-growth case, because the record shows decline
and the no-growth case would need a turn the filings do not show. *Tax treatment, CONVENTION of this run:* owner cash
is after cash income taxes; it is grossed up at the 21% federal statutory rate to a pre-tax figure (FY2025 effective rate
19.0%, 10-K) and discounted at 10%. Central case: $458M ÷ 0.79 = $580M pre-tax, −12.1% a year for ten years, then flat,
at 10%: **$2,678M, $23.62 a share.** On the D&A variant: $17.80. At no growth: $51.16. The price, $19.48, lies between
$17.80 and $23.62.

**(c) CHEAP PRICE** (below which no pencil is needed). *CONVENTION of this run:* the cheap price is the value of the
worst case the record supports, the D&A variant with the shown decline continuing for ever, at the long government rate
("what the worst case is" **[M2019-023]**): $345M × 0.879 ÷ (0.0563 + 0.121) = $1,712M, **$15.10 a share**. Below it
every case computed here is covered. The price is above it, so even on the arithmetic this needs a pencil: "If you
need to use a computer or a calculator to make the calculation, you shouldn’t buy it" **[M2009-005]**.

**Against the price:** $19.48 sits below the convention range ($28.28 to $71.78), above the cheap price ($15.10), and
below the central fair price ($23.62) but above its D&A twin ($17.80). None of it is a clearance: the file closed at Q2.

---
## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. *(The balance sheets were read in Step 0; the recast owner cash
is in Step 0 and the computation. Facts noted for a later reader, not judged: adjusted non-GAAP earnings are featured in
every results summary read; the FY2025 adjustments run both ways, removing the $129M gain as well as the charges.)*
## Q5: WHO RUNS IT. NOT REACHED. *(Facts noted, not judged: a chief executive terminated for cause on 2025-04-30 after an
Audit Committee investigation found undisclosed dealings with a vendor "founded by an individual with whom Mr. Buchanan
has a personal relationship" (8-K `0001193125-25-109074`); say-on-pay support of about 55% at the 2025 meeting (proxy
`0001104659-26-041769`); dissident proxy materials filed in April and May 2022 (DFAN14A filings by an outside filer agent,
e.g. `0000921895-22-001578`), not read.)*
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED. *(Facts noted: about $10.8 billion of repurchases
FY2010-FY2022; dividend cut from $0.50 to $0.125 a quarter in 2025 (paid $222M in FY2024, $56M in FY2025); a $100M
repurchase planned for 2026 under the $3.0 billion authorisation (10-Q).)*
## Q7: WHAT IS IT WORTH. NOT REACHED (see the computation above, not a clearance).
## Q8: BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9: COULD IT RUIN US. NOT REACHED. *(Facts noted for a later reader: B2/B+ ratings; $360M of 10% secured notes due
2030; $4.7 billion of lease liabilities; ABL revolver of $1.5 billion extended to 2031-06-30, undrawn at 2026-08-01.)*
## Q10: THE FAT PITCH. NOT REACHED.
## Q12 (optional): NOT ASKED.

---
## THE BOX
**OUT at Q2.** Kohl's castle is shown open on fifteen years of its own and its competitors' filings: sales down 21% from
FY2011 and pretax margin from 9.9% to about 1.3% before a one-time gain, while TJX and Ross grew revenue about 160% at
12% margins. The filer says its customers can decide "based solely on price", and the stores lose money before the
Capital One card revenue. The computation, not a clearance: convention range $28.28 to $71.78 (whole-cycle variant
$86.58 to $112.30, overstated), fair $23.62 (central, 10% pre-tax), cheap $15.10, against **$19.48**. No research pass
is opened: OUT is not TOO HARD (WORK).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **not
      done.** The operator's instruction for this run forbids commits; the file was written in one pass after the
      research and is the only output.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      found in that row); every filing fact has its accession; no number without a filing or a CONVENTION label.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; Q3 to Q10 not reached; the arithmetic after Q2 is headed
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost (finance-lease and financing-obligation payments and stock pay deducted), never
      a net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as found, "write it down in the first 30 minutes" **[M1997-127]** (six items in the foundations, each answered at Q2 or
      in the computation).
- [x] Not a point-in-time run; no row dated after the anchor arises.
- [x] Only the arithmetic lines of `tools/run.py` were used; its rule and id lines were ignored; its owner-earnings
      lines were replaced by the filer's free-cash-flow lines because the tool omits finance-lease payments.
- [x] `python tools/check_framework.py` PASS before finishing (no commit made, by instruction).
- Not done: interviews with customers, competitors or employees; the proxy and the 2022 contest read in full; a fair
  value for the owned real estate (none found in the filings read); FY2020 and FY2021 comparable sales (not found in the
  lines read).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1 and Q2 compete for the slow-decline retailer.** The retail rows ("it’s easy to sort of think you understand retail" **[M2014-052]**; "I’m not sure I’d know where we would
   stand in the competitive pecking order" **[M1996-062]**) read as doubts about the circle, and the doubt rule, "if you have doubts
   about something being into your circle of competence, it isn’t" **[M2002-092]**, would close the file at Q1 TOO HARD (NATURE). The routing
   rule sends only fast change to Q1. A department store in slow, one-way decline fits neither cleanly: the analyst can
   foresee the direction but not the level. This run read the doubt as a doubt about the castle and closed at Q2 OUT on
   the evidence; a second analyst could close Q1 TOO HARD. Both deny IN, but they differ on whether a lower price could
   ever matter (the newspaper exception). A sentence in Q1 saying whether "direction foreseeable, level not" passes Q1
   would settle it.
2. **The newspaper exception has no test.** Q2 says "Price does not reopen it" and also carries papers bought "at a very
   low multiple of current earnings" **[L2012-010]** as a tension marked [SPEAKER]. Nothing says what separates a
   newspaper-type decline (modest, unlevered, a local franchise) from a Kohl's-type decline. This run drew the line at
   the rate of erosion and the lease load; that line is the analyst's, not the framework's.
3. **The Q7 convention is generous to a declining business.** "No real growth" after year ten stops any decline at year
   ten, and the no-growth end of the range assumes the decline stops today. For a business with fifteen years of
   decline, the no-growth end is not a case the record supports, yet the convention makes it the top of the range and so
   decides the width test. Here the range passed the three-to-one test only because the shown decline is steep.
4. **The "shown growth" endpoints.** The convention measures growth on aggregate owner cash between the five-year
   endpoints. Here both endpoints were abnormal (FY2021's boom; FY2025's settlement), which the row warns against, "If either year was aberrational, any calculation of growth will be distorted" **[L2005-003]**;
   the convention gives no fallback. The run showed a linear trend beside it.
5. **Finance leases and `tools/run.py`.** The tool's owner earnings omit finance-lease and financing-obligation payments
   for a retailer whose stores are partly on finance leases; it prints them only as an "alternate". The Q4 rule "after
   every real cost" makes them a deduction; the tool should say so, or the run must catch it each time.
6. **The template's write-early line** cannot be ticked in a run whose instructions forbid commits; the self-audit says
   so rather than tick it.
7. **Em dashes.** This run's instructions forbid em dashes; operator rule 3 prescribes the heading "COMPUTATION — NOT A
   CLEARANCE" with one, and PRIME RULE 1 keeps the transcripts' own dashes inside quotations. The run keeps both and uses
   no em dash in its own prose or headings (the template's headings were rewritten with colons).
