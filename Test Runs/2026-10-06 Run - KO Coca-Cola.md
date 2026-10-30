# Company Run: The Coca-Cola Company (NYSE: KO), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface copied from
`Test Runs/_TEMPLATE - Company Run.md` before any fetch. Research folder: `Test Runs/_research 2026-10-06 KO/` (`fetch.py`,
`totext.py`, `list_filings.py`, `facts.py`, `owner_cash.py` and `owner_cash_output.txt`, `q7_calc.py` and its output,
`peers.py` and its output, `check_ids.py`, `run_py_output.txt`, `cover_shares.txt`, `sources_output.txt`; raw filings and
text dumps under `cache/`, gitignored). Every judgment cites a v5 ledger id in bold; every filing fact carries its
accession. A STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED. No em dashes are
used in this file's own prose.

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the register and the session-state files were not opened, so whether the operator holds KO is unknown to the analyst.

**CONTAMINATION DECLARED.** (1) **The shelf itself.** Berkshire has owned Coca-Cola since 1988 and the speakers discuss it
often: a text search counts 149 rows of `principle_ledger_v5.csv` that contain "Coca", and the framework quotes several of
them as rules (**[M1998-040]**, **[M1999-054]**, **[M1997-103]**, **[M2012-106]**, **[M2008-076]**, **[M2001-088]**,
**[M2006-029]**, **[M1997-046]**). The speakers are holders praising a holding; "Berkshire has a dog in this fight, and you
should therefore assess the commentary that follows with special care" **[L2009-015]**. In this run a row about Coca-Cola is
used only for the test it states (for example, the two variables of **[M1998-040]**), never as evidence of what the business
is today; every finding about KO comes from KO's and its competitors' filings. (2) **The map.** `CLAUDE.md`, which every
session loads, describes `Framework/v4/VERIFICATION - the two cases that decide the deletions.md` as "Citigroup and
Coca-Cola, worked". That file was not opened (the dispatch bars it), nor any earlier KO run or research folder. The
directory listing of `Test Runs/` shows a `2026-10-05 Run - BRK.B Berkshire Hathaway.md`, which may value Berkshire's KO
stake; it was not opened. One other company's v5 run of 2026-10-05 (PBH) was read for form only. (3) **Training memory.**
I came to this run knowing KO's general history (the bottler system, the Berkshire holding, the 1998 peak price and the
long flat stretch after it). That memory is a prior; the filings replace it. Two filing facts already differ from it: the
chief executive is Henrique Braun (8-K 2026-06-25, `0001552781-26-000366`, Ex 99.1), and the company owns fairlife and
BodyArmor outright.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$86.51** (2026-10-05 close as printed by `tools/run.py`; Yahoo chart endpoint; **aggregator, live quote
  only, flagged** under operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, $0.25 par, **4,302,549,243** shares (10-Q
  for the quarter ended 2026-07-03, filed 2026-07-29, accession `0001628280-26-050503`; `python Screens/cover_shares.py KO`,
  output in `cover_shares.txt`). No other class of common stock is registered (cover page lists the common stock and
  nineteen series of notes).
- **Market cap:** 4,302.549M x $86.51 = **$372,213.5M**.
- **Sovereign for the earnings currency (USD; the company reports in dollars and 84% of unit case volume is outside the
  United States, FY2025 10-K Item 1):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority; output in `sources_output.txt`).
- **Filings read** (operator rule 4):
  - 10-K for FY2025, filed 2026-02-20, accession `0001628280-26-010047` (Items 1, 1A in part, 3, 5, 7 in part; the cash-flow
    statement, the equity statement, Notes 2, 12, 17, 18 in part).
  - 10-K for FY2024 `0000021344-25-000011`, FY2023 `0000021344-24-000009`, FY2022 `0000021344-23-000011`, FY2021
    `0000021344-22-000009`, FY2020 `0000021344-21-000008`, FY2019 `0000021344-20-000006`, FY2018 `0000021344-19-000014`
    (cash-flow commentary, fairlife and BodyArmor notes, factoring disclosures).
  - 10-Q for the quarter ended 2026-07-03, filed 2026-07-29, accession `0001628280-26-050503`.
  - DEF 14A filed 2026-03-16, accession `0001104659-26-028215`.
  - 8-K 2026-07-28 `0001628280-26-049922`, Ex 99.1 (second-quarter 2026 earnings release); 8-K 2026-07-16
    `0001628280-26-048466` (fairlife ransomware event); 8-K 2026-06-25 `0001552781-26-000366` (North America leadership).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$7,408
  million** on the filed consolidated statement of cash flows (10-K `0001628280-26-010047`) = `tools/run.py` 7,408. Also
  equity attributable to shareowners $32,169 million at 2025-12-31 on the filed equity statement = run.py 32,169.
- **`python tools/run.py KO`, arithmetic lines only** (output in `run_py_output.txt`; its v4 material, its three-year mean
  and its "growth the price assumes" are not used, Part VII). Owner cash recomputed for ten years in `owner_cash.py`
  (output `owner_cash_output.txt`), USD millions:

| FY | OCF | SBC | capex | D&A | owner cash, capex basis | owner cash, D&A basis | recast item | capex basis, recast |
|---|---|---|---|---|---|---|---|---|
| 2016 | 8,792 | 258 | 2,262 | 1,787 | 6,272 | 6,747 | | 6,272 |
| 2017 | 7,041 | 219 | 1,750 | 1,260 | 5,072 | 5,562 | | 5,072 |
| 2018 | 7,627 | 225 | 1,548 | 1,086 | 5,854 | 6,316 | | 5,854 |
| 2019 | 10,471 | 201 | 2,054 | 1,365 | 8,216 | 8,905 | | 8,216 |
| 2020 | 9,844 | 126 | 1,177 | 1,536 | 8,541 | 8,182 | | 8,541 |
| 2021 | 12,625 | 337 | 1,367 | 1,452 | 10,921 | 10,836 | | 10,921 |
| 2022 | 11,018 | 356 | 1,484 | 1,260 | 9,178 | 9,402 | | 9,178 |
| 2023 | 11,599 | 254 | 1,852 | 1,128 | 9,493 | 10,217 | +167 fairlife | 9,660 |
| 2024 | 6,805 | 286 | 2,064 | 1,075 | 4,455 | 5,444 | +6,000 IRS deposit | 10,455 |
| 2025 | 7,408 | 279 | 2,112 | 1,050 | 5,017 | 6,079 | +6,069 fairlife | 11,086 |
| **5-yr mean 2021-2025** | | | | | **7,812.8** | 8,395.6 | | **10,260.0** |

  As filed (XBRL, latest vintage; FY2023 to FY2025 equal to the filed FY2025 cash-flow statement). SBC resolved and
  complete: one "Stock-based compensation expense" line a year, no other stock-pay line (run.py's statement-line read of
  the three latest 10-Ks). **The recast, a CONVENTION of this run, shown beside the as-filed figure and never instead of it:**
  (a) the fairlife contingent consideration paid inside operating cash flow is added back, because it is the purchase
  price of a business bought in January 2020, routed to operating activities by GAAP only because it exceeded the
  acquisition-date fair value ("the activity in 2025 included $6.1 billion of the $6.2 billion final milestone payment
  for fairlife", FY2025 10-K, MD&A; the other $104 million was in financing; FY2023: $108 million of the $275 million
  milestone in financing, the rest in operating, FY2023 10-K); it is counted instead as an acquisition at Q6; (b) the
  $6.0 billion IRS Tax Litigation Deposit of September 2024 (tax years 2007 to 2009, refundable "in full or in part if the
  Company's tax positions are ultimately sustained on appeal", FY2025 10-K, Item 3) is added back, and the whole tax
  dispute is carried instead as a contingent liability at Q7 and Q9, at the company's own figures. Rationale: the five-year
  average is meant to show the business's recurring cash; one acquisition price and one contested tax deposit in two
  years of five would otherwise set the base, which the averaging exists to prevent **[L2005-003]**.

## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**; for a
concentrate seller whose bottlers carry the plants, the answer turns on whether people keep asking for the drinks by name
and on the price paid, not on the quote. The market serves and does not instruct **[M2006-077]**: nothing in this run is
read from the price except the price. **Who is paid to tell you** bears hardest here, in two directions: the company
"raises full year guidance" in its own release (8-K `0001628280-26-049922`, Ex 99.1), and the speakers whose rows build
the framework are KO's largest holder ("Berkshire has a dog in this fight" **[L2009-015]**, declared above). Margin of
safety: if the case needs a pencil it is too close **[M1996-084]**. The analyst's habits: "the worst anchoring effect, which
is always your previous conclusion" **[M2016-054]**, and here the anchor is a famous one; the hunt is for "what you’re
missing" **[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. **Volume has stood still.** The system sold 33.8 billion unit cases in 2025 against 33.7 billion in 2024; North America
   unit case volume fell 1%, Trademark Coca-Cola in North America fell 1% (FY2025 10-K, Item 1 and MD&A,
   `0001628280-26-010047`). (Against it, first-half 2026 unit case volume rose 4%, 10-Q `0001628280-26-050503`.)
2. **The tax dispute is large and open.** The Tax Court sided "predominantly" with the IRS; the company paid $6.0 billion
   for 2007 to 2009 and estimates "the potential aggregate remaining incremental tax and interest liability for the tax
   years 2010 through 2025 could be approximately $14 billion", plus "approximately 3.5%" on the effective tax rate each
   year the method applies (FY2025 10-K, Item 3). The Eleventh Circuit heard the appeal on 2026-06-25; no decision is
   reported (10-Q `0001628280-26-050503`).
3. **Two recent brand purchases went wrong on price.** BodyArmor, bought for about $5,600 million in November 2021 (FY2022
   10-K), has had trademark impairments of $760 million (2024) and $960 million (2025) (FY2025 10-K, other operating
   charges). fairlife, bought outright in January 2020, cost a further $6,173 million in a final milestone paid in March
   2025 after remeasurement charges of $51M, $369M, $1,000M, $1,702M, $3,109M and $47M in 2020 to 2025 (FY2022, FY2023,
   FY2025 10-Ks).
4. **Operating cash is helped by financing the working capital.** Receivables sold under the factoring program rose from
   $185 million (2020) to $21,873 million (2024) and $14,710 million (2025) (each year's 10-K); receivables fell from 34.8
   days of revenue (2020) to 23.1 days (2025) (`owner_cash_output.txt`). Supplier-finance confirmed obligations were $1,363
   million at the end of 2025; the extension of supplier payment terms added an estimated $869 million to 2019's
   operating cash (FY2020 10-K).
5. **fairlife's United States production was suspended** after a ransomware event; "The full scope, nature and impacts of
   the incident are not yet known" (8-K 2026-07-16, `0001628280-26-048466`).
6. **Concentrated retail.** The 10-K names "a concentrated retail sector with powerful buyers able to freely choose among
   Company products, products of competitive beverage suppliers and individual retailers' own store or private-label
   beverage brands" among its competitive challenges (FY2025 10-K, Item 1).

## THE STANDING RULE
Owning KO shares bought with the buyer's own money and sized so that a total loss is survivable does not put the buyer at
risk of ruin; bought on margin it could: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "We are
never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. The target's own debt,
the tax dispute and its other exposures are weighed at Q9, not here.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The question: "can I understand it?" **[M1995-051]**, meaning "a pretty good idea where it’s going to be in ten years"
**[M1997-021]**.

- **What the business is, from the 10-K.** Two lines of business: concentrate operations, which sell "beverage
  concentrates, sometimes referred to as “beverage bases,” syrups, including fountain syrups" to authorized bottlers, and
  finished product operations (consolidated bottlers, fountain syrup in the United States, Costa shops, fairlife), which
  "generate higher net operating revenues but lower gross profit margins than concentrate operations" (FY2025 10-K, Item 1,
  `0001628280-26-010047`). The bottler buys "its entire requirement of concentrates or syrups" from the company in an
  exclusive territory, and the company sets the concentrate price under an "incidence-based concentrate pricing model in
  most markets", subject "as a practical matter" to "competitive market conditions" (same). Five independent bottlers
  carry 44% of worldwide unit case volume; 84% of volume is outside the United States; Trademark Coca-Cola is 47% of it
  (same).
- **Test 2, the key variables and how predictable they are** **[M1998-044]**. The rows name them for this company in so
  many words: "The two important elements in Coke are unit case sales and shares outstanding" **[M1998-040]** (used here
  as the test it states, not as a verdict; see the contamination note). Adding what the filings show moves the result:
  price/mix, currency (84% of volume abroad, reported in dollars) and the tax rate (the IRS method would add "approximately
  3.5%" to it, Item 3). Unit cases: 29.3 billion (2016), 29.2 (2017), 29.6 (2018), 30.3 (2019), 29.0 (2020), 31.3 (2021),
  32.7 (2022), 33.3 (2023), 33.7 (2024), 33.8 (2025) (FY2018, FY2020, FY2022, FY2024, FY2025 10-Ks, Item 1); about 1.6% a
  year, with the definition widened in 2019 for Costa transactions (FY2020 10-K). Shares outstanding on the 10-K covers:
  4,293,461,702 (February 2017) and 4,300,723,069 (February 2026): flat for nine years (XBRL dei, ten 10-K covers). Each
  of these is a slow-moving consumer quantity, measured and reported every quarter for decades.
- **Test 3, do the past statements tell me the future ones** **[M2008-033]**. With work, yes: revenue fell from $41.9
  billion (2016) to $33.0 billion (2020) and rose to $47.9 billion (2025) mostly by selling and buying bottlers
  ("structural changes", FY2025 10-K, MD&A), while operating income moved in a narrower band ($7.8 billion to $13.8
  billion, the low years carrying refranchising and fairlife charges; XBRL `OperatingIncomeLoss`). The structural changes
  are named and quantified in each MD&A, so the statements can be read through them.
- **Test 7, is the forecast about customers or technology** **[M2017-019]**, **[M2023-030]**. About customers: whether
  people in two hundred countries keep buying these drinks by name. No technology decides it. The changes that could move
  it (sugar and ingredient regulation, packaging rules, the 10-K's "Regulators in the United States and abroad have been
  expressing concerns about processing and the use of particular ingredients", Item 1) are slow, and slow change is
  Q2's question **[M2014-038]**.
- **Test 4, important and knowable** **[M2006-076]**. One important item is not knowable from here: the outcome of the
  Eleventh Circuit appeal heard on 2026-06-25 (10-Q `0001628280-26-050503`). It is bounded by the company's own figures
  ($6.0 billion paid, about $14 billion more for 2010 to 2025, about 3.5 points on the tax rate), so it is carried at Q7
  and Q9 as a stated range, not as a fog over the whole business.
- **Test 8, how far off could I be** **[M2011-084]**. On volume and price, a few points a year; the range at Q7 will show
  how much that matters. **Test 11, abroad** **[M2000-141]**: the governance and tax nuance of two hundred countries is
  not understood country by country; the business is read as a system whose foreign earnings arrive as concentrate
  sales and equity income, and the one tax question that matters is named above.
- **Test 9, doubt** **[M2002-092]**. No doubt that the economics can be pictured ten years out at the level the rows ask:
  "that didn’t mean we had to do it to four decimal places or anything of the sort" **[M2015-086]**.
- **VERDICT: IN.** The key variables are consumer quantities that move slowly and are reported **[M1998-044]**,
  **[M1998-040]**; the forecast is about consumer behaviour, not technology **[M2023-030]**; the statements, read through
  the named structural changes, tell what the future ones will look like **[M2008-033]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now." **[M1995-038]**

- **Test 1, the key factors and how permanent** **[M1995-038]**. The 10-K names them itself: "leading brands with high
  levels of consumer recognition and loyalty; a worldwide network of bottlers and distributors" (FY2025 10-K, Item 1).
  The bottler's agreement makes the bottler buy "its entire requirement of concentrates or syrups" from the company, in
  an exclusive territory, for ten-year terms renewable "indefinitely" in the United States (same). The system serves 2.2
  billion servings a day (same). Both factors are old and slow to change; neither depends on a product invention.
- **Test 3, the attacker with money** **[M2012-106]**. The richest attacker is named in its own filing: "In many countries
  in which our products are sold, including the United States, The Coca-Cola Company is our primary beverage competitor"
  (PepsiCo 10-K FY2025, `0000077476-26-000007`, Item 1). PepsiCo had $93.9 billion of revenue in 2025 (its XBRL) and has
  attacked for over a century; its own figures follow in the competitor row, and they do not show the castle falling.
- **Test 4, pricing power** **[M2005-020]**, **[M2000-031]**. Consolidated price/mix and concentrate volume, from each
  year's 10-K MD&A: 2021 +6% and +9%; 2022 +11% and +5%; 2023 +10% and +2%; 2024 +11% and +2%; 2025 +4% and +1%
  (FY2021 to FY2025 10-Ks). Prices compounded about 49% in five years and volume rose every year. Much of the price is
  inflationary pricing in high-inflation countries ("inflationary pricing in Argentina", FY2025 10-K), which currency took
  back (currency -7%, -4%, -5%, -2% in 2022 to 2025), so the dollar test is narrower: in North America, a hard-currency
  market, 2025 price/mix was +5% against unit case volume -1% (FY2025 10-K). "Anytime you can charge more for a product and
  maintain or increase market share against wellentrenched, well-known competitors, you have something very special in
  people’s minds." **[M2000-031]**: see the competitor row for the share half.
- **Test 5, unit volume and share of mind** **[M1999-054]**, **[M2000-030]**. Unit cases 29.3 billion (2016) to 33.8 billion
  (2025), about 1.6% a year (Q1); first-half 2026 +4%, second quarter +5%, with Trademark Coca-Cola +5% and Coca-Cola Zero
  Sugar +16% in the quarter (8-K `0001628280-26-049922`, Ex 99.1). Trademark Coca-Cola's share of worldwide volume was 45%
  in 2016 to 2019 and 47% in 2020 to 2025 (FY2018, FY2019, FY2021, FY2024, FY2025 10-Ks): the oldest brand gained share
  inside the company's own growing portfolio.
- **Test 7, the brand in the customer's mind** **[M2023-073]**, **[M2015-038]**. The product is the case the rows use for
  asking by name ("which hundreds of millions of people every day are going to go in and ask for by name" **[M2002-091]**,
  cited for the test, not as a finding). The filing fact: bottlers pay for the right to sell it, renewable for decades, and
  five of them carry 44% of the volume (FY2025 10-K). **Against the retailer** **[M2001-090]**, **[M2019-041]**: the 10-K
  names "a concentrated retail sector with powerful buyers able to freely choose among Company products, products of
  competitive beverage suppliers and individual retailers' own store or private-label beverage brands" as a challenge;
  no customer is disclosed above 10% of revenue except one bottler at 10% (FY2025 10-K, Note 20). Kraft Heinz is the rows'
  case of a brand losing to the intermediary; in this filing set the evidence runs the other way (price/mix positive in
  every segment in 2025).
- **Test 8, the low bid** **[M2008-076]**, **[M2001-088]**. North America 2025: KO volume -1% at +5% price/mix; PepsiCo's
  North American beverages volume -3% ("a 6% decline in non-carbonated beverage volume and a slight decline in CSD volume")
  at +5% effective net pricing (PepsiCo 10-K FY2025, PBNA). The customer paid the same rise for KO and left less.
- **Test 9, ask the competitors** **[M1999-130]**. PepsiCo's 10-K answers in print every year: "we and The Coca-Cola
  Company represented approximately 24% and 20%, respectively, of the U.S. liquid refreshment beverage category by
  estimated retail sales in measured channels" (FY2016, `0000077476-17-000010`); 22% and 20% (FY2020,
  `0000077476-21-000007`); 16% and 20% (FY2025, `0000077476-26-000007`), and each year: "However, The Coca-Cola Company
  has significant carbonated soft drink (CSD) share advantage in many markets outside the United States." Keurig Dr Pepper
  lists "Coca-Cola, PepsiCo" first among its primary competitors and records that Coca-Cola owns the Dr Pepper trademark
  and formula in some countries outside North America (KDP 10-K FY2025, `0001418135-26-000016`).
- **Test 2, without the lord** **[L2007-006]**, **[M2008-045]**. The chief executive changed in 2026 (Henrique Braun signs
  the releases, 8-K `0001552781-26-000366`) and the head of North America left in August 2026 (same 8-K), and the
  second quarter grew. The rows carry the counter-case for this very company: "It had stagnated during the previous decade
  under an earlier management, despite having the same product" **[M1997-046]**; the castle survived that stagnation, but
  the returns did not (section VI carries the pull OPEN). Weighed at Q5, not here.
- **Test 10, widening or narrowing** **[M1999-108]**, **[L2005-010]**. Widening: Trademark Coca-Cola's share of the system's
  volume up two points; the main rival's US share down eight points while KO's held; volume up every year 2021 to 2025
  through large price rises. Narrowing or flat: KO's own US share is 20% in all three PepsiCo filings, so in its home
  market it held rather than gained; whoever took PepsiCo's eight points was not KO; North America volume fell 1% in 2025;
  and the purchase into sports drinks (BodyArmor) is where the impairments sit (Q6); Costa, bought for $4.9 billion
  in 2019 (FY2019 10-K), shows no impairment in a text search of the FY2020 to FY2025 10-Ks, and coffee volume fell 2%
  in the second quarter of 2026 (Ex 99.1).
- **Test 11, what could destroy, modify or reduce it** **[M2000-014]**. The 10-K's own list: "ongoing public concern about
  obesity; other health-related public concerns surrounding consumption of sweetened beverages; the effects or perceived
  effects of the usage of weight-loss drugs on consumption patterns; potential new or increased taxes on sweetened
  beverages", and ingredient regulation (FY2025 10-K, Item 1A). These are slow and have been named for years; the zero-sugar
  line growing 16% is the company's answer to the first of them. Slow change can "lull you to sleep easier" **[M2014-038]**;
  nothing in the filings shows it moving fast now.

**The competitor row** (each filer's own 10-K XBRL; `peers.py`, output `peers_output.txt`):

| company | US LRB retail share, FY2016 / FY2020 / FY2025 (PepsiCo 10-K) | 2025 revenue | 2025 operating margin | revenue growth a year, 2016-2025 | accession (FY2025 10-K) |
|---|---|---|---|---|---|
| Coca-Cola | 20% / 20% / 20% | $47,941M | 28.7% (concentrate segments: EMEA 37.3%, Latin America 59.1%, North America 25.9% after a $960M impairment, Asia Pacific 36.2%) | 1.5% (bottlers sold and bought) | `0001628280-26-010047` |
| PepsiCo | 24% / 22% / 16% | $93,925M | 12.2% (includes snacks; PBNA operating profit fell 53% on a Rockstar impairment) | 4.6% | `0000077476-26-000007` |
| Keurig Dr Pepper | not stated | $16,603M | 21.5% | 11.1% (merger in 2018) | `0001418135-26-000016` |
| Monster (a KO distribution partner and 21% investee) | not stated | $8,294M | 29.2% | 11.8% | `0001104659-26-020831` |

  The margin column is not like for like (bottling, snacks and dairy sit inside some figures and not others); the share
  column is the cleaner comparison and comes from the rival's own filing.

- **VERDICT: IN.** The money test is answered by the money-rich rival's own filing, which has printed for ten years that
  its share fell while KO's held **[M1997-103]**, **[M2012-106]**, **[M1999-130]**; the customer took the same price rise from
  KO with less loss of volume than from that rival **[M2000-031]**, **[M2008-076]**; unit volume and the flagship's share of
  it rose **[M1999-054]**. The threats the company names are slow ones **[M2000-014]**, **[M2014-038]**. Contrary evidence
  kept: flat US share, falling North America volume in 2025, and failures in the categories KO bought into.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
"does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**; "whether that’s good or
bad depends on what we earn on that incremental $130 million over time" **[M2001-019]**. Arithmetic in `capital.py`,
output `capital_output.txt` (XBRL 10-K facts, latest vintage).

- **Test 1, return on the capital actually needed** **[M2010-090]**, **[M2011-060]**. Net tangible operating capital
  (trade receivables, inventories, prepaid and other current assets and net PP&E, less payables and accrued expenses and
  accrued income taxes; goodwill, trademarks, investments and cash left out) was $9,850M at the end of 2016 and $4,171M at
  the end of 2025 (2024: $4,625M once the $6.1 billion fairlife liability is taken out of payables). Operating income
  before "other operating charges" was $10,028M (2016) and $15,023M (2025). The pre-tax return on the tangible capital the
  business needs rose from about 100% to over 300%. Two cautions from the rows. The rise came partly from shrinking the
  capital: refranchised bottlers left the balance sheet, and payables (with supplier-finance terms) and factored
  receivables now fund most of the working capital (contrary evidence, item 4). And the "other operating charges"
  excluded above recur every year ($846M to $4,163M in 2016 to 2025, XBRL and FY2025 10-K); counted in, the return is
  lower but still far above 100% in every year: "special charges time after time [...] it’s not been good at all" is the
  test **[M1999-033]**, and here it does not bite.
- **Test 2, what must be reinvested to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending was
  $2,112M in 2025 against depreciation and amortization of $1,050M (FY2025 10-K); the split by segment was North America
  31.7%, Corporate 27.7%, Bottling Investments 25.9%, EMEA 11.2% (same). The filing does not state a maintenance figure;
  the rows allow depreciation as the proxy "in most companies" **[M1998-127]**, so the D&A basis ($1,050M) is the
  stand-still estimate and the excess (about $1.06 billion in 2025) is growth spending, mostly in North America (where
  fairlife and the fountain and finished-goods operations sit) and in corporate systems. Both bases are carried to Q7.
  The concentrate business itself needs very little: the bottlers own the plants, trucks and coolers (10-K, Item 1).
- **Test 3, what the added capital earned, FY2017 to FY2025.** Acquisitions $24,616M (including the fairlife milestones in
  every leg and the BodyArmor holdbacks), disposals $15,921M (mostly bottlers refranchised), capital spending above D&A
  $4,196M: net capital added about $12.9 billion. Pre-tax operating income before other charges rose $4,995M and equity
  income $1,196M. That is about 48% pre-tax on the net capital added, but most of it is price on the existing base
  (Q2), not a return the added dollars earned. The large added dollars went into BodyArmor ($5,600M; $1,720M impaired),
  Costa ($4.9 billion, 2019) and fairlife (outright purchase in 2020, then milestones of $100M, $275M and $6,173M). "Most
  of the great businesses generate lots of money. They do not generate lots of opportunities to earn high returns on
  incremental capital" **[M2003-120]**: the filings fit that row.
- **The growth arithmetic.** Owner cash (recast, capex basis) was $10,921M in 2021 and $11,086M in 2025, about 0.4% a year
  across the five-year window. The window opens on a high base: 2021 cash was raised by the start of factoring ($185M
  sold in 2020, $6,266M in 2021) and by lower payments made in 2021 for 2020's reduced incentives and marketing (FY2021
  10-K, MD&A). Unlevered (interest paid added back after tax at 21%), the series runs $11,504M to $12,448M, about 2.0% a
  year; operating income before other charges grew about 7.7% a year (2021 $11,154M to 2025 $15,023M) while interest
  paid rose from $738M to $1,724M and cash taxes from $2,168M to $2,873M (XBRL). No rate is carried past the discount
  rate **[M1997-095]**, and unprecedented returns are not assumed to last **[M1998-016]**.
- **WEIGHS FOR** on the business, with the incremental record against it: the business needs almost no tangible capital
  for what it earns **[M1998-081]**, **[M2011-060]**, while the money put in beyond that, mostly by purchase, earned little
  that the filings can show and lost $1.7 billion on one deal **[M2001-019]**, **[M2003-120]**.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.

- **The balance sheets, 2016 to 2025** (run.py's ten-year table, first-filed XBRL; the FY2025 and FY2024 columns read
  against the filed balance sheet in `0001628280-26-010047`). What moved, and why the filings say it moved:
  - **Equity and its parts.** Shareowners' equity $23,062M (2016), $17,072M (2017), $32,169M (2025). The 2017 drop is the
    year of the US tax reform charge (net income $1,248M that year, XBRL). Reinvested earnings rose from $65,502M to
    $80,382M; treasury stock is $56,423M at cost and accumulated other comprehensive loss $14,131M (mostly currency) at
    2025 (filed balance sheet). Equity is small against the earnings because of a century of buybacks and currency
    losses, so return on equity says little here; "you could make return on equity whatever you want" **[M1998-017]**.
  - **Goodwill and trademarks.** Goodwill $10,629M (2016), $16,764M (2019, Costa), $19,363M (2021, BodyArmor), $15,491M
    (2025, after the African bottlers moved to "assets held for sale", $5,342M); trademarks with indefinite lives
    $12,531M (2025). The trademark line carries BodyArmor after $1,720M of impairments.
  - **Cash and debt.** Cash and short-term investments $13,872M plus marketable securities $1,934M at 2025; debt on the face
    of the balance sheet $33,211M (2016, partial tag sum) and $45,492M (2025: loans and notes $1,551M, current maturities
    $1,822M, long-term $42,119M). Debt rose about $12 billion in nine years while owner cash was paid out in full (Q6).
  - **Receivables and inventory against sales.** Revenue rose 15% (2016 to 2025) while receivables fell 21% ($3,856M to
    $3,038M) and inventories rose 65% ($2,675M to $4,425M). The receivables are explained by the factoring program the
    filings disclose year by year (sold $185M in 2020, $21,873M in 2024, $14,710M in 2025). The inventories are partly
    explained: 2022's rise is "the buildup of inventory to manage potential supply chain disruptions" (FY2022 10-K), and
    the mix moved toward finished goods (fairlife dairy, Costa, BodyArmor) while bottlers left. "inventories look out of
    line, you know, with sales [...] you want to look twice" **[M1995-064]**: looked twice; disclosed, not hidden.
  - **Other noncurrent assets** $14,696M (2025) hold the $6.0 billion IRS deposit and $385M of accrued interest on it
    (FY2025 10-K, Item 3); that asset is worth its face only if the appeal succeeds.
  - What the figures cannot say **[M2025-032]**: the value of the equity stakes in the bottlers and Monster ($20,235M at
    equity-method carrying value), whose earnings arrive here only as dividends.
- **The real costs.** Depreciation is charged and is below capital spending (Q3); the D&A and capex bases are both
  carried. Stock pay ($279M in 2025) is expensed and deducted in owner cash, on the speakers' definition of earnings
  "after interest, taxes, depreciation, amortization and all forms of compensation" **[L2021-003]**. "Other operating
  charges" recur every year: $846M to $4,163M in 2016 to 2025, of which the "productivity and reinvestment program"
  alone was $97M to $164M a year in 2023 to 2025 (FY2025 10-K); owner cash already bears their cash part. Net income is
  swung by gains: "Significant (gains) losses, net" of $713M (2025) and $1,737M (2024) on the cash-flow statement
  (bottler and CCEP stake sales), and $217M of non-cash interest income on the IRS deposit in 2025 (Item 3); owner cash
  leaves both out, as the rows ask: "I would pay no attention to asset gains" **[M1998-040]** (for the test it states).
  Equity income ($2,031M in 2025) is counted only as the dividends received ($993M, equity income less the $1,038M
  "net of dividends" line), which is what operating cash already does (the framework's CONVENTION at Q4).
- **EBITDA in the filer's own mouth:** no instance found (a text search of the FY2025 10-K, the second-quarter 10-Q,
  the 2026 proxy and the second-quarter release returns zero).
- **The tells** **[M1995-064]**, **[L2016-006]**, **[L2002-041]**. (1) Adjusted earnings are featured: the release headline
  pairs "EPS Grew 16% to $1.03" with "Comparable EPS (Non-GAAP) Grew 11% to $0.97" (Ex 99.1, `0001628280-26-049922`).
  The adjustment cut the figure this quarter and removes gains as well as charges (asset impairments, transaction gains
  and losses, restructuring "when exceeding a U.S. dollar threshold", same exhibit), and GAAP is printed first; but
  restructuring is a recurring business cost, and telling owners year after year to set it aside "is misleading"
  **[L2016-007]**. (2) Annual guidance is given and raised ("Raises Full Year Guidance", same exhibit). No record of
  consistently meeting declared targets was assembled, so the make-the-numbers habit is not shown, only the guidance.
  (3) Working capital is financed (factoring, supplier finance), disclosed in each 10-K with amounts and costs ($60M in
  2025). No reserve release, no prepaid or deferred account building without explanation (the 2023 rise in prepaid
  assets is assets held for sale, FY2023 10-K), no profit on both sides of a contract was found.
- **VERDICT on confusion: IN** (the accounts are long but readable: the structural changes, gains, charges and the tax
  deposit are named and sized in the filings; nothing had to be guessed at to get owner cash) **[M1995-063]**,
  **[M2003-029]**. **WEIGHS slightly AGAINST**: adjusted figures and guidance in the release **[L2016-006]**, **[L2016-007]**,
  and operating cash flattered by financing the working capital (about $1.5 billion over the window if receivables had
  stayed at 2020's days, `owner_cash_output.txt`; a sensitivity, CONVENTION of this run, not deducted from the base). One
  tell plus guidance is not the two-tell suspicion of the framework's CONVENTION. The recast owner cash of Step 0 feeds
  Q7 **[M2012-034]**, **[L2021-003]**.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet **[M2007-081]**; the after-the-sale test belongs to whole
businesses, so the yardsticks and the reading tests carry this question.

- **Who.** James Quincey was chief executive from May 2017 and chairman from April 2019; Henrique Braun succeeded him as
  chief executive on 2026-03-31 and Quincey became Executive Chairman; the board separated the two roles at the
  succession; David B. Weinberg is Lead Independent Director (DEF 14A `0001104659-26-028215`). The chief financial officer,
  John Murphy, took the North America operating unit on an interim basis from 2026-08-01 (8-K `0001552781-26-000366`).
- **Yardstick 1, the record against the hand dealt** **[M1994-008]**. The hand is among the best in business (Q2). Under the
  2017 to 2025 management: unit cases 29.2 billion to 33.8 billion; operating margin 21.4% to 28.7%; the main rival's US
  share down eight points while KO's held (Q2); bottlers refranchised and the tangible capital shrunk (Q3). Against it,
  the purchases: BodyArmor ($5.6 billion, $1.72 billion impaired within four years) and a fairlife contingent payment that
  grew to $6.2 billion (Q3, Q6). The record is better on running the business than on buying businesses.
- **Yardstick 2, how they treat the owners** **[M1994-009]**. The proxy: the chief executive was paid $31,208,165 (2025),
  $28,002,284 (2024) and $24,742,908 (2023) (Summary Compensation Table, DEF 14A); 94% of it "performance-based" (same).
  Quincey beneficially owns 4,461,496 shares, of which 3,879,031 are exercisable options, so about 582 thousand shares
  outright (ownership table, same). No related-person transaction above $120,000 since January 2025 (same). The pay design
  is weighed at Q6, Part B.
- **The tells of dishonesty** (the framework's list under Integrity). Too good to be true: no instance found in the
  documents read. Reports that dance **[M2007-082]**: the key figures (unit cases, concentrate volume, price/mix, currency,
  structural changes) are reported every quarter in the same tables, including the bad ones (North America volume -1% in
  2025). Obfuscation **[M2003-029]**: none found (Q4). The stock price posted or chased **[M2004-067]**: the pay plan has
  a relative TSR modifier (Q6); no other instance found. Serial issuance **[L2014-015]**: none; shares outstanding flat for
  nine years (Q1).
- **How they talk about mistakes** **[L2024-003]**, **[M2010-081]**. The 10-K states the BodyArmor impairments as "revised
  projections of future operating results as well as higher discount rates resulting from changes in macroeconomic
  conditions since the acquisition date" (2024) and "lower expectations of future performance compared to the original
  forecasts" (2025) (FY2025 10-K, MD&A, critical accounting estimates): the second is close to plain admission; neither uses the word mistake. The tax
  case is argued as advocacy ("firmly believes that the IRS’ claims are without merit", Item 1A) while the downside is
  stated in dollars ($14 billion, 3.5 points), which is the candour that matters.
- **The letters and reports** **[M1998-038]**, **[M2007-083]**. The 10-K opens with a vision of "three connected pillars"
  ("Loved Brands", "Done Sustainably", "For a Better Shared Future") and the release with a FIFA campaign's "more than 60
  billion impressions"; "a standardized bunch of popular jargon that looks like it came out of the same consulting firm,
  I do think it’s a big turnoff" **[M1998-038]**. Under it the numbers are complete. A weighing on the people, not a tell
  of dishonesty.
- **Succession** **[L2011-001]**. Planned and announced (December 2025 board decision, DEF 14A); the successor came up
  through the system ("Since joining the Company in 1996", same). The North America head left four months after the
  succession and no successor is named yet (8-K `0001552781-26-000366`).
- **VERDICT on integrity: IN.** No tell of dishonesty found in the 10-Ks, the 10-Q, the proxy or the release; doubt alone
  would close it **[M2013-088]**, and the doubts found (jargon, adjusted figures, guidance) are about style and incentives,
  not truthfulness **[M2015-047]**. **Ability WEIGHS FOR** on running the business (volume, margin, share against the main
  rival) and **AGAINST** on buying businesses, which enters Q7 through "the degree of certainty that we attribute to the
  stream" **[M1999-104]**, **[L2010-002]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
The 1993 factors: "to wisely employ its cash flows" and "to channel the rewards from the business to the shareholders
rather than to itself" **[L1993-020]**.

### Part A: the money
- **Where the money went, FY2016 to FY2025** (cash-flow statements; `owner_cash.py`, `capital.py`). Owner cash as filed,
  capex basis, summed to about $73.0 billion (recast, $85.3 billion). Dividends paid were $72,857M; buybacks $16,855M
  before stock issued to employees; acquisitions (all legs) $24,616M in FY2017 to FY2025; disposals brought in $15,921M;
  debt on the balance sheet rose from $33,211M (2016, partial tag sum) to $45,492M (2025). The dividend alone took about
  all of owner cash as filed; buybacks and deals were paid from bottler sales and borrowing.
- **The retention test** **[R1995-009]**, **[M1998-110]**, **[M2011-072]**. Earnings retained FY2021 to FY2025 (reinvested
  earnings $66,555M at 2020 to $80,382M at 2025, filed equity statements) = **$13,827M**. Market value over the same five
  years: 4,309,311,676 shares (10-K cover, February 2021) at $54.84 (2020-12-31 close) = $236.3 billion; 4,300,723,069
  shares (February 2026) at $69.91 (2025-12-31) = $300.7 billion (closes from the aggregator cache, flagged,
  `prices_output.txt`): **+$64.3 billion, about $4.65 of market value per dollar retained**. The market leg passes, and
  not by a richer multiple on GAAP earnings (about 30 times in 2020, about 23 times in 2025, on net income over the cover
  share counts). Against intrinsic value, the caution of **[R2009-002]**: owner cash (recast) rose from $8,541M (2020) to
  $11,086M (2025), a gain of about $2.5 billion a year on $13.8 billion retained plus about $4.9 billion of added debt, much
  of it price on the old base (Q2, Q3). The forward question **[M2010-097]**: the business cannot use what it earns, and
  says so by paying it out; "it would be an enormous mistake for See’s Candy to retain money" **[M2008-104]** is the shape.
  **Weighs FOR** on retention, because little is retained and the payout fits the business **[M2004-089]**.
- **Buybacks** **[L1999-023]**, **[L2016-002]**, **[M2016-049]**. Stated policy: "During 2026, we also expect to repurchase
  shares to offset dilution resulting from employee stock-based compensation plans" (FY2025 10-K, MD&A); no price is
  named. Shares bought for treasury: 37M for $2,189M in 2023 (about $59 each), 27M for $1,702M in 2024 (about $63), 9M for
  $634M in 2025 (about $70) (filed equity statements). Buying to offset dilution is ruled out by name: "dilution by itself
  is a negative and buying back your stock at too high a price is another negative. So it has to be related to valuation."
  **[M2016-049]**; the 2014 row on the same practice names this company: "Some companies talk about — Coca-Cola does —
  they talk about buying in shares to cover options. That actually isn’t the best reason to buy in shares." **[M2014-008]**
  (a holder criticising its holding, used here for the rule). Under the framework's CONVENTION the programme with no
  stated price is read against the bottom of the Q7 range: **result recorded below, after Q7.**
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**, **[L2009-019]**. No stock issued for a deal; shares flat for nine
  years; **the one STOP (an all-stock deal by an undervalued acquirer) is not met.** Value given against value got, by
  deal: BodyArmor, about $5,600M in cash for the 85% it did not own (November 2021), then $760M and $960M of trademark
  impairments (2024, 2025): at least $1.72 billion more given than got, on the company's own fair-value tests. fairlife,
  bought outright in January 2020 with milestones "based on agreed-upon formulas related to fairlife’s operating
  results, the resulting value of which is not subject to a ceiling" (FY2025 10-K, Note 17): an uncapped earn-out, paid
  $100M, $275M and $6,173M; the price was set by fairlife's own success, so value got may match value given, but the
  company gave the seller an open-ended option on the result ("you never want to give an option" **[M2013-076]**). Costa,
  $4.9 billion in cash (2019): no impairment found, and coffee volume fell 2% in the second quarter of 2026 (Ex 99.1). The
  bottler sales (refranchising: Philippines, Bangladesh, parts of India in 2025; Africa agreed with CCHBC, closing expected
  by the end of 2026, 10-Q `0001628280-26-050503`) release low-return capital at gains, which is the right direction.
  Post-mortems against the original projections **[L2014-013]**: no instance found in the 10-K or proxy text read.
- **Part A WEIGHS AGAINST, narrowly**: the dividend policy fits a business that cannot use its earnings **[M2004-089]**,
  but buybacks are run to offset dilution at no stated price **[M2016-049]**, **[M2014-008]**, and the large purchases of the
  decade gave more than they got in the one case the company has written down **[M1995-001]**, **[L2014-012]**.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls** **[M2003-019]**. The annual incentive's business factor is "50% for overall
  Company net operating revenue growth and 50% for overall Company operating income growth", on comparable currency
  neutral measures with targets "at the midpoint of the Company’s publicly stated long-term growth plan of 4% to 6% for
  organic revenue (non-GAAP) growth and 6% to 8% for comparable currency neutral operating income (non-GAAP) growth"
  (DEF 14A). The performance share units weigh revenue growth, EPS growth and three-year free cash flow equally, adjusted
  to exclude significant acquisitions, divestitures and "impacts resulting from the application of the tax court rulings",
  with a relative TSR modifier (same). For: currency is taken out, which the managers do not control, and acquisitions
  are taken out, so a purchase does not raise pay. Against: no capital charge appears anywhere in the measures (the
  rows' "a batting average that does not include a cost of capital is a phony batting average" **[M1995-010]**); the
  comparable measures exclude impairments, so the BodyArmor write-downs did not touch pay ("Heads I win, tails you lose"
  is the test, **[L1994-020]**); currency-neutral revenue growth counts "inflationary pricing in Argentina" (FY2025 10-K)
  as growth, and no adjustment for it was found in the proxy (text search for "Argentina", "hyperinflation",
  "inflationary": none); the TSR modifier pays on the stock price, which the managers do not control. The 2023-2025 PSU
  programme "exceeded the maximum performance levels" on every financial measure and was certified at 229% of target
  (DEF 14A).
- **The proxy itself** **[M1994-009]**, **[M2009-087]**. Chief executive pay $31.2M (2025); a comparator group and a
  compensation consultant are used ("Benchmarked compensation program designs and pay opportunities against the
  compensation comparator group", DEF 14A), the ratchet the rows name **[L2005-015]**, **[M2012-095]**. The compensation
  discussion runs over many pages (the Summary Compensation Table is on page 64 of the proxy). Options are granted with a
  four-year vesting and no step-up for retained earnings **[L1994-021]**; the dividend conflict is small here because the
  company pays most of its earnings out, and the proxy does not name it (no instance found) **[L2005-014]**.
- **The board** **[M2007-120]**, **[L2014-026]**. Chairman and chief executive were one person from 2019 to March 2026; the
  roles are now split, with the former chief executive as Executive Chairman, and a Lead Independent Director (Weinberg)
  who with his family owns 9,248,693 shares; director Allen 19,282,444 shares (largely through Allen & Company and family)
  (DEF 14A). Most other directors hold between about 1,100 and 23,600 shares directly, plus deferred share units credited
  as a $200,000 annual equity retainer that are granted, not bought **[L2019-008]**, **[L2002-033]**. One director, Christopher
  Davis, sits on the board of Berkshire Hathaway, the 9.3% holder (400,000,000 shares, DEF 14A): noted for the
  contamination record.
- **Owners as partners, by inversion** **[M2022-054]**, **[L1994-023]**. Guidance is given and raised (Ex 99.1); the reporting
  is full and identical for every holder (8-K releases, 10-Q). The 64th consecutive annual dividend increase (DEF 14A) is a
  commitment kept.
- **Part B WEIGHS AGAINST, mildly**: the measures avoid the worst faults (currency and acquisitions are taken out) but
  carry no charge for capital, leave impairments and hyperinflation pricing out of the reckoning, and are benchmarked to
  peers **[M1995-010]**, **[L1994-020]**, **[L2005-015]**; the proxy shows no self-dealing **[M1994-009]**.

## Q7: WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate (which we consider to be the yield on long-term U.S. bonds)?" **[L2000-021]**, answered as a
range **[L2000-024]**. Arithmetic in `q7_calc.py`, output `q7_calc_output.txt`.

- **How much cash** (the framework's CONVENTION: five-year average of owner cash after every real cost **[L2021-003]**,
  **[L2005-003]**). FY2021 to FY2025, capex basis, recast as in Step 0 (fairlife purchase price and the IRS deposit added
  back): **$10,260.0M a year** (D&A basis $10,842.8M; as filed $7,812.8M). The equity-method stakes count only through
  the dividends they paid, which are inside operating cash (Q4).
- **How soon, and the growth shown** (on the aggregate, never per share; CONVENTION). Owner cash, recast capex basis,
  $10,921M (2021) to $11,086M (2025): **0.38% a year**. The window opens on a base raised by the start of factoring (Q3),
  so variants are shown beside it, not chosen: D&A basis 2.90%; unlevered after-tax 1.99%; pre-tax unlevered 3.20%. No
  rate past the discount rate **[M1997-095]**; Q3 found the incremental capital earning little, so nothing above the
  shown growth is carried in the range.
- **The rate:** 5.66%, the 30-year Treasury, 2026-10-05 **[M1996-025]**.
- **How sure.** The business is about as sure as any in the shelf's examples (Q1, Q2); the uncertainties are the tax case
  and the slow health and regulatory threats (Q2, test 11). Certainty enters the discount from value, not the rate
  **[M1997-126]**, **[M1999-104]**.
- **The range** (ten years at the growth input, then zero nominal growth, discounted throughout at 5.66%; levered owner
  cash, so the result is the equity):

| case | equity | per share |
|---|---|---|
| **no growth (bottom)** | $181,272M | **$42.13** |
| **shown growth, 0.38% (top)** | $186,736M | **$43.40** |
| variant: D&A basis, no growth / shown 2.90% | $191,569M / $240,999M | $44.52 / $56.01 |
| variant: unlevered, less net debt of $27,172M, no growth / shown 1.99% | $171,949M / $205,943M | $39.96 / $47.87 |
| variant: as filed, no growth | $138,035M | $32.08 |
| generous, above the growth shown: 2.0% / 4.0% / 5.5% for ten years | $212,367M / $248,864M / $280,295M | $49.36 / $57.84 / $65.15 |
| stress: tax case lost at the company's own figures ($14 billion now, 3.5 points on the tax rate), no growth | $159,284M | $37.02 |

  Net debt $27,172M at 2026-07-03 (debt $43,543M less cash, short-term investments and marketable securities of
  $16,371M; 10-Q `0001628280-26-050503`). **Width: top over bottom 1.03**, far inside the three-to-one line, so the range is
  narrow enough to decide on; even the widest pair of variants above (as filed against the generous 5.5% case) is about
  two to one.
- **The floor** (the framework's CONVENTION: about ten percent pre-tax on the price paid, "we don’t want to buy equities
  where our real expectancy is below 10 percent" and "And it’s arbitrary." **[M2003-149]**; "at least 10% pre-tax returns"
  **[L2002-020]**; a guess at "future opportunity cost" that a lasting change in long rates would move **[M2003-151]**,
  and cheap money moved what they paid "a little" **[M2016-078]**). On the all-equity basis (price paid = market cap
  $372,214M + net debt $27,172M = $399,386M) and the pre-tax unlevered owner cash ($14,196.0M a year): expected pre-tax
  return **3.55%** with no growth, **3.67%** at the shown growth, **4.62%** at the pre-tax series' 3.20%, and **5.51%** even at
  the generous 5.5% for ten years. After tax, levered, on the market value: 2.76%. Every case is below the 5.66% bond as
  well as below the floor.
- **COMPUTATION, NOT A CLEARANCE: the prices at which the floor is met.** "Cheap" (no-growth owner cash clears 10%
  pre-tax): **$26.68 a share**. "Fair" (the central case, shown growth 0.38%, clears 10%): **$27.53 a share**; on the
  pre-tax series' 3.20% growth, $34.73.
- **Reading it.** The price, $86.51, is about **two times the top of the range** ($43.40) and above every variant, including
  growth well beyond what the record shows ($65.15). A price above the top of the range "closes OUT through the floor
  convention above, the expected return at the price then being below the minimum" (Q7, the PG specifics). This is not
  a close call that needs a pencil **[M2009-005]**, **[M1996-084]**; it is a price at which the business would have to grow
  owner cash at more than the discount rate for many years to earn the floor, which is the arithmetic the rows send away
  **[M1997-095]**, **[M1999-067]**. Nor is it a case for a wider margin on a fuzzy range **[M2007-022]**: the range is narrow.
- **VERDICT: OUT.** Valued, and the price does not clear the floor: "there’s just a point at which we drop out of the
  game" **[M2003-149]**; the price is not "a reasonable price in relation to the bottom boundary of our estimate"
  **[L2013-012]**. The castle stands (Q2 IN); the price is the reason.

**Recorded back at Q6 (the buyback test, run now that Q7 has a range).** The bottom of the range is $42.13. Shares were
bought for treasury at about $59 (2023), $63 (2024) and $70 (2025), all above it; under the CONVENTION the programme with
no stated price therefore **weighs against** **[L2016-002]**, **[L1999-023]**, and Part A's verdict stands.

## Q8: IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (closed OUT at Q7). For the record only, not a clearance: at the price, every case of Q7 expects less before
tax (3.55% to 5.51%) than the 30-year Treasury pays (5.66%), so the bond, the first filter, would take it "out of the
filter" too **[M1997-089]**.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a verdict (the run closed at Q7). Facts gathered on the way, headed as computation and not weighed: debt
$43,543M against cash and securities of $16,371M at 2026-07-03 (10-Q `0001628280-26-050503`); long-term debt rated "A+"
and "A1", commercial paper "A-1" and "P-1" (FY2025 10-K, MD&A); the tax dispute's company-stated downside of about $14
billion plus 3.5 points on the tax rate, beside $6.4 billion already paid (Item 3); a trade receivables factoring program
and a supplier-finance program whose withdrawal would reverse part of the working-capital benefit (Q4); fairlife's United
States production suspended by ransomware, impact "not yet known" (8-K `0001628280-26-048466`). The "little or no debt"
criterion **[R1997-001]** is stated for whole businesses and was not applied.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. What the draft would have the buyer do: nothing. "your default position is always short-term instruments.
And whenever you see anything intelligent to do, you should do it." **[M2004-045]**; a wonderful business at twice the top
of its range is not a pitch to swing at **[L1997-006]**.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (closed at Q7). For the record only: sweetened drinks are not among the businesses the rows name for the STOP
(casinos, tobacco made and sold, distributor loading, gambling dressed as investing); the 10-K itself lists "ongoing
public concern about obesity" among its risks (Item 1A), which the newspaper test **[M2008-011]** would weigh; not weighed
here.

---
## THE BOX
**OUT, at Q7 (valued; the price does not clear the floor). Value range $42.13 to $43.40 a share (variants $32.08 to $65.15)
against a price of $86.51.** Q1 IN, Q2 IN (the castle stands, and the main rival's own filing says so), Q3 weighs for on
the business and against on the money put in by purchase, Q4 IN on confusion and weighs slightly against, Q5 IN on
integrity, Q6 weighs against in both parts. At the price the expected return is about 3.6% to 4.6% pre-tax, below the
bond. COMPUTATION, NOT A CLEARANCE: "fair" (central case clears 10% pre-tax) $27.53; "cheap" (no-growth case clears it)
$26.68. Not TOO HARD, so no research pass is opened. **What would reverse it:** a price at or below about $27.53 with
Q1 to Q6 unchanged, or filed owner cash that grows enough to lift the range (pre-tax owner cash would have to rise nearly threefold, from about $14.2 billion to about $40 billion,
at today's price to make 10% pre-tax), re-run from Q7.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy was made, and the research folder created, before `tools/run.py`
      or any EDGAR request); written question by question; committed after Step 0, Q1, Q2, Q3, Q4, Q5, Q6, Q7 and at the
      close (`git log` on this file).
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment followed by an id is a substring of that
      row's quote (`check_ids.py`, run before each commit); every filing fact carries its document and accession or
      names the 10-K year whose accession is listed in Step 0; numbers that come from neither a filing nor a row are
      labelled CONVENTION (the framework's or this run's) or flagged as aggregator data (the price, the year-end closes).
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8, Q9, Q10 and Q12 are NOT REACHED,
      with facts headed as record or computation only; the fair and cheap prices are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (OCF less stock pay less capital spending, as filed, with the D&A basis beside
      it), never a net-income proxy (operator rule 5); the recast (fairlife price and IRS deposit added back) is labelled
      a CONVENTION of this run and shown beside the as-filed figure in every table. Net income is used only in the
      retention test, which is about earnings retained. The sovereign is the US Treasury's 30-year par yield, from the
      issuing authority; aggregator quotes flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (six items under the foundations, and the
      contrary half of each Q2 test).
- [x] No row dated after the anchor is cited in a point-in-time run: not a point-in-time run (today's run).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII): its price, share count, the filed OCF, SBC, capex,
      D&A and balance-sheet lines; its three-year mean, its "growth the price assumes" and its v4 material were not used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The shelf is a holder of this name, and the framework has no procedure for that.** The speakers have owned Coca-Cola
since 1988; 149 rows of the v5 ledger contain "Coca", and the framework uses some of them as rules (the key variables of
**[M1998-040]**, the money test of **[M1997-103]**, the low-bid test of **[M2008-076]**), and one 2014 row criticises this
company's own buyback practice **[M2014-008]**. A director of KO sits on Berkshire's board. The dispatch's blind rule can
bar earlier run files but cannot bar the shelf. The foundations carry "Berkshire has a dog in this fight" **[L2009-015]**
as a habit, not a procedure. What was done: rows about Coca-Cola were cited only for the test they state, never as
evidence about KO, and every finding came from KO's and its competitors' filings. A short rule for runs on names the
speakers held or discussed would help. (2) **The five-year average and one-off cash in operating activities.** The Q7
CONVENTION averages owner cash "after every real cost" but says nothing about an acquisition price that GAAP routes
through operating cash (the $6.1 billion fairlife earn-out) or a refundable tax deposit ($6.0 billion). Left in, they cut
the average from $10.3 billion to $7.8 billion; I recast and showed both, and the verdict is the same either way, but two
analysts could reach very different ranges. (3) **The growth input and a financed base year.** "The growth shown" measured
from the window's first to last year is sensitive to working-capital financing: KO's factoring program started in 2021,
the window's first year, raising the base. The framework has no line on factoring or supplier finance in the owner-cash
figure; I showed a sensitivity (about $0.3 billion a year) without deducting it. (4) **Pricing power in hyperinflation.**
Q2's pricing test and Q6's pay test both read price/mix and currency-neutral growth, which count inflationary pricing in
Argentina as price; the framework gives no way to separate pricing power from inflation pass-through, so I used North
America, a hard-currency market, as the clean test. (5) **The floor's basis** (equity or enterprise) is still unstated, as
the PBH run found; here it does not matter (2.76% after tax on the equity, 3.55% pre-tax on the enterprise, both far below).
(6) **"Fair" and "cheap" prices** are asked for by the dispatch but are not defined in the framework; I defined them as the
prices at which the central and no-growth cases clear the 10% pre-tax floor on the enterprise basis, labelled
COMPUTATION, NOT A CLEARANCE.
