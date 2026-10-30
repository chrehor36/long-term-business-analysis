# Company Run: United Parks & Resorts Inc. (NYSE: PRKS), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Every judgment cites a v5 ledger id in bold;
every filing fact carries its accession; the STOP that returned OUT closed the run and the later questions are marked NOT
REACHED. Working folder: `Test Runs/_research 2026-10-05 PRKS/` (filings as text, `value.py` with the arithmetic,
`rows.py` and `check_ids.py` for the id checks).

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`,
so whether the operator holds PRKS is unknown to the analyst.

**CONTAMINATION, declared.** (1) A directory listing of `Test Runs/` showed the names (not the contents) of the other
2026-10-05 run, holding-review and research-pass files, and of a file dated 2026-07-16 named "Consumer & Leisure 6-pack
(HOG THO PRKS BYD ASO SBH)", which is a pre-v4.1 file about this company; none was opened. (2) The session context showed
the commit subjects of the PENN, YELP, ROCK and ENR runs of 2026-10-05 and a session-state commit; they name no verdict on
PRKS. (3) The memory index loaded with the session says the wave-7 queue had 57 gate-clearers and "nothing buyable"; it
names no company. Nothing else about PRKS was seen before the filings were read.

**LOCK.** `Screens/_daily/_overnight.lock` did not exist when checked and was not written: the dispatching instruction
limited this session to this file and its working folder. Recorded as a departure from CLAUDE.md's "an interactive
session running a name writes this lock first".

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $34.45 (2026-10-05, printed by `tools/run.py`; aggregator quote, flagged under operator rule 5, live quote only).
- **Shares, one class:** 45,341,309 as of 2026-07-31, cover of the 10-Q for the quarter ended 2026-06-30, filed
  2026-08-07, accession `0001193125-26-340383` (`python Screens/cover_shares.py PRKS`). Shares issued 97,447,598, of which
  treasury 52.1 million at 2026-06-30 (same 10-Q, statement of stockholders' deficit).
- **Market cap:** $1,562M (34.45 x 45.341M).
- **Sovereign for the earnings currency (USD):** 5.66%, 30-year par yield, US Treasury daily par yield curve, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 filed 2026-03-03, accession `0001193125-26-088288` (Items 1, 1A in
  part, 7, the balance sheet, the stockholders' deficit and debt notes); 10-Q for the quarter ended 2026-06-30, accession
  `0001193125-26-340383`; DEF 14A filed 2026-04-30, accession `0001193125-26-197833`; 8-K of 2026-09-22, accession
  `0001193125-26-398139` (a President appointed beside the CEO; the Chief Commercial Officer resigned). For the fifteen-year
  span, the MD&A tables of the 10-Ks for FY2013 (`0001193125-14-109073`), FY2015 (`0001564590-16-013463`), FY2017
  (`0001564590-18-003622`), FY2019 (`0001564590-20-007020`), FY2020 (`0001564590-21-009459`), FY2021 (`0001564590-22-007356`),
  FY2023 (`0000950170-24-023162`) and FY2024 (`0000950170-25-030398`). Yearly cash-flow lines 2011 to 2025 from the XBRL
  company facts (transcription), cross-checked as below.
- **One figure cross-checked against the filed statement:** net cash from operating activities 2025, $380,085 thousand in
  the FY2025 10-K cash-flow summary (Liquidity section), against 380.1 in the XBRL facts and in `tools/run.py`. Also total
  stockholders' deficit $(435,806) thousand and total assets $2,616,274 thousand on the filed balance sheet, against -436
  and 2,616 in the tool's table.
- **`tools/run.py` arithmetic lines only** (its v4 material ignored, Part VII): owner cash after SBC and all capex 183.0
  (2023), 218.0 (2024), 145.4 (2025); five-year mean 245.3; D&A basis five-year mean 306.7. SBC from the cash-flow
  statement: 17.0, 13.7, 17.2 ($M, 2023 to 2025), complete (the Adjusted EBITDA reconciliation's equity compensation line,
  17.96, 14.6, 17.8, includes payroll taxes). Finance-lease principal 0.9 to 1.5 a year, immaterial.

**Owner cash by year** ($M; OCF less SBC less all capital spending; cash taxes as paid; the arithmetic is
`_research 2026-10-05 PRKS/value.py`):

| year | OCF | SBC | capex | owner cash | D&A | "core" capex (filer) | attendance (000) | revenue | operating income |
|---|---|---|---|---|---|---|---|---|---|
| 2011 | 268.2 | 0.8 | 225.3 | 42.1 | 213.6 | n/a | 23,631 | 1,330.8 | 144.3 |
| 2012 | 303.5 | 1.2 | 191.7 | 110.6 | 167.0 | n/a | 24,391 | 1,423.8 | 226.8 |
| 2013 | 289.8 | 6.0 | 166.3 | 117.5 | 166.1 | n/a | 23,391 | 1,460.2 | 201.2 |
| 2014 | 261.5 | 2.3 | 154.6 | 104.6 | 176.3 | n/a | 22,399 | 1,377.8 | 160.6 |
| 2015 | 286.3 | 6.5 | 157.3 | 122.5 | 182.5 | n/a | 22,471 | 1,371.0 | 159.4 |
| 2016 | 280.4 | 37.5 | 160.5 | 82.4 | 199.6 | n/a | 22,000 | 1,344.3 | 59.6 |
| 2017 | 192.5 | 23.2 | 172.5 | -3.2 | 163.3 | n/a | 20,798 | 1,263.3 | -201.4 (goodwill impairment 269.3) |
| 2018 | 293.9 | 22.2 | 179.8 | 91.9 | 161.0 | 177.2 | 22,582 | 1,372.3 | 151.7 |
| 2019 | 348.4 | 11.1 | 195.2 | 142.1 | 160.6 | 171.8 | 22,624 | 1,398.2 | 213.2 |
| 2020 | -120.7 | 7.5 | 109.2 | -237.4 | 150.5 | 94.7 | 6,373 | 431.8 | -241.7 |
| 2021 | 503.0 | 39.7 | 128.9 | 334.4 | 148.7 | 69.4 | 20,203 | 1,503.7 | 432.0 |
| 2022 | 564.6 | 18.2 | 200.7 | 345.7 | 152.6 | 131.9 | 21,939 | 1,731.2 | 507.5 |
| 2023 | 504.9 | 17.0 | 304.8 | 183.1 | 154.2 | 226.2 | 21,606 | 1,726.6 | 459.8 |
| 2024 | 480.1 | 13.7 | 248.4 | 218.0 | 163.4 | 177.7 | 21,547 | 1,725.3 | 463.3 |
| 2025 | 380.1 | 17.2 | 217.5 | 145.4 | 174.5 | 182.4 | 21,169 | 1,662.6 | 365.4 |
| LTM to 2026-06-30 | 410.0 | 19.3 | 245.2 | 145.5 | | | H1: 9,275 vs 9,625 | H1: 761.6 vs 777.2 | H1: 108.6 vs 157.4 |

Sources: attendance from the five-year and two-year tables of the 10-Ks named above (2010 to 2013 from FY2013; 2014, 2015
from FY2015; 2016, 2017 from FY2017; 2018, 2019 from FY2019; 2020 from FY2020; 2021 from FY2021; 2022, 2023 from FY2023;
2024 from FY2024; 2025 from FY2025); "core" capex ("park rides, attractions and maintenance activities", unaudited) from
the FY2019, FY2021, FY2023 and FY2025 10-K capital-expenditure tables; H1 2026 from the 10-Q `0001193125-26-340383`.
Operating income 2011 to 2025 from the XBRL facts; the 2025 figure matches the FY2025 10-K ($365,436 thousand).

**The balance sheets, read first** **[M2025-032]** (ten year-ends from `tools/run.py`, checked against the filed FY2025
and 2026 Q2 statements; $M):

| year-end | assets | equity | goodwill | cash | receivables | debt (face) | retained earnings | treasury stock at cost |
|---|---|---|---|---|---|---|---|---|
| 2016 | 2,379 | 461 | 336 | 69 | 37 | 1,583 | 8 | 155 |
| 2017 | 2,086 | 287 | 66 | 33 | 38 | 1,542 | -195 | 155 |
| 2019 | 2,301 | 211 | 66 | 40 | 50 | 1,548 | -59 | 403 |
| 2020 | 2,566 | -106 | 66 | 434 | 30 | 2,193 | -372 | 415 |
| 2022 | 2,326 | -438 | 66 | 79 | 71 | 2,111 | 176 | 1,325 |
| 2024 | 2,574 | -462 | 66 | 116 | 79 | 2,244 | 638 | 1,830 |
| 2025 | 2,616 | -436 | 66 | 100 | 77 | 2,248 | 806 | 1,989 |
| 2026-06-30 | n/r | -617 | 66 | 19 | n/r | 2,290 | 835 | 2,208 |

What the figures say. (a) **The asset base has not grown in ten years**: total assets 2,379 (2016) and 2,616 (2025),
while capital spending of 2016 to 2025 ran about level with depreciation; the parks are being kept, not enlarged.
(b) **Equity went from +$461M to -$617M**, and the cause is on the face of the statement: treasury stock at cost rose from
$155M to $2,208M while retained earnings recovered only to $835M. About $2.05B of shares were bought in 2018 to mid-2026
(treasury value 2017 155 to 2026-06 2,208), for roughly 45.6 million shares; the cumulative cost of all 52.1 million
treasury shares averages about $42.4 a share against $34.45 today (computation from the 10-Q's treasury line and share
count). (c) **Debt rose from $1,548M (2019) to $2,290M (2026-06-30)**, the 2020 closure borrowing never repaid, and the
revolver was drawn ($50M at June 30; $80M borrowed after December 31, 10-K FY2025) while cash fell from $99.8M to $19.1M
in the half-year in which $220.3M was spent on buybacks (10-Q cash-flow statement). (d) **Goodwill was written down by
$269.3M in 2017** (10-K FY2017: "Due to financial performance, particularly late in the second quarter of 2017 at our
SeaWorld Orlando park"). (e) **Receivables doubled** from 37 to 77 on revenue up 24%; the FY2025 10-K records an
"approximately $8.6 million one-time non-cash write-off of certain accounts receivable balances". (f) Deferred revenue
$143M (2025) against $153M (2024), a falling advance book; deferred tax liabilities $258M against $213M, cash taxes paid
$17.5M in 2025 against a provision of $58.2M. (g) The filer's own split of capital spending was **re-cut after the fact**:
2023 "core" capex was $181.9M with $123.0M "expansion" in the FY2023 10-K, and $226.2M "core" with $78.6M "expansion" in
the FY2025 10-K, the same year's dollars. What the figures cannot say: how much of the "core" line is the price of
standing still, which the filer answers only in words (Q3 below would have weighed it; the run closed first).

---
## THE FOUNDATIONS (not a gate)
A share is bought as the business: would I be content "if the market closed for five years?" **[M1997-109]**. The price
has fallen from the $52 to $60 a share the company itself paid in 2021 to 2024 (computation, treasury cost over shares
acquired by year) to $34.45; the quotation "doesn’t tell us anything. It just tells us prices." **[M2006-077]**, so the fall
is read for nothing and the work is on attendance, price and capital. Who is paid to tell: the filer measures itself and
pays its managers on Adjusted EBITDA (DEF 14A: "Achievement of a predefined Adjusted EBITDA target", 75% weighting), and
its debt covenants run on a "Covenant Adjusted EBITDA" that adds $43.0M of "Estimated cost savings" (10-Q, last twelve
months); the projector is not asked, "don’t ask the barber whether you need a haircut" **[M2011-083]**. The analyst's
habit: look for "what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) margins after 2020 are far above the company's own past and above the regional peers (Q2 competitor row); (2) the
company owns about 2,000 acres in five states (10-K FY2025, Item 1) and holds the exclusive US theme-park licence for
Sesame Street through 2031, extended 15 years plus a 5-year option for each new standalone park (10-K FY2025, Sesame
License Agreement); (3) per-capita revenue rose faster than prices in 2019 to 2023. Each is weighed in Q2.

## THE STANDING RULE
A cash purchase of a listed share, unlevered and sized so that its loss would not touch what the buyer has and needs,
puts the buyer at no risk of ruin: "We are never going to risk what we have and need for what we don’t have and don’t
need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt is
Q9's matter and was not reached.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, found by "trying to identify the key variables in that particular business,
  and evaluating how predictable they were first" **[M1998-044]**.
- **The key variables, from the filer's own words:** "Our revenues are driven primarily by attendance in our theme parks
  and the level of per capita spending" (10-K FY2025, Item 7); against them a cost base the filer calls "relatively fixed
  because the costs for employees, maintenance, animal care, utilities, property taxes and insurance do not vary
  significantly with attendance" (Item 1A); and a capital need it states as "Maintaining and improving our theme parks, as
  well as opening new attractions, is critical to remain competitive" (Item 1, Capital Improvements). Three variables
  (visits, price per visit, the capital to keep the visits) and one fixed cost line. Each has fifteen years of filed
  history above.
- **Foreseeable?** The forecast is about consumer behaviour, not technology: "we know what we think we can project out in
  terms of consumer behavior and threats to a business." **[M2023-030]**. A theme park changes slowly; nothing in the
  filings shows an industry whose insiders would refuse to write the ten-year economics down **[M2000-105]**: the filer
  itself publishes per-capita and attendance drivers and peers do the same. The things that cannot be foreseen
  (hurricanes, a documentary, a pandemic) are shocks to a stable model, and the model itself is plain.
- **Doubt test** **[M2002-092]**: I do not doubt that I understand how a regional and destination theme park makes and
  loses money; what I doubt is whether this one's position holds, which is Q2's question, not Q1's.
- **VERDICT: IN.** The economics are knowable from the filings and do not turn on fast technology **[M2012-065]**,
  **[M1998-044]**, **[M2023-030]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. Every castle earning high returns is assaulted **[L2007-004]**.

**1. Unit volume, the first evidence.** "We measure it by unit cases sold and by shares outstanding. And we want a lot
more unit cases sold." **[M1999-054]**. PRKS's unit is the visit. Attendance (thousands): 24,391 in 2012, 23,391 (2013),
22,399 (2014), 22,471 (2015), 22,000 (2016), 20,798 (2017), 22,582 (2018), 22,624 (2019), 6,373 (2020), 20,203 (2021),
21,939 (2022), 21,606 (2023), 21,547 (2024), 21,169 (2025), and 9,275 in the first half of 2026 against 9,625, down 3.6%
(10-Ks as listed in Step 0; 10-Q `0001193125-26-340383`). **Thirteen years below the 2012 peak; down 13.2% from it, and
down in each of the last four reported periods.** The filer's reasons for the declines are named in its own words:
2014, "negative media attention in California, along with a challenging competitive environment, particularly in
Florida. Part of the challenges in Florida relate to significant new attraction offerings at competitor destination
parks" (10-K FY2015); 2017, "the combined impact of reduced national advertising and competitive pressures" and "public
perception issues, which resurfaced since we reduced marketing spend on our national reputation campaign" (10-K FY2017);
2025, "a decline in visitation from international markets and reseller tickets along with changes in operating schedules
across parks and less than optimal execution" (10-K FY2025); 2026, "unfavorable weather conditions, a decline in
visitation from international markets, and an Easter holiday shift" (10-Q). With a cost base the filer calls fixed, a
falling visit count is the newspaper's arithmetic: "Fixed costs are high in the newspaper business, and that's bad news
when unit volume heads south." **[L2006-009]**.

**2. Pricing power, and the agony before a rise.** "you can almost measure the strength of a business over time by the
agony they go through in determining whether a price increase can be sustained." **[M2005-020]**; "you learn a lot about
the durability of the economics of a business by observing the behavior of" the price, the same row. Admission per
capita: $39.37 (2013), $38.37 (2014), $37.69 (2015), $37.17 (2016), $36.79 (2017), $35.37 (2018), $35.48 (2019), $42.17
(2021), $44.00 (2022), $44.16 (2023), $43.61 (2024), $41.73 (2025), $42.21 in H1 2026 against $42.79 (10-Ks as listed;
10-Q). **The ticket price fell in nominal dollars in five consecutive years, 2014 to 2018, while volume also fell**, and
the filer gave the reasons as "an increase in promotional offerings" (2015), "free promotional ticket offerings" (2017);
it has **fallen again in 2024, 2025 and the first half of 2026**, again with volume falling: "lower pricing on certain
promotional admission products" (10-K FY2024); "the impact of promotional activities" (10-K FY2025). Whole span: total
revenue per capita $62.43 (2013) to $78.54 (2025), +25.8%, against US CPI-U annual average 232.957 to 321.943, +38.2% (BLS
series CUUR0000SA0): **real revenue per visit down about 9% and visits down about 9.5% over twelve years; real revenue
down about 18%** (computation). A business that cuts its price when volume falls and still loses volume has the
"prayer session" **[M2005-020]**. The row on overpricing is the Kellogg case, a company that "pushed their pricing too
far" **[M2001-087]**; the PRKS evidence fits the same row's last sentence: "once you start losing share, it’s hard to get
back." **[M2001-087]**.

*Contrary evidence on price, written down:* from 2019 to 2023 total revenue per capita rose from $61.80 to $79.91 (+29%)
against CPI +19.2% (255.657 to 304.702), and operating margin went from 15.2% to 26.6%; for four years the price held
with visits nearly flat. That is real pricing power for a period. It is weighed against what followed: since 2023 the
admission price, the visits and the margin (26.9% in 2024, 22.0% in 2025, 14.3% in H1 2026 against 20.2%) have all
fallen together.

**3. The money test.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?
[...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. Here the attack is not hypothetical and it is
funded. The filer: "Principal direct competitors of our theme parks include theme parks operated by The Walt Disney
Company, Universal Parks and Resorts" and "Certain of our direct competitors have substantially greater financial
resources than we do" (10-K FY2025, Item 1A); "The Orlando theme park market is extremely competitive" (Item 1); and
"Approximately 59%, 16% and 13% of our revenues in 2025 were generated in the States of Florida, California and Virginia".
Disney spent $8,024M on "Investments in parks, resorts and other property" in FY2025 alone (DIS 10-K FY2025, accession
`0001744489-25-000155`), 4.8 times PRKS's whole 2025 revenue; Comcast opened Epic Universe in Orlando in May 2025 (CMCSA
10-K FY2025, `0001628280-26-004994`: "driven by the opening of Epic Universe in May 2025"). PRKS's 2025 and 2026
attendance fell in the year the third Universal park opened in its largest market; the filer does not name Epic Universe
in its 10-K or 10-Q (text search, no instance), so the link is not proved by the filer, but the money test does not need
it: "one competitor is frequently enough to ruin a business." **[M2012-108]**.

**4. The low-cost position.** PRKS is not the low-cost operator in its main market; it is the smallest of three operators
in Orlando by revenue and capital (Disney Experiences revenue $36,156M FY2025; Comcast Theme Parks $9,836M 2025; PRKS
$1,663M total). It competes on price: "Our highly differentiated products provide a value proposition and a complementary
experience to those offered by fantasy-themed Disney and Universal parks" (10-K FY2025, Item 1). The value position is
held by the promotional discounts named in item 2. "you do not want to have something whose competitive position is going
to erode over time." **[M2007-117]**.

**5. The brand in the customer's mind.** The SeaWorld brand was the company's name until February 2024, when the
corporate name became United Parks & Resorts (10-K FY2025, opening note); the park brands stay. The filer itself lists
"the external perceptions of our brands and reputation have at times impacted relationships with some of our business
partners, including certain ticket resellers that have terminated relationships with us" (10-K FY2025, Item 7,
Attendance). California's 2016 law "codified the end of captive breeding programs" for orcas (10-K FY2017). The brand
carries a standing reputational exposure the filer names in four risk factors; it is not the brand of "a promise"
customers ask for by name in preference to the rival next door.

**6. Would the customer still choose it over the low bid?** The filer's own pricing language is "promotional activities",
"promotional offerings", "advance purchase discounts" and "demand-based pricing for select peak time periods at some of
our parks" (10-K FY2025). The evidence is that the customer is bought with price: the reverse of "it wouldn’t be a
question of people buying candy for the low bid" **[M2017-009]**.

**7. The competitor row** (same metrics, from the competitors' own filings, over the span each filing allows):

| operator | attendance, start to end | revenue, start to end | operating margin, start / end | source |
|---|---|---|---|---|
| PRKS | 23.4M (2013) to 22.6M (2019) to 21.2M (2025) | $1,460M to $1,398M to $1,663M | 13.8% (2013), 15.2% (2019), 26.6% (2023), 22.0% (2025) | 10-Ks as Step 0 |
| Cedar Fair | 23.5M (2013) to 27.9M (2019) to 26.7M (2023) | $1,135M to $1,475M to $1,799M | 26.6% (2013), 21.0% (2019), 17.0% (2023) | `0000811532-14-000042`, `0000811532-20-000029`, `0000811532-24-000035` |
| Six Flags (old) | 26.1M (2013) to 32.8M (2019) to 22.2M (2023) | $1,110M to $1,488M to $1,426M | 20.4% (2023) | `0000701374-14-000018`, `0001558370-20-001092`, `0000701374-24-000009` |
| Six Flags (merged, FUN) | 47.4M (2025) | $3,100M (2025) | operating loss $(1,375)M after $1,518M impairment of goodwill and intangibles; about 4.6% before it | `0001999001-26-000048` |
| Disney parks | not disclosed | Parks and Resorts $14,087M (FY2013), Experiences $36,156M (FY2025; segment redrawn) | 15.8% (FY2013), 27.6% (FY2025) | `0001001039-14-000228`, `0001744489-25-000155` |
| Universal (Comcast) | not disclosed | $5,933M (2019) to $9,836M (2025) | Adjusted EBITDA only: 41.4% to 31.3%, not comparable | `0001166691-20-000008`, `0001628280-26-004994` |

Read over the whole span, not one year. **From 2013 to 2019, before the pandemic and the price reset, the two regional
peers grew visits by 19% (Cedar Fair) and 26% (Six Flags) while PRKS lost 3%; PRKS's operating margin (4% to 16%, and
negative in 2017) sat below Cedar Fair's (21% to 27%) every year of that span.** After 2020 the order reversed: PRKS's margin (27% to 29% in
2021 to 2024) passed Cedar Fair's 17% (2023) and the merged Six Flags' single digits (2025), a gain the regional peers
did not share and which PRKS has been giving back since 2024. The destination rivals in its main market grew revenue and
profit by multiples over the span (Disney's parks operating income $2,220M FY2013 to $9,995M FY2025 with a redrawn
segment; Universal's revenue +66% 2019 to 2025). The regional industry as a whole is not a castle either: the merged Six
Flags wrote off $1.5B of goodwill and intangibles in 2025. The competitors' own answer to the silver-bullet question
**[M1999-130]** is not on the record; no scuttlebutt was done.

**8. Widening or narrowing; the moat that must be rebuilt.** The number-one question of a year: "could the
competitive advantage have been made stronger and more durable" **[M2000-075]**, and "whether it’s likely to widen further
or shrink on you." **[M1999-108]**. The filer states that new rides every year are the price of staying in the game
("critical to remain competitive"), and spends on them: a new coaster or land at most parks every year (Item 1, Capital
Improvements), record capital spending of $304.8M in 2023, $248.4M in 2024, $217.5M in 2025, each above depreciation.
Visits fell in each of those years. "A moat that must be continuously rebuilt will eventually be no moat at all."
**[L2007-005]**; "in those industries, you better be running very fast because there are a lot of other people that are
going to be running and looking at what you’re doing" **[M2012-106]**. The evidence here is not of a rebuilding that
holds the line; it is of rebuilding while the line moves back.

**9. What could destroy, modify or reduce it** **[M2000-014]**: 59% of revenue in one state exposed to hurricanes and
freezes (Milton closed the Florida parks 14 operating days in 2024; a "historic winter freeze in our Florida parks" cost
$6.9M of repairs in H1 2026, 10-Q); animal-welfare regulation the filer lists as pending (APHIS proposed rules of 2016 and
2023); activist and media attention, which the filer has twice blamed for falling visits (2014, 2017); and the destination
rivals' capital in Orlando. Slow change "can lull you to sleep easier" **[M2014-038]**: the thirteen-year volume decline
is that kind.

**What keeps it standing, the case for, stated as its holder would** **[M2016-055]**: about 2,000 owned acres in
markets where "the limited supply of real estate suitable for theme park development" constrains new parks (Item 1), a
zoological collection the filer calls "extremely difficult and expensive to replicate", an exclusive Sesame licence, and
margins since 2021 above its regional peers. This is a real asset base, and something like "an asset that couldn’t be
duplicated" **[M2012-030]** may be true of the land and the animals. But the rows ask about the castle's earning power,
not its replacement cost, and the filed record of the earning power is: visits down for thirteen years against regional
peers that grew, the price cut whenever volume fell, the post-2020 margin gain reversing, and an annual rebuilding that
has not held attendance against rivals spending many times its revenue in the same city.

**Routing.** A castle shown on the evidence to be filling in closes OUT; one whose future cannot be judged closes TOO
HARD **[M2006-013]**. I considered TOO HARD (WORK) on one question, whether the 2021 to 2023 price reset is durable, and
rejected it: the answer is already in the filings for 2024, 2025 and H1 2026, where price and volume both fell, and the
whole-span fact (real revenue per visit and visits both down about 9% from 2013 to 2025 while the regional peers grew
volume to 2019) is a single fact, not a forecast. The cheap price does not reopen it: "What you can’t do is turn any
investment into a good deal by paying little" **[M2019-015]**; "If you really think a business is declining, most of the
time you should avoid it." **[M2012-062]**.

- **VERDICT: OUT.** The castle is shown open on the filed evidence: unit volume down thirteen years **[M1999-054]**,
  **[L2006-009]**; price cut when volume falls **[M2005-020]**; a moat that must be rebuilt every year and is not holding
  **[L2007-005]**; a funded attacker in its largest market **[M2011-015]**, **[M2012-108]**.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED (the file closed at Q2). Facts gathered for the record: "core" capex (rides, attractions, maintenance) $171.8M
to $226.2M in every normal year 2018 to 2025 except the post-closure holiday (2021 $69.4M, 2022 $131.9M), against
depreciation of $148.7M to $174.5M.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion.
NOT REACHED. Facts gathered for the record (Step 0 holds the balance-sheet reading): the filer features Adjusted EBITDA and
pays on it; the reconciliation adds back "business optimization, development and strategic initiative costs" in every
year shown ($33.9M 2023, $18.4M 2024, $15.1M 2025, $27.7M LTM) and ride and equipment write-offs ($29.0M 2025, $29.3M LTM),
and the covenant measure adds projected "Estimated cost savings" ($43.0M LTM). "The one figure we regard as utter nonsense
is the so-called EBITDA." **[M1998-086]**. Coverage on the rows' own definition, "pre-tax earnings/interest, not
EBITDA/interest" **[L2012-002]**: LTM pre-tax income $182.1M plus interest $130.2M over interest $130.2M, about 2.4 times
(10-Q LTM reconciliation; computation).

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED. Facts gathered for the record: Hill Path Capital owns about 53.2% (27,205,306 shares at 2025-12-31, 10-K
FY2025), a holding that passed 50% through the company's buybacks, not its own purchases (the Stockholders Agreement caps
its own buying at 34.9%, DEF 14A); its founder chairs the board and the compensation committee; "certain members of our
Board, including our Chairman of the Board, are actively involved in overseeing certain key operating activities" (10-K
FY2025, Item 1). Chief executives since 2015: the chief executive resigned effective January 15, 2015 (10-K FY2015), Manby stepped down February
2018 (10-K FY2017), Rivera appointed November 2019 and resigned April 2020 (10-K FY2019, FY2020), Swanson since. The CFO
hired in late 2024 left in 2025 (DEF 14A); the Chief Commercial Officer resigned in September 2026 (8-K).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts gathered: buybacks of $215.7M (2021), $693.6M (2022), $17.9M (2023), $482.9M (2024), $160.4M (2025),
$220.3M (H1 2026) (XBRL; 10-Q), at average prices near $58, $56, $60, $52, $38 and $37 (treasury cost over shares
acquired, computation), against "Continuing shareholders are hurt unless shares are purchased below intrinsic value."
**[L2011-003]**; the programmes name a dollar amount and no price (10-K FY2025, Note 18). The nine non-employee directors who
served the full year were paid $433,841 to $672,640 each in 2025, most in stock (DEF 14A), against a CEO salary of $450,000; "A director getting $150,000
a year from a company, who needs it, is not an independent director." **[M2005-090]**. The 2024 amendment requires a
special committee and a disinterested-holder vote for any take-private proposed by Hill Path (DEF 14A), a protection for
the minority.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner asked for the range, the fair price and the cheap price as a report; they follow
below under COMPUTATION - NOT A CLEARANCE and carry no entry language.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts gathered: debt $2,290M at 2026-06-30 (Term B-3 $1,515M due December 2031; senior notes $725M at 5.25%
due August 2029; revolver $50M drawn, $700M facility due August 2029); cash $19.1M; net debt about $2,271M, about 3.9
times the filer's own LTM Adjusted EBITDA of $584.9M (an EBITDA, used only because the covenant is written on it); the
covenant net leverage, on the larger covenant figure, 3.55 times, with buybacks permitted while pro forma leverage stays at
or below 4.25 (10-Q).

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Not a named business; the zoological display is an open question for the operator, not asked here.)

---
## COMPUTATION - NOT A CLEARANCE
*Made at the owner's request after the file closed OUT at Q2. It is arithmetic, not a judgment of value, and it carries
no entry language (operator rule 3). Every number is from `_research 2026-10-05 PRKS/value.py`.*

**(a) Value range, by the Q7 CONVENTION** (Part VI: owner cash after every real cost, five-year average, carried at the
growth shown on the aggregate owner cash, never above it, ten years, then zero nominal growth, at the sovereign 5.66%
**[L2000-021]**; "working with a range of possibilities is the better approach" **[L2000-024]**):
- Base: owner cash 2021 to 2025 averages **$245.3M** (after SBC and all capital spending; cash taxes as paid). Depreciation
  variant $306.7M; filer's "core" capex variant (2023 to 2025 only) $243.6M.
- Growth shown on the aggregate: $334.4M (2021) to $145.4M (2025), **-18.8% a year**. Since the shown growth is negative,
  the no-growth case is the top of the range and the shown-growth case the bottom.
- **Range: $1,068M to $4,334M of equity, $23.54 to $95.59 a share, against $34.45.** Top to bottom 4.06 to 1, wider than
  the convention's three to one: had Q7 been reached, this range would close TOO HARD, "the range must be so wide that no
  useful conclusion can be reached" **[L2000-025]**.
- **The window holds abnormal years.** 2021 was the reopening year, with "core" capex of $69.4M, and 2022 still ran at
  $131.9M, against $171.8M to $226.2M in every other year 2018 to 2025; both years' owner cash ($334.4M, $345.7M) is
  inflated by capital not spent. **Whole-cycle variant** (CONVENTION of this run, ours: fifteen years 2011 to 2025, which
  hold the 2013 to 2017 reputational decline, the 2017 trough and the 2020 closure; put on an enterprise basis, because
  debt rose by about $700M within the span, by adding back interest at 75%, a tax shield close to the 25.7% effective rate
  of 2025): unlevered owner cash averages $197.6M; at 5.66% and no growth that is $3,490M of enterprise value, less net
  debt $2,271M, **$1,219M of equity, $26.89 a share.** The span's own growth is not used because the visit count and real
  price per visit both fell over it.
- For comparison, the three years after the capital holiday (2023 to 2025) average $182.2M, no growth, **$70.98**; the last
  twelve months $145.5M, no growth, **$56.70**. These are no-growth perpetuities of a cash stream whose volume has fallen
  for thirteen years; they are the generous end, not a central case.

**(b) Fair price** (the price at or below which the central case clears the floor CONVENTION of about 10% pre-tax,
**[M2003-149]**):
- Central case (CONVENTION of this run): owner cash averaged over 2023 to 2025, the three full years after the capital
  holiday ended, **$182.2M**, held flat in nominal dollars (a real decline of about the inflation rate, consistent with the
  record), cash taxes as paid. **Tax treatment:** the figure is after the company's income taxes as actually paid and
  before any tax of the shareholder; the 10% is applied to it as the shareholder's pre-tax return. Cash taxes have run below
  the provision (deferred taxes averaged $57.5M a year in 2023 to 2025, from accelerated depreciation), and that deferral is
  kept in the central case while capital spending continues.
- **FAIR PRICE about $40.18** ($182.2M / 10% / 45.34M shares). Expected return at $34.45: about 11.7%.
- Variants: with the full tax provision charged (deferred taxes deducted), $124.7M, **$27.50**; on the last twelve months
  ($145.5M), **$32.09**. At $34.45 the price is below the central fair price by about 14% and above both variants.

**(c) Cheap price** (below which no pencil is needed; CONVENTION of this run, ours): the price at which the **fifteen-year
whole-cycle owner cash, re-levered to today's interest bill** (unlevered $197.6M less LTM interest $130.2M after the 75%
shield, $99.9M) earns the 10% floor with no growth at all: **$22.03 a share.** Rationale: it assumes no recovery, keeps
every trough of record inside the average, and leaves the buyer comfortable "if they closed down on the stock market for a
couple of years" **[M2007-096]**; the margin is set wide because the business is volatile, "the more volatile the business
is [...] the larger the margin of safety." **[M1997-080]**. The price, $34.45, is 56% above it.

*Reading of the computation, not a clearance:* at $34.45 the central case needs a pencil, "it’s too close to think about"
**[M1996-084]**, and the range is too wide for a useful conclusion **[L2000-025]**. A low price was never going to reopen
Q2 **[M2019-015]**.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the filed evidence: visits down 13% from 2012 and falling again in 2025 and
2026; admission price cut in five straight years 2014 to 2018 and again 2024 to H1 2026; real revenue per visit down about
9% over 2013 to 2025 while the regional peers grew visits by 19% to 26% to 2019; record capital spending in 2023 to 2025
did not hold attendance against Disney and Universal in the market that gives 59% of revenue. Not reached: Q3 to Q12.
Computation only: range $23.54 to $95.59 (five-year convention, 4.06 to 1), whole-cycle $26.89, fair about $40.18 (full
tax $27.50; LTM $32.09), cheap about $22.03, against $34.45.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **not done**;
      the file was written in one pass after the reading, and no commit was made (the dispatching instruction forbade
      commits). Write-early was not kept.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row
      (`_research 2026-10-05 PRKS/check_ids.py`, run before close); no E-id is cited; every filing fact has its accession;
      numbers without a filing carry a source (BLS CPI-U) or are labelled computation or CONVENTION.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; Q3 to Q12 NOT REACHED; the valuation is under COMPUTATION - NOT A
      CLEARANCE with no entry language.
- [x] Owner cash after SBC and all capital spending, never a net-income proxy; the sovereign from the US Treasury; the
      price flagged as an aggregator quote.
- [x] Contrary evidence was written down as found (Foundations; Q2 items 2 and the case for).
- [x] No point-in-time anchor: rows of any date may be cited (Part VII's rule does not bind a present-day run).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [ ] The lock was not written (see LOCK above).
- [x] `python tools/check_framework.py`: PASS on 2026-10-05 after this file was written; `check_ids.py`: 46 ids, all
      present, every adjacent quoted fragment found in its row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The Q7 convention breaks when the shown growth is negative.** It says the range's two ends are "the no-growth case
and the shown-growth case" and that growth is "carried forward at the growth the business has actually shown [...] never
above it". With owner cash falling 18.8% a year over a window that starts in a capital-holiday year, the "shown-growth
case" compounds a decline produced by catching up deferred spending, and the "no-growth case" capitalises a five-year
average inflated by the same holiday; the 4.06-to-1 width is mostly an artefact of the window, not of the business. I
reported the convention as written and added a whole-cycle variant on an enterprise basis; a rule for a window holding an
abnormal year (and for negative shown growth) is missing. (2) **The convention's equity basis assumes the debt load is
stable across the window.** PRKS's debt rose about $700M within the span while its share count halved; averaging
after-interest owner cash across years of different leverage mixes two capital structures. I used an unlevered average
less today's net debt for the whole-cycle figure; the framework says nothing on it. (3) **The template's operator-rule-3
heading carries an em dash** between "COMPUTATION" and "NOT A CLEARANCE" while the operator's standing rule forbids em dashes; I wrote
"COMPUTATION - NOT A CLEARANCE". (4) **"Maintenance" capital is left to the analyst's judgment at Q3**, and the filer's own
split was re-cut after the fact ($44M of 2023 spending moved from "expansion" to "core" between the FY2023 and FY2025
10-Ks); the framework has no instruction for a filer's unaudited capex split that changes between filings. (5) **Q2's OUT
versus TOO HARD line** turns on whether the castle is "shown" filling in or its future "cannot be judged"; PRKS had a real
four-year period of pricing power (2019 to 2023) inside a thirteen-year decline. I treated the whole-span fact as deciding
and the four years as contrary evidence; the framework gives no rule for which span governs when a recent run contradicts
the long one. (6) The tax treatment for the fair price (cash taxes as paid against the provision) is not addressed by the
Q7 convention; deferred taxes of about 30% of owner cash move the fair price from $40.18 to $27.50.
