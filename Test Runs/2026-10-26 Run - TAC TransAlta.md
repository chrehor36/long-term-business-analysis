# Company Run — TransAlta Corporation (NYSE: TAC; TSX: TA) — 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-26, after the run was committed: `PORTFOLIO.md` read for this one ticker; the operator does not hold this name.*

**Dispatched run.** Done by a dispatched analyst under the brief of 2026-10-26, which departs from
`Screens/_daily/_dispatch_brief.md` where it says (repository path; lines of evidence derived from the filing; rivals the
filing names; a 40-F filer read through its exhibits and 6-Ks; the Canadian sovereign). The lock in `Screens/_daily/` was
present when the run began (written by the dispatching session; not touched here). Working folder:
`Test Runs/_research 2026-10-26 TAC/` (notes, fetch and conversion scripts, the computation script; raw filings in its
gitignored `cache/`).

**Contamination, declared.** (1) Before the run file was written, a shell command meant only to create the run file listed
`Test Runs/` file names matching "TAC" or "TransAlta"; it printed three file names of other companies (a construction-machinery
company run twice, and a medical-device company), none about this company. Nothing in them was opened or used. (2) The
repository's recent commit subjects shown at session start name another company's run (a utility, closed at Q7); not used.
(3) The memory index loaded with the session mentions the queue state in general terms; it names no position in this
company and was not used.

**Lines of evidence chosen from the filing** (the brief's departure (1)): from the annual information form, Business of
TransAlta (six segments; 58 per cent of gross installed capacity in Alberta, sold merchant into the Alberta pool and hedged
as one portfolio) and Competitive Environment; from the MD&A's Risk Management section, the commodity-price risk (the Alberta
electricity price), the regulatory and market-design risk, the competition risk (newer, lower-heat-rate turbines; cogeneration
offered at low prices; corporate buyers adding renewables), and the Brookfield exchange right over the Alberta hydro assets.
So the run reads: (a) the Alberta pool price and TransAlta's results across a full price cycle; (b) the cost position of the
Alberta thermal fleet; (c) the parts and which decides; (d) the field's returns from the filer's and rivals' filings;
(e) the ten balance sheets; (f) the deals of 2023 to 2026 and their financing.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** C$17.14 on the TSX (close 2026-10-23, the last full session before the run; US$12.22 on the NYSE the same day).
  Source: Yahoo Finance chart API, an aggregator, **flagged** under operator rule 5 (live quote only). The earnings currency
  is the Canadian dollar, so the TSX price in C$ is used throughout.
- **Shares by class:** one class of common shares. `python Screens/cover_shares.py TAC` read **296,717,495** from the 40-F
  cover (filed 2026-02-27, period 2025-12-31, accession `0001144800-26-000015`). Checked against the filed statements:
  296.7 million at 2025-12-31, then **316.0 million issued and outstanding at 2026-06-30** (interim statements, note 11:
  +18.2 million in the bought deal of 2026-06-09 at C$19.20, +0.9 million share plans, +0.2 million options; 6-K filed
  2026-07-31, accession `0001144800-26-000040`, exhibit 99.3). The underwriters' over-allotment option (2,734,500 shares,
  30 days) is not shown exercised in the 2026-06-30 count, and no later filing read states an exercise; the run uses
  **316.0 million**. First preferred shares (carrying value C$942 million) and the Brookfield exchangeable securities
  (C$750 million) are senior claims, carried as debt-like at Q7.
- **Market cap:** 316.0 million x C$17.14 = **C$5,416 million**.
- **Sovereign for the earnings currency:** **4.12%**, the Government of Canada long-term benchmark bond yield (Bank of Canada
  series BD.CDN.LONG.DQ.YLD, observation 2026-10-23, fetched from the Bank of Canada Valet service). The issuing-authority
  table in the protocol covers USD, JPY and EUR only; for CAD the Bank of Canada, which publishes the Government of Canada
  benchmark series, is taken as the issuing authority's publisher, as the brief directs. FX where needed: 1.3993 C$ per US$
  (Bank of Canada FXUSDCAD, 2026-10-23).
- **Filings read** (operator rule 4):
  - 40-F for FY2025, filed 2026-02-27, accession `0001144800-26-000015`: the annual information form (exhibit 99.1), the MD&A
    (exhibit 99.2), the audited IFRS consolidated statements (tac-20251231.htm), including note 37 (segments).
  - 40-F for FY2024 (accession `0001144800-25-000006`, MD&A), FY2023 (`0001144800-24-000008`, statements and MD&A), FY2021
    (`0001144800-22-000004`, statements and MD&A), FY2019 (`0001628280-20-002853`, MD&A), FY2017 (`0001104659-18-014379`,
    MD&A exhibit 13.2): for the segment history, the Alberta pool price, sustaining capital and the ten-year cash flows.
  - 6-K of 2026-07-31 (`0001144800-26-000040`): interim statements and MD&A to 2026-06-30.
  - 6-K of 2026-06-09 (`0001171843-26-003988` and `0001193125-26-263706`): the bought deal closed.
  - 6-K of 2026-10-22 (`0001171843-26-006780`): the Colorado acquisition **closed** (Mountain Peak Power and Canyon Peak Power,
    US$1.0 billion including US$750 million of assumed senior secured project debt) and 49 per cent of the Oklahoma wind
    portfolio sold to Ares for US$305 million, the same day.
  - 6-Ks of 2026-06-15 and 2026-09-14 (US DOE orders keeping Centralia Unit 2 available), 2026-07-29 (dividends),
    2026-06-30 and 2026-10-06 (results-call notices).
  - The 2026 management information circular, 6-K of 2026-03-31, accession `0001144800-26-000019` (confirmed as the
    circular: ta2026managementproxycircu.htm).
  - XBRL company facts (ifrs-full) for the ten-year table, transcription only.
- **One figure cross-checked against the filed statement:** cash flow from operating activities FY2025 **C$646 million** in
  the filed consolidated statement of cash flows equals the XBRL fact (646); total assets at 2025-12-31 **C$8,661 million**
  in the filed FY2025 statement equal the comparative column of the 2026-06-30 interim statement.
- `python tools/run.py TAC`: **failed** ("no overlapping OCF/D&A/capex annual facts. UNRESEARCHED"); it does not read an
  IFRS 40-F filer. Every figure below is taken from the filed statements (and transcribed from XBRL where so marked), as the
  brief directs. Arithmetic is in `Test Runs/_research 2026-10-26 TAC/q7_computation.py` and `table.py`.

### The ten balance sheets, read first (Q4's rule, read here in case the file closes before Q4) **[M2025-032]**
C$ millions at Dec. 31, from the 40-F statements (XBRL transcription in `table_xbrl.txt`; 2025 column checked to the filed
statement):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Total assets | 10,996 | 10,304 | 9,428 | 9,508 | 9,747 | 9,226 | 10,741 | 8,659 | 9,499 | 8,661 |
| PP&E | 6,824 | 6,578 | 6,164 | 6,207 | 5,822 | 5,320 | 5,556 | 5,714 | 6,020 | 5,665 |
| Goodwill | 464 | 463 | 464 | 464 | 463 | 463 | 464 | 464 | 517 | 516 |
| Cash | 305 | 314 | 89 | 411 | 703 | 947 | 1,134 | 348 | 337 | 205 |
| Receivables | 703 | 933 | 756 | 462 | 583 | 651 | 1,589 | 807 | 767 | 699 |
| Borrowings (incl. leases) | 4,361 | 3,707 | 3,267 | 3,212 | 3,361 | 3,267 | 3,653 | 3,466 | 3,808 | 3,593 |
| Decommissioning and other provisions | 343 | 470 | 456 | 546 | 673 | 827 | 729 | 689 | 933 | 891 |
| Total equity | 4,663 | 4,385 | 4,134 | 4,062 | 3,436 | 2,593 | 1,989 | 1,664 | 1,843 | 1,465 |
| of which non-controlling interests | 1,152 | 1,059 | 1,137 | 1,101 | 1,084 | 1,011 | 879 | 127 | 97 | 66 |
| Retained earnings (deficit) | (933) | (1,209) | (1,496) | (1,455) | (1,826) | (2,453) | (2,514) | (2,567) | (2,458) | (2,730) |

Plus, from 2019, the Brookfield exchangeable securities (C$750 million, carried apart from borrowings) and, throughout,
C$942 million of first preferred shares inside equity.

What the figures say. Total equity fell from C$4,663 million to C$1,465 million in nine years; the deficit deepened by
C$1,797 million, in a decade that included the highest Alberta prices on the filer's record. Part of the fall in equity is
the 2023 purchase of the TransAlta Renewables minority (non-controlling interests C$879 million to C$127 million, paid
C$811 million in cash plus about 46 million shares), but the deficit line is the owners' own: net earnings attributable to
common shareholders, after preferred dividends, summed **minus C$546 million** over 2016 to 2025
(117, -190, -248, 52, -336, -576, 4, 644, 177, -190). Borrowings are about where they were (C$3.6 billion) while equity is a
third of what it was, so the debt now carries a far thinner cushion. Receivables jumped to C$1,589 million in 2022 with the
price spike and came back; they track prices, not a build. Provisions (mostly decommissioning and mine reclamation) more than
doubled, C$343 million to C$891 million, as coal units and the Highvale and Centralia mines moved into reclamation: a real
claim on future cash that sits outside borrowings. Goodwill is small and stable (the Heartland purchase added about C$53 million).
What they do not say: what the converted coal units will earn against new gas turbines, which is Q2's question; and what the
Alberta price will be, which no filing says ("we cannot precisely predict future electricity prices", MD&A, Risk Management).

## THE FOUNDATIONS (not a gate)
Two foundations bear on this name. A share is a business: the test is whether one would be content to own it if the market
closed **[M1997-109]**; here the cash comes from selling power whose price the owner does not set, so the owner must be ready
to see the earnings halve with the pool price, as they did from 2023 to 2025, and the price of the shares with them **[M2020-022]**.
Who is paid to tell you: the filer reports its segments, its outlook and its executives' pay on "adjusted EBITDA" and "free
cash flow", measures of its own making, and the bought deal of June 2026 was sold by an underwriting syndicate paid on the sale;
the buyer asks who gains by persuading him **[M2004-046]**. No macro view enters: the Alberta price is not forecast here;
its level enters only at Q7 **[M2000-094]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the filer's
own words that older facilities "may, over time, be unable to compete with newer, more efficient facilities", with two
Alberta gas units mothballed (Sundance 6 from 2025-04-01; Sheerness 1 from 2026-04-01); (2) a ten-year deficit of C$546
million to common shareholders across a full price cycle; (3) Brookfield's right, from 2025-01-01 to 2028-12-31, to exchange
its C$750 million into up to 49 per cent of the Alberta hydro assets, the lowest-cost part of the fleet; (4) penalties of C$33
million from the Alberta Market Surveillance Administrator in 2024 for Brazeau ancillary-service offers in 2021 and 2022, and
MSA payments of C$31 million (2015) and C$25 million (2016); (5) for the business, not against it: contracted assets with
investment-grade buyers (BHP, Amazon, Meta, Puget Sound Energy) and inflation clauses in most contracts.

## THE STANDING RULE
Not engaged by the analysis: the rule binds the buyer's conduct, "Never risk permanent loss of capital." **[L2023-005]**,
and nothing here proposes borrowing to buy or a size; it is noted that the target itself is levered (Q9's subject), which
would matter to a buyer only through his own sizing **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; the key variables and how predictable they are come first
  **[M1998-044]**.
- **What the business is, from the filing.** A generator of electricity: 922 MW of hydro, about 2,559 MW net of wind and
  solar, 3,414 MW net of Alberta gas (most of it former coal units converted to gas) plus contracted gas in Ontario, the US
  and Western Australia, the last Centralia coal unit (Washington) awaiting a contracted conversion to gas, and an energy
  trading desk (AIF, Business of TransAlta, accession `0001144800-26-000015`). Fifty-eight per cent of gross installed capacity
  is in Alberta, sold into the province's deregulated pool and hedged as one portfolio; the rest is mostly contracted.
- **The key variables.** (1) The Alberta pool price, which the filer does not set: C$18.28/MWh (2016), 22.19 (2017), 50.29
  (2018), 54.88 (2019), 47 (2020), 102 (2021), 162 (2022), 134 (2023), 63 (2024), 44 (2025) (MD&As FY2017, FY2019, FY2021,
  FY2023, FY2025); a one-dollar move changes 2026 adjusted EBITDA by about C$2 million after hedges (MD&A, 2026 Outlook).
  (2) Gas and carbon costs. (3) Supply added by others: the filer puts the 2025 fall to new gas and cogeneration supply and
  to corporate buyers adding renewables "solely for environmental, social and governance reasons". (4) The contracts:
  their terms and recontracting (most run into the 2030s and 2040s). (5) Policy and market design, which the filer says it
  cannot predict.
- **Are they foreseeable?** The contracted half is: fixed contracts with named, creditworthy buyers, read from the AIF tables.
  The merchant half depends on a commodity price the speakers do not forecast either: "We don’t think we can predict commodity
  prices." **[M2016-025]**. The framework places that dependence: it "is never by itself a STOP at Q1 or Q2"; Q1 asks whether
  the business can be understood from its figures **[M2023-031]**, **[M2008-069]**. It can: the figures show plainly how the
  business makes and loses money (a price-taker whose fixed fleet earns the spread between the pool price and its fuel and
  carbon cost, with hedges smoothing a year or two), and the ten years of statements tell me what the future statements will
  look like in kind, if not in level **[M2008-033]**. The product is electricity, not a technology bet; the change the filer
  describes (coal retired, gas and renewables added, data-centre load) is change in who supplies a commodity, which Q2 judges.
- **Routing.** Not a bank. Not fast-moving technology in the sense of **[M1998-008]**: the generating technologies are mature;
  what moves is supply and policy. A business of parts: read by its parts at Q2.
- **VERDICT: IN.** The economics can be pictured from the filings: a commodity seller whose earnings follow a price it does not
  set and a contract book that can be read; whether it has any protection is the castle question, not this one
  **[M1997-148]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. For a commodity seller the framework puts it as the low-cost question, read from the
filer's and its operators' filings: "we would measure it, probably, more by cost of production than we would by whether copper
was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**.

### The parts table (section B of the gaps case)
The filer reports six segments with different economics. Its only segment profit measure for 2021 to 2023 is "adjusted EBITDA"
(note 37); segment depreciation is disclosed for 2024 and 2025 only (MD&A FY2025, segment tables). C$ millions, 2021 to 2025;
2021 to 2023 as restated in the FY2023 40-F (`0001144800-24-000008`, note 37), 2024 and 2025 from the FY2025 40-F (note 37):

| Part | Adj. EBITDA 2021-25 | share | after D&A, estimated (CONVENTION below) | share | Castle | Decides |
|---|---|---|---|---|---|---|
| Gas (Alberta merchant converted-coal and peaking units, 2,512 MW net of 4,525 MW; the rest contracted cogeneration, Ontario, Western Australia) | 2,880 (488, 629, 801, 524, 438) | 38% | 1,766 | 36% | open: see below | **yes, the largest** |
| Hydro (922 MW; the Alberta Bow and North Saskatchewan systems merchant, the rest contracted) | 1,909 (322, 527, 459, 316, 285) | 25% | 1,707 | 35% | a low-cost position that stands; price set by others | no (close second) |
| Wind and Solar (mostly contracted; Alberta merchant wind) | 1,484 (262, 311, 257, 316, 338) | 20% | 483 | 10% | contracts to term; recontracting competitive | no |
| Energy Marketing (proprietary trading outside Alberta) | 689 (166, 183, 109, 146, 85) | 9% | 679 | 14% | none claimed | no |
| Energy Transition (Centralia coal, mine reclamation) | 530 (133, 86, 122, 89, 100) | 7% | 217 | 4% | a closing coal unit | no |
| Corporate | (581) | | (681) | | | |

**CONVENTION of this run:** for 2021 to 2023, where segment depreciation is not disclosed, each part is charged its 2024
level (Hydro C$41 million a year; Gas C$212 million, the fleet before Heartland; Wind and Solar 198; Energy Transition 66;
Energy Marketing 2; Corporate 18). Rationale: the parts rule asks for operating profit and the filer gives depreciation by
segment for two years only; the 2024 levels are the nearest filed figures. On both measures (the filer's own, and this
estimate) Gas is the largest part and no part carries more than half. The margin between Gas and Hydro after depreciation is
small (about one point) and rests on the estimate; the run therefore also reads Hydro's castle, below, and says what it would
change. The filer itself runs the two as one book: "The assets within the Alberta electricity portfolio are managed as a
portfolio [...] the hedges are primarily tied to our portfolio of gas facilities and also allocated to our portfolio of hydro
facilities" (MD&A FY2025, Alberta Hedging).

### The castle tests, on the deciding part (Gas, and through it the Alberta merchant fleet)
- **The money test: could a well-funded attacker take it?** The attack has already come, and it worked. The filer: "supply
  additions, notably natural gas and cogeneration, meant that the market was more supplied as compared to 2024", and the
  average pool price fell from C$63/MWh to C$44/MWh (AIF FY2025, Competitive Environment); Gas segment revenue fell on
  "Higher dispatch optimization due to lower market prices driven by new gas generation in Alberta" (MD&A FY2025, Gas
  segment): the newcomers' units run and TransAlta's are taken off. The speakers' test was whether money could do it: "if
  I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?" **[M2011-015]**, and in its
  failing form, "you can create another airline" **[M2013-054]**. A gas turbine can be bought and connected by anyone with the
  money; the filer adds that corporate buyers build renewables in Alberta "solely for environmental, social and governance
  reasons" whatever the price (MD&A, Risk Management). One attacker can be enough: "one competitor is frequently enough to
  ruin a business" **[M2012-108]**.
- **Pricing power.** None. The fleet sells at the pool price everyone gets; the price fell 30 per cent in 2025, and from
  C$162 (2022) to C$44 (2025), with no act of the filer's. The speakers' gas-station row is the case exactly: "whatever he
  charged for gas was my price." **[M2012-109]**.
- **The low-cost position.** Not the thermal fleet's. Most of its Alberta merchant gas capacity is old coal units converted
  to gas (Battle River 4 and 5, 1975 and 1981; Keephills 2, 1984; Sheerness 1 and 2, 1986 and 1990; Sundance 6, 1980; AIF
  FY2025 gas table). The filer's own risk factor: "older facilities may, over time, be unable to compete with newer, more
  efficient facilities that benefit from advances in power technologies and cost-efficient new technologies, including gas
  turbines with lower heat rates" (MD&A FY2025, Risk Management). It mothballed Sundance 6 on 2025-04-01 and gave notice to
  mothball Sheerness 1 from 2026-04-01, to return "when market fundamentals or contracting opportunities are secured" (AIF
  FY2025, Three-Year History). Units that come off when the price falls are the units at the top of the cost curve. The
  rows: "commodity businesses have risk unless you’re the low-cost producer, because the low-cost producer can put you out
  of business." **[M1997-010]**; "In an unregulated commodity business, a company must lower its costs to competitive levels
  or face extinction." **[L1994-035]**. A heat-rate figure for each unit against the newcomers' is not stated in the filings
  read; the filer's admission, the dispatch record and the mothballing are the cost evidence, and they run one way.
- **The customer and the low bid.** The pool takes the cheapest offers each hour; no buyer asks for TransAlta's megawatt-hour
  by name, and cogeneration owners offer "at low prices to ensure it is dispatched" (MD&A, Risk Management). The speakers'
  words for that indifference in their own commodity field: "most insureds don't care from whom they buy." **[L2004-003]**.
- **Widening or narrowing.** Narrowing: new efficient gas in 2024 and 2025, two units mothballed, a carbon price that rose from
  C$80 to C$95 a tonne in 2025 and bears hardest on the highest-emitting units (MD&A FY2025, Gas segment). "you do not want to
  have something whose competitive position is going to erode over time." **[M2007-117]**.
- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: more new supply; carbon and
  clean-electricity rules; a change in Alberta's market design. The filer: "We are not able to predict whether there will be
  any further changes in the regulatory environment, including potential carbon and other environmental regulations, changes
  in market structure or market design" (MD&A FY2025, Risk Management).
- **A change for the better, not credited.** Data-centre load (the Keephills MOU of 2026-02-26; a 230 MW AESO contract) and
  the filer's expectation of higher 2026 prices are a possible change. The framework credits a change for the better only on
  a full cycle in which the price behaviour held **[M2005-020]**, **[L1995-022]**; none has been seen.

### The field's returns over the last full cycle (section C)
The Alberta pool price ran a full cycle in the filer's own record: C$18 (2016) trough, C$162 (2022) peak, C$44 (2025) down
again. Over it:
- **TransAlta** (the 40-F filings above): operating income summed C$3,118 million over 2016 to 2025 on average total assets of
  C$9,677 million, **about 3.2 per cent a year before interest and tax**; net earnings to common shareholders summed **minus
  C$546 million**; the deficit deepened by C$1,797 million. The two peak years (2022 and 2023) produced C$648 million to
  common between them, less than the losses of 2020 and 2021 (C$912 million).
- **The rivals the filing names:** none. The AIF's Competitive Environment and the MD&A's competition risk describe classes of
  rival ("large utilities to small independent power producers, as well as private equity, pension funds, international
  conglomerates, traditional energy companies and technology firms") and name no company. **CONVENTION of this run:** the two
  largest SEC-filing merchant generators in North America, Vistra Corp. and NRG Energy, Inc., stand for the field's SEC filers;
  rationale: they sell into deregulated energy-only and capacity markets like Alberta's and file the same line items. The
  Alberta merchant peer most like TransAlta, Capital Power, files on SEDAR+ only and is **flagged as a non-filer** for this
  purpose; ENMAX, municipally owned, likewise. Same metric, operating income over average total assets, whole span, from
  their own 10-K XBRL (transcription in `rivals_xbrl.txt`):
  - **Vistra** (10-K for FY2025, accession `0001692819-26-000006`): operating income summed US$9,957 million over 2017 to
    2025 (losses in 2021 and 2022, then a strong 2023 to 2025) on average assets of US$29.7 billion, **about 3.7 per cent a
    year**.
  - **NRG** (10-K for FY2025, accession `0001013871-26-000004`): operating income summed US$12,681 million over 2016 to 2025
    on average assets of US$22.4 billion, **about 5.7 per cent a year**.
  Judged in words, as the convention asks: over a full cycle the field's durable players earn ordinary returns on what is
  invested, and TransAlta the lowest of the three, with its owners' equity shrinking. That is the case the framework sends to
  OUT: the moat is what "protects excellent returns on invested capital" **[L2007-004]**, and fewness of rivals does not cure a
  commodity field: "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. A return set by a
  regulator would be the exception **[M2009-104]**; none applies (the filer's regulated element is a small transmission
  business inside Hydro).

### Hydro, the close second, read so the reader can see what it would change
Hydro has the castle the Gas part lacks: it is the low-cost producer (no fuel; dams built 1911 to 1972, carried at C$514
million of PP&E against five-year adjusted EBITDA of C$1,909 million), and dams on the Bow and North Saskatchewan rivers
cannot be built again: "Being the low-cost producer, for example, is a terribly important moat." **[M2018-043]**. Its earnings
still move with the pool price it does not set (C$527 million in 2022, C$285 million in 2025). Two facts cut the common owner's
claim on it: Brookfield may, from 2025-01-01 to 2028-12-31, exchange its C$750 million of securities into up to 49 per cent of
the equity of TA Alberta Hydro LP at its "tax-affected equity value" (AIF FY2025, Exchangeable Securities); and the part does
not decide on either measure. Were the depreciation estimate wrong by enough to make Hydro the largest part, the Hydro castle
would stand and the file would pass to Q3; the run records this and decides on the filings as they stand.

- **VERDICT: OUT.** The deciding part, Gas (with the Alberta merchant fleet it is hedged with), sells a commodity at a price
  set by others, from a fleet whose oldest units the filer itself says may not compete with newer turbines and has begun to
  mothball; and the field's durable players, TransAlta lowest among them, earned ordinary returns over the full Alberta price
  cycle of 2016 to 2025. A castle shown open on the evidence closes OUT **[M2011-015]**; a high-cost producer in a commodity
  field is OUT **[M1997-010]**; a standing castle that protects only ordinary returns is OUT **[L2007-004]**. Price does not
  reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (Q2 OUT).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict (the ten balance sheets were read in Step 0).
## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 — WHAT IS IT WORTH. NOT REACHED as a verdict; the owner's reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.
## Q8 — BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED.
## Q10 — THE FAT PITCH. NOT REACHED.
## Q12 (optional) — PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## THE BOX
**OUT at Q2** (the castle: the deciding part, Gas with the Alberta merchant fleet, is a price-taker in a commodity market whose
old converted units the filer says may not compete with newer turbines, in a field that earned ordinary returns over the full
Alberta price cycle of 2016 to 2025); **integrity facts recorded, not judged** (Market Surveillance Administrator penalties;
see below). COMPUTATION, NOT A CLEARANCE: value C$21.56 a share (no-growth case alone, all-equity, cycle base, maintenance
case) against C$17.14; fair price not positive on the all-equity basis (minus C$2.01), C$6.43 on the equity-only basis.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2); each with its source **[M1997-127]**.)*

**Q3 (capital).** Depreciation ran C$529 to C$654 million a year (2016 to 2025, average C$591 million) against the filer's
"sustaining capital" of C$141 to C$254 million (average C$174 million; MD&As FY2017, FY2019, FY2021, FY2023, FY2025); the gap
was closed by retiring coal units and by growth spending on new wind (PP&E additions C$918 million in 2022 and C$875 million in
2023). Committed or announced: about US$600 million to convert Centralia Unit 2 to gas under a tolling agreement to 2044 (final
decision expected early 2027); the Colorado peakers (US$1.0 billion including US$750 million of assumed project debt, closed
2026-10-22); Far North (C$107 million, 2026-02-02); the Nova loan (US$75 million term loan and US$100 million revolver, 2025).
Sales were C$2,397 million in 2016 and C$2,405 million in 2025.

**Q4 (the accounts).** The filer features "adjusted EBITDA" and "free cash flow" (non-IFRS) in its results, its outlook and its
pay plans; it gives an annual outlook range, and 2025 adjusted EBITDA "came in below the lower end of the range of management's
Outlook" (MD&A FY2025). The 2024 Brazeau penalties were excluded from adjusted revenues and adjusted OM&A as not "ongoing
performance". Impairment charges recurred in eight of ten years (C$648 million in 2021). Unrealized mark-to-market losses of
C$289 million in 2025 (Wind and Solar virtual power purchase agreements, hedge-accounted from 2026). The company's 2025 FCF as
it defines it was C$514 million (circular), against C$309 million of owner cash to common after all spending computed here,
the difference being chiefly growth spending, which FCF leaves out. These are the habits the framework records at Q4 as a
weighing and carries to Q5.

**Q5 (integrity facts; recorded, not judged).** (1) On 2022-11-30 TransAlta self-reported to the Alberta Market Surveillance
Administrator offers of active spinning reserve at Brazeau when the unit "was not properly configured to do so between Aug. 13,
2021, and Nov. 1, 2022" (MD&A FY2024, accession `0001144800-25-000006`); penalties of C$33 million were assessed in the fourth
quarter of 2024 and paid in the first quarter of 2025 (MD&A FY2025). (2) Payments to the MSA of C$31 million in 2015 and
C$25 million in 2016 (MD&A FY2017, accession `0001104659-18-014379`; the underlying matter was not read in this run). (3) The
MD&A says the company "conducts internal reviews of its offers and offer behaviour in both the energy and ancillary services
markets in Alberta on an ongoing basis and will self-report suspected contraventions". (4) Chief executive succession: John
Kousinioris retired 2026-04-30; Joel Hunter, chief financial officer since July 2024 and formerly CFO of TC Energy, succeeded him.
(5) Pay (2026 circular, `0001144800-26-000019`): the annual incentive weights free cash flow at 50 per cent; performance share
units vest on three-year cumulative adjusted EBITDA, three-year cumulative FCF per share and relative TSR; the CEO's 2025 total
compensation was C$7,049,277, in a year of a C$158 million net loss.

**Q6 (money and owners).** Buybacks under a normal course issuer bid with no stated price: C$68 million (2019), C$57 million
(2020), C$52 million (2022), C$87 million (2023), C$143 million (2024), C$24 million (2025, 1,932,800 shares at an average
C$12.42). Issued 18,230,000 shares at C$19.20 on 2026-06-09 to fund the Colorado purchase. The 2023 TransAlta Renewables
minority bought for C$800 million cash and about 46 million shares. Brookfield holds 26,923,345 common shares (9.1 per cent)
and nominates two directors while it holds the exchangeable securities. A shareholder rights plan runs to the 2028 meeting.
The Board "has not adopted a formal dividend policy" (AIF). Minority sales: 49 per cent of the Oklahoma wind portfolio to Ares
for US$305 million (2026-10-22).

**Q9 (debt and exposures).** At 2026-06-30: credit facilities, long-term debt and leases C$3,489 million (of which non-recourse
C$1,447 million); exchangeable securities C$750 million (current); first preferred shares C$942 million; cash C$302 million
(interim statements). Added after: US$750 million of senior secured project debt assumed with the Colorado plants. Credit
ratings: Morningstar DBRS BBB (low), S&P BB+ (AIF FY2025). In 2025 interest expense (C$347 million) exceeded operating income
(C$140 million). Decommissioning and reclamation provisions C$891 million (2025). Risk-management liabilities C$674 million
against assets of C$202 million at 2026-06-30. Hydro dam-failure risk named in the risk factors. Centralia Unit 2 has been held
available by successive US DOE orders since 2025-12-16, the latest to 2026-12-12.

**Q12.** The last coal unit (Centralia) runs under federal order; the remaining business is gas, hydro, wind and solar. No
business named in Q12's list.

## COMPUTATION, NOT A CLEARANCE
*(The file closed at Q2. These are the owner's two reporting figures, computed by Q7's convention as the brief asks; no
entry language; operator rule 3. Script: `Test Runs/_research 2026-10-26 TAC/q7_computation.py`.)*

**Owner cash** (C$ millions; filed cash-flow statements): operating cash flow, less capital spending, intangible spending,
lease principal, distributions to minority partners, preferred dividends and equity-settled stock pay; acquisitions net of
disposals deducted separately. Interest paid and cash taxes are inside operating cash flow (IFRS, as filed).

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| to common, after all spending | 156 | 7 | 299 | 218 | 41 | 296 | (314) | 281 | 355 | 309 |
| to common, after sustaining capital only | 260 | 127 | 426 | 494 | 370 | 577 | 462 | 982 | 524 | 396 |
| before interest (after its tax shield) and preferred dividends, sustaining only | 482 | 343 | 610 | 676 | 563 | 785 | 681 | 1,245 | 782 | 664 |
| acquisitions net of disposals | 0 | 0 | 30 | 117 | 32 | (8) | 10 | 811 | 217 | 0 |

**How the range is built, by Q7's convention and its specifics.**
- **(a) Cycle.** The five-year window 2021 to 2025 holds the peak of the Alberta price (C$162 in 2022, C$134 in 2023) and ends
  in a year the filer describes as one of "Lower power pricing in Alberta, subdued market volatility and lower wind resource",
  below its own outlook; the base is the last full cycle, trough to trough, **2016 to 2025** (pool price C$18 to C$162 to C$44),
  with the literal window beside.
- **(b), (f) Growth.** Growth between successive cycles cannot be measured with one full cycle on the record; between the
  cycle's halves it would compare a low-price half with a high-price half and is not meaningful, so the range is **the
  no-growth case alone, said so**. Any growth carried would in any case be cut by (f) to the business's own sales growth,
  which was about zero (C$2,397 million in 2016, C$2,405 million in 2025).
- **(c) Acquisitions.** Net purchases are deducted at their cycle average (C$121 million a year; the window's C$1,030 million is
  35 per cent of owner cash before purchases on the central case, below the serial-acquirer line). The Colorado purchase,
  closed 2026-10-22 after the window, has no filed earnings record of its own (one plant new, one just in service): credited at
  nothing, its financing (US$750 million assumed debt, US$250 million cash) added to net debt. The 49 per cent of the Oklahoma
  wind sold the same day: proceeds (US$305 million) deducted from net debt, and the share of cash sold removed from owner cash
  at the release's own figure, US$29 million a year (C$41 million). Far North (2026-02-02) is inside the 2026-06-30 balance
  sheet and credited at nothing.
- **(d) Working capital** is inside operating cash flow as filed.
- **(e) Maintenance.** The filing allows the guess (the filer's "sustaining capital"), so the central case charges sustaining
  capital only, with the all-spending case beside. The depreciation variant is shown too, because depreciation has run C$417
  million a year above sustaining capital over the cycle.
- **Basis.** Merchant generation stays on the all-equity basis (Q7, The regulated utility, last sentences); not a regulated
  utility. All-equity: owner cash before interest and preferred dividends (interest paid added back net of a 23.3 per cent
  tax shield, the filer's applicable rate) against market value plus net debt. **CONVENTION of this run:** the first preferred
  shares (C$942 million) and the exchangeable securities (C$750 million) are counted in net debt; rationale: both rank ahead of
  the common and carry fixed coupons, and the all-equity basis exists so that senior claims do not flatter the per-share
  figure. Net debt: C$3,489 million + C$750 million + C$942 million - C$302 million cash (2026-06-30) + C$972 million of
  subsequent financing net of the wind proceeds (at 1.3993) = **C$5,852 million**. Decommissioning provisions (C$891 million)
  are left out of net debt and their cash cost is inside operating cash flow, said so.
- **Rate:** 4.12 per cent (Government of Canada long benchmark, 2026-10-23); zero growth; shares 316.0 million.

**The figures.**

| Case | Owner cash a year | Value a share | At 10% (fair-price leg) |
|---|---|---|---|
| **Central: all-equity, cycle 2016-25, sustaining capital only, no growth** | 522 before interest | **C$21.56** | **minus C$2.01** |
| Equity-only beside (to common, after interest and preferred dividends) | 300 | C$19.99 | **C$6.43** |
| All spending (all-equity) | 225 | minus C$1.25 | minus C$11.40 |
| Depreciation in place of sustaining capital (all-equity) | 104 | minus C$10.50 | minus C$15.21 |
| Literal window 2021-25, sustaining only (all-equity; equity-only) | 585; 342 | C$26.41; C$23.16 | minus C$0.01; C$7.73 |

- **The floor, tested first.** At C$17.14 the central case returns about 4.6 per cent a year on the price of the whole
  business (522 on C$11,268 million of market value plus net debt) and 4.7 per cent on the equity-only basis, with no growth to
  add; the literal window gives 5.2 and 5.4 per cent. **No case earns the floor of about ten per cent at the price**, so Q7, had
  it been reached, would have closed OUT on the floor whatever the width **[M2003-149]**.
- **(a) VALUE RANGE: C$21.56 a share**, the no-growth case alone (all-equity, cycle base, sustaining capital only), against
  C$17.14; all-spending minus C$1.25 and the literal window C$26.41 beside.
- **(b) FAIR PRICE: not positive on the all-equity basis (minus C$2.01 a share); C$6.43 on the equity-only basis.** Each end case
  valued at ten per cent and averaged; with the range a single case, the two ends coincide. Tax: the company's own (cash taxes
  inside operating cash flow; no carryforward priced separately, since none was found running out inside ten years in the
  filings read).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `7527f735`); written question by question; committed after Step 0 to
      Q1 and after Q2, and at the close (write-early).
- [x] Dispatched: the brief allowed the per-question commits; the lock was present in `Screens/_daily/` (the dispatching
      session's, not touched); the fold is the dispatching session's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, except the one listing declared under
      contamination at the head of this file (a file-name filter on `Test Runs/`, run before the template copy, which showed three
      other companies' file names); nothing used.
- [x] Every v5 id resolves (check script `check_run.py`: every M/L/R id in `principle_ledger_v5.csv`, every quoted fragment
      beside an id in that row, no E-ids); every filing fact has its accession; numbers without a row are filed figures or
      labelled CONVENTION.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION, NOT
      A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from the
      Bank of Canada (the protocol's table has no CAD line, said so); the price quote is an aggregator's, flagged.
- [x] Contrary evidence written down as found, in the foundations; the facts for later questions are under AFTER THE STOP, with
      the integrity flag in the box line.
- [x] No point-in-time anchor; not applicable.
- [x] `tools/run.py` failed on this IFRS 40-F filer; nothing it printed was used. `Screens/cover_shares.py` gave the 40-F cover
      count, checked against the filed statements and the June 2026 offering.
- [x] `python tools/check_framework.py` PASS before the closing commit (see the commit).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The parts rule needs segment operating profit, and this filer reports none.** It reports adjusted EBITDA by segment, and
segment depreciation for two years only; on the filer's measure Gas leads (38 to 25 per cent), but after an estimated
depreciation Gas leads Hydro by about one point, and the two parts have opposite castles (Gas open, Hydro a standing low-cost
position). The rule has no measure for a filer without segment operating profit and no instruction for a near tie; the run
used the filer's measure and an estimate (a CONVENTION of the run), decided on Gas, and wrote what Hydro would change. A rule
for near ties (both parts read; or the filer's own measure governs) would stop the box resting on an estimate. (2) **Rivals
when the filing names none, and the natural peer files only on SEDAR+.** The brief allows a convention; US merchant generators
sell into different markets, and the comparison is weaker for it. (3) **Specific (a) with one full cycle.** Growth "between the
averages of successive cycles" cannot be measured when the record holds one cycle; the run fell back on (b)'s no-growth case,
which the text allows only for a meaningless rate; the two paragraphs could say so together. (4) **Specific (e) assumes the
maintenance guess is adequate.** Here the filer's sustaining capital is about 30 per cent of depreciation in a fleet that has
been shrinking (4,464 MW of coal retired since 2018) and replaced by growth spending; the central case on that guess (C$21.56)
and the depreciation variant (minus C$10.50) are far apart. The rows call depreciation charges "almost always true costs" **[L2015-004]**, and the
text gives no test of a maintenance guess against it. (5) **Net debt's definition names borrowings and leases only**; preferred
shares and exchangeable securities, senior to the common, are not named, and the run counted them (a CONVENTION). (6) **A
partial sale after the window** (49 per cent of a wind portfolio) is not covered by the convention for deals closed after the
window, which speaks of purchases; the run deducted the proceeds from net debt and removed the share sold at the release's own
adjusted-EBITDA figure, a forecast, said so. (7) **The CAD sovereign** is not in the protocol's table; the Bank of Canada's
long benchmark was used as the brief directs.
