# Company Run - M/I Homes, Inc. (NYSE: MHO) - 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The template says to check `PORTFOLIO.md`; the blind rule of
this assignment forbids opening it. The analyst does not know whether the operator holds MHO.

**CONTAMINATION, declared before any verdict.** (1) A directory listing of `Test Runs/` showed the file name
`2026-07-16 Run - Homebuilders 6-pack (KBH MHO TMHC MTH DFH CCS).md`, a pre-v4.1 run that includes this company. It was
not opened; only its name was seen. (2) The same listing showed the names of twelve other 2026-10-06 run files and their
research folders (ADT, ASO, BCC, BTU, GPOR, HRMY, NSIT, PATK, PTEN, REYN, TPC, WKC); none was opened. (3) The session
context carried recent commit subjects: PATK Patrick Industries "OUT at Q2; filer, its rival LCI and its customer Thor all
describe low barriers and price competition", BCC Boise Cascade "OUT at Q2 [...] builders moving to trusses", ASO Academy
Sports "OUT at Q2", and an addendum on the OSIS and BCC runs quoting the framework's phrase beside M2000-019. These are
building-products and retail names, two of them suppliers to homebuilders; they show a pattern of Q2 OUT on the same day
and could prime the same verdict here. The analyst also saw, in the memory index, the phrase "57 gate-clearers, nothing
buyable". None of these names MHO's verdict. The Q2 verdict below rests on MHO's own filings and its five competitors' own
filings, cited by accession.

Working folder: `Test Runs/_research 2026-10-06 MHO/` (filings as text, the fetch and arithmetic scripts
`fetch.py`, `facts.py`, `peers.py`, `compare.py`, `ownercash.py`, `value.py`, `squash.py`, `row.py`).

---
## STEP 0 - THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $132.00 (close 2026-10-05; the chart source in `tools/sources.py`, an aggregator, flagged per operator rule 5;
  live quote only).
- **Shares by class** from the latest filing's cover: 25,283,031 common shares, par $.01, one class (10-Q for the period
  ended 2026-06-30, filed 2026-07-31, accession `0000799292-26-000028`; cover count as of 2026-07-29;
  `python Screens/cover_shares.py MHO`). Issued 30,137,141, treasury 4,899,455 at 2026-06-30 (the 10-Q balance sheet).
- **Market cap:** $132.00 x 25.283M = $3,337M.
- **Sovereign for the earnings currency (USD):** 5.66%, the US Treasury daily par yield curve, 30-year, 10/05/2026 (the
  issuing authority; `python tools/run.py MHO`, which calls `tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-13, accession `0000799292-26-000006`: Item 1 in full, the risk factors on margins and
    incentives, MD&A (results, segments, land, liquidity), the four statements, the notes on inventory, debt, land options,
    warranty, bonds.
  - 10-Q Q2 2026, filed 2026-07-31, accession `0000799292-26-000028`: statements, MD&A, debt and repurchase notes.
  - DEF 14A filed 2026-04-10, accession `0001193125-26-150356`: CD&A, summary compensation table, ownership footnotes.
  - 8-K of 2026-07-29, accession `0000799292-26-000025` (the cover only; the press release exhibit was not read).
  - Earlier 10-Ks for the cycle: FY2005 `0000799292-06-000009`, FY2008 `0000799292-09-000010`, FY2010
    `0000799292-11-000010`, FY2012 `0000799292-13-000005`, FY2015 `0000799292-16-000048`, FY2018 `0000799292-19-000008`,
    FY2020 `0000799292-21-000032`, FY2022 `0000799292-23-000037`, FY2023 `0000799292-24-000014`, FY2024
    `0000799292-25-000018` (selected financial data, cash-flow statements, the downturn narrative). XBRL company facts
    for 2009 to 2025 as transcription only.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities 2025, $137,349
  thousand in the filed cash-flow statement (10-K FY2025, `0000799292-26-000006`), against 137.3 printed by `tools/run.py`.
  Agrees. Shareholders' equity 2025, $3,166,190 thousand filed, against 3,166 printed. Agrees.
- `python tools/run.py MHO` arithmetic lines (its v4 ids, floor and wording ignored, Part VII): OCF 2023/2024/2025
  552.1 / 179.7 / 137.3; SBC 11.4 / 14.6 / 17.0; D&A 15.8 / 17.4 / 18.9; capex 5.8 / 8.4 / 9.6; its "OE capex" 535.0 /
  156.8 / 110.7. **Its OE is incomplete for this business:** it omits the land invested through joint ventures, which the
  filer puts in investing activities ($59.2M in 2025, $54.1M in 2024), the proceeds of mortgage-servicing-right sales,
  preferred dividends in the years they were paid, and acquisitions. The full owner-cash table below replaces it.

### Owner cash after every real cost, 2006 to 2025 ($M; transcribed from the filed cash-flow statements above)
Owner cash = operating cash flow - stock pay - property and equipment bought + property sold - land invested in joint
ventures + capital returned from them - acquisitions + mortgage-servicing rights sold - preferred dividends. The
"warehouse-adjusted" column adds the net change in the mortgage subsidiary's repurchase-facility borrowings, because
operating cash flow carries the mortgage loans it originates and holds for days while the matched warehouse borrowing sits
in financing (CONVENTION of this run, shown beside the strict figure, never instead of it; rationale: the loans and their
funding are one transaction split across two sections of the statement).

| year | OCF | owner cash (strict) | warehouse-adjusted | net income | pre-tax income | revenue |
|---|---|---|---|---|---|---|
| 2006 | -104.0 | -128.8 | -128.8 | 38.9 | 45.3 | 1,274.1 |
| 2007 | 202.2 | 177.8 | 188.3 | -128.1 | -150.9 | 1,016.5 |
| 2008 | 148.9 | 141.8 | 136.5 | -245.4 | -215.1 | 607.7 |
| 2009 | 68.5 | 64.3 | 53.3 | -62.1 | -93.0 | 569.9 |
| 2010 | -37.3 | -42.9 | -34.8 | -26.3 | -27.4 | 616.4 |
| 2011 | -34.0 | -42.8 | -22.4 | -33.9 | -33.9 | 566.4 |
| 2012 | -47.0 | -56.1 | -40.7 | 13.3 | 12.7 | 761.9 |
| 2013 | -74.0 | -110.4 | -98.3 | 151.4 | 41.3 | 1,036.8 |
| 2014 | -132.7 | -160.5 | -155.1 | 50.8 | 69.7 | 1,215.2 |
| 2015 | -82.2 | -132.6 | -94.3 | 51.8 | 87.0 | 1,418.4 |
| 2016 | 34.2 | -7.6 | 21.6 | 56.6 | 91.8 | 1,691.3 |
| 2017 | -52.5 | -71.4 | -56.1 | 72.1 | 120.3 | 1,962.0 |
| 2018 | -2.6 | -142.6 | -157.6 | 107.7 | 141.3 | 2,286.3 |
| 2019 | 65.6 | 32.2 | 15.9 | 127.6 | 166.0 | 2,500.3 |
| 2020 | 168.3 | 127.4 | 216.1 | 239.9 | 310.1 | 3,046.1 |
| 2021 | -16.8 | -77.1 | -36.6 | 396.9 | 509.1 | 3,745.9 |
| 2022 | 184.1 | 148.0 | 127.6 | 490.7 | 635.2 | 4,131.4 |
| 2023 | 552.1 | 522.0 | 442.1 | 465.4 | 607.3 | 4,033.5 |
| 2024 | 179.7 | 110.2 | 230.5 | 563.7 | 733.6 | 4,504.7 |
| 2025 | 137.3 | 60.6 | 51.3 | 402.9 | 526.6 | 4,417.8 |
| **sum 2006-25** | 1,157.8 | **411.5** | **658.5** | **2,733.9** | 3,577.0 | 41,402.6 |

- Five-year average 2021-2025: owner cash $152.7M strict, $163.0M warehouse-adjusted, against average net income of
  $463.9M. Ten-year average 2016-2025: $70.2M strict, $85.5M adjusted.
- **Twenty years, the whole cycle: the business earned $2,733.9M and put out $411.5M of owner cash (strict), 15% of what it
  earned; $658.5M (24%) warehouse-adjusted.** The rest went into land and houses: inventory rose from $1,092.7M (2006) to
  $3,383.9M (2025), and the owners also supplied new equity in the bust (below). Income 2006-2008 and 2012 from the
  selected data and income statements of the FY2008, FY2010 and FY2012 10-Ks; 2006 and 2007 are continuing operations
  as restated after the West Palm Beach exit.
- Stock pay is in every year's figure (operator rule 5). No net-income proxy is used anywhere.
- H1 2026 (10-Q): operating cash $172.5M, stock pay $8.7M, property $5.5M, joint ventures $10.3M, MSR sales $9.1M;
  pre-tax income $193.7M against $306.2M in H1 2025 (-37%); trailing-twelve-month revenue $4,263.1M.

### The balance sheets, ten years, before the income account (read here because the file closes before Q4)
From `tools/run.py`'s ten-year table (first-filed XBRL) and the filed statements behind it ($M):
- **Equity against goodwill and intangibles.** Equity $654 (2016) to $3,166 (2025) and $3,227 (2026-06-30). Goodwill
  $16.4 since the 2018 Detroit acquisition, nothing else intangible of size: the equity is tangible, and it is mostly land
  and houses at cost.
- **Retained earnings** $407 to $3,268: the rise ($2,861) equals the ten years' net income less the preferred dividends of
  2016-2017; no common dividend since 2008. Treasury shares at cost reached -$446 (2025) and -$524 (2026-06-30) from
  buybacks of $51.5 (2021), $55.3 (2022), $65.3 (2023), $177.0 (2024), $202.0 (2025), $100.1 (H1 2026).
- **Inventory against sales.** Inventory $1,216 to $3,384 (x2.8) against revenue $1,691 to $4,418 (x2.6); inventory per home
  delivered $280.1K (2006) and $379.3K (2025). Of the $3,383.9M: lots, land and development $1,881.2M, homes under
  construction $1,282.6M, models $91.5M, land deposits $74.5M (Note 3, FY2025). 25,652 lots owned and 24,329 under
  contract for about $1.6B through 2031, 49,981 controlled, "a 5.6-year supply" against the filer's stated goal of "an
  approximate three to five-year supply" (Item 1). 68% of 2025 closings were inventory (speculative) homes, 60% in 2024.
- **Receivables:** none of size; homes close for cash through title and escrow. Mortgage loans held for sale $309.1M (2025)
  carried against $276.9M of repurchase-facility borrowings in the mortgage subsidiary.
- **Cash** $34 (2016) to a peak of $822 (2024), $689 (2025), $736 (2026-06-30).
- **Debt.** 2025: senior notes due 2028 (4.95%, $400M face) and due 2030 (3.95%, $300M face), carried at $696.3M; $900M
  revolving facility maturing 2030-09-18 with nothing drawn and $93.2M of letters of credit; filer's debt to capital 18%.
  Homebuilding cash exceeds the senior notes at 2026-06-30 ($735.9M against $696.9M carried). The run.py debt sum is
  partial before 2022 (the earlier notes were tagged differently); the FY2015 selected data shows senior notes $294.7M,
  convertible notes $141.2M and bank borrowings $43.8M against equity of $596.6M.
- **Off the balance sheet:** $590.1M of completion bonds and standby letters of credit (Note 8, FY2025); the land option
  purchase obligations above; loans sold with a limited-life repurchase guarantee, $722.1M covered at 2026-06-30 (10-Q).
- **Interest:** $36.0M incurred in 2025 and capitalized into inventory; it reaches the income account through cost of sales,
  which is why the income statement shows net interest income.
- **What the figures do not say:** land is carried at cost, and its value moves with house prices. The 2006-2010 inventory
  and joint-venture impairments reduced gross margin by $67.2M, $148.4M, $153.3M, $55.4M and $12.5M (FY2010 selected data,
  note (b)), $436.8M against 2006 equity of $617.1M. Impairments returned in 2025 ($35.9M plus $11.8M of deposits written
  off) and in Q2 2026 ($4.2M).

## THE FOUNDATIONS (not a gate)
"Because then you’re buying a business" **[M1997-109]**: the question is what a house builder in Columbus, Florida, the
Carolinas and Texas earns across the years in which houses are built and the years in which they are not, never when the
quote moves. "macro conclusions are [...] just never enter into the discussion" **[M2000-094]**: the temptation here is to
forecast mortgage rates and the next housing turn; the rows ask instead
for "the average profitability of the business over time and how strong its competitive mode is" **[M2015-016]**, which
is why the owner cash above is read over twenty years and not five. The speakers' own picture of this industry is in the
rows: "if you take the next 20 years, there will be, you know, three or four terrible years for residential housing, and
there will be a lot of them that are pretty good, and there will be a few that are terrific" **[M2011-101]**, and they
did not mind "if it comes in in a very lumpy fashion" "as long as it’s a good business" **[M2011-102]**. Who is paid to tell
you: the filer's case for the future is "favorable demographic trends" and "a decade of underbuilding" (Item 1, FY2025),
a seller's projection, and the speakers say "we’ve never looked at a projection in connection with either a security we’ve
bought or a business we’ve bought" **[M1995-050]**. Margin of safety: "if you have to actually do it on [...] with pencil
and paper, it’s too close to think about" **[M1996-084]**.

**Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**; evidence against the conclusion the analyst was forming at the
time it was found, in both directions):
- Against the business, found first: twenty years of owner cash total $411.5M against $2,733.9M of earnings; equity lost
  80% of its 2006 level in 2007-2011; shares were issued below book in 2009; deliveries fell 53% from 2005 to 2008.
- For the business, found while forming an OUT at Q2: the Northern region held its homebuilding gross margin at 22.0% in
  2025 (22.1% in 2024) while the Southern region fell from 26.6% to 19.8% (MD&A, FY2025); new contracts in Q2 2026 were a
  record 2,387, up 15%, with absorption 3.4 a month per community against 3.0 (10-Q); the company never failed or
  restructured its debt in 2007-2011, and has been profitable every year since 2012; it carries no net homebuilding
  debt; its homebuilding gross margin in 2025 (20.8%) is close to NVR's (21.2%); the price is about one times book
  ($127.88 a share at 2026-06-30). These are written into Q2 as the strongest case for it.

## THE STANDING RULE
Owning a marketable stake in MHO bought with the buyer's own money, unlevered, puts the buyer at no risk of ruin; the rule
binds the buyer's financing and sizing, and borrowed money "has no place in the investor's tool kit" **[L2014-005]**. Nothing
in the business forces the buyer to sell. One line: no conflict, provided no margin is used; "We are never going to risk
what we have and need for what we don’t have and don’t need." **[M2012-081]**

---
## Q1 - CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The product and the economics.** M/I builds and sells single-family homes and townhomes in 17 markets in ten states,
  with a captive mortgage and title arm that financed 93% of 2025 closings and earned 3% of revenue (Item 1, FY2025). It buys
  raw land, develops "over 80% of our lots internally", builds through subcontractors in four to six months, and sells at a
  2025 average of $479,000. Understanding here is "the economic dynamics of the industry. Is there [...] are there
  competitive moats? Is there ease of entry?" **[M2011-014]**, not the carpentry.
- **The key variables**, "evaluating how predictable they were first" **[M1998-044]**: (1) homes delivered, (2) the price per home
  against the cost of the lot and the build, (3) the land inventory carried at cost and what it is worth when prices fall,
  (4) the share of the market against larger rivals. None is technological. The first two swing hard with the cycle and are
  not foreseeable year by year (deliveries 4,291 in 2005, 2,025 in 2008, 8,921 in 2025); their range across a cycle is on
  the record for twenty years of the filer's own statements, so that "the financial statements will tell me the information
  that’s useful to me in making a judgment about what the future financial statements are going to look like"
  **[M2008-033]**, read as a range across a cycle. As to "how far off we can be" **[M2011-084]**: far off in any year,
  bracketed over a cycle.
- **Ten years out** ("where the business will be in 10 years" **[M2000-037]**; "how the industry will develop and where the
  company will stand within the industry" **[M2012-065]**): in ten years this is still a regional builder of detached houses
  selling on location and price, with a mortgage arm, competing with larger public builders and resales. Where it will stand
  within the industry is the castle question, and the evidence on it is concrete enough to judge at Q2; this is not the
  case of insiders who "would not want to put down on paper their predictions" **[M2000-105]**.
- **Routing:** not a fast-changing industry; not a bank (the mortgage arm originates and sells within days, holds $259.0M of
  loans against $252.4M of matched warehouse funding at 2026-06-30, and is a part that is readable from the filing); not a
  holding company.
- **The doubt rule**, "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**:
  the doubt the analyst holds is about the castle, not about understanding the
  economics; the speakers themselves describe the economics of residential housing in exactly these cyclical terms
  **[M2011-101]**.
- **VERDICT: IN.** The economics are simple, cyclical and on the record; the question that matters is among "things that
  are important and knowable" **[M2006-076]** and goes to Q2. "the first question is, can I understand it?" **[M1995-051]**:
  yes.

## Q2 - WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now. What are the key factors? And how permanent are they?" **[M1995-038]**

**The castle tests, each with its filing fact:**
1. **The key factors and their permanence.** The filer names its own: "a top ten builder in the majority of
   our markets", design and quality, the 10-year structural warranty, customer service, "offering mortgage and title
   services" (Item 1, FY2025). It names the field in the same section: "The homebuilding industry is fragmented and highly
   competitive. [...] Our competition ranges from small local builders to larger regional builders to publicly-owned
   builders and developers, some of which have greater financial, marketing, land acquisition, and sales resources than
   us. Previously owned homes and the availability of rental housing provide additional competition. We compete primarily
   on the basis of price, location, design, quality, service, and reputation." Price is first in its own list. None of the
   factors is held by M/I alone.
2. **Would it stand without the lord?** The land position is bought again each cycle, community by community (232
   communities at end-2025; 49 opened and 47 closed in H1 2026), on the judgment of a corporate land committee. "A moat that
   must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**
3. **The money test.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?"
   **[M2011-015]** Here: could a rival with money take M/I on? The rivals already do, in its markets. Century
   Communities, a public builder of M/I's size (revenue $4,118M in 2025 against M/I's $4,418M), states in its own 10-K that
   homebuilding "is characterized by relatively low barriers to entry" and again "highly competitive, with relatively low
   barriers to entry" (CCS 10-K FY2025, `0001576940-26-000005`). D.R. Horton calls itself "the largest homebuilding company
   in the United States [...] and we are also one of the largest builders in most of the markets in which we operate" (DHI
   10-K FY2025, `0000882184-25-000081`); its reporting regions list Ohio, Indiana, Illinois, Minnesota, Tennessee, Texas,
   Florida and North Carolina, every state named in M/I's market table except Michigan. "If the answer had been yes, we
   wouldn’t have done it." **[M2011-015]**; "there are some industries that are just never going to have barriers to entry"
   **[M2012-106]**.
4. **Pricing power.** The record is the opposite of a price rise: revenue
   and average price were reduced by $200.0M of "incentives and closing costs" in 2025 against $131.3M in 2024, including
   "a $53.3 million increase in mortgage interest rate buydowns" (MD&A, FY2025); $63.2M in Q2 2026 against $47.1M (10-Q).
   The Southern region's average price fell 8% in Q2 2026, from $463,000 to $426,000. In 2008 the average price fell from
   $296,000 to $274,000 and the gross margin was -12.8% of revenue (FY2008 and FY2010 10-Ks). The filer's own risk factor:
   "our pricing strategies may be limited by market conditions" (FY2025). "You can learn a lot about [...] the durability of
   the economics of a business by observing the behavior of [...] the price behavior." **[M2005-020]**
5. **Unit volume.** Homes delivered: 4,148 (2003), 4,303 (2004), 4,291 (2005), 3,901 (2006), 3,173 (2007),
   2,025 (2008), 2,409 (2009), 2,434 (2010), 2,278 (2011), 2,765 (2012), 3,472 (2013) ... 4,482 (2016), 7,709 (2020), 8,638
   (2021), 8,921 (2025) (the MD&A delivery tables of the 10-Ks named in Step 0). Volume fell 53% in three years and took
   eleven years to regain its 2005 level: volume follows the cycle. "It’s share of mind. It’s not share of market."
   **[M1997-099]**; no filing fact shows a share of mind that held the volume up.
6. **The low-cost position.** "Being the low-cost producer, for example, is a terribly important moat." **[M2018-043]**;
   "when a company is selling a product with commodity-like economic characteristics, being the low-cost producer is
   all-important" **[L2000-017]**. M/I is not the low-cost operator. Selling, general and
   administrative expense was 11.6% of revenue in 2025 ($510.6M on $4,417.8M); D.R. Horton's homebuilding SG&A was 8.3% of
   homebuilding revenue (DHI 10-K FY2025). Meritage, a peer of M/I's size, writes that "some of our homebuilder competitors
   have greater financial resources and may have lower costs than we do" (MTH 10-K FY2025, `0000833079-26-000010`). NVR earns
   a similar gross margin (21.2% in 2025, NVR 10-K FY2025, `0000906163-26-000018`) without owning the land: "We generally do
   not engage in land development [...] we typically acquire finished building lots from various third-party land
   developers pursuant to fixed price lot purchase agreements". "commodity businesses have risk unless you’re the low-cost
   producer, because the low-cost producer can put you out of business." **[M1997-010]**; "your costs are on parity or less
   [...] than your other major competitors, that is much more important to you than the absolute level" **[M2001-013]**.
7. **The brand.** "the brand has to stand for something in the consumer’s mind" **[M2015-038]**. The homes are sold "under the M/I Homes brand", and the 2026
   messaging is the 50th year (Item 1). The buyer chooses a community, a location and a monthly payment; the filer's own
   description of 2025 is that buyers moved to "inventory homes that offered quick move-ins and more selective incentives".
   No filing fact shows a buyer paying more for the name.
8. **The low bid.** Of See's: "it wouldn’t be a question of people buying candy for the low bid" **[M2017-009]**. Here the
   opposite is on the record. The Southern backlog fell 30% in 2025 "primarily
   due to a decline in homebuyer demand and increased popularity of inventory homes" which "offer incentives" (MD&A FY2025,
   10-Q Q2 2026). The customer moved to the discounted house. This is the commodity mark: "most insureds don't care from
   whom they buy" **[L2004-003]**.
9. **Ask the competitors** ("which one would it be and why?" **[M1999-130]**), here from their own filings: NVR, "The housing industry is highly competitive. We
   compete with numerous homebuilders of varying size [...] some of which have greater financial resources than we do";
   Lennar, "The residential homebuilding industry is highly competitive" (LEN 10-K FY2025, `0001628280-26-003870`); D.R.
   Horton, "We compete based on price, location, quality and design of our homes and on mortgage financing terms"; Meritage
   and Century as quoted in tests 3 and 6. Five rivals, the same description, and two of them name lower costs or low
   barriers.
10. **Widening or narrowing** ("whether it’s likely to widen further or shrink on you" **[M1999-108]**). Homebuilding gross margin 24.7% (2024), 20.8% (2025), 19.7% in
    Q2 2026 against 22.6%; pre-tax income H1 2026 down 37%; impairments back. Across the cycle the margin is set by the
    industry: total gross margin 22.2% (2001) to 25.5% (2004), 19.4% (2006), 3.5% (2007), -12.8% (2008), 3.4% (2009), 15.0%
    (2010), about 20% (2013-2019), 25.7% (2022), 26.6% (2024), 23.0% (2025) (selected data and income statements).
11. **What could destroy it** ("destroy, or modify, or reduce the economic strengths" **[M2000-014]**): the industry's own bust, which the record measures. 2007-2011
    net losses totalled $495.8M against 2006 equity of $617.1M (80%); inventory impairments $436.8M in 2006-2010; the credit
    facility's covenant on "minimum tangible net worth" became "the most restrictive covenant", and the filer wrote "we are
    currently restricted from paying dividends on our common shares and our 9.75% Series A Preferred Shares" (FY2008 10-K); it then sold 4,475,600 common shares for $52.6M in 2009 (about
    $11.75 a share, against book of about $17.6 a share at end-2009) and more at $17.63 in 2012 (FY2010 and FY2012 10-Ks).
    Shares outstanding went from about 14.0M (2008) to 30.1M issued. "one competitor is frequently enough to ruin a
    business." **[M2012-108]**

**The competitor row** (same metrics from each company's own filings; 2006-2010 from each FY2010 10-K's selected data,
2011-2025 from XBRL company facts; accessions: NVR FY2010 `0000950123-11-018386`, DHI FY2010 `0000950123-10-106707`, LEN
FY2010 `0001193125-11-018957`, MTH FY2010 `0000950123-11-019601`, and the FY2025 10-Ks above):

| metric | MHO | NVR | DHI | LEN | MTH | CCS |
|---|---|---|---|---|---|---|
| net income 2007-2011, $M | -495.8 | +962.1 (a profit every year) | -3,578.8 | -3,280.0 | -661.1 | listed 2014 |
| as share of 2006 equity | -80% | positive | -55% | -58% | -66% | n/a |
| gross margin 2006 / 2008 | 19.4% / -12.8% | 22.1% / 12.6% (homebuilding) | 22.6% / -27.0% (homebuilding) | n/a | 20.6% / -2.4% | n/a |
| mean pre-tax margin 2012-2025 | 8.9% | 14.5% | 13.5% | 12.6% | not obtained | 8.8% (2013-25) |
| mean return on beginning equity 2008-2025 | 10.2% | 30.8% (buybacks shrink its equity) | 13.9% | 11.0% | 10.8% | n/a |
| pre-tax margin 2025 | 11.9% | 17.1% | 13.8% | 8.2% | not obtained | 4.7% |
| land and house inventory (with deposits) / revenue, latest | 0.77 | 0.25 | 0.74 | not obtained | not obtained | not obtained |
| SG&A / revenue, latest | 11.6% | not obtained | 8.3% (homebuilding) | not obtained | not obtained | not obtained |

Read over the whole span, not one year: M/I earned the industry's average return, below the two leaders, and lost more of
its equity in the bust than any of the peers that existed then. The low-cost and low-capital positions are held by others,
D.R. Horton by scale and NVR by its lot-option model. A high return in 2021-2024 (return on beginning equity 31.5%, 30.2%,
22.5%, 22.4%) is "a cyclical peak in earnings" **[L1994-009]**, not a castle.

**The strongest case for the castle**, stated as well as the analyst can, "looking at what you’re missing" **[M2025-013]**:
fifty years in Columbus and a
top-ten position in most markets; the Northern region's margin held flat in 2025 while the South's collapsed; record Q2
2026 sales; no net homebuilding debt and no failure in the worst bust in its history; a gross margin near NVR's. Against
it: the Northern margin is one year; the record sales were bought with larger buydowns ($63.2M against $47.1M); surviving
the bust cost 80% of the 2006 equity and an issue of shares below book; the gross margin near NVR's is earned on three times
the capital per dollar of sales. "Average is going be terrible in insurance over time. [...] average is not going to go
away, either." **[M2000-072]**, said of a commodity, applies here: M/I is an average operator in a field whose average
includes the bust.

**The commodity reading and its exception.** The customer who moves to the discounted house is the insurer's customer: "most
insureds don't care from whom they buy" **[L2004-003]**. The incentives follow the market and the resale stock, as the gas
station's price followed the rival's: "whatever he charged for gas was my price" **[M2012-109]**. Design studios, quick
move-in programmes and rate buydowns are offered by every builder quoted above, "everybody in the crowd is up on tiptoes
and they’re not seeing any better" **[M2004-054]**. The rows' way through a commodity field: "Another way to prosper in a
commodity-type business is to be the low-cost operator." **[L2004-007]**; on the filings above M/I is not that operator.

- **VERDICT: OUT.** The castle is shown open on the evidence: the filer's own description of its competition, five rivals'
  identical descriptions (two naming low barriers or lower costs), pricing set by incentives and the resale market, a
  cost position behind the leaders, and a twenty-year record in which volume and margin follow the industry. "If the answer
  had been yes, we wouldn’t have done it." **[M2011-015]**. This is not TOO HARD: the castle's future is not unknowable, it
  is absent on the record; of the three boxes, "in, out, and too hard" **[M2006-013]**, this is the second. Price does not
  reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

---
## Q3 - HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed at Q2).
## Q4 - DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. (The ten-year balance-sheet reading is in Step 0.)
## Q5 - WHO RUNS IT. NOT REACHED.
## Q6 - WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 - WHAT IS IT WORTH. NOT REACHED (the owner's requested figures are below, as COMPUTATION - NOT A CLEARANCE).
## Q8 - BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 - COULD IT RUIN US. NOT REACHED.
## Q10 - THE FAT PITCH. NOT REACHED.
## Q12 (optional) - PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

Facts gathered on the way that would bear on the unreached questions, recorded and not judged: the chief executive, Robert
H. Schottenstein, has been CEO since 2004 and chairman since 2004, with 600,182 shares beneficially owned (DEF 14A); the
annual bonus pays on "Adjusted Pre-Tax Income" with a threshold of $75 million against a target of $625 million, and paid
94% of target for 2025 on $563 million achieved; the long-term units vest 80% on cumulative adjusted pre-tax income and 20%
on relative shareholder return, with no charge for the capital employed; no share-ownership requirement; the buyback
programme ($250M authorised November 2025, $120.3M left at 2026-06-30) names no price.

---
## THE BOX
**OUT, at Q2.** The castle is shown open on the filer's and five competitors' own filings and on a twenty-year record. No
research pass (the box is OUT, not TOO HARD). The figures below were requested by the owner and are reported as
computation only.

### COMPUTATION - NOT A CLEARANCE
Every figure in this section is arithmetic made after a closing STOP. It carries no entry language and clears nothing
(operator rule 3).

**(a) The VALUE RANGE per the Q7 convention** (Part VI of the framework; five-year average of owner cash after every real
cost, carried ten years at the growth shown, then no growth, discounted at the 5.66% sovereign; the ends are the no-growth
and shown-growth cases; 25.283M shares):
- Owner cash, five-year average 2021-2025: $152.7M strict, $163.0M warehouse-adjusted.
- The growth shown cannot be measured on aggregate owner cash, because the first year of the window is negative (-$77.1M in
  2021). CONVENTION of this run: the shown-growth end uses revenue growth over the window, 2021 to 2025, 4.21% a year
  (below the discount rate, so the Q3 cap does not bind). Earnings did not grow over the same window (net income $396.9M
  to $402.9M).
- **No-growth end $106.7 (strict) to $113.9 (adjusted); shown-growth end $149.0 to $159.0. Range about $107 to $159 a share
  against $132.00.** Width about 1.5 to 1. Had Q7 been reached, the price sits inside the range: the convention's close is
  OUT (not a screamer).

**(b) The whole-cycle variant** (the window 2021-2025 holds the boom; owner cash and margins over 2006-2025, a full cycle
from the 2006 top through the bust to the 2024 top, scaled to trailing revenue of $4,263.1M; zero nominal growth, at
5.66%). Three readings, because the twenty-year record separates what the business earned from what it let its owners take
out:
- B1, the owner cash it actually delivered: 0.99% of revenue strict, 1.59% warehouse-adjusted, so $42.4M to $67.8M a year:
  **$29.6 to $47.4 a share.**
- B2, earnings less the inventory needed to stand still (CONVENTION of this run: the rows name the split between spending to
  "maintain its competitive position" and "optional outlays, aimed at business growth" **[L1999-024]** but give no method;
  the method here: inventory per delivered home rose from $280.1K to $379.3K, so $885M of the $2,291M inventory increase
  kept the 2025 volume in place and $1,406M added volume; earnings $2,733.9M less $885M is 4.47% of revenue): $190.4M a
  year, **$133.0 a share.**
- B3, every dollar of whole-cycle earnings distributable (6.60% net margin): $281.5M a year, **$196.7 a share.**
- **Whole-cycle range about $30 to $197 a share, 6.6 to 1.** Wider than three to one: by the Q7 convention, "the range must
  be so wide that no useful conclusion can be reached" **[L2000-025]**. The central reading B2 sits at the price.

**(c) FAIR PRICE: the price at or below which the central case clears about 10% pre-tax** (the floor CONVENTION, Q7).
- Central case: B2, the whole-cycle earnings less stand-still inventory, $190.4M after tax.
- Tax treatment: grossed up at the 2025 effective rate, 23.5% ($123.6M on $526.6M), to $248.9M pre-tax.
- The floor is applied to equity (market value of the common), not to equity plus net debt, because homebuilding net debt
  is about nil: cash $735.9M against senior notes carried at $696.9M at 2026-06-30, and the mortgage warehouse ($252.4M) is
  matched by loans held for sale ($259.0M).
- **Fair price about $98 a share** ($248.9M / 10% / 25.283M). At $132.00 the central case returns about 7.5% pre-tax.
- For comparison, on the five-year window (owner cash plus the window's average cash taxes of $141.3M, $294.0M to $304.3M
  pre-tax): fair about $116 to $120; at $132.00, 8.8% to 9.1%.

**(d) CHEAP PRICE: below which no pencil is needed.** Rule (CONVENTION of this run): half the fair price, a 50% discount from
the central case, so that the central case yields about 20% pre-tax and the worst reading of the record, the owner cash
actually delivered over twenty years (B1 warehouse-adjusted, $47.4 a share at the government rate), is itself covered.
**Cheap price about $47 to $49 a share**, about 0.37 times the June 2026 book of $127.88. The rule is ours; it is the
"big discount from that present value" **[M1997-126]** made into a number, and its rationale is that a case below it would
not need the arithmetic above to see.

Summary against the price of $132.00: convention range $107 to $159 (price inside); whole-cycle range $30 to $197 (too
wide to conclude); fair about $98; cheap about $47 to $49.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question with a commit after each: **not done.**
      The file was filled in one pass after the research; the assignment forbade commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession; no
      number without a row, a filing or a CONVENTION label. Competitor figures marked "not obtained" were not filled from
      memory.
- [x] The order was kept; Q2 failed and closed the run; nothing after it is a clearance, and the requested figures are
      headed COMPUTATION - NOT A CLEARANCE.
- [x] Owner cash after every real cost, stock pay included, never a net-income proxy (operator rule 5); the sovereign from
      the issuing authority (US Treasury); the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, both ways, in the foundations and in Q2.
- [x] No row dated after the anchor: not a point-in-time run; n/a.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings figure was found incomplete for this business
      and replaced by the full table.
- [x] `python tools/check_framework.py` PASS (run before handing back; no commit made).
- Contamination declared at the top.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) The Q7 range convention measures shown growth "on the aggregate owner cash", and for a land-heavy builder the first
year of the five-year window is negative (-$77.1M in 2021), so no rate exists; the run substituted revenue growth and said
so. (2) For a business whose main capital is land and houses in operating cash flow, the convention's owner cash is set by
the land-spend choice of the window, and the framework gives no method to separate the inventory needed to stand still from
the inventory that adds volume, though L1999-024 names the distinction; the run used inventory per delivered home, a
CONVENTION, and the three whole-cycle readings differ by 6.6 to 1 on that one choice. (3) The floor is "about ten percent
pre-tax" while owner cash is after tax; whether to gross up at the effective rate or add back cash taxes paid is not said,
and the two methods give different fair prices here ($98 against $116 to $120, partly because they use different spans).
(4) A captive mortgage arm puts its loans in operating cash and their funding in financing; the framework has no rule, and
the run showed both a strict and an adjusted figure. (5) The template's POSITION NOTE tells the analyst to check
`PORTFOLIO.md`, which the blind rule of a run like this forbids; the note was left undetermined. (6) The template's write-early
self-audit line assumes commits, which this assignment forbade; the box is ticked "not done" rather than waived.
