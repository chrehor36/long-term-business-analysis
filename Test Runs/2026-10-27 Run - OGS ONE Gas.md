# Company Run — ONE Gas, Inc. (NYSE, NYSE Texas: OGS) — 2026-10-27
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch (commit 8157df1c). Dispatched blind run
under `Screens/_daily/_dispatch_brief.md`, with the two departures the brief states (the repository path, and the lines of
evidence and competitors derived by the analyst). Research folder: `Test Runs/_research 2026-10-27 OGS/` (notes, scripts,
the arithmetic outputs; raw filings in its ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-27: the operator does not hold this name (`PORTFOLIO.md` has no OGS row).*

**Contamination, declared.** (1) Before copying the template I listed `Test Runs/` filtered by this company's name to check
for a file-name collision; it printed `2026-10-18 Run - OGS ONE Gas.md` and `_research 2026-10-18 OGS`. Neither was opened,
read or used. The listing was itself a search of `Test Runs/` by this name, which the blind rule forbids; declared here.
(2) The dispatch context showed the last commit subjects of the repository: an XEL re-run closed OUT at Q5 on integrity.
Another company; not used. (3) The memory index loaded with the session names queue counts and holdings-review owing in
general terms; nothing about this name. Not used.

**Lines of evidence chosen** (the brief's second departure: derived from the 10-K's Item 1, Item 1A and Item 7, and said
why): (i) the regulatory construct, jurisdiction by jurisdiction (Item 1, Regulatory Overview: authorized ROE, equity
ratio, interim capital trackers), because the regulator sets the return and therefore the economics; (ii) the capital
programme and how it is funded (Item 7, Capital Expenditures; Liquidity: commercial paper, notes, forward equity sales),
because rate base grows only by spending and the spending is financed with new debt and new shares; (iii) Winter Storm
Uri of February 2021 and its securitization in all three states (Item 7 and the cash-flow statement), because it is the
one event in the window that demanded a sudden large sum and it distorts every cash figure of 2021 to 2023; (iv)
competition from electricity and fuel switching, and customer growth (Item 1, Competition; Item 1A, climate and
legislative risks), because that is the only attacker the filing names; (v) how management reports and is paid (Item 7's
non-GAAP measure, the earnings releases' guidance, the proxy), because Q4 and Q5 read it.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $78.36, close 2026-10-26, as printed by `python tools/run.py OGS` (**aggregator, live quote only, flagged**
  under operator rule 5).
- **Shares by class** from the latest filing's cover: 62,856,270 common shares, $0.01 par, one class (10-Q for the quarter
  ended 2026-06-30, filed 2026-08-05, accession 0001587732-26-000035, cover as of 2026-07-24; `python Screens/cover_shares.py OGS`).
  Check: the same 10-Q's balance sheet shows 62,797,154 shares issued and outstanding at 2026-06-30 and no treasury line
  (issued equals outstanding); the 59,116 difference is plan issuance between the dates. After the 10-Q: forward sale
  agreements outstanding at 2026-06-30 for 506,607 shares at $81.90 (net proceeds $41.5M available, 10-Q, "Total forward
  sale agreements"); the 8-K of 2026-08-13 (accession 0001193125-26-349155) is a debt issue and adds no shares. Count used:
  62.856M; the forward shares would add 0.8% with their cash, immaterial to the box and said so.
- **Market cap:** 62.856M x $78.36 = **$4,925M**.
- **Sovereign for the earnings currency (USD):** **5.31%**, US Treasury daily par yield curve, 30-year, 2026-10-26 (issuing
  authority, as printed by `tools/run.py` from `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-19, accession 0001587732-26-000009 (Items 1, 1A, 7,
  8 read: business, regulation, risks, MD&A, statements of income, balance sheets, cash flows); 10-K for FY2023
  (0001587732-24-000013) and FY2020 (0001587732-21-000030) for the cash-flow statements of 2018 to 2023; 10-Q for Q2 2026
  (0001587732-26-000035); DEF 14A filed 2026-04-01 (0001193125-26-137922); 8-Ks: earnings releases of 2024-02-21
  (0001587732-24-000010), 2026-02-18 (0001587732-26-000006) and 2026-08-04 (0001587732-26-000033); officer and board
  changes 2026-02-18 (0001193125-26-057048) and 2026-07-13 (0001193125-26-302034); the $375M 5.45% notes of 2026-08-13
  (0001193125-26-349155); the equity distribution agreement of 2026-02-24 (0001193125-26-064564).
  **One figure cross-checked against the filed statement:** FY2025 net income $264,224 thousand on the filed Consolidated
  Statement of Income (10-K, accession 0001587732-26-000009) equals the XBRL fact 264.2M; FY2025 total equity $3,440,123
  thousand on the filed balance sheet equals the 3,440 printed in `tools/run.py`'s ten-year table.
- `python tools/run.py OGS`, arithmetic lines only (Part VII): its owner-earnings window stops at 2023 (D&A and capex not
  tagged under the elements it reads after 2023), its D&A column is wrong (it found only amortization of intangibles; the
  filer tags depreciation as `UtilitiesOperatingExpenseDepreciationAndAmortization`), and its operating cash includes
  the Uri securitization proceeds of 2022 and 2023. **None of its owner-earnings figures is used.** Every figure below is
  taken from the filed statements. Its ten-year balance-sheet table and its price and share lines are used, each checked.

**Owner cash as Q4 recasts it** (USD millions; filed cash-flow statements; arithmetic in
`Test Runs/_research 2026-10-27 OGS/scripts/q7.py`, output in `q7_output.txt`):

| FY | net income | D&A | of which KGSS-I securitized amortization | capex | asset removal costs | total spending | maintenance guess (D&A less KGSS-I) | growth spending | owner cash after maintenance (equity) | after all spending |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 206.4 | 207.2 | 0 | 495.2 | 49.0 | 544.3 | 207.2 | 337.0 | 206.4 | -130.6 |
| 2022 | 221.7 | 228.5 | 12.1 | 609.5 | 47.0 | 656.5 | 216.4 | 440.1 | 221.7 | -218.4 |
| 2023 | 231.2 | 279.8 | 30.2 | 666.6 | 62.0 | 728.7 | 249.6 | 479.0 | 231.2 | -247.8 |
| 2024 | 222.9 | 296.7 | 27.7 | 703.2 | 59.0 | 762.1 | 269.0 | 493.1 | 222.8 | -270.2 |
| 2025 | 264.2 | 317.3 | 32.2 | 707.2 | 52.3 | 759.5 | 285.1 | 474.4 | 264.2 | -210.2 |
| **avg** | | | | | | **690.2** | **245.5** | **444.7** | **229.3** | **-215.4** |

Stock pay ($10.5M to $14.8M a year) is charged inside net income and not added back. Income tax is charged at the book
figure (deferred taxes not added back; the cash-tax variant is shown at Q7). The KGSS-I securitized intangible's
amortization and the KGSS-I bond repayments are left out together, with the dedicated Kansas securitization charge that
pays them (Q7, The regulated utility: securitization bonds "left out with the charge"); the 2022 amortization is the
issue proceeds less the year-end balance, an approximation, said so. Total spending agrees with the 10-K's own "Capital
expenditures and asset removal costs" of $728.7M, $762.1M and $759.5M for 2023 to 2025.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety: a regulated utility is the plainest case of a business
whose value can be computed, and so the plainest case where the computation must "scream" and not need a pencil: "if you
have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. Second, a share is a
business: the question is what the regulated franchise will pay its owner after the capital it must keep putting in, not
what the quotation does **[M1997-109]**. No macro forecast enters (gas prices pass through to customers at cost; interest
rates enter only as the sovereign at Q7) **[M2000-094]**. Who is paid to tell you: the company's own long-term growth
outlook ("7 to 9 percent" adjusted net income growth) is a projection by the party that sells the shares it issues every
year; it is not used **[M1995-050]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the company issues
new shares every year from 2022 to 2026 (forwards, at-the-market programmes) to fund a capital programme three times its
depreciation; (2) its earned return on book equity, 7.6% to 8.1% in 2024 and 2025, sits below every authorized return it
lists (9.4% to 9.8%); (3) one week of weather in February 2021 (Winter Storm Uri) forced about $2.5 billion of new
borrowing on a company whose equity was $2.3 billion; (4) the filing names fuel switching to electricity as the one
competitor, at the moment a customer installs equipment; (5) from February 2026 the company leads its releases with a
non-GAAP "adjusted" net income and guides on it.

## THE STANDING RULE
Blind run: the buyer's financing and size are not known to the analyst. A purchase of these shares for cash, unlevered,
sized so that a total loss could be borne, puts the buyer at no risk of ruin; bought on borrowed money it would be the
conduct the rule forbids: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "never risk permanent
loss of capital" **[L2023-005]**. Nothing about the target changes this line.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; "a reasonable probability of being able to asses where the
  business will be in 10 years" **[M2000-037]**.
- **The key variables** **[M1998-044]**: (1) rate base, which grows by the capital spent above depreciation (net PP&E
  $7,122M at 2025-12-31, 10-K balance sheet); (2) the return each regulator allows on it: Oklahoma 9.40% ROE on a 59%
  equity ratio and rate base $2,453M; Kansas 9.60% embedded in the GSRS carrying charge, rate base about $1,468M, no
  determined equity ratio; Texas 9.80% ROE on a 60% equity ratio and rate base about $1,887M (10-K Item 1, Regulatory
  Overview table); (3) regulatory lag between spending and rates, cut by the PBRC (Oklahoma), GSRS (Kansas) and GRIP (Texas)
  interim mechanisms and Texas House Bill 4384 (deferral of depreciation, taxes and a carrying cost on plant not yet in
  rates, from 2025); (4) customers, about 2.3 million, growing by about 23,000 new connections a year (10-K Item 7: average
  customers 2,281 thousand in 2024 and 2,295 thousand in 2025); (5) the gas price, passed through without markup
  ("These costs are passed on to customers without markup", Item 1 note 5), which moves revenue and working capital, not
  operating income.
- **Are they foreseeable?** Each of (1) to (4) is set in public proceedings with stated formulas and dates (Oklahoma must
  file a full rate case by 2027-06-30 on a 2026 test year; Texas consolidated its service areas in February 2026). The
  industry's insiders do write the forecast down: the company itself publishes a five-year capital and earnings outlook,
  so by test 5 this is not the case of "That’s too hard." **[M2000-105]**. The product is not changing fast; the threat is
  slow (electrification), and Q2 owns it **[M1999-063]**. The figures tell the future figures in the way **[M2008-033]**
  asks: rate base times allowed return, less lag.
- **Inside the perimeter?** Yes, without doubt: one segment, three regulated distribution divisions, no trading operations
  ("We do not utilize financial derivatives for speculative purposes, nor do we have trading operations", 10-K Item 1). It
  is not a financial institution and has no unreadable book. The doubt test **[M2002-092]** is not triggered.
- **VERDICT: IN.** The ten-year economics are "important and knowable" **[M2006-076]**: the deciding numbers are the
  regulators' allowed returns and the size of the spending, both on the public record.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- **The parts table.** One reportable segment ("We operate in one reportable business segment", 10-K Note 1); three
  divisions under three regulators with the same economics. The whole is the deciding part, and it earns a
  regulator-allowed return (Q7, The regulated utility, applies).
- **The castle tests, each with its filing fact.**
  - *Why is it still standing* **[M1995-038]**: it holds the franchise to distribute gas to about 89%, 72% and 13% of the
    gas-distribution customers of Oklahoma, Kansas and Texas (10-K Item 1), through a buried network a rival would have
    to duplicate street by street, under regulators that set its rates "to earn a fair and reasonable return on their
    investments" (Item 1). The reason is a natural monopoly under licence, not the genius of the lord.
  - *The attacker with money* **[M2011-015]**: a hundred million, or ten billion, would not build a second gas network in
    Tulsa or Wichita that a regulator would let earn a return; the answer is no. In Texas the filing names competition
    "from other local distribution companies" (Item 1, Competition), and for large industrial customers "from other
    pipelines", met with negotiated transport rates below tariff where "a competitive pipeline is in close proximity".
  - *Pricing power and the agony before a rise* **[M2005-020]**: none of its own. Every increase is asked of a regulator
    (2025: Oklahoma asked $41.5M, settled $41.1M; Texas asked $41.1M at 10.4% ROE, settled $15.0M at 9.8%; 10-K
    Regulatory Activities). The regulator is the prayer session. Against that, the formula mechanisms (PBRC, GSRS, GRIP)
    pass capital into rates annually.
  - *Unit volume and share of mind* **[M1999-054]**: sales volumes 156.6, 143.2 and 157.3 Bcf in 2023 to 2025 move with
    weather (HDDs 80% to 94% of normal); average customers rose from 2,281 thousand to 2,295 thousand in 2025, about 0.6%.
  - *Would the customer still choose it over the low bid* **[M2017-009]**: the choice is made once, at installation:
    "Customers and builders typically make the decision on the type of equipment, and therefore the energy source, at
    initial installation, generally locking in the chosen energy source for the life of the equipment" (Item 1). The
    customer cannot choose another gas distributor in Oklahoma or Kansas; he can choose an electric heat pump.
  - *The low-cost position* **[M2004-091]**: gas against electricity for heat is a cost question the filing frames as
    "comparative prices" and "perceived value of natural gas relative to other energy sources" (Item 7, Executive Summary);
    no filing figure states the comparison. Not judged on a number.
  - *Widening or narrowing* **[M1999-108]**: 23,000 new connections a year (Item 7) and a new $120M lateral to serve a
    generating plant in southeast Oklahoma (Item 7, Recent Developments, 2025-12-18) show the network still extending;
    the earned return on book equity has slipped from 9.0% (2019 to 2022) to 7.6% and 8.1% (2024, 2025), below every
    authorized return the filing lists, which is the regulatory lag and the equity issuance showing.
  - *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: (a) fuel switching by policy or
    price ("fuel switching from natural gas to other energy alternatives", Item 1; greenhouse-gas legislation, Item 1A);
    (b) the regulatory compact itself, the risk the rows name for utilities: "I did not anticipate or even consider the
    adverse developments in regulatory returns" **[L2023-011]**; the filing's own words: "there can be no assurance that we
    will be able to obtain rate increases, fully recover our costs" (Item 1A); (c) one event: Uri (below, Q9). None of
    these is a fast change; "slow change can be much harder to perceive" **[M2014-038]**, so it is carried, not dismissed.
- **The competitor row** (the 10-K names no rival company: Item 1 names only "other local distribution companies" in Texas
  and "other pipelines", unnamed; Item 1A none). **CONVENTION of this run:** the three comparables are Atmos Energy (ATO),
  Spire Inc. (SR) and Northwest Natural Holding (NWN); rationale: SEC-filing, mainly regulated gas distributors, and Atmos
  serves Kansas and Texas beside OGS; all three appear in the proxy's own benchmarking peer group (DEF 14A, 0001193125-26-137922),
  so the choice is not the analyst's alone. Metric: net income to common over average book equity, each filer's 10-K
  XBRL facts (script `scripts/peers.py`, output `peers_roe.txt`).

| FY | OGS (Dec) | ATO (Sep) | SR (Sep) | NWN (Dec) |
|---|---|---|---|---|
| 2016 | 7.5% | 10.5% | 8.6% | n/a |
| 2018 | 8.6% | 13.9% (tax-reform year) | 10.1% | 8.6% |
| 2019 | 9.0% | 9.7% | 7.5% | 7.6% |
| 2020 | 9.0% | 9.6% | 2.9% | 8.8% |
| 2021 | 9.0% | 9.1% | 9.9% | 8.6% |
| 2022 | 9.0% | 8.9% | 7.5% | 8.2% |
| 2023 | 8.6% | 8.7% | 7.1% | 7.6% |
| 2024 | 7.6% | 9.1% | 7.7% | 5.9% |
| 2025 | 8.1% | 9.3% | 7.7% | 7.9% |

  Accessions of the latest year: OGS 0001587732-26-000009; ATO 0000731802-25-000056; SR 0001193125-25-282583; NWN
  0001733998-26-000012 (the earlier years' accessions are in `peers_roe.txt`). ATO FY2017 is not in the facts read.
- **The field's returns over the last full cycle**, judged in words: across ten years and four filers the regulated gas
  distributors earn high single digits on book equity, with OGS in the middle of the four and below its own authorized
  returns lately. That is an ordinary return, set by regulators, not a moat return. The rows send the standing castle that
  protects only ordinary returns to OUT, with one exception: "A return set by a regulator is the exception, carried to Q3
  as a second best" (Q2, What it rules OUT), on the rows "there’s no way we get rich on our utility investments. But
  there’s no way we get poor, either." **[M2009-104]** and "decent returns on the incremental sums they invest"
  **[L2009-012]**. This is that exception.
- **VERDICT: IN.** The castle stands because it is a licensed natural monopoly that no attacker with money can duplicate
  **[M2011-015]**; what it protects is a regulated, ordinary return, carried to Q3 as a second best **[M2009-104]**. The two
  long threats, electrification and the regulatory compact **[L2023-011]**, are slow and are carried to Q7's certainty and
  to Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**: net income over average book equity 7.5% to 9.0% across
  2016 to 2025 (table at Q2). Goodwill is $158M and unchanged since 2016, so tangible and book returns are nearly the same.
  Book equity is the right base here because the regulator sets the return on it **[M2009-104]**.
- **Reinvestment to stand still and to grow.** Total spending (capex plus asset removal) averaged $690M a year over
  2021 to 2025 against depreciation, net of the Kansas securitized amortization, of $246M: 2.8 times. Guidance for 2026 is
  "approximately $800 million", of which "approximately $230 million" is for extensions to new customers (earnings release
  2026-08-04); the 2024 release put "nearly 75 percent" into "system integrity and replacement projects" (earnings release
  2024-02-21). So most of the spending replaces old pipe; under original-cost rate-making it still grows rate base and
  earnings, which is why the maintenance guess at Q7 is depreciation **[M1998-127]** and the replacement spending is
  charged as growth spending against the growth it buys (specific (e)). The rows' utility arithmetic: "To earn more,
  their owners must invest more" **[L2011-019]**.
- **What the added capital earns.** Over 2020 to 2025 net income rose $67.8M (196.4 to 264.2) while book equity rose
  $1,206.8M (2,233.3 to 3,440.1, 10-K balance sheets): about 5.6% on the added equity, below the 7.5% to 9.0% average and
  below every authorized ROE. Over 2016 to 2025: +$124.1M on +$1,551.8M, 8.0%. The added equity came from new shares
  ($133.7M, $85.3M, $252.4M and $212.2M issued in 2022 to 2025, cash-flow statements) and retained earnings ($909M at
  2025 against $484M at 2020). This is the case the rows describe: "we’re not earning a higher rate of return on capital
  than we were when we started. We just put way more capital into the business" **[M2023-081]**.
- **The growth arithmetic and its caps.** Owner cash after maintenance grew 6.4% a year 2021 to 2025 (Step 0 table), and
  the spending that bought it was $445M a year above maintenance, of which about $160M a year was new long-term debt.
  Owner cash after all spending was negative in every year of the window (-$130.6M to -$270.2M). The business is the
  second grade of the 1998 passage at best, "It takes more money" **[M1998-081]**, and a second best by the rows' own
  name **[M2018-055]**.
- **WEIGHS AGAINST.** A capital-heavy second best whose incremental equity has lately earned about 5.6%, below the
  regulators' own allowed returns: "cash-consuming businesses, by their nature, are unattractive unless the cash they
  consume gets to earn a reasonable return" **[M2012-057]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eight years shown of the ten read** **[M2025-032]** (`tools/run.py` table, first-filed
  XBRL, checked against the FY2025, FY2023 and FY2020 filed balance sheets; USD millions; 2017 and 2019 read and omitted
  here for width, they lie on the same line):

| year-end | assets | equity | goodwill | receivables | LT debt (noncurrent) | commercial paper | retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 4,943 | 1,888 | 158 | 291 | 1,192 | 145 | 161 |
| 2018 | 5,469 | 2,043 | 158 | 295 | 1,285 | 300 | 321 |
| 2020 | 6,029 | 2,233 | 158 | 293 | 1,582 | 418 | 484 |
| 2021 | 8,402 | 2,350 | 158 | 342 | 3,683 | 494 | 565 |
| 2022 | 7,776 | 2,584 | 158 | 554 | 2,662 | 552 | 652 |
| 2023 | 7,771 | 2,766 | 158 | 348 | 2,160 | 89 | 738 |
| 2024 | 8,426 | 3,105 | 158 | 408 | 2,385 | 915 | 810 |
| 2025 | 8,853 | 3,440 | 158 | 462 | 2,356 | 737 | 909 |

  What moved and why. Equity grew 82% in nine years while goodwill did not move: the growth is retained earnings
  (+$748M) and new shares (paid-in capital $2,530M at 2025). Debt rose with it: noncurrent long-term debt doubled and
  commercial paper went from $145M to $737M (2025; $771M at 2026-06-30). 2021 is the Uri year: assets jumped $2.4B and
  long-term debt to $3,683M when the company paid about $2B of storm gas costs and deferred them as regulatory assets
  (cash flow 2021: regulatory assets current -$1,562.6M, noncurrent -$367.2M); 2022 and 2023 show the recovery
  (Oklahoma securitization proceeds $1,330.6M in operating cash 2022; Texas $197.4M in 2023; Kansas through KGSS-I's
  $335.9M bonds, a financing line, 2022) and the repayment of storm-year notes ($1,627.0M in 2022). Receivables track the
  gas price (2022's $554M). Deferred income taxes are $964M (2025), a liability the regulator takes into account, "I
  don’t think I would look at that as a hidden form of equity" **[M2015-030]**. What the figures cannot say: the allowed
  return in each future rate case.
- **The real costs.** Depreciation is charged in full and used as the maintenance guess, the rows' proxy where it is not
  shown inadequate **[M1998-127]**; the replacement spending above it is charged as growth spending at Q7, so no spending
  is left out **[L2015-004]**. Stock pay ($14.8M in 2025) is charged. No restructuring charges in the window. EBITDA: no
  instance found in the FY2025 10-K or the 2025 year-end earnings release (text search for "EBITDA", zero hits).
  Pensions: plans in a net asset position ($47.0M pension and OPEB asset, 2025 balance sheet); contributions $6.4M (2025).
- **The accounts.** No confusion: Uri, the three securitizations and the KGSS-I consolidation are each set out on their
  own lines of the cash-flow statement and the balance sheet. No suspicion from the statements: no build-up of prepaid or
  deferred accounts beyond the disclosed regulatory assets (current regulatory assets fell from $101.2M to $49.5M in
  2025); gas in storage moves with the gas price; auditor PricewaterhouseCoopers LLP; internal control over financial
  reporting "was effective as of December 31, 2025" (10-K Item 9A).
- **The habits, recorded here as a WEIGHING and carried to Q5.** (1) Earnings guidance every year, the habit the rows call a
  "scourge" **[L2019-006]**. The record: the 2024 range ($214M to $231M, $3.70 to $4.00, release 2024-02-21; actual
  $222.9M, $3.91); 2026 adjusted net income $306M to $314M, $4.83 to $4.95, raised on 2026-08-04 to the "upper half";
  and a long-term outlook of "7 to 9 percent" adjusted net income growth and "5 to 7 percent" per share (release
  2026-02-18). (2) From 2026-02-18 an "adjusted net income"
  is featured in the headline of each release ("Releases Non-GAAP Adjusted Financial Guidance"; "Raises 2026 Adjusted
  Earnings Expectations"), and the 10-K's MD&A carries it. The adjustment adds an equity carrying cost on plant in service
  not yet in rates, which regulators or Texas law allow but GAAP does not let the company book: $6.7M in 2025, $2.0M in
  2024, $1.8M in 2023, about $12M guided for 2026 (10-K Item 7 reconciliation; release 2026-08-04). It adds income rather
  than waving away costs, but it is still a figure featured beside GAAP, and the long-term growth rates are now stated on
  the adjusted 2025 base ($271M, not GAAP $264M) **[L2016-006]**. A management "preoccupied with accounting
  considerations" is "a negative" but not "a total exclusionary factor" **[M1994-018]**.
- **VERDICT on the accounts: IN (no confusion, no suspicion); WEIGHS AGAINST** on the guidance and the featured adjusted
  figure, carried to Q5 **[L2019-006]**, **[L2016-006]**. The recast owner cash of Step 0 feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. *How well they run the business, against the hand dealt:* the hand is a
  regulated franchise in three constructive states; the play is read in the record. Through Uri (February 2021) management
  borrowed about $2.5B in weeks ($2,498.9M of notes issued in 2021, cash-flow statement), obtained securitized recovery in
  all three states by 2023, repaid the storm notes ($1,627.0M in 2022), and kept investment-grade ratings (Moody's A3, S&P
  A-, stable, 10-K Item 7). Safety measures improved or held (DART 0.18, PVIR 1.60 in 2025; Item 1, "top quartile" by the
  company's own statement, not checked). Against: the earned ROE has fallen below every authorized return (Q2, Q3), and
  the 2025 Texas rate case asked 10.4% and $41.1M and settled at 9.8% and $15.0M. *How well they treat the owners:* read in
  the proxy at Q6, Part B.
- **The tells of dishonesty, searched for** (Q5's list). Too good to be true: no instance found in the releases or the
  10-K read. Reports that dance: the reports state the bad news plainly (regulatory lag, costs "not allowed recovery",
  Item 1). Fixation on the stock price: the proxy's "Financial Performance" and "Total Shareholder Return" paragraphs lead
  with the price and TSR since 2014, a mild sign; the PSUs pay on relative TSR (Q6). Serial issuance: carried to Q6.
  Taking credit: none found. Restatements, auditor change, material weakness: none in the filings read.
- **The habits carried from Q4, read with the integrity record** **[M2004-067]**. Guidance every year and a featured
  adjusted figure from February 2026 **[L2019-006]**, **[L2016-006]**. Read against the record: (1) the annual incentive
  pays on **GAAP** diluted EPS, not the adjusted figure (2025 target $4.26, actual $4.37, 70% weight, DEF 14A "EPS (GAAP)";
  "computed in accordance with accounting principles generally accepted in the United States"), so the adjusted figure is
  not the number the officers are paid to hit; (2) the adjustment is small ($6.7M of $264.2M in 2025), fully reconciled in
  every document that shows it, and rests on a carrying cost a state law and regulators grant; (3) results land inside the
  guided ranges rather than at or just above a single target each year (2024: $3.91 within $3.70 to $4.00, release
  2024-02-21 and 10-K), which is not the "consistently reach their declared targets" pattern of **[L2002-041]**. What weighs
  against: guidance is the habit the rows call corrosive **[M2022-054]**, and re-basing the long-term growth rate on an
  adjusted base is a promoter's choice. I looked for the doubt that closes the file **[M2013-088]** and did not find it in
  the documents: no figure misstated, no cost hidden, no pay tied to the adjusted figure.
- **Love of the business.** The CEO (Robert S. McAnnally, CEO since 2021, COO 2020 to 2021) and the COO (Curtis L.
  Dinan, promoted to president and COO from 2026-03-01, 8-K 0001193125-26-057048) are career operators of this company or
  its industry; no evidence either way on love against money beyond tenure. Succession: a named president below the CEO,
  and the chair moved to an independent director, Deborah A.P. Hersman, from 2026-05-21 (DEF 14A); the CEO is the only
  non-independent director.
- **VERDICT on integrity: IN** (no doubt found in the filings and the record read; the habits weigh against and are
  recorded) **[M2013-088]**, **[M1994-018]**. **Ability WEIGHS FOR, modestly:** Uri handled without a dilutive rescue and
  with ratings kept; the slipping earned return is the counterweight **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. Over 2021 to 2025 the company kept $434.2M of earnings
  (net income $1,146.4M less dividends paid $712.2M, cash-flow statements) and raised about $710M of new equity (issuance
  of common stock lines, 2021 to 2025). The proxy's pay-versus-performance table puts the cumulative TSR of $100 invested at
  2020-12-31 at $119.72 at 2025-12-31, against $158.65 for its own benchmarking peer group (DEF 14A). That is about 3.7% a
  year with dividends reinvested, roughly the dividend yield alone ($2.68 declared in 2025 on the proxy's year-end price of
  $77.25, 3.5%), so the market value per share barely moved while $434M was retained and $710M added. Read in market value,
  the retained dollar did not become a dollar **[R1995-009]**; read against intrinsic value, the incremental equity earned
  about 5.6% (Q3). Weighs against. The forward question, "Can you keep using all of the capital you generate,
  effectively, for a very long time?" **[M2010-097]**: the company can use more than it generates; the regulator
  guarantees a use, not a rich one.
- **Buybacks.** None in the window (no repurchase line in the cash-flow statements 2021 to 2025; tax withholdings on share
  settlements only). The test against the bottom of the Q7 range does not arise; written back here when Q7 was reached.
- **Issuance and deals.** No acquisitions and no stock deals in the window; the Q6 STOP on an all-stock deal in
  undervalued stock **[L2009-019]** does not arise. Issuance is continuous: forward sale agreements in 2023 and 2025, an
  at-the-market programme of $300M (2023) and another of $225M (2026-02), shares issued every year 2022 to 2025, all to
  fund the capital programme while holding the equity ratio the regulators allow (59% to 60%). The rows' warning on the
  company "hell-bent on issuing shares" **[L2014-015]** is a candidate second STOP the framework leaves unresolved (Q6,
  Part A; section VI). Read here as a weighing: the issuance is the regulated model's funding, priced at market and
  disclosed in advance, not a promotion; but each share sold at a price above the value Q7 computes is sold well for
  the existing owners and each sold below it is sold badly **[R1995-010]**, and the owner of a utility that must issue
  every year is a partner who must keep buying in. Weighs against, mildly.
- **Dividends.** $2.68 a share declared in 2025, 61% of GAAP EPS, raised every year; paid while new equity is raised in
  the same years, so part of each dividend is returned capital raised from new owners. A fixed-ratio habit the rows call
  "nuts" in its general form **[M2000-051]**. Weighs against.
- **Part B, the pay, the board and the owners.** The proxy **[M1994-009]**: the annual incentive is 70% GAAP diluted EPS
  and 30% operational and safety measures (emissions, DART, PVIR, emergency response), under the person's control in part
  **[M2003-019]**; the long-term award is performance stock units that pay 0% to 200% on three-year TSR relative to a peer
  group, a measure the officer does not control, the rows' "lottery ticket" **[L1996-018]**; pay is benchmarked to a peer
  group at the median with a compensation consultant, Meridian (DEF 14A), the ratchet **[L2005-015]**, **[M2004-016]**.
  CEO summary compensation $5.58M in 2025 (pay-versus-performance table). In favour: anti-hedging and anti-pledging
  policies, a clawback, share-ownership guidelines with a hold-until-met rule, an independent chair from 2026-05-21, and
  the 2022 PSUs paid 50% of target on a 25th-percentile TSR, so the downside was felt (DEF 14A).
- **Part A: WEIGHS AGAINST** (retention test failed in market value over five years; continuous issuance; dividend paid
  out of a company raising equity). **Part B: WEIGHS AGAINST, mildly** (relative-TSR PSUs and peer benchmarking; GAAP EPS
  in the annual plan and an independent chair weigh the other way).

## Q7 — WHAT IS IT WORTH? STOP.
- **The question.** How much cash, how sure, how soon **[M2009-004]**, at the long government rate **[L2000-021]**, held as
  a range **[L2000-024]**. Arithmetic: `Test Runs/_research 2026-10-27 OGS/scripts/q7.py`, output `q7_output.txt`.
- **The basis: the regulated utility** (Q7, The regulated utility). The deciding part, the whole company, earns a
  regulator-allowed return; the central figure is the **equity-only** basis, owner cash after interest and after the
  company's own tax against the market value of the shares, with the long-term debt raised for the fixed assets credited
  against the growth spending **[L2017-012]**, **[L2010-012]**; the all-equity figure beside, never deciding alone.
- **The cash input** (Step 0 table): owner cash after maintenance, the five-year average 2021 to 2025, **$229.3M**
  (maintenance guess = depreciation less the Kansas securitized amortization, the filing allowing the guess through its
  own split of spending into replacement and extension, and depreciation being the rows' proxy **[M1998-127]**, **[L2000-035]**).
  Tax at the book figure; stock pay charged.
- **Growth shown:** 6.36% a year on the aggregate owner cash after maintenance, 2021 ($206.4M) to 2025 ($264.2M); the
  halves of the window agree ($214.1M to $243.5M). Carried ten years, then zero nominal growth.
- **Growth spending (specific (e)):** spending above maintenance averaged $444.7M a year; in the growth case it grows at
  6.36%: **$473.0M in year one, $823.9M in year ten, none after.** The maintenance guess is charged in every year of every
  case.
- **Utility debt credit (2026-10-23 text):** the increase over the window in long-term debt other than the KGSS-I
  securitization bonds (left out with their dedicated charge), current maturities included, commercial paper and cash
  left out: $1,582.4M at 2020-12-31 (10-K FY2020, 0001587732-21-000030) to $2,382.7M at 2025-12-31 ($2,133.0M noncurrent
  plus $249.7M current, 10-K FY2025): **$160.1M a year**, against growth spending only. **Cap:** the allowed debt share of
  the deciding part, weighted by rate base: Oklahoma 41% debt on $2,453M and Texas 40% on $1,887M (10-K Item 1 table),
  stated for 75% of rate base (Kansas settled "without a determination" of the ratio, so it is left out of the weighting,
  said so): **40.57%**, $180.4M on the average growth spending, so the credit of $160.1M is not capped. In the growth case
  it grows with the growth spending: $170.3M in year one, $296.6M in year ten, none after. Beside: the $250M 13-month
  term loan due September 2026 is in "current maturities of other long-term debt"; without it the credit is $110.1M a
  year.
- **The six specifics.** (a) *Cycles:* not a cyclical business; the window's first year, 2021, is aberrational in working
  capital (Uri, on the filer's own description) but not in owner cash as recast here (net income $206.4M, in line), so the
  window stands; the literal window as filed, operating cash less capex, averages **-$252.0M** (-$2,030.9M, +$961.4M,
  +$272.9M, -$334.8M, -$128.4M), shown beside and not used because the storm's deferral and recovery dominate it.
  (b) *Decline:* none. (c) *Acquisitions:* none in the window, none signed. (d) *Working capital:* the window's changes in
  working capital, with the storm's deferral netted against its recoveries (Oklahoma and Texas proceeds in operating cash,
  Kansas bonds in financing), sum to -$252.7M, -$50.5M a year; the part due to the storm cannot be separated from the
  rest in the filings read (regulatory assets of $256.2M noncurrent remain at 2025), so the central case carries working
  capital at zero as a draw tied to one event under (d), and the range with -$50.5M a year charged is shown beside.
  (e) *Growth spending:* as above. (f) *The cap:* 6.36% exceeds the 5.31% sovereign but only inside the ten years, where
  the shown rate is the cap; nothing above the discount rate is carried after year ten **[M1997-095]**. Absurdity test:
  owner cash in year ten $424.8M, against revenue that grew 7.6% a year 2021 to 2025 (1,808.6 to 2,427.4) and a highest
  share of sales in the filings read of 12.8% (2020); carried at that sales growth it is 8.4% of year-ten sales: not absurd.
- **Value range (equity-only, central):** no-growth case **$4,318M, $68.70 a share**; growth case **$4,185M, $66.59 a
  share** (ten years of owner cash less growth spending plus the debt credit, -$55.4M in year zero terms, then $424.8M a
  year at zero growth). **Range $66.59 to $68.70 against $78.36.** The growth case sits below the no-growth case: at the
  sovereign the growth bought is worth slightly less than it costs, "growth can destroy value" **[L2000-023]**; the
  inversion is the finding, not an error. Width 1.03 to one.
- **Beside, never deciding:** working capital charged (-$50.5M a year): no-growth $53.56. Cash tax (deferred taxes added
  back, +$40.4M a year): no-growth $80.82. Credit without the term loan: growth case $58.18. All spending charged, no
  growth, with the credit: -$55.4M a year (no value); without the credit -$215.4M. **All-equity basis:** owner cash
  before interest after the company's tax (interest added back at 1 less the window's effective tax rate of 16.2%)
  averages $320.4M, growing 10.56% 2021 to 2025 (a rate inflated by the storm's financing interest, $60.3M in 2021 to
  $142.8M in 2025); net debt at 2026-06-30 $3,146.5M (other long-term debt $2,133.7M plus current $249.9M plus commercial
  paper $770.8M less cash $7.9M; KGSS-I bonds left out with their charge; 10-Q 0001587732-26-000035; the $375M notes of
  2026-08-13 refinance and leave net debt unchanged, said so). No-growth $45.93; growth $79.95 (at the window's equity
  rate instead, $35.08).
- **The floor, tested first** **[M2003-149]**. The expected return at $78.36 is 4.66% on the no-growth case and 4.81% on
  the growth case (central); 5.5% even with cash taxes; 3.97% on the all-equity no-growth case (owner cash before interest
  over market value plus net debt). **No case in the range, central or beside, earns about ten percent at the price**;
  the central cases do not earn the sovereign. The file closes OUT whatever the width (Q7, The floor is tested first). The
  price also sits above the top of the range, the same close by the floor convention.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and averaged:
  no-growth $36.48, growth $18.71, **fair price $27.59 a share, equity-only (central for a regulated utility)**, after the
  company's own tax. **All-equity beside: -$7.94 a share (not positive)**: no-growth $0.91, growth -$16.79 at ten percent
  (with the equity series' rate instead, -$14.62). No cheap price is reported.
- **Q6 written back:** no buybacks in the window; the test of prices paid against the bottom of the range ($66.59) does
  not arise.
- **VERDICT: OUT.** "there’s just a point at which we drop out of the game" **[M2003-149]**: at $78.36 the owner's
  expected return is below the long government bond, let alone the floor; no pencil makes it a screamer **[M2009-005]**.
  The rows expected this of a utility at a full price: "there’s no way we get rich on our utility investments"
  **[M2009-104]**.

**Q8, Q9, Q10 and Q12: NOT REACHED** (the Q7 STOP closed the file; operator rule 2).

---
## THE BOX
**OUT at Q7** (no case in the range earns the floor of about ten percent at the price; tested first): value range
**$66.59 to $68.70 a share** (equity-only, central for a regulated utility) against **$78.36** (close 2026-10-26,
aggregator, flagged). Fair price (reporting figure) $27.59 equity-only; all-equity -$7.94, not positive. Q1 IN, Q2 IN
(regulated return carried as a second best), Q3 weighs against, Q4 accounts IN with the habits weighing against, Q5
integrity IN, Q6 weighs against. No research pass: the box is OUT, not TOO HARD.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; operator rule 2.)* **[M1997-127]**
- **Q8 (the bond).** The 30-year Treasury par yield was 5.31% on 2026-10-26 (US Treasury); the central owner's return at
  $78.36 computed at Q7 is 4.66% to 4.81%.
- **Q9 (debt and exposures).** At 2026-06-30: other long-term debt $2,383.6M (of which $249.9M due within a year, the
  13-month term loan due September 2026), commercial paper $770.8M, KGSS-I securitization bonds $238.5M (non-recourse in
  form, repaid from a dedicated Kansas charge), against equity $3,537.9M (10-Q 0001587732-26-000035); $375M of 5.45% notes
  due 2036 sold 2026-08-11 (8-K 0001193125-26-349155). Pre-tax earnings over interest in 2025: ($321.5M + $142.8M) /
  $142.8M = 3.25 times, the rows' definition **[L2012-002]**. Credit agreement covenant: total debt to capital, excluding
  KGSS-I, no more than 70%; 47.6% at 2025-12-31 (10-K Item 7). Ratings A3 / A-, stable. The one sudden demand for a large
  sum in the window: Winter Storm Uri, about $2B of gas costs in February 2021, met with $2,498.9M of new notes in 2021;
  the shape the rows refuse for themselves is "sudden demands for large sums" **[L2014-024]**. Concentration: three
  adjoining states ("Our business activities are concentrated in three states", Item 1A); the rows' utility note, "A
  catastrophic event can render a single utility insolvent" **[L2005-019]**. Commercial paper of $771M rolls within 270
  days.
- **Q10.** Nothing found.
- **Q12.** Not one of the named businesses. Nothing found for the newspaper test in the documents read beyond the
  ordinary pipeline-safety and environmental disclosures (12 former manufactured-gas sites in Kansas under a consent
  agreement, remediation reserve $13.7M, 10-K Item 7).
- **Integrity facts:** none beyond those judged at Q5, which was reached and answered; no flag in the box line.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 8157df1c); written question by question; committed after each
      question (8c985586 Q1, fd621895 Q2, 2acd6526 Q3 and Q4 together, d488b7d9 Q5, 82f0423e Q6, 9308c559 Q7). Q3 and Q4
      went in one commit because a shell quoting failure blocked the first attempt; both were written before the commit.
- [x] Dispatched: the brief allowed per-question pathspec commits; the dispatching session holds the lock; the fold is
      the dispatcher's. A run not in the register binds nothing.
- [ ] **Blind rule: one breach declared.** Before the template copy I listed `Test Runs/` filtered by this company's
      name (a collision check); it showed the file names of a run of 2026-10-18 and its research folder. Not opened, not
      used; declared under Contamination at the top. No `PORTFOLIO.md`, holding review, register, reading list or
      resume-state file was opened, listed or searched.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check
      script `Test Runs/_research 2026-10-27 OGS/scripts/check_ids.py`: 0 E-ids, 71 distinct ids, 0 missing, 28 quoted fragments
      checked, 0 problems, after two fixes: a filing quote and a framework quote had stood beside an id and were moved); every filing fact carries its document and accession; no E-ids.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; Q8 to Q12 not reached; nothing after Q7 is a
      clearance.
- [x] Owner cash after every real cost from the filed statements, never a net-income proxy: net income is the starting
      line of the filer's own cash-flow statement, with depreciation added and every dollar of capex and asset removal
      deducted (maintenance and growth shown separately); `tools/run.py`'s owner-earnings lines were rejected (wrong D&A
      element, window ending 2023, securitization proceeds inside operating cash). Sovereign from the US Treasury.
      Price from an aggregator, flagged.
- [x] Contrary evidence written down as found (Foundations, five items); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` used (price, shares, sovereign, the ten-year balance-sheet table, each
      checked).
- [x] `python tools/check_framework.py` run before the final commit: PASS.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The utility's maintenance guess.** Specific (e) asks for the maintenance guess "where the filing allows" it, and
the rows define maintenance as what "a company must make to maintain its competitive position" **[L1999-024]**. This
filing splits its spending into "system integrity and replacement" (about three quarters) and "extensions to new
customers" (about $230M of $800M). Replacement of old pipe is maintenance in the rows' sense, yet under original-cost
rate-making it grows rate base and earnings like any growth spending. Taken as maintenance, owner cash after maintenance
is near zero and the growth in earnings it buys would be credited free, the mismatch specific (e) forbids in its last
sentences. I took depreciation as the maintenance guess, the rows' proxy **[M1998-127]**, and
charged all replacement spending as growth spending against the growth it bought; the Q7 text does not say which reading
a regulated utility takes, and the two readings differ by the whole value. (2) **Securitized cost-recovery inside D&A.**
The 2026-10-23 text leaves securitization bonds out "with the charge" but does not say that the securitized intangible's
amortization, which sits inside the filer's D&A and repays those bonds, must leave the maintenance guess too; I removed
it, and said so. (3) **A storm deferral that spans the window.** Specific (d) treats "a single year's draw that the filer
ties to one contract or event" as aberrational; Uri's deferral (2021) and its recoveries (2022, 2023, part in financing
through Kansas bonds) span three years and leave a residual that the filings do not split from ordinary working capital.
I carried working capital at zero centrally and showed the -$50.5M a year residual beside. (4) **The cap's weighting.**
The text weights the allowed debt share by rate base, and switches to the company's own share where an allowed share is
stated for less than half of rate base; it does not say whether, when shares are stated for more than half, the
unstated jurisdiction is dropped from the weighting or given the company's own share. I dropped it (Kansas, 25% of rate
base); the cap did not bind either way. (5) **A 13-month term loan** is booked in "current maturities of other long-term
debt"; the credit counts long-term debt with its current maturities, so it is in, but it is closer to short-term
borrowing; shown both ways. (6) **Book or cash tax for a utility.** "Whose tax" says the company's own tax; it does not
say book or cash where deferred taxes are large and reduce rate base. I used book, reading **[M2015-030]**, and showed
the cash-tax case beside; it is the one case that rises above the price at the sovereign, and still earns 5.5%, not ten.
