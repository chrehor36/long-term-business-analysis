- **MGPI (MGP Ingredients, Inc.), 2026-09-20 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 11. Register entry 143** (re-derived by counting the register itself with a
  line-start regex `^- \*\*` inside the slice from this file's `## COMPLETED FROM THE QUEUE`
  **heading line** (line 502, not its earlier textual occurrences) to `## THE WRITE-EARLY
  PROTOCOL`: **142 entries stood above this one**, which agrees with the CE entry directly below
  claiming 142). **Price US$14.13**, close of 2026-09-18 (the last close before the run; the run
  began 2026-09-20 23:49 and finished after midnight), aggregator (Yahoo Finance chart endpoint),
  flagged, raw response on disk at `_research 2026-09-20 MGPI/quote_MGPI_10y_raw.json`.
  **Shares 21,414,076**, from the **cover of the 10-Q for the quarter ended 2026-06-30, accession
  `0000835011-26-000103`, filed 2026-07-29**, as of 2026-07-24 -- *"21,414,076 shares of Common
  Stock, no par value, as of July 24, 2026"*. **TWO equity classes, and the second one matters
  enormously but not to the cap:** Section 12(b) registers only *"Common Stock, no par value"*, and
  the balance sheet carries *"Preferred, 5 % non-cumulative; $ 10 par value; authorized 1,000
  shares; issued and outstanding 437 shares"* -- **437 shares, $4,370 of par, unlisted, no quote**,
  which changes the cap by 0.0014% and is therefore excluded, **while electing five of the nine
  directors and holding the only vote on a merger or a sale of substantially all the assets.** No
  splits in the available history. **Cap re-struck by hand: US$303M** (21,414,076 x $14.13 =
  $302,580,894), against the screen row's **$362M**, which is the same share count at a 16-trading-day
  staler quote of about $16.95 -- **the screen's cap is 20% too high and every yield in this file
  uses $303M.** **Sovereign 5.34%, 09/18/2026, US Treasury daily par yield curve, 30-year, from the
  issuing authority, struck fresh in this run with `tools/sources.py`.** Currency argued, not
  assumed: FY2025 Note 14 puts foreign sales at **$36,497k of $536,375k (6.8%)** and Northern Ireland
  long-lived assets at $5,120k of $327,987k, so USD is the earnings currency on the filed evidence.
  **SIX STEP-0 FLAGS RESOLVED BEFORE Q1 OPENED, AND THE SCREEN'S TWO IMPERATIVES WERE BOTH WRONG.**
  (i) `cap_flag` "cap $362M against a filed float of $423M (1.17x) as of 2025-06-30 ... **One of the
  two is wrong**": **NEITHER IS WRONG, AND THIS IS A THIRD BRANCH.** The FY2025 10-K cover
  (accession `0000835011-26-000031`) reports the float *"on June 30, 2025, was approximately $ 423
  million"*; MGPI closed at **$29.97** that day, so $423,000,000 / $29.97 = **14,114,782 implied
  non-affiliate shares** against *"21,292,736 shares of Common Stock ... as of July 25, 2025"* (Q2
  2025 10-Q, accession `0001628280-25-036842`). **Float is a genuine 66.3% subset and an affiliate
  block of ~7.18M shares (33.7%) is real -- the MCFT branch, not the CE branch** -- and the same
  14,114,782 float shares at the screen's $16.95 strike are worth **$239M against a cap of $362M**.
  **The whole of the 1.17x is the price: $29.97 to $16.95 is a 43% fall, and $29.97 to $14.13 is 53%.**
  (ii) `deal_note` "most likely a credit facility or offering; **open them only if something else is
  odd**": **OPENED, AND IT IS THE SHARPEST DOCUMENT IN THE FILE -- the third consecutive run where
  that clause would have hidden the best finding** (CGNX, CE, now MGPI). 8-K filed 2026-08-07,
  accession `0000835011-26-000108`, Item 1.01, **two** exhibits: *"the definition of Consolidated
  EBITDA was modified to permit the Company to add back, for any period on or prior to December 31,
  2027, **aggregate losses up to $20,000,000 related to accounts receivable from specific
  customers**"*, and *"**The Company has exercised its option for an Elevated Ratio Period**,
  commencing with the fiscal quarter ended June 30, 2026 and for the three fiscal quarters
  thereafter, in connection with the earnout obligations for the acquisition of Penelope Bourbon
  LLC"* -- **the net leverage covenant stepped from 4.00x to 4.50x using a permitted-acquisition
  clause invoked for an earnout PAYMENT on a 2023 deal** -- and the filer's own *"The Company
  continues to believe that **the third fiscal quarter of 2026 will represent its peak leverage**."*
  Against that $20,000,000 carve-out, the Q2 2026 10-Q books an allowance of **$2,148k** for a
  significant customer that *"filed a voluntary petition for reorganization under Chapter 11"* on
  2026-07-26: **relief negotiated at roughly nine times the loss disclosed, and the 10-Q reader is
  never given the $20M figure.**
  (iii)/(iv) `level_shift 1.94`, `best_year_dep_oe 0.225`, `flags_disagree`, `window_disagree`:
  **both series reproduced exactly from the filings** -- the 5-year (2021-2025) owner-earnings mean at
  the total-capex end of (c) is **$37.9M** (screen `oe_bottom_m 38`) and the 3-year (2023-2025) mean
  at the D&A end is **$73.3M** (screen `oe_top_m 73`); the disagreement is because the capex-end
  series is **-$0.7M in 2018 and -$0.3M in 2019** and refuses a ratio. **The OCF level step is 2020
  to 2021 and it is the LUXCO MERGER, not a cycle** (2017-2020 mean $35.0M against a 2022-2025 mean
  $99.1M). The 17 annual periods also contain a **fiscal-year change**: 10-Ks run to June 30 through
  FY2011 and to December 31 from 2011-12-31, so **the six months to 2011-12-31 are absent from every
  annual series.**
  (iv) **THE PERIMETER, and it is the finding that would have closed the file at Q4 had Q2 not:
  THERE IS NO FIVE-YEAR WINDOW ON ONE PERIMETER** ([E2-42], [E1-03]). Three companies inside 17
  periods: industrial alcohol and wheat proteins to FY2011; two segments FY2012-FY2020; then **Luxco
  2021-04-01** (which created Branded Spirits), **Penelope 2023-06-01**, the **Atchison distillery
  closed December 2023** (white goods and co-products $133,031k to $32,901k to $20,562k), and
  **distilling idled at two of three distilleries from 2026-05-01**. Luxco in, Penelope in, Atchison
  out leaves **FY2024 and FY2025 -- two years.** The BN shape of the same morning.
  (v) `acq_note` "acquisitions are $253M, 70% of cap": **the brief's prediction confirmed to the
  dollar, and the largest perimeter understatement recorded in this project -- the seventh
  consecutive one.** The screen's $253M is $149.0M + $103.7M, the **investing-cash line only**. The
  filings give Luxco at *"Fair value of total consideration transferred | $ 445,763"*, of which
  ***"Value of MGP Common Stock issued at close (a) | 296,279"*** -- 5,009,206 shares, *"approximately
  22.8 percent of the Company's outstanding common stock immediately following the closing"* -- plus
  Penelope at $104,638k cash **and the full $110,800k earnout, whose maximum was achieved in Q3 2025
  and which was paid in H1 2026** ($48,700k through operating and $62,100k through financing, funded
  by $145,000k of revolver draw). **Total $661.2M, or 218% of the hand-struck cap, not 70%.** The
  documented source limit held and was not re-tested:
  `BusinessCombinationConsiderationTransferred1` and its equity sibling do not resolve undimensioned
  in companyfacts, so both the stock leg and the earnout leg were read by hand out of the notes.
  (vi) `wc_note` **EMPTY, and that was the tool's blind spot the brief predicted.** Reported operating
  cash flow **rose 45% from $83.8M (FY2023) to $121.5M (FY2025) while operating cash flow BEFORE
  working capital FELL 42%, from $163.4M to $95.3M** -- FY2025 released **$32.2M** of receivables as
  sales fell 24%, turning FY2024's $47.2M of working-capital absorption into a $26.2M release. **A
  shrinking business releases working capital; that is not earnings.** H1 2026 operating cash flow is
  **negative $40.7M**. Barrelled distillate is **$301,665k of $382,741k of inventory (78.8%), 24.4%
  of total assets, all classified current**; cumulative inventory build 2015 to H1 2026 is
  **$273.8M**; and the FY2026 capex plan of *"approximately $20 million"* is **below D&A of $24.1M**,
  against a 2021-2025 capex mean of $53.0M (2.4x D&A). **[E2-60]** is the row: the 2026-27 cash-flow
  statements will look better while the business is made smaller.
  **ALL THREE OF THE BRIEF'S UNVERIFIED RECOLLECTIONS CONFIRMED, two of them larger than briefed:**
  the branded-spirits impairment is **three** consecutive events ($73,755k Q4 2024, $152,622k Q4 2025,
  $180,277k Q1 2026 = **$406,654k in five quarters, 61% of everything paid for the acquisitions**);
  the CEO change effective 2025-01-01 was an **interim** appointment (CFO Brandon Gall) with the
  permanent CEO, Julie Francis, from 2025-07-21; and the production cut is the **temporary idling of
  distilling at Limestone Branch and Lux Row from 2026-05-01** (8-K 2026-04-07, accession
  `0000835011-26-000052`).
  **THE GATE. [E3-03] criterion 2 fails on the filer's own numbers for the legs carrying 42.2% of
  FY2025 gross profit, and the commodity doctrine [E2-58] is stated by the subject company about its
  own market, over the CEO's name, in a furnished exhibit:** *"The American whiskey market continues
  to be **structurally oversupplied, with excess capacity and elevated inventory**."* The physical
  series **[E4-55]** is published by the filer and is decisive: **brown goods total (52)%, VOLUME
  (46)%, net price/mix (6)%** in FY2025, with the FY2024 MD&A adding *"instances of **customer
  contract non-performance**"*. Ingredient Solutions gross margin **35.6% to 20.1% to 12.7% to 10.1%**
  (Q2 2026) on *"higher waste starch stream costs"*. Branded Spirits splits: premium plus **+10.7%**
  over two years (Penelope **+13%** in Q2 2026) against mid **(21.4)%** and value **(31.9)%**, and the
  company's own valuation specialist says the trade-name write-down *"were most impacted by declines
  in the mid and value price tiers."*
  **THE COMPETITOR ROW, and the CENSUS IS SOURCED FROM A PEER'S OWN FILING as [E3-28] requires.**
  Brown-Forman's 10-K for FY ended 2026-04-30 (accession `0000014693-26-000024`) names the industry:
  *"Bacardi Limited, Becle S.A.B. de C.V., Davide Campari-Milano N.V., Diageo PLC, LVMH Moet Hennessy
  Louis Vuitton SE, Pernod Ricard SA, Remy Cointreau, and Suntory Global Spirits."* **Eight named and
  exactly ONE files with the SEC (Diageo, on 20-F) -- the industry is structurally unmeasurable from
  SEC filings, and that limit is stated rather than papered over. Brown-Forman's own competitor list
  does not contain MGP Ingredients, and neither does any other filer's:** an EDGAR full-text search
  for `"MGP Ingredients"` in Form 10-K from 2024-01-01 to 2026-09-20 returns **38 hits, 21 of them
  MGPI's own filings** and the rest board-overlap and unrelated. **5 peers attempted, 4 producing the
  metric.** Operating margin from each filer's own XBRL: **MGPI is THIRD OF FOUR on the 9-year mean
  (11.4%, against Ingredion 10.8%, Constellation 26.9%, Brown-Forman 31.7%) and LAST OF FIVE on the
  recent three-year mean (3.6%, against Ingredion 12.6%, Diageo 18.9%, Constellation 21.7%,
  Brown-Forman 29.0%).** On gross margin MGPI (31.7-40.7%) is **never within eighteen points of
  Brown-Forman (58.9-60.8%) in any year** and sits between a starch processor (Ingredion 19-25%) and a
  spirits company (Diageo ~43%). **Ex-impairment does not move the rank: FY2023 20.1%, FY2024 21.1%,
  FY2025 10.8% -- below Brown-Forman's worst year of the decade.** **The row's own limit is stated
  [E3-61]: it cannot measure the leg carrying 34% of gross profit at all, because MGPI's
  contract-distilling rivals are private or foreign and file nothing.** [E2-58] does not need the row
  to reach its conclusion; the row would be needed to establish **the exception** -- *"a cost
  advantage that is both wide and sustainable ... By definition such exceptions are few"* -- and the
  exception is what is missing. **[E4-36] and [E3-51]:** the 2020-to-2021 cash-flow step IS the Luxco
  merger and the rest was the wave the filer now says has turned; *"a surfing run is not a moat."*
  **[E4-04] IS NOT INVOKED** -- under the 2026-09-20 amendment it is a competence limit, and on the
  branded leg alone it would give UNKNOWABLE without prejudice; **the OUT rests on [E3-03] and
  [E2-58], which are findings about the business.**
  **Q3-Q6 recorded beneath the close WITHOUT VERDICTS (operator rule 2).** Q3 weight case: **daily
  execution and leverage both ticked, so Q3 would have been a BINARY GATE.** **[E4-29] fires at the
  largest gap this project has recorded: the DEF 14A of 2026-04-09 pays the executives 94-98% of
  target on *"Adjusted Operating Income | 70 | 89.2 million | 95"* in the same FY2025 whose filed
  statement reads *"Operating income (loss) | ( 94,615 )"* -- a $183.8M gap in one year**, with GAAP
  basic EPS of **$(4.99)** against an incentive figure of **$2.91**; the Q4 release headline is
  *"Full-year results above the top end of guidance"* and calls the $152.6M impairment *"a discrete,
  non-cash **adjustment**."* **[E4-22]'s third flag fires** on guidance reaffirmed even inside the
  distillery-idling release, and **[E3-48]'s action shows guided adjusted EBITDA falling 56% in two
  years** ($218-222M confirmed 2024-08-01, cut to $196-200M on 2024-10-17, a $120.0M STI target for
  2025, $90-98M for 2026) -- with the outgoing CEO calling the glut *"temporary"* in October 2024 and
  his successor calling it *"structurally oversupplied"* eighteen months later. **[E2-49] DOES NOT
  FIRE: its sixth failure** -- the STI metrics and weightings are identical across the 2023, 2024,
  2025 and 2026 proxies (Adjusted Operating Income 70%, Adjusted EBITDA 20%, Adjusted Basic EPS 10%)
  -- though the targets were reset down a third, a discretionary +$1.6M tariff adjustment was granted
  in the participants' favour, and the PSU performance period was **shortened to one year**; the
  single-to-double-trigger change ran the other way and is recorded as such **[E2-69]**. **[E3-54]
  retention fails hard: $182.8M retained from 2020-12-31 to 2025-12-31 against a market-value change
  of MINUS $277.9M**, before crediting the $296.3M of stock issued in 2021, and the stock is 88.7%
  below its 2022-11-25 high of $125.50. **[E5-08]/[E5-24]:** 886,936 shares bought back in 2024 at an
  average of **$52.53** against today's $14.13, in the same fiscal year whose Q4 impairment test cites
  *"a decrease in stock price and market capitalization"* as evidence the assets were worth less.
  **[E2-01]:** return on equity 18.5/16.8/15.4% (2018-2020) against 14.2/14.7/12.6/4.2/(15.0)%
  (2021-2025) -- **the pre-acquisition company earned more on its equity than the post-acquisition
  company did in any year** -- while **[E2-43]**'s unleveraged net tangible assets denominator gives
  46.6% (2024) and 16.2% (2025) ex-impairment, which is the kindest number in the file: **the
  operation is not the problem; the price paid for it was.** Q4, recorded: **great/good/GRUESOME**
  [E4-20] -- roughly **$1.15bn deployed since 2015** ($661.2M of acquisitions, $219.2M of 2021-24
  capex, $273.8M of inventory) to reach FY2025 sales of $536.4M against FY2020's $395.5M and a $303M
  cap. **All three [E5-11] strengths fail, and the third is the killer: $201,250k of Convertible
  Senior Notes is PUTABLE AT PAR ON 2026-11-15** -- conversion price $96.24 against a $14.13 share --
  and the FY2025 10-K states *"We expect some holders of the Convertible Senior Notes to require the
  Company to repurchase the Convertible Senior Notes during the fourth quarter of 2026"*, against cash
  of **$17,794k** and $338,000k of undrawn revolver that **[E5-39]** refuses to count. Refinancing that
  paper from 1.88% onto the 4.99% revolver costs about **$6.3M a year more**, taking cash interest from
  $9.4M toward $18-19M; **[E2-54]** coverage lands near **2.0x** -- met, not *"comfortably"* met. The
  named death, quantified **[E3-24]**: barrels realising 75 cents on a $301,665k carrying value is a
  **$75.4M** charge that consumes covenant headroom without the business stopping working --
  **A REAL POSSIBILITY.** Survival shape: **#20 THE WAVE** with **#11 THE PASS-THROUGH** and **#5 THE
  SELF-LIQUIDATING DISTRIBUTION** as features, **recorded on the PAGP precedent as THE SIGNATURE
  WITHOUT THE VERDICT and deliberately not counted as an instance, because Q4 was never reached.**
  **THE UNCOMFORTABLE PART: THE PRICE WAS NEVER THE PROBLEM.** At the hand-struck $303M cap the
  owner-earnings yield is **12.5% at the screen's bottom end and 24.1% at its top**, 16.2% on the only
  one-perimeter window at the capex end, and **13.5-19.0% even at my own harshest (c) of $50M** -- all
  of it clearing the ~10% floor **[E4-28]**, with the screen's `growth_required` at **-0.48%**.
  **A run that went to the arithmetic first would have passed this name.** It fails because
  **[E5-42]** puts the business first, and because the numerator's best year contains $26.2M of
  working-capital release from a shrinking business while the denominator is 88.7% off its high: **a
  high yield on a melting numerator against a collapsing denominator is not a discount, it is a
  description.** **NO PRICE ALERT AND NO `PORTFOLIO.md` ROW (the QLYS ruling): a business failure gets
  a reversal condition in words.** **REVERSAL CONDITION:** four consecutive quarters of **brown-goods
  VOLUME** growth in the filer's own attribution table (dollars will not do -- **[E4-55]**), with
  **barrel inventory FALLING rather than rising**, and the 2041 Notes retired or refinanced without
  materially raising cash interest. A lower price, an adjusted-EBITDA beat, a reaffirmed guidance range
  or a premium-plus growth rate would **not** re-open it. Run file:
  `Test Runs/2026-09-20 Run - MGPI MGP Ingredients.md`; research
  `Test Runs/_research 2026-09-20 MGPI/`.
