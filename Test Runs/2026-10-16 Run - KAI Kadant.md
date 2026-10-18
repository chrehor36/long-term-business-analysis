# Company Run — Kadant Inc. (NYSE: KAI) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md` (the overnight cycle's brief of 2026-10-16, with its two
stated departures: the lines of evidence are derived by the analyst from Items 1, 1A and 7 of the latest 10-K, and the
competitors are the rivals the 10-K names). Kadant Inc., SEC CIK 0000886346, formerly Thermo Fibertek Inc. to 2001.
Research folder: `Test Runs/_research 2026-10-16 KAI/` (raw filings in its gitignored `cache/`; `notes.md` lists the
lines of evidence chosen and where from; `scripts/q7.py` and `q7_output.txt` carry the Q7 arithmetic).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (e9ea3091): `PORTFOLIO.md` read for this ticker only; not held.*

**Contamination declared (the blind rule).** (1) A listing of `Test Runs/` filtered to today's date, made at the start to
see whether this run file already existed, showed the names of other companies' run files and research folders dated
2026-10-16 (none for KAI). (2) A directory listing of another company's research folder (`_research 2026-10-16 STRL`)
was made by mistake while looking for how sibling runs lay out their scripts; it showed file names only (scripts, drafts,
an output file); no file was opened. (3) The session context carried recent commit subjects about STRL and a memory
index line about the queue in general; none names Kadant. Nothing of these was used. No other `Test Runs/` file about
Kadant, Thermo Fibertek or KAI was opened, listed or searched; `PORTFOLIO.md`, holding reviews, the register, the reading
list and the resume-state files were not opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $264.15 (quote of 2026-10-16 as printed by `python tools/run.py KAI`; aggregator, a live quote only, flagged
  per operator rule 5).
- **Shares by class** from the latest filing's cover: 11,809,117 shares of common stock, $.01 par, the only class (10-Q for
  the quarter ended 2026-07-04, filed 2026-08-12, accession `0000886346-26-000052`, cover as of 2026-07-31;
  `python Screens/cover_shares.py KAI`). Checked against the 10-Q balance sheet: 14,624,159 issued less 2,815,057 in
  treasury at 2026-07-04 = 11,809,102, a difference of 15 shares, consistent with RSU vesting. No 8-K or prospectus filed
  after the 10-Q issues shares (the 8-K of 2026-09-10, `0000886346-26-000055`, is the CEO succession). No preferred stock
  issued (5,000,000 authorized, none issued).
- **Market cap:** $264.15 x 11.809117M = **$3,119.4M**.
- **Sovereign for the earnings currency (USD; the XBRL unit of the cash-flow series):** **5.43%**, the 30-year par yield of
  the US Treasury daily par yield curve, dated 2026-10-15 (issuing authority, as printed by `tools/run.py`, which calls
  `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025 (fiscal year ended 2026-01-03), filed 2026-03-03, accession
  `0000886346-26-000018` (Items 1, 1A, 3, 7, 7A, 8 notes on revenue, goodwill, segments); 10-Q for the quarter ended
  2026-07-04, filed 2026-08-12, `0000886346-26-000052`; proxy DEF 14A filed 2026-04-01, `0000886346-26-000027`; 8-Ks
  `0000886346-26-000034` (Profil closing, 2026-04-30), `0000886346-26-000049` (Q2 2026 results, exhibit 99.1),
  `0000886346-26-000037` (Q1 2026 results, exhibit 99.1), `0000886346-26-000015` (2026-02-23, adjusted measures recast,
  exhibit 99), `0000886346-26-000011` (FY2025 results, exhibit 99.1), `0000886346-25-000003` (FY2024 results and 2025
  guidance), `0000886346-24-000022` (FY2023 results and 2024 guidance), `0000886346-26-000055` (succession, and its
  exhibit 99). The last cycle: 10-Ks for FY2009 (`0001193125-10-058296`), FY2010 (`0001193125-11-069984`), FY2015
  (`0000886346-16-000221`), FY2020 (`0000886346-21-000021`), FY2021 (`0000886346-22-000018`), FY2022
  (`0000886346-23-000019`), FY2023 (`0000886346-24-000026`), FY2024 (`0000886346-25-000006`). **One figure
  cross-checked against the filed statement:** operating cash flow FY2025 $171.3M as `tools/run.py` transcribes it equals
  "Net Cash Provided by Operating Activities | $ | 171,328" in the FY2025 10-K's free-cash-flow reconciliation (Item 7).
- `python tools/run.py KAI` arithmetic lines only (output kept at `Test Runs/_research 2026-10-16 KAI/run_py.txt`):
  operating cash less stock pay less capital spending, FY2023 to FY2025: $123.9M, $123.6M, $143.0M; with depreciation and
  amortization in place of capital spending: $122.5M, $95.0M, $108.9M. Capital spending $31.9M, $21.0M, $17.0M against
  depreciation and amortization $33.3M, $49.6M, $51.2M (of which depreciation alone $14.8M, $20.5M, $22.9M, the rest
  amortization of acquired intangibles; FY2025 10-K Item 7 reconciliation). Stock pay $9.8M, $10.6M, $11.2M, one tag,
  resolved and complete. Other capital payments the tool found: finance-lease principal $1.1M to $1.2M a year and
  dividends to minority partners $1.3M (FY2024) and $1.7M (FY2025). The five-year owner cash used at Q7 is built in
  `scripts/q7.py` from the filed lines, not from the tool's three-year mean.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest on this name is the share as a business: "Would I be happy buying this stock if the
market closed for five years?" **[M1997-109]**. Kadant is a maker of machinery and of the parts that wear out in it, and
the question is what that installed base will pay its owner over a decade, not what the next buyer pays; the market
"just tells us prices" **[M2006-077]**. The second is who is paid to tell you: the company's own releases headline
adjusted figures and give annual and quarterly guidance (Q4 below), so its own commentary is read as a seller's.
**Contrary evidence, written down as found** **[M1997-127]**: (1) in the last deep downturn the business went to an
operating loss of $0.5M on revenue down 38% from 2007 (FY2009 10-K, selected financial data, `0001193125-10-058296`),
and its then only segment earned 4.7% on revenue in 2009; (2) growth since 2016 is mostly bought: $1,028M spent on
businesses FY2017 to FY2025, goodwill from $151M to $556M; (3) the adjusted earnings figure was redefined upward five
days after a year that missed the company's own guidance (Q4); (4) the price is far above every case of the range (Q7).

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? A part-interest bought for cash, without borrowed money, puts no demand
for sudden sums on the buyer; "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and nothing in
this purchase requires it. Kadant's own revolver debt is the target's exposure, weighed at Q9, not the buyer's conduct.
The rule is met as long as the purchase is made with the buyer's own money and sized so it can be held through a fall
**[M2004-065]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**.
  The products (doctor blades, rotary joints, syphons, stock-preparation and recycling lines, debarkers and stranders,
  conveyor idlers, balers) need not be understood as engineering; "What is important is that I understand the economic
  dynamics of the industry" **[M2011-014]**.
- **The key variables, and how predictable they are** **[M1998-044]**. (1) Production volume at the customers' mills and
  plants, which drives the parts and consumables that were "a record 71% of revenue in 2025" ($748.4M of $1,052.2M;
  FY2025 10-K Item 7 and the revenue note, `0000886346-26-000018`); a doctor blade "has a life ranging from eight hours to
  two months" (Item 1). Packaging, tissue and paper production in North America and Europe moves slowly; the graphic
  grades in structural decline are "Approximately 4% of our revenue in 2025" (Item 1A). (2) The capital-equipment cycle,
  "Approximately 29% of our revenue in 2025" (Item 1A), which is "variable and hard to predict" and tied to housing (wood
  processing, 22% of revenue), mining and Chinese paper capacity. (3) Acquisitions, which the company names "a
  significant driver of our long-term growth" (Item 1). The first variable is foreseeable within a range; the second is a
  cycle, not a trend, and the range absorbs it; the third is a capital-allocation question (Q3, Q6), not a forecast of
  the industry.
- **Would the insiders write it down?** **[M2000-105]** Yes for the aftermarket: the company states it expects "steady
  demand for our aftermarket parts to continue in 2026" and gives annual revenue guidance (8-K exhibit 99.1,
  `0000886346-26-000049`); the forecast here is about mill operating rates, not a technology race. No fast-moving
  technology decides the ten-year economics; Item 1A names factory digitalization and AI only as areas where larger
  rivals "may be able to adapt more quickly".
- **Doubt test** **[M2002-092]**: the part that matters most (Flow Control, Q2) is a consumables-on-installed-base
  business whose economics are legible from ten years of filings; the capital-equipment parts are cyclical but readable.
  Important and knowable **[M2006-076]**.
- **VERDICT: IN.** The ten-year economics turn on mill and plant operating rates and the replacement cycle of worn parts,
  which can be pictured from the filings **[M2012-065]**, **[M2011-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**.

**The parts table** (CONVENTION of the framework, Q2's business of parts: a part decides at more than half of five-year
operating profit, or else the largest). Segment operating income as filed, before corporate expense of $32.9M to $44.5M a
year, FY2021 to FY2025 (FY2021 and FY2023 from the FY2023 10-K segment note, `0000886346-24-000026`; FY2022 from the same
note; FY2024 and FY2025 from Note 11 of the FY2025 10-K, `0000886346-26-000018`):

| part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Flow Control (fluid handling; doctoring, cleaning and filtration) | $65.5M | $89.9M | $95.2M | $91.6M | $92.8M | $435.1M | 44.6% | consumables and critical parts on an installed base; see below | **yes, the largest** |
| Industrial Processing (wood processing; fiber processing; from 2025 boiler cleaning; from 2026 Kadant Profil) | $66.6M | $89.8M | $69.3M | $86.6M | $67.7M | $380.0M | 38.9% | not judged (does not decide) | no |
| Material Handling (conveying and vibratory; baling; fiber-based granules) | $17.5M | $27.6M | $40.7M | $34.1M | $41.2M | $161.2M | 16.5% | not judged (does not decide) | no |

No part carries more than half, so the largest, Flow Control, decides. The file closes on it. Industrial Processing and
Material Handling are not shown open on any evidence read; they are carried into Q7 inside the consolidated owner cash.
Lumping the parts "impedes analysis" **[L2008-005]**, which is why the margins below are read part by part.

**The deciding part's record, from the filings** (Flow Control segment, gross margin and segment operating margin; FY2018
to FY2020 from the FY2020 10-K, `0000886346-21-000021`; FY2021 from the FY2021 10-K, `0000886346-22-000018`; FY2022 and
FY2023 from the FY2023 10-K; FY2024 and FY2025 from the FY2025 10-K; H1 2026 from the 10-Q, `0000886346-26-000052`):

| year | FC revenue | organic change (filer's) | FC gross margin | FC segment operating margin |
|---|---|---|---|---|
| FY2018 | $248.0M | | 50.8% | 21.3% |
| FY2019 | $250.3M | +4% | 51.4% | 22.1% |
| FY2020 | $225.4M | **-9%** | **52.9%** | **22.9%** |
| FY2021 | $288.8M | +15% | 51.0% (1.1 points of acquired-inventory step-up) | 22.7% |
| FY2022 | $349.1M | +18% | 52.0% | 25.8% |
| FY2023 | $363.5M | +4% | 51.8% | 26.2% |
| FY2024 | $371.2M | -1% | 52.5% | 24.7% |
| FY2025 | $382.9M | 0% | 52.3% | 24.2% |
| H1 2026 | $198.9M | | 52.6% (53.6% in H1 2025) | 24.6% (25.1% in H1 2025) |

**The castle tests, each with its filing fact.**
- **Pricing power and the price behaviour** **[M2005-020]** ("you learn a lot about the durability of the economics of a
  business by observing the behavior of — the price behavior"). In FY2020, the one year in the table in which the
  segment's volume fell (organic -9%), its gross margin rose, to 52.9% from 51.4%, which the filer ties to "a greater
  proportion of higher-margin parts and consumables revenue and improved margins on capital equipment revenue, as well as
  benefits received from government employee retention assistance programs" (FY2020 10-K). Through the steel and tariff
  inflation of 2022 to 2025 the margin stayed between 51.8% and 52.5%; the 10-K says Section 232 steel tariffs are 50% and
  that the company mitigates them "through pricing and sourcing strategies". In the deeper downturn of 2009, before the
  segment existed as reported, the product lines that now make it fell hard (fluid-handling revenue -35%, doctoring
  "accessories" -24%, water-management -36%; FY2009 10-K, `0001193125-10-058296`), and the gross margin of the one
  segment that then held them was 40% against 42% in 2008: volume fell a third, price held within two points.
- **Would the customer still choose it over the low bid?** **[M2017-009]**, **[M2016-006]** ("where people don’t simply
  just take the low bid in order to get this gadget"). The parts are worn components of running machines: "A typical
  doctor blade has a life ranging from eight hours to two months" (FY2025 10-K Item 1). When customers deferred capital in
  2025 they kept buying parts: "While customers delayed large capital expenditures, the demand for our parts and
  consumables products was strong and represented a record 71% of revenue in 2025"; "customers continue to invest in
  maintenance and mission-critical equipment" (Item 7). The filer names its own competitive factors, with "Relative price"
  sixth of seven (Item 1, Competition). This is the filer's own account, a seller's (foundations); the margin record is
  the independent half of the evidence.
- **Small, specialized markets** **[M2011-017]** ("very small markets that aren’t really too attractive to anybody with
  any sense to enter, and fanaticism in service"), **[M1997-071]** ("they’re of a size and have specialized skills that
  other organizations just can’t get into it"). Flow Control is a $383M segment whose filer calls itself "a leading
  supplier of systems and equipment in each of our product lines within our Flow Control segment" (Item 1), selling rotary
  joints, syphons, doctor systems and blades into an installed base it describes as "one of the largest installed bases of
  equipment in the markets we serve around the globe" (Item 1).
- **The attacker with money** **[M2011-015]**. Item 1A: "Our competitors include a number of large multinational
  corporations that may have substantially greater financial, marketing, and other resources than we do", and
  "competition, especially in China, has increased as new companies enter the market". The attackers exist and have the
  money; the segment's margin did not fall across eight years of their attack, which is the evidence the test asks for.
- **Ask the competitors** **[M2017-012]**. The rival's own filing names the threat: Albany International writes that
  "Some of the MC’s paper machine clothing competitors also supply paper machines, papermaking equipment, and aftermarket
  parts and services, and often bundle machine clothing products with original or rebuilt machines and/or aftermarket
  services" (AIN 10-K FY2025, `0001628280-26-012906`). The machine builders who bundle are the marauders at Kadant's gate
  too. Written down as contrary evidence **[M1997-127]**. So is the latest half-year: Flow Control's gross margin fell to
  52.6% from 53.6% "primarily due to lower margins achieved on our parts and consumables products" (10-Q MD&A,
  `0000886346-26-000052`), one point in a half-year, inside the eight-year band but on the parts themselves.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Segment operating margin from 21.3% (FY2018) to 24.2% to
  26.2% (FY2022 to FY2025); the company's parts share from 66% of revenue (FY2024) to 71% (FY2025). The moat has not
  narrowed on the figures; whether it widened or the mix moved is not separable from the filings read.
- **What could destroy, modify or reduce it** **[M2000-014]**. (1) Mill closures in mature markets: "In certain European
  markets, excess production capacity and declining demand have resulted in the closure of several mills" (Item 7), and
  "Ongoing mill closures, production curtailments, and merger activity have contributed to weak market conditions in the
  pulp and paper industry" (Item 7). A closed mill buys no blades. (2) Graphic grades in decline, 4% of revenue (Item 1A).
  (3) Bundling by machine builders (above). (4) Chinese competitors (Item 1A). None of the four shows in the margin
  record yet; slow change "can lull you to sleep easier" **[M2014-038]**.
- **The brand, unit volume and the low-cost position** are not the source of this castle on the filings: the company
  competes on "technical expertise, product innovation, and product performance" (Item 1) and reports no unit volumes.

**The competitor row** (CONVENTION of this run: the FY2025 10-K names no rival; a text search of it for "Valmet",
"Andritz", "Voith", "Metso" and "competitor" found only generic mentions. Chosen: the SEC filers that sell consumables to
the same paper machines. Valmet, Andritz and Voith, the machine builders, do not file with the SEC and are flagged; Xerium
stopped filing after its FY2017 10-K). Same metric: segment operating income on segment revenue.

| company, part | 2007 | 2008 | 2009 | 2010 | 2016 | 2018 to 2025 | source |
|---|---|---|---|---|---|---|---|
| Kadant, Papermaking Systems (then the only segment, with stock preparation) | 13.8% | 13.0% before a $40.3M goodwill charge | 4.7% | 14.3% | | | FY2009 10-K `0001193125-10-058296`; FY2010 10-K `0001193125-11-069984` |
| Kadant, Flow Control | | | | | | 21.3% to 26.2% | as above |
| Albany International, Paper Machine Clothing / Machine Clothing | 14.0% | 11.6% before a $48.6M goodwill charge | 6.8% (after $85.9M of restructuring, idle-capacity and other costs) | | | 28.1% (2023), 24.5% (2024), 22.1% (2025) | AIN 10-K FY2009 `0001144204-10-012663`; FY2025 `0001628280-26-012906` |
| Xerium Technologies (machine clothing and roll covers), whole company, income from operations | | 6.7% after removing a $40.0M curtailment gain | 9.8% before an $80.6M goodwill charge; a prepackaged chapter 11 proposed in the FY2009 10-K | | 9.8% | | XRM 10-K FY2009 `0001193125-10-068115`; FY2016 `0001287151-17-000013` |

**The field's returns over the last full cycle, judged in words** (CONVENTION of the framework: "ordinary" carries no
figure). Over 2007 to 2010 the paper-machine consumables field earned modest margins that fell to single digits in the
trough, and the most indebted participant went to a prepackaged reorganization. Since then the two filers still filing,
Kadant's Flow Control and Albany's Machine Clothing, have earned segment margins in the twenties, and Flow Control did so
on segment assets of $451M including $140M of goodwill (FY2025 Note 11; goodwill by segment in the 10-Q), a pre-tax
return of about a fifth on all the segment's assets and far more on its tangible ones. These are not ordinary returns.
That is a change for the better relative to the last deep cycle, and the framework credits such a change only on a full
cycle in which the price behaviour held **[M2005-020]**, **[L1995-022]**. My reading of the record: the segment's volume
fell in FY2020 and its gross margin rose; its organic volume was flat to down in FY2024 and FY2025 and its margin held
above 24%; and in 2009, when the same product lines fell by a quarter to a third, the gross margin of the segment holding
them held within two points of the prior year. The price behaviour held in each fall the filings show. The honest limit:
no fall the size of 2009's has been seen by Flow Control as a reported segment with today's margin, and the operating
margin in 2009 did collapse, through fixed costs, not price.

- **VERDICT: IN.** The deciding part's castle stands on the evidence: customers keep buying worn critical parts when they
  cut capital, the price behaviour held through every volume fall the filings show **[M2005-020]**, the markets are small
  and specialized **[M2011-017]**, **[M1997-071]**, and the returns it protects are not ordinary **[L2007-004]**. The
  threats (mill closures, bundling by machine builders, Chinese entrants) are carried, not dismissed **[M2000-014]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**. The capital is "the
capital actually needed in the business" **[M2010-090]**; goodwill is set aside when judging the business and counted when
judging the buying, "because we paid for it" **[M2011-060]**.

- **Return on the capital the business needs (FY2025, 10-K `0000886346-26-000018`).** Total assets $1,712.2M less goodwill
  $555.6M, intangibles $350.4M and cash $119.6M, less the liabilities that carry no interest (current liabilities $228.2M
  excluding $3.1M of current debt, deferred income taxes $62.5M, other long-term liabilities $59.1M) leaves net tangible
  operating assets of about **$340M**. Operating income before the amortization of acquired intangibles, backlog and
  inventory step-up was $157.3M + $27.4M + $0.9M + $1.5M = **$187.1M** (Item 7 reconciliation). That is about 55% pre-tax
  on the tangible capital the business uses. Flow Control alone earned $92.8M on segment assets of $450.9M that include
  its goodwill (Note 11). By the measure the speakers name, "return on tangible assets" **[M2011-060]**, this is the
  first grade of business or close to it **[M1998-081]**: little capital in, much cash out.
- **Reinvestment to stand still and to grow.** Capital spending $31.9M, $21.0M, $17.0M (FY2023 to FY2025) against
  depreciation of $14.8M, $20.5M, $22.9M; FY2023 included $7.4M for a new Chinese plant, built after local authorities asked the company
  to relocate a facility (Item 7 note (e); Item 1A). The plan for 2026 is $23M to $27M (Item 7).
  Capital spending runs at about 2% of revenue and close to depreciation, so the maintenance need is about the capital
  spending itself; the filing gives no split between maintenance and growth spending, and none is invented here
  **[M2000-144]**, **[L1999-024]**. Working capital other than cash was about $194M at FY2025 (working capital of $313.8M
  less cash of $119.6M, Item 7), about 18% of revenue, so organic growth needs some working capital, not much fixed
  capital.
- **What the added capital earns: the acquisitions** **[M2001-019]**. Cash paid for businesses, FY2017 to FY2025:
  $204.7M, $0, $177.8M, $7.1M, $144.0M, $3.5M, $0.9M, $300.3M, $190.0M = **$1,028.3M** (cash-flow statements of the
  10-Ks read), plus $170.1M for Kadant Profil on 2026-04-30 (10-Q). Operating income rose from $45.6M (FY2016,
  `0000886346-17-000054` as tagged) to $157.3M (FY2025), an increase of $111.7M, part of it organic. On the price paid
  the purchases have therefore earned at most about 11% pre-tax as reported, about 13% before the amortization of the
  acquired intangibles, which is roughly 8% to 10% after the company's 26% to 28% tax. Measured on all the capital,
  goodwill included, the whole company earned about 9% after tax in FY2025 ($157.3M x (1 - 27.8%) = $113.6M on equity
  $979.8M plus minority $11.3M plus debt $374.5M less cash $119.6M = $1,246.0M), about 11% with the amortization added
  back. The engine is excellent on its own capital; the capital added to it by purchase earns a decent, not a high,
  rate: "Most of the great businesses generate lots of money. They do not generate lots of opportunities to earn high
  returns on incremental capital" **[M2003-120]**.
- **The growth arithmetic and its caps.** Organic revenue grew 15%, 15%, 6%, -2% and -4% in FY2021 to FY2025 (the filer's
  organic tables in each 10-K), about 3.5% a year from FY2021 to FY2025; reported revenue grew about 7.5% a year over the
  same span, the difference bought. Nothing in Q3 caps the growth below the sovereign.
- **WEIGHS FOR** on the business: a high return on the tangible capital it needs and capital spending near depreciation
  **[M2011-060]**, **[M1998-081]**. Carried to Q6: the purchases, which over FY2021 to FY2025 exceeded the owner cash
  before them ($638.7M against $621.8M, Q7), earn a decent rate on their price and not the rate the base business earns **[M2001-019]**, **[M2003-120]**.
  (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** ("I like to look at balance sheets
  over an 8 or 10 year period before I even look at the income account"). From `tools/run.py`'s ten-year table (first-filed
  XBRL vintage, accessions `0000886346-17-000054` to `0000886346-26-000018`), FY2025 checked against the filed statement
  (equity $979.8M, goodwill $555.6M, cash $119.6M, all as filed); revenue from the same 10-Ks; $ millions:

| year-end | revenue | equity | goodwill | intangibles | equity less goodwill and intangibles | debt on the face | cash | receivables / revenue | inventory / revenue | retained earnings |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2016 | 414 | 283 | 151 | 53 | 79 | 66 | 71 | 16.0% | 13.3% | 321 |
| FY2017 | 515 | 331 | 268 | 133 | -70 | 241 | 75 | 17.5% | 16.5% | 343 |
| FY2018 | 634 | 373 | 258 | 113 | 2 | 174 | 46 | 14.7% | 13.6% | 394 |
| FY2019 | 705 | 426 | 336 | 174 | -84 | 298 | 67 | 13.6% | 14.6% | 435 |
| FY2020 | 635 | 495 | 352 | 161 | -18 | 233 | 66 | 14.5% | 16.9% | 479 |
| FY2021 | 787 | 564 | 397 | 199 | -32 | 270 | 91 | 14.9% | 17.0% | 552 |
| FY2022 | 905 | 654 | 385 | 176 | 93 | 201 | 76 | 14.4% | 18.1% | 661 |
| FY2023 | 958 | 774 | 392 | 159 | 223 | 111 | 104 | 14.0% | 16.0% | 763 |
| FY2024 | 1,053 | 847 | 479 | 279 | 89 | 289 | 95 | 13.5% | 13.9% | 860 |
| FY2025 | 1,052 | 980 | 556 | 350 | 74 | 375 | 120 | 15.1% | 19.7% | 946 |

  **What the figures are saying.** Equity more than tripled while equity less purchased goodwill and intangibles stayed
  near zero in every year: what was kept and what was borrowed went into businesses bought, not into plant. Debt rises
  with each purchase (FY2017, FY2019, FY2021, FY2024, FY2025, and $510.6M at 2026-07-04 after Profil, 10-Q) and is paid
  down between them (to $111M in FY2023). Receivables move with revenue, between 13.5% and 17.5%. Inventory moved from
  13% to 18% of revenue in FY2016 to FY2022, back to 14% in FY2024, and to 19.7% at FY2025; the FY2025 figure includes
  $39.7M of inventory acquired with Babbini and Clyde (purchase-price allocation, FY2025 10-K), whose sales are in the
  year for only one and two quarters; without it, about 16%. Inventory "out of line with sales" is the tell
  **[M1995-064]** to look at twice; looked at, it is explained by purchases, and in H1 2026 inventory fell by $1.2M in the
  cash-flow statement (10-Q). Other current assets $47.2M to $49.0M (FY2025, 10-Q), no build-up. **What they don't say:**
  how much of the goodwill would survive a 2009; the FY2025 10-K's impairment test was qualitative only ("Step 0"), and
  $85.5M of accumulated impairment losses already sit in Industrial Processing's goodwill (10-Q goodwill table). **What
  they can't say:** the maintenance share of capital spending (Q3).
- **The real costs.** Depreciation is charged and capital spending runs near it (Q3), so depreciation is "almost always
  true costs" **[L2015-004]** and is covered by deducting all capital spending. Amortization of acquired intangibles
  ($27.4M in FY2025) is mostly customer relationships ($115.1M of the $154.0M of intangibles bought in 2024 and $80.5M of the
  $92.7M bought in 2025, purchase-price tables of the FY2025 10-K), which "arise through purchase-accounting rules and are clearly not real expenses" **[L2012-003]**; product
  technology may truly deplete. Owner cash at Q7 starts from operating cash flow, which carries no amortization, so the
  question is settled by construction. Stock pay ($11.2M in FY2025) is deducted **[L2021-003]**. Acquisition costs
  ($1.4M, $2.9M, $4.4M in FY2023 to FY2025) recur every year for a serial acquirer and are left in. Restructuring is small
  ($0.4M in FY2025, $0.8M in FY2023).
- **EBITDA and the adjusted figures in the filer's own mouth.** Every release headlines "Adjusted EBITDA" and "Adjusted
  EPS" beside GAAP ("Adjusted EPS increased 26% to a record $3.42", "Adjusted EBITDA increased 30% to a record $68 million";
  Q2 2026 release, `0000886346-26-000049`). "Free cash flow" is defined as operating cash flow less capital spending
  (Item 7), before stock pay and before the purchases that drive the growth. On 2026-02-19 the company changed its
  "methodology" for adjusted EPS to add back the amortization of acquired intangibles, and on 2026-02-23 filed the recast
  (8-K exhibit 99, `0000886346-26-000015`): FY2025 adjusted EPS of $9.26 as reported on 2026-02-18 became $11.01, FY2024's
  $10.28 became $11.92, back to FY2021. The recast was applied to every year, so the year-on-year change was not flattered
  (-10% before, -8% after), and the full reconciliation was filed. "a management that regularly attempts to wave away very
  real costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; here the cost added back is
  largely one the speakers themselves call not real **[L2012-003]**, and the GAAP figure stands beside it in every release.
- **Guidance and the habit of making the numbers.** Annual and quarterly guidance in every results release
  **[L2019-006]** ("the scourge of earnings "guidance""). The record, from the releases: FY2024 guidance of $1.040B to
  $1.065B revenue and $9.75 to $10.05 adjusted EPS (`0000886346-24-000022`) against $1.053B and $10.28 (beat); FY2025
  guidance of $1.040B to $1.065B and $9.70 to $10.05 (`0000886346-25-000003`) against $1.052B and $9.26 (missed, reported
  as "adjusted EPS decreased 10 percent"). Not a record of consistently reaching declared targets **[L2002-041]**.
- **VERDICT on the accounts: IN.** The statements are clear, reconciled and not suspect: no build-up of prepaid or
  deferred accounts, inventory explained by purchases, no reserves that move, GAAP shown first in the filings
  **[M1995-064]**. **WEIGHS AGAINST** on the featured adjusted figures, the adjusted-EPS redefinition and the guidance,
  carried to Q5 as evidence on the people **[M1994-018]**, **[L2016-006]**, **[L2019-006]**. The recast earnings for Q7:
  operating cash flow less stock pay, all capital spending, finance-lease principal and dividends to minority partners.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* the team took a business that lost
  money at the operating line in FY2009 (-$0.5M on $225.6M, FY2009 10-K) and runs it at $157.3M of operating income on
  $1,052.2M (FY2025), with the deciding part at 24% to 26% segment margins and gross margins held through FY2020 (Q2). The
  rival filer in the same mills, Albany's Machine Clothing, made a similar journey (Q2's competitor row), so part of the
  improvement is the field's, not only the managers'. *How they treat the owners:* read from the proxy, "see how they
  treat themselves versus how they treat the shareholders" **[M1994-009]**: chief executive pay $5.5M (2025), $6.1M (2024),
  $6.0M (2023) (Summary Compensation Table, DEF 14A `0000886346-26-000027`) against net income attributable to Kadant of
  $102.0M, $111.6M, $116.1M; directors and officers as a group own 1.3% of the shares (150,509 shares), the chief executive
  66,531; stock ownership guidelines with a 50% hold of vested RSUs; hedging and pledging prohibited; a clawback policy.
  One related-person item, disclosed: an executive officer's son employed at a subsidiary, paid about $255,952 since
  2025-01-01 (proxy).
- **The tells, from the record read.** No legal proceedings ("Not applicable", 10-K Item 3); internal control over
  financial reporting assessed effective at FY2025 (Item 9A). The FY2025 release told the bad news plainly: "GAAP EPS
  decreased nine percent to $8.65 compared to $9.48 in 2024, and adjusted EPS decreased 10 percent to $9.26"
  (`0000886346-26-000011`), the kind of telling owners "when you make mistakes" **[M2010-081]** that the rows ask for, and
  the 10-K's MD&A explains the year segment by segment in plain language **[M1998-036]**. Against that, the habits carried
  from Q4: guidance every quarter, adjusted figures in the headlines, and the adjusted-EPS methodology changed on 2026-02-19, the day after
  the release that reported a year below its guidance, with the 2026 cash incentive plan amended to "permit adjustment for intangible asset
  amortization expenses" in line with it (proxy). Read with the rest: the redefinition was filed with a full recast of
  every year back to FY2021, did not flatter the year-on-year change, and adds back a charge the speakers themselves treat
  as not a real expense for customer relationships **[L2012-003]**; the 2025 bonus paid on the EPS metric at a factor of
  0.52 for a 9.22% decline, so the plan did not hide the bad year. These are "things that they do in public in relation to
  their investors and the promises they make" **[M2004-067]**; on the record read they raise a preference against, not a
  doubt about honesty.
- **Succession.** Planned and internal: the 8-K of 2026-09-10 (`0000886346-26-000055`) names Michael C. Colwell, who ran
  Industrial Processing and before that was chief executive of Carmanah Design and Manufacturing until Kadant bought it in
  2013 (10-K Item 1), president and COO
  from 2026-10-01 and CEO from 2027-01-02; Jeffrey L. Powell stays as executive chairman, part-time, at half his base
  salary to 2028-01-01. The chief financial officer has been with the company or its predecessor since 1993 (Item 1). An
  heir from inside who ran a business the company bought and then a whole segment is the answer the succession question looks for
  **[M2014-059]**; whether he allocates capital as well is unknown until he does.
- **VERDICT on integrity: IN.** No fact read raises a doubt about honesty **[M2013-088]**; the adjusted-figure habits weigh
  against at Q4 and here, and are not a doubt on this record. **Ability WEIGHS FOR**: the record against the hand dealt
  **[M1994-008]**, the plain account of a bad year **[M2010-081]**, an internal succession **[M2014-059]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test.** "any time we thought that we weren’t going to get more than a dollar of value per dollar
  retained, that, obviously, would be the course to follow" **[M1994-061]**; "test number one" **[M1998-033]**. Kadant keeps
  almost everything: dividends of $15.8M in FY2025 ($0.34 a quarter) against owner cash of about $124M (Q7), and the rest,
  with borrowing, goes into purchases. The company states the policy: "a significant driver of our long-term growth will
  be the acquisition of businesses" (Item 1). Over FY2021 to FY2025 net purchases of $638.7M exceeded the owner cash before
  purchases of $621.8M (Q7), so the programme is the main use of the money. What the dollars retained have earned: about
  8% to 10% after tax on the price of the businesses bought (Q3), above the 5.43% bond and below what the base business
  earns on its own capital; "what is smart at one price is dumb at another" **[L2011-003]**, and the record gives no sign of
  a price discipline beyond the outcome. Each purchase was paid in cash, none in shares, so the narrower STOP on an
  all-stock deal in undervalued stock does not arise.
- **Buybacks.** None since FY2015 ($15.1M in FY2014, $9.9M in FY2015; cash-flow statements). A $50.0M authorization is
  renewed each year and unused: "We have not repurchased any shares of our common stock under this authorization or under
  our previous $50.0 million authorization" (FY2025 Item 7). The buyback test against the bottom of the Q7 range (written back
  with Q7): the bottom is $162 a share (all-equity); no share was bought in the window or since FY2015, so there are no
  prices paid to set against it, and the unused authorization states no price. Nothing weighs here either way.
- **Issuance.** Diluted shares 11.655M (FY2021) to 11.811M (H1 2026), about 0.3% a year from stock pay; no share
  offerings.
- **Part B, the pay.** Annual cash bonus on two adjusted measures, growth in adjusted diluted EPS against the prior
  two-year average and adjusted return on average equity, with the equity metric's target at 8% and its maximum factor of
  2.5 reached at 12% (proxy). In 2025 adjusted EPS fell 9.22% (factor 0.52) and the 11.82% adjusted return on equity
  earned a factor of 2.43, for a weighted 1.48: a bonus above target in a year of falling earnings. Performance RSUs vest
  on adjusted EBITDA (excluding acquisitions made in the year, depreciation, amortization and non-cash pay); 2025 reached
  95.9% of a $231.0M target. "you get what you reward for" **[M2016-083]**: EBITDA in the pay plan is the figure the rows
  call "utter nonsense" **[M1998-086]**; the return-on-equity metric does charge for capital, goodwill included, which is a
  partial cost of capital of the kind the rows ask for **[L1994-019]**, but its 8% target on a business that earns about
  55% pre-tax on its tangible capital sets the bar where a weak manager would put it **[M2004-097]**. From 2026 the
  bonus EPS adds back intangible amortization (Q4, Q5). The board is classified, with supermajority voting for charter and
  bylaw amendments and no right for shareholders to call special meetings (Item 1A). Directors and officers own 1.3%
  (Q5).
- **Part A WEIGHS UNDECIDED**: the money is kept and spent on purchases at a decent rate on their price, in cash, with no
  buyback below value and no issuance **[M1994-061]**, **[L2011-003]**. **Part B WEIGHS AGAINST**: pay on adjusted EBITDA
  and on a low return-on-equity bar, paid above target in a down year **[M2016-083]**, **[M2004-097]**.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**. Arithmetic in `Test Runs/_research 2026-10-16 KAI/scripts/q7.py`, output in
`q7_output.txt` (that output was first computed during the reading and is headed COMPUTATION, NOT A CLEARANCE; it is read
here, after Q1 to Q6).

**The cash, by year** (filed cash-flow lines of the 10-Ks for FY2021 to FY2025, accessions in Step 0; $ millions).
Owner cash, equity-only = operating cash flow less stock pay, all capital spending, finance-lease principal and dividends
to minority partners (working capital is inside operating cash flow, specific (d)). All-equity = the same plus interest
paid less interest received, after the company's own tax rate of that year (24.2%, 26.5%, 26.5%, 26.5%, 27.8%: provision
over pre-tax income).

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year mean |
|---|---|---|---|---|---|---|
| operating cash flow | 162.4 | 102.6 | 165.5 | 155.3 | 171.3 | |
| stock pay | 8.5 | 8.6 | 9.8 | 10.6 | 11.2 | |
| capital spending | 12.8 | 28.2 | 31.9 | 21.0 | 17.0 | |
| finance-lease principal; minority dividends | 1.0; 0.6 | 1.0; 0.6 | 1.1; 0 | 1.2; 1.3 | 1.2; 1.7 | |
| owner cash, equity-only | 139.5 | 64.2 | 122.8 | 121.1 | 140.1 | **117.6** |
| owner cash, all-equity | 142.7 | 68.0 | 127.5 | 134.2 | 149.5 | **124.4** |
| paid for businesses | 144.0 | 3.5 | 0.9 | 300.3 | 190.0 | 127.7 |
| all-equity after purchases | -1.3 | 64.5 | 126.6 | -166.2 | -40.5 | -3.4 |

**The specifics applied.**
- *The serial acquirer* (CONVENTION of the framework, 2026-10-12): net purchases of $638.7M over the window exceed half of
  owner cash before purchases ($621.8M), so the central figure is the **organic pair**: purchases left out, organic growth
  as the filer reports it. The filer's consolidated organic revenue changes were +15%, +6%, -2%, -4% for FY2022 to FY2025
  (and +15% for FY2021 over FY2020), a compound **3.48% a year** from FY2021 to FY2025. The default pair (purchases
  deducted, total growth) is shown beside: its five-year mean is -$3.4M and its series changes sign, so by (b) the halves
  are compared (+$31.6M for FY2021 and FY2022, -$103.3M for FY2024 and FY2025), which is a decline from a figure that is
  itself near zero; it yields no positive value.
- *(a) Cycles:* the filer describes no year of the window as aberrational; FY2021 is a recovery year (organic +15%) and
  FY2022's low owner cash is working capital. The window FY2022 to FY2025 alone gives a mean of $119.8M all-equity, close
  to the five-year $124.4M; the literal window is used.
- *(c) Deals after the window:* Kadant Profil closed 2026-04-30 for $170.1M, financed on the revolver (10-Q). No earnings
  of it are filed, so it is credited at nothing and its debt is in net debt; beside, credited at its price paid, it would
  add $14.4 a share. Babbini and Clyde (2025) are inside the window for part of a year only, and their debt is in net
  debt; the same bias, against the value, is stated rather than corrected.
- *(e) Maintenance:* the filing gives no split of capital spending; capital spending is near depreciation (Q3), so the
  all-spending case is the central one. Depreciation in place of capital spending (FY2023 to FY2025, the years filed
  separately) gives a three-year mean of $140.9M against $137.1M on capital spending: no material difference.
- *(f) The cap:* 3.48% is below the 5.43% sovereign; year-ten owner cash in the growth case would be $175M, about 12% of
  revenue grown at the same rate, below the highest share earned in the filings read (18.1%, FY2021), so no cut.
- *Tax:* the company pays above the statutory rate (27.8% in FY2025, Item 7); the net-operating-loss carryforwards are a
  $11.1M deferred tax asset; no shelter is priced.
- *Net debt* at the latest filed date (2026-07-04, 10-Q): long-term obligations including current maturities and finance
  leases $510.6M less cash $134.5M = **$376.1M**; operating leases left out. Profil's financing is inside it.

**The range** (ten years at the growth shown, then zero nominal growth, discounted at 5.43%):
- All-equity (central): business value $2,290M (no growth) to $3,025M (3.48%), less net debt $376.1M: **$162 to $224 a
  share**. Width 1.32 to one.
- Equity-only (beside): $2,165M to $2,860M: $183 to $242 a share.
- Against the price of **$264.15**: the price is above the top of the range on both bases.

**The floor, tested first** (CONVENTION of the framework: about ten percent, after the company's own tax). At the price the
business costs $3,495M (market value $3,119.4M plus net debt $376.1M). The expected return on the all-equity owner cash is
**3.6%** in the no-growth case and **4.7%** in the organic-growth case. No case in the range earns the floor at the price;
to earn 10% at this price the owner cash would have to grow about 14.8% a year for ten years and then hold, against 3.5%
shown organically and 7.5% shown with purchases (whose cost the organic pair does not charge). "we don’t want to buy
equities where our real expectancy is below 10 percent" **[M2003-149]**.

- **Value range:** $162 to $224 a share (all-equity, the organic pair) against $264.15. **Closes OUT**: no case earns the
  floor at the price (tested first), and the price is above the top of the range.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$88 a share** on the all-equity basis (the no-growth case
  at ten percent $73, the growth case at ten percent $102, averaged), after the company's own tax, with net debt of $376.1M
  at 2026-07-04 deducted; the equity-only figure **$113** beside it ($100 and $126 averaged). No cheap price is reported.
- **VERDICT: OUT.** The business is good and the price is not: the expected return at $264.15 is about 4% to 5% on every
  case the filings support, below the floor **[M2003-149]** and below the 5.43% bond itself; a purchase that needs 15% a
  year of growth to clear the floor is nowhere near one that "should scream at you" **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked by the operator; nothing found in the filings read that bears on it).

---
## THE BOX
**OUT at Q7**: the price of $264.15 is above the whole value range of $162 to $224 a share (all-equity, the organic pair;
equity-only $183 to $242), and no case earns the floor of about ten percent at the price (3.6% to 4.7%). Q1 IN, Q2 IN on
the deciding part (Flow Control), Q3 weighs for, Q4 accounts IN and weighs against on the adjusted figures, Q5 integrity
IN, Q6 Part A undecided and Part B against. Reporting figures: fair price $88 (all-equity), $113 (equity-only).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on a later question, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).
- **Q8 (the bond).** The 30-year Treasury par yield was 5.43% on 2026-10-15; the expected return at the price on the
  all-equity owner cash is 3.6% (no growth) to 4.7% (organic growth) (Q7).
- **Q9 (debt and exposures).** Gross debt $510.6M at 2026-07-04 (revolver $502.5M due
  2030-09-26; senior notes $5.0M due 2026 to 2028; finance leases $2.4M; other $0.8M), against cash of $134.5M, of which
  $114.5M is held by foreign subsidiaries (10-Q). "Substantially all of our existing indebtedness bears interest at
  floating rates" (10-K Item 1A). Credit agreement capacity $750.0M plus an uncommitted $200.0M; leverage covenant below
  3.75 to 1, or 4.25 to 1 for four quarters after a material acquisition; leverage ratio 1.33 at FY2025 year-end, before
  Profil (Item 7). Letters of credit and bank guarantees $16.4M (Item 7); banker's acceptance drafts transferred to vendors
  with recourse $12.0M at 2026-07-04 (10-Q). Interest expense is expected "to remain higher than prior-year levels" (10-Q).
  Customer concentration: none above 10% of revenue (Item 1); the two largest OSB customers were 12% of Industrial
  Processing revenue in 2025 (Item 1A). The "little or no debt" criterion **[R1997-001]** is stated for whole businesses
  only.
- **Q10.** Nothing found.
- **Integrity (Q5) was reached and answered; no integrity fact is left unjudged.**

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Step 0,
      the foundations, the standing rule and Q1 went in one commit; every later question in its own.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (a lock file was present in `Screens/_daily/` at the start; not touched); the run is folded into the
      register by the dispatcher (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. Two listings touched blind-listed
      names (a date-filtered listing of `Test Runs/`, and by mistake a listing of another company's research folder);
      both are declared under contamination at the top, file names only, nothing opened or used.
- [x] Every v5 id resolves (checked by `scripts/check_cites.py` in the research folder against `principle_ledger_v5.csv`);
      every filing fact has its accession or names its filing in Step 0; no number without a row or a filing.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost (stock pay, all capital spending, finance-lease principal, minority dividends),
      never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price an aggregator quote,
      flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q2's bundling and parts-margin
      lines, Q4's inventory and goodwill lines); facts for the questions after the stop are under AFTER THE STOP.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its yields, "points over the sovereign" and
      "growth the price assumes" lines were not used.
- [x] `python tools/check_framework.py` PASS before the final commit.
- **One departure from the order, declared:** the Q7 arithmetic (`scripts/q7.py`) was first run during the reading, before
  Q1 to Q4 had closed in the run file. Its output was headed COMPUTATION, NOT A CLEARANCE in the research folder (operator
  rule 3) and nothing from it entered the run file before Q7. The habit risks anchoring the earlier questions on the
  price; I note that Q2 was decided IN with the knowledge that the price was far above value, so the incentive to clear
  the castle (operator rule 9) was, if anything, absent.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The serial-acquirer convention credits "organic growth as the filer reports it"**, but the filer reports organic
*revenue* growth, not organic growth of owner cash; I applied the revenue rate to owner cash, which assumes constant
margins on the organic base, and the text does not say whether that is intended. (2) **The business of parts lets 44.6%
of the profit decide for 100%**: Flow Control decided Q2, and Industrial Processing (38.9%, capital equipment for
housing-driven wood products and Chinese paper capacity, $85.5M of past goodwill impairments) was never judged; the
convention is clear but it means the castle verdict rests on less than half the earnings. (3) **The change-for-the-better
rule assumes a part with a reported record across the last full cycle**; Flow Control has been reported only since the
2018 recast, so the test of 2009 had to be read from product-line revenue and the gross margin of the older, wider segment.
The rule does not say how to treat a recast segment. (4) **The competitor departure** works only where SEC filers sell the
same thing; the rivals that matter most here, the machine builders Valmet, Andritz and Voith, do not file, and the two
filers chosen sell consumables to the same machines rather than the same products. (5) **A deal closed after the window
is credited at nothing while its debt is counted**: Profil cost $170.1M, about 5% of the market value; the asymmetry
lowers the range by about $14 a share, stated beside the figure, but the text gives no symmetric treatment. (6) **Q4 and Q5
do not separate two kinds of adjusted figure**: an add-back the rows endorse (amortization of acquired customer
relationships, **[L2012-003]**) and the waving away of real costs the rows condemn (**[L2016-006]**); Kadant's
redefinition of 2026 is largely the first, published the day after a disappointing year, and the text gives no rule for
weighing the timing against the substance.
