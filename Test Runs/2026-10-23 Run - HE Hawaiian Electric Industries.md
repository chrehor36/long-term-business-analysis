# Company Run — Hawaiian Electric Industries, Inc. (NYSE: HE) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
50362895).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. The dispatching session
fills it at the fold. **Filled at the fold (2026-10-23, after the run was committed): not held** (`PORTFOLIO.md` read for HE only).

**Dispatched run.** Analyst dispatched by an unattended overnight cycle under `Screens/_daily/_dispatch_brief.md`, with
two departures the brief states: the lines of evidence and the competitors are chosen by the analyst from the 10-K (both
recorded below). The lock in `Screens/_daily/` is held by the dispatching session; this analyst did not touch it.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/` made to check for a name clash showed
other run files and research folders dated 2026-10-23 for EDN, ENIC, ES, ETR, EVRG, FE and FTS; none was opened. (2) The
session context carried recent commit subjects about an FTS run (its box and figures); not used. (3) The session context
carried the user's memory index, whose queue line names counts of gate-clearers; it says nothing of HE and was not used.
No file about HE under any name was seen.

**Lines of evidence chosen from the 10-K** (brief's departure; Item 1, 1A and 7 of 0000354707-26-000008): (a) the
regulatory compact: PBR, decoupling, the authorized and achieved returns, the 2027 rebasing; (b) the Maui windstorm and
wildfire settlement, its four installments and how they are financed; (c) the future liability regime (Acts 191, 258,
301 of 2025) and wildfire mitigation; (d) the competitive threats Item 1A names: self-generation, wheeling (Act 266),
competitive bidding, co-op or municipal structures; (e) the divestitures (ASB, Pacific Current) and the holding company's
own cash; (f) credit ratings below investment grade and liquidity; (g) pay and the board (proxy).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $8.75 (close 2026-10-22, as printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: HEI common, without par value, **172,728,004** outstanding July 31,
  2026 (10-Q for the quarter ended June 30, 2026, filed 2026-08-07, accession `0000354707-26-000054`;
  `python Screens/cover_shares.py HE`). The cover's second line, 17,854,278 shares of Hawaiian Electric Company, Inc.
  ($6-2/3 par), is the subsidiary's common, "not publicly traded" and wholly owned by HEI (same cover, and 10-K Item 1:
  "All of Hawaiian Electric’s equity securities are directly owned by HEI"); it is not added. Check: the balance sheet
  states 172,728,004 shares "issued and outstanding" at June 30, 2026; no treasury shares (no-par stock, issued equals
  outstanding). 8-Ks after the 10-Q (2026-09-08 presentation, 2026-09-21 ASB stake sale) report no HEI share issuance.
- **Market cap:** 172.728M x $8.75 = **$1,511M**.
- **Sovereign for the earnings currency (USD):** **5.29%**, US Treasury daily par yield curve, 30-year, 10/22/2026 (issuing
  authority; as fetched by `tools/run.py` through `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-27, accession `0000354707-26-000008` (Items 1, 1A, 5,
  7, 8 notes 1-2 and the cash-flow statements of HEI and of the Utilities); 10-Q for Q2 2026, filed 2026-08-07,
  `0000354707-26-000054` (balance sheet, Note 2, Note 4 legislation, MD&A capital structure); proxy, DEF 14A filed
  2026-04-29, `0001104659-26-051288` (summary compensation table and footnotes, say-on-pay); 8-Ks
  `0000354707-26-000044` (2026-07-31, Kalaeloa PPA), `0000354707-26-000053` (2026-08-07, Q2 earnings release, exhibit 99),
  `0000354707-26-000061` (2026-09-08, investor presentation, cover only), `0000354707-26-000066` (2026-09-21, ASB IPO
  stake sale); for the cycle, the 10-Ks for FY2024 `0000354707-25-000013`, FY2022 `0000354707-23-000032` and FY2021
  `0000354707-22-000049` (cash-flow statements and capital-structure tables).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, continuing
  operations, FY2025: $391,073 thousand on the face of HEI's consolidated statement of cash flows (10-K
  0000354707-26-000008, page 75) against $391.1M in the tagged data printed by `tools/run.py`. Agrees.
- `python tools/run.py HE`, arithmetic lines only (output kept in `Test Runs/_research 2026-10-23 HE/run_py_output.txt`).
  **Read with care:** its OCF series for 2023 and 2024 (551.5, 487.5) includes American Savings Bank, sold December 31,
  2024 and shown as discontinued operations; this run uses the filed continuing-operations lines instead (2022 333.7,
  2023 443.4, 2024 428.1, 2025 391.1, $M; 10-Ks 0000354707-25-000013 and 0000354707-26-000008). Capital expenditures,
  continuing: 2022 339.3, 2023 442.7, 2024 344.3, 2025 341.2. Stock pay: 2022 7.45 (restated continuing), 2023 6.78, 2024
  3.59, 2025 3.43. Other capital payments the tool found: preferred dividends of subsidiaries 1.89 a year (preferred
  redeemed in 2025), finance-lease principal 0.85, 3.52, 4.68, 10.37 (2022-2025). Depreciation of plant: 2022 244.5, 2023
  255.0, 2024 261.7, 2025 260.0. The tool's warning lines and v4 matter are not used (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether one would be content to own HE "if the market closed for five years"
**[M1997-109]**, which for a utility turns on the regulator and the liability regime, not the quote. The market serves: the quote, whatever it has done since the fire, "doesn’t tell us anything. It just tells us
prices." **[M2006-077]**; no price history is used as evidence here. No macro enters **[M2000-094]**: no rate or energy-price
forecast is used. Who is paid to tell you: the company features a "Core" earnings figure that excludes "Maui
wildfire-related items" (8-K 0000354707-26-000053), a figure prepared by the party with the incentive; it is weighed at
Q4. The analyst's habits: contrary evidence is written down as found **[M1997-127]**. **Contrary evidence, written down
as found** **[M1997-127]**: (1) the Berkshire letter for 2023 names this very jurisdiction: "the regulatory climate in a
few states has raised the specter of zero profitability or even bankruptcy (an actual outcome at California's largest
utility and a current threat in Hawaii). In such jurisdictions, it is difficult to project both earnings and asset
values" **[L2023-011]**; (2) HEI's ten-year return on its equity, 2016-2025, sums to about 2% a year (Q2); (3) the
Utilities' trailing Core return on equity is 5.7% against an authorized 9.5% (8-K 0000354707-26-000053, page 10; 10-K
page 51); (4) $1.44 billion of settlement is still to pay against a market value of $1.51 billion, and the 10-K's risk
factors say "Shareholders of HEI’s common stock may experience future dilution as a result of future equity offerings."
(10-K, Item 1A).

## THE STANDING RULE
Owning HE in a portfolio bought without borrowed money and sized so that its loss cannot end the owner leaves the
buyer's rule intact: "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt and its
exposure to one more fire are the target's, weighed at Q9, not the buyer's conduct. Nothing in a purchase of HE shares
requires the buyer to give an option or accept a call on cash.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the text states it.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**; "the first step" is to "identify the key variables" and
  evaluate "how predictable they were" **[M1998-044]**.
- **What the business is** (10-K 0000354707-26-000008, Item 1): after the sale of 90.1% of American Savings Bank on
  December 31, 2024 and of all Pacific Current investments in 2025 save Mahipapa, HEI is a holding company over three
  vertically integrated regulated electric utilities serving about 95% of Hawaii's population on five island grids that
  are not interconnected; "one reportable segment: Electric utility"; the Utilities' revenues were about 99% of HEI's in
  2025. The stated strategy is "to divest all of its affiliated companies other than the Utilities". Revenues are set by
  the PUC under performance-based regulation: a decoupling mechanism ("revenues not linked to kWh sales"), an annual
  revenue adjustment indexed to inflation, pass-through of fuel and purchased power (98% customer, 2% utility, capped),
  an exceptional project recovery mechanism, and an earnings-sharing band of 300 basis points around an authorized ROACE
  of 9.5%, suspended since August 31, 2023.
- **The key variables, and whether they are foreseeable.** (1) The allowed return and how much of it is earned: knowable
  in kind from the PBR order and the history; rate-making ROACE 2025 was 9.92% (Hawaiian Electric), 8.19% (Hawaii
  Electric Light), 4.54% (Maui Electric) against 9.5% (10-K page 51); a rate rebasing is proposed for 2027 (8-K
  0000354707-26-000053). (2) The rate base and its growth: grid hardening (wildfire mitigation plan approved December 31,
  2025, $350M of project costs approved for recovery June 25, 2026), the renewable transition, all recovered through
  rates if prudent. (3) The settlement: now fixed in amount and timing, three installments of about $479M due April 2027,
  2028 and 2029 after the first was paid April 10, 2026 (10-Q 0000354707-26-000054, Note 2); how it is financed (debt,
  equity, equity-linked) is not yet stated. (4) The liability regime for a future fire: Act 258 of July 1, 2025 "directs
  the PUC to study the viability of a wildfire relief fund, establish an aggregate liability cap on economic damages from
  future wildfires and authorizes securitization" (10-Q Note 4); the cap is not yet set. (5) Volume: MWh sales 8,261
  thousand in 2021, 8,423 thousand in 2025 (10-K Item 1); decoupled, so volume moves revenue little.
- **Reading.** The economics of a decoupled regulated utility are a formula the filings state: rate base times an
  allowed return, less what the regulator disallows and what the company fails to earn. Variables (1), (2), (3) and (5)
  are important and knowable **[M2006-076]**. Variable (4), the size of the next fire's liability, is important and not
  knowable today; but it bears on whether the castle can be destroyed (Q2, test 11) and whether the target can be ruined
  (Q9), not on whether the earning power of the franchise can be pictured. The row on Hawaii **[L2023-011]** says earnings
  and asset values there are "difficult to project"; by the run's convention on a row about one named company (Q2, A row
  about one company), it is weighed, not a verdict, and it was written before the settlement was fixed and before Acts
  191, 258 and 301. The doubt row "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]** was put to the business: the business itself, a wires-and-generation monopoly on islands, is not in
  doubt; what is in doubt is a liability and a regulatory climate, which the text sends to Q2 and Q9 **[L2023-011]** (Q7,
  The regulated utility: "the regulatory climate at Q2 and Q9").
- **Routing.** Not a fast-changing technology business (the energy transition is real, and slow, and Item 1A names it;
  carried to Q2); not a bank (ASB is gone; the 9.9% retained stake, partly sold, is a small security); a holding company
  understood by its one part, the Utilities, which decides (all of operating profit; the "All Other" segment lost money
  in 2025).
- **VERDICT: IN.** The deciding part is understood by its figures **[M2008-069]**: "where the business will be in 10
  years" **[M2000-037]** can be pictured as a regulated utility earning a set return on a slowly growing rate base. The
  unknowable liability regime is carried to Q2 (test 11) and Q9, written down, not waved off.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**

- **1. The key factors and how permanent.** A legal franchise: the State granted the three Utilities "nonexclusive
  franchises" over the streets, "in effect for an indefinite period of time until forfeited, altered, amended or
  repealed" (10-K 0000354707-26-000008, Item 1); five island grids with no interconnection; competition in generation
  "moderated by the scarcity of generation sites, various permitting processes and lack of interconnections to other
  electric utilities" (10-K, MD&A, Competition). The franchise is permanent only as long as the legislature and the PUC
  keep it so; Item 1A names "co-ops or a municipal" structures and unbundling as changes that "could potentially cause
  the Utilities to lose their competitive advantages".
- **2. Without the lord.** A regulated wires business needs no superstar to earn its allowed return; but August 2023
  showed that operating judgment in a wind event decides whether the equity survives. Carried to Q5 and Q9.
- **3. The money test** **[M2011-015]**. No attacker with money can build a second grid on Oahu. Generation is open to
  attack and is being taken: the PUC requires competitive bidding for new resources (10-K, MD&A, Competitive bidding);
  purchased power was 3,674 thousand MWh of 8,979 thousand MWh generated and purchased in 2025 (10-K Item 1);
  customer-sited solar rose from 1,418.0 thousand MWh in 2021 to 1,856.5 thousand MWh in 2025, against utility sales of
  8,423 thousand MWh in 2025 (10-K Item 1, operating statistics). Act 266 (2025) authorizes wheeling of renewable power,
  capped at two megawatts (10-Q 0000354707-26-000054, Note 4).
- **4. Pricing power, and the agony before a rise** **[M2005-020]**. The price is set by the PUC, not by the company:
  decoupled target revenues, an inflation-indexed ARA with a customer dividend, fuel and purchased power passed through
  (10-K Item 1). The agony is the commission's. The monopoly row, "If you name some business that has incredible pricing
  power, you’re talking about a business that’s a monopoly or a near monopoly." **[M2010-092]**, fits the wires; but the
  power is lent by the regulator, which suspended the earnings-sharing mechanism on August 31, 2023 so that customers
  would not bear fire costs; and the Utilities "have stated that customers will not be impacted by payments related to
  the Settlement Agreements" (10-K page 51).
- **5. Unit volume.** MWh sales 8,261 thousand (2021) to 8,423 thousand (2025); customer accounts 471,605 (2023) to
  474,241 (2025) (10-K Item 1). Flat volume; decoupling makes it matter little to revenue.
- **6. Low-cost position.** Not the castle here; a regulated cost-of-service monopoly. No cost comparison against
  mainland utilities was read; none decides for a wires monopoly that faces no rival on its own grid.
- **8. Would the customer choose it over the low bid?** For the grid, the customer has no choice; for energy, a rising
  share chooses the roof (test 3). The grid's fixed costs are then spread over fewer kWh, a cost shift the 10-K names
  under Act 266 ("cost shifting and customer equity considerations").
- **9. Ask the competitors.** Not done (no rival on the grid; IPPs and installers not on the public record read).
- **10. Widening or narrowing** **[M1999-108]**. Narrowing at the generation edge (bidding, rooftop solar, wheeling);
  under strain at the political edge (Item 1A's co-op or municipal structures; the credit downgrade "makes it more
  difficult for independent power producers to procure low-cost financing", 10-K Item 1). Supported at the centre: after
  the fire the legislature passed Act 191 (State "step-in" for PPAs), Act 258 (wildfire relief fund study, an aggregate
  liability cap to be established, securitization of mitigation) and Act 301 (the State's share of the settlement); the
  PUC approved the 2025-2027 wildfire mitigation plan and $350M of its costs for recovery (10-Q Note 4); the three rating
  agencies upgraded HEI in May and June 2025 (10-K page 40) and another upgraded "in recent months" (8-K
  0000354707-26-000053).
- **11. What could destroy, modify or reduce it** **[M2000-014]**. A second fire with liability not yet capped (Act 258's
  cap is to be established, not established); the regulatory compact turned against the owners, which the speakers name
  for this jurisdiction **[L2023-011]**; the economics of "whether you earn X or go broke is not an equation that works"
  **[M2024-011]**. The franchise survived the worst of these once: the castle stood, the equity did not (Q4).

**The competitor row.** The 10-K names no rival company; it names classes of rival (customer self-generation, IPPs,
wheeling, co-ops or municipal structures), none of which files a comparable statement. **CONVENTION of this run:** the
comparators are three SEC-filing western electric utilities, two struck by wildfire liability in the same decade (PG&E
Corporation, Edison International) and one not (Avista); rationale: a castle whose test is a regulated return with a
wildfire tail is best set beside utilities facing the same tail. Metric: net income to common over average common
equity, from each filer's tagged 10-K data (first-filed values; transcription; `roe_output.txt` in the research folder),
2016-2025.

| Filer (latest 10-K accession) | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Ten years |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HEI (0000354707-26-000008; bank included to 2024) | 12.4 | 7.9 | 9.5 | 9.8 | 8.6 | 10.4 | 10.5 | 8.8 | -74.6 | 8.0 | about 2.0% |
| PG&E Corp (0001004980-26-000009) | 8.1 | 8.9 | -43.0 | -86.1 | -10.1 | -0.5 | 8.2 | 9.4 | 9.0 | 8.3 | about -1.8% |
| Edison Intl (0000827052-26-000012; equity incl. noncontrolling) | 9.5 | 4.0 | -3.2 | 9.1 | 4.7 | 4.5 | 3.5 | 6.8 | 7.2 | 24.1 | about 7.3% (5.1% without 2025, a year not read) |
| Avista (0001193125-26-067872) | 8.6 | 6.9 | 7.8 | 10.6 | 6.5 | 7.0 | 6.9 | 7.1 | 7.1 | 7.3 | about 7.3% |

(Ten years: the sum of net income over ten years against the average year-end equity, in percent.)

**The parts table.** One part decides: the Utilities, all of HEI's operating profit over 2021-2025 (the "All Other"
segment, holding company and Pacific Current, lost money; 10-K Item 1 gives the Utilities' net income as 137% of HEI's
income from continuing operations in 2025 and 133% in 2023). The bank was a part until December 31, 2024 and is gone.

**The field's returns over the last full cycle.** In years without a fire the field earns the regulated return, about 7%
to 10% on book equity; across a decade that includes a fire, the struck filers earned about nothing on their equity
(HEI about 2%, PG&E below zero). Judged in words, under the convention that "ordinary" carries no figure: the castle
protects a regulator-set return, and in a fire decade it did not protect even that. By the text, a return set by a
regulator is carried to Q3 as a second best **[M2009-104]**, **[L2009-012]**: the rows expect "decent returns on the
incremental sums they invest" **[L2009-012]**, and "there’s no way we get rich on our utility investments. But there’s
no way we get poor, either." **[M2009-104]**. The second half of that row is what the last decade put in doubt here; the
doubt is carried to Q3, Q7 and Q9.

**Contrary evidence, written down as found** **[M1997-127]**: the speakers' own reading of this jurisdiction
**[L2023-011]**; Abel's row (2025 meeting) that "You earn a very set return for taking on a very defined risk associated
with that asset, and this has gone well beyond that." **[M2025-040]**; the flat volume and the rising roof; the field's
ten-year returns.

- **VERDICT: IN.** The castle, a legal franchise over isolated grids, is shown standing on the evidence: it survived a
  fire that destroyed most of its owners' equity, and the State legislated and the PUC ruled to keep it standing (test
  10). It is not shown open, so not OUT; its future as a franchise can be judged, so not TOO HARD. What it protects is a
  regulated return, carried to Q3 as a second best; the unbounded liability is carried to Q9 **[L2005-019]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed.** The regulator's own measure, 2025 (10-K 0000354707-26-000008, page 51):
  return on rate base 7.61% (Hawaiian Electric), 6.65% (Hawaii Electric Light), 4.49% (Maui Electric) against allowed
  7.37%, 7.52%, 7.43%; rate-making ROACE 9.92%, 8.19%, 4.54% against 9.50%. Maui Electric's returns are "lower than
  allowed levels due to higher sustained maintenance and investments than what is recovered in current rates" (same
  page). The Utilities' Core return on average equity, the company's own adjusted figure, was 5.7% for the twelve months
  to June 30, 2026 against 7.2% a year earlier (8-K 0000354707-26-000053, page 10). The rows ask whether it has "earned
  high returns on capital" **[M1995-051]**; here the return is the regulator's, at or below what is allowed.
- **Reinvestment to stand still and to grow.** Capital spending, continuing operations, $301.5M (2021, estimated, see Q7),
  339.3, 442.7, 344.3, 341.2 (2022-2025) against depreciation of plant of 244.5 to 261.7 (2022-2025): spending runs 1.3
  to 1.7 times depreciation. After all capital spending, stock pay, preferred dividends and finance-lease principal, the
  owner cash left averaged about $4.5M a year over 2021-2025 (Q7): the business reinvests essentially everything it makes.
  "To earn more, their owners must invest more." **[L2011-019]**. The text expects the capital-heavy business to be a
  second best only on condition of "decent returns on the incremental sums they invest" **[L2009-012]**; "as the
  second-best choice, still a good choice" **[M2018-055]**.
- **The added capital of 2024.** The $557.7M of new equity raised in September 2024 (62.2 million shares; 10-K, MD&A)
  went to the first settlement installment, paid April 10, 2026 (10-Q 0000354707-26-000054, Note 2); capital put in that
  earns nothing for the owners. The three installments still due ($1.44B gross) will need more: HEI "expects to finance
  the settlement payments through a mix of debt, common equity, equity-linked securities or other potential options"
  (10-K Item 1A).
- **The growth arithmetic and its caps.** Volume is flat (Q2, test 5); rate-base growth from grid hardening and the
  transition is the only growth, and it earns at most the allowed return. Against the time row: "if you have a business
  that’s earning 5 or 6 percent on equity and you hold it for a long time, you are not going to do well in investing.
  Even if you buy it cheap to start with." **[M1998-006]**; Maui Electric and the trailing Core figure sit in that zone,
  Hawaiian Electric's rate-making figure does not.
- **WEIGHS AGAINST**: a capital-heavy business that consumes its operating cash in capital spending, earns at or below
  its allowed return, and has had to put in new equity that earns nothing, meets the second-best condition of a decent
  return on the added sums **[L2009-012]** only on its best island. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first** **[M2025-032]** (`tools/run.py` table, first-filed tagged values, accessions in
  `run_py_output.txt`; the 2025 and June 2026 columns read on the filed statements, 0000354707-26-000008 and
  0000354707-26-000054). $M:

| Year-end | Assets | Equity | Cash | Long-term debt | Retained earnings | Wildfire claims (liability) |
|---|---|---|---|---|---|---|
| 2017 | 13,100 | 2,097 | 262 | 1,684 | 477 | - |
| 2018 | 13,104 | 2,162 | 169 | 1,880 | 544 | - |
| 2019 | 13,745 | 2,280 | 197 | 1,964 | 622 | - |
| 2020 | 15,004 | 2,338 | 341 | 2,119 | 660 | - |
| 2021 | 15,823 | 2,391 | 306 | 2,322 | 758 | - |
| 2022 | 16,284 | 2,202 | 200 | 2,385 | 846 | - |
| 2023 | 17,244 | 2,345 | 680 | 2,842 | 927 | 75 accrued in the year |
| 2024 | 8,931 | 1,479 | 751 (incl. 492 restricted) | 2,690 | -789 | 1,840 accrued in the year |
| 2025 | 8,923 | 1,606 | 502 (+479 restricted) | 2,285 (+125 current) | -666 | 1,966 (530 current, 1,436 noncurrent) |
| Jun 2026 | 8,402 | 1,763 | 239 | 2,266 | -512 | 1,348 (458 current, 890 noncurrent) |

  What moved and why. **2017-2023**: the bank is inside every column (assets of $13-17 billion are mostly ASB's loans and
  securities); equity rose to 2021, then fell $189M in 2022 while retained earnings rose $88M, so the fall is outside
  retained earnings (other comprehensive income, in a year the bank's securities were marked; the arithmetic only, the
  2022 note not read for it). **2024**: assets halve as ASB is sold (90.1% for $405.5M, 9.9% kept at $44.6M; 10-K
  0000354707-25-000013); the fire accrual of $1.84B pre-tax and the bank loss swing retained earnings to -$789M; equity
  falls to $1,479M despite $556.6M of new stock. **2025**: the balance sheet carries the settlement as its largest
  liability after debt, $1.97B, against equity of $1.61B; finance-lease liabilities of $505.6M appear (storage PPAs).
  **June 2026**: the first $479M paid from the restricted cash; the remaining liability remeasured from $1.44B to
  $1.30B, which put a $154M pre-tax gain into the quarter. Long-term debt rose 69% from 2017 to 2023 and has been brought
  back since with the bank's proceeds; the goodwill of $82M was the bank's and left with it. "what the figures are saying
  and what they don’t say and what they can’t say" **[M2025-032]**: they say the Utilities' book is intact and the owners
  paid for the fire with about three-fifths of their pre-fire equity (2023 equity $2,345M; 2024 loss $1,424M) and a 57% increase in the share count (109.47 million
  shares at 2022 year-end to 172.73 million); they cannot say what a second fire would cost.
- **The real costs.** Depreciation is a real cost here and short of what is spent (Q3). Stock pay is small ($3.4M in
  2025) and is deducted. Wildfire legal and related costs ran through operating cash in 2023-2025 and continue; some
  non-labor costs from August 8, 2023 to December 31, 2025 were deferred as regulatory assets with PUC approval (10-K Item
  1A), so part of the cost of the fire sits on the balance sheet awaiting recovery. Pension: the trusts' assets exceeded
  the plans' obligations at December 31, 2025 (10-K, MD&A). EBITDA: not used in the filer's mouth in the documents read.
- **The tells.** The earnings release headlines GAAP first and then "Core" net income, a non-GAAP figure "which exclude
  Maui wildfire-related items" (8-K 0000354707-26-000053); a featured adjusted figure weighs against and is carried to
  Q5 **[L2016-006]**, while describing unusual items is what the same row asks for ("to describe unusual items � good or
  bad � that affect the GAAP numbers" **[L2016-006]**; the replacement character is the row's). The release also carries
  an "OUTLOOK AND GUIDANCE" section, on O&M, not on earnings per share; carried to Q5 **[L2019-006]**. The Q2 2026 gain
  arises from discounting a fixed contractual debt at the Utilities' own high incremental borrowing rate; the filing says
  the gain "will be offset over time by future interest accretion"; it is disclosed plainly and is excluded from owner
  cash (no cash moved). No reserves that move with a stock sale, no inventories out of line (fuel stock fell in 2023 and
  2024 and rose in 2025 with prices), no profits on both sides of a contract were found.
- **VERDICT on the accounts: no STOP (no confusion, no suspicion); WEIGHS AGAINST**, lightly: the featured Core figure
  and the guidance section are carried to Q5 **[M1994-018]**; the balance sheet shows the owners' capital consumed by
  the fire and the remaining liability ($1.30B discounted, $1.44B gross) close to the equity's market value ($1.51B).
  The recast owner cash feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet **[M2007-081]**; this file reads the 10-K, the 10-Q, the
proxy and the 8-Ks.
- **The two yardsticks** **[M1994-008]**. How well they run it, against "the hand they were dealt": the Utilities earn
  near the allowed return on Oahu and well below it on Maui (Q3); the fire of August 2023 happened on this management's
  watch (Scott Seu, HEI President and CEO; Shelee Kimura, Hawaiian Electric President and CEO; proxy
  0001104659-26-051288). Since then the record shows a negotiated global settlement with its conditions met and the
  first installment paid; the bank and Pacific Current sold under the divestiture strategy; credit facilities
  refinanced, a high-yield bond issued at the Utility and a tender for HEI debt (proxy, footnotes to the summary
  compensation table); three rating upgrades in 2025 (10-K page 40). How well they treat their owners: see Q6.
- **The tells of dishonesty, read.** A securities class action filed August 24, 2023 "broadly alleged that the
  defendants made materially false and misleading statements or omissions regarding our wildfire prevention and safety
  protocols and related matters" (10-K Note 2); it is settled for $47.8M, funded by directors and officers insurance,
  with "no admission of liability"; the derivative actions are settled for $100M paid by insurers, also without
  admission (same note). These are allegations resolved with insurers' money, not findings; no restatement, no
  regulator's finding of misstatement and no auditor change was found in the documents read. How they talk about
  mistakes **[L2024-003]**: the filings speak of the fire in the language of litigation ("without any admission of
  liability"; "The Company intends to vigorously defend itself in the litigation if a definitive settlement of all open
  litigation is ultimately not achieved"); no sentence was found in the documents read in which management says what it
  did wrong. That weighs against candour, read beside the posture any defendant in thousands of suits keeps; it is not
  proof of dishonesty. The habits carried from Q4: the Core figure is featured beside GAAP and reconciled; the guidance
  is about costs, not a promised earnings figure; no record of targets consistently reached was found **[L2002-041]**.
- **Integrity applied on doubt alone** **[M2013-088]**. The doubt was put: is there anything in the record that makes
  these people untrustworthy, "no matter how able" **[M2015-047]**? The documents show allegations settled without
  findings and plain disclosure of hard facts (the going-concern discussion, the dilution risk, no dividend "in the
  foreseeable future", the remeasurement gain explained). No fact found raises the doubt the row means; the absence of
  an admitted mistake is recorded against candour under ability, not as a doubt of honesty.
- **Love of the business.** Not testable from the documents for hired executives beyond the pay design (Q6, Part B).
- **VERDICT on integrity: IN** on the documents read (the integrity facts above are recorded for any later reader).
  **Ability WEIGHS AGAINST**, lightly: this business needs operating judgment in a wind event more than the speakers'
  great business needs management **[M1996-037]**, and the record includes the one event that cost the owners most of
  their equity; the recovery work since is real.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[M1998-110]**. Dividends paid: $148.6M (2021), $153.2M (2022), $74.0M (2023), none
  since the suspension in August 2023 (tagged 10-K data, 0000354707-26-000008). Book value per share fell from about
  $21.87 (2021 year-end: $2,391M over 109.31M shares) to about $10.21 (June 30, 2026: $1,763M over 172.73M shares). The
  earnings kept since 2023 went to the fire and to liquidity, not to value per share: the test fails over the span,
  though the cause is the liability and not a choice to reinvest badly. "The Company does not expect to pay any
  dividends on HEI Common Stock in the foreseeable future." (10-K Item 1A): stated plainly.
- **Buybacks.** None: the only purchases are open-market purchases "to satisfy the requirements of certain plans" (10-K
  Item 5; 10-Q Part II Item 2). No programme to test against the bottom of the Q7 range (line written back at Q7).
- **Issuance and deals.** 62.2 million shares sold in September 2024 for net proceeds of about $557.7M (about $8.97 a
  share; 10-K MD&A) to fund the first settlement installment, a 57% increase in the count. "We will issue common stock
  only when we receive as much in business value as we give." **[R1995-010]**: the cash received was spent on a
  liability, so the issue bought survival, not business value. More is likely: an automatic shelf (S-3ASR filed
  2026-01-23, `0001104659-26-006300`), the at-the-market programme named in the 10-K's liquidity discussion, and $1.44B
  still to pay. The row on companies "hell-bent on issuing shares" **[L2014-015]** does not fit a forced single issue; it
  is carried as the risk of the next three years. No all-stock acquisition (the narrower STOP does not arise). The bank
  was sold, 90.1% for $405.5M, at a recorded loss (10-K 0000354707-25-000013), under duress.
- **Part A WEIGHS AGAINST**: the money kept could not be used for the owners, the issue diluted them by more than half,
  and more issuance is the stated alternative for $1.44B of payments.
- **Part B, pay, board, owners.** In the proxy, "see how they treat themselves versus how they treat the shareholders"
  **[M1994-009]**: the CEO's total compensation was $5.39M (2023), $6.54M (2024) and $4.43M (2025), including in 2024 a
  cash annual incentive of $1.70M and a retention cash award of $0.27M, in the year the company lost $1.42B and sold 62.2
  million shares; retention cash awards were paid again in 2025 (proxy, summary compensation table and its footnote on
  the Bonus column). Two facts weigh the other way: the 2023-25 long-term plan paid nothing ("no payout under the
  2023-25 long-term incentive plan for all named executive officers"), and the CEO's 2025 annual award is payable in four
  installments, each "subject to forfeiture if the corresponding settlement payment expected in that year is not made"
  (proxy). Against that again: an award conditioned on paying a contractual debt rewards completing an obligation, and
  "you get what you reward for" **[M2016-083]**; pay tied to "what is actually under the reasonable control of the person
  that’s being measured" **[M2003-019]** is met for the financing, not for the fire. Say-on-pay passed with about 94% in
  2025 (proxy). The board plans a "corporate integration" in which the HEI and Hawaiian Electric boards "would be
  composed of a single set of individuals" (10-K Item 1), pending the PUC.
- **Part B WEIGHS AGAINST**, lightly: cash incentives and retention awards paid through the owners' worst years,
  partly offset by the zero long-term payout and the settlement-linked deferral.
- **Buyback line written back from Q7:** the bottom of the Q7 range is about $8.95 a share (equity-only, the no-growth
  case alone). No buyback was made in the window, so nothing is read against it.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate, as a range **[L2000-021]**. All figures $M unless per
share; the script and its output are `calc.py` and `calc_output.txt` in the research folder.

- **The basis.** The deciding part earns a return a regulator allows (Q2): "when you get an allowed return in the
  electric utility you’re almost certain of earning it" **[M2010-037]**, and the all-equity basis carries its own
  exception for "the fixed-asset commitments at our regulated utilities" **[L2017-012]**. So, by Q7's paragraph on the
  regulated utility, the **central figure is equity-only**: owner cash after interest and after the company's tax,
  against the market value of the shares, with the long-term debt raised over the window to fund the fixed assets
  credited against the capital spending it funded, up to the regulator's allowed debt share. The all-equity figure is
  beside it. Pacific Current's last asset (Mahipapa, held for sale, net liabilities of about $8.8M at June 30, 2026) is
  left out, said so.
- **Owner cash after every real cost, by year** (HEI continuing operations; OCF after interest and tax, less capital
  spending, stock pay, preferred dividends of subsidiaries and finance-lease principal; filings in Step 0):

| Year | OCF | Capex | Stock pay | Preferred | Lease principal | Owner cash, all capex |
|---|---|---|---|---|---|---|
| 2021 (estimate) | 252.2 | 301.5 | 6.6 | 1.9 | 0.0 | -57.8 |
| 2022 | 333.7 | 339.3 | 7.5 | 1.9 | 0.9 | -15.8 |
| 2023 | 443.4 | 442.7 | 6.8 | 1.9 | 3.5 | -11.5 |
| 2024 | 428.1 | 344.3 | 3.6 | 1.9 | 4.7 | 73.7 |
| 2025 | 391.1 | 341.2 | 3.4 | 1.9 | 10.4 | 34.2 |
| Five-year average | | | | | | **4.5** |

  **CONVENTION of this run (2021):** HEI did not file continuing-operations cash flows for 2021 (the bank was sold in
  2024 and the recast reaches back to 2022). 2021 is the Utilities' own filed OCF of $273.1M and capex of $292.0M (10-K
  0000354707-22-000049) plus the mean difference between HEI continuing and the Utilities in 2022-2024 (OCF -$21.0M,
  capex +$9.5M); stock pay scaled from the consolidated $9.13M by the 2022 continuing-to-consolidated ratio. Rationale:
  the Utilities are the whole business; the holding company's drag is the one piece not filed, and its own later
  average is the least invented figure. The 2022-2025 base, which needs no estimate, is shown beside.
- **The debt credit.** The Utilities' long-term debt rose from $1,561M (December 31, 2020; 10-K 0000354707-22-000049)
  to $2,183M (December 31, 2025; 10-K 0000354707-26-000008), $622M over the window. The filings read state the company's
  aim "to maintain the Utilities’ equity capitalization at approximately 58%" (10-K 0000354707-23-000032) but no
  regulator-allowed structure, so the cap is the business's own debt share at the latest filed date: Hawaiian Electric
  52% debt at June 30, 2026 (10-Q 0000354707-26-000054). 52% of window capex ($1,769M) is $920M, so the full $622M is
  credited: **$124.4M a year**. (HEI consolidated long-term debt rose only $291M over the same years, $2,119M to $2,410M,
  as the holding company repaid debt with the bank's proceeds; the Utilities' figure is the one the convention names and
  the more generous to the owner.)
- **Central owner cash, equity-only:** 4.5 + 124.4 = **$128.9M a year**. Beside it: the 2022-2025 base (no estimate;
  2021 is also the year the filer called down "due to the impact of the pandemic", 10-K 0000354707-22-000049),
  20.1 + 126.8 = $146.9M; the maintenance-only variant, capital spending at depreciation and no debt credit (the two may
  not both be taken, specific (e)), 2022-2025, $131.7M. The Utilities' own Core net income for the first half of 2026,
  $68.3M, and HEI's, $53.4M (8-K 0000354707-26-000053), are of the same order. Three ways to the number land within
  $18M of each other; the central figure is the lowest-estimate one and stands.
- **The settlement, priced separately.** Three installments of about $479M remain, due April 2027, 2028 and 2029 (10-Q
  Note 2); none is in the window's owner cash. **CONVENTION of this run:** each is taken as deductible when paid at the
  composite statutory rate of 25.75% stated in the 8-K (0000354707-26-000053, page 10), so $355.7M after tax each;
  discounted at the sovereign, **$990.2M**; at ten percent, $930.6M. Rationale: the accrual of 2024 carried a deferred
  tax benefit of $486M against the $1.84B charge (10-K cash-flow statement), which is that rate applied; the timing of
  deduction is assumed, not read. The cash and stake from the bank are added: $33.9M from the September 2026 IPO sale
  and the remaining shares at the IPO's net price (8-K 0000354707-26-000066: 2.0 million shares were 30% of the stake for
  $29.5M), about $64.5M; **$98.4M** in all, a subsequent event the filing states.
- **Growth shown.** The owner-cash series changes sign (negative 2021-2023, positive 2024-2025), and the halves give no
  meaningful rate (first half average -$36.8M, second half +$53.9M); by specific (b) **the range is the no-growth case
  alone**, said so. Volume is flat (Q2, test 5). A 2% case, at the business's revenue growth 2021-2025 ($2,850M to
  $3,087M, which includes fuel prices passed through), is shown beside for information, not as an end of the range.
  Zero growth is carried after year ten, the cap is not reached, no absurdity arises.

**COMPUTATION of the range, at the sovereign of 5.29%:**

| Case | Owner cash | Value of equity ($M) | Per share |
|---|---|---|---|
| Central: equity-only, five-year, no growth | 128.9 | 2,437 - 990 + 98 = 1,545 | **$8.95** |
| Beside: 2022-2025 base, no growth | 146.9 | 1,884 | $10.91 |
| Beside: maintenance-only, no growth | 131.7 | 1,598 | $9.25 |
| Beside, information only: central at 2% for ten years | 128.9 | 1,969 | $11.40 |
| Beside: all-equity (owner cash before after-tax interest; net debt at June 30, 2026: debt $2,266M + finance leases $499M - cash $239M - bank stake $98M, plus the settlement) | 108.3 | 2,047 - 2,428 - 990 | **-$7.94** |

- **The floor, tested first.** The expected return at $8.75 on the central case is owner cash over what is paid plus the
  settlement still owed: 128.9 / (1,511 + 990 - 98) = **5.37%** a year, against a floor of about ten percent **[M2003-149]**,
  and barely above the bond at 5.29%. The 2022-2025 base gives 6.11%; the maintenance variant 5.48%. For the central case
  to earn ten percent at this price, owner cash would have to grow about 8.6% a year for ten years, in a business whose
  volume is flat and whose return is capped by its regulator. **No case in the range, nor any beside it, earns the floor
  at the price.**
- **Value range:** **$8.95** a share (equity-only, the no-growth case alone; $10.91 on the 2022-2025 base beside;
  all-equity -$7.94 beside) against **$8.75**. **Closes: OUT**, because no case earns the floor at the price (tested
  first, 2026-10-10): "there’s just a point at which we drop out of the game" **[M2003-149]**. It would close OUT on the
  width rule as well: the price sits just below a one-case range, which is "too close to think about" **[M1996-084]**;
  "It should scream at you." **[M2009-005]**, and this does not.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and averaged; the
  range here is one case, so the fair price is that case at ten percent: 128.9 / 0.10 = 1,289 - 930.6 + 98.4 = 457 =
  **$2.65 a share, equity-only, central** (regulated-utility basis), after the company's own tax. Beside it: the
  all-equity figure, **-$13.18** (1,083 - 2,428 - 931). For information, with the 2% case taken as a second end the
  equity-only fair price would be $3.19; on the 2022-2025 base, $3.68. No cheap price is reported.
- **VERDICT: OUT** at Q7, on the floor: at $8.75 the business offers its owner about 5.4% a year on the price plus the
  settlement still owed, half the floor, with no growth that could close the gap **[M2003-149]**, **[M2007-095]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (facts found are under AFTER THE STOP).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (no named business of the rows: an electric utility is none of casinos, tobacco, loading schemes).

---
## THE BOX
**OUT**, decided at **Q7** on the floor: value range $8.95 a share (equity-only, the no-growth case alone; all-equity
-$7.94 beside) against a price of $8.75; expected return at the price about 5.4% a year against a floor of about ten
percent; fair price $2.65 equity-only (all-equity -$13.18). Q1 IN, Q2 IN (regulated return carried to Q3), Q3 against,
Q4 no STOP and against lightly, Q5 integrity IN with integrity facts recorded (securities and derivative suits settled by
insurers without admission), ability against lightly, Q6 against. Re-look condition: a price at which some case earns
the floor, or a filed liability cap under Act 258 together with the settlement financed without further issuance below
value.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2); each with its source **[M1997-127]**.)*
- **Q8, the bond.** The 30-year Treasury yields 5.29% (US Treasury, 2026-10-22); the central expected return at the price
  is 5.37% (Q7), with a capped return, an uncapped liability tail and below-investment-grade credit.
- **Q9, debt and exposures.** At June 30, 2026: long-term debt $2,265.6M (none current), finance-lease liabilities
  $499.4M, wildfire tort claims $1,347.8M on the balance sheet (current $457.6M, which includes the $47.8M securities
  settlement offset by an insurance receivable; noncurrent $890.3M), against equity of $1,762.9M and cash of $238.7M (10-Q
  0000354707-26-000054). Credit ratings below investment grade since August 2023, upgraded in 2025 (10-K pages 40 and Item
  1A: "Unless and until these debt ratings are upgraded to investment grade, the Company will continue to have restricted
  access to lower cost sources of capital."). Liquidity: HEI and Hawaiian Electric credit agreements of $300M each and an
  undrawn $250M asset-based facility (10-Q MD&A, Note 5). Interest cover, arithmetic only: HEI continuing pre-tax income
  plus interest over interest, 2025 (166.9 + 117.3) / 117.3 = about 2.4 times; 2023 about 2.5 times (10-K income
  statement and tagged interest expense). The 10-K says a larger loss "could result in violations of the financial
  covenants in the Company’s debt agreements" (Note 2). Concentration: one jurisdiction, five grids, one fire season;
  the rows on a single utility **[L2005-019]**. The $500M holdback for opt-outs is believed "sufficient" (10-Q Note 2);
  about 80 plaintiffs had not joined. The "little or no debt" criterion is stated for whole businesses only.
- **Q9, the financing still needed.** $1.44B gross in 2027-2029, to be financed "through a mix of debt, common equity,
  equity-linked securities or other potential options" (10-K Item 1A); the company "is currently working with its
  financial advisors on a financing plan" (10-Q MD&A). Securitization is authorized for mitigation costs under Act 258,
  not for the settlement, on the documents read.
- **Q10.** Nothing found.
- **Q12.** Nothing found bearing on the newspaper test beyond the fire itself.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 50362895); written question by question; committed after each
      question or pair (Q3 with Q4 and Q5 with Q6 were committed together, said so).
- [x] Dispatched: the brief allowed the per-question pathspec commits and the lock is held by the dispatching session;
      the fold into the register is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; one directory listing of
      `Test Runs/` showed other runs' file names, declared under contamination at the top and not used.
- [x] Every v5 id resolves (`check_ids.py` in the research folder: no E-ids, every M/L/R id in the CSV, every quoted
      fragment directly before an id found in that row); every filing fact has its accession; numbers of ours are
      labelled CONVENTION (the 2021 estimate, the settlement's tax timing, the comparators).
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (the Core figures are shown only as a check); the
      sovereign from the issuing authority (US Treasury); the price an aggregator quote, flagged.
- [x] Contrary evidence written down as it was found (Foundations, Q2, Q5); facts for later questions under AFTER THE
      STOP; integrity facts recorded in Q5 and named in the box line.
- [x] Not a point-in-time run; no anchor (the rows cited are all dated before today).
- [x] Only the arithmetic lines of `tools/run.py` were used, and its consolidated OCF for 2023-2024 was replaced by the
      filed continuing-operations lines (Step 0).
- [x] `python tools/check_framework.py` PASS before the final commit (run 2026-10-23: "PASS — every number resolves to a verbatim source or a confessed convention"; `check_ids.py`: 52 ids, 0 faults).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The regulated-utility debt credit does not say whose debt.** For a holding company over a utility, "the long-term
debt raised over the window to fund the fixed assets" can be the utility's own ($622M here) or the consolidated
figure ($291M, because the holding company repaid debt with sale proceeds); the run took the utility's as the one that
funds fixed assets and showed the other; the choice moves the central owner cash by about $66M a year. (2) **The
regulator's allowed debt share** is often not stated in the filing; the fallback (the business's own share at the latest
date) here takes a post-fire, distressed structure (52% debt, against 41-42% before the fire), which raises the credit;
a rule could name the pre-event structure. (3) **A fixed liability outside the window** (a settlement payable in
installments) has no stated place on the equity-only basis: the all-equity basis subtracts net debt, the equity-only
basis subtracts nothing; the run subtracted its after-tax present value, which is the only reading that does not count
the owners free of a debt they must pay, and confessed the tax timing. (4) **Specific (b) leaves a one-case range** when
the series changes sign, so the width test and the "two ends averaged" fair price have one end; the run used the one
case and showed a 2% case beside, labelled information. (5) **Discontinued operations break the five-year window**:
when a filer recasts only three years, the fifth year must be estimated; the framework has no rule, and the run
confessed one. (6) The template's Q6 buyback write-back assumes a programme exists; for a company with none the line is
empty, and the run wrote that.
