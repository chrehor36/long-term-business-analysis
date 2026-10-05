# Company Run — NIHON KOHDEN CORPORATION (TSE Prime: 6849; unsponsored ADR NHNKY) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*(Copied from the template before any fetch, 2026-10-05. Working folder: `Test Runs/_research 2026-10-05 NHNKY/`; every
document relied on is saved there as fetched, with a text extraction beside it.)*

**POSITION NOTE, declared before any verdict:** not checked. This run was dispatched under a blind rule that forbids
opening `PORTFOLIO.md`, the 2026-07-15 NHNKY run file, any holding review, the session-state files and the queue register,
and forbids trying to learn whether anyone holds the name. None of them was opened.

**CONTAMINATION, declared.** (1) The dispatch itself names an earlier run file for this ticker (2026-07-15, pre-v4.1)
and a research folder of 2026-08-26 holding this company's FY2026-03 tanshin, so I know the name was worked before; I do
not know what those runs concluded. (2) To check that the permitted tanshin existed I listed the 2026-08-26 folder; the
first sixty entries shown were other companies' filings and nothing about Nihon Kohden beyond the permitted PDF was read.
(3) The auto-loaded project instructions and memory index do not name this ticker; the memory index mentions a count of
"gate-clearers" and "nothing buyable" for the queue generally, which carries no information about this name.
(4) The git status at session start (truncated) showed nothing about this ticker.

**Fiscal-year labels.** Nihon Kohden's year ends 31 March and the company calls the year ended March 2026 "FY2025". To
avoid that trap this file writes years by their end: **FY3/26** = April 2025 to March 2026; **Q1 FY3/27** = April to
June 2026.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥1,582.0, TSE close 2026-10-05 (Yahoo Finance chart API, `yahoo_6849.json`; **aggregator, flagged** under
  operator rule 5). Previous close ¥1,562.5 (2026-10-02). 52-week range ¥1,323.0 to ¥1,885.5 (same source, flagged).
  ADR: NHNKY last $9.91 (OTC, 2026-10-02, Yahoo, flagged, thin: 1,000 shares). **ADR ratio 1 ADS : 1 share**, from the
  depositary's Form F-6 POS of 2024 (accession `0001019155-24-000176`, `nihonreceipt.htm`: "One (1) American Depositary
  Share represents One (1) share"; the amendment re-set the ratio after the 2-for-1 split of 2024-07-01). Cross-check:
  ¥1,562.5 / 157.93 (USD/JPY 2026-10-01, Yahoo, flagged) = $9.89 against $9.91.
- **Shares by class** (one class, common): issued 167,961,960, treasury 7,989,554 (includes shares held by the employee
  stock ownership trust), outstanding **159,972,406** at 2026-06-30, from the cover of the Q1 FY3/27 tanshin
  ("Consolidated Financial Results for the 1st Quarter of the Fiscal Year Ending March 31, 2027", 2026-08-06, company IR
  file `140120260805510186.pdf`; a TDnet release, no EDINET document ID). The 3,000,000-share cancellation of
  2026-06-18 announced in the FY3/26 tanshin is reflected (issued fell from 170,961,960). `Screens/cover_shares.py` is
  SEC-only and was not usable.
- **Market cap:** 159,972,406 × ¥1,582 = **¥253.1bn** (about $1.60bn at 158.13).
- **Sovereign for the earnings currency (JPY):** **4.148%**, the 30-year JGB on 2026-10-02, from Japan's Ministry of
  Finance `jgbcme.csv` (issuing authority; file saved as `jgbcme.csv`). The 10-year was 3.097% the same day.
- **Filings read** (operator rule 4):
  - 有価証券報告書 (annual securities report) **FY3/26**, filed 2026-06-24 to the Kanto Local Finance Bureau, EDINET
    filer code E01903, **EDINET document ID S100YHO8** (the ID is the company's own file name for the PDF on its IR
    page; 126 pages, `S100YHO8.pdf`). Read: five-year indicators (p.1-2), business risks (p.15-17), directors' pay
    (p.58), consolidated statements (p.66-72).
  - 有価証券報告書 **FY3/24**, filed 2024-06-27, **EDINET document ID S100TUGR** (`S100TUGR.pdf`).
  - 有価証券報告書 **FY3/21** (第70期) and **FY3/19** (第68期), the company's printed PDFs (`yuuhou2021.pdf`,
    `yuuhou2019.pdf`); the EDINET IDs are not printed on these copies and I could not reach EDINET's own search to read
    them off, **so those two documents are identified by name and period only (gap confessed)**. Consolidated balance
    sheets and cash-flow statements for Mar-18 to Mar-21 were read from them.
  - 決算短信 FY3/26 (English translation, 2026-05-14, `NihonKohden_FY2026-03_ConsolidatedFinancialResults_tanshin.pdf`,
    the one file permitted from the 2026-08-26 folder, copied in); 決算短信 Q1 FY3/27 (English, 2026-08-06). Tanshin are
    TDnet releases with no EDINET ID.
  - The company's Factbook 2026 (ten years, FY3/17 to FY3/26, `Factbook2026.xlsx`), its five-year financial statements
    workbook (`financialstatements.xlsx`, FY3/22 to FY3/26), the FY3/26 results presentation with transcript and the
    analyst Q&A of 2026-05-15, and the Q1 FY3/27 presentation.
  - **No proxy in the US sense.** The securities report's governance and pay sections (p.55-58) were read in its place.
- **One figure cross-checked against the filed statement:** operating cash flow FY3/26 **¥21,055m** in the tanshin
  equals the filed consolidated cash-flow statement in S100YHO8 (p.72, 営業活動によるキャッシュ・フロー 15,286 / 21,055);
  total assets ¥256,538m agree in both (S100YHO8 p.66).
- `tools/run.py` was not used: it works from SEC data and this is not an SEC filer. The arithmetic below was done in
  `owner_cash_computation.py` in the working folder (output saved beside it); it fetches nothing and adds no number
  that is not a sum of filed figures.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what this company's operations will produce, not where the quote goes; "Would I
be happy buying this stock if the market closed for five years?" **[M1997-109]**. The quotation has fallen from ¥2,002
(split-adjusted, March 2024) to ¥1,455 (March 2026) and stands at ¥1,582 today; that fall "doesn’t tell us anything. It
just tells us prices" **[M2006-077]**, and it is neither a reason to buy nor a reason to stop looking. No macro view of
Japanese hospital budgets or the yen enters as a forecast; the hospital-budget dependence enters only as a property of the
business (Q2). The analyst's habits govern the work: "I’m looking for what’s wrong in things because that’s part of
investing – looking at what you’re missing." **[M2025-013]**, and the research is aimed "to possibly reject your original
hypothesis" **[M1998-144]**. **Contrary evidence, written down as found** **[M1997-127]**: (a) consumables and service
rose from 42.8% of sales (FY3/17) to 50.7% (FY3/26) and in-house products from 63.1% to 75.2% (Factbook 2026 sheet 4),
which is what a strengthening installed-base franchise looks like; (b) the company estimates its US share of mask-type
ventilators at "40% or more in 2025" (FY3/26 results presentation, p.33-34); (c) the pandemic years showed the business
can earn 13.6% to 15.1% operating margins (FY3/21, FY3/22); (d) the FY3/27 forecast is operating income ¥23.5bn, up
25.4%, on the exit from low-margin Abbott distribution; (e) the balance sheet is strong: equity ratio 72.0% at
2026-06-30. Each is weighed at the question it bears on.

## THE STANDING RULE
A cash purchase of TSE shares or 1:1 ADRs, unlevered, sized so that a fall of half would not force a sale, puts the buyer
at no risk of ruin; the rule is met by the buyer's conduct, not by the target **[M2012-081]**, **[L2014-005]**. Nothing
here requires borrowing. The one buyer-side exposure is currency: the earnings are in yen.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" and "some notion of how the industry will develop and where the company will stand within
  the industry" **[M2012-065]**; the first step is "trying to identify the key variables [...] and evaluating how
  predictable they were" **[M1998-044]**.
- **What the business is, from the filings.** A Japanese medical-electronics maker: patient monitors ¥84.3bn,
  physiological measuring equipment (ECG, EEG, neurology) ¥53.6bn, treatment equipment (defibrillators, AEDs,
  ventilators) ¥56.3bn, other (hematology, maintenance, purchased products) ¥40.9bn; sales ¥235.1bn FY3/26, 61% in
  Japan, where "sales to public medical institutions [...] account for a relatively high percentage of total sales"
  (FY3/26 tanshin, p.3). Half of sales are consumables and service on the installed base.
- **The key variables.** (1) Japanese hospital capital spending and the prices hospitals will pay, which move with the
  national reimbursement schedule and hospital finances: the company itself puts Japanese market growth at "Approx.1~2%"
  and its own ten-year domestic sales CAGR at "+1.6%" (FY3/26 presentation, p.32). Slow and visible. (2) Whether the
  overseas business (39% of sales) earns a decent margin against much larger competitors. (3) The pace at which
  monitoring moves from hardware to software and data (the company's "DHS" products are 16% of North American monitor
  sales). Variable (1) is foreseeable in a general way; (2) and (3) are the castle questions, and Q2 owns them.
- **Do the past statements tell me the future ones** **[M2008-033]**? Broadly yes: nine years of sales growing 3.9% a
  year and operating margins of 8.0% to 10.2% outside the two pandemic years (Factbook 2026, sheet 1). The product
  chemistry and electronics need not be understood; the economic dynamics can be **[M2011-014]**.
- **Against IN, written down.** Management's own one-year forecasts miss: the analyst Q&A of 2026-05-15 records "We
  will continue our efforts to improve the accuracy of forecasts, especially for overseas subsidiaries, which remains an
  issue" and a review of "the process of forecasts to avoid repeated revisions"; the three-year plan's FY3/27 operating
  income target of ¥38.5bn now stands against a forecast of ¥23.5bn. That is evidence that the insiders cannot place the
  margin within a few points. It is not evidence that the economics are unforeseeable in kind: the range of outcomes is
  an ordinary-margin device maker in every year of the record. I do not hold a doubt about whether the business is inside
  the perimeter **[M2002-092]**; the doubt I hold is about the castle, which is the next question.
- **Routing.** Not a fast-changing technology business that the Q1 routing sends to TOO HARD; not a financial
  institution; not a holding company.
- **VERDICT: IN**, narrowly, with **[M2012-065]**, **[M1998-044]**, **[M2011-014]**, and the filing facts above.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The rows define the castle by what it protects: "an enduring "moat" that protects excellent returns on invested capital"
**[L2007-004]**; "a great business, which means that business is going to earn a high return on capital employed for a
very long period of time" **[M2007-023]**. The question is therefore asked of the returns first, then of each test.

**What the filings show the castle protects.**
- Operating margin 8.2% (FY3/17), 8.3%, 8.4%, 8.4%, 13.6%, 15.1%, 10.2%, 8.8%, 9.2%, **8.0% (FY3/26)** (Factbook 2026,
  sheet 1, from the securities reports). ROE 9.1%, 8.6%, 9.9%, 8.3%, 14.0%, 15.9%, 10.6%, 9.8%, 7.8%, **8.1%** (sheet 8;
  S100YHO8 p.1). The company "currently estimates that its cost of capital is around 8%" (FY3/26 tanshin, p.9). Over
  the decade, outside the pandemic, the return on equity sat at or about the company's own estimate of its cost of
  capital.
- Pre-tax operating income on the tangible operating capital (receivables, inventories and property less trade
  payables) was **18.7%** in FY3/18 (¥14.5bn on ¥77.7bn) and **13.6%** in FY3/26 (¥18.7bn on ¥138.0bn); the ¥60.3bn
  added in between earned **7.0%** pre-tax (`owner_cash_computation_output.txt`; balance sheets in yuuhou2019 p.44-45
  and S100YHO8 p.66). Returns measured on the capital actually needed **[M2010-090]**, on tangible assets **[M2011-060]**.
- The speakers' own remark on Japanese business is the base rate here: "The returns on equity in most areas of Japanese
  business, returns on equity are very low. And it’s extremely difficult to get rich by owning — by being the owner of a
  business that earns a low return on equity." **[M1998-005]**

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent* **[M1995-038]**. For: an installed base whose consumables and service are now half
   of sales; the leading domestic position in monitors (Nihon Kohden sells ¥84.3bn of monitors worldwide; its domestic
   rival Fukuda Denshi sells ¥9.3bn, nearly all in Japan, Fukuda FY3/26 tanshin segment note); a domestic sales and service network. Against: the
   home market grows "Approx.1~2%" and the domestic business has grown 1.6% a year for ten years (presentation p.32); a
   tenth of sales (Abbott products, ¥23.6bn) is a distribution line now ending, falling to ¥2.3bn (p.30).
2. *Would it stand without the lord* **[L2007-006]**. Not tested by the record; the business has had ordinary
   management and ordinary returns throughout.
3. *The attacker with money* **[M2011-015]**, **[M1997-103]**. The attacker exists and is winning abroad: Mindray's
   Hong Kong listing document ranks the global patient-monitoring and life-support market in 2024 as Mindray 14.3%, a
   US-listed company (GE HealthCare by its description) 13.9%, a Dutch one (Philips) 13.4%, a German one (Dräger) 8.4%,
   and "Company M [...] a leading manufacturer, developer and distributor of medical electronic equipment headquartered
   in Japan and listed on the Tokyo Stock Exchange" 7.7% (Mindray H-share Application Proof, HKEX
   `sehk26051101259.pdf`, p.89; **a draft document, flagged**; the identification of Company M as Nihon Kohden is my
   inference from the description and from Nihon Kohden's own sales of about $0.9bn in these lines). Nihon Kohden itself
   reports "intensifying price competition" in the Middle East & Africa and Europe (FY3/26 presentation, p.30). "one
   competitor is frequently enough to ruin a business" **[M2012-108]**.
4. *Pricing power and the agony before a rise* **[M2005-020]**. The company "raised selling prices of in-house products
   and consumables" in Japan in FY3/26, and still "Gross profit margin decreased over FY2024 due to higher raw material
   prices and increase in inventory devaluation" (tanshin p.10); domestic sales fell 0.6%; the shortfall against its own
   operating-income forecast was "around 30% due to lower gross margin and around 70% due to higher SG&A expenses"
   (Q&A, 2026-05-15). Its customers are hospitals in which "the proportion of operating deficits increased" (tanshin
   p.5). The rows' test: "businesses with strong competitive positions manage to pass through increases in raw material
   costs" **[M2005-017]** (the same row allows "temporary situations"; one year is not a decade, and the decade's
   operating margin is flat, which is the stronger fact).
5. *Unit volume and share of mind* **[M1997-099]**. Domestic in-house product sales "decreased slightly" in FY3/26
   (tanshin p.10); in Q1 FY3/27 domestic sales fell 15.0%, flat on a comparable basis, and the Japan segment's income
   fell 84.2% to ¥243m (Q1 tanshin p.5-6).
6. *The low-cost position* **[M2018-043]**, **[M1997-010]**. Nihon Kohden is not the low-cost producer. Mindray's
   patient-monitoring and life-support gross margin was 59.4% in 2025 (Application Proof, p.16) against Nihon Kohden's
   whole-company gross margin of 51.8%, and Mindray sells at the lower price; "the low-cost producer can put you out of
   business" **[M1997-010]**.
7. *The brand in the customer's mind.* Strong in Japan by every sign the filings give (share of monitors, the
   reputation the DOWELL note claims for its operating-room IT); fifth abroad.
8. *Would the customer choose it over the low bid* **[M2017-009]**? The securities report names the buying method
   abroad: public hospitals with "入札案件が多い" (many tender cases) (S100YHO8 p.16, risk (3)); at home the largest
   customers are public institutions buying on budgets concentrated in September and March. The customer here is a
   budget-holder buying by tender, the class the rows describe in "most insureds don't care from whom they buy"
   **[L2004-003]**; I did not find, in any filing, evidence that Nihon Kohden wins tenders at a premium price.
9. *Ask the competitors* **[M1999-130]**. The nearest thing on the public record is the competitor's own ranking: Mindray
   places Nihon Kohden fifth of five globally (test 3).
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Narrowing on the capital measure: pre-tax return on tangible
   operating capital 18.7% to 13.6%, incremental 7.0% (above). Flat on the margin measure. Narrowing on the domestic
   segment: income down 35.7% in FY3/26 to ¥14.1bn (tanshin p.6). The three-year plan's 15% operating margin target is
   being missed by about five points (tanshin p.9-11).
11. *What could destroy, modify or reduce it* **[M2000-014]**. A low-cost rival with three to four times the margin,
   now selling more abroad than at home; the shift of monitoring value toward software and data; a domestic customer base
   under financial strain.

**The competitor row** (same metrics, competitors' own filings):

| Company | Document (accession or ID) | Metric | Value |
|---|---|---|---|
| Nihon Kohden | FY3/26 tanshin 2026-05-14; S100YHO8 | operating margin, group | **8.0%** (FY3/25 9.2%) |
| Nihon Kohden | same, segment note | segment income / external sales: Japan / North America / Rest of World | 9.7% / 5.3% / 6.2% (Japan FY3/25: 15.0%) |
| Fukuda Denshi (6960) | FY3/26 tanshin 2026-05-15 (TDnet, `peers/fukuda_tanshin_FY2026-03.pdf`) | operating margin, group; patient-monitor segment | **19.0%** (FY3/25 18.6%); monitors 18.3% (¥1,702m on ¥9,310m) |
| GE HealthCare | 10-K FY2025, accession `0001932393-26-000007` | Patient Care Solutions segment EBIT margin | **6.8%** ($209m on $3,086m; 2024: 11.1%) |
| Philips | 20-F FY2025, accession `0001628280-26-009470` | Connected Care income from operations; adjusted EBITA | **2%** (€89m on €5,076m); adjusted EBITA 10.7% |
| Mindray (300760) | HKEX Application Proof, May 2026, `sehk26051101259.pdf` (**draft**) | profit before tax / revenue 2025; PMLS gross margin | **29.1%** (RMB 9,674m on 33,282m); 59.4% |

Read together: the two Western incumbents earn single-digit or low-teens margins in this line of business; the Chinese
attacker earns about three times Nihon Kohden's margin while undercutting on price; and in Nihon Kohden's own home
market a smaller domestic rival in the same product classes earns more than twice its margin. Fukuda's mix is not the
same (its treatment segment includes home-oxygen rental at 21.9%), but its monitor and testing segments alone earn 16% to
18%. Nihon Kohden's castle has share; the filings do not show it protecting a return.

**Stating the other side's case** **[M2016-055]**. The installed base is real, consumables and service are rising toward
55% of domestic sales (presentation p.32), gross margin rose four points in ten years, the US ventilator share is a new
and genuine position, and the Abbott exit will lift the margin mechanically in FY3/27. On that case the castle is
"widening", and the poor returns are the cost of a decade of building abroad. My answer: the widening the rows ask for
is widening that shows in the return on capital over time **[M2000-075]**, **[M2000-018]**; ten years of building has
left the return on tangible operating capital lower, the incremental return at 7% pre-tax, and the overseas segments at
5% to 6% margins in the year of their best sales. Gross margin gains were absorbed by selling and administrative costs
(39.4% of sales FY3/17 to 43.8% FY3/26, Factbook sheet 5). The bull case is a forecast; the bear case is the record.

**VERDICT: OUT.** The castle test is not passed. What the filings show is the position the rows call "The average
company, in contrast, does battle daily without any such means of protection" **[L1993-021]**: a domestic leader whose
returns sit at its own cost of capital, a high-cost producer abroad against a low-cost attacker **[M1997-010]**,
**[M2007-117]**, and a return on capital that has narrowed over the decade **[M1999-108]**. This is a finding from the
evidence in hand, not an inability to judge, so the box is OUT, not TOO HARD **[M2011-015]**, **[M2006-013]**. Price does
not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "it makes
more sense [...] to buy a wonderful business at a fair price, than a fair business at a wonderful price." **[M2003-040]**

---
## Q3 to Q12, NOT REACHED
The run closed at Q2. Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are **NOT REACHED** and carry no verdict. The arithmetic
below was done because the operator asked for the balance-sheet reading, owner cash and the range; it is not a
clearance and carries no entry language.

## COMPUTATION — NOT A CLEARANCE
*Everything in this section was computed after the file closed OUT at Q2. It answers no question and reopens none.*

**1. The balance sheets, nine years read before the income account** **[M2025-032]** (¥bn, 31 March; Mar-18 to Mar-21
from yuuhou2019 and yuuhou2021, Mar-22 to Mar-26 from `financialstatements.xlsx` cross-checked to S100TUGR and
S100YHO8; Mar-17 totals only, from Factbook 2026):

| | Mar-18 | Mar-19 | Mar-20 | Mar-21 | Mar-22 | Mar-23 | Mar-24 | Mar-25 | Mar-26 | Jun-26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Sales, year to date | 174.2 | 178.8 | 185.0 | 199.7 | 205.1 | 206.6 | 222.0 | 225.4 | 235.1 | 47.4 (Q1) |
| Cash + securities | 31.6 | 34.8 | 36.0 | 44.6 | 60.9 | 44.5 | 50.4 | 43.4 | 46.7 | 51.3 |
| Trade receivables | 64.2 | 66.9 | 60.9 | 68.6 | 58.4 | 65.0 | 71.8 | 71.2 | 69.9 | 53.7 |
| Inventories | 23.1 | 28.6 | 29.2 | 38.9 | 48.4 | 58.8 | 57.8 | 56.2 | 56.0 | 56.2 |
| Property, plant | 20.3 | 19.9 | 20.0 | 20.2 | 19.9 | 24.4 | 25.4 | 29.3 | 32.3 | 31.7 |
| Goodwill + intangibles | 5.1 | 4.6 | 4.1 | 2.3 | 3.7 | 4.2 | 4.9 | 27.7 | 27.2 | 27.0 |
| Trade payables | 29.8 | 32.6 | 23.8 | 24.4 | 24.0 | 22.9 | 20.1 | 19.8 | 20.1 | 16.5 |
| Borrowings | 0.5 | 0.4 | 0.4 | 0.4 | 0.3 | 0.4 | 0.6 | 26.0 | 25.0 | 24.4 |
| Retained earnings | 96.1 | 102.4 | 108.5 | 123.8 | 142.2 | 152.5 | 163.6 | 166.2 | 175.5 | 165.0 |
| Net assets | 109.4 | 116.1 | 121.8 | 139.0 | 156.4 | 167.6 | 181.1 | 181.3 | 179.8 | 177.3 |
| Total assets | 157.9 | 169.7 | 167.8 | 193.0 | 210.2 | 216.7 | 233.2 | 258.3 | 256.5 | 246.2 |

What the figures say: **inventories rose 142% (¥23.1bn to ¥56.0bn) while sales rose 35%**; inventory turnover fell from
7.6 to 4.2 times (Factbook sheet 13); trade payables fell by a third; the cash-conversion cycle was 215 days against a
190-day target (tanshin p.9). "inventories look out of line, you know, with sales [...] you want to look twice"
**[M1995-064]**; the company itself booked an "increase in inventory devaluation" in FY3/26. Receivables run at about
108 days of sales, the public-hospital pattern, with an unusual March peak that collects in the June quarter
(¥69.9bn to ¥53.7bn). Goodwill and intangibles jumped by ¥22.8bn in FY3/25 with Ad-Tech (US neurology electrodes),
bought with short-term borrowing later refinanced long (¥25.5bn of long-term loans in FY3/26). Equity grew ¥70bn in
eight years. What the figures cannot say: whether the inventory build is a parts-shortage hedge (the company's
explanation) or slow-moving stock; the devaluation charge is the only evidence and it points both ways. One tell
(inventory) without a second does not make suspicion under v5's two-tell line; the accounts are clear and explained in
plain words **[M1994-018]**.

**2. Owner cash after every real cost** (¥m; operating cash flow, which is after interest, tax and all cash pay, less
cash capital spending on property and intangibles in full; the depreciation variant beside it; never net income
**[L2021-003]**, **[L2015-004]**):

| FY | OCF | Capex (cash) | Owner cash | OCF less D&A | Net income | Acquisitions |
|---|---|---|---|---|---|---|
| 3/18 | 10,843 | 3,315 | 7,528 | 7,505 | 9,154 | 0 |
| 3/19 | 9,819 | 3,250 | 6,569 | 6,277 | 11,191 | 0 |
| 3/20 | 9,217 | 3,591 | 5,626 | 5,620 | 9,854 | 0 |
| 3/21 | 13,945 | 3,384 | 10,561 | 10,709 | 18,243 | 0 |
| 3/22 | 25,699 | 2,934 | 22,765 | 22,277 | 23,435 | 929 |
| 3/23 | -2,513 | 8,256 | -10,769 | -6,188 | 17,110 | 858 |
| 3/24 | 15,607 | 4,786 | 10,821 | 11,903 | 17,026 | 0 |
| 3/25 | 15,286 | 8,709 | 6,577 | 11,220 | 14,098 | 18,869 |
| 3/26 | 21,055 | 7,858 | 13,197 | 16,298 | 14,513 | 7,973 |

- **Five-year average (FY3/22 to FY3/26): ¥8,518m on full capex; ¥11,102m on the depreciation variant.** Per share
  ¥53 and ¥69. After the acquisitions as well: ¥2,792m.
- Over nine years owner cash was ¥72.9bn against net income of ¥134.6bn: **54 cents of owner cash per yen of reported
  profit.** The gap is working capital (mainly inventory). "There was never any cash. Just more used construction
  equipment." **[M2008-036]**; "reports the 12 percent on capital but there’s never any cash" **[M2003-122]**.
- **Maintenance judgment** **[M2000-144]**, **[L1999-024]**: capital spending over nine years was ¥46.1bn against
  depreciation of ¥33.3bn; the excess is the Tsurugashima production centre and the PLM, MES and CRM systems, which I
  treat as growth or one-off. My best guess of maintenance capital spending is about the depreciation charge, ¥4bn to
  ¥5bn a year, which is where depreciation "is not inappropriate [...] to use as a proxy" **[M1998-127]**. The working
  capital build is not optional at present (the company says it must hold parts inventory against shortages, tanshin
  p.9), so it is counted, as operating cash flow counts it. Stock pay is immaterial: directors' restricted stock expense
  ¥21m in FY3/26 (S100YHO8 p.58).

**3. The retention arithmetic (Q6, Part A, not reached)** **[R1995-009]**, **[M1998-110]**. From FY3/19 to FY3/26 the
company earned ¥125.5bn, paid ¥35.8bn in dividends and ¥21.1bn in buybacks, and kept ¥68.5bn. Market value on issued
shares was ¥265.7bn at March 2018 (89.73m × ¥2,961) and is ¥265.7bn today (167.96m × ¥1,582). **¥68.5bn kept, no
market value added.** On the five-year span (FY3/22 to FY3/26): ¥38.2bn kept, market value down from ¥286.6bn (March
2021) to ¥265.7bn. The buybacks (¥10.0bn in FY3/25, ¥6.6bn in FY3/26; prices paid not found in the documents read)
named no price ceiling (tanshin p.8: conducted "in a flexible manner, taking into account [...] stock price level").

**4. A range by the Part VI convention, for information only.** Five-year average owner cash ¥8,518m; growth shown,
measured as the five-year average against the prior five-year average (¥6,786m, FY3/17 to FY3/21, the FY3/17 capex
being the Factbook's accrual figure, flagged), 4.65% a year; ten years then zero nominal growth; discounted at 4.148%.
- Full capex: **¥1,284 (no growth) to ¥1,894 (shown growth) a share**; width 1.5 to 1.
- Depreciation variant: ¥1,673 to ¥2,469.
- Net cash and securities less borrowings at 2026-06-30: ¥27.0bn, ¥169 a share, of which the company says it needs
  "approx. three months of monthly sales" (about ¥59bn) for operations (FY3/26 presentation p.38), so none is surplus.
- **Against ¥1,582 the price sits inside the full-capex range.** Had Q7 been reached it would have closed OUT: not a
  screamer, it needs a pencil **[M2009-005]**, **[M1996-084]**. The owner-cash yield at the price is 3.4% (4.4% on the
  depreciation variant) against the 30-year JGB at 4.148% and the floor convention of about ten percent pre-tax
  **[M2003-149]**; Q8's first filter, the bond **[M1997-089]**, **[M2007-095]**, would also have been failed on the
  full-capex figure.

**5. Debt (Q9, not reached).** Borrowings ¥24.4bn at 2026-06-30 against cash and securities of ¥51.3bn and operating
cash flow of ¥15bn to ¥21bn a year; equity ratio 72.0%. No sudden-demand exposure found in the filings read.

---
## THE BOX
**OUT, at Q2.** The castle the filings show protects an ordinary return: operating margin 8.0% (FY3/26) and 8% to 10% in
every non-pandemic year of ten; ROE about the company's own 8% estimate of its cost of capital; pre-tax return on
tangible operating capital down from 18.7% to 13.6% with 7.0% earned on the capital added; fifth in its global market
behind a low-cost attacker earning three times its margin; and a domestic rival earning 19.0% in the same home market.
Q7 not reached; the computation for information puts the full-capex range at ¥1,284 to ¥1,894 against ¥1,582 (inside the
range, so it would not have cleared either). Q11 belongs to the holding review, not to this run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed after each**: the
      dispatch forbade commits; the write-early order was kept in the file itself.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, see below); every filing fact carries
      its document, date and EDINET ID or accession, **except** the FY3/19 and FY3/21 securities reports (name and
      period only) and the tanshin (TDnet, no EDINET ID): gaps confessed in STEP 0. No v4 id is cited.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; everything after it is under COMPUTATION — NOT A CLEARANCE with
      no entry language.
- [x] Owner cash after every real cost, from operating cash flow less capital spending in full, never a net-income proxy
      (operator rule 5); the sovereign from Japan's Ministry of Finance, dated 2026-10-02; the price, the ADR quote and
      the exchange rate from Yahoo, flagged; the competitor share table from a draft HKEX document, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations paragraph, the "against IN"
      line at Q1, the other side's case at Q2).
- [x] No row dated after the anchor is cited in a point-in-time run (this is not a point-in-time run; the anchor is today).
- [x] `tools/run.py` was not used (non-SEC filer); no tool printed a rule, id or verdict into this file.
- [x] `python tools/check_framework.py` run after writing (result recorded in the reply to the operator; no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2's two closes do not name this case.** The framework sends "a castle shown open on the evidence" to OUT and "a
castle whose future cannot be judged" to TOO HARD. Nihon Kohden's castle is not breached: it has share, an installed base
and a rising consumables mix. What the evidence shows is that it never protected a high return. I read the rows'
definition of a moat by what it protects **[L2007-004]**, **[M2007-023]** as making that an OUT, since the finding is
present-tense and not a forecast; but the framework's text speaks of castles "filling in", and a second analyst could
close the same evidence at Q3 (a weighing) by reading Q2 as a test of share and durability only. The framework should
say which question owns "durable but ordinary". (2) **Accessions for Japanese filers.** The template asks for an
accession on every filing fact; EDINET document IDs serve for securities reports, but the tanshin, the company's main
timely document, has none, and older reports printed by the company carry no ID. The framework is silent; I used IDs
where I had them and confessed the rest. (3) **"Competitors' own filings" and draft documents.** The best competitor
evidence was Mindray's HKEX Application Proof, a draft that the exchange disclaims; its A-share annual report is in
Chinese and was not read. The framework does not say whether a draft listing document counts. (4) **"Growth shown" in the
Q7 convention** is undefined when owner cash swings negative (FY3/23: -¥10.8bn); endpoint growth on single years is
meaningless here, so I measured the five-year average against the prior five-year average. The convention should name
the measure. (5) **The template's "committed after each"** cannot be met when the dispatch forbids commits; the
self-audit line should allow a run made under a no-commit instruction.
