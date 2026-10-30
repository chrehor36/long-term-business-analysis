# Company Run, Garmin Ltd. (NYSE: GRMN), 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md`. Working folder `Test Runs/_research 2026-10-07 GRMN/`
(segment table `segments.csv`, annual figures `facts_annual.csv`, arithmetic `q7.py`; raw filings under `cache/`, ignored).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Contamination, declared at the start.** Before any fetch I saw, without opening them: the session's starting git status
(research-folder names of other runs: AYI, BDC, CHD, ARCB and others, none about Garmin); the last five commit subjects
(ESI, CTAS, ECL, EFX, EPAC, all other companies); the memory index lines carried in the session context (wave counts,
"57 gate-clearers, nothing buyable", five holding reviews owed, unnamed). Nothing in them names Garmin or a verdict on it.
The brief itself says earlier Garmin run files exist; I did not open, list or search them, and I did not list `Test Runs/`.
None of this is used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $276.05 (2026-10-07, printed by `tools/run.py` from an aggregator; live quote only, flagged under operator rule 5).
- **Shares by class** (one class, registered shares, par CHF/USD 0.10): **192,852,536** outstanding as of 2026-07-24,
  cover of the 10-Q for the quarter ended 2026-06-27 (filed 2026-07-29, accession `0001193125-26-322114`;
  `python Screens/cover_shares.py GRMN` returns the same count). Check against issued less treasury: the same 10-Q's
  balance sheet shows 194,901 thousand issued and 192,910 thousand outstanding at 2026-06-27; the cover count is
  58 thousand lower, consistent with repurchases in July. No 8-K or prospectus after the 10-Q changes the count (8-Ks
  filed 2026-07-29 and earlier only; submissions index read).
- **Market cap:** 192.853M x $276.05 = **$53,237M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-06 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (fiscal year ended 2025-12-27), filed 2026-02-18, accession
  `0001193125-26-056028`; 10-Q for the quarter ended 2026-06-27, filed 2026-07-29, `0001193125-26-322114`; proxy
  DEF 14A filed 2026-04-22, `0001308179-26-000318`; 10-K/A for FY2023 filed 2024-11-29, `0000950170-24-131914`; and for
  the span the 10-Ks for FY2007 `0001144204-08-011821`, FY2008 `0001144204-09-010751`, FY2010 `0001144204-11-010358`,
  FY2013 `0001144204-14-010483`, FY2016 `0001615774-17-000765`, FY2019 `0001564590-20-005133`, FY2022
  `0000950170-23-003566`, FY2023 `0000950170-24-017559`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025,
  **$1,633,359 thousand** in the filed Consolidated Statements of Cash Flows (10-K FY2025, `0001193125-26-056028`);
  `tools/run.py` prints 1,633 (USD millions). Agrees.
- `python tools/run.py GRMN --framework v5`, arithmetic lines only (USD millions): OCF 1,376 / 1,432 / 1,633 for
  FY2023 / 2024 / 2025; SBC 101 / 137 / 166; capex 194 / 194 / 270; D&A 163 / 171 / 185; OCF less SBC less capex
  1,081 / 1,102 / 1,197, three-year mean 1,127; the five-year window on the same basis 892. No securities flows inside
  operating cash, no other stock-pay line, no intangible or software payment beside capex (calculation linkbase,
  as printed). Everything else it printed (yields, "growth the price assumes", points over the sovereign) is not used.
  These are not yet owner cash: acquisitions and the equity-award share withholding are not in them (Q4).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the first: a share is a business, so the test is whether I "would be happy
buying this stock if the market closed for five years" **[M1997-109]**, which for a maker of consumer devices with a
two-year product cycle turns on whether I can say what the business will look like when the market reopens. The market's
quotation tells me nothing about that; "It just tells us prices." **[M2006-077]**. No macro view enters, so the
tariff and Taiwan questions are read only as properties of this business, not as forecasts **[M2000-094]**. The analyst's
habit applies to me: I am "looking for what’s wrong in things because that’s part of investing" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**:
- (against my first hypothesis that the deciding parts are a fast-changing technology) the outdoor and fitness parts
  have grown operating profit through the whole Apple Watch era: outdoor $156M (2014) to $690M (2025), fitness
  $191M (2014) to $726M (2025), at operating margins of 34% and 31% in 2025 (segments.csv; 10-K FY2016
  `0001615774-17-000765`, 10-K FY2025 `0001193125-26-056028`). Eleven years against the largest technology companies is
  a record, not a forecast, but it is real evidence of a standing castle.
- the company has no borrowings, $4,370M of cash and securities at 2026-06-27 (10-Q `0001193125-26-322114`), and came
  through the collapse of its former main business without debt.
- (against the business) the fitness part's operating profit fell 71% in one year, $359M (2021) to $105M (2022)
  (10-K FY2023 `0000950170-24-017559`); the auto part, 67% of company operating profit in 2007 ($609M of $907M), earned
  $102M in 2016 and its OEM successor has lost money every year since 2020 (segments.csv).

## THE STANDING RULE
Owning a part-interest in Garmin bought for cash, without borrowed money, puts the buyer at no risk of ruin from the
buyer's own conduct; the rule binds the financing and size of the purchase, "borrowed money has no place in the
investor's tool kit" **[L2014-005]**, and "We are never going to risk what we have and need for what we don’t have and
don’t need." **[M2012-081]**. Nothing about the target changes that; its own exposures are Q9's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**; "we have a reasonable probability of being able to asses where the business
will be in 10 years" **[M2000-037]**. Knowing the product is not enough: "Oh, we understand the product. [...] We just
don’t know the economics of it 10 years from now." **[M2000-104]**.

**Which part decides (Q1's holding-company paragraph as extended 2026-10-06 to operating segments; Q2's parts
CONVENTION).** Five-year operating profit FY2021 to FY2025, on the current segment basis (consumer auto inside outdoor;
FY2021 and FY2022 as recast in the 10-K FY2023 `0000950170-24-017559`, FY2023 to FY2025 from the 10-K FY2025
`0001193125-26-056028`), USD millions:

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share |
|---|---|---|---|---|---|---|---|
| Outdoor | 524.5 | 573.3 | 515.3 | 702.7 | 690.4 | 3,006.1 | 44.2% |
| Fitness | 359.2 | 104.7 | 232.2 | 482.7 | 725.9 | 1,904.7 | 28.0% |
| Marine | 249.8 | 215.3 | 179.4 | 236.0 | 251.3 | 1,131.8 | 16.6% |
| Aviation | 193.2 | 213.2 | 226.4 | 211.4 | 257.2 | 1,101.4 | 16.2% |
| Auto OEM | (108.0) | (78.7) | (61.1) | (38.8) | (48.6) | (335.2) | (4.9%) |
| total | 1,218.6 | 1,027.8 | 1,092.2 | 1,594.0 | 1,876.1 | 6,808.7 | |

No part carries more than half, so **the largest part, Outdoor, decides**. Outdoor's revenue is led by adventure
watches (fēnix, Instinct, tactix, Enduro, MARQ), with inReach satellite communicators, handhelds, golf devices,
consumer automotive navigators and dash cams, and dive computers (10-K FY2025, Item 1); its 2025 growth was "primarily
due to sales growth in adventure watches" (MD&A). Fitness, the second part, sells the same kind of product (running
watches, smartwatches, cycling computers) from the same factories and the same Garmin Connect platform; the two together
are 72% of five-year operating profit. The question is therefore whether the ten-year economics of a GPS wearable and
handheld maker can be foreseen.

**Key variables and how predictable they are** **[M1998-044]**. (1) Whether the dedicated sport and adventure watch
remains a category the customer buys separately, or is absorbed into the general smartwatch and phone, as the portable
car navigator was. (2) Garmin's share and price inside that category against Apple, Samsung, Google, Huawei, Xiaomi,
Coros, Polar, Suunto and others the filer names (10-K FY2025, Competition). (3) Whether satellite messaging stays a
separate device (inReach) or moves into the phone. (4) The cost of staying current: R&D of $1,126M in FY2025, 15.5% of
sales (facts_annual.csv), the largest operating expense line. None of the four is a variable whose ten-year value I can
state; each turns on product contests decided every one to two years.

**The filer's own words on its industry.** "A significant portion of our revenue has been, and we expect in the future
will continue to be, derived from sales of newly introduced products. The market for our products is characterized by
rapidly changing technology, evolving industry standards and regulations and changes in customer needs. If we fail to
introduce new products, or to modify or improve our existing products, [...] our products could rapidly become less
competitive or obsolete." and "Some of our competitors have significantly greater financial, technical and marketing
resources than we do. [...] existing and emerging competitors have been able to replicate certain features offered by
some of our products" (10-K FY2025, Item 1A, `0001193125-26-056028`). That is "a business that must deal with
fast-moving technology", which "is not going to lend itself to reliable evaluations of its long-term economics."
**[L1993-023]**, and a business "quite dependent on the technology continuing to gallop" **[M1999-075]**.

**The test of the past (test 3, "do I understand enough about this business so that the financial statements will tell
me [...] what the future financial statements are going to look like" **[M2008-033]**).** Garmin's own record says the
statements did not. In 2007 the automotive/mobile part earned $608.8M of $907.4M company operating income, on $2,342M of
sales (10-K FY2007 `0001144204-08-011821`). The 10-K for FY2008, filed 2009-02-25 (`0001144204-09-010751`), said of
phone navigation only that "The acceptance of this technology by consumers could slow our growth and further reduce
margins." The part's operating income then ran $524M (2008), $460M (2009), $246M (2010), $161M (2011), $102M (2016)
(10-Ks FY2010, FY2013, FY2016), and by the FY2016 10-K the filer wrote that the PND market "is declining as competing
technologies emerged and market saturation occurred". The insiders wrote the risk down and did not write down its
size; the speakers' test is exactly whether they would put "their predictions about where 10 companies you would choose
in the tech field would be in 10 years, in terms of their economics" on paper, and "They would say, “That’s too hard.”"
**[M2000-105]**. The fitness part's 71% one-year fall in operating profit (2021 to 2022) shows the same volatility in
the second part, in a year the filer explains only as "Fitness revenue decreased due to declines across all product
categories" (10-K FY2022 `0000950170-23-003566`, MD&A); fitness gross margin fell from 53% to 50% the same year.

**Customers or technology (test 7).** The strongest case for IN is the Apple row: a device "with all kinds of tech built
into it" can be "much more of a consumer products business", where the forecast is "what their prospective customers
will do in the future" **[M2017-019]**, and "we know what we think we can project out in terms of consumer behavior and
threats to a business" **[M2023-030]**. Garmin's athletes keep years of training data in Garmin Connect and buy by
brand; the record since 2014 is above. But the row's own speaker adds "That doesn’t mean it’s correct", and Apple's
case rested on a customer who would give up a second car before the phone; Garmin's customer is a buyer of the
second device, the one the phone absorbs when it can, which is what happened to the PND. Whether the dedicated watch
survives the general one is a technology contest against firms with "significantly greater financial, technical and
marketing resources" (the filer, above), not a habit I can project. I cannot name the winner, only the industry
**[M2012-067]**: "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can
judge what its profit margins and returns on capital will be as a host of competitors battle for supremacy."
**[L2009-005]**.

**How far off could I be (test 8).** Very far, by the company's own two precedents in twenty years: the main part's
operating profit fell by more than four-fifths in nine years after 2007, and the current second part fell 71% in one
year. "there’s some things we can be way off on" **[M2011-084]**; this is one.

**The doubt rule.** I have doubts that the deciding part is inside the circle, and "if you have doubts about something
being into your circle of competence, it isn’t." **[M2002-092]**. Change here is the threat the rows name: "whenever we
look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass on that." **[M1999-063]**;
"if something comes in where there’s a technological component that’s of significance, or where we think the future
technology could hurt the business as it presently exists [...] it won’t make it through the filter." **[M1998-008]**.

**What does not decide.** Aviation (16% of five-year operating profit) is a certified-avionics business I could read:
operating margins of 24% to 42% in every year 2005 to 2025 (segments.csv) and FAA certification of every product for
type-certificated aircraft (10-K FY2008, Item 1A). Marine (17%) has held 20% to 29% since 2019. Neither carries the
file; by the parts convention, a part that matters and cannot be understood keeps the whole outside **[M2002-092]**.

**Cause.** NATURE, not WORK. The deciding question (will the dedicated GPS wearable and satellite communicator earn
today's margins in ten years against the phone and the general smartwatch) is not answered by any filing not yet read;
the filer itself says its product schedules "are difficult to predict" and its "operating results are difficult to
predict" (10-K FY2025, Item 1A), and its own 2009 filing did not foresee the size of the PND collapse. "We couldn't solve
this problem, moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**;
"Our problem -- which we can't solve by studying up -- is that we have no insights into which participants in the tech
field possess a truly durable competitive advantage." **[L1999-018]**; "if we can’t make a decision in five minutes, we
can’t make it in five months." **[M2008-086]**.

**VERDICT: TOO HARD (NATURE).** The deciding part (outdoor, with fitness beside it) is a consumer-electronics wearable
business whose ten-year economics turn on a fast-moving technology contest, on the filer's own description and on its
own history of the PND collapse. "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction
of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**; the box is "too hard" **[M2006-013]**,
and a lower price does not reopen it. The file closes here; Q2 to Q12 are NOT REACHED. Facts already found are below,
under AFTER THE STOP, and every figure after this line is COMPUTATION, NOT A CLEARANCE.

## Q2: WHY IS THE CASTLE STILL STANDING? NOT REACHED (closed at Q1). Facts are under AFTER THE STOP.
## Q3: HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED. The balance sheets were read in Step 0's place (below), as the template asks when the file closes before Q4.
## Q5: WHO RUNS IT? NOT REACHED. Integrity facts recorded, not judged, under AFTER THE STOP.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7: WHAT IS IT WORTH? NOT REACHED. COMPUTATION, NOT A CLEARANCE, under AFTER THE STOP.
## Q8: BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9: COULD IT RUIN US? NOT REACHED.
## Q10: THE FAT PITCH? NOT REACHED.
## Q12: WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** The deciding part (outdoor, with fitness beside it) is a GPS wearable and handheld
business in an industry the filer itself calls "characterized by rapidly changing technology", and the company's former
main part, the PND, lost more than four-fifths of its operating profit within nine years of 2007. No range is a verdict;
the COMPUTATION below puts the price of $276.05 above the top of a computed range of $91.75 to $211.57 a share.
Integrity facts recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box is unchanged (operator rule 2). Each with its source **[M1997-127]**.)*

### The balance sheets, ten year-ends (read in Step 0's place; template Q4 line; "balance sheets over an 8 or 10 year period" **[M2025-032]**)
USD millions, first-filed XBRL (`tools/run.py` table and SEC companyfacts, transcription; FY2025 checked against the
prior-period column of the filed balance sheet in the 10-Q of 2026-06-27, `0001193125-26-322114`):

| year-end | sales | cash | securities | inventory | inv/sales | receivables | rec/sales | goodwill | equity | borrowings |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,019 | 847 | 1,480 | 485 | 16.1% | 527 | 17.5% | 225 | 3,418 | none |
| 2019 | 3,758 | 1,028 | 1,582 | 753 | 20.0% | 707 | 18.8% | 467 | 4,793 | none |
| 2021 | 4,983 | 1,498 | 1,617 | 1,228 | 24.6% | 843 | 16.9% | 575 | 6,114 | none |
| 2022 | 4,860 | 1,279 | 1,382 | 1,515 | 31.2% | 657 | 13.5% | 568 | 6,204 | none |
| 2023 | 5,228 | 1,693 | 1,400 | 1,346 | 25.7% | 815 | 15.6% | 608 | 7,012 | none |
| 2024 | 6,297 | 2,080 | 1,620 | 1,474 | 23.4% | 983 | 15.6% | 604 | 7,848 | none |
| 2025 | 7,246 | 2,279 | 1,856 | 1,772 | 24.5% | 1,253 | 17.3% | 760 | 8,973 | none |
| 2026-06-27 | (H1 3,776) | 2,334 | 2,036 | 1,966 | | 1,153 | | 748 | 9,029 | none |

(2017, 2018 and 2020 are in the `tools/run.py` table and companyfacts and move the same way; they are left out of the
table for length.) What moved and why, as the filings say it: no borrowings in any year (only operating leases, $178.0M
noncurrent at 2026-06-27); cash and securities rose from $2.3B to $4.4B while dividends paid rose from $481M (2016) to
$664M (2025); retained earnings rose from $2,057M (2016) to $6,970M (2025). Inventory rose from 16% of sales (2016) to
31% (2022), the year fitness sales fell 28%, and has stayed near a quarter of sales since; receivables have held at 14%
to 19% of sales. Goodwill is small against equity (8% in 2025). A deferred tax asset of $718M (2025) dates mostly from
2023, when the company recognized a $181.4M benefit "related to the revaluation of Switzerland deferred tax assets due to
an increase in the Schaffhausen cantonal tax rate" (10-K FY2023 `0000950170-24-017559`, income tax note); FY2023 net
income ($1,290M) carries that benefit, owner cash does not. Dividends payable of $607.7M at 2026-06-27 are the three
unpaid instalments of the $4.20 dividend approved 2026-06-05. What the figures cannot say: the margin in five years.

### Bearing on Q2 (the castle)
- **Parts over the span** (segments.csv; operating margin): Aviation 42% (2005), 38% (2007), 24% (2009), 25% to 28%
  (2011 to 2016), 31% to 34% (2017 to 2019), 24% to 27% (2020 to 2025). Marine 34% (2005), 8% (2013), 10% to 16% (2014
  to 2016), 20% to 29% (2019 to 2025). Outdoor (as reported) 30% to 45% in every year 2009 to 2025. Fitness 18% to 35%
  (2011 to 2021), 9% (2022), 17% (2023), 27% (2024), 31% (2025). Automotive/mobile $609M at 26% (2007), $246M at 15%
  (2010), $102M at 12% (2016), consumer auto $17M at 6% (2022, 10-K FY2022); auto OEM losses every year 2020 to 2025,
  $(39)M to $(108)M. Company operating margin 19.5% to 28.5% in every year 2007 to 2025 (facts_annual.csv; 2007 and
  2008 from the 10-Ks FY2007 and FY2008).
- **Competitor row, from their own filings, over the span:**

| filer | metric | values | accession |
|---|---|---|---|
| Garmin fitness + outdoor | net sales; operating income | 2022 $2,880M / $678M (24%); 2025 $4,411M / $1,416M (32%) | `0000950170-24-017559`, `0001193125-26-056028` |
| Apple (AAPL) | Wearables, Home and Accessories net sales (no margin reported by category) | FY2017 $12.8B, FY2019 $24.5B, FY2021 $38.4B, FY2022 $41.2B, FY2023 $39.8B, FY2024 $37.0B, FY2025 $35.7B ("decreased [...] primarily due to lower net sales of Accessories and Wearables", FY2025) | `0000320193-19-000119`, `0000320193-22-000108`, `0000320193-25-000079` |
| Zepp Health (ZEPP; Amazfit; 20-F) | revenues; gross margin; operating result | 2020 RMB 6,433M at 20.7%; 2021 RMB 6,250M at 20.9%; 2022 RMB 4,143M at 19.4%; 2023 US$352.9M at 26.2%, operating loss US$(30.5)M; 2024 US$182.6M at 38.5%, loss US$(47.3)M; 2025 US$258.9M at 38.3%, loss US$(29.2)M | `0001104659-23-049064`, `0001104659-26-048127` |
| Peloton (PTON) | total revenue; income (loss) from operations | FY2020 $1,826M / $(81)M; FY2021 $4,022M / $(188)M; FY2022 $3,582M / $(2,734)M; FY2023 $2,800M / $(1,197)M; FY2024 $2,701M / $(529)M; FY2025 $2,491M / $(36)M; FY2026 $2,446M / $161M | `0001639825-20-000122`, `0001639825-23-000132`, `0001639825-26-000038` |
| Honeywell (HON) Aerospace (Aerospace Technologies from 2023; engines, APUs and much besides avionics) | segment margin | 2020 25.2%, 2021 27.7%, 2022 27.3%, 2023 27.6%, 2024 25.8%, 2025 24.5% | `0000773840-23-000013`, `0000773840-26-000013` |
| Garmin aviation | operating margin, same years | 23.5%, 27.1%, 26.9%, 26.8%, 24.1%, 26.1% | segments.csv |
| Brunswick (BC) Navico Group (Navico bought 2021-10-04 for $1.094B; segment recast) | net sales; GAAP operating earnings (loss) | 2021 $688M / $53M; 2022 $1,069M / $68M; 2023 $915M / $5M; 2024 $800M / $(101)M; 2025 $800M / $(340)M (goodwill and trade-name impairments in 2024 and 2025) | `0000014930-24-000054`, `0000014930-26-000027` |
| Garmin marine | net sales; operating income, same years | $875M / $250M; $904M / $215M; $917M / $179M; $1,073M / $236M; $1,183M / $251M | segments.csv |

  Not SEC filers or not reported separately, flagged: Polar, Suunto, Coros, Wahoo, Whoop, Oura (private or foreign,
  no SEC filings); Huawei and Xiaomi (not SEC filers); Samsung and Google (wearables not a reported segment); Navico
  before 2021-10-04 (privately held, Egersund, Norway, per Brunswick's 10-K FY2023); Raymarine (inside Teledyne, not
  separate). Peloton is not among the competitors the filer names (10-K FY2025, Competition; no mention of Peloton in
  the filing); its row is kept because the brief asked for it.
- **Pricing and mix:** gross margin 57% (2023), 59% (2024), 59% (2025), 62.4% (Q2 2026, 8-K `0001193125-26-322113`
  exhibit 99.1); fitness gross margin 53% (2021) to 50% (2022) to 60% (2025) (10-Ks FY2022, FY2025). Units 20.7M in
  2025, up 11%, against revenue up 15% (10-K FY2025 MD&A).
- **R&D against sales:** 8.1% (2009), 12.0% (2012), 15.5% (2016), 16.9% (2020), 17.3% (2023), 15.5% (2025)
  (facts_annual.csv). The filer: "We must continue to make significant investments in research and development in order
  to continue to develop new products" (10-K FY2025, Item 1A).
- **Vertical integration:** "Garmin believes one of its core competencies is its vertically integrated manufacturing
  capabilities at its facilities in Taiwan, the U.S., the Netherlands, the U.K., Poland, and China"; about 10,200
  manufacturing staff and 6,500 engineering and development staff; 11,400 of about 23,000 employees in APAC (10-K FY2025,
  Item 1).
- **Aviation certification:** products for "type certificated aircraft" are "required to be certified by the FAA, its
  European counterpart, the European Aviation Safety Agency, and other comparable organizations before they can be used
  in an aircraft" (10-K FY2008, Item 1A, `0001144204-09-010751`); the filer names Honeywell, Collins (RTX), Thales,
  Safran, Avidyne, Dynon, Universal and others as aviation competitors (10-K FY2025).
- **Taiwan and tariffs:** "Our principal manufacturing facilities for consumer products are located in Taiwan", with the
  PRC risk stated at length (10-K FY2025, Item 1A); refunds of about $21M of IEEPA tariffs received in Q2 2026, further
  refunds not recognized (10-Q `0001193125-26-322114`); marine gross margin in Q2 2026 helped by tariff refunds (10-Q MD&A).

### Bearing on Q3 (capital)
- Capital spending $307.6M (2021), $244.3M (2022), $193.5M (2023), $193.6M (2024), $270.4M (2025), $194.4M in H1 2026,
  against depreciation of $103.5M to $152.6M (cash-flow statements). No maintenance figure is stated in the filing.
- Arithmetic of mine from the filed balance sheet, not a filed figure: FY2025 operating income $1,876M against equity
  less goodwill, other intangibles and cash and securities ($8,973M less $760M, $198M and $4,135M = $3,880M) is about
  48% pre-tax.

### Bearing on Q4 (the accounts) and Q5 (integrity), recorded, not judged
- Stock pay $166.0M in FY2025 (2.3% of sales), against $41.2M in 2016 (1.4%) (cash-flow statements).
- The company issues annual guidance and raises it ("we are raising our full year 2026 guidance. We now anticipate
  revenue of approximately $8.05 billion and pro forma EPS of $10.00", 8-K of 2026-07-29, exhibit 99.1,
  `0001193125-26-322113`), and puts "pro forma EPS" ($2.81, against GAAP $2.80 for Q2 2026) in its release highlights.
  The rows that bear on these: **[L2019-006]** (guidance), **[L2016-006]** (an adjusted figure featured),
  **[L2002-041]** (targets); not weighed here.
- 10-K/A for FY2023, filed 2024-11-29 (`0000950170-24-131914`): related-party transactions "erroneously omitted" from the
  original report (family members of two executive officers employed at more than $120,000 and less than $300,000 a year,
  from 2011 and 2014; "In October 2024, the Company determined that such transactions had not previously been approved
  or ratified by the Company’s Audit Committee"; three smaller ones ratified at the same time).
- Founder and executive chairman Min H. Kao beneficially owns 9.7% (proxy 2026, `0001308179-26-000318`); directors and
  officers with families about 15% (10-K FY2025, Item 1A). CEO total pay $7.74M in 2025: salary $1.40M, stock awards
  $6.30M (PC-RSU and RSU), a $358 holiday bonus (proxy 2026, Summary Compensation Table).

### Bearing on Q6 (the money and the owners)
- Dividends paid $491.5M (2021), $679.1M (2022), $558.8M (2023), $572.4M (2024), $663.9M (2025); approved per share
  $3.00 (2024), $3.60 (2025), $4.20 (2026), each in four instalments, approval by shareholders under Swiss law (10-Q
  `0001193125-26-322114`, note 9).
- Buybacks under plans: $201.0M (2022), $99.0M (2023), $62.3M (2024), $181.0M (2025), $81.6M (H1 2026). The 2024
  Program bought 1,375 thousand shares for $274.6M, about $199.7 a share; the 2026 Program ($500M, to 2028-12-30) bought
  216 thousand for $51.9M by 2026-06-27, about $240 a share; Q4 2025 average prices by month $252.15, $197.63 and $200.31
  (10-K FY2025 Item 5; 10-Q note 9). No program names a price above which it stops ("at management’s discretion").
  Against the COMPUTATION below (not a Q7 result): the 2026 Program's average sits above the top of the computed
  all-equity range ($211.57).
- Acquisitions, net of cash: $148.6M (2020), $20.2M (2021), $13.5M (2022), $150.9M (2023), $16.4M (2024), $175.7M
  (2025); TrainingPeaks and TrainHeroic acquired 2026-07-20, price not disclosed, "not material" (10-Q subsequent events).

### Bearing on Q9 (exposures)
- No borrowings; $4,369.9M of cash and marketable securities at 2026-06-27, of which corporate debt securities at
  $1,629.3M fair value (10-Q note 4). Noncancellable purchase obligations of about $411M beyond one year (10-K FY2025).

### Q7: COMPUTATION, NOT A CLEARANCE
*(The file closed at Q1. These are the two reporting figures the brief asks for, under its reporting convention;
nothing here is a verdict or entry language. Arithmetic in `q7.py`, output in `q7_output.txt`.)*

**Owner cash** (USD millions) = operating cash flow less stock pay, less all capital spending, less acquisitions net of
cash and purchases of intangibles, from the filed cash-flow statements (10-K FY2022 `0000950170-23-003566`, 10-K FY2025
`0001193125-26-056028`). Working capital is inside operating cash (the inventory builds of $476M in 2021 and $363M in
2022 are charged). The company's own tax is inside operating cash; no conversion (Q7, Whose tax).

| | 2021 | 2022 | 2023 | 2024 | 2025 | five-year average |
|---|---|---|---|---|---|---|
| owner cash after interest income (equity-only) | 590.1 | 451.8 | 930.5 | 1,085.3 | 1,021.3 | 815.8 |
| owner cash before interest (all-equity, central) | 566.5 | 418.1 | 866.6 | 991.5 | 914.8 | 751.5 |
| depreciation in place of capital spending (variant, all-equity) | 770.7 | 543.6 | 927.8 | 1,044.6 | 1,032.6 | 863.9 |

*CONVENTION of this run:* interest income is taken out after tax at the FY2025 effective rate (17.4%) in every year;
rationale: the effect is under $10M a year and the 2023 rate (negative, from the one-time Swiss deferred-tax benefit) is
not a rate. The maintenance-only case of specific (e) is not central because the filing gives no maintenance figure;
the depreciation variant is shown beside it. Specific (a): neither end year is described by the filer as aberrational;
the literal window is used (2022, the trough, is inside it). Specific (c): the default pair, acquisitions deducted and
total growth credited; the filer reports no organic growth figure, so there is no organic pair. The TrainingPeaks deal
after the window has no filed price; it is credited at nothing and added to net debt at nothing.

**The range** (ten years at the growth shown, capped at the shown rate, then zero nominal growth, discounted at 5.64%):
- **All-equity basis, central:** growth shown 12.7% a year (aggregate, 2021 to 2025); whole-business value $13,325M
  (no growth) to $36,433M (shown growth), 2.73 to 1; plus net cash of $4,369.9M (cash and marketable securities at
  2026-06-27; no borrowings, no finance leases; operating leases left out) gives **$91.75 to $211.57 a share** against
  $276.05.
- **Equity-only, beside:** growth shown 14.7%; $14,464M to $46,105M, 3.19 to 1; **$75.00 to $239.07 a share**.
- Depreciation variant (all-equity), beside: $102.08 to $167.61 a share.

**Fair price** (the price at which the midpoint of the range earns the floor of about ten percent, after the company's
own tax): the midpoint stream (the average of the no-growth and shown-growth streams) priced at 10%: **$89.38 a share on
the all-equity basis (central)**; **$80.08 on the equity only**. At $276.05 the midpoint stream earns about 3.1% on the
enterprise value of $48,867M, below the 5.64% sovereign.

What the computation would have meant had Q7 been reached: the price sits above the top of the range on both bases,
which the floor convention closes OUT. Recorded only. If the $607.7M of declared, unpaid dividends were treated as owed,
the all-equity per-share figures would each fall by about $3.15.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `fa6ab04c`); written question by question; committed after each
      closed section (template; Step 0 to Q1; after-the-stop facts and computation with the close).
- [x] Dispatched: the brief allowed per-question pathspec commits; a lock in `Screens/_daily/` was present, written by the
      dispatching session ("interactive v5 re-runs batch 5"); the fold is the dispatcher's. Not in the register until
      folded; binds nothing until then.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; `Test Runs/` was not listed.
      What I saw by accident is declared at the top under Contamination and not used.
- [x] Every v5 id resolves (`check_ids.py` in the working folder); every filing fact has its accession; numbers of mine
      are labelled as arithmetic or CONVENTION.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance, and the Q7 figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, all capital spending, acquisitions, working capital), never a
      net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found (foundations, and the IN case inside Q1); facts for later
      questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q1.** Q1's "What it rules OUT" list sends to OUT the business "quite dependent on the technology
continuing to gallop" **[M1999-075]**, and sends fast-moving technology to TOO HARD, and Garmin is both; the routing paragraph (Q1, What understanding means) decides it
for the second, so I closed TOO HARD, but the OUT item is never reconciled with the routing, and a second analyst could
close the same name OUT at Q1 on the same rows. (2) **The parts convention picks one of two twins.** The threshold makes
outdoor (44% of five-year operating profit) the deciding part and leaves fitness (28%) aside, although the two sell the
same kind of product from the same factories on the same platform; the segment line is the filer's, not an economic one,
and the text gives no rule for parts that share one castle. I read fitness beside outdoor and said so. (3) **"The midpoint
of the range earns the floor"** does not say whether the midpoint is the average of the two end values, the stream at
the average growth rate, or the average of the two streams; I used the average of the two streams priced at 10%. The
readings give different figures. (4) **Interest income on the all-equity basis.** Section H says owner cash "before
interest" against market value plus net debt; for a company with net cash, taking the cash off the enterprise value while
leaving interest income in owner cash counts the cash twice. The text does not say interest income comes out; I took it
out after tax and said so. (5) **The brief's error.** It says Polar, Suunto, Coros, Navico before 2022 "and the Chinese
wearable makers are not SEC filers or not reported separately". Zepp Health (Amazfit), a Chinese wearable maker that the
filer names among its fitness competitors, files a 20-F with the SEC every year; I read two of them and added the row.
A second, smaller slip: Peloton is offered as a competitor, but the filer does not name it and its business (connected
fitness equipment and subscriptions) is not the GPS wearable; its row is kept as asked.
