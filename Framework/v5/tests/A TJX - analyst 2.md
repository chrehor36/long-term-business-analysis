# A TJX - analyst 2
**Test A' (reproducibility), ANALYST 2. The TJX Companies, Inc. (NYSE: TJX), CIK 0000109198. Run 2026-10-04 under `Framework/v5/DRAFT - THE FRAMEWORK v5.md` and `Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`. Binds nothing; changes no verdict of record. The operator does not hold this name: Q11 is not answered; Q12 is.**

Working files: `Framework/v5/tests/_work_A2_TJX/` (the tool outputs, the filings as text, the ledger quotes checked, the arithmetic).

Filings read (all SEC EDGAR, primary documents):

| Doc | Filer | Period | Filed | Accession |
|---|---|---|---|---|
| 10-K FY2026 | TJX | FY ended 2026-01-31 | 2026-03-31 | 0000109198-26-000008 |
| 10-Q Q2 FY2027 | TJX | quarter ended 2026-08-01 | 2026-08-28 | 0000109198-26-000048 |
| DEF 14A 2026 | TJX | meeting 2026-06-09 | 2026-04-30 | 0000109198-26-000015 |
| 10-K FY2025 | Ross Stores (ROST) | FY ended 2026-01-31 | 2026-03-31 | 0000745732-26-000006 |
| 10-K FY2025 | Burlington Stores (BURL) | FY ended 2026-01-31 | 2026-03-19 | 0001193125-26-116001 |

Long history (FY2014 to FY2026) is XBRL from the SEC companyfacts feed, each year with the accession of the 10-K that carried it (`_work_A2_TJX/xbrl_history.txt`); it is used for trend only, and every figure that a judgment rests on for the current year is read from the filed FY2026 statements.

---

## 0. Step 0

- **Price:** $132.68, close 2026-10-02. Aggregator, live quote only, **FLAGGED** (operator rule 5).
- **Shares:** one class. Common Stock, par value $1.00: **1,099,974,061** shares, cover page of the 10-Q for the quarter ended 2026-08-01, filed 2026-08-28, accession 0000109198-26-000048 (`python Screens/cover_shares.py TJX`).
- **Market cap:** $132.68 x 1,099,974,061 = **$145.9 billion** (`python tools/run.py TJX` gives $145.94B on a 1,100.0M cover count as of 2026-08-21, the same count).
- **Sovereign, earnings currency USD:** US Treasury daily par yield curve, 30-year, **5.63%** on 10/02/2026 (issuing authority).
- **Cross-check (operator rule 4):** operating cash flow FY2026 of $6,874M from the tool equals "Net cash provided by operating activities | 6,874" in the filed Consolidated Statements of Cash Flows, 10-K accession 0000109198-26-000008; capex $1,957M, D&A $1,247M and share-based compensation $214M also match the filed statement line for line.

## 1. The foundations

A share is a business: the question is whether I would be content to own TJX "if the market closed for five years" **[M1997-109]**, and the test is the business, not the quote. The market serves and does not instruct **[M2006-077]**: the stock was bought back by the company at an average of $154.09 in January 2026 (10-K, Item 5, accession 0000109198-26-000008) and quotes at $132.68 now; neither number says anything about value. No macro forecast enters **[M2000-094]**: tariffs, the IEEPA ruling and the $331M of tariff refunds received in Q2 FY2027 (10-Q, accession 0000109198-26-000048) are treated as a one-time item and a business condition, never as a forecast. Who is paid to tell you **[M2020-037]**: management's "Estimated Store Potential" of 7,000 stores against 5,214 today (10-K, Item 1) is a seller's projection, and the rows say projections are not consulted **[M1995-050]**; it is recorded and not used as an input. The analyst's habits **[M1997-127]**, **[M2025-013]**: the disconfirming facts are written down where found, the first being the draft's own retail warning, "it’s easy to sort of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**, and the second a competitor's filing (Q2). Margin of safety is the attitude carried to Q7: "if you have to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**.

## 2. The standing rule

No. Owning TJX bought with the buyer's own money, unlevered and sized so that a large fall forces nothing, does not put the buyer at risk of ruin; the rule is the buyer's conduct, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, **[M2012-081]**, and no position is taken here.

## 3. Q1 to Q8 in order

### Q1. CAN I UNDERSTAND IT? STOP.

**The test as the draft states it.** "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" and "how the industry will develop and where the company will stand within the industry" **[M2012-065]**; the tests of the section: key variables and their predictability **[M1998-044]**; do the past statements tell the future ones **[M2008-033]**; can I name the winner, not just the industry **[M2012-067]**; is the forecast about customers or technology **[M2017-019]**, **[M2023-030]**; how far off could I be **[M2011-084]**; doubt means outside **[M2002-092]**.

**Applied to the filings.**
- *What it does.* TJX buys brand-name apparel and home goods opportunistically ("closeouts from brands, manufacturers and other retailers; special production direct from brands and factories; order cancellations and manufacturer overruns") from about 21,000 vendors, through a buying organization of over 1,400 Associates, and sells them "at prices generally 20% to 60% below full-price retailers' ... regular prices", with "no ... promotional pricing activity such as sales or coupons" and "a low cost structure compared to many traditional retailers" (10-K Item 1, accession 0000109198-26-000008). E-commerce is about 2% of sales (10-K MD&A).
- *Key variables.* Comp sales (5% FY2026, 4% FY2025), store count (5,214, up about 3%), pre-tax margin (12.1% against 11.5%), inventory turn (10-K MD&A). They are few and they are customer-behaviour variables, not technology variables **[M2017-019]**, **[M2023-030]**: will people keep visiting a store for brand-name goods at a discount, and will the full-price system keep producing excess goods to buy.
- *Do past statements tell the future?* Pre-tax income per diluted share (split-adjusted) went from $2.28 in FY2014 to $6.47 in FY2026, about 9% a year, through the whole internet-retail era (XBRL: FY2014 pre-tax $3,319M, accession 0001193125-16-521424; FY2026 $7,299M, accession 0000109198-26-000008). One year broke the line: FY2021 pre-tax income was $89M (accession 0000109198-21-000006) with stores closed, and FY2022 returned to $4,398M (accession 0000109198-22-000008). The statements read the business; they could not read a forced closure, which is Q9's subject, not Q1's.
- *Can I name the winner?* Yes, within the field: TJX is "the leading off-price apparel and home fashions retailer in the United States and worldwide" and the largest by sales ($60.4B against Ross $22.8B and Burlington $11.5B, the three 10-Ks).
- *Doubt.* The draft names retail as the place understanding is most often mistaken **[M2014-052]**. The same row family names the retailers that can be understood: "You can certainly understand Walmart. [...] You can understand Costco." **[M2002-092]**. I can state the five-to-ten-year picture in one sentence (more stores, similar margin, the same buying model, owners paid out most of the cash) and say how far off I could be: the downside is a margin squeeze or flat comps, not a vanished business **[M2011-084]**.

**Verdict: IN.** The economics are a consumer-behaviour forecast about a fifty-year-old format whose key variables are few and visible in the filings **[M2012-065]**, **[M2017-019]**; the retail warning **[M2014-052]** is carried forward to Q2 and Q5 rather than settled here.

### Q2. WHY IS THE CASTLE STILL STANDING? STOP.

**The test as the draft states it.** "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years from now" **[M1995-038]**; the eleven tests; "when we see a moat that’s tenuous in any way [...] it’s just too risky" **[M2000-019]**.

**Applied, test by test (the ones the filings can reach).**
1. *Key factors and permanence* **[M1995-038]**. The reason the customer comes is price on branded goods: "20% to 60% below full-price retailers' ... regular prices ... every day" (10-K Item 1). The reason it lasts is that the supply (overruns, cancellations, closeouts) is a by-product of the full-price system, and TJX's terms make it the vendors' preferred outlet: it buys "less-than-full assortments", "pay[s] promptly", and does "not ask for typical retail concessions" (10-K Item 1). TJX reports thousands of new vendors in FY2026 and that it has "not experienced difficulty in obtaining sufficient quality merchandise ... in either favorable or difficult retail environments".
2. *Would it stand without the lord?* The superstar test: "if a business requires a superstar to produce great results, the business itself cannot be deemed great" **[L2007-006]**. TJX has run the same model under three chief executives in thirty years; the current officers are all internal (Herrman joined 1989, Meyrowitz 1983; 10-K, executive officers). The advantage sits in a buying organization of 1,400 and 21,000 vendor relationships, the Mayo-Clinic case of **[L2007-006]**, not the surgeon. The draft also quotes the retail failing answer, "In retailing, to coast is to fail." **[L1995-008]**; TJX has not coasted (comps positive both years, margin up), so I read the row as the hazard Q5 must weigh, not as a fail here (see section 8).
3. *The money test* **[M2011-015]**. Disconfirming evidence first **[M1997-127]**: Ross's own 10-K says "There are limited economic barriers for others to enter the off-price retail sector" (ROST 10-K, accession 0000745732-26-000006), and Burlington's says "traditional, full-price retail chains ... have developed off-price concepts" (BURL 10-K, accession 0001193125-26-116001). Entry is easy; the question is whether the entrant gets the economics. **Same-metric comparison, pre-tax income over sales, fiscal years ended 2026-01-31:** TJX $7,299M / $60,372M = **12.1%**; Ross $2,842.2M / $22,750.6M = **12.5%**; Burlington $816.1M / $11,549.6M = **7.1%** (the three 10-Ks above). Second metric, capex over D&A: TJX 1.57, Ross 1.61, Burlington 2.54 (same filings). The scaled leaders earn about the same; the third-largest, with years of trying, earns a bit over half the margin and spends far more capital per dollar of depreciation. That is "Others may copy our model, but they will be unable to replicate our economics." **[L1999-006]**: entry is open, the economics are not.
4. *Low-cost position* **[L2007-004]**, **[M2018-043]**, **[M2004-091]**. The filing calls its structure low-cost and its policy is to pass the advantage to the customer every day, no promotions; the row: "if you can offer somebody a good product cheaper than the other guy then everybody practically has to buy it." **[M2024-013]**; and the goal "is not to widen our profit margin but rather to enlarge the price advantage we offer customers" **[L1996-016]**.
5. *Commodity check.* Two strong competitors can still be a terrible business **[M2013-052]**; here both earn 12% pre-tax on sales, so the field is not behaving like one. "one competitor is frequently enough to ruin a business" **[M2012-108]**: Ross has been that competitor for decades without ruining either.
6. *Brand against retailer* **[M2001-090]**: TJX is the retailer the brand's value moves to; the customer trusts TJ Maxx to have brands cheap. That is the right side of that row.
7. *Widening or narrowing* **[L2005-010]**: pre-tax margin 12.1% against 11.5% the year before; comp transactions up (10-K MD&A); in the 10-Q, margin 13.3% against 11.4% (inflated by tariff refunds of $331M; ex those, still up on "higher markon"). Not narrowing on the evidence read.
8. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: (a) brands cutting excess production or routing it to their own outlets, shrinking supply; (b) an online off-price model; (c) ultra-cheap direct-from-factory apparel. The filings show no sign of (a) (more vendors, not fewer); e-commerce has stayed at about 2% of sales through the period; (c) competes on price without the brands. Each is a change of degree, slow, and visible in comps and markon.

**Verdict: IN.** The castle stands on a low-cost position plus buying scale that competitors have been free to copy and have not matched on the same metric **[L1999-006]**, **[L2007-004]**, **[M2018-043]**; no test returned a castle shown open (OUT) or a future that cannot be judged (TOO HARD) **[M2000-019]**.

### Q3. HOW MUCH CAPITAL MUST GO IN? WEIGHING.

**Test 1, what it earns on the capital it needs** **[M2011-060]**, **[M2010-090]**. From the filed FY2026 balance sheet (accession 0000109198-26-000008): net property $8,220M + inventories $7,297M + receivables $602M + prepaid $1,065M, less payables $4,575M and accrued $5,891M = **$6,718M** of operating tangible capital, cash and leases excluded. Pre-tax income before net interest: $7,299M - $121M = $7,178M, about **107%** on that capital. Counting the operating lease right-of-use assets ($10,330M) as capital, about **42%**. The rows warn that a high return is checked for "a cyclical peak in earnings, a monopolistic position, or leverage" **[L1994-009]** and for equity shrunk by buybacks **[M1998-017]**; I measured on operating assets, not on equity, so the buybacks do not flatter it, and FY2026 includes a $419M net litigation gain (10-K MD&A) that is about 6% of pre-tax.
**Test 2, maintenance against growth** **[L1999-024]**, **[M2000-144]**. Capex $1,957M against D&A $1,247M; the filing splits it: new stores $185M, renovations $921M, offices and distribution centres $851M (10-K MD&A). Planned FY2027 capex $2.2 to $2.3 billion "to support growth". The excess over depreciation is mostly growth; renovations are close to maintenance.
**Test 3, the growth arithmetic** **[M1998-081]**, **[L2009-012]**. Base year chosen against **[L2005-003]**: from pre-COVID FY2020 to FY2026 net income rose from $3,272M (accession 0000109198-20-000004) to $5,494M, +$2,222M, while shareholders' equity rose from $5,948M to $10,190M, +$4,242M (same accessions): roughly fifty cents of added annual earnings per dollar of added book, with the larger part of earnings paid out (Q6).

**Verdict: WEIGHS FOR.** It is the "second-best business" of **[M1998-081]** at a very high rate, growing by stores and inventory that earn far more than they cost, with most of the cash free to return.

### Q4. DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion, otherwise WEIGHING.

- *Costs that are real.* Share-based compensation ($214M) is expensed in the income statement **[L2015-003]**, **[L2021-003]**; operating lease cost ($2,196M) sits in cost of sales (10-K Note L); depreciation is charged ($1,247M) and is the conservative end of the maintenance band **[R1996-023]**, **[M1998-127]**.
- *Tells* **[M1995-064]**. "prepaid expense, deferred asset accounts start building up suspiciously high, and inventories look out of line": prepaid and other current assets rose from $617M to $1,065M in FY2026 (10-K balance sheet). Looked at twice: the Q2 FY2027 10-Q explains the fall back to $730M as "the receipt of the credit card interchange fees settlement" (accession 0000109198-26-000048), consistent with the $470M gross settlement (the $419M net plus $51M legal costs, 10-K MD&A). Per-store inventories rose 10% against comps of 5% (10-K MD&A); the filing attributes inventory to opportunistic "packaway" buying and in-transit goods of $1.8B; in the 10-Q, inventories of $7,862M are up 6.6% on $7,372M a year earlier against sales up 5%. Not out of line.
- *Adjusted earnings* **[L2016-006]**. The proxy shows an "adjusted diluted EPS" of $4.73, which removes a **gain**, not a cost (DEF 14A, accession 0000109198-26-000015), and the incentive plans did not exclude the settlement gain or the costs. The direction is the conservative one.
- *Clear speech* **[M1994-018]**: the MD&A states the one-offs (litigation net benefit $0.14 a share; tariff refunds) in its own words.

**Verdict: WEIGHS FOR** (no confusion, no suspicion after the two tells were checked **[M1995-063]**); the earnings carried to Q7 are recast to remove the litigation gain and the tariff refunds.

### Q5. WHO RUNS IT? STOP on integrity, WEIGHING on ability.

- *Integrity, the STOP.* "If you’ve got doubts, forget it." **[M2013-088]**. The reading tests **[M1994-009]**, **[M2007-081]**: in the filings read I found no dishonest tell: the one-offs are disclosed and quantified, the "adjusted" figure lowers EPS, accounting estimates are explained (retail method, markdown policy "greatly reducing management's discretion", 10-K critical estimates). For a marketable stake the yardsticks and reading tests carry the weight **[M2007-081]**. **IN on integrity.**
- *Ability, the WEIGHING.* The record against the hand dealt **[M1994-008]**: through a period the draft itself calls hard for retailers **[L1995-008]**, pre-tax per share compounded about 9% (Q1), and the company ran margins equal to Ross and well above Burlington (Q2). The record is long, not a promise **[M1996-038]**, **[M2005-039]**. Retail is where ability weighs most, "Buying a retailer without good management is like buying the Eiffel Tower without an elevator." **[L1995-006]**; the weight falls for TJX, with internal succession across three CEOs.

**Verdict: IN on integrity; ability WEIGHS FOR.**

### Q6. WHAT WILL THEY DO WITH THE MONEY AND WITH THE OWNERS? WEIGHING.

**Part A, the money.**
- *Retention* **[M1998-033]**, **[R1995-009]**, **[M1998-110]**. Retained book of about $4.2B from FY2020 to FY2026 accompanied +$2.2B of annual net income (Q3), against a market value of $145.9B on $10.2B of book: the dollar retained has been worth far more than a dollar.
- *Buybacks* **[L1999-023]**, **[L2016-002]**, **[M2016-048]**, **[M2016-049]**. $2.5B a year for three years, planned at "$2.5 billion to $2.75 billion" for FY2027, timed on "excess cash flow, liquidity, economic and market conditions, our assessment of prospects" (10-K MD&A). No price is named above which purchases stop, the omission **[L2016-002]** calls puzzling; the Q4 FY2026 average was $154.09, above the bottom of the value range in Q7 below, so not "by a demonstrable margin" **[M2016-048]**. Shares issued under plans ($311M proceeds FY2026) are partly offset by the buybacks; diluted shares still fell from 1,453M (split-adjusted) in FY2014 to 1,128M in FY2026. **Weighs against**, mildly.
- *Deals.* No stock-paid acquisition; the all-stock STOP **[L2009-019]** does not arise; no serial issuance **[L2014-015]**. Equity-method stakes of $551M in FY2025 (cash).
- *Dividends* **[L2012-015]**: clear and consistent, $1.70 a share FY2026, planned $1.92.

**Part B, the pay, the board and the owners** (proxy, accession 0000109198-26-000015). CEO total $26.6M FY2026 (Summary Compensation Table). The annual plan pays on "MIP Incentive Pre-Tax Income", derived from total segment profit, a figure largely under the managers' control **[M2003-019]**; the PSUs pay on Incentive EPS growth with "planned share counts, which reflect the impact of anticipated buybacks" (so unplanned buybacks do not raise pay) and a downward ROIC modifier, a partial capital charge **[L1994-019]**. No stock options. Against: an "independent compensation consultant" sets the reference points **[M2004-016]**; directors' holdings are mostly deferred grant shares, not shares bought "with their savings" **[L2019-008]**; the company publishes forward expectations (dividend, buyback and capex plans; the MD&A opens "TJX provides projections") **[M2022-054]**. For: CEO and chair are separate, the chair a former CEO **[L2014-026]**; the CEO holds 466,759 shares (DEF 14A, beneficial ownership). "any compensation sins are generally of minor importance compared to the sin of having somebody that’s mediocre running a huge company" **[M2007-006]**.

**Verdict: WEIGHS FOR.** Retention passes plainly (the "test number one" of **[M1998-033]**); the price-blind buyback and the grant-based board weigh against but do not outweigh it **[M2007-006]**.

### Q7. WHAT IS IT WORTH? STOP.

Q1 to Q6 are IN or weighed, so the value may be reported.

**How much cash.** Owner earnings, recast per the draft's Q4-to-Q7 path (after all compensation **[L2021-003]**, depreciation as the floor of maintenance **[M1998-127]**, the year's one-offs out): `python tools/run.py TJX` gives (OCF - SBC) - maintenance capex, with maintenance between D&A and total capex: three-year mean **$4.3B to $5.1B**, FY2026 alone **$4.7B to $5.4B** (filing figures, Q0 cross-check). FY2026 includes the litigation net benefit of about $0.14 a share, about $0.16B (10-K MD&A). Range carried: **$4.3B to $5.4B** a year now.
**How sure.** High for the base: one interruption in twelve years, from a forced closure, and the cash stream rebuilt within a year (Q1). **How soon.** Now, growing with stores and comps; how fast is the judgment.
**The rate.** The long government rate, 5.63%, no risk premium added **[M1998-151]**, **[M2003-147]**; uncertainty goes into the cash estimate and the discount demanded **[M1997-126]**; no growth above the rate carried forever **[M1997-095]**.

**The range** (`_work_A2_TJX/q7_arith.txt`; growth rates are **CONVENTION**: no row supplies a growth figure, the draft asks inputs "reasonably conservatively" with the margin applied once at the end **[M2004-055]**, so three cases are set out and the spread is reported, not picked):

| Owner earnings now | 10 years at | then forever | Value | Per share |
|---|---|---|---|---|
| $4.3B | 4% | 2% | $143B | $130 |
| $5.0B | 6% | 2.5% | $221B | $200 |
| $5.4B | 8% | 3% | $325B | $296 |

At the price, the market assumes perpetual growth of about 1.9% to 2.6% at 5.63%, and the cash yield on the price is **2.9% to 3.7%**, below the bond's 5.63%.

**The verdict tests.**
- *Against the bottom boundary* **[L2013-012]**: the bottom of the range is about **$130** a share; the price is **$132.68**. The price is at the bottom, not below it.
- *Does it scream?* "it ought to just kind of scream at you" **[M1996-084]**; "if you really need a calculator [...] forget about the whole exercise" **[M2009-005]**. It needs a pencil to get anywhere: the margin exists only in the middle and upper cases, which rest on growth assumptions.
- *The floor.* "we are going to want to get a significantly higher return, obviously — in terms of cash produced relative to the amount we’re outlaying now for a business — than we are from a government bond" **[M2007-095]**: cash produced against the outlay is 2.9% to 3.7% against 5.63%. On the reading that counts growth in the expectancy, the answer depends on the conventions in the table; on the plain reading it fails.
- *Width* **[L2000-025]**: the range spans more than two to one; that alone is close to "no useful conclusion".

**Verdict: OUT.** "Valued, price below value, but the case is close: stop" and the price does not clear the floor on the plain reading **[M2009-005]**, **[M2007-095]**, **[M2003-149]**; in the rows' boxes, "out" **[M2006-013]**.

### Q8. IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the run).

## 4. Q9 and Q10

NOT REACHED.

### COMPUTATION — NOT A CLEARANCE
For the record only, the Q9 arithmetic from the FY2026 10-K (accession 0000109198-26-000008): senior notes $2,878M (next maturity $1,000M, 15 September 2026), cash $6,230M, operating lease liabilities $10,620M with a weighted remaining term of 6.6 years, no commercial paper outstanding, $1.5B of undrawn facilities; pre-tax income over interest expense $7,299M / $79M, about 92 times (the draft's coverage form, pre-tax over interest **[L2003-016]**). The one stress on record: in FY2021, with stores closed, TJX issued about $6.0B of long-term debt (XBRL ProceedsFromIssuanceOfLongTermDebt $5,987M, accession 0000109198-21-000006), the case of **[L2010-020]** in which a company that never needed credit had to reach for it. No clearance is drawn from this.

## 5. Q11 and Q12

**Q11:** not answered; the operator does not hold the name.

**Q12, the newspaper test.** TJX is not among the businesses the draft names (casinos, tobacco, loading schemes, gambling dressed as investing, promotion on a borrowed reputation), so the question is a WEIGHING. "if a story were written by an unfriendly but intelligent reporter" **[M2008-011]**: the exposure the filings themselves name is sourcing, "concerns about human rights, working conditions and other labor rights and conditions where merchandise is produced or materials are sourced" (10-K Item 1A), as for any apparel seller that does not control most of its makers; I found nothing in the filings read of a practice that is itself the story. "there’s something about every business that, if you knew it, you wouldn’t like" **[M2021-012]**. **Verdict: WEIGHS FOR**, weakly.

## 6. The box

**OUT, decided at Q7.** Value as a range in round numbers at 5.63%: about **$130 to $300 a share** ($145B to $325B), owner earnings $4.3B to $5.4B a year now, high certainty on the base, growth the open variable; **price $132.68 sits at the bottom of the range**, with a cash yield of about 3% to 3.7% under the bond's 5.63%. It is not so far below the value that it needs no pencil **[M1996-084]**, **[M2009-005]**.

## 7. Self-audit

- [x] **Every id resolves.** All ids in this file were checked against `principle_ledger_v5.csv` by script (all found); the quoted text was read from the ledger rows (`_work_A2_TJX/quotes_checked.txt`) and quotations are verbatim, with the rows' own dashes kept.
- [x] **Every filing fact has an accession**, stated in the line or in the filings table; XBRL trend figures carry the accession of the 10-K that filed them.
- [x] **No number without a row or a filing.** Ratios are arithmetic on filed figures; the growth rates in Q7 are labelled CONVENTION with their rationale.
- [x] **Files opened.** The protocol, the v5 purchase draft (read in full), `principle_ledger_v5.csv`, `tools/sources.py` (user-agent and helper names), the outputs of `tools/run.py` and `Screens/cover_shares.py`, SEC EDGAR. Disclosed: the harness loaded `CLAUDE.md`, `Framework/OPERATOR-PROTOCOL.md` and the user's memory index into context at session start (they carry no TJX verdict); `tools/run.py` printed v4 ledger ids and a v4 floor sentence, neither of which is used or cited here. No file under `Test Runs/`, `Screens/` (other than running `cover_shares.py`), `Framework/v4/`, `THE FRAMEWORK v4.md`, `principle_ledger.csv`, `PORTFOLIO.md` or another test session was opened.
- [x] **The order was kept.** Foundations, standing rule, Q1 to Q7 in order; Q7 returned OUT and closed the run; Q8 to Q10 NOT REACHED; the Q9 figures appear only under COMPUTATION — NOT A CLEARANCE; Q12 answered as instructed.
- [x] **No position is taken or recommended.**

## 8. What in the draft was wrong or unclear

The floor at Q7 is the instruction I could not apply cleanly: the draft says it "records the floor as the speakers' minimum expectancy, set against the long government rate and their next-best use of money, with no number of its own", but its strongest row for the floor, **[M2007-095]**, compares "cash produced relative to the amount we're outlaying now" with the bond, and for a growing business with a 3% cash yield against a 5.63% bond those two readings (cash now against expectancy over the years) give opposite answers; the draft does not say which governs, and it gives no rule for the growth input at all beyond the caps **[M1997-095]**, **[M1999-067]** and "reasonably conservatively" **[M2004-055]**, so the width of the range (here more than two to one) and therefore the box are set by conventions two analysts will not share. I applied both readings and decided on the screamer test **[M2009-005]**, which fails under either. Three smaller points: the draft quotes **[L2013-012]** ("a reasonable price in relation to the bottom boundary") beside the screamer rows without saying which wins at the boundary; Q2 test 2 lists "In retailing, to coast is to fail." **[L1995-008]** as its failing answer, which read literally fails every retailer at a STOP, while Q5 weighs retail management as ability **[L1995-006]**, so I applied the superstar form **[L2007-006]**; and the protocol closes the run at the first failed STOP but the brief asks for Q12, so I answered Q12 as a filter on how the money is made, which carries no value. Also noted: `tools/run.py` still prints the v4 ten-percent floor and v4 ids, which the v5 draft does not carry.
