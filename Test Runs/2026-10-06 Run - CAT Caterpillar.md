# Company Run — Caterpillar Inc. (NYSE: CAT) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run from the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Every judgment cites a v5
ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Research folder: `Test Runs/_research 2026-10-06 CAT/` (the `tools/run.py`,
`cover_shares.py` and `sources.py` outputs, the fetch and text scripts, the ledger helper `ids.py`, the arithmetic script,
and the filing extracts; raw .htm/.txt filings are not committed).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the queue register, the prepped reading list and `tools/alerts.json` were not opened,
and no attempt was made to learn whether the operator holds or wants this name.

**CONTAMINATION, declared.** (1) When the template was copied, a directory listing of `Test Runs/` filtered for "CAT"
showed that an earlier run file exists for this ticker, `2026-09-28 Run - CAT Caterpillar.md` (a v4.1-era date). It was
not opened; only its file name was seen, and the name carries no verdict. No earlier research folder for CAT was opened.
(2) The repository's last three commit subjects (exports of 2026-10-05: S&P 600 runs, tool fixes) were seen; none names
Caterpillar. (3) My training memory holds a general picture of Caterpillar (a cyclical maker of construction and mining
machines and engines, with a captive finance arm, a large independent dealer network, a 2016 loss year, and a data-centre
power boom). It is treated as a prior to be replaced by the filings; every fact below is from a filing read for this run.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$848.14** (2026-10-05 close as fetched by `tools/run.py`; aggregator, flagged per operator rule 5, used for
  the quote only). For scale, the 10-Q's issuer-purchase table shows the company buying its own stock at an average of
  $766.00 in April, $890.17 in May and $947.20 in June 2026 (10-Q Q2 2026, Part II Item 2), and at $385.64 in October 2025
  (10-K FY2025, Item 5).
- **Shares:** one class of common stock. The 10-Q for the quarter ended 2026-06-30 (filed 2026-08-05, accession
  `0000018230-26-000046`) gives on its cover **459,674,889** shares outstanding; `python Screens/cover_shares.py CAT`
  printed the same figure from the same filing ("single class / undimensioned"). The 10-K says basic shares were "approximately
  465 million" at 2025-12-31 (Item 7, Liquidity).
- **Market cap:** $848.14 × 459.675M = **$389.87B** (agrees with `tools/run.py`).
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4), all from SEC EDGAR (CIK 18230):
  - 10-K FY2025, filed 2026-02-13, accession `0000018230-26-000008`: Item 1 (business, competitors by segment, Cat
    Financial, dealers, backlog), Item 1A, Item 5 (issuer purchases), Item 7 (MD&A, outlook, liquidity, resource allocation,
    the non-GAAP reconciliations, the Supplemental Consolidating Data for MP&E and Financial Products), Statements 1, 3
    and 5, Note 3 (stock pay), Note 7 (Cat Financial financing activities, write-offs), Note 16 (repurchases), and the
    segment note's reconciliation of segment profit to consolidated profit.
  - 10-Ks for FY2024 (`0000018230-25-000008`), FY2023 (`0000018230-24-000009`), FY2022 (`0000018230-23-000011`) and FY2021
    (`0000018230-22-000050`): the supplemental cash-flow data and the "ME&T free cash flow" reconciliations, for the
    five-year owner-cash table.
  - 10-Q Q2 2026, filed 2026-08-05, `0000018230-26-000046`: statements, Note on repurchases and ASRs, the IEEPA tariff
    recovery note, MD&A, backlog, Part II Item 2.
  - DEF 14A filed 2026-04-30, `0001308179-26-000358` (read at Q5 and Q6).
  - 8-K of 2026-08-04, `0000018230-26-000040`, EX-99.1 (Q2 2026 earnings release, read at Q4 for non-GAAP habits);
    8-K of 2026-01-06, `0001104659-26-001346` (Executive Chairman Umpleby to leave the board 2026-04-01; CEO Joseph Creed to
    add the chair; board cut from ten to nine); 8-K of 2026-04-10, `0001104659-26-042062` (new CFO Kyle Epley from
    2026-05-01); 8-K of 2026-03-26, `0000018230-26-000013` (Rail moved from Power & Energy to Resource Industries, history
    recast); 8-K of 2026-09-01, `0001104659-26-104197` (bank credit facilities renewed: a $3.5B 364-day facility and the
    three- and five-year facilities extended).
- **One figure cross-checked against the filed statement:** consolidated net cash provided by operating activities for
  2025, **$11,739M** in `tools/run.py` (XBRL) and $11,739M on the filed Consolidated Statement of Cash Flow (10-K FY2025,
  Statement 5) and in the Supplemental Data for Cash Flow. Agrees.
- **`tools/run.py CAT`, arithmetic lines only** (Part VII; its v4 wording, owner-earnings window and verdict language were
  ignored). Its consolidated owner-cash lines treat Caterpillar as one business; they are not used as the input below,
  because the 10-K itself splits the company into two businesses with different balance sheets, and the rows say
  "lumping them together [...] impedes analysis" **[L2008-005]**. The tool did flag the consolidated
  `PaymentsToAcquireEquipmentOnLease` line (Cat Financial's lease fleet) as a capital payment outside capex; that is
  recorded and used in the consolidated variant below.

**The two businesses in the filing.** The 10-K presents "Machinery, Power & Energy" (MP&E: Caterpillar and subsidiaries
excluding Financial Products) and "Financial Products" (Cat Financial and the insurance subsidiaries) side by side, with
separate balance sheets and cash flows (10-K FY2025, Supplemental Consolidating Data). At 2025-12-31 MP&E held $60.1B of
assets, $11.0B of long-term debt and $17.4B of equity; Financial Products held $41.7B of assets (finance receivables
$17.3B current and $15.5B long-term before eliminations), $33.6B of debt ($5.5B short-term, $7.1B due within a year,
$21.0B long-term) and $4.8B of equity. MP&E's operating cash flow includes the dividends Financial Products paid it
($850M 2021, $475M 2022, $425M 2023, $625M 2024, $500M 2025; Supplemental Data for Cash Flow, footnote 5), so Financial
Products enters owner cash at the cash it sends up, which is how Part IV's equity-method convention counts an investee's
profit (Q4, CONVENTION).

**Owner cash after every real cost, MP&E basis** (MP&E operating cash flow as filed, which adds stock pay back, less stock
pay, less all MP&E capital spending including MP&E's own leased equipment; USD millions; from the supplemental cash-flow
data and the ME&T/MP&E free-cash-flow reconciliations of the five 10-Ks; stock pay from Note 3, "Before tax, stock-based
compensation expense"):

| year | MP&E OCF | stock pay | MP&E capex | **owner cash** | MP&E D&A | depreciation variant | company's "free cash flow" |
|---|---|---|---|---|---|---|---|
| 2021 | 7,177 | 200 | 1,129 | **5,848** | 1,550 | 5,427 | 6,048 |
| 2022 | 6,358 | 193 | 1,298 | **4,867** | 1,439 | 4,726 | 5,777 (adds back $717M IRS settlement) |
| 2023 | 11,688 | 208 | 1,663 | **9,817** | 1,361 | 10,119 | 10,025 |
| 2024 | 11,437 | 223 | 1,988 | **9,226** | 1,368 | 9,846 | 9,449 |
| 2025 | 12,278 | 242 | 2,794 | **9,242** | 1,497 | 10,539 | 9,484 |
| five-year mean | | | | **7,800** | | 8,131 | |

The company's "free cash flow" differs from owner cash by the stock pay, and in 2022 by $717M of "Cash payments related
to settlements with the U.S. Internal Revenue Service", which the company added back (10-K FY2022, ME&T free cash flow
reconciliation). A tax paid is a real cost; it stays in owner cash.

**Consolidated variant** (consolidated OCF less stock pay, less capex, less Cat Financial's equipment leased to others;
the conservative reading, which charges the lease fleet's growth to the owner although it is debt-funded and earns lease
income): 2021 4,526; 2022 4,974; 2023 9,585; 2024 8,597; 2025 7,211; **mean 6,979**. (Consolidated OCF 7,198 / 7,766 /
12,885 / 12,035 / 11,739; capex 1,093 / 1,296 / 1,597 / 1,988 / 2,821; leased 1,379 / 1,303 / 1,495 / 1,227 / 1,465; same
filings.)

Per share, on 459.675M shares: owner cash 2025 $20.11; five-year mean $16.97. Against the price, the mean is a **2.0%**
yield and the 2025 figure 2.4%; the sovereign is 5.66%. The arithmetic is in `Test Runs/_research 2026-10-06 CAT/arith.py`.

**The first half of 2026** (10-Q Q2 2026): sales and revenues $37.958B against $30.818B (+23%); profit $7.769B against
$5.388B; MP&E free cash flow, as the company defines it, $5.698B against $2.575B; repurchases $6.522B of cash paid (7.0M
shares received for $4.9B, the rest ASR advances); $392M of "expected IEEPA tariff recoveries" booked in operating profit
after the Supreme Court ruled the IEEPA tariffs unauthorized on 2026-02-20; backlog $72.1B at 2026-06-30 against $51.2B
at 2025-12-31 and $30.0B at 2024-12-31.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what Caterpillar's machines, engines and finance book will earn, not where the
quote goes, and the test is whether I would hold it "if the market closed for five years" **[M1997-109]**. The price has
roughly doubled in a year (the company itself bought at $385.64 in October 2025 and at $947.20 in June 2026), and a
rise "is never a reason to buy it" **[L2013-007]**. No macro enters **[M2000-094]**: the data-centre build-out, tariffs,
copper and gold prices and interest rates are not forecast here; they enter only as properties of the business, its
cyclicality and its freedom to price **[M2011-054]**. The margin of safety is an attitude here and arithmetic at Q7: a
decision that needs pencil and paper is "too close" **[M1996-084]**. Who is paid to tell you: the company's own outlook
("around the top end of our 5 to 7 percent compound annual growth rate (CAGR) target", 10-K FY2025, MD&A) is a seller's
projection and is not used **[M1995-050]**. **Contrary evidence, written down as found** **[M1997-127]**: (a) the
five-year owner-cash window 2021 to 2025 contains no trough year for a business whose own 10-K calls demand "highly
cyclical" (Critical Accounting Estimates, goodwill); the window flatters the base. (b) The 2025 price realization was
negative $817M overall and negative $1.136B in Construction Industries, the largest segment by sales; a business with
pricing power does not usually give back price in a year of record backlog. (c) Against the castle: the dealer agreements
"are terminable at will by either party primarily upon 90 days written notice" (Item 1). (d) For the castle: backlog
more than doubled in eighteen months and the 2026 first half shows price realization of +$1.0B.

## THE STANDING RULE
Owning this would be a cash purchase sized so that no fall in the quotation forces a sale: no borrowed money **[L2014-005]**,
nothing that lets "the other fellow" call the tune **[M2006-079]**, and "always be sure you can play the next day"
**[M2025-015]**. Caterpillar's own debt and Cat Financial's funding are the target's exposures and are weighed at Q9, not
here. **Clear, as to the buyer's conduct.**

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
*(to be written)*

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
*(to be written)*

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
*(to be written)*

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
*(to be written)*

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
*(to be written)*

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
*(to be written)*

## Q7 — WHAT IS IT WORTH? STOP.
*(to be written)*

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
*(to be written)*

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
*(to be written)*

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
*(to be written)*

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
*(to be written)*

---
## THE BOX
*(to be written)*

## SELF-AUDIT
*(to be written)*

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
*(to be written)*
