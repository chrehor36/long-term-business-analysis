# Company Run: Energizer Holdings, Inc. (NYSE: ENR), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. Copied from `Test Runs/_TEMPLATE - Company Run.md` before any fetch. Working
folder: `Test Runs/_research 2026-10-05 ENR/` (filings as text, `fetch.py`, `value.py`, the run.py output, the slides).
Monetary figures are USD millions unless marked per share. The em dashes of the template's headings are replaced by
colons and hyphens (owner's standing rule; see the last section).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this run by the blind rule, so
whether the operator holds ENR is unknown to the analyst.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, the prepped reading list, any other ENR run file (none was found by a file-name search
of `Test Runs/` for "ENR" or "Energiz"; the search returned only a Jack Henry run file, whose name matched on "Henry", and
it was not opened), other companies' 2026-10-05 run or research files, and the gaps case of 2026-10-05. Seen without
opening: the session's git status lists untracked 2026-10-05 run files for ANDE, LCII and ROCK by name; the recent commit
subjects name OUT-at-Q2 verdicts for SLVM, LKQ, SCSC and KSS; the memory index says the register holds "57
gate-clearers, nothing buyable". None of these names ENR. The prior that many names close at Q2 was in view; it is
declared so that the reader can weigh the Q2 verdict below against it.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $21.24 (2026-10-05, aggregator live quote as printed by `tools/run.py`; flagged under operator rule 5).
- **Shares by class:** one class, common, par $.01. **68,483,637** outstanding at the close of business on 2026-07-31
  (10-Q cover, filed 2026-08-04, accession `0001632790-26-000076`). `python Screens/cover_shares.py ENR` returned "NO COVER
  SHARE COUNT PARSED", so the count was read from the cover by hand; it matches the dei count `tools/run.py` printed
  (68.484M). Diluted weighted shares in the June quarter: 69.2M (same 10-Q).
- **Market cap:** $1,454.6M at $21.24. Net debt at 2026-06-30: long-term debt including current maturities 3,327.3 plus
  notes payable 30.5 less cash 173.4 = **3,184.4** (10-Q, `0001632790-26-000076`). Enterprise value at the price: about
  4,639. The equity is under a third of the whole.
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve, dated
  10/02/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2025-11-18, `0001632790-25-000091`); 10-Q for the quarter to
  2026-06-30 (filed 2026-08-04, `0001632790-26-000076`); proxy DEF 14A (filed 2025-12-12, `0001632790-25-000120`); 8-K of
  2026-08-04 with Ex. 99.1 press release and Ex. 99.2 slides (`0001632790-26-000073`); 8-K of 2025-11-18 with the FY2025
  release and slides (`0001632790-25-000087`); 8-Ks of 2025-09-10 (`0001140361-25-034505`) and 2025-09-22
  (`0001140361-25-035737`, $400 of 6.000% senior notes due 2033). For the span: 10-Ks FY2015 (`0001632790-15-000044`),
  FY2017 (`0001632790-17-000087`), FY2019 (`0001632790-19-000080`), FY2021 (`0001632790-21-000128`), FY2022
  (`0001632790-22-000091`), FY2023 (`0001632790-23-000064`), FY2024 (`0001632790-24-000102`); the pre-spin Energizer
  10-K FY2014, filed under the CIK that is now Edgewell (`0001096752-14-000141`).
- **One figure cross-checked against the filed statement:** FY2025 net cash from operating activities **147.1**, capital
  expenditures **83.9**, share based compensation **25.6** and depreciation and amortization **126.7**, read in the filed
  cash-flow statement of the 10-K (`0001632790-25-000091`), equal to the XBRL lines `tools/run.py` used. The 10-Q balance
  sheet's long-term debt of 3,294.9 at 2026-06-30 equals its debt note (3,327.3 less 10.2 short-term less 22.2 fees).
- **`tools/run.py ENR` arithmetic lines only** (its v4 labels, its three-year "owner earnings" mean and its yields are not
  used as rules; Part VII). Owner cash after every real cost, computed by this run in `value.py` from the filed cash-flow
  lines as OCF less stock pay less all capital spending, with the depreciation variant beside it:

| FY (Sept) | OCF | stock pay | capex | D&A | owner cash (capex) | owner cash (D&A) |
|---|---|---|---|---|---|---|
| 2016 | 193.9 | 20.4 | 28.7 | 34.3 | 144.8 | 139.2 |
| 2017 | 197.2 | 24.3 | 25.2 | 50.2 | 147.7 | 122.7 |
| 2018 | 228.7 | 28.2 | 24.2 | 45.1 | 176.3 | 155.4 |
| 2019 | 149.5 | 27.1 | 55.1 | 92.8 | 67.3 | 29.6 |
| 2020 | 376.4 | 24.5 | 65.3 | 111.9 | 286.6 | 240.0 |
| 2021 | 179.7 | 10.2 | 64.9 | 118.5 | 104.6 | 51.0 |
| 2022 | 1.0 | 13.2 | 77.8 | 121.6 | -90.0 | -133.8 |
| 2023 | 395.2 | 21.8 | 56.8 | 122.7 | 316.6 | 250.7 |
| 2024 | 429.6 | 23.1 | 97.9 | 120.5 | 308.6 | 286.0 |
| 2025 | 147.1 | 25.6 | 83.9 | 126.7 | 37.6 | -5.2 |

  Five-year mean FY2021-2025: **135.5** (capex basis), 89.7 (D&A basis). Prior five years FY2016-2020: 164.5. Ten-year
  mean: 150.0. Twelve months to 2026-06-30: OCF 217.5, stock pay 26.3, capex 66.9, owner cash **124.3**. Capex before FY2020
  is the filed "PaymentsToAcquireProductiveAssets" line; finance-lease principal (0.3 to 1.2 a year) and taxes paid on
  withheld share awards (8.1 in nine months of FY2026) are not deducted, which flatters the figure slightly. Interest is
  already paid inside OCF, so these are cash figures for the equity. FY2025 OCF excludes **120.9** of Section 45X
  production credits accrued but not yet collected (10-K cash-flow line "Production tax credits (120.9)"), and FY2022 OCF
  of 1.0 carries an inventory build in the cost inflation; both years are abnormal (see the whole-cycle variant below).

**The balance sheets, ten year-ends, read before the income account** (the rule asks for "balance
sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**; the file closes at Q2, so
the reading is done here, as the brief directs). First-filed XBRL as printed by `tools/run.py`; FY2025 checked against the
filed statement (total assets 4,556.7, equity 169.9 in the 10-Q's September column):

| Sept 30 | assets | equity | cash | receivables | inventory | goodwill | intangibles | LT debt | retained |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,732 | -30 | 287 | 191 | 289 | 230 | 235 | 982 | 71 |
| 2017 | 1,824 | 85 | 378 | 230 | 317 | 230 | 224 | 978 | 199 |
| 2018 | 3,179 | 24 | 522 | 230 | 323 | 244 | 233 | 976 | 177 |
| 2019 | 5,450 | 544 | 258 | 340 | 469 | 1,005 | 1,959 | 3,462 | 130 |
| 2020 | 5,728 | 309 | 460 | 292 | 511 | 1,016 | 1,909 | 3,307 | -66 |
| 2021 | 5,008 | 356 | 239 | 293 | 728 | 1,054 | 1,871 | 3,333 | -5 |
| 2022 | 4,572 | 131 | 205 | 422 | 772 | 1,003 | 1,296 | 3,499 | -305 |
| 2023 | 4,510 | 211 | 223 | 512 | 650 | 1,016 | 1,238 | 3,332 | -165 |
| 2024 | 4,342 | 136 | 217 | 441 | 657 | 1,046 | 1,071 | 3,193 | -128 |
| 2025 | 4,557 | 170 | 236 | 404 | 781 | 1,051 | 1,006 | 3,408 | 87 |

What moved, and why, from the filings:
- **Born with debt and no equity.** At the spin from Edgewell (July 2015) Edgewell received "a $1,000.0 cash distribution
  which was funded through the incurrence of long-term debt by Energizer" (10-K FY2015, `0001632790-15-000044`). Equity
  was negative (-30) at the first year-end shown.
- **The 2019 purchase, bought with debt.** Spectrum's batteries (Rayovac, Varta) for **1,962.4** cash and Spectrum's auto
  care (Armor All, STP, A/C Pro) for **938.7** cash plus 5.3M shares valued at **240.5** (10-K FY2019,
  `0001632790-19-000080`), financed by term loans and notes and by 205.3 of new common and 199.5 of mandatory convertible
  preferred. Long-term debt went from 976 to 3,462; goodwill and intangibles from 477 to 2,964. Diluted shares went from
  61.4M (FY2018) to a high of 72.7M (FY2024) and back to 68.5M.
- **The purchase written down.** Impairments of **541.9** in FY2022 (Armor All trade name 370.4, STP 26.3, Rayovac 127.8,
  goodwill 17.4; 10-K FY2022, `0001632790-22-000091`) and **110.6** in FY2024 (Rayovac 85.2, Varta 25.4, "driven by missed
  branded sales forecasts"; 10-K FY2025). After the June 2026 quarter the Rayovac trade name, book 337.0, was moved from an
  indefinite to a 30-year life "Based on decreases in forecasted demand, increased competition and other economic factors"
  (10-Q, `0001632790-26-000076`). About 652 of trade names and goodwill written off against roughly 3,141 paid.
- **Retained earnings at zero after ten years.** 71 (2016) to 87 (2025): the decade's earnings went out in dividends
  (62.7 to 87.4 a year from FY2016) and buybacks (437.3 over FY2016-2025 by the filed lines) or were lost to impairments.
  Tangible equity at 2025-09-30: 170 less 1,051 less 1,006 = **-1,887**.
- **Inventory against sales.** 289 on sales of 1,634 (17.7%) in FY2016; 781 on 2,953 (26.4%) in FY2025; 748 at
  2026-06-30. The filer gives the reasons (cost inflation in FY2022, the APS acquisition, network rebalancing and tariffs
  in FY2025), but the ratio rose by half over the span, which is the line the rows say to "look twice" at when
  "inventories look out of line, you know, with sales" **[M1995-064]**. Receivables went from 11.7% to 13.7% of sales.
- **Debt held at about 3.3 to 3.5 billion for seven years.** Maturities at 2026-06-30: 592.3 within two years (the 4.750%
  notes of 2028), 1,542.1 in the third year (the 4.375% and 3.50% euro notes of 2029), 1,118.4 after (the term loan of
  2032 and the 6.00% notes of 2033) (10-Q debt note). The weighted coupon of the 2028-2029 notes is about 4.17%; the
  filer's own most recent note, September 2025, priced at 6.000%.

What they cannot say: the share of the Energizer and Rayovac brands against Duracell and private label. No 10-K read
states it (sweep of the FY2015, 2017, 2019, 2021 and 2025 10-Ks for "market share", "share of", "number one/two",
"Duracell", "private label": share appears only in risk-factor form); the pre-spin FY2014 10-K is the last to give a
figure (below, Q2).

## THE FOUNDATIONS (not a gate)
The test that bears hardest here is the first: "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**. For this name the closed market is not the risk; a closed credit market is, because 2,134 of debt falls due
inside three years. The market's quote "just tells us prices." **[M2006-077]**, and the quote here sits on equity worth under a
third of the enterprise, so an error of 10% in the value of the whole business is an error of about 32% in the equity. The
filer's releases lead with adjusted earnings per share and adjusted EBITDA, and the proxy pays on them, so the habit of
asking who is paid to tell you applies to the company's own framing. The habit used throughout: look for "what you’re
missing" **[M2025-013]** and write the contrary evidence down at once.

**Contrary evidence, written down as found**, the habit being to "write it down in the first 30 minutes" **[M1997-127]**. Against the business: price rises of FY2022-2023 lost
volume and were then given back in "planned strategic pricing and promotional investments" (FY2024, FY2025) and "increased
promotional investment" (FY2026 Q3); both acquired brand families impaired; Rayovac's demand forecast cut and competition
said to be rising (June 2026); B&L segment profit flat in nominal dollars for five years; Walmart between 10.4% and 14.2% of
sales in every year FY2016-2025 and a 2023 antitrust class action naming Energizer and Walmart; FY2026 first-half organic sales -4.9%;
2,134 of debt due within three years at coupons well under today's long rate; pay tied to adjusted EBITDA, which by the
filer's definition excludes share based payments and restructuring. Against my own OUT reading, found as I went: the
category has lasted and the filer expects category volume "flat to slightly positive" over the long term; organic sales
over FY2016-2025 grew in most years and volume held over the decade as a whole; Batteries & Lights earns about 23% on its
sales; the filer's Circana chart shows Energizer's US volume ahead of the category from January to June 2026; it claims the
number one share in US specialty (coin) batteries; Duracell, in the same category, is described by Buffett as "a very good
business" (below, Q2).

## THE STANDING RULE
Buying ENR shares for cash, at any size the buyer can lose entirely without needing the money, puts no ruin on the buyer:
"We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. The rule
forbids financing the purchase: "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own
leverage is Q9's question (NOT REACHED), but it bears on sizing: equity this thin can go to a fraction of its price on a
modest fall in the business.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, and the first step is "trying to identify the key variables in that
  particular business, and evaluating how predictable they were first" **[M1998-044]**.
- **The key variables, from the filings.** (1) Primary battery unit volume: the filer has called the category's long-term
  volume "flat to slightly positive" while warning that built-in rechargeables can lead to a "declining volume trend"
  (10-K FY2025 risk factors); the same warning has stood in every 10-K read since FY2014. (2) Price and mix against Duracell
  above and private label and price brands below. (3) Retailer terms: Walmart 12.8% of FY2025 sales. (4) Input costs (zinc,
  manganese dioxide, steel, lithium), tariffs and currency (about 40% of sales outside the US). (5) Two policy items: the
  Section 45X production credits (available for calendar 2023 to 2032, phasing out from 2030; 10-Q) and the IEEPA tariff
  refund (64.1 credited to cost of sales in nine months of FY2026). (6) Auto Care (620.0 of 2,952.7 sales in FY2025):
  car parc, miles driven, weather.
- **Are they foreseeable?** The product and its uses change slowly; the industry's insiders write the forecast down (the
  filer prints a category outlook every year). The rows on the leader of this very category state the ten-year shape: "the
  battery business will be a declining business, but it will be around for a very, very, very long time on a worldwide
  basis" **[M2015-066]**. The statements do tell the future ones in outline: "the financial statements will tell me the
  information that’s useful to me in making a judgment about what the future financial statements are going to look like"
  **[M2008-033]** holds here, with the adjusted measures stripped off. The policy items are noise of a size (45X about 42
  a year) that can be bracketed, not a fast-changing technology.
- **Routing.** Not a business whose economics are put out of reach by fast change; not a bank; not a holding company.
- **VERDICT: IN.** The economics can be pictured ten years out in outline: a slowly shrinking or flat unit category, two
  large brands, retailers with growing power. Whether the picture is good is Q2's question, since understanding comes first
  and "we can’t make a decision as to whether it has a sustainable edge" **[M1997-148]** without it.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**. The castle the filer describes is a branded
battery franchise with a second, value brand (Rayovac) and an auto care portfolio, sold mostly through mass retailers. The
tests, each with its filing fact:

- **Pricing power, and the agony before a rise.** "you can almost measure the strength of a business over time by the
  agony they go through in determining whether a price increase can be sustained" **[M2005-020]**; the companion question,
  "if we raised the price 10 cents a pound, would sales fall off a cliff?" **[M2005-019]**. The filer's organic sales
  bridges (10-Ks FY2022, FY2023, FY2025): FY2022 pricing +7.6%, volume -5.3%; FY2023 pricing +7.5%, volume -7.5% "due to
  lower category volumes across both battery and auto care from higher retail pricing" and a further -1.0%; FY2024 pricing
  **-2.2%** "driven by planned strategic pricing and promotional investments" with Batteries & Lights volume still -0.7%;
  FY2025 pricing **-0.8%** for the same reason, volume +1.5%; FY2026 Q3 adjusted gross margin down "by unfavorable product
  mix and increased promotional investment" (10-Q). The price taken in the cost inflation lost about 13.8% of volume over
  two years and was then partly handed back over the next three. That is the agony the row measures, and the opposite of
  "Anytime you can charge more for a product and maintain or increase market share against wellentrenched, well-known
  competitors, you have something very special in people’s minds." **[M2000-031]**. Before the inflation the filer's price
  gains were small (about 2% FY2017, 1.5% FY2018, 0.9% FY2019, 0.8% FY2021).
- **Gross margin through the 2021-2023 cost inflation, whole span.** Filed gross profit over net sales: 43.6% (FY2016),
  46.2% (FY2017), 46.2% (FY2018), 40.2% (FY2019, Spectrum mix enters), 39.4% (FY2020), 38.4% (FY2021), 36.7% (FY2022),
  38.0% (FY2023), 38.3% (FY2024), 41.7% (FY2025, which includes 78.5 of FY2023-24 credits and 41.6 of FY2025 credits;
  the filer's adjusted 40.9% includes the FY2025 credits, about 1.4 points). Nine months of FY2026: adjusted 39.2% against
  41.9%, and that after a 64.1 IEEPA refund credit. The 46% years are pre-Spectrum mix and are not like for like; the
  post-2019 years are, and they have not regained FY2019-2020 levels without the government credits.
- **Unit volume and share of mind, against Duracell and private label, over the span.** The last share figure the
  filer gave: "We estimate Energizer and The Procter & Gamble Company collectively represent approximately 65% share in the
  markets in which we compete" (pre-spin 10-K FY2014, `0001096752-14-000141`). Since then the filer gives none. Duracell,
  from Berkshire's own 10-Ks, "a 32% market share of the global alkaline battery market in 2025" and the series:
  approximately 37% (FY2016, `0001193125-17-056969`), 36% (FY2017, `0001193125-18-057033`), 34% (FY2018,
  `0001193125-19-048926`), 32% (FY2019, `0001564590-20-005874`), 31% (FY2020, `0001564590-21-009611`), 29% (FY2021,
  `0001564590-22-007322`), 29% (FY2022, `0000950170-23-004451`), 31% (FY2023, `0000950170-24-019719`), 32% (FY2024,
  `0000950170-25-025210`), 32% (FY2025, `0001193125-26-083899`). The leader lost about eight points to 2021-2022 and won
  three back to 2025, while Energizer was cutting price to hold volume; where Energizer's share went over the decade, the
  public record read does not say. The rows ask for "share of mind" **[M1997-099]**; the nearest filed evidence is volume,
  and Energizer's own legacy volume fell 6.8% in FY2014 after "the loss of distribution within two U.S. retail customers"
  (10-K FY2015) and fell again in FY2022-2023 on price.
- **The low-cost position.** The rows put it as "commodity businesses have risk unless you’re the low-cost producer"
  **[M1997-010]**. The filer does not claim it, and its risk factors say the opposite in its own words: "Our competitors may
  have lower production, sales and distribution costs, and higher profit margins" and "Certain of our competitors have
  substantially greater financial, marketing, research and development, and other resources and greater market share in
  certain segments than we do" (10-K FY2025). Spectrum's own 10-K said it "manufactures alkaline batteries for third
  parties who sell under their own private labels" (SPB 10-K FY2017, `0000109177-17-000080`), so the value tier Energizer
  bought was partly the private-label supply it now competes against. No filing read shows Energizer as the low-cost
  producer.
- **The brand in the customer's mind, and the retailer.** Against the retailer, "the brand has to stand for something in
  the consumer’s mind" **[M2015-038]**; where shoppers trust the store as much as the brand, "then the value of having the
  brand moves over to the retailer from the product itself" **[M2001-090]**. Filing facts:
  Walmart was 13.3% of sales (FY2013), 8.5% (FY2014, the year distribution was lost), then 10.0%, 10.4%, 12.1%, 11.5%,
  13.8%, 14.1%, 13.7%, 12.9%, 14.2%, 13.2% and 12.8% (FY2015 to FY2025, the 10-Ks' customer notes); Berkshire's 10-K for
  FY2016 says "Costco and Walmart are significant customers, each representing 10% of Duracell’s annual revenue"; the
  filer names "club stores, grocery, dollar stores, mass merchandisers and internet-based retailers, which may offer
  private label brands that are typically sold at lower prices" (10-K FY2025). The rows read the retail system as having
  "gained in power relative to brands" **[M2019-014]**, and "the brand is our protection against the intermediaries making
  all the money" **[M2019-041]**. The value brand bought to protect the low end is the brand being written down.
- **Would the customer still choose it over the low bid?** See's passed because "it wouldn’t be a question of people
  buying candy for the low bid" **[M2017-009]**. The filer's own risk factor names "a shift of purchasing patterns to lower
  cost options such as “private label” brands sold by retail chains or price brands" (10-K FY2025), and its FY2023 volume
  loss came "from higher retail pricing". The rows doubt the money to be made "with a product that has a whole bunch of
  competitors" **[M2023-074]**.
- **The attacker with money.** "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The attackers are
  already inside: Duracell, owned by Berkshire since February 2016, holds the larger global alkaline share, and the
  retailers' own labels sit beside both on the shelf. "one competitor is frequently enough to ruin a business" **[M2012-108]**.
- **Ask the competitors.** Not done (no access); the filings of the two named competitors were read instead (row below).
- **Widening or narrowing.** The rows ask "whether it’s likely to widen further or shrink on you" **[M1999-108]**, and put
  it first: "could the competitive advantage have been made stronger and more durable" **[M2000-075]**. Batteries & Lights
  segment profit (10-Ks FY2022 and FY2025): 512.6 (FY2020), 553.6 (FY2021), 553.6 (FY2022), 551.5 (FY2023), 554.8 (FY2024),
  **542.2** (FY2025). The FY2025 figure includes the FY2025 production credits of 41.6, which the segment measure does not
  exclude (the 10-Q attributes the FY2026 B&L decline in part to "out of period production credits recorded in the prior
  year"); before them B&L earned about 500.6, against 553.6 in FY2021, on sales of 2,332.7 against 2,402.8, and FY2025 sales
  include 63.6 from the APS purchase. In the nine months to June 2026, B&L organic segment profit fell 6.9% "due to the
  decline in organic Net sales discussed above, higher input costs and unfavorable product mix" (10-Q; the June quarter's
  -16.1% is mostly the prior year's out-of-period credits and is not used). Auto Care: 98.2 (FY2021), 46.5 (FY2022), 75.0, 94.1, 105.6, with Armor All and STP written down by 396.7
  in FY2022 on "declines in their respective Auto Care category projections". Narrowing, on the filer's numbers.
- **What could destroy, modify or reduce it.** The rows ask what will "destroy, or modify, or reduce the economic
  strengths" **[M2000-014]**: built-in rechargeables (named in every 10-K since FY2014), private label and the online and
  discount channels (named in the FY2025 risk factors), a Walmart decision on shelf space, and the expiry of the 45X credits
  that now hold up the margin. The filer itself names the first two as the causes when it cut Rayovac's life: "decreases in
  forecasted demand, increased competition".

**The competitor row** (same metric where the competitors file it):

| Name | Metric | Span and figures | Source |
|---|---|---|---|
| Energizer (ENR) | organic price and volume, segment profit | price +7.6% / +7.5% (FY22, FY23), -2.2% / -0.8% (FY24, FY25); volume -5.3% / -8.5% then -0.7% B&L / +1.5%; B&L segment profit 553.6 (FY21) to 542.2 (FY25, incl. 41.6 credits) | 10-Ks `0001632790-22-000091`, `-23-000064`, `-25-000091` |
| Duracell (inside Berkshire) | global alkaline share, Duracell's own estimate | ~37% FY2016 falling to 29% FY2021-22, back to 32% FY2024-25; Costco and Walmart each 10% of revenue (FY2016); 2025 pre-tax earnings show "lower gross margins and higher selling, general and administrative expenses as a percentage of revenues" before its own 45X credits | Berkshire 10-Ks, accessions in the share bullet above |
| Spectrum Brands (SPB), batteries to 2018 | consumer battery net sales | 865.6 in FY2017, +3.0% (FY2016 organic +6.2%, partly "new private label customers" in EMEA); Rayovac and Varta, plus private-label alkaline for third parties | SPB 10-K FY2017 `0000109177-17-000080` |
| Panasonic | | not obtained: not an SEC filer; flagged, not used | |
| Private label (Amazon Basics, Kirkland) | | no filed figures; named only generically in ENR's risk factors; no instance found in the filings read of a share or price figure for either | |

The leader's own owner says of Duracell in 2018, "But it is not earning an appropriate amount now, based on the history of
the company." **[M2018-033]**, while holding that "the brand is strong. Very strong." **[M2018-033]**; and of the
category, Duracell "has a very strong position" **[M2015-066]**. These rows are evidence about the category and the
leader, not about the second brand: the leader is the one whose share the owner can see, and the leader's earnings were
themselves below their history.

**Weighing the castle.** For it: a two-brand franchise that has stood for decades, B&L earning about 23% on sales, a
category that will last, and volume roughly held across the decade. Against it, on the filer's own evidence: the price test
failed both ways (volume lost on the rise, price given back after it); the company is the second brand and does not claim
low cost while saying rivals may have lower costs and larger share; the retailer is growing in power and carries its own
label; the value brand bought in 2019 has been written down twice and in 2026 is said by the filer to face "decreases in
forecasted demand, increased competition"; the auto care brands were written down by 396.7 on category declines; and
battery segment profit, before government credits that end by 2032, is lower in nominal dollars than in FY2021. The rows'
rule for such a business: "If you really think a business is declining, most of the time you should avoid it."
**[M2012-062]**, and a low price does not cure it: "What you can’t do is turn any investment into a good deal by paying
little" **[M2019-015]**.

Is this a castle "shown open" (OUT) or one "whose future cannot be judged" (TOO HARD)? The moat is narrowing on the
evidence, not merely tenuous in the abstract: the filer has reported the filling in, in its price bridges, its segment
profit, three impairment events and the Rayovac reclassification. The one question the public record does not answer is
Energizer's share against Duracell and private label over the decade; it is knowable in principle (scanner data) but not
on the public record read, and the remaining answers all point one way. The framework sends a castle shown on the evidence
to be filling in to OUT (Q2, Why it is a STOP). The alternative reading, TOO HARD because "when we see a moat that’s tenuous in any way" the
speakers "leave it alone" **[M2000-019]**, is recorded below as an unclear point in the framework; on this file the evidence
is of narrowing, not of mere uncertainty.

- **VERDICT: OUT.** "We’ve got three boxes at the company: in, out, and too hard." **[M2006-013]**. The castle is shown on
  the filer's own figures to be narrowing: pricing given back after the inflation, the acquired value brand losing demand
  to competition, segment profit before subsidies below FY2021, and the leader and the retailers holding the stronger
  positions.

---
## COMPUTATION - NOT A CLEARANCE
*Reported at the owner's request. The file closed OUT at Q2; nothing in this section is a clearance, carries entry
language, or reopens Q2 (operator rule 3). Built by the Q7 CONVENTION of Part VI as written, with the run's own choices
confessed.*

**Inputs.** Owner cash after every real cost, "a figure calculated after interest, taxes, depreciation, amortization and
all forms of compensation" **[L2021-003]**, five-year mean FY2021-2025 = **135.5** (capex basis; the D&A variant is 89.7).
Rate: the long government bond, as the rows name it: "What is the risk-free interest rate (which we consider to be the yield
on long-term U.S. bonds)?" **[L2000-021]**, **5.63%**. Ten years at the growth shown, then zero nominal growth. The range,
not a point: "working with a range of possibilities is the better approach" **[L2000-024]**.

**The growth shown.** The convention measures it on aggregate owner cash over the window. Inside FY2021-2025 owner cash
runs 104.6, -90.0, 316.6, 308.6, 37.6; an endpoint rate on that series is meaningless, as the rows warn of a base year
"aberrational" **[L2005-003]**. CONVENTION of this run: the growth shown is the change between the two five-year means,
164.5 (FY2016-2020) to 135.5 (FY2021-2025), **-3.81% a year** on aggregate owner cash. Rationale: the only measure on
the aggregate series that no single year sets; it is also consistent with sales (3,021.5 in FY2021 to 2,952.7 in FY2025,
with 63.6 bought in).

**(a) VALUE RANGE** (per share on 68.48M shares; `value.py`):
- Base, five-year mean 135.5: shown-growth case **1,782 = $26.03**; no-growth case **2,406 = $35.14**. Range **$26.03 to
  $35.14** against **$21.24**; the width is 1.35 to one, so the range is narrow enough to read. The price is 18% below the
  bottom.
- **Whole-cycle variant** (the five-year window holds two abnormal years, FY2022 with OCF of 1.0 on an inventory build and
  FY2025 with 120.9 of credits accrued but not collected): ten-year mean 150.0 gives **$28.82 to $38.91**. Crude, because
  the FY2016-2018 business was smaller and paid about a third of today's interest.
- Variants beside it, CONVENTION of this run, each from a filed figure: (i) the 45X credits earned in the window counted
  when earned (120.9 over five years, +24.2 a year): **$30.67 to $41.41**, which overstates value because the credits phase
  out from 2030 and end after 2032 (10-Q); (ii) **refinancing**: the 2028-2029 notes (2,117.2 at a weighted 4.17%)
  refinanced at the 6.000% the filer paid in September 2025 add 38.7 of interest, 30.3 after tax at the mean of the three
  filed effective rates (20.0%, 29.2%, 15.9%; 21.7%), leaving owner cash of 105.2: **$20.20 to $27.28**; (iii) twelve months
  to June 2026, 124.3: $23.88 to $32.24.

**(b) FAIR PRICE.** The price at or below which the central case clears the floor of about 10% pre-tax, the speakers'
figure (they would "sit on the sidelines" without "a very high probability of at least 10% pre-tax returns" **[L2002-020]**),
which they call a line where "there’s just a point at which we drop out of the game. And it’s arbitrary." **[M2003-149]**.
Tax treatment: owner cash is after cash taxes; it is grossed up to pre-tax by dividing by (1 - 21.7%), the mean of the
three filed GAAP effective rates FY2023-2025, and the pre-tax stream is discounted at 10%. Central case = the mean of the
two ends' prices. **Fair price about $22.43** (base; no-growth end $25.27, shown-growth end $19.60). Whole-cycle variant
$24.84; refinancing variant **$17.41**. At $21.24 the price sits about 5% under the base fair price and above the fair price
once the 2028-2029 refinancing is priced at the filer's own latest coupon: a case that needs a pencil, which the rows put
as "It should scream at you." **[M2009-005]**.

**(c) CHEAP PRICE.** CONVENTION of this run: half the bottom of the base range, **about $13.01** (refinancing variant
$10.10; whole-cycle $14.41). Rationale: the rows' screamer is "I didn’t need to know whether it was worth 97 billion or 103
billion if I was buying it at 35 billion." **[M2008-068]**, a price near a third of value; half is used, not a third,
because the range here is narrow, but the margin must be wide because the equity is thin, "the more volatile the business
is [...] the larger the margin of safety" **[M1997-080]**: at the price, 10% of enterprise value (about 464) is 32% of the
market value of the equity. The discount is taken from "the bottom boundary of our estimate" **[L2013-012]** and as "a big
discount from that present value calculated using the risk-free interest rate" **[M1997-126]**.

Recorded, not weighed (Q6 NOT REACHED): the FY2025 buyback of 4M shares at an average $22.42 (8-K slides,
`0001632790-25-000087`) sits below the bottom of the base range; it was paid for in the year owner cash was 37.6 and the
company issued $400 of 6.000% notes.

---
## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2). Recorded only: on tangible operating capital the battery business earns high returns (segment
profit near 650 against PP&E of 403 and inventory of 781), while on the 3,141 paid in 2019 the added capital earned little,
as the impairments say.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The ten-year balance-sheet reading is in Step 0. Recorded for the next reader: the releases lead
with adjusted EPS and adjusted EBITDA (the slides' FY2026 outlook gives "Adjusted EBITDA $580M - $610M"), and the rows say
the count of companies bought "where people are talking about EBITDA, is going to be about zero" **[M2002-026]**; adjusted
EBITDA by the filer's definition "further excludes ... share based payments" (slides, `0001632790-25-000087`), the item the
rows name when "it has become common for managers to tell their owners to ignore certain expense items that are all too
real" **[L2015-003]**; restructuring has been excluded in every year since FY2019 (integration costs 68.0 and 68.9 in
FY2020-2021, Project Momentum 29.9 to 62.9 of cost of sales a year FY2023-2025 and continuing into FY2026); the rows say
that telling owners year after year to set aside such costs "when management is simply making business adjustments that
are necessary, is misleading" **[L2016-007]**.
Two tells sit on the list (adjusted figures featured; inventory rising against sales); whether they amount to suspicion was
not decided, because Q4 was not reached.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. Recorded: CEO Mark LaVigne, fiscal 2025 total compensation of $11 million by the proxy's summary; the annual
bonus pays one third each on adjusted net sales, adjusted EBITDA and adjusted gross margin rate, and the long-term units vest
on cumulative adjusted EPS and relative TSR against the Russell 2000 Consumer Staples Index (DEF 14A, `0001632790-25-000120`).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Recorded: dividends of 62.7 to 87.4 a year since FY2016 against a five-year owner-cash mean of 135.5; in
FY2025, dividends 87.1 plus buybacks 89.7 against owner cash of 37.6; the FY2026 slides call debt reduction "the
highest-impact use of cash today".

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED. The arithmetic the owner asked for is in the COMPUTATION section above and is not a Q7 answer.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Recorded for the next reader: 2,134 of debt due in fiscal 2028-2029 (10-Q maturity table); the rows warn that
"Companies with large debts often assume that these obligations can be refinanced as they mature." **[L2010-020]**; and
"you can’t talk about debt levels without relating it to the ability to pay debt" **[M1995-104]**: interest of 154.3 in
FY2025 against total segment profit of 647.8 before corporate costs of about 100.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Nothing found in the filings read that falls in the named businesses.

---
## THE BOX
**OUT at Q2.** The castle is shown on the filer's own figures to be narrowing: the 2022-2023 price rises lost volume and
were partly handed back in three years of "planned strategic pricing and promotional investments"; Energizer is the
second brand behind a leader with 32% of global alkaline (Berkshire's 10-K) and does not claim low cost; the Rayovac value
brand bought in 2019 was written down in FY2022 and FY2024 and in 2026 put on a 30-year life for "decreases in forecasted
demand, increased competition"; Batteries & Lights segment profit before the 45X credits (about 500.6 in FY2025) is below
FY2021's 553.6. Not a TOO HARD: the question is answered against the business on the evidence. For the record only
(COMPUTATION, not a clearance): base range **$26.03 to $35.14**, whole-cycle **$28.82 to $38.91**, refinancing variant
**$20.20 to $27.28**, fair price about **$22.43** (refinancing variant $17.41), cheap price about **$13.01**, against a
price of **$21.24**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Not committed after each question: the
      brief for this run forbids commits; the file was written in one sitting after the reading.*
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession; no
      number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q2 failed and closed the run; nothing after it is a clearance (the reporting section is headed
      COMPUTATION and carries no entry language).
- [x] Owner cash after every real cost (OCF less stock pay less all capex), never a net-income proxy; the sovereign from
      the US Treasury; the price is an aggregator quote and is flagged.
- [x] Contrary evidence was written down as it was found ("write it down in the first 30 minutes" **[M1997-127]**), both against the business and against the
      verdict.
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (its v4 owner-earnings label, its three-year mean and its
      yields were not used as rules).
- [x] `python tools/check_framework.py` PASS before the file was left (no commit, per the brief).
- Not done: competitor interviews; Panasonic (non-SEC); any share figure for Energizer after FY2014; private-label
  figures for Amazon Basics or Kirkland; reading the earnings slides' images beyond the one volume chart (slide 8 of the
  Q3 FY2026 deck, which shows only twelve months of tracked US channels).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **OUT or TOO HARD at Q2 for a castle that still stands in nominal terms but is narrowing.** Q2 sends "a castle shown
on the evidence to be filling in" to OUT and the tenuous moat, by M2000-019's own reason, to TOO HARD; it draws no line
between them. ENR is both: nominal segment profit is flat (standing), real and pre-subsidy profit is lower and the filer
itself reports rising competition (filling in), and the one figure that would settle it, share against Duracell and
private label over the decade, is not on the public record read. I closed OUT because every answer that the record does
give points one way, using rule (c) of the research-pass form by analogy (an unanswerable question is recorded and the
close is decided on the rest); a second analyst could close TOO HARD (WORK) on the share question, and the framework would
not say which is right. A sentence in Q2 saying how many filed signs of narrowing make "shown" would help. (2) **The Q7
growth input on aggregate owner cash** is unworkable when owner cash swings from -90.0 to 316.6 inside the window; I used
the change between two five-year means and confessed it. (3) **Government production credits** (Section 45X, about 42 a
year now, ending after 2032) are not addressed anywhere: whether a statutory subsidy with an end date is "owner cash" for a
ten-year carry, and whether it belongs in the castle (Duracell receives the same credit, Berkshire's 10-K FY2025). I kept it
out of the base and showed it as a variant. (4) **Refinancing at today's rate**: the convention discounts after-interest
cash at the sovereign but says nothing about known debt maturities whose coupons are far below today's long rate; for a
levered name the difference (here about 30 a year, a fifth of owner cash) moves the fair price below the market price.
(5) **Em dashes**: the operator protocol's required heading for pre-clearance arithmetic and the template's headings are written with
em dashes, which the owner's standing rule forbids; I used a hyphen and colons. (6) `Screens/cover_shares.py` failed to
parse ENR's 10-Q cover; the count was read by hand.
