# Company Run — Otis Worldwide Corporation (NYSE: OTIS) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run under `Screens/_daily/_dispatch_brief.md`. The business: elevators and escalators, New Equipment
and the maintenance, repair and modernization Service portfolio; spun off from United Technologies (UTC, now RTX) on
2020-04-03. Template copied to this file before any fetch; research folder `Test Runs/_research 2026-10-10 OTIS/`
(raw filings in its ignored `cache/`, the fetch and ledger helpers and the notes file tracked).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold (overnight cycle, 2026-10-10), after the run was committed: **not held**; `PORTFOLIO.md` carries OTIS only as a row of the ranked opportunity set from the v4.1 run of 2026-09-01, in no account.*

**CONTAMINATION, declared:** (1) The repository's `git log` shown at session start carried the subjects of the five most
recent commits, which name four other companies' runs and their boxes and alert prices (batch 8). Not used. (2) The
memory index loaded into this session's context names the queue state, a count of gate-clearers and that holding
reviews are owed; it names no company. Not used. (3) No `Test Runs/` listing was made; no other run, research-pass or
holding file, `PORTFOLIO.md`, `Screens/RESUME STATE*`, the register or the reading list was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $65.95 (close 2026-10-09; the quote `tools/run.py` printed; aggregator, live quote only, flagged per
  operator rule 5). For orientation only, the filed buyback prices: $78.4 a share average in 2026 Q2 ($400M for
  5.1M shares, 10-Q, accession 0001781335-26-000113).
- **Shares by class** from the latest filing's cover: one class, 380,669,339 shares as of 2026-07-15 (10-Q for the
  quarter to 2026-06-30, filed 2026-07-23, accession 0001781335-26-000113; `python Screens/cover_shares.py OTIS`).
  Check: issued 439.9M less treasury 59.2M at 2026-06-30 = 380.7M, agrees. No 8-K or prospectus after the 10-Q changes
  the count (the 8-K of 2026-09-15 is an officer transition, accession 0001140361-26-036566).
- **Market cap:** $25,105M (380.669M x $65.95).
- **Sovereign for the earnings currency:** USD (the cash-flow series is in USD), 30-year par yield **5.60%**, US
  Treasury daily par yield curve, 2026-10-09 (issuing authority, via `tools/sources.py` as `tools/run.py` printed it).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-05, accession 0001781335-26-000011); 10-Ks FY2024
  (0001781335-25-000010), FY2023 (0001781335-24-000013), FY2022 (0001781335-23-000009), FY2021
  (0001781335-22-000007), FY2020 (0001781335-21-000023); 10-Q to 2026-06-30 (0001781335-26-000113); proxy DEF 14A
  filed 2026-04-17 (0001140361-26-015389); 8-K earnings releases of 2026-01-28 (0001781335-26-000004, ex. 99) and
  2026-07-22 (0001781335-26-000110, ex. 99); 8-K of 2026-09-15 with ex. 10.1 and 99.1 (0001140361-26-036566); the
  Form 10 information statement, ex. 99.1 to the 10-12B/A of 2020-03-11 (0001140361-20-005505); United Technologies'
  annual-report segment tables (ex. 13 to the 10-Ks for FY2004 0001193125-05-025271, FY2007 0001193125-08-022346,
  FY2010 0001193125-11-029695, FY2013 0000101829-14-000006, FY2016 0000101829-17-000007, and the FY2019 10-K
  0000101829-20-000013). **One figure cross-checked against the filed statement:** operating cash flow FY2025, $1,596M
  on the filed Consolidated Statement of Cash Flows of the FY2025 10-K equals the XBRL value `tools/run.py` printed;
  FY2024 $1,563M and FY2023 $1,627M likewise.
- `python tools/run.py OTIS` arithmetic lines only (its v4 text, ids and floor ignored, Part VII): OCF 1,627 / 1,563 /
  1,596 (2023 to 2025), SBC 64 / 73 / 80, capex 138 / 126 / 152, D&A 193 / 182 / 175, dividends to minority partners
  85 / 94 / 69 (the alternate it prints; chosen here, see Q4); five-year OE on capex basis 1,412 before the minority
  dividends. Owner cash is recast at Q4 from the filed statements.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the maintenance portfolio and the new-equipment arm will earn, never when
the quote moves **[M1997-109]**. No macro enters: the Chinese property cycle that has cut New Equipment is read only as
a fact about this business's past cash, not forecast, "macro conclusions are — just never enter into the discussion"
**[M2000-094]**. The margin of safety is an attitude here and arithmetic at Q7 **[M1996-084]**. Who is paid to tell
you: the company issues annual guidance and features adjusted figures; both are read as the seller's projection
**[M2011-083]**. **Contrary evidence, written down as found** **[M1997-127]**: (i) segment operating profit of New
Equipment fell from $459M (2021) to $240M (2025) and China external sales from $2,877M to $1,650M; (ii) the
independent service providers hold "about 50% of service units" (FY2025 10-K, Item 1, Competition); (iii) from 2024
restructuring was taken out of segment profit, so segment margins after 2023 flatter the earlier ones (FY2024 10-K,
Note 22); (iv) Otis's own segment margin under UTC fell from 22.6% (2011) to 14.9% (2019); (v) unlevered owner cash
was no higher in 2025 than in 2021 (Q4); (vi) a European Commission competition fine of about $300M was levied on Otis
and UTC in 2007 for EU competition-rule violations by Otis subsidiaries, and cartel overcharge claims are still being
made in certain European countries (UTC FY2007 ex. 13; FY2025 10-K Note 20); (vii) the chair and chief executive
retires by 2027-07-31 (8-K 2026-09-15); (viii) the 2026 outlook was cut in July (adjusted free cash flow $1.6 to $1.7
billion in January, $1.50 to $1.55 billion in July).

## THE STANDING RULE
A part-interest bought for cash, unlevered, sized so that a fall of half or more is borne without a forced sale, puts
the buyer at no risk of ruin **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**.
The target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**. The product is old and its economics are visible in the filings: Otis
  installs elevators and escalators (New Equipment, 35% of 2025 sales), then maintains, repairs and modernizes a
  portfolio of about 2.5 million units (Service, 65% of sales, 91% of 2025 segment operating profit; FY2025 10-K,
  Item 1, accession 0001781335-26-000011). The petroleum-additives row is the model: the chemistry need not be known if
  "I understand the economic dynamics of the industry" **[M2011-014]**.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) units in the maintenance portfolio:
  "over 2 million" (FY2020 10-K), 2.1M (FY2021), 2.2M (FY2022), 2.3M (FY2023), 2.4M (FY2024), 2.5M (FY2025); the proxy
  says the portfolio "expanded 4% for the fourth consecutive year" (DEF 14A 2026, 0001140361-26-015389); (2) price per
  unit and the cost of the mechanic, read in the Service margin, 20.7% (2018) to 25.1% (2025, on the measure that
  excludes restructuring); (3) New Equipment volume, which is a construction-cycle number, half or more of it by units in
  China (FY2025 10-K, Item 1A). Variables (1) and (2) are slow-moving, contractual and code-driven: "A basic
  maintenance contract provides for inspection consistent with local regulatory needs" (Item 1). Variable (3) is not
  foreseeable over ten years, and the company's own filings say so year after year.
- **Do the past statements tell me the future ones** **[M2008-033]**: for Service, yes: eight years of standalone
  segment figures (2017 to 2025, Form 10 and the 10-Ks) and the UTC segment record back to 2002 show a business whose
  margin moved within a band through 2008-2009 and 2020. For New Equipment, no.
- **Would the insiders write it down** **[M2000-105]**: a maintenance portfolio's ten-year economics are what the
  company itself sets its incentive pay on ("Net Portfolio Unit Growth", DEF 14A 2026), and it is not a field of rapid
  change: the forecast is of building owners' behaviour under safety codes, "a different sort of analysis" from a
  technology forecast **[M2017-019]**. The China new-equipment market is the one the insiders decline to forecast.
- **Routing.** Not a fast-changing industry; not a bank. By the parts reading (Q1's holding-company paragraph, extended
  to operating segments by section B of the gaps case), the part that "matters" is the one that decides at Q2: Service,
  with 85% of five-year segment operating profit (Q2, the parts table). The part that decides can be understood; the
  part that cannot be foreseen (New Equipment volume) does not decide. Doubt test **[M2002-092]**: I have no doubt that
  a maintenance route of elevators is inside the perimeter; I do doubt any ten-year forecast of Chinese new-elevator
  volume, and the file does not rest on one.
- **VERDICT: IN.** Service, the deciding part, is understood on the filings' evidence **[M2012-065]**, **[M2011-014]**;
  New Equipment is carried to Q2 and Q7 as the part whose volume is not foreseeable.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (segment operating profit as filed; 2021 on the measure before 2024, which charged restructuring to
the segments; 2022 to 2025 on the 2024 measure, which does not, FY2024 10-K Note 22, accession 0001781335-25-000010;
2022 and 2023 as restated there):

| part | segment OP 2021 / 2022 / 2023 / 2024 / 2025 ($M) | five-year sum | share | castle | decides |
|---|---|---|---|---|---|
| Service (maintenance and repair, modernization) | 1,762 / 1,832 / 2,014 / 2,185 / 2,374 | 10,167 | 85% | standing (below) | yes, more than half |
| New Equipment | 459 / 381 / 381 / 329 / 240 | 1,790 | 15% | open on price (below) | no |

The file closes on Service (section B of the gaps case; "lumping them together [...] impedes analysis" **[L2008-005]**).
New Equipment does not decide and is carried to Q7 as an ordinary business at no growth.

**The castle tests, Service.**
- **Why the customer comes, and how permanent** **[M1995-038]**. The product is a legally required inspection and
  maintenance of a machine that carries people: "A basic maintenance contract provides for inspection consistent with
  local regulatory needs" (FY2025 10-K, Item 1). The customer is a building owner who cannot stop maintaining. The
  route is local: 37,000 service mechanics out of more than 1,400 branches "typically located in close proximity to
  concentrations of customers" (Item 1). The reasons read the same in the Form 10 of 2020 and the 10-K of 2026.
- **The attacker with money** **[M2011-015]**. A rich attacker can hire mechanics; what it cannot buy quickly is a dense
  route of 2.5 million units across 200 countries, the parts and codes of the installed Otis base, and the stream of
  newly installed units that convert to maintenance ("we seek to grow our maintenance portfolio, in part, through the
  conversion of new elevator and escalator installations into service contracts", Item 7). Against that: the
  independent service providers "have an aggregate portfolio of about 50% of service units, but account for a smaller
  percentage of the service business when measured by value because of the types of units and level of maintenance
  covered by these providers" (Item 1, Competition). The low end of the market is contestable and contested; the
  castle is the high-value, complex unit. "one competitor is frequently enough to ruin a business" **[M2012-108]**: no
  single independent is named as that competitor in any filing read.
- **Pricing power, and the price behaviour through the last inflation** **[M2005-020]**. Service operating profit rose in
  each year of the inflation with the filer naming price each time: 2021 "Favorable pricing and mix"; 2022 "favorable
  pricing on maintenance contracts [...] partially offset by [...] annual wage increases and other inflationary
  pressures"; 2023 "improved pricing on maintenance contracts and productivity, which were partially offset by annual
  wage increases and other inflationary pressures"; 2024 "improved pricing on maintenance contracts"; 2025 "improved
  pricing" (MD&A of the FY2021 to FY2025 10-Ks). Service margin 21.8% (2020), 22.4% (2021), 22.9% (2022, old measure),
  24.0% (2023), 24.6% (2024), 25.1% (2025). The row: "the businesses with strong competitive positions manage to pass
  through increases in raw material costs, just as they passed through increases in labor costs" **[M2005-017]**. The
  one year of concessions was 2020, "price concessions, lower volume and higher bad debt expense" (FY2021 10-K, 2020
  compared with 2019), and the Service margin still rose 30 basis points.
- **Unit volume** **[M1999-054]**. Portfolio over 2.0M units (FY2020 10-K) to about 2.5M (FY2025 10-K); the proxy:
  "Grew Service portfolio by 4%, marking our fourth year at 4% or greater", 2024 at 4.2% (DEF 14A 2026). The
  portfolio grew while the New Equipment that feeds it shrank, through conversions, recaptures and acquisitions.
  Retention or cancellation rates: not found in any filing read; the proxy defines net unit growth as "units acquired,
  units converted, units recovered and units cancelled" without giving the parts.
- **The low-cost position** **[M2004-091]**. Route density is the cost advantage of the largest portfolio: the cost of a
  call falls with the number of units a mechanic covers in a district. The filings assert scale ("the largest service
  provider in the industry worldwide") but give no cost per unit, so the low-cost claim is my reading, not a filed fact.
- **Would the customer still choose it over the low bid** **[M2017-009]**. Half the units by count have gone to the low
  bid (the independents); the higher-value half has not, and the share by value held by the large makers is not filed.
  The parachute row fits the product, people "care enormously about service and the assurance of safety"
  **[M2001-014]**, but the low-end evidence cuts against a universal claim.
- **Ask the competitors** **[M1999-130]**. No interview was possible; the rivals' own filings are not on EDGAR (the
  competitor row below).
- **Widening or narrowing** **[M1999-108]**. Under UTC, Otis's whole-segment margin was 15.5% (2002), 19.5% (2007),
  22.2% (2010), 22.6% (2011), 20.3% (2014), 16.2% (2017), 14.9% (2019) (UTC ex. 13 segment tables, accessions in Step
  0). The fall from 2011 to 2019 came while New Equipment's margin fell (the Form 10 gives New Equipment 8.8% in 2017
  and 7.0% in 2018 and 2019; Service 21.8%, 20.7%, 21.5%); since the spin the Service margin has risen every year. The
  Service moat reads as widening on the filed margins; the New Equipment moat as narrowing.
- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: (1) a code or law change that
  lets independents service complex units with open parts and diagnostics; (2) a fall in conversions as Chinese new
  units, over half of Otis's New Equipment units, shrink by more than 20% a year (FY2024 and FY2025 10-Ks); (3)
  connected units (1.1 million, Item 1) cut both ways, a route-cost advantage for the maker or a remote-diagnosis tool
  that lowers the independents' cost; (4) the cartel record: the 2007 European fine of about $300M for "certain Otis
  subsidiaries in Europe violating European Union competition rules" (UTC FY2007 ex. 13, 0001193125-08-022346), with
  overcharge claims "on elevators and escalators related to civil cartel cases" still being made (FY2025 10-K, Note
  20). Part of the industry's past pricing in Europe was collusion, and the castle cannot count on that.

**The competitor row.** The elevator rivals Otis names (KONE Oyj, Schindler Group, TK Elevator; FY2025 10-K, Item 1)
and Mitsubishi Electric are not SEC filers: no 10-K or 20-F found on EDGAR (the SEC company list searched 2026-10-10;
Schindler has only ADR registration forms, F-6, CIK 1655190). Hitachi filed 20-Fs to FY2010 (accession
0001193125-11-172867); its elevators sit inside "Social Infrastructure & Industrial Systems" with rail and industrial
plant (segment profit ¥39.9bn on revenue ¥1,156.9bn in the year to 2011-03-31, 3.4%), not comparable and not used for
a margin. For the service model, from their own filings:

| filer | metric | 2018-19 | 2021-22 | 2024-25 | accession |
|---|---|---|---|---|---|
| Otis | Service segment margin | 20.7% (2018), 21.5% (2019) | 22.4% (2021), 22.9% (2022, old measure) | 24.6% (2024), 25.1% (2025) | Form 10; FY2021, FY2022, FY2025 10-K |
| Johnson Controls | Building Solutions North America segment EBITA margin (install and service, not split) | 12.8% (FY2019) | 13.9% (FY2021), 12.0% (FY2022) | Americas segment 18.2% (FY2025; products included after a resegmentation) | 0000833444-19-000051; 0000833444-22-000043; 0000833444-25-000097 |
| Johnson Controls | services share of net sales | 26% (FY2019) | 24% (FY2022) | 32% (FY2025) | same |
| Carrier | Climate Solutions Americas segment margin (equipment and aftermarket, not split) | not on this basis | not on this basis | 22.1% (2024), 20.5% (2025) | 0001783180-26-000008 |

Neither JCI nor Carrier files a service-only margin, so the row sets Otis's service margin against the blended
install-and-service margins of building-system makers: Otis's Service is at or above them over the span. It is not a
like-for-like test of the castle; the like-for-like rivals do not file, and their absence is a gap in this run.

**The field's returns over the last full cycle** (section C). Only the filer's own record is on EDGAR. Under UTC, Otis
segment operating profit on Otis segment identifiable assets (goodwill included): 25.3% (2004), 30.1% (2007), 32.0%
(2008), 30.9% (2009), 31.8% (2010), 27.7% (2013), 24.2% (2016), 19.5% (2019) (operating profit 1,504 / 2,321 / 2,477 /
2,447 / 2,575 / 2,590 / 2,147 / 1,948 against assets 5,939 / 7,721 / 7,731 / 7,908 / 8,097 / 9,354 / 8,867 / 9,973, $M,
UTC ex. 13). Through the 2008-2009 recession the return held near 30% while sales fell 9% in 2009. Standalone, the
tangible capital is smaller still, since customers' advances and payables finance the working capital (Q3). These are
excellent returns over a full cycle, not ordinary ones; the moat "protects excellent returns on invested capital"
**[L2007-004]**. The other members' returns are unknown from filings, and the run says so.

**New Equipment.** Open on price on its own filings: "unfavorable price and mix" (2021), commodity costs of $107M not
recovered (2022), "unfavorable price and tariff headwinds" (2025); margin 8.8% (2017) to 4.8% (2025); China sales down
more than 20% in each of 2024 and 2025. A part that does not decide and is open goes to Q7 at no growth.

- **VERDICT: IN.** The deciding part's castle stands on the evidence: price passed through every year of the inflation
  **[M2005-017]**, units grew 4% or more a year for four years **[M1999-054]**, and the returns on the segment's assets
  held through the last full cycle **[L2007-004]**. Its weak flank, the independents' half of the units, is recorded
  against it and carried to Q7's certainty.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Capital actually needed** **[M2010-090]**, **[M2011-060]**. At 2025-12-31 (FY2025 10-K balance sheet): fixed assets
  $743M, inventories $613M, receivables $3,688M, contract assets $699M and other current assets $405M, against accounts
  payable $2,142M, accrued liabilities $1,847M and contract liabilities $2,611M: tangible operating capital of about
  $548M (computed) against total segment operating profit of $2,614M. Even on all operating assets including goodwill
  the UTC-era return was 19% to 32% (Q2). "the best businesses, by definition, are going to be businesses that earn
  very high returns on capital employed over time" **[M1995-047]**.
- **To stand still and to grow** **[L1999-024]**. Capital spending 1.0% to 1.4% of sales (156 / 115 / 138 / 126 / 152,
  2021 to 2025) against depreciation of 116 / 118 / 126 / 120 / 113 and amortization of acquired intangibles of 87 /
  73 / 67 / 62 / 62. Spending runs a little above depreciation, the excess in software and digital (FY2020 10-K:
  "investments in software for internal use to support our digital and strategic initiatives"). Maintenance guess
  **[M2000-144]**: about the depreciation charge, $115M to $125M a year; the rest, $10M to $40M, is growth spending.
  The cash ends the year as cash, not "profit sitting in the yard" **[M2008-036]**: operating cash flow has exceeded
  net income attributable to Otis in four of the five years 2021 to 2025 (1,750 vs 1,246; 1,560 vs 1,253; 1,627 vs
  1,406; 1,596 vs 1,384), and in 2024 fell short (1,563 vs 1,645) only by the non-cash German tax gain.
- **The growth arithmetic** **[M2001-019]**. Service grows with the portfolio (about 4% a year in units) and with price,
  needing little capital; it is the best business of the 1998 grading, one "that gives you more and more money every
  year without putting up anything to get it, or very little" **[M1998-081]**. The added capital the company has put in
  since the spin went mostly to buying out its own minority partners: Zardoya Otis (Spain) for $1,802M in 2022,
  financed by euro debt; the Japanese subsidiary for about $70M (2024); Otis Electric (China) for about $215M (2025)
  (FY2022, FY2024, FY2025 10-Ks, Note 1). What that capital earns is bounded by the filings: the minority partners'
  share of earnings fell from $174M (2021) to $92M (2023) after the Zardoya purchase, a fall of $82M that also contains
  the Chinese joint ventures' decline, so the Zardoya half earned at most about 4.6% after tax on its price. Bolt-on
  acquisitions of service portfolios: $36M to $109M a year.
- **Return on equity means nothing here** **[M1998-017]**: shareholders' equity is negative ($-5,392M at 2025-12-31),
  made so by the spin's debt and the buybacks, not by losses.
- **WEIGHS FOR.** The deciding business needs almost no capital and its customers fund its working capital
  **[M1998-081]**, **[M1995-047]**; against it, the large post-spin outlays bought minority interests at returns well
  under the floor, which is weighed again at Q6.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first** **[M2025-032]** ($M, year-end; 2017 and 2018 from the Form 10 carve-out statements as
`tools/run.py` transcribed them; 2019 to 2025 from the 10-Ks, checked against the filed balance sheets of the FY2025 and
FY2022 10-Ks; mid-2026 from the 10-Q):

| year | cash | receivables | receivables / sales | inventory | goodwill | total debt | shareholders' equity | accumulated deficit |
|---|---|---|---|---|---|---|---|---|
| 2017 | 1,571 | n/a | n/a | n/a | n/a | n/a | 2,532 (net parent investment with minority) | n/a |
| 2018 | 1,329 | n/a | n/a | n/a | 1,688 | n/a | 2,106 (same) | n/a |
| 2019 | 1,446 | 2,861 | 21.8% | 571 | 1,647 | about 5 | 1,700 | 0 |
| 2020 | 1,782 | 3,148 | 24.7% | 659 | 1,773 | 5,262 long-term, short-term untagged | -3,832 | -3,076 |
| 2021 | 1,565 | 3,232 | 22.6% | 622 | 1,667 | 7,273 | -3,625 | -2,256 |
| 2022 | 1,189 | 3,357 | 24.5% | 617 | 1,567 | 6,768 | -4,870 | -2,865 |
| 2023 | 1,274 | 3,538 | 24.9% | 612 | 1,588 | 6,898 | -4,924 | -2,005 |
| 2024 | 2,300 | 3,428 | 24.0% | 557 | 1,548 | 8,324 | -4,848 | -978 |
| 2025 | 1,096 | 3,688 | 25.6% | 613 | 1,695 | 7,956 | -5,392 | -440 |
| 2026-06-30 | 813 | 3,985 | half year | 686 | 1,794 | 8,436 | -5,748 | -117 |

What they say: (1) the spin put about $6.3bn of debt on the company ($5.3bn of notes and a $1.0bn term loan, since
repaid) and sent cash to the parent ("a $5.4 billion increase in net transfers to UTC related to the Separation",
FY2020 10-K); equity has been negative since, made more negative by $4.2bn of buybacks, while the accumulated deficit
has shrunk from $-3,076M to $-440M as earnings were kept; (2) goodwill and intangibles are small and steady ($1.5bn to
$1.8bn of goodwill), so the earnings were not bought; (3) inventory is flat while sales rose 10%; (4) **receivables have
grown faster than sales**, 21.8% of sales in 2019 to 25.6% in 2025 and $3,985M at mid-2026, with an allowance of $129M;
the filer gives "timing of billings and collections" and lists "Customer liquidity constraints and related credit
reserve" among its macro risks (FY2025 10-K, Item 7). A fact to watch, not the build-up in prepaid or deferred accounts
that the tell names **[M1995-064]**; (5) debt has risen from $5.3bn to $8.4bn while cash has fallen. The figures do not
say what the Chinese receivables will collect, which is among "what they don’t say and what they can’t say"
**[M2025-032]**.

**The real costs.**
- Depreciation $113M and amortization $62M (2025): capital spending of $152M exceeds depreciation; charged in full.
- Stock pay $80M (2025), up from $65M (2021): deducted. "Stock-based compensation" is "the most egregious example"
  **[L2015-003]** of costs owners are told to ignore; Otis's adjusted figures do not exclude it (ER 2025 Q4
  reconciliation, accession 0001781335-26-000004).
- Restructuring every year since the spin: $54M (2019), $77M, $56M, $60M, $67M, $71M, $130M (2025), plus UpLift
  transformation costs of $16M, $65M, $69M (2023 to 2025) booked in other expense, Separation-related adjustments of
  $177M (2024) and $70M (2025), litigation settlements of $18M and $21M. The adjusted figures exclude all of them (ER
  2026 Q2). Restructuring that recurs every year is a cost of the business; telling owners to ignore it year after year
  "when management is simply making business adjustments that are necessary, is misleading" **[L2016-007]**. These charges are cash inside operating cash flow, so owner
  cash counts them.
- **The 2024 change of the segment measure** moved restructuring out of segment operating profit and restated two prior
  years (FY2024 10-K, Note 22); segment margins after 2023 are higher than the earlier ones by the restructuring, about
  half a point of sales. Disclosed, recast and immaterial to the trend; recorded.
- EBITDA: not used by the company in any filing read (searched the 10-Ks, the two releases and the proxy).
- Dividends to minority partners ($155M, $118M, $85M, $94M, $69M, 2021 to 2025) are cash that consolidated operating
  cash flow contains and Otis's owners do not get: deducted.
- One-off cash to and from the former parent sits inside operating cash: German tax refunds of $216M (2025) and
  Separation-related payments to RTX of $258M (2025) and $49M (2024) (ER 2025 Q4, adjusted free cash flow
  reconciliation). Net, a small outflow; left in.

**Owner cash, recast** (operating cash flow less capital spending, stock pay and dividends to minority partners, $M;
after the company's own tax):

| | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| operating cash flow | 1,750 | 1,560 | 1,627 | 1,563 | 1,596 | |
| capital spending | -156 | -115 | -138 | -126 | -152 | |
| stock pay | -65 | -67 | -64 | -73 | -80 | |
| dividends to minority partners | -155 | -118 | -85 | -94 | -69 | |
| **owner cash after interest (equity-only basis)** | **1,374** | **1,260** | **1,340** | **1,270** | **1,295** | **1,308** |
| net interest expense after tax (x 0.75) | 102 | 107 | 113 | 127 | 147 | |
| **owner cash before interest (all-equity basis)** | **1,476** | **1,367** | **1,453** | **1,397** | **1,442** | **1,427** |

Net interest expense 136 / 143 / 150 / 169 / 196 (2024 shown without the $200M German interest income, a one-off; MD&A
of the FY2022 and FY2025 10-Ks), taken after tax at 25%: **CONVENTION of this run**, the company's own effective rates
of 2023 and 2025 (26.2% and 24.8%) rounded; rationale: the all-equity basis needs interest after the company's tax,
and the 2024 rate of 15.0% is a one-off. Bolt-on acquisitions net of businesses sold average $59M a year (80 + 46 +
36 + 87 + 109, less 61 received for the Russian business in 2022) and are deducted at Q7.

**The habits carried to Q5.** Annual guidance on organic sales, adjusted operating profit, adjusted EPS and adjusted free
cash flow ("Otis is revising our full year outlook", ER 2026 Q2); adjusted figures featured beside GAAP in every
release, GAAP first in the key-figures table **[L2016-006]**, **[L2019-006]**. Against the habit: the July 2026 release
cut the outlook and reported the fall in adjusted operating profit in its first bullets ("adjusted operating profit
down $25 million").

- **VERDICT on the accounts: WEIGHS AGAINST, no STOP.** Nothing confuses and nothing in the statements raises suspicion
  by the tells that live in the accounts **[M1995-064]**; the recurring restructuring left out of the featured figures
  weighs against **[L2016-007]**, **[M1994-018]**, and is counted here as cash. The recast owner cash feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. How well they run it, against the hand dealt: the hand at the spin was a
  business with a strong service portfolio, a New Equipment arm half dependent by units on China, and $6.3bn of debt
  put on it by the parent. Since 2020 the Service margin has risen every year (21.8% to 25.1%), the portfolio has grown
  4% a year for four years, and an operating-model programme (UpLift, about $300M of cost for about $200M of run-rate
  savings, FY2025 10-K Item 7) was carried through. New Equipment fell with China. How they treat the owners: Q6.
- **The proxy** **[M1994-009]** (DEF 14A 2026, 0001140361-26-015389). Chief executive's total pay $16,977,877 for 2025,
  286 times the median employee. The 2025 bonus formula paid 72% of target because the company missed: adjusted net
  income $1,577M against a $1,648M target, adjusted free cash flow $1,583M against $1,600M, net portfolio unit gain
  87,000 against a threshold of 88,000, which paid nothing. Pay fell when results fell. Directors and officers are
  barred from hedging and pledging Otis stock. The compensation section runs from page 57 to page 91 of a 112-page
  proxy; the row's warning is "If you take 100 pages to explain how you’re paying the people of the place, something
  is wrong." **[M2009-087]**: here it is about 35 pages; recorded at Q6.
- **The make-the-numbers habit, carried from Q4** **[L2002-041]**. Otis gives annual guidance and features adjusted
  figures. It does not consistently reach its declared targets: the 2025 bonus targets were missed and the miss was
  printed in the proxy's own table; the 2026 outlook was cut in July with the fall in adjusted operating profit in the
  release's first lines. The row is "downright incredulous if they consistently reach their declared targets"
  **[L2002-041]**; this record is the opposite of that pattern. The guidance itself is a weighing against (Q6, Part B).
- **The tells** **[M2004-067]**, **[M2007-082]**. The figure that matters in this industry is the service portfolio and
  what it earns; Otis reports units, Service margin and price each year. One figure does not reconcile on the numbers
  given: the proxy says the portfolio "expanded 4%" in 2025, while its own bonus table shows a net gain of 87,000
  units, which on the 10-K's "approximately 2.4 million" at the end of 2024 is 3.6%. The difference may be definition
  (the bonus measure's scope is not stated) or rounding of the unit counts; it is recorded as a question, not a doubt.
- **How they talk about mistakes** **[L2024-003]**. The releases and the proxy name the misses (New Equipment down,
  adjusted operating profit down, the bonus formula's shortfall). No instance found in the documents read of a
  management letter that names a capital-allocation error such as the price paid for Zardoya.
- **The integrity record.** The 2007 European Commission fine of about $300M was for conduct by "certain Otis
  subsidiaries in Europe violating European Union competition rules" (UTC FY2007 ex. 13), under UTC's ownership and a
  different management; overcharge claims from those cartel cases are still being settled, "historical settlement
  experience of these cases have not been material" (FY2025 10-K, Note 20). "you can’t make a good deal with a bad
  person" **[M1995-084]**: the question is the present people. No instance found, in the 10-Ks of FY2020 to FY2025,
  the 10-Q, the proxy or the 8-Ks read, of misconduct, restatement, an enforcement action or an investigation of the
  present management. Litigation settlements "outside of the ordinary course of business" of $18M (2024) and $21M
  (2025) are not described further (FY2025 10-K, Note 21); recorded.
- **Love of the business, succession.** The chair and chief executive since 2017 retires by 2027-07-31; a search is
  under way, "considering both internal and external candidates" (8-K 2026-09-15). The board has not named a successor
  "ready to take over tomorrow" **[L2011-001]**, and the chair and chief executive roles are combined, with an
  independent lead director (DEF 14A 2026); "how hard it is to replace a mediocre CEO if that person is also
  Chairman" **[L2014-026]** is a weighing, not a doubt about honesty.
- **VERDICT on integrity: IN.** Doubt closes the file **[M2013-088]**; on the documents read I find a cartel two decades
  old under other owners and other managers, recorded, and no fact that raises doubt about the present people's
  honesty: the misses are reported and paid for. **Ability WEIGHS FOR**, on the Service record against a hard hand
  **[M1994-008]**, with the succession open.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**. Little is retained. 2021 to 2025: net income attributable to
  Otis $6,934M; dividends $2,650M (393 / 465 / 539 / 606 / 647) and buybacks $4,191M (725 / 850 / 800 / 1,007 / 809),
  together $6,841M, 99% of earnings, while total debt rose from $7,273M to $7,956M and cash fell (FY2021 to FY2025
  10-Ks, cash-flow statements). The dollar kept is mostly the dollar spent on the minority buyouts below.
- **Buybacks** **[L1999-023]**, **[L2016-002]**, **[M2019-002]**. The programme is a sum ($2.0bn authorized 2025-01-16)
  with no price above which it stops (FY2025 10-K, Item 5; 10-Q 2026 Q2: "does not obligate it to acquire any specific
  number of shares"). Average prices paid (dollars over shares, the 10-Ks' Note on stock and the 10-Q): $74.7 (2021,
  $725M / 9.7M), $76.6 (2022, $850M / 11.1M), $83.3 (2023, $800M / 9.6M), $94.3 (2024, $1.0bn / 10.6M), $93.0 (2025,
  $800M / 8.6M), $83.3 (2026 first half, $800M / 9.6M). **Q6's buyback line, written back from Q7:** every average price paid, $74.7 to $94.3, is above the
  bottom of the Q7 range ($41.24 all-equity) and above the top of either basis ($44.13 all-equity, $58.56 equity-only);
  the no-price programme therefore weighs against, read by what it did **[L2016-002]**: shares were bought above value,
  which harms the owners who stay **[M2019-002]**.
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**. No all-stock deal: the one STOP in Part A does not arise. The
  largest use of capital after the buyback was cash for the minority half of Zardoya Otis, $1,802M in 2022 at €7.07 a
  share, debt-financed; Q3 bounds what it earns at about 4.6% after tax or less, against a floor of about ten percent
  and against the "second best deal that’s around at a given time, including more — doing more of some of the things
  we’re already in" **[M2001-084]**, which for a company is its own stock. Value given looks larger than value got on
  the filings; the Zardoya accounts themselves were not read.
- **Dividends** rise every year ($1.65 a share declared in 2025, FY2025 10-K statement of equity), a consistent policy.
- **Part A WEIGHS AGAINST**: a fixed-sum buyback with no stated price and a large debt-financed minority purchase at a
  return under the floor.

**Part B, the pay, the board, the owners.**
- **Pay tied to what the person controls** **[M2003-019]**, **[L1996-018]**. The bonus pays on adjusted net income
  (40%), adjusted free cash flow (30%), net portfolio unit growth (15%) and orders (15%), the region heads half on their
  region; performance shares on three-year cumulative EPS and organic sales growth, adjusted by relative TSR within
  plus or minus 20%, with a cap at 100% when absolute TSR is negative from 2026 (DEF 14A 2026). Portfolio units and
  regional profit are under the measured person's control; TSR is not. No charge for capital is in the formula: "a
  batting average that does not include a cost of capital is a phony batting average" **[M1995-010]**, and the
  minority buyouts, debt-financed, add to EPS while earning under the floor. The adjusted measures leave out the
  restructuring that recurs every year (Q4). "you get what you reward for" **[M2016-083]**.
- **The board.** Chair and chief executive combined, an independent lead director; the chief executive leaves by July
  2027 and the successor is not named **[L2011-001]**.
- **The owners as partners.** Guidance is given annually (Q4) **[L2019-006]**; information is supplied in full in the
  filings, with GAAP and adjusted shown side by side.
- **Part B WEIGHS AGAINST, narrowly**: pay without a capital charge on adjusted figures, guidance, and a combined chair,
  set against pay that did fall when targets were missed.

## Q7 — WHAT IS IT WORTH? STOP.
**The definition and the rate.** Value is "the discounted value of the cash that can be taken out of a business during
its remaining life" **[R1996-018]**, counting "whatever net cash is left every year" **[M1998-080]**, at "the yield on
long-term U.S. bonds" **[L2000-021]**: 5.60%, the Treasury 30-year par yield of 2026-10-09 (Step 0). The arithmetic is
in `Test Runs/_research 2026-10-10 OTIS/q7.py`.

**The cash input, by Q7's range convention and its ten specifics.**
- Five-year window 2021 to 2025, owner cash after every real cost as Q4 recasts it. All-equity basis (central): owner
  cash before interest, average $1,427M; equity-only basis (beside): owner cash after interest, average $1,308M.
- **Acquisitions (specific c).** Bolt-on purchases of service portfolios, net of the Russian business sold, $59M a year,
  are deducted, and the total growth is credited: central base **$1,368M** all-equity, $1,248M equity-only. The
  minority buyouts (Zardoya $1,802M in 2022, Japan $75M in 2024, Otis Electric $217M in 2025, cash-flow statements) are
  debt-financed deals, which the specific values "as if paid with equity: unlevered owner cash, less today's net debt"
  (the convention's text); their financing is in today's net debt, so their cash is not also deducted from the average
  (that would count it twice). The literal variant, every buyout deducted as yearly capital spending ($419M a year),
  is shown beside. The window's owner cash already deducts the minority dividends the buyouts removed, at their earlier
  higher level, which is conservative.
- **Growth shown (aggregate, not per share; specifics of the PG re-test).** All-equity owner cash $1,476M (2021) to
  $1,442M (2025): **-0.58% a year**. Equity-only $1,374M to $1,295M: -1.47% a year. **Decline (specific b):** a negative
  growth shown is carried as negative and makes the bottom; the no-growth case is the top.
- **Cycles (specific a).** Neither 2021 nor 2025 is described by the filer as aberrational in owner cash; 2021 was the
  peak of Chinese New Equipment and carried a $160M working-capital inflow the filer attributes to volume and the timing
  of payments (FY2021 10-K, MD&A). The literal window is used, and the longer series is shown beside: all-equity owner
  cash $1,182M (2018), $1,138M (2019), $1,146M (2020), on the parent's cost allocation and with almost no interest
  before the spin (pre-spin years from the cash-flow statements of the FY2020 10-K, interest paid used), grew 2.88% a
  year from 2018 to 2025.
- **Working capital (d)** is inside operating cash flow; the receivables' drift (Q4) is therefore already charged.
- **Growth spending (e).** The maintenance guess is the depreciation charge (Q3); maintenance-only adds back $19M a year
  of capital spending above depreciation. The growth it buys is not separately visible; shown beside.
- **The cap (f).** No growth above the discount rate; zero nominal growth after year ten.
- **New Equipment** (Q2: open, not deciding) is inside the consolidated owner cash and is carried at the growth the whole
  shows, which is no growth or less.

**The range** (all-equity, central; per share after net debt of $7,623M at 2026-06-30: short-term borrowings $210M plus
long-term debt including the current portion $8,226M, less cash $813M; operating leases of about $0.5bn and the pension
deficit of $411M left out and said so; 10-Q, accession 0001781335-26-000113):

| case | ten-year growth | value of the business | per share |
|---|---|---|---|
| bottom: growth shown | -0.58% | $23,324M | **$41.24** |
| top: no growth | 0% | $24,421M | **$44.13** |
| beside: literal, every minority buyout deducted | -0.58% / 0% | | $22.48 / $24.48 |
| beside: organic pair, acquisitions left out, the filer's organic sales growth 2022 to 2025 (2.5%, 5.6%, 1%, 0%) credited | 2.25% | | $60.02 |
| beside: maintenance-only, no growth | 0% | | $45.01 |
| beside: the 2018 to 2025 growth on the central base | 2.88% | | $60.61 |
| equity-only basis: shown growth / no growth | -1.47% / 0% | $19,847M / $22,293M | $52.14 / $58.56 |

**Value range: $41.24 to $44.13 a share (all-equity, central) against $65.95; equity-only $52.14 to $58.56.** Width
1.07 to one, far inside the three-to-one line: the range is not too wide to conclude **[L2000-024]**,
**[L2000-025]**. Every variant shown beside it, including the two most generous, sits below the price.

**What the price asks.** At $65.95 the business is priced at $32,728M with its net debt; the central owner cash is 4.18% of
that, below the 30-year Treasury's 5.60%. To be worth the price at the sovereign rate, the central owner cash must grow
3.69% a year for ten years, against a shown -0.58% (2021 to 2025) or 2.88% (2018 to 2025); and that only earns the
sovereign rate, not the floor. "we don’t want to buy equities where our real expectancy is below 10 percent"
**[M2003-149]**.

**The floor and the close.** The price is above the top of the range, so the expected return at the price is below the
floor of about ten percent (the convention's text: "A price above the top of the range closes OUT however wide the
range, by the floor convention above."); "there’s just a point at which we drop out of the game" **[M2003-149]**. The
screamer test is not reached: no pencil is needed to see the price is above value **[M2009-005]**, **[M1996-084]**.

**Fair price (a reporting figure, never a verdict; Part VII; reporting convention of the brief):** the price at which the
midpoint of the range earns the floor of about ten percent, on owner cash after the company's own tax, no conversion;
the midpoint case is the central base at the growth halfway between the range's ends (-0.29% a year for ten years,
then none), discounted at 10%. **All-equity (central): $15.20 a share** (business value $13,410M less net debt
$7,623M); **equity-only (beside): $31.21 a share**. The gap between them is the net debt: at the all-equity basis the
lenders' $7.6bn takes the first dollar of a value that the floor sets at about $13.4bn **[L2017-004]**. No cheap
price is reported.

- **VERDICT: OUT** at Q7, on price: the price ($65.95) is above the top of a narrow range ($41.24 to $44.13 all-equity;
  $58.56 at the top of the equity-only basis), so the expected return is below the floor **[M2003-149]**, **[L2000-024]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q7** on price: value range $41.24 to $44.13 a share (all-equity, central; equity-only $52.14 to
$58.56) against $65.95 (aggregator, 2026-10-09). Q1 IN, Q2 IN (Service decides), Q3 weighs for, Q4 weighs against
(no STOP), Q5 integrity IN, Q6 weighs against. Reporting figures: fair price $15.20 (all-equity) and $31.21
(equity-only). Integrity facts recorded and judged at Q5 (the 2007 EU cartel fine under UTC, the cartel overcharge
claims still open).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.*
- **Q8 (the bond).** At the price the central owner cash is 4.18% of the business's value with its debt, and the
  equity-only owner cash 4.97% of the market value ($1,248M on $25,105M), against the 30-year Treasury at 5.60% (Step
  0; q7.py).
- **Q9 (debt and exposures).** Total debt $8,436M at 2026-06-30 (short-term borrowings $210M, long-term debt $8,226M of
  which $1,180M current), cash $813M; maturities: €600M 0.318% notes due 2026-12-15 (to be repaid from the $700M
  4.488% notes of 2026-05-07), $500M 2.293% and €850M 2.875% notes in 2027, $750M 5.250% in 2028 (10-Q, accession
  0001781335-26-000113, debt note). A $1.5bn revolving credit facility to 2030-08-08, undrawn, backs a $1.5bn
  commercial paper programme, none outstanding at 2026-06-30. Pre-tax earnings of $1,934M against net interest of
  $196M in 2025 (FY2025 10-K). Pension and postretirement obligations $411M; operating lease liabilities $410M
  long-term. About a quarter of long-term debt is euro-denominated ($2,214M of $8,270M principal); settlements of
  derivative contracts cost $204M of cash in 2025 (FY2025 cash-flow statement, investing), purpose not read. Shareholders' equity $-5,748M. Indemnity payable to RTX $56M, disputed (FY2025
  10-K, Note 20). Customer receivables $3,985M with an allowance of $129M.
- **Q9 (the narrower STOP's criterion).** "little or no debt" is the whole-business criterion; the company carries net
  debt of about 5.6 times its central owner cash.
- **Q12.** Nothing found against the business itself; the cartel record is at Q5.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each, with one
      departure: **Q2, Q3 and Q4 were written in one append and committed together** (commit dda8afda), not one commit
      each. Q1, Q5, Q6, Q7 (with Q6's buyback line) and the close were committed separately.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock `Screens/_daily/_overnight.lock` was held by
      the dispatching session ("interactive v5 re-runs batch 9") throughout; I did not touch it. The fold is the
      dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and not used:
      the session-start git log's subjects of batch 8 (four companies, their boxes and alert prices), and, in my own
      commit outputs during the run, the subjects of another analyst's concurrent commits on SBUX ("Q2 IN (North America
      decides; castle standing, a notch lost; China filled in)", "Q3 weighs against (a decade of added capital, owner
      cash flat)"). The memory index in context (queue counts, holding reviews owed; no company named). None used.
- [x] Every v5 id resolves (`check_quotes.py`: ids present in `principle_ledger_v5.csv`, every quoted fragment set beside
      an id found in that row, no E-ids); every filing fact carries its document and accession.
- [x] The order was kept; Q7 closed the file; nothing after it is a clearance; Q8 to Q12 NOT REACHED.
- [x] Owner cash after every real cost (capital spending, stock pay, minority dividends; restructuring inside operating
      cash), never a net-income proxy; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations' list, and at Q2, Q4, Q6); facts for later questions
      under AFTER THE STOP.
- [x] Not a point-in-time run; no row after an anchor arises.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 floor, ids and wording ignored.
- [x] `python tools/check_framework.py` PASS before the closing commit (run 2026-10-10; `check_quotes.py` also PASS: 75 ids, 28 quoted fragments, 0 problems).
- **Gaps owned.** The like-for-like rivals do not file with the SEC, so the field's returns are the filer's alone. No
  maintenance retention or cancellation rate is in any filing read. The Zardoya accounts were not read, so its return is
  a bound. The share of China in New Equipment comes from the filer's rounded words ("approximately 35%", "one fifth"),
  not a filed table. The two CONVENTIONS of this run are named where used (interest after tax at 25%; the minority
  buyouts not also deducted from the average).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Minority buyouts under specific (c).** The specific says cash paid for businesses is capital spending, and
separately that a debt-financed deal is valued "as if paid with equity: unlevered owner cash, less today's net debt". A
purchase of the minority half of a subsidiary already consolidated is both: cash paid for (part of) a business and a
debt-financed deal whose debt is in today's net debt. Deducting it from the average and also subtracting its debt
counts it twice; the two readings differ by about $20 a share here ($22.48 to $24.48 against $41.24 to $44.13). I took
the second and showed the first beside; the text should say which. (2) **The all-equity add-back.** The basis is "owner
cash before interest and after the company's tax", with no rule for the tax on the interest added back; I used 25%, the
company's own recent rate, as a convention. (3) **A segment measure changed inside the window.** The parts rule counts
"five-year operating profit" and gives no rule when the filer restates some years onto a new measure and not others
(here restructuring left the segments in 2024 and only 2022 and 2023 were recast); the share did not depend on it
(85% either way). (4) **"Midpoint of the range" for the fair price** is not defined as the midpoint of values or of
growth; for a declining range they differ by cents, but for a wide range they would not. **The brief's errors:** (a) it
asks for Carrier's and Johnson Controls' "service lines where reported"; neither files a service-line margin (JCI files
service revenue only; Carrier files no service line, only segment margins that blend equipment and aftermarket), so
the comparison could only be blended margins, and the run says so; (b) it lists Hitachi among the rivals that are not
SEC filers; Hitachi filed 20-Fs through FY2010 and deregistered in 2012 (Form 15F, CIK 47710), so for part of the span
it was a filer, though its elevators were inside a mixed segment and gave no comparable margin; (c) it says Service
decides "if it carries more than half of segment profit", where the framework's threshold is "more than half of the
company's five-year operating profit"; here both readings give Service (85% of segment profit, 97% of company operating
profit), but the bases are not the same.
