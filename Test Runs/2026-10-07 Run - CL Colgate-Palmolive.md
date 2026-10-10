# Company Run — Colgate-Palmolive Company (NYSE: CL) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`, as amended through 2026-10-07). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

Dispatched run under the canonical brief `Screens/_daily/_dispatch_brief.md` (operator rule 10); the dispatching session holds
the lock in `Screens/_daily/` (seen at 09:26, "interactive v5 re-runs batch 3"). Working folder `Test Runs/_research 2026-10-07 CL/`;
raw filings and XBRL dumps sit in its `cache/` subfolder, which `.gitignore` covers, and are not committed.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared as found (not used):** (1) the session's opening git status and recent-commit list showed the subject
of commit de1279db, which names a v5 re-run box for CHD (a competitor named in this brief), and listed research-folder file names for
AYI, BDC, CHD and ARCB runs of 2026-09-26 and 2026-09-27; (2) the project memory index loaded with the session states queue counts and
"57 gate-clearers, nothing buyable", with no ticker; (3) `.gitignore` comments name other runs (DELL, SNPS, MGM, AGCO, ATR) by ticker,
seen while checking that `cache/` is ignored; (4) the brief itself says earlier Colgate run files exist. No other run file, holding
review, `PORTFOLIO.md` or queue file was opened, listed or searched. Nothing from (1) to (4) is used below.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $87.25 (close 2026-10-06; printed by `tools/run.py` from its quote source; **aggregator, flagged**, live quote only per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common, **797,172,829** as of June 30, 2026 (10-Q for the quarter ended
  2026-06-30, filed 2026-07-31, accession `0000021665-26-000042`; `python Screens/cover_shares.py CL`). Checked: the 10-K's note 8
  gives issued 1,465,706,360 less treasury 664,466,836 = 801,239,524 at 2025-12-31 (10-K accession `0000021665-26-000006`), and the
  10-Q shows 3,223,398 shares bought in Q2 2026 alone at an average $87.40; the cover count is consistent. No 8-K after the 10-Q
  reports an issue of shares (8-K read: 2026-07-31 earnings, `0000021665-26-000041`). Preference stock authorized, none issued.
- **Market cap:** 797.173M x $87.25 = **$69,553M**.
- **Net debt at the latest filed balance sheet** (2026-06-30, 10-Q `0000021665-26-000042`): debt payable within one year $34M plus
  long-term debt $7,823M = $7,857M (finance leases inside it; operating lease liabilities, $566M at 2025-12-31, left out as Q7's
  convention says); less cash $1,370M and marketable securities $83M = **$6,404M**. The 10-Q states no subsequent event that changes it.
- **Sovereign for the earnings currency:** USD 30-year par yield **5.64%**, US Treasury daily par yield curve, 2026-10-06
  (`python tools/sources.py`, the issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-23, `0000021665-26-000006`): Items 1, 1A in part, 5, 7, the
  statements and notes 3, 4, 5, 6, 8, 13, 14, 15, 16, 17, 18; 10-Q Q2 2026 (`0000021665-26-000042`): balance sheet, cash flow,
  segments, repurchases; proxy DEF 14A filed 2026-03-25 (`0001308179-26-000136`); 8-Ks of 2026-07-31 (`0000021665-26-000041`),
  2026-04-30 Item 2.05 (`0000021665-26-000022`), 2026-03-17 segment recast (`0000021665-26-000010`), 2025-11-10 euro notes
  (`0001104659-25-109135`); for the cycle, the segment notes and MD&A of the 10-Ks for FY2022 (`0000021665-23-000007`), FY2019
  (`0000021665-20-000004`), FY2016 (`0000021665-17-000002`) and FY2014 (`0001628280-15-000846`).
  **One figure cross-checked against the filed statement:** net cash provided by operations FY2025 $4,198M, as printed on the
  10-K's cash-flow statement, equals the XBRL figure `tools/run.py` printed (4,198).
- `python tools/run.py CL`, arithmetic lines only (its rule text, ids and floor are not used, Part VII): OCF 3,745 / 4,107 / 4,198
  (2023 to 2025), SBC 122 / 135 / 155, capex 705 / 561 / 564, D&A 567 / 605 / 630; OCF less SBC less capex 2,918 / 3,411 / 3,479.
  It found no securities inside operating cash, no other stock-pay line, no intangible or software spending beside capex, and printed
  no line for dividends to minority partners, which the filing does carry (statement of changes in equity: $170M, $168M, $157M in
  2023 to 2025; $166M and $135M in 2021 and 2022 from the FY2022 10-K); the run deducts them at Q4. Its debt table adds
  "ShortTermBankLoansAndNotesPayable" and "LongTermDebtCurrent", which in 2024 and 2025 are the same dollars (the filed line "Debt
  payable within one year" $1,117M contains the current portion $1,115M), so its "sum" double counts; the filed total debt is $7,988M
  at 2025-12-31 (note 6).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether the analyst would be content to own Colgate "if the market closed for five years"
**[M1997-109]**, which turns the run toward what the business will do and away from when the quote moves **[M1994-038]**,
**[M1998-099]**. The market serves and does not instruct: a price is read only against where "the facts and reasoning lead you"
**[M2006-077]**. No macro enters: two thirds of sales are outside the United States and about 45% in emerging markets (10-K FY2025,
Item 7), so currency and inflation will tempt a forecast; the rows put them in only as properties of the business and its "average
profitability" over time **[M2015-016]**, and treat any currency bet as a bet on governments **[M2011-025]**. Who is paid to tell
you: the filer features organic growth and non-GAAP earnings (Item 7, "Non-GAAP Financial Measures") and says it uses them "as a
factor in determining compensation" (same); carried to Q4 and Q5. Margin of safety: if the purchase needs pencil and paper it is "too
close to think about" **[M1996-084]**. The analyst's habits: the run looks for "what's wrong in things" **[M2025-013]** and asks "What
do I not know that I need to know?" **[M1999-129]**. **Contrary evidence, written down as found** **[M1997-127]**: (a) global
toothpaste share 41.3% in 2025, down 0.4 points, with shares down in North America, Latin America and Africa/Eurasia (10-K FY2025,
Item 7); (b) North America organic sales fell 1.6% in 2025 on volume declines (same); (c) three impairments of the 2018 and 2019
skin-health purchases, $571M in 2021, $721M in 2022 and $919M in 2025, against about $2.4 billion paid (FY2019, FY2022 and FY2025
10-Ks); (d) a restructuring programme charged in every year from 2012 to 2026 except 2020 and 2021 ($1,854M for 2012 to 2019,
$228M for 2022 to 2024, a programme raised to $350M to $550M on 2026-04-30, $300M of it charged in H1 2026); (e) shareholders'
equity of $54M at 2025-12-31, after $28.5 billion of treasury stock at cost; (f) Hill's volumes fell 0.6% in 2025 and lower
private-label sales cut its organic growth by 320 bps.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase made with the buyer's own money, unlevered and sized so that a fall of half "or
more" can be borne **[M2020-022]**, puts nothing the buyer has and needs at risk **[M2012-081]**; borrowed money "has no place in the
investor's tool kit" **[L2014-005]**. Nothing in the target changes that. No ruin risk from the buyer's side on those terms.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five
  or 10 years" **[M2012-065]**; the first question is "can I understand it?" **[M1995-051]**. Colgate sells toothpaste, manual
  toothbrushes, mouthwash, bar and liquid soap, shower gel, deodorant, hand-dish liquid, surface cleaners, fabric softener and, through
  Hill's, therapeutic and wellness pet food; oral care was 44% of 2025 net sales, personal care 17%, home care 16%, pet nutrition 23%
  (10-K FY2025, Item 1, `0000021665-26-000006`). Each is a repeat purchase of a cheap, slowly changing product.
- **The key variables and how predictable they are** **[M1998-044]**. For oral care they are the variables named for Coca-Cola,
  units sold and shares outstanding **[M1998-040]**, with price net of materials beside them. The filer reports all of them: global
  toothpaste share by year (44.4% in 2014, 41.1% in 2019, 39.4% in 2021, 41.4% in 2024, 41.3% in 2025; the 10-Ks of those years),
  volume and price separately each year, and diluted shares (960M in 2012, 811M in 2025, XBRL). The forecast these call for is
  about "consumer behavior and threats to a business" **[M2023-030]**, not about technology; no part of the business lives on
  continued invention. For Hill's the variables are the same in kind: veterinary recommendation of prescription diets, price, and
  volume through pet-specialty and online retailers.
- **Do the past statements tell me the future ones** **[M2008-033]**? For the operating businesses, yes: segment margins in
  Latin America ran 26.7% to 31.9% from 2014 to 2025 through the Brazilian, Argentine and Mexican currency falls (segment notes,
  FY2014, FY2016, FY2019, FY2022, FY2025 10-Ks), and the gross margin went 59.6% (2021), 57.0% (2022), 58.2% (2023), 60.5%
  (2024), 60.1% (2025) through the last inflation (XBRL). What the statements do not foretell is the acquisition record (the
  skin-health write-downs), which is a Q6 question about the people, not a Q1 question about the economics.
- **Abroad** **[M2000-141]**. Two thirds of sales are outside the United States, about 45% in emerging markets; hyperinflation in
  Argentina, Nigeria and Türkiye is named (10-K FY2025, Item 7); Venezuela was deconsolidated in 2015 with a $1,084M charge (FY2016
  10-K); a Brazilian tax dispute from the 1995 Kolynos purchase has run since 2001 (note 13). The rows do not send an understood
  business in a less familiar country to a pass; they ask to be "paid more" for it **[M2006-021]**. Carried to Q7 as a reason the
  margin must be wider.
- **Doubt** **[M2002-092]**: none that the ten-year economics of toothpaste, soap and prescription pet food can be pictured; the
  insiders would write the forecast down **[M2000-105]**. Routing: no fast-changing technology; not a bank; the parts (two product
  segments, oral-personal-home care and pet nutrition) are each understood, so no part keeps the whole outside.
- **VERDICT: IN.** The economics can be pictured ten years out from the filer's own reported variables **[M2012-065]**,
  **[M1998-044]**, **[M2023-030]**; the foreign exposure is a price question carried to Q7 **[M2006-021]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what's going to keep it standing or cause it not to be standing five, 10, 20
years from now" **[M1995-038]**; a moat is what "protects excellent returns on invested capital" and a "powerful world-wide brand"
is one of the two named forms **[L2007-004]**.

- **The parts table** (section B; segment operating profit as each year's 10-K reports it, 2021 to 2025, $M: FY2022 10-K for 2021 and
  2022, FY2025 10-K for 2023 to 2025; Corporate, which carries restructuring, impairments and stock pay, is not a part):

  | part | 5-yr segment operating profit | share | castle | decides |
  |---|---|---|---|---|
  | Oral, Personal and Home Care (product segment) | 18,771 | 80.4% | standing (below) | **yes, more than half** |
  | Hill's Pet Nutrition (product segment) | 4,586 | 19.6% | standing, returns lower since 2022 (below) | no |
  | *geographic reading:* Latin America 6,474 (27.7%), North America 4,009 (17.2%), Asia Pacific 3,920 (16.8%), Europe 3,175 (13.6%), Africa/Eurasia 1,193 (5.1%) | | | | Latin America, as largest |

  The filer names two product segments and manages the first through five geographic reportable segments (note 14). The parts with
  "vastly different" economics **[L2008-005]** are the two product segments, so the oral-personal-home care segment decides at 80%. If
  the convention is read on reportable segments instead, no part reaches half and Latin America, the largest, decides; its castle is
  the same oral-care franchise (toothpaste and manual toothbrush lead its organic growth, MD&A 2025), so both readings close on the
  same castle. Recorded under WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR. **[M2023-031]** stays open against the convention, as
  the framework says.

- **Test 1, what keeps it standing, and how permanent** **[M1995-038]**. The reason the customer comes is a brand in the mouth of
  most of the world: global toothpaste share 44.4% (2014), 44.0% (2016), 41.8% (2018, from the FY2019 10-K's "down 0.7 share points"), 41.1% (2019), 39.8% (2020), 39.4% (2021),
  39.8% (2022), 41.1% (2023), 41.4% (2024), 41.3% (2025), 41.3% year to date 2026 (the 10-Ks of each year; 10-Q Q2 2026); manual
  toothbrush 33.4% (2014) to 32.4% (2025). P&G, the next rival, states "a nearly 30% global market share" in oral care with Crest and
  Oral-B, power brushes included (P&G 10-K FY2026, `0000080424-26-000103`). A product used twice a day, bought for a few dollars,
  where the reason for choosing one brand changes slowly, as See's customers' did **[L1996-028]**.
- **Test 3, the money test** **[M2012-106]**, **[M2002-051]**. P&G, with sales of $87 billion and the money to try, holds the second
  place and reported oral-care unit volume down in Greater China and North America "due to competitive activity" in FY2026 (P&G
  10-K). Haleon, demerged from GSK on 18 July 2022 (20-F filer, IFRS, £; flagged), has grown oral health organically 10.6%, 9.6% and 7.9% in
  2023 to 2025 and says it "continued to outperform the category with market share gains" (Haleon 20-F FY2025,
  `0001104659-26-027443`). So money does attack, in the premium and therapeutic end, and has taken share there; it has not displaced
  the leader, whose share in 2025 was where it stood in 2019.
- **Test 4, pricing power through the last inflation** **[M2005-020]**, **[M2005-017]**, **[M2000-031]**. Net selling price +3.5%
  (2021), **+9.5%** (2022), **+10.0%** (2023), +4.4% (2024), +2.1% (2025); volume +1.0%, -2.0%, -0.5%, +3.1%, -0.4% (10-K MD&A
  of each year). Gross margin 59.6%, 57.0%, 58.2%, 60.5%, 60.1% (XBRL). Toothpaste share rose from 39.4% to 41.4% across the
  same years. Prices up about a fifth in two years, volume nearly held, margin restored by the third year and share gained against
  entrenched rivals: what the row calls "something very special in people's minds" **[M2000-031]**. The costs came through faster
  than prices for one year (2022), the "temporary situations" of **[M2005-017]**.
- **Test 5, share of mind** **[M1997-099]**; **test 7, the brand against the retailer** **[M2015-038]**, **[M2001-090]**,
  **[M2019-041]**. Walmart and affiliates take about 11% of net sales; the filer says it is "increasingly dependent on certain key
  retailers, some of which exercise greater bargaining strength than we do" and that private label competes in some products (10-K
  Item 1). Private label is the Kraft Heinz lesson **[M2019-041]**; in toothpaste the filer's share data show no erosion to it
  over 2021 to 2025, but the data exclude eCommerce and some discounters (MD&A, "Market Share Information"), so the retailer's own
  channels are partly unmeasured. Weighed against, not decisive.
- **Test 7, does it travel** **[M1997-068]**: sold in over 200 countries; Latin America segment margin 26.7% to 31.9% in every
  year from 2014 to 2025 despite foreign exchange cutting reported sales by 11% in 2015 and 13.7% in Latin America in 2024 (segment
  notes; MD&A 2025 reconciliation). The brand travels and keeps its margin in local currency.
- **Test 10, widening or narrowing** **[M1999-108]**, **[L2005-010]**; the notch **[L1995-023]**. Against: (i) toothpaste share fell
  five points from 2014 to 2021 before regaining two; (ii) North America's margin fell from 33.5% (2017) to 19.4% (2025), and on
  the 2026 recast without skin health it was 22.8%, 23.0%, 21.5% in 2023 to 2025 (8-K 2026-03-17, Exhibit 99,
  `0000021665-26-000010`); (iii) total segment margin was 29.4% in 2016 and 24.6% in 2025; (iv) advertising rose from $1,428M
  (9.4% of sales) in 2016 to $2,703M (13.3%) in 2025 (XBRL; note 17), so part of the restored gross margin is spent again to hold
  the place. For: Latin America, Europe and Asia Pacific margins in 2025 were at or near their 2016 to 2019 range; global share is
  back above 41%. Munger's remark that the packaged-goods houses are "all weaker than they used to be at their peak" **[M2016-080]**
  is a row about named companies at a date and is weighed, not applied as a verdict on the industry or on Colgate (Q2, A row about
  one company, convention of 2026-10-07). Reading: a castle that has lost a notch in its home market and is holding elsewhere.
- **Test 11, what could destroy or reduce it** **[M2000-014]**: retailer power and private label, unmeasured eCommerce and social
  commerce channels where the filer says new direct-to-consumer entrants appear (10-K Item 1); premium therapeutic toothpaste
  (Haleon); Greater China, where organic sales fell in 2025 on toothpaste (MD&A, Asia Pacific) and where the skin-health
  write-down says performance was weaker "particularly" (note 5). None is a
  technology that removes the need for the product.
- **Hill's, the part that does not decide.** Prescription and wellness diets sold through veterinarians, pet-specialty stores and
  online. Segment margin 27.3% (2012), 28.8% (2016), 27.8% (2019), 27.2% (2021), then 22.9% (2022), 18.8% (2023), 21.5% (2024),
  23.1% (2025), after buying three dry-food plants from Red Collar for $719M in 2022 and carrying their private-label sales, which
  cut 2025 organic growth by 320 bps (FY2022 and FY2025 10-Ks). Rivals: General Mills' North America Pet (Blue Buffalo) earned
  18.0%, 20.5%, 20.3%, 19.1% on sales in fiscal 2023 to 2026, had organic sales down 3% in fiscal 2026 and wrote down $1,750M of its
  goodwill and brands (GIS 10-K FY2026, `0001628280-26-046466`; FY2024, `0001193125-24-168943`); Freshpet, the fresh-food entrant,
  grew sales from $87M (2014) to $1,102M (2025) at operating margins of -9% to +7% (FRPT XBRL, 10-K `0001611647-26-000006`); Mars
  (Royal Canin) and Nestle Purina are **not SEC filers, flagged**, and could not be read. Hill's castle stands on the veterinary
  recommendation; its returns are lower than before 2022 and still at or above the one filing rival's.
- **The competitor row** (same metrics, each from its own filings; operating margin = operating income / revenue; cash margin =
  (operating cash less capital spending less stock pay) / revenue; whole span shown in the research file `peers.py` output):

  | company | span | operating margin | cash margin | note |
  |---|---|---|---|---|
  | Colgate (CL) | 2014-2025 | 16.1% to 26.0%, GAAP | 9.7% to 19.4% | segment margin 24.6% to 29.4% |
  | Procter & Gamble (PG) | FY2016-FY2026 | 20.0% to 24.3% (8.1% FY2019, Gillette write-down) | 13.9% to 19.8% | Health Care segment pretax 24.9% to 26.2%, FY2024 to FY2026 |
  | Church & Dwight (CHD) | 2014-2025 | 11.1% to 21.0% | 12.5% to 17.8% | |
  | Kenvue (KVUE) | 2021-2025 | 11.9% to 19.4% | -0.7% to 16.3% | separated from J&J (10-K FY2025, `0001944048-26-000030`) |
  | Haleon (HLN, 20-F, IFRS, £, flagged) | 2020-2025 | 16.2% to 21.9% | 11.8% to 20.2% | oral health organic +7.9% to +10.6% |
  | General Mills (GIS) North America Pet | FY2023-FY2026 | segment 18.0% to 20.5% | n/a | whole company 4.8% to 18.3% |
  | Freshpet (FRPT) | 2014-2025 | -8.7% to 6.9% | -81% to -0.1% | |

- **The field's returns over the cycle** (section C): the branded household and oral-care field earns operating margins near a fifth of
  sales on small tangible capital, at every filer above, across 2014 to 2026; not "ordinary" returns. Colgate's own pre-tax segment
  profit of $5,023M in 2025 sat on net tangible operating capital of $4,336M (Q3). The OUT clause for a
  castle that protects only ordinary returns does not apply. No change for the better is being credited.
- **VERDICT: IN.** The deciding part's castle is a world-wide brand with about two fifths of global toothpaste, which raised prices
  about a fifth through the last inflation while holding volume and gaining share **[M2000-031]**, **[M2005-020]**, **[L2007-004]**;
  it is attacked by funded rivals and has not fallen **[M1995-038]**. It has lost a notch in North America and spends more to hold
  its place **[L1995-023]**, **[L2005-010]**; those are carried to Q7 as limits on the growth credited, not as an open castle.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, measured on tangible assets **[M2011-060]**, **[M2014-007]**. Net
  tangible operating capital (total assets less cash, marketable securities, goodwill, intangibles and deferred tax assets, less
  current liabilities other than debt; XBRL, checked by hand for 2025 against the filed balance sheet: 16,330 - 1,288 - 107 - 3,122 -
  1,536 - 205 - (6,853 - 1,117) = 4,336) and segment operating profit before Corporate (`capital.py` in the research folder):

  | year | tangible operating capital $M | segment operating profit $M | pre-tax return |
  |---|---|---|---|
  | 2016 | 3,795 | 4,467 | 118% |
  | 2019 | 4,021 | 4,208 | 105% |
  | 2021 | 4,257 | 4,396 | 103% |
  | 2022 | 5,556 | 4,198 | 76% |
  | 2023 | 5,326 | 4,688 | 88% |
  | 2024 | 4,468 | 5,053 | 113% |
  | 2025 | 4,336 | 5,023 | 116% |

  Charged with Corporate (overhead, R&D, stock pay, restructuring) but not the 2025 write-down, 2025 operating profit is $4,225M
  (3,306 + 919): 97% on tangible capital. Working capital is negative, -7.0% of sales in 2025 (MD&A, Liquidity): customers and
  suppliers finance the inventory. The high return is not a cyclical peak or leverage **[L1994-009]**: it holds in every year back to
  2016 and is measured before debt. Return on equity is meaningless here, equity being $54M after buybacks **[M1998-017]**.
- **Reinvestment to stand still and to grow** **[L2000-035]**, **[M2000-144]**. Capital spending 2021 to 2025: 567, 696, 705, 561,
  564 (average 619); depreciation and amortization 556, 545, 567, 605, 630 (average 581), of which amortization of intangibles
  about 75 a year (note 17). The 2022 and 2023 peaks were Hill's capacity (segment capex 297 and 301 against 56 in 2020, note 14);
  the filer guides 2026 capital spending to about 3.0% of sales (MD&A). Maintenance guess, stated as a guess **[M2000-144]**: about
  the depreciation charge, $500M to $550M a year; the filing does not split maintenance from growth.
- **The growth arithmetic** **[M1994-081]**, **[M2003-120]**, **[M2023-081]**. From 2016 to 2025 segment operating profit rose $556M
  (4,467 to 5,023). Tangible capital rose $541M over the same years, and $3,894M was paid for businesses (2018 PCA Skin and EltaMD
  $728M; 2019 Filorga $1,711M; 2020 hello $353M; 2022 Red Collar plants and other $809M; 2025 Prime100 $293M; XBRL and notes).
  Measured on everything put in, the increment earned about 12.5% pre-tax (556 / 4,435), against 100%+ on the base business. The
  base is the great business of the first grade **[M1998-081]**; the dollars added since 2016 earned a second-grade return, mostly
  because the skin-health purchases failed (Q6) and because currency cut the dollar value of foreign profits.
- **WEIGHS FOR.** The business itself needs little capital and earns very high pre-tax returns on what it uses **[M1998-081]**,
  **[M2011-060]**; the weak increment is a capital-allocation fact, weighed at Q6 **[M2023-081]**. (The "little or no debt"
  criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends (2016 to 2025) read, seven shown, before the income account** **[M2025-032]**
  (`tools/run.py` table, first-filed XBRL;
  2025 checked line by line against the filed balance sheet in the FY2025 10-K: assets 16,330, cash 1,288, receivables 1,675,
  inventories 2,032, goodwill 3,122, intangibles 1,536, long-term debt 6,871, retained earnings 26,595, equity 54; all agree):

  | year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | LT debt | retained |
  |---|---|---|---|---|---|---|---|---|---|
  | 2016 | 12,123 | -243 | 1,315 | 1,411 | 1,171 | 2,107 | 1,313 | 6,520 | 19,922 |
  | 2018 | 12,161 | -102 | 726 | 1,400 | 1,250 | 2,530 | 1,637 | 6,354 | 21,615 |
  | 2019 | 15,034 | 117 | 883 | 1,440 | 1,400 | 3,508 | 2,667 | 7,333 | 22,501 |
  | 2020 | 15,920 | 743 | 888 | 1,264 | 1,673 | 3,824 | 2,894 | 7,334 | 23,699 |
  | 2022 | 15,731 | 401 | 775 | 1,504 | 2,074 | 3,352 | 1,920 | 8,741 | 24,573 |
  | 2024 | 16,046 | 212 | 1,096 | 1,521 | 1,987 | 3,272 | 1,756 | 7,289 | 26,145 |
  | 2025 | 16,330 | 54 | 1,288 | 1,675 | 2,032 | 3,122 | 1,536 | 6,871 | 26,595 |

  What the figures say: (1) equity has sat near zero for ten years while retained earnings rose $6.7 billion, because treasury stock
  at cost reached $28.5 billion and currency losses in other comprehensive income reached $3.9 billion; the business is run on
  almost no book equity, and return on equity says nothing **[M1998-017]**. (2) Goodwill and intangibles rose from $3,420M (2016) to $4,167M
  (2018, PCA Skin and EltaMD) and $6,718M (2020, Filorga and hello), and $2,211M of impairments followed (2021, 2022, 2025); the
  balance sheet shows the skin-health purchases arriving and leaving. (3) Receivables moved from 9.3% of sales (2016) to 8.2% (2025): no
  stretching of terms. (4) Inventory moved from 7.7% of sales to 11.5% (2022) and back to 10.0% (2025), with the Hill's plants and
  the inflation; inventory under LIFO is about a quarter, with a $129M LIFO reserve (note 18); not out of line with the trend of
  sales **[M1995-064]**. (5) Long-term debt rose from $6.5 billion to $8.7 billion (2022) and stood at $7.8 billion in June 2026;
  total debt $7,988M at 2025-12-31. (6) Cash is small and offshore: $1,234M of $1,288M held by foreign subsidiaries (MD&A), "not
  worth as much as cash held at home" **[L2016-009]**. What they cannot say: the worth of the brands, which the balance sheet does
  not carry except for those bought.
- **The real costs** **[L2021-003]**. Depreciation runs at about capital spending (Q3). Stock pay, $155M in 2025, is expensed and is
  subtracted from owner cash **[L2015-003]**. Restructuring is not one-time here: the Global Growth and Efficiency Program charged
  $1,854M from 2012 to 2019, the 2022 Global Productivity Initiative $228M, and the Strategic Growth and Productivity Program, begun
  July 2025 at $200M to $300M, was raised on 2026-04-30 to $350M to $550M, $300M of it charged in H1 2026 (notes 4; 8-K Item 2.05;
  10-Q note 11). The non-GAAP figures exclude these every year; telling owners year after year "Don't count this" for necessary
  business adjustments "is misleading" **[L2016-007]**. Owner cash below is built from operating cash, which already bears the cash
  part of every programme, so nothing is added back. Pension: the U.S. plan assumes 6.5% on assets against realized 5% over 10 and 25
  years (MD&A, critical estimates); a one-point change moves net income about $12M, so the optimism is visible but small
  **[L2002-039]**. ERISA: $267M (2023) and $65M (2025) charges for a 2005 annuity amendment, settled for $332M, $99M of it fees paid
  by the company (note 13). Minority partners: $157M to $170M a year paid to noncontrolling holders (statement of equity); a real
  outflow from the owner's cash, deducted below. No EBITDA in the filer's mouth in the 10-K or the July 2026 release.
- **The figures featured.** The July 2026 release leads with "Base Business EPS" up 8% beside GAAP EPS down 5%, and gives full-year
  guidance for sales, organic growth, gross margin and both GAAP and Base Business EPS growth (8-K 2026-07-31, Exhibit 99,
  `0000021665-26-000041`); the 10-K says the non-GAAP measures are used "as a factor in determining compensation" and states the aim
  of "consistent, compounded earnings per share growth" (Item 7). The adjusted figure featured **[L2016-006]** and earnings guidance
  **[L2019-006]** weigh against here and are carried to Q5 (section A). The same release puts the GAAP figure in its first lines and
  reconciles every adjustment (Table 8), which is the clear explanation **[M1994-018]** credits.
- **Owner cash after every real cost** (operating cash less stock pay, less all capital spending, less dividends to minority holders;
  never net income; `value.py` in the research folder):

  | year | operating cash | stock pay | capital spending | minority dividends | owner cash, after interest | after-tax net interest added back (23%) | owner cash, before interest | acquisitions |
  |---|---|---|---|---|---|---|---|---|
  | 2021 | 3,325 | 135 | 567 | 166 | 2,457 | 79 | 2,536 | 0 |
  | 2022 | 2,556 | 125 | 696 | 135 | 1,600 | 118 | 1,718 | 809 |
  | 2023 | 3,745 | 122 | 705 | 170 | 2,748 | 179 | 2,927 | 0 |
  | 2024 | 4,107 | 135 | 561 | 168 | 3,243 | 173 | 3,416 | 0 |
  | 2025 | 4,198 | 155 | 564 | 157 | 3,322 | 148 | 3,470 | 293 |
  | average | | | | | 2,674 | | 2,813 | 220 |

  The tax rate on interest is the company's own non-GAAP effective rate, 22.7% and 23.1% in 2024 and 2025 (MD&A). 2022 is low
  because "changes in working capital and lower net income" cut operating cash (FY2022 10-K, MD&A); it is a middle year of the
  window, not an end year, so specific (a) does not move the base. GAAP net income for comparison only: 2,166 / 1,785 / 2,300 /
  2,889 / 2,132.
- **VERDICT on the accounts: no confusion and no suspicion; WEIGHS AGAINST** on the recurring restructuring presented as
  non-recurring **[L2016-007]** and the adjusted figure featured with guidance **[L2016-006]**, **[L2019-006]**, both carried to Q5;
  the statements themselves are clear and reconciled **[M1994-018]**, and none of the account tells of **[M1995-064]** is present.
  The recast cash feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet **[M2007-081]**: the proxy, the reports and the record, judged by the two
yardsticks, how well they run the business against "the hand they were dealt" and "how well that they treat their owners"
**[M1994-008]**; read the proxy "see how they treat themselves versus how they treat the shareholders" **[M1994-009]**.

- **The people.** Noel Wallace, 61, with Colgate since 1987; President of Colgate North America 2010 to 2013, Latin America 2013 to
  2016, COO for Hill's and innovation 2016 to 2018, CEO since 2019, Chairman since 2020; a director of American Express since July
  2025 (proxy, DEF 14A `0001308179-26-000136`). Stanley Sutula, CFO since 2020. A career insider, not a hired star.
- **The proxy: how they treat themselves.** CEO total pay $17.1M (2023), $18.2M (2024), $16.5M (2025): salary $1.5M, stock awards
  $8.0M, options $3.6M, cash bonus $2.5M (2025); 276 times the median employee (Summary Compensation Table; pay-ratio note). The
  cash bonus fell from $4.6M to $2.5M as organic growth slowed; the proxy says so in plain words: "our organic sales growth slowed
  considerably and our Base Business Earnings Per Share also grew at a slower rate" and "our annual incentive payments also declined
  in 2025". Wallace owns 362,719 shares directly (about $31.6M at $87.25), plus 1,613,677 exercisable options; officers must hold two
  to eight times salary; no hedging or pledging; two clawback policies; no related-person transactions reported. One discretionary
  move upward: the committee raised 2025 Base Business EPS "by $0.06 to $3.75" for tariffs "not known at the time the original
  target was set", having reserved the right in March 2025; it also cut its free-cash-flow productivity measure from 133.6% to
  115.7% to strip out the write-downs, a move against the officers' interest. Read against "I hate, with a passion, rewarding anything
  that can be easily faked" **[M1996-089]**: the tariff lift is disclosed and small; it weighs against, it is not a lie.
- **The habits carried from Q4** (section A): the adjusted figure featured **[L2016-006]**, earnings guidance **[L2019-006]**, and
  the filer's stated aim of consistent, compounded growth in earnings per share (10-K Item 7). Read with the record: the GAAP figure is in the first lines of
  the release and every adjustment is reconciled; three write-downs of the skin-health purchases were taken in three different years
  rather than avoided; in 2025 the bonus paid 93.6% of opportunity because Base Business EPS and organic growth fell short of target,
  and the July 2026 release revises its guidance line by line, raising some lines and holding others, so the record read is not one of always
  reaching declared targets **[L2002-041]** (a stockholder proposal in the same proxy says guidance was cut in January 2025; that is
  the proponent's statement and is not used); the reports tell an owner what he would want to know, segment by segment, with share data and
  price-volume splits each year **[M1998-036]**. The restructuring excluded every year is the weakest point, "Don't count this" told
  year after year **[L2016-007]**, but every charge is named, sized and reconciled. Tells of dishonesty sought and not found: no
  stock price posted as a goal **[M2004-067]**, no report that dances around the key figure **[M2007-082]**, no serial share
  issuance (diluted shares fell from 960M in 2012 to 811M in 2025).
- **How they talk about mistakes** **[L2024-003]**: the skin-health write-downs are explained by "lower than expected category growth
  rates and weaker than expected performance, particularly in China", followed by "continues to believe in the growth prospects of the
  business" (10-K FY2025, note 5). That names the outcome and not the error of paying $1.7 billion for Filorga; it weighs against
  ability and candour, not as a sign of dishonesty.
- **Ability, the weighing** **[M1994-008]**. For: toothpaste share regained from 39.4% (2021) to 41.4% (2024) under this CEO;
  prices raised about a fifth through 2022 and 2023 with margin restored by 2024 (Q2); record operating cash in 2025. Against: the
  Filorga purchase (2019, under this CEO) and the skin-health unit written down $2.2 billion; North America margin down from 33.5%
  to about 22% (Q2); Hill's margin down from about 28% to 19% to 23% after the 2022 plant purchase, followed by the 2025 decision to
  exit the private-label pet food that came with the plants; restructuring in nearly every year. Chairman and CEO in one person, with
  an independent Lead Director (proxy) **[L2014-026]**.
- **VERDICT on integrity: IN.** No doubt about honesty is raised by the accounts, the proxy or the record; the featured adjusted
  figure and guidance are weighed and do not reach doubt **[M2013-088]**, **[M2004-067]**, **[M1998-036]**. **Ability WEIGHS BOTH
  WAYS**: the franchise has been run well, the money spent outside it has not **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **Where the money went, 2021 to 2025** (cash-flow statements): owner cash after interest $13,370M in total (Q4 table); dividends
  to common holders $8,376M declared (statements of equity: 1,515; 1,562; 1,584; 2,034, five declarations; 1,681); buybacks $6,705M,
  less $1,961M received for options exercised; acquisitions $1,102M; total debt up from $7,600M (2020, `tools/run.py` debt lines,
  filed totals) to $7,988M. More went out than the business produced, the difference borrowed. Over the longer span the
  acquisitions were PCA Skin and EltaMD ($728M, 2018), Filorga ($1,711M, 2019), hello ($353M, 2020), the Red Collar plants and
  other ($809M, 2022) and Prime100 ($293M, 2025).
- **The retention test** **[M1998-033]**, **[M1998-110]**. Little is retained: payouts exceed owner cash. What was retained and spent
  on businesses is the test's object, and its largest use failed it: $2.4 billion into skin health, written down $2,211M (Q4); the
  dollar given was worth far less than a dollar received **[M1995-001]**. The Red Collar plants were bought with a private-label
  business that was exited in 2025, and Hill's margin is below its pre-purchase level (Q2). No post-mortem against the original
  projections appears in the filings read **[L2014-013]**. Weighs against.
- **Buybacks** **[L1999-023]**, **[L2016-002]**, **[L2011-003]**. The 2025 Program is a sum, "up to $5 billion", with no price named
  (10-K Item 5); shares are bought "to maintain its targeted capital structure and to fulfill certain requirements of its
  compensation and benefit plans" (MD&A). Average prices paid (total purchase price over shares bought, 10-Ks): 2014 $65.9; 2015
  $68.0; 2016 $69.2; 2018 $66.2; 2019 $69.9; 2021 $79.0; 2022 $76.5; 2023 $76.6; 2024 $93.0; 2025 $84.6; Q2 2026 $87.40 (10-Q). Set
  against the Q7 central range, $49.64 to $83.25 a share (run when Q7 was reached, recorded back here): every year's average sits above
  the bottom, and 2024 to 2026 sit at or above the top. By the convention on a buyback with no stated price, it weighs against
  **[L2016-002]**, **[L2013-012]**. Part of the buying offsets option exercises, the "sell low and then they buy high" pattern
  **[M1998-027]**, and buying to offset dilution is not a reason **[M2016-049]**, **[M2014-008]**. The same row M1998-027 likes
  buybacks in a wonderful business "even at prices that may give you nose bleeds"; that tension is carried OPEN in section VI (Q6:
  M1997-131 and M1998-027 against M1996-013) and not settled here.
- **Issuance and deals.** All acquisitions were for cash; no all-stock deal, so the one STOP of Part A is not met; no serial issuance
  (diluted shares 960M in 2012 to 811M in 2025).
- **Dividends.** $2.08 a share declared for 2025, raised each year (MD&A; statements of equity); the policy is clear and
  consistent **[L2012-015]**. A dividend is right where retained dollars cannot earn more than a dollar **[M2004-089]**, and the
  acquisition record says that here they have not.

**Part B, the pay, the board and the owners** (proxy, DEF 14A `0001308179-26-000136`).
- **Pay tied to what?** Annual bonus 80% on Base Business EPS and organic sales growth, 20% on strategic initiatives; long-term
  awards on organic growth relative to a peer group (50%), Base Business net income growth relative to peers (30%) and free cash flow
  as a share of net income (20%). Both EPS and net income measures exclude "restructuring charges, charges for certain litigation and
  tax matters, acquisition-related costs" and other items; organic growth excludes currency and acquisitions. So the costs of the
  failed purchases and of the yearly restructuring never reach the pay measures, and no measure charges for the capital used: "a
  batting average that does not include a cost of capital is a phony batting average" **[M1995-010]**; pay tied to what the person
  controls **[M2003-019]**, and the acquisitions were in management's control. Options are ten-year, at market, with no step-up for
  retained earnings **[L1994-021]**. A compensation consultant (FW Cook) advises the committee **[M2004-016]**, and two of three
  long-term measures are relative to a comparison group **[L2005-015]**.
- **For the owners:** the bonus fell with results; the committee removed a write-down benefit from the cash measure against the
  officers; officers hold two to eight times salary and the CEO holds about $31.6M of stock directly; no hedging, no pledging,
  clawbacks.
- **The board:** CEO is also Chairman, with a Lead Director **[L2014-026]**; directors are paid about $300,000, of which $180,000 in
  granted stock and $45,000 in options; whether any bought shares "with their savings" **[L2019-008]** is not shown in the proxy read.
- **WEIGHS AGAINST.** Part A: the retained dollars spent on businesses lost most of their value **[M1995-001]**, **[M1998-110]**, and
  buybacks with no stated price were made at or above the top of the Q7 range **[L2016-002]**, **[L2011-003]**. Part B: pay is
  measured on figures that exclude the costs of those choices and charge nothing for capital **[M1995-010]**, **[M2003-019]**,
  softened by real ownership and a bonus that fell with results.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**: value is "the discounted value of the cash that
can be taken out of a business during its remaining life" **[R1996-018]**, credited only with "whatever net cash is left every
year" **[M1998-080]**, after what must be put back in **[M2014-068]**. Arithmetic in `value.py`, output in `value_output.txt`.

- **The construction** (Q7 CONVENTION and its specifics, applied as written):
  - Cash input: owner cash after every real cost (Q4 table), on the all-equity basis (before interest, after the company's own tax,
    after minority dividends), five-year average 2021 to 2025 **[L2005-003]**.
  - (a) Cycles: neither end year (2021, 2025) is described by the filer as a peak, trough or aberrational year; 2022, the low year
    the filer ties to working capital, is inside the window. Literal window used.
  - (c) Acquisitions: $809M (2022) and $293M (2025) deducted, total growth credited (the default pair) **[M1998-080]**,
    **[M2014-068]**; the organic pair shown beside.
  - (d) Working capital: inside operating cash; no single-event draw the filer ties to one contract.
  - (e) Growth spending: the filing gives no maintenance split; the run's guess ($500M to $525M to $550M, Q3) is shown beside, not
    central, because the guess is the run's and not the filing's.
  - Growth shown: measured on the aggregate series between the end years, 2021 to 2025: **5.79%** a year; carried ten years, then
    zero nominal growth; discounted at the sovereign 5.64%. (f) No rate above the discount rate after year ten; 5.79% inside ten
    years is the shown rate and the cap.
  - Net debt $6,404M at 2026-06-30 (Step 0); no deal closed after the window; no carryforward shelter priced (the company pays tax
    near its statutory mix, 23% non-GAAP effective).
- **The range, all-equity (central):** base $2,593M (series 2,536 / 909 / 2,927 / 3,416 / 3,177). Whole business $45,975M (no
  growth) to $72,770M (shown growth), **1.58 to one**. Less net debt, per share: **$49.64 to $83.25**, midpoint $66.45, against
  **$87.25**. Expected return at the price (market value plus net debt, $75,957M): **3.41%** (no growth) to **5.42%** (shown growth).
- **Beside it, never deciding alone:**
  - equity-only (owner cash after interest, base $2,454M, growth 5.37%): $54.57 to $83.55 a share; return at the price 3.53% to
    5.42%;
  - organic pair (acquisitions left out, the filer's organic growth 5.73% a year, 2021 to 2025, credited): $54.54 to $90.53 a share
    all-equity; return at the price 3.70% to 5.82%. The organic figure includes price rises in hyperinflationary markets that the
    dollar owner never receives: reported net sales grew 1.4% a year from 2012 to 2025 while organic growth ran several points higher,
    the gap being currency (MD&A reconciliations each year);
  - maintenance-only spending at the $525M guess: $51.72 to $85.71 a share; return at the price 3.54% to 5.56%;
  - the longer record: operating cash less stock pay, capital spending and acquisitions grew 3.70% a year from the 2014 to 2016
    average to the 2023 to 2025 average (XBRL); at that rate the central top is $69.28 a share. The window's 5.79% is above the
    longer record, so the shown-growth end is generous, not stingy.
- **How sure** **[M1999-104]**: the castle is strong (Q2) and the cash is about two thirds foreign, 45% emerging-market, where the
  rows ask to be "paid more" **[M2006-021]** and the margin grows as certainty falls **[M1997-080]**; the use of retained cash has
  turned dollars into "fifty-cent pieces" once already **[L2010-002]** (Q6).
- **The floor (CONVENTION):** about ten percent on the price, applied to owner cash after the company's own tax, no conversion
  **[M2003-149]**, **[L2002-020]**. At $87.25 the expected return is 3.4% to 5.4% on the central basis and at most 6.0% on any
  variant shown; below the floor on every basis, and below the long government rate itself at the no-growth end.
- **Value range:** $49.64 to $83.25 a share (all-equity, central) against $87.25. **Closes:** the range is narrower than three to one
  (1.58), so not TOO HARD; the price sits **above the top** of the range, which closes OUT by the floor convention: the expected return
  at the price is below the minimum **[M2003-149]**. No pencil was needed to see it; the case is the opposite of a screamer
  **[M2009-005]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$32.44** a share on the all-equity basis (the midpoint stream,
  the average of the no-growth and shown-growth streams, whose value at the sovereign is the range's midpoint, discounted instead at
  the 10% floor: $32,264M for the whole business less net debt $6,404M, over 797.17M shares), after the company's own tax; the
  equity-only figure beside it **$37.64**. No cheap price is reported.
- **VERDICT: OUT.** Valued, a range of 1.58 to one, and the price above its top: "there's just a point at which we drop out of the
  game" **[M2003-149]**; the expected return of 3.4% to 5.4% does not clear the floor **[L2002-020]**, and the margin the foreign
  exposure and the capital record call for **[M2006-021]**, **[M1997-080]** is negative. The all-equity basis decides **[L2017-004]**;
  the equity-only figure agrees.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** The file closed OUT at Q7.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.**

---
## THE BOX
**OUT at Q7, on price by the floor.** Range $49.64 to $83.25 a share (all-equity, central; 1.58 to one) beside $87.25; expected
return at the price 3.4% to 5.4% against a floor of about ten percent. Q1 IN, Q2 IN, Q3 weighs for, Q4 weighs against (accounts
clear), Q5 integrity IN (ability both ways), Q6 weighs against. Reporting figures: fair price $32.44 all-equity, $37.64 equity-only.
No integrity facts are left unjudged (Q5 was reached and answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**. Every figure here is COMPUTATION, NOT A
CLEARANCE.
- **Q8 (the bond):** the 30-year Treasury yields 5.64% (2026-10-06, Treasury); the central expected return at $87.25 is 3.41% to
  5.42% (Q7). The alternatives of Q8 were not compared.
- **Q9 (debt and exposures):** total debt $7,988M at 2025-12-31 and $7,857M at 2026-06-30; net debt $6,404M; scheduled maturities
  $1,115M (2026, refinanced in H1 2026 largely with commercial paper: short-term borrowing +$1,053M, 10-Q), $523M (2027), $615M
  (2028); commercial paper backed by a $3,000M revolving facility to November 2030; unused lines $3,641M; bank agreements carry
  covenants and cross-default provisions, "in full compliance" (note 6). Pre-tax earnings over interest expense 2025: (3,059 + 267) /
  267 = 12.5 times, 15.9 times before the write-down. Operating leases $566M left out of net debt. Talc cases pending: 453 at
  2025-12-31, 525 at 2026-06-30 (10-Q); reasonably possible losses beyond accruals $0 to about $225M across disclosed matters (note
  13); Brazil Kolynos tax assessments about $97M and $26M; IRS imputed-income matter about $165M, not reserved. Derivatives
  "prohibit the use of derivatives for speculative purposes and leveraged derivatives for any purpose" (MD&A). The Strategic Growth
  and Productivity Program, $350M to $550M, mostly cash, through 2028, with projected annualized pre-tax savings of $200M to $300M
  (10-Q).
- **Q10:** none beyond Q7.
- **Q12:** no business named in Q12 is carried on (toothpaste, soaps, cleaners, pet food).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy was its own command; `tools/run.py`, the first fetch, ran after it);
      written question by question; committed after each: Step 0 to the standing rule, Q1, Q2, Q3, Q4 (and a correction to Q4's
      goodwill sentence committed before Q5 was written), Q5, Q6, Q7, then the close. Pathspec commits of the run file and the
      research folder only.
- [x] Dispatched: the brief allowed the per-question commits; the lock in `Screens/_daily/` was the dispatching session's (read,
      not touched). Folding is the dispatcher's; a run not in the register binds nothing.
- [x] No other run file, holding review, `PORTFOLIO.md`, queue or reading-list file was opened, listed or searched; `Test Runs/`
      was not listed. Seen by accident and declared under CONTAMINATION at the top: commit subjects and research-folder names in the
      opening git status, the memory index line, ticker names in `.gitignore` comments. Not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (`check_ids.py` in the
      research folder, output `check_ids_output.txt`); no E-ids. Every filing fact carries its document and accession in Step 0 or
      at the point of use.
- [x] The order was kept; Q7 was the first STOP to fail and closed the file; Q8, Q9, Q10, Q12 NOT REACHED; their facts are under
      AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash from operating cash after stock pay, all capital spending and minority dividends, never net income (operator rule
      5); sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations list, and in Q2, Q3, Q4, Q6).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; two of its lines were found wanting and said so in Step 0 (no
      minority-dividend line though the filing has one; the debt "sum" double counts the current portion in 2024 and 2025).
- [x] `python tools/check_framework.py` run before the closing commit (result recorded in the closing commit message).
- Declared: the maintenance guess ($500M to $550M) and the 23% tax rate on the interest add-back are the run's own figures, each
  stated with its basis; the definition of the "midpoint" for the fair price is the run's reading (below).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Parts (Q2, section B).** "Where a company reports parts with different economics" does not say whether the parts are product
segments or reportable operating segments. Colgate has two product segments, the first managed through five geographic reportable
segments. On product segments the oral-personal-home care part decides at 80%; on reportable segments none passes half and Latin
America decides as the largest at 27.7%. Both readings land on the same oral-care castle here, so the box does not turn on it; for
another filer it could. (2) **Fair price.** "The price at which the midpoint of the range earns the floor" does not say what stream
the midpoint is. The run took the average of the two end streams (whose value at the sovereign is exactly the midpoint) and
discounted it at 10%; another analyst could instead solve for a single growth rate whose value is the midpoint, which gives a
slightly different figure. (3) **The organic pair** in specific (c) credits "organic growth, as the filer reports it"; for a filer
with two thirds of sales abroad and hyperinflationary markets, organic growth includes local price rises that currency takes back
before they reach a dollar owner (reported sales grew 1.4% a year 2012 to 2025). The pair was shown and not used to decide; the rule
could say the organic pair is credited only net of the currency effect the filer itself reports. (4) **Minority holders.** Q4's
list of real costs does not name dividends paid to noncontrolling holders ($135M to $170M a year here); the run deducted them as cash
that never reaches the owner, and `tools/run.py` did not print them. (5) **The growth measure** "between the end years" falls on a
series in which an end year carries an acquisition payment (2025, $293M); the default pair deducts it, which lowers the end point and
the growth credited. Not decisive here (the price is above the top either way), but the text does not say whether a deal in an end
year should be spread. (6) **Restructuring every year.** Q4 calls recurring restructuring a real cost **[L2016-007]** but says
nothing on how to count it when owner cash is built from operating cash, which already bears the cash part; the run counted it once
through operating cash and did not add the non-cash part back.

**Where this brief erred** (the dispatcher asked): the brief's reporting paragraph reads "the VALUE RANGE as Q7 builds it, with a built
by Q7's six specifics", a garbled clause, and its parenthesis names three of the six specifics as if they were the list; the brief
says `tools/run.py` prints "dividends to minority partners" among its alternates, but for CL it printed none though the statement of
equity carries $157M to $170M a year; and the brief's blind rule forbids other companies' run files "of the last week" while the
dispatcher's message forbids "every run file of other companies" (the stricter reading was kept). The reporting paragraph also points
to section F of `Framework/v5/CASE 2026-10-05 - gaps found by the small-cap runs, for the operator's approval.md` while the blind rule
forbids opening any `Framework/v5/CASE` file "not yet adopted"; the case was not opened, and Part VII's adopted text was used instead.
