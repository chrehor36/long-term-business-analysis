# Company Run — American States Water Company (NYSE: AWR) — 2026-10-28
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-28: the operator does not hold this name (`PORTFOLIO.md` has no AWR row).*

**Dispatched run.** Brief of 2026-10-28 (canonical brief `Screens/_daily/_dispatch_brief.md`, with two departures the brief
states: the repository path is `C:\Projects\BRK`, and the lines of evidence are derived by the analyst from the 10-K, not
written by the dispatcher). Working folder `Test Runs/_research 2026-10-28 AWR/`; raw filings in its `cache/` (gitignored).

**Contamination, declared and not used.** (1) The git status and recent commit subjects shown at session start name a v5 run
of another company in the same industry dated today, with its box, deciding question and a range against a price. I did not
open that file and use nothing from it; because I saw its subject line, I did not choose that company as a Q2 comparator
(see Q2, the competitor row). (2) The memory index loaded at session start carries general lines about the queue and holdings
(counts, no names relevant to this company) and the line "owed: five holding reviews under v5". Nothing in it names AWR; not
used. No other run, holding review, `PORTFOLIO.md` or blind-listed file was opened, listed or searched.

**The lines of evidence, chosen by the analyst from the FY2025 10-K** (accession 0001628280-26-009114), as the brief's second
departure requires: from **Item 1**: the three segments (water: GSWC, CPUC-regulated, 265,142 customers; electric: BVES,
CPUC-regulated, 24,915 customers; contracted services: ASUS, U.S. military bases under 50-year firm-fixed-price contracts),
the competition paragraph (territories "substantially free from direct and indirect competition", subject to condemnation),
and the seasonality paragraph (the loss of full revenue decoupling, WRAM and MCBA, from 2025). From **Item 1A**: regulatory
risk and rate-case delay; condemnation; wildfire and strict liability at BVES; water supply, drought and conservation;
groundwater contamination (PFAS, hexavalent chromium); geographic concentration in California; the firm-fixed-price and
appropriations risk at ASUS; the need for external capital. From **Item 7**: the 2025-2027 water rate case and 2023-2026
electric rate case decisions; the cost of capital (7.93% on rate base, 10.06% return on equity, 57% equity and 43% debt,
deferred to 2028); segment results; the ATM equity program; the debt issues; capital spending against depreciation; the
dividend policy; the cash-flow drivers (the 2023 rate-case delay and the 2025 surcharge recovery). The span read is FY2021
to FY2025 (10-Ks for FY2020 to FY2025) and the 10-Q to 2026-06-30, with the balance sheets from FY2017.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $85.48 (close 2026-10-27; Yahoo Finance chart endpoint via `tools/sources.py`/`tools/run.py`; **aggregator, a
  live quote only, flagged per operator rule 5**).
- **Shares by class** from the latest filing's cover: 39,635,626 common shares, no par, as of 2026-08-04 (10-Q for the
  quarter ended 2026-06-30, filed 2026-08-05, accession 0001628280-26-053401; `python Screens/cover_shares.py AWR`). The
  tool's second line, 178 shares, is Golden State Water Company's own common stock, all held by AWR (the 10-Q balance sheet
  of GSWC: "Outstanding: 178.3836 shares in 2026 and 178.3836 in 2025"); the filing is a combined report of two registrants,
  so this is not a second class of AWR and is not added. Cross-check: the 10-Q consolidated balance sheet shows 39,635,452
  shares outstanding at 2026-06-30; the difference to the cover (174 shares) is stock-plan issuance. AWR reports no
  treasury shares (no par common, "Outstanding" only). After the 10-Q: the ATM program reached its $200 million limit on
  2026-06-12 and "No further sales of Common Shares will be made under this program" (10-Q, same accession); no 8-K or
  prospectus after the 10-Q issuing shares was found in the EDGAR filing list (8-Ks after 2026-08-05: none listed).
- **Market cap:** 39.636M x $85.48 = **$3,388M**.
- **Sovereign for the earnings currency (USD):** **5.30%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-27 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-18, accession 0001628280-26-009114); 10-Ks FY2024
  (0001628280-25-006389), FY2023 (0001628280-24-005922), FY2022 (0001628280-23-005869), FY2021 (0001056903-22-000022),
  FY2020 (0001056903-21-000021); 10-Q for 2026-06-30 (0001628280-26-053401); proxy DEF 14A filed 2026-04-03
  (0001140361-26-013117); 8-Ks of 2026-02-20 (ATM amendment, 0001104659-26-018151), 2025-11-19 (cost of capital deferral,
  0001628280-25-053202), 2025-06-03 (GSWC notes, 0001056903-25-000014), 2026-08-05 (results, 0001628280-26-053403).
  **One figure cross-checked against the filed statement:** operating cash flow FY2025, `tools/run.py` (XBRL) 229.7M against
  the filed Consolidated Statement of Cash Flows, "Net cash provided (used) | 229,730" (10-K FY2025): agrees. Capital
  expenditures FY2025: XBRL 236.8M, filed "Capital expenditures | ( 236,822 )": agrees.
- `python tools/run.py AWR`, arithmetic lines only (Part VII; its v4 floor, ids and "OE" labels not used): saved in
  `Test Runs/_research 2026-10-28 AWR/run_py_output.txt`. Its debt table tags "CapitalizationLongtermDebtAndEquity" as debt
  (d2), which is debt plus equity on the filed statement of capitalization; that column is wrong as debt and is not used. Its
  balance-sheet table is used for Q4 after checking against the filed statements. The five-year figures used below are taken
  from the filed cash-flow statements (FY2025 10-K for 2023 to 2025; FY2022 10-K for 2021 and 2022), in USD millions:

| FY | Operating cash flow | Stock pay | Capital spending | D&A (cash-flow line) | Developer advances and contributions, net of refunds | Other investing, net |
|---|---|---|---|---|---|---|
| 2021 | 115.584 | 2.566 | 144.515 | 39.974 | 7.766 | -0.577 |
| 2022 | 117.799 | 2.571 | 166.240 | 41.697 | 1.580 | -0.862 |
| 2023 | 67.683 | 3.298 | 188.540 | 43.254 | 7.349 | -0.224 |
| 2024 | 198.732 | 3.744 | 231.960 | 44.226 | 6.276 | -0.820 |
| 2025 | 229.730 | 3.559 | 236.822 | 48.873 | 8.148 | -0.719 |

  Interest paid, net of capitalized interest (supplemental cash data): 22.540 (2021), 26.005 (2022), 39.367 (2023), 50.347
  (2024), 46.050 (2025) (FY2022 and FY2025 10-Ks).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this if the market closed for years **[M1997-109]**,
and what decides it is "the prospects of the businesses" **[M1998-099]**. The margin of safety is an attitude here and an
arithmetic only at Q7 **[M1997-126]**. No macro forecast enters: the long rate is used as the yardstick, not forecast
**[M2000-094]**. Who is paid to tell you: a utility that sells shares through sales agents (the ATM program) has a reason to
want its stock well priced, and the dividend-growth policy is a message to buyers of the stock; both are read at Q5 and Q6
**[M2020-037]**. **Contrary evidence, written down as found** **[M1997-127]**: (i) the 2025-2027 water rate case took away the
full revenue decoupling (WRAM) and full supply-cost balancing (MCBA) GSWC had since 2008, so the regulator moved volume and
supply-mix risk onto the owners (10-K FY2025, Item 1, Seasonality); (ii) capital spending ran 3.6 to 5.2 times depreciation
in every year of the window, and the company sold 2,575,947 new shares through the ATM in 2024 to 2026 to fund it (10-K
FY2025; 10-Q 2026-06-30); (iii) BVES distributes power in a high wildfire risk area in California, where a utility can be
held strictly liable (inverse condemnation) without negligence (10-K FY2025, Item 1A); (iv) the 2023 operating cash flow
fell to $67.7M when the water rate case decision was delayed and regulatory assets built by $81.4M (FY2025 cash-flow
statement).

## THE STANDING RULE
The buyer's own conduct: a purchase of common stock with cash, no borrowing and no position size that can call, puts the
buyer at no risk of ruin; "always be sure you can play the next day" **[M2025-015]**; borrowed money to own stocks is ruled out
**[L2014-005]**. Nothing about this name changes that; the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, of the economics, not the product **[M2000-104]**. The parts (Q1, A holding company,
  and Q2's threshold): five-year segment operating income FY2021 to FY2025 (Note 17 of the FY2023 and FY2025 10-Ks):
  water $661.1M (77.6%), electric $60.1M (7.1%), contracted services $130.7M (15.3%), of a $851.9M total. **Water decides**
  (more than half). Electric and contracted services do not decide.
- **The key variables** **[M1998-044]**, for the deciding part: (1) rate base, which grows with the capital spending the CPUC
  authorizes ($573.1M authorized over 2025-2027 in the final decision of 2025-01-30); (2) the allowed return (7.93% on rate
  base, return on equity 10.06%, 57% equity, set for 2022-2024 and extended to 2027 under the cost of capital deferral of
  2025-11-19, 8-K 0001628280-25-053202); (3) regulatory lag and mechanism (rate-case delays, the loss of WRAM and MCBA); (4)
  water supply and quality costs, largely passed through. Each is set in public proceedings and reported in the filings, so
  the statements do tell me what future statements will look like **[M2008-033]**: earning power is roughly allowed equity
  return times equity rate base, and the equity rate base grows with authorized capital. That is foreseeable for ten years in
  the way the insiders themselves write it down (the company files three-year capital budgets and cost-of-capital requests),
  which is the opposite of the "too hard" forecast **[M2000-105]**.
- **What could put it beyond the horizon.** Not technology: water distribution has no fast-moving technology **[L1993-023]**.
  The uncertainty is regulatory and climatic (drought, contamination, wildfire at BVES), which are the castle's threats (Q2)
  and the ruin question (Q9), not a failure to understand the business. Contracted services (15%) is understood too: cost-plus
  style economic price adjustments on 50-year contracts plus construction work (10-K FY2025, Item 1). Electric (7%) carries the
  wildfire risk I understand only as a tail, but it does not matter under the parts threshold.
- Routing: no fast-changing industry; not a financial institution; a holding company read by its parts, and the deciding
  part is understood. Doubt test **[M2002-092]**: I do not doubt that I can say where GSWC's earning power will be in ten years
  within a range, which is what the definition asks **[M2000-037]**.
- **VERDICT: IN.** The deciding part is a regulated water utility whose earning power is set by rate base and an allowed
  return, both on the public record **[M2012-065]**, **[M2008-033]**, **[M1995-051]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (Q2, A business of parts; five-year segment operating income FY2021 to FY2025, USD millions, Note 17 of
the FY2023 10-K, accession 0001628280-24-005922, for 2021 and 2022, and of the FY2025 10-K, 0001628280-26-009114, for 2023
to 2025):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year | Share | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Water (GSWC) | 107.6 | 92.5 | 159.2 | 143.5 | 158.4 | 661.1 | 77.6% | regulated franchise, CPUC | **yes** |
| Electric (BVES) | 10.7 | 11.7 | 11.2 | 12.2 | 14.3 | 60.2 | 7.1% | regulated franchise, CPUC, wildfire area | no |
| Contracted services (ASUS) | 22.7 | 22.4 | 26.2 | 28.8 | 30.6 | 130.7 | 15.3% | 50-year military contracts | no |

**The castle tests, on the deciding part (water):**
- *Why is it still standing* **[M1995-038]**: GSWC serves certificated territories in eleven California counties, and "The
  businesses of GSWC and BVES are substantially free from direct and indirect competition with other public utilities,
  municipalities and other public agencies within their existing service territories" (10-K FY2025, Item 1, Competition).
  The customer comes because there is one pipe to the house, and water is "something that’s essential to people"
  **[M2004-091]**. That reason will not change in twenty years.
- *The money test* **[M2011-015]**, **[M1997-103]**: an attacker with money cannot duplicate a regulated distribution network
  in a certificated territory. The castle stands against the money test.
- *Would it stand without the lord* **[M1995-038]**, **[M2008-045]**: yes; the return is a function of rate base and the
  allowed return, not of a superstar.
- *Pricing power, and the agony before a rise* **[M2005-020]**: here the castle is not of the speakers' great kind. GSWC
  cannot raise a price on its own: every rise is a general rate case before the CPUC, settled or litigated with the Public
  Advocates Office. The 2022-2024 case was decided late, in 2023, and that year operating cash fell to $67.7M while regulatory
  assets built by $81.4M (FY2025 cash-flow statement); the 2025-2027 decision removed the WRAM and MCBA held since 2008 (10-K
  FY2025, Item 7, Overview). The rate case is the prayer session in institutional form. What the moat protects is not a price
  but an allowed return on invested capital.
- *Low bid, brand, share of mind* **[M2017-009]**, **[M2008-075]**: not applicable; the customer has no choice.
- *Widening or narrowing* **[M1999-108]**, **[L2005-010]**: in the window the regulator narrowed the protection (without the
  WRAM and MCBA, "Registrant may be subject to future volatility in revenues and earnings as a result of fluctuations in
  water consumption by our customers and changes in water supply cost mix", 10-K FY2025, Item 1), while the 10.06% allowed
  return on equity was kept through 2027 by the deferral approved in November 2025 (8-K 0001628280-25-053202). Mixed; on
  balance slightly narrower.
- *What could destroy, modify or reduce it* **[M2000-014]**: (i) condemnation, "Our assets at our regulated utilities are
  subject to condemnation" (Item 1A), compensated at fair value, so a change in the owner's position more than a destruction;
  (ii) the regulatory compact itself, "the regulatory climate in a few states has raised the specter of zero profitability
  or even bankruptcy (an actual outcome at California's largest utility" **[L2023-011]**, said of electric utilities and
  wildfire, the risk that lives in BVES (7% of operating income), not in the deciding part; (iii) drought, supply cost and
  contamination (PFAS, hexavalent chromium), which the CPUC has so far let GSWC track in memorandum accounts for recovery
  (Item 7, Environmental Matters), a dependence on the regulator again; (iv) conservation and lower use per customer, which
  now reach earnings through the M-WRAM's partial decoupling.
- *Ask the competitors* **[M1999-130]**: not possible from the public record; the comparators' filings are used instead.

**The competitor row.** The 10-K names no rival (Item 1, Competition, names only "governmental agencies and other
investor-owned utilities" for new developments and, for ASUS, other utilities, third-party providers and governmental
entities). **CONVENTION of this run:** I chose three listed water utilities that file with the SEC: California Water Service
Group (CWT) and H2O America (formerly SJW Group, HTO), the two other CPUC-regulated investor-owned water utilities of size,
and Essential Utilities (WTRG), a multi-state water and gas utility. Rationale: the 10-K names none; the two California filers
face the same regulator, and one filer outside California shows whether the California result is the regulator's. I did not
choose American Water Works, the largest listed water utility, because a run of that company dated today was visible in the
commit subjects at session start (contamination, declared above). Metric: net income over average shareholders' equity,
FY2016 to FY2025, from each filer's own XBRL facts as first filed in its 10-Ks (script and output
`Test Runs/_research 2026-10-28 AWR/roe.py`; the accession named is the latest 10-K, earlier years from the earlier 10-Ks):

| Filer | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Ten-year mean |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AWR (0001628280-26-009114) | 12.4% | 13.5% | 11.7% | 14.5% | 13.9% | 14.2% | 11.2% | 16.8% | 14.0% | 13.2% | 13.5% |
| CWT (0001628280-26-012444) | 7.5% | 10.8% | 9.2% | 8.4% | 11.4% | 9.6% | 7.7% | 3.8% | 12.4% | 7.7% | 8.9% |
| HTO, ex-SJW (0001628280-26-012438) | 13.1% | 13.4% | 5.7% | 2.6% | 6.8% | 6.2% | 6.9% | 7.3% | 7.2% | 7.1% | 7.6% |
| WTRG (0000078128-26-000050) | 13.1% | 12.6% | 9.7% | 7.6% | 6.7% | 8.7% | 8.8% | 8.8% | 9.8% | 9.4% | 9.5% |

(HTO's 2018 and 2019 are depressed by its 2019 merger, WTRG's 2020 by its gas acquisition, CWT's 2023 by its own delayed rate
case; CWT's equity from 2021 includes non-controlling interests, the tag it filed.) AWR earned more on its equity than each
comparator in at least eight of the ten years, over the whole span, and above its own allowed 10.06%. Part of the margin is
ASUS, which earned $23.5M in 2025 (segment net income, Note 17) on contracts that need little of its own capital; the water
segment alone earned $100.9M in 2025 on GSWC's average equity of $869.8M ($933.7M and $805.8M, GSWC statements of
capitalization), about 11.6%, including $5.5M of gains on a retirement-plan trust.

**The field's returns over the last full cycle, judged in words.** The field earns what its regulators allow, about the
allowed equity return and in two of the three comparators less, never the "excellent returns" a moat protects in the
speakers' sense **[L2007-004]**. Q2's list sends a standing castle that protects only ordinary returns to OUT, but "A return
set by a regulator is the exception, carried to Q3 as a second best" (Q2, What it rules OUT), on **[M2009-104]** and
**[L2009-012]**. This is that case: "there’s no way we get rich on our utility investments. But there’s no way we get poor,
either." **[M2009-104]**

**The regulatory climate.** The tension the framework carries OPEN, that the regulatory compact can break **[L2023-011]**,
**[M2024-011]**, is live in California, and the 2025 rate case moved risk onto the owner. But the evidence of the window is a
regulator that removed a mechanism, not one that cut the allowed return or disallowed the capital: it authorized $573.1M of
capital for 2025-2027 and kept the 10.06% through 2027. A castle under pressure, not one shown open; and its future can be
judged within a range from the filed proceedings, so I do not send it to TOO HARD.

- **VERDICT: IN.** The deciding part's castle is a regulated monopoly franchise that the money test cannot cross **[M2011-015]**;
  its returns are set by a regulator, which Q2 sends to Q3 as a second best rather than OUT **[M2009-104]**, **[L2009-012]**;
  the regulatory climate **[L2023-011]** is carried to Q7's certainty and to Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital needed** **[M2010-090]**, **[M2011-060]**: FY2025 operating income $203.3M, after tax at the year's
  effective rate (23.2% = $39.4M / $169.8M) about $156.1M, on capital employed of $1,962.1M (equity $1,045.6M, long-term
  debt including current maturities $794.3M, bank notes $141.0M, less cash $18.8M): about 8.0%. On equity, 13.2% (Q2 table).
- **The added capital** **[M2001-019]**, **[M2014-086]**: from FY2020 to FY2025 capital employed rose from $1,183.5M (equity
  $641.7M, long-term debt $444.3M, bank notes $134.2M, less cash $36.7M; FY2020 10-K, 0001056903-21-000021) to $1,962.1M, an
  increase of $778.6M; operating income rose from $130.5M to $203.3M, $72.8M pre-tax, about $55.9M after tax at 23.2%: about
  7.2% on the added capital, measured as the row says, by "the operating earnings after depreciation" **[M2014-086]**. On
  the added equity ($403.9M, of which $155.7M was new shares through the ATM), net income rose $44.3M ($86.1M to $130.4M),
  about 11%. Decent returns on the incremental sums **[L2009-012]**, about what the regulator allows and no more.
- **How much to stand still, and how much to grow** **[L1999-024]**, **[M2000-144]**: capital spending was $968.1M over the
  five years against depreciation of $218.0M, 4.4 times; the company says capital spending "in future years at GSWC and BVES
  are expected to remain at substantially higher levels than depreciation expense" (10-K FY2025, Item 7). Customers grew 0.2%
  in 2025 (290,057 against 289,414), so the spending above depreciation buys rate base, not volume. Operating cash never
  covered capital spending plus the dividend in any year of the window; the gap was met by debt and, from 2024, by 2,575,947
  new shares. "To earn more, their owners must invest more." **[L2011-019]** The spending is close to compulsory: the
  regulator authorizes it and the renewal programs require it **[M1997-016]**.
- **The growth arithmetic and its cap** **[M1999-067]**: earnings grow with rate base at about the allowed return; there is no
  route to returns above that on the regulated 85% of operating income. ASUS earns more on little capital but is 15%.
- **WEIGHS FOR, as a second best, weakly.** The added capital earns a decent return, about the allowed return **[L2009-012]**,
  **[M2014-086]**, **[M2018-055]**; against it, the owner must keep adding capital to earn more and never receives the
  reported earnings as free cash **[L2011-019]**, **[L2023-009]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first** **[M2025-032]**, year-ends FY2017 to FY2025, USD millions (`tools/run.py` table of first-filed
XBRL values, checked against the filed FY2025 and FY2020 balance sheets and statements of capitalization: 2025 assets
$2,715.1M, equity $1,045.6M, cash $18.8M, long-term debt $782.7M agree; long-term debt gross of current maturities and issue
costs from the statements of capitalization; the 2017 cash figure is untagged in XBRL and shown as the tool printed it):

| Year-end | Assets | Equity | Cash | Customer receivables | Goodwill | Long-term debt (gross, statement of capitalization) | Bank notes | Retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2017 | 1,417 | 530 | n/a | 26 | 1 | 321 (net, tool) | 59 | 280 |
| 2018 | 1,501 | 558 | 7 | 23 | 1 | 281 (net, tool) | 96 | 305 |
| 2019 | 1,641 | 602 | 1 | 21 | 1 | 284.7 | 205 | 346 |
| 2020 | 1,792 | 642 | 37 | 29 | 1 | 444.3 | 134.2 | 385 |
| 2021 | 1,901 | 686 | 5 | 34 | 1 | 415.8 | 205 | 428 |
| 2022 | 2,034 | 710 | 6 | 26 | 1 | 450.4 | 278 | 449 |
| 2023 | 2,246 | 776 | 14 | 34 | 1 | 579.0 | 334 | 513 |
| 2024 | 2,500 | 920 | 27 | 38 | 0 | 643.9 | 289 | 565 |
| 2025 | 2,715 | 1,046 | 19 | 38 | 0 | 794.3 | 141 | 620 |

(Bank notes: the tool's notes-payable lines d1 plus d4, checked for 2024 and 2025 against the filed balance sheet, $124.0M
current plus $165.0M non-current in 2024 and $141.0M non-current in 2025. At 2026-06-30: long-term debt $717.7M plus current
$73.2M, bank notes $119.0M, cash $21.7M, equity $1,121.5M; 10-Q 0001628280-26-053401.)

**What moved, and why.** Assets nearly doubled in eight years, almost all of it utility plant; equity doubled ($530M to
$1,046M), from retained earnings ($280M to $620M) and, in 2024 to 2026, new shares; goodwill and intangibles are nil, so
nothing was bought and nothing is carried on a purchase price. Debt rose faster than equity in 2019 to 2023 (bank notes peaked
at $334M in 2023, during the rate-case delay) and was then termed out and partly replaced by equity (bank notes $141M in 2025,
$119M in June 2026). Customer receivables moved with revenue ($26M to $38M against revenue of $440.6M in 2017 and $658.1M in 2025). The one
line out of proportion is ASUS's: receivable from the U.S. government $46.4M current plus $27.7M non-current, and contract
assets $31.5M, together about $106M against contracted-services revenue of $136.7M in 2025 (10-K FY2025 balance sheet). The
filing ties it to price adjustments and equitable-adjustment requests pending with the government and to construction billed
on milestones (Item 1A and Item 7). It is a tell to watch **[M1995-064]**, not one that confuses: it is explained by the
contracts, and it is 15% of the business. Regulatory assets built during the late rate case (cash-flow line: $(18.9)M in
2022, $(81.4)M in 2023) and came back as surcharges ($18.5M in 2024, $46.1M in 2025), as the filer describes. What the figures
"can’t say" **[M2025-032]**: whether the CPUC will keep allowing recovery of the next under-collection, which is a regulatory
judgment, not an accounting one.

**The real costs.**
- *Depreciation* **[R1996-023]**, **[L2015-004]**: $48.9M in 2025 against capital spending of $236.8M. For a utility whose
  assets last fifty years or more and whose spending is mostly renewal, depreciation at historical cost understates what it
  costs to stay in place; the filer itself says renewal is a large part of the spending ("infrastructure renewal programs (to
  replace infrastructure, including those to mitigate wildfire risk) and major capital investment projects", 10-K FY2025,
  Item 7). The owner-cash figure below therefore deducts all capital spending, with the depreciation (maintenance) variant
  beside it, as Q7 requires.
- *Stock pay* **[L2015-003]**, **[L2021-003]**: $2.6M to $3.7M a year (restricted stock units including performance awards,
  Note on share-based compensation), about 3% of net income; deducted.
- *Restructuring and special charges* **[L2016-007]**: none in the window.
- *Pensions* **[M2003-110]**: a defined benefit plan closed to hires after 2010; the expected return assumption is 6.00%; the
  cost is recovered in rates and the funded status is carried against regulatory accounts; "contribution to its pension plan
  in 2026 is not expected to be significant given its current funded status" (Item 8). Not a tell.
- *Taxes* **[M2015-030]**: deferred income taxes of $194.1M are not treated as hidden equity; owner cash is after cash taxes.
- *Non-recurring cash in the window*: $14.7M of PFAS class-action proceeds received in 2025 and $3.5M of COVID relief funds in
  2024 (10-K FY2025, Item 7, GSWC cash flows). Small; left in the average and said so.
- *EBITDA* **[M1998-086]**: used only as defined in a debt covenant (indebtedness to EBITDA below 8 to 1; GSWC at 3.4); never
  presented as earnings. No tell.

**The habits carried to Q5 (a weighing here, judged there; Q4, The make-the-numbers habit).** (1) An adjusted figure
featured: each year's MD&A leads with "diluted earnings per share, as adjusted (Non-GAAP)", reconciled to GAAP. The
adjustments cut both ways (2024 removed a $5.0M tax benefit; 2023 removed retroactive revenue and trust gains and losses),
but the 2024 removal makes the 2025 increase read $0.33 adjusted against $0.20 recorded **[L2016-006]**. (2) Earnings
guidance: "The contracted services segment is expected to contribute $0.63 to $0.67 per share for the full year of 2026"
(10-Q 0001628280-26-053401) **[L2019-006]**. (3) A stated dividend-growth target: "AWR’s current policy is to achieve a CAGR
in the dividend of more than 7% over the long-term" (10-K FY2025, Item 7), carried to Q6.

**The recast earnings that feed Q7** (owner cash after every real cost, operator rule 5; USD millions):

| FY | Owner cash, all spending deducted (OCF less stock pay less capital spending, plus net developer funds and other investing) | Owner cash after maintenance only (depreciation as the maintenance guess) |
|---|---|---|
| 2021 | -24.3 | 80.2 |
| 2022 | -50.3 | 74.2 |
| 2023 | -117.0 | 28.3 |
| 2024 | -31.5 | 156.2 |
| 2025 | -3.2 | 184.7 |
| Five-year mean | -45.3 | 104.7 |

(These are after interest and after the company's tax: the equity-only basis.)

- **VERDICT on the accounts: IN (no confusion, no suspicion); WEIGHS slightly AGAINST** on the featured adjusted figure and the
  segment guidance, both carried to Q5 **[L2016-006]**, **[L2019-006]**, **[M1994-018]**. The accounts are clear and the
  management explains the movements in plain terms **[M1994-018]**; regulatory accounting is complex but readable from the
  notes, and nothing in the statements raises the tells that close the file **[M1995-063]**, **[M1995-065]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Robert J. Sprowls, President and Chief Executive Officer since 2009 and chief financial officer for more than four
  years before that; the board has nine directors, all independent except him, with an independent chair (proxy DEF 14A,
  0001140361-26-013117). He owned 204,955 shares at the record date, about $17.5M at $85.48, about eighteen times his 2025
  salary of $974,327 (the guideline is five times); hedging and pledging are prohibited and "No officer or director has
  pledged shares since the policy was implemented" (proxy).
- **The first yardstick, the record against the hand dealt** **[M1994-008]**: the hand is the same CPUC that regulates CWT and
  HTO; over FY2016 to FY2025 AWR earned 13.5% on its equity on average against 8.9% and 7.6% for those two (Q2 table), never
  below 11.2% in a year, through a rate-case delay (2022-2023) and the loss of decoupling (2025). ASUS, built over two decades
  into ten military-base contracts (10-K FY2025, Item 1), adds earnings on little of the company's capital. That is ability
  shown in a long record, not a promise **[M1996-038]**, **[M2005-039]**.
- **The second yardstick, how they treat the owners** **[M1994-009]**: total 2025 pay for the chief executive was $5,028,665
  (summary compensation table, proxy), for a company earning $130.4M; the short-term plan pays 80% on objective criteria
  (adjusted EPS against the board-approved budget, by unit) plus a discretionary bonus ($312,000 to the chief executive in
  2025); performance shares vest on relative total shareholder return against water utilities and on GSWC operating-expense
  and ASUS cumulative-earnings goals. Read at Q6, Part B.
- **The tells of dishonesty** **[M2003-029]**, **[M1995-111]**, **[M2007-082]**: none found. The 10-K tells the bad news in
  plain terms (the CPUC "rejected GSWC’s request for the continuation of a full sales and revenue decoupling mechanism",
  "GSWC’s future earnings will continue to be subject to volatility", 10-K FY2025, Item 7), names the dilution its own share
  sales cause in each segment's earnings ("a decrease in earnings of approximately $0.07 per share due to the dilutive
  effects from the issuance of equity under AWR’s ATM offering program"), and reports the industry's key figures (rate base
  inputs, authorized capital, cost of capital) where an owner would want them **[M1998-036]**. No restatement, no material
  weakness; internal control effective (Item 9A); legal proceedings are routine and the company is a plaintiff, not a
  defendant, in the PFAS litigation (Item 3).
- **The habits carried from Q4** (an adjusted EPS featured, segment guidance, a dividend-growth target), read with the
  integrity record **[M2004-067]**: they are a utility's conventional investor-relations practice, reconciled to GAAP and
  adjusted in both directions; the adjusted EPS is also the bonus measure, so the adjustment matters to pay. They weigh
  against at Q6 Part B; they do not raise a doubt about honesty **[M2013-088]**.
- **Love of the business** **[M2000-098]**: not testable from outside for a hired executive beyond tenure and ownership; a
  seventeen-year chief executive holding eighteen times salary in shares is consistent with it.
- **VERDICT on integrity: IN** (no tell found, bad news told plainly) **[M2013-088]**, **[M1998-036]**; **ability WEIGHS FOR**
  (the record against the same regulator's other companies) **[M1994-008]**, **[M2005-039]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**: from 2020-12-31 to 2026-06-30 retained earnings rose $269.0M ($385.0M
  to $654.0M; FY2020 10-K and 10-Q 0001628280-26-053401) and owners put in $195.8M net through the ATM (net $88.7M in 2024,
  $67.0M in 2025 and $40.1M in the first half of 2026; the program's $200M gross was completed 2026-06-12). Market value moved
  from $2,933M at 2020-12-31 (36,889,103 shares at $79.51, aggregator close, flagged) to $3,388M at 2026-10-27, a rise of
  about $455M against about $465M retained and contributed: roughly a dollar of market value for each dollar kept, no more.
  On the intrinsic leg **[R2009-002]**, the dollars kept went into rate base that earns about the allowed return (Q3), which
  the Q7 range values below the dollar in owner cash (Q7 below). The test is passed on the market leg only narrowly and is not
  shown on the intrinsic leg.
- *Dividends and the use of cash* **[M2004-089]**, **[M2000-051]**: the company pays out about 57% of net income ($74.7M in
  2025) while its operating cash never covers its capital spending; in 2025 it paid $74.7M of dividends and raised $67.1M of
  new equity. The dividend is in effect partly financed by share sales, at commissions of about 1.5%. The stated policy, "to
  achieve a CAGR in the dividend of more than 7% over the long-term", fixes the payout by a growth target rather than by
  whether the business can use the dollar, which the rows call the wrong test **[M2000-051]**, **[L2012-015]**. Weighs against.
- *Buybacks* **[L1999-023]**, **[L2011-003]**: no repurchases in the window (cash-flow statements FY2021 to FY2025 show none).
  *Written back at Q7:* the bottom of the Q7 range is $49.86 a share (central, equity-only); with no repurchases there is
  no price paid to read against it **[L1999-023]**, **[L2013-012]**.
- *Issuance and deals* **[R1995-010]**, **[M1995-001]**, **[L2014-015]**: one ATM program, 2,575,947 shares for $200M gross, an
  average of about $77.64 a share, about 7% of the shares outstanding, used to keep the regulated capital structure near the
  authorized 57% equity; the company says it has "no plans to issue additional equity through, at least, the end of 2029"
  (10-Q 0001628280-26-053401). Not a company "hell-bent on issuing shares" **[L2014-015]**; no acquisitions and no stock-paid
  deal in the window, so Q6's STOP **[L2009-019]** does not arise.
- **Part A WEIGHS AGAINST, mildly**: the retention test is not shown on the intrinsic leg, and a dividend raised by target
  while equity is sold to fund the spending is not the rows' test of a dividend **[M2000-051]**, **[M2004-089]**.

**Part B, the pay, the board and the owners.**
- *Pay tied to what the person controls* **[M2003-019]**: operating-expense levels and ASUS earnings are controllable;
  adjusted EPS against a budget the board approves is partly controllable but invites making the budget **[L2002-041]**;
  relative total shareholder return pays on the market's ride **[M2000-062]**, **[L1996-018]**. Restricted stock units carry
  dividend equivalents (8-K 0001628280-26-017733). Size: $5.0M against $130.4M of earnings is not lavish for the industry,
  and the rows rank the person above the plan **[M2007-006]**.
- *The board* **[M2007-120]**, **[L2014-026]**: an independent chair separate from the chief executive; directors subject to
  ownership guidelines of three times the retainer (proxy). No sign of a weak board in the record read.
- *Owners as partners* **[L1994-023]**: the reports explain the business plainly (Q5); against it, earnings guidance for a
  segment **[L2019-006]** and the featured adjusted EPS **[L2016-006]**.
- **Part B WEIGHS slightly AGAINST**: pay partly on a budget-relative adjusted EPS and on relative stock return, and guidance
  given; offset by an independent chair and real ownership by the chief executive.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon **[M2009-004]**, at the long government rate **[L2000-021]**, **[M1996-025]**, as a range
**[L2000-024]**. The arithmetic is in `Test Runs/_research 2026-10-28 AWR/q7.py`, its output in `q7_output.txt` beside it.

**The basis.** The deciding part (water, 77.6% of five-year operating income, Q2) earns a return the CPUC allows on its
invested capital, so by Q7, The regulated utility, the central figure is on the **equity-only basis**: owner cash after
interest and after the company's own tax, against the market value of the shares **[L2017-012]**, **[M2010-037]**; the
all-equity figure is shown beside it and does not decide. Tax: the company's own cash tax, no conversion (Q7, Whose tax);
no carryforward shelter found.

**The cash input** (Q4's recast, five-year window FY2021 to FY2025, USD millions): owner cash after maintenance only
(operating cash less stock pay less depreciation as the maintenance guess, plus developer advances and contributions net of
refunds, plus other investing) **$104.74M** a year; after all capital spending **$(45.27)M** a year. Mean capital spending
$193.62M, mean depreciation $43.60M, so the growth spending above the maintenance guess is **$150.01M** a year.
*The maintenance guess* **[M2000-144]**, **[L1999-024]**: depreciation, "not inappropriate in most companies to use as a
proxy" **[M1998-127]**. The filing allows no finer split: it describes the spending as "infrastructure renewal programs (to
replace infrastructure, including those to mitigate wildfire risk) and major capital investment projects (to construct new
water treatment, supply and delivery facilities)" without amounts (10-K FY2025, Item 7). Depreciation at historical cost on
assets of very long life probably understates the true cost of standing still **[L2015-004]**, so this guess flatters the
central case; the all-spending case beside it is the check.

**The utility debt credit** (Q7, The regulated utility, as amended 2026-10-23): long-term debt, gross of issue costs and
including current maturities, from the statements of capitalization, was $444.271M at 2020-12-31 and $794.310M at
2025-12-31, an increase of $350.039M, **$70.01M a year**; bank revolver notes and cash left out (with the revolver notes
counted the increase is $71.37M a year; no change to the result); no securitization bonds, no finance leases found. Credited
against the growth spending only, capped at the deciding part's allowed debt share: **43%**, stated for GSWC ("a capital
structure with 57% equity and 43% debt", 10-K FY2025, Item 7, Water Cost of Capital) and the same 43% for BVES, so the
whole regulated rate base is covered. Cap: 43% x $150.01M = **$64.50M**, which binds. Growth spending charged to the equity:
$150.01M less $64.50M = **$85.51M** a year.

**The growth shown, and the cap** (specifics (b) and (f)): maintenance-case owner cash by year was $80.2M, $74.2M, $28.3M,
$156.2M, $184.7M; the end-year compound rate is 23.2% a year, which carried ten years gives about $842M a year against
revenue of $658M, far above the highest share of sales the business has shown (28.1%, in 2025): an absurdity **[M1999-067]**.
By (f) the growth carried is the business's own sales growth over the same window, revenue $498.853M (2021) to $658.073M
(2025), **7.17%** a year, never above the discount rate: **5.30%**. Both written down: shown 23.2%, cut to 7.17%, capped at
5.30%. After year ten, zero nominal growth (Q7 convention).

**The window, by (a) and (d).** The first and last years are not peaks or troughs of a business cycle; the swings are the
rate-case cycle. The filer itself describes 2023 as depressed by the late rate-case decision (regulatory assets built by
$81.4M) and 2025 as lifted by surcharges recovering "all pre-2025 revenue and supply cost activity" and by $14.7M of PFAS
proceeds (10-K FY2025, Item 7). The five-year window contains the whole 2022-2024 rate cycle and the first year of its
recovery, so I keep it as the central base and show beside it the variants (a) and (d) would give; all close the same way.

**The range (equity-only, central; specific (e), the maintenance case central):**
- **No-growth case:** $104.74M a year at 5.30%: $1,976M, **$49.86 a share**.
- **Growth case:** owner cash grows at 5.30% for ten years while the net growth spending ($85.51M, growing with it) is
  charged, then flat at year ten's level with the growth spending stopped: **$54.71 a share**. Growth spending charged in
  year one $158.0M gross, $67.9M of it credited to debt, $90.0M to the equity; in year ten $251.4M gross, $108.1M credited,
  $143.3M to the equity; none after year ten.
- **VALUE RANGE: $49.86 to $54.71 a share**, width 1.10 to one, against **$85.48**.
- *Beside (e), all spending charged:* owner cash $(45.27)M; with the debt credit $19.23M a year, $9.15 a share at no growth;
  without the credit no positive value.
- *Beside, the variants on the base:* the 2022-2024 rate cycle alone (base $86.2M): $41.05 to $41.24; seven years 2019-2025
  (base $99.0M): $47.14 to $50.55; the window with the regulatory-balance line and the PFAS receipt removed, (d)'s
  "intensity before the event" (base $110.1M): $52.41 to $58.62.
- *Beside, the all-equity basis* (owner cash plus interest paid after tax at the window's 23.2% effective rate, $28.32M, so
  $133.06M; no debt credit; net debt at 2026-06-30 of $888.3M = long-term debt $717.7M + current $73.2M + bank notes $119.0M
  - cash $21.7M, operating leases left out): growth case $36.65, no-growth $40.93 a share. On this basis the growth bought
  is worth less than it costs, so the growth case is the bottom (specific (e)'s inversion): $36.65 to $40.93.

**How it closes.** *The floor is tested first* (Q7, CONVENTION of 2026-10-10): at $85.48 the market value is $3,388M; the
central maintenance owner cash is 3.09% of it, and valued at the floor of about ten percent the two cases are worth $26.42
(no growth) and $20.92 (growth) a share. **No case in the range earns the floor at the price**, on any basis or variant shown;
the price is above the top of every range, which closes OUT "however wide the range" (specific (f)'s last sentence). "So,
there’s just a point at which we drop out of the game." **[M2003-149]** "there’s no way we get rich on our utility
investments" **[M2009-104]**: at this price the owner's expected return on the cash the business can give out is below the
long government bond, before any margin of safety **[M1997-126]**.

**The two reporting figures** (the owner's request; Part VII; a reporting convention, not a rule, not a verdict, no entry
language):
- **(a) VALUE RANGE: $49.86 to $54.71 a share** (equity-only, regulated-utility basis, central), against $85.48 (close
  2026-10-27, aggregator).
- **(b) FAIR PRICE: $23.67 a share** on the equity-only basis (central): each end case valued at ten percent, $26.42 and
  $20.92, averaged; owner cash after the company's own tax, no conversion. **All-equity figure beside it: $3.52 a share** (each
  end case at ten percent, $11.16 and $(4.11), averaged, less net debt). Utility debt credit as above: $70.01M a year of
  long-term debt increase, against growth spending only, cap 43% (the deciding part's allowed share), $64.50M credited.
  Growth spending above maintenance $158.0M in year one and $251.4M in year ten (gross), none after.

- **VERDICT: OUT.** No case earns the floor at the price **[M2003-149]**, and the price is above the top of the range
  **[L2013-012]**, **[M2009-005]**.

*Written back to Q6 with this commit:* the bottom of the Q7 range is $49.86 a share (central); the company made no
repurchases in the window, so no price paid is read against it; its share sales averaged about $77.64 gross, above the top
of the range ($54.71), so on this range the ATM sold shares for more than they were worth to the remaining owners, which is
the right side of the value-given test **[R1995-010]**, **[M1995-001]**.

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
**OUT at Q7**: no case of the range earns the floor at the price; VALUE RANGE $49.86 to $54.71 a share (equity-only,
regulated-utility basis) against $85.48 (close 2026-10-27, aggregator); FAIR PRICE $23.67 (equity-only), $3.52 all-equity
beside. Q1 IN, Q2 IN (return set by a regulator, carried to Q3 as a second best), Q3 weighs for weakly, Q4 IN (weighs slightly
against), Q5 IN, Q6 weighs against mildly. No integrity facts outside Q5's answer.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q8 (the bond).** The 30-year Treasury par yield was 5.30% on 2026-10-27 (Treasury); the central maintenance owner cash
  was 3.09% of the market value at $85.48 (Q7). (Source: `tools/sources.py`; Q7 arithmetic.)
- **Q9 (debt and exposures).**
  - Debt at 2026-06-30: long-term debt $717.7M, current maturities $73.2M (including the 5.50% notes of $65M due 2027),
    bank notes $119.0M, cash $21.7M (10-Q 0001628280-26-053401). The revolvers mature in 2029 (AWR, GSWC) and 2028 (BVES);
    the CPUC requires GSWC and BVES to pay their revolvers to zero within each 24-month period (10-K FY2025, Item 7).
  - Cover: pre-tax income plus interest expense over interest expense, 4.0 times in 2024 ($149.4M + $50.4M over $50.4M), 4.9
    in 2023, 4.6 in 2025 (10-K FY2025 income statement). Covenants: GSWC indebtedness to capitalization 0.4352 against a
    limit of 0.6667, indebtedness to EBITDA 3.4 against 8 (10-K FY2025, Note on debt).
  - Strict liability without negligence: "Water utilities may be held strictly liable under inverse condemnation claims for
    fire damage in the event the water system did not operate as designed, including being damaged by the fire itself, even
    if the fire is no fault of the water utility" (10-K FY2025, Item 1A); BVES distributes electricity in a high wildfire
    risk area; wildfire insurance "could become unavailable on reasonable terms or without exclusions for losses due to
    wildfires" (Item 1A). The single-utility concentration the rows warn of, "A catastrophic event can render a single utility
    insolvent" **[L2005-019]**, applies: all regulated operations are in southern California, with earthquake exposure (Item
    1A, natural disasters).
  - The holding company depends on subsidiary dividends; California law limited GSWC's distributable amount to $933.7M and
    BVES's to $117.7M at 2025-12-31 (Item 7). AWR "generally guarantees performance of all of the contracts of ASUS’s
    subsidiaries" (Item 1).
  - ASUS receivables and contract assets due from the U.S. government were about $106M at 2025-12-31 (Q4), exposed to
    appropriations delays and shutdowns (Item 1A).
- **Q10.** Nothing found beyond Q7.
- **Q12.** Nothing found bearing on how the money is made: a regulated water and power distributor and a contractor to the
  U.S. military bases' water systems.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit d67b6f39, before the first EDGAR request); written question by
      question; committed after each (Q1 39c69d6c, Q2-Q3 8783c559, Q4 5d960bee, Q5-Q6 bfa34136, Q7 with the Q6 line 9f483e30).
- [x] Dispatched run: the brief allowed per-question pathspec commits of my two paths; the lock is the dispatching session's
      and I did not touch it. The fold is the dispatching session's (operator rule ten); a run not in the register binds
      nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared at
      the top under contamination, not used: commit subjects of another water utility's run dated today; the memory index.
      My `git log --oneline -1` calls after each commit printed only my own commits.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row, by the check
      script `Test Runs/_research 2026-10-28 AWR/check_ids.py` (output beside it); every filing fact has its accession or the
      named 10-K; no number without a filing or a row, the conventions labelled.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 are NOT REACHED; the facts after the
      stop are not weighed.
- [x] Owner cash after every real cost from the filed cash-flow statements (operating cash less stock pay less capital
      spending, with the maintenance variant), never a net-income proxy (operator rule 5); the sovereign from the US Treasury
      (issuing authority), dated; the price and the 2020 year-end price are aggregator quotes, flagged.
- [x] Contrary evidence written down as found (foundations; Q2; Q3; Q4; after the stop).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its debt column d2 (debt plus equity) was found wrong as debt and
      not used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the final commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (a) does not fit a rate-case cycle.** The swings in a utility's owner cash are regulatory lag (a late decision
builds regulatory assets, surcharges later release them), not a business cycle with peaks and troughs; (a) speaks of
"cyclical peak or trough" and "a year aberrational on the filer's own description", and here the filer describes both the
delay year (2023) and the recovery year (2025) as unusual. I kept the five-year window central because it holds
a whole rate cycle and its first recovery year, and showed the cycle-only, seven-year and normalized bases beside; all close
OUT, so the choice did not decide, but on a closer price it would. A sentence saying that for a regulated utility the cycle is
the rate-case cycle, and whether the regulatory asset and liability line is working capital under (d) or a timing item to be
averaged out, would remove the choice. (2) **The maintenance guess for a utility.** Q7 asks for the maintenance case central
"where the filing allows the guess"; a utility's renewal spending is economically maintenance but earns a return in rate base
like growth spending, and the filing gives no split. Depreciation as the guess (**[M1998-127]**) probably flatters, since
historical-cost depreciation on fifty-year assets understates replacement (**[L2015-004]**). The utility paragraph credits
debt against "growth spending" without saying how renewal spending is classed. (3) **The cap in (f) at the discount rate
makes the growth case nearly equal to the no-growth case** whenever g is cut to the discount rate: with g equal to r the
growth case adds only ten years of net cash. That is arithmetic, not an error, but it means the sales-growth cut, not the
business, sets the top of the range. (4) **"Capped at the allowed debt share"** reads naturally as 43% of the growth spending,
which is how I applied it; the text could say "of the growth spending" to remove the second reading (43% of the debt
increase). (5) The template's fair-price line asks for a figure "on the equity alone and on equity plus net debt where the two
differ"; for a utility the all-equity fair price can be near zero or negative (here $3.52, with the growth case negative at
ten percent), as the 2026-10-18 paragraph notes of earlier runs; the reporting figure on that basis says little.
