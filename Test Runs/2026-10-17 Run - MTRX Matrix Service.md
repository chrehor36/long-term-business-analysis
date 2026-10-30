# Company Run: Matrix Service Company (Nasdaq: MTRX), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated name before any fetch (commit 8d5c9ad9). Dispatched blind run
under `Screens/_daily/_dispatch_brief.md`, with the two departures the brief states (lines of evidence derived by the analyst
from the 10-K; competitors from the 10-K's own names, or comparable filers as a CONVENTION where it names none). Working
folder `Test Runs/_research 2026-10-17 MTRX/` (notes, fetch and check scripts, the Q7 arithmetic `q7.py` and its output;
raw filings in `cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (2118ccb3): not held; `PORTFOLIO.md` has no line for MTRX or Matrix Service.*

**CONTAMINATION, declared.** (1) The session context showed recent commit subjects of another company's run (LGN, Legence:
"OUT at Q2, after Q1 IN narrowly", "a fixed-price bid contractor with no castle shown") and file names of other research
folders (AYI, ARCB) in the git status. (2) The auto-memory index line shown at session start names queue and gate-clearer
counts ("57 gate-clearers, nothing buyable", wave 7 state). (3) At the very start, before the blind rule was applied with
care, I ran a file-name filter of the `Test Runs/` directory listing for "MTRX" or "matrix" to check that the dated run name
was free; it returned no file. No file was opened and no content read. None of this is used below; the LGN subject is
another company's verdict and is not evidence about this one.

**Lines of evidence chosen, and from where** (the brief's departure (1)). From Item 1: the three segments and their
economics; contract types (fixed-price, time-and-material, cost-plus, MSAs); "We competitively bid most of our projects";
customer concentration; bonding. From Item 1A: competition on price and "willingness to accept contractual risk"; fixed-price
overrun risk; cyclicality of customer capital spending; percentage-of-completion accounting; leadership turnover; surety
and letter-of-credit dependence; multiemployer pensions. From Item 7: segment margins, backlog and its removals, the
customer advances (billings in excess of costs) that drive operating cash, restructuring, the new CEO's plan. From these:
segments and margins over the whole span FY2010 to FY2026; pricing against the low bid; customer advances and working
capital; acquisitions and their goodwill; restructuring as a recurring cost; stock pay; the proxy's pay terms; the late
FY2022 10-K.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $10.02 (close 2026-10-16, via `tools/run.py`'s quote source; an aggregator, flagged per operator rule 5; live quote only).
- **Shares by class** from the latest filing's cover: 28,291,921 common shares outstanding as of 2026-09-02, one class
  (10-K for FY2026, filed 2026-09-03, accession `0000866273-26-000057`; `python Screens/cover_shares.py MTRX` returns the
  same). Checked against the balance sheet: 28,133,850 shares issued and outstanding at 2026-06-30 with zero treasury
  shares (27,888,217 issued less 277,731 treasury a year earlier); the rise to the cover count is restricted-stock vesting
  (the equity statement shows 231,950 shares issued for restricted stock in FY2026). No 8-K or prospectus after the 10-K
  issues shares (8-Ks read: 2026-09-02 results; the earlier 2026 8-Ks are items 2.02 and 5.02).
- **Market cap:** $283.5M (10.02 x 28.292M).
- **Sovereign for the earnings currency (USD):** 5.43%, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2026 (filed 2026-09-03, `0000866273-26-000057`), Items 1, 1A, 2, 5, 7, 7A, 8
  (statements, notes 1 to 14), 9A; DEF 14A filed 2026-09-23 (`0001140361-26-037426`); 8-K of 2026-09-02 and its exhibit 99.1
  earnings release (`0000866273-26-000053`); 8-K of 2025-08-25 (ABL amendment, `0000866273-25-000037`); 8-K of 2022-09-30
  (Nasdaq late-filing notice, `0000866273-22-000097`); 10-K FY2023 (`0000866273-23-000058`, segment note for FY2021 to
  FY2023); 10-K FY2022 (`0000866273-22-000105`, the late-filing note); 10-K FY2021 (`0000866273-21-000088`). The latest
  10-Q (quarter to 2026-03-31, `0000866273-26-000029`) is superseded by the 10-K and was not separately read. Years
  FY2010 to FY2020 are taken from XBRL company facts of the 10-Ks (each frame's accession in
  `_research 2026-10-17 MTRX/notes.md`): transcription, not a substitute for the filed statements, and used only for the
  long margin series and the owner-cash series.
- **One figure cross-checked against the filed statement:** FY2026 revenue $873,632 thousand on the Consolidated Statements
  of Income (10-K page 47) equals the XBRL figure $873.6M and `tools/run.py`'s series; FY2026 operating cash $6,907 thousand
  and capital expenditures $5,483 thousand on the filed cash-flow statement equal `tools/run.py`'s 6.9 and 5.5.
- `python tools/run.py MTRX`, arithmetic lines only (Part VII): owner cash (operating cash less stock pay less capital
  spending) FY2024 $57.8M, FY2025 $100.9M, FY2026 -$5.7M; the five-year window FY2022 to FY2026 averages $16.4M on the
  capital-spending basis and $11.2M on the depreciation basis; capital spending ($5.5M to $7.7M) sits below depreciation
  ($8.6M to $11.0M) in each of the three years. Stock pay resolved: ShareBasedCompensation each year ($7.1M to $8.9M); no
  other stock-pay line, no securities inside operating cash, no intangible or software spending beside capital spending.
  Its v4 lines (the yield, "growth the price assumes", points over the sovereign) are not used.

### The balance sheets, ten year-ends, read before the income account (Q4's instruction, done here because the file closes before Q4) **[M2025-032]**
From `tools/run.py`'s table (first-filed XBRL) checked against the filed FY2026 balance sheet for 2025 and 2026 (USD millions):

| June 30 | assets | equity | cash | receivables | goodwill | intangibles | retained earnings | billings in excess (BIE) | line of credit |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 586.0 | 321.8 | 43.8 | 211.0 | 113.5 | 26.3 | 223.0 | 75.1 | 44.7 |
| 2019 | 633.4 | 352.0 | 89.7 | 218.4 | 93.4 | 19.5 | 239.5 | 105.6 | 5.3 |
| 2021 | 467.6 | 285.5 | 83.9 | 148.0 | 60.6 | 6.6 | 175.2 | 53.8 | 0 |
| 2022 | 440.8 | 227.7 | 52.4 | 153.9 | 42.1 | 4.8 | 111.3 | 65.1 | 15.0 |
| 2023 | 400.5 | 181.5 | 54.8 | 145.8 | 29.1 | 3.1 | 58.9 | 85.4 | 10.0 |
| 2024 | 451.4 | 164.2 | 115.6 | 139.0 | 29.0 | 1.7 | 33.9 | 171.3 | 0 |
| 2025 | 600.3 | 142.7 | 224.6 | 155.0 | 29.0 | 0.6 | 4.5 | 323.6 | 0 |
| 2026 | 602.6 | 141.9 | 223.0 | 172.0 | 28.9 | 0 | 1.9 | 299.9 | 0 |

(2018 and 2020 are in `tools/run.py`'s table and move the same way; BIE from the XBRL contract-liability tags.)

What the figures are saying: retained earnings fell from $239.5M (2019) to $1.9M (2026), so about $238M of losses in seven
years; equity fell by more than half while stock pay was credited to paid-in capital each year; goodwill and intangibles fell
from $139.8M (2017) to $28.9M through impairments ($32.9M FY2020, $18.3M FY2022, $12.3M FY2023 per the XBRL tags) and
amortization. What they do not say on their face: the cash rose from $43.8M to $223.0M while the business lost money, because
customers prepaid. Billings in excess of costs rose from $75.1M to $299.9M; against cash of $223.0M (plus $25.0M restricted)
the company owes $299.9M of work already billed, less $29.2M of costs in excess of billings, so the "debt-free balance sheet
and substantial liquidity" of the earnings release is customers' money held against work not yet done. Receivables have not
outgrown sales (172.0 on $873.6M of revenue in 2026 against 211.0 on $1,197.5M in 2017). Debt: none drawn on the $90M ABL at
2026-06-30. Contrary evidence for the bear reading, written down as found **[M1997-127]**: the advances are themselves a sign
that customers accept upfront billing on the specialty storage work, and the company has carried no borrowings since 2024.

## THE FOUNDATIONS (not a gate)
The foundation that bears here is that a share is a business: "Would I be happy buying this stock if the market closed for
five years?" **[M1997-109]**. The question is therefore what the business earns, not what the price or the earnings release's
"second consecutive quarter of profitability" will do next. The analyst's habit applied throughout: "I’m looking for what’s
wrong in things because that’s part of investing – looking at what you’re missing." **[M2025-013]**. No macro view of LNG,
data-centre power or mining enters; the management's "$7 billion" pipeline is a seller's projection and is not used.
**Contrary evidence, written down as found** **[M1997-127]**: (i) the customer advances are large and real cash; (ii) gross
margin rose from 5.2% to 7.3% in FY2026 and the last two quarters were profitable on GAAP; (iii) the storage segment holds a
perpetual licence to LNG, liquid nitrogen/oxygen and LPG tank technology and a set of patented tank products (10-K Item 1,
Patents); (iv) the board replaced the chief executive in 2026. Each is carried to the question it bears on.

## THE STANDING RULE
The buyer's conduct: the purchase would be made in cash, unlevered, at a size the buyer can hold through a fall of half or
more; nothing in owning a $283M equity stake creates a demand on the buyer for sudden large sums **[L2014-024]**, and
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. No ruin to the buyer from this name. The target's
own surety indemnities and contract risks are Q9's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the chemistry may stay opaque if "I understand the economic dynamics of the
  industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**; the first step is "trying to
  identify the key variables in that particular business, and evaluating how predictable they were first" **[M1998-044]**.
- **The key variables, from the filing.** (1) The volume of awards, which follows customers' capital spending on LNG, NGL,
  power and mining: the 10-K calls demand "cyclical" and "vulnerable to the level of capital and maintenance spending of our
  customers" (Item 1A). Not foreseeable in level or timing. (2) The margin bid on fixed-price work, which made up $682.9M
  of $873.6M of FY2026 revenue (auditor's critical audit matter): set by competitive bidding, "Contracts are generally
  awarded based on price, quality, safety performance, schedule, experience and customer satisfaction" (Item 1,
  Competition), and "Competitive pressures may require us to accept lower margins, assume greater contractual risk"
  (Item 1A). (3) Execution on those bids: overruns "may not be recoverable" (Item 1A). (4) Overhead absorption: "Our
  overhead cost structure is generally fixed in the short term" (Item 1).
- **Are the economics foreseeable?** The level of awards is not, but the economics of the position are: a mid-sized
  bidder for fixed-price industrial construction, paid what the low competent bid allows, with earnings that swing with
  volume and with the outcome of a few large contracts. Sixteen years of filings (FY2010 to FY2026) show that shape without
  a break, and nothing in the 10-K describes a change in it (the new chief executive's plan is to bid, execute and cut
  overhead better, inside the same model). This is not a field of fast technical change; the insiders would write down the
  shape of a contractor's economics, unlike the ten-year forecast of tech companies **[M2000-105]**. The financial
  statements do tell me what the future ones will look like in kind **[M2008-033]**, though not in amount: percentage-of-
  completion estimates are the weakness of the accounts, and that is Q4's.
- **The doubt rule.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.
  My doubt is about the amount and timing of earnings (awards, a few large contracts), which is a question of value and of
  the castle; I have no doubt about what kind of business this is or how its industry works. That doubt does not keep the
  economics outside the perimeter; it is carried to Q2 and Q7.
- **VERDICT: IN, narrowly.** The ten-year economics of a price-bid contractor are foreseeable in kind from its filings
  **[M2012-065]**, **[M2011-014]**; what they show is judged at Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. The moat is what "protects excellent returns on invested capital" **[L2007-004]**.

### The castle tests, each with its filing fact
- **The attacker with money** **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on See’s
  Candy, could I do it? [...] If the answer had been yes, we wouldn’t have done it." Filing: "We compete with local,
  regional, national and international contractors and service providers" and "Some of our competitors may have greater
  financial, technical, personnel or equipment resources, lower cost structures or greater ability to accept contractual
  risk than we do" (Items 1 and 1A). A funded contractor with crews, bonding and a fabrication shop can bid the same jobs;
  the filer says it already faces rivals with lower costs. Answer: yes, it could be attacked, and is.
- **Pricing power and the agony before a rise** **[M2005-020]**: "you can almost measure the strength of a business over
  time by the agony they go through in determining whether a price increase can be sustained." Filing: the price is set
  per bid ("We competitively bid most of our projects"); "Competitive pressures may require us to accept lower margins,
  assume greater contractual risk, or offer more favorable terms to customers"; cost increases may not be passed through
  ("our customer contracts may not allow us to pass through these costs"; of tariffs, "we may be unable to pass through some
  or all of these increases"). Through the inflation of 2021 to 2023 the gross margin fell to 4.9%, -0.2% and 3.9% (FY2021
  to FY2023) from 9.3% in FY2020: costs were not passed on. In FY2026 a Utility and Power award was lost because "Our
  unwillingness to accept an increased risk profile caused the client to change their award decision" (Item 7, backlog
  note 2): the customer, not Matrix, sets the terms.
- **Unit volume and share of mind** **[M1999-054]**: the volume measure this business has is revenue and backlog, not a
  brand. Revenue was $1,416.7M in FY2019 and $873.6M in FY2026; backlog fell from $1,382.1M to $953.2M during FY2026
  (book-to-bill 0.7x), after $197.0M of earlier awards were removed.
- **The low-cost position** **[M1997-010]**: "commodity businesses have risk unless you’re the low-cost producer, because
  the low-cost producer can put you out of business." The cost is read against the competitor **[M2001-013]**, from the
  figures, which "are available" **[M2009-059]**: see the competitor row. Matrix's gross margin is below both broad
  comparable filers in every year from FY2012 to FY2025 (the last year with rival figures), which in a business won on the bid price reads as the higher-cost
  or the weaker bidder, not the low-cost one.
- **The brand in the customer's mind** **[M2008-075]**: the 10-K claims "long-term client relationships, high return of
  repeat customers" and "a number of preferred provider relationships" (Item 1), and also that "Because these significant
  customers generally contract with us for specific projects or for specific periods of time, we may lose these customers
  from year to year". Customer one was 38.3% of Storage and Terminal revenue and customer two 53.3% of Utility and Power
  revenue in FY2026 (Note 13); concentration of that size runs the bargaining power toward the customer.
- **Would the customer still choose it over the low bid?** **[M2017-009]**: the See's question was whether "it wouldn’t be
  a question of people buying candy for the low bid." Here the filer's own words are that contracts are "awarded based on
  price" among other factors and that most projects are "competitively bid". The low bid is the mechanism of the trade.
- **Ask the competitors** **[M1999-130]**: not available on the public record for this name; the rivals' filings are used
  in its place (the competitor row).
- **Widening or narrowing** **[M1999-108]**: "whether it’s likely to widen further or shrink on you." Gross margin averaged
  11.0% over FY2011 to FY2014 and 4.4% over FY2022 to FY2026 (arithmetic mean of the yearly margins); operating margin went
  from about 4% to 5% (FY2011 to FY2014) to a loss in each of FY2020 to FY2026. Narrowing, on the evidence.
- **What could destroy, modify or reduce it** **[M2000-014]**: one large fixed-price contract can erase years of profit (the
  10-K's percentage-of-completion risk factor; the FY2025 $6.4M write-down on "a legacy project completed in fiscal 2021 that
  was in arbitration"); and the loss of one of the three customers each over 10% of revenue.
- **Contrary evidence, written down as found** **[M1997-127]**: specialty cryogenic and LNG storage tanks are a narrow field
  with few builders, and Matrix holds a perpetual licence to LNG and other tank technology plus patented tank products; in
  LNG peak-shaving plants the filer calls the small upgrade projects "key measures of our brand power"; customers pay large
  sums in advance ($299.9M of billings in excess of costs at 2026-06-30); FY2026 gross margin rose to 7.3% and Utility and
  Power earned 11.1% gross and 7.2% operating. Against these: the Storage and Terminal segment, where the licence and the
  tank products sit, earned a gross margin of 0.1% to 6.1% and lost money at the operating line in four of the five years
  FY2022 to FY2026 (the parts table). A niche that protected anything would show in that segment's margins, and it does not.

### The competitor row
The 10-K names no rival (Item 1, Competition: "local, regional, national and international contractors and service
providers"; Item 1A: "regional, national and international contractors"). **CONVENTION of this run:** the three comparable
SEC filers are Primoris Services (PRIM; utility, energy and industrial construction), MYR Group (MYRG; electrical
transmission, distribution and commercial-industrial construction; the comparison for Utility and Power) and Argan (AGX;
power-plant EPC). Rationale: the brief allows comparable filers where the 10-K names none; these three file with the SEC,
bid the same kinds of fixed-price and unit-price industrial work in North America, and report gross profit. No SEC filer was
found whose main business is specialty storage tanks, so the Storage and Terminal comparison is against the broad field
only, said so. Metric: gross margin and operating margin, from each filer's 10-K XBRL facts (Matrix's fiscal year ends June
30; PRIM's and MYRG's December 31; AGX's January 31, shown in the calendar year it mostly covers). Accessions of the latest
10-K read: PRIM `0001104659-26-018677`, MYRG `0000700923-26-000007`, AGX `0001104659-26-035216`.

| year | MTRX GM | MTRX OM | PRIM GM | PRIM OM | MYRG GM | MYRG OM | AGX GM | AGX OM |
|---|---|---|---|---|---|---|---|---|
| 2011 | 11.9% | 4.9% | 12.7% | 6.8% | 11.0% | 3.8% | 16.3% | 8.4% |
| 2012 | 10.8% | 4.3% | 12.5% | 6.2% | 11.9% | 5.6% | 18.0% | 12.7% |
| 2013 | 10.6% | 4.1% | 13.2% | 6.4% | 13.8% | 6.2% | 34.7% | 29.0% |
| 2014 | 10.8% | 4.6% | 11.3% | 5.0% | 14.0% | 6.2% | 21.8% | 16.7% |
| 2015 | 6.5% | 0.7% | 11.4% | 3.5% | 11.5% | 4.2% | 24.1% | 18.0% |
| 2016 | 9.6% | 3.1% | 10.1% | 2.9% | 11.8% | 3.4% | 21.7% | 16.6% |
| 2017 | 6.8% | 0.4% | 11.7% | 4.5% | 8.9% | 2.1% | 16.7% | 12.0% |
| 2018 | 8.4% | -1.0% | 11.1% | 4.4% | 10.9% | 3.3% | 17.1% | 8.3% |
| 2019 | 9.3% | 2.7% | 10.7% | 4.5% | 10.3% | 2.8% | -2.9% | -23.4% |
| 2020 | 9.3% | -3.3% | 10.6% | 4.7% | 12.3% | 3.9% | 15.8% | 5.9% |
| 2021 | 4.9% | -6.5% | 11.9% | 4.9% | 13.0% | 4.7% | 19.6% | 8.7% |
| 2022 | -0.2% | -12.4% | 10.3% | 4.4% | 11.4% | 3.8% | 19.0% | 9.2% |
| 2023 | 3.9% | -6.7% | 10.3% | 4.4% | 10.0% | 3.5% | 14.1% | 6.4% |
| 2024 | 5.6% | -4.1% | 11.0% | 5.0% | 8.6% | 1.6% | 16.1% | 10.1% |
| 2025 | 5.2% | -4.6% | 10.7% | 5.4% | 11.6% | 4.6% | 20.5% | 14.3% |
| 2026 | 7.3% | -1.1% | | | | | | |

(AGX revenue for 2021 to 2025 is its cost of revenue plus gross profit, its revenue tag not being carried in those frames.)
Over the whole span Matrix's gross margin is below PRIM's in every year and below MYRG's in every year but 2011; its
operating margin is below PRIM's in every year but 2016 and below MYRG's in every year but 2011. Cumulative
operating income FY2010 to FY2026 was about -$48M on about $16B of revenue (sum of the XBRL OperatingIncomeLoss series).

### The parts table (Note 13 of the FY2026 10-K for FY2024 to FY2026; Note 13 of the FY2023 10-K for FY2022 and FY2023; USD millions)

| part | op. income FY22 / 23 / 24 / 25 / 26 | five-year op. income | five-year revenue | gross margin FY22 to FY26 | castle | decides |
|---|---|---|---|---|---|---|
| Storage and Terminal Solutions | -24.4 / -10.6 / -8.5 / -9.2 / +3.1 | -49.6 | 1,589.5 | 0.1%, 4.1%, 4.1%, 4.0%, 6.1% | none shown | yes, largest by revenue |
| Utility and Power Infrastructure | -23.1 / +3.6 / +0.3 / +3.8 / +20.3 | +4.9 | 1,105.6 | -3.9%, 6.3%, 5.0%, 6.8%, 11.1% | none shown | yes, largest by operating income |
| Process and Industrial Facilities | -10.1 / -17.4 / +11.3 / +0.5 / -2.6 | -18.3 | 1,177.5 | 3.6%, 2.9%, 8.2%, 5.8%, 3.4% | none shown | no |
| Corporate (unallocated) | about -30 each year | -152.7 | | | | |

The company's five-year operating income is -$215.6M (segments -$63.0M), so no part carries more than half of a positive
total, and the fallback, "the largest part decides" (Q2, A business of parts, CONVENTION), does not say largest by what. I
apply it both ways and the answer is the same. Utility and Power, the largest by operating income and the only part with a
positive five-year sum, had one good year in five (operating margin -10.5%, 2.1%, 0.2%, 1.5%, 7.2%); its gross margin sat
below MYR Group's in each of the five years (11.1% in FY2026 against MYRG's 11.6% for 2025); its backlog fell from $346.4M to
$145.7M in FY2026 (book-to-bill 0.4x) after a client moved an award away over risk terms; its transmission and distribution
line is being wound down (Item 7, investing activities); and one customer was 53.3% of its FY2026 revenue. Storage and
Terminal, the largest by revenue and the home of the tank licence and products, lost money at the operating line in four of
five years on gross margins of 0.1% to 6.1%. Neither part shows a castle; the filer's own words on both are bidding on price.

### The field's returns over the last full cycle
Judged in words, as the CONVENTION asks. The broad comparable filers earned thin, positive, ordinary margins on revenue over
the whole span (Primoris 2.9% to 6.8% operating, MYR Group 1.6% to 6.2%), with Argan, a power-plant EPC, higher in most years
and at -23.4% in 2019; "the improvement you get one day, your competitor gets the next day" **[M2004-053]**, and a field can
stay poor with few rivals on a job: "you can have only two competitors and they’re still terrible businesses"
**[M2013-052]**. Matrix itself, over a span that includes the FY2014 and FY2019 peaks and the FY2022 trough, earned less than
the ordinary field and in total lost money. A castle that protects excellent returns **[L2007-004]** is not in the evidence,
for the field or for Matrix.

### The change for the better claimed by the management
The new chief executive's plan and FY2026 (gross margin 7.3%, two GAAP-profitable quarters, SG&A down 11%) are the claim.
The framework credits a change for the better only on a full cycle in which the price behaviour held **[M2005-020]** (Q2,
Change, and what it does to a castle, CONVENTION), and none has passed. I do not close TOO HARD (NATURE) on it, for a reason
stated so it can be checked: crediting FY2026 in full, the business would earn a 7.3% gross margin and a -1.1% operating
margin, still below the ordinary returns of the comparable filers in the same year. The improvement, if it held through a
downturn, would bring Matrix toward the ordinary field; it would not show a castle. So the change-for-the-better question
does not decide the box (see What in the framework was wrong or unclear).

### Why OUT and not TOO HARD
The castle is shown open on the evidence, not merely unknowable: the filer says the price is bid and that rivals with lower
costs and more capital compete for the same work; its margins sit below the field's in nearly every year for fifteen years;
and the field's own returns are ordinary. "In an unregulated commodity business, a company must lower its costs to
competitive levels or face extinction." **[L1994-035]**; "there are some industries that are just never going to have
barriers to entry." **[M2012-106]**. The rows about the gas station, the textile mill and the airline are about named
businesses and are weighed, not applied as verdicts (Q2, A row about one company, CONVENTION); the box rests on the filings.

- **VERDICT: OUT.** No castle is shown for either deciding part; the business bids on price, earns below an ordinary field,
  and the field's own returns are ordinary **[M2011-015]**, **[M2005-020]**, **[M1997-010]**, **[L2007-004]**. The file
  closes here; Q3 to Q12 are NOT REACHED.

## Q3 to Q10, Q12: NOT REACHED
The file closed at Q2 (operator rule 2). Nothing below is a clearance. Q11 belongs to a holding review.

---
## THE BOX
**OUT, decided at Q2** (no castle shown in either deciding part; a price-bid contractor earning below an ordinary field
over FY2011 to FY2026); after Q1 IN narrowly. Integrity facts recorded, not judged (the late FY2022 10-K and its cause; pay
on an adjusted figure while GAAP operations lost money; see AFTER THE STOP, Q5). COMPUTATION beneath the stop, all-equity
basis: value range $13.26 to $17.93 a share against $10.02, fair price $12.23 (equity-only $4.35), both resting on cash that
is customers' advance payments; before the advance build, no positive value (see Q7 below).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.*

**Q3 (capital).** Equity $141.9M and tangible equity about $113M at 2026-06-30 (10-K balance sheet); operating income was
negative in every year FY2020 to FY2026 (XBRL series), so the return on the capital employed in those years was negative.
Acquisitions FY2011 to FY2018 cost $125.9M in cash (XBRL PaymentsToAcquireBusinessesNetOfCashAcquired); goodwill
impairments of $32.9M (FY2020), $18.3M (FY2022) and $12.3M (FY2023) followed (XBRL GoodwillImpairmentLoss). Capital spending
ran below depreciation in every year FY2020 to FY2026 (capex $3.3M to $18.5M; D&A $8.6M to $19.1M) and above it in FY2019
($19.6M against $18.2M); the filing gives no maintenance figure.

**Q4 (the accounts).** Revenue on fixed-price work is recognised by percentage of completion ($682.9M of $873.6M in FY2026;
the auditor's critical audit matter); the 10-K's risk factor says earlier reported profit can be reversed when estimates
change. Operating cash is dominated by customer advances: billings in excess of costs moved +$85.9M (FY2024), +$152.3M
(FY2025) and -$23.6M (FY2026). Restructuring has been charged in six consecutive years ($6.8M FY2021, $19.0M FY2022
including goodwill, $15.5M FY2023 including goodwill, $0.5M FY2024, $3.6M FY2025, $10.0M FY2026; 10-K income statements
and the FY2023 segment note). The earnings release of 2026-09-02 (`0000866273-26-000053`, exhibit 99.1) headlines "Adjusted
net income" of $7.4M for FY2026 and "Adjusted EBITDA" of $16.0M, the latter excluding stock-based compensation and
restructuring, against a GAAP net loss of $2.6M; its headline speaks of the "second consecutive quarter of profitability" on
the adjusted figure. Full valuation allowance on deferred tax assets since FY2022; federal NOLs of $61.7M carry forward
indefinitely (10-K tax note).

**Q5 (the people).** The FY2022 10-K was filed late (Form 12b-25 on 2022-09-12; Nasdaq notice 8-K of 2022-09-30,
`0000866273-22-000097`). The FY2022 10-K (`0000866273-22-000105`) gives the cause: "employee support and oversight time for
a certain project was allocated to our general overhead expense category rather than to the specific project to which it
should have been allocated"; the audit committee's outside review found the amount immaterial and no material weakness.
The chief executive (Hewitt) separated on 2026-06-30, the chief financial officer on 2026-09-10 and the chief
administrative officer on 2026-05-07; the chief operating officer (Payne) became chief executive on 2026-07-01 (DEF 14A
`0001140361-26-037426`). The FY2026 annual incentive paid on "The combination of adjusted operating income and net interest
income", which the proxy says "was positive for our largest operating company, MSI, and at the consolidated level", in a year
of a $9.6M GAAP operating loss. Hewitt's FY2026 total compensation was $6,741,465, including $1,600,000 cash severance (two
years of salary) and equity awards modified so that their service condition was deemed satisfied. Director Miller is
not independent because his son is the company's General Counsel. The fiscal 2024 performance-share award paid nothing
(relative TSR below threshold). The proxy lists 520,796 shares for all directors, nominees and executive officers as a group
(10 persons), about 1.8% of the cover count; the new chief executive held 46,834 shares.

**Q6 (the money and the owners).** No dividend ever; the ABL forbids dividends and limits buybacks to $2.5M a year. Buybacks
under the 2018 programme name no price; amounts by year (XBRL PaymentsForRepurchaseOfCommonStock): $8.1M FY2012, $5.0M FY2015,
$10.5M FY2016, $5.2M FY2019, $17.0M FY2020, none since; the prices paid were not read. Stock pay ran $6.3M to $11.9M a year
FY2015 to FY2026, about 2.5% of the present market value a year in FY2026; share count rose from 27.4M (FY2024 weighted) to
28.3M (cover). Q6's buyback test against the bottom of Q7's range is not run, the file being closed before Q6.

**Q9 (ruin of the target).** No borrowings at 2026-06-30; ABL of $90M (borrowing base $65.4M, availability $60.9M), first
lien on all assets, maturing 2029-09-09; $25.0M of cash restricted under it at all times; $4.5M of letters of credit plus a
$20.0M project letter of credit issued after year-end. $237.2M of surety bonds in force, which the company indemnifies.
Contracts "require us to indemnify our customers for injury, damage or loss". Multiemployer pension plans with more than 100
local unions; withdrawal liability "not currently able to determine". Three customers were each over 10% of FY2026 revenue
(20.1%, 17.5%, 10.0%).

---
## Q7 COMPUTATION, NOT A CLEARANCE: the reporting figures (Part VII, The owner's price)
*Arithmetic only, in `_research 2026-10-17 MTRX/q7.py` and `q7_output.txt`. The file closed at Q2; nothing here is a
verdict or entry language (operator rule 3).*

**Inputs.** Owner cash after every real cost = operating cash less stock pay less capital spending less cash paid for
businesses net of businesses sold (specific (c)); working capital counted (specific (d)). All-equity basis: before interest
(interest income on cash removed, interest expense added back), against market value plus net debt. Net debt at 2026-06-30:
no borrowings, no finance leases, unrestricted cash $223.0M, so net debt is -$223.0M; operating leases left out ($22.9M of
future payments), and the $25.0M of restricted cash left out as unavailable while the ABL stands; both said so. Company's own
tax: actual, near nil (owner cash after the cash taxes paid); the federal NOLs carry forward indefinitely, so the statutory
recompute for a shelter that runs out inside ten years does not apply. Rate 5.43% (US Treasury 30-year, 2026-10-16). Shares
28.292M.

**The cycle base (specific (a)).** The literal window's first year, FY2022, is the trough of owner cash in the sixteen years
read (-$65.4M) and the lowest operating margin (-12.4%); so the base is the last full cycle, with the series defined by owner
cash: peaks at FY2014, FY2018 and FY2025, troughs at FY2012, FY2017 and FY2022. The last full cycle, peak FY2018 to peak
FY2025, is FY2019 to FY2025: owner cash before interest averages $15.44M (after interest $15.42M). The prior cycle
(FY2015 to FY2018) averages -$4.65M before interest with its acquisitions deducted, so the growth between cycles changes sign
and is meaningless; by specific (b) the growth is measured between the halves of the cycle: $5.27M (FY2019 to FY2021) to
$51.59M (FY2023 to FY2025). That rate traces to an absurdity: sales over the same halves fell from $1,063.7M to $764.2M, and
the rise is the customer-advance build. By specific (f) ("any result that traces to an absurdity is cut back"), the growth
carried is the business's own sales growth over the same halves, -7.93% a year (midpoints FY2020 to FY2024); a decline, so by
specific (b) it is the bottom and the no-growth case is the top. Specific (e): the filing allows no maintenance guess
(capital spending is below depreciation in every year of the cycle but FY2019, and no split is given); all spending is deducted, and the depreciation
variant (base $10.33M) is lower. No business was bought in the cycle; businesses sold for $3.9M (FY2019) and $6.3M (FY2023) are
credited.

**(a) VALUE RANGE, central figure, all-equity basis: $13.26 to $17.93 a share, against $10.02.** (Top: $15.44M a year at no
growth; bottom: the same base declining 7.93% a year for ten years, then flat; each whole-business value plus $223.0M net
cash, divided by 28.292M shares.) Width top to bottom 1.87 to 1. Floor test: at ten percent the no-growth case is worth
$13.34 and the decline case $11.13 a share, both above the price.
Equity-only beside: $5.37 to $10.04 a share.

**(b) FAIR PRICE: $12.23 a share on the all-equity basis** (each end valued at ten percent, averaged, after the company's own
tax); **equity-only: $4.35 a share.** The two differ by the $223.0M of cash, which the all-equity basis adds and the
equity-only basis leaves out (its owner cash carries the interest earned on that cash instead).

**Beside, as the convention asks.** The literal five-year window FY2022 to FY2026: owner cash $14.6M before interest; the
series changes sign and its halves do too, so the no-growth case alone, $17.38 a share all-equity (fair $13.04). The ten
years FY2017 to FY2026: $12.72 to $14.94 (fair $11.20). **Before the customer-advance build** (specific (d), the run's
reading that the FY2024 and FY2025 inflows are the upfront billings the filer ties to its large fixed-price contracts): over
FY2019 to FY2025, $204.5M of the owner cash was the rise in billings in excess of costs; without it the cycle's owner cash is
-$13.8M a year, and with the cash counted net of what customers have prepaid (cash $223.0M less billings in excess $299.9M
plus costs in excess $29.2M = -$47.8M) the value is about -$10.65 a share. **The central figure counts the customers'
prepayments twice**: once in owner cash as they arrived, and again as the $223.0M of cash they left on the balance sheet.
The framework's net-debt rule ("borrowings and finance leases less cash and securities, as the filing states them") and its
working-capital rule, applied together to a contractor funded by its customers' advances, produce that double count; I
report the central figure as the text builds it and flag it (see What in the framework was wrong or unclear). The
operator's alert, if one is set from this file, should be read with this paragraph.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 8d5c9ad9); written question by question; committed after Q1
      (c315ca83), after Q2 (306c7fe0) and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock `Screens/_daily/_overnight.lock` was present,
      written by the dispatching session (2026-10-17T06:46); folding is the dispatcher's (operator rule ten). This run binds
      nothing until it is in the register.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened: none was opened, but a file-name filter of the
      `Test Runs/` listing for "MTRX" or "matrix" was run at the start, which the blind rule counts as listing; it returned
      nothing. Declared under contamination with the commit subjects and memory line seen; none used. Box left unticked for
      that reason.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `_research 2026-10-17 MTRX/check_ids.py`); every filing
      fact carries its document and accession; numbers come from the filings, the XBRL facts or the scripts in the folder.
- [x] The order was kept; Q2 closed the file; everything after it is under AFTER THE STOP or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (operating cash less stock pay less capital spending less acquisitions); never net
      income; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (foundations, the balance sheets, Q2); facts for later questions under AFTER
      THE STOP; the integrity flag in the box line.
- [x] Not a point-in-time run; rows of any date may be cited.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit (2026-10-17); the run's own check
      (`_research 2026-10-17 MTRX/check_ids.py`): no E-ids, 29 ids all resolve, 19 quoted fragments all in their rows.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts rule when the whole loses money.** Q2's business-of-parts CONVENTION says a part decides at more than half of
five-year operating profit, "or else the largest part", without saying largest by what. Here the five-year total is
negative and the largest part by operating income (Utility and Power, +$4.9M) is not the largest by revenue (Storage and
Terminal). I judged both; they agreed, so the gap did not decide this file, but it would where the two parts differed.
(2) **The change for the better, when crediting it would not show a castle.** The CONVENTION sends an uncredited improvement
to TOO HARD (NATURE) "on that question". It does not say what happens when the improvement, credited in full, would still
leave returns below an ordinary field. I closed OUT on the reasoning that the question then cannot change the box; a sentence
saying so would stop the next analyst from closing such a file TOO HARD (NATURE). (3) **Customer advances counted twice in
Q7.** For a contractor whose cash is its customers' prepayments, counting the working-capital inflow in owner cash (specific
(d)) and also subtracting the resulting cash from net debt (On what the floor is earned) values the same dollars twice, and
turns a business whose owner cash before advances is negative into a fair price above the market. The floor-plan CONVENTION
treats inventory-secured trade finance as working capital to avoid a double charge; no rule treats billings in excess of
costs, the mirror case, to avoid a double credit. I reported the text's figure and the before-advance figure beside it. (4)
**Which cycle is "the last full cycle".** Specific (a) allows peak to peak or trough to trough on owner cash; for this series
the two give FY2019 to FY2025 ($15.4M) or FY2018 to FY2022 (about $2.2M), and the text does not choose. I took the latest
complete cycle and showed the ten-year and literal-window figures beside. (5) The template's self-audit has no line for a
file-name search done before the blind rule was applied; I declared it rather than tick the box.
