# Company Run — Air Water Ventures Limited (Nasdaq: WATR) — 2026-10-29
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (2026-10-29), after the run was committed: not held (`PORTFOLIO.md` does not name WATR or Air Water).

**Dispatched run.** Done by a dispatched analyst under `Screens/_daily/_dispatch_brief.md` with three departures the brief
states: (1) the repository path is `C:\Projects\BRK` (moved 2026-10-25); (2) the lines of evidence were derived by the
analyst from the filings, not supplied (listed below); (3) the company files a 20-F shell company report, not a 10-K, and
the incorporated sections of the 424B3, the F-1 of 2026-09-11 and the 6-Ks stand in for Items 1, 1A and 7.

**Lines of evidence chosen** (derived from the incorporated business section, risk factors and MD&A): revenue, gross
margin and cash burn over every year filed (FY2023 to FY2025); the stage of the business (plant built or not, revenue
against cost of revenue); the going-concern language; the SPAC terms, redemptions and the PIPE; the Series A preferred and
warrant terms (accrual, reset, put); earnouts; related-party loans and share repurchases; customers and distributors named;
competitors named; the pending Second Spring deal; the governance elections in the 6-Ks.

**Contamination declared.** Before any fetch, the session context showed recent commit subjects of the repository (other
names' overnight runs) and the git status listing; none concerns this company, and nothing of them is used. No other
`Test Runs/` file, holding review, `PORTFOLIO.md` or blind-listed screen was opened, listed or searched. The memory index
loaded with the session names queue states in general terms only; nothing about this company.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $1.47 (close 2026-10-28; Yahoo Finance chart API; **aggregator, flagged** per operator rule 5). The stock
  first traded as WATR on 2026-08-17 at a close of $2.51 and has fallen since (same source).
- **Shares by class:** 31,639,454 Ordinary Shares outstanding on 2026-08-14 (20-F shell company report cover, filed
  2026-08-20, accession `0001213900-26-092139`). The F-1 of 2026-09-11 (accession `0001213900-26-099277`) gives
  31,639,439 "Securities Outstanding Before the Offering", fifteen shares fewer; the 20-F cover figure is used and the
  difference is immaterial. `python Screens/cover_shares.py WATR` failed (HTTP 404, a new filer with no XBRL cover); the
  count is from the filed covers. No treasury shares are stated at the listed company.
  **Senior and potential claims beside the ordinary shares** (F-1, Capitalization and Description of Securities):
  117,037.282 Series A Preferred Shares with an Accrued Value of $117.0M at the Closing Date, accruing 12% a year if paid
  in kind (10% if in cash), compounding semi-annually, convertible at $12.00 (full-ratchet reset to any lower issue price
  below $10.00, down to par, and a one-time reset to the six-month VWAP, not below the Floor Price), with a holder put at
  100% of Accrued Value from the fifth anniversary; Series A Investor Warrants for up to 12,204,036 shares at $12.00 (same
  ratchet; the one-time reset not below $5.00); up to 20,000,000 Earnout Shares; 5,750,500 shares reserved under the 2025
  Equity Incentive Plan and ESPP. The F-1 registers up to 230,515,880 shares on the good-faith maximum assumption of a
  $1.00 conversion and exercise price.
- **Market cap:** 31.639454M × $1.47 = **$46.5M** (ordinary shares only).
- **Sovereign for the earnings currency:** the reporting currency is the US dollar; the UAE dirham, the main operating
  currency, is pegged to the dollar (F-1 MD&A). **5.37%**, US Treasury daily par yield curve, 30-year, 2026-10-28
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 20-F shell company report, event date 2026-08-14, filed 2026-08-20,
  `0001213900-26-092139` (cover, incorporation list); F-1 filed 2026-09-11, `0001213900-26-099277` (prospectus summary,
  risk factor summary, capitalization, MD&A of the operating company, business, related party transactions, executive
  compensation, description of securities, beneficial ownership, the audited IFRS statements of Air Water Ventures
  Holdings Limited for FY2025 and FY2024 with the Grant Thornton (Dubai) report, and the SPAC's notes); 424B3 filed
  2026-07-08, `0001213900-26-076389` (downloaded; the same incorporated sections, read through the F-1, which repeats them
  later-dated); DRS filed 2026-01-05, `0001213900-26-001168` (FY2023 figures and the material-weakness risk factor); 6-Ks
  `0001213900-26-090327` (closing release, 2026-08-14), `0001213900-26-093258` (Second Spring LOI and note, 2026-08-25),
  `0001213900-26-108018` (home-country practice election, 2026-10-08); Schedule 13D `0001213900-26-092779` (2026-08-21);
  S-8 `0001213900-26-112479` (2026-10-26). No proxy statement exists; the Forms 3 were not opened.
  **One figure cross-checked against the filed statement:** net cash used in operating activities FY2025, $18,104,877
  in the audited consolidated statement of cash flows (F-1, F-58), against the MD&A's narrative of the same year; the
  FY2025 loss of $27,542,913 in the statement of comprehensive income equals the figure in the auditor's going-concern
  paragraph.
- `python tools/run.py WATR`: failed ("no overlapping OCF/D&A/capex annual facts. UNRESEARCHED"); a new 20-F filer with
  IFRS statements and no annual XBRL facts. Every figure in this run is from the filed statements.
  **Owner cash after every real cost** (operating cash flow, less purchases of property, plant, equipment and intangibles,
  less lease principal repaid; no acquisitions in the window; stock pay is inside the loss and non-cash, and none is added
  back): FY2023 about **−$3.1M** (operating cash −$2.9M and investing −$0.213M as the DRS MD&A rounds them; lease principal
  for FY2023 not stated in the MD&A read); FY2024 **−$16.93M** (−13.074 − 3.311 − 0.544); FY2025 **−$20.01M**
  (−18.105 − 0.758 − 1.144). Three years filed, all negative; average **−$13.35M**. Depreciation and amortization:
  FY2024 $0.565M, FY2025 $2.463M; capital spending FY2024 $3.31M, FY2025 $0.76M. Script:
  `Test Runs/_research 2026-10-29 WATR/q7_computation.py`.

## THE FOUNDATIONS (not a gate)
The foundation that bears here is the first: a share is a business, and the test is "“Would I be happy buying this stock if
the market closed for five years?”" **[M1997-109]**. The business behind the share sold $1.37M of water and machines in
FY2025 at a cost of revenue of $4.71M and used $18.1M of cash in operations; whether it would exist in five years without
fresh capital is the question its own auditor raises. The margin-of-safety foundation also bears: "if you have to actually
do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**; no pencil can be put to a cash stream
that has been negative in every filed year. Who is paid to tell you: the closing release speaks of "a $12.5 billion
opportunity in the air-to-water market" (6-K `0001213900-26-090327`), a seller's projection the foundations rule out.
**Contrary evidence, written down as found** **[M1997-127]**: revenue rose from $224K (FY2023) to $519K (FY2024) to
$1.37M (FY2025); a national distribution agreement with Southern Glazer's Wine & Spirits was announced 2025-10-02, and
Southern Glazer's invested in the PIPE (6-K `0001213900-26-090327`); placements with the Miami HEAT's arena, Inter Miami
CF's stadium, Hilton (UAE) and Le Méridien are named (F-1, Business). Cash was about $37.6M at the F-1 date. These are the
strongest facts for the business, and none is a year of positive cash.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase made with borrowed money or sized so that a total loss could matter is
forbidden whatever the questions conclude, "borrowed money has no place in the investor's tool kit: Anything can happen
anytime in markets." **[L2014-005]**. Nothing in this run proposes a purchase; the rule is noted, not tested.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The product is
  plain: water condensed from air, filtered, mineralized and packed in cans and glass; and atmospheric water generators
  sold or leased. The economics are not. The key variables are (1) whether a consumer will pay a premium for water made
  from air over spring, purified and mineral water sold by the largest beverage companies, (2) the cost per litre of
  water made by machines whose output the filing says "will vary depending on weather conditions including humidity and
  temperature that can impact AWG effectiveness and uptime" (F-1, MD&A, Liquidity), and (3) whether a US plant not yet
  built can be built and run. None has a record: every filed year shows cost of revenue above revenue (FY2023 direct
  costs $761K on revenue $224K; FY2024 $1.14M on $519K; FY2025 $4.71M on $1.37M; DRS `0001213900-26-001168` and F-1
  `0001213900-26-099277`), the Hialeah facility "is not yet operational", needs "between $20 and $25 million" more and
  targets "commencement of operations in the fourth quarter of 2026 to the first quarter of 2027" (F-1, MD&A).
- **It is a start-up.** The rows rule it out by name and before any other test: "Start-ups are not our game."
  **[L2007-015]**; "I say, “We don’t do startups.” They don’t exist." **[M2008-088]**. The filing describes the stage
  itself: a "limited operating history at our current scale" and "our history of net losses and substantial doubt as to
  our ability to achieve or maintain profitability, and our need to raise significant additional capital" (F-1, Risk
  Factor Summary); the auditor's report on FY2025 carries a going-concern paragraph on a loss of $27,542,913 and
  accumulated losses of $40,480,472 (Grant Thornton, Dubai Branch, F-1 page F-54). Eight years after the company says it
  "began manufacturing and developing our AWGs in 2018" (F-1, Business), annual sales are $1.37M.
- **The past statements do not tell the future ones.** The test asks whether "the financial statements will tell me the
  information that’s useful to me in making a judgment about what the future financial statements are going to look
  like" **[M2008-033]**. Here they do not: the company's own plan is a different
  business from its record, a US consumer brand to be built through a distributor and a plant not yet equipped, so the
  three years filed describe a UAE machine-and-bottling start-up, not the business the money is now being spent on.
- **Seeing the industry is not seeing the company.** The filing's case rests on market growth (a bottled water market of
  "approximately $335.5 billion" growing at "5.4%", F-1, Business, citing Precedence Research); the rows answer it: "Just
  because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we can judge what its profit
  margins and returns on capital will be" **[L2009-005]**.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.
- **Routing.** The framework's Q1 lists start-ups under "What it rules OUT" with these two rows; a start-up is answered
  against, not left unanswered, so the box is OUT rather than TOO HARD. The other reading (the ten-year economics cannot
  be foreseen, which would be TOO HARD) is recorded under "What in the framework was wrong or unclear"; either box closes
  the file here.
- **VERDICT: OUT** at Q1. A start-up, and "Start-ups are not our game." **[L2007-015]**; its ten-year economics cannot be
  foreseen from a record of gross losses, and "if you have doubts about something being into your circle of competence,
  it isn’t." **[M2002-092]**. The file closes. Q2 to Q12 are NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP. NOT REACHED.
## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING. NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (computed below under COMPUTATION, NOT A CLEARANCE, for the reporting figures only).
## Q8 — BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — THE FAT PITCH? NOT REACHED.
## Q12 (optional) — PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT**, decided at **Q1** (a start-up: "Start-ups are not our game." **[L2007-015]**), with **integrity facts recorded,
not judged** (Q5 and Q6 facts below: insider share buybacks funded by a related-party loan, related-party noteholders
converting at a set price, an election to issue large blocks of shares without shareholder approval). Price $1.47; the
COMPUTATION below finds no positive value on any case.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on a later question, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).

**Bearing on Q2 (the castle).**
- Rivals the filing names (F-1, Business, Competition): "Nestle Water, Primo Water, brands from Coca Cola and Pepsi, as
  well as a myriad of local and regional brands"; on the generator side "Watergen, Source Water and Kara Water". The filer
  adds: "we do not consider any single company to be a key competitor to our business as a whole."
- The competitor row, gross margin and operating margin from the rivals' own 10-K XBRL facts (whole company; none breaks
  out water, so this compares the field's economics, not water alone):

  | Company | Years | Gross margin | Operating margin | Source accession (latest) |
  |---|---|---|---|---|
  | Coca-Cola (KO) | FY2017 to FY2025 (FY2022 frame missing) | 59.3% to 62.1% | 21.2% to 28.7% | `0001628280-26-010047` |
  | PepsiCo (PEP) | FY2016 to FY2025 (FY2022 frame missing) | 53.3% to 55.1% | 12.2% to 16.2% | `0000077476-26-000007` |
  | Primo Brands (PRMB; Primo Water merged with BlueTriton, owner of Poland Spring and Deer Park, in Nov 2024) | FY2022 to FY2025 | 22.4% to 31.5% | 0.5% to 8.6% | `0001628280-26-012779` |
  | Air Water (WATR) | FY2023 to FY2025 | −240%, −119%, −244% | operating loss $10.9M (FY2024), $22.8M (FY2025) | DRS `0001213900-26-001168`; F-1 `0001213900-26-099277` |

  Named rivals not taken: Nestle Water (Nestlé S.A., not an SEC 10-K filer), Watergen, Source Water and Kara Water (not
  searched on EDGAR; believed private; flagged).
- Customers and channel: a national distribution agreement with Southern Glazer's Wine & Spirits (announced 2025-10-02),
  beginning in South Florida; arena and hotel placements; "a majority of our customers currently are in the UAE and other
  countries in the Middle East" (F-1, Business). One granted patent (GCC, to 2040) and PCT applications pending (F-1,
  Business). The filing's own risk summary: the US market is "highly competitive and dominated by companies with
  substantially greater financial resources than ours".

**Bearing on Q3 and Q4 (capital, and what the numbers show).**
- Balance sheets (eight to ten years do not exist; two audited year-ends and the filer's June 30, 2026 capitalization):

  | USD M | 2024-12-31 | 2025-12-31 | 2026-06-30 actual | at Closing, as adjusted |
  |---|---|---|---|---|
  | Cash | 0.08 | 16.62 | 12.16 | 46.94 (about 37.6 at the F-1 date) |
  | Inventories | 4.68 | 3.10 | n/a | n/a |
  | Prepayments and deposits | 0.45 | 3.97 | n/a | n/a |
  | PP&E / right-of-use / intangibles | 3.03 / 5.36 / 0.43 | 3.37 / 3.51 / 0.58 | n/a | n/a |
  | Loans from related parties | 11.47 | 5.62 | 1.00 | nil |
  | Series A shares and warrants (financial liability) | nil | 35.30 | 61.50 | 117.04 |
  | Lease liabilities | 5.33 | 3.66 | n/a | n/a |
  | Trade and other payables | 4.62 | 9.63 | n/a | n/a |
  | Total equity (deficit) | (7.50) | (23.15) | (47.84) | (169.78) |
  | Accumulated losses | (9.11) | (40.48) | (65.18) | (169.78) |

  Sources: audited statement of financial position (F-1, F-55) and the F-1 Capitalization table. What moved: inventory
  stood at 9.0 times FY2024 revenue and 2.3 times FY2025 revenue, after a $669K obsolescence provision in FY2025 tied to
  "managements realignment of revenue channels" (F-1, MD&A); prepayments and deposits rose almost ninefold, including
  $1.33M of prepaid advertising and marketing against $1.37M of revenue (note 9); payables doubled; the equity deficit
  deepened every period, the new capital arriving as a liability (the Series A) rather than as equity. What the figures
  cannot say: anything about the US business the money is now for.
- The DRS risk factors report material weaknesses in internal control found in the FY2024 and FY2023 audits (lack of
  financial-reporting resources, entity-level controls and segregation of duties, purchase-to-pay cut-off, IT general
  controls; DRS `0001213900-26-001168`).
- The FY2025 loss includes $8.6M of consultancy and professional fees "in support of the Business Combination" and $4.9M
  of finance costs, mostly accrued on the Series A (F-1, MD&A). Without the $8.6M, FY2025 owner cash would still be about
  −$11.4M.
- One earnout tranche is set on "EBITDA (as defined and reported by Bloomberg L.P.)" above $12.5M in a quarter; others on
  quarterly revenue above $25M or $50M, a $100M federal contract, or a $20.00 share price (F-1, the SPAC's notes, which
  state 30,000,000 Earnout Shares in four tranches; the F-1 cover and Capitalization state up to 20,000,000; the
  difference is not explained in the sections read).

**Bearing on Q5 (integrity facts, recorded, not judged).**
- 2024: the company borrowed $9,954,709 at 4% from Tau Capital, a shareholder whose general partner Andrea Mollica is a
  director, "to fund Air Water UK’s repurchase of 4,999 Air Water UK ordinary shares from shareholders" under a Share
  Buyback Agreement of 2024-05-31 among Air Water UK, Paul Guy (a former director) and Jessica Lauren Bain; in the same
  transactions Tau Capital and Mr. Mollica bought shares from shareholders for $10.77M and $1.0M; the loan converted into
  shares in May 2025 (F-1, Related Party Transactions; cash flow statement, "Purchase of treasury shares (9,954,708)").
- 2025: repurchases from the founder and former CEO Alexander Guy, his spouse and a holding company of his for $3.50M,
  with a mutual Deed of Release of claims, and from former director Robert Bain for $326K (F-1, Related Party
  Transactions; cash flow statement, "Shares repurchase (3,826,220)").
- 2025: directors and officers (Mr. Mollica, Matthew Hurn, the CEO Peter Carr, the COO Ryan Bibbo) and a family trust
  subscribed convertible notes and, as holders of more than half, resolved the same day to convert all notes at $765.73 a
  share (F-1, Related Party Transactions).
- Amounts due from related parties written off: $756,891 (FY2024) and $206,015 (FY2025) (cash flow statement).
- Executive pay: aggregate $1,312,166 in FY2025; individual pay not disclosed, as Cayman law permits; pre-closing RSUs
  became fully vested at the Closing and carry rights to Earnout Shares (F-1, Executive Compensation).
- The closing release projects "a $12.5 billion opportunity in the air-to-water market" (6-K `0001213900-26-090327`).
- The lock-up requirement was waived for as many former holders "as necessary to permit Air Water to satisfy the public
  float requirements for initial listing on Nasdaq" (F-1, Prospectus Summary).

**Bearing on Q6 (the money and the owners).**
- The 6-K of 2026-10-08 (`0001213900-26-108018`) elects Cayman home-country practice in lieu of Nasdaq Rules 5635(a), (b)
  and (d): no shareholder approval before issuing shares to buy a company, for a change of control, or for a below-market
  issue of 20% or more.
- The Second Spring LOI (6-K `0001213900-26-093258`): non-binding; $92.5M of company stock and $7.5M cash for a spring
  water brand, the share count set by VWAP with a $3.00 floor and $6.00 cap; at a VWAP below $3.00 the floor sets about
  30.8M shares, close to the 31.6M now outstanding. The company's subsidiary lent the seller $3.0M on a secured note on
  2026-08-18. No definitive agreement and no filed record of the target.
- The Series A conversion and warrant prices reset in full to any lower issue price below $10.00 (down to par) unless the
  issue is an Exempt Issuance (the definition was not read), and once to the six-month VWAP (F-1, Description of
  Securities). Dividend policy: none expected.
- Ownership: the Inflection Point group reports 15,391,525 shares, 40.5% of the class (Schedule 13D
  `0001213900-26-092779`); Tau Capital 9,225,699 ordinary shares plus preferred and warrants (F-1, Beneficial Ownership).

**Bearing on Q9 (debt and exposures).**
- The Series A preferred: $117.0M of Accrued Value at the Closing, accruing at 12% in kind compounding semi-annually,
  with a holder put at 100% of Accrued Value from the fifth anniversary; at that accrual the put would be about $210M in
  August 2031 (arithmetic: 117.04 × 1.06^10), against about $37.6M of cash and a plan needing $20M to $25M more for
  Hialeah alone (F-1). Going-concern paragraphs in the operating company's audit report and the SPAC's.
- Operations in the UAE, with the filing's own risk of "the ongoing conflict involving the United States, Israel and Iran"
  (F-1, Risk Factor Summary).

## COMPUTATION, NOT A CLEARANCE (Q7 arithmetic for the reporting figures; the file closed at Q1)
Built by Q7's range convention as far as the filings allow; script `Test Runs/_research 2026-10-29 WATR/q7_computation.py`.
- **Window.** Three filed years, FY2023 to FY2025, not five: no earlier statements exist (operating subsidiary incorporated
  2019; first audited statements FY2023 and FY2024 in the DRS). **CONVENTION of this run:** the window is every year filed
  when fewer than five exist; rationale: the five-year average cannot be formed, and dropping years would only shorten a
  short record.
- **Owner cash** (operating cash less all capital spending and lease principal; no net-income proxy): −$3.1M, −$16.93M,
  −$20.01M; average **−$13.35M**.
- **The specifics.** (a) No cycle; FY2025 carries $8.6M of deal fees on the filer's own description, and owner cash
  without them (about −$11.4M) is shown beside and is still negative. (b) The series worsens in every year and never
  changes sign; the compound rate between end years and between halves of a three-year window is meaningless for a
  negative series, so **the range is the no-growth case alone, said so**. (c) No acquisitions in the window; the Second
  Spring LOI is non-binding, not a signed deal, and has no filed record; not valued beside. (d) Working capital is inside
  operating cash. (e) The maintenance guess cannot be made: the plant the business will depend on is not built, and FY2025
  depreciation ($2.46M) and capital spending ($0.76M) describe a business being reshaped; the all-spending case is the
  only case. No growth spending is charged (no growth case): $0 in year one and year ten. (f) No cap is reached.
- **Value range (whole business, no growth, at the sovereign 5.37%):** −$248.6M. **Net debt** on the latest filed basis:
  the Series A at its $117.0M Accrued Value (booked by the company as a financial liability and cash-puttable at 100% of
  Accrued Value; counted as debt on the all-equity basis, said so) less about $37.6M of cash stated in the F-1 =
  **$79.4M**; IFRS 16 lease liabilities ($3.66M at 2025-12-31) left out, their principal being charged inside owner cash.
  **Per share: −$10.37** (top and bottom the same; 31,639,454 shares). Against **$1.47**.
- **Floor tested first:** no case earns the floor of about ten percent at $1.47; every case is negative. Had Q7 been
  reached it would close OUT on the floor, "there’s just a point at which we drop out of the game" **[M2003-149]**, and
  before that on "if we don’t have the faintest idea what the future stream is going to look like, we don’t have the
  faintest idea what it’s worth, now." **[M1994-077]**.
- **Fair price (reporting figure, Part VII):** each end case valued at ten percent and averaged; with one case, the
  no-growth case alone: −$133.5M for the business, less $79.4M net debt = −$212.9M, **−$6.73 a share on the all-equity
  basis (central)**; **−$4.22 a share on the equity-only basis** beside it (owner cash after interest is the same figure,
  the Series A dividends being paid in kind, so the equity-only figure differs only by not deducting the preferred that
  ranks ahead of the ordinary shares). Tax: the company paid no income tax in any year filed; the cash stream is already
  after the company's own tax (nil). **No positive fair price exists on the filed record.**

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits for the template copy, Step 0, Q1 and the box, and the after-the-stop sections.
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's; the fold into the
      register is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; commit subjects and the git
      status seen in the session context are declared under contamination and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (check script
      `Test Runs/_research 2026-10-29 WATR/check_ids.py`); every filing fact carries its accession or its filing section.
- [x] The order was kept; Q1 closed the file; everything after it is facts or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash flow statements, never a net-income proxy; the sovereign from the US
      Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No point-in-time anchor; no row dated after an anchor arises.
- [x] `tools/run.py` and `Screens/cover_shares.py` failed on this filer; nothing they print was used.
- [x] `python tools/check_framework.py` run before the final commit (result in the analyst's reply).
- Gaps, honestly: FY2023 lease principal not stated in the MD&A read, so FY2023 owner cash is slightly overstated; the
  FY2023 balance sheet in the DRS was not extracted; the 424B3 was read through the later F-1, which repeats its sections;
  the Forms 3 and the S-8 plan text were not read; the "Exempt Issuance" and "Floor Price" definitions in the articles
  were not read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Start-up: OUT or TOO HARD.** Q1 lists start-ups among what it rules out, on "Start-ups are not our game."
**[L2007-015]** and "We don’t do startups." **[M2008-088]**, while
the rows that refuse businesses whose future cannot be foreseen send them to TOO HARD, and the framework does not define a
start-up. This company has had an operating subsidiary since 2019 and sales in every year, but its sales are below its
cost of sales, its US plant is unbuilt and its auditor doubts it continues. I took the filer's own description (limited
operating history, net losses, need for significant capital) as the definition and closed OUT; a stated test (for
instance, no year of positive owner cash, or the main plant not yet operating) would make two analysts agree.
(2) **Fewer than five years.** Q7's range convention assumes a five-year window; a new filer may have three. I confessed a
run CONVENTION (every year filed). (3) **A series negative in every year.** Specific (b) covers decline and sign changes,
not a stream negative throughout; the no-growth case alone gives a negative value, and Part VII's fair price is then a
negative number, which the reporting convention does not say how to report. I reported it as computed and as "no positive
fair price". (4) **Preferred stock on the all-equity basis.** The basis names borrowings and finance leases; a
cash-puttable, PIK-accruing convertible preferred that the company books as a liability is neither by name. I counted it
as debt centrally and showed the equity-only figure beside. (5) **IFRS 16 leases.** The basis leaves operating leases out;
an IFRS filer reports all leases as lease liabilities, and the run had to choose (left out, since their principal is
charged inside owner cash). (6) **Tools.** `tools/run.py` and `Screens/cover_shares.py` both fail on a new 20-F filer with
IFRS statements, as the brief anticipated.
