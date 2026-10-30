# Company Run — KION GROUP AG (Xetra: KGX; US OTC ADR: KIGRY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (KION files nothing
with the SEC, so the document and its date stand in place of an accession number, as the brief directs); a STOP that
returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (KIGRY, KION Group; also searched for KION and KGX); not held.*

**Dispatch:** a dispatched blind run under `Screens/_daily/_dispatch_brief.md` with the three departures the brief states
(lines of evidence derived by the analyst; competitors are the rivals the company's own report names; no SEC filings).

**Lines of evidence chosen (brief, departure 1).** From the 2025 annual report: the combined management report's
"Fundamentals of the KION Group" (business model, segments, market position), the "Risk report" (competition,
procurement, market risks), and the "Report on the economic position" (business situation, segment performance,
financial position, net debt, cash flow); the notes on the segment report [41], goodwill [15], related parties [42],
long-term variable remuneration [43] and board pay [44]. The same sections of the 2024, 2023, 2022, 2021, 2019, 2018 and
2017 annual reports for the cycle, and the Q2 2026 interim report for the latest balance sheet and subsequent events.

**Contamination declared.** The repository's recent commit subjects (visible in the session's git context) name another
company's run (JCSE); nothing of it bears on KION and nothing of it was used. No other run file, holding review,
`PORTFOLIO.md`, register or reading list was opened, listed or searched. I did not learn whether anyone holds or wants
this name.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** EUR 33.85, Xetra close 2026-10-12 (Yahoo Finance chart API, `KGX.DE`, exchange XETRA; **aggregator, flagged**
  per operator rule 5). The prior Xetra close, 2026-10-09, was EUR 34.14. The ADR KIGRY last traded USD 9.35 on 2026-10-12
  (Yahoo, OTC Markets, aggregator). The quote fell from about EUR 45 at the start of September 2026 to EUR 33.85; no ad hoc
  release after the Q2 report was found on the IR pages (the press-release list loads dynamically, so that sweep is
  incomplete), and the market's move is not an instruction **[M2006-077]**.
- **ADR ratio:** one American Depositary Share represents one-fourth of one ordinary share: "each American Depositary
  Share representing one-fourth of one ordinary share of Kion Group AG", Form F-6 POS of the depositary, Deutsche Bank
  Trust Company Americas, filed 2017-09-18 (SEC accession 0001193805-17-002687; an unsponsored programme; other
  depositaries have filed F-6 forms for the same name). Check: 4 x USD 9.35 = USD 37.40 against EUR 33.85 x 1.1177
  (EURUSD 2026-10-13, Yahoo, aggregator) = USD 37.83; consistent.
- **Shares:** 131,198,647 no-par-value shares issued, less 73,876 treasury shares = **131,124,771 outstanding** at
  2026-06-30 (Q2 2026 interim report, published 2026-07-30, notes on equity; the same counts at 2025-12-31 in the 2025
  annual report, note [26]). One class. No split, merger or spin-off found in the Q2 2026 report; the segment Supply Chain
  Solutions was renamed Intelligent Automation Solutions from 2026-01-01 (Q2 report). `python tools/run.py KIGRY` and
  `python Screens/cover_shares.py KIGRY` returned "not an SEC filer"; all arithmetic below is by hand from the reports.
- **Market cap:** 131.1248m x EUR 33.85 = **EUR 4,438.6m**.
- **Sovereign for the earnings currency (EUR):** **3.78%**, ECB euro area AAA yield curve, 30-year spot,
  YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y, dated 2026-10-09 (`python tools/sources.py`, run 2026-10-13).
- **Filings read** (operator rule 4; the German versions are authoritative, the English versions were read):
  KION Group annual report 2025 (published 2026-02-26; 386 pages), annual reports 2024, 2023, 2022, 2021, 2019, 2018 and
  2017 (each the "entire" PDF from reports.kiongroup.com), and the interim report Q2 2026 (published 2026-07-30). The 2020
  report was not obtained in English (only the German "gesamt" file was linked); 2020 figures come from the 2021 report's
  comparatives, and 2016 from the 2017 report's.
- **One figure cross-checked against the filed statement:** net financial debt at 2025-12-31 of EUR 584.0m in the
  multi-year overview (AR 2025, p. 383) equals financial liabilities 903.8 + 155.1 = 1,058.9 less cash 474.9 on the
  consolidated statement of financial position (AR 2025, pp. 260-261). Agrees.
- **Owner cash after every real cost** (EUR m; `calc/owner_cash.py`, from the filed cash flow statements: operating cash
  flow, less capital spending net of disposals, plus dividends received, less acquisitions net of disposals, less the
  principal and interest of procurement leases, less interest on financial debt; operating cash flow already contains
  the lease and short-term rental business, its fleet growth net of its own funding and its interest, and the taxes paid):

| Year | Owner cash, after interest (equity-only) | Owner cash before financial-debt interest (all-equity) | as % of revenue |
|---|---|---|---|
| 2018 | 360.6 | 406.0 | 5.1% |
| 2019 | 404.6 | 442.0 | 5.0% |
| 2020 | -62.8 | -12.5 | -0.1% |
| 2021 | 364.2 | 398.7 | 3.9% |
| 2022 | -895.4 | -867.3 | -7.8% |
| 2023 | 497.3 | 557.3 | 4.9% |
| 2024 | 469.1 | 526.9 | 4.6% |
| 2025 | 444.3 | 491.9 | 4.4% |
| **5-yr avg 2021-25** | **175.9** | **221.5** | |
| 8-yr avg 2018-25 | 197.7 | 242.9 | |

  Capital spending 2021-25 averaged 403.6 against depreciation and amortization (segment definition: excluding
  right-of-use and PPA items) of 244.7. Stock pay is cash-settled phantom shares, already inside operating cash flow.
  Net working capital moved -201.9, -804.5, +27.5, +243.0, +257.8 in 2021-25.
- **The balance sheets, ten of them, read before the income account** **[M2025-032]** (EUR m, consolidated statements of
  financial position, AR 2017 to AR 2025, each year from the report that closes it or its successor's comparatives; 2016
  and 2017 are before IFRS 16 and show the then "lease liabilities"; 2018-19 show "liabilities from financial services"
  for lease and rental funding together). *(Placed in Step 0 after Q2 had closed the file, as the template directs for a
  file that closes before Q4.)*

| Dec. 31 | Goodwill | Other intangibles | Leased + rental assets | Lease receivables | Inventories | Trade receivables | Cash | Total assets | Equity | Financial liabilities | Lease-business liabilities | Rental liabilities | Pensions | Net financial debt | Revenue |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,572.9 | 2,602.7 | 1,005.0 | 731.6 | 672.4 | 998.9 | 279.6 | 11,297.0 | 2,495.7 | 3,183.0 | 1,007.2 (lease liab.) | n/s | 991.0 | 2,903.4 | 5,587.2 |
| 2017 | 3,382.5 | 2,333.9 | 1,173.7 | 875.8 | 768.6 | 1,094.1 | 173.2 | 11,228.4 | 3,148.8 | 2,268.7 | 1,131.1 (lease liab.) | n/s | 1,002.7 | 2,095.5 | 7,653.6 |
| 2018 | 3,424.8 | 2,296.8 | 1,932.3 | 1,097.4 | 994.8 | 1,036.4 | 175.3 | 12,968.8 | 3,305.1 | 2,045.2 | 1,472.4 (fin. services) | in prior col. | 1,043.0 | 1,869.9 | 7,995.7 |
| 2019 | 3,475.8 | 2,256.6 | 1,994.1 | 1,421.0 | 1,085.3 | 1,074.2 | 211.2 | 13,765.2 | 3,558.4 | 1,820.5 | 2,500.1 (fin. services) | in prior col. | 1,263.4 | 1,609.3 | 8,806.5 |
| 2020 | 3,407.6 | 2,152.0 | 1,862.9 | 1,595.3 | 1,101.0 | 1,172.7 | 314.4 | 14,055.7 | 4,270.8 | 1,194.5 | 2,739.3 | 505.6 | 1,450.3 | 880.0 | 8,341.6 |
| 2021 | 3,544.8 | 2,165.9 | 1,934.3 | 1,784.0 | 1,632.1 | 1,339.2 | 483.0 | 15,850.9 | 5,168.9 | 1,050.6 | 3,070.8 | 488.9 | 1,265.3 | 567.6 | 10,294.3 |
| 2022 | 3,619.4 | 2,162.1 | 1,969.8 | 1,890.3 | 1,804.6 | 1,667.3 | 318.1 | 16,599.4 | 5,607.8 | 1,988.5 | 3,214.6 | 544.2 | 712.8 | 1,670.5 | 11,135.6 |
| 2023 | 3,558.0 | 2,106.9 | 2,192.7 | 2,314.4 | 1,817.1 | 1,755.8 | 311.8 | 17,388.4 | 5,772.7 | 1,522.4 | 3,756.2 | 716.6 | 775.7 | 1,210.6 | 11,433.7 |
| 2024 | 3,648.2 | 2,166.7 | 2,436.7 | 2,812.7 | 1,748.6 | 1,695.6 | 787.0 | 18,805.4 | 6,207.1 | 1,700.3 | 4,407.5 | 814.1 | 747.5 | 913.2 | 11,503.2 |
| 2025 | 3,450.9 | 2,022.4 | 2,529.5 | 3,136.1 | 1,631.7 | 1,528.3 | 474.9 | 18,294.9 | 6,123.0 | 1,058.9 | 4,828.6 | 810.2 | 604.3 | 584.0 | 11,297.2 |
| 2026-06-30 | 3,505.8 | n/r | 2,614.3 | 3,268.6 | n/r | n/r | 391.0 | 18,983.4 | 6,378.5 | 1,635.1 | 4,540.1 | 774.7 | n/r | 1,244.1 | H1 5,687.3 |

  (n/s: not shown as a separate line; n/r: not read. Net financial debt is the company's figure; it reconciles to
  financial liabilities less cash in every year checked.) **What the figures say:** (1) Equity has grown from EUR 2.50bn to
  6.12bn, but about EUR 1.84bn of that came from new shares (capital increases of 449.4 in 2016, 593.6 in 2017 and 800.2
  in 2020; cash flow statements), not from retained earnings, which rose by about 2.09bn in nine years. (2) Goodwill and
  other intangibles, EUR 6.18bn in 2016, exceeded equity by 3.68bn; in 2025 equity exceeds them by only 0.65bn. The
  balance sheet is mostly purchase price: the 2016 Dematic acquisition (cash paid for subsidiaries EUR 2,118.7m in 2016,
  AR 2017), and the ITS goodwill (EUR 1,503.0m) and Linde and STILL brand names carried from before the window (AR 2025
  note [15]; their origin was not read). (3) The leasing book, lease
  receivables plus leased assets, grew from about 1.16bn to 4.86bn and is financed almost entirely by lease-business
  liabilities of 4.83bn: a finance company inside a machinery maker, to be read apart **[L2008-005]**. (4) Inventories
  rose from 10.0% of revenue (2017) to 15.9% (2023) and 14.4% (2025); the 2022 jump (1,804.6 on 11,135.6) is the
  unfinished trucks of the supply crisis (AR 2022). (5) Net financial debt fell from 2.90bn to 0.58bn, mostly with the
  2020 share issue and the working-capital release of 2023-25, then rose to 1.24bn by June 2026 when a EUR 500m bond was
  used to repay lease-business liabilities (Q2 2026 report). (6) Pensions fell from 1.45bn (2020) to 0.60bn with
  discount rates, not with payments. What they cannot say: what the business is worth, and, because no segment
  balance sheet separates the leasing book, what ITS earns on its own tangible capital **[M2025-032]**.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety as an attitude: "if you have to actually do it on — with
pencil and paper, **it’s too close to think about**" **[M1996-084]**, which matters for a cyclical, debt-carrying
industrial whose owner cash swings from -867 to +557 in four years. A share is a business: would I be content to own
this "if the market closed for five years" **[M1997-109]**; the 25% fall in the quote since September is a price, not a
fact about the business **[M2006-077]**. No macro forecast enters: the 2022 inflation and the 2020 shutdown are read
only as what the business did in them **[M2000-094]**. The analyst's habits: "What do I not know that I need to know?"
**[M1999-129]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the company's own risk report says
"some manufacturers having cost advantages" and that "price competition is fierce, particularly in the economy and
volume segments" (AR 2025, risk report, competition risks, p. 234); (2) the global unit share it reported fell from
15.0% (2016) to 12.1% (2020), 12.8% (2021) and 13.4% (first nine months of 2022), after which the reports stop giving a
global unit share and give "market leader in the EMEA region" and "second-largest supplier" by revenue instead (AR 2017
p. 73; AR 2019; AR 2021; AR 2022; AR 2025 p. 30); (3) group ROCE, by the company's own definition, has not exceeded 9.7%
in any year 2017-2025 (multi-year overviews, AR 2021 and AR 2025); (4) from 2026 the company redefined free cash flow,
which "increased free cash flow for the reporting period by 494.7 million" (Q2 2026 report, free cash flow section).

## THE STANDING RULE
A part-interest bought for cash, unlevered, by a holder who does not borrow to own it, cannot put the buyer at risk of
ruin through this purchase: "We are **never going to risk what we have and need for what we don’t have and don’t need**"
**[M2012-081]**; "always be sure you can play the next day." **[M2025-015]**. The target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (AR 2025, fundamentals, pp. 29-32; segment report note [41], p. 346). Two operating segments.
  Industrial Trucks & Services (ITS): forklift and warehouse trucks under Linde, STILL, Baoli, Fenwick and OM, with service,
  spare parts, used trucks, short-term rental, and a captive leasing arm (KION Financial Services) that finances
  customers' long-term leases; "nearly half of its revenue in 2025 from sales of new industrial trucks"; service was 50.9%
  of the segment's external revenue in 2025 (47.8% in 2024); a fleet of "more than 2.0 million industrial trucks" in use;
  21 production facilities in ten countries. Supply Chain Solutions (SCS, Dematic; renamed Intelligent Automation
  Solutions in 2026): warehouse automation, "mainly caters for customer-specific, longer-term project business", plus
  service on the installed base.
- **The parts** (adjusted EBIT, EUR m, segment reports; the 2020 comparatives restated in AR 2021):

| Year | ITS revenue | ITS adj. EBIT | margin | SCS revenue | SCS adj. EBIT | margin |
|---|---|---|---|---|---|---|
| 2016 | 5,202.6 | 586.9 | 11.3% | 366.0 (2 months) | 6.0 | |
| 2017 | 5,630.9 | 640.1 | 11.4% | 2,006.3 | 181.4 | 9.0% |
| 2018 | 5,922.0 | 655.4 | 11.1% | 2,055.2 | 180.2 | 8.8% |
| 2019 | 6,410.2 | 695.1 | 10.8% | 2,378.8 | 228.1 | 9.6% |
| 2020 | 5,723.4 | 311.4 | 5.4% | 2,627.1 | 277.5 | 10.6% |
| 2021 | 6,514.0 | 536.0 | 8.2% | 3,796.2 | 409.5 | 10.8% |
| 2022 | 7,356.1 | 420.5 | 5.7% | 3,806.9 | -45.6 | -1.2% |
| 2023 | 8,479.6 | 848.5 | 10.0% | 2,997.0 | 44.3 | 1.5% |
| 2024 | 8,608.8 | 917.5 | 10.7% | 2,943.2 | 112.9 | 3.8% |
| 2025 | 8,272.5 | 721.8 | 8.7% | 3,071.4 | 183.2 | 6.0% |

  Five-year adjusted EBIT 2021-25: ITS 3,444.3, SCS 704.3; ITS carries 83% of the two. **ITS decides** (more than half of
  five-year operating profit, Q2's business-of-parts CONVENTION, which also defines "matters" for Q1's by-parts reading).
  On reported EBIT the split is ITS 3,180.9 against SCS 196.3, the same answer.
- **The test applied.** Understanding means "a reasonable fix on about **what the earning power and competitive position
  will look like in five or 10 years.**" **[M2012-065]**. The key variables of ITS **[M1998-044]**: world unit demand for
  industrial trucks (cyclical: world orders fell 2.1% in 2019, rose 17.9% in 2017; AR 2019, AR 2017), KION's share of it
  and the price it realises against low-cost rivals, and the service and rental annuity on the installed fleet. The
  product is old and changes slowly: the shift to electric drive is largely made (92.6% of KION's ITS units ordered in
  2025 were electric; 78% of the world market in the first nine months of 2025; AR 2025). These variables can be read from
  the filings, and the past statements say something about the future ones **[M2008-033]**. What cannot be foreseen with
  confidence is the outcome of the competitive attack the filer itself describes, and that is Q2's question, not Q1's:
  the forecast concerns customers choosing between a premium truck with service and a cheaper one **[M2017-019]**, not
  a technology race.
- **SCS** is project business whose margins swung from 10.8% to -1.2% in a year on fixed-price contracts; it does not
  decide, so by the by-parts reading it does not keep the whole outside the circle; it is carried to Q7 at no growth.
- Abroad: a German AG with a two-tier board, a 46.5% shareholder (Weichai Power Co. Ltd., through Weichai Power (Luxembourg) Holding S.à r.l.,
  Luxembourg; AR 2025, combined management report, the paragraph on the parent company; note [42]), and IFRS accounts;
  the governance and tax can be read **[M2000-141]**.
- **VERDICT: IN.** The deciding part, ITS, is a slowly changing machinery-and-service business whose ten-year economics
  turn on a competitive question that Q2 can put to the filings **[M2012-065]**, **[M1998-044]**; doubt about the circle
  is not on the understanding of the business but on its castle, which Q2 owns **[M1997-148]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is put to the deciding part, ITS **[M1995-038]**; SCS is read beside it.

**The castle tests, each with its filing fact.**
- **Key factors and how permanent** **[M1995-038]**. What keeps customers: the Linde and STILL premium brands (carried
  at EUR 465.0m and 107.0m, AR 2025 note [15]), a network of "more than 2,000 outlets in over 100 countries" with "some
  9,400 service employees", and a fleet of more than 2.0 million trucks in use that feeds service, parts and rental
  (AR 2025, fundamentals). These are real and old. Their permanence is what the following facts put in doubt.
- **The attacker with money** **[M2011-015]**. The filer names the attack itself: "Competitive pressure remains high around
  the world as some manufacturers in the economy and volume segments based in China have been pursuing an international
  expansion strategy for a number of years now" (AR 2025, influencing factors in the ITS segment). The same sentence, with
  "based in emerging markets" and "in the economy segment", stands in AR 2017 and AR 2019. The risk report rates
  competition risk "high overall after countermeasures", with "severe" impact (AR 2025, risk report).
- **The low-cost position** **[L2000-017]**, **[M1997-010]**. The filer says it does not hold it where the volume is:
  "Price competition is compounded by some manufacturers having cost advantages [...] This mainly affects the Industrial
  Trucks & Services segment, where price competition is fierce, particularly in the economy and volume segments" (AR 2025,
  risk report, competition risks). Its answer is "a wide range of product variants made possible by modular concepts,
  along with good availability of services, mainly in the volume and premium segments": the defence is service and
  variety, not cost.
- **Pricing power and the agony before a rise** **[M2005-020]**. Through the 2022 inflation, "the raising of list prices
  during the year did little to compensate for the increase in manufacturing costs" because the segment was working
  through orders taken before the rises (AR 2022); the ITS margin fell from 8.2% to 5.7% and the group gross margin from
  24.5% to 19.1%. The 2022 price rises came through in 2023-24 (ITS margin 10.0% and 10.7%; AR 2023: "the price
  adjustments carried out in 2022 resulted in a sharp year-on-year increase in revenue and adjusted EBIT"). In 2025 new
  business showed narrower margins "as a result of pricing and mix effects" (AR 2025, ITS segment). The price could be
  raised, with a lag of a year, and only back to the level of earlier years.
- **Unit volume and share** **[M1999-054]**. Global unit share of ITS: 15.0% (2016), 14.4% (2017), 14.1% (2018), 14.2%
  (2019), 12.1% (2020), 12.8% (2021), 13.4% (first nine months of 2022) (AR 2017, AR 2019, AR 2021, AR 2022, each under
  "Market position"). No global unit share is given in AR 2023 to AR 2025, which give EMEA unit leadership and world
  number two by revenue instead. KION's units ordered rose 8.6% to 266 thousand in 2025, in a world market whose order
  numbers were "significantly higher" in the first nine months (AR 2025).
- **The brand and the low bid** **[M2015-038]**, **[M2017-009]**. The premium brands serve "the premium and higher value
  segments" and Baoli "the lower value and economy segments" (AR 2025, company profile). Where the customer buys on price,
  the filer says the price is set by rivals with lower costs; where he buys on service, the installed base holds him.
- **Ask the competitors** **[M1999-130]**. No rival is named in any of the eight reports read (a text search of each for
  Toyota, Jungheinrich, Hyster, Crown Equipment, Hangcha, Anhui Heli, Daifuku, Honeywell, Vanderlande, Knapp, Schaefer,
  Swisslog, Symbotic, AutoStore, Mitsubishi and Logisnext found none; the reports cite only Interact Analysis, Modern
  Material Handling, World Industrial Truck Statistics and China Forklift Network rankings). The search terms are the
  names a reader would try first; by the brief, no rival is supplied from memory, and none of them is used below.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Over the decade the ITS margin went from 11.3-11.4% (2016-17)
  to 8.7% (2025), the global unit share from 15.0% to about 13%, and the filer's description of the attack from
  "emerging markets" to "China" with the same answer from the company. The service share of ITS revenue rose (50.9% in
  2025). The moat is not shown widening; on the share and margin evidence it has narrowed slightly.
- **What could destroy it** **[M2000-014]**. A lower-cost producer that reaches the premium buyer with an adequate truck and
  adequate service; the filer lists among its own risks that "competitors will join forces" and that higher predicted
  volumes "may lead to overcapacity" (AR 2025, risk report).

**The competitor row.** Not possible from the sources the brief allows: the company's reports name no rival, so no rival's
filing was read and no same-metric comparison is shown. Flagged in the self-audit and under "wrong or unclear".

**The parts table** (five-year adjusted EBIT 2021-25, segment reports):

| Part | Share of 5-yr adj. EBIT | Castle | Decides |
|---|---|---|---|
| ITS (trucks, service, rental, leasing) | 83% | premium brands and installed-base service, under the attack the filer describes from lower-cost rivals | yes |
| SCS / Dematic (warehouse automation projects) | 17% | "world's leading provider" by revenue (AR 2025); margin -1.2% to 10.8% on fixed-price projects | no |

**The field's returns over the last full cycle** (2017-2025: two troughs, 2020 and 2022, and two recoveries), from the
filer's own filings, judged in words **[M1999-108]**:
- Group ROCE, the company's own measure (adjusted EBIT, pre-tax, on capital employed including acquisition goodwill):
  9.3%, 9.3%, 9.7%, 6.2%, 9.1% (2017-21; AR 2021 multi-year overview), 2.9%, 7.7%, 8.7%, 7.7% (2022-25; AR 2025, which
  restates 2021 at 9.5% on its five-quarter average). It never reached 10% pre-tax in nine years.
- On the capital the business actually needs **[M2010-090]**, taking acquisition goodwill and all other intangibles out of
  the company's average capital employed (a generous cut, since capitalized development is a real asset): about
  EUR 4.6-4.7bn in 2024-25 (10,250.0 less average goodwill 3,549.6 and average other intangibles 2,094.6 for 2025;
  10,484.9 less 3,603.1 and 2,136.8 for 2024). Adjusted EBIT on it was 19.3% (2024) and 17.1% (2025) pre-tax, before
  restructuring that recurs (non-recurring items of EUR 201.1m in 2025, 168.8m of it the efficiency program; AR 2025 note
  [41]). Owner cash after every real cost and after tax was 11.1% (2024) and 10.7% (2025) of it, the best years of the
  window; the five-year average owner cash of EUR 221.5m is 4.8% of it.
- Owner cash after every real cost was 3.9% to 5.1% of revenue in the normal years and negative in 2020 and 2022 (Step 0).
  Net income on average equity 2017-25: about 7%.
- Judged in words: across a full cycle this business has turned its castle into ordinary returns. In its good years it
  earns a decent return after tax on its tangible capital; across the cycle its cash return on that capital is about 5%;
  on the capital its owners have paid in, goodwill included, it has never earned 10% pre-tax. That is not a moat that
  "protects excellent returns on invested capital" **[L2007-004]**. The castle stands (EMEA leader, service base, prices
  raised after 2022), but what it protects is ordinary: "you can have only two competitors and they’re still terrible
  businesses" **[M2013-052]**; and the filer itself says the two segments risk "coming under increased price pressure"
  from makers with lower costs, which is near to, though short of, the rival who sets the price **[M2012-109]**.
- SCS does not change the answer: its margins over the same years were 9.0%, 8.8%, 9.6%, 10.6%, 10.8%, -1.2%, 1.5%, 3.8%,
  6.0%, with impairments and onerous-contract provisions in the project business (AR 2025 note [41]; provisions).

**Why OUT and not TOO HARD.** The returns are known from the filings, so the tenuous-moat reason for TOO HARD ("We don’t
know how to valuate that" **[M2000-019]**) does not apply; Q2's list sends "the standing castle that protects only
ordinary returns" to OUT. The missing rival comparison would refine the picture of the field; it could not raise the
filer's own nine years of returns. A change for the better (ITS at 10.7% in 2024) is credited only over a full cycle,
and the next year fell back to 8.7% **[M2005-020]**, **[L1995-022]**.

- **VERDICT: OUT.** A durable but contested castle (premium brands and installed-base service, strongest in EMEA) that, by
  the filer's own figures over 2017-2025, has protected only ordinary returns, in a field where the filer says rivals with
  cost advantages press the price of the volume segments **[L2007-004]**, **[M2013-052]**, **[M1997-010]**. The file
  closes here; Q3 to Q12 are NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (facts under AFTER THE STOP).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (the balance sheets are in Step 0; facts under AFTER THE STOP).
## Q5 — WHO RUNS IT. NOT REACHED (facts under AFTER THE STOP).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (facts under AFTER THE STOP).

## Q7 — WHAT IS IT WORTH. NOT REACHED as a clearance. The figures below are the owner's reporting figures only.

### COMPUTATION, NOT A CLEARANCE
*(Operator rule 3: valuation arithmetic after a closing STOP carries no entry language. `calc/q7.py`,
`calc/q7_output.txt`.)*
- **Basis.** All-equity (Q7, On what the floor is earned): owner cash before interest on financial debt and after the
  company's own tax, EUR 221.5m (2021-25 average), against market value EUR 4,438.6m plus net financial debt EUR 1,244.1m
  at 2026-06-30 (Q2 2026 report; financial liabilities 1,635.1 less cash 391.0) = **EUR 5,682.7m**. Equity-only beside:
  owner cash after interest, EUR 175.9m, against EUR 4,438.6m. Operating (procurement) leases are left out of net debt
  and their full payments (EUR 217.6m in 2025) are charged inside owner cash, said so. Pensions (net obligation 527.5 at
  2025-12-31) are left out of net debt; their cash payments are inside owner cash.
- **CONVENTION of this run (ours):** the liabilities of the lease business (EUR 4,540.1m) and of the short-term rental
  business (EUR 774.7m) are treated as the finance arm's own funding, like inventory-secured trade finance under Q7's
  convention, and not as net debt, because the filed cash flow statement already charges inside operating cash flow both
  the fleet's growth net of that funding and the interest paid in that business, so counting the principal as debt as
  well would charge it twice; rationale: the speakers keep a finance arm apart from its operations **[L2008-005]**. The
  figures with them counted in net debt are shown beside.
- **Tax.** Owner cash is after taxes actually paid (EUR 250.5m in 2025; group tax rate 32.0%, AR 2025); no carryforward
  that runs out inside ten years was found that would change it; the tax shield on financial-debt interest is ignored in
  the all-equity figure (about EUR 15m a year at 32% on net interest of about EUR 48m; immaterial).
- **The window and the specifics.** (a) *Cycles:* 2022 is a trough the filer itself describes (supply shortages,
  unfinished trucks, working capital -804.5), and 2025's last year is flattered by a working-capital release (+257.8) and
  by efficiency-program costs booked but "not yet" paid (AR 2025, cash flow). The literal window 2021-25 is shown, and the
  eight years 2018-25, which hold the 2020 and 2022 troughs and the recoveries after them, are used as the cycle base.
  (b) *Decline:* the owner-cash series changes sign (2022), so the window's growth is measured between halves; 2021-22
  (-234.3) against 2024-25 (509.4) is meaningless because of the sign change, so the literal window gives the no-growth
  case alone. Across the cycle, the halves 2018-21 (308.6) and 2022-25 (177.2) give a decline of 12.9% a year, carried as
  the bottom. (c) *Acquisitions:* net purchases 2021-25 were EUR 85.7m against owner cash before purchases of 1,193.2m,
  under half: not a serial acquirer; purchases are deducted and no growth is credited. The robotics stake signed on
  2026-07-20 ("low-triple-digit millions of euros", not closed; Q2 2026 report) is left out of the central figure and
  shown beside as if paid from debt and credited nothing. (d) *Working capital* is counted; the window with the average
  working-capital draw added back is shown beside. (e) *Maintenance:* capital spending averaged 403.6 against
  depreciation of 244.7 (segment definition) in 2021-25; the maintenance-only case replaces the first with the second
  (+158.9). The growth that the extra spending bought is not shown in owner cash (no positive growth is measurable), so the
  maintenance-only no-growth case is the top and no growth is credited on top of it. (f) *The cap:* no growth rate above
  the discount rate is carried; owner cash has never exceeded 5.1% of revenue in the years read.
- **Cases** (whole-business values at the sovereign 3.78%, then less net debt 1,244.1, per share on 131.1248m shares; the
  expected return at the price is the rate that equates each case to EUR 5,682.7m):

| Case | Owner cash, start (EUR m) | Growth | Value at 3.78% | Per share | Return at the price |
|---|---|---|---|---|---|
| Bottom: cycle base 2018-25, decline carried | 242.9 | -12.9%/yr ten years, then zero | 2,162.7 | EUR 7.01 | 1.2% |
| Literal window 2021-25, all spending | 221.5 | none (sign change) | 5,859.8 | EUR 35.20 | 3.9% |
| Top: window, maintenance-only | 380.4 | none | 10,063.5 | EUR 67.26 | 6.7% |
| Beside: window, working-capital draw added back, maintenance-only | 476.0 | none | | | 8.4% |
| Beside: top case carried at the 2018-25 revenue growth of 5.06% (double-credits the growth spending) | 380.4 | 5.06%/yr ten years | | | 9.5% |

- **The floor is tested first.** No case, not even the two shown beside that are more generous than the rules allow,
  earns about ten percent at EUR 33.85; the best is 9.5%. On Q7's floor convention the name would close OUT here even had
  Q2 passed **[M2003-149]**. The range EUR 7.01 to 67.26 is 4.7 to 1 wide on whole-business value, which the width test
  does not reach because the floor closes first.
- **The literal window beside:** EUR 35.20 a share, no growth, at 3.78%.

**Reporting figures (a reporting convention, not a rule; neither is a verdict or entry language):**
- **(a) VALUE RANGE: EUR 7.01 to EUR 67.26 a share** (all-equity basis, less net financial debt of EUR 1,244.1m), against
  the price of EUR 33.85; ADR equivalent EUR 1.75 to 16.82 (one ADR = one-fourth of a share), about USD 1.96 to 18.79 at
  EURUSD 1.1177.
- **(b) FAIR PRICE: EUR 9.10 a share, all-equity basis, central** (each end case valued at ten percent: bottom 1,069.7,
  top 3,804.0; averaged 2,436.9; less net debt 1,244.1; after the company's own tax); ADR equivalent EUR 2.27 (about
  USD 2.54). **Equity-only beside: EUR 16.09 a share** (ends on owner cash after interest: cycle base 197.7 declining
  12.9% a year, and window 175.9 plus maintenance 158.9 at no growth; valued at ten percent, 870.6 and 3,348.0, averaged,
  per share), ADR EUR 4.02. The all-equity figure is the central one.
- Beside, not central: with the EUR 494.7m of bond money that the Q2 report says went to repay lease-business
  liabilities taken out of net debt, fair EUR 12.87; with the robotics stake at EUR 100m or 300m added to net debt, fair
  EUR 8.33 or 6.81; with the lease-business and rental liabilities counted in net debt as well, the fair price is
  negative (EUR -31.44) and the range EUR -33.53 to 26.73.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED (facts under AFTER THE STOP).
## Q10 — IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED. (Forklifts, warehouse automation and
their service and finance: no business of the kinds Q12 names.)

---
## THE BOX
**OUT at Q2** (the deciding part, Industrial Trucks & Services, is a standing but contested castle that has protected only
ordinary returns over the 2017-2025 cycle on the filer's own figures; no rival named in the reports, so no rival compared);
integrity facts recorded, not judged. COMPUTATION, not a clearance: value range EUR 7.01 to 67.26 a share against
EUR 33.85; fair price EUR 9.10 all-equity (EUR 16.09 equity-only); no case earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.)*

**Q3, capital.** Capital spending 2021-25 of 333.8, 382.7, 442.8, 462.9, 395.7 against segment depreciation of 202.1,
233.6, 250.2, 248.9, 288.6 (segment reports; cash flow statements). Lease-and-rental fleet growth net of its funding in
operating cash flow: -599.2 (2025) and -543.1 (2024), of which interest paid in that business -213.5 and -226.6 (AR 2025
cash flow statement). Revenue grew 2.35% a year 2021-25 and 5.06% a year 2018-25 (about 5.0% a year 2017-25, the first full Dematic year
included).

**Q4, the accounts.** (1) The company features adjusted EBIT and adjusted EBITDA, which leave out "non-recurring items"
and PPA items; non-recurring items were 42.9 (2019), 65.1 (2020), -37.8 (2021), 31.5 (2022), 37.2 (2023), 27.9 (2024)
and 201.1 (2025) (segment reports): present every year. ITS goodwill in KION ITS Americas was written off in full in
2024 (EUR 22.4m); SCS's 2025 non-recurring items were "predominantly" impairment losses (AR 2025 note [41]). (2) Free
cash flow was redefined from 2026 to add "cash receipts and payments from financial debt used for financing of lease
business", which "increased free cash flow for the reporting period by 494.7 million" in H1 2026 (Q2 2026 report);
H1 2026 free cash flow on the new definition was EUR 22.2m. Procurement-lease payments (EUR 217.6m in 2025) are outside
the company's free cash flow under both definitions. (3) EBITDA is printed and reconciled in every report read. (4)
Inventories rose from 10.0% to 14.4% of revenue, 2017 to 2025.

**Q5, the people (integrity facts, recorded, not judged).** (1) The company publishes an annual outlook with ranges for
revenue, adjusted EBIT, free cash flow and ROCE, firms or raises it during the year, and reports the actual against it:
in 2025 revenue, adjusted EBIT and ROCE landed "within" or "in the middle of" the projected ranges and free cash flow
"slightly higher than the raised target range", the raise explained by efficiency-program costs that would not hit cash
"until the first quarter of 2026" (AR 2025, comparison between actual and forecast performance). (2) The free cash flow
redefinition of 2026 (Q4 above). (3) Executive Board pay (IFRS): EUR 26.1m in 2025 (16.6m in 2024), of which short-term
11.0m and a change in fair value of share-based payments of 13.7m; the long-term plan is phantom shares measured 30% on
total shareholder return against the MDAX, 50% on ROCE and 20% on ESG targets (AR 2025 notes [43], [44]); the proxy-style
remuneration report was not read. These are the habits Q4 carries to Q5; a later run that reaches Q5 must answer them
**[M2013-088]**.

**Q6, the money and the owners.** (1) Share issuance: 9,300,000 shares placed at EUR 64.83 on 2017-05-22 (AR 2017),
13,108,647 shares for EUR 813.3m (EUR 62.04 a share) in December 2020 (AR 2021 note [28]), and a capital increase of
EUR 449.4m in 2016 (AR 2017 cash flow statement); shares in issue rose from about 108.6m to 131.2m (subscribed capital,
EUR 1 a share). (2) No buyback programme found; 73,876 treasury shares. (3) Dividends per share: 0.99 (2017), 1.20
(2018), 0.04 (2019), 0.41 (2020), 1.50 (2021), 0.19 (2022), 0.70 (2023), 0.82 (2024), 0.62 proposed for 2025 (multi-year
overviews). (4) Acquisitions: Dematic in 2016 (EUR 2,118.7m net cash paid); small ITS dealer purchases since; 35.3% of
ZIKOO Smart Technology (China) in April 2026; a robotics and software stake signed 2026-07-20 (Q2 2026 report). (5)
Related parties: Weichai Power and affiliates hold 46.5%; KION bought EUR 100.2m of goods and services from them in
2025 (100.7m in 2024) and sold them EUR 10.1m (27.9m); Weichai received EUR 50.1m of the 2025 dividend (AR 2025 note
[42]). Three Weichai-linked companies are named as the ultimate, intermediate and direct parents.

**Q9, debt and exposures.** Net financial debt EUR 1,244.1m at 2026-06-30 (0.58bn at 2025-12-31); lease-business
liabilities 4,540.1m and short-term rental liabilities 774.7m, funded by "sale-and-leaseback transactions,
securitizations, and dedicated bank loans" and from 2026 by the corporate bond; procurement-lease liabilities 775.1m;
industrial net debt EUR 2,780.7m (Q2 2026 report). The revolving credit facility of EUR 1,385.7m was undrawn at
2025-12-31 (AR 2025). Residual-value and credit risk on the leasing book of about EUR 4.9bn sits with KION.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 5511237d); written question by question; committed after Step 0
      to Q1 and after Q2 (write-early). The Step 0 balance-sheet table was added after Q2 closed, as the template directs,
      and is marked so.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock was held by the dispatching session (a lock
      file was present in `Screens/_daily/` when the run started; not touched). The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the one accidental sighting
      (another company's commit subjects in the session context) is declared under contamination and not used.
- [x] Every v5 id resolves (`calc/check_ids.py`: no E-ids, every M/L/R id in `principle_ledger_v5.csv`, every quoted
      fragment beside an id found in its row). Every filing fact names its report and date; KION has no accession numbers
      (non-SEC filer), as the brief anticipated. The ADR ratio carries the depositary's SEC accession.
- [x] The order was kept; Q2's STOP closed the run; everything after it is headed NOT REACHED or COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost from the filed cash flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the ECB, dated; the price and the FX rate are aggregator quotes, flagged.
- [x] Contrary evidence written down as found (foundations, four items); facts for later questions under AFTER THE STOP,
      with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor applies.
- [x] `tools/run.py` returned nothing for this non-SEC name; nothing of it was used.
- [x] `python tools/check_framework.py` PASS before each commit of the run file.
- Gaps, stated: no rival's filing was read (none named); the 2020 annual report was not read in English; the ITS
  segment's own capital employed is not disclosed, so the Q2 return reading is for the group, with ITS at 83% of
  five-year segment profit; the remuneration report was not read; the IR press-release list could not be read
  (loaded dynamically), so the sweep for events after 2026-07-30 is incomplete.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q2's "standing castle that protects only ordinary returns" asks for the field's returns "on the evidence of the
filer's and the rivals' own filings", while the brief allowed only rivals the company's report names, and KION's reports
name none in eight years. The text does not say what to do when the rival half is empty. I judged on the filer's nine
years alone and said so; another analyst could read the missing half as making the question TOO HARD (WORK). (2) The
same test does not say on which capital "ordinary" is judged: the company's ROCE includes acquisition goodwill (never
above 9.7% pre-tax), while Q3's measure is the capital "actually needed" (17-19% pre-tax on adjusted EBIT in the best
two years, about 5% in cash over the window). The two give different pictures and the text gives no rule for which
governs Q2; I showed both. (3) Q7's net-debt definition ("borrowings and finance leases") has no rule for a captive
leasing business whose funding and interest already sit inside operating cash flow; the inventory-finance convention is
the nearest and I confessed its extension as a CONVENTION of this run. The choice moves the fair price from about EUR 9
to below zero. (4) The business-of-parts threshold needs segment operating profit, but a part's own return on capital
(which Q2's ordinary-returns test needs) is not disclosed by many filers; the text does not say whether the group figure
may stand in for the deciding part.
