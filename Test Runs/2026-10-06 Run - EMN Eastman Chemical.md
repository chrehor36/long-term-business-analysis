# Company Run: Eastman Chemical Company (NYSE: EMN), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. *(Template headings carried with a plain hyphen or
colon in place of the template's dashes: the dispatch for this run forbids em dashes.)*

**POSITION NOTE, declared before any verdict:** not checked. The dispatch for this run is blind and forbids opening
`PORTFOLIO.md`, so whether the operator holds EMN is unknown to the analyst. The run is written as a purchase run for a
name not known to be held.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, any other run or research
file on EMN, any other company's 2026-10-05 or 2026-10-06 run or research-pass file, and the unadopted 2026-10-05 gaps case.
Seen without opening: (1) a directory listing of `Test Runs/` that showed the file name
`2026-07-16 Run - Industrials & Misc 9-pack (LKQ SLVM GPK UFPI FBIN EMN AMPH IIPR VSNT).md` (an older pre-v4.1 run that
includes EMN; its contents and verdict were not seen) and the names of the 2026-10-05 holding reviews, research passes and
runs (names only); (2) the session's recent commit subjects, which give verdicts for four other names (MTCH TOO HARD
(NATURE) at Q1; NWL OUT at Q2; MD OUT at Q2; COLL OUT at Q1) and nothing on EMN; (3) the git status, which names three other
2026-10-06 run files (INSW, LRN, NX), names only; (4) the project memory index, which carries general queue state and no
EMN fact. No EMN verdict from any earlier session was seen.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $64.94 (close 2026-10-05; aggregator live quote via `tools/run.py`, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 114,377,421 common, single class (Form 10-Q for the quarter ended
  2026-06-30, filed 2026-07-31, accession `0000915389-26-000141`; `python Screens/cover_shares.py EMN`). The 10-K gives
  114,097,314 issued and outstanding at 2025-12-31, of which 50,798 held by the company's charitable foundation (10-K FY2025,
  Item 5, accession `0000915389-26-000013`). No other class.
- **Market cap:** $7,428M (114.377M x $64.94).
- **Sovereign for the earnings currency:** USD, 30-year par yield 5.66% (US Treasury daily par yield curve, 2026-10-05;
  `python tools/sources.py`). Earnings currency USD (the filer reports in dollars; about 55% of 2025 sales came from outside
  the US and Canada, 10-K FY2025, Item 1).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-13, accession `0000915389-26-000013` (Items 1, 1A, 2, 3, 5,
  7 in full; notes 1, 2, 4, 5, 9, 11, 20 in part); 10-Q for Q2 2026, filed 2026-07-31, accession `0000915389-26-000141`
  (MD&A in full); proxy (DEF 14A) filed 2026-03-24, accession `0000915389-26-000074` (compensation discussion, summary
  compensation table, ownership); 8-K of 2026-07-30 with Exhibit 99.01 (Q2 2026 release), accession
  `0000915389-26-000138`; 8-K of 2025-10-08 (officer change), accession `0000915389-25-000160`. For the span, the segment
  sections of every 10-K from FY2009 to FY2024: FY2009 `0000915389-10-000020`, FY2010 `0000915389-11-000022`, FY2011
  `0000915389-12-000031`, FY2012 `0000915389-13-000010`, FY2013 `0000915389-14-000013`, FY2014 `0000915389-15-000021`,
  FY2015 `0000915389-16-000095`, FY2016 `0000915389-17-000014`, FY2017 `0000915389-18-000016`, FY2018
  `0000915389-19-000009`, FY2019 `0000915389-20-000016`, FY2020 `0000915389-21-000016`, FY2021 `0000915389-22-000010`,
  FY2022 `0000915389-23-000015`, FY2023 `0000915389-24-000016`, FY2024 `0000915389-25-000012`. Texts and scripts are in
  `Test Runs/_research 2026-10-06 EMN/`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025, $970M, read
  on the face of the consolidated statement of cash flows in the 10-K FY2025 (`0000915389-26-000013`), with 2024 at $1,287M and
  2023 at $1,374M; `tools/run.py` transcribes the same three figures from XBRL. Also checked: total borrowings $4,787M at
  2025-12-31 (10-K, MD&A, Net Debt table) against the run.py debt sum of $4,787M.
- **`python tools/run.py EMN`, arithmetic lines only** (output saved as `run_py_output.txt`; its v4 lines are not used, per
  Part VII). Owner cash after every real cost (OCF less stock pay less all capital spending), by year, USD millions, with
  capitalised software added to capex where the cash flow statement shows it:

  | Year | OCF | Stock pay | Capex (incl. software) | D&A | Owner cash, capex basis | Owner cash, D&A basis |
  |---|---|---|---|---|---|---|
  | 2016 | 1,385 | 36 | 626 | 580 | 723 | 769 |
  | 2017 | 1,657 | 52 | 649 | 587 | 956 | 1,018 |
  | 2018 | 1,543 | 64 | 528 | 604 | 951 | 875 |
  | 2019 | 1,504 | 59 | 431 | 611 | 1,014 | 834 |
  | 2020 | 1,455 | 44 | 396 | 574 | 1,015 | 837 |
  | 2021 | 1,619 | 70 | 578 | 538 | 971 | 1,011 |
  | 2022 | 975 | 69 | 624 | 477 | 282 | 429 |
  | 2023 | 1,374 | 64 | 833 | 498 | 477 | 812 |
  | 2024 | 1,287 | 63 | 599 | 509 | 625 | 715 |
  | 2025 | 970 | 48 | 546 | 513 | 376 | 409 |

  Five-year average 2021-2025: $546M on the capex basis, $675M on the D&A basis (run.py agrees: 546 and 675). Stock pay is
  resolved (the `AllocatedShareBasedCompensationExpense` line every year) and complete for these years. Two items the
  tagged data does not show, read in the filings: (a) **receivables factoring**. The company sells about $2.7B of
  receivables a year without recourse; the receivables that would have been outstanding had they not been sold were $150M at
  end-2020, $239M (2021), $402M (2022), $397M (2023), $385M (2024), $346M (2025) (10-K FY2020 to FY2025, MD&A, Working
  Capital Management). The rise of $196M over the five-year window flowed through operating cash, about $39M a year;
  (b) **supplier finance**: confirmed obligations $69M (2023), $56M (2024), $110M (2025) (10-K FY2025, note 1), small. The
  2021 and 2022 cash includes businesses since sold (rubber additives sold 2021-11-01, adhesives resins sold 2022-04-01,
  Texas City operations sold 2023-12-01; proceeds $667M, $998M and $456M, cash flow statements, 10-K FY2022 to FY2024).
  Depreciation alone was $425M in 2025; amortisation of acquired intangibles $79M (10-K FY2025, notes 4 and 5). Capex for
  2026 is guided at about $400M, "primarily for maintenance capital and limited growth capital for projects already in
  progress" (10-K FY2025, MD&A, Capital Expenditures).

- **The balance sheets, read first (the template asks for them here because the file closes before Q4).** Ten year-ends from
  `tools/run.py` (first-filed XBRL, transcription), read against the filed statements, USD millions:

  | Year-end | Equity | Goodwill | Intangibles | Equity less goodwill and intangibles | Cash | Receivables | Inventory | Debt on the face | Retained earnings |
  |---|---|---|---|---|---|---|---|---|---|
  | 2016 | 4,532 | 4,461 | 2,469 | (2,398) | 181 | 812 | 1,404 | 6,594 | 5,721 |
  | 2019 | 5,958 | 4,431 | 2,011 | (484) | 204 | 980 | 1,662 | 5,782 | 7,965 |
  | 2022 | 5,153 | 3,664 | 1,210 | 279 | 493 | 957 | 1,894 | 5,151 | 8,973 |
  | 2025 | 5,961 | 3,665 | 970 | 1,326 | 566 | 737 | 1,980 | 4,787 | 10,105 |

  What moved and why. (1) **The equity is mostly purchased goodwill.** Goodwill was $315M in 2009 and $406M in 2011, then
  $2,644M after Solutia (2012, $4.8B consideration including $1.5B of its debt and $700M of Eastman stock, 10-K FY2012) and
  $4,486M after Taminco (2014, $2.8B including $1.1B of its debt, 10-K FY2014). Equity less goodwill and intangibles was
  negative at every year-end 2016 to 2020 and is $1,326M now; the improvement came from paying debt down, amortisation, and
  the write-off of goodwill with the businesses sold (rubber additives carried $398M of goodwill and $381M of intangibles and
  was sold for $687M, a $552M loss, 10-K FY2021, note 2). (2) **Retained earnings rose $4,384M from 2016 to 2025 while equity
  rose $1,429M**: the difference went to repurchases ($3.8B, 2016-2025, cash flow statements) and other comprehensive items.
  (3) **Inventory against sales went up**: inventory was 15.6% of sales in 2016 and 22.6% in 2025, on sales that fell from
  $9,008M to $8,752M. Receivables look lower only because $346M was sold; with the factored amount added back, receivables
  were 12.4% of 2025 sales against 9.0% in 2016 (factoring outstanding is first disclosed for end-2019, $169M, so the 2016
  figure may also be understated). (4) **Debt** fell from $6.6B (2016) to $4.8B (2025) and rose again to
  $5.2B at 2026-06-30 after $600M of 4.5% notes due 2031 were issued in Q1 2026 (10-Q Q2 2026, MD&A). (5) **Pension and
  retiree promises** are small against the balance sheet: US pension $85M short, non-US pension $55M over, retiree medical
  $144M short at 2025-12-31 (10-K FY2025, note 11), with the US plan assuming 7.50% on its assets. What the figures cannot
  say: what the methanolysis assets in Kingsport and the Longview project will earn; the Longview grant was
  terminated by the Department of Energy on 2025-05-29 and the filer is "actively evaluating the impact of the termination
  on the project's scope, timeline, and carrying values of associated assets" (10-K FY2025, note 1).

## THE FOUNDATIONS (not a gate)
- A share is a business: the test is whether I would be content to own Eastman "if the market closed for five years"
  **[M1997-109]**, so the reading below is of the four businesses and their cash, not of the quote, which "just tells us
  prices" **[M2006-077]**.
- No macro enters: "macro conclusions are [...] just never enter into the discussion" **[M2000-094]**. So the 2026 lift in
  Chemical Intermediates prices, which the filer puts down to "tightening market conditions from the ongoing Middle East
  conflict" (10-Q Q2 2026, MD&A), is a macro event and is not counted as earning power.
- Margin of safety: if the case needs pencil and paper, "it's too close to think about" **[M1996-084]**. The analyst's
  habits: look for "what's wrong in things" **[M2025-013]**.
- **Contrary evidence, written down as found** **[M1997-127]**: (a) through the 2023-2025 chemical downturn Eastman's
  GAAP EBIT margin held at 8.9% in 2025 while Celanese, Huntsman and Dow went negative (Q2, competitor row), so part
  of the decline below is the cycle, not the castle; (b) Fibers raised acetate tow prices 26% in 2023 and tripled its
  earnings on flat volume, which is pricing power, and in 2009 it raised prices 8% in a recession and lifted earnings
  24% (10-K FY2023, FY2009); (c) Additives & Functional Products held its 2025 earnings up 5% on cost-pass-through
  contracts in a weak year (10-K FY2025); (d) management owns stock (the chief executive holds 501,158 shares and
  units outside options, about $33M at the price, proxy 2026); (e) Q2 2026 volume grew across Advanced Materials.

## THE STANDING RULE
Buying EMN for cash, with no borrowed money and no instrument that can call for collateral, does not "risk what we have
and need" **[M2012-081]**; the buyer's conduct carries no "short-term debt maturities of size" and no "collateral calls"
**[L2014-024]**. The standing rule is met so long as the purchase is unlevered and sized so that a 50% fall
does not force a sale; the operator's sizing is not known to this blind run.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, and the chemistry need not be understood: of a petroleum-additives business, "I never
  would understand the chemistry of it, but I [...] but that's not necessarily vital. What is important is that I understand the
  economic dynamics of the industry" **[M2011-014]**.
- **What the business is** (10-K FY2025, Item 1). Four segments, 2025 sales and adjusted EBIT: Advanced Materials (AM,
  copolyesters such as Tritan, Saflex PVB interlayers for car and building glass, window and paint-protection films) $2,880M
  and $349M; Additives & Functional Products (AFP, coatings additives, care additives, amines, heat-transfer fluids) $2,880M
  and $516M; Chemical Intermediates (CI, olefins, acetyls, oxo alcohols, plasticizers) $1,925M and a $38M loss; Fibers
  (acetate tow for cigarette filters, 69% of the segment, plus acetate yarn and nonwovens) $1,050M and $285M. "Other" (the
  circular-economy and cellulosic growth initiatives, research) lost $182M before non-core items. The streams are integrated:
  CI "sells excess intermediates beyond the Company's internal specialty needs" and supplies the specialty segments with
  "advantaged cost positions".
- **The key variables** **[M1998-044]**: (1) acetate tow volume and contract price, which the filer ties to cigarette demand,
  customer backward integration in China and "industry capacity utilization" (10-K FY2016, FY2017, FY2023); (2) the CI spread
  of olefin and acetyl prices over propane, ethane and propylene, set in a world market with Asian capacity; (3) price and
  volume of the specialty lines (AM, AFP) against named rivals (Sekisui, Kuraray and two Chinese makers in interlayers; SK
  Chemicals, Covestro and others in copolyesters; BASF, Dow, Celanese and others in additives); (4) the return on the
  molecular-recycling capital (Kingsport methanolysis, running since 2024; Longview, grant terminated in 2025; a French
  project announced in 2022, of which a text search of the FY2025 10-K for "France" found no mention).
- **Are they foreseeable?** Variables 1 to 3 belong to old, slowly changing industries whose dynamics the filings describe
  plainly: the company began in 1920, the tow and acetyl chains have run at Kingsport for decades, and the competitors are
  named and few. That is the "economic dynamics of the industry" kind of understanding **[M2011-014]**; I can say "how the
  industry will develop and where the company will stand within the industry" **[M2012-065]** in kind: tow volume declines
  slowly, intermediates cycle with Asian supply, specialty additives grow with their end markets. Variable 4 is a technology
  and policy bet whose economics are not foreseeable from the filings (the filer itself is evaluating the carrying value of
  Longview). The past statements do tell me the shape of the future ones **[M2008-033]**, although six re-segmentations
  between FY2011 and FY2024 make the comparison laborious. The recycling bet is not the earning base: the incremental
  earnings the proxy credits to Kingsport methanolysis in 2025 were "approximately $60 million" (proxy 2026), against $930M
  of adjusted EBIT. It weighs on capital allocation (Q6, not reached), not on whether the base can be understood.
- **Routing.** Not a fast-moving technology business; not a financial institution; not a holding company. The question is
  "important and knowable" **[M2006-076]** for the earning base.
- **VERDICT: IN.** The ten-year economics of the four parts can be reasoned about in kind from the filings **[M2012-065]**,
  **[M2011-014]**; the recycling bet is flagged as the least foreseeable piece and is small in the earning base (proxy 2026,
  $60M of incremental 2025 earnings). Filing facts: 10-K FY2025 Item 1 and note 20 (`0000915389-26-000013`).

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what's going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**; a castle is a moat "that protects excellent returns on invested capital"
**[L2007-004]**. Eastman is a mix of specialty and commodity segments, so the castle tests are run on each part and then on
the whole.

**The castle the filer claims.** For each stream "the Company has developed and acquired a combination of assets and
technologies that combine scale and integration across multiple manufacturing units and sites as a competitive advantage",
worked through an "innovation-driven growth model" (10-K FY2025, Item 1, Business Strategy). The segment claims: AM
"principally competes on differentiated technology and application development capabilities"; AFP makes additives that
"comprise a small percentage of total customer product cost"; CI product lines "remain cost competitive and, for some
products, cost-advantaged"; Fibers has "the largest and most integrated acetate tow site in the world" (same filing).

**The parts over the span** (segment sales and EBIT excluding the filer's non-core items, USD millions, from the 10-K of
each year or the next; margins mine; segments were re-drawn in FY2012, FY2014, FY2016, FY2022 and FY2024, and each figure is
the one the cited 10-K prints):

| Segment | 2009 | 2015 | 2019 | 2022 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|
| Fibers sales / EBIT / margin | 1,032 / 300 / 29% | 1,219 / 390 / 32% | 869 / 194 / 22% | 1,022 / 140 / 14% | 1,050 / 285 / 27% | 468 / 81 / 17% |
| AM sales / EBIT / margin | (Specialty Plastics) 749 / 13 / 2% | 2,414 / 409 / 17% | 2,688 / 518 / 19% | 3,207 / 395 / 12% | 2,880 / 349 / 12% | 1,532 / 178 / 12% |
| AFP sales / EBIT / margin | (CASPI) 1,217 / 224 / 18% | 3,159 / 660 / 21% | 3,273 / 550 / 17% | 3,475 / 546 / 16% | 2,880 / 516 / 18% | 1,546 / 293 / 19% |
| CI sales / EBIT / margin | (PCI) 1,330 / 69 / 5% | 2,811 / 294 / 10% | 2,443 / 192 / 8% | 2,716 / 349 / 13% | 1,925 / (38) / -2% | 1,138 / 40 / 4% |

Sources: FY2009 10-K `0000915389-10-000020` (Fibers, PCI) and FY2010 10-K `0000915389-11-000022` (CASPI and Specialty
Plastics 2009); FY2016 10-K `0000915389-17-000014` (2015, as re-drawn); FY2020 10-K `0000915389-21-000016` (2019); FY2023
10-K `0000915389-24-000016` (2022, with AFP and CI as re-drawn that year; the FY2022 10-K had printed AFP at 3,165 / 483 and
CI at 3,026 / 412); FY2025 10-K `0000915389-26-000013`; 10-Q Q2 2026 `0000915389-26-000141`. Fibers year by year (EBIT excluding non-core): 2012 388,
2013 462, 2014 474, 2015 390, 2016 310, 2017 224, 2018 219, 2019 194, 2020 180, 2021 142, 2022 140, 2023 422, 2024 454,
2025 285. AM year by year: 2016 471 (19.2%), 2017 494, 2018 501, 2019 518 (19.3%), 2020 448, 2021 532, 2022 395 (12.3%),
2023 343 (11.7%), 2024 464 (15.2%), 2025 349 (12.1%).

**The whole over the span.** The filer's own EBIT excluding non-core items: 2011 1,073; 2013 1,591; 2014 1,613; 2015
1,717; 2016 1,534; 2017 1,631; 2018 1,635; 2019 1,389; 2020 1,216; 2021 1,635; 2022 1,339; 2023 1,097; 2024 1,298; 2025 930
(the overview table of the 10-K for the year or the next; 2011 as restated in the FY2012 10-K after the pension
accounting change, the FY2011 10-K having printed $891M). Diluted shares were 150M in 2015 and 116M in 2025 (XBRL, the same
10-Ks), so this measure per share fell from about $11.45 to about $8.02 while the company retained about $5.0B of earnings
over 2016-2025 (net earnings $8,478M less dividends $3,479M) and spent $5,810M on capital projects, capitalised software
included (cash flow statements, FY2016 to FY2025). Sales were $9,350M in
2013, the first full year with Solutia, and $8,752M in 2025, after Taminco was added in December 2014 ($2.8B consideration)
and three businesses were sold (proceeds $2.1B). Consolidated gross margin: 20.9% (2009), 25.2% (2010), 26.7% (2015), 24.1%
(2019), 20.2% (2022), 21.1% (2025) (XBRL, each year's 10-K).

**The castle tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**. The attackers are in the filer's own pages. CI: 2025 prices fell "primarily
   due to competitive pressure in Asia" (10-K FY2025, MD&A). Fibers: 2016 tow volume fell on "reduced sales in China
   attributed to weaker demand and customer backward integration" (FY2016 as printed in the 10-K FY2017,
   `0000915389-18-000016`); 2025 volume fell on "customer inventory destocking and industry capacity share adjustments"
   (10-K FY2025). AM: the interlayer competitors listed are Sekisui, Kuraray and two Chinese makers, Kingboard (Fo Gang) and
   Chang Chun; the copolyester competitors include SK Chemicals, Sichuan Push Acetati and Covestro (10-K FY2025, Item 1). The
   answer to "could I do it?" is yes for the intermediates, and the tow customers themselves have done it in China.
2. **Pricing power and the agony before a rise** **[M2005-020]**. Fibers showed real power once: 2023 prices rose 26% on
   flat volume and EBIT tripled, but the filer ties the price to the industry's load factor, "driven by an increase in
   industry capacity utilization" (10-K FY2023), as it tied the 2016-2017 price falls to "lower industry capacity utilization
   rates" (10-K FY2017). A price that follows the industry's utilisation is a price the industry sets. After the 2023 rise,
   volume fell 19% in 2025 and 14% more in H1 2026, with "modestly lower acetate tow contract pricing" (8-K 2026-07-30, Ex
   99.01). AFP raises price through "cost-pass-through contracts" (10-K FY2025), which holds the margin and does not lift
   it. AM price fell 2% in 2025 and 2% in H1 2026, with "modestly lower price-cost in advanced interlayers" in Q2 2026 (8-K
   2026-07-30).
   - The speakers name the failing form of this test: pricing pushed "too far to the point that they lost market share"
     **[M2001-087]**. Whether the 2023 tow rise did that, the filings do not say; the sequence is recorded, not concluded.
3. **Unit volume** **[M1999-054]**. A declining unit volume is not by itself a fail **[M2015-066]**, but in a plant business
   "Fixed costs are high [...] and that's bad news when unit volume heads south" **[L2006-009]**. Tow is 69% of Fibers sales
   and serves cigarette filters; the filer says the segment "seeks to offset declines in acetate tow" (10-K FY2025, Item 1).
   Fibers sales were $1,457M in 2014 and $1,050M in 2025, and in H1 2026 Fibers EBIT fell 52% on a 17% fall in sales, with
   "unfavorable asset utilization" (10-Q Q2 2026).
4. **The low-cost position** **[L2000-017]**, **[M1997-010]**. CI's claim is "cost competitive and, for some products,
   cost-advantaged" (10-K FY2025), not low-cost across the line, and CI lost money in 2025 at the bottom of the cycle while
   its price was set in Asia. Its 2026 recovery came from "supply disruptions" elsewhere (10-Q Q2 2026), which is a rival's
   misfortune, not a moat.
5. **The customer and the low bid** **[M2017-009]**, **[L2004-003]**. AFP passes this test on the filer's account: an additive
   that is a small share of the customer's cost and is formulated with the customer, and its margin held at 15% to 19% from
   2022 to H1 2026. The intermediates fail it: commodity solvents, olefins and acetyls are bought on price.
6. **Ask the competitors** **[M1999-130]**. Celanese, the other large Western tow maker, printed acetate tow at 16% of $5,082M
   of sales in 2009, 16% of $6,510M in 2013, 10% of $6,140M in 2017 (10-K FY2011 `0001306830-12-000015`, FY2014
   `0001306830-15-000022`, FY2017 `0001306830-18-000030`), and $519M as a segment in 2020, citing "lower acetate tow volume
   and pricing due to lower global industry utilization" (FY2017) and a 14% volume fall in 2020 (10-K FY2020
   `0001306830-21-000020`). Tow sales at Celanese roughly halved from 2013 to 2020, as Eastman's Fibers sales fell 42% from
   2014 to 2020. The industry's own record says the tow field shrank.
7. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Narrowing in every part over the decade: Fibers margin 32%
   (2015) to 27% (2025) and 17% (H1 2026); AM 18% to 19% (2016-2019) to 12% (2022, 2023, 2025, H1 2026); AFP 21% (2015) to 18%
   (2025); CI 10% (2015) to -2% (2025). The whole: EBIT excluding non-core items $1,717M (2015) to $930M (2025). The
   speakers' instruction is "we want the moat widened every year" **[M2000-018]**; this one has not widened in ten. In AM,
   films lines were closed and films capital projects terminated in 2025-2026, and performance films was the one reporting
   unit whose fair value did not "significantly exceed" its carrying value in the 2025 goodwill test (10-K FY2025, Critical
   Accounting Estimates).
8. **What could destroy, modify or reduce it** **[M2000-014]**. Cigarette volumes and Chinese self-supply for tow; Asian
   capacity for intermediates; Chinese entrants in PVB and copolyesters; a recycling platform whose largest project lost its
   federal grant.

**The competitor row** (same metrics, each filer's own 10-K figures through XBRL, 2009-2025; Covestro, SK Chemicals, Sekisui
and Kuraray file outside the SEC and were not read: flagged, not obtained):

| Company | Gross margin, avg 2009-2025 | Gross margin 2009-2014 / 2020-2025 | EBIT margin (pre-tax plus interest), avg 2009-2025 | 2015-2019 | 2023-2025 | Accessions (FY2025; FY2015) |
|---|---|---|---|---|---|---|
| Eastman | 23.9% | 23.9% / 22.5% | 12.7% | 14.4% | 12.2% | `0000915389-26-000013`; `0000915389-16-000095` |
| Celanese | 23.4% | 20.7% / 24.3% | 16.5% (includes a 2020 gain and 2024-2025 impairments) | 18.4% | 2.9% | `0001306830-26-000031`; `0001306830-16-000212` |
| Huntsman | 17.5% | 16.1% / 16.8% | 5.3% | 6.5% | -2.1% | `0001437749-26-004524`; `0001047469-16-010161` |
| Dow Inc. (from 2018) | 15.1% (2018-2020 only) | n/a | 6.1% (2018-2025) | 4.5% (2018-2019) | 1.5% | `0001751788-26-000018` |

What the row says: over the whole span Eastman's gross margin is the same as Celanese's, an acetyls-heavy company, and
above Huntsman's and Dow's; its EBIT margin sits between Celanese and the commodity makers and held up better than all three
in 2023-2025. Eastman is a better-run chemical company than its weaker peers; the row does not show a business whose
margins stand apart from the industry's, which is what a castle would show.

**The parts, judged.**
- **CI: no castle.** Its price is set by others, as at the gas station where "whatever he charged for gas was my price"
  **[M2012-109]** and the rival "determined our profit" **[M2023-079]**: the filer's 2025 price fall to Asian competition
  and its 2026 price rise from others' outages. The low-cost exception **[L2000-017]** is not shown (a loss at the trough,
  and the filer's own "for some products").
- **Fibers: a castle in a shrinking field, its price following the industry's utilisation.** The oligopoly earned 27% to
  34% margins in its good years, but its volume declines by the filer's own word, customers integrated backward in China,
  share moved in 2025, and the price falls when utilisation falls. "If you really think a business is declining, most of
  the time you should avoid it" **[M2012-062]**.
- **AM: narrowing.** Margins down a third since 2016-2019 on rising capital, price down in 2025 and H1 2026, films
  restructured, Chinese makers listed in interlayers. Part of the fall is the 2023-2025 downturn in cars, buildings and
  durables; the speakers read a bad year as "a cyclical problem, not a secular one" when "we at least maintained [...] our
  competitive superiority" **[L1995-022]**. The filings show the position maintained in volume (Q2 2026 growth "across the
  segment") but not in price or margin.
- **AFP: holding.** Cost-pass-through pricing, small share of customer cost, steady margins. It is the one part where the
  castle tests read well, and it is also where the acquired lines that failed sat: crop protection goodwill impaired by $45M
  in 2019 (10-K FY2019), $125M of tradename and customer intangibles impaired in 2020 (10-K FY2020), rubber additives sold
  at a $552M loss in 2021 and adhesives resins sold in 2022 for "earnings volatility that was not in line with Eastman's
  expectations for the performance of a specialty business" (10-K FY2023).

**CONVENTION (this run's, confessed): how a mix closes at Q2.** Q2 gives no rule for a company of several segments (Q1's
by-parts rule covers a holding company's understanding, not its castle). This run judges the whole by the castle the filer
claims for the whole (here, scale and integration across the streams, so the parts are not separable businesses an owner
could buy one at a time) and by the consolidated record, and reads each part for its evidence; the whole closes OUT when the
consolidated record shows the castle narrowing and no part shows it widening. Rationale: the filer's integration claim makes
the consolidated record the fair test of the claimed castle, and the rule keeps one strong part from licensing the whole.

- **VERDICT: OUT.** The speakers' test is "how wide the moat is and whether it's likely to widen further or shrink on you"
  **[M1999-108]**. The castle claimed for the whole has not protected the earning power: the filer's own EBIT excluding
  non-core items fell from $1,717M (2015) to $930M (2025), and per share from about $11.45 to $8.02, across a decade in which
  $5.0B was retained and $5.8B spent on plant. Two of the four parts carry prices set by others, by the filer's own account
  (CI by Asian competition, Fibers by industry utilisation and customer self-supply); the largest part by assets (AM, $5.7B
  of segment assets) has narrowed; only AFP holds. On the evidence the moat has shrunk, a castle being filled in, and of the
  money test the speakers say "If the answer had been yes, we wouldn't have done it" **[M2011-015]**. Price does not reopen
  it: "What you can't do is turn any investment into a good deal by paying little" **[M2019-015]**.
- **Why OUT and not TOO HARD.** A tenuous moat whose value cannot be judged goes to TOO HARD: "We don't know how to valuate
  that, and therefore we leave it alone" **[M2000-019]**. Here the narrowing is in the filed record and the filer's own
  words, not in a forecast nobody would write, so the question is answered, against the business. The strongest case against
  this verdict is recorded above: Eastman held up better than Celanese, Huntsman and Dow in the downturn, Fibers showed
  pricing power in 2009 and 2023, and AFP holds. Those facts describe a better-than-average chemical company; they do not
  describe a widening castle, and the competitor row puts Eastman's margins inside the industry's band, not above it.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed OUT at Q2).

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks when the file closes before Q4.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED. The arithmetic the owner asked for is below, headed as a computation.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Noted for the operator, not answered: about 69% of Fibers sales is acetate tow, made "for use in filtration
media, primarily cigarette filters", for customers that include "multinational as well as regional cigarette producers" (10-K FY2025, Item 1), so a run that reached Q12 would
have to ask whether supplying a named business counts as the named business.

---
## COMPUTATION - NOT A CLEARANCE
*(Written after the Q2 STOP at the owner's request for reporting; it is not a rule change and carries no entry language.
Operator rule 3's heading is written with a plain hyphen because the dispatch forbids em dashes.)*

**Method.** Value is "the discounted value of the cash that can be taken out of a business during its remaining life"
**[R1996-018]**, at "the yield on long-term U.S. bonds" **[L2000-021]**, here 5.66%. The Q7 CONVENTION of the framework
builds the range: five-year average owner cash after every real cost, carried ten years at the growth shown (never above it),
then no growth, the ends being the no-growth case and the shown-growth case. The debt is treated "on an all-equity basis"
**[L2017-004]**: owner cash is put back before interest (interest paid less a 16% tax effect, the filer's 2024 and 2025
effective rate), discounted, and net debt at 2026-06-30 ($4,526M, 10-Q Q2 2026) plus the net pension and retiree-medical
shortfall ($174M, 10-K FY2025, note 11) is subtracted. Shares 114.377M. Script: `Test Runs/_research 2026-10-06 EMN/value.py`.

**Owner cash** (from the Step 0 table, USD millions):
- Five-year average 2021-2025, capex basis: $546M; less the factoring lift ($196M over five years, $39M a year): **$507M**.
- D&A basis (OCF less stock pay less D&A): $675M, $636M after the factoring lift.
- Maintenance variant (depreciation of $425M taken as the maintenance need, beside the filer's guide of about $400M of 2026
  capex "primarily for maintenance capital"): $718M after the factoring lift.
- Ten-year average 2016-2025 (the whole-cycle variant), capex basis: $739M, $704M after a factoring lift of $35M a year; it
  includes the cash of the three businesses sold in 2021-2023 (proceeds $2.1B), so it overstates the business as it now is
  by an amount the filings do not give.

**The growth shown.** On the aggregate owner cash, endpoint to endpoint, 2021 to 2025: -21.1% a year; the five-year window
starts at a peak (2021, with businesses since sold) and ends at a trough (2025), and "If either year was aberrational, any
calculation of growth will be distorted" **[L2005-003]**, so the log-linear trend over the five years, -10.4% a year, is
shown beside it. Over ten years: endpoints -7.0%, trend -9.3%. No case carries positive growth, because none was shown.

**(a) VALUE RANGE** (USD a share; unlevered, at 5.66%; the price is $64.94):

| Case | No-growth end | Shown-growth end (trend) | Shown-growth end (endpoints) | Width |
|---|---|---|---|---|
| Five-year, capex basis (the convention's case) | $62.68 | $5.22 | below zero (-$19.14) | about 12 to 1 |
| Five-year, D&A basis | $82.61 | $7.40 | below zero | about 11 to 1 |
| Five-year, maintenance variant | $95.28 | $18.84 | below zero | about 5 to 1 |
| Ten-year whole-cycle, capex basis | $96.12 | $25.33 | $38.29 | about 3.8 to 1 |
| Five-year, capex basis, levered (owner cash after interest, debt rolled, nothing subtracted) | $78.32 | n/a | n/a | n/a |

Read by the Q7 CONVENTION, every unlevered case is wider than about three to one, which is the convention's TOO HARD close,
"the range must be so wide that no useful conclusion can be reached" **[L2000-025]**. The price sits at the top of the
five-year capex-basis range and inside the others. The whole-cycle variant is the case the dispatch asks for because the
window holds an abnormal year at each end; it too is wider than three to one.

**(b) FAIR PRICE.** Central case: the five-year capex-basis owner cash after the factoring lift ($507M), at no growth (the
upper end the convention allows, since the growth shown is negative). The floor is the Q7 CONVENTION's figure of about ten
percent pre-tax, which rests on "a very high probability of at least 10% pre-tax returns" **[L2002-020]** and "a point at which we
drop out of the game" **[M2003-149]**. Tax treatment: owner cash is after cash taxes, so the pre-tax figure adds back the
five-year average of income taxes paid ($126M) and, on the enterprise basis, interest paid ($196M): $829M pre-tax before
interest. **On equity plus net debt** (the all-equity basis, the run's primary statement): $829M / 10% = $8,290M, less
$4,700M of net debt and pension shortfall, = $3,590M, **about $31.40 a share**. On equity alone (pre-tax owner cash after
interest, $633M / 10%): about $55.30 a share. At $64.94 the central case returns about 6.8% pre-tax on equity plus net debt
and about 8.5% pre-tax on equity, both under the floor. Variants on the enterprise basis: D&A basis about $42.65,
maintenance variant about $49.80, ten-year whole-cycle about $52.25 (on equity alone: $66.59, $73.76, $74.20).

**(c) CHEAP PRICE.** Rule (CONVENTION of this run, confessed): the price at or below which the business is worth the price
even if the decline it has shown continues for ten years, that is, at or below the shown-growth end of the range, "the
bottom boundary of our estimate" **[L2013-012]**, so that no pencil is needed **[M1996-084]**. Five-year capex basis: about
$5 a share; ten-year whole-cycle: about $25 a share. On the five-year window the cheap price is, in practice, none.

**Record noted after the close (facts only, not judged, no verdict).** For a later reader of Q5 and Q6: the chief executive's
reported pay was $19.50M in 2025, $15.94M in 2024 and $17.60M in 2023; the 2025 annual plan set its threshold for adjusted
EBIT and for operating cash flow at $480M each against targets of $1.20B, paid 57% of target on actuals of $930M and $970M,
cut by the committee to 47%; the 2023-2025 performance shares paid 75% on an average adjusted ROIC of 8.91% against a target
of 8.75% (proxy 2026, `0000915389-26-000074`). Repurchases: $1.0B in 2021, $1.0B in 2022, $150M in 2023, $300M in 2024
(3,001,409 shares, about $100 a share), $100M in 2025 (1,420,768 shares, about $70 a share), none in H1 2026, under an
authorization that names no price (10-K FY2025, Item 5; 10-Q Q2 2026). The filer issues quarterly EPS guidance (8-K
2026-07-30, Ex 99.01). The credit facility's leverage covenant was "temporarily" adjusted through Q2 2027 "in the event of
further macroeconomic uncertainty impacting operating results" (10-K FY2025, MD&A).

---
## THE BOX
**OUT, at Q2**: the castle claimed for the whole (scale and integration across the streams, plus innovation) is shown
narrowing on the filed record (the filer's own EBIT excluding non-core items $1,717M in 2015 to $930M in 2025; two parts priced
by others; AM margins down a third), with only AFP holding. Not reached Q7; the computation puts the five-year capex-basis
range at about $5 to $63 a share against $64.94, the fair price about $31 on equity plus net debt (about $55 on equity alone),
and the cheap price about $5 (none in practice).

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch: **yes** (the template was copied before `tools/run.py` or any EDGAR fetch).
      Written question by question: **in part** (the filings were read before Step 0 was written; Step 0 to Q1 were then
      written, then Q2, then the rest). Committed after each: **no**, the dispatch forbids commits. Left unticked for the
      last two.
- [x] Every v5 id resolves: `Test Runs/_research 2026-10-06 EMN/check_ids.py` checks every M, L and R id against
      `principle_ledger_v5.csv`, no E-id, every id in bold, and every quoted fragment beside an id against that row's text.
      Every filing fact carries its accession or names its filing (whose accession is in Step 0); the XBRL figures for the
      competitor row carry the FY2025 and FY2015 accessions of each filer.
- [x] The order was kept; the first failing STOP (Q2) closed the run; nothing after it is a clearance, and the arithmetic
      after it is headed as a computation.
- [x] Owner cash after every real cost (OCF less stock pay less all capital spending, with the D&A and maintenance variants
      beside it), never a net-income proxy; the sovereign from the US Treasury par curve; the price flagged as an
      aggregator quote.
- [x] Contrary evidence was written down **[M1997-127]**: in the foundations and in Q2 (the downturn comparison, the 2009 and
      2023 tow pricing, AFP, management's ownership).
- [x] No row dated after the anchor: not a point-in-time run; every row cited is dated 2025 or earlier.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py`: PASS on the finished file, 2026-10-06 (Test Runs sweep: phantom ids in 0 files;
      pointers 0 missing). No commit was made, per the dispatch.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2 has no rule for a company of several segments.** Q1 has a by-parts rule for a holding company's understanding, and
the dispatch asked for Q2 "read by parts", but nothing says how parts that disagree (one holding, one narrowing, two priced
by others) add up to one STOP. This run confessed a CONVENTION (the filer's claimed castle tested on the consolidated record,
OUT when it narrows and no part widens); a framework rule is needed. (2) **The Q7 convention's "growth shown" is undefined
when the window starts at a peak and ends at a trough.** Endpoint growth gave a negative equity value; the run showed a
log-linear trend beside it, citing the base-year row, and the convention should say which measure governs. (3) **The fair
price depends on the basis**, $31 on equity plus net debt against $55 on equity alone, a factor near two for a levered
company; the floor convention does not say which, and this run chose the all-equity basis from the acquisition row.
(4) **Working-capital financing**: the owner-cash input does not say whether a growing receivables-factoring programme (here
$150M to $346M outstanding) is stripped from operating cash; this run stripped it. (5) **The template's position note** asks
the analyst to check `PORTFOLIO.md` while the blind rule forbids it; recorded as not checked. (6) **Em dashes**: the
operator-rule-3 heading and several ledger rows contain em dashes, which the dispatch forbids; the heading was written with a
hyphen and the rows were quoted with [...] elisions in place of the dashes. (7) **Q12 and suppliers**: whether selling
cigarette-filter tow to tobacco makers falls under the named business "tobacco" is not settled by the text.
