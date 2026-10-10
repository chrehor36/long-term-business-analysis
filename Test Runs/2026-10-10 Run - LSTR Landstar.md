# Company Run — Landstar System, Inc. (NASDAQ: LSTR) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md` (brief slots filled by the dispatcher's message of
2026-10-10; departures named under "What in the framework was wrong or unclear"). Template copied to this file and
committed (03224864) before any fetch. Working folder: `Test Runs/_research 2026-10-10 LSTR/` (raw filings and XBRL under
its ignored cache subfolder; the scripts `fetch.py`, `peers.py`, `lstr_series.py`, `compute.py`, `ids.py` and the check
script are committed beside them).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared and not used.** (1) The dispatcher's message says other Landstar run files exist ("there are
earlier ones"); none was opened, listed or searched, and nothing of their content is known to me. (2) The session context
handed to me at start carried a git-status snapshot naming an untracked run file for another company (LOW) and research
folders for AYI and ARCB, and five recent commit subjects naming AME, ITW, JKHY, KEYS and KLAC with their boxes and alert
prices. (3) The same context carried the operator's memory index, whose lines speak of the queue's state and of holdings
reviews owed, without naming Landstar. None of this bears on Landstar and none of it was used. (4) While checking my own commit, `git log -2` and `git show --stat HEAD` printed another analyst's commit subject
and file list for the LOW run (a Q2 verdict on Lowe's); not about Landstar, not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $169.11 (close 2026-10-09, as printed by `python tools/run.py LSTR`; aggregator, live quote only, flagged per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, **33,936,925** shares (10-Q for the period
  ended 2026-06-27, filed 2026-07-29, accession `0001193125-26-322966`; `python Screens/cover_shares.py LSTR`). Checked
  against the same 10-Q's balance sheet: issued 68,631,174 less 34,694,249 in treasury = 33,936,925. No 8-K or prospectus
  after that 10-Q changes the count (8-K list read to 2026-07-28; the 2026-07-28 8-K is the earnings release).
- **Market cap:** $5,739.1M (169.11 × 33.936925M).
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 2026-10-09 (as fetched
  by `tools/run.py` from the issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2025 (period ended 2025-12-27, filed 2026-02-24, accession
  `0001193125-26-064756`); the 10-Qs for 2026 Q1 (`0001193125-26-191131`) and Q2 (`0001193125-26-322966`) and 2025 Q3
  (`0001193125-25-253766`); the 2026 proxy (filed 2026-03-23, `0001193125-26-118697`) and the 2025 proxy
  (`0001193125-25-072935`); the earnings releases (exhibit 99.1) of 2026-01-28 (`0001193125-26-027265`) and 2026-07-28
  (`0001193125-26-321050`); and every 10-K from FY2007 to FY2024 for the cycle record (FY2007 `0000950144-08-001392`,
  FY2008 `0000950144-09-001583`, FY2009 `0000950123-10-015813`, FY2010 `0000950123-11-016941`, FY2011
  `0001193125-12-077747`, FY2012 `0001193125-13-069441`, FY2013 `0001193125-14-062590`, FY2014 `0001193125-15-056671`,
  FY2015 `0001193125-16-469941`, FY2016 `0001193125-17-056249`, FY2017 `0001193125-18-055528`, FY2018
  `0001193125-19-048217`, FY2019 `0001193125-20-044766`, FY2020 `0001193125-21-052225`, FY2021 `0001193125-22-046673`,
  FY2022 `0001193125-23-048874`, FY2023 `0001193125-24-044902`, FY2024 `0001193125-25-033543`).
  **Figures cross-checked against the filed statements:** net income for the 2026 second quarter, $48,951K, in the 10-Q's
  income statement equals the release's $1.44 a share on 33,935,000 shares; FY2025 cash from operations, $224,882K, in the
  10-K's liquidity text equals the XBRL value `tools/run.py` printed (224.9).
- `python tools/run.py LSTR`, arithmetic lines only (Part VII): OCF 393.6 / 286.6 / 224.9 (FY2023 to FY2025), SBC 4.3 / 3.4 /
  6.0, capex 25.7 / 31.0 / 9.9, D&A 58.2 / 56.7 / 46.4; OCF less SBC less capex 363.7 / 252.1 / 209.0. Two corrections from
  the filing: (a) the tool's balance-sheet column "lt debt" prints 0 for every year, but the filed balance sheets carry
  long-term debt (finance leases for trailers) of $48,480K plus current maturities $28,342K at 2025-12-27 (10-K) and $42,088K
  plus $24,686K at 2026-06-27 (10-Q); (b) the tool's owner-cash line omits trailing equipment bought by finance lease, which
  the 10-K states ($7,732K, $62,194K, $4,093K acquired by finance lease in FY2025, FY2024, FY2023) and whose principal is
  repaid in financing ($33.2M, $31.0M, $36.4M). The run counts that principal as capital spending (operator rule 5:
  every real cost). Owner cash as recast is in `compute.py` and under AFTER THE STOP, Q7.

**The balance sheets, eight to ten years, read here because the file closes before Q4** (brief, Read first item 2;
`tools/run.py` table checked against the FY2016 to FY2025 10-Ks and the 2026 Q2 10-Q) **[M2025-032]**:

| year-end | assets | equity | cash | receivables | goodwill | debt (finance leases) | insurance claims (current + noncurrent) |
|---|---|---|---|---|---|---|---|
| 2016 | 1,097 | 543 | 179 | 463 | 31 | in other liabilities, not split by the tool | 53.0 |
| 2018 | 1,381 | 687 | 200 | 692 | 38 | 128.5 | 70.6 |
| 2020 | 1,654 | 692 | 249 | 764 | 41 | 100.8 | 188.7 |
| 2022 | 1,932 | 887 | 340 | 968 | 41 | 103.4 | 109.1 |
| 2024 | 1,813 | 972 | 515 | 684 | 41 | 102.3 | 103.3 |
| 2025 | 1,636 | 796 | 397 | 670 | 34 | 76.8 | 150.0 |
| 2026-06-27 | 1,743 | 837 | 294 | 867 | 34 | 66.8 | 157.7 |

(USD millions; FY2018 onward finance leases are the XBRL `FinanceLeaseLiability` current plus noncurrent and, from FY2023,
the filed "long-term debt including current maturities"; insurance claims are `SelfInsuranceReserveCurrent` plus
`SelfInsuranceReserveNoncurrent`.)
What moved and why. Equity stays small (about $0.5bn to $1.0bn) against $2.85bn of retained earnings because about
$2.5bn has gone to buybacks since 1997 (FY2025 10-K: "Since January 1997, the Company has purchased approximately
$2,515,000,000 of its Common Stock") and $1.09bn to dividends since 2005; the treasury account was $2,313M at 2025-12-27.
Goodwill is trivial against equity in every year ($31M to $42M). Receivables move with revenue and keep their proportion
(14.6% of FY2016 revenue, 14.1% of FY2025 revenue; the peak, $1,154M in FY2021, was 17.7% of a 58% revenue jump), so the
receivable book is not building against sales. Debt is only trailer finance leases. Cash rose to $515M in FY2024 and fell
to $397M and then $294M as buybacks of $180.9M (FY2025), dividends and a receivables build in the 2026 recovery
(receivables up $194M in the first half) drew it down. The one balance-sheet line that has grown against the business
is insurance claims: $53M at FY2016 on $3.2bn revenue, $189M at the FY2020 peak, $150M at FY2025 on $4.7bn, $158M at
2026-06-27, with $12.0M of a
reinsurer's "no claims bonus" reclassified into it in connection with the Cabral judgment (FY2025 10-K, note 11). What the
figures cannot say: the size of a nuclear verdict not yet suffered, which is outside any reserve (see Q2 below).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, which for Landstar means owning a commission-and-percentage freight network whose earnings swing with the
truck cycle; the market's quote of $169.11 tells me only a price **[M2006-077]**. Margin of safety: a decision that
needs "pencil and paper" is "too close to think about" **[M1996-084]**. No macro forecast enters: the freight cycle is read
as a property of the business over whole cycles, not forecast. The analyst's habits: write contrary evidence down as found
**[M1997-127]**; look for what would reject the hypothesis **[M1998-144]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the BCO truck fleet at 2025-12-27 (8,514) is smaller than at 2006-12-30 (9,205) and 28% below its
2021 peak (11,864); (2) independent agents fell from "over 1,200" (FY2019, FY2021 10-Ks) to "approximately 960" (FY2025);
(3) insurance and claims were $159.4M in FY2025, above operating income of $151.6M; (4) on 2026-05-14 the Supreme Court held
in Montgomery v. Caribe Transport II that negligent-selection claims against freight brokers are not preempted (10-Q
2026 Q2), and 53% of Landstar's FY2025 revenue was brokered; (5) operating margin of 3.2% in FY2025 is the lowest in the
span read (FY2005 to FY2025), below the 2009 trough of 5.7%.

## THE STANDING RULE
The buyer's conduct: a purchase of this name at any size the operator would consider is for cash, with no borrowed money
and nothing that can call **[L2014-005]**, **[M2012-081]**. Nothing in the target makes a holder's loss larger than the price
paid. No ruin to the buyer from this name as such; the rule is met if the operator's own financing keeps it so.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the 10-K (FY2025, `0001193125-26-064756`).** An agent network that sells truck capacity it
  does not own. "approximately 960 independent commission sales agents" find the freight; the capacity is "BCO Independent
  Contractors" (owner-operators leased exclusively to Landstar, 38% of FY2025 revenue) and "Truck Brokerage Carriers"
  (62,790 approved, 53% of revenue), with rail, air and ocean the rest. Revenue $4,743.8M. The cost structure is contractual
  and variable: a BCO "provides only a tractor" and receives 62% to 70% of the load's revenue, or 73% to 77% with its own
  trailer, paying "substantially all of the expenses of operating his/her equipment"; agents receive a contractual
  percentage. Purchased transportation was 77.8% and commissions 8.2% of FY2025 revenue, so Landstar keeps about 14.0% of
  revenue (its "variable contribution") from which it pays insurance and claims, SG&A, depreciation and other costs.
- **The key variables, and how predictable they are** **[M1998-044]**: (1) loads and revenue per load, which swing with the
  truck cycle and are priced largely "in the spot market" (FY2025 10-K, Item 1); (2) the share of revenue kept after
  purchased transportation and commissions, which the filings show in a narrow band over eighteen years (variable
  contribution 17.2% in FY2009 at the widest, 14.0% in FY2025 at the narrowest; FY2007 to FY2025 10-K percentage tables);
  (3) the indirect costs, of which insurance and claims is the one that moves (1.3% to 2.4% of revenue FY2007 to FY2024,
  3.4% in FY2025). Variables (1) and (2) are cyclical but bounded and readable from the past statements, which "tell me the
  information that’s useful" about future ones for this model **[M2008-033]**; I understand the "economic dynamics of the
  industry" **[M2011-014]**: a fragmented spot market for trucks in which an intermediary is paid a cut. Variable (3) is
  where foresight fails, and it is a threat to the economics rather than a gap in understanding the model, so it is taken
  at Q2, test 11, where the rows put what can "destroy, or modify, or reduce the economic strengths" **[M2000-014]**.
- **Routing.** Not a fast-changing technology business in the sense of **[M1998-008]**: the model (agents plus leased
  owner-operators plus brokered carriers) is the one the FY2007 10-K describes, and the digital-broker threat is a castle
  question, owned by Q2. Not a financial institution; the captive insurer (Signature) is about 1% of revenue and reinsures
  the company's own BCO programs.
- **VERDICT: IN.** A reasonable fix on the earning power's drivers and the company's place in its industry ten years out
  **[M2012-065]**, **[M2000-037]**, with the claims-and-liability cost named as the one variable I cannot fix and carried to
  Q2. Doubt about the perimeter itself is not present: the business is simple **[M2002-092]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**

**The parts table.** Two reported segments (FY2025 10-K note 12; FY2023 and FY2021 10-K segment notes): transportation
logistics operating income $464.3M (FY2021), $524.5M (FY2022), $288.6M (FY2023), $205.7M (FY2024), $147.9M (FY2025);
insurance (the captive Signature, reinsuring the company's own BCO programs and billing internal premiums) $41.4M, $46.6M,
$55.6M, $43.2M, $3.7M. Transportation logistics carries about 90% of five-year operating profit and decides; the captive is
not a separate castle but the self-insurance of the decider, so it is read inside test 11 below.

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent* **[M1995-038]**. The filer names its walls: "the largest fleet of truckload BCO
   Independent Contractors in the United States", "more independent commission sales agents than any other asset-light
   integrated transportation management solutions company in the United States", a 62,790-carrier brokerage database, and
   "paying its agents and carriers promptly" against "less capitalized competitors" (FY2025 10-K, Item 1). Permanence: the
   model is the one the FY2007 10-K describes; Million Dollar Agent terminations "have typically been less than 3%" a year.
   Against: both walls have shrunk. BCO trucks 9,205 (FY2006), 8,993 (FY2007), 8,519 (FY2009), 8,432 (FY2013), 9,500
   (FY2015), 10,599 (FY2018), 11,864 (FY2021), 9,809 (FY2023), 8,843 (FY2024), 8,514 (FY2025); BCO turnover 35% (FY2024)
   and 31% (FY2025). Agents "over 1,200" (FY2019, FY2021 10-Ks), "over 1,100" (FY2022), "over 1,000" (FY2023),
   "approximately 1,050" (FY2024), "approximately 960" (FY2025); Million Dollar Agents 625 (FY2022) to 457 (FY2025), against
   555 in FY2019 on lower revenue.
2. *Without the lord* **[L2007-006]**. Not a superstar chief executive (the present one was hired from outside in 2024,
   proxy 2026); the lords are the agencies: 77 agencies produced about 68% of FY2025 revenue. The network keeps them by
   capacity, credit and administration, not by ownership of the customer.
3. *The money test* **[M2011-015]**. An attacker with money can build a brokerage; the field is "extremely competitive and
   fragmented" (FY2025 10-K, Item 1A), and the large private rivals are not filers (below). What an attacker cannot quickly
   buy is 8,500 exclusive owner-operator trucks and 960 agents; the filings show the number of each falling, but no filing
   shows an attacker taking them.
4. *Pricing power* **[M2005-020]**. None shown. Truck revenue per load fell 9% (FY2019), 13% (FY2023) and 2% (FY2024) and
   rose 29% (FY2021) (10-K MD&A); "A significant portion of the Company’s truckload services is priced in the spot market"
   (FY2025 10-K). The price is the market's **[M2012-109]**; what Landstar holds is a contractual share of it.
5. *Unit volume* **[M1999-054]**. Truck loads 2,060,270 (FY2018), 2,006,260 (FY2019), 2,566,800 (FY2022), 1,943,800
   (FY2025); loads hauled by BCOs 851,880 (FY2006), 761,940 (FY2009), 806,350 (FY2012), 898,610 (FY2023), 798,050 (FY2025).
   Volume through the network's own trucks is flat for twenty years; the growth came from brokered loads.
6. *Low-cost position* **[L2004-007]**, **[M2001-013]**. On operating margin against the largest asset-light rival,
   Landstar was below C.H. Robinson in FY2009 (5.7% against 7.7%) and FY2025 (3.2% against 4.9%) and above it in the years
   between shown below. Not shown to be the low-cost operator through the whole span.
7. and 8. *The brand, and the low bid* **[L2004-003]**, **[M2017-009]**. Eight of the top 25 customers in FY2025 were
   transportation service providers, including 3PLs, buying Landstar's capacity for their own shippers (10-K, Item 1); for
   them the purchase is capacity at a price. No filing evidence that shippers ask for Landstar by name.
9. *Ask the competitors*. Not on the public record; recorded as unanswered.
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Revenue less purchased transportation and commissions was
   17.2% of revenue (FY2009), 16.0% (FY2012), 15.0% (FY2015), 15.1% (FY2019), 14.6% (FY2023), 14.2% (FY2024), 14.0% (FY2025),
   partly mix (brokerage grew faster than BCO revenue). Operating income as a share of that contribution was 43.4% to 49.7%
   in FY2013 to FY2019 (10-K tables "as a percentage of gross profit") against about 23% in FY2025 (151.6 on 664.1).
   Narrowing on every measure the filings give, in what the filer calls "the soft freight demand environment" (FY2025
   10-K). The rows excuse a bad year as "a cyclical problem, not a secular one" where superiority was "at least
   maintained" **[L1995-022]**; here the walls themselves (trucks, agents) shrank, and the recovery is one half-year old
   (2026 Q2 release, `0001193125-26-321050`: revenue up 18%, "net 68 BCO truck additions during the second quarter").
11. *What could destroy, modify or reduce it* **[M2000-014]**. The claims cost of the carrier model and of brokerage.
   Insurance and claims were 1.3% to 2.4% of revenue in FY2007 to FY2024 and 3.4% in FY2025 ($159.4M, more than operating
   income of $151.6M); about $7.1K per BCO truck in FY2018 against $18.7K in FY2025; $32.1M of unfavorable prior-year
   development in FY2025 against $8.8M and $6.1M in the two years before. Excess-coverage premiums up "approximately 400%"
   since the policy year ended 2020-04-30; a hypothetical $65M claim leaves Landstar "an aggregate financial exposure of
   approximately $33 million" in the policy year ending 2027-05-31, and above "an uppermost coverage layer" "the Company
   retains additional financial exposure" (FY2025 10-K; the $33M figure from the 10-Q 2026 Q2). The Cabral judgment of 2026-01-13 held Landstar Ranger, as
   broker, responsible for 100% of $22.8M rather than the jury's 15%. On 2026-05-14 the Supreme Court held in Montgomery v.
   Caribe Transport II that such a broker-liability claim falls within the FAAAA "safety exception"; the filer says the
   decision "may increase the frequency, severity and potential loss associated with such claims" and "Following the
   decision, others in our industry have faced Broker Liability Claims resulting in Nuclear Verdicts in excess of $100
   million" (10-Q 2026 Q2, Item 1A). Brokered revenue was 53% of FY2025 revenue. The filer's own forecast of the cost:
   "Potential liability associated with accidents in the trucking industry is severe and occurrences are unpredictable",
   and the Cabral outcome is "difficult to predict" (FY2025 10-K).

**The competitor row** (same metrics, each from its own 10-K XBRL, first-filed vintage; operating margin = operating
income over revenue; ROE = net income over year-end equity; latest 10-K accessions: LSTR `0001193125-26-064756`, CHRW
`0001043277-26-000009`, JBHT `0001437749-26-005294`, WERN `0000793074-26-000071`, KNX `0001492691-26-000016`, RXO
`0001929561-26-000013`, HUBG FY2024 `0000950170-25-026866`, SNDR `0001692063-26-000013`):

| op margin / ROE | FY2009 | FY2016 | FY2019 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|---|
| Landstar | 5.7% / 26.3% | 7.0% / 25.3% | 7.3% / 31.6% | 7.7% / 48.6% | 6.5% / 26.9% | 5.2% / 20.1% | 3.2% / 14.5% |
| C.H. Robinson (asset-light broker) | 7.7% / 33.4% | 6.4% / 40.8% | 5.2% / 34.5% | 5.1% / 69.5% | 2.9% / 22.9% | 3.8% / 27.0% | 4.9% / 31.8% |
| J.B. Hunt (asset-based) | 7.7% / 21.2% | 11.0% / 30.6% | na / 22.8% | na / 26.4% | na / 17.7% | na / 14.2% | na / 16.8% |
| Werner (asset-based) | 5.8% / 8.0% | 6.3% / 8.0% | 9.2% / 15.0% | 9.8% / 16.7% | 5.4% / 7.4% | 2.2% / 2.4% | 0.4% / -1.1% |
| Knight-Swift (Swift's figures to FY2016) | 5.1% / negative equity | 6.0% / 19.0% | 8.8% / 5.5% | 14.7% / 11.1% | 4.7% / 3.1% | 3.3% / 1.7% | 2.9% / 0.9% |
| old Knight Transportation (to FY2016) | 12.6% / 9.7% | 13.3% / 11.9% | merged | | | | |
| RXO (spun from XPO in 2022; its filings reach back to FY2020 only) | no filing | no filing | no filing | 2.6% / 15.7% | 1.0% / 0.7% | -1.2% / -18.0% | -1.4% / -6.5% |
| Hub Group | 3.7% / 9.7% | 4.5% / 11.9% | 4.2% / 10.0% | 8.9% / 22.3% | 5.1% / 10.2% | 3.6% / 6.3% | not read |
| Schneider | no filing | 7.2% / na | 4.4% / 6.6% | 9.1% / 16.1% | 5.4% / 8.1% | 3.1% / 3.9% | 3.0% / 3.4% |

(J.B. Hunt's revenue tag is absent from the first-filed vintage after FY2017, so its margin is not shown. **Non-filers
flagged:** Total Quality Logistics, Arrive and Mode are private and not SEC filers; Echo Global Logistics has not filed since
it was taken private in 2021; Uber Freight and Coyote (inside UPS until RXO bought it) are not separately reported. No
figure about any of them is used.)

**The field's returns over the last full cycle**, judged in words (CONVENTION of Q2: "ordinary" carries no figure). The
two asset-light leaders earned excellent returns on their small capital through the 2009 trough, the 2016 and 2019
softness and the 2023-25 freight recession (Landstar's ROE never below 14.5% in the span, C.H. Robinson's never below
22.9%); the asset-based carriers earned ordinary returns at best and close to nothing in FY2024-25; the newest public broker
has lost money since FY2024. So this is not a durable castle protecting only ordinary returns. A thin margin earns this
return only because the equity turns fast **[M2017-096]**: revenue was about six times equity in FY2025 (4,743.8 on 795.7).

**What the evidence says, together.** The castle stands: the same model for thirty years, among the field's best returns
on capital, no loss year in the span read. It is not widening: the owner-operator fleet is smaller than in 2006, the agent
count has fallen by about a fifth since 2021, the share of contribution reaching operating income has roughly halved since
2019, and there is no pricing power of its own **[M2005-020]**. And the economic strength it protects is being reduced by a
cost the filer says it cannot predict, sharpened by a Supreme Court decision under five months old that narrows a defence on
more than half the revenue **[M2000-014]**. Whether 2023-25 was a cyclical trough or the walls thinning cannot be told from
one recovering half-year; whether the network's economics survive the liability regime is a forecast the insiders decline
to write down, "occurrences are unpredictable" in the filer's words **[M2000-105]**. "If something’s important but
unknowable, forget it." **[M2006-076]**; "when we see a moat that’s tenuous in any way [...] it’s just too risky. We don’t
know how to valuate that, and therefore we leave it alone." **[M2000-019]**; "If we can think of very much that can go wrong
with them, we just forget it." **[M2000-016]**. The castle is not shown open on the evidence (the walls shrank in a freight
recession, and no rival is shown taking them), so the box is not OUT; its future cannot be judged, so it is TOO HARD
**[M2006-013]**.

**Which cause.** The deciding question is the forward cost of accident and broker liability on this network, together with
whether the network's walls recover with the cycle. The first is a forecast the insiders will not make (above), and no
filing not yet read would supply it; the second is knowable only from cycles not yet run. A research pass could not close
it, and a pass that ends unsure ends in NATURE (section I, citing **[M2002-092]**); "in other cases the nature of the
industry would be the roadblock" **[L1993-023]**.

- **VERDICT: TOO HARD (NATURE)**, with **[M2000-014]**, **[M2000-019]**, **[M2006-076]**, **[M2000-105]**, **[M2006-013]**.
  The file closes here. Q3 to Q10 and Q12 are NOT REACHED.

## Q3 to Q10, Q12: NOT REACHED (closed at Q2, operator rule 2)

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q2**: the castle stands and earns high returns on little capital, but it is not
widening, and its future economics turn on accident and broker-liability costs that the filer itself calls unpredictable,
sharpened by the Supreme Court's Montgomery decision of 2026-05-14. Integrity facts recorded, not judged (Q5 below).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box unchanged.

**Q3 (capital).** Equity $795.7M (FY2025) against revenue $4,743.8M; operating income over equity plus finance-lease debt
less cash ran from 38% (FY2025) to over 100% (FY2022) in the run's XBRL arithmetic (`peers.py`, finance leases not in that
denominator). Capital spending is trailers and IT: purchases $9.9M (FY2025), $31.0M (FY2024), $25.7M (FY2023), plus trailers
by finance lease $7.7M, $62.2M, $4.1M; planned for FY2026 about $104M of trailers "by purchase or lease financing", $12M of
IT and $3M of buildings (FY2025 10-K, liquidity). Working capital: receivables built $194M in the first half of 2026 as
revenue rose 10% (10-Q 2026 Q2 cash-flow statement), and released in FY2022-23.

**Q4 (accounts).** FY2025 carried $32.2M of non-cash impairments (Landstar Metro held for sale $18.2M, a brokerage TMS wound
down $9.0M, the remaining $5.0M not itemized in this run) and a $4.8M charge for the "Supply Chain Fraud Matter" in international freight
forwarding, through which revenue and purchased transportation "as reported in the Company’s fiscal year 2024, 2023 and 2022
financial results were each overstated by approximately 2 %, 1 %, and less than 0.5 %" (FY2025 10-K, note 18), judged
immaterial by the company. Unfavorable prior-year claims development in each of FY2023 to FY2025 ($6.1M, $8.8M, $32.1M) and
again in the 2026 first half. Stock pay $6.0M (FY2025), $27.5M in FY2021. The releases' only non-GAAP measures are variable
contribution and its margin (release of 2026-07-28); the headline is GAAP EPS. No earnings guidance found in the text of the
releases of 2026-01-28 and 2026-07-28 (search: "guid", "outlook", "range").

**Q5 (people; integrity facts recorded, not judged).** (1) The 2025 annual bonus plan was changed to add a "Strategic Goals
Incentive" portion; diluted EPS of $3.31 fell 41.0% below the $5.61 threshold, and "Had the ICP not been modified for 2025
to include the Strategic Goals Incentive portion, there would have been no bonus payouts generated for any Named
Executives", as in 2023 and 2024 (proxy 2026, `0001193125-26-118697`). (2) Only 47% of votes cast supported say-on-pay at
the 2025 meeting, attributed by the company to the chief executive's $10,000,000 sign-on grant of TSR-based RSUs (vesting on
a 9% TSR CAGR from a $188.74 base, measured after years six to ten; on a change in control at 125% of the price that
achieves that CAGR). (3) The revenue overstatement through a supply-chain fraud, undetected over 2022-2025 (Q4 above).
(4) Hedging and pledging of company stock are prohibited for directors and named executives (proxy 2026). (5) The
chief executive (since 2024-02-02) was hired from outside after a search; the board chair is non-executive.

**Q6 (money and owners).** Buybacks, average price paid (cost over shares, 10-K and 10-Q text): FY2013 $53.3; FY2015 $64.5;
FY2016 $65.3; FY2018 $104.0; FY2019 $104.3; FY2020 $98.4; FY2021 $167.2; FY2022 $150.5; FY2023 $169.9; FY2024 $181.7;
FY2025 $141.1; first half 2026 $149.5. Authorization is stated in shares (1,266,118 remaining at 2025-12-27); no price limit
found in the filings read. Special dividends of $0.35 (paid 2014-01), $1.00 (2015-01), $1.50 (2018-01) and $2.00 (each
January 2020 to 2026); regular dividend $0.40 a quarter in 2026. About $2.5bn of stock bought since 1997 and $1.09bn of
dividends since 2005 (FY2025 10-K). Pay: annual bonus on EPS against budget until 2025, on operating income against budget
from 2026; RSUs on average change in operating income and pre-tax income per share, moving to EPS for 2026 (proxy 2026).

**Q7 (COMPUTATION, NOT A CLEARANCE).** Owner cash = cash from operations less stock pay less capital spending less
finance-lease principal (all from the 10-K cash-flow statements; `compute.py`):

| FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| owner cash, after interest (equity-only) | 117.4 | 68.9 | 226.6 | 239.6 | 131.8 | 188.3 | 545.2 | 327.2 | 221.2 | 175.8 |
| owner cash before net interest (all-equity) | 119.8 | 70.9 | 229.1 | 242.0 | 134.8 | 191.3 | 547.9 | 324.2 | 217.0 | 176.6 |

Specific (a), the cycle base: the literal window's first year, FY2021, is aberrational on the filer's own description,
"two years of unprecedented strength in demand for the Company’s services in 2021 and 2022" (FY2022 10-K), and its last,
FY2025, is the trough of what the filer calls the "soft freight demand environment". Base = the last full cycle, trough
FY2020 to trough FY2025, averaged FY2020-24: $283.0M all-equity ($282.7M equity-only). Growth between the averages of
successive cycles (FY2016-19, $165.4M, to FY2020-24; 4.5 years between midpoints): 12.7% a year (13.0% equity-only),
carried ten years at the shown rate as the cap allows **[M1997-095]**, then no growth, at 5.60%. Beside it, operating income
grew 7.8% a year between the same cycle averages, and the literal window FY2021-25 averages $291.4M with growth of -2.0% a
year 2021 to 2025. Net cash at 2026-06-27 (10-Q): cash $294.4M + short-term investments $53.4M + long-term investments
$95.7M - cash overdraft $71.8M - finance-lease debt $66.8M = $304.8M; no subsequent event stated in that filing changes it;
$83.7M of the investments secure insurance letters of credit (counted as the convention directs, said so).

**The two reporting figures (reporting convention, brief and Part VII; COMPUTATION, NOT A CLEARANCE):**
- **(a) VALUE RANGE, by Q7's specifics, all-equity basis (central):** $157.92 to $415.05 a share (no-growth case to the
  12.7% case, whole business $5,054M to $13,781M plus net cash, over 33,936,925 shares; width 2.73 to 1). Equity-only beside
  it: $148.77 to $416.11. The literal window beside both: $140.01 to $162.32 (all-equity; -2.0% growth at the bottom, no
  growth at the top).
- **(b) FAIR PRICE: $151.41** a share on the all-equity basis; **$144.63** equity-only. Definition used (one, stated): the
  two cases of the range are each valued at the 10% floor instead of 5.60%, on owner cash after the company's own tax, and
  the fair price is the midpoint of those two values plus net cash (none added on the equity-only basis), per share.
- Against the price of **$169.11** (2026-10-09, aggregator): above the fair price on both bases; inside the computed range,
  near its bottom. The range itself rests on the cash figures whose future Q2 could not judge.

**Q9 (exposures).** No borrowings; $300M revolver undrawn, maturing 2027-07-01, with $34.9M of letters of credit under it
and $75.3M more secured by $83.7M of investments; self-insured retention $5M per trucking occurrence, $18M aggregate
deductible on the $5M-$10M layer to 2026-05-31, new $5M-$10M layer from 2026-06-01 with a $10M yearly aggregate; above the
top excess layer the company retains the loss; $65M claim leaves about $33M with Landstar (FY2025 10-K; 10-Q 2026 Q2).
"we have passed up some businesses, because we were worried about the product liability potential" **[M2001-008]** is the
row these facts would be weighed against.

**Q12.** Truck freight services; none of the businesses the rows name.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (03224864); written question by question; Step 0 to Q1 committed (76a606f3,
      after waiting on an `index.lock` held by another session, never deleted). Q2 and the sections after it went into one
      commit: the lock blocked the Q2 commit while the rest was being written. A partial departure from write-early, declared.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatcher's; the fold is the dispatcher's.
- [x] No other run file, holding review, `PORTFOLIO.md`, register or reading list was opened, listed or searched; what I saw
      by accident is declared under CONTAMINATION and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every fragment quoted beside an id is in that row (check script
      `Test Runs/_research 2026-10-10 LSTR/check_ids.py`); every filing fact carries its document and accession.
- [x] The order was kept; Q2 closed the file; everything after it is a recorded fact or a COMPUTATION, not a clearance.
- [x] Owner cash after every real cost, including trailer finance-lease principal; no net-income proxy; sovereign from the
      Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor issue.
- [x] Only the arithmetic lines of `tools/run.py` used, and two of them corrected from the filing (Step 0).
- [x] `python tools/check_framework.py` run before the final commit (result in the dispatcher's report).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Where an industry-wide, unpredictable cost belongs.** Landstar's deciding question is a cost (accident and broker
liability) that falls on the whole field, not a rival crossing the moat. The text gives it three possible homes: Q1 test 4
("important but unknowable", **[M2006-076]**), Q2 test 11 (what could "reduce the economic strengths", **[M2000-014]**), and
Q9's liability test (**[M2001-008]**, a WEIGHING). Q1's routing sentence covers only fast-changing industries. I placed it at
Q2, test 11, because that row names reduction of the strengths over five to fifteen years; a second analyst could weigh it at
Q9 and reach Q7, where the price on this run's computation would have closed the file OUT. The box would differ in name
only if Q7 had been reached, but the cause recorded (NATURE) bars a later re-look that an OUT would not. (2) **A change for
the worse has no rule.** Section C of the gaps case says a change for the better is credited only after a full cycle and is
TOO HARD (WORK) till then; the text says nothing of narrowing seen only inside a downturn. I read it as a future that cannot
yet be judged. (3) **The cycle base with working-capital swings.** Specific (a) defines the cycle on owner cash, which here
swings with receivables (FY2022 includes a release of the FY2021 build), so the growth between cycle averages (12.7%) is
well above the growth of operating income between the same cycles (7.8%); both are shown. (4) **Net debt and restricted
securities.** The convention subtracts all cash and securities "as the filing states them"; $83.7M of Landstar's
investments secure insurance letters of credit; counted, and said. (5) **The fair price** is defined in words only ("the
price at which the midpoint of the range earns the floor"); this run's construction (both cases revalued at 10%, the
midpoint taken) is one reading, stated. **Errors in the brief.** (a) It asks for RXO "from their own filings over the whole
span"; RXO was spun from XPO in 2022 and its filings reach back only to FY2020, so the whole span is impossible
for it. (b) The dispatcher's message tells the analyst that earlier Landstar run files exist, which is itself a fact about
blind-listed files that the blind rule says not to try to learn; declared under contamination. (c) It names RXO, J.B. Hunt,
Werner and Knight-Swift as the comparison; three of the five are asset-based carriers, not the agent-and-broker model, and
the closest model rivals (other agent networks, TQL) are private; I added Hub Group and Schneider from their filings and
flagged the non-filers.
