# Company Run: Xcel Energy Inc. (Nasdaq: XEL), 2026-10-27
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run,
and later questions are marked NOT REACHED.

A dispatched blind run (operator rule 10). The brief departs from the canonical brief in two places, which it states:
the repository path (now `C:\Projects\BRK`), and the lines of evidence, which are derived here from the 10-K's Item 1,
Item 1A and Item 7 rather than handed over by the dispatcher.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-27: the operator does not hold this name (`PORTFOLIO.md` has no XEL row).*

**Contamination, declared.** Seen by accident and not used: (1) the session context listed the latest commit subjects,
which name another company's run (a utility, "WEC v5 re-run, OUT at Q7, armed at the equity-only fair price"); (2) the
same context's `git status` named another company's research folder (`_research 2026-09-27 ARCB`); (3) the operator's
memory index lines in the session context, which describe the queue in general and name no fact about this company.
No other run file, holding review, `PORTFOLIO.md`, register, reading list or resume-state file was opened, listed or
searched. The framework's own Q7 text says utilities run on 2026-10-17 and 2026-10-18 showed a fair price that was not
positive on the all-equity basis; that is governing text, read as text.

**The lines of evidence, derived from the 10-K for FY2025 (0000072903-26-000009), and why.** From Item 1: (a) the
business is four state-regulated utilities, electric and gas, with rate base, allowed return and equity ratio set by
eight state commissions and FERC; (b) a five-year base capital plan of $60 billion, funded by $30.2 billion of cash from
operations, $22.8 billion of new debt and $7.0 billion of equity. From Item 1A: (c) wildfire liability ("damage amounts
could exceed our coverage (as experienced with the Marshall Wildfire settlement in 2025)"); (d) cost recovery and
affordability ("Regulators may challenge rate increases due to increased customer affordability pressures"); (e) large-load
(data-center) concentration; (f) dependence on capital markets and on the subsidiaries' dividends. From Item 7: (g) the
featured non-GAAP "ongoing" earnings and its guidance, and the 21-year record of meeting it; (h) the gap between allowed
and earned returns in Colorado (PSCo GAAP ROE 5.66%, ongoing 7.55% in 2025); (i) the financing plan, ATM and forward
equity sales. Chosen because they are the variables the filer itself says decide its earnings (rates, capital, recovery)
and the risks it ranks as able to impair them (wildfire, regulation, capital access); (g) was added because Q4 and Q5 ask
for it by name.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $77.86 (close 2026-10-26; `tools/run.py` quote, an aggregator, flagged per operator rule 5: live quote only).
- **Shares by class:** one class, 624,634,306 shares, from the cover of the 10-Q for the quarter ended 2026-06-30, filed
  2026-07-30, accession `0000072903-26-000154` (`python Screens/cover_shares.py XEL`). Checked: the 10-Q balance sheet
  gives 624,405,747 outstanding at 2026-06-30 (no treasury shares are shown; the balance sheet line is "shares
  outstanding"); the proxy (`0000072903-26-000063`) gives 624,162,193 at 2026-03-23; no share issuance 8-K or prospectus
  after the 10-Q closed. **Not in the count:** forward sale agreements outstanding at 2026-06-30 for 69.8 million shares
  (12.2 + 15.1 + 21.2 + 21.3 million), minimum expected proceeds $5,177 million, maturing December 2026 to December 2028
  (10-Q, `0000072903-26-000154`, Note on financing). They are committed but unissued; Q7 shows the effect beside.
- **Market cap:** $48,634M (624.634M x $77.86).
- **Sovereign for the earnings currency (USD):** 5.31%, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-26 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-25, `0000072903-26-000009` (Item 1, 1A, 5, 7, 8 and
  notes 5, 12, 14); 10-K for FY2024, `0000072903-25-000029` (the 2025 guidance and its assumptions); 10-K for FY2022,
  `0000072903-23-000007` (2021 and 2022 cash-flow lines); 10-K for FY2021, `0000072903-22-000010` (the 2021 operating cash
  explanation); 10-Q for Q2 2026, `0000072903-26-000154`; 10-Qs for Q2 2025 `0000072903-25-000225` and Q3 2025
  `0000072903-25-000257` (timing of the 2025 debt repurchases); proxy filed 2026-04-07, `0000072903-26-000063`; 8-Ks of
  2026-10-09 `0000072903-26-000175` (Minnesota rate stability plan), 2026-08-20 `0000072903-26-000160` (Colorado electric
  verbal decision), 2026-07-14 `0000072903-26-000144` (Colorado gas settlement), 2026-07-30 `0000072903-26-000149`,
  2026-05-01 `0001193125-26-201734` (equity distribution agreement).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, FY2025, $4,083M,
  and capital/construction expenditures, $10,908M: `tools/run.py` (XBRL) and the filed consolidated statement of cash
  flows in `0000072903-26-000009` agree to the million.
- **`tools/run.py XEL`, arithmetic lines only** (its v4 material ignored, Part VII): owner cash (OCF less stock pay less
  capital spending) FY2023 -$554M, FY2024 -$2,756M, FY2025 -$6,882M; on the depreciation basis $2,829M, $1,839M, $1,058M;
  capex $5,854M, $7,364M, $10,908M; D&A $2,471M, $2,769M, $2,968M; stock pay $27M, $33M, $57M (the filed cash-flow line
  reads $25M, $33M, $46M; the filed line is used). No securities inside operating cash, no other stock-pay line, no
  intangible or software spending beside capex. **A defect in the tool's debt table, recorded:** its "sum" column adds
  `xel:DeferredCreditsAndOtherLiabilitiesOtherThanLongTermDebtNoncurrent` and
  `us-gaap:LiabilitiesOtherThanLongtermDebtNoncurrent`, which are not debt; the debt read here is from the filed balance
  sheets (short-term debt, current portion and long-term debt, plus finance leases where shown separately).
- Working notes, the ledger-row printer, the fetch and the Q7 arithmetic are in `Test Runs/_research 2026-10-27 XEL/`
  (`notes.md`, `q7_calc.py`, `q7_output.txt`, `peers.py`); raw filings under its ignored `cache/`.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**, which for a regulated utility turns on the rate orders and the capital plan, not the quotation. Who is
paid to tell you bears heavily here: the filer publishes an annual earnings guidance range, a long-term objective of
"annual EPS growth of 6% to 8+%" and a $60 billion five-year plan, and the speakers' rule on a seller's projection is
"don't ask the barber whether you need a haircut" **[M2011-083]**; those figures are read as the seller's, and none is
used as an input. The analyst's habits: look for "what's wrong in things" **[M2025-013]**, and write contrary evidence
down as found **[M1997-127]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) every year of the window
the business spent more than it took in from operations (owner cash after all spending negative in each of FY2021 to
FY2025); (2) shares outstanding rose from 507.2M (2016) to 624.6M (2026), 49.2M of them in 2025 alone; (3) the 2025
"ongoing" EPS of $3.80 met guidance of $3.75 to $3.85 with the help of a $162M pre-tax gain on the parent's purchase of a
subsidiary's bonds at a discount, while the same figure excluded the $298M Marshall Wildfire charge (worked at Q4 and Q5);
(4) Smokehouse Creek wildfire: the Texas A&M Forest Service found SPS's power lines caused it, settlements reached total
$404M, and about $80M of the $525M insurance for that policy period remained at 2026-06-30 (10-Q `0000072903-26-000154`).

## THE STANDING RULE
The buyer's conduct, not the target's: a part-interest bought for cash, with no borrowed money, carries no ruin to the
buyer, since "borrowed money has no place in the investor's tool kit" **[L2014-005]** and the rule is "always be sure you
can play the next day" **[M2025-015]**. Nothing about this purchase would require the buyer to borrow or to give anyone a
call on his cash. The target's own debt is Q9's.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**. The economics are written in the filings: revenue requirements set to
  "recover plant investment, operating costs and an allowed return on investment" (10-K Item 7, `0000072903-26-000009`),
  so earnings are roughly rate base x equity ratio x the return earned on it. The key variables **[M1998-044]**: (1) rate
  base growth, which the capital plan states ($60.0 billion of base capital 2026 to 2030 against $11.6 billion spent in
  2025); (2) the allowed return and equity ratio (recent orders and settlements: Minnesota electric ROE 9.60%, equity
  52.5%, verbal decision June 2026; Colorado electric ROE 9.3%, equity 54.5%, verbal decision 2026-08-19; Wisconsin ROE
  9.8%, equity 52.5%; North Dakota ROE 9.8%, equity 52.5%); (3) the gap between allowed and earned (2025 GAAP ROE: NSP-
  Minnesota 9.19%, PSCo 5.66%, SPS 8.70%, NSP-Wisconsin 9.09%); (4) sales growth (weather-normalized retail electric +2.0%
  in 2025; ~3% projected); (5) wildfire liability and the regulatory climate. The first four are knowable and important
  **[M2006-076]**; the fifth is important and only partly knowable, and is weighed where the text puts it (Q2 and Q9).
- **Do the past statements tell me the future ones?** **[M2008-033]**: for this business, largely yes. The filer itself
  writes the ten-year inputs down: a five-year capital plan by subsidiary and function, a five-year financing plan, rate
  base and allowed returns by jurisdiction. The insiders would "put down on paper" their forecast, the opposite of the
  "too hard" answer of **[M2000-105]**. The product needs no technical understanding; "What is important is that I
  understand the economic dynamics of the industry" **[M2011-014]**, and those are rate regulation.
- **Change.** The industry is changing (coal exit by 2030, ~9,500 MW of wind, solar and storage in the base plan, data
  centers), but the change is in what is built, not in how the owner is paid: the return is still set on invested capital
  by commission. Change that puts the ten-year economics out of reach closes TOO HARD here **[M1998-008]**; I do not find
  that here, because the payment mechanism is the variable and it is foreseeable in form. Doubt about that is carried to
  Q2 as the regulatory-climate question **[L2023-011]**.
- **VERDICT: IN.** The economics are rate-regulated returns on a stated capital plan; the key variables are named and,
  except wildfire and regulatory climate, foreseeable **[M2012-065]**, **[M1998-044]**, **[M2011-014]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
- **The parts table** (10-K note 14, `0000072903-26-000009`; the segment measure the filer reports is net income, so the
  share is of segment net income, 2023 to 2025, the years the note gives):

  | Part | Segment net income 2023 / 2024 / 2025 ($M) | Share of the three years | Castle | Decides |
  |---|---|---|---|---|
  | Regulated electric utility (four utilities, eight states) | 1,686 / 1,846 / 1,870 | 88.6% | exclusive regulated service territory | **yes** (more than half) |
  | Regulated natural gas utility (three utilities) | 219 / 237 / 256 | 11.4% | the same, on gas distribution | no |
  | Non-segment (holding company interest, rental housing, RDF) | net losses | n/a | none | no |

  The electric part decides (Q2, a business of parts, CONVENTION as the text states it).
- **Why the castle stands.** The money test: "if I had a hundred million dollars [...] could I do it?" **[M2011-015]**. No
  attacker can duplicate 115,000 conductor miles of transmission and 225,000 of distribution with state certificates of
  need, franchise agreements and siting approvals behind them (10-K Item 1); the speakers' railroad answer applies in
  kind: "You really couldn't create another railroad" **[M2013-054]**, an asset "that couldn't be duplicated"
  **[M2012-030]**. The filer names its competition and it is not another wire: customers' self-generation, rooftop and
  community solar, wholesale buyers' alternatives, FERC Order 1000 competition for some new transmission, and cities that
  could municipalize at franchise renewal ("No municipalization activities are occurring presently", 10-K Item 1).
- **Pricing power and the agony before a rise** **[M2005-020]**: none of the business's own. Every increase is a rate case
  before a commission, which is the "prayer session" in literal form, and the recent orders show the agony: Colorado
  electric asked $356M and was given about $157M at 9.3% (8-K 2026-08-20, `0000072903-26-000160`); Minnesota electric asked
  $473M, revised to $365M, and was given about $211M over two years at 9.60% (10-Q `0000072903-26-000154`); New Mexico asked
  $175M, stipulated at $90M. In October 2026 NSP-Minnesota offered a base-rate freeze for 2027 and 2028 in place of a rate
  case (8-K `0000072903-26-000175`), and Item 1A names "customer affordability pressures". The rows put a regulated
  return where the castle's excellent return would be: the moat "protects excellent returns" **[L2007-004]**, and a return
  "set by a regulator is the exception" to the ordinary-returns OUT, carried to Q3 as a second best, in the speakers'
  words "there's no way we get rich on our utility investments. But there's no way we get poor, either" **[M2009-104]**,
  "deploy large sums at fair returns" **[L2005-005]**, and "in utilities the trade has been the compact has been that you
  get a modest return" **[M2024-011]**.
- **The low-cost position and the customer's choice.** The filer reports five-year average residential electric bills 28%
  below the national average and gas bills 12% below, on EIA data (10-K Item 1). The residential customer has no low bid
  to take, except to generate his own; the large C&I customer can self-generate or relocate (10-K Item 1).
- **The competitor row** (CONVENTION of this run: the 10-K names no rival company; its competition paragraph names only
  classes of competitor, and its performance graph uses the EEI index. Comparators chosen as three SEC filers that are
  state-regulated, vertically integrated electric and gas utilities of the Midwest and of comparable mix: Ameren (AEE),
  CMS Energy (CMS) and Alliant Energy (LNT); rationale: the Q2 field test needs the field's returns from the field's own
  filings, and these three run the same business under similar commissions). Same metrics, each from the company's own
  10-K XBRL facts (first-filed values; `Test Runs/_research 2026-10-27 XEL/peers.py`), 2016 to 2025:

  | Company | Return on average equity, range over 2016-2025 | OCF less capex, sign | Shares 2016 to 2025 | Latest 10-K |
  |---|---|---|---|---|
  | XEL | 9.4% (2025) to 10.8%; ten-year mean about 10.4% | negative every year; 2025 -$6,825M | 507.2M to 623.6M (+23%) | `0000072903-26-000009` |
  | AEE | 7.3% (2017) to 11.4% (2025) | negative 2017-2025 | 242.6M to 276.4M (+14%) | `0001002910-26-000009` |
  | CMS | 12.0% to 14.4% (2019-2025, 2021's 22.2% includes a sale of a bank); 2016-2018 not tagged | negative most years; capex untagged 2023-2025 | 279.2M to 306.4M (+10%) | `0000811156-26-000004` |
  | LNT | 9.8% to 11.7% | negative every year 2016-2022; capex untagged as one line 2023-2025 | 227.7M to 257.1M (+13%) | `0000352541-26-000007` |

  The field earns about ten to twelve percent on book equity over the whole span, every year, through 2020 and 2022: a
  durable, ordinary, regulator-set return, consuming cash and issuing shares. XEL sits in the field, at the low end in 2025,
  and issues shares fastest of the four. Judged in words, as the convention requires: ordinary, and set by regulators.
- **Widening or narrowing** **[M1999-108]**, and what could destroy it **[M2000-014]**. For widening: load growth (the
  Colorado commission approved a load forecast of 3% compound annual sales growth through 2031; a Google data-center
  agreement in Minnesota); large-load tariffs requiring the new customer to pay its own costs (approved in Minnesota, June
  2026). For narrowing: (1) wildfire. Marshall Fire settlement charge $296M in 2025 beyond insurance; Smokehouse Creek
  settlements $404M, the 2025-26 policy nearly exhausted; excess liability coverage cut from $600M to $450M while the
  premium rose from about $40M to about $135M a year (10-K Item 7); supportive wildfire laws passed in Texas and North
  Dakota, not in Colorado (10-K Item 1). (2) The earned-allowed gap in Colorado: PSCo's ongoing ROE 7.55% in 2025, and
  the Denver District Court affirmed the CPUC's 2024 gas order against PSCo on cost of capital and capital structure (10-K
  Item 7). (3) Affordability: the Minnesota rate-freeze offer. The rows name this exact risk and the speakers' own error in
  it: "the regulatory climate in a few states has raised the specter of zero profitability or even bankruptcy [...] I did
  not anticipate or even consider the adverse developments in regulatory returns" **[L2023-011]**. On the filings read, no
  Xcel state has denied recovery of prudent costs wholesale or set returns near zero; the narrowing is a notch, not a
  breach. Where the text puts it, the regulatory climate is weighed again at Q9 **[L2023-011]**.
- **Change for the better.** None is credited. The load growth is forecast, not shown over a full cycle.
- **VERDICT: IN.** The deciding part's castle stands: an exclusive regulated franchise no attacker with money can
  duplicate **[M2011-015]**, **[M2013-054]**, earning a regulator-set return the rows carry as the exception, not the OUT
  **[M2009-104]**, **[L2005-005]**. Its weakness is the compact itself, which is notched (wildfire, Colorado lag,
  affordability) but not shown broken on these filings **[L2023-011]**.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What it earns on the capital it needs** **[M2010-090]**, **[M2000-065]**. Consolidated return on average equity about
  10% to 11% from 2016 to 2024 and 9.4% in 2025 (net income over average equity, 10-K XBRL facts). At the utilities, where
  the capital is actually employed, the filer's own table gives 2025 GAAP ROE of 7.60% and ongoing 8.40% for the utility
  subsidiaries together, against 9.36% and 10.38% for Xcel Energy consolidated (10-K Item 7). The two points between them
  are the holding company's own borrowing, laid on top of the utilities' allowed capital structures; a return made that way
  is the kind the rows read with care, "we could make it almost any number you want if we just used enough leverage"
  **[M2001-054]**. On all the capital (debt plus equity), net income plus after-tax interest (interest at 21%) was about
  6.3% of average capital in 2020 and 5.9% in 2025.
- **What the added capital earned.** From 2020 to 2025 debt plus equity rose by $23.5 billion ($35.3B to $58.8B, filed
  balance sheets) and the after-tax return before interest rose by about $1.04 billion ($2.14B to $3.18B): about 4.4% on
  the added capital. Net income rose $545M on $9.0 billion more equity, 6.0%; 7.1% with the 2025 Marshall charge and the
  2025 bond-repurchase gain both taken out. Part of the added capital is construction work not yet in rates (AFUDC rose
  from $157M to $406M), so a lag flatters nothing and understates something; even so, the added capital has so far earned
  below what the commissions allow. "whether that's good or bad depends on what we earn on that incremental $130 million
  over time" **[M2001-019]**.
- **Reinvestment to stand still, and to grow** **[L1999-024]**, **[M2000-144]**. Depreciation plus nuclear fuel
  amortization ran $2.26B (2021) to $3.08B (2025); capital spending ran $4.24B to $10.91B, and the base plan is $13.79B in
  2026 and $15.13B in 2027 (10-K Item 7). Owner cash after all spending was negative in every year of the window
  (-$2,086M, -$726M, -$552M, -$2,756M, -$6,871M) and is planned to stay so: the 2026-2030 plan funds $60.0B of capital with
  $30.2B of operating cash after dividends, $22.8B of debt and $7.0B of equity. The speakers' utility sentence is exact:
  "To earn more, their owners must invest more" **[L2011-019]**. The spending is not optional in the sense of **[M1998-128]**
  (a utility must serve load and replace retiring coal), but it is the kind the rows accept when it earns "decent returns
  on the incremental sums they invest" **[L2009-012]**, "the second-best choice, still a good choice" **[M2018-055]**, and
  "It's measured by the operating earnings after depreciation" **[M2014-086]**.
- **The growth arithmetic.** Earnings per share grew from $2.21 (2016, 10-K XBRL) to $3.42 GAAP (2025); aggregate net
  income from $1,123M to $2,018M while equity more than doubled ($11.0B to $23.6B) and shares rose 23%. "we're not earning
  a higher rate of return on capital than we were when we started. We just put way more capital into the business"
  **[M2023-081]**.
- **WEIGHS AGAINST.** A capital-heavy second best **[M2018-055]**, **[L2009-012]**, whose added capital has earned below
  the allowed return so far (about 4.4% after tax on all added capital, 6% to 7% on added equity), whose consolidated
  equity return leans on holding-company debt **[M2001-054]**, and which must keep issuing shares to fund growth
  **[L2011-019]**. The "little or no debt" criterion is Q9's.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** (USD millions; year-end; 10-K XBRL
  first-filed values, accessions `0000072903-17-000008` to `0000072903-26-000009` as `tools/run.py` lists them, with the
  FY2024 and FY2025 sheets read in the filed statements; debt = short-term + current portion + long-term, finance leases
  added where shown separately):

  | Year-end | Total assets | PP&E net | Equity | Debt | Debt/equity | Retained earnings | Receivables | Reg. assets (cur.+noncur.) | Prepayments and other | Cash |
  |---|---|---|---|---|---|---|---|---|---|---|
  | 2016 | 41,155 | 32,842 | 11,021 | 14,843 | 1.35 | 3,982 | 776 | 3,445 | 139 | 84 |
  | 2017 | 43,030 | 34,329 | 11,455 | 15,791 | 1.38 | 4,413 | 797 | 3,429 | 183 | 83 |
  | 2018 | 45,987 | 36,944 | 12,222 | 17,247 | 1.41 | 4,893 | 860 | 3,790 | 154 | 147 |
  | 2019 | 50,448 | 39,483 | 13,239 | 18,785 | 1.42 | 5,413 | 837 | 3,423 | 185 | 248 |
  | 2020 | 53,957 | 42,950 | 14,575 | 20,727 | 1.42 | 5,968 | 916 | 3,377 | 250 | 129 |
  | 2021 | 57,851 | 45,457 | 15,612 | 23,457 | 1.50 | 6,572 | 1,018 | 3,844 | 289 | 166 |
  | 2022 | 61,188 | 48,253 | 16,675 | 24,843 | 1.49 | 7,239 | 1,373 | 3,930 | 360 | 111 |
  | 2023 | 64,079 | 51,642 | 17,616 | 26,314 | 1.49 | 7,858 | 1,315 | 3,409 | 294 | 129 |
  | 2024 | 70,035 | 57,198 | 19,522 | 29,174 | 1.49 | 8,553 | 1,249 | 3,410 | 652 | 179 |
  | 2025 | 81,371 | 65,639 | 23,609 | 35,184 | 1.49 | 9,207 | 1,330 | 3,527 | 1,075 | 274 |
  | 2026-06-30 (10-Q) | 87,165 | 69,497 | 24,057 | 40,784 | 1.70 | 9,607 | 1,255 | 3,629 | 587 | 2,010 |

  What the figures say: the balance sheet doubled in nine years and it is all plant (PP&E $32.8B to $65.6B); there is no
  goodwill to speak of and no acquisition in the decade; equity doubled, but $4.8B of the rise is new shares (paid-in
  capital $8,155M at end-2022 to $12,906M at end-2025) and retained earnings rose only $5.2B in nine years because the
  dividend takes about half of earnings; debt grew faster than equity (to 1.70 times equity at 2026-06-30, after $4.7B of
  bonds issued in the half-year); cash is kept near zero, liquidity being the credit lines and commercial paper.
  Receivables rose 71% against revenue up 32%, most of the rise in 2022 with high gas prices, then flat. Regulatory assets
  are steady (they peaked in 2021 to 2022 with the Winter Storm Uri fuel deferral, recovered by 2023), and regulatory
  liabilities ($7.0B at end-2025, 10-K Item 7) exceed them. **Prepayments and other** rose from $139M to $1,075M: I looked
  twice, as **[M1995-064]** asks of prepaid accounts building up, and the notes explain it: insurance receivables of $353M
  (Marshall) and $195M (Smokehouse Creek) sit in that line at end-2025 (10-K note 12, `0000072903-26-000009`), and it fell
  back to $587M by 2026-06-30 as insurance was collected. What the figures cannot say: whether the commissions will let
  the $60 billion plan earn the allowed return; the balance sheet shows only that it is being built on borrowed money and
  new shares.
- **The real costs.** Depreciation is a true cost here **[R1996-023]**, and for a utility it is a floor for maintenance,
  not a ceiling, "To earn more, their owners must invest more" **[L2011-019]**; nuclear fuel is bought inside capital
  spending (PP&E includes nuclear fuel of $3,678M gross) and amortized ($96M to $118M a year), so it is charged with
  depreciation in owner cash. Stock pay is small ($20M to $46M). AFUDC-equity is a non-cash credit to income ($281M in
  2025, 14% of net income, and guided to rise $140M to $150M in 2026); owner cash is taken from operating cash flow, where
  it is reversed, so it inflates nothing below. Wildfire losses are real recurring costs of this business, in the speakers'
  words on catastrophe losses, "Except for" losses "will forever be paid with shareholders' money" **[L2002-002]**.
- **EBITDA in the filer's own mouth:** no instance found in the 10-K text read (a search for "EBITDA" in the FY2025 10-K
  returns none). The featured figure is "ongoing earnings" and "ongoing diluted EPS", which "may adjust the related GAAP
  amounts for certain items that are non-recurring in nature" and is used "in determining performance-based compensation"
  (10-K Item 7).
- **The habits, recorded here and carried to Q5** (the make-the-numbers paragraph, CONVENTION as the text states it):
  (1) the guidance habit of **[L2019-006]** and **[L2000-037]**: earnings guidance every year, and a long-term EPS growth
  objective of "6% to 8+%" (10-K Item 7); (2) the pattern of **[L2002-041]**: the boast, in the 10-K and again in the
  proxy, of "meeting or exceeding our initial ongoing earnings guidance range for 21 consecutive years" (10-K Item 1); (3) an adjusted figure featured, which in 2025 excluded the $298M Marshall
  Wildfire charge (a real cost of the business, **[L2002-002]**, **[L2016-006]**) while it kept in a $162M pre-tax gain from
  Xcel Energy Inc.'s purchase of $787M face of NSP-Minnesota's 2.60% to 4.125% first mortgage bonds for $607M (10-K note 5,
  `0000072903-26-000009`). The gain is correctly accounted for as a debt extinguishment; the question it raises is not of
  the statements but of the figure management chose to feature and to be paid on, and it belongs to Q5.
- **VERDICT on the accounts: IN** (no confusion, and no suspicion raised by the statements themselves: the prepaid
  build-up is explained in the notes, the regulatory accounts are steady, every adjustment is reconciled to GAAP)
  **[M1995-063]**, **[M1995-064]**. **WEIGHS AGAINST** on the habits above, as a negative that is not by itself exclusionary
  **[M1994-018]**, carried to Q5.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The record against the hand dealt** **[M1994-008]**. Bob Frenzel, chairman since December 2021 and CEO since August
  2021 (CFO 2016 to 2020); Brian Van Abel, CFO since March 2020 (10-K Item 1). They inherited a franchise with good
  regulatory relations in the Upper Midwest and a harder one in Colorado and Texas. On ability: low bills against the
  national average, the coal exit on schedule, large-load tariffs that make data centers pay their own way, settlements
  of both wildfire matters before trial; against it, earned returns below allowed in Colorado (PSCo ongoing ROE 7.55%),
  two wildfires attributed to or alleged against the company's lines in four years, and added capital earning below the
  allowed return so far (Q3).
- **The habits carried from Q4, read with the integrity record.** The facts, each from a filing:
  1. The 2025 guidance was "$3.75 to $3.85 per share", with key assumptions listing sales, riders, O&M, depreciation,
     property tax, interest and AFUDC; none names a gain on debt repurchases (10-K for FY2024, `0000072903-25-000029`).
  2. In the third quarter of 2025 the company raised its O&M assumption to "~5%" from ~3%, "primarily due to increasing
     benefit costs" (10-Q Q3 2025, `0000072903-25-000257`). By then the parent had bought $190M face of NSP-Minnesota bonds
     for $122M (pre-tax gain about $63M, of which $43M by June 30: 10-Qs `0000072903-25-000225`, `0000072903-25-000257`).
  3. For the full year the parent bought $787M face for $607M, pre-tax gain about $162M (10-K note 5,
     `0000072903-26-000009`): so about $597M face and about $99M of the gain came in the fourth quarter, the quarter that
     closes the year against guidance.
  4. Ongoing EPS came in at $3.80, the midpoint. The $162M gain is inside it ("Xcel Energy Inc. other results [...] primarily
     include gains from debt repurchases": $0.23 a share of positive "other results" in 2025 against $0.07 in 2024). At the
     21% federal rate (the combined statutory rate was not read; a state rate would lower the figure slightly) the gain is
     about $0.22 a share on 589M diluted shares, so ongoing EPS without it would have been about $3.58, below the $3.75 bottom
     of guidance. The same figure excluded the $298M Marshall Wildfire charge ($0.38 a share).
  5. In 2024, guidance was $3.50 to $3.60 and ongoing EPS was $3.50; a $56M pre-tax gain on the same kind of repurchase was
     inside it (about $0.07 a share), and a $47M Sherco refund was excluded (10-K `0000072903-26-000009`, Item 7 and note 5).
     Without the gain, about $3.43, below the bottom.
  6. The figure is paid on: "When ongoing EPS is below guidance, awards will not be paid"; at $3.78 or more the operational
     results earn a multiplier of 100% to 150%; the 2025 annual incentive paid 143.76% of target; 30% of the 2025-2027
     performance units vest on ongoing EPS growth (proxy, `0000072903-26-000063`). The CEO's 2025 total compensation was
     $15,998,859.
  7. The boast, in the 10-K and the proxy: guidance met or exceeded "for 21 consecutive years, with 18 years in the mid to
     high range of guidance" (proxy, `0000072903-26-000063`).
- **What the rows say of exactly this.** "we become downright incredulous if they consistently reach their declared
  targets. Managers that always promise to "make the numbers" will at some point be tempted to make up the numbers."
  **[L2002-041]**. The means need not be fraud to count: "CEOs engaged in uneconomic operating maneuvers so that they could
  meet earnings targets they had announced" **[L2000-039]**; "they might do a little fudging in order to make sure that we
  actually came out at that number" **[M2010-001]**; the scourge is "earnings "guidance" and the desire of CEOs to "hit the
  number."" **[L2019-006]**; and "a management that regularly attempts to wave away very real costs by highlighting
  "adjusted per-share earnings" makes us nervous" **[L2016-006]**. Here the two moves run in the same direction in the same
  year: a real cost waved away, a one-time financing gain kept, and a fourth-quarter transaction outside the stated
  assumptions supplying the difference between missing the declared range and the midpoint of it, in a year when the pay
  of the people who chose the transaction turned on that range. The bond purchase may well have been sound in itself (the
  parent paid 77 cents on the dollar for low-coupon bonds); what it bought in the featured figure is the point.
- **The rest of the record, written down for the other side** **[M1997-127]**: GAAP comes first in the 10-K and every
  ongoing adjustment is reconciled to it; the gain is disclosed each quarter in the notes and MD&A; no restatement, no
  auditor change, clawback policies in place and none triggered; the risk factors are candid (the insurance for the
  Smokehouse Creek period is nearly spent; damages "could exceed our coverage"); the CEO holds 512,597 shares; a lead
  independent director beside a combined chairman and CEO. Preoccupation with accounting is "a negative" but not "a total
  exclusionary factor" **[M1994-018]**, and the speakers concede "we may be wrong about a fair number that we're ruling
  out" **[M2007-092]**.
- **Love of the business, and after being paid.** Not separately testable from outside for a marketable stake beyond the
  record above; the pay design (70% of the annual incentive on safety, reliability and inclusion metrics; long-term units
  on EPS growth, emissions, nuclear ratings and wildfire mitigation, modified by relative TSR) is weighed at Q6, Part B,
  which this file does not reach.
- **VERDICT on integrity: OUT.** Read with the rest of the record, the habit carried from Q4 leaves doubt, and the rule is
  applied on doubt alone: "If you've got doubts, forget it." **[M2013-088]**. The doubt is specific: in each of the last
  two years the declared range, the 21-year streak and the incentive pay were reached only with a non-operating gain the
  guidance did not name, while a real cost was excluded from the same figure **[L2002-041]**, **[L2016-006]**,
  **[M2010-001]**. The file closes here. Ability is not weighed further. Q6 to Q12 are NOT REACHED; the figures below Q7
  are COMPUTATION, NOT A CLEARANCE.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED (the file closed at Q5). Facts are under AFTER THE STOP.

## Q7: WHAT IS IT WORTH? NOT REACHED as a question. The owner's reporting figures follow, as the brief asks.

### COMPUTATION, NOT A CLEARANCE (the file closed at Q5; nothing here is a verdict or entry language, operator rule 3)
Built by Q7's construction as written (the range convention, the four PG specifics, specifics (a) to (f), the floor tested
first, The regulated utility as amended 2026-10-23, and Part VII's fair price). Arithmetic in
`Test Runs/_research 2026-10-27 XEL/q7_calc.py`, output in `q7_output.txt`. USD millions unless per share.

- **The window and the cash input.** FY2021 to FY2025, from the filed cash-flow statements (`0000072903-26-000009` for
  2023 to 2025; `0000072903-23-000007` for 2021 and 2022). Owner cash after interest and after the company's own tax =
  operating cash flow less stock pay less spending. The maintenance guess is depreciation plus nuclear fuel amortization
  (nuclear fuel is bought inside capital spending). The rows allow depreciation as the guess: it is "not inappropriate in
  most companies to use as a proxy for required capital expenditures" **[M1998-127]**. For a utility it is read as a floor
  **[L2011-019]**. The filing gives no maintenance figure of its own, so specific (e)'s case rests on this guess, said so.

  | FY | OCF | Stock pay | Capex | Maintenance (D&A + NFA) | Owner cash after maintenance | After all spending | Growth spending |
  |---|---|---|---|---|---|---|---|
  | 2021 | 2,189 | 31 | 4,244 | 2,257 | -99 | -2,086 | 1,987 |
  | 2022 | 3,932 | 20 | 4,638 | 2,554 | 1,358 | -726 | 2,084 |
  | 2023 | 5,327 | 25 | 5,854 | 2,567 | 2,735 | -552 | 3,287 |
  | 2024 | 4,641 | 33 | 7,364 | 2,875 | 1,733 | -2,756 | 4,489 |
  | 2025 | 4,083 | 46 | 10,908 | 3,082 | 955 | -6,871 | 7,826 |
  | 5-yr average | | | | | **1,336** | **-2,598** | **3,935** |

- **(a) The cycle base.** The first year is aberrational on the filer's own description: 2021 operating cash fell $659M,
  in the 10-K for FY2021 (`0000072903-22-000010`) "primarily due to the deferral of net natural gas, fuel and purchased
  energy costs related to Winter Storm Uri", and the deferral was recovered in 2022 and 2023 (Colorado: over 24 and 30
  months from January and April 2022). A utility has no business cycle to average over; the deferral and its recovery
  both fall inside the window, so the five-year average already nets the event and is used as the base. CONVENTION of this
  run: where the aberrational year's own reversal lies inside the window, the window average is the cycle base;
  rationale: it is the shortest span that contains the whole event, and the text's "last full cycle" does not exist here.
  Beside it, the 2022-2025 base without 2021: owner cash $1,695M.
- **(b) The growth shown.** The compound rate between the end years is meaningless (2021 is negative), so it is measured
  between the halves: 2021-2022 average $630M to 2024-2025 average $1,344M, 28.8% a year.
- **(f) The cap.** Carried ten years, 28.8% would put owner cash at about $16.7 billion, above the highest share of sales
  the business has earned in the filings read (19.3%, 2023) and above sales themselves; the text cuts any result that
  traces to an absurdity **[M1999-067]**. Cut to the business's own sales growth over the same window: revenue $13,431M
  (2021) to $14,669M (2025), 2.23% a year. Both written down. Beside it, sales growth 2020-2025 (4.94%).
- **(c) Acquisitions:** none in the window. **(d) Working capital:** inside operating cash flow, counted.
- **(e) Growth spending** = capital spending above the maintenance guess: $3,935M in year one, growing at 2.23% to $4,795M
  in year ten, none after. The maintenance guess is charged in every year of every case.
- **The regulated utility.** The deciding part (regulated electric, 88.6% of segment net income) earns a return a regulator
  allows, so the equity-only basis is central **[L2017-012]**, **[M2010-037]**. Utility debt credit: long-term debt
  (long-term, current portion and finance leases) rose from $20,143M at end-2020 to $33,634M at end-2025, $2,698M a year;
  commercial paper and cash left out; no securitization bonds found in the 10-K text read. Credited against the growth
  spending only **[L2000-035]**, capped at the deciding part's allowed debt share. The filings state allowed equity
  ratios for Minnesota electric (52.5%, verbal decision June 2026), North Dakota (52.5%), Wisconsin (52.5%) and Colorado
  electric (54.5%, verbal decision 2026-08-19), which together cover more than half of the electric rate base; weighted
  by rate base (Minnesota electric $14.0B, North Dakota $0.8B, Wisconsin taken at NSP-Wisconsin's $3.5B, Colorado electric
  $13.0B), the allowed debt share is about 46.6%. CONVENTION of this run: the electric rate base by state is not stated as
  one table, so the weights are the rate bases the filings give for each case; rationale: every stated share lies between
  45.5% and 47.5%, so no reasonable weighting moves the cap by more than a point. The cap binds: credit = 46.6% x growth
  spending = $1,834M in year one, growing and stopping with the growth spending (the uncapped $2,698M exceeds it). Beside
  it, the cap at the business's own long-term debt share of long-term capital at 2026-06-30 (61.4%).
- **The two ends, at the 5.31% Treasury rate:**
  - No-growth case (maintenance owner cash $1,336M a year, no growth spending, no credit): $25,160M, **$40.29 a share**.
  - Shown-growth case (2.23%): owner cash after maintenance grows from $1,336M; growth spending and the credit run ten
    years and stop; zero nominal growth after year ten: **$20.13 a share**.
  - The growth bought is worth less than its cost, so the order inverts: the no-growth case is the top of the range and
    the growth case the bottom. The text names this finding, in the row's words "growth can destroy value"
    **[L2000-023]**.
- **VALUE RANGE: $20.13 to $40.29 a share, against $77.86** (2026-10-26, aggregator). Width 2.0 to 1. The literal window
  is the one shown; the 2022-2025 base beside it gives $22.36 to $51.11.
- **The floor, tested first** **[M2003-149]**: at $77.86 the no-growth case yields 2.75% on the price (owner cash
  $1,336M against a market value of $48,634M), and the growth case less; no case in the range earns about ten percent at
  the price, so a Q7 reached would close OUT on the floor whatever the width. A price above the top of the range closes
  OUT by the floor convention as well.
- **FAIR PRICE (Part VII; a reporting figure, never a verdict): $11.91 a share, equity-only, central** (each end valued at
  ten percent: no-growth $21.39, growth $2.42; averaged), after the company's own tax.
  **All-equity, beside: not positive (-$46.26 a share).** Owner cash before interest (interest paid averaged $1,003M,
  added back at 79%): $2,128M; enterprise value no-growth at 5.31% $40,084M against net debt of $38,774M at 2026-06-30
  (long-term $35,948M, current portion $999M, short-term $2,510M, finance leases about $1,327M, less cash $2,010M; operating
  leases left out), $2.10 a share; the all-equity growth case, with all growth spending charged and no credit, -$37.87.
  The utility rule makes the equity-only figure central; the all-equity figure never decides alone.
- **Beside the central figures, for the operator** (none decides): growth at 2020-2025 sales growth (4.94%): range $28.45
  to $40.29, fair $13.23; growth at the low end of the filer's own EPS objective (6%; a seller's figure, see the
  foundations): $32.29 to $40.29, fair $13.84; cap at own long-term debt share (61.4%): $27.90 to $40.29, fair $15.02; the
  2025 finance-lease addition ($1,239M, non-cash) left out of the debt credit: unchanged (the cap binds); the 69.8M forward
  shares and their $5,177M minimum proceeds added: the proceeds per share (about $74) exceed the range, so adding both
  raises value per share slightly and changes no conclusion; the all-spending case (owner cash -$2,598M a year): negative.
- **Whose tax.** The company paid little income tax in the window (income tax benefit of $245M in 2025) because of
  production tax credits, which the filer flows back to customers through rates (10-K Item 7: "PTCs flowed back to
  customers (offset by lower ETR)", $172M in 2025). CONVENTION of this run: owner cash is not recomputed at the statutory
  rate; rationale: the credits are passed through to customers in rates, so their expiry would raise revenue as it raises
  tax, and the text's shelter rule assumes a credit the owner keeps.
- **Q6's buyback line:** no repurchases of common stock (none in the fourth quarter of 2025, 10-K Item 5; none in the
  cash-flow statements of the window), so the buyback test has nothing to read against the bottom of the range.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9: COULD IT RUIN US? NOT REACHED. Facts are under AFTER THE STOP.
## Q10: IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT at Q5 (integrity, on doubt), integrity facts recorded, judged at Q5.** Q1 IN, Q2 IN, Q3 weighs against, Q4 IN on
the accounts and weighs against. The COMPUTATION beneath the stop: equity-only value range $20.13 to $40.29 a share
against $77.86 (2026-10-26); fair price $11.91 equity-only, all-equity not positive; no case of the range earns the floor
at the price, so Q7 would also have closed OUT. Q11 belongs to a holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q6, Part A (the money).** Common stock issued: proceeds $3,349M in 2025, $1,117M in 2024, $270M in 2023 (filed cash
  flows, `0000072903-26-000009`); shares outstanding 507.2M (2016) to 623.6M (end-2025), 49.2M in 2025; ATM programs of
  $4.0B (August 2025) and $4.3B (May 2026); forward sale agreements for 69.8M more shares outstanding at 2026-06-30
  (minimum proceeds $5,177M); the 2026-2030 plan calls for $7.0B of equity (10-K Item 7; 10-Q `0000072903-26-000154`). The
  serial-issuance row stands in the text as a candidate second STOP, unresolved **[L2014-015]**; the issue prices (about
  $74 a share on the forwards) sit above the computed range. Dividends: $1,282M paid in 2025; target payout 45% to 55%;
  annual increases of 4% to 6% are an objective (10-K Item 7). No repurchases of common stock. Deals: none. The parent
  bought $953M face of its own subsidiary's bonds for $712M in 2024 and 2025 (10-K note 5).
- **Q6, Part B (pay, board, owners).** CEO total compensation 2025 $15,998,859; CEO pay ratio 108 to 1; annual incentive
  2025 paid at 143.76% of target, funded only if ongoing EPS reaches guidance; long-term units 70% performance (ongoing EPS
  growth 30%, emissions 30%, nuclear ratings and wildfire mitigation 20% each, a relative TSR modifier of up to 30%) and
  30% time-based; combined chairman and CEO with a lead independent director; directors' holdings are mostly granted
  stock-equivalent units, with bought shares from none to 14,481 each (proxy, `0000072903-26-000063`).
- **Q8 (the bond).** The 30-year Treasury yields 5.31%; the no-growth case yields 2.75% on the price.
- **Q9 (the target's debt and exposures).** Debt $40.8B at 2026-06-30, 1.70 times equity; interest coverage by pre-tax
  earnings over interest charges **[L2012-002]** fell from about 3.6x (2016) to 2.75x (2020) and 2.2x (2025; about 2.1x
  without AFUDC-equity and the bond-repurchase gain and with the Marshall charge added back); short-term debt $2.51B plus a
  364-day term loan of $1.5B (drawn $750M) maturing January 2027; utilities may have to post collateral if rated below
  investment grade (10-K Item 1A); Xcel Energy Inc. depends on its subsidiaries' dividends, which commissions can limit;
  wildfire exposure in Colorado and Texas with excess liability cover of $450M and the Smokehouse Creek policy period
  nearly spent; the Texas Attorney General's suit over Smokehouse Creek seeks damages and civil penalties (10-K note 12).
  One utility's catastrophe is the rows' named case **[L2005-019]**; here there are four utilities in eight states.
- **Q12.** No business of the named kinds.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `f20df1e1`, before the first EDGAR call); written question by
      question; committed after each (Q1 `7a099560`, Q2 `1c677643`, Q3 `6ccc5fa7`, Q4 `93f1cc8f`, Q5 `ed35b4e0`, Q7
      computation `9bed0171`). **Declared:** the Q7 arithmetic script was written and run during the research, before Q2
      to Q5 were written (it was committed with Q1); its output file is headed COMPUTATION, NOT A CLEARANCE. I saw its
      result (the price far above every case) before judging Q5. The Q5 verdict rests on the integrity facts listed there
      and not on the price; the reader should know the order all the same.
- [x] Dispatched: the brief allowed per-question pathspec commits of my two paths; the lock and the fold are the
      dispatcher's (operator rule 10). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-27 XEL/check_ids.py`; every
      filing fact carries its accession; numbers without a row or a filing are labelled CONVENTION.
- [x] The order was kept; Q5 closed the file; nothing after it is a clearance, and the Q7 figures are headed so.
- [x] Owner cash after every real cost (stock pay, depreciation and nuclear fuel, wildfire payments inside operating cash),
      never a net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (the foundations, Q2's narrowing, Q5's facts for the other side); facts for
      the later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no row dated after an anchor is at issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; a defect in its debt-table sum is recorded at Step 0.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the final commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The utility debt credit counts finance leases but not the leased asset.** The 2026-10-23 text puts finance leases
in the long-term debt whose increase is credited, but a finance lease added without cash ($1,239M in 2025 here) buys a
plant that never passes through capital spending, so the credit can offset spending the lease did not fund; it did not
matter here only because the cap bound. (2) **The cap's weighting needs a rate base the filings do not tabulate.**
Allowed equity ratios are stated case by case, and electric rate base by state is not one table; I weighted by the rate
bases each case states, and the text does not say whether a verbal decision or a pending settlement counts as "stated".
The cap also takes the operating companies' allowed share while the holding company borrows on top of it (here about two
points of ROE), which the text does not address. (3) **Specific (a) has no reading for a non-cyclical business with an
aberrational year whose reversal sits inside the window** (Winter Storm Uri's deferral in 2021, recovered 2022-2023); I
used the window average and confessed it. (4) **Specific (f)'s fallback to sales growth is a poor measure for a utility,**
whose revenue is dominated by fuel costs passed through at cost (revenue fell from 2022 to 2025 while rate base grew);
kWh sales or rate base growth would measure the business, but the text names sales. (5) **Whose tax** assumes a credit the
owner keeps; production tax credits that a regulator passes to customers through rates need their own sentence. (6)
**Forward equity sales** (69.8M committed, unissued shares here) are not addressed by the share-count instructions. (7)
**The make-the-numbers rows speak of costs waved away and targets reached; the text has no sentence on a non-operating
gain kept inside the featured figure.** I judged it under the rows on hitting the number **[L2002-041]**, **[M2010-001]**,
and the operator may want the line drawn in the text, since it decided this file. (8) **The template's Q7 heading** asks
for growth spending "in year one" and "in year ten"; with the utility credit capped, the credit's year-one and year-ten
figures are as needed and the template has no line for them.
