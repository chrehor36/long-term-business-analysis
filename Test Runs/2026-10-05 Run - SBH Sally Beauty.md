# Company Run: Sally Beauty Holdings, Inc. (NYSE: SBH), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch** (2026-10-05).
Working folder: `Test Runs/_research 2026-10-05 SBH/` (fetch helper, filing texts, the arithmetic scripts and their output).

**POSITION NOTE, declared before any verdict:** not checked. This is a blind run; `PORTFOLIO.md` was not opened, by instruction.

**CONTAMINATION, declared.** (1) A directory listing of `Test Runs/` showed two older file names that name SBH: a 2026-07-16 "Consumer & Leisure 6-pack" run and a 2026-07-17 "Pre-Entry Verification" file. Neither was opened; their verdicts are unknown to me. (2) The same listing showed the names of other companies' 2026-10-05 run and research-pass files; none was opened. (3) The session's git snapshot showed five recent commit subjects about other names (INVA, PBH, RHI, SKYW and a session-state note); none mentions SBH. (4) `tools/run.py` prints v4 material; only its arithmetic lines were read (Part VII). Nothing else of the blind list was opened.

**Session note.** The run was written in one working session that crossed midnight into 2026-10-06; every price, rate and filing fact is as of 2026-10-05. Nothing was committed, by instruction, so the write-early "commit after each question" step of the self-audit was not done.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $16.06 (2026-10-05, via `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class**, from the latest filing's cover: one class, Common Stock $0.01 par, **93,622,292** shares as of 2026-07-30 (10-Q for the quarter ended 2026-06-30, filed 2026-08-03, accession `0001368458-26-000007`; `python Screens/cover_shares.py SBH`). The balance-sheet count at 2026-06-30 is 94.092M; the cover count is used.
- **Market cap:** 93.622M x $16.06 = **$1,504M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 2026-10-05 (issuing authority, via `tools/sources.py` as called by `tools/run.py`).
- **Filings read** (operator rule 4):
  - 10-K for FY2025 (year ended 2025-09-30), filed 2025-11-13, accession `0001193125-25-280122`: Item 1 (business, stores, merchandise, competition, suppliers), Item 1A (competition, suppliers, exclusive rights, diversion), Item 7 (results, comparable sales, contractual obligations), balance sheet, cash flow.
  - 10-Q for the quarter ended 2026-06-30, filed 2026-08-03, accession `0001368458-26-000007`: segment table, comparable sales, cash flow, debt note, repurchase note.
  - DEF 14A filed 2025-12-10, accession `0001193125-25-313464`: pay table, AIP and PSU metrics, beneficial ownership, board leadership, pay ratio.
  - 8-K of 2026-08-03 (accession `0001368458-26-000004`), Exhibit 99.1, Q3 FY2026 results and FY2026 guidance.
  - 8-K of 2026-03-17 (accession `0001193125-26-109350`): a director (Erin Nealy Cox) resigned to join Walmart, Inc.
  - 8-K of 2026-04-02 (accession `0001193125-26-138926`): the CFO (Marlo Cormier) left by mutual agreement with a separation payment of $881,250 (15 months' salary), effective 2026-04-11; Adrianne Lee (previously President and CFO of Bed, Bath & Beyond [NYSE: BBBY]) appointed CFO from 2026-04-28, with a $1,850,000 supplemental equity grant and a $175,000 sign-on bonus.
  - Older 10-Ks for the long record: FY2007 (`0001047469-07-009602`), FY2010 (`0001047469-10-009883`), FY2015 (`0001047469-15-008573`), FY2016 (`0001047469-16-016713`), FY2018 (`0001564590-18-029551`), FY2019 (`0001564590-19-044262`), FY2020 (`0001564590-20-054910`), FY2022 (`0001564590-22-037949`), FY2024 (`0000950170-24-127217`).
- **One figure cross-checked against the filed statement:** total stockholders' equity at 2025-09-30, **$794,207 thousand** on the filed balance sheet of the FY2025 10-K (`0001193125-25-280122`), against 794 in the `tools/run.py` ten-year table. Agrees. Total assets ($2,871,096K) and inventory ($987,575K) also agree.
- **`tools/run.py SBH`, arithmetic lines only** (USD millions; OE capex = OCF less SBC less capex; OE D&A = OCF less SBC less D&A):

  | FY (Sept) | OCF | SBC | D&A | capex | OE capex | OE D&A |
  |---|---|---|---|---|---|---|
  | 2021 | 381.9 | 11.7 | 102.2 | 73.9 | 296.3 | 268.0 |
  | 2022 | 156.5 | 9.9 | 99.9 | 99.2 | 47.4 | 46.7 |
  | 2023 | 249.3 | 15.9 | 102.4 | 90.7 | 142.7 | 131.0 |
  | 2024 | 246.5 | 17.2 | 109.7 | 101.2 | 128.2 | 119.6 |
  | 2025 | 274.8 | 19.2 | 99.9 | 102.1 | 153.4 | 155.7 |
  | **five-year mean** | | | | | **153.6** | **144.2** |

  SBC is the `ShareBasedCompensation` tag in each year, complete; the tool found finance-lease principal of $0.1M to $0.2M a year as the only other capital payment (immaterial). The FY2021 and FY2022 lines are abnormal and offset each other (FY2021 the stimulus year, comparable sales +9.6%; FY2022 an inventory build, OCF $156.5M); see Q7's whole-cycle variant. Nine months of FY2026 (10-Q above): OCF $247.5M, capex $84.3M, SBC $18.1M.
- **The balance sheets, read first** (the Q4 rule **[M2025-032]**, "balance sheets over an 8 or 10 year period"; done here because the file closes before Q4). From the `tools/run.py` table, first-filed XBRL, checked at FY2025 against the filed statement (USD millions):

  | Sept 30 | assets | equity | cash | inventory | goodwill + intangibles | long-term debt | retained earnings |
  |---|---|---|---|---|---|---|---|
  | 2016 | 2,132 | -276 | 87 | 907 | 626 | 1,800 | -178 |
  | 2017 | 2,123 | -364 | 64 | 931 | 618 | 1,891 | -283 |
  | 2018 | 2,097 | -269 | 77 | 944 | 609 | 1,795 | -180 |
  | 2019 | 2,098 | -60 | 71 | 953 | 593 | 1,609 | 56 |
  | 2020 | 2,895 | 15 | 514 | 815 | 598 | 1,813 | 117 |
  | 2021 | 2,847 | 281 | 401 | 871 | 597 | 1,393 | 357 |
  | 2022 | 2,577 | 294 | 71 | 936 | 576 | 1,087 | 440 |
  | 2023 | 2,725 | 509 | 123 | 975 | 588 | 1,078 | 625 |
  | 2024 | 2,793 | 629 | 108 | 1,037 | 598 | 994 | 741 |
  | 2025 | 2,871 | 794 | 149 | 988 | 594 | 875 | 898 |

  What moved and why. **Equity was negative from the spin to FY2019**: the business was separated from Alberto-Culver on 2006-11-16 with about **$1,850.0 million** of new debt, the proceeds of which, with $575.0 million of equity from Clayton, Dubilier & Rice funds (about 48%), went to the old parent's holders (FY2007 10-K, `0001047469-07-009602`). Debt then stayed near $1.8 billion for twelve years, not because the business could not pay it down but because about **$2.0 billion of stock was bought back in FY2012 to FY2018** (81.1 million shares for $1,989.9 million, an average of about $24.5 a share; the yearly counts and costs are in the FY2015, FY2016 and FY2018 10-Ks). From FY2019 the cash went to debt instead: long-term debt fell from $1,800M (2016) to $875M (2025) and to **$815M of principal at 2026-06-30** ($600M senior notes due 2032, $215M term loan B due 2030; cash $173M; ABL undrawn). Retained earnings went from -$178M to +$898M as buybacks slowed. Goodwill and intangibles are flat near $600M: no large acquisitions in ten years, only small distributor tuck-ins. **Inventory rose while sales fell**: $907M against sales of $3,953M in FY2016 (23%), $988M against $3,701M in FY2025 (27%); the FY2024 10-K puts the rise on "expanded distribution rights in BSG and vendor price increases". What the table does not show: **operating lease liabilities of $697M** at 2025-09-30 ($158.6M current, $538.4M long-term; $884M undiscounted), since every store is leased; the lease is a fixed charge senior to the owners as surely as the notes. What the figures cannot say: whether the BSG supplier relationships behind that inventory will be there in five years, which is Q2's question.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would own this if "the market closed for five years" **[M1997-109]**, which turns the run to what the 4,400 stores and the supplier contracts will earn, not to the quote. The market serves and "just tells us prices" **[M2006-077]**; a $16.06 quote that is a third of the 2013 level instructs nothing. The analyst's habits govern the hunt: the list of "What do I not know that I need to know?" **[M1999-129]** was written first (below), and the reading was aimed "to possibly reject your original hypothesis" **[M1998-144]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) FY2025 10-K, Item 1A: "there are few significant barriers to entry into the marketplace for most of the products we sell, making it easy for new market entrants to compete with us" (the filer's own words, `0001193125-25-280122`); (2) supplier contracts "can be terminated without cause upon 90 days' notice or less" (same filing; the same words in the FY2010 10-K); (3) L'Oreal, BSG's largest supplier in 2006, "moved a material amount of revenue out of the BSG nationwide distribution network" and then "acquired distributors competing with BSG" (FY2010 10-K, `0001047469-10-009883`); (4) Sally's FY2024 comparable-sales decline "was a result of fewer transactions", and FY2025's small gain came from "average unit retail, driven by inflationary impacts and pricing leverage, partially offset by fewer average number of units per transaction and a decrease in the number of transactions" (FY2024 and FY2025 10-Ks); (5) BSG comparable sales -2.1% in Q3 FY2026 with "a decrease in the number of transactions" (10-Q `0001368458-26-000007`); (6) the CFO left in April 2026 after two years in the seat, with a separation payment. Evidence for the business, written down the same way: owned brands are about 35% of Sally sales (FY2025 10-K); hair color and care are about 70% of consolidated sales; gross margin rose from 50.9% (FY2024) to 51.6% (FY2025) and 52.4% (Q3 FY2026); BSG keeps winning distribution of newer brands (K18, Amika, Moroccanoil, Color Wow); 15 million active Sally customers in the U.S. and Canada.

**What I did not know and needed to know, written before the reading:** (a) the comparable-sales record by segment over the whole span, not one year; (b) whether brand owners have taken lines away from BSG or gone direct, and on what contract terms BSG holds them; (c) whether Sally's DIY color customer is leaving for Amazon, Ulta or mass; (d) what a competitor earned over the same span; (e) where the cash went after the spin. Each is knowable from filings; each was read.

## THE STANDING RULE
Owning a small, unlevered position in SBH puts the buyer at no risk of ruin; the rule governs the buyer's financing and sizing, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt and leases belong to Q9 (NOT REACHED).

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as stated:** "what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**.
- **What the business is** (FY2025 10-K): two segments that sell other people's beauty products plus some owned brands. **Sally Beauty** (net sales $2,094M FY2025; segment operating earnings $327M): about 3,100 stores of about 1,700 square feet, mostly strip centres, selling up to 7,000 items to do-it-yourself consumers and stylists; owned brands about 35% of sales. **Beauty Systems Group** (net sales $1,607M; segment operating earnings $196M): about 1,330 Cosmo Prof and Armstrong McCall stores and 591 salon consultants selling only to licensed professionals, "many of which have exclusive distribution rights with us". The five largest suppliers (Henkel, L'Oreal Professional, Wella, John Paul Mitchell Systems, Kao) were about 48% of merchandise purchases in FY2025, against about 39% in FY2010 and FY2015.
- **The key variables** **[M1998-044]**: (1) the terms on which brand owners keep supplying BSG, and whether they sell around it; (2) whether the DIY color customer keeps coming to a Sally store; (3) transactions per store. None is technology; all are the behaviour of suppliers and customers, which the rows say can be projected **[M2023-030]**. The financial statements over twenty years show these variables plainly (comparable sales, store count, margin), so past statements do tell me what the future ones depend on **[M2008-033]**.
- **The perimeter.** Retail is the arena the rows name as the one where understanding is easiest to overrate: it is easy to "think you understand retail" and then find out otherwise **[M2014-052]**. I hold the business inside the circle only to the extent of the claim Q1 requires: the economics are a distributor's spread on products it does not make, and the forces that set that spread are named in the filer's own risk factors and visible in its record. Whether that spread will hold is the castle question, and the routing sends it to Q2 rather than closing here: the industry does not change by fast technology **[M1998-008]**, and the change it does undergo (brand owners and retailers fighting over the intermediary's margin) is a slow change the rows treat as a castle question **[M2006-091]**, **[M2019-014]**.
- **Do I doubt it is inside?** "if you have doubts about something being into your circle of competence" **[M2002-092]** it is not. My doubt is not about what the business is or what drives it; it is about whether it is protected. That doubt is answered by evidence at Q2, not by the circle.
- **VERDICT: IN**, narrowly, on the record above **[M2012-065]**, **[M1998-044]**, with the warning of **[M2014-052]** carried to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, asked from the attacker's side, since "competitors will repeatedly assault" any castle earning high returns **[L2007-004]**.

**The record over the whole span, from the filer's own 10-Ks.** Comparable (same-store) sales, percent, by fiscal year:

| FY | Sally | BSG | Consolidated | source |
|---|---|---|---|---|
| 2006 | 2.4 | 4.1 | 2.8 | FY2010 10-K |
| 2007 | 2.7 | 10.1 | 4.5 | FY2010 10-K |
| 2008 | 1.2 | 6.9 | 2.6 | FY2010 10-K |
| 2009 | 2.1 | 1.0 | 1.8 | FY2010 10-K |
| 2010 | 4.1 | 6.2 | 4.6 | FY2010 10-K |
| 2011 | 6.3 | 5.5 | 6.1 | FY2015 10-K |
| 2012 | 6.5 | 6.1 | 6.4 | FY2015 10-K |
| 2013 | -0.6 | 4.2 | 0.8 | FY2015 10-K |
| 2014 | 1.3 | 3.5 | 2.0 | FY2015 10-K |
| 2015 | 1.7 | 5.7 | 2.9 | FY2015 10-K |
| 2016 | 1.7 | 5.5 | 2.9 | FY2020 10-K (BSG 5.5 confirmed in FY2016 10-K) |
| 2017 | -1.6 | 1.3 | -0.7 | FY2020 10-K |
| 2018 | -1.5 | -1.5 | -1.5 | FY2020 10-K |
| 2019 | 0.4 | 0.2 | 0.3 | FY2020 10-K |
| 2020 | -8.1 | -8.3 | -8.1 | FY2020 10-K (COVID closures) |
| 2021 | 9.1 | 10.3 | 9.6 | FY2022 10-K |
| 2022 | -0.6 | 2.3 | 0.6 | FY2022 10-K |
| 2023 | 3.4 | -1.3 | 1.4 | FY2024 10-K |
| 2024 | -0.7 | 1.6 | 0.3 | FY2024 10-K |
| 2025 | 0.4 | 0.2 | 0.3 | FY2025 10-K |
| 9 mo. FY2026 | 1.4 | -0.9 | 0.4 | 10-Q `0001368458-26-000007` |

The record breaks in FY2013 (Sally) and FY2017 (BSG). From FY2017 to FY2025 the consolidated figures sum to about +2% in nine years, in nominal dollars, through years in which the filer says its unit prices rose with inflation; and the filer says transactions fell (Sally FY2024 and FY2025; BSG Q3 FY2026). **Stores** (including franchises): 4,309 (FY2011), 4,967 (FY2015), 5,156 (FY2018, the peak), 5,038 (FY2020), 4,422 (FY2025), 4,386 (2026-06-30). **Net sales**: $2,648M (FY2008), $3,953M (FY2016, the peak), $3,701M (FY2025). **Operating earnings**: $520M (FY2013, 14.4% of sales) to $328M (FY2025, 8.9%, and that figure includes a $26.6M gain on the sale of the headquarters). The FY2013 to FY2025 operating earnings fell by about 37% while the number of shares fell by about 41%.

**The castle tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**: "could I do it?" It was done. L'Oreal, BSG's largest supplier, "moved a material amount of revenue out of the BSG nationwide distribution network and into competitive regional distribution networks" in December 2006 and then "acquired distributors competing with BSG" (FY2010 10-K, `0001047469-10-009883`); the FY2015 10-K (`0001047469-15-008573`) says L'Oreal "directly competes with BSG" and that BSG's rights to Matrix ran only "through December 2018". The rival built (SalonCentric, L'Oreal's own distributor) is not an SEC filer; its sales and margins could not be read (flagged). "one competitor is frequently enough to ruin a business" **[M2012-108]**.
2. **Who holds the switch** (the supplier side of the castle). Contracts are "at-will" or "can be terminated without cause upon 90 days' notice or less", and suppliers "may seek to decrease their reliance on distribution intermediaries ... by promoting their own distribution channels" and "may offer advantages, such as lower prices, when their products are purchased from distribution channels they control" (FY2025 10-K, Item 1A). The concentration of purchases in five suppliers rose from about 39% (FY2010, FY2015) to about 48% (FY2025). The rows describe exactly this fight and say who has been winning it: "those intermediaries are trying to make money" **[M2019-041]**; "the struggle between the manufacturers of brands and retailers will go on" **[M2006-091]**. A distributor whose product belongs to the other party, on ninety days' notice, is the intermediary in that fight, not the brand.
3. **Pricing power, and the agony before a rise** **[M2005-020]**: "a prayer session before you raise your prices a penny". The filer: competition "may require us to reduce prices to retain business", customers "comparison-shop" with "real-time product availability", leading "to decisions driven solely by price" (FY2025 10-K, Item 1A). The recent unit-price gains came with fewer transactions, which is the opposite of the test's pass, "charge more for a product and maintain or increase market share" **[M2000-031]**.
4. **Would the customer still choose it over the low bid** **[M2017-009]**: for the third-party half of the shelf, the same Wella, L'Oreal and Paul Mitchell products are on Amazon, Walmart.com and Ulta (Sally itself sells through "Amazon, Walmart.com, DoorDash, Uber Eats, and Instacart", FY2025 10-K), and BSG's "Diversion of professional products" risk factor records salon-only goods leaking to general merchants. For the owned-brand third of Sally's sales, the filer offers its own belief that they "offer equal or better quality than leading third-party brands"; no filing figure shows customers asking for them by name. Where the retailer is trusted as much as the brand, "the value of having the brand moves over to the retailer" **[M2001-090]**, and here the intermediary is the smaller party on both sides.
5. **Share of mind and unit volume** **[M1997-099]**: transactions falling and stores closing for eight years. The positive fact, hair color's strength in every recent quarter, is real but has not turned the total.
6. **The low-cost position** **[M2018-043]**: no filing fact shows SBH as the low-cost route from the brand to the salon or the home; the filer names "efficiency of distribution networks" as a competitive factor and is running a cost programme ("Fuel for Growth") to restore margin, not to pass a cost advantage on.
7. **Retail's own test.** "In retailing, to coast is to fail." **[L1995-008]**; "Your competitor is always copying and then topping whatever you do." **[L1995-008]**; "retailing is a good case of a business where you have to stay smart" **[M1995-040]**. The filer's strategy is a series of rebuilds: the 2023 Distribution Center Consolidation and Store Optimization Plan (294 Sally stores closed in FY2023), "Fuel for Growth" since FY2024, "Sally Ignited" (pivoting "from a 'beauty supply house' to a modernized specialty beauty retailer"), the Happy Beauty Co. test. "A moat that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**
8. **Ask the competitors; the competitor row** (same metric, competitors' own filings):

| | span | net sales | operating margin | comparable sales |
|---|---|---|---|---|
| **SBH** (10-Ks above; XBRL first-filed) | FY2013 to FY2025 | $3,622M to $3,701M | 14.4% to 8.9% | positive in 13 of 20 years FY2006-25; 9-yr FY2017-25 sum about +2% |
| **Ulta Beauty** (ULTA; 10-K FY2014 `0001193125-15-115602`, FY2019 `0001558370-20-003272`, FY2025 `0001104659-26-035243`; XBRL first-filed) | FY2012 to FY2025 (years ending Jan/Feb) | $2,220M to $12,393M | 12.6% to 12.4% (peak 16.1% in FY2022) | +11.9, +11.5, +9.3, +7.9, +9.9 (FY2010-14); +8.1, +5.0 (FY2018-19); +5.7, +0.7, +5.4 (FY2023-25) |
| **SalonCentric** (L'Oreal) | not an SEC filer | not read (flagged) | not read | not read |
| **Walmart** (10-K filed 2026-03-13, `0000104169-26-000055`) | | beauty is inside "health and beauty aids" within grocery; no instance found of a beauty sales figure (text sweep for "beauty") | | |
| **Amazon** (10-K filed 2026-02-06, `0001018724-26-000004`) | | no instance found of the word "beauty" (text sweep) | | |

Ulta's haircare category alone was 19% of $12.4B of sales in its FY2025 (about $2.4B), larger than the whole Sally segment ($2.1B). Over the span in which SBH's sales stood still and its margin fell by about a third, the specialty competitor in the same strip centres grew more than fivefold at a steady margin. Whose silver bullet hits whom **[M2017-022]** is not in doubt from these filings.
9. **Widening or narrowing** **[L2005-010]**: the position "grows either weaker or stronger" every day; the margin, the comparable-sales record, the store count and the transaction counts all read narrower from FY2013 (Sally) and FY2017 (BSG) on. The newspaper rows describe the shape: an industry that "has lost still another notch" **[L1995-023]**.
10. **What could destroy, modify or reduce it** **[M2000-014]**: the supplier going direct or to a rival distributor (has happened); the internet, of which the rows said in 1999 "the internet, in many forms of retailing, is likely to pose such a threat" **[M1999-013]** and in 2012 "terrible for most retailers" **[M2012-047]**; and the filer's own "few significant barriers to entry".

**The case for the castle, stated as well as I can** (the habit of stating the other side). Professional hair color is a category where the customer wants advice and the exact shade, and Sally is the place a home colorist goes; owned brands (35% of Sally) cannot be bought elsewhere; BSG is the largest North American full-service distributor and brand owners still hand it new lines; gross margin has risen three years running; the business throws off about $150M to $200M a year of owner cash on a $1.5B market value and has halved its debt. All true. None of it answers the attacker test: the products that make BSG are owned by suppliers who can leave on ninety days' notice and one of whom built a rival network; the products that make Sally are increasingly bought where its customers already shop; and the record shows the narrowing, not a stable fort.

**Hunting the other way, the TOO HARD question.** Is this a castle whose future cannot be judged (TOO HARD) rather than one shown filling in (OUT)? The rows send to TOO HARD the castle that is "tenuous" and cannot be valued **[M2000-019]**; they send to OUT the castle shown open on the evidence **[M2011-015]**. Here the evidence is not a forecast: it is twenty years of the filer's own numbers, a supplier that has already gone around it, contract terms that leave the switch with the supplier, and the filer's own statement that barriers are few. The deciding question was knowable, and the reading answered it. That is OUT, not TOO HARD; and a lower price does not reopen a castle shown open: no one can "turn any investment into a good deal by paying little" **[M2019-015]**; "If you really think a business is declining" **[M2012-062]**, avoid it.

- **VERDICT: OUT** at Q2. The castle is shown on the evidence to be filling in: the filer's "few significant barriers to entry", supplier contracts terminable on 90 days' notice, a supplier that has moved revenue out of BSG and bought competing distributors, nine years of flat nominal comparable sales with falling transactions, an operating margin down from 14.4% to 8.9%, and a direct competitor that grew fivefold at a steady margin over the same span. **[M1995-038]**, **[M2011-015]**, **[M2012-108]**, **[M2019-041]**, **[L1995-008]**, **[L2007-005]**, **[L2005-010]**, **[M2006-013]** ("three boxes at the company").

## Q3: HOW MUCH CAPITAL MUST GO IN. WEIGHING.
NOT REACHED (the file closed OUT at Q2). Facts gathered, not judged: capex $74M to $102M a year against D&A of about $100M to $110M (FY2021-25); inventory of about $1.0B carried against sales of $3.7B, rising as sales fell.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The balance sheets were read in Step 0. Facts gathered, not judged: a restructuring or "transformation" charge in most recent years (the Plan, then "Fuel for Growth" at $1.5M, $32.0M and $23.7M in FY2023, FY2024 and FY2025, per the proxy's reconciliation, `0001193125-25-313464`); the FY2025 adjusted operating income ($328.4M) nets the $26.6M headquarters gain against relocation costs and excludes the Fuel for Growth costs, so "adjusted" equalled GAAP that year by offset; the filer reports Adjusted EBITDA among its non-GAAP measures. The rows' tests on recurring charges **[L2016-007]** and the base year **[L2005-003]** would apply here if the file were open.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. Facts gathered, not judged: CEO Denise Paulonis since 2021, total FY2025 pay $9,112,619, a CEO pay ratio of 534:1 (proxy); directors and officers as a group own 2.0% including options; independent chair (Diana Ferguson); CFO departure in April 2026 with severance after about two years; a director left in March 2026 to join Walmart, Inc.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. WEIGHING.
NOT REACHED. Facts gathered, not judged: buybacks of 81.1 million shares for $1,989.9 million in FY2012 to FY2018 (about $24.5 a share on average) while debt from the spin stayed near $1.8B, against a price today of $16.06 and a range computed below of $14.57 to $28.99; repurchases at about $10 to $13 a share in FY2019-20 and FY2023-25; the programme authorised in 2017 for up to $1.0 billion names no price (10-Q). The rows' test is "what is smart at one price is dumb at another" **[L2011-003]**, and a programme that names no price above which "repurchases will be eschewed" **[L2016-002]** weighs against unless the prices paid sit at or below the bottom of the Q7 range. PSUs pay on one-year adjusted operating margin periods and relative TSR; the annual bonus on adjusted operating income and comparable sales (proxy).

---
## COMPUTATION — NOT A CLEARANCE
*(The file closed OUT at Q2. Everything below is arithmetic reported at the owner's request, not a clearance and not an entry price. Script and output: `Test Runs/_research 2026-10-05 SBH/value_calc.py`, `value_calc.txt`.)*

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The construction is the Part VI CONVENTION: five-year mean owner cash after every real cost, carried at the growth shown, ten years, then zero nominal growth, at the long government rate **[L2000-021]** ("What is the risk-free interest rate"), with the two ends the no-growth and shown-growth cases.

- **Owner cash base:** $153.6M (capex basis, the five-year mean) and $144.2M (D&A basis). Per share at 93.622M: $1.64 and $1.54.
- **Growth shown:** negative. The endpoint rate FY2021 to FY2025 is -15.2% a year, but FY2021 is an abnormal base year, the trap **[L2005-003]** names ("a base year in which earnings were poor", here the reverse). Measured instead on half-decade means (FY2016-20 mean $244.1M against FY2021-25 mean $153.6M), owner cash fell **-8.8% a year**; added back for the lower interest of the later years (25% tax), the unlevered fall is -8.3% a year. Since the shown growth is below zero, the "shown-growth" end is the bottom of the range and the no-growth end is the top (CONVENTION of this run: the framework's construction assumes the shown growth is at or above zero and does not say which end is which when it is not).
- **VALUE RANGE (five-year base, capex basis): $14.57 to $28.99 a share** ($1,364M to $2,714M) against **$16.06**. Width 1.99 to one, inside the three-to-one line. D&A basis: $13.68 to $27.21.
- **Whole-cycle variant** (the five-year window holds two abnormal years, FY2021 high and FY2022 low): ten-year mean owner cash FY2016-25 of $198.9M gives **$18.86 to $37.53**. It carries the years of higher interest and higher margins, so it flatters the present business; the five-year range is the one I would use.
- **FAIR PRICE** (the price at or below which the central case clears the ~10% pre-tax floor, the CONVENTION of Q7, "at least 10% pre-tax returns" **[L2002-020]**). Tax treatment: the floor is pre-tax, so the five-year owner cash after tax ($153.6M) is grossed up at the FY2025 effective tax rate of 25.6% ($67.5M on $263.4M) to $206.6M pre-tax. The floor is on **equity** (owner cash is after interest; the $815M of debt and $697M of leases stay in place). Central case: owner cash falling 2% a year in nominal terms (CONVENTION of this run: between the no-growth end and the shown decline, nearer the former because FY2023-25 owner cash has been flat at about $125M to $155M). Expected pre-tax return = yield + growth, so fair market value = $206.6M / (10% + 2%) = $1,721M, **about $18.40 a share**. At no growth it would be $22.06; at the shown -8.8% it would be $11.70.
- **CHEAP PRICE** (below which no pencil would be needed, **[M2009-005]**, "It should scream at you."). Rule, CONVENTION of this run: half the bottom of the five-year value range, so that even the shown decline is bought at a 50% discount, **about $7.30 a share**.
- **At $16.06**: after-tax owner-cash yield 10.2%, pre-tax 13.7%; the price sits just above the bottom of the range and below the fair price. On arithmetic alone it would clear the floor in the central case and would not be a screamer. None of this matters to the verdict: a castle shown open is not reopened by price **[M2019-015]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES. STOP.
NOT REACHED.

## Q9: COULD IT RUIN US. WEIGHING.
NOT REACHED. Facts gathered: $815M of debt principal (senior notes 2032, term loan B 2030), $697M of operating lease liabilities, $173M of cash, ABL facility of $500M undrawn (10-Q); net debt leverage 1.4x by the company's own adjusted measure (Exhibit 99.1).

## Q10: IS IT THE FAT PITCH. WEIGHING.
NOT REACHED. The draft would have the buyer do nothing: OUT at Q2 is not a pitch.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked (operator's option). Nothing in the filings read names a business on the Q12 list.

---
## THE BOX
**OUT**, decided at **Q2**: the castle is shown on the evidence to be filling in (the filer's "few significant barriers to entry"; supplier contracts terminable on 90 days' notice and a supplier that has already gone around BSG; nine years of flat nominal comparable sales with falling transactions; operating margin 14.4% to 8.9%; Ulta grew fivefold at a steady margin over the same span). Not TOO HARD: the deciding question was knowable and was answered from the filings. Computation only: value range $14.57 to $28.99 (whole-cycle $18.86 to $37.53) against $16.06; fair about $18.40; cheap about $7.30.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed after each question**: the brief forbade commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id checked against that row); every filing fact has its accession; no number without a row, a filing, or a CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; Q3 to Q10 are NOT REACHED; the Q7 figures are headed COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost (OCF less SBC less capex, D&A variant beside it), never a net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, in the foundations, before Q1.
- [x] No row dated after the anchor is cited (the run is dated today; not a point-in-time test).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS (run after the file was written; result in the reply).
- Honest notes: the 2016 comparable-sales figures for Sally and the consolidated total were taken from the FY2020 10-K's five-year table and only BSG's 5.5% was confirmed in the FY2016 10-K itself; the SalonCentric side of the competitor row is missing (non-SEC); the FY2012-18 average buyback price is the filed cost divided by the filed share counts.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **The Q7 range construction assumes growth at or above zero.** The CONVENTION names "the no-growth case and the shown-growth case" as the ends and caps growth from above, but says nothing for a business whose owner cash has shrunk; here the shown-growth case is the bottom, and I had to choose which end is which, and also how to measure "growth shown" when the five-year window opens on an abnormal year (I used half-decade means, a choice the convention does not make). A sentence saying that a negative shown rate makes the shown-growth case the bottom, and that an abnormal first or last year is replaced by a half-period mean, would remove two choices. (2) **OUT against TOO HARD at Q2 turns on "shown on the evidence" against "cannot be judged", with no line between them.** A declining castle is always partly a forecast. I drew the line at evidence already in the filings (a supplier that has gone around the business, contract terms that leave the switch with the supplier, the filer's own statement on barriers, and a decade-long record); another analyst could call the same facts "tenuous" **[M2000-019]** and close TOO HARD. The framework should say whether a castle whose decline is observed but whose floor is unknown is OUT or TOO HARD. (3) **The fair and cheap prices asked for by the owner have no rule in the framework**: the "central case" growth for the fair price and the discount for the cheap price are mine and are confessed as CONVENTIONs of this run. Minor: the template's Q4 line asks for eight to ten years of balance sheets, and on a file that closes at Q2 the instruction to read them in Step 0 came from the brief, not from the template.
