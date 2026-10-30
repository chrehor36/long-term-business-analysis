# Company Run — Table Trac, Inc. (OTCQX: TBTC) — 2026-10-25
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run. Departure from the canonical brief, stated by the dispatcher: the repository moved on 2026-10-25 from
`C:\Users\chreh\OneDrive\Documents\BRK` to `C:\Projects\BRK`; nothing else departs. This file was copied from the template
before any fetch; working folder `Test Runs/_research 2026-10-25 TBTC/` (notes, `compute.py`, `compute_output.txt`,
`check_ids.py`; raw filings in the ignored `cache/`).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-25: [withheld from the public copy].*

**CONTAMINATION, declared.** Nothing below was used. (1) A directory listing of `Screens/` (made to find
`cover_shares.py`) printed file names, among them `RESUME STATE 2026-09-02 ...`, `RESUME STATE 2026-09-12 ...`,
`WATCHLIST RUN QUEUE.md`, `2026-08-31 PREPPED READING LIST (operator lists).md`, `V5 PASSERS - the alert list.md`,
`SURVIVORS - Non-Bank Candidates Awaiting Full Gate Run.md` and screen files for OTCQX, OTCQB and OTCID (TBTC trades on
OTCQX, so it may appear in one of them); none was opened. (2) A listing of the repository root printed the name
`PORTFOLIO.md`; not opened. (3) `git log --oneline -3` printed three commit subjects about another company's run (KSS,
"OUT at Q2"); not used. (4) `git status` printed the names of uncommitted files in another analyst's research folder (ARCB)
and in `MBA - UNG/`; not opened, not touched. (5) One command listed `Test Runs/` through a filter for my own folder name
only; it returned nothing. No file about TBTC under any name was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.37 (close 2026-10-23; `tools/run.py`; **aggregator, live quote only**, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 4,642,887 common, one class (10-Q for the quarter to 2026-06-30, filed
  2026-08-12, accession `0001437749-26-027186`; `python Screens/cover_shares.py TBTC` gives the same). Checked against the
  balance sheet of that 10-Q: 4,756,734 issued less 113,847 treasury = 4,642,887. The only filings after that 10-Q are two
  8-Ks (`0001437749-26-027198`, an option grant of 100,000 shares to the CEO at $4.51, unexercised; and the dividend 8-K
  `0001437749-26-026491`); no prospectus. Dilution beside: diluted weighted shares for the second quarter 4,681,571.
- **Market cap:** $24.93M.
- **Sovereign for the earnings currency (USD):** 5.33%, US Treasury daily par yield curve, 30-year, 10/23/2026
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-03-24, `0001437749-26-009488`); 10-Ks FY2015 to FY2024
  (`0001144204-16-091605`, `0001144204-17-017231`, `0001144204-18-018239`, `0001615774-19-004791`,
  `0001213900-20-007284`, `0001437749-21-007795`, `0001437749-22-007336` with its 10-K/A `0001437749-22-007728` (exhibit
  only), `0001437749-23-007994`, `0001437749-24-010085`, `0001437749-25-008353`); the latest 10-Q
  (`0001437749-26-027186`); the proxy (DEF 14A filed 2026-04-09, `0001437749-26-011855`); the 8-Ks of 2026
  (`0001437749-26-000465`, `-001995`, `-005801`, `-015918`, `-016581`, `-016613`, `-026491`, `-027198`).
  **One figure cross-checked against the filed statement:** cash and cash equivalents at 2025-12-31, $8,235,788 in the
  filed balance sheet and cash-flow statement of `0001437749-26-009488`, against 8,236 (thousands) printed by `tools/run.py`;
  revenue FY2025 $11,048,237 filed against 11,048 printed.
- `python tools/run.py TBTC`, arithmetic lines only: OCF 2023 0.4, 2024 2.0, 2025 1.8 ($M); stock pay about 0.1 a year;
  capital spending about 0.1; D&A under 0.05; the ten balance sheets (read at Q4 below, under AFTER THE STOP). Its
  three-year "owner earnings" mean and its yield lines are not used; owner cash is recast from the filed cash-flow
  statements in the COMPUTATION below (operator rule 5). The tool found no securities inside operating cash, no other
  stock-pay line, no intangible, mine or fleet spending; checked against the filings: right, except that the filer's
  capitalized software ($61,989 in 2025, $16,691 in 2023) is in its "PaymentsForSoftware" capex tag, which the tool did count.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own Table Trac's maintenance stream "Would I be happy
buying this stock if the market closed for five years?" **[M1997-109]**, and with a $25M company whose stock trades thinly
(the filer's own risk factor) the market closing is close to the real condition. The market serves and does not instruct:
"It just tells us prices." **[M2006-077]**. Margin of safety: "if you have to actually do it on — with pencil and paper,
it’s too close to think about" **[M1996-084]**. The analyst's habits govern this run: the evidence against was hunted
first and written down as found, "write it down in the first 30 minutes" **[M1997-127]**, and the question put was "What do
I not know that I need to know?" **[M1999-129]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the
filer's own description of its field, "intense competition in the gaming management and gaming products industry which is
characterized by dynamic customer demand and rapid technological advances" and "Several of our competitors are larger ...
and significantly greater resources" (10-K FY2025, Item 1A); (2) the count of operators under maintenance contract has been
"115 casino operators in over 300 casinos" in the 10-Ks for FY2023, FY2024 and FY2025 and in the 10-Q to 2026-06-30, while
the filer reports eight systems delivered in 2024 and CasinoTrac installed "at eight new customer in 2025"; either customers
were lost in the same number or the count is stale, and the filings do not say which; (3) maintenance revenue, the
recurring line, has been flat for six quarters: $1,509,782 in the first quarter of 2025 and $1,541,403 in the first quarter
of 2026, $1,580,992 in the second quarter of 2025 and $1,565,358 in the second quarter of 2026 (10-Q
`0001437749-26-027186`, derived from its three- and six-month tables); (4) operating income peaked in 2022 at $2,019,951
and was $1,603,593 in 2025 on the same revenue ($11.06M and $11.05M), as selling, general and administrative cost rose from
$4.93M to $6.55M; (5) the 2019 statements were restated in the FY2020 10-K for revenue-recognition errors, and internal
control was reported not effective for 2020, 2022 and 2023; (6) one customer was 33.9% of 2024 revenue and 47.5% of
receivables at 2024 year-end, and two installed contracts ($887,500 at 2025 year-end) are carried off the books because
collection is doubtful, "one customer has a large debtor in a senior position to Table Trac" (10-K FY2025, revenue policy);
(7) the founder, who designed the product, gave up the chief executive role on 2026-01-01 and remains President and Chief
Technology Officer at 64.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin: the business has no borrowings and $8.15M of cash at 2026-06-30, and a
stake bought with the buyer's own money, sized so that a total loss is survivable, risks nothing the buyer needs; the rule
bars only borrowed money to own it, "borrowed money has no place in the investor's tool kit" **[L2014-005]**. One feature of
the holding bears on conduct: the stock is illiquid (filer's risk factor), so the buyer must be one who is never forced to
sell.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in that particular business,
  and evaluating how predictable they were first" **[M1998-044]**; and "do I understand enough about this business so that
  the financial statements will tell me the information that’s useful to me" **[M2008-033]**.
- **What the business is, from the filings.** One segment (10-K FY2025, Note 1, segment paragraph). Table Trac sells casino
  management systems (player tracking and loyalty, table games, cage and vault, kiosks) to casinos, mostly small and
  regional US casinos and tribal casinos, with some in the Caribbean, Central and South America and Australia (93.7% of
  2025 revenue from the US). A sale is a system installation recognized on installation, often financed by the company on
  payment terms of 6 to 72 months at about 2% to 7% interest; each installation carries a maintenance contract
  recognized over an average five years; "service and other" is DataTrac, kiosks and promotional software. 32 employees.
- **The key variables and how predictable they were.** (1) The installed base under maintenance and its rate: maintenance
  revenue $1.69M (2015), $2.00M, $2.27M, $2.64M, $2.83M (2019), $2.62M (2020, after COVID credits), $3.12M, $3.51M, $4.99M,
  $5.38M, $6.15M (2025) (disaggregation tables of the 10-Ks FY2015 to FY2025; FY2015 to FY2018 labelled "maintenance
  fees"). This variable has been foreseeable for ten years, and the 2020 closures showed it: total revenue fell 44.3% to
  $4.40M while maintenance fell 8% "due to an increase in COVID-19 related customer credits" (10-K FY2020,
  `0001437749-21-007795`). (2) New installations: system revenue $2.05M (2015) to $6.25M (2022) to $2.92M (2025), lumpy
  by the filer's own risk factor ("unpredictable order flows"); not foreseeable year to year, but bounded, and it is the
  smaller part of gross profit since 2023. (3) The cost base, mostly salaried people; foreseeable.
- **The technology question.** The filer calls its field one of "rapid technological advances" and the routing sends a
  business whose ten-year economics cannot be foreseen because its industry changes fast to TOO HARD here **[M1998-008]**.
  The record does not show the economics of this business moved by technology: the same product family has carried a
  rising maintenance line for ten years, and casino management systems in the filings are installed for multi-year terms.
  Whether the castle will hold against larger vendors as the systems change is a castle question and is put at Q2, where
  the framework places rapid change **[M2001-069]**.
- **Would the insiders write it down?** The economics of the installed base (how many casinos pay how much for maintenance)
  are the kind of figure a management states; the test of an industry whose insiders would call the forecast "too hard"
  **[M2000-105]** is not met by the maintenance line, which the company has reported every year.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. My doubt
  is about the durability of the position (Q2), not about how the business makes its money or whether the statements show it;
  the statements answer the economic questions this question asks.
- **VERDICT: IN.** The economics (a recurring maintenance stream on an installed base, plus lumpy installations financed on
  the company's own balance sheet) can be read from ten years of filings, and the key variable has been predictable through
  the 2020 closures **[M2012-065]**, **[M2008-033]**, **[M1998-044]**. The ten-year competitive position is carried to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and "How much do they depend on the genius of the lord in the castle?"
**[M1995-038]**. It starts from the attacker: "A truly great business must have an enduring "moat" that protects excellent
returns on invested capital." **[L2007-004]**.

- **What keeps it standing, on the filings.** Table Trac sells a full casino management system to casinos too small or too
  remote to be the large vendors' first target, finances the purchase itself over 6 to 72 months, and then holds them on
  maintenance contracts averaging five years (10-K FY2025, Notes 1 and 2). The record of that position: operators under
  contract 71 (FY2015), 77, 86, 93, 100 (FY2019), 100, 100, 100, 115 (FY2023), 115, 115 (FY2025); casinos "over 130"
  (FY2017) to "over 300" (FY2023 to FY2025) (Item 1 of each 10-K). The rows name such a niche as a moat: "very small markets
  that aren’t really too attractive to anybody with any sense to enter, and fanaticism in service" **[M2011-017]**; and
  "they’re of a size and have specialized skills that other organizations just can’t get into it" **[M1997-071]**. That is
  the case for the castle, and it is real for 2015 to 2023.
- **The attacker with money** **[M2011-015]**. The attackers are already inside the walls: Light & Wonder's 10-K for FY2025
  (`0000750004-26-000012`) states "Our principal competitors in CMSs include Aristocrat, IGT and Konami", and reports gaming
  systems revenue of $285M (2025), $302M (2024), $268M (2023), about 26 times Table Trac's whole revenue; it does not name
  Table Trac. Everi was bought by Voyager Parent, LLC (Apollo-managed funds) and its stock delisted on 2025-07-01 (8-K
  `0001193125-25-153550`), in the same transaction as "IGT’s Gaming & Digital business" (the 8-K's words), so two of the
  larger systems vendors are now one company under a private owner. Aristocrat and Konami are not SEC filers (no filing read). Against a field like
  this the rows warn: "We have found in a long life that one competitor is frequently enough to ruin a business."
  **[M2012-108]**. The filer agrees in its own words (Item 1A, quoted in the foundations above).
- **Pricing power and the agony before a rise** **[M2005-020]**. In ten 10-Ks the filer names one rate increase, in 2025
  ("due to the increase in our customer base and rates from 2024 to 2025", 10-K FY2025). Maintenance revenue per casino, on the
  filer's rounded counts, was about $17,500 in 2017 ($2.27M over "over 130") and about $20,500 in 2025 ($6.15M over "over
  300"): a rise of about 17% in eight years that spans the last inflation. The cost of maintenance rose faster: maintenance
  gross margin 86% in 2020 ($371,205 cost on $2,615,024), 81% in 2024, 79% in 2025 ($1,287,384 on $6,152,538). In 2024 the
  company paid a customer $275,000 "as a result of certain promotional software not performing in accordance with agreed
  upon specifications" (10-K FY2025, Note 1). None of this shows a business that prices without agony; none shows one that
  cannot price.
- **Unit volume and the low bid** **[M2017-009]**. Eight systems delivered in 2024, eight new customers in 2025, six systems
  in the second quarter of 2026 (10-Q). Against that, the operator count has not moved off 115 since FY2023, and
  maintenance revenue has been flat for six quarters (foundations, items 2 and 3). The filings give no retention or renewal
  rate, and do not say whether the flat count is a stale rounded figure or a net of losses; they do not say whether
  customers buy CasinoTrac as the low bid or for something they would not give up.
- **Would it stand without the lord** **[L2007-006]**. The founder designed the product and its patents (DEF 14A
  `0001437749-26-011855`) and is now President and Chief Technology Officer at 64; the CEO since 2026-01-01 is the CFO. The
  filer names key-person risk among 32 employees. Not decisive; weighed.
- **Widening or narrowing** **[M1999-108]**. For 2015 to 2023, widening on every count the filings give. Since 2023 the
  counts stop, operating income has fallen from $2.02M (2022) to $1.60M (2025) on flat revenue, selling and administrative
  cost has risen from $4.93M to $6.55M, and research spending tripled in 2025 ($243,357 to $771,060, Note 1) with patent
  filings for new products (10-Q). Whether that is widening or "A moat that must be continuously rebuilt will eventually be
  no moat at all." **[L2007-005]** cannot be read from these filings.
- **What could destroy, modify or reduce it** **[M2000-014]**: a larger vendor pricing for small casinos; customer
  consolidation (one customer was 33.9% of 2024 revenue and 47.5% of year-end receivables); the move of casino systems
  toward cashless and mobile play, which the filer's patent filings address; tribal sovereign immunity against collection
  (Item 1A).
- **Ask the competitors** **[M1999-130]**: not done; no competitor, customer or employee was contacted (blind desk run).
- **The competitor row** (same metric, each company's own filings, SEC XBRL company facts as transcription of each year's
  annual filing, latest filed value per year; operating income over revenue, summed over the whole span, never one year):

  | company | span | operating margin, span | range of single years | source (latest annual filing) |
  |---|---|---|---|---|
  | Table Trac (TBTC) | 2015-2025 | 11.2% (op. income $9.63M on revenue $85.8M) | -18.9% (2015), -7.8% (2020) to 21.7% (2021); 2021-2025 17.1% | 10-K `0001437749-26-009488` and the ten before it |
  | Light & Wonder (LNW) | 2015-2025 | 6.8% ($2.06B on $30.2B) | -37.1% (2015), -14.4% (2020) to 21.0% (2024) | 10-K `0000750004-26-000012` |
  | Everi (EVRI) | 2015-2024 | 11.4% ($0.81B on $7.06B) | -13.8% (2016), -1.4% (2020) to 29.9% (2021) | 10-K `0001318568-25-000004` |
  | Agilysys (AGYS) | FY2016-FY2026 (March years) | 0.2% ($4.6M on $2.01B) | -21.2% (FY2020) to 13.5% (FY2026) | 10-K `0001193125-26-234423` |
  | IGT PLC (now Brightstar Lottery) | 2015-2021 as filed | 9.7% ($2.90B on $30.0B) | -3.4% (2020) to 22.1% (2021) | 20-F `0001619762-22-000022`; later years restated to lottery only, not comparable |
  | Aristocrat, Konami, private systems vendors | | not SEC filers; no figures | | |

  Caveats: LNW and IGT carry heavy amortization of acquired intangibles and are mostly game-machine, lottery and digital
  businesses; Agilysys sells hospitality software (point of sale, property management) to casinos, not player tracking;
  every margin is a whole-company margin. No competitor reports a casino-management-system margin.
- **The field's returns over the last full cycle, judged in words.** Over 2015 to 2025 the field earned modest margins on
  revenue, swung to losses in 2020, and (for LNW and IGT) earned them on capital swollen by purchased goodwill. Table Trac
  earned the field's average margin over the span, worse than the field before 2021 (losses in 2015 and 2020, thin margins
  2016 to 2019) and at its top since. On the capital it actually needs, Table Trac's recent returns are high (operating
  income after a 25% tax on equity less cash and certificates of deposit: 43% in 2022, 26% in 2023, 28% in 2024, 26% in 2025;
  see AFTER THE STOP, Q3). So this is not a standing castle that protects only ordinary returns; the open question is
  whether it is standing.
- **A change for the better, section C.** The returns changed for the better from 2021. The business's volume has fallen
  since then: system revenue fell 47% in 2023 and 28.5% in 2025, total revenue 14.2% in 2023, and operating income held
  ($1.68M in 2023, $1.60M in 2025), with maintenance rising in 2023 on "the addition of maintenance coverage by one of our
  larger customers" (10-K FY2023). So the change has been through one fall in the business's own volume, and the
  section C condition is met on that reading; it is not what decides the box.
- **The parts table:** one reportable segment (10-K FY2025, Note 1); not applicable.
- **VERDICT: TOO HARD (WORK).** The castle that the record shows for 2015 to 2023 (a niche of small and tribal casinos,
  held on financed installations and five-year maintenance, against vendors many times larger) may still be standing, but
  the two facts that would show whether it is (whether customers are being lost as fast as they are won, and why the
  recurring line stopped growing at the start of 2025) are not in the filings. A moat about which that cannot be said is
  "tenuous in any way", and the rows' answer is "it’s just too risky. We don’t know how to valuate that, and therefore we
  leave it alone." **[M2000-019]**; the future of the castle cannot be judged, so the box is TOO HARD, not OUT
  **[M2006-013]**: nothing in the filings shows the castle open, and "If something’s important but unknowable, forget it."
  **[M2006-076]** does not apply because the deciding facts are knowable. **Cause: WORK.** The deciding question (retention
  and renewal of the installed base, and the cause of the maintenance plateau) is a matter of fact that the company could
  state and that the next annual report, the state and tribal gaming regulators' vendor records and competitors'
  announcements could show; it is not a forecast that the industry's insiders "would not want to put down on paper"
  **[M2000-105]**; "I haven’t done the work" **[M1994-026]**. The research pass is written at the end, steps 1 and 2 only,
  not run, and the COMPUTATION below decides under Part VII whether it is run at all.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read and are recorded under AFTER THE STOP, not weighed.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts, and the buyback line against the bottom of the computed range, under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The arithmetic is under COMPUTATION, NOT A CLEARANCE, below.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Fact under AFTER THE STOP.

---
## THE BOX
**TOO HARD (WORK), decided at Q2**: whether the installed base of small and tribal casinos is being kept (the operator
count has stood at 115 since FY2023 while eight to sixteen new customers were installed, and maintenance revenue has been
flat for six quarters) is knowable and not in the filings; research pass written (steps 1 and 2), not run. **Integrity
facts recorded, not judged** (a 2019 restatement for revenue recognition and three years of ineffective internal control,
under Q4 and Q5 below). COMPUTATION beside the price $5.37: value range $7.21 to $7.57 a share (all-equity, at the long
rate), fair price $4.63 (equity-only $3.35); no case of the central range earns the floor at the price, so by Part VII the
pass is closed unrun with a dated note for the register; the literal window beside gives $7.57 to $16.98 and a fair price
of $6.62, at which the pass would run.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down **[M1997-127]**, not weighed; the box is unchanged.

**Q3 (capital).**
- Capital the business needs (equity less cash and certificates of deposit; no debt): $3.49M (2022), $4.91M (2023), $4.58M
  (2024), $4.61M (2025) (balance sheets of the 10-Ks; certificates of deposit $1.50M at 2023 and $4.63M at 2024 year-ends).
  Operating income after a 25% tax on it: 43%, 26%, 28%, 26%. That is earnings after depreciation against capital employed;
  the cash test (cash earnings against capital spending) is the next line.
- Capital spending (equipment and capitalized software) $0, $0, $56k, $129k, $93k in 2021 to 2025, against depreciation and
  amortization $23k, $8k, $1k, $21k, $41k; the heavy draw is working capital: $2.07M absorbed over 2021 to 2025 (receivables
  including long-term, inventory, and the run-off of customer deposits), recast in `compute.py` from the filed cash-flow
  statements. Revenue went from $4.40M (2020) to $11.05M (2025) on it.
- Before 2021 the business earned little on any capital: operating loss in 2011, 2012, 2014, 2015 and 2020; operating
  margin 3.5% to 11.7% in 2016 to 2019 (XBRL from the 10-Ks).

**Q4 (the accounts).** The balance sheets, ten year-ends and the latest quarter, before the income account **[M2025-032]**
(thousands; `tools/run.py` first-filed values, checked against the filed statements; 2019 as restated in the FY2020 10-K):

| year-end | equity | cash (+ CDs) | receivables, current + long-term | inventory | customer deposits | debt |
|---|---|---|---|---|---|---|
| 2016 | 2,764 | n/a | 2,807 + n/a | 843 | n/a | 25 |
| 2019 (restated) | 4,357 | 1,264 | 2,252 + 91 | 1,264 | 254 | 0 |
| 2020 | 4,693 | 1,732 | 1,304 + 34 | 1,748 | 164 | PPP loan, forgiven |
| 2021 | 6,527 | 4,946 | 1,018 + 289 | 1,582 | 1,576 | PPP loan, forgiven |
| 2022 | 8,276 | 4,787 | 1,868 + 1,524 | 1,560 | 1,486 | 0 |
| 2023 | 9,900 | 3,490 + 1,503 | 2,109 + 891 | 2,904 | 786 | 0 |
| 2024 | 11,462 | 2,258 + 4,628 | 2,343 + 1,011 | 1,936 | 871 | 0 |
| 2025 | 12,844 | 8,236 | 2,763 + 422 | 1,615 | 114 | 0 |
| 2026-06-30 | 14,207 | 8,153 | 3,046 + 1,713 | 882 (+ 1,493 prepaid inventory) | 39 | 0 |

- What moved and why: equity rose from retained earnings ($3.06M in 2020 to $11.79M in June 2026); there is no goodwill and
  no purchased intangible, only $64k of capitalized software; cash became more than half of equity; receivables (including
  the company's own customer financing, 6 to 72 months) ran at 29% to 31% of revenue in 2022, 2024 and 2025 and rose by
  $1.65M in the first half of 2026; customer deposits, paid on signing, have run off from $1.58M (2021) to $39k (June
  2026), with three projects in backlog at 2025 year-end against five a year earlier (10-K FY2025, Backlog); the deferred
  tax liability rose to $935k (June 2026). The allowance for credit losses is $72k against receivables of $3.2M, with
  write-offs of $87k (2022), $40k (2023), $1k (2025).
- Prepaid expenses rose from $437k to $1,899k in the first half of 2026, the tell the rows name, "if some prepaid expense,
  deferred asset accounts start building up suspiciously high" **[M1995-064]**; the 10-Q says $1,492,514 of it is prepaid
  inventory, and inventory fell by $734k in the same half.
- **The restatement.** The FY2020 10-K (`0001437749-21-007795`, Note 2) restated 2019 and the first three quarters of 2020
  for misstatements in the treatment of system costs deferred on contracts not probable of collection and in the
  collectability assessment of extended-term contracts; 2019 receivables went from $4,791,559 as reported to $2,342,489,
  contract assets of $1,037,364 and contract liabilities of $3,148,410 went to zero, equity went from $4,617,246 to
  $4,357,224, and 2019 revenue from $7,505,371 to $7,908,461. Internal control over financial reporting was reported not
  effective for 2020 (revenue recognition), 2022 and 2023 ("significant, non-recurring events, and complex transactions"),
  and effective for 2021, 2024 and 2025. Auditor Boulay PLLP since 2015.
- Revenue on contracts not probable of collection is now taken as cash is received ($887,500 of installed systems off the
  books at 2025 year-end, $721,470 at June 2026); the policy errs toward later revenue.
- Stock pay is expensed ($105k to $219k a year, 2021 to 2025) and is charged as a cost in the computation below. No EBITDA
  or adjusted figure was found in the 10-Ks read; no earnings guidance was found in the filings read.
- PPP loan forgiveness of $473,400 was booked as other income in both 2020 and 2021 (10-K FY2021); it is removed from owner
  cash below.

**Q5 (the people): integrity facts recorded, not judged.**
- The restatement and the three years of ineffective control above. "There is seldom just one cockroach in the kitchen."
  **[L2002-039]** is the row a later run must answer on them; this run gives no verdict.
- Since 2026-01-01 one person is Chief Executive, Chief Financial and Chief Operating Officer (8-K `0001437749-26-000465`;
  DEF 14A). The founder, 25.51% holder, is Chairman, President and CTO. Zeff Capital, LP holds 9.98%; director Andrew
  Berger (AB Value Management, an investment partnership) 1.83%; all directors and officers 30.33% (DEF 14A, record date
  2026-04-02).
- The proxy's pay-versus-performance table prints 2025 net income as $1,576,428, which is the 2024 figure (2025:
  $1,626,620): an error in a filed document.
- No related-party transaction found: no instance found in the proxy or the 10-K FY2025 by a text search of both for
  "related part" and "related person".
- Pay (DEF 14A): the founder $341,864 salary and bonus in 2025; the CEO-CFO $294,313 plus $67,957 of stock; directors
  $26,125 to $27,875 each, cash. Options at the market price with a ten-year term: 20,000 and 30,000 at $2.42 (2021); on
  2026-08-07 100,000 at $4.51 to the CEO-CFO, vesting over four years (8-K `0001437749-26-027198`).

**Q6 (the money and the owners).**
- Dividends began in 2022: $95k (2022), $139k (2023), $139k (2024), $371k (2025); in 2026 a special $0.10 and $0.02 a quarter
  ($650k paid in the first half). Cash has still risen to $8.15M.
- Buybacks: 50,000 shares for about $44,000 in 2015 (about $0.88), 25,000 shares for $51,475 in 2019 (about $2.06), small
  amounts in 2014 to 2018 (10-Ks FY2015 to FY2019); none since 2019. **The buyback line (written back from the computation
  and committed with it):** every price paid ($0.88 to $2.06) sits far below the bottom of the computed range ($7.21 a share,
  central, at the long rate) and below the fair price ($4.63); the purchases are read by what they did. No price limit was
  stated in the programmes (the 2019 programme capped the sum, "not to exceed $600,000" for up to 200,000 shares).
- The retention record: from the end of 2022 to the end of 2025 the proxy's own total-shareholder-return line went from $100
  to $97.03 (DEF 14A, pay versus performance), while book value per share rose from about $1.80 to about $2.77.
- Shares outstanding 4,506,788 (2019) to 4,642,887 (2026): about 3% more in six and a half years, from stock pay. No
  acquisition and no stock-paid deal in the span.

**Q9 (debt and exposures).** No borrowings; a $500,000 line of credit, undrawn, renewed to February 2027. Cash held through
the IntraFi network in FDIC-insured slices (10-K FY2025, Note 1). Exposures: the company's own financing of customers
(receivables $4.76M at June 2026, about 29% of total assets), customers with sovereign immunity (tribal) or in foreign
jurisdictions where collection may be impractical (Item 1A), and concentration (one customer 34.7% of receivables at 2025
year-end).

**Q12 (how the money is made).** Casinos are a business the rows name: "It’s a dirty business" **[M2007-018]**. Table Trac
does not run casinos; it sells them player-tracking, loyalty-marketing and promotional systems. The named STOP is for a
casino to be bought and run; a marketable stake in a supplier would be a WEIGHING. Not judged.

---
## COMPUTATION, NOT A CLEARANCE
*(Q7's arithmetic after the STOP at Q2; no entry language; operator rule 3. Script and output:
`Test Runs/_research 2026-10-25 TBTC/compute.py`, `compute_output.txt`.)*

**Owner cash, recast from the filed cash-flow statements** (thousands; all-equity basis, so before interest: all interest
income removed after a 25% tax (run CONVENTION below); PPP forgiveness removed; stock pay charged as a cost; depreciation and
amortization taken as the maintenance spending, so netted; working capital counted as spending under specific (d)):

| year | maintenance-only owner cash | working capital (cash effect) | growth spending (capex above D&A + working capital absorbed) | all-spending owner cash |
|---|---|---|---|---|
| 2021 | 914.8 | +1,617.2 | -1,640.2 | 2,555.0 |
| 2022 | 1,943.9 | -2,344.1 | 2,336.2 | -392.3 |
| 2023 | 1,422.4 | -1,420.1 | 1,475.2 | -52.7 |
| 2024 | 1,429.8 | +275.5 | -167.5 | 1,597.2 |
| 2025 | 1,503.0 | -201.5 | 253.3 | 1,249.7 |
| **average** | **1,442.8** | | **451.4** | **991.4** |

- **Conventions of this run, confessed.** (i) CONVENTION: all interest income is removed for the all-equity basis, taxed at
  25%; rationale: the filer attributes its interest income to cash, certificates and money-market holdings, the interest on
  customer financing sits in the same line and cannot be split, and 25% is near the 2022 to 2025 effective rates (25.4%,
  19.8%, 25.3%, 22.2%). (ii) CONVENTION: maintenance spending is taken as depreciation and amortization; rationale: capital
  spending is about 1% of revenue and runs near it, and the filing gives no other guess. (iii) CONVENTION: where specific
  (a) applies and no full cycle has closed at the business's present scale, the five-year average stays the base and the
  growth is measured by (b)'s halves, the literal window beside; rationale: the only closed cycle (2015 to 2020) is of a
  business half the size, and (b)'s halves are the framework's own remedy for an end-year rate that means nothing.
- **The maintenance guess** (specific (e)): the filing allows it, so the central case is maintenance-only owner cash,
  $1,442.8k a year, with the growth spending ($451.4k a year over the window) charged against the growth it buys;
  all-spending beside.
- **The growth shown.** Literal, first year to last on the central series: 13.2% a year (2021 $914.8k to 2025 $1,503.0k).
  The first year is aberrational on the filer's own description: 2021 was the year of "the easing of limitations related to
  the COVID-19 pandemic" (10-K FY2021), with PPP forgiveness and a $260k deferred-tax swing; "a base year in which earnings
  were poor can produce a breathtaking, but meaningless, growth rate." **[L2005-003]**. Halves (2021 to 2022 average
  $1,429.4k; 2024 to 2025 average $1,466.4k; three years apart): **0.86% a year**, central. Sales grew 12.2% a year over 2021
  to 2025, so the cap (f) binds neither rate. Operating income on the same revenue fell from $2.02M (2022) to $1.60M (2025),
  which the halves rate reflects and the literal rate does not.
- **Growth bought below its cost: the inversion.** At 0.86% the growth case buys about $12k a year of added owner cash for
  about $455k a year of growth spending, so the growth case is worth less than the no-growth case: the no-growth case is the
  top of the range and the growth case the bottom, "growth can destroy value" **[L2000-023]**. Growth spending charged:
  $455.3k in year one, $491.6k in year ten, none after (specific (e)).
- **Net debt** (all-equity basis): no borrowings or finance leases; cash $8,152,589 at 2026-06-30 less the $0.02 dividend
  declared 2026-08-07, which the same 10-Q states as a subsequent event ($92,858): net cash $8,059,731. Operating leases
  left out ($411k of lease liabilities). Market value at $5.37: $24.93M; enterprise value $16.87M.
- **Tax** (Q7, Whose tax): owner cash after the company's own income tax as paid; no carryforward or credit shelter of size
  (research credits inside an effective rate of 22.2% in 2025); no conversion.

**The range** (each end discounted at the 30-year Treasury, 5.33%; ten years at the growth carried, then zero nominal growth;
the floor of about ten percent pre-tax, Q7's CONVENTION, tested first):

| case | whole business | per share (plus net cash) |
|---|---|---|
| no growth, maintenance-only (top, by the inversion) | $27.07M | **$7.57** |
| growth 0.86% with growth spending (bottom) | $25.41M | **$7.21** |
| *literal window beside:* growth 13.2% | $70.79M | $16.98 (range $7.57 to $16.98; width 2.24 a share, 2.62 whole) |
| *all-spending beside:* no growth on $991.4k | $18.60M | $5.74 |
| *equity-only beside (central):* | | $6.34 to $6.69 |

- **The floor, tested first.** At the price, the no-growth case yields $1,442.8k on an enterprise value of $16.87M, 8.55%;
  the growth case less. Valued at ten percent: no growth $4.84 a share, growth $4.41, both below $5.37. **No case of the
  central range earns the floor at the price**, so Q7, had it been reached, would close OUT whatever the width: "there’s just
  a point at which we drop out of the game" **[M2003-149]**. The width (1.05 a share) is then not the test.
- **On the literal window beside**, the growth case valued at ten percent is $8.39, above the price; the width is 2.24, under
  three to one; and the price is 29% below the bottom ($7.57). That would put the case to the screamer test, and with this
  file's certainty (Q2 unanswered, the recurring line flat for six quarters) the margin asked is large, "the larger the
  margin of safety" **[M1997-080]**; a case that turns on which growth rate is chosen needs a pencil, which the rows read as
  the sign it is not a screamer: "It should scream at you." **[M2009-005]**.
- **Outside the window, beside only:** the first half of 2026 was the best half in the record (net income $1,976,425 against
  $927,021, on system revenue of $3.70M against $1.84M); trailing twelve months to June 2026, revenue $13.33M and net income
  $2.68M. Maintenance in the same half was $3,106,761 against $3,090,774.

**Reporting figures (Part VII; a reporting convention, never a verdict or entry language; labelled COMPUTATION because the
file closed at Q2):**
- **(a) VALUE RANGE, Q7's construction: $7.21 to $7.57 a share** (all-equity basis, central; at 5.33%), against **$5.37**.
  Literal window beside: $7.57 to $16.98.
- **(b) FAIR PRICE** (each end case valued at ten percent, the two averaged; owner cash after the company's own tax, no
  conversion): **$4.63 a share on the all-equity basis (central)**; **$3.35 equity-only** (owner cash including the
  after-tax interest on the cash, $213.9k a year held flat, against the market value, no credit for the cash). Literal window
  beside: $6.62 all-equity, $5.34 equity-only. Growth spending in the central growth case $455k in year one, $492k in year ten,
  none after. Not a regulated utility; no debt credit.

**The research pass under Part VII.** A pass is run only where the COMPUTATION beneath the stop shows some case of the range
earning the floor at the price. In the central range none does ($4.84 and $4.41 at ten percent against $5.37), so the pass
below is written and closed unrun, with a dated note for the register (2026-10-25), and the file is re-looked under an alert
at the top of its computed range like any OUT ($7.57 a share, central). The dispatcher should know that the literal window
beside does have a case that earns the floor at the price, so a reader who rejects this run's halves convention would run
the pass.

---
## RESEARCH PASS (TOO HARD (WORK) at Q2): STEPS 1 AND 2 ONLY, NOT RUN
*(Part VII form, refined after the HRB pilot: each OUT answer one fact; each question with its span and source fixed before
any reading; an unanswerable question recorded and set aside. Written 2026-10-25, before any reading for it.)*

**Step 1.** "What do I not know that I need to know?" **[M1999-129]**
1. **(deciding)** Is the installed base being kept: the exact number of operators and of casinos under maintenance contract
   at each year-end from 2022 to 2026, and the operators lost each year? **Knowable**: the company counts its contracts and
   the 10-K reports a rounded count; it is important and knowable, not "important but unknowable" **[M2006-076]**.
2. Why did maintenance revenue stop growing after the first quarter of 2025 (lost customers, credits, rate cuts, shorter
   terms, or the timing of new contracts)? **Knowable.**
3. Has the customer that was 33.9% of 2024 revenue and 47.5% of year-end receivables stayed under contract and paid?
   **Knowable** (the filer's major-customer note; the company).
4. Have the larger vendors (Light & Wonder, Aristocrat, Konami, the combined Everi and IGT gaming company) converted
   CasinoTrac sites or priced into the small-casino niche? **Knowable in part** (competitor releases, state and tribal
   regulators' vendor records).
5. Where casino systems will be in ten years (cashless, mobile, hosted) and whether a 32-person vendor keeps pace. **Not
   knowable**: a forecast of the kind the industry's insiders would not write down **[M2000-105]**; recorded and set aside;
   not the deciding question.

**Step 2.** Evidence, span and source fixed; the single fact that closes OUT. The reading, step 3, is aimed "to possibly
reject your original hypothesis" **[M1998-144]**.
1. Evidence: exact year-end counts of operators and casinos under maintenance contract, and operators lost. Span: FY2022 to
   FY2026. Source: the 10-K for FY2026 (due about March 2027); the 10-Q for the third quarter of 2026; a written reply from
   the company. **OUT if:** the count of operators under maintenance contract at 2026-12-31 is below the count at
   2023-12-31.
2. Evidence: maintenance revenue by quarter and the filer's explanation. Span: first quarter 2024 to fourth quarter 2026.
   Source: the 10-Qs and 10-Ks for those periods. **OUT if:** maintenance revenue for FY2026 is below FY2025's $6,152,538.
3. Evidence: the major-customer note and any disclosed non-renewal. Span: FY2024 to FY2026. Source: 10-K FY2026, Note 1; the
   company. **OUT if:** the filer discloses the loss or non-renewal of a customer that was 10% or more of revenue in any
   year of the span.
4. Evidence: announced replacements of CasinoTrac by another vendor; approved-vendor records of the regulators in the states
   where the company is licensed (California, Iowa, Kansas, Louisiana, Maryland, Minnesota, Mississippi, Nevada, West
   Virginia, Wisconsin) and of the tribal gaming commissions of its customers. Span: 2023 to 2026. Source: competitors' 8-Ks
   and releases; regulator records; National Indian Gaming Commission public records. **OUT if:** five or more operators are
   documented as having replaced CasinoTrac with another vendor's system in the span. CONVENTION of this run: the figure of
   five; rationale: the form needs a single fact, the rows give no churn figure, and five is about 4% of the 115 operators.
- **How step 4 closes.** OUT on any one OUT fact above. IN on Q2 only if questions 1 and 2 both answer against OUT and
  neither 3 nor 4 closes it; the run then continues from Q2 to Q3. A pass that ends unsure ends TOO HARD (NATURE)
  **[M2002-092]**, never TOO HARD (WORK) a second time on the same question **[M2008-086]**. Any margin comparison in the
  pass covers the whole span 2015 to 2026; any capital test sets earnings after depreciation against capital employed, or
  cash earnings against capital spending, never one against the other.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Q1, after Q2, and after the
      computation and the close (pathspec commits of the run file and the research folder only).
- [x] Dispatched: the brief allowed the per-question commits; the lock and the register fold are the dispatching
      session's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the names seen by accident are
      declared under CONTAMINATION at the top and were not used; one listing of `Test Runs/` filtered to my own folder
      name, which returned nothing, is declared there too.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row's text (`check_ids.py`: PASS); no E-ids.
      Every filing fact carries its accession or names its filing.
- [x] The order was kept; Q2 closed the file; nothing after it is a clearance; Q3 to Q12 are marked NOT REACHED.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from the
      US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations, items 1 to 7); facts for later questions under AFTER THE STOP,
      with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the final commit.
- **Honest exceptions.** (1) Operator rule 9 asks to pre-register before computing. I did rough owner-cash and fair-price
  arithmetic in my head before Q2 was written, and ran `compute.py` before writing Q2 (it was committed with Q1). The Q2
  verdict rests on facts written in the foundations first (items 2 and 3), but I saw the numbers before deciding; weigh the
  Q2 call with that in mind. The first rough figures, on the literal growth rate, made the stock look near fair; the halves
  convention, adopted afterwards, made it look dearer; the box does not depend on either. (2) Competitor margins come from
  SEC XBRL company facts (transcription), not from reading each competitor's filed statements; LNW's 10-K FY2025 and
  Everi's closing 8-K were read in part. (3) The operator and casino counts are the filer's rounded "over" figures; the
  per-casino maintenance figures built on them are approximate. (4) Removing all interest income also removes the interest
  on customer financing, which the filer books in the same line; that understates owner cash by something like the $54k
  to $103k a year of interest income of 2015 to 2019, when cash was small.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The growth input decided the computation, and the text left the choice open.** Specific (b) uses halves where the
end-year rate is "meaningless" and does not say what makes it so; specific (a) sends an aberrational first year to the last
full cycle and does not say what to do when no cycle has closed since the business reached its present size. Here the
literal rate (13.2%) gives a fair price of $6.62, above the price, and the halves rate (0.86%) gives $4.63, below it; and
Part VII's rule for running a research pass turns on the same choice. I confessed a CONVENTION of this run and showed both.
(2) **Specific (e) speaks of capital spending above the maintenance guess; for this business the growth spending is almost
all working capital** (customer financing and inventory), and (d) and (e) had to be read together to charge it; a sentence
saying that working capital drawn for growth is growth spending under (e) would remove the doubt. (3) **The all-equity
basis removes interest on cash, but this filer books interest on customer financing in the same line**; the text has no rule
for a business that is partly its customers' lender; I removed all of it and said what that costs. (4) **The Q1 routing on
fast technology can be triggered by a filer's boilerplate**: this filer, like most software vendors, calls its field one of
"rapid technological advances"; the text does not say whether the filer's own risk-factor words decide Q1, and I read the
ten-year record instead and carried the question to Q2. (5) **Q12 names casinos as a business to be bought and run** and
says nothing of a supplier whose product is the casinos' loyalty marketing; a later run that reaches Q12 will need a line on
suppliers to a named business. (6) **Part VII's pass rule speaks of "some case of the range"** and does not say whether the
literal window shown beside the central range counts; I read it as the central range and flagged the other reading.
