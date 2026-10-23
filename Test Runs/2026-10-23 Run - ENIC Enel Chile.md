# Company Run — Enel Chile S.A. (NYSE: ENIC, ADSs of 50 shares each) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-23, after the run was committed (384cf6af): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Run status:** dispatched blind run (operator rule 10), started 2026-10-23; written question by question.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** US$4.34 per ADS (close 2026-10-22; Yahoo Finance chart endpoint through `tools/sources.py price()`; an
  aggregator, flagged per operator rule 5, used for the live quote only). One ADS represents 50 shares of common stock, so
  the per-share equivalent is US$0.0868.
- **Shares by class** from the latest filing's cover: 69,166,557,219 shares of common stock, one class (20-F for 2025,
  filed 2026-04-28, accession `0001104659-26-050251`; `python Screens/cover_shares.py ENIC`). Checked against the 20-F:
  weighted average 69,167 million in 2023, 2024 and 2025 (Item 5, selected data); Item 16E: "In the fiscal year 2025, there
  were no purchases of Enel Chile's equity securities by us or any of our affiliates"; no treasury shares are carried. The
  6-Ks filed after the 20-F (0001292814-26-002639, 0001292814-26-002712, 0001292814-26-003952) report no issuance; the
  Q2 2026 analysis states issued capital unchanged at US$3,896 million. That is 1,383.33 million ADS-equivalents.
- **Market cap:** US$6,003.7M (69,166.56M shares / 50 x US$4.34).
- **Net debt at the latest filed date** (Q7's all-equity basis): gross financial debt US$3,785M at 2026-06-30, which the
  company states includes the bonds, bank loans, the Enel Finance International loans and the IFRS 16 lease liabilities,
  less cash and cash equivalents US$276M (Q2 2026 financial statements analysis furnished on 6-K 2026-07-29, accession
  `0001292814-26-003952`) = **US$3,509M**. Cross-check at 2025-12-31 from the filed balance sheet and notes: interest-bearing
  borrowings US$2,420.8M (Note 20) + Enel Finance International loans US$1,028.6M (Note 10, current 167.1 and
  non-current 861.5) + lease liabilities US$410.2M (Note 21) - cash US$461.9M - other current financial assets US$1.0M =
  US$3,396.7M; the company's own gross figure for that date is US$3,840M against my US$3,859.6M. Hedging derivatives
  (US$71.6M) are left out of debt, said so. Operating leases are inside the IFRS 16 figure and cannot be separated from the
  company's number, said so. Non-controlling interests (US$377M book at 2026-06-30, chiefly the 6.45% minority of Enel
  Generación Chile) are handled by deducting the dividends paid to them from owner cash.
- **Sovereign for the earnings currency: 5.29%**, the US Treasury daily par yield curve, 30-year par yield, 2026-10-22
  (issuing authority; `python tools/sources.py`). **How the earnings currency was decided:** the 20-F says that effective
  2025-01-01 the functional and presentation currency is the US dollar "because the U.S. dollar became the currency that
  most significantly influences the primary economic environment in which the Company operates", that the change followed
  Enel Generación Chile's own change because its revenue "comes predominantly from agreements with unregulated customers"
  billed on a dollar basis, and that "a substantial amount of our consolidated indebtedness and operating cash flows are
  linked to the U.S. dollar" (Item 5.A.1; Item 3.D). Generation, which carries more than nine tenths of operating profit
  (Q2's parts table), earns on dollar-linked contracts, so the earnings currency is the dollar. The distribution part earns
  pesos; **I did not take a Chilean peso sovereign from the Banco Central de Chile**; no figure in this run depends on it,
  and it is confessed here as not obtained.
- **Exchange rates, and how the earlier years are put on one basis.** The 2025 20-F restated 2023 and 2024 into US dollars
  under IAS 21 at average rates for flows (Ch$839.91 and Ch$943.74) and year-end rates for balances; those restated
  figures are used as filed. For 2016 to 2022, filed in pesos, I translated flows at the Banco Central de Chile annual
  average dólar observado (2016 676.83, 2017 649.33, 2018 640.29, 2019 702.63, 2020 792.22, 2021 759.27, 2022 872.33;
  BCCh BDE table "Dólar observado", annual frequency, fetched 2026-10-23 from si3.bcentral.cl, the issuing authority) and
  balances at the year-end rate printed in each 20-F (2019 748.74, 2020 710.95, 2021 844.69, 2022 855.86). This is the
  method the company itself used for 2023 and 2024 (check: 2023 operating cash Ch$705,662M / US$840.2M = 839.9). It is a
  translation, not a restatement: years before 2025 were peso-functional and their dollar figures carry the peso's moves
  (the peso fell from 649 to 944 per dollar on average between 2017 and 2024).
- **Filings read** (operator rule 4): 20-F for 2025 (filed 2026-04-28, `0001104659-26-050251`): Item 3.D, Item 4, Item 5,
  Items 6 to 8, 16E, the statements and Notes 3, 9, 10, 20, 35, 36.3; 20-F for 2024 (2025-04-29, `0001558370-25-005756`);
  2023 (2024-04-30, `0001558370-24-006219`); 2022 (2023-04-26, `0001558370-23-006813`); 2021 (2022-04-28,
  `0001558370-22-006151`); 2020 (2021-04-29, `0001558370-21-005231`); 2019 (2020-04-29, `0001558370-20-004669`); 2018
  (2019-04-30, `0001104659-19-025167`); 2017 (2018-04-27, `0001564590-18-009415`); the 6-Ks of 2026-04-29 (material fact,
  the 2025 final dividend, `0001292814-26-002639`), 2026-04-30 (Q1 2026, `0001292814-26-002712`) and 2026-07-29 (Q2 2026,
  `0001292814-26-003952`). The 2021 to 2024 20-Fs were read for their statements, segment notes and selected data only;
  the 2018 and 2017 20-Fs for a few lines. There is no proxy: a foreign private issuer; Item 6 stands in for it. **One
  figure cross-checked against the filed statement:** net cash flows from operating activities 2025, US$1,320 million in
  Item 5.B against ThUS$1,319,678 in the Consolidated Statement of Cash Flows, Direct Method (F-11): they agree.
- `python tools/run.py ENIC` returned "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (an IFRS 20-F filer with
  no usable XBRL series). **Every figure below is taken from the filed statements**, transcribed into
  `Test Runs/_research 2026-10-23 ENIC/compute.py`, whose output is `compute_output.txt` in the same folder.

**Owner cash by year, US$ millions** (operating cash as filed, which is after the company's income tax and before
interest, since this filer classifies interest paid in financing; less purchases of property, plant and equipment and of
intangibles; less payments on lease liabilities; less dividends to non-controlling interests; the income tax paid on two
divestiture gains added back because the sale proceeds are left out, US$280M in 2023 on Enel Transmisión and US$74M in
2024 on Arcadia, Item 5.B of the 2025 20-F). "Equity-only" also deducts interest paid less interest received.

| Year | Operating cash | Capex (PP&E + intangibles) | D&A | Owner cash, all-equity | Owner cash, equity-only | Revenue | Operating income |
|---|---|---|---|---|---|---|---|
| 2019 | 1,058.5 | 457.0 | 336.8 | 571.5 | 388.8 | 3,943.5 | 748.7 |
| 2020 | 954.1 | 699.7 | 290.3 | 225.3 | 56.6 | 3,263.5 | -43.2 |
| 2021 | 543.8 | 1,035.3 | 277.8 | -528.2 | -712.0 | 3,760.5 | 341.9 |
| 2022 | 853.8 | 1,074.8 | 273.1 | -255.4 | -446.6 | 5,681.8 | 1,045.9 |
| 2023 | 840.2 | 788.7 | 301.7 | 284.6 | 95.7 | 5,215.1 | 914.1 |
| 2024 | 1,622.2 | 765.4 | 313.1 | 875.2 | 679.4 | 4,224.8 | 395.3 |
| 2025 | 1,319.7 | 499.1 | 387.4 | 740.8 | 578.7 | 4,662.7 | 1,011.3 |

Five-year average 2021 to 2025: **US$223.4M all-equity, US$39.1M equity-only**. Stock pay: none found; the LTI plan pays
cash (Item 6), so it is inside operating cash, and "None of the directors or officers described in Item 6.A beneficially
owns any of our shares or holds stock options". Operating income 2020 carries the Bocamina II impairment (about Ch$713bn)
and 2024 a US$657M loss on discontinued cash-flow hedges recognized when Enel Generación Chile changed its functional
currency (Item 5, note 2 to the selected data). What the table does not show by itself: operating cash in 2023 to 2025
contains the proceeds of selling price-stabilization receivables built up in 2019 to 2022 (about US$345M of Treasury
payment documents and US$51M of balances in 2023; about US$697M in 2024; US$235.2M in 2025; Note 9.a.2), and every year
contains the factoring of short-term receivables (US$1.68 billion nominal sold in 2025, Note 9.a.2) and the assignment of
distribution collection rights (US$840M outstanding at 2025-12-31 against US$605M at 2024-01-01). The low years 2021 and
2022 are the years the receivables were built up; the high years 2024 and 2025 are partly their release.

**The balance sheets, 2016 to 2025** (read here because the file closes before Q4; **[M2025-032]**). Ch$ billions to 2022,
US$ millions from 2023 (the restated figures).

| Year-end | Total assets | Equity to parent | Goodwill | Trade receivables (current + non-current) | Net debt (incl. EFI loans, leases) |
|---|---|---|---|---|---|
| 2016 | Ch$5,398.7 | Ch$2,763.4 | Ch$887.3 | not read | not read |
| 2017 | Ch$5,694.8 | Ch$2,983.4 | Ch$887.3 | not read | not read |
| 2018 | Ch$7,488.0 | Ch$3,421.2 | not read | not read | not read |
| 2019 | Ch$7,858.0 | Ch$3,484.7 | Ch$917.4 | Ch$825.0 | Ch$2,503.5 |
| 2020 | Ch$7,904.5 | Ch$3,351.9 | Ch$915.7 | Ch$999.9 | Ch$2,525.0 |
| 2021 | Ch$9,500.3 | Ch$3,097.9 | Ch$921.1 | Ch$1,204.0 | Ch$3,180.0 |
| 2022 | Ch$11,865.6 | Ch$4,097.2 | Ch$883.6 | Ch$2,200.7 | Ch$2,759.9 |
| 2023 | US$13,491.6 | US$5,069.0 | US$1,008.4 | US$2,682.6 | US$3,638.7 |
| 2024 | US$12,765.1 | US$4,976.4 | US$892.4 | US$2,658.6 | US$3,544.3 |
| 2025 | US$12,903.7 | US$5,175.9 | US$902.2 | US$2,491.6 | US$3,396.7 |

(The 2016 to 2018 statements sit in the 2017 and 2019 20-Fs in a layout I read only for the lines shown.) What moved and
why. **Assets** rose in 2018 because Enel Green Power Latin America (1,189 MW of wind and solar) was merged in for Enel
Chile shares (49,093M shares became 69,167M) and the minority of Enel Generación Chile was bought largely with debt
(long-term loans of Ch$1,565.8bn drawn in 2018). **Goodwill** has stood near Ch$0.9 trillion since 2016, about a sixth of
equity; it comes from the Enersis-era combinations, not from purchases in the window. **Receivables** rose far faster than
revenue: about 30% of revenue in 2019, 51% in 2023, 63% in 2024, 53% in 2025; the cause the filing gives is the three
tariff stabilization laws (Law 21,185 of 2019, 21,472 of 2022, 21,667 of 2024), under which the generators financed
regulated customers' bills, with the distributor's non-current energy payables (US$985.6M at 2025-12-31) the mirror of the
same mechanism. **Debt** rose with the 2018 tender offer and again in 2021 to 2023 while capital spending ran at two to four
times depreciation and the receivables were built; a large part is lent by the controlling shareholder's finance arm
(Enel Finance International, US$1,028.6M at 2025-12-31, the main loans at fixed 2.55% to 3.30%, Note 10). **Equity** in
dollars moved little over ten years: Ch$2,763bn in 2016 (about US$4.1bn at the year-end rate) against US$5.2bn in 2025,
after shares were issued for the 2018 merger. In 2025 the change of functional currency moved US$2,068M from share
capital to other reserves (statement of changes in equity, opening balance restated after adjustment): a reclassification,
not a loss. What the figures cannot say: what the remaining stabilization balances (US$1,324.8M of receivables at
2025-12-31, Note 9) will finally fetch, and how much of the 2021 to 2025 capital spending was replacement of closed coal
plants rather than growth.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the one against macro forecasts: this is a Chilean electricity company whose results move
with rainfall, LNG prices, the peso and the Chilean state's tariff policy, and the rows say "macro conclusions are — just
never enter into the discussion" **[M2000-094]**; the run asks what the business earns over a cycle and what protects it,
not where rainfall or the peso will go. The peso matters only as a property of the business: before 2025 the accounts were
peso-denominated, dividends are still paid in pesos, and "Any currency-related investment is a bet on how government now,
and in the future, will behave" **[M2011-025]**. The market "is there to serve you and not to instruct you"
**[M2006-077]**: the ADS price tells nothing here. **Contrary evidence, written down as found** **[M1997-127]**:
(1) owner cash after all spending averaged US$223M a year in 2021 to 2025 against a market value of US$6.0bn and net debt
of US$3.5bn; (2) the 153 MW Los Cóndores hydro plant cost "approximately US$1.2 billion" (Item 4.D), and generation in 2025
(21,583 GWh) was about what it was in 2019 (21,041 GWh: 17,548 at Enel Generación and 3,493 at EGP Chile, 2020 20-F)
although net capacity rose from about 7,303 MW to 8,904 MW, because 636 MW of coal was closed; (3) three laws in five
years overrode the regulated tariff and made the generators lend to customers (Item 3.D); (4) the named rival AES Andes
(formerly AES Gener) recorded a US$781M asset impairment in 2020 and a US$644M goodwill impairment in 2022, and the 531 MW
Alto Maipo hydro project of AES Andes went through Chapter 11, emerging in May 2022 (AES Corp 10-Ks for 2020 and 2023); (5) Enel Chile
impaired the Bocamina II coal plant by about Ch$713bn in 2020; (6) a first-instance judgment of December 2023 ordered Enel
Green Power Chile and a state agency to pay ThUS$383,847 jointly in a mining-project tort case, under appeal, the company
estimating "A very minor risk of adverse judgment" (Note 36.3).

## THE STANDING RULE
A purchase of these ADSs for cash, unlevered and sized so that their total loss would not touch what the buyer needs,
puts the buyer at no risk of ruin; bought on margin it would, because "borrowed money has no place in the investor's tool
kit" **[L2014-005]**, and the owner must be prepared to see a holding "go down 50 percent — or more — and be comfortable
with it" **[M2020-022]**. The rule binds the buyer's financing and size, not the company: "We are never going to risk what
we have and need for what we don’t have and don’t need" **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in that particular
  business, and evaluating how predictable they were" **[M1998-044]**; the product need not be understood if "I
  understand the economic dynamics of the industry" **[M2011-014]**.
- **The business, from the filing.** Two reported segments: Generation (Enel Generación Chile, EGP Chile, Pehuenche;
  8,904 MW, 41% hydro by capacity, 22% of the SEN's capacity, 40.2% of the system's electricity sales in 2025) and
  Distribution and Networks (Enel Distribución Chile, 2.2 million customers in 33 municipalities of Santiago under an
  indefinite concession). Generation sells under contracts sized to "our estimated electricity production in a dry year",
  to distributors through regulator-run auctions ("an average term of ten years") and to unregulated industrial customers
  ("typically range from five to fifteen years"), and balances its contracts against its dispatch by buying or selling at
  the hourly spot price, which is the system's marginal cost (Item 4.B). Distribution earns a regulated value added (VAD)
  set every four years on a model company, at an after-tax return the Distribution Short Law of 2019 bands between three
  points below and two points above the CNE's rate (Item 4.B; Item 5.A.1.b).
- **The key variables and whether they are foreseeable.** (1) Contracted volume and price: visible for years ahead in
  part, since the company was awarded "100% of the energy tendered" in May 2024 for twenty years from 2027 and 2028 at
  US$56.68 per MWh, and in 2025 four-year and one-year blocks at US$64.5 and US$98.7 (Item 4.B). (2) Hydrology: not
  foreseeable year to year; the filing says conditions have been "significantly below average, as has been the case for
  much of the period since 2007"; a cyclical input to the base, not a forecast I need. (3) Spot prices, LNG and the solar
  build-out: commodity inputs. (4) Regulation: the distribution tariff process and the state's interventions in regulated
  generation prices. (5) The peso, which since 2025 matters chiefly to the distribution part.
- **Routing.** The commodity paragraph governs (1) to (3): a dependence on a commodity price "is never by itself a STOP at
  Q1 or Q2"; the speakers say "We don’t think we can predict commodity prices" **[M2016-025]** and still decide "off the
  figures" **[M2008-069]**; Q1 asks whether the business can be understood from its figures, and Q2 asks whether it is the
  low-cost producer. The regulatory climate is placed by the text at Q2 and Q9 (Q7, The regulated utility). The industry is
  not one of fast-moving technology in the sense of **[L1993-023]**: the assets are dams, gas turbines, wind and solar
  plants and wires whose economics the filing explains, and the change under way (solar and batteries, coal closures) is a
  change in the supply curve of a commodity, which Q2 tests.
- **Can the figures tell me the future figures?** "do I understand enough about this business so that the financial
  statements will tell me the information that’s useful to me" **[M2008-033]**: yes for the mechanics (contracts against a
  dry-year generation, spot purchases, the receivables the laws created), with ten years of filed statements and a segment
  note (Note 35) that separates the two businesses. Abroad, "where we think we understand the nuances of the corporate
  governance system and taxation" **[M2000-141]**: the filing explains the Chilean corporations law, Resolution 667/2002's
  separation of the generation and distribution boards, the dividend rule (a 30% legal minimum; policy 50%) and the
  controlling shareholder's 64.93%.
- **The doubt I carry, stated so that it can be checked.** "if you have doubts about something being into your circle of
  competence, it isn’t" **[M2002-092]**. My doubt is not whether I can read this business but whether its earnings are any
  good, which is Q2's question. The state's interventions deferred the generators' money rather than taking it: the
  stabilization balances are guaranteed in full (Law 21,472's first US$1.8bn) or 30% (the added US$3.7bn), are being sold
  to IDB Invest and others at the costs Note 9 records, and must be repaid by 2032 and 2035 (Item 3.D; Item 5.A.1). That is
  a regulatory climate to judge at Q2 and Q9, not an unknowable.
- **VERDICT: IN.** The economics can be read from the figures and the key variables named; price, rainfall and policy are
  routed by the text to Q2, Q7 and Q9 **[M2016-025]**, **[M2008-069]**, **[M2011-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The question:** "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The moat is what
"protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (Note 35 of each 20-F; operating income by segment, US$ millions, 2021 and 2022 translated at the BCCh
annual average; Distribution and Networks includes transmission until its sale in December 2022):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum | Share of the segments' sum | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Generation | 293.5 | 999.7 | 933.7 | 478.8 | 956.2 | 3,661.9 | 92.9% | see below | **yes** (more than half) |
| Distribution and Networks | 76.6 | 95.8 | 37.3 | -12.9 | 81.3 | 278.1 | 7.1% | a regulated concession | no |
| Holdings and eliminations | -28.2 | -49.6 | -56.9 | -70.6 | -26.2 | -231.5 | | | |

Generation 2024 is after the US$657M hedge-discontinuation loss; with it added back the share rises. The file closes on
Generation (the business-of-parts convention: a part decides at more than half of five-year operating profit). The
regulated-utility paragraph of Q7 therefore does not govern this run's central basis: the deciding part does not earn "a
return a regulator allows on its invested capital"; its regulated sales are made at prices bid in auctions, and the text
says "Merchant generation and unregulated renewables, priced by a market, stay on the all-equity basis". The distribution
part does earn a regulated return (the VAD band around the CNE's rate), but it does not decide.

**The castle tests, on Generation, each with its filing fact.**
- *What keeps it standing, and how permanent.* The durable assets are real: 3,667 MW of hydro, reservoirs at Ralco,
  Pangue, El Toro and Rapel, and water rights that are "for an unlimited duration" and "absolute and unconditional property
  rights" (Item 3.D); a 40.2% share of the system's electricity sales and 22% of its capacity (Item 4.B). Large reservoir
  hydro of this kind is not being built again in Chile on any terms the filing shows (Los Cóndores, 153 MW run-of-river,
  "approximately US$1.2 billion", Item 4.D). What is not durable is the price those assets earn.
- *The low bid.* "would people still want to be both eating and giving away that candy in preference to other candies?
  And it wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**: here it is exactly a question of
  the low bid. "Supply contracts with distribution companies must be auctioned"; "Electricity generation companies compete
  mainly on price, technical experience, and reliability"; unregulated contracts reflect "competitive market conditions"
  (Item 4.B). The product is a kilowatt-hour on a common grid, sold to the lowest bidder in tender and settled hourly at
  the system's marginal cost.
- *Who sets the price.* The spot price is "the cost of the most expensive power plant in operation, given an
  efficiency-based dispatch" (Item 5.A.1.a), and the company bought 10,393 GWh, 32.5% of what it sold in 2025, in that
  market (Item 4.B). "whatever he charged for gas was my price" **[M2012-109]**; "he determined our profit, because we
  looked at his price every day" **[M2023-079]**.
- *Pricing power, and the agony before a price rise.* None shown. The regulated price was frozen by law from 2019 (Law
  21,185 "eliminates the price increase of 9.2% that would have been applied to regulated customers as of July 2019"), the
  generators financed the difference up to US$5.5bn under three laws, and in 2025 the regulator found it had over-billed
  regulated customers and cut tariffs by about 2% to refund it (Item 3.D). Regulated customers between 300 kW and 5,000 kW
  are leaving the regulated price "because regulated tariffs are currently higher than unregulated tariffs" and the
  Ministry lowered the threshold from 500 kW to 300 kW in November 2024 (Item 3.D). Sales to regulated customers fell from
  13,895 GWh to 10,616 GWh in 2025, with "a lower average sales price" costing US$198M (Item 4.B; Item 5.A.2).
- *The low-cost position* (the commodity paragraph's own test, **[M2006-004]**, **[M1997-010]**). The company's claim:
  "We have lower marginal production costs than companies whose installed capacity is primarily thermal because 41% of our
  installed capacity connected to the SEN is hydroelectric" (Item 4.B). Against it, from the same filing: the marginal cost
  of solar and wind is "close to zero" as well, the reservoirs' water is "assigned an opportunity cost" that rises in
  drought (Item 5.A.1.a), and the company's newest capacity is dear (Los Cóndores at about US$7.8M per MW). The rivals' cost
  per MWh cannot be read: Colbún, Engie Energía Chile and GM Holdings, named in the 20-F as the distributor's other principal
  suppliers, and AES Andes, named in the 2020 20-F as "one of our competitors in Chile", do not file with the SEC. The cost
  question is therefore answered by the returns, which are on the record, below.
- *Ask the competitors; widening or narrowing.* The only rival on the SEC record recorded a US$781M asset impairment at AES
  Gener in 2020 on the early termination of two Angamos PPAs and the accelerated retirement of Ventanas 1 and 2, a US$644M
  goodwill impairment at AES Andes in 2022 because "The estimated fair value was less than its carrying amount", a US$137M
  impairment at Norgener in 2023, and saw its 531 MW Alto Maipo hydro project emerge from Chapter 11 in May 2022 (AES
  Corp 10-K for 2020, accession `0000874761-21-000015`; for 2023, `0000874761-24-000011`). Enel Chile's own share of system
  sales moved 42.1% (2023), 44.9% (2024), 40.2% (2025) (Item 4.B), and its regulated volume is shrinking. Narrowing, not
  widening, on the evidence.
- *What could destroy, modify or reduce it.* Solar and battery capacity that sets daytime prices near zero and is being
  "completed faster than new transmission projects" (Item 3.D); drought "for much of the period since 2007"; a state that
  has already rewritten the regulated price three times in five years.

**The competitor row** (same metric from each filer's own filings: operating income over total assets, pre-tax):

| Filer | Metric | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | Source |
|---|---|---|---|---|---|---|---|---|
| AES Corp, Andes SBU (2015-17: Chile, Colombia, Argentina, all owned through AES Gener) / South America SBU (2018-20) | SBU operating margin / SBU total assets | 7.2% | 7.1% | 7.4% | 9.3% | 7.7% | 11.0% | AES 10-K 2017 `0000874761-18-000014`, 10-K 2020 `0000874761-21-000015`, segment notes |
| Enel Chile, consolidated | operating income / total assets | n/r | n/r | n/r | n/r | 7.1% | -0.4% (7.7% before the Bocamina II impairment) | 20-F 2020 |

| Filer | Metric | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| Enel Chile, consolidated | operating income / total assets | 3.0% | 7.5% | 6.8% | 3.1% (8.2% before the hedge loss) | 7.8% |

AES's "operating margin" is before its general and administrative expense and before impairments, so it flatters the
rival against Enel Chile's operating income; the AES SBU after 2018 also holds Brazil and Colombia, and AES changed its
segments after 2020, so the rival's span stops there. **CONVENTION of this run:** where the 20-F names no rival that files
with the SEC, the parent of a named rival (AES Corp, parent of AES Andes / AES Gener) is used through its segment note;
rationale: it is the only filed record of a named rival's economics, and the brief asks for the rivals' own filings.

**The field's returns over the last full cycle, judged in words** (section C; "ordinary" carries no figure). Enel Chile's
operating income after a 27% Chilean statutory rate, over total equity plus net debt, ran 6.5% (2019), -0.4% (2020), 3.2%
(2021), 9.1% (2022), 7.4% (2023), 3.2% (2024) and 8.2% (2025): about 5% on average as filed, about 7% with the Bocamina II
impairment and the 2024 hedge loss added back (compute.py, a CONVENTION of the run for the tax rate). Owner cash after all
spending averaged US$223M a year over 2021 to 2025 on about US$9bn of capital. The rival on the record earned a single
digit before overhead and then wrote off more than US$1.5bn of the capital behind it. Over a cycle that includes a drought,
a fuel spike, three tariff laws and the coal exit, the durable players in this field earned about what a long government
bond pays and destroyed capital where they guessed wrong. That is a standing castle that protects ordinary returns: "you
can have only two competitors and they’re still terrible businesses" **[M2013-052]**, and in a commodity business "the
improvement you get one day, your competitor gets the next day" **[M2004-053]**. A return set by a regulator is the
exception the text allows, "there’s no way we get rich on our utility investments. But there’s no way we get poor,
either" **[M2009-104]**; it describes the distribution part, which does not decide.

**A change for the better?** None shown that the text would credit. Owner cash was higher in 2024 and 2025, but the filing
explains it by the sale of receivables built in 2019 to 2022 and by capital spending falling from US$1,075M (2022) to
US$499M (2025), not by better prices: 2025 carried "a lower average sales price", and the newest twenty-year tender cleared
at US$56.68 per MWh. Operating income in dollars was US$749M in 2019 and US$1,011M in 2025 on capital that grew. The
clause that sends an unproven change to TOO HARD (NATURE) does not arise.

- **VERDICT: OUT.** The deciding part, Generation, sells a commodity at the low bid and at a price its marginal rival sets,
  and the field's durable players earned ordinary returns over the full cycle on their own filings **[L2007-004]**,
  **[M2013-052]**, **[M2017-009]**, **[M2012-109]**; the castle is judged, not measured **[M1999-108]**. The regulated
  return that would be the exception belongs to the part that does not decide **[M2009-104]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict (closed at Q2). The eight to ten balance sheets were read in Step 0 **[M2025-032]**; the facts
found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED (closed at Q2). Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED (closed at Q2). No buyback was made in the window (Item 16E), so no buyback price needs the bottom of Q7's range.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED (closed at Q2). The range and the fair price are computed under AFTER THE STOP, headed COMPUTATION, NOT A
CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2**: the deciding part (Generation, 92.9% of the segments' 2021 to 2025 operating income) sells a commodity at the
low bid and at the price the marginal plant sets, and the field's durable players, Enel Chile and the one named rival on
the SEC record, earned ordinary returns over the full cycle on their own filings. Integrity facts recorded, not judged.
*(Beneath the stop, COMPUTATION, NOT A CLEARANCE: value range US$5.38 to US$7.03 per ADS against US$4.34; no case of the
range earns the floor of about ten percent at the price.)*

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box is unchanged (operator rule 2) **[M1997-127]**.

**Bearing on Q3 (capital).**
- Capital spending ran US$1,035M (2021), US$1,075M (2022), US$789M (2023), US$765M (2024) and US$499M (2025) against
  depreciation and amortization of US$273M to US$387M (cash flow statements; Note 35). Net capacity rose from about
  7,303 MW (2019) to 8,904 MW (2025) while 636 MW of coal closed (Tarapacá 2019, Bocamina I 2020, Bocamina II 2022; Item
  3.D), and generation was 21,041 GWh in 2019 and 21,583 GWh in 2025.
- Los Cóndores, 153 MW run-of-the-river hydro: "The total investment was approximately US$1.2 billion" (Item 4.D).
- The plan for 2026 to 2028 is US$1.8 billion of capital spending, about half for 600 MW of renewables and batteries
  (Item 4.A); battery retrofits approved at US$87M (94 MW), US$170M (206 MW) and US$126M (153 MW).
- After-tax operating income over capital employed (CONVENTION of the run: 27% statutory rate): see Q2.

**Bearing on Q4 (the accounts).**
- Operating cash in 2023 to 2025 includes sales of price-stabilization receivables, and every year includes the factoring
  of short-term receivables (generation subsidiaries sold US$1,677M nominal of them in 2025) and the assignment of
  distribution collection rights (US$840.1M outstanding at 2025-12-31); finance costs of US$20.5M were recognized on these
  in 2025 (Note 9.a.2). Owner cash is therefore lumpy with the laws, not with the business.
- 2024 operating income carries a US$657M loss "from the discontinuation of certain accounting cash flow hedges" when Enel
  Generación Chile moved to a dollar functional currency (Item 5, note 2); 2020 carries the Bocamina II impairment (about
  Ch$713bn); 2025 other operating income includes about US$50M more insurance-claim revenue than 2024 (Item 5.A.2).
- In 2025 the CNE found "a methodological error" that over-billed regulated customers in 2024 and 2025; the company booked
  US$61M of higher financial costs on "the financial restatement of accounts receivable pending invoicing from prior
  years" (Item 3.D; Item 5.A.2).
- The 6-K for Q2 2026 leads with EBITDA ("the Company's EBITDA increased by 3.9% to US$ 685 million"); the segment note
  calls the same measure "Gross Operating Income". A featured EBITDA figure is, under the text, a Q4 weighing carried to
  Q5; recorded here, not weighed.

**Bearing on Q5 (the people): integrity facts recorded, not judged.**
- January 2025: the SEF fined Enel Distribución Chile about US$20M over the August 2024 storm outages for "failure to
  properly maintain its infrastructure; delay in restoring service; failure to provide information to the government in a
  timely manner; and failure to have an adequate system to receive customer complaints and outage reports"; reconsideration
  pending. July 2025: a further fine of about US$8.5M under the Electro-Persons Law; contested. A court-approved
  compensation of US$17.1M to more than 800,000 customers was agreed with SERNAC (Item 3.D).
- SERNAC suits against Enel Distribución Chile: guilty verdicts, under appeal, for the outages of January-February 2021
  and for "alleged violations in the process of contracting insurance" (Note 36.3, items 3.2 and 3.3).
- GasAtacama Chile (merged into Enel Generación Chile in 2019) was fined by the SEF in 2016 "for providing allegedly
  erroneous information to CDEC-SING" on technical parameters for 2011 to 2015; the Court of Appeals reduced the fine from
  10,000 UTA to 500 UTA in April 2019 (20-F for 2019, `0001558370-20-004669`, litigation note). Rivals AES Gener, Eléctrica
  Angamos and Engie Energía Chile sued GasAtacama in 2017; first-instance judgment partly for them (October 2023);
  dismissed by the Court of Appeals of Santiago on 2026-02-04, not yet final (Note 36.3).
- Inversiones Tricahue sued Enel Chile in 2020 for losses "as a result of the corporate restructuring" (ThUS$80,479
  claimed); dismissed in July 2024, on appeal (Note 36.3, item 1.1).
- The controlling shareholder holds 64.93%; the antitrust tribunal's Resolution 667/2002 requires separate generation and
  distribution units with boards "elected from different and independent groups" (Item 4.B); Enel Finance International
  lends US$1,028.6M to the company (Note 10); the risk factor says conflicts "may be resolved in a manner that is different
  from the interests of our company or our minority shareholders" (Item 3.D). Any later run that reaches Q5 must answer
  these first: "If you’ve got doubts, forget it." **[M2013-088]**.

**Bearing on Q6 (the money and the owners).**
- Dividend policy: 15% interim of nine-month income, final payout 50% of the year's net income, paid in pesos (Item 8;
  6-K 2026-04-29). No buybacks in 2025 (Item 16E) and none found in the window.
- 2018: Enel Green Power Latin America, controlled by Enel, was merged into Enel Chile for newly issued Enel Chile shares,
  and the minority of Enel Generación Chile was bought in a tender offer (Item 4.A; shares 49,093M to 69,167M; cash flow
  2018: share issuance Ch$665.8bn, purchases of subsidiaries Ch$1,624.3bn). This is an all-stock deal with the controlling
  shareholder; its price against value was not examined.
- Divestitures: Enel Transmisión Chile sold December 2022 (cash Ch$1,234.5bn); Arcadia's 416 MW of solar sold to Sonnedix
  October 2023.

**Bearing on Q7: COMPUTATION, NOT A CLEARANCE.** *(Q7's construction, carried out because the operator asks for the two
reporting figures; it clears nothing and carries no entry language.)*
- **Basis.** All-equity central (Q7, On what the floor is earned), because the deciding part is market-priced generation
  and the regulated-utility swap applies only "Where the deciding part of a business [...] earns a return a regulator
  allows"; the equity-only figure is beside it. Owner cash after the company's own tax, no conversion; the income tax the
  company paid was at a normal rate (effective 26.4% in 2025), and no carryforward shelter was found.
- **The literal window, 2021 to 2025:** owner cash after all spending US$223.4M a year; after maintenance only (D&A as the
  maintenance guess) US$745.4M.
- **(a) The cycle.** The first window year is aberrational on the filer's own description: 2021 operating cash fell 45.4%
  on a "less efficient generation mix due to dry hydrology conditions and higher commodity prices" (20-F for 2021,
  `0001558370-22-006151`, Item 5.B), hydro output 7,743 GWh against 10,578 GWh in 2019. The base is the cycle peak (2019)
  to peak (2024) of owner cash: **US$700.2M a year after maintenance only, US$195.5M after all spending.** 2018 is left
  out because the merger and the tender offer changed the perimeter and the share count that year; with it the figures
  are US$711.4M and US$259.8M.
- **(b), (f) Growth.** Owner cash after maintenance grew 13.9% a year from 2019 to 2024; carried ten years that needs
  about US$2.6bn a year, far above the highest share of revenue the business has earned in the filings read (31.4%, 2024),
  so by (f) the growth carried is the business's own revenue growth over the same span, **1.39% a year** (US$3,943.5M in
  2019 to US$4,224.8M in 2024), then zero nominal growth after year ten.
- **(c) Acquisitions:** none in the window (cash paid for businesses ThUS$76 in 2023); divestiture proceeds left out and the
  tax on their gains added back, said so in Step 0. **(d) Working capital** is inside operating cash as filed.
- **(e) Maintenance central, and the inversion.** The filing gives one maintenance figure, for distribution ("Network
  maintenance for US$43.6 million" in 2025), and none for generation. The guess is therefore depreciation, which the rows call
  "not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**, a guess stated
  as a guess **[M2000-144]**. The growth spending (capital spending above depreciation, cycle average US$504.7M a year) bought
  growth worth US$1,559M at the sovereign against a cost of US$3,843M over the ten years: the growth bought is worth less
  than its cost, so the maintenance-only no-growth case is the top of the range and the growth case the bottom; "growth
  can destroy value" **[L2000-023]**. A caution the run cannot remove: a good part of the "growth" spending replaced closed
  coal plants, so depreciation may understate what keeps this business in place.
- **The value range (at the US Treasury 30-year, 5.29%), all-equity, central:** enterprise value US$10,952M to US$13,236M;
  less net debt US$3,509M = equity US$7,443M to US$9,727M; **US$0.1076 to US$0.1406 per share, US$5.38 to US$7.03 per
  ADS**, against the price of US$4.34 per ADS (US$0.0868 per share). Width 1.31 to one. Beside it: the literal window on the
  same construction, US$5.98 to US$7.65 per ADS; the equity-only basis, US$5.09 to US$7.04 per ADS; owner cash after all
  spending with no maintenance judgment, US$0.13 to US$0.45 per ADS on the cycle base.
- **The floor, tested first** **[M2003-149]**: at the price, the top case (maintenance-only, no growth, US$700.2M on an
  enterprise value of US$9,512.7M) returns **7.36%**, the growth case less; on the equity-only basis the top case returns
  8.58%. No case in the range earns the floor of about ten percent at US$4.34. Were Q7 reached, it would close OUT by the
  floor convention, whatever the width; the range sits above the price only because it is discounted at 5.29%.
- **The fair price** (Part VII: each end valued at ten percent, the two averaged; after the company's own tax):
  **all-equity, central: US$0.0331 per share, US$1.65 per ADS** (top case US$7,002M, growth case US$4,592M, average
  US$5,797M, less net debt US$3,509M = US$2,288M). **Equity-only, beside: US$0.0557 per share, US$2.79 per ADS.** The
  literal window on the central construction: US$1.96 per ADS. On owner cash after all spending the fair price is not
  positive on the all-equity basis.

**Bearing on Q9 (debt and exposures).**
- Net debt US$3,509M at 2026-06-30 against gross operating income (the segment note's EBITDA) of US$1,473M in 2025 and
  US$764M in 2024; operating income covered interest paid 5.8 times in 2025 (1,011.3 / 174.3) and 1.8 times in 2021
  (341.9 / 188.2) (cash flow statements; Note 35). "earning power that, even under very adverse business conditions, amply
  covers their interest requirements" **[L2010-012]** is the test a later run would put.
- Cross-default clauses at US$150M on the bank facilities and the Yankee bonds (Note 36.4); the US$644M Enel Finance
  International loan amortizes semi-annually from June 2024 to December 2027 (Note 10).
- The stabilization receivables (US$1,324.8M at 2025-12-31) carry a full state guarantee only for the first US$1.8bn
  programme and 30% for the added US$3.7bn (Item 3.D).
- The Taltal mining tort: first-instance joint judgment of ThUS$383,847 against Enel Green Power Chile and a state agency
  (December 2023), on appeal (Note 36.3).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `be4a1d67`); written question by question; committed after each
      (`79b84dcf` Step 0 to Q1, `af80bf75` Q2, and the close).
- [x] Dispatched run: the brief allowed the per-question pathspec commits and states that the dispatching session holds
      the lock and folds the run; this run binds nothing until it is in the register.
- [ ] **The blind rule, one breach declared.** Before reading the blind rule I ran a listing of `Test Runs/` filtered for
      "enic", "enel" and "enersis" (`ls "Test Runs" | grep -i ...`), which counts as searching for files about this
      company. It printed no file name. Nothing else of the blind-listed files was opened, listed or searched. **Contamination
      declared, not used:** the session's opening git log showed commit subjects of another company's run (EDN, closed
      TOO HARD (NATURE) at Q1 on Argentine tariff policy), and the memory index loaded into the session names queue states
      and counts in general terms; none names this company. I read neither, and the EDN outcome was not used; it is
      declared because the regulatory question here is of the same family.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (check script `check_ids.py` in the research folder); every filing
      fact has its document and accession; numbers come from the filings or from `compute.py`.
- [x] The order was kept; Q2 closed the run; everything after it is a fact recorded or a COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the issuing authority (US Treasury);
      the peso sovereign not obtained, confessed, no figure depends on it; the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] `tools/run.py` returned nothing usable; no line of it was used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the commit message).

**Conventions of this run** (each ours, confessed): (1) where the 20-F names no rival that files with the SEC, the parent
of a named rival (AES Corp, parent of AES Andes / AES Gener) is used through its segment note; (2) a 27% Chilean statutory
rate is applied to operating income to state an after-tax return on capital employed in Q2; rationale: the segment and
consolidated tax lines mix the divestiture gains and the hedge loss, and the rate is the statutory one; (3) peso years are
translated at the Banco Central de Chile annual average (flows) and the 20-F year-end rate (balances), the company's own
method for the years it restated; (4) the cycle is drawn 2019 to 2024 and 2018 is left out for the merger, with the
sensitivity shown; (5) the income tax paid on divestiture gains is added back to owner cash because the proceeds are left
out.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Divestitures inside the window.** Q7(c) says "Cash paid for businesses, net of businesses sold, is capital spending
for the range". Read literally, the US$1.4bn received for Enel Transmisión in 2022 would be negative capital spending and
would lift the five-year owner cash by about US$280M a year, crediting the owner with the price of a business he no longer
owns; and the income tax on such a gain sits inside operating cash. I left the proceeds out and added the tax back, but the
text does not say which is meant for a seller. (2) **Working capital that is a state-mandated loan.** Specific (d) counts
the rise in working capital as capital spending, and (a) picks the cycle from owner cash; here the working-capital swing is
the stabilization receivables, built by law in 2019 to 2022 and sold in 2023 to 2025, so the cycle in owner cash is a cycle
of the law, not of the business, and a five-year window can start inside the build-up and end inside the release. The text
gives no rule for receivables that are financing extended at a regulator's order. (3) **The maintenance guess when growth
spending replaced closed plants.** (e) assumes the spending above maintenance buys growth; here much of it replaced coal
plants closed under a decarbonization agreement, so depreciation as the maintenance guess may be too low, and the inversion
paragraph then reads as "growth worth less than its cost" when the spending was in truth stay-in-place. (4) **The
regulated-utility paragraph and a two-part business whose regulated part does not decide.** The text settles the basis by
the deciding part; it does not say whether the regulated part's own debt (distribution carries part of the group's debt)
should be credited on the equity-only figure shown beside. I did not credit it. (5) **The rival rule when no named rival
files.** The brief's instruction and the text both assume a filed rival; I confessed a CONVENTION (the parent's segment
note), but the parent's segment changed its perimeter twice and its "operating margin" is before overhead and impairments,
so the comparison is weaker than the rule implies.
