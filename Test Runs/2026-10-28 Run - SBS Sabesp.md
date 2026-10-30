# Company Run — Companhia de Saneamento Básico do Estado de São Paulo, SABESP (NYSE: SBS; B3: SBSP3) — 2026-10-28
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, 2026-10-28, after the run was committed (cf7298ee): not held (`PORTFOLIO.md` read for this ticker only).*

**Departures from the canonical brief, as the dispatcher stated them:** the repository path is C:\Projects\BRK; the lines of
evidence are derived by this analyst from the 20-F (Item 4, Item 3.D, Item 5); the filer is a 20-F filer reporting in Brazilian
reais, so the sovereign is Brazil's, from its National Treasury.

**Lines of evidence chosen from the 20-F (Item 4, 3.D, 5), and why:** (1) the URAE-1 concession: term, tariff model,
universalization targets, the Factor U penalty, the termination and compensation terms (Item 4.B, Item 3.D), because the castle
is a contract and a regulator, not a brand; (2) the capital programme (R$70 billion 2024 to 2029 at privatization, R$15.2
billion recorded in 2025) and how it is funded (Item 4.A, Item 5.B), because owner cash is decided by it; (3) the accounting of
the concession under IFRIC 12 (construction revenue at cost, the financial asset of the concession and its IPCA adjustment),
because reported profit departs from cash by billions of reais (Item 5.A, notes 13 to 15, 30); (4) the privatization and the
governance it left (State of São Paulo 18%, Equatorial 15% as reference investor, a golden share, a 30% vote cap), Item 7, Item
3.D; (5) internal control (material weaknesses in 2024 and 2025, Item 15) and the 20-F/A of 2025-09-02; (6) the acquisitions of
2026 (EMAE, Sanessol, Águas de Andradina and Castilho) and the EMAE share merger; (7) water availability (the 2014 to 2015
crisis, Item 3.D). Competitors: the filing names no rival company (Item 4.B, Competition: "we may face competitors" in public
tenders); see Q2.

**Contamination declared:** none of the blind-listed files was opened, listed or searched. The session's context carried the
repository's recent commit subjects (five lines about another company's v5 re-run, CWCO) and the project map; neither concerns
this company, and neither is used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price (aggregator, flagged per operator rule 5; live quotes only):** SBSP3 **R$25.53**, close 2026-10-27 (Yahoo
  Finance chart API; intraday 2026-10-28 R$24.73 at 15:49 UTC). ADS (NYSE: SBS) **US$4.75**, close 2026-10-27 (intraday
  2026-10-28 US$4.59). One ADS represents one common share (20-F cover, "American Depositary Shares, evidenced by American
  Depositary Receipts, each representing one Common Share"; the 1:5 split of 2026 split the ADSs five for one and left the ratio
  unchanged, 20-F Item 4.A, "Approval of Our Share Split"). The two quotes agree at the aggregator's BRL rate of 5.37 per dollar
  (25.53 / 5.37 = 4.75). **Fact written down as found [M1997-127]:** both quotes fell about 21% on 2026-10-26 (SBSP3 R$31.98
  to R$25.27; SBS US$6.40 to US$4.73), the same day the aggregator shows the Ibovespa down about 14% (205,083 to 176,608) and
  the real down about 8% the next day. No 6-K was filed by SBS after 2026-10-21 (EDGAR submissions, checked 2026-10-28). The
  cause is not in any filing read and is not used; no macro conclusion enters **[M2000-094]**.
- **Shares by class:** `python Screens/cover_shares.py SBS` returns the 20-F cover, **700,219,438 common and one preferred
  (golden) share outstanding at 2025-12-31** (20-F filed 2026-04-29, accession 0001292814-26-002681). That count is stale three
  times over: (a) a capitalization of reserves on 2026-03-16 issued 1,132,937 bonus shares (20-F Item 4.A, "Capital Increase",
  704,906,805 common after it); (b) a 1:5 split took effect about 2026-05-04 (20-F Item 4.A); (c) the EMAE share merger. The
  interim statements to 2026-06-30 (6-K filed 2026-08-14, accession 0001292814-26-004252, note 28(a)) give **3,524,534,025
  common shares issued** plus the golden share, and treasury shares of R$472.0 million. The amended bylaws approved 2026-07-30,
  effective on consummation of the merger (6-K filed 2026-09-23, accession 0001292814-26-004674, Article 5; 6-K filed
  2026-10-02, accession 0001292814-26-004840, says they "will become effective at a later date when certain corporate events are
  completed"), give **3,534,409,282 common shares**; the difference, **9,875,257 shares**, is the issue to EMAE's other holders
  at 1.3195 SABESP shares per EMAE share, credited 2026-10-27 (6-K filed 2026-10-21, accession 0001292814-26-004962; no
  withdrawal right was exercised). Treasury: the 20-F Item 16E records 3,452,087 shares bought in October to December 2025 at
  an average R$136.26 (pre-split), which is 17,260,435 after the split, less 126,728 delivered to plan participants in the half
  (note 28(c)), **17,133,707 treasury shares** (derived; purchases after 2026-06-30 under the plan running to 2026-11-12 not
  known). **Shares outstanding used: 3,534,409,282 less 17,133,707 = 3,517,275,575.** Cross-check: the cover count of
  700,219,438 times the bonus ratio 1.00160980 times five, plus 9,875,257, gives 3,516,608,457, within 0.02%.
- **Market cap:** 3,517.3 million × R$25.53 = **R$89,796 million** (about US$16.7 billion at the ADS price).
- **Sovereign for the earnings currency (BRL), issuing authority:** Brazil's National Treasury (Tesouro Nacional), the
  Tesouro Direto price and rate file published on the Treasury's open-data portal (tesourotransparente.gov.br,
  "PrecoTaxaTesouroDireto.csv"), base date 2026-10-27. The longest-dated nominal bond is **Tesouro Prefixado com Juros
  Semestrais (NTN-F) maturing 2037-01-01: 14.93%** (buying rate, morning). The same bond stood at 12.90% on 2026-10-23; it rose
  about two points on 2026-10-26 with the market move above. Inflation-linked bonds (Tesouro IPCA+) are not nominal and are
  not used.
- **Filings read** (operator rule 4): the **20-F for FY2025**, filed 2026-04-29, accession 0001292814-26-002681 (Items 3.D, 4,
  5, 6, 7, 8, 15, 16E, the audited statements); the **20-F/A for FY2024**, filed 2025-09-02, accession 0001292814-25-003200;
  the **20-F for FY2023** (accession 0001292814-24-001825) and **FY2021** (accession 0001292814-22-001850) for the balance
  sheets of 2020 to 2023; the **interim statements to 2026-06-30 and the 2Q26 earnings release** (6-K filed 2026-08-14,
  accession 0001292814-26-004252; 6-K filed 2026-08-13, accession 0001292814-26-004210); the 6-Ks of 2026-07-31
  (0001292814-26-003998), 2026-09-18 (0001292814-26-004598), 2026-09-23 (0001292814-26-004674), 2026-10-02
  (0001292814-26-004840), 2026-10-09 (0001292814-26-004876) and 2026-10-21 (0001292814-26-004962). There is no proxy
  statement for a foreign private issuer; pay is read from 20-F Item 6.B. SEC company facts (XBRL, ifrs-full) for FY2015 to
  FY2024 lines, checked against the filed statements below. **One figure cross-checked against the filed statement:** net cash
  from operating activities FY2024, XBRL R$7,405 million; the FY2025 20-F's cash flow statement prints 7,404,568 thousand for
  2024. Agrees.
- `python tools/run.py SBS` **failed**: "SBS: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (an IFRS 20-F filer;
  the company facts carry no FY2025 values at all). Every figure below is taken from the filed statements, with the XBRL
  company facts used only for FY2015 to FY2024 lines that were checked against a filed statement where they decide anything.
  The arithmetic is in `Test Runs/_research 2026-10-28 SBS/owner_cash.py` and its output file.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the concession's cash will be over decades, not where the quote goes after a 21%
fall in a day **[M1997-109]**. The market serves and does not instruct **[M2006-077]**; the fall of 2026-10-26 is a price, and
"macro conclusions are — just never enter into the discussion" **[M2000-094]**. Abroad the speakers ask a lower price, not a
pass: "So, Brazil would not be off limits at all, but we’d have to be able to get a lot of money into a business we understood
at an attractive price. We would want it to be cheaper than if it were in the United States." **[M2006-021]**. Who is paid to
tell you: the company's release features an "adjusted" EBITDA and earnings per share (Q4). The analyst's habits: look for
"what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) owner cash after
all capital spending has been negative every year from 2021 to 2025 and was R$5.9 billion negative in 2025 (Q4); (2) reported
profit of 2024 and 2025 includes R$9.15 billion and R$1.68 billion of non-cash revenue from the inflation adjustment of the
"financial asset of the concession" (note 30); (3) internal control over financial reporting was not effective at the end of
2024 and of 2025 (Item 15); (4) the FY2024 20-F had to be amended because the total of legal claims was printed as R$167.7
billion instead of R$24.7 billion (20-F/A); (5) the regulator sets the price, and the tariff can be cut by up to 10% a year
by Factor U if the universalization targets are missed, with dividends barred and forfeiture possible (Item 3.D); (6) the
quote fell 21% in a day on no company filing.

## THE STANDING RULE
The buyer would pay cash for a listed minority stake: no borrowed money, no collateral, no option given, so nothing in the
purchase can call on the buyer **[L2014-005]**, **[M2012-081]**. Sizing is the buyer's, and a Brazilian equity priced in reais
adds a currency the buyer does not earn in; that is weighed at Q10, not here. Passes as the buyer's conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as written** **[M1995-051]**, **[M2000-037]**: "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**.
- **What the business is (20-F Item 4):** water supply and sewage collection and treatment to 375 municipalities of the State
  of São Paulo, 371 of them under one regional concession (URAE-1) running to 2060, the rest under four individual contracts;
  one reported operating segment, "the provision of sanitation services" (note 29); substantially all assets and revenue in the
  State of São Paulo. Since January 2026 it also controls EMAE, a hydroelectric generator and water-system operator, bought for
  the Guarapiranga and Billings reservoirs (6-K 0001292814-26-004252, note 4).
- **The key variables and how predictable they are** **[M1998-044]**: (1) **the tariff**, set by a regulator (ARSESP) from a
  regulatory asset base, a pre-tax WACC set at each review, efficient costs, inflation (IPCA) and the Factor U and Factor Q
  adjustments (Item 4.B, "The Concession Agreement for URAE-1"); the model is written in Annex V of the contract and the
  tariff is adjusted every year; (2) **volume**, people and per-capita use, slow-moving, billed volume +1.9% in 2025 (Item 5.A);
  (3) **the capital programme**, R$70 billion over 2024 to 2029 to reach 99% water and 90% sewage coverage by 2029 (Item 3.D),
  after which spending should fall; (4) **the regulator's later choices**, the WACC, the X-factor from the third cycle, how the
  RAB is valued (depreciated replacement cost for new investment); (5) **water**, droughts like 2014 to 2015 (Item 3.D). The
  first, second and fifth are the variables of any water utility; the third is scheduled in the contract; the fourth is the
  regulator's and is the one that cannot be read from the filings ten years out.
- **Abroad** **[M2000-141]**: the governance (no controlling holder, a binding vote between the State and Equatorial on
  reserved matters, a golden share, a 30% vote cap and a 200% premium tender rule, 20-F "Privatization"), the tax (34% statutory
  rate, interest on capital deductible), and the inflation-indexed tariff and debt are all stated in the 20-F and can be
  followed. The speakers did not put Brazil out of bounds; they asked to be paid more for it **[M2006-021]**.
- **Doubt test** **[M2002-092]**: a regulated water monopoly is a business whose economics are read from its contract and its
  accounts; the doubt is about one party (the regulator and the State), and that is a question of the castle's future (Q2)
  and of certainty in the value (Q7), not of whether the business can be understood.
- **VERDICT: IN.** The ten-year economics of a water and sewage concession with a written tariff model can be pictured: a
  regulated return on a growing asset base **[M2012-065]**, **[M2000-037]**; the filing says where the business will stand
  (sole provider in its area to 2060). The regulator's later parameters are carried to Q2 and Q7.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The castle questions** **[M1995-038]**: the key factors are (a) a contract: the URAE-1 concession to 2060, under which a
municipality may leave only after paying "the indemnification amounts owed to us" and a takeover requires "compensation must
be paid prior to termination" for investments not yet amortized (Item 3.D); (b) the pipes: a second water and sewage network
in the same streets is not built; (c) the scale of the system (641 sewage plants, the Cantareira and other reservoirs, Item
4.B). How permanent: the contract runs 34 more years; the threat to it is the grantor and the regulator, not a rival.

- **The money test** **[M2011-015]**: an attacker with R$100 billion could not take these customers. Competition "primarily
  arises through mandatory public tenders for new or renewed sanitation concessions"; within URAE-1 the company serves 371
  municipalities "under a regional concession" (Item 4.B, Competition). The one leak named is large customers on "alternative
  sources" since the 2014 to 2015 crisis (Item 4.B). Passes.
- **Pricing power and the agony before a rise** **[M2005-020]**: the company has none of its own; the regulator prices. The
  record: average tariff +9.56% (2023), +6.45% (2024), +6.47% (2025, effective 2026-01-01) against IPCA of 4.62%, 4.83% and
  4.26% (Item 5, "Effects of Tariff Increases"). Since privatization the State's fund (FAUSP) pays the difference between the
  "equilibrium tariff" and the tariff charged, so the price to users is partly a political choice (Item 5; FAUSP deducted
  R$966 million from 2025 gross revenue, note 30). The tariff tracks inflation plus the asset base; it is not a price the
  customer bids.
- **Unit volume and share of mind** **[M1999-054]**: billed volume +1.9% in 2025, new connections +1.6% (Item 5.A); the
  universalization programme adds connections by contract.
- **The low-cost position and the low bid** **[M2004-091]**: "being a low-cost producer of something that’s essential to
  people, it’s going to be a very good business usually." Water is essential and the customer cannot take a low bid.
- **Ask the competitors** **[M1999-130]**: the filing names no rival company. The rivals of record are other bidders for
  concessions outside URAE-1; inside it there is none.
- **Widening or narrowing** **[M1999-108]**: widened in one way (the 2024 contract replaced hundreds of municipal contracts
  with one regional concession to 2060), and made conditional in another: Factor U cuts the annual tariff by up to 10% if the
  2029 targets are missed, dividends are barred in non-compliance, and two consecutive years of missing a coverage target can
  bring forfeiture, for which compensation is not paid in advance (Item 3.D).
- **What could destroy it, five to fifteen years out** **[M2000-014]**: (1) the regulator or the grantor changing the return:
  "I did not anticipate or even consider the adverse developments in regulatory returns" **[L2023-011]**; (2) a missed
  universalization target, through Factor U and forfeiture; (3) a drought like 2014 to 2015, which the filing lists as a
  material risk; (4) legal challenges to the privatization, which "remain ongoing" (Item 3.D). None of these is a rival taking
  the customers; each is a party to the contract or nature. The filings state the compensation terms that bound the loss on
  termination, so the castle's future can be judged on the contract, with the regulatory climate carried as uncertainty to Q7
  and Q9.
- **The parts table:** one reported segment (note 29). EMAE (electricity generation, consolidated from 2026-01-01) is far
  below half of operating profit (2Q26 EBITDA contribution R$44 million of R$3,906 million, 2Q26 release) and does not decide.

**The competitor row.** The filing names no rival company. **CONVENTION of this run:** three SEC-filing regulated water and
sewage utilities are chosen, American Water Works (AWK), Essential Utilities (WTRG) and California Water Service Group (CWT);
rationale: no Brazilian sanitation company files with the SEC, and these three earn a regulator-set return on a water asset base,
which is the economics in question. The Brazilian state companies a reader would name (Copasa, Sanepar) do not file with the
SEC and are not named by the filing. Metric: net income over average equity, each from its own filings (SEC company facts;
latest 10-K accessions AWK 0001410636-26-000034, WTRG 0000078128-26-000050, CWT 0001628280-26-012444).

| Year | SABESP (BRL, nominal) | AWK | WTRG | CWT |
|---|---|---|---|---|
| 2016 | 20.2% | 9.1% | 13.1% | n/a |
| 2017 | 15.3% | 8.0% | 12.6% | 10.7% |
| 2018 | 15.3% | 10.1% | 9.7% | 9.2% |
| 2019 | 16.4% | 10.4% | 7.6% | 8.4% |
| 2020 | 4.4% | 11.3% | 6.7% | 11.4% |
| 2021 | 9.7% | 18.4% | 8.7% | 9.7% |
| 2022 | 11.9% | 10.9% | 8.8% | 7.7% |
| 2023 | 12.3% | 10.8% | 8.8% | 3.8% |
| 2024 | 28.7% (incl. R$9.15 bn non-cash financial-asset revenue) | 10.4% | 9.8% | 12.4% |
| 2025 | 21.3% (incl. R$1.68 bn of it) | 10.5% | 9.4% | 7.7% |

**The field's returns over the last full cycle, judged in words** **[M1999-108]**: the US water utilities earn about nine to
eleven percent on equity in dollars, year after year, a regulated and ordinary return. SABESP earned ten to sixteen percent
in reais from 2016 to 2023 (2020 the low year at 4.4%), in a currency whose inflation (IPCA) was 4.62%, 4.83% and 4.26% in
2023 to 2025 alone (Item 5), so its real return was ordinary at best; 2024 and 2025 are lifted by a non-cash accounting gain on
the new concession, not by cash. The castle stands, and it protects a regulated, ordinary return. Q2's list of what it rules
OUT names the return set by a regulator as the exception and carries it to Q3 as a second best; the row it rests on: "there’s
no way we get rich on our utility investments. But there’s no way we get poor, either." **[M2009-104]**.

- **VERDICT: IN.** The castle is a legal monopoly by contract to 2060 that no money could attack **[M2011-015]**; the return
  it protects is set by a regulator, and the framework's Q2 carries that case to Q3 rather than closing it OUT. The threat is
  regulatory and political, not competitive, and is carried to Q7 (how sure) and Q9: "I did not anticipate or even consider
  the adverse developments in regulatory returns" **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **The capital actually needed** **[M2010-090]**: concession assets (intangible, contract assets and the financial asset of
  the concession) rose from R$42.4 billion at the end of 2020 to R$83.2 billion at the end of 2025 (filed balance sheets, table
  at Q4); there is no purchased goodwill to set aside **[M2011-060]** until EMAE (R$505 million provisional, 2026).
- **What it earns, operating earnings after depreciation** **[M2014-086]**: operating profit less the non-cash financial-asset
  revenue was about R$6.3 billion in 2023, R$6.4 billion in 2024 and R$10.9 billion in 2025 (income statement, note 30);
  after the 34% statutory rate that is roughly 8.5% (2023) and 10.3% (2025) nominal on capital employed (equity plus
  borrowings and PPP less cash and investments: about R$49 billion and R$70 billion). In a currency whose long government bond
  yields 14.93%, that is a regulated, ordinary return.
- **To stand still and to grow** **[L2000-035]**, **[L1999-024]**: the filing does not split spending into maintenance and
  growth amounts (it names four pillars, "Expansion", "Renewal", "Operational Efficiency" and "Indirect", Item 4.A, without
  figures); the maintenance guess is depreciation and amortization **[M1998-127]**, R$2.2 to 2.8 billion a year, stated as a
  guess **[M2000-144]**. Cash capital spending was R$3.7 billion (2021) and R$13.7 billion (2025), and the company expects
  "close to R$20 billion in CapEx in the year" 2026 (2Q26 release) inside R$70 billion for 2024 to 2029 (Item 4.A). The
  spending is compulsory: missing the 2029 targets cuts the tariff (Factor U), bars dividends above the minimum and can
  bring forfeiture (Item 3.D, Item 8.A). That is the trap the rows name: "you have to spend it the same way if it’s
  unattractive" **[M1998-128]**. Owner cash after all capital spending was negative in each of the five years (Q4).
- **The second best** **[L2009-012]**, **[M2009-104]**: a regulated return is accepted only where it is "decent" on the added
  sums; the regulator's pre-tax WACC is applied to an asset base that, for new investment, is valued at depreciated
  replacement cost (Item 4.B), so the added capital is meant to earn the allowed return. The filing states no WACC figure.
- **WEIGHS AGAINST.** A capital-heavy business in a compulsory spending programme several times its depreciation, whose
  cash after spending is negative and whose return on capital employed is ordinary in its own currency **[M1998-128]**,
  **[L2023-009]**; a regulated return keeps it from the worst grade **[M2009-104]**. (The "little or no debt" criterion is
  applied at Q9, not reached.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first** **[M2025-032]** (R$ million; 2020 to 2025 from the filed statements in the FY2021, FY2023 and
FY2025 20-Fs; 2016 to 2019 from SEC company facts, flagged, not checked against the filed pages; cash includes financial
investments from 2020; concession assets are intangible + contract assets + financial asset of the concession; n/r = not read):

| Year-end | Total assets | Equity | Borrowings | PPP liabilities | Cash + investments | Trade receivables (current) | Concession assets |
|---|---|---|---|---|---|---|---|
| 2016 (XBRL) | 36,745 | 15,419 | 11,964 | n/r | 1,886 (cash only) | n/r | n/r |
| 2017 (XBRL) | 39,546 | 17,513 | 12,101 | n/r | 2,283 (cash only) | n/r | n/r |
| 2018 (XBRL) | 43,565 | 19,552 | 13,153 | n/r | 3,029 (cash only) | n/r | n/r |
| 2019 (XBRL) | 46,458 | 21,636 | 13,245 | n/r | 2,253 (cash only) | n/r | n/r |
| 2020 | 50,419 | 22,794 | 17,259 | 3,175 | 3,808 | 2,204 | 42,375 |
| 2021 | 53,165 | 24,932 | 17,724 | 3,060 | 3,151 | 2,695 | 45,054 |
| 2022 | 57,208 | 27,334 | 18,959 | 2,959 | 3,545 | 3,063 | 47,935 |
| 2023 | 61,471 | 29,857 | 19,536 | 3,287 | 3,265 | 3,584 | 51,406 |
| 2024 | 80,965 | 36,928 | 25,258 | 3,306 | 6,152 | 3,895 | 67,251 |
| 2025 | 104,203 | 42,401 | 40,142 | 3,326 | 12,371 | 4,413 | 83,176 |
| 2026-06-30 (interim) | 119,607 | 45,310 | 51,658 | 3,322 | 17,441 | 3,945 | 92,192 |

What moved and why: borrowings more than doubled from 2023 to mid-2026 (R$19.5 billion to R$51.7 billion) to fund the
capital programme, and cash and investments rose with them (the Blue Bonds and debentures of early 2026 raised ahead of
spending, Item 4.A); equity grew by retention, by R$19.6 billion from 2020 to 2025 with no share issue for cash (the share
count rose only by bonus shares and the split), but R$10.8 billion of 2024 and 2025 pre-tax profit was the non-cash
restatement of the financial asset, so retained "earnings" are partly an accrual to be collected at the end of the
concession in 2060; concession assets jumped by R$15.8 billion in 2024 with no matching cash, when R$9.15 billion of
restatement revenue was recognized on the new contract (note 15, note 30). Receivables grew roughly with sales (R$2.2
billion to R$4.4 billion against sales of R$14.1 billion to R$22.2 billion) and fell in the 2026 half. What the figures
cannot say: the regulator's future return.
- **The real costs.** Depreciation and amortization are real costs **[R1996-023]**; the 2025 charge fell to R$2.2 billion
  from R$2.7 billion as assets moved into the non-amortizing financial asset, so the charge understates what keeps the
  system in place, and the maintenance guess is a guess. Stock pay: a R$145 million long-term incentive programme (Item
  6.B), expensed. EBITDA in the filer's own mouth: the 2Q26 release leads with "Adjusted EBITDA" and "adjusted EPS",
  excluding the construction margin, the financial asset and named non-recurring costs (6-K 0001292814-26-004210): "the
  so-called EBITDA" **[M1998-086]**; an adjusted figure featured **[L2016-006]** is recorded here as a weighing against and
  carried to Q5 **[M1994-018]**. No earnings guidance found; capital-spending guidance (R$20 billion for 2026) is given.
- **Revenue far from cash.** The financial asset's IPCA restatement is booked as operating revenue (R$9,151 million in 2024,
  R$1,676 million in 2025, R$818 million in the 2026 half), and in December 2025 a change of estimate added "the additional
  amount of R$ 1 billion in financial assets, increasing, in the same amount, the operating revenue" (note 15). The rows
  warn where revenue and expenses are not "matched up on something close to cash in the short-term" **[M1995-065]**, and
  of "the most optimistic interpretation" **[M1994-079]**. The item is explained in a note, follows a regulator's letter
  (ARSESP Official Letter No. 180/2025), is attested by the auditor, and the company removes it from its own adjusted
  figures; it is recast out here by working from cash. It weighs against; it does not confuse.
- **Control and care.** Internal control over financial reporting was not effective at the 2024 and the 2025 year-ends
  (information technology general controls and information produced by the entity; no misstatement found, Item 15); the
  FY2024 20-F printed the total of legal claims as "R$167.7 billion" instead of "R$24.7 billion" and was amended (20-F/A,
  accession 0001292814-25-003200). "When managements take the low road in aspects that are visible, it is likely they are
  following a similar path behind the scenes." **[L2002-039]**: the visible faults here are control and care, not a low
  road in the numbers; recorded as a weighing.
- **The recast (owner cash, R$ million, equity-only: operating cash after interest and tax paid; `owner_cash.py`):**

| Year | Operating cash | Cash capital spending | PPP and program payments | D&A (maintenance guess) | Owner cash after all spending | Owner cash after maintenance only | Sales (ex construction, ex financial asset) |
|---|---|---|---|---|---|---|---|
| 2021 | 3,914 | 3,747 | 701 | 2,253 | -534 | 960 | 15,114 |
| 2022 | 3,968 | 3,624 | 606 | 2,451 | -263 | 910 | 17,192 |
| 2023 | 4,854 | 4,139 | 755 | 2,791 | -39 | 1,308 | 19,972 |
| 2024 | 7,405 | 8,031 | 605 | 2,677 | -1,231 | 4,123 | 21,726 |
| 2025 | 8,361 | 13,740 | 480 | 2,209 | -5,860 | 5,672 | 22,213 |
| **5-yr avg** | | | | | **-1,586** | **2,595** | |

  2021 and 2022 sales are total revenue less construction revenue from the company facts (those years had no financial
  asset); 2023 to 2025 are the filer's own figures (note 30, Item 5.A). 2025 operating cash includes a R$1.5 billion fall in
  trade receivables, which the filer ties to the recognition of court-ordered payments (precatórios) from the City of São
  Paulo (Item 5.A): a working-capital release, not a recurring inflow.
- **VERDICT on the accounts: WEIGHS AGAINST** (not a STOP). The accounts are understood once recast to cash: the IFRIC 12
  construction revenue is at cost, the financial asset is an IPCA-indexed claim to be paid in 2060 and is taken out, and the
  cash flow statement carries interest paid in operations (note 35). Nothing found reads as suspicion that the statements
  themselves raise **[M1995-065]**; the weighings against (non-cash revenue booked by estimate, two years of ineffective
  control, a careless amendment, adjusted figures featured) are carried to Q5 **[M1994-018]**, **[L2016-006]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**: the management came in with privatization (CEO Carlos Piani from 2024-10-01; CFO
  Daniel Szlak from 2024-10-02; Item 6.A). The hand dealt: a state company with a compulsory programme to 2029. What they
  have done in two years: billed volume up, average employees down 11% through a dismissal programme, administrative expense
  down by more than half in 2025, capital spending more than tripled (Item 5.A); "We are confident in delivering U-Factor
  targets for the year" (2Q26 release). The CEO's earlier record includes a utility operator (Equatorial Energia, CEO and CFO
  2004 to 2010), a SPAC, Kraft Heinz Canada and PDG Realty (Item 6.A). Two years at SABESP is too short a record to grade
  **[M1996-038]**.
- **How they treat the owners; the proxy** **[M1994-009]**: no proxy for a foreign issuer; Item 6.B shows total pay for the
  board, executives and fiscal council of R$63.1 million in 2025 against R$11.3 million in 2024 and R$10.5 million in 2023,
  the executives' bonus and share pay R$39.5 million of R$49.3 million; R$71.2 million approved for 2026. The long-term plan
  pays in shares on time (restricted shares, eight-year vesting for the CEO) and on Factor U and total shareholder return
  (performance shares). Factor U is under the managers' control **[M2003-019]**; total shareholder return is the quote.
- **The letters and reports** **[M1998-036]**: the 20-F is full and plain on the contract, the risks and the control
  failures; the release leads with adjusted figures (Q4).
- **Integrity, the habits carried from Q4** **[M2013-088]**: no make-the-numbers habit found (no earnings guidance); the
  adjusted figures are reconciled line by line in the release; the financial-asset estimate is disclosed with its regulator
  letter; the control weaknesses are disclosed by management with a remediation plan. Sweep of the 20-F (Item 3.D, Item 8.A,
  Item 16B) for findings against these officers: none found; the privatization's legal challenges are suits against the
  State's sale, not against the managers. No doubt about honesty is raised by what was read.
- **VERDICT on integrity: IN** (no doubt found on the record read **[M2013-088]**); **ability: WEIGHS FOR, lightly**, on two
  years of execution against a compulsory programme, with the record too short to grade **[M1996-038]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**: equity rose R$19.6 billion from 2020 to 2025; market value
  rose from about R$30 billion at the end of 2020 (aggregator split-adjusted close R$8.62 times about 3,524 million share
  equivalents) to R$89.8 billion, so the market leg passes. Against intrinsic value **[R2009-002]** it fails: retained
  earnings include R$10.8 billion of non-cash restatement, owner cash after spending was negative in every year, and Q7 puts
  the value far below the quote. Forward, the business cannot fund itself from its own cash (Q3), and the dividend policy
  ties payouts above the 25% minimum to Factor U and to a leverage ratio at or below 3.25 (Item 8.A).
- **Buybacks** **[L1999-023]**: 3,452,087 shares (pre-split) bought October to December 2025 at an average R$136.26, about
  R$27.25 a share after the split; the stated purpose is "to efficiently manage our capital structure and to meet
  obligations arising from share-based incentive plans" (Item 16E). No price limit was named **[L2016-002]**; buying in to
  cover incentive plans is the reason the rows reject: "That actually isn’t the best reason to buy in shares." **[M2014-008]**;
  and the business spent beyond its own cash that year. **Q7 line written back:** the prices paid sit far above the bottom
  of the Q7 range (R$4.94, equity-only, at the sovereign). **Weighs against.**
- **Issuance and deals** **[L2014-012]**: EMAE was bought mostly for cash (R$682.6 million for control; R$567.7 million,
  R$171.6 million and R$7.1 million for minority blocks; R$484.4 million above carrying value charged to retained earnings;
  interim note 4), and the remaining minority by issuing 9,875,257 SABESP shares. Classed by the larger part paid, an
  acquisition for cash; the share leg is not the all-stock deal of the STOP, and by Q7 SABESP's stock is not undervalued,
  so **[L2009-019]** does not apply. Value got: EMAE's 2Q26 contribution was R$44 million of EBITDA and R$77 million of net
  income, much of it financial income (2Q26 release). Undecided as value given against value got.
- **Part B, pay and the board** **[M2003-019]**, **[L1994-020]**: pay rose about five-fold with privatization; the
  performance plan is tied in part to what the managers control (Factor U) and in part to the quote (TSR). Board of nine:
  three named by Equatorial, three by the State, three independents named jointly (20-F, "Privatization"); the reference
  investor must bring its Brazilian water opportunities to SABESP; the State keeps a golden share. **Undecided.**
- **WEIGHS AGAINST** on Part A (a buyback with no price, for incentive plans, far above value; retention that does not pass
  against value); Part B undecided.

## Q7 — WHAT IS IT WORTH? STOP.
- **The definition** **[R1996-018]**: the cash that can be taken out, discounted at the long government rate **[L2000-021]**,
  no risk premium in the rate **[M1996-024]**; the rate is Brazil's, 14.93% on the NTN-F 2037 (Step 0).
- **Basis: the regulated utility** **[L2017-012]**, **[M2010-037]**: the one segment earns a return a regulator allows on its
  asset base, so the **equity-only basis is central**: owner cash after interest and the company's tax, against the market
  value of the shares. The **all-equity basis** is beside. Net debt at 2026-06-30 (consolidated interim): borrowings
  R$51,658 million + PPP liabilities R$3,322 million + derivative liabilities R$2,294 million (the swaps on the foreign debt,
  counted with it) less cash and financial investments R$17,441 million = **R$39,833 million**; leases are inside
  borrowings as the filer presents them (note 17(b)); no subsequent event stated by the filings changes it except the share
  merger (shares only).
- **The cash input** (Q4 recast): five-year average owner cash after maintenance only, **R$2,595 million** (central, specific
  (e): the filing allows the maintenance guess); after all spending **-R$1,586 million** (beside). Working capital is inside
  operating cash (specific (d)). The window 2021 to 2025 is used as written: the 2024 change (new contract, privatization)
  is a change of regime, not a cyclical peak or trough, and the filer does not describe an end year as aberrational in the
  sense of specific (a). The post-privatization bases are shown beside; they do not change the close.
- **Growth** (specific (f)): owner cash after maintenance grew 55.9% a year from 2021 to 2025 (960 to 5,672); carried ten
  years it would require owner cash of 379% of sales against a highest share seen of 25.5% (2025), an absurdity **[M1999-067]**;
  cut to the business's own sales growth, **10.1% a year** (15,114 to 22,213), below the discount rate. The base years are
  read with **[L2005-003]** in mind: 2021 to 2023 were years of the old regime.
- **Growth spending and the utility debt credit** (specific (e); The regulated utility): growth spending = cash capital
  spending less the maintenance guess, window average **R$4,180 million**, grown at 10.1% for ten years (year one R$4,180
  million, year ten R$9,941 million), none after. Long-term debt (borrowings plus PPP liabilities) rose from R$20,434
  million (2020) to R$43,468 million (2025), **R$4,607 million a year**; the filing states no allowed debt share, so the cap
  is the business's own long-term debt share of long-term capital at 2026-06-30, **54.8%**, which caps the credit at
  R$2,292 million against R$4,180 million of growth spending: **credit R$2,292 million** in year one, R$5,450 million in
  year ten, stopping with the spending.
- **Value range (equity-only, central, at the sovereign 14.93%): R$4.94 (no growth) to R$5.21 (growth case) a share,
  against R$25.53.** Width 1.05 to 1. Beside it: the growth case without the debt credit, R$0.50; owner cash after all
  spending, not positive; the **all-equity basis, not positive** (R$-4.13 to R$-6.68 a share at the sovereign: maintenance
  owner cash before interest after tax, R$3,777 million, valued as a whole business, is worth less than the net debt).
  Post-privatization bases, beside and not cases of the convention: 2024 to 2025 average (R$4,897 million) R$9.33 to
  R$13.27; trailing twelve months to 2026-06-30 (R$5,209 million) R$9.92 to R$14.37; 2025 alone (R$5,672 million, which
  carries the R$1.5 billion receivables release) R$10.80 to R$15.99. Every one of them tops out below the price.
- **The floor, tested first** (CONVENTION, about ten percent, **[M2003-149]**): on the central cash, the expected return at the
  price is 5.2% in the growth case and the owner-cash yield is 2.9% in the no-growth case: **no case earns the floor at the
  price**. On the most favorable base beside (2025 alone) the growth case would return 10.6% at the price; the price then
  still sits above the top of that range at the sovereign (R$15.99), which closes OUT however wide the range, and the bond
  at 14.93% beats it (a fact for Q8, not reached).
- **Closes: OUT.** No case earns the floor at the price **[M2003-149]**; the price is about five times the top of the
  central range, the opposite of a screamer **[M2009-005]**; and the regulatory climate the rows warn of **[L2023-011]** and
  the foreign setting where the speakers asked to be paid more **[M2006-021]** would widen the margin asked, not narrow it
  **[M1997-080]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged,
  after the company's own tax. **Equity-only (central for the regulated utility): R$8.67 a share** (no-growth R$7.38,
  growth R$9.96 at ten percent), about US$1.61 an ADS at the aggregator's 5.37. **All-equity (beside): not positive
  (R$-0.56).** No cheap price is reported. Growth spending R$4,180 million in year one, R$9,941 million in year ten, none
  after; utility debt credit: long-term debt increase R$4,607 million a year, credited against growth spending only, cap
  54.8% (the business's own long-term debt share of long-term capital at 2026-06-30; the filing states no allowed share),
  credit R$2,292 million in year one.
- **VERDICT: OUT**, with **[M2003-149]**, **[M2009-005]**, **[L2013-012]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7** (price): value range R$4.94 to R$5.21 a share (equity-only, central for the regulated utility, at the 14.93%
Brazilian sovereign) against R$25.53 (US$4.75 an ADS); no case earns the floor at the price; fair price R$8.67
equity-only, not positive all-equity.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, with sources **[M1997-127]**; no verdict; the box unchanged.)*
- **Q8, the bond:** the NTN-F 2037 yields 14.93% (Tesouro Direto file, 2026-10-27); the equity-only owner-cash yield on the
  market value is 2.9% on the window base and 6.3% on 2025 alone.
- **Q9, debt and exposures:** net debt R$39.8 billion at 2026-06-30 including PPP and derivative liabilities; borrowings
  R$51.7 billion, of which foreign-currency loans and the US$1.35 billion Blue Bonds (5.750% due 2031 and 6.500% due 2036,
  issued 2026-02-03) are swapped to reais (Item 5: swaps "to fully protect us against a devaluation of the real"); R$6.3
  billion of debentures issued 2026-02-10 at IPCA plus 6.25% to 6.35% and CDI plus 0.64% to 0.72% (Item 4.A); financial
  covenants that limit indebtedness (Item 3.D, Item 5.B); dividends above the minimum only with leverage at or below 3.25
  (Item 8.A); legal claims of R$18.2 billion, R$1.9 billion provisioned (Item 3.D); pension obligations R$2.4 billion
  (interim); one concession carries almost all revenue, so one drought or one regulatory decision reaches the whole company
  (Item 3.D, the 2014 to 2015 crisis); interest paid rose from R$845 million (2021) to R$2,696 million (2025) and R$1,914
  million in the 2026 half.
- **Q10:** an asset in reais for a buyer who does not earn reais; the quote fell 21% on 2026-10-26 with no company filing.
- **Q12:** water and sewage to 375 municipalities, with universalization to poor and rural areas required by contract;
  nothing named by the rows.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch: yes. Committed after each question: **no, partly.** Commits were the
      template copy with framework notes; Step 0 to Q2 together; Q3 to Q7, the box and the self-audit together. Q3 to Q6 were
      drafted after the Q7 arithmetic was run, in one pass, and not committed one by one; a crash in that pass would have
      lost them. The order of the answers in the file is the framework's order, and no later finding changed an earlier verdict.
- [ ] Operator rule 3: the valuation arithmetic (`owner_cash.py` and its output) was run before Q4 was written, and its
      output file in the research folder is not headed COMPUTATION, NOT A CLEARANCE. Declared here; it carries no entry
      language, and Q4 closed as a weighing, not a STOP, so no figure was reported past a failed STOP.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock in `Screens/_daily/` was present, written
      2026-10-28T12:00:01 by the dispatching session (I only read that it exists); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident: the five recent
      commit subjects in the session's start-up context (another company, CWCO) and the project map in `CLAUDE.md`;
      declared at the top, not used.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check_ids.py` in the research folder);
      every filing fact has its accession; numbers carry a filing or a CONVENTION.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 are NOT REACHED.
- [x] Owner cash from operating cash less capital spending and PPP payments, never a net-income proxy (operator rule 5);
      the sovereign from Brazil's National Treasury, dated; aggregator quotes flagged.
- [x] Contrary evidence written down as found (Foundations, Q4); facts for later questions under AFTER THE STOP.
- [x] No point-in-time anchor; no row barred by date.
- [x] `tools/run.py` failed on this IFRS filer (message quoted at Step 0); nothing it printed was used.
- [x] `python tools/check_framework.py` run before the final commit: **PASS** (2026-10-28). `check_ids.py` in the research
      folder: 69 distinct ids, 91 citations, no E-ids, every id in `principle_ledger_v5.csv`, every quoted fragment beside an
      id found in its row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The floor below the sovereign.** The floor convention is "about ten percent", while Q7 values at the long government
rate, here 14.93%. The text's line that a price above the top of the range closes OUT "through the floor convention above,
the expected return at the price then being below the minimum" assumes the sovereign is below the floor. On one base beside
(2025 alone) the growth case returns 10.6% at the price, above the floor, while the price sits above the top of the range at
the sovereign. The close did not depend on it (the central case fails the floor), but the text does not say whether the floor
moves with a lasting long rate above it, as its first statement suggests (**[M1994-004]**, "in a world of 7 percent long-term
bond rates"), or whether Q8's bond filter is meant to do that work. (2) **A window that straddles a change of regime.**
Specific (a) covers cycles and end years aberrational "on the filer's own description"; it says nothing of a business whose
contract, owner and tariff model changed in the middle of the window (privatization, July 2024). I kept the five-year window
and showed the post-privatization bases beside; the box is the same on every base. (3) **The utility debt credit**: with no
allowed debt share in the filing the fallback worked as written, but it is not said whether PPP liabilities (finance-lease-
like) and swap liabilities on foreign debt are "long-term debt" for the credit; I counted PPP liabilities in the credit and
the swaps only in net debt, and said so. (4) **The maintenance guess under IFRIC 12**: depreciation fell in 2025 because
assets moved into a non-amortizing financial asset, so depreciation as the guess understates maintenance for this
accounting; the text gives no instruction. (5) `tools/run.py` and the SEC company facts carry nothing for FY2025 for this IFRS
filer, so every figure was typed from the filings, as the brief anticipated.
