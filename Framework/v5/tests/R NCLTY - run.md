# R NCLTY - run. Nitori Holdings Co., Ltd. (TSE 9843; unsponsored ADR NCLTY, 1 ADR = 1 share). Regression run under the v5 drafts, 2026-10-04.

Binds nothing; changes no verdict of record. Run under `Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`. Sources opened: the two v5 drafts, `principle_ledger_v5.csv`, the securities reports and fact books in `Test Runs/_research 2026-09-18 NCLTY/` folders `txt/` and `fbtxt/` (PDFs in `docs/` and `fb/` not needed: the text extracts carry the page markers of the filed documents), and nitorihd.co.jp (monthly domestic sales pages, saved to `Framework/v5/tests/_work_R_NCLTY/`). Nothing else under `Test Runs/` was opened.

**Document key.** SR = 有価証券報告書 (annual securities report), Nitori Holdings, EDINET filer code E03144. SR FY3/26 = 第54期 (2025-04-01 to 2026-03-31), filed 2026-06-24, IFRS. SR FY3/25 = 第53期, filed 2025-06-25 (first IFRS year). SR FY3/24 = 第52期, filed 2024-06-21. SR FY3/23 = 第51期 (13 months 11 days, 2022-02-21 to 2023-03-31, fiscal year end changed), filed 2023-06-23. SR FY2/22 = 第50期, filed 2022-05-20. SR FY2/21 = 第49期, filed 2021-05-14. SR FY2/20 = 第48期, filed 2020-05-15. SR FY2/19 = 第47期, filed 2019-05-17. FB = company Fact Book for the fiscal year named. MONTHLY = nitorihd.co.jp/ir/performance/sales_YYYY.html, "株式会社ニトリ月次国内売上高前年比推移", fetched 2026-10-04. **Accession:** the EDINET document ID (S100xxxx) does not appear in the extracted text of any report and was not fetched; each filing is identified instead by filer code, period, filing date and page ("p. n/172" is the filed page footer). This is a gap against the protocol's accession requirement, recorded in section 8.

---

## 0. Step 0

| Item | Value | Source |
|---|---|---|
| Price | ¥3,009, TSE close 2026-10-02; ADR $9.73 same day | aggregator, FLAGGED (supplied by the parent session; not re-fetched) |
| Shares issued | 572,217,480 common, one class | SR FY3/26 p.33, 発行済株式 (at 2026-03-31 and at filing 2026-06-24) |
| Treasury | 5,223,437 own name (5,223,400 + 37 odd-lot); 1,936,805 in the J-ESOP trust (1,936,800 + 5), treated as treasury under IFRS | SR FY3/26 p.35, 議決権の状況 notes 2-3 and 自己株式等 |
| Shares outstanding | 572,217,480 - 5,223,437 - 1,936,805 = **565,057,238** | arithmetic; cross-check: equity attributable ¥988,559m / ¥1,749.49 per share (SR FY3/26 p.2) = 565.05m |
| Split | 1-for-5 effective 2025-10-01 (+457,773,984 shares) | SR FY3/26 p.33 |
| Market cap | ¥3,009 x 565,057,238 = **¥1,700.3bn** | arithmetic |
| Sovereign | JGB 30-year 4.122%, 2026-10-01, Japan Ministry of Finance (jgbcme), earnings currency JPY | supplied by the parent session as issuing authority; not re-fetched here |
| Cross-check of one figure | Revenue FY3/26 ¥912,248m: SR FY3/26 p.2 (主要な経営指標) = FB FY3/26 p.2 (01. 連結累計損益実績) | matches |

`tools/run.py` handles SEC filers only; all arithmetic below is done by hand from the SR and FB lines cited, in yen millions unless stated, and shown in full.

---

## 1. The foundations

The foundation that bears hardest is **a share is a business** **[M1997-109]**: the quote fell from about ¥2,365bn at FYE Feb 2021 (P/E 25.67 x net income ¥92,114m, SR FY2/21 p.2) to ¥1,700bn today, and the run asks what happened to the business, never when the price will move **[M1994-038]**. **The market serves, it does not instruct** **[M2006-077]**: the fall tells nothing by itself. **No macro forecast enters** **[M2000-094]**: the yen matters here only as a property of this business's cost base (about 90% of goods are private-label imports, SR FY3/26 p.22), not as a forecast of the yen. **Who is paid to tell you**: the company's own long vision (¥3 trillion sales, 3,000 stores by 2032, SR FY2/22 p.9) is a seller's projection and is not consulted **[M1995-050]**, **[M2011-083]**. **The analyst's habits** bind with extra force because the operator holds the name: the holder wants the holding to be right, so contrary evidence is written down at once **[M1997-127]** and the previous conclusion is treated as the worst anchor **[M2016-054]**; the run looks for "what’s wrong" and "what you’re missing" **[M2025-013]**.

## 2. The standing rule

Owning this does not put the buyer at risk of ruin provided it is not held on borrowed money: "you don’t want to put yourself in a position where you have to sell" **[M2020-007]**, **[M2020-022]**, **[L2014-005]**. The operator's financing of the position is not visible to this run (PORTFOLIO.md is off the whitelist); recorded as a condition, not a finding.

---

## 3. Q1 to Q8

### Q1 - CAN I UNDERSTAND IT? STOP. **Verdict: IN (narrowly).**

The test: "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; "I understand the economic dynamics of the industry" **[M2011-014]**; is the forecast about customers or technology **[M2017-019]**.

Applied. The economics can be stated from the filings in a few lines. Nitori designs about 90% of what it sells as private label, makes or sources it in Asia (own factories in Vietnam; procurement and logistics companies in China), imports it and sells it through its own stores and EC in Japan ("製造物流IT小売業", SR FY3/26 p.9; "商品の約90％をプライベートブランドとして開発輸入", p.22). Revenue FY3/26 ¥912,248m, operating profit ¥125,526m (13.8%), net income attributable ¥89,270m (SR FY3/26 p.2, p.25). The key variables **[M1998-044]**: existing-store customer count and ticket (MONTHLY), store count (1,069 at 2026-03-31, SR FY3/26 p.27), gross margin, which moves with the dollar cost of imports (risk ①, SR FY3/26 p.22), and personnel and logistics cost. It is a consumer business, not a technology one **[M2017-019]**; no financial-institution question arises.

Two cautions, carried forward rather than settled here. First, test 3, "do the past statements tell me the future ones?" **[M2008-033]**: the record to FY2/21 (34 consecutive years of rising sales and ordinary profit, SR FY2/21 p.14 line "34期連続増収増益") did not foretell FY2/22 to FY3/26, in which net income ran ¥96.7bn, ¥95.1bn (13 months), ¥86.5bn, ¥82.5bn (IFRS), ¥89.3bn (SR FY3/26 p.2-3). Second, the draft's own narrated example is retail: "it’s easy to sort of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**. I hold the economics understood (the dynamics of an import-based, private-label, low-price home-goods chain in a shrinking market are legible from the reports, **[M2011-014]**); whether the competitive position holds is Q2's question, which the draft assigns there **[M1997-148]**. A reader applying "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]** could return TOO HARD here; I record IN narrowly and pass to Q2.

### Q2 - WHY IS THE CASTLE STILL STANDING? STOP. **Verdict: OUT.**

The question: "why is that castle still standing? And what’s going to keep it standing [...] five, 10, 20 years from now" **[M1995-038]**. The tests applied:

**Test 4, pricing power** **[M2005-020]**, **[M2005-019]**. The monthly series (MONTHLY, existing stores, Nitori Co. domestic, EC included, year-on-year):

| Fiscal year | Existing-store sales | Customers | Ticket |
|---|---|---|---|
| FY2/21 | 110.4 | 112.8 | 97.9 |
| FY2/22 | 90.9 | 90.1 | 100.8 |
| FY3/23 | 101.2 | 94.4 | 107.2 |
| FY3/24 | 102.9 | 98.7 | 104.2 |
| FY3/25 | 100.2 | 100.9 | 99.3 |
| FY3/26 | 95.8 | 92.8 | 103.2 |
| FY3/27, Apr to Sep | 100.0 | 100.7 | 99.3 |

Chained (arithmetic, product of the yearly figures): FY3/23 to FY3/26, ticket x1.145, customers x0.872, existing-store sales x1.000. Over four years the ticket rose 14.5%, the customer count fell 12.8%, and existing-store sales did not grow at all. In the earlier stretch FY2/13 to FY2/20 the same chain gives customers x1.100, ticket x1.138, sales x1.256: volume and price rose together. The filing's own reading of FY3/26: "国内既存店の客数が前期比92.8%となり、売上が前期比95.8%となりました。足元における客数の減少は、デザインや機能、価格競争力に優れた新たな商品の開発が十分に進まず [...] お客様の期待に応えられなかったことが要因" (SR FY3/26 p.25), and the first priority for the coming year is "①安さの実現", because "消費者の節約志向・低価格指向に充分にお応えできていない" (SR FY3/26 p.10). Between the price rises the company ran markdowns to hold sales: permanent cuts on 1,389 + 520 items (SR FY2/22 p.16), time-limited markdowns of up to 2,200 items (SR FY3/25 p.29). This is the draft's failing answer: price past the moat "and the moat is shown to be smaller than thought" **[M2001-087]**, and the prayer session before a price rise **[M2005-020]**. A strong position "manage[s] to pass through increases in raw material costs" **[M2005-017]**; here the yen-driven cost rise (SR FY3/23 p.21 "急激な円安の進行や原油高に起因する輸入コストの上昇") was passed through at the cost of one customer in eight.

**Test 8, would the customer still choose it over the low bid?** **[M2017-009]**. The company says, in its own words, that the customer it lost is a price-led customer it was not cheap enough for (SR FY3/26 p.10, above). "most insureds don't care from whom they buy" **[L2004-003]** is the draft's failing form; the filing describes the same indifference. **Fails.**

**Test 5, unit volume** **[M1999-054]**. The unit here is the customer. Existing-store customers chained FY2/22 to FY3/26: x0.786, a fall of about 21%; FY2/13 to FY2/21: x1.241. Volume decline alone is not a fail **[M2015-066]**, but it is not explained by a one-off year: four of the five years are below 100. **Weighs against.**

**Test 10, widening or narrowing?** **[M1999-108]**, **[L2005-010]**. Operating margin 16.6% (FY2/19), 16.7% (FY2/20), 19.2% (FY2/21), 17.0% (FY2/22), 14.8% (FY3/23), 14.3% (FY3/24), 12.7% IFRS (FY3/25), 13.8% IFRS (FY3/26) (FB FY2/21 p.2, FB FY2/22 p.2, FB FY3/23 p.2, FB FY3/24 p.2, FB FY3/26 p.2). Return on equity 14.5% to 16.6% in FY2/15 to FY2/21 (SR FY2/19 p.2, SR FY2/21 p.2) against 9.5% and 9.4% in FY3/25 and FY3/26 (SR FY3/26 p.2, IFRS). The notch is lost, and lost on the customer side **[L1995-023]**. **Narrowing.**

**Test 6, the low-cost position, and the commodity exception** **[L2004-007]**, **[L2000-017]**, **[M2001-013]**. This is the one route by which a price-led business keeps a castle, and it is the test the run cannot close in Nitori's favour. The company states its aim as "どこよりも安い価格" (SR FY3/26 p.22, risk ②) and states in the same report that its price competitiveness has fallen short (p.10, p.25); the report also names "業種・業態の垣根を越えた販売競争の激化" (p.25). The cost is to be "measured against the competitor, not in absolute terms" **[M2001-013]**, and no peer filing lies within the whitelisted folders (section 8), so the relative cost position is not shown. What the filings do show is the company's own judgement that it is not currently the cheapest choice for its customer.

**Test 2, would it stand without the lord?** **[L2007-006]**, **[M1996-037]**. The founder, Akio Nitori, born 1944-03-05, is chairman and CEO and since 2024-02 also president of the operating company Nitori, since 2025-05 chairman of Shimachu, and since 2023-12 president of the furniture manufacturing subsidiary (SR FY3/26 p.50); the risk section names him and the president as officers whose absence would hurt (p.23, ⑤). A founder of 82 taking operating posts back is the opposite of the business that "doesn’t require good management". The draft's failing answer for a retailer is "In retailing, to coast is to fail." **[L1995-008]**. **Weighs against.**

**Test 11, what could destroy, modify or reduce it** **[M2000-014]**: the company itself lists Japan's population decline and the settled weak yen among the changes it faces (SR FY3/26 p.9), with about 90% of goods priced in dollars at cost (p.22).

**Tests 3 and 9 (the money test, ask the competitors)**: not answerable from the whitelisted sources; no instance in the reports of a competitor named with figures.

**Verdict and why OUT rather than TOO HARD.** Tests 4 and 8 are answered against the castle with the company's own figures and words; test 10 shows it narrowing; test 2 shows it leaning on the lord; the one exception that could rescue a price-led business, the low-cost position, is unproven and contradicted by the company's own diagnosis. The draft's list "What it rules OUT" names "The customer who buys on the low bid **[L2004-003]** **[M2017-009]**" and "The tenuous moat, which cannot be valued **[M2000-019]**"; "If we can think of very much that can go wrong with them, we just forget it." **[M2000-016]**. A question answered against the name is OUT in section I's terms **[M2006-013]**. A reader who weighs the unproven low-cost exception more heavily would send it to TOO HARD ("a castle whose future cannot be judged", **[M2000-014]**); the box changes, the result does not: the file closes at Q2. Price does not reopen it **[M2019-015]**.

### Q3 to Q8. **NOT REACHED.**

### COMPUTATION — NOT A CLEARANCE

Recorded for the holdings review (section 5), which needs the retention arithmetic, and for the record. No value below is a clearance and none is reported as one.

*Owner earnings, FY3/26, built as the draft's Q4 directs* (regular earnings after all costs **[L2021-003]**, depreciation as a real cost with depreciation as a proxy for maintenance spending in most companies **[M1998-127]**, the maintenance figure a stated guess **[M2000-144]**). IFRS 16 moves store rent into depreciation of right-of-use assets plus interest, so the rent is put back as a cash cost by deducting lease principal repaid.

| Line | ¥m | Source |
|---|---|---|
| Net income attributable | 89,270 | SR FY3/26 p.2 |
| + Depreciation and amortization | 69,509 | FB FY3/26 p.4 (CF) |
| of which right-of-use depreciation | 38,973 | SR FY3/26 p.106 (使用権資産の減価償却費) |
| of which owned-asset D&A | 30,536 | arithmetic |
| - Lease liabilities repaid | 36,066 | FB FY3/26 p.4 (CF) |
| - Maintenance capex, guessed at owned-asset D&A | 30,536 | guess, per **[M1998-127]**, **[M2000-144]** |
| **Owner earnings, maintenance basis** | **92,177** | arithmetic |
| Actual capex FY3/26 (PP&E and investment property 41,412 + intangibles 3,000) | 44,412 | FB FY3/26 p.4 |
| Owner earnings on actual capex | 78,301 | arithmetic |
| FY3/25 on actual capex: 82,546 + 66,143 - 37,319 - 125,308 | -13,938 | FB FY3/26 p.4 |

Per share on the maintenance basis: ¥92,177m / 565.06m = about ¥163; against ¥3,009 that is an owner-earnings yield of about 5.4% on earnings that have not grown since FY2/21, beside the JGB 30-year at 4.122%. Price to net income: ¥1,700.3bn / ¥89.27bn = 19.0x. No range of value is computed: Q2 closed the file, and the draft says a tenuous moat leaves Q7 "nothing to work on" **[M2000-019]**.

*Capital spent, FY2/22 to FY3/25* (SR CF lines, PP&E + intangibles): 103,162; 116,404 (13 months); 121,961; 125,308. The FY3/26 report says the six owned DCs are now all running and logistics cost "当連結会計年度でピークアウトする見込み" (SR FY3/26 p.26). Acquisition: Shimachu, 77.04% bought for cash ¥165,054m in January 2021, goodwill ¥31,665m provisional (SR FY2/21 p.82), squeezed out to 100% in 2021 (SR FY2/22 p.82); Shimachu segment profit ¥-1,288m (FY3/25) and ¥7,212m (FY3/26) on revenue ¥110,273m (SR FY3/26 p.25).

---

## 4. Q9 and Q10. **NOT REACHED.** (For the record: borrowings ¥160,000m against cash ¥145,010m and other current financial assets ¥38,644m at 2026-03-31, equity ratio 62.9%, FB FY3/26 p.3; nothing in the reports read suggests the target's debt could ruin an owner.)

---

## 5. Q11 and Q12

### Q11 - under `DRAFT - THE HOLDINGS FRAMEWORK v5.md` (the operator holds the name)

Default: keep unless a reason the rows name is found; "when in doubt, keep holding. But it’s no inviolable rule." **[M2009-040]**. The holder cannot be forced to sell only if no borrowed money stands behind the position **[M2020-022]** (not visible to this run).

**H-Q1 - What has moved: the business, or only its price? STOP on price alone; WEIGHING on a silly price. Answer: the business has moved, not only the price; the price is not silly.** Would the operator feel poorer if he owned all of it **[M2020-018]**? Yes: net income ¥92.1bn (FY2/21) to ¥89.3bn (FY3/26) with ¥368bn retained in between (H-Q4), existing-store customers down about 21% (Q2). So the STOP against selling on price alone does not close the review; the review goes on to the business questions. At 19x earnings the price is not a silly one **[M2007-089]** (the rows give no threshold; none is written).

**H-Q2 - Has the castle changed? WEIGHING. Answer: yes, narrowed; graded MAJOR, not life-threatening.** The moat test runs "more subjective" **[L2007-016]**; this one narrowed by every measure in Q2 (margin 19.2% to 13.8%, ROE about 15% to 9.4%, customers falling, the company's own statement that it is not cheap enough). Grade **[M2016-081]**: not life-threatening (operating cash flow ¥148,911m in FY3/26, FB p.4; no cash drain **[M2020-026]**); more than minor, because it is the core proposition (price) that the customer has marked down, not a scandal that leaves the earning power intact **[M2012-051]**. The rows act on exactly this for a marketable holding: "we probably don’t think that their competitive advantage is as strong as we might have thought" **[M2002-004]**; against it, "we can’t [...] make a portfolio change [...] every time something is a little less advantaged than it used to be" **[M2016-080]**. **Weighs toward sale**, not decisive.

**H-Q3 - Has the management changed, or changed after being paid? WEIGHING on ability. Answer: UNDECIDED, with succession weighing against.** No misconduct found in the reports read **[L2022-001]**. Candour is a plus: the FY3/26 report names its own failure as the cause of the customer loss (p.25), the opposite of the "mistake" taboo **[L2024-003]**, **[M1998-039]**. Against: the founder, now 82, has re-taken operating posts (SR FY3/26 p.50), so the business depends on him more, not less **[M2018-007]**, and the draft's first risk is the wrong successor **[M2021-042]**. The founder group owns a large stake (Nitori Shoji 18.34%, Akio Nitori 3.00%, the Nitori International Scholarship Foundation 4.40%, SR FY3/26 p.34), so love of the business over money is not in doubt.

**H-Q4 - Is the money kept still becoming more than a dollar? WEIGHING. Answer: NO, it fails over five years.** Retained FY2/22 to FY3/26 = net income (96,724 + 95,129 + 86,523 + 82,546 + 89,270 = 450,192) less dividends paid (15,360 + 16,064 + 16,713 + 16,715 + 17,280 = 82,132) = **¥368bn** (SR CF lines; FY3/24 and earlier JGAAP, FY3/25 and FY3/26 IFRS; mixing labelled). Market leg **[R1995-009]**: market value about ¥2,365bn at FYE Feb 2021 against ¥1,700bn now, a fall of about ¥665bn against ¥368bn kept. Earnings leg **[M2011-072]**, which the 2009 rewrite says to read when the market leg may mislead **[R2009-002]**: "whether the earnings progress at a rate that’s commensurate with the amount of capital that’s being retained" - net income went from ¥92.1bn to ¥89.3bn. Both legs fail over the span the rows set (three or four years **[M1998-110]**, five **[R1995-009]**). The presumption "becomes very strong" **[M1998-110]**. Buybacks: none of size (¥2m to ¥5m a year, FB FY3/26 p.4); issuance: none (no options, SR FY3/26 p.33). The Shimachu purchase (¥165bn for 77%) earns a segment profit of ¥7.2bn in its best recent year; the post-mortem the rows ask for **[L2014-013]** is not in the reports read. The draft's one STOP here is on further money into a business that will chew it up **[L2023-010]**; this business is not chewing up cash, so the STOP does not fire, but it **weighs against** keeping.

**H-Q5 - Is there a plainly better use for this money? WEIGHING. Answer: UNDECIDED.** The holder's opportunity cost is "the least attractive stock which I would give up" **[M2007-104]**, and "the ideal way is when you found something you like immensely better" **[M1998-013]**. The operator's other holdings and candidates are off the whitelist, so no comparison can be made. The one visible alternative is the JGB at 4.122% against an owner-earnings yield of about 5.4% on flat earnings; the gap is thin, and "8 1/2 wouldn’t tempt you" **[M2007-098]** reads both ways. Not decided here.

**H-Q6 - Was it a mistake to buy, now recognised? WEIGHING. Answer: UNDECIDED; the purchase record is not visible.** The question separates a misjudgement at entry from a change in the world **[M2012-031]**, **[M2016-065]**. The date, price and reasoning of the operator's purchase are off the whitelist. If the purchase rested on the pre-2022 record of rising customers at flat prices, the change since is in the business (H-Q2), not necessarily an error at entry. New facts have come in and are written down here **[M1997-127]**; if the operator concludes it was a mistake, the rows ask that the whole position be acted on, promptly **[M2020-020]**, **[L2008-003]**.

**Adds.** Under the holdings draft, section IV, an add is a purchase on price (Q7) and the comparison (Q8), with the section II answers standing in for Q1 to Q6. The purchase run above closed OUT at Q2, so no add is supported on either reading.

**Summary of the review (no named outcome; the draft gives verbs, not verdicts, and a named outcome would be a CONVENTION).** H-Q1 does not close the review; H-Q2 and H-Q4 weigh toward sale; H-Q3, H-Q5 and H-Q6 are undecided on the evidence visible to this run. The burden sits on the reason to sell **[M2009-040]**, and for a marketable security "at some price, you have to be willing to sell" **[M1996-095]**; this run does not take or recommend a position.

### Q12 - the newspaper test (optional). WEIGHING. **Answer: nothing against found.**

A home-furnishings retailer is not among the businesses the rows name **[M2008-011]**, **[M2007-018]**. No conduct read in the reports would trouble the neighbours; the run did not search outside the filings.

---

## 6. The box

**OUT, decided at Q2** (the castle: the customer buys on the low bid and the moat is narrowing, in the company's own figures and words). Q7 not reached; no value range is reported. Holdings review: the business has moved, not only its price; Q2 and Q4 of the holdings draft weigh toward sale; no position taken.

---

## 7. Self-audit

- [x] Every v5 id cited was grepped in `principle_ledger_v5.csv` before writing (a list of 180-odd ids, all present); the ids added during writing were checked the same way.
- [~] Every filing fact carries document, period, filing date and page. **The EDINET document ID (accession) is missing for every report**: it is not in the extracted text and was not fetched. Filer code E03144 and filing dates stand in.
- [x] One figure cross-checked between two filed documents (FY3/26 revenue, SR p.2 against FB p.2).
- [x] No number without a filing, a row, or arithmetic shown. Price and sovereign are the parent session's, flagged. The maintenance-capex figure is a guess, labelled as the draft requires **[M2000-144]**.
- [x] Whitelist kept: the two drafts, the v5 ledger, `txt/` and `fbtxt/` under the NCLTY research folder, nitorihd.co.jp. Not opened: `peers_jp/`, `peers_jp.md`, `part*.md`, `_README.md`, `monthly/`, any `.md` under `Test Runs/`, the v4 framework, the holdings framework of record, `principle_ledger.csv`, `PORTFOLIO.md`, other test files.
- [x] Order kept; the first failing STOP (Q2) closed the purchase run; Q3 to Q10 marked NOT REACHED; the arithmetic shown is under `COMPUTATION — NOT A CLEARANCE`.
- [x] No em dashes in my own prose.
- [ ] Peer comparison not made (section 8).

---

## 8. What in the draft was wrong or unclear

Four things. (1) **OUT or TOO HARD at Q2 is not decidable from the draft's text for a tenuous moat.** Q2's STOP paragraph sends "a castle shown to be open" to OUT and "a castle whose future cannot be judged" to TOO HARD, but its list "What it rules OUT" puts "The tenuous moat, which cannot be valued **[M2000-019]**" under OUT, while **[M2000-019]**'s own reason ("We don’t know how to valuate that") is the TOO HARD reason the draft gives for rapid change. A narrowing moat whose rescue (the low-cost exception) is unproven sits exactly between the two; I chose OUT because two tests were answered against the name with filed evidence, and say so. (2) **The low-cost exception needs a competitor's figures, and nothing in the draft says what to do when they cannot be had.** "The cost is measured against the competitor" **[M2001-013]**; the task asked for a peer comparison from a peer's own filing "if the folders hold one", but the four folders I was allowed to open hold none (the peer files sit in `peers_jp/`, which the task's whitelist excludes), so test 6 was left open and the verdict rests on tests 4, 8 and 10. (3) **The holdings draft's section IV and the purchase draft disagree on what an add must pass**: the holdings draft lets the holding's own answers stand in for Q1 to Q6 and tests an add only on Q7 and Q8, while the purchase draft's Q8 counts "more of what I already own" as an ordinary purchase alternative; for a name the purchase run closes at Q2, the two give different routes to the same "no add" here, but could diverge for a name that is OUT at Q2 yet cheap. (4) **The protocol's accession rule assumes an SEC filer**; for an EDINET filer the document ID was not in the extracted text, and neither the draft nor the protocol says what stands in. I used filer code, period, filing date and page.
