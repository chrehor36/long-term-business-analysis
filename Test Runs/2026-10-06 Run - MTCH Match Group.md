# Company Run: Match Group, Inc. (NASDAQ: MTCH), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The dispatch for this run is blind and forbids opening
`PORTFOLIO.md`; whether the operator holds MTCH is unknown to the analyst.

**CONTAMINATION, declared:** (1) a directory listing of `Test Runs/` showed the file names of the other runs dated
2026-10-06 (ADT, ASO, BCC, BTU, COLL, GPOR, HRMY, LRN, MD, MHO, NSIT, NWL, PATK, PTEN, REYN, TPC, WKC) and an addendum
title naming the OSIS and BCC runs; none was opened. (2) The session's git snapshot showed four commit subjects with
their boxes and reasons (NWL OUT at Q2, MD OUT at Q2, COLL OUT at Q1, MHO OUT at Q2). (3) The memory index loaded at
session start says, in general terms, that earlier v5 work found gate-clearers but nothing buyable. No other company's
run, research pass or holding review was read, and nothing about MTCH from any earlier run was seen.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $40.33, close 2026-10-05, from `tools/run.py` (aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, par $0.001, **229,550,985** shares
  (10-Q for the quarter to 2026-06-30, filed 2026-08-05, accession `0000891103-26-000130`;
  `python Screens/cover_shares.py MTCH`). The balance sheet of the same 10-Q gives 229,905,859 outstanding at
  2026-06-30 and 304,807,863 issued, 74,902,004 in treasury. No second class; nothing to add.
- **Market cap:** about $9,258M (229.551M x $40.33).
- **Sovereign for the earnings currency:** USD, 5.66%, the 30-year par yield of the US Treasury daily par yield curve,
  2026-10-05 (`python tools/sources.py`, issuing authority). Earnings currency USD (the filer reports in dollars; 56% of
  2025 revenue is international and earned in local currencies, FY2025 10-K).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-26, accession `0000891103-26-000025`: Item 1, Item 1A summary and the competition, users
    and app-store risk factors, Item 3, Item 5 dividends and repurchases, Item 7 in full through liquidity, the cash
    tax table.
  - 10-Q Q2 2026, filed 2026-08-05, `0000891103-26-000130`: balance sheet, cash flow, segment payer table, Azar note.
  - DEF 14A 2026, filed 2026-04-30, `0000891103-26-000066`: the CEO change only (read for facts; Q5 and Q6 not reached).
  - Earlier 10-Ks for the span: FY2024 `0000891103-25-000027`, FY2023 `0000891103-24-000014`, FY2022
    `0000891103-23-000013`, FY2021 `0000891103-22-000020`, FY2020 `0000891103-21-000014`; the pre-separation Match
    Group (CIK 1575189) FY2019 `0001575189-20-000018`, FY2017 `0001575189-18-000019`, FY2015 `0001575189-16-000006`.
  - Schedule 13D, Starboard Value LP, filed 2024-07-15, `0000902664-24-004719`; 8-K of 2024-03-27,
    `0000891103-24-000030` (board seats for Ms. Jones and Mr. Rascoff).
  - Competitors' own filings: Bumble 10-K FY2025 `0001830043-26-000027`, 10-Q Q2 2026 `0001830043-26-000104`, 10-K
    FY2022 `0000950170-23-005080`, 10-K FY2020 `0001564590-21-013176`; Grindr 10-K FY2025 `0001820144-26-000007`,
    10-K FY2022 `0001820144-23-000005`; Meta DEF 14A 2024 `0001326801-24-000034` (see the competitor row at Q1).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities 2025,
  $1,080,380 thousand in the FY2025 10-K's cash-flow discussion, against $1,080M in `tools/run.py`. Agrees. Total
  revenue 2025 $3,487,197 thousand (10-K revenue table) against $3,487.2M in the XBRL series. Agrees.
- **Entity note found in the reading.** CIK 891103 was IAC/InterActiveCorp until the separation of 2020-06-30; the
  surviving registrant was renamed Match Group, Inc. (FY2020 10-K, "Separation of Match Group and IAC"). The XBRL
  rows `tools/run.py` prints for 2017 to 2019 are therefore IAC's, not Match's. The pre-2020 Match figures below come
  from the former Match Group's own filings (CIK 1575189) and from the 2018 and 2019 columns as restated in the
  post-separation 10-Ks.
- **`tools/run.py` arithmetic lines only** (Part VII; its rule, id and verdict lines were not used): OCF, SBC, D&A and
  capex for 2023 to 2025 agree with the filings. Owner cash after every real cost, computed here from the filed cash-flow
  statements as operating cash flow less stock pay less capital spending (stock pay deducted in full, L2021-003's
  "all forms of compensation"; never a net-income proxy):

  | Year | OCF | SBC | Capex | D&A | Owner cash (capex) | Owner cash (D&A) | Cash taxes paid, net |
  |---|---|---|---|---|---|---|---|
  | 2016 (former Match) | 259.5 | 52.4 | 46.1 | 27.7 | 161.0 | | |
  | 2017 (former Match) | 321.1 | 69.1 | 28.8 | 32.6 | 223.2 | | |
  | 2018 | 611.5 | 66.0 | 31.4 | 34.8 | 514.1 | | |
  | 2019 | 648.0 | 89.7 | 39.0 | 34.4 | 519.3 | | |
  | 2020 | 788.6 | 102.3 | 42.4 | 41.3 | 643.9 | | |
  | 2021 | 912.5 | 146.8 | 80.0 | 41.4 | 685.7 | 724.3 | 40.9 |
  | 2022 | 525.7 | 203.9 | 49.1 | 43.6 | 272.7 | 278.2 | 46.4 |
  | 2023 | 896.8 | 232.1 | 67.4 | 61.8 | 597.3 | 602.9 | 102.0 |
  | 2024 | 932.7 | 267.4 | 50.6 | 87.5 | 614.7 | 577.8 | 145.5 |
  | 2025 | 1,080.4 | 258.2 | 56.8 | 67.1 | 765.4 | 755.1 | 99.5 |
  | H1 2026 | 564.2 | 120.6 | 37.7 | 29.5 | 405.9 | | |

  USD millions. Five-year average 2021 to 2025: **$587.2M** (capex basis), $587.7M (D&A basis); cash taxes average
  $86.9M (FY2025 10-K tax table for 2023 to 2025; FY2023 and FY2022 10-K supplemental cash-flow lines for 2021 and 2022,
  payments less refunds). OCF is after cash interest (interest paid $152.5M in 2023, FY2023 10-K). **2022 is abnormal:**
  it carries the $441M payment, in June 2022, of the settlement of the former Tinder employees' valuation suit (Rad v.
  IAC; FY2022 10-K, `0000891103-23-000013`), expensed in 2021 and paid in 2022. **H1 2026 is not like-for-like with
  H1 2025:** cost of revenue fell 16% in Q2 2026 on in-app fee savings that the 10-K attributes to the Google partnership,
  alternative payments and "the current inability of Apple to impose fees on transactions processed through alternative
  payment systems in the U.S." (FY2025 10-K, Item 7), a legal position, not a fact of the business.
- **Where maintenance sits in the capex band:** capital spending is mostly "internal development of software" (FY2025
  10-K, cash flows); 2026 guidance is $55M to $65M, "flat to 2025". Depreciation and capex sit within $10M to $40M of each
  other each year, so the band is narrow and the choice does not move the average. The heavier maintenance cost of this
  business is not in capex at all: it is product development ($449.5M in 2025, 13% of revenue) and selling and
  marketing ($625.5M, 18%), both expensed, both rising as a share of revenue since 2021 (8% and 19% then), recorded here
  and not judged (Q3 not reached).

### The balance sheets, eight to ten years, read before the income account
Read under the template's Step 0 instruction because the file closes before Q4: "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.

| Year-end | Total assets | Equity | Cash | Goodwill | Intangibles | Long-term debt | Retained earnings (deficit) |
|---|---|---|---|---|---|---|---|
| 2016 (former Match) | 2,048.7 | 496.5 | 253.7 | 1,280.8 | 249.2 | 1,176.5 | 182.1 |
| 2017 (former Match) | 2,130.1 | 501.2 | 272.6 | 1,247.6 | 230.3 | 1,252.7 | 532.2 |
| 2018 (former Match) | 2,053.1 | 125.9 | 186.9 | 1,244.8 | 237.6 | 1,515.9 | 453.8 |
| 2019 (former Match) | 2,423.7 | 319.8 | 465.7 | 1,239.6 | 228.3 | 1,603.5 | 988.5 |
| 2020 | 2,977.0 | (1,177.7) | 739.2 | 1,270.5 | 230.9 | 3,534.7 | (8,491.1) |
| 2021 | 5,063.3 | (203.8) | 815.4 | 2,412.0 | 771.7 | 3,829.4 | (8,144.5) |
| 2022 | 4,182.8 | (359.9) | 572.4 | 2,348.4 | 357.7 | 3,835.7 | (7,782.6) |
| 2023 | 4,507.9 | (19.5) | 862.4 | 2,342.6 | 305.7 | 3,842.2 | (7,131.0) |
| 2024 | 4,465.8 | (63.7) | 966.0 | 2,310.7 | 215.4 | 3,849.0 | (6,579.8) |
| 2025 | 4,460.8 | (253.5) | 1,027.8 | 2,339.3 | 192.9 | 3,549.1 (+423.6 current) | (5,966.3) |
| 2026-06-30 | 4,033.9 | (237.1) | 580.6 | 2,335.2 | 153.0 | 3,551.9 | (5,628.9) |

USD millions; XBRL first-filed values from each year's 10-K (CIK 1575189 to 2019, CIK 891103 from 2020), with the
2025 and 2026 columns read on the filed statements. What the figures say, and what they do not:
- **The equity was taken out, not lost.** The former Match paid a $2.00 special dividend, $556.4M, in December 2018
  "funded with cash on hand and borrowings" (FY2019 10-K), which is the 2018 drop. The 2020 separation entry
  ("Exchange Common stock and Class B for Class M Common stock and spin off IAC") reduced total equity by $5.23bn (FY2020
  10-K equity statement); equity has been negative since. Buybacks of $2.57bn from 2022 to 2025 and dividends from 2025
  kept it there while the deficit shrank by earnings. Negative equity here records distributions, not operating losses;
  it also means no return on equity is meaningful.
- **Debt doubled at the separation and has not come down.** About $1.2bn to $1.6bn at the former Match (2016 to 2019);
  $3.5bn to $3.85bn from 2020; $3.55bn at June 2026 after the 2026 exchangeable notes ($423.9M) were settled in cash
  with the proceeds of $700M of 6.125% notes due 2033 issued in August 2025 to replace 0.875% money. Net debt at
  2026-06-30 about $2,968M ($3,551.9M less cash $580.6M less short-term investments $3.2M; the $112M of investments bought
  in H1 2026 sit in non-current assets and are not counted).
- **Goodwill jumped once and intangibles have been written down since.** Goodwill rose $1.14bn in 2021 with Hyperconnect
  (Azar, Hakuna), $890.9M of it paid in stock (FY2023 10-K, supplemental cash flow); intangibles fell from $771.7M (2021)
  to $153.0M (June 2026) through a $319.5M impairment in 2022 "primarily at MG Asia" (FY2022 10-K), the 2024 impairments
  on closing Hakuna and live streaming, and a $25.2M Azar trade-name impairment in Q1 2026 after Apple removed Azar from
  its store (10-Q Q2 2026). The acquired businesses are being written off in steps.
- **Deferred revenue is shrinking while revenue is flat.** Current deferred revenue $262.1M (2021) to $151.3M (2025);
  the filer explains part of it in 2024 as "weekly subscriptions have increased". Customers prepay for shorter periods
  than they did: the float from subscribers is falling. Receivables rose from $188.5M (2021) to $325.0M (2024) because
  app-store revenue "settle[s] more slowly compared to credit card payments" (FY2024 10-K): the platforms hold the cash
  longer.
- **What the balance sheet cannot say:** anything about whether the users stay. The assets of this business (brands,
  user pools, software) are mostly not on it.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**, and for MTCH the answer turns entirely on what Tinder's and Hinge's users do in those years, which is Q1's question. The market serves and does not instruct: "It just tells us prices." **[M2006-077]**; the fall in the price says nothing by itself about the business. The analyst's habits govern the reading: "We really try and destroy our previous ideas." **[M2016-054]**, and "I’m looking for what’s wrong in things because that’s part of investing" **[M2025-013]**. Margin of safety and the floor are arithmetic for Q7, which is not reached.

**Contrary evidence, written down as found** **[M1997-127]** (the case FOR understanding and owning it, recorded at the hour it was read):
- Revenue grew from $909.7M (2015, former Match) to $3,487.2M (2025); owner cash from $161.0M (2016) to $765.4M (2025).
- The company has owned each new format in turn: Match (1995), OkCupid, Plenty Of Fish, Tinder (incubated, 2012), Hinge
  (acquired; payers 980K in 2022 to 2,049K in Q2 2026, revenue $196.5M in 2021 to $690.9M in 2025). The portfolio is a
  bet on the category, not one app, and the filer argues "A large portion of customers use multiple services [...]
  making our broad portfolio of brands a competitive advantage" (FY2025 10-K, Item 1).
- Revenue per payer rose at every brand from 2022 to 2025 (Tinder $13.75 to $17.20, Hinge $24.11 to $31.97; FY2024 and
  FY2025 10-Ks): prices were raised while payers fell, and revenue held.
- H1 2026 owner cash $405.9M against $270.8M in H1 2025 (10-Q Q2 2026).
- A narrower community app can grow: Grindr's average paying users rose from 601K (2021) to 1,258K (2025) (Grindr
  10-Ks FY2022 and FY2025).
- The price, $40.33, sits below the bottom of the Q7-convention range computed at the bond rate ($45.19; see the
  COMPUTATION block). This is written down as a temptation, not a finding: the file closed before Q7.

## THE STANDING RULE
Owning MTCH need not put the buyer at risk of ruin if bought without borrowing and sized so that a large fall can be borne: "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The run closes before any purchase is in question.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it.** Understanding is "our definition of understanding is thinking that we have a reasonable probability of being able to asses where the business will be in 10 years" **[M2000-037]**, which means "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" and "some notion of how the industry will develop and where the company will stand within the industry" **[M2012-065]**. The product is easy to understand; the question is the economics ten years out: "We just don’t know the economics of it 10 years from now." **[M2000-104]**.

**The key variables and whether they are foreseeable** ("trying to identify the key variables in that particular business, and evaluating how predictable they were first" **[M1998-044]**). The variables are payers and revenue per payer by brand, the share of revenue the app stores take, and the marketing cost of replacing users who leave. The filings show how they moved:

| Brand (direct revenue, $M / average payers, thousands) | 2017 | 2019 | 2021 | 2022 | 2023 | 2024 | 2025 | Q2 2026 |
|---|---|---|---|---|---|---|---|---|
| Tinder revenue | 403.2 | 1,152.0 | 1,649.8 | 1,794.5 | 1,917.6 | 1,940.6 | 1,862.9 | |
| Tinder payers | | 5.9M avg subscribers, Q4 | | 10,877 | 10,375 | 9,696 | 9,026 | 8,518 |
| Hinge revenue | | | 196.5 | 283.7 | 396.5 | 550.4 | 690.9 | |
| Hinge payers | | | | 980 | 1,242 | 1,532 | 1,801 | 2,049 |
| Evergreen and Emerging revenue | | | 807.9 | 730.4 | 691.4 | 643.0 | 593.8 | |
| Evergreen and Emerging payers | | | | 3,487 | 3,066 | 2,666 | 2,282 | |

Sources: FY2019 10-K of the former Match (Tinder 2017, 2019; 5.9M Tinder average subscribers in Q4 2019, a different
metric); FY2023, FY2024, FY2025 10-Ks; 10-Q Q2 2026 (Q2 figures; from 2026 Evergreen and Emerging is merged with Asia as
"Everyone Everywhere", 2,683K payers, down 21%). Tinder was 55% of 2025 direct revenue and $832.6M of the $1,068.5M of
segment operating income (78%). The variables swung from Tinder payers roughly doubling in three years to falling four
years in a row (down 22% from 2022 to Q2 2026), and from Evergreen brands that defined the category to payers falling
12% to 14% a year. "If something is not very predictable, forget it." **[M1998-044]**

**Do the past statements tell me the future ones?** "do I understand enough about this business so that the financial statements will tell me the information that’s useful to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**. The filings themselves changed the lens four times in seven years: North America and International with Average Subscribers and ARPU (to 2020); Americas, Europe and APAC with Payers and RPP (2021 to 2023, with payer data before Q2 2020 "likely overstated" for privacy reasons, FY2021 10-K); Tinder, Hinge, Evergreen and Emerging, and MG Asia (2024 to 2025); Tinder, Hinge and Everyone Everywhere (2026). Each change is explained; none breaks the accounts. But the history that would show a brand's full life cycle on one basis does not exist in the filings, and the decade it does show is a decade of the leading brand rising and turning.

**What the filer itself says about the next ten years** (FY2025 10-K, Item 1A, `0000891103-26-000025`):
- "In recent years, demand for online dating services has softened among younger generations, particularly among women
  in those generations, reflecting evolving preferences, shifting social behaviors, and changing expectations regarding
  digital interactions."
- "costs for consumers to switch between services are low, and consumers have a propensity to try new approaches to
  connecting with people and to use multiple services at the same time. As a result, new services, entrants, and
  business models are likely to continue to emerge. It is possible that a new service could gain rapid scale at the
  expense of existing brands through harnessing a new technology, such as generative AI".
- "Facebook offers a dating feature on its platform, which has grown dramatically in size supported by Facebook’s
  massive worldwide user footprint."
- On distribution: Apple removed Azar from its App Store on 2026-02-22 after a rule change of 2026-02-06; 76% of Azar's
  $155.8M of 2025 direct revenue came through that store (FY2025 10-K, Item 7). Apple and Google take "generally up to
  30% on iOS and 15% on Android"; in-app purchase fees were $687.1M in 2025, 19.7% of revenue (18.5% in 2021).
- On Tinder: "Over the past several years, Tinder has experienced a decline in user growth" and "Tinder expects revenue
  to decrease in 2026 at a similar rate to the decrease in 2025". A year earlier the FY2024 10-K had said Tinder had
  "plans to return to growth through product initiatives that focus on the female experience and younger users"; the
  payers kept falling (8,518K in Q2 2026, down 5%).

**The competitor row, from the competitors' own filings** (test 6, can I name the winner):

| Company and metric | Earlier | Peak | Latest | Source |
|---|---|---|---|---|
| Bumble app revenue | $275.5M (2019) | $866.3M (2024) | $783.0M (2025); Q2 2026 $171.7M, down 15% | Bumble 10-K FY2020 `0001564590-21-013176`, 10-K FY2025 `0001830043-26-000027`, 10-Q Q2 2026 `0001830043-26-000104` |
| Bumble app paying users | 1.1M (2020) | 2.8M (2024) | 2.4M (2025), down 13.3%; 2.1M in Q2 2026, down 16.9% | same, and 10-K FY2022 `0000950170-23-005080` (2.0M in 2022) |
| Bumble impairment | | | $1,039.0M in 2025 on "a strategic shift to improve the health of our membership base" and the closing of Fruitz and Official | Bumble 10-K FY2025 |
| Grindr average paying users | 601K (2021) | | 1,258K (2025), up 16.9% | Grindr 10-K FY2022 `0001820144-23-000005`, 10-K FY2025 `0001820144-26-000007` |
| Meta, Facebook Dating | | | no user or revenue metric found in Meta's filings: an EDGAR full-text search of Meta's filings for "Facebook Dating" returned two documents, the 2024 proxy and its preliminary, both on age verification (DEF 14A `0001326801-24-000034`) | the claim of dramatic growth is Match's, above |

Read across the whole span, not one year: Bumble, launched 2014, took paying users from 1.1M to 2.8M in four years while
Tinder was still growing, then lost a sixth of them in eighteen months and wrote off $1.04bn. Tinder rose "to scale and
popularity faster than any other service in the online dating category" (FY2025 10-K, Item 1) and has shrunk for four
years. Hinge has more than doubled since 2022. The one app that grows steadily, Grindr, serves one community. Within one
decade the leader of the mainstream category has changed at least twice, and the free entrant with the largest user
base in the world (Facebook) reports nothing.

**The tests, applied.**
1. **Where will it be in ten years?** "You’re trying to print the next 10 years of Value Line in your head." **[M1999-132]**. I cannot print Tinder's payer line for 2036 within any useful band: the last decade holds a doubling and a 22% decline. "there’s others that are just too tough" **[M1999-132]**.
2. **Customers or technology?** Read as a consumer business, as the rows allow ("in terms of laying out what their prospective customers will do in the future" **[M2017-019]**; "we know what we think we can project out in terms of consumer behavior and threats to a business" **[M2023-030]**), the forecast is of young adults' habits in choosing a dating app, and the filer reports those habits changing (the softening of demand among younger generations, FY2025 10-K, quoted above). The product is of the kind the rows set against chewing gum: "there’s just things that you experiment a lot with, and there’re things that you don’t fool around with once you’re happy" **[M2002-050]**. A dating app is used to be left: the satisfied customer stops paying (Hinge is "Designed to be Deleted", FY2025 10-K), and the filer says customers switch at low cost and use several at once.
3. **Gained fast, lost fast.** "usually if something can gain competitive advantage very quickly, you have to worry about them losing it quickly, too" **[M2002-050]**. Tinder gained faster than any service before it; Bumble gained and is losing; "when an industry is in flux, there are a lot of people that think they’re the survivors, or the ones that are going to prosper, where it turns out otherwise" **[M2002-050]**.
4. **Can I name the winner, not just the industry?** Online dating will very likely exist in 2036. But "there’s industries we know that may have a wonderful future, but we don’t have the faintest idea who the winners will be, so we don’t think about those, either" **[M2012-067]**; "we know there’ll be change, and we don’t know who the winners will be" **[M2014-097]**; "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge what its profit margins and returns on capital will be as a host of competitors battle for supremacy." **[L2009-005]**. The portfolio argument (Match owns the winners) rests on Match catching the next format by building or buying it; the record has both outcomes (Tinder and Hinge, against Bumble escaping and Hyperconnect written down), and whether the next one is caught is the forecast itself.
5. **The technology that could hurt it.** The filer names generative AI as a means by which a new service could take scale from its brands (quoted above), and names Apple and Google as gatekeepers who set its fee and removed one of its apps this year. The rows: "where we think the future technology could hurt the business as it presently exists, [...] it won’t make it through the filter" **[M1998-008]**; "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]**.
6. **How far off could I be?** "we also have some model in our mind of how far off we can be" **[M2011-084]**. On Tinder ten years out I could be off by half either way; the rows place that case outside: "I just don’t know how to evaluate the people that are out there working, either in big companies or in garages, that are trying to think of something that will change the world" **[M2012-073]**.
7. **By its parts** (the framework's holding-company reading, CONVENTION, applied here by analogy to a multi-brand operator, and confessed as this run's extension): Tinder, the part that is 78% of segment operating income, is the part whose ten-year economics cannot be foreseen; Hinge, the growing part, is three years into its expansion outside English-speaking markets. A part that cannot be understood and that matters keeps the whole outside, since "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.
8. **Is it important and knowable?** Important, yes: Tinder's payers decide most of the value. Knowable, no: "If something’s important but unknowable, forget it." **[M2006-076]**

**The routing.** The framework sends a business whose ten-year economics cannot be foreseen because its industry changes fast to Q1, TOO HARD, before the castle tests; the rows: "we’re looking for businesses that, in general, are not going to be susceptible to very much change" and "whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**. The Q2 rows point the same way and are not applied here: "industries where it’s very hard to evaluate moats" are "the businesses of rapid change" **[M2001-069]**, and the 2007 letter would "rule out companies in industries prone to rapid and continuous change" **[L2007-005]**. I considered the alternative close, Q1 IN and Q2 OUT on Tinder's decline as a castle filling in. I did not take it: the evidence against Tinder is evidence that the next ten years cannot be seen, not proof that the portfolio's castle is open (Hinge is growing, prices held, owner cash rose). The difference is recorded under What in the framework was wrong or unclear.

**Which cause: WORK or NATURE.** The deciding question is: where will Match's payers and revenue per payer, Tinder's above all, stand in ten years against new services, AI-built apps, a free Facebook feature and two platform owners who tax and can remove its apps? The test is whether the industry's insiders would write that forecast down: they "would not want to put down on paper their predictions about where 10 companies you would choose in the tech field would be in 10 years" **[M2000-105]**. The insiders here do not: Match guides one year at a time, its 2024 forecast of a Tinder return to growth failed within the year, its own risk factors say a new service could take scale from its brands (quoted above), and Bumble wrote off $1.04bn on a revised one-year outlook. More reading would not change this; it is "the nature of the industry" that "would be the roadblock" **[L1993-023]**, and "Our problem -- which we can't solve by studying up -- is that we have no insights into which participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**. Not "I haven’t done the work and I’m not sure if I did the work I would understand them." **[M1994-026]**: the work on the filings is done, and it shows the question cannot be answered from them. "if we can’t make a decision in five minutes, we can’t make it in five months" **[M2008-086]**.

**VERDICT: TOO HARD (NATURE).** The file closes here. "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**; of the "three boxes at the company: in, out, and too hard" **[M2006-013]**, this is the third. A lower price does not reopen it.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED. (The competitor row the template asks for here is filled at Q1, test 4, where it was evidence.)

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read at Step 0. Facts recorded for a later reader, not judged: the filer renamed
its primary non-GAAP measure "Adjusted EBITDA" in the FY2025 10-K "to better align with our peers"; it excludes stock
pay ($258.2M in 2025) and is "among the primary metrics [...] by which management is compensated" (FY2025 10-K, Item 7).

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED (operator rule 2: no Q5 output while Q1 is not IN). Facts read, not judged: the chief executive changed from
Mr. Kim to Mr. Rascoff, a director since March 2024, effective 2025-02-04 (DEF 14A 2026); Starboard Value reported 6.6%
on 2024-07-15 (13D); a securities class action alleging Tinder's challenges were understated was dismissed voluntarily
by the plaintiff on 2025-09-22, with derivative suits pending (FY2025 10-K, Item 3); Tinder settled an age-tiered pricing
class action for $60.5M and the FTC settled for $14.0M over certain E&E apps in 2025 (FY2025 10-K, Item 7). No Elliott
filing was found among the filings read.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts read, not judged: repurchases of 7.2M shares for $482.0M in 2022 (about $66.94 a share), 13.5M for
$546.2M in 2023 (about $40.46), 22.2M for $752.7M in 2024 (about $33.91), 24.7M for $788.8M in 2025 (about $31.94), and
$245.4M in H1 2026 against 7.27M more treasury shares (about $33.77); shares outstanding 283.5M (2021) to 229.9M (June
2026), down 19%; no programme names a price; quarterly dividend from 2025 ($0.19, then $0.20). FY2022 to FY2025 10-Ks,
10-Q Q2 2026.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED. The owner's reporting request is answered below, under COMPUTATION - NOT A CLEARANCE.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US? WEIGHING.
NOT REACHED. Fact recorded: $3.55bn of senior and exchangeable notes, maturities 2027 ($450M), 2028 ($500M), 2029
($350M), 2030 ($500M senior, $575M exchangeable), 2031 ($500M), 2033 ($700M) (FY2025 10-K, key terms; the 2026
exchangeables were settled in cash in June 2026, 10-Q Q2 2026); revolver $499.4M undrawn.

## Q10: IS IT THE FAT PITCH? WEIGHING.
NOT REACHED. The framework would have the buyer do nothing.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Dating services are not among the businesses the framework names.)

---
## COMPUTATION - NOT A CLEARANCE
*Written at the owner's request (not a rule change), after the file closed at Q1. No entry language; nothing here
reopens Q1. Label kept with a hyphen in place of the protocol's dash under the standing no-em-dash rule.*

**Inputs.** Owner cash after every real cost, five-year average 2021 to 2025: **$587.2M** (capex basis; D&A basis
$587.7M), after interest and taxes, so it is cash to the equity. Growth shown, on aggregate owner cash, 2021 to 2025:
$685.7M to $765.4M, **2.79% a year** (the Q7 convention's measure, aggregate not per share). Rate: 5.66%, the 30-year
Treasury. Ten years at the growth shown, then zero nominal growth; ends are the no-growth and shown-growth cases (the
framework's Q7 CONVENTION). Shares 229.551M (cover).

**(a) Value range (equity, after tax, at the bond rate):**
- **Central (2021 to 2025 as filed): $10.37bn to $12.94bn, $45.19 to $56.35 a share**, top 1.25 times the bottom.
- **Whole-cycle variant** (2022 abnormal: the $441M settlement payment added back, base $675.4M): $11.93bn to
  $14.88bn, **$51.98 to $64.82 a share**. I give it because the brief asks; I do not prefer it, since legal settlements
  recur here ($60.5M and $14.0M in 2025).
- **D&A variant:** $45.23 to $49.13 a share (growth shown on that basis 1.05%).
- **A declining case the convention does not draw** (owner cash falling 5% a year for ten years, about Tinder's payer
  decline, then flat): $30.53 a share; at 3% a year, $35.69. Shown because the convention's two ends both assume no
  decline, and the core brand is declining; see What in the framework was wrong or unclear.
- Price $40.33 sits below the central range's bottom. At the price, the perpetual growth the bond rate implies is
  about -0.7% a year.

**(b) Fair price** (the price at or below which the central case clears the ~10% pre-tax floor, the framework's Q7
CONVENTION; "we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**, a figure
its speaker called "arbitrary"). Tax treatment: pre-tax owner cash = after-tax owner cash plus cash taxes paid (five-year
average $86.9M), so **$674.0M**; expected pre-tax return = pre-tax owner cash yield on the price plus the growth shown.
- **On equity: $40.71 a share** (7.21% yield plus 2.79% growth = 10%). At $40.33 the expected pre-tax return is
  about 10.07%, a hair over the floor: a pencil case.
- **On equity plus net debt** (pre-tax owner cash plus average interest expense $148.7M, against market cap plus net debt
  $2,968M): **$36.76 a share**. This is the stricter and, for a company carrying $3.55bn of notes being refinanced from
  0.875% to 6.125%, the more honest one.
- With no growth: $29.36 (equity), $22.91 (equity plus net debt).

**(c) Cheap price** (below which no pencil is needed): **$22.60 a share**, one half of the bottom of the central range.
My rule, a CONVENTION of this run: the rows ask a price "at a big discount from that present value calculated using the
risk-free interest rate" **[M1997-126]**, illustrated by "I didn’t need to know whether it was worth 97 billion or 103
billion if I was buying it at 35 billion" **[M2008-068]** (about a third of value); half is the more lenient reading. It
also sits at the no-growth, equity-plus-net-debt fair price ($22.91). Neither price is a buy level: a TOO HARD (NATURE)
is not reopened by price.

Scripts and inputs: `Test Runs/_research 2026-10-06 MTCH/value.py`, `annual.py`, `bs.py`.

---
## THE BOX
**TOO HARD (NATURE), at Q1.** The deciding question, where Tinder's and the portfolio's payers and prices will be in ten
years in a category where users switch at low cost, new services can "gain rapid scale" (the filer's words), the
mainstream leader has changed at least twice in a decade, and two platform owners tax and can remove the apps, is a
forecast the industry's own insiders do not write down. No research pass: the cause is the industry, not unread
documents. Range for reference only (COMPUTATION): $45.19 to $56.35 against $40.33; fair $40.71 (equity) or $36.76
(equity plus net debt); cheap $22.60.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: not done.
      The dispatch forbade commits, and the file was written in one pass after the reading.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact has its accession
      or names its filing; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q1 failed and closed the run; Q2 to Q12 are NOT REACHED; facts listed under them are marked
      not judged, and nothing after Q1 is a clearance.
- [x] Owner cash after every real cost (stock pay deducted in full), never a net-income proxy; the sovereign from the
      issuing authority; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: the list under THE FOUNDATIONS.
- [x] No row dated after the anchor: not a point-in-time run; n/a.
- [x] Only the arithmetic lines of `tools/run.py` were used; its 2017 to 2019 rows were found to be IAC's and were
      replaced from the former Match Group's filings.
- [x] `python tools/check_framework.py` run after writing (result in the report; no commit made by this session).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a consumer app with a declining core brand.** The routing fixes fast industry change at Q1 TOO
HARD and a castle "shown on the evidence to be filling in" at Q2 OUT, but MTCH has both kinds of evidence at once: an
industry the filer itself calls prone to new entrants with low switching costs, and a core brand whose payers fell four
years running. Two analysts could close it at Q1 TOO HARD (NATURE) or at Q2 OUT on the same facts. I chose Q1 because
the decisive fact is that ten years cannot be seen (the portfolio as a whole is not shown open: Hinge grows, prices held,
owner cash rose), and said so in the run; a sentence saying which governs when a single brand's decline is visible
inside an industry that changes fast would settle it. (2) **The holding-company reading by parts** is written for a
holding company; I applied it by analogy to a multi-brand operator and confessed it. The framework does not say whether
a portfolio of brands in one industry is read whole or by brand. (3) **The Q7 range convention has no declining end.**
Both ends (no growth, shown growth) assume the cash does not shrink; for a business whose largest part is shrinking, the
"bottom" ($45.19) is not a bottom, the range looks narrow (1.25 to one) and sits above the price, and a run that reached
Q7 would be invited toward IN by an artefact. A -5% case gives $30.53. The convention needs a rule for the case where the
shown trend of the main part is negative even though the aggregate grew. (4) **The floor's basis is unstated.** The
CONVENTION says "about ten percent pre-tax on the price paid" without saying equity or equity plus net debt, or how
after-tax cash is grossed up; here the two bases differ by about $4 a share at the price and decide whether the price
clears. (5) **The template's competitor row lives at Q2**, but Q1's test 6 (name the winner) needs it; when Q1 closes,
the template has no slot, so I put it at Q1. (6) **`tools/run.py` silently mixes registrants**: for CIK 891103 its 2017
to 2019 balance-sheet rows are IAC's, before the 2020 separation; nothing in its output warns of it. (7) **The
protocol's required label "COMPUTATION" with a dash** conflicts with the standing no-em-dash rule; I used a hyphen.
