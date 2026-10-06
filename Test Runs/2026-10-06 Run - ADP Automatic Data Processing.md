# Company Run — Automatic Data Processing, Inc. (NASDAQ: ADP) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the run queue, the prepped reading list, `tools/alerts.json` and every earlier ADP file
were not opened. **Contamination declared:** the analyst's training memory of ADP (payroll leader, client-fund float) is a
prior to be replaced by the filings; the directory listing of `Test Runs/` showed other runs' file names only.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$260.26** (2026-10-05, the quote printed by `python tools/run.py ADP`, which labels it "aggregator, live
  quote only"; flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, $0.10 par: **397,262,737** (10-K for
  FY2026, year to 2026-06-30, filed 2026-08-05, accession `0000008670-26-000030`, cover as of 2026-07-31;
  `python Screens/cover_shares.py ADP`). The balance sheet gives 397.8M outstanding at 2026-06-30 (638.7M issued, 240.9M
  in treasury); preferred authorized, none issued. No second class.
- **Market cap:** 397.263M x $260.26 = **$103,392M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority). ADP reports in USD; its wage-and-tax services run in ten countries but
  the PEO is US only and most revenue is North American (10-K FY2026, Item 1).
- **Filings read** (operator rule 4), all from SEC EDGAR, raw text kept under `_research 2026-10-06 ADP/cache/`
  (gitignored):
  - 10-K FY2026, filed 2026-08-05, `0000008670-26-000030`: Items 1, 1A, 5, 7, 7A, 8 (balance sheet, earnings, equity,
    cash flows, Notes 1, 5, 9).
  - 10-Q for the quarter to 2026-03-31, filed 2026-04-30, `0000008670-26-000022` (the latest 10-Q; superseded for the
    year by the 10-K; no 10-Q for the September 2026 quarter is filed yet).
  - DEF 14A filed 2026-09-24, `0001308179-26-000409` (CD&A, summary compensation, governance, ownership).
  - 8-K of 2026-07-29, Item 2.02, EX-99 earnings release for Q4 and FY2026, `0000008670-26-000025` (read before judging
    the non-GAAP habits, Q4).
  - Earlier 10-Ks for retention and client-fund history: FY2019 `0000008670-19-000021`, FY2022 `0000008670-22-000038`.
  - Competitors' 10-Ks: Paychex FY2026 (May) `0001193125-26-307785`; Paycom 2025 `0001193125-26-059372`; Paylocity
    FY2026 (June) `0001591698-26-000069`.
- **One figure cross-checked against the filed statement:** XBRL operating cash flow FY2026 $5,441.2M against the filed
  Statement of Consolidated Cash Flows, "Net cash flows provided by operating activities | 5,441.2"; they agree. run.py's
  10-year balance-sheet figures for FY2026 (equity $6,031M, goodwill $3,284M, LT debt $4,964M) agree with the filed
  balance sheet.
- `python tools/run.py ADP`, arithmetic lines only (`_research 2026-10-06 ADP/run_py_ADP.txt`). **One repair made by
  hand:** run.py's main owner-earnings lines leave out "Additions to intangibles" (capitalized software and other
  intangibles, $355.0M, $378.3M, $468.5M in FY2024 to FY2026), which it prints only as an alternate. That spending is a
  real and recurring cost of staying in place for a software-delivered service, so this run deducts it.
- **Owner cash after every real cost** = operating cash flow - stock pay - capital expenditures - additions to
  intangibles ($M; FY2024 to FY2026 from the filed cash-flow statement, earlier years from the first-filed XBRL
  vintage; computation `_research 2026-10-06 ADP/q7_arith.py`, output `q7_arith_out.txt`). The depreciation variant
  (OCF - stock pay - D&A) sits beside it. Client funds do not inflate this figure: the change in client funds
  obligations runs through financing and the purchases of client-fund securities through investing; the interest earned
  on them ($1,354.8M in FY2026) and the interest paid on the short borrowings that support them are inside OCF.

| FY (June) | OCF | stock pay | capex | additions to intangibles | D&A | **owner cash** | dep. variant | acquisitions |
|---|---|---|---|---|---|---|---|---|
| 2017 | 2,125.9 | 138.9 | 240.2 | 230.4 | 316.1 | 1,516.4 | 1,670.9 | 87.4 |
| 2018 | 2,515.2 | 175.4 | 206.1 | 264.7 | 377.6 | 1,869.0 | 1,962.2 | 612.4 |
| 2019 | 2,688.3 | 167.3 | 162.0 | 404.5 | 409.0 | 1,954.5 | 2,112.0 | 125.5 |
| 2020 | 3,026.2 | 130.8 | 172.7 | 443.7 | 480.0 | 2,279.0 | 2,415.4 | 0.0 |
| 2021 | 3,093.3 | 175.3 | 178.6 | 327.3 | 510.7 | 2,412.1 | 2,407.3 | 0.0 |
| 2022 | 3,099.5 | 201.7 | 174.4 | 379.0 | 515.1 | 2,344.4 | 2,382.7 | 11.7 |
| 2023 | 4,207.6 | 220.4 | 206.3 | 365.3 | 549.3 | 3,415.6 | 3,437.9 | 32.4 |
| 2024 | 4,157.6 | 243.5 | 208.4 | 355.0 | 561.9 | 3,350.7 | 3,352.2 | 33.6 |
| 2025 | 4,939.7 | 266.1 | 168.7 | 378.3 | 582.4 | 4,126.6 | 4,091.2 | 1,165.1 |
| 2026 | 5,441.2 | 242.6 | 196.6 | 468.5 | 585.9 | 4,533.5 | 4,612.7 | 22.8 |

  Five-year average FY2022 to FY2026: **$3,554.2M** (depreciation variant $3,575.3M; after acquisitions as well,
  $3,301.0M). Growth of the aggregate: 17.9% a year FY2022 to FY2026 (FY2022 is a low base, OCF flat on FY2021) and
  12.9% a year FY2017 to FY2026. Stock pay is in the table every year and is not left out anywhere.
- **The client-fund float (stage zero of the sector method, read because the brief names float companies).** ADP holds
  $43,957.8M of funds held for clients against $44,415.5M of client funds obligations (balance sheet, 2026-06-30), in a
  grantor trust overseen by ADP Trust Company, N.A. under the OCC (10-K, Item 1). It is float as the rows define it, money
  held but not owned **[L1993-009]**, a liability that finances assets **[M2023-004]**. The sector method's CONVENTION
  C9 applies the method to "a part that carries float funding its investments"; here the float funds only a segregated,
  investment-grade bond ladder (Item 7A: corporate bonds BBB minimum, asset-backed AAA), not the owners' investments,
  has no underwriting cost and no reserve to develop, and does not pass through OCF. So the method's two-component
  value is not built; the run counts the float's earnings once, as the interest inside owner cash, and reads its rate
  sensitivity (Q2, Q7) and its short-term funding (Q9). Recorded as a framework gap at the end.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether the buyer would be content if the market closed for five years **[M1997-109]**,
and for a payroll processor whose clients stay about thirteen years (10-K FY2026, Item 1) the question is answerable from
the business, not the quote. The market serves and does not instruct **[M2006-077]**: the price of $260.26 is a fact to
set against value at Q7, not a verdict. Margin of safety: if it needs a pencil it is too close **[M1996-084]**; ADP's
range will be computed, and the foundation warns before it is that a well-known, steadily compounding franchise is the
case most likely to be "fair" rather than screaming. No macro enters, but one macro-shaped input sits inside the
business itself: about a quarter of pre-tax earnings is interest on client funds (FY2026: $1,354.8M of $5,730.3M pre-tax,
EX-99), which moves with rates; it is read as a property of the business, not forecast. Who is paid to tell you: the
earnings release frames FY2026 around AI and "trust" and gives a guidance range met "at the high end" (EX-99); that is
read at Q4 and Q6. **Contrary evidence, written down as found** **[M1997-127]**: (1) the owner-cash growth since FY2022
is flattered by rates: client-fund interest rose from $451.8M (FY2022, 10-K `0000008670-22-000038`) to $1,354.8M, about
$0.7B after tax, roughly a third of the rise in owner cash; (2) U.S. pays per control grew only 1% in FY2026 and is
guided at 0% to 1%, and ES client revenue retention is guided down 10 to 30 basis points for FY2027 (EX-99); (3) smaller
rivals grow faster: Paycom 9%, Paylocity 11% against ADP's 7% (their 10-Ks); (4) ADP funds an average $4.2B of
commercial paper at a three-day maturity and $3.6B of reverse repos to avoid selling client-fund bonds (10-K, Item 7).

## THE STANDING RULE
The run is a purchase of a marketable part-interest for cash. Bought without borrowed money and sized so that a fall of
half or more could be sat through, it puts the buyer at no risk of ruin **[M2012-081]**, **[L2014-024]**; the target's
own short borrowing is the target's exposure, weighed at Q9, not the buyer's conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **What ADP does** (10-K FY2026, Item 1): it runs payroll, payroll tax filing, HR, benefits and time for over 1.1 million
  clients and pays over 42 million workers; in the U.S. it "pay[s] one in six workers" and moved $3.5 trillion in FY2026.
  Two segments: Employer Services ($14,831.4M revenue FY2026) and PEO Services, a co-employer for about 762,000
  worksite employees ($7,128M revenue, of which about $4.6B is zero-margin benefits pass-through) (EX-99).
- **The key variables** **[M1998-044]**: (1) the number of clients and the revenue kept from them (ES client revenue
  retention 89.9% in FY2017, 90.4% FY2018, 90.8% FY2019 from the FY2019 10-K; 92.1% in FY2022 and FY2026; client life
  estimated at about 11 years in FY2019 and 13 years in FY2026); (2) the price per pay and per module (each year's MD&A
  names "an increase in pricing" among the revenue drivers); (3) pays per control, which is employment at existing
  clients (+1% FY2026); (4) client-fund balances and the yield on them ($40.4B average at 3.4%, FY2026). Variables 1 to 3
  are customer behaviour about a compulsory, regulated task: every employer must pay staff and remit taxes correctly
  every period, and the record of the last decade shows retention rising, not falling. Variable 4 is a rate and is not
  foreseeable; but it is a quarter of pre-tax earnings and can be bracketed (Q7), not a reason the economics cannot be
  seen.
- **Do the past statements tell me the future ones?** **[M2008-033]** Yes for the service business: recurring revenue,
  no client above 2% of revenue, ten years of steadily rising revenue ($12,379.8M FY2017 to $21,947.4M FY2026, every year
  up) and owner cash (table, Step 0).
- **Customers or technology?** **[M2017-019]**, **[M2023-030]**. The product is delivered as software and the release leads
  with AI, but the forecast that matters is whether employers keep handing payroll, tax and compliance to a trusted
  processor, which is a judgment about customers and about a compliance network "with direct integration to tens of
  thousands of government entities, tax authorities, and banking institutions" (Item 1). Contrary evidence written down
  **[M1997-127]**: the HCM software field does change (cloud entrants since 2010, AI agents now), and the insiders' own
  filings call competition intense (Paycom 10-K, Item 1A: "new technologies and new market entrants emerge and aggressive
  pricing and client retention strategies persist"). The analyst judges that the change has so far moved the interface,
  not the economics: ADP's retention and margins rose through the cloud transition. Whether AI changes that is a Q2
  question (what could destroy it), not a reason the ten-year economics cannot be pictured; the insiders do write this
  forecast down (each filer guides a year and states multi-year retention), unlike the case of **[M2000-105]**.
- **Does doubt put it outside?** **[M2002-092]**. The doubt the analyst holds is about the size of the client-fund
  interest and the pace of growth, not about what the business is or where it will stand.
- **The bank door.** ADP's balance sheet carries $44B of client funds, so the Q1 test for a financial institution is
  applied: both sides can be read **[M2002-022]**, **[M2011-022]**. The asset side is a disclosed, investment-grade bond
  ladder of at most ten years (Note 5, Item 7A: no sub-prime, CDOs, derivatives or non-investment-grade securities;
  unrealized loss $459.2M on $37.7B at 2026-06-30); the liability side is client money due within days. It is not a
  derivatives book whose condition cannot be seen **[M2005-068]**.
- **VERDICT: IN** **[M2006-013]**. The economics are a compulsory service bought on trust, readable from ten years of
  filings; the rate-driven part is bracketed, not forecast.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now." **[M1995-038]**
- **What keeps it standing, and how permanent** **[M1995-038]**. Four things, each in the filing: (1) **switching cost and
  risk**: the client's payroll, tax filings, benefits and history live in the system; a large implementation takes "six
  to nine months" and multi-country ones "may exceed two years" (10-K, Item 1); a payroll error is a legal and staff
  problem for the client, so the choice is not made on the low bid **[M2017-009]**. (2) **A compliance and money network
  hard to copy**: "direct integration to tens of thousands of government entities, tax authorities, and banking
  institutions", a "final mile" ecosystem the filer calls "hard to replicate", the OCC-chartered ADP Trust Company holding
  U.S. client funds, which "most competitors cannot offer" (Item 1). (3) **Scale and data**: one in six U.S. workers paid,
  $3.5 trillion moved in FY2026. (4) **Trust earned over 77 years**: client life about 13 years in ES (Item 1). None of
  the four depends on the genius of the lord in the castle; the business has passed through several chief executives.
- **The attacker with money** **[M2011-015]**, **[M2012-106]**. Money has attacked: Paycom (founded 1998), Paylocity,
  Workday at the top end, and well-funded private entrants. The evidence of what the attack has done: ADP's ES revenue
  retention rose from 89.9% (FY2017) to 92.1% (FY2022 and FY2026); its ES segment margin was 36.7% in FY2026, up 60
  basis points (10-K, MD&A); revenue rose every year of the ten. An attacker can build a payroll product; the filings do
  not show one taking ADP's clients faster than before. **Contrary evidence** **[M1997-127]**: rivals grow faster (row
  below), new business bookings grew 5.6% against a 6.8% plan in FY2026 (DEF 14A), and one competitor "is frequently
  enough to ruin a business" **[M2012-108]**; no single rival is shown doing so here.
- **Pricing power** **[M2005-020]**, **[M2000-031]**. The MD&A names "an increase in pricing" among the drivers of revenue
  in FY2026 alongside rising retention, so prices rose without share falling; that is the positive form of the test.
  No disclosure of the size of the price rises was found (10-K MD&A; EX-99), so the agony cannot be measured, only that
  rises stick.
- **Would the customer still choose it over the low bid?** **[M2017-009]**. Revenue retention of 92.1%, flat through a
  price rise, and a 13-year client life say yes for the base; the guided FY2027 retention decline of 10 to 30 basis
  points (EX-99) is the one forward sign the other way, small.
- **The low-cost position** **[M2004-091]**. A service everyone must buy, delivered at the largest scale in the field;
  ADP's margin on revenue excluding zero-margin pass-throughs is about 33% (computed: operating result before interest
  and other income $5,779.0M = pre-tax $5,730.3M + interest expense $459.3M - other income $410.6M, over revenue
  $21,947.4M less pass-throughs of about $4,594.8M (PEO revenue $7,115.8M less PEO ex-pass-through $2,521M)). Paychex, a
  smaller-client book, earns more on revenue, so ADP is not shown to be the lowest-cost operator; it is a large-scale one.
- **Ask the competitors** **[M1999-130]**. No competitor names ADP as the rival it would shoot in the filings read;
  Paycom's 10-K describes the field as one of intense competition with "aggressive pricing and client retention
  strategies" (Item 1A). Recorded as not answerable from the public record beyond that.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Widening on the evidence of a decade: retention up 2.2
  points, client life up from about 11 to about 13 years, segment margin up. The forward guides are flat to slightly
  narrower (retention down 10 to 30 bp; pays per control 0 to 1%).
- **What could destroy, modify or reduce it** **[M2000-014]**: (a) software that makes payroll a cheap commodity,
  including AI agents and embedded payroll in other platforms; ADP's own answer is to embed AI and to sell compliance and
  trust, not the screen; (b) a large breach or a failure to move client money, the risk that would hit trust (Item 1A);
  (c) lower interest rates, which modify the earnings (a 25 bp move in short and intermediate rates is about $21.0M of
  pre-tax earnings over the next year, Item 7A) but not the castle.

**The competitor row** (each figure from the filer's own 10-K; operating income over total revenue, revenue growth, and
the retention measure each one reports):

| Company | Fiscal year | Revenue | Operating income / revenue | Revenue growth | Retention as reported | Accession |
|---|---|---|---|---|---|---|
| ADP | FY to 2026-06-30 | $21,947.4M | 26.3% (about 33% ex pass-throughs) | 6.7% | ES client revenue retention 92.1% | `0000008670-26-000030` |
| Paychex | FY to 2026-05-31 | $6,512.0M | 38.6% ($2,510.5M) | 16.9% (Paycor acquired April 2025, "approximately 12%" of it) | payroll client retention 82% to 83% of clients | `0001193125-26-307785` |
| Paycom | CY2025 | $2,051.7M | 27.6% ($567.2M) | 8.9% | revenue retention 91% | `0001193125-26-059372` |
| Paylocity | FY to 2026-06-30 | $1,771.3M | 21.8% ($386.0M) | 11.0% | annual revenue retention "in excess of 92%" for three years | `0001591698-26-000069` |

The row says: ADP keeps its revenue as well as the best of the rivals, earns a margin in the middle of the group on
reported revenue and near the top once the PEO pass-through is removed, and grows more slowly than the younger rivals
(it is ten times Paylocity's size). Nothing in it shows the castle filling in **[M2011-015]**; nothing shows the moat
widening faster than the rivals'.
- **VERDICT: IN** **[M2006-013]**. The castle is standing on the evidence of ten years of rising retention and margin
  against funded attackers, and the reason it stands (switching risk, the compliance and money network, trust) is not
  the kind that a new screen removes quickly. Change is the known threat **[M1999-063]**, and slow change "can lull you
  to sleep easier" **[M2014-038]**; it is written down here, not found operating in the figures.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**. At 2026-06-30 (filed balance sheet): equity
  $6,031.2M, less goodwill $3,284.4M and intangibles $1,653.3M, leaves tangible equity of $1,093.5M; add net claims of
  $734.7M (long-term debt $4,964.1M + reverse repos $139.3M - corporate cash and securities $4,368.7M) and the tangible
  capital the business uses is about $1.8B (the client funds are matched by client obligations and are not owners'
  capital). Against FY2026 net earnings of $4,413.5M the return on tangible capital is far above any reasonable bar; with
  purchased goodwill and intangibles counted, as the capital-allocation view requires **[M2011-060]**, capital is about
  $6.8B and the after-tax return about 65%. Deferred contract costs ($3,244.1M, capitalized commissions and set-up
  costs) are already netted inside operating cash, so they do not hide a capital need.
- **To stand still and to grow** **[M1994-081]**. Capital spending plus additions to intangibles was $665.1M in FY2026
  against D&A of $585.9M, and the ten-year table shows the same order every year: the business grows its revenue about
  6.6% a year (FY2017 to FY2026) while reinvesting little more than its depreciation. Acquisitions are occasional
  ($1,165.1M in FY2025, small otherwise). This is the first of the three grades, "more and more money every year without
  putting up anything to get it, or very little" **[M1998-081]**, the See's account of **[L2007-010]**.
- **The growth arithmetic and its caps** **[M1997-095]**, **[M1999-067]**. Owner cash grew 12.9% a year FY2017 to
  FY2026, but part of that is the client-fund interest tailwind (Foundations, contrary evidence) and part is the PEO's
  growth; revenue grew 6.6%. "Most of the great businesses generate lots of money. They do not generate lots of
  opportunities to earn high returns on incremental capital" **[M2003-120]**: ADP pays out nearly all it earns (Q6), which
  is consistent with that. Q7 carries the shown growth at no more than the discount rate.
- **WEIGHS FOR** **[M1998-081]**, **[L2009-012]**: very high returns on the tangible capital needed, growth bought with
  little added capital. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eight to ten years of them, before the income account** **[M2025-032]** (`tools/run.py`
  prints the ten-year table; read the filed statements behind it). Say what moved and why: equity against goodwill and
  intangibles, cash, receivables and inventory against sales, debt, retained earnings; "what the figures are saying and
  what they don’t say and what they can’t say" **[M2025-032]**. *(line added 2026-10-05: the rule was in Q4 of the
  framework from adoption, and no run had been asked to do it.)*
- **The ten balance sheets, FY2017 to FY2026** (run.py table, first-filed XBRL vintages; FY2026 checked against the filed
  balance sheet). Total assets swing between $37B and $63B because client funds sit on both sides; read without them:
  equity $3,977M to $6,031M, dipping to $3,225M in FY2022 when rising rates put the client-fund bond ladder into an
  unrealized loss (still $459.2M pre-tax at 2026-06-30, Item 7A); retained earnings $14,728M to $26,967M, while treasury
  stock reached $23,165.9M, so the retained earnings have gone back to owners rather than into the balance sheet;
  goodwill $1,741M to $3,284M and intangibles $620M to $1,653M, the step in FY2025 being the $1.2B acquisition (Q6);
  long-term debt $2,002M to $4,964M, the last two steps raised in FY2025 and FY2026 ($1,980.3M and $985.7M issued, cash
  flow statement) while corporate cash and securities ran $4.4B to $7.8B; receivables $1,704M to $3,521M against revenue
  $12,380M to $21,947M, 13.8% to 16.0% of revenue, a slow drift with the PEO's growth, not a jump (FY2025 to FY2026 they
  fell $58.0M while revenue rose 6.7%). Deferred contract costs rose from $2,579.7M (FY2022 10-K) to $3,244.1M (+26%)
  while revenue rose 33%: not building ahead of sales **[M1995-064]**. What the figures say: a business that earns far more
  than it keeps and sends it out; what they cannot say: the market value of the client-fund ladder's earning power once
  rates move, which Q7 brackets **[M2025-032]**.
- **The real costs.** Depreciation and amortization $585.9M is charged; capital spending plus capitalized software is
  deducted in full in owner cash, since "With software, for example, amortization charges are very real expenses"
  **[L2012-003]**. Stock pay ($242.6M) is expensed and left in the adjusted figures (EX-99 reconciliation adds back no
  stock pay and no amortization of acquired intangibles), which is the speakers' definition "after interest, taxes,
  depreciation, amortization and all forms of compensation" **[L2021-003]**, against the practice condemned in
  **[L2015-003]**. EBITDA: the release and the 10-K use "adjusted EBIT", not EBITDA (no instance of "EBITDA" in EX-99 by
  a text search).
- **The recurring "one-time".** EX-99 excludes from adjusted results a $91.1M "business alignment program" (FY2026,
  severance $89.1M), and its footnote (b) shows that the "workforce optimization initiatives from fiscal 2025 and 2024"
  were excluded the same way. Three consecutive years of severance carried outside adjusted earnings is the habit
  **[L2016-007]** warns about, though small (1.6% of adjusted EBIT of $5,874.6M) and disclosed with the candid note that
  "Severance charges have been taken in the past and not included as an adjustment". Owner cash in this run includes the
  cash of every such charge (it is inside OCF).
- **The make-the-numbers habit** **[L2002-041]**. ADP gives annual guidance by segment and the release reports finishing
  "at the high end of our guidance range"; the CFO's language is about the guide. That is the habit, found; it weighs
  against **[M1994-018]**. A second tell that would make it suspicion **[L2002-039]** was looked for and not found:
  reserves are not a feature of the business; adjusted figures are shown beside GAAP, GAAP first in each bullet, with
  adjustments under 2% of EBIT; deferred and prepaid accounts are not building ahead of sales; there is no profit booked
  on both sides of a contract. The adjusted-earnings presentation is a mild form of **[L2016-006]**, not "highlighting" to
  wave away real costs.
- **VERDICT on confusion: IN** (the accounts are clear, the float is disclosed both sides, no suspicion) **[M2003-029]**;
  **WEIGHS slightly AGAINST** on the guidance habit and the three years of excluded severance **[L2002-041]**,
  **[L2016-007]**. Recast earnings for Q7: owner cash as in Step 0, five-year average $3,554.2M.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stake the speakers read rather than meet **[M2007-081]**; the yardsticks are how well they run the
business against the hand dealt, and how they treat the owners **[M1994-008]**.
- **Who.** Maria Black, President and CEO since January 2023, joined ADP in 1996 and ran TotalSource, Small Business
  Solutions and worldwide sales before (DEF 14A `0001308179-26-000409`); her predecessor, CEO 2011 to 2022, sits on the
  board. CFO Peter Hadley. The board chair is independent and non-executive (DEF 14A, governance highlights), so the
  "also Chairman" problem does not arise **[L2014-026]**.
- **Yardstick one, the record against the hand dealt.** The hand is a superb franchise **[M1996-037]**; the record under
  the present and the prior chief executive is the ten-year table: retention up, margins up, revenue up every year, owner
  cash up about threefold. Part of the last four years is rates, which management did not make; the rest is execution.
  The FY2026 bonus plan missed its bookings target (5.6% against 6.8%) and the proxy says so (DEF 14A, CD&A).
- **Yardstick two and the tells** **[M1994-009]**. The proxy: CEO total pay $25,452,877 for FY2026, of which stock awards
  $20,671,694; pay ratio 363:1; ownership guideline six times salary; clawback beyond the listing rule; no poison pill;
  holders may call special meetings and act by written consent. Nothing found that reads as owners treated as marks
  **[L2001-002]**-type conduct; the reports do not dance around the key figures: retention, pays per control, client-fund
  balances and yield are all reported each year, including when retention is guided down **[M1998-036]**. Against: the
  10-K's business section reads in places as the product of a marketing department ("award-winning", "Most Innovative
  Companies", "purpose-built"), which "tells you something" **[M2007-083]**; and the release speaks of guidance met
  "at the high end" (Q4). No instance found in the 10-K or EX-99 of a mistake named in plain words (text search for
  "mistake", "wrong", "regret" in both documents found none, the one hit for "wrong" being "wrongfully acquired" in the
  risk factors) **[L2024-003]**; for a business that has had few, this is a
  weak signal.
- **Love of the business.** A thirty-year insider at the top and a former CEO who started at the company in 1999 are
  evidence of people who chose this business over others; no whole-business sale is in question, so the after-the-cheque
  test does not apply **[M2007-081]**.
- **Integrity on doubt** **[M2013-088]**: no doubt found. No restatement, no adverse audit opinion, no related-party
  dealings of note were found in the 10-K or proxy read.
- **VERDICT on integrity: IN** **[M2015-047]**; **ability WEIGHS FOR** **[M1994-008]**, tempered by the promotional
  register of the reports **[M2007-083]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. FY2022 to FY2026 net earnings were $18,606.1M; dividends
  paid $10,770.9M and repurchases $7,686.3M (cash flow statements, XBRL series in `xbrl_series_out.txt`), together
  $18,457.2M, 99% of earnings. Almost nothing is retained, so the test has little to grade: the company does what
  **[M2004-089]** asks of a business that earns more than it can use, and keeps the moat first **[L2012-011]** through the
  capital spending and software inside owner cash.
- **Buybacks** **[L1999-023]**, **[L2011-003]**. The authorization is a $6 billion sum with no expiration and no stated
  price; the factors named are "acquisition activity, cash balances and cash flows, issuances due to employee benefit plan
  activity, and market conditions" (10-K, Item 5 and MD&A); value is not among them **[L2016-002]**. Prices paid:
  FY2024 about $260.96 (5.1M shares, $1,330.9M, equity statement), FY2025 $289.11, FY2026 $242.92 (10-K MD&A). Read
  against the Q7 range (CONVENTION, framework Q6; range computed at Q7 and recorded back here): **$156 to $246** a share
  on the five-year base. Every year's average price sits above the bottom of the range and FY2025's above its top, so the
  programme is not rescued by its prices and **weighs against** **[M2016-049]**, **[M2014-008]**. Part of the buying
  offsets employee issuance, which the rows rule out as a reason by itself **[M2016-049]**.
- **Issuance and deals.** No all-stock acquisition; the FY2025 purchase ($1,165.1M cash, the largest of the decade, the
  WorkForce Software acquisition of October 2024, named in the FY2026 10-K MD&A; its purchase note was not read in this
  run) was paid in cash and debt. No STOP **[L2009-019]**. The serial-issuer tell does not apply: shares
  outstanding fell from 450.3M diluted (FY2017) to 403.3M (FY2026).
- **Part B, pay** **[M2003-019]**, **[L1994-019]**. The annual bonus pays on revenue growth, new business bookings growth
  and adjusted EBIT growth; the PSUs on adjusted net income growth (67%) and revenue ex pass-throughs growth (33%), with a
  relative TSR modifier of plus or minus 20% against the S&P 500 (DEF 14A, CD&A). The measures are under management's
  reasonable control and none is a raw stock price **[L1996-018]**; but none charges for capital, so growth bought with
  debt-funded acquisitions or with rate-driven client-fund interest pays the same as growth earned **[M1995-010]**, and
  the plan pays on adjusted figures that exclude the severance programmes of Q4. Stock awards, not options; no rule
  found in the rows for restricted stock for another company's managers (framework, absences).
- **The board and the owners.** Independent non-executive chair; a "no overboarding" policy; directors hold five times
  their cash retainer in stock (DEF 14A). Earnings guidance is given each year **[M2022-054]**, **[L2019-006]**, the one
  owner-relations practice the rows turn against by inversion.
- **Part A WEIGHS slightly AGAINST** (payout right, buybacks priced above the bottom of the range) **[L2016-002]**;
  **Part B UNDECIDED** (sensible measures and an independent chair, against no capital charge and the guidance habit)
  **[M2003-019]**, **[M2022-054]**.

## Q7 — WHAT IS IT WORTH? STOP.
"It is the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at "the yield on long-term U.S. bonds" **[L2000-021]**, held as a range **[L2000-024]**; and "are you going to have to put
more cash into after you buy it?" **[M2014-068]** (Q3: very little).
- **The construction (framework CONVENTION, Part VI):** five-year average owner cash after every real cost, carried ten
  years at the growth shown, capped by Q3, then zero nominal growth, discounted at the sovereign, **5.66%**; the ends are
  the no-growth and the shown-growth cases.
- **Base:** **$3,554.2M**, the FY2022 to FY2026 average of OCF less stock pay, capital spending and additions to
  intangibles (Step 0). Claims ahead of the common: long-term debt $4,964.1M + reverse repos $139.3M - corporate cash and
  marketable securities $4,368.7M (Note 5, "Total corporate investments") = **$734.7M**. Client funds and client funds
  obligations are left out on both sides (they net to a $457.7M shortfall at fair value at 2026-06-30, about the size of
  the $459.2M unrealized loss on the ladder, which matures at par); the float's earnings are inside owner cash.
- **Growth shown, and the cap.** Aggregate owner cash grew 12.9% a year FY2017 to FY2026 (17.9% from the low FY2022 base);
  revenue grew 6.6%. The cap the framework names, "when the compound rate becomes higher than the discount rate, you get
  into infinite numbers" **[M1997-095]**, holds the shown-growth case at the discount rate, **5.66%**, which is below both
  the owner-cash rate and the revenue rate; the shown growth is not used above it **[M1999-067]**.
- **COMPUTATION** (`_research 2026-10-06 ADP/q7_arith.py`, output `q7_arith_out.txt`):
  - No-growth end: $3,554.2M / 5.66% = $62,795M; less $734.7M; over 397.263M shares: **$156 a share**.
  - Shown-growth end (5.66% for ten years, then none): **$246 a share**.
  - Width 1.57 to one, inside the three-to-one line: the range is usable, not TOO HARD **[L2000-025]**.
  - Beside it, not the convention: on the FY2026 owner cash alone ($4,533.5M) the same two ends are **$200 and $314**.
- **Value range: $156 to $246 a share against $260.26.** The price is above the top of the convention range and inside
  the FY2026-base variant. At the price the owner cash yields 3.41% on the five-year base and 4.35% on FY2026 (on an
  enterprise value of $104,127M). The expected return at the price, with the convention's shape (growth for ten years,
  then flat), is 5.4% on the five-year base at 5.66% growth and 7.4% on the FY2026 base at 7% growth; none reaches ten.
- **How sure** **[M1999-104]**. The moat makes the service cash sure; the client-fund interest is the unsure quarter.
  COMPUTATION, a bracket only: a fall of the client-fund yield from 3.4% to 2.0% on the $40.4B average balance would take
  about $566M a year off pre-tax earnings, about $436M after the 23% tax rate, some 10% of FY2026 owner cash; the filer's
  own sensitivity is about $21.0M of pre-tax earnings in the next year for each 25 basis points (Item 7A), smaller at
  first because the ladder reprices over up to ten years.
- **The floor (CONVENTION):** about ten percent pre-tax, "we don’t want to buy equities where our real expectancy is
  below 10 percent" **[M2003-149]**, "a very high probability of at least 10% pre-tax returns" **[L2002-020]**, a figure
  the speakers called their guess at opportunity cost **[M2003-151]**, and which very cheap money moved "a little"
  **[M2016-078]**; with the long bond at 5.66% today, money is not cheap.
- **Contrary evidence, written down** **[M1997-127]**: the convention's flat line after year ten is harsh for a franchise
  that has raised its prices and kept its clients for decades. If owner cash from the FY2026 base grew about 6% a year
  for ever, the return at $260.26 would be about 4.35% x 1.06 + 6%, roughly 10.6%, at the floor. That is a perpetual-growth
  reading, which the framework's caps forbid as a value **[M1997-095]**; and even on it the case is at the line, which is
  the case the speakers call "too close" **[M1996-084]**.
- **VERDICT: OUT** **[M2006-013]**. The price sits above the top of a narrow range, and the framework closes that through
  the floor: "there’s just a point at which we drop out of the game" **[M2003-149]**. It does not scream on any variant;
  "If you need to use a computer or a calculator to make the calculation, you shouldn’t buy it" **[M2009-005]**.

**Reporting at the owner's request (COMPUTATION, not a rule change, not a clearance):**
- **VALUE RANGE:** $156 to $246 a share (framework convention); $200 to $314 on the FY2026 base.
- **FAIR PRICE: about $171 a share.** Rule: the price at which the central case returns 10% a year to the holder (the
  floor), in the convention's shape. Central case: FY2026 owner cash $4,533.5M, growing 6% a year for ten years (between
  revenue growth of 6.6% and the FY2027 revenue guide of 5% to 6%), then zero nominal growth, discounted at 10%, less
  $734.7M of claims. Sensitivity: 4% growth gives $148, 8% gives $196; on the five-year base the same rule gives $133.
- **CHEAP PRICE: about $112 a share.** Rule: the price at which FY2026 owner cash clears the 10% floor with no growth,
  so that no growth assumption and no pencil are needed: $4,533.5M / 10%, less $734.7M, over 397.263M shares. On the
  five-year base the same rule gives $88.
- Against the price of $260.26: 1.5 times the fair price, 2.3 times the cheap price.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** Q7 closed the file OUT. (For the record only, not a clearance: on the convention's shape the expected
return at the price, 5.4% to 7.4%, sits about level with the 30-year Treasury at 5.66%, so the bond as first filter
**[M1997-089]** would also bind.)

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Observations written down while reading, for a later run, not weighed here: long-term debt $4,964.1M
against pre-tax earnings of $5,730.3M and interest expense of $459.3M (10-K FY2026), little debt in the sense of
**[R1997-001]**; but the client-funds strategy borrows short to avoid selling the bond ladder, an average $4.2B of
commercial paper at about three days' maturity and $3.6B of reverse repos in FY2026, backed by $11.7B of committed
credit facilities and $7.5B of committed repo capacity (10-K, Item 7). That is the "short-term debt maturities of size"
shape **[L2014-024]**, **[L2010-020]**, and the filer names the risk of a bank failure delaying client funds (Item 1A).
A Q9 reached in a later run must weigh it.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** The draft's default applies: inaction **[M1996-006]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED** (not asked; the operator did not choose it, and the file closed at Q7).

---
## THE BOX
**OUT, decided at Q7** **[M2006-013]**: value range **$156 to $246** a share (convention; $200 to $314 on FY2026 owner
cash alone) against **$260.26**; the price is above the top of a narrow range and the expected return at it is below the
ten percent floor **[M2003-149]**. Fair price about $171, cheap price about $112 (COMPUTATION). Q1 IN, Q2 IN, Q3 WEIGHS
FOR, Q4 IN on confusion and weighs slightly against (guidance habit, three years of excluded severance), Q5 IN on
integrity with ability weighing for, Q6 Part A weighs slightly against (buybacks with no price, paid above the bottom of
the range), Part B undecided. Q8 to Q12 NOT REACHED. Not a TOO HARD, so no research pass is opened.
**What would reverse it:** a price that falls well below the bottom of the range, near the cheap price of about $112,
so that FY2026 owner cash alone clears the floor without a pencil **[M2009-005]**; or owner cash compounding so that the
range's bottom moves above the price, with the castle still standing on the retention and margin evidence of Q2.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Exceptions declared: the first commit came after the tool runs and the first filing fetches (the copy itself was
      made before any fetch, the commit was delayed by the session limit); Q5 and Q6 went in one commit.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before each commit); every filing fact carries its
      accession; numbers are from filings, from the arithmetic scripts in the research folder, or labelled CONVENTION.
- [x] The order was kept; Q7 was the first STOP to fail and closed the run; Q8 to Q12 are NOT REACHED and their notes
      are marked as not clearances.
- [x] Owner cash after every real cost (OCF less stock pay, capital spending and additions to intangibles), never a
      net-income proxy; the sovereign from the US Treasury par curve; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations, Q1, Q2, Q7).
- [x] No row dated after the anchor is cited (this is not a point-in-time run; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings lines were repaired by hand to include
      additions to intangibles.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Float that is not an insurer's.** The brief sends "an insurer or a float company" to the sector
method, and its CONVENTION C9 applies the method to "a part that carries float funding its investments"; ADP's $44B of
client funds is float in the rows' sense **[L1993-009]**, but it funds a segregated bond ladder, not the owners'
investments, has no underwriting cost, and does not pass through operating cash. The method's two components and its
float deductions have no referent here, and neither the method nor the framework says whether a payroll processor (or a
payments, escrow or title business) is inside it. The run read the stage-zero questions, counted the float's interest
once inside owner cash, bracketed its rate sensitivity at Q7 and left its funding for Q9; a one-line scope rule for
non-insurance float would settle it. (2) **Rate-driven earnings in the growth input.** The Q7 convention carries "the
growth shown", but a third of ADP's owner-cash growth since FY2022 came from interest rates on client funds, which no
management made and no row lets the analyst forecast **[M2000-094]**; the cap at the discount rate hid the issue this
time, but a rule is missing for separating rate-driven from earned growth. (3) **`tools/run.py`** puts capitalized
software ("Additions to intangibles", $468.5M in FY2026) only in an alternate line, so its headline owner earnings
overstate a software-delivered business by about a tenth; and EDGAR returned HTTP 429 on the first runs of `run.py` and
`Screens/cover_shares.py`, which crash with a traceback rather than backing off (both succeeded on a retry after a
pause). Reported as tool defects, not fixed.
