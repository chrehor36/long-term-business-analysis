# Company Run — Lam Research Corporation (NASDAQ: LRCX) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md` (operator rule 10). Business: wafer fabrication
equipment for etch, deposition and clean, and the Customer Support Business Group (CSBG: spares, service, upgrades and
non-leading-edge "Reliant" tools for the installed base); fiscal year ends late June (FY2026 ended 2026-06-28). No
rename; the one merger of size is Novellus Systems (closed 2012-06-04, all stock); ten-for-one forward split effective
2024-10-02 (8-K accession 0000707549-24-000123).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared before any verdict (seen by accident, not used):** the session context that dispatched me
showed git status and recent commit subjects naming other companies' runs and research folders (AME AMETEK OUT at Q7
on price; ITW and JKHY OUT at Q7 on price; KEYS and KLAC TOO HARD (NATURE) at Q1; research folders for AYI, ARCB, BDC)
and memory-index lines about the queue ("57 gate-clearers, nothing buyable", holding reviews owed, no names). KLAC is a
Lam competitor, so its earlier box could anchor this one; it is declared here and the Q1 verdict below rests only on
Lam's own filings and the v5 rows. The dispatcher's message also says earlier Lam run files exist; none was opened,
listed or searched, and `Test Runs/` was never listed.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $318.84 (close 2026-10-09; `tools/run.py`; an aggregator quote, flagged per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: one class, 1,251,321,000 common shares as of 2026-08-04 (10-K for
  FY2026, filed 2026-08-07, accession `0000707549-26-000037`; `python Screens/cover_shares.py LRCX`). Checked against
  the balance sheet of the same 10-K: "issued and outstanding 1,251,278 shares" (thousands) at 2026-06-28, with
  1,710,109 thousand shares held in treasury at cost, which Lam presents separately (so "issued less treasury" does not
  apply as the brief words it: Lam's tagged issued count already excludes treasury; see the framework notes). No 8-K
  after the 10-K changes the count (8-Ks of 2026-07-29, results, and 2026-08-27, two directors retiring, accessions
  `0000707549-26-000033` and `0000707549-26-000043`). **Split:** ten-for-one forward split effective 2024-10-02 (8-K
  `0000707549-24-000123`); price, cover count and every per-share figure here are on the post-split basis, and the
  XBRL share series before FY2025 is pre-split (diluted 126M in FY2010 is 1,260M post-split).
- **Market cap:** $398,970M (318.84 x 1,251.321M).
- **Sovereign for the earnings currency (USD):** 5.60%, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-09 (`tools/run.py`, which reads `tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2026 (2026-08-07, `0000707549-26-000037`: Item 1, Item 1A, Item 5,
  Item 7, the statements and Notes 9 and 19); the 10-Q for the quarter to 2026-03-29 (2026-04-23,
  `0000707549-26-000022`); the proxy (DEF 14A, 2026-09-24, `0000707549-26-000047`); the 8-Ks above and the earnings
  release (Exhibit 99.1 to `0000707549-26-000033`); for the cycles, the 10-Ks for FY2008 (`0000950134-08-015947`),
  FY2009 (`0001193125-09-182356`), FY2012 (`0001193125-12-365446`), FY2013 (`0001193125-13-348269`), FY2015
  (`0001193125-15-290023`), FY2016 (`0000707549-16-000050`), FY2019 (`0000707549-19-000124`), FY2021
  (`0000707549-21-000136`), FY2023 (`0000707549-23-000102`), FY2024 (`0000707549-24-000106`); the Novellus S-4
  (2012-01-31, `0001193125-12-032338`). Raw copies in `Test Runs/_research 2026-10-10 LRCX/cache/` (ignored).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, FY2026:
  $5,857,657 thousand in the filed cash-flow statement (10-K `0000707549-26-000037`) against $5,858M in the XBRL
  series `tools/run.py` printed. Agrees. Also revenue $23,232,690 thousand against 23,233.
- `python tools/run.py LRCX`, arithmetic lines only (output kept at `_research 2026-10-10 LRCX/runpy_output.txt`).
  Owner cash after every real cost, OCF less stock pay less all capital spending, $M: FY2022 2,295; FY2023 4,391
  (4,271 with the $120M paid for a business deducted, the Q7 default); FY2024 3,963; FY2025 5,071; FY2026 4,505.
  Five-year average 4,045 as `run.py` prints it (4,021 with the acquisition deducted). Capital spending FY2026 $966M
  against depreciation and amortization $442M; stock pay $386M (the only stock-pay line found; no other stock-pay line,
  securities line or finance-lease principal of size: finance-lease principal $5M FY2026). Owner-cash yield at the price
  1.01%, against the sovereign 5.60%.

**The balance sheets, read here because the file closes before Q4** **[M2025-032]** (ten year-ends from `run.py`, first
filed vintage; the FY2026 and FY2025 columns read against the filed balance sheet, `0000707549-26-000037`):
| $M | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|---|---|---|
| equity | 6,502 | 4,674 | 5,172 | 6,027 | 6,278 | 8,210 | 8,539 | 9,862 | 12,471 |
| goodwill | 1,485 | 1,485 | 1,484 | 1,490 | 1,515 | 1,622 | 1,627 | 1,600 | 1,630 |
| cash | 4,512 | 3,658 | 4,915 | 4,418 | 3,522 | 5,337 | 5,848 | 6,391 | 5,579 |
| receivables | 2,177 | 1,456 | 2,097 | 3,026 | 4,314 | 2,823 | 2,519 | 3,378 | 5,340 |
| inventory | 1,876 | 1,540 | 1,900 | 2,689 | 3,966 | 4,816 | 4,218 | 4,308 | 4,276 |
| long-term debt | 1,760 | 3,768 | 4,959 | 4,961 | 4,962 | 4,965 | 4,466 | 3,720 | 3,722 |
| retained earnings | 8,261 | 9,931 | 11,521 | 14,685 | 18,455 | 22,032 | 24,811 | 28,989 | 34,950 |

What the figures say: retained earnings rose $26.7B in eight years while equity rose $6.0B, because the difference went
out in buybacks (treasury stock at cost $31.6B at 2026-06-28) and dividends; equity fell in FY2019, the year debt was
raised from $1.8B to $3.8B and $3.8B of stock was bought, so the buyback was partly borrowed. Goodwill is flat at about
$1.5B to $1.6B since the Novellus merger, so the growth was not bought. Inventory more than doubled from FY2018 to FY2023
and has not fallen back in proportion to the FY2024 revenue dip; receivables jumped 58% in FY2026 on revenue up 26%
(days of revenue 84 against 67 a year earlier), and five customers held 20%, 16%, 15%, 11% and 10% of receivables at
2026-06-28 (Note 9). Debt is long: the $3.75B of notes outstanding run to 2029, 2030, 2049, 2050 and 2060 (10-K Item 7A
and the XBRL members), after the $750M 2026 notes were repaid in March 2026; the company is net cash by $1.8B. What they
cannot say: anything about the next cycle. This reading is written here because Q4 is NOT REACHED.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own Lam "if the market closed for five years"
**[M1997-109]**, and the owner cash the business itself throws off is about 1% of the price, against 5.60% on the bond.
The market serves and does not instruct **[M2006-077]**: the 10-K's own table shows $100 in Lam on 2021-06-25 worth
$633.13 on 2026-06-28 (Item 5, `0000707549-26-000037`), and a price that has risen is no evidence of value. No macro
forecast enters **[M2000-094]**: the filer's own case for the next years is an industry forecast ("the AI market
driving higher semiconductor industry spending", 10-K Item 7), and that forecast is the kind that may not be used. Margin
of safety **[M1996-084]**: whatever the questions find, a decision that needs pencil and paper is too close.
**Contrary evidence, written down as found** **[M1997-127]**: against the Q1 verdict below, the filings show (1) gross
margin held between 39% and 51% in every year FY2010 to FY2026 while revenue ran from $2.1B to $23.2B; (2) the FY2008
10-K names the same two primary etch rivals, Tokyo Electron and Applied Materials, that the FY2026 10-K names beside
Hitachi, so the etch field's leaders did not change in eighteen years (deposition came with Novellus in 2012); (3) the
installed-base revenue (CSBG) was 33% to 40% of revenue FY2019 to FY2026 and fell in only one of those years (FY2024,
down 11%); (4) the filer describes qualification lock-in: once a chipmaker qualifies a tool "the manufacturer generally
maintains that selection for that specific production application and technology node" (10-K FY2026, Competition).
These say the castle has stood. They are weighed at Q1 against the question Q1 asks, which is not whether it has stood.

## THE STANDING RULE
Owning this with the buyer's own money, unlevered, puts no one at risk of ruin; the rule binds the buyer's financing and
sizing, not the target **[M2012-081]**, **[L2014-005]**. Nothing here licenses borrowed money to own it.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The question.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. Knowing what the
product does is not the test; "What is important is that I understand the economic dynamics of the industry"
**[M2011-014]**. I can say what an etch chamber does. The test is whether I can print "the next 10 years of Value Line"
in my head **[M1999-132]**.

**Test 2, the key variables and how predictable they are** **[M1998-044]**:
1. **The industry's equipment spending.** Lam's revenue was $2,567M in FY2007, $1,116M in FY2009 (down 57%, operating
   margin from 30.3% to minus 25.2%), $2,665M in FY2012, $9,654M in FY2019 after $11,077M in FY2018, $14,905M in FY2024
   after $17,429M in FY2023, and $23,233M in FY2026 (10-Ks FY2008, FY2009, FY2012, FY2019, FY2024, FY2026; selected
   data and statements). The filer says customer decisions on capital spending "could change rapidly and be impacted by
   factors outside of our control" (10-K FY2026, Item 1A). Not predictable over ten years.
2. **Lam's share of etch and deposition at each new node.** The share is re-won at every node and every application,
   by qualification. The filer: "The market for semiconductor capital equipment is characterized by rapid technological
   change and product innovation" (Item 1, Research and Development); competitors "may adapt more quickly to new
   technologies" (Item 1A); and "Should technologies change so that the manufacture of semiconductors requires fewer
   steps using our products, this could have a larger impact on our business than it would on the business of our less
   concentrated competitors" (Item 1A). The product families named in the FY2026 10-K (cryogenic dielectric etch for
   3D NAND, gate-all-around selective etch, molybdenum fill, dry EUV resist, HBM packaging) are themselves the record of
   how fast the served applications turn over. Not predictable over ten years.
3. **The customer mix.** Memory took 36% of systems shipments in FY2013, 60% in FY2014, 68% in FY2016, 70% of systems
   revenue in FY2019, 42% in FY2023 to FY2025 and 39% in FY2026; foundry 54% in FY2026 (10-Ks FY2015, FY2016, FY2019,
   FY2023, FY2026). Four customers took 16%, 15%, 12% and 12% of FY2026 revenue (Note 19), and the names changed over
   the span (Samsung and Toshiba at 19% and 13% in FY2008; Micron, Samsung, SK hynix and TSMC named in FY2026).
4. **China.** 9% of revenue in FY2013, 22% in FY2019, 35% in FY2021, 42% in FY2024, 34% in FY2026 (26% in the June 2026
   quarter, Exhibit 99.1), under US export rules whose "implementation, interpretation, and impact on our business ...
   is uncertain and evolving" (Item 1A), with the filer naming state-backed rivals not subject to the rules.

**Test 3, do the past statements tell me the future ones** **[M2008-033]**: no. The FY2009 statements would have told
nothing of FY2026; the customer mix flipped twice, China's share quadrupled, the revenue base grew twentyfold.
**Test 5, would the insiders write it down** **[M2000-105]**: the filer gives one quarter of guidance (Exhibit 99.1:
the September 2026 quarter) and describes its own industry as one of rapid change; the ten-year forecast of Lam's share
of a market whose technology and whose largest customer country are both in motion is the forecast its insiders would
not put on paper. **Test 6, can I name the winner and not just the industry** **[M2012-067]**: the growth is visible
and the filer believes in it; "Just because Charlie and I can clearly see dramatic growth ahead for an industry does
not mean we can judge what its profit margins and returns on capital will be" **[L2009-005]**. **Test 7, customers or
technology** **[M2017-019]**: technology; the buyers are a handful of chipmakers choosing tools on "process
performance, productivity, defect control, customer support, and overall cost of ownership" (Item 1, Competition).
**Test 8, how far off could I be** **[M2011-084]**: far. Owner cash averaged about $1.1B a year over FY2013 to FY2018 and
about $3.0B over FY2019 to FY2023 (computed from the XBRL series, research folder); the ten-year forecast spans
multiples, not a band. **Test 9, do I doubt it is inside** **[M2002-092]**: yes, and "if you have doubts about something
being into your circle of competence, it isn’t."

**The contrary evidence** written under the foundations (the stable gross margin, the unchanged etch rivals, the
installed base, the qualification lock-in) is real, and it is a record of the past. Q1 asks for the fix
on "the earning power and competitive position" ten years out **[M2012-065]**, and the filer's own description of the
industry puts that out of reach.

**Routing.** "if something comes in where there’s a technological component that’s of significance, or where we think
the future technology could hurt the business as it presently exists, ... it won’t make it through the filter"
**[M1998-008]**; "a business that must deal with fast-moving technology is not going to lend itself to reliable
evaluations of its long-term economics" **[L1993-023]**; "whenever we look at a business and we see lots of change coming,
9 times out of 10, we’re going to pass on that" **[M1999-063]**. The framework's fixed routing sends this case to TOO
HARD at Q1, never OUT on the business: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a
fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**; the boxes are "in, out,
and too hard" **[M2006-013]**.

**The cause.** NATURE, not WORK. The deciding question (Lam's share and earning power across the next nodes, the size
of its customers' spending, and its access to China) is important and, from where an outside analyst stands,
unknowable **[M2006-076]**; it is a forecast the industry's insiders would not write down **[M2000-105]**; and the rows
say study does not cure it: "in other cases the nature of the industry would be the roadblock" **[L1993-023]**; "Our
problem -- which we can't solve by studying up -- is that we have no insights into which participants in the tech field
possess a truly durable competitive advantage." **[L1999-018]**. More reading of Lam's filings would add facts about the
past, which this run already has; it would not make the ten-year forecast knowable.

- **VERDICT: TOO HARD (NATURE).** The ten-year economics depend on technology turnover the filer itself calls rapid, on
  a customer mix and a China share that have each moved by multiples inside the span read, and on government rules the
  filer calls uncertain and evolving (10-K FY2026, `0000707549-26-000037`). The file closes here.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED.
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read at Step 0).
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (the reporting figures are computed below as COMPUTATION, NOT A CLEARANCE).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the ten-year earning power and competitive position cannot be foreseen in an
industry the filer itself calls one of "rapid technological change", with a customer mix, a China share and export
rules that have each moved by multiples inside the span read **[L1993-023]**, **[M2000-105]**, **[L1999-018]**; no
research pass is opened, and a lower price does not reopen it **[M2000-038]**. *Integrity facts recorded, not judged*
(the 2007-2008 stock-option review and restatement, under Q5 below). Reporting figures, COMPUTATION, NOT A CLEARANCE:
value range $64.83 to $232.99 a share (all-equity, central) against $318.84; fair price $74.86.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged, operator rule 2 **[M1997-127]**.)*

**For Q2 (the castle).**
- *The competitor row, from the rivals' own filings over the whole span* (SEC XBRL companyfacts, newest vintage, each
  company's 10-K or 20-F; table `_research 2026-10-10 LRCX/competitor_table.csv`, script `comp.py`):

| filer (form, fiscal year end) | years | gross margin, low to high | operating margin, low to high | R&D / revenue | last year revenue |
|---|---|---|---|---|---|
| Lam (10-K, June) | FY2009-FY2026 | 34.8% (FY2009) to 50.5% (FY2026) | -25.2% (FY2009) to 35.3% (FY2026) | 9.3% to 25.8% | $23,233M |
| Applied Materials (10-K, October) | FY2007-FY2025 | 28.5% (FY2009) to 48.7% (FY2025) | -7.9% (FY2009) to 30.2% (FY2022) | 10.6% to 18.6% | $28,368M |
| KLA (10-K, June) | FY2009-FY2026 | 43.1% (FY2009) to 64.2% (FY2018) | -38.0% (FY2009) to 41.7% (FY2026) | 11.2% to 24.4% | $13,579M |
| ASML (**20-F, flagged: IFRS, euros**, December) | 2009-2025 | 28.7% (2009) to 52.8% (2025) | -10.2% (2009) to 36.3% (2021) | 10.4% to 18.3% (2015-16 not tagged) | EUR 32,667M |
| Tokyo Electron | none | **not an SEC filer, flagged; no filing read** | | | |

  Lam's operating margin was 3.3% in FY2013 and 8.9% in FY2012, the Novellus years (amortization and integration);
  29.0% in FY2018, 25.5% in FY2019, 29.7% in FY2023, 28.6% in FY2024 (the two recent dips were shallow: revenue down 13%
  and 15%), against minus 25.2% in FY2009 on revenue down 57%. Lam's operating margin was above Applied Materials' in
  every year matched from FY2018 to FY2025 except FY2024 (28.6% against 28.9%), and below KLA's in every year from
  FY2011 (above it in FY2009 and FY2010).
- *The field's returns.* All four filers earned operating margins in the 20s and 30s through FY2019-FY2025 and losses or
  thin margins in 2009 and 2012-2013 (table above); whether the last cycle's returns are the field's durable level or a
  change for the better not yet tested by a full cycle is the question Q2 would have had to answer (section C).
- *The filer on the attackers:* primary competitors named as Applied Materials, Hitachi and Tokyo Electron in etch;
  Applied Materials, ASM International and Wonik IPS in deposition; Screen, Semes and Tokyo Electron in wet clean; and
  "competitors, including those that are created and financially backed by foreign governments", competitors not
  bound by US export rules, and customers' own affiliated equipment makers (10-K FY2026, Item 1 and Item 1A).
- *Qualification lock-in* in the filer's words (Item 1, Competition), quoted under the foundations.

**For Q3 (capital).** Operating income after the year's effective tax against tangible capital employed (equity plus
debt less cash less goodwill and intangibles; a capital test of earnings after depreciation against capital employed):
70% FY2019, 78% FY2022, 63% FY2024, 83% FY2026 (computed from the filed statements; script output in this run's
working notes). Capital spending $966M in FY2026 against depreciation and amortization $442M; the filer ties the rise to
"lab investments in the United States and global growth in manufacturing facilities" (Item 7). R&D 10.2% of revenue in
FY2026, 9.3% to 19.0% FY2010-FY2026 and 25.8% in FY2009 (the trough year, when it was cut least).

**For Q4 (the accounts).** The earnings releases feature non-GAAP figures beside GAAP (Exhibit 99.1 to
`0000707549-26-000033`); the non-GAAP adjustments are small (acquired-intangible amortization, deferred-compensation
marks, note discount, workforce charges) and do not remove stock pay. Quarterly guidance is given for revenue, margins
and diluted EPS ($8.10B plus or minus $400M for the September 2026 quarter). A restructuring of FY2023-FY2024 cost
$181.9M cumulative (Note 20). FY2026 receivables up $1.96B, which the filer names as the main reason operating cash fell
while net income rose (Item 7).

**For Q5 (who runs it). INTEGRITY FACTS, RECORDED, NOT JUDGED.** The FY2008 10-K (`0000950134-08-015947`) records a
review by an independent committee of the board of "our historical stock option practices", a restatement that
recorded "additional non-cash, stock-based compensation expense of $95.2 million in the aggregate for the periods from
fiscal 1997 to fiscal 2006", "misdated stock options", remedial payments to make "employees including our Chief
Executive Officer and other affected executive officers, whole" for tax liabilities "approximately $50 million as of June
29, 2008", and a risk factor headed "We Recently Regained Compliance with SEC Reporting Requirements" (the FY2007 10-K
was filed 2008-03-31). The present chief executive, Timothy Archer, has held the post since December 2018 and joined Lam
from Novellus in June 2012 (DEF 14A 2026); whether any officer or director of 2006-2008 remains was not checked. Any later
run that reaches Q5 must answer these facts **[M2013-088]**. Also recorded: the quarterly guidance habit (Q4 above),
carried for Q5 as the framework directs.

**For Q6 (the money and the owners).**
- *Buybacks.* $30.5B of treasury purchases FY2009-FY2026 (XBRL, TreasuryStockValueAcquiredCostMethod, sum of years;
  includes net share settlement); $3.85B in FY2026 at quarterly average prices of $105.67, $153.62 and $210.57, then
  $287.93 and $370.15 in the two months of the last quarter, with accelerated repurchases at $91.00 (April 2025) and
  $270.71 (March 2026) (10-K FY2026, Item 5). The programme: $10.00B authorized May 2024, "no termination date", no
  price named (Item 5). Every FY2026 purchase price sits above the bottom of the computed central range ($64.83), so the
  no-stated-price test of Q6 would have weighed against (computation only). The FY2019 buyback ($3.78B) was made in the
  year debt rose by $2.0B.
- *Share count.* Diluted shares (post-split basis) about 1,250M to 1,280M in FY2010-FY2012, 1,730M in FY2013 after the
  merger, 1,261M in FY2026: fourteen years of buybacks took the count back to about where it stood before Novellus.
- *Novellus (2012).* All stock: 82,689 thousand Lam shares (pre-split) at $35.99, consideration $3,027M including
  assumed awards (10-K FY2012, `0001193125-12-365446`); exchange ratio 1.125, a premium of 28.0% to the prior day's price
  ratio (Goldman Sachs analysis in the S-4, `0001193125-12-032338`); announced alongside an intent to "return up to $1.6
  billion" by repurchase within twelve months of closing (S-4). Novellus brought $419M of cash and $641M of short-term
  investments. Whether Lam's stock was below its intrinsic value when it was issued, the question the Q6 STOP asks
  **[L2009-019]**, was not answered.
- *Dividends* since April 2014; $1,271M in FY2026 ($0.26 a quarter); about $8.1B paid FY2015-FY2026 (XBRL sum).
- *Stock pay* $386M in FY2026 (1.7% of revenue; about 8% of five-year average owner cash).
- *Pay.* CEO total compensation FY2026 $40,354,475; pay ratio 500 to 1; annual incentive on non-GAAP operating margin;
  long-term awards in market-based PRSUs measured by relative total shareholder return against the members of the
  Philadelphia Semiconductor index, plus service-based RSUs; separate, independent chair; clawback; ownership
  guidelines (DEF 14A 2026, `0000707549-26-000047`). Ten-for-one split effected by charter amendment without a
  stockholder vote (8-K `0000707549-24-000123`).

**For Q7 (value): the reporting figures, COMPUTATION, NOT A CLEARANCE.** Built by Q7's construction (CONVENTION, the
framework's), script `value_range.py`, output `value_range_output.txt`. Inputs: owner cash = operating cash less stock
pay less capital spending less cash paid for businesses ($120M FY2023), FY2022-FY2026 (the literal window; the filer
describes no end year as aberrational, and the cycle base is shown beside); growth measured on aggregate owner cash,
first to last year; ten years at that growth, then zero nominal growth; discounted at 5.60%. Specific (e): the filer ties
the capital-spending rise to growth, so the bottom of the range is no growth on owner cash after maintenance only
(depreciation as the maintenance guess **[M1998-127]**), and the top is the shown growth with all spending charged.
Net cash $1,844.6M at 2026-06-28 (debt and finance leases $3,734.6M less cash $5,579.2M; operating leases left out);
shares 1,251.321M.

| basis | bottom | top | width (whole business) | fair price |
|---|---|---|---|---|
| **all-equity, central** (owner cash before interest, after the company's tax; plus net cash) | **$64.83** (avg $4,440M, no growth) | **$232.99** (avg $4,179M, growth 17.2%) | 3.65 to 1 | **$74.86** |
| equity-only, beside (owner cash after interest) | $61.11 | $243.20 (growth 18.4%) | 3.98 to 1 | $75.15 |
| all spending at both ends, all-equity (beside) | $61.10 | $232.99 | 3.88 to 1 | $73.81 |
| cycle base, all-equity (beside): FY2019-FY2023 average $2,956M, growth 19.3% a year between the FY2013-FY2018 and FY2019-FY2023 cycle averages | $43.65 | $193.28 | 4.55 to 1 | $58.81 |

Price $318.84. The fair price is the present value at the ten-percent floor of the midpoint cash stream (the average of
the two ends' streams, which by linearity is the average of the two ends valued at ten percent), after the company's own
tax, plus net cash, per share (CONVENTION of this run, the reading of the reporting convention's words; rationale: the
reporting convention names the midpoint and the floor but not whether the midpoint is a value or a stream; the stream
reading is the one that gives a price at which the buyer's expected return is the floor). Read as Q7 would read them, if
it had been reached: the range is wider than three to one, which is Q7's TOO HARD, and the price is above the top of the
range, which is Q7's OUT through the floor; the owner-cash yield at the price is about 1.0% to 1.1% against 5.60% on the
bond. None of this is a verdict or entry language (operator rule 3).

**For Q9 (debt).** Fixed-rate notes of $3.75B principal maturing 2029, 2030, 2049, 2050 and 2060 (fair value $3.16B),
commercial paper capacity $2.00B with none outstanding at 2026-06-28, net cash $1.8B (10-K FY2026, Item 7 and 7A).
Customer credit concentrated: five customers 72% of receivables at 2026-06-28 (Note 9).

**For Q12.** Semiconductor equipment is not among the businesses the rows name; not reached.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before `run.py` or any EDGAR call). Written
      question by question. **Committed after each question: not as the brief intends.** The first commit (Step 0 to
      Q1) was blocked by `.git/index.lock`, created 10:35:25 and unchanged at 10:41 with no git process running; ten
      tries thirty seconds apart failed; I did not delete it (the brief), and by 10:43 it had been replaced by another
      writer's fresh lock. The AFTER THE STOP section, the box and this audit were written while that first commit was
      pending, so Step 0 to Q1 and the closing sections land together in one commit; the Q1 text is as first written,
      except three factual lines corrected before any commit (the etch-rivals line, the margin comparisons, a
      framework-wording quote the citation check caught).
- [x] Dispatched: the brief allowed per-question commits; the lock in `Screens/_daily/` is the dispatcher's (not
      checked by me). The fold is the dispatcher's; a run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; `Test Runs/` was never listed.
      What was seen by accident (commit subjects and folder names of other runs, memory-index lines) is declared under
      CONTAMINATION at the top and was not used.
- [x] Every v5 id resolves (checked by `_research 2026-10-10 LRCX/check_citations.py`: no E-ids, every M/L/R id in the
      CSV, every quoted fragment standing before an id found in that row); every filing fact has its accession.
- [x] The order was kept; Q1's STOP closed the run; everything after it is under AFTER THE STOP or headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay deducted, all capital spending and acquisitions deducted), never a
      net-income proxy; the sovereign from the US Treasury curve; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (under the foundations, and weighed at Q1); integrity facts under Q5 above
      with the flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the commit attempt (output in the research folder); run again before
      the final commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 sends the same business two ways.** Its "rules OUT" list holds the business that lives on continued invention,
on the row "if they had never invented any more pharmaceuticals, it would be a terrible business" **[M1999-075]**, and
Lam is one (R&D 9% to 26% of revenue every year; each node re-won), while the fixed routing sends
"fast-moving technology" to TOO HARD, "never OUT on the business". I followed the routing, because the reason found here
is ignorance of the ten-year economics, not a finding against them; the text should say which governs when both fit.
(2) **The cycle base.** Specific (a) makes a window year aberrational only "on the filer's own description of it". Lam
describes its whole industry as cyclical and no single year as a peak, so the literal window governs although FY2026 is
a record year in a filer-described upswing; the rule cannot see a cycle the filer describes only in general. I showed the
cycle base beside. (3) **The fair price** is defined as the price at which "the midpoint of the range earns the floor";
whether the midpoint is a value or a cash stream is not said, and the two readings give different numbers; I used the
stream (confessed above). (4) **Specific (e)** does not say how the two ends pair when the maintenance-only case is
central; I paired no growth after maintenance with the shown growth after all spending, which is the only pairing I
found that charges the growth spending against the growth it buys without charging it twice. (5) **A business of parts**
(Q2, section B) reaches operating segments with different economics; Lam reports one segment and discloses the
installed-base revenue (CSBG, 33% to 40%) only as revenue, without profit, so the parts rule cannot be applied to the one
part that might have been foreseeable. (6) **The brief's share check** says to check the cover count "against issued
shares less treasury shares"; Lam's balance sheet states "issued and outstanding" shares with treasury shown apart, and
`tools/run.py` labels the tagged issued count "includes treasury" when for this filer it does not; read literally, issued
less treasury is negative. (7) **The lock rule** (wait thirty seconds, ten tries, never delete) has no path for a stale
lock left by a dead process during a dispatched run; the analyst can only stop committing.
