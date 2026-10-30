# Company Run — Nordson Corporation (Nasdaq: NDSN) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, written by the analyst on 2026-10-10. The template was copied
to this file before any fetch. Working folder: `Test Runs/_research 2026-10-10 NDSN/` (raw filings and XBRL under its `cache/`
subfolder, which is ignored; `fetch.py`, `facts.py`, `competitors.txt` and `check_quotes.py` are committed).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared** (the brief's blind rule): (1) the session opened with a git status snapshot that names, as file
paths, other companies' run files dated 2026-10-10 (Mastercard, MSA Safety) and research folders of other names (AYI, ARCB),
and five commit subjects of other companies' runs (LOW, LOPE, LRCX, LSTR) with their boxes; none concerns Nordson and none
was opened. (2) The memory index loaded with the session carries a line on the queue (counts of gate-clearers, "nothing
buyable"); it names no company. (3) The lock file in `Screens/_daily/` was read to confirm the dispatcher holds it; it reads
"interactive v5 re-runs batch 8" and names no company. (4) The dispatch message says earlier Nordson run files exist; their
names, dates and contents were not seen. (5) Added during Q3: the session's scratchpad directory is shared with another
dispatched analyst; a change notice displayed, unasked, that analyst's draft Q3 for another company (a card network:
capitalized customer incentives, acquisitions, a WEIGHS FOR verdict). It concerns no Nordson fact; drafts of this run were
moved to file names of their own (`ndsn_*.md`) and the run file was checked to contain only this run's text. Nothing of
these is used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $328.17 (close 2026-10-09; aggregator quote through `tools/run.py`, flagged per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: one class, Common Shares without par value, **55,699,366** as of
  2026-08-18 (10-Q for the quarter ended 2026-07-31, filed 2026-08-20, accession `0000072331-26-000054`;
  `python Screens/cover_shares.py NDSN` agrees). Check against issued less treasury: 98,023 thousand issued at 2025-10-31
  and 2026-07-31 (both balance sheets); the 2025-10-31 balance-sheet count of 55.920M outstanding puts treasury at about
  42.1M shares, and the nine months' buybacks (shareholders' equity statement, 10-Q) move the count to the cover's figure.
  No 8-K or prospectus was filed after the 10-Q (submissions index read on 2026-10-10: the 10-Q of 2026-08-20 is the
  latest filing; the last 8-K, 2026-08-19, is the results release). No charter note is needed: one class.
- **Market cap:** $328.17 × 55.699M = **$18,279M**.
- **Sovereign for the earnings currency:** USD (the XBRL unit of the cash-flow series; about 67 percent of sales are outside
  the United States, 10-K FY2025, but the accounts and the dividends are in dollars) **5.60%**, US Treasury daily par yield
  curve, 30-year, 2026-10-09 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025 (year to 2025-10-31), filed 2025-12-17, accession `0000072331-25-000144`: Item 1, Item 1A in part,
    MD&A, the statements, Notes on acquisitions, segments (Note 15), cash-flow supplement.
  - 10-Q for the quarter to 2026-07-31, filed 2026-08-20, accession `0000072331-26-000054`: the statements, Acquisitions
    (CapstanAG, March 2026), Investments, segment EBITDA, organic sales table, Item 2 repurchase table.
  - Proxy DEF 14A for the 2026 meeting, filed 2026-01-16, accession `0001193125-26-014662` (pay design, read at Q6).
  - 8-Ks: 2026-08-19 (results; Exhibit 99.1 press release), accession `0000072331-26-000052`; 2026-06-02 (new $1.2
    billion commercial paper programme), accession `0000072331-26-000034`; 2026-01-30 (amended $1,200 million revolving
    credit facility to 2031), accession `0000072331-26-000005`.
  - The cycle, from earlier 10-Ks: FY2010 `0000950123-10-114569` (2008 to 2010), FY2013 `0001193125-13-474384` (2011 to
    2013), FY2016 `0001564590-16-030237` (2014 to 2016), FY2019 `0001564590-19-045927` (2017 to 2019), FY2021
    `0000072331-21-000079` (2019 to 2021), FY2022 `0000072331-22-000185` (2020 to 2022), FY2023 `0000072331-23-000242`,
    FY2024 `0000072331-24-000177` (2022 to 2024). Segment tables read from each.
  - **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $719,175
    thousand on the filed Consolidated Statement of Cash Flows (10-K FY2025, `0000072331-25-000144`), against 719.2 printed by
    `tools/run.py` from the tagged data: agrees. Also checked: FY2025 capital spending $58,060 thousand, depreciation $71,259
    thousand and amortization $79,264 thousand on the same statement against the tool's 58.1 and 150.5 (D&A combined): agree.
- `python tools/run.py NDSN`, arithmetic lines only (its rule lines, ids and floor are not used, Part VII): owner cash
  (operating cash less stock pay less capital spending) FY2023 $584.0M, FY2024 $472.8M, FY2025 $642.2M; on the D&A basis
  $506.7M, $401.1M, $549.7M. Five-year window (FY2021 to FY2025) means: $523.0M (capital-spending basis), $451.8M (D&A
  basis). Capital spending FY2023 to FY2025 $34.6M, $64.4M, $58.1M against D&A $111.9M, $136.2M, $150.5M (D&A is mostly
  amortization of purchased intangibles: $59.7M, $77.0M, $79.3M, the filed cash-flow statement). Stock pay $22.7M, $19.0M,
  $18.9M, resolved from the filed statement ("Non-cash stock compensation"); no other stock-pay line found. Finance-lease
  principal $6.8M, $6.1M, $5.9M (financing section) is a capital payment outside capital spending and is added back in at
  Q7. Q7 rebuilds owner cash from the filed statements; the tool's figures are not used as the Q7 input.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety: at $328.17 the tool's own arithmetic puts the owner-cash
yield (2.5 to 3.1 percent) below the 5.60 percent bond, so any case for the name has to come from growth, and "if you have
to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. The second is who is paid to
tell you: the company's results release leads with adjusted earnings per share and a record EBITDA, and gives guidance
(Exhibit 99.1, `0000072331-26-000052`); the speakers' instruction is to ask whether the speaker is paid more for one
answer than another **[M2020-037]**, and to answer a forecast with "So what?" **[M2000-095]**. No macro view enters
**[M2000-094]**: the semiconductor up-cycle now lifting the electronics segment (ATS organic sales up 30.9 percent in the
quarter, 10-Q) is weighed as a property of that part, not as a forecast. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the company paid $4,625M for businesses, net of cash acquired, from FY2011 to the third quarter of FY2026, against
$28M received net in FY2025 (cash-flow statements; tagged series checked against the FY2025 filed statement) and twice wrote acquired businesses down hard (a goodwill and long-lived asset impairment in FY2009 that turned
the Advanced Technology segment's operating profit to a loss of $214.4M, 10-K FY2010; an $87.4M impairment in FY2020 on the
screws-and-barrels line it then sold, 10-K FY2021); (2) goodwill of $3,316M and intangibles of $626M exceed shareholders'
equity of $3,269M at 2026-07-31 (10-Q); (3) the filings give no figure for the parts-and-consumables share of sales, the
one number that would show the installed base paying (see Q2); (4) segment profit has been reported, from FY2025, as an
EBITDA that excludes the amortization of purchased intangibles (Note 15, 10-K FY2025).

## THE STANDING RULE
A part-interest bought for cash in the market with no borrowing and no position size that could force a sale puts the
buyer at no risk of ruin; the rule binds the buyer's financing and sizing, not the target **[M2012-081]**, **[L2014-024]**.
The target's own debt ($1.73 billion of borrowings at 2026-07-31, including $192M short-term and a commercial paper
programme of up to $1.2 billion opened 2026-06-02) is weighed at Q9, not here. No borrowed money: "borrowed money has no
place in the investor's tool kit" **[L2014-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** Equipment, components and spare parts that dispense, apply and control
  adhesives, coatings, polymers, sealants and fluids, test and inspect electronic assemblies, and make single-use plastic
  medical components; sold mainly direct, in more than 35 countries; no customer at 10 percent of sales; 67 percent of
  sales outside the United States (10-K FY2025, Item 1, `0000072331-25-000144`). Three reported segments: Industrial
  Precision Solutions (IPS: hot-melt and other adhesive dispensing for packaging, nonwovens and product assembly,
  industrial coatings, polymer processing, precision agriculture), Medical and Fluid Solutions (MFS: engineered fluid
  components, interventional and single-use medical components, Atrion since August 2024), Advanced Technology Solutions
  (ATS: electronics dispense, test and inspection, measurement and control).
- **The parts, and which decides** (Q1's holding-company paragraph, extended to segments by section B of the gaps case;
  the threshold is Q2's business of parts). Five-year segment operating profit, FY2021 to FY2025, from Note 15 of each
  10-K: FY2021 and FY2022 from the FY2022 10-K (`0000072331-22-000185`), FY2023 and FY2024 from the FY2024 10-K
  (`0000072331-24-000177`); FY2025 is reported only as segment EBITDA, so FY2025 operating profit is computed from the
  same note as segment EBITDA less segment depreciation less segment amortization of intangibles (all three filed lines,
  `0000072331-25-000144`; special items stay excluded, as the filer's segment measure excludes them).

  | Segment | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 (computed) | Five-year sum | Share |
  |---|---|---|---|---|---|---|---|
  | IPS | 414.2 | 434.5 | 460.9 | 470.6 | 441.4 | 2,221.6 | 58.7% |
  | MFS | 198.2 | 217.2 | 189.4 | 187.7 | 240.1 | 1,032.6 | 27.3% |
  | ATS | 73.5 | 133.3 | 101.7 | 94.2 | 127.9 | 530.6 | 14.0% |

  ($ millions. FY2025 moved the measurement-and-control division from IPS to ATS, with FY2024 and FY2023 revised in the
  FY2025 10-K; the FY2021 to FY2024 figures above are as first reported, which puts that small division in IPS for four of
  the five years. Either way IPS is above half.) **IPS decides** (more than half of five-year operating profit). The file
  closes on IPS; MFS and ATS are read but do not decide.
- **The test applied to IPS.** Understanding is "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**; the chemistry need not be understood if "the economic dynamics of the
  industry" are **[M2011-014]**. The key variables **[M1998-044]** for IPS are three: (1) the installed base of dispensing
  systems on customers' packaging, hygiene-product and assembly lines, which keeps buying parts and replacement units; (2)
  the customers' own volumes (food and beverage packaging, diapers and incontinence products, appliances, building
  products), which are consumer staples or near them and move slowly; (3) price against the cost of a stopped line. The
  first is stated by the filer in words only, "We also support our customers with parts and consumables, so a significant
  percentage of our revenue is recurring" (10-K FY2019, MD&A outlook, `0001564590-19-045927`; the same sentence in the
  10-K FY2021, `0000072331-21-000079`); no figure for that share was found in any 10-K or 10-Q read (text search for
  "consumable", "parts and", "recurring", "installed base", "aftermarket" in the FY2010, FY2013, FY2016, FY2019, FY2021 and
  FY2025 10-Ks and the latest 10-Q). Do the past statements tell the future ones **[M2008-033]**? For this part, yes in a
  way that is unusual: the adhesive-dispensing segment (Adhesive Dispensing Systems to FY2019, the core of IPS after)
  earned an operating margin between 23.4 and 34.4 percent in every year FY2008 to FY2019, including FY2009, when its sales
  fell 20.7 percent and its margin rose to 27.7 percent (segment tables, 10-Ks FY2010, FY2013, FY2016, FY2019; detail at
  Q2). A ten-year picture drawn from that record is a picture the record supports.
- **Would the insiders write it down** **[M2000-105]**? For IPS, the forecast is about customers' production lines that
  change slowly, not about technology races: the products are dispensers, pumps, nozzles, guns and controllers for hot-melt
  adhesive, sealants and powder coatings, a field the company has led since 1954. **Technology** **[M1998-008]**: there is
  a technological component (controls, software in precision agriculture), but no filing read describes a change that
  could make the installed base obsolete; the risk factors name economic cycles, trade policy, raw materials and
  acquisitions, not substitution (10-K FY2025, Item 1A).
- **The parts that do not decide.** ATS sells into semiconductor packaging and printed circuit boards, an industry whose
  winners ten years out the insiders would not write down **[M2000-105]**; read alone it would close here TOO HARD
  (NATURE). It carries 14.0 percent of five-year operating profit and does not decide. MFS (single-use medical
  components) is understandable as a components supplier to device makers, with procedure volumes as its key variable.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The
  doubt that exists is about price and capital allocation, not about where the adhesive-dispensing business will stand; it
  belongs to Q3, Q6 and Q7.
- **VERDICT: IN.** The deciding part's ten-year economics can be pictured from a seventeen-year segment record that
  includes a deep recession **[M2012-065]**, **[M2008-033]**; the part that could not be (ATS) does not decide.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**. It is asked of the deciding part, IPS (Q1), and of the others for the record.

- **The record of the deciding part through a full cycle** (segment tables; $ millions; operating profit as reported,
  so special charges included):

  | FY | Segment as then reported | Sales | Operating profit | Margin | Source |
  |---|---|---|---|---|---|
  | 2008 | Adhesive Dispensing Systems | 580.7 | 145.4 | 25.0% | 10-K FY2010 `0000950123-10-114569` |
  | 2009 | Adhesive Dispensing Systems | 460.7 | 127.6 | 27.7% | same |
  | 2010 | Adhesive Dispensing Systems | 525.3 | 166.3 | 31.6% | same |
  | 2011 | Adhesive Dispensing Systems | 611.9 | 210.4 | 34.4% | 10-K FY2013 `0001193125-13-474384` |
  | 2012 | Adhesive Dispensing Systems | 684.1 | 211.1 | 30.9% | same |
  | 2013 | Adhesive Dispensing Systems | 793.5 | 203.8 | 25.7% | same |
  | 2014 | Adhesive Dispensing Systems | 899.7 | 229.6 | 25.5% | 10-K FY2016 `0001564590-16-030237` |
  | 2015 | Adhesive Dispensing Systems | 836.1 | 195.9 | 23.4% | same |
  | 2016 | Adhesive Dispensing Systems | 879.6 | 229.1 | 26.1% | same |
  | 2017 | Adhesive Dispensing Systems | 916.0 | 256.8 | 28.0% | 10-K FY2019 `0001564590-19-045927` |
  | 2018 | Adhesive Dispensing Systems | 955.2 | 262.6 | 27.5% | same |
  | 2019 | Adhesive Dispensing Systems | 950.9 | 275.2 | 28.9% | same |
  | 2020 | IPS (adhesives plus industrial coatings) | 1,143.4 | 208.0 | 18.2% (25.8% before the $87.4M held-for-sale impairment of the screws-and-barrels line) | 10-K FY2021 `0000072331-21-000079` |
  | 2021 | IPS | 1,246.9 | 414.2 | 33.2% | 10-K FY2022 `0000072331-22-000185` |
  | 2022 | IPS | 1,337.2 | 434.5 | 32.5% | same |
  | 2023 | IPS | 1,391.0 | 460.9 | 33.1% | 10-K FY2024 `0000072331-24-000177` |
  | 2024 | IPS | 1,484.2 | 470.6 | 31.7% | same |
  | 2025 | IPS (revised, measurement-and-control moved out) | 1,331.8 | 441.4 computed (segment EBITDA 493.9, 37.1%) | 33.1% | 10-K FY2025 `0000072331-25-000144` |

  The segment never earned less than 23 percent of sales on its own reported profit in eighteen years, except FY2020's
  impairment year, and in the recession year its sales fell a fifth while its margin rose. "you can almost measure the
  strength of a business over time by the agony they go through in determining whether a price increase can be sustained"
  **[M2005-020]**; the same row adds "you learn a lot about the durability of the economics of a business by observing the
  behavior of" **[M2005-020]** its prices, and the margin through 2009 is that observation. The growth is the weak side:
  segment sales went from $899.7M in FY2014 to $950.9M in FY2019, about one percent a year with acquisitions inside it;
  IPS organic sales grew 3.8 percent in the nine months to 2026-07-31 (10-Q `0000072331-26-000054`).
- **Pricing through the last inflation.** The filer says it passed cost through: FY2022 gross margin fell from 56.1 to
  55.1 percent, "driven by the impact of passing through inflationary cost increases", while IPS operating margin went
  from 33.2 to 32.5 percent and the company's from 26.0 to 27.1 percent (10-K FY2022 MD&A); gross margin was 55.2 percent
  in FY2024 and FY2025 (10-K FY2025). Passing cost through at cost, not at margin, dilutes the percentage a little and
  keeps the dollars, the behaviour of "the businesses with strong competitive positions" that "manage to pass through
  increases in raw material costs" **[M2005-017]**. The filer's risk factor admits a lag: "there historically has been a
  delay between an increase in our raw material costs and our ability to increase the prices of our products" (10-K
  FY2025, Item 1A). In FY2026 to date IPS segment EBITDA margin fell 190 basis points on "select near-term inflationary
  pressures" and investment (10-Q MD&A): written down here as contrary evidence **[M1997-127]**.
- **The attacker with money** **[M2011-015]**. Graco, a well-funded fluid-handling maker, sells equipment for "moving and
  applying paints, powder coatings, sealants, adhesives and other fluids" in its Industrial segment (Graco 10-K FY2025,
  Item 1, `0000042888-26-000081`), so the money test has a live attacker in the deciding part's own field. The attack has
  not shown in Nordson's adhesive margins, which were 23 to 29 percent in FY2013 to FY2019 and 31 to 33 percent in FY2021
  to FY2025 (table). Graco also warns of "low-cost copies" from Asia that are "increasingly offering" outside Asia (same
  filing, Item 1A); that is the shape of the threat for this field too.
- **Would the customer still choose it over the low bid** **[M2017-009]**? The filer sells on uptime and material saved,
  "solutions that increase uptime, enable faster line speeds, and reduce consumption of materials" (10-K FY2025, Item 1):
  on a high-speed packaging or diaper line the dispenser is small against the line and the adhesive it meters, which is
  the condition of the business "where people don’t simply just take the low bid in order to get this gadget"
  **[M2016-006]**. The evidence that customers act that way is the margin held through 2009, not a filed survey.
- **Unit volume, share of mind, brand.** Not measurable from the filings: no unit counts, no market-share figure, no
  parts share. Recorded as unknown.
- **Ask the competitors.** The rivals in hot-melt dispensing that are not SEC filers (Valco Melton, Robatech, Henkel's own
  dispensing equipment) and ITW's adhesive-dispensing line, which sits inside a larger ITW segment, cannot be asked or
  separated from the public record; flagged.
- **Widening or narrowing** **[M1999-108]**. Margin: widened, from the mid-twenties of FY2013 to FY2016 to the low
  thirties of FY2021 to FY2025, with a dip in FY2026 to date. Sales: slow. The record reads as a castle held and not
  much enlarged, with growth bought rather than grown (Q3, Q6).
- **What could destroy, modify or reduce it** **[M2000-014]**. Low-cost Asian copies of dispensing equipment (the rival's
  own risk factor); a slow shift of customers' packaging away from hot-melt adhesive; customer concentration in hygiene
  products. None is shown in the filings read as happening at scale.

**The competitor row** (same metric, operating income over sales, from each company's own 10-K facts through SEC
companyfacts, latest filed value per period; whole company unless stated; `competitors.txt` in the research folder):

| Company | Latest 10-K accession | Operating margin, mean of FY2008 to FY2025 | Low year | FY2021 to FY2025 range | Note |
|---|---|---|---|---|---|
| Nordson (whole) | `0000072331-25-000144` | 20.5% | -15.6% (FY2009, impairment) | 25.1% to 27.1% | adhesive segment above, 23% to 34% |
| Graco (GGG) | `0000042888-26-000081` | 23.7% | 9.1% (FY2016) | 26.7% to 29.5% | Industrial segment, which holds its adhesive and sealant equipment: 34% FY2025, 33% FY2024 |
| IDEX (IEX) | `0000832101-26-000003` | 19.3% | 6.6% (FY2012) | 20.2% to 23.6% | pumps, flow meters, dispensing |
| Illinois Tool Works (ITW) | `0000049826-26-000008` | 20.9% | 10.2% (FY2009) | 23.8% to 26.8% | adhesive dispensing is a line inside a segment; not separable |
| Dover (DOV) | `0000029905-26-000009` | 14.5% | 11.1% (FY2009) | 15.6% to 17.0% | pumps and process solutions inside a conglomerate |

Non-filers flagged: Valco Melton, Robatech (private), Henkel's equipment business (part of a German group that does not
file with the SEC). Compared over the whole span, Nordson's adhesive segment and Graco's industrial segment both earn
margins in the high twenties to mid thirties, above the diversified rivals.

**The parts table** (section B of the gaps case):

| Part | Share of five-year operating profit (Q1) | Castle | Decides |
|---|---|---|---|
| IPS | 58.7% | stands: margin 23% to 34% every year FY2008 to FY2025 on its own reported profit (25.8% in FY2020 before an impairment), held through a 20.7% sales fall | **yes** |
| MFS | 27.3% | single-use medical and fluid components; margin 28.7% to 31.5% FY2021 to FY2023 (10-K FY2022 and FY2023 MD&A), about 29% FY2025 computed; not tested through a medical down-cycle in this run | no |
| ATS | 14.0% | electronics and semiconductor equipment; margin 15.5% FY2021, 23.7% FY2022, 17.6% FY2023 (10-K FY2022 and FY2023 MD&A); a FY2009 impairment turned its predecessor segment to a $214.4M loss; future cannot be judged | no |

**The field's returns over the last full cycle** (section C). The filer's adhesive segment and the closest filed rival
segment (Graco Industrial) earn excellent, not ordinary, returns on sales over FY2008 to FY2025; Nordson's operating
profit of $711.7M in FY2025 sits on net tangible operating capital of under $1 billion (equity $3,044M plus borrowings and
finance leases $2,010M less cash $108M less goodwill $3,305M less intangibles $682M = $959M; 10-K FY2025 balance sheet),
a pre-tax return on the capital the business needs **[M2010-090]** far above any ordinary figure. A castle that protects
"excellent returns on invested capital" **[L2007-004]** is what the 2007 letter calls a moat; this one is shown on the
filed record. The cost of buying castles (goodwill) is a separate matter, judged at Q3 and Q6.

- **VERDICT: IN.** The deciding part's castle stands on the evidence of a full cycle, including the 2009 recession and the
  2021 to 2023 inflation **[M2005-020]**, **[L1995-022]**; its rivals earn high returns too, so the field is not ordinary
  **[L2007-004]**; the threats named (Asian copies, a well-funded rival in the same field) are written down and not shown
  to be filling the moat **[M2000-014]**. ATS, which alone would be TOO HARD, does not decide and is carried to Q7.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **The capital the business needs** **[M2010-090]**. Capital spending ran $34.6M to $64.4M a year in FY2021 to FY2025
  against depreciation of $49.1M to $71.3M (cash-flow statements; `facts.py` transcription, FY2023 to FY2025 checked
  against the filed FY2025 statement): the plant needs about its depreciation or less, under 2.5 percent of sales. Net
  property, plant and equipment was $516.9M at 2025-10-31 against sales of $2,791.7M. Working capital is the larger need:
  receivables $587.8M and inventories $444.8M less payables $121.0M and customer advances $44.0M is $867.6M, 31 percent of
  sales (10-K FY2025 balance sheet). Operating profit of $711.7M on net tangible capital of $959M (Q2) is a return on the
  capital the business needs that the speakers' best grade describes: "The best business is one that gives you more and
  more money every year without putting up anything to get it, or very little" **[M1998-081]**. The same arithmetic for
  FY2016 (10-K FY2016 balance sheet as printed by `tools/run.py`: equity $852M plus debt $983M less cash $67M less goodwill
  $1,107M less intangibles $260M = $401M against operating profit of $388.4M) shows the high return is old, not new.
- **What the added capital earns** **[M2001-019]**. Total capital (equity plus borrowings and finance leases less cash) went
  from $1,768M at 2016-10-31 to $4,946M at 2025-10-31, up $3,178M, while operating profit went from $388.4M to $711.7M, up
  $323.3M; after the company's own tax (effective rate 18.9 percent in FY2025, 10-K FY2025 income statement) that is about
  $262M a year on $3,178M added, about 8 percent. The company's own measure says the same: its proxy reports return on
  invested capital (net income plus after-tax interest over equity plus net debt) of 12 percent against a 16 percent target
  in the 2024 and 2025 measurement years, which cut the performance-share payout (DEF 14A 2026, `0001193125-26-014662`).
  The added capital went mostly into businesses bought: $2,356M net in FY2022 to FY2025 alone (CyberOptics $377.8M,
  10-K FY2023; ARAG about €957M, 10-K FY2023; Atrion $790.0M net of cash, 10-K FY2024). Organic sales over the same years,
  as the filer reports them: +10.8 percent FY2022, -1.4 percent FY2023, -2.5 percent FY2024, -2.5 percent FY2025 (MD&A of
  each 10-K), under one percent a year compounded. Most of the growth was bought.
- **The growth arithmetic.** The rows' test of rising earnings: "we’re not earning a higher rate of return on capital than
  we were when we started. We just put way more capital into the business" **[M2023-081]**. Here the core earns a very high
  return and the capital added earns about 8 percent after tax, the second of the 1998 grades, a business that grows
  where the rate at which the money is reinvested must be judged **[M1998-081]**, and well short of the core's own rate. The
  speakers accept a second-best return if it is decent on the incremental sums **[L2009-012]**; 8 percent after tax is
  above the bond and below the floor Q7 applies.
- **WEIGHS FOR on the capital the business needs, AGAINST on the capital added; recorded UNDECIDED** **[M1998-081]**,
  **[M2001-019]**, **[M2023-081]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** (`tools/run.py` table, first-filed
  XBRL, FY2016 to FY2025; the FY2025 and 2026-07-31 statements read as filed). $ millions:

  | Year-end | Assets | Equity | Cash | Receivables | Inventory | Goodwill | Intangibles | Debt (current + long-term) | Retained earnings |
  |---|---|---|---|---|---|---|---|---|---|
  | 2016 | 2,422 | 852 | 67 | 429 | 220 | 1,107 | 260 | 983 | 1,933 |
  | 2017 | 3,415 | 1,155 | 90 | 505 | 264 | 1,589 | 547 | 1,583 | 2,165 |
  | 2018 | 3,421 | 1,451 | 96 | 491 | 264 | 1,608 | 500 | 1,314 | 2,488 |
  | 2019 | 3,516 | 1,581 | 151 | 531 | 283 | 1,615 | 446 | 1,244 | 2,748 |
  | 2020 | 3,675 | 1,759 | 208 | 472 | 277 | 1,713 | 408 | 1,106 | 2,909 |
  | 2021 | 3,791 | 2,159 | 300 | 489 | 327 | 1,713 | 357 | 816 | 3,265 |
  | 2022 | 3,820 | 2,294 | 163 | 537 | 383 | 1,805 | 329 | 738 | 3,652 |
  | 2023 | 5,252 | 2,598 | 116 | 591 | 455 | 2,784 | 673 | 1,737 | 3,989 |
  | 2024 | 6,001 | 2,932 | 116 | 595 | 477 | 3,281 | 741 | 2,205 | 4,295 |
  | 2025 | 5,918 | 3,044 | 108 | 588 | 445 | 3,305 | 682 | 1,996 | 4,601 |
  | 2026-07-31 (10-Q) | 5,948 | 3,269 | 113 | 649 | 469 | 3,316 | 626 | 1,731 | 4,867 |

  What moved and why. (1) **Goodwill and intangibles exceed equity in every year** (2016: $1,367M against $852M; 2025:
  $3,987M against $3,044M): tangible equity is negative throughout, because the company bought its growth (Vention Medical
  in FY2017, ARAG and CyberOptics in FY2023, Atrion in FY2024, the steps in the goodwill line) and returned more than it
  kept (treasury stock at cost $2,210M at 2025-10-31). (2) **Debt** rose with each purchase and was paid down between them:
  $1,583M after FY2017, $738M by FY2022, $2,205M after FY2024, $1,731M at 2026-07-31. (3) **Cash** is kept thin, $67M to
  $300M; the company runs on its revolving credit and, since June 2026, commercial paper. (4) **Receivables** moved with
  sales: 23.7 percent of sales in FY2016, 21.1 percent in FY2025. (5) **Inventory** rose faster than sales after 2021, from
  13.8 percent of sales (FY2021) to 17.7 percent (FY2024), and came back to 15.9 percent (FY2025); the release shows in
  operating cash (cash-flow statements: inventories provided $46.6M in FY2024 and $34.6M in FY2025). The filer's releases
  of FY2024 call the backlog "concentrated in systems businesses" as it normalized (2024-02-21, 2024-05-20). (6) **Retained earnings** rose from $1,933M to $4,601M, $2,668M kept over nine
  years after dividends. What the figures "don’t say and what they can’t say" **[M2025-032]**: the parts-and-consumables
  share of sales, the installed base, and segment returns on the capital paid for each acquisition.
- **The real costs.** Depreciation is a true cost **[R1996-023]**, and capital spending ran below it in three of the five
  years (Q3), so the capital-spending basis of owner cash may flatter the business slightly; Q7 shows the D&A basis beside
  it. Stock pay of $18.9M to $30.7M a year is deducted **[L2015-003]**. Amortization of purchased intangibles ($79.3M in
  FY2025) is not cash; the purchases themselves are charged at Q7 as capital spending, which is where their cost belongs,
  though software and technology amortization "are very real expenses" **[L2012-003]**. Restructuring recurs: severance and
  other $5.5M, $17.3M, $19.3M in FY2023 to FY2025 and a $12.5M divestiture charge in FY2025 (Note 15), all inside GAAP
  operating profit and inside owner cash. A pension settlement charge of $24.0M in FY2026 (10-Q) is a real cost of the
  promises made.
- **EBITDA in the filer's own mouth.** The results release heads with "Third quarter EBITDA reached an all-time quarterly
  record of $262 million", features "Adjusted earnings per diluted share were $3.25", which exclude "acquisition-related
  amortization and costs" and the loss on a minority investment (Exhibit 99.1, `0000072331-26-000052`), and raises guidance
  every quarter of FY2026 (releases of 2026-02-18, 2026-05-20, 2026-08-19); the proxy's first financial highlight is
  "EBITDA" of "$900 Million A Nordson Record" and an EBITDA margin is 30 percent of the performance-share award (DEF 14A
  2026). The segment measure itself became EBITDA in FY2025 (Note 15). The speakers: "The one figure we regard as utter
  nonsense is the so-called EBITDA" **[M1998-086]**, and an adjusted figure featured "makes us nervous" **[L2016-006]**. Here
  the business's capital spending is genuinely small (Q3), so EBITDA overstates owner cash less than at most companies; the
  habit is still the habit. Weighed against and carried to Q5.
- **The tells** **[M1995-064]**: no prepaid or deferred account building (prepaid and other current assets $101.8M at
  2025-10-31, $96.3M at 2026-07-31); inventory out of line with sales for three years and since reversed; no reserve moves found; the auditor (Ernst & Young) gives clean opinions on the statements and internal control
  (10-K FY2025); no restatement and no material weakness found (text search of the FY2025 10-K). Guidance has been cut as
  well as raised (FY2023 narrowed to 0 to 2 percent growth from 1 to 7 percent; FY2024 cut to flat to 2 percent from 4 to 7
  percent; FY2025 first-quarter sales "at the low end of our guidance range"; releases of 2022-12-14, 2023-08-21,
  2024-02-21, 2024-05-20, 2025-02-19), so the record is not one of targets always met **[L2002-041]**.
- **VERDICT on the accounts: IN.** The statements are readable and consistent; nothing in them confuses or raises suspicion
  **[M1995-063]**. **WEIGHS AGAINST** on the habits: EBITDA and adjusted earnings featured, quarterly guidance **[L2016-006]**,
  **[L2019-006]**, **[M1994-018]**; carried to Q5. The recast owner cash feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Sundaram Nagarajan, President and Chief Executive Officer since 2019, age 63 (10-K FY2025, executive officers);
  an independent Chair of the Board (Victor Richey, Jr.) separate from the chief executive; nine of ten directors
  independent (DEF 14A 2026, `0001193125-26-014662`). For a marketable stake the speakers read rather than meet
  **[M2007-081]**; this is a reading.
- **The two yardsticks** **[M1994-008]**. (1) *How well they run the business, against the hand dealt*: the adhesive
  segment's margins rose under this management from 28.9 percent (FY2019) to 31 to 33 percent (FY2021 to FY2025), and
  company operating margin from 22.0 to 25.5 percent (Q2), while organic sales growth since FY2022 has been weak (Q3); the
  rival with the nearest segment (Graco Industrial) did about as well, 33 to 34 percent (Q2), so the hand was good and was
  played well. (2) *How they treat the owners*: a dividend raised for the 62nd consecutive year (proxy highlights),
  buybacks with no stated price (Q6), pay that fell when return on capital missed (performance shares paid 65 percent of
  target for 2023 to 2025, the ROIC leg at 46 to 52 percent; DEF 14A 2026).
- **The habits carried from Q4**, read with the integrity record **[M2004-067]**. Against: EBITDA and adjusted earnings
  featured in every release and in the proxy's first highlight, and quarterly guidance **[L2016-006]**, **[L2019-006]**.
  For: the record is not one of targets always met **[L2002-041]**; guidance was cut in FY2023, FY2024 and FY2025 and the
  releases said so in plain words ("weakness across multiple end markets", "sales performance at the low end of our
  guidance range", release of 2025-02-19, `0000072331-25-000030`). The 10-K states the opposite of a quarterly
  obsession in its own purpose: "Each quarter, we may not produce increased sales, net income, or earnings per share, or
  exceed the comparative prior year's quarter. When short-term swings occur, we do not intend to alter our foundational
  objectives" (10-K FY2025, Item 1). The adjusted figure excludes acquisition amortization, which is the industry's
  common practice and is reconciled to GAAP in each release; it flatters an acquirer, and the 10-K and the release both
  show the GAAP figure first in the tables.
- **The tells of dishonesty** searched for and not found: no restatement, no material weakness, no investigation, no
  related-person transaction beyond ordinary sales to directors' other companies at under 1 percent (DEF 14A 2026); one
  late Form 3 explained by an EDGAR code delay; legal proceedings ordinary and not material (10-Q, Part II Item 1). The
  reports name the industry's key figure poorly: the parts-and-consumables share is described ("a significant percentage
  of our revenue is recurring", 10-K FY2019 and FY2021) and never quantified **[M2007-082]**; recorded, not read as
  dishonest, since the figure has never been given.
- **How they talk about mistakes.** The FY2020 impairment of the screws-and-barrels line ($87.4M) was called an "assets
  held for sale impairment charge" and the line sold; the FY2025 sale of the medical contract-manufacturing business came
  with a $12.5M charge (10-K FY2021, 10-K FY2025). The MFS segment leader left in April 2025, after the Atrion purchase and
  a year of MFS organic decline (8-K 2025-04-29, `0000072331-25-000043`). No filing read uses the word "mistake" of an
  acquisition **[L2024-003]**; recorded as a weighing on ability, not as a tell.
- **Love of the business.** Not readable from the filings beyond the long tenure of the operating leaders (an executive
  vice president retiring after "an incredible 40 year career with Nordson", DEF 14A 2026) and the founding family's
  continued holdings in trusts (Nord family trusts named in the beneficial-ownership notes, DEF 14A 2026).
- **VERDICT on integrity: IN.** The record leaves no doubt of honesty **[M2013-088]**: the accounts are clean (Q4), bad
  quarters are reported as bad, and guidance is cut when it is missed. **Ability WEIGHS FOR** on running the business
  **[M1994-008]**, with the capital-allocation record weighed at Q6.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**. Market leg, by the filer's own cover-page measure: the market value
  of shares held by non-affiliates was about $4,357M at 2016-04-30 (10-K FY2016 cover, `0001564590-16-030237`) and about
  $10,705M at 2025-04-30 (10-K FY2025 cover), a rise of about $6,348M, against earnings kept after dividends of $2,556M in
  FY2016 to FY2024 (net income $3,453.9M less dividends $898.4M; companyfacts transcription of the filed statements). More
  than a dollar of market value per dollar kept. Intrinsic leg, which the speakers add because the market leg alone can
  mislead **[R2009-002]**: owner cash after interest went from about $255M in FY2016 (operating cash $334.6M less stock
  pay $18.2M less capital spending $60.9M) to $636M in FY2025 (Q7 table), up about $380M a year on roughly $2.9B kept and
  about $1.0B of added net debt: on the order of a 10 percent pre-tax return on what was put in, a dollar kept producing
  about a dollar of value at a 10 percent rate, not much more. Passes on the market leg; about even on the intrinsic leg.
- **Buybacks.** $987M spent FY2016 to FY2025 and $158.8M in the nine months to 2026-07-31 (cash-flow statements; 10-Q).
  The programme names no price: authorizations are stated in dollars only, "authorized the repurchase of up to an
  additional $500,000" thousand (10-Q, Item 2), and the shares serve partly "the funding of benefit programs including stock
  options and restricted stock" (same). Prices paid: $217.15 to $233.26 a share in August to October 2025 (10-K FY2025, Item
  5), $282.17 to $290.30 in May to July 2026 (10-Q, Item 2). Against Q7's range (all-equity basis, $151.16 to $248.42 a
  share), every price paid sits above the bottom of the range and the 2026 prices above its top. By the framework's test
  the buyback with no stated price weighs against unless the prices paid sit at or below the bottom of the Q7 range; they
  do not **[L2016-002]**, **[L1999-023]**. Buying to fund option and stock programmes is a use the rows name and refuse
  **[M2014-008]**, **[M2016-049]**.
- **Issuance and deals: value given against value got** **[M1995-001]**, **[L2014-012]**. Every acquisition in the record was
  paid in cash, much of it borrowed (ARAG on a 364-day term loan and the revolver; Atrion on the revolver and a term loan,
  10-K FY2023 and FY2024); no all-stock deal by an undervalued acquirer was found, so the one STOP of Part A
  **[L2009-019]** does not apply. The prices: Atrion $790.0M net of cash (10-K FY2024) for a company that reported net
  income of $19.4M in 2023 and $33.1M to $36.8M in 2019 to 2022 (Atrion's own 10-K facts, accession `0001654954-24-002411`
  for FY2023): 21 to 41 times its earnings, an earnings yield of 2.5 to 4.7 percent on the price, below the 5.60 percent
  bond. CyberOptics $377.8M net of cash (10-K FY2023). ARAG about €957M (10-K FY2023). The record of what such purchases
  became: a FY2009 goodwill and long-lived asset impairment that turned the Advanced Technology segment's operating profit to
  a loss of $214.4M (10-K FY2010); an $87.4M impairment on the screws-and-barrels line, bought within the adhesive business
  and then sold (10-K FY2021); the medical contract-manufacturing business sold in FY2025 with a $12.5M charge (10-K
  FY2025). A premium is defensible only where the combined companies earn more than apart **[L1997-031]**, and synergies are
  not counted on **[L2016-008]**; the filer's own return on invested capital, 12 percent against a 16 percent target in
  2024 and 2025 (DEF 14A 2026), says the purchases have not yet earned what the board asked.
- **Dividends** rose every year, from $56.4M (FY2016) to $179.1M (FY2025), $3.16 a share declared in FY2025; paid out of a
  business that cannot use most of its cash internally (capital spending under 2.5 percent of sales), which is the case the
  rows say should pay out **[M2004-089]**.
- **Part A WEIGHS AGAINST**: the core's surplus is real and partly paid out, but the bought growth has been priced near or
  below the bond's yield in its latest large case, the buybacks name no price and are made above the range, and the
  retention test is only about even on the intrinsic leg **[L2016-002]**, **[M1995-001]**, **[R1995-009]**.

**Part B: the pay, the board and the owners.**
- **Pay** (DEF 14A 2026). Chief executive's total pay $8.15M (2025), $8.57M (2024), $7.06M (2023), Summary Compensation
  Table; ratio to the median employee 130 to 1. Long-term pay is 50 percent performance shares on three-year adjusted
  earnings-per-share growth (40 percent), ROIC (30 percent) and EBITDA margin (30 percent); 30 percent stock options with a
  ten-year term and four-year vesting; 20 percent restricted share units; the annual cash award on revenue (40 percent) and
  operating profit (60 percent) "excluding non-recurring significant costs associated with acquisitions". Against the rows:
  the options are fixed-price with no step-up for retained earnings, the "royalty on money that you left with me"
  **[M1997-043]**, **[L1994-021]**; adjusted EPS growth and EBITDA margin are figures a buyer of businesses can lift by buying
  and by excluding the cost of buying **[M2003-019]**. For: ROIC is in the plan and cut the payout when missed (65 percent
  of target for 2023 to 2025); retention awards of restricted units were granted in 2025 "to retain certain top talent"
  (time-based, three-year cliff); clawback beyond the legal minimum; no hedging or pledging; executive ownership guideline
  of five times salary for the chief executive.
- **The board.** Independent chair separate from the chief executive; directors must hold five times their cash retainer,
  but shares received as units count toward it, not only shares bought with savings **[L2019-008]**; the compensation
  consultant was changed in 2025 (FW Cook from Exequity). Nothing found of a director or chief executive "also Chairman"
  **[L2014-026]**.
- **Owners as partners.** The filer's purpose statement rejects quarterly targets (Q5) while its releases give quarterly
  guidance **[L2019-006]**; the information is given to all at once, by release and webcast.
- **Part B WEIGHS AGAINST, narrowly**: the structure is better than most (independent chair, ROIC in the plan, payout cut on
  the miss), but fixed-price options with no step-up and pay on adjusted EPS and EBITDA reward the acquisition habit the
  rows warn of **[M1997-043]**, **[M2003-019]**.
- **Q6 WEIGHS AGAINST.** Recorded and carried. (Q6's buyback test was run when Q7 was reached; see Q7 for the range.)

## Q7 — WHAT IS IT WORTH? STOP.
Reached: no STOP among Q1 to Q6 closed the file (Q1 IN, Q2 IN, Q4 accounts IN, Q5 integrity IN; Q3 recorded UNDECIDED and
Q6 AGAINST, both weighings; Q6's one STOP not met). Value is "the discounted value of the cash that can be taken out of a
business during its remaining life" **[R1996-018]**, at the long government rate **[L2000-021]**, held as a range
**[L2000-024]**. Every figure below is computed by `q7.py` in the research folder from filed figures; output in
`q7_output.txt`.

- **Owner cash after every real cost, all-equity basis** (operating cash, which is after interest and tax paid, less stock
  pay, less capital spending, less finance-lease principal, plus interest paid after the company's own effective tax rate
  that year; Q7, On what the floor is earned). $ millions:

  | FY | Operating cash | Stock pay | Capital spending | Finance-lease principal | Interest paid | Effective tax | Owner cash, all-equity | Owner cash after interest |
  |---|---|---|---|---|---|---|---|---|
  | 2021 | 545.9 | 22.8 | 38.3 | 6.6 | 27.1 | 20.9% | 499.6 | 478.2 |
  | 2022 | 513.1 | 30.7 | 51.4 | 5.4 | 23.0 | 21.0% | 443.8 | 425.6 |
  | 2023 | 641.3 | 22.7 | 34.6 | 6.8 | 54.7 | 20.8% | 620.5 | 577.2 |
  | 2024 | 556.2 | 19.0 | 64.4 | 6.1 | 86.0 | 20.2% | 535.3 | 466.7 |
  | 2025 | 719.2 | 18.9 | 58.1 | 5.9 | 98.7 | 18.9% | 716.3 | 636.3 |
  | Mean | | | | | | | **563.1** | **516.8** |

  Sources: cash-flow statements and supplements, 10-K FY2022 (FY2021, FY2022 through the tagged series) and 10-K FY2025
  (FY2023 to FY2025, read as filed, `0000072331-25-000144`). Working capital is inside operating cash, as Q7's specific (d)
  asks; FY2022 carries a working-capital build and FY2025 a release (inventories and payables), neither described by the
  filer as tied to one event, so the literal window stands. No first or last year is described by the filer as
  aberrational (specific (a)); the growth between the window's halves (FY2021-22 mean $471.7M to FY2024-25 mean $625.8M,
  9.88 percent a year) is shown beside the end-to-end figure (9.42 percent) and gives a top of $259.92.
- **Acquisitions** (specific (c)). Cash paid for businesses net of businesses sold, FY2021 to FY2025: $0.0M, $171.6M,
  $1,422.8M, $790.0M, -$28.1M, total $2,356.3M, mean $471.3M a year, 83.7 percent of mean owner cash (cash-flow
  statements). Default pair: acquisitions deducted and the total growth credited (9.42 percent a year on aggregate owner
  cash, FY2021 to FY2025). Pair beside: acquisitions left out and organic growth only, as the filer reports it: +10.8,
  -1.4, -2.5, -2.5 percent of sales in FY2022 to FY2025 (MD&A of each 10-K), 0.95 percent a year compounded. The deal closed
  after the window and before the price date (CapstanAG, March 2026, $11.6M paid net of cash, "not material", 10-Q) is in
  today's net debt and credited at nothing.
- **CONVENTION of this run** (rationale: the framework says acquisitions are deducted while the total growth is credited,
  and that growth spending stops when growth stops (specifics (c) and (e)), but not how the deduction runs through the ten
  years): in the shown-growth case, acquisition spending is carried for years one to ten at the window's share of owner
  cash (83.7 percent) and stops after year ten, when growth stops; the terminal value is owner cash before acquisitions.
- **Net debt at the latest filed date** (2026-07-31, 10-Q `0000072331-26-000054`): short-term debt $192.0M, current
  maturities $10.0M, long-term debt $1,529.0M, finance leases $18.7M, less cash $113.4M = **$1,636.3M**. Operating leases
  ($68.5M) left out, as the convention says. No subsequent event stated in that filing adds to it. Minority investments
  ($11.7M) left out as immaterial.
- **The range, all-equity basis (the central figure)**, sovereign 5.60 percent, ten years then zero nominal growth:

  | Case | Value of the business | Less net debt, per share |
  |---|---|---|
  | No growth, no acquisitions (owner cash $563.1M a year) | $10,055.7M | **$151.16** |
  | Total growth 9.42% credited, acquisitions deducted (default growth case) | $15,473.2M | **$248.42** |
  | Organic growth 0.95%, acquisitions left out (pair beside) | $10,842.4M | $165.28 |
  | Depreciation in place of capital spending (variant beside), both ends | | $148.70 to $251.22 |

  **Value range: $151.16 to $248.42 a share against $328.17**; width 1.64 to 1. The literal window is the window used.
  Equity-only basis beside (owner cash after interest, mean $516.8M, total growth 7.40 percent, against the market value):
  $165.69 to $205.22 a share; organic pair $165.69 to $178.65.
- **What the price assumes.** At $328.17 the market value is $18,278.9M and the business with its debt $19,915.1M; the
  five-year mean owner cash is a 2.83 percent yield on that, half the bond. Shown only to size the acquisition deduction,
  and not a case (it is the pairing specific (c) forbids): the total growth credited with nothing paid for it gives $351.85
  a share. The price is roughly what the business is worth if the acquired growth comes free.
- **The floor and the screamer.** The floor is about ten percent pre-tax, applied to owner cash after the company's own tax
  (Q7 CONVENTION; Whose tax) **[M2003-149]**. The price is above the top of the range, so the expected return at the price
  is below the sovereign rate itself, let alone the floor; "a price above the top of the range closes OUT however wide the
  range" (Q7, specific (f)). Nothing here screams **[M2009-005]**; "if you have to actually do it on — with pencil and paper,
  it’s too close to think about" **[M1996-084]**, and this is not close.
- **Fair price (a reporting figure, never a verdict; Part VII):** defined here as the price at which the midpoint of the
  range earns the floor: the two end cases' cash streams averaged and discounted at 10 percent (ten years, then zero
  growth), less net debt, per share. **$77.15 a share on the all-equity basis (central); $86.51 equity-only beside.** No
  cheap price is reported.
- **Q6's buyback test, recorded back:** the bottom of the range is $151.16; the prices paid ($217.15 to $290.30 in the
  latest two filed periods) are all above it (Q6).
- **VERDICT: OUT.** The range is narrower than three to one, and the price sits above its top: the expected return at
  $328.17 is below the floor **[M2003-149]**; a wonderful castle at a price that needs the acquired growth free is not a
  margin of safety **[M1996-084]**, **[M2019-015]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (No named business of Q12 is among the company's lines.)

---
## THE BOX
**OUT at Q7 on price.** Range $151.16 to $248.42 a share (all-equity basis, central; literal window FY2021 to FY2025) against
$328.17 (close 2026-10-09); equity-only $165.69 to $205.22 beside. Fair price $77.15 all-equity, $86.51 equity-only
(reporting figures, not verdicts). Q1 IN, Q2 IN (the adhesive-dispensing part decides), Q3 UNDECIDED, Q4 accounts IN and
weighs against, Q5 integrity IN, Q6 weighs against. Not a TOO HARD; no research pass is opened.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Bearing on Q8 (the alternatives).** The five-year mean owner cash is a 2.83 percent yield on the business with its debt
  at $328.17, against the 5.60 percent 30-year Treasury (2026-10-09).
- **Bearing on Q9 (the target's debt).** Borrowings $1,731.4M at 2026-07-31: commercial paper $192.0M (maturities up to
  364 days, under a $1.2 billion programme opened June 2026, backed by a $1.2 billion revolving facility to January 2031);
  senior notes $10.0M due 2026-2027 and $90.0M due 2026-2030 (insurance-company private placements); 5.600 percent notes
  $350M due 2028; 4.500 percent notes $600M due 2029; 5.800 percent notes $500M due 2033; a term loan of $2.7M due 2031
  (10-Q, Debt note). Covenants include a leverage ratio and an interest-coverage ratio; the company reports compliance
  (10-Q; 8-K 2026-01-30). FY2025 pre-tax earnings over interest expense: ($597.6M + $104.2M) / $104.2M = 6.7 times (10-K
  FY2025 income statement; pre-tax earnings, not EBITDA). Cross-currency swaps of $842.6M notional as net-investment
  hedges (10-Q, derivatives note); whether they carry collateral terms was not read. Pension obligations $41.5M and
  postretirement $43.7M at 2026-07-31 (10-Q). Debt has been taken up for each large purchase and paid down between them
  (Q4 table).
- **Bearing on Q10.** None beyond the above.
- **Integrity facts:** none recorded that were not judged; Q5 was reached and answered.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits for Step 0 to the standing rule, Q1, Q2, Q3, Q4, Q5, Q6, Q7 and this close, each a pathspec commit of the run
      file and the research folder only.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (the lock file in `Screens/_daily/` was present from the start of the run, "interactive v5 re-runs batch 8");
      the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen
      by accident is declared under CONTAMINATION at the top, items (1) to (5), and not used. `Test Runs/` was never listed;
      the only paths used under it were this run file, this research folder and the two templates.
- [x] Every v5 id resolves (`check_quotes.py`: every M/L/R id found in `principle_ledger_v5.csv`, every quoted fragment
      beside an id found in that row, no E-id); every filing fact has its accession or its named filing; the numbers are
      from filings or from `q7.py` on filed numbers, except those labelled CONVENTION.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash less stock pay, capital
      spending and finance-lease principal; the sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q2, Q3, Q6); the facts found for
      later questions are under AFTER THE STOP.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; rows up to 2025.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its rule lines, ids and floor were not.
- [x] `python tools/check_framework.py` PASS before the closing commit (run 2026-10-10, after the close was written;
      `check_quotes.py` also PASS: 71 ids, 22 quoted fragments, no problems).

**Honest notes on the audit.** (a) FY2021 and FY2022 cash-flow lines were taken from SEC's tagged data (companyfacts) and
not re-read on the filed FY2022 statement; FY2023 to FY2025 were read as filed. (b) FY2025 segment operating profit is
computed (EBITDA less depreciation less amortization) because the filer stopped reporting it. (c) The competitor margins
are company-level from tagged data except Graco's Industrial segment, read in its 10-K. (d) The Atrion earnings multiple
uses Atrion's own tagged net income, not its filed statement. (e) Rivals' and customers' views (scuttlebutt) were not
available from the public record.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q7 specific (c) does not say how the acquisition deduction runs through the ten years.** "Deducted and the total
   growth credited" can be read as a flat deduction of the window's mean (which, at 83.7 percent of owner cash here, leaves
   a base of $91.8M and makes the terminal value nearly vanish if the deduction is carried forever), or as a deduction that
   grows with the business and stops when growth stops. This run took the second and confessed it as a CONVENTION of the
   run; the framework should say which, since for a serial acquirer it moves the top of the range by more than the width
   of the range.
2. **The fair price's "midpoint of the range" is not defined as a cash stream.** The floor is a rate, the midpoint is a
   value; the run averaged the two end cases' cash streams and discounted that at 10 percent. Another analyst could take
   the midpoint value's implied perpetuity yield instead and get a different figure. One line in Part VII would fix it.
3. **The business-of-parts convention has no rule for a non-deciding part that is TOO HARD rather than open.** It says
   an open part is carried to Q7 at no growth; ATS here is neither shown open nor judgeable. The run left it inside the
   aggregate owner cash (its growth inside the total-growth case) and said so; the convention should say whether such a
   part is carried at no growth or at nothing.
4. **The template's segment table assumes operating profit by segment.** From FY2025 this filer reports only segment
   EBITDA (ASU 2023-07 adoption); the run computed operating profit from the same note, which is arithmetic, but the parts
   threshold will meet this more often as filers adopt EBITDA as the segment measure.
5. **The brief's errors.** (a) The canonical brief's reporting paragraph tells the analyst to build the range "by Q7's six
   specifics", but Q7 carries ten: the four the PG re-test added on 2026-10-05 (growth on aggregate owner cash, all capital
   spending deducted with the depreciation variant beside, zero nominal growth after year ten, a price above the top of the
   range closing OUT) and the six of 2026-10-06. One of the four omitted decided this run (the price above the top). (b) The
   dispatch message lists "the parts-and-consumables share of sales" as a line of evidence; no 10-K or 10-Q read gives that
   figure (the filer says only that "a significant percentage of our revenue is recurring"), so the line asks for a number
   the primary record does not hold; it is recorded as unknown, not estimated. (c) The canonical brief names other
   companies' runs in its own dated notes (the ATR, LOPE and LSTR analysts), so every analyst who reads it as instructed
   sees other names; small, but it is the brief breaching its own blind rule. (d) Not the brief's text but its environment:
   the scratchpad directory of the dispatch session is shared by concurrent analysts, and a draft of another analyst's run
   was displayed to this one (contamination item (5)); a brief that names a per-run draft location would close that.
