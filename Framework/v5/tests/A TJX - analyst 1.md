# A' TJX, analyst 1: The TJX Companies, Inc. (NYSE: TJX) under the v5 purchase draft

Test A' (reproducibility), 2026-10-04. Run under `Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md` against `Framework/v5/DRAFT - THE FRAMEWORK v5.md`. This run binds nothing and changes no verdict of record. The operator does not hold TJX: Q11 is not answered; Q12 is. Working files: `Framework/v5/tests/_work_A1_TJX/`.

Filings read (all SEC EDGAR, CIK 0000109198 unless stated):

| short name | document | filed | accession |
|---|---|---|---|
| 10-K FY26 | Form 10-K, fiscal year ended 2026-01-31 (tjx-20260131.htm) | 2026-03-31 | 0000109198-26-000008 |
| 10-Q Q2 FY27 | Form 10-Q, quarter ended 2026-08-01 (tjx-20260801.htm) | 2026-08-28 | 0000109198-26-000048 |
| Proxy 2026 | DEF 14A (tjx-20260430.htm) | 2026-04-30 | 0000109198-26-000015 |
| 8-K Q2 FY27 | earnings release exhibit (tjxq2fy27earningspressrele.htm) | 2026-08-19 | 0000109198-26-000045 |
| 8-K headlines | earnings release exhibits, Q4 FY24 to Q1 FY27 (headline lines only) | 2024-02-28 to 2026-05-20 | 0000109198-24-000010, -24-000031, -24-000044, -24-000056, -25-000006, -25-000037, -25-000051, -25-000058, -26-000004, -26-000023 |
| Ross 10-K | Ross Stores, Form 10-K, fiscal 2025 ended 2026-01-31 (rost-20260131.htm), CIK 0000745732 | 2026-03-31 | 0000745732-26-000006 |
| Burlington 10-K | Burlington Stores, Form 10-K, fiscal 2025 ended 2026-01-31 (burl-20260131.htm), CIK 0001579298 | 2026-03-19 | 0001193125-26-116001 |
| XBRL (screening only) | companyfacts, older years: FY2015 pretax (0001193125-16-521424), FY2020 and FY2021 revenue and pretax (0000109198-21-000006) | | flagged: tagged data, transcription |

---

## 0. Step 0

- **Price:** $132.68, close 2026-10-02. Source: aggregator (as supplied for the test, and as `tools/run.py` reports it). **Flagged: aggregator, live quote only.**
- **Share count by class, from the latest filing's cover:** Common Stock, par value $1.00, **1,099,974,061** shares. 10-Q Q2 FY27, filed 2026-08-28, accession 0000109198-26-000048 (`python Screens/cover_shares.py TJX`). One class.
- **Market cap:** 1,099,974,061 x $132.68 = **$145.9 billion** (`tools/run.py` gives 145.94B on 1,100.0M shares).
- **Sovereign for the earnings currency (USD; 78% of FY26 revenue is U.S., 10-K FY26, Revenues by Geography):** US Treasury 30-year par yield **5.63%**, 10/02/2026, US Treasury daily par yield curve (issuing authority).
- **Cross-check of one figure against the filed statement:** net cash provided by operating activities FY26 = $6,874 million in the 10-K FY26 cash-flow statement (0000109198-26-000008), equal to the `run.py` figure of 6,874. Also equal: SBC 214, D&A 1,247, capex 1,957.

## 1. The foundations

Five foundations bear on this name. **A share is a business:** the question is whether I would be content to own TJX "if the market closed for five years" **[M1997-109]**, which turns the work to the stores and the buying organisation, not the quote. **Margin of safety:** "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**; this is decisive at Q7 below. **Who is paid to tell you:** TJX publishes quarterly earnings guidance and eleven consecutive release headlines report results "above plan" (section 3, Q4); the foundation warns that information reaching the investor is shaped by who is paid **[M2020-037]**, and I read the filings, not the plan. **Macro kept out:** the filings are full of tariffs, the IEEPA ruling and consumer spending; none of it enters the judgment beyond what it shows of the business **[M2000-094]**. **The analyst's habits:** the contrary evidence (the FY2021 year in which pretax income fell to about $89 million on $32.1 billion of revenue, XBRL 0000109198-21-000006, flagged; and the eleven "above plan" headlines) is written down at once rather than explained away **[M1997-127]**. Nothing here admits or rejects the company.

## 2. The standing rule

No: buying TJX for cash, unlevered and not sized to the edge, puts the buyer at no risk of ruin; the rule binds the buyer's financing and sizing, and no borrowed money or position size is in question in this run **[M2012-081]**, **[L2014-005]**.

## 3. Q1 to Q8 in order

### Q1. Can I understand it? STOP.

**The test as the draft states it:** a "reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; identify the key variables and judge "how predictable they were first" **[M1998-044]**; doubt means outside **[M2002-092]**; beware "it’s easy to sort of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**.

**Applied.** The business is one model run in four segments: buy branded apparel and home goods opportunistically (closeouts, overruns, cancellations; "approximately 21,000 vendors"; a buying organisation of "over 1,400" associates) and sell them "every day" at "prices generally 20% to 60% below full-price retailers’" with no promotions, turning inventory fast (10-K FY26, Item 1). The key variables are few and visible in the filings: comparable sales (FY26 +5%, FY25 +4%; 10-Q Q2 FY27, first half +5%), store count (5,085 to 5,214, with a stated long-term potential of 7,000 in current geographies), and pretax margin (FY24 11.0%, FY25 11.5%, FY26 12.1%, from the 10-K FY26 income statement). The longer record is steady except for one year: pretax margin about 12.2% in FY2015 (XBRL 0001193125-16-521424, flagged) and 10.6% in FY2020, near zero in FY2021 when stores were shut (XBRL 0000109198-21-000006, flagged), then back. The forecast needed is a forecast about customers (will people keep wanting brand-name goods well below full price in a store), not about technology **[M2017-019]**, **[M2023-030]**; e-commerce is about 2% of sales (10-K FY26, MD&A). The winner can be named, not just the industry **[M2012-067]**: TJX is the largest, Ross is the other large one (Q2).

**The retail warning, faced.** The draft names retail as the place false understanding is found **[M2014-052]**, **[M1997-024]**, and the doubt test is strict **[M2002-092]**. The same doubt row, read in full in the ledger, names two retailers as understandable in the next breath ("You can certainly understand Walmart [...] You can understand Costco."), so the warning is against believing, not against retailing as a class. My doubt is about the castle (whether the advantage lasts), which is Q2's question, not about whether I can see where the earning power and position will be. On the definition in **[M2012-065]** and **[M2000-037]**, I can.

**Verdict: IN.** The earning power and position can be foreseen in rough terms ten years out from a few predictable variables in the filed statements **[M2012-065]**, **[M1998-044]**.

### Q2. Why is the castle still standing? STOP.

**The test as the draft states it:** the castle questions **[M1995-038]**; would it stand without the lord **[L2007-006]**; the money test **[M2011-015]**; pricing power **[M2005-020]**; volume **[M1999-054]**; the low-cost position and the commodity exception **[L2004-007]**, **[L2000-017]**, cost measured against the competitor **[M2001-013]**; widening or narrowing **[M1999-108]**; what could destroy it **[M2000-014]**; rapid change and the rebuilt moat **[L2007-005]**.

**What keeps it standing (test 1, test 6).** The customer comes for one reason, the price gap on branded goods, and the reason is the same one the filing has given for decades (TJ Maxx founded 1976; 10-K FY26, Item 1). The advantage that produces the gap is a buying position: scale to take "quantities ranging from small to very large", a network to "disperse merchandise across our geographically diverse network of stores", prompt payment and no requested "advertising, promotional and markdown allowances", and the statement that it has "not experienced difficulty in obtaining sufficient quality merchandise for our business in either favorable or difficult retail environments" (10-K FY26, Item 1, Opportunistic Buying). This is the low-cost operator in a commodity-like field (the goods are the same brands sold elsewhere), the one way through such a field the draft names: "Another way to prosper in a commodity-type business is to be the low-cost operator." **[L2004-007]**; the 2007 definition names a retailer, Costco, as the low-cost castle **[L2007-004]**; "if you can offer somebody a good product cheaper than the other guy then everybody practically has to buy it" **[M2024-013]**.

**Same-metric comparison with the competitors' own filings (test 6, test 3).** Pretax income over revenue and (operating cash flow less capex) over revenue, each from the filed 10-K for the fiscal year ended 2026-01-31:

| | revenue | pretax income | pretax / revenue | OCF less capex / revenue | stores |
|---|---|---|---|---|---|
| TJX (0000109198-26-000008) | $60,372M | $7,299M | 12.1% (11.7% without the $221M net litigation benefit) | (6,874 - 1,957) / 60,372 = 8.1% | 5,214 |
| Ross (0000745732-26-000006) | $22,750.6M | $2,842.2M | 12.5% | (3,026.9 - 819.3) / 22,750.6 = 9.7% | 1,904 Ross Dress for Less, plus dd's |
| Burlington (0001193125-26-116001) | $11,566.9M | $816.1M | 7.1% | (1,231.4 - 1,059.8) / 11,566.9 = 1.5% | 1,212 |

The cost position is measured against the competitor, not absolutely **[M2001-013]**: TJX is level with Ross, not below it, so the castle is shared by two; it is well ahead of Burlington, the funded attacker that has built 1,212 stores and earns about half the margin and a fraction of the cash. That is the money test answered by a real attacker, not a hypothetical one **[M2011-015]**, **[M2000-077]**: the well-funded entrant exists and has not taken the economics. The two large operators are not beating each other's brains out (both earn 12% pretax), which is the commodity mark **[M2013-052]** the field does not show.

**Pricing and volume (tests 4, 5).** The 10-K says TJX has "generally been able to react to price fluctuations in the wholesale market to maintain our pricing gap relative to prices offered by traditional retailers as well as our merchandise margins through various economic cycles" (10-K FY26, Item 1, Pricing): costs passed through **[M2005-017]**. Comparable sales were driven by "a higher average basket and an increase in customer transactions" (10-K FY26, MD&A), more units of custom, the evidence of share of mind **[M1999-054]**.

**The failing answers, faced (test 2, test 11, rebuilt moat).** Test 2 is failed in its strict form: retail is the draft's own failing answer, "In retailing, to coast is to fail." **[L1995-008]**, and "For a retailer, hiring that nephew would be an express ticket to bankruptcy." **[L1995-009]**. TJX must stay smart every day in buying. Two things keep this from closing the file: the draft carries the retailer forward to Q5 as a heavy weight on management ("Buying a retailer without good management is like buying the Eiffel Tower without an elevator." **[L1995-006]**), which presupposes a retailer can pass Q2; and the skill sits in an organisation, not a superstar (1,400 buyers; every executive officer joined between 1983 and 2000, 10-K FY26, executive officers), so the surgeon-and-Mayo distinction of **[L2007-006]** goes the Mayo way. On the rebuilt moat **[L2007-005]** the draft says the line between widening and rebuilding is a judgment with no separating test; my judgment is that the vendor relationships, the scale to absorb any lot and the 31 million square feet of distribution are a standing advantage that daily buying uses, not one competitors take back each year: the evidence is the margin gap to Burlington and fifty years. Test 11 (would it be started today against its substitutes) and the threat named by the silver-bullet row, "in retail, there are a lot of people that would aim that silver bullet at Jeff" **[M2017-022]**: TJX's comparable sales and transactions have grown through the whole period of online retail; the risk is real and slow, and slow change "can lull you to sleep easier" **[M2014-038]**, carried to the box.

**Verdict: IN.** The castle stands on a low-cost buying position that a funded attacker's own filing shows has not been crossed **[L2004-007]**, **[M2001-013]**, **[M2011-015]**; the retail failing answers **[L1995-008]**, **[L1995-009]** are carried as a weight on Q5 and a risk on Q7's "how sure", not as a STOP.

### Q3. How much capital must go in, and what does the added capital earn? WEIGHING.

**The test:** return on the capital the business needs **[M1998-005]**, **[M2010-090]**, measured on tangible assets **[M2011-060]**; maintenance against growth outlays **[L1999-024]**, **[M2000-144]**.

**Applied (my arithmetic from the 10-K FY26 balance sheet and income statement, 0000109198-26-000008).** Operating capital excluding cash and lease right-of-use assets: receivables 602 + inventory 7,297 + prepaid 1,065 + taxes recoverable 8 + net property 8,220 + other assets 1,772 + deferred tax asset 147, less payables 4,575, accrued 5,891 and taxes payable 170 = about $8.5 billion. Operating pretax income (pretax 7,299 less net interest income 121, less the $221 million net litigation benefit) = about $7.0 billion: roughly 80% pretax on that capital. Counting the leases as capital (right-of-use assets 10,330) and adding back their imputed interest (about 3.9% on $10.6 billion of lease liabilities, Note L), roughly 39%. The company's own "Incentive ROIC" averaged 33.1% over FY24 to FY26 (Proxy 2026, CD&A). Growth needs capital beyond depreciation: capex 1,957 against D&A 1,247, of which new stores 185, renovations 921, offices and distribution centres 851 (10-K FY26, MD&A, Investing Activities); FY27 capex guided at $2.2 to $2.3 billion. Inventory grew 876 in FY26 against sales up 4,012.

**Verdict: WEIGHS FOR.** High returns on the tangible capital the business needs, with growth that takes moderate capital, the second-best kind at worst **[M1998-081]**, **[L2009-012]**.

### Q4. Do the numbers show what it earns, and can its condition be known? STOP on confusion or suspicion, otherwise WEIGHING.

**The test:** read the balance sheet first **[M2025-032]**; the real costs (depreciation, stock pay, all compensation) **[R1996-023]**, **[L2015-003]**, **[L2021-003]**; the tells **[M1995-064]**, **[L2002-041]**, **[L2022-006]**, **[L2016-006]**; confusion or suspicion is a STOP **[M1995-063]**, **[M1995-065]**.

**Applied.** The accounts are plain. GAAP net income is the headline in the 10-K; stock compensation ($214 million) and option cost are expensed (Note H); operating cash flow exceeds net income every year shown (6,874 against 5,494 in FY26); inventory is on the retail method with "a specific policy as to when and how markdowns are to be taken, greatly reducing management’s discretion" (10-K FY26, Critical Accounting Estimates); pensions are small (funded asset $189 million, Note I); there is no EBITDA talk in the filings read. Two balance-sheet tells were looked at twice **[M1995-064]**: (a) prepaid and other current assets rose from 617 to 1,065 in FY26; the 10-Q Q2 FY27 shows it back to 730 and says the cause: "a decrease of prepaid expenses and other current assets related to the receipt of the credit card interchange fees settlement" (0000109198-26-000048, MD&A); resolved. (b) Per-store inventories were "up 10%" against comparable sales up 5% (10-K FY26, MD&A highlights), with in-transit inventory up from $1.6 to $1.8 billion (Note A); by 2026-08-01 inventory was 7,862 against 7,372 a year earlier, +6.7%, against first-half sales +7.2% (10-Q Q2 FY27); resolved. Adjusted EPS appears only in the proxy (Appendix A) and its four adjustments run both ways (two add back charges, two remove benefits), so it is not the habit of "highlighting "adjusted per-share earnings"" to wave costs away **[L2016-006]**.

**The tell that is not resolved.** TJX gives quarterly and annual EPS and pretax-margin guidance, and every earnings release headline from Q4 FY24 to Q2 FY27, eleven in a row, reports EPS and pretax margin "above plan" or "well above plan" (8-K exhibits listed above; e.g. Q2 FY27: "PRETAX PROFIT MARGIN AND DILUTED EPS BOTH WELL ABOVE PLAN; INCREASES FULL YEAR FY27 PRETAX PROFIT MARGIN AND EPS GUIDANCE", 0000109198-26-000045). The draft's row: "we become downright incredulous if they consistently reach their declared targets. Managers that always promise to "make the numbers" will at some point be tempted to make up the numbers." **[L2002-041]**; and "Beating "expectations" is heralded as a managerial triumph. That activity is disgusting." **[L2022-006]**. I looked twice at the accounts for the mark of made-up numbers (accruals running ahead of cash, reserves released, inventory or prepaid building) and found none in the filings read; the beats are against a plan the company sets, a practice about expectations rather than about the accounts. So it is not confusion, and the suspicion is of the guidance practice, not of the figures; the draft's own edge, a management preoccupied with accounting is "a negative" but not "a total exclusionary factor" **[M1994-018]**, keeps it a weight.

**Owner earnings carried to Q7 (Q4 supplies the cash, Q3 what goes back).** FY26 net income 5,494 less the $0.14 per share net litigation benefit (about 158 on 1,128 million diluted shares, 10-K FY26, MD&A) = about 5,336; plus D&A 1,247; less maintenance capex placed between D&A (1,247; depreciation as the proxy "not inappropriate in most companies" **[M1998-127]**) and capex less new stores (1,772; renovations alone are 921, three quarters of D&A, and the 851 for offices, distribution and IT serves both upkeep and growth, 10-K FY26, MD&A): about **$4.8 to $5.3 billion** for FY26. `run.py`'s three-year mean is 4.3 to 5.1 billion; its five-year window 3.4 to 4.1 billion includes the weaker FY22 and FY23, a base-year effect the draft says to check **[L2005-003]**. Carried: **$4.3 to $5.3 billion**, after all compensation **[L2021-003]**.

**Verdict: no STOP; WEIGHS AGAINST, narrowly.** The accounts are readable and cash-backed, so the file stays open; the habit of beating declared numbers is the tell the rows name **[L2002-041]**, **[L2022-006]**, and it is weighed, not cleared.

### Q5. Who runs it? STOP on integrity, WEIGHING on ability.

**The test:** two yardsticks, the record against the hand dealt and the treatment of owners **[M1994-008]**, **[M1994-009]**; integrity on doubt **[M2013-088]**; for a marketable stock the speakers read rather than meet **[M2007-081]**.

**Integrity (STOP).** None of the tells the draft names was found in the filings read: no report dancing round the key figure (comparable sales are defined at length and the definition change for e-commerce is disclosed, 10-K FY26, MD&A); no credit taken for the litigation gain (it is reported as non-recurring, and its use to fund a "discretionary bonus for eligible non-bonus plan Associates" is disclosed); no serial issuance (shares fell from 1,155 million to 1,101 million between January 2023 and August 2026, 10-K FY26 equity statement and 10-Q Q2 FY27 balance sheet). The guidance habit is weighed at Q4 and Q6, not here, since the Q5 tells do not list it. **IN.**

**Ability (WEIGHING).** For a retailer the weight is heavy **[L1995-006]**. The record against the hand dealt: comparable sales +5% against Ross +5% and Burlington +2% in the same year (Ross 10-K, MD&A; Burlington 10-K, MD&A), margins level with the best competitor and above the attacker (Q2 table), and a return to full earnings after the shut-down year. The people are lifers (chief executive with TJX since 1989, executive chairman since 1983, chief financial officer since 2000; 10-K FY26, executive officers), a long record rather than a promise **[M1996-038]**, **[M2005-039]**. **WEIGHS FOR.**

**Verdict: IN on integrity; WEIGHS FOR on ability** **[M1994-008]**, **[L1995-006]**.

### Q6. What will they do with the money and with the owners? WEIGHING.

**Part A, the money.** Retention: TJX keeps little. In FY26 it paid $1,842 million in dividends and $2,522 million for buybacks against net income of $5,494 million (10-K FY26 cash-flow statement), about 79% returned; what was kept went into stores and distribution at the returns in Q3, and diluted EPS rose from $2.97 (FY23) to $4.87 (FY26) on that small retention, so the dollar-retained test passes **[M1998-110]**, **[R1995-009]**. No stock-paid acquisitions; the only deals are two small equity-method stakes ($551 million in FY25, 10-K FY26, Note A), so the STOP of **[L2009-019]** and the serial-issuer candidate **[L2014-015]** do not arise. **Buybacks are set by sum, not by price:** $2,484M, $2,495M and $2,506M in FY24 to FY26 (Note D), and "We currently plan to repurchase approximately $2.5 billion to $2.75 billion of stock" in FY27 (10-K FY26, MD&A, Equity), with buyback amounts carried in the guidance raised in the Q1 FY27 release headline (0000109198-26-000023). The implied average prices rose from about $86 (FY24: 2,484 / 29.0M) to about $112 (FY25), $135 (FY26) and about $159 (first half FY27: "$1.4 billion to repurchase and retire 8.9 million shares", 10-Q Q2 FY27). No price limit is named; this is the programme **[L2016-002]** describes, and "what is smart at one price is dumb at another" **[L2011-003]**. Shares are also issued each year under the stock plan (7 million in FY26, equity statement), and buying to offset option issuance is ruled out by name **[M2014-008]**; the filings do not say that is the motive, so I weigh only the sum-not-price fact.

**Part B, pay, board and owners.** Chief executive total pay $26.6 million in FY26 (Proxy 2026, Summary Compensation Table). The annual plan pays on pretax income with no charge for capital **[M1995-010]**; the PSUs pay on "Incentive EPS growth", which "Excludes the impact of certain unplanned items, such as unbudgeted buybacks", so budgeted buybacks lift the paying metric, with ROIC only a downward modifier (Proxy 2026, CD&A); the FY24 to FY26 PSUs paid the 200% maximum. The committee works with an "independent compensation consultant" and a peer group **[M2004-016]**, **[L2005-015]**. Options for others are at market price with a ten-year term and no step-up for retained earnings (Note H) **[L1994-021]**. Earnings guidance is published (test 13) **[L2019-006]**, **[M2022-054]**. Against these: the chairman and chief executive roles are separate, with a lead independent director (Proxy 2026), and directors carry ownership guidelines.

**Verdict: WEIGHS AGAINST.** Retention and the absence of stock deals weigh for, but the buyback is a fixed sum at rising prices with no price named **[L2016-002]**, **[L2011-003]**, and pay is tied to EPS growth that the buyback feeds and to guidance the company habitually beats **[L2019-006]**.

### Q7. What is it worth: how much cash, how sure, how soon, at the long government rate, held as a range; and is the price so far below it that it needs no pencil? STOP.

Q1 to Q6 are each IN or weighed; Q7 is reached.

**The definition and the rate.** Value is the discounted cash that can be taken out **[R1996-018]**, at the long government rate with no risk premium in the rate **[M1996-024]**, **[M1999-103]**: 5.63%. Certainty is taken in the cash estimate and in the discount demanded from the result **[M1997-126]**.

**How much cash, how sure, how soon.** Starting owner earnings $4.3 to $5.3 billion (Q4). Growth from the filings: store count to a stated potential of 7,000 from 5,214 (about a third more) at the recent pace of about 3% a year, plus comparable sales of 4% to 5% in the last two years, plus a net share count falling about 1% a year (Q6). How sure: the castle is shared and the business is a stay-smart-every-day retailer **[L1995-008]** that earned almost nothing in one shut-down year, so the cash stream is less sure than a See's or a Coca-Cola, and the margin asked rises with that **[M1997-080]**.

**The range (my arithmetic; `_work_A1_TJX/value.py`).** CONVENTION: a ten-year explicit period followed by a perpetual rate below the discount rate; rationale: the rows define value as a discounted stream **[R1996-018]** but give no horizon, and forbid growth at or above the rate forever **[M1997-095]**.

| case | owner earnings now | growth, years 1 to 10 | growth after | value at 5.63% | per share |
|---|---|---|---|---|---|
| low | $4.3B | 5% | 2% | about $155B | about $140 |
| middle | $4.8B | 7% | 3% | about $265B | about $240 |
| high | $5.3B | 8% | 3.5% | about $380B | about $345 |

The range is wide (about 2.5 times from bottom to top), and 73% to 84% of each value sits beyond year ten. The price, $146 billion ($133 a share), is about 6% below the bottom boundary **[L2013-012]**. Turned round, the price implies an expectancy of about 5.9% (low case) to 8.8% (high case) a year against a 5.63% bond.

**Is the price so far below it that it needs no pencil?** No. It needed the table above to show the price under the bottom of the range at all, and only by a few percent; "if you really need a calculator to figure out that it’s — the discount rate is 9.6 percent instead of 9.8 percent — forget about the whole exercise" **[M2009-005]**; "it ought to just kind of scream at you" **[M1996-084]**. The expectancy at the price is not "a significantly higher return [...] than we are from a government bond" at the low end and only modestly so in the middle **[M2007-095]**. A wide range is not to be rescued by a bigger discount **[M2007-022]**.

**Verdict: OUT.** Valued, with the price below the bottom of the range by too little to need no pencil: the close case, which the draft sends to "out" **[M2009-005]**, **[M1996-084]**, **[M2007-095]**.

### Q8. Is it better than the alternatives? STOP.

NOT REACHED (Q7 closed the run).

## 4. Q9 and Q10

NOT REACHED. For the record only, and not a clearance: total debt $2,878 million against $6,230 million of cash at 2026-01-31, with $1,000 million due September 2026 and $10.6 billion of operating lease liabilities (10-K FY26, Notes J and L); the leases, not the notes, are the fixed claim a Q9 weighing would turn on.

## 5. Q11 and Q12

**Q11:** not answered; the operator does not hold TJX.

**Q12. Would we be proud of how the money is made? (STOP for named businesses, otherwise WEIGHING).** Off-price apparel and home retailing is none of the businesses the draft names (casinos, tobacco, loading schemes, gambling dressed as investing, promotion on a borrowed reputation) **[M2007-018]**, **[M2005-097]**, **[M2013-015]**, so it is a WEIGHING. The newspaper test **[M2008-011]**: nothing in the filings read would trouble the neighbours; sourcing from "more than 100 countries" with a large low-wage store workforce carries the ordinary imperfection the draft accepts **[M2021-012]**; I did not read beyond the filings listed. **WEIGHS FOR** (no finding against).

## 6. The box

**OUT, decided at Q7.** Value as a range in round numbers at the 5.63% long government rate: **about $155 to $380 billion, or about $140 to $345 a share, against a price of $133 ($146 billion)**: how much cash, $4.3 to $5.3 billion of owner earnings growing with stores and comparable sales; how sure, less sure than the draft's exemplars (a shared castle, a retailer that must stay smart daily, one near-zero year); how soon, mostly after year ten. The price sits only a few percent under the bottom of the range: it needs a pencil, so it is not a buy under the draft **[M2009-005]**. Q1 IN, Q2 IN, Q3 weighs for, Q4 weighs against narrowly, Q5 IN and weighs for, Q6 weighs against.

## 7. Self-audit

- **Every id resolves.** All ids cited in this file were checked against `principle_ledger_v5.csv` by `grep -c "^<id>,"` (one row each); 92 distinct ids, all resolve, and all 92 also appear in the draft itself (checked by grep against the draft). Em dashes appear only inside verbatim quotations.
- **Every filing fact has an accession.** Yes; the table at the top maps each short name to its accession, and each fact names its document. Three older-year figures are XBRL transcription (FY2015, FY2020, FY2021) and are flagged as such; none of them is an input to Q7.
- **No number without a row or a filing.** Filing figures carry their document; my own arithmetic is shown with its inputs; the ten-year horizon and the perpetual rates in Q7 are labelled CONVENTION with a rationale; the growth rates in Q7 are my judgment from filed store counts and comparable sales, stated as such.
- **Files opened.** The protocol, the v5 draft, `principle_ledger_v5.csv` (rows read by id), `tools/sources.py` (for the SEC user agent), `tools/run.py` and `Screens/cover_shares.py` (run, not read), SEC EDGAR, and my own output and working folder. Not opened: v4, `principle_ledger.csv`, anything under `Test Runs/` or other `Screens/` files, `PORTFOLIO.md`, any other file under `Framework/v5/tests/`. `run.py` printed v4 ids and a v4 floor line in its output; I did not use them.
- **Order kept; the first STOP stopped the run.** Q1 to Q7 in order; Q7 returned OUT; Q8 to Q10 marked NOT REACHED, with only the debt facts recorded under Q9 as a non-clearance note; Q12 answered as the test instruction asks.

## 8. What in the draft was wrong or unclear

The draft does not say how a retailer passes Q1 and Q2, and its retail rows pull two ways. Q1 lists retail as the example of false understanding **[M2014-052]**, the doubt test is absolute **[M2002-092]**, and Q2's test 2 gives retail as the failing answer **[L1995-008]**, **[L1995-009]**; but Q2 names Costco as the model low-cost castle **[L2007-004]**, the full ledger row behind **[M2002-092]** names Walmart and Costco as understandable (the draft quotes only its first sentence), and Q5 carries "buying a retailer without good management" **[L1995-006]** as a weight, which presupposes a retailer gets past Q2. I read the retail rows as a warning and a Q5 weight rather than a STOP; a second analyst who reads test 2's failing answer as closing Q2 would put TJX in TOO HARD at Q2, and nothing in the draft says which reading governs. Second, Q4's "What it rules OUT" lists "managements that habitually make or beat their numbers" **[L2002-041]**, **[L2022-006]** in the same unqualified list as confusing accounts, while section I and the Q4 heading make Q4 a STOP only on confusion or suspicion and name no box; I treated a clean-cash company with a beat-the-plan habit as WEIGHS AGAINST, but the draft should say whether the habit alone is "suspicion about accounting" under **[M1995-065]**. Third, Q7 gives three ways to close (cannot value, below the floor, too close) but writes no floor, so when the price sits just under a wide range the run must choose between TOO HARD (range "so wide that no useful conclusion can be reached" **[L2000-025]**) and OUT (close call **[M2009-005]**); I chose OUT because a range could be built, and both give the same box only by luck. Fourth, the protocol whitelists `tools/run.py`, whose output prints v4 ids and a 10% floor rule that the v5 draft expressly declines to adopt; a v5 run should get a v5-clean arithmetic print.
