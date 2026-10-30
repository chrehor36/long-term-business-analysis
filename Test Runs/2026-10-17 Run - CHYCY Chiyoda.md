# Company Run: Chiyoda Corporation (Tokyo Stock Exchange: 6366; OTC ADR: CHYCY), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its source (for this filer, a document title,
date and URL in place of an accession number: see the departures below); a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. Copied from the template to this dated name before any fetch.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (0178a77b): not held; `PORTFOLIO.md` has no line for CHYCY, Chiyoda or 6366.*

**Dispatched run.** Run by a dispatched analyst under `Screens/_daily/_dispatch_brief.md` with the brief's two stated
departures: (1) the filer files no 10-K, 20-F or 40-F with the SEC (CIK 0001442657 carries ADR forms only), so the primary
documents are the company's own, from https://www.chiyodacorp.com/en/ir/ ; (2) the lines of evidence are derived by the
analyst from the company's own business description, stated risks and management's discussion.

**Lines of evidence chosen (departure 2), and from which document.**
1. The business and its parts: "Consolidated Financial Results for the Fiscal Year Ended March 31, 2026" (Kessan Tanshin,
   abridged English translation, unaudited, dated 2026-05-11), section 1(1) and 1(3) and section 4 "Contracts and Sales"
   (new orders, backlog and net sales by field, domestic and overseas, major clients);
   https://www.chiyodacorp.com/en/ir/assets/2025Q4_Tanshin_E.pdf
2. The stated business risks: the same document, section 1(5) "Business Risks", items (a) to (k).
3. Management's discussion of results, financial position and strategy: the same document, sections 1(2) and 1(3); the
   CHIYODA REPORT 2025 (integrated report; cited by PDF page, each PDF page a two-page spread: CEO message PDF page 5;
   Business Plan 2025 strategy PDF pages 14-15; roundtable PDF page 19), https://www.chiyodacorp.com/en/ir/assets/CR2025_E.pdf
4. The capital history: CHIYODA REPORT 2019 (cited by PDF page: profile PDF page 2; "New Capital Structure" PDF page 7; FY2018 losses PDF page 11),
   https://www.chiyodacorp.com/en/ir/assets/AR2019_r_1.pdf ; the "Notice of Agreement regarding the redemption plan of
   Class A Preferred Shares and Partial Amendment to Articles of Incorporation", 2026-01-28,
   https://www.chiyodacorp.com/en/ir/assets/20260128-1_E_r1.pdf
5. The latest position: "Consolidated Financial Results for Three Months ended June 30, 2026" (dated 2026-08-03),
   https://www.chiyodacorp.com/en/ir/assets/2026Q1_Tanshin_E.pdf
6. The span: the full-year Kessan Tanshin for every fiscal year from the year ended 2016-03-31 to the year ended 2026-03-31
   (eleven documents, each listed in the table under Step 0 by its release date), all at
   https://www.chiyodacorp.com/en/ir/library/settlement/

The annual securities report (yuho) for the year ended 2026-03-31, filed 2026-06-18 on EDINET in Japanese, was **not read**
(see What I could not get). The Kessan Tanshin is unaudited by its own statement; one figure was cross-checked against the
audited English statements (Step 0).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** JPY 617, Tokyo close 2026-10-16 (ticker 6366.T); ADR CHYCY USD 4.06, close 2026-10-16. Both from Yahoo
  Finance through `tools/sources.py` `price()`, **an aggregator, flagged** (operator rule 5: live quotes only). ADR ratio:
  one ADR represents one common share (Form F-6 POS, Deutsche Bank Trust Company Americas, filed 2017-09-29, accession
  0001193805-17-002847). The two quotes imply about JPY 152 to the dollar; the Tokyo price is the one used.
- **Shares by class**, from the latest filing after the preferred acquisition ("Consolidated Financial Results for Three
  Months ended June 30, 2026", dated 2026-08-03, section "Notes" (4)):
  - Common: 260,324,529 issued less 1,141,064 treasury (of which 691,909 held by the officer-pay BIP trust) =
    **259,183,465 outstanding**.
  - Class A preferred (unlisted, held by Mitsubishi Corporation): 175,000,000 issued in 2019 at JPY 400 (JPY 70,000
    million), less 110,400,000 acquired and cancelled on 2026-06-30 at JPY 499.2 each (JPY 55,111,680,000; FY2025 Tanshin,
    subsequent-events note, pages 21-22; 1Q FY2026 Tanshin, "Notes to Significant Changes in Shareholders' Equity") =
    **64,600,000 remaining**. Under the articles as amended on 2026-06-24 (the 2026-01-28 notice), each is redeemable for
    JPY 436 plus accumulated unpaid dividends (JPY 63.2 at 2026-06-30 by the FY2025 Tanshin's note), carries a 3% dividend
    on JPY 400 until 2028-06-30 and 12% compound from 2028-07-01, and converts into common at a JPY 100 conversion price
    only from 2029-07-01. The notice states Mitsubishi "holds approximately 33% of our voting rights, which will increase
    to about 82% after the exercise of conversion rights into common shares" (that figure was for all 175,000,000).
    Redemption claim of the remaining shares at 2026-06-30: 64,600,000 x JPY 499.2 = **JPY 32,248 million**.
  - `python Screens/cover_shares.py CHYCY` returned "NOT AN SEC REGISTRANT in the live ticker file"; the count above is
    by hand from the filing, issued less treasury, every line shown.
- **Market cap:** 259,183,465 x JPY 617 = **JPY 159,916 million** (common only). With the preferred redemption claim:
  JPY 192,164 million.
- **Sovereign for the earnings currency (JPY):** **4.02%**, the 30-year JGB, Japan Ministry of Finance official curve
  (`jgbcme.csv`), dated 2026-10-15, fetched by `python tools/sources.py` on 2026-10-17.
- **Filings read** (operator rule 4; no accession numbers exist for these, so title, date and URL are recorded): the
  documents listed under the lines of evidence above, and the eleven full-year Tanshin of the table below.
  **One figure cross-checked against the filed statement:** profit attributable to owners of parent for the year ended
  2025-03-31, JPY 26,987 million, and total net assets at 2025-03-31, JPY 25,456 million, in the FY2024 Tanshin (dated
  2025-05-08) and in the FY2025 Tanshin's comparative column, agree with the audited "Consolidated Financial Statements
  FY2024" (English, scanned; Consolidated Statement of Changes in Equity, report page 06),
  https://www.chiyodacorp.com/en/ir/assets/CFSFY2024_E.pdf . The same audited page shows 175,000 thousand preferred shares
  outstanding at 2025-03-31.
- `python tools/run.py CHYCY` returned: "CHYCY: not an SEC filer. Use the evidence ladder: company IR site (English),
  exchange filings (TDnet / RNS / SEDAR+). This is UNRESEARCHED, not UNKNOWABLE." No arithmetic lines were printed; every
  figure below is by hand from the filed statements (scripts and extraction in `Test Runs/_research 2026-10-17 CHYCY/`).

### The span, as filed (JPY millions; fiscal years end 31 March; "FY2025" is the year ended 2026-03-31, the company's own label)
Source: each year's full-year Kessan Tanshin (release dates: 2016-05-12, 2017-05-12, 2018-05-11, 2019-05-09, 2020-05-08,
2021-05-07, 2022-05-10, 2023-05-09, 2024-06-26, 2025-05-08, 2026-05-11). Borrowings are short-term loans, the current
portion of long-term borrowings and long-term borrowings. "Advances" are "advances received on uncompleted construction
contracts" to March 2021 and "contract liabilities" from March 2022 (a change of accounting standard; the line name changes
with it). Capex is purchase of property, plant and equipment plus purchase of intangible assets.

| FY | Net sales | Operating profit | Pre-tax | Net income (owners) | Equity (owners' ref.) | Cash and deposits | Borrowings | Advances | Op. cash flow | Capex |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2015 | 611,548 | 16,015 | 14,460 | 3,375 | 200,166 | 137,715 | 10,347 | 135,667 | 55,526 | 2,607 |
| FY2016 | 603,745 | 15,680 | (26,368) | (41,116) | 155,339 | 135,373 | 10,211 | 85,187 | (4,375) | 2,100 |
| FY2017 | 510,873 | (12,330) | 4,867 | 6,445 | 157,557 | 96,008 | 10,000 | 76,294 | (34,115) | 2,594 |
| FY2018 | 341,952 | (199,795) | (194,181) | (214,948) | (60,114) | 69,457 | 15,988 | 122,252 | (37,941) | 2,253 |
| FY2019 | 385,925 | 26,789 | 19,050 | 12,177 | 24,423 | 124,404 | 35,869 | 119,911 | (32,217) | 2,262 |
| FY2020 | 315,393 | 7,015 | 8,876 | 7,993 | 36,399 | 106,988 | 45,747 | 74,784 | (20,806) | 2,149 |
| FY2021 | 311,115 | 10,545 | (9,258) | (12,629) | 15,654 | 68,795 | 45,621 | 143,431 | (25,591) | 2,139 |
| FY2022 | 430,163 | 18,116 | 20,829 | 15,187 | 22,180 | 61,241 | 29,090 | 163,347 | 44,157 | 2,784 |
| FY2023 | 505,981 | (15,006) | (6,159) | (15,831) | 4,858 | 102,072 | 23,600 | 188,701 | 62,747 | 3,886 |
| FY2024 | 456,969 | 24,421 | 32,386 | 26,987 | 23,705 | 153,340 | 23,599 | 217,390 | 51,175 | 4,022 |
| FY2025 | 493,942 | 82,102 | 92,474 | 84,663 | 113,855 | 145,203 | 22,397 | 190,815 | 26,132 | 2,346 |
| 2026-06-30 | (quarter) 86,763 | 4,716 | 6,191 | 5,508 | 64,058 | 169,668 | 2,397 | 185,277 | n/a | n/a |

Sums over the eleven years: net sales JPY 4,967,606 million; operating profit **JPY (26,448) million** (a margin of
about minus 0.5%); pre-tax **JPY (43,024) million**; net income to owners **JPY (127,697) million**; income taxes charged
JPY 83,518 million. Shareholders' equity of JPY 206,395 million at 2015-03-31 (FY2015 Tanshin) became JPY (60,114) million
at 2019-03-31; JPY 70,000 million of preferred shares were issued in FY2019 ("Proceeds from issuance of shares 70,000",
FY2019 Tanshin cash flow statement); net assets per common share were negative from 2019-03-31 to 2025-03-31 (JPY (211.23)
at 2025-03-31) and JPY 128.56 at 2026-03-31 (each year's Tanshin, page 1).

**The balance sheets, read first** (Q4's rule, read here because the file may close before Q4) **[M2025-032]**, "balance
sheets over an 8 or 10 year period". What moved and why:
- **Equity** was wiped out once (FY2018, the Cameron LNG and Tangguh LNG losses, CHIYODA REPORT 2019, PDF pages 7 and 11)
  and nearly a second time (JPY 4,858 million at 2024-03-31, after the FY2023 Golden Pass loss). It was rebuilt by JPY 70,000
  million of preferred capital from Mitsubishi Corporation, a capital reduction that moved retained earnings from
  JPY (127,778) million at 2020-03-31 to JPY 15,708 million at 2021-03-31 on a year's net income of JPY 7,993 million (FY2020
  Tanshin balance sheet), and the FY2025 profit. After the 2026-06-30 preferred purchase, equity is JPY 64,058 million.
- **Cash** is mostly customers' money. Advances or contract liabilities (JPY 185,277 million at 2026-06-30) exceed cash and
  deposits (JPY 169,668 million) at the latest date and at every March from 2022. The cash rises and falls with the
  advances: cash fell from JPY 137,715 million (2016) to JPY 69,457 million (2019) while advances fell and losses were paid,
  and rose to JPY 153,340 million (2025) as contract liabilities rose to JPY 217,390 million.
- **Receivables and work in progress against sales:** the largest asset is "jointly controlled assets of joint venture"
  (JPY 164,960 million at 2026-06-30, against quarterly sales of JPY 86,763 million), Chiyoda's share of the JV balance
  sheets of the large projects; the filing does not break it down. "Short-term loans receivable" of JPY 100,010 million at
  2026-03-31 fell to JPY 9 million at 2026-06-30, the quarter in which JPY 55,111 million went to the preferred purchase and
  the JPY 20,000 million subordinated loan was repaid early (1Q FY2026 Tanshin, section 1(2)).
- **Debt** was never large in borrowings (peak JPY 45,747 million, 2021-03-31) and is JPY 2,397 million after the early
  repayment; the senior claim that mattered was the preferred (JPY 32,248 million remaining).
- **Retained earnings** are not a record of retained profit: they passed through a deficit of JPY (139,956) million
  (2019-03-31) and a capital reduction.
- **Provision for loss on construction contracts** stood at JPY 3,288 million (2018-03-31), JPY 67,637 million
  (2019-03-31), JPY 28,379 million (2025-03-31) and JPY 5,580 million (2026-03-31); its fall of JPY 22,799 million in FY2025
  is named by the filer as part of the year's profit ("due to the revision of GPX project profitability", FY2025 Tanshin,
  section 1(1)).
- **What the figures do not say:** the profit of each field (LNG, refinery, pharmaceutical, domestic); the filer reports one
  segment, "Engineering", and omits segment detail (FY2025 Tanshin, segment note). What they cannot say: the outcome of the
  open lump-sum contracts (Golden Pass Trains 2 and 3; North Field East) before completion.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the first: a share is a business, and the test is whether I would be content to
own it with the market closed, "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**.
The stock's own history (net assets per common share negative for seven year-ends) makes the second foundation bear too:
the price "just tells us prices" and the question is whether it is out of line with where the facts lead **[M2006-077]**.
No macro view enters; the Middle East suspension of the Qatar project is treated as a fact in the filing, not a forecast,
since "macro conclusions are" to "just never enter into the discussion" **[M2000-094]**. Who is paid to tell me: the
company's own medium-term plan figures are management's projections and are not used as evidence of earning power
**[M1995-050]**; their past projections are set beside them, as that row asks. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the company's own statement that on large LNG projects "we had limited competition and Chiyoda's
excellent track record gave us a strong advantage" (CHIYODA REPORT 2025, PDF page 19), evidence for a castle, recorded at Q2;
(2) the FY2025 result (operating profit JPY 82,102 million, equity restored to JPY 113,855 million) and management's claim of
"transitioning to a stable profit structure" (FY2025 Tanshin, section 1(3)), evidence for a change, weighed at Q2;
(3) net cash as filed of about JPY 167,271 million at 2026-06-30 against a common market value of JPY 159,916 million,
recorded in the COMPUTATION; (4) the 2019 plan said equity would return "to over 20% by fiscal 2023 by acquiring steady
profits totaling approximately ¥90 billion in the five years from fiscal 2019" (CHIYODA REPORT 2019, PDF page 7); the
filed net income for FY2019 to FY2023 sums to JPY 6,897 million and the equity ratio at 2024-03-31 was 1.1%, recorded under
AFTER THE STOP.

## THE STANDING RULE
Owning a part-interest in this company, bought for cash without borrowing and sized so that its loss to zero could be borne,
does not put the buyer at risk of ruin; the rule binds the buyer's conduct, "Never risk permanent loss of capital."
**[L2023-005]**, and the company's own record (equity wiped out in FY2018) is a reason to size any position as if a total
loss were possible, "what can really go wrong with this place" **[M2012-081]**. No leverage is contemplated.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the
  industry" **[M2011-014]**.
- **What the business is, from its own filing.** An EPC contractor: "The Chiyoda Group continues to execute Engineering,
  Procurement and Construction (EPC) projects in fields such as Liquefied Natural Gas (LNG)/Refinery/Petrochemical
  worldwide" (FY2025 Tanshin, section 1(1)); one reportable segment, "Engineering" (segment note). LNG plants were 58.4% of
  FY2025 net sales (JPY 288,394 million of 493,942) and 51.8% of the year-end backlog (JPY 316,783 million of 613,056);
  overseas 71.1% of sales; two clients took 55.6% of sales (QatarEnergy 30.7%, Golden Pass LNG 24.9%) (FY2025 Tanshin,
  section 4). Its own account of its economics: "The majority of our major overseas projects to date have been lump sum
  contracts of a significant scale [...] This resulted in an earnings structure in which the contract amount and profit and
  loss of each project heavily influenced our financial results." (CHIYODA REPORT 2025, PDF page 15); "Under previously
  dominant lump-sum contracts*, contractors take on significant risks related to unforeseeable external factors such as
  rising material costs." (same, CEO message, PDF page 5).
- **The key variables and whether they are foreseeable** **[M1998-044]** ("evaluating how predictable they were"):
  (1) the award of a few very large LNG contracts, set by clients' investment decisions; (2) the margin finally realised on
  each fixed-price contract, which is set at the bid and revealed at completion. The second has run from an operating loss
  of JPY 199,795 million (FY2018) to an operating profit of JPY 82,102 million (FY2025), and management guides JPY 10,000
  million for FY2026 (FY2025 Tanshin, section 3). Test 3 asks whether the past statements tell the future ones
  **[M2008-033]**: for an individual contract, no; for the economic character of the business, yes, because eleven years of
  statements show the same pattern repeated (losses in FY2016, FY2017 at the operating line, FY2018, FY2021 and FY2023).
- **Routing.** The industry does not change fast; LNG liquefaction plants are built today much as in the 2010s, and Q1's
  TOO HARD routing for fast change **[M1998-008]** does not apply. What cannot be foreseen is the outcome of individual
  fixed-price contracts, not the economics of the trade: a contractor bidding fixed prices against other qualified
  contractors and carrying the cost risk. I judge those economics legible from the filings, and their verdict is a castle
  question, so it is taken at Q2. The doubt rule **[M2002-092]** ("if you have doubts about something being into your circle
  of competence") was put to this: my doubt is about the contracts' outcomes, which is the castle's failure, not about what
  kind of business this is. The insiders do write their forecasts down **[M2000-105]**; their record of meeting them is set
  out under AFTER THE STOP.
- **VERDICT: IN.** The economic dynamics of the industry can be understood from the filings **[M2011-014]**, **[M2012-065]**;
  the unforeseeable contract outcome is carried to Q2 as the central castle fact. (The alternative routing, TOO HARD
  (NATURE) at Q1 on the unforeseeable margin, is recorded under What in the framework was wrong or unclear.)

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. A moat is what "protects excellent returns on invested capital"
**[L2007-004]**.

**The parts table.** The filer reports one segment and no profit by field (FY2025 Tanshin, segment note), so the share of
five-year operating profit by part, which the business-of-parts convention uses, cannot be computed. **CONVENTION of this
run:** the parts are ranked by net sales, the only measure the filer gives by field; rationale: the convention's fallback
("where no part does, the largest part decides") needs a measure, and sales is the only one filed.

| Part (filer's field) | FY2025 net sales, JPY m (share) | Year-end backlog (share) | Castle | Decides |
|---|---|---|---|---|
| LNG plants (overseas lump-sum and risk-sharing EPC) | 288,394 (58.4%) | 316,783 (51.8%) | open on the evidence below | **yes** (more than half of sales and of backlog) |
| Environment, new energy, infrastructure | 60,634 (12.3%) | 100,657 (16.4%) | not judged separately (no profit filed) | no |
| Refinery and petrochemical | 65,822 (13.3%) | 126,520 (20.6%) | not judged separately | no |
| Pharmaceutical, biochemistry, chemical | 64,016 (13.0%) | 36,605 (6.0%) | not judged separately | no |
| Gas-related, others, other business | 15,074 (3.0%) | 32,488 (5.3%) | not judged separately | no |

Management calls the domestic work "achieving stable earnings" (CHIYODA REPORT 2025, PDF page 14; domestic was 28.9% of FY2025
sales) but files no profit for it; it does not decide on any measure filed.

**The castle tests, each with its filing fact.**
1. *What keeps it standing, and how permanent* **[M1995-038]**: the reason clients come is the record, "having completed
   over 300 projects across 60 countries and regions worldwide" (FY2025 Tanshin, section 1(3)); in 2019 "around 40% of the
   world's total LNG plant capacity" (CHIYODA REPORT 2019, PDF page 2); and on large LNG projects "we had limited competition and
   Chiyoda's excellent track record gave us a strong advantage" (CHIYODA REPORT 2025, PDF page 19). That is a real barrier to
   entry. But the test is what it protects, and over the span it protected a cumulative operating loss (Step 0 table).
2. *The money test* **[M2011-015]** ("could I do it?"): an attacker does not need to displace Chiyoda; the large LNG jobs of
   the span were awarded to consortia of the same few contractors, often Chiyoda with its rivals as partners: McDermott and
   Chiyoda 50/50 on Cameron LNG, McDermott/Zachry/Chiyoda on Freeport Train 3 (McDermott 10-K for 2018, filed 2019-02,
   accession 0001564590-19-003980, joint-venture note); JGC, KBR and Chiyoda on Ichthys (CHIYODA REPORT 2019, PDF page 9,
   "(JGC, KBR, Chiyoda)"); Technip Energies on North Field East, McDermott on Golden Pass (CHIYODA REPORT 2025,
   PDF page 15). Rivalry with few players is not a castle: "you can have only two competitors and they’re still terrible
   businesses" **[M2013-052]**.
3. *Pricing power, and the agony before a rise* **[M2005-020]**: the price is fixed at the bid; cost increases are recovered
   only by renegotiation after the loss (Tangguh, "Negotiations with the clients regarding the schedule and costs are still
   underway", CHIYODA REPORT 2019, PDF page 11; Golden Pass, amended EPC contracts in November 2024 and November 2025 after the
   withdrawal of the JV partner Zachry, FY2025 Tanshin, sections 1(1) and 1(3)). The company states that contractors under
   lump-sum terms "take on significant risks related to unforeseeable external factors such as rising material costs"
   (CHIYODA REPORT 2025, PDF page 5). No pass-through of cost is shown.
4. *Unit volume and share of mind*: new orders JPY 298,024 million in FY2025 (up 41.1%) after JPY 211,260 million in FY2024;
   backlog JPY 613,056 million, down 17.1%; new orders in the quarter to 2026-06-30 JPY 30,992 million, down 76.7% (FY2025
   and 1Q FY2026 Tanshin). The volume is a few contracts, and the company is choosing to take fewer large LNG ones (test 10).
5. *The low-cost position* **[M1997-010]** ("the low-cost producer can put you out of business"): no filing read shows
   Chiyoda as the low-cost contractor. Its own account of the Cameron loss is the reverse: "A substantial amount of
   unanticipated additional work occurred in the final phase of construction of Cameron Train 1. In addition, worker
   productivity was low due to a continuously high worker turnover rate." (CHIYODA REPORT 2019, PDF page 11).
6. *Would the customer still choose it over the low bid?* **[M2017-009]** ("people buying candy for the low bid"): the
   contracts are bid. A rival's filing says how the bids are won: "our bidding, while designed to enhance the probability of
   winning the contracts in a competitive market, included estimates about costs and timing that, in hindsight, were at
   times too optimistic" (Fluor 10-K for 2019, accession 0001628280-20-013900, Special Committee findings). Chiyoda's own
   sales staff on the work it is now moving toward: "Small- and medium-scale projects, on the other hand, are extremely
   challenging, with more competition and a more demanding market in terms of price and other requirements." (CHIYODA
   REPORT 2025, PDF page 19). The customer here is the one who buys on the bid, the commodity mark: "most insureds don't care
   from whom they buy" **[L2004-003]**.
7. *Ask the competitors* (test 9): their own filings answer. KBR: "management approved strategic business restructuring
   activities and decided to discontinue pursuing certain projects, principally lump-sum EPC and commoditized construction
   services" (KBR 10-K for 2021, accession 0001357615-22-000012). McDermott, Chiyoda's partner on Cameron LNG and Golden
   Pass, recorded "unfavorable changes in estimates of $815 million on the Cameron LNG project" (10-K for 2018, accession
   0001564590-19-003980) and filed for Chapter 11 on 2020-01-21 (10-K for 2019, accession 0001564590-20-007841). Fluor's
   Special Committee tied its losses to "our customers' migration toward lump-sum contracts" and "a larger percentage of
   high-risk lump-sum contracts" (10-K for 2019, accession 0001628280-20-013900).
8. *Is the moat widening or narrowing?* **[M1999-108]** ("how wide the moat is"): narrowing by the company's own plan. The
   one place it described limited competition, the extra-large LNG lump-sum contract, is the place it is leaving: "we will
   fundamentally reform our business structure, reduce reliance on large-scale projects, and transition to a diversified
   portfolio combining multiple medium-scale projects" (CHIYODA REPORT 2025, PDF page 5), toward the work its own staff
   describe as having "more competition" (test 6).
9. *What could destroy, modify or reduce it* **[M2000-014]** ("destroy, or modify, or reduce the economic strengths"): one
   or two contracts. The FY2018 net loss of JPY 214,948 million exceeded the whole equity of JPY 157,557 million at the
   start of that year; FY2023's Golden Pass loss took equity to JPY 4,858 million. The partner risk is stated by the filer:
   "the Group may bear contractual joint responsibility" if a partner defaults (FY2025 Tanshin, risk (c)), as happened when
   Zachry withdrew from Golden Pass in May 2024 (CHIYODA REPORT 2025, PDF page 15).

**The commodity business and its exception.** Q2's commodity paragraph asks whether the business is the low-cost producer,
read from its own and its operators' filings **[M1997-010]**; no filing shows that it is (test 5), and the rivals' filings
show the field's bids won on optimistic costs (test 6). The exception does not apply.

**The competitor row** (same metric from the competitors' own filings, over the whole span; USD millions for the rivals,
from SEC XBRL companyfacts of each 10-K, earliest-filed value for each year, accessions in
`Test Runs/_research 2026-10-17 CHYCY/rivals.txt`). **The company names no competitors** in the documents read; it names
partners (McDermott, Technip, Zachry; JGC and KBR in 2019). **CONVENTION of this run:** the comparison set is McDermott and
KBR (named by the company as partners in the same LNG EPC field and SEC filers) and Fluor (an SEC-filing EPC contractor
taking lump-sum energy work, not named by the company); rationale: the brief allows up to three SEC filers and the company
names none as rivals. **Flagged, not SEC filers:** JGC Holdings, Technip Energies, Zachry (private), Bechtel (private).

| Company | Span | Net income summed over the span | Owners' equity, start to end | Note from its own filing |
|---|---|---|---|---|
| Chiyoda (JPY m) | FY2015 to FY2025 | (127,697) | 206,395 (2015-03) to 113,855 (2026-03), after JPY 70,000 of new preferred | equity negative at 2019-03 |
| McDermott | 2015 to 2019 (last 10-K) | (5,401) | 1,487 to (2,143) | Chapter 11, 2020-01-21 |
| Fluor | 2016 to 2025 | 678 (of which 2,145 in 2024; the other nine years sum to (1,467)) | 3,125 (2016) to 3,244 (2025) | losses 2019, 2020, 2021 and 2025 |
| KBR | 2015 to FY ended 2026-01 | 1,720 | 1,065 to 1,503 | left lump-sum EPC in 2020 |

**The field's returns over the last full cycle, judged in words.** The span from FY2015 to FY2025 holds two of Chiyoda's own
peaks and its trough, and the rivals' same years. The contractors that stayed in large fixed-price energy EPC earned, on
the evidence of their own filings, losses or nothing over the decade: Chiyoda a cumulative operating loss on JPY 5 trillion
of sales and a cumulative net loss of more than half of its starting equity, McDermott bankruptcy, Fluor three loss years in
a row and equity no higher than where it began. The one rival with a respectable decade, KBR, got it by leaving lump-sum EPC.
That is not a castle protecting "excellent returns" **[L2007-004]**; it is the field the rows call terrible even with few
players **[M2013-052]**, where "one competitor is frequently enough to ruin a business" **[M2012-108]**.

**The change for the better, weighed.** The company claims a change: FY2024 and FY2025 profits, the redemption of most of the
preferred, and a new order policy toward "Risk Sharing Type" and "Reimbursable (cost plus fee)" contracts (CHIYODA REPORT
2025, PDF page 15). Q2 credits a change for the better only on a full cycle **[M2017-026]**, **[L1995-022]**. Two facts settle
how it bears here. First, the FY2025 profit is named by the filer as coming from "the revision of GPX project profitability"
on a contract taken before the change, and the company guides operating profit down 87.8% for FY2026 (FY2025 Tanshin,
sections 1(1) and 3). Second, and decisive: the change claimed is a change of risk, not of castle. By the company's own
account the work it is moving toward has "more competition and a more demanding market in terms of price" (CHIYODA REPORT
2025, PDF page 19), so even if the new policy succeeds through a full cycle, it moves the business from a field with few
players and ruinous fixed-price risk to a field with more players and price competition. No version of the claimed change,
proven or not, describes a barrier that protects excellent returns; the question the change-for-the-better rule would hold
open is therefore not the deciding one, and the file does not wait on it.

- **Why OUT and not TOO HARD.** The castle's future is not unknowable: its past is filed for eleven years, alongside three
  rivals', and it shows the barrier (few qualified contractors) protecting losses, not returns. A castle shown open on the
  evidence closes OUT **[M2011-015]**, **[M2006-013]** ("in, out, and too hard"); "A moat that must be continuously rebuilt
  will eventually be no moat at all." **[L2007-005]**; and price does not reopen it, "turn any investment into a good deal by
  paying little" being what cannot be done **[M2019-015]**, **[L2014-009]**. The tenuous-moat row sends a castle to TOO HARD
  for a reason that does not apply when the returns are known **[M2000-019]** ("tenuous in any way").
- **VERDICT: OUT.** The deciding part (LNG EPC, more than half of sales and backlog) has no castle that protected returns over
  the full cycle on its own and its rivals' filings; the customer buys on the bid; the company is leaving the one niche with
  limited competition for a more competitive one **[L2007-004]**, **[M2013-052]**, **[M1997-010]**, **[L2004-003]**.
  **The file closes here.** Q3 to Q12 are NOT REACHED; everything after this line that carries a number is headed
  COMPUTATION, NOT A CLEARANCE.

## Q3: HOW MUCH CAPITAL MUST GO IN. WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks when the file closes before Q4.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. Integrity facts found are under AFTER THE STOP and flagged in the box line.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. WEIGHING.
NOT REACHED. (The buyback test needs the bottom of a Q7 range that was not reached as a clearance; the company bought no
common stock in the span read.)

## Q7: WHAT IS IT WORTH. STOP.
NOT REACHED as a clearance. The two reporting figures the owner asked for follow, under the protocol's heading.

### COMPUTATION, NOT A CLEARANCE
Built by Q7's range convention as written (five-year window, its six specifics, the floor tested first, the literal window
beside), from the filed cash flow statements; every line is in `Test Runs/_research 2026-10-17 CHYCY/computation.txt`
(script `scripts/compute.py`). JPY millions unless per share. No verdict and no entry language attaches to any figure here
(operator rule 3).
- **Owner cash.** All-equity basis: operating cash flow, less interest and dividends received, plus interest paid, less
  purchases of property, plant, equipment and intangibles; equity-only: operating cash flow less the same capex. Taxes are
  the company's own, as paid inside operating cash flow. **CONVENTION of this run:** interest and dividends received are
  taken out of all-equity owner cash because the cash that earns them is counted in net cash; rationale: counting both
  would credit the same cash twice. Capex (JPY 2,100 to 4,022 million a year) is close to depreciation (JPY 2,816 to 3,727
  million), so the maintenance case (e) and the all-spending case do not differ materially; no acquisitions of size were
  made in the span (c). Working capital is inside operating cash flow (d).
- **The window and its ends (a).** The literal five years FY2021 to FY2025 sum to JPY 131,554 million (average 26,311).
  Both end years are aberrational on the filer's own description: FY2021 carried "Extraordinary losses of 20,374 million
  yen [...] related to the ICHTHYS LNG project" (FY2021 Tanshin, section 1(1)); FY2025's profit was "due to the revision of
  GPX project profitability" (FY2025 Tanshin, section 1(1)), with FY2026 guided 87.8% lower. The base is therefore the last
  full cycle of owner cash, peak to peak: owner cash peaked at JPY 51,466 million in FY2015 and JPY 56,830 million in FY2023;
  the cycle FY2016 to FY2023 averages **JPY (9,527) million** a year (FY2015 to FY2022 beside: JPY (10,197) million; the
  eleven years FY2015 to FY2025: JPY 3,356 million). Only one full cycle lies in the span read, so growth between
  successive cycles cannot be measured, and by (b) the range is the no-growth case alone, said so.
- **What the literal window holds.** JPY 98,923 million of the window's JPY 131,554 million of owner cash is the increase in
  contract liabilities (customers' advances) on the cash flow statements (FY2021 65,506; FY2022 14,536; FY2023 22,603;
  FY2024 22,500; FY2025 (26,222)). Its growth, measured between halves because the end years change sign (b), is 67.8% a
  year; carried ten years that would need owner cash far above the highest share of sales earned (11.2%, FY2023), so by (f)
  it is cut to sales growth over the window (12.3%), and no rate above the discount rate (4.02%) is carried.
- **Net cash and claims, at the latest filed date (2026-06-30).** Cash and deposits 169,668 plus investment securities 4,365
  less borrowings 2,397 = net cash **171,636**; no finance leases are shown separately; operating leases left out. Senior to
  the common: the remaining Class A preferred at its redemption claim, **32,248** (**CONVENTION of this run:** the preferred
  is counted as a debt-like claim at the amended articles' cash redemption price; rationale: the company and the holder have
  agreed to redeem it for cash by June 2028, and it cannot convert before July 2029); non-controlling interests at book,
  2,188. Market value of the common 159,916; enterprise value on the all-equity basis **22,717**.
- **Range, central (all-equity, cycle base, no growth alone):** value of operations at the sovereign 4.02% = JPY (236,984)
  million; per common share **JPY (385)**. The floor is tested first: no case of the central range earns the floor at the
  price, the expected return on the operations being negative (JPY (9,527) million against an enterprise value of JPY
  22,717 million); by the convention this case is OUT whatever the width, "drop out of the game" **[M2003-149]**. The width
  test does not arise.
- **Beside, the literal window:** no-growth JPY 3,055 a share, growth (4.02% for ten years, then none) JPY 4,070 a share;
  its fair price JPY 1,705. These rest on a window in which three quarters of owner cash was customers' advances rising and
  both end years are aberrational on the filer's word; they are shown because the convention requires the literal window
  beside, and they are the strongest figures in the name's favour.
- **Beside, the eleven-year average** (JPY 3,356 million): value JPY 851 a share, fair JPY 659.
- **Beside, cash netted for customers' money.** Contract liabilities exceed receivables, contract assets and costs on
  contracts in progress by JPY 140,226 million at 2026-06-30. **CONVENTION of this run (beside only):** that excess deducted
  from net cash; rationale: it is cash received for work not yet done, whose cost will draw it down, and the cycle-base
  average does not show that outflow. Central value JPY (926) a share, central fair JPY (379); eleven-year value JPY 310.
- **Beside, the preferred converted instead of redeemed** (from 2029-07-01 at JPY 100, with unpaid dividends of about
  JPY 150 by then, a rough figure): about 355 million new common shares, 614 million in all; central fair on that count
  JPY 121 a share.
- **Tax.** Over the eleven years the company charged JPY 83,518 million of income taxes against a cumulative pre-tax loss
  of JPY (43,024) million (Step 0 table), so the cycle base is not flattered by a tax shelter; the carryforward balances
  (yuho tax note) were not read, and the statutory-rate adjustment of Q7's Whose tax was not computed for the literal
  window, whose tax rate was 22.9% (JPY 29,839 million on JPY 130,272 million of pre-tax).
- **Reporting figure (a), the VALUE RANGE:** central **JPY (385) a share** (no-growth case alone, cycle base, all-equity),
  against a price of **JPY 617** (ADR USD 4.06). Literal window beside: JPY 3,055 to 4,070.
- **Reporting figure (b), the FAIR PRICE** (Part VII: each end case valued at ten percent, averaged; here one case): **JPY 162
  a share on the all-equity basis** (operations valued at ten percent, JPY (95,268) million, plus net cash, less the
  preferred claim and minority interests); **equity-only JPY (462)** (owner cash after interest, cycle base JPY (8,538)
  million, at ten percent, less the preferred claim and minority interests). The all-equity figure is the central one. The
  all-equity fair price exceeds the central value at the sovereign only because a negative cash stream valued at ten
  percent is a smaller negative; both sit below the price. No cheap price is reported.

## Q8 to Q12
NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q2** (the deciding part, LNG EPC, has no castle that protected returns over FY2015 to FY2025 on its own
and its rivals' filings; the company is moving from its one limited-competition niche to work it calls more price
competitive). COMPUTATION beside, not a clearance: central value JPY (385) a share, fair price JPY 162 (all-equity), against
JPY 617. **Integrity facts recorded, not judged** (Part VII): see AFTER THE STOP, Q5.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).

**Q3 (capital).** Fixed capital is small: property, plant and equipment JPY 9,703 million and intangibles JPY 5,142 million
at 2026-06-30 on quarterly sales of JPY 86,763 million (1Q FY2026 Tanshin). The capital at risk is the equity buffer
against fixed-price contract losses: the FY2018 loss of JPY 214,948 million exceeded the opening equity of JPY 157,557
million (Step 0 table). Management's own targets for FY2025 to FY2027 include "Gross Margin: 10% or greater (3-year
average)" and a net profit of JPY 15 billion a year on average (FY2025 Tanshin, section 1(3)).

**Q4 (the accounts).** The Kessan Tanshin are unaudited by their own statement; the yuho was not read. Revenue is recognised
on contracts over time, and the year's profit moves with the provision for loss on construction contracts (JPY 3,288
million, 2018-03; JPY 67,637 million, 2019-03; JPY 28,379 million, 2025-03; JPY 5,580 million, 2026-03), which the filer
names as a cause of the FY2025 profit. The largest asset, "jointly controlled assets of joint venture" (JPY 164,960 million
at 2026-06-30), is not broken down in the documents read. The FY2023 results were dated 2024-06-26 and the annual securities
report filing date given as 2024-07-01, later than the May results and June filings of the other years read (FY2023
Tanshin, page 1); the cause was not read. A capital reduction in FY2020 moved retained earnings from a deficit to a surplus
(Step 0). No EBITDA or adjusted figure was seen featured in the documents read.

**Q5 (the people), integrity facts recorded, not judged.** (1) The 2019 Revitalization Plan stated: "we expect to return the
shareholders' equity ratio to over 20% by fiscal 2023 by acquiring steady profits totaling approximately ¥90 billion in the
five years from fiscal 2019" (CHIYODA REPORT 2019, PDF page 7). Filed net income for FY2019 to FY2023 sums to JPY 6,897
million, and the equity ratio at 2024-03-31 was 1.1% (FY2023 Tanshin, page 1). (2) The company publishes earnings forecasts
and revises them: notices of revision dated 2024-02-05, 2025-02-05, 2025-11-05 and 2026-01-28 are listed in the IR
library (titles read, contents of the first three not read). (3) The company describes the losses since 2019 as coming
"from large projects ordered prior to this restructuring plan" (2026-01-28 notice); the Golden Pass contract was awarded in
2019 (CHIYODA REPORT 2019, PDF page 11, "an EPC contract has been awarded for the Golden Pass LNG Project in the U.S.").
(4) A director, Satoshi Sato, is an executive officer of Mitsubishi Corporation and did not take part in the board's
2026-01-28 resolution; the outside auditors' opinion found the preferred amendment "not disadvantageous to our general
shareholders" (2026-01-28 notice). (5) The officer pay plan is a performance-based share plan through a BIP trust from 2021
(FY2025 Tanshin, Additional Information); its targets were not read.

**Q6 (the money and the owners).** No dividend on the common since FY2018 (each Tanshin's dividend table); "all distributable amounts will be allocated to the redemption of preferred shares until the redemption is fully
completed" (FY2025 Tanshin, section 1(4)). The last common dividend was JPY 7.50 for FY2017 (FY2018 Tanshin, dividend
table); the Class A preferred received JPY 20.78 a share for FY2020 and nothing since (FY2021 Tanshin), and its unpaid
dividends stood at JPY 10,538 million at 2026-03-31 (FY2025 Tanshin, net assets per share note). The amendment of 2026-06-24 replaced a redemption price "generally equivalent to
the market value of four common shares" with a fixed JPY 436 plus unpaid dividends and deferred conversion to July 2029
(2026-01-28 notice); at JPY 617 a common share, four common shares are worth JPY 2,468 against the JPY 499.2 paid on
2026-06-30. The remaining 64,600,000 preferred carry a dividend that steps to 12% compound from 2028-07-01 and convert from
2029-07-01; unredeemed, they would convert into more common shares than are now outstanding (COMPUTATION, beside).
Mitsubishi Corporation holds about 33% of the voting rights (2026-01-28 notice). No buyback of common.

**Q9 (ruin).** Borrowings JPY 2,397 million after the early repayment of the JPY 20,000 million subordinated loan in the
quarter to 2026-06-30 (1Q FY2026 Tanshin). Customers' advances (contract liabilities) JPY 185,277 million. Partner risk:
"the Group may bear contractual joint responsibility" (FY2025 Tanshin, risk (c)); Zachry's withdrawal from Golden Pass in
May 2024 (CHIYODA REPORT 2025, PDF page 15). Concentration: QatarEnergy 30.7% and Golden Pass LNG 24.9% of FY2025 sales.
The North Field East project in Qatar was temporarily suspended after February 2026 and had resumed by mid-March 2026 (FY2025
Tanshin, subsequent events). The company states it has "confirmed continued support from our main bank, Mitsubishi UFJ
Bank" and is discussing "the establishment of new commitment lines" (2026-01-28 notice). Guarantees, letters of credit and
performance bonds were not read.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Partly kept:** Step 0, the foundations, the standing rule, Q1 and Q2 were
      written in one pass and committed together in one commit (b7205a52), not one commit per question; the COMPUTATION and
      the closing sections are a second commit. Declared, not hidden.
- [x] Dispatched: the brief allowed the per-question commits; whether the dispatching session holds the lock and folds the
      run is the dispatcher's to confirm (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination declared:** the
      session context showed, unasked, the git status (research-folder names of two other companies' runs and recent commit
      subjects about another company) and the auto-memory index (lines about the queue's state); a count of files in
      `Test Runs/` (not their names) appeared in one command's output. None concern Chiyoda; none were used.
- [x] Every v5 id resolves (check script in the research folder, `scripts/check_ids.py`); no E-ids. Filing facts carry
      title, date and URL in place of accessions (the filer has none); the rivals' facts carry SEC accessions.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance, and every later number is under
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash from the cash flow statements after every real cost, never a net-income proxy; the sovereign from the
      Japan Ministry of Finance; the prices flagged as aggregator quotes.
- [x] Contrary evidence written down as found (the foundations paragraph, and the literal-window figures beside the
      COMPUTATION); the facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No point-in-time anchor before today; no row barred.
- [x] `tools/run.py` printed no arithmetic for this non-SEC filer; nothing it printed was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (see the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1's routing has no rule for a business whose key variable is the realised margin on a few fixed-price contracts.**
The routing sends fast-changing industries to Q1 TOO HARD; a lump-sum contractor's industry does not change fast, but its
earnings turn on contract outcomes no insider can forecast. I took Q1 IN (the economics of the trade are legible) and
judged the castle at Q2 on eleven years of evidence; another analyst could close the same name at Q1 TOO HARD (NATURE).
(2) **Q7 (a), "aberrational on the filer's own description", fails for a contractor**: nearly every year read is described
by one project event (FY2016 Ichthys, FY2018 Cameron and Tangguh, FY2021 Ichthys settlement, FY2023 and FY2025 Golden
Pass), so every window's end is aberrational; and "peak to peak" is underdetermined when the first year read may itself be
a peak. I used FY2016 to FY2023 and showed FY2015 to FY2022 and the eleven-year average beside. (3) **Net debt counts cash
as filed**, which for a contractor credits customers' advances (contract liabilities exceed cash here) as the owner's money;
I showed a beside figure with the excess advances deducted, a CONVENTION of this run; the framework needs a rule. (4) **The
business-of-parts convention needs operating profit by part**; a one-segment filer files sales by field only; I ranked by
sales as a CONVENTION of this run. (5) **No rule for a convertible preferred with a fixed cash redemption** in net debt or in
the share count; I counted it at its redemption claim (CONVENTION of this run) with a converted count beside. (6) **The
change-for-the-better rule** (TOO HARD (NATURE) until a full cycle) does not say what happens when the claimed change, even
if proven, is a change of risk and not of castle; I read it as not deciding, and said why. (7) **The fair-price definition
gives a figure above the range itself when owner cash is negative**, since a negative stream at ten percent is a smaller
negative; flagged in the COMPUTATION. (8) **The template asks for an accession for every filing fact**; a non-SEC filer has
none, and the brief's departure (title, date, URL) was used. (9) The Kessan Tanshin are unaudited and abridged; the audited
yuho is in Japanese on EDINET and was not read; one figure was cross-checked against the audited English FY2024 statements.
