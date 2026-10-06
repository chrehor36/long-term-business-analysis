# Company Run: Patterson-UTI Energy, Inc. (NASDAQ: PTEN), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template before any fetch.

**POSITION NOTE, declared before any verdict:** not known to this session. The blind rule of the dispatch forbids
opening `PORTFOLIO.md`, so whether the operator holds PTEN was not checked.

**CONTAMINATION, declared.** Nothing about PTEN was read from any other file. Seen without being opened: the session's
git snapshot listed five recent commit subjects (GPOR Gulfport OUT at Q2 as a gas price-taker; POOL OUT at Q7; KTB TOO
HARD (NATURE) at Q2; SBH OUT at Q2; AMN OUT at Q2) and three untracked run file names dated 2026-10-06 (ADT, HRMY,
NSIT); the memory index line "57 gate-clearers, nothing buyable". None concerns this company or its industry except GPOR,
whose subject shows another analyst sending a commodity producer to OUT at Q2. I read that as a pull toward the same
route and tested the route against the text below (Q1 discussion) rather than taking it.

**Write-early note.** The file was written question by question. It was not committed: the dispatch forbids commits.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $11.55 (close 2026-10-05, from `tools/run.py`'s quote feed; an aggregator, flagged per operator rule 5,
  used as a live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **381,384,874** shares
  (10-Q for the period ended 2026-06-30, filed 2026-08-04, accession `0000889900-26-000056`;
  `python Screens/cover_shares.py PTEN`). The balance sheet of the same 10-Q shows 526,633 thousand issued less
  145,252,880 treasury shares, which agrees.
- **Market cap:** 381.385M x $11.55 = **$4,405M**. Net debt at 2026-06-30: long-term debt $1,234.2M (book, 10-Q) less
  cash and restricted cash $203.2M = **$1,031M**; enterprise value about $5,436M.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 2026-10-05
  (issuing authority, via `tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-10, `0000889900-26-000013` (business, competition, risk factors, MD&A, segment tables,
    cash-flow statement).
  - 10-Q Q2 2026, filed 2026-08-04, `0000889900-26-000056` (balance sheet, cash flow, equity statement, debt note).
  - Proxy DEF 14A, filed 2026-04-13, `0000889900-26-000020` (pay table, bonus metrics, pay-versus-performance).
  - 8-Ks: 2026-04-28 `0000889900-26-000030` (revolver extended to 2031 for $450M of commitments); 2026-05-19
    `0001193125-26-230750` ($500M 6.050% notes due 2036, to redeem the 3.95% 2028 notes); 2026-07-30
    `0000889900-26-000050` (Q2 results furnished); 2026-09-08 `0000889900-26-000065` (investor slides furnished).
  - For the twenty-year span: 10-Ks FY2002 `0000950134-03-001857`, FY2006 `0000950134-07-004227`, FY2009
    `0000950123-10-014515`, FY2012 `0001193125-13-054428`, FY2015 `0001564590-16-012604`, FY2017
    `0001564590-18-002481`, FY2020 `0001564590-21-005045`, FY2022 `0000950170-23-002618`, FY2023
    `0000950170-24-020661`, FY2024 `0000889900-25-000034`.
  - Text copies and the scripts that read them are in `Test Runs/_research 2026-10-06 PTEN/`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, 2025:
  $961,219 thousand in the FY2025 10-K cash-flow statement; the XBRL feed `tools/run.py` used gives 961. They agree.
- **`python tools/run.py PTEN`, arithmetic lines only** (Part VII: nothing it prints as a rule, id or floor is used):
  OCF 2023/2024/2025 = 1,006 / 1,176 / 961; SBC 51 / 47 / 41 (its tag; the filed cash-flow statement says 46.8 /
  46.4 / 39.3, used below); capex 616 / 678 / 589; finance-lease principal 16 / 45 / 8.
  **Tool defect found:** its "D&A" column (42 / 124 / 126) is only the amortization of intangibles. The filer reports
  "Depreciation, depletion, amortization and impairment" of 731.4 / 1,171.9 / 940.3 (FY2025 10-K cash-flow statement),
  under no standard tag the tool reads. Its "OE D&A" column (914 / 1,005 / 794) and its "D&A basis" yield (20.53%)
  are therefore wrong by about $700M to $1,000M a year and are not used. The capex column is right.

### Owner cash after every real cost, by year (USD millions; filed cash-flow statements)
OCF less stock pay (treated as a cash cost) less purchases of property and equipment less finance-lease principal.
Disposal proceeds shown separately. Sources per year are listed in `owner_cash.py` in the research folder.

| Year | OCF | SBC | Capex | Disposals | **Owner cash (capex basis)** | Owner cash (depreciation basis) | Net income |
|---|---|---|---|---|---|---|---|
| 2007 | 812 | 19 | 605 | 34 | 189 | 547 | 439 |
| 2008 | 675 | 20 | 445 | 11 | 210 | 379 | 347 |
| 2009 | 454 | 18 | 453 | 3 | -17 | 146 | -38 |
| 2010 | 526 | 17 | 738 | 29 | -229 | 175 | 117 |
| 2011 | 869 | 21 | 1,012 | 22 | -164 | 410 | 322 |
| 2012 | 1,005 | 23 | 974 | 66 | 8 | 455 | 300 |
| 2013 | 889 | 26 | 662 | 10 | 200 | 266 | 188 |
| 2014 | 729 | 27 | 1,052 | 33 | -351 | -17 | 163 |
| 2015 | 999 | 28 | 744 | 21 | 227 | 106 | -294 |
| 2016 | 305 | 28 | 120 | 22 | 157 | -392 | -319 |
| 2017 | 301 | 44 | 567 | 61 | -311 | -527 | 6 |
| 2018 | 731 | 38 | 642 | 47 | 51 | -223 | -321 |
| 2019 | 696 | 39 | 348 | 46 | 309 | -347 | -426 |
| 2020 | 279 | 27 | 146 | 21 | 107 | -419 | -804 |
| 2021 | 96 | 22 | 166 | 43 | -93 | -776 | -655 |
| 2022 | 566 | 21 | 437 | 26 | 108 | 61 | 155 |
| 2023 | 1,006 | 47 | 616 | 26 | 328 | 228 | 246 |
| 2024 | 1,176 | 46 | 678 | 26 | 405 | -43 | -966 |
| 2025 | 961 | 39 | 589 | 44 | 325 | -18 | -93 |

- **Five-year average 2021-2025:** capex basis **$215M** (with disposal proceeds $248M); depreciation basis **-$110M**.
- **Nineteen-year average 2007-2025:** capex basis $77M (with disposals $108M); depreciation basis $0.6M.
  Cumulative net income 2007-2025: **-$1,635M**; 2015-2025: **-$3,472M**.
- **Cash paid for acquisitions** over the same years (cash-flow statements): about $1,410M (2007 $29M, 2010 $238M,
  2014 $176M, 2017 $502M, 2018 $14M, 2021 $29M, 2023 $65M NexTier plus $357M Ulterra). Owner cash on the capex basis
  summed over 2007-2025 is $1,460M, so after the cash paid for acquired fleets the nineteen years left about **$50M**.
  The large fleets bought for stock (Seventy Seven 2017, Pioneer 2021, NexTier and Ulterra 2023) are not in this sum.
- **First half 2026** (10-Q): OCF $119.9M (after a $196.9M rise in receivables), SBC $12.9M, capex $272.6M,
  finance-lease principal $3.3M: owner cash **-$168.9M** for the half; net loss to common $44.2M; dividends paid $76.0M;
  cash fell from $420.6M to $203.2M.

### The balance sheets, ten year-ends (read in Step 0 because the file closes before Q4) **[M2025-032]**
From `tools/run.py`'s ten-year table (first-filed XBRL), checked against the filed balance sheets of FY2017, FY2020,
FY2024 and FY2025 and the 10-Q (USD millions).

| Year-end | Equity | Goodwill | Intangibles | Retained earnings | LT debt | Cash | Receivables | Shares out (M) |
|---|---|---|---|---|---|---|---|---|
| 2016 | 2,249 | 86 | 3 | 2,116 | 598 | 35 | 148 | 148 |
| 2017 | 3,982 | 611 | 76 | 2,106 | 599 | 43 | 580 | 222 |
| 2018 | 3,505 | 411 | 67 | 1,754 | 1,119 | 245 | 559 | 214 |
| 2019 | 2,834 | 395 | 49 | 1,295 | 967 | 174 | 340 | 192 |
| 2020 | 2,016 | 0 | 30 | 472 | 901 | 225 | 160 | 188 |
| 2021 | 1,609 | 0 | 8 | -198 | 852 | 118 | 356 | 215 |
| 2022 | 1,666 | 0 | 6 | -87 | 831 | 138 | 566 | 214 |
| 2023 | 4,812 | 1,380 | 1,052 | 57 | 1,225 | 193 | 971 | 411 |
| 2024 | 3,466 | 487 | 930 | -1,039 | 1,220 | 239 | 764 | 387 |
| 2025 | 3,219 | 487 | 815 | -1,258 | 1,221 | 419 | 723 | 379 |
| 2026-06 | 3,107 | 487 | n/r | -1,379 | 1,234 | 203 | 920 | 381 |

What the figures say, and what they cannot say **[M2025-032]**:
- **Retained earnings went from $2,812M (2014) to -$1,379M (June 2026).** About $4.2B of accumulated earnings were
  lost or paid out in eleven and a half years. Equity rose in 2017 and 2023 only because shares were issued: 46.3M
  shares for Seventy Seven plus a $472M offering in 2017, and in 2023 the NexTier merger (0.752 PTEN share per NexTier
  share, $2,799M consideration) and 34.9M shares for Ulterra. Shares outstanding went from 148M (2016) to 381M (2026).
- **Goodwill was built twice and written off twice.** Seventy Seven and other deals took goodwill from $86M to $611M
  (2017); $211M (2018), $18M (2019) and $395M (2020) were written off, to zero. The 2023 deals rebuilt it to $1,380M;
  $885M was written off in 2024, one year after NexTier closed (FY2025 10-K, Note 7, the completion services
  reporting unit).
- **Debt** stayed between about $0.6B and $1.2B; refinanced in 2026 at 6.050% to 2036 (8-K `0001193125-26-230750`).
- **Property:** gross PP&E stayed about $8.9B to $9.2B from 2017 to 2025 while net PP&E fell from $4,255M (2017) to
  $2,711M (2025) and $2,598M (June 2026); the fleet's book value is being consumed faster than it is renewed.
- **Receivables** rose to $920M in June 2026 from $723M at year-end on flat revenue; a working-capital draw, recorded,
  not judged (Q4 is not reached).
- What the balance sheets cannot say: whether the rigs and pumps carried at $2.6B net would fetch that in a downturn.
  The 2024 abandonment of 42 rigs ($114M charge) says some would not.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which for PTEN means owning the cash the fleet throws off over a full cycle, not the next move in oil.
No macro forecast enters: "macro conclusions are" said to "just never enter into the discussion." **[M2000-094]**; the
relevant figure is "the average profitability of the business over time and how strong its competitive mode is"
**[M2015-016]** (the transcript's word), which is what the twenty-year table above supplies. The analyst's habits:
look for "what’s wrong in things" **[M2025-013]**, and treat later reading as a way "to possibly reject your original
hypothesis" **[M1998-144]**. **Contrary evidence, written down as found** **[M1997-127]**:
1. (Against a quick OUT.) Drilling services earned segment operating income of $204M (2024) and $197M (2025) after
   $477M and $367M of depreciation and impairment (FY2025 10-K, MD&A); the losses of those years sit in completion
   services ($885M goodwill in 2024).
2. (Against a quick OUT.) US revenue per operating day rose from $21.64k (2021) to $36.24k (2023), and adjusted margin
   per day from about $6.5k to $16.8k (FY2023 10-K): the super-spec rig commanded more than the old fleet ever did.
3. (Against a quick OUT.) In 2021 and 2022 PTEN's margin per US rig day was equal to or above Helmerich & Payne's
   (Q2 competitor row).
4. (Against a quick OUT.) Ulterra, the bit business, reports "an industry-leading position in the North American PDC
   drill bit market" and an adjusted gross margin of 43% in 2025 ($147.6M on $343.7M; FY2025 10-K). It is 7% of revenue.
5. (For a quick OUT, found while reading the 10-Q.) The first half of 2026 produced negative owner cash and a net loss
   while $76M of dividends were paid out of cash.

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Not by the business: a common share bought outright cannot call on the
owner. The rule binds the buyer's financing: "borrowed money has no place in the investor's tool kit" **[L2014-005]**,
and "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. A
purchase of PTEN with cash, sized so that a fall of half or more would not force a sale, breaks no form of the rule. No
purchase is proposed here.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the text states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years", with "some notion of how the industry will develop and where the
company will stand within the industry." **[M2012-065]**. The product can stay opaque so long as the analyst can say "I understand the economic dynamics of the
industry." and can answer "Is there ease of entry?" **[M2011-014]**.

**The key variables and whether they are foreseeable** **[M1998-044]**:
1. *Demand* (US land rig days and frac activity): set by oil and gas prices and customers' budgets. Not foreseeable
   year to year. The filer: "We cannot predict either the future level of demand for our oil and natural gas services
   or future conditions in the oil and natural gas service businesses." (FY2025 10-K, MD&A). The rows treat the oil
   price the same way: "how it works out is going to depend on the price of oil to a great extent" **[M2020-035]**.
2. *The supply of equipment and the price it fetches*: foreseeable in character. The filer, in its own Competition
   paragraph: "Historically, available equipment used in our drilling services and completion services businesses has
   frequently exceeded demand, particularly in an industry downturn. The price for our services is a key competitive
   factor, in part because equipment used in these businesses can be moved from one area to another in response to
   market conditions." (FY2025 10-K, Item 1). The phrases "frequently exceeded demand" and "key competitive factor"
   stand in every 10-K read from FY2009 to FY2025 (not found in the FY2002 and FY2006 text copies).
3. *Rig days needed per well*: falling, and foreseeably so. The filer abandoned 42 rigs in 2024 because "efficiency
   gains and technology advancements that have reduced the total number of rigs needed for the U.S. drilling market"
   (FY2025 10-K, Item 1). US operating days: 108,192 (2006), 93,068 (2008), 77,000 (2014), 54,544 (2019),
   45,270 (2023), 36,371 (2025), although PTEN bought 91 rigs (Seventy Seven) and 17 US rigs (Pioneer) in between.
4. *What the capital earns over a cycle*: shown by nineteen years of filings, three busts included (2009, 2015-2016,
   2020-2021): owner cash averaging $77M a year on the capex basis, about $0.6M on the depreciation basis, cumulative net
   income -$1,635M.

**Does the past statement tell the future one** **[M2008-033]**? For the cycle average and the competitive character,
yes: twenty years of the same competition paragraph, the same capacity swings and the same thin average. For any
single year, no.

**The doubt, tested.** Two readings were open. (a) TOO HARD (NATURE): the filer itself will not write the forecast down,
which is test 5's mark **[M2000-105]**, and "If something’s important but unknowable, forget it." **[M2006-076]**.
(b) IN: the unforecastable variable is the year's demand, while what decides the purchase, the castle and the
average earning power over a cycle, is knowable from the record. The rows give the cyclical case directly: "if you
take the next 20 years, there will be, you know, three or four terrible years for residential housing, and there will
be a lot of them that are pretty good, and there will be a few that are terrific. And I don’t know the order in which
they’re going to appear" **[M2011-101]**, and the macro rows send the analyst to "the average profitability of the
business over time" **[M2015-016]**. The framework's own Q2 carries a section on the commodity business and its
low-cost exception, which could never be reached if every business with a commodity-priced customer closed at Q1; and
the cement row treats a business with "periods of substantial overcapacity" as "an understandable business"
**[M2001-059]**. Reading (b) is taken. The doubt row **[M2002-092]** is answered as follows: my doubt is about the
order of the years, not about where the business stands in its industry or what its capital earns over a cycle. The
industry changes by efficiency (fewer rigs per well) and by fuel (gas and electric pumps), not by a technology that
puts the ten-year economics out of reach; both changes run in one direction, against the equipment owner, and both are
on the record.

**VERDICT: IN**, on the rows above and the filing facts in variables 2 to 4. The economics can be foreseen in the sense
**[M2012-065]** asks: the earning power will be cyclical with a thin average, and the company will stand as one of the
two largest US land drillers and a large frac provider in an industry where equipment exceeds demand.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**.

**Is it a commodity business?** The rows define one by the customer's indifference and the price set by rivals:
"Policy forms are standard, and the product is available from many suppliers" and "Consequently, price competition in
insurance is usually fierce. Think airline seats." **[L2004-003]**; "whatever he charged for gas was my price."
**[M2012-109]**. The filer's own description fits: equipment "has frequently exceeded demand", "The price for our
services is a key competitive factor", and equipment moves to wherever the price is (FY2025 10-K, Competition). Its
largest customers are "combining and using their size and purchasing power to seek economies of scale and pricing
concessions"; ten customers gave 57% of 2025 revenue (FY2025 10-K, Item 1A). This is a commodity-type business.

**The castle tests, each with its filing fact.**
1. *The attacker with money* **[M2011-015]**: could $1B build a competing frac or drilling business? Yes, and it was
   done. Liberty ("We have grown from one active hydraulic fracturing fleet as of December 2011 to
   approximately 40 active fleets as of December 31, 2025", its 10-K `0001694028-26-000006`) filed revenue of $4,748M in 2023, more than PTEN's whole company in any year before the
   NexTier merger, and earned cumulative net income of $1,398M from 2016 to 2025 (Liberty's own XBRL facts, 10-Ks
   through `0001694028-26-000006`). The rows' case: "you can create another airline. WARREN BUFFETT: Very easily, and you
   have people that like to do it." **[M2013-054]**; "there are some industries that are just never going to have
   barriers to entry." **[M2012-106]**. **Fails.**
2. *Pricing power and the agony before a rise* **[M2005-020]**: 2025 frac revenue fell $306M with pumping hours "relatively
   flat year over year, with most of the decline driven by lower service and materials pricing" (FY2025 10-K, MD&A).
   Revenue per US rig day: $19.55k (2007), $17.95k (2009), $20.62k (2017, down 10.5%), $21.64k (2021), $36.24k (2023),
   $35.86k (2024); from 2025 the filer stopped printing the figure. Price follows the rig count down in every bust.
   **Fails.**
3. *Unit volume*: US operating days down by two-thirds from 2006 to 2025 (Q1 variable 3), with fleets bought in between;
   the term backlog fell from about $830M (2022) to $700M, $426M and $291M (2023-2025), with 9% of it running past
   2026 (FY2025 10-K). **Fails.**
4. *The low-cost position, the one exception* **[L2004-007]**, **[L2000-017]**, **[M1997-010]**: see the competitor row
   below. In land drilling Helmerich & Payne earned more per rig day in four of the six comparable years (2015, 2016,
   2019, 2024; PTEN was level or ahead in 2021 and 2022) and earned +$3,458M cumulative net income over fiscal 2009-2025 against PTEN's -$2,421M. In pressure
   pumping Liberty earned +$1,398M (2016-2025) while PTEN's legacy pumping lost $177M in 2016 and its completion
   segment lost $899M in 2024 and $79M in 2025. PTEN is not the low-cost operator in either business. **Fails.**
5. *The brand, and the low bid* **[M2017-009]**: the filer names price, availability, condition and specification,
   personnel, service and safety as what wins a job (FY2025 10-K, Competition); nothing a customer asks for by name.
   The exception the rows allow for service **[M2001-014]** is not shown: no filing fact shows a customer paying PTEN
   more than a rival for the same rig or fleet. **Fails.**
6. *Ask the competitors* **[M2017-091]**: their own filings say the same thing. ProPetro: "The energy service industry
   is highly competitive and has relatively few barriers to entry." (10-K `0001680247-26-000028`). Liberty: "projects
   are often awarded on a bid basis, which tends to create a highly competitive environment." (10-K
   `0001694028-26-000006`), naming Patterson-UTI among its competitors. H&P, the drilling leader, had six net-loss years
   in seventeen at the company level, and its net income was 1.9% of revenue over fiscal 2015-2025.
7. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**: narrowing. Rigs needed per well fall; 42 rigs abandoned in
   2024; goodwill paid for NexTier written down by $885M a year after closing; backlog down 65% in three years.
8. *What could destroy it* **[M2000-014]**: one more cycle like 2015-2016 or 2020-2021. In those years PTEN's net loss
   was $294M, $319M, $804M and $655M.

**Contrary evidence weighed** (from the foundations list). The super-spec rig did command a premium in 2022-2024 and
drilling services earned operating income in 2024-2025; the industry has consolidated to a few large drillers. The
rows answer fewness directly: "you can have only two competitors and they’re still terrible businesses, they beat each
other’s brains out." **[M2013-052]**; and the premium did not hold: the filer stopped disclosing revenue per day in
2025 as the rig count fell from 105 to 93. Ulterra's bit position is real but is 7% of revenue and cannot carry the
whole. The cement row allows a commodity business "at a price, you know, for low-cost capacity" **[M2001-059]**; PTEN's
capacity is shown above not to be the low-cost capacity.

### The competitor row (each company's own filings; USD millions)
| Company | Span | Cumulative net income | Cumulative OCF less capex | Net income / revenue | Loss years | Source |
|---|---|---|---|---|---|---|
| **PTEN** | 2009-2025 | **-2,421** | 1,644 | -5.5% | 9 of 17 | 10-Ks listed in Step 0 |
| Helmerich & Payne (HP) | FY2009-FY2025 | +3,458 | 3,087 | 8.1% | 6 of 17 | XBRL facts; 10-Ks `0001047469-16-016935`, `0000046765-19-000019`, `0000046765-22-000070`, `0000046765-25-000071` |
| Nabors (NBR) | 2009-2025 | -5,034 | 612 | -7.8% | 12 of 17 | XBRL facts (10-K filings) |
| Halliburton (HAL) | 2009-2025 | +14,213 | 14,828 | 3.8% | 5 of 17 | XBRL facts (10-K filings) |
| Liberty (LBRT) | 2016-2025 | +1,398 | 498 (2016-2025) | 5.2% | 3 of 10 | XBRL facts; 10-K `0001694028-26-000006` |
| ProPetro (PUMP) | 2015-2025 | +41 | 61 | 0.3% | 5 of 11 | XBRL facts; 10-K `0001680247-26-000028` |
| **PTEN** | 2015-2025 | **-3,472** | 2,064 | -11.4% | 8 of 11 | as above |
| HP | FY2015-FY2025 | +487 | 2,399 | 1.9% | 6 of 11 | as above |

**Margin per US rig day, PTEN against H&P** (thousands of dollars; each company's 10-K; H&P fiscal years end
September; H&P 2022, 2024 and 2025 computed as segment revenue less direct operating expense over revenue days, both
including reimbursements):

| Year | 2015 | 2016 | 2019 | 2021 | 2022 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| PTEN | 12.07 | 10.08 | 9.59 | 6.53 | 10.25 | 16.06 | not disclosed |
| H&P (US land / North America Solutions) | 16.73 | 17.25 | 10.41 | 6.45 | 9.55 | 19.49 | 19.42 |

PTEN's longer series (FY2002, FY2006, FY2009 10-Ks): margin per day $2.02k (2000), $4.59k (2001), $2.01k (2002, 39%
utilization); revenue per day $10.47k (2004), $14.77k (2005), $20.05k (2006), $19.55k (2007), $19.38k (2008), $17.95k
(2009, average rigs operating 91, down from 254); pressure pumping operating income $62M (2010), $193M (2011), $133M
(2012), $89M (2014), $21M (2017) and a loss of $177M (2016).

**Why the castle is shown open, not merely unjudgeable.** The tests above are answered by facts, not left open: the
attacker came and succeeded (Liberty), the price falls with the count in every cycle, the volume fell by two-thirds,
and the low-cost position belongs to someone else in each business. "In an unregulated commodity business, a company
must lower its costs to competitive levels or face extinction." **[L1994-035]**; "the guy with the lower cost comes in
and kills you." **[M2001-013]**. A castle shown open on the evidence is OUT: "If the answer had been
yes, we wouldn’t have done it." **[M2011-015]**. Price does not reopen it: "What you can’t do is turn any investment into a good deal
by paying little" **[M2019-015]**.

**VERDICT: OUT**, on **[L2004-003]**, **[M1997-010]**, **[M2013-054]**, **[M2012-106]**, **[L1994-035]** and the filing
facts above. The run closes here.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
Facts recorded for the record, not weighed: capex exceeded owner cash in most years; capex fell below depreciation in
2016, 2019-2021 and 2024-2025 as the fleet shrank, and the filer says maintenance capex falls "due to fewer operating
days" (FY2025 10-K). The row that would govern: "you have to spend money like crazy if it’s attractive to spend money,
and you have to spend it the same way if it’s unattractive." **[M1998-128]** (cited as the governing row, not applied).

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.
Facts recorded: the annual bonus pays on Adjusted EBITDA, defined as net income plus "depreciation, depletion,
amortization and impairment expense" and "impairment of goodwill", with a 2025 target of $953.3M (proxy
`0000889900-26-000020`); net income that year was -$93.1M. The balance sheets are read in Step 0.

## Q5: WHO RUNS IT. NOT REACHED.
Facts recorded: chief executive total pay $12.08M (2025), $12.05M (2024) (proxy summary compensation table).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
Facts recorded: two transforming mergers paid in stock (Seventy Seven 2017, NexTier 2023) and Pioneer and Ulterra in
part in stock; buybacks of $201M (2023), $290M (2024), $70M (2025) under a $1.0B authorization with no stated price;
dividends of $100M to $127M a year in 2023-2025 and $0.10 a quarter in 2026 while net income was negative. The STOP
that Q6 carries (an all-stock deal by an undervalued acquirer, **[L2009-019]**) and the buyback test against the
bottom of the Q7 range were not run.

## Q7 to Q10, Q12: NOT REACHED.

---
## COMPUTATION - NOT A CLEARANCE (reported at the owner's request; the file closed OUT at Q2)
Everything in this section is arithmetic on the owner cash above. It is not a value finding, carries no entry language,
and does not reopen Q2.

**(a) VALUE RANGE, the Q7 convention.** Input: the five-year average of owner cash after every real cost, $215M on the
capex basis ($248M with disposal proceeds). Growth shown: the aggregate owner cash runs -$93M (2021) to $325M (2025);
from a negative base year the rate is "breathtaking, but meaningless" **[L2005-003]**, and the rise came with a merger
that roughly doubled the share count while US operating days fell 20% from 2023 to 2025. **CONVENTION of this run:** the
shown-growth case is set equal to the no-growth case (rationale: no positive growth rate can be measured from this base,
and the convention forbids carrying a rate above the one shown). Discounted at 5.66%, no growth:
- capex basis: $215M / 5.66% = $3,793M = **$9.94 a share**;
- with disposal proceeds: $248M / 5.66% = $4,377M = **$11.48 a share**;
- depreciation basis: owner cash negative (-$110M a year); **no range can be built on it**.
Range **$9.94 to $11.48 against $11.55**: the price sits at the top of a narrow range.

**Whole-cycle variant** (the five-year window holds the 2022-2024 boom): 2007-2025 average owner cash $77M (capex
basis) or $108M (with disposals): **$3.56 to $5.01 a share** at 5.66%. Because the company is now larger than in most
of those years, a second variant scales the nineteen-year owner cash margin on revenue (3.05%) to 2025 revenue
($4,827M): $147M a year, **$6.81 a share** (CONVENTION of this run: scaling by revenue; rationale: the share count and
fleet nearly doubled in 2023, so an unscaled average understates the present company's cash). After deducting the
$1,410M of cash paid for acquired fleets over the same years, the whole-cycle margin is 0.10% of revenue, about
$5M a year at 2025 revenue, about $0.23 a share. On the depreciation basis the whole-cycle owner cash is about zero.

**(b) FAIR PRICE.** The price at or below which the central case clears the ~10% pre-tax floor (the Q7 CONVENTION,
**[M2003-149]**). Central case: the five-year capex-basis owner cash, $215M. Tax treatment: owner cash is after cash
taxes, which were small (effective tax rate 9.6% in 2025, -1.0% in 2024; FY2025 10-K), so the after-tax figure is used
as the pre-tax figure, which flatters the price slightly. Floor on equity (owner cash is after interest):
$215M / 10% = $2,147M = **about $5.63 a share** ($6.50 with disposal proceeds). On equity plus net debt (owner cash plus
$71M interest, at 10%, less $1,031M net debt): about $4.79. Whole-cycle central case: about **$2.02** ($3.86 scaled to
2025 revenue). At $11.55 the five-year owner cash yields 4.9% on the market value, below the sovereign.

**(c) CHEAP PRICE.** Rule (CONVENTION of this run): the price at which the bottom of the whole-cycle cases (unscaled
nineteen-year owner cash, capex basis, before the cash paid for acquisitions) clears the 10% floor, so that no pencil
is needed even on the poorest honest input: **about $2.02 a share**. Below that the arithmetic stops needing a pencil;
it does not stop the business from being OUT at Q2, and after the cash paid for acquired fleets even this input is
close to zero.

---
## THE BOX
**OUT at Q2.** A commodity-type service, by the filer's own competition paragraph, whose capacity has frequently exceeded
demand for twenty years, where an attacker with money built a larger and more profitable rival in a decade, and where
PTEN is not the low-cost operator in drilling or in pressure pumping. Cumulative net income -$1,635M over 2007-2025;
owner cash after the cash paid for acquired fleets about $50M over nineteen years. Not reached: Q3 to Q10, Q12. For
the record only (COMPUTATION): a five-year range of $9.94 to $11.48, a whole-cycle range of $3.56 to $6.81, a fair price
near $5.63 and a cheap price near $2.02, against $11.55.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed** after each question:
      the dispatch forbids commits. Recorded, not hidden.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, with every quoted fragment beside an id
      found in that row); every filing fact has its accession; no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; nothing after it is a clearance, and the computation is headed
      as such.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the five items under the foundations).
- [x] No row dated after the anchor is cited (the run is dated today; no point-in-time anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used, and one of them (D&A) was found wrong and replaced from the
      filing.
- [x] `python tools/check_framework.py` PASS before finishing (no commit made).
- Gaps: the H&P per-day margin series is not continuous (years 2017-2018 and 2020 not read); NexTier's own pre-merger
  record (2017-2022) was not read from its filings; Liberty's and ProPetro's per-fleet economics were not compared,
  only their company totals; the 2026 investor slides were not read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The Q1 / Q2 line for a cyclical commodity business is not drawn.** Q1's test 5, on whether the insiders would write the
   forecast down, is met literally by this filer, which writes that it cannot predict demand (FY2025 10-K, MD&A).
   Read alone, the test sends every
   oil-service, shipping or mining name to TOO HARD (NATURE) at Q1, and Q2's commodity section and its low-cost exception
   would never be reached. I read Q1 as asking about the average earning power and the position, using **[M2011-101]**
   and **[M2015-016]**, and let Q2 decide. A sentence saying which of the two Q1 should test for a cyclical (the year's
   level or the cycle's average) would stop two analysts closing the same name at different questions.
2. **The Q7 range convention breaks on a negative base year.** "The growth shown" over the five years cannot be
   computed when the first year is negative, and a merger paid in stock that doubles the company inside the window
   makes aggregate growth mean nothing per owner. I set the shown-growth case equal to the no-growth case and said so.
   The convention needs a rule for this case.
3. **Acquired fleets are capital the owner-cash definition misses.** In a fleet business the equipment is replaced by
   capex and by buying other fleets, for cash or for stock. The convention deducts capex only. Here the cash paid for
   acquisitions ($1,410M) nearly equals nineteen years of owner cash ($1,460M), and the stock-paid fleets are not counted
   at all. The convention should say whether acquisitions that replace or add fleet count as capital.
4. **The required heading contains a dash the operator's style rule forbids.** Operator rule 3 asks for the heading
   "COMPUTATION", a long dash, "NOT A CLEARANCE"; the standing rule of this project bans em dashes. I wrote it with a
   hyphen.
5. **`tools/run.py` reads only intangible amortization as "D&A" for a filer that reports one combined
   "Depreciation, depletion, amortization and impairment" line**, which overstated its D&A-basis yield fourfold
   (20.53%). A run that trusted the printed line would have had a wrong second basis. The tool needs a check that D&A
   is at least, say, a fraction of capex, or should print "not found" rather than the nearest tag.
