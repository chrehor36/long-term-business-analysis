# Company Run: Callaway Golf Company (NYSE: CALY) - 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Every judgment cites a v5 ledger id in bold;
every filing fact carries its accession; the first STOP that failed closed the run and later questions are NOT REACHED.
Working folder: `Test Runs/_research 2026-10-05 CALY/` (filings as text, `calc.py` for the arithmetic, `rows.txt` for the
ledger rows read).

**POSITION NOTE, declared before any verdict:** not checked. The template says to check `PORTFOLIO.md`; the brief's blind
rule forbids opening it, and the blind rule was kept. Whether the operator holds CALY is unknown to this analyst.

**CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`, `Screens/WATCHLIST RUN
QUEUE.md`, the prepped reading list, any other `Test Runs/` file on CALY or MODG (a listing of `Test Runs/` for
"caly|modg|callaway|topgolf" returned nothing), other companies' 2026-10-05 runs and research passes, and the unadopted
small-cap gaps case. Seen without opening: the session's git snapshot, which names recent commit subjects (v5 runs of OGN
OUT at Q1, PENN OUT at Q2, YELP TOO HARD (NATURE) at Q1, ROCK TOO HARD (WORK) at Q2, a session-state commit on S&P 600 ranks)
and untracked run files for CENT, PRKS and TDS; and the auto-memory index, which says v5 governs, wave 7 is paused, and "57
gate-clearers, nothing buyable". None of it concerns this company. The verdicts in those subjects are a mild prior that
small and mid caps close early; it was noted and set aside.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $14.28 (2026-10-05; `tools/run.py` live quote, **aggregator, flagged** per operator rule 5).
- **Shares by class:** one class, common, **178,510,521** as of the cover of the 10-Q for the period ended 2026-06-30, filed
  2026-08-04, accession `0000837465-26-000022` (`python Screens/cover_shares.py CALY`). The same 10-Q's diluted
  weighted-average count for the quarter is 190.1M against 179.7M basic: award dilution is real and is carried at Q4 below.
- **Market cap:** $2,549M (178.51M x $14.28).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 10/05/2026 (as fetched
  by `tools/run.py` from the issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-27, `0000837465-26-000010`; 10-Q Q2 2026, filed 2026-08-04,
  `0000837465-26-000022`; 8-K of 2025-11-18 (Topgolf sale agreement), `0001193125-25-286175`; 8-K of 2026-01-07 (sale
  closed), `0000837465-26-000003`; 10-K FY2024 `0000837465-25-000024`; the selected financial data and segment tables of the
  10-Ks for FY2002 `0000936392-03-000258`, FY2003 `0000936392-04-000209`, FY2008 `0001193125-09-039469`, FY2013
  `0000837465-14-000002`, FY2018 `0000837465-19-000002`, FY2020 `0000837465-21-000003`, FY2022 `0000837465-23-000006`,
  FY2023 `0000837465-24-000016`. The proxy (DEF 14A filed 2026-04-08, `0000837465-26-000013`) was fetched and not read for
  judgment, because Q5 was not reached. The 8-K of 2026-05-26 (`0001193125-26-239488`) was fetched; only its cover was read.
- **One figure cross-checked against the filed statement:** `tools/run.py` gives FY2025 operating cash flow of $334.0M. The
  filed cash flow statement (10-K FY2025, F-7) shows $334.0M **in total**, of which $219.7M is continuing operations and
  $114.3M discontinued (Topgolf and Jack Wolfskin). The figure transcribes correctly; **the tool's owner-earnings lines are
  therefore built on cash flows that include businesses the company no longer owns** (its 2023 and 2024 OCF of $364.7M and
  $382.0M are likewise totals, against continuing $224.9M and $166.2M). Its "yield 11.32%" and its five-year window
  (which takes in Topgolf's $322.3M and $532.3M of 2021-2022 capex) are not used anywhere in this run.
- **`tools/run.py` arithmetic lines used:** the price, the cover share count, the sovereign, and the ten-year balance-sheet
  transcription (read against the filed statements at Q4 below). Nothing it prints as a rule or verdict was read as one
  (Part VII, the tooling).

**What the company is today, from the filings.** Callaway Golf Company (renamed from Topgolf Callaway Brands on 2026-01-15;
ticker MODG to CALY on 2026-01-16, 10-K FY2025 Item 1) has two segments: Golf Equipment (Callaway clubs and balls, Odyssey
putters; FY2025 sales $1,375.1M, segment income $170.1M) and Apparel, Gear and Other (TravisMathew, Callaway soft goods,
OGIO; $685.0M, $87.8M). Jack Wolfskin was sold to ANTA Sports on 2025-05-31 for about $290.0M. **A 60% stake in Topgolf and
Toptracer was sold to Leonard Green & Partners effective 2026-01-01** "based upon an equity value of approximately $1.1
billion", for net proceeds of $820.1M after preliminary adjustments (10-Q Q2 2026, MD&A); the company keeps 39.3% (after
dilutive units issued by Topgolf in April 2026), carried at $213.9M under the equity method, and retains Full Swing. The
term loan was repaid in full on 2026-05-29 and the convertible notes are gone; at 2026-06-30 debt is a $43.1M Japan
asset-based facility and $7.7M of equipment notes against $278.1M of cash. Treasury stock rose from 2.3M to 7.1M shares in
the half year ($84.5M spent).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**,
and for this name the answer turns on whether the golf equipment business holds its place through product cycles nobody
can schedule. The market serves: the price has moved from a $19.40 deal price in 2021 to $14.28, and "It just tells us
prices." **[M2006-077]**; it is read for nothing else. No macro enters: tariffs, rounds played and consumer spending are
named in the filing as business variables, and "the way we pick our investments is we just don’t get into the macro
factors" **[M2000-094]**. Margin of safety is an attitude here: if the case needs a pencil, "it’s too close to think about"
**[M1996-084]**. The analyst's habits govern the hunt: write the contrary evidence down at once **[M1997-127]** and look
for "looking at what you’re missing" **[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]** (against the verdict this run reaches, and against the
business, in the order found):
1. (Against the business) Five consecutive operating losses, 2009 to 2013, while Acushnet's golf business stayed profitable
   in every one of the same years (Q2 row below).
2. (Against the business) The filer's own risk factor: "New product introductions, price reductions, consignment sales,
   extended payment terms, 'closeouts,' including closeouts of products that were recently commercially successful, and
   significant tour and advertising spending by competitors continue to generate intense market competition." (10-K FY2025,
   Item 1A, `0000837465-26-000010`.)
3. (Against the business) Topgolf, bought in 2021 for stock at a fixed $19.40 a share on an equity value of $1,987.0M, was
   impaired by $1,452.0M in 2024 and a further $284.0M (trade name) and $143.1M (loss on sale) in 2025, and 60% of it was
   sold on an equity value of about $1.1B (10-K FY2022 `0000837465-23-000006`; 10-K FY2025).
4. (Against my verdict) Golf Equipment has earned a segment profit every year since 2014, and H1 2026 segment income rose
   22.4% to $217.9M with gross margin 48.7% against 44.5% (10-Q Q2 2026), credited to "favorable pricing, product mix, cost
   savings from gross margin initiatives and lower tariffs". A business with no pricing power does not usually write that.
5. (Against my verdict) Odyssey: "According to Golf Datatech, sales of Odyssey putters in 2003 accounted for almost 50% of
   all revenue generated from putters sold in the United States." (10-K FY2003, `0000936392-04-000209`.) That is a
   franchise-like position in one category, and no later share figure was found in the filings read.
6. (Against my verdict) The balance sheet is now nearly debt-free, so a bad product year no longer threatens solvency as
   2009 to 2013 might have.
7. (Against the business) Acushnet, the strongest competitor, says of its own industry that "there may be low barriers to
   entry in many of our markets" (Acushnet 10-K FY2025, Item 1A, `0001672013-26-000057`).

## THE STANDING RULE
The rule binds the buyer: "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**. A cash purchase of a minority stake, unlevered, cannot ruin the buyer; "the only way smart people can get
clobbered, really, is through leverage" **[M2004-065]**. Nothing in this name changes that. No purchase is proposed, so
there is nothing further to test.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years", including "where the company will stand within the industry" **[M2012-065]**; the product may stay
opaque if "I understand the economic dynamics of the industry" **[M2011-014]**; the first step is "trying to identify the
key variables in that particular business" **[M1998-044]**.

**The key variables, from the filer's own text** (10-K FY2025 Item 1A): (1) rounds played and the number of golfers, which
drive balls and replacement; (2) the success of each launch, since products "generally have life cycles of two-to-three
years" and "a substantial portion of our annual revenues is generated each year by products that are in their first year of
their product life cycle"; (3) share against "several well-financed competitors", one of which holds an "estimated U.S.
market share of over 50%" in balls; (4) tour usage, bought with "significant cash incentives"; (5) retailer concentration;
(6) tariffs and currency; (7) the Rules of Golf, including the ball rollback "effective in January 2028 for professional
golfers and January 2030 for recreational golfers".

**What can be foreseen.** The industry's shape for ten years: the same few makers named in the filer's competitor lists in
2003, 2008, 2013, 2018 and 2025 (Acushnet/Titleist, TaylorMade, Ping, Srixon/Cleveland, Bridgestone, Mizuno); a product
whose performance is capped by the Governing Bodies, so the forecast is about golfers' behaviour rather than a galloping
technology, which the rows treat as a consumer question **[M2023-030]**, **[M2017-019]**; and Callaway as one of the
three or four premium club makers. What cannot be foreseen from these filings is whether Callaway's launches will beat its
rivals' in any given cycle. The rows ask whether a business is "quite dependent on the technology continuing to gallop"
and would be "a terrible business" without continued invention **[M1999-075]**; golf clubs depend on continued launches, but
the launches run inside a fixed rule book and the filer names "consumer demands for the latest technology", which is a
consumer behaviour, so I do not read M1999-075 as closing the file here. That reading is mine and is carried to "What was
unclear" below.

**Routing.** Whether Callaway's place within the industry holds is the castle question; the rows put "a sustainable edge"
after understanding: "if it passes through that, it’s whether a company can have a sustainable edge" **[M1997-148]**. I
can describe the economic dynamics of the industry and name the variables; the doubt rule ("if you have doubts about
something being into your circle of competence, it isn’t." **[M2002-092]**) bites on the company's ten-year standing, which
Q2 owns, not on the industry's economics.

**The parts (holding company read by parts, CONVENTION of the framework).** The 39.3% Topgolf stake is carried at $213.9M,
about 8% of the market value, produced a $28.7M equity-method loss in H1 2026 and a $5.6M cash distribution (10-Q Q2 2026,
Note 9). It is a minority stake in a leveraged, private-equity-controlled venue business whose same-venue sales "have
recently declined" (10-K FY2024 Item 1A, `0000837465-25-000024`). By the convention, a part that cannot be understood and
that matters keeps the whole outside; I judge this part small enough not to decide the whole and value it at carrying
amount in the computation below. The open tension, reading a group without the parts **[M2023-031]**, is noted.

**VERDICT: IN (narrowly).** The industry's economics and the company's variables are named in its own filings; the
question whether its position lasts goes to Q2.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and "How much do they depend on the genius of the lord in the
castle?" **[M1995-038]**.

**The competitor row** (operating income over net sales, each company's own filings; USD M):

| Year | Callaway (consolidated, golf-era; continuing ops 2023-25) | Acushnet (Fortune Brands Golf segment 2005-2010; Acushnet Holdings 2012-2025) |
|---|---|---|
| 2005 | 17.2 / 998.1 = 1.7% | 171.5 / 1,265.8 = 13.5% |
| 2007 | 90.2 / 1,124.6 = 8.0% | 165.5 / 1,405.4 = 11.8% |
| 2008 | 84.2 / 1,117.2 = 7.5% | 125.3 / 1,368.9 = 9.2% |
| 2009 | (30.5) / 950.8 = -3.2% | 25.0 / 1,218.3 = 2.1% |
| 2010 | (26.6) / 967.7 = -2.7% | 88.7 / 1,241.6 = 7.1% |
| 2011 | (81.1) / 886.5 = -9.1% | not in the filings read (Fila ownership) |
| 2012 | (116.2) / 834.1 = -13.9% | 80.2 / 1,451.1 = 5.5% |
| 2013 | (10.8) / 842.8 = -1.3% | 114.9 / 1,477.2 = 7.8% |
| 2016 | 44.2 / 871.2 = 5.1% | 140.8 / 1,572.3 = 9.0% |
| 2018 | 128.4 / 1,242.8 = 10.3% | 172.3 / 1,633.7 = 10.5% |
| 2019 | 132.7 / 1,701.1 = 7.8% | 185.7 / 1,681.4 = 11.0% |
| 2023 | 194.1 / 2,132.7 = 9.1% | 285.3 / 2,382.0 = 12.0% |
| 2024 | 152.9 / 2,077.7 = 7.4% | 304.3 / 2,457.1 = 12.4% |
| 2025 | 128.1 / 2,060.1 = 6.2% | 299.4 / 2,558.7 = 11.7% |

Sources: Callaway selected financial data in the 10-Ks for FY2002, FY2003, FY2008, FY2013, FY2018 and the FY2025 statements
(accessions in Step 0); Fortune Brands 10-K FY2007 `0001193125-08-041927` and FY2010 `0001193125-11-043658` (Golf segment
operating income, before corporate expense, and the segment included Cobra until 2010); Acushnet 10-K FY2016
`0001558370-17-002327` (2012-2016) and Acushnet XBRL from its 10-Ks through FY2025 `0001672013-26-000057`. The bases are not
identical (segment before corporate cost for Fortune Brands; consolidated after corporate cost for Callaway and Acushnet
Holdings; Callaway before 2006 did not expense options), and the gap runs the same way on every basis. Over the 25
comparable Callaway years (1998-2019 and 2023-2025) the mean operating margin is 4.15%, with operating losses in 7 of 25
years (1998, 2004, 2009, 2010, 2011, 2012, 2013); Acushnet's mean over the 20 years shown is 9.76%, its lowest 2.1% (2009),
with no loss year. Callaway's margin was below Acushnet's in every year shown; it came closest in 2018.

**TaylorMade and Ping are private: no filing, flagged, no figure used.** The one filed statement about TaylorMade is
Callaway's own: competitors "compete for market share in the golf clubs business, with TaylorMade having a significant
market share of the golf clubs business in the United States" (10-K FY2013, `0000837465-14-000002`).

**Dave & Buster's (PLAY), for the venue part:** operating income $306.6M (fiscal year ended 2024-02-04) falling to $86.1M
(fiscal year ended 2026-02-03), 10-K `0001525769-26-000008`. Topgolf's own record in the same years is the impairments listed
at contrary evidence 3. The venue part is a 39.3% minority stake and does not decide Q2; it gives no help to the castle.

**The castle tests, each with its filing fact.**
1. *What keeps it standing, and how permanent?* The filer's answer is invention and launch: "We innovate to maintain our
   market share leadership position ... by continually investing in research and development" (10-K FY2025 Item 1). The
   advantage lasts one product cycle, "two-to-three years", and "For new products to generate equivalent or greater revenues
   than their predecessors, they must either maintain the same or higher sales levels with the same or higher pricing, or
   exceed the performance of their predecessors" (10-K FY2025 Item 1A). The rows' sentence for this is "A moat that must be
   continuously rebuilt will eventually be no moat at all." **[L2007-005]**.
2. *Would it stand without the lord?* The losses ran from 2009 to 2013; the present chief executive "has served in such
   capacity since March 2012" (10-K FY2025, executive officers) and the recovery from 2014 followed. A recovery dated to a
   new chief executive is the case the rows describe as businesses "where you have to stay smart" **[M1995-040]**; "if a
   business requires a superstar to produce great results, the business itself cannot be deemed great" **[L2007-006]**.
   The filing does not prove the recovery was his; it is consistent with it, and nothing in the filings read shows the
   business earning through a cycle without a winning launch.
3. *The money test.* No new entrant's figures are on the public record. The filer says "we compete with several
   well-financed competitors with reputable brand names" (Item 1A), and Acushnet says "there may be low barriers to entry in
   many of our markets". The rows: "there are some industries that are just never going to have barriers to entry" and "you better be
   running very fast" **[M2012-106]**; "one competitor is frequently enough to ruin a business" **[M2012-108]**.
4. *Pricing power.* The filer books "sell-through promotions" throughout a product's life and "price concessions or price
   reductions" at its end (10-K FY2025, revenue note); its competitors' "price reductions, consignment sales, extended
   payment terms" and closeouts of "recently commercially successful" products set the market (Item 1A). Against that, H1
   2026's "favorable pricing" (contrary evidence 4). The rows' measure is "a prayer session before you raise your prices a
   penny" **[M2005-020]**, and the positive form is to "charge more for a product and maintain or increase market share
   against wellentrenched, well-known competitors" **[M2000-031]**. Over the span the second is not shown: Golf Equipment
   sales were $1,124.6M in 2007 and $1,375.1M in 2025, 1.1% a year nominal for 18 years (10-Ks FY2008 and FY2025), while
   Titleist golf equipment alone grew from $1,420.4M (2023) to $1,596.2M (2025) (Acushnet 10-K FY2025).
5. *Unit volume and share of mind.* Golf clubs $894.1M (2008), $710.7M (2013), $768.3M (2019), $1,097.1M (2022), $1,052.9M
   (2025); balls $223.1M (2008), $132.1M (2013), $210.9M (2019), $322.2M (2025). In 2003 the filer's "primary current
   objective is to increase its sales of drivers and fairway woods and regain market share" (10-K FY2003); in 2013 it
   named TaylorMade's "significant market share". Share of mind has been lost and regained, not held.
6. *The low-cost position.* No filing claims it. The filer assembles clubs mostly in Mexico and buys from contract makers
   in China and Vietnam, as competitors do; in 2003 its ball business "was not profitable due to its high cost structure"
   (10-K FY2003).
7. *The brand.* The brand "has to stand for something in the consumer’s mind" against the retailer **[M2015-038]**; the
   filer warns of retailers "gaining increased leverage, which may impact our margins" (Item 1A). Odyssey's 2003 putter
   position (contrary evidence 5) is the strongest brand fact found, and no current figure was found to say whether it held.
8. *Over the low bid.* Golfers pay premium prices for new clubs; the same golfers are offered last year's model at closeout,
   by Callaway and by every competitor (Item 1A). Whether they "ask for you by name" **[M2023-073]** rather than for the newest
   model from whoever launched best was not shown by any filing read.
9. *Ask the competitors.* The rows' question is "which one would it be and why?" **[M1999-130]**. The public record's
   nearest answer is in the ball market, where Callaway's own 10-Ks of 2003, 2008, 2013, 2018 and 2025 each give Acushnet
   more than half the US market. A rival choosing one castle in this industry to own would, on those filings, choose the
   ball franchise, not Callaway. That is my inference from the filed shares, not a competitor's statement.
10. *Widening or narrowing?* The rows ask "whether it’s likely to widen further or shrink on you" **[M1999-108]**. Golf
    Equipment segment income was $251.4M (2022), $193.3M (2023), $183.7M (2024, restated), $170.1M (2025), then $217.9M for
    H1 2026 against $178.0M. Over 2022 to 2025 Acushnet's operating income went from $281.5M to $299.4M. Narrowing over
    three years, rising in the last half year: not a widening shown.
11. *What could destroy, modify or reduce it?* The ball rollback of 2028 and 2030, tariffs ($22.0M of unfavourable impact
    on Golf Equipment in 2025, MD&A), and the next product cycle. "usually if something can gain competitive advantage very
    quickly, you have to worry about them losing it quickly, too" **[M2002-050]**; the 1990s Big Bertha leadership,
    then the 1998 operating loss (-$40.1M, 10-K FY2002) and the 2009 to 2013 losses, is that pattern on this company's own
    record. "Leadership alone provides no certainties" and leaders are often "companies now riding high but vulnerable to
    competitive attacks" **[L1996-031]**.

**Reading.** The same industry holds a castle: a ball business with more than half of US share in every year Callaway's own
filings record it, earning a profit in every year of the span including 2009. Callaway's position is the other kind: re-won
every two to three years by launches, defended with price reductions, closeouts and tour payments, and lost for five
consecutive years within the last seventeen. The rows put "there are going to be marauders. And they’ll never go away."
**[M2017-012]** as the condition of every castle; the record shows the marauders inside the walls in 1998, 2004 and
2009 to 2013. Q2's list of what it rules out names the moat that must be continuously rebuilt where the evidence shows the
rebuilding failing (the framework's wording), on the row "A moat that must be continuously rebuilt will eventually be no
moat at all." **[L2007-005]**; and the See's test reads "If the answer had been yes, we wouldn’t have done it."
**[M2011-015]**. A cheap price does not reopen it: "What you can’t do is turn any investment into a good deal by paying
little" **[M2019-015]**.

Why OUT and not TOO HARD. TOO HARD is for "a moat that’s tenuous in any way" whose value cannot be judged **[M2000-019]**.
Here the judgment can be made from the filings and the competitors' filings over twenty-eight years, and it runs one way:
the position is rebuilt each cycle and the rebuild has failed for long stretches, against a competitor in the same years
that did not fail. The 2014-2026 recovery (contrary evidence 4) is twelve good years inside a record that also holds seven
loss years; it shows the rebuild succeeding under the present management, not a castle that stands without it.

**VERDICT: OUT** **[M2006-013]**, **[L2007-005]**, **[M2011-015]**. The file closes here. Q3 to Q12 are NOT REACHED; the
balance sheets and the arithmetic below are reported at the owner's request and are COMPUTATION.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED. Facts found, not judged: continuing capex $50.0M, $48.7M, $31.8M (2023-2025) against D&A of $45.7M, $44.5M,
$46.4M; working capital is the heavy item (inventory $625.3M at 2025 year-end on $2,060.1M of sales).

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion; otherwise WEIGHING.
NOT REACHED as a verdict. **The balance sheets, read at the owner's request** ("balance sheets over an 8 or 10 year period
before I even look at the income account" **[M2025-032]**). Transcription from `tools/run.py` (first-filed XBRL), checked
against the FY2025 and Q2 2026 filed balance sheets; USD M.

| Year-end | Assets | Equity | Cash | Inventory | Goodwill | Intangibles | Debt on the face | Retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2018 | 1,053 | 725 | 64 | 338 | 56 | 225 | 50 | 414 |
| 2019 | 1,961 | 767 | 107 | 457 | 204 | 493 | 595 | 489 |
| 2020 | 1,981 | 676 | 366 | 353 | 57 | 484 | 687 | 360 |
| 2021 | 7,748 | 3,683 | 352 | 533 | 1,960 | 1,529 | 1,034 (partial) | 682 |
| 2022 | 8,590 | 3,774 | 180 | 959 | 1,984 | 1,504 | 1,396 (partial) | 852 |
| 2023 | 9,121 | 3,878 | 394 | 794 | 1,989 | 1,506 | 1,590 | 948 |
| 2024 (restated, Topgolf in discontinued) | 7,636 | 2,408 | 445 | 757 | 620 | 1,373 | 1,499 | (500) |
| 2025 (Topgolf held for sale) | 7,286 | 2,069 | 903 | 625 | 620 | 222 | 1,461 | (910) |
| 2026-06-30 (10-Q) | 2,783 | 2,162 | 278 | 518 | 620 | 222 | 51 | (741) |

What the figures say. (a) The 2019 Jack Wolfskin purchase took debt from $50M to $595M; the 2021 all-stock Topgolf merger
took equity from $676M to $3,683M and goodwill from $57M to $1,960M. (b) Retained earnings of $948M at 2023 became a deficit
of $910M at 2025: the Topgolf write-downs consumed every dollar the company had retained since 1982 and more. (c) Inventory
went from $338M (2018) to $959M (2022), the pandemic over-build, and was worked down to $518M by June 2026. Against golf and
lifestyle sales the 2025 figure is about 30% of $2,060.1M; the 2018 figure was about 27% of $1,242.8M. (d) $619.5M of
goodwill still sits on the June 2026 balance sheet with no Topgolf behind it: at the merger, $563.4M of goodwill was
"allocated to other business units" (10-K FY2022, merger note), that is to Callaway's own golf and apparel units. "Goodwill
should not be used in evaluating the fundamental attractiveness of a business." **[M2011-060]**; tangible equity at June 2026
is about $1,321M ($2,162.4M less $619.5M goodwill, $218.8M trade names, $3.1M intangibles). (e) Debt went from $1,590M
(2023) to $51M (June 2026), paid with the Topgolf and Jack Wolfskin proceeds; cash fell from $903M to $278M in the same
half year. What they can't say: whether the H1 2026 margin is a launch year or a level; June is the seasonal peak of
receivables ($315.7M against $123.2M at year-end). One cost to carry forward: stock pay of $23.8M to $33.3M a year and a
diluted share count about 10M above basic in Q2 2026.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED. Fact found, not judged: the chief executive since March 2012 "has served as a Director of TopGolf International,
Inc." since 2012, while Callaway held a minority stake (10-K FY2013), before Callaway merged with Topgolf in 2021.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found, not judged, which a reader reaching Q6 would have to weigh first: the 2021 merger paid for Topgolf
wholly in Callaway stock at a fixed $19.40 a share on a Topgolf equity value of $1,987.0M (10-K FY2022); 60% of Topgolf was
sold on an equity value of about $1.1B; the rows' STOP in Part A concerns an acquirer whose stock sits below its value,
"You simply can't exchange an undervalued stock for a fully-valued one without hurting your shareholders." **[L2009-019]**.
Whether the 2021 stock was below its value was not examined. Buybacks of $84.5M in H1 2026; the price paid per share and
the programme's stated price limit, if any, were not examined.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED. **COMPUTATION - NOT A CLEARANCE** (operator rule 3; the protocol's heading carries a dash that this file
writes as a hyphen). Reported at the owner's request. It carries no entry language and clears nothing: the file closed at
Q2.

**Owner cash after every real cost** ("a figure calculated after interest, taxes, depreciation, amortization and all forms
of compensation" **[L2021-003]**), continuing operations only, from the 10-K FY2025 cash flow statement (USD M):

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Operating cash flow, continuing | 224.9 | 166.2 | 219.7 |
| less stock pay | 33.3 | 27.6 | 23.8 |
| less capex | 50.0 | 48.7 | 31.8 |
| **Owner cash, capex basis** | **141.6** | **89.9** | **164.1** |
| Owner cash, D&A basis (D&A 45.7, 44.5, 46.4) | 145.9 | 94.1 | 149.5 |
| add back interest expense net (70.7, 63.0, 60.6) x (1 - 21%) | 55.9 | 49.8 | 47.9 |
| **Owner cash before interest (the debt is now repaid)** | **197.5** | **139.7** | **212.0** |

Three-year mean before interest: **$183.0M** (capex basis, levered mean $131.9M; D&A basis $129.8M). CONVENTIONS of this run,
confessed: (i) **three years, not five**: the continuing shape exists in the filings only for 2023 to 2025, because the
2021-2022 statements include Topgolf and Jack Wolfskin; (ii) the interest add-back at a 21% tax rate, because the debt that
bore it was repaid from sale proceeds already reflected in the net cash below; (iii) 2023's OCF holds a $153.8M inventory
release and 2024's a $34.1M build, so the base-year warning applies ("it will pay you to be suspicious as to why the
beginning and terminal years have been selected" **[L2005-003]**).

**Growth shown.** Owner cash before interest, 2023 to 2025: 3.6% a year (endpoints, aggregate). Sales over the same years
fell, from $2,132.7M to $2,060.1M. Q3 cap (stated, though Q3 was not reached): Golf Equipment sales grew 1.1% a year nominal
from 2007 to 2025, and a rate above that is not carried as the central case **[M1997-095]**.

**The range** (Q7 CONVENTION: carried ten years, then zero nominal growth, discounted at the 5.66% sovereign; plus net cash
at 2026-06-30 of $227.3M ($278.1M less $43.1M and $7.7M) and the Topgolf stake at its $213.9M carrying amount; 178.51M
shares; `calc.py`):
- no growth: **$20.59** a share;
- capped growth (1.1%): $22.27;
- shown growth (3.6%): **$26.59**.
**VALUE RANGE: $20.59 to $26.59** against $14.28 (top to bottom 1.29 to 1, narrower than three to one).

**Whole-cycle variant** (the five-year window convention's purpose, applied to a window that is abnormal: 2023-2025 margins of
6.2% to 9.1% against a 25-year mean of 4.15%). The 25-year mean operating margin on 2025 sales gives operating income of
$85.5M, $67.6M after a 21% tax with D&A taken as equal to capex: **$9.16** (no growth) to **$9.78** (capped growth) a share
at the sovereign, both including net cash and the Topgolf stake. CONVENTION of this run: the margin series mixes
golf-only years (to 2016) with years carrying apparel and corporate costs, and pre-2006 years did not expense options; the
mean is a reading of the record's centre, not a forecast.

**FAIR PRICE** (the price at or below which the central case clears the ~10% pre-tax floor, the framework's CONVENTION from
"we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]** and "at least 10% pre-tax
returns" **[L2002-020]**). Tax treatment, CONVENTION of this run: owner cash is after the company's income tax and before the
holder's; the expected return is owner cash over enterprise value plus growth; "pre-tax" is read as before the holder's
taxes. Central case ($183.0M, 1.1% growth): enterprise value $2,062M, **fair about $14.02** a share. Whole-cycle case:
**about $6.74**. At $14.28 the central case's owner cash yields 8.68% on the $2,108M enterprise value the price implies,
about 9.8% with the capped growth: at or just under the floor, and a case that needs a calculator: "It should scream at
you." **[M2009-005]**; it does not.

**CHEAP PRICE** (below which no pencil is needed). Rule, CONVENTION of this run: the price at which the whole-cycle owner
cash, with no growth at all, alone yields the 10% floor, so that neither the recent margins nor any growth has to be
believed; this also answers the rows' demand that the margin widen with volatility ("the more volatile the business is"
**[M1997-080]**). **Cheap about $6.26** a share.

| | per share |
|---|---|
| Price (2026-10-05, aggregator) | $14.28 |
| Value range (sovereign, 3-year base) | $20.59 to $26.59 |
| Whole-cycle range (sovereign) | $9.16 to $9.78 |
| Fair (central case at ~10% floor) | ~$14.02 |
| Fair (whole-cycle at ~10% floor) | ~$6.74 |
| Cheap (whole-cycle, no growth, 10%) | ~$6.26 |

The spread between the three-year range and the whole-cycle range is the business's record, not a choice of window: the
rows do not "compensate for that sort of thing by having some extra large margin of safety" **[M2007-022]**, and Q2 has
already closed the file.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED. Fact found: at 2026-06-30, debt of $51M against cash of $278M; operating lease liabilities $199.6M; the company
indemnifies the Topgolf buyer against "certain ongoing litigation matters, subject to certain thresholds" (8-K of
2025-11-18).

## Q10: IS IT THE FAT PITCH?
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked. Golf equipment and apparel are not among the named businesses.

---
## THE BOX
**OUT at Q2** **[M2006-013]**: the golf equipment position must be re-won every two-to-three-year product cycle, is defended
with price reductions, closeouts and tour payments in the filer's own words, and failed for five consecutive years (2009 to
2013) and in 1998 and 2004, while Acushnet, in the same industry and the same years, never lost money and earned a higher
margin in every comparable year **[L2007-005]**, **[M2011-015]**. COMPUTATION only: value range $20.59 to $26.59 on the
2023-2025 base, $9.16 to $9.78 whole-cycle, fair about $14.02 (central) or $6.74 (whole-cycle), cheap about $6.26, against
$14.28.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch: **yes**. Written question by question and committed after each: **no**.
      The brief forbade commits, and the questions were written in one pass after the reading, not as each closed. Declared.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact carries its accession
      or names its filing; the PLAY and Acushnet figures carry theirs. Private competitors flagged, no figure used.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; nothing after Q2 is a clearance; Q7 is headed COMPUTATION.
- [x] Owner cash after every real cost from continuing operating cash, stock pay and capex, never net income (operator
      rule 5); the tool's consolidated owner-earnings lines were found to include discontinued businesses and were not used.
      Sovereign from the Treasury par curve; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found **[M1997-127]**: seven items, three of them against this verdict.
- [x] No point-in-time anchor; Part VII's later-row bar does not apply.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` **PASS** on 2026-10-05 (run-file sweep: phantom ids in 0 files). The Python check in
      `Test Runs/_research 2026-10-05 CALY/verify.py`: no em or en dashes, no E-ids, all cited M/L/R ids present in
      `principle_ledger_v5.csv`, and every quoted fragment set directly beside an id found in that row (the script's
      remaining flags are filing quotes carried with their own accessions earlier in the same paragraphs). No commit made,
      as the brief instructed.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Where a product-cycle business closes.** Q1's OUT list names businesses that live on continued invention, on the row
   "if they had never invented any more pharmaceuticals, it would be a terrible business" **[M1999-075]**; Q1's TOO HARD
   paragraph names industries whose winners cannot be named; Q2's OUT list names the moat that must be rebuilt, on the row
   "A moat that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**. A golf club maker fits all three in part, and a second analyst could
   close this name at Q1 OUT, Q1 TOO HARD or Q2 OUT on the same filings. I took Q2 because the rows put "a sustainable edge"
   after understanding **[M1997-148]** and because M1999-075 speaks of technology that must "gallop", which the Rules of Golf
   cap. The framework does not say which of the three governs a business whose industry is stable and whose position within
   it turns over by product cycle. A TOO HARD (WORK) reading also exists: club market share by category over fifteen years
   (Golf Datatech, paid) is not on the public record, and a reader could hold that share data would decide the castle. I did
   not take it, because the profit record and the competitor's profit record already answer the question the share data
   would ask.
2. **The five-year average when the business was reshaped.** Q7's convention asks for five years of owner cash; a company
   that sold two of its three segments in eighteen months has three restated years of the business that remains. The
   framework has no rule for the shorter window or for falling back to the long record; this run used three years and showed
   the whole-cycle variant beside it.
3. **"Pre-tax" in the floor.** The speakers' "at least 10% pre-tax returns" **[L2002-020]** are stated beside an
   after-corporate-tax translation in the same row, so they are pre-corporate-tax for a corporate holder; the convention does not say whether a run's owner cash,
   which is after the company's tax, is to be grossed up. Read here as before the holder's tax; stated.
4. **The holding company by parts has no threshold for "matters".** The Topgolf stake is about 8% of the price and loses
   money; I judged it not to matter to the whole. The convention gives no size or earnings test.
5. **The tool and discontinued operations.** `tools/run.py` builds owner earnings from total operating cash flow, which for
   this filer includes Topgolf and Jack Wolfskin in every year it prints; its 11.3% yield is overstated for the company that
   exists. A filer with discontinued operations needs the continuing-operations line.
6. **The template's position note against the blind rule.** The template says to check `PORTFOLIO.md`; the brief forbade
   opening it. The note was left unchecked and declared.
7. **The protocol's heading and the house style.** Operator rule 3's heading "COMPUTATION" carries an em dash; this file
   follows the no-em-dash rule and writes a hyphen. If the acceptance test ever looks for the exact string, it will miss it.
