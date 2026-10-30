# Company Run — Korea Electric Power Corporation (NYSE: KEP ADS; KRX KOSPI: 015760) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
25d3041f, before the first EDGAR request).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. The dispatching session
fills this line at the fold. **Filled at the fold (2026-10-23, after the run was committed): not held** (`PORTFOLIO.md` read for KEP only).

**Dispatched run.** Dispatched blind under `Screens/_daily/_dispatch_brief.md` as departed from in the brief itself (the
lines of evidence derived by the analyst from Items 4, 3.D and 5 of the 20-F, not supplied). Working folder
`Test Runs/_research 2026-10-23 KEP/` (notes, scripts, the computation output; raw filings under `cache/`, ignored by git).

**Contamination, declared.** (1) Before the first fetch I ran a directory listing of `Test Runs/` filtered for "KEP" or
"korea", to confirm the run file name was free. That is a listing of `Test Runs/` and the brief forbids it; it returned no
file name, so nothing about any earlier run of this name was seen, but the act is declared. (2) The session context showed
recent commit subjects about another company (IDA, a US utility, OUT at Q7) and memory-index lines about queue states and a
count of gate-clearers; none names this company and none is used. (3) The lock file `Screens/_daily/_overnight.lock` was
seen to exist (name only, not opened). Nothing else from a blind-listed file was seen.

**Lines of evidence, chosen from the 20-F and why** (this brief's one departure: the analyst derives them). From Item 4
(business): (i) the tariff mechanism, because the rate the Government approves is the price of everything KEPCO sells;
(ii) Government ownership and control, because the owner who sets the price also appoints the managers; (iii) the
competition and restructuring passages, because they say who could take share and what the Government may do to the
structure. From Item 3.D (risk factors): (iv) fuel costs not passed on, (v) policy measures easing the burden on consumers,
(vi) restructuring, (vii) the debt that must be refinanced and the debt ceiling set by statute, because these four are the
filer's own account of how owners lose money here. From Item 5 (review): (viii) the results by year and by segment over two
cycles, (ix) liquidity, capital requirements and the capital-expenditure budget, because they test (i) to (vii) against what
happened. The 6-Ks of 2026 test the same lines since the 20-F: the first-half results, the dividend, the board changes,
the KENTECH contribution, the UAE arbitration and the generation-merger clarification.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** KRX common **KRW 28,650** (close 2026-10-23); NYSE ADS **$10.72** (close 2026-10-22); **KRW 1,324.9 per USD**
  (2026-10-23). All three from the Yahoo chart feed through `tools/sources.py`: **aggregator, flagged** (operator rule 5,
  live quotes only). One ADS represents one-half of one common share, so the KRX close is **$10.81 per ADS** at that rate;
  the NYSE close a day earlier is consistent with it. Per-ADS figures below are the won figure halved and divided by 1,324.9.
- **Shares by class** from the latest filing's cover: **641,964,077 common** (20-F for FY2025, filed 2026-04-29, accession
  `0001193125-26-190113`; `python Screens/cover_shares.py KEP` returns the same count, "single class / undimensioned").
  Checked three ways: share capital KRW 3,209,820 million at par KRW 5,000 is 641,964,077 shares issued (consolidated
  statement of financial position, FY2025 20-F); no treasury shares found in the equity statement; the dividend 6-K of
  2026-02-26 (accession `0001193125-26-073345`) and the EGM 6-K of 2026-06-17 (accession `0001193125-26-273324`) both state
  641,964,077 outstanding voting shares. One class; no preferred.
- **Market cap:** KRW 18,392 billion = **$13,882M** at KRW 1,324.9.
- **Sovereign for the earnings currency (won):** **4.189%**, Korea Treasury Bond 30-year, **Bank of Korea** Economic
  Statistics System (ECOS), table 817Y002 (market interest rates, daily), item 010230000 (국고채 30년), dated 2026-10-23
  (4.239% on 2026-10-22). Issuing-authority side: the Bank of Korea is the State's central bank and publishes the
  Ministry of Economy and Finance's KTB market series; fetched through its public API (sample key), saved at
  `cache/ktb30.json`. `tools/sources.py` carries no won series, so this was fetched by hand.
- **Filings read** (operator rule 4), all from SEC EDGAR (CIK 0000887225, a 20-F filer under K-IFRS; no 10-K, 10-Q or proxy):
  - 20-F FY2025, filed 2026-04-29, `0001193125-26-190113`: Items 3.D, 4.A, 4.B (tariff, competition, restructuring,
    Government ownership), 5.A and 5.B, 8 (dividends), the consolidated statements and the segment, borrowings and
    capital-management notes.
  - 20-F FY2023, filed 2024-04-30, `0001193125-24-125063` (statements for 2021 to 2023, segments 2021 and 2022);
    20-F FY2021, filed 2022-04-29, `0001193125-22-132015` (2019 to 2021); 20-F FY2019, filed 2020-04-29,
    `0001193125-20-125462` (2017 to 2019); 20-F FY2017, filed 2018-04-30, `0001193125-18-141125` (2015 to 2017 and the
    end-2015 debt). The FY2016 20-F (`0001193125-17-145220`) did not download (EDGAR returned a placeholder page twice);
    its years are covered by the FY2017 filing.
  - 6-Ks of 2026: FY2025 results 2026-02-26 `0001193125-26-073342`; dividend 2026-02-26 `0001193125-26-073345`; AGM notice
    2026-03-10 `0001193125-26-099560`; AGM results 2026-03-25 `0001193125-26-123338`; KENTECH contribution 2026-03-30
    `0001193125-26-130298`; EGM results 2026-04-27 `0001193125-26-178954`, 2026-05-21 `0001193125-26-233301`, 2026-06-17
    `0001193125-26-273324`; non-standing directors appointed 2026-05-07 `0001193125-26-210657`; UAE arbitration 2026-05-22
    `0001193125-26-235407` and 2026-06-23 `0001193125-26-278519`; Q1 results 2026-05-13 `0001193125-26-220509`; first-half
    results 2026-08-12 `0001193125-26-345650`; generation-merger clarifications 2026-09-03 `0001193125-26-380884` and
    2026-10-02 `0001193125-26-411215`. The quarterly business reports of 2026-06-16 (`0001193125-26-271756`) and
    2026-09-15 (`0001193125-26-391239`) were downloaded and not read beyond their opening pages.
  - **One figure cross-checked against the filed statement:** 2024 net cash from operating activities, KRW 15,876,116
    million in the FY2025 20-F's filed cash-flow statement, against 15,876 billion in the SEC XBRL extract; and 2023 sales,
    87,476,410 million filed against 87,476 billion in XBRL. Both agree. XBRL was used only for 2016 to 2020 depreciation and
    the 2016 to 2020 dividends-paid line (transcription; flagged), every other figure from the filed statements.
- `python tools/run.py KEP` **failed**: "KEP: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (it reads US-GAAP
  tags; this filer tags IFRS). Every figure below was taken from the filed statements by the analyst
  (`_research 2026-10-23 KEP/owner_cash.py`, output in `owner_cash_output.txt`). No rule, id or verdict from the tool used.
- **Owner cash after every real cost, by year** (KRW billions; equity-only, i.e. after interest paid and income tax paid,
  because operating cash flow under K-IFRS here is stated after both; less spending on fixed assets and intangibles, plus
  fixed-asset disposals, less net purchases of associates and joint ventures, lease principal, dividends to minority
  holders and hybrid-bond dividends):

  | | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | sum |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Operating cash flow | 16,521 | 11,250 | 6,680 | 8,213 | 13,208 | 4,491 | -23,478 | 1,522 | 15,876 | 20,880 | 75,163 |
  | Fixed-asset + intangible spending | 12,153 | 12,680 | 12,378 | 14,229 | 13,401 | 12,800 | 12,428 | 13,983 | 14,308 | 15,937 | 134,297 |
  | Depreciation + amortization less right-of-use depreciation | 8,961 | 9,774 | 10,025 | 10,548 | 10,962 | 11,383 | 11,952 | 12,495 | 13,458 | 13,311 | 112,869 |
  | **Owner cash, all spending** | 4,394 | -1,746 | -6,021 | -6,286 | -906 | -9,316 | -36,199 | -13,272 | 1,006 | 2,697 | **-65,649** |
  | **Owner cash, maintenance only** (depreciation as the maintenance guess) | 7,652 | 1,356 | -3,351 | -2,497 | 1,870 | -7,230 | -35,418 | -11,292 | 2,071 | 7,405 | **-39,434** |
  | Profit to owners of the parent | 7,049 | 1,299 | -1,315 | -2,346 | 1,992 | -5,305 | -24,467 | -4,823 | 3,492 | 8,545 | -15,879 |

  Five-year (2021 to 2025) average owner cash, all spending: KRW -11,017 billion a year; maintenance only: -8,893 billion.
  Stock pay: none found (a state enterprise; no option or share plan in Item 6). Depreciation is the real cost of the plant
  **[L2015-004]**; capital spending ran above depreciation in every year. Dividends to minorities are derived as
  consolidated dividends paid less KEPCO's own (dividend per share times 641,964,077), and 2016 lease principal is taken as
  nil because no line was found in the FY2017 statement; both are small and said so.

### The balance sheets, ten years, before the income account **[M2025-032]**
*(Read here in Step 0 because the file closes before Q4. KRW billions, year ends, filed statements.)*

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Property, plant and equipment | 145,743 | 150,882 | 152,743 | 164,702 | 168,709 | 173,135 | 177,865 | 179,876 | 182,983 | 187,752 |
| Borrowings and debt securities | 53,639 | 54,747 | 61,035 | 67,877 | 69,725 | 80,530 | 120,605 | 133,632 | 132,533 | 129,769 |
| Cash and equivalents | 3,051 | 2,370 | 1,358 | 1,810 | 2,030 | 2,635 | 3,235 | 4,343 | 2,383 | 2,241 |
| Total equity | 73,051 | 72,965 | 71,093 | 68,890 | 70,668 | 65,327 | 42,000 | 37,265 | 41,363 | 49,323 |
| Equity of owners of the parent | 71,724 | 71,681 | 69,744 | 67,496 | 69,297 | 63,780 | 40,545 | 35,845 | 39,915 | 48,170 |

What moved and why. **Debt** rose from KRW 53.6 trillion to 129.8 trillion (2016 to 2025) and from 1.7 times parent equity to
2.7 times (the capital-management note gives 315% and 259% debt to total equity at 2024 and 2025). Most of the rise came in
2021 to 2023 (+63.9 trillion), when operating cash flow was 4.5, -23.5 and 1.5 trillion: the debt funded the selling of power
below cost, then the plant. **Equity** fell by a third, 71.7 trillion to 35.8 trillion (2016 to 2023), with no buyback and
no write-down of goodwill to explain it (goodwill is KRW 99 billion; intangibles about 1 trillion throughout): it is retained
losses. It recovered to 48.2 trillion by 2025 on two profitable years. **Cash** is thin against the debt (2.2 trillion
against 129.8 trillion) and the business does not hold a reserve; the contractual maturity table puts KRW 49.3 trillion of
borrowings and debt securities, interest included, inside one year (FY2025 20-F, Item 5.B). **Receivables** were 13.0% of
sales in 2016 (7.79 trillion on 59.8 trillion) and 13.1% in 2025 (12.62 trillion on 96.6 trillion); **inventories** 9.2% and
10.5% (5.48 and 10.15 trillion): nothing building out of line with sales **[M2025-032]**. **Deferred tax assets** went from
1.9 trillion (2021) to 10.9 trillion (2022) and 13.0 trillion (2025): the losses of 2021 to 2023 are carried as future tax
relief, which is real only if profits return. **Non-current provisions** are 28.9 trillion at 2025 (nuclear decommissioning
and spent fuel among them, FY2025 statement of financial position), a long-dated claim ahead of the owners. What the figures
cannot say: whether the tariff will ever return what was lost. No regulatory asset is booked for the unrecovered fuel cost;
the filer says it "may accumulate such portions and reflect them in" the Total Comprehensive Cost, subject to Government
approval (FY2025 20-F, Item 4.B, Electricity Rates).

## THE FOUNDATIONS (not a gate)
Two foundations bear hardest. **A share is a business:** the test is whether one would be content to own it "if the market
closed for five years" **[M1997-109]**; here the cash the business yields to its owners in those years is decided each year
by a Ministry weighing "consumer welfare" and "the effect of electricity tariff on inflation in Korea" (Item 4.B), so the
owner is buying a claim whose size another party sets. **No macro forecast enters**: no view on fuel prices, the won or
rates is used below; "macro conclusions are — just never enter into the discussion" **[M2000-094]**. The nearest row to this case is the currency row, "Any currency-related investment is a bet
on how government now, and in the future, will behave" **[M2011-025]**; the analogy to a state-priced utility is mine, not
the speaker's. **Who is paid to tell you:** nothing below rests on broker or rating-agency opinion. **The analyst's habits:**
"What do I not know that I need to know?" **[M1999-129]**; look for "what’s wrong in things" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) at KRW 28,650 the shares sell at 2.15 times FY2025 profit
to owners (KRW 8,545 billion) and 0.38 times parent equity; (2) the Government held the fuel-cost unit price at +5 won per
kWh from 2023Q4 to 2026Q2 although the formula gave -1.8 to -13.3 won, "taking into consideration our financial conditions"
(Item 4.B), which is the regulator acting for the owners; (3) operating profit was KRW 14.0 trillion in 2025 and the
FY2025 dividend was KRW 1,540 a share, the first material dividend since FY2020; (4) the transmission and distribution
monopoly is statutory and no rival can build a second grid. Each is weighed where it bears (Q2).

## THE STANDING RULE
Owning this does not put the buyer at risk of ruin if it is bought with the buyer's own money and sized so that a large fall
is borne: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "We are never going to risk what we have
and need for what we don’t have and don’t need" **[M2012-081]**. The target's own debt is the target's question (Q9), not the
buyer's ruin. No leverage or margin is contemplated. The rule is not engaged.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; the product may be plain while the economics are not
  **[M2011-014]**. The economics here are plain and the filer names them: "demand for electricity; electricity rates we
  charge to our customers; fuel costs; and the exchange rates of Won against other foreign currencies" (Item 5.A).
- **The key variables and whether they are foreseeable**, "trying to identify the key variables in that particular business,
  and evaluating how predictable they were" **[M1998-044]**. (a) *Competitive position:* foreseeable. KEPCO
  carries "substantially all" transmission and distribution in Korea by statute and holds 53.4% of generation capacity
  through six wholly-owned subsidiaries (Item 4.B); the Government must own at least 51% (KEPCO Act); independent producers
  hold 46.6% of capacity and generated 36.3% of power in 2025 (Item 4.B, Competition). Ten years out it is still the grid.
  (b) *Demand:* flat and foreseeable, -0.4%, +0.7% and -0.1% in 2023 to 2025 (Item 5.A). (c) *Capital need:* foreseeable and
  rising; the Government's Basic Plan sets the build, and the capital-expenditure budget is KRW 23.1, 27.4 and 27.6 trillion
  for 2026 to 2028 against 18.7 trillion in 2025 (Item 3.D). (d) *The tariff:* set by the Ministry of Climate, Energy and
  Environment with the Ministry of Finance and Economy, after review by the Korea Electricity Commission, at a "Total
  Comprehensive Cost" meant to recover fair costs plus a "fair investment return" on the rate base (2024 fair rate of
  return 3.18%; equity component 6.847% by a capital asset pricing model), with "a variety of other factors" weighed,
  including "consumer welfare" and inflation (Item 4.B). This is the variable that decides the owner's result, and it is a
  decision of the Government, not a market.
- **Do the past statements tell me the future ones?** **[M2008-033]** They tell me how the compact has behaved over two
  cycles, which is what Q2 must judge: the filer itself records actual returns below the fair return in 2006 to 2013 and
  losses in 2021 to 2023 (Items 4.B and 5.A). They do not tell me next year's tariff, and the file does not need it.
- **Abroad** **[M2000-141]**: the governance is laid out in the filing (the Act on the Management of Public Institutions;
  the President appoints the chief executive; the Ministry of Finance and Economy appoints the non-standing directors, a
  majority of the board; Item 4.A and the 6-K of 2026-05-07). Tax: the filer states its applicable rate (26.92% for 2025).
  An understood business abroad asks a lower price, not a pass **[M2006-021]**.
- **Routing.** The industry does not change fast; the transmission business has no technology race that puts its ten-year
  economics out of sight **[M1998-008]**. What is uncertain is the regulator's conduct, and the framework puts a regulated
  return and a regulated moat that broke at Q2 and Q3 (Q2, What it rules OUT, the regulator exception; Q2's mistakes,
  **[L2023-011]**), not at Q1. The doubt test **[M2002-092]** is applied to the business, whose economics I can state in a
  paragraph from the filing; the doubt about the regulator is carried to Q2, where the record answers it.
- **VERDICT: IN.** A statutory grid monopoly with government-owned generation, read from its own filings **[M2008-069]**,
  **[M2005-015]**; its competitive position in ten years is foreseeable **[M2012-065]**, and the deciding variable, the
  tariff compact, is judged at Q2 on the record of two cycles.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**; a moat is what "protects
excellent returns on invested capital" **[L2007-004]**. Here the walls stand; the question is what they protect, and for whom.

- **The attacker with money** **[M2011-015]**. No one can build a second national grid, and the law reserves transmission and
  distribution to KEPCO ("we have had a substantial monopoly over electricity transmission and distribution in Korea", Item
  4.B). In generation the castle is open: independent producers hold 46.6% of capacity and generated 36.3% of power in 2025;
  44 of them plus 7,355 renewable producers; private coal plants allowed since 2013 (Item 4.B, Competition). The share of
  KEPCO's purchases supplied by its own generators fell from 68.3% (2023) to 65.9% (2025) (Item 5.A). The walls stand where
  the law builds them and nowhere else.
- **Pricing power and the agony before a rise** **[M2005-020]**: "you can almost measure the strength of a business over time
  by the agony they go through in determining whether a price increase can be sustained." KEPCO cannot raise a price at all.
  It submits proposals; the Ministry decides after consultation and review, weighing "consumer welfare", "our projected
  capital requirements, the effect of electricity tariff on inflation in Korea and the effect of tariff on demand" (Item
  4.B). The fuel-cost charge of 2021 is capped at ±5 won per kWh and the Government may withhold it: it held the charge at
  -3.0 won in 2021Q2 and Q3 although the formula gave -0.2 and +1.7, and at 0.0 in 2022Q1 and Q2 although it should have been
  +3.0; in 2023Q3 the formula gave +10.2 and the cap allowed 5.0 (Item 4.B). The filer: "there typically is a significant
  time lag for the tariff increases as such increases requires a series of deliberation processes and administrative
  procedures and the Government also has to consider other policy considerations" (Item 4.B). Munger's rider, "If you name
  some business that has incredible pricing power, you’re talking about a business that’s a monopoly or a near monopoly"
  **[M2010-092]**, fails here in the instructive way: a monopoly whose price belongs to someone else.
- **Whose price.** The rows' case is a competitor who "determined our profit, because we looked at his price every day. And
  if we cut the price he’d match it, and we couldn’t raise the price" **[M2023-079]**; "You don’t like to be in a business like
  that" **[M2012-109]**. The rows speak of a rival; the analogy to a Government that sets the price is mine. The filer states
  the conflict itself: the Government "may from time to time pursue policy initiatives that could directly or indirectly
  impact our business and operations, and such initiatives may vary from the interest and objectives of our other
  shareholders" (Item 3.D), and calls itself "an entity formed to serve public policy goals of the Government" (Item 4.B).
- **Unit volume**: demand is flat, electricity consumption -0.4%, +0.7%, -0.1% in 2023 to
  2025, industrial demand -2.1% in 2025 (Item 5.A). Volume neither builds nor erodes the castle.
- **The low-cost position and the low bid.** Not the test for a monopoly grid: the customer has no other wire. In generation the
  cost-based pool sets what KEPCO pays its own and independent generators (Item 4.B, Purchase of Electricity); KEPCO is the
  buyer, not a price-setter.
- **Ask the competitors.** No rival company is named in the 20-F (Item 4.B names only "independent power producers"; none of
  them files with the SEC so far as the filing shows). Not done.
- **Widening or narrowing**, "whether it’s likely to widen further or shrink on you" **[M1999-108]**. Narrowing at the edges: generation share eroding to independents; the 2016
  proposal to liberalise retail sale stands without a roadmap; the Government announced on 2026-09-03 a plan that "includes a
  proposal to merge five power generation subsidiaries [...] into a single entity", details not yet determined (6-Ks
  `0001193125-26-380884`, `0001193125-26-411215`). The grid monopoly itself is not narrowing.
- **What could destroy, modify or reduce it** **[M2000-014]**: the tariff decision, which is the Government's, and the
  structure, which is the Government's. Neither is a competitor.

**The competitor row** *(CONVENTION of this run: the filing names no rival company, so the comparison is chosen by the
analyst. Rationale: the test is whether a state-influenced, tariff-regulated integrated utility can earn an owner's return
through the same 2017 to 2024 fuel cycle; two such issuers that file 20-Fs with the SEC were chosen. Figures are the
issuers' own reported profit to owners and parent equity as tagged in their 20-F XBRL facts, transcription, flagged; the
filed documents were not opened.)* Return on average parent equity, %:

| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | average |
|---|---|---|---|---|---|---|---|---|---|
| **KEPCO** (KRW; 20-Fs above) | 1.8 | -1.9 | -3.4 | 2.9 | -8.0 | -46.9 | -12.6 | 9.2 | **-7.4** |
| CEMIG, Companhia Energética de Minas Gerais (BRL; CIK 1157557; 20-F XBRL, latest accessions `0001292814-20-002008` to `0001554855-25-000408`) | 7.3 | 11.8 | 20.9 | 17.2 | 20.3 | 19.8 | 24.8 | 27.4 | **18.7** |
| Enel Chile S.A. (CLP; CIK 1659939; 20-F XBRL, `0001558370-20-004669` to `0001558370-25-005756`) | 12.2 | 11.3 | 8.6 | -1.5 | 2.6 | 34.8 | 14.8 | 3.1 | **10.7** |

CEMIG's 2019 profit to owners is tagged -3,194 million in its 2022 filing and +3,127 million in its 2020 filing, while its
profit for the year is +3,194 million in every filing; the sign is a tagging error and +3,194 is used. KEPCO's 2025 return
is 19.4% (KRW 8,545 billion on average parent equity of 44,042 billion); the comparison issuers' 2025 figures were not yet
in their facts. Both comparison utilities are state-influenced (CEMIG is controlled by the State of Minas Gerais) and both
went through the same fuel and rate cycle; both kept a positive average. KEPCO's result is not the industry's; it is the
compact's.

**The parts table** (section B), operating profit by segment, KRW billions, filed segment notes (FY2023 and FY2025 20-Fs):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | castle |
|---|---|---|---|---|---|---|---|
| Transmission and distribution (the parent) | -7,244 | -33,624 | -6,154 | 3,543 | 9,004 | -34,475 | statutory monopoly; price set by the Government |
| Nuclear generation (KHNP) | 762 | 761 | 820 | 1,442 | 2,371 | 6,156 | sells to the pool; paid by the parent |
| Non-nuclear generation (five companies) | 370 | 289 | 929 | 2,663 | 2,194 | 6,445 | sells to the pool; paid by the parent |
| Plant maintenance and engineering | 245 | 240 | 355 | 418 | 366 | 1,624 | service to the group |
| Others | 208 | 334 | 89 | 97 | 152 | 880 | mainly overseas |
| Consolidated operating profit | -5,723 | -32,241 | -4,245 | 8,461 | 14,011 | -19,737 | |

**Which part decides.** The five-year total is negative, so "more than half of five-year operating profit" has no meaning; "the
largest part" decides. By revenue (KRW 92.4 trillion of 96.6 trillion external revenue in 2025) and by the size of its result
in either direction, transmission and distribution is the largest part. The generation parts sell over 90% of what they
produce to it (intersegment revenue 14,981 of 15,347 billion at nuclear, 26,183 of 28,711 billion at non-nuclear, 2025), at
prices set inside the cost-based pool; the filer says "the results of operations for our business segments substantially
mirror our consolidated results of operations" (Item 5.A). The split is one regulated chain priced by transfer, and the parent
decides. *(How "largest" is measured when the total is negative is not stated by the convention; see What in
the framework was wrong or unclear.)*

**The field's returns over the last full cycle** (section C). The cycle is the fuel cycle the filer describes: cheap fuel and
high profit in 2015 and 2016, the spike of 2021 and 2022, the recovery of 2024 and 2025; peak to peak 2016 to 2025. Over
those ten years: operating profit summed to KRW -0.4 trillion; profit to owners of the parent to -15.9 trillion; owner cash
after all spending to -65.6 trillion; parent equity fell from 71.7 trillion to 48.2 trillion while debt rose from 53.6
trillion to 129.8 trillion; return on average parent equity averaged -4.4% a year over 2017 to 2025. The filer's longer
record runs the same way: "For the period between 2006 and 2013, our actual rates of return were lower than the fair rate of
return largely due to a general increase in fuel costs and additional facility investment costs incurred, the effects of
which were not offset by timely increases in our tariff rates"; the 2014 to 2016 excess "has been used to fund capital
expenditure and repair and maintenance, and make investments in renewable energy and other environmental programs" (Item
4.B). So in the good years the surplus was spent on policy and plant, and in the bad years the owners bore the loss. The
rows' verdict on that kind of return held long: "if you have a business that’s earning 5 or 6 percent on equity and you hold
it for a long time, you are not going to do well in investing. Even if you buy it cheap to start with." **[M1998-006]**;
this one earned less.

**The regulator exception, and why it does not apply.** A return set by a regulator is carried to Q3 as a second best
instead of closing OUT (Q2, What it rules OUT). The rows behind that exception rest on the allowed return being earned:
"when you get an allowed return in the electric utility you’re almost certain of earning it, I mean, if you behave
yourself" **[M2010-037]**; "there’s no way we get rich on our utility investments. But there’s no way we get poor, either"
**[M2009-104]**; capital-heavy businesses are taken on "reasonable expectations of earning decent returns on the incremental
sums they invest" **[L2009-012]**. The record here is the case the exception does not cover: the owners got poor over a
full cycle, the allowed return was not earned in 2006 to 2013 or 2017 to 2023, and the allowed equity return itself
(6.847% for 2024) is a ceiling the compact offers, not a floor it guarantees. The speakers name this exact failure among
their own mistakes: "the regulatory climate in a few states has raised the specter of zero profitability or even
bankruptcy [...]. In such jurisdictions, it is difficult to project both earnings and asset values in what was once regarded as
among the most stable industries in America. [...] I did not anticipate or even consider the adverse developments in
regulatory returns" **[L2023-011]**.

**A change for the better?** The contrary evidence written at the foundations: 2024 and 2025 were profitable, and the
Government held the fuel charge above the formula for eleven quarters to rebuild KEPCO's finances. Under section C a change
for the better is credited only on a full cycle in which the price behaviour held **[M2005-020]**, **[L1995-022]**. This is
not a new compact: the tariff system is the one in force since 2021, the discretion that withheld the charge in 2021 and
2022 is the same discretion that holds it now, and the filer itself says the hold reflects "the fact that a substantial
amount of the Fuel Cost Adjusted Charge that should have been reflected in previous years has not previously been
reflected" (Item 4.B). It is the recovery leg of the cycle just counted, and the cycle with it included is negative. There
is also no claim to the rest: no regulatory asset is booked for the unrecovered cost, and recovery through the Total
Comprehensive Cost "needs to be approved by the Government" (Item 4.B). The first half of 2026 already shows operating
profit down to KRW 4,913 billion from 5,889 billion, second quarter 1,129 billion from 2,136 billion (6-K
`0001193125-26-345650`). No change is credited.

**Price.** At 2.15 times last year's profit the price is the strongest argument against this verdict, and the rows answer
it: "You can turn any investment into a bad deal by paying too much. What you can’t do is turn any investment into a good
deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** The castle stands, but what it protects is the Government's policy, not the owners' return. A moat is
  what "protects excellent returns on invested capital" **[L2007-004]**; on the filer's own filings the returns this one
  protected over the last full cycle were negative in aggregate, while the two comparison utilities kept positive averages
  through the same cycle. The case is the framework's standing castle that protects only ordinary returns (Q2, What it
  rules OUT, section C), which closes OUT and not TOO HARD because the returns are known; the moat "is judged, not measured"
  in the framework's words, and the rows' own measure is "whether it’s likely to widen further or shrink on you"
  **[M1999-108]**, which over two cycles has been shrink. The regulator exception does not reach it, because its premise,
  that "when you get an allowed return in the electric utility you’re almost certain of earning it" **[M2010-037]** and
  "there’s no way we get poor, either" **[M2009-104]**, fails on the record, which is the mistake the speakers name: "I did
  not anticipate or even consider the adverse developments in regulatory returns" **[L2023-011]**. And the price is set by
  another party with other aims than the owners', the business in which someone else "determined our profit"
  **[M2023-079]**. Q3 to Q12 are NOT REACHED; what was found for them is under AFTER THE STOP, and the value range is shown
  there as COMPUTATION, NOT A CLEARANCE.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The ten years of balance sheets were read in Step 0 and the owner cash recast there; facts for Q4
are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (No buyback exists to test against the bottom of the Q7 range.)

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The range and the fair price are computed under AFTER THE STOP, headed COMPUTATION, NOT A
CLEARANCE (operator rule 3).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT, at Q2.** The castle stands but protects the Government's policy, not the owners' return: over the full cycle 2016 to
2025 the filer's profit to owners summed to KRW -15.9 trillion and owner cash after all spending to -65.6 trillion, while
two state-influenced comparison utilities kept positive returns through the same cycle; the regulator exception does not
reach it because the allowed return was not earned. Q7 was not reached; computed beneath the stop, the range is the
no-growth case alone, **KRW 38,171 a share ($14.41 per ADS) against KRW 28,650 ($10.81)**, and its central case earns about
5.6% at the price, below the floor of about ten percent. No integrity tell was found in what was read; Q5 was not reached.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box unchanged, operator rule 2.)*

**Bearing on Q3 (capital).** Capital spending on fixed assets and intangibles exceeded the depreciation-and-amortization
charge in every year 2016 to 2025 (KRW 134.3 trillion against 112.9 trillion, right-of-use depreciation excluded). The
filer's own capital-expenditure figures are KRW 15,518, 16,720 and 18,701 billion for 2023 to 2025 and the budget is 23,099,
27,391 and 27,625 billion for 2026 to 2028 (Item 3.D). The build is set by the Government's Basic Plan (the Eleventh, February
2025, amended March 2025: two new large nuclear units and a small modular reactor by 2038, coal capacity 39.2 to 22.2 GW, LNG
43.2 to 69.2 GW, renewables 30.0 to 121.9 GW, and the grid to carry them; Item 3.D). The 2024 fair rate of return on the rate
base was 3.18% (debt 2.790%, equity 6.847%); the 2025 rate was not yet determined at filing (Item 4.B). Volume was flat over
the same years (Item 5.A).

**Bearing on Q4 (the accounts).** The statements are K-IFRS, audited by KPMG Samjong; no EBITDA figure was seen featured in
what was read (the results 6-Ks show sales, operating income, profit before tax and net income only). Deferred tax assets of
KRW 13.0 trillion at 2025 stand on the losses of 2021 to 2023; their expiry schedule was not read. No regulatory asset is
carried for the fuel cost not passed through. 2015 operating profit as filed (KRW 20.3 trillion) includes the gain on the
sale of the Samseong-dong headquarters land (PPE disposals KRW 9.84 trillion that year), which is why 2016, not 2015, opens
the cycle used below. Small figure differences found: FY2025 dividend per share KRW 1,540 in the dividend 6-K
(`0001193125-26-073345`) and KRW 1,542 in the 20-F, Item 5.B; the 2021 operating cash flow 4,473 billion in the FY2021 20-F
and 4,491 billion as restated in the FY2023 20-F (the later figure used).

**Bearing on Q5 (who runs it).** The President of Korea appoints the president and chief executive and the standing director
on the audit committee, on the motion of the Ministers, after the Committee for Management of Public Institutions (Item 4.A).
The chief executive at the 2026 AGM notice was Kim Dong-Cheol (6-K `0001193125-26-099560`). Six non-standing directors were
replaced by appointment of the Minister of Finance and Economy on 2026-05-07 (6-K `0001193125-26-210657`); standing members
or directors were elected at EGMs on 2026-04-27, 2026-05-21 and 2026-06-17 (6-Ks `0001193125-26-178954`,
`0001193125-26-233301`, `0001193125-26-273324`). The six generation subsidiaries' presidents are appointed by the President of
Korea and contract with the Ministry, not with KEPCO (Item 4.A). Item 6 (pay and board) was not read. No integrity tell was
found in what was read; the reading was not a Q5 reading.

**Bearing on Q6 (the money and the owners).** Dividends per share by fiscal year: 3,100 (2015), 1,980 (2016), 790 (2017), none
(2018, 2019), 1,216 (2020), none (2021 to 2023), 213 (2024), 1,540 (2025), against profit to owners shown in Step 0; no buyback
in the ten years; no share issuance; the Government must hold at least 51% and the filer says it may not be able to raise
share capital without the Government's participation (Item 3.D). On 2026-03-27 the board resolved a KRW 48.8 billion
contribution to the Korea Institute of Energy Technology (KENTECH), "an initial contribution through the year of 2026" for
its facilities and operations (6-K `0001193125-26-130298`). Retained earnings over 2016 to 2025 did not become value per
share: parent equity per share fell from KRW 111,726 to 75,035.

**Bearing on Q9 (debt and exposures).** Borrowings and debt securities KRW 129.8 trillion and cash 2.2 trillion at 2025-12-31;
debt to total equity 259% (capital-management note). Contractual cash flows of borrowings and debt securities due within one
year: KRW 49,273 billion, interest included (Item 5.B). The statutory ceiling on KEPCO's separate debt securities was raised
on 2022-12-28 from two to five times share capital and reserves (six with the Minister's approval), effective to 2027-12-31;
the ceiling shrinks if losses shrink reserves (Item 3.D). 16.9% of long-term debt is in foreign currencies, mainly dollars
(Item 3.D). Operating profit covered interest expense 3.2 times in 2025 (14,011 against 4,340 billion) and not at all in
2021, 2022 and 2023 (operating losses). Non-current provisions KRW 28.9 trillion. Through KHNP, 26 nuclear units, four of
them shut down at filing; neither KEPCO nor its non-nuclear generation subsidiaries carries insurance against terrorist attacks (Item 3.D). 20.1% of bituminous coal in 2025
was of Russian origin, plus uranium services and LNG, about $1.1 billion in all (Item 3.D). KHNP, a subsidiary, claims about
KRW 1,661 billion in arbitration over the UAE nuclear operating-support contract, which KEPCO disputes (6-Ks
`0001193125-26-235407`, `0001193125-26-278519`); both parties are consolidated. One country, one grid, one price-setter.

**Bearing on Q12.** The group runs coal-fired plants (coal capacity to fall under the Basic Plan); none of the businesses
the rows name is involved.

### COMPUTATION, NOT A CLEARANCE: Q7's range and the fair price (reporting figures, at the operator's request)
*(Not a verdict and not entry language. Built by Q7's range convention in full, with the regulated-utility paragraph.
Arithmetic in `_research 2026-10-23 KEP/owner_cash.py`; output saved beside it in `owner_cash_output.txt`.)*

- **Basis.** The deciding part earns a return a regulator sets, so the central figure is equity-only, the rows' own exception
  being debt "dedicated [...] to the fixed-asset commitments at our regulated utilities" **[L2017-012]**: owner cash after
  interest and after the company's own tax (both are paid inside operating cash flow), against the market value of the
  shares, KRW 18,392 billion. The all-equity figure is shown beside.
- **The base, specific (a).** The literal window 2021 to 2025 opens on three years the filer ties to the fuel spike ("our net losses
  in 2023 were largely due to sustained rise in fuel costs", Item 5.A) and closes near the cycle's top; "If either
  year was aberrational, any calculation of growth will be distorted" **[L2005-003]**. The base is the last full cycle, peak
  to peak, 2016 to 2025 (2015 left out because its profit includes the land sale); the literal window is shown beside.
- **Growth, specific (b).** Owner cash changes sign within the cycle; between the halves, maintenance-only owner cash averaged
  KRW 1,006 billion a year (2016 to 2020) and -8,893 billion (2021 to 2025), so the rate between them is meaningless too, and
  the range is **the no-growth case alone**, said so. The cap (f) does not bite. After year ten, no growth; zero nominal.
- **Acquisitions (c) and working capital (d).** Net purchases of associates and joint ventures (KRW 4,787 billion over the
  cycle, 2,082 billion in 2025) are deducted in the all-spending case and left out of the no-growth maintenance case, which
  credits no growth. Working capital is counted (inside operating cash flow).
- **Maintenance, specific (e).** The filing does not split capital spending into maintenance and growth; the maintenance
  guess is the depreciation charge on owned assets plus amortization, the rows' proxy: "the depreciation charge is not
  inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**. Central case:
  maintenance only.
- **The debt credit (the regulated-utility paragraph).** The regulator divides the rate base "in proportion to our total
  equity and our total debt" (Item 4.B) and states no other share, so the allowed debt share is the business's own at
  2025-12-31: 72.46%. Over the cycle debt rose KRW 71,015 billion; fixed-asset spending was 134,297 billion; operating cash
  75,163 billion; spending not met from operating cash 59,134 billion; the debt-share cap 97,311 billion. *CONVENTION of this
  run:* the credit is the least of the debt raised, the cap, and the spending not met from operating cash (59,134 billion),
  because the paragraph credits debt raised to fund the fixed assets and the borrowing beyond that funded the operating
  losses of 2021 to 2023. *CONVENTION of this run:* in the maintenance-only case the credit is taken pro rata to the spending
  that case charges (112,869 of 134,297 billion, 0.840), because the debt funded all the spending and the case charges only
  part of it. The return on the added capital is "measured by the operating earnings after depreciation" **[M2014-086]**.
- **Owner cash a year on the cycle base (KRW billions), and value at no growth discounted at the KTB 30-year 4.189%:**

  | case | owner cash a year | value a share | per ADS | expected return at KRW 28,650 |
  |---|---|---|---|---|
  | **Central: maintenance only, equity-only, debt credited pro rata** | **1,026** | **KRW 38,171** | **$14.41** | **5.58%** |
  | All spending, equity-only, debt credited | -652 | negative | negative | -3.54% |
  | Maintenance only, equity-only, no credit | -3,943 | negative | negative | -21.44% |
  | All spending, equity-only, no credit | -6,565 | negative | negative | -35.69% |
  | All-equity, maintenance only (interest added back after the 26.92% rate; less net debt KRW 127,528 billion) | -1,918 | negative | negative | -1.31% on enterprise value |
  | Literal window 2021 to 2025, central construction (beside) | 150 | KRW 5,567 | $2.10 | 0.81% |

- **The floor, tested first.** The minimum is about ten percent at the price, after the company's own tax: "we don’t want
  to buy equities where our real expectancy is below 10 percent" **[M2003-149]**. No case earns it: the best, the central
  case, earns 5.58% at KRW 28,650, and every other case is negative. Under Q7 the file would close **OUT** on the floor
  whatever the width. The width test does not arise: the range is a single case.
- **VALUE RANGE (reporting figure):** the no-growth case alone, **KRW 38,171 a share, $14.41 per ADS**, equity-only with the
  debt credit (central); the all-equity range is negative. Price KRW 28,650 ($10.81 per ADS at the KRX close; $10.72 NYSE
  close 2026-10-22).
- **FAIR PRICE (reporting figure, Part VII):** the single end case valued at ten percent: KRW 1,026 billion / 0.10 = 10,267
  billion = **KRW 15,990 a share, $6.03 per ADS**, equity-only with the debt credit, the central figure for a regulated
  utility. Beside it, the all-equity fair price is **negative** (KRW -228,530 a share on the maintenance case: net debt
  exceeds the value of the cash before interest). On the literal window the central fair price would be KRW 2,332 ($0.88).
  Tax treatment: the company's own tax, no conversion; the deferred tax assets were not priced separately (their expiry was
  not read). Exchange rate KRW 1,324.9 per USD (2026-10-23, aggregator).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 25d3041f precedes the first EDGAR request); written question by
      question; committed after Step 0 to Q1 (1f0c3880), after Q2 (930a668d), and after the closing sections.
- [x] Dispatched run: the brief allowed the per-question pathspec commits; the lock `Screens/_daily/_overnight.lock` was
      present, held by the dispatching session (not opened). The fold is the dispatcher's; a run not in the register binds
      nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Not clean:** one filtered listing
      of `Test Runs/` for "KEP|korea" was run before the first fetch (no match returned); declared under contamination. No
      run file, review or blind-listed file was opened.
- [x] Every v5 id resolves (`check_cites.py`: every M/L/R id found in `principle_ledger_v5.csv`, no E-ids, every quoted
      fragment beside an id found in its row); every filing fact carries its accession; numbers come from filings or rows.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the Bank of Korea, dated; the price and exchange rate from an aggregator, flagged. Two approximations
      confessed in Step 0 (minority dividends derived; 2016 lease principal taken as nil).
- [x] Contrary evidence written down as found (the foundations) and weighed at Q2; facts for later questions under AFTER THE
      STOP; no integrity facts to flag.
- [x] No point-in-time anchor; rows of any date may be cited.
- [x] `tools/run.py` failed on this IFRS filer and printed nothing used; `Screens/cover_shares.py` gave the share count only.
- [x] `python tools/check_framework.py` PASS before each commit.
- Weak points, said plainly: the comparison issuers' figures are XBRL facts, not read in their filed documents; the 2016
  to 2020 depreciation and dividends-paid lines are XBRL; Item 6 (pay, board) and the two 2026 quarterly business reports
  were not read; the FY2016 20-F did not download.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The regulator exception at Q2 has no rule for a regulator whose set return is not earned.** "A return set by a
regulator is the exception, carried to Q3 as a second best" reads, on its face, as covering KEPCO, whose tariff is set on a
stated fair rate of return. I read the exception through its rows, which assume the allowed return is earned, and found
that premise failing on two cycles of the filer's record, so the castle closed OUT under section C. A second analyst could
carry it to Q3 and reach Q7; the computation shows Q7 would then close OUT on the floor, so the box is OUT either way, at a
different question. The text should say which. (2) **Q1 or Q2 for a regulator's conduct.** Q1's test 5 (would the insiders
write it down) could send a business whose deciding variable is a Government's tariff decision to TOO HARD (NATURE) at Q1;
the routing paragraph sends only fast-changing industries there, and the regulated-moat mistake row sits under Q2, so I
passed Q1 and decided at Q2. Unstated. (3) **The parts convention with a negative total.** "More than half of five-year
operating profit" means nothing when the total is negative, and "the largest part" is not said to be measured by revenue,
assets or the absolute result; by five-year operating profit the largest positive part is a generator that sells over 90%
of its output to the parent at pool prices. I took the parent by revenue and said why. (4) **The regulated-utility debt
credit** does not say how to separate debt that funded operating losses from debt that funded plant, nor how the credit
meets specific (e)'s maintenance-only case; two CONVENTIONS of this run fill the gaps, and the central value moves from
negative to KRW 38,171 a share on the second of them, so the method decides the figure. (5) **Section C's re-look
condition** ("the first fiscal year in which the business's volume or its field's volume falls") does not fit a regulated
business, whose test is a cost spike under a fixed tariff, not a fall in volume. (6) **The competitor row for a statutory
monopoly** names no rival; the comparison chosen is a run CONVENTION. (7) **Tooling:** `tools/run.py` reads US-GAAP tags
only and failed on an IFRS filer; the protocol's sovereign table has no won series, so the Bank of Korea's ECOS series was
used by hand.
