# Company Run: Whirlpool Corporation (NYSE: WHR), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 23d4b56e). Research folder:
`Test Runs/_research 2026-10-17 WHR/` (notes, scripts, the tool outputs; raw filings in its ignored `cache/`).
Dispatched blind run, purchase run of record.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (ac2b671c): `PORTFOLIO.md` read for this one ticker; the operator does not hold WHR (no line names WHR or Whirlpool).*

**Contamination declared.** Before this run I saw only what the session context showed unasked: the recent commit
subjects of the repository (a VUOC run and its fold, another company) and the memory index lines, which name queue
states, counts and other runs but no line about Whirlpool. Nothing about this company from any other run, register,
holding file or portfolio file was seen; none was opened, listed or searched. Nothing seen is used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $27.89 (close 2026-10-16, printed by `python tools/run.py WHR`; **aggregator, live quote only, flagged**
  under operator rule 5).
- **Shares by class** from the latest filing's cover: **65,199,378 common** (10-Q for the quarter ended 2026-06-30, filed
  2026-08-04, accession `0000106640-26-000061`, cover as of 2026-07-31; `python Screens/cover_shares.py WHR`). Checked
  against the balance sheet of the same 10-Q: 73 million issued less 8 million treasury = 65 million outstanding; it agrees.
  The cover count already includes the 7,898,550 common shares sold at $69 on 2026-02-27 (10-Q, MD&A, Common Stock
  Offering; the brief's 6,884,057 base shares and, by subtraction, 1,014,493 shares under the 30-day option). No 8-K or prospectus after the 10-Q adds
  common shares (filing index read to 2026-08-13). The Guangdong Whirlpool private placement of 434,782 shares was
  terminated for want of regulatory approval (same 10-Q).
  **A second class, convertible:** 575,000 shares of 8.50% Series A Mandatory Convertible Preferred Stock ($575 million
  liquidation preference), held as 11,500,000 depositary shares (WHR-PRA), mandatory conversion expected 2029-02-15 at
  between 12.3340 and 14.4920 common shares per preferred share (prospectus supplement 424B5 filed 2026-02-26, accession
  `0001193125-26-076958`). At any price below the $69 initial price the maximum rate applies: 575,000 x 14.4920 =
  8,332,900 common shares. **CONVENTION of this run:** the mandatory convertible is counted as the common shares it must
  become at the maximum rate, since conversion is compulsory and the price is far below $69; rationale: it is equity that
  takes common shares on a fixed date, and counting it as debt or leaving it out would each misstate the per-share figure.
  **As-converted count: 73,532,278 shares.**
- **Market cap:** common only 65,199,378 x $27.89 = **$1,818.4M**; as-converted 73,532,278 x $27.89 = **$2,050.8M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-16 (`python tools/sources.py`, issuing authority). The earnings currency is USD (the XBRL unit of the cash-flow
  series; the 10-K reports in US dollars, with Brazil and Mexico the largest foreign operations).
- **Filings read** (operator rule 4): the 10-K for FY2025, filed 2026-02-11, accession `0000106640-26-000009` (Items 1,
  1A, 7, the statements, notes 15 and 16); the 10-Q for Q2 2026, filed 2026-08-04, `0000106640-26-000061` (statements,
  MD&A, forward-looking perspective); the 10-Q for Q1 2026, `0000106640-26-000036` (fetched, not relied on); the proxy
  (DEF 14A filed 2026-03-10, `0001193125-26-100387`, fetched, not reached); the 8-Ks of 2026-02-27
  (`0001193125-26-082849`), 2026-06-16 (`0001193125-26-272923`), 2026-06-18 (`0001193125-26-275891`), 2026-07-01
  (`0000106640-26-000052`) and 2026-08-03 (`0000106640-26-000056`); the two 424B5 prospectus supplements of 2026-02-26
  (`0001193125-26-076958`, `0001193125-26-076926`); and for the history the segment notes of the 10-Ks for FY2022
  (`0000106640-23-000015`), FY2019 (`0000106640-20-000017`) and FY2016 (`0000106640-17-000013`).
  **One figure cross-checked against the filed statement:** FY2025 cash provided by operating activities, $470 million
  on the filed Consolidated Statement of Cash Flows (10-K, page 57), equals the XBRL figure `tools/run.py` printed (470.0);
  FY2025 net sales $15,524 million on the MD&A table equals the tagged figure.
- **`python tools/run.py WHR`, arithmetic lines only** (output kept in `run_py_output.txt`): OCF 915 / 835 / 470 for
  2023 to 2025; capex 549 / 451 / 389; D&A 361 / 333 / 338. Its "SBC" column (34 / 91 / 137) is the filed line "Share based
  compensation and other", which carries other items; the filed stock-pay expense (`AllocatedShareBasedCompensationExpense`)
  is 33 / 28 / 28, and that is the figure this run deducts. The tool's owner-cash means and yields are not used.
  Owner cash after every real cost, OCF less stock pay less all capital spending, USD millions, from the filed series
  (`scripts/series.py` over the companyfacts file; first-filed figures):

  | year | OCF | stock pay | capex | owner cash | cash paid for businesses |
  |---|---|---|---|---|---|
  | 2016 | 1,203 | 39 | 660 | 504 | |
  | 2017 | 1,264 | 48 | 684 | 532 | |
  | 2018 | 1,229 | 51 | 590 | 588 | |
  | 2019 | 1,230 | 50 | 532 | 648 | |
  | 2020 | 1,500 | 67 | 410 | 1,023 | |
  | 2021 | 2,176 | 82 | 525 | 1,569 | 46 |
  | 2022 | 1,390 | 58 | 570 | 762 | 3,000 (InSinkErator) |
  | 2023 | 915 | 33 | 549 | 333 | 14 |
  | 2024 | 835 | 28 | 451 | 356 | (Europe deconsolidated: proceeds 95, cash left with the business 245) |
  | 2025 | 470 | 28 | 389 | 53 | (India deconsolidated: proceeds 198, cash left with the business 327) |

  Six months to 2026-06-30: OCF $(947) million, capex $162 million (seasonal; the 10-Q). The company's own 2026 outlook,
  cut at the Q2 10-Q: OCF about $700 million, capex about $400 million, GAAP EPS $2.25 to $2.75 (it was about $6.25 in
  the 10-K). These outlook figures are the company's projections and are recorded as facts about what it said, not used.

**The balance sheets, read here because the file closes before Q4** (ten year-ends, `tools/run.py` table read against
the filed statements of FY2025 and Q2 2026; USD millions):

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | borrowings | retained |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 19,153 | 4,773 | 1,085 | 2,711 | 2,623 | 2,956 | 2,552 | 4,436 | 7,314 |
| 2019 | 18,881 | 3,195 | 1,952 | 2,198 | 2,438 | 2,440 | 2,225 | 4,993 | 7,870 |
| 2021 | 20,285 | 4,846 | 3,044 | 3,100 | 2,717 | 2,485 | 1,981 | 5,237 | 10,170 |
| 2022 | 17,124 | 2,336 | 1,958 | 1,555 | 2,089 | 3,314 | 3,164 | 7,615 | 8,261 |
| 2024 | 16,301 | 2,683 | 1,275 | 1,317 | 2,035 | 3,322 | 2,717 | 6,626 | 1,311 |
| 2025 | 16,001 | 2,726 | 669 | 1,276 | 2,307 | 3,103 | 2,563 | 6,520 | 1,330 |
| 2026-06-30 | 17,326 | 3,933 | 1,239 | 1,237 | 2,219 | 3,103 | 2,552 | 7,068 | 1,262 |

(The other year-ends are in `run_py_output.txt`.) What moved and why. **Equity against goodwill and intangibles:** in
every year from 2018 the goodwill and intangibles (about $5.7 billion at 2025) exceed the whole of Whirlpool's equity
(about $2.7 billion), so tangible equity is negative throughout; the equity is what was paid for brands and deals, not
plant. The InSinkErator purchase (2022, $3.0 billion in cash, goodwill up $1.1 billion per the FY2022 10-K) was paid
with borrowings: debt rose from $5.2 billion to $7.6 billion that year. **Retained earnings** fell from $8,358 million to
$1,311 million in 2024; the filed equity statement shows a "Treasury stock retirement" of $6,340 million charged to
retained earnings, an accounting retirement of shares bought back in earlier years, not a loss. **Cash** fell from $3.0
billion (2021) to $669 million (2025), and was restored to $1.2 billion in 2026 only by the $1.08 billion equity raise and
the $2 billion secured notes. **Receivables and inventory against sales:** receivables fell with the deconsolidations
(Lowe's alone is 44% of receivables at 2025, 10-K note 15); inventory rose $372 million in 2025 against flat North
American sales (the 10-K ties it to product transitions). **Debt** has stayed at $6.5 to $7.6 billion since 2022
while sales fell from $22.0 billion (2021) to $15.5 billion (2025); by mid-2026 it is secured (second-lien notes and an
asset-based facility on receivables, inventory, intellectual property and equipment; the 8-K of 2026-06-16), and the
senior unsecured rating is Ba3 / BB- (Q2 10-Q). "what the figures are saying and what they don’t say and what they
can’t say" **[M2025-032]**: the sheets say the business now carries more debt per dollar of sales than at any year-end
read, that its equity is almost wholly purchased intangibles, two of which the company itself has written down (Maytag
$381 million in 2024, JennAir $106 million in 2025; Maytag, JennAir, Amana and InSinkErator "continue to be at risk",
Q2 10-Q); they do not say what the brands will earn.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which turns the run toward the appliance business and away from the price's fall from $69 in February to
$27.89 now; the market "just tells us prices" **[M2006-077]**, and the fall instructs nothing. No macro enters
**[M2000-094]**: the housing cycle, rates and tariffs are not forecast; they enter only as facts in the filings about what
the business has done under them. Who is paid to tell you: the filings feature "free cash flow", a "value creation
framework" and an EPS outlook; these are the seller's projections and are not used **[M1995-050]**. The analyst's habit
that bears most here: look for "what’s wrong in things because that’s part of investing" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) in 2014 to 2019 Whirlpool's North America segment
earned EBIT of 10% to 13% of sales, which is not the margin of a business without a castle; (2) about 80% of the major
appliances it sells in the US are made in the US and 96% of its US steel is domestic (10-K Item 1), a local-scale
position in bulky goods; (3) it reports "leading U.S. builder share" (10-K Item 1); (4) the small-appliance part (SDA
Global, KitchenAid) earned EBIT margins of 14% to 16% in 2023 to 2025 and rose in 2025 on price/mix (10-K MD&A). Each of
these is weighed at Q2.

## THE STANDING RULE
Owning a part-interest bought for cash, unlevered, at a size the buyer's own liquidity dwarfs, puts the buyer at no risk
of ruin; "borrowed money has no place in the investor's tool kit" **[L2014-005]** and "We are never going to risk what we
have and need for what we don’t have and don’t need." **[M2012-081]**. The target's own heavy and now secured debt is a
risk to the holding, not to the buyer, and belongs to Q9. Nothing here closes the file.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, of "the economic dynamics of the industry" rather than the product
  **[M2011-014]**. Whirlpool makes and sells washers, dryers, refrigerators, ranges, dishwashers and disposers in North and
  Latin America, and KitchenAid small appliances (10-K Item 1). The products change slowly; a 2021 "first top-load
  clothes washer with a removable agitator" is the kind of invention the 10-K lists. Demand is mostly replacement
  (the 10-K's 2026 outlook names "strong replacement demand" beside "subdued discretionary demand").
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) industry unit demand in the US and Brazil,
  replacement-led, foreseeable in its long average and not year to year; (2) price and mix against Samsung, LG, Haier
  (GE Appliances), Midea, Electrolux, Bosch and the rest (10-K Item 1, Competition); (3) materials and tariff costs;
  (4) the power of a few large trade customers (Lowe's 15% of 2025 sales). None is a technology forecast; the 10-K's
  risk factor on AI and connected appliances is a risk of the ordinary kind, not a change in what an appliance is. The
  insiders would write the forecast down: an appliance maker's ten-year unit demand is the kind of figure the industry
  publishes, unlike the tech field the row describes **[M2000-105]**. Variable (2) is knowable from the filings of the
  maker and its rivals, and it is the castle question, which Q2 owns.
- **Routing.** Not a fast-changing industry (no TOO HARD at Q1); not a financial institution; the parts (three
  segments) are each a manufacturer whose economics can be read from the segment note. A dependence on steel and resin
  prices is not by itself a STOP **[M2016-025]**; the business is judged "off the figures" **[M2008-069]**. I have no doubt
  that a maker of white goods sits inside the perimeter **[M2002-092]**; whether it is a good business is not this
  question.
- **VERDICT: IN.** The economics of a slow-changing durable-goods maker can be foreseen in kind; the key variable that
  decides it, price against the rivals, is knowable and is put at Q2 **[M1995-051]**, **[M2006-076]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence, chosen from the latest 10-K and why** (the brief leaves them to the analyst). From Item 1: the
segments and their products; the Competition paragraph, which names the rivals and the trade customers "who have many
choices and demand competitive products, services and prices, and many of whom have their own brands"; the cost-position
paragraph (80% US-made). From Item 1A: the first two strategic risks (intense competition; large trade customers with
"significant leverage as buyers", "Most of our products are not sold through long-term contracts"); the brand risk; the
tariff risk, in which "Many of our most significant competitors are foreign companies" and foreign competitors
"pre-loaded" finished goods into the US; the credit-rating risk. From Item 7: each segment's EBIT margin and the cause the
filer itself names for each year's change; the trademark impairments. They were chosen because Q2's tests ask exactly
these things (pricing power, the low bid, the brand, the attacker, widening or narrowing), and the filer's own words
for the cause of each margin change are the nearest the filings come to "the agony before a price rise".

**The parts table** (business of parts, more than half of five-year operating profit decides; segment EBIT as the 10-Ks
report it, USD millions):

| part | five-year segment EBIT | share | castle | decides |
|---|---|---|---|---|
| North America major appliances (MDA NA; "North America" before the 2024 recast, which then also held small appliances) | 2021 2,220; 2022 1,319; 2023 1,008; 2024 665; 2025 499 = 5,711 | about 76% of the segments' 7,448 | read below | **yes** |
| MDA Latin America (Brazil, Mexico; Brastemp, Consul) | 265; 200; 187; 245; 201 = 1,098 | about 15% | not read to a close | no |
| SDA Global (KitchenAid small appliances; reported apart from 2024, 2023 recast) | 139; 145; 177 (2023 to 2025) | about 6% | possibly standing: EBIT margin 14.3%, 14.3%, 16.0%, rising on price/mix in 2025 | no |
| EMEA / MDA Europe, Asia (gone: contributed to Beko 2024, India deconsolidated 2025) | EMEA 100; (58); 25; (9); Asia 66; 54; (Asia in Other from 2023) | small | EMEA earned about nothing for the years read and was disposed of at a $1.9 billion total loss (10-K note 16) | no |

Sources: segment notes of the 10-Ks for FY2022 (`0000106640-23-000015`, 2020 to 2022) and FY2025 (`0000106640-26-000009`,
2023 to 2025, recast). The two bases differ (small appliances moved out of North America in 2024); on either basis North
America carries more than half, so it decides, and the file closes on its castle.

**The deciding part's margins over the span** (North America EBIT as a share of its sales; FY2016 10-K
`0000106640-17-000013` for 2014 to 2016, where the segment measure was "operating profit"; FY2019 10-K
`0000106640-20-000017` for 2017 to 2019; FY2022 10-K for 2020 to 2022; FY2025 10-K for 2023 to 2025, MDA NA basis;
Q2 2026 10-Q for the half-year):

| 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10.1% | 11.7% | 11.5% | 11.6% | 11.8% | 12.7% | 15.7% | 17.8% | 11.5% | 9.4% | 6.5% | 4.9% | 1.5% |

The causes the filer names: 2024, "EBIT margin decreased primarily due to the unfavorable impact of product price/mix";
2025, "primarily due to the unfavorable impact of tariff cost"; H1 2026, "operational inefficiencies associated with lower
volume, tariff cost and inflation", with "favorable product price/mix" in Q2 only (10-K MD&A; Q2 10-Q MD&A).

**The competitor row** (same metric, the rivals' own filings). The 10-K names BSH (Bosch), Electrolux, Haier, Hisense, LG,
Mabe, Midea, Panasonic and Samsung in major appliances. **None of the nine files annual reports with the SEC** (flagged:
Bosch and Mabe are private; Electrolux reports in Stockholm, Haier, Hisense and Midea in China and Hong Kong, LG and
Samsung in Korea, Panasonic in Tokyo). One rival was read from its own filing: AB Electrolux, the financial-data
workbook published with its Q4 2025 interim report (quarterly figures 2017 to 2025, summed to years in
`electrolux_annual_from_finstat.txt`; the 2025 and 2024 sums cross-checked against its year-end report: net sales SEK
131,282m and 136,150m, operating income excluding non-recurring items SEK 3,657m and 1,666m):

| operating margin excl. non-recurring items | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Electrolux group | 6.1% | 4.8% | 3.8% | 5.0% | 6.0% | 0.6% | 0.3% | 1.2% | 2.8% |
| Electrolux North America (Frigidaire), reported operating margin | n/a | 2.8% | -1.3% | 3.2% | 1.7% | -5.1% | -5.2% | -3.9% | -1.3% |
| Whirlpool North America (above) | 11.6% | 11.8% | 12.7% | 15.7% | 17.8% | 11.5% | 9.4% | 6.5% | 4.9% |

Electrolux group operating income excluding non-recurring items against its year-end net assets: 2017 36%, 2019 17%,
2021 28%, 2022 2%, 2023 1%, 2024 4%, 2025 10% (same workbook). Haier (owner of GE Appliances since 2016), Samsung and LG,
the rivals most relevant in Whirlpool's home market, were not read from their own filings (what I could not get).

**The tests, each with its filing fact.**
1. **The castle questions** **[M1995-038]**. What keeps it standing: scale in bulky goods made locally (80% US-made),
   distribution and service through the big home-improvement chains and builders, and a brand portfolio. How permanent:
   the filings show the margin these protect falling for five straight years, from 17.8% to 4.9% and 1.5% in the half.
2. **Would it stand without the lord?** The lord here is not a manager but the trade regime. The 10-K expects "positive
   impacts of tariffs on appliances"; Whirlpool filed the dumping petitions against Samsung, LG and Electrolux washers in
   2011 and 2015 and holds the resulting orders (Q2 10-Q, Antidumping); the Supreme Court voided the IEEPA tariffs in
   February 2026 (same). My reading, not a speaker's: a margin that waits on tariffs and dumping orders is protected by
   the government, not by the customer, and "The really great business is one that doesn’t require good management"
   **[M1996-037]** reads the same way for a business that requires good trade policy.
3. **The money test** **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy,
   could I do it?" The question has been answered by events in this market: Samsung and LG came into US laundry and
   took enough of it that Whirlpool went to law against their prices, and the 10-K says the rivals are "increasingly
   expanding beyond their existing manufacturing footprint". "If the answer had been yes, we wouldn’t have done it."
   **[M2011-015]**.
4. **Pricing power and the agony** **[M2005-020]**: "you can almost measure the strength of a business over time by the
   agony they go through in determining whether a price increase can be sustained." The filings show the agony: 2024's
   decline came from "price/mix"; the 2026 plan rested on "margin expansion from previously announced promotional pricing
   actions" (10-K) and then on "the largest pricing changes in a decade" (Q2 10-Q), into falling volume and a guidance cut
   from about $6.25 to $2.25 to $2.75 a share. Accrued advertising and promotions stood at $755 million at 2025 year-end
   (balance sheet), about 7% of North American sales.
5. **Unit volume and share of mind**: volume fell in 2025 and H1 2026 (MD&A). Market share: no figure in the 10-K or the
   Q2 10-Q (a search of both for "market share", "share of" and "builder share" finds only "leading U.S. builder share",
   asserted without a figure, and the risk factor quoted under test 6). Unit volume
   with high fixed costs is the newspaper's warning, "that's bad news when unit volume heads south" **[L2006-009]**, and
   the Q2 10-Q names "operational inefficiencies associated with lower volume" as the first cause of the half's margin.
6. **The low-cost position** **[M2018-043]**, **[M1997-010]**: the 10-K claims a "Strong Cost Position"; its own risk
   factor says the opposite of the rivals: "Our competitors, especially global competitors with low-cost sources of
   supply, vertically integrated business models and/or highly protected home countries outside the United States (U.S.),
   have aggressively priced their products and/or introduced new products to increase market share" (10-K Item 1A). The
   filings give no cost figure against a rival, and the company petitioning against the rivals' prices is not the
   low-cost producer. Against Electrolux, Whirlpool's North America margin has been far higher every year; against the Asian
   rivals no figure is on the record I read. "The guy who could sell it cheaper than we could made it risky for us."
   **[M1997-010]**.
7. **The brand in the customer's mind** **[M2015-038]**: "the retailer is going to use all the pressure they’ve got and,
   therefore, the brand has to stand for something in the consumer’s mind." The owner of the brands has itself written
   two of them down: Maytag by $381 million (2024) and JennAir by $106 million (2025), with Maytag, JennAir, Amana and
   InSinkErator still "at risk" (10-K MD&A; Q2 10-Q). Whirlpool also sells "some products to other manufacturers,
   distributors, and retailers for resale [...] under those manufacturers' and retailers' respective brand names" (10-K
   Item 1), the case in which "the value of having the brand moves over to the retailer from the product itself"
   **[M2001-090]**.
8. **Would the customer still choose it over the low bid?** **[M2017-009]**: the buyer who decides is the trade customer:
   "large, sophisticated trade customers who have many choices and demand competitive products, services and prices, and
   many of whom have their own brands which compete with our products"; "Most of our products are not sold through
   long-term contracts, allowing trade customers to change volume among suppliers like us" (10-K Items 1 and 1A). Lowe's
   is 15% of sales and 44% of receivables. That is the customer who buys on the low bid **[L2004-003]**.
9. **Ask the competitors**: not done beyond Electrolux's figures; no interview or scuttlebutt is on the public record I
   read.
10. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**: narrowing, every year from 2021 to the latest half; the
    filer's own causes are price/mix, tariffs and volume, and none of its filings claims a gain in share or price.
11. **What could destroy it** **[M2000-014]**: the attackers already inside the market, the product shipped in from
    abroad (the 10-K's "pre-loading" of finished goods by foreign rivals is the shipment in plain terms; "a product that
    can be shipped in from abroad very easily" **[M2007-116]**), and the loss of tariff protection.

**The field's returns over the last full cycle** (2016 to 2025, the decade that holds the pre-pandemic years, the 2020 to
2021 peak the FY2022 10-K describes as a pattern that "differed from historical periods due to the COVID-19 pandemic", and
the trough since). Whirlpool consolidated: operating profit summed $9,251 million on sales summed $196,178 million, an
average operating margin of 4.7%; on the owners' capital (equity plus borrowings less cash, ten year-end average about
$7.4 billion) the average operating profit of $925 million is about 12.5% before tax and about 9% after a 25% tax; a
restructuring charge was booked in every one of the sixteen years 2010 to 2025 (companyfacts series). Electrolux, the one
rival read, earned 3.3% on summed sales (2017 to 2025) and its North American business lost money in five of the eight years
read. In words: the field's durable players earn an ordinary return over the cycle on what their owners have put in,
and the rival in Whirlpool's own market earns less than nothing; Whirlpool's North America earned good margins before
2022 and has given back all of the excess since. "you can have only two competitors and they’re still terrible
businesses, they beat each other’s brains out." **[M2013-052]**.

**Contrary evidence, weighed** **[M1997-127]**. (1) The 2014 to 2019 North America margins of 10% to 13% are the strongest
case for a castle, and the business's tangible capital is small (goodwill and intangibles exceed equity), so on the
capital actually needed the return in those years was high. (2) The decline since 2022 coincides with a housing trough
and a tariff shock, and a bad year is "a cyclical problem, not a secular one" when "we at least maintained, and in some
instances widened, our competitive superiority" **[L1995-022]**. Against (2): the row's condition is the maintained
superiority, and the filings show the opposite of it (price/mix named as the cause in 2024, promotions to be withdrawn,
brands written down, no claim of share held); the rival in the same cycle, Electrolux North America, narrowed its loss
from -3.9% to -1.3% in 2025 while Whirlpool's margin fell from 6.5% to 4.9%. Against (1): good margins in a protected
period do not show the castle when the protection is the tariff and the evidence since is a five-year retreat
"whether it’s likely to widen further or shrink on you" **[M1999-108]**. (3) KitchenAid small appliances may well be a
standing castle; it does not decide (6% of five-year segment EBIT).

**The box considered, OUT or TOO HARD.** A castle whose future cannot be judged goes to TOO HARD **[M2000-019]**; a castle
shown on the evidence to be filling in is OUT. The evidence here is not silence: the filer's own causes, its own
impairments, its own description of its customers and rivals, and five years of narrowing, all point one way. The
question that would send it to TOO HARD (NATURE), whether the next upturn restores the old margins, is asked of a
business that the same filings show losing the price, the brand and the trade customer; the rows do not wait for an
upturn to credit a castle shown open. "If we can think of very much that can go wrong with them, we just forget it."
**[M2000-016]**.

- **VERDICT: OUT.** The deciding part's castle is shown on the evidence to be filling in: price set by trade customers
  and rivals, brand values written down by their owner, attackers with money inside the home market, protection that
  depends on tariffs, and a margin narrowing every year from 2021 to 2026 **[M2011-015]**, **[M2005-020]**,
  **[M2001-090]**, **[M1999-108]**; and the field's durable players earn only ordinary returns over the last full cycle
  **[L2007-004]**, **[M2013-052]**. Price does not reopen it: "What you can’t do is turn any investment into a good deal
  by paying little" **[M2019-015]**.

## Q3: HOW MUCH CAPITAL MUST GO IN. WEIGHING.
NOT REACHED (Q2 closed the file OUT; operator rule 2). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 because the file closes before Q4; facts found are under AFTER THE STOP.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. The proxy was fetched and not read.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. WEIGHING.
NOT REACHED. The buyback test against the bottom of the Q7 range is not run, since Q7 is not reached; facts found are
under AFTER THE STOP.

## Q7: WHAT IS IT WORTH. STOP.
NOT REACHED as a question. The owner's reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8, Q9, Q10, Q12
NOT REACHED.

---
## THE BOX
**OUT at Q2**: the deciding part, North America major appliances (about three quarters of five-year segment EBIT), has a
castle shown on the evidence to be filling in, and the field's durable players earn only ordinary returns over the last
full cycle. Not TOO HARD: the deciding question was answered from the filings, so no cause is named and no research pass
is opened. Q7 not reached; the computation below sits beside the price and is not a range in the box. No integrity facts
were found before the stop (the proxy was not read), so no integrity flag is carried.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged **[M1997-127]**.
- **Bears on Q3 (capital).** Goodwill and intangibles ($5.7 billion at 2025) exceed equity ($2.7 billion) at every
  year-end from 2018; tangible equity is negative. Capital spending of $389 to $684 million a year over 2016 to 2025
  against depreciation and amortization of $333 to $655 million (ten-year averages $536 million and $511 million); the
  10-K gives no maintenance figure. InSinkErator bought for $3.0 billion cash in 2022. Source: companyfacts series; the
  10-Ks above.
- **Bears on Q4 (accounts).** A restructuring charge in every year 2010 to 2025 (from $16 million to $288 million), about
  $175 million expected for 2026 (Q2 10-Q), and the Supsa refrigeration plant closure announced 2026-07-01 at about $165
  million (about $95 million impairment, $70 million cash; 8-K `0000106640-26-000052`). The FY2025 10-K features "free
  cash flow" and a segment EBIT that excludes "restructuring costs, asset impairment charges and certain other items";
  the company guides EPS (10-K and Q2 10-Q). Retained earnings fell $6,340 million in 2024 by a treasury-stock retirement
  (the filed equity statement), not a loss. The cash-flow line "Share based compensation and other" (137 / 91 / 34 for
  2025 to 2023) differs from the stock-pay expense (28 / 28 / 33); the difference is "other", not identified.
- **Bears on Q5 (people).** Marc Bitzer, chairman and CEO, an executive officer since 2006; a CFO who became an executive
  officer in 2026 (10-K executive officers table; the item 5.02 8-Ks of 2026-03-16, 2026-04-01 and 2026-04-03 not read).
  The 2026 EPS outlook was cut from about $6.25 (10-K, filed 2026-02-11) to $2.25 to $2.75 (Q2 10-Q, filed 2026-08-04).
  No fact bearing on integrity was found in what was read.
- **Bears on Q6 (money and owners).** Buybacks of $5,316 million from 2013 to 2024 (including $1,944 million in 2021 and
  2022) and dividends of $4,439 million from 2010 to 2025, together more than the $7,730 million of net income summed
  over 2010 to 2025 (companyfacts series). Then: the quarterly dividend cut from $1.75 to $0.90 in the second half of 2025
  (10-K), 7,898,550 common shares sold at $69 and the 8.50% mandatory convertible issued on 2026-02-27, and the common
  dividend suspended in the second quarter of 2026 (Q2 10-Q). A Schedule 13D was filed on 2026-03-03 by Appaloosa LP
  (accession `0001493152-26-008749`, index page only read).
- **Bears on Q9 (debt).** Borrowings $7,068 million and cash $1,239 million at 2026-06-30 (net $5,829 million), plus
  noncurrent lease liabilities of $989 million; $2 billion of senior secured second-lien notes due 2031 and 2034 and a $2
  billion asset-based facility on receivables, inventory, intellectual property and equipment (8-K of 2026-06-16); senior
  unsecured ratings cut to Ba3 (Moody's) and BB- (Fitch) in 2026; $745 million of bank guarantees, letters of credit and
  surety bonds, mainly for Brazilian tax matters; Lowe's 44% of receivables. Pre-tax earnings plus interest over interest:
  2025 (516 + 341) / 341 = 2.5 times; first half 2026 (45 + 140) / 140 = 1.3 times (10-K; Q2 10-Q).

## COMPUTATION, NOT A CLEARANCE
*(The owner's two reporting figures, built by Q7's construction after a closing STOP; not a judgment of value, no entry
language. Script and output: `scripts/valuation.py`, `valuation_output.txt`.)*

**Inputs.** Owner cash after every real cost: OCF less stock-pay expense less all capital spending (Step 0 table).
**Specific (a), the cycle:** the last year of the literal window (2025, owner cash $53 million) is a trough the filer
ties to tariffs, lower earnings and product-transition inventory, and its first year (2021) sits in the 2020 to 2022
period the FY2022 10-K says "differed from historical periods due to the COVID-19 pandemic"; the base is therefore the
decade 2016 to 2025, which runs from before that peak to the trough after it. **CONVENTION of this run:** the decade is
taken as one full cycle and growth is measured between its two halves; rationale: the filings give no cycle dates, and
the peak and trough are the filer's own. **Specific (c), acquisitions:** cash paid for businesses, less proceeds from
sales of assets and businesses, less cash left in divested businesses (filed lines; 2016 and 2017 proceeds not read,
taken as nil), sums to $1,990 million over the decade, under half of owner cash before purchases ($6,368 million). So it
is not a serial acquirer, and the default pair is central (purchases deducted, total growth credited), with the organic
pair beside. The retained 40% of Whirlpool India and the Beko stake sold in 2026 are not credited separately; their cash
is inside the history. **Specific (b), decline:** on the default pair the halves run from $944.6 million a year (2016 to
2020) to $(69.0) million (2021 to 2025); the series changes sign, so the range is the no-growth case alone, said so. On the
organic pair the halves run from $659.0 million to $614.6 million, a decline of 1.39% a year, carried as the bottom.
**Specific (d):** working capital is inside OCF. **Specific (e):** the filing gives no maintenance figure, so the
all-spending case stands; the depreciation variant would add about $25 million a year (capex $536 million average
against D&A $511 million). **Specific (f):** no growth is carried, so no cap applies. **Tax:** the company's own, inside
OCF; interest added back after a 25% rate for the all-equity basis (**CONVENTION of this run**; rationale: it is the
company's own "anticipated tax rate is approximately 25%" from the FY2025 10-K, not a holder's rate). **Net debt:**
borrowings $7,068 million less cash $1,239 million at 2026-06-30 = $5,829 million; operating leases left out, said so;
the $212 million of notes discharged on 2026-07-01 lowered debt and cash alike. **Shares:** 73.532 million as-converted.
**Rate:** 5.43%.

| case (USD a share) | all-equity basis (central) | equity-only basis (beside) |
|---|---|---|
| owner cash, a year | default $614.1M; organic $813.1M | default $437.8M; organic $636.8M |
| **default pair, no-growth alone (central)** | **$74.54** | $109.65 |
| organic pair, bottom (-1.39% for ten years, then none) | $103.10 | $142.83 |
| organic pair, top (no growth) | $124.38 | $159.49 |
| literal window 2021 to 2025, default pair | $(43.88), nil | nil (owner cash after purchases negative) |

**(a) VALUE RANGE (COMPUTATION):** **$74.54 a share**, the no-growth case alone on the default pair (the series changes
sign, so no width can be shown), on the all-equity basis; organic pair beside, **$103.10 to $124.38**; equity-only
beside, $109.65 (organic $142.83 to $159.49). Against the price of **$27.89**.

**(b) FAIR PRICE (COMPUTATION):** each end valued at ten percent and the two averaged; the central default pair has one
case, so its fair price is that case at ten percent: **$4.25 a share** on the all-equity basis (the central figure), and
**$59.54** on the equity-only basis beside. Organic pair beside: all-equity ($31.31 + $21.47) / 2 = **$26.39**;
equity-only ($86.60 + $78.90) / 2 = $82.75. Against $27.89: the central case earns 7.8% a year at no growth on the
all-equity basis at the price (owner cash $614.1 million against $2,050.8 million of shares plus $5,829 million of net
debt), below the floor; the organic top case earns 10.3%.

**What the figures do not say.** The decade's average includes the European business disposed of at a $1.9 billion loss,
the Indian business now deconsolidated, and the pandemic peak. The latest year's owner cash was $53 million, and the
company's own 2026 outlook (OCF about $700 million less capex about $400 million) implies about $272 million on the
equity basis; both are far below the averages used. The gap between the all-equity and equity-only figures is the debt:
the lenders take the first $5.8 billion of the business.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 23d4b56e); written question by question; committed after Step 0
      and Q1 (ad6bbabf), after Q2 (ecbab7a0), and after the close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is held by the dispatching session; the
      fold is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen unasked (commit
      subjects naming another company, memory index lines) is declared above and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `scripts/check_cites.py`); every filing fact carries
      its accession or names its filing; the Electrolux figures name their source file. No E-ids.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and the figures after it are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): OCF less the filed stock-pay expense
      less all capital spending, purchases deducted on the default pair. The sovereign from the US Treasury. The price is an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations, and weighed at Q2); facts for later questions are under
      AFTER THE STOP; no integrity facts found, so no flag.
- [x] Not a point-in-time run; no row is barred by the anchor rule.
- [x] Only the arithmetic lines of `tools/run.py` were used; its stock-pay column was found to be the "and other" line
      and was replaced by the filed expense; its yields and means were not used.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Honest gaps: Haier, Samsung and LG, the rivals that matter most in North America, were not read from their own
  filings; the full Electrolux annual report could not be downloaded, only its published data workbook; the proxy, the
  Q2 earnings-release exhibit and the item 5.02 8-Ks were not read (not reached); 2016 and 2017 divestiture proceeds were
  not read and were taken as nil in the computation.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **"Ordinary returns" names no capital.** Q2's "standing castle that protects only ordinary returns" is judged in
words, but the text does not say on which capital: Q3 measures "the capital actually needed" (tangible), while the
owner's experience is the return on what was paid (equity plus debt, here mostly purchased goodwill and brands). For
Whirlpool the two readings differ sharply: on tangible capital its North America earned high returns before 2022; on
the capital its owners put in, the decade's return was about 9% after tax. I judged the field on the owners' capital and
on margins, said so, and rested the OUT chiefly on the evidence of the castle filling in, which does not depend on the
choice. (2) **The competitor row when no named rival files with the SEC.** None of the nine rivals the 10-K names files
with the SEC. I used one rival's own published financial data and flagged the rest; the framework does not say whether a
foreign rival's own reports satisfy "their own filings", or what to do when the rivals that matter most (Haier, Samsung,
LG) publish only in other forms. (3) **The cycle in specific (a) has no dates.** The text asks for "the last full cycle,
peak to peak or trough to trough" but gives no way to date a cycle when the filer names only one peak; I confessed the
decade as a CONVENTION of this run. (4) **Specific (b) with a sign change leaves a single point.** On the default pair the
range collapses to one case, so the width test has nothing to measure and the fair-price definition (two ends averaged)
reduces to one end; the text should say so. (5) **A mandatory convertible preferred** is not addressed in Q7's share count
or in net debt; I counted it as the common shares it must become at the maximum rate, a CONVENTION of this run. (6) **The
tool's stock-pay column** reads the cash-flow line "Share based compensation and other", here up to five times the filed
stock-pay expense; Part VII's tooling note warns of v4 rules, not of a mis-chosen line.
