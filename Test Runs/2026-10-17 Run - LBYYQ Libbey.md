# Company Run — LIBBEY INC. (OTC: LBYYQ; formerly NYSE American: LBY; SEC CIK 0000902274) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure: the lines of evidence were
derived by the analyst from the FY2019 10-K's Item 1, Item 1A and Item 7 (named below). Every judgment cites a v5 ledger id in
bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked
NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (47cb5815): `PORTFOLIO.md` read for this one ticker; the operator does not hold LBYYQ (no line names LBYYQ, LBY or Libbey).*

**CONTAMINATION, declared before any verdict.** (1) At the start, to confirm the dated file did not already exist, I listed
`Test Runs/` filtered for "LBY" or "libbey"; the filter returned nothing. That listing is a search the blind rule forbids, and it
is declared here; it showed no file name. (2) The session context showed the repository's git status (other research folders,
e.g. AYI and ARCB) and five recent commit subjects about another company (HWDJY); and a memory index line about queue state
("57 gate-clearers, nothing buyable"). None names Libbey; none was used. (3) No `PORTFOLIO.md`, holding review, `RESUME STATE`,
register, reading list or other company's run file was opened.

**The research folder:** `Test Runs/_research 2026-10-17 LBYYQ/` (filings as text in `filings/`, the one rival in `peers/`,
scripts in `scripts/`, the tool output in `run_py_output.txt`, the computation in `q7_computation_output.txt`).

**The lines of evidence, chosen from the FY2019 10-K (accession 0001437749-20-003729):**
- From **Item 1 (Business, Competition)**: (i) the competitive position in the U.S. & Canada segment, which the filer calls
  "leading market share" and the "leading market share in glass tableware sales in the U.S. and Canadian foodservice channel";
  (ii) the filer's own account of the field: "broad scale industry overcapacity among glass tableware manufacturers" and "the
  ease with which foreign manufacturers can sell products into the U.S. at competitive prices"; (iii) the named rivals.
- From **Item 1A (Risk Factors)**: (iv) the cost position, "Our labor and energy costs also may be higher than those of some
  foreign producers of glass tableware"; (v) the debt and its maturities (Term Loan B due 2021-04-09, ABL springing maturity
  2021-01-09); (vi) the unfunded Mexican pension ($41.3 million).
- From **Item 7 (MD&A)**: (vii) the segment results (Segment EBIT by segment, 2017 to 2019, and back to 2013 from the earlier
  10-Ks); (viii) the 2019 drivers the filer names ("global competition in all of our distribution channels", "continued
  declines in U.S. & Canada foodservice traffic", Chinese manufacturers diverting sales to Latin America); (ix) the featured
  non-GAAP figures (Segment EBIT, Adjusted EBITDA).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **no quote found.** The tool's aggregator returned HTTP 404 for LBYYQ on 2026-10-17; Yahoo's chart endpoint
  returned "No data found, symbol may be delisted"; the OTC Markets endpoint returned "Temporarily Unavailable". The issuer's
  own last word on the quote: "The Company’s common stock may continue to be quoted on the OTC Pink marketplace, but under the
  terms of the Plan, the common stock has no underlying asset value" (8-K filed 2020-11-16, accession 0001437749-20-023926).
- **Shares by class:** one class, common, $.01 par. 22,667,869 shares at 2020-07-31 (10-Q cover, filed 2020-08-10, accession
  0001437749-20-017281) and the same 22,667,869 "As of November 12, 2020" (8-K of 2020-11-16, accession 0001437749-20-023926),
  which states that all of them, with restricted stock and units, "were cancelled, discharged and of no force and effect" on
  the effective date, 2020-11-13. `python Screens/cover_shares.py LBYYQ` returned "NOT AN SEC REGISTRANT in the live ticker
  file"; the count is read from the filed cover and the 8-K instead. The FY2019 10-K cover gave 22,361,002 at 2020-02-20; the
  rise to 22,667,869 is vesting of share pay in 2020 (the 10-Q cover). Shares outstanding today that carry a claim on Libbey:
  **none**, by the plan.
- **Market cap:** not computable (no quote); the claim it would price is nil by the plan.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield of the US Treasury daily par yield curve,
  2026-10-16, as fetched by `tools/run.py` (issuing authority). Most sales are in USD (the 10-K: "approximately 78 percent of
  our sales were to customers located in North America (U.S., Canada and Mexico)"); the earnings currency is the reporting
  currency.
- **Filings read** (operator rule 4): 10-K FY2019 (filed 2020-02-27, accession 0001437749-20-003729): Item 1, Item 1A, Item 7,
  the cash-flow statement, note 19 (segments). 10-K FY2018 (filed 2019-02-27, accession 0000902274-19-000033), FY2016 (filed
  2017, accession 0000902274-17-000034) and FY2015 (filed 2016, accession 0000902274-16-000250): segment tables. 10-Q for the
  quarter to 2020-06-30 (filed 2020-08-10, accession 0001437749-20-017281): statements, going-concern note, liabilities subject
  to compromise. Proxy DEF 14A (filed 2020-04-01, accession 0001437749-20-006778): pay measures. 8-K of 2020-06-01 (Chapter 11,
  accession 0001437749-20-012113), 8-K of 2020-10-20 (confirmation, accession 0001437749-20-021322), 8-K of 2020-11-16
  (effective date, accession 0001437749-20-023926), Form 15-12B of 2020-11-16 (accession 0001437749-20-023937). No SEC filing
  after 2020-11-16 (EDGAR submissions index, read 2026-10-17).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities 2019, $63,432 thousand,
  and cash paid for property, plant and equipment 2019, $31,159 thousand, read on the face of the FY2019 cash-flow statement;
  `tools/run.py` transcribed 63.4 and 31.2. They agree.
- `tools/run.py`: the ticker is gone from the SEC ticker map ("LBYYQ: not an SEC filer"), so it was driven by CIK 0000902274
  through `scripts/run_cik.py`, with a placeholder price of 1.00 so the filed-figure lines would print; **every line that uses
  the price (yield, implied growth, points over the sovereign, market cap) is void and not used.** Arithmetic lines used, USD
  millions (owner cash = operating cash less stock pay less capital spending):

  | FY | OCF | stock pay | D&A | capex | owner cash (capex basis) | owner cash (D&A basis) |
  |---|---|---|---|---|---|---|
  | 2015 | 69.7 | 5.9 | 42.7 | 48.1 | 15.6 | 21.1 |
  | 2016 | 83.9 | 4.8 | 48.5 | 34.6 | 44.5 | 30.7 |
  | 2017 | 45.3 | 3.5 | 45.5 | 47.6 | -5.8 | -3.7 |
  | 2018 | 36.9 | 2.8 | 44.3 | 45.1 | -11.0 | -10.3 |
  | 2019 | 63.4 | 3.2 | 39.0 | 31.2 | 29.0 | 21.2 |
  | mean | | | | | **14.5** | 11.8 |

  The tool found no securities flows inside operating cash, no other stock-pay line, no intangible or software payment beside
  capex. Stock pay resolved and complete (ShareBasedCompensation each year). The window's last year is FY2019: the business
  filed no annual report after it, and H1 2020 is in the 10-Q only.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, bought for what "the asset, itself, produces" and "Not by
selling it to somebody else" **[M1997-052]**; the test is "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**. A LBYYQ certificate is, on the issuer's own filing, a cancelled claim: the shares "were cancelled,
discharged and of no force and effect" and "the common stock has no underlying asset value" (8-K, 0001437749-20-023926).
Anything paid for it would be paid on "what somebody else will pay you for it later on, irrespective of what the asset
produces", which the rows call speculation **[M2002-078]**; it is the Frozen Corporation in its plainest form, an instrument
that can never pay its holder **[M1998-084]**. The foundations admit and reject nothing; this is recorded here and carried to
Q7, where it is the whole of the value. The business behind the old ticker (Libbey Glass, now a private subsidiary of the former
lenders, per the same 8-K) is what Q1 and Q2 examine. **Contrary evidence, written down as found** **[M1997-127]**: (1) the
filer claims "leading market share" in U.S. and Canadian foodservice glass and "a leading share of the U.S. retail market for
glass beverageware" (10-K FY2019, Item 1); (2) the U.S. & Canada segment's EBIT rose from $36.8 million in 2018 to $54.1
million in 2019 (10-K FY2019, MD&A); (3) gross margin rose 30 basis points in 2019 and operating cash rose $26.6 million (same).
Each is weighed at Q2.

## THE STANDING RULE
Owning LBYYQ puts no buyer at risk of ruin unless it is bought with borrowed money; the rule binds the buyer's conduct, "borrowed
money has no place in the investor's tool kit" **[L2014-005]**, and "Never risk permanent loss of capital." **[L2023-005]**. A
security the issuer says has "no underlying asset value" is, for whatever is paid, a permanent loss on the filing's own words;
that is a Q7 fact, not a ruin to the buyer at any sane size. No breach found.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The object.** The security carries no claim (foundations, above); Q1 is asked of the business the filings describe, glass
  tableware made in six plants (Toledo, Shreveport, Monterrey, Leerdam, Marinha Grande, Langfang) and sourced ceramic and
  metal tabletop, sold to foodservice distributors, retailers and business-to-business buyers (10-K FY2019, Item 1).
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**.
- **The key variables and how predictable they are** **[M1998-044]**: (1) unit volume in U.S. foodservice, which the filer ties
  to restaurant traffic it reports as in "continued declines" (Item 7); (2) the price it can hold against imports, which the
  filer ties to "broad scale industry overcapacity" and the dollar (Item 1); (3) its cost of labor and energy against foreign
  producers (Item 1A); (4) currency (peso, euro, renminbi; Item 1A); (5) debt service (Item 1A). None is a technology bet.
  The product is a tumbler and a stem; the forecast is about customers, price and cost, the kind the rows can make
  **[M2017-019]**.
- **Do the past statements tell me the future ones?** **[M2008-033]**: yes, in direction. Ten years of filed statements (sales
  $799.8 million in 2010, $782.4 million in 2019; operating income between $63.5 million and $81.3 million in each year 2010 to 2014, then
  $43.7 million (2015), $45.3 million (2016), a loss of $53.7 million (2017), $27.0 million (2018), a loss of $33.3 million
  (2019); XBRL OperatingIncomeLoss, first-filed vintage) tell a reader where earning power and
  position were heading; Q2 reads what they show.
- **Would the insiders write it down?** **[M2000-105]**: the filer did. Its 10-K writes the next year down in plain words,
  "Management expects these trends, and the challenging environment to continue into 2020" (Item 7). The forecast is
  "important and knowable" **[M2006-076]**.
- **Contrary facts on Q1, written down as found** **[M1997-127]**: the business has filed nothing since 2020-11-16; its
  statements for 2020 to 2026 are not public, and it is now owned by the former lenders. Its ten-year future can be judged only
  from the 2010 to mid-2020 record. That makes Q1 a judgment on the economics of the field and of this maker in it, which the
  record does show, not on the present accounts of a private company.
- **Doubt test** **[M2002-092]**: no doubt that the economics of a mature glass-tableware maker are inside the perimeter; the
  doubt in this file is about the castle and the claim, which belong to Q2 and Q7.
- **VERDICT: IN.** The economics are foreseeable from the filings: a mature product, a known set of variables, a filer that
  writes its own outlook down **[M2012-065]**, **[M1998-044]**, **[M2000-105]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10,
20 years from now." **[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (Segment EBIT as the filer reports it, before retained corporate costs of about $32 million a year; USD
millions; 10-Ks FY2015 0000902274-16-000250, FY2016 0000902274-17-000034, FY2018 0000902274-19-000033, FY2019
0001437749-20-003729):

| part | 2015 | 2016 | 2017 | 2018 | 2019 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| U.S. & Canada | 80.4 | 77.9 | 48.0 | 36.8 | 54.1 | 297.2 | 80% | shown open (below) | **yes** (more than half) |
| Latin America (Mexico) | 22.0 | 10.7 | 6.6 | 12.6 | 6.2 | 58.1 | 16% | shown open: $79.7 million goodwill impairment of the Mexico unit in 2017 and $46.0 million more in 2019; filer cites Chinese makers diverting sales there | no |
| EMEA | 1.3 | -1.0 | 1.3 | 7.2 | 5.5 | 14.3 | 4% | none shown; $19.2 million asset impairment in 2019 | no |
| Other (China) | 4.4 | 0.9 | -3.8 | 1.9 | -2.7 | 0.7 | 0% | none shown | no |
| total | 108.1 | 88.6 | 52.1 | 58.5 | 63.1 | 370.4 | | | |

The file closes on U.S. & Canada (the business of parts, Q2; **[L2008-005]**).

**U.S. & Canada over the whole span** (segment sales are consolidated net sales less the other segments, from the same tables):

| | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | H1 2019 | H1 2020 |
|---|---|---|---|---|---|---|---|---|---|
| segment sales | 459.6 | 482.1 | 497.7 | 488.2 | 481.8 | 483.7 | 491.2 | | |
| Segment EBIT | 76.4 | 72.5 | 80.4 | 77.9 | 48.0 | 36.8 | 54.1 | 27.1 | -13.7 |
| margin | 16.6% | 15.0% | 16.2% | 16.0% | 10.0% | 7.6% | 11.0% | | |

(H1 from the 10-Q, 0001437749-20-017281. The 10.0%, 7.6% and 11.0% margins are the filer's own figures in MD&A.)

**The castle tests, each with its filing fact.**
- **The attacker with money; one competitor can be enough** **[M2011-015]**, **[M2012-108]**: the filer names the attack itself,
  "broad scale industry overcapacity among glass tableware manufacturers" and "the ease with which foreign manufacturers can sell
  products into the U.S. at competitive prices" (10-K FY2019, Item 1). The castle is being entered, on the filer's word.
- **The low-cost position** **[M1997-010]**, **[M2001-013]**: the filer says it is not the low-cost producer against the
  importers: "Our labor and energy costs also may be higher than those of some foreign producers of glass tableware" and "some of
  our competitors may have greater financial and capital resources than we do and continue to invest heavily to achieve increased
  production efficiencies" (Item 1A). This is the business the rows name and refuse: "we do not want to buy into a business that
  has a very high labor content and that has a product that can be shipped in from abroad very easily. Because, sooner or later,
  that will probably be trouble" **[M2007-116]**. The filer employed 5,872 people at 2019 year-end; "The majority of our
  employees are paid hourly and covered by collective bargaining agreements" (Item 1).
- **The low bid** **[M2017-009]**: the filer's own list puts "price" among the "principal competitive factors" and says
  "Advantages or disadvantages in any of these competitive factors may be sufficient to cause the customer to consider changing
  providers of the kinds of products that we sell" (Item 1A). A customer who changes provider on any one factor, price among them,
  is the customer who takes the low bid.
- **Pricing power and the agony before a rise** **[M2005-020]**: the filer lists inflation that would force it "to increase the
  prices of our products in order to maintain their profitability" as a threat to its "cost-competitiveness" (Item 1A); in 2018
  its core channel, U.S. foodservice, "declined $3.0 million, driven by an unfavorable price and mix of product sold" (10-K
  FY2018, MD&A). In 2019 price and mix were favourable in U.S. & Canada (10-K FY2019, MD&A): contrary evidence, recorded. One year
  of favourable price after two years of falling segment profit does not show a business that raises price without the prayer
  session.
- **Unit volume**: the filer's own words, foodservice volume lower in 2019 and "continued declines in U.S. & Canada foodservice
  traffic" (Item 7). Share is claimed ("leading market share", Item 1) and not shown to hold the margin: segment sales held at
  $482 million to $498 million from 2014 to 2019 while segment EBIT fell from $80.4 million (2015) to $36.8 million (2018) and
  $54.1 million (2019).
- **The brand in the customer's mind**: the brands are said to "enjoy a high degree of consumer recognition" (Item 1, Patents,
  Trademarks and Licenses). The claim is the filer's; it does not show in price (above).
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**: narrowing. The deciding part earned 15.0% to 16.6% on its sales in
  2013 to 2016 and 7.6% to 11.0% in 2017 to 2019; the company's operating margin before impairments averaged 8.9% in 2010 to
  2014 and 4.4% in 2015 to 2019 (XBRL OperatingIncomeLoss with the filed impairments of $79.7 million in 2017 and $65.2 million
  in 2019 added back; `scripts/returns.py`). This is the notch lost **[L1995-023]**.
- **Ask the competitors**: the one named rival that filed with the SEC described the same field in the same words (below).
- **What could destroy it** **[M2000-014]**: cheaper imported glass, as above; the filer also lists plastic and melamine as
  substitutes (Item 1).

**The competitor row.** The 10-K names Arc International (France), Paşabahçe (a unit of Şişecam, Turkey), Anchor Hocking (U.S.),
AnHui DeLi Glassware (China), Vicrila (Spain), Oneida Hospitality Group and Steelite (Item 1). **Flagged: none files with the SEC
today.** An EDGAR entity search on 2026-10-17 found no filer named Vicrila, Steelite, Paşabahçe, AnHui DeLi or Anchor
Hocking; the "ARC International PLC" and "ARC International Corp" entities it returned were not shown to be the French
glassmaker, and the Şişecam entities it returned (Sisecam Resources LP, Sisecam Chemicals USA Inc.) are not the tableware
business by their names; "ONEIDA LTD" is a former filer whose filings were not read. None was used. Anchor Hocking and Oneida filed through **EveryWare Global, Inc.** (CIK 0001532543) for FY2012 to
FY2014 only; it is the one rival with SEC filings and the only competitor row available.

| | metric | 2012 | 2013 | 2014 | source |
|---|---|---|---|---|---|
| Libbey | operating income / net sales | 9.9% | 8.9% | 9.5% | XBRL, Libbey 10-Ks (accessions in `run_py_output.txt`) |
| EveryWare Global (Anchor Hocking, Oneida) | operating income / net sales | 4.6% (19.1 / 414.8) | 3.7% (14.7 / 401.1) | -10.4% (-36.3 / 347.6) | 10-K FY2013 0001532543-14-000020; 10-K FY2014 0001532543-15-000014 |

EveryWare's FY2014 10-K, filed 2015-04-14, carries the same sentence about the field, "Our labor and energy costs also may be
higher than those of some foreign producers of glass tableware", adds "our products may be subject to competition from low-cost
imports that intensify the price competition faced in various markets", names "Libbey, Inc. and Arc International" as
competitors, and carries an auditor's "substantial doubt" paragraph; its 8-K of 2015-04-08 (0001193125-15-122107) reports Chapter
11 petitions filed 2015-04-07, and it filed Form 15 on 2015-05-13 (0001193125-15-186071). The comparison over the span the
filings allow: Libbey earned about twice the rival's margin in 2012 and 2013; the rival failed in 2015; Libbey's own margin
before impairments then fell to 3.3% to 5.7% in 2015 to 2019, near the rival's 2012 to 2013 level, and Libbey filed Chapter 11 on
2020-06-01 (8-K 0001437749-20-012113). Three overlapping years are the most the filings give; it is not a full cycle.

**The field's returns over the last full cycle** (section C): the field's two U.S. makers that filed with the SEC both went through
Chapter 11 inside six years, EveryWare in 2015 and Libbey in 2020, and Libbey's equity holders received nothing (8-K
0001437749-20-023926). Libbey's own decade: net income summed to $40.2 million over 2010 to 2019 on sales of about $8.1 billion;
retained earnings were a deficit at every year-end from 2010 (-$178.7 million) to 2019 (-$240.5 million); shareholders' equity
was $11.3 million in 2010, $148.4 million at its best (2015) and -$25.8 million in 2019 (balance-sheet table,
`run_py_output.txt`). Pre-tax operating income before impairments on tangible equity plus net debt ran 23% to 36% in 2010 to 2014
and 8% to 15% in 2015 to 2019 (`scripts/returns.py`; the denominator leaves out the pension and retiree liabilities and the
equity was thinned by past losses, so these figures flatter). Judged in words, as the rows say the moat is judged
**[M1999-108]**: not excellent returns protected, but returns falling toward poor, in a field where "you can have only two
competitors and they’re still terrible businesses" **[M2013-052]**.

**Contrary evidence weighed.** The leading share in U.S. foodservice glass, the 2019 rebound in the deciding part to 11.0%, the
30-basis-point rise in gross margin in 2019 and the $26.6 million rise in operating cash (Item 7) are real. Against them: the
rebound left the deciding part below every year of 2013 to 2016; 2019's operating cash included $16.5 million from smaller
inventories and $9.2 million from larger payables (cash-flow statement); and the filer itself expected "the challenging
environment to continue into 2020". The 2020 collapse (H1 2020 net sales $228.1 million against $381.1 million, gross profit $2.9
million against $80.7 million; 10-Q) came from the pandemic and is not counted against the castle; the decline before it is.

**Why it closes OUT and not TOO HARD.** The castle's future is not unknowable: the filer, its one filing rival and ten years of
statements say the same thing, that imports with lower labor and energy costs set the price, and the deciding part's returns fell
by about a third while its sales held. "you do not want to have something whose competitive position is going to erode over
time." **[M2007-117]**; "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; "sooner or later,
the nature of a capitalist society is that the guy with the lower cost comes in and kills you." **[M2001-013]**. The framework
sends the high-cost producer in a commodity field and high labor content in a product easily shipped in to OUT, and a castle shown
open on the evidence to OUT **[M2011-015]**. Price does not reopen it: "What you can’t do is turn any investment into a good deal
by paying little" **[M2019-015]**; "If you really think a business is declining, most of the time you should avoid it."
**[M2012-062]**.

- **VERDICT: OUT.** The deciding part's castle is shown open on the filer's own words and figures and on its one filing rival's:
  not the low-cost producer against importers, segment margins down from about 16% to 8% to 11%, the field's two filing U.S. makers
  both through Chapter 11 **[M2007-116]**, **[M1997-010]**, **[M2001-013]**, **[L1995-023]**, **[M2011-015]**.

## Q3 — NOT REACHED (closed at Q2).
## Q4 — NOT REACHED (closed at Q2). The balance sheets were read in Step 0's table and are recorded under AFTER THE STOP.
## Q5 — NOT REACHED (closed at Q2).
## Q6 — NOT REACHED (closed at Q2).
## Q7 — NOT REACHED (closed at Q2). The reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.
## Q8 — NOT REACHED.
## Q9 — NOT REACHED.
## Q10 — NOT REACHED.
## Q12 — NOT REACHED.

---
## THE BOX
**OUT at Q2** (the castle of the deciding part, U.S. & Canada, shown open: a high-cost maker of a product shipped in from abroad,
segment margins halved over the span, the field's two SEC-filing U.S. makers both through Chapter 11). The security itself carries
no claim: the issuer's shares were cancelled on 2020-11-13 under the confirmed plan (8-K 0001437749-20-023926). Integrity facts
recorded, not judged (a CEO retention bonus approved on the eve of the Chapter 11 filing; see AFTER THE STOP, Q5 and Q6). No
research pass: the box is OUT, not TOO HARD.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; operator rule 2 and Part VII **[M1997-127]**.)*

**Q3, capital.** Capital spending ran $31.2 million to $48.1 million a year in 2015 to 2019 against depreciation of $39.0 million
to $48.5 million (`run_py_output.txt`); the filer calls itself "a capital-intensive business, with investments in our furnaces being
long-term in nature" and reports lengthening furnace lives "resulting in more time between furnace rebuilds and a reduction in
depreciation expense" (10-K FY2019, Item 1). Sales did not grow over the decade ($799.8 million in 2010, $782.4 million in 2019),
so no part of the spending is shown to have bought growth.

**Q4, the balance sheets, 2010 to 2019** (first-filed XBRL vintage, `run_py_output.txt`; read before the income account
**[M2025-032]**):
- Shareholders' equity $11.3 million (2010), $130.8 million (2013), $148.4 million (2015, the peak), $66.9 million (2017), -$25.8
  million (2019); -$172.5 million at 2020-06-30 (10-Q). Retained earnings a deficit every year, -$178.7 million to -$240.5
  million.
- Goodwill $169.3 million (2010) held to 2016, then cut to $84.4 million (2017, Mexico impairment $79.7 million) and $38.4 million
  (2019, Latin America $46.0 million); nil at 2020-06-30. The impairments are where the castle's narrowing reached the accounts.
- Debt (current plus noncurrent, as tagged) $397.0 million to $466.5 million every year, $391.8 million at 2019; never paid down
  in the decade. Cash $24.7 million to $76.3 million. At 2020-06-30: short-term debt $161.4 million plus $317.9 million of debt in
  liabilities subject to compromise, cash $45.8 million (10-Q).
- Inventory against sales: 18.5% (2010), 21.6% (2015), 24.0% (2017), 24.1% (2018), 22.3% (2019). Inventory grew while sales did
  not; 2019 released $16.5 million of it. Receivables $80 million to $94 million, flat with sales.
- Off the debt line: the Mexican pension plan unfunded by $41.3 million at 2019 (Item 1A); pension and retiree liabilities shown at
  2020-06-30 of $6.2 million and $44.0 million noncurrent outside compromise (10-Q).
- What they say: a thinly capitalised maker whose equity was consumed by losses and impairments while its debt stayed level.
- Accounts habits: the 10-K features non-GAAP "Segment EBIT" and "Adjusted EBITDA" (the phrase appears 21 times in the FY2019
  10-K text); the 2020 proxy reports "Our adjusted EBITDA [...] for 2019 was $70.3 million". Recorded for Q4 and Q5, not weighed.

**Q5, integrity facts (recorded, not judged).** On 2020-05-19 the Compensation Committee approved "a retention bonus in the amount
of $900,000" for the chief executive, amended 2020-05-31 with repayment terms tied to cash-flow milestones (8-K filed 2020-06-01,
0001437749-20-012113, the same filing that reports the Chapter 11 petitions). The shareholders' claim was cancelled five months
later. Any later run that reaches Q5 on this business answers this first **[M2013-088]**.

**Q6, money and owners.** Dividends paid $9.6 million (2015), $10.1 million (2016), $10.4 million (2017), $2.6 million (2018);
buybacks $1.1 million (2014), $15.3 million (2015), $2.0 million (2016) (XBRL, cash-flow statements), with debt near $400 million
throughout. The proxy's long-term plan paid on "2017 ROIC and 2018 and 2019 adjusted EBITDA" (DEF 14A 2020,
0001437749-20-006778).

**Q9, debt.** Before the filing: Term Loan B due 2021-04-09 and an ABL springing maturity of 2021-01-09 (10-K FY2019, Item 1A).
Chapter 11 on 2020-06-01; plan confirmed 2020-10-20 (8-K 0001437749-20-021322); effective 2020-11-13, prepetition credit
agreements "cancelled and discharged", Libbey Glass merged into "an entity formed and controlled by the Company’s former lenders"
and surviving as their wholly owned subsidiary (8-K 0001437749-20-023926). Going-concern doubt stated in the 10-Q for the quarter
to 2020-06-30.

**Q7, the claim.** "all of the shares of common stock of the Company [...] outstanding immediately prior to the Effective Date,
were cancelled, discharged and of no force and effect"; "the common stock has no underlying asset value"; "No shares of the
Company’s common stock will be reserved for future issuance in respect of claims and interests" (8-K 0001437749-20-023926). Form
15-12B filed the same day (0001437749-20-023937); no filing since.

## COMPUTATION, NOT A CLEARANCE (the operator's two reporting figures; Part VII, The owner's price)
*Every figure here is arithmetic beneath the Q2 stop. None is a verdict, a clearance or entry language (operator rule 3).*
Script `scripts/q7_computation.py`, output `q7_computation_output.txt`.

**Inputs.** Window FY2015 to FY2019, the last five filed fiscal years (the business filed no annual report after FY2019; H1 2020 is
the pandemic quarter and a Chapter 11 period and is not an annual year). Owner cash after every real cost (operating cash less
stock pay less all capital spending; working-capital changes are inside operating cash, specific (d)):
- **equity-only** (after interest): 15.6, 44.5, -5.8, -11.0, 29.0; mean **$14.5 million**.
- **all-equity** (interest paid added back: 16.5, 21.6, 18.6, 20.1, 20.7): 32.2, 66.1, 12.8, 9.1, 49.7; mean **$34.0 million**.
  **CONVENTION of this run:** interest is added back in full with no tax shield deducted; rationale: the filer booked tax expense
  on pre-tax losses (2019: an $8.8 million provision on a $60.3 million pre-tax loss), so the filings show no shield to remove.
  Taxes are the company's own cash taxes, inside operating cash (Q7, Whose tax); no carryforward is priced, since none is shown
  sheltering the cash taxes paid.
- Rate: 5.43% (Treasury 30-year par, 2026-10-16). Net debt at the latest filed balance sheet (2020-06-30): $161.4 million plus
  $317.9 million less $45.8 million cash = **$433.5 million** (operating leases left out). The subsequent event the filings state
  is the plan: the debt was exchanged for the business and the shares were cancelled. Shares: 22,667,869 before cancellation;
  **none** carrying a claim today.

**The specifics, applied.** (a) No year of the window is described by the filer as aberrational (the 2018 furnace-rebuild downtime
is routine maintenance on its own account), so the literal window is the base and no cycle base is used. (e) The filing does not
separate growth from maintenance spending, and sales did not grow, so all spending is treated as maintenance and the central case
is the all-spending case. (c) No acquisitions in the window. (b) and (f): the all-equity series does not change sign; its end-year
rate is +11.5% a year, which carried ten years from the mean would put owner cash at $100.6 million, 12.9% of 2019 sales, against
a highest share in the filings read of 8.3% (2016); by (f) the rate is cut to the business's own sales growth, 2015 to 2019,
**-1.24% a year**, which is negative and so makes the bottom by (b), the no-growth case the top. The equity-only series changes
sign, so its growth is measured between halves (2015 to 2016 against 2018 to 2019): -33.1% a year, the bottom.

**(a) VALUE RANGE (all-equity, the central figure), at 5.43%:** the business **$567 million to $626 million** (width 1.10 to 1),
less net debt $433.5 million: equity $134 million to $192 million, **$5.89 to $8.48 per pre-cancellation share**. **Per LBYYQ
share today: nil.** The certificates were cancelled by the plan and carry no claim on the business whose range this is; the
per-share figures are what the old shares would have claimed had the plan not given the business to the lenders, shown because
the operator asked for the arithmetic, not because any holder can receive them.
Beside it: the equity-only range at 5.43%, $28 million to $267 million, $1.22 to $11.76 per pre-cancellation share; and the
halves reading of the all-equity series (-15.7% a year between halves), business $187 million to $626 million (width 3.35 to 1),
per pre-cancellation share -$10.86 to $8.48. The literal window is the base throughout.

**(b) FAIR PRICE (all-equity, central), each end valued at ten percent and averaged:** the business is worth $313 million (bottom)
and $340 million (top) at ten percent, both below the net debt of $433.5 million; the average per pre-cancellation share is
**-$4.73: there is no positive fair price.** At the floor the business did not cover its debt, which is what the plan carried out.
Equity-only figure beside it (never decides alone): $23 million to $145 million at ten percent, average **$3.71 per
pre-cancellation share**. Per LBYYQ share today, on either basis: **nil**, by the plan.

**Against the price:** no quote was found (Step 0). The floor test cannot be run against a price; it does not need to be: no case
of the central range earns the floor at any positive price for a share that claims nothing.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (b961ce0e template;
      79c95d4c Step 0 to Q1; f90d3e3b Q2; this section's commit). The session was cut off once by a network error after the Q2
      commit; the run was resumed from the file on disk with nothing refetched.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock `Screens/_daily/_overnight.lock` was present at start,
      held by the dispatching session, and not touched. The fold is the dispatcher's.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched: **one breach, declared** under
      CONTAMINATION above (a filtered listing of `Test Runs/` for this company's name at the start, which returned nothing). No
      other file of the blind list was opened.
- [x] Every v5 id resolves (checked by `scripts/check_citations.py`); every filing fact has its accession; numbers carry a filing
      or a script.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the computation is headed as the protocol requires.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the Treasury curve (via `tools/run.py`); no
      aggregator quote exists and none is used.
- [x] Contrary evidence written down as found (foundations, Q1, Q2); facts for later questions under AFTER THE STOP, the integrity
      flag in the box line.
- [x] Not a point-in-time run (dated today); no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its price-based lines (placeholder price) are void.
- [x] `python tools/check_framework.py` run before the final commit (result in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **No question asks whether the security carries a claim on the business.** The purchase questions examine the business; a
share cancelled under a confirmed plan reaches Q1 and Q2 as if it were the business, and its nil claim appears only in the
foundations, which reject nothing, and at Q7. Here Q2 closed first, so the cancellation is recorded beneath the stop. A Step 0
line ("does the quoted security still carry a claim on the business, per the latest filing?") would close such a file at once;
none exists, and I did not invent one. (2) **Q7's specifics (b) and (f) do not state their order** when the end-year rate is
positive but the halves fall: the end-year rate (+11.5%) is cut by (f) to sales growth (-1.24%) and gives a range of 1.10 to 1,
while the halves reading gives 3.35 to 1. I applied (b)'s halves only where (b) says (a sign change) and (f) after; the other
reading is shown beside. (3) **Net debt for a company in Chapter 11**: the convention names "borrowings and finance leases"; it
does not say that debt classified inside "liabilities subject to compromise" counts. I counted it. (4) **A negative fair price**:
Part VII does not say how to report one; reported as "no positive fair price" with the arithmetic. (5) **Tooling**: `tools/run.py`
and `Screens/cover_shares.py` cannot resolve a ticker removed from the SEC map, and `run.py` aborts without a price; a CIK override
and a placeholder price were needed, and every price-based line it then prints is void.

