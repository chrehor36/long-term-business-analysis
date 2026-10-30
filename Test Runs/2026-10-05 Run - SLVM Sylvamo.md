# Company Run: Sylvamo Corporation (NYSE: SLVM), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Filled top to
bottom from `Test Runs/_TEMPLATE - Company Run.md`; every judgment cites a v5 ledger id in bold; every filing fact carries
its accession; the STOP that returned OUT (Q2) closed the run and later questions are marked NOT REACHED. Working folder:
`Test Runs/_research 2026-10-05 SLVM/` (filings as text, `fetch.py`, `calc.py`, `lookup.py`, competitor filings in `peers/`).

**POSITION NOTE, declared before any verdict:** not checked. The template says to check `PORTFOLIO.md`; the blind rule of
this run forbids opening it, so whether the operator holds SLVM is unknown to this analyst.

**CONTAMINATION, declared:** (1) a directory listing showed the file name `2026-07-16 Run - Industrials & Misc 9-pack (LKQ
SLVM GPK UFPI FBIN EMN AMPH IIPR VSNT).md`, a pre-v4.1 run that includes SLVM; only the name was seen, the file was not
opened, and no verdict from it is known to me. (2) The session's git snapshot showed recent commit subjects for the AMR,
MBC and ADNT runs of 2026-10-05, including their boxes and their "fair" and "cheap" figures (in two of them the cheap price
is half the fair price). (3) The same listing showed file names of other 2026-10-05 runs, holding reviews and research
passes (names only). (4) A `grep -l` for the computation heading's spelling returned three other 2026-10-05 run file names
(names only, no text read). The cheap-price rule below was chosen for its own reason and is stated as such; the half-fair
figure is shown beside it only as an alternate and is named as the pattern seen in (2).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $33.31 (2026-10-05, from `python tools/run.py SLVM`; aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 39,760,243 common, single class, as of 2026-07-31 (10-Q for the
  period ended 2026-06-30, filed 2026-08-07, accession `0001856485-26-000034`; `python Screens/cover_shares.py SLVM`).
  The 10-K cover gave 39,508,287 as of 2026-02-13 (`0001856485-26-000008`).
- **Market cap:** $1,324M (33.31 x 39.760M).
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 2026-10-02 (as printed
  by `tools/run.py` from the issuing authority). Earnings are reported in USD; about half of sales are in BRL and EUR.
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-20, `0001856485-26-000008`): Items 1, 1A, 2, 5, 7, the
  balance sheet, cash-flow statement, segment note, tax and contingency notes. 10-Q Q2 2026 (filed 2026-08-07,
  `0001856485-26-000034`): MD&A, balance sheet, notes 10, 11, 12. 10-Ks FY2021 (`0001856485-22-000010`), FY2022
  (`0001856485-23-000007`), FY2023 (`0001856485-24-000008`), FY2024 (`0001856485-25-000008`): cash-flow statements and
  segment notes. Form 10/A information statement, exhibit 99.1 (filed 2021-08-23, `0001193125-21-253977`): business, cost
  position, selected data 2018 to 2020. Proxy DEF 14A 2026 (`0001193125-26-138839`) fetched; not read beyond the fetch,
  since the file closed before Q5. 8-Ks read: 2024-10-31 (`0001193125-24-248167`, Georgetown offtake terminated),
  2025-08-22 (`0001193125-25-185647`, a director's resignation), 2025-10-29 (`0001193125-25-254570`, Riverdale offtake
  wind-down and the Brazil Payment Agreement amendment), 2025-11-10 (`0001193125-25-274343`, a shareholder rights plan).
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025 $268M on the
  filed consolidated statement of cash flows (10-K FY2025) equals the XBRL value and `tools/run.py`'s OCF line; total
  equity $966M at 2025-12-31 on the filed balance sheet equals the XBRL value.
- **`tools/run.py` arithmetic lines checked against the filings.** Its OCF, SBC, capex and D&A for 2023 to 2025 match the
  filed statements. Its five-year window (2021 to 2025) uses OCF as filed in the FY2021 10-K, which still contained the
  Russian operations (OCF 2021 $549M); the continuing-operations figure in the FY2022 10-K is $423M, and its capex tag is
  absent for years before 2021. The table below is rebuilt from the filed statements, continuing operations only. Its
  "retained" column is the filed retained earnings, but equity also carries an accumulated other comprehensive loss of
  $1,353M (mostly currency translation), which the column does not show. Nothing it printed as a rule, id or verdict is used
  (Part VII).

**Owner cash after every real cost, continuing operations, USD millions** (OCF as filed, less stock pay, less all capital
spending; the D&A variant beside it):

| Year | OCF (cont.) | SBC | Capex | D&A | Owner cash (capex) | Owner cash (D&A) | Source |
|---|---|---|---|---|---|---|---|
| 2020 | 245 | 15 | 66 | 135 | 164 | 95 | 10-K FY2022, `0001856485-23-000007` |
| 2021 | 423 | 14 | 69 | 126 | 340 | 283 | same |
| 2022 | 418 | 20 | 149 | 125 | 249 | 273 | same |
| 2023 | 504 | 23 | 210 | 143 | 271 | 338 | 10-K FY2025, `0001856485-26-000008` |
| 2024 | 469 | 23 | 221 | 159 | 225 | 287 | same |
| 2025 | 268 | 18 | 224 | 179 | 26 | 71 | same |
| TTM to 2026-06-30 | 209 | 11 | 220 | n/a | -22 | n/a | 10-Q `0001856485-26-000034` (H1 2026 OCF 28, capex 110, SBC 6) |

Five-year mean 2021 to 2025: **$222M** (capex basis), $250M (D&A basis). Finance-lease principal (3 to 5 a year, 2023 to
2025) would lower the capex basis by that much. **2021 is abnormal:** nine months were inside International Paper with no
interest expense (net interest was income of $1M in 2021 against $69M of expense in 2022, segment note, FY2022 10-K),
capex was $69M against D&A of $126M, and OCF carried $77M of accounts payable for inventory bought at the spin (FY2021
10-K, operating activities). **2025 and the first half of 2026 are a trough** shared by the filer's competitors (below).
Maintenance: the filer states "maintenance, regulatory and reforestation capital expenditures are expected to be in the
range of approximately $165 to $190 million per year (before inflation)", with $162M spent on that class in 2025 and $62M
on "high-return" projects (10-K FY2025, Item 7, Capital Expenditures). The stated maintenance need is at or above D&A
($179M), so the D&A variant does not understate the cost of standing still; the capex basis is the governing one.

**The balance sheets, eight year-ends**, read as the row asks, "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]** (the file closes before Q4, so the
reading is done here as the template directs; filed balance sheets FY2021 to FY2025 and the 10-Q, XBRL for 2018 to 2020):
- *Equity against what was taken out.* Parent equity of $2,528M (2018) and $2,517M (2019) fell to $2,112M (2020) and to
  **$182M at 2021-12-31**: at the spin the company borrowed $1,501M and paid International Paper a special payment of
  $1,520M (FY2021 10-K, financing activities). Equity rebuilt to $678M (2022), $901M (2023), $847M (2024), $966M (2025) and
  $955M (2026-06-30) from earnings, net of $301M of buybacks (2022 to 2025) and dividends. Accumulated other comprehensive
  loss is $1,353M at 2025-12-31 against retained earnings of $2,514M; the figures are saying that a large part of what the
  Brazilian and European assets earned in local currency was lost in dollars. "what the figures are saying and what they
  don’t say" **[M2025-032]**: they do not say what the mills would fetch.
- *Goodwill and intangibles.* Goodwill $179M (2019) to $114M (2025) and $121M (2026-06-30), down by currency and by the
  write-off of all $11M of France goodwill in 2025 "due to continued challenging market conditions in Europe" (10-K FY2025,
  critical accounting estimates). Intangibles are negligible. Equity is mostly tangible.
- *Cash.* $175M (2018), $135M (2019), $95M (2020), $180M (2021), $360M (2022), $280M (2023), $205M (2024), $135M (2025),
  $123M (2026-06-30). Falling for three years while buybacks continued in 2025.
- *Receivables and inventory against sales.* Receivables about $400M to $470M on sales of $2.8B to $3.8B, steady. Inventory
  $342M (2020) to $418M (2025) while sales fell from $3,773M (2024) to $3,351M (2025); $503M at 2026-06-30, which the 10-Q
  explains as stock built "in response to the extended Eastover mill outage later in the year". Not a tell on its own.
- *Debt.* None on the carve-out balance sheets before the spin; $1,400M (2021), $1,032M (2022), $959M (2023), $804M (2024),
  $853M (2025), $964M at 2026-06-30 (current $121M plus long-term $843M), against cash of $123M: net debt about $841M, up
  from about $599M at 2024-12-31. Maturities at 2025-12-31: 2026 $20M, 2027 $370M, 2028 $23M, 2029 $189M (10-K FY2025);
  Term Loan F ($257M, due 2027) was refinanced in 2026 by Term Loan F-3 of $357M (10-Q, financing activities). Covenant:
  maximum total leverage 3.75 to 1 (10-Q, note 12). Debt is rising again into a trough.
- *Contingencies against equity.* The Brazil goodwill-amortization tax case: assessments of about $113M tax and $321M
  interest, penalties and fees at 2026-06-30; under the Tax Matters Agreement Sylvamo pays 40% of up to $300M (at most
  $120M) and International Paper the rest, and International Paper runs the litigation; the administrative court upheld one
  third of the assessments in November 2025 (10-Q, note 10). Other Brazilian VAT matters of $57M, $27M and $19M are
  unreserved; Suzano won the right on 2026-08-06 to invoice VAT on pulp sold to the Três Lagoas mill, "potentially totaling
  $ 15 to $ 20 million annually" (10-Q, note 11). The mercury-contaminated legacy basins at Mogi Guaçu carry an unestimated
  liability that "may be material". Pensions: US and UK plans "fully funded with respect to statutory requirements" (10-K
  FY2025, Item 1A).
- *Retained earnings.* Rising $1,935M (2021) to $2,514M (2025), falling to $2,464M at 2026-06-30 after a first-half net loss
  of $14M and dividends.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the analyst's habits. The price has fallen far (the company bought back $82M of stock in 2025, and shares withheld from employees in the
fourth quarter were valued at $40.60 to $47.37, 10-K FY2025 Item 5, against $33.31 today), which invites the cheap-statistic
reasoning the rows warn against; the test is whether I would be content "if the market closed for five years"
**[M1997-109]**, and the market "just tells us prices" **[M2006-077]**. No macro forecast enters: what counts is "the average
profitability of the business over time" **[M2015-016]**, so the pulp and paper trough of 2025 and 2026 is read as one more
year of a long record, not as a forecast. The other side's case is stated first, to "state their case better than they can" **[M2016-055]**; it is set out
under Q2. **Contrary evidence**, written as found, to "write it down in the first 30 minutes" **[M1997-127]**: (a) North America
earned a 15% segment margin in 2025 (263/1,754) with price and mix rising while volumes fell, and it outearned Domtar's paper
business in every year from 2020 (competitor table); (b) the Brazilian mills sit on owned eucalyptus land a third party
valued at about $900M on 2025-10-17 (10-K FY2025, Item 2), two thirds of the market cap; (c) International Paper is
converting Riverdale paper machine no. 16 to containerboard (8-K `0001193125-25-254570`), taking North American UFS
capacity out, which is the supply exit the Form 10 thesis relies on; (d) on the whole-cycle owner cash the price is a 14.6%
yield. Each is weighed under Q2.

## THE STANDING RULE
Owning a share of SLVM for cash, sized so that a total loss could not touch what the buyer needs, does not put the buyer at
risk of ruin; no borrowed money, no option written: "Never risk permanent loss of capital." **[L2023-005]** is the buyer's
rule and is met by how the purchase would be financed and sized, not by the target. The target's own debt is Q9's (not
reached).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; the product may be plain, what matters is "the economic
  dynamics of the industry" **[M2011-014]**; the first step is "trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**.
- **The key variables, from the filings.** (1) Volume: the filer states "Demand for the types of products that we sell is in
  a secular decline", global UFS demand down at a 2.1% CAGR 2019 to 2025 and 1.1% from 2021 to 2025, and "Demand for paper
  products is likely to decline further" (10-K FY2025, Item 1A). The direction is foreseeable and the insiders write it
  down. (2) Price: set by supply against demand; "we have little influence over the timing and extent of price changes"
  (same). Foreseeable in kind: the price follows whether capacity leaves faster than demand. (3) Cost against rivals: fiber,
  energy, chemicals, currency (BRL, EUR), measurable from segment results against competitors' filings. (4) Capacity exits:
  public (Georgetown closed to Sylvamo's supply at 2024-12-31; Riverdale converting in 2026).
- **Routing.** This is not a fast-changing technology business of the kind the routing sends to TOO HARD; it is a
  slow, stated decline of a plain product. Slow change "can lull you to sleep easier" **[M2014-038]**, so the decline is
  carried to Q2, where it is judged, rather than excused here. The economics are "important and knowable" **[M2006-076]**:
  a commodity sold by price into a shrinking market, whose producers survive in order of cost. I can say where the industry
  will be in ten years (smaller, priced by the marginal mill) and what decides where Sylvamo stands in it (its cost and
  margin against the other mills), which is what "where the business will be in 10 years" **[M2000-037]** asks. The doubt test is "if you have doubts about something being into your circle of competence" **[M2002-092]**, and I
  have none here; a reader can make the decision "off the figures"
  **[M2008-069]**.
- **VERDICT: IN.** "What is important is that I understand the economic dynamics of the industry." **[M2011-014]**: they
  can be foreseen in direction and in kind. Whether Sylvamo's position within them is a castle is the next question.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is "why is that castle still standing?" and "how permanent are they?" **[M1995-038]**.

**The filer's own description of the product and the field (10-K FY2025, `0001856485-26-000008`):**
- "Most of our products are commodities that are available from other producers. We believe our brand recognition and
  service levels impact the demand for our products, but because commodity products have few other distinguishing
  qualities from producer to producer, competition for these products is significantly based on price, which is determined
  by supply relative to demand." (Item 1A.)
- "paper production does not generally rely on proprietary processes, except for highly specialized papers or products"
  (Item 1, Competition).
- "The commodity nature of our products means that supply and demand primarily determine our ability to increase our
  prices." (Item 1A.)
- "Our top ten customers represent approximately 41% of our net sales, including one customer that represents
  approximately 15% of our net sales"; "Generally, our customers are not contractually required to purchase any product
  minimums from us" (Item 1A). The single North American customer was 12% to 14% of sales in 2020 to 2023 (segment notes).
- Demand "is in a secular decline" and "is likely to decline further" (Item 1A, quoted at Q1).

**The castle tests, each with its filing fact.**
1. *The commodity mark.* The rows define the commodity by the customer's indifference: "They sell a commodity-like
   product." **[L2004-003]**; its marks are that "the improvement you get one day, your competitor gets the next day"
   **[M2004-053]** and that the rival sets the price: "whatever he charged for gas was my price." **[M2012-109]**; "he
   determined our profit, because we looked at his price every day." **[M2023-079]**. Fewness of rivals does not cure it:
   "you can have only two competitors" **[M2013-052]**, and North America's four largest producers holding about 80% of
   capacity (Item 1) is therefore not a castle by itself. The filer's words above meet every mark.
2. *The one exception: the low-cost operator.* "when a company is selling a product with commodity-like economic
   characteristics, being the low-cost producer is all-important" **[L2000-017]**; "Another way to prosper in a
   commodity-type business is to be the low-cost operator." **[L2004-007]**; "Our textile business was not the low-cost
   producer." **[M1997-010]**. The cost is measured against the competitor, not in absolute terms: "that is much more
   important to you than the absolute level" **[M2001-013]**; "Those are two different kinds of businesses." **[M2009-059]**.
   The filer claims it: its North American and Latin American mills "predominantly rank in the lowest quartile on global and
   regional UFS cost curves" (Item 1), and Eastover "enjoys the lowest manufacturing cost in North America according to
   Fisher International" (Form 10, `0001193125-21-253977`). The cost curve itself is a third-party dataset not on the
   public record. The public test is the segment result against the competitors' own filings over the whole span, below.
3. *The low-cost operator welcomes the hard market.* "a tough market helps the low-cost operator" **[L1997-021]**; "We want
   the most efficient to be the ones that do well and the less-efficient ones to have plenty of problems." **[M2000-127]**.
   In the 2025 to 2026 trough, Sylvamo's business segment operating profit was $251M in 2025 and **negative $1M in the first
   half of 2026** (Europe -64, Latin America -12, North America +75; 10-Q). In the same trough Suzano's paper segment kept a
   23.1% adjusted EBITDA margin in 2025, and Packaging Corp of America's paper segment earned 21.1% in 2025. A low-cost
   operator does not lose money in two of its three regions while its rivals in those regions earn.
4. *Pricing power and the agony before a rise.* "you can almost measure the strength of a business over time by the agony
   they go through in determining whether a price increase can be sustained" **[M2005-020]**; "over time the businesses with strong
   competitive positions manage to pass through increases in raw material costs" **[M2005-017]**. The filer: "Our ability to increase prices to offset those costs without
   reducing demand is constrained" (Item 1A); 2025 price and mix fell in Europe ($74M of sales) and Latin America ($27M),
   rose $19M in North America (Item 7); first half 2026 price and mix fell again in Europe ($30M) and Latin America ($8M).
5. *Unit volume.* Volume fell in all three regions in 2025 (Item 7). A declining unit count is not by itself a fail: the
   battery "will be around for a very, very, very long time" **[M2015-066]**. But volume decline in a high-fixed-cost
   business is the newspaper case: "Fixed costs are high in the newspaper business" **[L2006-009]**. Here North American
   volume falls further by the filer's own transition: the Georgetown supply ended 2024-12-31 (8-K `0001193125-24-248167`)
   and Riverdale's on 2026-05-30 (8-K `0001193125-25-254570`), with a stated "unfavorable $85 million impact on full year
   2026 Adjusted EBITDA" (10-Q).
6. *The brand and the low bid.* Chamex, Hammermill and the others are real names, but the filer itself ranks them below
   price (test 1). Imaging papers are about half of North American volume and are sold "under private label and brand
   names" (Item 7); with one customer at 15% of sales, "the value of having the brand moves over to the retailer from the
   product itself" **[M2001-090]**. The customer buys "for the low bid" **[M2017-009]** on the filer's own description.
7. *The money test and new entrants.* Capacity is leaving, not entering (Item 1: competitors "have shut down or converted
   mills or paper machines"); the only addition found in the filings read is Sylvamo's own 60,000 tons at Eastover (10-Q). The absence of entrants here is the
   absence of returns, not a barrier: "why are there no new entrants into the field?" **[M2000-077]** is answered by the
   decline. In Brazil the strongest rival is also Sylvamo's pulp supplier at Três Lagoas, now invoicing VAT on that pulp
   (10-Q, note 11): "one competitor is frequently enough to ruin a business" **[M2012-108]**.
8. *Widening or narrowing.* "could the competitive advantage have been made stronger and more durable" **[M2000-075]**. The
   Form 10 said "we expect to be able to generate improved margins and substantial cash flow over the long-term despite
   stable or declining demand" and set a target of Adjusted EBITDA margins "between 15% and 18% over the business cycle"
   (Form 10, Business). The filer's own adjusted EBITDA margin was 17% in 2024, 13% in 2025 and 6% in the first half of 2026
   (10-K FY2025, 10-Q). Latin America and Europe produced 66% of business segment operating profit in 2018 to 2020 (Form 10,
   with Russia) and 28% in 2023 to 2025 (10-K FY2025, Item 1); the Russian mill, which the Form 10 credited with "strong and
   steady margins for more than 10 years", was sold in October 2022, and Europe has lost money in four of the six years
   2020 to 2025 and in the first half of 2026 (segment notes) after a second European mill (Nymölla) was bought for $167M in 2023. The moat is narrowing:
   the case of the business that "has lost still another notch" **[L1995-023]**.
9. *What could destroy or reduce it.* "destroy, or modify, or reduce the economic strengths" **[M2000-014]**: electronic
   substitution, named by the filer as the cause of the decline (Item 1A), works on the product itself and does not reverse.
   "a product that can be shipped in from abroad very easily" **[M2007-116]**: the filer reports tariffs "introduced
   additional competing products into some countries where we sell, putting downward pressure on the pricing of our
   products" (Item 1A).

**The competitor row** (same metric, from the competitors' own filings; segment operating margin = segment operating
profit or income over segment sales, as each filer reports it, special items as filed; Suzano reports only EBITDA by
segment, so Latin America is compared on EBITDA, Sylvamo's computed as segment operating profit plus segment D&A):

| Year | SLVM North America | PCA Paper (Boise UFS) | Domtar paper segment | SLVM Latin America (EBITDA) | Suzano Paper (EBITDA) | SLVM Europe |
|---|---|---|---|---|---|---|
| 2014 | (in IP) | n/a | 7.5% | (in IP) | n/a | (in IP) |
| 2015 | (in IP) | 9.8% | 6.1% | (in IP) | n/a | (in IP) |
| 2016 | (in IP) | 12.6% | 5.1% | (in IP) | n/a | (in IP) |
| 2017 | (in IP) | 5.8% | 5.6% | (in IP) | n/a | (in IP) |
| 2018 | 9.0% | 9.8% | 9.7% | 23.2% (op. margin) | n/a | 13.9% (with Russia) |
| 2019 | 10.0% | 18.2% | 5.2% | 16.3% (op. margin) | n/a | 12.5% (with Russia) |
| 2020 | 2.8% | -3.0% | -4.5% | 23.6% | 32.2% | -11.4% |
| 2021 | 7.7% | 6.5% | 4.4% | 32.1% | 39.8% | -7.9% |
| 2022 | 13.4% | 16.6% | 11.5% | 26.5% | 41.8% | 10.0% |
| 2023 | 13.8% | 20.0% | 4.9% | 26.3% | 33.9% (adj.) | -3.0% |
| 2024 | 14.4% | 20.8% | 7.0% | 23.1% | 30.4% (adj.) | 1.2% |
| 2025 | 15.0% | 21.1% | 0.0% | 20.7% | 23.1% (adj.) | -15.1% |
| H1 2026 | 9.4% | n/a | n/a | -3.0% (op. margin) | n/a | -16.5% |

Sources: SLVM 2020 to 2025 segment notes, 10-K FY2022 `0001856485-23-000007`, FY2023 `0001856485-24-000008`, FY2025
`0001856485-26-000008`; 2018 and 2019 regional operating margins from the Form 10 selected data (`0001193125-21-253977`,
Europe there includes Russia, Latin America on operating margin, not EBITDA); H1 2026 from the 10-Q. Packaging Corp of
America Paper segment from its 10-Ks FY2016 `0000075677-17-000004`, FY2017 `0001564590-18-003690`, FY2019
`0001564590-20-006774`, FY2020 `0001564590-21-008051`, FY2022 `0000950170-23-003990`, FY2023 `0000950170-24-022794`,
FY2025 `0001193125-26-074129`. Domtar Pulp and Paper segment (2014 to 2022; 2021 combines predecessor and successor
periods) and Paper and Packaging segment (2023 to 2025, after the Resolute combination) from its 10-Ks FY2016
`0001564590-17-002312`, FY2019 `0001564590-20-006192`, FY2022 `0000950170-23-005891`, FY2025 `0001193125-26-131800`.
Suzano Paper segment EBITDA margin (2020 to 2022 "EBITDA margin" as printed; 2023 to 2025 adjusted EBITDA over net sales,
computed) from its 20-Fs FY2022 `0001104659-23-051482` and FY2025 `0000909327-26-000045`; Suzano's segment holds paperboard
and tissue as well as uncoated paper and, from 2024, North American paper. The predecessor, International Paper's Printing
Papers segment (with Russia, with India to 2019, and with market pulp to 2014): 9.6% (2012), 4.4% (2013), -0.3% (2014, with $554M of Courtland closure
charges), 11.5% (2015), 13.3% (2016), 11.0% (2017), 12.4% (2018), 12.3% (2019), 7.5% (2020), from IP 10-Ks FY2014
`0000051434-15-000009`, FY2017 `0000051434-18-000008`, FY2020 `0000051434-21-000012`. Clearwater Paper (10-K FY2025
`0001441236-26-000007`) makes SBS paperboard only and Mercer (10-K FY2025 `0001193125-26-048855`) makes softwood pulp and
lumber; neither makes uncoated freesheet, so neither gives a like-for-like row; Mercer's 2025 operating loss of $397.7M,
including impairments and lower pulp realizations, confirms the pulp trough of 2025.

**What the row says, over the whole span, not one year.** North America: Sylvamo's margin was below PCA's paper segment in
2019 and in every year from 2022 to 2025 (2020 to 2025 average 11.2% against PCA's 13.7%) and above Domtar's in every year
from 2020 (Domtar average 3.9%). It is a good mill system in North America, not the clear low-cost operator. Latin America:
Suzano's paper segment margin was above Sylvamo's Latin American margin in every year 2020 to 2025 (averages 33.5% against
25.4%), with the caution that Suzano's segment mixes in other grades; in the first half of 2026 Sylvamo's Latin American
segment lost money while purchased fiber costs rose and its own "forestlands have been producing sub-optimal yields" (Item
1A). Europe: losses in four of the six years 2020 to 2025 (profits of $50M in 2022 and $10M in 2024 against losses of
$200M in the other four) and again in the first half of 2026. Margins are the public proxy for
cost position and are not unit costs; mix, integration and product differ, and the Fisher curve the filer cites is not
public. Even read generously, the row does not show the low-cost operator the exception requires in two of the three
regions, and in the third it shows a rival earning more.

**The other side's case, stated as strongly as I can** (to "state their case better than they can" **[M2016-055]**). The bull reads the Form 10's own logic: in a
declining commodity, high-cost capacity leaves first, and a first-quartile survivor's operating rate and price rise; North
America shows exactly that (2.8% margin in 2020 to 15.0% in 2025, price and mix up in 2025 while volumes fell); the Eastover
investments add 60,000 tons and an expected $50M of annual Adjusted EBITDA from 2027 (10-Q); Brazil sits on owned eucalyptus
land valued by a third party at about $900M; Europe can be fixed or closed; and at $33.31 the market cap is about seven times the
whole-cycle owner cash. Where it fails on the record: the survivor thesis requires the survivor to be the low-cost one, and
in North America a rival earns more; the "improved margins" the Form 10 expected have gone the other way in two regions;
the North American gain since 2020 rode capacity that International Paper itself closed, which took Sylvamo's supplied
volume with it (Georgetown, Riverdale); and the $50M Eastover benefit is the textile mill's new machine, the improvement
"your competitor gets the next day" **[M2004-053]**: "everybody in the crowd is up on tiptoes" **[M2004-054]**.

**The declining business and its one exception.** "If you really think a business is declining, most of the time you should
avoid it." **[M2012-062]**. The exception the framework carries is newspapers bought "at a very low multiple of current
earnings" **[L2012-010]**, which the speakers paid "because the earnings will go down" **[M2013-026]**. The exception does
not fit on the facts: current earnings are a first-half net loss of $14M and owner cash of minus $22M for the twelve months
to 2026-06-30, so there is no low multiple of current earnings to pay; and the papers bought were ones "of the type we like"
in L2012-010's own sentence, a type the row does not extend to a commodity priced by its rivals. The rows on the cheap
declining business govern instead: "the idea of buying the cigar butts that are declining or poor businesses for a bargain
price is not something that we try to do anymore" **[M2019-015]**; marginal businesses at cheap prices "are the wrong
foundation on which to build a large and enduring enterprise" **[L2014-009]**; "Though the price I paid for Berkshire looked
cheap" **[L2024-005]**; and the better manager "would have done a little bit better. But it still would have failed."
**[M2024-030]**.

**Why OUT and not TOO HARD.** The rows give three boxes, "in, out, and too hard" **[M2006-013]**; the tenuous moat that
cannot be valued is the one of which they say "therefore we leave it alone" **[M2000-019]**, which is TOO HARD in the
framework's routing, and a castle shown open on the evidence is OUT. Here the evidence is the filer's own: a commodity priced by supply and demand,
no proprietary process, a customer base that buys on price with one customer at 15%, demand in stated secular decline, and
segment results that over the whole span do not show the low-cost position the one exception needs, with two regions
losing money in the current trough while rivals in those regions earn. "In an unregulated commodity business, a company
must lower its costs to competitive levels or face extinction." **[L1994-035]**. The decision is made from the documents,
and no further reading would turn a price-taker into a low-cost operator.

- **VERDICT: OUT.** In a commodity "being the low-cost producer is all-important" **[L2000-017]**, and over the span the
  competitors' own filings do not show Sylvamo to be it; "The guy who could sell it cheaper than we could made it risky for
  us." **[M1997-010]**; the rival sets the price, "whatever he charged for gas was my price." **[M2012-109]**; and "If you
  really think a business is declining, most of the time you should avoid it." **[M2012-062]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts recorded for the record only, not weighed: capital spending was 125% of D&A in
2025 and 139% in 2024 (10-K FY2025, Item 7); the filer's own maintenance estimate ($165M to $190M a year before inflation)
is at or above D&A.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 as the template directs. Recorded only: the filer features Adjusted
EBITDA and "free cash flow" in its executive summaries (10-K FY2025, Item 7), and its Form 10 margin target was stated in
Adjusted EBITDA; not weighed.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. The 2026 proxy (`0001193125-26-138839`) was fetched and not read.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Recorded only: $82M of buybacks in 2025 under a programme that names no price (10-K FY2025, Item 5), none in
the first half of 2026; a $167M European acquisition in 2023; a shareholder rights plan adopted 2025-11-10 with a 15%
trigger, expiring 2026-11-09 (8-K `0001193125-25-274343`).

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED. The owner asked for the value range, fair price and cheap price; they are given below as computation.

## Q8 to Q10, Q12
NOT REACHED.

---
## COMPUTATION - NOT A CLEARANCE
*(Operator rule 3: the file closed OUT at Q2, so every figure below is arithmetic at the owner's request, carries no entry
language, and is not a clearance. Script: `Test Runs/_research 2026-10-05 SLVM/calc.py`.)*

**(a) VALUE RANGE, the Q7 CONVENTION as written** (five-year average owner cash after every real cost, aggregate not per
share, carried ten years at the growth shown, then zero nominal growth, discounted at the 5.63% sovereign; the ends are the
no-growth and shown-growth cases):
- Base: $222.2M (2021 to 2025, capex basis). Growth shown on the aggregate, 2021 to 2025: from $340M to $26M, a compound
  rate of minus 47.4% a year.
- No-growth end: $3,947M, **$99.26 a share**. Shown-growth end: $224M, **$5.63 a share**.
- **Range $5.63 to $99.26 against $33.31.** Top over bottom is about 17.6 to 1, far wider than the convention's three to
  one: had Q7 been reached, it would close TOO HARD by the width rule ("the range must be so wide that no useful conclusion
  can be reached" **[L2000-025]**).
- D&A variant (base $250.4M, shown growth minus 29.2%): $14.59 to $111.86.
- **Whole-cycle variant** (the window holds an abnormal year, 2021, inside International Paper with no interest and starved
  capex): base the four post-spin years 2022 to 2025, mean $192.8M, which runs from the 2022 price peak to the 2025 trough.
  Growth shown 2022 to 2025: minus 52.9% a year. No-growth end $3,424M, **$86.11 a share**; shown-growth end $156M,
  **$3.93 a share**. Range $3.93 to $86.11, about 22 to 1.
- What the range is saying: the no-growth end assumes the 2022 to 2025 cash forever in a business whose filer says demand
  will keep falling; the shown-growth end carries a peak-to-trough collapse for ten years. Neither end is a forecast, and the
  width is itself the finding.

**(b) FAIR PRICE** (the price at or below which the central case clears the about 10% pre-tax floor, CONVENTION at Q7):
- Tax treatment: owner cash is after cash taxes (OCF is after tax). The 10% pre-tax floor ("a very high probability of at
  least 10% pre-tax returns" **[L2002-020]**) is converted to after tax at Sylvamo's own three-year effective rate,
  29.4% (income tax over pre-tax income from continuing operations, 2023 to 2025: 286/973, 10-K FY2025 and FY2024), giving
  **7.06% after tax**.
- Central case (CONVENTION of this run, chosen because it is the least invented decline rate on the record): the
  whole-cycle owner cash of $192.8M, declining forever at 2.1% a year, the filer's own figure for global UFS demand
  2019 to 2025 (10-K FY2025, Item 1A, citing RISI). Expected return at a price = yield minus 2.1%.
- **Fair price: $2,104M, about $52.92 a share.** Alternates: the five-year base at minus 2.1%: $61.01; whole-cycle base at
  minus 1.1% (the 2021 to 2025 demand rate): $59.40; whole-cycle at no growth: $68.66.
- Against the trailing twelve months (owner cash minus $22M) no price clears the floor.

**(c) CHEAP PRICE** (below which no pencil is needed). **Rule (CONVENTION of this run):** the price at which the worst full
year in the window, 2025 ($26M of owner cash), alone, at no growth, clears the floor after tax. Rationale: "it ought to just
kind of scream at you" **[M1996-084]**, and the margin grows with "the more volatile the business is" **[M1997-080]**; a
price that needs the average year to work needs a pencil in a business whose trough year earns a tenth of its average.
- **Cheap price: $368M, about $9.26 a share.**
- Alternate shown for comparison only (the pattern seen in the contaminating commit subjects, declared above): half the fair
  price, about $26.46.

**Against the price of $33.31:** above the cheap price ($9.26), below the fair price ($52.92), inside both value ranges. Price
does not reopen a castle shown open: "the idea of buying the cigar butts that are declining or poor businesses for a bargain
price is not something that we try to do anymore" **[M2019-015]**.

---
## THE BOX
**OUT, decided at Q2.** A commodity in stated secular decline (filer: "Most of our products are commodities", price
"determined by supply relative to demand", demand "likely to decline further"), whose one exception, the low-cost operator,
is not shown against Suzano in Brazil or PCA in North America over 2018 to 2025, with Europe losing money in four of the six
years 2020 to 2025 and the whole company at a segment loss in the first half of 2026. Computation only: value range $5.63 to $99.26
(whole-cycle $3.93 to $86.11), fair about $52.92, cheap about $9.26, against $33.31. No research pass is opened (OUT, not
TOO HARD).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before the first EDGAR request); written
      question by question. **Not committed after each**: the operator's instruction for this run is not to commit, so
      write-early was kept by writing to the file and the commit step was not done.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact has its accession; no
      number without a filing or a labelled CONVENTION.
- [x] The order was kept; Q2 failed and closed the run; Q3 to Q12 are NOT REACHED and carry no clearance.
- [x] Owner cash after every real cost (OCF less stock pay less all capital spending), never a net-income proxy; sovereign
      from the US Treasury par yield curve; the price is an aggregator quote and is flagged.
- [x] Contrary evidence written down as found, "write it down in the first 30 minutes" **[M1997-127]** (Foundations,
      items a to d; the other side's case at Q2).
- [x] No row dated after the anchor: not a point-in-time run (anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used, and its 2021 OCF (with Russia) and missing pre-2021 capex were
      replaced by the filed continuing-operations figures.
- [x] `python tools/check_framework.py` PASS (run 2026-10-05 after the file was complete), and a script check
      (`_research 2026-10-05 SLVM/idcheck.py`): no v4 ids, every M, L and R id in `principle_ledger_v5.csv`, every
      quoted fragment beside an id found in that row, every id preceded by its row's own words, no em dashes.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **Q7's shown-growth end is unworkable for a shrinking business.** The convention carries owner cash "at the
growth the business has actually shown over those years, never above it" from the window's endpoints; here both endpoints
are abnormal (2021 pre-spin, 2025 trough) and the endpoint rate is minus 47%, which makes the range 17 to 1 and would send
every cyclical decliner to TOO HARD at Q7 by width, whatever its castle. The convention cites a base-year row (L2005-003) for
checking the start year but gives no rule for a negative rate or for an abnormal end year; I computed it as written
and said what it shows. (2) **The low-cost exception has no stated public test.** Q2 says the cost "is measured against the
competitor" but the cost curve that would show it is a private dataset; I used segment margins from the competitors' own
filings over the span as the public proxy and said its limits (mix, segment definitions, EBITDA against operating margin
for Suzano). A line saying which public measure stands for cost position would make two analysts agree. (3) **The newspaper
exception to the decline rule is carried as a tension with no test of fit.** I tested it on its own row's words (a very low
multiple of current earnings, papers of the type liked) and found it unmet; whether the exception can ever apply to a
commodity is not said. (4) **The template's headings and operator rule 3's required heading contain em dashes**, which the
operator's standing rule forbids in written output; I wrote "COMPUTATION - NOT A CLEARANCE" with a hyphen and the headings
with colons. Also: the template's position note sends the analyst to `PORTFOLIO.md`, which this run's blind rule forbids;
the note was left unknown. And the template's "committed after each" box cannot be ticked under an instruction not to
commit; it is marked as not done, with the reason.
