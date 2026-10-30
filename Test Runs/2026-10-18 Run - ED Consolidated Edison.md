# Company Run — Consolidated Edison, Inc. (NYSE: ED) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run (overnight cycle brief, the canonical brief with one stated departure: the lines of evidence and the
competitor set are derived by the analyst from the 10-K, not handed down). Analyst's working folder:
`Test Runs/_research 2026-10-18 ED/` (notes, fetch and arithmetic scripts, `q7_output.txt`; raw filings in the ignored
`cache/` subfolder).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. (Left for the dispatching
session to fill at the fold.) *Filled at the fold by the dispatching session, 2026-10-18, after the run was committed
(349381e5): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Contamination declared (the blind rule).** No blind-listed file was opened, listed or searched. Seen without asking:
(1) the session's opening git status and recent commit subjects, which name other companies' runs and research folders
(ELPC, AYI, ARCB) and nothing about ED; (2) the session's memory index lines, which mention holding reviews owed and counts
of gate-clearers but no ticker of this run; (3) the governing framework text itself, which says under Q7, The regulated
utility, that "sixteen utilities run 2026-10-17 and 2026-10-18 showed a fair price that was not positive on the all-equity
basis" (no names given). None of it is used below. The adopted case file behind the regulated-utility paragraph was not
opened, so that it could not carry other runs' results; the framework paragraph is applied as written.

**Lines of evidence chosen (the brief's departure), from the 10-K's Item 1, Item 1A and Item 7.** (1) The parts and their
operating profit over the cycle (Note P; the Clean Energy Businesses sold 2023-03-01); (2) the rate plans: allowed and earned
return on common equity, the allowed equity ratio, rate base, the bill impact (Note B); (3) the capital programme and how it
is financed: capex against depreciation, long-term debt raised, common equity issued and its prices, the 2023 buyback
(Item 1 Capital Requirements and Resources, the cash-flow statements, Note C); (4) the threats Item 1A and Item 1 name:
the regulator (penalties, prudence, the rate plans "May Not Provide A Reasonable Return"), state climate law moving gas and
steam customers to electricity, distributed generation, the single dense service territory; (5) the integrity record
(the gas and steam weld-film misconduct by contractors, the NYSPSC income-tax audit, the 2014 East Harlem explosion,
guidance and the adjusted figure, the proxy); (6) the balance sheets for ten years and the debt's cover.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $112.26 (close 2026-10-16, the last close before the run date; via `python tools/run.py ED`, an aggregator
  quote, flagged per operator rule 5, used for the live quote only).
- **Shares by class** from the latest filing's cover: **369,828,633 Common Shares ($.10 par value) outstanding as of July 31,
  2026**, the only class (10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0001047862-26-000142`;
  `python Screens/cover_shares.py ED` returns the same count). Checked against issued less treasury: the 10-Q balance sheet
  shows "shares outstanding of 370 and 361" (millions; 2026-06-30 and 2025-12-31) with treasury stock of 34 million shares;
  the walk from 361 is the 7,000,000 shares issued in March 2026 on settlement of the February forward (8-K
  `0001193125-26-071602`, initial forward price $110.81; 10-Q Note C: "approximately $776 million"), 1,018,307 shares
  delivered in June 2026 under the ATM forwards for about $108 million, and the stock and dividend-reinvestment plans.
  **Not yet settled at 2026-06-30:** ATM forward tranches of 1,074,178 shares (less the 1,018,307 delivered, so 55,871) at an
  initial forward price of $105.7586 and 889,415 shares at $104.6730 (10-Q Note C), about 0.95 million shares; no 8-K after
  the 10-Q reports a settlement (8-Ks of 2026-07-02 and 2026-09-04 read: a director elected; a steam rate joint proposal).
  The count used is the cover count; the unsettled forward shares would add about 0.26 percent and bring in their cash.
- **Market cap:** $41,517M (369.83M × $112.26).
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-16 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2025 (ed-20251231.htm, filed 2026-02-19, accession
  `0001047862-26-000031`): Items 1, 1A, 1C, 5, 7 and the Con Edison statements and Notes B, C, E, H, P; the 10-Ks for FY2024
  (`0001047862-25-000011`), FY2023 (`0001047862-24-000012`), FY2022 (`0001047862-23-000038`) and FY2020
  (`0001047862-21-000049`) for the earlier cash-flow statements, segment tables, rate-plan tables and debt schedules; the
  10-Q for 2026-06-30 (`0001047862-26-000142`); the proxy (DEF 14A filed 2026-04-08, `0001047862-26-000078`); the 8-Ks of
  2025-11-24 (MVP sale `0001193125-25-293866`; term loan `0001193125-25-292287`), 2026-02-25 (forward sale), 2026-03-11 (credit
  agreement `0001193125-26-102202`), 2026-05-08 (ATM `0001193125-26-214767`), 2026-06-03 (debentures
  `0001193125-26-254760`), 2026-07-02 (`0001193125-26-294715`), 2026-09-04 (steam joint proposal `0001193125-26-383674`); the
  fourth-quarter 2025 earnings presentation filed with the 8-K of 2026-02-19 (`0001047862-26-000028`).
  **One figure cross-checked against the filed statement:** net cash flows from operating activities for 2025, $4,800M on the
  filed Consolidated Statement of Cash Flows (10-K `0001047862-26-000031`), equals the XBRL value `tools/run.py` and the
  company-facts file carry (4,800). Depreciation and amortization 2025, $2,321M, likewise agrees.
- `python tools/run.py ED` arithmetic lines only (Part VII): its window stopped at 2022 because the later capital spending
  is filed under "Utility capital expenditures", an element it does not read; its 2020-2022 rows (OCF 2,198 / 2,733 / 3,935;
  capex 4,085 / 3,964 / 4,465) agree with the filed statements, but its capex omits "Cost of removal less salvage" (2025:
  $481M), a real cash cost of keeping the plant. The owner cash used below is therefore built by hand from the filed
  statements (Q4 and Q7), not from the tool's means. Stock pay (AllocatedShareBasedCompensationExpense, $35M to $64M a year
  2021-2025) is deducted. Its ten-year balance-sheet table is used in Q4 after checking two years against the filed
  balance sheets.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**, and for a regulated delivery utility the cash it throws off, not the quote, is the whole of the case. The
market serves and does not instruct **[M2006-077]**: the stock's rise from $72.27 at year-end 2020 to $112.26 says nothing
about value. No macro forecast enters **[M2000-094]**: interest rates enter only through the sovereign and through the
regulator's formula, which the 10-K says sets the allowed return from "a dividend discount model using stock prices" and "a
capital asset pricing model applied to a peer group" (10-K Item 1, Rate Plans), a property of the business, not a forecast of
ours. Who is paid to tell you **[M2020-037]**: the company's own presentation leads with "top end of guidance" and a
"Dividend King" label; read as a seller's account, not as evidence. Margin of safety: "if you have to actually do it on —
with pencil and paper, it’s too close to think about" **[M1996-084]**. The analyst's habits: look for "what’s wrong in
things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) on GAAP earnings, not owner
cash, the stock prices at about 20 times 2025 net income for common ($2,023M against $41.5B), a 4.9 percent earnings yield,
and the company targets 6 to 7 percent annual growth in adjusted EPS for 2026-2030 (earnings presentation, 8-K
`0001047862-26-000028`); added together these come near the floor, which is the strongest case for the name and is tested at
Q7; (2) the franchise is protected by law, and the 10-K states the Utilities "do not consider it reasonably likely that another
company would be authorized to provide utility delivery service" in their territory; (3) the regulator has granted rising
allowed returns (CECONY 8.8 percent for 2020-2022, 9.25 percent for 2023-2025, 9.40 percent for 2026-2028) and CECONY earned at
or above them in 2023-2025 (10-K Note B).

## THE STANDING RULE
Owning a minority stake in a listed utility bought with cash does not put the buyer at risk of ruin; the rule binds the
buyer's financing and sizing, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, **[M2012-081]**. No
leverage, no position size and no option is assumed by this run; the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product may stay plain or opaque, what counts is "the economic dynamics of the
  industry" **[M2011-014]**. What the business is (10-K `0001047862-26-000031`, Item 1): CECONY delivers electricity to
  New York City (except part of Queens) and most of Westchester, gas to Manhattan, the Bronx, parts of Queens and Westchester,
  and steam in Manhattan; O&R delivers electricity and gas in southeastern New York and northern New Jersey. Almost all the
  energy is bought in the wholesale market and passed through at cost; the Utilities earn a return on their rate base, set by
  the NYSPSC as "rate base by the pre-tax weighted average cost of capital determined in the rate plan" (Item 1, Rate Plans).
- **The key variables and whether they can be foreseen** **[M1998-044]**: (1) rate base, which grows with the capital
  programme the regulator approves (CECONY's electric average rate base for Yr. 3 of the 2026-2028 plan: $39,174M; capital
  investment forecast 2026-2030: $38 billion, earnings presentation, 8-K `0001047862-26-000028`); (2) the allowed return on
  common equity and the allowed equity ratio (9.0 percent for 2017-2019, 8.8 for 2020-2022, 9.25 for 2023-2025, 9.40 for
  2026-2028, each on a 48 percent equity ratio, 10-Ks `0001047862-21-000049`, `0001047862-23-000038`, `0001047862-26-000031`,
  Note B); (3) the gap between earned and allowed, which over nine plan years ran from 0.8 points below to 0.6 above in electric
  and gas (Q2); (4) the regulator's climate, which "in a few states has raised the specter of zero profitability or even
  bankruptcy" **[L2023-011]**; (5) state climate law, which over twenty years may shrink the gas and steam networks (CECONY's
  own five-year forecast of peak demand: electric +0.7 percent a year, gas +0.2, steam -0.9; 10-K Item 1). The first three
  are foreseeable within a range: "when you get an allowed return in the electric utility you’re almost certain of earning
  it, I mean, if you behave yourself" **[M2010-037]**, and the filings show three successive plans and their outcomes. The
  insiders do write the forecast down **[M2000-105]**: the company publishes a five-year capital and financing plan and the
  regulator a three-year rate plan. The fourth and fifth are the hard part: whether a regulator re-prices the return is not
  a matter of technology but of politics and bills, and the gas network's life under the climate law is a policy question the
  regulator will answer through depreciation and recovery orders. Neither moves the delivery wires out of the forecast; the
  electric business, which carried 73 percent of CECONY's 2025 operating income ($2,056M of $2,812M), gains load from the
  same law.
- **Routing.** No fast technology changes the ten-year economics of a wires-and-pipes delivery monopoly; distributed
  generation is named by the 10-K as "an alternative source of electricity" but it is connected to and paid for through the
  same network (Item 1, DER). This is not a bank. Con Edison is a holding company of parts and is understood by its parts
  (Q1, A holding company; Q2's parts table): the deciding part, CECONY, is understood.
- **Contrary evidence written down** **[M1997-127]**: the regulatory-climate row is the speakers' own confession of a
  utility misjudged, "I did not anticipate or even consider the adverse developments in regulatory returns" **[L2023-011]**;
  and the gas business ($751M, 27 percent of CECONY's 2025 operating income) faces a state law whose end point is not
  written in any filing read. These are carried to Q2 (what could destroy it) and Q7 (the width of the range), not used to
  close the file here, because the nine years of filed outcomes give a range for them.
- **VERDICT: IN.** The economics of a regulated delivery monopoly can be foreseen within a range from its rate plans and their
  filed outcomes **[M2012-065]**, **[M2010-037]**; doubt about the regulator is carried, not settled here.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (Q2, A business of parts; segment operating income, 10-Ks `0001047862-26-000031` and
`0001047862-24-000012`, Note P; 2021-2025, the 2023 pre-tax gain of $865M on the sale of the Clean Energy Businesses left out):

| Part | Operating income 2021-2025 ($M) | Share of five-year operating profit | Castle | Decides |
|---|---|---|---|---|
| CECONY (electric, gas, steam delivery, NYSPSC-regulated) | 12,177 (2,460 / 2,135 / 2,177 / 2,593 / 2,812) | 91.0% | a legal franchise | **yes** |
| O&R (electric and gas delivery, NYSPSC and NJBPU) | 727 | 5.4% | a legal franchise | no |
| Clean Energy Businesses (sold 2023-03-01) | 641 | 4.8% | merchant and contracted renewables | no (gone) |
| Con Edison Transmission, parent and other | -159 | -1.2% | | no |
| Total | 13,386 | 100% | | |

CECONY carries more than half and decides; the file closes on its castle.

- **1. The castle questions** **[M1995-038]**: what keeps it standing is the law. "The Utilities do not consider it
  reasonably likely that another company would be authorized to provide utility delivery service of electricity, gas or steam
  where the Utilities already provide service. Any such other company would need to obtain NYSPSC consent, satisfy applicable
  local requirements, install facilities to provide the service" (10-K Item 1). How permanent: as permanent as the franchise
  and the regulator's consent; it does not "depend on the genius of the lord in the castle" **[M1995-038]**.
- **2. Without the lord.** The business would be a delivery monopoly under any management; what management changes is the
  earned return against the allowed (Q5).
- **3. The money test.** A well-funded attacker could not duplicate the wires and mains under New York City streets and would
  need the regulator's consent to try; the speakers' railroad, "You really couldn’t create another railroad" **[M2013-054]**,
  is the same shape.
- **4. Pricing power, and the agony before a rise** **[M2005-020]**: the company has none of its own. Every rise is a rate
  case, the agony made into a procedure: the 2026-2028 electric plan raises base rates by $222M, $473M and $329M,
  "implemented on a shaped bill impact basis resulting in a consistent total bill impact of 2.80% each year" (10-K, Item 7
  summary). The regulator's own pressure is affordability: in July 2025 the NYSPSC "issued an order adopting an enhanced energy
  affordability policy" (10-K Item 1).
- **5. Volume.** Five-year forecast of peak demand at design conditions: electric +0.7 percent a year, gas +0.2, steam -0.9
  (10-K Item 7 summary).
- **6. The low-cost position.** Not the test for a franchise; the customer has no second network to compare.
- **7 and 8. The brand; the low bid.** The customer may buy the energy from another supplier, but every supplier's energy moves
  over these wires and pipes and pays the delivery charge; the low bid does not reach the delivery business.
- **9. Ask the competitors.** The 10-K names no competitor for delivery (Item 1, quoted above). The rivals it names are
  alternative sources of the energy (distributed generation, energy storage), which connect to the network. **CONVENTION of
  this run:** the competitor set is the three other owners of New York delivery utilities under the same regulator that file
  with the SEC (National Grid plc, owner of Niagara Mohawk, KEDNY and KEDLI; Avangrid, owner of NYSEG and RG&E, whose last
  10-K is for FY2023; National Fuel Gas, owner of Distribution Corporation); rationale: the 10-K names none, and the same
  commission's treatment of other franchises is the nearest evidence on how this one is treated.
- **10. Widening or narrowing** **[M1999-108]**: the allowed return has moved 9.0, 8.8, 9.25, 9.40 percent over four plans
  and the earned return has followed it (table below); by that measure the castle is stable. Against it, written down as
  found **[M1997-127]**: CECONY's aged customer receivables (over 60 days) were $1,427M at 2025-12-31 against $408M at
  2020-02-28, and total customer receivables $2,970M against $1,322M (10-K Item 7, Aged Accounts Receivable Balances). The
  customers are paying more slowly and the regulator answers with affordability programmes, the ground on which "the adverse
  developments in regulatory returns" **[L2023-011]** grew elsewhere.
- **11. What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: (a) a regulator that re-prices
  the return or refuses a prudence claim, which the 10-K names, "The Utilities’ Rate Plans May Not Provide A Reasonable Return"
  (Item 1A); (b) the gas network's shrinking under the state's climate law, a quarter of the deciding part's operating income;
  (c) one event in one dense territory, "A catastrophic event can render a single utility insolvent" **[L2005-019]**; (d) the
  open weld investigation (Q5) and the income-tax audit (Q4). None of these opens the castle to an attacker; each bears on the
  return the castle earns.

**The competitor row** (the same metric, the regulated return on common equity, from each filer's own filing):

| Company (NY utility) | Earned return on regulated equity, % | Allowed, % | Source |
|---|---|---|---|
| CECONY electric | 9.30 / 9.36 / 8.82 (2017-19); 8.5 / 8.03 / 8.41 (2020-22); 9.46 / 9.21 / 9.36 (2023-25) | 9.0; 8.8; 9.25 | 10-Ks `0001047862-21-000049`, `0001047862-23-000038`, `0001047862-26-000031`, Note B |
| CECONY gas | 9.22 / 9.04 / 8.72; 8.4 / 8.48 / 8.93; 9.00 / 9.82 / 9.45 | 9.0; 8.8; 9.25 | same |
| National Grid, New York (weighted) | 8.8 (FY2021/22); 8.6 (FY2022/23); 8.5 (FY2023/24); 8.7 (FY2024/25); 9.0 (FY2025/26) | 8.9 (FY2022/23 and FY2023/24); "96% of the allowed return" (FY2025/26) | 20-Fs `0001004315-22-000057`, `0001004315-24-000007`, `0001004315-26-000006` |
| Avangrid, NYSEG and RG&E | not stated in the filing read | 8.80 (2020 plan); 9.20 (2023 plan); 48% equity | 10-K FY2023 `0001634997-24-000031` |
| National Fuel Gas, Utility segment (NY and PA) | segment net income $57.1M (FY2024), $83.2M (FY2025) on net plant of $2.0B | 9.7 (NY, 2024 order) | 10-K FY2025 `0000070145-25-000039` |

Flagged: Avangrid's earned New York return is not stated in the 10-K read, and NFG reports its segment as net income, not as a
return on equity; the comparison rests on CECONY and National Grid, the two with a stated earned return.

- **The field's returns over the last full cycle.** Over nine plan years, through the 2020 pandemic year and the 2022 cost
  spike, the regulated New York field earned about 8 to 9.8 percent on regulated book equity, within about a point of what
  the commission allowed. In words: ordinary returns, steady. The framework sends this case away from OUT: "A return set by
  a regulator is the exception, carried to Q3 as a second best" (Q2, What it rules OUT), on **[M2009-104]**, "there’s no way
  we get rich on our utility investments. But there’s no way we get poor, either", and **[L2009-012]**, "decent returns on the
  incremental sums they invest".
- **VERDICT: IN.** The castle stands, because the law keeps the attacker out **[M2011-015]**, **[M2013-054]**; its returns
  are the regulator's and are carried to Q3 as a second best **[M2009-104]**; the regulatory climate and the gas network are
  carried to Q7's range and Q9 **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**. The regulated equity of CECONY earned 8.03 to 9.82 percent a
  year over 2017-2025 (Q2 table). On Con Edison's own book equity (the filed balance sheets; net income for common, which is
  the consolidated net income less the minority share, 10-K cash-flow statements and income statements), the return was 6.9
  percent in 2021 (impairments of $443M in the renewables), 8.2 percent in 2022, 8.4 percent in 2024 and 8.8 percent in 2025;
  2023 (12.0 percent) carries the gain on the sale of the Clean Energy Businesses. Goodwill is $406M of $24,190M of equity
  (2025-12-31), so return on tangible equity is the same within a fraction of a point. These are the returns the speakers call
  fair, not rich: "deploy large sums at fair returns" **[L2005-005]**; "there’s no way we get rich on our utility investments.
  But there’s no way we get poor, either" **[M2009-104]**.
- **To stand still and to grow** **[L1999-024]**, **[M2000-144]**. Utility capital spending with cost of removal and the
  transmission investments averaged $4,713M a year over 2021-2025 against depreciation and amortization (Clean Energy
  Businesses removed) of $2,037M, about 2.3 times (the filed cash-flow statements, accessions in Step 0). The filing does not
  split the spending into maintenance and growth; the stated guess of this run is depreciation as the maintenance need, which
  the rows allow, "not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**,
  with the confessed risk that a century-old urban network may need more than its depreciation to stay in place
  **[L2015-004]**. The growth is the rate base: CECONY's electric average rate base was $26,095M in Yr. 1 of the 2023 plan
  and is set at $39,174M for Yr. 3 of the 2026 plan (10-K Note B), about 8.5 percent a year; the company targets an 8.6
  percent annual growth of its "investment earnings base" for 2026-2030 (8-K `0001047862-26-000028`).
- **The growth arithmetic.** "To earn more, their owners must invest more" **[L2011-019]**: each added dollar of rate base
  earns the allowed return on its equity half and no more. The business cannot fund itself: over 2021-2025 operating cash
  (Clean Energy Businesses removed) of $16,557M did not cover utility capital spending of $23,343M, before $5,481M of cash
  dividends; the gap was filled with long-term debt and new shares (public offerings of $775M in 2021 and $1,308M in 2025,
  10-K cash-flow statements), and the company plans to issue "up to $1,100 million of common equity in 2026", "approximately
  $1,200 million in 2027 and up to $3,300 million in aggregate during 2028 through 2030" (10-K Item 1). That is the savings
  account into which the owner must "keep adding money" **[L2007-010]**, at a rate the regulator sets near 9.4 percent on book;
  whether that is "an attractive rate of interest that will be earned also on deposits that are added" or a disappointing one
  **[L2007-010]** depends on the price paid for the deposit, which is Q7's question. The spending is partly compulsory, set by
  reliability needs the grid operator names (10-K Item 1, a reliability need in New York City from summer 2026) and by state
  law: "we have tried to avoid places where there was a lot of compulsory reinvestment just in order to stand still"
  **[M1997-016]**.
- **The second best.** The rows admit it by name: "as the second-best choice, still a good choice, the answer is yes"
  **[M2018-055]**; "if they earn a decent return on capital, it can be a good business over time" **[M2007-112]**; the
  condition is "decent returns on the incremental sums they invest" **[L2009-012]**, which the filed record meets on book,
  and the speakers prefer the utility that must invest, "because we like the idea of getting more capital out at reasonable
  returns" **[M2014-086]**.
- **WEIGHS UNDECIDED.** For: a decent, steady regulated return on the added capital, the rows' admitted second best
  **[L2009-012]**, **[M2014-086]**. Against: the owners must keep adding money at that fair rate and no more, and part of the
  spending is compulsory **[L2011-019]**, **[M1997-016]**. Carried to Q7, where the price paid for each dollar of book equity
  (about 1.7 times, $41,517M against $24,190M) decides what the fair rate is worth to a buyer.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL vintage, $M; checked against
the filed balance sheets for 2018 and 2019, 10-K FY2019: total assets $53,920M and $58,079M, long-term debt $17,495M and
$18,527M, common equity $16,726M and $18,022M, all equal; and for 2024 and 2025, 10-K `0001047862-26-000031`: total assets
$70,562M and $74,603M, equity $21,962M and $24,190M, equal; long-term debt for 2024 is $24,651M in the FY2025 10-K against
$24,710M first filed, a reclassification of $59M. Revenue from the filed income statements.)

| Year-end | Total assets | Common equity | Cash | Customer and other receivables | Goodwill | Intangibles | Long-term debt | Revenue |
|---|---|---|---|---|---|---|---|---|
| 2016 | 48,255 | 14,298 | 776 | 1,106 | 428 | 124 | 14,735 | 12,075 |
| 2017 | 48,111 | 15,418 | 797 | 1,103 | 428 | 131 | 14,731 | 12,033 |
| 2018 | 53,920 | 16,726 | 895 | 1,267 | 440 | 1,654 | 17,495 | 12,337 |
| 2019 | 58,079 | 18,022 | 981 | 1,236 | 446 | 1,557 | 18,527 | 12,574 |
| 2020 | 62,895 | 18,847 | 1,272 | 1,701 | 446 | 1,460 | 20,382 | 12,246 |
| 2021 | 63,116 | 20,037 | 992 | 1,943 | 439 | 1,293 | 22,604 | 13,676 |
| 2022 | 69,065 | 20,687 | 1,282 | 2,192 | 408 | 0 | 22,439 | 15,670 |
| 2023 | 66,331 | 21,158 | 1,189 | 2,418 | 408 | n/a | 21,989 | 14,663 |
| 2024 | 70,562 | 21,962 | 1,324 | 2,440 | 408 | n/a | 24,710 | 15,256 |
| 2025 | 74,603 | 24,190 | 1,629 | 2,583 | 406 | n/a | 25,551 | 16,918 |

What moved and why. (1) Equity rose $9,892M in nine years, long-term debt $10,816M: the two grew together, as a regulated
capital structure near 48 percent equity requires (the 10-K's own table: Con Edison 47.1 to 50.9 percent, CECONY 46.0 to 47.9
percent of capitalization, 2021-2025). (2) The intangibles of $1,654M that appear in 2018 are the renewable projects the Clean
Energy Businesses bought; they leave with the 2022 reclassification as held for sale and the 2023 sale. Goodwill is small and
flat. (3) Receivables rose 134 percent while revenue rose 40 percent: the "inventories look out of line" tell **[M1995-064]**
in a utility's form. The filer explains it in full (Item 7, Aged Accounts Receivable Balances): customer receivables of
$2,970M at CECONY at 2025-12-31 against $1,322M at 2020-02-28, of which $1,427M older than 60 days against $408M, after the
pandemic suspension of terminations and slower collection since, with write-offs reconciled to rates under caps "that produce
no more than a half percent (0.5 percent) total customer bill impact". It is explained and disclosed; it is not a profit that
may not exist, but a customer base paying more slowly (carried to Q2, test 10). (4) Cash stays near $1 to $1.6B against
$1.2 to $1.6B a year of dividends: the business holds no reserve of its own and lives on the capital markets (Q9). (5)
Retained earnings, tagged only for 2024 and 2025 ($14,048M, $14,857M), rose $809M in 2025 while $1,308M of new shares were
sold. What the figures cannot say **[M2025-032]**: whether the regulatory assets on the balance sheet will be recovered,
which depends on orders not yet written, the largest open one being the tax matter below.

**The real costs.**
- Depreciation and amortization $2,321M in 2025 (filed statement), counted in full **[R1996-023]**; cost of removal less
  salvage ($481M in 2025) is a cash cost of retiring plant that `tools/run.py` leaves out of its capital spending and that this
  run counts with the capital spending.
- Stock pay ($35M to $64M a year, 2021-2025) is deducted **[L2015-003]**.
- No EBITDA anywhere in the 10-K, the earnings presentation or the proxy (a text search returns none).
- Pensions: the rate plans reconcile pension and retiree costs to the amounts in rates (Note B), so the pension book is the
  customers' cost more than the owners'; the cash contributions run through operating cash.
- **The income-tax audit.** "In January 2018, the NYSPSC issued an order initiating a focused operations audit of the
  Utilities’ financial accounting for income taxes. The audit is investigating the Utilities’ inadvertent understatement of a
  portion, the amount of which may be material, of their calculation of total federal income tax expense for ratemaking
  purposes" (10-K Note B, Other Regulatory Matters). The result is an income-tax regulatory asset of $1,049M at CECONY and
  $10M at O&R at 2025-12-31, "which are not earning a return", whose recovery depends on a private letter ruling not yet
  sought. Eight years open. Disclosed plainly, with the amount; the open risk is a write-down of up to about $1.06B, some
  $2.86 a share before tax effects, carried to Q7 as a reason the range is not narrower and to Q5 as part of the record.
- **Operating cash is moved by deferrals.** The line for deferred charges and regulatory assets took $496M, $870M, $1,216M,
  $797M and $721M out of operating cash in 2021-2025 (filed cash-flow statements): costs paid now and collected later. Owner
  cash is therefore averaged over five years and not read from one year **[L2005-003]**.

**The recast owner cash, equity-only basis** (Q7, The regulated utility; $M; Clean Energy Businesses removed using the
segment cash-flow and depreciation figures in the 10-Ks; the computation in `q7.py`, output in `q7_output.txt`):

| | 2021 | 2022 | 2023 | 2024 | 2025 | Average |
|---|---|---|---|---|---|---|
| Operating cash (after interest and tax) | 2,558 | 3,429 | 2,156 | 3,614 | 4,800 | 3,311 |
| less stock pay | 35 | 64 | 53 | 35 | 55 | 48 |
| less depreciation (the maintenance guess) | 1,801 | 1,878 | 2,031 | 2,155 | 2,321 | 2,037 |
| **= owner cash after maintenance only** | 722 | 1,487 | 72 | 1,424 | 2,424 | **1,226** |
| capital spending with removal and transmission | 3,983 | 4,226 | 4,789 | 5,273 | 5,295 | 4,713 |
| Utilities' net long-term debt raised (credited, below the 52 percent cap) | 1,685 | 800 | 2,050 | 2,500 | 1,150 | 1,637 |
| **= owner cash after all spending, debt credited** | 225 | -61 | -636 | 806 | 600 | **187** |

The debt credit: CECONY's issuance less retirements from its own filed cash-flow statements (2,250 less 640; 700; 2,000;
2,850 less 475; 900); O&R's issuance as the 10-Ks state it (about 75, 100, 50, 125, 250), its small retirements not
separated, so the O&R figure is an upper bound (flagged). The cap: the allowed debt share is 52 percent (the 48 percent
equity ratio of every NYSPSC plan above), applied to utility capital spending of $23,343M, $12,138M; the credit of $8,185M is
below it. Against net income for common of $1,346M to $2,023M (2021, 2022, 2024, 2025), owner cash after all spending is a
small fraction: the reported earnings are reinvested and more, the case **[L2023-009]** describes, cash that "will regularly
fall considerably short" of reported earnings.

**Guidance and the adjusted figure.** The earnings presentation leads with "$5.66 earnings per share (GAAP) / $5.70 adjusted
earnings per share (non-GAAP) - top end of guidance for the year", introduces "$6.00 to $6.20 2026 adjusted earnings per share
(EPS) guidance range (non-GAAP)", and claims "Consistently delivering actual adjusted EPS growth rates in excess of guidance"
(8-K `0001047862-26-000028`). The rows: "we become downright incredulous if they consistently reach their declared targets"
**[L2002-041]**; "a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share
earnings" makes us nervous" **[L2016-006]**; earnings guidance **[L2019-006]**. Here the adjusted and GAAP figures differ by
four cents, and the five-year adjusted growth (6.4 percent) is stated below the GAAP growth (11.46 percent), so the adjusted
figure is not used to flatter growth. Recorded as a WEIGHING against and carried to Q5 (Q4, The make-the-numbers habit).

- **VERDICT on the accounts: WEIGHS AGAINST, no STOP.** The accounts are readable and explain their own oddities (the
  receivables, the deferrals, the tax asset); nothing confuses or raises suspicion in the statements themselves
  **[M1995-063]**, **[M1995-065]**. Against: owner cash after all spending is a fraction of reported earnings **[L2023-009]**,
  the eight-year-old tax audit leaves a $1.06B asset in doubt, and guidance with an adjusted figure is featured
  **[L2002-041]**, **[L2016-006]**, carried to Q5. The recast figures above feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the speakers read rather than meet **[M2007-081]**; the reading here is the 10-Ks, the proxy (DEF 14A
`0001047862-26-000078`) and the earnings presentation.

**The integrity record, item by item.**
- **The gas and steam welds.** "CECONY determined that in some instances third-party contractors engaged in misconduct by
  substituting duplicate weld films for different welds"; CECONY "voluntarily disclosed its initial review and findings to the
  NYSDPS" and "reported the contractors’ misconduct to law enforcement"; two contractor employees were indicted in August 2025
  "for wire fraud arising out of their scheme to defraud CECONY" (10-K Note B, Other Regulatory Matters). The regulator's
  question is "the prudence of CECONY’s oversight of the weld testing process"; $100M of 2026-2028 revenue is collected subject
  to refund. The misconduct was the contractors'; the company found it, told the regulator and the police. That is the
  conduct the rows ask for when bad news arrives: "tell us the bad news immediately" **[M1998-039]**; "the main problem was
  they didn’t act when they learned about it" **[M2017-005]** is the failure, and the filing shows the opposite. What it
  shows against the company is oversight, an ability question, open.
- **The income-tax understatement** (Q4): "inadvertent", disclosed since 2018 with its amount; the taxes themselves were
  "properly calculated and paid". An error of competence in ratemaking accounting, disclosed; not a tell of dishonesty, but
  eight years without a cure.
- **The 2014 East Harlem explosion.** Eight people died; the NTSB found as probable cause "the failure of a defective fusion
  joint at a service tee [...] installed by CECONY" together with a breach in a city sewer, and in February 2017 the NYSPSC
  approved a settlement with CECONY "related to the NYSPSC's investigations of the incident and the practices of qualifying
  persons to perform plastic fusions" (10-K Note H). A safety and competence failure twelve years old, settled and still
  reported each year; not a finding of deceit.
- **The habits carried from Q4.** Guidance each year, an adjusted figure beside GAAP, and the boast "Consistently delivering
  actual adjusted EPS growth rates in excess of guidance". The rows read the habit for its purpose: "we become downright
  incredulous if they consistently reach their declared targets" **[L2002-041]**; predictions "can turn fudging into fraud"
  **[L2000-039]**. In this business the earnings are set mostly by rate orders the regulator writes and publishes (the
  allowed return, the equity ratio, the rate base targets and reconciliations, Note B), so the room to manufacture a figure is
  narrow and the outcome is checked each year by the regulator's earned-return table; the adjusted figure is four cents from
  GAAP and is not used to flatter the growth rate (Q4). The habit is a culture of managing to a number, which the rows dislike
  **[M2015-034]**, more than evidence of a number managed.
- **The proxy** **[M1994-009]**: the chief executive, Timothy P. Cawley, is also chairman (since 2022), with an independent
  lead director; his Summary Compensation Table total was $19,899,971 for 2025 and $14,984,213 for 2024, of which $14,131,247
  for 2025 is the pay the proxy calls actually received; the annual incentive turns on adjusted EPS (target $5.61, actual
  $5.70), adjusted net income and an operating budget, and the long-term units 50 percent on relative total shareholder return
  (DEF 14A). Weighed at Q6, Part B.
- **How they talk about mistakes** **[L2024-003]**: no instance found in the 10-K or presentation read of a mistake named as
  management's own (a text search of both for "mistake" and "we were wrong"); the weld and tax matters are described in the
  regulator's terms. Neither for nor against beyond that.

**Ability** (the WEIGHING) **[M1994-008]**: the hand dealt is a monopoly with a fixed allowed return, so ability shows in the
earned return against the allowed. CECONY earned at or above the allowed return in 8 of the 12 electric and gas plan-years of
2017-2019 and 2023-2025 (below: electric 2019 and 2024, gas 2019 and 2023), above it on average in the 2023-2025 plan (electric
9.34, gas 9.42, against 9.25), and below it in all six plan-years of 2020-2022 (the pandemic, with terminations suspended); National Grid's New York companies earned 96 to 99 percent of their allowed (Q2). The
sale of the Clean Energy Businesses in 2023 for a pre-tax gain of $865M, after the 2018 purchase, ended a venture outside the
franchise. Against: the aged receivables tripled (Q2, Q4), the weld oversight is under investigation, and the tax matter has
stood for eight years.

- **VERDICT on integrity: IN.** No tell of dishonesty in the record read: the bad news found was disclosed and acted on
  **[M1998-039]**, the errors are of competence and are stated with their amounts, and the guidance habit, read with the rest
  of the record and with the regulator's published check on every outcome, does not leave the doubt that closes the file
  **[M2013-088]**. **Ability WEIGHS FOR, narrowly**: the earned return tracks the allowed and averaged above it in the last plan, the
  equal of the one New York peer that states its return **[M1994-008]**; against it the receivables, the welds and the tax audit.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**. Over 2021-2025 Con Edison earned $26.71 a share (basic GAAP EPS
  3.86, 4.68, 7.25, 5.26, 5.66) and declared about $16.22 in dividends (3.10, 3.16, 3.24, 3.32, 3.40; the 10-Ks and the
  earnings presentation's "$0.15 per share to $3.55" for 2026), retaining about $10.49 a share. Book value per share rose from
  $55.06 (2020-12-31, $18,847M on 342.3M shares) to $66.99 (2025-12-31, $24,190M on 361.1M shares), $11.93, with new shares
  sold above book helping it; the market price rose from $72.27 to $112.26. On the market leg the dollar retained became more
  than a dollar **[M2011-072]**. On the intrinsic leg, which the rows require because the market leg alone misleads
  **[R2009-002]**, Q7 below finds the value per share far under the price; the retention cannot be credited with a rise that
  Q7 does not find in the cash. The forward question, "Can you keep using all of the capital you generate, effectively, for a
  very long time?" **[M2010-097]**: yes, and more than it generates, at the regulated rate (Q3).
- **Buybacks.** One programme in the window: in 2023, after the sale of the Clean Energy Businesses, "accelerated share
  repurchase agreements with two dealers to repurchase $1,000 million in aggregate", receiving 10,543,263 shares (10-K FY2023
  `0001047862-24-000012`, Note C), an average of $94.85 a share. The plan named a sum, not a price (10-K FY2022: "repurchase up
  to $1,000 million of its common shares"), which weighs against **[L2016-002]** unless the prices paid sat at or below the
  bottom of the Q7 range: **written back from Q7: the bottom of the equity-only range is $14.35 a share and its top $61.04; the $94.85 paid sits above the whole range, so the purchases do not escape the weight against**. In the same years the company sold shares to fund
  its spending, so the buyback returned in 2023 money it raised again in 2025.
- **Issuance and deals.** New shares were sold in 2021 (public offering, $775M), March 2025 (7,000,000 shares for about $677M,
  $96.71 a share, and 6,300,000 for about $631M, $100.16), March 2026 (7,000,000 shares on a forward at an initial $110.81, 8-K
  `0001193125-26-071602`) and through the 2026 at-the-market forwards ($104.67 to $105.76, 10-Q Note C), and the plan is about
  $5.6B more in 2026-2030 (Q3). Value given against value got **[R1995-010]**, **[M1995-001]**: shares sold above every case
  of the Q7 range transfer value to the continuing holders, not from them. But the pattern is serial, the behaviour of a
  company that must issue to grow, and "we have never invested in companies that are hell-bent on issuing shares"
  **[L2014-015]**; the framework carries serial issuance as a candidate second STOP, unresolved (Q6 and section VI), so it is
  weighed here, against. No acquisition paid in shares in the window: the one STOP of Part A **[L2009-019]** does not arise.
- **Dividends.** The company calls itself a "Dividend King" with "52 consecutive years of dividend increases" (8-K
  `0001047862-26-000028`) and paid $1,166M in 2025 while raising $1,308M of new equity. A dividend paid with one hand and
  replaced by stock sold with the other is a round trip through the market with its costs, the policy the rows test by
  whether the dollar kept is worth more than a dollar **[M2004-089]**; a fixed habit of increase is the kind of rule by ratio
  the speakers call "nuts" **[M2000-051]**. Weighs against, mildly: the dividend is clear and consistent **[L2012-015]**.

**Part B: the pay, the board and the owners** (DEF 14A `0001047862-26-000078`).
- Pay: the annual incentive turns on adjusted EPS (a 55 percent weight for the named officers, target $5.61, actual $5.70),
  adjusted net income and an operating budget, partly within the managers' control but tied to the figure they also guide
  to **[M2003-019]**; the long-term units vest 50 percent on relative total shareholder return, a "lottery ticket" whose value
  "is totally out of the control of the person whose behavior we would like to affect" **[L1996-018]**; levels are set
  against "a compensation peer group of publicly-traded utility companies of comparable size and scope", the comparison the
  rows call a ratchet **[M2012-095]**. The chief executive's reported total rose from $14,984,213 (2024) to $19,899,971
  (2025).
- The board: the chief executive is also chairman, with an independent lead director **[L2014-026]** (the rows' warning is
  for a mediocre one; Q5 does not find him so).
- Owners as partners: guidance each year, the opposite of Berkshire's rule by inversion **[M2022-054]**; the disclosure is full
  and the bad news (welds, tax audit) is in the 10-K with amounts **[L1994-023]**.

- **Part A WEIGHS AGAINST**: a buyback with no stated price at $94.85 (tested against the Q7 bottom below), serial issuance
  **[L2014-015]**, and a dividend replaced by new stock; the issuance prices, above value, are the one credit **[R1995-010]**.
  **Part B WEIGHS AGAINST**: pay on the guided figure and on relative share-price return, set by peer comparison
  **[L1996-018]**, **[M2012-095]**.

## Q7 — WHAT IS IT WORTH? STOP.
**The question** **[L2000-021]**: how much cash, how sure, how soon, at the long government rate (5.43 percent, Step 0).
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
credited only "for whatever net cash is left every year" **[M1998-080]**, after asking "are you going to have to put more
cash into after you buy it?" **[M2014-068]**.

**The basis.** The deciding part (CECONY, 91 percent, Q2) earns a return the NYSPSC allows on its invested capital, so the
central figure is the equity-only basis (Q7, The regulated utility): the row's own exception, "debt dedicated [...] to the
fixed-asset commitments at our regulated utilities" **[L2017-012]**, with "when you get an allowed return in the electric
utility you’re almost certain of earning it" **[M2010-037]**. The Utilities' long-term debt raised over the window is credited
against the capital spending, capped at the allowed debt share of 52 percent stated in every rate plan (Q4 table: $8,185M
credited against a cap of $12,138M). The all-equity figure is shown beside and does not decide. The floor of about ten percent
is earned on the equity **[M2003-149]**, after the company's own tax, no conversion (Q7, Whose tax).

**The cash input** (Q4's recast table; `q7.py`, `q7_output.txt`): five-year average owner cash after maintenance only,
**$1,226M** a year; after all spending with the debt credited, **$187M** a year.

**The specifics applied.**
- (a) Cycles: no year of the window is called aberrational by the filer; the low 2023 (deferred charges of $1,216M taken out of
  operating cash) sits inside the window and is averaged. Literal window beside: consolidated owner cash after all spending,
  Clean Energy Businesses not removed and no debt credit, averages **-$1,534M** a year (2021-2025: -1,589, -931, -2,793, -1,623,
  -732).
- (b) Decline: none shown. The all-spending series changes sign (225, -61, -636, 806, 600), so its growth is measured between
  the halves (first two years 82, last two 703), an eightfold rise that traces to an absurdity **[M1999-067]**.
- (f) The cap: the growth carried is therefore the business's own sales growth over the window, 7.53 percent a year (revenue,
  Clean Energy Businesses removed, $12,654M in 2021 to $16,918M in 2025), never above the discount rate, so **5.43 percent**
  for ten years, then zero nominal growth (the PG specifics). The shown rate (absurd) and the cut are both written here.
- (c) Acquisitions: none in the window for the utilities; the Clean Energy Businesses (sold 2023) are removed from every year
  of the series and their sale proceeds are not credited; Con Edison Transmission's interest in Mountain Valley Pipeline was
  sold in late 2025 for $357M (8-K `0001193125-25-293866`) and enters only through cash in today's net debt. No signed, unclosed deal.
- (d) Working capital: inside operating cash as filed.
- (e) The maintenance case is central where the filing allows the guess; it does, at depreciation (Q3). The growth spending
  ($2,676M a year above depreciation) buys growth worth less than its cost at this rate, so the maintenance-only no-growth case
  is the top of the range and the growth case the bottom: the inversion is the finding, "growth can destroy value"
  **[L2000-023]**, here because the regulator lets the added capital earn about what it costs and no more.

**The range, equity-only (central), at the sovereign 5.43 percent, per share on 369,828,633 shares:**

| Case | Owner cash base | Growth | Value a share | Value at 10% |
|---|---|---|---|---|
| Top: maintenance only, no growth | 1,226 | 0 | **$61.04** | $33.15 |
| Bottom: all spending, debt credited, growth carried | 187 | 5.43% ten years | **$14.35** | $7.33 |
| Beside: all spending, debt credited, no growth | 187 | 0 | $9.30 | |
| Beside: debt credit on gross issuance ($9,300M) instead of net | 410 | 5.43% | $31.50 (expected return at price 1.62%) | |

**Value range (equity-only, central): $14.35 to $61.04 a share against $112.26.**
All-equity beside (owner cash before interest, interest after tax at 25 percent, less net debt of $26,347M at 2026-06-30:
long-term debt $26,843M, current portion $250M, notes payable $721M, finance leases $3M, less cash $1,470M, 10-Q
`0001047862-26-000142`; operating leases left out): **-$123.30 to $28.27 a share**.

**The floor, tested first** (Q7, The floor is tested first). At $112.26 the shares cost $41,517M. The expected return on
each case at that price: top case **2.95 percent**; bottom case **0.75 percent**; the gross-credit variant 1.62 percent; the
top case grown at the uncapped sales growth of 7.53 percent, which the framework does not allow, 5.39 percent. The strongest
case against this close, written down **[M1997-127]**: GAAP net income for common of $2,023M (2025), a figure the framework
forbids as owner cash (operator rule 5) and shown only as a test, grown at the company's own 6.5 percent target for ten years,
returns **7.87 percent** at the price, and 8.41 percent at 7.53 percent growth. **No case earns the floor of about ten
percent** at the price, nor does the forbidden one. The file closes OUT whatever the width (4.3 to 1, which would otherwise be
TOO HARD): "there’s just a point at which we drop out of the game" **[M2003-149]**. The price is also above the top of the
range, which closes OUT by the floor convention on its own. The speakers met the same thing: "some utilities have sold at
extraordinary prices. And we can’t pay them and have it make sense for Berkshire shareholders" **[M2017-095]**; and the
utility at a full price "closes OUT as before" (Q7, The regulated utility), "no way we get rich on our utility investments"
**[M2009-104]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and averaged, after the
company's own tax: **$20.24 a share on the equity-only basis (central, the regulated utility)** ($33.15 top, $7.33 bottom);
**-$57.52 a share on the all-equity basis (beside)** ($-17.20 top, $-97.84 bottom). No cheap price is reported. The
unsettled at-the-market forward shares (about 0.95 million, 0.26 percent) would bring in their cash and move neither figure
by more than a cent or two.

- **VERDICT: OUT.** No case of the range earns the floor at $112.26; the best case returns 2.95 percent on the equity
  **[M2003-149]**, below even the long bond at 5.43 percent; the price sits above the top of the range **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed OUT). Facts under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7**: the equity-only value range (central, the regulated utility) is $14.35 to $61.04 a share against $112.26, the
best case returns 2.95 percent at the price, and no case earns the floor (fair price $20.24 equity-only central, -$57.52
all-equity beside). Q1 IN, Q2 IN, Q3 UNDECIDED, Q4 WEIGHS AGAINST, Q5 integrity IN and ability WEIGHS FOR narrowly, Q6 Part A
and Part B WEIGH AGAINST. Not a TOO HARD; no research pass. *Re-look condition (the operator's alert, not a rule): the fair
price; and a fresh Q7 when the income-tax audit or the weld investigation is decided, or a new rate plan changes the allowed
return.*

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury yields 5.43 percent (Step 0); the top case of the range returns 2.95 percent at the
  price and the strongest contrary test 7.87 percent (Q7).
- **Q9 (debt and exposures).** Pre-tax income plus interest over interest (consolidated, 10-K income statements via the XBRL
  facts, the 2023 pre-tax gain of $865M removed): 2.2 times in 2020, 2.5 in 2021, 3.5 in 2022, 3.1 in 2023, 2.8 in 2024, 3.1 in
  2025. Borrowings at 2026-06-30: long-term debt $26,843M, current portion $250M, notes payable (commercial paper) $721M; cash
  $1,470M (10-Q `0001047862-26-000142`). The company plans long-term debt of "up to $3,200 million" in 2026 and "up to $3,000
  million" in 2027, "including for maturing securities", and about $9,900M in 2028-2030 (10-K Item 1): the maturities are
  refinanced, not paid. The parent's dividends and interest depend on dividends from the Utilities, which the NYSPSC limits to
  "not more than 100 percent of their respective income available for dividends calculated on a two-year rolling average
  basis" (Item 1A). One dense territory: the 2014 East Harlem explosion (eight dead), the open weld investigation, and the
  10-K's risk that "A failure of, or damage to, these facilities [...] could result in bodily injury or death" (Item 1A); the
  tariff limits liability for service interruptions to gross negligence or willful misconduct (Item 1).
- **Q10.** Nothing recorded.
- **Q12.** Delivery of electricity, gas and steam in New York City; no business named in Q12's list. Nothing recorded.
- **Integrity facts** were judged at Q5, which was reached; no flag is owed.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Step 0 to
      the lines of evidence were committed before the session limit (6d8106c7); Q1 to Q7 were written and committed one by one
      on resume.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's; the fold is the
      dispatching session's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Contamination declared at the top;
      added on resume: the opening commit list of this session showed the subject "Overnight log: ED skipped, run file fresh"
      (a scheduling note, no result) and subjects of an ELPC run (another company); not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (`check_ids.py`
      in the research folder, 0 problems); no E-id; every filing fact has its accession.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; nothing after it is a clearance. The Q7 arithmetic was
      computed before the session limit (`q7.py`) and was not read into Q1 to Q6 as a clearance; Q6's buyback line was written
      back with Q7, as the template asks.
- [x] Owner cash after every real cost, never a net-income proxy: built by hand from the filed cash-flow statements; GAAP net
      income appears only as a labelled test of the close, forbidden as an input and not used in the range. The sovereign from
      the Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found: the foundations' earnings-yield-plus-growth case, the receivables, the tax
      asset, the welds, the regulator, each where found.
- [x] No row dated after the anchor (a live run; not point-in-time).
- [x] Only the arithmetic lines of `tools/run.py` were used; its capital spending stops at 2022 and omits cost of removal, so
      the series was built from the filed statements.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Confessed weak points: (1) the O&R share of the debt credit is its gross issuance as the 10-Ks state it, its retirements not
  separated (an upper bound, at most about $120M a year); (2) the Clean Energy Businesses' operating cash for 2021 and 2022
  ($175M, $506M) was re-read on resume in the segment liquidity table of the 10-K FY2022 (`0001047862-23-000038`) and agrees;
  their depreciation ($231M, $178M), removed from the maintenance guess, was written into `q7.py` before the session limit
  and not re-read; (3) depreciation as the maintenance need is a stated guess the filing does not confirm; (4) the
  all-equity figure taxes interest at 25 percent, a round figure near the combined federal and state rate, not a filed rate;
  it decides nothing.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **"The long-term debt raised over the window"** (Q7, The regulated utility) does not say gross issuance or issuance less
retirements, nor whether a holding company's parent debt counts. Refinancing raises debt without funding any asset, so this
run credited the Utilities' issuance less retirements (central, $8,185M) and showed gross issuance beside ($9,300M); the
parent's debt was left out because the parent retired debt with the sale proceeds of a business removed from the series. The
two readings move the bottom case from $14.35 to $31.50 a share and decide nothing here, but on a closer price they would.
(2) **Whether the debt credit applies to the maintenance-only case.** Specific (e) makes the maintenance-only no-growth case
the top; the utility paragraph credits debt "against the capital spending it funded". At no growth the rate base and its debt
stay flat, so no new debt is raised and none was credited to the top case; the text does not say so. (3) **The cap's two
sentences in (f)**: "inside the ten years the shown rate is the cap" and, for an absurd rate, "the business's own sales growth
[...] never above the discount rate". Here the cut rate (7.53 percent) exceeds the sovereign, and the run carried 5.43 percent
on the second sentence. (4) **Q2 test 9 for a monopoly**: the test presumes rivals; the brief's departure supplied the
convention (the same regulator's other franchises), but the framework itself has no rule for a business whose filing names
no competitor. (5) **Q2's regulator exception** sends ordinary regulated returns "to Q3 as a second best", and Q3 has no
paragraph that receives them; Q3's test 4 covered it in substance.
