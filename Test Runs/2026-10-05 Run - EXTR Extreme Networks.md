# Company Run — Extreme Networks, Inc. (NASDAQ: EXTR) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. This is a blind run: the dispatch forbade opening
`PORTFOLIO.md`, any holding review, the session-state file, the register and the prepped reading list, and none was
opened. Whether the operator holds or wants this name is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) The session opened with the repository's recent commit subjects in view; they name the
boxes of four other v5 runs (CTS, MOV, DBD, RES), none about this company. (2) The memory index loaded at session start
says the queue had "57 gate-clearers, nothing buyable"; it names no ticker. (3) The run file of no other company and no
earlier file about EXTR was opened. (4) Prior general knowledge: I knew before reading that Extreme is a sub-scale
networking vendor built by acquisitions; every fact below is from the filings, not from that memory.

Working folder: `Test Runs/_research 2026-10-05 EXTR/` (filings as fetched, text extracts, `run_py_output.txt`,
`cover_shares.txt`, `computation.txt`, peers' XBRL in `peers/`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $23.41 (2026-10-05; `tools/run.py` live quote; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, 130,490,653 shares (Form 10-K for the year
  ended 2026-06-30, filed 2026-08-17, accession `0001193125-26-352872`; cover as of 2026-08-07;
  `python Screens/cover_shares.py EXTR`). No preferred issued (balance sheet: "none issued"). The proxy gives
  132,170,695 outstanding at the 2026-09-09 record date (DEF 14A, 2026-09-18, accession `0001193125-26-395545`); the
  cover count is used.
- **Market cap:** about $3,055M (130.49M x $23.41).
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 2026-10-02
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): Form 10-K FY2026 (filed 2026-08-17, `0001193125-26-352872`): Item 1, Item 1A
  (competition), Item 7 (revenue mix, gross margin, operating expenses, liquidity, buyback, debt), Item 8 (auditor's
  report and critical audit matter, balance sheet, income statement, cash-flow statement). Form 10-Q for the quarter
  ended 2026-03-31 (`0001193125-26-197200`, fetched, debt note incorporated by the 8-K below; not otherwise read). Form
  10-K FY2025 (`0000950170-25-109742`, fetched for the record; its figures reached through XBRL). DEF 14A 2026
  (`0001193125-26-395545`): pay table, incentive metrics, non-GAAP section, ownership, equity-plan burn rate. 8-Ks:
  2026-08-26 auditor change (`0001193125-26-368873`), 2026-07-30 new credit agreement (`0001193125-26-324888`),
  2026-01-07 director appointment (`0001193125-26-005441`), 2026-08-05 results (`0001193125-26-333840`, cover only;
  the release exhibit was not fetched).
- **One figure cross-checked against the filed statement:** net cash from operations FY2026 $123,182K, share-based
  compensation $88,261K and capital expenditures $27,941K in the filed cash-flow statement equal the tool's 123 / 88 /
  28. One tool line is incomplete: its "lt debt 144" for FY2026 is the non-current part only; the filed balance sheet
  carries $19,341K current plus $144,382K non-current, net of issuance costs, and the MD&A states "$165.0 million of debt
  outstanding".
- `python tools/run.py EXTR`, arithmetic lines only (Part VII): owner cash after stock pay and all capital spending
  FY2024 -$39M, FY2025 $45M, FY2026 $7M. Its v4 floor, yield verdict and "points over the sovereign" lines are not read
  as rules. Stock pay is resolved and complete in the cash-flow statement (FY2024 $76.8M, FY2025 $82.3M, FY2026 $88.3M).

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**, which here
means owning a company whose owner cash after stock pay was $7.0M in its latest year on a $3.06B price. The margin of
safety asks that a case not need pencil: "it’s too close to think about" **[M1996-084]**. Who is paid to tell you bears
hard on this name: the 10-K's market case is a vendor projection of the addressable market ("Based on data from 650
Group, demand is projected to grow [...] reaching $77 billion by 2030"), and the speakers did not decide on projections:
"we’ve never looked at a projection in connection with either a security we’ve bought or a business we’ve bought"
**[M1995-050]**; "don’t ask the barber whether you need a haircut" **[M2011-083]**. The analyst's habit applied: look
for "what you’re missing" **[M2025-013]**, and "state their case better than they can" **[M2016-055]** (done
under Q1). **Contrary evidence, written down as found** **[M1997-127]**: (a) gross margin has held between about 51% and
62% for seventeen years (XBRL, FY2010 57.0%, FY2014 51.4%, FY2021 58.0%, FY2026 61.5%), a stable figure in a supposedly
fast-changing field; (b) subscription and support revenue is $474.0M, 36.9% of FY2026 revenue, with $652.8M of deferred
revenue on the balance sheet, which is recurring and sticky; (c) FY2026 product revenue rose 14.9% "driven by average
selling price improvements as a result of price increases implemented during fiscal 2026" (10-K Item 7), a sign of some
price acceptance; (d) the company has survived as an independent vendor since 1996. Each is weighed at Q1 below.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase would be made without borrowed money and at a size that cannot
threaten the buyer, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"Never risk permanent loss of capital." **[L2023-005]**. Nothing in this name forces a breach; the file closes before
sizing arises.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test applied.** Understanding means "a reasonable fix on about what the earning power and competitive position
will look like in five or 10 years" **[M2012-065]**, and "We just don’t know the economics of it 10 years from now."
**[M2000-104]** is the failing form. The product is plain: switches, Wi-Fi access points, cloud management software and
maintenance contracts (10-K Item 1). The question is whether the economics of Extreme, inside its industry, can be seen
ten years out.

**The "key variables"** **[M1998-044]**: (1) Extreme's share of campus switching and wireless against Cisco, HPE (now with
Juniper), Huawei, Arista, Fortinet, Ubiquiti and the cloud platforms; (2) the price it can hold against those rivals;
(3) whether the management layer it sells (ExtremeCloud IQ, Extreme Platform ONE, the AI agents of "Extreme Agent ONE")
stays a vendor product or passes to hyperscalers and AI software vendors; (4) operating cost per revenue dollar at a
tenth or less of the leader's scale. How predictable each is, from the filer's own words:
- **The industry, in the filer's mouth, is in a transition.** "We believe the convergence of AI, Wi-Fi 7, campus
  modernization, cloud flexibility, and autonomous network operations represents one of the most significant
  networking technology transitions in over a decade." "AI agents represent the next major inflection point." (10-K
  Item 1, `0001193125-26-352872`.) The access-point line has turned over Wi-Fi 6, 6E and 7 within the portfolio now sold
  ("Universal Wi-Fi 6/6E/7 APs"); the 10-K says "We are at a technology inflection point with the pending migration from
  Wi-Fi 6 solutions to Wi-Fi 6E and Wi-Fi 7".
- **New classes of entrant are named by the filer.** "AI software vendors and platforms could leverage their AI model
  capabilities, integrations, and agentic workflows to address network-centric use cases that compete with traditional
  network management solutions. If these technologies enable customers to manage, analyze, and operate network
  infrastructure through AI-enabled interfaces, they could disrupt portions of the networking industry"; and "AWS,
  Microsoft Azure, and GCP may provide enterprise customers with a cloud-based platform [...] that could compete with our
  services" (10-K Item 1A).
- **The filer cannot forecast its own subscription base.** "We may also face challenges accurately forecasting customer
  renewal rates, conversion rates from on-premises to cloud offerings, and levels of customer usage or consumption"
  (10-K Item 1A).
- **The industry is consolidating around it.** "There has been a trend toward industry consolidation in our markets for
  several years, and we expect this trend to continue" (Item 1A); HPE's FY2025 10-K records the Juniper acquisition
  (`0001645590-25-000130`: "Networking net revenue increased $2,318 million, or 51.1%, primarily due to revenue
  attributable to Juniper Networks").

**The rows.** "if something comes in where there’s a technological component that’s of significance, or where we think
the future technology could hurt the business as it presently exists [...] it won’t make it through the filter"
**[M1998-008]**; "a business that must deal with fast-moving technology is not going to lend itself to reliable
evaluations of its long-term economics" **[L1993-023]**; "whenever we look at a business and we see lots of change
coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**. Test 6, can I name the winner, not just the
industry: "there’s industries we know that may have a wonderful future, but we don’t have the faintest idea who the
winners will be" **[M2012-067]**; the 650 Group's eleven percent growth in the market settles nothing, since seeing growth
"does not mean we can judge what its profit margins and returns on capital will be as a host of competitors battle for
supremacy" **[L2009-005]**. Test 8, "how far off we can be" **[M2011-084]**: far; the same company reported operating
margins from -10.4% (FY2020) to +8.3% (FY2023) and back to -5.8% (FY2024) inside five years (XBRL; FY2024 to FY2026 in
the filed income statement). Test 9: "if you have doubts about something being into your circle of competence, it
isn’t." **[M2002-092]**.

**The other side's case**, so as to "state their case better than they can" **[M2016-055]**. Enterprise campus networking has had the same leader
for thirty years; gross margin at Extreme has held near 51% to 62% for seventeen years; maintenance contracts renew;
$652.8M of deferred revenue sits on the balance sheet; the company took price in FY2026. On this reading the economics
are foreseeable, and foreseeably poor, which would put the name IN at Q1 and close it at Q2. I do not adopt it, for two
reasons from the filings. First, the stable figure is gross margin, and gross margin is not where Extreme's economics
are decided: research, selling and administration take 56.6% of revenue (FY2026 Item 7) and decide whether anything is
left, and that share moves with the scale Extreme will or will not have against consolidating rivals and new entrants in
the management layer. Second, the recurring revenue is attached to the product generation and the management platform
that the filer says are in transition; "the predictability of the economics of the situation 10 years out" **[M2000-104]**
is the thing that cannot be had. The other reading is carried into "What in the framework was wrong or unclear".

**Which cause** (section I, the two causes). The deciding question is: where will Extreme stand in campus switching,
wireless and network management in 2036, and at what operating margin? The test is whether the industry's insiders would
write that forecast down **[M2000-105]**: "they would not want to put down on paper their predictions about where 10
companies you would choose in the tech field would be in 10 years, in terms of their economics". The insider here, the
filer, writes down a market-size projection and a list of ways the industry could be disrupted, not a forecast of its own
economics; its pay plans run on half-year targets ("semi-annual performance targets to allow it to better set
challenging, yet reasonable goals", DEF 14A). This is the industry's cause, "the nature of the industry would be the
roadblock" **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we have no insights into which
participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**; "we’re not going to learn
enough in the followings five months to make up for the fact that we went in deficient in the first place."
**[M2008-086]**. The cause is NATURE, not WORK: more reading of Extreme's filings would answer what Extreme has earned,
not where the industry's technology will put it.

- **VERDICT: TOO HARD (NATURE)** **[M1998-008]**, **[L1993-023]**, **[M2012-067]**. The ten-year economics of a
  sub-scale vendor cannot be foreseen in an industry that its own 10-K calls in "one of the most significant networking
  technology transitions in over a decade" (Item 1). The box is "in, out, and too hard" **[M2006-013]**, and it is not a
  judgment of quality: "It just means that we don’t know how to evaluate it." **[M2000-038]**. A lower price does not
  reopen it (section I, TOO HARD (NATURE)). **The file closes here.**

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**NOT REACHED.** The Q2 evidence gathered while reading is written down below as contrary evidence and context, not as a
verdict (operator rule 2).

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.**

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance-sheet reading the template asks for is done below in the computation block, because the
file closed before Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.**

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** The owner's reporting request is answered below under COMPUTATION — NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.**

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked.

---
## COMPUTATION — NOT A CLEARANCE
*Everything in this block was produced after Q1 closed the file TOO HARD (NATURE). It carries no entry language and
reopens nothing (operator rule 3). It is written because the owner asked for the value range, fair price and cheap price
on every run, and because the template asks for the balance sheets when the file closes before Q4.*

### The balance sheets, ten year-ends, read before the income account
Read as **[M2025-032]** asks, "balance sheets over an 8 or 10 year period before I even look at the income account"
(tool table, first-filed XBRL vintages, checked against the filed FY2026 and FY2025 balance sheet in
`0001193125-26-352872`). USD millions.

| June year-end | Total assets | Equity | Goodwill | Intangibles | Equity less goodwill and intangibles | Accumulated deficit | Debt (tool, non-current) |
|---|---|---|---|---|---|---|---|
| 2017 | 483 | 107 | 80 | 25 | 2 | -800 | 80 |
| 2018 | 770 | 113 | 139 | 77 | -103 | -828 | 189 |
| 2020 | 979 | 5 | 331 | 68 | -394 | -980 | 395 |
| 2022 | 1,069 | 90 | 400 | 33 | -343 | -934 | 271 |
| 2024 | 1,043 | 25 | 394 | 11 | -380 | -942 | 178 |
| 2026 | 1,178 | 89 | 398 | 3 | -312 | -907 | 144 (165.0 gross in total) |

What the figures say:
- **Goodwill and intangibles have exceeded equity in every year since FY2018.** Tangible equity has been negative by
  $100M to $400M since the Avaya-networking and Brocade purchases (FY2018) and Aerohive (FY2020). The acquisitions were
  paid in cash (XBRL acquisition payments: FY2014 $180.0M, FY2017 $51.1M, FY2018 $97.6M, FY2020 $219.5M, FY2022 $69.5M,
  about $618M in all), and the goodwill they left is $397.8M (FY2026 balance sheet). No goodwill impairment is tagged in
  the period.
- **The accumulated deficit is $907.3M** after thirty years; cumulative net income FY2010 to FY2026 is -$265.1M across
  seventeen fiscal years, with net losses in nine of them (FY2014 to FY2020, FY2024, FY2025; XBRL).
- **Equity is held up by stock pay.** Additional paid-in capital is $1,373.7M against treasury stock of $361.9M (FY2026
  balance sheet). The share count rose from 94.5M (cover, 2012-08-06) to 130.5M (cover, 2026-08-07) although no
  acquisition was paid in shares and $379M was spent on buybacks (XBRL, FY2013 to FY2026) and $185M on tax withholding
  for net-settled awards (XBRL, FY2018 to FY2026). The proxy's three-year average gross burn rate is 3.13% of shares a
  year and the plan reserve is said to last "approximately one year" (DEF 14A).
- **The channel episode of FY2024 shows in the working capital.** Inventory rose to $141M at June 2024 from $89M while
  receivables fell to $90M from $182M; the cash-flow statement shows a $71.1M provision for excess and obsolete
  inventory in FY2024, and product gross margin was 47.7% in FY2024 against 57.3% in FY2025 (filed income statement);
  the 10-K attributes FY2024 to "elongated sales cycles to end customers and lower channel sell-through". By
  June 2026 inventory is $70.0M and receivables $164.6M.
- **Customers' prepayments are the largest liability.** Deferred revenue is $329.7M current plus $323.1M non-current,
  $652.8M, against cash of $211.8M; its growth added $40.1M, $37.7M and $76.2M to operating cash in FY2026, FY2025 and
  FY2024. Operating cash therefore includes growth in prepaid multi-year support; if bookings stopped growing, that
  source would stop.
- **A tell the rows name, not judged here (Q4 not reached):** "Prepaid expenses and other current assets" rose to
  $103.5M from $74.3M (+39%) and "Other assets" to $143.4M from $128.8M while revenue rose 12.6%; the cash-flow line
  "Prepaid expenses and other assets" consumed $53.6M in FY2026. The rows say "if some prepaid expense, deferred asset
  accounts start building up suspiciously high [...] you want to look twice" **[M1995-064]**. Its composition was not
  read; it is recorded as found **[M1997-127]**.
- **What they cannot say:** whether the installed base's support contracts survive the move to cloud and AI management.

### Owner cash after every real cost
Net cash from operations less stock pay less all capital spending (Q4's definition of the costs, "all forms of
compensation" **[L2021-003]**; stock pay "the most egregious example" of costs owners are told to ignore
**[L2015-003]**). USD millions, filed cash-flow statements for FY2024 to FY2026, XBRL for earlier years.

| FY (June) | OCF | Stock pay | Capex | Owner cash | Depreciation variant (OCF - stock pay - depreciation) |
|---|---|---|---|---|---|
| 2017 | 59.3 | 12.6 | 10.4 | 36.3 | |
| 2018 | 19.0 | 27.6 | 40.4 | -49.0 | |
| 2019 | 104.9 | 32.9 | 22.7 | 49.3 | |
| 2020 | 35.9 | 37.8 | 15.3 | -17.2 | |
| 2021 | 144.5 | 39.1 | 17.2 | 88.2 | |
| 2022 | 128.2 | 43.4 | 15.4 | 69.4 | |
| 2023 | 249.2 | 63.5 | 13.8 | 171.9 | |
| 2024 | 55.5 | 76.8 | 18.1 | -39.4 | -45.4 |
| 2025 | 152.0 | 82.3 | 24.7 | 45.0 | 55.0 |
| 2026 | 123.2 | 88.3 | 27.9 | 7.0 | 19.1 |

Five-year average (FY2022 to FY2026) **$50.8M**, about $0.39 a share; three-year average $4.2M; ten-year average
$36.1M. Capital spending ($27.9M) exceeds depreciation ($15.8M) in FY2026, so the capex column is the stricter one and
is used. The adjusted figures the company features are far from these: "Non-GAAP net income of $143.1 million, or $1.06
earnings per share" and "Non-GAAP operating margin of 14.8%" for FY2026 against GAAP net income of $42.1M and a GAAP
operating margin of 4.9% (DEF 14A; 10-K Item 7). The non-GAAP figures exclude "share-based compensation", and the
annual bonus is funded 40% on "EBITDA (excluding bonus payout)" built from that non-GAAP net income (DEF 14A). The rows:
"a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes
us nervous" **[L2016-006]**. Recorded, not judged (Q4 and Q5 not reached).

### (a) The value range, under the Q7 convention
- **Top: $7.27 a share.** Five-year average owner cash $50.8M at no growth, discounted at 5.63%: $902M, plus net cash
  $46.8M (cash $211.8M less debt $165.0M) = $949M over 130.49M shares. No growth is used at the top because the growth
  shown is not positive (next line), so the convention's "never above it" caps the top at no growth.
- **Bottom: $0.93 a share.** The convention's other end is the growth shown on aggregate owner cash. Over FY2022 to
  FY2026 it fell from $69.4M to $7.0M, through a negative year; a compound rate on those ends is about -44% a year, which
  traces to an absurdity the convention forbids ("no result that traces to an absurdity", Q3's cap). I stand in for the
  shown-growth end with the latest three-year average ($4.2M) at no growth: $75M plus net cash $46.8M = $121M. This
  substitution is mine and is confessed below.
- **Width: 7.8 to one,** wider than the convention's three to one; had the file reached Q7 it would have closed TOO HARD
  there as well: "the range must be so wide that no useful conclusion can be reached" **[L2000-025]**, and a wide range
  is not cured by a bigger discount **[M2007-022]**.
- **Sensitivity outside the convention, shown only to bound the case:** carrying the five-year average for ten years at
  Extreme's revenue growth of FY2021 to FY2026 (4.9% a year, above any growth the owner cash has shown), then flat, gives
  $10.57 a share.
- **Against the price of $23.41:** the price is 3.2 times the top of the range and 2.2 times the generous sensitivity.
  The owner-cash yield at the price is 1.7%, against a 5.63% Treasury. To earn 10% at $23.41 with no growth the business
  would need about $301M of owner cash a year, 5.9 times its five-year average and 23.4% of FY2026 revenue, which is
  above Cisco's owner-cash margin in each of its last three years (table below).

### (b) The fair price
**$4.25 a share.** The price at or below which the expected return on the central case clears the floor CONVENTION of
about ten percent pre-tax (**[M2003-149]**, **[L2002-020]**). Central case: five-year average owner cash $50.8M, no
growth (the growth shown is negative, so no growth is already the generous central case); $50.8M / 0.10 = $508M plus
net cash $46.8M = $555M over 130.49M shares. With the 4.9% revenue-growth sensitivity for ten years then flat, the price
that returns 10% is $5.81. **After-tax equivalent used:** owner cash is after Extreme's own taxes, and the 10% is
applied to it directly as the holder's pre-tax return; for a holder taxed at 21% that is about 7.9% after tax. The fair
price sits far below the price: at $23.41 the expected return is 1.7% with
no growth and about 2.6% on the revenue-growth sensitivity.

### (c) The cheap price
**$0.68 a share.** Rule (mine, stated): the price at which even the bottom of the range, the latest three-year average
owner cash of $4.2M at no growth, returns the 10% floor ($42M plus net cash $46.8M = $89M). Below that the case needs no
pencil because the worst stated case clears the floor without any growth or recovery assumed; "it ought to just kind of
scream at you" **[M1996-084]**; the adjustment for risk is "a big discount from that present value" **[M1997-126]**,
not a higher rate. On a name closed TOO HARD (NATURE) the cheap price buys nothing: a lower price does not reopen the
box (section I).

### The Q6 buyback note, recorded back as the convention asks
FY2026 repurchases were 5,377,808 shares for $87.0M at an average $16.18 (10-K Item 7), against a top of range of $7.27;
the authorization states no price ("The manner, timing and amount of any future purchases will be determined by our
management based on their evaluation of market conditions, stock price"). The buyback equals stock pay ($88.3M) and the
share count barely moved (131.2M outstanding at June 2026 against 132.1M a year earlier). Not judged: Q6 not reached.

### The competitor row, from the competitors' own filings (Q2 not reached; context and contrary evidence)
| Company, fiscal year | Revenue $M | Gross margin | Operating margin | R&D / revenue | Stock pay / revenue | Owner cash (OCF - stock pay - capex) / revenue | Accession |
|---|---|---|---|---|---|---|---|
| Extreme, FY Jun-2026 | 1,284 | 61.5% | 4.9% | 18.2% | 6.9% | 0.5% (five-year average 4.3%) | 0001193125-26-352872 |
| Cisco, FY Jul-2026 | 63,325 | 64.5% | 24.3% | 15.1% | 6.0% | 14.1% (FY2025 17.0%, FY2024 13.3%) | 0000858877-26-000132 |
| Arista, FY Dec-2025 | 9,006 | 64.1% | 42.8% | 13.7% | 4.9% | 43.7% before capex (OCF $4,372M less stock pay $439M; capex not pulled) | 0001596532-26-000013 |
| HPE Networking segment, FY Oct-2025 | 6,850 | 59.8% | 23.3% segment earnings (FY2024 24.6%, FY2023 25.0%); segment measure as HPE reports it, not checked for stock pay | n/a | n/a | n/a | 0001645590-25-000130 |
| Juniper, FY Dec-2024 (last before HPE) | 5,074 | 58.8% | 5.8% (FY2021 to FY2023 8.2% to 9.8%) | 22.7% | 5.7% | not pulled | 0001043604-25-000025 |
| Ubiquiti, FY Jun-2026 | 3,274 | 46.2% | 36.2% | 6.2% | 0.2% | 27.5% | 0001511737-26-000056 |

Source: each company's companyfacts XBRL, annual 10-K values (the accession is the latest 10-K carrying the year); HPE
from the segment table in its FY2025 10-K text. What the row shows: Extreme's gross margin equals the leaders', so the
difference is not in what it pays for the box. It is in operating cost: Extreme spends 56.6% of revenue on research,
selling and administration (FY2026 Item 7) and keeps 4.9%; Cisco, Arista, HPE's segment and Ubiquiti keep 23% to 43%.
The nearest analogue, Juniper, a high-gross-margin, high-R&D vendor at about four times Extreme's revenue, earned 6% to
10% and was absorbed by HPE.

### The strongest evidence against the business, written down as found **[M1997-127]**
1. **The filer describes the low bid as its daily condition.** The critical audit matter (Grant Thornton, 2026-08-14):
   "Frequently, distributors need to sell at a price lower than the contractual distribution price in order to win
   business and submit rebate requests for the Company’s pre-approval". Item 1A: "Some of our competitors are capable of
   operating at significant losses for extended periods of time or otherwise offer competitive products at lower
   prices"; "From time to time, we may lower the prices of our products and services in response to competitive
   pressure." The row: "one competitor is frequently enough to ruin a business" **[M2012-108]**.
2. **Thirty years without a durable profit.** Accumulated deficit $907.3M; cumulative net loss of $265.1M over FY2010 to
   FY2026; nine loss years in seventeen.
3. **Owner cash after stock pay is near nil.** $7.0M in FY2026 on $1,284M of revenue; stock pay of $88.3M is 12.6 times
   that, and the CEO's reported pay for FY2026 was $14.2M (DEF 14A summary compensation table).
4. **Scale is the rivals'.** "Most of our competitors have greater name recognition, larger customer bases, broader
   product lines and substantially greater financial, technical, sales, marketing and other resources." (10-K Item 1A.)
5. **The FY2026 price increase did not widen the margin.** Product gross margin fell to 56.6% from 57.3% while prices
   rose, with "higher memory component costs" named in the gross-margin discussion (10-K Item 7): the price passed cost
   through rather than showing a castle.
6. **Auditor change** effective 2026-08-21, Grant Thornton dismissed and Deloitte appointed, with no disagreements and no
   reportable events stated (8-K `0001193125-26-368873`). Recorded as found; the filing gives no reason and none is read
   into it.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1** **[M2000-105]**, **[L1993-023]**. The forecast that would decide it is one the
industry's insiders would not write down: the ten-year economics of a sub-scale vendor facing named new entrants from
cloud platforms and AI software, in an industry its own 10-K calls in "one of the most significant networking technology
transitions in over a decade" (Item 1). No research pass is opened (that is for WORK). For the record only, as COMPUTATION: value
range $0.93 to $7.27 a share (7.8 to one) against $23.41; fair price $4.25; cheap price $0.68.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written question by question in one session. **Not committed:** the
      dispatch forbade commits; the write-early commit discipline was therefore not kept, and is declared here.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and each quoted fragment beside an id
      checked to be in that row); every filing fact has its accession; no number without a row, a filing or a
      CONVENTION label.
- [x] The order was kept; Q1 closed the file; nothing after it is a clearance, and the computation block is headed as the
      protocol requires.
- [x] Owner cash after every real cost (stock pay and all capital spending deducted), never a net-income proxy; the
      sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q1's other-side case, the
      computation block).
- [x] No row dated after the anchor is cited in a point-in-time run (this is a live run; the rule does not bite).
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 floor, yield line and debt line were not used as
      rules, and its debt line was corrected against the filing.
- [x] `python tools/check_framework.py` PASS before handing back (no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 TOO HARD against Q1 IN and Q2 OUT, for a long-lived, sub-scale technology vendor whose poor economics are
themselves foreseeable.** The routing sends a business "whose ten-year economics cannot be foreseen because its industry
changes fast" to Q1 TOO HARD, but it does not say what to do when one layer of the economics is stable for seventeen
years (gross margin near 51% to 62%) and the layer that decides the outcome (operating cost against scale, the management
platform) is in flux. A second analyst could read the same filings as IN at Q1 ("foreseeably poor") and OUT at Q2 (the
low bid in the critical audit matter, the rivals' margins). Both close the file; they differ in the box, and so in whether
a lower price could ever matter. I chose Q1 because the filer itself calls the period a transition and names new entrants;
the framework could say which layer of the economics the ten-year test is applied to. (2) **The Q7 range convention has
no rule for a negative growth shown.** "Carried forward at the growth the business has actually shown [...] never above
it" is silent when the shown growth is negative and its compound rate is absurd; I substituted the latest three-year
average at no growth for the shown-growth end and confessed it. (3) **The cheap price has no convention.** The owner's
reporting request asks for one; the framework's screamer test is a judgment, not a number. My rule (the bottom of the
range clears the floor) is mine. (4) **The floor's pre-tax basis against owner cash that is already after corporate
tax** is not spelled out; I applied 10% to after-company-tax owner cash as the holder's pre-tax return and stated the
after-tax equivalent. (5) `tools/run.py`'s "lt debt" column carries only the non-current part of debt; a v5 run using its
table for the balance-sheet reading would understate debt.
