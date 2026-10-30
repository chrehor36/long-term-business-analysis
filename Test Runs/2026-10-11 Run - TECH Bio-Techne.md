# Company Run: Bio-Techne Corporation (NASDAQ: TECH), 2026-10-11
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch
(commit 0289d743).

**Dispatched blind run.** Analyst dispatched by the session that holds the lock (operator rule 10). Working folder
`Test Runs/_research 2026-10-11 TECH/` (notes, fetch and check scripts, `run.py` output, peer table; raw filings in its
gitignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-11, after the run was committed: not held (`PORTFOLIO.md` read for this one ticker; TECH appears in no account, only in the opportunity set).*

**Contamination, declared and not used.** (1) My first directory listing of `Test Runs/` (a name filter for "TECH" and
"techne", run to see whether the dated file already existed) printed the file names
`2026-09-28 Run - TECH Bio-Techne.md` and `_research 2026-09-28 TECH`. So a run of this name exists, dated under v4.1.
I did not open, list inside or search either path. The filter also printed other companies' run file names (MU, AATC, DELL, MRVL, ALKT,
SOFI, MHH, CMT, ST, AIT, KEYS, TCMD, UTI), not opened. Strictly, that filter is a listing of `Test Runs/`, which the blind rule forbids;
it is declared here as a breach of form, not used. (2) The session context showed the last five commit subjects
of the repository (an SPGI run and fold) and a memory index line counting gate-clearers; neither names this company.
Nothing of either is used below.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $72.46 (close 2026-10-09, the last close before this run, as printed by `tools/run.py`; **aggregator, live quote only, flagged**
  under operator rule 5). The price is pinned by a signed cash merger at $73.00 a share (below).
- **Shares by class** from the latest filing's cover: one class, common, **156,818,238** as of 2026-08-17 (10-K for FY ended
  2026-06-30, filed 2026-08-24, accession `0001104659-26-100322`; `python Screens/cover_shares.py TECH`). Checked: the
  balance sheet shows 156,095,113 issued and outstanding at 2026-06-30 (Minnesota company; repurchased shares are retired,
  no treasury line); the merger proxy and the 8-K of the vote give **156,800,296** outstanding at the record date
  2026-08-11 (DEFM14A `0001140361-26-033911`; 8-K `0001140361-26-037450`). The cover count is used; the three agree to
  within 0.5%.
- **Market cap:** 156.818M x $72.46 = **$11,363M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-09 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2026 (period 2026-06-30, filed 2026-08-24, `0001104659-26-100322`): Items 1, 1A, 5, 7, the statements, notes 1,
    13 (segments), 14 (restructuring), the Wilson Wolf note.
  - 10-Ks FY2025 (`0001558370-25-011716`), FY2023 (`0001558370-23-015226`), FY2020 (`0001437749-20-018754`), FY2017
    (`0001437749-17-015711`) for the segment tables, organic growth, cash-flow statements and repurchase notes back to FY2015.
  - Latest 10-Q: quarter to 2026-03-31 (`0001104659-26-056302`), superseded by the 10-K above; no later 10-Q filed.
  - Merger: 8-K of 2026-06-26 (Items 1.01, 5.02; `0001999371-26-013527`); definitive merger proxy DEFM14A filed 2026-08-20
    (`0001140361-26-033911`: background, reasons, Management Projections, Goldman Sachs analyses, interests of officers);
    8-K of 2026-09-14 (`0001140361-26-036499`: the one lawsuit, *Garfield v. Baumgartner et al.*, filed 2026-09-09 in
    Minnesota's Fourth Judicial District, alleging proxy omissions, plus demand letters; the company supplemented its
    disclosures "solely to avoid the nuisance"); 8-K of 2026-09-23 (`0001140361-26-037450`: merger approved, 121,929,544
    for, 1,208,817 against; the advisory vote on merger-related executive pay **failed**, 25,912,275 for, 96,412,306
    against).
  - Proxy: DEF 14A filed 2025-09-19 (`0001308179-25-000599`); 8-K of 2025-11-05 (`0001104659-25-106631`, annual meeting
    votes); the press release of 2022-02-01 (8-K exhibit 99.1, `0001437749-22-002038`) for the stated FY2026 revenue target.
- **One figure cross-checked against the filed statement:** net cash from operations FY2026 **$292,073K** on the filed
  cash-flow statement (10-K `0001104659-26-100322`) against `run.py`'s 292.1; cash **$264,712K** on the filed balance sheet
  against `run.py`'s 265. Both agree.
- `python tools/run.py TECH`, arithmetic lines only (`_research 2026-10-11 TECH/run_py_output.txt`): owner cash, OCF less stock
  pay less capital spending, $195.8M (FY2024), $215.7M (FY2025), $221.9M (FY2026); on the D&A basis $147.0M, $136.1M,
  $152.7M. Stock pay is in each year (tags named). `run.py` found no securities, other stock-pay, intangible or software
  lines inside operating cash. Acquisitions are not in its owner cash; they are added at Q7 from the filed cash-flow
  statements. The D&A basis is not used as maintenance (Q3 says why). Ten balance sheets are printed and read at Q4.

**The merger, stated once.** On 2026-06-25 TECH signed an Agreement and Plan of Merger with Merck KGaA, Darmstadt,
Germany: each share converts into **$73.00 in cash** at the effective time; shareholders approved it on 2026-09-23; closing is
"expected to close by late 2026 or early 2027", subject to regulatory approvals (10-K Item 1). Termination fees: $230.5M payable
by TECH in specified cases, $576.1M by the buyer on a regulatory failure (10-K MD&A). Buybacks are barred while the agreement
is in effect, and so are dividends (10-K Item 1A and Item 5).

## THE FOUNDATIONS (not a gate)
Two foundations bear here. **A share is a business:** at $72.46 against a cash offer of $73.00, the quotation no longer
tells what the business will produce. It says whether a deal closes. The speakers name this kind of security: one "whose value depends not on what the market price does, but whether a given corporate event occurs" **[M2022-057]**. This run
is a purchase run, so it asks what the business is worth to an owner, "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. It
does not price the merger spread, and nothing below is a judgment on it. **Who is paid to tell you:** the merger proxy carries management's ten-year
projections and a banker's capital-asset-pricing discount rate. The rows do not consult projections and ask instead for the
projector's past ones: "I asked that the record of the people who made the projections, their past projections also be presented at the same time" **[M1995-050]**. That record is read at Q1.
**Contrary evidence, written down as found** **[M1997-127]**: (a) in its own Item 1A the company says competition is
increasing, including from "competitors based in low-cost manufacturing locations", and in FY2026 its larger segment's
organic sales fell 1% with "pricing pressures" (10-K MD&A); (b) in 2022 the then CEO wrote that a deal "has the potential to further extend our 2026 revenue target beyond $2 billion";
FY2026 revenue was $1,215M (8-K `0001437749-22-002038`; 10-K); (c) $1,354.7M paid for businesses and the 19.9% Wilson Wolf stake,
net of businesses sold, in FY2017 to FY2026 (Q3), with roughly $1B more committed, while GAAP operating income went from
$151M (FY2016) to $252M (FY2026); (d) the board granted the executives excise-tax gross-ups two days before signing the sale, and the owners voted
the merger pay down 96.4M to 25.9M. Each is weighed where it belongs below.

## THE STANDING RULE
A part-interest bought for cash with no borrowing does not put the buyer at risk of ruin. The rule binds the buyer's
financing and sizing: "We are never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing about TECH engages it; the target's own debt
and the Wilson Wolf commitment are weighed at Q9 if reached.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The lines of evidence, and why these** (the brief's departure: derived from the 10-K, not given). From Item 1, the
business is two segments with different economics, so the first line is **the parts** (segment sales and operating income,
note 13, read back to FY2015). From Item 1A, the risks that bear on ten-year economics are **customer funding** (pharma, biotech
and government research budgets "can fluctuate"), **competition and price** (large multinationals, low-cost entrants,
consolidating customers), and **acquisitions** as a stated growth strategy, including the Wilson Wolf commitment. From
Item 7, the measured facts are **organic growth, segment gross margin, pricing** and the **cash flows**. Those six lines are
followed through Q1 to Q7: parts, funding, competition and price, acquisitions, margins, cash.

**The parts** (note 13; 10-Ks FY2017, FY2020, FY2023, FY2026). Protein Sciences (reagents: cytokines, growth factors, antibodies,
small molecules, cGMP proteins for cell therapy; analytical instruments and immunoassays) and Diagnostics and Spatial Biology
(diagnostic controls and calibrators sold mostly OEM, ACD in-situ hybridisation assays, the Lunaphore COMET instrument,
Asuragen molecular kits). Segment operating income, $M:

| FY | Protein Sciences sales | PS segment op. income | PS margin | DSB segment op. income |
|---|---|---|---|---|
| 2018 | 482.4 | 209.9 | 43.5% | 35.5 |
| 2019 | 543.2 | 240.9 | 44.4% | 10.1 |
| 2020 | 555.4 | 234.9 | 42.3% | 15.0 |
| 2021 | 704.6 | 330.2 | 46.9% | 38.4 |
| 2022 | 832.3 | 377.6 | 45.4% | 49.0 |
| 2023 | 845.7 | 373.7 | 44.2% | 43.0 |
| 2024 | 830.9 | 354.8 | 42.7% | 24.5 |
| 2025 | 870.2 | 370.4 | 42.6% | 21.3 |
| 2026 | 874.6 | 359.4 | 41.1% | 37.7 |

Five-year (FY2022 to FY2026) segment operating income: Protein Sciences $1,835.9M, DSB $175.5M; **Protein Sciences carries
91.3%** and so decides under Q2's business-of-parts convention, which reaches Q1's "matters" (framework, Q1, A holding
company; Q2, A business of parts). The parts are read separately because "lumping them together [...] impedes analysis" **[L2008-005]**.
DSB does not decide; it is the part with the fast-moving technology (spatial instruments, molecular diagnostics) and is
carried to Q7 as an ordinary business at no growth.

**The test applied to the deciding part.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**.
The product's chemistry need not be understood, only "the economic dynamics of the industry" **[M2011-014]**. Those dynamics, from the 10-K:
research consumables sold in small lots to many buyers (no customer over 10% of the segment; "the majority of our products
are shipped within one day of receipt"), made in-house, at a segment gross margin of 75.0% to 76.8% every year FY2019 to
FY2026; demand set by pharma, biotech and academic research budgets; competition from larger multinationals, niche firms
and low-cost entrants; growth bought by acquisition as a stated strategy.

- **Key variables and how predictable** **[M1998-044]**: (1) the volume of research and cell-therapy manufacturing that consumes
  the reagents. Organic sales growth was 4%, 6%, 6%, 9%, 10%, 4%, 22%, 17%, 5%, 1%, 5%, 0% (FY2015 to FY2026; 10-Ks), so it
  swings with funding, and its rate is not foreseeable. (2) The price the segment keeps against rivals: segment
  margin 41% to 47% for nine years, through the boom of FY2021 and FY2022 and the downturn since, so its level has been
  predictable so far, but it has fallen five years running.
- **Do the past statements tell the future ones?** **[M2008-033]** For the margin structure, yes over nine years; for growth, no.
- **How far off could I be?** **[M2011-084]** The insiders' own record answers it. In February 2022 the then CEO wrote that the Wilson Wolf
  agreement "has the potential to further extend our 2026 revenue target beyond $2 billion" (8-K exhibit 99.1,
  `0001437749-22-002038`); FY2026 revenue was $1,215.0M, at least 39% short of the target that sentence presumes.
  The present management's ten-year projections in the merger proxy (FY2026 $1,208M to FY2036 $3,222M revenue) are not used
  **[M1995-050]**, **[M2003-065]**. The test is whether the insiders would write a forecast down **[M2000-105]**. They do write one down, and
  their last one missed badly on growth.
- **Is it important and knowable?** **[M2006-076]** The growth rate is important and not knowable. The castle's level is
  knowable from the filings and is Q2's question.
- **Is the forecast about customers or about technology?** **[M2017-019]**, **[M2023-030]** For the reagent core it is about the customer: whether a
  researcher or a cell-therapy maker keeps buying a validated, cited reagent from a known maker. The technology risk
  sits in the analytical instruments (inside Protein Sciences) and in spatial biology (DSB). The 10-K says success depends "to a large extent, on our ability to
  keep pace with changing technologies"; that sentence is weighed at Q2 (continued invention).
- **Do I doubt it is inside?** **[M2002-092]** I take the doubt seriously and name it: I cannot foresee the growth rate,
  and I cannot judge the newer platforms. Neither decides Q1 for this part. The growth input is the shown growth, never a forecast
  (Q7), and the platforms are a minority of the deciding part. What must be foreseeable is the earning power and position:
  a maker of high-margin research consumables that customers reorder, in a field with named large rivals. I can state those dynamics and test them
  against the record. Whether the position holds is the castle question, and it is put at Q2, not assumed here.

**VERDICT: IN** on the deciding part (Protein Sciences, 91.3% of five-year segment operating income): its economic dynamics
can be stated from the filings and its margin record is long and readable **[M2011-014]**, **[M2012-065]**; the growth rate is not foreseeable and
is not used as a forecast. DSB's fast-changing technology does not decide and is carried at no growth.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.

The question as the rows put it: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years from now" **[M1995-038]**.
The file closes on the deciding part, Protein Sciences (Q1).

**The castle tests, each with its filing fact.**
1. **Key factors and how permanent.** The filer names its own: "We believe our competitive position is strong due to the
   unique aspects of many of our products and our product quality" (10-K Item 1); "we believe we are the world leader in
   providing high quality proteins, both for research use and under current Good Manufacturing Practices"; innovation kept
   largely "as trade secrets, particularly in the Reagent Solutions division". The factors are reputation for quality,
   catalog breadth ("hundreds of thousands of diverse products"), and, for cGMP proteins, a place in customers'
   manufacturing processes. Permanence: the filer itself says "our future success depends, to a large extent, on our ability
   to keep pace with changing technologies and market needs" and launched "over 1,900 new products" in FY2026.
2. **Without the lord.** A catalog of consumables run by managers recruited from the field (the CEO, CFO and both segment
   presidents came from Thermo Fisher or similar companies; 10-K Item 1). No superstar is needed **[M1996-037]**, **[L2007-006]**. Passes.
3. **The money test.** Could a funded attacker take it **[M2011-015]**? The attackers are already inside the walls. The 10-K
   says competitors range from start-ups to "large multinational companies, which may have greater financial, marketing,
   operational, and research and development resources than us", and reports "increased competition in a number of our
   markets as a result of the entry of new companies into certain markets, the entry of competitors based in low-cost
   manufacturing locations, and increasing consolidation". TECH also sells "through a distribution agreement with Thermo
   Fisher Scientific", the largest of those multinationals. Weighs **against**: this is a field where "you better be running very fast" **[M2012-106]**.
4. **Pricing power, the agony before a rise** **[M2005-020]**. FY2026: Protein Sciences segment gross margin fell to 75.0%
   from 75.6%, "primarily attributable to unfavorable product mix and pricing pressure within the segment"; segment revenue
   "was impacted by unfavorable product mix and pricing pressures" (10-K MD&A). Item 1A: customer consolidation has created
   "increased pricing pressure on us". No filing read reports a price rise that held. Weighs **against** in the latest year.
5. **Unit volume.** Protein Sciences organic sales fell 1% in FY2026; company organic growth was 0%, 5% and 1% in FY2026,
   FY2025 and FY2024 (10-K). Volume is flat over three years. Weighs against, on the evidence of a downturn.
6. **The low-cost position.** Not held: the filer competes on quality against "competitors based in low-cost manufacturing
   locations". The castle, if there is one, is quality, not cost.
7. **The brand.** R&D Systems, Tocris, Novus, ProteinSimple; the filer counts "brand name recognition" among the competitive
   factors. Part of the catalog reaches customers through Thermo Fisher. The rows warn that the value of a brand can move to the
   channel: "the value of having the brand moves over to the retailer from the product itself" **[M2001-090]**. The filings read do not show how much of the
   segment goes through that channel. Undecided.
8. **Would the customer still choose it over the low bid?** For the researcher whose weeks of work ride on a reagent,
   and for the cell-therapy maker whose process is qualified on a cGMP protein, the rows' parachute applies:
   "if you were buying a parachute you’d want to take the [...] necessarily take the low bid" **[M2001-014]**; "people don’t simply just take the low bid" **[M2016-006]**. The filer lists
   "price, quality and safety, performance" first among its competitive factors, so price does count. Weighs for, qualified.
9. **Ask the competitors.** Not on the public record; the 10-K names no competitor.
10. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. The segment's own record across a full cycle (table in Q1):
    before the boom (FY2018 to FY2020) operating margin averaged 43.4% and gross margin ran 75% to 77%; at the boom (FY2021,
    FY2022) 46.9% and 45.4%; in the downturn since (FY2024 to FY2026) 42.1% on average, with gross margin 75.0% to 75.7%. So
    the returns held across the cycle within about a point and a half of the pre-boom level. But the operating margin has
    fallen five years running from its peak, and FY2026 is the first year in the MD&As read (FY2017, FY2020, FY2023, FY2025,
    FY2026) that attributes the segment's results to "pricing pressures"; the risk-factor sentence on consolidation and
    "increased pricing pressure" stands in every 10-K read since FY2017. **The castle stood through a full cycle; it is a notch narrower at the end of it.** Contrary evidence, written
    down: sales rose 24% from FY2021 to FY2026 (704.6 to 874.6) while segment operating income rose 9% (330.2 to 359.4).
11. **What could destroy, modify or reduce it** **[M2000-014]**. From Item 1A: research funding (the board itself cited
    "National Institutes of Health funding" and tariffs in September 2025, DEFM14A background); commoditisation by low-cost
    makers; customer consolidation; and for the newer lines, technology change. A reagent catalog is not a business that
    would be terrible without new invention, as is said of drug makers, "if they had never invented any more pharmaceuticals, it would be a terrible business" **[M1999-075]**:
    decades-old proteins still sell, and R&D is 6.6% of segment sales (57.4 of 874.6, FY2026). But the 10-K's own sentence
    about keeping pace is the rows' warning that "A moat that must be continuously rebuilt will eventually be no moat at all" **[L2007-005]**, and it is carried.

**The competitor row** (same metric, each company's own XBRL from its 10-Ks; `_research 2026-10-11 TECH/peers_output.txt`).
The 10-K names **no competitor** in Items 1 or 1A. So I took the peer list in the company's own merger proxy
(Goldman Sachs' "Selected Companies": Agilent, Bruker, Danaher, QIAGEN, Revvity, Thermo Fisher; DEFM14A
`0001140361-26-033911`). From it I chose the three with research-reagent businesses: **Thermo Fisher** (10-K FY2025
`0000097745-26-000018`), **Danaher** (`0000313616-26-000062`), **Revvity** (`0000031791-26-000012`). This is a
**CONVENTION of this run**: the brief's rule takes rivals from the 10-K, which names none. Rationale: the merger proxy is the
filer's own document and names its peers. All three file with the SEC; no named rival is a non-filer. Limitation: these are
whole-company figures, and each rival's reagent line sits inside a larger segment, so the comparison is of fields, not of
reagent lines. Metric: operating income plus amortization of intangibles, as a share of sales and against total assets
less goodwill, intangibles and cash (the "capital actually needed" reading of **[M2010-090]**; a reporting measure of this
run, not a row's).

| | TECH (FY to June) | Thermo Fisher | Danaher | Revvity |
|---|---|---|---|---|
| (OI+amort.)/sales, FY2017 | 29.3% | 21.8% | 20.1% | 16.8% |
| FY2019 | 28.8% | 24.7% | 21.7% | 18.3% |
| FY2021 | 32.5% | 30.1% | 30.3% | 42.4% (year to Jan 2022) |
| FY2023 | 33.1% | 21.5% | 28.0% | 24.2% |
| latest (TECH FY2026; others FY2025) | 25.8% | 21.3% | 26.0% | 24.2% |
| (OI+amort.)/tangible assets ex cash, FY2017 | 37.9% | 34.1% | 40.0% | 30.3% |
| FY2019 | 43.6% | 38.8% | 40.1% | 27.0% |
| FY2023 | 35.8% | 30.7% | 30.2% | 17.4% |
| latest | 30.1% | 26.9% | 28.4% | 30.3% |

**The field's returns over the last full cycle** (section C): every company in the field earned high pre-tax returns on the
tangible capital it needs, through the cycle of 2017 to 2025. The field is not one of ordinary returns, so the OUT for "a
durable castle that protects only ordinary returns" does not apply. TECH sits at or above the field on both measures across
the span, but its lead has narrowed: its return on tangible assets ex cash went from 55.6% (FY2016) to 30.1% (FY2026).

**The parts table** (section B):

| Part | Share of five-year segment operating income (FY2022 to FY2026) | Castle | Decides |
|---|---|---|---|
| Protein Sciences | 91.3% | stands across the full cycle, narrowing (above) | **yes** |
| Diagnostics and Spatial Biology | 8.7% | OEM controls sticky; spatial and molecular lines in fast-changing technology; an $83.1M impairment on the business held for sale in FY2025 (10-K) | no: carried to Q7 at no growth |

**The closest other reading, and why I did not take it.** The rows say "when we see a moat that’s tenuous in any way [...] it’s just too risky. We don’t know how to valuate that, and therefore we leave it alone" **[M2000-019]**,
and "If we can think of very much that can go wrong with them, we just forget it" **[M2000-016]**. Tests 3, 4, 5 and 10 all
point the same way in FY2026, and an analyst could close here TOO HARD on that row. I did not, because nine years of the
segment's record, across a boom and a bust, show gross margin within 75% to 77% and operating margin within 41% to 47%.
That is a castle that has held, not one whose future cannot be read at all. The narrowing is real and is carried to Q7, whose
growth input is the growth actually shown, never a forecast.

**VERDICT: IN**, narrowly, on the deciding part: the castle has stood through a full cycle on the filings **[M1995-038]**,
**[L2007-004]**, and the field earns more than ordinary returns. The money test, the price test and the narrowing (tests 3,
4, 5, 10) weigh against and are carried.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.

The question in the rows: "Has it earned high returns on capital?" **[M1995-051]**, measured on "the capital actually needed in the business" **[M2010-090]**, "return on tangible assets" for the business and goodwill included "In terms of evaluating the job we’re doing in allocating capital" **[M2011-060]**.

- **Return on the capital the business needs.** Operating income plus amortization of acquired intangibles, against total
  assets less goodwill, intangibles and cash (Q2 table; XBRL from the 10-Ks): 34.4% to 55.6% pre-tax in FY2016 to FY2023,
  26.7%, 17.0% and 30.1% in FY2024 to FY2026 (FY2025 carries a $80.5M held-for-sale impairment and a $41.8M litigation charge).
  Capital spending is light: $28.9M to $62.9M a year in FY2022 to FY2026, 2.4% to 5.4% of sales; depreciation of property
  and equipment alone was $29.7M, $31.9M, $34.6M, $36.2M in FY2023 to FY2026 (XBRL `Depreciation`). The base business
  "gives you more and more money every year without putting up anything to get it, or very little" **[M1998-081]** in its
  capital needs, if not in its recent growth. **Weighs for.**
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. The filing allows a maintenance guess: the 10-K
  says capital additions went to "new buildings, machinery, construction in progress, and IT equipment" and that spending
  enables "revenue growth"; FY2020 ($51.7M) and FY2024 ($62.9M) carried facility building. My guess at maintenance is
  depreciation of property and equipment, about $33M a year (FY2023 to FY2026 average $33.1M), against capital spending
  averaging $41.2M in FY2022 to FY2026, so growth capex runs about $8M a year. Working capital has grown faster than sales:
  inventory went from $60M (10.7% of sales, FY2017) to $196M (16.1%, FY2026); receivables from 20.8% to 17.9% of sales
  (run.py balance sheets; read against the filed balance sheet for FY2026). The real reinvestment is acquisitions.
- **What the added capital earned** **[M2001-019]**, **[M2000-065]**. Cash paid for businesses and for the Wilson Wolf stake,
  FY2017 to FY2026, net of businesses sold (filed cash-flow statements): $1,354.7M (FY2017 253.8; FY2018 67.9; FY2019 289.5;
  FY2021 225.4; FY2022 25.0 Wilson Wolf forward contract; FY2023 101.2 Namocell plus 232.0 Wilson Wolf less 17.8 Eminence
  sold; FY2024 169.7 Lunaphore; FY2025 15.0 Spear Bio less 2.4; FY2026 less 4.6). Over the same span owner cash before
  purchases (OCF less stock pay less capital spending) rose from $117.9M (FY2016) to $221.8M (FY2026), **$103.9M a year more
  on $1,354.7M spent, 7.7% after tax, even crediting every dollar of the base business's organic growth to the purchases.**
  Pre-tax, operating income plus amortization rose from $180.0M to $313.7M, $133.7M on the same spending, 9.9%. Against a
  long bond at 5.60% this is a thin return on the money kept and spent. Wilson Wolf in particular: $257M for 19.9%,
  distributions of $7.0M, $7.3M and $6.0M in FY2024 to FY2026 (2.3% to 2.8% cash on the money paid), and the company is bound to
  buy the other 80.1% on 2027-12-31 at "approximately 4.4 times trailing twelve month revenue", or "approximately $1 billion
  plus potential consideration" if Wilson Wolf reaches its second milestone (10-K note 1). Rising earnings bought this way
  are what the rows warn of: "we’re not earning a higher rate of return on capital than we were when we started. We just put way more capital into the business" **[M2023-081]**. **Weighs against.**
- **The growth arithmetic and its caps.** The best grade is growth that needs little capital; the worst is growth bought at "a very low rate of return" **[M1998-081]**. TECH's organic growth
  needs little capital, but its total growth has been bought, and the purchases have earned little more than the bond.
  Q7 deducts them and credits the total growth (convention (c)).

**WEIGHS AGAINST** on balance: for on the capital the reagent business needs **[M2010-090]**, **[M2011-060]**; against on the
capital added, $1.35B of purchases returning 7.7% after tax on the most generous attribution, with about $1B more
committed on the same kind of terms **[M2001-019]**, **[M2023-081]**. (The "little or no debt" criterion is applied at Q9.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.

**The balance sheets first, ten of them** **[M2025-032]** (`run.py` table from first-filed XBRL; the FY2026 and FY2025 columns
read against the filed balance sheet, 10-K `0001104659-26-100322`; $M at June 30):

| | 2017 | 2019 | 2021 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|
| Total assets | 1,558 | 1,884 | 2,263 | 2,639 | 2,704 | 2,558 | 2,587 |
| Equity | 950 | 1,166 | 1,563 | 1,967 | 2,069 | 1,919 | 2,108 |
| Goodwill + intangibles | 1,031 | 1,312 | 1,459 | 1,408 | 1,480 | 1,347 | 1,278 |
| Cash | 92 | 101 | 199 | 181 | 152 | 162 | 265 |
| Receivables | 117 | 137 | 145 | 218 | 241 | 207 | 217 |
| Inventory | 60 | 91 | 117 | 172 | 180 | 189 | 196 |
| Debt (revolver, term loan) | 344 | 493 | 329 | 350 | 319 | 346 | 200 |
| Retained earnings | 799 | 932 | 1,085 | 1,309 | 1,325 | 1,066 | 1,144 |

What moved, and why, "what the figures are saying and what they don’t say" **[M2025-032]**:
- **Equity against goodwill and intangibles.** In 2017 goodwill and intangibles ($1,031M) exceeded all of equity ($950M); in
  2026 they are $1,278M against $2,108M. Equity grew $1,158M in nine years, but retained earnings only $345M: the rest is
  paid-in capital from option exercises and stock pay, the buybacks having been charged to retained earnings (10-K equity
  note). The fall in retained earnings in FY2025 ($1,325M to $1,066M) is the $275.7M of repurchases in a year of $73.4M net
  earnings. So the owners' capital grew mainly through new shares issued to employees, while the buybacks went the other way.
- **Goodwill and intangibles** rose with the purchases (Exosome Diagnostics, Asuragen, Namocell, Lunaphore) and fell with
  amortization and impairment: Eminence $18.7M (FY2022), held-for-sale impairments $22.0M (FY2024) and $80.5M (FY2025;
  cumulative $83.1M on Exosome Diagnostics). Exosome was bought in August 2018 "for approximately $ 251.6 million, net of
  cash acquired, plus contingent consideration of up to $ 325.0 million" (10-K FY2020 `0001437749-20-018754`) and sold in
  FY2026 "for approximately $ 15.0 million, with approximately $ 6.8 million in stock received at closing" (10-K FY2026).
  Wilson Wolf sits in other assets at $230.8M as an equity-method investment.
- **Inventory against sales.** Inventory rose 3.3 times (2017 to 2026) while sales rose 2.2 times: 10.7% of sales to 16.1%.
  Finished goods went from $66.9M (June 2022) to $111.8M (June 2026) while sales were flat after FY2023 (10-K inventory notes
  FY2023 and FY2026), and $6.3M of finished goods is held in other assets as not saleable within twelve months. The filer
  explains supply-chain "safety stock" (Item 1) and instrument lines. This is the tell the rows name: "inventories look out of line, you know, with sales" **[M1995-064]**. I looked twice. A build of slow-moving finished
  reagent and instrument stock in a downturn is consistent with the flat sales; nothing found points to inflated value, and
  the receivables have kept pace with sales (20.8% to 17.9%). Weighs against, not suspicion.
- **Cash and debt** both modest throughout; debt peaked at $493M after the Exosome purchase and is $200M on the revolver at
  June 2026 (10-K liquidity).

**The real costs, recast.**
- **Stock pay** $41.4M in FY2026 (3.4% of sales), $38.0M to $49.0M a year since FY2021; excluded from every adjusted figure
  the company publishes (10-K non-GAAP section: "Stock-based compensation is excluded from non-GAAP adjusted net earnings").
  The rows call it "the most egregious example" **[L2015-003]**. Counted here as a cash cost.
- **Restructuring** in four straight years: $3.8M (FY2023), $12.2M (FY2024), $28.2M (FY2025), $21.1M (FY2026), with FY2026's
  programme "expecting to incur costs related to these actions through fiscal 2027" (note 14), each year excluded from
  the adjusted figures. A recurring cost; the rows: "to tell owners year after year, "Don't count this," when management is simply making business adjustments that are necessary, is misleading" **[L2016-007]**.
- **Impairments and litigation:** above, plus $41.8M of "certain litigation charges" in FY2025, of which $37.2M was a
  binding arbitration award to the former CEO over the expiry date of his options (10-K FY2025 `0001558370-25-011716`).
- **Amortization** of acquired intangibles $61.2M (FY2026 MD&A): largely developed technology and customer relationships.
  Some of it depletes, as software does: "With software, for example, amortization charges are very real expenses" **[L2012-003]**. Owner cash below is built from cash flows,
  so amortization is neither added nor charged; the purchases are charged instead (Q7).
- **EBITDA in the filer's mouth.** Not in the 10-K's headline figures, which are "adjusted" operating margin and EPS. It
  appears in the merger proxy (the premium stated as "26.6x" "Adjusted EBITDA (Core)"), in the Wilson Wolf contract's
  EBITDA milestones, and in the pay plan's "adjusted EBITA" (DEF 14A 2025). EBITDA is the figure the rows call "utter nonsense" **[M1998-086]**.

**The adjusted figure featured, and the targets.** The proxy's letter to shareholders (DEF 14A 2025 `0001308179-25-000599`)
puts the two side by side: "GAAP earnings per diluted share were $0.46, while adjusted EPS was $1.92 per diluted share". The
adjusted figure is 4.2 times GAAP, after excluding stock pay, amortization, restructuring, impairment and litigation. The 10-K
MD&A reports "adjusted net earnings" every year; FY2026 adjusted net earnings $303.3M against GAAP $181.9M and owner cash
$221.9M. The rows: "a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**.
The company also "has from time to time provided limited financial guidance" (DEFM14A) and stated a 2026 revenue target
of about $2 billion (Q1). Predicting growth is called "both deceptive and dangerous" **[L2000-037]**, and guidance is called "the scourge of earnings "guidance"" **[L2019-006]**.
Under the gaps case, section A, these habits are **weighed against here and carried to Q5**. The target was missed by a wide margin,
which is the opposite of the made-every-quarter pattern **[L2002-041]** warns of.

**Owner cash, recast** (filed cash-flow statements; $M): OCF less stock pay less all capital spending, FY2022 to FY2026:
238.2, 177.0, 198.1, 215.8, 221.8 (five-year average **210.2**); acquisitions are charged at Q7. FY2023 is low because of
a $30.2M inventory build, a $24.6M fall in accrued pay, and taxes paid of $88.4M against $30.3M the year before, in the
year of a $37.2M gain on the CCXI stake (cash-flow statement FY2023; XBRL `IncomeTaxesPaidNet`). GAAP net earnings FY2026 $181.9M; adjusted $303.3M; owner cash $221.8M.

**VERDICT on the accounts: WEIGHS AGAINST.** The accounts are readable and reconcile, so there is no confusion **[M1995-063]**,
and no tell in the statements rises to suspicion **[M1995-065]**: the inventory build is explained and the receivables are in
line. Against: the adjusted figure featured, which waves away stock pay and four years of restructuring **[L2016-006]**,
**[L2016-007]**, **[L2015-003]**; the inventory trend **[M1995-064]**; the published target **[L2000-037]**. The habits go to Q5. The
recast owner cash feeds Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.

The people: Kim Kelderman, CEO since 2024-02-01 (at TECH since 2018, before that Thermo Fisher and Becton Dickinson); James
Hippel, CFO since 2014; the board chaired by Robert Baumgartner (10-K Item 1; DEF 14A 2025). The predecessor CEO, Charles
Kummeth, ran the company through the acquisition years and the 2022 target. Two yardsticks: "how well they run the business" and "how well that they treat their owners" **[M1994-008]**.

**The record against the hand dealt** **[M1994-008]**. The hand since FY2023 has been poor for the whole field: biotech funding
fell ("the continued lag in spending by emerging biotech", DEFM14A background, the May 2026 release), and the rivals'
margins fell with TECH's (Q2 table). Against it, TECH grew organically 5%, 1%, 5%, 0% in FY2023 to FY2026, held its segment
gross margin within a point, and sold two losing businesses (fetal bovine serum; Exosome Diagnostics). The capital record
is the weak part: $1.35B of purchases returning about 7.7% after tax (Q3), Exosome bought for $251.6M and sold for about
$15.0M, and buybacks at $57 to $102 a share (Q6). Under Kelderman specifically (two and a half fiscal years) the decisions were
the Lunaphore purchase (closed at the start of FY2024, before he became CEO), the FY2025 buyback of $275.7M at $60.60,
two divestitures, and the sale of the company.

**The habits carried from Q4.** The adjusted figure featured over GAAP in the shareholder letter, stock pay and recurring
restructuring left out of it, and a published 2026 revenue target missed by at least 39% (Q4). Read with the rest of the
integrity record:
- **Candour about bad news.** The FY2026 10-K says plainly that organic growth was nil and that "pricing pressures" hit the
  core segment. It discloses the $37.2M arbitration loss to the former CEO, the $83.1M impairment and the sale of
  Exosome. The rows count a management that "does explain to you in clear terms what’s going on" **[M1994-018]** as a plus, and ask
  "whether the management is telling us about the things that we would want to know about if we owned a hundred percent of the company" **[M1998-036]**. Mostly yes.
- **How they talk about mistakes** **[L2024-003]**. The proxy letter of 2025 describes the Exosome exit as divesting "a CLIA-lab
  service business requiring a dedicated infrastructure that had limited synergies with our core life sciences and diagnostic
  product offering", and calls FY2025 "differentiated performance" and "industry-leading". The word "mistake" does not appear in the
  2025 proxy, the merger proxy or the FY2023, FY2025 and FY2026 10-Ks (text search). A purchase of $251.6M sold for about $15.0M is
  described as a portfolio choice. The letter's language ("EPIC values", "four growth pillars", "dynamic operating environment") reads as the rows'
  "standardized bunch of popular jargon" **[M1998-038]**, and it shows the hand of an investor relations department **[M2007-083]**. Weighs against.
- **Insider dealing, checked.** Every Form 4 filed by TECH insiders from January 2025 to September 2026 was read (62
  filings; `notes.md`). Open-market sales were few and small: the CEO sold 13,392 shares at about $77 in January 2025; two
  directors exercised and sold 17,040 shares each at about $56 in August 2025; one director sold small lots. On 2026-05-05,
  the day before the third-quarter release that took the price from $56.68 to $47.41, the CEO, CFO and General Counsel each
  exercised options struck at $47.60 and had shares withheld at $56.68 (Form 4s `0000914190-26-000088` to `-000090`). They
  sold nothing in the market and kept the net shares through the fall; the exercise gave up the options' time value. I record it as a fact checked and found
  not to be a sale ahead of bad news.
- **How they treat themselves against the owners** **[M1994-009]**. On 2026-06-23, two days before the merger was signed and after
  the buyer's final price was in hand, the Compensation Committee granted the executive officers cash retention bonuses
  ($6.7M in all) and a full gross-up of any excise tax on their merger payments, "plus an amount such that the officer will,
  after payment of all taxes [...] be in the same after-tax position as if the excise tax [...] had not been incurred"; the
  gross-ups are estimated at **$25,390,040**, of which **$16,476,326** for the CEO, whose merger-related pay totals
  **$52,887,509** (DEFM14A, Golden Parachute Compensation). The owners voted that pay down, **96,412,306 against, 25,912,275
  for** (8-K `0001140361-26-037450`). The CEO held 50,968 shares directly in September 2025 (DEF 14A 2025); the rest of
  his stake was options. This is the agency cost the rows name: "the guy favors himself at the expense of the shareholders" **[M1995-109]**.

**Integrity: the doubt confronted.** The rule is "If you’ve got doubts, forget it" **[M2013-088]**. The question here is whether these
facts raise doubt about honesty, or only about how they treat owners, the second yardstick. Every fact above was
disclosed by the company in its own filings, put to the owners' vote, and explained in plain terms. I found no statement
in the filings read that misleads on the figures that matter, and no market sale ahead of bad news. The gross-up is
the worst fact, and it is a pay decision made by the board's committee, which the framework weighs under Q6 Part B and of which the rows
say "There are more problems with having the wrong manager than with having the wrong compensation system" **[M2007-006]**. The contrary reading is
that a gross-up taken from the owners at the hour of the sale shows leaders who "view shareholders as patsies, not partners" **[L2001-002]**, and that
doubt is enough. I do not take it, because that row's case is CEOs who "were urging investors to buy shares while concurrently dumping their own, sometimes using methods that hid their actions" **[L2001-002]**, and nothing here was hidden or dumped. The fact stays on the record for Q6.

**Ability.** The weights: the business was run well operationally through a downturn (margin held within a point and a
half of pre-boom, Q2), and the price obtained from the buyer was raised to $73 by refusing bids of $65, $69, $67 and $69 (DEFM14A).
Against: the capital record (Q3, Q6), the target missed, and the
mistakes not named. The rows ask "how they have allocated capital over time" **[M1994-008]**, and on that test the record is poor. If the CEO's
"talents or motives are suspect, today's value must be discounted" **[L2010-002]**; carried to Q7 as no credit for future
purchases.

**VERDICT on integrity: IN** (no dishonesty found in the filings, the Form 4s or the sale process; the doubt was confronted
above and is not a doubt about honesty) **[M2013-088]**, **[M1994-018]**. **Ability WEIGHS AGAINST**: operations held, capital
was spent poorly, and the owners were charged for the executives' excise tax at the sale **[M1994-008]**, **[M1995-109]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.

### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**, **[R2009-002]**. Five years to June 2026: net earnings FY2022 to FY2026
  $980.8M (XBRL), dividends $251.2M, so $729.6M kept (about $4.70 a share), plus $504M taken in from option exercises
  over FY2016 to FY2026. Market value per share went from $112.57 (2021-06-30, split-adjusted close, **aggregator**) to
  $58.88 unaffected (2026-06-24, the figure in the DEFM14A) and $73.00 in the merger. The market leg fails by a wide margin. The rows warn that the market
  leg misleads when the whole market falls **[R2009-002]**, and the field fell too (Q2). So the intrinsic leg is read from
  what the money bought: purchases earning about 7.7% after tax on the most generous attribution (Q3). At the 5.60% bond
  that is barely more than a dollar for a dollar; at the floor of about ten percent it is less. And the rows warn that "almost any management that wants to retain money is going to rationalize it" **[M1998-110]**. **Weighs against.**
- **Buybacks.** The February 2022 programme "granted management the discretion to mitigate the dilutive effect of stock
  option exercises" (10-K Item 5); the April 2025 programme authorises $500M; neither names a price. The rows say value is "entirely purchase-price dependent" **[L2016-002]**, and of buying to offset dilution they say "It’s got nothing to do with preventing dilution" **[M2016-049]**. Prices paid (10-K equity notes): FY2021 480,000 shares at $89.95;
  FY2022 1,576,952 at $102.06; FY2023 222,000 at $88.12; FY2024 1,397,471 at $57.28; FY2025 4,550,195 at $60.60; FY2026
  909,555 at $45.82. Ten years of buying ($686.6M, FY2019 to FY2026) left the basic share count higher than it started
  (148.8M split-adjusted in FY2016, 156.0M in FY2026; XBRL), because employees were issued more. **Written back from Q7:**
  the bottom of the Q7 range is $25.69 a share (all-equity); every price paid, $45.82 to $102.06, sits 1.8 to 4.0 times
  above it, so the no-price programmes are not rescued by what they paid. Weighs against.
- **Issuance and deals: value given against value got** **[M1995-001]**. Every purchase was paid in cash, so the narrower STOP
  for an all-stock deal in undervalued stock **[L2009-019]** does not arise. The record of what was got: Exosome Diagnostics,
  $251.6M plus up to $325.0M contingent (August 2018), impaired $83.1M and sold for about $15.0M (FY2026); Eminence impaired
  $18.7M and sold for $17.8M (FY2022 to FY2023); Wilson Wolf, $257M for 19.9% with $6.0M to $7.3M a year of distributions,
  and a binding purchase of the rest at about 4.4 times trailing revenue by 2027-12-31 (10-K note 1). No post-mortem of any
  purchase appears in the filings read, though the rows say "Post mortems of acquisitions, in which reality is honestly compared to the original projections, are rare in American boardrooms. They should instead be standard practice" **[L2014-013]**. **Weighs against.**
- **Dividends** $0.32 a share a year, about $50M, steady since FY2021; suspended by the merger agreement. Neutral.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**, and charged for capital **[M1995-010]**. The annual bonus is paid on
  organic revenue and "adjusted EBITA"; the three-year awards on 40% organic revenue, 35% adjusted EBITA and 25% relative
  total shareholder return (DEF 14A 2025). Adjusted EBITA excludes stock pay, amortization of what was bought, and
  restructuring, so the managers are paid on a figure that leaves out the cost of the capital they spend on purchases.
  Shareholders asked for a return-on-invested-capital measure; the Compensation Committee "declined to adopt an ROIC
  performance metric because of the potential to actually discourage such calculated risk-taking" (DEF 14A 2025). The rows: "a batting average that does not include a cost of capital is a phony batting average" **[M1995-010]**. And "if you have a dumb incentive system, you get dumb outcomes" **[M2016-083]**. For the plan: the FY2023 three-year grants "did not vest due to failure to achieve
  three-year payout targets", so it has some teeth, and a cap was added on the shareholder-return metric when returns are
  negative (DEF 14A 2025). **Weighs against.**
- **Options.** Granted at market, with no step-up for retained earnings, the rows' "ten-year option" problem **[L1994-021]**: "the combination of a ten-year option, a low dividend payout, and compound interest can provide lush gains to a manager who has done no more than tread water in his job" **[L1994-021]**.
  Stock pay of $41.4M in FY2026 is 3.4% of sales and 19% of owner cash. **Weighs against.**
- **Heads I win** **[L1994-020]**. At the sale: retention bonuses and full excise-tax gross-ups ($25.4M estimated), granted after the
  buyer's final price was known; the owners rejected the merger pay 96.4M to 25.9M (Q5). At the 2025 annual meeting 39.0M
  shares voted against the pay plan and 100.8M for (8-K `0001104659-25-106631`). The rows' test of reform is "a hard look at their own pay and perks" **[L2002-029]**. **Weighs against.**
- **The board.** Chair and CEO are separate (Baumgartner chairs). Directors are paid $75,000 in cash plus yearly
  grants (1,640 restricted units each in October 2025, Form 4s). Their holdings are mostly grants and options: the chair held
  44,863 shares directly, and six of the nine non-employee directors listed held under 15,000 directly (DEF 14A 2025). The rows prefer directors "purchasing shares with their savings, rather than simply having been the recipients of grants" **[L2019-008]**. On
  the sale itself the board refused four bids below $73 and ran a limited check of two other buyers (DEFM14A). Mixed.

**Q6 WEIGHS AGAINST** on both parts. Part A: retained money spent on purchases that earned about the bond rate, buybacks
with no price and dilution not stopped **[R1995-009]**, **[L2016-002]**, **[M1995-001]**. Part B: pay on adjusted figures with
no charge for capital, options without step-up, and gross-ups at the sale **[M1995-010]**, **[L1994-020]**, **[L2002-029]**. The
narrower STOP does not arise: no all-stock deal **[L2009-019]**.

## Q7: WHAT IS IT WORTH? STOP.

The question: how many birds, how sure, how soon, at "the yield on long-term U.S. bonds" **[L2000-021]**; value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, crediting "whatever net cash is left every year" **[M1998-080]** after asking "are you going to have to put more cash into after you buy it?" **[M2014-068]**.
Arithmetic: `_research 2026-10-11 TECH/q7.py`, output `q7_output.txt`. All figures $M from the filed cash-flow statements
(10-K FY2023 for FY2022 and FY2023; 10-K FY2026 for FY2024 to FY2026), interest paid from XBRL.

**The cash input (Q4's recast, all-equity basis).** Owner cash = operating cash flow less stock pay less all capital
spending, plus Wilson Wolf distributions (the equity-method convention: dividends received are the cash counted), plus
interest paid after tax, which puts it on the all-equity basis. **CONVENTION of this run:** interest is taken after tax at 25%; rationale: the filer's
"long-term GAAP tax rate" is 23.5% to 26.3% in FY2024 to FY2026 (10-K MD&A) and no row supplies a rate. Owner cash is
after the company's own tax, with no conversion (Q7, Whose tax; no carryforward running out inside ten years was found).

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | 5-yr avg |
|---|---|---|---|---|---|---|
| Owner cash, equity-only, before purchases | 238.2 | 176.9 | 205.1 | 223.0 | 227.9 | **214.2** |
| Owner cash, all-equity, before purchases | 246.4 | 183.2 | 215.9 | 237.3 | 238.7 | **224.3** |
| Businesses bought, net of sold (incl. Wilson Wolf) | 25.0 | 315.4 | 169.7 | 12.6 | -4.6 | **103.6** |
| Owner cash, all-equity, after purchases | 221.4 | -132.1 | 46.2 | 224.7 | 243.3 | **120.7** |

**The specifics, applied.**
- **(a) Cycle base.** The window runs from the boom year FY2022 (17% organic growth) into the downturn. The filer does not
  call either end year aberrational in the documents read, so the literal window is the base. A base reaching back a full
  cycle would take in a smaller, pre-purchase business and only lower the figure.
- **(b) and (f) Growth shown.** After purchases the series changes sign, so growth is measured between the halves of the window:
  44.6 (FY2022 and FY2023) to 234.0 (FY2025 and FY2026), 73.7% a year. That is the absurdity the rows warn of: "if you trace out the mathematics of it, you bump into absurdities, then you better change expectations somewhat" **[M1999-067]**. Cut by (f) to the business's own sales growth over the window,
  **2.39% a year** (FY2022 $1,105.6M to FY2026 $1,215.0M). Owner cash before purchases shows **-0.79% a year** (246.4 to 238.7).
- **(c) Purchases.** Deducted, with the total growth credited (the default pair). After year ten the growth stops and so do
  the purchases: the terminal value is on owner cash before purchases (section E, 2026-10-10).
- **(d) Working capital** is inside operating cash flow and so is counted (the FY2023 inventory build included).
- **(e) Maintenance and the inversion.** The filing allows a maintenance guess: property and equipment depreciation, about
  $33.1M a year, against capital spending averaging $41.2M (Q3), so the maintenance-only case adds $8.1M. The growth bought
  is worth less than its cost: the purchases-deducted growth case ($25.69 a share) is below the no-purchase, no-growth case
  ($26.87). So by (e) the maintenance-only no-growth case is the **top** and the growth case the **bottom**. That inversion
  is the finding, "growth can destroy value if it requires cash inputs in the early years [...] that exceed the discounted value of the cash that those assets will generate in later years" **[L2000-023]**.
  The case "purchases deducted, no growth" ($21.00) charges the spending and also caps the growth it bought, which (e) forbids;
  it is shown in `q7_output.txt` and not used.
- **The Diagnostics and Spatial Biology part** is inside the aggregate cash and carried at the same rates. It does not
  decide (Q2).
- **The signed, unclosed deal, beside.** The purchase of the remaining 80.1% of Wilson Wolf is bound but not closed. Wilson
  Wolf files nothing, so its own record is read through TECH's equity-method income: $0.9M of share of income plus $10.0M of
  basis amortization implies about $54.5M a year at 100% (an earnings figure, generous as cash). At a price of 4.4 times the
  first-milestone revenue of about $92M for 80.1% ($324M), the bottom moves to $28.59; at the 10-K's "approximately $1
  billion", to $24.28 (financing added to net debt). Neither touches the box.

**Value range (all-equity, owner cash before interest against market value plus net debt; net debt at 2026-06-30 is
$200.0M revolver less $264.7M cash = net cash $64.7M; operating leases left out; the 10-K states "SUBSEQUENT EVENTS None"):
$25.69 to $26.87 a share against $72.46.** Equity-only beside: $23.89 to $25.31. Width 1.05 to 1. The literal window is
shown above. The most generous case I could defend, with no purchases, the filer's own organic growth of 5.43% a year
(FY2022 to FY2026, boom year included) and maintenance-only capital, gives $41.15.

**Closes.** The floor is tested first **[M2003-149]**: at $72.46 the expected return by case is 1.8% to 2.3% on the range's
cases and 3.3% on the most generous, against about ten percent pre-tax (CONVENTION, the floor) and against the long bond
at 5.60%. **No case earns the floor at the price, so the file closes OUT whatever the width**. The rows say "there’s just a point at which we drop out of the game" **[M2003-149]**. The
narrow range would close OUT anyway, the price sitting far above its top, so there is no screamer **[M2009-005]**.

**Fair price** (a reporting figure, never a verdict; Part VII): each end case valued at ten percent and the two averaged,
per share. **All-equity $13.96** (the ends $12.69 and $15.23), **equity-only $12.85** (the ends $11.52 and $14.18); owner
cash after the company's own tax. No cheap price is reported.

**VERDICT: OUT**: the price of $72.46 sits about 2.7 times the top of the range ($26.87), and no case earns the floor
**[M2003-149]**, **[L2013-012]**. The price is the merger's; the business at that price is what Q7 judges (Foundations).

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED** (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (No business of the kinds the rows name was found in the filings read.)

---
## THE BOX
**OUT**, decided at **Q7**: no case earns the floor of about ten percent at $72.46 (expected return 1.8% to 3.3% by case);
**value range $25.69 to $26.87 a share (all-equity; equity-only $23.89 to $25.31) against $72.46**. Q1 IN, Q2 IN (narrowly),
Q3 against, Q4 against, Q5 integrity IN and ability against, Q6 against. The price is pinned by Merck KGaA's $73.00 cash merger,
approved by shareholders on 2026-09-23 and not yet closed.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box is unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond).** Every case's expected return at $72.46 (1.8% to 3.3%) is below the 30-year Treasury at 5.60%
  (2026-10-09, Treasury par yield curve) (`q7_output.txt`).
- **Q9 (debt and sudden demands).** At 2026-06-30: $200.0M drawn on a $1B revolving facility that "matures on August 31,
  2027" (10-K Item 5), cash $264.7M. The Wilson Wolf purchase of the remaining 80.1% is bound for 2027-12-31 at about 4.4
  times trailing revenue, or "approximately $1 billion plus potential consideration" if the second milestone is met; the
  10-K says the payment "is forecasted to occur between fiscal 2027 and fiscal 2028" (10-K note 1 and MD&A). Against
  five-year average owner cash of $224.3M, a $1B payment would take net debt to roughly four years of owner cash. A
  termination fee of about $230.5M is payable by TECH in specified cases (10-K MD&A); the merger agreement bars buybacks and
  dividends while in effect.
- **Q12.** Research reagents, instruments and diagnostic controls; nothing found of the businesses the rows name.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the `cp` ran before `run.py` and before the first EDGAR request); the first
      commit (0289d743) came after the 10-K, merger proxy, 8-Ks and proxy had been downloaded but before any section was
      written. Written question by question; committed after Q1 (2ee1ad6f), Q2 (01b8c003), Q3 (93a9539c), Q4 (cb7a5337),
      Q5 (35eb03d5), Q6 (05ad69e4) and Q7 with the box (this commit), each with a pathspec of the run file and research
      folder only.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's (operator rule ten). The run
      binds nothing until it is folded into the register.
- [ ] **The blind rule: one breach of form, declared.** My first `ls "Test Runs" | grep` listed `Test Runs/` with a name filter,
      which showed that a 2026-09-28 TECH run file and research folder exist and printed thirteen other companies' run file
      names. Nothing was opened, listed inside or searched, and nothing was used (Contamination, at the top). No holding
      review, `PORTFOLIO.md`, resume-state, queue, reading-list or unadopted case file was opened.
- [x] Every v5 id resolves (`check_quotes.py`: all ids in `principle_ledger_v5.csv`, every quoted fragment beside an id found
      in that row, no E-ids); every filing fact carries its document and accession; numbers carry a filing or a CONVENTION label.
- [x] The order was kept: Q1 to Q6 answered in order, Q7 the first STOP that failed; Q8 to Q12 not reached; nothing after
      Q7 is a clearance. Q6's buyback line was written back from Q7 in the same commit.
- [x] Owner cash after every real cost from the filed cash-flow statements (stock pay charged, purchases charged), never a
      net-income proxy; sovereign from the Treasury; the price and the 2021 historical close are aggregator quotes, flagged.
- [x] Contrary evidence written down as found (Foundations, Q2 test 10, Q2's closest other reading, Q5's doubt confronted).
- [x] Not a point-in-time run; no anchor applies.
- [x] Only the arithmetic lines of `tools/run.py` were used (prices, shares, filed figures and sums); nothing it prints as a
      rule, id or verdict.
- [x] `python tools/check_framework.py` run before this commit (result recorded at the end of the file).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **(c) against (e) at Q7.** Convention (c) makes the default pair "purchases deducted, total growth credited", and (f)
   cuts an absurd shown growth to sales growth. Together they charge all of the purchase spending and also cap the growth
   it bought, and (e) says never to do that. The text does not say how the two combine, nor whether the no-growth end of
   the default pair still deducts purchases. I used (e)'s inversion: the top is the no-purchase, maintenance-only, no-growth
   case and the bottom is the purchases-deducted growth case. I did not use the case that deducts purchases at no growth
   ($21.00), and I name it here so the dispatcher can see what the other reading gives.
2. **(b)'s "halves of the window"** is undefined for a five-year window; I compared FY2022 and FY2023 with FY2025 and FY2026,
   dropping the middle year.
3. **The all-equity add-back of interest** needs a tax rate, and the framework names none; I confessed 25% as a CONVENTION of
   this run.
4. **Competitors when the 10-K names none.** The brief's rule takes rivals from the 10-K, and this 10-K names no competitor.
   I took three from the peer list in the company's own merger proxy and confessed it as a CONVENTION of this run.
5. **A price pinned by a signed cash merger.** The framework has nothing on running a purchase run on a workout. The row
   **[M2022-057]** names the kind; I valued the business, as the template asks, and the Q7 close was then mechanical. A line
   saying whether such names are run at all, or run with the deal price set aside, would save a run.
6. **Q2: a narrowing inside a high-return band.** The framework gives a full-cycle rule for a change for the better
   (TOO HARD (NATURE) until a downturn) but none for a castle that held across a cycle and is slipping at its end. Whether
   "tenuous in any way" **[M2000-019]** reaches it is left to judgment; I took IN and wrote the other reading down.
7. **Q5: integrity against the second yardstick.** The line between the integrity STOP and the treatment of owners, which Q6
   Part B weighs, is not drawn. An excise-tax gross-up granted at the sale sits exactly on it. I read "integrity" as honesty,
   following the tells the rows list, and carried the gross-up to Q6. Another analyst could read **[L2001-002]** as reaching it,
   and the file would then close at Q5. The box would still be OUT.

**Acceptance test.** `python tools/check_framework.py` run 2026-10-11 after Q7 was written: **PASS** (every check, including
phantom ids across every run file). `_research 2026-10-11 TECH/check_quotes.py`: **PASS** (no E-ids; every M, L and R id in
`principle_ledger_v5.csv`; every quoted fragment set directly before an id found in that row).
