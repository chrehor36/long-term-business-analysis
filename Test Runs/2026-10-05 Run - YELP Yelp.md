# Company Run: Yelp Inc. (NYSE: YELP), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. The template was copied to this dated name before any fetch. Working folder:
`Test Runs/_research 2026-10-05 YELP/` (filings as text, `compute.py` and its output `compute_out.txt`, `run_py_output.txt`).

*Dash note: the only dashes of that kind in this file are inside the protocol's required label "COMPUTATION — NOT A
CLEARANCE" (operator rule 3), written as the protocol writes it, and inside nothing else.*

**POSITION NOTE, declared before any verdict:** not checked. The dispatch's blind rule forbids opening `PORTFOLIO.md`, so
whether the operator holds YELP is unknown to this analyst. The template asks for the check; the blind rule wins here.

**CONTAMINATION DECLARED.** Seen before or during the run, not opened: the git status and recent commit subjects of the
session (five purchase runs of 2026-10-05, ANDE, SLVM, LKQ, SCSC and KSS, all closed OUT at Q2; three untracked run files
of the same day, ENR, LCII and ROCK, names only); the memory index line "57 gate-clearers, nothing buyable". None concerns
Yelp or its competitors. No other `Test Runs/` file about Yelp was searched for or opened (a directory listing filtered on
"yelp" returned nothing before this file was created). No queue, resume-state or reading-list file was opened.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $18.52 (close 2026-10-05; Yahoo Finance chart endpoint via `tools/run.py`; **aggregator, live quote only,
  flagged** per operator rule 5). Weekly closes from the same aggregator: $25.81 (2026-07-06), $23.18 (2026-08-24),
  $18.03 (2026-09-21), $18.50 (2026-10-05).
- **Shares by class** from the latest filing's cover: **54,263,621** common shares, par $0.000001, one class, as of
  2026-07-31 (Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-07, accession `0001345016-26-000066`;
  `python Screens/cover_shares.py YELP` returned the same). No second class in the charter note of the cover.
- **Market cap:** $1,005.0M. Balance sheet at 2026-06-30 (same 10-Q): cash and equivalents $94.1M, no marketable
  securities, revolving credit facility drawn $100.0M: net debt $5.9M, enterprise value about $1,010.8M.
- **Sovereign for the earnings currency (USD):** 5.63%, 30-year par yield, US Treasury daily par yield curve, 2026-10-02
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-27, `0001345016-26-000019`: Item 1 (business, competition), Item 1A (traffic, search
    engines, AI, competition), Item 5 (repurchases), Item 7 (key metrics, results, liquidity), the cash flow statement, the
    tax and other-income notes.
  - 10-Q Q2 2026, filed 2026-08-07, `0001345016-26-000066`: MD&A, key metrics, legal proceedings, repurchases, subsequent events.
  - DEF 14A, filed 2026-04-17, `0001345016-26-000027`: read only for the stock-pay target lines (Q5 and Q6 NOT REACHED).
  - 8-Ks: `0001345016-25-000086` (revolver raised to $325.0M, 2025-12-18); `0001345016-26-000007` (Hatch bought for about
    $270M cash plus $30M retention, closed 2026-02-02, funded in part by the revolver); `0001345016-26-000033` (CTO leaves
    2026-06-30); `0001345016-26-000051` (Chief Product Officer leaves 2026-07-03; meeting votes); `0001345016-26-000059`
    (Q2 2026 results, Exhibit 99.1; the Exhibit 99.2 shareholder letter is filed as page images and was not read).
  - 10-Ks FY2015 to FY2024 for the ten-year metric series: `0001206774-16-004640`, `0001206774-17-000642`,
    `0001628280-18-002519`, `0001628280-19-002312`, `0001345016-20-000009`, `0001345016-21-000015`,
    `0001345016-22-000026`, `0001345016-23-000009`, `0001345016-24-000009`, `0001345016-25-000007`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 $372,029K on
  the filed consolidated statement of cash flows (10-K FY2025, page F-7) equals the tagged 372.0 that `tools/run.py`
  printed; stock-based compensation $133,993K and purchases of property, equipment and software $48,353K also agree.
- **`tools/run.py YELP --framework v5`, arithmetic lines only** (Part VII; nothing it prints as a rule was used; full
  output in `run_py_output.txt`). Owner cash = operating cash flow less all stock pay less all capital spending (the
  capex line is "Purchases of property, equipment and software", so capitalized software is inside it), USD millions:

| FY | revenue | OCF | stock pay | stock pay % rev | capex | owner cash (capex basis) | D&A basis |
|---|---|---|---|---|---|---|---|
| 2016 | 716.1 | 126.9 | 86.3 | 12.1% | 23.0 | 17.6 | 5.3 |
| 2017 | 850.8 | 167.6 | 100.4 | 11.8% | 30.2 | 37.0 | 26.0 |
| 2018 | 942.8 | 160.2 | 114.4 | 12.1% | 45.0 | 0.8 | 3.0 |
| 2019 | 1,014.2 | 204.8 | 121.5 | 12.0% | 37.5 | 45.8 | 33.9 |
| 2020 | 872.9 | 176.7 | 124.6 | 14.3% | 32.0 | 20.1 | 1.5 |
| 2021 | 1,031.8 | 212.7 | 151.7 | 14.7% | 28.3 | 32.7 | 5.3 |
| 2022 | 1,193.5 | 192.3 | 156.1 | 13.1% | 32.0 | 4.2 | -8.7 |
| 2023 | 1,337.1 | 306.3 | 173.5 | 13.0% | 26.8 | 106.0 | 90.6 |
| 2024 | 1,412.1 | 285.8 | 158.2 | 11.2% | 37.3 | 90.3 | 87.2 |
| 2025 | 1,465.0 | 372.0 | 134.0 | 9.1% | 48.4 | 189.7 | 187.9 |

  Five-year mean (2021 to 2025): 84.6 (capex basis), 72.5 (D&A basis). Ten-year mean: 54.4. Twelve months to
  2026-06-30: 179.4. Stock pay over 2016 to 2025 totals $1,320.6M against operating cash less capex of $1,864.8M: 71% of
  the cash the business threw off before stock pay was paid out as stock pay. The 2025 figure is lifted by tax timing: the
  10-K says the One Big Beautiful Bill Act of July 2025 restored *"full expensing of domestic research and development
  expenses"*, after Section 174 had required capitalization from 2022; deferred taxes added $25.1M to 2025 operating cash
  after subtracting $24.9M in 2024, and cash taxes paid fell from $58.2M (2024) to $34.5M (2025). The 2022 to 2024 figures
  are depressed by the same rule in the other direction (cash taxes paid $2.5M in 2021, $50.4M in 2022).

- **Balance sheets, ten year-ends, read before the income account** (the file closes before Q4, so they are read here, as
  the dispatch asked; transcription from `tools/run.py`, first-filed XBRL, checked against the FY2025 and Q2 2026 filed
  balance sheets), "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**:

| year-end | assets | liabilities | equity | cash | receivables | goodwill | intangibles | debt | retained (deficit) |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 885 | 78 | 807 | 272 | 69 | 171 | 33 | 0 | -70 |
| 2017 | 1,217 | 117 | 1,100 | 548 | 76 | 108 | 17 | 0 | 70 |
| 2019 | 1,071 | 316 | 755 | 170 | 107 | 105 | 10 | 0 | -493 |
| 2021 | 1,051 | 299 | 751 | 480 | 107 | 105 | 11 | 0 | -760 |
| 2023 | 1,015 | 265 | 750 | 314 | 146 | 104 | 8 | 0 | -1,025 |
| 2025 | 958 | 248 | 711 | 216 | 153 | 136 | 49 | 0 | -1,291 |
| 2026-06-30 | 991 | 346 | 645 | 94 | 158 | 355 | 92 | 100 | -1,417 |

  (2018, 2020, 2022 and 2024 are in `run_py_output.txt` and run between their neighbours; "cash" is cash and
  equivalents only, marketable securities excluded.) What the figures say: the business has needed almost no capital to
  run (receivables rose from $69M to $158M as revenue doubled, about 10% of revenue throughout; no inventory; fixed
  assets small), and every surplus dollar, plus the 2017 Eat24 sale proceeds and most of the cash pile, has gone to
  buying back stock: the accumulated deficit grew from $70M to $1,417M while the business was profitable in most years,
  because retired shares are charged there. What they say since January 2026: for the first time the company borrows
  (revolver $100M), cash fell from $319M (cash plus securities at 2025 year-end) to $94M, and goodwill plus intangibles
  ($447M) now equal about 69% of equity after the Hatch purchase. What they cannot say: how much of the reported
  revenue rests on traffic Google chooses to send. Provision for credit losses runs about 3% of revenue ($43.3M in 2025),
  the cost of selling to small businesses that cancel or fail.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content owning Yelp "if the market closed for five years"
**[M1997-109]**, and that turns entirely on what local search looks like in five years, not on the 28% fall in the
quote since July; the quote "just tells us prices" **[M2006-077]**. No macro view enters: the filer blames the
*"challenging operating environment"* for local businesses, and a macro story of that kind would "just never enter into
the discussion" **[M2000-094]**; what matters is the structural question underneath it. The analyst's habits apply most
here, since a trailing owner-cash yield of nearly 18% is the kind of number that makes an analyst want to understand a business:
"I’m looking for what’s wrong in things" **[M2025-013]**, and the reading is aimed "to possibly reject your original
hypothesis" **[M1998-144]**. **Contrary evidence, written down as found** **[M1997-127]**:
1. Against TOO HARD (found first, written first): Yelp has lived twenty years with Google as both its main traffic
   source and its main competitor and has doubled revenue in ten years ($716M to $1,465M, 8.3% a year) while desktop
   traffic fell about 40%; its 330 million reviews are now licensed to OpenAI and Apple Maps (10-Q Q2 2026: *"Yelp ratings
   and reviews recently began powering ChatGPT’s local experience"*), and other revenue nearly doubled. That is a
   business adapting, not one being erased.
2. Against TOO HARD again: the speakers count the miss of a business they could see as an error, "What’s an error is
   when it’s something we understand, and we stand there and stare at it, and we don’t do anything." **[M2001-006]**, and
   they count Google itself as such a miss, seen through the cost per click at GEICO: "we were paying $10 a click"
   **[M2019-024]**. A reflexive "tech, too hard" is not free if the business is in fact inside the circle.
3. Against the business, found during Q1: advertising revenue fell 3% in the first half of 2026; paying advertising
   locations are below 2019; ad clicks fell 7% in 2025 and 8% in the first half of 2026; the filer itself says AI answers
   in Google *"may be having a negative impact on our traffic"*. Recorded at Q1 below.

## THE STANDING RULE
Owning Yelp would not put the buyer at risk of ruin provided it is bought without borrowed money and sized so that a total
loss is bearable: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "We are never going to risk
what we have and need for what we don’t have and don’t need." **[M2012-081]**. No purchase is reached in any case.

---
## Q1. CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years", with "some notion of how the industry will develop and where the company
will stand within the industry" **[M2012-065]**; the definition is having "a reasonable probability of being able to
asses where the business will be in 10 years" **[M2000-037]**. Knowing the product is not enough: "We just don’t know the
economics of it 10 years from now." **[M2000-104]**. The first step is "trying to identify the key variables in that
particular business, and evaluating how predictable they were first" **[M1998-044]**.

**The key variables, from the filing.** Yelp's 10-K states them itself: revenue is ad clicks times price per click; ad
clicks come from consumer traffic; price per click comes from the number of advertisers and their budgets (10-K FY2025,
Key Metrics). So two variables decide the ten-year economics:

1. **Monetizable consumer traffic, and who controls it.** The filer: *"We rely heavily on Internet search engines,
   including primarily Google, to drive traffic to our platform"*; *"Google in particular is the most significant source
   of traffic to our website"*; and, in the competition section, *"online search engines and directories, including
   those incorporating AI technologies, such as our primary competitor, Google"* (10-K FY2025, Items 1 and 1A). The source
   of the traffic and the primary competitor are the same company. On AI: *"search engines such as Google have
   incorporated AI-generated responses to search queries above their organic search results, which has reduced the
   prominence of links to our platform and may be having a negative impact on our traffic"*, and the risk that consumers
   use *"Google’s AI Overviews and AI Mode, AI chatbots or other AI platforms instead of traditional search engines, as
   these tools often present their results in a format that de-emphasizes links to our platform"* (same). The FY2024 10-K
   adds that app traffic *"continued to be negatively impacted by the reduced volume of app downloads driven by Apple
   Maps"*. The traffic series, from the 10-Ks (monthly averages, thousands of unique visitors or devices; the method
   changed twice, so only like is set against like):

| stream | 2019 | 2020 | 2021 | 2022 | 2023 | 2023 (new method) | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| desktop web | 60,252 | 43,685 | 45,990 | 38,046 | 36,301 | 39,959 | 39,627 | 37,399 |
| mobile web | 73,722 | 52,794 | 56,668 | 59,172 | 60,282 | 62,013 | 63,987 | 59,729 |
| app | 36,250 | 31,132 | 33,085 | 33,026 | 31,909 | 29,842 | 28,595 | 28,009 |

   (2019 to 2023 by Google Analytics and the historical app method, annual averages, from the FY2021, FY2022 and FY2023
   10-Ks; 2023 new method to 2025 by internal measurement with a minimum-engagement screen, from the FY2024 and FY2025
   10-Ks; FY2025 restated 2024 desktop from 40,341.) On the old basis desktop fell 40% from 2019 to 2023 and app 12%; on
   the new basis every stream fell from 2024 to 2025. The filer: traffic *"has remained below our pre-pandemic 2019 traffic
   levels"* and *"we expect traffic to remain challenged in 2026"*.
2. **Advertiser demand.** Paying advertising locations (fourth-quarter averages, thousands): 478 (2017), 541 (2018), 565
   (2019), 520 (2020), 528 (2021), 545 (2022), 544 (2023), 521 (2024), 496 (2025); 510 in Q2 2026 against 515 a year
   before. Services 235 (2019) to 250 (2025); Restaurants, Retail & Other 330 (2019) to 246 (2025). Ad clicks: -7% in
   2025, -8% in the first half of 2026; average price per click +10% in 2025, +4% in the first half of 2026. Advertising
   revenue was 95% of revenue in 2025; Services $947.6M (+8%), RR&O $443.7M (-6%); in the first half of 2026 Services +1%,
   RR&O -10%, advertising -3%, other revenue +87% (Hatch and data licensing). The 2020 COVID year: revenue fell from
   $1,014M to $873M, RR&O advertising revenue fell 31%, Q2 2020 ad clicks -51%, paying locations 378 thousand in Q2 2020
   against 549 thousand a year before (10-K FY2020 quarterly tables).

**Are the key variables predictable?** The second one, advertiser demand, is the kind of thing a reader can follow:
small local businesses buying clicks, with a record. The first one is not. Whether a consumer looking for a plumber or a
restaurant in 2036 types into Google, asks Google's AI Mode, asks ChatGPT, opens Apple Maps, or opens Yelp, and whether
the interface they use sends the click (and so the advertiser's budget) to Yelp, is a forecast about the product decisions
of Alphabet, OpenAI and Apple. The filer's own management is rebuilding the company around that uncertainty: the 2026 plan
is to *"Reconceive Yelp around actions and answers"* and *"Extend our reach to power local discovery across the AI
ecosystem"*, with Yelp's content licensed to the AI assistants that may replace the visit (10-K FY2025, Item 1; 10-Q Q2
2026). The company's answer to the threat is to feed the threat its content for a fee; whether that fee replaces the
click is not knowable from any filing.

**The tests, one by one.**
- *Where will it be in ten years?* "You’re trying to print the next 10 years of Value Line in your head." **[M1999-132]**.
  I cannot print traffic, ad clicks or the mix of advertising and licensing revenue for 2036 within any range I would
  defend. An analyst in 2016 could not have printed 2026 either: the shift of the business to Services, the COVID drop,
  desktop traffic down by roughly half since 2014 on the filer's successive measures, and AI answers in search were none of them in the 2016 10-K's picture.
- *Do the past statements tell me the future ones?* "the financial statements will tell me the information that’s useful
  to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**. No:
  the decade of statements records revenue growing while traffic fell, which was paid for by raising the price per click
  and moving to Services. Whether that can go on is exactly what the past figures cannot show; the filer warns that
  higher prices with fewer clicks are expected to hurt retention unless the clicks perform better (10-K FY2025, Key
  Metrics).
- *Is it important and knowable?* "If something’s important but unknowable, forget it." **[M2006-076]**. The deciding
  variable is the most important one in the business and is unknowable from here.
- *Would the insiders write it down?* The rows' test: insiders "would not want to put down on paper their predictions"
  about tech companies' economics ten years out **[M2000-105]**. Yelp: *"We compete in rapidly evolving and intensely
  competitive markets, and we expect competition to intensify further in the future with the emergence of new
  technologies, such as AI"*, *"the use of, as well as consumer expectations for, such technologies are rapidly
  evolving"*, and on the Google lawsuit *"We are unable to predict the ultimate outcome of this case"* (10-K FY2025; 10-Q
  Q2 2026). Alphabet, the other side: *"AI technology and services are highly competitive, rapidly evolving, and require
  significant investment"* (10-K FY2025, `0001652044-26-000018`). Tripadvisor, a review site in the same position:
  its Hotels and Other segment will be hurt by *"AI overviews displacing top-ranked links, reduced click-through rates and a shift
  towards platform based non-traditional search"* (10-K FY2025, `0001193125-26-051281`). None of the three writes the
  forecast down.
- *Can I name the winner, not just the industry?* Local discovery will keep growing as a use of the internet, but "we
  don’t have the faintest idea who the winners will be" **[M2012-067]**, and seeing the industry "does not mean we can
  judge what its profit margins and returns on capital will be as a host of competitors battle for supremacy"
  **[L2009-005]**.
- *Is the forecast about customers or about technology?* The rows allow a consumer business to be read through
  "consumer behavior and threats to a business" **[M2023-030]** and "laying out what their prospective customers will do
  in the future" **[M2017-019]**. Yelp's consumers' habits might be forecast; the channel that delivers them to Yelp is a
  technology owned by others and is changing now. The pull is recorded; it does not rescue the forecast, because the
  revenue arrives only through the channel.
- *Is there a technological component of significance?* Yes: "where we think the future technology could hurt the
  business as it presently exists", "it won’t make it through the filter" **[M1998-008]**; "a business that must deal
  with fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics"
  **[L1993-023]**; "We view change as more of a threat into the investment process than an opportunity." and "whenever we
  look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**.
- *How far off could I be?* The rows keep "how far off we can be" **[M2011-084]** in view. Here the range of outcomes runs
  from Yelp as the licensed local-content layer of every AI assistant, earning more than today, to Yelp as a directory
  whose clicks were absorbed by the answer box, the case the rows narrate for newspapers: "that virtuous cycle is going in
  the other direction now" **[M2006-060]**, and "the advertiser just does not need you the same way as they needed you 10
  or 15 years ago. So your ability to price evaporates in them." **[M2010-053]**. The World Book was not worth less; it
  was beaten by people "who can go on the internet and get an awful lot of that information free" **[M2007-134]**. The
  Yelp review in an AI answer is the same information, free, without the visit.
- *Do I doubt it is inside?* I do. "if you have doubts about something being into your circle of competence, it isn’t"
  **[M2002-092]**.

**Answering the contrary evidence.** Item 1 (twenty years of survival, revenue doubling) is real and is written down
above. It shows management has adapted so far; it does not show the next ten years, and the rows warn that "slow change
can be much harder to perceive, and can lull you to sleep easier" **[M2014-038]**: the traffic decline since 2019 has
been gradual and was covered by price increases. Item 2 (the Google miss) cuts the other way on inspection: the speakers
regret missing the toll-taker, Google, whose economics they saw in their own advertising bills **[M2019-024]**; Yelp is
on the other side of that toll, a site that depends on the toll-taker for traffic and competes with it for the same
advertiser. The error the rows count is staring at something "we understand" **[M2001-006]**; this is not that. And
outside the circle, "there is no penalty in investing if you don’t swing at a ball that’s in the strike zone"
**[M2018-087]**.

**Routing.** A business whose ten-year economics cannot be foreseen because its industry changes fast closes here,
"too hard" among the "three boxes at the company: in, out, and too hard" **[M2006-013]**, not OUT on the business: "It
doesn’t mean it isn’t a good buy." and "It just means that we don’t know how to evaluate it." **[M2000-038]**. The
evidence of erosion recorded above (traffic, locations, clicks, RR&O revenue) would be weighed at Q2 if Q1 had passed;
it is not used here to close OUT, because Q2 is reached only by a business Q1 has passed (framework, Q1, The routing,
fixed).

**Which cause: WORK or NATURE.** NATURE. The deciding question (how local discovery will be routed among Google's AI
answers, chat assistants, maps and Yelp over ten years, and what Yelp is paid in each case) is a forecast the industry's
own insiders do not write down **[M2000-105]**: Yelp, Alphabet and Tripadvisor each call the field rapidly evolving in
their 2025 10-Ks, and Yelp says it cannot predict even its own lawsuit against Google, set for trial in September 2028.
It is the roadblock "the nature of the industry would be" **[L1993-023]**, not the reader's want of work: "I haven’t
done the work and I’m not sure if I did the work I would understand them." **[M1994-026]** describes the other cause, and
here more reading of Yelp's filings would not reveal Alphabet's and OpenAI's product plans, a problem "which we can't
solve by studying up" **[L1999-018]**. "if we can’t make a decision in five minutes, we can’t make it in five months"
**[M2008-086]**. A lower price does not reopen the box **[M2000-038]**.

**VERDICT: TOO HARD (NATURE).** The ten-year economics turn on traffic that Google, Yelp's primary competitor and largest
traffic source, increasingly answers itself, and on AI interfaces whose economics no insider writes down. The file closes
here. No research pass is opened (a NATURE close takes none, framework section I).

---
## Q2. WHY IS THE CASTLE STILL STANDING? STOP. **NOT REACHED** (closed at Q1).
The competitor figures gathered for this question are recorded below the box as evidence only, not as a Q2 verdict.

## Q3. HOW MUCH CAPITAL MUST GO IN? WEIGHING. **NOT REACHED.**

## Q4. DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion. **NOT REACHED.** (The balance sheets were read in Step 0.)

## Q5. WHO RUNS IT? STOP on integrity. **NOT REACHED.**

## Q6. WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING. **NOT REACHED.** (Buyback facts recorded below as evidence only.)

## Q7. WHAT IS IT WORTH? STOP. **NOT REACHED.** (The owner's reporting request is answered below, labelled COMPUTATION.)

## Q8. IS IT BETTER THAN THE ALTERNATIVES? STOP. **NOT REACHED.**

## Q9. COULD IT RUIN US? WEIGHING. **NOT REACHED.**

## Q10. IS IT THE FAT PITCH? WEIGHING. **NOT REACHED.**

## Q12 (optional). WOULD WE BE PROUD OF HOW THE MONEY IS MADE? **NOT ASKED.**

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** Yelp's ten-year economics depend on how much local-search traffic reaches it through
Google (its primary competitor and largest traffic source) and the AI answer engines now replacing the link; no insider
writes that forecast down. For the owner's reporting request, the computation below puts a range of $27.57 to $43.16 a
share (five-year window; $17.70 to $27.73 whole cycle) beside a price of $18.52: COMPUTATION, not a clearance.

---
## EVIDENCE RECORDED BEYOND THE CLOSE (record only; not a Q2, Q6 or Q9 verdict)

**The competitor row, from the competitors' own filings** (XBRL company facts, first-filed annual values, USD millions;
operating margin = GAAP operating income over revenue):

| company | revenue start of span | revenue 2025 | op. margin start | op. margin 2025 | own words on search and AI (2025 10-K) | accession |
|---|---|---|---|---|---|---|
| Yelp | 716.1 (2016) | 1,465.0 | -0.3% (2016) | 12.6% | Google is *"our primary competitor"* and the largest traffic source | `0001345016-26-000019` |
| Angi | 498.9 (2016); peak 1,764.4 (2022) | 1,030.5 | 4.8% (2016) | 6.3% | network service requests -58%, network leads -74%, active pros -19% in 2025; reliant on *"paid and free search engine marketing"* | `0001705110-26-000011` |
| Tripadvisor | 1,480.0 (2016) | 1,891.0 | 11.2% (2016) | 4.2% | *"AI overviews displacing top-ranked links, reduced click-through rates"* | `0001193125-26-051281` |
| Alphabet (Google local) | not broken out | Google Search & other $224,532M (2025), $198,084M (2024), $175,033M (2023) | n/a | n/a | *"AI Overviews makes it easier to ask Google anything"*; AI Mode answers questions *"that might have previously taken multiple searches"* | `0001652044-26-000018` |
| Thumbtack | private; no filings; **not obtainable, flagged** | | | | | |

Over the span, Yelp's margin rose while Tripadvisor's fell from 27% (2014: $340M on $1,246M) to 4% and Angi's revenue fell
42% from its 2022 peak; Angi's own 2025 table puts the loss in network revenue (-72%, $373.1M to $103.5M) and advertising
revenue (-31%), while its proprietary revenue rose 17%. More than half of Yelp's margin gain since 2021 (3.1% to 12.6%)
came from stock pay falling from 14.7% to 9.1% of revenue with headcount held flat, not from traffic. The one competitor that gains from every one of these trends files no local
figures: Alphabet.

**Stock pay, buybacks and shares** (record only, Q6 NOT REACHED): repurchases $1,910.1M in 2017 to 2025 plus $456.7M of
taxes paid on net share settlement, against operating cash less capex of $1,864.8M over 2016 to 2025; diluted weighted
shares 88.7M (2018) to 65.1M (2025); cover count 54.3M (2026-07-31). In the first half of 2026 the company bought
7,097,439 shares for $175.1M (Q2 average prices $27.12, $22.72, $23.18 by month) while drawing $165.0M on its revolver and
repaying $65.0M, and bought $25.0M more in July. The repurchase program names no price. The stated plan is stock pay
below 6% of revenue by the end of 2027 (10-K FY2025; DEF 14A). Set against the computation below, the 2026 prices paid sit
inside the five-year range or near its bottom, not "below its intrinsic value, conservatively-calculated" by a clear
margin **[L1999-023]**; recorded, not weighed.

---
## COMPUTATION — NOT A CLEARANCE
*(The file closed at Q1 TOO HARD (NATURE). Nothing here is entry language, a Q7 verdict or a reason to reopen the box. A
range for a business I cannot see ten years into is exactly the range the rows say usually tells nothing: "Usually, the
range must be so wide that no useful conclusion can be reached." **[L2000-025]**; and "we don’t really try to compensate
for that sort of thing by having some extra large margin of safety" **[M2007-022]**. Arithmetic in `compute.py`.)*

**(a) VALUE RANGE, by the Q7 convention.** Cash input: owner cash after every real cost, "a figure calculated after
interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**, with stock pay deducted in
full since it "is the most egregious example" of a real cost owners are told to ignore **[L2015-003]**, and all capital
spending deducted, capitalized software included ("With software, for example, amortization charges are very real
expenses." **[L2012-003]**). Five-year mean 2021 to 2025: **$84.6M** (D&A variant $72.5M). Rate: the long government bond,
"(which we consider to be the yield on long-term U.S. bonds)" **[L2000-021]**, 5.63%. Ten years, then zero nominal growth.
- Growth shown: on aggregate owner cash, 2021 to 2025 is 55% a year from a $32.7M base, "a breathtaking, but meaningless,
  growth rate" **[L2005-003]**; revenue grew 9.2% a year. Both exceed the discount rate, so the shown-growth end is capped
  at 5.63% by the convention's cap. Current evidence runs against even that: the 2026 outlook is revenue of $1.460B to
  $1.470B against $1.465B in 2025, adjusted EBITDA guided down, and Q3 2026 revenue expected to fall slightly (10-Q Q2 2026;
  Exhibit 99.1).
- **Five-year window:** no-growth end $1,502M, less net debt $5.9M, **$27.57 a share**; shown-growth end (capped)
  $2,348M, **$43.16 a share**. Width 1.56 to 1, inside the convention's three-to-one.
- **Whole-cycle variant** (the window holds abnormal years: 2022 depressed and 2025 lifted by the R&D tax rule; and it
  carries interest income, $19.6M in 2023, $20.9M in 2024, $13.8M in 2025, on cash since spent on buybacks and Hatch):
  ten-year mean 2016 to 2025, **$54.4M**, which includes the 2020 COVID year: **$17.70 to $27.73 a share**.
- D&A variant (five-year): $23.62 to $36.97.
- Against the price: $18.52 is 33% below the bottom of the five-year range and 5% above the bottom of the whole-cycle range.
  The two windows together span $17.70 to $43.16, 2.4 to 1. Had Q7 been reached, a price at the bottom of one honest window
  and inside the other is not a case that would "scream at you" **[M2009-005]**.

**(b) FAIR PRICE: $18.78 a share.** Rule (owner's request; a CONVENTION of this run): the price at which the central case
returns the floor of about 10% a year, the speakers' "real expectancy is below 10 percent" line, which they call
"arbitrary" **[M2003-149]**. Central case: the five-year mean owner cash, $84.6M, growing at half the capped rate (2.8%)
for ten years, then flat; solved as the price whose internal rate of return is 10%: enterprise value $1,025M, less net
debt, $18.78. **Tax treatment:** owner cash is after Yelp's own corporate income tax (cash taxes paid) and after all stock
pay, and before any tax on the holder; the 10% floor is applied to it as the holder's pre-tax return, with no gross-up for
corporate tax (Yelp's 2025 book tax rate was 28.6%, $58.4M on $204.0M pre-tax; grossing up would raise the fair price and
was not done). Variants: the same cash with no growth, $15.48; at today's $18.52 the central case returns about 10.1% a
year, the five-year no-growth case 8.4%, the whole-cycle no-growth case 5.4%, the trailing-twelve-month no-growth case
17.8% (that last on a tax-lifted year).

**(c) CHEAP PRICE: $9.92 a share.** Rule (a CONVENTION of this run): the price at which the worst case shown, the ten-year
whole-cycle mean owner cash with no growth at all, still returns the 10% floor ($544M); below it the floor clears in every
case computed and no pencil is needed, "it’s too close to think about" **[M1996-084]** applying above it. The price is
$18.52, 1.9 times the cheap price.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Not** written question by question with a commit after each: the file
      was written in one pass after the reading, and nothing was committed, because the dispatch forbids commits and edits
      outside this file and the working folder. For the same reason the overnight lock was not written.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, see below); every filing fact carries its
      accession; every number is from a filing, a row, or `compute.py`, and the fair and cheap rules are confessed as
      conventions of this run.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance, and the computation carries the protocol's label.
- [x] Owner cash after every real cost (all stock pay, all capex), never a net-income proxy; the sovereign from the US
      Treasury; the price quote flagged as an aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, the strongest case against TOO HARD first.
- [x] No row dated after the anchor is cited (not a point-in-time run; today's date is the anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS after writing; `verify_ids.py` in the working folder PASS (no E-ids; 49 distinct
      v5 ids all in the ledger; 57 quoted fragments each found in the row cited beside it; no stray long dashes).
- [ ] Not done: the Exhibit 99.2 shareholder letters (image files); Thumbtack (private); Google's local revenue (not
      disclosed); a paying-location series before 2017 on the same definition (earlier 10-Ks report paying accounts).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 TOO HARD against Q2 OUT.** Yelp carries both a forecast nobody can make (AI routing of local search) and evidence
on the record that the castle is already being entered (traffic below 2019 on every stream, paying locations and clicks
falling, RR&O revenue down 10%). The routing sends the file to Q1 TOO HARD, so the erosion evidence is never weighed, and
a reader of the box alone learns "we don't know how to evaluate it" **[M2000-038]** when the filings say rather more. I
followed the routing and recorded the evidence below the box; the framework might say whether a Q1 TOO HARD (NATURE) may
carry a note that the Q2 evidence leans OUT. (2) **Test 7 of Q1, customers or technology,** does not cover a consumer
business whose access to its customers is owned by a technology platform that competes with it. The rows on Apple and
consumer behaviour **[M2017-019]**, **[M2023-030]** read as permission; the channel decided it here. (3) **The Q7
convention's "growth shown on aggregate owner cash"** gives 55% a year when the first year of the window is near zero;
the convention caps it at the discount rate but does not say whether a meaningless shown rate should be replaced by
another measure (revenue) or by zero. I used the cap and showed the no-growth end. (4) **Fair and cheap prices** are not
in the framework; both rules here are this run's, at the owner's request, and the tax treatment of the ~10% pre-tax floor
for a minority holder (gross up for corporate tax or not) is not stated in the convention. (5) **The template's position
note** tells the analyst to check `PORTFOLIO.md`, which the dispatch's blind rule forbids; the blind rule was followed.
