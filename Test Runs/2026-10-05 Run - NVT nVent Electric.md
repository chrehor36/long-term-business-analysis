# Company Run — nVent Electric plc (NYSE: NVT) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not known to this analyst. The run was dispatched blind: `PORTFOLIO.md`,
the holding reviews, the session-state file, the register, the prepped reading list and any other `Test Runs/` file on
this company were not opened, and no attempt was made to learn whether anyone holds or wants the name.

**CONTAMINATION, declared.** (1) The commit subjects shown at the start of the session name five other v5 runs dated
today (WCC, LMB, DY, MTZ, PRIM), each closed OUT at Q2; their boxes were seen, their files were not opened. (2) The git
status shown at the start lists an untracked file `2026-10-05 Run - HUBB Hubbell.md` and HUBB, ETN and other peer data
files inside another run's research folder (AYI, 2026-09-26); none was opened, and every competitor figure below was
fetched fresh from EDGAR. (3) The session memory index says, of the whole watchlist, that many names cleared the gates
and "nothing buyable"; it names no verdict on this company. (4) `tools/run.py` prints v4 material; only its arithmetic
lines were read (Part VII), and its owner-earnings lines were found defective for this filer (Step 0).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $169.55 (quote of 2026-10-05 printed by `tools/run.py`; aggregator, live quote only, flagged per operator
  rule 5). For scale only: the proxy gives the closing price on the last trading day of 2025 as $101.97 (DEF 14A filed
  2026-03-31, accession `0001104659-26-037751`), so the quote has risen about two-thirds in nine months.
- **Shares by class** from the latest filing's cover: one class, ordinary shares, $0.01 nominal, **161,857,939**
  outstanding on June 30, 2026 (10-Q for the quarter ended 2026-06-30, filed 2026-07-31, accession
  `0001628280-26-051428`; `python Screens/cover_shares.py NVT` returns the same count). Irish plc, one class; no charter
  note bears on the count.
- **Market cap:** 169.55 × 161.858M = **$27,443M**.
- **Sovereign for the earnings currency:** USD, US Treasury daily par yield curve, 30-year, **5.63%**, 2026-10-02
  (`python tools/sources.py`, issuing authority). About three-quarters of sales are in the US (sales outside the US
  "approximately 24%" in 2025, 10-K Item 1A); reporting currency USD.
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-17, accession `0001628280-26-008608`: Items 1, 1A, 7, the three statements, segment and
    disaggregation notes.
  - 10-Q Q2 2026, filed 2026-07-31, accession `0001628280-26-051428`: statements, disaggregation, MD&A, repurchases.
  - DEF 14A, filed 2026-03-31, accession `0001104659-26-037751`: incentive metrics, the year-end price.
  - 8-Ks: 2026-02-06 `0001628280-26-005930` (Q4 2025 release, first 2026 guidance); 2026-05-01 `0001628280-26-029098`
    (Q1 release, guidance raised); 2026-07-31 `0001628280-26-051203` (Q2 release, guidance raised again); 2026-09-15
    `0001104659-26-107974` (Ex. 99.1, prospectus excerpt on the Maverick Power acquisition); 2026-09-16
    `0001104659-26-108250` (underwriting); 2026-09-17 `0001104659-26-108580` (term loan); 2026-09-29
    `0001104659-26-111938` ($800.0M 6.150% notes due 2036 issued).
  - Earlier 10-Ks for the history: FY2018 `0001720635-19-000008`, FY2019 `0001720635-20-000009`, FY2020
    `0001720635-21-000013`, FY2021 `0001720635-22-000009`, FY2022 `0001720635-23-000009`, FY2023
    `0001720635-24-000012`, FY2024 `0001720635-25-000018`.
  - Competitors (fetched fresh): Vertiv 10-K FY2025 `0001674101-26-000008` (text read for its competition section);
    XBRL company facts for HUBB, ETN, ATKR, VRT (accessions in the competitor row below).
- **One figure cross-checked against the filed statement:** net cash from operating activities, FY2025. `tools/run.py`
  prints $465M; the filed cash-flow statement (10-K FY2025, `0001628280-26-008608`) shows $465.2M in total but
  **$649.0M from continuing operations** and $(183.8)M from discontinued operations (largely tax on the Thermal sale).
  The tool took the total, so for 2024 it also took $643M including Thermal's $142.1M. **The tool's owner-earnings
  lines are defective for this filer and are not used**; the table below is recast from the filed statements on a
  continuing basis.
- `tools/run.py` arithmetic lines, recast (USD millions; owner cash = operating cash of continuing operations, less stock
  pay added back in it, less all capital spending net of equipment sale proceeds; the depreciation variant beside it):

| FY | operating cash | stock pay | capex, net | depreciation | **owner cash** | depreciation variant | source |
|---|---|---|---|---|---|---|---|
| 2021 | 373.3 (consolidated, Thermal inside) | 16.6 | 38.9 | 40.9 | **317.8** | 315.8 | FY2021 10-K |
| 2022 | 273.3 (continuing, restated) | 23.3 | 38.5 | 36.1 | **211.5** | 213.9 | FY2024 10-K |
| 2023 | 422.2 | 21.8 | 65.5 | 43.7 | **334.9** | 356.7 | FY2025 10-K |
| 2024 | 501.0 | 27.3 | 73.5 | 51.3 | **400.2** | 422.4 | FY2025 10-K |
| 2025 | 649.0 | 37.5 | 88.0 | 60.7 | **523.5** | 550.8 | FY2025 10-K |
| five-year mean | | | | | **357.6** | 371.9 | |

  2021 cannot be put on a continuing basis: no filing restates it without Thermal (the FY2024 10-K restates 2022 to 2024
  only). The four continuing years average $367.5M. First half 2026: $278.7M − $23.1M − $57.6M = $198.0M (10-Q).
  Earlier consolidated years, as filed: 2016 $282.0M, 2017 $367.5M, 2018 $293.6M, 2019 $287.7M, 2020 $292.1M (FY2018,
  FY2019, FY2020 10-Ks). Amortization of purchased intangibles ($147.1M in 2025) is a non-cash charge and is already
  outside operating cash.

## THE FOUNDATIONS (not a gate)
Three bear on this name. **The market serves, it does not instruct:** the quote has gone from $101.97 to $169.55 in nine
months on a run of guidance raises; "It just tells us prices." **[M2006-077]**, and a rise "is never a reason to buy it"
**[L2013-007]**. **A share is a business:** the test is whether one would be content to own it "if the market closed for
five years" **[M1997-109]**, which turns the question onto the ten-year economics of a business that the filings show
has been rebuilt by deals since 2023. **The analyst's habits:** look for "what’s wrong in things" **[M2025-013]** and
write down at once what cuts against the case **[M1997-127]**; and the habit the excitement tempts one to skip, that
seeing "dramatic growth ahead for an industry does not mean we can judge what its profit margins and returns on capital
will be" **[L2009-005]**. No macro view enters: the AI-capex cycle is not forecast here, which is exactly why it cannot
be used to clear Q1 **[M2000-094]**.

**Contrary evidence, written down as found** **[M1997-127]**:
- 10-K FY2025 Item 1: "We compete against large and well-established national and global companies, as well as regional
  and local companies and lower-cost manufacturers. Some of our competitors, in particular smaller companies, attempt to
  compete based primarily on price".
- 10-K FY2025 Item 1A: future revenue requires the company "to successfully bid on new contracts and, in particular,
  contracts for large greenfield projects, which are frequently subject to competitive bidding processes"; fixed-price
  contracts can lose money if costs exceed the bid.
- Largest customer about 11% of 2025 net sales (10-K Item 1A); not named.
- Infrastructure (data centers and power utilities) rose from $796.8M of $2,668.9M sales in 2023 (30%) to $1,746.1M of
  $3,893.1M in 2025 (45%) and $882.5M of $1,471.3M in Q2 2026 (60%) (10-K note on disaggregation; 10-Q).
- 2026 organic sales guidance moved from 10 to 13% (Feb 6) to 21 to 23% (May 1) to 32 to 34% (July 31): management's
  own one-year forecast nearly tripled in six months (the three 8-K releases above).
- "liquid cooling" appears zero times in the FY2021 and FY2023 10-Ks, once in FY2024 and once in FY2025 (text count),
  yet the Q2 2026 release credits data-center growth and new products with "more than 30 points" of sales growth.
- Goodwill and intangibles of $4,554M exceed equity of $3,730M at 2025 year-end; tangible equity is negative (10-K).
- $1.75B cash acquisition of Maverick Power (data-center power distribution, revenue about $527M in the twelve months to
  June 2026) plus up to $550M of earn-out, financed with about $1,650M of new debt (8-K 2026-09-15, Ex. 99.1).
- Owner cash was flat for six years as filed (about $282M to $368M, 2016 to 2021) before the deals of 2023 to 2025.
- Vertiv, the largest dedicated data-center infrastructure competitor, writes that its competitors "could introduce new
  technologies or business models that disrupt significant portions of our markets" and that it carries "the risk of
  inventory obsolescence because of rapidly changing technology and customer requirements" (Vertiv 10-K FY2025,
  `0001674101-26-000008`).

## THE STANDING RULE
The buyer's own ruin is not at risk from the analysis: no purchase is made here, and any purchase would be made with the
buyer's own money and no borrowing, since "borrowed money has no place in the investor's tool kit" **[L2014-005]**;
"We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years", including "how the industry will develop and where the company will stand
within the industry" **[M2012-065]**; it is not knowing the product: "We just don’t know the economics of it 10 years
from now." **[M2000-104]**.

**What the business now is, from the filings.** The nVent of the 2018 spin was three segments of roughly equal weight to
each other in profit: Enclosures (Hoffman, Schroff), Thermal Management, and Electrical & Fastening Solutions (ERICO,
CADDY), with sales of about $2.2B and owner cash near $290M a year (FY2018 10-K). Since then the company has sold Thermal
($1.6B net proceeds, January 2025), bought ECM Industries ($1.1B, 2023), Trachte ($0.7B, 2024), the Avail Electrical
Products Group ($1.0B, 2025), and agreed to buy Maverick Power ($1.75B plus up to $0.55B of earn-out, 2026) (10-K FY2025
Item 1; 8-K 2026-09-15). The segments were renamed Systems Protection and Electrical Connections in 2025. Infrastructure,
"which includes our data centers business that is primarily in our Systems Protection segment" (10-Q MD&A), is 60% of Q2
2026 sales, and Maverick adds about $527M of data-center power revenue on top. Backlog went from $749.3M to $2,349.9M
in 2025 (10-K Item 1). The business a buyer would own in 2026 is, by sales, mostly a supplier of cooling, enclosures,
switchgear, bus and power distribution into data-center and utility construction, with an older industrial and
electrical-products business beside it.

**The key variables and whether they are foreseeable** **[M1998-044]**:
1. *The level of data-center construction spending over ten years.* The company's own one-year forecast moved from 10 to
   13% organic growth to 32 to 34% within six months of 2026. If the insiders' forecast for the current year moves by
   twenty points, the insiders would not write the ten-year figure down **[M2000-105]**. "If something is not very
   predictable, forget it." **[M1998-044]**.
2. *nVent's place among the suppliers of liquid cooling and power distribution.* The product line that the Q2 release
   credits with most of the growth does not appear by name in the 10-Ks before FY2024. The competitors named in Vertiv's
   own filing are Schneider, Eaton, Legrand, Huawei, Delta, Stulz, Johnson Controls and Socomec, besides nVent; Vertiv
   itself warns of technologies "that disrupt significant portions of our markets". This is the case the 2009 letter
   names: "dramatic growth ahead for an industry does not mean we can judge what its profit margins and returns on
   capital will be as a host of competitors battle for supremacy" **[L2009-005]**; "there’s industries we know that may
   have a wonderful future, but we don’t have the faintest idea who the winners will be" **[M2012-067]**.
3. *Margins on bid project work.* The 10-K says the large greenfield projects are "frequently subject to competitive
   bidding", some at fixed price. The margin on that work through a down-cycle has not been seen: the infrastructure
   share was 30% of sales as recently as 2023.

**Do the past statements tell me the future ones?** **[M2008-033]**. No. The FY2018 to FY2021 statements describe a
company one-third of which (Thermal) is gone and which had no named liquid-cooling line; the 2025 statements carry eight
months of a $1.0B acquisition and none of the $1.75B one pending. The statements of 2026 to 2036 will be those of a
business still being assembled.

**How far off could I be?** **[M2011-084]**. Very far: owner cash could plausibly be half or double the 2025 figure in
five years depending on a spending cycle the company itself cannot see one year ahead. A gain made "very quickly" is the
kind the rows warn can be lost quickly: "when an industry is in flux, there are a lot of people that think they’re the
survivors" **[M2002-050]**.

**Change.** "whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass
on that" **[M1999-063]**; "a business that must deal with fast-moving technology is not going to lend itself to reliable
evaluations of its long-term economics" **[L1993-023]**. The routing is fixed: a business whose ten-year economics
cannot be foreseen because its industry changes fast closes at Q1, TOO HARD **[M1998-008]**.

**The older half.** Enclosures, grounding, fastening and connectors (Industrial, Commercial & Residential and Energy,
together about 40% of Q2 2026 sales) are businesses whose economics a reader can follow: Electrical & Fastening margins
held between 25.3% and 31.1% of sales from 2016 to 2025, through the 2020 fall (segment tables, 10-Ks FY2018 to FY2025).
But the part that cannot be foreseen is the larger part and the part the company is buying more of, so by the doubt
rule the whole stays outside: "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**; and it is "better to be well within the circle than to be trying to tiptoe along the line"
**[M2002-093]**. The by-parts reading is the framework's CONVENTION for holding companies (Q1, A holding company),
applied here by analogy; see the closing section.

**Which cause.** NATURE. The deciding question is where the data-center majority's earnings and competitive position
will stand in ten years; the industry's insiders do not write that down, and nVent's own management could not write
down the current year within twenty points. More reading would not cure it: "We couldn't solve this problem, moreover,
even if we were to spend years intensely studying those industries." **[L1993-023]**. Test 5 of Q1 decides between the
two causes **[M2000-105]**.

**VERDICT: TOO HARD (NATURE).** Not a judgment of quality: "It doesn’t mean it isn’t a good buy. It doesn’t mean it
isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**; the
box is the rows' third, "in, out, and too hard" **[M2006-013]**. A lower price does not reopen it **[M2000-038]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**NOT REACHED.** The competitor row was gathered before the close and is recorded at the end under COMPUTATION; it
decides nothing.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.**

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The ten-year balance-sheet reading was done at the owner's request and is recorded under COMPUTATION; it
clears nothing.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts gathered, unjudged: repurchases of $253.1M in 2025 and $50.4M in the first half of 2026 under
dollar authorizations that name no price (10-K Item 5; 10-Q); a new $500.0M authorization from July 23, 2026; dividends
of $0.21 a quarter; annual incentive metrics include adjusted EPS, sales and free cash flow, and performance shares pay
on relative TSR (DEF 14A); adjusted EPS of $3.35 against reported $2.60 for 2025 (DEF 14A), the gap being mostly
amortization of purchased intangibles.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** At the owner's request the value range, the fair-price band and the cheap price are computed below,
headed as COMPUTATION; none of them is a clearance.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Fact gathered: total debt $1,500.0M at June 30, 2026, rising by about $1,650.0M with the Maverick
financing (8-K 2026-09-15, Ex. 99.1); covenants cap consolidated net debt at 3.75 times EBITDA as the lenders define it,
4.25 times for four quarters after a material acquisition (8-K 2026-09-17).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (Nothing in the filings read names a business of the kinds Q12 lists.)

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** The majority of the business, and the part being bought, now rides on
data-center construction and on a liquid-cooling and power-distribution field whose ten-year shape and winners the
industry's own insiders do not write down; the company's 2026 organic growth forecast went from 10 to 13% to 32 to 34%
in six months. No research pass is opened: the cause is the industry's, not the work's (section I, the two causes). For
the record only, the COMPUTATION below puts the value range at **$39 to $61** a share against **$169.55**.

---
## COMPUTATION — NOT A CLEARANCE
*(The file closed at Q1. Everything in this section was computed at the owner's request, carries no entry language,
and would not reopen the box at any price **[M2000-038]**.)*

**1. The ten balance sheets** (`tools/run.py` table, checked against the filed statements; USD millions; the 2017 column
is Pentair's carve-out, before the spin; 2023 and 2024 include Thermal held for sale, 2025 does not). What the figures
can and cannot say **[M2025-032]**:

| year-end | assets | equity | goodwill + intangibles | long-term debt | cash | inventory | retained earnings |
|---|---|---|---|---|---|---|---|
| 2017 | 4,725 | 3,791 | 3,475 | 0 | 27 | 224 | 0 |
| 2018 | 4,553 | 2,687 | 3,407 | 929 | 159 | 228 | 83 |
| 2019 | 4,640 | 2,592 | 3,439 | 1,047 | 106 | 245 | 187 |
| 2020 | 4,366 | 2,410 | 3,204 | 928 | 122 | 235 | 21 |
| 2021 | 4,674 | 2,496 | 3,331 | 994 | 50 | 322 | 174 |
| 2022 | 4,902 | 2,732 | 3,244 | 1,068 | 298 | 347 | 457 |
| 2023 | 6,162 | 3,142 | 4,088 | 1,749 | 185 | 441 | 905 |
| 2024 | 6,735 | 3,238 | 3,809 | 2,118 | 131 | 360 | 1,109 |
| 2025 | 6,852 | 3,730 | 4,554 | 1,546 | 238 | 472 | 1,688 |
| Jun 2026 | 7,146 | 3,987 | 4,470 | 1,479 | 256 | n/r | n/r |

- *Equity against goodwill and intangibles.* Goodwill and intangibles have exceeded equity in every year since the spin
  (2018: $3,407M against $2,687M; 2025: $4,554M against $3,730M). Tangible equity has been negative throughout; the
  business runs on the intangibles bought by Pentair (ERICO, 2015) and by nVent (2019 to 2025), and on debt. A
  $212.3M goodwill impairment of Thermal in 2020 (FY2020 10-K) shows a bought intangible that did not hold.
- *Equity's path.* $3,791M carve-out equity fell to $2,687M at the spin, when about $1.0B was borrowed and paid to the
  parent (FY2018 10-K). Retained earnings rose from $83M (2018) to $1,688M (2025), but $435.3M of that is the 2025 gain
  on the Thermal sale (10-K FY2025 MD&A), so the operating build is smaller than the line suggests.
- *Debt.* Zero before the spin, $0.9B to $1.1B through 2022, $2.1B at the 2024 peak after ECM and Trachte, $1.5B after
  the Thermal proceeds repaid term loans in 2025, and about $3.1B on completion of Maverick (8-K 2026-09-15). The debt
  has been used to buy, then partly repaid from a sale, then raised again to buy.
- *Receivables and inventory against sales.* 2025 receivables $693.0M against $473.1M (+46%) on sales +29.5%; inventory
  +31%. Both are distorted by the May 2025 acquisition, whose year-end balances carry a full run-rate against eight
  months of sales; no tell is read from them. Contract assets and liabilities, and bonds and letters of credit ($75.7M
  against $10.7M), grew with the project work (10-K).
- *What they cannot say.* Before 2016 the business sits inside Pentair as part of a segment; the FY2018 10-K gives 2016
  and 2017 only. No balance sheet shows a data-center business through a full cycle, because there has not been one in
  these filings.

**2. Owner cash**, from Step 0: five-year mean **$357.6M** (all capital spending deducted; depreciation variant
$371.9M); four continuing years $367.5M. Shown growth on aggregate owner cash, 2021 to 2025: 13.3% a year, on a mixed
basis (2021 includes Thermal); 2022 to 2025 on a continuing basis it is 35% a year, which is mostly purchased: $2,773.5M
was spent on acquisitions in 2023 to 2025 against $1,584.5M received for Thermal (10-K FY2025 cash-flow statement). The
base-year warning applies **[L2005-003]**.

**3. The value range** (CONVENTION, Q7: five-year average, growth shown capped by Q3, ten years then no growth, at the
sovereign; the two ends are the no-growth and shown-growth cases). The shown 13.3% runs past the 5.63% discount rate and
is capped at it **[M1997-095]**, **[M1999-067]**. Owner cash is after interest, so net debt is not subtracted again;
Maverick's earnings and its debt are both left out, as neither is in the filed history.
- No-growth: $357.6M ÷ 5.63% = $6,352M = **$39.2** a share.
- Shown growth, capped at 5.63% for ten years, then zero nominal growth: $9,928M = **$61.3** a share.
- **Value range $39 to $61 against $169.55.** Width 1.56 to 1. Depreciation variant $40.8 to $63.8.
- Sensitivities, not the convention input: at the uncapped 13.3% for ten years, $112; at a hypothetical $800M of owner
  cash (well above any year filed) the range is $88 to $137. The price is above every version computed.
- Expected return at $169.55, after tax: 1.3% (no growth), 2.2% (capped growth), 3.9% (uncapped growth). Converted to
  pre-tax as below, every case is under 5%, far below the floor of about ten percent pre-tax (CONVENTION, Q7;
  **[M2003-149]**, **[L2002-020]**, **[M1994-004]**).

**4. The fair-price band.** *Conversion between pre-tax and after-tax:* owner cash is an after-tax figure (operating
cash is after cash taxes). The floor of about 10% pre-tax is converted to after-tax at the company's 2025 effective tax
rate on continuing operations, 22.1% (10-K FY2025): 10% × (1 − 0.221) = **7.79% after tax**. (The 2002 letter's own
conversion, at the corporate rate of its day, was "6�-7% after corporate tax" **[L2002-020]**, the character damaged in
the row; using it would lower every price below.) The price at which each case returns 7.79% after tax:
- No-growth case: $357.6M ÷ 7.79% = **$28.4** a share.
- Capped-growth case, discounted at 7.79%: **$43.0** a share.
- **Fair-price band, inside the range: $39 to $43**, and only in the capped-growth case; in the no-growth case no price
  inside the range clears the floor (it clears only at $28.4 and below).

**5. The cheap price: $28** (CONVENTION, ours, for this report: the price at which the no-growth case alone earns the
floor, so that the case needs no growth assumption and no pencil **[M1996-084]**, **[M2009-005]**). It is a computation
on a file that is closed, and it would not open the file: a business that cannot be evaluated is not cured by "some
extra large margin of safety" **[M2007-022]**.

**6. The competitor row** (gathered before the close; decides nothing). Operating income after depreciation and
amortization, as a percentage of sales, and against net tangible operating assets (total assets less goodwill,
intangibles and cash), each company's own 10-K as first filed, via XBRL company facts:

| | 2016 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| **NVT** margin / on NTA | 15.7 / 15 | 14.0 / 32 | 15.1 / 30 | 1.9 / 4 (impairment) | 14.4 / 28 | 15.1 / 32 | 18.0 / 31 | 17.5 / 18 (held-for-sale assets inflate the base) | 15.8 / 27 |
| **HUBB** | 13.6 / 29 | 12.4 / 27 | 13.0 / 28 | 12.7 / 26 | 12.7 / 22 | 14.3 / 31 | 19.3 / 37 | 19.4 / 39 | 20.7 / 37 |
| **ETN** | 15.0 / 27 | 16.8 / 29 | 17.2 / 26 | 10.6 / 13 | 15.5 / 23 | n/a | 17.1 / 22 | 18.9 / 25 | 18.8 / 26 |
| **ATKR** (FY Sept) | n/a / 21 | 9.8 / 24 | 11.7 / 23 | 13.6 / 22 | 27.3 / 67 | 31.5 / 80 | 25.4 / 49 | 19.5 / 31 | 0.8 / 1 |
| **VRT** | n/a | n/a | 4.7 / n/a | 4.9 / 8 | 5.2 / 9 | 3.9 / 6 | 12.7 / 21 | 17.1 / 27 | 17.9 / 28 |

Accessions of the FY2025 10-Ks: HUBB `0001628280-26-007500`, ETN `0001551182-26-000007`, ATKR `0001628280-25-054049`,
VRT `0001674101-26-000008`, NVT `0001628280-26-008608` (earlier years from each company's 10-K for that year; ETN 2020
onward is pre-tax income plus interest expense, its operating-income tag having stopped; ETN 2022 not tagged). nVent's
margins sit with Eaton's and below Hubbell's since 2023; its returns on tangible operating assets are in the same band
as Hubbell and Eaton in ordinary years; Atkore shows what a commodity electrical product (conduit) did through the 2021 to 2022 price spike (its 2025 figure was not examined), and
Vertiv what the data-center supplier's margin was before the boom (4 to 5%). Segment detail: Electrical & Fastening
(now Electrical Connections) held 25 to 31% segment margins from 2016 to 2025 and took price of 1.6% in 2020 against a
volume fall of 6.1% (FY2020 10-K); Enclosures (now Systems Protection) ran 15.6 to 22.1% (segment income excludes
amortization; 10-Ks FY2018 to FY2025).

**7. The strongest evidence against, in one line:** the business a buyer gets in 2026 is not the business whose history
is on file; the majority is data-center project supply, bought or grown in three years, bid competitively against
larger rivals in a field its leading competitor calls subject to disruptive technology, priced at about 77 times the
five-year owner cash.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written question by question in one pass; **not committed**: the
      dispatch instruction forbade commits, so write-early was kept by writing the file first and filling it, not by
      commits after each question.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      checked to be in that row); every filing fact has its accession; no number without a row or a filing, except the
      CONVENTION figures labelled as such.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance, and the COMPUTATION section is
      headed as operator rule 3 requires.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); stock pay deducted; all capital
      spending deducted, depreciation variant shown; the sovereign from the US Treasury; the price quote flagged as an
      aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]**.
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII), and its owner-earnings lines were rejected after
      the cross-check.
- [x] `python tools/check_framework.py` PASS before the hand-off (see the closing report).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **Q1 has no rule for a business that is part understood and part not.** The by-parts reading exists
only for a holding company (Q1, A holding company, CONVENTION). nVent is an operating company with an old, legible half
and a new, larger half that cannot be foreseen; I applied the doubt row **[M2002-092]** and the holding-company
convention by analogy, letting the part that matters most and is growing decide. A stated rule (does the unforeseeable
part have to be the majority, or only material?) would stop two analysts closing the same name at Q1 and at Q2. (2)
**The Q7 range convention breaks on a company rebuilt by deals.** The convention measures growth on aggregate owner cash; over five years that
it counts purchased growth as if it were organic and mixes a divested business into the base year; the convention says
nothing about deducting acquisition outlays or restating for divestitures. Here the cap at the discount rate made the
question moot, but on a cheaper name it would decide the box. (3) **Q7's growth cap is ambiguous**: the convention's words on a rate that runs past the discount rate could cap the ten-year growth input at the sovereign, as done here, or only forbid a perpetual
rate above it; the two readings give $61 against $112 at the top of this range. (4) **The floor's conversion is not
fixed.** The Q7 convention states the floor pre-tax, owner cash is after tax, and the only conversion the rows give is the 2002 letter's, "6�-7% after corporate tax" **[L2002-020]**, at the corporate rate of that year. I converted at the company's effective rate; a stated rule (statutory, effective, or the row's own) would make fair-price bands comparable across runs. A smaller point: `tools/run.py` takes total operating cash
including discontinued operations, so its owner-earnings lines are wrong for any filer with a recent divestiture.
