# Company Run — IDACORP, Inc. (NYSE: IDA) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
5fca580d).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. The dispatching session
fills it at the fold. **Filled at the fold (2026-10-23, after the run was committed): not held** (`PORTFOLIO.md` read for IDA only).

**Contamination declared (seen by accident, not used).** (1) The directory listing of `Test Runs/` made to check this
file's name showed other run files dated 2026-10-23 (EDN, ENIC, ES, ETR, EVRG, FE, FTS, HE) and the session context showed
commit subjects of the HE run (OUT at Q7); none is about this company and none was opened. (2) The adopted case
`Framework/v5/CASE 2026-10-18 - the regulated utility's fair price, decided from the corpus.md`, read because Q7's regulated
utility paragraph cites it, lists utilities that closed OUT at Q7 on 2026-10-17 and 2026-10-18; Avista (AVA), one of this
run's comparison filers, is among them. Nothing of that list was used; Avista enters below only through its own filed
figures. (3) The session's memory index carries general lines about the queue; nothing about IDA. No file about IDA under any
name was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $142.06 (close 2026-10-22; Yahoo Finance chart endpoint through `tools/sources.py`; **aggregator, live quote
  only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: IDACORP, Inc. 57,842,043 common shares outstanding as of 2026-07-24
  (10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession `0001057877-26-000129`). `cover_shares.py` printed a
  second line, 39,150,812: those are Idaho Power Company's shares, "all held by IDACORP, Inc." (same cover), a combined
  filing's subsidiary count and not a second class; it is not added. Cross-check: the 10-Q balance sheet shows 56,115
  thousand shares issued and outstanding at 2026-06-30, and the 10-Q's Note 6 records an FSA settlement of 1,726,727 shares
  on 2026-07-13 (56,115K + 1,727K = 57,842K, agrees). No treasury stock is carried. `run.py` used the 10-K cover count
  (54.899M at 2026-02-13), now stale by about 2.9M shares; it is not used.
- **Unsettled forward sales (not in the count):** at 2026-07-24 the 10-Q states FSAs that "may be physically settled" for
  about $154M (2024 ATM), $262M (2026 ATM) and $299M (outside the ATMs), about $715M in all; at June 30 they stood at
  2,995,502 ATM shares and 4,484,296 shares of the 2025 series, less the 1,726,727 settled on July 13, so about 5.75M
  shares still to come (10-Q `0001057877-26-000129`, Note 6 and Liquidity). Shown beside the central figure at Q7.
- **Market cap:** 57.842M x $142.06 = **$8,217M** (about $9.03B with the forward shares and their $715M of proceeds).
- **Sovereign for the earnings currency (USD):** **5.29%**, US Treasury daily par yield curve, 30-year, 10/22/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-19, accession `0001057877-26-000028` (Items 1, 1A, 2,
  3, 5, 7 and 8, Notes 3, 6 and 22); 10-Q for Q2 2026, filed 2026-07-30, `0001057877-26-000129` (statements, Notes 6, 10,
  16, MD&A liquidity); DEF 14A filed 2026-04-02, `0001057877-26-000091`; 8-K 2025-05-30 `0001057877-25-000053` (Idaho rate
  case filed: capital structure about 49% debt and 51% equity, cost of debt 5.132%); 8-K 2025-12-31 `0001057877-25-000091`
  (settlement approved: 9.6% ROE, 7.410% authorized rate of return "based on the filed cost of debt and capital
  structure"); 8-K 2026-02-19 `0001057877-26-000029` and 8-K 2026-07-30 `0001057877-26-000130` (earnings releases,
  guidance); 10-K FY2022 `0001057877-23-000007` (cash flows 2020 to 2022, stock pay); 10-K FY2023 `0001057877-24-000005`
  (ADITC use in 2023); 10-K FY2020 `0001057877-21-000036` (stock pay 2018 to 2020). The 424B5 and 8-K of 2026-05-15 (the
  $600M ATM) were fetched; their terms are restated in the 10-Q and were read there.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, 2025, $601,838
  thousand in the filed IDACORP consolidated statement of cash flows (10-K `0001057877-26-000028`, page 81) against
  $601.8M in the XBRL series `run.py` printed. Agrees. Also checked: additions to property, plant and equipment 2025,
  $1,179,327 thousand filed against $1,179.3M tagged.
- **`python tools/run.py IDA` arithmetic lines only** (saved in `Test Runs/_research 2026-10-23 IDA/runpy_output.md`): OCF
  2023 to 2025 $267.0M, $594.4M, $601.8M; capex $611.1M, $1,009.3M, $1,179.3M; D&A $199.9M, $228.1M, $258.4M; finance
  lease principal 2025 $3.8M. **Stock pay was "n/f" in XBRL; resolved from the filed statements of equity:** share-based
  compensation expense $8.583M (2021), $10.279M (2022), $9.578M (2023), $11.708M (2024), $12.505M (2025); it is added back
  inside "Other non-cash adjustments" in operating cash flow and is deducted below. `run.py` does not see the joint-funding
  receipts from transmission partners, which the filed investing section shows as a separate inflow ($5.9M, $17.8M,
  $26.5M, $83.7M, $151.9M for 2021 to 2025): those are co-owners' reimbursements of the B2H and other line costs that the
  gross capex line includes, and capital spending is taken net of them. Nothing `run.py` prints as a rule, a floor or a
  verdict is used (Part VII).

## THE LINES OF EVIDENCE THIS NAME NEEDS (the brief's one departure: derived from the 10-K, Items 1, 1A and 7)
Chosen from the 10-K itself, in the order the filing's own risk discussion gives them weight:
1. **The regulatory compact: allowed return, earned return, and the lag between them.** Item 1 calls the authorized prices
   "critical factors"; Item 1A's first risks are rates that do not give "timely or sufficient recovery", and MD&A says the
   company filed rate cases in Idaho in 2023, 2024 and 2025 because of lag. Read: Note 3, the 2025 and 2023 settlements,
   the ADITC mechanism that supports the earned return.
2. **The capital programme and how it is financed.** Capital spending of "up to $7.2 billion" for 2026 to 2030 against
   operating cash of about $0.6B a year; the funding mix (first mortgage bonds, forward equity, the ATM). Read: Liquidity
   and Capital Resources, Notes 5 and 6, the 10-Q.
3. **Load growth and its concentration.** The 2025 IRP's 8.3% five-year retail sales growth forecast "include[s]
   significant large commercial and industrial additions"; Item 1A names stranded-cost risk if the new load does not come.
4. **Wildfire liability.** Item 1A says fires "have exposed, and in the future could expose" the company to claims; the
   neighbouring West has seen utilities ruined by them. Read: Item 1A, Note 11 contingencies, the Idaho Wildfire Standard
   of Care Act and the WMP filings.
5. **Water and power costs**, mitigated by the power cost adjustment; and the Hells Canyon relicensing (70% of hydro
   nameplate, licence pending since 2005).
6. **Concentration**: one industry, one region (Item 1A).
Why these: they are the six things the filer itself says can move its results; the business has one reportable operating
business ("Idaho Power's utility operations constitute nearly all of IDACORP's current business operations", Item 1).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what Idaho Power's regulated franchise will pay its owners, not
what the quotation will do. Margin of safety **[M1996-084]**: the decision must not need a pencil. No macro enters
**[M2000-094]**: the long rate is used as the yardstick at Q7, not forecast. Who is paid to tell you **[M2020-037]**: the
company's own 20-year load forecasts and its guidance are the seller's projections of what it sells and are read as such
**[M2011-083]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) owner cash after all capital spending
was negative in four of the five window years; the company has funded its dividend and growth with new debt and new
shares (cash flow statements, 10-K `0001057877-26-000028` and `0001057877-23-000007`); (2) the earned return has needed
tax-credit amortization to reach the regulatory floor in 2024 and 2025 ($29.8M and $40.3M); (3) about 5.75M more shares
are already sold forward; (4) Moody's outlook on both companies is "Negative" (10-K, Liquidity).

## THE STANDING RULE
Owning a part-interest bought for cash, unlevered and sized within the buyer's means, puts the buyer at no risk of ruin;
the rule binds the buyer's financing **[M2012-081]**, **[L2014-005]**. The target's own debt and wildfire exposure are
Q9's, not this rule's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test** is "a reasonable fix on about what the earning power and competitive position will look like in five or 10
  years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **The business, from Item 1:** a vertically integrated electric utility, about 664,000 retail customers (561,000
  residential) in southern Idaho and eastern Oregon; rates set on "cost of service" by the IPUC (about 95% of retail revenue)
  and the OPUC, transmission by FERC formula rate; 17 hydro projects (1,818 MW nameplate), gas and two co-owned coal-to-gas
  plants, long-term PPAs (mostly PURPA). The other subsidiaries (IFS, tax-credit housing, about $50M unamortized; Ida-West,
  44 MW of small hydro) are immaterial; there is one deciding part, the regulated utility.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (a) rate base, which grows with the capital the
  regulators admit; the company states 2026 to 2030 spending of $1.3B to $1.5B, $1.4B to $1.6B, and $3.6B to $4.1B (10-K,
  Capital Requirements); (b) the allowed return, 9.6% on Idaho equity in the 2023 and 2025 settlements and 9.5% in Oregon,
  and the earned return against it (lag, the ADITC backstop); (c) load, where customer growth (2.3% in 2025) and
  large-industrial additions drive the IRP's forecast; (d) water, whose cost effect passes largely through the PCA; (e) the
  tail: wildfire liability and regulatory climate. The first four are foreseeable to the degree the regulator's own process
  makes them: the IPUC and OPUC require a 20-year IRP every two years, so the industry's insiders do write the ten-year
  forecast down, the opposite of the case in **[M2000-105]**. The speakers' own reading of this business: "when you get an
  allowed return in the electric utility you’re almost certain of earning it, I mean, if you behave yourself" **[M2010-037]**.
- **The doubt, stated:** "if you have doubts about something being into your circle of competence, it isn’t"
  **[M2002-092]**. The doubt here is not about the economics but about one tail (fires); a tail is a matter of loss, which
  the framework weighs at Q9 and at Q2's "what could destroy it", not a forecast that cannot be made. The figures tell the
  future figures in the sense of **[M2008-069]**: rate base, allowed return and the capital plan are filed.
- **Routing:** not a fast-changing industry; not a bank; not a holding company of parts that matter (one part decides).
- **VERDICT: IN.** The ten-year economics of a cost-of-service utility can be foreseen from its filings and its regulators'
  orders **[M2012-065]**, **[M2010-037]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**.

- **The attacker with money** **[M2011-015]**: an attacker with any sum could not build a second wire network to the same
  664,000 customers: "In return for agreeing to provide service to all customers within a defined service area, electric
  utilities are typically provided with an exclusive right to provide service in that service area" (10-K Item 1,
  Competition). The castle is a legal franchise, held in 69 Idaho and 9 Oregon cities and certificated in 25 Idaho and 3
  Oregon counties. The filer names its only rivals as "fuel distribution companies, including natural gas providers" for
  heating and appliances, and "customer-owned solar and other forms of distributed generation". A franchise of this kind
  is what Munger describes when he says pricing power means "a monopoly or a near monopoly" **[M2010-092]**; here the
  regulator holds the power on the customer's behalf.
- **Pricing power and the agony before a rise** **[M2005-020]**: the agony is institutional. Every rise is a public rate
  case with intervenors; in 2025 the company asked for $199.1M of Idaho revenue (8-K `0001057877-25-000053`) and the
  settlement gave about $110.0M (8-K `0001057877-25-000091`), at 9.6% on equity where it asked 10.4%. The castle does not
  let the owner raise price; it lets the owner earn the allowed return on what it invests.
- **Unit volume** **[M1999-054]**-type evidence: retail MWh 15,515K (2023), 15,971K (2024), 16,177K (2025); customers
  +2.3% in 2025; peak demand records in 2024 (3,793 MW summer). Against it: weather-adjusted residential use per customer
  fell from 1,032 kWh (2012) to 922 kWh (2025) (Item 1A), the slow erosion distributed generation and efficiency bring.
- **The low-cost position, the brand, the low bid**: not the tests that apply to a franchise monopoly; the customer has no
  choice of distribution provider. Hydro supplies 52% to 55% of own generation (Item 1), which keeps power costs low, but
  the filing gives no comparison of rates with neighbours and none is claimed.
- **Ask the competitors / widening or narrowing** **[M1999-108]**: the franchise is unchanged in extent since the last
  cycle except by the company's own choice to sell its Oregon distribution (about 5% of retail revenue) to OTEC, a
  cooperative, for a $154M base price (10-K Note 22). The 10-K also records the threat to the edge of the castle: a
  municipality or tribal area "may elect not to take service from Idaho Power" and buy the distribution plant within it.
- **What could destroy, modify or reduce it** **[M2000-014]**: (a) the regulatory compact, which "can break": "the
  regulatory climate in a few states has raised the specter of zero profitability or even bankruptcy" **[L2023-011]**.
  Idaho's own record over the cycle is of settlements at 9.6% and of a 2025 statute, the Wildfire Standard of Care Act,
  under which an IPUC-approved mitigation plan "establishes the utility's duty" (10-K, MD&A, Other Matters, under the
  heading for the Act), the reverse of the California climate the row describes. (b) Wildfire liability: the filer says fires
  "have exposed, and in the future could expose" it to claims, insurance "may not be sufficient", and it "regularly
  received claims" none of which it deems material (10-Q Note 10). One fire can be the "one zero" of a single-state
  utility; that is a loss question, carried to Q9 (whose answer here falls after the stop) and weighed there, not a sign
  that the franchise itself is filling in. (c) Slow change, "much harder to perceive" **[M2014-038]**: rooftop solar and
  falling use per customer.
- **The competitor row** (CONVENTION of this run: the 10-K names no rival company, only rival fuels and distributed
  generation; it names five interconnected neighbours, BPA, Avista, PacifiCorp, NorthWestern Energy and NV Energy. The
  comparison filers are the neighbours that file their own SEC statements with their own XBRL: Avista and NorthWestern.
  BPA is a federal agency and does not file; PacifiCorp's and NV Energy's figures sit inside Berkshire Hathaway Energy's
  combined filing and were not read for the metric; flagged.) Metric: net income over average common equity, from each
  filer's XBRL company facts (transcription of the filed 10-Ks; Avista latest 10-K `0001193125-26-067872`, NorthWestern
  Energy Group `0001993004-26-000006`, NorthWestern Corp `0000073088-23-000028` for the years before the holding company):

  | Year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | IDACORP | 9.4% | 9.6% | 9.8% | 9.6% | 9.4% | 9.4% | 9.5% | 9.1% | 9.3% | 9.4% | 9.5% |
  | Avista | 8.6% | 6.9% | 7.8% | 10.6% | 6.5% | 7.0% | 6.9% | 7.1% | 7.1% | n/f | 7.6% |
  | NorthWestern | 10.0% | 9.4% | 10.5% | 10.2% | 7.5% | 8.5% | 7.3% | 7.1% | n/f | n/f | 8.8% |

  (n/f: the year-end equity was not in the framed XBRL series fetched; not filled from any other source.) Over the same
  span all three spent more on plant than they took in from operations (IDACORP 2016 to 2025: OCF $4,204M against capex
  $4,982M). IDACORP's 2024 and 2025 returns include $29.8M and $40.3M of additional ADITC amortization (10-K, Note 3);
  without it the two years read about 8.3% and 8.2%.
- **The field's returns over the last full cycle, judged in words:** ordinary. The durable players earn 7% to 10% on equity,
  a return set by the regulator, never the "excellent returns" a moat protects **[L2007-004]**. Section C's exception
  governs: a return set by a regulator is carried to Q3 as a second best **[M2009-104]**, **[L2009-012]**, not closed OUT.
- **The parts table:** one part. The regulated utility carries all but a few million dollars of operating profit (Item 1:
  "nearly all"); it decides.
- **VERDICT: IN.** The castle is a legal franchise that a well-funded attacker cannot cross **[M2011-015]**; what it
  protects is a regulator-set, ordinary return, which section C carries to Q3 as a second best **[M2009-104]**,
  **[L2009-012]**. The regulatory compact and the fire tail are named as the things that could take it down **[L2023-011]**,
  **[M2000-014]**; on Idaho's record over the cycle neither shows the castle filling in.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital the business needs.** The regulator fixes it: 9.6% on Idaho equity and a 7.41% overall return on
  an Idaho rate base of about $4.9B (2025 settlement), 9.5% and 7.302% in Oregon on $188.9M (10-K Note 3). Earned: about
  9.1% to 9.8% on average common equity in every year 2016 to 2025 (Q2 table), but in 2024 and 2025 only with $29.8M and
  $40.3M of additional ADITC amortization, the IPUC mechanism that gives the company "the ability to earn a minimum Idaho
  ROE" (now 9.12%) by amortizing tax credits (10-K FY2023 `0001057877-24-000005`, Note 3; 10-K FY2025 Note 3). No additional
  ADITC was used in 2018 to 2023 ("the full $45 million of additional ADITC remained available" at end 2022, 10-K FY2022;
  none needed in 2023, 10-K FY2023). The return is decent and regulated, "fair, not rich" in the framework's words: "there’s
  no way we get rich on our utility investments. But there’s no way we get poor, either" **[M2009-104]**.
- **What the added capital has earned** **[M2014-086]** ("measured by the operating earnings after depreciation"): from 2020
  to 2025 common equity rose $1,012M (2,560.0 to 3,571.9) and net income attributable rose $86.1M (237.4 to 323.5), 8.5%
  on the added equity; with the 2025 tax-credit amortization taken out, $45.8M, 4.5%. From 2023 to 2025: equity +$664M,
  net income +$62.3M (9.4%), or +$22.0M without the credits (3.3%). The 2026 rate increase of about $110M lands after the
  window, so the incremental figure is read at a lag trough; the company's own 2026 guidance of $6.30 to $6.45 a share
  still assumes "less than $15 million" of credits (8-K `0001057877-26-000130`). The incremental return is decent at best
  and below the allowed 9.6% on the evidence of the last three years **[L2009-012]**.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**: D&A averaged $207.9M over 2021 to 2025
  (rising from $179.4M to $258.4M, partly accelerated coal depreciation at Bridger and Valmy, Note 3); net capital spending
  (gross additions less partners' reimbursements) averaged $649.3M and reached $1,027.4M in 2025; the plan is $1.3B to
  $1.6B a year to 2030. The filing splits the spending by asset (transmission, distribution, thermal, hydro, general plant,
  resources) and not by maintenance against growth, so the maintenance guess at Q7 is depreciation, the proxy the rows call
  "not inappropriate in most companies" **[M1998-127]**, stated as a guess **[M2000-144]**.
- **Compulsory reinvestment** **[M1997-016]**, **[M1998-128]**: the obligation to serve all comers in the territory makes
  the growth spending compulsory, not optional: the IRP's capacity deficits and peak records drive it, and the company
  says "the company incurs the cash requirements of constructing and the costs of financing" before rates follow (MD&A,
  Overview). "To earn more, their owners must invest more" is said of exactly these businesses in **[L2011-019]**.
- **Cash at the end of the year** **[M2008-036]**, **[M2003-122]**: operating cash less all net capital spending and stock
  pay was +$60.6M, -$73.8M, -$327.2M, -$342.9M, -$441.9M for 2021 to 2025; the dividend ($146M rising to $188M) and the
  growth were paid with $1,471M of net new long-term debt and $396M of new shares in the window, and $715M more in forward
  sales. The business "reports the 12 percent on capital but there’s never any cash" **[M2003-122]**, at 9% rather than 12.
- **The growth arithmetic and its caps:** the company's growth is rate-base growth at the allowed return; it cannot run past
  the discount rate in owner cash because each dollar of it needs a dollar of new capital. Growth here can destroy value at
  the price if the return on the added equity sits below what the buyer must earn **[L2000-023]**; that is Q7's test.
- **WEIGHS AGAINST.** A capital-heavy, compulsory reinvestor whose added capital has earned a decent regulated return at
  best and less than allowed lately, accepted by the rows only as a second best **[M2018-055]** and only on "decent returns
  on the incremental sums they invest" **[L2009-012]**; it throws off no cash after its spending **[M2003-122]**. (The
  "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (`run.py` table from each year's first-filed XBRL, the 2024,
  2025 and 2026-06-30 columns read on the filed statements, 10-K `0001057877-26-000028` and 10-Q `0001057877-26-000129`;
  USD millions):

  | Year-end | Assets | Equity | Cash | Receivables | LT debt (non-current) | Retained earnings |
  |---|---|---|---|---|---|---|
  | 2016 | 6,290 | 2,154 | 61 | 72 | 1,745 | 1,323 |
  | 2017 | 6,045 | 2,251 | 77 | 75 | 1,746 | 1,427 |
  | 2018 | 6,383 | 2,370 | 267 | 77 | 1,835 | 1,532 |
  | 2019 | 6,641 | 2,465 | 217 | 73 | 1,737 | 1,635 |
  | 2020 | 7,095 | 2,560 | 275 | 73 | 2,000 | 1,734 |
  | 2021 | 7,211 | 2,668 | 215 | 79 | 2,001 | 1,834 |
  | 2022 | 7,543 | 2,807 | 178 | 114 | 2,194 | 1,938 |
  | 2023 | 8,476 | 2,908 | 327 | 107 | 2,776 | 2,036 |
  | 2024 | 9,239 | 3,331 | 369 | 115 | 3,054 | 2,150 |
  | 2025 | 10,225 | 3,572 | 216 | 98 | 3,331 | 2,285 |
  | 2026-06-30 | 10,866 | 3,775 | 84 | 111 | 3,678 | 2,358 |

  **What moved and why.** Assets grew 63% in nine years, almost all of it in plant: utility plant in service net $5.65B and
  construction work in progress $1.74B at end 2025 (CWIP was $1.24B a year earlier), plus a $220M finance-lease
  right-of-use asset for a leased battery facility that first appears in 2025. Long-term debt nearly doubled (1,745 to
  3,331, then 3,678 at June 2026, plus $116M current and $217M of finance-lease liability); equity grew 66%, from retained
  earnings (up $962M) and from new shares from 2024 (common stock account $888.6M at end 2023, $1,301.9M at end 2025,
  $1,431.6M at June 2026). Debt as a share of debt plus equity rose from about 45% (2016) to about 51% (2025, with the
  finance lease), the company's own covenant figure being 52% (10-K, Liquidity). No goodwill; no intangibles of note.
  Receivables stayed near $100M against revenue rising from $1,262M to $1,813M, which says the revenue is collected.
  What the balance sheet says that the income account does not: regulatory assets of $1,428M non-current plus $137M
  current (pension, power-cost and wildfire deferrals among them) against regulatory liabilities of $1,031M, the record of
  costs the company has spent and expects the commissions to let it collect; and the Hells Canyon relicensing, $536M sitting
  in CWIP since the licence expired in 2005, with a $281M regulatory liability for financing costs already collected in
  cash from customers against it (10-K, Capital Requirements). What it cannot say: whether the commissions will allow every
  deferred dollar; the 10-K says recovery is not assured ("may not allow").
- **The income account and the real costs.** Depreciation is a real cost here **[R1996-023]** and is if anything inflated by
  the accelerated coal schedules; stock pay ($8.6M to $12.5M a year) is expensed and deducted at Q7; no restructuring
  charges recur; no EBITDA anywhere in the 10-K, the releases or the proxy (text search, zero hits). Two items in net
  income are not cash: the allowance for equity funds used during construction ($62.5M in 2025, $53.2M in 2024, $43.2M in
  2023), which is a return booked on plant not yet in service, and the additional ADITC amortization ($40.3M, $29.8M, nil).
  Together they were 31% of 2025's $323.5M. Both are regulator-prescribed, both are disclosed in the MD&A's own
  reconciliation, and operating cash flow (used at Q7) excludes both.
- **The make-the-numbers habit, guidance, the featured figure.** The company gives annual EPS guidance and reports against
  it: 2025 earnings "were at the top-end of the previously increased earnings guidance range", and the guidance itself
  states how much tax credit it expects to use ("less than $15 million", 8-K `0001057877-26-000130`; "less than $30 million"
  at the February release, `0001057877-26-000029`). The proxy celebrates an "18th consecutive year of earnings per share
  growth" (DEF 14A `0001057877-26-000091`). On the filed figures, the streak held in 2024 only with the credits: 2023 EPS
  $5.14 with none; 2024 $5.50 with $29.8M (about $0.57 a share on 52.6M diluted shares). These are recorded as a weighing
  against and carried to Q5 **[L2002-041]**, **[L2019-006]**. The figure featured is GAAP EPS, not an adjusted one.
- **Confusion or suspicion?** Neither. The accounts are complicated by rate regulation, not obscured: each regulatory
  mechanism is explained, quantified and reconciled in Note 3 and the MD&A bridge, which is the "clear terms" the rows
  count as a plus **[M1994-018]**; nothing in the balance sheets builds suspiciously (receivables and inventories track
  the business; the deferrals have orders behind them). The test of **[M1995-063]** is not met.
- **VERDICT on the accounts: IN (no STOP); WEIGHS AGAINST, lightly.** The reported earnings overstate the cash the owner can
  take out by the AFUDC equity and tax-credit lines and by the capital the business must keep adding **[R1996-023]**; the
  guidance habit, kept by a tax-credit backstop, goes to Q5 **[L2002-041]**. The recast cash figure feeds Q7.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
*(pending)*

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The people** (10-K, Executive Officers; DEF 14A `0001057877-26-000091`): Lisa A. Grow, president and CEO since June
  2020; Brian Buckham, CFO (general counsel before 2022); Adam Richins, COO since 2019. The chair is a separate,
  independent director, Dennis L. Johnson; the two posts have been separated "since 1999" (proxy). A whole-company
  management in place; for a stock, the rows read rather than meet **[M2007-081]**.
- **The first yardstick, the record against the hand dealt** **[M1994-008]**: the hand is a fast-growing territory
  (customers +2.3% in 2025, peak records in 2024) under cost-of-service rates set on historic test years, which builds lag
  into every year of heavy spending. On that hand they have obtained three Idaho rate orders in three years (2023 general,
  2024 limited-issue, 2025 general), moved coal units to gas, begun B2H after a decade of permitting, and kept both ratings
  investment-grade (Moody's Baa2/Baa1 with a negative outlook, S&P BBB stable). Against the hand: the earned Idaho return
  slipped below the 9.12% floor in 2024 and 2025 before the tax credits, and the cash shortfall widened every year.
  Rivals over the same span (Q2 table) earned less on equity.
- **The second yardstick, the treatment of owners; the proxy** **[M1994-009]**: CEO total pay $7.53M in 2025 ($5.79M
  without the pension value change), against 36,312 shares owned (about $5.2M at the price); directors' holdings are small
  and in large part deferred stock units granted as pay, not the experience of "purchasing shares with their savings" **[L2019-008]**.
  The proxy discloses plainly the relatives of officers on the payroll (the CEO's son-in-law among them) and a 40-year
  law-firm relationship with an officer's spouse's firm; these are disclosed with their terms, which is the candour the
  rows ask for **[M1998-036]**, and none is large.
- **The tells of dishonesty**: none found in the documents read. No adjusted earnings figure; no restatement; no EBITDA
  talk; the reports explain each regulatory mechanism in numbers. The 10-K and releases say where earnings came from,
  including the tax credits ("the use of tax credits under the company's Idaho regulatory mechanism", 8-K
  `0001057877-26-000029`), which is the opposite of the report that "dances" around its key figure.
- **The habits carried from Q4, read with the integrity record** **[M2013-088]**: annual EPS guidance, results "at the
  top-end" of a "previously increased" range, an 18-year streak of EPS growth that in 2024 rested on $29.8M of tax-credit
  amortization. The rows grow "downright incredulous" of managers who "consistently reach their declared targets"
  **[L2002-041]** and name guidance a "scourge" **[L2019-006]**. Read with the rest: the credit is not a choice of accounting
  but an IPUC-designed backstop that gives "the ability to earn a minimum Idaho ROE" and is sized by formula to reach it,
  disclosed in every release with its amount, and capped by the commission; the guidance itself names how much of it will
  be used. That is preoccupation with the number, a "negative" the rows will not make "a total exclusionary factor"
  **[M1994-018]**; it does not raise a doubt that the figures are false or the people dishonest.
- **Love of the business, and the owner question** **[M2017-029]**: not answerable from the documents for a stock; the
  succession is internal (the 10-K lists every executive officer in an Idaho Power or IDACORP post for at least the past
  five years, the CFO and COO promoted from within in 2026).
- **VERDICT on integrity: IN** on the documents read; no doubt formed **[M2013-088]**. **Ability WEIGHS FOR, lightly**: a
  good record on a hard regulatory hand **[M1994-008]**, with the number-making habit carried as a negative **[M1994-018]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**: over 2021 to 2025 the company earned $1,378M (net income
  attributable), paid $829M of dividends and kept $549M, and raised $396M more from new shares (cash flow statements). On
  the market leg, the 10-K's performance graph shows $100 at end 2020 becoming $153.24 at end 2025 with dividends
  reinvested, against $143.83 for the EEI Electric Utilities Index and $195.96 for the S&P 500 (10-K Item 5), and the stock
  sells at about 2.1 times book ($142.06 against $67.27 of equity per share at June 2026): by the market's measure each
  retained dollar has been worth more than a dollar **[M2011-072]**. By the 2009 form of the test the book-value gain
  (about 50.7 to 65.1 a share, roughly 28% in five years) fell short of the S&P's **[R2009-002]**. On intrinsic value, the
  added equity has earned 4.5% to 8.5% (Q3), below the floor a buyer applies at Q7. Mixed, leaning against.
- **Dividends while issuing shares.** The company pays out about 58% of reported earnings (2025: $188.5M of $323.5M) and
  in the same years sells new shares and forward contracts for more than it pays out ($396M in 2024 and 2025, $129M in the
  first half of 2026, about $715M more contracted). The rows' rule is that a company should pay out what it "can't" employ
  **[M2004-089]** and keep "a dollar in the business" only if it is worth more than a dollar there **[M2000-050]**; this
  company can employ more than it earns and pays out anyway, then raises the money back at a cost. The policy is "clear,
  consistent" **[L2012-015]**, but the circle costs fees and tax for the owners who take the dividend. Weighs against.
- **Buybacks:** none in the window (cash flow statements 2021 to 2025 show only tax withholdings on share awards; 10-K
  Item 5: no repurchases in the fourth quarter of 2025). **Buyback test, written back from Q7:** no programme and no prices
  paid, so there is nothing to read against the bottom of the range ($70.72, equity-only); the test is not engaged. The
  issue prices are read instead: every share sold in the window and since ($107.78 and $108.17 on the 2025 series, about
  $139.5 on the 2026 forwards) was sold above the top of Q7's equity-only range ($91.45 at the government rate), so the
  continuing owners received more in cash than the business value they gave **[R1995-010]**; on price the issuance did not
  harm them, the inverse of **[M1996-013]**. *(written back with Q7, as the brief requires.)*
- **Issuance and deals** **[R1995-010]**, **[M1996-013]**: no acquisition, no stock deal; the one disposal (Oregon
  distribution, $154M base price, to a cooperative) is small. The shares were issued for cash: 2025 series forward sale
  price $107.67 initially, settled at $107.78 and $108.17; 2026 ATM forwards at an aggregate $418.0M for 2,995,502 shares,
  about $139.5 a share (10-Q Note 6). Whether those prices gave away value is read against Q7's range (line written back
  at Q7). Serial issuance is the framework's unresolved candidate second STOP, "hell-bent on issuing shares" **[L2014-015]**;
  here the issuance is announced in advance as the funding of a stated 50/50 regulated capital structure (10-K, Liquidity),
  which is not the promotion the row describes; it is weighed, not applied as a STOP (Part VI leaves it open).
- **The all-stock deal STOP** **[L2009-019]**: no such deal. Not triggered.
- **Part A WEIGHS AGAINST.** The money kept and raised goes into compulsory plant at a regulated return below the buyer's
  floor, and a dividend is paid out of money that is then borrowed and raised back **[M2004-089]**, **[M2000-050]**.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls, and a capital charge** **[M2003-019]**, **[M2009-081]**, **[L1994-019]**: the
  short-term plan is 70% "adjusted net income" (target $308M for 2025; actual net income $323.5M, which included the $40.3M
  tax-credit amortization) and 30% customer satisfaction and reliability; the long-term plan is cumulative EPS and relative
  TSR against the EEI index (DEF 14A). The 2023 to 2025 award paid 163% of target, 200% on the CEPS goal. No element
  charges management for the capital it employs, in the most capital-hungry business a buyer can own, and both EPS and net
  income rise mechanically as rate base is funded with new shares and debt. The rows require "a capital cost element" in a
  capital-intensive business **[M2009-081]**. Against. (The committee also used "preservation of" ADITCs as a pay metric in
  2024 and dropped it for 2025, DEF 14A, short-term incentive metrics.)
- **The chimpanzee test** **[M2004-097]**: a regulated monopoly whose return is set by order is close to the case the row
  describes; paying on net income against a budget that already embeds the rate orders pays partly for the commission's
  decisions. Against, lightly.
- **The board** **[L2014-026]**: an independent chair, separate from the CEO since 1999, is what the row asks; directors
  paid about $250,000 each (chair $362,959), holding mostly granted units **[L2002-033]**, **[L2019-008]**. Mixed.
- **Owners as partners**: candid filings, no splits, no political spending found; the guidance habit counts against the
  "positions reversed" standard as it does at Q5.
- **Part B WEIGHS AGAINST**: pay on EPS and net income with no capital charge in a capital-intensive business
  **[M2009-081]**; the board's structure is a plus **[L2014-026]**.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L1994-007]**, as a range **[L2000-024]**. Arithmetic in
`Test Runs/_research 2026-10-23 IDA/q7.py`, output `q7_output.txt`; inputs are the filed cash flow statements (10-K
`0001057877-26-000028` for 2023 to 2025, 10-K `0001057877-23-000007` for 2021 and 2022). USD millions unless a share figure.

**The basis.** The deciding part earns a return a regulator allows on its invested capital, so Q7's regulated-utility
paragraph governs: the central figure is the **equity-only basis**, owner cash after interest and after the company's tax,
against the market value of the shares, with the long-term debt raised over the window to fund the plant credited against
the spending it funded, up to the regulator's allowed debt share **[L2017-012]**, **[L2010-012]**, **[M2014-086]**. The
allowed share: Idaho's 2025 settlement set a 7.410% return "based on the filed cost of debt and capital structure" (8-K
`0001057877-25-000091`), and the filing proposed about 49% long-term debt at 5.132% and 51% equity (8-K
`0001057877-25-000053`); 0.49 x 5.132% + 0.51 x 9.6% = 7.41%, which confirms it. **49%** is used (Oregon's 50% applies to
a rate base of $189M against Idaho's $4.9B). The all-equity figure is shown beside and does not decide.

**Owner cash by year** (OCF as filed; less stock pay; less gross additions to plant net of transmission partners'
reimbursements; less finance-lease principal):

| | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| Operating cash flow | 363.3 | 351.3 | 267.0 | 594.4 | 601.8 | |
| Stock pay | 8.6 | 10.3 | 9.6 | 11.7 | 12.5 | |
| Net capital spending | 294.1 | 414.8 | 584.6 | 925.6 | 1,027.4 | 649.3 |
| D&A (maintenance guess) | 179.4 | 173.6 | 199.9 | 228.1 | 258.4 | 207.9 |
| Owner cash, all spending | 60.6 | -73.8 | -327.2 | -342.9 | -441.9 | -225.0 |
| Owner cash, maintenance only | 175.2 | 167.5 | 57.5 | 354.6 | 327.2 | 216.4 |
| Net new long-term debt | 0.0 | 193.6 | 647.0 | 250.2 | 380.1 | 294.2 |

- **The debt credit:** net new long-term debt over the window $1,471.0M (issued $1,770.0M less $299.0M retired) against a
  cap of 49% x $3,246.6M of net capital spending = $1,590.8M; the credit is the full $1,471.0M, **$294.2M a year**.
  CONVENTION of this run: the credit uses debt issued *net of retirements*, because a bond that refinances a maturing one
  funds no new plant; rationale: the paragraph credits "the long-term debt raised over the window to fund the fixed assets",
  and refinancing does not fund them. Beside it: gross issuance capped at $1,590.8M gives $318.2M a year; capping year by
  year (2023's $647.0M cut to $286.5M) gives $222.1M a year.
- **(e) The maintenance case is central**, the filing allowing the guess at depreciation **[M1998-127]**, **[M2000-144]**
  (Q3). Owner cash after maintenance only averages **$216.4M**. The growth spending, $441.4M a year (net spending less D&A),
  is charged against the growth it buys, and the debt credit is applied to it: equity-funded growth spending **$147.2M a
  year** ($441.4M less $294.2M). The credit is not applied to the maintenance spending, since plant held level needs no new
  debt. The all-spending, credited figure ($216.4M less $147.2M = **$69.2M**) is shown beside; held flat forever it would
  charge growth spending without the growth, which (e) forbids.
- **(a) Cycles:** neither end year is aberrational on the filer's own description; 2023's low operating cash (power-cost
  deferrals in a poor water year, PCA) is an interior year inside the average. The literal window is the window used.
  `run.py`'s literal as-filed means are shown for the record: 5-year owner earnings on gross capex -$270.9M, on D&A $227.7M
  (both before stock pay and partners' reimbursements).
- **(b) Decline:** none in the maintenance series. The all-spending credited series changes sign (halves: +$90.2M, then
  -$77.2M), so it has no meaningful growth rate; it enters only as the figure beside.
- **(c) Acquisitions:** none in the window. **The signed, unclosed deal, beside:** the Oregon sale to OTEC, $154M base
  price, expected within a year of 2026-06-30, subject to OPUC, IPUC and FERC approval (10-Q Note 16); Oregon is about 5%
  of retail revenue (Item 1). Valued as if closed, $154M of cash against about 5% of the maintenance owner cash ($10.8M a
  year, $205M at the government rate): about -$0.9 a share. It does not move the box.
- **(d) Working capital** is inside operating cash flow, with the regulatory deferrals.
- **(f) The cap:** the maintenance series grew 16.9% a year from 2021 to 2025 (halves $171.3M to $340.9M). Carried ten
  years that rate would put owner cash near a third of sales, against a highest share of sales in the filings read of
  19.4% (2024): an absurdity **[M1999-067]**. The growth carried is cut to the company's own sales growth over the window,
  **5.60%** a year ($1,458.1M in 2021 to $1,813.0M in 2025), below the discount rate; zero nominal growth after year ten
  **[M1997-095]**.
- **Whose tax:** owner cash is after the company's actual cash taxes (paid $34.3M, $45.9M, $6.2M, $25.2M, $24.5M), below
  the statutory rate because of flow-through and investment tax credits. CONVENTION of this run: the shelter rule of
  "Whose tax" is not applied, because under cost-of-service rates the tax saving passes to customers through rates and a
  higher tax would be recovered in rates, so the shelter is not owner cash that runs out; rationale: the rate orders, not
  a carryforward schedule, decide it. Sensitivity: at the 21% federal rate on average pre-tax income ($297M), owner cash
  would be about $35M a year lower. It does not move the box.

**The range, equity-only (central):**

| Case | Owner cash | Value at 5.29% | Per share | At the floor (10%) per share |
|---|---|---|---|---|
| No growth, maintenance only | $216.4M | $4,091M | **$70.72** | $37.41 |
| Growth at 5.60% for ten years, equity-funded growth spending $147.2M charged | $216.4M rising | $5,290M | **$91.45** | $39.32 |

Shares 57.842M (cover, 2026-07-24). Width 1.29 to 1. Growth adds value at the government rate and almost none at the
floor: the added plant earns more than 5.29% and little more than 10% on the equity that funds it **[L2000-023]**.

**Beside (not deciding):** all-spending credited, no growth: $22.60 a share; growth case with 2025's equity-funded growth
spending ($388.9M) in place of the average: $59.64; with the forward-sold shares settled (about 5.75M shares, $715M cash):
about $75.6 and $94.4. **All-equity basis** (owner cash before after-tax interest, $81.5M a year added back at 21%; net
debt $3,737M = long-term debt $3,677.9M + current $116.3M + finance lease $213.6M - cash $83.6M at 2026-06-30, less the
$186.8M FSA settlement of 2026-07-13 that the 10-Q states; the July repayment of $116M of pollution control bonds nets to
zero; operating leases and the finance lease's current portion left out, said so): no growth $32.73, growth $29.83 at
5.29%.

**The floor, tested first** (CONVENTION, Q7): at $142.06 the market value is $8,217M. The no-growth case returns 2.63% a
year on that price; the growth case's expected return, solved, is **3.69%**. No case in the range earns the floor of about
ten percent **[M2003-149]**; the file closes OUT whatever the width. The price also sits above the top of the range, which
closes OUT by the same convention. Nothing here is close enough to need the screamer test **[M2009-005]**.

- **Value range (equity-only, central): $70.72 to $91.45 a share against $142.06.**
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, the two averaged,
  after the company's own tax: **$38.36 a share on the equity-only basis (central for a regulated utility)**; the
  all-equity figure beside is **-$24.49** (not positive: at ten percent the business before interest is worth less than
  its net debt). No cheap price is reported.
- **VERDICT: OUT.** No case earns the floor at the price **[M2003-149]**; "there’s just a point at which we drop out of the
  game" **[M2003-149]**. The rows' own reading of the field holds: "some utilities have sold at extraordinary prices. And we
  can’t pay them" **[M2017-095]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** Q7 closed the file OUT. (The bond fact is recorded under AFTER THE STOP.)

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts recorded under AFTER THE STOP, not weighed.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** Inaction is the default; nothing is a pitch at this price.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED** (after the stop; not asked by the operator). No business named in Q12's list is involved (a fact, not a
judgment).

---
## THE BOX
**OUT at Q7, on the floor.** Equity-only value range **$70.72 to $91.45 a share** (central for a regulated utility:
maintenance case, growth carried at the company's own sales growth of 5.60%, the debt raised over the window credited
against the growth spending up to the regulator's 49% debt share) **against $142.06**; the price earns 2.6% (no growth) to
3.7% (growth) a year, below the floor of about ten percent on every case. Fair price (reporting figure): **$38.36
equity-only**; all-equity **-$24.49**. Q1 IN; Q2 IN (legal franchise; regulator-set ordinary return carried as a second
best); Q3 weighs against; Q4 no STOP, weighs against lightly; Q5 integrity IN, ability for lightly; Q6 Part A and Part B
weigh against. Q8 to Q12 not reached. Not TOO HARD: the deciding question was answered.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down with their sources **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).
- **Q8 (the bond):** the 30-year Treasury yields 5.29% (US Treasury par curve, 2026-10-22); the maintenance owner cash
  yields 2.63% on the price (Q7 arithmetic).
- **Q9 (debt and exposures):** long-term debt $3,677.9M non-current and $116.3M current at 2026-06-30, plus a $213.6M
  finance lease (10-Q `0001057877-26-000129`); maturities at end 2025 were $116.3M in 2026 (repaid July 2026), none in
  2027 to 2029, $80M in 2030 and $3,265M thereafter; first mortgage bonds outstanding $3.461B; effective debt cost 5.13%
  (10-K Note 5). Covenant leverage 52% against a 65% limit; $500M of undrawn credit facilities and no commercial paper at
  2026-02-13 (10-K, Liquidity). In 2025 interest charged was $204.4M ($174.9M on long-term debt and finance leases, $29.5M
  other) against pre-tax income of $310.4M, which itself includes $62.5M of non-cash equity AFUDC. Moody's outlook
  negative on both companies, S&P stable; a downgrade can require collateral to be posted under credit-risk-related
  contingent features (10-K Item 1A and Item 7A; the dollar figure was cut off in the text extraction read and is not
  recorded). Wildfire: Item 1A says fires "have exposed, and in the future could expose" the company to claims, that
  insurance "may not be sufficient", and that recovery of uninsured losses in rates is not assured; the 10-Q says claims
  arrive "regularly" and the existing ones are not material; Idaho's Wildfire Standard of Care Act (2025) ties the utility's
  duty to an IPUC-approved mitigation plan, filed 2025-10-10. One region, one industry (Item 1A). The Hells Canyon licence
  ($536M in CWIP) has been renewed year by year since 2005 while the new one is pending. The "little or no debt" criterion
  **[R1997-001]** is stated for whole businesses offered to Berkshire.
- **Q10, Q12:** nothing beyond the above.
No integrity facts are carried after the stop: Q5 was reached and answered.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 5fca580d). **Written question by question and committed, with two
      departures declared:** (1) the research for all questions (filings, XBRL series, and the Q7 arithmetic in `q7.py`) was
      gathered before the Q1 section was written, so valuation arithmetic existed in the research folder before Q1 to Q4
      closed in the run file; it carried no entry language and entered the run file only at Q7 (operator rule 3 kept in
      substance; write-early bent in its order); (2) Q3 and Q4 were committed together (eea1e6fb), and Q5 and Q6 together
      (5db29557); Q1 (ee316775), Q2 (a3b72f4f) and Q7 with the Q6 buyback line (3578d73c) each alone.
- [ ] Dispatched run: the brief allowed per-question commits; whether the dispatching session held the lock cannot be seen
      from here; the fold is the dispatcher's (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched for this company; the one
      `Test Runs/` listing (to check this file's name), the session's commit subjects and the AVA line of the adopted
      2026-10-18 case are declared under contamination. Not used.
- [x] Every v5 id resolves (`Test Runs/_research 2026-10-23 IDA/check_run.py`: every M/L/R id found in the CSV, every quoted
      fragment beside an id found in that row, no E-ids); every filing fact has its accession; the run's own conventions are
      labelled (the comparison filers; the debt credit net of retirements; the tax shelter rule not applied).
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED.
- [x] Owner cash after every real cost (operating cash flow as filed, less stock pay from the statements of equity, less net
      capital spending, less finance-lease principal), never a net-income proxy (operator rule 5); the sovereign from the US
      Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (foundations; Q3; Q4); facts for later questions are under
      AFTER THE STOP.
- [x] Not a point-in-time run (Part VII).
- [x] Only the arithmetic lines of `tools/run.py` were used; its stale share count, its missing stock pay and its gross
      capital spending were corrected from the filings, as stated in Step 0.
- [x] `python tools/check_framework.py` PASS before the final commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The regulated-utility paragraph does not say which debt counts or how its cap is applied.** "The long-term debt raised
over the window to fund the fixed assets" could be gross issuance (refinancing included) or net of retirements, and the
49% cap could be applied to the window's sum or year by year; on IDA the readings give $294.2M, $318.2M or $222.1M a year.
I used net of retirements on the window sum, confessed as this run's CONVENTION, and showed the others; the box did not
depend on it. (2) **The paragraph and specific (e) do not say how they combine.** The paragraph reads as if all capital
spending is charged and the debt then credited; (e) makes the maintenance case central and charges growth spending only
against the growth it buys. Applied one after the other they give no-growth figures of $22.60 a share (all spending,
credited, held flat) or $70.72 (maintenance only). I took (e) as governing and applied the credit to the growth spending,
since plant held level needs no new debt; one sentence in Q7 would stop the next utility run choosing the other way.
(3) **"Whose tax" does not fit flow-through regulation**: its shelter rule assumes carryforwards that run out, while a
cost-of-service utility's low cash tax passes to customers through rates. I did not apply it and gave the sensitivity.
(4) **Forward-sold shares** (about 5.75M shares, $715M) are not addressed by the equity-only basis; the filed count is
central and the settled case is shown beside. (5) **`run.py` misses two utility lines**: partners' reimbursements of jointly
built transmission (an investing inflow, $151.9M in 2025) and stock pay that appears only in the statement of equity.
(6) **Q6's serial-issuance STOP is still unresolved** (Part VI); a utility funding a regulated 50/50 structure issues
shares every year by design, and the run had to weigh it without a rule.
