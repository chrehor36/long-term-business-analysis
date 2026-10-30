# Company Run — WESCO International, Inc. (NYSE: WCC) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template before any fetch.**

**POSITION NOTE, declared before any verdict:** NOT CHECKED. This is a blind run: `PORTFOLIO.md`, the holding reviews,
the session-state files, the run queue and the prepped reading list were not opened, and no attempt was made to learn
whether the operator holds or wants this name.

**CONTAMINATION, declared:** (1) the session's opening context listed recent commit subjects for five other runs of today
(IESC, FIX, MYRG, PRIM, MTZ, all contractors, all "OUT at Q2") and the file names of today's other runs; none of those
files was opened, and none is about WCC or a distributor. (2) `tools/run.py WCC` was run; only its arithmetic lines were
read (Part VII). (3) The memory index loaded with the session names counts of earlier gate-clearers; it names no ticker
relevant here. No WCC file in `Test Runs/` existed before this one (directory listing checked by name only).

Working folder: `Test Runs/_research 2026-10-05 WCC/` (filings as fetched, text conversions, `calc.py`, `rows.txt`, the
peer facts in `peers/`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $382.19 (2026-10-05, live quote through `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: common stock 48,732,854 (10-Q for the period ended 2026-06-30,
  filed 2026-07-30, accession `0000929008-26-000024`; `python Screens/cover_shares.py WCC`). The 4,339,431 Class B
  nonvoting shares are issued with none outstanding (10-K balance sheet); the Series A preferred was redeemed in June 2025
  (10-K FY2025, `0000929008-26-000008`). One class counts.
- **Market cap:** 48.733M x $382.19 = **$18,625M**. Debt at 2026-06-30 $5,985.9M gross, cash $808.9M (10-Q), so the
  enterprise is about $23.8B.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 filed 2026-02-13, `0000929008-26-000008` (Items 1, 1A, 5, 7, 7A, the
  statements, notes 2, 6, 9; segment tables); 10-Q Q2 2026 filed 2026-07-30, `0000929008-26-000024` (statements,
  MD&A, liquidity); DEF 14A filed 2026-04-17, `0001193125-26-159688` (ownership, CEO pay table, incentive metrics);
  8-Ks `0001193125-26-396005` (2026-09-21, ABL to 2031, receivables facility to 2029 and raised to $1,750M),
  `0001193125-26-068181` and `0001193125-26-083054` (Feb 2026, $650M 5.250% notes 2031 and $850M 5.500% notes 2034 to
  retire the 7.250% 2028 notes), `0000929008-25-000027` (Sept 2025, EES division head's severance), `0000929008-26-000021`
  (Q2 2026 results, cover only); 10-K FY2020 `0000929008-21-000006` (Anixter merger note), 10-Ks FY2019, FY2022, FY2023
  (`0000929008-20-000013`, `0000929008-23-000006`, `0000929008-24-000005`) searched for the merger and synergy record.
- **One figure cross-checked against the filed statement:** net cash from operating activities FY2025 **$125.0M** in the
  filed cash-flow statement (10-K p. 50) equals the XBRL figure `tools/run.py` printed; capex $99.8M and stock pay $40.5M
  also agree.
- `python tools/run.py WCC`, arithmetic lines only: OCF 2023/2024/2025 = 493 / 1,101 / 125; SBC 48 / 29 / 40; D&A
  181 / 183 / 198; capex 92 / 95 / 100. Its "OE lo / OE hi" labels were not used; owner cash is recomputed below from the
  filed lines as OCF less stock pay less all capex. Its share count (48.7M, cover 2026-07-29) matches the cover.
  Its stock-pay and OCF lines were checked against the filed statement and are correct for this filer.

**The record, 2008 to 2025** (XBRL first-filed vintage, transcription; FY2025, FY2024, FY2023 and the 2020 merger year
read in the filed statements; $M; `calc.py`):

| year | sales | gross margin | SG&A / sales | op. margin | op. income / tangible assets | sales / (AR + inventory − AP) | owner cash (OCF − SBC − capex) |
|---|---|---|---|---|---|---|---|
| 2008 | 6,111 | 19.7% | 13.7% | 5.7% | n/a | n/a | 231.7 |
| 2009 | 4,624 | 19.5% | 15.0% | 3.9% | 11.6% | 6.7x | 265.4 |
| 2010 | 5,064 | 19.7% | 15.1% | 4.2% | 12.5% | 6.0x | 96.4 |
| 2011 | 6,126 | 20.2% | 14.2% | 5.4% | 17.4% | 6.6x | 118.8 |
| 2012 | 6,579 | 20.2% | 14.6% | 5.1% | 14.1% | 5.9x | 250.0 |
| 2013 | 7,513 | 20.6% | 13.3% | 6.4% | 19.7% | 6.8x | 271.4 |
| 2014 | 7,890 | 20.4% | 13.6% | 5.9% | 18.0% | 6.7x | 215.9 |
| 2015 | 7,518 | 19.9% | 14.0% | 5.0% | 14.9% | 6.4x | 248.4 |
| 2016 | 7,336 | 19.7% | 14.3% | 4.5% | 14.0% | 6.3x | 269.7 |
| 2017 | 7,679 | 19.3% | 14.3% | 4.2% | 12.4% | 5.8x | 112.8 |
| 2018 | 8,177 | 19.2% | 14.1% | 4.3% | 13.7% | 6.2x | 244.1 |
| 2019 | 8,359 | 18.9% | 14.0% | 4.1% | 11.7% | 6.1x | 161.2 |
| 2020 | 12,326 | 18.9% | 15.1% | 2.8% | 5.2% | 4.2x | 467.9 |
| 2021 | 18,218 | 20.8% | 15.3% | 4.4% | 10.7% | 5.2x | −18.4 |
| 2022 | 21,420 | 21.8% | 14.2% | 6.7% | 14.9% | 4.8x | −134.8 |
| 2023 | 22,385 | 21.6% | 14.5% | 6.3% | 14.1% | 4.7x | 352.8 |
| 2024 | 21,819 | 21.6% | 15.2% | 5.6% | 12.3% | 5.1x | 977.6 |
| 2025 | 23,511 | 21.1% | 15.1% | 5.2% | 10.8% | 4.7x | −15.3 |

Owner cash five-year averages: 2009-13 **$200.4M**; 2016-20 **$251.1M**; 2021-25 **$232.4M**. Diluted shares 42.7M
(2009), 43.5M (2019), 49.5M (2025). Owner cash per average diluted share was about $4.1 in 2009-13 and about $4.5 in 2021-25. First half
2026: sales $12,745M (+13.4%), operating income $675.7M (5.3%), OCF $275.1M (10-Q).

## THE FOUNDATIONS (not a gate)
A share is a business, so the question is what the distribution business will throw off, not where the quote goes. The
market serves and does not instruct: the price of $382 is information about others' expectations only **[M2006-077]**.
No macro view enters **[M2000-094]**; the filing's own story of "secular trends of digitalization, including AI-driven
data centers" is a forecast offered by the seller, and is read as such. The analyst's habits: look for "what’s wrong in things"
**[M2025-013]**, and aim the reading "to possibly reject your original hypothesis" **[M1998-144]**; the steelman of the
moat is stated in Q2 before it is answered **[M2016-055]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) in its own Item 1 the company calls its field "highly fragmented" with "significant competition";
(2) supplier agreements "are terminable by either party on 60 days’ notice or less"; (3) "Some of our existing
competitors have, and new market entrants may have, greater resources than us"; (4) UBS gross margin fell in 2025
"primarily due to competitive pressures in the public power market"; (5) owner cash in 2021-25 averaged no more than in
2016-20, after a $4.7B merger; (6) adjusted EBITDA adds back stock pay, "digital transformation costs" in every year
shown, and cloud-software amortization; (7) a $60.3M inventory overstatement from cost-absorption accounting was found
in Q4 2020 and booked out of period; (8) Graybar, an employee-owned rival with no acquisition debt, runs a lower cost
ratio and earned more on its tangible assets than WCC in each of 2022 to 2025. Written in the order found.

## THE STANDING RULE
A purchase for cash, unlevered and sized within the buyer's means, puts the buyer at no risk of ruin from this name;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**, and the buyer is "never going to risk what we
have and need for what we don’t have and don’t need" **[M2012-081]**. The target's own debt is weighed at Q9 (not
reached).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" and "how the industry will develop and where the company will stand within the industry"
  **[M2012-065]**; the chemistry of the product need not be known, only "the economic dynamics of the industry. Is there
  — are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **The key variables** **[M1998-044]**: (a) gross margin, the spread between supplier cost and selling price, 18.9% to
  21.8% in every year 2008-2025; (b) the cost of serving, SG&A 13.3% to 15.3% of sales; (c) working-capital turns,
  sales over receivables plus inventory less payables, 5.8x to 6.8x before the merger and 4.7x to 5.2x after;
  (d) volume, which follows construction, industrial, utility and data-center spending, and fell 24% in 2009. Each is
  read off eighteen years of filed statements, and the past statements do tell what the future ones will look like in
  form **[M2008-033]**: a wholesaler of wire, conduit, switchgear, cable, lighting and security products, buying from
  35,000 suppliers (top ten 32% of purchases) and selling to about 130,000 customers (top ten 15%, none over 5%), FY2025
  10-K Item 1.
- **Routing.** The products change slowly and the distributor carries no technology risk of its own; the CSS
  data-center line is technology demand, not technology the company must invent. Insiders of this trade would write a
  ten-year forecast of a distributor's spread and cost ratio down; it is not the case of **[M2000-105]**. Not a
  financial institution, not a holding company.
- **Doubt recorded.** Two pieces are less foreseeable: the size of the data-center wave in CSS (a single segment grew
  18.3% in 2025 on "several large project sales") and whether manufacturers or e-commerce sellers go around the
  distributor (Item 1A names "a supplier’s change in sales strategy to reduce its reliance on distribution channels" and
  "e-commerce companies"). Both are questions about the castle, which is where the routing sends them (Q2), not about
  whether the economics of distribution can be pictured. The doubt rule **[M2002-092]** is applied to the circle, and
  electrical distribution is inside it: a wholesaler's earnings are spread less cost times volume, turned by working
  capital.
- **VERDICT: IN.** The economics are of a kind that can be pictured ten years out **[M2000-037]**, **[M1995-051]**; the
  open questions are castle questions and pass to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**.

**The steelman, stated first** **[M2016-055]**. The case for a moat is scale and density in a fragmented trade: the
largest electrical, datacom and utility distributor in North America by the filer's account, with 700 sites, 63 large
distribution centers, preferred-supplier agreements with 450 suppliers covering about 68% of purchases, supplier volume
rebates worth 1.4% of sales in 2025 (1.3% in 2024, 1.4% in 2023; note 2), and services (kitting, job-site trailers,
vendor-managed inventory) that bind large accounts. The record supports part of it: legacy WCC earned 3.9% operating
margin in the 2009 trough when Graybar earned 1.7%, and 4% to 6% through 2010-2019 when Graybar earned 1.7% to 3.0%; it
never lost money in any year 2008-2025.

**The castle tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**, **[M1997-103]**. The filer answers it: "Some of our existing
   competitors have, and new market entrants may have, greater resources than us", and "Other sources of competition
   are buying groups formed by smaller distributors to increase purchasing power and provide some cooperative marketing
   capability, as well as e-commerce companies" (10-K Item 1A). The buying groups are the answer to the purchasing-scale
   moat: small rivals pool their buying to get what scale gets. The attacker need not be built; Sonepar, Rexel, Graybar
   and CED are in the field already. This is the industry "never going to have barriers to entry" of **[M2012-106]**
   unless the low-cost exception below applies.
2. **Pricing power, and the agony before a rise** **[M2005-020]**. "Existing or future competitors may seek to gain or
   retain market share by reducing prices, and we may be required to lower our prices or may lose business ... We may be
   subject to supplier price increases while not being able to increase prices to customers" (Item 1A). Gross margin
   never left a 2.9-point band in eighteen years, through the 2021-2022 shortage inflation and the 2025 tariffs; the
   price is passed through, not set. In 2025 the UBS margin fell "primarily due to competitive pressures in the public
   power market" (MD&A). The case the rows describe, where a rival's price is one's own, is **[M2012-109]** and **[M2023-079]**.
3. **The customer and the low bid** **[M2017-009]**. "Customers look to product line breadth, product availability,
   service capabilities, geographic proximity and price" (Item 1); project awards "often involve complex and lengthy
   negotiations and competitive bidding processes" (Item 1A). The branded product (an Eaton breaker, a Panduit
   connector) carries the name the customer asks for; the distributor of it does not. This is "most insureds don't care
   from whom they buy" in another trade **[L2004-003]**.
4. **Suppliers.** "Most of our agreements with suppliers are terminable by either party on 60 days’ notice or less for
   any reason" (Item 1A). The preferred-supplier position that the steelman leans on can be withdrawn in two months.
5. **The commodity field and its one exception: the low-cost operator** **[L2004-007]**, **[L2000-017]**,
   **[M1997-010]**. In a commodity-like trade the castle stands only for the low-cost operator, and the cost is measured
   against the competitor **[M2001-013]**, **[M2009-059]**. The competitor row (below) shows WCC is not that operator:
   Graybar runs SG&A at 13.7% to 14.5% of sales in 2022-2025 against WCC's 14.2% to 15.2%, sells at a lower gross margin
   (19.3% to 20.4% against 21.1% to 21.8%, that is, it charges the customer less), and earned more on its tangible assets
   in each of those four years (18.3%, 17.9%, 15.3%, 13.2% against 14.9%, 14.1%, 12.3%, 10.8%). Rexel, the third large
   listed electrical distributor, reports an adjusted EBITA margin of 6.0% (non-SEC, below), level with WCC's adjusted
   figures. WCC earns its operating margin by a higher gross margin on a richer mix (the Anixter datacom and security
   lines), not by lower cost.
6. **Unit volume, scale and widening or narrowing** **[M1999-108]**, **[L2005-010]**. Sales rose 3.8 times from 2008 to
   2025 (5.1 times from the 2009 trough), most of it bought (EECOL 2012, $1.29B of acquisition cash that year; Anixter
   2020, $4.70B of purchase consideration). If scale were the moat, the return on tangible assets should have risen
   with it. It did not: 11.6% in 2009, 11.7% in 2019, 10.8% in 2025; operating margin 5.7% in 2008 and 5.2% in 2025, the
   2022 peak of 6.7% given back in three years of record sales. Owner cash per share moved little, about $4.1 in 2009-13 and about $4.5 in 2021-25. The
   improvement one day goes to the competitor the next **[M2004-053]**.
7. **What could destroy or reduce it, five to fifteen years out** **[M2016-065]**, **[M2000-016]**: a manufacturer selling
   direct, an e-commerce seller of electrical supplies, a buying group of independents, or a larger private rival
   pricing for share. The filer names all four in Item 1A. "one competitor is frequently enough to ruin a business"
   **[M2012-108]**; here there are several with the resources to try.

**The competitor row** (same metrics from each company's own filings; operating income over total assets less goodwill
and intangibles; XBRL first-filed vintage, transcription):

| company (filing) | 2009 op. margin | 2019 op. margin | 2025 op. margin | 2025 SG&A / sales | 2025 gross margin | ROTA 2019 | ROTA 2025 |
|---|---|---|---|---|---|---|---|
| WESCO (10-K `0000929008-26-000008`; 2019 `0000929008-20-000013`) | 3.9% | 4.1% | 5.2% | 15.1% | 21.1% | 11.7% | 10.8% |
| Graybar Electric, employee-owned (10-K `0000205402-26-000015`; 2019 `0000205402-21-000006`) | 1.7% | 3.0% | 4.5% | 14.2% | 19.3% | 9.0% | 13.2% |
| Anixter, pre-merger (10-K `0000052795-20-000037`, FY ended Jan 2020; FY2009 in `0000950123-11-019602`) | 2.1% | 4.2% | merged | n/a | 20.1% (FY2019) | 10.2% (FY2019) | merged |
| Rexel SA (FY2025 results release, Paris, 2026-02-11, rexel.com; **IFRS, non-SEC, flagged**) | n/a | n/a | adj. EBITA 6.0% on €19,415M | n/a | not extracted | n/a | n/a |
| W.W. Grainger, MRO (10-K `0000277135-26-000011`) | 10.7% | 11.0% | 13.9% | 25.2% | 39.1% | 23.9% | 29.9% |
| Fastenal, MRO (10-K `0000815556-26-000009`) | 15.3% | 19.8% | 20.2% | 24.8% | 45.0% | 27.8% | 32.8% |

What the row says. Among the electrical distributors the spread is narrow: everyone earns a 19% to 21% gross margin and
a 4% to 6% operating margin, and the best of the decade on tangible assets is the employee-owned one with the lowest cost
ratio. Grainger and Fastenal show what a distributor castle looks like in the figures (a gross margin near 40% to 45%
held for two decades, returns on tangible assets near 30%); WCC's figures are the electrical trade's, not theirs. The
2009 trough, the one point where legacy WCC clearly beat its electrical peers, is a margin of 3.9% against 1.7% and
2.1%, a better operator in a poor trade, which the rows do not call a moat unless it is the low-cost position, and the
2022-2025 figures show it is not. Rexel's release also records a €124M fine imposed by the French Competition
Authority (paid April 2025), a reminder that the trade's margins are policed by price competition and its regulators,
not by any one firm's castle.

**Why it closes.** The filer's own account is the commodity mark set: fragmented field, competition on breadth,
availability, service and price, rivals cutting price, suppliers free to leave in sixty days, buying groups neutralising
scale purchasing, and a segment margin lost to "competitive pressures". The one exception the rows allow in such a field,
the low-cost operator **[L2004-007]**, **[M1997-010]**, is not shown: a rival runs lower costs and charges less. And the
scale test of eighteen years shows no widening: returns on tangible assets flat at about 11% from 2009 to 2025 while
sales grew nearly fourfold **[M1999-108]**. This is a castle shown open on the evidence, not a castle whose future cannot
be judged: the question was answerable from the filings, and the filings answer it against the business. "If we can
think of very much that can go wrong with them, we just forget it" **[M2000-016]**; and price does not reopen it,
"What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

The steelman is not dismissed: legacy WCC was the better operator against Graybar and Anixter for a decade. But being
better than the average operator in a trade that prices off the average is the case of **[M2013-052]**, and the rows ask the
analyst to find why the castle stands against attack, which the filer itself says it does not claim to know beyond
breadth, availability, service and price.

- **VERDICT: OUT.** The castle is shown open: the high-cost-relative, price-competed distributor in a commodity-like
  field **[L1994-035]**, **[M2001-013]**, with no low-cost position against its own competitors **[L2004-007]**, and a
  return on tangible capital that scale did not widen **[M1999-108]**; a castle shown open is OUT **[M2011-015]**,
  **[M2006-013]**.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN. WEIGHING. **NOT REACHED** (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. **NOT REACHED.**
## Q5 — WHO RUNS IT. **NOT REACHED.**
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. **NOT REACHED.**
## Q7 — WHAT IS IT WORTH. **NOT REACHED.**
## Q8 — IS IT BETTER THAN THE ALTERNATIVES. **NOT REACHED.**
## Q9 — COULD IT RUIN US. **NOT REACHED.**
## Q10 — IS IT THE FAT PITCH. **NOT REACHED.**
## Q12 (optional). **NOT REACHED** (not asked by the operator; nothing in the filings touches the named businesses).

---
## COMPUTATION — NOT A CLEARANCE
*Everything below was computed or read after the closing STOP at Q2, at the owner's request for the value range, the
fair-price band and the cheap price, and for the balance-sheet reading. It answers no question, carries no entry
language, and does not reopen Q2 (operator rule 3).*

### The balance sheets, 2016 to 2025, read before the income account (the reading Q4 asks for **[M2025-032]**)
From the `tools/run.py` ten-year table and the filed FY2025, FY2024 and FY2020 statements ($M):
- **Size and what it is made of.** Total assets $4,491 (2016) → $5,018 (2019) → $11,880 (2020) → $16,495 (2025). The
  2020 step is Anixter. Goodwill $1,721 → $3,343 and intangibles $393 → $1,769; together $5,113, about 102% of
  common equity of $5,032 at end-2025. Tangible common equity is therefore about **zero to slightly negative**
  (about −$80M at end-2025; lower still in 2020-2024, when the $573M preferred sat inside total equity).
- **Working capital is the business.** Receivables $1,034 → $4,070 and inventory $821 → $4,009, against payables
  $685 → $3,031. Net trade working capital (AR + inventory − AP) $1,171 (2016) → $5,048 (2025); sales over that figure
  fell from about 6.3x before the merger to 4.7x in 2025: each dollar of sales now ties up about a third more working
  capital than it did. In H1 2026 receivables rose a further $615M and inventory $409M; supplier prepayments and
  customer deposits both rose (10-Q).
- **Receivables are pledged.** The securitization ($1,300M drawn of $1,550M at end-2025; $1,275M at 2026-06-30) sells an
  undivided interest in "all domestic accounts receivable" to a special-purpose entity; it stays on the balance sheet as
  secured borrowing (note 9). The ABL revolver is secured by "substantially all assets" of the borrowers. Most of the
  current assets stand behind lenders before owners.
- **Debt.** Long-term debt $1,363 (2016) → $4,370 (2020) → $5,756 (2025) → $5,911 (2026-06-30). The preferred
  ($573M, 10.625%) was retired in 2025 with $800M of 6.375% notes due 2033: a claim moved from equity to debt.
  The 2028 notes ($1,325M) were refinanced in 2026 into 2031 and 2034 notes; the ABL now runs to 2031 and the
  receivables facility to 2029 (8-K 2026-09-21). Pre-tax earnings over interest, 2025: ($855.9 + $386.7) / $386.7 =
  **3.2 times**; the company's own leverage ratio is 3.0x net debt to adjusted EBITDA at 2026-06-30.
- **Retained earnings** $1,957 (2016) → $5,513 (2025): $3.6B kept over nine years; owner equity per share rose, but
  equity is now almost wholly goodwill.
- **What the figures do not say.** Unrecognized tax benefits of $164.7M with no timing; purchased transferable tax
  credits used against 2024 and 2025 tax, with recapture risk named in Item 1A; operating leases of $1,101M of future
  payments off the debt line.

### The income account, recast (what Q4 would have weighed)
- **Adjusted EBITDA in the filer's own mouth.** Segment profit is measured by adjusted EBITDA, and management uses
  non-GAAP measures "in the determination of incentive compensation" (MD&A). The adjustment adds back stock pay ($40.5M
  in 2025; $57.1M TTM June 2026), "digital transformation costs" ($24.9M 2024, $35.2M 2025, $62.1M TTM), and the
  amortization of capitalized cloud-software implementation ($14.1M, $30.2M, $41.8M TTM). The rows: EBITDA is "utter
  nonsense" **[M1998-086]**, stock pay is "the most egregious example" of real costs owners are told to ignore
  **[L2015-003]**, and featured adjusted figures make the speakers "nervous" **[L2016-006]**. In mitigation, the 2025
  bonus used EBITDA less stock pay and cloud amortization, and the free-cash-flow half of the bonus paid **zero** because
  the target was missed (DEF 14A); the plan bit.
- **A second tell, recorded.** Q4 2020: "inventories were overstated by $60.3 million because of a misstatement in
  inventory cost absorption accounting, which occurred over multiple periods" (10-K FY2020 note 2), booked as an
  out-of-period adjustment and judged immaterial. With the recurring add-backs this is two items from the list of tells;
  had Q4 been reached, whether they rise to suspicion would have had to be argued, not assumed.
- **Earnings after every real cost** **[L2021-003]**: net income to common 2021-2025 = $408.0, $803.1, $708.1, $660.2,
  $612.9 (2025 less the $32.9M preferred-redemption gain); average **$638.5M**. Capital spending ran below depreciation
  and amortization ($88.2M against $187.9M, five-year averages); much of D&A is amortization of purchased intangibles.
- **Delivered owner cash** (OCF − stock pay − all capex): five-year average **$232.4M**; less preferred dividends paid
  ($51.4M a year) **$181.0M**; the depreciation variant (D&A in place of capex) **$132.7M**. The gap between $638.5M of
  earnings and $232.4M of cash is working capital: receivables and inventory absorbed the profits of growth. This is
  the "gruesome" leg of **[L2007-010]** only in part (the added capital earns about 24% to 32% pre-tax on net working
  capital), but it means reported earnings have not reached the owner as cash: over 2021-2025 owner cash totalled
  $1,162M against $3,193M of earnings to common.

### The value range (CONVENTION construction, Part VI), the fair-price band and the cheap price
Rate 5.63% (sovereign). No real growth after year ten computed as zero nominal growth (Part VI specifics).

| input basis | annual cash | value, no growth | per share |
|---|---|---|---|
| Delivered owner cash, 5-yr avg, OCF − SBC − all capex | $232.4M | $4,128M | **$85** |
| same, less preferred dividends paid | $181.0M | $3,215M | $66 |
| depreciation variant (D&A for capex) | $132.7M | $2,357M | $48 |
| Recast earnings if growth and working-capital absorption stopped (NI to common + D&A − capex) | $738.0M | $13,108M | **$269** |
| TTM to 2026-06-30 on the same recast basis | about $804M | $14,281M | $293 |

**Shown growth.** Measured on aggregate owner cash, as the convention requires: 2016-20 average $251.1M, 2021-25 average
$232.4M. **No growth shown** over the decade, so the shown-growth end equals the no-growth end on delivered cash. On the
recast-earnings basis, growth costs working capital at about 21.5% of each added dollar of sales (end-2025 ratio): if
sales grew 5% a year for ten years with that working capital paid for, the value would be about $19.0B, **$390 a share**;
at 3% a year, $347; at 8%, $468. The price of $382 therefore assumes about 5% a year of growth for a decade on earnings
that have not yet been delivered as cash, or (by the `run.py` arithmetic line) about 13.8% a year on the delivered cash.

- **Value range: $85 to $269 a share** against **$382.19**. Top over bottom is 3.2 to 1, wider than the convention's
  three to one, so Q7, had it been reached, would have closed TOO HARD on width **[L2000-025]**; and the price sits
  above the top of the range, so it would have closed OUT through the floor convention in any case **[M2003-149]**.
- **Expected pre-tax return at $382** (after-tax cash grossed up at 25%, approximate): 1.7% on delivered owner cash,
  about 5.3% on recast earnings, 5.8% on TTM recast earnings; the first two below the sovereign of 5.63% and the third barely above it, and all below
  the floor of about ten percent pre-tax (CONVENTION, Part VI).
- **Fair-price band: $85 to about $195 a share.** Inside the range, the floor of about ten percent pre-tax is met on the
  recast-earnings basis only at or below about $195 (pre-tax recast earnings about $951M / 10% / 48.73M shares). On the
  delivered-cash basis no price inside the range meets the floor; it needs about **$64** or less.
- **Cheap price: about $64 a share** (CONVENTION, ours: the price at which even the delivered owner cash, with no growth
  credited and the preferred gone, yields the ten percent pre-tax floor; at that price the recast-earnings basis yields
  about 30%, a case that would "scream" without a pencil **[M2009-005]**, **[M1996-084]**). The price is six times it.
- All three figures are COMPUTATION, the file having closed at Q2; they describe price against a business the run
  found to have no castle, and a lower price does not reopen Q2 **[M2019-015]**.

### Facts gathered for the unreached questions (recorded, not weighed)
- **Anixter merger, 2020** (10-K FY2020 note 6): consideration $4,698M: cash $2,563M, WCC common $314M (0.2397 share per
  Anixter share), Series A preferred $574M at 10.625%, and $1,248M of Anixter debt extinguished; financed with $1.5B of
  7.125% 2025 notes and $1.325B of 7.250% 2028 notes. Not an all-stock deal, so the one Q6 STOP **[L2009-019]** does not
  apply. Synergies: the 10-Ks of 2020 to 2023 speak of "the realization of integration synergies" without a figure; no
  claimed-against-achieved post mortem was found in the 10-Ks read. Merger and integration costs were added back each
  year from 2020 to 2023 (2022: $67.4M).
- **Buybacks.** $75.0M in 2023 (504,335 shares, about $149), $425.0M in 2024 (2,424,488 shares, about
  $175), $75.0M in 2025 (419,570 shares, about $179), $39.9M in H1 2026. A $1B authorization of 2022 with no expiration
  date and no stated price, the announcement the rows find "almost never refer to a price" **[L2016-002]**. Every price paid is above the bottom of the range ($85), so the CONVENTION
  test of Q6 (prices paid at or below the bottom of the Q7 range) would have weighed against.
- **The people.** John J. Engel, chief executive since 2009 and chairman since 2011; 753,914 shares beneficially owned
  (1.5%, including 296,637 under exercisable SARs and options); total 2025 pay $12.3M ($11.5M 2024, $10.3M 2023). New
  CFO (Indraneel Dev signs the July 2026 8-K); the EES division head left in September 2025 with severance.
- **Debt and exposures.** Gross debt $5,986M at 2026-06-30, about 66% to 68% fixed; maturities now 2029 (receivables
  facility), 2029 (6.375% notes), 2031 (ABL and 5.250% notes), 2032, 2033, 2034. Debt that must be met by payment if
  credit closes is the case of **[L2010-020]**; the R1997-001 "little or no debt" criterion **[R1997-001]** is not met by a
  business with net debt about three times its adjusted EBITDA.

---
## THE BOX
**OUT, at Q2.** The castle is shown open on the filings: a commodity-like distribution trade in the filer's own words
(fragmented, priced on breadth, availability, service and price, suppliers free to leave in sixty days, rivals with more
resources, buying groups, a 2025 segment margin lost to "competitive pressures"), without the low-cost position the rows
require in such a trade (Graybar runs a lower cost ratio, charges less and earned more on tangible assets in 2022-2025),
and with eighteen years in which a near-fourfold rise in sales left the return on tangible assets at about 11% and owner
cash per share little changed from 2009-13 (about $4.1 to about $4.5). Not TOO HARD: the deciding question was knowable and answered. COMPUTATION
(not a clearance): range **$85 to $269** a share against **$382.19**; fair-price band **$85 to about $195**; cheap price
**about $64**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. (No commit: the task instruction forbids
      committing; the write-early commits were therefore not made, declared.)
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      checked to be in that row); every filing fact has its accession; no number without a row or a filing, except the
      CONVENTION figures labelled as such.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is headed COMPUTATION — NOT
      A CLEARANCE and carries no entry language.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): the cash basis is OCF less stock pay
      less all capex; the recast-earnings basis is shown beside it, labelled, as the top of a range, never as owner cash.
      Sovereign from the US Treasury; the price is an aggregator quote, flagged; Rexel's figures are a non-SEC release,
      flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, eight items).
- [x] No row dated after the anchor is cited (not a point-in-time run; anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its stock-pay, OCF and share lines were checked
      against the filing and were right for this filer.
- [x] `python tools/check_framework.py` PASS (run after writing; see the reply).
- Shortfalls, declared: Sonepar and CED, the two largest private rivals, file nothing, so the low-cost comparison rests
  on Graybar, Anixter's history and Rexel's release; Rexel's gross margin and North American margin were not extracted
  from its PDF; the Anixter synergy figures claimed at announcement were not found in the 10-Ks read (they were in
  investor decks, not opened); pre-2016 balance sheets and 2008 figures are XBRL transcription, not read in the filed
  statements.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Q7's convention breaks on a distributor's working capital.** The range is built from five-year owner
cash after "all capital spending", and its growth is measured on that aggregate; for a wholesaler, growth is bought
mostly with receivables and inventory, so delivered owner cash is depressed in growth years and its "shown growth" can
be nil while earnings rise, which makes the no-growth and shown-growth ends the same number ($85) and leaves the
convention silent on the obvious second basis (the cash the business would yield if growth, and the working-capital
build with it, stopped). I showed both and called the spread between the two bases the range; the convention should say
whether working-capital absorption is capital spending for its purposes, and how the no-growth case treats it.
(2) **The pre-tax floor against after-tax cash.** The floor is "about ten percent pre-tax on the price paid", but every
cash input the convention names is after tax; I grossed up at an assumed 25% rate, which is ours and approximate; the
convention should state the gross-up. (3) **Q2's low-cost exception has no stated comparison set.** The rows measure cost against competitors (**[M2001-013]**), which leaves open which competitor when the two largest rivals are private and file nothing; I used
the one filing rival of the same trade (Graybar) plus Anixter's history and Rexel's release, and named the gap. A rule
that the comparison is to every filing rival of the same trade, with the non-filers named as unread, would make two
analysts read the same evidence.
