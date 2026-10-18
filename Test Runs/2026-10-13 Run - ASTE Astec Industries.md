# Company Run: Astec Industries, Inc. (Nasdaq: ASTE), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run (operator rule 10). The template was copied to this file and committed (d7f15c94) before any fetch.
The brief departs from the canonical brief in one stated place: the lines of evidence and the competitors were not
hand-written by the dispatcher; this analyst derived them from the FY2025 10-K (Items 1, 1A and 7) and names them below.*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (ASTE; also searched for Astec); not held.*

**CONTAMINATION DECLARED (the blind rule).** Seen by accident, not used: (1) a directory listing of `Test Runs/` filtered
to today's date, made only to confirm this run's file name was free, showed the file and folder names of thirteen other
runs dated 2026-10-13 (GRFXY, HDSN, HRIBF, JCSE, KIGRY, LHSW, LZ, MSM, SIEGY, SITE, SQFT, TPICQ, VELO), none about this
company; (2) the session's opening context showed the last five commit subjects (the VELO run and its fold) and
untracked research-folder names for AYI and ARCB; (3) the memory index lines name the queue state in general terms
(wave counts, "57 gate-clearers, nothing buyable") and say nothing about this company. No file about ASTE under any
name was opened, listed or searched; no file listed in the blind rule was opened.

**LINES OF EVIDENCE, chosen from the FY2025 10-K (the brief's departure).** From Item 1: the two segments
(Infrastructure Solutions; Materials Solutions) and their named rivals; the parts business ("an integral part of our
business"); backlog; steel as the main input. From Item 1A: cyclical demand tied to government highway funding (the IIJA,
whose five-year period ends in 2026); competition from larger rivals; steel prices and tariffs; the TerraSource
integration; indebtedness under the 2025 credit facilities; the ERP programme. From Item 7: segment sales and Segment
Operating Adjusted EBITDA; pricing against cost ("competition limits our ability to pass through cost increases in many
cases"); the transformation-programme cost; working capital (inventory, receivable days); the two acquisitions
(TerraSource 2025, CWMF 2026) and their goodwill; debt, interest and covenants. Read beside them: stock pay, buybacks
and their amounts, litigation (Note 16), the 2018 material weaknesses and pellet-plant losses (FY2018 10-K), the proxy's
pay metrics.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $39.48 (close 2026-10-12, as printed by `tools/run.py`; **aggregator quote, live price only, flagged under
  operator rule 5**).
- **Shares by class** from the latest filing's cover: one class, common stock, **23,025,367** shares (10-Q for the
  quarter ended 2026-06-30, filed 2026-08-05, accession `0000792987-26-000044`, cover as of 2026-07-31;
  `python Screens/cover_shares.py ASTE`). Check: the 10-Q balance sheet shows 22,994,624 shares issued and outstanding
  at 2026-06-30 and no treasury stock (the company holds a few shares only inside its deferred compensation programmes,
  $0.2M at cost); the difference to the cover is vesting in July. The 8-Ks filed after the 10-Q (2026-08-05, Item 2.02
  results; 2026-07-30, Item 5.02, a director appointed) issue no shares. No preferred stock is issued.
- **Market cap:** 23.025M x $39.48 = **$909.0M**.
- **Sovereign for the earnings currency:** USD, US Treasury daily par yield curve, 30-year, **5.60%**, dated
  2026-10-09 (`python tools/sources.py`, issuing authority; 2026-10-12 was a bond-market holiday).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-25, accession `0000792987-26-000011` (Items 1, 1A, 3, 5, 7, 7A, 8 with Notes 3, 7,
    16, 17, 19 and 21, 9A).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-08-05, accession `0000792987-26-000044` (balance sheet,
    operations, cash flows, the CWMF note, liquidity).
  - Proxy (DEF 14A) filed 2026-03-13, accession `0001104659-26-027745` (Summary Compensation Table, incentive metrics,
    the 2023 PSU outcome, board independence).
  - 10-K for FY2022, filed 2023-03-01, accession `0000792987-23-000015` (segment results for 2021 and 2022 as revised
    to the present two segments; the GEFCO suit).
  - 10-K for FY2018, filed 2019-03-18, accession `0000792987-19-000019` (the material weaknesses; the wood pellet
    plant losses and company-financed sales).
  - 8-Ks: 2026-07-30 (`0000792987-26-000036`, Item 5.02, a director appointed) and 2026-04-20
    (`0000792987-26-000016`, Item 5.02, the Group President of Infrastructure Solutions left and was replaced). The
    other recent 8-Ks were read from the EDGAR index by item code only (results releases under Item 2.02; the
    TerraSource 8-K of 2025-07-01, `0001104659-25-064747`, whose facts were taken from Note 3 of the FY2025 10-K).
  - XBRL company facts (data.sec.gov) for the ten-year series, first-filed values, transcription only.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for FY2025,
  $61.4M on the filed Consolidated Statement of Cash Flows (10-K `0000792987-26-000011`), equal to the XBRL value and to
  the `tools/run.py` line. Also checked: FY2025 shareholders' equity $681.7M, goodwill $111.8M and inventories $466.0M
  on the filed balance sheet against the ten-year table below.
- `python tools/run.py ASTE` arithmetic lines only (saved as `Test Runs/_research 2026-10-13 ASTE/run_py_output.txt`),
  extended to ten years by `Test Runs/_research 2026-10-13 ASTE/calc.py` from the filed figures (output in
  `Test Runs/_research 2026-10-13 ASTE/calc_output.txt`). Owner cash = operating cash as filed less stock pay less
  capital spending (USD millions):

| FY | Op. cash | Stock pay | Capex | Owner cash (equity-only) | after-tax interest added back (all-equity) | D&A | Acquisitions paid |
|---|---|---|---|---|---|---|---|
| 2016 | 134.8 | 2.9 | 27.4 | 104.5 | 105.5 | 24.8 | 39.8 |
| 2017 | 41.9 | 3.1 | 20.0 | 18.8 | 19.2 | 25.8 | 26.4 |
| 2018 | -29.8 | 2.2 | 27.4 | -59.4 | -58.7 | 27.9 | 0.0 |
| 2019 | 112.4 | 2.6 | 23.4 | 86.4 | 87.7 | 26.2 | 0.0 |
| 2020 | 141.5 | 5.1 | 15.4 | 121.0 | 121.2 | 26.9 | 32.5 |
| 2021 | 7.4 | 6.0 | 20.1 | -18.7 | -18.5 | 30.2 | -0.1 |
| 2022 | -73.9 | 6.8 | 40.7 | -121.4 | -120.6 | 27.9 | 17.8 |
| 2023 | 27.8 | 4.1 | 34.1 | -10.4 | -5.3 | 25.6 | 0.0 |
| 2024 | 23.0 | 5.0 | 20.5 | -2.5 | 3.7 | 26.8 | 0.0 |
| 2025 | 61.4 | 7.1 | 40.7 | 13.6 | 25.4 | 36.3 | 248.7 |

  Five-year mean 2021-2025: **-27.9** equity-only, -23.1 all-equity (interest paid added back at the filer's 2025
  effective tax rate of 26.9%, CONVENTION of this run: the filer's own stated rate; rationale: the template asks for
  owner cash before interest and the filer states one rate for its most recent year), -26.0 on the D&A basis. Ten-year
  mean 2016-2025: 13.2 equity-only, 16.0 all-equity. Stock pay is resolved and complete: one line, share-based
  compensation; `tools/run.py` found no other stock-pay line, no securities inside operating cash beyond the small
  trading-securities line (-0.2 to -1.5 a year, left in), no finance leases (the 10-K says the company had none at the
  end of 2025 and 2024), no paid-in-kind interest. The D&A tag covers depreciation and amortization together; it is not
  intangible amortization alone. Proceeds from selling property (17.7 in 2020, 20.3 in 2023) are not netted against
  capex in the table; netting them moves the five-year mean to -21.7.

### The balance sheets, eight to ten years, read here because the file closes before Q4 **[M2025-032]**
Ten year-ends from `tools/run.py` (first-filed XBRL, transcription; FY2025 and FY2024 checked against the filed balance
sheet in `0000792987-26-000011`; USD millions):

| Year-end | Assets | Equity | Cash | Receivables | Inventory | Goodwill | Intangibles | Debt on the face | Retained earnings | Sales (year) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 844 | 648 | 82 | 107 | 360 | 41 | 27 | 11 | 537 | 1,147 |
| 2017 | 890 | 686 | 62 | 115 | 391 | 46 | 31 | 4 | 565 | 1,185 |
| 2018 | 855 | 585 | 26 | 131 | 356 | 33 | 25 | 60 | 495 | 1,172 |
| 2019 | 800 | 602 | 49 | 120 | 295 | 33 | 24 | 2 | 508 | 1,170 |
| 2020 | 848 | 642 | 159 | 116 | 250 | 39 | 31 | 2 | 545 | 1,024 |
| 2021 | 911 | 654 | 134 | 144 | 303 | 39 | 23 | 3 | 553 | 1,097 |
| 2022 | 1,014 | 627 | 66 | 167 | 393 | 45 | 22 | 88 | 528 | 1,275 |
| 2023 | 1,059 | 653 | 63 | 153 | 456 | 46 | 16 | 83 | 549 | 1,338 |
| 2024 | 1,044 | 638 | 91 | 167 | 423 | 25 | 11 | 118 | 542 | 1,305 |
| 2025 | 1,367 | 682 | 72 | 219 | 466 | 112 | 125 | 348 | 568 | 1,410 |

What the figures say. (1) **The owners' stake did not grow.** Equity moved from 648 to 682 in nine years and retained
earnings from 537 to 568; the sum of reported net income over 2016 to 2025 is $196.1M (55.2, 37.8, -60.4, 22.3, 46.9,
17.8, -0.1, 33.5, 4.3, 38.8), about 3% a year on equity, and dividends of about $10M a year (total $104.9M over the ten
years) and two buybacks ($24.1M in 2018, $10.1M in 2022) took most of it. (2) **Inventory is the business's largest asset and it moves with
the cycle, not with sales.** It was 31% of sales in 2016, fell to 24% in 2020 as the company released it, and rose to
33% in 2025 (466 on 1,410); the swing is what turned owner cash from +121 in 2020 to -121 in 2022, when inventory rose
by about $90M (operating cash -73.9). Receivable days rose from 40.3 to 47.8 in 2025 (Item 7). (3) **Debt arrived in
2022 and jumped in 2025.** Debt on the face was near zero from 2019 to 2021, 88 in 2022, and 348 at the end of 2025
after the TerraSource purchase was financed with a term loan; at 2026-06-30 the borrowings are $393.4M (10-Q). (4)
**Goodwill and intangibles were small until 2025** (68 at the end of 2016, 36 at the end of 2024 after the 2024
write-off) and are $236.3M at the end of 2025 and $271.7M at 2026-06-30, now about two fifths of equity, nearly all from the two
purchases of 2025 and 2026. What the figures cannot say: the price at which the company sells against its rivals, or
whether the 2023 to 2025 rise in gross margin (22.9% in 2021, 20.7% in 2022, 24.7%, 25.1%, 26.5%) will hold through a
downturn; no downturn has been filed since it began.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own it "if the market closed for five years"
**[M1997-109]**, so the work below is on the business, its castle and its cash, and the quotation is used only as the
price **[M2006-077]**. No macro forecast enters **[M2000-094]**: the end of the IIJA's five-year period in 2026 and any
reauthorization are recorded as the filer states them and are not forecast. The margin of safety is an attitude here and
an arithmetic at Q7 **[M1996-084]**. Who is paid to tell you: the filer's chosen measure of segment profit, and of its
own pay, is an adjusted EBITDA (Item 7; the proxy), which is read but not taken as earnings. The analyst's habits: look
for "what’s wrong in things" and "what you’re missing" **[M2025-013]**, and keep the scuttlebutt aimed "to possibly reject
your original hypothesis" **[M1998-144]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) shareholders' equity was $648M at the end of 2016 and $682M at the end of 2025, and retained earnings $537M and
$568M, so nine years of reported profit, net of about $10M to $12M of dividends a year, left the owners' stake nearly
where it was (ten-year balance sheets, read under Step 0 below because the file closes before Q4); (2) the filer writes that "competition limits our ability to pass
through cost increases in many cases" (FY2025 10-K, Item 7); (3) owner cash was negative in four of the last five years;
(4) the whole goodwill of the Materials Solutions reporting unit ($20.2M) was written off in 2024 (Note 7); (5) the
five-year cumulative return to holders was 79.28 against 200.50 for the S&P 600 SmallCap Industrials (Item 5
performance graph, base 100 at 2020-12-31). Evidence for the business, written down as found as well: the segment
measure rose every year 2023 to 2025 in Infrastructure Solutions; backlog rose to $514.1M at 2025-12-31 from $419.6M;
the filer sells "replacement parts for some competitors' equipment" and calls parts "an integral part of our business".

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase of a quoted minority stake with the buyer's own money, unlevered,
sized so that a fall of half in the quotation forces no sale, risks nothing the buyer has and needs **[M2012-081]**;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing about this name requires the buyer to
borrow, give collateral or accept a call. The rule is satisfied on the buyer's side; the target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test, applied to the filings.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
  The product need not be mastered if "the economic dynamics of the industry" are understood **[M2011-014]**.
- **What the business is** (FY2025 10-K, Item 1): steel fabrication and assembly of equipment for every step of road
  building (asphalt and concrete plants, pavers, milling machines, material transfer vehicles; crushers, screens,
  washing plants, conveyors), plus wood chippers and grinders, burners and heaters, plant controls, and the replacement
  parts for all of them, sold to asphalt and concrete producers, contractors, quarries and mines, directly and through
  dealers. 80.1% of 2025 sales were domestic. Manufacturing "consist[s] primarily of fabricating steel components and
  the integration of supplier purchased components" (Item 1, Manufacturing).
- **The key variables and how predictable they are** **[M1998-044]**: (1) the volume of road and utility construction,
  which the filer calls "cyclical" and "sensitive to the amount of public sector spending on infrastructure" (Items 1A
  and 7); its level is a macro quantity and is not forecast here, but its *nature* (a cycle around a long-lived need:
  "federal highway funding programs have consistently been in place for several decades", Item 7) is known; (2) steel,
  "a major component of our equipment" (Item 7), whose price the company "may not be able to pass through" in full;
  (3) the company's price and cost against named rivals, readable from their filings. None of the three is a fast-moving
  technology: asphalt drum plants, crushers and pavers are sold today in forms recognisable from the company's 1972
  founding, and the filer's own new products (warm-mix water injection, recycled-asphalt content, telematics) are
  improvements to the same machines, not replacements of them.
- **Would the insiders write the forecast down?** **[M2000-105]** Yes in kind: that asphalt will be produced and laid,
  aggregate crushed and screened, and the machines bought, repaired and supplied with parts in ten years is a forecast
  this industry's participants make in public (the filer and Gencor each describe the same product lines and
  customers; Terex names Astec among its crushing and screening rivals, `0000097216-26-000035`). The earning power it
  implies is low and cyclical; that is a finding about the economics, and it belongs to Q2 and Q3, not a failure to
  foresee them.
- **Can I name the winner, not just the industry?** **[M2012-067]** The question is answered at Q2 from the competitors'
  filings; for Q1 it suffices that the competitive position can be read, and it can (the rivals' margins are filed).
- **The parts that matter** (Q1's holding-company paragraph, reaching operating segments): Infrastructure Solutions
  carries 69% of the five-year segment profit (Q2, the parts table) and decides; it is the asphalt, concrete, paving and
  forestry equipment business described above, inside the perimeter on the same reading. Materials Solutions (crushing
  and screening) is likewise a slow-changing machinery business.
- **Doubt test** **[M2002-092]**: no doubt that the economics are foreseeable in kind; the doubt this run carries is
  about whether they are good, which Q2 asks.
- **VERDICT: IN.** A cyclical, slow-changing machinery and parts business whose economics can be read from its own and
  its rivals' filings **[M2012-065]**, **[M2011-014]**, **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**; and what a castle is for: an enduring "moat" that "protects excellent
returns on invested capital" **[L2007-004]**.

**The parts table** (Q2, a business of parts). The filer reports two segments with different economics. It reports no
segment operating profit, only Segment Operating Adjusted EBITDA, so the shares are measured on that (CONVENTION of
this run: the only segment profit the filings state; rationale: the threshold needs a filed figure, and depreciation by
segment is not filed). 2021-2022 from the FY2022 10-K (`0000792987-23-000015`, segments revised to the present two),
2023-2025 from the FY2025 10-K (`0000792987-26-000011`, Note 19); margins on external sales:

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum | Share | Margin on external sales, five years | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Infrastructure Solutions (asphalt and concrete plants, pavers, milling, forestry, burners, controls) | 73.9 | 73.0 | 102.4 | 121.5 | 134.3 | 505.1 | 69.0% | 12.4% (505.1 on 4,086.0) | **yes** |
| Materials Solutions (crushing, screening, washing, conveying; TerraSource from 2025-07-01) | 39.1 | 44.5 | 50.7 | 37.2 | 55.6 | 227.1 | 31.0% | 9.7% (227.1 on 2,333.3) | no |
| Corporate and Other (parent, captive insurer) | -48.2 | -46.5 | -43.1 | -46.9 | -49.2 | -233.9 | | | |

Both segment figures are *before* depreciation, before the corporate costs above, and before the transformation
(ERP) programme, which the filer reports outside the segments at $29.2M, $32.8M and $19.6M in 2023, 2024 and 2025
(Note 19 reconciliation) and expects to total $180M to $200M by 2028 or 2029 (Item 7). These are costs of running the
two parts ("The parent company and the captive provide support and corporate oversight for our other sites", Item 1),
so the owners' return on the parts is the consolidated one. The file closes on Infrastructure Solutions; Materials
Solutions, which does not decide, is read as well because its rival's figures are filed.

**The castle tests, each with its filing fact.**
1. *The castle questions, key factors and permanence* **[M1995-038]**. The filer's own candidates: breadth of line,
   "our product portfolio enables us to be a singular provider to our customers for both asphalt and concrete
   equipment"; the parts business, sold for its own installed base and "for some competitors' equipment"; brand names
   (Astec, Roadtec, Telsmith, Heatec, Peterson); 117 U.S. patents (Item 1). These are real and old. What they have
   protected is the question, and the ten-year record (below) says: not the owners' returns.
2. *Pricing power and the agony before a rise* **[M2005-020]**. The filer, in its own words: "Whenever possible, we
   attempt to cover increased costs of production by adjusting the prices of our products. The markets we serve are
   competitive in nature, and competition limits our ability to pass through cost increases in many cases" (Item 7,
   Industry and Business Condition), and of steel: "we may not be able to pass through all increases in steel costs to
   our customers" (Item 7). The record agrees: when steel rose in 2021-2022, consolidated gross margin fell to 22.9% and
   20.7% and operating margin to 2.0% and 0.6%. The rows say "over time the businesses with strong competitive positions
   manage to pass through increases in raw material costs" **[M2005-017]**; this one says it cannot, "in many cases".
   The failing answer is the prayer session **[M2005-020]**. Favourable pricing is credited in each of 2023, 2024 and
   2025 (Item 7), after the cost spike, which is the catch-up the row allows for ("temporary situations where,
   sometimes, the costs are increasing faster" **[M2005-017]**); it has not yet been tested by a fall in volume.
3. *The attacker with money* **[M2011-015]**. The attackers are already inside: "Some of our domestic and international
   competitors have greater financial, product development and marketing resources than we have" (Item 1A), and the
   named rivals include Caterpillar Paving Products, the Wirtgen Group (John Deere: Vogele pavers, Benninghoven
   asphalt plants), the Fayat Group (Bomag, Dynapac, Asphalt Drum Mixers, LeeBoy), Metso, Sandvik, Epiroc and Terex
   (Item 1). Imports are significant competition in the United States only in milling machines and track-mounted
   crushers (Item 1, Competition). "one competitor is
   frequently enough to ruin a business" **[M2012-108]**; here several, each larger, sell the same machines.
4. *Unit volume and share of mind*. Sales were $1,147.4M in 2016 and $1,410.4M in 2025, 2.3% a year compounded in
   nominal dollars with acquisitions inside it (purchases in 2016, 2017, 2020 and 2022, and TerraSource's $84.7M in
   2025); international sales fell to 19.9% of the total in 2025 from 22.2%. No filing read states unit volumes.
5. *The low-cost position* **[M2018-043]**, measured against the competitor, not in the absolute **[M2001-013]**:
   "The figures are available." **[M2009-059]** The competitor row below shows Astec's operating margin over the whole
   span at about a quarter of each filing rival's or less, and its Materials segment earning less *before* depreciation and
   central costs (8.0% to 11.1% of external sales) than Terex's Materials Processing segment earns *after* them (11.4%
   to 16.1%). In the deciding part the gap is smaller: Infrastructure Solutions' 12.4% before depreciation, central
   costs and the ERP programme is about what Gencor, the one filing asphalt-plant rival, earns after all of its costs
   (8.8% operating margin 2021-2025, before adding back its depreciation), so Astec's Infrastructure part is not shown
   to be the low-cost producer either; its all-in cost of doing the same business is higher.
6. *The brand in the customer's mind; would the customer still choose it over the low bid.* The filer gives the terms
   of competition in every domestic market as "highly competitive with respect to price, service and product quality"
   (Item 1, Competition). No filing fact shows a customer paying more for the Astec name; the rival Gencor says the same
   of itself, that "its products’ performance reliability, brand recognition, pricing, and after-the-sale technical
   support are other important factors that enable the Company to compete effectively" (`0001193125-25-312742`, Item 1).
7. *Ask the competitors.* Terex names "Astec Industries" first among its Crushing & Screening rivals
   (`0000097216-26-000035`, Item 1). Gencor calls the asphalt-plant industry "fairly concentrated, with a small number of
   companies competing in the markets of the majority of the Company’s product lines" (`0001193125-25-312742`); Astec
   calls both its fields "highly competitive and fragmented" (Item 1). No rival filing read names Astec as the one it
   fears or as the price setter.
8. *Widening or narrowing* **[M1999-108]**, **[M2000-075]**. For the business: segment profit and gross margin rose
   in each year 2023 to 2025 and backlog rose in 2025, under the chief executive appointed in January 2023 (proxy). Against it: the 2024 write-off of all
   Materials goodwill (Note 7, $20.2M, the unit's carrying value exceeded its fair value); the first half of 2026 shows
   operating income of $29.4M on sales of $804.4M, 3.7%, against $41.9M on $659.7M, 6.4%, a year earlier (10-Q
   `0000792987-26-000044`); the Infrastructure group president left in April 2026 (8-K `0000792987-26-000016`).
9. *What could destroy, modify or reduce it* **[M2000-014]**: the filer names highway funding, steel prices and tariffs,
   larger rivals and the ERP programme (Item 1A). None needs forecasting here, since the castle is read on what it has
   already done.

**The competitor row**, same metric from each filer's own filings: operating income divided by net sales, and summed
over the span. Rivals chosen from those the FY2025 10-K names that file with the SEC: Gencor Industries (asphalt plants
and related equipment, fiscal years to September 30; 10-K `0001193125-25-312742` read for its competition and
liquidity text; XBRL company facts for the series), Terex Corporation (its Materials Processing segment, a named rival
of Materials Solutions; segment figures from the 10-Ks `0000097216-23-000012` for 2020-2022 and
`0000097216-26-000035` for 2023-2025, the latter as re-segmented in 2025, flagged), and Alamo Group (owner of Morbark, a
named rival of Infrastructure Solutions in forestry; consolidated, a broader business; XBRL company facts only, its
10-K `0000897077-26-000016` not opened). Caterpillar and Deere file but do not report their road-equipment lines apart,
so were not chosen. **Named rivals that do not file with the SEC** (private or foreign): Fayat Group (Bomag, Dynapac,
Asphalt Drum Mixers, LeeBoy), Ammann Group, the Wirtgen Group's own figures (inside Deere), Metso, Sandvik, Epiroc,
FLSmidth, The Weir Group, Tigercat, Bandit, ALmix, Stephens, Vince Hagan, ERIE Strayer, CMI Roadbuilding, Diamond Z,
Doppstadt, Weiler, EDGE Innovate, CDE, Conn-Weld, Deister, Masaba, McLanahan, Superior, Thor.

| Year | ASTE operating margin | Gencor operating margin | Terex Materials Processing | Alamo Group |
|---|---|---|---|---|
| 2016 | 7.6% | 11.1% | n/r | 8.0% |
| 2017 | 4.7% | 12.7% | n/r | 9.7% |
| 2018 | -7.4% | 13.9% | n/r | 10.0% |
| 2019 | 2.1% | 11.7% | n/r | 8.5% |
| 2020 | 4.2% | 7.1% | 11.4% | 8.0% |
| 2021 | 2.0% | 0.8% | 14.2% | 8.8% |
| 2022 | 0.6% | 4.1% | 15.3% | 9.8% |
| 2023 | 3.6% | 12.7% | 16.1% | 11.7% |
| 2024 | 1.8% | 12.1% | 13.2% | 10.1% |
| 2025 | 4.7% | 12.1% | 13.9% | 9.5% |
| **Whole span** | **2.4% (2016-2025)** | **10.0% (2016-2025)** | **14.3% (2020-2025)** | **9.6% (2016-2025)** |

ASTE's own 2023-2025 margin with the transformation programme, restructuring and impairments added back is 6.3%, 6.5%
and 6.0%, still below each rival in each of those years. Return on equity over 2016-2025 (each year's net income over
that year-end's equity, averaged): ASTE 2.9% (calc output); Alamo 11.4% (net income summed over equity summed); Gencor
5.8% on its whole equity, which is mostly cash and marketable securities ($136.3M of $211.8M at its 2025 year-end), and
18.8% pre-tax on its equity net of them (operating income of $92.7M over the ten years against $494M of year-end
operating equity summed). Terex's equity cannot be split by segment and is not used. "n/r": segment figures not taken
from a filing read for those years.

**The field's returns over the last full cycle** (2016 to 2025 holds the 2018 company loss, the 2020 trough, the
2021-2022 cost squeeze and the 2023-2025 recovery), judged in words, not by a figure **[M1999-108]**: the filing rivals
earned ordinary-to-good returns across the cycle; Astec earned about 3% a year on its owners' equity on average,
below today's 5.60% long government rate, and more than 6% in only two of the ten years (2016 and 2020). The difference is not the field's; it is Astec's.
A castle is what "protects excellent returns" **[L2007-004]**; this one has protected no excellent return, and no
ordinary one, for a decade, while the rivals in the same products did better. That is a castle shown open on the
evidence, the case **[M2011-015]** sends out: others with money already sell these machines more profitably, and the
filer says competition limits its prices.

**The change for the better, and why it does not decide the box.** Since 2023 gross margin and segment profit have
improved each year, backlog rose in 2025, and the ERP spending fell in 2025; a change for the better is credited only on a full cycle in which the
price behaviour held **[M2005-020]**, **[L1995-022]**, and none has passed since it began (the first half of 2026 is
already weaker). Crediting it in full at its best year does not change the answer: in 2025 the company earned 4.7% on
sales, 5.7% on equity, and 9.2% pre-tax on tangible capital employed (11.9% with the transformation programme added
back; calc output), an ordinary return, below every filing rival's margin that year. The railroads "got good"
**[M2017-026]**; this change has not yet made the business good, so there is nothing for the full-cycle test to defer
(see What in the framework was wrong or unclear). Price does not reopen it: "What you can’t do is turn any investment
into a good deal by paying little" **[M2019-015]**; "it makes more sense, as we pointed out, to buy a wonderful business
at a fair price, than a fair business at a wonderful price." **[M2003-040]**

**Hunting the case against this verdict.** (1) The deciding part, before central costs, earns about what the asphalt
rival earns; if corporate cost and the ERP spending fell away the part could earn a decent return. That is a forecast of
a change the filings have not shown, and the central costs have been $43M to $49M a year for five years (Note 19; FY2022
10-K). (2) Parts are an annuity on a large installed base; the filer does not report parts revenue or margins by line
(the segment-expense table shows parts costs of $217.9M in 2025 without the parts revenue beside it), so the annuity
cannot be valued apart from the filings' totals, which already contain it. (3) The weak years 2017-2019 and 2024 had
particular causes (the wood pellet plants, the GEFCO drilling business, the exit at Enid); the record after them,
2023-2025, is still 1.8% to 4.7% operating margin.

- **VERDICT: OUT.** The deciding part's castle, read with the costs of running it, has not protected excellent returns
  over a full cycle **[L2007-004]**; the filer says competition limits its ability to pass through costs **[M2005-020]**;
  better-resourced rivals sell the same machines at margins several times Astec's over the whole span, so Astec is not
  the low-cost producer against them **[M2001-013]**, **[M2009-059]**. A castle shown open on the evidence closes OUT
  **[M2011-015]**, among the rows' three boxes **[M2006-013]**. Q3 to Q12: NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten-year balance sheets were read under Step 0, as the template asks when the file closes before Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The two reporting figures are computed below under the protocol's heading.

### COMPUTATION, NOT A CLEARANCE
*(Operator rule 3: arithmetic made after a closing STOP; it carries no entry language and clears nothing. Built by Q7's
range convention in full, so that the operator's figures are comparable with other runs.)*

- **Inputs.** Owner cash after every real cost, operating cash as filed less stock pay less all capital spending, five
  years 2021-2025 (Step 0 table): -18.7, -121.4, -10.4, -2.5, 13.6; mean **-27.9** equity-only; **-23.1** all-equity
  (interest paid added back after the filer's 26.9% rate). Long government rate 5.60% (Treasury, 2026-10-09). Net debt
  at the latest filed date, 2026-06-30 (10-Q `0000792987-26-000044`): borrowings $393.4M (current maturities 16.2,
  short-term 11.8, long-term 365.4; principal $332.5M term loan and $54.0M revolver plus the foreign lines) less cash
  $76.8M and current investments $1.8M = **$314.8M**. Left out and said so: operating leases; the $23.1M of non-current
  investments, which belong to the deferred compensation programmes (offset by a liability) and the captive insurer.
  Shares 23.025367M. Price $39.48 (aggregator, flagged).
- **(a) Cycles.** The window's first year (2021) and last year (2025) are not described by the filer as a peak, a trough
  or otherwise aberrational; 2022's inventory build is inside the window and stays. The literal window is the base. The
  ten-year mean (2016-2025, which spans the 2018 loss, the 2020 release of inventory and the 2022 build) is shown beside.
- **(b) Decline.** The series changes sign (four negative years, then +13.6), so the compound rate between end years is
  meaningless; measured between the halves of the window, 2021-2022 mean -70.1 against 2024-2025 mean +5.5, it changes
  sign again and is meaningless too. **The range is therefore the no-growth case alone, as (b) directs; it is a point,
  not a range.**
- **(c) Acquisitions.** Net cash paid for businesses 2021-2025: $266.4M (TerraSource $248.7M net of cash acquired in
  2025; $17.8M in 2022). Purchases exceed half of owner cash before purchases (which is negative), so the **serial
  acquirer rule makes the organic pair central** (purchases left out, organic growth as reported; growth is meaningless
  here, so the organic pair is the no-growth case on owner cash before purchases). The default pair (purchases deducted,
  mean -76.3 all-equity, -81.2 equity-only) is shown beside. TerraSource is inside the window and is read on the combined
  figures it already sits in (a cash deal, so an acquisition, not a merger). CWMF, $70.1M in cash on 2026-01-01, closed
  after the window: no earnings of its own are filed (the 10-Q gives only $25.9M of first-half revenue), so it is
  credited at nothing, and its financing is already inside the 2026-06-30 net debt. No signed, unclosed deal was found.
- **(d) Working capital** is counted: the increases sit inside operating cash, and the 2022 build is not tied by the filer
  to one contract or event.
- **(e) Growth spending.** The filing gives no maintenance figure (only the 2026 capital budget, $40M to $50M); D&A
  averaged 29.4 against capex of 31.2, so the D&A basis stands in for the maintenance guess and gives a mean of -26.0,
  shown beside; it does not change the sign.
- **(f) The cap** does not bind: no positive growth is carried.
- **The floor, tested first.** At $39.48 no case earns the floor of about ten percent: every central case is negative,
  and the most generous figure beside it (the five-year owner earnings before working capital, $21.3M, equity-only) is a
  2.3% yield on the $909.0M market value. "there’s just a point at which we drop out of the game" **[M2003-149]**. On the
  convention this would close Q7 OUT before the width is looked at; the width test does not arise, the range being a
  point.

| Case (USD a share) | Base, $M a year | Value at 5.60% | Value at 10% |
|---|---|---|---|
| **Central: organic pair, no-growth alone, all-equity** (less net debt $314.8M) | -23.1 | **-31.55** | **-23.68** |
| Equity-only beside it | -27.9 | -21.62 | -12.11 |
| Default pair (acquisitions deducted), all-equity | -76.3 | -72.87 | -46.82 |
| Default pair, equity-only | -81.2 | -62.94 | -35.25 |
| Beside: ten-year base 2016-2025, all-equity | 16.0 | -1.29 | -6.74 |
| Beside: ten-year base, equity-only | 13.2 | 10.23 | 5.73 |
| Beside: five-year owner earnings before working capital (net income + D&A + impairments - capex), equity-only | 21.3 | 16.50 | 9.24 |

- **VALUE RANGE (the owner's reporting figure, COMPUTATION):** **-$31.55 a share**, all-equity, the no-growth case alone
  (no range can be formed, by specific (b)); equity-only -$21.62; against a price of **$39.48**. No positive figure is
  produced by any case the convention allows; the most generous figure computed beside it is $16.50 equity-only.
- **FAIR PRICE (the owner's reporting figure, COMPUTATION; Part VII):** **-$23.68 a share** on the all-equity basis (the
  single end valued at ten percent, less net debt), **-$12.11** equity-only beside it; after the company's own tax, no
  conversion. Not positive; nothing to arm.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2** (the castle shown open on the evidence: about 3% a year on equity over 2016-2025 with equity flat for nine
years, the filer's own statement that competition limits its ability to pass through cost increases, and filing rivals
earning about four times its operating margin or more on the same machines over the whole span). COMPUTATION beneath the stop:
value -$31.55 a share all-equity (no-growth case alone; no range can be formed), fair price -$23.68 all-equity,
-$12.11 equity-only, against $39.48; no positive figure. **Integrity facts recorded, not judged** (a 2019 shareholder
class action against the company and former officers, settled for $13.7M; material weaknesses in internal control
identified in 2018; immaterial tax-provision errors corrected in 2024).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).

**Bearing on Q3 (capital).** Pre-tax return on tangible capital employed in 2025, the best year of the window: 9.2%
(EBIT $65.9M on $719.2M of equity plus debt less cash, investments, goodwill and intangibles), 11.9% with the
transformation programme added back (calc output). Capex 2021-2025 averaged $31.2M against D&A of $29.4M; the 2026
budget is $40M to $50M (Item 7). Inventory is 33% of 2025 sales. TerraSource cost $252.6M (of which $71.9M repaid its
debt) for a business that contributed $84.7M of revenue and a $2.7M net loss in its first half-year; half its purchase price
went to customer relationships, trade names, patents and other intangibles ($127.2M) and a third to goodwill ($86.4M)
(Note 3). The unaudited
pro forma combined net income was -$19.4M for 2024 and $42.1M for 2025. CWMF cost $70.1M on 2026-01-01.

**Bearing on Q4 (the accounts).** EBITDA in the filer's own mouth: Segment Operating Adjusted EBITDA is the measure "used
by our CEO, who is the chief operating decision maker" (Item 7), and Adjusted EBITDA carries 70% of the 2025 annual
incentive (proxy). The transformation programme ($29.2M, $32.8M, $19.6M in 2023-2025; $151M spent through 2025 of
$180M to $200M expected by 2028 or 2029) is reported outside segment profit every year; restructuring charges recur
(2023 $7.7M, 2024 $9.5M). $28.2M of ERP implementation cost is capitalized (Note 21). The FY2018 10-K
(`0000792987-19-000019`) disclosed material weaknesses in internal control and said disclosure controls were "not
effective"; it also described company-financed wood pellet plant sales with deferred revenue. In the fourth quarter of
2024 the company "identified immaterial errors associated with the calculation of its income tax provisions" and
recorded $2.7M (FY2025 10-K, Note 2). Deloitte & Touche has audited the company since 2023 and reported internal control
effective at 2025-12-31; the auditor-change 8-K of 2023-03-08 (Item 4.01) was seen in the index and not read.

**Bearing on Q5 (people; integrity facts recorded, not judged).** "The Company and certain of its former executive
officers were previously named as defendants in a putative shareholder class action lawsuit filed in 2019"; settled for
$13.7M, "funded entirely by the Company's insurance carriers", approved in September 2024 (Note 16). The 2018 material
weaknesses above. Product claims settled in 2024: 37 Building Products v. Telsmith, $6.3M; VenVer v. GEFCO, $8.4M (Note
16). Management: the chief executive has served since January 2023 (after group-president roles from 2019); the group
president of Infrastructure Solutions left on 2026-04-20 with severance-plan benefits and was replaced (8-K
`0000792987-26-000016`); a director was added on 2026-07-27 (8-K `0000792987-26-000036`). All directors but the chief
executive are independent (proxy).

**Bearing on Q6 (the money and the owners).** Dividends $0.13 a quarter, $11.9M a year (Item 5); buybacks of $24.1M in
2018 and $10.1M in 2022 (XBRL; prices paid not read); shares outstanding rose from 22.62M at the end of 2022 to 23.03M on
the latest cover. Chief executive pay $4.03M in 2025 ($0.84M salary, $2.24M stock, $0.78M incentive), against net
income of $38.8M (proxy). Long-term pay: PSUs on three-year Adjusted ROIC and relative TSR; the 2023 PSUs paid 120% on an
Adjusted ROIC of 10.4% against a 10.0% target and 87% on a TSR "relative to the TSR comparator group" of 43.48% (proxy).
Annual pay: 70% Adjusted EBITDA, 30% working capital turnover. The retention record: retained earnings $537M at the
end of 2016, $568M at the end of 2025.

**Bearing on Q9 (debt).** Borrowings $393.4M at 2026-06-30, up from about zero at the end of 2021; the 2025 credit
agreement carries net-leverage and interest-coverage covenants, "Failure to satisfy these covenants could result in the
accelerated repayment of our indebtedness" (Item 7); part of the borrowing is at variable rates (Item 1A). Interest
expense was $14.5M in the first half of 2026 against operating income of $29.4M. Five-year owner cash is negative, so
the debt has been serviced from borrowing and working-capital release, not from surplus cash. Customer-financing
guarantees are small ($0.6M), letters of credit $5.3M plus $4.1M (Note 16).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit d7f15c94); written question by question; committed after Step
      0, Q1 and Q2, and at the close (write-early).
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (not checked here, by
      the brief); the fold into the register is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. One listing of `Test Runs/`
      filtered to today's date, made to check this file's name, showed other runs' names; declared under contamination
      at the top and not used. On reflection that listing should not have been made; a direct test of this run's own
      path would have served.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-13 ASTE/check_ids.py`); every filing fact has its
      accession or its 10-K item; numbers come from a filing or from the run's arithmetic files.
- [x] The order was kept; Q2's STOP closed the run; every figure after it sits under COMPUTATION, NOT A CLEARANCE or
      AFTER THE STOP.
- [x] Owner cash after every real cost (operating cash less stock pay less all capex), never a net-income proxy; the
      before-working-capital figure that uses net income is shown only beside, labelled, and decides nothing. Sovereign
      from the Treasury. The price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations; the hunt in Q2); facts for later questions are under AFTER
      THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 text was not read as a rule.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded below).
- Shortfalls, said plainly: the Alamo 10-K and the Gencor 10-Ks before FY2025 were not opened (their series are XBRL
  transcription); Terex's Materials Processing figures for 2016-2019 were not taken; segment D&A is not filed, so the
  deciding part's return after its own depreciation could not be computed; the buyback prices of 2018 and 2022 were not
  read; the auditor-change 8-K and the TerraSource 8-K were not opened.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The change for the better, when crediting it still leaves ordinary returns.** Q2 says a change for the better is
credited only on a full cycle and "until then the file is TOO HARD (NATURE) on that question". Read literally, any
improving business with a short record would close TOO HARD (NATURE) with a re-look date, even where the improved
figures, taken at face value, still show only ordinary returns and so could not make the castle IN. This run read the
deferral as applying only where crediting the change would decide the question, and closed OUT; the text should say
which. (2) **The parts rule assumes a segment operating profit the filer does not report.** The threshold is "five-year
operating profit"; this filer gives only an adjusted EBITDA before depreciation, central costs and a large multi-year
ERP programme, so the shares were measured on it (a CONVENTION of this run), and the deciding part's castle had to be
read "with the costs of running it", which the rule does not mention. A sentence on central costs (allocate, ignore, or
read the part before them and the whole after them) would stop two analysts splitting here. (3) **"The standing castle
that protects only ordinary returns" speaks of a field whose durable players all earn ordinary returns.** Here the
filer alone does, and its filing rivals earn more; the item does not fit, and the run closed instead on "a castle shown
open on the evidence". The text has no sentence for the weak participant in a field that earns decent returns, which is
the commoner case. (4) **A range that is a point.** Specific (b) can leave "the no-growth case alone", and Part VII's fair
price is "each end case valued at ten percent, the two averaged"; with one end the fair price is that end at ten
percent, which this run used, and the three-to-one width test cannot be applied. (5) **After-tax interest for the
all-equity basis** needs a tax rate the text does not name; the filer's latest effective rate was used and confessed.
