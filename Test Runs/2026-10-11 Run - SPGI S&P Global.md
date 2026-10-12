# Company Run: S&P Global Inc. (NYSE: SPGI), 2026-10-11
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit 6570ac2c). Every judgment cites a v5
ledger id in bold; every filing fact carries its accession. Dispatched blind run (operator rule 10); research folder
`Test Runs/_research 2026-10-11 SPGI/` (raw filings in its `cache/`, gitignored; scripts and notes tracked).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-11, after the run was committed: not held (`PORTFOLIO.md` read for this one ticker; SPGI appears in no account, only in the opportunity set).*

**Contamination, declared.** (1) My first directory command listed `Test Runs/` filtered on the ticker and printed three
names: `2026-07-15 Run - SPGI (S&P Global).md`, `2026-09-18 Run - SPGI S&P Global.md` and `_research 2026-09-18 SPGI`.
Names only; none was opened, and nothing in them is known to me or used. A filtered listing of `Test Runs/` comes close to
the search the brief forbids; it is declared here as a breach of the blind rule's spirit. (2) The session context showed
recent commit subjects about another company (SHOP), not this one; not used. (3) The project memory index names counts of
"gate-clearers" and holdings reviews owed, with no company named; not used.

**The perimeter.** The S&P Global of the price date is Market Intelligence, Ratings, Energy (formerly Platts, then Commodity
Insights) and Indices. Mobility was spun off on 2026-07-01 (8-K of 2026-07-02, accession 0001104659-26-080005); Engineering
Solutions was sold on 2023-05-02; IHS Markit was merged in on 2022-02-28 for stock. Every figure below says which perimeter
it is on.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $407.82, close 2026-10-09 (the last close before the run date, a Sunday), from `tools/run.py`'s quote source,
  an aggregator, flagged per operator rule 5. The price is after the spin-off; `tools/run.py` printed a "split" factor of
  1.057 from the aggregator's history, which is the spin-off adjustment of past prices and not a split; it is ignored and
  the filed count is used.
- **Shares:** 294.8 million common shares outstanding as of 2026-07-24, from the cover of the 10-Q for the quarter ended
  2026-06-30 (filed 2026-07-28, accession 0000064040-26-000045), "excluding 7.2 million outstanding common shares held by
  the Markit Group Holdings Limited Employee Benefit Trust". `python Screens/cover_shares.py SPGI` returns 294,800,000 from
  the same filing. One class. Check: 415 million issued (balance sheet, 2026-06-30) less treasury and the trust shares; the
  10-Q states 3.5 million shares bought under the February and May 2026 accelerated repurchase agreements in the half
  year. No 8-K after the 10-Q reports a share count; a final delivery under the May 2026 agreement could lower the count
  slightly, not read, immaterial at this scale.
- **Market cap:** 294.8M x $407.82 = **$120.22B**.
- **Sovereign for the earnings currency (USD):** **5.60%**, the 30-year par yield of 2026-10-09 from the US Treasury daily
  par yield curve (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-11, accession 0000064040-26-000013): Item 1,
  Item 1A, Item 5, Item 7 segment review, the statements, Note 12 segment table, Note 13; the 10-Q for the quarter ended
  2026-06-30 (accession 0000064040-26-000045): balance sheet, cash flow, debt note, liquidity; the 8-K of 2026-07-02
  (spin-off completion, accession 0001104659-26-080005) and its amendment of 2026-07-06 with the unaudited pro forma
  statements without Mobility (8-K/A, accession 0001104659-26-080571, Exhibit 99.2); the proxy of 2026-03-31 (DEF 14A,
  accession 0001104659-26-037380); the 10-Ks for FY2024 (0000064040-25-000052), FY2023 (0000064040-24-000071), FY2022
  (0000064040-23-000058), FY2021 (0000064040-22-000055), FY2020 (0000064040-21-000063), FY2019 (0000064040-20-000055),
  FY2018 (0000064040-19-000059), FY2017 (0000064040-18-000061), FY2016 (0000064040-17-000015), FY2014
  (0000064040-15-000004) and FY2012 (0000064040-13-000005) for the segment and cash history; the FY2009 annual report
  (Exhibit 13 to the 10-K filed 2010-02-24, accession 0000950123-10-016328) for the 2007-2009 cycle.
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025 = $5,651M in
  the Consolidated Statements of Cash Flows of the FY2025 10-K; `tools/run.py` (tagged data) prints 5,651. Agrees.
- **`python tools/run.py SPGI`, arithmetic lines only** (consolidated, Mobility included; full output in
  `runpy_out.txt`): OCF 3,710 / 5,689 / 5,651 (2023-2025); SBC 171 / 247 / 236; capital spending 143 / 124 / 195 (the 10-Q
  says capital expenditures "include purchases of property and equipment and additions to technology projects", so
  capitalized software is inside it); depreciation and amortization 1,143 / 1,173 / 1,179; distributions to minority
  holders 280 / 287 / 321 (CME Group's share of S&P Dow Jones Indices). OCF - SBC - capex: 3,396 / 5,318 / 5,220. The
  tool's yield and growth lines are not used (Part VII). Owner cash on the price-date perimeter is built at Q4.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, and the answer turns entirely on whether the rating, index and price-benchmark franchises keep earning,
not on the quote. The foundation that bears hardest is the analyst's habits: I am to look for "what’s wrong in things"
**[M2025-013]**, and the rows hold a pointed irony for this name, since the speakers say of ratings "we don’t believe in
outsourcing investment decisions" **[M2009-011]**: the core product here is an opinion the speakers themselves do not use.
That says nothing about the economics of selling it, but it is written down as a caution against admiring the product.
No macro view enters; issuance cycles are read as cycles, not forecast. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the filer itself says "The rapid change of technology is a key feature of all of the markets in which
we operate" and that AI "is fundamentally changing the way data is gathered, produced, protected, licensed, processed, and
consumed" (10-K FY2025, Item 1A); (2) the company recorded "$1.6 billion of legal and regulatory settlements" in 2014 (FY2014 10-K, accession
0000064040-15-000004): $687.5M to the United States and $687.5M to the states under the Department of Justice settlement
of 2015-02-03 over pre-crisis structured-finance ratings, $125M to CalPERS, and $58M to the SEC, which found in January
2015 that S&P Ratings violated Section 17(a)(1) of the Securities Act over CMBS ratings of 2011 (FY2015 operating cash
fell to $195M); the business has a record of conduct that cost owners, and part of it is post-crisis; (3) the 2022 merger with IHS Markit
was paid entirely in stock; (4) the FY2025 10-K lists the risk that "free or relatively inexpensive information sources"
reduce demand. Each is carried to the question it bears on.

## THE STANDING RULE
A part-interest bought for cash, unlevered, sized by the buyer, puts no claim on the buyer beyond the price: the rows forbid
the buyer's borrowing, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and nothing in owning this
share can call cash from the holder. Clear, provided the purchase is unlevered **[M2012-081]**.

---
## THE LINES OF EVIDENCE (chosen from the 10-K, as the brief requires)
DEPARTURE FROM THE CANONICAL BRIEF, recorded by the brief itself: no hand-written list was supplied. From Item 1 (five
businesses, one now spun off), Item 1A (technology and AI, free information, issuance volumes and markets, regulation of
ratings and benchmarks, litigation, acquisitions and the separation) and Item 7 (segment review), I chose:
1. **Ratings**: revenue, operating profit and margin over every cycle on file (2007-2009 crisis, 2014 settlement year,
   2021 peak, 2022 trough, 2025), billed issuance, "improved contract terms", regulation, and Moody's MIS from Moody's
   own 10-Ks as the rival. Why: Ratings is the largest part by five-year operating profit and decides (Q2, parts).
2. **Indices, Market Intelligence and Energy**: margins and growth from the segment tables; MSCI and FactSet from their own
   filings as rivals. Why: the non-deciding parts, read for Q1's perimeter and for Q7.
3. **The perimeter**: the pro forma statements without Mobility (8-K/A Exhibit 99.2), the IHS Markit merger (2022), the
   Engineering Solutions sale (2023), the divestitures. Why: Q4 and Q7 must value the company as it now stands.
4. **The accounts**: ten balance sheets, amortization of acquired intangibles, stock pay, capitalized technology, merger
   and restructuring charges, the adjusted figure featured. Why: Q4.
5. **Capital allocation**: the all-stock merger, buybacks by accelerated agreement, dividends, the CME minority. Why: Q6.
6. **Integrity and pay**: the legal note, the 2015 settlement history, the proxy. Why: Q5 and Q6, Part B.
7. **Debt and exposures**: debt, maturities, the redeemable minority interest, litigation exposure of Ratings. Why: Q9.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The parts, and which one decides** (Q1's holding-company paragraph, extended to operating segments, and Q2's
business-of-parts CONVENTION: a part decides at more than half of five-year operating profit, else the largest).
Segment operating profit as reported, $M (FY2021 and FY2022 from the FY2022 10-K Note 12, accession 0000064040-23-000058;
FY2023-FY2025 from the FY2025 10-K Note 12; Mobility and Engineering Solutions excluded because they are gone):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share |
|---|---|---|---|---|---|---|---|
| Ratings | 2,629 | 1,672 | 1,864 | 2,707 | 3,013 | 11,885 | 45.2% |
| Market Intelligence | 676 | 2,488 (incl. a $1.8B gain on the divestitures the merger required) | 714 | 875 | 991 | 5,744 | 21.9% |
| Indices (27% owned by CME Group) | 798 | 927 | 925 | 1,103 | 1,271 | 5,024 | 19.1% |
| Energy (Platts, Commodity Insights) | 544 | 591 | 704 | 845 | 943 | 3,627 | 13.8% |
| sum | | | | | | 26,280 | |

Without the 2022 divestiture gain Ratings is 48.6% (11,885 of 24,480); counted on S&P Global's own share of Indices it is
higher still. No part carries more than half; **Ratings is the largest and decides**. The other three are read below and
carried, not decided on.

**The test, applied to Ratings.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in
that particular business, and evaluating how predictable they were first" **[M1998-044]**. The key variables, from the
filer's own MD&A (10-K FY2025, Ratings): (a) the volume of rated debt, which the filer tracks as billed issuance ($2,539B
in 2023, $3,911B in 2024, $4,327B in 2025); (b) price, which the filer reports in both 2024 and 2025 as "improved contract
terms across product categories"; (c) the share of the rated market held by a small number of agencies; (d) the
regulatory structure, where the filer is an SEC-registered NRSRO and registered with ESMA and the FCA. Of these, (a) is
cyclical in any year but its ten-year direction follows the stock of debt the world refinances; (b), (c) and (d) have
been stable for decades on the filings read: through the 2007-2009 collapse of structured finance the S&P financial
services segment's revenue fell from $3,046M (2007) to $2,610M (2009) and its operating profit from $1,370M to $1,014M,
the margin going from 45% to 40% to 39% (FY2009 annual report, accession 0000950123-10-016328); after the post-crisis
reforms (the filer names the Reform Act of 2006 and the Dodd-Frank Act among the laws it is regulated under) Ratings
revenue grew from $1,695M (2010, FY2012 10-K) to $4,724M (2025). Would insiders write down a ten-year forecast of a rating
agency's economics? The test is whether "they would not want to put down on paper their predictions" **[M2000-105]**; the
industry's two largest firms report the same few variables year after year in the same words, and the speakers, asked
about the field after the crisis, said "I think there will probably be rating agencies in the future" and "it has the
fundamentals of a pretty good business" **[M2009-010]**. The forecast is about customers who must have a rating to sell a
bond, which is the consumer kind of forecast, not the technology kind **[M2017-019]**.

**Contrary evidence, weighed here.** The filer says "The rapid change of technology is a key feature of all of the markets
in which we operate", and "all" includes Ratings. A business whose ten-year economics fast technology puts out of reach
closes here **[M1998-008]**, **[L1993-023]**. For Ratings the technology changes how the rating is produced, not why it is
bought: the buyer pays for an opinion that index rules, investment mandates and regulators in several jurisdictions name,
and AI does not supply that acceptance. The speakers' own qualification is the live risk: the business is very good "If
they are not forced to change their — the whole structure around them does not change in some dramatic way" **[M2010-062]**;
the filer lists proposals "seeking to reduce regulatory and investor reliance on credit ratings or to increase competition
among credit rating agencies" (Item 1A). That is an important variable and it is knowable from the record: the post-crisis reforms
were enacted and Ratings revenue nearly tripled after them (2010 $1,695M, 2025 $4,724M). A second risk, private credit lent outside the
rated bond market, is named by the filer as a source of growth for it ("private market opportunities, which contributed to
revenue growth in 2025"), which cuts the other way; carried to Q2. How far off could I be? On volume, a cycle's width
(2022 revenue fell 26% from 2021); on structure, little on the evidence of the filer's "over 150 years" and of the crisis
years read above. That is a model with a known error
band **[M2011-084]**.

**The parts that do not decide.** Indices (asset-linked fees on ETFs and funds, royalties on exchange-traded derivatives
on the S&P 500 and Dow Jones names) and Energy (Platts price assessments licensed to exchanges and sold by subscription)
are benchmark businesses whose key variables (assets tracking the benchmarks, contracts settled on the assessments) are
named in the filing. Market Intelligence (Capital IQ, data feeds, workflow software) is the part the technology risk
fits best: the filer calls its market "intensely competitive, ranging from established firms to fast evolving market
disruptors" (MD&A, Market Intelligence). Its ten-year economics I cannot claim to foresee with the confidence I have for
Ratings; it carries 22% of five-year operating profit with the 2022 gain and 16% without it. Under the convention it does
not decide; it is carried to Q2 and Q7 as the part whose future is least clear. Seeing an industry is not seeing the
company **[M2012-067]**; here the company in Ratings is one of the two that already hold the field.

**Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. My doubt
is real for Market Intelligence and is not for Ratings' economics; under the convention the deciding part governs.
Whether that is the right reading when the non-deciding parts together carry more than half of profit is written up in
WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR.

**VERDICT: IN** (on the deciding part, Ratings), with Market Intelligence's ten-year economics recorded as not foreseen
and carried. "can I understand it?" **[M1995-051]**: for the part that decides, yes, the key variables are known and
the forecast is one the industry writes down **[M1998-044]**, **[M2000-105]**.

---
## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.

The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. A moat "protects
excellent returns on invested capital" **[L2007-004]**.

**The parts table** (section B; the file closes on the deciding part):

| part | share of five-year segment operating profit (2021-2025, as reported) | castle | decides |
|---|---|---|---|
| Ratings | 45.2% (48.6% without the 2022 divestiture gain) | standing, widening on the margins (below) | **yes, the largest** |
| Market Intelligence | 21.9% (16.1% without the gain) | not judged: "intensely competitive", "fast evolving market disruptors" (10-K FY2025); margin 31% (2019, 607 / 1,959) to 20% (2025, 991 / 4,916) after $588M amortization of acquired intangibles, 32% before it | no |
| Indices | 19.1% | standing: S&P 500 and Dow Jones benchmarks; margin 69% in 2019 (630 / 918) and 69% in 2025 (1,271 / 1,850); ETF assets tracking its benchmarks $5.480 trillion at end-2025 | no |
| Energy | 13.8% | standing on the evidence read: Platts assessments licensed to exchanges, "increased trading volumes for Platts based contracts across all commodity sectors" (2025); margin 52% in 2019 (438 / 844) and 41% in 2025 after $130M amortization | no |

**The castle tests, on Ratings, each with its filing fact.**
1. *Key factors and how permanent.* The rating is bought because issuers cannot sell most bonds without it and
   investors, index rules and regulators read it; the filer describes itself as having "played a leading role for over
   150 years" and as an SEC-registered NRSRO and EU- and UK-registered agency (10-K FY2025, MD&A, Ratings). The factor is
   acceptance built over decades, which a rival cannot buy quickly; what is gained fast is lost fast **[M2002-050]**, and
   this was not gained fast.
2. *Without the lord.* "The really great business is one that doesn’t require good management" **[M1996-037]**. The
   test was run for us: the company recorded $1.6 billion of legal and regulatory settlements in 2014 (FY2014 10-K) after
   the worst failure in its history, and Ratings revenue rose from $2,455M (2014) to $4,724M (2025). Like the card whose
   users did not leave after a scandal, "nobody quit using the card" **[M2018-073]**, issuers did not stop buying. (The
   speakers' "Moody’s is a little like Harvard" **[M2000-084]** is a row about one company and is weighed only as their
   view of a rival at that date, under Q2's one-company CONVENTION.)
3. *The money test.* "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?"
   **[M2011-015]**. For ratings the attacker exists and is funded: Fitch (owned by Hearst, not an SEC filer, not named in
   the 10-K) and the state-backed local agencies the filer names as a risk: governments "provide financial or other
   support to locally-based competitors (particularly credit rating agencies)" (Item 1A). After the crisis, lawmakers
   considered "provisions seeking to reduce regulatory and investor reliance on credit ratings or to increase competition
   among credit rating agencies" (Item 1A). The two leaders still hold the field: Moody's MIS external revenue $4,119M
   and S&P Ratings $4,724M in 2025, each larger than in any earlier year on file. Given a very large sum and told to
   displace S&P Ratings, I would not know how to do it **[M1997-103]**.
4. *Pricing power and the agony before a rise.* "you can almost measure the strength of a business over time by the
   agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. The filer reports
   "improved contract terms across product categories" in both 2024 and 2025, and the Ratings margin rose from 44% (2015)
   to 64% (2025). Contrary: Moody's own 10-K (FY2025, accession 0001628280-26-009136) says "Competitive pricing pressures
   have intensified" and names "more aggressive tactics by some competitors in areas such as pricing". Weighed: the
   margins of both leaders rose over the decade while that sentence stood in the risk factors, which is what charging
   more and holding share looks like **[M2000-031]**.
5. *Unit volume and share of mind.* Billed issuance rose from $2,539B (2023) to $4,327B (2025); revenue in the 2022
   trough ($3,050M) was still above every year on file before 2020.
6. *The low-cost position.* Not the castle here; the castle is acceptance, not cost.
7. *The brand in the customer's mind.* The filer: "Our reputation, credibility, and the strength of our brand are key
   competitive strengths" (Item 1A).
8. *Would the customer choose it over the low bid?* The issuer pays, but the investor decides which agencies count; a
   cheaper unknown agency's rating does not sell the bond. The speakers: "you can’t shop pricing in the rating agency
   business" **[M2010-062]** (a row about the industry, weighed with the filings, not instead of them).
9. *Ask the competitors.* Moody's describes the same market and the same threats (pricing, Gen AI, non-NRSRO
   evaluators) and reports margins of the same order: the two firms read the castle alike.
10. *Widening or narrowing.* "whether it’s likely to widen further or shrink on you" **[M1999-108]**. Ratings margin,
    segment operating profit over segment revenue, from the 10-Ks: 2015 44% (1,078 / 2,428), 2016 50% (1,262 / 2,535),
    2017 51% (1,517 / 2,988), 2018 53% (1,530 / 2,883), 2019 57% (1,763 / 3,106), 2020 62% (2,223 / 3,606), 2021 64%
    (2,629 / 4,097), 2022 55% (1,672 / 3,050), 2023 56% (1,864 / 3,332), 2024 62% (2,707 / 4,370), 2025 64%
    (3,013 / 4,724). Widening, with the issuance cycle visible inside it **[L2005-010]**.
11. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: (a) a change in the structure,
    the issuer-pays model banned or ratings removed from rules and mandates, the risk the speakers themselves name
    **[M2010-062]**; (b) lending moving to private credit outside rated markets, which the filer so far reports as a
    source of revenue ("private market opportunities, which contributed to revenue growth in 2025"); (c) a loss of
    credibility, which the filer and Moody's both name, and of which 2008-2015 is the case where it happened and the
    business survived; (d) Gen AI tools that let investors form their own credit opinions, which Moody's names. None of
    these is shown on the evidence to be filling the moat; (a) and (c) are the ones that could.

**The competitor row, from the rivals' own filings** (the 10-K names its peer group in Item 5: Moody's, CME Group,
MSCI, FactSet, Verisk and ICE; three are taken; Fitch, Bloomberg, LSEG/FTSE Russell and Argus Media do not file with the
SEC, and the 10-K's competition text names no rival):

| rival (filing) | metric | years |
|---|---|---|
| Moody's MIS (10-Ks FY2019 0001059556-20-000005, FY2020 0001059556-21-000010, FY2022 0001059556-23-000016, FY2023 0001059556-24-000017, FY2025 0001628280-26-009136) | external revenue $M / margin as printed (2018-2019 segment operating margin; 2021-2025 "Adjusted Operating Margin", before D&A and restructuring, on revenue including the intersegment royalty) | 2018 2,712 / 55.0%; 2019 2,875 / 54.3%; 2020 3,292 / not printed; 2021 3,812 / 62.2%; 2022 2,699 / 51.8%; 2023 2,860 / 54.5%; 2024 3,793 / 60.1%; 2025 4,119 / 63.6% |
| S&P Ratings, for comparison (segment operating profit after its own small amortization; revenue includes its royalty from Market Intelligence) | revenue $M / margin | 2018 2,883 / 53%; 2019 3,106 / 57%; 2021 4,097 / 64%; 2022 3,050 / 55%; 2023 3,332 / 56%; 2024 4,370 / 62%; 2025 4,724 / 64% |
| MSCI (XBRL companyfacts of its 10-Ks; whole company, index-led), the Indices rival | operating income / revenue | 2016 42% (488 / 1,151); 2020 52% (885 / 1,695); 2025 55% (1,714 / 3,134) |
| FactSet (XBRL companyfacts of its 10-Ks; fiscal years to August), the Market Intelligence rival | operating income / revenue | FY2016 31% (350 / 1,127); FY2020 29% (440 / 1,494); FY2025 32% (748 / 2,322) |

**The field's returns over the last full cycle** (section C). The issuance cycle on file runs peak 2021, trough 2022,
recovery 2024-2025: the two rating leaders earned 52% to 64% margins on revenue through it, on almost no capital (Q3).
The cycle before it, 2007-2009, the deepest in structured finance on record: S&P's financial services segment kept a 39%
margin at the bottom (FY2009 annual report). These are excellent returns, not ordinary ones; the exclusion of the
standing castle with ordinary returns does not apply. Two competitors can still make "terrible businesses"
**[M2013-052]**; the filings show these two do not.

**Why not TOO HARD.** A castle whose future cannot be judged closes TOO HARD **[M2000-019]**. For Ratings the future
can be judged on the factors above, and the gravest threat named, a change of structure, was tried once in the filed
record (the post-crisis reforms) and the business grew through it. For Market Intelligence I do not judge the future;
it does not decide, and it is carried to Q7 at no growth (a CONVENTION of this run: Q2's text sends an open
non-deciding part to Q7 at no growth and says nothing of a non-deciding part whose future cannot be judged; the same
treatment is used, as the conservative one).

**VERDICT: IN** on the deciding part. The castle stands because the product is an accepted opinion the market requires
and that cannot be bought new **[M1995-038]**, **[M2011-015]**; it has widened on the margins **[M1999-108]**; the
threats are named and carried to Q9 and the box line.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.

"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**; the best business
"gives you more and more money every year without putting up anything to get it, or very little" **[M1998-081]**.

**The capital the business needs** **[M2010-090]**. Capital spending, which the filer says includes "additions to
technology projects", was $143M, $124M and $195M in 2023-2025 against revenue of $12.5B to $15.3B (about 1% to 1.3%), and
$35M to $123M a year on the smaller pre-merger company in 2016-2021 (XBRL of the 10-Ks, `runpy_out.txt`). Working
capital is negative: customers pay ahead, and unearned revenue was $3,886M against receivables of $3,276M on the
continuing perimeter at 2026-03-31 (8-K/A pro forma balance sheet). Property and equipment, net, was $242M. Tangible
capital employed is therefore about nil, and the return on it is not a meaningful finite number: the profit ends the
year as cash, the opposite of "your profit sitting in the yard" **[M2008-036]**, **[M2003-122]**. Goodwill is set aside
in judging the business and counted in judging the allocation, "because we paid for it" **[M2011-060]**.

**What the added capital earned.** Almost all the capital put in during the decade was the IHS Markit merger: $43,536M of
stock (113.8 million shares at $380.89) plus $5,159M of debt assumed (FY2022 10-K, Note 2, accession
0000064040-23-000058), for a business whose owner cash in its last full year (FY2021: operating cash $1,486.2M less
capital spending $294.3M and stock pay $226.9M = $965M; IHS Markit 10-K, accession 0001598014-22-000011) was about 2% of
what was paid, about 2.3% with its interest added back. On the whole company today, owner cash on an all-equity basis
($4,621M in 2025, Q4 and `numbers_out.md`) against capital employed including what was paid for goodwill (equity
$21,174M, debt $13,318M less cash $3,663M and the CME minority's $4,917M on the pro forma balance sheet of 2026-03-31,
total about $35.7B) is about 13%. So: the business needs almost no capital; the decade's added capital went into a merger
that earns a low return on its price. "whether that’s good or bad depends on what we earn on that incremental $130
million over time" **[M2001-019]**; here the incremental billions earn little, and earnings that rose because "We just
put way more capital into the business" **[M2023-081]** are not a better rate.

**Ruling out the flatterers**: the high return on tangible capital is not leverage (tangible capital is
about nil before any debt) and not a single peak year (it held through 2022); it rests partly on "a monopolistic
position" **[L1994-009]**, which here is the duopoly of Q2, the castle itself. Unprecedented returns are not assumed to last
**[M1998-016]**; Q7 carries no rate above what the filings show.

**Reinvestment to stand still and to grow.** The filing gives no split of capital spending into maintenance and growth;
at about 1% of revenue the split does not matter to the range. The growth the business has bought has come by
acquisition (IHS Markit, Visible Alpha, With Intelligence for $1.8B in 2025), not by capital spending.

**WEIGHS FOR** on the business (the best kind on the rows' scale, "very little" capital in **[M1998-081]**, **[L2009-012]**),
**AGAINST** on the use of added capital (the merger's low return on its price), carried to Q6. The "little or no debt"
**[R1997-001]** half of criterion (3) is applied at Q9.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.

**The balance sheets first, ten of them, before the income account** **[M2025-032]**. Year-ends 2016-2025 from the
first-filed XBRL of each 10-K (`tools/run.py`, transcription; accessions in `runpy_out.txt`), checked against the filed
balance sheets of FY2025 and FY2022, with the 10-Q of 2026-06-30 added. USD millions.

| year-end | total assets | equity (SPGI) | cash | receivables | goodwill | other intangibles | long-term debt | retained income | receivables / revenue |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 8,669 | 650 | 2,392 | 1,122 | 2,949 | 1,506 | 3,564 | 9,210 | 20% |
| 2017 | 9,425 | 711 | 2,779 | 1,319 | 2,989 | 1,388 | 3,170 | 10,025 | 22% |
| 2018 | 9,458 | 628 | 1,917 | 1,449 | 3,535 | 1,524 | 3,662 | 11,284 | 23% |
| 2019 | 11,348 | 479 | 2,866 | 1,577 | 3,575 | 1,424 | 3,948 | 12,205 | 24% |
| 2020 | 12,537 | 509 | 4,108 | 1,593 | 3,735 | 1,352 | 4,110 | 13,367 | 21% |
| 2021 | 15,026 | 2,032 | 6,497 | 1,650 | 3,506 | 1,285 | 4,114 | 15,017 | 20% |
| 2022 | 61,784 | 36,388 | 1,286 | 2,494 | 34,545 | 18,306 | 10,730 | 17,784 | 22% |
| 2023 | 60,589 | 34,200 | 1,290 | 2,826 | 34,850 | 17,398 | 11,412 | 18,728 | 23% |
| 2024 | 60,221 | 33,159 | 1,666 | 2,867 | 34,917 | 16,556 | 11,394 | 20,977 | 20% |
| 2025 | 61,200 | 31,127 | 1,745 | 3,441 | 36,475 | 16,271 | 12,370 | 23,666 | 22% |
| 2026-06-30 (Mobility still in) | 62,906 | 31,501 | 4,134 | n/r | 36,348 | 15,695 | 12,598 (+2,572 short) | n/r | |

**What moved, and why.** (1) *Equity against goodwill and intangibles.* Before the merger, equity was $0.5B to $2.0B on a
business earning $2-3B a year: buybacks had taken it near zero, which is no sign of distress in a business that needs
no capital. In 2022 equity jumped to $36.4B, the stock issued for IHS Markit, and goodwill and intangibles to $52.9B;
tangible equity has been negative since (2025: $31.1B equity against $52.7B of goodwill and intangibles). The balance
sheet now carries the price of the merger, not the capital the business uses. Since 2022 equity has fallen every year
($36.4B to $31.1B) because buybacks and dividends exceeded earnings. (2) *Cash.* Cash was built to $6.5B in 2021 ahead
of the merger and spent in 2022 on $12.0B of buybacks, funded also by $3.5B of proceeds from the divestitures the merger
required (FY2022 10-K cash flow). (3) *Receivables against sales.* 20% to 24% of revenue in every year: no build-up
**[M1995-064]**. The 2025 rise in receivables ($600M in the cash flow) brought the ratio back to its 2022-2023 level
(acquisitions of With Intelligence and others in the year). (4) *Debt.* Long-term debt rose from $3.6B (2016) to $12.4B
(2025), most of it IHS Markit's notes assumed ($4.9B at fair value) and new notes in 2022; commercial paper of $715M
appeared in 2025 and $825M by mid-2026. (5) *Retained income* rose every year, $9.2B to $23.7B; the treasury stock beside
it (to $36.4B in 2025, $38.3B by mid-2026) is where it went. (6) *Unearned revenue* ($2.2B in 2021, $4.1B in 2025): the
customers' prepayments, a float that finances the working capital. What the figures cannot say: what the intangibles
bought will earn, and whether a $4.9B redeemable minority (CME's put on its 27% of S&P Dow Jones Indices, Note 9) will be
exercised. What management might like them to say: the adjusted figures below.

**The real costs** **[L2021-003]**.
- *Depreciation and amortization.* Depreciation is small ($96M continuing, 2025). Amortization of acquired intangibles
  was $1,069M in 2025 (Mobility included): databases and software $341M, customer relationships $542M, tradenames $111M,
  other $75M (Note on intangibles, FY2025 10-K). The rows separate them: "With software, for example, amortization
  charges are very real expenses. Charges against other intangibles such as the amortization of customer relationships,
  however, arise through purchase-accounting rules and are clearly not real expenses" **[L2012-003]**. Owner cash below
  charges actual capital spending (which includes capitalized technology) and not the amortization; the depreciation
  variant charging all depreciation and amortization of the continuing business is shown beside it as the conservative
  bound, and the truth sits between them by about the software share.
- *Stock pay*: $236M (2025), $247M (2024), deducted in full **[L2015-003]**.
- *Restructuring and severance* recur every year (2025 segment footnotes: severance of $56M, $17M, $19M, $15M and $4M by
  segment; 2024 and 2023 similar), and IHS Markit merger costs ran through 2022-2024. They are inside operating cash and
  are not added back **[L2016-007]**.
- *Legal and regulatory settlements* are a real cost of this business: $1.6 billion in 2014 (FY2014 10-K); $20M SEC
  penalty in 2024 (FY2024 10-K). The 2014 cost sits outside the window; it is carried to Q5 and Q9 as a cost that comes
  in lumps.
- *Taxes*: the effective rate was 21.2%, 21.5% and 22.6% in 2023-2025 on the pro forma continuing statements; cash taxes
  paid were $1,279M, $1,159M and $1,502M (consolidated). No carryforward shelter is relied on.
- *The minority*: CME Group's 27% of S&P Dow Jones Indices takes $280M to $321M a year in distributions; owner cash is
  counted after them.

**Owner cash on the price-date perimeter** (`numbers.py`, output in `numbers_out.md`). Operating cash less capital
spending, stock pay and distributions to the minority, from the filed cash flow statements; Mobility removed; IHS Markit
added before the merger. Two estimates are a CONVENTION of this run, with the rationale that the filer gives Mobility's
income but not its cash: Mobility's cash = its operating profit plus its depreciation and amortization less its pro forma
tax (8-K/A Exhibit 99.2; FY2022 10-K Note 12 for 2022, tax at 21%), less a share of capital spending in proportion to
its property and equipment (19 of 261 at 2026-03-31) and a share of stock pay in proportion to its revenue; and IHS
Markit's FY2021 owner cash is cut by Transportation's share of its segment adjusted EBITDA (645.0 of 1,946.5, 33.1%),
with two months of it added to 2022 (not filed). All-equity adds back interest paid after the year's tax rate.

| year | OCF - capex - SBC - minority | less Mobility (est.) | plus IHS Markit (est.) | equity basis | all-equity |
|---|---|---|---|---|---|
| 2021 | 3,214 | 0 | 645 | 3,859 | 4,126 |
| 2022 | 2,030 | 394 | 108 | 1,744 | 1,958 |
| 2023 | 3,116 | 534 | 0 | 2,582 | 2,873 |
| 2024 | 5,031 | 560 | 0 | 4,471 | 4,778 |
| 2025 | 4,899 | 580 | 0 | 4,319 | 4,621 |

Depreciation variant (equity basis, all continuing depreciation and amortization charged in place of capital spending):
2023 1,882; 2024 3,728; 2025 3,638. 2022 is aberrational on the filer's own description: the merger year, with IHS
Markit merger costs, taxes paid on $1.9B of divestiture gains (cash taxes $1,555M against $883M in 2021), and two months
of IHS Markit unfiled. 2023 also carries merger costs and severance ($90M in Market Intelligence alone).
Acquisitions net of dispositions: 2021 +83 (SPGI), 2022 -3,719 (the merger's required divestitures), 2023 -718
(Engineering Solutions sold), 2024 +137, 2025 +474; over 2023-2025 they net to -36 a year, so deducting them (Q7
convention (c)) changes nothing material; the 2022 inflow is treated as part of the merger, not as a year's capital
spending (said so at Q7).

**EBITDA in the filer's own mouth, guidance, and the adjusted figure.** The 2Q 2026 release (8-K of 2026-07-28, accession
0000064040-26-000040, Exhibit 99.1) leads with reported figures and sets "adjusted diluted EPS" ($4.83 against $4.08
reported) beside them, adjusting chiefly for "deal-related amortization"; it gives full-year guidance ("2026 guidance
calls for revenue growth of 5.9% to 7.9%"), including adjusted operating margin. Pay is set on "non-GAAP ICP Adjusted
EBITA Margin" and "non-GAAP ICP Adjusted EPS" (proxy, DEF 14A 2026, accession 0001104659-26-037380). The rows: "a
management that regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us
nervous" **[L2016-006]**; guidance is "the scourge of earnings "guidance"" **[L2019-006]**. The adjustment here removes
mostly customer-relationship amortization, which the rows themselves call not a real expense **[L2012-003]**, but it
also removes acquired software amortization, which they call real; and the GAAP figure is shown first. Recorded as a
WEIGHING against and carried to Q5 (the gaps case, section A).

**Confusion or suspicion?** None found. The statements reconcile; receivables, prepaid accounts and reserves move with
the business **[M1995-064]**; the segment footnotes list every charge by name; the pro forma statements were filed when
the spin-off closed. "if I don’t understand it, I figure it’s probably because the management doesn’t want me to
understand it" **[M2003-029]**: I understand it, with the perimeter work above. The accounts are a place to start
**[M1994-079]**, and the restated perimeter is the filer's own.

**VERDICT on the accounts: no STOP** (neither confusion nor suspicion). **WEIGHS AGAINST, mildly**, for guidance and the
featured adjusted figure, carried to Q5 **[M1994-018]**. The recast owner cash (all-equity $2,873M / $4,778M / $4,621M
in 2023-2025; literal five-year average $3,671M) feeds Q7.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.

**Who.** Martina Cheung, President and CEO since 2024-11-01; she "joined the Company in May 2010" as Vice President of
Operations for S&P Global Ratings and later ran Market Intelligence and then Ratings (proxy, DEF 14A of 2026-03-31,
accession 0001104659-26-037380). CFO Eric Aboaf since 2025-02-19, from outside. The board has an independent chair,
separate from the CEO. This is a marketable part-interest: the people are read, not met **[M1994-009]**.

**The integrity record, on the filings read.**
1. 2015, pre-crisis ratings: the settlement of 2015-02-03 with the Department of Justice and nineteen states and the
   District of Columbia, $687.5M to each side, plus $125M to CalPERS; "The settlement agreement contains no findings of
   violations of law" (FY2014 10-K, accession 0000064040-15-000004).
2. 2015, post-crisis conduct: S&P Ratings settled with the SEC over CMBS ratings of 2011, 2012 criteria publications
   and an RMBS surveillance assumption; "the SEC found that S&P Ratings violated Section 17(a)(1) of the Securities
   Act", censured it, took $58M, and imposed a one-year "time-out" from new conduit/fusion CMBS ratings; S&P "neither
   admitted nor denied" (same 10-K). This conduct came after the crisis, when scrutiny was highest.
3. 2024: a $20M SEC penalty "as part of an industry-wide investigation into off-channel communications" for
   recordkeeping violations, the order recognising "remedial acts and its cooperation" (FY2024 10-K, accession
   0000064040-25-000052).
4. Pending: an Australian class action over CDOs rated 2005-2007 (FY2025 10-K, Note 13). Nothing else is disclosed.

**How the rows read it.** "people leave track records" **[M1998-168]**; the track record here is an institution's, and
the incentive that produced items 1 and 2 is the one the rows name in another firm: "it’s very hard to control people
when their income depends on bringing in dubious people into the door" **[M2004-110]**. The issuer pays the agency that
rates it, and that will not change. Against it, the rows' own reading of the agencies' failure was mostly cognition:
"the incentive part of it, there may have been some small aspect that that played. I just think that, you know, it’s
very hard to think contrary to the crowd" **[M2010-063]**; and the Wells Fargo test is whether, once the bad incentive is
found, the company acts: "we have to do something about it" **[M2018-012]**. On the filed record, the decade since 2015
holds one industry-wide recordkeeping penalty and no finding of a fraud provision; the 2015 matters were paid and the
SEC time-out served. No finding in the filings read names the present CEO or CFO.

**The habits carried from Q4.** Annual guidance and an adjusted EPS shown beside the reported one; pay on adjusted
measures. Read with the record above: the adjusted figure is shown second, not instead; the adjustment is mostly an
amortization the rows themselves set aside **[L2012-003]**; I found no record in the filings read of targets made
quarter after quarter by reserves or one-offs, and the filer reports its charges (severance, legal costs, merger costs)
segment by segment. "Managers that always promise to "make the numbers" will at some point be tempted to make up the
numbers" **[L2002-041]**: the guidance habit is a standing temptation, recorded, not a tell in itself.

**Doubt.** "If you’ve got doubts, forget it." **[M2013-088]**. The question is whether I doubt the honesty of the people
who now run it. I do not, on the filed record: the findings are of 2005-2012 conduct under earlier leadership, settled
with large payments, and the ten years since show nothing of that kind. What I do doubt is that any management can make
the issuer-pays structure immune to the pressure that produced them; that is a doubt about the business's structure, not
about these people, and it is carried to Q9 (litigation and regulatory claims come in lumps: $1.6B in 2014) and to Q12.
A reader who holds that the institution's record is itself the managers' record would close the file here; I record
that this run did not, and why. Hunting the evidence against: the present CEO came up through Ratings from 2010, the
years of item 2; the filings read do not connect her to it, and I have no evidence that they should.

**Love of the business, and owners as partners.** Directors and executive officers as a group held 100,468 shares on
2026-03-02 (proxy), about $41M at the price, about 0.03% of the company; the CEO's 2025 pay was $12,831,062 in the Summary
Compensation Table (proxy, pay-versus-performance table). Insiders' stakes are small against their pay; recorded for Q6, Part B.

**Ability.** Read against the hand dealt **[M1994-008]**: Ratings' margin rose from 44% (2015) to 64% (2025); Indices held
69%; Energy and Market Intelligence improved after the merger's integration (Market Intelligence 16% to 20% margin,
2023-2025, after amortization); the Mobility spin-off and the pro forma statements were delivered as announced. Against
it, the capital allocation of the decade (Q3, Q6). Ability enters as a weight on value, not a gate.

**VERDICT on integrity: IN** (no doubt found about the present managers' honesty on the filed record; the institutional
record and the structural incentive are written down and carried, and the guidance habit weighs against). **Ability
WEIGHS FOR** on running the businesses, with capital allocation weighed at Q6.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING (with one narrower STOP).

"the biggest judgment you have to make is how well capital will be deployed in the future" **[M2001-111]**.

### Part A: the money

**Issuance and deals: the IHS Markit merger, tested against the one STOP in Part A.** "If shares of a prospective acquirer
are selling below their intrinsic value, it's impossible for that buyer to make a sensible deal in an all-stock deal. You
simply can't exchange an undervalued stock for a fully-valued one without hurting your shareholders." **[L2009-019]**.
The facts (FY2022 10-K, Note 2, accession 0000064040-23-000058): on 2022-02-28 S&P Global paid for IHS Markit wholly in
stock, 113.8 million shares at the 2022-02-25 close of $380.89, $43,536M of equity consideration, and assumed $5,159M of
IHS Markit debt (cash acquired $310M). Before the merger S&P Global had 241.1 million shares (FY2021 10-K cover, as of
2022-02-04); the IHS Markit holders received 32.1% of the combined company.

*Was S&P Global's stock below its intrinsic value when it paid?* The text gives no method for this test; this run applies
Q7's own construction at the deal date (a CONVENTION of this run, rationale: Q6's other test, the buyback test, is read
against the bottom of the Q7 range, so the range is the framework's own measure of "intrinsic value, conservatively-calculated" **[L1999-023]**). The rate is the long government bond **[L2000-021]**: the US Treasury 30-year par yield was 2.29% on
2022-02-25 and 1.58% on 2020-11-30, the signing (Treasury daily par yield curve files, issuing authority, in `cache/`).
S&P Global's own owner cash on an all-equity basis, 2017-2021 average, was $2,566M (10-K cash flow statements; method as
at Q4; `numbers_out.md`); net cash at 2021-12-31 was $2,383M. The no-growth case alone, the bottom of the range, comes to
**$474.73 a share at 2.29%** ($683.61 at the signing's 1.58%) against the **$380.89** at which the shares were given: the
stock was given at about 0.80 of the bottom of its own range. The business received was priced the other way: IHS
Markit's all-equity owner cash averaged $950M in FY2019-FY2021 (IHS Markit 10-K, accession 0001598014-22-000011), whose
no-growth value at 2.29% is $41.5B, against $48.4B of enterprise value paid, 1.17 times it. On the same evidence the
holders of S&P Global gave 32.1% of the combined company for a business that brought 23.1% (equity basis) to 25.5%
(all-equity) of the combined FY2021 owner cash: "The intrinsic value of the shares you give in an acquisition must not be
greater than the intrinsic value of the business you receive" **[L2014-012]**. The case for the deal rests on what the two
"will earn more combined than they would separately" **[L1997-031]**, and "At Berkshire, we never count on synergies when
we acquire companies." **[L2016-008]**.

*The post-mortem* **[L2014-013]**: all-equity owner cash per share was about $13.76 for the stand-alone company in 2021
(3,317 / 241.1) and about $15.15 on today's perimeter in 2025 (4,621 / 305.1 diluted), about 2.4% a year across the
merger and $23.6B of buybacks in 2022-2025 (12,004 + 3,301 + 3,301 + 5,001), with the Mobility shares distributed beside it. The merged company has
not shown that the stock given bought more than it cost.

*Sensitivity, written down because it cuts against the finding* **[M1997-127]**: the rows allow "in times of very — what
would seem like very low rates — we might use a little higher rate" **[M1996-024]**; at 3.00% the no-growth bottom is
$364.71, just under the price given, and the price then sits inside a range whose growth case is far higher, so the stock
was still in the lower part of its range. Only on a floor of about ten percent, which Q7 uses for buying and not for
value, does the 2022 price look full. The finding that value given exceeded value got, measured in owner cash, holds at
any rate.

**The STOP: triggered.** S&P Global paid for an acquisition wholly in stock while its stock sat below the bottom of its own
range on Q7's construction at the deal date's sovereign. "No further weighing of that deal is done", and "A company that
has made such a deal is not cleared by the rest of Part A" (Q6 text). The file closes here.

**The rest of Part A, recorded and not weighed** (operator rule 2): *buybacks* without a stated price: the 2026 release
says the company "now expects to repurchase more than $7 billion in shares in total in 2026" (8-K of 2026-07-28), a fixed
sum; prices paid under the accelerated agreements of 2023-2025 ran from $341.95 to $518.47 a share (FY2025 10-K, Note 9)
and $1.5B bought 3.5 million shares in the first half of 2026 (10-Q), about $429; the line against the bottom of the Q7
range is written below under AFTER THE STOP, since Q7 is computation only. *Retention*: 2023-2025 dividends ($3,451M)
and buybacks ($11,603M) exceeded consolidated owner cash; commercial paper and a $1.0B note issue in 2025 funded part of
it; little was retained, so the retention test **[R1995-009]** has little to bite on.

### Part B: the pay, the board and the owners (recorded, not weighed, after the STOP)
Pay is set on "non-GAAP ICP Adjusted Revenue", "non-GAAP ICP Adjusted EBITA Margin" and "non-GAAP ICP Adjusted EPS"
(proxy, accession 0001104659-26-037380): no charge for the capital employed, the amortization of the merger's
intangibles excluded, and an EPS target that a buyback at any price helps to reach; "a batting average that does not
include a cost of capital is a phony batting average" **[M1995-010]**. The CEO's 2025 Summary Compensation Table total
was $12,831,062. Directors and executive officers as a group held 100,468 shares (about 0.03%). The board chair is
independent of the CEO. The proxy runs to more than a hundred pages: "If you take 100 pages to explain how you’re paying
the people of the place, something is wrong." **[M2009-087]**.

**VERDICT: Part A's narrower STOP closes the file** (the all-stock merger by an acquirer whose stock sat below its own
range, **[L2009-019]**). Part A otherwise weighs against (value given over value got, **[L2014-012]**; fixed-sum buybacks
with no stated price, **[L2016-002]**); Part B recorded as found.

## Q7: WHAT IS IT WORTH? STOP.
**NOT REACHED** (the file closed at Q6). The reporting figures the owner asked for are computed below under AFTER THE STOP,
headed COMPUTATION, NOT A CLEARANCE.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are recorded below.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts found are recorded below.

---
## THE BOX
**OUT**, decided at **Q6** by its narrower STOP: S&P Global paid for IHS Markit wholly in stock (2022) while its own stock
sat below the bottom of its range on Q7's construction at the deal date's sovereign ($474.73 a share at 2.29% against the
$380.89 given) **[L2009-019]**; on owner cash the holders gave 32.1% of the combined company for 23% to 25% of its cash
**[L2014-012]**. Q1 IN and Q2 IN on the deciding part (Ratings), Q4 no STOP, Q5 integrity IN with the institutional record
carried. The box is named by a CONVENTION of this run (the Q6 STOP is "stated without naming the box", section I):
**OUT**, because the question was answered against the name on the evidence, which is section I's definition of OUT, and
the cause is not ignorance. Beneath the stop, computation only: value range **$216.63 to $565.06** a share (all-equity)
against **$407.82**; fair price **$187.97** (all-equity), $203.06 equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(The box is unchanged by anything below; operator rule 2.)* **[M1997-127]**

**Q7, COMPUTATION, NOT A CLEARANCE** (Q7's range convention in full, as the owner's reporting convention asks; arithmetic
in `numbers.py`, output in `numbers_out.md`).
- *Base.* Owner cash on the price-date perimeter, all-equity (before interest, after the company's own tax, after the
  minority's distributions): 2021 $4,126M, 2022 $1,958M, 2023 $2,873M, 2024 $4,778M, 2025 $4,621M (Q4 table). **Literal
  five-year window (2021-2025): $3,671M** average. **Central base: $4,090M**, the 2023-2025 average, a CONVENTION of this
  run with the rationale that the window's first two years belong to companies that no longer exist as such (2021 is
  S&P Global plus an estimated IHS Markit, with businesses since sold; 2022 is the merger year, "aberrational" on the
  filer's own description of merger costs, divestiture taxes and two unfiled months), while 2023-2025 are the years the
  filer itself restated to today's perimeter in the 8-K/A; convention (a) asks for the last full cycle where an end year
  is aberrational, and no full cycle exists on today's perimeter. The literal window is shown beside throughout. Equity
  basis: central $3,791M, literal $3,395M.
- *Growth shown* (aggregate, not per share): 2023 to 2025, 26.83% a year (a recovery from the 2022-2023 trough); carried
  ten years it would need owner cash at 128% of sales, above the highest share of sales found in the filings read
  (44.8%, S&P Global 2020), so by specific (f) it is cut to the sales growth of the same years, **11.08%** (pro forma
  revenue $11,013M to $13,589M, 8-K/A). Literal window: end years 2021 to 2025, 2.87% a year; halves, 15.60%, which would
  need 50.7% of sales and is cut to 11.08% likewise. Ten years at the rate carried, then zero nominal growth.
- *Specifics.* (a) above. (b) no decline. (c) acquisitions net of dispositions over 2023-2025 average a net inflow of
  $36M a year (dispositions exceeded purchases); counted at nil, which is conservative by under 1%, with the total growth
  credited; the 2022 inflow of $3.7B (the merger's required divestitures) is part of the merger, not a year's spending.
  (d) working capital is inside operating cash. (e) the filing gives no maintenance split; all capital spending charged
  (about 1% of revenue); the depreciation variant is beside. (f) applied as above. The Mobility spin-off is handled by the
  perimeter, its own notes ($2.0B) leaving net debt and its $1.974B cash distribution staying.
- *Net debt*, at 2026-06-30 with the spin-off of 2026-07-01 that the 10-Q itself states: debt $15,170M less the Mobility
  Global notes of $1,986M = $13,184M; cash $4,134M less Mobility's own operating cash (estimated at its $121M of
  2026-03-31) and the $12M of note proceeds beyond the distribution = $4,001M; **net debt $9,183M** (estimate as stated).
  Operating leases ($618M) are left out, said so. The CME minority's $4,917M redemption value is not added, because owner
  cash is counted after its distributions. Market value 294.8M x $407.82 = $120,225M; enterprise value $129,408M.
- **VALUE RANGE (central, all-equity): $216.63 to $565.06 a share** (no-growth to growth case; 2.61 to 1). Equity-only
  beside: $229.61 to $552.50. Literal window beside: $191.23 to $503.95 (growth cut to 11.08%), or $191.23 to $248.14 on
  the literal end-year growth of 2.87%. Depreciation variant: $173.75 to $461.88.
- *The floor, tested first:* expected return at $407.82 on the all-equity basis, no-growth 3.16%, growth case 7.28%;
  equity-only 3.15% and 7.26%. No case earns about ten percent at the price; a growth of about 17% a year for ten years
  would be needed (15% gives 9.21%, 18% gives 10.83%). Had Q7 been reached it would have closed **OUT** on the floor
  **[M2003-149]**, before the width test (2.61 to 1, under three). The price sits inside the range, not a screamer
  **[M2009-005]**.
- **FAIR PRICE (each end valued at ten percent, averaged; Part VII): $187.97 a share on the all-equity basis (central)**;
  equity-only $203.06. Literal window: $165.52 all-equity, $181.86 equity-only. After the company's own tax; "pre-tax"
  read as before the holder's tax. No other price figure is reported.

**Q6, the buyback line against the bottom of the Q7 range.** Prices paid under the accelerated agreements of 2023-2025,
$341.95 to $518.47 (pre-spin shares), and about $429 in the first half of 2026, against a central bottom of $216.63 on
today's perimeter; adding a rough no-growth value for the Mobility shares then still attached (2023-2025 Mobility owner
cash about $558M a year, at 5.60%, about $33 a share) puts the pre-spin bottom near $249. Every price paid sits above it.
No price limit is stated. Under Q6's buyback CONVENTION this weighs against **[L2016-002]**.

**Q8.** The sovereign is 5.60%; the expected return at the price is 3.16% to 7.28% on the computation above.

**Q9.** Debt $13.2B after the spin (commercial paper $825M at 2026-06-30; senior notes otherwise); the credit facility's
only covenant is indebtedness to cash flow of no more than 4 to 1, "never exceeded" (10-Q). Pro forma 2025 pre-tax income
$5,888M against net interest of $288M. **A demand for a large sum at another's option**: CME Group "has the right at any
time to sell, and we are obligated to buy, at least 20% of their share in S&P Dow Jones Indices LLC", carried at $4.9B
(FY2025 10-K, critical accounting estimates and Note 9), against cash of about $4.0B and a $2.0B commercial-paper
facility. Litigation and regulatory claims arrive in lumps: $1.6B in 2014; an Australian class action over 2005-2007 CDO
ratings is pending. The European ESG ratings rules start in mid-2026.

**Q12.** The issuer pays for the opinion on its own securities. The filer's 2005-2007 structured-finance ratings led to the
2015 settlements, and the SEC's 2015 findings concerned 2011-2012 conduct. The newspaper test would be asked of that
record; not judged here.

**Q5 (judged before the stop, for the register):** integrity IN on the present managers; the institutional record of 2015
and 2024 and the issuer-pays incentive are written at Q5 for any later run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (6570ac2c); written question by question; committed after each
      (Q1 83ca5456, Q2 bcd7b784, Q3 7065a141, Q4 39a21781, Q5 405c652f, Q6 67343172, and this close).
- [x] Dispatched analyst: the brief allowed per-question pathspec commits of my two paths only; I did not hold the lock;
      the fold is the dispatching session's (operator rule 10).
- [ ] **The blind rule, kept with one breach declared**: my first command filtered a listing of `Test Runs/` on the
      ticker and printed three names of earlier SPGI files; none was opened; declared at the head of the file. No other
      run file, holding review or `PORTFOLIO.md` was opened, listed or searched.
- [x] Every v5 id checked against `principle_ledger_v5.csv` and every quoted fragment beside an id checked against its row
      by `check_quotes.py` in the research folder (output `check_quotes_out.md`); no E-ids; every filing fact has its
      accession.
- [x] The order was kept; the first STOP that failed (Q6's narrower STOP) closed the run; everything after it is headed
      COMPUTATION, NOT A CLEARANCE or recorded as facts.
- [x] Owner cash after every real cost, never a net-income proxy; stock pay deducted; the sovereign from the US Treasury;
      the price is an aggregator quote, flagged. Two estimates (Mobility's cash; IHS Markit's pre-merger share without
      Transportation) are confessed as CONVENTIONS of this run with their rationale.
- [x] Contrary evidence written down as found (foundations; Q1; Q2 test 4; Q6 sensitivity).
- [x] Not a point-in-time run; the Q6 test is point-in-time on filings and Treasury data of its dates, and cites no row
      for a fact after them.
- [x] Only the arithmetic lines of `tools/run.py` were used; its "split" factor (the spin-off adjustment) was ignored.
- [x] `python tools/check_framework.py`: **PASS** before the final commit (2026-10-11). `check_quotes.py`: no E-ids, 78
      distinct ids all in the ledger; every fragment beside an id in its row (24 filing or framework quotes reviewed by hand).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q6's narrower STOP has no method, no date limit and no box.** "Below its intrinsic value" is not defined for a deal
   years past. I used Q7's construction at the deal date's sovereign, because Q6's buyback test already reads the Q7
   range. The answer turns on the rate: at the 2.29% of 2022-02-25 the stock was 0.80 of its bottom; at 3% the price
   sat just above the bottom; on the ten-percent floor, which Q7 applies to buying, the 2022 price looks full. The
   framework holds two measures of value (the range at the sovereign and the floor at ten percent) and does not say
   which one "intrinsic value" means outside Q7. Nor does it say whether a deal made under an earlier chief executive
   (the merger was signed in 2020) still closes a file today, or which box the STOP fills; I named OUT as a CONVENTION.
   A ruling is needed; a reader who reads "intrinsic value" as the floor would not close here and would go on to Q7,
   where the computation above closes OUT on the floor anyway.
2. **The parts rule lets a part with 45% to 49% of profit decide** while the three parts that do not decide carry the
   rest, and one of them (Market Intelligence, 16% to 22%) is the part whose ten-year economics I could not foresee. Q1's
   doubt rule and the parts CONVENTION pull apart here; the convention governed.
3. **A non-deciding part whose future cannot be judged** is not covered: Q2 sends an open non-deciding part to Q7 at no
   growth and says nothing of a TOO HARD one. I used the same treatment (a CONVENTION of this run); the computation above
   did not in fact separate Market Intelligence, which is a gap in my own work, noted.
4. **The five-year window across a merger and a spin-off.** Convention (c) values a merger inside the window on the
   combined companies' averages, but says nothing of a spin-off after the window that shrinks the perimeter, of a target
   whose months before closing were never filed, or of a filer that gives a spun business's income but not its cash.
   Each needed an estimate, confessed above; the central base departs from the five-year average to the three years the
   filer restated, with the literal window beside.
5. **Template.** The template has no slot for a WEIGHING question's narrower STOP closing the file (Q3, Q6, Q9); the
   NOT REACHED marks and the box line were written by analogy with the other STOPs.
