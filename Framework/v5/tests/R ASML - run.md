# R ASML - run (regression, v5 drafts)

**ASML Holding N.V.** (Nasdaq ADR: ASML; one ADR equals one ordinary share). CIK 0000937966. Foreign private issuer, Form 20-F and 6-K.
Run date 2026-10-04. Purchase questions under `Framework/v5/DRAFT - THE FRAMEWORK v5.md`; Q11 under `Framework/v5/DRAFT - THE HOLDINGS FRAMEWORK v5.md` (the operator sold this name on 2026-08-28; Q11 is answered as it would have been for a holder). Every id is from `principle_ledger_v5.csv`. This run binds nothing and changes no verdict of record. No position is taken or recommended.

**Documents read (all SEC EDGAR):**

| Doc | Filed | Accession | Used for |
|---|---|---|---|
| Form 20-F, FY2025 (`asml-20251231.htm`) | 2026-02-25 | 0001628280-26-011378 | statements, cover count, risk factors, competition, customers, export controls, remuneration report, buybacks, debt |
| Form 6-K, Q2 2026 results (Ex. 99.1 press release) | 2026-07-15 | 0001628280-26-048235 | Q1 and Q2 2026 net income, 2026 outlook, buyback and dividend |
| Form 6-K, Q4 2025 results (press release) | 2026-01-28 | 0001628280-26-003701 | Q4 2025 bookings, year-end backlog |
| Form 6-K, Q2 2025 results (press release) | 2025-07-16 | 0001628280-25-034992 | Q1 and Q2 2025 net income (for the trailing twelve months) |
| SEC XBRL companyfacts, CIK 0000937966 | as fetched 2026-10-04 | (each year's 20-F) | 2009 to 2022 series, transcription only |

Cross-check (operator rule 4): XBRL `NetIncomeLoss` FY2025 = €9,609.4m; the filed Consolidated statements of operations in the 20-F (0001628280-26-011378) show net income €9,609.4m. Also FY2025 operating cash flow €12,658.5m in both. The submissions feed shows no filing between the 6-K of 2026-07-15 and 2026-10-04 (the next is not yet filed), so the filed facts were the same on 2026-08-28, the sale date, as on the run date.

---

## 0. Step 0

| Item | Value | Source |
|---|---|---|
| Price | **$1,867.31**, close 2026-10-02 | aggregator, as supplied by the parent session; **flagged: aggregator, live quote only** |
| FX | **1.1225 USD per EUR**, ECB euro foreign exchange reference rate, 2026-10-02 (series EXR.D.USD.EUR.SP00.A) | ECB data portal, fetched 2026-10-04 |
| Price in earnings currency | 1,867.31 / 1.1225 = **€1,663.53** per share | arithmetic |
| Shares, by class | **385,417,665 ordinary shares** (€0.09 nominal), "issued and outstanding at December 31, 2025"; one class of ordinary share; the Nasdaq ADR is one share | 20-F cover and balance sheet, filed 2026-02-25, 0001628280-26-011378 (`Screens/cover_shares.py ASML` prints the same count and accession) |
| Market cap | 385,417,665 x €1,663.53 = **€641.2bn** (the 2026 buybacks have reduced the count since the cover date; the 6-K of 2026-07-15 does not state a share count in text, so the cover count is used as directed) | arithmetic |
| Sovereign, earnings currency EUR | **3.835%**, euro area AAA 30-year spot yield, 2026-10-01, ECB series YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y (3.8350007105 as fetched) | ECB, the issuing authority for the series, fetched 2026-10-04 |
| `tools/run.py ASML` | refused: "CURRENCY MISMATCH: earnings in EUR, quote in USD. Refusing to convert." It printed the USD Treasury yield, which is the wrong sovereign for this name and is not used | tool output, ignored as instructed |

---

## 1. The foundations

The foundation that bears hardest here is the analyst's habits. The operator owned this name and sold it, so the session reads with "the worst anchoring effect, which is always your previous conclusion" in view **[M2016-054]**; the verdict of record was not opened, and the contrary case is stated at Q1 before the verdict is given **[M2016-055]**. Second, who is paid to tell you: the most quoted forward numbers for this company are its own (the 2024 Investor Day 2030 scenarios and the quarterly outlook), and the rows do not consult projections **[M1995-050]**, **[M2003-065]**. Third, macro kept out: export controls are a government's choice, not a macro forecast, and are read here only as a property of the business **[M2000-094]**, **[M2015-016]**. A share is a business **[M1997-109]**, and the market's price is a servant **[M2006-077]**; at about 60 times trailing earnings (Step 0 and Q11) the margin-of-safety attitude **[M1996-084]** is the one most at risk of being read from the quote. The index fork is passed: the run proceeds as the professional's questions **[M2008-055]**.

## 2. The standing rule

No position is taken, so no buyer's financing exists; owned unlevered, a listed share cannot call the owner, and the rule is met so long as nothing is borrowed against it and the owner is prepared to see it "go down 50 percent — or more" **[M2020-022]**, **[L2014-005]**, **[M2006-079]**.

---

## 3. Q1 to Q8

### Q1. CAN I UNDERSTAND IT? STOP.

**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**; the product may stay opaque if the economics are clear **[M2011-014]**. Twelve tests; the ones that bear are 2, 5, 6, 7, 8 and 9. Fast-moving technology goes to TOO HARD, not OUT **[L1993-023]**, **[M1998-008]**, **[M2000-038]**.

**The filing facts.**
- What it sells. Total net sales 2025 €32,667.3m: net system sales €24,474.3m and "Net service and field option sales" (installed base) €8,193.0m, 25.1% of the total. EUV systems (NXE €10,445.8m plus EXE €1,156.9m) are 47.4% of system sales. 20-F, Consolidated statements of operations and Note 2, 0001628280-26-011378.
- Its position. "ASML is currently the world’s only manufacturer of EUV lithography systems." In DUV, "We compete primarily with Canon and Nikon". 20-F, Our products and services; Risk factors, "We face intense competition", 0001628280-26-011378.
- Customers. "In 2025, four customers each individually exceeded 10% of total net sales, totaling €20.0 billion, or 61.2%"; the largest customer was 23.9% of 2025 sales against 16.6% in 2024. 20-F, Note 3 and Risk factors, 0001628280-26-011378.
- What the future turns on, in the company's own words: "Our future success depends on our ability to respond in a timely manner to commercial and technological developments in the semiconductor industry"; "if customers choose not to adopt our innovations or shift toward architectures that rely less on lithography, our competitive position may weaken"; "the success of our EUV 0.55 NA (High NA) technology [...] depends on continued technical progress by both us and our suppliers"; "the cost and time required to develop new products and technologies continue to rise". R&D €4,698.8m in 2025, 14.4% of sales. 20-F, Risk factors (Strategic) and statements of operations, 0001628280-26-011378.
- Governments as a variable. "Customers in China represented 29.1% of our 2025 total net sales and 36.1% of our 2024 net sales"; Taiwan "25.5% of our 2025 total net sales and 15.4% of our 2024"; export licenses are required "for EUV systems, specific DUV immersion systems", and "we do not control the licensing process or approval criteria". Three new export-control measures in 2025 (Netherlands, 15 January; US Affiliates Rule, 1 October, suspended to 10 November 2026; EU, November). 20-F, Risk factors and Global geopolitics, 0001628280-26-011378.
- One supplier. Carl Zeiss SMT is "our sole supplier of lenses, mirrors, illuminators, collectors and other critical optical components"; if it stopped, "we would effectively cease to be able to conduct our business." 20-F, Risk factors, 0001628280-26-011378.
- How far off the insiders' own view has been. The 2024 Investor Day put 2030 revenue at "between approximately €44 billion and €60 billion" (20-F, 0001628280-26-011378); the July 2026 outlook expects 2026 sales "between €43 billion and €45 billion" (6-K 2026-07-15, 0001628280-26-048235). The low end of the six-year range is being reached in year two.
- The record. Net income €1,471.9m (2016) to €9,609.4m (2025), with falls in 2012, 2013, 2022 and 2024 (XBRL series; 2023 to 2025 cross-checked to the 20-F).

**The other side, stated first** **[M2016-055]**. The case for IN is real. The economics are those of a sole supplier to a few customers who have no second source for EUV; a quarter of sales is service on an installed base that grows with every system shipped; the record of earning power over ten years is strong. Test 6 is passed: the winner can be named, not just the industry **[M2012-067]**. And the rows hold one case of a technology company entered on the record of people who had done the near impossible **[M2010-095]**.

**The verdict.** It does not carry Q1. Test 2 asks for the key variables and how predictable they are **[M1998-044]**; here they are (a) whether lithography intensity holds against "architectures that rely less on lithography" and "alternative technological solutions", (b) whether High NA succeeds on its own and its suppliers' technical progress, (c) what three governments license, and (d) the customers' capital cycle. None of the four is predictable from where the analyst stands, and two are not knowable by anyone: "If something’s important but unknowable, forget it." **[M2006-076]**. Test 7, customers or technology: the forecast is about technology, and the customers' behaviour is itself driven by technology roadmaps; this is the IBM-customer side of **[M2017-019]**, not the consumer side. Test 8, how far off could I be **[M2011-084]**: the company's own 2030 range was overtaken in two years, which is a measure of the width, not a reassurance. Test 5: the insiders did write it down, as a range of €44bn to €60bn, and the rows do not take an insider's projection as understanding **[M2000-105]**, **[M1995-050]**. The row that decides it is stated as the first filter: "if something comes in where there’s a technological component that’s of significance, or where we think the future technology could hurt the business as it presently exists [...] it won’t make it through the filter." **[M1998-008]**. And the perimeter is drawn conservatively: "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**. Study does not cure it **[L1993-023]**, **[L1999-018]**, and a low or high price does not reopen it **[M2000-038]**.

**Q1: TOO HARD.** The economics ten years out turn on technology, licensing and customer capital cycles that cannot be foreseen from the filings **[M1998-008]**, **[L1993-023]**, **[M2006-076]**; this is "too hard", not OUT, and "It doesn’t mean it isn’t a good buy" **[M2000-038]**, **[M2006-013]**. The run closes here.

### Q2 to Q8. NOT REACHED.

The first STOP returned TOO HARD. Q2, Q3, Q4, Q5, Q6, Q7 and Q8 are not answered. The competitive facts gathered for Q2 (sole EUV maker; Canon and Nikon in DUV; Zeiss sole optics supplier; the export-control record) are recorded above as Q1's filing facts only.

### COMPUTATION — NOT A CLEARANCE

Shown for the record only; it clears nothing and carries no entry language.

| Item (FY2025 unless stated) | Figure | Source |
|---|---|---|
| Net income | €9,609.4m | 20-F, 0001628280-26-011378 |
| Trailing twelve months to Q2 2026 net income | 9,609.4 − (2,355 + 2,290) + (2,757 + 2,918) = €10,639.4m | 6-K 0001628280-25-034992; 6-K 0001628280-26-048235 |
| Depreciation and amortization | €1,025.9m | 20-F cash flow |
| Purchase of PP&E plus intangibles | €1,573.6m + €57.6m = €1,631.2m (above depreciation) | 20-F cash flow |
| Share-based compensation (already expensed in net income) | €202.3m | 20-F cash flow |
| Net income + D&A − capex (a stated guess at what the owner can take out, not a value) | €9,004.1m | arithmetic |
| Tangible equity (equity 19,612.2 − goodwill 4,588.6 − other intangibles 540.1) | €14,483.5m; net income on it 66% (flattered by €19.4bn of customer down payments carried as contract liabilities) | 20-F balance sheet |
| Debt (long-term 2,709.0 + short-term and current 1,681.9) against cash and short-term investments (12,916.0 + 405.9) | €4,390.9m against €13,321.9m | 20-F balance sheet |
| Price to trailing earnings | €641.2bn / €10,639.4m = about 60 times; earnings yield about 1.66% against the 3.835% sovereign | arithmetic |

No value range is stated, because Q1 did not return IN and the draft forbids a value before Q1 to Q6 are IN or weighed.

---

## 4. Q9 and Q10

NOT REACHED (the run closed at Q1).

---

## 5. Q11 and Q12

### Q11. Under the holdings draft, as it would have been for a holder

The filed facts on 2026-08-28 (the sale date) were those of the 6-K of 2026-07-15; nothing was filed between then and 2026-10-04. The price used is the run's price of 2026-10-02; the price on the sale date was not looked up. Default first: "when in doubt, keep holding. But it’s no inviolable rule." **[M2009-040]**. The owner cannot be forced to sell if he holds without borrowed money **[M2020-007]**, **[M2020-022]**; assumed so.

**Holdings Q1. What has moved, the business or only its price? (STOP against selling on price alone; WEIGHING on a silly price.)** Both moved. The business: 2025 sales +15.6% and net income +26.9% (20-F, 0001628280-26-011378); first-half 2026 net income €5,675m against €4,645m a year earlier, and 2026 sales guided to €43bn to €45bn against €32.7bn (6-K 0001628280-26-048235). The price moved more: $1,069.86 at 31 December 2025 (the Nasdaq close the 20-F's remuneration report uses, 0001628280-26-011378) to $1,867.31, up 74.5%. The rise alone is no reason to sell **[M2018-014]**, **[L1996-025]**. The silly-price weighing: about 60 times trailing and 67 times 2025 earnings sits inside the band of the two remarks the rows carry, "60 or 70 times earnings, keep an eye on me" **[M1996-095]** and "50 times earnings, it was a silly price" **[M2006-029]**, and the draft writes no threshold. **WEIGHS AGAINST holding, weakly:** the price is in the range the speakers called silly in two cases, but "probably" **[M2007-089]** and the rows' own record run both ways **[M1998-101]**.

**Holdings Q2. Has the castle changed? (WEIGHING, action at the life-threatening grade.)** No filing fact shows the moat narrower: still "the world’s only manufacturer of EUV lithography systems" (20-F); Q4 2025 net bookings €13.2bn and year-end backlog €38.8bn (6-K 0001628280-26-003701); low-NA EUV capacity of about 65 in 2026 planned up 30% for 2027 (6-K 0001628280-26-048235). The threats graded **[M2016-081]**: export controls (China down from 36.1% to 29.1% of sales; three new measures in 2025) and state-backed "new competitors [...] driven by the ambition of self-sufficiency" are major, not life-threatening on the filed facts; the Zeiss single source and Taiwan at 25.5% of sales are standing exposures, not changes. Industry change is the form the rows sell on **[M2016-008]**; none is filed. **WEIGHS FOR holding:** the castle is not shown to have narrowed, and a major threat can be held through **[M2014-048]**, though "slow change can be much harder to perceive" **[M2014-038]**.

**Holdings Q3. Has the management changed, or changed after being paid? (WEIGHING on ability; prompt action pressed on trust.)** The chief executive changed on 24 April 2024 (Fouquet in; Wennink and van den Brink retired), 20-F remuneration report. Nothing filed suggests a breach of trust **[L2022-001]**, **[L2023-003]**. Pay reads well against Q6 Part B of the purchase draft: CEO total €7.0m, "CEO vs. average per FTE" 46:1, 2025 pay "below the median level of the reference group"; LTI 2026-2028 weights a three-year return on average invested capital at 35% with target 55% (a capital charge in the pay, **[L1994-019]**); a two-year holding period after vesting and an ownership guideline of four times base salary, met; a clawback policy; the remuneration chair's own words, "we do not want to contribute to the escalation that can happen when everyone takes part in a race to the top" (20-F, 0001628280-26-011378). Against: a peer reference group used to set pay **[M2012-095]**, and relative TSR at 25% of the LTI, a measure partly outside management's control **[M2003-019]**. **WEIGHS FOR holding:** no change in trust found, and the pay is tied in large part to what the managers control.

**Holdings Q4. Is the money kept still becoming more than a dollar? (WEIGHING; STOP on further money into a business that chews it up.)** Over 2021 to 2025 net income was €36,527.4m, dividends paid €11,279.6m, buybacks €20,650.0m (XBRL series; 2023 to 2025 per the 20-F cash flow statement). Earnings rose from €3,553.7m (2020) to €9,609.4m (2025), €6,055.7m a year more on €25,247.8m kept after dividends, before buybacks: progress commensurate with the capital retained, and more **[M2011-072]**, **[R1995-009]**. Buybacks: €5,950.0m in 2025 at an average of about €715 a share (20-F purchase table), and a new programme "up to €12 billion" to 2028 that names no price above which buying stops **[L2016-002]**; whether the buying is below value **[L2011-003]** cannot be read from the filings. One use outside the core: "We have invested €1.3 billion in Mistral AI as lead investor" (20-F), against the rows' warning on redeploying into unrelated activities **[L2014-016]** and the order of uses **[L2012-011]**. The STOP is not triggered: the business throws off cash (operating cash flow €12,658.5m) and does not chew it up **[L2023-010]**. **WEIGHS FOR holding,** with the price-blind buyback and the Mistral stake noted against.

**Holdings Q5. Is there a plainly better use for this money? (WEIGHING, marketable holdings.)** The run may not open the operator's other holdings, so "the least attractive thing I hold" **[M2007-104]** cannot be named. The sovereign at 3.835% against an earnings yield of about 1.66% is a comparison the purchase draft makes at Q8; the holdings draft asks for "something you like immensely better" **[M1998-013]**. **UNDECIDED:** the alternatives are outside what this run may read.

**Holdings Q6. Was it a mistake to buy, now recognised? (WEIGHING on the finding; once found, action whole and prompt.)** Under the v5 purchase draft, Q1 returns TOO HARD: the holding rests on an understanding the draft says the analyst does not have. That is a misjudgment at entry, not a change in the world, which is the line the holdings draft draws **[M2012-031]**, **[M2016-065]**; and it is the case the rows fear most, "if I think I understand a business and I don’t" **[M1997-024]**. Against the finding: the business did what the owner hoped; a good result does not prove a sound decision any more than a bad one proves a poor one **[M2020-017]**. **WEIGHS AGAINST holding:** if the finding is accepted, the rows press action "whole" **[M2020-020]** and prompt **[L2008-003]**; the holdings draft does not say whether a purchase-side TOO HARD on a name already held is such a finding (see section 8).

**The six together.** For holding: Q2, Q3, Q4. Against: Q1 (weakly, the price) and Q6 (the circle). Undecided: Q5. The holdings draft gives no named outcome (its section VI, item 2), so none is written. The holdings questions taken alone, under "when in doubt, keep holding" **[M2009-040]**, would keep it; what presses a sale is the purchase draft's Q1 entering through holdings Q6, together with a price in the range the speakers twice called silly.

### Q12. Would we be proud of how the money is made? (STOP for named businesses, otherwise WEIGHING.)

ASML makes and services lithography equipment for chipmakers. It is none of the named businesses: casinos **[M2007-018]**, tobacco **[M2005-097]**, loading schemes **[M2013-015]**, gambling dressed as investing **[M2021-059]**. The newspaper test **[M2008-011]**: the filings disclose the export-control regime and the licensing it requires, and the Speak Up policy protects reporters of suspected violations "even if we could lose business as a result" (20-F, 0001628280-26-011378); the rows count declining legal business as part of the test **[M2010-007]**. **WEIGHS FOR:** no fact found that would trouble the unfriendly reporter; the export-control exposure is a business risk, not a moral one, on the filed record.

---

## 6. The box

**TOO HARD, decided at Q1** (fast-moving technology, government licensing and customer capital cycles put the economics ten years out beyond a reasonable fix) **[M1998-008]**, **[L1993-023]**, **[M2006-013]**. Q7 not reached; no value range is stated. For the record only: price $1,867.31 = €1,663.53, about 60 times trailing earnings, earnings yield about 1.66% against the 3.835% euro AAA 30-year rate.

---

## 7. Self-audit

- [x] **Every id resolves.** All bold ids in this file were checked against `principle_ledger_v5.csv` by script on 2026-10-04 (68 distinct ids, none missing), and fifteen quoted fragments were matched against their rows' text.
- [x] **Every filing fact has an accession.** 20-F 0001628280-26-011378; 6-Ks 0001628280-26-048235, 0001628280-26-003701, 0001628280-25-034992; the 2009 to 2022 series are XBRL transcription, cross-checked for 2023 to 2025 against the filed statements.
- [x] **No number without a row or a filing.** Every number is a filing figure, an ECB figure, the supplied price (flagged), or arithmetic on these. No CONVENTION number used. No threshold of the analyst's own: the 60 and 70 and 50 times figures are quoted remarks **[M1996-095]**, **[M2006-029]**, not a rule.
- [x] **No file outside the whitelist was opened.** Opened: the protocol, the purchase draft, the holdings draft, `principle_ledger_v5.csv`, `tools/run.py` and `tools/sources.py` (run and grepped for the SEC helpers), `Screens/cover_shares.py` (run only), SEC EDGAR, the ECB data portal, and this file and its work folder. Not opened: `THE FRAMEWORK v4.md`, `THE HOLDINGS FRAMEWORK.md`, `principle_ledger.csv`, any run file or screen, `PORTFOLIO.md`, other test files. The `run.py` output's USD sovereign was discarded.
- [x] **Order kept; the first STOP stopped the run.** Q1 TOO HARD; Q2 to Q10 NOT REACHED; arithmetic shown only under COMPUTATION — NOT A CLEARANCE; Q11 and Q12 answered as the parent instructed.
- [x] No em dashes in the run's own prose (quoted rows and filings keep theirs; the required heading keeps its own).

---

## 8. What in the draft was wrong or unclear

Three things. First, **where a technology business is stopped, and in which box.** Q1 lists "Businesses that live on continued invention" **[M1999-075]** under "What it rules OUT", but two paragraphs later sends "fast-moving technology and businesses that change" to TOO HARD, "never OUT on the business", and the reconciliation note says rapid change is "owned by Q2" while Q1 "points to it"; ASML is all three at once (it lives on continued invention, its technology moves fast, and the change is the castle question). I stopped at Q1 in TOO HARD because **[M1998-008]** is stated as the first filter and Q1's tests 2, 7 and 8 apply directly, but another analyst could as defensibly pass Q1 on the economics (a named winner, test 6) and stop at Q2 in TOO HARD, or read **[M1999-075]** and write OUT; the draft should say which list governs a business that fits both. Second, **the holdings draft does not say what a purchase-side verdict means for a name already held.** When the purchase draft returns TOO HARD at Q1 on a holding, it is unclear whether holdings Q6 ("a mistake to buy, now recognised") must take that as the finding, which would press a whole and prompt sale, or whether the holdings questions stand on their own (Q2 to Q4 here weigh for keeping); I recorded Q6 as weighing against and said the draft is silent. Third, **Q11's "silly price" has no instrument and Q5 cannot be answered blind:** the draft rightly writes no multiple, but it also gives no way to weigh a price at 60 times trailing earnings against "probably" **[M2007-089]**, and holdings Q5 asks for the least attractive thing held, which a regression run that may not open the portfolio cannot know; I quoted the two remarks and marked Q5 UNDECIDED.
