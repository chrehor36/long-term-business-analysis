# Company Run — Sumitomo Corporation (TSE: 8053; US OTC ADR: SSUMY) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit b9a6f404). A dispatched blind run under
`Screens/_daily/_dispatch_brief.md`; the brief's one stated departure (the lines of evidence derived by the analyst from the
annual report, not a dispatcher's list) is followed and the lines chosen are named in Step 0. Working folder:
`Test Runs/_research 2026-10-12 SSUMY/` (downloads in `docs/cache/`, gitignored; page dumps of the filed statements in
`docs/`; arithmetic in `scripts/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session (overnight cycle, 2026-10-12), after the run was committed: `PORTFOLIO.md` names no Sumitomo Corporation (8053, SSUMY); not held.*

**Contamination, declared and not used.** (1) The session context showed the last five commit subjects of the repository,
which name another trading house's v5 re-run (MARUY): its box, its deciding question and the wording of its Q1 and Q2 commit
subjects. (2) The auto-memory index loaded into the session mentions a queue state with "Japanese names" owed and a count of
gate-clearers. (3) The git status snapshot listed research-folder names of two other runs (ARCB, AYI). None of these was opened,
searched or used; every judgment below rests on Sumitomo's own documents, the rivals' filings and the v5 ledger. Where my
reasoning reaches a step that resembles what a commit subject said, that is stated at the step. (4) The framework's own text
names an earlier trading-house regression run (MITSY) and quotes **[M2023-031]**, the row on the five Japanese trading houses;
both are governing text and are used only as the framework uses them.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥1,708 a share, Tokyo close 2026-10-09 (the last Tokyo session before this run; 2026-10-12 is a Japanese public
  holiday), Yahoo Finance chart API via `tools/sources.py`, **an aggregator, flagged** (operator rule 5). ADS: **$10.84**,
  SSUMY close 2026-10-12, same aggregator, flagged. USD/JPY 158.68 (same aggregator, 2026-10-12, flagged).
- **The ADS ratio:** one ADS represents one common share: Form F-6EF filed by Citibank, N.A. as depositary, 2026-06-22,
  accession 0001193805-26-000852 ("each American Depositary Share representing the right to receive one common share of
  Sumitomo Corporation"). That filing predates the four-for-one split of 2026-07-01. The ratio after the split is checked
  from the two quotes: ¥1,708 / 158.68 = $10.76 against the ADS at $10.84, so one ADS still carries one (post-split) share;
  the ADS split with the shares. **Ratio used: 1 ADS = 1 share, post-split.**
- **Shares:** one class of common stock. Post-split, as of 2026-06-30: issued 4,780,460,736; treasury 41,613,968;
  **outstanding 4,738,846,768** (Consolidated Financial Results FY2026, three months ended 2026-06-30, "Tanshin", dated
  2026-07-31, section (3) Outstanding stocks; the document restates counts as if the split had occurred at the start of the
  prior year). Cross-check against the audited annual report: Note 20 of the Annual Financial Report for the year ended
  2026-03-31 gives 1,211,426,667 issued and 18,766,168 treasury pre-split; times four, 4,845,706,668 and 75,064,672, which
  are exactly the Tanshin's March figures. Between March and June about 65.2 million post-split shares were cancelled
  (the Tanshin's statement of changes in equity shows a cancellation of treasury stock). A buyback of up to ¥80,000 million
  (up to 88 million post-split shares) runs from 2026-05-07 to 2027-03-31 (AFR Note 35), so the count is falling.
  `python Screens/cover_shares.py SSUMY` returned "NOT AN SEC REGISTRANT in the live ticker file"; the count is by hand.
- **Market cap:** 4,738,846,768 × ¥1,708 = **¥8,094.0 billion** (about $51.0 billion at 158.68).
- **Sovereign for the earnings currency (JPY):** **4.136%**, the 30-year JGB, Japan Ministry of Finance JGB curve
  (`jgbcme.csv`), dated 2026-10-08, via `python tools/sources.py` (issuing authority).
- **Filings read** (operator rule 4; the company is not an SEC registrant, so each document is recorded with its date in
  place of an accession number):
  - Annual Financial Report (English; MD&A and audited IFRS consolidated statements, KPMG AZSA LLC) for the years ended
    2026-03-31 (statements approved 2026-06-12), 2025-03-31, 2024-03-31, 2023-03-31, 2022-03-31, and the Consolidated
    Financial Statements for the year ended 2021-03-31; all from https://www.sumitomocorp.com/en/jp/ir/report/yuka/AnnualFinancialReport .
    The company's "FY2025" is the year ended 2026-03-31; this run uses the company's labels throughout.
  - Integrated Report 2026 (Performance & Data section: the eleven-year Summary of Key Financial Indicators FY2015 to
    FY2025, segment information FY2024 to FY2025), and the data sections of the Integrated Reports 2023, 2024 and 2025.
  - Results presentations for FY2022 (May 2023) and FY2023 (May 2024), which split profit into the company's own
    "Mineral resources" and "Non-mineral resources"; the Q1 FY2026 Tanshin, presentation and scripts (2026-07-31).
  - **One figure cross-checked:** profit attributable to owners of the parent for FY2025, ¥600,334 million in the audited
    Consolidated Statement of Comprehensive Income (AFR, p.86), against ¥600.3 billion in the Integrated Report 2026 summary,
    and against the Tanshin's FY2026 forecast of ¥630,000 million stated as +4.9% (630,000/600,334 = 1.049). Net
    interest-bearing liabilities at 2026-03-31: bonds and borrowings 951,667 + 3,225,446 less cash 1,005,442 and time
    deposits 24,451 = ¥3,147,220 million (AFR balance sheet), matching the Integrated Report's ¥3,147.2 billion and the
    Tanshin's opening figure. They agree.
- `python tools/run.py SSUMY` returned "SSUMY: not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE." No arithmetic
  line was printed; every figure below is by hand from the filed statements (`scripts/owner_cash.py`, inputs transcribed
  from the page dumps `docs/cf_*.txt`).
- **The lines of evidence chosen from the annual report** (the brief's departure): the description of the business groups
  and the reorganization of 2026-04-01 (AFR Note 4 and MD&A section 1), the business risks (AFR section 3, "Risks
  pertaining to mineral resource and gas development/production", commodity, country, credit and liquidity risks), the
  climate-transition disclosures by business (coal, copper, iron ore, aluminium), the MD&A by segment, the segment tables
  (profit, assets, equity-method share) for FY2019 to FY2025, the balance sheets FY2015 to FY2025 (eleven-year summary) and
  FY2019 to FY2025 (statements), the cash-flow statements FY2019 to FY2025, the share and buyback notes, the subsequent
  events (the Ambatovy transfer, the split, the buyback), and the Q1 FY2026 Tanshin for the debt after the aircraft-leasing
  acquisition. Litigation and investigations: the AFR's note says the Companies "are subject, in the ordinary course of
  business, to legal actions and other claims" and that management believes none will have a material adverse effect; the
  risk section (item 9) says the outcome of pending lawsuits cannot be predicted and names none. One regulatory action was
  found (search of the FY2025 AFR for "investigation", "penalt", "lawsuit", "order"): on 2025-12-05 the Financial Services
  Agency issued a business improvement order to Sumisho Realty Management Co., Ltd. ("SRM"), the subsidiary that manages the
  group's REITs, and Sumitomo, "a major provider of properties to the REITs operated by SRM", says it "will further enhance
  its awareness of and attention to conflicts of interest with SRM" (AFR FY2025, risk section 8, footnote 3). Carried to
  AFTER THE STOP under Q5. Stock pay: a restricted performance share unit plan (AFR Notes 3 and 20; 327,300 shares issued
  in FY2025).

**The balance sheets first, eight to ten years of them** (Q4's instruction **[M2025-032]**, read here because the file
closes before Q4). Eleven years from the Integrated Report 2026 summary (¥ billion, years ended March 31; company FY):

| FY | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total assets | 7,817.8 | 7,761.8 | 7,770.6 | 7,916.5 | 8,128.6 | 8,080.0 | 9,582.2 | 10,105.4 | 11,032.6 | 11,631.2 | 13,638.3 |
| Equity (owners) | 2,251.5 | 2,366.5 | 2,558.2 | 2,771.5 | 2,544.1 | 2,528.0 | 3,197.8 | 3,778.7 | 4,445.5 | 4,648.5 | 4,628.6 |
| Net interest-bearing debt | 2,770.3 | 2,627.9 | 2,521.5 | 2,427.1 | 2,468.8 | 2,300.4 | 2,273.7 | 2,484.4 | 2,523.4 | 2,672.5 | 3,147.2 |
| Profit (owners) | 74.5 | 170.9 | 308.5 | 320.5 | 171.4 | -153.1 | 463.7 | 565.3 | 386.4 | 561.9 | 600.3 |
| Operating cash flow | 599.7 | 345.8 | 295.3 | 268.9 | 326.6 | 467.1 | 194.1 | 232.8 | 608.9 | 612.3 | 813.5 |

And from the filed statements, year-ends March 2020 to March 2026 (¥ billion):

| Mar 31 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|
| Revenues (year to) | 5,299.8 | 4,645.1 | 5,495.0 | 6,817.9 | 6,910.3 | 7,292.1 | 7,337.3 |
| Trade receivables, current | 1,231.1 | 1,303.6 | 1,621.9 | 1,679.0 | 1,863.2 | 2,028.2 | 2,413.8 |
| Inventories | 930.0 | 793.3 | 1,058.0 | 1,390.6 | 1,486.8 | 1,653.8 | 1,782.0 |
| Inventories / revenues | 17.5% | 17.1% | 19.3% | 20.4% | 21.5% | 22.7% | 24.3% |
| Equity-method investments | 2,025.3 | 2,102.1 | 2,357.0 | 2,642.5 | 2,857.9 | 3,010.5 | 3,286.8 |
| Intangible assets | 288.9 | 256.0 | 255.0 | 284.8 | 349.8 | 640.7 | 668.4 |
| Bonds and borrowings | 3,189.4 | 2,912.2 | 3,021.4 | 3,152.1 | 3,201.7 | 3,254.7 | 4,177.1 |
| Cash | 710.4 | 599.0 | 733.8 | 656.9 | 667.9 | 570.6 | 1,005.4 |
| Other components of equity | -4.1 | 187.0 | 454.1 | 637.5 | 1,077.0 | 897.9 | 1,255.0 |
| Retained earnings | 2,073.9 | 1,871.4 | 2,269.7 | 2,707.4 | 2,898.1 | 3,297.7 | 3,236.1 |

What moved and why, "what the figures are saying and what they don’t say" **[M2025-032]**: (a) for five years (FY2015 to
FY2019) the balance sheet stood still at about ¥7.8 to 8.1 trillion while profit swung from ¥74.5 billion to ¥320.5 billion
and back; in the six years since, total assets rose 68% and equity 82%. (b) A large part of the equity rise is translation, not
retained profit: other components of equity went from -¥4.1 billion to ¥1,255.0 billion (the AFRs' convenience
translation rate moved from about ¥111 to the dollar at March 2021 to about ¥159 at March 2026, implied by their yen and
dollar columns; the accounting policy note places "Exchange differences on translating foreign operations" in other
components of equity, and FY2025's comprehensive income carries ¥379.4 billion of them). Retained earnings rose ¥1,162 billion over the six years against cumulative profit of ¥2,424 billion; dividends and,
in FY2025, the charge for buying out SCSK's minority took the rest (additional paid-in capital fell from ¥236.1 billion to
nil and retained earnings fell ¥61.6 billion in FY2025 despite ¥600.3 billion of profit). (c) **Inventories rose faster than
sales in every year since FY2020**, from 17.1% to 24.3% of revenues, and current receivables from 28.1% (FY2020) to 32.9%
(FY2025), with the steepest step in FY2025 (+¥385.6 billion of receivables on revenues up 0.6%); the Mineral Resources group's
own receivables and inventories went from ¥555.5 billion to ¥914.2 billion in that year (Integrated Report 2026 segment table)
on segment revenues up 8.7%. A contrary fact, written down as found **[M1997-127]**, carried to AFTER THE STOP under Q4.
(d) Debt was flat for six years and then rose by ¥922 billion in FY2025 and a further ¥566 billion of net debt in the first
quarter of FY2026 (the SCSK buyout, ¥754.2 billion, and the aircraft-leasing acquisition); net debt to equity went from 0.6 to
0.78. (e) About a quarter of total assets are equity-method investments whose own balance sheets are not in this filing.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety as an attitude: Sumitomo's profit has crossed zero twice in
eleven years (¥74.5 billion in FY2015 after resource impairments, a loss of ¥153.1 billion in FY2020), so a buyer must be
"prepared, when you buy a stock, to have it go down 50 percent — or more — and be comfortable with it" **[M2020-022]**, and
"the more volatile the business is [...] the larger the margin of safety" **[M1997-080]**. No macro view enters: the commodity
cycle and the yen are not forecast here **[M2000-094]**, **[M2015-016]**. A share is a business: would I be content to own this
if the market closed for years **[M1997-109]**? That depends on the deciding part, below. Who is paid to tell you: the
company's own documents feature an "underlying profit" that excludes "asset replacement and extraordinary profits/losses"
(AFR MD&A section 1); this run uses the IFRS figures and the cash statements instead. **Contrary evidence, written down as found [M1997-127]:** (1) the swings above; (2) inventories
and receivables outgrowing sales for six years; (3) a nickel venture held for over a decade, written down repeatedly, and
given away in May 2026 with a pre-tax loss of about ¥70 billion (AFR Note 35); (4) the parts table below shows the
deciding part is decided by the two boom years; on the three restated years alone, two other groups each earned more.

## THE STANDING RULE
Owning a marketable part-interest in Sumitomo, bought without borrowed money and sized so a fall of half or more cannot force a
sale, puts the buyer at no risk of ruin; the rule binds the buyer's financing, "never going to risk what we have and need for
what we don’t have and don’t need" **[M2012-081]**; borrowing is "the one thing that ends — or can prevent you from playing
out your hand" **[M2004-065]**, and "anything times zero is zero" **[M2007-050]**, so the position is never held on borrowed
money. The rule is satisfied by conduct, whatever the questions conclude. The target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**; the first question is "can I understand it?" **[M1995-051]**. Sumitomo is a holding
company of 327 consolidated subsidiaries and 192 equity-accounted investees, with 346 and 73 more held through them (AFR FY2025,
risk section (2), "Risks pertaining to business investment"), in ten business groups (eleven reported parts over the
window, reorganized on 2024-04-01 and again on 2026-04-01). Under the framework's holding-company paragraph (a CONVENTION of the
framework, **[M2023-031]** OPEN against it), "a holding company is understood when each part that matters to its earnings can be
understood", and a part matters when it decides under Q2's business-of-parts paragraph: more than half of five-year operating
profit, or else the largest part.

**The parts table** (profit attributable to owners of the parent, ¥ billion; the company's segments as reported; five-year
window FY2021 to FY2025). The segments were reorganized inside the window, so the table is built from the company's own split
into "Mineral resources" and "Non-mineral resources", which it reports in every year of the window (results presentations of
May 2023 and May 2024, Integrated Reports 2025 and 2026), excluding one-off items, plus the restated nine-group segment table
for the three years it covers:

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year | share |
|---|---|---|---|---|---|---|---|
| Mineral resources (excl. one-offs)* | 160 | 209 | 117 | 122 | 99 | 707 | 28% of 2,521 |
| Non-mineral resources (excl. one-offs) | 288 | 343 | 360 | 398 | 425 | 1,814 | 72%, eight to nine segments |
| One-off items, all parts | 7 | 11 | -114 | 47 | 72 | 23 | |
| Corporate and eliminations | 9 | 2 | 24 | -5 | 3 | 33 | |
| Total (rounded by the company) | 464 | 565 | 386 | 562 | 600 | | |

\*Mineral Resources Divisions No.1 and No.2 and the Energy Division until FY2023 (presentation of 2024-05-02, footnote 1);
the Mineral Resources Group and the Gas Value Chain SBU from FY2024 (Integrated Report 2026, footnote 2). The company's
definition changed with its organization; the two definitions are the company's own and are taken as one part, a
**CONVENTION of this run** (rationale: it is the only series the filer itself carries across the reorganization, and the
part's economics, commodity prices and mine costs, are the same on both definitions).

The restated nine-group segment profits for FY2023 to FY2025 (AFR FY2024 Note 4 for FY2023; AFR FY2025 Note 4): Steel 69.2,
68.4, 74.3; Automotive 51.8, 51.2, 63.2; Transportation & Construction Systems 96.2, 101.5, 88.9; Diverse Urban Development
46.5, 77.1, 81.5; Media & Digital -1.0, 45.2, 51.2; Lifestyle -3.7, 14.1, -3.6; Mineral Resources -9.5, 91.1, 82.3; Chemical
Solutions 16.4, 21.4, 26.5; Energy Transformation 84.3, 96.4, 102.4 (one-offs included). No non-mineral segment can reach 707
over five years: the largest three-year sums are Transportation & Construction Systems 286.6 and Energy Transformation 283.1,
and their two earlier years sat inside smaller predecessor units (Transportation & Construction Systems with Automotive, 34.9
and 92.0 in FY2021 and FY2022; Infrastructure 33.3 and 20.8). **No part carries more than half; the largest part, Mineral
resources, decides** (about 28% of five-year profit before one-offs).

*Contrary evidence on the table itself, written down as found* **[M1997-127]**: the part decides on the strength of FY2021 and
FY2022, the commodity-price peak; on the three restated years alone (one-offs included), Mineral Resources earned 163.9
against 286.6 and 283.1 for the two groups above. The convention's five-year rule is applied as written; the sensitivity is
reported under "What in the framework was wrong or unclear".

**The deciding part, read by the tests.** It holds interests in copper mines (Chile and the United States), coking and thermal
coal (Australia), iron ore (South Africa), aluminium, nickel (Madagascar, until the transfer resolved 2026-05-01), LNG and gas
(the Gas Value Chain SBU), and runs a commodity trading business "utilizing commodity derivatives" (AFR Note 4 and MD&A).
- *Key variables and their predictability* **[M1998-044]**: the prices of copper, coking coal, iron ore and LNG; the unit costs
  of the mines; mine lives. Prices are not predictable, and the company says so of copper itself: "Fluctuations in copper prices
  associated with changes in copper demand entail a high degree of uncertainty, making it difficult to calculate the financial
  impact" (AFR FY2025, climate disclosures, copper business). Costs and mine lives are knowable from the operators' reports.
- *The economic dynamics* **[M2011-014]**: a producer of a commodity sold at a world price is understood by where it sits on the
  cost curve: "It’s like comparing a copper producer whose costs are $2.50 a pound with a copper producer whose costs are $1 a
  pound. Those are two different kinds of businesses." **[M2009-059]**. That reading is the framework's own: the commodity
  business and its one exception, the low-cost operator, are Q2's tests, and a business reaches them only if Q1 has passed it.
  The industry is not one of fast-changing technology; its products (copper, coal, ore) are the same in ten years.
- *How far off could I be* **[M2011-084]**: very far on the part's earnings (from a loss in FY2020 for the unit that held it,
  -¥63.7 billion, to ¥266.9 billion in FY2022 and back to a segment loss of ¥9.5 billion in FY2023); not far on what kind of
  business it is.
- *Abroad: governance and tax* **[M2000-141]**: a Japanese company reporting under IFRS in English with an audited annual
  report; the governance and tax are readable; the rows ask a lower price, not a pass, for a less familiar country **[M2006-021]**.
- *Doubt* **[M2002-092]**: the doubt I hold is about the part's castle and its earnings, which are Q2's and Q7's questions; I do
  not doubt what the part is or how its economics work.
- *The open tension* **[M2023-031]**: the speakers bought five Japanese trading houses as businesses "that we could understand as
  a group, although it didn’t mean we had deep understanding on any". By the framework's convention on a row about named
  companies, it is weighed, never a verdict alone; it does not decide this Q1, and the by-parts reading governs.
- *Contamination note:* a commit subject seen in the session context described another trading house's Q1 as IN on a mineral
  deciding part "understood by cost position". I reached the same reading from **[M2009-059]**, **[M2011-014]** and the
  framework's placement of the commodity tests in Q2; I did not open that run.

**VERDICT: IN.** The deciding part, Mineral resources, is understood by its economics: a set of interests in commodity mines and
a commodity trading book, whose ten-year earning power turns on its cost position against the industry's, which is knowable,
and on prices, which no one knows and which belong to the castle and value questions **[M2012-065]**, **[M2011-014]**,
**[M2009-059]**. Filing fact: AFR FY2025 Note 4 and the business descriptions; the company's resource/non-resource split.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years from
now. What are the key factors? And how permanent are they?" **[M1995-038]**. The file closes on the deciding part, Mineral
resources (Q1's parts table), under the framework's business-of-parts convention; the other parts are not judged here.

**What the part sells, and to whom.** Copper, coking and thermal coal, iron ore and manganese, aluminium, LNG and gas, and
commodity trading "utilizing commodity derivatives" (AFR FY2025 Note 4); the Integrated Report 2026 adds "we leverage derivatives
to capture price differentials across markets and time horizons". These are standard products bought at a world price. The
commodity mark in the rows is the buyer's indifference, "most insureds don't care from whom they buy" **[L2004-003]**, and the
business whose price is set outside it is the one the gas-station row describes, "whatever he charged for gas was my price"
**[M2012-109]**. The company's own account of the part's year confirms that the price is the market's: "Coal business in
Australia: profit declined due to a drop in coal prices and a decrease in coking coal sales volume"; "Iron ore mining business in
South Africa: decline in prices"; "Copper business: profit increased due to increasing prices" (AFR FY2025, MD&A, segment remarks).

**How the part earns.** Mostly as a minority owner: equity-method profit was ¥60.8 billion of the group's ¥82.3 billion in FY2025
and ¥63.1 billion of ¥91.1 billion in FY2024 (AFR FY2025 Note 4). The interests the company names: Quebrada Blanca (copper,
Chile; "started operation in 2023", Integrated Report 2024), Morenci (copper, United States), Cerro Verde (copper, Peru), Clermont,
Oaky Creek and Hail Creek (coal, Australia), Assmang (iron ore and manganese, South Africa, through Oresteel Investment),
Mineracao Usiminas (iron ore, Brazil), Press Metal's aluminium smelters (Malaysia), and, until May 2026, Ambatovy (nickel,
Madagascar, 54.17%) (Integrated Reports 2024 and 2026, Mineral Resources Group pages; AFR FY2025 Note 35).

**The castle tests, each with its filing fact.**
1. *The commodity business and its one exception, the low-cost operator.* "commodity businesses have risk unless you’re the
   low-cost producer, because the low-cost producer can put you out of business" **[M1997-010]**; "when a company is selling a
   product with commodity-like economic characteristics, being the low-cost producer is all-important" **[L2000-017]**; and the
   copper case in the speakers' own words: "It’s like comparing a copper producer whose costs are $2.50 a pound with a copper
   producer whose costs are $1 a pound. Those are two different kinds of businesses. One is going to go broke at a buck-fifty a
   pound." **[M2009-059]**. **Filing fact: Sumitomo discloses no unit cost, cash cost or cost-curve position for any producing
   interest** (search of the FY2025 AFR and the Integrated Report 2026 for "cost curve", "quartile", "cash cost", "unit cost":
   no instance). Its cost claims are qualitative: the thermal coal interests "produce high-grade coal, which is in relatively high
   demand, and are cost-competitive" (AFR FY2025, coal disclosure), the business it plans to take to zero equity production in
   the late 2020s; the coking coal and iron ore interests produce "high-grade" material, a quality claim and not a cost claim; the
   group lists "Highly competitive and high-potential business assets" among its strengths and "rising development and
   operational costs" among its risks (Integrated Report 2026, Mineral Resources Group page).
2. *The high-cost producer's end* **[L1994-035]**, **[M2001-013]**, in the part's own record: the unit that held the part lost
   ¥63.7 billion in FY2020, the filing citing lower coal prices and volumes, the suspension in Madagascar, "and recording
   impairment loss of ¥84.8 billion" (AFR FY2020 MD&A); the Madagascar nickel venture was then impaired by ¥88.7 billion in FY2023
   and ¥18.9 billion in FY2024 (the segment notes of the AFRs for those years), and transferred in May 2026 with expected pre-tax
   losses of about ¥55 billion and ¥15 billion, offset largely by tax effects (AFR FY2025 Note 35). That asset is gone; whether
   what remains is low-cost is not shown.
3. *Pricing power and the agony before a rise* **[M2005-020]**: the part takes the world price; its profit moved with prices in
   both directions inside the window (above), which is the commodity's behaviour, not a franchise's.
4. *Unit volume and share of mind* **[M1999-054]**: the filing facts on volume are a "decrease in coking coal sales volume" in
   FY2025 and the plan to take thermal coal equity production to zero in the late 2020s (AFR FY2025).
5. *The money test* **[M2011-015]**: in a commodity the attacker is new supply. The company says new copper supply is hard to
   bring on, citing "the depletion of operating mines, the difficulty of developing new mines, and the strengthening of
   environmental protection regulations" (AFR FY2025, copper disclosure); that protects the price for every producer, not this
   one's place among them.
6. *Would the customer still choose it over the low bid* **[M2017-009]**: no; a tonne of copper or coking coal of a given grade
   is bought at the market price. The grade premium in coking coal and iron ore is the one product difference the filings name.
7. *Widening or narrowing* **[M1999-108]**: the part is changing shape: nickel exited, thermal coal run off, copper the growth
   area through "new interests through investment in overseas copper mines" (AFR FY2025). Its return on invested capital, on the
   company's own definition, was 12% in FY2024 and 10% in FY2025, with 10% forecast for FY2026; invested capital ¥840 billion,
   ¥970 billion and ¥990 billion (forecast) (Integrated Report 2026, Mineral Resources Group page).
8. *What could destroy, modify or reduce it* **[M2000-014]**: the company names the decline of coal and iron ore demand with
   decarbonization, a tailings dam failure at its iron ore and copper interests, and host-government action, "changes to tax
   regimes, confiscation of business assets and infringements of rights" (AFR FY2025, climate, natural-capital and risk sections).
9. *Ask the competitors* **[M1999-130]**: not done; the company names no competitor (search of the FY2025 AFR for "competitor",
   "competition", "trading compan": antitrust policy text and two segment remarks on "intensified competition" in steel and
   automotive only).

**The competitor row.** The company names no rivals. Compared against: the four SEC filers among the large producers of the same
commodities, two of which operate mines in which Sumitomo names interests (Freeport-McMoRan for Morenci and Cerro Verde, Teck
Resources for Quebrada Blanca; that they operate them is the general record, not read in this run's documents, and their
mine-level reports were not read). Not read and not SEC filers: the other Japanese trading houses, which Sumitomo does not name.
Metric: profit attributable to owners over total assets (Freeport: profit including non-controlling interests, the annual profit
tag it files), from each filer's own annual report via SEC XBRL company facts (`competitor_row.txt`), fiscal years 2019 to 2025:

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2021-25 mean | accession (latest filing) |
|---|---|---|---|---|---|---|---|---|---|
| BHP (20-F, June years) | 8.2% | 7.5% | 10.4% | 32.5% | 12.8% | 7.7% | 8.3% | 14.3% | 0001193125-25-185641 |
| Rio Tinto (20-F) | 9.1% | 10.0% | 20.5% | 12.8% | 9.7% | 11.2% | 7.8% | 12.4% | 0001628280-26-009531 |
| Freeport-McMoRan (10-K) | -0.5% | 2.1% | 11.2% | 8.8% | 7.1% | 8.0% | 7.1% | 8.4% | 0000831259-26-000012 |
| Teck Resources (40-F) | -1.5% | -2.1% | 6.1% | 6.3% | 4.3% | 0.9% | 3.1% | 4.1% | 0000886986-26-000004 |
| Sumitomo, the part (company FY) | 2.7% | -3.8% | 9.0% | 10.7% | -0.7% | 6.1% | 3.3% | 5.7% | AFRs FY2020 to FY2025, Note 4 |

The Sumitomo line is the reporting unit that held the part in each year: Mineral Resources, Energy, Chemical & Electronics (profit
¥43.2, -63.7, 247.3 and 266.9 billion on segment assets of ¥1,595.8, 1,662.6, 2,747.4 and 2,490.1 billion) for FY2019 to FY2022,
and the Mineral Resources Group (¥-9.5, 91.1 and 82.3 billion on ¥1,284.6, 1,493.9 and 2,463.7 billion) from FY2023. The bases
differ: the earlier unit also held chemicals and electronics, and the group's FY2025 assets include ¥914.2 billion of trading
receivables and inventories. The row is read in words, not to the decimal.

**The field's returns over the last full cycle, judged in words.** The cycle inside the window runs from the trough of FY2020
through the price peak of FY2021 and FY2022 to the trough of FY2023. Over it the two largest iron ore and copper producers earned
on their assets about twice what Sumitomo's part earned; the copper producer whose new mine's start-up weighed on it (Teck) earned
about what Sumitomo's part earned; the operator of two of Sumitomo's copper interests (Freeport) earned in between. The part lost
money in two of the seven years, as Teck and Freeport did in the deep trough. The part is therefore not shown to be the low-cost
operator, and not shown to be a high-cost one either: its returns sit in the middle of the field and below its best members, on a
basis that favours neither side cleanly. A castle shown open on the evidence (the framework's Q2 wording) would need the cost facts the company does not
publish; a castle shown standing would need them as much.

**Why the box is TOO HARD, and which cause.** "when we see a moat that’s tenuous in any way — getting back to your question —
it’s just too risky. We don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**; a castle whose future
cannot be judged goes to the "too hard" pile **[M2006-013]**. The cause is **WORK**. The deciding question, whether the remaining
producing interests sit low on their industries' cost curves and will for ten to twenty years, is "important and knowable"
**[M2006-076]**: the operators of those mines publish unit costs, reserves and mine lives in their own annual reports, and none
was read in this run. "I haven’t done the work and I’m not sure if I did the work I would understand them." **[M1994-026]**. It is
not NATURE on the present evidence, because the castle question for a commodity producer is the cost position, which insiders
write down, not the future price, which they do not (the company's own sentence on copper prices, quoted at Q1, bears on value,
not on the castle). Two findings could turn the pass to NATURE, and step 1 below names them: a remaining portfolio whose results
through a trough cannot be read from any filing (the framework credits a change for the better only on a full cycle, and sends
the question to TOO HARD (NATURE) until then), and a derivatives trading book whose condition cannot be read from outside.

*Contamination note:* a commit subject seen in the session context put another trading house's Q2 at TOO HARD (NATURE). This run's
cause differs and rests on the reasoning above; nothing of that run was read.

**VERDICT: TOO HARD (WORK)** on the deciding part: a commodity seller with no disclosed cost position, a long and costly record in
one high-cost asset now given away, and full-cycle returns in the middle of its field; whether its remaining interests are
low-cost producers is knowable from the operators' filings and was not read **[M1997-010]**, **[M2009-059]**, **[M2000-019]**,
**[M1994-026]**. The file closes here; Q3 to Q12 are NOT REACHED.

## Q3: NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.
## Q4: NOT REACHED. The balance sheets were read in Step 0; facts found are under AFTER THE STOP.
## Q5: NOT REACHED. Integrity facts found are under AFTER THE STOP and flagged in the box line.
## Q6: NOT REACHED. Facts found are under AFTER THE STOP.
## Q7: NOT REACHED. The owner's reporting figures are computed below, headed COMPUTATION, NOT A CLEARANCE.
## Q8: NOT REACHED.
## Q9: NOT REACHED. Facts found are under AFTER THE STOP.
## Q10: NOT REACHED.
## Q12 (optional): NOT REACHED. One fact found is under AFTER THE STOP.

---
## THE BOX
**TOO HARD (WORK) at Q2**, on the deciding part (Mineral resources, about 28% of five-year profit before one-offs): whether its
remaining producing interests are low-cost producers is knowable from the operators' filings and was not read; a research pass
is opened below (steps 1 and 2 written, not run). **Integrity facts recorded, not judged** (the regulator's business improvement
order to the REIT-management subsidiary, 2025-12-05; under Q5 below). Q7 not reached; the owner's reporting figures are a
computation only: central value range ¥899 to ¥1,594 a share against ¥1,708 (COMPUTATION, NOT A CLEARANCE).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found* **[M1997-127]**; *no verdict; the box is unchanged (operator rule 2).*

**Bearing on Q3 (capital).**
- Company-wide return on invested capital, on the company's own definition, 8% in FY2024 and FY2025 on invested capital of ¥8,670
  billion and ¥9,440 billion (Integrated Report 2026 segment table); ROE 16.2%, 16.2%, 9.4%, 12.4%, 12.9% for FY2021 to FY2025 and
  3.2% to 12.5% in FY2015 to FY2019 (eleven-year summary).
- Owner cash before purchases (operating cash flow less property and investment-property spending net of sales, net loans, lease
  repayments and dividends to minority holders) averaged ¥309.2 billion a year over FY2021 to FY2025 against average profit to
  owners of ¥515.5 billion; after net purchases of businesses and investments (including the SCSK minority buyout) it averaged
  ¥66.6 billion (`scripts/owner_cash.py`). The gap: working capital absorbed ¥104.5 billion a year and "Other, net" ¥65.9 billion
  a year inside operating cash flow; the equity-method share of profit (¥1,145.3 billion over the five years) exceeded all
  dividends received (¥983.7 billion, which also include dividends from other investments).
- Property, plant and equipment bought: ¥105.9 billion in FY2025 against depreciation and amortization of ¥227.6 billion, which
  includes right-of-use and intangible amortization (AFR FY2025 cash-flow statement).

**Bearing on Q4 (the accounts).**
- Inventories rose from 17.1% of revenues (FY2020) to 24.3% (FY2025) and current receivables from 28.1% to 32.9%; FY2025's
  receivables rose ¥385.6 billion on revenues up 0.6% (Step 0 table).
- FY2025 operating cash flow of ¥813.5 billion includes ¥577.8 billion from the increase in trade payables; the MD&A describes
  the year only as "Steady cash generation by core businesses" (AFR FY2025, cash-flow table).
- The company features "underlying profit", which excludes "asset replacement and extraordinary profits/losses" (AFR MD&A
  section 1), and publishes an annual profit forecast: ¥630.0 billion for FY2026, including "an additional buffer of JPY 30.0
  billion" (AFR FY2025). Record against forecasts and targets: the FY2025 target of ¥600.0 billion, stated in May 2023 ("we aim
  to achieve a profit of ¥600.0 bil. in FY2025", FY2022 results presentation), was met at ¥600.3 billion; the FY2023 forecast of
  ¥500.0 billion (announced February 2024) was missed at ¥386.4 billion, while the same forecast excluding one-off items
(¥500.0 billion) was met at ¥501.0 billion; the FY2024 forecast of ¥530.0 billion was exceeded at ¥561.9 billion (FY2023
  results presentation; AFRs).
- About a quarter of total assets are equity-method investments (¥3,286.8 billion at March 2026) whose own accounts are not in
  the filing.

**Bearing on Q5 (integrity, flagged in the box line).**
- On 2025-12-05 the Financial Services Agency issued a business improvement order to Sumisho Realty Management Co., Ltd., the
  subsidiary that manages the group's REITs; Sumitomo, "a major provider of properties to the REITs operated by SRM", states it
  "takes this matter very seriously" and "will further enhance its awareness of and attention to conflicts of interest with SRM"
  (AFR FY2025, risk section 8, footnote 3). The filing does not state the conduct the order addressed beyond this; the order
  itself was not read.
- The Madagascar nickel venture was carried through impairments in FY2020, FY2023 and FY2024 before its transfer in May 2026;
  in May 2024 the company wrote "We are implementing a turnaround plan while considering all options available" (FY2023 results
  presentation).
- Directors' remuneration ¥1,339 million in FY2025, ¥1,204 million in FY2024 (AFR FY2025, Note 28); a restricted performance
  share unit plan whose evaluation items include non-financial indicators (AFR FY2025, human capital section).

**Bearing on Q6 (the money and the owners).**
- Purchases: the SCSK minority buyout, ¥754.2 billion in cash (FY2025, financing activities); acquisitions of businesses ¥271.7
  billion in FY2024 (mainly Net One Systems by SCSK, per the MD&A); Sumisho Air Lease, about ¥330 billion, closed April 2026
  (Q1 FY2026 presentation). All paid in cash: no all-stock deal was found in the window, so Q6's STOP would not arise.
- Policy: "a total payout ratio of 40% or higher" and a "progressive dividend payment" (AFR FY2025 section 1(3)); dividend ¥150
  a share for FY2025 (pre-split; ¥37.5 post-split) and ¥40 forecast for FY2026 (post-split).
- Buybacks, net: ¥37.9 billion (FY2022), ¥32.1 billion (FY2023), ¥50.0 billion (FY2024), ¥80.0 billion (FY2025); the current
  programme sets a maximum amount (¥80 billion) and share count (88 million post-split) and no price (AFR Note 35). FY2025's
  treasury shares rose from 1,092,736 to 18,766,168 pre-split (70.7 million post-split) for net ¥80.0 billion, about ¥1,132 a
  post-split share on average (an upper estimate, since some treasury shares were also issued for share pay). **The Q6 line from
  the Q7 computation** (headed COMPUTATION, NOT A CLEARANCE, not weighed): that average sits above the bottom of the central
  computed range, ¥899.
- The stated plan to restore "financial soundness to the level prior to the execution of major investments (as of the end of
  FY2024)" by FY2028 "through accelerated asset replacement" (AFR FY2025 section 1).

**Bearing on Q9 (debt and exposures).**
- Net interest-bearing debt ¥3,713.5 billion at 2026-06-30 (net D/E 0.78), up from ¥3,147.2 billion at March; lease liabilities a
  further ¥516.4 billion. At March 2026, short-term debt ¥489.6 billion and current maturities of long-term debt ¥462.1 billion;
  some loan agreements carry financial-ratio and net-worth covenants and lender-requested prepayment clauses (AFR FY2025 MD&A (9)).
- Guarantees ¥252.0 billion (continuing through 2044); financing commitments ¥894.4 billion (AFR FY2025).
- A commodity derivatives trading business inside the deciding part, run "within well-defined position limits and loss limits"
  (AFR FY2025, market risk); marketable equity exposure ¥213.7 billion.

**Bearing on Q12.** Thermal coal equity production to be taken to zero by the end of the 2020s; coal-fired power generation to be
ended "by the late 2040s" (AFR FY2025, policy on coal-related businesses). No business on the framework's named list was found.

---
## THE OWNER'S REPORTING FIGURES: COMPUTATION, NOT A CLEARANCE
*The file closed at Q2. These figures are the reporting convention of the brief and of Part VII, computed under Q7's range
convention; they carry no entry language and are not a verdict (operator rule 3). Arithmetic: `scripts/owner_cash.py`,
`scripts/q7_computation.py`, output in `q7_output.txt`.*

**Inputs.** Owner cash from the audited cash-flow statements, FY2021 to FY2025, after the company's own income tax (taxes paid sit
inside operating cash flow; the floor's "pre-tax" is read as before the holder's tax, Q7, Whose tax), with equity-method income
counted as the dividends actually received (the framework's convention). All property and investment-property spending is
deducted, net loans, lease repayments (so lease liabilities are left out of net debt, said so) and dividends to minority holders.
The all-equity basis adds back net interest paid after tax (**CONVENTION of this run:** at 31.0%, "The applicable income tax rate in
Japan" in the AFR's tax reconciliation, FY2025 Note 30; rationale: the framework names the basis and not the rate). The company's
average effective tax rate was 7.4% in FY2025 and 12.5% in FY2024 (same note), low because equity-method profit is booked after
the investees' own tax. Five-year averages
(¥ billion a year): before purchases 309.2 (equity basis) and 329.7 (all-equity); after net purchases 66.6 and 87.1.

**The specifics, in order.**
- *PG specifics:* growth measured on aggregate owner cash (not per share); all spending deducted (the filing allows no maintenance
  guess: no maintenance figure is disclosed and depreciation of ¥227.6 billion includes right-of-use and intangible amortization,
  so specific (e) leaves the all-spending case central); zero growth after year ten; a price above the top closes OUT.
- *(a) Cycles:* the literal window FY2021 to FY2025 is used. Its owner cash swings with working capital (−¥125.4 billion,
  −¥324.5 billion, −¥182.1 billion, −¥128.0 billion, +¥237.7 billion by year); the filer does not describe either end year as
  aberrational, so the base is not moved; the working-capital-free figure is shown beside (D).
- *(b) Decline:* not applicable (the shown growth is positive).
- *(c) Acquisitions:* net purchases over the window were ¥1,213.0 billion against owner cash before purchases of ¥1,546.0 billion:
  more than half, so **the serial-acquirer rule makes the organic pair central** (purchases left out). The filer reports no organic
  growth rate (search of the FY2025 AFR for "organic": the plan's words "Organic initiatives" and "organic growth" in the eight
  growth areas, no rate); **CONVENTION of this
  run:** the organic pair's growth end uses the growth the cap below allows, since no organic figure exists; rationale: specific (c)
  presumes a reported organic rate, and the cap is the framework's own fallback. The default pair (purchases deducted, total growth)
  is shown beside (C). The aircraft-leasing deal closed after the window (April 2026): its financing is in the June net debt and no
  earnings of it are credited (Sumitomo has filed none for it; Air Lease Corporation's own filings were not read); shown beside with
  the deal excluded both ways (E). No signed, unclosed deal was found.
- *(d) Working capital:* counted in the central case.
- *(e) Growth spending:* see the PG line; the all-spending case is central.
- *(f) The cap:* growth between the halves of the window (FY2021-22 against FY2024-25) is 74.4% a year, which carried ten years
  would put owner cash far above the highest share of sales it has reached (8.4% in FY2025); it is cut to the business's own sales
  growth, 7.5% a year (revenues ¥5,495.0 billion to ¥7,337.3 billion, FY2021 to FY2025), and that, being above the discount rate,
  is cut again to **4.136%**, "never above the discount rate". Both cuts are written down here.
- *The floor tested first:* at ¥1,708 the expected return is 2.8% on the no-growth case and 4.0% on the growth case; no case in the
  central range earns about ten percent, which by itself would close OUT (computation only). *The width:* 1.77 to 1.

**(a) VALUE RANGE (central: all-equity basis, organic pair, net debt ¥3,713.5 billion at 2026-06-30):**
**¥899 to ¥1,594 a share** (enterprise value ¥7,971 billion to ¥11,268 billion at 4.136%), **$5.66 to $10.05 per ADS**
(1 ADS = 1 share, ¥158.68), against **¥1,708** (Tokyo close 2026-10-09, aggregator) and **$10.84** per ADS (2026-10-12, aggregator).

**(b) FAIR PRICE** (each end case valued at ten percent, the two averaged, less net debt; Part VII): **¥26 a share, $0.16 per ADS**
on the all-equity basis (the central figure); **¥759 a share, $4.78 per ADS** on the equity-only basis (owner cash after interest,
¥309.2 billion a year, against the shares alone), shown beside and never deciding alone. The two differ because net debt of ¥3.7
trillion takes nearly all of the value of ¥329.7 billion a year capitalized at ten percent.

**Beside the central figure** (per share; per ADS at 158.68):

| case | range at 4.136% | fair price |
|---|---|---|
| B. equity-only basis | ¥1,578 to ¥2,230 ($9.94 to $14.05) | ¥759 ($4.78) |
| C. default pair (purchases deducted, total growth capped) | ¥-339 to ¥-155 | ¥-570 |
| D. working capital removed | ¥1,431 to ¥2,347 ($9.02 to $14.79) | ¥282 ($1.78) |
| E. aircraft-leasing deal excluded both ways (net debt at March 2026) | ¥1,018 to ¥1,714 ($6.42 to $10.80) | ¥145 ($0.92) |

The inventory-secured trade finance convention does not apply: Sumitomo's borrowings are general bank loans and bonds, not notes
secured by inventory and repaid as it is sold (AFR FY2025 MD&A (9)); the whole of net debt is counted.

---
## RESEARCH PASS FOR THE TOO HARD (WORK): steps 1 and 2 (written, not run)
*Part VII's form, with the refinements of 2026-10-05: each OUT answer one fact; span and source fixed now; an unanswerable question
recorded and set aside; the pass closes IN, OUT or TOO HARD (NATURE), never TOO HARD (WORK) again on this question **[M2008-086]**.
"What do I not know that I need to know?" **[M1999-129]**; the reading aims "to possibly reject your original hypothesis"
**[M1998-144]**.*

**Step 1: the list (each marked knowable or not).**
1. *Which interests make the part's profit?* The split of Mineral resources profit by interest or business line (copper, coking
   coal, iron ore and manganese, aluminium, gas value chain, trading) for FY2021 to FY2025. Knowable (Sumitomo's quarterly results
   supplements and presentations).
2. *Where does each main interest sit on its industry's cost curve?* For every interest carrying more than a tenth of the part's
   FY2024-FY2025 profit: its unit cash cost and its position against its industry. Knowable (the operators' annual reports).
3. *How long do the main interests last?* Proven and probable reserves against annual production for the same interests.
   Knowable (the operators' reserve statements).
4. *Did the portfolio that remains earn through the trough?* The remaining interests' results in FY2020 and FY2023, excluding the
   exited nickel venture and the thermal coal run-off. Knowable only if a filing gives business-level results for those years;
   if not, unanswerable, and by the framework's rule on a change for the better the question goes to TOO HARD (NATURE).
5. *Can the trading book be read?* The commodity derivatives trading business's size, limits and losses, FY2021 to FY2025.
   Knowable in part (market-risk disclosures); if its condition cannot be read from outside, the readable half does not make the
   unreadable half readable **[M2002-094]**, and the pass closes TOO HARD (NATURE).

**Step 2: for each question: the evidence, its span and source, and the single fact that closes OUT.**
1. Evidence: profit by business inside Mineral resources. Span FY2021 to FY2025. Source: Sumitomo's results presentations and
   supplementary materials for those years (company IR library). Closes OUT: none by itself (a sizing question); it fixes which
   interests questions 2 and 3 read.
2. Evidence: unit cash cost per pound or tonne for each main interest and the operator's statement of its industry position.
   Span: calendar 2021 to 2025 (the whole span, never one year). Sources: Freeport-McMoRan's 10-K for Morenci and Cerro Verde;
   Teck Resources' annual reports and 40-F for Quebrada Blanca; the annual reports of the other owners or operators of Assmang,
   Mineracao Usiminas, the Australian coking coal joint ventures and the Malaysian smelters. Closes OUT: **the interest carrying
   the largest share of the part's FY2024-FY2025 profit has unit cash costs in the upper half of its industry's curve, on its
   operator's own statement, in a majority of the five years.** A margin comparison, if used, covers the whole span; a capital test,
   if used, sets earnings after depreciation against capital employed, or cash earnings against capital spending, never one against
   the other.
3. Evidence: reserves and annual production. Span: the latest reserve statements (2025). Sources: as in 2. Closes OUT: **the
   interest carrying the largest share of the part's profit has proven and probable reserves of less than ten years of current
   production.**
4. Evidence: business-level results in FY2020 and FY2023. Sources: Sumitomo's results presentations for those years. Closes OUT:
   **the remaining interests in aggregate lost money in FY2020 or FY2023 before impairments of exited assets.** If no filing gives
   the figure: recorded as unanswerable with the search that failed; the close then goes to TOO HARD (NATURE) on the change-for-
   the-better rule.
5. Evidence: trading results and limits. Span FY2021 to FY2025. Sources: the AFRs' market-risk sections and the results
   presentations. Closes OUT: **a trading loss in any year that the company attributes to its positions and that exceeds that
   year's trading profit in the best year of the span.** If unreadable: TOO HARD (NATURE).

**How step 4 closes.** IN if the interests making more than half of the part's profit are in the lower half of their cost curves
(question 2), last beyond ten years (3), earned through the trough (4), and the trading book is readable and none of the OUT facts
holds (5); the run then continues from Q2 to Q3. OUT on any single OUT fact. TOO HARD (NATURE) if question 4 or 5 is unanswerable,
or if the pass ends unsure **[M2002-092]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit b9a6f404); written question by question; committed after Q1 (677bf77c)
      and Q2 (5111b45a) and at the close.
- [x] Dispatched: the brief allowed the per-question commits; the lock in `Screens/_daily/` was present (held by the dispatching
      session, not touched by this run); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared at the top:
      the commit subjects of another trading house's run, a memory line, two research-folder names. Not used.
- [x] Every v5 id resolves (`scripts/check_ids.py`: no E-ids, no missing id; the fragments it flags are the company's own quoted
      words, each attributed to its document in parentheses, and one framework phrase marked as such). Every filing fact carries
      its document and date (the company files no accession numbers; the rivals' accessions are in the competitor row).
- [x] The order was kept; Q2 closed the file; nothing after it is a clearance; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy; the sovereign from the Ministry of
      Finance; aggregator quotes flagged.
- [x] Contrary evidence written down as found (foundations, Step 0, the parts table, Q2); facts for later questions under AFTER THE
      STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` and `Screens/cover_shares.py` returned no arithmetic (not an SEC registrant); nothing they print was used.
- [x] `python tools/check_framework.py` PASS before each commit.
- Confessed conventions of this run: the company's two "Mineral resources" definitions taken as one part (Q1); the 31.0% rate for
  the after-tax interest add-back; the organic pair's growth end set by the cap where no organic rate is reported.
- What could not be got: the mines' unit costs and reserves (the research pass); a business-level split of the part's profit;
  Air Lease Corporation's earnings attributable to Sumitomo's share; the regulator's order itself; a maintenance capital figure.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The parts rule across a reorganization.** The business-of-parts convention measures five-year operating profit
by part, but Sumitomo reorganized its segments in April 2024 (and again in April 2026), so no segment series covers the window. I
used the company's own resource/non-resource split, the only series it carries across the change, and confessed it. The rule is
also sensitive to the window's peak: the deciding part decides on FY2021 and FY2022, the commodity peak; on the three restated
years alone, Transportation & Construction Systems (286.6) and Energy Transformation (283.1) each earned more than Mineral
Resources (163.9), and the first of those holds the leasing businesses, which would have sent the file to Q1's bank and finance
tests instead. The framework does not say whether an aberrational window year, which Q7's specific (a) moves, should also move the
parts table; I applied the rule as written. (2) **Specific (c) presumes a reported organic growth rate.** The serial-acquirer rule
makes the organic pair central, with "organic growth as the filer reports it", and Sumitomo reports none; I confessed a
convention (the cap's fallback). (3) **The all-equity basis for a trading house.** Net debt of ¥3.7 trillion finances trade
receivables, inventories and lease assets whose returns are inside owner cash; the floor-plan convention covers only inventory-
secured notes, so the whole of net debt is counted and the central fair price falls to ¥26 against ¥759 on the equity-only basis.
The framework is clear on what to do; whether it measures what it means for a trading or leasing balance sheet is a question it
does not ask. (4) **WORK or NATURE for a commodity producer.** The two causes are clear in principle, but the change-for-the-better
rule (a portfolio reshaped by exits is credited only on a full cycle) can turn a knowable cost question into NATURE after the
reading; I wrote that path into step 1 rather than closing NATURE now.
