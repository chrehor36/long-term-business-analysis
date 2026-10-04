# Company Run — The Coca-Cola Company (KO) — 2026-09-19
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
## STEP 0: THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

Run unattended on 2026-09-19 (from about 09:30 local); the template was copied and committed before any fetch
(`b3407b8`). **KO is not held, so this is a purchase question under v4, not a holding review.** WAVE 6: one of five
ordinary businesses the 2026-09-01 triage dropped with no recorded exclusion, recovered from the operator's screenshots
on 2026-09-19. **There is no KO row in `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`**, so there is no screen
label to test. Research, scripts and downloaded filings are in `Test Runs/_research 2026-09-19 KO/` (fetch scripts copied
from the HBB folder with the CIK changed). Every figure below is from Coca-Cola's own filings, fetched by this run, with
the accession.

**The analyst's own incentive, stated first [E4-27, E4-26, E3-41].** Coca-Cola is the corpus's most-cited operating
business, and a reader steeped in the corpus has an incentive to clear it. The famous past is not evidence about the
present: every gate below is decided on the 2020s filings, and the disconfirming evidence is hunted hardest where the
favourite hypothesis (a wide franchise) lives, at Q2 and Q4.

### The entity
CIK 0000021344, `submissions.json` (fetched by this run): *"COCA COLA CO"*, SIC 2080 Beverages, state of incorporation DE,
fiscal year end 1231, ticker KO on NYSE, no former names; 3,301 filings listed (`filings_list.txt`). One class of common
stock, $0.25 par, plus twenty listed euro note issues on the cover.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by this
  run at 09:34 local on 2026-09-19 (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned **(5.34, '09/18/2026', 'US Treasury daily par yield curve')** in the same minute
  (`step0_out.txt`): current, not stale. FRED not used. Struck by this run, not inherited.
- **Earnings currency: a judgment, stated.** Coca-Cola earns in many currencies: *"In 2025, we derived $28.8 billion of net
  operating revenues from operations outside the United States"* (FY2025 10-K Item 1A), 60% of $47.9bn, and 84% of unit
  cases are sold outside the US. It reports, borrows chiefly, pays dividends and is quoted in USD, and the owner's claim is
  a dollar claim; **the USD long bond is used, as the COKE and PEP runs did.** The currency drag is not assumed away: it is
  in the revenue bridge every year (currency -4, -5 and -2 points of revenue growth in 2023-25) and is carried at Q2 and Q4.
  No ADR, no FX conversion of the quote.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$88.25, the close of 2026-09-18** (Friday). Yahoo Finance chart via `sources._chart("KO", rng="1mo", max_age_h=0)`
  (aggregator, permitted for live quotes only, **flagged**): `regularMarketPrice` 88.25, `regularMarketTime` 1789761603 =
  16:00:03 EDT, exchange NYQ; the day's bar $87.52-$88.29 on 28.0M shares. `tools/sources.price("KO")` returned the same
  88.25 stamped 2026-09-18.
- **The two years, recorded rather than choosing a day** (`price2y_out.txt`): monthly mean closes $71.48 (2024-09), $62.77
  (2024-12), **two-year low $60.81 on 2025-01-06**, $69.67 (2025-08), $70.30 (2025-12), $78.94 (2026-02, the month of the FY2025
  results), $80.46 (2026-06), **two-year high $91.99 on 2026-08-24**, $88.26 (2026-09 to date). **The price has risen about 26%
  in twelve months** (from $69.67 in August 2025).
- **Primary-filing cross-check:** the Q2 2026 10-Q, Part II Item 2, gives the company's own average repurchase price:
  *"April 4, 2026 through May 1, 2026 | 1,093,205 | $ | 76.63"*, *"May 2, 2026 through May 29, 2026 | 528,481 | 79.95"*,
  *"May 30, 2026 through July 3, 2026 | 772,808 | 80.23"*. Yahoo's monthly mean closes for April, May and June 2026: **$76.50,
  $80.02, $80.46**. The aggregator's series is corroborated in three periods by the issuer's own purchases.
- **Split factor after the count's date: 1.0** (`sources.split_factor_after`). `close` used, never `adjclose`.

### The share count: from the cover, with the accession
- **4,302,549,243 shares**, from the cover of the **Form 10-Q for the quarter ended 2026-07-03, filed 2026-07-29, accession
  `0001628280-26-050503`**, the latest periodic filing: *"Class of Common Stock | Shares Outstanding as of July 27, 2026 |
  $0.25 Par Value | 4,302,549,243"*. `python Screens/cover_shares.py KO` returned the same filing, accession and count
  (*"single class / undimensioned 4,302,549,243"*).
- **Cross-check against the filed balance sheet (rule 4):** the same 10-Q: *"issued — 7,040 shares"* and *"Treasury stock, at
  cost — 2,737 and 2,738 shares"* (millions), so **4,303M outstanding at 2026-07-03**; *"Average Shares Outstanding — Basic |
  4,303"* for the quarter. **Consistent.** One class; nothing to sum.
- **Tooling note:** `tools/run.py KO` printed *"share basis: dei cover-page count as of 2026-04-28"*, i.e. the Q1 10-Q cover,
  one filing behind (the count is almost unchanged, so immaterial here; recorded as the known companyfacts lag).

### THE PAIR
**US$88.25 x 4,302,549,243 x 1.0 = market cap US$379.7bn** (379,699,970,694). Beside it at 2026-07-03 (10-Q balance sheet):
cash, equivalents and short-term investments $13,529M plus marketable securities $2,842M; loans and notes payable $48M,
current maturities of long-term debt $6,494M, long-term debt $37,001M, so **net debt about $27.2bn** (enterprise value about
$407bn; recorded, not used as the yield denominator, which stays the equity cap as in every run in this queue). The
$6.0bn IRS deposit plus $514M of accrued interest sits in other noncurrent assets and is **not** counted as cash (below).

### The deal check (the ROKU lesson: a live merger makes the quote a spread)
`sources.deal_filings("0000021344")` returned **no** SC TO, SC 13E-3, DEFM14A or 425 (`step0_out.txt`, `([], [], '2026-02-20')`).
The 8-Ks since 2023 that are not earnings releases or annual-meeting results were read (`8K_*.txt`): note issues (2024, opened and read: $3.0bn of 5.000%/5.300%/5.400%
notes due 2034-64 on 2024-05-13, EUR1.0bn on 2024-05-14, $3.0bn of 4.650%/5.200%/5.400% notes due 2034-64 on 2024-08-14 and EUR1.0bn on
2024-08-15; the IRS deposit was paid 2024-09-10, carried to Q4); segment recasts (7.01 on 2025-03-27 and 8.01 on 2025-06-26, Global Ventures sunset); director elections
(Max Levchin, 2025-10-16) and officer changes; **the CEO succession** (8-K of 2025-12-10, and of 2026-02-20: *"Henrique Braun,
currently Executive Vice President and Chief Operating Officer ... will become Chief Executive Officer of the Company effective
as of March 31, 2026. In addition, James Quincey ... will continue as Executive Chairman"*); and **2026-07-16, Item 8.01: a
ransomware incident at fairlife** (*"identified unauthorized access by a third party to a portion of its systems, including its
production-related systems"*), carried to Q3 and Q4. **No offer for KO; the quote is not a spread.** The live transactions are
KO's own disposals, below.

### The perimeter: which years are comparable
Coca-Cola has been selling its company-owned bottlers for a decade, and the windows below straddle that. From the 10-Ks and the
Q2 2026 10-Q, Note 2:
- **Refranchised or sold, inside the FY2021-25 window:** Vietnam (2023, gain $439M), the Philippines (2024, gain $595M), bottlers in
  certain territories of India (2024, gain $303M; May 2025, *"net cash proceeds of $ 218 million"*), the finished-product
  operations in Nigeria (October 2025, charge $393M), **a 40% noncontrolling interest in the India bottler** (*"In July 2025, we
  sold a 40 % noncontrolling interest in our bottling operations in India to a local partner for approximately $ 1.3 billion"*,
  booked in financing, not investing); equity stakes sold: Thailand (2024), part of CCEP (March 2025, $741M), and **the whole
  stake in Coca-Cola Consolidated** (2025, gain $1,952M; the COKE fold records it as $2.4bn for 18.84M shares at $127 on
  2025-11-07).
- **Pending, the one live disposal:** *"In October 2025, the Company entered into a definitive agreement to sell a portion of our
  interest in our bottling operations in Africa to Coca-Cola HBC AG ... Closing is subject to various regulatory approvals and is
  expected by the end of 2026, upon which we will deconsolidate these bottling operations. We have also agreed to a separate option
  arrangement for CCHBC to acquire the Company's remaining 25% ownership interest within a six-year period"* (10-Q Note 2). Held for
  sale at 2026-07-03: assets $5,438M, liabilities $2,442M, after *"an impairment charge of $ 1,274 million, primarily due to the
  negative net foreign currency translation adjustments"* (partly reversed, $56M, in H1 2026).
- **Bought, inside or just before the window:** fairlife (the remaining 57.5%, January 2020, with milestone payments through 2025,
  below); BodyArmor (2021, *"Acquisitions of businesses ... (4,766)"* in the FY2021 cash-flow statement); Costa (2019, *"(5,542)"* in
  FY2019).
- **Honest windows.** Bottling Investments shrank every year (revenue *"Acquisitions & Divestitures"* -8, -28, -7 points of the
  segment in 2023-25), so consolidated revenue in FY2021 contains bottlers that FY2025 does not. The bottlers are the low-margin
  part (*"finished product operations generate higher net operating revenues but lower gross profit margins than concentrate
  operations"*, FY2025 10-K), so the perimeter shrinks revenue faster than cash: the effect on owner earnings is small and
  its direction is down (the sold bottlers' cash leaves the later years). **The five-year window FY2021-25 is used as the
  default, with the three-year FY2023-25 beside it; both carry a shrinking bottler perimeter, stated, not adjusted.**

### Two one-off cash items inside operating cash, found in the notes (the COKE lesson, reversed)
The COKE run found a perpetual royalty sitting in FINANCING, outside operating cash. At KO the defect runs the other way: **two
very large payments sit INSIDE operating cash** and depress the two latest years.
1. **The IRS deposit, 2024: $6.0bn.** FY2024 10-K MD&A: *"This decrease was primarily driven by the $6.0 billion IRS Tax Litigation
   Deposit"*. The 10-Q: the Tax Court *"entered a decision reflecting additional federal income tax of $ 2.7 billion for the 2007
   through 2009 tax years. With applicable interest, the total liability ... is $ 6.0 billion ... The Company paid those invoices
   ('IRS Tax Litigation Deposit') on September 10, 2024"*, recorded in other noncurrent assets, *"refunded in full or in part if the
   Company's tax positions are ultimately sustained on appeal"*. Appeal to the Eleventh Circuit filed 2024-10-22; **heard
   2026-06-25; no decision in the Q2 10-Q.** Reserve *"$ 529 million"* at 2026-07-03. Exposure for later years: *"the potential
   aggregate remaining incremental tax and interest liability for the tax years 2010 through 2025 could be approximately $ 14
   billion as of December 31, 2025"*, growing *"approximately $ 450 million and $ 900 million"* for the three and six months to
   2026-07-03, and continuing application *"would increase the Company's effective tax rate by approximately 3.8 %"*. Carried to Q4.
2. **The fairlife milestone, 2025: $6.1bn of $6.173bn in operating cash.** FY2025 10-K MD&A: *"the activity in 2025 included $6.1
   billion of the $6.2 billion final milestone payment for fairlife"*, and in financing *"$104 million of the $6.2 billion final
   milestone payment for fairlife"*. Earlier milestones: *"the first milestone payment of $ 100 million"* (2021) and *"a milestone
   payment of $ 275 million during 2023"* (*"$108 million of the $275 million"* in financing, so about $167M in operating cash). The
   remeasurement charges went through operating income: $51M (2020), $369M (2021), $1,000M (2022), $1,702M (2023), $3,109M (2024),
   $47M (2025). **Carried to Q3 (capital allocation) and Q4 (how each enters owner earnings, a disclosed judgment).**

Also found in the operating-cash notes and carried to Q4: **a trade receivables factoring programme** (*"The Company sold $14,710
million and $21,873 million of trade accounts receivables under this program during the years ended December 31, 2025 and 2024"*;
$17,704M in 2023; $7,011M in H1 2026; *"The cash received from the financial institutions is classified within the operating
activities section"*), named by the filer as a benefit to operating cash in 2024 and H1 2026; and **transfers of surplus non-US
pension assets** into company cash of *"$ 332 million and $ 523 million"* (2025, 2024).

### The filing was read (rule 4)
- [x] MD&A [x] cash-flow statement incl. detail lines [x] footnotes
- **Documents:** FY2025 10-K filed 2026-02-20 (`0001628280-26-010047`); Q2 2026 10-Q filed 2026-07-29 (`0001628280-26-050503`); Q1
  2026 10-Q filed 2026-04-30 (`0001628280-26-028802`); 10-Ks FY2020-24 (`0000021344-21-000008`, `-22-000009`, `-23-000011`,
  `-24-000009`, `-25-000011`); DEF 14A 2026 (`0001104659-26-028215`); the 8-Ks named above; earnings releases at Q3. Raw text in the
  research folder (`10K_FY*.txt`, `.flat.txt`).
- **Figure cross-checked against the filed statement:** FY2025 net cash from operating activities, *"Net Cash Provided by Operating
  Activities | 7,408 | 6,805 | 11,599"* (FY2025 10-K cash-flow face) against `tools/run.py`'s companyfacts reads of 7,408, 6,805 and
  11,599: **identical**. The cover count was cross-checked to the balance sheet above. **Auditor:** Ernst & Young LLP (PCAOB ID 42),
  FY2025 opinions on the statements and on internal control signed.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** Coca-Cola mostly does not make drinks. It makes a flavouring
  base and a set of brand names, and sells the base to about two hundred independent bottlers, each of which holds a territory
  and is obliged to buy *"its entire requirement of concentrates or syrups"* for the named brands from Atlanta (FY2025 10-K Item 1).
  The bottler adds water, sweetener, carbon dioxide and a can or bottle, trucks the drink to shops and restaurants, and keeps what
  is left. The price of the base is set mostly as a share of what the bottler sells the drink for (*"the concentrate price we charge
  is impacted by a number of factors, including, but not limited to, bottler pricing, the channels ... and package mix"*), so when
  the shelf price rises, Atlanta's take rises with it without Atlanta building a plant. Atlanta pays for the advertising
  ($5.4bn in 2025, per the advertising-costs note), keeps a gross margin of about 60% (58.1% to 61.6%, FY2021-25, from the
  income-statement faces), and earned an operating margin of 21-29% over those years. In FY2025, 59% of revenue and about
  85% of unit cases came from the base (MD&A, *"Concentrate operations | 59 %"*); the other 41% of revenue is finished drinks it
  still sells itself: the company-owned bottlers it has not yet sold (Bottling Investments: India, Africa and others), US fountain
  syrup, fairlife milk, BodyArmor, and the Costa coffee shops. It also owns minority stakes in the large bottlers (CCEP 18%, Monster
  21%, AC Bebidas 20%, Coca-Cola FEMSA 28%, CCHBC 22%, Coca-Cola Bottlers Japan 24%; FY2025 Note 6) that paid it $993M of dividends
  in 2025 on $2,031M of equity income.
- **The scarce input this business controls:** the **trademarks** (Coca-Cola alone is *"47% of our worldwide unit case volume"*) and
  **the bottler contracts that make the whole system buy the base only from Atlanta**, in 200+ countries, 33.8bn unit cases a year.
  Not a patent, not a plant, not a customer list. The contracts are not all perpetual (outside the US *"generally are of stated
  duration, subject in some cases to possible extensions or renewals"*; in the US ten-year CBAs *"renewable by the bottler
  indefinitely"*), and the incidence model gives the bottler a share of every price rise: **whether the trademark and the contracts
  are scarce enough is Q2's question.**
- **Will the fundamentals look broadly the same in ten years?** The model will: the concentrate-and-bottler structure has been
  the company's shape for over a century, and the direction of the last decade is toward more of it (bottlers refranchised every
  year of the window). The mix will move: *"Sparkling soft drinks represented 69% of our worldwide unit case volume"*, and sugar,
  weight-loss drugs, taxes and packaging rules press on that category (Item 1A); **that is a Q2 question about who keeps the price,
  and a Q4 question about volume, not a question about how the money is made.**
- **Kept outside the circle, and small enough not to decide Q1 [E4-46]:** the Costa coffee-shop estate (a retail business, bought
  in January 2019 *"in exchange for $ 4.9 billion of cash, net of cash acquired"*, FY2020 10-K Note 2; its record is read at Q3), the alcohol ventures
  (a *"firewalled subsidiary"* in the US), and the transfer-pricing tax law. None is needed to understand where the money comes from.
- **The case for UNKNOWABLE, recorded and not taken:** the consolidated statements are hard to read year to year, because every
  year carries a refranchising gain, an impairment, a fairlife remeasurement or a tax item, and the Tax Court exposure (about $14bn
  plus $6.0bn deposited) is an order of magnitude larger than any single year's charge. But each item is quantified in the notes and
  the core mechanism is plain. A business whose accounts are noisy but whose model is simple is understood [E3-31]; the noise belongs
  to Q3 (candor) and Q4 (owner earnings).
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
*The favourite hypothesis lives here, so the case against it is built first [E4-26, E4-51].*

### The case against, at full strength, in the filer's own words
1. **The shelf has substitutes, and the filer says so.** FY2025 10-K Item 1: *"Our competitive challenges include strong
   competitors in all geographic regions; in many countries, a concentrated retail sector with powerful buyers able to freely
   choose among Company products, products of competitive beverage suppliers and individual retailers' own store or
   private-label beverage brands; new industry entrants"*. Item 1A: *"Competitive pressures may cause the Company and our bottling
   partners to reduce prices we charge customers or may restrict our and our bottlers' ability to increase prices"*.
2. **Much of the "pricing" is inflation in weak currencies, and the dollar takes it back.** Price/mix was +10% (2023) and +11%
   (2024) consolidated, but the Latin America bullet each year reads *"favorable pricing initiatives, including inflationary
   pricing in Argentina"*, and currency cut consolidated **operating income** by **9% (2022), 8% (2023), 11% (2024) and 12% (2025)**
   (MD&A, each 10-K; +2% in 2021). A rise in pesos that the dollar erases is not [E2-44] pricing power.
3. **The US volume is flat.** North America unit cases: +2 (2022), -1 (2023), even (2024), -1 (2025) (10-K volume tables). The growth
   in cases is in India, China, Brazil and Africa.
4. **The category's risk is named by the filer**: *"the effects or perceived effects of the usage of weight-loss drugs on consumption
   patterns; potential new or increased taxes on sweetened beverages"* (Item 1A). Sparkling is *"69% of our worldwide unit case
   volume"*.
5. **The fastest-growing category was ceded, not won.** Monster's FY2025 10-K: the company acquired *"the various energy drink brands
   acquired from The Coca-Cola Company ('TCCC') in 2015"*, and *"TCCC and certain affiliates have agreed, subject to certain exceptions,
   not to compete in the energy drink category in certain territories"*. Coca-Cola owns 21% of Monster (Note 6) and its bottlers haul
   the cans; it does not own the brand.
6. **The bottlers keep part of every price rise.** The incidence model ties Atlanta's concentrate price to the bottler's selling price;
   the COKE run found the largest US bottler's gross margin rose 35.1% to 39.7% (2021-25) through the same pricing wave (*"BOTH:
   proportionally Atlanta, incrementally Charlotte"*).
7. **The portfolio bets outside the core have lost money**: BodyArmor's trademark was impaired by $760M (2024) and $960M (2025); the
   fairlife purchase cost $6.2bn more than first booked (remeasurement charges 2020-25, Step 0). Read at Q3; recorded here because
   a franchise that must keep buying new brands to grow is the [E4-04] question.

### What the filings show against that case
**[E2-44], the two-characteristic test, run the PEP way: volume against price/mix, year by year** (consolidated, % change in net
operating revenue, from each 10-K's MD&A table; FY2016-18 tables order the columns volume / acquisitions / price / currency, FY2019 on
volume / price / currency / acquisitions; `10K_FY*.flat.txt`):

| FY | volume | price/mix | currency | acq & div | total | unit cases, bn (system) |
|---|---|---|---|---|---|---|
| 2016 | 1 | 3 | (3) | (6) | (5) | 29.3 |
| 2017 | — | 3 | (1) | (17) | (15) | 29.2 |
| 2018 | 3 | 2 | (1) | (16) | (10) | 29.6 |
| 2019 | 1 | 5 | (4) | 7 | 9 | 30.3 |
| 2020 | (7) | (2) | (2) | — | (11) | 29.0 |
| 2021 | 9 | 6 | 1 | — | 17 | 31.3 |
| 2022 | 5 | 11 | (7) | 2 | 11 | 32.7 |
| 2023 | 2 | 10 | (4) | (1) | 6 | 33.3 |
| 2024 | 2 | 11 | (5) | (4) | 3 | 33.7 |
| 2025 | 1 | 4 | (2) | (1) | 2 | 33.8 |
| H1 2026 | 6* | 2 | 2 | (1) | 9 | unit cases +4% |

*H1 2026 concentrate volume carries *"six additional days"* in Q1; unit cases, on average daily sales, grew 4% (Q2 alone: +5%).

**The same table for North America, the one segment without a hyperinflation in it** (segment rows, same sources):

| FY | NA volume (concentrate) | NA price/mix | NA unit cases | NA operating income, $M | NA operating margin |
|---|---|---|---|---|---|
| 2020 | (7) | 2 | (7) | 2,471 | 21.5% |
| 2021 | 7 | 7 | 5 | 3,331 | 25.3% |
| 2022 | 1 | 12 | 2 | 3,742 | 23.9% |
| 2023 | (1) | 8 | (1) | 4,435 | 26.4% |
| 2024 | 1 | 10 | — | 4,336 (4,556 recast) | 23.3% (24.1% recast) |
| 2025 | (1) | 5 | (1) | 5,070 | 25.9% |
| H1 2026 | 7* | 3 | 3 | | |

**Read against [E2-44](1):** in the US, **price/mix compounded to about +49% over 2021-25 (1.07 x 1.12 x 1.08 x 1.10 x 1.05) while
unit cases held level from 2022 to 2025 and then grew 3% in H1 2026** (Q2: Trademark Coca-Cola +5% in North America), and the segment's
operating income rose from $3,331M to $5,070M (+52%) with the margin up. That is prices raised *"even when product demand is flat"*
and kept: the COKE run's own bottler series says the same from the other side of the contract (volume -1.3% cumulative against +52%
price per case, then +7.1% in H1 2026). **Set beside the same four years at PepsiCo** (the PEP run, its [E2-44] table, and the Q2 2026
10-Q): PBNA volume negative in eight of ten years, *"Unit volume declined 4%"* in the twelve weeks to 2026-06-13 and 3% in the 24 weeks,
Frito-Lay pricing negative. **Two brand owners, one country, one wave: one held price and volume, the other held neither.**
Worldwide, unit cases grew every year but the pandemic year, **29.3bn (2016) to 33.8bn (2025), +15%** [E4-55]: the physical series
is rising, not the Precision Steel shape.

**Read against [E2-44](2):** growth in dollars *"with only minor additional investment of capital"*: capex was $1.2-2.1bn a year on
$33-48bn of revenue (3.6-4.6%), falling as a share of revenue as bottlers were sold; the tangible operating capital is small (below).

**Who kept the pricing wave?** Three layers, from the filings: (a) Atlanta: NA margin 21.5% to 25.9%, consolidated gross margin 58.1%
(2022) to 61.6% (2025); (b) the bottler: COKE's gross margin 35.1% to 39.7% (COKE run, filed); (c) the rival: PBNA margin 13.8%
(2016) to 11.7% core (2025) (PEP run). **Both layers of the Coca-Cola system kept it; the rival did not.** The currency point (2) is
real and is carried into Q4 as dollar earning power: consolidated operating income before "other operating charges" went $10,544M
(2019), $9,850M (2020), $11,154M, $12,124M, $13,262M, $14,155M, **$15,023M (2025)**: **+35% over 2021-25 in dollars, after the
currency losses and after selling bottlers**, so the pricing is not all pesos.

**[E3-03], criterion by criterion, in the filer's words and numbers:**
- Needed or desired **[x]**: *"Consumers enjoy finished beverage products bearing trademarks owned by or licensed to the Company at a
  rate of 2.2 billion servings each day"*; 33.8bn unit cases, rising.
- No close substitute **[x], as the corpus defines it: in the buyer's mind, evidenced by conduct [E3-43]** (*"a company's ability to
  regularly price its product or service aggressively and thereby to earn high rates of return on capital"*). The shelf holds Pepsi
  and private label beside Coke (criterion 1 of the case against); the conduct shows the drinker does not treat them as close: US
  price +49% in five years with cases level, while the #2's cases fell at a lower price rise. The filer's Item 1A *"may restrict"*
  is a risk statement, not a recorded event: *"The favorable pricing initiatives for the year ended December 31, 2025 in all operating
  segments included both new and carryover pricing increases from the prior year"*.
- Not price-regulated **[x]**: sugar and packaging taxes are levied (Item 1A), and they cap volume at the margin ([E3-03](3) caps a
  franchise, it does not create or deny one); no authority sets the price.

**[E4-04], does the moat have to be rebuilt?** No, on the test the framework sets: *"does the spending defend the same advantage, or buy
its replacement?"* The spending that keeps the franchise is advertising ($5.4bn in 2025; $4bn in 2021, from the advertising-costs
note) on the same trademarks, and the framework's own worked example is this company (*"Coca-Cola's advertising defends the same
trademark"*). The base is not depleting: Trademark Coca-Cola is 47% of cases in both 2024 and 2025 (45% in 2016-19), and sparkling soft drinks 69% in every year
2016-25 on the definition the FY2017 10-K adopted (the FY2016 10-K's broader *"sparkling beverages"* read 72%; not comparable). **The acquisitions (Costa 2019, fairlife 2020, BodyArmor 2021) are adjacencies bought beside an intact base, not replacements for
a failing one**, and they are judged as capital allocation at Q3 [E3-40], not as a moat defect. The energy concession (case 5) narrows
the franchise's reach, it does not undermine its base. **Great-manager dependence [E4-23]: none recorded.** The CEO changed on
2026-03-31 (Quincey to Braun, a 30-year insider); Q2 2026, the first quarter under the new CEO, reported unit cases +5%.

**The primary moat metric [E3-46, E2-43]: pre-tax return on unleveraged net tangible operating assets, filing-sourced.** On the
project's standard formula (the PEP run's KO/KDP research file, faces transcribed with accessions; FY2025 recomputed here from the
10-K: 104,816 - 10,270 - 3,602 - 15,491 - 12,531 - 1,697 - 17,587 = 43,638): **31.8%, 35.7%, 33.2%, 31.0%, 31.5% (FY2021-25).** That
base holds **$17.6-20.2bn of equity-method stakes** whose earnings are below operating income, and in 2024-25 the $6bn IRS deposit.
Taking the equity stakes and the held-for-sale Africa net assets out of the base, as the operating income does (`peers/ntoa_ex_eq.py`):
**operating income on the remaining tangible operating capital was 69.6%, 88.8%, 78.4%, 71.1%, 66.7% (FY2021-25)**; before "other
operating charges", 75-101%. **The business earns its operating profit on roughly $12-21bn of tangible capital.** That is the
franchise signature [E3-46]: the return is high because the price is high relative to the capital, not because the capital is small
(contrast HBB's asset-light 20%).

**[E2-45], the attacker's test.** With ample capital and skilled people, would I like to compete with Coca-Cola in colas? The
experiment has been run for decades by the best-funded attacker available, PepsiCo, whose beverage segment's filed volume fell in eight
of ten years and whose margin fell through the wave; Keurig Dr Pepper grows in the US by buying brands (GHOST, then JDE Peet's in
April 2026, KDP 10-Q). **No.** The attacks that worked came in a new category (energy: Monster 10.6% revenue growth a year FY2021-25,
Celsius from $314M to $2,515M), and Coca-Cola answered that one with a 21% stake and its trucks rather than a brand.

**[E4-36], which cause of success?** Extreme maximisation of one or two variables: a brand everywhere (*"a permanent obsession"*, the
availability doctrine the corpus records at [E3-49]) and a toll on the system's revenue. Ownable, and owned.

**[E2-53], the dominance class.** The evidence is partial and I state it as such: the economics held through a CEO change, a
pandemic and an inflation, and the #2 with comparable resources has not dented them. That is position carrying the economics; it is
not proof that "good or bad, it will prosper".

**[E4-37] and [E3-33]:** no agony is visible: pricing *"in all operating segments"* every year, volume held. The pricing power is used,
not untapped; claiming the [E5-28] near-monopoly class is not needed and is not made (the shelf is contested; the drinker's preference is
the franchise).

**[E4-32], direction.** Units rising worldwide; US margin up; the company has reported **gaining value share in total nonalcoholic
ready-to-drink beverages in each of the 21 quarters from Q2 2021 to Q2 2026** in its furnished releases, after reporting a loss for full
year 2020 and for Q1 2021 (`EX99_*.flat.txt`; a company claim from syndicated data, unaudited, weighed as such; its candour in
reporting the two losses is noted). **Direction: stable to widening in units and share; narrowing only in the reach ceded in energy.**

### THE COMPETITOR ROW - required [E3-28]
Same metrics, same window (FY2021-25), each from the filer's own companyfacts, cross-read to the faces for KO (`peers/metrics.py`,
`peers/row.py`, output `peers/row_out.txt`); volume and pricing words from each filer's 10-K and latest 10-Q (`peers/*_10K_FY2025.txt`,
`*_10Q_2026Q2.txt`).

| Company | revenue FY2021 to FY2025, a year | operating margin, 5-yr | owner cash (OCF - capex - SBC) / revenue, 5-yr | gross margin FY2021 to FY2025 | volume and price, latest | source |
|---|---|---|---|---|---|---|
| **Coca-Cola (KO)** | $38,655M to $47,941M, **+5.5%** (after selling bottlers) | **25.3%** (21.2-28.7) | **17.6% as filed; 23.1% with the IRS deposit and fairlife milestone added back** | 60.3% to 61.6% | unit cases +5%, price/mix +2% (Q2 2026); NA price/mix +49% 2021-25 on level cases | 10-Ks FY2021-25; 10-Q `0001628280-26-050503` |
| PepsiCo (PEP), whole company | $79,474M to $93,925M, +4.3% | 13.3% | 7.6% | 53.3% to 54.1% | PBNA unit volume -4% (12 weeks to 2026-06-13), Frito-Lay pricing negative (PEP run) | 10-K `0000077476-26-000007`; 10-Q `0000077476-26-000035` |
| Keurig Dr Pepper (KDP) | $12,683M to $16,603M, +7.0% (GHOST inside; JDE Peet's from 2026-04-01) | 20.2% | 11.6% | 55.0% to 54.2% | US Refreshment volume/mix +6.5%, price +3.5% (Q2 2026), led by acquired energy | 10-K `0001418135-26-000016`; 10-Q `0001418135-26-000051` |
| Monster (MNST), 21% owned by KO, hauled by KO's bottlers | $5,541M to $8,294M, +10.6% | 27.8% | 18.7% | 56.1% to 55.8% | energy only; *"new entrants in the energy drink category"* | 10-K `0001104659-26-020831` |
| Celsius (CELH), distributed by PepsiCo | $314M to $2,515M, +68% | 6.5% | 9.1% | 40.8% to 50.4% | energy attacker; PepsiCo holder and distributor | 10-K `0001341766-26-000024` |
| Coca-Cola Consolidated (COKE), KO's largest US bottler | $5,563M to $7,228M, +6.8% | 11.6% | 7.0% | 35.1% to 39.7% | cases -1.3% 2020-25, +7.1% H1 2026 (COKE run) | COKE run; companyfacts |

**Return on unleveraged net tangible operating assets [E2-43]** (FY2025): KO 31.5% on the standard formula (66.7% without the equity
stakes); PEP 32.9% (42.7% core; 34.9% without its $2.0bn of equity stakes); KDP n.m. (NTOA $4.6bn against $44bn of goodwill and
intangibles; 7.4% including them); COKE 48.4% (COKE run). **On the standard formula PepsiCo's return is level with Coca-Cola's**, and
that is recorded honestly: the formula counts KO's $20bn of bottler stakes as operating capital. On the capital that produces the
operating income, KO's is about double PepsiCo's, and **KO's five-year owner cash per dollar of revenue is three times PepsiCo's and
twice KDP's.**

- **Peers named: 5 filers (PEP, KDP, MNST, CELH, and the bottler COKE) of the industry's ~10 real competitors** named in KO's Item 1:
  *"PepsiCo, Inc. is a primary competitor. Other significant competitors include ... Nestlé S.A., Keurig Dr Pepper Inc., Danone S.A.,
  Suntory Beverage & Food Limited, Anheuser-Busch InBev, Kirin Holdings, Heineken N.V., Diageo plc and Red Bull GmbH"*. **Unavailable:**
  Nestlé, Danone, Suntory, Kirin, Heineken, Diageo (foreign filers, IFRS, beverage lines unsegmented or alcoholic), Red Bull (private).
- **Is the missing data a reason to hold the moat PROVISIONAL?** No. The verdict rests on the subject's own ten-year physical and pricing
  series and on the head-to-head with the #2 in the same country and the same years; the missing peers are foreign owners of
  mostly different categories (beer, spirits, water, dairy) or, for Red Bull, the energy category already recorded as ceded. No
  missing peer's figures could turn a filed record of price +49% on level US cases into a no-franchise finding.
- **The row's limit [E3-61]:** it shows position, not conduct. The conduct that matters (KO's price discipline, PepsiCo's promotional
  turn) is read from the filings, not predicted.
- **Untapped pricing power [E3-33]:** none untapped; the power is being used every year.
- **Class: [x] WIDE, with two named limits** (the energy category ceded to an affiliate; a share of each price rise kept by the bottler
  under incidence pricing) · **Direction: stable to widening in units and share (21 quarters of claimed value-share gains, cases +15%
  in ten years); the dollar value of foreign pricing is cut by currency every year since 2022, carried to Q4.**

**Priors argued against, as instructed.** The prior most likely wrong was mine: that the corpus's most-cited franchise is still one.
The seven-point case against was built from the filer's own text before the numbers were read, and three of its points stand as
limits (currency, the bottler's share, energy), one as a Q4 exposure (health and taxes), one as a Q3 question (acquisitions). **What
refutes the case for OUT is the head-to-head record**: in the same country, through the same inflation, Coca-Cola raised prices about
49% on level cases and grew its segment profit 52%, while the #2 lost volume and margin. The famous past played no part: nothing
before FY2016 is used.

- **VERDICT: [x] IN - class WIDE, on [E3-03] (all three), [E3-43], [E2-44] (both characteristics), [E4-55], [E2-43], [E2-45] and
  [E4-04]**, with the energy concession and the bottler's share recorded as limits.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 - THE WEIGHT CASE.**
- [ ] **Daily execution** **[E3-38]** - not ticked. Q2 found a franchise, and [E3-43]'s original form is that *"franchises can
  tolerate mis-management"*; the product is not *"promises"* re-won each season. The daily execution sits with ~200 bottlers.
- [ ] **Control** **[E1-16]** - a minority holder of a widely held company with an exit every trading day.
- [ ] **Leverage** **[E3-29]** - total debt $45.5bn at 2025-12-31 (loans $1,551M, current maturities $1,822M, long-term $42,119M;
  FY2025 10-K balance sheet) against operating income before other operating charges of $15.0bn and equity of $34.3bn; A+/A1 rated
  (*"our long-term debt was rated 'A+' by Standard & Poor's and 'A1' by Moody's"*). Material, not the small-asset-error class.
- **Case declared: OVERLAY.** Findings are recorded; a mediocre manager is survivable and price does the work. The binary still
  runs: an integrity failure would be OUT.

**Honesty - binary [E5-16], each matter dated to when it became public.**
- **The IRS transfer-pricing case (Notice 2015-09-17; Tax Court opinions 2020-11-18 and 2023-11-08; decision 2024-08-02; Eleventh
  Circuit argued 2026-06-25).** A dispute over which method prices the foreign licensees' royalty, under a 1996 closing agreement the
  IRS audited *"in five successive audit cycles for tax years 1996 through 2006"*; *"Consistent with the Closing Agreement, the IRS did
  not assert penalties, and it has yet to do so."* **Not a conduct finding.** It is a candor test, and the company passes it: the
  10-K and every 10-Q print the full exposure, *"approximately $ 14 billion"* for 2010-25, the quarterly accrual, the effective-rate
  effect (*"approximately 3.8 %"*), and the reserve ($529M) beside management's *"more likely than not"* view, so a reader can form
  the opposite view from the company's own numbers.
- **Item 3 Legal Proceedings, FY2025 10-K:** Aqua-Chem (a 1970-81 subsidiary's asbestos coverage, stayed since 2004) and the tax case.
  A grep of the FY2021, FY2023 and FY2025 10-Ks for securities class actions, SEC investigations, FCPA matters, subpoenas and
  consent decrees returned no instance (recorded as no instance found, per the absence-claim rule).
- **2026-07-16, fairlife ransomware**: disclosed by 8-K the day it was announced, with production systems named. A Q4 exposure,
  not a conduct matter.
- **Binary: IN (no disqualifier found).** Not a finding that the managers are honest [E5-17].

**STEP 2 - THE FLAGS [E4-22, E5-15], read in the 10-Ks AND in the 23 furnished EX-99.1 earnings releases, 2021-02-10 to 2026-07-28**
(`EX99_*.flat.txt`; counts in `release_metric_counts.txt`):
- [ ] weak accounting - not fired. Stock pay expensed since long before the window ($254-356M a year); the pension return
  assumption is *"6.25 % for pension plans"* (2026) against a 5.34% long bond, not fanciful; Ernst & Young, effective controls. **Two
  cash-flow levers are recorded as prompts, not fires**: the receivables factoring programme (*"The cash received from the financial
  institutions is classified within the operating activities section"*; $14.7-21.9bn sold a year; the year-end balance outstanding is
  not disclosed in what I read, so its lift to operating cash cannot be measured, only named) and the transfers of *"surplus
  international plan assets"* from pension trusts into company cash ($523M 2024, $332M 2025). Both are named by the filer in its MD&A
  cash-flow explanation, which is the candor case; both are carried to Q4.
- [ ] unintelligible footnotes - no. The fairlife, tax and held-for-sale notes are plain and quantified.
- [x] **projections - FIRED, and the record is read [E3-48].** Annual guidance every February, on non-GAAP measures, and a
  published long-term growth algorithm (*"publicly stated long-term growth plan of 4% to 6% for organic revenue (non-GAAP) growth and
  6% to 8% for comparable currency neutral operating income (non-GAAP) growth"*, DEF 14A 2026). **Guidance against outturn, from the
  February releases:** organic revenue guided high single digits / 7-8% / 7-8% / 6-7% / 5-6% for 2021-25, delivered **16% / 16% / 12% /
  12% / 5%**; comparable EPS guided high-single to low-double digits / 5-6% / 4-5% / 4-5% / 2-3%, delivered **+19% ($2.32) / +7%
  ($2.48) / +8% ($2.69) / +7% ($2.88) / +4% ($3.00)**. Ten calls, nine beats and one at the low end (2025 organic revenue). The
  organic-revenue beats of 2022-24 rode the inflationary pricing that currency took back (Q2), so the beat is flattered by the metric,
  not invented. [E5-30]'s ratchet exists (a guidance culture of decades); the calls are modest and beaten.
- [ ] serial share issuance [E5-15] - no. Shares outstanding 4,328M (start of 2023) to 4,302M (end of 2025) to 4,302.5M (cover
  2026-07-27): issuance to employees ($313-837M a year) more than bought back.
- [ ] **EBITDA [E4-29] - CLEAN in all 23 releases** (the word appears zero times).
- [x] **"Comparable" and "currency neutral" - the except-for flag [E2-57] FIRES, and the pay plan is where it bites.** Every
  release leads with *"Comparable Currency Neutral Operating Income (Non-GAAP)"* and *"Comparable EPS (Non-GAAP)"* (the phrases appear
  79-121 times per release). What "comparable" removes is not all one-off: the **fairlife remeasurement** (the price of an acquisition
  management chose, $6.2bn of it, 2020-25), the **BodyArmor impairments** ($1.72bn, 2024-25), and the **productivity and reinvestment
  programme** charged every year (*"$ 97 million"* 2025, $133M 2024, $164M 2023; $264M in 2019), which [E5-33] and [E3-53] treat as
  normal costs. What "currency neutral" removes is a cost the owner bears every year in dollars: **operating income -9%, -8%, -11%,
  -12% from currency, 2022-25.** The headline gap in one year: FY2024 operating income **-12%** GAAP against *"Comparable Currency
  Neutral Operating Income (Non-GAAP) ... 16% for the Full Year"*. **Mitigated, and the mitigation is real:** each release also prints
  the GAAP figure first in the headline pair, names the fairlife charge and the BodyArmor impairment in words, and the cash-flow line is
  GAAP operating cash with the one-offs named (*"cash flow from operations and free cash flow (non-GAAP) were $7.4 billion and $5.3
  billion, respectively, which reflects $6.1 billion of the contingent consideration payment"*). [E2-26]'s positions-reversed test is
  passed on disclosure; [E2-57] fires on what is counted.
- [x] **What pay vests on [E4-27], from the DEF 14A 2026:** the annual incentive is *"equally weighted between net operating revenue
  growth and operating income growth"*, both organic or comparable currency-neutral, with targets *"at the midpoint of the Company's
  publicly stated long-term growth plan"*; the PSUs weigh *"net operating revenue growth, earnings per share growth and free cash
  flow"* equally, the cash-flow measure *"adjusted ... to exclude acquisitions, divestitures and structural changes that are significant
  to the Company as a whole and impacts resulting from the application of the tax court rulings"*, with a relative-TSR modifier. **Pay
  vests on growth, with currency, the fairlife price and the tax case taken out; no measure is a return on capital [E2-01].** *"All
  financial performance measures in the PSU program exceeded the maximum performance levels"* for 2023-25, the three years in which
  GAAP operating income fell 12% in one year and $6.2bn went to fairlife. Incentives point at growth over return; the prompt is
  recorded. The relative-TSR modifier is a mild [E3-50] prompt (pay moved by the share price), not a fire.
- [ ] filed-figure tells [E4-30] - no. **Cash taxes paid as a share of pretax income** (10-K tax notes: *"We made income tax
  payments of ..."*): 25.8% (2018), 19.7%, 13.0% (2020), 17.4%, 20.6%, 19.9%, 24.9% (2024), 18.0% (2025), with no falling trend, and
  2021-24 include the transition-tax instalments; the $6.0bn deposit is outside these figures. Reported growth is not smooth
  (operating income -11% in 2020, -12% in 2024, +38% in 2025).
- **[E2-49] metric-switching, checked across the releases and proxies: not fired.** The one new measure, *"free cash flow excluding
  the fairlife contingent consideration payment (non-GAAP)"*, was announced in the February 2025 guidance, **before** the payment, with
  its reason: the candor case the framework names. The 2026 guidance adds *"comparable currency neutral EPS excluding acquisitions and
  divestitures"*, announced ahead of the Africa sale; a prompt to watch, not a switch after deterioration.

**STEP 3 - THE PRIMARY TEST [E2-01]**, balance sheet first. Net income on average shareowners' equity (companyfacts, cross-read to the
faces; `roe_out.txt`): **49.6% (2019), 40.5%, 46.2%, 40.5%, 42.8%, 41.9%, 46.0% (2025)**. [E2-47]'s carve-out applies: equity is
shrunk by $56.4bn of treasury stock and $14.1bn of accumulated currency losses, so the ratio overstates. The honest denominator is
Q2's [E2-43] figure: **31-36% on all net tangible operating assets including $18-20bn of bottler stakes, 67-89% on the assets that
earn the operating income**, level across the five years, not rising. *"Without undue leverage"*: debt was $42.8bn (2019) and $45.5bn
(2025) while operating income before charges rose 42%; leverage fell.

**Candor [E2-26, E2-72]:** passes on the big items (tax exposure quantified to the quarter; the fairlife and IRS cash named in the
headline cash line; share losses reported in the releases of 2021-02-10 and 2021-04-19 as well as gains). **Authorship [E2-72]:** the release
quotes are the CEO's; neither the 10-K nor the proxy read here carries a CEO letter to owners (the proxy's letter is from the Talent
and Compensation Committee). The annual report outside the 10-K was not fetched; not scored.

**The institutional imperative [E2-30]:**
- [ ] resists change - no: bottlers refranchised every year; Global Ventures dissolved (8-K 2025-03-27); a CEO succession from inside.
- [x] **acquisitions materialise to soak up funds - FIRED, mixed record.** Costa, January 2019, *"$ 4.9 billion of cash"*; fairlife, 2020,
  $979M plus milestones of $100M, $275M and $6,173M on a formula *"not subject to a ceiling"*; BodyArmor, November 2021, *"approximately
  $ 5,600 million of cash"*: **about $18bn in three years**. BodyArmor's trademark was written down $760M and $960M, the second time
  for *"a slowing of the projected long-term growth rate for the category, an intensifying competitive environment"*: the
  franchise did not transfer to a bought brand in a category Gatorade leads. fairlife's cost rose because it outperformed its
  targets: KO paid $6.2bn more than booked for a business that did better than planned, which is expensive, not a failure. No Costa
  impairment was found in the FY2020-25 10-Ks (grep; no instance found). **[E3-40]'s test, the base business neglected?** No: the base's
  volume, price and US margin rose through the same years (Q2). **[E2-56], the Pro-Am effect:** the consolidated return hides the
  acquisitions' returns; the BodyArmor write-downs are the visible part.
- [ ] staff studies - no instance found.
- [x] **peer imitation - mild.** "Total beverage company" breadth (coffee, dairy, sports drinks) alongside PepsiCo's (Rockstar, whose
  $1.9bn impairment the PEP run recorded); both leaders bought outside the core and both wrote down a sports or energy brand.

**Capital allocation - the buyback conditions [E5-08, E4-31, E5-24]:**
- (1) ample funds: yes; A+ credit, $16.4bn of cash, short-term investments and marketable securities at 2026-07-03.
- (2) a material discount to conservatively calculated value: repurchases were $2,289M (2023), $1,795M (2024), $746M (2025) and $663M
  (H1 2026), at average prices near the market ($76.63-$80.23 a share in Q2 2026). On the owner earnings Q4 builds (about $10bn a year
  on the adjusted five-year mean), a price of $60-90 on about 4.3bn shares is a yield of roughly 2.6-3.9%, below the long bond: **not a
  material discount.** The buyback has mostly offset employee issuance (net shares -0.6% over 2023-25), which is compensation, not
  allocation. **CAPITAL-ALLOCATION FLAG, with the humility clause [E4-13]: management knows the business better than I do, and this
  rests on my own range.** It binds position size, never the rate.
- **Dividends [E2-52, E2-60]:** $7,252M (2021) to $8,779M (2025), raised every year. Not funded by share issuance (count flat). In 2024
  and 2025 the dividend exceeded GAAP free cash flow ($4.7bn and $5.3bn against $8.4bn and $8.8bn) because the IRS deposit and the
  fairlife payment sat inside operating cash; the gap was met by $6bn and EUR2bn of 2024 notes, disposal proceeds of $3.5bn and $3.6bn,
  and the India minority sale ($1.3bn). **Without those two payments, free cash flow covered the dividend in every year of the window**
  (Q4). Recorded as a prompt for [E2-60]'s third dimension, financial strength, not as a fire: total debt is flat over seven years.

**THE GUARDRAIL:** [x] nothing in this Q3 promotes the name; a disciplined pricing record and a candid tax note cannot repair a later
gate [E2-37, E2-38, E3-39]. [x] No superstar dependence recorded at Q2 [E4-23]; the succession was internal and uneventful in the
filed numbers. [x] The manager is not the plan [E2-35, E2-36].

- **VERDICT: [x] IN** on the binary (no disqualifier found), with four prompts recorded: [E2-57] except-for on "comparable" and
  "currency neutral" measures, which the pay plan also uses [E4-27]; the projections culture [E3-48] (beaten, modest); acquisitions that
  soaked $18bn with one clear write-down [E2-30]; and a capital-allocation flag on buybacks near value [E5-08]. *IN = no disqualifier
  found, not a finding that the managers are honest [E5-17]. IN never promotes.*

## Q4 — WILL IT SURVIVE?

### Owner earnings - the one number **[E2-23]**, rebuilt from the filed cash-flow faces (`oe.py`, output `oe_out.txt`), $M
CONVENTION per v4: operating cash flow less stock pay less (c). Every adjustment below is a **disclosed judgment**, shown beside the
as-filed figure so a reader can take either.

| FY | OCF as filed | + IRS deposit | + fairlife milestone (operating part) | - pension surplus transfer | - tax-credit partnerships | OCF adjusted | SBC | capex | D&A | **OE, capex end** | **OE, D&A end** | undistributed equity income |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 10,471 | | | | | 10,471 | 201 | 2,054 | 1,365 | 8,216 | 8,905 | 421 |
| 2020 | 9,844 | | | | | 9,844 | 126 | 1,177 | 1,536 | 8,541 | 8,182 | 511 |
| 2021 | 12,625 | | | | | 12,625 | 337 | 1,367 | 1,452 | 10,921 | 10,836 | 615 |
| 2022 | 11,018 | | | | | 11,018 | 356 | 1,484 | 1,260 | 9,178 | 9,402 | 838 |
| 2023 | 11,599 | | 167 | | | 11,766 | 254 | 1,852 | 1,128 | 9,660 | 10,384 | 1,019 |
| 2024 | 6,805 | 6,000 | | (523) | (226) | 12,056 | 286 | 2,064 | 1,075 | 9,706 | 10,695 | 802 |
| 2025 | 7,408 | | 6,069 | (332) | (306) | 12,839 | 279 | 2,112 | 1,050 | 10,448 | 11,510 | 1,038 |
| TTM to 2026-07-03 | 16,342 | | | | (233) | 16,109 | 266 | 2,045 | 1,034 | 13,798 | 14,809 | 1,171 |

**How each item enters, and why (the brief's three questions):**
1. **The IRS deposit, $6.0bn in 2024: added back.** It is tax and interest for **2007-09**, paid under protest *"which stopped interest
   from accruing"* and refundable if the appeal succeeds; it is not a cost of 2024's business. **Its risk is not dropped**: it is carried
   whole into the named death below (the deposit lost, about $14bn more for 2010-25, and a higher tax rate from 2026).
2. **The fairlife milestones, $167M (2023) and $6,069M (2025) of operating cash: added back.** They are the purchase price of fairlife,
   paid on an uncapped earn-out formula, classified in operating cash only because they exceeded the acquisition-date fair value.
   Owner earnings measures the cash the business produces; the price paid for a business is capital allocation, and it is **charged
   at Q3** (about $7.5bn in all for fairlife; an [E2-30] prompt). fairlife's own earnings are inside every year's operating cash since
   2020. The 2021 milestone ($100M) is left in: its split is not disclosed in what I read, and it is small.
3. **Equity-method income: not in the base.** Operating cash counts only the dividends the bottlers pay (*"Equity (income) loss - net of
   dividends"* is deducted on the face: $615M to $1,038M a year). The undistributed share is shown in the last column as [E3-04]'s
   look-through and added only at the top of the range. It is **not** owner earnings in the [E2-60] sense until paid: these are bottlers
   that must reinvest to hold their territories (the COKE run's capex ran 2.3x D&A), and GAAP equity income is not their owner earnings.
4. **The pension surplus transfers ($523M, $332M): removed** [E4-41], a favourable one-time inflow named by the filer.
5. **The tax-credit partnerships: subtracted.** The cash spent buying the credits ($226M, $306M, $233M TTM) sits in investing while the
   tax saved sits in operating cash; the pair belongs together.
6. **Left in, and named:** the receivables factoring programme (lift to operating cash not measurable from what is disclosed); the
   one-time transition-tax instalments of the 2017 Tax Act inside the tax paid ($385M 2021 and 2022, $723M 2023, $964M 2024, from the
   tax notes), which end with 2025 and bias the window **down**; the BodyArmor holdback payments ($637M 2022, $311M 2023), which sit in
   financing and are acquisition price.

**THE WINDOWS AND BOTH (c) ENDS [E4-25, E4-38]** - every window, both ends, as filed and adjusted:

| window | as filed, capex end | as filed, D&A end | **adjusted, capex end** | adjusted, D&A end | look-through added to the adjusted D&A end |
|---|---|---|---|---|---|
| **5-year FY2021-25 (the default [E2-42])** | 7,813 | 8,396 | **9,983** | 10,565 | 11,427 |
| 3-year FY2023-25 | 6,322 | 7,247 | **9,938** | 10,863 | 11,816 |
| 7-year FY2019-25 | 7,974 | 8,438 | **9,524** | 9,988 | 10,737 |
| TTM to 2026-07-03 | | | 13,798 | 14,809 | 15,980 |

*Cross-check:* `tools/run.py KO` printed the as-filed five-year range *"OE 7,795 .. 8,412"* and three-year *"6,322 .. 7,247"*; the
three-year reproduces exactly and the five-year within $18M (its stock-pay pick differs slightly). **The tool's figures are the as-filed
column, and they are about $2bn a year low because two one-offs of $6bn each sit inside the latest three years.**

- **Spread, conservative end:** adjusted, the three windows agree within 5% ($9.5-10.0bn at the capex end); **the spread is not
  width, it is two named one-offs**, and once they are treated the record is steady. The TTM ($13.8bn) is not used as a level: the 10-Q
  names *"a benefit of the trade accounts receivable factoring program"*, *"lower income tax payments"* and *"lower annual incentive
  payments"*, and the first quarter carried *"six additional days"*; management's own 2026 guide is *"cash flow from operations of
  approximately $14.4 billion"* against the TTM's $16.3bn.
- **Combined range: $7.8bn (as filed, five-year, capex end) to $11.4bn (adjusted, D&A end, with look-through); the default, the
  adjusted five-year capex end, is about $10.0bn.** Not too wide to conclude: the ends differ by named items, not by guesswork.
- **(c), a disclosed judgment [E3-44, E2-41, E5-20].** Coca-Cola is not in [E5-20]'s capital-intensive class (capex 3.6-4.6% of
  revenue; net PP&E $9.6bn against $47.9bn of revenue), so **the D&A end is admissible**. But capex has run at about twice D&A for three
  years ($1,852M/$1,128M, $2,064M/$1,075M, $2,112M/$1,050M), and the segment note shows where: North America $669M against $326M of
  D&A, Corporate $585M against $159M, Bottling Investments $547M against $313M (FY2025 Note 20); 2026 capex is guided at *"approximately
  $2.2 billion"*. Part is growth (the bottlers being sold, the fairlife capacity), part may be that depreciation charged on a shrinking,
  refranchised plant understates renewal. **I sit at the capex end as the default**, because the filing does not split maintenance from
  growth and the gap is recent and persistent; the D&A end is the display of the guess [E2-09].
- **Stock compensation [E5-06]: RESOLVES and is COMPLETE as far as the filings show.** *"Stock-based compensation expense"* is a line on
  every cash-flow face read, seven of seven years ($126-356M), subtracted in full (the cash-flow add-back, $279M in 2025, is the larger
  of it and the equity statement's $266M). The US matching contribution is a cash expense (*"The Company's expense for the U.S. plans
  totaled $ 48 million"*); no stock-settled match was found. At 2-4% of operating cash, [E3-70]'s grant-value measure does not change
  the answer and was not built.
- **Working-capital increment:** inside operating cash. Adjusted for the two one-offs, the net change in operating assets and
  liabilities was +$1,325M (2021), -$605M, -$846M, about -$234M and about -$1,139M (2025): no build that flatters the mean.
- **Does the capex band change the verdict?** No: both ends are about $10bn and positive in every year, as filed and adjusted.

### Great, good, or gruesome? **[E4-20]**
- [x] **great** [ ] good [ ] gruesome. Operating income of $15.0bn before other operating charges on roughly $12-21bn of tangible
  operating capital outside the bottler stakes (Q2), capex 4% of revenue, and dollar operating income before charges up 42% from 2019
  to 2025 while tangible capital shrank with each refranchising. The rate is not rising in every year ([E2-43] 67-89%, level), so
  "great" is carried with the plain note that the rise is in dollars earned, not in the ratio.

### Staying power **[E5-11]** - scored in the worst case, not the expected one **[E2-55]**
- (1) **a large and reliable stream of earnings: yes.** Adjusted owner earnings $8.2-10.9bn in every year 2019-25, the pandemic year
  included ($8.5bn); as filed, the lowest year is 2024 at $4.5bn, and positive in all seven.
- (2) **massive liquid assets: yes.** $12,907M of cash and equivalents, $622M of short-term investments and $2,842M of marketable
  securities at 2026-07-03, **$16.4bn**; beside them listed bottler stakes with a quoted value of **$34.3bn** at 2025-12-31 (*"Total | $ |
  34,286"*, Note 6), saleable and repeatedly sold (CCEP, COKE, Thailand, 2024-25). The $6.5bn deposit and interest receivable is not
  counted as liquid.
- (3) **no significant near-term cash requirements: mostly yes, with one large contingent requirement.** Current maturities $6,494M
  and loans $48M at 2026-07-03; dividends about $8.8bn a year, which the adjusted owner earnings cover (about 1.1x at the capex end; the
  thinnest strength, and it is a choice, not a contract). **The contingent requirement is the tax case**: if the Eleventh Circuit
  affirms, the $6.0bn deposit and $514M of interest are not refunded, and the company *"would likely be subject to significant additional
  liabilities for subsequent years"*, which it estimates at *"approximately $ 14 billion as of December 31, 2025"*, growing about $0.9bn a
  half-year. The appeal was argued 2026-06-25; the decision date is unknown.
- **Leverage [E4-16, E2-54, E3-52]:** debt $43.5bn at 2026-07-03, flat since 2019 ($42.8bn); interest expense $1,654M in 2025 against
  interest income of $786M; owner earnings plus interest cover interest about seven times, *"comfortably met out of current cash flow net
  of ample capital expenditures"*. The debt is mostly long-dated notes (twenty euro issues are listed on the 10-K cover, maturing 2026-53), with no financial
  covenant found in what I read; A+/A1. Moderate, deliberate, not the [E4-16] kind.

### The specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**
**Model exposure, not experience [E4-40].** The last decade's record is good; the exposure list comes from what the filing says the
business is exposed to.

**1. The sovereign re-prices the royalty (the tax case), quantified.** Worst case, all at once: the deposit written off ($6.5bn with
interest), about $14bn of 2010-25 tax and interest paid, and the effective tax rate *"approximately 3.8 %"* higher from 2026. On 2025's
pretax income of $15,998M, 3.8 points is **about $0.6bn a year**, 6% of the adjusted owner earnings. The lump sum of about **$20bn**
is two years of owner earnings: met from $16.4bn of liquid assets, the saleable stakes, or new debt against $10bn a year of earnings.
**Outcome: a large loss of value, not death.** Likelihood: **a real possibility**, stated as the filer frames it (the Tax Court sided with
the IRS on the method in 2020 and 2023; management holds its *"more likely than not"* view; the 3M reversal of 2025-10-01 bears on one
part, the blocked-income regulation, not on the method).

**2. The drinker leaves, slowly (the named death, stated as its holders would state it [E4-51]).** Sparkling soft drinks are 69% of
cases and Trademark Coca-Cola 47%. The filer names the mechanism: concern about *"obesity"*, *"the effects or perceived effects of the
usage of weight-loss drugs on consumption patterns"*, *"potential new or increased taxes on sweetened beverages"*, and packaging rules.
In the richest market the volume is already level (US unit cases +2, -1, 0, -1 in 2022-25), and the profit growth there has come from
price (+49% in five years). The growth in cases is in India, China, Brazil and Africa, **whose currencies cut consolidated operating
income by 8-12% a year in 2022-25.** The death is the three together: rich-market volume falls a few points a year as the habit weakens
under drugs, taxes and labels; the price rises that carried the US stop being accepted ([E4-37]'s agony returns); and the emerging-market
growth arrives in currencies that lose value against the owner's dollar. **Quantified from filed figures:** North America is 40.8% of
revenue and earned $5,070M in 2025; a 3% a year fall in US cases for ten years with price only matching cost would take about a quarter
(0.97^10 = 0.74) of that segment's $19,586M of revenue, and **$1.3bn a year of operating income at the segment's 25.9% operating
margin, up to $2.6bn at its 51.8% gross margin if no cost follows the volume down** (Note 20: revenue $19,586M, cost of goods $9,438M), while a
continued currency drag at 2025's -12% would consume most of the growth elsewhere. The business would still earn about $8bn a year; the
owner's return would be a dividend with no growth. **Outcome: stagnation, not insolvency. Likelihood: a real possibility for the
stagnation; a low-level possibility for anything worse** (no filed series yet shows it: worldwide cases +15% in ten years, US Trademark
Coca-Cola +5% in Q2 2026).

**3. Considered and not the death:** a bottler failing (the largest are listed, A-rated or equity-rich, and territories are re-granted,
as 2013-17 showed at COKE); a fairlife-type cyber event (disclosed 2026-07-16; one dairy business); the Africa sale failing (the
business is held for sale at $3.0bn net, a small share of value).

**Survival shape [`Screens/SURVIVAL SHAPES - index.md`].** None of #1-#21 fits the main mechanism: it is not a pass-through (#11: the
gains are not competed away; the filer keeps them), not the shelf (#19: the brand is owned and the drinker, not the retailer, chooses),
not the patron (#14: no government funds the plant). **Proposed #22, THE HABIT** *(pending the operator)*: *the franchise is a consumer
habit priced above its cost for decades; medicine, taxes and labels can weaken the habit market by market; the business lives, the
volume in the richest markets drifts down, and the growth left arrives in currencies that lose value against the owner's.* The tax case
is carried as a feature (the home sovereign re-pricing the royalty), not as the shape.

- **VERDICT: [x] IN** - owner earnings positive in every year, window and (c) end, as filed and adjusted (default about $10.0bn, range
  $7.8-11.4bn); great on the capital employed; two strengths fully present and the third present with one large, quantified contingency
  (the tax case, about $20bn at worst, met from liquid assets and saleable stakes); the named death is stagnation, not insolvency.
  **[E4-51]'s bear case above is the one its holders would accept.**

---
⛔ **Q5 opens: Q1, Q2, Q3 and Q4 each show IN.** Counted from the register in `Screens/WATCHLIST RUN QUEUE.md`
(117 entries before this one: 28 closed at Q5, every one of them after clearing Q1-Q4; 83 at Q2, 2 at Q4, 4 at Q1), Coca-Cola is the
29th entry in that register to clear all four business gates.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
Arithmetic in `q5.py`, output `q5_out.txt`. Market cap $379.7bn (Step 0). Sovereign **5.34%** (US Treasury 30-year, 09/18/2026).

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*

**1. THE YIELD** (owner earnings / market cap, every construction Q4 built):

| construction | owner earnings | yield | points against 5.34% |
|---|---|---|---|
| **default: adjusted five-year, capex end** | **$9,983M** | **2.63%** | **-2.71** |
| adjusted five-year, D&A end | $10,565M | 2.78% | -2.56 |
| adjusted five-year, D&A end, with [E3-04] look-through | $11,427M | 3.01% | -2.33 |
| as filed five-year, capex end (the tool's figure) | $7,813M | 2.06% | -3.28 |
| TTM to 2026-07-03, adjusted, capex end (flattered, Q4) | $13,798M | 3.63% | -1.71 |

**Below the long bond on every construction, including the most generous.**

**2. WHAT THE PRICE ALREADY ASSUMES** (the growth, in perpetuity from year one, at which owner earnings discounted at the rate
equal the price; a DCF used as an engine only, casting no vote [E3-34]):
- to match the **bond**: **2.6%** a year (default), 2.3% (most generous), 3.2% (as filed);
- to reach the **~10% floor**: **7.2%** a year (default), 6.8% (most generous), 6.1% even on the flattered TTM.
- **What the business has actually done, 2019-25** (the widest filed window, across the pandemic, in dollars): adjusted owner earnings
  at the capex end **+4.1% a year** ($8,216M to $10,448M); operating income before other operating charges **+6.1%** ($10,544M to
  $15,023M); revenue **+4.3%** after selling bottlers. **The floor needs more than the business's best filed measure has done, forever.**
- **Against the corpus's base rates:** a perpetual 7% for a $380bn business asks for growth well above the nominal economy it sells
  into; [E4-44] (*"the value of an asset ... cannot over the long term grow faster than its earnings do"*) and [E4-35] (fewer than 10 of
  the 200 most profitable companies attain 15% EPS growth for 20 years) put the burden on the believer, and Coca-Cola's own filed
  7-year record is 4-6%. **The Tinker Bell growth is not granted.**

**3. WHAT YOU ARE PAID:** **-2.7 points against the sovereign** on the default static yield. As an expectancy (yield plus the growth the
record supports, 4.1-6.1%): **about 6.8% to 9.3%** (`q5_out.txt`: 6.8% at the default with 4.1%; 9.3% at the most generous earnings
with 6.1%), **below the ~10% floor on every combination the filings support.**

**THE FLOOR VERDICT FIRST [E4-28]: honest expectancy ~7-9% against ~10%. QUIT ON; not ranked, however it compares with the bond of the
day.** (It is also below the bond on the static yield, so this is not the Berkshire case where the floor and the bond disagree.)

**WHERE CERTAINTY IS PRICED [E3-42]:** the bare 5.34%; no per-name premium. Certainty was handled at Q1 and would be handled in the end
margin; it is not reached.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** - at the ~10% floor, owner earnings $10.0-11.4bn growing 4.1-6.1% a year:
**about $175bn to $310bn, roughly $40 to $70 a share.** Current price **$88.25**. **The price is above the whole range**: [E4-01]'s third
outcome, *no*. (The two-year low, $60.81 on 2025-01-06, sat inside the range; it would have been a middle-outcome *no useful
conclusion*, not a screamer.) **What bounds the upside [E2-63]:** a business growing with the nominal economy, returning nearly all its
earnings as dividends; no reinvestment runway large enough to change the rate.
*Context, not evidence:* the 1988 price in CASE 2 of the verification file assumed 1.2% growth against a 9% bond; today's price assumes
2.6% just to match a 5.34% bond and 7.2% to reach the floor. The same franchise; a different price.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21]:**
- floor verdict: honest expectancy ~7-9% vs ~10% **[E4-28] - below: quit on; the ranking lines are not filled in.**

**WHICH BAR?** Neither is applied: the floor closes the question before a margin is needed. For the record, **Bar 2 [E4-01] would read
"above the whole range: no"**. **Windage count: one** (the capex end of (c) chosen as the default); the IRS deposit and fairlife
add-backs move owner earnings **up**, the look-through is shown separately, and the tax-case risk is carried at Q4 rather than deducted
from the yield, so conservatism is not stacked.

- **VERDICT: QUIT ON at the [E4-28] floor - FAIL ON PRICE. Ranking position: not ranked.** Not UNKNOWABLE: the range is narrow enough
  to conclude, and it concludes *no*.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists or is opened. This section pre-commits the re-look, as the queue does for floor-fail gate-clearers.)*

**Pre-committed before any entry [E1-02]:**
- **Thesis-confirming metrics:** worldwide unit cases rising (33.8bn in 2025); North America unit cases level or rising with positive
  price/mix; consolidated operating income before other operating charges rising in dollars after currency; the filed value-share claim
  holding.
- **Thesis-breaking metrics and thresholds (the Q2 falsifiers):** (i) **two consecutive years of negative worldwide unit cases**
  outside a pandemic; (ii) **North America price/mix negative in a year when commodity costs fell** (the PEP/HBB pass-through shape);
  (iii) **North America unit cases down 3% or more in two consecutive years** (the named death arriving); (iv) currency cutting
  operating income by more than 10% in a year while price/mix is below 5% (the pesos no longer covered); (v) [E2-49]: withdrawal of the
  unit-case or price/mix tables, or of the value-share line after a loss.
- **The tax case, the one dated event:** the Eleventh Circuit's decision (argued 2026-06-25). **An affirmance re-prices the business
  by about $20bn and 6% of owner earnings (Q4) and requires a re-run of Q4 and Q5; a reversal returns $6.5bn and removes the 3.8-point
  tax-rate risk.** Either way it is read when it lands.
- **Re-look prices, recomputed at the rate of the day:** **at or below about $63** (the ~10% floor met if the 2019-25 growth of
  operating income before charges, 6.1%, is granted in perpetuity on $10.0bn of owner earnings) - a prompt for a full v4.1 re-run in
  which that growth is re-tested before it is spent; **at or below about $41** (the floor met on the owner-earnings record itself,
  4.1%) - the price at which the name would clear the floor on filed growth alone. **Neither is a buy signal; each is a prompt to re-run
  the gates.**
- **Next catalyst dates:** the Q3 2026 10-Q (late October 2026: the six fewer days in Q4 2026, the factoring lift, fairlife after the
  ransomware event); the Eleventh Circuit decision (date unknown); the Africa closing (*"expected by the end of 2026"*); the FY2026 10-K
  (February 2027) to rebuild the windows with the fairlife and IRS years one step further back.

**The sell rule [E2-28]** - recorded for a future holder: hold while the return on the capital that earns the operating income stays
high (Q2's 67-89%), no integrity event occurs and the except-for gap between "comparable" and GAAP does not widen, and the market does
not overvalue the business; **at $88.25 the third condition would already be in question for a holder**, which is recorded, not acted
on, since there is no position.

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question here: is a year of flat US cases
the weight-loss-drug and sugar-tax trend arriving (permanent), or a price-elasticity pause after +49% in five years (aberrational)?
The unit-case table decides it, not the value-share claim.

**Do not trim winners [E5-14]. Position size:** none; no entry.

- **VERDICT: [x] IN as a monitoring plan; no position.**

---
## SELF-AUDIT
- [x] Questions answered in order; Q1-Q4 each IN; Q5 opened only after all four; the file closes at Q5 on price.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. Q2's class rests on the subject's own ten-year series and
  the filed head-to-head with PepsiCo; the missing foreign peers were weighed and did not make the moat PROVISIONAL (reason at Q2).
- [x] No UNRESEARCHED or UNKNOWABLE verdict issued.
- [x] Step 0: filings read with accession numbers; FY2025 operating cash (7,408 / 6,805 / 11,599) cross-checked to the face and to
  companyfacts; the cover count cross-checked to the 10-Q balance sheet (7,040M issued less 2,737M treasury).
- [x] Owner earnings on multi-year means, three windows plus the TTM, both (c) ends, as filed and adjusted; every adjustment a
  disclosed judgment with its source; SBC resolves in 7 of 7 years and is subtracted in full.
- [x] Competitor row filled from five filers' filings plus the PEP run's KO/KDP research file (accessions given).
- [x] Sovereign from the US Treasury, dated 09/18/2026, for a USD-reporting, multi-currency earner (the judgment stated at Step 0).
- [x] Value stated as a round range ($40-70 a share); one windage place; no bar applied because the floor closed the question.
- [x] Price dated and flagged; corroborated by the issuer's own repurchase prices in three periods.
- [x] Committed: template `b3407b8`, Step 0 `124c685`, Q1 `54b462a`, Q2 `1c071ca`, Q3 `ed1abc5`, Q4 `d7edf5a`; Q5-Q6, this audit
  and the register in the next commit; the fold after.
- [x] Ledger ids: every id cited was checked against `principle_ledger.csv` before writing (`ledger_check.txt`); [E4-27] is used for
  incentives; the lollapalooza row is not cited for them (the resume note's seventh error).

**Corrections made before close (recorded so nothing is silent):**
1. **Q1 first carried a garbled parenthesis about Costa's goodwill**, written before the figure was read; replaced before the Q1 commit
   with the filed price (*"$ 4.9 billion of cash, net of cash acquired"*, FY2020 10-K Note 2). A draft had said $5.1bn from memory.
2. **Step 0 first described the 2024 8-Ks as "euro and dollar note issues" from their file names** (the resume note's error B: trusting
   a name not opened). All six were fetched and read before the Q2 commit; the amounts are now quoted from the filings.
3. **Q2 first compared sparkling's 69% share (2025) with 72% (2016)**; the FY2017 10-K changed the definition (sparkling soft drinks vs
   sparkling beverages) and restated 2016 to 69%. Corrected before the Q2 commit.
4. **Q4's first draft used a 60% gross margin for North America** in the named death; the segment note gives 51.8% (revenue $19,586M,
   cost of goods $9,438M). Corrected before the Q4 commit.

### THE BRIEF'S DEFECTS (recorded for the operator)
1. **The brief pointed the COKE lesson at the wrong line.** It asked how much of the fairlife contingent payment sat in operating vs
   financing cash, which was right; but the larger single item inside operating cash was the **$6.0bn IRS deposit of 2024**, which the
   brief named only as litigation. Both one-offs sit INSIDE operating cash (the reverse of COKE's financing-line royalty), and together
   they make the tool's as-filed owner earnings about $2bn a year low.
2. **"Any African or Indian bottler transactions"**: right, and there were more than the brief listed: the India 40% minority sale
   (booked in financing, $1.3bn), the Nigeria finished-goods sale, the Philippines, Vietnam and Thailand exits, and the sale of the whole
   Coca-Cola Consolidated stake. None is a live offer for KO; the Africa sale is the one pending.
3. **"Equity-method income may not arrive as cash"**: right in direction; the size is modest ($0.4-1.0bn a year undistributed against
   about $10bn of owner earnings), and it does not change the verdict at either end.
4. **The brief did not mention three operating-cash items** a TTM reader would take at face value: the receivables factoring programme
   ($14.7-21.9bn of receivables sold a year, lift unmeasurable), the pension-surplus transfers ($523M, $332M), and the tax-credit
   partnerships whose cost sits in investing. The TTM ($16.3bn of operating cash) would have reported a 3.6% yield.
5. **The brief's priors were otherwise right**: the perimeter straddle, the need for the PEP [E2-44] method, the proxy's [E4-27] read, and
   the warning that the famous past is not evidence. The hypothesis most likely wrong (that the franchise still clears) **was not
   refuted**: it cleared Q2 on the 2020s filings, and the file closed on price instead.

## REGISTER
- Verdict: **[x] IN on the business (Q1-Q4), quit on at the Q5 floor - FAIL ON PRICE.** [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Coca-Cola still has the franchise on its 2020s filings: in the US it raised prices about 49% in five years on level
  cases and grew segment profit 52% while PepsiCo's beverage volume fell; worldwide cases rose 15% in ten years; the operating income
  is earned on roughly $12-21bn of tangible capital. Owner earnings are about $10.0bn a year (adjusted five-year, capex end; range
  $7.8-11.4bn) once the $6.0bn IRS deposit (2024) and the $6.1bn fairlife milestone (2025) are taken out of operating cash. **At
  $88.25 (2026-09-18) x 4,302,549,243 shares (cover of 10-Q `0001628280-26-050503`) = $379.7bn, the yield is 2.6% against a 5.34%
  bond, the price needs 7.2% perpetual growth to reach the ~10% floor against a filed 4-6%, and the value at the floor is about
  $40-70 a share. FAIL at Q5.** Named death: stagnation (proposed #22 THE HABIT), with the tax case (about $20bn at worst) as a
  dated feature.
