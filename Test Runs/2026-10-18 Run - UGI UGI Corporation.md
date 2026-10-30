# Company Run — UGI Corporation (NYSE: UGI) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to its dated name before any fetch.**

Dispatched blind run, written question by question under the canonical brief `Screens/_daily/_dispatch_brief.md`, with
the brief's one stated departure (the lines of evidence and the competitors derived by the analyst from the 10-K). Research
folder: `Test Runs/_research 2026-10-18 UGI/` (notes, scripts, the `tools/run.py` output; raw filings in the ignored
`cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold (overnight 2026-10-18), after the run was committed: the operator does not hold this name (`PORTFOLIO.md`
names no UGI position).*

**CONTAMINATION, declared:** (1) a directory listing of `Test Runs/` made to confirm the dated file name showed eight other
run files and research folders dated 2026-10-18 (HOKCY, MDU, NJR, NWN, OGS, SR, SWX, XNGSY); none was opened. (2) The
session context carried the subjects of recent commits, among them the fold of the SR (Spire) run, whose subject states its
box (OUT at Q7) and that its Q2 passed as "the regulated exception". (3) The memory index loaded with the session carries one
line on the queue state (counts of gate-clearers), nothing on this company. None of these was used: the boxes below are
reached from the UGI filings and the v5 text alone, and the regulated-return paragraph applied at Q2 is read from the
framework's own Q2 text. (4) *Added on resume (2026-10-18):* the resumed session's context carried a git status listing
naming untracked files in two other companies' research folders (dated 2026-09-26 and 2026-09-27, tickers AYI and ARCB),
the subject of an overnight-log commit saying the overnight cycle skipped UGI because this run file already existed, and
this run's own earlier commit subjects. None was opened or used; none says anything about this business.

**THE LINES OF EVIDENCE, chosen from the 10-K (the brief's departure), and why.** From Item 1 (accession
0000884614-25-000053): four segments with different economics, so the parts table and the deciding part (Q1, Q2) are the
first line. From Item 1A: weather, the decline of retail LPG volumes in the US and Europe ("mature and has experienced
either no or modest growth (or decline)"), electrification and EU decarbonisation policy, regulatory rate risk, commodity
and collateral liquidity risk, about $7 billion of debt, and the impairments; so the second line is the trend of the LPG
parts' volumes and profits over the span, and the third is the debt, the collateral calls and the convertible notes (Q9).
From Item 7: the adjusted earnings reconciliation (Q4, Q5), the goodwill impairments of AmeriGas (FY2023 $656 million,
FY2024 $195 million), the portfolio sales of FY2024 to FY2026 (UGID, European energy marketing, Italy, UK cylinders,
Austria, four central European countries, Hawaii, and from April 2026 the Electric Utility), and the capital programme
($1,053 million estimated for FY2026, most of it in Utilities); so the fourth line is what the capital spent earns (Q3,
Q7) and the fifth is the use of the money and the deals (Q6).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $38.43 (close 2026-10-16, the last close before the run date; source `tools/run.py`, which takes it from an
  aggregator; **aggregator, flagged**, operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock without par value, **214,494,967** shares as
  of 2026-07-31 (10-Q for the quarter to 2026-06-30, filed 2026-08-06, accession `0000884614-26-000052`;
  `python Screens/cover_shares.py UGI`). Check: issued shares 217,706,132 at 2026-06-30 on the same 10-Q's balance sheet,
  less treasury shares (not tagged by count; the difference implies about 3.2 million, consistent with treasury stock at
  cost of $118 million); basic weighted shares for the quarter 214,690 thousand. The 8-Ks filed after the 10-Q
  (2026-08-06 results, 2026-08-10 officer item, 2026-08-17 and 2026-10-02 private note placements at UGI Utilities and
  Mountaineer, "used primarily to refinance indebtedness") issue no shares. The $700 million convertible senior notes of
  UGI Corporation (due June 2028) settle in cash up to principal and in cash or shares above it (10-K, Item 1A); no
  conversion event existed at 2025-09-30. No preferred stock outstanding.
- **Market cap:** $38.43 × 214.495M = **$8,243M**.
- **Sovereign for the earnings currency:** the reporting currency is USD (UGI International's euro and sterling results are
  translated); **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16 (`tools/run.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (filed 2025-11-21, accession `0000884614-25-000053`): Items 1 and 2,
  1A, 3, 5, 7 in full, the balance sheet, income statement, cash-flow statement, statement of equity, Note 22 (segments)
  and parts of the other notes; 10-K for FY2022 (`0000884614-22-000061`), FY2021 (`0000884614-21-000065`), FY2023
  (`0000884614-23-000104`) and FY2019 (`0000884614-19-000059`) for the segment tables and cash flows of the span; 10-Q
  for the quarter to 2026-06-30 (`0000884614-26-000052`); proxy statement DEF 14A filed 2025-12-17
  (`0001104659-25-122095`); 8-Ks of 2026-08-06 (`0000884614-26-000048`), 2026-08-17 (`0001104659-26-097884`) and
  2026-10-02 (`0001104659-26-113317`). **One figure cross-checked against the filed statement:** total assets at
  2025-09-30, $15,462 million in the `tools/run.py` ten-year table, equal to the filed consolidated balance sheet in
  `0000884614-25-000053`; operating cash flow FY2025 $1,227 million, capital expenditures $837 million and stock pay $18
  million, each equal to the filed cash-flow statement.
- `python tools/run.py UGI` arithmetic lines only (saved as `Test Runs/_research 2026-10-18 UGI/run_py_output.txt`):
  OCF less stock pay less capital spending, FY2023 $116M, FY2024 $378M, FY2025 $372M; depreciation and amortization
  $532M, $551M, $561M; stock pay $17M, $8M, $18M; finance-lease principal $1M to $3M a year (immaterial, shown beside). The
  tool reads only three years and does not deduct acquisitions or equity-method investments; the five-year owner cash used
  below is built from the filed cash-flow statements in the research folder (`owner_cash.py`), not from the tool's
  mean. Nothing the tool prints as a rule, a yield verdict or a floor was used (Part VII).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the first: a share is a business, bought for what the business will produce
over years, "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**; for a holding
company of a regulated utility, a midstream and marketing arm and two retail LPG distributors, that means reading the
parts' cash, not the quoted dividend. The market "just tells us prices" **[M2006-077]**, and no forecast of gas, propane or
interest rates is made here: "macro conclusions are — just never enter into the discussion" **[M2000-094]**. On who is paid
to tell: the filer features "adjusted net income" and "adjusted diluted earnings per share" ahead of the GAAP figures in its
MD&A (10-K, Item 7), and its incentive plans pay on adjusted EPS (proxy, below); that is the management's own telling and is
read as such. **Contrary evidence, written down as found** **[M1997-127]**: (1) LPG volumes are falling in both LPG parts
on the filer's own words: "continuing customer attrition" at AmeriGas and "continued structural conservation" in Europe
(10-K, Item 7); (2) AmeriGas, bought in full in 2019, has had $851 million of goodwill written off in two years (FY2023
$656M, FY2024 $195M); (3) the company has been selling parts in every year since FY2024, and from April 2026 is selling the
Electric Utility for $470 million (10-Q `0000884614-26-000052`, Note 5); (4) AmeriGas refinanced at 9.5% in May 2025
(10-K, Item 7), a lender's verdict on that part; (5) FY2023 carried $420 million of derivative collateral paid out of
operating cash (cash-flow statement, FY2025 10-K).

## THE STANDING RULE
Owning this, bought for cash and held unlevered in a size whose loss would not touch what the buyer has and needs, puts
the buyer at no risk of ruin: the rule governs the buyer's conduct, "never going to risk what we have and need for what we
don’t have and don’t need" **[M2012-081]**, "Never risk permanent loss of capital." **[L2023-005]**. The target's own debt
(about $7 billion) is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The parts, and which decides** (Q1's holding-company paragraph reads the whole by its parts; a part "matters" when it
decides under Q2's business-of-parts paragraph: more than half of five-year operating profit, or else the largest part).
Segment earnings before interest and taxes, as the filer's chief operating decision maker measures them (Note 22; FY2021
and FY2022 from `0000884614-22-000061`, FY2023 to FY2025 from `0000884614-25-000053`), $ millions:

| Part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Five-year sum | Share |
|---|---|---|---|---|---|---|---|
| Utilities (PA gas, WV gas from Sept 2021, PA electric) | 242 | 336 | 365 | 400 | 403 | 1,746 | 30.0% |
| UGI International (European LPG) | 317 | 254 | 234 | 323 | 314 | 1,442 | 24.8% |
| Midstream & Marketing | 190 | 269 | 291 | 313 | 293 | 1,356 | 23.3% |
| AmeriGas Propane (US retail propane) | 385 | 307 | 268 | 142 | 166 | 1,268 | 21.8% |
| Total of the four | 1,134 | 1,166 | 1,158 | 1,178 | 1,176 | 5,812 | 100% |

No part carries more than half; the largest, **Utilities, decides** (30.0%). The other three are carried to Q2's parts
table and, where open, to Q7 at no growth.

**The test applied to the deciding part.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years"
**[M2000-037]**. The key variables **[M1998-044]** of Utilities are: the rate base (PA Gas Utility $1.7 billion of
DSIC-eligible replacement spending planned for 2025 to 2029 under an LTIIP the PAPUC approved on 2024-12-05; Mountaineer
$445 million planned for 2026 to 2030 under its IREP filing), the returns the regulators allow on it (the last PA gas case
settled on 2025-09-11 at a $69.5 million annual increase against $110 million asked), the customer count (PA Gas Utility
about 694,000, Mountaineer about 210,000; "more than 9,000 residential heating customers" added in FY2025, over half
converted from oil and electricity), and the weather, now dampened by weather-normalization riders in both states (10-K,
Item 1, `0000884614-25-000053`). Gas costs pass through: "permitted to recover all prudently incurred costs of natural
gas" (Item 1). These variables are written down years ahead by the insiders themselves (five-year LTIIP and IREP plans
filed with the regulators), which is test 5 passed the other way **[M2000-105]**. The product is plain; "What is important
is that I understand the economic dynamics of the industry" **[M2011-014]**, and here the dynamics are those of a
franchise monopoly paid a regulated return on what it invests. The past statements do tell the future ones in this part
**[M2008-033]**: segment profit has followed the rate base up each year (242, 336, 365, 400, 403).

**What could put it outside.** Change: electrification policy is the slow threat to a gas distributor; the 10-K names
heat pumps and EU building rules for the LPG parts and "competition from other energy sources" for the US gas business
(Item 1A), and states that "Natural gas generally benefits from a competitive price advantage over oil, electricity and
propane" (Item 1). No rule in Pennsylvania or West Virginia restricting gas connections is named in the filing; the
change is slow, not fast, and Q2 owns it. The whole company is changing shape quickly by sale (see Foundations), which
makes the ten-year picture of the whole harder than that of the deciding part; that is weighed at Q6 (the use of the money)
and does not move the deciding part out of the circle. M&M's commodity marketing carries derivatives (FY2023 net losses on
commodity derivatives not associated with current-period transactions of $236 million in M&M and $1,402 million in UGI
International, Note 22 of the FY2025 10-K), but the international energy-marketing book was exited in FY2024 and M&M does
not decide; it is carried to Q9 as an exposure. A commodity dependence is "never by itself a STOP at Q1 or Q2" (Q2,
A commodity business) and the speakers buy off the figures, "if you can’t make a decision on something like PetroChina off
the figures, forget about going further" **[M2008-069]**.

**Doubt test.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. I
have no doubt that a Pennsylvania and West Virginia gas distribution franchise can be understood from its filings and its
regulators' orders; the doubts run to the LPG parts' decline and the derivatives in M&M, which are parts that do not
decide. [M2023-031] stays OPEN against the by-parts reading, as the framework says.

**VERDICT: IN.** The deciding part (Utilities, 30% of five-year segment profit) is a regulated gas distributor whose key
variables are filed with and set by its regulators years ahead **[M2012-065]**, **[M1998-044]**, **[M2011-014]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**Competitors, by the brief's rule.** The 10-K names no rival by name: it names categories ("other large propane
marketers, including other full-service marketers, and thousands of small independent operators"; "supermarket chains"
in France; "other midstream operators"; "fuel oil dealers"), and the companies it names (Enterprise Products Operating
LLC, Crestwood Services LLC, Texas Eastern, Columbia Gas Transmission and the other pipelines) are its suppliers, not its
rivals (Item 1, `0000884614-25-000053`). **CONVENTION of this run:** the three comparators are chosen by the analyst, one
for the deciding part's field and one for its nearest neighbour in the same state, and one for the largest LPG part that
has a filing US rival: National Fuel Gas (NFG; its Utility segment serves western New York and northwestern
Pennsylvania), Essential Utilities (WTRG; its Regulated Natural Gas segment is Peoples, western Pennsylvania), and
Suburban Propane Partners (SPH; US retail propane, AmeriGas's nearest listed rival). Rationale: the 10-K names no rival
that files, and these three file with the SEC and serve the same customers in the same regions or the same trade. Flagged
as not filing: the "thousands of small independent operators" and the farm and electric cooperatives (US propane), and
UGI International's European rivals, which the 10-K does not name.

**The castle tests, on the deciding part (Utilities).**
- *The attacker with money* **[M2011-015]**: PA Gas Utility "is the only regulated gas distribution utility having the
  right, granted by the PAPUC or by law, to provide gas distribution services" in substantially all its territories, under
  certificates of public convenience and "grandfather rights" with eminent domain and the right to use the streets;
  Mountaineer holds the same in West Virginia (Item 1). An attacker with any sum cannot lay a second distribution network
  without a certificate the regulator does not grant. The bypass threat is named and limited: 17 large industrial
  customers can take service direct from interstate pipelines, 15 under contracts beyond FY2026 (Item 1).
- *Pricing power and the agony before a rise* **[M2005-020]**: none of its own; the price is the regulator's. The last PA
  gas case asked $110 million and received $70 million (Item 7). The rows class a regulated return as fair, not rich:
  "there’s no way we get rich on our utility investments. But there’s no way we get poor, either" **[M2009-104]**.
- *The low-cost position and the customer's choice*: within the franchise the competitor is another fuel, not another
  utility; the filer states "Natural gas generally benefits from a competitive price advantage over oil, electricity and
  propane", and more than 55% of the 9,000 residential heating customers added in FY2025 converted from oil and electricity
  (Item 1). PA Gas Utility had "nearly 655,000" customers in 44 counties in the FY2019 10-K (`0000884614-19-000059`) and
  about 694,000 in 46 counties in FY2025: the castle has widened slowly **[M1999-108]**.
- *What could destroy, modify or reduce it* **[M2000-014]**: (1) the regulator: "I did not anticipate or even consider
  the adverse developments in regulatory returns" **[L2023-011]**; the filer's own Item 1A names rates not approved and
  "regulatory initiatives aimed at increasing competition within our industry"; (2) electrification and building rules,
  named by the filer for Europe and as "competition from other energy sources" for the US gas business; slow, and "slow
  change can be much harder to perceive" **[M2014-038]**; (3) one event: the West Reading explosion of 2023-03-24 (seven
  dead; the NTSB found a UGI Utilities service tee degraded by heat from a third party's steam pipe; litigation in
  discovery, no range of loss estimable, Item 7), carried to Q9.

**The parts table** (Q2's business-of-parts paragraph; segment EBIT shares from Q1's table):

| Part | Share of five-year segment EBIT | Castle, on the filings | Decides |
|---|---|---|---|
| Utilities | 30.0% | Regulated franchise monopoly on distribution in its territories; customer count rising; return set by regulator | **Yes (largest part)** |
| UGI International | 24.8% | Leading LPG distributor in France, Belgium, Denmark, Luxembourg; retail gallons 792M (FY2021) to 698M (FY2025), down 12%, "continued structural conservation"; EU and national rules mandating replacement of fossil heating; four country businesses and Italy sold FY2025 to FY2026. Being filled in slowly | No; open, carried to Q7 at no growth |
| Midstream & Marketing | 23.3% | Mixed: FERC-regulated storage and two pipelines at cost-based or market rates; gathering where "competition in the midstream segment is significant"; retail marketing sold "principally on the basis of price, customer service and reliability" | No; not judged in full |
| AmeriGas Propane | 21.8% | Largest US retail propane distributor, but retail gallons 968M (FY2021) to 733M (FY2025), down 24%, "continuing customer attrition"; segment EBIT 385 to 166; goodwill written down $851M in two years. Open on the evidence (below) | No; open, carried to Q7 at no growth |

Gallons: FY2022 10-K (`0000884614-22-000061`) for FY2021 and FY2022, FY2023 10-K (`0000884614-23-000104`) for FY2023, FY2025
10-K for FY2024 and FY2025.

**The competitor row** (same metric from each filer's own segment note: segment net income as the filer states its
segment profit, over segment assets; for SPH, which reports one business, operating income over total assets against
AmeriGas's segment EBIT over segment assets):

| Filer and part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Source |
|---|---|---|---|---|---|---|
| UGI Utilities, NI / segment assets | 144/4,859 = 3.0% | 206/5,354 = 3.8% | 219/5,691 = 3.8% | 237/5,963 = 4.0% | 237/6,434 = 3.7% | `0000884614-22-000061`, `0000884614-25-000053` (Note 22) |
| NFG Utility, NI / segment assets | 54.3/2,148 = 2.5% | 68.9/2,299 = 3.0% | 48.4/2,248 = 2.2% | 57.1/2,399 = 2.4% | 83.2/2,534 = 3.3% | `0000070145-22-000034`, `0000070145-25-000039` |
| WTRG Regulated Natural Gas, NI / segment assets (calendar years) | 148.2/5,960.6 = 2.5% | 185.3/6,528.7 = 2.8% | NI 200.6 | NI 293.6 | NI 267.4 | `0001562762-23-000064`, `0000078128-26-000050` (segment assets not in the 2025 note; ratio not computed) |
| AmeriGas Propane, EBIT / segment assets | 385/4,485 = 8.6% | 307/4,332 = 7.1% | 268/3,415 = 7.8% | 142/3,051 = 4.7% | 166/2,914 = 5.7% | `0000884614-22-000061`, `0000884614-25-000053` |
| Suburban Propane, operating income / total assets | 213/2,052 = 10.4% | 206/2,104 = 9.8% | 207/2,270 = 9.1% | 171/2,273 = 7.5% | 206/2,296 = 9.0% | XBRL companyfacts; operating income cross-checked to the FY2025 (`0001193125-25-298630`) and FY2022 (`0000950170-22-025646`) 10-K text |

SPH's retail propane gallons: 419.8M (FY2021) to 400.5M (FY2025), down 5% (the same two 10-Ks), against AmeriGas's 24%.

**The field's returns over the last full cycle, judged in words.** The gas distribution field earns ordinary returns:
segment net income of 2% to 4% of segment assets for all three filers over five years, UGI's Utilities at the top of that
band. A moat is what "protects excellent returns on invested capital" **[L2007-004]**, and these are not excellent; but
the paragraph on the standing castle that protects only ordinary returns names its exception, "A return set by a regulator
is the exception, carried to Q3 as a second best" (Q2, What it rules OUT, citing **[M2009-104]**, **[L2009-012]**). The
deciding part's return is set by the PAPUC and the WVPSC, so the exception applies and the question passes to Q3.
In the propane trade the comparison is against AmeriGas: the low-cost or better-run operator kept its profit and most of
its volume while AmeriGas lost a quarter of its gallons and more than half its segment profit; "one competitor is
frequently enough to ruin a business" **[M2012-108]**, and in an unregulated commodity trade "a company must lower its
costs to competitive levels or face extinction" **[L1994-035]**. Had AmeriGas decided, it would close OUT on that evidence.
It does not decide, and is carried to Q7 at no growth.

**Contrary evidence written down** **[M1997-127]**: the deciding part is only 30% of the profit; the two LPG parts (47%
together) are shrinking in volume, and one of them is open on the evidence. Under the convention the file closes on the
deciding part; the weight of the open parts falls on Q7.

**VERDICT: IN**, on the deciding part, as the regulated exception: a franchise monopoly no attacker can cross
**[M2011-015]**, whose return is set by regulators, fair but not rich **[M2009-104]**, **[L2009-012]**, carried to Q3 as a
second best; threats from regulation **[L2023-011]** and slow electrification **[M2014-038]** are written down and carried.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
Arithmetic in `Test Runs/_research 2026-10-18 UGI/scripts/owner_cash.py`, from the filed statements (FY2021 and FY2022
from `0000884614-22-000061`, FY2023 to FY2025 from `0000884614-25-000053`).

**What it earns on the capital it needs** **[M2010-090]**, measured on tangible assets **[M2011-060]**: the four segments'
EBIT over total assets less goodwill and intangibles was 9.2%, 8.7%, 9.7%, 10.0% and 9.6% in FY2021 to FY2025, pre-tax and
before interest; on total assets, goodwill included because it was paid for **[M2011-060]**, 6.8% to 7.8%. That is a
pre-tax return near 10% on the tangible capital and under 8% on what was paid, in a business that carries about $7
billion of debt against $4.8 billion of equity (FY2025 balance sheet); it is not a return that the rows call high.

**What the added capital earned.** Over FY2021 to FY2025 the company spent $4,101M on property, $648M on acquisitions
(Mountaineer, $540M including $140M of assumed debt, FY2021; UGI Appalachia and renewable projects, FY2022) and $388M in
equity-method investments (mostly renewable gas projects), and took in $293M from businesses and assets sold (FY2023 to
FY2025); net of the $2,664M of depreciation charged, $2,180M of capital was added. The four segments' EBIT went from
$1,134M to $1,176M: $42M more a year on $2,180M added, about 2% pre-tax. Revenue fell from $7,447M to $7,287M. By parts:
- **Utilities**: segment assets $4,859M to $6,434M (+$1,575M), EBIT $242M to $403M (+$161M), about 10% pre-tax on the
  added assets, and flattered, since FY2021's EBIT carries one month of Mountaineer while its assets carry all of it. The
  rows' description fits it: "To earn more, their owners must invest more" **[L2011-019]**; the incremental return is
  decent and regulated, the second best the rows accept, "still a good choice [...] It’s not as good as the best choice"
  **[M2018-055]**, on the condition of "decent returns on the incremental sums they invest" **[L2009-012]**. Much of the
  spending is compulsory replacement (cast iron by March 2027, bare steel by September 2041, under a PAPUC agreement; Item
  1), the kind of reinvestment "just in order to stand still" that the speakers avoid **[M1997-016]**, though here the
  regulator pays a return on it.
- **AmeriGas Propane**: capital spending of $559M against $883M of depreciation over five years, and segment EBIT fell
  from $385M to $166M; less capital went in and much less came out.
- **UGI International**: capital spending $523M against $608M of depreciation; EBIT $317M to $314M on volumes down 12%,
  helped by the exit of the loss-making energy-marketing book.
- **Midstream & Marketing**: capital spending $475M plus most of the acquisitions and equity investments; EBIT $190M to
  $293M.

**The growth arithmetic.** The company as a whole put about $2.2 billion of net new capital in and earned no more on it in
aggregate: the Utilities' growth was bought at a regulated return, and the LPG parts' decline gave it back. The rows' own
words for the aggregate: "we’re not earning a higher rate of return on capital than we were when we started. We just put
way more capital into the business" **[M2023-081]**; and the shape they warn against, a business forced to keep investing
"at a very low rate of return" **[M1998-081]**. "cash-consuming businesses, by their nature, are unattractive unless the
cash they consume gets to earn a reasonable return" **[M2012-057]**. Depreciation is not enough to stand still at the
Utilities (capex $556M against $178M of depreciation in FY2025), which is the BNSF case: owner cash "will regularly fall
considerably short" of reported earnings **[L2023-009]**.

**Maintenance and growth, the guess the filing allows** **[M2000-144]**, **[L1999-024]**: the 10-K splits capital spending by
segment but not into maintenance and growth. The guess, stated: AmeriGas and UGI International spend below their
depreciation, so all their spending is taken as maintenance; Utilities' mandated replacement (the LTIIP, about $1.7
billion over 2025 to 2029, so about $340M a year, and Mountaineer's IREP, $445M over 2026 to 2030, about $89M a year) is
taken as maintenance, since it keeps the system in place even though the regulator pays a return on it; M&M's maintenance
is guessed at its depreciation ($81M in FY2025). On FY2025 segment figures that is $81M + $93M + about $429M + $81M = about
$684M of maintenance against $844M of capital spending, about 81%; the rest, and all purchases, is growth spending. This
guess feeds Q7's central case.

**WEIGHS AGAINST.** The deciding part earns a decent regulated return on added capital and is a second best **[M2018-055]**,
**[L2009-012]**; the company as a whole added about $2.2 billion of net capital in five years and earned about 2% pre-tax
more on it **[M1998-081]**, **[M2023-081]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL vintages
`0000884614-16-000067` to `0000884614-25-000053`; FY2025 and FY2024 read on the filed statement; June 2026 from the 10-Q),
$ millions:

| Year-end | Assets | UGI equity | Goodwill | Intangibles | Cash | Receivables | Inventory | Debt on the face | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 10,847 | 2,851 | 2,989 | 580 | 503 | 552 | 210 | 4,087 | 1,841 |
| 2018 | 11,981 | 3,681 | 3,160 | 514 | 453 | 752 | 318 | 4,590 | 2,611 |
| 2019 | 13,347 | 3,818 | 3,456 | 709 | 447 | 641 | 230 | 6,600 | 2,653 |
| 2021 | 16,723 | 5,522 | 3,770 | 583 | 855 | 880 | 469 | 6,816 | 4,081 |
| 2022 | 17,575 | 6,066 | 3,612 | 500 | 405 | 1,127 | 665 | 7,000 | 4,841 |
| 2023 | 15,401 | 4,386 | 3,027 | 443 | 241 | 878 | 433 | 7,249 | 3,027 |
| 2024 | 15,098 | 4,345 | 2,871 | 391 | 213 | 709 | 411 | 7,143 | 2,978 |
| 2025 | 15,462 | 4,777 | 2,852 | 328 | 335 | 714 | 385 | 7,134 | 3,334 |
| Jun 2026 | 15,631 | 5,213 | 2,780 | 289 | 476 | 768 | 352 | 7,049 | 3,777 |

(2017 and 2020 in the tool's table, not repeated: they lie between their neighbours.) What moved and why. **Debt** rose from
$4.1 billion to $7.1 billion, the step in 2019 being the year UGI bought out the AmeriGas public unitholders (the FY2019
10-K, `0000884614-19-000059`) and the later steps the Mountaineer purchase and the utility programme; it has not fallen
since 2022 although equity has. **Goodwill** rose to $3.8 billion with the 2019 merger and Mountaineer and then fell by $0.9
billion through the AmeriGas impairments ($656M FY2023, $195M FY2024) and the sales; the price paid for AmeriGas was not
earned. **Retained earnings** rose to $4.8 billion in 2022 and fell to $3.0 billion in 2023 on the $1.5 billion loss of that
year; the 2021 and 2022 figures had carried large unrealized derivative gains that 2023 reversed (operating cash flow
reconciliations: "Changes in unrealized gains on derivative instruments" of $(1,398)M FY2021 and $(648)M FY2022, and
$1,682M FY2023), so the peak in the equity line was paper. **Receivables and inventory** rose with the 2022 commodity
prices and came back; receivables were 9.8% of revenue in FY2025 against 11.2% in FY2022, and inventory is not building
against sales. Cash is small and mostly at the subsidiaries ($214M at the parent level, Item 7). What the figures cannot
say: how much of the utility plant is replacement that only keeps the system in place (Q3's guess), and what the West
Reading litigation will cost (no range estimable, Item 7).

**The real costs.**
- *Depreciation* ($561M FY2025) is a true cost **[R1996-023]**, and at the Utilities it falls short of what keeps the
  system in place (capex $556M against $178M of segment depreciation in FY2025); "You should also subtract something to
  reflect BNSF's inadequate depreciation charge" **[L2015-004]** applies by analogy; owner cash below deducts capital
  spending, not depreciation, for that reason.
- *Stock pay* is small ($8M to $21M a year) and is deducted.
- *The recurring "one-time"*: every year of the span carries charges the filer asks the reader to set aside: losses on
  disposals of businesses ($221M FY2023, $95M FY2024, $36M FY2025, $42M in the nine months to June 2026), restructuring
  ($56M after tax FY2024), an "AmeriGas operations enhancement for growth project" ($24M FY2023, $25M FY2024), goodwill
  impairments ($656M, $195M), exit costs of the European energy-marketing book ($69M after tax FY2024), losses on debt
  extinguishment every year (Note 22 of `0000884614-25-000053`; 10-Q `0000884614-26-000052`). "to tell owners year after
  year, "Don't count this," when management is simply making business adjustments that are necessary, is misleading"
  **[L2016-007]**. Owner cash below is built from operating cash flow and investing cash flow as filed, so these charges'
  cash parts are counted.
- *EBITDA in the filer's own mouth*: not featured in the 10-K or the releases read; the term appears only as the goodwill
  test's input and in a covenant (Mountaineer's EBITDA-to-interest covenant, 8-K `0001104659-26-113317`).
- *The featured adjusted figure*: the MD&A opens its results with "adjusted net income attributable to UGI Corporation"
  and "adjusted diluted earnings per share" (FY2025 $728M against GAAP $678M; FY2024 $658M against $269M), and the releases
  lead with "record adjusted earnings per share that exceeded our revised guidance range" (release of 2025-11-20) and
  reportable segments' EBIT. "a management that regularly attempts to wave away very real costs by highlighting "adjusted
  per-share earnings" makes us nervous" **[L2016-006]**. In fairness the reconciliation is full and its largest adjustment
  (marks on derivatives that hedge future transactions) is economically argued.
- *Guidance*: the company issues adjusted EPS guidance (FY2026 $2.90 to $3.15 on 2025-11-20, cut to $2.75 to $2.90 on
  2026-05-06, reaffirmed 2026-08-05; releases `0000884614-25-000051`, `0000884614-26-000018`, `0000884614-26-000048`),
  and its FY2025 release celebrates beating a revised range. The rows: "the scourge of earnings "guidance" and the desire
  of CEOs to "hit the number."" **[L2019-006]**; "we become downright incredulous if they consistently reach their
  declared targets" **[L2002-041]**. Here the targets are not consistently reached (FY2026 was cut), which is the opposite
  of the tell, but the habit of guiding and featuring is there.

**Confusion or suspicion?** The accounts are long and the GAAP line swings by billions on derivative marks, but every swing
is reconciled and the cash statements are plain; I can recast what it earns, so this is not "when the accounting confuses
you" **[M1995-063]**. The tells that live in the accounts **[M1995-064]** were looked for: prepaid and other current assets
are flat ($102M to $113M prepaid, FY2024 to FY2025), inventory is not out of line with sales, reserves do not move with an
offering, and the auditor was changed by a competitive tender with no disagreements (8-K `0001558370-24-013848`: KPMG
appointed for FY2025, EY dismissed after its FY2024 report). The pension plans are nearly fully funded ($3M short).
**No STOP.**

**Recast earnings for Q7.** Owner cash after every real cost, from the filed cash-flow statements (not a net-income proxy,
operator rule 5): operating cash flow less stock pay, less capital spending, less acquisitions and equity-method
investments, plus proceeds from businesses and assets sold. Equity-only, $ millions: FY2021 308, FY2022 (392), FY2023 (9),
FY2024 379, FY2025 504; five-year average **$158M**. Before purchases (capital spending only): 770, (103), 116, 378, 372,
average $307M. The working-capital swings of the commodity spike (collateral received $472M FY2021, paid $420M FY2023;
receivables and inventory built in FY2022 and released in FY2023) are inside the five-year window and largely net out
across it.

**VERDICT on the accounts: no STOP; WEIGHS AGAINST.** The featured adjusted figure **[L2016-006]**, the guidance
**[L2019-006]** and the yearly "don't count this" charges **[L2016-007]** are recorded here as a weighing **[M1994-018]**
and carried to Q5; the recast earnings feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**Who.** Robert (Bob) Flexon, President and CEO from 2024-11-01 (formerly UGI's CFO, then CEO of Dynegy 2011 to 2018,
10-K Part III); before him Mario Longhi as interim CEO from December 2023 (now non-executive chair); the Chief Operations
Officer left on 2024-12-31 and the post was eliminated (an involuntary termination, $7.1 million of "All Other
Compensation"); a new AmeriGas president from 2024-12-30; the General Counsel resigned effective 2026-07-03 (8-K
`0001104659-26-067541`). Proxy DEF 14A `0001104659-25-122095`.

**The two yardsticks** **[M1994-008]**. *How they ran it, against the hand dealt*: the prior management bought out AmeriGas
(2019) and then lost a quarter of its retail gallons in four years while its listed rival lost a twentieth (Q2), wrote off
$851 million of the goodwill paid, built a European energy-marketing book that swung by $1.4 billion of derivative marks
(FY2023) and was exited at a cost (FY2023 $221 million loss on disposal, FY2024 $69 million after tax), and grew the
regulated utility steadily. Since late 2024 the new management has sold the non-core LPG countries, Hawaii, the UK
cylinders and (signed) the Electric Utility, refinanced AmeriGas, and lifted AmeriGas segment EBIT from $142 million to
$166 million; it describes AmeriGas as "the transformation is taking hold" (release of 2026-08-05,
`0000884614-26-000048`). The record before 2024 weighs against ability; the record since is short. *How they treat the
owners*: read in the proxy, "see how they treat themselves versus how they treat the shareholders" **[M1994-009]**: the
CEO's FY2025 pay was $8.99 million (salary $1.02 million, sign-on cash $0.30 million, stock awards $5.43 million, bonus
$1.84 million); bonuses paid 129.4% to 143.7% of target on adjusted EPS, safety, cost and free-cash-flow goals, with
committee discretion "to adjust Adjusted EPS for extraordinary items"; pay targeted "within a range of 85% to 115% of the
50th percentile of the survey data" (proxy, CD&A). These bear on Q6, Part B.

**The habits carried from Q4**, read with the integrity record **[M2004-067]**: the featured adjusted figure
**[L2016-006]**, adjusted EPS guidance cut once and reaffirmed **[L2019-006]**, and a release that celebrates beating a
revised range. Against them: the reconciliations are complete, the guidance cut of May 2026 was announced plainly, the
AmeriGas impairments and the energy-marketing losses are stated in the GAAP accounts and the MD&A in so many words, the
auditor was changed by tender with no disagreements, no restatement, no securities class action and no regulatory finding
of dishonesty was found in the 10-K's Note 16, Item 3 or the 10-Q (text search for class action, securities law,
derivative suit, consent order and penalty; the consent orders found are environmental). The NTSB placed the West Reading
cause in a third party's steam pipe and recommended an inventory of plastic assets in high-temperature environments; the
company "cooperated with the investigation" (Item 7). The rows separate preoccupation, "a negative" that "we can’t afford
to use [...] as a total exclusionary factor" **[M1994-018]**, from the reports that dance or the figures obscured with a
purpose; I find the first, not the second. "If you’ve got doubts, forget it." **[M2013-088]**: my doubts are about ability
and pay design, not about honesty.

**Love of the business** **[M2000-098]**: no direct evidence either way for a hired chief executive of eighteen months; he
was not a seller. **How they talk about mistakes** (test 4): the 10-K and releases speak of "portfolio optimization" and
"transformation", not of a mistake made in AmeriGas; the speakers were nervous where "mistake" or "wrong" were forbidden
words **[L2024-003]**. Weighs mildly against.

**VERDICT on integrity: IN** (no fact found that raises doubt about honesty; the Q4 habits are recorded as a weighing
**[M1994-018]**, **[M2013-088]**). **Ability WEIGHS AGAINST**: the record of the last full span is the AmeriGas merger and
its decline, the energy-marketing book and three chief executives in two years **[M1994-008]**; the business is not one that
"doesn’t require good management" in its LPG parts **[M1996-037]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**, **[M2011-072]**: over FY2021 to FY2025 GAAP net income was $1,985M
  (1,467 + 1,073 − 1,502 + 269 + 678) and dividends $1,526M, so $459M was kept, about $2.15 a share on about 213 million
  shares. The quote went from $32.98 (2020-09-30) to $33.26 (2025-09-30) (aggregator closes, flagged): about $0.28 of
  market value for each $2.15 kept. On owner cash the test is worse: owner cash after all spending was $790M over the five
  years against $1,526M of dividends, so the dividend was paid in part from borrowing and asset sales (net debt on the face
  rose from $6.0 billion at FY2020, less cash, to $6.8 billion at FY2025). Over ten years the quote fell from $44.86
  (2016-10-17) to $38.43 while retained earnings rose $1.5 billion. The presumption the rows raise after "three or four
  years" **[M1998-110]** is strong here: retention has not delivered a dollar of value per dollar kept.
- *Buybacks*: 1.0 million shares for $33M in FY2025 (500,000 in September 2025 at $33.05), $22M FY2023, $38M FY2022, 0.6
  million shares for $23M in the nine months to June 2026; the programme authorises a number of shares (8 million over four
  years, renewed February 2026) and names no price (10-K Item 5; 10-Q). A programme with no stated price weighs against
  "unless the prices actually paid sit at or below the bottom of the Q7 range" (Q6, The buyback with no stated price);
  **[L2016-002]**, **[L1999-023]**. *Written back from Q7 (2026-10-18, committed with Q7):* the bottom of Q7's range is
  $12.85 a share on the all-equity basis ($21.05 equity-only); the shares were bought at about $33 in FY2025 ($33.05 in
  September 2025) and at about $38 in the nine months to June 2026 ($23M for 0.6 million shares), every purchase above the
  bottom on either basis, and above the top of the all-equity range ($33.00) in FY2026. The buyback line **weighs
  against**: "Continuing shareholders are hurt unless shares are purchased below intrinsic value." **[L2011-003]**.
- *Issuance and deals*: the 2019 buyout of the AmeriGas public units (outside the five-year window; paid mostly in UGI
  shares with a cash part, FY2019 10-K) is the deal whose goodwill was later written down by $851 million; the 2021 equity
  units ($213M, settled in FY2024 into common shares, statement of equity) and the 2024 convertible notes ($700M, cash up
  to principal) are the issuance of the span; shares outstanding rose from about 209 million (FY2020 basic) to 214.5
  million. No all-stock acquisition in undervalued stock inside the span, so Part A's one STOP **[L2009-019]** does not
  apply. The portfolio sales of FY2024 to FY2026 took in about $293M (FY2023 to FY2025) plus about $145M (FY2026, central
  Europe and Austria) plus $470M signed for the Electric Utility, mostly at losses to book.

**Part A WEIGHS AGAINST**: a dollar kept has not become a dollar of value **[R1995-009]**, **[M1998-110]**, and the dividend
has exceeded the owner cash after all spending.

**Part B, the pay, the board and the owners.**
- *Pay tied to what the person controls* **[M2003-019]**: the corporate officers' annual bonus is 40% adjusted EPS "(as
  adjusted for bonus purposes)", 30% operating cost, 20% free cash flow, 10% safety, with discretion to adjust EPS for
  extraordinary items; the AmeriGas and Energy Services presidents' bonus is 60% on their own unit (70% of that on the
  unit's EBIT, 15% cost, 15% safety) and 40% on the company (proxy, Annual Bonus Awards). The unit split is what the row
  asks for; the EBIT measures carry no charge for the capital each unit employs, and none was found in the plan
  descriptions. The FY2025 PSUs pay on absolute TSR from the price of 2024-11-01 ($23.46 close, aggregator,
  flagged), annualised and measured each year, with "a named executive officer’s payout is determined upon the highest
  goal achieved in any measurement period" (proxy, PSU Metrics): a rise in any one year is kept even if it is lost later.
  That is a ride on the quote **[M2000-062]**, and the best-of-three-years design leans to "heads I win, tails you lose"
  **[L1994-020]**, a plan that tends to "payoff no matter what happens" **[M1999-018]**.
- *The ratchet*: pay set at the 50th percentile of survey data **[L2005-015]**, **[M2012-095]**.
- *The board*: ten directors, nine independent (10-K Item 1); a non-executive chair who was the interim CEO; hedging and
  pledging prohibited; stock ownership guidelines; a clawback on restatement (proxy). These count for the board.
- *The owners told*: full reconciliations, but guidance and a featured adjusted figure (Q4).

**Part B WEIGHS AGAINST**: pay on adjusted EPS and on a best-of-years TSR from a low base **[M2003-019]**, **[L1994-020]**,
set by survey percentile **[L2005-015]**; the speakers rank the person above the plan **[M2007-006]**, and the plan is
weighed, not closed on.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
credited only "for whatever net cash is left every year" **[M1998-080]**, discounted at the long government rate
**[L2000-021]**: 5.43% (Step 0). Arithmetic in `Test Runs/_research 2026-10-18 UGI/scripts/q7_range.py` (output saved
beside it as `q7_output.txt`), inputs from the filed cash-flow statements (`0000884614-22-000061`, `0000884614-25-000053`)
and the 10-Q balance sheet (`0000884614-26-000052`). *(Resume note: the killed session left this script uncommitted; it was
read and checked line by line against `owner_cash.py` and the filings, kept, and changed in one respect, the tax, below.)*

**The inputs.**
- *Owner cash* (Q4's recast, operator rule 5): operating cash flow less stock pay less capital spending less acquisitions
  and equity-method investments plus proceeds of businesses sold. Five-year averages FY2021 to FY2025, $ millions:
  operating cash flow 1,143; stock pay 16; capital spending 820; net purchases 149; so equity-only owner cash after all
  spending **$158M**. Interest paid averaged $345M; added back after tax it is $273M.
- **CONVENTION of this run (the interest add-back):** cash interest paid is added back at the 21% US federal statutory
  rate. Rationale: the all-equity basis needs owner cash before interest and after the company's own tax, the filer does
  not state the tax shield of its interest, and the federal rate is the one stated in its own reconciliation; adding the
  4.6 points of state tax as well would lower the add-back by about $16M a year, which moves no case across the floor.
- *All-equity owner cash* (Q7, On what the floor is earned; **[L2017-004]**): $158M + $273M = **$431M** after all spending;
  **$735M** after maintenance only (Q3's guess: about 81% of capital spending, $665M of the $820M average, is maintenance;
  **[M2000-144]**, **[L1999-024]**); $867M on the depreciation variant, shown beside.
- *Net debt* at 2026-06-30 (latest filed balance sheet): current maturities $18M + short-term borrowings $336M + long-term
  debt $6,695M, less cash $476M = **$6,573M** (restricted cash of $47M left out; operating leases left out, said so). The
  10-Q states no subsequent event that changes it; the 8-Ks after it (2026-08-17, 2026-10-02) place notes "to refinance
  indebtedness". Market value $8,243M; market value plus net debt **$14,816M**. Cash was $335M at 2025-09-30 and $350M at
  2025-06-30 (same 10-Q), so the June 2026 figure is about $130M above its recent level; not adjusted.
- *Whose tax.* The company paid little cash tax in the window (FY2023 to FY2025 cash taxes $(17)M, $80M, $55M; effective
  rate 2.6% in FY2025). The 10-K's reconciliation puts 12.7 points of FY2025's gap in investment tax credits on renewable
  gas projects, a credit that ends; but the deferred tax asset for unused investment tax credits rose from $26M to $116M
  over FY2025 (10-K tax note), so the credits were mostly carried forward, not used against cash tax in the window. The
  rest of the gap is accelerated tax depreciation (excess book over tax basis of plant, $1,051M) and valuation-allowance
  releases. Under Q7's tax convention the run therefore charges no extra tax to the window's cash and adds the unused
  credits, $116M, as the shelter's value, undiscounted since they are expected to be used within a few years.
  *(The killed session's draft charged a further $22M a year for the credits; with it every value below is about $1.90 a
  share lower; shown in the output, it moves no case across the floor.)* A further confession: the window's averages
  include the cash of parts since sold (Hawaii, the UK cylinders, Italy, Austria, four central European countries, the
  European energy-marketing book) while net debt already holds their proceeds; the sold parts' own owner cash is not filed
  separately, so this flatters the range by an amount the filings do not let me state.

**The range, by Q7's convention and its specifics.**
- *(a) Cycles.* The commodity spike of FY2021 to FY2023 sits inside the window: collateral received $472M in FY2021, paid
  $420M in FY2023, working capital built in FY2022 and released in FY2023 (Q4). Netted both ways the five-year average moves
  by about $10M a year, so neither end year sets a distorted base; the literal window is the base, and it is the base shown.
- *Growth shown, (b) and (f).* The all-equity owner-cash series after all spending changes sign (FY2021 to FY2025: 543,
  (139), 253, 697, 800), so the growth is measured between the halves: $202M to $749M, about 55% a year, which is the kind
  of rate the rows call "a breathtaking, but meaningless, growth rate" **[L2005-003]**, made by the FY2022 working-capital
  build. Carried ten years it would require owner cash of about $63 billion against sales of $7.3 billion, where the
  highest share of sales the business earned in the window was 11.0%; by (f) the rate is cut to the business's own sales
  growth over the same window, $7,447M to $7,287M, **minus 0.54% a year** **[M1999-067]**. (Segment EBIT grew 0.9% a year
  over the same years; the shown rate is the sales rate, as (f) directs.) By (b) a negative rate is carried as negative and
  makes the bottom; the no-growth case is the top **[M2006-058]**.
- *(c) Acquisitions.* Net purchases over the window were $743M against half of owner cash before purchases, $767M: just
  under the serial-acquirer line, so the default pair applies, purchases deducted and the total growth credited; the
  purchases stop after year ten. The filer reports no organic growth figure, so the organic pair cannot be built as the
  convention defines it; on owner cash before purchases at no growth it is $19.1 a share (expected return 3.9%), beside.
  No merger (a deal paid in shares) inside the window. **The signed, unclosed deal**: the Electric Utility sale for $470M
  (April 2026; closing expected in the second quarter of FY2027; 10-Q Note 5). Its own owner cash is not filed separately,
  so valued as if closed on the most favourable reading (proceeds off net debt, the cash it would take away credited at
  nothing) it adds at most $2.19 a share: range $15.04 to $35.19, expected return at the price 3.6% to 5.2%. Beside only;
  the box is decided on the central figure.
- *(d) Working capital* is counted: owner cash is built from operating cash flow after its working-capital changes.
- *(e) Maintenance central, and the inversion.* Q3 found the growth bought earning about 2% pre-tax on the net capital
  added, so the growth bought is worth less than its cost: the maintenance-only no-growth case is the **top**, and the
  growth case (all spending, the shown decline) is the **bottom**; "growth can destroy value" **[L2000-023]**.
- *No rate above the discount rate* is carried anywhere **[M1997-095]**.

**The figures** (per share, all-equity: the business's value at the rate, plus the $116M of credits, less net debt of
$6,573M, over 214.495 million shares):

| Case | Owner cash base | Growth | Value a share at 5.43% | At 10% | Expected return at $38.43 |
|---|---|---|---|---|---|
| **Top**: maintenance only, no growth | $735M | 0 | **$33.00** | $4.16 | 5.0% |
| **Bottom**: all spending, the shown decline, purchases stop after year ten | $431M | −0.54% | **$12.85** | −$8.07 | 3.5% |
| beside: bottom with growth spending also stopping after year ten | $431M, then maintenance only | −0.54% | $19.90 | −$5.56 | 4.1% |
| beside: all spending, no growth | $431M | 0 | $14.41 | −$7.34 | 3.6% |
| beside: depreciation variant, no growth | $867M | 0 | $44.32 | $10.31 | 5.9% |
| beside: literal window, purchases continuing, no credits | $431M | 0 | $6.35 | | 2.9% |
| Equity-only top (owner cash after interest, against the market value) | $462M | 0 | $40.21 | $22.08 | 5.7% |
| Equity-only bottom | $158M | −0.54% | $21.05 | $10.31 | 3.2% |
| beside: equity-only depreciation variant | $594M | 0 | $51.54 | $28.23 | 7.3% |

**The floor is tested first.** At $38.43 the best expected return on any case the analyst could defend is 5.0% on the
all-equity top and 5.9% on the depreciation variant, which the run does not use because it charges less than the
maintenance the utility must spend (Q4); 5.7% and 7.3% on the equity-only figures. No case earns the floor of about ten
percent; on the central cases the expected return sits a little below the long bond's 5.43%. "So, there’s just a point at
which we drop out of the game." **[M2003-149]**. The width is not reached (it is 2.6 to one in any case), and the price
is above the top of the all-equity range, which closes OUT on its own.

- **Value range (all-equity, central): $12.85 to $33.00 a share against $38.43** (close 2026-10-16, aggregator, flagged).
  Equity-only beside: $21.05 to $40.21.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged,
  after the company's own tax: **all-equity (the central figure): −$1.95 a share**, which is to say no positive price at
  which the midpoint earns the floor, net debt exceeding the midpoint's value at ten percent; **equity-only, beside:
  $16.20 a share**. No cheap price is reported.
- **Contrary evidence against the OUT, written down** **[M1997-127]**: the regulated utility, the deciding part, is
  growing its rate base under five-year plans and its segment EBIT rose from $242M to $403M; a run that valued Utilities
  alone at its own regulated return would show a better part than the whole. But the floor is applied to what the buyer
  buys, the whole company at its price, and the rows refuse a wide or close case cured by optimism: "we don’t really try to
  compensate for that sort of thing by having some extra large margin of safety" **[M2007-022]**.

**VERDICT: OUT.** No case in the range earns the floor at the price **[M2003-149]**, and the price ($38.43) is above the
top of the all-equity range ($33.00); a business whose growth costs more than it returns is worth less on the growth case
**[L2000-023]**, and the price is set against the bottom of the range, $12.85 **[L2013-012]**. Q8, Q9, Q10 and Q12 are NOT
REACHED.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT). The fact found for it is under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. The facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7** (no case in the range earns the floor at the price **[M2003-149]**; the price is above the top of the range).
Value range, all-equity: **$12.85 to $33.00 a share** (equity-only $21.05 to $40.21) **against $38.43** (close
2026-10-16, aggregator, flagged). Fair price, a reporting figure: all-equity **below zero (−$1.95)**; equity-only $16.20.
Weighings carried: Q3 against, Q4 against, Q5 ability against (integrity IN), Q6 against in both parts, the buyback line
against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond).** The long government rate on the price date was 5.43% (Step 0); the expected return at $38.43 is 3.5%
  on the all-equity bottom case and 5.0% on its top (Q7's table), 3.2% to 5.7% equity-only.
- **Q9 (the target's debt and exposures).**
  - Debt on the face $7,049M at 2026-06-30 (current maturities $18M, short-term borrowings $336M, long-term debt $6,695M)
    against UGI shareholders' equity of $5,213M and cash of $476M (10-Q `0000884614-26-000052`); $7,134M at 2025-09-30 (10-K
    `0000884614-25-000053`). Debt has stood above $6.6 billion since FY2019 (Q4's table). The criterion "Businesses earning
    good returns on equity while employing little or no debt" **[R1997-001]** is the one Q3 hands to Q9.
  - $700M of convertible senior notes of UGI Corporation, due June 2028, cash up to principal (10-K Item 1A; 10-Q).
  - AmeriGas refinanced at 9.5% in May 2025 (10-K, Item 7).
  - Derivative collateral: $472M received in FY2021 and $420M paid in FY2023, through operating cash (cash-flow statements,
    Q4); FY2023 net losses on commodity derivatives not associated with current-period transactions of $1,402M at UGI
    International and $236M at Midstream & Marketing (Note 22, FY2025 10-K). The international energy-marketing book was
    exited in FY2024.
  - Private notes of 2026-08-17 and 2026-10-02 at UGI Utilities and Mountaineer, "used primarily to refinance
    indebtedness"; the Mountaineer notes carry an EBITDA-to-interest covenant (8-Ks `0001104659-26-097884`,
    `0001104659-26-113317`).
  - The West Reading explosion of 2023-03-24: seven dead; the NTSB placed the cause in a UGI Utilities service tee degraded
    by heat from a third party's steam pipe; litigation in discovery, no range of loss estimable (10-K, Item 7).
  - Cash held mostly at the subsidiaries: $214M at the parent level at 2025-09-30 (10-K, Item 7).
- **Q10, Q12.** No fact found that bears on them beyond those above.
- No integrity facts are recorded here: Q5 was reached and answered (integrity IN).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      *Exception:* Q5 and Q6 were committed together by the earlier session (`c1b61b45`). The run was killed by a session
      limit at about 06:01 after Q6 and resumed from Q7 by a second session, which committed Q7 (`857933bb`) and then the
      close.
- [x] Dispatched run: the brief granted per-question pathspec commits; the lock in `Screens/_daily/` is the dispatcher's
      (present on resume, not touched by the analyst); the fold into the register is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched in either session after the
      directory listing declared at (1). What was seen by accident is declared under CONTAMINATION, item (4) added on
      resume.
- [x] Every v5 id resolves (`scripts/check_cites.py`: no E-id, every id in `principle_ledger_v5.csv`, every quoted
      fragment beside an id found in that row); every filing fact carries its accession.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 NOT REACHED; nothing after it
      is a clearance.
- [x] Owner cash after every real cost, built from the filed cash-flow statements, never a net-income proxy (operator
      rule 5); the sovereign from the US Treasury par yield curve; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (Foundations, Q2, Q7); facts for the later questions are
      under AFTER THE STOP.
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used, each checked against the filing (Step 0).
- [x] `python tools/check_framework.py` PASS before the final commit.
- Honest notes. (1) The resumed session changed one input of the killed session's uncommitted Q7 script: it dropped a
  $22M a year tax charge for investment tax credits, on the evidence that the credits were mostly carried forward unused;
  the change raises every value by about $1.90 a share and both versions are in `q7_output.txt`. (2) The maintenance share
  (about 81%) is Q3's guess on FY2025 segment figures applied to the five-year average; the filing gives no split.
  (3) The window's averages carry the cash of parts since sold while net debt holds their proceeds (Q7, confessed); the
  direction is to flatter the range. (4) Net purchases were 97% of the serial-acquirer line; under the organic pair the
  box is the same (expected return 3.9%). (5) The Electric Utility's own owner cash is not filed, so the signed sale was
  valued beside on its most favourable reading only.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. First, Q7's specific (c) values a deal closed after the window and a deal signed but not closed, but says
nothing about **divestitures closed inside or after the window**: for a company that sold seven parts in three years, the
five-year averages still carry the sold parts' cash while the latest net debt already holds their proceeds, and the filer
does not file the parts' own owner cash, so the rule cannot be applied symmetrically; I left the averages as filed and
confessed the direction of the error (it flatters the range). Second, Q7's tax convention speaks of a company that pays
tax below its statutory rate because of carryforwards or credits that run out, but here the low cash tax came mostly from
accelerated tax depreciation in a growing utility, which does not run out, while the credits that do run out were mostly
unused in the window; the text does not say how to split a low cash tax among its causes, and I charged nothing for the
depreciation and added the unused credits as the shelter's value. Third, the all-equity basis needs owner cash before
interest and after tax, and the text does not say at what rate the interest is added back; I used the 21% federal
statutory rate and confessed it as a CONVENTION of this run. None of the three moves any case across the floor here.
