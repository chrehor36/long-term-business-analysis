# Company Run: Wolverine World Wide, Inc. (NYSE: WWW), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before
any fetch. Working folder: `Test Runs/_research 2026-10-06 WWW/` (scripts `pull.py`, `pull2.py`, `comp.py`, `value.py`,
`fetch.py`, `row.py`; filings converted to text there).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this run by the blind rule of the
assignment, so whether the operator holds the name is unknown to the analyst.

**CONTAMINATION DECLARED.** Nothing on the blind list was opened. Seen without opening, in the session context: the git
status names three untracked run files of this date for other companies (EMN, INSW, LRN; names only); the recent commit
subjects name four v5 runs of other companies and their boxes (NX OUT at Q2, MTCH TOO HARD (NATURE) at Q1, NWL OUT at Q2,
MD OUT at Q2) and a session-state commit; the auto-memory index line says the queue holds "57 gate-clearers, nothing
buyable". None concerns WWW. A listing of `Test Runs/` filtered for "www" or "wolverine" returned nothing, so no earlier
file on this company was seen. Two earlier run files of other companies (XPEL 2026-09-28, PAYO 2026-09-29) were grepped
only for the form of the computation heading.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $18.94 (close 2026-10-05; Yahoo chart via `tools/run.py`; **aggregator, live quote only**, flagged per
  operator rule 5).
- **Shares by class** from the latest filing's cover: Common Stock, $1 par, **82,066,339** as of 2026-07-27 (10-Q for the
  quarter ended 2026-07-04, filed 2026-08-13, accession `0001628280-26-056524`; `python Screens/cover_shares.py WWW`).
  One class only; the balance-sheet issued count (116.342M) includes treasury shares and is not used.
- **Market cap:** $18.94 x 82.066M = **$1,554M**.
- **Sovereign for the earnings currency:** USD, **5.66%**, 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-05 (`tools/sources.py` through `tools/run.py`; issuing authority). International revenue was 52.2% of 2025
  revenue, but the reporting and owner-cash currency is USD (the XBRL unit of the cash-flow series).
- **Filings read** (operator rule 4):
  - 10-K for fiscal 2025 (year ended 2026-01-03), filed 2026-02-27, `0001628280-26-012614`: Items 1, 1A, 3, 5, 7,
    the balance sheet, Notes 1, 4, 16, 17.
  - 10-Q for the quarter ended 2026-07-04, filed 2026-08-13, `0001628280-26-056524`: MD&A, liquidity, Note 15, tariffs.
  - DEF 14A filed 2026-03-25, `0001140361-26-011157`: annual bonus, long-term plan, summary compensation, pay versus
    performance.
  - 8-K 2026-09-21, `0001628280-26-062912` (President, Active Group position eliminated; Ms. Kuhn left).
  - Earnings-release exhibits for brand revenue: Q4 2025 (8-K `0001628280-26-011956`), Q4 2022
    (`0000110471-23-000018`), Q4 2019 (`0000110471-20-000005`), Q4 2017 (`0000110471-18-000008`).
  - Older 10-Ks for the history: FY2023 `0000110471-24-000057` (Note 20 divestitures, Note 4 impairments), FY2022
    `0000110471-23-000021` (PFAS payments, inventory), FY2021 `0000110471-22-000008` (Sweaty Betty purchase, 2020 Sperry
    impairment), FY2019 `0000110471-20-000008` (environmental costs), FY2017 `0000110471-18-000010` (Stride Rite licence,
    2017 Sperry impairment), FY2012 `0001193125-13-079739` (PLG purchase), FY2009 `0000950123-10-020483` (five-year summary
    2005-2009).
- **One figure cross-checked against the filed statement:** operating cash flow fiscal 2025 **$140.0M** in the 10-K's cash
  flow table (`0001628280-26-012614`, MD&A "Cash Flows") equals the XBRL figure `tools/run.py` printed (140.0); stockholders'
  equity attributable to Wolverine **$408.0M** on the filed balance sheet equals the run.py figure (408).
- `python tools/run.py WWW`, **arithmetic lines only** (Part VII; its rule text, ids and verdicts are not read): OCF, SBC,
  capex and D&A for 2023 to 2025 below; the five-year window prints owner cash of $23.2M (capex basis) and $12.9M (D&A
  basis), against $111.3M and $98.7M on the three-year window, a divergence the tool itself flags. SBC is tagged
  `ShareBasedCompensation` every year; no other stock-pay line, no securities trading inside operating cash, no software or
  intangible payment beside capex. **PFAS settlement payments, remediation payments, the 3M receipt and insurance recoveries
  all run through operating cash** (10-K FY2022 MD&A; 10-K FY2025 MD&A, "a cash outflow of $14.5 million for environmental
  and other related costs, net of cash payments"), so owner cash below is after them.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what Merrell, Saucony, Wolverine, Sweaty Betty and the Cat licence will earn over a
decade, not what the quotation does after a 31% Saucony year. The analyst's habits bear hardest here, because the recent
filings read well (2025 gross margin 47.3%, debt down, earnings per share doubled): look for "what’s wrong in things"
**[M2025-013]**, and treat the outside reading as a means "to possibly reject your original hypothesis" **[M1998-144]**.
**Contrary evidence, written down as found** **[M1997-127]**, in both directions:
- *Against the business (found first):* operating margin over fifteen years averaged 4.7% with three loss years; the
  Sperry trade name was written down in four separate years and the business sold for $97.4M; Sweaty Betty was bought for
  $417.4M in August 2021 and $237.7M of it written off sixteen months later; the Work Group's Wolverine brand fell 23% from
  2021 to 2025; the Cat brand is rented, licence to 2028.
- *For the business (found while reading):* Saucony revenue rose 31.1% in 2025 to $533.1M; gross margin rose 300 basis
  points in 2025 with "the positive impact from recent price increases" (10-K FY2025 MD&A); debt fell from $1,158.0M
  (2022) to $601.1M (2026-07-04); the PFAS litigation is down to one pending suit; $34.0M of IEEPA tariff refunds have been
  claimed and $6.9M received (10-Q Q2 2026).

## THE STANDING RULE
Nothing in this run commits the buyer's money, and no purchase is proposed; were one made, it would be made without
borrowing, which "has no place in the investor's tool kit" **[L2014-005]**, and sized so that nothing is risked "what we
have and need for what we don’t have and don’t need" **[M2012-081]**. No conflict.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the 10-K FY2025 (`0001628280-26-012614`, Item 1):** a designer, marketer and licensor of
  branded footwear and apparel, "Substantially all of the units sourced by the Company are procured from numerous
  third-party manufacturers in the Asia Pacific region"; sold through wholesale accounts, 128 stores and 39 eCommerce sites,
  and through distributors and licensees abroad. Two segments: Active Group (Merrell, Saucony, Sweaty Betty, Chaco; 2025
  revenue $1,407.8M) and Work Group (Wolverine, Cat under licence, Bates, Harley-Davidson under licence, HYTEST; $422.2M).
- **The key variables** **[M1998-044]**, "trying to identify the key variables in that particular business": unit demand
  and full-price sell-through for four or five brands; gross margin (sourcing cost, tariffs, promotion); inventory against
  sales; SG&A and advertising; and the licences. Each is disclosed every year, and the past statements tell me the form of
  the future ones **[M2008-033]**: "the financial statements will tell me the information that’s useful to me".
- **Can I see where it stands in ten years?** The economics of a contract-sourced brand house are not a technology forecast:
  they turn on what customers will choose, the kind of forecast the rows treat as possible, "we know what we think we can
  project out in terms of consumer behavior and threats to a business" **[M2023-030]**. The understanding asked is "a
  reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]**. The fix I have is on the economics: a low-capital, inventory-heavy, fashion-exposed business whose
  earning power follows the heat of a few brands. That fix is enough to put the castle question; whether the castle stands
  is Q2's, and the routing sends a castle shown open to OUT there, not to Q1.
- **The doubt, stated.** The rows warn "it’s easy to sort of think you understand retail, and then subsequently find out you
  don’t" **[M2014-052]**, and "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**. My doubt is not about how the business makes money but about whether its brands will hold, which is the
  castle question itself. Recorded, not hidden.
- **VERDICT: IN**, on the economics as filed **[M2012-065]**, **[M2008-033]**; the doubt above is carried to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" with the warning in the same answer that "most moats aren’t worth a
damn in, you know, in capitalism" **[M1995-038]**.

- **The filer's own account of its position (10-K FY2025, Item 1, "Competition").** "The Company markets its footwear and
  apparel lines in a highly competitive and fragmented environment." "Because of the lack of reliable published statistics,
  the Company is unable to state with certainty its competitive position in the overall footwear and apparel industries. The
  non-athletic footwear and apparel markets are highly fragmented and no one company has a dominant market position."
  "Future sales by the Company will be affected by its continued ability to sell its products at competitive prices and to
  meet shifts in consumer preferences." And Item 1A: "consumers may consider the Company's brands’ images to be outdated".
  That is the industry the rows describe as one with no barrier, where "you better be running very fast" **[M2012-106]**.
- **The money test** **[M2011-015]** ("If the answer had been yes, we wouldn’t have done it."). The company's own record
  is the test run in reverse: with $1,249.5M it bought PLG (Sperry, Saucony, Stride Rite, Keds) in October 2012 (10-K FY2012,
  `0001193125-13-079739`), and with $417.4M it bought Sweaty Betty in August 2021 (10-K FY2021, `0000110471-22-000008`).
  Money bought brands; it did not keep them valuable. Stride Rite went to a licence in July 2017; Keds was sold for net
  proceeds of $83.4M (February 2023) and Sperry for $97.4M (January 2024) (10-K FY2023, `0000110471-24-000057`, Note 20).
  Sperry's trade name alone was written down $68.6M (2017), $222.2M (2020), $191.0M (2022) and $38.3M (2023), and its
  remaining long-lived assets by a further $95.0M to zero before the sale (10-K FY2017 `0000110471-18-000010`; FY2021; FY2023
  Notes 4 and 20). Sweaty Betty's trade name ($189.3M) and goodwill ($48.4M) were written down in Q4 2022, sixteen months
  after the purchase. The rows' word for this is plain: "companies whose moats proved illusory and were soon crossed"
  **[L2007-004]**; the speakers' own diagnosis of such errors, "I misjudged either the competitive strength of the business I
  was purchasing or the future economics of the industry in which it operated." **[L2010-009]**.
- **Widening or narrowing** **[M1999-108]**, "whether it’s likely to widen further or shrink on you"; asked as "could the
  competitive advantage have been made stronger and more durable" **[M2000-075]**. Brand revenue from the company's own
  supplemental tables (earnings releases Q4 2022 `0000110471-23-000018` and Q4 2025 `0001628280-26-011956`), 2021 to 2025:
  Merrell $647.4M to $648.9M (after $764.2M in 2022 and $598.4M in 2024); Saucony $476.2M to $533.1M; Wolverine $227.4M to
  $175.7M; Sweaty Betty $245.4M pro forma to $192.8M. Two of the four disclosed brands shrank by about a fifth, the largest is
  where it was four years ago, and one grew. The 2025 10-K records further declines in Chaco ("softer consumer demand"), Cat
  ("softer consumer demand in the North American market"), HYTEST, Harley-Davidson and Bates. This is the notch the rows
  describe, "we do not think the franchise in 2002 is the same as it was in 1970" **[M2002-005]**.
- **The return the castle protects, against the field, over the whole span** (the competitor row below). Wolverine's
  operating margin averaged **4.7%** over 2011 to 2025 with loss years in 2020, 2022 and 2023; its gross margin averaged
  40.6%. Before the PLG purchase it earned 11.5% (2008), 7.8% (2009), 11.4% (2010) and 12.1% (2011) with long-term debt of
  $1.6M at the end of 2009 (10-K FY2009 five-year summary, `0000950123-10-020483`); in the fourteen years since, it has never
  exceeded 11.2% (2018). A castle "that protects excellent returns on invested capital" **[L2007-004]** is not visible in
  any span of these numbers.
- **The brand in the customer's mind, and the low bid.** "the brand has to stand for something in the consumer’s mind"
  **[M2015-038]**; "you’re probably going to get better gross of margins if they ask for you by name" **[M2023-073]**.
  Wolverine's gross margin, the nearest filed measure of being asked for by name, sat below Deckers, Columbia and Skechers in
  every comparison year, above only Rocky (row below). Revenue in the 10-K is repeatedly explained by "closeout sales"
  (Wolverine, HYTEST, Bates, Chaco in 2025), and the 2022 inventory build (inventories $366M to $745M, +$428.9M in the year,
  10-K FY2022 `0000110471-23-000021`) was cleared in 2023 at a 39.0% gross margin. The test the rows put, whether "it
  wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**, is answered for most of the portfolio by
  the filer's own phrase "its continued ability to sell its products at competitive prices". The wholesale channel adds the
  retailer's pressure: "the value of having the brand moves over to the retailer from the product itself" **[M2001-090]**.
- **Pricing power, the contrary evidence weighed.** 2025 shows price increases holding: gross margin 47.3% against 44.3%
  "primarily due to the benefit of product cost savings, a favorable mix shift toward more full-price sales, and the
  positive impact from recent price increases" (10-K FY2025 MD&A). The rows read pricing power "over time"
  **[M2005-020]**, "over time the businesses with strong competitive positions manage to pass through increases in raw
  material costs" **[M2005-017]**. One year of price increases, in the year Saucony's revenue rose 31%, against fifteen
  years in which the gross margin never exceeded 44.3% before 2025, does not make the case; and the first half of 2026 gave
  back 40 basis points to tariffs (10-Q Q2 2026, gross margin 47.0% against 47.4%).
- **The rented and the rebuilt.** Cat footwear is a licence: "The Cat® license term runs through December 31, 2028 and the
  Harley-Davidson® license term runs through December 31, 2029. Both licenses are subject to early termination for breach."
  (10-K FY2025, Item 1). The castle there belongs to Caterpillar. And a portfolio that must buy new brands as the old ones
  fade (PLG 2012, Sweaty Betty 2021; sales 2017 to 2024) is the case the rows name: "A moat that must be continuously
  rebuilt will eventually be no moat at all." **[L2007-005]**.
- **The speakers' own shoe company.** Of Dexter, a domestic manufacturer, not a brand house, so the parallel is partial:
  "I concluded that Dexter could continue to cope with that problem, and I was wrong." **[L2001-025]**.
- **What could reverse it.** Saucony's run and Merrell's recovery are real in the 2025 and 2026 filings. Whether they last a
  decade is not shown by anything filed; the question at this STOP is whether the castle is standing on the evidence, and the
  evidence over fifteen years is of brands bought, written down and sold, margins at the bottom of the field, and a filer
  that says it competes on price in a fragmented market.

**The competitor row** (each from its own XBRL filings through SEC companyfacts, newest vintage; script
`_research 2026-10-06 WWW/comp.py`, output `comp_summary.txt`; fiscal years aligned to the year in which most months fall).

| Company (latest 10-K accession) | Span | Revenue first to last ($M) | Operating margin, mean of years | Loss years | Gross margin, mean |
|---|---|---|---|---|---|
| Wolverine World Wide (`0001628280-26-012614`) | 2011-2025, 15 yrs | 1,409 to 1,874 (2.1% a year, after $1.67bn of purchases) | **4.7%** (range -7.8% to 12.1%) | 3 | 40.6% |
| Deckers (DECK) (`0001628280-26-037664`) | FY2011-FY2025, 15 yrs | 1,377 to 5,472 | 15.7% | 1 (FY2016, -0.1%) | 50.7% |
| VF Corp (VFC) (`0000103379-26-000030`) | FY2011-FY2025, 15 yrs | 9,459 to 9,605 | 10.2% | 1 (FY2023) | not tagged |
| Columbia (COLM) (`0001050797-26-000028`) | 2011-2025, 15 yrs | 1,694 to 3,397 | 9.7% | 0 | 47.7% |
| Rocky Brands (RCKY) (`0001437749-26-007634`) | 2011-2025, 15 yrs | 240 to 482 | 6.0% | 1 (2016) | 35.7% |
| Skechers (SKX) (`0000950170-25-030016`, its last 10-K; taken private 2025) | 2011-2024, 11 yrs with revenue tagged (2013-2015 untagged) | 1,606 to 8,969 | 6.5% | 1 (2011) | 47.3% |

Over the whole span Wolverine has the lowest mean operating margin of the six, the most loss years, the second-lowest
gross margin, and the second-slowest revenue growth (VF's is slower; Rocky, a smaller boot maker, earned more on sales).
The single year 2025 (8.0%) is above its own mean and still below every peer's mean except Rocky and Skechers. Margins
include each company's own impairments; VF's 2023 loss and Deckers' FY2016 near-zero year are inside their means.

**VERDICT: OUT.** The castle is shown open on the evidence, not merely unjudgeable: the single fact is that over fifteen
years the business earned a 4.7% average operating margin, the lowest of its field, while the brands bought to defend it
were written down and sold at a fraction of cost, in a market the filer itself calls "highly competitive and fragmented"
with sales dependent on "competitive prices". The rows close such a file: "If the answer had been yes, we wouldn’t have done
it." **[M2011-015]**; the cheap, poor or declining business is not rescued by price, "What you can’t do is turn any
investment into a good deal by paying little" **[M2019-015]**; the boxes are "in, out, and too hard" **[M2006-013]**. TOO
HARD was weighed and rejected: that box is for "a moat that’s tenuous in any way" whose value cannot be read, "We don’t
know how to valuate that, and therefore we leave it alone." **[M2000-019]**; here the record reads, and it reads against.

---
## Q3 to Q12: NOT REACHED
Q3 (capital), Q4 (the numbers), Q5 (the people), Q6 (the money and the owners), Q7 (value), Q8 (alternatives), Q9 (debt and
exposures), Q10 (the fat pitch) and Q12 (how the money is made) are **NOT REACHED**. Nothing below is a clearance. Facts the
assignment asked to be read for those questions are recorded under the computation, as record only.

---
## COMPUTATION — NOT A CLEARANCE
*(Reporting at the owner's request, not a rule change. The file closed OUT at Q2; every figure here is arithmetic and
record, carries no entry language, and is not a judgment under Q3 to Q12.)*

### The balance sheets, ten year-ends, read before the income account (Q4's rule, read here because the file closed first)
The rows ask for "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.
From `tools/run.py` (first-filed XBRL; accessions printed there, `0000110471-17-000010` to `0001628280-26-012614`), checked
for 2024 and 2025 against the filed balance sheet in the 10-K FY2025 (2024 equity shown as restated there for the LIFO
change, $312.9M; first filed $307M). USD millions; inventory over the year's revenue.

| Year-end | Equity | Goodwill | Indef. intangibles | Inventory | Inv./sales | Debt on the face | Cash |
|---|---|---|---|---|---|---|---|
| 2016 | 966 | 424 | n/a in run.py | 349 | 14.0% | 821 | 370 |
| 2017 | 950 | 430 | | 277 | 11.8% | 783 | 481 |
| 2018 | 986 | 424 | | 318 | 14.2% | 570 | 143 |
| 2019 | 767 | 439 | | 348 | 15.3% | 798 | 181 |
| 2020 | 561 | 442 | 382 (10-K FY2021) | 243 | 13.6% | 722 | 347 |
| 2021 | 630 | 557 | 718 (10-K FY2021) | 366 | 15.2% | 967 | 162 |
| 2022 | 321 | 485 | 274 (10-K FY2023) | 745 | 27.7% | 1,158 | 132 |
| 2023 | 279 | 427 | 174 (10-K FY2023) | 374 | 16.7% | 921 | 179 |
| 2024 | 313 | 425 | 173 | 241 | 13.7% | 648 | 152 |
| 2025 | 408 | 431 | 180 | 274 | 14.6% | 622 | 206 |

What the figures say: equity fell from $966M to $408M in nine years while the business paid dividends throughout and
bought back $494M of stock in 2018 and 2019 alone; treasury stock stands at 34.3M shares costing $905.1M (about $26.40 a
share) on the 2025 balance sheet. Tangible equity at 2026-01-03 is negative: $408.0M less goodwill $431.3M, indefinite-lived
intangibles $180.2M and amortizable intangibles $29.3M is **-$232.8M**. The indefinite-lived intangibles rose to $718.1M
with Sweaty Betty and fell to $180.2M through the write-downs. Inventory against sales is steady near 14-15% except the
2022 glut (27.7%). Debt rose with each purchase and fell with the sales of brands and the inventory release. What they
cannot say: what the remaining brand values are worth; the impairment tests that carried Sperry's trade name at $296.0M at
the start of 2022 (10-K FY2021 audit report) were wrong in four successive years. What management would like them to say
that the auditors would not: no instance found. One accounting change flatters 2025: the move of certain domestic inventory
from LIFO to FIFO added $3.9M to 2025 net earnings (10-K FY2025, Note 1).

Record for Q4 and Q6 (not judged): the company features "adjusted" results that exclude environmental costs and
reorganization costs that have recurred in most years (2017 restructuring and transformation, 2019, 2023 and 2024
reorganization; earnings releases), the habit the rows read as "wave away very real costs by highlighting"
**[L2016-006]**; the 2025 bonus paid on adjusted pretax earnings of $141M against GAAP pretax earnings of $121.5M (DEF 14A).

### Owner cash after every real cost (operator rule 5; never a net-income proxy)
Owner cash = operating cash flow less stock pay less capital spending (all from the filed cash-flow statements via XBRL;
PFAS payments and recoveries are inside OCF). USD millions.

| Year | OCF | SBC | Capex | D&A | Owner cash (capex basis) | Note |
|---|---|---|---|---|---|---|
| 2016 | 296.3 | 22.8 | 55.3 | 43.5 | 218.2 | still holds Sperry, Keds, Stride Rite retail |
| 2017 | 202.7 | 25.4 | 32.4 | 37.2 | 144.9 | |
| 2018 | 97.5 | 31.2 | 21.7 | 31.5 | 44.6 | |
| 2019 | 222.6 | 24.5 | 34.4 | 32.7 | 163.7 | |
| 2020 | 309.1 | 28.9 | 10.3 | 32.8 | 269.9 | includes 3M's $55.0M lump sum (Q1 2020) and a working-capital release |
| 2021 | 86.8 | 38.1 | 17.6 | 33.2 | 31.1 | PFAS settlements begin |
| 2022 | -178.9 | 33.4 | 36.5 | 34.6 | **-248.8** | inventory +$428.9M; $50.1M PFAS litigation payments and $15.0M to the consent decree |
| 2023 | 121.8 | 15.2 | 14.6 | 35.1 | 92.0 | inventory -$286.5M (the glut released) |
| 2024 | 180.1 | 19.1 | 20.2 | 26.2 | 140.8 | Sperry sold 2024-01-10; insurance recoveries |
| 2025 | 140.0 | 24.4 | 14.5 | 25.9 | 101.1 | |

- **Five-year average (2021-2025), the convention's input:** **$23.2M** (capex basis); **$12.9M** on the D&A variant (D&A
  ran above capex in each of the last five years). Maintenance: the business owns no factories ("avoid capital expenditures
  necessary for owned factories", 10-K FY2025 Item 1) and its 2025 capex was "building improvements, eCommerce site
  enhancements, new retail stores, distribution operations improvements and information system enhancements"; I take
  capex as close to the maintenance need and show the D&A variant beside it.
- **Abnormal year in the window:** 2022 (the inventory glut and the bulk of the PFAS settlements), with 2023 its partial
  mirror. A whole-cycle variant is therefore shown: the **ten-year average 2016-2025, $95.7M**, which spans one full brand
  cycle but includes businesses since sold. The three-year average on the present perimeter (2023-2025) is **$111.3M**,
  shown for reference.

### Value range (the Q7 CONVENTION construction, as computation)
Ten years at the growth shown, then no growth (zero nominal), discounted at the 5.66% sovereign; ends are no growth and
shown growth; per share on 82.066M shares.
- **Growth shown.** On aggregate owner cash 2021 to 2025 the endpoint rate is 34.3% a year, from a depressed base year;
  the rows reject it: "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate"
  **[L2005-003]**, and it runs past the discount rate, which Q3's cap forbids. **CONVENTION of this run:** the shown-growth
  end uses 2023 to 2025 on the present perimeter, **4.83%** a year. Rationale: the only span in the window with neither the
  glut nor the divestitures at its ends. Over the decade the shown growth is negative (-8.2% a year, 2016 to 2025).
- **Convention range, five-year input $23.2M:** **$5.00 to $7.34 a share** ($411M to $602M), top 1.47 times the bottom, so
  not TOO HARD by width. The price, $18.94, is 2.6 times the top: under the convention a price above the top closes OUT
  through the floor.
- **Whole-cycle variant, ten-year input $95.7M:** **$10.89 to $20.61 a share** (the decade's shown decline of 8.2% a year
  carried ten years, to no growth). The price sits inside it, near the top.
- **Present-perimeter reference, three-year input $111.3M:** $23.96 (no growth) to $35.13 (4.83% for ten years). Shown
  because it is the most favourable reading the filings allow; it rests on three years, one of them carrying the glut's
  release, and on a growth rate taken from two data points.

### FAIR PRICE (the price at or below which the central case clears the ~10% pre-tax floor)
- **Central case:** the whole-cycle owner cash, $95.7M a year, **no growth** (the decade's own growth was negative, so no
  growth is the generous centre, not the cautious one).
- **Tax treatment:** owner cash is after tax; grossed up at the 2025 effective rate of 16.9% (10-K FY2025) to $115.2M
  pre-tax. Floor: "at least 10% pre-tax returns" **[L2002-020]**, "we don’t want to buy equities where our real expectancy
  is below 10 percent" **[M2003-149]**, as the CONVENTION at Q7 takes it.
- **On equity:** owner cash is after interest, so the floor is set on the equity value: $115.2M / 10% = $1,152M =
  **$14.04 a share**.
- **On equity plus net debt:** add back after-tax interest ($32.8M x 0.831 = $27.3M), gross up, capitalize at 10%
  ($1,481M), deduct net debt at 2026-07-04 ($601.1M less $158.5M cash = $442.6M): $1,038M = **$12.64 a share**.
- At $18.94 the central case yields **7.4% pre-tax** on equity; the price is above the fair price on both bases. On the
  present-perimeter reference ($111.3M) the fair price would be $16.32 (equity) or $14.92 (with net debt), still below the
  price.

### CHEAP PRICE (below which no pencil is needed)
**Rule of this run (CONVENTION):** the price at which the *low* case, the convention's five-year average with no growth,
itself clears the 10% pre-tax floor on equity; at that price the decision would not need "pencil and paper", the case the
rows call "too close to think about" **[M1996-084]**. $23.2M / 0.831 / 10% = $280M = **$3.41 a share**. (On the D&A variant,
$12.9M, it would be about $1.90.)

| | Per share |
|---|---|
| Price (2026-10-05, aggregator) | **$18.94** |
| Convention value range (5-yr input) | $5.00 to $7.34 |
| Whole-cycle variant (10-yr input) | $10.89 to $20.61 |
| Fair price, central case, equity / equity plus net debt | $14.04 / $12.64 |
| Cheap price | $3.41 |

### Record for the questions not reached (facts read, no judgment)
- **Q6, buybacks and dividends.** $319.2M bought in 2019 and $174.7M in 2018 (XBRL cash-flow line), at prices the treasury
  account averages near $26.40; 900,000 shares at $16.13 in November 2025 under a $150.0M programme of March 2024 that names
  no price (10-K FY2025 Item 5); none in the first half of 2026. Every one of those purchase prices is above the convention
  range's top of $7.34; the rows' law is "what is smart at one price is dumb at another" **[L2011-003]**. The dividend of
  $0.40 a year was paid through the loss years 2020, 2022 and 2023.
- **Q6 Part B, pay.** CEO total compensation $10,854,729 for 2025 against net earnings attributable of $95.8M; bonus metrics
  revenue and adjusted pretax earnings, the revenue threshold ($1,750M) set below the prior year's $1,755.0M; the 2023-2025
  performance units paid 131% although "For 2023, operating profit performance was below threshold", because each later year
  was measured against the year before (DEF 14A `0001140361-26-011157`). Chief executives: Krueger, then Hoffman (to
  2023-08-05), then Hufnagel; independent chairman. SBC $24.4M in 2025, 25% of net earnings.
- **Q9, debt and exposures.** Debt $601.1M at 2026-07-04: $550.0M 4.0% senior notes due 2029-08-15 and revolver borrowings
  under a $600.0M facility maturing 2030-09-24; covenants met. Coverage 2025 on the rows' definition, "pre-tax
  earnings/interest, not EBITDA/interest" **[L2012-002]**: $121.5M / $32.8M = 3.7 times (4.7 times on operating profit);
  in 2020, 2022 and 2023 pre-tax earnings were negative. Pension liability $56.4M; operating leases $168.9M.
- **Q9 and Q12, PFAS.** The tannery in Rockford used 3M's Scotchgard from the late 1950s to 2002; byproducts disposed of at
  House Street and elsewhere "may have contained PFOA and/or PFOS" (10-K FY2025 Note 16). Consent decree of February 2020:
  municipal water to more than 1,000 properties, cap $69.5M, $61.3M paid; 3M paid the company $55.0M in 2020; individual
  suits settled 2022, class action settled 2023 (final approval 2023-03-29); the Landfill Suit settled April 2026; one suit
  pending (the "2025 Suit", motion to dismiss denied 2026-05-06). Reserves at 2026-07-04: remediation $23.3M ($9.5M within
  twelve months, the rest "over the course of up to 25 years") and litigation $8.7M (10-Q Q2 2026 Note 15). Net
  environmental charges in the income statement 2017 to 2025 sum to about $221M after recoveries (35.3, 15.3, 83.5, 11.1,
  56.4, 33.7, -10.4, -10.3, 6.6; 10-Ks FY2017 to FY2025). The filer: "the Company cannot estimate a possible loss or range of
  loss in excess of the associated established reserves", naming changes in drinking-water limits and "efforts to recover
  natural resource damages" among the developments that could change it. The exposure is now paid down to reserves of about
  $32M plus an open tail; it is not what closed this file.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the evidence: fifteen years of the field's lowest operating margin (4.7% mean,
three loss years), brands bought for $1.67bn written down and sold, two of four disclosed brands down about a fifth since
2021, and a filer that says its sales depend on "competitive prices" in a "highly competitive and fragmented" market.
COMPUTATION only: convention range $5.00 to $7.34 (whole-cycle $10.89 to $20.61) against $18.94; fair $14.04 (equity) or
$12.64 (equity plus net debt); cheap $3.41. Not TOO HARD; no research pass is opened.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **not
      committed**; the assignment forbids commits, so write-early by commit was not possible. The file was written in order.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession; no
      number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and the computation is headed as one.
- [x] Owner cash after every real cost (OCF less SBC less capex), never a net-income proxy; the sovereign from the
      issuing authority (US Treasury par curve, 2026-10-05); the price quote flagged as aggregator.
- [x] Contrary evidence written down as found **[M1997-127]** (foundations; Q2, pricing power and what could reverse it).
- [x] No row dated after the anchor is cited (the run is dated today; not a point-in-time run).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before finishing (no commit made); a separate script confirmed no E-ids, every
      M/L/R id present in the v5 ledger, and every quoted fragment beside an id found in that row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a fashion brand house.** The routing says a business whose ten-year economics cannot be foreseen
"because its industry changes fast" closes at Q1, and a castle shown open closes OUT at Q2; it does not say where consumer
fashion sits. Brand heat is a consumer-behaviour forecast **[M2023-030]**, not a technology one, so I passed Q1 on the
economics and let Q2 decide on the record; another analyst could close the same name TOO HARD at Q1 on **[M2002-092]** and
**[M2014-052]**. A sentence placing fashion and brand-heat businesses would remove the fork. (2) **The Q7 growth input when
the window's first year is aberrational.** The convention measures growth on aggregate owner cash over the five years, but
2021 to 2025 gives 34% a year from a depressed base; **[L2005-003]** rejects that, and Q3's cap applies, yet the convention
gives no replacement rule, so I used 2023 to 2025 and confessed it. (3) **The whole-cycle variant and divestitures.** A
ten-year average spans the cycle but includes businesses sold; the framework has no rule for restating owner cash to the
present perimeter. (4) **The cheap price** has no rule in the framework (the screamer is described, not priced); the
run's rule is confessed above. (5) **The em-dash ban against operator rule 3.** The assignment forbids em dashes and the
protocol requires the heading "COMPUTATION — NOT A CLEARANCE" verbatim; the heading is kept as the protocol writes it, the
only em dash in this file outside quoted rows, and no quoted fragment was chosen that contains one. (6) **The fiscal-year
alignment in the competitor row** (Deckers and VF end in March) is a choice of this run; the framework says compare "over
the whole span" but not how to align fiscal years.
