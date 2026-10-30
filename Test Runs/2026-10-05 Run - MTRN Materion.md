# Company Run — Materion Corporation (NYSE: MTRN) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`, so
whether the operator holds MTRN is unknown to the analyst. This is a purchase run, not a holding review.

**CONTAMINATION, declared.** (1) The session context showed recent commit subjects naming other runs' boxes (OSIS OUT at
Q2 "the castle stands but protects only ordinary returns"; ENSG OUT at Q4; MBUU research pass OUT at Q2). I read them
before any MTRN fact and they describe a pattern (a castle that protects only ordinary returns) that I also considered
here; I did not let it decide the question, and the deciding question below is Q1, not Q2. (2) A directory listing of
`Test Runs/` showed the names of other 2026-10-05 run and research files; none was opened. (3) No file about MTRN other
than this one and its research folder was opened. `Screens/`, `PORTFOLIO.md` and every holding review were not opened.

**Working folder:** `Test Runs/_research 2026-10-05 MTRN/` (filings as fetched from EDGAR and their text conversions,
`facts.json`, `sub.json`, the USGS beryllium summary).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $319.40 (2026-10-05, the live quote printed by `tools/run.py`; aggregator, flagged per operator rule 5; not
  cross-checked against a second quote).
- **Shares by class** from the latest filing's cover: 20,833,725 common shares, no par value, one class (10-Q for the
  quarter ended 2026-07-03, filed 2026-08-05, accession `0001104657-26-000044`; `python Screens/cover_shares.py MTRN`).
  Diluted weighted shares Q2 2026: 21,075 thousand (press release, 8-K accession `0001104657-26-000042`).
- **Market cap:** 20.834M x $319.40 = **$6,654M**. Net debt at 2026-07-03: total debt $440.7M less cash $20.0M =
  **$420.7M** (10-Q `0001104657-26-000044`). Off-balance-sheet consigned metal at 2026-07-03: **$505.6M** notional
  (same 10-Q).
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-02 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-12, accession `0001104657-26-000011` (Items 1, 1A, 3, 5, 7, 7A; cash-flow statement;
    balance sheet; notes on tax credits and factoring).
  - 10-Q Q2 2026, filed 2026-08-05, accession `0001104657-26-000044`; Q2 2026 earnings release, 8-K accession
    `0001104657-26-000042`.
  - Proxy (DEF 14A) filed 2026-03-26, accession `0001104657-26-000022` (CD&A, AIP and PRSU tables, Appendix B).
  - Earlier 10-Ks for the ten-year read: FY2017 `0001104657-18-000007`, FY2019 `0001104657-20-000013`, FY2021
    `0001104657-22-000021`, FY2022 `0001104657-23-000019`, FY2023 `0001104657-24-000019`, FY2024 `0001104657-25-000024`.
  - 8-K of 2025-12-11 (accession `0001104657-25-000207`, item 5.02: a director's retirement and a new director).
- **One figure cross-checked against the filed statement:** net cash from operations FY2025 = $103,243 thousand in the
  10-K's Consolidated Statement of Cash Flows (`0001104657-26-000011`) = the XBRL fact printed by `tools/run.py` (103).
  Shareholders' equity 2025-12-31 = $943,277 thousand in the Q2 2026 balance sheet = 943 in the tool's table.
- **`tools/run.py MTRN`, arithmetic lines only** (its v4 output ignored, Part VII). Its known defects checked against the
  filings: the share count is current (2026-07-03 cover); stock pay is printed and matches the filings; **it omits
  "Payments for mine development"** (a separate investing line, $26.3M in 2025, $12.2M in 2024, $9.3M in 2023), so its
  owner-earnings columns overstate owner cash; its window stops at FY2024 although FY2025 is filed; its debt column is
  non-current debt only. I rebuilt the owner-cash table from the filed cash-flow statements:

  | FY | OCF | stock pay | PP&E capex | mine dev. | D&A | owner cash (OCF − SBC − all capex) | depreciation variant (OCF − SBC − D&A) |
  |---|---|---|---|---|---|---|---|
  | 2016 | 68.2 | 3.2 | 27.2 | 9.9 | 45.7 | 27.9 | 19.3 |
  | 2017 | 67.8 | 5.0 | 27.5 | 1.6 | 42.8 | 33.7 | 20.0 |
  | 2018 | 76.4 | 5.3 | 27.7 | 6.6 | 35.5 | 36.8 | 35.6 |
  | 2019 | 99.2 | 7.2 | 24.3 | 2.3 | 41.1 | 65.4 | 50.9 |
  | 2020 | 101.1 | 5.5 | 67.3 | 0 | 42.4 | 28.3 | 53.2 |
  | 2021 | 90.2 | 6.5 | 102.9 | 0 | 44.1 | −19.2 | 39.6 |
  | 2022 | 116.0 | 8.8 | 77.6 | 0 | 53.4 | 29.6 | 53.8 |
  | 2023 | 144.4 | 10.1 | 110.5 | 9.3 | 61.6 | 14.5 | 72.7 |
  | 2024 | 87.8 | 10.6 | 68.6 | 12.2 | 68.7 | −3.6 | 8.5 |
  | 2025 | 103.2 | 10.9 | 53.3 | 26.3 | 69.1 | 12.7 | 23.2 |
  | **5-yr mean 2021-25** | | | | | | **6.8** | **39.6** |
  | 10-yr mean | | | | | | 22.6 | 37.7 |

  ($ millions; sources: the cash-flow statements of the 10-Ks listed above; 2016 from the FY2017 10-K, 2017 to 2019 from
  the FY2019 10-K, 2019 to 2021 from the FY2021 10-K, 2021 to 2023 from the FY2023 10-K, 2023 to 2025 from the FY2025
  10-K.) Three things in the OCF line are not ordinary operating cash and are written down here as found: **customer
  prepayments** booked as "unearned income" ($4.7M 2019, $54.1M 2020, $13.8M 2021, $21.9M 2022, $16.7M 2023, about
  $111M in all, funding the precision clad strip capacity for one customer; $41.1M of it still unearned at 2026-07-03);
  **receivables factoring** begun in 2024 ($48.9M sold in 2024, $59.4M in 2025, FY2025 10-K note A); and a **$42.0M
  pension contribution** in 2018. Stock pay is deducted at its expense; the cash paid for withholding on vested awards
  ($2.6M to $7.6M a year) is a financing line and is not deducted again.

### The balance sheets, ten year-ends, read before the income account **[M2025-032]**
(Template: read in Step 0 because the file closes before Q4. $ millions, from the filed balance sheets; first-filed
values as transcribed by `tools/run.py`, checked at 2025.)

| year-end | equity | goodwill | intangibles | LT debt | cash | receivables | inventory | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2017 | 495 | 91 | n/a | 3 | 42 | 124 | 220 | 536 |
| 2019 | 611 | 79 | n/a | 1 | 125 | 155 | 190 | 590 |
| 2020 | 656 | 145 | n/a | 37 | 26 | 166 | 251 | 631 |
| 2021 | 720 | 319 | n/a | 434 | 14 | 224 | 361 | 694 |
| 2023 | 885 | 321 | 134 | 388 | 13 | 193 | 442 | 854 |
| 2025 | 943 | 281 | 106 | 436 | 14 | 223 | 461 | 912 |

What the figures say: from 2017 to 2025 equity rose $448M, of which retained earnings $376M; long-term debt rose about
$433M; goodwill and intangibles rose about $296M (Optics Balzers 2020, $130.7M; HCS-Electronic Materials 2021, purchase
price about $395.9M, FY2021 10-K). The company was debt-free with $125M of cash at the end of 2019 and has carried
about $420M to $445M of net debt since 2021, secured on substantially all assets (FY2025 10-K, Item 1A). Inventory
went from $220M to $461M while value-added sales went from $678M (2017) to $1,046M (2025): inventory per dollar of
value-added sales rose from about 32 cents to about 44 cents. Receivables at 2025 are after $59.4M of receivables sold
that year. What they do not say: the consigned precious metal and copper, **$526.2M** at 2025-12-31 against $381.6M a
year earlier (FY2025 10-K, Off-balance Sheet Obligations), owned by banks and paid for by a fee, sits outside the
balance sheet; its capacity is limited by covenant and by metal prices (unused capacity fell from $233.4M to $88.4M
in 2025). What they cannot say: whether the $281M of goodwill (of which $221.4M in Electronic Materials) is worth its
carrying value; the Precision Optics goodwill was written down by $56.1M in 2024, with $17.1M of long-lived assets.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**; the
answer depends on whether the business can be understood at all (Q1). The market serves: at $319.40 the quote "just
tells us prices" **[M2006-077]** and carries no information about value; the stock's rise is no reason to buy
**[L2013-007]**. Margin of safety: a decision that needs a spreadsheet is "too close to think about" **[M1996-084]**.
No macro enters: the defense-spending and AI-semiconductor narrative in the proxy's opening pages is the kind of
outlook that must not decide a purchase **[M2000-094]**. Who is paid to tell you: the press release headlines are
"record" quarters and adjusted figures; the seller's account of what he sells is read last, not first **[M2011-083]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the beryllium position is real and rare: USGS
(Mineral Commodity Summaries 2026, beryllium) reports one company in Utah mining bertrandite, US mine output of about
230 of a world total of about 430 tons in 2025, and Defense Production Act support for the leading US producer; reserves
of 40.9M pounds of beryllium, proven reserves to last "a minimum of seventy-five years" (FY2025 10-K, Ore Reserves);
(b) zero pending beryllium-disease cases at 2025-12-31, against several in the FY2017 and FY2021 10-Ks; (c) the 2025
annual bonus paid **0%**, and the bonus measure charged the $28.6M quality-claim cost against management rather than
excluding it (proxy, AIP table and Appendix B). Against the business, as found: (d) the filer's own risk factor, "The
markets for our products are experiencing rapid changes in technology" (FY2025 10-K, Item 1A); (e) value-added sales
fell from $1,143.6M (2022 as first reported) to $1,046.2M (2025) despite a $392M acquisition paid in late 2021; (f)
mine development cash is omitted by the house tool, and owner cash after all capital spending averaged $6.8M a year
2021-2025; (g) the consigned metal grew 38% in 2025 to more than half of book equity.

## THE STANDING RULE
Owning this, bought for cash and sized so that a total loss could be borne, puts the buyer at no risk of ruin; the rule
forbids only borrowed money or a size that a loss could not survive **[M2012-081]**, **[L2014-024]**. No margin, no
leverage. Nothing in the target can call on the buyer. PASS (the buyer's conduct, not the target's).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**.
The product may stay opaque if "the economic dynamics of the industry" are understood **[M2011-014]**. A business whose
ten-year economics cannot be foreseen because its industry changes fast closes here, TOO HARD; a holding company, or a
company of distinct businesses, is understood by its parts: the framework's CONVENTION (Q1, A holding company) keeps
the whole outside the circle when a part that matters cannot be understood, because doubt means outside: "if you have
doubts about something being into your circle of competence" **[M2002-092]**. **[M2023-031]** stays OPEN against the
by-parts reading.

**The parts, from the FY2025 10-K (`0001104657-26-000011`), value-added sales (VA) and segment EBITDA, $ millions:**

| segment | VA 2020 | VA 2022 | VA 2025 | EBITDA 2025 | share of 2025 VA | share of 2025 segment EBITDA |
|---|---|---|---|---|---|---|
| Performance Materials (beryllium mine and mill, beryllium and copper alloys, clad strip) | 345.3 | 589.5 | 618.1 | 127.2 | 59% | 62% |
| Electronic Materials (precious and specialty metal targets, lids, wire, chemicals) | 220.5 | 412.8 | 327.6 | 71.1 | 31% | 35% |
| Precision Optics (thin-film filters and coatings) | 101.9 | 113.6 | 100.5 | 7.7 | 10% | 4% |
| Other (corporate) | | | | (24.7) | | |

(2020 and 2022 from the FY2022 and FY2024 10-Ks; Electronic Materials 2022 as restated in the FY2023 10-K, first
reported as $442.0M.)

**Part 1, the beryllium business.** The key variables **[M1998-044]**: beryllium volume into defense, aerospace,
energy, industrial and consumer-electronics connectors; mix; yields; the regulation of beryllium exposure; and
substitution. These are foreseeable in kind: one US mine, 75 years of proven reserves, a mature product sold for its
properties where they are "crucial" (USGS, Substitutes). But the earnings of the part have not been steady enough
for the past statements to tell me the future ones **[M2008-033]**: segment operating profit of the predecessor
segment was $6.6M (2% of VA) in 2016, $22.0M (6%) in 2017, $70.7M (17%) in 2019 (FY2017 and FY2019 10-Ks); segment
EBITDA was $38.7M in 2020 and $174.5M in 2023 (FY2022 and FY2023 10-Ks). Inside the segment sits the precision clad
strip line, whose "large precision clad strip customer" raised a quality claim in 2025 that cost $27.3M and idled the
plant (FY2025 10-K, MD&A); one Performance Materials customer was about ten percent of company net sales in 2023 and
2024 (Item 1; the filing does not say whether it is the same customer); and about $111M of customer prepayments
(2019-2023) funded equipment that is "serviced out of" for those customers (Q2 2026 10-Q, unearned income note). The 2023 to 2025 figures also carry an undisclosed amount of the IRA advanced
manufacturing production credit, booked as a reduction of cost of goods sold (FY2025 10-K, Note H; amount: no instance
found in the 10-K, 10-Q or releases, searched for "production credit"); OBBBA accelerated the phase-out of certain
IRA incentives (same note). I judge the beryllium mine and mill understandable; I do not judge the whole segment's
ten-year earning power foreseeable, because a large slice of it is one device-maker's design choice.

**Part 2, Electronic Materials (35% of 2025 segment EBITDA, so it matters).** The filer's own words: "we may lose
existing applications and customers from time to time due to the rapid change in technologies" (FY2025 10-K, Item 1,
Electronic Materials), and, for the company, "Next-generation solutions may quickly render an existing product
obsolete" and "Our sales and development cycle [...] may typically take several years, making it very difficult to
forecast sales and results of operations" (Item 1A). The winner in semiconductor sputtering targets is not Materion:
JX Advanced Metals states about 65% of the world market for semiconductor sputtering targets (jx-nmm.com, Quick Guide;
company website, not a filing; flagged), and its Semiconductor Materials segment earned ¥39.5B on revenue of ¥177.2B
in the year to March 2026 (japanstockpulse.com summary of the results; aggregator, flagged; revenue includes metal and is
not comparable to Materion's value-added basis). Materion sold its Albuquerque target business at a $6.4M loss in 2024
(FY2024 10-K), and paid about $395.9M for HCS-Electronic Materials in November 2021 (FY2021 10-K); the segment's VA
was $412.8M in 2022 and $327.6M in 2025. Can I name the winner, not just the industry **[M2012-067]**? No. Is the
forecast about customers or about technology **[M2017-019]**? About technology: which metals each node and package
will use, and whose qualification wins. Would the insiders write the ten-year economics down **[M2000-105]**? The
company gives one-year adjusted-EPS guidance and says forecasting is "very difficult"; its own impairment models
rest on five-year unit forecasts (FY2025 10-K, Critical Accounting Policies). This is the case the rows send to the
box: "where we think the future technology could hurt the business as it presently exists" it does not make it
through the filter **[M1998-008]**; "We view change as more of a threat" **[M1999-063]**.

**Part 3, Precision Optics (4% of segment EBITDA).** "it recognizes the inherent challenges of operating in a rapidly
evolving technological landscape" (FY2025 10-K, Item 1); competitors Viavi, Coherent, MKS; goodwill and assets written
down by $73.2M in 2024. Small; it would not decide the whole on its own.

**Is it important and knowable** **[M2006-076]**? The ten-year economics of Electronic Materials, and of the clad
strip line, are important (together well over a third of segment EBITDA) and, by the filer's own account, not
knowable to the people who run them. Seeing that semiconductors and defense will grow is seeing the industry, not the
company: "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge
what its profit margins and returns on capital will be" **[L2009-005]**. My doubt is real, and doubt places it
outside **[M2002-092]**; the danger the rows name is to think one understands a business and not **[M1997-024]**.

**Which cause.** NATURE, not WORK: the deciding question (who wins the materials of the next nodes and the next
device designs, and at what margin, ten years out) is a forecast the industry's own insiders would not write down
**[M2000-105]**, and the filer says so in its risk factors; "in other cases the nature of the industry would be the
roadblock" **[L1993-023]**; study does not cure it **[L1999-018]**. More reading would not change the answer **[M2008-086]**.
A lower price does not reopen it **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)**, "in, out, and too hard" **[M2006-013]**. The file closes here. Everything below is
  NOT REACHED, and every number after this line is COMPUTATION, NOT A CLEARANCE.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED. Evidence gathered before the close, recorded for the operator and not judged:
- **The competitor row** (same metric where one exists):

  | competitor | what it is | metric | source |
  |---|---|---|---|
  | Materion, Electronic Materials | targets etc. | 2025 EBITDA $71.1M on VA $327.6M (21.7%) and on net sales $1,010.0M (7.0%) | FY2025 10-K `0001104657-26-000011` |
  | Materion, Performance Materials | beryllium and alloys | 2025 EBITDA $127.2M on VA $618.1M (20.6%); 2024 24.6%; 2023 25.3% | same |
  | JX Advanced Metals (Tokyo 5016), Semiconductor Materials | about 65% of semiconductor sputtering targets | operating profit ¥39.5B on revenue ¥177.2B (22.3%) FY3/2026; ¥26.7B FY3/2025 | aggregator summary (japanstockpulse.com) of company results; non-SEC, flagged; revenue basis includes metal |
  | NGK Insulators (Tokyo 5333) | beryllium copper | not separately reported; inside the Digital Society segment | web search of NGK results; non-SEC, flagged; no segment margin found |
  | Honeywell Electronic Materials | targets | not separately reported | no figure found |
  | Plansee | refractory metal targets | private | no figure found |
  | Ulba Metallurgical (Kazakhstan) | beryllium | state-owned | no figure found |

- The consignment fee "can only be charged to customers in a limited case-by-case basis" "Because of market forces and
  competition" (FY2025 10-K, Item 7A): the filer's own statement of limited pricing power in the precious-metal lines.
- The management's own return target: ROIC PRSUs pay 100% at an average ROIC of 10.6% for 2025-2027, 50% at 9.6%
  (proxy `0001104657-26-000022`), against a 5.63% Treasury.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED. Recorded only: about $523M paid for acquisitions in 2020-2021 and about $189M of capital spending and
mine development above depreciation 2020-2025 ($528M against $339M, Step 0 table), while GAAP operating profit went from $70.5M (2019) to
$109.8M (2025) and adjusted EBIT from about $150M (2024, 2025; proxy Appendix B). Not judged.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0. Recorded only, not judged: segment results are reported as
EBITDA in the filer's own mouth; "special items" appear every year (restructuring charges in nine of the ten years
2016-2025, 2021 a small reversal, XBRL); the release headlines adjusted EPS and gives and raises adjusted-EPS guidance; the
production credit is netted in cost of goods sold without an amount; customer prepayments and factoring move OCF.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Recorded only: CEO Jugal K. Vijayvargiya, 2025 total pay $4.79M; the 2025 bonus paid 0% on missed goals
(proxy `0001104657-26-000022`); the FY2025 10-K added to its beryllium risk factor the parenthesis "(despite numerous
studies affirming the safety of beryllium in these products)", absent from the FY2021 wording.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Recorded only: dividends $11.5M in 2025; 100,000 shares bought back in Q2 2025 for $7.8M (about $78 a
share); a new $50M authorization of October 2025 that names no price (FY2025 10-K, Item 5 and Liquidity); HCS bought
for cash with a $300M term loan (FY2021 10-K). Share count flat at about 20.9M diluted since 2014 (XBRL).

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. **COMPUTATION — NOT A CLEARANCE**, at the owner's request, with the Q7 CONVENTION construction:
- **Cash input:** five-year average of owner cash after every real cost (all capital spending including mine
  development, stock pay deducted) = **$6.8M**; the depreciation variant = **$39.6M** (Step 0 table). Owner cash is
  after interest and tax, so it is the equity holders' cash.
- **Growth shown:** none. Aggregate owner cash fell (2021 −$19.2M to 2025 $12.7M is not a rate; the depreciation
  variant went from $39.6M to $23.2M); over ten years the first measure went from $27.9M (2016) to $12.7M (2025). The
  shown-growth end therefore collapses onto the no-growth end; growth carried at zero nominal, discounted at 5.63%.
- **Value range (COMPUTATION):** $6.8M / 0.0563 = $121M = **$5.80 a share** (all-capex basis) to $39.6M / 0.0563 =
  $703M = **$33.76 a share** (depreciation basis), against **$319.40**. The two ends are 5.8 to 1 apart, wider than
  the three-to-one width, which by the convention would itself close TOO HARD **[L2000-025]**. The price is about
  9.5 times the top of the range.
- **FAIR PRICE (COMPUTATION; owner's request, not a rule).** Central case: the depreciation-basis owner cash, $39.6M,
  at no growth (the growth shown). The floor of about ten percent pre-tax (Q7 CONVENTION; "real expectancy is below
  10 percent" **[M2003-149]**) is converted to after-tax at the 21% US federal statutory rate (the company's own
  effective rate was 8.2% in 2025 and 60.5% in 2024, so neither is a guide): 10% x (1 − 0.21) = **7.9% after tax**.
  Fair price = $39.6M / 0.079 = $501M = **$24.06 a share**. At $319.40 the expected after-tax return on the central
  case is $39.6M / $6,654M = 0.6% a year plus growth of zero.
- **CHEAP PRICE (COMPUTATION; my rule, stated):** the price at which even the lower, all-capex cash ($6.8M) clears the
  floor with no growth, so that no pencil is needed on any reading of the capital spending: $6.8M / 0.079 = $86M =
  **$4.13 a share**.
- **Sensitivity, the most generous reading I can defend, shown so the gap is not a matter of definitions:** taking the
  company's own 2026 adjusted-EPS guidance midpoint ($7.00, an adjusted figure that excludes acquisition amortization
  and special items, so not owner cash) on 21.05M diluted shares = $147M a year, the price that clears 7.9% after tax
  at no growth is $147M / 0.079 / 21.05M = **about $89 a share**; to justify $319.40 at 7.9% the $147M would have to grow
  forever at about 5.7% a year, a rate the sovereign itself (5.63%) caps **[M1997-095]**.
- What the arithmetic shows: on no reading of these filings is the price below value; the case is not close.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED. (For the record: an after-tax owner-cash yield of 0.1% to 0.6% against a 5.63% Treasury.)

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Recorded only: debt $440.7M, secured on substantially all assets, maturing mostly 2030, with leverage and
coverage covenants; consigned metal $505.6M (2026-07-03) under an agreement maturing 2028-08-31, with covenants, whose
fee rises with metal prices (a 20% rise adds about $4.5M a year) and whose capacity the consignors can limit; beryllium
health claims: none pending at 2025-12-31, insurance "subject to an annual deductible" (FY2025 10-K, Item 3); OSHA
standards that "may make them more stringent" (Item 1). The "little or no debt" criterion was not applied.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Recorded only: beryllium is not among the businesses the rows name; the question for a later run would be
the newspaper test on worker and community exposure, read against the litigation history.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** Materion is three businesses; the beryllium mine and mill can be understood, but
Electronic Materials (35% of 2025 segment EBITDA) and the single-customer clad strip line sit in markets the filer
itself calls subject to "rapid changes in technology", whose ten-year winners and margins the industry's insiders do
not write down. By the by-parts reading, a part that matters and cannot be understood keeps the whole out. No
research pass is opened (NATURE). For the record only, COMPUTATION: value range $5.80 to $33.76 a share, fair price
$24.06, cheap price $4.13, against $319.40.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before `tools/run.py` ran); written question
      by question. Not committed: this run's instructions forbid commits, so write-early was kept by saving the file,
      not by commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      checked to be in that row); every filing fact has its accession; no number without a row or a filing; the
      aggregator figures (price, JX) are flagged.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance, and the
      valuation is headed COMPUTATION — NOT A CLEARANCE (operator rule 3).
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5), with mine development added back
      in where the tool omitted it; the sovereign from the issuing authority; aggregator quotes flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations paragraph, items a to g).
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 yield and growth lines were not used.
- [x] `python tools/check_framework.py` PASS before saving the final version (see the note at the end).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The by-parts rule decides this file, and it was written for holding companies.** Q1's "A holding company" paragraph
is a CONVENTION built for conglomerates of separate businesses; Materion is an operating company with three
segments. I applied it because it is the only rule the framework has for a company whose parts differ in
understandability, but it lets a 35% part veto a 60% part that is the reason anyone would own the company. A second
analyst could read Materion as one materials converter with a unique resource, pass Q1, and close at Q2 (the
filer's admission of limited pricing power, a ten-year return around management's own 10.6% ROIC target) or at Q7
(the price is roughly ten times the top of the range). The box would differ (OUT against TOO HARD) though the action
(no purchase) would not. The framework does not say how large a part must be to "matter", nor whether a STOP may
fall on a part when another STOP would plainly fall on the whole. (2) **WORK against NATURE at the edge.** The
NATURE test asks whether insiders would write the forecast down **[M2000-105]**; for a supplier into
semiconductors the insiders write five-year plans, not ten-year ones, and the framework does not say whether a
five-year plan counts. I read the filer's "very difficult to forecast" as NATURE; a WORK reading would have opened a
research pass on the beryllium franchise alone, which the by-parts rule would still have overridden. (3) **The tool
omits mine development**, a capital outlay a mining company reports on its own line; `tools/run.py`'s owner-earnings
columns overstate owner cash for every miner and should read every "Payments for mine development" or similar line.
(4) **Q7's shown-growth end is undefined when owner cash has no trend** (here it is negative or not a rate); I set it
to zero, which collapses the range to the two cash definitions; the convention could say so. (5) **Cash flows that
are customer prepayments or factoring** are not named anywhere in Q4 or the Q7 convention; over a long span they wash
out, but a five-year average can start or end inside them.
