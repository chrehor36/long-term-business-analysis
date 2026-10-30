# B CASE_E - run. Test B' (blind falsification), sealed case E, under the v5 purchase draft. 2026-10-04.

**Binds nothing.** Run under `Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`. Data: `Framework/v4/testB/CASE_E.json` and `Framework/v4/testB/DESC_E.md` only. Rules: `Framework/v5/DRAFT - THE FRAMEWORK v5.md`, ids from `principle_ledger_v5.csv`. The company is not named or guessed here.

**Accession numbers.** The case file carries filing dates, not accession numbers. Every filing fact below is cited as "case, <series>, period <date>, filed <date>"; the FY2016 annual facts were all filed 2017-02-23, and the FY2014 balance-sheet facts were filed 2016-03-03. Operator rule 4's accession requirement cannot be met from the case and is flagged, not invented.

---

## 0. Step 0 (as given by the case)

| Item | Value | Source as given |
|---|---|---|
| Anchor | 2018-01-02 | case, `anchor` |
| Price | 77.02 (close 77.0199966430664) | case, `price`; Yahoo close, **aggregator, flagged**; stated on today's split basis |
| Shares | 1,226 million | case, `market_cap.shares_millions_as_reported`; period 2016-12-31, filed 2017-02-23. **Flag:** this is the weighted-average share count from tagged data (`shares_dil`), not a cover-page count by class. The case carries no cover page. |
| Split factor after measurement | 1.0 | case |
| Market cap | USD 94,426.5 million | case, `market_cap.value_millions` (close x shares x splits after) |
| Sovereign, earnings currency USD | 2.81%, 2018-01-02 | case, `sovereign`: "US Treasury daily yield curve (issuing authority)". **Flag:** the case does not state the tenor; recorded as given. |
| Newest annual period public at anchor | FY ended 2016-12-31, filed 2017-02-23 | case, `ticker_map_check` |
| Case flags | revenue series blocked (no tag at anchor); long-term debt series empty; stated equity SUSPECT for 2014-12-28 and 2016-01-03 ("DO NOT USE without reading the filed balance sheet"); equity reconciles only for 2016-12-31 | case, `series`, `equity_cross_check` |

## 1. The foundations

Three bear on this name. **A share is a business** **[M1997-109]**: the question is whether one would be content to own this food business with the market closed for five years, which turns on the brands' future against the retailers, not on the quotation. **Margin of safety** **[M1996-084]**: if the case needs pencil and paper it is too close. **The analyst's habits**: write contrary evidence down at once **[M1997-127]** and look for "what's wrong in things" **[M2025-013]**. Under that habit the analyst confesses one hazard: a description this detailed may be recognisable from general knowledge, and the draft itself narrates post-anchor purchase mistakes in packaged food in its Q2 and Q7 mistake lists. To keep the blind, no row from those mistake lists is cited below, and every verdict rests on a case fact. **No macro forecast** **[M2000-094]**: commodity input costs and the currencies of 190 countries enter only as properties of the business, not as forecasts. **Who is paid to tell you** **[M2020-037]**: the present company was assembled by two sponsors; the filing's word "iconic" is the seller's word, and is read as a claim to be tested at Q2, not as evidence.

## 2. The standing rule

No ruin to the buyer: no position is taken; a cash purchase of a marketable stake, unlevered and sized within the buyer's means, risks nothing the buyer has and needs **[M2012-081]**, **[L2014-005]**. Passes; it governs financing and size, not the business.

## 3. Q1 to Q8

### Q1. Can I understand it? STOP.

**The test as the draft states it:** "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]**; the key variables and how predictable they are **[M1998-044]**; whether the forecast is about customers or technology **[M2017-019]**, **[M2023-030]**.

**Applied.** The business sells condiments and sauces (about 26% of sales), cheese and dairy (about 21%), meats and seafood (about 10%), ambient meals (about 9%) and frozen and chilled meals (about 8%), through grocery chains, mass merchants and club stores, in about 190 countries (DESC_E, from the filing of record's Item 1). There is no technology to forecast; R&D "is modest relative to sales" (DESC_E). The forecast is about "consumer behavior and threats to a business" **[M2023-030]**, the analysis the rows call a consumer-products one **[M2017-019]**. The key variables can be named: unit volume and price by category, the brands' standing against retailer-label and generic products, and the share of sales held by a few large customers (DESC_E: largest customer about 22% of net sales). Whether those variables are predictable is the castle question, which Q2 owns.

One reservation is recorded and not decided here: "do I understand enough about this business so that the financial statements will tell me [...] what the future financial statements are going to look like" **[M2008-033]**. The company in its present form dates from a mid-2015 merger and FY2016 is its first full combined year (DESC_E; case, every series has one combined full year). That bears on what the figures can show (Q4), not on whether the economics are of a kind the analyst can foresee.

**Verdict: IN.** The economics are of a kind the rows treat as understandable: consumer products whose forecast is about customers, not technology **[M2017-019]**, **[M2023-030]**, with nameable key variables **[M1998-044]**. Filing fact: DESC_E (Item 1 of the annual report filed 2017-02-23; accession not in case).

### Q2. Why is the castle still standing? STOP.

**The test as the draft states it:** "why is that castle still standing? And what's going to keep it standing or cause it not to be standing five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. A castle shown to be open is OUT; a castle whose future cannot be judged is TOO HARD (draft, Q2, Why it is a STOP).

**Applied, test by test (draft numbering).**

1. *The castle questions.* The key factors the filing names are brands "several of them more than a century old", trademarks "among the company's most valuable assets", and centralised procurement for scale (DESC_E). A century of standing is evidence the castle has stood. It is not evidence of why it will keep standing against the attackers the filing itself names.
2. *Without the lord.* Not decidable from the case; no management information is carried.
3. *The money test* **[M2012-106]**. The case carries no evidence on what it would cost to displace these brands category by category. The filing says improving market position or launching a product "requires substantial advertising and promotional spending" (DESC_E). The rows set share of mind against exactly that spending: "You can't do it by a billion dollar advertising budget" **[M1997-099]**. Whether this business holds its place without that spending, or must buy it every year, the case does not show.
4. *Pricing power* **[M2005-020]**. **Not testable from the case.** The revenue series is blocked at the anchor (case, `revenue.blocked`: 24, no tag), so there is no price, volume or gross margin history. The filing lists price among the grounds of competition (DESC_E). The rows say "you learn a lot about the durability of the economics of a business by observing [...] the price behavior" **[M2005-020]**; there is no price behaviour to observe. Whether raw-material increases (dairy, meats, coffee, oils, among others: DESC_E) are passed through, the mark of a strong position **[M2005-017]**, cannot be seen.
5. *Unit volume and share of mind* **[M1999-054]**. **Not testable:** no unit or volume data in the case.
6. *The low-cost position.* The filing claims procurement scale (DESC_E); no figure in the case sets this company's costs against a competitor's.
7. *The brand against the retailer.* **This is where the case's evidence points, and it points against.** The largest customer, a mass-market retailer, took about 22% of net sales; the five largest took about 49% of home-country segment sales, 76% of the neighbouring country's segment sales and 31% of the overseas developed region's (DESC_E). The filing names competition from "branded, generic and retailer-label products" and on "shelf space" and "merchandising support" (DESC_E). The rows: "to the extent that people trust [...] more than they [...] or as much as [...] they trust the brand, then the value of having the brand moves over to the retailer from the product itself." **[M2001-090]**; "the retailer is going to use all the pressure they've got and, therefore, the brand has to stand for something in the consumer's mind" **[M2015-038]**. With one customer at more than a fifth of sales and the same channel selling its own label, the retailer holds that pressure. Whether the brands stand for enough in the consumer's mind to withstand it is the one fact that decides this castle, and the case does not carry it.
8. *The low bid* **[M2017-009]**. The low bid exists on the same shelf (generic and retailer-label: DESC_E). Whether the customer refuses it is the same unknown as test 7. The rows add that pricing too far against private label changes consumption **[M2001-088]** and that a brand priced past its moat loses share that "once you start losing share, it's hard to get back" **[M2001-087]**; the case cannot say where this business stands on that line.
9. *Ask the competitors.* No competitor's or customer's filing is in the case.
10. *Widening or narrowing* **[M1999-108]**, **[M2000-075]**. **Not testable:** one full combined year (case, every series), so there is no trend.
11. *What could destroy, modify or reduce it* **[M2000-014]**. The named threat is the retailer and its own label. The case cannot size it.

**Weighing the tests together.** The castle is not shown to be open: the brands have stood for a century, and nothing in the case proves the retailer has crossed the moat. So OUT is not supported. But the tests that would show why it stands and whether it will keep standing (4, 5, 10) cannot be run from the case, and the one test the case can run (7) reads as a moat under pressure. The rows' reply to a moat that is "tenuous in any way": "it's just too risky. We don't know how to valuate that, and therefore we leave it alone." **[M2000-019]**; where the threat cannot be figured, "we don't even think about it then." **[M2000-014]**. And a chancy competitive position is not cured by asking a bigger discount: "we don't really try to compensate for that sort of thing by having some extra large margin of safety" **[M2007-022]**.

**Verdict: TOO HARD.** The castle's future against its largest customers cannot be judged from where the analyst stands **[M2000-019]**, **[M2000-014]**, filed in the third box **[M2006-013]**; this is not a judgment that the business is poor or the price high **[M2000-038]**. Filing facts: DESC_E (customer concentration, competition, advertising, trademarks; Item 1, filed 2017-02-23); case `revenue` series blocked at anchor; one combined full year in every series. Accessions not in case.

**What would resolve it (named, not opened):** the FY2016 annual report's MD&A organic net sales split into price and volume/mix by segment, with the same split from the predecessor companies' annual reports for 2010 to 2014; category share against retailer-label and generic products (syndicated scanner data, not a filing); the largest customer's own annual report on its private-label strategy; and the two or three largest branded competitors' annual reports for their price and volume trends in the same categories.

**The run closes here.** Q3 to Q8 are NOT REACHED.

### Q3 to Q8. NOT REACHED.

#### COMPUTATION — NOT A CLEARANCE

Recorded for the record only. No value below is a clearance, and none carries entry language.

- **Q3 / Q4 figures from the case (USD millions).** FY2016 (period 2016-12-31, filed 2017-02-23): operating cash flow 5,238; capital expenditure 1,247; depreciation and amortization 1,337; stock pay 46; net income 3,632. Two estimates of cash after real costs, labelled as estimates: OCF less capex less stock pay = 3,945; net income plus D&A less capex = 3,722. Stock pay is subtracted because it is a real cost **[L2015-003]**, **[L2021-003]**. Per share at 1,226 million shares: about 3.0 to 3.2.
- **Things Q4 would have had to read before using those figures.** (a) Capex sat below D&A in all three years (399 vs 530; 648 vs 740; 1,247 vs 1,337). D&A is "almost always" a true cost **[L2015-004]**, but the case does not split depreciation from amortization of purchased intangibles, which "Some truly deplete over time while others never lose value" **[L2012-003]**; the filed cash-flow note would split them. (b) Net income moved from 634 to 3,632 between FY2015 and FY2016 on a merger midway through FY2015: a base year the rows warn about **[L2005-003]**. (c) The case flags stated equity as SUSPECT for two of four periods; the rows' rule on suspect accounts is to move on **[M1995-063]**, so these would have to be read in the filed balance sheet before any judgment. (d) FY2014 figures are of a predecessor only.
- **Q6, for the record.** Weighted shares went 377 to 786 to 1,226 million over FY2014 to FY2016 (case, `shares_dil`): the merger was paid at least partly in stock. Whether value given matched value got, and whether the sponsors' sale was a business "dressed up for sale, particularly when the seller is a "financial owner"" **[L2000-008]**, would need the merger proxy and the deal terms. Not in the case.
- **Q9, for the record.** Total liabilities 62,906 against total assets 120,480 at 2016-12-31 (case). The long-term debt series is empty, so debt against earning power **[M1995-104]** cannot be read; the filed balance sheet and debt note would be needed.
- **Q7 arithmetic, for the record only.** Against a market cap of 94,426.5, the two cash estimates above are about 3.9% to 4.2% of the price, against a 2.81% sovereign. Discounting one year of combined figures at 2.81% with no growth gives roughly 130,000 to 140,000; a single year after a merger, with the castle undecided, is the case where "the range must be so wide that no useful conclusion can be reached" **[L2000-025]**. No range is reported as a value.

## 4. Q9 and Q10

NOT REACHED (the run closed at Q2). Q9's data gap is recorded above for the record.

## 5. Q11 and Q12

**Q11:** does not apply (not a holding).

**Q12. Would we be proud of how the money is made? STOP for named businesses, otherwise WEIGHING.** Answered at the parent's instruction although the run closed at Q2; it clears nothing. The business is not one the draft names (casinos, tobacco, distributor-loading schemes, gambling dressed as investing; draft Q12). As a weighing, the newspaper test **[M2008-011]** needs conduct evidence (legal proceedings, regulatory actions, the proxy), and the case carries none; the line on "things that are bad for people" **[M2021-059]** is not drawn by the rows at packaged food, and perfection is not demanded **[M2021-012]**. **Verdict: UNDECIDED.** No evidence either way in the case; the annual report's Item 3 (legal proceedings) and the proxy would decide it.

## 6. The box

**TOO HARD, decided at Q2** (the castle's future against its concentrated retail customers and their own labels cannot be judged from the case; the price, volume and trend tests cannot be run with the revenue series blocked and one combined year). Q7 not reached; no value range is reported. Market cap as given: USD 94.4 billion at 2018-01-02.

## 7. Self-audit

- [x] Every id cited resolves in `principle_ledger_v5.csv` (checked by script; see `_work_B_E/idcheck.txt`).
- [ ] Every filing fact has an accession: **NOT MET.** The case carries filing dates (2017-02-23; 2016-03-03) but no accession numbers; flagged in the header, not invented. Operator rule 4's cross-check of one figure against the filed statement is impossible from the case; the case's own equity cross-check is reported instead.
- [x] No number without a row or a filing: every figure is from CASE_E.json or DESC_E.md; derived figures (3,945; 3,722; the percentages) are shown with their arithmetic; the no-growth capitalisation is labelled for the record only.
- [x] Files opened: the protocol, the v5 purchase draft, `principle_ledger_v5.csv`, `Framework/v4/testB/CASE_E.json`, `Framework/v4/testB/DESC_E.md`, and this file and its work folder. `CLAUDE.md` and `Framework/OPERATOR-PROTOCOL.md` were loaded by the session (the protocol whitelists the latter). No sealed key, other case, web or EDGAR.
- [x] Order kept: foundations, standing rule, Q1 IN, Q2 TOO HARD, stop. Q3 to Q10 not reached; arithmetic only under COMPUTATION — NOT A CLEARANCE.
- [x] Company not named or guessed. The possible recognition hazard is confessed in section 1, and no mistake-list row from the draft that could name the case is cited.
- [x] No em dashes in the analyst's prose (headings and quotations keep the draft's forms).

## 8. What in the draft was wrong or unclear

Four things. (1) **OUT or TOO HARD for a tenuous moat.** The Q2 STOP paragraph sends "a castle whose future cannot be judged" to TOO HARD, but Q2's "What it rules OUT" list carries "The tenuous moat, which cannot be valued **[M2000-019]**" under OUT, and M2000-019's own reason ("We don't know how to valuate that") is ignorance, which is the TOO HARD reason. I followed the STOP paragraph and the row's reason and filed TOO HARD; the list item should be moved or relabelled. (2) **No rule separates "too hard for the business" from "too hard for this file."** Here the deciding tests (price, volume, trend) fail because the evidence is missing from the case, not because the business is unforeseeable in principle. Section I says a verdict for a document not yet read is a CONVENTION to be confessed in section VI; the protocol says to return TOO HARD and name the document. I did the latter, which makes the box unable to tell a data gap from an opaque business; a run file needs a field for "the document that would resolve it". (3) **Mixed portfolios.** Every Q2 test assumes one castle. This business is a portfolio, roughly a quarter condiments and about a third cheese, dairy and meats, which the rows would read very differently against a retailer's own label. The draft gives no instruction on whether to judge the castle by its strongest part, its weighted whole or its weakest large part. (4) **Contamination in a blind test.** The draft's narrated-mistakes lists (Q2 "Brands against retailers"; Q7 "Paying too much for a good business") name post-anchor purchases and their outcomes in the food and brands field. In a blind test those lists hand the analyst outcome knowledge. They should be withheld from Test B' sessions, or the draft should mark them as not citable in a point-in-time run. A smaller point: section VII says nothing after a failing STOP is answered, while Q12 has no fixed place in the sequence; I answered it after the stop as instructed and marked it as clearing nothing.
