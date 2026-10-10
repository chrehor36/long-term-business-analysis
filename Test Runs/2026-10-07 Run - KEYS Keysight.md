# Company Run — Keysight Technologies, Inc. (NYSE: KEYS) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md`. Keysight: electronic design and test instruments, software
and services, spun from Agilent on 2014-11-01 (Agilent itself spun from HP in 1999); fiscal year ends October 31. The run
was started 2026-10-07, interrupted by the session limit after the template commit and the research, and finished
2026-10-10 under the same file name and the same 2026-10-07 price (see Step 0).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared:** the session's opening context showed the repository's git status and recent commit subjects:
untracked files named for other companies' runs and research folders (ITW run file of 2026-10-07; research folders for AYI,
BDC, CHD, ARCB) and five recent commit subjects about the ESI and HAS runs and their boxes (ESI and HAS OUT at Q5, GFF and
GRMN TOO HARD). Nothing about Keysight was among them. None of it was opened or used. The lock file
`Screens/_daily/_overnight.lock` was read to confirm the dispatcher held it (it reads "interactive v5 re-runs batch 6").

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $379.50 (quote of 2026-10-07 printed by `tools/run.py`, an aggregator, live quote only, flagged per operator
  rule 5). **Not refreshed** on 2026-10-10 when the run resumed: the run is dated 2026-10-07 and every figure is set
  against that day's quote.
- **Shares:** 170,244,745 common shares, one class, from the cover of the 10-Q for the quarter ended 2026-07-31, filed
  2026-09-02, accession `0001601046-26-000036` (`python Screens/cover_shares.py KEYS`). Check: the same 10-Q's balance sheet
  shows 203 million issued less 32.7 million in treasury = about 170.3 million; the proxy (DEF 14A, `0001140361-26-002381`)
  counted 171,517,760 on 2026-01-20, the fall being the 1,845,082 shares bought back in the nine months (10-Q). No 8-K after
  the 10-Q changes the count (8-Ks of 2026-08-18, earnings, and 2026-08-26, a director, `0001601046-26-000032`).
- **Market cap:** $64,608M (379.50 × 170.245M).
- **Sovereign for the earnings currency (USD):** 5.64%, US Treasury daily par yield curve, 30-year, 2026-10-06
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2025-12-17, `0001601046-25-000127`): business, risk factors,
  MD&A, segment note 16, cash-flow statement, debt; 10-Q Q3 FY2026 (filed 2026-09-02, `0001601046-26-000036`); DEF 14A 2026
  (filed 2026-01-26, `0001140361-26-002381`); 8-K 2026-04-23 (`0001601046-26-000017`, new $750M revolver to 2031); the 10-Ks
  for FY2024 (`0001601046-24-000159`), FY2023 (`0001601046-23-000134`), FY2022 (`0001601046-22-000161`), FY2019
  (`0001601046-19-000110`), FY2017 (`0001601046-17-000033`) and FY2016 (`0001601046-16-000077`) for segments, orders,
  backlog and the Ixia record; and the predecessor's own 10-Ks, Agilent FY2003 (`0001193125-03-098260`) and FY2010
  (`0001047469-10-010499`), for the test business through the 2001-03 and 2009 cycles.
- **One figure cross-checked against the filed statement:** operating cash flow FY2025 $1,409M, as printed in the
  consolidated statement of cash flows of the FY2025 10-K and in its MD&A, equals the XBRL figure `tools/run.py` used.
- `python tools/run.py KEYS`, arithmetic lines only (its rule text, ids and floor ignored, Part VII), checked against the
  filings: OCF $1,408M / $1,052M / $1,409M (FY2023-25); stock pay expense $136M / $145M / $176M (the segment reconciliation
  figure; the cash-flow add-back is $135M / $137M / $162M, and the higher figure is used); capex $197M / $154M / $128M;
  depreciation $120M / $126M / $131M and amortization of acquired intangibles $92M / $144M / $145M. Owner cash after every
  real cost (OCF less stock pay less all capex), FY2021-25: $1,044M, $833M, $1,075M, $753M, $1,105M; five-year average
  $962M (the tool's five-year figure, 962, agrees). No securities inside operating cash, no other stock-pay line, no
  capitalized software beside capex (tool, read against the cash-flow statement). Owner cash yield on the market cap at
  $379.50: about 1.5%, against a 5.64% sovereign.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**; that question
here turns on whether I can say what the business will earn, which is Q1's question. The market serves and does not
instruct: the price has roughly doubled inside a year on an order boom (orders up 48% in the nine months to 2026-07-31,
10-Q), and "It just tells us prices." **[M2006-077]**; the boom is evidence about the next year, not a reason. Margin of
safety: "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**.
**Contrary evidence, written down as found** **[M1997-127]**: against the business, the predecessor test business lost money
in a downturn (Agilent test and measurement, operating loss of $710M on $2,612M of revenue in FY2002 after $4,547M in
FY2001, `0001193125-03-098260`), earned $1M in FY2009 (`0001047469-10-010499`), and Keysight's own orders fell 13% in FY2023
and again in FY2024; its own 10-K says its markets are characterized by "rapid technological changes and innovations and
changing industry standards" and that without timely new products its offerings "will become technologically obsolete over
time" (`0001601046-25-000127`, Item 1A). For the business, written down as hard: the HP-Agilent-Keysight instrument line
has led its field for over 80 years by its own account; segment margins rose from 17-20% (FY2014-17) to 25-29% (FY2019-25)
and about 32% in FY2026 to date; no customer is 10% of revenue; services and other are 24% of revenue.

## THE STANDING RULE
A marketable part-interest bought with the buyer's own money cannot put the buyer at risk of ruin; borrowing to buy it is
what the rule forbids, "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing in this name
changes that; the rule is the buyer's conduct and is not tested further here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The parts.** Keysight reports two segments (10-K FY2025 note 16, `0001601046-25-000127`; 10-K FY2022 note 16,
`0001601046-22-000161`). Segment income from operations, the filer's measure (before stock pay, acquired-intangible
amortization, acquisition and restructuring costs), FY2021-25: Communications Solutions Group (CSG) $932M, $1,085M,
$1,068M, $921M, $986M = $4,992M; Electronic Industrial Solutions Group (EISG) $444M, $501M, $581M, $357M, $407M = $2,290M.
CSG carries 68.6% of five-year segment profit, so CSG decides and is the part Q1 must foresee (Q1's holding-company
paragraph, extended to operating segments; Q2's business-of-parts threshold). CSG is 69% of FY2025 revenue: commercial
communications (wireless, wireline and data-centre interconnect, network test from Ixia and Spirent) 67% of it, aerospace,
defense and government 33%.

**The test: where will CSG's earning power be in ten years?** Understanding is "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" **[M2012-065]**; the question is not whether the product
is understood but "the predictability of the economics of the situation 10 years out" **[M2000-104]**. The key variables
**[M1998-044]**, from the filings: (1) how much the communications industry spends on design and test of the next
standard (5G evolution, 6G, 800G to 1.6T Ethernet, non-terrestrial networks, quantum, all named in the FY2025 10-K MD&A
outlook); (2) whether Keysight is first to market with the instrument each new standard needs ("first-to-market solutions"
is the strategy the 10-K names); (3) the length and depth of the customers' spending cycles. All three are forecasts about
technology and about technology customers' budgets, not about consumer behaviour **[M2017-019]**, **[M2023-030]**.

What the filings show of those variables:
- **The filer's own description.** "We generally sell our solutions in industries that are characterized by increased
  competition through frequent new solution and service introductions, rapid technological changes and innovations and
  changing industry standards. [...] Without the timely introduction of new solutions, services and enhancements, our
  solutions and services will become technologically obsolete over time"; "Visibility into our markets is limited"; backlog
  "is not necessarily a reliable indicator of medium or long-term revenue performance"; "Keysight operates in a highly
  competitive and rapidly changing global marketplace" (10-K FY2025, Items 1 and 1A). R&D was 16% to 19% of revenue in
  FY2023-25 ($882M, $919M, $1,007M), rising every year from $361M in FY2014 (XBRL, the 10-Ks listed in Step 0).
- **How far the earnings move inside one cycle.** The predecessor business, Agilent test and measurement: revenue $4,547M
  in FY2001, $2,612M in FY2002 (down 43%); operating income $52M in FY2001, then losses of $710M (FY2002) and $315M
  (FY2003); orders down 29% in FY2002 on "the continued deterioration of the wireline communications market, pricing
  pressures, the competitive pressures of the used equipment market" (Agilent 10-K FY2003, `0001193125-03-098260`).
  Agilent electronic measurement FY2008-10: revenue $3,579M, $2,418M, $2,784M; operating income $477M, $1M, $438M; orders
  down 31% in FY2009 (Agilent 10-K FY2010, `0001047469-10-010499`). Keysight itself: orders $5,984M (FY2022), $5,190M
  (FY2023, down 13%), $5,033M (FY2024, down 3%, about 7% organically); GAAP operating margin 24.8% (FY2023) to 16.7%
  (FY2024); then orders up 48% and revenue up 31% in the nine months to 2026-07-31 on AI data-centre interconnect demand,
  CSG segment margin 31.8% (10-K FY2024 `0001601046-24-000159`, 10-K FY2025, 10-Q `0001601046-26-000036`).
- **The acquired communications businesses did not hold their economics.** Ixia, bought 2017 for $1,622M net of cash
  (10-K FY2017 `0001601046-17-000033`), earned segment operating income of $42M (part year), $16M and $29M on $256M to $489M
  of segment revenue (FY2017-19), and $709M of its goodwill was written off in FY2018 (10-K FY2019
  `0001601046-19-000110`). In 2025 Keysight bought Spirent and sold three of its network-test lines (high-speed Ethernet,
  network security, channel emulation) to Viavi for $399M to satisfy regulators (10-K FY2025).
- **The rivals in the same field** (their own filings; Rohde & Schwarz is private and Anritsu files in Japan, neither an SEC
  filer, neither read): Tektronix, now inside Ralliant, T&M segment sales down 14.5% in 2025 with a $1.44B goodwill
  write-off, operating margin 13.1% in 2024 (Ralliant 10-K FY2025, `0002041385-26-000023`); National Instruments, GAAP
  operating margin between 6.9% and 12.9% across 2008-22 (NI 10-Ks, last `0000935494-23-000008`), sold to Emerson for $8.2B
  of equity value on about $170M of pretax earnings, then an Emerson segment loss of $290M (FY2024) and $68M (FY2025) after
  amortization (Emerson 10-K FY2025, `0000032604-25-000087`); Viavi's network-and-service-enablement segment margin 5.5%
  (FY2025) and 16.1% (FY2026), GAAP operating result between a $900M loss (FY2009) and $185M income (FY2022) (Viavi 10-K
  FY2026, `0001628280-26-056765`). Teradyne (semiconductor test, the adjacent field) swung from operating losses of $381M
  (2008) and $63M (2016) to $1,201M of income (2021) (Teradyne 10-K FY2025, `0001193125-26-059002`, and XBRL). In 2025, the
  year Keysight's revenue rose 8%, Tektronix's fell 15%: the field's earnings move with the technology wave each firm is
  exposed to.

**The tests applied.**
1. *Where will it be in ten years* **[M2000-037]**: I can say Keysight will very probably still be a leading test vendor;
   I cannot say whether CSG's earning power in 2036 is nearer its FY2024 level, its FY2026 level, or the predecessor's
   FY2002 level, because that depends on which communications standards are funded, when, and who is first to them.
   Seeing the industry is not seeing the economics: "does not mean we can judge what its profit margins and returns on
   capital will be as a host of competitors battle for supremacy" **[L2009-005]**.
2. *Key variables and their predictability*: the deciding variables are technology transitions and the customers' R&D
   budgets; the filer calls its own visibility "limited". "If something is not very predictable, forget it."
   **[M1998-044]**.
3. *Do the past statements tell me the future ones* **[M2008-033]**: no. FY2014-17 segment margins of 17-20%, FY2019-25
   of 25-29%, FY2026 near 32%, and a predecessor that lost 43% of its revenue in a year: the past statements show a range,
   not a path.
4. *Important and knowable* **[M2006-076]**: the communications industry's test spending ten years out is important and,
   on the filer's own words, not knowable from where an outside analyst stands.
5. *Would the insiders write it down*: the filer will not ("Visibility into our markets is limited"), and the row is that
   insiders "would not want to put down on paper their predictions about where 10 companies you would choose in the tech
   field would be in 10 years" **[M2000-105]**.
6. *Can I name the winner, not just the industry* **[M2012-067]**: for the current wave, Keysight is winning (CSG revenue up
   35% in nine months, 10-Q); for the waves after it, the rivals' records above show leadership in one wave does not carry
   the margins of the next.
7. *Customers or technology* **[M2017-019]**: technology. CSG lives on the next standard; "a lot of these businesses are
   quite dependent on the technology continuing to gallop" **[M1999-075]**.
8. *How far off could I be* **[M2011-084]**: on the record above, from a segment loss to a 34% quarterly segment margin.
9. *Do I doubt it is inside*: I do, so it is not: "if you have doubts about something being into your circle of
   competence, it isn’t." **[M2002-092]**.

**Against the stop, weighed and not enough.** The product can stay opaque if the economics are clear: "What is important is
that I understand the economic dynamics of the industry." **[M2011-014]**. Some of the dynamics are clear: a field of
long-lived vendors, a large installed base, services 24% of revenue, no customer at 10%. But the dynamic that decides the
earnings, the size and timing of each technology wave and who wins it, is the one that cannot be foreseen, and EISG (the
other 31% of segment profit) does not change the answer because it does not decide.

**Routing.** Q1 closes on a business "that must deal with fast-moving technology", which "is not going to lend itself to
reliable evaluations of its long-term economics" **[L1993-023]**; technology that matters "won’t make it through the
filter" **[M1998-008]**; "We view change as more of a threat into the investment process than an opportunity."
**[M1999-063]**. The verdict is TOO HARD, never OUT on the business: "It doesn’t mean it isn’t a good buy. [...] It just
means that we don’t know how to evaluate it." **[M2000-038]**, in the box "in, out, and too hard" **[M2006-013]**.

**The cause: NATURE, not WORK.** The deciding question is a forecast of the communications industry's spending on the next
standards and of Keysight's place in each, which its own management says it cannot see past a backlog it expects to ship
mostly within six months; more reading would not supply it: "in other cases the nature of the industry would be the
roadblock" **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we have no insights into which
participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**; "if we can’t make a decision
in five minutes, we can’t make it in five months." **[M2008-086]**. The work that could still be done (CSG's sub-markets,
the 6G schedule, Rohde & Schwarz and Anritsu from non-SEC sources) would describe the next wave, not the tenth year.

- **VERDICT: TOO HARD (NATURE).** CSG, the deciding part, cannot be foreseen ten years out because its economics ride on
  fast-changing communications technology, by the filer's own description and by its predecessor's and rivals' records.
  The file closes here. Q2 to Q12 NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED.
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0's research; see below).
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (the reporting figures are computed below, as computation).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), at Q1**: the Communications Solutions Group, 68.6% of five-year segment profit, lives on
fast-changing communications technology, and its ten-year earning power cannot be foreseen; integrity facts recorded, not
judged (see Q5 below). Reporting figures, as computation: value range $36.68 to $37.71 a share (default pair) or $101.91 to
$113.52 (organic pair) against $379.50.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2); each with its source* **[M1997-127]**.

**Bearing on Q2 (the castle).** Parts table (segment income from operations, FY2021-25, 10-Ks `0001601046-22-000161`,
`0001601046-25-000127`): CSG $4,992M, 68.6%, decides; EISG $2,290M, 31.4%. CSG segment margin by year: FY2014 18.3%,
FY2015 19.4%, FY2016 17.9% (old CSG, before services were folded in; 10-K FY2016), FY2017 16.8%, FY2018 19.8%, FY2019 26.6%
(CSG without Ixia; 10-K FY2019), FY2020 24.7%, FY2021 26.5%, FY2022 28.5%, FY2023 29.0%, FY2024 26.9%, FY2025 26.5%,
nine months FY2026 31.8%. EISG: 32.7% (FY2023), 22.9% (FY2024), 24.7% (FY2025), 30.5% (nine months FY2026). The competitor
row is under Q1 above (Ralliant-Tektronix, NI and then Emerson, Viavi, Teradyne; Rohde & Schwarz and Anritsu not SEC filers
and not read). Pricing: the 10-K FY2025 credits "favorable pricing" in both segments against tariffs; the predecessor's
FY2002 orders fell on "pricing pressures, the competitive pressures of the used equipment market" (Agilent
`0001193125-03-098260`). No customer is 10% of revenue in FY2023-25. China was 18.4%, 17.8% and 17.5% of revenue in
FY2023-25 ($1,005M, $884M, $938M; 10-K FY2025 note 16); the 10-K says Keysight has "been prevented from selling large orders
to certain key customers due to trade restrictions" and suspends business with customers placed on US lists.

**Bearing on Q3 (capital).** Capex $128M to $197M a year (FY2021-25), about equal to depreciation ($117M to $131M); R&D,
expensed, $811M to $1,007M a year over the same span. Acquisitions net of divestitures FY2021-25: $178M, $33M, $85M,
$1,163M (ESI Group $681M of cash paid, $458M for the ESI minority in financing, $24M of ESI debt repaid), $1,623M (Spirent
$1,415M net, Synopsys optical group $578M, PowerArtist $26M, less $399M from Viavi): $3,082M, about 64% of the five-year
sum of owner cash ($4,810M). Earlier: Anite $574M (FY2015), Ixia $1,622M net (FY2017).

**Bearing on Q4 (the accounts), with the balance sheets read first** **[M2025-032]** (`tools/run.py` table, first-filed
XBRL of the ten 10-Ks listed in Step 0, checked against the FY2025 and Q3 FY2026 statements). FY2017 to FY2025: total assets
$5,933M to $11,301M; equity $2,310M to $5,881M ($6,571M at 2026-07-31); goodwill plus intangibles $2,737M (46% of assets)
to $4,728M (42%), after the $709M Ixia goodwill write-off of FY2018; tangible equity about $1,153M at FY2025; cash $818M to
$1,873M ($2,605M at 2026-07-31); receivables $547M to $939M and inventory $588M to $1,050M against revenue of $3,189M to
$5,375M, both roughly in step with sales; long-term debt $2,038M to $2,534M; retained earnings $1,041M to $7,075M, with
$4,319M of treasury stock at cost by 2026-07-31. GAAP operating income was $148M (FY2017) and a $394M loss (FY2018, the
write-off) before $711M to $1,358M (FY2019-25). Recurring "non-recurring" items in the segment reconciliation: acquisition
and integration costs $13M, $91M, $152M and restructuring and other $52M, $70M, $48M (FY2023-25). Adjusted figures
featured: the proxy's highlights put non-GAAP EPS of $7.16 beside GAAP EPS of $4.91 and non-GAAP net income of $1,240M
beside GAAP $850M for FY2025 (DEF 14A `0001140361-26-002381`); the non-GAAP measure excludes share-based compensation, and
non-GAAP EPS is the short-term incentive metric. The rows on these habits: **[L2016-006]**, **[L2015-003]**. The FY2026
nine-month tax rate was 6.0% on a $97M audit settlement benefit (10-Q). Singapore's tax incentive expires 2029-07-31 and
Malaysia's expired 2025-10-31, renewal in process (10-K FY2025); effective rate 20% in FY2025 against a 21% statutory rate.

**Bearing on Q5 (the people) — integrity facts recorded, not judged.** The featured adjusted EPS and the pay plan built on
a measure that excludes stock pay (above; Part VII sends such habits to Q5 to be read, where "If you’ve got doubts, forget
it." **[M2013-088]**). CEO Satish Dhanasekaran's summary compensation: $18.0M (FY2025), $12.4M (FY2024, the year net income
fell 42%); he owned 28,229 shares outright plus 17,863 deferred on 2026-01-20 (DEF 14A). The chairman, Ronald Nersesian, is
the former chief executive; the roles are separate. Long-term pay: PSUs on non-GAAP operating margin and relative TSR. Ixia
was bought in 2017 and $709M of it written off in 2018 under the same management line (CFO Neil Dougherty in office since
2013). Centripetal patent suits since 2022, with most claims found invalid so far (10-K FY2025). No restatement or
investigation found in the filings read.

**Bearing on Q6 (the money).** Buybacks, average price paid (shares and dollars from the 10-Ks and the 10-Q): FY2016 $27,
FY2018 $58, FY2019 $76, FY2020 $96, FY2021 $154, FY2022 $156, FY2023 $144, FY2024 $149, FY2025 $158, nine months FY2026 $280
(1,845,082 shares, $517M), the quarter to 2026-07-31 about $328 (644,000 shares, $211M). The programme is a dollar
authorization ($1,500M, November 2025; $983M left at 2026-07-31) with no stated price. Issuance: 13,142,856 shares sold in
March 2017 for $444M (about $34 a share) to help fund the cash purchase of Ixia (10-K FY2017). Against the computation
below, every year's average buyback price from FY2021 sits above the top of both ranges. No dividend.

**Bearing on Q9 (debt).** Senior notes $2,550M face: $700M at 4.60% due April 2027 (now current), $500M at 3.00% 2029,
$750M at 5.35% 2030, $600M at 4.95% 2034; cash $2,605M at 2026-07-31, so net cash of about $88M; a $750M revolver to 2031,
undrawn; operating leases $229M; non-cancellable purchase commitments $704M (10-Q). Interest paid about $75M a year against
operating income of $711M or more since FY2019.

### The reporting figures (at the owner's request; a reporting convention, not a rule; COMPUTATION, NOT A CLEARANCE)
Built as Q7 and its specifics build the range, in `Test Runs/_research 2026-10-07 KEYS/q7_computation.py`. Owner cash
after every real cost = OCF less stock pay expense less all capex, FY2021-25. **All-equity basis (central)**: interest paid
added back and interest income taken out, both after a 21% rate: $1,101M, $880M, $1,054M, $748M, $1,085M, average $974M.
Net debt at 2026-07-31: $2,517M of notes less $2,605M of cash = -$88M (long-term equity investments of $188M and operating
leases left out). Sovereign 5.64%; ten years at the growth shown, then zero nominal growth; floor about 10% (Q7's
CONVENTION) for the fair price.
- **Cycle (specific a):** neither end year of the window (FY2021, FY2025) is called aberrational by the filer; the window is
  the base and the literal window is the same. The FY2026 boom lies outside the window and is not in the base.
- **Default pair (specific c), acquisitions deducted, total growth credited:** base $974M less $616M a year of net
  acquisitions = $357M; total growth on the all-equity series between end years -0.36% a year, so the negative case is the
  bottom (specific b). **Value range $36.68 to $37.71 a share.** Fair price **$21.24**.
- **Organic pair beside, acquisitions left out, organic growth as the filer reports it** (revenue +10%, +1%, -12%, +8% in
  FY2022-25, 1.37% a year): base $974M. Range **$101.91 to $113.52**. Fair price **$60.49**.
- **Equity-only, beside (never decides):** default pair $35.99 to $40.31, fair $21.34; organic pair $100.19 to $111.66, fair
  $59.26.
- Maintenance (specific e): capex runs at about depreciation and the filing gives no maintenance split, so the all-spending
  case is central; the depreciation variant (OCF less stock pay less depreciation) averages $1,007M equity-only, about 5%
  above the capex basis.
- **Against the price of $379.50**, the default range's top is about a tenth of the price and the organic range's top is
  under a third of it. The fair price is "the price at which the midpoint of the range earns the floor": computed here as the
  average of the two ends' present values at 10%, less net debt, per share.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `d611f803`); written question by question; committed after Step 0
      to Q1 (`c9fa8cbc`; a stale `.git/index.lock` from another process blocked the Step 0 commit for some minutes, so Step 0
      and Q1 went in one commit) and at the close.
- [x] Dispatched: the brief allowed the per-question commits; the dispatching session holds the lock (read: "interactive v5
      re-runs batch 6"); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; `Test Runs/` was never listed.
      What was seen by accident (git status and commit subjects in the session's opening context) is declared above.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_ids.py` in the research folder; every filing fact
      carries its accession.
- [x] The order was kept; Q1, the first STOP, closed the file; everything after it is a fact or a computation.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the US Treasury; the price an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit.
- Honest note: the run was interrupted by the session limit between the research and the writing; the Q1 judgment was
  formed on 2026-10-07 from the filings read that day and written on 2026-10-10. Step 0's commit was late (above), so
  write-early was kept for the template copy and for Q1 but not for Step 0 alone.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q1's "What it rules OUT" list puts businesses that live on continued invention among the OUT items, on the row
"if they had never invented any more pharmaceuticals, it would be a terrible business" **[M1999-075]**, while the paragraph
under it sends "fast-moving technology and businesses that change" to TOO HARD; a test business is both, and the two lists
give opposite boxes. I followed the routing paragraph and the reason the rows give (ignorance, not a finding against the
business, **[M2000-038]**), so TOO HARD. (2) The deciding-part threshold says "five-year operating profit" without saying
whose measure; for segments only the filer's segment income (before stock pay, amortization, acquisition and restructuring
costs) exists, and I used it. (3) Specific (c) says "total growth" without saying whether it is measured on owner cash
before or after the acquisition deduction; after the deduction this series turns negative (FY2024-25) and specific (b)
would leave only the no-growth case; I measured it before, and say so. (4) The fair price's "midpoint of the range" can be
read as the midpoint value or the midpoint growth; I averaged the two ends' present values at 10%. (5) Section E's tax
convention names carryforwards and credits that run out inside ten years, not expiring incentive tax rates (Singapore 2029,
Malaysia expired 2025); immaterial here (20% effective against 21% statutory) but unaddressed. (6) Specific (a) looks only at
the window's end years; a boom that begins after the last fiscal year (FY2026 here, revenue up 31% in nine months) is
outside the base by construction, which the text does not mention.
