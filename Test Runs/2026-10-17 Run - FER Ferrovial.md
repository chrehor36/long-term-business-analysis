# Company Run — Ferrovial N.V. (Nasdaq: FER) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind
run under `Screens/_daily/_dispatch_brief.md` as departed from by the brief (the lines of evidence derived by the analyst
from the 20-F's Items 4.B, 3.D and 5, stated below). Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (8d44ae97): not held; `PORTFOLIO.md` has no line for FER or Ferrovial.*

**Contamination declared (seen by accident, not used):** the session's opening context listed recent repository commit
subjects naming another company's run (TTEK) and its box; the memory index line in the session context names counts of
gate-clearers and queue state. None of it concerns this company and none of it is used. No `Test Runs/` file other than
the template was opened, listed or searched; no file under any former Ferrovial name was looked for.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $49.41, Nasdaq close 2026-10-16 (Yahoo chart endpoint via `tools/sources.py`; **AGGREGATOR, live quote
  only**, operator rule 5). EUR/USD 1.1244 the same day (Yahoo, aggregator, flagged) gives **EUR 43.94**. The quote fell
  from about $68 in June 2026 to $49.41 (same aggregator, weekly closes); the run does not explain the fall and does not
  use it (the market serves, it does not instruct, **[M2006-077]**).
- **Shares:** `python Screens/cover_shares.py FER` returns 720,626,181 ordinary shares outstanding at 2025-12-31 (20-F
  cover, accession 0001628280-26-011789, filed 2026-02-25). Checked against issued less treasury: treasury shares
  13,129,191 at 2025-12-31, so issued 733,755,372 (share capital EUR 7 million at EUR 0.01 par agrees to rounding);
  4,200,000 treasury shares cancelled (6-K 2026-03-11, 0001468522-26-000016); treasury 8,423,217 at 2026-06-30 (H1 2026
  interim statements, note 6, 6-K 0001628280-26-050224). **Outstanding at 2026-06-30: 721,132,155**, single class. Buybacks
  continued after June (6-Ks 0001468522-26-000050, -000060, -000066; programme extended 2026-09-14, 0001468522-26-000064);
  the run keeps the June count with the June net debt so that cash spent and shares retired are taken at one date.
- **Market cap:** 721.13 million x EUR 43.94 = **EUR 31,689 million** ($35,630 million).
- **Sovereign for the earnings currency (EUR):** **3.67%**, ECB euro area AAA curve, 30-year spot (`SR_30Y`), dated
  2026-10-15, from the issuing authority via `python tools/sources.py`.
- **Filings read** (operator rule 4): 20-F for FY2025 (0001628280-26-011789, filed 2026-02-25; the 20-F/A
  0001628280-26-064381 of 2026-10-02 adds a geographic asset breakdown only and was not needed); 20-F for FY2024
  (0001468522-25-000034, filed 2025-02-28); Form 20-FR12B registration of 2024-01-05 (0001104659-24-001882), which carries
  the audited FY2020 to FY2022 statements; the H1 2026 interim management report and statements on 6-K
  (0001628280-26-050224, 2026-07-28); the 6-Ks of 2026 on the I-24 Choice Lanes (0001468522-26-000055, -000069,
  0001628280-26-064744), the I-285 East award (0001468522-26-000075), the conversion to N.V. (0001468522-26-000030),
  the Euronext delisting (0001468522-26-000062) and the buyback programme. For balance sheets before FY2020, which are on
  no SEC filing (the company registered with the SEC in 2024), the company's own audited consolidated annual accounts:
  FY2020 (with FY2019 comparatives) and the FY2018 management report balance sheet (with FY2017), downloaded from
  ferrovial.com (primary documents of the issuer, not SEC filings; flagged). There is no 10-K, 10-Q or proxy: Item 6 of
  the 20-F carries pay and the board.
- **One figure cross-checked against the filed statement:** cash flows from operating activities FY2025 EUR 1,926
  million appears in the consolidated cash flow statement (F-11) and again as the total of the ex-infrastructure
  (1,285), infrastructure (1,107) and eliminations (-466) columns in Item 5.B (0001628280-26-011789); the FY2024 figure
  EUR 1,293 million agrees between the FY2025 and FY2024 20-Fs.
- **`python tools/run.py FER`:** "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The tool does not read this
  IFRS filer. **All arithmetic was done by hand from the filed statements**, in
  `Test Runs/_research 2026-10-17 FER/q7.py` and `notes.md`, and is shown where used.
- **Owner cash by year** (EUR million, consolidated, before interest, after tax paid; the construction of each line is
  at Q4 and Q7):

  | | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr avg |
  |---|---|---|---|---|---|---|
  | Operating cash flow (incl. dividends from equity-accounted) | 810 | 1,002 | 1,263 | 1,293 | 1,926 | |
  | less PP&E/intangible capex | 124 | 95 | 86 | 226 | 187 | |
  | less investment in infrastructure projects (net of grants) | 239 | 784 | 310 | 186 | 466 | |
  | less lease payments | 131 | 72 | 87 | 104 | 121 | |
  | **all spending, 100%** | 316 | 51 | 780 | 777 | 1,152 | 615 |
  | less dividends paid to non-controlling partners | 270 | 161 | 377 | 444 | 367 | |
  | **all spending, attributable** | 46 | -110 | 403 | 333 | 785 | 291 |
  | **maintenance case, attributable** (project capex replaced by a EUR 50m maintenance guess) | 235 | 624 | 663 | 469 | 1,201 | 638 |

  Sources: consolidated cash flow statements, FY2025 20-F (2023 to 2025), FY2024 20-F (2022), 20-FR12B (2021). The
  2021 and 2022 operating cash flow include the operating cash of the Services business then being sold.

- **The lines of evidence this name needs, and why** (derived from Items 4.B, 3.D and 5 of the FY2025 20-F, as the brief
  asks): (1) the parts and which one decides (Item 5.A.7 segment tables; Item 4.B.3.2): the filer itself says Highways
  and Airports are "approximately 89% of our valuation" by analysts' reports (Item 3.D.2.1), and Highways carries most of
  the operating profit; (2) the toll-rate mechanisms and their limits, since the castle is a contract (Item 4.B.3.2.1:
  407 ETR free tolling subject to Schedule 22 traffic thresholds; the Texas soft caps; I-66 and I-77 above inflation;
  Item 3.D.4.2 termination for convenience); (3) traffic and revenue per transaction by asset over the cycle (Item
  4.B.3.2.1 tables; H1 2026 report); (4) the split of cash and debt between the non-recourse project companies and the
  parent (Item 5.B, the ex-infrastructure tables), because the parent's cash is mostly dividends after project debt
  service; (5) the competitive bidding for new concessions and the construction margins (Items 3.D.2.2, 4.B.8), because
  growth is bought at auction; (6) the litigation and regulatory findings (Note 6.5 and Item 8.A), because the business
  lives on public tenders; (7) the commitments signed after the year (I-24, I-285, NTO at JFK), because they set the
  capital the next decade needs.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the margin of safety: the price must be so far below value that "it ought to just
kind of scream at you" **[M1996-084]**, and "the more volatile the business is [...] the larger the margin of
safety" **[M1997-080]**; a group of non-recourse concessions, a contracting arm and a terminal under
construction is not a simple business. Second, who is paid to tell you **[M2020-037]**: every release leads with
"Adjusted EBITDA" and "like-for-like" growth, and the bid presentations project traffic decades ahead; the run uses
neither projections nor the adjusted figures. Third, a share is a business **[M1997-109]**: the question is what the
roads, the contractor and the terminal will pay their owners, not the recent fall in the quote. No macro view enters
**[M2000-094]**; the run takes the long euro rate as given and does not forecast rates or tolls. **Contrary evidence,
written down as found [M1997-127]:** (i) Schedule 22 payments are being made because 407 ETR traffic is below the
concession's thresholds (CAD 41 million accrued for 2025, Item 3.D.3.3); (ii) Ontario removed the tolls on the
neighbouring Highway 407 East in June 2025 (H1 2026 report); (iii) Highways' adjusted EBIT on the consolidated
concession assets is about 6% pre-tax (Q2); (iv) the regulator's "very serious infringement" findings on public-tender
conduct (Q5); (v) the company's own risk factor that infrastructure funds "requiring lower rates of return" bid against
it (Item 3.D.2.2).

## THE STANDING RULE
A part-interest bought for cash, unlevered, sized so that a fall of half or more is borne: the purchase itself puts the
buyer at no risk of ruin **[M2012-081]**, **[L2014-024]**. The target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, **[M2000-037]**; the product may be ordinary, the "economic dynamics of the
  industry" must be clear **[M2011-014]**. Read by parts (the framework's holding-company paragraph, extended to segments
  on 2026-10-06): the part that decides must be understood.
- **The parts** (adjusted EBIT, EUR million, Item 5.A.7/5.A.8 of the FY2025, FY2024 20-Fs and the 20-FR12B):

  | Part | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr total | share |
  |---|---|---|---|---|---|---|---|
  | Highways (consolidated managed lanes, Spain, Portugal) | 275 | 391 | 586 | 686 | 719 | 2,657 | 74% |
  | Construction (Budimex, Webber, Ferrovial Construcción) | 132 | 69 | 77 | 284 | 351 | 913 | 26% |
  | Airports (Dalaman; equity stakes not in EBIT) | -26 | -9 | 2 | 4 | 14 | -15 | 0% |
  | Energy | n/a | -13 | -8 | -11 | -12 | -44 | neg. |

  407 ETR (48.3%, equity-accounted) sits outside EBIT; counted as dividends received (the framework's equity-method
  convention, Q4) it adds EUR 452 million in 2025 to Highways (Item 4.B.2.4). **Highways decides on either basis**: more
  than half of five-year operating profit. Construction, Airports (Dalaman, and NTO at JFK, which is under construction
  and earns nothing yet) and Energy do not decide.
- **The key variables of the deciding part** **[M1998-044]**: traffic (VKT on 407 ETR; transactions on the managed
  lanes), the toll per trip, the concession terms and the project debt. Each is reported asset by asset (Item 4.B.3.2.1;
  H1 2026 report). The toll rules are written in the contracts: 407 ETR may "raise prices freely without prior
  authorization" subject to Schedule 22 traffic thresholds, to 2098; the Dallas lanes have CPI soft caps that may be
  exceeded to keep a minimum speed, to 2061; I-66 and I-77 may rise faster than inflation, 50-year terms from 2016 and
  2019 (Item 4.B.3.2.1, 0001628280-26-011789). These are variables an outsider can read and follow.
- **Do the insiders write it down?** **[M2000-105]**: yes; every concession bid is a written traffic and toll forecast
  over 50 years (the I-24 presentation of 2026-10-05, 0001628280-26-064744, targets a "double-digit equity IRR"). Their
  forecasts are not used here, by the rule against projections **[M1995-050]**; the point is only that the industry treats the ten-year economics as
  forecastable, which is test 5's question.
- **Change and technology.** Roads change slowly; the threats the filer names are competing roads, transit, remote
  work, weather and government action (Item 3.D.3.3, 3.D.4.2), not a fast-moving technology **[M1998-008]**.
- **Abroad** **[M2000-141]**: a Dutch N.V. controlled in practice by a Spanish family (the del Pino holdings, 21.87% and
  8.66%, H1 2026 Appendix II), earning mostly in US and Canadian dollars, reporting in euros. The governance and the tax
  (Item 3.D.6, Netherlands residence) can be read.
- **The parts that do not decide.** Construction is a fixed-price contracting business on public tenders (84% of order
  book public, Item 3.D.1.6); its economics are understood as a commodity business (Q2). NTO at JFK is a greenfield
  terminal whose opening slipped to March 2027 (H1 2026 report), with traffic exposed to Asian routes (Item 3.D.1.1);
  its ten-year economics are not foreseeable by me, but it does not decide.
- **Against:** what Ferrovial will be in ten years depends on concessions not yet won or built (I-24, a $9.2 billion
  project with service in 2034; I-285 East, $8.9 billion construction value), whose returns are set at auction. That is
  a question of the price paid for growth (Q3, Q7), not of whether the economics can be understood.
- **VERDICT: IN, narrowly.** The deciding part's economics are contractual, reported asset by asset and slow to change
  **[M2012-065]**; the doubt that would keep it outside **[M2002-092]** attaches to NTO, which does not decide.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is the 1995 one: "why is that castle still standing?" and "how permanent" are the key factors
**[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (five-year adjusted EBIT, from the Q1 table; 407 ETR counted as dividends received):

| Part | Share of 5-yr operating profit | Castle | Decides |
|---|---|---|---|
| Highways (US managed lanes consolidated; 407 ETR equity-accounted; Spain, Portugal, India stakes) | 74% of adjusted EBIT, more with 407 dividends | contractual local monopolies with written toll freedom; see below | **yes** (more than half) |
| Construction | 26% | commodity contracting on public tenders; not the low-cost producer on the evidence below | no |
| Airports (Dalaman; NTO at JFK in construction) | about 0% | concession and a terminal not yet open | no |
| Energy | negative | renewable projects in development | no |

The file closes on Highways. Construction, which does not decide and whose castle is open, is carried to Q7 as an
ordinary business at no growth (the framework's business-of-parts paragraph).

**The castle tests, on Highways, each with its filing fact.**
1. *The key factors and how permanent* **[M1995-038]**. The castle is a right granted by a government to toll a
   specific corridor: 407 ETR for 99 years to 2098; NTE and LBJ to 2061; I-66 to 2066; I-77 to 2069 (Item 4.B.3.2.1 and
   the consolidation-scope table, 0001628280-26-011789). The customer's reason to pay is time saved against a congested
   free road beside it, the same reason in each corridor; the 20-F describes 407 ETR tolls as set "to the time savings
   offered to drivers" (Item 4.B.3.2.1). Permanence is the contract's, not the lord's: the lanes run on dynamic pricing
   and a toll system, not on a superstar.
2. *The attacker with money* **[M2011-015]**. No rival can build a second 407 ETR or a parallel set of managed lanes in
   the same right of way; the concession is exclusive by its nature. The attacker the filer names is the bidder for the
   *next* concession: "international developers and infrastructure funds", funds "requiring lower rates of return", and
   US competition expected to "intensify over 2026–2027" (Items 3.D.2.2, 4.B.8.1). That attacker can take new growth; it
   cannot take an existing road.
3. *Pricing power and the agony before a rise* **[M2005-020]**, **[M2010-092]**. The strongest evidence in the file. 407
   ETR revenue grew at an 8.3% compound rate 2009 to 2025 (Item 4.B.3.2.1); in H1 2026 its toll revenue rose 20.2% on VKT
   up 1.8%, after a new toll schedule on 2026-01-01, with an EBITDA margin of 85.9% (H1 2026 report,
   0001628280-26-050224). The managed lanes' revenue per transaction rose in H1 2026 by 18.9% (NTE), 11.7% (LBJ), 17.3%
   (NTE 35W), 8.7% (I-66) and 11.8% (I-77) against US inflation of 2.7%, with traffic between -5.2% and +8.5% (same
   report). There is no prayer session; the rises are set by algorithm and contract every year.
4. *Unit volume* **[M1999-054]**. 407 ETR VKT: 1,500 (2020), 1,696 (2021), 2,213 (2022), 2,535 (2023), 2,658 (2024),
   2,819 (2025) million (20-FR12B, 0001104659-24-001882; FY2025 20-F). Managed-lane transactions 2023 to 2025: NTE 40, 39,
   37; LBJ 43, 46, 46; NTE 35W 42, 51, 52; I-77 41, 43, 42; I-66 29, 32, 35 million (FY2025 20-F). Volume holds while the
   price rises, but it does not grow on the oldest Dallas lane, and Q2 2026 traffic fell on 407 ETR (-2.7%), NTE (-0.6%),
   NTE 35W (-0.2%) and I-77 (-4.8%) (H1 2026 report).
5. *Would the customer still choose it over the low bid* **[M2017-009]**. The low bid is the free general-purpose lane
   next to it. The customer pays more each year and mostly stays (point 4); the test is met, for now.
6. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. The filer names: termination
   for convenience by the grantor, compensated "at fair market value" for 407 ETR, I-77 and I-66 and by formula in Texas
   (Item 3.D.4.2); "additional restrictions (including on toll rates)" (same); competing roads, transit and travel habits
   (Item 3.D.3.3); Schedule 22 payments when 407 ETR traffic falls below the thresholds, CAD 41 million accrued for 2025
   (Item 3.D.3.3). The regulated moat that broke is the speakers' own warning **[L2023-011]**; here the grantors are a
   province and four US states whose contracts specify compensation. Recorded against: Ontario removed the tolls on the
   adjacent provincially owned Highway 407 East in June 2025 (H1 2026 report, fee revenue -10.6%); the Charlotte planning
   organization voted against the I-77 South project (same report).
7. *Widening or narrowing* **[M1999-108]**, **[M2000-075]**. Widening on the existing roads (price per trip, margins:
   NTE 35W adjusted EBITDA margin 81.7%, LBJ 84.9%, I-66 83.0% in Q2 2026); the 407 Schedule 22 expense fell (CAD 5.5
   million H1 2026 against 45.2 million H1 2025). Being bid away at the margin where new concessions are won: the filer's
   own statement of funds with lower hurdle rates (Item 3.D.2.2).
8. *Ask the competitors* **[M1999-130]**. Not available on the public record read: no rival's management was heard.
   The nearest fact is that a rival owner, Transurban, joined Ferrovial's I-24 consortium rather than bid against it
   (6-K 2026-08-20, 0001468522-26-000055).

**The competitor row.** The 20-F names no competitor by name: it names classes only ("international developers and
infrastructure funds", "listed companies", "big construction groups", Item 4.B.8). The firms that appear in the filings
are partners (Meridiam, APG, John Laing, Acciona, Sacyr, Macquarie, Transurban, Tikehau); none of the toll-road owners
among them files a 10-K, 20-F or 40-F (SEC company-ticker list checked 2026-10-17: Transurban, Meridiam, Vinci SA, ACS
and Macquarie absent). **CONVENTION of this run:** for the deciding part no SEC-filing rival exists, so the Highways
castle is judged on Ferrovial's own asset-by-asset figures and 407 ETR's; for the construction part two US civil
contractors that file 10-Ks and work in Webber's and Ferrovial Construction's US markets are used; rationale: the brief
requires rivals' own filings and these are the nearest SEC filers in the same work.

| Firm (filing) | Metric | 2021 | 2022 | 2023 | 2024 | 2025 | Avg |
|---|---|---|---|---|---|---|---|
| Ferrovial Construction (20-F, adjusted EBIT margin) | % of revenue | 2.2 | 1.1 | 1.1 | 3.9 | 4.6 | 2.6 |
| Granite Construction (10-K, operating income / revenue; latest 0000861459-26-000004) | % | 0.7 | 2.6 | 2.3 | 5.2 | 6.4 | 3.4 |
| Fluor (10-K, operating income / revenue; latest 0001124198-26-000007) | % | -1.9 | 1.5 | 1.0 | 2.8 | -2.4 | 0.2 |

Granite 2016 to 2020: 3.7, 2.1, 0.3, -1.4, -4.4%; Fluor 2017 to 2020: 1.4, 2.7, -5.4, -1.5% (XBRL from the 10-Ks).
Ferrovial Construction 2020: 1.7% (20-FR12B). Over the whole span the field earns ordinary to poor margins and
Ferrovial's construction arm sits inside the field, not below it in cost; the 20-F itself says the sector "has been
experiencing low profitability margins" (Item 3.D.2.2). A commodity contractor that is not the low-cost producer is
the open castle of **[M1997-010]**, **[L2000-017]**; Construction is therefore carried at no growth.

**The field's returns over the last full cycle** (judged in words, as the framework's "ordinary" convention asks).
Highways adjusted EBIT rose from EUR 171 million (2020) and 275 million (2021) to 719 million (2025). Against the
consolidated US highway concession assets of EUR 11,402 million plus the I-66 goodwill of EUR 243 million (auditor's
critical audit matter, FY2025 20-F) the 2025 figure is about 6.2% pre-tax, and it was far lower in 2021 to 2023. That is
an ordinary return on its face and it is the strongest evidence against the castle. Two facts qualify it. First, the
book includes I-66 carried at the fair value of the 2021 acquisition of control (non-controlling-interest table, FY2025
20-F: I-66 assets EUR 5,447 million against liabilities 2,398 million), which is a return on a price paid, not on "the
capital actually needed" **[M2010-090]**. Second, the assets are young (I-66 opened 2022, NTE 35W segment 3C 2023), and
the return is rising at 10 to 20% a year on revenue per trip with traffic flat (point 3). 407 ETR, the oldest asset,
earns an EBIT margin of 81% (H1 2026) on a road opened in the 1990s and has compounded revenue at 8.3% a year since 2009:
a castle protecting excellent returns on the capital that built it, shown over a full cycle (2009 to 2025, through
2020). On the managed lanes the return is shown rising, not yet shown excellent over a cycle.

**VERDICT: IN, on the deciding part.** The existing Highways castle stands: exclusive corridors, written toll freedom,
and price rises that hold with volume **[M2005-020]**, **[M2010-092]**, **[M2011-015]**; the threats are named and
compensated by contract or slow **[M2000-014]**. Carried forward against: the ordinary book return on the consolidated
managed lanes (to Q3), and new concessions won at auction against cheaper capital (to Q3 and Q7). Construction is open
and carried at no growth.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **To stand still, on the roads built: little.** H1 2026 highway project capex was EUR 93 million, of which NTE EUR 81
  million for the capacity works; the other four US lanes spent EUR 2 to 4 million each (H1 2026 report,
  0001628280-26-050224). Depreciation of the Highways segment was EUR 270 million in 2025 (segment table) against those
  small replacement sums: an operating road is close to the best business of **[M1998-081]** once it is built.
- **But part of it is compulsory.** NTE's "Mandatory Capacity Improvements", brought forward by the contract with TxDOT
  and financed with USD 397 million of bonds in 2023 plus a further PAB issue at 5.50% (Item 4.B.3.2.1; Note 5.2), are
  reinvestment the concession requires once traffic succeeds; the I-66 and I-24 contracts carry the same kind of
  obligation. That is the "compulsory reinvestment" the speakers avoid **[M1997-016]**, here earned on by contract.
- **To grow: a great deal, at prices set at auction.** Growth comes from new concessions: I-24 Southeast Choice Lanes,
  a $9.2 billion project, commercial close 2026-09-30, financial close due July 2027, service from 2034, Ferrovial-led
  with Transurban and Tikehau, "targeting double-digit equity IRR" (0001468522-26-000069, 0001628280-26-064744); I-285
  East Phase 1, $8.9 billion construction value, selected 2026-10-15 (0001468522-26-000075); NTO at JFK, EUR 469
  million (2024) and 236 million (2025) of equity with no earnings yet and opening moved to March 2027 (FY2025 20-F Item
  5.B; H1 2026 report). The equity IRR is levered: the projects are "principally debt-financed" (Item 4.B.3.2.1), so a
  double-digit equity return is consistent with a modest return on the whole capital, and the filer says the competing
  bidders accept "lower rates of return" (Item 3.D.2.2). Cash goes in for eight years before any comes out, the case
  in which "growth can destroy value" **[L2000-023]**.
- **Bought growth, priced.** The 5.06% of 407 ETR bought in June 2025 for CAD 1.99 billion (EUR 1.3 billion; Item
  4.A.1.1) implies about CAD 39 billion for the whole equity; with 407's net debt of CAD 10.5 billion (Dec. 2025) and its
  2025 revenue of CAD 2,009 million at roughly an 83% EBITDA margin (FY2025 20-F; H1 2026 report), the price is about
  30 times 2025 EBITDA, a pre-tax EBITDA yield near 3.4% on what was paid (my arithmetic from the filed figures). A wonderful road bought at a price whose return on the added capital is thin: "whether it’s a good
  investment for us depends on how much we pay for that in the end" **[M2010-090]**.
- **What the purchases have returned:** over 2021 to 2025 the group was a net seller (purchases of companies and
  associates EUR 4,449 million against divestments EUR 5,833 million, cash flow statements), chiefly the Heathrow and AGS
  sales; it is not a serial acquirer under Q7(c). The capital released was redeployed into 407 ETR, Indian toll roads
  (Private InvIT, EUR 710 million in 2024) and NTO.
- **Construction** needs little capital (customer advances of EUR 1,824 million against receivables of EUR 1,761
  million at Dec. 2025) and earns thin margins; a thin margin "only works in terms of return on capital if you turn your
  equity extraordinarily fast" **[M2017-096]**, and the risk is the fixed-price contract, not the capital.
- **WEIGHS AGAINST.** The roads already built need little to stand still, but the growth the next decade shows is bought
  with very large sums at returns set by competitive auction and, in the 407 stake, at a thin yield on the price paid;
  the test is "what we earn on that incremental" capital **[M2001-019]**, and on the evidence here it is the second-best
  case at best **[M2018-055]**, **[L2009-012]**, with eight years of cash going in first.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, nine years of them** **[M2025-032]** (EUR million, year-end; FY2017 and FY2018 from the
FY2018 management report balance sheet, FY2019 and FY2020 from the FY2020 audited consolidated accounts, both company
documents downloaded from ferrovial.com and flagged as not SEC-filed; FY2021 and FY2022 from the 20-FR12B
0001104659-24-001882; FY2023 from the FY2024 20-F 0001468522-25-000034; FY2024 and FY2025 from the FY2025 20-F
0001628280-26-011789):

| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Equity attributable to shareholders | 5,503 | 4,530 | 4,304 | 3,187 | 4,156 | 4,233 | 3,766 | 6,075 | 5,908 |
| Non-controlling interests | 731 | 833 | 783 | 640 | 1,790 | 2,240 | 2,113 | 2,045 | 1,757 |
| Goodwill | 2,062 | 372 | 248 | 208 | 431 | 480 | 475 | 500 | 412 |
| Fixed assets in infrastructure projects | 6,917 | 7,155 | 6,880 | 6,200 | 11,185 | 13,667 | 13,495 | 14,147 | 12,509 |
| Investments in associates (407 ETR, NTO, IRB...) | 2,687 | 2,455 | 2,557 | 1,710 | 1,838 | 1,951 | 2,038 | 3,023 | 3,955 |
| Cash, ex-infrastructure companies | 4,137 | 3,766 | 4,617 | 6,321 | 5,329 | 4,962 | 4,585 | 4,653 | 4,070 |
| Borrowings, ex-infrastructure (long + short) | 2,780 | 2,807 | 3,104 | 4,521 | 3,200 | 3,686 | 3,450 | 2,889 | 2,810 |
| Borrowings, infrastructure projects (long + short) | 5,570 | 5,385 | 5,494 | 5,106 | 7,409 | 7,967 | 7,915 | 8,399 | 7,617 |
| Trade receivables | 2,032 | 801 | 891 | 956 | 1,068 | 1,300 | 1,353 | 1,625 | 1,761 |
| Inventories | 629 | 594 | 700 | 691 | 403 | 476 | 458 | 492 | 540 |
| Advances from customers | n/a | n/a | 1,390 | 1,333 | 885 | 1,364 | 1,529 | 1,619 | 1,824 |
| Revenue (continuing) | n/a | n/a | n/a | 6,641 | 6,910 | 7,551 | 8,515 | 9,148 | 9,627 |

(2017 includes the Services business; from 2018 it is in assets and liabilities held for sale, so receivables and
goodwill fall in 2018 by reclassification, not by events. The ex-infrastructure borrowing lines are the filer's own
split.)

**What moved and why.** (1) Equity attributable fell from EUR 5,503 million (2017) to 3,187 million (2020) through the
Services losses and sale, the Heathrow losses of the pandemic (share of equity-accounted results EUR -373 million in
2020, -178 million in 2021, 20-FR12B) and continuing distributions; it was rebuilt in one year, 2024, by the Heathrow
gain (EUR 2,570 million, Item 4.A.1.3), not by retained operating earnings. Over nine years book equity per share has
gone sideways while about EUR 0.5 to 0.9 billion a year went out in dividends and buybacks. (2) Goodwill is small
(EUR 412 million, mostly I-66 at 243 million): the balance sheet is not built on purchased premiums. (3) The jump in
concession assets and in non-controlling interests in 2021 is the consolidation of I-66 at fair value, with its
project debt (borrowings of infrastructure projects up EUR 2.3 billion). (4) The parent's "net cash" (ex-infrastructure
net debt EUR -1,341 million at Dec. 2025, Item 5.B) is about the size of construction's working-capital float:
customer advances EUR 1,824 million plus trade payables 1,803 million against receivables 1,761 million and
inventories 540 million. It is the customers' money as much as the owners'. (5) Receivables have risen from 15.5% of
revenue (2021) to 18.3% (2025) while inventories stayed near 5 to 6%; a slow drift, noted, not a tell on its own
**[M1995-064]**. What the figures cannot say: the value of 407 ETR (carried at EUR 3.9 billion of associates in total,
including a EUR 1.5 billion intangible from the 2025 purchase price allocation, Item 4.A.1.1) and of NTO, both outside
the consolidated lines **[M2025-032]**.

**The real costs.**
- *Depreciation and concession amortization* (EUR 490 million in 2025) are real: a concession is handed back to the
  grantor at term (Item 4.B.3.2.1), so its amortization is the using-up of a wasting right, a true cost **[R1996-023]**,
  **[L2012-003]**. Owner cash in Step 0 deducts the cash spent, not the charge.
- *Stock pay* is in personnel expense under IFRS 2 and is small (share-based schemes EUR 12 to 15 million a year in the
  equity statements); it is counted, not added back **[L2015-003]**.
- *Recurring "one-time" items*: the construction margin of 2025 was "supported by settlements related to the completion
  of several significant contracts" and 2024's by "risk mitigations in the completion of contracts" (Items 5.A.8 of the
  two 20-Fs); 2022 and 2023 carried losses on US contracts. Construction's settlements and losses are recurring parts of
  its earnings, and the five-year average carries both.
- *Equity-method income* (EUR 258 million in 2025) is counted as dividends received (EUR 502 million in 2025, inside
  operating cash), by the framework's convention.
- *Tax*: the income tax line was a benefit of EUR 60 million in 2025 while EUR 97 million was paid (cash flow
  statement); owner cash uses tax paid.

**EBITDA in the filer's own mouth.** Every results release leads with "Adjusted EBITDA" and like-for-like growth (H1
2026 press release, 0001628280-26-050224); the 20-F says "Adjusted EBITDA is used as an approximation to pre-tax
operating cash flow" (Item 5.A.8.1), and the corporate financial policy is a ceiling on net debt "to Adjusted EBITDA
plus dividends from projects" (Item 5.A). The speakers call the figure "utter nonsense" **[M1998-086]** and would buy
into such a company about "zero" times **[M2002-026]**; under the framework's 2026-10-06 convention the featured adjusted
figure is a WEIGHING against here and is carried to Q5 **[L2016-006]**, **[M1994-018]**. In fairness the filer also
reports IFRS operating profit, separates project and parent cash and debt in every period, and states its alternative
measures' limits at length (Item 5.A.8): it explains "in clear terms what’s going on" in the sense of **[M1994-018]**.

**Confusion or suspicion?** No. The ex-infrastructure split makes the parent's cash readable year by year; no tell
that lives in the accounts was found (no prepaid or deferred build-up, no reserve swing, profits backed by cash). The
one item outside the consolidated figures that bears on value, 407 ETR, is reported in summary every quarter (H1 2026
report).

**VERDICT on the accounts: WEIGHS AGAINST, not a STOP.** The numbers show what it earns once owner cash is built from
the cash flow statement; the featured Adjusted EBITDA and the construction settlements weigh against **[L2016-006]**,
and the parent's net cash is largely customer float. The recast owner cash (Step 0) feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For a stock the speakers read rather than meet **[M2007-081]**; the reading tests are the record, the reports and the
proxy **[M1994-008]**, **[M1994-009]**. Integrity is applied on doubt: "If you’ve got doubts, forget it."
**[M2013-088]**.

**Who runs it.** Rafael del Pino, CEO 1992 to 2000 and Executive Chairman since 2000; Ignacio Madridejos, CEO since
September 2019 (Item 6.A, 0001628280-26-011789). The del Pino family holds 21.87% and 8.66% (H1 2026 Appendix II); TCI
holds 10.03%.

**The integrity record in the filings** (each with its source; nothing from outside the filings is used):
1. **Spanish public-works tenders, Ferrovial Construcción.** The CNMC opened proceedings in 2019 against Ferrovial
   Construcción and other builders; the conduct "ostensibly consists of the exchange of certain information between
   companies for the purposes and/or with the effect of restricting competition during the course of the competitive
   tendering processes organized by Public Authorities in Spain" (20-FR12B, Note 6.5, 0001104659-24-001882). On
   2022-07-06 the CNMC issued a resolution "stating that it had been proven" that Ferrovial Construcción committed "a
   very serious infringement" of Article 1 of the Competition Law and Article 101 of the EU Treaty, with a fine of EUR
   38.5 million (same; restated in the FY2025 20-F, Note 6.5.1). Ferrovial appealed on 2022-10-04; the National High
   Court suspended the resolution on 2022-12-09 pending judgment; the group "considers the outcome of this lawsuit is
   unlikely to be unfavorable" and provides nothing (FY2025 20-F). The filings read give no period for the conduct.
2. **Spanish road-maintenance tenders, Ferroser Infraestructuras** (a Ferrovial company until its sale on
   2022-01-31): CNMC proceedings opened July 2019 for "alleged anti-trust practices during tendering for maintenance and
   operation services for the State Road Network"; in August 2021 the CNMC Board declared "a very serious infringement"
   and fined EUR 5.7 million, with a prohibition on contracting; both suspended on appeal; Ferrovial gave the buyer a EUR
   6 million guarantee and provided for it (FY2025 20-F, Note 6.5.1).
3. **Poland, FBSerwis (a Budimex subsidiary):** in February 2023 its president and vice-president were detained by the
   Central Anticorruption Office in an investigation "for alleged tax fraud and money laundering, invoice forgery, and
   bribery" concerning municipal waste tenders; both were dismissed; by the FY2024 20-F the investigation "appears to
   have been completed with respect to Budimex with no further developments related to the company" (20-FR12B; FY2024
   20-F, 0001468522-25-000034).
4. **Slovakia, D4R7:** four criminal-law environmental matters against the construction joint venture (soil and land
   used without permits), EUR 8.7, 6.6 and 15.2 million claimed and one small fine; not provided (FY2025 20-F).
5. **The habits carried from Q4:** Adjusted EBITDA and like-for-like growth featured in every release; a construction
   margin "long-term average target" of 3.5% reported against (H1 2026 report); no earnings guidance found in the
   filings read.
6. **On the other side:** every matter above is disclosed in the annual filings, with amounts, appeals and the
   company's own estimate; no finding names any director or executive officer (the 20-FR12B of January 2024 states
   that "No director or executive officer has been convicted of a criminal offense or is the subject of a pending
   criminal proceeding during the past ten years", in its directors section); the people at
   FBSerwis were removed within two months; the pay of the executive directors is a fixed salary (Chairman EUR 1.65
   million) with annual and three-year variable parts on business cash flow and relative shareholder return (Item 6.B),
   ordinary for the size and not a tell of self-dealing.

**The judgment.** The business decided at Q2 lives on winning public tenders: every concession, and 84% of the
construction order book, is awarded by a public authority (Item 3.D.1.6). Two separate regulator resolutions, in two
different Ferrovial companies, found "very serious" infringements in the conduct of public tenders, one of them
described by the regulator as "proven"; a third unit's chiefs were arrested in a bribery investigation over tenders.
The resolutions are suspended and appealed, and no court has ruled; proof is not established. But the rows do not ask
for proof. They ask whether there is doubt **[M2013-088]**, they warn that "everybody mouths the integrity, even when
it’s lacking" **[M2010-069]**, that "there are whole fields that you can just quit playing because it looks like there’s
too much fraud in it" **[M2002-025]**, and they accept being wrong about some of those ruled out: "we rule out 90
percent of the times. And we may be wrong about a fair number that we’re ruling out" **[M2007-092]**. The conduct
alleged is of a kind a contract cannot police **[M1995-084]**, and the executive chairman has led the group through the
whole span of the proceedings. The case for the people (full disclosure, no individual director named, prompt removal
in Poland) is real and is written down; it lowers the doubt, it does not remove it. The newspaper test of **[M2008-011]**
is already failed in the regulator's own words.

**VERDICT on integrity: OUT.** Doubt about how the group wins public tenders, in two companies and two regulator
findings of "very serious" infringement, closes the file on the rows' standard of doubt, not proof **[M2013-088]**,
**[M2007-092]**. Ability is not weighed (NOT REACHED as a verdict); the facts found are under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED (facts under AFTER THE STOP).
## Q7 — WHAT IS IT WORTH? NOT REACHED as a clearance (COMPUTATION, NOT A CLEARANCE under AFTER THE STOP).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED (facts under AFTER THE STOP).
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED (facts under AFTER THE STOP).

---
## THE BOX
**OUT at Q5 (integrity, on doubt), integrity facts recorded and judged at Q5.** Q1 IN narrowly and Q2 IN on the
Highways part; Q3 and Q4 weighed against. COMPUTATION, NOT A CLEARANCE: value range EUR 15.41 to 41.39 a share
($17.33 to $46.54) against EUR 43.94 ($49.41); no case of the range earns the floor at the price, so Q7 would also
have closed OUT.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; the box is unchanged (operator rule 2) **[M1997-127]**.*

**Bearing on Q6 (the money and the owners).**
- Buybacks: EUR 701 million plus EUR 272 million of other repurchases in 2024, EUR 501 million in 2025, EUR 300 million
  in H1 2026 (equity statements; H1 2026 note 6). Prices: 7,169,540 shares at an average EUR 37.90 under the 2024
  programme (Item 16E, FY2025 20-F); 5,144,574 shares for EUR 300 million in H1 2026, about EUR 58.31 each (H1 2026
  note 6). The December 2025 programme states a maximum of EUR 800 million and 15 million shares and a purpose "in the
  context of actions related to future projects" (H1 2026 Appendix I); it names no price above which buying stops. The
  prices paid sit above the bottom of the COMPUTATION range below (EUR 15.41), the case the framework's buyback
  convention weighs against **[L2016-002]**, **[L1999-023]**; written down, not weighed.
- 4,200,000 treasury shares cancelled in March 2026; scrip dividends delivered from treasury (5,230,564 shares in June
  2026), 75.55% of shares electing shares (H1 2026 Appendix I).
- The Chairman is also an executive (Executive Chairman since 2000); a Lead Director (Juan Hoyos) is named (Item 6.A).
  Variable pay is on business cash flow and relative shareholder return (Item 6.B).
- Retention: book equity per share went sideways over 2017 to 2025 while large sums were distributed; value was
  realised by asset sales (Heathrow, Services, AGS) rather than retained earnings (Q4 table).

**Bearing on Q7 (COMPUTATION, NOT A CLEARANCE).** Q7's range convention in full, arithmetic in
`Test Runs/_research 2026-10-17 FER/q7.py`.
- *Owner cash* (Step 0): consolidated operating cash flow, before interest and after tax paid, with equity-accounted
  investees counted by the dividends received, less PP&E/intangible capex, project capex and lease payments, less the
  dividends paid to the minority partners in the consolidated projects (their share of the cash).
- *Central case, (e) maintenance:* project capex replaced by a maintenance guess of EUR 50 million a year
  (**CONVENTION of this run:** H1 2026 highway capex outside NTE's capacity works was about EUR 12 million, doubled and
  rounded up for energy and other projects; rationale: the filer gives no maintenance split and the framework asks for
  the guess where the filing allows one, **[M2000-144]**). Five-year average attributable: **EUR 638 million**. The
  all-spending case (EUR 291 million) is shown beside.
- *Growth, (a) and (b):* the literal compound rate 2021 to 2025 of the central series is 50.4% from a depressed first
  year (2021: pandemic traffic, Services still inside, I-66 build); the first year is aberrational on the filer's own
  description (20-FR12B, Item 5) and the filings read hold only one trough, so no peak-to-peak cycle base can be built;
  the growth is measured between the first and second halves of the window (2021-22 average 430, 2024-25 average 835):
  **24.8% a year** (**CONVENTION of this run**, the halves rule of (b) borrowed for the aberrational first year where
  (a)'s cycle base cannot be formed; rationale: the nearest written rule).
- *(f) the cap:* 24.8% carried ten years would put owner cash at about 26.5% of 2035 sales against a highest share
  shown of 12.5% (2025); cut to the business's own sales growth 2021 to 2025, **8.64% a year**. Both rates written down.
- *(c) acquisitions:* net purchases over the window were negative (EUR -1,384 million; the group was a net seller); not
  a serial acquirer. **CONVENTION of this run:** net sale proceeds are not credited to owner cash in the central case,
  because they are the price of parts sold, whose dividends stop; the default pair with them credited is shown beside.
  The signed, unclosed I-24 (financial close July 2027) and I-285 East (selected, not signed) are left out of the
  central figure; their own filed record shows no earnings before 2034 and equity commitments not stated in the
  filings read, so as if closed they would add outlays and no cash inside ten years, lowering the figures.
- *(d) working capital:* inside operating cash flow.
- *Construction at no growth:* the range carries all owner cash at the capped rate; carrying Construction at no growth
  would lower the top further (the direction is stated, the split was not computed).
- *Net debt:* consolidated net debt at 2026-06-30, EUR 6,283 million (H1 2026 report; leases excluded, as the filer
  defines it), on 721.13 million shares. Sovereign 3.67%, ten years then zero nominal growth.

| Case (EUR a share unless stated) | Base EUR m | No growth | Shown growth (8.64%, 10 yrs) | Fair price (ends at 10%, averaged) | Return at price, growth case |
|---|---|---|---|---|---|
| **Central: all-equity, maintenance, attributable** | 638 | **15.41** | **41.39** | **3.76 ($4.23)** | 3.5% |
| Beside: all spending, attributable | 291 | 2.30 | 14.16 | -3.02 | 1.7% |
| Beside: equity-only (after net interest), maintenance | 364 | 13.75 | 28.55 | **7.11 ($7.99)** | 2.5% |
| Beside: minorities not deducted (100%) | 962 | 27.64 | 66.80 | 10.09 | 5.1% |
| Beside: default pair (c), net sale proceeds credited | 915 | 25.87 | 63.11 | 9.17 | 4.9% |

- **Closes (as a computation):** the floor is tested first. At EUR 43.94 the central case returns 1.7% (no growth) to
  3.5% (growth); no case shown returns 10% **[M2003-149]**; the price is above the top of the central range. It would
  close OUT whatever the width. The growth the central base would need to earn 10% at the price is about 25.5% a year
  for ten years. A sensitivity outside the convention: on the single best year (2025, 100%, EUR 1,568 million) at 15%
  growth for ten years the return at the price is about 11.3%; that case uses one year, ignores the minority partners'
  share and exceeds the cap, and is shown only so that the distance is known.
- **The two reporting figures (reporting convention, not a verdict):** VALUE RANGE EUR 15.41 to 41.39 ($17.33 to
  $46.54) on the all-equity basis, central; FAIR PRICE EUR 3.76 ($4.23) all-equity, EUR 7.11 ($7.99) equity-only,
  after the company's own tax, against EUR 43.94 ($49.41).

**Bearing on Q8.** The euro 30-year sovereign at 3.67% exceeds every case's return at the price except the beside
cases with minorities or sale proceeds credited (Q7 table).

**Bearing on Q9 (debt and exposures).**
- Project debt is non-recourse: borrowings of infrastructure project companies EUR 7,617 million (Dec. 2025), Highways
  project net debt EUR 7,114 million (June 2026); TIFIA loans USD 2,386 million (Item 3.D.1.6); 97% of debt hedged or
  fixed (Item 3.D.1.5). 407 ETR's own net debt CAD 10,611 million at 4.37%, 59% maturing after 2039 (H1 2026 report).
- Parent: ex-infrastructure net cash EUR 1,307 million (June 2026), comparable to construction's customer float (Q4);
  liquidity EUR 4,747 million; a policy ceiling of 2 times net debt to Adjusted EBITDA plus project dividends.
- NTO at JFK: Phase A financing about USD 6 billion at about 5%; the contractor's delay "has the potential to trigger
  various contractual rights and obligations of NTO (including the presentation of a remedial plan under the NTO
  Lease)" and penalties (Item 3.D.2.1); a remedial plan with March 2027 was submitted (H1 2026 report).
- Construction: fixed-price risk; the Turów power plant claim of EUR 248.2 million against the Budimex consortium
  (provisioned for Budimex's share), Ruta del Cacao fine in arbitration (FY2024 and FY2025 20-Fs); equity swaps that
  hedge share plans can lose (Item 3.D.5.3).
- New equity commitments to come: I-24 ($9.2 billion project) and I-285 East ($8.9 billion construction value), "with
  no need to issue equity at Ferrovial level" per the I-24 presentation (0001628280-26-064744).

**Bearing on Q12.** No named business (casinos, tobacco, loading schemes) is involved. The facts bearing on the
newspaper test are the Q5 findings and the steep toll rises on 407 ETR (toll revenue +20.2% in H1 2026), set against
Ontario's removal of tolls on the neighbouring 407 East.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 430f9ded); written question by question; committed after Step 0
      and Q1, Q2, Q3, Q4 and Q5 with pathspecs of the two paths only.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's, not touched; the fold
      is the dispatcher's.
- [x] Blind rule kept: no other run file, holding review, `PORTFOLIO.md`, RESUME STATE, queue or reading-list file
      opened, listed or searched; the contamination seen (commit subjects about TTEK, the memory index line) is declared
      at the top and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-17 FER/check_run.py`;
      every filing fact carries its accession or names its company document (the pre-2020 annual accounts, flagged).
- [x] Order kept; the first failing STOP (Q5) closed the run; Q6 to Q12 are NOT REACHED; every figure after the stop
      is under COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash built from the cash flow statements after every real cost, never a net-income proxy (operator rule
      5); sovereign from the ECB, dated; the price and FX rate flagged as aggregator quotes.
- [x] Contrary evidence written down as found (foundations line, Q2 points 4 and 6, the Q2 return paragraph, Q5 point 6).
- [x] Not a point-in-time run; no anchor bar applies.
- [x] `tools/run.py` produced no arithmetic for this IFRS filer; nothing it prints was used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message).
- **Departures declared:** (1) the balance sheets of FY2017 to FY2020 are from the company's own audited accounts, not
  SEC filings, because the company was not an SEC registrant then; (2) the Q5 STOP was decided on regulator findings
  under appeal, a judgment the rows' doubt standard permits but which another analyst could weigh short of closing; the
  facts for both readings are in Q5; (3) the maintenance guess, the halves growth measure and the treatment of net sale
  proceeds are CONVENTIONS of this run, each confessed where used; (4) Q6 ability and pay were not weighed after the stop.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q5 and regulator findings under appeal.** The framework says integrity is applied "on doubt alone" but gives no
rule for a finding by a competition authority against a subsidiary, suspended by a court, with no individual named.
This run closed on it; a reader could equally hold that the doubt attaches to a part (Construction) that does not
decide at Q2, and the business-of-parts convention does not say whether integrity is read by parts or for the whole.
A sentence saying which would make the box reproducible. (2) **The all-equity basis with consolidated minority
partners.** Q7's basis adds net debt to the market value but says nothing about non-controlling interests that own
27% to 46% of the consolidated concessions; deducting their dividends (used here) and adding their book equity to
the enterprise value (shown beside) give fair prices of EUR 3.76 and EUR 10.09. The framework should say which.
(3) **Range specific (a) where only one trough exists.** The cycle base needs peak to peak or trough to trough; the
filings read held one trough (2020-21), so the run borrowed (b)'s halves measure; the text could say so. (4) **Net
sellers under (c).** The default pair credits net divestment proceeds as negative capital spending, which counts the
price of parts sold, whose earnings stop, as owner cash; the run did not credit it centrally and showed it beside.
(5) **The template's 10-K wording** (proxy, 10-Q, 8-K) does not fit a 20-F filer whose earlier balance sheets are not on
EDGAR; the run used the company's own audited accounts and flagged them.
