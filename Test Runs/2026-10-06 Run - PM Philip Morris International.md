# Company Run — Philip Morris International Inc. (NYSE: PM) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the register, the reading list, the session-state files and `tools/alerts.json` were not opened, so whether the
operator holds PM is unknown to the analyst.

**CONTAMINATION DECLARED.** (1) No earlier run file or research folder for PM was opened; a directory listing of `Test Runs/`
for 2026-10-0x names showed no PM file. (2) One other company's v5 run (PBH, 2026-10-05) was read for FORM only, its first 150
lines; it is a consumer-brands name and its Q2 reasoning on store brands was seen, not applied here. (3) The analyst's training
memory holds a prior on PM (a cigarette maker turning to heated tobacco and nicotine pouches, negative book equity, a high
dividend). It is a prior to be replaced by the filings; every fact below is from a filing with its accession.

Research folder: `Test Runs/_research 2026-10-06 PM/` (`fetch.py`, `retry.py`, `run_py_output.txt`, `cover_shares.txt`,
extract notes and arithmetic scripts; raw filings under `cache/`, gitignored).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$189.53** (2026-10-05; `tools/run.py`, Yahoo chart endpoint; **aggregator, live quote only, flagged** under
  operator rule 5; the last quote the tool returned on the run date).
- **Shares by class** from the latest filing's cover: one class, common stock, no par, **1,558,613,439** (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-24, accession `0001628280-26-049493`; `python Screens/cover_shares.py PM`, output
  in `cover_shares.txt`). Preferred: 250 million authorized, none issued (10-K FY2025, Note 7). The proxy counts
  1,558,530,268 outstanding at 2026-03-13 (DEF 14A `0001628280-26-021169`).
- **Market cap:** 1,558.613M x $189.53 = **$295,404M**. (Noncontrolling interests in consolidated subsidiaries,
  $1,966M of book at 2025-12-31, sit outside this figure; their cash is deducted from owner cash below instead.)
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority). PM reports in USD; about 6% of net revenues is Russia and most revenue is
  earned in other currencies (10-K FY2025, Item 1A), so the USD rate is the reporting currency's, not every cash flow's.
- **Filings read** (operator rule 4), all from SEC EDGAR:
  - 10-K FY2025, filed 2026-02-06, accession `0001628280-26-005939` (Item 1, Item 1A, Item 7 including Financial Review
    and Liquidity, the four statements, Notes 7 and 8 on stock, the equity statement).
  - 10-K FY2023, filed 2024-02-08, `0001413329-24-000013`, and 10-K FY2020, filed 2021-02-09, `0001413329-21-000007`
    (cash-flow and equity statements for FY2018 to FY2023); 10-K FY2017, `0001413329-18-000007`, fetched for the balance
    sheets.
  - 10-Q Q2 2026, filed 2026-07-24, `0001628280-26-049493` (balance sheet, cash flow, Note 13 on RBH).
  - DEF 14A filed 2026-03-26, `0001628280-26-021169` (CD&A, incentive targets, Summary Compensation Table, ownership).
  - 8-K 2026-07-22, `0001628280-26-049107`, Ex 99.1 (Q2 2026 earnings release), read before judging non-GAAP habits.
  - Competitors: Altria 10-K FY2025, `0000764180-26-000017`; British American Tobacco 20-F FY2025, `0001303523-26-000017`.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$12,233
  million** on the filed cash-flow statement (10-K `0001628280-26-005939`) = `tools/run.py` 12,233. Also total PMI
  stockholders' deficit $(9,994)M and goodwill $17,264M on the filed balance sheet = run.py -9,994 and 17,264.
- **`python tools/run.py PM`, arithmetic lines only** (`run_py_output.txt`; its v4 material ignored, Part VII). run.py
  found **no stock-pay tag** ("n/f") and deducted nothing for stock pay, and it does not deduct the cash paid to the
  minority owners of consolidated subsidiaries; both are real costs to PM's owners, so owner cash was rebuilt from the filed
  statements (`owner_cash.py`, output `owner_cash_output.txt`):

| FY | OCF | stock pay | capex | D&A | paid to NCI | owner cash, capex basis | owner cash, D&A basis | acquisitions and rights | dividends |
|---|---|---|---|---|---|---|---|---|---|
| 2018 | 9,478 | 128 | 1,436 | 989 | 435 | 7,479 | 7,926 | 0 | 6,885 |
| 2019 | 10,090 | 160 | 852 | 964 | 378 | 8,700 | 8,588 | 1,346 (RBH cash deconsolidated) | 7,161 |
| 2020 | 9,812 | 160 | 602 | 981 | 602 | 8,448 | 8,069 | 0 | 7,364 |
| 2021 | 11,967 | 197 | 748 | 998 | 560 | 10,462 | 10,212 | 2,111 | 7,580 |
| 2022 | 10,803 | 155 | 1,077 | 1,077 | 472 | 9,099 | 9,099 | 16,473 (Swedish Match 13,976; Altria IQOS rights 1,002; SM minority 1,495) | 7,812 |
| 2023 | 9,204 | 193 | 1,321 | 1,398 | 497 | 7,193 | 7,116 | 2,658 (Altria 1,775; SM minority 883) | 7,964 |
| 2024 | 12,217 | 195 | 1,444 | 1,787 | 494 | 10,084 | 9,741 | -43 | 8,197 |
| 2025 | 12,233 | 208 | 1,569 | 1,996 | 430 | 10,026 | 9,599 | 0 | 8,624 |
| **5-yr mean 2021-2025** | | | | | | **9,373** | 9,153 | | |

  USD millions, as filed. Stock pay is the "Issuance of stock awards" line of each year's equity statement (the expense
  credited to equity; the FY2025 Note 8 gives RSU expense of $175M plus the PSU expense). Paid to NCI is the equity
  statement's dividends or payments to noncontrolling interests. Owner cash is after interest (cash paid $1,688M in 2025)
  and after cash taxes ($3,852M in 2025). The 2025 OCF includes a **$0.5B dividend from RBH**, the deconsolidated
  Canadian affiliate (Item 7, Financial Review); under the equity-method CONVENTION (Q4) the dividend received is the cash
  counted. OCF is also helped by **factoring of trade receivables** and a **supply-chain financing** programme (Item 7,
  Liquidity; Notes 17 and 20); amounts not quantified here. Capex basis is the lower base in 2018 and 2020 and the
  higher in the other years; D&A from 2023 includes amortization of the Swedish Match intangibles, which is not a
  replacement cost, so the capex basis is used as the base and the D&A basis shown beside it.
  Sums FY2018-2025 (`owner_cash_output.txt`): owner cash 71,491; dividends 61,587; acquisitions and rights 22,545;
  buybacks 984. The gap of 13,625 was borrowed: debt on the face of the balance sheet rose from 31,759 (2018) to 48,835
  (2025) (`run_py_output.txt`).
- **Six months to 2026-06-30** (10-Q `0001628280-26-049493`): OCF $5,093M (prior year $3,062M), capex $733M; long-term
  debt $42,366M plus current $3,406M; PMI stockholders' deficit $(8,583)M.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, and for PM it turns on whether the cigarette cash keeps coming while the smoke-free products replace it,
not on the quote. The market serves and does not instruct: the $189.53 quote "just tells us prices" **[M2006-077]**.
Who is paid to tell you: the Q2 2026 release headlines "Adjusted Diluted EPS grew by 15.2%" above "Reported Diluted EPS
declined by 7.7%" (Ex 99.1 to `0001628280-26-049107`); "you do not get impartial advice from Wall Street" **[M2020-037]**,
and a company's own release is read the same way. Margin of safety is an attitude here and arithmetic only at Q7
**[M1997-126]**. No macro enters: the excise, currency and Russia lines are read as properties of the business
**[M2000-094]**. The analyst's habits: hunt "what you’re missing" **[M2025-013]**; and the analyst's prior (a
famously strong tobacco franchise) is the anchor the rows warn against, "always your previous conclusion" **[M2016-054]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The filer's own risk factor: "The financial and business performance of our smoke-free products is less predictable
   than our cigarette business." (10-K FY2025, Item 1A). Smoke-free was $16,854M of $40,648M net revenues in 2025.
2. Owner cash (capex basis) was **$10,026M in 2025 against $10,462M in 2021**, after about $21.2B was spent in
   2021-2023 on acquisitions, the IQOS U.S. rights and Swedish Match minority buyouts (table above).
3. Debt on the face of the balance sheet rose from $27,806M (2021) to $48,835M (2025); PMI stockholders' deficit
   $(9,994)M at 2025-12-31 (`run_py_output.txt`; 10-K FY2025 balance sheet).
4. U.S. ZYN: "ZYN offtake volumes were flat to slightly growing versus the prior year" in Q2 2026 and U.S. net revenues
   fell 0.7% (Ex 99.1 to `0001628280-26-049107`); competitors' pouches are growing fast: BAT's Modern Oral in the U.S.
   "up 297%" on the Velo Plus launch (BAT 20-F `0001303523-26-000017`), and Altria received FDA marketing orders for on!
   PLUS in December 2025 (Altria 10-K `0000764180-26-000017`).
5. RBH (the deconsolidated Canadian business under a court-approved plan): impairment $2,316M in 2024 and $511M in Q2
   2026; carrying value down to $51M (10-Q `0001628280-26-049493`, Note 13).
6. Collateral posted for derivatives: $2,274M paid in 2025, against $50B gross notional of derivatives (10-K FY2025,
   cash-flow statement and Item 7); a demand for cash the standing rule names.
7. Russia: about 6% of net revenues and 9% of cigarette and HTU volume; $2.3B of the $4.9B cash at year end was held in
   Russia, under capital controls (10-K FY2025, Items 1A and 7).
8. Cigarette shipments fell 1.5% in 2025 and the company guides to about 3% lower in 2026; Turkey share 52.0% to 46.4%
   (10-K FY2025, Item 7).
9. Regulation and tax: characterizing-flavor ban in Poland hit IQOS (Q2 2026 release); Germany's supplemental surcharge
   on heated tobacco, about $0.8B paid in January 2025 under dispute (10-K FY2025, Item 7); excise taxes on products were
   $53,211M in 2025, more than net revenues (income statement note).

## THE STANDING RULE
Owning PM shares bought with the buyer's own money, sized so that a total loss could be borne, does not put the buyer at
risk of ruin; bought on margin it would: "borrowed money has no place in the investor's tool kit" **[L2014-005]**;
"We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. The target's
own debt and collateral are weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What it is, from the 10-K** (`0001628280-26-005939`, Items 1 and 7): cigarettes sold in about 170 markets outside
  the U.S. (607.4 billion units in 2025; Marlboro about 43% of cigarette volume; PM cigarette share 25.3% of the
  international market excluding China and the U.S.), and smoke-free products in 106 markets: heated tobacco units for
  IQOS (155.1 billion units), nicotine pouches and snus (ZYN, General; 1,240 million cans), and e-vapor (VEEV). Net
  revenues $40,648M, of which combustibles $23,794M and smoke-free $16,854M. From 2026 three segments: International
  Smoke-Free, International Combustibles, U.S.
- **The key variables** **[M1998-044]**: (a) cigarette volume, falling slowly (-1.5% in 2025, about -3% guided for
  2026); (b) the price PM can take over excise increases; (c) the rate at which smokers move to IQOS and pouches and PM's
  share of them; (d) the excise and regulatory treatment of the smoke-free categories, market by market. (a) and (b) have
  a long filed record: in 2025 pricing added $1,536M of revenue against a cigarette volume decline (Financial Summary,
  Item 7). (c) is about customers, which the rows call projectable: "we know what we think we can project out in terms of
  consumer behavior and threats to a business." **[M2023-030]**; the product is the same nicotine habit in a new form,
  and the switching runs mostly into PM's own products (HTU international share 5.3% to 5.8%; PM holds "around
  three-quarters volume share" of heat-not-burn, Q2 2026 release `0001628280-26-049107`).
- **Is it important and knowable?** **[M2006-076]** (d) is the variable least in PM's hands: the filer itself calls the
  smoke-free business "less predictable than our cigarette business" (Item 1A), and the rows warn that "We view change as
  more of a threat into the investment process than an opportunity." **[M1999-063]**. Against it: the direction of the
  change (cigarettes to reduced-risk nicotine, with PM leading the heated category) is the company's stated strategy and
  has been reported year by year since 2014 (IQOS launched in Nagoya, Item 1); the uncertainty is in rate and tax, not in
  who the leader is. "Can I name the winner, not just the industry?" **[M2012-067]**: in heated tobacco, yes, on PM's
  share of the category and BAT's own heated-products revenue of £914M against PM's $16.9B of smoke-free revenue (BAT 20-F
  `0001303523-26-000017`); in U.S. pouches, not with the same confidence (contrary evidence 4).
- **Would the insiders write it down?** **[M2000-105]** PM publishes forward volume, revenue and cash guidance each year
  (2026: "broadly stable total ... shipment volume", OCF "around $13.5 billion", Item 7); insiders do write the forecast
  down here, which separates it from the technology case of that row.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. The
  doubt is real for one segment (U.S. oral, about 8% of revenue on the Q2 2026 segment table: $0.9B of $11.2B) and for
  regulation of the new categories. It is not a doubt about where the bulk of the economics will be: a cigarette and
  heated-tobacco franchise outside the U.S., priced above excise, with volume roughly flat to slowly falling. The
  understanding asked is "a reasonable fix on about what the earning power and competitive position will look like in
  five or 10 years" **[M2012-065]**, and "that didn’t mean we had to do it to four decimal places" **[M2015-086]**.
- **VERDICT: IN.** The ten-year economics rest mainly on two variables with a long filed record (cigarette volume and
  price, 2018-2025) and on a switch to products PM leads; the less predictable part is named and carried to Q2 as the
  question of what could destroy or reduce the castle **[M2000-014]**, not used to close the file. The analyst's prior
  points the same way, so the doubt is written down at contrary evidence 1, 4 and 9 **[M1997-127]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**
- **Pricing power, and the agony before a rise** **[M2005-020]**: in 2025 the price variance added **$1,536M** to net
  revenues while cigarette volume fell 1.5%; net revenues ex currency and acquisitions +6.5% (10-K FY2025, Financial
  Summary). In Q2 2026 international combustibles took "an exceptional quarter of 10.0% pricing" with cigarette volume
  +1.1% and category share flat at 25.3% (Ex 99.1 `0001628280-26-049107`). The rows' test: "Anytime you can charge more
  for a product and maintain or increase market share against wellentrenched, well-known competitors, you have something
  very special in people’s minds." **[M2000-031]**. Price is taken on top of excise of $53,211M in 2025 (income statement
  note), so the consumer pays the tax rise and PM's rise together. Passes.
- **Unit volume and share of mind** **[M1999-054]**: total shipments up 1.4% in 2025 and a "fifth consecutive year of
  volume growth" (DEF 14A `0001628280-26-021169`, letter); international share cigarettes plus HTU 28.6% (2023), 29.0%,
  29.2% (2025); Marlboro cigarette share 9.8%, 10.2%, 10.7% (10-K FY2025, Item 1 table). Volume of the old product falls,
  the new product's rises; the battery row holds that unit declines alone are no fail, "we’ll do fine with the Duracell investment" **[M2015-066]**.
- **The brand in the customer's mind** **[M2008-075]**, **[M2023-073]**: Marlboro is "the world’s best-selling
  international cigarette" (Item 1); it is asked for by name against the low bid **[M2017-009]**, shown by price taken
  without share lost. The counter-row is Marlboro's own home market, in Altria's hands: U.S. smokeable volume -10.0% in
  2025 with pricing +$1,680M against lower volume -$2,426M (Altria 10-K `0000764180-26-000017`); the brand holds price
  there too, but the U.S. category is shrinking faster.
- **The money test** **[M1997-103]**, **[M2011-015]**: could a well-funded attacker take heated tobacco from PM? BAT has
  tried for a decade with glo: BAT's heated-products revenue was **£914M** in 2025, down 0.7% (BAT 20-F
  `0001303523-26-000017`), against PM's smoke-free net revenues of **$16,854M** (mostly IQOS). Altria, which held the
  U.S. IQOS rights until 2024, sold them back to PM for $2.7B ($1,002M in 2022 and $1,775M in 2023, PM cash-flow
  statements). In pouches the attack is live: BAT's U.S. Modern Oral +297% on Velo Plus; Altria's on! PLUS authorized
  December 2025 (contrary evidence 4).
- **Ask the competitors** **[M1999-130]**, **[M2025-043]**: on the public record, BAT's 20-F says of its competitors
  that they "may be able to do so more quickly and at a lower cost" (20-F, risk factors, of developing and rolling out
  new products); Altria's 10-K names "illicit flavored disposable e-vapor products" as the cross-category drain on cigarettes
  (2% to 3% of the U.S. industry decline). Neither names PM's heated position as beatable; no instance found in either
  filing of a stated heated-tobacco share above PM's.
- **The low-cost position** **[M2018-043]**: not the claim made; PM's castle is brand, scale of distribution in 170
  markets, and the regulatory authorizations it holds (the first FDA marketing and MRTP orders for a heated product and
  for snus, Item 1), which the rows count among moats of "any kind of reason at all" **[M1995-037]**.
- **Would it stand without the lord?** **[M1995-038]**, **[M1996-037]**: the cigarette business would; the transition
  needs continued product and regulatory work ("we must continue transforming our culture", Item 1). Leans on management
  more than See's; carried to Q5.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**: widening internationally (HTU share +0.5 points in 2025;
  IQOS 9.2% of combined cigarette and HTU volume where present, +0.2 points, Q2 2026 release); narrowing in U.S.
  pouches (ZYN flat while competitors grow). Cigarette-over-cigarette share 25.5% to 25.3%: a notch, not a breach.
- **What could destroy, modify or reduce it, five to fifteen years out** **[M2000-014]**: (i) tax: if governments tax
  heated tobacco like cigarettes, the margin of the new product falls (Germany's surcharge; the filer's own risk factor
  "We may be unsuccessful in our efforts to differentiate smoke-free products and cigarettes with respect to taxation",
  Item 1A); (ii) bans and flavor rules (Poland); (iii) illicit and counterfeit supply, "Marlboro is the most heavily
  counterfeited international cigarette brand" (Item 1A); (iv) Russia (6% of revenues). Each reduces; none, on the filed
  record, destroys the brand's pricing in the main markets. The would-it-be-started-today test **[L2006-008]** cuts for
  PM: a nicotine company starting today could not buy the distribution, the authorizations or Marlboro.
- **The competitor row** (same metric, own filings, FY2025):

| company | filing | revenue growth, ex currency | combustible price vs volume | heated or new-category revenue |
|---|---|---|---|---|
| Philip Morris International | 10-K `0001628280-26-005939` | +6.5% (organic) | price +$1,536M; cigarette volume -1.5% | smoke-free $16,854M, +15.0% reported |
| Altria | 10-K `0000764180-26-000017` | net revenues -3.1% (reported, U.S. only) | smokeable price +$1,680M vs volume -$2,426M; U.S. cigarette volume -10.0% | on! 177.8M cans; NJOY impaired |
| British American Tobacco | 20-F `0001303523-26-000017` | +2.1% (constant currency) | U.S. price/mix +12.3% vs volume -7.7% | New Categories £3,621M; heated (glo) £914M |

  PM grows its top line faster than both and carries the largest heated business by a wide margin; its pricing holds
  where the other two lose more volume to price.
- **VERDICT: IN.** The castle is standing on the evidence: price taken above excise with share held, the leading position
  in the category its own customers are moving to, and rivals' own filings showing their heated products far smaller.
  The narrowing in U.S. pouches and the tax treatment of heated tobacco are what could reduce it **[M2000-014]**; they
  are written down as contrary evidence 4 and 9 **[M1997-127]**, and they bear on "how sure" at Q7 **[M1999-104]**,
  not on whether a castle exists. Not tenuous enough to be unvaluable **[M2000-019]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**: at 2025-12-31, tangible operating assets
  (total assets less goodwill, intangibles, equity investments and cash) $33,274M, less non-interest-bearing current
  liabilities (payables, accrued marketing, excise and other taxes, employment costs, other, income taxes) $19,414M,
  leaves **$13,860M** of net tangible operating capital against operating income of $14,892M: about **107% pre-tax**
  (`q3_capital.py`, 10-K `0001628280-26-005939` balance sheet). Much of the low capital is excise collected before it is
  paid ($7,555M of accrued non-income taxes), which is float from governments, real while the business runs. Ruled out
  first, per **[L1994-009]**: not a cyclical peak (operating income 11,377 in 2018 to 14,892 in 2025, rising most years),
  and the return is on assets, not on an equity shrunk by buybacks **[M1998-017]** (equity is negative, so return on
  equity is meaningless here).
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**: capex rose from $602M (2020) to $1,569M
  (2025), "primarily related to our ongoing investments in smoke-free product manufacturing capacity" (Item 7); 2026
  guided at $1.4B to $1.6B. Depreciation and amortization $1,996M in 2025 includes amortization of the Swedish Match
  intangibles. No maintenance figure is given by the filer; the depreciation charge is taken as the stay-in-place guess
  **[M1998-127]**, and on either basis reinvestment is small against $12.2B of operating cash: the profit ends the year
  as cash **[M2008-036]**.
- **What the added capital earned** **[M2001-019]**: the growth did not come from the tangible base. From 2018 to 2025
  PM spent $22,545M on acquisitions, rights and minority buyouts (Swedish Match, the IQOS U.S. rights, Fertin, Vectura
  and others, with $1,346M of RBH cash deconsolidated in 2019), funded by debt (Step 0). Over the same years operating
  income rose $3,515M and owner cash $2,547M: about **11% after tax on the purchased capital**, or 15.6% pre-tax on
  operating income (`q3_capital_output.txt`), before crediting any of the gain to the base business's own pricing. The
  Vectura purchase was sold at a loss of $199M in 2024 (Item 7). The rows call this kind of business "good enough"
  where the added sums earn decently **[L2009-012]**, **[M2018-055]**; the 2021-2025 window shows aggregate owner cash flat
  to down (-1.06% a year on the capex basis) after the largest purchase.
- **WEIGHS FOR.** The base business needs almost no tangible capital to produce its earnings, "The best business is one
  that gives you more and more money every year without putting up anything to get it, or very little." **[M1998-081]**;
  the growth bought with borrowed money has earned a fair, not a rich, return so far, which weighs against the
  reinvestment and is carried to Q6 and Q7 **[M1995-113]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends 2016-2025** **[M2025-032]** (`run_py_output.txt`, first-filed XBRL; the
  2025 and 2024 columns read against the filed balance sheet in `0001628280-26-005939`, the 2017 sheet in
  `0001413329-18-000007`). What moved, and why:
  - **Equity negative throughout**, $(12,688)M (2016) to $(9,994)M (2025). The cause is on the face of the sheet: cost of
    repurchased stock $35,551M (552.7 million shares, bought in earlier years; buybacks in 2018-2025 were only $984M) and
    dividends nearly equal to earnings, so retained earnings rose only from $30,397M to $35,400M in nine years while net
    earnings ran $7.1B to $11.3B a year. Negative equity here is a record of cash paid out, not of losses; "a low
    price-book ratio means nothing to us" **[M1998-116]**, and the inverse is as uninformative.
  - **Goodwill and intangibles**: $7,324M and $2,470M (2016) to $17,264M and $10,884M (2025); the step is 2022
    (Swedish Match). Purchased goodwill is read when judging the capital allocation, "because we paid for it"
    **[M2011-060]** (Q6).
  - **Debt**: $29,067M (2016), $27,806M (2021), $48,835M (2025); total debt "primarily fixed rate", weighted maturity about
    7 years (Item 7). Q9.
  - **Receivables against sales**: $3,499M to $4,572M while net revenues went from $29,625M (2018) to $40,648M (2025);
    receivables stayed low partly because $1.0B of sold receivables were outstanding at 2025-12-31 ($0.9B 2024, $1.6B 2023;
    Note 17). The factoring and the supplier-finance programme ($1,014M due to participating suppliers at 2025-01-01,
    Note 20) move cash between years; both are disclosed.
  - **Inventory** $9,017M (2016) to $11,478M (2025), up $1,201M in 2025 alone, which the filer ties to excise-tax-paid
    inventory moved ahead of excise increases (Item 7). Inventory is in line with revenue growth over the decade.
  - **Cash** $4,239M to $4,872M; $2.3B of the 2025 figure is in Russia (Item 7).
  What the figures "can’t say" **[M2025-032]**: the value of the brands built inside the company (Marlboro, IQOS) is not
  on the sheet at all; only purchased brands are.
- **The real costs** **[L2021-003]**: depreciation $1,996M (2025) is counted; stock pay $208M (equity statement) is
  counted in owner cash although run.py missed it; cash to minority owners $430M is counted. **EBITDA in the filer's
  own mouth**: earnings are spoken in "adjusted operating income" and "adjusted diluted EPS"; EBITDA appears once, as the
  leverage target, "net debt to adjusted EBITDA ratio improvement as we target a ratio of close to 2.0x by the end of
  2026" (Q2 2026 Ex 99.1; no instance in the FY2025 10-K by text search). The rows measure coverage as "pre-tax
  earnings/interest, not EBITDA/interest" **[L2012-002]**: on that basis 2025 earnings before income taxes $13,880M plus
  net interest $966M, against net interest of $966M, is about fifteen times (income statement). Not EBITDA talk about
  earnings. **Restructuring as a recurring "one-time"**
  **[L2016-007]**, **[L1998-031]**: a restructuring or asset-impairment-and-exit line appears in every cash-flow statement
  read, 2018 to 2025, and the 2025 charges of $241M restructuring, $176M German excise litigation and $94M loss on
  businesses sold follow $180M, $199M (Vectura) and $45M in 2024 (Item 7, Financial Summary note 1). These are counted
  as costs here: owner cash is after them.
- **Adjusted earnings featured** **[L2016-006]**: the Q2 2026 release puts "Adjusted Diluted EPS grew by 15.2%" in the
  headline beside "Reported Diluted EPS declined by 7.7%", and the reported decline is explained (the $511M RBH
  impairment, fair-value losses on equity securities). The incentive plan pays on adjusted net revenues and adjusted OI
  (DEF 14A). One tell.
- **A second tell?** **[L2002-039]**: the make-the-numbers habit **[L2002-041]** is not shown by these filings: the
  proxy reports targets met ("on target" for revenue and OI, OCF exceeded), not a run of years beating a stated number,
  and the multi-year record was not swept here. No reserves found moving with a stock sale, no prepaid or deferred
  accounts building out of line (other current assets not flagged by the filer or the sheet), no profits on both sides of
  a contract. Under the two-tell CONVENTION (Q4, ours) the adjusted-earnings habit alone weighs against and is not
  suspicion.
- **Confusion?** **[M1995-063]**, **[M2003-029]**: no. The statements reconcile (OCF cross-checked in Step 0); the
  items that flatter (factoring, RBH dividend, collateral moving between operating and investing) are each disclosed and
  quantified by the filer.
- **VERDICT on confusion: IN. WEIGHS AGAINST** on the accounts' character: adjusted figures featured, and charges called
  special that recur every year. The recast earnings fed to Q7 are owner cash after every one of them (Step 0).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a marketable stock the speakers read rather than meet **[M2007-081]**; the reading tests carry the weight.
- **The first yardstick, the record against the hand dealt** **[M1994-008]**: Jacek Olczak, CEO since 2021 (COO before;
  DEF 14A `0001628280-26-021169`), and André Calantzopoulos, CEO before him and Chairman since 2024. Dealt a cigarette
  business losing volume to regulation and tax, they built a heated-tobacco business from launch in 2014 to the largest
  in the world (three-quarters of the category by volume, Q2 2026 release) and kept cigarette share near 25%. Against
  peers on the same years: PM's organic revenue +6.5% in 2025, against Altria -3.1% and BAT +2.1% at constant currency
  (Q2 competitor row). The capital half of the record (Swedish Match, Vectura sold at a loss, RBH written down) is Q6's.
- **The tells of dishonesty the rows name**: the proxy **[M1994-009]**, read for how they treat themselves against the
  owners: CEO total compensation $29,072,171 in 2025, $20,237,916 in 2024, $25,480,514 in 2023 (Summary Compensation
  Table), with 60% of the equity grant in PSUs; anti-hedging and anti-pledging policies; share ownership guidelines; no
  severance or change-in-control provisions in NEO agreements except the CFO's (DEF 14A). Rich, and disclosed in full; no
  instance found of the self-dealing the rows name. Reports that dance **[M1995-111]**, **[M2007-082]**: the key figures
  of this industry (volume by category, share by market, pricing variance, excise) are published market by market in the
  10-K (Item 7 key market data table), including the unflattering ones (Turkey share 52.0% to 46.4%, U.S. ZYN flat).
  Stock price in the lobby **[M2004-067]**: 40% of the PSU weight is total shareholder return (Note 8), a fixation the
  rows warn of, carried to Q6 Part B as pay design rather than as a sign of cheating. Serial issuance **[L2014-015]**:
  none; shares outstanding 1,556.7 million at 2025-12-31 against 1,554.8 million at 2024-12-31, only stock awards (Note 7).
- **How they talk about mistakes** **[L2024-003]**: the Q2 2026 release says "challenging" of the U.S. first quarter
  and "transient headwinds" of Japan and Poland, and the proxy letter "challenging and volatile" of the world economy; no instance found of "mistake" or "wrong" in the proxy or
  the Q2 release (text search). The RBH and Vectura losses are reported in the notes, not owned in the letter. Weighs
  against, mildly: the rows ask to be told "when you make mistakes" **[M2010-081]**.
- **Governmental investigations** (10-K FY2025, Item 1A and Note 16): allegations "of contraband shipments of
  cigarettes, ... unlawful pricing activities, ... underpayment of income taxes, customs duties and/or excise taxes" in
  several markets; the Germany excise classification charge $176M (2025). These are written down **[M1997-127]**. They
  are allegations against an industry in many jurisdictions, with no finding against these managers personally in the
  filings read; integrity is applied on doubt alone **[M2013-088]**, and the doubt the rows mean is doubt about the
  people, which the filed record does not raise.
- **Love of the business** **[M2000-098]**: both leaders are career PM employees; the CEO owns 500,844 shares (about $95M
  at the run price) and the Chairman 986,075 (DEF 14A ownership table), so their own money rides with the owners'.
- **VERDICT on integrity: IN** (no doubt raised by the proxy, the letters or the accounts about these people's honesty
  **[M2015-047]**). **Ability WEIGHS FOR**: a new category built and led against two capable rivals, and the old one
  priced and held **[M1999-104]**; the capital record is weighed at Q6.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**: PM retains almost nothing. Retained earnings rose from
  $29,859M (2017-12-31) to $35,400M (2025-12-31), about $5.5B kept out of about $67.5B of net earnings attributable to
  PM over the eight years (income statements 2018-2025, 10-Ks `0001413329-21-000007`, `0001413329-24-000013`,
  `0001628280-26-005939`); dividends declared were $5.64 a share in 2025 against diluted EPS of $7.26. "a company that
  expects to regularly earn more than it can profitably employ in its business, should be paying out dividends."
  **[M2004-089]**: the policy matches the business. What was reinvested beyond the dividend was borrowed: $22,545M of
  acquisitions and rights 2018-2025 against debt up $17,076M (Step 0). The forward question, "Can you keep using all of
  the capital you generate, effectively, for a very long time?" **[M2010-097]**, is answered by the company's own choice:
  no; it pays the cash out.
- **The deals: value given against value got** **[M1995-001]**, **[L2014-012]**: Swedish Match ($13,976M net cash in 2022
  plus $2,378M for its minority in 2022-2023) was paid in **cash, not stock**, so the one STOP of Part A **[L2009-019]**
  does not arise. What it earned: aggregate owner cash 2021 $10,462M, 2025 $10,026M; operating income 2021 $12,975M,
  2025 $14,892M, against $19.2B paid in 2021-2023 for Swedish Match, its minority and the IQOS U.S. rights; Vectura (2021)
  sold at a $199M loss in 2024; RBH written down by $3,060M cumulatively (10-Q Note 13). Gains real but modest so far on
  the largest outlay; "it is our judgment on a 10-year basis." **[M1999-061]**, and the window is four years. Weighs
  against, provisionally.
- **Buybacks**: none since 2022 ($775M in 2021, $209M in 2022; cash-flow statements). No programme is in force, so the
  no-stated-price test has nothing to read; the shares bought before 2018 ($35.6B at cost) are history this run did not
  price against a value.
- **Issuance**: none beyond stock awards (Q5); no serial issuer **[L2014-015]**.
- **Part A WEIGHS AGAINST, mildly**: the dividend policy fits a business that cannot use its cash, but the one large
  redeployment was debt-financed and has not yet shown more than a fair return on what it cost. The cost of a deal is
  "measured by the second best deal that’s around at a given time" **[M2001-084]**; on the evidence so far, paying down
  debt would have done about as well.

**Part B, the pay, the board, the owners.**
- **Pay tied to what the person controls** **[M2003-019]**: the annual incentive pays on top-30 market share, smoke-free
  shipment volume, adjusted net revenue growth, adjusted OI growth and operating cash flow (DEF 14A, 2025 targets), all
  inside management's reach; the operating-cash-flow target can be helped by receivable factoring (Q4), a weakness, not a
  finding. The PSUs pay 40% on total shareholder return, relative and absolute (10-K Note 8), the market's ride the rows
  name **[M2000-062]**; 30% on adjusted EPS growth; 30% on a sustainability index.
- **Size and design**: CEO pay $29.1M in 2025 on targets "met or exceeded" for a rating of 115 (DEF 14A); the committee
  sets pay by "reference market data and relative positioning ... versus other CEOs in our Peer Group" (DEF 14A), the
  ratchet the rows describe **[M2012-095]**, **[L2005-015]**.
- **The board**: Chairman is the former CEO, not the current one, with a Lead Independent Director (DEF 14A); the rows'
  worst case, the mediocre CEO who also chairs **[L2014-026]**, is not present. Director share retention of five times the
  cash retainer (DEF 14A); directors' holdings are small against their pay (most 3,418 to 28,646 shares).
- **Owners as partners**: the CEO's 500,844 shares and the Chairman's 986,075 are their own money at risk with the owners'
  **[L2019-008]**; guidance is given each year (OCF, EPS, volume), the habit the rows invert **[M2022-054]**.
- **Part B WEIGHS AGAINST, mildly**: rich pay set by peer comparison and partly on the share price, guidance given;
  against it, controllable annual metrics and large personal holdings.

**WEIGHS AGAINST** (both parts, mildly).

## Q7 — WHAT IS IT WORTH? STOP.
"how much do you get back, how sure are you of getting it, when do you get it?" **[M2009-004]**, at the long government
rate **[L2000-021]**, **[M1996-025]**, as a range **[L2000-024]**. Arithmetic in `q7_calc.py`, output `q7_calc_output.txt`
(computed early and headed "COMPUTATION — NOT A CLEARANCE" until this question opened).
- **How much cash**: five-year mean owner cash after every real cost, FY2021-2025, **$9,373M** on the capex basis
  ($9,153M on the D&A basis) **[L2021-003]**, **[L2005-003]** (Step 0). Owner cash yield at the price: 9,373 / 295,404 =
  **3.17% after tax**.
- **The growth shown** (CONVENTION, Q7, the range; measured on aggregate owner cash): 2021 $10,462M to 2025 $10,026M, **-1.06%
  a year**. The base year 2021 was a strong cash year (working capital released, Step 0), and the longer record 2018-2025
  shows +4.28% a year; the convention fixes the window, and the longer rate is shown beside it as a comparison only,
  never as an end of the range **[M1999-067]**.
- **How sure** **[M1999-104]**: the castle stands (Q2) and cigarette pricing has a long record, but the cash is earned in
  roughly 170 currencies, 6% of revenue is Russia with $2.3B of cash held there, and the new category's tax treatment is
  the least predictable variable (Q1, Q2). Held as a range, not a point **[L2005-001]**.
- **Value range** (ten years at the growth case, then zero nominal growth, discounted at 5.66%; CONVENTION):

| case | capex basis | D&A basis |
|---|---|---|
| shown growth, -1.06% | $152,307M = **$97.72** a share | $148,732M = $95.43 |
| no growth | $165,601M = **$106.25** a share | $161,714M = $103.75 |
| comparison only: 2018-2025 growth, +4.28% | $232,454M = $149.14 | $226,998M = $145.64 |

  **Value range: $97.72 to $106.25 a share against $189.53.** The range is narrow (about 1.09 to one), so it does not close
  TOO HARD **[L2000-025]**. Even the comparison case outside the convention, $149.14, sits below the price.
- **The floor** (CONVENTION, about ten percent pre-tax, **[M2003-149]**, **[L2002-020]**): at the FY2025 effective tax
  rate of 19.7% (provision $2,737M on pre-tax earnings $13,880M), ten percent pre-tax is about **8.03% after tax**. At
  $189.53 the expected return is the 3.17% owner cash yield plus growth: negative growth on the convention's window,
  +4.28% on the longer one, so about 3% to 7.5% after tax, below the floor in every case. The price implies 2.49% a year
  of perpetual growth at the sovereign rate, more than the five-year record and about half the eight-year one.
- **The prices at which it would clear** (owner cash / (8.03% - growth), on the capex basis): no-growth owner cash clears
  the floor at **$74.91** ("cheap"); the central case, the midpoint of the two ends (-0.53%), at **$70.27** ("fair");
  because the shown growth is negative the "fair" price sits below the "cheap" one, which the convention's labels did not
  anticipate (last section). The comparison growth of 4.28% would clear at $160.45.
- **VERDICT: OUT.** The price is above the top of a narrow range, so the expected return at the price is below the floor
  and the name is quit on, not ranked: "there’s just a point at which we drop out of the game." **[M2003-149]**; and it is
  nowhere near a price that would "scream at you" **[M2009-005]**. A wonderful business can be bought at a fair price
  **[M2003-040]**, but the rows also say "you can pay too much for a wonderful business" **[M2019-013]**.

Q6's buyback test, which needs the bottom of this range, has no buyback to read (no repurchases since 2022).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED (Q7 closed OUT).
## Q9 — COULD IT RUIN US. NOT REACHED. Facts found on the way are recorded for a later run, not weighed: debt $48,835M at
2025-12-31 (fixed rate mostly, about 7 years average maturity); $2,274M of derivative collateral posted in 2025 on $50B
gross notional; committed revolvers $6.3B undrawn with no rating triggers or collateral provisions (10-K FY2025, Item 7).
## Q10 — THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED. Noted for the record, not answered: the
business is cigarettes and nicotine, which the rows name for a whole business bought and run ("we sat down in the lobby
and just decided that we didn’t want to be in that business." **[M2005-097]**) and leave a WEIGHING for a marketable
stake ("we would not have trouble owning stock in a cigarette company" **[M2005-096]**).

---
## THE BOX
**OUT, at Q7.** Value range **$97.72 to $106.25** a share (owner cash after every real cost, five-year mean $9,373M,
shown growth -1.06% to no growth, at the 5.66% Treasury 30-year) against **$189.53**; the expected return at the price
(about 3% to 7.5% after tax) is below the floor of about ten percent pre-tax (about 8.03% after tax), so the name is quit
on **[M2003-149]**. Q1 IN, Q2 IN, Q3 weighs for, Q4 IN on confusion and weighs against, Q5 IN on integrity and ability
weighs for, Q6 weighs against mildly. The price at which no-growth owner cash clears the floor is $74.91; the central
case clears at $70.27. **What would reverse it:** a price near $75, or owner cash shown growing fast enough that the
expected return at the market price clears the floor (at $189.53, 8.03% less the 3.17% yield: about 4.9% a year sustained
on aggregate owner cash, above even the 2018-2025 record of 4.28%).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `eed39b7` holds the template copy and the first tool output; the
      first filing fetch followed the copy); written question by question; committed after each (Q1 `86de701`, Q2
      `7e9920f`, Q3 `34ea813`, Q4 `8bf5747`, Q5 `8e79823`, Q6 `18d781f`, Q7 `a636e48`). One departure: `q7_calc.py` was
      written and committed with the Q1 commit, before Q2 to Q4 closed; its output is headed "COMPUTATION — NOT A
      CLEARANCE" (operator rule 3) and was not read into any verdict before Q7.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before it was written; `tools/check_framework.py`
      check 5 passed); every filing fact has its accession; no number without a filing or a CONVENTION label.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; Q8 to Q12 are NOT REACHED and nothing after
      Q7 is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): stock pay and cash paid to
      noncontrolling interests added back into the deduction after run.py missed both; the sovereign from the US
      Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (nine items under the foundations).
- [x] No row dated after the anchor is cited (the run is dated today; no point-in-time anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its v4 lines were not read as rules.
- [x] `python tools/check_framework.py` PASS before every commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The Q7 range convention breaks when the shown growth is negative.** "The range's two ends are the no-growth case and
the shown-growth case" assumes the shown growth is positive; for PM the five-year window starts in a strong cash year
(2021) and gives -1.06%, so the shown-growth end lies *below* the no-growth end, and the "central case" lies below the
no-growth case: the price at which the central case clears the floor ($70.27) is lower than the price at which no-growth
owner cash clears it ($74.91). The run reported both as computed and did not pick a reading. The convention says nothing
of a picked base year inside its own fixed window, although Q4 cites **[L2005-003]** against exactly that; the eight-year
rate (+4.28%) was shown as a comparison only. It did not decide this run (the price is above every case), but for a name
priced near the range it would. (2) **Q12 comes after Q7**, so a tobacco company closed on price never reaches the
question the rows answer most directly for its industry; for a whole business bought and run the named-business STOP
would close the file before any valuation work. The run noted the rows at Q12 without answering them. (3) **The floor is
stated pre-tax and owner cash is after tax**; the convention does not say how to convert. The run used the filer's own
effective tax rate (19.7%) and says so; a different rate moves the "cheap" and "fair" prices. (4) **Tool defect:**
`tools/run.py` finds no stock-pay tag for PM ("n/f") and therefore deducts nothing for stock pay, and it never deducts
cash paid to noncontrolling interests ($378M to $602M a year here); both were rebuilt by hand from the equity statements.
It also hit SEC HTTP 429 on one filing of three in its statement-lines pass (accession `0001413329-25-000013` not read)
and printed a partial table without failing; the run used the filed statements instead.
