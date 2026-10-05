# Company Run: The Wendy's Company (NASDAQ: WEN), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated name before any fetch. Every judgment cites a v5 ledger id
in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions
are marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-05 WEN/` (every filing named below is saved there as
text, with its source URL and accession on its first two lines).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` was not opened, under the blind rule of
this run. The analyst does not know whether the operator holds WEN.

**CONTAMINATION, declared:** no prior WEN run, research file or register entry was opened. Seen without opening: the
commit subjects in the session's git snapshot (runs of WSC, CAG and GIII, a small-cap triage screen) and the names of
three untracked 2026-10-05 run files (ABG, AHCO, EFOR); the session memory index line "57 gate-clearers, nothing
buyable". None concerns WEN or a restaurant franchisor. `tools/run.py` printed arithmetic only (Part VII); nothing it
printed as a rule was used.

---
## STEP 0 - THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $6.10 (2026-10-05, Yahoo Finance chart via `tools/sources.py`; **aggregator, live quote only**, flagged
  per operator rule 5). The same source gives a 2025 range of $7.87 to $16.17 and a 2021 high of $28.87.
- **Shares:** one class, 190,669,930 common shares outstanding at 2026-07-31 (cover of the 10-Q for the quarter to
  2026-06-28, filed 2026-08-07, accession `0000030697-26-000116`; `python Screens/cover_shares.py WEN`). 470,424
  thousand issued, the rest in treasury.
- **Market cap:** about $1,163M (190.67M x $6.10).
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 2026-10-02
  (`python tools/sources.py`; the issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (period 2025-12-28, filed 2026-02-23, `0000030697-26-000009`);
  10-Q for Q2 2026 (`0000030697-26-000116`); proxy statement DEF 14A filed 2026-04-02 (`0001193125-26-140220`); 8-Ks of
  2025-07-08 (`0001193125-25-156450`), 2025-07-22 (`0001193125-25-162611`), 2025-07-30 (`0001193125-25-169324`),
  2025-11-12 (`0001193125-25-276128`), 2025-11-20 (`0001193125-25-288625`), 2025-12-16 (`0001193125-25-321131`),
  2026-05-20 (`0001193125-26-231809`), 2026-05-22 (`0001193125-26-236835`), 2026-06-09 (`0001193125-26-263775`),
  2026-06-23 (`0001193125-26-278576`), 2026-07-28 (`0001193125-26-321244`), 2026-08-17 (`0001193125-26-354008`); the
  earnings releases (Exhibit 99.1) of 2025-11-07 (`0001193125-25-271014`), 2026-02-13 (`0001193125-26-049816`) and
  2026-08-07 (`0001193125-26-339132`); Trian's Schedule 13D/A No. 61 (`0000950170-24-095003`) and No. 62
  (`0000950170-24-104437`); and every WEN 10-K for FY2010 to FY2024 for the fifteen-year series (accessions in the
  competitor and history rows below and in `_research 2026-10-05 WEN/`).
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025, $344,543
  thousand on the filed cash-flow statement (10-K, `0000030697-26-000009`), against $344.5M in `tools/run.py`'s XBRL
  transcription. They agree.
- **`tools/run.py WEN` arithmetic lines** (checked line by line against the filed cash-flow statements):

| FY | OCF | stock pay | capex | franchise development fund | finance-lease principal | **owner cash** | D&A |
|---|---|---|---|---|---|---|---|
| 2021 | 345.8 | 22.0 | 78.0 | 0.0 | 13.6 | **232.2** | 125.5 |
| 2022 | 259.9 | 24.5 | 85.5 | 3.6 | 17.3 | **129.0** | 133.4 |
| 2023 | 345.4 | 23.7 | 85.0 | 8.0 | 21.6 | **207.1** | 135.8 |
| 2024 | 355.3 | 23.0 | 94.4 | 41.2 | 20.4 | **176.3** | 143.2 |
| 2025 | 344.5 | 14.6 | 101.9 | 38.4 | 24.5 | **165.1** | 152.2 |
| H1 2026 | 160.0 | 8.2 | 31.4 | 11.0 | 12.1 | 97.3 (half year) | 78.6 |

  USD millions. Owner cash = operating cash flow less stock pay, capital expenditures, the franchise development fund
  (cash the company puts into franchisee new builds, filed as an investing line) and finance-lease principal (filed as
  a financing line). OCF is already after interest and cash taxes. Sources: the FY2022 10-K (`0000030697-23-000002`)
  for 2021-2022 lines, the FY2025 10-K for 2023-2025, the Q2 2026 10-Q for the half year. The run.py "capex alt" column
  is this definition; its as-filed column (capex only) gives 236.6 / 237.9 / 228.0 for 2023-2025 and is not used,
  because the fund and the lease principal are real outlays. **Five-year average owner cash: $181.9M.** Depreciation
  variant (D&A in place of capex): 184.7 / 81.1 / 156.3 / 127.5 / 114.8, average $132.9M. Where maintenance sits: capex
  ran below D&A in every year of the five (78 to 102 against 126 to 152), with D&A swollen by finance-lease
  amortization and acquired-franchise amortization; the filings do not split maintenance from growth capex, so the
  capex basis is used and the D&A basis is shown. Acquisitions (2021 $123.1M for 93 Florida restaurants; 2025 $16.9M)
  are growth outlays and are left out of both.

  Abnormal years in the window: 2021 (U.S. same-restaurant sales +9.2%, the post-2020 rebound) and 2022 (operating cash
  of $259.9M, depressed by working-capital swings). H1 2026 owner cash is held up by working capital (a $1.4M outflow
  against $45.9M in H1 2025) while pre-tax income fell 36.8% ($82.7M against $130.8M).

**The balance sheets first, ten year-ends, read before the income account** **[M2025-032]**, done here because the file
closes before Q4 (`tools/run.py` table, checked against the filed FY2016 and FY2025 balance sheets):

| year-end | total assets | equity | goodwill | intangibles | cash | receivables | long-term debt (incl. current) | shares out (M) |
|---|---|---|---|---|---|---|---|---|
| 2016-01-03 | 4,109 | 753 | 771 | 1,340 | 327 | 105 | 2,426 | 272.3 |
| 2017-01-01 | 3,939 | 528 | 741 | 1,323 | 198 | 99 | 2,512 | 246.6 |
| 2018-12-30 | 4,292 | 648 | 748 | 1,294 | 431 | n/t | 2,329 | n/r |
| 2021-01-03 | 5,040 | 550 | 751 | 1,225 | 307 | 94 | 2,247 | n/r |
| 2023-01-01 | 5,499 | 466 | 773 | 1,249 | 746 | 99 | 2,851 | n/r |
| 2024-12-29 | 5,035 | 259 | 771 | 1,192 | 451 | 100 | 2,740 | 203.8 |
| 2025-12-28 | 4,957 | 117 | 774 | 1,171 | 301 | 117 | 2,760 | 190.3 |

USD millions; n/t not tagged that year, n/r not read. FY2016 balance sheet in the FY2016 10-K (`0000030697-17-000002`);
FY2025 in `0000030697-26-000009`. What the figures say: (1) equity fell from $753M to $117M while goodwill and
intangibles stayed near $1.95-2.11B, so tangible equity is about -$1.83B at FY2025; (2) treasury stock rose from
$1,741M to $3,287M and shares outstanding fell from 272.3M to 190.3M, paid for with securitized debt (long-term debt
$2.40B to $2.73B) and with the cash raised in 2022 (cash $746M at 2023-01-01, $301M at 2025-12-28); (3) lease
liabilities now stand beside the debt: finance leases $673M and operating leases $711M at FY2025 (the jump in total
assets between the 2018 and 2019 year-ends is consistent with the lease standard bringing them on; the finance-lease
line grew from $598M to $673M in 2025 alone); (4) receivables net of allowance
are steady in amount, but the allowance for doubtful accounts went from $2.7M (end 2023) to $7.3M (end 2024) to $20.9M
(end 2025), with a $16.0M provision in 2025 (FY2025 10-K, receivables note); (5) properties fell from $1,228M to
$938M as company restaurants were sold to franchisees, while net investment in sales-type and direct financing leases
($285M) appeared as land and buildings were leased to them. What they do not say: franchisee profitability. No
franchisee cash-flow or margin figure was found in the 10-K, the 10-Q or the proxy (text search: "franchisee
profitab", "franchisee economics", "franchisee EBITDA", "cash flow margin"); the CEO named it in words only (Q2 below).
What they cannot say: whether the equity drawn down into buybacks bought value. That is Q6, NOT REACHED.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the buyer would be content to own Wendy's royalty, rent and restaurant
streams "if the market closed for five years" **[M1997-109]**, which turns the question onto U.S. traffic and the
franchisees, not onto a price that has fallen from $28.87 to $6.10. The market "just tells us prices" **[M2006-077]**,
and the fall is not evidence of value either way. The analyst's habits govern this file: "I’m looking for what’s wrong
in things" **[M2025-013]**, and the hardest-hunted evidence was the evidence that a low price is a bargain, since that is
the conclusion a falling quote invites. Margin of safety enters only as attitude: a case that needs a pencil "it’s too
close to think about" **[M1996-084]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. (found first, against the business) U.S. same-restaurant sales -5.6% in 2025 and -7.4% in H1 2026, "primarily due
   to a decrease in traffic, partially offset by higher average check" (10-K FY2025; 10-Q Q2 2026).
2. (against the business) In the same half year Burger King U.S. comparable sales were +7.2% and McDonald's U.S. +2.3%
   (QSR 10-Q `0001618756-26-000045`; MCD 10-Q `0000063908-26-000073`).
3. (against the business) 286 U.S. franchised restaurants closed in H1 2026, against 40 opened (10-Q Q2 2026,
   restaurant count table); the system lost 217 restaurants net in six months.
4. (against the business) The new CEO, 2026-08-07: "Our traffic, our value proposition and franchisee economics are not
   meeting our expectations" (Exhibit 99.1, `0001193125-26-339132`). 2026 outlook withdrawn; dividend cut from $0.25
   (Q1 2025) to $0.14 to $0.07 a quarter.
5. (against the business) Four chief executives or interim chiefs in thirty months: Penegor departed February 2024;
   Tanner served 2024-02-05 to 2025-07-18 and left for Hershey; Cook was interim to 2026-05-21 and was terminated as CFO
   without cause effective 2026-07-31; Wright from 2026-05-21. The chief accounting officer resigned 2026-06-04 and the
   President, U.S. resigned 2026-08-14 (8-Ks listed in Step 0).
6. (for the business, written down as found) Over 2017-2025 Wendy's U.S. same-restaurant sales compounded to about
   +21%, ahead of Burger King U.S. at about +18% (computed below); Burger King itself fell to -5.6% in 2020 and came back,
   which shows a number-two burger brand's sales can be rebuilt.
7. (for the business) Wendy's U.S. company-operated restaurant margin, 14.2% in 2025, is above McDonald's U.S.
   company-operated margin of about 11.6% the same year ($360M on $3,115M, MCD 10-K FY2025 `0000063908-26-000035`),
   and McDonald's own U.S. company-operated margin dollars fell 15% in 2024 and 14% in 2025: margin compression is
   industry-wide, not Wendy's alone.
8. (for the business) International systemwide sales grew 8.1% in 2025 and 4.6% in H1 2026 at constant currency, and
   digital sales reached 23.7% of systemwide sales in Q2 2026.
9. (for the price, against nothing in the business) At $6.10 the five-year owner cash is a 15.6% yield on the market
   cap. Written down because it is the strongest pull toward a wrong conclusion in this file.

## THE STANDING RULE
Owning WEN shares bought with cash and sized so that a total loss could not touch what the buyer needs does not put the
buyer at risk of ruin; the rule binds the buyer's financing, and "borrowed money has no place in the investor's tool
kit" **[L2014-005]**; "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**. The target's own debt is Q9, NOT REACHED; its facts are recorded in the computation section.

---
## Q1 - CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**. The economics are simple and are in the filings: Wendy's takes royalties
  (franchise royalty revenue $504.5M in 2025) and rents ($235.8M) as a percentage of franchisee sales and on property it
  owns or leases and sublets, runs 423 U.S. and 11 international restaurants itself (sales $916.3M), and passes the
  advertising funds through (revenue $422.1M, expense $422.6M). Operating profit $343.5M, interest $126.5M, pre-tax
  $227.2M in 2025 (10-K FY2025, results table).
- **The key variables** **[M1998-044]**: U.S. systemwide sales (traffic times check) and the number of U.S. restaurants,
  which together set the royalty and rent base; the franchisees' ability to pay rent and to build. The speakers name the
  second variable for franchisors in so many words: "you have to have a good business for the franchisee to, over time,
  have a good business for the parent company" **[M1998-164]**.
- **Is it foreseeable in kind?** This is a consumer business, not a technology one; the forecast is "in terms of consumer
  behavior and threats to a business" in the sense of **[M2023-030]**, and the speakers read such a business as "much more
  of a consumer products business" **[M2017-019]**. The industry does not change fast; the product is fifty-seven years
  old. The routing sentence (rapid change closes at Q1 TOO HARD) does not apply: drive-through hamburgers are not "lots of
  change coming" **[M1999-063]**.
- **The doubt, stated.** "if you have doubts about something being into your circle of competence, it isn’t"
  **[M2002-092]**. The doubt in this file is not about how the business makes money; it is about where Wendy's will stand
  against McDonald's and Burger King, which is the castle question Q2 owns. The speakers say of the food business itself
  that "you would never get the total certainty of dominance" and "People move around in the food business"
  **[M1997-001]**, and that "convenience is a huge factor" **[M1997-139]**: that is a statement about the castle, carried to
  Q2, not about the analyst's grasp of the economics.
- **VERDICT: IN.** The earning mechanism, its key variables and their sources are understood from the filings
  **[M2012-065]**, **[M1998-044]**; the industry is not one of rapid change **[M1999-063]**.

## Q2 - WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**, with the 1995 test of what destroys or reduces it,
"destroy, or modify, or reduce the economic strengths that we perceive currently exist in a business" **[M2000-014]**.

**The competitor row** (same metric, the competitors' own filings; U.S. comparable or same-restaurant sales, % change):

| year | WEN U.S. systemwide | MCD U.S. | BK U.S. (QSR) | JACK system (Jack in the Box) | Taco Bell (YUM) |
|---|---|---|---|---|---|
| 2011 | +1.9 | +4.8 | n/r | n/r | n/r |
| 2012 | +1.6 | +3.3 | n/r | +3.4 | n/r |
| 2013 | +1.8 | -0.2 | -0.9 (US & Canada) | +0.3 | n/r |
| 2014 | +1.6 | -2.1 | +2.1 (US & Canada) | +2.0 | n/r |
| 2015 | +3.3 | +0.5 | n/r | +6.5 | n/r |
| 2016 | +1.6 | +1.7 | n/r | +1.2 | n/r |
| 2017 | +1.9 (U.S.) / +2.0 (N.A.) | +3.6 | +2.5 | +0.5 | n/r |
| 2018 | +0.6 | +2.5 | +1.4 | +0.1 | n/r |
| 2019 | +2.9 | +5.0 | +1.7 | +1.3 | n/r |
| 2020 | +2.0 | +0.4 | -5.6 | n/r | n/r |
| 2021 | +9.2 | +13.8 | +4.7 | +10.3 | n/r |
| 2022 | +3.9 | +5.9 | +2.2 | +0.9 | +8 (division) |
| 2023 | +3.7 | +8.7 | +7.5 | n/r | n/r |
| 2024 | +1.4 | +0.2 | +1.2 | -1.3 | n/r |
| 2025 | **-5.6** | +2.1 | +1.6 | -4.2 | +7 (division) |
| H1 2026 | **-7.4** | +2.3 | +7.2 | -4.4 (franchise, YTD to 2026-07-05) | n/r |
| compounded 2011-2025 | about +36% | about +62% | | | |
| compounded 2017-2025 | about +21% | about +50% | about +18% | | |

Sources and accessions: WEN 10-Ks FY2011 (`0000030697-12-000007`), FY2013 (`0000030697-14-000006`), FY2014
(`0000030697-15-000003`), FY2016 (`0000030697-17-000002`), FY2018 (`0000030697-19-000004`), FY2019
(`0000030697-20-000002`), FY2020 (`0000030697-21-000002`), FY2022 (`0000030697-23-000002`), FY2025; 2011-2018 are North
America (U.S. and Canada), the series the filings gave before 2019; 2014-2016 on the new method of the FY2016 10-K (old
method 1.6 / 3.3 / 1.5). MCD 10-Ks FY2013 (`0000063908-14-000019`), FY2016 (`0000063908-17-000017`), FY2019
(`0000063908-20-000022`), FY2022 (`0000063908-23-000012`), FY2025 (`0000063908-26-000035`), 10-Q Q2 2026. QSR 10-Ks FY2014
(`0001193125-15-072217`), FY2017 (`0001618756-18-000007`), FY2018 (`0001618756-19-000005`), FY2019
(`0001618756-20-000004`), FY2020 (`0001618756-21-000007`), FY2021 (`0001618756-22-000018`), FY2022
(`0001618756-23-000013`), FY2024 (`0001618756-25-000087`), FY2025 (`0001618756-26-000017`), 10-Q Q2 2026
(`0001618756-26-000045`; BK segment, "Comparable Sales - US"). JACK 10-Ks FY2016 (`0000807882-16-000036`), FY2019
(`0000807882-19-000023`), FY2022 (`0000807882-22-000017`), FY2025 (`0000807882-25-000072`), 10-Q to 2026-07-05
(`0000807882-26-000091`); JACK fiscal years end in September or October. YUM 10-Ks FY2022 (`0001041061-23-000009`) and
FY2025 (`0001041061-26-000084`), Taco Bell Division worldwide same-store sales, mostly U.S. n/r = not read in this run.
The compounded figures are this run's arithmetic on the rows above; Burger King's 2015-2016 were not found by the text
search used ("U.S. and Canada", "US&C") and the BK span starts 2017.

**Units and margins over the span.** Wendy's restaurants in North America: 6,244 at 2012-01-01 (10-K FY2011), 6,178 at
2018-12-30 (10-K FY2018); in the U.S.: 5,852 at 2019-12-29, 6,030 at 2023-12-31, 5,969 at 2025-12-28, 5,724 at
2026-06-28. McDonald's U.S.: 14,098 (2011) to 13,457 (2023) to 13,706 (2025). Neither grew U.S. units over the span;
McDonald's added 249 U.S. restaurants in 2024-2025 while Wendy's lost 306 U.S. restaurants net from end-2023 to mid-2026.
Company-operated restaurant margin: Wendy's 14.0% (2011, "Total Wendy's restaurant margin", 10-K FY2011) to 13.6% global
(2025) to 12.3% (H1 2026); McDonald's U.S. 20.6% (2011, 10-K FY2013 table) to about 11.6% (2025). Average unit volume:
Wendy's company-owned $1,456.4 thousand (2011) to U.S. company-operated $2,241.3 thousand (2025); U.S. systemwide
$2,098.2 thousand (2024) to $2,001.3 thousand (2025).

**The castle tests, each with its filing fact.**
1. **What keeps it standing; the key factors and how permanent** **[M1995-038]**. The filings' own answer is quality
   (fresh beef, made to order), a fifty-seven-year-old brand, 5,724 U.S. locations, and the Frosty and Baconator names
   (10-Q Q2 2026, Item 2). The locations are the permanent factor in a business where "convenience is a huge factor"
   **[M1997-139]**, and they are shrinking: 315 restaurants closed systemwide in H1 2026 against 98 opened.
2. **Pricing power and the agony before a rise** **[M2005-020]**. Same-restaurant sales "decreased due to a decrease in
   traffic, partially offset by higher average check" in 2025 and H1 2026; customer counts also fell in 2023 and 2024
   while check rose (10-Ks FY2023 `0000030697-24-000004` and FY2024 `0000030697-25-000003`, results text). Price has been
   bought with traffic for three years. The positive form, "Anytime you can charge more for a product and maintain or
   increase market share against wellentrenched, well-known competitors" **[M2000-031]**, is failed in its second half:
   the price rose and the share fell. The new CEO lists "rebuilding a quality menu at compelling value" first among the
   five fixes (Exhibit 99.1, 2026-08-07): the prayer session is under way.
3. **Unit volume and share of mind** **[M1999-054]**, **[M2000-030]**. Coca-Cola's test was "we want a lot more unit cases
   sold" **[M1999-054]**; Wendy's unit volume (traffic) has fallen in every year from 2023 to H1 2026 by its own wording,
   and U.S. systemwide sales fell from $12,553.8M (2024) to $11,897.5M (2025) and 7.7% further in H1 2026 at constant
   currency. Contrast the case the speakers excuse: "They’re selling more units than any year in history." **[M2000-013]**.
   Wendy's is not.
4. **The money test** **[M2011-015]**. The attacker needs no money of its own: McDonald's and Burger King already have it
   and are taking the traffic now (competitor row, 2025 and H1 2026). The test's own answer for a business that can be
   taken: "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. And: "one competitor is frequently
   enough to ruin a business" **[M2012-108]**; here there are two, gaining in the same months.
5. **Would the customer still choose it over the low bid?** **[M2017-009]**. Visits are being fought over across the
   category: McDonald's H1 2026 U.S. comparable sales were "primarily driven by positive check growth, including
   favorable product mix, partly offset by negative comparable guest counts" (MCD 10-Q), and Wendy's answer is price, in
   "everyday Biggie value offerings" (Exhibit 99.1, 2026-02-13) and the new CEO's "compelling value". The See's test, that "it wouldn’t be a question of people
   buying candy for the low bid" **[M2017-009]**, reads the other way for a burger chain: "People move around in the food
   business" **[M1997-001]**.
6. **The low-cost position.** Wendy's does not claim it and the filings show no cost advantage; its company-operated
   margin is above McDonald's U.S. (contrary item 7), but that is restaurant-level margin on 423 restaurants, not a
   system cost position, and franchisee costs are not disclosed.
7. **The brand in the customer's mind.** The brand is real and still draws about $2.0M a restaurant a year (U.S.
   systemwide AUV 2025); that is the strongest fact for the castle, and the reason this is not a judgment that the brand is
   worthless. It is a judgment on its direction.
8. **The franchisee, the second key variable** **[M1998-164]**, **[M1998-165]**. The speakers' goal for a franchisor is
   "you want the franchise operator to make money and you want him to create a capital asset that’s worth more than he’s
   put in it" **[M1998-165]**. The evidence on Wendy's franchisees runs against: 286 U.S. franchised closures in six
   months; the doubtful-accounts allowance up from $2.7M to $20.9M in two years and a further rise in the provision in
   Q2 2026 (release: lower net franchise fees "primarily due to an increase in the provision for doubtful accounts");
   the company spending its own money on franchisee builds (franchise development fund $41.2M in 2024, $38.4M in 2025);
   and the CEO's sentence that "franchisee economics are not meeting our expectations".
9. **Ask the competitors.** Not done by interview; the competitors' filings were read instead. Burger King reports U.S.
   comparable sales +8.5% in Q2 2026 (QSR 10-Q, BK segment; the cause was not read); McDonald's reports positive U.S.
   comparable sales in each of 2024, 2025 and H1 2026.
10. **Widening or narrowing?** **[L2005-010]**. Over 2011-2025 Wendy's compounded about 26 points less U.S. same-store
    growth than McDonald's; over 2017-2024 it ran ahead of Burger King (about +28% against +16%); in 2025 and H1 2026 it
    fell behind both by about 7 to 15 points a year. The 1995 letter's test for a bad year is whether "we at least maintained, and in some instances
    widened, our competitive superiority" **[L1995-022]**, in which case the year is "a cyclical problem, not a secular one"
    **[L1995-022]**. Wendy's did not maintain it: the rivals grew in the same economy. That is the newspaper row's case:
    the franchise "has lost still another notch" **[L1995-023]**.
11. **What could destroy, modify or reduce it** **[M2000-014]**. Named in the filings: closures that shrink the royalty
    and rent base (a quarter of revenue is royalty and a tenth is rent); franchisee defaults on leases the company has
    guaranteed ($99.5M of guarantees at 2026-06-28, 10-Q note) or sublets; a China franchise partner with a new right to
    terminate without liability before 2026-12-12 (10-Q, Item 2).

**Breakfast, digital and the marketing fund.** Breakfast launched across the U.S. on 2020-03-02 after earlier attempts
the 10-K describes as "accompanied by competitive pressures and responses from our competitors" (10-K FY2019,
`0000030697-20-000002`); the company spent $16.8M in 2019 preparing the system for the launch (10-K FY2019) and itself
funded $14.6M (2020) and $25.0M (2021) of incremental advertising for the daypart (10-K FY2021,
`0000030697-22-000003`, note to the results table). Digital rose to 23.7% of systemwide sales
in Q2 2026. Neither stopped the 2025-2026 fall in traffic. In Q2 2026 local advertising funds were "reallocated to U.S.
national advertising" (release, 2026-08-07): the marketing fund is being moved, not enlarged.

**What the rows say this evidence is.** The castle is not shown to be gone; it is shown to be giving ground to two named
competitors in the same months, with the business's own operator saying so. "once you start losing share, it’s hard to
get back" **[M2001-087]**; "If you really think a business is declining, most of the time you should avoid it."
**[M2012-062]**; and the moat that must be rebuilt by a turnaround plan is the one the 2007 letter discounts: "A moat that
must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**. The contrary evidence (Burger King's
recovery, the brand's unit volumes, international growth) shows a turnaround is possible; it does not show the castle
standing, and "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

**Why OUT and not TOO HARD.** The single fact that would show the castle filling in (the research-pass rule (a), applied
here at the first pass) is: U.S. same-restaurant sales negative while the two largest U.S. burger rivals' comparable
sales are positive over the same periods, with net U.S. closures. That fact is in the filings for 2025 and for H1 2026.
The future of the turnaround cannot be judged, and if that were the only question the box would be TOO HARD
**[M2000-019]**; but the question Q2 asks is whether the castle is standing, and the evidence answers it, so the framework's
routing sentence (Q2, "The routing with Q1": a castle being filled in on the evidence closes OUT) governs, and the row it
rests on gives the same answer for a castle that can be taken: "If the answer had been yes, we wouldn’t have done it."
**[M2011-015]**.

- **VERDICT: OUT** **[M2011-015]**, **[M2001-087]**, **[M2012-062]**, **[L1995-023]**, **[M2006-013]**. The run closes here.

## Q3 - HOW MUCH CAPITAL MUST GO IN. NOT REACHED.
## Q4 - DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. (The balance sheets were read in Step 0.)
## Q5 - WHO RUNS IT. NOT REACHED.
## Q6 - WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 - WHAT IS IT WORTH. NOT REACHED.
## Q8 - BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 - COULD IT RUIN US. NOT REACHED.
## Q10 - THE FAT PITCH. NOT REACHED.
## Q12 - PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## COMPUTATION - NOT A CLEARANCE
*Written at the owner's request (reporting, not a rule change) after Q2 closed the file OUT. Nothing below is a
clearance, an entry price or a reason to buy (operator rule 3); a price does not reopen a castle that is filling in
**[M2019-015]**, **[M2012-063]**.*

**(a) VALUE RANGE, by the framework's Q7 CONVENTION** (five-year average owner cash after every real cost, carried ten
years at the growth shown on the aggregate figure and never above it, then zero nominal growth, discounted at the
sovereign; the two ends are the no-growth case and the shown-growth case):
- Base: $181.9M (2021-2025 average, Step 0). Growth shown on the aggregate: $232.2M (2021) to $165.1M (2025), **-8.2% a
  year**. Rate 5.63%. Shares 190.67M.
- **No-growth end: $3,232M, $16.95 a share. Shown-growth end (ten years at -8.2%, then flat): $1,708M, $8.96 a share.**
  Range $8.96 to $16.95 against $6.10; top to bottom 1.9 to one.
- **Whole-cycle variant** (2021, the post-2020 rebound year, is abnormal): the 2022-2025 average, $169.4M, with the same
  growth: **$8.34 to $15.78**.
- **Two sensitivities the convention does not carry, shown because they cut against the range.** (i) Refinancing: the
  2021-1 notes ($412.0M at 2.370% and $617.3M at 2.775%, 10-Q Q2 2026 debt note) re-priced at the 5.422% coupon of the
  December 2025 issue would add about $28.9M of pre-tax interest, about $21.0M after tax at the 2025 rate (27.3%):
  base $160.9M, range **$7.92 to $14.99**. (ii) The run-rate: H1 2026 pre-tax income was 36.8% below H1 2025; if that
  holds, the next year's owner cash sits below every year of the window and below the bottom end's first years.

**(b) FAIR PRICE.** The price at or below which the central case returns about 10% a year, the floor CONVENTION
**[M2003-149]**, **[L2002-020]**. Central case: the year-by-year midpoint of the two ends' cash (falling from $181.9M
toward $129.7M in year ten, then flat). Tax treatment: owner cash is after the company's interest and taxes and before
the holder's own tax; the 10% is applied to it as the holder's return before personal tax (CONVENTION of this run: the
rows give "pre-tax" for Berkshire's whole-business purchases, and for a minority holder the corporate tax is already
paid inside the owner cash). **Fair price: $7.57** (whole-cycle variant $7.05; with the refinancing sensitivity $6.69).

**(c) CHEAP PRICE.** Rule (CONVENTION of this run): the price at which even the bottom end of the range, the shown
decline carried ten years, returns 10%; below it the arithmetic clears the floor on the worst case the five years show,
which is the nearest this run can write to "It should scream at you." without a pencil **[M2009-005]**. **Cheap price:
$5.60** (whole-cycle variant $5.21; with the refinancing sensitivity $4.95).

**Against the price.** $6.10 sits below the range ($8.96 to $16.95), below the fair price ($7.57) and above the cheap
price ($5.60). At $6.10 the arithmetic gives about 15.6% a year on the no-growth end, 12.6% on the central case and 9.0%
on the shown decline. This is the arithmetic of a declining business bought cheaply, the case the rows name and decline:
"the cigar butt approach, where you get one free puff" **[M2012-063]**. The sensitivities in (a) both lower every
figure; the run-rate one would put the bottom end's year-one cash above what the business is now earning.

**Other facts recorded for a later reader (not weighed; Q3 to Q9 NOT REACHED).**
- *Dividends and buybacks against owner cash, 2021-2025:* dividends $744.9M and buybacks $788.3M, together $1,533.2M,
  against owner cash of $909.7M (168%); the gap came from the 2022 debt raise and the cash it left (cash $746M to $301M).
  In H1 2025 the company bought 12.957M shares for $186.0M, about $14.35 a share (10-Q Q2 2026, equity note); none since.
  The $500M authorization runs to 2027-02-28 with $35.0M unused.
- *Debt:* Class A-2 securitized notes $2,774M outstanding at 2026-06-28 (seven series, coupons 2.370% to 5.422%,
  anticipated repayment dates 2028 to 2032: $429M in 2028, $900M in 2029), plus a $300M variable funding facility
  undrawn except $29.2M of letters of credit; finance leases $673M and operating leases $711M at FY2025. Missing an
  anticipated repayment date steps the interest up by at least 5.00% a year (8-K 2025-12-16). Rapid amortization events
  are tied to a "failure to maintain stated debt service coverage ratios" (10-K FY2025, debt note; the thresholds are in
  the indenture, not read). Cash interest paid $145.8M in 2025.
- *Trian:* Nelson Peltz and Peter May each beneficially 16.2% and 16.1% (overlapping, the same Trian shares), Trian
  entities directly 14,943,466 shares (7.9%) "held ... in comingled margin accounts with a prime broker" (proxy 2026,
  ownership note). Peltz resigned as chairman 2024-09-06 (13D/A No. 62); Matthew Peltz left the board 2025-07-08 and
  Bradley Peltz joined it (8-K 2025-07-08). Peltz family members and Bradley Peltz hold interests in Yellow Cab Holdings,
  a franchisee of 87 Wendy's restaurants that paid the company about $15.2M in 2025 (proxy, related-person transactions).
  The 2011 agreement lets the Trian group own up to 32.5% without Section 203 restrictions (proxy).
- *Stock pay and pay design:* stock-based compensation $14.6M in 2025 (down from $23.0M after the CEO's forfeitures);
  stockholders approved 21,000,000 more plan shares on 2026-05-20, about 11% of shares outstanding (8-K 2026-05-22).
  The 2025 annual bonus is 50% on adjusted EBITDA (proxy, CD&A). Stock pay is a real cost, "the most egregious
  example" of costs owners are told to ignore **[L2015-003]**; the EBITDA weighting would have been read at Q4 and Q6.

---
## THE BOX
**OUT at Q2** (the castle is shown on the filings to be giving ground: U.S. same-restaurant sales -5.6% in 2025 and -7.4%
in H1 2026 while Burger King U.S. was +1.6% and +7.2% and McDonald's U.S. +2.1% and +2.3%, with 315 restaurants closed in
H1 2026 and the CEO's statement that traffic, value and franchisee economics are short of expectations). Computation
only: range $8.96 to $16.95, fair $7.57, cheap $5.60, against $6.10.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (16:21 local, before the first EDGAR call). **Not** written question by
      question and **not** committed after each: the operator's instruction for this run forbids commits, and the
      questions were written in one pass after the reading. Declared.
- [x] Every v5 id resolves (Python check against `principle_ledger_v5.csv`, below); every filing fact has its accession;
      numbers are from filings or are this run's arithmetic on them, labelled.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and the computation is headed as such.
- [x] Owner cash after every real cost, never a net-income proxy; stock pay, the franchise development fund and
      finance-lease principal deducted; the sovereign from the Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found, both ways (nine items).
- [x] No point-in-time anchor in this run; the rule on later rows does not apply.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run on this file: result recorded at the end.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **OUT against TOO HARD at Q2 for a turnaround.** The routing sentence sends "a castle shown on the evidence to be
filling in" to OUT and "a castle whose future cannot be judged" to TOO HARD, but a business in an announced turnaround
is always both: the present evidence shows the castle filling in, and the outcome of the plan cannot be judged. The
framework does not say which reading governs when the two coincide. This run let the present evidence govern, using the
research pass's own single-fact rule (a) to state the fact, because the Q2 question is whether the castle is standing,
not whether it can be rebuilt; another analyst could reasonably have closed TOO HARD (NATURE) on **[M2000-019]**. The
verdicts differ in what follows (none either way, since a lower price reopens neither), so the practical cost is small,
but the box recorded differs. (2) **"COMPUTATION - NOT A CLEARANCE".** Operator rule 3 prescribes the heading with an em
dash; the operator's standing rule forbids em dashes. Written with a hyphen. (3) **The fair and cheap prices** are asked
for at the owner's request, and the framework has no rule for either when the file closed before Q7; both rules are this
run's CONVENTIONS and are stated where used. The Q7 convention's "growth shown" produced a negative growth rate here; the
convention says "never above it" but does not say whether a shown decline should be carried as a decline. It was carried
as shown, which makes the bottom end the declining case; a reader who caps decline at zero gets a single point, $16.95,
which the range rule cannot use. (4) **Franchisee economics** are the speakers' named key variable for a franchisor
(**[M1998-164]**), but the template's Q2 list does not ask for them; for an asset-light franchisor they were the most
important thing the filings did not disclose.

**Acceptance and id checks (run 2026-10-05):** `python tools/check_framework.py` **PASS** (test runs: phantom ids in 0
files; v5 scope 0 outside; pointers 0 missing). Python check (`_research 2026-10-05 WEN/idcheck.py`): 64 citations,
42 distinct v5 ids, all in `principle_ledger_v5.csv`; no E-ids; 33 quoted fragments standing beside an id, each found
verbatim in that id's row (fragments split at "..." checked part by part); every other quoted fragment in the file is a
filing's words or a search string, with no id beside it; no em dash in the file.
